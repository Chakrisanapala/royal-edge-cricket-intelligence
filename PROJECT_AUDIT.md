# ROYAL EDGE — Project & Stitch Export Audit (Phase 0)
**Project Title:** ROYAL EDGE: Rajasthan Royals — IPL 2027 Auction Intelligence Platform  
**Subtitle:** Data-Driven Player Scouting, Pressure Reliability and Auction Strategy Command Center  
**Challenge:** SupeRR Selector Season 2 — Round 1  
**Project Workspace:** `D:\Desktop\RR - Hackathon`  
**Date:** November 10, 2026  

---

## 1. Executive Summary & Audit Purpose

This audit establishes the comprehensive technical inventory of the Rajasthan Royals cricket analytics repository and evaluates the two supplied Stitch AI export folders:
- **Folder 1:** `D:\Downloads\stitch_royal_edge_cricket_intelligence_platform (1)`
- **Folder 2:** `D:\Downloads\stitch_royal_edge_cricket_intelligence_platform`

The audit confirms that **Folder 1** contains the definitive, production-complete version of all eight screens in full desktop format (1440px) accompanied by the official `DESIGN.md` theme token specification. All analytical models, raw data stores, and verified player rankings are preserved in their pristine, read-only state.

---

## 2. Comparative Audit of the Two Stitch Export Folders

| Dimension | Folder 2 (`...platform`) | Folder 1 (`...platform (1)`) | Audit Verdict |
| :--- | :--- | :--- | :--- |
| **Directory Path** | `D:\Downloads\stitch_royal_edge_cricket_intelligence_platform` | `D:\Downloads\stitch_royal_edge_cricket_intelligence_platform (1)` | **Folder 1 is the authoritative master** |
| **Total Screens** | 4 Screens (plus mobile drafts) | **8 Complete Screens** (1440px Desktop) | Folder 1 contains 100% of required screens |
| **Design System** | `DESIGN.md` (10,753 bytes) | `DESIGN.md` (10,753 bytes) | Identical token specifications |
| **Executive Overview** | Draft + Desktop (56.8 KB) | Final Desktop (53.0 KB) | Folder 1 has unified navigation anchors |
| **Pressure Engine** | Draft + Desktop (60.9 KB) | Final Desktop (38.0 KB clean structure) | Folder 1 includes clean SVG leverage curves |
| **Batting Analytics** | Draft + Desktop (57.7 KB) | Final Desktop (66.2 KB) | Folder 1 has full 10-row tabular data grid |
| **Bowling Analytics** | Draft + Desktop (67.3 KB) | Final Desktop (64.1 KB) | Folder 1 features dual-tab BCCI separation |
| **Player Comparison** | *Missing* | **Present (5 variants)** | Folder 1 Variant 5 is full 6-axis radar |
| **Auction War Room** | *Missing* | **Present (2 variants)** | Folder 1 Variant 2 has dynamic purse simulator |
| **Player Profile** | *Missing* | **Present (2 dossiers)** | Ashutosh Sharma dossier with phase splits |
| **Methodology** | *Missing* | **Present (58.4 KB)** | Complete mathematical equation framework |

### Master Source-to-Implementation Mapping
All screen assets from Folder 1 have been copied and structured into `d:\Desktop\RR - Hackathon\stitch_screens/`:
1. `executive_overview_franchise_intelligence` -> `stitch_screens/screen_01_executive_overview.html` & `.png`
2. `pressure_intelligence_dynamic_leverage_engine` -> `stitch_screens/screen_02_pressure_intelligence.html` & `.png`
3. `batting_analytics_bpri_pressure_rankings` -> `stitch_screens/screen_03_batting_analytics.html` & `.png`
4. `bowling_analytics_bowpri_pressure_matrix` -> `stitch_screens/screen_04_bowling_analytics.html` & `.png`
5. `player_comparison_head_to_head_pressure_radar_5` -> `stitch_screens/screen_05_player_comparison.html` & `.png`
6. `auction_war_room_franchise_strategy_console_2` -> `stitch_screens/screen_06_auction_war_room.html` & `.png`
7. `player_intelligence_profile_ashutosh_sharma` -> `stitch_screens/screen_07_player_intelligence_profile.html` & `.png`
8. `methodology_reliability_statistical_framework` -> `stitch_screens/screen_08_methodology_reliability.html` & `.png`
9. `royal_edge_intelligence/DESIGN.md` -> `stitch_screens/DESIGN.md`

---

## 3. Existing Codebase Architecture & Analytical Engine

The project structure in `D:\Desktop\RR - Hackathon` comprises:
* **Raw Data (`data/raw/`):**
  - `ball_by_ball.csv`: 200,999 delivery-level tracking rows.
  - `matches.csv`: 867 matches across 2022–2026.
  - `competitions.csv`, `teams.csv`, `playing_eleven.csv`, `competition_team_player_mapping.csv`.
* **Processed Analytics Store (`data/processed/`):**
  - `ball_by_ball_pressure.parquet` (5.41 MB): Vectorized leverage indices.
