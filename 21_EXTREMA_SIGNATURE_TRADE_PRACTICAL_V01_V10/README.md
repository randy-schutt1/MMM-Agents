# Extrema and Signature-Trade Practical — Videos 1–10

## Purpose

This is a separate chart-heavy examination for the AI student. Every case requires the student to identify:

- high of the selected trading day (HOD);
- low of the selected trading day (LOD);
- high of the completed week (HOW/PFH retrospectively);
- low of the completed week (LOW/PFL retrospectively);
- any source-supported signature or separately named trade candidate.

## Critical terminology boundary

V10 explicitly designates the **safety trade with a second-leg element** as the student's official signature trade. V04's four-trade taxonomy—stop-hunt-high M, stop-hunt-low W, straightaway rise, and straightaway drop—and V02's 22/straightaway terminology are separate named teachings. They must not be silently relabelled as the official signature trade.

Raw chart shape alone cannot certify the V10 safety trade because several required inputs remain prospectively undefined through Video 10. Positive cases therefore provide explicit stipulations. Difficult cases intentionally require `UNRESOLVED` or `NONE CONFIRMABLE`.

## Two-phase administration

Each of the 46 cases uses two charts from one previously unused development week:

1. **Phase A:** The decision chart ends at the printed trading-day close. The student marks HOD/LOD and classifies the signature-trade checklist.
2. **Phase B:** After Phase A is immutable, the instructor reveals the completed week. The student marks HOW/LOW but may not revise the signature answer.

The printed trading-day window is an examination input: 17:00 through 16:45 fixed UTC-5. It does not claim to resolve the course's session-clock ambiguity.

## Composition

- 46 cases: the original 12 easy, 12 intermediate, and 12 difficult extrema/signature cases plus 10 direction-decision cases randomly mixed through the packet.
- The 10 added cases require `BUY`, `SELL`, `NO TRADE`, `DNC`, `WAIT`, or `UNRESOLVED` and explicit chart markup of the decision logic.
- 46 visible-only Phase-A charts and CSVs.
- 46 sealed completed-week charts and CSVs.
- 690 total points.
- Historical periods are distinct from the 63 weeks already used by the two earlier test suites.
- Development data only; no reserved holdout data.

## Files

- `STUDENT_TEST_PACKET.md` — student-facing two-phase cases.
- `INSTRUCTOR_ANSWER_KEY.md` — sealed exact prices, timestamps, and signature decisions.
- `SCORING_RUBRIC.md` — component scoring, hard gates, and critical failures.
- `TEST_BLUEPRINT.md` — architecture and difficulty design.
- `COVERAGE_MATRIX.md` — case mapping.
- `RESULTS_TEMPLATE.md` — immutable two-phase attempt ledger.
- `assets/ASSET_INDEX.md` — permitted Phase-A assets.
- `assets/DATA_PROVENANCE.md` — hashes and cutoffs.
- `instructor_only/REVEAL_PROTOCOL.md` — Phase-B reveal mapping.

## Administration firewall

The AI student receives only the student packet, results template, asset index, and currently assigned Phase-A chart/CSV. The answer key, completed-week assets, provenance report, scripts, previous attempts, and all other repository evidence remain sealed. Reveal one completed week only after its matching Phase-A answer and marked chart are locked and hashed.
