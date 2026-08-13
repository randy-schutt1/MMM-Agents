# PT-030 — "They will not go below last week's peak formation": a barrier survival test (RE-ISSUE of PT-012)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-012, which is NON-CONFORMING under D-035 (its window W-C straddles the
             pinned DEVELOPMENT/HOLDOUT boundary by 546 days). PT-012 is RETAINED, NOT
             DELETED, NEVER RUN, and is not edited into conformance — only its status
             block is added, per D-027 and the PT-022 precedent.
LESSON:      V02 [00:15:40]-[00:15:52], [00:25:21]-[00:25:35]
RELATION:    Informs C-001. ADOPTS NO DAY COUNT — see 3c. This is the point of the design.
ATTESTATION: No chart, no price series and no outcome data of any kind — in W-C′ or in
             any other window — was opened, loaded, parsed or inspected by the session
             that wrote this file. The HistData corpus was cited from its committed
             provenance (SHA256SUMS.txt) and its QA report; not one quote was read from
             it. The D-035 holdout (2016-07-01 → 2017-12-29) was not opened, and per
             D-036a it is not on disk.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.
Decisions: `D-007` · `D-026`/`D-029` · `D-027`/`D-028` · **`D-030`** · **`D-031`** ·
`D-034` → **`D-036`/`D-036a`** · **`D-035`**.

---

## 0. WHY THIS FILE EXISTS, AND WHAT THE SUBSTITUTIONS COST

`D-035` pins **DEVELOPMENT = 2013-01-06 → 2016-06-30**, **HOLDOUT = 2016-07-01 → 2017-12-29**.
`PT-012`'s window `W-C` runs to 2017-12-29 and **straddles the boundary by 546 days**.
`COMMON_PROTOCOL.md` §3a and `D-027` require re-issue under a new `PT` number; the original is
**retained and marked, never edited**.

| Field | `PT-012` | **PT-030** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 complete weeks → **181**; this test spends one to the lag and **two more to the 2014-06-01 data hole and its heir** — **n = 178 tested weeks**, §3a″/§3b |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | **levels no longer comparable**; **bid-only, no spread** — §0b |
| **Week open** | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | the barrier is computed over a **one-hour-shifted week**, so *"last week's extreme"* is literally a different price |
| Everything else | — | **unchanged** — question, four measures, controls, seed, `C-001` handling, scope | — |

### 0a. Three losses that are not negotiable

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   offset cannot be measured here. **Levels are not comparable with the V02–V06 FXCM homework;
   only shape and distance claims travel** (`D-036a`). **This test is unusually exposed to
   that**: its barrier *is* a price. **The barrier and the quote it is tested against come from
   the same file**, so the comparison is internally sound — but **no barrier price from this
   test may be compared with, plotted against, or reconciled to any FXCM-sourced level in the
   V02–V06 homework.** The **distances** (Measures 3 and 4, in pips) travel; the levels do not.
2. **The October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase at all.**
   For a barrier-breach test this removes the single most extreme breach candidate in the era.
   That is a **property of the sample** and is stated in the report, not discovered in review.
3. **The EU referendum week (2016-06-23) is inside `W-C′` and inside DEVELOPMENT**, one week
   before the boundary. **Not excluded** (`E09`). Stated now that it is very likely to appear in
   the sensitivity appendix and to sit in the tail of Measure 4.

### 0b. Two vendor properties that constrain what may be claimed

- **Bid-only bars, no spread** (`D-036a`). A "breach" here is a **bid** trading beyond the
  barrier. A real fill would face the spread on one side. The measure is therefore a **bid-side
  breach**, labelled as such, and no execution claim is derived from it. Inventing a spread
  would be `D-030`'s exact prohibition.
- **Volume is structurally zero** in this vendor's data and **no measure in this test reads
  it**.

---

## 1. WHY THIS TEST IS WORTH RUNNING

V02 states an **absolute** barrier claim, with a stated mechanism:

> *"Next week, they want to start the week and drop again, but here's the deal. **They will not
> go below last week's peak formation.**"* `[00:15:40]`
> *"Because they will release the traders that were jammed up from their actions last week.
> They're not in the business of letting go with the money."* `[00:15:52]`
> *"He can't come back above the low of the previous week because it releases the traders back
> into profit."* `[00:25:21]`

Two things make this unusually testable. First, the barrier is **the previous week's extreme** —
fully known at the start of the current week, requiring no future data and no blocked
definition. Second, the claim is stated **absolutely** (`V02_SOURCE_NOTES.md` §6 condition 6:
*"Absolute as stated"*), and absolute claims are refuted by a single counter-example — so the
honest measurement is a **rate and a survival curve**, not a yes/no.

`V02_INTERPRETATION.md` `G10` records the deeper problem this test fixes: the claim is
*"Unfalsifiable as presented"* because the lesson shows no case where the dealer did cross.
**This test supplies the missing denominator.**

