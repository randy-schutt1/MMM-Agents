# PROPOSED DECISION TEXT — THE `D-035` RE-ISSUE, AND A DEFECT IN `D-035`'s CONFORMANCE TABLE

```text
STATUS:   PROPOSED — NOT A DECISION. NOT BINDING. AWAITING OWNER INTEGRATION.
WRITTEN:  2026-08-13
BY:       the session that executed D-035's re-issue obligation.
WHY THIS FILE EXISTS: this session was instructed not to edit 00_SYSTEM/DECISIONS.md or
          00_SYSTEM/SETUP_ISSUES.md, and a concurrent session shares this working tree
          (SETUP_ISSUES.md I-009). The work below IMPLIES a decision entry and a
          correction to an existing one. Both are written out here, in DECISIONS.md's
          own format, for the owner to paste, renumber or reject.
SCOPE:    This file records TWO things: (1) the executed re-issue of eight
          non-conforming tests; (2) a DEFECT in D-035's own conformance table, found by
          reading the PT files rather than the table. The defect is the reason the
          obligation was eight tests and not seven.
NUMBERING: D-037 is proposed because D-036a is the highest existing entry. The owner may
          renumber freely; nothing in the PT files depends on the number, only on the
          content.
```

---

## PART 1 — WHAT WAS FOUND, BEFORE THE PROPOSED TEXT

### 1.1 The defect, stated plainly and verifiably

`D-035` consequence 1 reads:

> *"**`W-A` and `W-B` lie wholly inside DEVELOPMENT.** ✅ `PT-002`…`PT-007`, `PT-014`–`PT-018`,
> `PT-020`, `PT-021` and `PT-001` conform on the boundary test."*

**`PT-002` does not conform.** Its own pre-registration, `PT-002` §3, declares **two** windows:

> `| Windows | **W-A** (2015-01-04 → 2015-12-31) for daily extremes; **W-C** (2013-01-06 →
> 2017-12-29) for weekly extremes |`

and `PRE_REGISTERED/INDEX.md` §1 has recorded `PT-002`'s window as **"W-A, W-C"** since the
batch was written on 2026-08-12. `PT-002` §7 step 1 says *"confirm the window**s** sit inside
DEVELOPMENT"*, plural. Its attestation line says *"No chart in **W-A or W-C** was opened"*.

**The `W-C` arm straddles the pinned boundary by 546 days, exactly as the seven named tests
do.** `D-035` classified the file by its first window and missed its second, so the re-issue
obligation it created was **one test short**.

**Verification method, so this is checkable rather than asserted:** every `PT` file in
`06_MANUAL_BACKTEST/PRE_REGISTERED/` was searched for `W-C` and for the literal string
`2017-12-29`. The hits are `PT-002`, `PT-008`, `PT-009`, `PT-010`, `PT-011`, `PT-012`,
`PT-013`, `PT-019` — **eight files, not seven.** No other file in the batch references either.

**This is a bookkeeping defect, not a methodological one.** `D-035`'s split, its arithmetic,
its rationale and its rejection of *"pinning the boundary so that W-C fits"* are all unaffected
and are **not** proposed for change. What is wrong is one row of one table, and the fix is an
append in the style `D-028` and `D-019` already use — the superseded text retained, the
correction recorded beneath it.

### 1.2 What was executed

Eight non-conforming tests re-issued under new `PT` numbers onto **`W-C′` = 2013-01-06 →
2016-06-30**, assigned deterministically in ascending order of the original number:

| Original | Status now | Re-issued as |
|---|---|---|
| `PT-002` (**W-C arm only**; its W-A arm conforms and stays runnable) | **PARTIALLY NON-CONFORMING** — marked | **`PT-025`** |
| `PT-008` | NON-CONFORMING — marked | **`PT-026`** |
| `PT-009` | NON-CONFORMING — marked | **`PT-027`** |
| `PT-010` | NON-CONFORMING — marked | **`PT-028`** |
| `PT-011` | NON-CONFORMING — marked | **`PT-029`** |
| `PT-012` | NON-CONFORMING — marked | **`PT-030`** |
| `PT-013` | NON-CONFORMING — marked | **`PT-031`** |
| `PT-019` | NON-CONFORMING — marked | **`PT-032`** |

