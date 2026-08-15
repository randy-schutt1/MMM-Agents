# PHASE 2 REMAINING-WORK HANDOFF

**Branch:** `phase2/cross-lesson-review`
**Lesson review state:** **21/21 reviewed and approved; zero lesson-review backlog**
**Authority:** D-062 and `18_REVIEW/PHASE_2_OWNER_REVIEWER_CLOSEOUT.md`

## Completed

- All 27 Phase 2 findings are corrected and closed.
- V11, V13, V15 and V17–V20 are complete under owner-authorized reviewer remediation.
- The historical `REVISE` records remain append-only; no review verdict was rewritten.
- The 25% and 50% cumulative reviews are complete.
- Self-verification and owner-authorized reviewer remediation now have distinct, explicit labels.

## Remaining gate

The existing V01–V10 student practical scored 96.3% but is formally `NOT MASTERED` because V05-06
falsely closed C-001. A clean Student session must take the sealed targeted retest before the 75%
and final reviews begin.

### Clean Student files

- `19_STUDENT_TEST_SUITE_V01_V10/retests/PHASE_2_TARGETED_RETEST_001/STUDENT_PACKET.md`
- `19_STUDENT_TEST_SUITE_V01_V10/retests/PHASE_2_TARGETED_RETEST_001/RESULTS_TEMPLATE.md`

The Student must not open `INSTRUCTOR_KEY.md`, prior attempts, lesson files or review files before
locking all ten answers. The session that authored/read the key cannot take the Student role.

## After the retest

1. Grade the immutable attempt in a separate instructor session.
2. If it passes, change the 25%/50% checkpoint dispositions from halted to cleared by retest,
   preserving their original decisions.
3. Complete `CUMULATIVE_75.md` over V01–V16.
4. Complete `FINAL_COURSE_REVIEW.md` over all 21 lessons.
5. Do not populate `12_MASTER_SPEC/` or `13_MACHINE_SPEC/` unless final review authorizes it.

## Copy-ready clean Student prompt

```text
Act as the clean Student Agent for PHASE_2_TARGETED_RETEST_001 on branch
phase2/cross-lesson-review. Read only README.md, STUDENT_PACKET.md and RESULTS_TEMPLATE.md inside
that retest folder. Do not open INSTRUCTOR_KEY.md, prior attempts, lesson files, review files, or
search the repository. Answer all ten cases, record provenance/confidence/missing information and
FUTURE INFORMATION USED: NO, then lock the complete attempt with timestamp and SHA-256. Do not
self-grade.
```

## Boundary

This handoff does not claim setup codability or trading edge. `DO NOT CODE` records remain binding,
and empirical tests retain their development-sample and operationalization limitations.
