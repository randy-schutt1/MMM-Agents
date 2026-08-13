# PT-031 — Are Sunday and Monday the week's accumulation phase? (RE-ISSUE of PT-013)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-013, which is NON-CONFORMING under D-035 (its window W-C straddles the
             pinned DEVELOPMENT/HOLDOUT boundary by 546 days). PT-013 is RETAINED, NOT
             DELETED, NEVER RUN, and is not edited into conformance — only its status
             block is added, per D-027 and the PT-022 precedent.
LESSON:      V02 [00:09:22]-[00:09:51], [00:11:44]-[00:12:15]
ATTESTATION: No chart, no price series and no outcome data of any kind — in W-C′ or in
             any other window — was opened, loaded, parsed or inspected by the session
             that wrote this file. The HistData corpus was cited from its committed
             provenance (SHA256SUMS.txt) and its QA report; not one quote was read from
             it. The D-035 holdout (2016-07-01 → 2017-12-29) was not opened, and per
             D-036a it is not on disk.
NOTE:        PT-013 3a asked whether the declared feed prints Sunday bars. IT DOES, and
             the answer changes the shape of the test rather than merely unblocking it.
             See 0c.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.
Decisions: `D-007` · `D-026`/`D-029` · `D-027`/`D-028` · **`D-030`** · **`D-031`** ·
`D-034` → **`D-036`/`D-036a`** · **`D-035`**.

---

## 0. WHY THIS FILE EXISTS, AND WHAT THE SUBSTITUTIONS COST

`D-035` pins **DEVELOPMENT = 2013-01-06 → 2016-06-30**, **HOLDOUT = 2016-07-01 → 2017-12-29**.
`PT-013`'s window `W-C` runs to 2017-12-29 and **straddles the boundary by 546 days**.
`COMMON_PROTOCOL.md` §3a and `D-027` require re-issue under a new `PT` number; the original is
**retained and marked, never edited**.

| Field | `PT-013` | **PT-031** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 complete weeks → **180 usable trading weeks** (arm 3: **179**) — §3b′–§3c |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | **levels no longer comparable** with the V02–V06 homework |
| **Week open** | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | **the Sunday span is 7 hours, and "Sunday + Monday" is 31 hours, not 48** — §0c |
| Arm 2 status | *"unrunnable on a feed with no Sunday bars"* — conditional | **RUNNABLE.** This corpus prints Sunday bars | the conditional resolves **in favour of running it** |
| Everything else | — | **unchanged** — question, three day-set arms, four metrics, controls, seed, scope | — |

### 0a. Three losses that are not negotiable

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   offset cannot be measured here. **Levels are not comparable with the V02–V06 FXCM homework;
   only shape and distance claims travel** (`D-036a`). This test's metrics are a **range in
   pips**, a **containment share**, a **distance** and a **time** — all shape/distance, so all
   travel.
2. **The October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase at all.**
3. **The EU referendum week (2016-06-23) is inside `W-C′` and inside DEVELOPMENT**, one week
   before the boundary. **Not excluded** (`E09`); very likely to appear in the sensitivity
   appendix. Stated now.

### 0b. `D-030` inheritance — the block this re-issue does NOT resolve

`PT-013` §6 records that **"accumulation" is not defined by the course** (`V02_SOURCE_NOTES.md`
§3 — given as an answer, never expanded), and that the test measures a **named proxy**: range,
containment and boundary relevance. **That block is inherited unchanged.** The re-issue supplies
a window and a data source; it supplies **no definition** of accumulation, and nothing here may
be read as having closed it.

### 0c. THE CHANGE THAT MATTERS: "Sunday + Monday" IS 31 HOURS, NOT TWO DAYS

On this corpus the trading week runs **Sunday 17:00 → Friday 17:00 local = 120 hours**. The
day-sets the instructor names are therefore **not** equal-length two-day blocks, and neither are
the controls they are ranked against:

| Span | Hours (Arm A) | Note |
|---|---|---|
| **Arm 1 — Sunday + Monday** | **31 h** (Sun 17:00 → Mon 24:00) | the headline reading, and the **shortest** span in the comparison |
| **Arm 2 — Sunday alone** | **7 h** (17:00 → 24:00) | runnable, and very short |
| **Arm 3 — Friday + Sunday + Monday** | **48 h** (prior Fri 00:00–17:00, + 7 h, + 24 h) | needs the **previous** week's Friday — §3b |
| Control — Monday + Tuesday | 48 h | |
| Control — Tuesday + Wednesday | 48 h | |
| Control — Wednesday + Thursday | 48 h | |
| Control — Thursday + Friday | **41 h** (24 + 17) | |

**Consequences, all pre-registered:**

1. **A raw range comparison is rigged against Arm 1 and Arm 2 by arithmetic alone.** A 31-hour
   span contains less range than a 48-hour span for reasons that have nothing to do with market
   makers. `PT-013`'s third baseline (length normalisation) was written to police *across arms
   1–3*; **it is extended here to the primary control as well, and the length-normalised
   comparison becomes the HEADLINE**, with the raw one reported beside it. **Both are always
   reported.**
2. **Under `D-031` Arm B the spans change size again** — the week opens at local 18:00 during US
   DST, so Sunday is **6 h** and Arm 1 is **30 h** in DST weeks. **Span lengths are computed per
   week and per arm, never once for the batch.**
3. **Thursday + Friday has no "remaining week".** Metric 2 (containment of the remaining week's
   bars) and Metric 4 (time to first breach after the span) are **undefined** for it. They are
   reported as **`NOT APPLICABLE`**, never as zero and never silently dropped — a zero would
   read as "perfectly contained" and invert the meaning.
4. **Under FXCM's 21:00 UTC open none of this would have been visible**, because a 16:00 open
   makes the Sunday span 8 hours and Arm 1 32 hours — still not 48. **The asymmetry was always
   there; the vendor change is what forced it onto the record.** Recorded so a later session does
   not read it as an artifact introduced by HistData.

---

## 1. WHY THIS TEST IS WORTH RUNNING

This is the analogy the whole weekly cycle is built on, stated four times in one lesson:

> *"What's the Asian session? Accumulation."* `[00:09:22]`
> *"So if the Asian session is accumulation, then **Sunday and Monday is the Asian session for
> the week**."* `[00:09:29]`

If it holds, the intraday method transfers to the week and V02's central claim has support. If
Sunday+Monday is an ordinary two-day span on GBP/USD, the transfer is an analogy and nothing
more — and three lessons of weekly-scale teaching rest on it.

The claim has a measurable core: an **accumulation phase is a low-range, range-bound span whose
boundaries later matter**. Range, containment and subsequent boundary-relevance are all
measurable. Nothing blocked is required.

### 1a. The instructor relaxes the days himself, so the test must too

> *"I could say Sunday is the Asian session… The first part of the week, Sunday, Monday,
> Tuesday, could be **Friday, Sunday, Monday**."* `[00:11:44]`

`V02_INTERPRETATION.md` `G9` is explicit: **do not encode the days.** The *role* is fixed; the
*calendar* is not. This test therefore pre-registers **all three day-sets he names as separate
arms, all reported** — which converts his own hedge from a get-out into a measured comparison.

---

## 2. THE QUESTION

> Is the Sunday+Monday span systematically lower-range and more contained than the spans that
> follow it — **once length is held constant** — and do its boundaries matter to the rest of the
> week?

