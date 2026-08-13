# PT-027 — Does the first move out of the week's opening range reverse? (RE-ISSUE of PT-009)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-009, which is NON-CONFORMING under D-035 (its window W-C straddles the
             pinned DEVELOPMENT/HOLDOUT boundary by 546 days). PT-009 is RETAINED, NOT
             DELETED, NEVER RUN, and is not edited into conformance — only its status
             block is added, per D-027 and the PT-022 precedent.
LESSON:      V01 [00:38:27], [00:38:39], [00:39:53], [00:43:07];
             V02 [00:09:44]-[00:09:51], [00:14:17]
DEPENDS ON:  PT-026 (the re-issued block definition). PT-008 is superseded and must not
             be run to supply it.
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
`PT-009`'s window `W-C` runs to 2017-12-29 and **straddles the boundary by 546 days**.
`COMMON_PROTOCOL.md` §3a and `D-027` require re-issue under a new `PT` number; the original is
**retained and marked, never edited**.

| Field | `PT-009` | **PT-027** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 complete weeks → **180 usable** (§3a) |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | **levels no longer comparable**; **no spread is in the data** — §0c |
| **Week open** | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | the opening range is a **Sunday-evening** object on a one-hour-shifted grid |
| Block supplier | `PT-008` | **`PT-026`** | inherits `PT-026` §0c's *"eight hours" vs "two bars"* split — §0b |
| Everything else | — | **unchanged** — question, trigger, outcomes, nulls, seed, scope | — |

### 0a. Three losses that are not negotiable

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   offset cannot be measured here. **Levels are not comparable with the V02–V06 FXCM homework;
   only shape and distance claims travel** (`D-036a`). This test's outcomes are breaches,
   returns and pip distances — **distances travel**; the drawn prices do not.
2. **The October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase at all.**
3. **The EU referendum week (2016-06-23) is inside `W-C′` and inside DEVELOPMENT**, one week
   before the boundary. **Not excluded** (`E09`). Stated now that it is very likely to appear in
   the sensitivity appendix, so that cannot later be presented as a discovery.

### 0b. The inherited block ambiguity — `D-030`, not resolved here

`PT-026` §0c records that on this corpus the instructor's *"first eight hours"* and *"first two
4-hour bars"* are **different spans** (8 h by clock vs 6–7 h by midnight-anchored buckets,
differing between `D-031` arms), because the 17:00 week open no longer lands on a 4-hour bucket
boundary as FXCM's 16:00 did.

**This test inherits that and does not resolve it.**

- **Headline trigger** = first 15m close beyond the **8-hour clock block**.
- **Pre-registered sensitivity arm** = the same trigger computed on the **two-4h-bars block**,
  reported every time.
- **The 12-hour block is not carried here** — `PT-026` reports it; adding a third trigger arm
  would multiply this test's cells without answering its question. Recorded so the omission is
  a choice on the record, not an oversight.

### 0c. A vendor property that changes what Outcome 3 can claim

The corpus is **bid-only M1 bars** with **structurally zero volume** (`D-036a`;
`datasets/README.md`). Consequences, pre-registered:

- **No spread is in the data.** Outcome 3 prices the prohibited trade on **bid quotes with no
  spread and no slippage modelled**, which makes it an **upper bound** on what taking that
  trade would have returned. **It is labelled as an upper bound in every report.** V04's own
  stop language elsewhere is *"7 pips plus spread"* — the *"plus spread"* half cannot be
  honoured by this corpus, and inventing a spread would be `D-030`'s exact prohibition.
- **Volume is not traded volume and no measure in this test reads it.**

---

## 1. WHY THIS TEST IS WORTH RUNNING

*"Do not take the first move of the week"* is **the clearest instruction in V01** — stated
three times as a prohibition (`V01_INTERPRETATION.md` I1, `EXPLICIT`, High confidence) — and
V02 supplies the mechanism:

> *"They are where the false move, where the dealer traps the traders."* `[00:09:44]`
> *"If they make the false move… and you bite on that… they are now trapped for the entire
> week."* `[00:14:17]`

A prohibition is only justified if the thing prohibited loses. **This test asks whether it
does.** And it can be asked without defining a single blocked term, because `PT-026` supplies a
measurable referent for "the first move": the first breach of the week's opening range (V03
`[00:12:46]`), which is the object V01's *"the first move out of the box"* `[00:43:07]` most
plausibly names and which V03/V04 make drawable.

> **The referent substitution is disclosed, not hidden.** V01's *"the box"* is `A-006` and its
> referent is open. This test does **not** claim to have resolved it. It tests a specific,
> drawable object and says so in §6 — which is the difference between an operationalisation and
> an approximation (`D-030`).

---

## 2. THE QUESTION

> After the first breach of the week's opening eight-hour range, does price return through the
> range and set the week's extreme on the **breach** side — more often than a matched control?

