"""
Investigate extras fields and match totals to verify exact runs calculation.
"""

import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def check_extras():
    bbb = pd.read_csv(os.path.join(DATA_DIR, 'ball_by_ball.csv'), low_memory=False)
    matches = pd.read_csv(os.path.join(DATA_DIR, 'matches.csv'))
    
    print("=== EXTRAS1_RUNS vs EXTRAS_TYPE ===")
    print(bbb.groupby('extras_type', dropna=False)['extras1_runs'].value_counts().unstack().fillna(0))
    
    print("\n=== EXTRAS_2_RUNS vs EXTRAS_TYPE ===")
    print(bbb.groupby('extras_type', dropna=False)['extras_2_runs'].value_counts().unstack().fillna(0))
    
    # Check a single full match innings to see score progression
    sample_match_id = bbb['match_id'].iloc[0]
    match_df = bbb[(bbb['match_id'] == sample_match_id) & (bbb['innings'] == 1)]
    print(f"\nSample match {sample_match_id}, Innings 1 total balls: {len(match_df)}")
    print(match_df[['overid', 'over_ball_num', 'innings_ball_num', 'striker_name', 'bowler_name', 
                    'runs', 'extras_type', 'extras1_runs', 'extras_2_runs', 'is_wicket', 'dismissal_type']].head(20))
    
    # Let's inspect rows where extras_type is NaN vs extras1_runs
    print("\nValue counts of extras1_runs when extras_type is NaN:")
    print(bbb[bbb['extras_type'].isna()]['extras1_runs'].value_counts())
    print("\nValue counts of extras_2_runs when extras_type is NaN:")
    print(bbb[bbb['extras_type'].isna()]['extras_2_runs'].value_counts())

if __name__ == "__main__":
    check_extras()