### 1a. The concession that must be measured with it

Ten seconds of the same lesson also says *"possibly using it as a higher low of the current
week"* `[00:14:54]`, and V01/V02 elsewhere describe the level being *approached* to within
*"three to five pips"* `[00:26:48]`. So a near-touch is expected doctrine and a clean break is
not. The test therefore measures **distance to the barrier** as well as breach, and reports the
near-miss distribution, which is where the interesting number probably lives.

---

## 2. THE QUESTION

> In how many GBP/USD weeks does price trade beyond the previous week's extreme, how soon, and
> how close does it come when it does not?

Null hypothesis: **the previous week's extreme is an ordinary price.** It is crossed at the rate
any equivalently-distant reference level is crossed.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block (data split)** | **DEVELOPMENT, confirmed.** `W-C′` **is** `D-035`'s DEVELOPMENT block |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 in `raw/SHA256SUMS.txt`; aggregated by `scripts/aggregate_m15.py` per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST** (`D-036a`, QA `C7`). **NOT FXCM's 21:00 UTC.** Both the barrier week and the tested week are delimited by this open |
| **Data-QA gate** | **Precondition.** `scripts/qa_histdata_m1.py`; `QA_REPORT.txt`; `C1`–`C4` PASS, `C5`–`C8` signed off in `D-036a`. Cited in the observation |
| Measurement rule | `E06` restated for a CSV corpus (`COMMON_PROTOCOL.md` §2) |
| Timezone | **Both `D-031` arms.** Arm A = corpus stamps verbatim; Arm B = +1h during US DST |
| Barrier | **Previous week's high and previous week's low, both carried forward.** Known at week open; **no future data** |
| Measure 1 — **survival** | Hours from week open until first trade beyond the barrier, as a **survival curve, censored at week close** |
| Measure 2 — **breach rate** | Share of weeks breaching each barrier at all |
| Measure 3 — **approach** | Minimum distance to the un-breached barrier, in pips; the near-miss distribution (§1a) |
| Measure 4 — **breach depth** | For breaches, maximum excursion beyond, in pips — **a 2-pip poke and a 90-pip break are not the same event** |
| Directional conditioning | Reported separately for the barrier the week's net direction runs **toward** vs **away from** |
| Decision point | **Week open.** Everything after is outcome |
| Excluded weeks | **None**, except the structural exclusion in §3a, which is a data-boundary fact rather than a judgement |
| **Sample** | **178 TRADING weeks × 2 barriers = 356 barrier observations** — denominated in **trading weeks present with an observable week open and a clean predecessor**, not calendar weeks. See §3a, §3a′, §3a″ and §3b |

### 3a. The one structural exclusion, and why it is not a discretionary one

This test needs a **complete previous week** for every tested week.

- The first week in `W-C′` opens **2013-01-06**. Its predecessor is the corpus's opening
  fragment — the corpus begins **2013-01-01 17:00**, a **Tuesday**, so that "week" is a
  **Tue→Fri partial** and its high/low are not a week's high/low. **The week of 2013-01-06 is
  therefore excluded as a tested week and counted as excluded.** It is still available *as* a
  barrier week for 2013-01-13.
- The final week-open in `W-C′`, **2016-06-26**, is **truncated by the DEVELOPMENT boundary**
  (no Friday). It cannot be a tested week (its survival curve would be censored early for a
  reason that has nothing to do with the market) and it cannot be a barrier week (its extreme is
  a partial-week extreme). **Excluded and counted.**

**Both exclusions are mechanical, fixed here, and reported as counts.** Neither is a judgement
about a week's character, which would be `E09`.

### 3a′. THE WEEK CENSUS — CALENDAR WEEKS ARE NOT TRADING WEEKS

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong.** Against the corpus's own census (QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| **Calendar-complete weeks WITH an observable Sunday open** | **180** | 181 complete weeks, less the **2014-06-01** data hole |

**Two facts a naive reading of `C7` gets backwards:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** looks like a week open.
   `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` sit **inside** weeks
   that opened normally on Sunday. **A run session taking week boundaries from `C7` would invent
   extra "previous week" extremes out of half-weeks and restart the survival clock mid-week.**
   Pre-registered: **a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open
   is never a week boundary.**
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** Zero bars
   for `2014-06-01 Sun` (nominal ~420), **521 of 1,440** for `2014-06-02 Mon`: **~22 continuous
   hours missing**. `C8` marks it `*** ABSENT AND UNEXPLAINED ***`.

### 3a″. `C8` DISPOSITIONS — PRE-REGISTERED, BY NAME. THIS TEST LOSES **TWO** WEEKS, NOT ONE

