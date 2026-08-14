# Test Suite Blueprint

## Architecture

The suite contains **88 scored cases**:

| Block | Cases | Count |
|---|---:|---:|
| V01, V05, V07, V09 individual lesson blocks | 6 per video | 24 |
| V02, V03, V04, V06, V08 individual lesson blocks | 7 per video | 35 |
| V10 individual lesson block | 9 | 9 |
| Cumulative weekly/sequence/provenance block | I01–I08 | 8 |
| Risk and calculation integration block | I09–I14 | 6 |
| Ambiguity/contradiction/hindsight block | I15–I20 | 6 |

Each case is worth 10 raw points before penalties, for 880 total raw points. The same case may assess several mastery dimensions; primary-plus-secondary mappings appear in the coverage matrix.

## Case balance

Minimum design targets:

- Positive/valid: at least 20.
- Negative/lookalike: at least 20.
- Borderline/insufficient/unresolved: at least 20.
- Neutral recall/calculation/provenance: remainder.
- Foundational/intermediate/advanced/integration: all represented.
- At least 12 cases use visible-only GBP/USD development charts or source-card visuals.
- At least 10 cases require calculations or quantitative risk work, including cumulative exposure and loss/win sizing sequence.
- At least 12 cases require chart markup.
- At least 12 cases require an explicit `UNRESOLVED`/`NO VALID CONCLUSION` response.
- At least 8 cases explicitly separate rule application from trade outcome.

## Major recognition clusters

Because course geometry remains partly undefined, recognition clusters are framed around conditions the recording actually supplies. Each cluster has at least 3 valid, 3 invalid/lookalike, and 2 borderline/insufficient cases:

| Cluster | Valid | Invalid/lookalike | Borderline/insufficient |
|---|---|---|---|
| Weekly context and first-move discipline | V01-02, V01-03, I01 | V01-04, V03-06, I02 | V01-05, V02-04, I03 |
| V04 instructor sequence | V04-01, V04-02, I04 | V04-03, V04-04, I05 | V04-05, V04-06, I06 |
| High-low drill/basic confirmation | V08-01, V08-02, I07 | V08-03, V08-04, I08 | V08-05, V08-06, I17 |
| V10 safety-trade checklist | V10-02, V10-09, I09 | V10-03, V10-04, I10 | V10-05, V10-06, V10-07 |

“Valid” means the stated case facts satisfy the cited course condition. It does not mean the course has demonstrated positive expectancy. Where a chart alone cannot establish the undefined facts, the only correct classification is insufficient evidence.

## Competency and mastery-dimension coverage

| Dimension | Minimum cases | What is tested |
|---|---:|---|
| Recall | 8 | Faithful terminology and cautions |
| Recognition | 12 | Source-grounded conditions and visible-only charts |
| Discrimination | 12 | Lookalikes, missing prerequisites, pass decisions |
| Sequence | 10 | Before/setup/confirm/invalidate/after |
| Exceptions | 8 | Beginner/advanced, overshoot, obvious stop hunts, re-entry |
| Homework application | 8 | Flashcards, R&D, H4→M15, hard-right-edge preservation |
| Manual backtesting | 8 | Pre-registration, nulls, holdout, outcome separation |
| Provenance | 10 | Evidence tier and label selection |
| Ambiguity handling | 12 | Correct uncertainty and `DO NOT CODE` discipline |
| Contradiction handling | 10 | Preserve both sources and apply hierarchy |

These are primary-plus-secondary mappings, not mutually exclusive buckets. The generated `COVERAGE_MATRIX.md` is the controlling case-level map and `VALIDATION_SUMMARY.json` records the achieved counts.

## Anti-lookahead design

- `assets/charts/` images end exactly at the decision timestamp and contain no later candles.
- Visible-only CSV files end at the same timestamp.
- Student materials never report future direction, target, stop, profit, or loss.
- Instructor answers grade only information available at the decision point, except cases explicitly asking the student to audit a previously disclosed historical study.
- Outcome-reveal exercises use hypothetical outcomes that are irrelevant to the original classification.
- Any answer changed after reveal is preserved as a second attempt, never substituted for the first.

## Data boundary

All generated charts use HistData GBP/USD development data no later than 2015-12-31, fixed UTC−5 Arm A. They do not open or reference the `2016-07-01 → 2017-12-29` holdout. Source-card visuals remain tied to their lesson screenshot and may have unknown market dates; that limitation is explicit.

## Administration forms

Allowed classification choices, where used: `VALID`, `INVALID`, `BORDERLINE`, `INSUFFICIENT INFORMATION`, `UNRESOLVED`, `NO TRADE`, `NOT A COURSE RULE`. Free-response justification and provenance are always required even when a choice is supplied.

## Why 88 cases

Sixty cases would cover the ten lessons only once per dimension and would under-sample the large uncertainty/provenance burden. The original 80-case architecture supplied repeated discrimination, recognition clusters, risk-sequence calculations, and cumulative cases. A completion audit added seven source-grounded material-gap cases plus one independent valid V10 safety-sequence case, producing 88 cases without turning undefined chart geometry into invented rules.
