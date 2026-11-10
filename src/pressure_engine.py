"""
Pressure Classification Engine (Vectorized High-Performance Implementation)
Calculates ball-by-ball match state, dynamic leverage, and pressure scores
for both batters and bowlers.
"""

import os
import pandas as pd
import numpy as np

def compute_ball_by_ball_pressure(bbb_df, matches_df, competitions_df):
    """
    Computes dynamic ball-by-ball pressure scores and categories using vectorized operations.
    Returns processed DataFrame with all dynamic state columns.
    """
    print("Enriching ball-by-ball data with match metadata...")
    
    # 1. Merge match metadata
    match_meta = matches_df[['match_id', 'comp_id', 'knock_out', 'revised_target', 'second_inn_revised_overs']].copy()
    comp_meta = competitions_df[['comp_id', 'comp_name', 'match_format', 'season']].copy()
    match_meta = match_meta.merge(comp_meta, on='comp_id', how='left')
    
    df = bbb_df.merge(match_meta, on='match_id', how='left')
    df['knock_out'] = df['knock_out'].fillna(0).astype(int)
    
    # 2. Sort accurately to maintain chronological ball order
    print("Sorting deliveries by match, innings, and innings_ball_num...")
    df = df.sort_values(by=['match_id', 'innings', 'innings_ball_num']).reset_index(drop=True)
    
    # 3. Ball accounting: Legal deliveries & runs (Vectorized)
    extras = df['extras_type'].fillna('')
    extras_2 = df['extras_2_runs'].fillna(0).astype(int)
    runs = df['runs'].fillna(0).astype(int)
    
    df['is_legal_batter'] = (extras != 'wide')
    df['is_legal_bowler'] = (~extras.isin(['wide', 'Overstep']))
    df['batter_runs'] = runs
    
    # Bowler runs conceded (vectorized)
    # wide: 1 + extras_2
    # Overstep: 1 + runs + extras_2
    # byes/legbyes: 0
    # penalty: 0
    # normal: runs
    bowler_runs = np.where(
        extras == 'wide', 1 + extras_2,
        np.where(
            extras == 'Overstep', 1 + runs + extras_2,
            np.where(
                extras.isin(['byes', 'legbyes', 'Penalty']), 0,
                runs + extras_2
            )
        )
    )
    df['bowler_runs_conceded'] = bowler_runs
    
    # Team runs delivery (vectorized)
    team_runs = np.where(
        extras == 'wide', 1 + extras_2,
        np.where(
            extras == 'Overstep', 1 + runs + extras_2,
            np.where(
                extras.isin(['byes', 'legbyes']), runs + 1 + extras_2,
                np.where(
                    extras == 'Penalty', 5,
                    runs + extras_2
                )
            )
        )
    )
    df['team_runs_delivery'] = team_runs
    
    # Bowler wicket flag (excluding run outs, retirements, obstructing field)
    bowler_dismissals = {'Caught', 'Bowled', 'LBW', 'Stump', 'Hit Wicket'}
    df['is_bowler_wicket'] = (df['is_wicket'] == True) & (df['dismissal_type'].isin(bowler_dismissals))
    df['is_batter_out'] = (df['is_wicket'] == True)
    
    # 4. Groupby match and innings to compute running states
    print("Computing running innings states (cumulative runs, wickets, balls remaining)...")
    grp = df.groupby(['match_id', 'innings'])
    
    df['cum_legal_balls'] = grp['is_legal_bowler'].cumsum() - df['is_legal_bowler']
    df['cum_runs_before'] = grp['team_runs_delivery'].cumsum() - df['team_runs_delivery']
    df['cum_wickets_before'] = grp['is_wicket'].cumsum() - df['is_wicket']
    df['wickets_in_hand'] = np.clip(10 - df['cum_wickets_before'], 0, 10)
    
    # Scheduled balls
    df['scheduled_balls'] = 120
    mask_revised = (df['innings'] == 2) & (df['second_inn_revised_overs'].notnull()) & (df['second_inn_revised_overs'] > 0)
    df.loc[mask_revised, 'scheduled_balls'] = df.loc[mask_revised, 'second_inn_revised_overs']
    df['balls_remaining'] = np.clip(df['scheduled_balls'] - df['cum_legal_balls'], 0, 120)
    
    # 5. Determine Target for Innings 2
    print("Determining first innings totals and chase targets...")
    inn1_totals = df[df['innings'] == 1].groupby('match_id')['team_runs_delivery'].sum()
    df['inn1_total'] = df['match_id'].map(inn1_totals)
    
    df['target'] = np.where(
        df['innings'] == 1, np.nan,
        np.where(
            df['revised_target'].notnull() & (df['revised_target'] > 0),
            df['revised_target'],
            df['inn1_total'] + 1.0
        )
    )
    
    # Runs needed and RRR
    df['runs_needed'] = np.where(df['innings'] == 2, np.clip(df['target'] - df['cum_runs_before'], 0, 300), np.nan)
    
    balls_rem = df['balls_remaining'].values
    needed = df['runs_needed'].values
    innings = df['innings'].values
    
    # RRR vectorized
    with np.errstate(divide='ignore', invalid='ignore'):
        rrr_calc = np.where(balls_rem > 0, (needed / balls_rem) * 6.0, 36.0)
    rrr_calc = np.where(needed <= 0, 0.0, rrr_calc)
    df['required_run_rate'] = np.where(innings == 2, rrr_calc, np.nan)
    
    # CRR vectorized
    cum_legal = df['cum_legal_balls'].values
    cum_runs = df['cum_runs_before'].values
    with np.errstate(divide='ignore', invalid='ignore'):
        crr_calc = np.where(cum_legal > 0, (cum_runs / cum_legal) * 6.0, 6.0)
    df['current_run_rate'] = crr_calc
    
    # 6. Vectorized Pressure Calculation
    print("Vectorizing dynamic pressure scores (BPRI & BOWPRI delivery scores)...")
    overid = df['overid'].values
    knockout = df['knock_out'].values
    cum_wickets = df['cum_wickets_before'].values
    wickets_in_hand = df['wickets_in_hand'].values
    
    # --- INNINGS 1 PRESSURE ---
    # Phase bases
    # Powerplay (overid <= 6)
    inn1_bat = np.where(
        overid <= 6,
        np.where(cum_wickets >= 3, 65.0, np.where(cum_wickets == 2, 45.0, 30.0)),
        np.where(
            overid <= 15,
            np.where(cum_wickets >= 4, 65.0, 40.0),
            # Death overs (16-20)
            np.where(wickets_in_hand >= 5, 65.0 + (overid - 16) * 3.0, 72.0 + (overid - 16) * 2.0)
        )
    )
    
    inn1_bowl = np.where(
        overid <= 6,
        np.where(cum_wickets >= 3, 50.0, 35.0),
        np.where(
            overid <= 15,
            np.where((cum_wickets <= 1) & (crr_calc >= 9.0), 60.0, 40.0),
            # Death overs
            np.where(wickets_in_hand >= 5, 68.0 + (overid - 16) * 3.5, 55.0)
        )
    )
    
    inn1_bat += knockout * 8.0
    inn1_bowl += knockout * 8.0
    
    # --- INNINGS 2 PRESSURE ---
    rrr_clean = np.nan_to_num(rrr_calc, nan=8.5)
    # Logistic sigmoid
    rrr_factor = 100.0 / (1.0 + np.exp(-0.45 * (rrr_clean - 9.0)))
    wkt_mult = 1.0 + np.maximum(0.0, (5 - wickets_in_hand) * 0.08)
    
    inn2_bat = rrr_factor * wkt_mult
    inn2_bowl = rrr_factor.copy()
    
    # Endgame leverage adjustment (last 4 overs)
    mask_endgame = (balls_rem <= 24) & (needed > 0)
    close_mask = mask_endgame & (needed <= balls_rem * 2.2)
    far_mask = mask_endgame & (needed > balls_rem * 2.2)
    
    inn2_bat = np.where(close_mask, np.maximum(inn2_bat, 70.0 + (24 - balls_rem) * 1.0), inn2_bat)
    inn2_bat = np.where(far_mask, np.minimum(inn2_bat, 85.0), inn2_bat)
    
    inn2_bowl = np.where(close_mask, np.maximum(inn2_bowl, 72.0 + (24 - balls_rem) * 1.0), inn2_bowl)
    inn2_bowl = np.where(far_mask, 45.0, inn2_bowl)
    
    # Low pressure dead rubbers in chase
    mask_dead_chase = (needed <= 20) & (balls_rem >= 30) & (wickets_in_hand >= 6)
    inn2_bat = np.where(mask_dead_chase, 20.0, inn2_bat)
    inn2_bowl = np.where(mask_dead_chase, 20.0, inn2_bowl)
    
    inn2_bat += knockout * 8.0
    inn2_bowl += knockout * 8.0
    
    # Combine Innings 1, 2, and Super Overs (3+)
    bat_score = np.where(
        innings == 1, inn1_bat,
        np.where(innings == 2, inn2_bat, 95.0)
    )
    bowl_score = np.where(
        innings == 1, inn1_bowl,
        np.where(innings == 2, inn2_bowl, 95.0)
    )
    
    # Clip to [5, 100]
    df['batting_pressure_score'] = np.clip(bat_score, 5.0, 100.0)
    df['bowling_pressure_score'] = np.clip(bowl_score, 5.0, 100.0)
    
    # 7. Vectorized Categorical Classification
    b_score = df['batting_pressure_score'].values
    bw_score = df['bowling_pressure_score'].values
    
    def get_cat(score_arr):
        return np.where(
            score_arr < 35.0, 'LOW PRESSURE',
            np.where(
                score_arr < 60.0, 'MODERATE PRESSURE',
                np.where(score_arr < 80.0, 'HIGH PRESSURE', 'EXTREME PRESSURE')
            )
        )
        
    df['batting_pressure_cat'] = get_cat(b_score)
    df['bowling_pressure_cat'] = get_cat(bw_score)
    
    df['is_high_pressure_bat'] = df['batting_pressure_score'] >= 60.0
    df['is_high_pressure_bowl'] = df['bowling_pressure_score'] >= 60.0
    
    # Innings phase label
    df['phase'] = pd.cut(
        df['overid'], 
        bins=[0, 6, 15, 20], 
        labels=['Powerplay', 'Middle', 'Death']
    )
    
    print("Pressure computation complete!")
    return df

if __name__ == "__main__":
    from data_loader import load_raw_datasets
    datasets = load_raw_datasets()
    processed_df = compute_ball_by_ball_pressure(
        datasets['ball_by_ball'], 
        datasets['matches'], 
        datasets['competitions']
    )
    
    print("\n=== BATTING PRESSURE DISTRIBUTION ===")
    print(processed_df['batting_pressure_cat'].value_counts(normalize=True) * 100)
    
    print("\n=== BOWLING PRESSURE DISTRIBUTION ===")
    print(processed_df['bowling_pressure_cat'].value_counts(normalize=True) * 100)
    
    print("\n=== PRESSURE BY PHASE (BATTING) ===")
    print(pd.crosstab(processed_df['phase'], processed_df['batting_pressure_cat'], normalize='index') * 100)
    
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed", "ball_by_ball_pressure.parquet")
    processed_df.to_parquet(out_path, index=False)
    print(f"\nSaved processed pressure dataset to: {out_path} ({round(os.path.getsize(out_path)/(1024*1024), 2)} MB)")
