# SupeRR Selector Season 2 – Rajasthan Royals IPL 2027 Auction Analytics
## Complete Methodological Framework: Identifying the Most Reliable Players Under Pressure

---

## 1. Executive Mandate & Analytical Philosophy
In competitive T20 cricket, traditional cumulative metrics (such as total runs, raw batting averages, and overall bowling economies) confound volume with reliability. A boundary hit in a trivial chase (e.g., needing 12 runs off 30 balls with 8 wickets in hand) is treated identically to a boundary hit when needing 14 runs off the final 6 balls.

For the **Rajasthan Royals IPL 2027 Auction**, this project establishes a mathematically defensible, delivery-level evaluation platform that isolates and ranks:
1. **Top 10 Most Reliable Batters Under Pressure (BPRI)**
2. **Top 10 Most Reliable Bowlers Under Pressure (BOWPRI)**

---

## 2. Dataset Feasibility & Relational Integrity
The dataset spans 5 calendar years (2022 to 2026), covering all Indian Premier League (IPL) matches and major T20 Internationals (T20Is):
- `ball_by_ball.csv`: 200,999 delivery-level records across 867 matches.
- `matches.csv`: 883 matches, with target tracking, DLS revisions, and knockout indicators.
- `competitions.csv`: 141 competitions (IPL 2022, 2023, 2024, 2025, 2026; bilateral T20Is; ICC tournaments).
- `competition_team_player_mapping.csv`: 6,413 player registrations, mapping 958 unique players in ball-by-ball records.

### Relational Integrity Principles:
1. All joins are executed strictly via `player_id` and `match_id`. Player names are retained purely for human readability.
2. 100% of bowlers and strikers in `ball_by_ball.csv` resolve to authoritative player records in mapping tables. Zero data fabrication was performed.

---

## 3. Dynamic Pressure Classification Engine
We reject static phase-based definitions (e.g. assuming all balls in overs 16–20 constitute pressure). Pressure is determined dynamically per delivery ($t$) using continuous match leverage:

### Innings 2 (The Run Chase):
- **Required Run Rate (RRR):** Calculated at each legal delivery:
  $$RRR = \frac{\text{Runs Needed}}{\text{Balls Remaining}} \times 6$$
- **Chase Leverage Sigmoid:**
  $$P_{RRR} = \frac{100}{1 + e^{-0.45 \times (RRR - 9.0)}}$$
- **Resource Depletion Multiplier:**
  $$M_{wickets} = 1 + \max(0, (5 - \text{Wickets in Hand}) \times 0.08)$$
- **Endgame Leverage:** Deliveries in the final 4 overs ($\le 24$ balls remaining) where runs needed $\le 2.2 \times \text{balls remaining}$ receive maximum leverage boost ($70 + (24 - \text{balls remaining})$).

### Innings 1 (Target Setting):
- **Collapse Recovery:** In overs 1–10, if $\ge 3$ wickets have fallen, incoming batters face acute rebuilding pressure (Score: 65.0).
- **Death Over Maximization:** In overs 16–20, if wickets in hand $\ge 5$, batters and bowlers face high pressure to maximize / suppress boundaries (Score: $65 + (\text{overid} - 16) \times 3$).

### Knockout Match Elevation:
All playoff matches (Eliminators, Qualifiers, Finals) receive a flat $+8.0$ point pressure elevation.

### Pressure Tiers:
- **LOW PRESSURE (<35):** 23.01% of balls
- **MODERATE PRESSURE (35–59):** 31.99% of balls
- **HIGH PRESSURE (60–79):** 30.39% of balls
- **EXTREME PRESSURE ($\ge 80$):** 14.61% of balls

---

## 4. Index Architecture: BPRI & BOWPRI

### Batting Pressure Reliability Index (BPRI):
$$BPRI_{raw} = 0.30 \times P_{baseline} + 0.20 \times P_{SR} + 0.15 \times P_{control} + 0.15 \times P_{chase} + 0.10 \times P_{death} + 0.10 \times P_{consistency}$$
1. **Pillar 1: Baseline Differential (30%):** Lift under pressure relative to player's normal performance ($SR_{pressure} - SR_{normal}$ and $Avg_{pressure} - Avg_{normal}$).
2. **Pillar 2: Pressure Strike Rate Effectiveness (20%):** Standardized strike rate under High/Extreme pressure.
3. **Pillar 3: Boundary & Dot-Ball Control (15%):** High boundary percentage and suppressed dot-ball percentage under pressure.
4. **Pillar 4: Chase Performance (15%):** Strike rate and average in 2nd innings run chases.
5. **Pillar 5: Death-Over Execution (10%):** Strike rate and boundary percentage in overs 16–20.
6. **Pillar 6: Match Consistency (10%):** Inverted standard deviation of per-match strike rate under pressure.

### Bowling Pressure Reliability Index (BOWPRI):
$$BOWPRI_{raw} = 0.30 \times P_{baseline} + 0.20 \times P_{econ} + 0.15 \times P_{wickets} + 0.15 \times P_{prevention} + 0.10 \times P_{death} + 0.10 \times P_{consistency}$$
1. **Pillar 1: Baseline Differential (30%):** Improvement under pressure ($Econ_{normal} - Econ_{pressure}$ and $SR_{normal} - SR_{pressure}$).
2. **Pillar 2: Economy Control Under Pressure (20%):** Inverted runs conceded per over under High/Extreme pressure.
3. **Pillar 3: Wicket-Taking Effectiveness (15%):** Inverted legal balls per wicket (strike rate) under pressure.
4. **Pillar 4: Boundary & Dot-Ball Prevention (15%):** High dot-ball percentage and suppressed boundary conceded percentage.
5. **Pillar 5: Death-Over Bowling (10%):** Overs 16–20 economy control and wickets per 100 legal balls.
6. **Pillar 6: Match Consistency (10%):** Inverted standard deviation of per-match economy rate under pressure.

