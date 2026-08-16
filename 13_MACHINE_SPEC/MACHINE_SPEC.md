# MACHINE SPECIFICATION (MMM-MACHINE-V1.0)

**Document ID:** `13_MACHINE_SPEC/MACHINE_SPEC.md`  
**Classification:** Formal Mathematical & Algorithmic Specification  
**Target Engine:** Multimodal Intelligence Layer & Deterministic Pre-Processor  
**Companion File:** `12_MASTER_SPEC/CANONICAL_SPEC.md`

---

## 1. Mathematical Formulas & Indicator Definitions

### 1.1 Exponential Moving Averages (EMA)
Given a series of bar close prices $\{C_t\}_{t=1}^N$ and smoothing period $K \in \{5, 13, 50, 200, 800\}$:
$$\alpha = \frac{2}{K + 1}$$
$$\text{EMA}_t(K) = \alpha \cdot C_t + (1 - \alpha) \cdot \text{EMA}_{t-1}(K)$$
with seed $\text{EMA}_K(K) = \frac{1}{K}\sum_{i=1}^K C_i$.

### 1.2 Traders Dynamic Index (TDI) Mathematical Series
Let $R_t = \text{RSI}(C_t, 21)$ over 21 periods.
1. **RSI Price Line (Green Line)**:
   $$\text{PL}_t = \text{SMA}(R_t, 2) = \frac{R_t + R_{t-1}}{2}$$
2. **Trade Signal Line / TSL (Red Line)**:
   $$\text{TSL}_t = \text{SMA}(\text{PL}_t, 7) = \frac{1}{7}\sum_{i=0}^6 \text{PL}_{t-i}$$
3. **Market Baseline / MBL (Yellow Line)**:
   $$\text{MBL}_t = \text{SMA}(\text{PL}_t, 34) = \frac{1}{34}\sum_{i=0}^{33} \text{PL}_{t-i}$$
4. **Volatility Bands (Blue Lines)**:
   $$\sigma_t = \sqrt{\frac{1}{34}\sum_{i=0}^{33} (\text{PL}_{t-i} - \text{MBL}_t)^2}$$
   $$\text{VB}_{\text{Upper}, t} = \text{MBL}_t + 2.0 \cdot \sigma_t$$
   $$\text{VB}_{\text{Lower}, t} = \text{MBL}_t - 2.0 \cdot \sigma_t$$

### 1.3 Average Daily Range (ADR)
Let $H_{d}, L_{d}$ be the High and Low of day $d$:
$$\text{Range}_d = H_d - L_d$$
$$\text{ADR}_{14} = \frac{1}{14}\sum_{i=1}^{14} \text{Range}_{d-i}$$
$$\text{ADR\% Used}_t = \frac{H_{\text{today}, t} - L_{\text{today}, t}}{\text{ADR}_{14}} \times 100\%$$

---

## 2. Prospective Finite State Machine (FSM)

To eliminate lookahead bias and ensure the agent reasons as candles unfold in real-time, the market cycle is modeled as a formal deterministic state machine:

```
                  ┌────────────────────────────────────────────────────────┐
                  │                      S0: ACCUMULATING                  │
                  │             (Asian Session Box forming <= 50 pips)     │
                  └──────────────────────────┬─────────────────────────────┘
                                             │
                       Asian Session Ends (01:00 AM EST) &
                       Vector Candle exits Asian Box (+25 pips)
                                             │
                                             ▼
                  ┌────────────────────────────────────────────────────────┐
                  │                  S1: VECTOR_INDUCTION                  │
                  │             (Speed >= 12 pips in <= 2 M15 bars)        │
                  └──────────────────────────┬─────────────────────────────┘
                                             │
                       Peak High/Low printed; Pullback toward 13 EMA
                                             │
                                             ▼
                  ┌────────────────────────────────────────────────────────┐
                  │                    S2: LEG1_ESTABLISHED                │
                  │           (Candidate Peak Formation High / Low)        │
                  └──────────────────────────┬─────────────────────────────┘
                                             │
                       Price returns to re-test Leg 1 extreme
                                             │
                                             ▼
                  ┌────────────────────────────────────────────────────────┐
                  │                    S3: LEG2_TESTING                    │
                  │        (Agent Status: WATCH — Pattern Forming)         │
                  └──────────────┬──────────────────────────┬──────────────┘
                                 │                          │
           Leg 2 closes back     │                          │ Candle body closes beyond
           within 30-45 mins     │                          │ Leg 1 by > 10 pips
           & TDI Shark Fin       │                          │
                                 ▼                          ▼
      ┌────────────────────────────────────┐      ┌─────────────────────────┐
      │        S4: LOCKED_PEAK_FORMATION   │      │     S_INV: INVALIDATED   │
      │    (Confirmed M or W Structure)    │      │   (Trend Breakout Trap) │
      └──────────────────┬─────────────────┘      └─────────────────────────┘
                         │
      5/13 M15 EMA Cross │
      in setup direction │
                         ▼
      ┌────────────────────────────────────┐
      │          S5: TRADE_CONFIRMED       │
      │   (Agent Status: TRADE — Enter)    │
      └──────────────────┬─────────────────┘
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
┌───────────────────────────────┐ ┌───────────────────────────────┐
│       S6: TP1_HIT (+30 pips)  │ │      S_STOP: STOPPED_OUT      │
│ (Close 50%, Trail to BE)      │ │   (Exit at -7 to -10 pips)    │
└───────────────┬───────────────┘ └───────────────────────────────┘
                │
                ▼
┌───────────────────────────────┐
│       S7: TP2_HIT (+50 pips)  │
│     (Full Cycle Complete)     │
└───────────────────────────────┘
```

