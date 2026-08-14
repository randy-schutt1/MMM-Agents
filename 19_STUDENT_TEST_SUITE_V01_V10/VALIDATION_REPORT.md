# Validation Report

## Result

The suite passed its build and integrity checks. This is an assessment-artifact validation, not a claim that Videos 1–10 define a complete trading strategy or demonstrate a profitable edge.

## Case integrity

- 88 unique case IDs occur once each in the student packet, instructor key, and coverage matrix.
- All 88 instructor cases contain a correct answer, evidence-based reasoning, traceable citation, expected-answer provenance label, reasoning sequence, rejection/invalidation conditions, ambiguity field, scoring criteria, common errors, difficulty, and lookahead check.
- The student packet contains no `Correct answer` or `Evidence-based reasoning` fields.
- Actual hypothetical outcome reveals are retained only in the instructor key. Student cases that test outcome/application separation require the first classification to be locked before an instructor reveal.
- Distribution: 34 positive/valid, 22 negative/lookalike, 21 borderline/insufficient, and 11 evidence-neutral cases.
- Difficulty: 25 foundational, 23 intermediate, 25 advanced, and 15 integration cases.
- Each Video 1–10 has at least six individual cases; 20 additional cases integrate lessons, risk, evidence, ambiguity, contradictions, and hindsight control.

## Coverage checks

The primary-plus-secondary coverage audit records: Recall 16, Recognition 52, Discrimination 45, Sequence 88, Exceptions 16, Homework application 10, Manual backtesting 13, Provenance 88, Ambiguity handling 81, and Contradiction handling 12. Every case requires a sequence and a provenance response even when those are not the primary competency.

The four major recognition clusters in `TEST_SUITE_BLUEPRINT.md` each contain at least three valid, three invalid/lookalike, and two borderline/insufficient cases. Undefined geometry is tested by correct refusal or by explicitly stipulated facts, never by an invented raw-chart rule.

`MATERIAL_CONCEPT_CROSSWALK.md` independently maps every material lesson/control cluster to multiple cases and records the course-versus-unresolved boundary for each.

## Data and lookahead checks

- Eleven chart images and eleven matching CSV slices were generated from the HistData GBP/USD M15 development corpus, fixed UTC−5 Arm A.
- Each CSV begins at its verified Sunday 17:00 week-open boundary and ends exactly at its printed decision timestamp. The ten partial-week slices contain 34–173 observations; the completed-week retrospective slice contains 480 observations.
- CH01 and CH04 were independently recomputed after the first audit: their final bars are exactly the first post-opening-band breaches (2013-02-04 02:15 and 2014-02-10 01:15 fixed UTC−5). The earlier noon timestamps were rejected and replaced.
- Every generated image states `NO LATER CANDLES INCLUDED` and was made only from its matching visible-only slice.
- Chart dates run from 2013 through 2015. The reserved holdout beginning 2016-07-01 was neither present in the slices nor opened.
- The blue first-eight-hours range is clearly labelled as an administration aid, not a claimed universal course definition.
- Visual inspection of CH01 confirmed legibility, decision-time truncation, timezone/data-arm labelling, and the source-boundary warning.

## Provenance checks

- Current V01–V10 source SWFs were rehashed directly from disk; all ten SHA-256 digests matched `00_SYSTEM/SOURCE_MANIFEST.md`. No V11 source file, transcript, notes, screenshot, or review artifact was opened.
- All citation filenames and all cited `BT_`/`PT-` identifiers resolve within the repository.
- Eight source-card assets are byte-for-byte copies of their indexed V04, V07, V08, V09, and V10 screenshots; all source/destination SHA-256 comparisons matched.
- `assets/DATA_PROVENANCE.md` records a SHA-256 digest and source/scope entry for every chart, CSV, and source card.
- Expected answers are assigned a primary `EXPLICIT`, `VISUAL`, `INFERRED`, or `UNRESOLVED` provenance label. No expected answer required the weaker `IMPLIED` category; the category remains available for student claim-level labelling.

## Repository checks

The repository's own `scripts/validate_project.py` completed with **103 passed, 0 warnings, 0 failures**. Git inspection shows only the new `19_STUDENT_TEST_SUITE_V01_V10/` directory is untracked; no pre-existing source, transcript, review, result, decision, or append-only record was modified.

## Known limits retained

- V09 and V10 remain self-verified at owner direction, not normally independently passed.
- The concept library and existing chart-example folders remain incomplete; this suite does not alter them.
- Core definitions including level, blue-box construction, second-leg/M/W anatomy, stop-hunt boundary, and TDI remain constrained or unresolved.
- V10 supplies no safety-trade stop rule and defers TDI to V11. No V11 material was opened or used.
- Historical findings remain development-period evidence only and do not establish profitability.