Null hypothesis: **it is not.** Sunday+Monday behaves like any equal-length span in the week.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute; 4-hour cross-check |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block (data split)** | **DEVELOPMENT, confirmed.** `W-C′` **is** `D-035`'s DEVELOPMENT block |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 in `raw/SHA256SUMS.txt`; aggregated by `scripts/aggregate_m15.py` per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST** (`D-036a`, QA `C7`). **NOT FXCM's 21:00 UTC.** Every span boundary below is derived from it |
| **Sunday bars** | **PRESENT.** This corpus opens the week Sunday 17:00 and prints Sunday bars — **7 hours of them**. `PT-013` §3a's conditional resolves: **arm 2 runs**, and is **not** redefined as "Monday's first eight hours" (that substitution would be `D-030`'s exact prohibition) |
| **Data-QA gate** | **Precondition.** `scripts/qa_histdata_m1.py`; `QA_REPORT.txt`; `C1`–`C4` PASS, `C5`–`C8` signed off in `D-036a`. Cited in the observation |
| Measurement rule | `E06` restated for a CSV corpus (`COMMON_PROTOCOL.md` §2) |
| Timezone | **Both `D-031` arms.** Arm A = corpus stamps verbatim; Arm B = +1h during US DST — **and Arm B resizes every span** (§0c.2) |
| **Arm 1** | **Sunday + Monday** — the headline reading. **31 h** |
| **Arm 2** | **Sunday alone** — `[00:11:44]`. **7 h** |
| **Arm 3** | **Friday + Sunday + Monday** — `[00:11:44]`, **48 h**, length-normalised. Uses the **previous** week's Friday (§3b) |
| Metric 1 — range | Span range in pips, and as a share of the whole week's range. **Reported raw AND length-normalised (pips per hour); the normalised form is the headline** (§0c.1) |
| Metric 2 — containment | Share of the remaining week's bars that trade **inside** the span's high/low. **`NOT APPLICABLE` for Thu+Fri** (§0c.3) |
| Metric 3 — boundary relevance | Whether the week's extreme forms beyond the span's edge, and the distance |
| Metric 4 — the false move | Time from span close to the first breach of either edge (shared definition with `PT-026`/`PT-027`, computed here at day rather than 8-hour granularity). **`NOT APPLICABLE` for Thu+Fri** |
| Excluded weeks | **None.** Weeks with a holiday Monday are retained and reported separately |
| Decision point | **Span close.** Metrics 2–4 are outcomes |
| **Sample** | **180 TRADING weeks** for arms 1 and 2; **179** for arm 3 — denominated in **trading weeks present in the corpus with an observable Sunday session**, not calendar weeks (§3b′–§3c) |

### 3a. Sunday bars are a feed property, not a market property — and this feed has them

Some feeds print a short Sunday session; some fold it into Monday; some do not print it at all.
`V03_INTERPRETATION.md` §9.2 flags exactly this. **This corpus prints Sunday bars**, measured:
`C7`'s week-open census finds **187 opens, 181 of them Sunday, modal time 17:00 in all twelve
months, no seasonal shift** (`D-036a`).

