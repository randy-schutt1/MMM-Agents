# PT-026 — "The dealer must cut" the first-eight-hours range of the week (RE-ISSUE of PT-008)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-008, which is NON-CONFORMING under D-035 (its window W-C straddles the
             pinned DEVELOPMENT/HOLDOUT boundary by 546 days). PT-008 is RETAINED, NOT
             DELETED, NEVER RUN, and is not edited into conformance — only its status
             block is added, per D-027 and the PT-022 precedent.
LESSON:      V03 [00:12:46]-[00:13:29] and its slide; V04 [00:16:06]-[00:16:15]
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
`PT-008`'s window `W-C` runs to 2017-12-29 and therefore **straddles the boundary by 546
days**. `COMMON_PROTOCOL.md` §3a and `D-027` require a **re-issue under a new `PT` number**
with a conforming window; the original is **retained and marked, never edited**. This is that
re-issue.

| Field | `PT-008` | **PT-026** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 complete weeks → **180 usable** (§3b–§3d) |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | **levels no longer comparable** with the V02–V06 homework |
| **Week open** | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | **§0c — this is the most consequential change in the file**, because the block *is* the first bars of the week |
| Everything else | — | **unchanged** — question, measures, nulls, seed, scope | — |

### 0a. Three losses that are not negotiable

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   offset cannot be measured for this window. **Levels are not comparable with the V02–V06 FXCM
   homework; only shape and distance claims travel** (`D-036a`). Every report says so. This
   test's measures are ranges, excursions and times — all **distances**, so they travel; the
   *drawn prices* of the block do not.
2. **The October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase at all.**
3. **The EU referendum week (2016-06-23) is inside `W-C′` and inside DEVELOPMENT**, one week
   before the boundary. It is **not excluded** (`E09`), and it is stated now that it is very
   likely to appear in the five-largest-range-weeks appendix, so that cannot later be presented
   as a discovery.

### 0b. `D-030` inheritance — what this re-issue does NOT quietly resolve

`PT-008` was blocked by `I-007` on *which feed defines the week*. `D-036a` supplies a feed and
a measured week open, so **that blocker is discharged, not approximated.** Nothing else in
`PT-008` was definitionally blocked, and this file introduces no new definition. Where the
vendor change creates a genuine ambiguity (§0c), it is **pre-registered as two reported arms**,
not resolved by preference.

### 0c. THE CHANGE THAT MATTERS: "eight hours" AND "two bars" NO LONGER COINCIDE

`PT-008` inherited both of the instructor's phrasings as though they were the same object:

> *"block the first **eight hours** off"* V03 `[00:12:46]` … *"two bars"* `[00:12:54]`
> *"Block off the first eight hours"* V04 `[00:16:11]`

On FXCM's **21:00 UTC** week open — 16:00 in a fixed UTC−5 chart — 16:00 is exactly a 4-hour
bucket boundary, so *the first two 4-hour bars* and *the first eight hours* are **the same
span**. `PT-008` could carry both phrasings in one row without noticing.

**On this corpus they are different spans, and by different amounts in each `D-031` arm:**

| Reading | Arm A (fixed UTC−5, week opens 17:00) | Arm B (`America/New_York` DST, week opens 18:00 in summer) |
|---|---|---|
| **"the first eight hours"** — by clock from the week open | 17:00 → **01:00**, 8 h | 18:00 → **02:00**, 8 h |
| **"the first two 4-hour bars"** — midnight-anchored buckets, per `aggregate_m15.py` | 16:00–20:00 bucket (**partial: 17:00–20:00, 3 h**) + 20:00–24:00 → **7 h total** | 16:00–20:00 bucket (**partial: 18:00–20:00, 2 h**) + 20:00–24:00 → **6 h total** |

**Pre-registered handling, fixed now:**

- **Headline = "the first eight hours" by clock**, 8 hours measured from the realised week
  open. Chosen because **that is what the slide prints** and what both lessons say aloud, and
  because it is the only reading that is the same length in both `D-031` arms.
- **Second arm = "the first two 4-hour bars"**, reported every time with its realised span
  length stated in hours.
- **Third arm = the 12-hour block**, carried over from `PT-008` unchanged
  (V03 `[00:29:51]` — *"Four, eight, twelve hours"*).
- **All three are reported whatever they show.** Reporting only the block that "worked" is
  `E09`.

**This is a disclosure, not a resolution.** Which span the instructor meant is not recoverable
from source; both phrasings are his, in two lessons. `D-030` forbids picking one and calling it
the definition, so the test **measures both and adopts neither.**

---

## 1. WHY THIS TEST IS WORTH RUNNING

This is **the most mechanically specific instruction in V01–V04**. It names a timeframe, a
count and two drawable prices, and it is given twice, by the instructor, in two lessons:

