# PT-029 — Is the rest of the week a "unidirectional swing" after the extreme? (RE-ISSUE of PT-011)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-011, which is NON-CONFORMING under D-035 (its window W-C straddles the
             pinned DEVELOPMENT/HOLDOUT boundary by 546 days). PT-011 is RETAINED, NOT
             DELETED, NEVER RUN, and is not edited into conformance — only its status
             block is added, per D-027 and the PT-022 precedent.
LESSON:      V02 [00:14:37], [00:14:54]; V03 [00:33:36]-[00:34:19]
ATTESTATION: No chart, no price series and no outcome data of any kind — in W-C′ or in
             any other window — was opened, loaded, parsed or inspected by the session
             that wrote this file. The HistData corpus was cited from its committed
             provenance (SHA256SUMS.txt) and its QA report; not one quote was read from
             it. The D-035 holdout (2016-07-01 → 2017-12-29) was not opened, and per
             D-036a it is not on disk.
CLASS:       DESCRIPTIVE by construction — the anchor is retrospective. See 3a.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.
Decisions: `D-007` · `D-026`/`D-029` · `D-027`/`D-028` · **`D-030`** · **`D-031`** ·
`D-034` → **`D-036`/`D-036a`** · **`D-035`**.

---

## 0. WHY THIS FILE EXISTS, AND WHAT THE SUBSTITUTIONS COST

`D-035` pins **DEVELOPMENT = 2013-01-06 → 2016-06-30**, **HOLDOUT = 2016-07-01 → 2017-12-29**.
`PT-011`'s window `W-C` runs to 2017-12-29 and **straddles the boundary by 546 days**.
`COMMON_PROTOCOL.md` §3a and `D-027` require re-issue under a new `PT` number; the original is
**retained and marked, never edited**.

| Field | `PT-011` | **PT-029** | Cost, stated now |
|---|---|---|---|
| Window | `W-C` 2013-01-06 → **2017-12-29** | **`W-C′` 2013-01-06 → 2016-06-30** | 260 complete weeks → **180 usable trading weeks** (§3a) |
| Block | `PROVISIONAL DEVELOPMENT pending D-028` | **DEVELOPMENT — confirmed against `D-035`** | none; this is the gain |
| Data source | TradingView / FXCM (`D-034`) | **HistData GBP/USD M1 CSV corpus** (`D-036a`) | **levels no longer comparable**; the **path-length metric is now bar-resolution-dependent** — §0b |
| **Week open** | FXCM **21:00 UTC** | **22:00 UTC** (Sunday 17:00, fixed UTC−5, no DST) | the post-anchor span and the net-zero reference open both shift by an hour |
| Everything else | — | **unchanged** — question, metrics, controls, seed, scope | — |

### 0a. Three losses that are not negotiable

1. **Price levels do not travel.** FXCM serves no 2013–2016 GBP/USD, so `D-034`'s cross-vendor
   offset cannot be measured here. **Levels are not comparable with the V02–V06 FXCM homework;
   only shape and distance claims travel** (`D-036a`). Every metric in this test is a **ratio or
   a pip distance**, so all of them travel — this is the test least damaged by the vendor change.
2. **The October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase at all.**
   That matters more here than elsewhere: a flash crash is the archetype of a maximally
   efficient post-extreme run, and its absence is a **property of the sample, not of the
   market**. Say so in the report.
3. **The EU referendum week (2016-06-23) is inside `W-C′` and inside DEVELOPMENT**, one week
   before the boundary. **Not excluded** (`E09`), and very likely to appear in the sensitivity
   appendix and near the top of the efficiency distribution. Stated now.

### 0b. One metric is resolution-dependent, and that is a vendor fact worth pinning

Directional efficiency is `|net movement| ÷ Σ|bar-to-bar movement|`. **The denominator grows as
the bar gets finer** — the same week measured on M1 has a longer path than on M15, so efficiency
is *lower* at finer resolution. This is arithmetic, not a market property.

**Pre-registered:** the path is summed over **15-minute bars**, on the `aggregate_m15.py` output
for the arm being reported, **for every week and every control alike**. The M1 corpus is **not**
used for the path sum. The resolution is stated in the observation as a first-class parameter,
because an efficiency number without its bar size is unreadable and **not comparable with any
figure computed elsewhere in this project on a different timeframe.**

---

## 1. WHY THIS TEST IS WORTH RUNNING

The payoff half of the whole weekly thesis is one phrase:

