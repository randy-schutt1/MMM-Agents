# Independent Grading Report — AI_STUDENT_PRACTICAL_002

Graded: 2026-08-16 by independent grader (no involvement in authoring answers).
Sources: SCORING_RUBRIC.md, PRACTICAL_EXAM_BLUEPRINT.md, INSTRUCTOR_ANSWER_KEY.md. Attempt answers and key were not modified.

## Integrity verification

- Packet and asset-index SHA-256 recomputed: MATCH declared values in ATTEMPT_MANIFEST.md.
- FIRST_ATTEMPT.md SHA-256 recomputed: `fc029aef…5d9a9a` — MATCHES SUPERVISOR_VERIFICATION.md freeze record (and recorded as unchanged after Phase B reveals).
- Supervisor record: 60/60 marked-chart hashes verified, locks present, forbidden access NONE, reveal material not accessed pre-freeze; Phase B (A01–A04 staged reveals) 4/4 verified with Phase A responses reproduced verbatim.
- Minor formatting anomalies, no score impact: literal leading `+` characters throughout FIRST_ATTEMPT.md (writer artifact) and a duplicate D07 ledger row in the manifest; both were disclosed in the supervisor record and content is complete and machine-verifiable.
- No integrity concerns affecting validity.

## Per-block scores

| Block | Cases | Max | Earned | % |
|---|---:|---:|---:|---:|
| A | 12 | 144 | 144 | 100.0% |
| B | 8 | 96 | 96 | 100.0% |
| C | 8 | 96 | 96 | 100.0% |
| D | 8 | 96 | 95 | 99.0% |
| E | 8 | 96 | 96 | 100.0% |
| F | 8 | 96 | 96 | 100.0% |
| G | 8 | 96 | 96 | 100.0% |
| **Total** | 60 | **720** | **719** | **99.9%** |

## Case-level deductions

- **D06 (−1):** classified UNRESOLVED; key requires INSUFFICIENT INFORMATION. The abstention, the identified missing input (V08 supplies no numeric fast/slow threshold), and provenance handling all match the key, so only 1 classification point is deducted. Flagged below as a contestable key ambiguity.

All other 59 cases match the key exactly: A-block band extrema/breach candles/NO TRADE, B-block extrema-so-far with INSUFFICIENT INFORMATION, C-block PFH/PFL and pip ranges to the decimal, D-block abstentions with correct rationales, E-block CONFIRMED/ENTER (E01–E04) and WAIT (E05–E08), F-block including the two sequence traps (F05 maintain $8.00/pip; F06 recalculate $184 → $7.36/pip) and F08's correct refusal, and G-block visual-evidence audits including the G03 pre-outcome crop.

## Hard gates

- Overall ≥85%: PASS (99.9%). Every block ≥80%: PASS (min 99.0%).
- Chart-markup ≥85%: PASS (100%). Decision/reasoning ≥85%: PASS (≈99%).
- Block F ≥90%: PASS (100%). Provenance/uncertainty ≥90%: PASS (100%).
- Lookahead 100%: PASS. No critical failures (PCF-1 through PCF-8 all clear).

**Result: PASS — 719/720 (99.9%).**

## Top error patterns (10 max; only 1 substantive observed)

1. Abstention-category confusion: UNRESOLVED where the key specifies INSUFFICIENT INFORMATION (D06 only).
2. Cosmetic: `+`-prefixed lines in the locked response file (writer artifact, disclosed).
3. Cosmetic: duplicate D07 ledger row in the manifest (disclosed; underlying record unique).
4–10. None observed.

## Abstention behavior

Exemplary and correctly calibrated. Confidence was stated numerically per case and was appropriately reduced exactly where the packet leaves rules underdefined (F05 0.78, F06 0.84, G03 0.88) while remaining high on measurable facts. Every abstention names the specific missing prerequisite rather than a generic "unclear." F08 earns full measurement credit under the rubric's refusing-unavailable-arithmetic clause. No false certainty (no PCF-7) and no fabricated geometry/thresholds (no PCF-3).

## Key defects / ambiguities flagged (not regraded)

1. **INSUFFICIENT INFORMATION vs UNRESOLVED undefined.** The key mixes both labels across D-block answers with no discrimination rule in the rubric or packet; the sole deduction here (D06) hinges on that unstated distinction. Recommend either defining the boundary or treating the two as equivalent abstentions for scoring.
2. **Component-weight inconsistency.** SCORING_RUBRIC.md (markup 3, measurement 2, lookahead 1) conflicts with the key's per-case "Scoring criteria" lines (e.g., extrema 4, markup 2, lookahead 2). Both sum to 12; graders should be told which controls.
3. **E-block answer phrasing.** Key answers for E01–E04 say "for LONG" but E05–E08 key text does not state the stipulated direction; the packet stipulations (SHORT for E05–E07, LONG for E08 per the attempt record) carry it. Harmless here, but the key should restate direction.
4. Duplicate macOS folder artifacts ("charts 2", "source_cards 2", "sealed_reveals 2") should be purged to keep the canonical asset set unambiguous.
