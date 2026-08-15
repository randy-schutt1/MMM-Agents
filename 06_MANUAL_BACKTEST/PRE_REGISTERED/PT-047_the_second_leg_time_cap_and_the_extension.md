# PT-047 — V19's "MUST CLOSE BACK BELOW WITHIN 30 MINUTES, OR HE EXTENDS 25 TO 50"

**Pre-registered:** 2026-08-14, by the V19 student session.
**Status at commit time:** ⚠️ **NO BAR HAS BEEN READ. NO RUNNER EXISTS.** This file is committed
**before** `run_pt047.py` is written, per `COMMON_PROTOCOL.md` §9 rule 7. **If the runner and this
file ever disagree, THIS FILE GOVERNS**, neither is edited, and the disagreement is reported in
`BT_V19_0001.md`.

---

## §1 — THE CLAIM UNDER TEST

V19's central rule, stated for the M at `[00:22:43]` and mirrored for the W at `[00:46:38]`,
**confirmed verbatim on an independent ASR engine**, and — uniquely in this corpus — **written into
the deck on camera** during the lesson (`04_SCREENSHOTS/V19/INDEX.md` frames `21:15` / `23:10` /
`23:25`):

> `[00:22:43]` *"The second leg rise | can be slightly above the first **but must close back below**
> | **within 30 minutes**."*

And the stated consequence of failing it, `[00:23:51]`–`[00:24:32]`, `[00:38:33]`, `[00:40:43]`:

> *"If he stays above the previous high … he is gonna extend that high to the next level strike zone
> **25 to 50** higher."* … *"if the deal[er] breaks above the level and sta[ys] above **he will
> extend. That's the rule.**"*

**The testable core, in one sentence:**

> After price exceeds an established level, **whether it closes back below that level within 30
> minutes** separates two populations: the ones that do should **roll off** the level, and the ones
> that do not should **extend 25–50 pips beyond it**.

⭐ **This is the rare V19 claim that is testable on price alone.** It needs no moving average, no
*"blue tracer"*, no TDI threshold and no nickname, so `D-030` does not block it. **Every other
V19 entry rule is blocked** (`V19_INTERPRETATION.md` §2.9).

### §1a — ⚠ WHAT THIS TEST DELIBERATELY DOES **NOT** TEST

* **It is not a strategy backtest and must not be cited as one.** No entry, exit, stop, target,
  position size or P&L is computed anywhere. It measures a **conditional excursion difference**.
* **It does not test the M or W formation.** Identifying an M would require the eight-bar count
  *and* the *"blue tracer"* confirmation, and the latter is undefined (`A-132`). **This test
  isolates the time-cap clause only**, which the lesson states as a standalone condition.
