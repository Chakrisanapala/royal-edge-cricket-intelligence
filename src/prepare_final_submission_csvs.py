"""
Prepare Authoritative Final Submission CSVs with Bootstrap Intervals and SSSI
"""

import os
import pandas as pd
import numpy as np

BASE_DIR = r"d:\Desktop\RR - Hackathon"
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
FINAL_DIR = os.path.join(BASE_DIR, "final_submission")
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_FILE = os.path.join(BASE_DIR, "data", "processed", "ball_by_ball_pressure.parquet")

def build_final_csvs():
    os.makedirs(FINAL_DIR, exist_ok=True)
    df = pd.read_parquet(PROCESSED_FILE)
    mapping = pd.read_csv(os.path.join(DATA_DIR, 'competition_team_player_mapping.csv'))
    
    top10_bat = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_batters.csv'))
    top10_bowl = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_bowlers.csv'))
    
    # 1. Batters Final CSV
    np.random.seed(42)
    bat_rows = []
    for _, r in top10_bat.iterrows():
        pid = r['player_id']
        p_balls = df[(df['striker_id'] == pid) & df['is_legal_batter'] & df['is_high_pressure_bat']]
        runs = p_balls['batter_runs'].values
        n = len(runs)
        
        boot_srs = [np.random.choice(runs, size=n, replace=True).sum() / n * 100.0 for _ in range(1000)]
        ci_low = np.percentile(boot_srs, 2.5)
        ci_high = np.percentile(boot_srs, 97.5)
        se = np.std(boot_srs)
        
        sssi = min(99.0, max(40.0, round((n / 250.0) * 100.0, 1)))
        
        bat_rows.append({
            'rank': r['rank'],
            'player_id': pid,
            'player_name': r['player_name'],
            'team': r['team'],
            'batting_role': r['batting_role'],
            'matches_analyzed': r['matches'],
            'pressure_innings': int(r['hp_innings']),
            'pressure_balls_faced': n,
            'pressure_runs_scored': int(r['hp_runs']),
            'pressure_batting_avg': round(r['hp_avg'], 2),
            'pressure_strike_rate': round(r['hp_strike_rate'], 2),
            'death_strike_rate': round(r['death_strike_rate'], 2),
            'chase_strike_rate': round(r['chase_strike_rate'], 2),
            'delta_strike_rate_vs_normal': round(r['delta_strike_rate'], 2),
            'bootstrap_95_ci_lower_sr': round(ci_low, 2),
            'bootstrap_95_ci_upper_sr': round(ci_high, 2),
            'bootstrap_standard_error_sr': round(se, 2),
            'bpri_score': round(r['bpri_score'], 2),
            'sample_size_saturation_index_pct': sssi,
            'uncertainty_interpretation': f"True historical high-pressure strike rate lies in [{ci_low:.1f}, {ci_high:.1f}] with 95% bootstrap confidence; not a predictive win probability",
            'ipl_auction_eligibility': 'Eligible'
        })
        
    df_final_bat = pd.DataFrame(bat_rows)
    bat_csv_path = os.path.join(FINAL_DIR, 'RR_Top_10_Batters.csv')
    df_final_bat.to_csv(bat_csv_path, index=False)
    print(f"Generated {bat_csv_path}")

    # 2. Bowlers Final CSV
    bowl_rows = []
    pakistan_ids = {2490, 5979, 3578, 34485}
    
    for _, r in top10_bowl.iterrows():
        bid = r['bowler_id']
        b_balls = df[(df['bowler_id'] == bid) & df['is_high_pressure_bowl']]
        runs_c = b_balls['bowler_runs_conceded'].values
        legal = b_balls['is_legal_bowler'].values
        n = len(runs_c)
        n_legal = legal.sum()
        
        boot_econs = []
        for _ in range(1000):
            idx = np.random.choice(n, size=n, replace=True)
            sr = runs_c[idx].sum()
            sl = legal[idx].sum()
            if sl > 0:
                boot_econs.append(sr / (sl / 6.0))
        ci_low = np.percentile(boot_econs, 2.5)
        ci_high = np.percentile(boot_econs, 97.5)
        se = np.std(boot_econs)
        
        sssi = min(99.0, max(40.0, round((n_legal / 200.0) * 100.0, 1)))
        elig = 'Ineligible under current BCCI Policy (Statistical Benchmark Only)' if bid in pakistan_ids else 'Eligible (Overseas Quota)'
        
        bowl_rows.append({
            'rank': r['rank'],
            'player_id': bid,
            'player_name': r['player_name'],
            'team': r['team'],
            'bowling_role': r['bowling_role'],
            'matches_analyzed': r['matches'],
            'pressure_innings': int(r['hp_innings']),
            'pressure_overs_bowled': round(n_legal / 6.0, 1),
            'pressure_legal_balls': int(n_legal),
            'pressure_runs_conceded': int(r['hp_runs_conceded']),
            'pressure_wickets': int(r['hp_wickets']),
            'pressure_bowling_avg': round(r['hp_bowling_avg'], 2),
            'pressure_economy_rate': round(r['hp_economy'], 2),
            'pressure_bowling_strike_rate': round(r['hp_bowling_sr'], 2),
            'death_economy_rate': round(r['death_economy'], 2),
            'delta_economy_vs_normal': round(r['delta_economy'], 2),
            'bootstrap_95_ci_lower_econ': round(ci_low, 2),
            'bootstrap_95_ci_upper_econ': round(ci_high, 2),
            'bootstrap_standard_error_econ': round(se, 2),
            'bowpri_score': round(r['bowpri_score'], 2),
            'sample_size_saturation_index_pct': sssi,
            'uncertainty_interpretation': f"True historical high-pressure economy rate lies in [{ci_low:.2f}, {ci_high:.2f}] with 95% bootstrap confidence; not a predictive win probability",
            'ipl_auction_eligibility': elig
        })
        
    df_final_bowl = pd.DataFrame(bowl_rows)
    bowl_csv_path = os.path.join(FINAL_DIR, 'RR_Top_10_Bowlers.csv')
    df_final_bowl.to_csv(bowl_csv_path, index=False)
    print(f"Generated {bowl_csv_path}")

if __name__ == '__main__':
    build_final_csvs()

