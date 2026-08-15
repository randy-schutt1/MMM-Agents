# V20 — INDEPENDENT REVIEW, ROUND 2

**Round:** R2 — remediation re-review of `V20_REVIEW_R1.md`
**Reviewer:** Independent Reviewer / Teacher Agent (`D-003`)
**Date:** 2026-08-15
**Lesson:** `Bootcamp1 Wk9 052012 Part2 (46mins) (1).swf` · V20 · 2012-05-20 · 00:45:49
**Reviewed:** `video/v20` @ **`a761eb4`** — **2 commits** (`7bac6a9`, `a761eb4`) on top of R1's
`2ab5e83`
**Review branch:** `review/v20`, isolated worktree `MMM-Agents-v20-review` (`D-038`)

---

## FINAL DECISION

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 1 MINOR, 8 NOTE.**
**Confidence:** `HIGH`.

⭐ **Both R1 `MAJOR`s are FIXED and the fixes are independently verified. `V21`'s GATE IS OPEN**
under `D-024` — zero `CRITICAL`, zero `MAJOR`. **R1's items 332–335 are all discharged.**

**One new `MINOR` (item 348)** is raised, on the `N1` baseline's undeclared direction convention. It
does not touch the corrected verdict.

⚠️ **One factual correction to the handover:** the remediation is **2 commits**, not 3
(`git rev-list --count 2ab5e83..a761eb4` = 2). Nothing turns on it; recorded because this round
checks stated facts rather than repeating them.

---

## §1 — `M1` (item 332) — ⭐ FIXED, AND RE-DERIVED FROM SCRATCH RATHER THAN MATCHED

### §1.1 — THE CODE FIX IS THE RIGHT ONE

`run_pt048.py`'s `measures()` now takes `k=PIVOT_K` and detects interior counter-swings with
`ll[t] == ll[t-k:t+k+1].min()` — **the same test `PT-048` §3.1 specifies for a swing pivot, and the
same one this reviewer's independent implementation used in R1.** The hardcoded `±1` comparison is
gone from both the up-leg and down-leg branches.

⭐ **`PT-048` itself is unedited.** Verified: `git diff 2ab5e83..a761eb4 --
06_MANUAL_BACKTEST/PRE_REGISTERED/PT-048_*` is empty. **The runner was brought to the file, not the
file to the runner** — which is what the pre-registration's own governance clause requires.

### §1.2 — ⭐ THE NUMBERS, RE-DERIVED INDEPENDENTLY

**This round did not check the submission's numbers against R1's.** A fresh implementation was
written from `PT-048` §3 and run with a **different bootstrap seed (`987654321`) and a different
iteration count (50,000 against the runner's 20,000)**, so the interval is an independent estimate
rather than a re-run of the same draw.

| `W-A` / arm A | Submission (corrected) | **Reviewer, fresh R2 derivation** | |
|---|---|---|---|
| `k = 1` | 22.45 `[22.00, 23.20]`, n=2506 | 22.40 `[22.00, 23.20]`, n=2519 | ✅ |
| `k = 2` | 26.80 `[25.90, 27.60]`, n=1200 | 26.80 `[25.85, 27.60]`, n=1204 | ✅ |
| ⭐ **`k = 3` — PRIMARY** | ⛔ **30.10** `[28.80, 31.25]`, n=702 | ⛔ **30.10** `[28.70, 31.20]`, n=706 | ✅ **median EXACT** |
| `k = 4` | 33.10 `[31.30, 34.90]`, n=440 | 33.10 `[31.20, 34.60]`, n=447 | ✅ |

⭐ **Three of the four medians are exact and the fourth differs by 0.05.** The `n` differences
(≤ 1.5 %) are this reviewer's slightly looser day-length filter and are immaterial.

⚠️ **On the handover's phrase *"agrees to the second decimal"* — that is true of the MEDIAN and
should not be claimed of the interval.** R1's bootstrap returned `[28.70, 31.25]`, R2's fresh one
returned `[28.70, 31.20]`, and the runner's returns `[28.80, 31.25]`. **This reviewer's own two
independent bootstraps disagree in the same digit**, so the second decimal of the bound is
resampling noise on a 0.05-pip-granular distribution, not a precision claim. **Nothing turns on it:
all three intervals lie entirely above the band.**

### §1.3 — ⭐ AND THE VERDICT IS `REFUTED` ON ALL FOUR CELLS, WHICH R1 DID NOT ESTABLISH

Re-derived here across both arms and both windows at the pre-registered `k = 3`:

| cell | median `P1` | boot 95 % | verdict |
|---|---|---|---|
| `W-A` / A **(primary)** | **30.10** | `[28.70, 31.20]` | ⛔ **REFUTED** |
| `W-B` / A | 27.10 | `[26.60, 28.45]` | ⛔ REFUTED |
| `W-A` / B | 30.90 | `[29.90, 32.30]` | ⛔ REFUTED |
| `W-B` / B | 27.30 | `[26.70, 28.60]` | ⛔ REFUTED |

**The median rises monotonically in `k` on every cell**, and `k = 1` is the only scale of the four
that puts it in the band — **confirming R1's characterisation that the original choice ran toward
the claimed band.**

### §1.4 — THE SENSITIVITY TABLE IS NOW PERMANENT OUTPUT

The runner publishes `k = 1…4` on every run, labelled **reporting-only** with `k = PIVOT_K` the sole
verdict basis. ⭐ **This is the correct response to R1's review question 3** (`N3` brackets
boundaries, arms and windows but not measure internals) and it closes the hole `M1` went through.

