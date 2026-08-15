# PHASE 2 FRESH-REVIEW HANDOFF — CLAUDE / NEXT AGENT

**Branch:** `phase2/cross-lesson-review`
**Submission state:** 14/14 V17–V20 and 13/13 V11/V13/V15 remediations applied; 25%/50%
cumulative reviews completed and halted on the existing NOT MASTERED student practical
**Required role:** fresh Independent Reviewer / Teacher Agent under D-003

## Read first

1. `00_SYSTEM/PHASE_2_GATE_AUDIT.md`
2. `00_SYSTEM/SELF_VERIFICATION_POLICY.md`
3. `00_SYSTEM/PHASE_2_REMEDIATION_LEDGER.md`
4. `00_SYSTEM/PHASE_2_V11_V15_REMEDIATION_LEDGER.md`
5. `00_SYSTEM/PHASE_2_HUMAN_RECONSTRUCTION_AUDIT.md`
6. `00_SYSTEM/PHASE_2_VALIDATION_REPORT.md`
7. `18_REVIEW/CUMULATIVE_25.md` and `18_REVIEW/CUMULATIVE_50.md`
8. `19_STUDENT_TEST_SUITE_V01_V10/attempts/AI_STUDENT_ATTEMPT_001/FINAL_GRADING_REPORT.md`
9. Original findings 109–113, 154–155, 197–202, 244–249, 264–268, 303–304, and 348 in
   `18_REVIEW/REVIEW_INDEX.md`

## Required independent work

1. Re-derive each of the fourteen findings from its original evidence before reading the applied
   edit in detail.
2. Verify each correction against source, not against the remediation ledger's description.
3. Write fresh V17 R2, V18 R2, V19 R2, and V20 R3 review files.
4. Independently re-derive the thirteen V11/V13/V15 fixes and write V11 R2, V13 R2, and V15 R2.
5. Preserve the original findings; append close-outs rather than overwriting review history.
6. Issue `PASS` only where the full lesson criteria and all findings support it.
7. Keep `FINAL_COURSE_REVIEW.md` `NOT STARTED` until all 21 lessons hold an independent `PASS`.

## Separate clean-student retest required

The reviewer work above cannot clear the cumulative mastery gate. A different clean Student session,
which must not read the instructor key or the existing answer rationale before locking answers, must
take a fresh targeted retest covering:

1. the C-001/V05 unresolved day-count contradiction;
2. exact setup retrieval for 22, 33, PFH+M, PFL+W, and safety trade — name, role, source tier,
   known conditions, and blockers;
3. the four V01 trap contexts and the V03 standard/mini/micro meanings;
4. separation of explicit inputs from inferred calculations or chart conclusions.

Do not reuse V05-06 verbatim. Preserve `AI_STUDENT_ATTEMPT_001` unchanged.

## Copy-ready continuation prompt

```text
Act as the fresh Independent Reviewer / Teacher Agent for MMM Phase 2 on branch
`phase2/cross-lesson-review`. You did not author the Phase 2 remediation.

Read the governing protocols and then:
1. independently re-derive and review items 109–113, 154–155, 197–202, 244–249, 264–268,
   303–304, and 348;
2. write V11 R2, V13 R2, V15 R2, V17 R2, V18 R2, V19 R2, and V20 R3, preserving all original findings;
3. run scripts/validate_project.py, scripts/validate_phase1.py, and
   scripts/validate_phase2.py;
4. audit the V09–V16 latest independent decisions and produce the exact remaining route to 21/21
   reviewer PASS;
5. do not start FINAL_COURSE_REVIEW.md unless its every-lesson-PASS precondition is actually true;
6. do not populate 12_MASTER_SPEC or 13_MACHINE_SPEC, adopt any draft decision, or claim a
   validated trading edge.

The Phase 1 claim of twelve V17–V20 minors was arithmetically wrong: the cited ranges total fourteen.
The broader formal census is 14/21 independent PASS. V09, V10, V12, V14, and V16 reached fresh
independent PASS; seven lessons retain latest independent verdict REVISE.

Also preserve the new cumulative result: CUMULATIVE_25 and CUMULATIVE_50 are completed but both say
HALT AND REMEDIATE. They rely on the independently graded V01–V10 attempt, which scored 96.3% yet is
NOT MASTERED because V05-06 falsely closed C-001. A separate clean Student session must pass the
targeted retest before CUMULATIVE_75 or FINAL_COURSE_REVIEW can begin.
```
