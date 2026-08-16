# Independent Grading Report — AI_STUDENT_PRACTICAL_001

Graded: 2026-08-16 by independent grader (no involvement in authoring answers).
Sources: SCORING_RUBRIC.md, PRACTICAL_EXAM_BLUEPRINT.md, INSTRUCTOR_ANSWER_KEY.md, instructor_only/REVEAL_PROTOCOL.md context. Attempt answers and key were not modified.

## Integrity verification

- Packet SHA-256 recomputed: MATCHES declared `1e7eb564…5bdcb`.
- Asset-index SHA-256 recomputed: MATCHES declared `31e7a131…8b3a41`.
- FIRST_ATTEMPT.md SHA-256 recomputed: MATCHES manifest `80c25087…70f691`.
- All 60 declared marked-chart SHA-256 values recomputed against files in `MARKED_CHARTS/`: 60/60 MATCH.
- **Integrity concern (material):** the manifest's own Forbidden-access disclosure records that, before packet-order processing reached E01/G01, the student inspected the eight E-block visible-only CSVs and the eight G-block source cards out of sequence. No instructor-only, key, holdout, or future-bar data was accessed, and the E CSVs terminate at their decision candles, so no within-case lookahead contamination is demonstrable. This is a sequencing violation, not a literal PCF-2 (the assets were assigned, not "adjacent unassigned data" or holdout). However, SUPERVISOR_VERIFICATION.md for attempt 002 records that this attempt "was preserved but rejected as the grading-ready attempt" for this incident. Attempt 001 also has no Phase B STAGED_RESPONSES.md (staged reveals carry no points, so no score impact).

**Ruling:** raw score is reported below for the record, but this attempt is ADMINISTRATIVELY NOT GRADING-READY per the exam administration's own rejection. The recorded outcome should rest on AI_STUDENT_PRACTICAL_002.

## Per-block scores

| Block | Cases | Max | Earned | % |
|---|---:|---:|---:|---:|
| A | 12 | 144 | 144 | 100.0% |
| B | 8 | 96 | 96 | 100.0% |
| C | 8 | 96 | 96 | 100.0% |
| D | 8 | 96 | 95 | 99.0% |
| E | 8 | 96 | 96 | 100.0% |
| F | 8 | 96 | 87 | 90.6% |
| G | 8 | 96 | 96 | 100.0% |
| **Total** | 60 | **720** | **710** | **98.6%** |

## Case-level deductions

- **D06 (−1):** classified UNRESOLVED; key requires INSUFFICIENT INFORMATION. Abstention is correct in kind and rationale (no V08 numeric boundary) matches the key, so only 1 classification point deducted. See key-defect note below.
- **F05 (−6):** student halved size to $4.00/pip after loss 3. Key: MAINTAIN the previously established $8.00/pip through loss 3; do not recalculate merely because balance fell. Classification 0/2, reasoning 0/2, measurement 0/2. Not a critical failure: resulting exposure ($100 ≈ 1.06%) is under the 2% cap, so PCF-6 does not trigger.
- **F06 (−3):** student applied a half-size $92/$3.68-per-pip figure. Key: after loss 4 recalculate full 2% of $9,200 → $184 and $7.36/pip. Measurement 0/2, reasoning 1/2 (sequence-boundary concept invoked but misapplied).

All other 57 cases match the key exactly in decision, extrema/OHLC values, pip arithmetic, markup declarations, provenance labeling, and lookahead declarations: 12/12 each.

## Hard gates (on raw score)

- Overall ≥85%: PASS (98.6%). Every block ≥80%: PASS (min 90.6%, Block F).
- Chart-markup component ≥85%: PASS (100%). Decision/reasoning ≥85%: PASS (≈97%).
- Block F ≥90%: PASS at 90.6% — by a single point.
- Provenance/uncertainty ≥90%: PASS. Lookahead 100%: PASS. No in-case critical failure.

**Result: raw PASS 710/720 (98.6%), superseded by administrative invalidation (attempt rejected as grading-ready by the supervising record). Remediation if re-credited: Block F V09 sequence rules (F05/F06 maintain-vs-recalculate boundary).**

## Top error patterns (10 max; only 3 observed)

1. Misapplied loss-sequence sizing: recalculating/halving inside the sequence when the rule maintains size (F05).
2. Wrong recalculation basis at the four-loss boundary: half-size instead of fresh 2% of current balance (F06).
3. Abstention-category confusion: UNRESOLVED vs INSUFFICIENT INFORMATION (D06).
4. Procedural: out-of-sequence asset access disclosed in manifest (integrity, not scored).
5. Procedural: Phase B staged-reveal record absent.
6–10. None observed.

## Abstention behavior

Excellent. All 8 B-block cases correctly withheld final PFH/PFL; all D-block abstentions carried correct missing-prerequisite rationales; F08 correctly refused $/pip with an undefined stop denominator (full credit per rubric for refusing unavailable arithmetic); G-block consistently limited screenshots to VISUAL evidence. No false certainty anywhere (no PCF-7).

## Key defects / ambiguities flagged (not regraded)

1. **INSUFFICIENT INFORMATION vs UNRESOLVED is nowhere operationally defined.** The key uses both across D-block cases (D01/D02/D06/D07 vs D03/D04/D05/D08) without a stated discrimination rule; the D06 one-point deduction is therefore contestable.
2. **Rubric vs key component-weight inconsistency.** SCORING_RUBRIC.md allocates markup 3 / measurement 2 / lookahead 1; the per-case "Scoring criteria" lines in the key allocate e.g. "exact range and breach 4; decision 2; markup 2; provenance 2; lookahead 2." Both sum to 12 but distribute differently; graders could produce divergent partial-credit results.
3. **PCF-2 wording gap.** PCF-2 covers "adjacent unassigned data" and holdouts but is silent on out-of-order access to *assigned* assets — exactly the 001 incident. The invalidation here rests on the supervisor record, not on rubric text.
4. Duplicate macOS folder artifacts ("charts 2", "sealed_reveals 2", "MARKED_CHARTS 2") create ambiguity about the canonical asset set; hashes in ASSET_INDEX.md resolve it but the duplicates should be removed.
