# Claim Verification and Evidence Audit
## Systematic Audit of Qualitative Statements, Tactical Claims, and Analytical Inferences

**Auditor:** Senior Cricket Analytics Auditor & Statistical Research Reviewer  
**Audit Target:** `src/scouting_strategy.py`, `outputs/presentation.pptx`, `outputs/methodology_report.pdf`

---

### 1. Framework for Claim Verification

A competitive analytics submission must strictly distinguish between:
1. **Verified Empirical Evidence (Tier 1):** Directly derived from the supplied 200,999 delivery records with mathematical reproducibility.
2. **Supported Analytical Inference (Tier 2):** Modeled outputs (e.g. dynamic leverage curves, empirical Bayesian shrinkage, modal batting order roles).
3. **External Domain Knowledge (Tier 3):** Verified public cricket facts (e.g. BCCI auction rules, player handedness, historical IPL franchise registrations).
4. **Unsupported Qualitative Speculation (Tier 4):** Biomechanical, psychological, or speculative claims that have zero supporting records in the dataset. **Must be flagged and removed.**

---

### 2. Sentence-by-Sentence Audit of Tactical Scouting Claims

| Player / Topic | Exact Statement in Strategy Documents | Evidence Tier | Audit Verdict & Source Verification | Required Correction / Editorial Action |
| :--- | :--- | :---: | :--- | :--- |
| **Ashutosh Sharma** | *"Astonishing 192.83 strike rate in death overs; holds a +38.6 SR improvement in high-pressure chases."* | **Tier 1** | **VERIFIED.** Exactly matches ball-by-ball record: 192.83 death SR ($N=223$ balls), +38.62 delta SR vs normal baseline. | **Retain as core quantitative evidence.** |
| **Ashutosh Sharma** | *"Sweeps pace and targets square boundaries under extreme pressure."* | **Tier 2 / 4** | **PARTIALLY SUPPORTED.** `stroke` records 14 sweeps, but dataset lacks $(x, y)$ boundary coordinates. | **Label as analytical inference from stroke logs.** |
| **Ashutosh Sharma** | *"Vulnerable to hard-length deliveries angling into the body early in his innings."* | **Tier 4** | **UNSUPPORTED SPECULATION.** Ball pitch coordinates are not logged in `ball_by_ball.csv`. | **FLAG & REMOVE from formal methodology report.** |
| **Shashank Singh** | *"Exceptional 41.95 average under pressure alongside a 170.53 strike rate."* | **Tier 1** | **VERIFIED.** Exactly matches: 41.95 pressure average (492 pressure balls, 839 runs, 20 dismissals). | **Retain as core quantitative evidence.** |
| **Shashank Singh** | *"Can take 4-5 balls to assess pitch bounce before accelerating."* | **Tier 2** | **ANALYTICAL INFERENCE.** Batter's first 5 balls faced average SR of 118.4, accelerating to 184.2 after ball 6. | **Rephrase strictly as entry-ball strike-rate progression.** |
| **Suryakumar Yadav** | *"The undisputed gold standard: 1,005 pressure balls faced with 182.69 pressure SR and 217.17 death SR."* | **Tier 1** | **VERIFIED.** Over 1,005 deliveries, he scored 1,836 runs under pressure; death SR is 217.17 ($N=459$). | **Retain as primary benchmark.** |
| **Suryakumar Yadav** | *"High retention probability by Mumbai Indians makes availability conditional on mega-auction dynamics."* | **Tier 3** | **EXTERNAL CONTEXT.** Public franchise contract knowledge; not derived from CSV files. | **Label explicitly as 'Franchise Governance Context'.** |
| **Phil Salt** | *"Maintains an unrelenting 187.33 pressure strike rate; dismantles opening bowlers... facing 140+ km/h pace."* | **Tier 1** | **VERIFIED.** 187.33 pressure SR ($N=292$). Delivery logs confirm 68 balls faced at $\ge 140.0\text{ km/h}$ with an SR of 192.6. | **Retain; radar speeds directly verified in data.** |
| **Phil Salt** | *"Turning Jaipur into a fortress through powerplay domination."* | **Tier 4** | **UNSUPPORTED RHETORIC.** Speculative promotional rhetoric. | **REMOVE rhetoric; replace with objective powerplay run-rate uplift.** |
| **Mohammad Nawaz** | *"Staggering 6.15 economy under pressure with 27 pressure wickets; 5.76 economy in death overs."* | **Tier 1** | **VERIFIED.** 233 legal pressure balls, 239 runs conceded (6.15 RPO); death economy is 5.76 ($N=25$ overs). | **Retain as core quantitative evidence.** |
| **Mohammad Nawaz** | *"Darting trajectory with subtle seam variation that denies batters elevation."* | **Tier 4** | **UNSUPPORTED SPECULATION.** Ball seam orientation and vertical launch degrees are not tracked in CSV. | **FLAG & REMOVE speculative biomechanical commentary.** |
| **Abrar Ahmed** | *"6.51 economy and an unbelievable 12.89 bowling strike rate under pressure."* | **Tier 1** | **VERIFIED.** 245 legal balls, 266 runs, 19 wickets (12.89 balls per wicket). | **Retain as core quantitative evidence.** |
| **Sunil Narine** | *"97.66 pressure overs bowled with a 7.27 economy and 6.06 death economy; 34 pressure wickets."* | **Tier 1** | **VERIFIED.** 586 legal pressure balls (97.7 overs), 710 runs, 34 wickets; 6.06 death economy ($N=36$ overs). | **Retain as premier high-volume benchmark.** |
| **Corbin Bosch** | *"Familiar with Rajasthan Royals culture."* | **Tier 3** | **EXTERNAL CONTEXT.** Bosch was signed by RR in 2022 as an injury replacement; factually true but outside CSV. | **Label as historical franchise roster note.** |
| **Pakistani Players** | *"Ineligible for IPL auction under Indian government / BCCI directives."* | **Tier 3** | **VERIFIED EXTERNAL GOVERNANCE.** Established BCCI policy since 2008. Essential for realistic auction planning. | **Retain as mandatory regulatory qualification.** |

---

### 3. Guidelines for the Final Submission Report

1. **Purge Subjective Adjectives:** Replace descriptive rhetoric (e.g. *"miracle victories"*, *"fortress"*, *"fearlessness"*) with exact statistical differentials (e.g. *"+38.6 SR improvement over baseline"*, *"6.06 economy rate in overs 16–20"*).
2. **Disclose Shot Tracking Limitations:** Explicitly state that while `stroke` categorizes shot types (Cover Drive, Pull shot, Sweep), the dataset does not record field placement coordinates or boundary distance in meters.
3. **Disclose Ball Speed Verification:** Note that `bowl_speed` is fully tracked in `ball_by_ball.csv`, allowing empirical verification of player performance against high pace ($\ge 140\text{ km/h}$).

