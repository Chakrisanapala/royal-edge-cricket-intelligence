"""
Data Loader and Initial Inspection Module
SupeRR Selector Season 2 - Rajasthan Royals IPL 2027 Auction Analytics
"""

import os
import pandas as pd
import numpy as np

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def load_raw_datasets():
    """Load all raw CSV datasets with appropriate data types."""
    datasets = {}
    
    files = {
        'competitions': 'competitions.csv',
        'teams': 'teams.csv',
        'matches': 'matches.csv',
        'playing_eleven': 'playing_eleven.csv',
        'mapping': 'competition_team_player_mapping.csv',
        'ball_by_ball': 'ball_by_ball.csv'
    }
    
    for key, filename in files.items():
        filepath = os.path.join(DATA_DIR, filename)
        if os.path.exists(filepath):
            print(f"Loading {filename}...")
            datasets[key] = pd.read_csv(filepath, low_memory=False)
            print(f"  Loaded {key}: {datasets[key].shape[0]:,} rows, {datasets[key].shape[1]} cols")
        else:
            print(f"WARNING: File {filename} not found at {filepath}")
            datasets[key] = None
            
    return datasets

def audit_datasets(datasets):
    """Generate comprehensive audit statistics for all datasets."""
    audit_results = {}
    
    for name, df in datasets.items():
        if df is None:
            continue
        
        info = {
            'shape': df.shape,
            'columns': list(df.columns),
            'dtypes': df.dtypes.to_dict(),
            'null_counts': df.isnull().sum().to_dict(),
            'null_pct': (df.isnull().sum() / len(df) * 100).to_dict(),
            'duplicate_rows': df.duplicated().sum(),
            'memory_mb': round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)
        }
        
        # Key specific checks
        if 'match_id' in df.columns:
            info['unique_matches'] = df['match_id'].nunique()
        if 'player_id' in df.columns:
            info['unique_players'] = df['player_id'].nunique()
        if 'competition_id' in df.columns:
            info['unique_competitions'] = df['competition_id'].nunique()
            
        audit_results[name] = info
        
    return audit_results

if __name__ == "__main__":
    datasets = load_raw_datasets()
    audit = audit_datasets(datasets)
    for name, a in audit.items():
        print(f"\n==================== {name.upper()} ====================")
        print(f"Rows: {a['shape'][0]:,}, Cols: {a['shape'][1]}, Memory: {a['memory_mb']} MB, Duplicates: {a['duplicate_rows']}")
        print("Columns & Missing Values:")
        for col in a['columns']:
            nulls = a['null_counts'][col]
            pct = a['null_pct'][col]
            dtype = str(a['dtypes'][col])
            print(f"  - {col} ({dtype}): {nulls:,} missing ({pct:.2f}%)")

