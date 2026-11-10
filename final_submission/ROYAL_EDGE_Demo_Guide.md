# ROYAL EDGE — SYSTEM DEMO & USER GUIDE
## Rajasthan Royals | IPL 2027 Auction Intelligence Platform
**SupeRR Selector Season 2: Round 1 – Pressure Reliability Analytics**

---

## 1. Quick Access & Live Ports

| Service | URL / Port | Technology Stack | Purpose |
| :--- | :--- | :--- | :--- |
| **Primary Web Console** | `http://127.0.0.1:5173` | React 19, TypeScript, Vite, Tailwind v4 | Full 8-Screen Interactive RR Front Office UI |
| **FastAPI Backend** | `http://127.0.0.1:8000` | FastAPI, Uvicorn, Python 3.14 | REST API Engine & Statistical Compute |
| **API Documentation** | `http://127.0.0.1:8000/docs` | Swagger / OpenAPI | Interactive API Testing & Inspection |
| **Streamlit Fallback** | `http://127.0.0.1:8502` | Streamlit, Pandas, NumPy | Contingency Data & Prototyping Engine |

---

## 2. Walkthrough of the Eight Screens

### Screen 1: Executive Overview (`/`)
- **Macro KPIs:** 867 Matches, 200,999 Deliveries, 45,951 High-Pressure Balls (22.86%), ₹42.80 Cr Simulated Purse.
- **Top 3 Previews:** Ashutosh Sharma (78.22), Shashank Singh (77.73), Suryakumar Yadav (76.90) for Batters; Matthew Humphreys (76.68), George Linde (76.10), Sunil Narine (75.71) for Actionable Bowlers.
- **Quick Actions:** Instant routing to Auction War Room, Comparison Studio, and Methodology.

### Screen 2: Pressure Intelligence (`/pressure`)
- **Leverage Engine:** Progression of match pressure across Overs 1 to 20 (Powerplay 0.85–1.05 LEI, Middle 1.15–1.45 LEI, Death 1.82–2.68 LEI).
- **Leverage Classification:** Donut breakdown across Normal (72.7%), High Pressure (18.42%), Extreme Pressure (4.44%), and Cleanup (4.44%).
- **Phase Concentration:** High pressure density: 13.2% in Powerplay, 20.3% in Middle, 40.5% in Death.

### Screen 3: Batting Pressure Reliability (`/batting`)
- **Audited Top 10 Batters Table:** BPRI, HP Strike Rate, HP Average, Death SR (16–20), Chase SR, $\Delta$ SR vs Normal, SSSI %, 95% Bootstrap CI.
- **Filters & Search:** Filter by role (Finisher, Power Hitter, Middle-order) and dynamic search by player or franchise.
- **Profile Routing:** Click "Profile" on any batter to open their dedicated deep-dive dossier.

### Screen 4: Bowling Pressure Reliability (`/bowling`)
- **Audited Top 10 Bowlers Table:** BOWPRI, HP Economy, HP Average, Death Economy, Wickets, SSSI %, 95% Bootstrap CI, Regulatory Status.
- **Actionability Toggle:** Switch seamlessly between "BCCI-Eligible Actionable Targets" and "All Global Benchmark Bowlers".

### Screen 5: Player Comparison Studio (`/compare`)
- **Interactive Selectors:** Compare any two batters or two bowlers head-to-head.
- **6-Axis Leverage Radar:** Visualizes high-pressure SR/Econ, Death lethality/containment, Chase pacing, Collapse recovery, and SSSI saturation.
- **Statistical Significance Engine:** Evaluates bootstrap 95% confidence interval overlap; displays amber warning if intervals overlap.

### Screen 6: Auction War Room (`/auction`)
- **Purse Tracker:** Real-time simulation against Rajasthan Royals' ₹42.80 Cr remaining purse.
- **Interactive Bid Sliders:** Adjust bidding ceilings for priority targets (Ashutosh Sharma, Shashank Singh, Matthew Humphreys, George Linde).
- **Tactical Alerts:** Instant visual warning when simulated bids exceed recommended tactical ceilings or cause purse deficits.
- **Quota Tracking:** Live overseas slot allocation (3 of 8 free) and squad roster capacity (18 filled of 25).

### Screen 7: Player Intelligence Profiles (`/profiles`)
- **Front-Office Dossiers:** Complete player profiles with historical sample metrics, leverage delta, and regulatory standing.
- **Phase-by-Phase Breakdown:** Balls faced/overs bowled and strike rates/economies across Powerplay, Middle, and Death phases.
- **Data-Backed Scouting Notes:** Evidence-based qualitative insights derived strictly from ball-by-ball delivery records.

### Screen 8: Methodology & Reliability (`/methodology`)
- **Mathematical Formulations:** First-innings $P_{1st}$ and second-innings $P_{2nd}$ leverage equations.
- **Empirical Bayesian Shrinkage:** Explains shrinkage prior formulation ($K=60$ balls batting, $K=50$ balls bowling).
- **Metric Definitions:** Formal component weights for BPRI and BOWPRI.
- **Scientific Guardrails:** Clear definition of Sample Size Saturation Index (SSSI %) vs 95% Bootstrap Confidence Intervals.

---

## 3. Verification & Compliance Checklist

- [x] All 8 Stitch screens fully implemented and interactive.
- [x] Zero synthetic, fabricated, or inferred deliveries.
- [x] Complete alignment with official Unstop dropdown rankings.
- [x] Fast, reactive REST API powered by FastAPI on port 8000.
- [x] High-performance React 19 frontend on port 5173.
- [x] Contingency Streamlit dashboard running on port 8502.