Null hypothesis: **it does not.** The first breach continues as often as it reverses.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute, with 4-hour for the "two bars" sensitivity block |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block (data split)** | **DEVELOPMENT, confirmed.** `W-C′` **is** `D-035`'s DEVELOPMENT block |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 in `raw/SHA256SUMS.txt`; aggregated by `scripts/aggregate_m15.py` per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST** (`D-036a`, QA `C7`). **NOT FXCM's 21:00 UTC.** Realised opens are read from timestamps and recorded |
| **Data-QA gate** | **Precondition.** `scripts/qa_histdata_m1.py`; `QA_REPORT.txt`; `C1`–`C4` PASS, `C5`–`C8` signed off in `D-036a`. Cited in the observation |
| Measurement rule | `E06` restated for a CSV corpus (`COMMON_PROTOCOL.md` §2): every quote parsed from a checksummed file; nothing measured off a rendering |
| Timezone | **Both `D-031` arms.** Arm A = corpus stamps verbatim; Arm B = +1h during US DST |
| **Trigger** | First 15m **close** beyond the week's opening **8-hour clock block** (`PT-026` headline arm), either side. **Sensitivity arm:** the same on the two-4h-bars block (§0b) |
| Decision point | **That close. No later bar is consulted for classification** |
| Outcome 1 — **reversal** | Does price subsequently trade back through the **opposite** edge of the block before the week's close? |
| Outcome 2 — **trap geometry** | Is the week's extreme on the breach side, and does it form within `X` hours of the trigger? `X` reported as a **distribution**, not pre-set |
| Outcome 3 — **the prohibition priced** | Counterfactual position taken **in the breach direction** at the trigger, **stop 18 pips, target 50 pips** (V04 `[00:04:43]`, `[00:05:07]` — the instructor's own numbers, not fitted). **Bid-only, no spread, no slippage → an UPPER BOUND** (§0c) |
| Excluded weeks | **None.** Weeks with no breach at all are **counted and reported**, not dropped |
| **Sample** | **180 TRADING weeks** — denominated in **trading weeks present with an observable week open**, not calendar weeks — at most one first-breach trigger each → **n ≤ 180**. See §3a |

Outcome 3 is the heart of it. **The prohibition is a claim that this trade loses**, and the only
honest way to test a prohibition is to price the prohibited trade.

### 3a. THE WEEK CENSUS, THE `C8` DISPOSITIONS, AND THE HONEST SAMPLE

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong.** Corrected against the corpus's own census (QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| **Calendar-complete weeks WITH an observable Sunday open** | **180** | 181 complete weeks, less the week of **2014-06-01**, which has none |

**Two facts a naive reading of `C7` gets backwards:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** looks like a week open.
   `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` sit **inside** weeks
   that opened normally on Sunday. **A run session taking week boundaries from `C7` would split
   those weeks and then hunt for a "first move of the week" inside a Thursday fragment.**
   Pre-registered: **a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open
   is never a week boundary and never arms a trigger.**
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** Zero bars
   for `2014-06-01 Sun` (nominal ~420), **521 of 1,440** for `2014-06-02 Mon`: **~22 continuous
   hours missing, covering the entire week open**. `C8` marks it
   `*** ABSENT AND UNEXPLAINED ***`.

**`C8` dispositions — pre-registered, by name.** `QA_REPORT.txt`'s gate requires an explicit
disposition for every `C8`-flagged session. Eleven sessions fall into **seven weeks** inside
`W-C′`, and the disposition is **not uniform**:

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition for this test** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0) | market closure | **INCLUDE, report separately** — block and trigger window intact |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE, report separately** |
| **2014-06-01** | **Sun (0), Mon (521)** | **DATA DEFECT** | **EXCLUDE BY NAME — no observable week open, so no block and no trigger** |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE, report separately** |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE, report separately** |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE, report separately** — **week ends Thursday**, so Outcome 1's "before the week's close" window is shorter |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE, report separately** — **week ends Thursday** |

*(The eleventh, `2013-01-01 Tue`, lies **outside** `W-C′`. Not applicable.)*

**Why the six holiday weeks are INCLUDED.** All six closures fall mid-week; every one of those
weeks **opens normally on Sunday**, so the block and the first-breach trigger are fully
observable. `PT-009` inherited *"Excluded weeks: None"* from the batch and
`COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation for being unrepresentative
(`E09`). **Re-deciding that after a QA check surfaced them would be the suit-the-result choice
the gate exists to prevent.** Two of them end Thursday, which shortens Outcome 1's reversal
window and Outcome 3's holding window — **reported separately with the realised censoring time,
never averaged in silently.**

**Why 2014-06-01 is EXCLUDED, and why that is not `E09`.** `E09` forbids excluding an
observation for **what the market did**. This is excluded because **the corpus does not contain
what the market did**, and the missing 22 hours contain the very object the trigger is defined
against. **Mechanical, by name, counted.**

**The honest sample:**

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar span, inclusive | 1,819 days | **1,272 days** |
| Calendar-complete Sun→Fri weeks | 260 | **181** |
| **Weeks USED (complete, observable open)** | 260 | **180** |
| Weeks yielding a first-breach trigger | ≤ 260 | **≤ 180** |

`n ≤ 180` clears `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 by a wide margin **for the
headline outcomes**, and stays clear even if a substantial minority of weeks never breach.

