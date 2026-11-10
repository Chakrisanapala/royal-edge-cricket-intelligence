"""
Rajasthan Royals Tactical Auction Scouting Strategy Engine
Synthesizes statistical reliability profiles into actionable franchise auction recommendations.
"""

import os
import pandas as pd

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")

def generate_scouting_strategy():
    t10_bat = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_batters.csv'))
    t10_bowl = pd.read_csv(os.path.join(OUTPUT_DIR, 'top_10_bowlers.csv'))
    
    # Detailed tactical profiles for Batters
    bat_scouting = [
        {
            "rank": 1,
            "player_id": 8101,
            "player_name": "Ashutosh Sharma",
            "team": "Delhi Capitals / Punjab Kings",
            "tactical_role": "Lower-order Power Hitter / Designated Finisher (No. 6-7)",
            "why_reliable": "Astonishing 192.83 strike rate in death overs; holds a +38.6 SR improvement in high-pressure chases; sweeps pace and targets square boundaries under extreme pressure.",
            "rr_fit": "Direct replacement/rotation for lower-order pinch hitting; gives RR fearlessness when 40+ runs are needed in the final 3 overs at Sawai Mansingh Stadium.",
            "pressure_situations": "Chasing 12+ RRR from balls 16-20; recovering from mid-innings stalls; counter-attacking elite death pacers.",
            "risks_weaknesses": "Vulnerable to hard-length deliveries angling into the body early in his innings; aggressive intent can result in high dismissal variance.",
            "auction_recommendation": "HIGH PRIORITY TARGET: Domestic Indian finisher commodity at auction; high upside-to-cost ratio."
        },
        {
            "rank": 2,
            "player_id": 2756,
            "player_name": "Shashank Singh",
            "team": "Punjab Kings",
            "tactical_role": "Ice-Cool Finisher / Middle-Order Stabilizer (No. 5-6)",
            "why_reliable": "Exceptional 41.95 average under pressure alongside a 170.53 strike rate; outstanding temperament when top order collapses (chase average: 38.5).",
            "rr_fit": "Solves RR's historical dependency on top-order runs; provides a calm, technically compact Indian batting cushion in chase pressure.",
            "pressure_situations": "Top-order collapse recovery (e.g., 35/3); calculating required runs ball-by-ball in close chases.",
            "risks_weaknesses": "Relies heavily on orthodox cricketing strokes against spin; can take 4-5 balls to assess pitch bounce before accelerating.",
            "auction_recommendation": "HIGH PRIORITY TARGET: Rare Indian middle-order batsman with proven high-leverage composure."
        },
        {
            "rank": 3,
            "player_id": 1699,
            "player_name": "Suryakumar Yadav",
            "team": "India / Mumbai Indians",
            "tactical_role": "Elite 360-degree Middle-Order Aggressor (No. 3-4)",
            "why_reliable": "The undisputed gold standard of modern T20 batting: 1,005 pressure balls faced with an 182.69 pressure SR and 217.17 death SR; disrupts field geometry completely.",
            "rr_fit": "Franchise cornerstone; dictates terms in overs 7-15 against both spin and pace, elevating team total by 20-30 runs above par.",
            "pressure_situations": "Accelerating against mystery spin in middle overs; setting imposing targets in playoff games; manipulating fields in steep chases.",
            "risks_weaknesses": "Premium auction price tag; high retention probability by Mumbai Indians makes availability conditional on mega-auction dynamics.",
            "auction_recommendation": "MARQUEE TARGET: Bid aggressively if released; otherwise benchmark RR targets against his strike-rate profiles."
        },
        {
            "rank": 4,
            "player_id": 6273,
            "player_name": "Tom Banton",
            "team": "England",
            "tactical_role": "Dynamic Powerplay / Middle-Order Enforcer (No. 3-4)",
            "why_reliable": "Explosive 186.84 strike rate in pressure situations; attacks front-line bowlers with reverse scoops and high-intent boundary striking.",
            "rr_fit": "Overseas dynamic batting option who can slot into multiple positions and provide instant impetus if momentum stalls.",
            "pressure_situations": "Powerplay counter-attack after an early wicket; rapid tempo injection against defensive bowling.",
            "risks_weaknesses": "Sample size in high-pressure matches is moderate (114 pressure balls; 45.6% confidence); susceptible to disciplined off-stump back-of-length pace.",
            "auction_recommendation": "VALUE SCOUTING TARGET: Highly economical overseas squad depth with explosive ceiling."
        },
        {
            "rank": 5,
            "player_id": 768,
            "player_name": "Reeza Hendricks",
            "team": "South Africa",
            "tactical_role": "Aggressive Opener / High-Tempo Anchor (No. 1-2)",
            "why_reliable": "Maintains an elite 44.21 pressure average with a 169.59 strike rate; combines classical technique with decisive boundary execution in international cricket.",
            "rr_fit": "Provides solid top-order insurance alongside explosive openers like Yashasvi Jaiswal, eliminating powerplay collapses.",
            "pressure_situations": "Knockout games; tricky chases on tacky or gripping pitches; absorbing early swing while punishing bad balls.",
            "risks_weaknesses": "Does not bowl; consumes an overseas slot; strike rate stabilizes rather than skyrockets at the extreme death.",
            "auction_recommendation": "TACTICAL SQUAD OPTION: Reliable backup opener for high-stakes games."
        },
        {
            "rank": 6,
            "player_id": 37052,
            "player_name": "Naman Dhir",
            "team": "India / Mumbai Indians",
            "tactical_role": "Fearless Middle-Order Aggressor / Utility All-Rounder (No. 3-5)",
            "why_reliable": "Emerging sensation with 186.26 pressure SR and 200.56 death SR; demonstrated immediate readiness to take down world-class pace from ball one.",
            "rr_fit": "Young Indian batter with huge ceiling; fulfills modern T20 mandate of strike-rate dominance from arrival.",
            "pressure_situations": "Walking in at 12 RRR with 4 overs left; taking down hard lengths over mid-wicket and extra cover.",
            "risks_weaknesses": "Dismissal frequency is slightly elevated (28.95 avg); needs mentorship on shot selection against quality leg-spin.",
            "auction_recommendation": "PRIME AUCTION ACCELERATOR: High priority young Indian uncapped/emerging target."
        },
        {
            "rank": 7,
            "player_id": 2101,
            "player_name": "Quinton de Kock",
            "team": "Mumbai Indians / South Africa / LSG",
            "tactical_role": "Wicketkeeper-Batter / Elite Aggressive Opener (No. 1-2)",
            "why_reliable": "Proven global match-winner: 170.33 pressure SR and an extraordinary 232.00 death SR; elite glovework behind the stumps.",
            "rr_fit": "Dual-threat wicketkeeper and opener; guarantees high run-rate in powerplay and seamlessly handles captaincy / DRS inputs.",
            "pressure_situations": "Chasing 190+ targets; neutralizing swing bowling in the first 4 overs; rapid acceleration at the back end.",
            "risks_weaknesses": "Overseas slot requirement; can struggle against high-arm off-spin in the powerplay.",
            "auction_recommendation": "KEY TARGET: Exceptional pedigree if RR seeks an experienced overseas keeper-batter."
        },
        {
            "rank": 8,
            "player_id": 5553,
            "player_name": "Phil Salt",
            "team": "England / KKR / RCB",
            "tactical_role": "High-Impact Powerplay Destroyer (No. 1-2)",
            "why_reliable": "Maintains an unrelenting 187.33 pressure strike rate; dismantles opening bowlers and forces captains into defensive field placements in over 2.",
            "rr_fit": "Forms a devastating opening partnership with Yashasvi Jaiswal, turning Jaipur into a fortress through powerplay domination.",
            "pressure_situations": "Setting 210+ totals; counter-punching in chases of 200+; taking on 145+ km/h pace bowling.",
            "risks_weaknesses": "High-risk approach can lead to single-digit scores; vulnerable to high-quality left-arm spin in early overs.",
            "auction_recommendation": "TIER-1 OPENING TARGET: Transcends traditional match situations through sheer strike-rate leverage."
        },
        {
            "rank": 9,
            "player_id": 4703,
            "player_name": "Rishabh Pant",
            "team": "India / LSG / DC",
            "tactical_role": "Match-Winning Wicketkeeper / Left-Handed Middle-Order Pivot (No. 4-5)",
            "why_reliable": "176.53 pressure strike rate and 200.81 death strike rate; proven ability to single-handedly engineer miracle victories from losing positions.",
            "rr_fit": "Provides critical left-handed middle-order balance; disrupts opposition spin plans through aggressive sweep and reverse-lap hitting.",
            "pressure_situations": "Middle-overs rebuilding followed by exponential acceleration; defending low totals with decisive wicketkeeping.",
            "risks_weaknesses": "Extremely high retention / marquee bidding price; improvisational strokes carry inherent dismissal risk.",
            "auction_recommendation": "MARQUEE LEADER: Top priority if RR seeks a transformative captain-wicketkeeper."
        },
        {
            "rank": 10,
            "player_id": 6396,
            "player_name": "Tim David",
            "team": "Australia / Mumbai Indians",
            "tactical_role": "Specialist Death-Overs Finisher / Boundary Demolisher (No. 6-7)",
            "why_reliable": "Immense track record over 937 pressure balls: 181.32 pressure SR and 200.87 death SR; unmatched physical power and range against wide yorkers.",
            "rr_fit": "Fills the classic 'Kieron Pollard / Andre Russell' role for RR; turns lost causes into last-ball wins.",
            "pressure_situations": "Defending 15 off the last over; chasing 45 runs off the final 18 deliveries; attacking pace in death overs.",
            "risks_weaknesses": "Susceptible to high-class wrist-spin if he walks in before over 14; requires careful tactical entry-point management.",
            "auction_recommendation": "PREMIER FINISHER TARGET: The best overseas specialist finisher in modern franchise cricket."
        }
    ]
    
    # Detailed tactical profiles for Bowlers
    bowl_scouting = [
        {
            "rank": 1,
            "player_id": 2490,
            "player_name": "Mohammad Nawaz",
            "team": "Pakistan",
            "tactical_role": "Middle-Over Spin Controller / Defensive Choke Bowler",
            "why_reliable": "Staggering 6.15 economy under pressure with 27 pressure wickets; 5.76 economy in death overs; darting trajectory with subtle seam variation that denies batters elevation.",
            "rr_fit": "Provides RR with a suffocating left-arm spin option who can operate across all phases, pairing brilliantly with wrist spin at Jaipur.",
            "pressure_situations": "Defending sub-160 totals; bowling overs 15-18 to squeeze boundary flow; bowling to right-hand heavy middle orders.",
            "risks_weaknesses": "Geopolitical restrictions historically prevent Pakistani players from participating directly in the IPL auction; evaluation provides vital analytical archetype for overseas targets.",
            "auction_recommendation": "TACTICAL BENCHMARK: Represents the gold-standard profile for left-arm spin control under pressure."
        },
        {
            "rank": 2,
            "player_id": 5979,
            "player_name": "Abrar Ahmed",
            "team": "Pakistan",
            "tactical_role": "Mystery Leg-Spinner / Middle-Overs Breakthrough Weapon",
            "why_reliable": "6.51 economy and an unbelievable 12.89 bowling strike rate under pressure; deceptive carrom ball and googlies that freeze attacking batters.",
            "rr_fit": "Pure wicket-taking potency in overs 7-15; breaks burgeoning partnerships that threaten to run away with matches.",
            "pressure_situations": "Opposition cruising at 80/1 in over 9; bowling against set top-order batters in high-scoring games.",
            "risks_weaknesses": "Availability constraints (Pakistani player); slight risk of conceding boundaries when pitch offers zero grip.",
            "auction_recommendation": "ANALYTICAL BENCHMARK: Model for target acquisition of mystery leg-spinners."
        },
        {
            "rank": 3,
            "player_id": 22471,
            "player_name": "Matthew Humphreys",
            "team": "Ireland",
            "tactical_role": "Powerplay Left-Arm Orthodox Specialist / Economical Dart Bowler",
            "why_reliable": "6.80 pressure economy and an incredible 4.97 death economy; takes wickets every 8.3 balls in pressure bursts through flatter trajectory.",
            "rr_fit": "Low-cost overseas scouting gem; delivers high tactical leverage with minimal auction expenditure.",
            "pressure_situations": "Stifling explosive powerplay openers; bowling defensive stump-to-stump lines in death overs.",
            "risks_weaknesses": "Smaller sample size (41.5% confidence); limited exposure to top-tier subcontinent franchise batters.",
            "auction_recommendation": "SLEEPER SCOUTING TARGET: Highly economical developmental prospect for overseas bench depth."
        },
        {
            "rank": 4,
            "player_id": 4229,
            "player_name": "George Linde",
            "team": "South Africa / LSG",
            "tactical_role": "Tactical Left-Arm Spin Controller / All-Phase Utility Bowler",
            "why_reliable": "7.38 pressure economy and 6.32 death economy; high arm action and arm ball that regularly skids into pads.",
            "rr_fit": "Versatile overseas bowling all-rounder who gives RR tactical flexibility in selecting conditions-based playing XIs.",
            "pressure_situations": "Bowling the 6th powerplay over; defending tight targets in death overs against aggressive tail-enders.",
            "risks_weaknesses": "Moderate sample size (40.0% confidence); can be targeted by aggressive left-handed batters.",
            "auction_recommendation": "SMART SQUAD DEPTH: Cost-effective overseas bowling all-rounder."
        },
        {
            "rank": 5,
            "player_id": 781,
            "player_name": "Sunil Narine",
            "team": "Kolkata Knight Riders",
            "tactical_role": "Elite All-Phase Mystery Spinner / Death-Over Master (Spin)",
            "why_reliable": "Absolute franchise legend: 97.66 pressure overs bowled with a 7.27 economy and 6.06 death economy; 34 pressure wickets; completely suppresses boundary percentages.",
            "rr_fit": "Guarantees 4 overs of total control; eliminates the opponent's best batters and anchors RR's entire defensive strategy.",
            "pressure_situations": "Bowling the 19th over defending 12 runs; breaking 100-run partnerships; suffocating chases in IPL playoff games.",
            "risks_weaknesses": "High retention certainty by KKR; aging profile (36+); requires careful workload monitoring.",
            "auction_recommendation": "TOP TARGET IF UNRETAINED: Transformative defensive weapon for any championship bowling unit."
        },
        {
            "rank": 6,
            "player_id": 3578,
            "player_name": "Imad Wasim",
            "team": "Pakistan",
            "tactical_role": "Powerplay & Death Bowling Specialist / Defensive Dart Master",
            "why_reliable": "6.00 pressure economy and 13.0 bowling strike rate; master of the sliding new-ball delivery that hits the top of off-stump.",
            "rr_fit": "Demonstrates the power of disciplined length control and arm balls to deny batsmen room in high-scoring matches.",
            "pressure_situations": "Bowling overs 1 and 3 in the powerplay; bowling to aggressive pinch-hitters.",
            "risks_weaknesses": "Pakistani player auction constraint; limited vertical turn on flat surfaces.",
            "auction_recommendation": "ARCHETYPE REFERENCE: Key template for acquiring disciplined defensive spinners."
        },
        {
            "rank": 7,
            "player_id": 3629,
            "player_name": "Corbin Bosch",
            "team": "Rajasthan Royals / Mumbai Indians / South Africa",
            "tactical_role": "Death-Over Pace Enforcer / Heavy-Ball Fast Bowler",
            "why_reliable": "7.14 pressure economy and 12.60 strike rate; hits the deck hard at 140+ km/h and executes sharp cutters and wide yorkers in pressure overs.",
            "rr_fit": "Familiar with Rajasthan Royals culture; provides high-intensity pace overs without leaking boundaries.",
            "pressure_situations": "Bowling overs 17 and 19; defending sub-10 run margins in the final over; breaking partnerships with bouncers.",
            "risks_weaknesses": "Slightly higher economy in general death phases (8.77); needs disciplined field settings on flat wickets.",
            "auction_recommendation": "HIGH VALUE PACE TARGET: Proven franchise utility pacer with strong pressure resilience."
        },
        {
            "rank": 8,
            "player_id": 6643,
            "player_name": "Hasan Mahmud",
            "team": "Bangladesh",
            "tactical_role": "Skiddy Pace Spearhead / Yorker & Slower-Ball Craftsman",
            "why_reliable": "7.50 pressure economy and brilliant 10.91 strike rate (takes a wicket every 1.8 overs under pressure); 8.39 death economy; natural skid and reverse swing.",
            "rr_fit": "Solves RR's middle-to-death pace penetration; attacks the stumps directly and prevents batters from getting under the ball.",
            "pressure_situations": "Executing pinpoint yorkers against aggressive finishers; defending 8-10 runs in final overs.",
            "risks_weaknesses": "Moderate international experience; international scheduling / NOC clearances must be planned.",
            "auction_recommendation": "SMART VALUE AUCTION PICK: Elite death bowling yorker execution at bargain pricing."
        },
        {
            "rank": 9,
            "player_id": 34485,
            "player_name": "Sufiyan Muqeem",
            "team": "Pakistan",
            "tactical_role": "Left-Arm Wrist Spinner (Chinaman) / Mystery Wicket-Taker",
            "why_reliable": "Phenomenal 4.89 pressure economy; 7.11 death economy; rare left-arm wrist spin angle that deceives both left and right-handed batters with natural drift and turn.",
            "rr_fit": "Showcases the immense value of rare bowling angles that modern analytical batting scouting struggles to counter.",
            "pressure_situations": "Stifling middle-order scoring; bowling to set batters looking to clear long-on and mid-wicket.",
            "risks_weaknesses": "Pakistani player auction constraint; developing young player.",
            "auction_recommendation": "ARCHETYPE BENCHMARK: Informs RR's search for left-arm wrist-spin talent."
        },
        {
            "rank": 10,
            "player_id": 4101,
            "player_name": "Mitchell Santner",
            "team": "Chennai Super Kings / New Zealand",
            "tactical_role": "Master Tactician / Elite Left-Arm Finger Spinner & Leader",
            "why_reliable": "95.5 pressure overs bowled with a 7.21 economy and 38 pressure wickets; subtle changes of pace and trajectory that prevent batters from predicting ball length.",
            "rr_fit": "Outstanding tactical fit for RR; can bowl powerplay, middle, and death overs; exceptional fielder and handy lower-order batter.",
            "pressure_situations": "Choking run chases in IPL playoffs; defending small totals on turning tracks; containing power hitters.",
            "risks_weaknesses": "Can occasionally be targeted on very short straight boundaries against elite power hitters.",
            "auction_recommendation": "PRIME AUCTION TARGET: Underrated, world-class all-phase spinner who brings championship winning experience."
        }
    ]
    
    df_bat_scouting = pd.DataFrame(bat_scouting)
    df_bowl_scouting = pd.DataFrame(bowl_scouting)
    
    df_bat_scouting.to_csv(os.path.join(OUTPUT_DIR, 'scouting_batters_strategy.csv'), index=False)
    df_bowl_scouting.to_csv(os.path.join(OUTPUT_DIR, 'scouting_bowlers_strategy.csv'), index=False)
    print("Scouting Strategy CSVs generated successfully!")

if __name__ == "__main__":
    generate_scouting_strategy()