### §1.5 — THE REPORTING IS HANDLED CORRECTLY

`BT_V20_0001.md` §0a carries a prominent corrected-on notice; §0 states **`REFUTED`**; the previous
`CONFIRMED` is **retained as historical fact with a warning not to cite any version without §2a**;
§2a gives the full accounting, accepts the finding, and reproduces R1's own fairness caveat that
§3 does not restate `±3` inside the `P1` row. **§6's *"No other disagreement"* sentence is corrected.**

⛔ **`M1` IS CLOSED.**

---

## §2 — `M2` (item 333) — ⭐ FIXED, AND CONFIRMED ON TWO FURTHER MODEL FAMILIES

### §2.1 — A SIXTH AND SEVENTH DECODE, ON MODELS NEITHER SIDE HAD USED

R1 used `large-v3` and `medium.en`. The remediation added an `openai-whisper medium.en` fifth. **This
round ran two more, deliberately on model families not yet used on this passage:**

| Decode | Model | Result at `[00:29:16]` / `[00:29:25]` |
|---|---|---|
| 6 | **`small.en`** | *"take the distance of this **candle** … one third off the high o…"* |
| 7 | **`distil-large-v3`** | *"Take the distance of this **candle** … one-third off the high of thi…"* |

⭐ **Seven decodes across four distinct model families — `large-v3`, `distil-large-v3`, `medium.en`,
`small.en` — under both `vad_filter` settings. Every one returns `candle`. None has ever returned
`handle`.** The correction is settled.

### §2.2 — THE RECORD CHANGES ARE CORRECT IN FORM AND IN SUBSTANCE

* ⭐ **`A-136` is CLOSED as `RAISED IN ERROR`**, citing item 333, with the **superseded title retained
  struck-through per `REMEDIATION_PROTOCOL.md` §2** rather than deleted.
* ⭐ **The transcript body is NOT edited.** A **§2a correction block** was added, listing all six
  markers including `[00:29:50]` *"So track 33 pitch"* → *"Subtract 33 pips"*, and explicitly noting
  the two genuine **verb** uses are unaffected. **This is the same handling V18 used for its
  `[00:19:40]` inversion and it is the right one** — Tier-1 source is preserved and annotated.
* ⭐ **`A-139` is opened as the narrowed successor** — the arithmetic is complete, **which bar** is
  not stated. It lists the two contextual candidates, notes they may be the same bar, and **refuses
  to choose** (`D-030`). ⭐ **This is the correct residue**: R1 said the rule is not blocked, not that
  every question about it is answered.