---

## 3. Quantitative Error Bounds & Calibration Rubric

| Parameter | Permissible Tolerance Bound | Consequence if Exceeded |
|---|---|---|
| **Asian Box Range** | $0.0 \le \text{Range} \le 50.0\text{ pips}$ | If $>50.0\text{ pips}$, classify `NO_TRADE` (Blown Box). |
| **Trading Zone Hunt** | $25.0 \le \text{Excursion} \le 75.0\text{ pips}$ | If $<25.0\text{ pips}$, classify `WEAK_HUNT` (`WATCH`). |
| **Leg 2 Overshoot** | $\Delta_{\text{Leg2-Leg1}} \le 10.0\text{ pips}$ (wick only) | If body closes beyond or overshoot $>10\text{p}$, classify `INVALIDATED`. |
| **Leg 2 Time Duration** | $2 \le \text{Bars} \le 3\text{ M15 bars}\;(30–45\text{ mins})$ | If $>3\text{ bars}$ without close-back, classify `INVALIDATED`. |
| **Stop Loss Distance** | $7.0 \le \text{SL} \le 25.0\text{ pips}$ | If $>25.0\text{ pips}$, reject trade (Risk/Reward violation). |
| **Take Profit 1** | Fixed at $+30.0\text{ pips} \pm 2\text{p}$ | Enforce $R:R \ge 1.5$ on first partial. |
| **Take Profit 2** | Fixed at $+50.0\text{ pips} \pm 5\text{p}$ | Enforce $R:R \ge 2.5$ on runner. |

---

## 4. Multi-Condition Confluence Scoring Algorithm

The AI Market-Reading Agent calculates a composite **Confluence Confidence Score** $S \in [0, 100]$:

$$S = w_{\text{pattern}} + w_{\text{session}} + w_{\text{tdi}} + w_{\text{ema}} + w_{\text{liquidity}}$$

Where each component is scored from 0 to 20 points:
1. **$w_{\text{pattern}}$ (Pattern Geometry)**:
   - 20: Clean 2-leg M/W with Leg 2 closing back in 2–3 bars, or textbook Railroad Tracks.
   - 10: Leg 2 developing or slightly sloppy wick.
   - 0: No recognizable pattern or broken geometry.
2. **$w_{\text{session}}$ (Timing Window)**:
   - 20: Peak London Open (03:00–04:00 AM EST) or NY Reversal (09:00–10:00 AM EST).
   - 10: Active session but off-peak (e.g. 05:00 AM EST).
   - 0: Asian session, Dead gap (05:00–08:00 PM EST), or Friday afternoon.
3. **$w_{\text{tdi}}$ (TDI Confluence)**:
   - 20: Shark Fin (outside band) + Blood in the Water (TSL cross) in extreme zone ($>63$ or $<37$).
   - 10: RSI bounce off 50 Market Baseline or partial hook.
   - 0: Flat, middle-of-band RSI with no direction.
4. **$w_{\text{ema}}$ (EMA Alignment & Levels)**:
   - 20: Reaction at 50 EMA (Safety) or 200 EMA (Mayo) + 5/13 cross confirmation.
   - 10: 5/13 cross without major EMA confluence.
   - 0: Trapped inside tangled EMAs.
5. **$w_{\text{liquidity}}$ (Liquidity Hunt & ADR Exhaustion)**:
   - 20: Price in Trading Zone (25–50p outside Asian box) or testing Blue Tracer + ADR $\ge 70\%$.
   - 10: Price outside Asian box but $<25$ pips extension.
   - 0: Inside Asian box or middle of daily range.

### Disposition Mapping:
- **$S \ge 80$**: Disposition = `TRADE` (High-confidence setup).
- **$50 \le S \le 79$**: Disposition = `WATCH` (Developing setup, awaiting confirmation).
- **$S < 50$**: Disposition = `NO_TRADE` (Stand aside; insufficient edge).
