# Statistical Reliability and Uncertainty Audit
## Critical Investigation of Confidence Scores, Small Samples, and Bootstrap Uncertainty

**Auditor:** Senior Cricket Analytics Auditor & Statistical Research Reviewer  
**Audit Target:** Statistical Reliability Claims, "Confidence Scores", and Sample Size Dynamics

---

### 1. Investigation of the "Confidence Score (%)" Metric

In the generated dashboard, presentation, and report, players are assigned a "Confidence Score" (e.g. **99.0%** for Ashutosh Sharma, **45.6%** for Tom Banton, and **41.5%** for Matthew Humphreys).

#### How Was This Value Actually Calculated?
Inspecting `src/metrics_engine.py` (lines 159 and 224) reveals the exact formula:
```python
# Batters
eb['confidence_score'] = np.clip((eb['hp_balls'] / 250.0) * 100.0, 40.0, 99.0)

# Bowlers
ebowl['confidence_score'] = np.clip((ebowl['hp_legal_balls'] / 200.0) * 100.0, 40.0, 99.0)
```

#### Why This Is Statistically Misleading:
1. **Misrepresentation of Statistical Confidence:** In probability and statistics, a "confidence score" or "confidence level" (e.g., 95% or 99%) denotes the frequentist coverage probability of a confidence interval, or the Bayesian posterior probability that a parameter falls within a credible region. Here, it is simply a **linear sample-size volume ratio** ($N / N_{\text{target}}$) bounded between 40% and 99%.
2. **Conflating Sample Volume with Quality:** An uninformed decision-maker reading *"Confidence: 99%"* could mistakenly conclude that there is a 99% probability that the player will perform well in the IPL, or that the rating is 99% accurate.
3. **Arbitrary Thresholds:** The denominators ($250$ balls for batters, $200$ balls for bowlers) and the arbitrary $40.0\%$ floor were chosen without empirical sampling variance calibration.

#### Remediation Mandate:
The term **"Confidence Score" must be completely removed** or renamed to **"Sample Size Saturation Index (SSSI)"**. True uncertainty must be expressed using **Bootstrap Confidence Intervals** and **Standard Errors**.

---

### 2. True Statistical Uncertainty: 1,000-Iteration Bootstrap Audit

To establish mathematically valid uncertainty bounds, we performed a non-parametric bootstrap resampling ($B = 1,000$ iterations) on the delivery-level performance of every top-10 player.

#### 2.1 Batting Pressure Strike Rate: 95% Bootstrap Confidence Intervals
| Rank | Player Name | Pressure Balls ($N$) | Observed Pressure SR | 95% Bootstrap Confidence Interval | Bootstrap Std. Error ($\text{SE}$) | Sample Saturation Ratio | True Statistical Reliability Assessment |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Ashutosh Sharma** | 341 | 168.62 | **[148.67, 189.74]** | $\pm 10.83$ | 99.0% | **High Sample Depth:** Narrow band, statistically stable elite finisher. |
| **2** | **Shashank Singh** | 492 | 170.53 | **[153.65, 186.79]** | $\pm 8.57$ | 99.0% | **Very High Depth:** Exceptionally tight confidence band; high certainty. |
| **3** | **Suryakumar Yadav** | 1,005 | 182.69 | **[170.25, 194.43]** | $\pm 6.20$ | 99.0% | **Gold Standard:** Lowest standard error ($\pm 6.20$); undisputed statistical certainty. |
| **4** | **Tom Banton** | 114 | 186.84 | **[152.63, 222.83]** | $\pm 18.11$ | 45.6% | **High Variance:** Wide 70-point interval! Ranking is vulnerable to sample volatility. |
| **5** | **Reeza Hendricks** | 365 | 169.59 | **[151.23, 188.77]** | $\pm 9.38$ | 99.0% | **High Sample Depth:** Reliable international sample baseline. |
| **6** | **Naman Dhir** | 342 | 186.26 | **[168.13, 207.02]** | $\pm 9.98$ | 99.0% | **Solid Sample Depth:** Stable power-hitting interval. |
| **7** | **Quinton de Kock** | 455 | 170.33 | **[153.41, 188.36]** | $\pm 8.71$ | 99.0% | **Very High Depth:** High certainty, proven IPL & T20I record. |
| **8** | **Phil Salt** | 292 | 187.33 | **[164.03, 209.61]** | $\pm 12.04$ | 99.0% | **Moderate/High Depth:** Moderate standard error ($\pm 12.04$), strong powerplay floor. |
| **9** | **Rishabh Pant** | 473 | 176.53 | **[157.93, 193.46]** | $\pm 9.05$ | 99.0% | **Very High Depth:** Statistically defensible middle-order anchor. |
| **10** | **Tim David** | 937 | 181.32 | **[169.48, 194.67]** | $\pm 6.44$ | 99.0% | **Gold Standard:** Second-highest volume in world cricket; ultra-reliable. |