**Where it can go marginal, pre-registered rather than discovered:**

- **The third baseline — "second and later breaches of the same block in the same week" — has a
  count nobody can predict before running it.** If the number of weeks producing a *second*
  breach falls below 30, that control carries `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive
  only` in the same sentence as any rate quoted from it, **and the primary comparison then rests
  on N1 and N3 alone.** That contingency is fixed here so it cannot be renegotiated at run time.
- **Outcome 2's conditional cell** — *reversal happened* **and** *the week's extreme is on the
  breach side* — is a subset of a subset. If it falls under 30 it is descriptive only.
- The original file claimed *"~260 weeks, one trigger each. ≥ 30 satisfied"*. **That claim is
  now ≤ 180 and the sub-cell caveats above are new. They are a consequence of an honest window
  and an honest corpus, not of a weaker test.**

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN.** The session-completeness check was
> added to `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was
> drafted, and it is what surfaced the 2014-06-01 hole — which `C6` had excluded by
> construction (it skips anything ≥ 12 h as "the weekend") and `C7` had rendered cosmetic (it
> surfaced as a decorative **Monday** entry in a weekday tally). §3a is the **correction that
> check forced**, made **before any bar in `W-C′` was read**.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry** in the same weeks and the same session hours, direction matched to the breach, **same stop and target (18/50)**, 1,000 iterations, seed `20260812` |
| **Second** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812`. Answers whether the effect belongs to *the week's opening range* or to *any* range breach |
| **Third — the natural control** | **Second and later** breaches of the same block in the same week, measured identically. This is the course's own contrast: V01 forbids the *first* move and V02–V03 endorse the *return*. Holding week, instrument and geometry fixed while varying only the ordinal is the cleanest comparison available. **Subject to §3a's sample caveat** |

Baselines are run **before** the rule arm's aggregate is looked at.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| First breaches reverse more than later breaches and more than N1 | **The prohibition is doing real work.** Necessary support for V01's central instruction; not sufficient for any entry rule |
| First and later breaches behave alike | The prohibition is not distinguishing anything at this sample. A significant negative, since three lessons rest on it |
| Outcome 3 shows the forbidden trade is profitable | Report it plainly and prominently — **with §0c's upper-bound label attached**, because a no-spread result flatters any entry rule. A result that embarrasses the lesson is exactly the result `E25` exists to protect |
| Reversal happens but the week's extreme is elsewhere | The *"trapped for the entire week"* framing is not supported even where the reversal is. Report the two outcomes separately — they are separate claims |
| The headline block and the two-bars block (§0b) disagree | A finding about the instructor's two phrasings, not about the market. Report both; adopt neither as *the* definition (`D-030`) |
| Arms A and B diverge | Report both. A one-hour shift moves the block, the trigger and the week's extreme, so divergence here is expected to be larger than elsewhere in the batch |

## 6. MANDATORY SCOPE STATEMENT

> **PT-027 tests one operationalisation of *"the first move of the week"*: the first breach of
> the week's opening eight-hour range.** **`A-006` — what "the box" refers to in V01
> `[00:43:07]` — remains OPEN, and this test does not close it.** Nothing here identifies a
> "false move" or a "trap move" (`A-002`), which are undefined as patterns; the trigger is a
> range breach and is reported as a range breach.
>
> It **re-issues `PT-009`** onto `W-C′` under `D-035`; `PT-009` is retained, marked and never
> run, and no result here may be reported as `PT-009`'s result.
>
> **Price levels on this corpus are not comparable with the V02–V06 FXCM homework** (`D-036a`);
> only shape and distance claims travel. The **week open is 22:00 UTC**, not FXCM's 21:00 UTC.
> **Outcome 3 carries no spread and no slippage and is an upper bound**, always labelled as one.

## 7. TO RUN THIS

1. **Run the QA gate first**; confirm `C1`–`C4` PASS; cite `QA_REPORT.txt`.
2. **Run `PT-026` first.** This test consumes its block definition, and running them in the
   other order would mean tuning the block against this test's outcome. **`PT-008` is superseded
   and must not be run to supply the block.**
3. Build **both** `D-031` arms with `aggregate_m15.py`; record row counts and spans.
4. Confirm the window is `2013-01-06 → 2016-06-30`, wholly inside DEVELOPMENT. **Read nothing
   past 2016-06-30.** Record which `D-031` clock the boundary was applied in (`I-010` Q2, OPEN).
5. Record the realised week-open timestamp per week; boundaries by timestamp lookup, never by
   bar count, and **never from `C7`'s open list** (§3a.1). **Apply §3a's dispositions by name**:
   exclude the week of **2014-06-01**; include and report separately the six Dec/Jan holiday
   weeks, recording the realised week-close for **2015-12-20** and **2015-12-27**.
6. Run **all three baselines** before looking at the rule arm's aggregate.
7. Report the headline block **and** the two-bars sensitivity block, and **both** `D-031` arms,
   every time. Label Outcome 3 as an upper bound.
8. Write `BT_V01_NNNN.md` from the template, §0 referencing **this file and `PT-009`**.
9. **Neither this file nor `PT-009` is ever edited to match what was found.**
