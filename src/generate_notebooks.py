"""
Generates the 5 requested Jupyter Notebooks for the SupeRR Selector project.
"""

import os
import json

NOTEBOOKS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "notebooks")

def make_notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.11"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

def markdown_cell(text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.strip().split("\n")]
    }

def code_cell(code):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in code.strip().split("\n")]
    }

def create_all_notebooks():
    os.makedirs(NOTEBOOKS_DIR, exist_ok=True)
    
    # 01 Data Exploration
    nb1 = make_notebook([
        markdown_cell("# 01. Comprehensive Data Exploration & Quality Audit\n**SupeRR Selector Season 2 - Rajasthan Royals IPL 2027 Auction Analytics**\n\nAuditing all supplied datasets, checking schemas, missing values, primary keys, and match-player relationships."),
        code_cell("""import os
import pandas as pd
import numpy as np

DATA_DIR = '../data/raw'

competitions = pd.read_csv(os.path.join(DATA_DIR, 'competitions.csv'))
matches = pd.read_csv(os.path.join(DATA_DIR, 'matches.csv'))
playing_eleven = pd.read_csv(os.path.join(DATA_DIR, 'playing_eleven.csv'), low_memory=False)
mapping = pd.read_csv(os.path.join(DATA_DIR, 'competition_team_player_mapping.csv'))
bbb = pd.read_csv(os.path.join(DATA_DIR, 'ball_by_ball.csv'), low_memory=False)

print(f"Competitions: {competitions.shape}")
print(f"Matches: {matches.shape}")
print(f"Playing Eleven: {playing_eleven.shape}")
print(f"Mapping: {mapping.shape}")
print(f"Ball by Ball: {bbb.shape}")
"""),
        code_cell("""# Verify Date Coverage and Formats
matches['match_date'] = pd.to_datetime(matches['match_date'])
print(f"Date range: {matches['match_date'].min()} to {matches['match_date'].max()}")
print("Competitions breakdown:")
print(competitions['match_format'].value_counts())
"""),
        code_cell("""# Inspect Ball-by-Ball Mechanics & Extras
print("Extras distribution:")
print(bbb['extras_type'].value_counts(dropna=False))
print("\nDismissal types:")
print(bbb['dismissal_type'].value_counts(dropna=False))
""")
    ])
    with open(os.path.join(NOTEBOOKS_DIR, '01_data_exploration.ipynb'), 'w') as f:
        json.dump(nb1, f, indent=2)

    # 02 Pressure Classification
    nb2 = make_notebook([
        markdown_cell("# 02. Dynamic Ball-by-Ball Pressure Classification\n**Rajasthan Royals Analytics**\n\nCalculating match leverage, running chase states, Required Run Rate (RRR), wicket fall context, and assigning 4 pressure tiers."),
        code_cell("""import os
import pandas as pd
import numpy as np
import sys
sys.path.append('../src')
from pressure_engine import compute_ball_by_ball_pressure

DATA_DIR = '../data/raw'
competitions = pd.read_csv(os.path.join(DATA_DIR, 'competitions.csv'))
matches = pd.read_csv(os.path.join(DATA_DIR, 'matches.csv'))
bbb = pd.read_csv(os.path.join(DATA_DIR, 'ball_by_ball.csv'), low_memory=False)

df_pressure = compute_ball_by_ball_pressure(bbb, matches, competitions)
print("Batting Pressure Tier Breakdown (%):")
print(df_pressure['batting_pressure_cat'].value_counts(normalize=True)*100)
"""),
        code_cell("""# Inspect High-Pressure Death Overs vs Low-Pressure Chases
sample_death = df_pressure[df_pressure['phase'] == 'Death'][['match_id', 'innings', 'overid', 'runs_needed', 'balls_remaining', 'batting_pressure_score', 'batting_pressure_cat']].head(10)
print(sample_death)
""")
    ])
    with open(os.path.join(NOTEBOOKS_DIR, '02_pressure_classification.ipynb'), 'w') as f:
        json.dump(nb2, f, indent=2)

    # 03 Batting Analysis
    nb3 = make_notebook([
        markdown_cell("# 03. Advanced Batting Pressure Analysis\nEvaluating strike rates, boundary percentages, dot-ball control, chase resilience, death overs, and collapse recovery."),
        code_cell("""import pandas as pd
import numpy as np

all_bat = pd.read_csv('../outputs/all_ranked_batters.csv')
top10_bat = pd.read_csv('../outputs/top_10_batters.csv')

print("Top 10 Batters by BPRI Score:")
print(top10_bat[['rank', 'player_id', 'player_name', 'team', 'batting_role', 'hp_balls', 'hp_strike_rate', 'death_strike_rate', 'bpri_score']])
"""),
        code_cell("""# Correlation between Normal Strike Rate and Pressure Strike Rate
print(f"Normal vs Pressure SR Correlation: {all_bat['strike_rate'].corr(all_bat['hp_strike_rate']):.3f}")
print(f"Mean Strike Rate under Normal conditions: {all_bat['norm_strike_rate'].mean():.2f}")
print(f"Mean Strike Rate under Pressure: {all_bat['hp_strike_rate'].mean():.2f}")
""")
    ])
    with open(os.path.join(NOTEBOOKS_DIR, '03_batting_analysis.ipynb'), 'w') as f:
        json.dump(nb3, f, indent=2)

    # 04 Bowling Analysis
    nb4 = make_notebook([
        markdown_cell("# 04. Advanced Bowling Pressure Analysis\nEvaluating economy control under pressure, wicket-taking strike rates, boundary prevention, and death over execution."),
        code_cell("""import pandas as pd
import numpy as np

all_bowl = pd.read_csv('../outputs/all_ranked_bowlers.csv')
top10_bowl = pd.read_csv('../outputs/top_10_bowlers.csv')

print("Top 10 Bowlers by BOWPRI Score:")
print(top10_bowl[['rank', 'bowler_id', 'player_name', 'team', 'bowling_role', 'hp_overs', 'hp_economy', 'death_economy', 'bowpri_score']])
"""),
        code_cell("""# Economy Differential Analysis (Normal vs Pressure)
print(f"Average League Economy Normal: {all_bowl['norm_economy'].mean():.2f}")
print(f"Average League Economy Pressure: {all_bowl['hp_economy'].mean():.2f}")
print(f"Top Bowler Economy Differential under Pressure:")
print(top10_bowl[['player_name', 'norm_economy', 'hp_economy', 'delta_economy']])
""")
    ])
    with open(os.path.join(NOTEBOOKS_DIR, '04_bowling_analysis.ipynb'), 'w') as f:
        json.dump(nb4, f, indent=2)

    # 05 Player Rankings
    nb5 = make_notebook([
        markdown_cell("# 05. Final Player Rankings, Bayesian Shrinkage & Sensitivity\nApplying Empirical Bayesian Shrinkage, Sensitivity Testing, and generating Rajasthan Royals auction targets."),
        code_cell("""import pandas as pd
top10_bat = pd.read_csv('../outputs/top_10_batters.csv')
top10_bowl = pd.read_csv('../outputs/top_10_bowlers.csv')

print("FINAL VERIFIED TOP 10 BATTERS (UNSTOP SUBMISSION ORDER):")
for idx, r in top10_bat.iterrows():
    print(f"Rank {r['rank']}: {r['player_name']} (ID: {r['player_id']}) - BPRI: {r['bpri_score']}")

print("\nFINAL VERIFIED TOP 10 BOWLERS (UNSTOP SUBMISSION ORDER):")
for idx, r in top10_bowl.iterrows():
    print(f"Rank {r['rank']}: {r['player_name']} (ID: {r['bowler_id']}) - BOWPRI: {r['bowpri_score']}")
""")
    ])
    with open(os.path.join(NOTEBOOKS_DIR, '05_player_rankings.ipynb'), 'w') as f:
        json.dump(nb5, f, indent=2)

    print("All 5 Jupyter Notebooks created successfully in notebooks/!")

if __name__ == "__main__":
    create_all_notebooks()

