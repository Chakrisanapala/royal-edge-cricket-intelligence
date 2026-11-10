# SupeRR Selector Season 2: Rajasthan Royals IPL 2027 Auction Analytics
## Complete Scientific Methodology & Mathematical Architecture (Audited Final Version)

---

## 1. Executive Summary & Research Mandate
The objective of this challenge is to identify and rank the **Top 10 Most Reliable Batters** and **Top 10 Most Reliable Bowlers Under Pressure** to shape Rajasthan Royals' IPL 2027 Auction Strategy.

Analyzing 200,999 delivery-level records across 867 matches from January 22, 2022 to November 1, 2026 (spanning IPL seasons 2022–2026 and international T20s), we formulate two transparent, regularized indices:
- **Batting Pressure Reliability Index (BPRI)**
- **Bowling Pressure Reliability Index (BOWPRI)**

### Independent Scientific Audit Compliance
In accordance with professional sports analytics standards:
1. **Decoupling Statistical Excellence from Auction Eligibility:** The official statistical rankings preserve all players qualifying under historical delivery logs (including Pakistani international performers). An adjacent **Actionable IPL 2027 Auction Board** filters targets in compliance with BCCI player auction regulations.
2. **True Statistical Uncertainty:** Misleading heuristic "confidence scores" are completely eliminated and replaced by **1,000-Iteration Non-Parametric Bootstrap 95% Confidence Intervals** and the **Sample Size Saturation Index (SSSI)**.
3. **Collinearity Disclosure:** Multi-collinearity between strike-rate sub-components is disclosed; the model intentionally places an aggressive valuation on boundary striking and run-rate escalation under pressure.

---

## 2. Dynamic Match Leverage Engine (What Counts as Pressure)

Static phase definitions (e.g. assuming all death-over balls represent pressure) are rejected. A chase of 15 runs off 35 balls with 8 wickets in hand in over 16 carries virtually zero pressure (RRR: 2.57). 

Our engine tracks leverage dynamically delivery-by-delivery:

### Innings 2 (The Run Chase)
- **Dynamic Required Run Rate (RRR):**
  $$RRR = \frac{\text{Runs Needed}}{\text{Balls Remaining}} \times 6$$
- **Leverage Sigmoid Function:**
  $$P_{RRR} = \frac{100}{1 + e^{-0.45 \times (RRR - 9.0)}}$$
- **Resource Depletion Multiplier:**
  $$M_{wickets} = 1 + \max(0, (5 - \text{Wickets in Hand}) \times 0.08)$$
- **Combined Innings 2 Pressure:**
  $$P_{chase} = \min(100, P_{RRR} \times M_{wickets} + 8.0 \times \text{is\_knockout})$$
- **Endgame Finish Boost:** When balls remaining $\le 24$ and runs needed $\le 2.2 \times \text{balls remaining}$, pressure peaks at $70 + (24 - \text{balls remaining})$.

### Innings 1 (Target Setting)
- **Collapse Recovery:** In overs 1–10, if $\ge 3$ wickets fall, pressure is elevated to 65.0.
- **Death-Over Boundary Maximization:** In overs 16–20 with $\ge 5$ wickets in hand, pressure scales from 65.0 to 77.0.

### Validated Classification Tiers:
- **LOW PRESSURE (<35):** 23.01% of deliveries (comfortable chases, early unhurried powerplay).
- **MODERATE PRESSURE (35–59):** 31.99% of deliveries (par-rate middle overs).
- **HIGH PRESSURE (60–79):** 30.39% of deliveries (chases RRR 10–12, death overs, collapses).
- **EXTREME PRESSURE ($\ge 80$):** 14.61% of deliveries (endgame finishes, RRR > 13.0, super overs).

---

## 3. Index Mathematical Architecture

### Batting Pressure Reliability Index (BPRI):
$$BPRI_{raw} = 0.30 \times P_{baseline} + 0.20 \times P_{SR} + 0.15 \times P_{control} + 0.15 \times P_{chase} + 0.10 \times P_{death} + 0.10 \times P_{consistency}$$
- **Pillar 1: Baseline Differential (30%):** Lift under pressure relative to player normal ($SR_{pressure} - SR_{normal}$ and $Avg_{pressure} - Avg_{normal}$).
- **Pillar 2: Pressure Strike Rate (20%):** Standardized high-pressure strike rate.
- **Pillar 3: Control & Boundary Impact (15%):** High boundary % and suppressed dot % under pressure.
- **Pillar 4: Chase Performance (15%):** 2nd innings strike rate and average.
- **Pillar 5: Death-Over Execution (10%):** Overs 16–20 strike rate and boundary rate.
- **Pillar 6: Match Consistency (10%):** Inverted standard deviation of match strike rates.

### Bowling Pressure Reliability Index (BOWPRI):
$$BOWPRI_{raw} = 0.30 \times P_{baseline} + 0.20 \times P_{econ} + 0.15 \times P_{wickets} + 0.15 \times P_{prevention} + 0.10 \times P_{death} + 0.10 \times P_{consistency}$$
- **Pillar 1: Baseline Differential (30%):** Improvement under pressure ($Econ_{normal} - Econ_{pressure}$).
- **Pillar 2: Economy Control Under Pressure (20%):** Inverted pressure economy rate.
- **Pillar 3: Wicket-Taking Effectiveness (15%):** Inverted legal balls per wicket under pressure.
- **Pillar 4: Prevention & Choke Impact (15%):** High dot % and suppressed boundary conceded %.
- **Pillar 5: Death-Over Execution (10%):** Overs 16–20 economy and wickets per 100 balls.
- **Pillar 6: Match Consistency (10%):** Inverted standard deviation of match economies.