> *"Their goal is to tie up your margin, charge you swap or interest, and **move away from you
> in a unidirectional swing for the rest of the week**."* V02 `[00:14:37]`

Everything the method promises after the anchor — the hold, the target, the swing-trade option
— assumes the remainder of the week travels **in one direction**. That word is measurable
without any of the blocked vocabulary: directional efficiency is `|net movement| ÷ path length`,
and it needs a start point, an end point and the bars in between.

The instructor also supplies the counter-example himself, which is what makes this test fair
rather than rhetorical:

> *"Net change for the week zero… the dealer starts on ends on Friday where he started on
> Sunday"* V03 `[00:33:36]`; *"Very little profit seen on swing trades. Well, very little none.
> How about that? None"* `[00:34:15]`

So the course's own position is *usually unidirectional, sometimes net-zero*. **The question is
the proportion**, and nobody has measured it.

---

## 2. THE QUESTION

> After the week's extreme prints, is the remainder of the week more directionally efficient
> than a matched span of the same length elsewhere?

Null hypothesis: **it is not.** Post-extreme efficiency matches what any equal-length span
delivers.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN `W-C′` WAS READ

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | **15-minute** — and the path sum is defined on it (§0b) |
| **Window** | **`W-C′` — 2013-01-06 → 2016-06-30** |
| **Block (data split)** | **DEVELOPMENT, confirmed.** `W-C′` **is** `D-035`'s DEVELOPMENT block |
| **Data source** | **HistData GBP/USD M1 CSV corpus** (`D-036a`), `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 in `raw/SHA256SUMS.txt`; aggregated by `scripts/aggregate_m15.py` per `D-031` arm |
| **Week open** | **22:00 UTC — Sunday 17:00, fixed UTC−5, no DST** (`D-036a`, QA `C7`). **NOT FXCM's 21:00 UTC.** The week's open price for the net-zero metric is the **first bar at or after the realised week open** |
| **Data-QA gate** | **Precondition.** `scripts/qa_histdata_m1.py`; `QA_REPORT.txt`; `C1`–`C4` PASS, `C5`–`C8` signed off in `D-036a`. Cited in the observation |
| Measurement rule | `E06` restated for a CSV corpus (`COMMON_PROTOCOL.md` §2) |
| Timezone | **Both `D-031` arms.** Arm A = corpus stamps verbatim; Arm B = +1h during US DST |
| Anchor | The timestamp of the week's high **or** low, **whichever the week's net direction runs away from**. Both are computed; the choice rule is stated here and **not decided per week** |
| Metric — **efficiency** | `\|close(week end) − price(anchor)\| ÷ Σ\|bar-to-bar movement\|` over the post-anchor **15-minute** bars, in `[0,1]` |
| Metric — **monotonicity** | Largest counter-directional retracement after the anchor, in pips and as a share of the total move |
| Metric — **net-zero weeks** | Share of weeks whose **Friday close** sits within **±25 pips** of the **Sunday 17:00 week open** — V03's own counter-case, counted rather than asserted. ±25 pips is a **distance** and travels across vendors |
| Post-hoc anchor, disclosed | The anchor is only knowable **after** the week ends. **This test is retrospective by construction and is therefore `DESCRIPTIVE` about structure, never a trading result.** It is labelled so in every report |
| Excluded weeks | **None.** Holiday-shortened weeks retained and reported separately |
| **Sample** | **180 TRADING weeks** — denominated in **trading weeks present in the corpus with an observable week open**, not calendar weeks. The 182nd week-open (2016-06-26) is truncated by the DEVELOPMENT boundary, has no Friday close, and is **excluded, counted and reported**; the **2014-06-01** data hole is **excluded by name** (§3a) |

**The retrospective-anchor disclosure is load-bearing.** A trader cannot know on Wednesday that
Wednesday's high is the week's high. This test measures whether the *structure* the course
describes exists; it does not and cannot show that it is tradeable. Any report that elides that
is `E14` at the level of the whole test.

### 3a. THE WEEK CENSUS, THE `C8` DISPOSITIONS, AND THE HONEST SAMPLE

**The first draft of this file counted calendar Sundays and called them week opens. That was
wrong.** Against the corpus's own census (QA `C7`, `C8`):

| Quantity | Count | Source |
|---|---|---|
| Calendar Sundays in `W-C′` (2013-01-06 … 2016-06-26) | **182** | calendar arithmetic |
| Calendar weeks complete Sun→Fri inside the window | **181** | the 182nd (2016-06-26) is truncated by the DEVELOPMENT boundary |
| **Week opens the corpus actually contains in `W-C′`** | **186** | `C7` (187 corpus-wide, less the Tue 2013-01-01 corpus start) |
| — opening on a **Sunday** | **181** | `C7` |
| — opening on another weekday | **5** | `C7` |
| **TRADING weeks used by this test** | **180** | 181 complete weeks, less the **2014-06-01** data hole |

**Two facts a naive reading of `C7` gets backwards:**

1. **Four of the five irregular opens are NOT week starts.** `C7`'s detector emits the first bar
   after any gap ≥ 12 h, so a mid-week holiday **re-open** looks like a week open.
   `2013-12-26 Thu`, `2014-01-01 Wed`, `2014-12-25 Thu` and `2015-01-01 Thu` sit **inside** weeks
   that opened normally on Sunday. **A run session taking week boundaries from `C7` would split
   those weeks and compute directional efficiency over half-weeks** — and a shorter span is
   mechanically more efficient, so the error would manufacture support for the claim under test.
   Pre-registered: **a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open
   is never a week boundary.**
2. **The fifth, `2014-06-02 Mon 15:01`, IS a week start — and it is a data defect.** Zero bars
   for `2014-06-01 Sun` (nominal ~420), **521 of 1,440** for `2014-06-02 Mon`: **~22 continuous
   hours missing**. `C8` marks it `*** ABSENT AND UNEXPLAINED ***`.

**`C8` dispositions — pre-registered, by name.** Eleven flagged sessions fall into **seven
weeks** inside `W-C′`, and the disposition is **not uniform**:

| Week (Sunday) | `C8`-flagged sessions | Kind | **Disposition for this test** |
|---|---|---|---|
| 2013-12-22 | Wed 2013-12-25 (0) | market closure | **INCLUDE, report separately** |
| 2013-12-29 | Wed 2014-01-01 (392) | market closure | **INCLUDE, report separately** |
| **2014-06-01** | **Sun (0), Mon (521)** | **DATA DEFECT** | **EXCLUDE BY NAME** |
| 2014-12-21 | Wed 2014-12-24 (840), Thu 2014-12-25 (360) | market closure | **INCLUDE, report separately** |
| 2014-12-28 | Thu 2015-01-01 (424) | market closure | **INCLUDE, report separately** |
| 2015-12-20 | Thu 2015-12-24 (840), Fri 2015-12-25 (0) | market closure | **INCLUDE, report separately** — **week ends Thursday**; the net-zero metric uses the **realised** last bar, never a nominal Friday close |
| 2015-12-27 | Fri 2016-01-01 (0) | market closure | **INCLUDE, report separately** — **week ends Thursday** |

*(The eleventh, `2013-01-01 Tue`, lies **outside** `W-C′`. Not applicable.)*

**Why the six holiday weeks are INCLUDED.** `PT-011` inherited *"Excluded weeks: None"* from the
batch and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation for being
unrepresentative (`E09`). A real closure **is** market structure: a week that trades four days
and travels in one direction is exactly the phenomenon V02 describes, and removing it would be
selecting on the outcome. **Re-deciding this after a QA check surfaced them would be the
suit-the-result choice the gate exists to prevent.** The two Thursday-ending weeks are reported
separately with their realised span length, because §0b makes span length load-bearing.

**Why 2014-06-01 is EXCLUDED, and why that is not `E09`.** `E09` forbids excluding an
observation for **what the market did**. This is excluded because **the corpus does not contain
what the market did** — and this test is the one where that does the most damage: the efficiency
denominator is a **path length summed over 15-minute bars**, so 22 missing hours silently shorten
the path and **inflate** efficiency, while the week's extreme may itself lie in the hole. A
defect that biases the headline metric toward the claim under test cannot be included.
**Mechanical, by name, counted.**

**The honest sample:**

| Quantity | `W-C` (original) | **`W-C′` (this file)** |
|---|---|---|
| Calendar span, inclusive | 1,819 days | **1,272 days** |
| Calendar-complete Sun→Fri weeks | 260 | **181** |
| **TRADING weeks used** | 260 | **180** |

**`n = 180` clears `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 by a factor of six for the
efficiency and monotonicity distributions.** Neither headline metric is marginal.