---

## 5. Statistical Reliability & Bayesian Shrinkage
To prevent low-sample anomalies from topping the leaderboards, we enforce:
1. **Eligibility Thresholds:**
   - Batters: $\ge 10$ innings and $\ge 75$ pressure balls faced.
   - Bowlers: $\ge 10$ innings and $\ge 60$ pressure legal balls bowled.
2. **Empirical Bayesian Regularization:**
   $$Index_{final} = \left(\frac{N}{N + K}\right) \times Index_{raw} + \left(\frac{K}{N + K}\right) \times \mu_{league}$$
   Where $K_{bat} = 60$, $K_{bowl} = 50$, and $\mu_{league}$ is the population mean.
3. **Confidence Scoring:** Explicitly calculated as $\min(99\%, \max(40\%, (N / N_{target}) \times 100\%))$.

---

## 6. Official Final Rankings

### Top 10 Batters Under Pressure:
1. **Ashutosh Sharma** (Delhi Capitals / Punjab Kings) — BPRI: 78.22 | Death SR: 192.83 | Conf: 99%
2. **Shashank Singh** (Punjab Kings) — BPRI: 77.73 | HP Avg: 41.95 | HP SR: 170.53 | Conf: 99%
3. **Suryakumar Yadav** (India / Mumbai Indians) — BPRI: 76.90 | HP SR: 182.69 | Death SR: 217.17 | Conf: 99%
4. **Tom Banton** (England / Gujarat Titans) — BPRI: 74.05 | HP SR: 186.84 | Conf: 45.6%
5. **Reeza Hendricks** (South Africa) — BPRI: 72.93 | HP Avg: 44.21 | HP SR: 169.59 | Conf: 99%
6. **Naman Dhir** (India / Mumbai Indians) — BPRI: 72.91 | HP SR: 186.26 | Death SR: 200.56 | Conf: 99%
7. **Quinton de Kock** (Mumbai Indians / South Africa) — BPRI: 72.20 | Death SR: 232.00 | Conf: 99%
8. **Phil Salt** (England / KKR / RCB) — BPRI: 72.12 | HP SR: 187.33 | Death SR: 208.42 | Conf: 99%
9. **Rishabh Pant** (Lucknow Super Giants / India) — BPRI: 71.31 | HP SR: 176.53 | Death SR: 200.81 | Conf: 99%
10. **Tim David** (Australia / Mumbai Indians) — BPRI: 71.28 | HP SR: 181.32 | Death SR: 200.87 | Conf: 99%

### Top 10 Bowlers Under Pressure:
1. **Mohammad Nawaz** (Pakistan) — BOWPRI: 83.00 | HP Econ: 6.15 | Death Econ: 5.76 | Conf: 99%
2. **Abrar Ahmed** (Pakistan) — BOWPRI: 77.96 | HP Econ: 6.51 | HP SR: 12.89 | Conf: 99%
3. **Matthew Humphreys** (Ireland) — BOWPRI: 76.68 | HP Econ: 6.80 | Death Econ: 4.97 | Conf: 41.5%
4. **George Linde** (South Africa / LSG) — BOWPRI: 76.10 | HP Econ: 7.38 | Death Econ: 6.32 | Conf: 40.0%
5. **Sunil Narine** (Kolkata Knight Riders) — BOWPRI: 75.71 | HP Econ: 7.27 | Death Econ: 6.06 | Conf: 99%
6. **Imad Wasim** (Pakistan) — BOWPRI: 75.62 | HP Econ: 6.00 | Death Econ: 7.67 | Conf: 52%
7. **Corbin Bosch** (Rajasthan Royals / MI / SA) — BOWPRI: 74.56 | HP Econ: 7.14 | HP SR: 12.60 | Conf: 63%
8. **Hasan Mahmud** (Bangladesh) — BOWPRI: 74.09 | HP Econ: 7.50 | HP SR: 10.91 | Conf: 60%
9. **Sufiyan Muqeem** (Pakistan) — BOWPRI: 73.81 | HP Econ: 4.89 | Death Econ: 7.11 | Conf: 73%
10. **Mitchell Santner** (Chennai Super Kings / NZ) — BOWPRI: 73.53 | HP Econ: 7.21 | HP Wkts: 38 | Conf: 99%

---

## 7. Rajasthan Royals Auction Strategy Summary
1. **Acquire Elite Domestic Finishing:** Ashutosh Sharma and Shashank Singh provide RR with the missing lower-order run-scoring engine required in chases of 12+ RRR at the Sawai Mansingh Stadium.
2. **Powerplay Firepower:** Phil Salt pairs devastatingly with Yashasvi Jaiswal to ensure runaway powerplay run rates.
3. **Championship Spin Defense:** Mitchell Santner and Sunil Narine offer suffocating boundary prevention on Jaipur's large playing dimensions.