Eleven `C8`-flagged sessions fall into **seven weeks** inside `W-C′`. The disposition is **not
uniform**, and this test is the only one in the batch where the data hole costs a second week:

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition for this test** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0) | market closure | **INCLUDE, report separately** |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE, report separately** |
| **2014-06-01** | **Sun (0), Mon (521)** | **DATA DEFECT** | **EXCLUDE AS A TESTED WEEK** — no observable week open, so no survival clock |
| **2014-06-08** | *(none — the week itself is clean)* | **INHERITS THE DEFECT** | **EXCLUDE AS A TESTED WEEK** — its barrier **is** the 2014-06-01 week's high and low, drawn from a week missing 22 hours |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE, report separately** |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE, report separately** |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE, report separately** — **week ends Thursday**, so the survival curve is **censored at ~96 h, not ~120 h**; record the realised censoring time |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE, report separately** — **week ends Thursday** |

*(The eleventh flagged session, `2013-01-01 Tue`, is the corpus's opening fragment; §3a already
excludes the week it would serve.)*

**The 2014-06-08 exclusion is the one a careless run would miss.** That week's own data is
clean, so nothing flags it. But this test's barrier is *last week's extreme*, and last week is
the holed one: a high and a low computed over a week missing its entire Sunday and 15 hours of
Monday is a **biased barrier — systematically too narrow**, which would make it look easier to
breach. **Excluded by name, counted, and reported.**

**Why the six holiday weeks are INCLUDED.** `PT-012` inherited *"Excluded weeks: None"* from the
batch and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation for being
unrepresentative (`E09`). A holiday closure is **market structure**, and a barrier that survives
a four-day week is a real observation. **Re-deciding this after a QA check surfaced them would be
the suit-the-result choice the gate exists to prevent.** The two Thursday-ending weeks shorten
the censoring horizon and are reported separately with their realised censoring time — which
matters here more than anywhere, because §3c reads a **survival curve** off this test.

**Why 2014-06-01 is EXCLUDED, and why that is not `E09`.** `E09` forbids excluding an
observation for **what the market did**. This is excluded because **the corpus does not contain
what the market did**: the survival clock starts at the week open, and there is no week open.
**Mechanical, by name, counted.**

### 3b. The sample, computed honestly

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar span, inclusive | 1,819 days | **1,272 days** |
| Calendar Sundays | 260 | **182** |
| Calendar-complete Sun→Fri weeks | 260 | **181** |
| Tested weeks after the §3a lag exclusions | 259 | **180** |
| **Tested weeks after §3a″ (the data hole and its heir)** | 259 | **178** |
| **Barrier observations (× 2)** | 518 | **356** |

**`n = 178` tested weeks and `n = 356` barrier observations clear
`BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 comfortably. The headline breach rates and
the survival curve are not marginal.** The `n` is denominated in **trading weeks present in the
corpus with an observable week open and a clean predecessor**, never in calendar weeks.

**Where it thins, pre-registered rather than discovered:**

- **Measure 3 (the near-miss distribution) is computed only on UN-BREACHED barriers**, and
  **Measure 4 only on BREACHED ones**. These two subsets partition 356 observations, and neither
  size is knowable before the run. **If either subset falls under 30, every figure from it
  carries `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` in the same sentence**
  (`COMMON_PROTOCOL.md` §9.4). Given that V02 states the barrier holds *absolutely*, the
  **breached** subset is the one at risk if the claim is strong, and the **un-breached** subset
  is the one at risk if it is weak — so the caveat is stated for both and neither can be
  dropped after seeing which way it went.
- **The directional conditioning halves whatever survives**: toward-barrier and away-barrier are
  reported separately, at ~178 each before the breach/no-breach split, and the four-way cell
  (direction × breach status) is where §4.1's floor will bite first. **Report the four cell
  counts in the same table as the four cell rates.**
- The original claimed *"~260 weeks × 2 barriers. ≥ 30 satisfied"*. **That is now 178 × 2, and
  the sub-cell caveats above are new — a consequence of an honest window and an honest corpus,
  not of a weaker test.**

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN.** The session-completeness check was
> added to `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was
> drafted, and it is what surfaced the 2014-06-01 hole — which `C6` had excluded by
> construction (it skips anything ≥ 12 h as "the weekend") and `C7` had rendered cosmetic (it
> surfaced as a decorative **Monday** entry in a weekday tally). §3a′, §3a″ and the corrected
> counts in §3b are the **correction that check forced**, made **before any bar in `W-C′` was
> read**. The **2014-06-08** exclusion in particular is a consequence `C8` does not itself
> report — it follows from this test's one-week lag and had to be derived.

### 3c. `C-001` — why this test reports a curve and adopts no number

`C-001` is the project's foundational open contradiction: *"for sure two and a half to three
days"* (V01 `[00:35:05]`), *"likely… four days, three and a half days, three days"* (V01
`[00:35:15]`), *"at least three days"* (V02 `[00:16:15]`), the printed *"For At Least 3 Days"*
(V02 slide), and V04 `[00:20:28]` restating 2.5–3. `D-030` forbids picking one.