* **It does not test the `90%` figure at `[00:25:34]`.** `D-009` forbids optimising toward a
  claimed rate, and the lesson qualifies it out of testability at `[00:40:53]` (*"Is it hard and
  fast? No, he could correct"*).
* **It does not test the `high 80 percent` eight-bar figure at `[00:28:45]`.** That is a reported
  third-party manual count with no definition of *"successful"*, no sample size and no holdout —
  the course reporting an anecdote *about* a measurement. **Recorded in `Q-020` and
  `V19_INTERPRETATION.md` §2.3, and deliberately not reproduced.**

---

## §2 — ⚠⚠ THE PRE-REGISTERED WEAKNESSES, DECLARED BEFORE THE RUN

**Stated here, before any bar is read, rather than defended after the result.**

### (a) THE LESSON DOES NOT SETTLE ITS OWN TIME CAP

`30`, `30–45`, `45 tops`, and `30 minutes to an hour` all appear (`V19_SOURCE_NOTES.md` §5.2), and
**the two on-camera slide edits disagree with each other** — `30M` on the M slide, `30 to 45 m` on
the W slide (`C-029`). `[00:26:12]` ranks them: *"30 minutes is a good rule"*, and `[00:47:21]`
supplies the only exclusion: *"90 minutes is too long"*.

**DECISION, FIXED NOW: the primary test uses 30 minutes = 2 M15 bars**, because that is the figure
the instructor himself calls the rule and the figure written onto the M slide. **45 minutes (3 bars)
is run as a pre-declared robustness arm, NOT as an alternative primary.** ⚠ **A result that holds at
30 and fails at 45, or vice versa, is reported as fragile and is NOT reported as a confirmation.**

### (b) "THE LEVEL" IS NOT DEFINED BY THE LESSON AS AN ALGORITHM

V19 talks about *"the previous high"* and *"the high of the day"* while pointing at charts. **The
operationalisation in §3 is a DECLARED CONVENTION OF THIS TEST, not a reading of the lesson**, and
it is the single largest threat to validity here.

⭐ **What the lesson does supply, and what this test uses:** `[00:32:59]` *"bar one is the bar that
forms the high of the day"*, and `[00:41:32]` *"eight candles or greater … which is by the way two
hours"*. **The eight-bar separation in §3 is taken from the lesson; the rest of the level definition
is this test's convention.**

### (c) THE 15-MINUTE TIMEFRAME IS DERIVED, NOT STATED

`M15` appears **zero** times in V19. The bar size comes from `8 bars = 2 hours` ⇒ 15 minutes
(`V19_INTERPRETATION.md` §2.3). **This is a sound derivation from the course's own two numbers and
it is still a derivation.** No robustness arm on bar size is run, and that limitation is declared.

### (d) THE `25 to 50` FIGURE RESTS ON AN ASR CORRECTION

The committed transcript reads `25 to 55` at `[00:23:57]` and `[00:24:32]`, and `25 to 50` at
`[00:25:06]` and `[00:25:31]`. **An independent engine reads `50` at both disputed markers**
(`V19_TRANSCRIPT.md` §5 correction #2). **The band used below is `[25, 50]` pips.** ⚠ If a reviewer
overturns that correction the band becomes `[25, 55]`; **`O3` below is reported against both bands
so the verdict does not depend on the correction.**

### (e) SESSION CLOCK

V19 gives **one** clock reference — `[00:31:44]` *"at the Asian session at 3 30 in the morning"* —
**with no timezone.** ⚠ **Same class as open item 248.** This test therefore **never conditions on a
named session** and runs **both `D-031` timezone arms**; a result that appears on one arm only is
reported as arm-dependent and is not a confirmation.

---

## §3 — OPERATIONAL DEFINITIONS — FIXED NOW

Data: HistData GBP/USD M1, resampled to M15 by `mmm_lib.load_m15()`, arms **A** and **B**
(`D-031`), scope **DEVELOPMENT only** (`D-035`; the 2016-07-01 → 2016-12-31 holdout is sealed and
not on disk, and `assert_development()` re-checks every window).

Windows, pre-registered (`COMMON_PROTOCOL.md` §3): **`W-A`** (2015) as primary, **`W-B`**
(2014-01-05 → 2015-12-31) as the pre-declared out-of-window replication.

Session day, box and inclusion: `mmm_lib.build_days()` at `offset_min = 0`, `require_full = True`.
Days failing completeness are **excluded before any event is identified**, and the excluded count is
reported.

### The event

Within one session day's post-box bars (`03:00 → 17:00`, 56 M15 buckets):

1. Let `R(t)` be the running high of the day over bars strictly before `t`.
2. Let `a(t)` be the index of the bar that **set** `R(t)`.
3. ⭐ **EXCEED EVENT** at bar `t` iff **all** of:
   * `high(t) > R(t)` — the level is exceeded;
   * `t − a(t) ≥ 8` — the level is at least **eight bars** old (`[00:41:32]`);
   * `t − a(t) ≤ 24` — and no more than six hours old, so *"the high of the day"* is still the
     day's structure and not yesterday's residue. **This upper bound is this test's convention**
     (§2b) and is fixed here;
   * at least **16 bars** (4 h) of the same session day remain after `t`, so `O1` is measurable for
     every event without look-ahead truncation.
4. **`L` = `R(t)`**, the level, in price.
5. **Only the FIRST exceed event per session day is taken.** Multiple events within a day are
   serially dependent and would inflate `n` without adding information.

### The classifier — the clause under test

* **`CLOSED_BACK`** — `close(t+1) < L` **or** `close(t+2) < L`. *(30 minutes = the 2 bars after the
  exceeding bar. The exceeding bar itself is excluded: it is the bar that made the high.)*
* **`HELD_ABOVE`** — otherwise.

**Robustness arm (pre-declared, not primary):** the same classifier over **3** bars (45 minutes).

### The outcomes

Measured over the **16 bars (4 hours) following `t`**, within the same session day:

| ID | Definition |
|---|---|
| **`O1`** | **MFE above `L`**, in pips: `(max high over t+1 … t+16 − L) / PIP`, floored at 0 |
| **`O2`** | fraction of events reaching **≥ 25 pips** above `L` |
| **`O3`** | fraction of events whose `O1` lands **inside the `[25, 50]` pip band** — and, separately, inside `[25, 55]` (§2d) |
| **`O4`** | **MAE below `L`**, in pips — the roll-off the lesson predicts for `CLOSED_BACK`. **Measured and reported, NOT used as a decision criterion**, because V19 gives no target for it |

---

## §4 — THE BASELINE, PRE-REGISTERED (`D-026`)

**`N1` — label permutation.** The `HELD_ABOVE` / `CLOSED_BACK` labels are shuffled across the pooled
event set, preserving both group sizes exactly, **10,000 iterations**, `seed = mmm_lib.SEED`. This
is the correct null here: it holds the event population and the market fixed and destroys **only**
the relationship between the time-cap clause and the outcome. **The claim is that the clause carries
information; the null is that it carries none.**

**`N2` — matched random entry (`D-029`).** For scale only: the same `O1` measured from bars drawn at
random from the same days and the same hours, with no exceed condition. **Reported, not used in the
verdict.**

**`N3` — the fragility guard.** ⚠ Fires, and **downgrades any positive result to `FRAGILE`**, if
**any** of:

* the primary (30 min) and robustness (45 min) arms disagree in **direction**;
* arms **A** and **B** disagree in **direction**;
* `W-A` and `W-B` disagree in **direction**;
* either group has **`n < 30`** on any arm;
* removing the single largest `O1` value from either group flips the primary verdict.

**A `FRAGILE` result is reported as a null.** This guard is fixed now, before any number exists.

---

## §5 — THE DECISION RULE, FIXED NOW

Let `Δ = median O1(HELD_ABOVE) − median O1(CLOSED_BACK)`, in pips, on **arm A, window `W-A`,
30-minute classifier** (the primary cell).

| Verdict | Condition |
|---|---|
| **CONFIRMED** | `Δ ≥ 10` pips **AND** `N1` permutation `p < 0.05` **AND** `median O1(HELD_ABOVE)` lies **inside `[25, 50]`** **AND** `N3` does not fire |
| **PARTIAL** | `Δ ≥ 10` pips **AND** `p < 0.05` **AND** `N3` does not fire, **but** the median falls **outside** `[25, 50]` — the *direction* is confirmed, the *magnitude* is not |
| **FRAGILE** | any `N3` condition fires. **Reported as a null.** |
| **REFUTED** | `p ≥ 0.05`, **or** `Δ < 10` pips, **or** `Δ` is negative |

⚠️ **`Δ ≥ 10` pips is a pre-registered materiality floor, not a fitted one.** It is set at
**40% of the lower edge of the lesson's own `25` pip band** — a difference smaller than that would
be statistically detectable and practically meaningless, and this project does not report those as
confirmations.

⭐ **Note what CONFIRMED would and would not mean.** It would mean the time-cap clause separates two
excursion populations by a material, non-random margin **at the magnitude the lesson states**. It
would **not** mean the rule is tradeable: no cost, no spread, no slippage and no execution is
modelled anywhere in this test, and `D-006` defers all of that to Phase 8.

---

## §6 — WHAT WOULD MAKE THIS TEST WRONG

Listed now so the reviewer does not have to derive them:

1. **The level definition (§2b) is this test's convention.** A reviewer preferring a different
   *"previous high"* — a swing pivot, a prior session's high, a peak-formation high — would build a
   different event set. **That is a legitimate attack and this file names it first.**
2. **The `≤ 24` bar upper bound is arbitrary within its motivation.** It is fixed before the run so
   it cannot be tuned, but it is not derived from the lesson.
3. **First-event-per-day discards data** and could bias toward early-session structure.
4. **`O1` is an excursion, not a close.** V19's *"extend to the next level strike zone"* is
   ambiguous between "trades there" and "settles there". **This test measures "trades there"**, the
   weaker and easier condition — so a `REFUTED` verdict is strong evidence and a `CONFIRMED` verdict
   is the lower bar. **Stated so the asymmetry is not read the wrong way.**
