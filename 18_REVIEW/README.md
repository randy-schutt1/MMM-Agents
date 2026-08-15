# 18_REVIEW

Independent review records. Maintained by the Reviewer Agent.

## STATUS: 21 / 21 LESSONS REVIEWED AND APPROVED; TARGETED RETEST PASSED; 75% REVIEW NEXT

## STRUCTURE

```text
18_REVIEW/
├── REVIEW_INDEX.md          ← decisions, error counts, open items
├── CUMULATIVE_25.md         ← completed; HALT AND REMEDIATE
├── CUMULATIVE_50.md         ← completed; HALT AND REMEDIATE
├── CUMULATIVE_75.md         ← template
├── FINAL_COURSE_REVIEW.md   ← template
└── VXX/
    ├── VXX_REVIEW_R1.md
    └── VXX_REVIEW_R2.md
```

## THE GATE

```text
PASS      → advancement authorized
REVISE    → specific correctable deficiencies
BLOCKED   → foundational problem
```

**Reviewer `PASS` is the only decision that authorizes progression to the next
lesson** (`DECISIONS.md` D-004). A student mastery report of `PASS` is a
submission, not an authorization.

## VERSIONING

**Never overwrite an earlier review.** Each round is its own file, and each round
gets its own row in `REVIEW_INDEX.md`. The progression from `REVISE` to `PASS` is
part of the learning record, not clutter to tidy away
(`SETUP_ISSUES.md` I-002).

## INDEPENDENCE

Reviews run in a **fresh session** that did not produce the work, and inspect
source evidence **before** the student's conclusions (`DECISIONS.md` D-003). A
reviewer that just wrote the notes cannot independently evaluate them.

Protocol: `00_SYSTEM/REVIEW_PROTOCOL.md`
Prompt: `00_SYSTEM/REVIEWER_SESSION_PROMPT.md`
Template: `00_SYSTEM/TEMPLATES/REVIEW_TEMPLATE.md`
