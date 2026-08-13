# STUDY PROTOCOL

The Student Agent's per-lesson workflow, plus the long-term phase roadmap.

Source: `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` §§1, 11–20, 27–31.

---

## 0. CORE PRINCIPLE — LEARN BEFORE AUTOMATING

During the Student Phase:

- Do **not** convert subjective trading concepts into arbitrary machine rules.
- Do **not** optimize parameters.
- Do **not** modify the methodology to improve results.
- Do **not** reverse-engineer rules to produce a desired win rate.
- Do **not** write production Pine Script.
- Do **not** treat any advertised accuracy claim as a required outcome.

The methodology must first be faithfully reconstructed. Later phases determine
which rules are measurable, which remain discretionary, which parameters need
empirical estimation, and what the actual historical performance is.

---

## 1. PER-LESSON SEQUENCE

One lesson per session. Do not begin lesson N+1 until lesson N has a reviewer
`PASS`.

### STEP 1 — PREVIEW

Identify: title, duration, apparent subjects, homework references, chart examples,
continuation from the previous lesson.

Do not begin interpretation until the lesson context is understood.

### STEP 2 — TRANSCRIPT

Create `02_TRANSCRIPTS/VXX/VXX_TRANSCRIPT.md` from
`TEMPLATES/TRANSCRIPT_TEMPLATE.md`.

- Preserve timestamps in `[HH:MM:SS]` form.
- Use exact transcription where possible.
- Mark uncertain wording explicitly — `[unclear]`, `[inaudible]`, `[?word?]`.
- **Never silently invent missing speech.**

### STEP 3 — SOURCE NOTES

Create `03_LESSON_NOTES/VXX_SOURCE_NOTES.md`.

Contains **only**: explicit teachings, chart observations, definitions, examples,
warnings, homework instructions. Every entry carries a timestamp.

Keep interpretation out of this file entirely.

### STEP 4 — INTERPRETATION NOTES

Create `03_LESSON_NOTES/VXX_INTERPRETATION.md`.

Every interpretation includes: evidence, timestamp, screenshot reference, and a
confidence classification (`EXPLICIT` / `VISUAL` / `IMPLIED` / `INFERRED` /
`UNRESOLVED`).

The separation between Step 3 and Step 4 is not cosmetic — it is the mechanism
that prevents interpretation from being falsely remembered as instructor doctrine.

### STEP 5 — SCREENSHOTS

Screenshots are first-class evidence. Do not capture merely because a slide
changed; capture the visual moments necessary to reconstruct the teaching.

Categories worth capturing: definitions, diagrams, annotated charts, setup
formation, setup completion, pre-entry context, entry, stop location, target
location, invalidation, weekly structure, intraday structure, timing examples, EMA
behaviour, pushes, levels, M/W formations, peak formations, failed setups,
borderline setups, exceptions, homework examples, before/after market progression.

Store in `04_SCREENSHOTS/VXX/`, named per `FILE_NAMING_STANDARD.md`:

```text
V07_00-43-12_three-push-example.png
```

Maintain `04_SCREENSHOTS/VXX/INDEX.md` from
`TEMPLATES/SCREENSHOT_INDEX_TEMPLATE.md`, recording for each: screenshot,
timestamp, concept, what to notice, rule supported, Source/Visual/Inferred,
related homework.

### STEP 6 — HOMEWORK

If the instructor assigns work, complete it. A lesson is not complete merely
because the video ended.

Cycle: **Learn → Attempt → Grade → Diagnose → Reattempt → Pass**

Store in `05_HOMEWORK/VXX/`. Preserve: task, source timestamp, first attempt,
reasoning, answer, grading evidence, errors, correction, final attempt, mastery
result.

**Preserve the first attempt even when it is wrong.** Reconstructing the answer
after seeing a solution is not independent mastery, and the reviewer will
distinguish `FIRST-PASS SUCCESS` from `SUCCESS AFTER CORRECTION` and
`SUCCESS AFTER SOURCE REVIEW`.

### STEP 7 — MANUAL BACKTEST

See §2 below. Store in `06_MANUAL_BACKTEST/VXX/`, one file per observation.

### STEP 8 — CHART EXAMPLES

