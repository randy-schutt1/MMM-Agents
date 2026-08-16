# CANONICAL MASTER SPECIFICATION (MMM-CANONICAL-V1.0)

**Document ID:** `12_MASTER_SPEC/CANONICAL_SPEC.md`  
**Classification:** Canonical Methodology Specification (Tier 1 Primary + Tier 1 X-Series Harmonized)  
**Governing Decisions:** `D-043`, `D-055`, `D-058`, `D-061`, `D-063`, `D-064`, `D-065`  
**Target Instruments:** Primary: `GBP/USD` (M15 / H1); Secondary: Forex Majors (`EUR/USD`, `USD/JPY`)

---

## 1. Core Market Philosophy & Market Maker Model

### 1.1 The Market Maker's Structural Role
The Forex market is an auction liquidity pool managed by institutional market makers / dealing desks whose primary mandate is to balance asymmetric order books, manage inventory risk, and capture spread. 

To fill large institutional positions without generating unfavorable self-slippage, the dealer must:
1. **Accumulate Inventory**: Range-bound price action during quiet sessions (Asian session) to build liquidity on both sides.
2. **Induce Off-Side Retail Positioning**: Produce sharp, deceptive momentum breakout moves ("vector candles") to trigger breakout orders and trap retail participants.
3. **Trigger Liquidity Pools (Stop Hunts)**: Extend price 25–50 pips outside structural consolidation ranges into the "Trading Zone" where stop-loss orders congregate.
4. **Shift the Trading Zone**: Rapidly reverse price in 25–50 pip increments, leaving off-side traders trapped.
5. **Expand Intraday/Multi-Day Trends**: Drive price across 3 levels of Average Daily Range (ADR) over 2–3 trading days.
6. **Distribute / Reset**: Re-accumulate or reverse at structural exhaustion points (Level 3 fanned EMAs / TDI extremes).

```
   [ 1. Accumulation ] ──> [ 2. Stop Hunt Induction ] ──> [ 3. Zone Shift ] ──> [ 4. 3-Level Expansion ] ──> [ 5. Reset / Reversal ]
    (Asian Box <=50p)       (Vector breakout candle)       (M/W Leg 2 rejection)   (L1 -> L2 -> L3 ADR)     (TDI Shark Fin + Re-test)
```

---

## 2. Temporal & Session Architecture

### 2.1 The New York (EST / EDT) Clock & Rollover
All market activity is referenced strictly to **New York Time** (Eastern Standard Time UTC-5 in winter, Eastern Daylight Time UTC-4 in summer per `X05 [29:46]`). Broker server time (GMT+0, GMT+2, GMT+3) must always be converted to NY Time.

```
05:00 PM EST ────────── 08:00 PM EST : Daily Rollover & Dead Gap (High/Low reset, Blue Tracer plotted)
08:00 PM EST ────────── 01:00 AM EST : Asian Accumulation Box (Ideal range <= 50 pips)
01:00 AM EST ────────── 02:00 AM EST : Pre-London Swing / Spread Expansion Window
02:00 AM EST ────────── 05:00 AM EST : London Stop Hunt & Zone Shift (Peak action: 03:30 - 03:45 AM EST)
05:00 AM EST ────────── 08:30 AM EST : London Continuation Move
08:30 AM EST ────────── 11:30 AM EST : New York Reversal / Continuation Window (Peak: 09:30 - 09:45 AM EST)
11:30 AM EST ────────── 05:00 PM EST : ADR Completion & Daily Consolidation
```

### 2.2 Session Range & Trading Zone Boundaries
1. **Asian Accumulation Box**:
   - Defined from **08:00 PM to 01:00 AM EST** (5 hours / 20 M15 candles).
   - **Range Filter Constraint**: $\text{Range}_{\text{Asian}} = \text{High}_{\text{Asian}} - \text{Low}_{\text{Asian}} \le 50.0\text{ pips}$.
   - If $\text{Range}_{\text{Asian}} > 50.0\text{ pips}$: The market has already expanded in Asia. Standard reversal setups are invalidated (`NO_TRADE` or evaluate last $1/3$ consolidation box only per `X08 [22:57]`).
2. **The Trading Zone (Stop Hunt Band)**:
   - **Upper Trading Zone**: $[\text{High}_{\text{Asian}} + 25.0\text{ pips},\;\text{High}_{\text{Asian}} + 50.0\text{ pips}]$.
   - **Lower Trading Zone**: $[\text{Low}_{\text{Asian}} - 50.0\text{ pips},\;\text{Low}_{\text{Asian}} - 25.0\text{ pips}]$.
   - Stop hunts that extend $< 25.0$ pips are generally insufficient to clear institutional books (`X10 [08:47]`).
