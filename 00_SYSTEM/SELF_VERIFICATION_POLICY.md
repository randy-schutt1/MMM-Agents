# SELF-VERIFICATION POLICY — PHASE 2 FORMALIZATION

## Governing rule

This file restates active D-003, D-004 and D-024 and incorporates owner ruling D-062:

- self-verification may show that a fix was attempted;
- self-verification itself never opens a progression gate. A separately recorded owner override
  may authorize progression, and a minor-only independent `REVISE` opens the next-lesson gate under
  D-024, but neither event turns the self-check into independent verification;
- it does not satisfy separation of duties;
- it does not produce an independent reviewer `PASS`;
- it does not make a lesson eligible for the final-course-review precondition.

## Canonical status language

| Situation | Required label |
|---|---|
| Fix applied by the authoring session | `APPLIED — AWAITING INDEPENDENT REVIEW` |
| Fix checked by the same session at owner direction | `CLOSED — SELF-VERIFIED AT OWNER DIRECTION` |
| Fix re-derived from source by a fresh reviewer | `CLOSED — VERIFIED` |
| Minor fixed by the independent reviewer at explicit owner direction under D-062 | `CLOSED — REVIEWER REMEDIATED AT OWNER DIRECTION` |
| All findings cleared in a fresh review round | reviewer `PASS` / lesson `COMPLETE` |

`COMPLETE — SELF-VERIFIED AT OWNER DIRECTION` is historical qualified language, not equivalent to
the last row. Cumulative and final reviews must count only independent `PASS` decisions.

## Owner-decision boundary

D-062 records the owner's intended reviewer workflow. An independent reviewer may fix and close its
own minor findings when the five D-062 conditions hold. This makes the lesson complete without
rewriting the historical `REVISE` as a `PASS`. A Student still cannot certify its own submission,
and a closed gate with unresolved critical/major findings still requires correction under D-024.

## Phase 2 application

The Phase 2 remediation for V11, V13, V15 and V17–V20 is closed under D-062 at the owner's explicit
direction. The closeout does not claim a third-session verification; it records that the independent
reviewer was instructed to fix and approve the minor issues. V19's corrected reporting major and
V20's already independently closed majors retain their full historical disclosures.
