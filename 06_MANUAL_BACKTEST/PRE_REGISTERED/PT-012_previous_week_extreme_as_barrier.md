# PT-012 — "They will not go below last week's peak formation": a barrier survival test

```text
STATUS:      NON-CONFORMING UNDER D-035 — SUPERSEDED BY PT-030, 2026-08-13.
             NEVER RUN. NOT EDITED INTO CONFORMANCE. RETAINED, NOT DELETED.

             WHY: this file pre-registered W-C (2013-01-06 -> 2017-12-29) as its window.
             D-035 pins the project-wide D-028 split at 2016-07-01 -- DEVELOPMENT
             2013-01-06 -> 2016-06-30, HOLDOUT 2016-07-01 -> 2017-12-29. W-C STRADDLES
             that boundary by 546 days, so 30% of this test's window lies in the
             holdout, which no session may open during the Student Phase (D-027, D-028).

             D-027 is explicit that changing a range creates a NEW TEST ID and that the
             abandoned test is retained and marked. COMMON_PROTOCOL.md 3a says the same
             and names the replacement window: W-C' = 2013-01-06 -> 2016-06-30. PT-030
             carries this test's question, four measures, three controls, seed, the
             directional conditioning and the C-001 handling (a curve, no day count)
             onto W-C', and declares as costs rather than as details everything the
             substitution changes:
               - data source: HistData GBP/USD M1 CSV corpus (D-036a), not TradingView
                 / FXCM (D-034). This test is unusually exposed, because its barrier IS
                 a price: barrier and quote come from the same file, so the comparison
                 is internally sound, but NO barrier price may be reconciled to any
                 FXCM-sourced level in the V02-V06 homework;
               - week open: 22:00 UTC (Sunday 17:00, fixed UTC-5, no DST), NOT 21:00 UTC
                 -- so "last week's extreme" is literally a different price;
               - breaches are BID-SIDE; the corpus carries no spread;
               - sample: 178 TRADING weeks x 2 barriers = 356, not the 518 implied in 3
                 below. This test loses TWO weeks to the data hole, not one: the week
                 of 2014-06-01 (the corpus is absent Sun 2014-06-01 17:00 -> Mon
                 2014-06-02 15:01, ~22 hours, so there is no week open to start the
                 survival clock) AND the week of 2014-06-08, whose BARRIER is the holed
                 week's high and low -- a systematically too-narrow barrier that would
                 look easier to breach. The second exclusion is not reported by any QA
                 check; it follows from this test's one-week lag and had to be derived.
                 Surfaced by QA check C8, which was ADDED AFTER PT-030 was drafted.
                 (Superseded first-draft figure, retained: 180 tested weeks x 2 = 360.)

             --- the superseded line, as first written ---
               - sample: 180 tested weeks x 2 barriers = 360, not the 518 implied in 3
                 below, because the test spends one week to the previous-week lag and
                 the corpus's opening fragment is a Tue-Fri partial, not a week.

             THIS FILE HAS NEVER BEEN RUN AND MUST NOT BE RUN.
             NOTHING IN THIS FILE WAS CHANGED except this status block.

--- original status block, as pre-registered 2026-08-12, unchanged ---
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V02 [00:15:40]–[00:15:52], [00:25:21]–[00:25:35]
BLOCKERS:   I-007 · D-028 boundary dates unpinned
RELATION:   Informs C-001. ADOPTS NO DAY COUNT — see §3a. This is the point of the design.
ATTESTATION: No chart in W-C was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

V02 states an **absolute** barrier claim, with a stated mechanism:

> *"Next week, they want to start the week and drop again, but here's the deal. **They will
> not go below last week's peak formation.**"* `[00:15:40]`
> *"Because they will release the traders that were jammed up from their actions last week.
> They're not in the business of letting go with the money."* `[00:15:52]`
> *"He can't come back above the low of the previous week because it releases the traders
> back into profit."* `[00:25:21]`

Two things make this unusually testable. First, the barrier is **the previous week's
extreme** — fully known at the start of the current week, requiring no future data and no
blocked definition. Second, the claim is stated **absolutely** (`V02_SOURCE_NOTES.md` §6
condition 6: *"Absolute as stated"*), and absolute claims are refuted by a single
counter-example — so the honest measurement is a **rate and a survival curve**, not a
yes/no.

`V02_INTERPRETATION.md` `G10` records the deeper problem this test fixes: the claim is
*"Unfalsifiable as presented"* because the lesson shows no case where the dealer did cross.
**This test supplies the missing denominator.**

### 1a. The concession that must be measured with it

Ten seconds of the same lesson also says *"possibly using it as a higher low of the current
week"* `[00:14:54]`, and V01/V02 elsewhere describe the level being *approached* to within
*"three to five pips"* `[00:26:48]`. So a near-touch is expected doctrine and a clean break
is not. The test therefore measures **distance to the barrier** as well as breach, and
reports the near-miss distribution, which is where the interesting number probably lives.

---

## 2. THE QUESTION

> In how many GBP/USD weeks does price trade beyond the previous week's extreme, how soon,
> and how close does it come when it does not?

Null hypothesis: **the previous week's extreme is an ordinary price.** It is crossed at the
rate any equivalently-distant reference level is crossed.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| Window | **W-C** — 2013-01-06 → 2017-12-29 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| Barrier | Previous week's high and previous week's low, both carried forward. Known at week open; **no future data** |
| Measure 1 — **survival** | Hours from week open until first trade beyond the barrier, as a survival curve, censored at week close |
| Measure 2 — **breach rate** | Share of weeks breaching each barrier at all |
| Measure 3 — **approach** | Minimum distance to the un-breached barrier, in pips; the near-miss distribution (§1a) |
| Measure 4 — **breach depth** | For breaches, maximum excursion beyond, in pips — a 2-pip poke and a 90-pip break are not the same event |
| Directional conditioning | Reported separately for the barrier the week's net direction runs **toward** vs **away from** |
| Decision point | Week open. Everything after is outcome |
| Sample | ~260 weeks × 2 barriers. ≥ 30 satisfied |

### 3a. `C-001` — why this test reports a curve and adopts no number

`C-001` is the project's foundational open contradiction: *"for sure two and a half to
three days"* (V01 `[00:35:05]`), *"likely… four days, three and a half days, three days"*
(V01 `[00:35:15]`), *"at least three days"* (V02 `[00:16:15]`), the printed *"For At Least
3 Days"* (V02 slide), and V04 `[00:20:28]` restating 2.5–3. `D-030` forbids picking one.

**A survival curve requires no choice.** It reports the whole distribution of time-to-breach
and lets every stated value be read off it — including the possibility that none of them
matches. That is the maximum this project can honestly do with `C-001` today, and it is
strictly more than testing any single value would give.

**No session may read a modal survival time off this curve and record it as resolving
`C-001`.** The contradiction is about what the instructor *said*; this measures what price
*did*.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | The same measures against a **sham barrier** placed at the same distance from the week's open as the real one, but in a random direction/offset, 1,000 draws, seed `20260812`. Holds distance constant and varies only *whether the level is last week's extreme* |
| **Second** | **N3 — week-anchor shift**, 1,000 draws: the "previous week's extreme" computed on shifted week boundaries |
| **Third** | Random reference weeks: last week's extreme taken from a **different, randomly chosen** week, scaled to the same distance |

The first arm is the whole test. Distance to a barrier dominates the breach rate — a
barrier 200 pips away survives longer than one 20 pips away for reasons that have nothing
to do with market makers. Any comparison that does not hold distance constant measures
volatility and reports it as doctrine.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Real barriers survive longer than distance-matched sham barriers | Support for a real level effect. The strongest weekly-scale result available from V02 |
| Identical survival | **The previous week's extreme is an ordinary price at this sample.** Report prominently — it would undercut the mechanism V02 states three times |
| Breach rate high but breach depth tiny | The "spread to reach a little higher" reading (V02 `[00:24:51]`) becomes the live one. Report depth alongside rate always; a rate alone is misleading here |
| Asymmetry between the toward/away barriers | Expected, and reported as a conditioning finding rather than folded into one number |

## 6. MANDATORY SCOPE STATEMENT

> PT-012 tests whether the previous week's extreme acts as a barrier on GBP/USD. It is
> **not** a test of "peak formation" (`A-010`) — the previous week's extreme is a
> measurement, and whether the instructor's peak formation coincides with it is undefined
> and untested here. **It resolves nothing in `C-001`** and adopts no day count. It is not
> a trading test: no entry, stop or target is involved.

## 7. TO RUN THIS

1. Close `I-007`; record the feed's week-open timestamp; confirm W-C is DEVELOPMENT.
2. Harvest with timestamps from DOM text only.
3. Build the distance-matched sham-barrier control **before** computing the real survival
   curve.
4. Report the five largest-range weeks as the pre-registered sensitivity appendix.
5. Write `BT_V02_NNNN.md` from the template, §0 referencing this file. Record the survival
   curve against `C-001` as **evidence about price, not about the source**.