For every major pattern, deliberately collect all four kinds:

| Kind | Location | Meaning |
|---|---|---|
| Positive | `09_CHART_EXAMPLES/positive/` | Clearly satisfies the methodology |
| Negative | `09_CHART_EXAMPLES/negative/` | Looks similar but violates an important rule |
| Borderline | `09_CHART_EXAMPLES/borderline/` | Reasonable experts might disagree |
| Unresolved | `09_CHART_EXAMPLES/unresolved/` | Cannot yet be classified |

Also record **failed valid setups** — setups that met the rules and lost. These
belong with positive examples, annotated as valid-but-losing.

A recognition system requires **discrimination**, not merely pattern familiarity.
A knowledge base of only successful examples is a failure.

### STEP 9 — CONCEPT LIBRARY, AMBIGUITIES, CONTRADICTIONS

- New concepts → `08_CONCEPT_LIBRARY/` (one file each, from
  `TEMPLATES/CONCEPT_TEMPLATE.md`), registered in `CONCEPT_INDEX.md`.
- Subjective language → `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`, status
  `DO NOT CODE`.
- Conflicting teachings → `11_CONTRADICTIONS/CONTRADICTIONS.md`. Never silently
  reconcile.

Do not finalize the ontology early. Let the course reveal the correct hierarchy.

### STEP 10 — MASTERY REPORT

Create `07_MASTERY_REPORTS/VXX_MASTERY_REPORT.md` against `MASTERY_STANDARD.md`.

Status is exactly one of `PASS` / `REVIEW REQUIRED` / `BLOCKED`, and it is a
**self-assessment**, not an authorization.

### STEP 11 — STOP AND REQUEST REVIEW

Update `COURSE_PROGRESS.md`, append to `LOG.md`, run
`scripts/validate_project.py`, commit, push.

Then **stop**. Do not open the next video. The next action is an independent
reviewer session.

---

## 2. MANUAL BACKTEST PROTOCOL

Manual backtesting is part of the Student Phase and is different from later
automated backtesting. Its purpose is to determine whether the agent can correctly
**apply** what was taught to historical market data.

Primary instrument: **GBP/USD**, unless the course requires another for a teaching
example.

### Procedure

1. Define exactly which lesson rule is being tested.
2. Select a historical period **without** choosing only obvious winning examples.
3. Move through the chart sequentially.
4. **Do not use future candles when making the initial classification.**
5. Capture the chart at the decision point (screenshot "before").
6. Record the prediction or classification — before revealing anything.
7. Reveal subsequent candles.
8. Record the outcome (screenshot "after").
9. Grade **rule application** separately from **trade result**.

### The essential distinction

```text
Correct Setup   / Winner
Correct Setup   / Loser        ← still a correct application
Incorrect Setup / Winner       ← still an error
Incorrect Setup / Loser
Borderline      / Unresolved
```

A profitable invalid setup must not inflate confidence in the method. A correctly
identified losing setup is not a misunderstanding.

### Anti-hindsight rules

Never: define setup boundaries using future highs/lows; classify a pattern in a way
that requires seeing the later reversal; justify an entry after the target was hit;
quietly drop losing examples; change the interpretation after the outcome is known;
select only aesthetically clean historical setups; or assume information
unavailable at the decision candle.

If hindsight contaminated a sample, the sample must be **redone**, not edited.

### Record

One file per observation in `06_MANUAL_BACKTEST/VXX/`, named `BT_VXX_NNNN.md`,
from `TEMPLATES/MANUAL_BACKTEST_TEMPLATE.md`. Fields: Test ID, date, instrument,
timeframe, lesson, setup, market context, evidence visible at decision time, entry
criteria, invalidation criteria, expected outcome, actual outcome, result in R,
correct rule application (Y/N), valid setup (Y/N/Borderline), screenshot before,
screenshot after, mistake classification, notes.

Maintain cumulative summaries in `06_MANUAL_BACKTEST/cumulative/`. **Never delete
individual observations**, including losers and mistakes.

### Baseline, pre-registration and holdout — REQUIRED

Before opening any chart in a test period, complete §0 of the observation template and
record the matching entries in `DECISIONS.md`:

