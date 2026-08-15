# PHASE 2 FRESH-REVIEW HANDOFF — CLAUDE / NEXT AGENT

**Branch:** `phase2/cross-lesson-review`
**Submission state:** 14/14 V17–V20 remediations applied; automated validation PASS
**Required role:** fresh Independent Reviewer / Teacher Agent under D-003

## Read first

1. `00_SYSTEM/PHASE_2_GATE_AUDIT.md`
2. `00_SYSTEM/SELF_VERIFICATION_POLICY.md`
3. `00_SYSTEM/PHASE_2_REMEDIATION_LEDGER.md`
4. `00_SYSTEM/PHASE_2_HUMAN_RECONSTRUCTION_AUDIT.md`
5. `00_SYSTEM/PHASE_2_VALIDATION_REPORT.md`
6. Original findings 244–249, 264–268, 303–304, and 348 in `18_REVIEW/REVIEW_INDEX.md`

## Required independent work

1. Re-derive each of the fourteen findings from its original evidence before reading the applied
   edit in detail.
2. Verify each correction against source, not against the remediation ledger's description.
3. Write fresh V17 R2, V18 R2, V19 R2, and V20 R3 review files.
4. Preserve the original findings; append close-outs rather than overwriting review history.
5. Issue `PASS` only where the full lesson criteria and all findings support it.
6. Separately audit the remaining V11, V13, and V15 non-PASS backlog. V09, V10, V12, V14, and V16
   reached independent `PASS`; do not treat V19's owner-directed self-verification as independent.
7. Keep `FINAL_COURSE_REVIEW.md` `NOT STARTED` until all 21 lessons hold an independent `PASS`.

## Copy-ready continuation prompt

```text
Act as the fresh Independent Reviewer / Teacher Agent for MMM Phase 2 on branch
`phase2/cross-lesson-review`. You did not author the Phase 2 remediation.

Read the governing protocols and then:
1. independently re-derive and review items 244–249, 264–268, 303–304, and 348;
2. write V17 R2, V18 R2, V19 R2, and V20 R3, preserving all original findings;
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
```
