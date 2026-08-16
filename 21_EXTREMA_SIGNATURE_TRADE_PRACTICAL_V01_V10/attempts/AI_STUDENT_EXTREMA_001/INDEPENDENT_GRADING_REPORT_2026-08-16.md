# Independent Grading Report — AI_STUDENT_EXTREMA_001

- Grader: Independent AI grader (no prior involvement in authoring this attempt)
- Date: 2026-08-16
- Materials used: SCORING_RUBRIC.md, TEST_BLUEPRINT.md, INSTRUCTOR_ANSWER_KEY.md, instructor_only/REVEAL_PROTOCOL.md, attempt files, assets/decision_csv (independent recomputation)
- Method: Machine-parsed key and both response files; exact-match comparison of all HOD/LOD/HOW/LOW price+timestamp pairs; manual adjudication of all 46 signature/direction classifications and reasoning against the key; hash and ledger verification; independent recomputation of all 92 key HOD/LOD values from the assigned CSVs.

## Result

| Component | Earned | Possible | % |
|---|---:|---:|---:|
| HOD/LOD (Phase A extrema) | 184 | 184 | 100% |
| HOW/LOW (Phase B extrema) | 184 | 184 | 100% |
| Signature/direction classification | 55 | 92 | 59.8% |
| Signature reasoning/sequence | 74 | 92 | 80.4% |
| Provenance/uncertainty | 92 | 92 | 100% |
| Lookahead/lock integrity | 46 | 46 | 100% |
| **TOTAL** | **635** | **690** | **92.0%** |

**Overall verdict: FAIL** — overall score 635/690 (92.0%) clears the 587/690 threshold, but the attempt fails the mandatory **signature classification/reasoning gate: 129/184 = 70.1% (< 85% required)**. No critical failure (ECF-1..9) was identified, so this is a gate failure, not an invalidated attempt. Per rubric, remediation targets the signature checklist, with both fully stipulated and raw-chart retest cases.

## Per-tier and per-family scores

| Family | Cases | Earned | Possible | % | Gate | Status |
|---|---:|---:|---:|---:|---|---|
| Easy (E01–E12) | 12 | 165 | 180 | 91.7% | ≥80% | PASS |
| Intermediate (I01–I12) | 12 | 160 | 180 | 88.9% | ≥80% | PASS |
| Difficult (D01–D12) | 12 | 180 | 180 | 100% | ≥80% | PASS |
| Mixed direction (M01–M10) | 10 | 130 | 150 | 86.7% | ≥85%, no unsupported BUY/SELL | PASS (no unsupported BUY/SELL made) |
| Combined HOD/LOD/HOW/LOW | 46 | 368 | 368 | 100% | ≥90% | PASS |
| Signature classification+reasoning | 46 | 129 | 184 | 70.1% | ≥85% | **FAIL** |
| Provenance/uncertainty | 46 | 92 | 92 | 100% | ≥90% | PASS |
| Lookahead/lock integrity | 46 | 46 | 46 | 100% | =100% | PASS |

## Per-case signature scoring (classification 2 + reasoning 2)

- **4/4 (25 cases):** E01–E07, I01, I02, I04, I10, M03, M07, D01–D12. Correct state and controlling prerequisite. D-tier "NONE CONFIRMABLE" matches the key's "UNRESOLVED / NONE CONFIRMABLE".
- **3/4 (4 cases):** I08, I09, M09 (student NONE CONFIRMABLE vs key UNRESOLVED — same epistemic verdict, wrong state label: 1+2); M04 (student "VALID CHECKLIST — DOWN direction" vs key SELL — direction correct but the required M-case decision vocabulary/commitment was not used: 1+2).
- **1/4 (17 cases):** two systematic error patterns, each scored 0 classification + 1 reasoning (correct controlling fact identified, wrong terminal state):
  - **WAIT/UNRESOLVED collapsed to INVALID (8):** E08, E10, E11, E12, I07, M06, M08, M10. A single missing/unclear prerequisite (second leg, pull-away, consolidation, peak identity) was labeled INVALID where the key requires WAIT, INCOMPLETE, UNRESOLVED, or NO TRADE.
  - **Evasive abstention where the key is determinate (8):** E09, I03, I05, I11, I12, M01, M02, M05 answered NONE CONFIRMABLE where the key holds VALID (I03), BUY (M01), SELL (M02), INVALID/DNC (E09, I05), NO TRADE/DNC (M05), or a stipulated 22/straightaway candidate (I11, I12). The student declared stipulated facts (direction, stop hunt, peak) "UNRESOLVED" that the key treats as supplied.
  - (E08 counted once in the first pattern; total distinct = 17 with M06 in pattern one.)

