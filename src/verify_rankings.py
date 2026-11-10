"""
Verify Top 10 Player Mappings, Roles, and Data Integrity
"""

import os
import pandas as pd

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def verify():
    mapping = pd.read_csv(os.path.join(DATA_DIR, 'competition_team_player_mapping.csv'))
    t10_bat = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_batters.csv'))
    t10_bowl = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_bowlers.csv'))
    
    print("=== TOP 10 BATTERS VERIFICATION ===")
    for idx, r in t10_bat.iterrows():
        m = mapping[mapping['player_id'] == r['player_id']]
        names = list(m['player_name'].unique())
        teams = list(m['team_name'].unique())
        print(f"Rank {r['rank']}: ID={r['player_id']}, Output Name='{r['player_name']}', Mapping Names={names}, Teams={teams}")
        
    print("\n=== TOP 10 BOWLERS VERIFICATION ===")
    for idx, r in t10_bowl.iterrows():
        m = mapping[mapping['player_id'] == r['bowler_id']]
        names = list(m['player_name'].unique())
        teams = list(m['team_name'].unique())
        print(f"Rank {r['rank']}: ID={r['bowler_id']}, Output Name='{r['player_name']}', Mapping Names={names}, Teams={teams}")

if __name__ == "__main__":
    verify()