---

## 4. Empirical Bayesian Shrinkage & Uncertainty Calibration
To regularize small-sample variance:
$$Index_{final} = \left(\frac{N}{N + K}\right) \times Index_{raw} + \left(\frac{K}{N + K}\right) \times \mu_{prior}$$
- $K_{bat} = 60.0$, $K_{bowl} = 50.0$.
- Qualification Thresholds: $\ge 10$ innings and $\ge 75$ pressure balls faced (batters); $\ge 10$ innings and $\ge 60$ pressure legal balls bowled (bowlers).
- **Uncertainty Quantification:** True measurement precision is quantified via 1,000-iteration non-parametric bootstrap resampling, establishing exact 95% Confidence Intervals for every player.

---

## 5. Official Statistical Rankings (Unstop Submission Order)

### Top 10 Batters (BPRI):
1. **Ashutosh Sharma** (ID: 8101) — BPRI: **78.22** | HP SR: **168.62** | 95% CI: **[148.7, 189.7]** | Death SR: **192.83**
2. **Shashank Singh** (ID: 2756) — BPRI: **77.73** | HP SR: **170.53** | 95% CI: **[153.6, 186.8]** | HP Avg: **41.95**
3. **Suryakumar Yadav** (ID: 1699) — BPRI: **76.90** | HP SR: **182.69** | 95% CI: **[170.3, 194.4]** | Death SR: **217.17**
4. **Tom Banton** (ID: 6273) — BPRI: **74.05** | HP SR: **186.84** | 95% CI: **[152.6, 222.8]** | Death SR: **188.57**
5. **Reeza Hendricks** (ID: 768) — BPRI: **72.93** | HP SR: **169.59** | 95% CI: **[151.2, 188.8]** | HP Avg: **44.21**
6. **Naman Dhir** (ID: 37052) — BPRI: **72.91** | HP SR: **186.26** | 95% CI: **[168.1, 207.0]** | Death SR: **200.56**
7. **Quinton de Kock** (ID: 2101) — BPRI: **72.20** | HP SR: **170.33** | 95% CI: **[153.4, 188.4]** | Death SR: **232.00**
8. **Phil Salt** (ID: 5553) — BPRI: **72.12** | HP SR: **187.33** | 95% CI: **[164.0, 209.6]** | Death SR: **208.42**
9. **Rishabh Pant** (ID: 4703) — BPRI: **71.31** | HP SR: **176.53** | 95% CI: **[157.9, 193.5]** | Death SR: **200.81**
10. **Tim David** (ID: 6396) — BPRI: **71.28** | HP SR: **181.32** | 95% CI: **[169.5, 194.7]** | Death SR: **200.87**

### Top 10 Bowlers (BOWPRI):
1. **Mohammad Nawaz** (ID: 2490) — BOWPRI: **83.00** | HP Econ: **6.15** | 95% CI: **[5.16, 7.35]** | Death Econ: **5.76**
2. **Abrar Ahmed** (ID: 5979) — BOWPRI: **77.96** | HP Econ: **6.51** | 95% CI: **[5.44, 7.62]** | Death Econ: **6.88**
3. **Matthew Humphreys** (ID: 22471) — BOWPRI: **76.68** | HP Econ: **6.80** | 95% CI: **[5.05, 8.69]** | Death Econ: **4.97**
4. **George Linde** (ID: 4229) — BOWPRI: **76.10** | HP Econ: **7.38** | 95% CI: **[5.30, 9.54]** | Death Econ: **6.32**
5. **Sunil Narine** (ID: 781) — BOWPRI: **75.71** | HP Econ: **7.27** | 95% CI: **[6.47, 8.08]** | Death Econ: **6.06**
6. **Imad Wasim** (ID: 3578) — BOWPRI: **75.62** | HP Econ: **6.00** | 95% CI: **[4.58, 7.60]** | Death Econ: **7.67**
7. **Corbin Bosch** (ID: 3629) — BOWPRI: **74.56** | HP Econ: **7.14** | 95% CI: **[5.43, 8.98]** | Death Econ: **8.77**
8. **Hasan Mahmud** (ID: 6643) — BOWPRI: **74.09** | HP Econ: **7.50** | 95% CI: **[5.85, 9.18]** | Death Econ: **8.39**
9. **Sufiyan Muqeem** (ID: 34485) — BOWPRI: **73.81** | HP Econ: **4.89** | 95% CI: **[3.70, 6.29]** | Death Econ: **7.11**
10. **Mitchell Santner** (ID: 4101) — BOWPRI: **73.53** | HP Econ: **7.21** | 95% CI: **[6.45, 8.02]** | Death Econ: **9.34**

---

## 6. Actionable IPL 2027 Auction Bowler Board
Filtered in compliance with BCCI player regulations, promoting the next highest-rated auction-eligible bowlers:
1. **Matthew Humphreys** (Ireland) — BOWPRI: 76.68
2. **George Linde** (South Africa) — BOWPRI: 76.10
3. **Sunil Narine** (West Indies / KKR) — BOWPRI: 75.71
4. **Corbin Bosch** (South Africa) — BOWPRI: 74.56
5. **Hasan Mahmud** (Bangladesh) — BOWPRI: 74.09
6. **Mitchell Santner** (New Zealand / CSK) — BOWPRI: 73.53
7. **Sikandar Raza** (Zimbabwe / PBKS) — BOWPRI: 72.26
8. **Jasprit Bumrah** (India / MI) — BOWPRI: 71.98
9. **Tabraiz Shamsi** (South Africa) — BOWPRI: 71.92
10. **Sakib Hussain** (India / SRH) — BOWPRI: 71.89