## Abstention analysis

Abstention dispositions (NONE CONFIRMABLE / WAIT / UNRESOLVED): **25 of 46 cases** (24 NONE CONFIRMABLE + 1 WAIT).

- **Correct/allowed abstentions: 17/25 (68%)** — D01–D12 (12), I06, I08, I09, M09 (key also abstains; I06 mislabeled WAIT→NONE CONFIRMABLE but same refusal), M07 (WAIT, exact).
- **Evasive abstentions: 8/25 (32%)** — E09, I03, I05, I11, I12, M01, M02, M05, where the key had a determinate answer. Most costly: M01 (BUY) and M02 (SELL), where the key states all prerequisites were stipulated and the student still refused to commit.

The abstention-heavy style was fully vindicated on the raw-chart D tier (perfect) but was over-applied to stipulated-fact cases: the student repeatedly demoted printed stipulations to "UNRESOLVED".

## Integrity review

- **Hashes:** Packet, Phase-A, Phase-B, and growth-notebook SHA-256 values in the manifest all verify against files on disk. All 92 marked-chart hashes verify; all 92 files exist. No forbidden-access or revision declarations; Phase-B responses copy Phase-A decisions verbatim (spot-checked; consistent).
- **Lookahead:** All 46 Phase-A locks (last: 21:32:52) precede all corresponding Phase-B locks (earliest batch: 21:35:42+ except E01–E04, which follow per-case). No ECF-1/ECF-2 evidence. Lock integrity scored 46/46.
- **29-minute completion — concern, not a violation:** E01–E04 show realistic per-case pacing (2–4 min each). From E05 onward, 42 Phase-A locks are stamped ~1 second apart (21:32:31–21:32:52) and all remaining Phase-B locks fall within a 3-second window. Combined with verbatim-templated reasoning blocks (identical wording across cases with only stipulation values substituted), the work was clearly batch-generated, which is inconsistent with the manifest's declared "Sequential two-phase, one case at a time" administration. Because the answers derive correctly from the assigned CSVs (independently recomputed) and no key access is indicated, this is flagged as a **ledger-credibility concern** for the supervisor, not a critical failure.

## Key defects (flagged, not regraded)

1. **Missing reveal assets:** `instructor_only/REVEAL_PROTOCOL.md` references `completed_week_reveals/FULL_*.png` and `completed_week_csv/FULL_*.csv` for all 46 cases, but neither directory exists anywhere in the exam package. Phase-B HOW/LOW therefore cannot be independently verified against source data (student values match the key exactly, but the common source is unverifiable). This also means the administered reveal provably used files outside the archived package.
2. **Key HOD/LOD verified clean:** all 92 key HOD/LOD values were independently recomputed from `assets/decision_csv/DEC_*.csv` over the printed 17:00–16:45 windows using first-matching wick timestamps — zero discrepancies.
3. **State-label granularity:** the key uses compound states ("WAIT/INCOMPLETE", "INVALID/DNC", "UNRESOLVED / NONE CONFIRMABLE") while the rubric lists atomic states; the rubric gives no partial-credit rule for adjacent abstention labels (UNRESOLVED vs NONE CONFIRMABLE). This grading awarded 1/2 classification for adjacent-abstention labels; a published equivalence table would remove grader discretion.

## Top error patterns (ranked by points lost)

1. Collapsing WAIT/UNRESOLVED/NO TRADE states into INVALID when any prerequisite was missing (8 cases, ~24 pts lost).
2. Evasive NONE CONFIRMABLE where stipulations were determinate, including refusing the supported BUY (M01) and SELL (M02) (8 cases, ~24 pts lost).
3. Not using the M-case decision vocabulary (M04 "DOWN" instead of SELL; ~1 pt).
4. Missing separately stipulated 22/straightaway candidates (I11, I12).

No answers or key content were modified.