- **Baseline** (D-026) — matched random entry, ≥200 iterations, distribution reported.
  A hit rate with no comparator is not a result.
- **Period pre-registration** (D-027) — instrument, range, timeframe, sessions, fixed
  in advance. Changing the range mid-test creates a new test ID.
- **Holdout** (D-027) — the reserved block is not opened during the Student Phase.

Full specification: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`. `scripts/validate_project.py`
fails the build if an observation exists without these.

Where the course supplies its own control, use it. V04's claim is that **location**
changes the outcome — same M formation, loser inside the blue box, winner outside. That
is a natural experiment with the pattern confound removed, and it is stronger evidence
than any hit rate taken alone.

### Sample sufficiency

There is no universal minimum count during the learning phase. Sufficiency depends
on lesson complexity, setup frequency, chart ambiguity, variation, and diversity of
market conditions. The reviewer may require more testing before `PASS`.

---

## 3. WHAT NOT TO DO DURING PHASE 1

- Do not treat any claimed win rate (e.g. 90–95%) as a target. Record the claim
  with provenance and treat it as a **hypothesis to test**.
- Do not manipulate parameters, setup selection, sample windows, trade exclusions,
  risk/reward, entry timing, or labelling rules to reach an expected percentage.
- Do not write Pine Script or generate trading signals.
- Do not populate `12_MASTER_SPEC/` or `13_MACHINE_SPEC/`.
- Do not import external frameworks (ICT, SMC, Wyckoff, Elliott Wave, generic
  price action).

---

## 4. PHASE ROADMAP

| Phase | Name | Content | Status |
|---|---|---|---|
| 0 | Environment | Repository, files, provenance, source manifest, logging | **Complete** |
| 1 | Student | Process every bootcamp lesson; homework; manual historical backtesting | **Blocked — awaiting source videos** |
| 2 | Scholar | Cross-reference the course; resolve terminology, dependencies, contradictions, exceptions | Not started |
| 3 | Expert | Produce canonical MMM specification (`12_MASTER_SPEC/`) | Not started |
| 4 | Formalizer | Translate human concepts into measurable machine definitions (`13_MACHINE_SPEC/`) | Not started |
| 5 | Observer | TradingView indicators that identify structures without trading (`14_PINE/`) | Not started |
| 6 | Evaluator | Compare machine recognition against manually labelled GBP/USD history | Not started |
| 7 | Strategist | Deterministic entries, stops, invalidations, targets, trade management | Not started |
| 8 | Automated Backtester | Repeatable historical strategy testing (`15_AUTOMATED_BACKTEST/`) | Not started |
| 9 | Researcher | Robustness, sensitivity, regimes, sessions, years, volatility, spread, slippage, parameter stability | Not started |
| 10 | Forward Tester | Paper / shadow trading in live conditions (`16_FORWARD_TEST/`) | Not started |
| 11 | Risk Engine | Sizing, exposure caps, daily stop, max loss, kill switch, duplicate-trade and stale-signal prevention | Not started |
| 12 | Execution Robot | Only after sufficient evidence and controlled validation (`17_EXECUTION_ROBOT/`) | Not started |

Phases are gates, not suggestions. Do not begin work belonging to a later phase.

---

## 5. STUDENT-PHASE EXIT CRITERIA

Phase 1 is complete only when:

1. Every bootcamp video has been processed.
2. Every required lesson has passed mastery **and reviewer `PASS`**.
3. All available homework is complete.
4. Major concepts have been tested manually on historical GBP/USD charts.
5. Both positive and negative examples exist.
6. Every major rule has provenance.
7. Ambiguities are documented.
8. Contradictions are documented.
9. The concept library is sufficiently mature.
10. The course can be explained coherently from beginning to end.
11. The methodology can be applied to unseen charts with documented reasoning.
12. The repository is complete enough for a new researcher to independently
    understand what was learned.

Only then begin full-course synthesis and machine formalization.

---

## 6. REPRODUCIBILITY

Every important result must be reproducible. Record: source video, source
checksum, chart symbol, broker/data feed, timeframe, timezone, date range, script
version, Git commit, configuration, test parameters.

A future researcher must be able to recreate any result in this repository.
