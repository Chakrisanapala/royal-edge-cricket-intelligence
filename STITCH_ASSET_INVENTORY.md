# ROYAL EDGE — Google Stitch AI Asset & Screen Inventory
**Platform:** Rajasthan Royals | IPL 2027 Auction Intelligence  
**Stitch Project:** `ROYAL EDGE – Cricket Intelligence Platform` (`projects/8745219091983978821`)  
**Design System Spec:** `assets/7748abd5fbf04608b6aa5adad0fda753` (`Royal Edge Intelligence`)  
**Live Endpoint:** `https://stitch.googleapis.com/mcp`  
**Date:** November 10, 2026  

---

## 1. Project & Design System Overview

* **Project Identifier:** `projects/8745219091983978821`
* **Design System Reference:** `assets/7748abd5fbf04608b6aa5adad0fda753`
* **Style Philosophy:** Modern Precision Technical — Dark Command Center ergonomics, 1px micro-borders, dense data tables, and high-contrast tactical highlights.
* **Palette Tokens:**
  * Surface Canvas (Base): `#051424` (Midnight Navy)
  * System Base / Darkest: `#010F1F`
  * Structural Paneling: `#0D1C2D`
  * Data Module Container: `#122131`
  * Elevated Card / Focus: `#1C2B3C`
  * Primary Accent: `#EB107E` (Royal Pink)
  * Secondary Accent: `#FABC4D` (Champagne Gold)
  * Telemetry Accent: `#7BD0FF` (Cyan)
* **Typography:** `Inter` across all scales (400, 500, 600, 700).

---

## 2. Complete Inventory of All 8 Screens

All 8 screens were retrieved and verified. The full HTML codebases and rendered PNG screenshots are preserved locally in `d:\Desktop\RR - Hackathon\stitch_screens/`:

| # | Screen Name | Screen / File Resource Identifier | Local HTML File | Local Rendered Screenshot | Size (HTML / PNG) | Status |
| :-: | :--- | :--- | :--- | :--- | :---: | :---: |
| **1** | **Executive Overview** | `screens/07f3eec5e0e5445ba1e3ec472e6e9d4b` | `screen_01_executive_overview.html` | `screen_01_executive_overview.png` | 57.8 KB / 1.10 MB | **Updated & Verified** |
| **2** | **Pressure Intelligence** | `screens/2e8068c7073d43bc941b1ff63a753b55` | `screen_02_pressure_intelligence.html` | `screen_02_pressure_intelligence.png` | 62.1 KB / 1.67 MB | **Updated & Verified** |
| **3** | **Batting Analytics** | `screens/da85b6e87e574f62ad1b2308e842858e` | `screen_03_batting_analytics.html` | `screen_03_batting_analytics.png` | 58.8 KB / 1.26 MB | **Updated & Verified** |
| **4** | **Bowling Analytics** | `screens/b995e8d8155348b7920fe307de43d90b` | `screen_04_bowling_analytics.html` | `screen_04_bowling_analytics.png` | 68.5 KB / 1.67 MB | **Updated & Verified** |
| **5** | **Player Comparison** | `files/e303204b815a42f0811f0bd479966a33` | `screen_05_player_comparison.html` | `screen_05_player_comparison.png` | 56.4 KB / 1.66 MB | **Generated & Verified** |
| **6** | **Auction War Room** | `files/17028917926877300978_auction` | `screen_06_auction_war_room.html` | `screen_06_auction_war_room.png` | 61.2 KB / 1.35 MB | **Generated & Verified** |
| **7** | **Player Intelligence Profile** | `files/player_profile_8101` | `screen_07_player_intelligence_profile.html` | `screen_07_player_intelligence_profile.png` | 50.2 KB / 1.42 MB | **Generated & Verified** |
| **8** | **Methodology & Reliability** | `files/methodology_reliability_framework` | `screen_08_methodology_reliability.html` | `screen_08_methodology_reliability.png` | 53.4 KB / 1.57 MB | **Generated & Verified** |

---

## 3. Screen Architectural Summaries

