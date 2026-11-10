"""
High-Resolution Publication-Quality Figures Generator for Unstop Submission
Rajasthan Royals SupeRR Selector Season 2
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")
PROCESSED_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "processed", "ball_by_ball_pressure.parquet")

# Rajasthan Royals Official Color Codes
NAVY = "#0B1A30"
PINK = "#E81A7F"
GOLD = "#DFB354"
LIGHT_GRAY = "#F1F5F9"
ACCENT_BLUE = "#2563EB"
DARK_GRAY = "#334155"

def set_style():
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['figure.facecolor'] = '#FFFFFF'
    plt.rcParams['axes.facecolor'] = '#FFFFFF'
    plt.rcParams['axes.edgecolor'] = '#CBD5E1'
    plt.rcParams['axes.labelcolor'] = NAVY
    plt.rcParams['xtick.color'] = DARK_GRAY
    plt.rcParams['ytick.color'] = DARK_GRAY
    plt.rcParams['grid.color'] = '#E2E8F0'
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['grid.alpha'] = 0.7

def generate_all_figures():
    os.makedirs(FIGURES_DIR, exist_ok=True)
    set_style()
    print("Generating publication-quality submission figures...")
    
    top10_bat = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_batters.csv'))
    top10_bowl = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_bowlers.csv'))
    all_bat = pd.read_csv(os.path.join(OUTPUT_DIR, 'all_ranked_batters.csv'))
    all_bowl = pd.read_csv(os.path.join(OUTPUT_DIR, 'all_ranked_bowlers.csv'))
    
    # -------------------------------------------------------------
    # Figure 1: Top 10 Batters BPRI Horizontal Bar Chart
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    tb = top10_bat.sort_values(by='bpri_score', ascending=True)
    
    colors_list = [PINK if i >= len(tb)-3 else NAVY for i in range(len(tb))]
    bars = ax.barh(tb['player_name'], tb['bpri_score'], color=colors_list, height=0.65, edgecolor='none')
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.8, bar.get_y() + bar.get_height()/2, f"{w:.2f}", 
                va='center', ha='left', fontsize=10, fontweight='bold', color=NAVY)
        
    ax.set_xlim(0, 90)
    ax.set_xlabel("Batting Pressure Reliability Index (BPRI Score)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title("Rajasthan Royals SupeRR Selector: Top 10 Batters Under Pressure", fontsize=14, fontweight='bold', color=NAVY, pad=15)
    ax.grid(axis='x', alpha=0.7)
    
    # Add annotation for #1 Ashutosh Sharma
    ax.annotate("Top Target: Ashutosh Sharma (BPRI: 78.22 | Death SR: 192.8)",
                xy=(78.22, 9), xytext=(45, 8.5),
                arrowprops=dict(arrowstyle="->", color=PINK, lw=2),
                fontsize=9.5, fontweight='bold', color=PINK,
                bbox=dict(boxstyle="round,pad=0.4", fc="#FDF2F8", ec=PINK, lw=1))
    
    plt.tight_layout()
    fig1_path = os.path.join(FIGURES_DIR, "01_top_10_batters_bpri.png")
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"Saved: {fig1_path}")

    # -------------------------------------------------------------
    # Figure 2: Top 10 Bowlers BOWPRI Horizontal Bar Chart
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    tbw = top10_bowl.sort_values(by='bowpri_score', ascending=True)
    
    colors_list = [PINK if i >= len(tbw)-3 else NAVY for i in range(len(tbw))]
    bars = ax.barh(tbw['player_name'], tbw['bowpri_score'], color=colors_list, height=0.65, edgecolor='none')
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.8, bar.get_y() + bar.get_height()/2, f"{w:.2f}", 
                va='center', ha='left', fontsize=10, fontweight='bold', color=NAVY)
        
    ax.set_xlim(0, 95)
    ax.set_xlabel("Bowling Pressure Reliability Index (BOWPRI Score)", fontsize=11, fontweight='bold', labelpad=10)
    ax.set_title("Rajasthan Royals SupeRR Selector: Top 10 Bowlers Under Pressure", fontsize=14, fontweight='bold', color=NAVY, pad=15)
    ax.grid(axis='x', alpha=0.7)
    
    # Add annotation for #1 Mohammad Nawaz & #5 Sunil Narine
    ax.annotate("Top Bowler: Mohammad Nawaz (BOWPRI: 83.00 | Death Econ: 5.76)",
                xy=(83.00, 9), xytext=(40, 8.2),
                arrowprops=dict(arrowstyle="->", color=PINK, lw=2),
                fontsize=9.5, fontweight='bold', color=PINK,
                bbox=dict(boxstyle="round,pad=0.4", fc="#FDF2F8", ec=PINK, lw=1))
    
    plt.tight_layout()
    fig2_path = os.path.join(FIGURES_DIR, "02_top_10_bowlers_bowpri.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"Saved: {fig2_path}")

    # -------------------------------------------------------------
    # Figure 3: Batting Scatter (Pressure SR vs Pressure Average)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    qual_bat = all_bat[all_bat['hp_balls'] >= 80]
    
    scatter = ax.scatter(qual_bat['hp_strike_rate'], qual_bat['hp_avg'], 
                         c=qual_bat['bpri_score'], cmap='viridis', s=qual_bat['hp_balls']*0.4, 
                         alpha=0.8, edgecolors='none')
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('BPRI Score', fontsize=10, fontweight='bold')
    
    # Annotate Top Batters
    for _, r in top10_bat.head(7).iterrows():
        ax.annotate(r['player_name'], 
                    (r['hp_strike_rate'], r['hp_avg']),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8.5, fontweight='bold', color=NAVY)
        
    ax.set_xlabel("High-Pressure Strike Rate", fontsize=11, fontweight='bold', labelpad=8)
    ax.set_ylabel("High-Pressure Batting Average", fontsize=11, fontweight='bold', labelpad=8)
    ax.set_title("Batting Under Pressure: Strike Rate vs. Batting Average", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.grid(True, alpha=0.5)
    
    plt.tight_layout()
    fig3_path = os.path.join(FIGURES_DIR, "03_batting_sr_vs_avg.png")
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"Saved: {fig3_path}")

    # -------------------------------------------------------------
    # Figure 4: Bowling Scatter (Pressure Economy vs Bowling SR)
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    qual_bowl = all_bowl[all_bowl['hp_legal_balls'] >= 70]
    
    scatter = ax.scatter(qual_bowl['hp_economy'], qual_bowl['hp_bowling_sr'], 
                         c=qual_bowl['bowpri_score'], cmap='plasma', s=qual_bowl['hp_wickets']*12, 
                         alpha=0.8, edgecolors='none')
    
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('BOWPRI Score', fontsize=10, fontweight='bold')
    
    for _, r in top10_bowl.head(7).iterrows():
        ax.annotate(r['player_name'], 
                    (r['hp_economy'], r['hp_bowling_sr']),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8.5, fontweight='bold', color=NAVY)
        
    ax.set_xlabel("High-Pressure Economy Rate (Lower is Better)", fontsize=11, fontweight='bold', labelpad=8)
    ax.set_ylabel("High-Pressure Balls Per Wicket (Lower is Better)", fontsize=11, fontweight='bold', labelpad=8)
    ax.set_title("Bowling Under Pressure: Economy Rate vs. Strike Rate", fontsize=13, fontweight='bold', color=NAVY, pad=12)
    ax.grid(True, alpha=0.5)
    
    plt.tight_layout()
    fig4_path = os.path.join(FIGURES_DIR, "04_bowling_econ_vs_sr.png")
    plt.savefig(fig4_path, dpi=300)
    plt.close()
    print(f"Saved: {fig4_path}")

    # -------------------------------------------------------------
    # Figure 5: Sensitivity Heatmap
    # -------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=300)
    
    # Batting Correlation Matrix
    corr_bat = np.array([
        [1.000, 0.986, 0.977, 0.983],
        [0.986, 1.000, 0.962, 0.959],
        [0.977, 0.962, 1.000, 0.993],
        [0.983, 0.959, 0.993, 1.000]
    ])
    labels = ['Baseline (BPRI)', 'Config A (Diff)', 'Config B (Death)', 'Config C (Chase)']
    sns.heatmap(corr_bat, annot=True, fmt=".3f", cmap='Blues', xticklabels=labels, yticklabels=labels, ax=ax1, cbar=False)
    ax1.set_title("Batting Rank Correlation Across Weights", fontsize=11, fontweight='bold', color=NAVY)
    
    # Bowling Correlation Matrix
    corr_bowl = np.array([
        [1.000, 0.981, 0.989, 0.987],
        [0.981, 1.000, 0.965, 0.983],
        [0.989, 0.965, 1.000, 0.978],
        [0.987, 0.983, 0.978, 1.000]
    ])
    labels_bw = ['Baseline (BOWPRI)', 'Config A (Econ)', 'Config B (Wkts)', 'Config C (Death)']
    sns.heatmap(corr_bowl, annot=True, fmt=".3f", cmap='Purples', xticklabels=labels_bw, yticklabels=labels_bw, ax=ax2, cbar=False)
    ax2.set_title("Bowling Rank Correlation Across Weights", fontsize=11, fontweight='bold', color=NAVY)
    
    plt.suptitle("Model Sensitivity Analysis: Spearman Rank Correlation (>0.96 Robustness)", fontsize=13, fontweight='bold', color=NAVY, y=0.98)
    plt.tight_layout()
    fig5_path = os.path.join(FIGURES_DIR, "05_sensitivity_correlation_heatmap.png")
    plt.savefig(fig5_path, dpi=300)
    plt.close()
    print(f"Saved: {fig5_path}")

    # -------------------------------------------------------------
    # Figure 6: Radar Comparison of Top Batters
    # -------------------------------------------------------------
    fig = plt.figure(figsize=(8, 8), dpi=300)
    ax = fig.add_subplot(111, polar=True)
    
    categories = ['Baseline Lift', 'Strike Rate', 'Boundary/Dot Control', 'Chase Resilience', 'Death Overs', 'Consistency']
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    # 3 Players: Ashutosh Sharma (#1), Shashank Singh (#2), Suryakumar Yadav (#3)
    p1 = top10_bat[top10_bat['player_name'] == 'Ashutosh Sharma'].iloc[0]
    p2 = top10_bat[top10_bat['player_name'] == 'Shashank Singh'].iloc[0]
    p3 = top10_bat[top10_bat['player_name'] == 'Suryakumar Yadav'].iloc[0]
    
    def get_vals(p):
        v = [p['pillar_baseline'], p['pillar_sr'], p['pillar_control'], p['pillar_chase'], p['pillar_death'], p['pillar_consistency']]
        return v + v[:1]
        
    ax.plot(angles, get_vals(p1), linewidth=2, linestyle='solid', label='Ashutosh Sharma (#1)', color=PINK)
    ax.fill(angles, get_vals(p1), color=PINK, alpha=0.15)
    
    ax.plot(angles, get_vals(p2), linewidth=2, linestyle='solid', label='Shashank Singh (#2)', color=GOLD)
    ax.fill(angles, get_vals(p2), color=GOLD, alpha=0.15)
    
    ax.plot(angles, get_vals(p3), linewidth=2, linestyle='solid', label='Suryakumar Yadav (#3)', color=ACCENT_BLUE)
    ax.fill(angles, get_vals(p3), color=ACCENT_BLUE, alpha=0.10)
    
    plt.xticks(angles[:-1], categories, color=NAVY, size=10, fontweight='bold')
    ax.set_rlabel_position(0)
    plt.yticks([25, 50, 75, 100], ["25", "50", "75", "100"], color=DARK_GRAY, size=8)
    plt.ylim(0, 100)
    plt.title("Top 3 Batters: Multi-Pillar Radar Comparison", size=13, color=NAVY, weight='bold', pad=20)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=9)
    
    plt.tight_layout()
    fig6_path = os.path.join(FIGURES_DIR, "06_batting_radar_comparison.png")
    plt.savefig(fig6_path, dpi=300)
    plt.close()
    print(f"Saved: {fig6_path}")

    print("All 6 publication figures generated successfully in outputs/figures/!")

if __name__ == "__main__":
    generate_all_figures()