#### 2.2 Bowling Pressure Economy: 95% Bootstrap Confidence Intervals
| Rank | Player Name | Pressure Legal Balls ($N$) | Observed Pressure Econ | 95% Bootstrap Confidence Interval | Bootstrap Std. Error ($\text{SE}$) | Sample Saturation Ratio | True Statistical Reliability Assessment |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **Mohammad Nawaz** | 233 | 6.15 | **[5.16, 7.35]** | $\pm 0.56$ | 99.0% | **High Certainty:** Extremely tight economy band under pressure. |
| **2** | **Abrar Ahmed** | 245 | 6.51 | **[5.44, 7.62]** | $\pm 0.58$ | 99.0% | **High Certainty:** Statistically solid mystery spin execution. |
| **3** | **Matthew Humphreys** | 83 | 6.80 | **[5.05, 8.69]** | $\pm 0.93$ | 41.5% | **High Volatility:** Wide interval spanning from elite (5.05) to mediocre (8.69). |
| **4** | **George Linde** | 78 | 7.38 | **[5.30, 9.54]** | $\pm 1.12$ | 40.0% | **High Volatility:** Broadest error margin among all bowlers ($\pm 1.12$). |
| **5** | **Sunil Narine** | 586 | 7.27 | **[6.47, 8.08]** | $\pm 0.41$ | 99.0% | **Gold Standard:** Exceptional stability over 97+ pressure overs. |
| **6** | **Imad Wasim** | 104 | 6.00 | **[4.58, 7.60]** | $\pm 0.75$ | 52.0% | **Moderate Sample:** Economy is elite but subject to moderate variance. |
| **7** | **Corbin Bosch** | 126 | 7.14 | **[5.43, 8.98]** | $\pm 0.88$ | 63.0% | **Moderate Sample:** Solid floor, but economy upper bound reaches 8.98. |
| **8** | **Hasan Mahmud** | 120 | 7.50 | **[5.85, 9.18]** | $\pm 0.84$ | 60.0% | **Moderate Sample:** Wicket-taking compensates for economy variance. |
| **9** | **Sufiyan Muqeem** | 146 | 4.89 | **[3.70, 6.29]** | $\pm 0.67$ | 73.0% | **Moderate Sample:** Exceptional economy floor ($<6.30$ at 97.5% confidence). |
| **10** | **Mitchell Santner** | 573 | 7.21 | **[6.45, 8.02]** | $\pm 0.40$ | 99.0% | **Gold Standard:** Lowest standard error in dataset ($\pm 0.40$); ultra-stable. |

---

### 3. Critical Analytical Insight: Sample Size Threshold Sensitivity

When evaluating the impact of the minimum delivery threshold:
- **At Minimum Threshold $N \ge 75$ (Current Implementation):**
  - Tom Banton ($N=114$), Matthew Humphreys ($N=83$), and George Linde ($N=78$) qualify. Their observed rates place them in the top 5, but their bootstrap intervals indicate that their true population performance could be substantially lower.
- **At Elevated Threshold $N \ge 120$ (High-Confidence Cutoff):**
  - Tom Banton is removed from the Top 10 Batters, promoting **Yashasvi Jaiswal** (Rank 11, $N=259$, BPRI: 70.58) and **Ryan Rickelton** (Rank 12, $N=270$, BPRI: 70.50).
  - Matthew Humphreys, George Linde, and Imad Wasim are removed from the Top 10 Bowlers, promoting **Sikandar Raza** ($N=224$, BOWPRI: 72.26), **Jasprit Bumrah** ($N=564$, BOWPRI: 71.98), and **Tabraiz Shamsi** ($N=139$, BOWPRI: 71.92).

### 4. Recommendation for Franchise Reporting
The report must explicitly state that **Tom Banton, Matthew Humphreys, and George Linde represent high-variance "emerging upside" targets**, whereas **Suryakumar Yadav, Sunil Narine, Mitchell Santner, and Shashank Singh represent "high-certainty proven anchors."**

