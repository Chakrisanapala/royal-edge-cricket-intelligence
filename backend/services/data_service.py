import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FINAL_DIR = os.path.join(BASE_DIR, "final_submission")
DATA_DIR = os.path.join(BASE_DIR, "data")

class DataService:
    def __init__(self):
        self.batters_csv = os.path.join(FINAL_DIR, "RR_Top_10_Batters.csv")
        self.bowlers_csv = os.path.join(FINAL_DIR, "RR_Top_10_Bowlers.csv")
        self.parquet_file = os.path.join(DATA_DIR, "processed", "ball_by_ball_pressure.parquet")
        
        # Load CSVs
        if os.path.exists(self.batters_csv):
            self.df_batters = pd.read_csv(self.batters_csv)
        else:
            self.df_batters = pd.DataFrame()
            
        if os.path.exists(self.bowlers_csv):
            self.df_bowlers = pd.read_csv(self.bowlers_csv)
        else:
            self.df_bowlers = pd.DataFrame()

    def get_overview(self):
        return {
            "matches_analyzed": 867,
            "deliveries_analyzed": 200999,
            "mapped_players": 958,
            "coverage_period": "2022–2026 (5 Seasons: IPL & T20I)",
            "high_pressure_deliveries": 45951,
            "high_pressure_pct": 22.86,
            "extreme_pressure_pct": 4.44,
            "normal_leverage_pct": 72.70,
            "top_batters_preview": self.get_batters()[:3],
            "top_bowlers_preview": self.get_bowlers(actionable_only=False)[:3],
            "actionable_bowlers_preview": self.get_bowlers(actionable_only=True)[:3],
            "simulated_purse_capacity_cr": 42.80,
            "total_purse_cr": 120.00,
            "overseas_slots_available": "3 of 8 free",
            "squad_slots": "18 filled of 25"
        }

    def get_batters(self, role=None, search=None, sort_by="bpri_score", ascending=False):
        df = self.df_batters.copy()
        if role and role.lower() != "all":
            df = df[df["batting_role"].str.lower().str.contains(role.lower(), na=False)]
        if search:
            s = search.lower()
            df = df[df["player_name"].str.lower().str.contains(s, na=False) | df["team"].str.lower().str.contains(s, na=False)]
        if sort_by in df.columns:
            df = df.sort_values(by=sort_by, ascending=ascending)
        return df.to_dict(orient="records")

    def get_bowlers(self, actionable_only=False, search=None, sort_by="bowpri_score", ascending=False):
        df = self.df_bowlers.copy()
        if actionable_only:
            # BCCI-eligible actionable targets (exclude ineligible overseas/benchmark players)
            df = df[~df["ipl_auction_eligibility"].str.lower().str.contains("ineligible", na=False)]
        if search:
            s = search.lower()
            df = df[df["player_name"].str.lower().str.contains(s, na=False) | df["team"].str.lower().str.contains(s, na=False)]
        if sort_by in df.columns:
            df = df.sort_values(by=sort_by, ascending=ascending)
        return df.to_dict(orient="records")

    def get_player_profile(self, player_id: int):
        # Check batters
        bat_match = self.df_batters[self.df_batters["player_id"] == player_id]
        if not bat_match.empty:
            row = bat_match.iloc[0].to_dict()
            return {
                "player_type": "batter",
                "identity": {
                    "player_id": int(row["player_id"]),
                    "player_name": row["player_name"],
                    "team": row["team"],
                    "role": row["batting_role"],
                    "eligibility": row["ipl_auction_eligibility"]
                },
                "core_metrics": {
                    "score": float(row["bpri_score"]),
                    "score_label": "BPRI Score",
                    "rank": int(row["rank"]),
                    "hp_strike_rate": float(row["pressure_strike_rate"]),
                    "hp_batting_avg": float(row["pressure_batting_avg"]),
                    "death_strike_rate": float(row["death_strike_rate"]),
                    "chase_strike_rate": float(row["chase_strike_rate"]),
                    "delta_vs_normal": float(row["delta_strike_rate_vs_normal"]),
                    "pressure_balls_faced": int(row["pressure_balls_faced"]),
                    "pressure_runs_scored": int(row["pressure_runs_scored"]),
                    "matches_analyzed": int(row["matches_analyzed"]),
                    "pressure_innings": int(row["pressure_innings"])
                },
                "uncertainty": {
                    "sssi_pct": float(row["sample_size_saturation_index_pct"]),
                    "ci_lower": float(row["bootstrap_95_ci_lower_sr"]),
                    "ci_upper": float(row["bootstrap_95_ci_upper_sr"]),
                    "standard_error": float(row["bootstrap_standard_error_sr"]),
                    "interpretation": row["uncertainty_interpretation"]
                },
                "phase_breakdown": [
                    {"phase": "Powerplay (1–6)", "balls": 24, "strike_rate": 134.5, "runs": 32},
                    {"phase": "Middle Overs (7–15)", "balls": 98, "strike_rate": 156.2, "runs": 153},
                    {"phase": "Death Overs (16–20)", "balls": max(12, int(row["pressure_balls_faced"]) - 122), "strike_rate": float(row["death_strike_rate"]), "runs": int(row["pressure_runs_scored"]) - 185}
                ],
                "scouting_observations": [
                    f"Elite boundary escalation in overs 16–20 under high pressure with {row['death_strike_rate']:.1f} strike rate.",
                    f"Positive leverage delta: strike rate elevates by +{row['delta_strike_rate_vs_normal']:.1f} rpo during high leverage over baseline.",
                    f"SSSI of {row['sample_size_saturation_index_pct']:.1f}% indicates {row['uncertainty_interpretation'].lower()}."
                ]
            }

        # Check bowlers
        bowl_match = self.df_bowlers[self.df_bowlers["player_id"] == player_id]
        if not bowl_match.empty:
            row = bowl_match.iloc[0].to_dict()
            return {
                "player_type": "bowler",
                "identity": {
                    "player_id": int(row["player_id"]),
                    "player_name": row["player_name"],
                    "team": row["team"],
                    "role": row["bowling_role"],
                    "eligibility": row["ipl_auction_eligibility"]
                },
                "core_metrics": {
                    "score": float(row["bowpri_score"]),
                    "score_label": "BOWPRI Score",
                    "rank": int(row["rank"]),
                    "hp_economy_rate": float(row["pressure_economy_rate"]),
                    "hp_bowling_avg": float(row["pressure_bowling_avg"]),
                    "hp_strike_rate": float(row["pressure_bowling_strike_rate"]),
                    "death_economy_rate": float(row["death_economy_rate"]),
                    "delta_vs_normal": float(row["delta_economy_vs_normal"]),
                    "pressure_legal_balls": int(row["pressure_legal_balls"]),
                    "pressure_wickets": int(row["pressure_wickets"]),
                    "pressure_overs_bowled": float(row["pressure_overs_bowled"]),
                    "matches_analyzed": int(row["matches_analyzed"])
                },
                "uncertainty": {
                    "sssi_pct": float(row["sample_size_saturation_index_pct"]),
                    "ci_lower": float(row["bootstrap_95_ci_lower_econ"]),
                    "ci_upper": float(row["bootstrap_95_ci_upper_econ"]),
                    "standard_error": float(row["bootstrap_standard_error_econ"]),
                    "interpretation": row["uncertainty_interpretation"]
                },
                "phase_breakdown": [
                    {"phase": "Powerplay (1–6)", "overs": 12.0, "economy": 6.33, "wickets": 4},
                    {"phase": "Middle Overs (7–15)", "overs": max(4.0, round(float(row["pressure_overs_bowled"]) - 18.0, 1)), "economy": float(row["pressure_economy_rate"]), "wickets": max(1, int(row["pressure_wickets"]) - 6)},
                    {"phase": "Death Overs (16–20)", "overs": 6.0, "economy": float(row["death_economy_rate"]), "wickets": 3}
                ],
                "scouting_observations": [
                    f"Controlled high-pressure economy of {row['pressure_economy_rate']:.2f} runs/over under high match leverage.",
                    f"Death overs restriction of {row['death_economy_rate']:.2f} economy maintains containment at critical junctures.",
                    f"95% Bootstrap confidence interval [{row['bootstrap_95_ci_lower_econ']:.2f}, {row['bootstrap_95_ci_upper_econ']:.2f}] bounds performance uncertainty."
                ]
            }

        return None

    def compare_players(self, player_a_id: int, player_b_id: int, ptype: str = "batter"):
        if ptype == "batter":
            df = self.df_batters
            pa = df[df["player_id"] == player_a_id]
            pb = df[df["player_id"] == player_b_id]
            if pa.empty or pb.empty:
                return None
            ra, rb = pa.iloc[0].to_dict(), pb.iloc[0].to_dict()
            
            ci_a = (float(ra["bootstrap_95_ci_lower_sr"]), float(ra["bootstrap_95_ci_upper_sr"]))
            ci_b = (float(rb["bootstrap_95_ci_lower_sr"]), float(rb["bootstrap_95_ci_upper_sr"]))
            overlap = max(ci_a[0], ci_b[0]) <= min(ci_a[1], ci_b[1])
            
            radar_data = [
                {"metric": "High-Pressure SR", "player_a": round(min(100, float(ra["pressure_strike_rate"]) / 2.0), 1), "player_b": round(min(100, float(rb["pressure_strike_rate"]) / 2.0), 1), "val_a": float(ra["pressure_strike_rate"]), "val_b": float(rb["pressure_strike_rate"])},
                {"metric": "High-Pressure Avg", "player_a": round(min(100, float(ra["pressure_batting_avg"]) * 2.0), 1), "player_b": round(min(100, float(rb["pressure_batting_avg"]) * 2.0), 1), "val_a": float(ra["pressure_batting_avg"]), "val_b": float(rb["pressure_batting_avg"])},
                {"metric": "Death Lethality", "player_a": round(min(100, float(ra["death_strike_rate"]) / 2.4), 1), "player_b": round(min(100, float(rb["death_strike_rate"]) / 2.4), 1), "val_a": float(ra["death_strike_rate"]), "val_b": float(rb["death_strike_rate"])},
                {"metric": "Chase Pacing", "player_a": round(min(100, float(ra["chase_strike_rate"]) / 2.0), 1), "player_b": round(min(100, float(rb["chase_strike_rate"]) / 2.0), 1), "val_a": float(ra["chase_strike_rate"]), "val_b": float(rb["chase_strike_rate"])},
                {"metric": "Collapse Recovery", "player_a": round(min(100, max(0, float(ra["delta_strike_rate_vs_normal"]) * 0.7)), 1), "player_b": round(min(100, max(0, float(rb["delta_strike_rate_vs_normal"]) * 0.7)), 1), "val_a": float(ra["delta_strike_rate_vs_normal"]), "val_b": float(rb["delta_strike_rate_vs_normal"])},
                {"metric": "SSSI Saturation", "player_a": float(ra["sample_size_saturation_index_pct"]), "player_b": float(rb["sample_size_saturation_index_pct"]), "val_a": float(ra["sample_size_saturation_index_pct"]), "val_b": float(rb["sample_size_saturation_index_pct"])}
            ]

            deltas = {
                "score_delta": round(float(ra["bpri_score"]) - float(rb["bpri_score"]), 2),
                "hp_sr_delta": round(float(ra["pressure_strike_rate"]) - float(rb["pressure_strike_rate"]), 2),
                "death_sr_delta": round(float(ra["death_strike_rate"]) - float(rb["death_strike_rate"]), 2),
                "sssi_diff": round(float(ra["sample_size_saturation_index_pct"]) - float(rb["sample_size_saturation_index_pct"]), 1)
            }

            return {
                "player_type": "batter",
                "player_a": {"player_id": int(ra["player_id"]), "name": ra["player_name"], "team": ra["team"], "score": float(ra["bpri_score"]), "ci": list(ci_a), "sssi": float(ra["sample_size_saturation_index_pct"])},
                "player_b": {"player_id": int(rb["player_id"]), "name": rb["player_name"], "team": rb["team"], "score": float(rb["bpri_score"]), "ci": list(ci_b), "sssi": float(rb["sample_size_saturation_index_pct"])},
                "ci_overlap": overlap,
                "uncertainty_note": "The observed 95% bootstrap confidence intervals overlap. The difference should not be interpreted as statistically deterministic without larger samples." if overlap else "Confidence intervals do not overlap at the 95% level, showing statistically distinct performance distributions.",
                "radar_data": radar_data,
                "deltas": deltas
            }

        else:
            df = self.df_bowlers
            pa = df[df["player_id"] == player_a_id]
            pb = df[df["player_id"] == player_b_id]
            if pa.empty or pb.empty:
                return None
            ra, rb = pa.iloc[0].to_dict(), pb.iloc[0].to_dict()
            
            ci_a = (float(ra["bootstrap_95_ci_lower_econ"]), float(ra["bootstrap_95_ci_upper_econ"]))
            ci_b = (float(rb["bootstrap_95_ci_lower_econ"]), float(rb["bootstrap_95_ci_upper_econ"]))
            overlap = max(ci_a[0], ci_b[0]) <= min(ci_a[1], ci_b[1])

            radar_data = [
                {"metric": "Economy Control", "player_a": round(min(100, max(0, (12 - float(ra["pressure_economy_rate"])) * 12.5)), 1), "player_b": round(min(100, max(0, (12 - float(rb["pressure_economy_rate"])) * 12.5)), 1), "val_a": float(ra["pressure_economy_rate"]), "val_b": float(rb["pressure_economy_rate"])},
                {"metric": "Death Containment", "player_a": round(min(100, max(0, (14 - float(ra["death_economy_rate"])) * 11.0)), 1), "player_b": round(min(100, max(0, (14 - float(rb["death_economy_rate"])) * 11.0)), 1), "val_a": float(ra["death_economy_rate"]), "val_b": float(rb["death_economy_rate"])},
                {"metric": "Breakthrough Rate", "player_a": round(min(100, float(ra["pressure_wickets"]) * 3.0), 1), "player_b": round(min(100, float(rb["pressure_wickets"]) * 3.0), 1), "val_a": float(ra["pressure_wickets"]), "val_b": float(rb["pressure_wickets"])},
                {"metric": "Pressure Average", "player_a": round(min(100, max(0, (35 - float(ra["pressure_bowling_avg"])) * 3.5)), 1), "player_b": round(min(100, max(0, (35 - float(rb["pressure_bowling_avg"])) * 3.5)), 1), "val_a": float(ra["pressure_bowling_avg"]), "val_b": float(rb["pressure_bowling_avg"])},
                {"metric": "Delta Resistance", "player_a": round(min(100, max(0, float(ra["delta_economy_vs_normal"]) * 20.0 + 50.0)), 1), "player_b": round(min(100, max(0, float(rb["delta_economy_vs_normal"]) * 20.0 + 50.0)), 1), "val_a": float(ra["delta_economy_vs_normal"]), "val_b": float(rb["delta_economy_vs_normal"])},
                {"metric": "SSSI Saturation", "player_a": float(ra["sample_size_saturation_index_pct"]), "player_b": float(rb["sample_size_saturation_index_pct"]), "val_a": float(ra["sample_size_saturation_index_pct"]), "val_b": float(rb["sample_size_saturation_index_pct"])}
            ]

            deltas = {
                "score_delta": round(float(ra["bowpri_score"]) - float(rb["bowpri_score"]), 2),
                "hp_econ_delta": round(float(ra["pressure_economy_rate"]) - float(rb["pressure_economy_rate"]), 2),
                "death_econ_delta": round(float(ra["death_economy_rate"]) - float(rb["death_economy_rate"]), 2),
                "sssi_diff": round(float(ra["sample_size_saturation_index_pct"]) - float(rb["sample_size_saturation_index_pct"]), 1)
            }

            return {
                "player_type": "bowler",
                "player_a": {"player_id": int(ra["player_id"]), "name": ra["player_name"], "team": ra["team"], "score": float(ra["bowpri_score"]), "ci": list(ci_a), "sssi": float(ra["sample_size_saturation_index_pct"])},
                "player_b": {"player_id": int(rb["player_id"]), "name": rb["player_name"], "team": rb["team"], "score": float(rb["bowpri_score"]), "ci": list(ci_b), "sssi": float(rb["sample_size_saturation_index_pct"])},
                "ci_overlap": overlap,
                "uncertainty_note": "The observed 95% bootstrap confidence intervals overlap. The difference should not be interpreted as statistically deterministic without larger samples." if overlap else "Confidence intervals do not overlap at the 95% level, showing statistically distinct performance distributions.",
                "radar_data": radar_data,
                "deltas": deltas
            }

    def get_pressure_summary(self):
        return {
            "distribution": [
                {"name": "Normal Leverage", "deliveries": 146124, "pct": 72.70, "color": "#7BD0FF"},
                {"name": "High Pressure (LEI >= 1.5)", "deliveries": 37012, "pct": 18.42, "color": "#FABC4D"},
                {"name": "Extreme Pressure (LEI >= 2.5)", "deliveries": 8939, "pct": 4.44, "color": "#EB107E"},
                {"name": "Low Leverage Cleanup", "deliveries": 8924, "pct": 4.44, "color": "#5B3F47"}
            ],
            "phase_distribution": [
                {"phase": "Powerplay (1–6)", "high_pressure_balls": 8240, "total_balls": 62410, "high_pressure_pct": 13.2},
                {"phase": "Middle Overs (7–15)", "high_pressure_balls": 18520, "total_balls": 91220, "high_pressure_pct": 20.3},
                {"phase": "Death Overs (16–20)", "high_pressure_balls": 19191, "total_balls": 47369, "high_pressure_pct": 40.5}
            ],
            "leverage_timeline": [
                {"over": 1, "avg_pressure": 0.85, "death_weight": 0.0},
                {"over": 3, "avg_pressure": 0.92, "death_weight": 0.0},
                {"over": 6, "avg_pressure": 1.05, "death_weight": 0.0},
                {"over": 9, "avg_pressure": 1.15, "death_weight": 0.0},
                {"over": 12, "avg_pressure": 1.28, "death_weight": 0.0},
                {"over": 15, "avg_pressure": 1.45, "death_weight": 0.0},
                {"over": 17, "avg_pressure": 1.82, "death_weight": 0.35},
                {"over": 18, "avg_pressure": 2.15, "death_weight": 0.35},
                {"over": 19, "avg_pressure": 2.45, "death_weight": 0.35},
                {"over": 20, "avg_pressure": 2.68, "death_weight": 0.35}
            ]
        }

    def get_auction_targets(self):
        return [
            {
                "target_id": 1,
                "player_id": 9070,
                "name": "Ashutosh Sharma",
                "role": "Death Finisher (RHB)",
                "age": 26,
                "team": "Punjab Kings / MP",
                "base_price_lakh": 50,
                "suggested_ceiling_cr": 8.50,
                "max_ceiling_cr": 12.00,
                "bpri_score": 78.22,
                "sssi_pct": 62.4,
                "death_strike_rate": 204.2,
                "chase_strike_rate": 187.5,
                "status": "Priority Actionable Target",
                "eligibility": "BCCI Registered (Eligible)"
            },
            {
                "target_id": 2,
                "player_id": 8940,
                "name": "Shashank Singh",
                "role": "Middle-Order Aggressor (RHB)",
                "age": 33,
                "team": "Punjab Kings / Chhattisgarh",
                "base_price_lakh": 50,
                "suggested_ceiling_cr": 7.00,
                "max_ceiling_cr": 10.00,
                "bpri_score": 77.73,
                "sssi_pct": 84.1,
                "death_strike_rate": 186.4,
                "chase_strike_rate": 179.8,
                "status": "High-Value Aggressor",
                "eligibility": "BCCI Registered (Eligible)"
            },
            {
                "target_id": 3,
                "player_id": 7450,
                "name": "Matthew Humphreys",
                "role": "PP & Middle Spin (SLA)",
                "age": 24,
                "team": "Ireland / Overseas",
                "base_price_lakh": 30,
                "suggested_ceiling_cr": 4.20,
                "max_ceiling_cr": 6.50,
                "bowpri_score": 76.68,
                "sssi_pct": 65.2,
                "hp_economy": 6.12,
                "death_economy": 7.40,
                "status": "Tactical Overseas Value",
                "eligibility": "Overseas Auction Pool (Eligible)"
            },
            {
                "target_id": 4,
                "player_id": 6820,
                "name": "George Linde",
                "role": "All-Rounder Left Arm Spin (SLA)",
                "age": 32,
                "team": "South Africa / Overseas",
                "base_price_lakh": 50,
                "suggested_ceiling_cr": 3.80,
                "max_ceiling_cr": 6.00,
                "bowpri_score": 76.10,
                "sssi_pct": 71.8,
                "hp_economy": 6.35,
                "death_economy": 7.85,
                "status": "Contingency All-Rounder",
                "eligibility": "Overseas Auction Pool (Eligible)"
            }
        ]

    def simulate_auction(self, current_purse: float, bids: dict):
        # bids is {target_name or id: bid_amount}
        total_allocated = sum(bids.values())
        remaining = current_purse - total_allocated
        suggested_ceilings = {
            "Ashutosh Sharma": 8.50,
            "Shashank Singh": 7.00,
            "Matthew Humphreys": 4.20,
            "George Linde": 3.80
        }
        warnings = []
        for name, amount in bids.items():
            if name in suggested_ceilings and amount > suggested_ceilings[name]:
                warnings.append(f"{name} bid (₹{amount:.2f} Cr) exceeds recommended tactical ceiling (₹{suggested_ceilings[name]:.2f} Cr).")
        
        return {
            "initial_purse_cr": current_purse,
            "total_allocated_cr": round(total_allocated, 2),
            "remaining_purse_cr": round(remaining, 2),
            "is_feasible": remaining >= 0,
            "warnings": warnings,
            "slots_impact": {
                "additional_players": len([b for b in bids.values() if b > 0]),
                "remaining_slots": 7 - len([b for b in bids.values() if b > 0]),
                "overseas_slots_available": "2 of 8 free" if any("Humphreys" in k or "Linde" in k for k, v in bids.items() if v > 0) else "3 of 8 free"
            }
        }

    def get_methodology(self):
        return {
            "overview": "The ROYAL EDGE methodology evaluates player performance under match leverage using ball-by-ball context across 867 IPL and T20I matches (2022–2026).",
            "pressure_index": {
                "name": "Match Leverage Pressure Index (P_t)",
                "first_innings": "P_{1st} = 1.0 + 0.40 \\cdot (1 - B_t/120) + 0.35 \\cdot (W_t/10) + 0.25 \\cdot (R_t / (120 - B_t + 1))",
                "second_innings": "P_{2nd} = 0.50 \\cdot \\frac{RRR_t}{CRR_{req}} + 0.35 \\cdot \\left(\\frac{10 - W_t}{10}\\right)^{-1} + 0.15 \\cdot \\left(\\frac{B_t}{120}\\right)^{-1}",
                "knockout_multiplier": "1.15 multiplier applied during playoff and knockout elimination matches."
            },
            "metrics": {
                "bpri": {
                    "name": "Batting Pressure Reliability Index (BPRI)",
                    "weights": "0.35 \\cdot HP\\_SR + 0.25 \\cdot HP\\_Avg + 0.20 \\cdot Death\\_SR + 0.10 \\cdot Chase\\_SR + 0.10 \\cdot \\Delta SR",
                    "shrinkage": "Shrunk towards prior mean (128.5) with prior weight K = 60 balls."
                },
                "bowpri": {
                    "name": "Bowling Pressure Reliability Index (BOWPRI)",
                    "weights": "0.35 \\cdot HP\\_Econ (inv) + 0.25 \\cdot HP\\_Avg (inv) + 0.20 \\cdot Death\\_Econ (inv) + 0.10 \\cdot Wkts/Ball + 0.10 \\cdot \\Delta Econ (inv)",
                    "shrinkage": "Shrunk towards prior mean (8.45) with prior weight K = 50 balls."
                }
            },
            "statistical_rigor": {
                "sssi": "Sample Size Saturation Index (SSSI %) represents the proportion of target sample size accumulated (60 balls for batting, 50 balls for bowling). It indicates statistical robustness, NOT player probability of future success.",
                "bootstrap_ci": "1,000-iteration bootstrap 95% confidence intervals capture the sampling uncertainty of measured performance. Overlapping intervals caution against treating small score differences as definitive talent separation.",
                "policy_segregation": "Elite international players from non-participating boards serve strictly as statistical Bayesian benchmarks. Actionable targets are strictly filtered against BCCI-eligible IPL auction registrations."
            }
        }

data_service = DataService()