* **`V20_INTERPRETATION.md` dimension `B` and the mastery report's §4.5 *"cheapest high-value
  blocker"* claim are both amended.**

⛔ **`M2` IS CLOSED.**

---

## §3 — ITEMS 334 AND 335 — BOTH DISCHARGED

* **334 (the `PT-048` baseline / NULL ruling).** `BT_V20_0001.md` §3 now reports the baseline in the
  verdict block and §3a names the pre-registration's own defect as a defect. ⭐ **And the corrected
  run makes the point stronger than R1 could:** the null returns essentially the result at `k = 3`
  (29.15 vs 30.10) *and* did so at `k = 1` (23.00 vs 22.45). **The claim now fails on two
  independent grounds — wrong magnitude at the pre-registered scale, and non-diagnostic.**
  ⚠️ **With one qualification — item 348 below.**
* **335 (the missing ASR pass).** Discharged in R1, when this reviewer ran it. ⭐ **The remediation
  correctly identifies item 326 as the ROOT CAUSE OF BOTH `MAJOR`s** rather than treating them as
  unrelated.

---

## §4 — `PT-049` — THE PRE-REGISTRATION IS SOUND

Reviewed as a pre-registration, since **no runner exists** — verified: no `run_pt049.py` and no
`BT_V20_0002.md` anywhere on the branch. **Committed before any bar was read, per
`COMMON_PROTOCOL.md` §9 rule 7.**

⭐ **It closes every methodological hole R1 found, by name:**

| R1 finding | What `PT-049` does |
|---|---|
| **`M1`** — a scale used by the primary measure was not stated where it was used | §3 **states every scale once, inside the measure that uses it**, and §6 makes the cross-convention output **mandatory on every run** |
| **334** — `N1` was defined and never scored | §4: ***"`N1` is an EXPLICIT CONDITION of every non-null verdict"***, and §5's `CONFIRMED` row requires beating it |
| **345** — `PT-048` §5's decision-table hole | §5: *"A median outside a threshold whose interval overlaps it falls to `PARTIAL`, explicitly"* |
| **R1 question 3** — `N3` does not cover measure internals | `N3` now includes *"the `1/3` result is not distinguishable from the `1/4` and `1/2` results"* |

**Other things it gets right:** the primary cell (`S1`, `1/3`, arm A, `W-A`) is **named before any
number exists**; the three bar conventions are **declared as conventions, not course rules**
(`D-010`/`D-030`); `W-B ⊃ W-A` non-independence is stated in advance; it says plainly that a high
fill rate is **not** evidence the rule is good; `D-009` is cited to bar optimising across the
fraction set; and `CONFIRMED` is explicitly defined **not** to mean profitable (`D-006`).

⚠️ **Two observations for whoever runs it, neither a finding:**

1. **`O4 = O2 − O3` is reported "for scale only" and is not a verdict input** — correct, but it is
   the figure most likely to be quoted out of context later. Worth a *do not cite* line in
   `BT_V20_0002.md` when it lands, of the kind `BT_V20_0001.md` §0 now carries.
2. **`N3`'s fourth condition is a genuine improvement and also the likeliest to fire.** A fraction
   that is not special is the expected outcome, and the guard is written so that outcome reads as
   `FRAGILE`/null rather than as support. **That is the right way round.**

---

## §5 — FINDINGS

### `CRITICAL` — **NONE**
### `MAJOR` — **NONE.** Both R1 `MAJOR`s are fixed and independently verified.

### `MINOR`

