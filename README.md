# SupeRR Selector Season 2 – Rajasthan Royals IPL 2027 Auction Analytics
## Identify the Most Reliable Players Under Pressure

An advanced, evidence-based cricket analytics system and franchise auction scouting platform built for **Rajasthan Royals** through Unstop.

---

## 📌 Project Architecture
```text
RR - Hackathon/
├── data/
│   ├── raw/                        # Original supplied datasets (ball_by_ball, matches, competitions, etc.)
│   └── processed/                  # Processed parquet store with running pressure states
├── notebooks/
│   ├── 01_data_exploration.ipynb   # Comprehensive data audit & quality checks
│   ├── 02_pressure_classification.ipynb # Dynamic ball-by-ball pressure classification
│   ├── 03_batting_analysis.ipynb   # Advanced batting pressure metrics & baseline deltas
│   ├── 04_bowling_analysis.ipynb   # Advanced bowling pressure metrics & baseline deltas
│   └── 05_player_rankings.ipynb    # Bayesian shrinkage, sensitivity testing & rankings
├── src/
│   ├── data_loader.py              # Raw data ingest & schema auditor
│   ├── pressure_engine.py          # Vectorized dynamic match leverage & pressure classifier
│   ├── metrics_engine.py           # BPRI & BOWPRI formulation with Bayesian regularization
│   ├── scouting_strategy.py        # RR tactical fit, roles, and auction target profiles
│   ├── generate_notebooks.py       # Notebook generator
│   ├── generate_presentation.py    # PowerPoint generator (16:9 branded deck)
│   ├── generate_pdf_report.py      # Official ReportLab PDF methodology report generator
│   └── validation.py               # 15-point automated quality assurance test suite
├── outputs/
│   ├── top_10_batters.csv          # Authoritative Top 10 Batters (Unstop Dropdown Reference)
│   ├── top_10_bowlers.csv          # Authoritative Top 10 Bowlers (Unstop Dropdown Reference)
│   ├── all_ranked_batters.csv      # Complete ranked database of all 263 eligible batters
│   ├── all_ranked_bowlers.csv      # Complete ranked database of all 224 eligible bowlers
│   ├── scouting_batters_strategy.csv # Qualitative tactical scouting profiles for batters
│   ├── scouting_bowlers_strategy.csv # Qualitative tactical scouting profiles for bowlers
│   ├── methodology_report.pdf      # Complete 16-section executive PDF methodology report
│   ├── presentation.pptx           # Professional editable 16:9 slide presentation
│   ├── sensitivity_analysis.txt    # Weight perturbation Spearman rank correlation proofs
│   └── validation_report.txt       # 15/15 quality assurance audit certificate
├── dashboard/
│   └── app.py                      # Interactive Streamlit franchise scouting dashboard
├── methodology.md                  # Comprehensive mathematical methodology & index formulas
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation and quick start guide
```

---

## 🚀 Quick Start Guide

### 1. Environment Setup
```bash
pip install -r requirements.txt
```

### 2. Run the Full Analytics Pipeline
```bash
# 1. Run dynamic pressure engine (vectorized processing)
python src/pressure_engine.py

# 2. Calculate BPRI, BOWPRI and generate rankings
python src/metrics_engine.py

# 3. Generate scouting strategies & sensitivity tests
python src/scouting_strategy.py
python src/sensitivity_and_exploration.py

# 4. Generate presentation & official PDF report
python src/generate_presentation.py
python src/generate_pdf_report.py

# 5. Run full quality control verification
python src/validation.py
```

### 3. Launch the Interactive Dashboard
```bash
streamlit run dashboard/app.py
```

---

## 🏆 Official Final Rankings (Unstop Submission Reference)

