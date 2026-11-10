"""
Detailed Dataset Inspection Script
Analyzes competitions, ball-by-ball mechanics, extras, wickets, and player linkage.
"""

import os
import pandas as pd
import numpy as np

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def explore():
    comp = pd.read_csv(os.path.join(DATA_DIR, 'competitions.csv'))
    matches = pd.read_csv(os.path.join(DATA_DIR, 'matches.csv'))
    bbb = pd.read_csv(os.path.join(DATA_DIR, 'ball_by_ball.csv'), low_memory=False)
    mapping = pd.read_csv(os.path.join(DATA_DIR, 'competition_team_player_mapping.csv'))
    
    print("=== COMPETITIONS SUMMARY ===")
    print(comp.groupby(['match_format', 'season']).agg({'comp_id': 'count', 'comp_name': 'unique'}))
    
    # Check IPL vs T20I in comp
    ipl_comps = comp[comp['comp_name'].str.contains('Indian Premier League|IPL', case=False, na=False)]
    print("\n=== IPL COMPETITIONS ===")
    print(ipl_comps[['comp_id', 'comp_name', 'season', 'match_format']])
    
    print("\n=== ALL FORMATS IN COMPETITIONS ===")
    print(comp['match_format'].value_counts())
    
    print("\n=== MATCH DATES RANGE ===")
    matches['match_date'] = pd.to_datetime(matches['match_date'], errors='coerce')
    print(f"Min match date: {matches['match_date'].min()}, Max match date: {matches['match_date'].max()}")
    
    # Check match linkage
    matches_in_bbb = bbb['match_id'].nunique()
    total_matches = matches['match_id'].nunique()
    print(f"\nUnique matches in matches.csv: {total_matches}, in ball_by_ball.csv: {matches_in_bbb}")
    
    # Check overid range
    print(f"\nOverid unique values: {sorted(bbb['overid'].unique())}")
    print(f"Innings unique values: {sorted(bbb['innings'].unique())}")
    print(f"Innings value counts:\n{bbb['innings'].value_counts()}")
    
    # Check extras_type and runs mechanics
    print("\n=== EXTRAS TYPE VALUE COUNTS ===")
    print(bbb['extras_type'].value_counts(dropna=False))
    
    print("\n=== SAMPLE WITH EXTRAS ===")
    sample_extras = bbb[bbb['extras_type'].notnull()][['extras_type', 'extras1_runs', 'extras_2_runs', 'runs', 'is_four', 'is_six']].drop_duplicates().head(15)
    print(sample_extras)
    
    print("\n=== DISMISSAL TYPES ===")
    print(bbb['dismissal_type'].value_counts(dropna=False))
    
    # Check runs when is_four is True and is_six is True
    print("\n=== RUNS DISTRIBUTION FOR FOURS AND SIXES ===")
    print("Fours runs values:", bbb[bbb['is_four'] == True]['runs'].value_counts())
    print("Sixes runs values:", bbb[bbb['is_six'] == True]['runs'].value_counts())
    
    # Check if runs is batter runs or total runs
    print("\n=== SAMPLE DELIVERIES (RUNS VS EXTRAS) ===")
    print(bbb[['runs', 'extras_type', 'extras1_runs', 'extras_2_runs']].head(10))
    
    # Check players in ball_by_ball vs mapping
    strikers = set(bbb['striker_id'].unique())
    bowlers = set(bbb['bowler_id'].unique())
    all_bbb_players = strikers.union(bowlers)
    mapped_players = set(mapping['player_id'].unique())
    print(f"\nUnique strikers in BBB: {len(strikers)}")
    print(f"Unique bowlers in BBB: {len(bowlers)}")
    print(f"Total unique players in BBB: {len(all_bbb_players)}")
    print(f"Total unique players in mapping: {len(mapped_players)}")
    print(f"BBB players present in mapping: {len(all_bbb_players.intersection(mapped_players))} / {len(all_bbb_players)}")
    
if __name__ == "__main__":
    explore()