**No original was edited except its status block.** None has ever been run. The marking follows
the `PT-022` precedent exactly: new status block on top, reason stated, original status block
retained verbatim beneath a `--- original status block ---` rule.

### 1.3 What is OWED and was NOT done, because this session does not own the files

| File | What it needs | Why not done here |
|---|---|---|
| `00_SYSTEM/DECISIONS.md` | `D-037` (Part 2) + the `D-035` append (Part 3) | Session instructed not to edit it |
| `00_SYSTEM/SETUP_ISSUES.md` | nothing required; `I-010` Q1/Q2 remain OPEN and are cited by every new file | Session instructed not to edit it |
| `PRE_REGISTERED/COMMON_PROTOCOL.md` | §3a should state `W-C′`'s **definition and honest week count — 180 TRADING weeks**, not 182 calendar Sundays — as a first-class window beside W-A/W-B; §1's *"`PT-008`–`PT-013` and `PT-019` must state 22:00 UTC"* row should add **`PT-002`/`PT-025`** and the eight new numbers; §1's Data-QA row should be extended from `C5`–`C7` to **`C5`–`C8`** | **Shared file owned by another agent this session.** Flagged, not touched |
| `06_MANUAL_BACKTEST/datasets/README.md` | Its *"Notes"* still say *"only 3 intra-week gaps ≥ 30 minutes"* and **187 week opens detected** with no mention of the 2014-06-01 hole. `C8` now contradicts the implied completeness | **Not in this session's ownership.** Flagged, not touched |
| `00_SYSTEM/COURSE_PROGRESS.md`, `CHANGELOG.md`, `LOG.md` | the usual bookkeeping | Out of scope for this session |

---

## PART 2 — PROPOSED NEW ENTRY

*(Paste into `00_SYSTEM/DECISIONS.md` after `D-036a`. Renumber at will.)*

---

## D-037 — `D-035`'s re-issue obligation is EXECUTED, and its conformance table was defective: the count is EIGHT, not seven

**Date:** 2026-08-13
**Executes:** `D-035` consequence 2, which recorded a re-issue obligation and explicitly
declined to discharge it (*"This session does not re-issue them; it records the defect"*).
**Corrects:** `D-035` consequence 1, which listed `PT-002` as conforming.
**Governs:** `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-025` … `PT-032`.
**`D-035` is NOT superseded.** Its split, its arithmetic and its reasoning stand unchanged. One
row of one table is corrected by append, in the manner of `D-028`'s and `D-019`'s appends.

**Decision:** The eight `PT` tests whose pre-registered window `W-C` (`2013-01-06 →
2017-12-29`) straddles the `D-035` boundary are **re-issued under new `PT` numbers onto
`W-C′` = `2013-01-06 → 2016-06-30`**, which is `D-035`'s DEVELOPMENT block exactly. The
originals are **retained, marked and never run**; **none was edited into conformance.**

| Original | Question | Re-issued as | `W-C′` sample |
|---|---|---|---|
| `PT-002` **(W-C arm only)** | Do turning points cluster at the six printed boundaries? | **`PT-025`** | **180** weeks × 2 extremes = **360** |
| `PT-008` | "The dealer must cut" the first-eight-hours range | **`PT-026`** | **180** weeks |
| `PT-009` | Does the first move out of the opening range reverse? | **`PT-027`** | **≤ 180** weeks |
| `PT-010` | On which weekday does the week make its high and low? | **`PT-028`** | **180** weeks — **two cells below n = 30** |
| `PT-011` | Is the rest of the week a unidirectional swing? | **`PT-029`** | **180** weeks |
| `PT-012` | Previous week's extreme as barrier | **`PT-030`** | **178** weeks × 2 barriers = **356** |
| `PT-013` | Are Sunday and Monday the accumulation phase? | **`PT-031`** | **180** / **180** / **179** by arm |
| `PT-019` | The weekend gap and the Friday-flat rule | **`PT-032`** | **180** gaps |