**A survival curve requires no choice.** It reports the whole distribution of time-to-breach and
lets every stated value be read off it — including the possibility that none of them matches.
That is the maximum this project can honestly do with `C-001` today, and it is strictly more
than testing any single value would give.

**No session may read a modal survival time off this curve and record it as resolving `C-001`.**
The contradiction is about what the instructor *said*; this measures what price *did*.

**One arithmetic note the shortened window forces:** the survival curve is censored at the
**week close**, so it can only speak about the first **≈120 hours** (Sunday 17:00 → Friday
17:00). Every day-count in `C-001` lies inside that span, so the curve still covers all of them
— **but the censoring is at 120 hours, not 168**, and any reading of "three days" must be taken
against a 5-day trading week, not a 7-day calendar one.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | The same measures against a **sham barrier** placed at the **same distance** from the week's open as the real one, but in a random direction/offset, 1,000 draws, seed `20260812`. Holds distance constant and varies only *whether the level is last week's extreme* |
| **Second** | **N3 — week-anchor shift**, 1,000 draws: the "previous week's extreme" computed on **shifted** week boundaries |
| **Third** | Random reference weeks: last week's extreme taken from a **different, randomly chosen** week, scaled to the same distance |

The first arm is the whole test. **Distance to a barrier dominates the breach rate** — a barrier
200 pips away survives longer than one 20 pips away for reasons that have nothing to do with
market makers. Any comparison that does not hold distance constant measures volatility and
reports it as doctrine.

Baselines are run **before** the real survival curve is computed.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Real barriers survive longer than distance-matched sham barriers | Support for a real level effect. The strongest weekly-scale result available from V02 |
| Identical survival | **The previous week's extreme is an ordinary price at this sample.** Report prominently — it would undercut the mechanism V02 states three times |
| Breach rate high but breach depth tiny | The *"spread to reach a little higher"* reading (V02 `[00:24:51]`) becomes the live one. **Report depth alongside rate always**; a rate alone is misleading here |
| Asymmetry between the toward/away barriers | Expected, and reported as a conditioning finding rather than folded into one number — **with §3b's cell counts attached** |
| Arms A and B diverge | Report both. A one-hour shift changes *which price* last week's extreme was, so divergence here is a genuine `D-031` finding rather than a rounding effect |

## 6. MANDATORY SCOPE STATEMENT

> **PT-030 tests whether the previous week's extreme acts as a barrier on GBP/USD.** It is
> **not** a test of "peak formation" (`A-010`) — the previous week's extreme is a measurement,
> and whether the instructor's peak formation coincides with it is undefined and untested here.
> **It resolves nothing in `C-001`** and adopts no day count. It is not a trading test: no
> entry, stop or target is involved.
>
> It **re-issues `PT-012`** onto `W-C′` under `D-035`; `PT-012` is retained, marked and never
> run, and no result here may be reported as `PT-012`'s result.
>
> **Price levels on this corpus are not comparable with the V02–V06 FXCM homework** (`D-036a`);
> only shape and distance claims travel, and **no barrier price here may be reconciled to an
> FXCM-sourced level**. Breaches are **bid-side** (§0b). The **week open is 22:00 UTC**, not
> FXCM's 21:00 UTC.

## 7. TO RUN THIS

1. **Run the QA gate first**; confirm `C1`–`C4` PASS; cite `QA_REPORT.txt`.
2. Build **both** `D-031` arms with `aggregate_m15.py`; record row counts and spans.
3. Confirm the window is `2013-01-06 → 2016-06-30`, wholly inside DEVELOPMENT. **Read nothing
   past 2016-06-30.** Record which `D-031` clock the boundary was applied in (`I-010` Q2, OPEN).
4. Record the realised week-open timestamp per week; derive week boundaries by timestamp lookup,
   never by bar count, and **never from `C7`'s open list** (§3a′.1). **Apply and count every
   exclusion explicitly: both §3a lag/boundary exclusions, and §3a″'s TWO — the week of
   2014-06-01 and the week of 2014-06-08, whose barrier comes from it.** Include and report
   separately the six Dec/Jan holiday weeks, recording the realised censoring time for
   **2015-12-20** and **2015-12-27**, which end on Thursday.
5. Build the **distance-matched sham-barrier control before** computing the real survival curve.
6. Report the four direction × breach-status cell **counts** beside their rates (§3b).
7. Report the five largest-range weeks as the pre-registered sensitivity appendix.
8. Write `BT_V02_NNNN.md` from the template, §0 referencing **this file and `PT-012`**. Record
   the survival curve against `C-001` as **evidence about price, not about the source**.
9. **Neither this file nor `PT-012` is ever edited to match what was found.**
