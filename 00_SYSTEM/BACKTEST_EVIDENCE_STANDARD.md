# BACKTEST EVIDENCE STANDARD

What a manual backtest must satisfy before its result may be called evidence.

Governing decisions: `DECISIONS.md` **D-026** (baseline mandatory, hard gate),
**D-027** (period pre-registration and holdout reserve).

Applies to Phase 1 manual backtesting. Phase 8+ automated backtesting inherits
every requirement here and adds its own (`15_AUTOMATED_BACKTEST/README.md`).

---

## 0. WHY THIS FILE EXISTS

The original protocol (`STUDY_PROTOCOL.md` §2) is strong on **procedure** — sequential
walking, hidden future, losers retained, rule application graded apart from outcome.
It was silent on **inference**: what a result is compared against, and whether the
period it came from was chosen before or after seeing it.

An external methodological review put four questions to this repository:

1. Does a rule test run across every instance in the range, or search for matching
   examples?
2. Are losing and ambiguous setups in the output, or filtered out?
3. Is there a train/test split — are results measured on data not used to define or
   tune the rule?
4. What is the baseline — coin flip, buy-and-hold, random entry at the same times?

Answers at the time: (1) exhaustive **by design, never exercised**; (2) retained,
enforced at three layers; (3) **no**; (4) **none — zero mentions repository-wide**.

This file closes (3) and (4). It was written while `06_MANUAL_BACKTEST/` held **zero
observations**, so nothing needed to be redone — the standard is in place before the
first record exists, which is the only time this is cheap.

---

## 1. THE HARD GATE

```text
NO BT_*.md FILE MAY BE WRITTEN UNTIL:

  1. DECISIONS.md contains a baseline decision for the rule under test, AND
  2. DECISIONS.md contains the period pre-registration for that test, AND
  3. Both were recorded BEFORE any chart in the test period was examined.
```

`scripts/validate_project.py` enforces this mechanically: if any `BT_*.md` exists and
the required decision records do not, validation **fails**. This is deliberate — a
protocol that lives only in prose is a protocol that gets skipped at 2am.

---

## 2. BASELINE — MANDATORY

> A hit rate with no baseline is not a result. It is a number.

The method claims roughly 1 : 2.8 risk-to-reward and, at V04 `[00:08:56]`,
*"you're going to be in profit in 15 to 45 minutes. Guaranteed."* A 60% hit rate on
those terms sounds decisive and is, on its own, **unreadable** — it is not
distinguishable from entering at random in the same sessions, or from any long taken
during a week that happened to trend up.

### 2.1 Required baseline — matched random entry

For every rule tested, generate a control that holds **everything constant except the
setup itself**:

| Held constant | Varied |
|---|---|
| Instrument | Entry bar (drawn at random within the eligible window) |
| Session and eligible time window | Direction (drawn at random, or held at the rule's direction — state which) |
| Stop distance and target distance | — |
| Date range | — |
| Number of trades (match n) | — |
| **Entry PRICE convention** (see 2.1a — this row was added 2026-08-13) | — |

#### 2.1a The null's entry-**price** convention is a required pre-registration field

> **ADDED 2026-08-13** in remediation of `V08_REVIEW_R1.md` `M2` (`E20`, open item 65). This is
> a **forward** requirement. It does **not** invalidate any completed test, and `PT-034` — the
> test that exposed the gap — **is not edited**; `COMMON_PROTOCOL.md` §9 rule 7 forbids that.

The table above tells a session to hold the entry *bar* selection and the stop/target
distances. **It never said to fix the entry PRICE**, and `PT-034` shows what happens: the
pre-registration specified the random *bar* and left the *price* to the runner, which chose the
bar's **close**. The choice was sound, was committed before the run, and was validated by
landing on the analytic break-even — but it was settled in code rather than in the
pre-registration, which is exactly the location a reviewer cannot audit in advance.

**Requirement.** Every `PT-xxx` carrying a matched-random null **must state, in the
pre-registration's own parameter table, the price at which the null enters** — e.g.
*"the chosen bar's close"*, *"the chosen bar's open"*, *"the bar's midpoint"*.

**State it even when — especially when — it differs from the rule arm's.** A rule arm anchored
to an extreme (`LOD + X`) and a null entering at the close are **not** using the same price
convention, and that asymmetry is load-bearing for what the comparison means. A null must not
be given an intrabar-favourable price (its bar's low for a long, its high for a short): that
borrows the very favourability the rule arm is being tested for and biases the null **toward**
the rule. A random bar has no extreme to anchor to — that is what makes it a null — so the
close is the ordinary neutral choice, but the choice must be **written down, not inferred from
the code**.

**Reviewer enforcement:** an unstated null entry-price convention is at minimum a `MINOR`
`E20` (pre-registration completeness). See `06_MANUAL_BACKTEST/V08/BT_V08_0001.md` §5 for the
worked precedent.

Run it at least **200 iterations** and report the distribution, not one draw. The
comparison is *the rule's result against that distribution*, and the honest statement
of an unimpressive outcome is:

> The rule's 58% hit rate sits at the 61st percentile of matched random entry
> (median 55%, 5–95% range 44–66%, n = 30 trades, 200 iterations). **This sample
> cannot distinguish the rule from chance.**

### 2.2 Strongly recommended second baseline — the course's own natural control

V04 hands the project a controlled comparison most methods never provide. The
instructor's claim is that **location, not pattern, is what changes the outcome**:
the same M formation is a loser inside the blue box and a winner outside it
(`V04_SOURCE_NOTES.md` §2b, `[00:03:04]`–`[00:03:27]`).

That is a testable contrast with the confound removed — same pattern, same pair, same
week, different location. Where the sample permits, run:

```text
Arm A — setup satisfying the rule, OUTSIDE the Asian range
Arm B — same pattern, INSIDE the Asian range        ← the course predicts this loses
```

If both arms perform alike, the prohibition that forms the spine of V04 is not doing
the work the course says it does. That finding would be **more valuable** than a
favourable hit rate, and it must be reported with equal prominence.

### 2.3 Optional third baseline

Buy-and-hold / drift over the same window. Weak for intraday FX, but it catches a
directional bias in the sample (e.g. a test period that only contains a downtrend).

### 2.4 Baselines are pre-registered

The baseline definition is written into `DECISIONS.md` **before** the first
observation. Choosing or adjusting a baseline after seeing the rule's result is
performance chasing with extra steps, and is reviewer error `E09`.

---

## 3. PERIOD SELECTION AND HOLDOUT

### 3.1 The genuine strength, stated honestly

The rules are **not fitted to price data**. They are transcribed from 2012 lectures
and were fixed before any chart was opened — the strongest form of pre-registration
available, and better than a conventional train/test split on that one axis.

**It does not follow that no split is needed.** Pre-registered rules do not protect
against a *period* chosen, consciously or not, because it looked cooperative. That is
the exposure a split closes.

### 3.2 Requirements

1. **Pre-register the period.** Instrument, date range, timeframe and session
   boundaries are recorded in `DECISIONS.md` **before** any chart in that range is
   examined. If a range must change mid-test, that is a **new test with a new ID**;
   the abandoned one is retained and marked `ABANDONED — PERIOD CHANGED`.
2. **Reserve a holdout.** A contiguous block of history — recommended: the most
   recent 30% — is **never opened** during the Student Phase, by anyone, for any
   reason. It exists so that a rule set assembled across 21 lessons can be tested
   once, at the end, against data no session has seen.
3. **Record every look.** Inspecting the holdout converts it into development data.
   If it happens, say so; do not quietly continue calling it a holdout.
4. **No period may be tested twice** for the same rule without recording the repeat
   and reporting both results. Two tests of one rule with only the favourable one
   reported is cherry-picking at the sample level.

### 3.3 The boundaries are the owner's decision

This file requires that boundaries exist and be recorded; it does not set them, and
no agent may invent them. Recommended default, pending the owner's decision:

```text
DEVELOPMENT   earliest available → 70% point   (student-phase testing)
HOLDOUT       70% point → most recent          (untouched until Phase 6+)
```

---

## 4. STATISTICAL HONESTY

### 4.1 Minimum reportable sample

Below **n = 30** decision points for a given rule, report the observations and state
plainly:

> `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only.`

Below n = 30 no hit rate may be quoted in a summary, a mastery report, a concept
entry, or the master specification without that label attached in the same sentence.

### 4.2 Interval, not point estimate

Every hit rate is reported with an interval. At n = 30, a 60% hit rate carries a
roughly 42–76% confidence interval — wide enough to contain both "excellent" and
"no better than chance." Reporting "60%" alone hides that.

### 4.3 Multiple comparisons

Twenty-one lessons will yield many testable claims. Testing enough of them guarantees
some will look significant. Mitigations, all required:

- the rule and its baseline are pre-registered before testing,
- every test performed is recorded, **including the ones that found nothing**,
- a summary that reports only the rules that worked is invalid.

### 4.4 Never report a win rate alone

Required alongside: sample size, baseline comparison, expectancy, average win,
average loss, maximum adverse excursion, and the rule-application grades
(`Correct Setup / Loser` etc.) separately from trade outcomes.

---

## 5. WHAT COUNTS AS WHAT

| Category | Meaning | May support |
|---|---|---|
| `DESCRIPTIVE` | Measurement of what happened. No baseline, or n < 30. | Illustration only. **Never** a claim that a rule works. |
| `EVIDENTIAL` | Pre-registered rule and period, baseline run, n ≥ 30, interval reported. | A conclusion about the rule, stated with its interval. |
| `INVALID` | Any integrity check failed. | Nothing. Retained, marked, superseded. |

Existing quantitative work is `DESCRIPTIVE` and already labels itself correctly —
`V04_HOMEWORK.md`: *"One week is one week — this is a single observation."* The
"2 of 4 formed anchors, both 3.83 days" figure is a **two-observation** result and
must never be quoted as support for the 2.5–3 day claim (`C-001`).

---

## 6. RETROACTIVE APPLICATION

At the time of writing: **0 backtest observations exist**, so there is nothing to
redo. Concretely:

| Item | Status |
|---|---|
| `06_MANUAL_BACKTEST/` observations | None. Standard applies to the first one written. |
| V02/V03/V04 homework | `DESCRIPTIVE`, already self-labelled. **No rework required.** |
| Rules in source/interpretation notes | Untouched — this standard governs testing, not transcription. |

**The four-lesson backtest debt is now owed under this standard**, not the previous
one. When `A-039` clears and the backlog is discharged, each discharged test needs a
pre-registered period and a baseline, exactly as a fresh test would.

---

## 7. REVIEWER ENFORCEMENT

`REVIEW_PROTOCOL.md` §6.G carries checks 15–20 covering baseline, pre-registration,
holdout integrity, sample sufficiency, interval reporting, and negative-result
retention. Any check failing is at least `MAJOR`; a missing or post-hoc baseline is
`CRITICAL`, because it makes the result unreadable rather than merely weak.

New error codes:

```text
E21 — No baseline, or baseline chosen after seeing the result
E22 — Period not pre-registered, or changed mid-test without a new ID
E23 — Holdout data inspected during the Student Phase
E24 — Hit rate reported without sample size, interval, or baseline
E25 — Negative or null result omitted from a summary
```

---

## 8. THE STANDARD

> Would this result survive someone who wanted it to be false?

If the answer depends on the reader not asking what it was compared against, it is
not evidence yet.

**A null result honestly obtained is worth more to this project than a favourable one
that cannot be read.**
