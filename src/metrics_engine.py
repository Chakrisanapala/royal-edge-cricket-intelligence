"""
Advanced Batting and Bowling Performance Metrics Engine
Implements BPRI and BOWPRI with Empirical Bayesian Shrinkage and Reliability Adjustments.
"""

import os
import pandas as pd
import numpy as np

PROCESSED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed", "ball_by_ball_pressure.parquet")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")

def compute_player_metrics():
    print(f"Loading processed delivery dataset from {PROCESSED_FILE}...")
    df = pd.read_parquet(PROCESSED_FILE)
    
    # ---------------------------------------------------------
    # 1. ADVANCED BATTING METRICS
    # ---------------------------------------------------------
    print("Computing advanced batting metrics across all players...")
    
    # Filter to legal balls for batter
    batter_balls = df[df['is_legal_batter']].copy()
    
    # Identify unique match-innings per player
    # A batter played an innings if they faced at least 1 legal ball or were non-striker
    batter_grp = batter_balls.groupby('striker_id')
    
    # Overall Batting
    b_overall = batter_balls.groupby('striker_id').agg(
        player_name=('striker_name', 'last'),
        total_runs=('batter_runs', 'sum'),
        balls_faced=('is_legal_batter', 'count'),
        fours=('is_four', 'sum'),
        sixes=('is_six', 'sum'),
        dots=('batter_runs', lambda x: (x == 0).sum()),
        dismissals=('is_batter_out', 'sum'),
        innings=('match_id', lambda x: len(np.unique(list(zip(df.loc[x.index, 'match_id'], df.loc[x.index, 'innings']))))),
        matches=('match_id', 'nunique'),
        knockout_matches=('match_id', lambda x: df.loc[x.index[df.loc[x.index, 'knock_out'] == 1], 'match_id'].nunique())
    ).reset_index()
    
    b_overall['batting_avg'] = np.where(b_overall['dismissals'] > 0, b_overall['total_runs'] / b_overall['dismissals'], b_overall['total_runs'])
    b_overall['strike_rate'] = (b_overall['total_runs'] / b_overall['balls_faced']) * 100.0
    b_overall['boundary_pct'] = ((b_overall['fours'] + b_overall['sixes']) / b_overall['balls_faced']) * 100.0
    b_overall['dot_pct'] = (b_overall['dots'] / b_overall['balls_faced']) * 100.0
    
    # High Pressure Batting (is_high_pressure_bat == True)
    hp_bat = batter_balls[batter_balls['is_high_pressure_bat']].groupby('striker_id').agg(
        hp_runs=('batter_runs', 'sum'),
        hp_balls=('is_legal_batter', 'count'),
        hp_fours=('is_four', 'sum'),
        hp_sixes=('is_six', 'sum'),
        hp_dots=('batter_runs', lambda x: (x == 0).sum()),
        hp_dismissals=('is_batter_out', 'sum'),
        hp_innings=('match_id', lambda x: len(np.unique(list(zip(df.loc[x.index, 'match_id'], df.loc[x.index, 'innings'])))))
    ).reset_index()
    
    hp_bat['hp_avg'] = np.where(hp_bat['hp_dismissals'] > 0, hp_bat['hp_runs'] / hp_bat['hp_dismissals'], hp_bat['hp_runs'])
    hp_bat['hp_strike_rate'] = (hp_bat['hp_runs'] / hp_bat['hp_balls']) * 100.0
    hp_bat['hp_boundary_pct'] = ((hp_bat['hp_fours'] + hp_bat['hp_sixes']) / hp_bat['hp_balls']) * 100.0
    hp_bat['hp_dot_pct'] = (hp_bat['hp_dots'] / hp_bat['hp_balls']) * 100.0
    
    # Normal / Low Pressure Batting (is_high_pressure_bat == False)
    norm_bat = batter_balls[~batter_balls['is_high_pressure_bat']].groupby('striker_id').agg(
        norm_runs=('batter_runs', 'sum'),
        norm_balls=('is_legal_batter', 'count'),
        norm_dismissals=('is_batter_out', 'sum')
    ).reset_index()
    norm_bat['norm_strike_rate'] = np.where(norm_bat['norm_balls'] > 0, (norm_bat['norm_runs'] / norm_bat['norm_balls']) * 100.0, 120.0)
    norm_bat['norm_avg'] = np.where(norm_bat['norm_dismissals'] > 0, norm_bat['norm_runs'] / norm_bat['norm_dismissals'], norm_bat['norm_runs'])
    
    # Death Overs Batting (overid >= 16)
    death_bat = batter_balls[batter_balls['overid'] >= 16].groupby('striker_id').agg(
        death_runs=('batter_runs', 'sum'),
        death_balls=('is_legal_batter', 'count'),
        death_fours=('is_four', 'sum'),
        death_sixes=('is_six', 'sum'),
        death_dots=('batter_runs', lambda x: (x == 0).sum()),
        death_dismissals=('is_batter_out', 'sum')
    ).reset_index()
    death_bat['death_strike_rate'] = np.where(death_bat['death_balls'] > 0, (death_bat['death_runs'] / death_bat['death_balls']) * 100.0, 0.0)
    death_bat['death_boundary_pct'] = np.where(death_bat['death_balls'] > 0, ((death_bat['death_fours'] + death_bat['death_sixes']) / death_bat['death_balls']) * 100.0, 0.0)
    death_bat['death_dot_pct'] = np.where(death_bat['death_balls'] > 0, (death_bat['death_dots'] / death_bat['death_balls']) * 100.0, 0.0)
    
    # Chase Batting (Innings == 2)
    chase_bat = batter_balls[batter_balls['innings'] == 2].groupby('striker_id').agg(
        chase_runs=('batter_runs', 'sum'),
        chase_balls=('is_legal_batter', 'count'),
        chase_dismissals=('is_batter_out', 'sum')
    ).reset_index()
    chase_bat['chase_strike_rate'] = np.where(chase_bat['chase_balls'] > 0, (chase_bat['chase_runs'] / chase_bat['chase_balls']) * 100.0, 0.0)
    chase_bat['chase_avg'] = np.where(chase_bat['chase_dismissals'] > 0, chase_bat['chase_runs'] / chase_bat['chase_dismissals'], chase_bat['chase_runs'])
    
    # Collapse Recovery Batting (Innings 1 or 2 when cum_wickets_before >= 3 in overs 1-10)
    collapse_bat = batter_balls[(batter_balls['cum_wickets_before'] >= 3) & (batter_balls['overid'] <= 10)].groupby('striker_id').agg(
        collapse_runs=('batter_runs', 'sum'),
        collapse_balls=('is_legal_batter', 'count'),
        collapse_dismissals=('is_batter_out', 'sum')
    ).reset_index()
    collapse_bat['collapse_strike_rate'] = np.where(collapse_bat['collapse_balls'] > 0, (collapse_bat['collapse_runs'] / collapse_bat['collapse_balls']) * 100.0, 0.0)
    
    # Match-to-Match Consistency (Standard deviation of match strike rates under pressure)
    # Per-match pressure runs and balls
    match_bat = batter_balls[batter_balls['is_high_pressure_bat']].groupby(['striker_id', 'match_id']).agg(
        m_runs=('batter_runs', 'sum'),
        m_balls=('is_legal_batter', 'count')
    ).reset_index()
    match_bat['m_sr'] = (match_bat['m_runs'] / match_bat['m_balls']) * 100.0
    consistency_bat = match_bat.groupby('striker_id')['m_sr'].std().fillna(30.0).reset_index(name='bat_sr_std')
    
    # Merge Batting Table
    batters = b_overall.merge(hp_bat, on='striker_id', how='left')
    batters = batters.merge(norm_bat[['striker_id', 'norm_strike_rate', 'norm_avg', 'norm_balls']], on='striker_id', how='left')
    batters = batters.merge(death_bat[['striker_id', 'death_runs', 'death_balls', 'death_strike_rate', 'death_boundary_pct', 'death_dot_pct']], on='striker_id', how='left')
    batters = batters.merge(chase_bat[['striker_id', 'chase_runs', 'chase_balls', 'chase_strike_rate', 'chase_avg']], on='striker_id', how='left')
    batters = batters.merge(collapse_bat[['striker_id', 'collapse_runs', 'collapse_balls', 'collapse_strike_rate']], on='striker_id', how='left')
    batters = batters.merge(consistency_bat, on='striker_id', how='left')
    
    # Fill NAs
    batters = batters.fillna({
        'hp_runs': 0, 'hp_balls': 0, 'hp_fours': 0, 'hp_sixes': 0, 'hp_dots': 0, 'hp_dismissals': 0, 'hp_innings': 0,
        'hp_avg': 0.0, 'hp_strike_rate': 0.0, 'hp_boundary_pct': 0.0, 'hp_dot_pct': 100.0,
        'norm_strike_rate': 120.0, 'norm_avg': 20.0, 'norm_balls': 0,
        'death_runs': 0, 'death_balls': 0, 'death_strike_rate': 0.0, 'death_boundary_pct': 0.0, 'death_dot_pct': 100.0,
        'chase_runs': 0, 'chase_balls': 0, 'chase_strike_rate': 0.0, 'chase_avg': 0.0,
        'collapse_runs': 0, 'collapse_balls': 0, 'collapse_strike_rate': 0.0, 'bat_sr_std': 45.0
    })
    
    # Baseline Differentials
    batters['delta_strike_rate'] = batters['hp_strike_rate'] - batters['norm_strike_rate']
    batters['delta_avg'] = batters['hp_avg'] - batters['norm_avg']
    
    # Primary Batting Role classification based on batting order mode
    bo_mode = batter_balls.groupby('striker_id')['batting_order'].agg(lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 5).reset_index(name='modal_order')
    batters = batters.merge(bo_mode, on='striker_id', how='left')
    
    def assign_bat_role(row):
        order = row['modal_order']
        sr = row['strike_rate']
        death_balls = row['death_balls']
        if order <= 2:
            return 'Aggressive Opener' if sr >= 138 else 'Top-order Anchor'
        elif order <= 4:
            return 'Middle-order Aggressor' if sr >= 135 else 'Middle-order Stabilizer'
        elif order <= 6:
            return 'Finisher' if death_balls >= 40 or sr >= 140 else 'Middle-order Anchor'
        else:
            return 'Lower-order Power Hitter'
            
    batters['batting_role'] = batters.apply(assign_bat_role, axis=1)
    
    # ---------------------------------------------------------
    # 2. ADVANCED BOWLING METRICS
    # ---------------------------------------------------------
    print("Computing advanced bowling metrics across all players...")
    
    # All deliveries where bowler bowled
    bowler_deliveries = df.copy()
    
    # Overall Bowling
    bowl_overall = bowler_deliveries.groupby('bowler_id').agg(
        player_name=('bowler_name', 'last'),
        runs_conceded=('bowler_runs_conceded', 'sum'),
        legal_balls=('is_legal_bowler', 'sum'),
        total_balls=('is_legal_bowler', 'count'),
        wickets=('is_bowler_wicket', 'sum'),
        dots=('bowler_runs_conceded', lambda x: (x == 0).sum()),
        boundaries=('runs', lambda x: (df.loc[x.index, 'is_four'] | df.loc[x.index, 'is_six']).sum()),
        innings=('match_id', lambda x: len(np.unique(list(zip(df.loc[x.index, 'match_id'], df.loc[x.index, 'innings']))))),
        matches=('match_id', 'nunique'),
        knockout_matches=('match_id', lambda x: df.loc[x.index[df.loc[x.index, 'knock_out'] == 1], 'match_id'].nunique())
    ).reset_index()
    
    bowl_overall['overs'] = bowl_overall['legal_balls'] / 6.0
    bowl_overall['economy'] = np.where(bowl_overall['overs'] > 0, bowl_overall['runs_conceded'] / bowl_overall['overs'], 12.0)
    bowl_overall['bowling_avg'] = np.where(bowl_overall['wickets'] > 0, bowl_overall['runs_conceded'] / bowl_overall['wickets'], 50.0)
    bowl_overall['bowling_sr'] = np.where(bowl_overall['wickets'] > 0, bowl_overall['legal_balls'] / bowl_overall['wickets'], 40.0)
    bowl_overall['dot_pct'] = (bowl_overall['dots'] / bowl_overall['total_balls']) * 100.0
    bowl_overall['boundary_conceded_pct'] = (bowl_overall['boundaries'] / bowl_overall['total_balls']) * 100.0
    
    # High Pressure Bowling (is_high_pressure_bowl == True)
    hp_bowl = bowler_deliveries[bowler_deliveries['is_high_pressure_bowl']].groupby('bowler_id').agg(
        hp_runs_conceded=('bowler_runs_conceded', 'sum'),
        hp_legal_balls=('is_legal_bowler', 'sum'),
        hp_total_balls=('is_legal_bowler', 'count'),
        hp_wickets=('is_bowler_wicket', 'sum'),
        hp_dots=('bowler_runs_conceded', lambda x: (x == 0).sum()),
        hp_boundaries=('runs', lambda x: (df.loc[x.index, 'is_four'] | df.loc[x.index, 'is_six']).sum()),
        hp_innings=('match_id', lambda x: len(np.unique(list(zip(df.loc[x.index, 'match_id'], df.loc[x.index, 'innings'])))))
    ).reset_index()
    
    hp_bowl['hp_overs'] = hp_bowl['hp_legal_balls'] / 6.0
    hp_bowl['hp_economy'] = np.where(hp_bowl['hp_overs'] > 0, hp_bowl['hp_runs_conceded'] / hp_bowl['hp_overs'], 12.0)
    hp_bowl['hp_bowling_avg'] = np.where(hp_bowl['hp_wickets'] > 0, hp_bowl['hp_runs_conceded'] / hp_bowl['hp_wickets'], 50.0)
    hp_bowl['hp_bowling_sr'] = np.where(hp_bowl['hp_wickets'] > 0, hp_bowl['hp_legal_balls'] / hp_bowl['hp_wickets'], 40.0)
    hp_bowl['hp_dot_pct'] = np.where(hp_bowl['hp_total_balls'] > 0, (hp_bowl['hp_dots'] / hp_bowl['hp_total_balls']) * 100.0, 0.0)
    hp_bowl['hp_boundary_pct'] = np.where(hp_bowl['hp_total_balls'] > 0, (hp_bowl['hp_boundaries'] / hp_bowl['hp_total_balls']) * 100.0, 0.0)
    
    # Normal / Low Pressure Bowling (is_high_pressure_bowl == False)
    norm_bowl = bowler_deliveries[~bowler_deliveries['is_high_pressure_bowl']].groupby('bowler_id').agg(
        norm_runs_conceded=('bowler_runs_conceded', 'sum'),
        norm_legal_balls=('is_legal_bowler', 'sum'),
        norm_wickets=('is_bowler_wicket', 'sum')
    ).reset_index()
    norm_bowl['norm_overs'] = norm_bowl['norm_legal_balls'] / 6.0
    norm_bowl['norm_economy'] = np.where(norm_bowl['norm_overs'] > 0, norm_bowl['norm_runs_conceded'] / norm_bowl['norm_overs'], 8.5)
    norm_bowl['norm_bowling_sr'] = np.where(norm_bowl['norm_wickets'] > 0, norm_bowl['norm_legal_balls'] / norm_bowl['norm_wickets'], 25.0)
    
    # Death Overs Bowling (overid >= 16)
    death_bowl = bowler_deliveries[bowler_deliveries['overid'] >= 16].groupby('bowler_id').agg(
        death_runs_conceded=('bowler_runs_conceded', 'sum'),
        death_legal_balls=('is_legal_bowler', 'sum'),
        death_wickets=('is_bowler_wicket', 'sum'),
        death_dots=('bowler_runs_conceded', lambda x: (x == 0).sum()),
        death_boundaries=('runs', lambda x: (df.loc[x.index, 'is_four'] | df.loc[x.index, 'is_six']).sum())
    ).reset_index()
    death_bowl['death_overs'] = death_bowl['death_legal_balls'] / 6.0
    death_bowl['death_economy'] = np.where(death_bowl['death_overs'] > 0, death_bowl['death_runs_conceded'] / death_bowl['death_overs'], 13.0)
    death_bowl['death_wickets_per_100'] = np.where(death_bowl['death_legal_balls'] > 0, (death_bowl['death_wickets'] / death_bowl['death_legal_balls']) * 100.0, 0.0)
    death_bowl['death_dot_pct'] = np.where(death_bowl['death_legal_balls'] > 0, (death_bowl['death_dots'] / death_bowl['death_legal_balls']) * 100.0, 0.0)
    death_bowl['death_boundary_pct'] = np.where(death_bowl['death_legal_balls'] > 0, (death_bowl['death_boundaries'] / death_bowl['death_legal_balls']) * 100.0, 0.0)
    
    # Defending Totals Bowling (Innings == 2)
    defend_bowl = bowler_deliveries[bowler_deliveries['innings'] == 2].groupby('bowler_id').agg(
        defend_runs=('bowler_runs_conceded', 'sum'),
        defend_legal_balls=('is_legal_bowler', 'sum'),
        defend_wickets=('is_bowler_wicket', 'sum')
    ).reset_index()
    defend_bowl['defend_overs'] = defend_bowl['defend_legal_balls'] / 6.0
    defend_bowl['defend_economy'] = np.where(defend_bowl['defend_overs'] > 0, defend_bowl['defend_runs'] / defend_bowl['defend_overs'], 9.0)
    
    # Consistency in Bowling (std dev of match economy under pressure)
    match_bowl = bowler_deliveries[bowler_deliveries['is_high_pressure_bowl']].groupby(['bowler_id', 'match_id']).agg(
        m_runs=('bowler_runs_conceded', 'sum'),
        m_legal=('is_legal_bowler', 'sum')
    ).reset_index()
    match_bowl['m_econ'] = np.where(match_bowl['m_legal'] > 0, (match_bowl['m_runs'] / match_bowl['m_legal']) * 6.0, 9.0)
    consistency_bowl = match_bowl.groupby('bowler_id')['m_econ'].std().fillna(3.5).reset_index(name='bowl_econ_std')
    
    # Pace or Spin & Bowling Type Mode
    bowler_type_info = bowler_deliveries.groupby('bowler_id').agg(
        pace_or_spin=('pace_or_spin', lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Pace'),
        bowling_type=('bowling_type', lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Right-arm medium')
    ).reset_index()
    
    # Merge Bowling Table
    bowlers = bowl_overall.merge(hp_bowl, on='bowler_id', how='left')
    bowlers = bowlers.merge(norm_bowl[['bowler_id', 'norm_economy', 'norm_bowling_sr', 'norm_legal_balls']], on='bowler_id', how='left')
    bowlers = bowlers.merge(death_bowl[['bowler_id', 'death_overs', 'death_legal_balls', 'death_economy', 'death_wickets', 'death_wickets_per_100', 'death_dot_pct', 'death_boundary_pct']], on='bowler_id', how='left')
    bowlers = bowlers.merge(defend_bowl[['bowler_id', 'defend_economy', 'defend_wickets']], on='bowler_id', how='left')
    bowlers = bowlers.merge(consistency_bowl, on='bowler_id', how='left')
    bowlers = bowlers.merge(bowler_type_info, on='bowler_id', how='left')
    
    # Fill NAs
    bowlers = bowlers.fillna({
        'hp_runs_conceded': 0, 'hp_legal_balls': 0, 'hp_total_balls': 0, 'hp_wickets': 0, 'hp_dots': 0, 'hp_boundaries': 0, 'hp_innings': 0,
        'hp_overs': 0.0, 'hp_economy': 12.0, 'hp_bowling_avg': 50.0, 'hp_bowling_sr': 40.0, 'hp_dot_pct': 0.0, 'hp_boundary_pct': 30.0,
        'norm_economy': 8.5, 'norm_bowling_sr': 25.0, 'norm_legal_balls': 0,
        'death_overs': 0.0, 'death_legal_balls': 0, 'death_economy': 12.0, 'death_wickets': 0, 'death_wickets_per_100': 0.0, 'death_dot_pct': 0.0, 'death_boundary_pct': 30.0,
        'defend_economy': 9.0, 'defend_wickets': 0, 'bowl_econ_std': 4.0
    })
    
    # Baseline Differentials
    # Positive delta_economy means bowler conceded FEWER runs under pressure than their normal baseline!
    bowlers['delta_economy'] = bowlers['norm_economy'] - bowlers['hp_economy']
    # Positive delta_strike_rate means bowler took wickets in FEWER balls under pressure than normal!
    bowlers['delta_bowling_sr'] = bowlers['norm_bowling_sr'] - bowlers['hp_bowling_sr']
    
    # Bowling Role classification
    # Determine phase where bowler bowls most balls
    bowl_phases = bowler_deliveries.groupby(['bowler_id', 'phase'], observed=False)['is_legal_bowler'].sum().unstack().fillna(0)
    bowl_phases_pct = bowl_phases.div(bowl_phases.sum(axis=1).replace(0, 1), axis=0) * 100.0
    
    def assign_bowl_role(row):
        b_id = row['bowler_id']
        p_or_s = row['pace_or_spin']
        d_overs = row['death_overs']
        
        pp_share = bowl_phases_pct.loc[b_id, 'Powerplay'] if b_id in bowl_phases_pct.index else 0
        death_share = bowl_phases_pct.loc[b_id, 'Death'] if b_id in bowl_phases_pct.index else 0
        
        if death_share >= 28.0 or d_overs >= 25.0:
            return f"Death-over Specialist ({p_or_s})"
        elif pp_share >= 40.0:
            return f"Powerplay Specialist ({p_or_s})"
        elif p_or_s == 'Spin':
            return "Middle-over Spin Controller"
        else:
            return f"Middle-over Wicket-taker ({p_or_s})"
            
    bowlers['bowling_role'] = bowlers.apply(assign_bowl_role, axis=1)
    
    return batters, bowlers, df

def calculate_bpri_and_bowpri(batters, bowlers, df):
    """
    Applies MinMax percentile normalization, candidate weights,
    Empirical Bayesian shrinkage, and generates final BPRI and BOWPRI scores.
    """
    print("\n---------------------------------------------------------")
    print("APPLYING STATISTICAL RELIABILITY, SHRINKAGE, AND INDEXING")
    print("---------------------------------------------------------")
    
    # ---------------------------------------------------------
    # ELIGIBILITY THRESHOLDS (Phase 6)
    # ---------------------------------------------------------
    # Batters: >= 10 innings, >= 75 pressure balls faced across competitions
    # Bowlers: >= 10 innings, >= 60 pressure balls bowled across competitions
    BAT_MIN_INNINGS = 10
    BAT_MIN_HP_BALLS = 75
    
    BOWL_MIN_INNINGS = 10
    BOWL_MIN_HP_BALLS = 60
    
    eligible_batters = batters[(batters['innings'] >= BAT_MIN_INNINGS) & (batters['hp_balls'] >= BAT_MIN_HP_BALLS)].copy()
    eligible_bowlers = bowlers[(bowlers['innings'] >= BOWL_MIN_INNINGS) & (bowlers['hp_legal_balls'] >= BOWL_MIN_HP_BALLS)].copy()
    
    print(f"Eligible Batters meeting threshold (>= {BAT_MIN_INNINGS} inngs, >= {BAT_MIN_HP_BALLS} hp balls): {len(eligible_batters)} / {len(batters)}")
    print(f"Eligible Bowlers meeting threshold (>= {BOWL_MIN_INNINGS} inngs, >= {BOWL_MIN_HP_BALLS} hp balls): {len(eligible_bowlers)} / {len(bowlers)}")
    
    # ---------------------------------------------------------
    # BATTING PRESSURE RELIABILITY INDEX (BPRI)
    # ---------------------------------------------------------
    # Candidate Weights:
    # 30% Pressure performance relative to player's normal baseline (Delta SR + Delta Avg)
    # 20% Strike-rate effectiveness under pressure
    # 15% Boundary and dot-ball control (Boundary % high, Dot % low)
    # 15% Chase and close-match performance
    # 10% Death-over performance
    # 10% Match-to-match consistency (lower std dev is better)
    
    eb = eligible_batters.copy()
    
    # Helper MinMax scaler to [0, 100] with clipping
    def scale_series(s, invert=False, q_low=0.02, q_high=0.98):
        v_min = s.quantile(q_low)
        v_max = s.quantile(q_high)
        if v_max == v_min:
            return pd.Series(50.0, index=s.index)
        scaled = np.clip((s - v_min) / (v_max - v_min), 0.0, 1.0) * 100.0
        return 100.0 - scaled if invert else scaled
        
    # Pillar 1: Baseline Differential (30%)
    eb['score_delta_sr'] = scale_series(eb['delta_strike_rate'])
    eb['score_delta_avg'] = scale_series(eb['delta_avg'])
    eb['pillar_baseline'] = 0.65 * eb['score_delta_sr'] + 0.35 * eb['score_delta_avg']
    
    # Pillar 2: Pressure Strike Rate Effectiveness (20%)
    eb['pillar_sr'] = scale_series(eb['hp_strike_rate'])
    
    # Pillar 3: Boundary & Dot-ball Control (15%)
    eb['score_hp_bound'] = scale_series(eb['hp_boundary_pct'])
    eb['score_hp_dot'] = scale_series(eb['hp_dot_pct'], invert=True) # Lower dots = higher score
    eb['pillar_control'] = 0.55 * eb['score_hp_bound'] + 0.45 * eb['score_hp_dot']
    
    # Pillar 4: Chase & Pressure Finish Performance (15%)
    eb['score_chase_sr'] = scale_series(eb['chase_strike_rate'])
    eb['score_chase_avg'] = scale_series(eb['chase_avg'])
    eb['pillar_chase'] = 0.60 * eb['score_chase_sr'] + 0.40 * eb['score_chase_avg']
    
    # Pillar 5: Death-Over Performance (10%)
    eb['score_death_sr'] = scale_series(eb['death_strike_rate'])
    eb['score_death_bound'] = scale_series(eb['death_boundary_pct'])
    eb['pillar_death'] = 0.60 * eb['score_death_sr'] + 0.40 * eb['score_death_bound']
    
    # Pillar 6: Consistency (10%)
    eb['pillar_consistency'] = scale_series(eb['bat_sr_std'], invert=True) # Lower variance = higher consistency
    
    # Raw BPRI
    eb['raw_bpri'] = (
        0.30 * eb['pillar_baseline'] +
        0.20 * eb['pillar_sr'] +
        0.15 * eb['pillar_control'] +
        0.15 * eb['pillar_chase'] +
        0.10 * eb['pillar_death'] +
        0.10 * eb['pillar_consistency']
    )
    
    # Empirical Bayesian Shrinkage for Sample Reliability (Phase 6)
    # Prior mean = mean of raw_bpri across eligible population
    prior_mean_bat = eb['raw_bpri'].mean()
    # Shrinkage weight: w = N / (N + K_bat), where K_bat is shrinkage constant
    K_BAT = 60.0
    eb['shrinkage_weight'] = eb['hp_balls'] / (eb['hp_balls'] + K_BAT)
    eb['bpri_score'] = (eb['shrinkage_weight'] * eb['raw_bpri']) + ((1.0 - eb['shrinkage_weight']) * prior_mean_bat)
    
    # Reliability / Confidence indicator (0 to 100%)
    eb['confidence_score'] = np.clip((eb['hp_balls'] / 250.0) * 100.0, 40.0, 99.0)
    
    # Round metrics for readability
    eb['bpri_score'] = eb['bpri_score'].round(2)
    eb['confidence_score'] = eb['confidence_score'].round(1)
    
    # Sort Batters
    ranked_batters = eb.sort_values(by='bpri_score', ascending=False).reset_index(drop=True)
    ranked_batters['rank'] = ranked_batters.index + 1
    
    # ---------------------------------------------------------
    # BOWLING PRESSURE RELIABILITY INDEX (BOWPRI)
    # ---------------------------------------------------------
    # Candidate Weights:
    # 30% Pressure performance relative to normal baseline (Delta Economy + Delta Strike Rate)
    # 20% Economy control under pressure (lower is better)
    # 15% Wicket-taking effectiveness under pressure (hp bowling strike rate: lower balls per wicket is better)
    # 15% Dot-ball and boundary prevention under pressure
    # 10% Death-over performance (death economy low, death wickets high)
    # 10% Match-to-match consistency (lower economy variance is better)
    
    ebowl = eligible_bowlers.copy()
    
    # Pillar 1: Baseline Differential (30%)
    ebowl['score_delta_econ'] = scale_series(ebowl['delta_economy'])
    ebowl['score_delta_sr'] = scale_series(ebowl['delta_bowling_sr'])
    ebowl['pillar_baseline'] = 0.65 * ebowl['score_delta_econ'] + 0.35 * ebowl['score_delta_sr']
    
    # Pillar 2: Economy Control Under Pressure (20%)
    ebowl['pillar_econ'] = scale_series(ebowl['hp_economy'], invert=True) # Lower economy = higher score
    
    # Pillar 3: Wicket-Taking Effectiveness (15%)
    # Lower balls per wicket (strike rate) is better!
    ebowl['pillar_wickets'] = scale_series(ebowl['hp_bowling_sr'], invert=True)
    
    # Pillar 4: Dot-ball & Boundary Prevention (15%)
    ebowl['score_hp_dots'] = scale_series(ebowl['hp_dot_pct'])
    ebowl['score_hp_bound'] = scale_series(ebowl['hp_boundary_pct'], invert=True) # Lower boundary % = higher score
    ebowl['pillar_prevention'] = 0.50 * ebowl['score_hp_dots'] + 0.50 * ebowl['score_hp_bound']
    
    # Pillar 5: Death-Over Performance (10%)
    ebowl['score_death_econ'] = scale_series(ebowl['death_economy'], invert=True)
    ebowl['score_death_wkts'] = scale_series(ebowl['death_wickets_per_100'])
    ebowl['pillar_death'] = 0.55 * ebowl['score_death_econ'] + 0.45 * ebowl['score_death_wkts']
    
    # Pillar 6: Consistency (10%)
    ebowl['pillar_consistency'] = scale_series(ebowl['bowl_econ_std'], invert=True) # Lower std dev = higher consistency
    
    # Raw BOWPRI
    ebowl['raw_bowpri'] = (
        0.30 * ebowl['pillar_baseline'] +
        0.20 * ebowl['pillar_econ'] +
        0.15 * ebowl['pillar_wickets'] +
        0.15 * ebowl['pillar_prevention'] +
        0.10 * ebowl['pillar_death'] +
        0.10 * ebowl['pillar_consistency']
    )
    
    # Empirical Bayesian Shrinkage for Bowlers
    prior_mean_bowl = ebowl['raw_bowpri'].mean()
    K_BOWL = 50.0
    ebowl['shrinkage_weight'] = ebowl['hp_legal_balls'] / (ebowl['hp_legal_balls'] + K_BOWL)
    ebowl['bowpri_score'] = (ebowl['shrinkage_weight'] * ebowl['raw_bowpri']) + ((1.0 - ebowl['shrinkage_weight']) * prior_mean_bowl)
    
    # Confidence Score for Bowlers
    ebowl['confidence_score'] = np.clip((ebowl['hp_legal_balls'] / 200.0) * 100.0, 40.0, 99.0)
    
    ebowl['bowpri_score'] = ebowl['bowpri_score'].round(2)
    ebowl['confidence_score'] = ebowl['confidence_score'].round(1)
    
    # Sort Bowlers
    ranked_bowlers = ebowl.sort_values(by='bowpri_score', ascending=False).reset_index(drop=True)
    ranked_bowlers['rank'] = ranked_bowlers.index + 1
    
    # ---------------------------------------------------------
    # Attach Team and Mapping Metadata
    # ---------------------------------------------------------
    mapping = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw", "competition_team_player_mapping.csv"))
    # Get player most recent team / dominant team
    player_teams = mapping.groupby('player_id')['team_name'].agg(lambda x: x.iloc[-1]).to_dict()
    
    ranked_batters['team'] = ranked_batters['striker_id'].map(player_teams).fillna('Various')
    ranked_bowlers['team'] = ranked_bowlers['bowler_id'].map(player_teams).fillna('Various')
    
    # Rename IDs for uniform representation
    ranked_batters = ranked_batters.rename(columns={'striker_id': 'player_id'})
    
    # Save Full Ranked CSVs
    ranked_batters.to_csv(os.path.join(OUTPUT_DIR, 'all_ranked_batters.csv'), index=False)
    ranked_bowlers.to_csv(os.path.join(OUTPUT_DIR, 'all_ranked_bowlers.csv'), index=False)
    
    # Top 10 Batters and Bowlers
    top10_batters = ranked_batters.head(10).copy()
    top10_bowlers = ranked_bowlers.head(10).copy()
    
    top10_batters.to_csv(os.path.join(OUTPUT_DIR, 'top_10_batters.csv'), index=False)
    top10_bowlers.to_csv(os.path.join(OUTPUT_DIR, 'top_10_bowlers.csv'), index=False)
    
    print("\n================== TOP 10 BATTERS UNDER PRESSURE (BPRI) ==================")
    print(top10_batters[['rank', 'player_id', 'player_name', 'team', 'batting_role', 'matches', 'hp_innings', 'hp_balls', 'hp_avg', 'hp_strike_rate', 'death_strike_rate', 'bpri_score', 'confidence_score']].to_string(index=False))
    
    print("\n================== TOP 10 BOWLERS UNDER PRESSURE (BOWPRI) ==================")
    print(top10_bowlers[['rank', 'bowler_id', 'player_name', 'team', 'bowling_role', 'matches', 'hp_innings', 'hp_overs', 'hp_economy', 'hp_bowling_sr', 'death_economy', 'hp_wickets', 'bowpri_score', 'confidence_score']].to_string(index=False))
    
    return ranked_batters, ranked_bowlers, top10_batters, top10_bowlers

if __name__ == "__main__":
    batters, bowlers, df = compute_player_metrics()
    calculate_bpri_and_bowpri(batters, bowlers, df)

