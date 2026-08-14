# V11 — HOMEWORK

**Lesson:** V11 · `Bootcamp1 Wk4 040812 Part1 (51mins).swf` · 2012-04-08 · course author, 100%
**Assignments source:** `03_LESSON_NOTES/V11_SOURCE_NOTES.md` §12, taken from the transcript before
the screenshot pass.

## ⚠ THE HEADLINE FACT ABOUT THIS LESSON'S HOMEWORK

**V11 announces a week-4 assignment and does not give it.**

> `[00:00:46]`–`[00:00:51]` — *"Make an honest effort to do the assignments. **We got a really good
> assignment coming up this week**… I'm gonna **insist** that you do it. It's good, it's a good
> one."*

The lesson then runs 50 more minutes and **ends mid-sentence** at `[00:50:56]` on a divergence
chart, with no assignment given. **This is Part 1 of a two-part session** — `SOURCE_MANIFEST.md`
V12 is `Bootcamp1 Wk4 040812 Part2 (55mins).swf`, **same date**.

**No assignment is inferred, reconstructed, or carried over from another week.** The promise is
recorded; the content is not invented. This is the `Q-012` failure mode in miniature and the
temptation is real, because a "week 4 assignment" is exactly the kind of thing a session could
confabulate plausibly.

## DISPOSITIONS — `D-018` / `D-019`

`D-019` binds: **`NOT APPLICABLE` means there is nothing here to do, ever, for this lesson.
`DEFERRED` means the work exists and is blocked.** The test is *"is there anything here to do at
all"*, not *"can this be done today"*.

| # | Item | Timestamp | Disposition |
|---|---|---|---|
| **H1** | *"two hours a week now looking at charts"* | `[00:00:38]` | **PERFORMED — see §1** |
| **H2** | Post research work in the forum; grade it against his posts/slides | `[00:01:48]` | **NOT APPLICABLE** |
| **H3** | **The flashcards** — do them; rip them up and re-do them if any shows one candle straight out of the box | `[00:14:46]`, `[00:16:58]` | **DEFERRED — blocked by `A-082`** |
| **H4** | Adopt the five `Trade Strong` commitments before every trade, live or demo | `[00:18:07]`–`[00:20:52]` | **PERFORMED IN PART — see §2** |
| **H5** | Post your bad trades — and good ones — on the board under your own name | `[00:19:52]` | **NOT APPLICABLE** |
| **H6** | ⭐ Open the RSI/TDI sub-graph full height and **scroll back fast** to watch the 80/40 ↔ 60/20 oscillation switch | `[00:40:56]`–`[00:41:18]` | **DEFERRED — blocked by `A-080`.** A bounded demonstration of the blocker was performed instead — §3 |

**Two `NOT APPLICABLE`, two `DEFERRED`, one `PERFORMED`, one `PERFORMED IN PART`.**

---

## 1. H1 — chart study

**PERFORMED.** This session performed substantially more than two hours of GBP/USD chart and data
work: 27 curated frames reviewed and named across 28 detected screen states, and `PT-039` run over
**894 session days / 26,028 candidate lows** of the `D-036a` corpus.

**Recorded honestly as a partial match to the assignment's intent.** His two hours are
*discretionary human chart-reading* — marking up a week and looking at it. This session's hours
were *programmatic measurement over a checksummed file*. **They are not the same activity**, and
claiming the assignment satisfied would over-state it. The work is real; the equivalence is not
asserted.

## 2. H4 — the `Trade Strong` commitments

**PERFORMED IN PART.**

The **artifact** half is done: the five commitments are transcribed verbatim from the printed slide
(frame `20:20`) **and** from the audio, and the print-vs-speech divergence on commitment 3 is
recorded as **`A-081`** (`V11_SOURCE_NOTES.md` §5.4). That is the part a research agent can do.

The **behavioural** half — *"before you take any trade, any trade at all, in your live account or
demo"* — is **NOT APPLICABLE**: no live account and no demo account exists in this project, and
`D-006` defers all execution to Phase 8. This follows the V01 H6/H7 precedent exactly (an
instruction whose subject is an account the project does not have).

| # | PRINTED, frame `20:20` | SPOKEN `[00:20:18]`–`[00:20:52]` |
|---|---|---|
| 1 | I will only take **Second leg** setups | same |
| 2 | I will only take **M or W outside the box** | same (+ *"dammit"*) |
| 3 | I will not **overleverage** my account | **+ *"I will not take a 25 risk on one trade"*** ⚠ `A-081` — no unit |
| 4 | I will **execute with clarity free of distraction** | same |
| 5 | I will **never lift my stops** | same |

## 3. ⭐ H6 — THE ONE NEW EXERCISE, AND WHY IT CANNOT BE PERFORMED AS SET

> `[00:40:56]`–`[00:41:18]` — *"a neat little trick to do is hit the … home key on your chart and
> **open up your TDI or RSI all the way, and then scroll through kind of fast** and you'll watch
> you'll see what it does… it almost looks like an EKG on the top part, EKG on the bottom part, and
> **you'll see it switching back and forth**"* — i.e. the 80/40 ↔ 60/20 switch of §4d.5.

**This is the only genuinely new, performable-sounding exercise the lesson sets. It is blocked.**