So arm 2 **runs**, at **7 hours** per week. `PT-013` §3a's instruction — *record it as `NOT
RUNNABLE ON THIS FEED` rather than silently redefining it* — does not fire, **and the reason it
does not fire is recorded here so that a future feed change re-raises it rather than inheriting
this answer.**

### 3b. Arm 3 needs the previous week's Friday — one structural exclusion

Arm 3's *"Friday, Sunday, Monday"* spans the weekend, so its Friday is the **previous trading
week's**. For the first week in `W-C′` (opening **2013-01-06**) that Friday is **2013-01-04**,
which lies **inside the corpus but outside `W-C′`**. **Arm 3 therefore excludes that week: n =
180**, and the exclusion is **counted and reported**. Using 2013-01-04 would silently widen the
pre-registered window, which is exactly what `D-027` forbids.

The final week-open in `W-C′`, **2016-06-26**, is **truncated by the DEVELOPMENT boundary** (no
Friday, no remaining week). **Excluded from all arms, counted and reported.**

### 3b′. THE WEEK CENSUS — CALENDAR WEEKS ARE NOT TRADING WEEKS

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong, and for a test whose headline arm IS the Sunday session it is the worst place to be
wrong.** Against the corpus's own census (QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| **Weeks with an observable SUNDAY SESSION** | **180** | 181 complete weeks, less the **2014-06-01** data hole |

**Two facts a naive reading of `C7` gets backwards:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** looks like a week open.
   `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` sit **inside** weeks
   that opened normally on Sunday. **A run session taking week boundaries from `C7` would build
   a "Sunday + Monday" span starting on a Thursday.** Pre-registered: **a week is delimited by
   its Sunday 17:00 open; an intra-week holiday re-open is never a week boundary and never
   starts a span.**
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** The corpus
   holds **zero bars** for `2014-06-01 Sun` (nominal ~420) and **521 of 1,440** for
   `2014-06-02 Mon`. `C8` marks it `*** ABSENT AND UNEXPLAINED ***`. **That week has no Sunday
   session at all**, so arms 1, 2 and 3 have no span to measure.

### 3b″. `C8` DISPOSITIONS — PRE-REGISTERED, BY NAME

Eleven `C8`-flagged sessions fall into **seven weeks** inside `W-C′`. The disposition is **not
uniform**:

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition for this test** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0) | market closure | **INCLUDE, report separately** — Sun+Mon span intact; the **Wed+Thu control** is degenerate that week |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE, report separately** — Sun+Mon intact |
| **2014-06-01** | **Sun (0), Mon (521)** | **DATA DEFECT** | **EXCLUDE BY NAME from ALL THREE ARMS — no Sunday session exists** |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE, report separately** |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE, report separately** |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE, report separately** — **no Friday**, so the **Thu+Fri control** is a Thursday-only span that week |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE, report separately** — **no Friday** |

*(The eleventh, `2013-01-01 Tue`, lies **outside** `W-C′`. Not applicable.)*

**Why the six holiday weeks are INCLUDED — and the one thing that must be reported with them.**
`PT-013` pre-registered *"Excluded weeks: **None.** Weeks with a holiday Monday are retained and
reported separately"*, and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation
for being unrepresentative (`E09`). **Re-deciding that now, after a QA check surfaced them,
would be the suit-the-result choice the gate exists to prevent.** Note that in all six the
**Sunday and Monday sessions are intact** — the closures fall Wed/Thu/Fri — so the **headline
arm is unaffected in every one of them**. What *is* affected is the **control set**: a week with
a closed Wednesday or an absent Friday makes `Wed+Thu` or `Thu+Fri` a short span, and §0c
already makes span length load-bearing. **The realised span length in hours is reported per week
per control**, and the length-normalised comparison (§0c.1) absorbs the difference by design.
**A short control span in a holiday week is market structure, not a defect.**

**Why 2014-06-01 is EXCLUDED, and why that is not `E09`.** `E09` forbids excluding an
observation for **what the market did**. This is excluded because **the corpus does not contain
what the market did** — and here the missing session *is* the test: arm 2 **is** the Sunday
session, arm 1 begins with it, and arm 3 contains it. There is nothing to measure.
**Mechanical, by name, counted.**

### 3c. The sample, computed honestly

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar span, inclusive | 1,819 days | **1,272 days** |
| Calendar Sundays | 260 | **182** |
| Calendar-complete Sun→Fri weeks | 260 | **181** |
| **Arm 1 / Arm 2 weeks (TRADING weeks with a Sunday session)** | 260 | **180** |
| **Arm 3 weeks** (also needs the previous week's Friday) | 259 | **179** |
| Control spans per week | 4 | **4** (Mon+Tue, Tue+Wed, Wed+Thu, Thu+Fri) |

**`n = 180` (arms 1–2) and `n = 179` (arm 3) clear `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor
of 30 by a factor of six. No arm and no control span is marginal on its own count.** All three
are denominated in **trading weeks present in the corpus with an observable Sunday session**,
never in calendar weeks.

**Where it thins, pre-registered rather than discovered:**

- **The ranking statistic** — *"is Sun+Mon the lowest-range span in this week?"* — is a
  **per-week categorical outcome over five spans**, so the ranking distribution has 180
  observations spread over 5 ranks: 36 per rank under the null. **Adequate.** But the
  **Thu+Fri** control drops out of Metrics 2 and 4 (§0c.3), leaving **four** spans there and a
  different denominator. **Report the denominator with every ranking figure**; a rank-of-5 and a
  rank-of-4 are not comparable numbers.
- **Metric 3's conditional** — *the week's extreme forms beyond the span's edge* — will be true
  in the large majority of weeks by construction for a 31-hour span inside a 120-hour week. **The
  informative quantity is the DISTANCE, not the share**, and if the complementary subset (extreme
  inside the span) falls below 30 it is **descriptive only**.
