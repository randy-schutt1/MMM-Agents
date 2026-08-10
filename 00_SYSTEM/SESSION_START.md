# SESSION START PROTOCOL

Run this at the beginning of **every** agent session, student or reviewer, before
doing any work.

Source: `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` §33;
`MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md` §34.

---

## 1. THE PRINCIPLE

> **Do not rely on conversational memory when repository state provides stronger
> evidence.**

You may be a different model, on a different day, with no knowledge of what came
before. The repository is the memory. Read it before acting.

---

## 2. READ, IN ORDER

| # | File | What you are looking for |
|---|---|---|
| 1 | Your governing file | Student → `MMM_MASTER_STUDENT_RESEARCH_AGENT.md`; Reviewer → `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md` |
| 2 | `README.md` | Current phase, current status, standing prohibitions |
| 3 | `LOG.md` (tail) | What the last session actually did and its stated next action |
| 4 | `00_SYSTEM/COURSE_PROGRESS.md` | Which lesson is current and what state it is in |
| 5 | `00_SYSTEM/DECISIONS.md` | Binding decisions you must not contradict |
| 6 | `18_REVIEW/REVIEW_INDEX.md` | Which lessons hold a reviewer `PASS`; recurring errors |
| 7 | `00_SYSTEM/SETUP_ISSUES.md` | Open issues that may block or reshape the work |

A reviewer session additionally reads `00_SYSTEM/REVIEW_PROTOCOL.md`; a student
session additionally reads `00_SYSTEM/STUDY_PROTOCOL.md`.

---

## 3. CHECK REPOSITORY STATE

```bash
git status
git log --oneline -10
git branch --show-current
python3 scripts/validate_project.py
```

Expected: a clean tree on the working branch, and a passing validation.

If the tree is dirty, the previous session did not close properly. Inspect the
uncommitted changes and reconcile them against the last `LOG.md` entry **before**
starting new work — do not simply commit or discard them.

If validation fails, fix the structural problem first.

---

## 4. IDENTIFY THE CURRENT LESSON AND STATE

From `COURSE_PROGRESS.md`, find the first row that is not `COMPLETE`:

| Final Status | What this session should do |
|---|---|
| _(no rows at all)_ | Source not ingested. Run `SOURCE_INGESTION_PROTOCOL.md` — if the videos are actually available. If not, stop and report the blocker. |
| `NOT STARTED` | Student session: begin this lesson at `STUDY_PROTOCOL.md` Step 1. |
| `IN PROGRESS` | Student session: resume from the first missing artifact. Do not restart completed work. |
| `AWAITING REVIEW` | **Reviewer** session. A student session must not proceed to the next lesson. |
| `IN REMEDIATION` | Student session: work the required corrections from the latest review file, per `REMEDIATION_PROTOCOL.md`. |
| `COMPLETE` | Move to the next row. If all rows are `COMPLETE`, the Student Phase may be finished — check the exit criteria in `STUDY_PROTOCOL.md` §5. |

---

## 5. VERIFY YOU ARE THE RIGHT AGENT

| Situation | Correct session |
|---|---|
| Lesson needs studying / remediation | Student |
| Lesson is `AWAITING REVIEW` | Reviewer |
| Lesson has reviewer `PASS`, next lesson not started | Student |

**Do not run both roles in one session.** Independence is the point of the design
(`DECISIONS.md` D-003). If you find yourself about to review work you produced in
this same session, stop and hand off.

---

## 6. CONFIRM THE GATE BEFORE STUDYING A NEW LESSON

Before opening lesson N, confirm in `18_REVIEW/REVIEW_INDEX.md` that lesson N−1
carries a reviewer `PASS`.

A student mastery report of `PASS` is **not** sufficient. See `DECISIONS.md` D-004
and `SETUP_ISSUES.md` I-001/I-004.

---

## 7. STATE YOUR PLAN BEFORE ACTING

Before producing artifacts, state briefly:

1. Which lesson and which state it is in.
2. Which role you are running as.
3. What artifacts this session will produce.
4. Any open setup issue that affects the work.
5. Where you will stop.

If the repository's state contradicts what the user's message implied, say so
before proceeding — the repository is the stronger evidence, but the discrepancy is
worth surfacing.

---

## 8. IF THE PROJECT IS BLOCKED

The current blocker is `SETUP_ISSUES.md` I-005 — no source videos.

If a blocker prevents the planned work, **do not substitute plausible-looking
output for the missing input.** Do not write transcripts from general knowledge,
invent lesson content, fabricate screenshots, or produce backtest observations
without charts. Report the blocker, record it in `LOG.md`, and stop.
