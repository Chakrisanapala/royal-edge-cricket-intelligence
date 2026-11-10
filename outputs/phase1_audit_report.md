# SupeRR Selector Season 2 – Rajasthan Royals IPL 2027 Auction Analytics
## Phase 1: Dataset Quality Audit & Feasibility Assessment

### 1. Executive Summary & Verification of Deliverables
- **Delivery-level dataset (`ball_by_ball.csv`) presence:** **CONFIRMED & VALIDATED**.
- **Total Deliveries Analyzed:** 200,999
- **Total Matches in Master Dataset:** 883 (Ball-by-ball coverage: 867 matches)
- **Total Competitions:** 141 (IPL Seasons: 2022 to 2026; T20I Series/Tournaments: 2022 to 2026)
- **Total Unique Players:** 958 active in match deliveries (1,217 registered in official mapping)
- **Primary Linking Keys:** `match_id`, `player_id`, `comp_id`, `team_id`. (Zero unmatched players between `ball_by_ball.csv` and `competition_team_player_mapping.csv`).

---

### 2. Dataset Overview & Dimensions
| Dataset | Rows | Columns | Memory (MB) | Duplicate Rows | Primary Keys |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `competitions.csv` | 141 | 4 | 0.01 | 0 | `comp_id` |
| `teams.csv` | 353 | 3 | 0.01 | 0 | `comp_id`, `team_id` |
| `matches.csv` | 883 | 23 | 0.23 | 0 | `match_id` |
| `playing_eleven.csv` | 28,381 | 9 | 3.21 | 0 | `match_id`, `team_id`, `player_id` |
| `competition_team_player_mapping.csv` | 6,413 | 6 | 0.64 | 0 | `comp_id`, `team_id`, `player_id` |
| `ball_by_ball.csv` | 200,999 | 33 | 69.49 | 0 | `match_id`, `innings`, `overid`, `over_ball_num` |

---

### 3. Date & Format Coverage
- **Temporal Range:** 2022-01-22 to 2026-11-01 (Covers 5 full calendar years of modern high-intensity T20 cricket).
- **Match Formats:**
  - T20 (Domestic / Franchise Leagues - primarily IPL 2022, 2023, 2024, 2025, 2026): 401 matches (371 IPL matches).
  - T20I (Bilateral T20 Internationals, ICC T20 World Cups, Asia Cups): 482 matches.
- **Seasons Covered:** 2022, 2022/23, 2023, 2023/24, 2024, 2024/25, 2025, 2026

---

### 4. Relational Integrity & Key Consistency
1. **Match Linking (`match_id`):**
   - 867 of 883 matches have full ball-by-ball delivery logs. 16 matches in `matches.csv` were abandoned / no-result prior to ball bowled.
   - 100% of matches in `ball_by_ball.csv` join cleanly to `matches.csv`.
2. **Player Linking (`player_id`):**
   - 100% of `striker_id` (888) and `bowler_id` (647) exist in `competition_team_player_mapping.csv`.
   - Primary linking is strictly implemented via `player_id` and `match_id`. Player names are retained purely for human readability.
3. **Competition Linking (`comp_id`):**
   - 100% of matches join cleanly to `competitions.csv`.

---

### 5. Ball Mechanics & Data Quality Rules Established
1. **Batter Runs:** Stored in `runs`. Fours and sixes are verified with `is_four` and `is_six`.
2. **Extras & Legal Deliveries:**
   - `extras_type == 'wide'`: NOT a legal ball for batter (does not count as ball faced), NOT a legal delivery for bowler (bowler must re-bowl). Concedes 1 run + `extras_2_runs` charged to bowler.
   - `extras_type == 'Overstep'` (No Ball): Counts as ball faced for batter, NOT a legal delivery for bowler. Concedes 1 penalty run + batter runs charged to bowler.
   - `extras_type in ['byes', 'legbyes']`: Legal ball for both, adds to team total, NOT charged against bowler economy, NOT credited to batter.
3. **Wicket Attribution:**
   - Bowler wickets: `dismissal_type in ['Caught', 'Bowled', 'LBW', 'Stump', 'Hit Wicket']`.
   - Non-bowler dismissals: `dismissal_type in ['RunOut', 'Retire Out', 'Obstracting the field', 'Obstructing the field']` are NOT credited to the bowler.
4. **Overs Indexing:** `overid` spans 1 to 20 (1 = 1st over / 0.1–0.6; 20 = 20th over / 19.1–19.6). Death overs are strictly defined as `overid in [16, 17, 18, 19, 20]`.