### Screen 1: Executive Overview (`screen_01_executive_overview.html`)
* **Layout:** Desktop-first 1440px with 260px fixed collapsible sidebar.
* **Top Metric Grid:** 4 responsive KPI cards:
  * 867 Matches Parsed (2022–2026)
  * 200,999 Total Deliveries Evaluated
  * 45,951 High-Pressure Deliveries (22.86%)
  * ₹42.80 Cr Simulated Active Purse Capacity
* **Marquee Player Focus:** Side-by-side featured spotlight cards for **Ashutosh Sharma** (#1 BPRI: 78.22) and **Matthew Humphreys** (#1 Actionable Bowler BOWPRI: 76.68).

### Screen 2: Pressure Intelligence (`screen_02_pressure_intelligence.html`)
* **Layout:** Mathematical telemetry console with interactive leverage curves.
* **Core Components:**
  * Dynamic RRR Sigmoid Formulation visualizer.
  * 4-Tier Pressure Taxonomy breakdown (Low, Moderate, High, Extreme).
  * 1st vs 2nd Innings leverage bifurcation curves.
  * Over-by-over win-probability swing demonstration.

### Screen 3: Batting Analytics (`screen_03_batting_analytics.html`)
* **Layout:** High-density data grid and scatter plot.
* **Core Components:**
  * Verified Top 10 Batters table matching `RR_Top_10_Batters.csv` (Ashutosh Sharma, Shashank Singh, Suryakumar Yadav, Tom Banton, Reeza Hendricks, Naman Dhir, Quinton de Kock, Phil Salt, Rishabh Pant, Tim David).
  * True 95% Bootstrap Confidence Intervals and SSSI % column.
  * Role filters (Finisher, Aggressor, Opener) and search bar.

### Screen 4: Bowling Analytics (`screen_04_bowling_analytics.html`)
* **Layout:** Dual-tab command matrix.
* **Core Components:**
  * Tab 1: Official Statistical Benchmarks (Nawaz, Abrar, Humphreys, Linde, Narine, Wasim, Bosch, Mahmud, Muqeem, Santner).
  * Tab 2: Actionable IPL 2027 Auction Shortlist (BCCI-Eligible targets).
  * Economy under pressure vs. dot ball frequency visualization.

### Screen 5: Player Comparison (`screen_05_player_comparison.html`)
* **Layout:** Dual-player head-to-head comparison center.
* **Core Components:**
  * Side-by-side dropdown player selectors.
  * 6-Axis Pillar Radar Chart (HP SR, HP Avg, Death SR, Chase Acceleration, Collapse Recovery, SSSI %).
  * Direct statistical delta table with statistical significance warning note when intervals overlap.

### Screen 6: Auction War Room (`screen_06_auction_war_room.html`)
* **Layout:** Franchise auction command board with real-time budget simulator.
* **Core Components:**
  * User-editable purse controls (Total Purse, Spent, Remaining).
  * Overseas slot counter (8 maximum).
  * Target roster board with simulated bidding ceilings (clearly marked as simulations).
  * Dynamic squad balance validator.

### Screen 7: Player Intelligence Profile (`screen_07_player_intelligence_profile.html`)
* **Layout:** Comprehensive scouting dossier.
* **Core Components:**
  * Deep-dive profile for shortlisted targets (Ashutosh Sharma, Matthew Humphreys).
  * Innings phase breakdown (Powerplay, Middle, Death overs 16–20).
  * Collapse entry delta metrics (+135.29 SR lift).
  * Evidence-based strengths and risk mitigations (unsupported biomechanics claims omitted).

### Screen 8: Methodology & Statistical Reliability (`screen_08_methodology_reliability.html`)
* **Layout:** Technical documentation and mathematical proof repository.
* **Core Components:**
  * LaTeX mathematical formulations of BPRI and BOWPRI across all 6 pillars.
  * Empirical Bayesian shrinkage priors ($K_{\text{bat}}=60$, $K_{\text{bowl}}=50$).
  * 1,000-iteration bootstrap distributions and confidence limits.
  * SSSI definition and sensitivity analysis correlation matrices ($r > 0.97$).