**Every `n` above is denominated in TRADING WEEKS PRESENT IN THE CORPUS, never in calendar
weeks** — see the census below, which is the correction that matters most in this entry.

**`PT-002` is the correction, and it is the important half of this entry.** `D-035` consequence
1 lists `PT-002` among the conforming tests. **It is not.** `PT-002` §3 pre-registers **two**
windows — `W-A` for daily extremes and **`W-C` for weekly extremes** — and `INDEX.md` §1 has
recorded it as *"W-A, W-C"* since 2026-08-12. Its `W-C` arm straddles the boundary by the same
546 days as the other seven. `D-035` classified the file by its first window; the search that
found the seven was for files *whose window is W-C*, not for files *that use W-C*.

**`PT-002` is therefore marked PARTIALLY non-conforming, not superseded.** Its `W-A` daily arm
conforms, is unblocked by `D-036a`, and **stays runnable in `PT-002` itself**. Only the weekly
arm moves to `PT-025`. Marking the whole file superseded would have destroyed a conforming test
to fix a bookkeeping error.

**Six substantive changes the re-issues carry, none of them cosmetic:**

0. **Every `n` is denominated in TRADING WEEKS PRESENT IN THE CORPUS, not calendar weeks**, and
   each file carries a **pre-registered `C8` disposition by name** for all seven flagged weeks
   in `W-C′`. `C8` — the session-completeness check — was **added to `qa_histdata_m1.py` after
   these files were drafted**, and it found a **~22-hour hole at 2014-06-01** that `C6` had
   excluded by construction and `C7` had rendered cosmetic. See the findings table below; this
   is the change with the largest effect on the reported numbers.

1. **The data source is the HistData M1 CSV corpus** (`D-036a`), not TradingView/FXCM. Every new
   file states the corpus path, its SHA-256 provenance, the `aggregate_m15.py` derivation, and
   the QA gate (`qa_histdata_m1.py` → `QA_REPORT.txt`) as a **precondition on the run**.
2. **The week open is 22:00 UTC** — Sunday 17:00, fixed UTC−5, no DST — **not FXCM's 21:00
   UTC.** Every one of these eight is a week-boundary test; this is the single most consequential
   substitution and `D-036a` requires it in writing.
3. **Both `D-031` arms are carried and both are always reported** — Arm A = corpus stamps
   verbatim (the corpus is natively UTC−5), Arm B = +1h during US DST.
4. **Price levels are not comparable with the V02–V06 FXCM homework**; only shape and distance
   claims travel (`D-036a`). Stated in every new file's scope statement.
5. **The EU referendum (2016-06-23) is inside `W-C′` and inside DEVELOPMENT** and is **not
   excluded**; the **October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase
   at all.** `COMMON_PROTOCOL.md` §3 disclosure 1's sensitivity appendix is carried in every new
   file and discharges only over what remains.

**Four honest sample findings, recorded because a shortened window is where numbers get
quietly rounded up:**