* **Core Computational Modules (`src/`):**
  - `data_loader.py`: Schema validation, entity mapping.
  - `pressure_engine.py`: Vectorized Dynamic RRR Sigmoid ($L_t = \sigma(k_1 \cdot \text{RRR} - c) \cdot (1 + \text{wickets\_lost}/10) \cdot E_t$).
  - `metrics_engine.py`: Regularized BPRI & BOWPRI calculations with Empirical Bayesian Shrinkage ($K_{\text{bat}}=60$, $K_{\text{bowl}}=50$) and Sample Size Saturation Index (SSSI %).
  - `validation.py`: 1,000-resample non-parametric cluster bootstrap (95% CIs).
  - `scouting_strategy.py`: Tactical role matching, Sawai Mansingh venue boundary analytics.
* **Verified Deliverables (`final_submission/`):**
  - `RR_Top_10_Batters.csv`: Official audited top 10 batters.
  - `RR_Top_10_Bowlers.csv`: Official audited top 10 bowlers.
  - `RR_Methodology.md`: Official audited methodology.
* **Streamlit Fallback Application (`dashboard/app.py`):**
  - Active and validated on Port 8502.

---

## 4. Scientific Verification & Data Governance

The verified reference statistics are mathematically locked:
* **Batters:**
  1. Ashutosh Sharma (BPRI: 78.22 | HP SR: 168.62 | 95% CI: [148.67, 189.74] | SSSI: 99.0%)
  2. Shashank Singh (BPRI: 77.73 | HP SR: 170.53 | 95% CI: [153.65, 186.79] | SSSI: 99.0%)
  3. Suryakumar Yadav (BPRI: 76.90 | HP SR: 182.69 | 95% CI: [170.25, 194.43] | SSSI: 99.0%)
  4. Tom Banton (BPRI: 74.05 | HP SR: 186.84 | 95% CI: [152.63, 222.83] | SSSI: 45.6%)
  5. Reeza Hendricks (BPRI: 72.93 | HP SR: 169.59 | 95% CI: [151.23, 188.77] | SSSI: 99.0%)
  6. Naman Dhir (BPRI: 72.91 | HP SR: 186.26 | 95% CI: [168.13, 207.02] | SSSI: 99.0%)
  7. Quinton de Kock (BPRI: 72.20 | HP SR: 170.33 | 95% CI: [153.41, 188.36] | SSSI: 99.0%)
  8. Phil Salt (BPRI: 72.12 | HP SR: 187.33 | 95% CI: [164.03, 209.61] | SSSI: 99.0%)
  9. Rishabh Pant (BPRI: 71.31 | HP SR: 176.53 | 95% CI: [157.93, 193.46] | SSSI: 99.0%)
  10. Tim David (BPRI: 71.28 | HP SR: 181.32 | 95% CI: [169.48, 194.67] | SSSI: 99.0%)
* **Bowlers:**
  1. Mohammad Nawaz (BOWPRI: 83.00 | Statistical Benchmark / BCCI Policy Ineligible)
  2. Abrar Ahmed (BOWPRI: 77.96 | Statistical Benchmark / BCCI Policy Ineligible)
  3. Matthew Humphreys (BOWPRI: 76.68 | Actionable Target #1 Overseas)
  4. George Linde (BOWPRI: 76.10 | Actionable Target #2 Overseas)
  5. Sunil Narine (BOWPRI: 75.71 | Actionable Target #3 Overseas)
  6. Imad Wasim (BOWPRI: 75.62 | Statistical Benchmark / BCCI Policy Ineligible)
  7. Corbin Bosch (BOWPRI: 74.56 | Actionable Target #4 Overseas)
  8. Hasan Mahmud (BOWPRI: 74.09 | Actionable Target #5 Overseas)
  9. Sufiyan Muqeem (BOWPRI: 73.81 | Statistical Benchmark / BCCI Policy Ineligible)
  10. Mitchell Santner (BOWPRI: 73.53 | Actionable Target #6 Overseas)

---

## 5. Implementation Roadmap

The full-stack application will be constructed across two coordinated layers:
1. **Backend Layer (`backend/`):**
   - Framework: FastAPI + Uvicorn + Pydantic v2.
   - Purpose: Expose high-performance JSON endpoints directly backed by the audited CSV files and Parquet data store.
   - Zero analytical duplication in JavaScript.
2. **Frontend Layer (`frontend/`):**
   - Framework: React 18 + Vite + TypeScript + Tailwind CSS + Recharts + Lucide Icons + React Router v6.
   - Theme: Midnight Navy (`#051424`), Royal Pink (`#EB107E`), Champagne Gold (`#FABC4D`), Cyan (`#7BD0FF`).
   - Layout: Responsive desktop-first (1440px/1280px) with 260px collapsible sidebar and mobile drawer navigation.
   - Screens: All 8 screens fully interactive with real data filtering, sorting, radar comparisons, dynamic purse calculations, and mathematical proofs.

