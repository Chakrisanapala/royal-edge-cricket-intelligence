"""
Check exact scorecards against known match results to verify runs calculation.
"""

import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def verify_scorecard():
    bbb = pd.read_csv(os.path.join(DATA_DIR, 'ball_by_ball.csv'), low_memory=False)
    matches = pd.read_csv(os.path.join(DATA_DIR, 'matches.csv'))
    
    # Check match 13511
    m_bbb = bbb[bbb['match_id'] == 13511]
    
    for inn in [1, 2]:
        inn_df = m_bbb[m_bbb['innings'] == inn]
        batter_runs = inn_df['runs'].sum()
        
        # Check extras
        wides = (inn_df['extras_type'] == 'wide').sum()
        noballs = (inn_df['extras_type'] == 'Overstep').sum()
        legbyes = (inn_df['extras_type'] == 'legbyes').sum()
        byes = (inn_df['extras_type'] == 'byes').sum()
        other = (inn_df['extras_type'] == 'other').sum()
        
        # Check extras_2_runs
        ext2 = inn_df['extras_2_runs'].sum()
        
        print(f"Match 13511 Innings {inn}:")
        print(f"  Batter runs: {batter_runs}")
        print(f"  Wides count: {wides}, Overstep count: {noballs}, Legbyes: {legbyes}, Byes: {byes}, Other: {other}")
        print(f"  Extras 2 sum: {ext2}")
        print(f"  Total wickets: {inn_df['is_wicket'].sum()}")
        print(f"  Dismissals: {inn_df[inn_df['is_wicket'] == True]['dismissal_type'].value_counts().to_dict()}")

    # Check match 1358 (IPL 2022 Match 1) or another IPL match
    ipl_matches = matches[matches['comp_id'] == 1358]
    print("\nIPL 2022 first match in dataset:")
    print(ipl_matches[['match_id', 'match_number', 'home_team', 'away_team', 'result']].head(3))
    
    sample_ipl_id = ipl_matches['match_id'].iloc[0]
    ipl_bbb = bbb[bbb['match_id'] == sample_ipl_id]
    for inn in [1, 2]:
        inn_df = ipl_bbb[ipl_bbb['innings'] == inn]
        print(f"IPL Match {sample_ipl_id} Innings {inn}: Batter runs: {inn_df['runs'].sum()}, Wides: {(inn_df['extras_type']=='wide').sum()}, NoBalls: {(inn_df['extras_type']=='Overstep').sum()}, Byes: {(inn_df['extras_type']=='byes').sum()}, Legbyes: {(inn_df['extras_type']=='legbyes').sum()}, Wickets: {inn_df['is_wicket'].sum()}")

if __name__ == "__main__":
    verify_scorecard()