> *"What I want you to do on the four hour chart is block the first eight hours off. Mark
> the high of the first eight hours and mark the low of the first eight hours, two bars."*
> V03 `[00:12:46]`–`[00:12:54]`
> *"Block off the first eight hours that draw a line all the way across your chart. Those
> are your psychological support and resistance levels."* V04 `[00:16:11]`–`[00:16:15]`

And the slide states the prediction outright: *"Dealer **must cut** the perceived support and
resistance zone to make money and get traders in the game"* (`V03_SOURCE_NOTES.md` §4a) — a
stronger verb than the spoken *"has to exploit"*.

**"Must cut" is a falsifiable claim about a measurable object.** No pattern, no indicator, no
undefined noun. It is also the object every weekly rule downstream measures from, which makes
it the weekly-scale equivalent of what `PT-001` is doing at daily scale.

---

## 2. THE QUESTION

> Is the first-eight-hours range of the GBP/USD week breached — and is that breach more than
> what an arbitrarily placed eight-hour block would deliver?

Null hypothesis: **it is not special.** An eight-hour block at the week's open is breached at
the same rate, at the same speed and by the same distance as an eight-hour block placed
anywhere else in the week.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | **4-hour** for the "two bars" arm (the instructor's own); **15-minute** for the clock-based block and for breach timing |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block (data split)** | **DEVELOPMENT, confirmed.** `W-C′` **is** `D-035`'s DEVELOPMENT block; it cannot straddle the boundary |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 in `raw/SHA256SUMS.txt`; aggregated by `scripts/aggregate_m15.py`, one file per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST** (`D-036a`, QA `C7`: 187 opens, modal 17:00 in all twelve months, no seasonal shift). **NOT FXCM's 21:00 UTC.** The realised open of each week is read from timestamps and recorded |
| **Data-QA gate** | **Precondition.** `scripts/qa_histdata_m1.py`; report at `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt`; `C1`–`C4` PASS, `C5`–`C8` signed off in `D-036a`. Cited in the observation |
| Measurement rule | `E06` as restated for a CSV corpus (`COMMON_PROTOCOL.md` §2): every quote is parsed from a checksummed file; nothing is measured off a rendering |
| Timezone | **Both `D-031` arms.** Arm A = corpus stamps verbatim; Arm B = +1h during US DST |
| **The block — headline** | High and low of the **first eight hours of the trading week**, measured **by clock from the realised week open**, boundaries **looked up from bar timestamps, never counted in bars** (the V04 `M1` defect) |
| **The block — second arm** | High and low of the **first two 4-hour bars**, with its realised span length in hours reported (§0c) |
| **The block — third arm** | The **12-hour** block, V03 `[00:29:51]` |
| Measure 1 — **is it cut?** | Share of weeks in which price trades beyond the block high, beyond the block low, beyond **both**, beyond **neither** |
| Measure 2 — **when?** | Time from block close to first breach, in hours |
| Measure 3 — **how far?** | Maximum excursion beyond each edge, in pips |
| Measure 4 — **which first?** | Which edge is breached first, and whether the week's extreme ends up on that side |
| Decision point | **Block close.** Measures 2–4 are outcomes; **nothing after the block close informs the block itself** |
| Excluded weeks | **None.** Holiday-shortened weeks retained and reported separately |
| **Sample** | **180 TRADING weeks**, denominated in **trading weeks present in the corpus with an observable week open** — not calendar weeks. 181 calendar-complete weeks (the 182nd, 2016-06-26, is truncated by the DEVELOPMENT boundary — **excluded, counted, reported**) less the **2014-06-01** data hole, **excluded by name** (§3b–§3d) |

### 3a. `I-007` bit harder here than anywhere else in this batch — and it is now closed, with a different number

The block **is** the first hours of the week, so its value depends entirely on when the feed
opens the week. Feeds differ by hours, and some do not print Sunday bars at all —
`V03_INTERPRETATION.md` §9.2 flags exactly this (*"the instructor's feed shows Sunday candles;
many modern feeds do not"*).

**This corpus prints Sunday bars**, and the week opens **Sunday 17:00 local = 22:00 UTC**,
fixed, year-round. So:

- the block is a **Sunday-evening** object, not a Monday one;
- the Sunday portion of the trading week is only **7 hours long** (17:00 → 24:00), so the
  headline 8-hour block **crosses midnight into Monday** by one hour, and the "two bars" arm
  does **not** (§0c);
- **a feed change is a new test ID, not an adjustment.** The realised week-open timestamp is
  recorded in the observation as a first-class parameter.

**`I-010` Q1 is OPEN and touches this test directly:** whether FXCM's 21:00 UTC is a year-round
constant or a summer artifact is unmeasured. If FXCM is DST-anchored, it agrees with this
corpus in winter and differs by an hour in summer — which would mean any future cross-source
comparison of this block is on two different grids for part of the year. **Do not compare this
test's block against an FXCM-sourced one until `I-010` Q1 is closed.**

### 3b. THE WEEK CENSUS — CALENDAR WEEKS ARE NOT TRADING WEEKS

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong, and for this test — whose whole object is the first bars of the week — it is the worst
place to be wrong.** Corrected against the corpus's own census (QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start, which precedes `W-C′`) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| **Calendar-complete weeks WITH an observable Sunday open** | **180** | 181 complete weeks, less the week of **2014-06-01**, which has none |

**Two facts that a naive reading of `C7` gets backwards, and both would corrupt this test:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** is indistinguishable from a week open
   in that tally. `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` sit
   **inside** weeks that opened normally on Sunday. **A run session that took its week
   boundaries from `C7` would split those four weeks and then measure a "first eight hours"
   block starting on a Thursday.** Pre-registered: **a week is delimited by its Sunday 17:00
   open; an intra-week holiday re-open is never a week boundary and never starts a block.**
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** The corpus
   holds **zero bars** for `2014-06-01 Sun` (nominal ~420) and **521 of 1,440** for
   `2014-06-02 Mon`: **~22 continuous hours missing, covering the entire week open**. `C8` marks
   it `*** ABSENT AND UNEXPLAINED ***`. **That week has no observable week open, so it cannot
   support this test at all.**

### 3c. `C8` DISPOSITIONS — PRE-REGISTERED, BY NAME, NOT LEFT TO RUN TIME

`QA_REPORT.txt`'s gate line requires that *"any session flagged by `C8` must have an explicit,
**PRE-REGISTERED** disposition (include / exclude / report separately) in the test that spans
it."* `C8` flags **eleven sessions**, falling into **seven weeks** inside `W-C′`. The
disposition is **not uniform**, because the two categories are not the same kind of thing.

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition for this test** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0 bars) | market closure | **INCLUDE, report separately** — block intact |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE, report separately** — block intact |
| **2014-06-01** | **Sun 2014-06-01 (0), Mon 2014-06-02 (521)** | **DATA DEFECT** | **EXCLUDE BY NAME — no observable week open** |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE, report separately** — block intact |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE, report separately** — block intact |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE, report separately** — block intact, **week ends Thursday** |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE, report separately** — block intact, **week ends Thursday** |

*(The eleventh flagged session, `2013-01-01 Tue`, is the corpus's opening fragment and lies
**outside** `W-C′`. Not applicable.)*

**Why the six holiday weeks are INCLUDED — and note the specific reason for this test.** All six
closures fall **mid-week (Wed/Thu/Fri)**; every one of those weeks **opens normally on Sunday**,
so **the first eight hours, the first two 4-hour bars and the twelve-hour arm are all fully
present in all six.** Nothing this test decides at its decision point is affected. What *is*
affected is the outcome window: two of the six end on **Thursday**, so Measures 2–4 are censored
earlier, and those two are reported separately with their realised censoring time. `PT-008`
already pre-registered *"Excluded weeks: None — holiday-shortened weeks retained and reported
separately"*, and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation for being
unrepresentative (`E09`). **Re-deciding that now, after a QA check surfaced them, would be the
suit-the-result choice the gate exists to prevent.** The disposition is inherited; the naming is
what is new.

**Why the 2014-06-01 week is EXCLUDED, and why that is not `E09`.** `E09` forbids excluding an
observation because of **what the market did**. This is excluded because **the corpus does not
contain what the market did** — and specifically because the missing 22 hours *are* the object
under test. There is no week open to measure eight hours from. **Mechanical, by name, counted.**

### 3d. The sample, computed honestly

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar span, inclusive | 1,819 days | **1,272 days** |
| Calendar Sundays | 260 | **182** |
| Calendar-complete Sun→Fri weeks | 260 | **181** |
| **Weeks USED — blocks measurable (Measures 1–4)** | 260 | **180** — 181 less the 2014-06-01 hole (§3c) |

**`n = 180` clears `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 by a factor of six.
Nothing in this test is marginal at the headline level.**

**Where it thins, stated in advance:** Measure 4's cross-tabulation — *first-breach side* ×
*week's-extreme side* × **three block arms** × **two `D-031` arms** — is a 2×2 table computed
twelve times. Each 2×2 table still has n = 180, so the tables are fine; what is **not** fine is
quoting a cell as a rate without its interval (§4.2). The **weeks that breach neither edge**
(Measure 1's fourth category) may plausibly be a small minority; if that count falls under 30,
it carries `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` in the same sentence,
**every time it is quoted**. That is pre-registered here so it cannot be negotiated at run time.

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN.** The session-completeness check was
> added to `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was
> drafted, and it is what surfaced the 2014-06-01 hole — which `C6` had excluded by
> construction (it skips anything ≥ 12 h as "the weekend") and `C7` had rendered cosmetic (it
> surfaced as a decorative **Monday** entry in a weekday tally). §3b, §3c and §3d are the
> **correction that check forced**, made **before any bar in `W-C′` was read**.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812`. The price path is untouched; only the week boundary moves. This isolates "the week's *opening* block" from "any eight-hour block" |
| **Second — the natural control** | Eight-hour blocks at **every** 4-hour offset through the week, measured identically. The 120-hour trading week gives **30** such offsets; the week-open block is **ranked among them** rather than tested alone |
| **Third** | Block-width control: the same measures for blocks of **4, 8, 12 and 24 hours**, so a "wider blocks get breached less" artifact cannot masquerade as a finding about the week's open. **This control also absorbs §0c**: the "two bars" arm's realised 6–7 hour span sits inside this sweep by construction |

Baselines are run **before** the week-open block's numbers are looked at.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| The week-open block is breached at a rate indistinguishable from shifted blocks | **The week's opening range carries no special status at this sample.** A foundational null for the weekly half of the method — report prominently |
| Breach rate is ordinary but breach *timing* is not (e.g. concentrated early) | A narrower, real finding, and the more likely one. Report the timing distribution |
| The block is breached on both sides in most weeks | The "must cut" language is satisfied trivially, and the measure that matters becomes *which side first* (Measure 4) rather than *whether* |
| First-breach side predicts the week's extreme side | **This is the result `PT-027` is built to follow up.** Reported here as an association, not as a rule; `PT-027` tests it as a prediction |
| The three block arms (§0c) disagree | **A finding about the instructor's two phrasings, not about the market.** Report all three spans with their realised lengths; adopt none as *the* definition (`D-030`) |
| Arms A and B diverge | Report both. Here the divergence is structural as well as statistical — the "two bars" arm is a **different length** in each arm (§0c) — so state which part of any divergence is arithmetic |

## 6. MANDATORY SCOPE STATEMENT

> **PT-026 tests whether the first-eight-hours range of the week is breached, when and how
> far.** It is **not** a test of the anchor point (`A-001`), the level (`A-004`), the M/W
> (`A-011`) or any entry. It measures a drawn range and reports what price did to it.
>
> It **re-issues `PT-008`** onto `W-C′` under `D-035`; `PT-008` is retained, marked and never
> run, and no result here may be reported as `PT-008`'s result.
>
> **Price levels on this corpus are not comparable with the V02–V06 FXCM homework** (`D-036a`);
> only shape and distance claims travel. The **week open is 22:00 UTC**, not FXCM's 21:00 UTC.
> The instructor's *"eight hours"* and *"two bars"* are **different spans on this corpus** and
> both are reported; neither is adopted as the definition.

## 7. TO RUN THIS

1. **Run the QA gate first**; confirm `C1`–`C4` PASS; cite `QA_REPORT.txt`.
2. Build **both** `D-031` arms with `aggregate_m15.py` (15m), and the 4-hour aggregation for
   the "two bars" arm. Record row counts and spans.
3. **Record the realised week-open timestamp for every week** — this test is *about* that
   instant. Boundaries by timestamp lookup, never by bar count, and **never from `C7`'s open
   list**, which counts intra-week holiday re-opens as opens (§3b.1). **Apply §3c's dispositions
   by name**: exclude the week of **2014-06-01**; include and report separately the six Dec/Jan
   holiday weeks, recording the realised censoring time for **2015-12-20** and **2015-12-27**,
   which end on Thursday.
4. Confirm the window is `2013-01-06 → 2016-06-30`, wholly inside DEVELOPMENT. **Read nothing
   past 2016-06-30.** Record which `D-031` clock the boundary was applied in (`I-010` Q2 is
   OPEN — record, do not decide).
5. Run **N3 and the 30-offset sweep and the width sweep first**, before looking at the
   week-open block's numbers.
6. Report **all three block arms** (8-hour clock, two-4h-bars, 12-hour) and **both** `D-031`
   arms, every time.
7. Report the five largest-range weeks in `W-C′` as the pre-registered sensitivity appendix
   (`COMMON_PROTOCOL.md` §3), as an appendix and **not** as a filtered re-run.
8. Write `BT_V03_NNNN.md` from the template, §0 referencing **this file and `PT-008`**.
9. **Neither this file nor `PT-008` is ever edited to match what was found.**
