"""
Deep dive into extras_type and extras_2_runs to verify exact run formulas.
"""

import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def inspect_all_extras():
    bbb = pd.read_csv(os.path.join(DATA_DIR, 'ball_by_ball.csv'), low_memory=False)
    
    print("=== Unique combinations of extras_type, extras_2_runs, runs ===")
    combos = bbb.groupby(['extras_type', 'extras_2_runs', 'runs']).size().reset_index(name='count')
    print(combos.to_string())

if __name__ == "__main__":
    inspect_all_extras()