3. **Blue Tracer (Prior-Period High/Low)**:
   - Defined as the horizontal marker of the **prior day's High and Low established at the 5:00 PM EST rollover** (`X13 [19:14]`, `X16 [36:21]`).
   - Acts as a high-probability liquidity hunt level for multi-session trap moves.

---

## 3. The Exponential Moving Average (EMA) Ecosystem

The canonical M15 EMA hierarchy is standardized under `D-043` and `D-061`:

| Period | Color | Colloquial Name | Primary Structural Role |
|---|---|---|---|
| **5 EMA** | **Yellow** | *Mustard* | Fast momentum tracker; crossover trigger line. |
| **13 EMA** | **Red** | *Ketchup* | Signal line. $5 \times 13$ cross confirms short-term momentum shift. |
| **50 EMA** | **Cyan / Aqua** | *Water* | Intraday trend filter & Level 1/2 boundary. 1st touch is high-probability bounce. |
| **200 EMA** | **White** | *Mayonnaise* | Multi-session baseline; institutional balance point; Level 2/3 boundary. |
| **800 EMA** | **Dark Blue** | *Blueberry* | Multi-day structural trend anchor / macro baseline. |

### Intraday Level Quantification by EMA Geometry (`X19 [22:27]`, `X11 [14:05]`):
- **Level 1**: Price breaks out from Peak Formation; 5/13 cross occurs, followed by 13/50 EMA cross; averages tighten and flatten.
- **Level 2**: Pullback to the 50 EMA ("Water") without breaking back into the Peak Formation; first touch to the 50 EMA produces continuation.
- **Level 3**: Price accelerates into exhaustion; EMAs fan out with maximum separation ($\Delta(\text{EMA}50 - \text{EMA}200) \gg \text{historical mean}$); price action becomes erratic and choppy, signaling upcoming Peak Formation reversal or multi-day reset.

---

## 4. Traders Dynamic Index (TDI) Specification

Under `D-063` and `D-065`, the TDI is calculated on M15 as follows:
- **RSI Price Line (Green)**: 21-period modulated RSI (smoothed 2-period SMA of RSI).
- **Trade Signal Line / TSL (Red)**: 7-period SMA of RSI Price Line.
- **Market Baseline / MBL (Yellow)**: 34-period SMA of RSI Price Line.
- **Volatility Bands (Blue)**: 34-period Bollinger Bands plotted at $\pm 2.0$ Standard Deviations from the **Market Baseline (MBL)**.
- **Reference Levels**: 68 (Overbought limit), 63 (High alert line), 50 (Market baseline equilibrium), 37 (Low alert line), 32 (Oversold limit).

### Canonical TDI Event Signals:
1. **Shark Fin**:
   - The Green RSI Price Line penetrates outside the Blue Volatility Band ($\ge 63$ or $\le 37$) and immediately hooks back inside the band (`X20 [20:21]`).
   - Represents a sharp liquidity stop hunt into extreme pricing followed by dealer rejection.
2. **Blood in the Water**:
   - The Green RSI Price Line crosses the Red Trade Signal Line (TSL) while returning from the extreme (`X20 [21:00]`).
   - Confirms that momentum has shifted in the direction of the reversal.

---

## 5. Signature Setup Taxonomy & Anatomies

### 5.1 The 9 Canonical Setups (V20 Slide `38:15` & X-Series)

```
        M-FORMATION (Top Reversal)                     W-FORMATION (Bottom Reversal)
                 Apex/Nadir                                      Apex/Nadir
                 /\       /\                                         \/
                /  \     /  \  <-- Leg 2 (30-45m)                   /  \     /\  <-- Leg 2 (30-45m)
     Leg 1 --> /    \   /    \                           Leg 1 --> /    \   /  \
              /      \_/      \                                   /      \_/    \
            Asian Box High                                      Asian Box Low
```

#### S1: M Formation (Bearish Top Reversal)
- **Context**: Forms at the high of the day/session, Asian High, Blue Tracer, or 200/800 EMA after an upward push.
- **Leg 1**: Vector candle breaking out of Asian Range / consolidation into the Upper Trading Zone (`X06 [00:52]`).
- **Apex**: Pullback toward 13 EMA / Asian range center.
- **Leg 2**: Second upward move re-testing the Leg 1 extreme. Leg 2 may fall slightly short or overshoot Leg 1 by up to 10 pips.
- **Time Cap & Close Rule**: Leg 2 must **close back below the Leg 1 high within 30 to 45 minutes** (2 to 3 M15 bars) (`X13 [24:18]`, `X17 [03:53]`).
- **Invalidation**: A full M15 candle body closing above the highest wick of Leg 1 (`X13 [29:46]`).

