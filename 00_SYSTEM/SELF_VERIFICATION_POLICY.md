# SELF-VERIFICATION POLICY — PHASE 2 FORMALIZATION

## Governing rule

This file does not create a new owner decision. It restates active D-003, D-004, and D-024:

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
| All findings cleared in a fresh review round | reviewer `PASS` / lesson `COMPLETE` |

`COMPLETE — SELF-VERIFIED AT OWNER DIRECTION` is historical qualified language, not equivalent to
the last row. Cumulative and final reviews must count only independent `PASS` decisions.

## Owner-decision boundary

No new owner decision is needed to interpret the existing record. D-003/D-004 already answer the
certification question, and D-024 already answers progression after a minor-only independent
`REVISE`. If the owner chooses to waive a closed gate in a future case, that waiver must name its
scope and remain labelled `OWNER OVERRIDE`; it cannot authorize the authoring session to emit a
reviewer `PASS`, `CLOSED — VERIFIED`, or lesson `COMPLETE`.

## Phase 2 application

The current Phase 2 session is independent of the historical V09–V16 self-verification work, but it
authored the V17–V20 remediation edits. It may audit the older fixes, but it may not certify its own
new edits as an independent R2/R3. Those edits are therefore handed to a fresh reviewer.