| # | Item |
|---|---|
| **348** | ⚠️ **`N1`'s DIRECTION CONVENTION IS UNDECLARED, AND THE *"NON-DIAGNOSTIC AT EVERY SCALE"* CLAIM IS CONVENTION-DEPENDENT.** `PT-048` §4 says a random window is drawn *"with no leg condition"* and that the control *"destroys only 'this is a trend leg'"*. **It does not say how the window's DIRECTION is assigned**, and `P1` cannot be computed without one. `run_pt048.py` uses `d = 1 if h[b] >= h[a] else -1` — the window's own realised direction. **Reproduced here: 28.20 against the runner's 29.15** (sampling noise, same design). ⚠️ **Under the alternative — measuring in a direction not derived from the window — this reviewer gets 34.20–35.47, which SEPARATES from the trend legs' 30.10 with a random-window interval of `[33.70, 37.10]` that excludes it.** So the **specificity** half of §3's conclusion flips on an undeclared convention. ⭐ **In fairness: the runner's rule is the faithful generalisation of how observed legs get their direction (endpoints), and is arguably the better choice** — this is not charged as a wrong answer. **What is charged is that §3 states the conclusion as *"non-diagnostic at EVERY scale"* and *"SCALE-INVARIANT"* without recording that it is not convention-invariant** — the same species as `M1`, in a report that has just added a mandatory sensitivity table for the other free convention. ⛔ **The primary verdict `REFUTED` is UNAFFECTED**: 30.10 lies outside `[20, 25]` whatever the baseline does. `E20` |

### `NOTE` — no action required

| # | Item |
|---|---|
| **349** | ⭐⭐ **`M1`'s FIX RE-DERIVED FROM SCRATCH, NOT MATCHED.** Fresh implementation, **independent bootstrap seed and iteration count**. Primary `k = 3` median **30.10 — exact**; `k = 1/2/4` exact or within 0.05. ⭐ **And `REFUTED` holds on all four arm×window cells**, which R1 had not established |
| **350** | ⭐ **THE PRE-REGISTRATION WAS NOT EDITED.** `git diff` over `PT-048_*` between `2ab5e83` and `a761eb4` is **empty**. The runner was brought to the file. **This is the clause `BT_V20_0001.md` §6 failed to honour in R1, honoured now** |
| **351** | ⭐⭐ **SEVEN DECODES, FOUR MODEL FAMILIES, ZERO `handle`.** R1's four, the remediation's fifth, and **this round's `small.en` and `distil-large-v3`** — the last two chosen because neither side had used them on this passage |
| **352** | ⭐ **THE TRANSCRIPT BODY IS PRESERVED AND ANNOTATED, NOT EDITED** — a §2a correction block covering all six markers, with the two genuine verb uses explicitly excluded. **Same handling as V18's `[00:19:40]`** |
| **353** | ⭐ **`A-136`'s CLOSURE IS CORRECT IN FORM** — `RAISED IN ERROR`, superseded title struck through and **retained** per `REMEDIATION_PROTOCOL.md` §2, and **`A-139` opened for the narrower residue** rather than the question being declared answered |
| **354** | ⭐⭐ **`PT-049` CLOSES EVERY METHODOLOGICAL HOLE R1 FOUND, BY NAME** — `N1` as an explicit verdict condition (334), every scale stated inside its own measure (`M1`), the §5 decision-table hole closed (345), and `N3` extended to cover the "not special" outcome (R1 question 3). **No runner exists; committed before any bar was read** |
| **355** | ⛔ **THE FIX ROUND WAS DELIBERATELY NOT SELF-VERIFIED**, and says so: *"`D-024` holds the gate closed on any `MAJOR` until it is fixed **and re-reviewed in a fresh round** … This round does not use it."* ⭐ **R1's review question 1 was that owner-authorised self-verify was becoming the default. This round declines it explicitly.** The owner question stands — the exception still has no numbered decision — but **the practice has corrected itself without one** |
| **356** | **THE HANDOVER SAID 3 COMMITS; THERE ARE 2.** `git rev-list --count 2ab5e83..a761eb4` = 2 (`7bac6a9`, `a761eb4`). Nothing turns on it. Recorded because this round checks stated facts rather than repeating them — the same discipline item 246 charged and item 278 credited |

---

## §6 — REQUIRED CORRECTIONS