#### S2: W Formation (Bullish Bottom Reversal)
- **Context**: Direct mirror of the M Formation at session low / Lower Trading Zone (`X13 [32:14]`).
- **Time Cap & Close Rule**: Leg 2 must close back above the Leg 1 low within 30 to 45 minutes.
- **Invalidation**: A full M15 candle body closing below the lowest wick of Leg 1.

#### S3: Railroad Tracks (RR Reversal)
- **Definition**: Rapid 2-bar M15 reversal structure (30 minutes total: 15 min spike out, 15 min spike back) (`V20 [00:25:50]`, `X12 [34:42]`).
- **Geometry**: Bar 1 is an aggressive vector candle into the Trading Zone; Bar 2 is an opposing candle of equal or greater size ($\ge 70\%$ body match) closing back inside the range.

#### S4: Outside Structure
- **Definition**: A single-leg vector spike extending 25+ pips outside the Asian range that sets the HOD/LOD and immediately trades away without printing a distinct second leg (`X17 [03:25]`).

#### S5: Safety Trade (50 EMA Continuation Bounce)
- **Context**: Level 1 consolidation following a confirmed Peak Formation.
- **Trigger**: Pullback touches the 50 EMA ("Water") during London or NY session; price rejects the 50 EMA with a small M/W, hammer, or railroad track in the direction of the weekly trend (`V17`, `X10 [55:53]`).

#### S6: 22 Trade (Second Leg of a Second Leg)
- **Definition**: A micro M or W formation occurring on the second leg of a larger multi-session M/W structure at a repeated key level (`X06 [21:49]`).

#### S7: 33 Trade (Day 3 / Level 3 Climax)
- **Definition**: Trade occurring on Day 3 of the cycle following 3 completed intraday ADR pushes into structural exhaustion (`X07 [56:04]`).

#### S8: Half-A-Batman
- **Definition**: An asymmetrical setup where the market maker fills their full order book on the first spike and shifts the zone immediately without returning for a second leg (`X13 [16:36]`).

#### S9: Reset Pattern (Continuation Day)
- **Definition**: Price creates stop hunts to both the high and low of the day, but the daily candle closes near its open ($|\text{Close} - \text{Open}| \le 0.2 \times \text{ADR}$), resetting the intraday cycle and continuing the prior weekly trend (`Pt 2 Cycles L1 [20:08]`).

---

## 6. Execution, Timing & Risk Management Rules

### 6.1 Entry Timing Gate (`D-058`)
1. **Prerequisite**: Structural setup (M, W, RR, Safety Trade) confirmed at key liquidity level with TDI confluence.
2. **Timing Execution**: Entry is triggered on **the close of the M15 candle where the 5 EMA crosses the 13 EMA in the direction of the trade thesis**.

### 6.2 Stop Loss Placement (`D-055`, `X14 [43:19]`)
- **Primary Stop**: Set exactly **7 to 10 pips beyond the 2nd leg extreme** (or beyond the highest/lowest wick of the pattern).
- **Hard Maximum Stop**: Under no circumstances may a stop loss exceed **25.0 pips**. If structural invalidation requires $>25.0$ pips, the trade is rejected as poor risk-to-reward.

### 6.3 Take Profit & Exit Architecture (`D-055`, `X09 [10:52]`)
- **Take Profit 1 (TP1)**: +30.0 pips / touch of 50 EMA (close $50\%$ position, move stop to Break-Even).
- **Take Profit 2 (TP2)**: +50.0 pips / touch of 200 EMA / 3x ADR target (close remainder).
- **Time Stop**: If price fails to shift the zone and produce favorable momentum within **2.0 hours (8 M15 bars)**, close trade or tighten stop to breakeven (`X12 [30:33]`, `PT-018`).

### 6.4 Capital Risk Allocation (`V19 [00:58:20]`)
- Fixed **1.0% to 2.0% equity risk** per trade.
- Lot size is mathematically determined:
  $$\text{Lot Size} = \frac{\text{Account Equity} \times \text{Risk \%}}{\text{Stop Distance (pips)} \times \text{Pip Value}}$$