**Rendering any RSI requires choosing a lookback period, and the lesson does not state one**
(`A-080`). Neither does the Tier 2 seminar-notes PDF (`D-040` step 2, searched). **Choosing one to
make a blocked exercise runnable is precisely what `D-030` forbids** — and the trap is well-baited,
because the TDI's distributed default is 13 and `MMM-NOTES` p.38 lists a **13 EMA**, so a session
could reach *"13"* by conflating two different indicators and feel sourced doing it.

### What was done instead — a bounded demonstration of the blocker

`scripts/rsi_period_sensitivity.py` computes V11's **own printed statistics** at **six candidate
periods** and **adopts none**, on the `D-036a` corpus, `W-C′`, M15 (the timeframe `[00:31:39]`
names first). Output: `data/rsi_period_sensitivity_output.txt`, 86,536 bars.

| period | > 80 | < 20 | inside 70/30 | inside 80/40 | inside 60/20 |
|---|---|---|---|---|---|
| 5 | **5.66%** | **5.84%** | 69.09% | 63.32% | 63.76% |
| 9 | 1.72% | 1.81% | 83.93% | 74.18% | 74.86% |
| 13 | 0.74% | 0.78% | 89.90% | 79.33% | 80.35% |
| 14 | 0.60% | 0.65% | 90.88% | 80.28% | 81.30% |
| 21 | 0.16% | 0.20% | 95.02% | 84.76% | 85.88% |
| 34 | **0.04%** | **0.01%** | **98.20%** | 88.90% | 90.29% |

**The spread is the result:**

- *"Time above 80"* — V11's **overextended** condition, and half of the `[00:36:19]` composite
  entry — ranges from **0.04% to 5.66%** across the candidate periods. **A ratio of 144×.**
- *"Time below 20"* ranges **0.01% to 5.84%. A ratio of 561×.**
- Even the **adjacent** pair 13 vs 14 differs by 0.13 pp on a ~0.7% base — **roughly 20%
  relative.** That is the *floor* on how much `A-080` matters, not the ceiling.

**Read plainly: `A-080` is not a bookkeeping gap. The lesson's single most codable-looking
condition varies by two orders of magnitude depending on a number the lesson never states.**

### What §3 does NOT show — stated in the file and repeated here

- **It does not show which period the instructor used**, and **no period is adopted** here or in any
  V11 artifact.
- **It does not test any V11 claim.** The 80/40 ↔ 60/20 **switch** he asks students to watch for is
  a **regime-transition** claim; these are **unconditional occupancy fractions** and are a different
  statistic.
- **It does not close, narrow, or unblock `A-080`**, and it unblocks no `PT` test.
- **It does not license *"13 is close enough"*.** 13 is in the sweep precisely so that its distance
  from its neighbours is visible.

## 4. H2 / H5 — `NOT APPLICABLE`, and why that is a positive claim

`D-019`: `NOT APPLICABLE` asserts there is **no subject matter**, and the reviewer audits the claim.

- **H2** — the forum is the 2012 `marketmakersforex` member forum. It is not in the source library,
  no URL is given, and no archive is available. **There is nothing to post to, now or ever, for
  this lesson.** (Note this is *not* the same as H1's chart work, which is performable and was
  performed.)
- **H5** — the same board, plus it requires **trades taken under one's own name**, which requires an
  account the project does not have (`D-006`).

**Neither is merely blocked.** No future infrastructure makes a 2012 member forum postable to.

## 5. H3 — `DEFERRED`, not `NOT APPLICABLE`

The flashcards **have subject matter** — they are a real artifact the speaker says he possesses
(*"there is not one flashcard in my collection"* `[00:14:52]`) and that gates trading for the week
(`[00:16:58]`). **They are simply never specified** anywhere in V11: no count, no format, no
medium, no production instruction (**`A-082`**).

**`DEFERRED` under `D-019`**, and specifically blocked by a **definitional** gap, so `D-030`'s
*"wait for the lesson that defines it"* governs. **It discharges in whichever lesson specifies
them**, and V12 — same session, same day — is the first place to look.

---

## 6. DATA SOURCE — `D-034` / `D-036a`

| Field | Value |
|---|---|
| Corpus | **HistData.com GBP/USD M1** (`D-036a`), SHA-256 in `raw/SHA256SUMS.txt` |
| Window | **`W-C′` 2013-01-06 → 2016-06-30** — `D-035` DEVELOPMENT |
| Holdout | **NOT OPENED.** Not on disk; `assert_development` re-checked every slice |
| QA gate | `GATE: PASS — C1-C4 clean` (precondition) |
| Timeframe | **M15** for §3 (`[00:31:39]` names 15-minute first); **M1** for `PT-039` |
| Measurement | Every number parsed from a checksummed file. **No value read from any rendering** — `E06` as restated by `D-036a` |
| Level comparability | **NOT comparable with the V02–V06 FXCM homework** (`D-036a`). §3 reports occupancy fractions and `PT-039` reads no level at all, so neither is affected |

**No TradingView chart was opened for V11.** This is the first lesson whose homework runs entirely
on the CSV corpus, which is a change from V02–V06 and is recorded as such.

## 7. FILES

| Path | What |
|---|---|
| `scripts/rsi_period_sensitivity.py` | §3's demonstration. Committed before its output |
| `data/rsi_period_sensitivity_output.txt` | Its output |
| `../../06_MANUAL_BACKTEST/PRE_REGISTERED/PT-039_how_long_must_the_low_hold.md` | The pre-registration |
| `../../06_MANUAL_BACKTEST/V11/BT_V11_0001.md` | The observation |