- The original claimed *"~260 weeks per arm. ≥ 30 satisfied"*. **That is now 180/180/179 and the
  caveats above are new — a consequence of an honest window, an honest week length and an honest
  corpus, not of a weaker test.**

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN.** The session-completeness check was
> added to `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was
> drafted, and it is what surfaced the 2014-06-01 hole — which `C6` had excluded by
> construction (it skips anything ≥ 12 h as "the weekend") and `C7` had rendered cosmetic (it
> surfaced as a decorative **Monday** entry in a weekday tally). §3b′, §3b″ and the corrected
> counts in §3c are the **correction that check forced**, made **before any bar in `W-C′` was
> read**. Note the irony this test should record: **`C8` is the check that finally measured
> whether the Sunday session is actually there — which is the very object arm 2 tests.**

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | The same metrics for **every other two-day span** in the week (Mon+Tue, Tue+Wed, Wed+Thu, Thu+Fri). Ranking Sun+Mon among them holds week, instrument and metric fixed and varies only the days — **and the ranking is done on the LENGTH-NORMALISED metric**, because the spans are 31/48/48/48/41 hours (§0c.1) |
| **Second** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812` |
| **Third** | Length-normalised comparison **across arms 1–3 and across the four controls**, so no span can win on range simply by being longer or shorter |

Baselines are run **before** Sun+Mon's own numbers are looked at.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Sun+Mon is the lowest length-normalised-range span in most weeks, and its edges are later relevant | Support for the analogy that carries V02's weekly teaching |
| Low range but no boundary relevance | Half the claim. *"Quiet"* and *"the level the dealer later exploits"* are different assertions and this outcome separates them — which is the most useful thing this test can do |
| Sun+Mon ranks mid-pack | **The analogy has no measurable support at this sample.** Report prominently |
| A different arm wins | Report all three and adopt none as doctrine. The instructor names all three himself, so a winner among them is a **measurement, not a correction of him** |
| Sun+Mon wins on **raw** range but not on **normalised** range | **The most likely trap in this test, and it is arithmetic.** A 31-hour span containing less range than a 48-hour one is not a finding. Both forms are reported; **the normalised one governs the verdict** |
| Arms A and B diverge | Report both — and state how much of the divergence is the DST resizing of the spans (§0c.2) rather than market behaviour |

## 6. MANDATORY SCOPE STATEMENT

> **PT-031 tests whether the week's opening days are a low-range, later-relevant span on
> GBP/USD.** **"Accumulation" is not defined by the course** (`V02_SOURCE_NOTES.md` §3 — given
> as an answer, never expanded), so this test measures a proxy it names explicitly: range,
> containment and boundary relevance. It is not a test of contract accumulation, which no candle
> chart can observe.
>
> It **re-issues `PT-013`** onto `W-C′` under `D-035`; `PT-013` is retained, marked and never
> run, and no result here may be reported as `PT-013`'s result.
>
> **"Sunday + Monday" is 31 hours on this corpus, not two days** (§0c); the length-normalised
> comparison governs. **Price levels are not comparable with the V02–V06 FXCM homework**
> (`D-036a`); only shape and distance claims travel. The **week open is 22:00 UTC**, not FXCM's
> 21:00 UTC.

## 7. TO RUN THIS

1. **Run the QA gate first**; confirm `C1`–`C4` PASS; cite `QA_REPORT.txt`.
2. Build **both** `D-031` arms with `aggregate_m15.py`; record row counts and spans.
3. Confirm the window is `2013-01-06 → 2016-06-30`, wholly inside DEVELOPMENT. **Read nothing
   past 2016-06-30.** Record which `D-031` clock the boundary was applied in (`I-010` Q2, OPEN).
4. **Record that the feed prints Sunday bars, and record the realised Sunday span length per
   week and per arm** (§0c.2) before any metric is computed.
5. Derive all span boundaries by timestamp lookup from the 22:00 UTC / 17:00-local week open,
   never by bar count, and **never from `C7`'s open list** (§3b′.1). **Apply and count every
   exclusion: §3b's two, and §3b″'s exclusion of the week of 2014-06-01 from all three arms.**
   Include and report separately the six Dec/Jan holiday weeks, recording the realised span
   length per week per control — the **Wed+Thu** control is short in three of them and the
   **Thu+Fri** control has no Friday in two.
6. Compute the four other two-day spans **before** looking at Sun+Mon.
7. Report **all three day-set arms, both `D-031` arms, and both the raw and length-normalised
   forms of Metric 1** — every time. Mark Thu+Fri's Metrics 2 and 4 **`NOT APPLICABLE`**.
8. Report the five largest-range weeks as the pre-registered sensitivity appendix.
9. Write `BT_V02_NNNN.md` from the template, §0 referencing **this file and `PT-013`**.
10. **Neither this file nor `PT-013` is ever edited to match what was found.**
