# PHASE 2 TARGETED RETEST 001

## Purpose

Clear—or confirm—the cumulative mastery failure recorded in `CUMULATIVE_25.md` and
`CUMULATIVE_50.md`. This is a targeted retest, not a substitute for the seven outstanding lesson
reviews or the 75%/final course reviews.

## Role separation

1. A **clean Student session** may read only `STUDENT_PACKET.md` and `RESULTS_TEMPLATE.md` before
   locking all ten answers. It must not search the repository, read the prior attempt, or open
   `INSTRUCTOR_KEY.md`.
2. The Student saves the completed results as a new immutable file beside this README and records
   its SHA-256.
3. Only after the lock may a separate **Instructor/Reviewer session** open `INSTRUCTOR_KEY.md`,
   grade the locked answers, and append a grading report. First answers are never overwritten.

## Copy-ready clean-student prompt

```text
Act as the clean Student Agent for PHASE_2_TARGETED_RETEST_001. Read only STUDENT_PACKET.md and
RESULTS_TEMPLATE.md in this retest folder. Do not open INSTRUCTOR_KEY.md, prior attempts, lesson
files, review files, or search the repository. Answer all ten cases from retained course knowledge,
state provenance and confidence, write FUTURE INFORMATION USED: NO for every case, then lock the
complete first attempt with a timestamp and SHA-256. Do not self-grade.
```

## Gate rule

Passing this retest clears only the cumulative student-remediation item. `CUMULATIVE_75.md` still
requires V01–V16 independent lesson PASS, and `FINAL_COURSE_REVIEW.md` still requires all 21.