### Top 10 Batters Under Pressure:
1. **Ashutosh Sharma** (Delhi Capitals / Punjab Kings) — BPRI: **78.22** | Death SR: **192.83** | Conf: **99%**
2. **Shashank Singh** (Punjab Kings) — BPRI: **77.73** | HP Avg: **41.95** | HP SR: **170.53** | Conf: **99%**
3. **Suryakumar Yadav** (India / Mumbai Indians) — BPRI: **76.90** | HP SR: **182.69** | Death SR: **217.17** | Conf: **99%**
4. **Tom Banton** (England / Gujarat Titans) — BPRI: **74.05** | HP SR: **186.84** | Conf: **45.6%**
5. **Reeza Hendricks** (South Africa) — BPRI: **72.93** | HP Avg: **44.21** | HP SR: **169.59** | Conf: **99%**
6. **Naman Dhir** (India / Mumbai Indians) — BPRI: **72.91** | HP SR: **186.26** | Death SR: **200.56** | Conf: **99%**
7. **Quinton de Kock** (Mumbai Indians / South Africa) — BPRI: **72.20** | Death SR: **232.00** | Conf: **99%**
8. **Phil Salt** (England / KKR / RCB) — BPRI: **72.12** | HP SR: **187.33** | Death SR: **208.42** | Conf: **99%**
9. **Rishabh Pant** (Lucknow Super Giants / India) — BPRI: **71.31** | HP SR: **176.53** | Death SR: **200.81** | Conf: **99%**
10. **Tim David** (Australia / Mumbai Indians) — BPRI: **71.28** | HP SR: **181.32** | Death SR: **200.87** | Conf: **99%**

### Top 10 Bowlers Under Pressure:
1. **Mohammad Nawaz** (Pakistan) — BOWPRI: **83.00** | HP Econ: **6.15** | Death Econ: **5.76** | Conf: **99%**
2. **Abrar Ahmed** (Pakistan) — BOWPRI: **77.96** | HP Econ: **6.51** | HP SR: **12.89** | Conf: **99%**
3. **Matthew Humphreys** (Ireland) — BOWPRI: **76.68** | HP Econ: **6.80** | Death Econ: **4.97** | Conf: **41.5%**
4. **George Linde** (South Africa / LSG) — BOWPRI: **76.10** | HP Econ: **7.38** | Death Econ: **6.32** | Conf: **40.0%**
5. **Sunil Narine** (Kolkata Knight Riders) — BOWPRI: **75.71** | HP Econ: **7.27** | Death Econ: **6.06** | Conf: **99%**
6. **Imad Wasim** (Pakistan) — BOWPRI: **75.62** | HP Econ: **6.00** | Death Econ: **7.67** | Conf: **52%**
7. **Corbin Bosch** (Rajasthan Royals / MI / SA) — BOWPRI: **74.56** | HP Econ: **7.14** | HP SR: **12.60** | Conf: **63%**
8. **Hasan Mahmud** (Bangladesh) — BOWPRI: **74.09** | HP Econ: **7.50** | HP SR: **10.91** | Conf: **60%**
9. **Sufiyan Muqeem** (Pakistan) — BOWPRI: **73.81** | HP Econ: **4.89** | Death Econ: **7.11** | Conf: **73%**
10. **Mitchell Santner** (Chennai Super Kings / NZ) — BOWPRI: **73.53** | HP Econ: **7.21** | HP Wkts: **38** | Conf: **99%**

---

## 🎯 Rajasthan Royals IPL 2027 Strategic Insights
1. **Solve Lower-Order Finishing:** Ashutosh Sharma & Shashank Singh offer rare, elite domestic finishing commodities capable of winning chases from 12+ RRR at the Sawai Mansingh Stadium.
2. **Pair Jaiswal with Ultra-Intent:** Phil Salt's explosive powerplay profile creates optimal match matchups in the first 6 overs.
3. **Lock Down Overs 7–15 & Death with Controlled Spin:** Sunil Narine & Mitchell Santner neutralize opposition scoring at under 7.30 RPO under maximum pressure.

