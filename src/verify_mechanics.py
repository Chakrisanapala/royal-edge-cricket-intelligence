"""
Detailed check on how runs, extras, and wickets are recorded.
"""

import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def verify_ball_mechanics():
    bbb = pd.read_csv(os.path.join(DATA_DIR, 'ball_by_ball.csv'), low_memory=False)
    matches = pd.read_csv(os.path.join(DATA_DIR, 'matches.csv'))
    
    print("=== SAMPLE WIDE BALLS ===")
    wides = bbb[bbb['extras_type'] == 'wide']
    print(wides[['overid', 'over_ball_num', 'runs', 'extras_type', 'extras1_runs', 'extras_2_runs', 'is_four', 'is_six']].head(10))
    print("\nRuns distribution on wides:")
    print(wides['runs'].value_counts())
    print("\nExtras 2 runs distribution on wides:")
    print(wides['extras_2_runs'].value_counts())
    
    print("\n=== SAMPLE NO-BALLS (OVERSTEP) ===")
    noballs = bbb[bbb['extras_type'] == 'Overstep']
    print(noballs[['overid', 'over_ball_num', 'runs', 'extras_type', 'extras1_runs', 'extras_2_runs', 'is_four', 'is_six']].head(10))
    print("\nRuns distribution on no-balls:")
    print(noballs['runs'].value_counts())
    print("\nExtras 2 runs distribution on no-balls:")
    print(noballs['extras_2_runs'].value_counts())
    
    print("\n=== SAMPLE BYES / LEGBYES ===")
    byes = bbb[bbb['extras_type'].isin(['byes', 'legbyes'])]
    print(byes[['overid', 'over_ball_num', 'runs', 'extras_type', 'extras1_runs', 'extras_2_runs']].head(10))
    print("\nRuns distribution on byes/legbyes:")
    print(byes['runs'].value_counts())
    
    # Check legal delivery: does over_ball_num repeat or how is it tracked?
    print("\n=== SAMPLE OVER WITH WIDE OR NO-BALL ===")
    sample_match = wides['match_id'].iloc[0]
    sample_over = wides[wides['match_id'] == sample_match]['overid'].iloc[0]
    over_deliveries = bbb[(bbb['match_id'] == sample_match) & (bbb['innings'] == 1) & (bbb['overid'] == sample_over)]
    print(over_deliveries[['overid', 'over_ball_num', 'innings_ball_num', 'striker_name', 'bowler_name', 'runs', 'extras_type', 'extras1_runs', 'extras_2_runs']])
    
    # Check total score of an innings compared to sum of runs
    print("\n=== CHECK INNINGS TOTAL RUNS VS MATCH RESULT ===")
    m1 = matches[matches['match_id'] == sample_match].iloc[0]
    print(f"Match {sample_match}: {m1['home_team']} vs {m1['away_team']}, result: {m1['result']}")
    inn1_df = bbb[(bbb['match_id'] == sample_match) & (bbb['innings'] == 1)]
    inn2_df = bbb[(bbb['match_id'] == sample_match) & (bbb['innings'] == 2)]
    print(f"Inn 1 total batter runs: {inn1_df['runs'].sum()}")
    print(f"Inn 1 wides count: {(inn1_df['extras_type'] == 'wide').sum()}")
    print(f"Inn 1 overstep count: {(inn1_df['extras_type'] == 'Overstep').sum()}")
    print(f"Inn 1 byes/legbyes: {inn1_df['extras_type'].isin(['byes', 'legbyes']).sum()}")
    print(f"Inn 2 total batter runs: {inn2_df['runs'].sum()}")

if __name__ == "__main__":
    verify_ball_mechanics()