**The one metric that can go marginal is the net-zero share**, and it is a *count of a subset*,
not a distribution: if fewer than 30 weeks close within ±25 pips of their open, the **share is
still reportable** (it is a proportion over n = 180) but **any statement about what net-zero
weeks look like** — their efficiency, their anchor weekday, their range — is computed on that
subset and **carries `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` in the same
sentence**. Pre-registered here so it cannot be renegotiated at run time. The original file
anticipated *"say >25%"* as a discussion threshold; **that number is a discussion aid, not a
decision rule, and it is not treated as one.**

> **`C8` DID NOT EXIST WHEN THIS FILE WAS FIRST WRITTEN.** The session-completeness check was
> added to `06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` **after** this pre-registration was
> drafted, and it is what surfaced the 2014-06-01 hole — which `C6` had excluded by
> construction (it skips anything ≥ 12 h as "the weekend") and `C7` had rendered cosmetic (it
> surfaced as a decorative **Monday** entry in a weekday tally). §3a above is the **correction
> that check forced**, made **before any bar in `W-C′` was read**.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary — the natural control** | Efficiency over **equal-length spans anchored at a random bar** in the same week, 1,000 draws, seed `20260812`. Same week, same volatility, same length; only the anchor changes |
| **Second** | Efficiency over equal-length spans anchored at the **extreme of a randomly chosen other week's relative position** — controls for the mechanical fact that any span starting at a local extreme has elevated efficiency by construction |
| **Third** | **N3 — week-anchor shift**, 1,000 draws, seed `20260812` |

