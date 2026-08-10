# REVIEW INDEX

Master record of every independent review decision, and the project's running
error statistics.

Maintained by the Reviewer Agent. Append-only for decisions — a superseded decision
stays visible with its round number.

---

## STATUS

```text
LESSONS REVIEWED: 0
PASSED:           0
IN REMEDIATION:   0
AWAITING REVIEW:  0
```

No lesson has been studied or reviewed. See `README.md` §11.

---

## DECISION TABLE

| Video | Student Status | Review Version | Reviewer Decision | Critical Issues | Major Issues | Final |
|---|---|---|---:|---:|---:|---|
| _(no lessons reviewed)_ | | | | | | |

### Row template

```text
| V01 | PASS | R1 | REVISE | 0 | 2 | ⏳ |
| V01 | PASS | R2 | PASS   | 0 | 0 | ✅ |
```

Each review round gets its **own row**. Earlier rows are never edited or removed —
the progression from `REVISE` to `PASS` is part of the learning record.

### Legend

| Symbol | Meaning |
|---|---|
| ✅ | Reviewer PASS — advancement authorized |
| ⏳ | REVISE — in remediation |
| ⛔ | BLOCKED — substantial remediation required |
| 🔍 | Awaiting review |
| 👤 | Human review required |
| — | Not yet reached |

**Student Status** uses the student vocabulary (`PASS` / `REVIEW REQUIRED` /
`BLOCKED`); **Reviewer Decision** uses the reviewer vocabulary (`PASS` / `REVISE` /
`BLOCKED`). They are different actors' judgements and are deliberately not merged
(`SETUP_ISSUES.md` I-001).

---

## RECURRING ERROR COUNTS

Updated after every review. Reveals systematic weakness over time — a code that
keeps recurring is a training problem, not a lesson problem.

| Code | Description | Count | Lessons |
|---|---|---:|---|
| E01 | Source misquote | 0 | |
| E02 | Unsupported generalization | 0 | |
| E03 | Missed qualifier | 0 | |
| E04 | Wrong sequence | 0 | |
| E05 | Wrong pattern boundary | 0 | |
| E06 | False positive | 0 | |
| E07 | False negative | 0 | |
| E08 | Hindsight contamination | 0 | |
| E09 | Cherry-picking | 0 | |
| E10 | Incomplete homework | 0 | |
| E11 | Missing provenance | 0 | |
| E12 | Ambiguity treated as rule | 0 | |
| E13 | Contradiction ignored | 0 | |
| E14 | Outcome confused with correctness | 0 | |
| E15 | Machine assumption introduced prematurely | 0 | |
| E16 | Terminology drift | 0 | |
| E17 | Missing negative examples | 0 | |
| E18 | Invalid manual-backtest procedure | 0 | |
| E19 | Data/timeframe inconsistency | 0 | |
| E20 | Other | 0 | |

**Escalation rule:** any code reaching 3 occurrences is a systematic weakness.
Note it in the next cumulative review and consider whether the student protocol
itself needs strengthening — not just the individual lesson.

---

## SEVERITY TOTALS

| Severity | Total | Open |
|---|---:|---:|
| CRITICAL | 0 | 0 |
| MAJOR | 0 | 0 |
| MINOR | 0 | 0 |
| NOTE | 0 | 0 |

A lesson with unresolved CRITICAL issues cannot pass.

---

## OPEN RESEARCH ITEMS CARRIED FORWARD

Non-foundational issues that permitted a `PASS` but must not be forgotten.

| # | From | Item | Where tracked | Status |
|---|---|---|---|---|
| _(none)_ | | | | |

---

## HUMAN REVIEW QUEUE

| # | Lesson | Issue | Why a human is needed | Status |
|---|---|---|---|---|
| _(none)_ | | | | |

---

## CUMULATIVE REVIEWS

| Checkpoint | Trigger | File | Status |
|---|---|---|---|
| 25% | TBD at ingestion | `CUMULATIVE_25.md` | Not started |
| 50% | TBD at ingestion | `CUMULATIVE_50.md` | Not started |
| 75% | TBD at ingestion | `CUMULATIVE_75.md` | Not started |
| Final | All lessons passed | `FINAL_COURSE_REVIEW.md` | Not started |

---

## REVIEW FILE LOCATIONS

```text
18_REVIEW/VXX/VXX_REVIEW_R1.md
18_REVIEW/VXX/VXX_REVIEW_R2.md
```

Never overwrite a round (`SETUP_ISSUES.md` I-002).
