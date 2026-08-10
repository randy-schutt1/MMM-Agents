# COURSE PROGRESS

Single source of truth for where the course stands.

Updated after every meaningful milestone by both Student and Reviewer sessions.

---

## SUMMARY

```text
PHASE:               1 — STUDENT  (blocked, awaiting source videos)
VIDEOS INGESTED:     0
VIDEOS IN PROGRESS:  0
VIDEOS PASSED:       0
CURRENT LESSON:      none — ingestion not yet run
NEXT ACTION:         run 00_SYSTEM/SOURCE_INGESTION_PROTOCOL.md
```

---

## EXPECTED COURSE LENGTH — UNVERIFIED

The project owner expects **approximately 21 usable lesson videos**, in a folder
that may hold **around 24 files**.

**This is not a verified fact and must not be treated as one.** The table below is
deliberately empty rather than pre-filled with 21 or 24 placeholder rows. Rows are
added only for videos that have been verified to exist during ingestion, in their
verified order. If the real count turns out to be 18 or 26, the table simply gets
that many rows.

---

## PROGRESS TABLE

| Video | Source Verified | Transcript | Notes | Screenshots | Homework | Manual Backtest | Student Mastery | Reviewer | Final Status |
|---|---|---|---|---|---|---|---|---|---|
| _(no videos ingested)_ | | | | | | | | | |

### Row template — copy for each verified lesson

```text
| V01 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
```

---

## LEGEND

### Artifact columns

| Symbol | Meaning |
|---|---|
| ⬜ | Not started |
| ⏳ | In progress |
| ✅ | Complete |
| — | Not applicable to this lesson (e.g. no homework assigned) |
| ⚠️ | Complete but flagged by review — see the review file |

`Source Verified` means the file is inventoried in `SOURCE_MANIFEST.md` with a
SHA-256 and a non-`UNCERTAIN` ordering confidence.

### Student Mastery column

Values from `MASTERY_STANDARD.md` — a **self-assessment**, not an authorization:

```text
PASS | REVIEW REQUIRED | BLOCKED | —
```

### Reviewer column

Values from `REVIEW_PROTOCOL.md` — the **only** column that authorizes
advancement. Include the review round:

```text
PASS (R1) | REVISE (R1) | BLOCKED (R1) | —
```

### Final Status column

```text
NOT STARTED     ← no work begun
IN PROGRESS     ← student is working the lesson
AWAITING REVIEW ← student complete, reviewer session not yet run
IN REMEDIATION  ← reviewer returned REVISE or BLOCKED
COMPLETE        ← reviewer PASS; advancement authorized
```

**A lesson is `COMPLETE` only on reviewer `PASS`.** A student mastery `PASS` moves
the row to `AWAITING REVIEW`, never to `COMPLETE`.

---

## PROGRESSION RULE

```text
Lesson N must be COMPLETE (reviewer PASS)
        before lesson N+1 may be opened.
```

No exceptions. Working ahead while a lesson sits in remediation corrupts the
dependency chain the mastery gate exists to protect.

---

## CUMULATIVE REVIEW CHECKPOINTS

Triggered at roughly 25% / 50% / 75% / 100% of verified lessons. Exact trigger
points are set once the real lesson count is known at ingestion.

| Checkpoint | Trigger (lessons passed) | File | Status |
|---|---|---|---|
| 25% | TBD at ingestion | `18_REVIEW/CUMULATIVE_25.md` | Not started |
| 50% | TBD at ingestion | `18_REVIEW/CUMULATIVE_50.md` | Not started |
| 75% | TBD at ingestion | `18_REVIEW/CUMULATIVE_75.md` | Not started |
| 100% | All lessons passed | `18_REVIEW/FINAL_COURSE_REVIEW.md` | Not started |

---

## PHASE STATUS

| Phase | Name | Status |
|---|---|---|
| 0 | Environment | ✅ Complete |
| 1 | Student | ⛔ Blocked — no source videos |
| 2 | Scholar | Not started |
| 3 | Expert (Master Spec) | Not started |
| 4 | Formalizer (Machine Spec) | Not started |
| 5 | Observer (Pine indicators) | Not started |
| 6 | Evaluator | Not started |
| 7 | Strategist | Not started |
| 8 | Automated Backtester | Not started |
| 9 | Researcher | Not started |
| 10 | Forward Tester | Not started |
| 11 | Risk Engine | Not started |
| 12 | Execution Robot | Not started |

Full phase definitions: `STUDY_PROTOCOL.md` §4.
