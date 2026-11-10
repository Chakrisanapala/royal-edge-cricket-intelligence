---
name: Royal Edge Intelligence
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#e3bdc6'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#aa8890'
  outline-variant: '#5b3f47'
  surface-tint: '#ffb1c7'
  primary: '#ffb1c7'
  on-primary: '#650032'
  primary-container: '#ff4994'
  on-primary-container: '#59002b'
  inverse-primary: '#ba0061'
  secondary: '#fabc4d'
  on-secondary: '#432c00'
  secondary-container: '#bd8718'
  on-secondary-container: '#3a2600'
  tertiary: '#7bd0ff'
  on-tertiary: '#00354a'
  tertiary-container: '#009bd1'
  on-tertiary-container: '#002d40'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffd9e2'
  primary-fixed-dim: '#ffb1c7'
  on-primary-fixed: '#3e001d'
  on-primary-fixed-variant: '#8e0049'
  secondary-fixed: '#ffdead'
  secondary-fixed-dim: '#fabc4d'
  on-secondary-fixed: '#281900'
  on-secondary-fixed-variant: '#604100'
  tertiary-fixed: '#c4e7ff'
  tertiary-fixed-dim: '#7bd0ff'
  on-tertiary-fixed: '#001e2c'
  on-tertiary-fixed-variant: '#004c69'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.005em
  title-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-xs:
    fontFamily: Inter
    fontSize: 10px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.05em
  metric-display:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
  metric-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 22px
    letterSpacing: -0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-desktop: 1.25rem
  margin: 1rem
  margin-desktop: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1rem
  space-xl: 1.5rem
---

## Brand & Style

This design system establishes an elite, high-stakes sports analytics command center engineered for IPL auction rooms, strategic war rooms, and front-office scouting divisions. The aesthetic balances utilitarian computational clarity with the assertive prestige of franchise cricket.

### Personality & Tone
- **Authoritative & Mission-Critical:** Built for zero-latency comprehension under live auction timers. Every metric, percentile, and valuation must feel definitive.
- **Precision Utilitarian:** Minimal decorative chrome, high tabular density, hairline boundary framing, and clear structural hierarchy.
- **Electric Prestige:** The deep nocturnal backdrop gives focus to laser-sharp signals in the signature royal magenta and champagne gold accents.

### Design Movement
The interface operates under a **Modern Precision Technical** paradigm—merging dark command center ergonomics, hairline borders, dense tabular structures, and micro-elevation shifts to maintain maximum legibility during intense bidding sequences.

## Colors

The palette leverages a dark nocturnal base to minimize optical fatigue in low-light war rooms, punctuated by high-contrast categorical accents.

### Palette Architecture
- **Primary (`#EB107E`):** Franchise Royal Magenta. Reserved for primary actions, current active bids, critical selection targets, and high-priority alerts. Hover state transitions to `#FF2A96`.
- **Secondary (`#E5A93C`):** Royal Gold / Champagne. Strictly designated for elite player tier tags (Marquee/Icon status), purse allocation milestones, and cap room ceilings. Secondary hover state scales to `#F3C669`.
- **Tertiary (`#38BDF8`):** Ice Blue. Applied to pure statistical markers, projected true values, expected run values (xRV), and delivery phase modeling.
- **Neutral Base (`#070B14`, `#0D1322`, `#121A2D`, `#182238`):** Layered obsidian tones that define deep canvas backgrounds, secondary panels, card surfaces, and control wells.
- **Neutral Text & Dividers (`#FFFFFF`, `#94A3B8`, `#64748B`, `#1E2D4A`):** High-clarity white for primary stats, slate grey for contextual metrics, and crisp navy borders.

### Telemetry & Cricket Phase Tokens
- **Peak Performance / Surplus (`#10B981`):** High bowling economy, strike-rate spikes, value-to-cost surplus.
- **Contested / Pivot (`#F59E0B`):** Middle overs attrition, bidding pressure inflection, secondary targets.
- **Critical / Risk (`#EF4444`):** Death-overs volatility, purse exhaustion warning, extreme bid inflation.

## Typography

Typography prioritizes rapid analytical consumption. Inter is leveraged across all roles, with specific stylistic features activated for tabular analytics:

- **Tabular Figures (`tnum`):** All numeric displays, auction purse counters, strike rates, dot-ball percentages, and economy rates must enable `font-feature-settings: 'tnum' 1, 'cv05' 1`. This prevents layout shifts when auction numbers fluctuate live.
- **Metric Tokens:** `metric-display` and `metric-sm` are purpose-built for fast scout scanning across dense multi-column player matrices.
- **Micro Labels:** `label-xs` uses uppercase styling with `0.05em` letter spacing for phase indicators (POWERPLAY, MIDDLE, DEATH) and tactical designations.

