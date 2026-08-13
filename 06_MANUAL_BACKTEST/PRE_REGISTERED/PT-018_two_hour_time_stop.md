# PT-018 — The two-hour time stop: is "not in profit yet" predictive?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 printed slide [00:33:10]; spoken [00:34:23], [00:34:39]
BLOCKERS:   I-007 · D-028 unpinned · A-007 blocks the true entry — proxy declared in §6
ATTESTATION: No chart in W-B was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

The slide prints a parameter the audio never states — *"If Trade Does Not See Substantial
Profit **In 2 Hours**, Take Profit Or Small Loss"* `[00:33:10]` — which
`V02_INTERPRETATION.md` §10.2 U1 calls *"the single most useful number the visuals added"*.
The audio supplies the threshold and the tone:

> *"**The time clock is not negotiable.** If the trade doesn't move into substantial profit
> — 25, 30, 40 pips — then out. Scratch out."* `[00:34:23]`

Together they form a **complete, numeric, falsifiable management rule**: a position not
showing 25–40 pips within 2 hours should be closed. And unlike almost everything else in
the corpus, both halves are stated — the window *and* the threshold.

The claim underneath is testable and interesting on its own: **is early progress predictive
of eventual outcome?** If positions that are flat at 2 hours go on to do as well as
positions that are 30 pips up at 2 hours, the time stop is costing money rather than saving
it — and that would be a real finding about a rule the instructor calls non-negotiable.

---

## 2. THE QUESTION

> Conditional on a mechanical entry, does *"not in substantial profit at 2 hours"* predict
> a worse eventual outcome than the unconditional population?

Null hypothesis: **it does not.** Early progress carries no information about the eventual
result, and the time stop merely truncates outcomes at random.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| Entry (proxy) | The `PT-001`/`PT-017` location trigger: first close 25–50 pips beyond the Asian range, direction away from the box |
| Stop / target | 18 / 50 pips (V04 `[00:04:43]`, `[00:05:07]`) — the instructor's numbers, not fitted |
| **Classifier at T+2h** | `PROGRESSED` if unrealised P&L ≥ **+25 pips**; `STALLED` otherwise. The 25-pip cut is the **lowest** of the instructor's three (25/30/40), pre-registered; the other two are reported as pre-registered sensitivities |
| Measure 1 | Eventual outcome (target hit / stop hit / open at session end) by class |
| Measure 2 | **Counterfactual comparison**: expectancy of *closing every `STALLED` position at T+2h* versus *letting it run to stop or target*. This is the rule's actual value in pips |
| Measure 3 | Second-leg clock reset — *"If you see a second leg, restart the clock"* `[00:34:51]` — **NOT MODELLED.** `A-007` is undefined; the omission is recorded in every report of this test |
| Measure 4 | The same classification at T+1h and T+3h, so "2 hours" is ranked rather than assumed |
| Sample | Trigger-dependent; `PT-014` predicts it. ≥ 30 required per class |

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry**, classified identically at T+2h. Establishes the base rate at which *any* position that is flat at 2 hours goes on to lose. **This is the comparison that decides whether the rule adds anything** |
| **Second — the natural control** | The unconditional trigger population: what happens if the time stop is never applied |
| **Third** | Time-in-trade control: positions are open for different durations by construction, so expectancy is also reported **per hour of exposure**, not only per trade |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| `STALLED` positions do materially worse, and closing them improves expectancy | The time stop earns its place. **The clearest actionable instruction in V02 gains support** — and it would be the first management rule in this project with any |
| `STALLED` and `PROGRESSED` end alike | The time stop truncates at random; it costs the spread and gains nothing. Report prominently — a rule described as *"not negotiable"* failing is exactly what `E25` protects |
| Closing `STALLED` positions **improves** the win rate but **reduces** total expectancy | The classic time-stop result, and the most likely one. Report both figures; a win-rate improvement alone is the kind of number that gets quoted out of context |
| T+1h or T+3h beats T+2h | Report the ranking and adopt nothing. The printed number is the instructor's; a better cut found here is this session's, and `D-010` keeps it out of the spec |

## 6. MANDATORY SCOPE STATEMENT

> PT-018 tests a **management** rule on a **proxy entry**. The instructor's rule applies to
> his own entry (second-leg close, `A-007`; TDI, `A-039`), and the second-leg clock reset at
> `[00:34:51]` is **not modelled at all** because the term is undefined — so this test
> measures a *stricter* rule than the one taught, and the difference favours finding the
> time stop worse than it is. That direction of bias is stated here so the result can be
> read with it.

## 7. TO RUN THIS

1. Close `I-007`; confirm W-B is DEVELOPMENT; run `PT-014`, then `PT-017` (whose
   time-to-profit curve makes this test's classifier interpretable).
2. Harvest with timestamps from DOM text only.
3. Compute the N1 classification base rate **before** looking at the trigger population's.
4. Report measure 2 in pips of expectancy, never as a win-rate delta alone.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file.