| Finding | Detail |
|---|---|
| **CALENDAR WEEKS ARE NOT TRADING WEEKS, and the first drafts confused them** | `W-C′` spans 1,272 days and holds **182 calendar Sundays** — but the corpus contains **186 week opens** in the window, of which only **181 open on a Sunday** and **5 do not**. **Four of those five are mid-week holiday RE-OPENS, not week starts**: `C7`'s detector emits the first bar after any gap ≥ 12 h, so a Christmas re-open is indistinguishable from a week open in that tally, and a run session taking week boundaries from it **would split four weeks in two**. Every re-issue now states: **a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open is never a week boundary.** |
| **THE DATA HOLE — the fifth irregular open** | `2014-06-02 Mon 15:01` **is** a week start, and it is a **defect**: the corpus holds **zero bars** for `2014-06-01 Sun` (nominal ~420) and **521 of 1,440** for `2014-06-02 Mon` — **~22 continuous hours absent, covering the entire week open.** It is the **only unexplained hole in 3.5 years**. **Excluded by name from all eight re-issues, counted in every reported `n`.** |
| **The headline `n` is 180, not 181 and not ~260** | 182 calendar Sundays → **181** calendar-complete Sun→Fri weeks (the 182nd, opening 2016-06-26, is truncated by the boundary) → **180 trading weeks** after the data hole. `W-C` would have given **260** — its last Sunday, 2017-12-24, closes exactly on the window's final day. **A 30.8% loss, and every new file states its own number rather than inheriting "~260".** |
| **`PT-030` loses TWO weeks, and the second is not reported by any check** | The week of **2014-06-08** inherits the defect: its barrier **is** the holed week's high and low — a **systematically too-narrow barrier** that would look easier to breach. `n = 178` tested weeks × 2 barriers = **356**. |
| **`PT-032` would have FABRICATED its headline observation** | Applied mechanically, the `2014-05-30 → 2014-06-02` "weekend gap" spans **~22 hours of data the corpus does not contain**. It would be large, land in the tail and the `> 50 pip` bucket, and very likely appear in the five-largest-gaps appendix — **an artifact of absent data on the one test whose finding is gap size.** **Excluded by name.** |
| **`PT-028` goes marginal in two cells** | The trading week is **120 hours and not five equal days** — Sunday **7 h**, Mon–Thu **24 h**, Friday **17 h**. Under the exposure-weighted null at **180 trading weeks** the expected counts are **Sunday ≈ 10.5** and **Friday ≈ 25.5**, both **below `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30**. These are **equal-week upper bounds**: two included holiday weeks carry **zero Friday exposure**, so the realised Friday figure is lower still and the verdict is robust in the direction that matters. Sunday was already marginal at `W-C` (≈ 15.2 over 260 weeks); **Friday was not (≈ 36.8) and now is.** Both carry `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`. The focal Tue/Wed prediction is unaffected. **Correcting calendar → trading weeks moved these figures by less than one observation and changed no verdict; the inputs are now right.** |
| **`PT-028`'s joint table cannot carry inference** | Measure 3's 6 × 6 weekday table averages **5.0 observations per cell** at n = 180. **No χ² or p-value may be quoted for it**; it is printed as a raw count matrix, and the inferential summary is the **sign of `high_day − low_day`** at n = 180. |
| **`C8` dispositions are pre-registered and NOT uniform** | `QA_REPORT.txt`'s gate requires an explicit **pre-registered** disposition for every `C8`-flagged session. Eleven flagged sessions fall into **seven weeks** inside `W-C′`: **six Dec/Jan market closures → INCLUDE, report separately**; **one data hole → EXCLUDE by name**. The include disposition is **inherited, not newly chosen** — the originals already carried *"Excluded weeks: None; holiday-shortened weeks retained and reported separately"* and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation as unrepresentative (`E09`). **Re-deciding it after a QA check surfaced them would be precisely the suit-the-result choice the gate exists to prevent.** Two of the six (`2015-12-20`, `2015-12-27`) **end on Thursday**, which shortens every censoring horizon and, in `PT-032`, produces two **genuine ≥ 72 h closure gaps** that are retained and flagged with their realised duration. |
| **The `E09` line, drawn explicitly** | `E09` forbids excluding an observation because of **what the market did**. The 2014-06-01 exclusion is because **the corpus does not contain what the market did**. That distinction is the entire reason `C8` was written, and it is stated in every affected file so no later reader mistakes a data-integrity exclusion for a convenience one. |
| **Subset cells across the batch** | `PT-027`'s second-breach control, `PT-030`'s breached/un-breached partition and its four-way direction × breach cells, `PT-031`'s extreme-inside-span complement, and `PT-032`'s >18 / >50 pip tails all have run-time-unknown counts. **Each new file pre-registers the `n < 30` label rather than leaving it to be negotiated after the number is seen.** |

**Three vendor-induced substantive changes that are findings in their own right:**

1. **`PT-026`: *"the first eight hours"* and *"the first two 4-hour bars"* are no longer the same
   span.** On FXCM's 16:00-local week open they coincided exactly. On this corpus's 17:00 open,
   midnight-anchored 4-hour buckets give **7 hours** in Arm A and **6** in Arm B, against 8 by
   clock. **Both readings are the instructor's own, in two lessons.** `D-030` forbids picking
   one, so `PT-026` **reports both and adopts neither**, with the 12-hour arm carried over.
2. **`PT-031`: *"Sunday + Monday"* is 31 hours, not two days**, against 48-hour controls. A raw
   range comparison is rigged by arithmetic alone, so the **length-normalised comparison is
   promoted to headline**. `PT-013` §3a's conditional also **resolves**: this corpus **does**
   print Sunday bars, so the Sunday-alone arm **runs** — at 7 hours.
3. **`PT-032`: the original's primary control does not survive.** This corpus trades continuously
   Sunday 17:00 → Friday 17:00 (QA `C6`: **three** intra-week gaps ≥ 30 m in 3.5 years), so
   *"intra-week daily-boundary gaps"* **do not exist on it**. The control is **retained,
   relabelled** as the bar-to-bar change across the 17:00 instant on Mon–Thu, declared a **floor
   rather than a matched comparator**, and the **N3 shifted-boundary sanity control is promoted
   to co-primary** because it is now the only control that separates a real discontinuity from a
   harvest defect. `PT-032` also declares that its bid-only gaps are a **lower bound** on
   execution risk — a measurement error that runs **in favour** of the instructor's rationale,
   and therefore stated before the result.

**Reason:** `D-035` created a re-issue obligation and left it undischarged; leaving it open meant
seven — in fact eight — tests that could not be run without either opening the holdout or
editing a pre-registration to fit, both of which `D-027` forbids. Discharging it now, while
nothing has been run and no result exists, is the only time it is free. The `PT-002` correction
is recorded rather than silently absorbed because **a conformance table that is wrong in one row
will be trusted in all of them** by the next session that reads it.
**Evidence:** `PT-002` §3, §7, attestation line (two windows declared);
`PRE_REGISTERED/INDEX.md` §1 (window recorded as *"W-A, W-C"*); `PT-008`, `PT-009`, `PT-010`,
`PT-011`, `PT-012`, `PT-013`, `PT-019` §3 (window `W-C`); a repository search of
`PRE_REGISTERED/` for `W-C` and `2017-12-29` returning exactly those eight files;
`COMMON_PROTOCOL.md` §3, §3a; `D-027`, `D-028`, `D-030`, `D-031`, `D-035`, `D-036`, `D-036a`;
`datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt` (`C6` gap census, `C7` week-open census);
`scripts/aggregate_m15.py` (bucket anchoring, arm derivation); `PT-022`/`PT-023` (the marking
and re-issue precedent this follows). Week counts are **calendar arithmetic over the window's
dates**; **no price was read from the corpus by the session that wrote these files.**
**Alternatives considered:** *Re-issuing only the seven `D-035` named and leaving `PT-002` for a
later session* — rejected; the defect was found while doing the work, and a known-wrong
conformance table left standing is worse than the original omission. *Marking `PT-002` wholly
superseded* — rejected; its `W-A` arm conforms and is runnable, and destroying a conforming test
to tidy a table is a net loss. *Editing `W-C` to `W-C′` in the seven originals* — rejected
outright; `D-027` requires a new test ID and a retained original, and this is the exact failure
mode the retention rule exists to prevent. *Re-issuing onto a window chosen to restore n ≈ 260
(e.g. starting in 2011)* — rejected; the windows were fixed on calendar grounds before any chart
existed (`COMMON_PROTOCOL.md` §3), and re-cutting one to recover sample size is choosing a period
for its size, which is the selection pressure `D-027` exists to remove. *Keeping the calendar
count because it is simpler, or because it happened to land near the right number* — rejected;
`n = 181` from calendar arithmetic and `n = 181` calendar-complete weeks agreed **by
coincidence**, and the correct trading-week figure is **180**. *Leaving the `C8` dispositions to
the run session* — rejected outright; that is the one choice that would certainly be made to
suit whatever the result looked like, and `QA_REPORT.txt`'s own gate line now forbids it.
*Rounding 180 up to
"~180" or "about 260 as before"* — rejected; the sample loss is the price of the pin and is
reported as such.
**Consequences:** `PT-025`…`PT-032` are pre-registered and **runnable** — `D-036a` supplies their
data, `D-035` supplies their window, and no blocker remains for them. `PT-002` is runnable **on
its W-A arm only**. `PT-008`–`PT-013` and `PT-019` are **permanently retired unrun** and must
never be run; any future session finding them must read their status block first.
`COMMON_PROTOCOL.md` §3a should record `W-C′` as a first-class window with its **180-trading-week**
count (182 calendar Sundays, 181 observable Sunday opens, less the 2014-06-01 hole),
and §1's 22:00 UTC row should name the eight new numbers — **owed, not done in the session that
wrote this text.** `validate_project.py` may now check that no observation cites `PT-008`–
`PT-013`, `PT-019`, or `PT-002`'s W-C arm.
**Status:** ACTIVE

---

## PART 3 — PROPOSED APPEND TO `D-035`

*(Paste at the end of `D-035`, before the `---` that closes it. `D-035` is **not** superseded and
its existing text is **not** edited — this is the same append pattern `D-028` uses.)*

---

> ### APPENDED 2026-08-13 — THE CONFORMANCE TABLE ABOVE IS DEFECTIVE IN ONE ROW: `PT-002`
>
> Consequence 1 lists **`PT-002`** among the tests that *"conform on the boundary test"*. **It
> does not.** `PT-002` §3 pre-registers **two** windows — *"**W-A** (2015-01-04 → 2015-12-31)
> for daily extremes; **W-C** (2013-01-06 → 2017-12-29) for weekly extremes"* — and
> `PRE_REGISTERED/INDEX.md` §1 has recorded it as *"W-A, W-C"* since the batch was written. Its
> **`W-C` arm straddles this boundary by the same 546 days** as the seven named in consequence 2.
> The classification error was to file the test by its **first** window.
>
> **The corrected count is EIGHT, not seven**: `PT-002` (W-C arm), `PT-008`, `PT-009`, `PT-010`,
> `PT-011`, `PT-012`, `PT-013`, `PT-019`.
>
> **Nothing else in this entry changes.** The 2016-07-01 pin, the 1,272 / 546-day arithmetic, the
> `W-A`/`W-B` verdicts, the event split and the rejection of *"pinning the boundary so that W-C
> fits wholly inside DEVELOPMENT"* are all unaffected. The defective row is **retained above**
> rather than corrected away, because it is what the re-issue session worked against.
>
> **`PT-002` is marked PARTIALLY non-conforming, not superseded**: its `W-A` daily arm conforms,
> is unblocked by `D-036a`, and stays runnable in `PT-002` itself. Only its weekly arm is
> re-issued, as **`PT-025`**.
>
> The obligation this entry created is **discharged by `D-037`**, which re-issues all eight onto
> `W-C′` = 2013-01-06 → 2016-06-30 as `PT-025` … `PT-032`.

---

## PART 4 — WHAT THE OWNER SHOULD DECIDE, IF ANYTHING

Nothing in Parts 2 and 3 requires a new judgement — they record executed work and correct a
factual row. **Two items already open elsewhere touch these files and are the owner's:**

1. **`I-010` Q2 — which `D-031` arm's clock the `D-035` boundary is expressed in.** Every new
   file instructs the run session to **record** the convention used and **not to decide it**.
   Four Arm-B bars sit at wall-clock 2016-07-01. One line appended to `D-035` closes it.
2. **`I-010` Q1 — whether FXCM's 21:00 UTC week open is a year-round constant or a summer
   artifact.** Until it is closed, **no block, barrier or gap measured on this corpus may be
   compared with an FXCM-sourced one**, because the two grids may differ by an hour for part of
   the year. `PT-026` §3a states this explicitly.

Neither blocks `PT-025`…`PT-032` from running.