## Layout & Spacing

The layout model is optimized for high information density across multi-display war room consoles, iPads, and mobile monitoring feeds.

### Grid & Structure
- **Desktop (1200px+):** 12-column dynamic fluid grid with `1.25rem` gutters. Accommodates three distinct working viewports: Left Strategic Queue (3 cols), Center Live Player Board & Analytical Deep Dive (6 cols), and Right Real-Time Auction Ledger & Roster Composition (3 cols).
- **Tablet / Mobile (360px - 1199px):** Reflows into single-column modular stacks with a consolidated bottom docked operational HUD.
- **Vertical Spacing:** Compact vertical rhythm utilizing an 8px base rhythm scaled down to 4px (`space-xs`) for tight data table rows and metric badges.

## Elevation & Depth

To maintain visual clarity without muddying data with heavy shadows, this system relies on **tonal layered surfaces** backed by **hairline micro-borders**.

### Surface Hierarchy
1. **Canvas (`#070B14`):** Base system depth. Zero elevation.
2. **Structural Paneling (`#0D1322`):** Primary command center navigation, war room filters, and permanent sideboards. Bound by hairline borders (`#1E2D4A`).
3. **Data Modules & Cards (`#121A2D`):** Primary actionable cards and player summaries. Separated by `1px solid rgba(30, 45, 74, 0.8)` or accented with `rgba(235, 16, 126, 0.15)` for active targets.
4. **Interactive Floating & Overlays (`#182238`):** Bidding modulators, confirmation sheets, and popovers. Employs a crisp perimeter stroke (`1px solid #1E2D4A`) alongside an ambient anchor shadow: `0 8px 32px -4px rgba(0, 0, 0, 0.6)`.

## Shapes

The design system adopts a **Level 1 (Soft)** shape geometry (`0.25rem` / 4px base radius). This produces sharp, high-tech instrument corners that convey precision engineering, eschewing casual roundness in favor of command console rigor.

- **Standard Elements (Cards, Inputs, Data Cells):** `0.25rem` (4px).
- **Secondary Containers & Dialogs (`rounded-lg`):** `0.5rem` (8px).
- **Pill Exceptions:** Micro status badges, metric indicators, and tactical phase tags use fully rounded pill profiles (`9999px`) to create clear shape-contrast against the structural angular cards.

## Components

### Buttons
- **Primary (Bid / Confirm Target):** Background `#EB107E`, text `#FFFFFF`, font weight 600, border radius `0.25rem`. Hover `#FF2A96`. Active scale down `0.98`. Glow effect on live auction bid button: `box-shadow: 0 0 16px rgba(235, 16, 126, 0.4)`.
- **Secondary (Strategy Alternative / Filter):** Background `rgba(18, 26, 45, 0.8)`, border `1px solid #1E2D4A`, text `#94A3B8`. Hover border `#EB107E`, text `#FFFFFF`.
- **Marquee / Premium Action:** Background `#E5A93C`, text `#070B14`, font weight 700. Hover `#F3C669`.

### Badges & Chips
- **Player Role Chips:** Solid pill shape (`9999px`), `label-xs` typography. 
  - Overseas icon/slot: `rgba(56, 189, 248, 0.12)` background, text `#38BDF8`.
  - Marquee Tier: `rgba(229, 169, 60, 0.12)` background, text `#E5A93C`.
  - Target Status: `rgba(235, 16, 126, 0.12)` background, text `#EB107E`.

### Cards & Player Modules
- Surface `#121A2D`, border `1px solid #1E2D4A`, padding `space-lg`.
- Top header carries player headshot preview, national flag identifier, base price vs current hammer price, and radar metric tags.
- Stat strips inside cards use surface `#0D1322` with hairline inner dividers.

### Data Tables & Analytics Rows
- Dense height (36px–40px per row).
- Header row styled with `label-xs`, uppercase, text `#64748B`, bottom border `1px solid #1E2D4A`.
- Alternating subtle stripe on hover: `rgba(235, 16, 126, 0.04)`.
- Active bidding row highlights with a continuous `2px` left border in `#EB107E`.

### Inputs & Bidding Increments
- Dark inset containers (`#070B14`), text `#FFFFFF`, border `1px solid #1E2D4A`.
- Focus state triggers `1px solid #EB107E` with zero outward blur bleed.
- Numeric quick-bid increment steppers (`+20L`, `+50L`, `+1Cr`) rendered in bold monospaced layout.

### Telemetry Bars & Gauges
- Purse burn-down progress bar: Track background `#0D1322`, filled fill with transition gradient `#EB107E` to `#E5A93C`.
- Over-pressure indices: Segmented micro-bars showing phase efficiency (Death Overs economy vs benchmark) colored dynamically via status tokens (`#10B981`, `#F59E0B`, `#EF4444`).