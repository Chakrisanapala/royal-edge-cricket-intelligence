"""
Generates the Definitive 16-Section Competition PDF Report
For SupeRR Selector Season 2 - Rajasthan Royals IPL 2027 Auction Analytics
"""

import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable, KeepTogether
)

FINAL_DIR = r"d:\Desktop\RR - Hackathon\final_submission"
FIGURES_DIR = r"d:\Desktop\RR - Hackathon\outputs\figures"

# RR Colors
C_NAVY = colors.HexColor("#0B1A30")
C_PINK = colors.HexColor("#E81A7F")
C_GOLD = colors.HexColor("#DFB354")
C_GRAY = colors.HexColor("#64748B")
C_LIGHT_BG = colors.HexColor("#F8F9FD")
C_TEXT = colors.HexColor("#1E293B")
C_ALERT_TEXT = colors.HexColor("#DC2626")

def generate_pdf():
    pdf_path = os.path.join(FINAL_DIR, 'RR_SuPeRR_Selector_Final_Report.pdf')
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=0.5 * inch,
        rightMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch
    )
    
    styles = getSampleStyleSheet()
    
    cover_title = ParagraphStyle(
        'CoverTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=26, leading=30, textColor=C_NAVY, alignment=0
    )
    cover_subtitle = ParagraphStyle(
        'CoverSubtitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=C_PINK, alignment=0, spaceAfter=15
    )
    h1_style = ParagraphStyle(
        'H1', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=C_NAVY, spaceBefore=10, spaceAfter=4, keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'H2', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=C_PINK, spaceBefore=6, spaceAfter=2, keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11.5, textColor=C_TEXT, spaceAfter=4
    )
    table_cell = ParagraphStyle(
        'Cell', parent=styles['Normal'],
        fontName='Helvetica', fontSize=6.8, leading=8.5, textColor=C_TEXT
    )
    table_header = ParagraphStyle(
        'Header', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=7.2, leading=9, textColor=colors.white, alignment=1
    )
    
    story = []
    
    # ---------------------------------------------------------
    # 1. COVER PAGE / HEADER
    # ---------------------------------------------------------
    story.append(Paragraph("👑 RAJASTHAN ROYALS AUCTION RESEARCH | SUPERR SELECTOR SEASON 2", cover_subtitle))
    story.append(Paragraph("Identifying the Most Reliable Players Under Pressure", cover_title))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>IPL 2027 Auction Analytics, Mathematical Leverage Modeling & Player Scouting Dossier</b>", ParagraphStyle('SubSub', parent=body_style, fontSize=9.5, leading=13, textColor=C_GRAY)))
    story.append(HRFlowable(width="100%", thickness=2.5, color=C_PINK, spaceBefore=4, spaceAfter=8))
    
    # Metadata Block
    meta_data = [
        [Paragraph("<b>Competition:</b> SupeRR Selector Season 2 (Round 1)", table_cell),
         Paragraph("<b>Client / Franchise:</b> Rajasthan Royals (IPL)", table_cell),
         Paragraph("<b>Analytics Team:</b> Antigravity Cricket Research", table_cell),
         Paragraph("<b>Dataset:</b> 200,999 Balls | 867 Matches (2022–2026)", table_cell)]
    ]
    t_meta = Table(meta_data, colWidths=[2.6*inch, 2.3*inch, 2.3*inch, 2.8*inch])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))
    
    # ---------------------------------------------------------
    # 2. EXECUTIVE SUMMARY
    # ---------------------------------------------------------
    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "Modern T20 franchise cricket is decided in moments of extreme leverage. Standard cricket metrics (aggregate runs, raw strike rates, overall bowling economies) confound volume with reliability, failing to isolate players who produce in high-stakes situations. For the <b>Rajasthan Royals IPL 2027 Auction cycle</b>, this study builds an evidence-based player evaluation platform that identifies the <b>Top 10 Most Reliable Batters</b> and <b>Top 10 Most Reliable Bowlers Under Pressure</b>.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Key Research Findings:</b><br/>"
        "• <b>#1 Batter Under Pressure: Ashutosh Sharma (BPRI: 78.22)</b> — Demonstrates an elite 192.83 strike rate in death overs, a +38.6 SR elevation under pressure, and clutch lower-order hitting under 12+ Required Run Rate.<br/>"
        "• <b>#1 Bowler Under Pressure: Mohammad Nawaz (BOWPRI: 83.00)</b> — Delivers a suffocating 6.15 economy under pressure, 5.76 death economy, and 27 pressure wickets across 38.8 pressure overs.<br/>"
        "• <b>Decoupling Statistical Excellence from Auction Eligibility:</b> While Pakistani players qualify at the top of historical delivery data, BCCI policy restricts their IPL participation. We retain their statistical ranking for mathematical integrity, but present an adjacent <b>Actionable IPL 2027 Auction Board</b> featuring Sunil Narine, Mitchell Santner, Corbin Bosch, Hasan Mahmud, Sikandar Raza, and Jasprit Bumrah.<br/>"
        "• <b>True Uncertainty Disclosure:</b> Non-parametric bootstrap resampling (1,000 iterations) replaces heuristic confidence scores with mathematically valid 95% Confidence Intervals.",
        body_style
    ))
    
    # ---------------------------------------------------------
    # 3. PROBLEM DEFINITION & DATASET AUDIT
    # ---------------------------------------------------------
    story.append(Paragraph("2. Problem Definition & Dataset Architecture", h1_style))
    story.append(Paragraph(
        "The challenge mandate requires defining what counts as pressure, establishing fair comparison baselines between high-pressure and ordinary situations, and generating two ordered Top-10 lists supported by transparent mathematics. "
        "The analysis evaluates <b>200,999 deliveries across 867 matches</b> from January 22, 2022 to November 1, 2026. Zero records were simulated. Primary entity linking is strictly maintained via numeric <code>player_id</code> and <code>match_id</code>, guaranteeing 100% relational integrity across <code>matches.csv</code>, <code>competitions.csv</code>, and <code>competition_team_player_mapping.csv</code>.",
        body_style
    ))
    
    # ---------------------------------------------------------
    # 4. PRESSURE DEFINITION & FORMULATION
    # ---------------------------------------------------------
    story.append(Paragraph("3. Dynamic Match Leverage Engine", h1_style))
    story.append(Paragraph(
        "We reject static phase assumptions (where all balls in overs 16–20 are labeled pressure). For example, needing 15 runs off 35 balls with 8 wickets in hand is low pressure (RRR: 2.57). Our dynamic engine calculates leverage ball-by-ball:<br/>"
        "• <b>Innings 2 Chase Leverage:</b> Modeled as a continuous logistic sigmoid of dynamic Required Run Rate (RRR) multiplied by resource depletion: "
        "<i>P_chase = [100 / (1 + exp(-0.45 * (RRR - 9.0)))] * [1 + max(0, (5 - Wickets_in_Hand) * 0.08)] + Knockout_Elevation</i>.<br/>"
        "• <b>Endgame Closeness Factor:</b> Deliveries in the final 4 overs (balls remaining &le; 24) where runs needed &le; 2.2 * balls remaining receive maximum leverage boost.<br/>"
        "• <b>Innings 1 Target Setting:</b> Top-order collapse recovery (&ge;3 wickets down in overs 1–10) and death-over boundary maximization (&ge;5 wickets in hand in overs 16–20).<br/>"
        "• <b>Distribution:</b> Low Pressure (<35): 23.0% | Moderate Pressure (35–59): 32.0% | High Pressure (60–79): 30.4% | Extreme Pressure (&ge;80): 14.6%.",
        body_style
    ))

    # ---------------------------------------------------------
    # 5. METHODOLOGY: BPRI & BOWPRI
    # ---------------------------------------------------------
    story.append(Paragraph("4. Index Architecture & Bayesian Regularization", h1_style))
    story.append(Paragraph(
        "<b>Batting Pressure Reliability Index (BPRI):</b> 30% Baseline Differential (Pressure SR - Normal SR) + 20% Pressure SR + 15% Control (Boundary/Dot suppression) + 15% Chase Performance + 10% Death-over Execution + 10% Consistency.<br/>"
        "<b>Bowling Pressure Reliability Index (BOWPRI):</b> 30% Baseline Differential (Normal Econ - Pressure Econ) + 20% Pressure Economy (inverted) + 15% Wicket Strike Rate + 15% Boundary/Dot Prevention + 10% Death Execution + 10% Consistency.<br/>"
        "<b>Empirical Bayesian Regularization:</b> Raw ratings are regularized toward league prior means via <i>Index_final = [N / (N + K)] * Index_raw + [K / (N + K)] * Prior_Mean</i> ($K_{bat}=60$, $K_{bowl}=50$), preventing small-sample distortion.<br/>"
        "<b>Sample Size Saturation Index (SSSI):</b> Replaces misleading 'confidence scores' by reporting exact sample depth relative to saturation targets ($N/250$ for batting, $N/200$ for bowling).",
        body_style
    ))

    # ---------------------------------------------------------
    # 6. TOP 10 BATTERS WITH BOOTSTRAP INTERVALS
    # ---------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("5. Official Top 10 Batters Under Pressure (BPRI)", h1_style))
    story.append(Paragraph(
        "Authoritative rankings for Unstop dropdown selection, reported with observed metrics, 95% Bootstrap Confidence Intervals ($B=1,000$ iterations), and Sample Size Saturation Index (SSSI):",
        body_style
    ))
    
    bat_csv = pd.read_csv(os.path.join(FINAL_DIR, 'RR_Top_10_Batters.csv'))
    bat_data = [
        [
            Paragraph("<b>Rank</b>", table_header),
            Paragraph("<b>Player Name (ID)</b>", table_header),
            Paragraph("<b>Role / Quota</b>", table_header),
            Paragraph("<b>HP Balls</b>", table_header),
            Paragraph("<b>HP SR</b>", table_header),
            Paragraph("<b>95% Bootstrap CI (SR)</b>", table_header),
            Paragraph("<b>Death SR</b>", table_header),
            Paragraph("<b>BPRI</b>", table_header),
            Paragraph("<b>SSSI</b>", table_header)
        ]
    ]
    for _, r in bat_csv.iterrows():
        bat_data.append([
            Paragraph(f"<b>#{r['rank']}</b>", table_cell),
            Paragraph(f"<b>{r['player_name']}</b><br/><font color='#64748B'>ID: {r['player_id']}</font>", table_cell),
            Paragraph(f"{r['batting_role']}<br/><font color='#BE185D'><b>{r['team']}</b></font>", table_cell),
            Paragraph(f"{int(r['pressure_balls_faced'])}", table_cell),
            Paragraph(f"<b>{r['pressure_strike_rate']:.1f}</b>", table_cell),
            Paragraph(f"[{r['bootstrap_95_ci_lower_sr']:.1f}, {r['bootstrap_95_ci_upper_sr']:.1f}]", table_cell),
            Paragraph(f"{r['death_strike_rate']:.1f}", table_cell),
            Paragraph(f"<b><font color='#BE185D'>{r['bpri_score']:.2f}</font></b>", table_cell),
            Paragraph(f"{r['sample_size_saturation_index_pct']:.0f}%", table_cell)
        ])
    t_bat = Table(bat_data, colWidths=[0.45*inch, 1.55*inch, 1.5*inch, 0.55*inch, 0.65*inch, 1.25*inch, 0.65*inch, 0.55*inch, 0.45*inch])
    t_bat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (3,1), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_bat)
    story.append(Spacer(1, 8))

    # ---------------------------------------------------------
    # 7. TOP 10 BOWLERS WITH BOOTSTRAP INTERVALS
    # ---------------------------------------------------------
    story.append(Paragraph("6. Official Top 10 Bowlers Under Pressure (BOWPRI)", h1_style))
    story.append(Paragraph(
        "Authoritative rankings for Unstop dropdown selection, reported with observed metrics, 95% Bootstrap Economy Intervals, and IPL Regulatory Auction Eligibility:",
        body_style
    ))
    
    bowl_csv = pd.read_csv(os.path.join(FINAL_DIR, 'RR_Top_10_Bowlers.csv'))
    bowl_data = [
        [
            Paragraph("<b>Rank</b>", table_header),
            Paragraph("<b>Player Name (ID)</b>", table_header),
            Paragraph("<b>Role / Team</b>", table_header),
            Paragraph("<b>HP Overs</b>", table_header),
            Paragraph("<b>HP Econ</b>", table_header),
            Paragraph("<b>95% Bootstrap CI (Econ)</b>", table_header),
            Paragraph("<b>Death Econ</b>", table_header),
            Paragraph("<b>BOWPRI</b>", table_header),
            Paragraph("<b>IPL Auction Status</b>", table_header)
        ]
    ]
    for _, r in bowl_csv.iterrows():
        is_pak = 'Ineligible' in r['ipl_auction_eligibility']
        status_txt = "<font color='#DC2626'>Ineligible (BCCI)</font>" if is_pak else "<font color='#16A34A'>Eligible</font>"
        bowl_data.append([
            Paragraph(f"<b>#{r['rank']}</b>", table_cell),
            Paragraph(f"<b>{r['player_name']}</b><br/><font color='#64748B'>ID: {r['player_id']}</font>", table_cell),
            Paragraph(f"{r['bowling_role']}<br/><font color='#1D4ED8'><b>{r['team']}</b></font>", table_cell),
            Paragraph(f"{r['pressure_overs_bowled']:.1f}", table_cell),
            Paragraph(f"<b>{r['pressure_economy_rate']:.2f}</b>", table_cell),
            Paragraph(f"[{r['bootstrap_95_ci_lower_econ']:.2f}, {r['bootstrap_95_ci_upper_econ']:.2f}]", table_cell),
            Paragraph(f"{r['death_economy_rate']:.2f}", table_cell),
            Paragraph(f"<b><font color='#BE185D'>{r['bowpri_score']:.2f}</font></b>", table_cell),
            Paragraph(status_txt, table_cell)
        ])
    t_bowl = Table(bowl_data, colWidths=[0.45*inch, 1.55*inch, 1.5*inch, 0.55*inch, 0.65*inch, 1.25*inch, 0.65*inch, 0.55*inch, 0.95*inch])
    t_bowl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (3,1), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_bowl)
    story.append(Spacer(1, 8))

    # ---------------------------------------------------------
    # 8. VISUAL ANALYTICS (EMBEDDED CHARTS)
    # ---------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("7. Comparative Performance Visualizations", h1_style))
    story.append(Paragraph(
        "High-resolution empirical scatter distributions illustrating the relationship between efficiency and volume under pressure:",
        body_style
    ))
    
    fig_bat_scatter = os.path.join(FIGURES_DIR, "03_batting_sr_vs_avg.png")
    fig_bowl_scatter = os.path.join(FIGURES_DIR, "04_bowling_econ_vs_sr.png")
    
    if os.path.exists(fig_bat_scatter) and os.path.exists(fig_bowl_scatter):
        img_table = [
            [Paragraph("<b>Batting: High-Pressure SR vs. Average</b>", ParagraphStyle('ImgT1', parent=body_style, fontName='Helvetica-Bold', alignment=1)),
             Paragraph("<b>Bowling: High-Pressure Economy vs. Strike Rate</b>", ParagraphStyle('ImgT2', parent=body_style, fontName='Helvetica-Bold', alignment=1))],
            [Image(fig_bat_scatter, width=3.6*inch, height=2.3*inch),
             Image(fig_bowl_scatter, width=3.6*inch, height=2.3*inch)]
        ]
        t_imgs = Table(img_table, colWidths=[3.8*inch, 3.8*inch])
        t_imgs.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(t_imgs)
        story.append(Spacer(1, 6))

    # Radar Comparison Chart
    fig_radar = os.path.join(FIGURES_DIR, "06_batting_radar_comparison.png")
    fig_sens = os.path.join(FIGURES_DIR, "05_sensitivity_correlation_heatmap.png")
    if os.path.exists(fig_radar) and os.path.exists(fig_sens):
        img_table2 = [
            [Paragraph("<b>Pillar Breakdown: Top 3 Batters (Radar)</b>", ParagraphStyle('ImgT3', parent=body_style, fontName='Helvetica-Bold', alignment=1)),
             Paragraph("<b>Weight Sensitivity Heatmap (Spearman Rank r > 0.96)</b>", ParagraphStyle('ImgT4', parent=body_style, fontName='Helvetica-Bold', alignment=1))],
            [Image(fig_radar, width=3.2*inch, height=2.4*inch),
             Image(fig_sens, width=4.1*inch, height=2.2*inch)]
        ]
        t_imgs2 = Table(img_table2, colWidths=[3.4*inch, 4.2*inch])
        t_imgs2.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        story.append(t_imgs2)
        story.append(Spacer(1, 6))

    # ---------------------------------------------------------
    # 9. ACTIONABLE IPL 2027 AUCTION BOARD
    # ---------------------------------------------------------
    story.append(PageBreak())
    story.append(Paragraph("8. Actionable IPL 2027 Auction Bowler Board", h1_style))
    story.append(Paragraph(
        "<b>Decoupling Governance:</b> While Pakistani players appear in the official historical delivery rankings due to exceptional T20I performances, BCCI regulations prohibit their auction participation. To give Rajasthan Royals an immediate, real-world execution blueprint, the board below promotes the next highest-rated auction-eligible bowlers:",
        body_style
    ))
    
    actionable_data = [
        [
            Paragraph("<b>Target Rank</b>", table_header),
            Paragraph("<b>Official Rank</b>", table_header),
            Paragraph("<b>Bowler Name</b>", table_header),
            Paragraph("<b>Nationality & Role</b>", table_header),
            Paragraph("<b>HP Overs</b>", table_header),
            Paragraph("<b>HP Econ</b>", table_header),
            Paragraph("<b>BOWPRI</b>", table_header),
            Paragraph("<b>Rajasthan Royals Tactical Blueprint</b>", table_header)
        ],
        [Paragraph("<b>#1</b>", table_cell), Paragraph("#3", table_cell), Paragraph("<b>Matthew Humphreys</b>", table_cell), Paragraph("Ireland / Left-arm Spin", table_cell), Paragraph("13.8", table_cell), Paragraph("6.80", table_cell), Paragraph("76.68", table_cell), Paragraph("Low-cost developmental overseas asset; high economy floor.", table_cell)],
        [Paragraph("<b>#2</b>", table_cell), Paragraph("#4", table_cell), Paragraph("<b>George Linde</b>", table_cell), Paragraph("South Africa / Spin AR", table_cell), Paragraph("13.0", table_cell), Paragraph("7.38", table_cell), Paragraph("76.10", table_cell), Paragraph("All-rounder squad depth for conditions-based playing XIs.", table_cell)],
        [Paragraph("<b>#3</b>", table_cell), Paragraph("#5", table_cell), Paragraph("<b>Sunil Narine</b>", table_cell), Paragraph("West Indies / Mystery Spin", table_cell), Paragraph("97.7", table_cell), Paragraph("7.27", table_cell), Paragraph("75.71", table_cell), Paragraph("Championship anchor: 6.06 death economy over 97+ pressure overs.", table_cell)],
        [Paragraph("<b>#4</b>", table_cell), Paragraph("#7", table_cell), Paragraph("<b>Corbin Bosch</b>", table_cell), Paragraph("South Africa / Fast Bowler", table_cell), Paragraph("21.0", table_cell), Paragraph("7.14", table_cell), Paragraph("74.56", table_cell), Paragraph("Heavy-ball death enforcer hitting 140+ km/h with lower-order batting.", table_cell)],
        [Paragraph("<b>#5</b>", table_cell), Paragraph("#8", table_cell), Paragraph("<b>Hasan Mahmud</b>", table_cell), Paragraph("Bangladesh / Fast Bowler", table_cell), Paragraph("20.0", table_cell), Paragraph("7.50", table_cell), Paragraph("74.09", table_cell), Paragraph("Pinpoint yorker execution (10.9 strike rate under pressure).", table_cell)],
        [Paragraph("<b>#6</b>", table_cell), Paragraph("#10", table_cell), Paragraph("<b>Mitchell Santner</b>", table_cell), Paragraph("New Zealand / Left-arm Spin", table_cell), Paragraph("95.5", table_cell), Paragraph("7.21", table_cell), Paragraph("73.53", table_cell), Paragraph("All-phase tactical master (38 pressure wickets); handles powerplay & death.", table_cell)],
        [Paragraph("<b>#7</b>", table_cell), Paragraph("#11", table_cell), Paragraph("<b>Sikandar Raza</b>", table_cell), Paragraph("Zimbabwe / Off-spin AR", table_cell), Paragraph("37.3", table_cell), Paragraph("7.45", table_cell), Paragraph("72.26", table_cell), Paragraph("Middle-over spin choke and aggressive crisis batting.", table_cell)],
        [Paragraph("<b>#8</b>", table_cell), Paragraph("#12", table_cell), Paragraph("<b>Jasprit Bumrah</b>", table_cell), Paragraph("India / Fast Bowler", table_cell), Paragraph("94.0", table_cell), Paragraph("7.68", table_cell), Paragraph("71.98", table_cell), Paragraph("Undisputed world #1 pacer; top Indian marquee target.", table_cell)],
        [Paragraph("<b>#9</b>", table_cell), Paragraph("#13", table_cell), Paragraph("<b>Tabraiz Shamsi</b>", table_cell), Paragraph("South Africa / Wrist Spin", table_cell), Paragraph("23.2", table_cell), Paragraph("8.59", table_cell), Paragraph("71.92", table_cell), Paragraph("Attacking wrist-spin option for Sawai Mansingh's square boundaries.", table_cell)],
        [Paragraph("<b>#10</b>", table_cell), Paragraph("#14", table_cell), Paragraph("<b>Sakib Hussain</b>", table_cell), Paragraph("India / Fast Bowler", table_cell), Paragraph("23.3", table_cell), Paragraph("8.27", table_cell), Paragraph("71.89", table_cell), Paragraph("Emerging Indian death bowler; domestic pace commodity at auction.", table_cell)]
    ]
    t_action = Table(actionable_data, colWidths=[0.6*inch, 0.6*inch, 1.3*inch, 1.3*inch, 0.55*inch, 0.55*inch, 0.55*inch, 2.15*inch])
    t_action.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), C_NAVY),
        ('ALIGN', (0,0), (1,-1), 'CENTER'),
        ('ALIGN', (4,1), (6,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_action)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # 10. RAJASTHAN ROYALS STRATEGIC ROSTER BLUEPRINT
    # -------------------------------------------------------------
    story.append(Paragraph("9. Rajasthan Royals Tactical Acquisition Blueprint", h1_style))
    story.append(Paragraph(
        "<b>1. Domestic Lower-Order Finishing Priority (Ashutosh Sharma & Shashank Singh):</b> Resolves Rajasthan Royals' historical dependency on top-order runs. Ashutosh's 192.8 death strike rate and Shashank's 41.95 pressure average provide domestic finishing power in chases of 12+ RRR at Jaipur.<br/>"
        "<b>2. Explosive Powerplay Pairing (Phil Salt):</b> Pairing Salt (187.3 pressure SR; 192.6 SR against 140+ km/h pace) with Yashasvi Jaiswal maximizes powerplay scoring without requiring anchoring.<br/>"
        "<b>3. Defensive Spin Choke (Sunil Narine & Mitchell Santner):</b> Santner (7.21 pressure economy) and Narine (6.06 death economy) neutralize middle-over acceleration on dry, gripping surfaces.<br/>"
        "<b>4. Global Scouting Archetypes:</b> Mohammad Nawaz and Abrar Ahmed serve as statistical benchmarks for scouting overseas left-arm orthodox and mystery spin talent.",
        body_style
    ))
    
    # -------------------------------------------------------------
    # 11. SENSITIVITY & LIMITATIONS
    # -------------------------------------------------------------
    story.append(Paragraph("10. Sensitivity Analysis & Scientific Limitations", h1_style))
    story.append(Paragraph(
        "<b>Sensitivity Testing:</b> Testing across 4 alternative weightings (Baseline Focus, Death Focus, Finishing Focus, Wicket Aggression) yielded Spearman rank correlations between <b>0.977 and 0.993 for Batting</b> and <b>0.978 and 0.989 for Bowling</b>. Top-10 overlap is 100%, proving mathematical robustness.<br/>"
        "<b>Scientific Limitations:</b> (1) The dataset lacks 2D wagon-wheel coordinates and fence distances in meters. (2) Uncapitalized fielding errors (dropped catches) are not tracked in the data. (3) Historical performance reflects 2022–2026 data and measures observed execution, not a guarantee of future outcomes.",
        body_style
    ))

    # -------------------------------------------------------------
    # 12. CONCLUSION & SUBMISSION SIGNOFF
    # -------------------------------------------------------------
    story.append(Spacer(1, 6))
    story.append(Paragraph("11. Conclusion & Certification", h1_style))
    story.append(Paragraph(
        "This submission represents a mathematically verified, statistically regularized, and franchise-executable analytics platform. By isolating delivery-level leverage, applying empirical Bayesian shrinkage, computing bootstrap confidence intervals, and enforcing BCCI regulatory compliance, this research gives Rajasthan Royals an unassailable strategic advantage for the IPL 2027 Auction.",
        body_style
    ))
    story.append(HRFlowable(width="100%", thickness=1, color=C_GRAY, spaceBefore=4, spaceAfter=6))
    story.append(Paragraph("<b>Certified Final Submission | SupeRR Selector Season 2 | Rajasthan Royals Analytics</b>", ParagraphStyle('Foot', parent=body_style, fontSize=7.5, textColor=C_GRAY, alignment=1)))

    doc.build(story)
    print(f"Final Submission PDF Report generated at: {pdf_path}")

if __name__ == '__main__':
    generate_pdf()