1. **Item 348 (`MINOR`, does not hold the gate).** In `BT_V20_0001.md` §3, **state the `N1` direction
   convention** (`d` from the window's own endpoints) and **either** report the alternative
   convention's figure **or** narrow *"non-diagnostic at every scale"* to name what was held fixed —
   e.g. *"non-diagnostic at every swing scale, under the endpoint direction convention."*
   ⭐ **Do not re-run `PT-048` and do not edit the pre-registration.** This is one sentence and one
   declared convention.

**Nothing else is owed.** Items 332–335 are discharged.

---

## §7 — REVIEWER QUESTIONS FOR THE OWNER

1. **R1's question 1 stands, but is less urgent.** `SELF-VERIFIED AT OWNER DIRECTION` still has no
   numbered decision authorising it for `MAJOR` closure, and V19's item 302 was closed that way.
   ⭐ **This round shows the practice self-correcting** — V20's remediation explicitly declined it.
   **A decision that either authorises the route with conditions, or bars it for `MAJOR`s, would
   settle it before the next occasion.**
2. **A standing clause is now earned, not hypothetical.** Both R1 `MAJOR`s and new item 348 are the
   same species: **a free convention inside a measure, undeclared, with a conclusion-determining
   effect.** `PT-049` fixes it for one test by fiat. **`BACKTEST_EVIDENCE_STANDARD.md` should carry
   it for all of them:** *every free parameter of a primary measure is either fixed by the
   pre-registration or published at three settings on every run.*

---

## §8 — ADVANCEMENT

```text
LESSON: V20
DECISION: REVISE (R2)
CONFIDENCE: HIGH

CRITICAL ISSUES: none
MAJOR ISSUES:    none - both R1 MAJORs fixed and independently verified

R1 ITEM DISPOSITION:
  332  M1  PT-048 primary measure       -> CLOSED. Runner wired to PIVOT_K;
           k=3 median 30.10 re-derived from scratch (exact); REFUTED on all
           four cells; k=1..4 sensitivity now permanent output.
  333  M2  A-136 / candle-vs-handle     -> CLOSED. A-136 closed as an artifact,
           A-139 opened for the residue, transcript annotated not edited;
           confirmed on two further model families (7 decodes, 4 families).
  334      PT-048 baseline / NULL       -> DISCHARGED.
  335      Missing ASR pass             -> DISCHARGED.

NEW MINOR:
  348      N1's direction convention is undeclared; the "non-diagnostic at
           every scale" claim is convention-dependent. Primary verdict
           REFUTED is unaffected.

REQUIRED ACTIONS:
1. Declare N1's direction convention and narrow one sentence in
   BT_V20_0001.md §3. Do not re-run; do not edit the pre-registration. (348)

ADVANCEMENT: AUTHORIZED
V21 GATE: OPEN under D-024 - zero CRITICAL, zero MAJOR.
V20 STATUS: IN REMEDIATION on item 348 alone. Not COMPLETE until it is applied.
```

⭐ **What this round actually demonstrates.** R1's two `MAJOR`s were the two things a session cannot
find about itself — one needed an independent re-implementation, the other an independent ear.
**Both were accepted without argument, verified by the session before being acted on, fixed at the
root rather than at the symptom, and deliberately not self-closed.** ⭐ **And `PT-049` generalises
the lessons instead of patching the instance.** **That is what a remediation round should look
like.**

---

## §9 — REVIEWER'S OWN DISCLOSURES

1. **Worktree isolation honoured** — `MMM-Agents-v20-review`, branch `review/v20`.
2. **The k=1…4 table and the four-cell verdict table were computed by fresh code written for this
   round**, with a bootstrap seed and iteration count deliberately different from both the runner's
   and R1's, so the interval is an independent estimate. **The submission's numbers were read only
   afterwards.**
3. **The `N1` direction finding was isolated by re-running the reviewer's own baseline under both
   conventions** (`28.20` under the runner's, `34.20`–`35.47` under the alternative), rather than
   asserted from the code alone.
4. **Item numbering.** Items **348–356** allocated against integration at `d1088c2`, where **317**
   remains the highest item; `video/v20` holds 318–331 and R1 holds 332–347. **No collision, no
   renumbering.**