The second arm is the one that matters. *A span beginning at an extreme is directional almost by
definition* — that is arithmetic, not market-maker behaviour, and a test that skipped this
control would confirm the thesis every time.

Baselines are run **before** the observed efficiency distribution is read.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Post-extreme efficiency exceeds **all three** controls | Genuine support for the unidirectional claim, beyond the extreme-anchoring artifact |
| Exceeds arm 1 but not arm 2 | **The claim is an artifact of anchoring at an extreme.** The most likely outcome and the most valuable one to establish early |
| Net-zero weeks are common | V03's counter-case is not rare, and any swing-hold instruction inherits that base rate. **Report the share prominently either way**, with §3a's subset caveat where it applies |
| Arms A and B diverge | Report both; the anchor bar can move by an hour between arms |
| Efficiency is high but the figure is quoted without its bar size | **Not a result — a defect.** §0b makes the resolution a required parameter |

## 6. MANDATORY SCOPE STATEMENT

> **PT-029 measures directional efficiency after a *retrospectively identified* weekly
> extreme.** It is **not** a trading test, **not** a test of the anchor point (`A-001`), and it
> adopts **no** day count (`C-001` untouched). It cannot support any claim that the post-extreme
> run is capturable in real time, because its anchor is unknowable in real time.
>
> It **re-issues `PT-011`** onto `W-C′` under `D-035`; `PT-011` is retained, marked and never
> run, and no result here may be reported as `PT-011`'s result.
>
> **Price levels on this corpus are not comparable with the V02–V06 FXCM homework** (`D-036a`);
> only shape and distance claims travel — which, for this test, is all of them. **Efficiency is
> resolution-dependent and is reported with its bar size** (§0b). The **week open is 22:00
> UTC**, not FXCM's 21:00 UTC.

## 7. TO RUN THIS

1. **Run the QA gate first**; confirm `C1`–`C4` PASS; cite `QA_REPORT.txt`.
2. Build **both** `D-031` arms with `aggregate_m15.py`; record row counts and spans.
3. Confirm the window is `2013-01-06 → 2016-06-30`, wholly inside DEVELOPMENT. **Read nothing
   past 2016-06-30.** Record which `D-031` clock the boundary was applied in (`I-010` Q2, OPEN).
4. Derive week boundaries from the **22:00 UTC / 17:00-local** week open by timestamp lookup —
   **never from `C7`'s open list** (§3a.1). **Apply §3a's dispositions by name**: exclude the
   week of **2014-06-01**; include and report separately the six Dec/Jan holiday weeks, using
   the **realised** last bar as the week close for **2015-12-20** and **2015-12-27**.
5. Compute the three controls **before** the observed efficiency distribution.
6. **Report the net-zero share in the headline, not the appendix.**
7. Report **both** `D-031` arms and the **bar resolution** with every efficiency figure.
8. Report the five largest-range weeks as the pre-registered sensitivity appendix.
9. Write `BT_V02_NNNN.md` from the template, §0 referencing **this file and `PT-011`**,
   classified `DESCRIPTIVE` per §3.
10. **Neither this file nor `PT-011` is ever edited to match what was found.**
