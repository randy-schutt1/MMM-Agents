# SETUP ISSUES

Inconsistencies, gaps, and open questions in the **project infrastructure** —
including places where the two governing files disagree.

This file is about the operating system of the project, not about the Market Maker
Method. Contradictions found *in the course* belong in
`11_CONTRADICTIONS/CONTRADICTIONS.md`.

Per the build instruction: where the governing files conflict, the conflict is
documented here rather than silently resolved. Provisional handling is applied so
work can proceed, and is marked as provisional.

Status values: `OPEN` / `PROVISIONALLY HANDLED` / `RESOLVED` / `ACCEPTED AS-IS`.

---

## I-001 — Two different status vocabularies for the same gate

**Status:** `PROVISIONALLY HANDLED` — human confirmation requested

**Conflict**

| Source | Vocabulary |
|---|---|
| Student file §21 (mastery report) | `PASS` / `REVIEW REQUIRED` / `BLOCKED` |
| Reviewer file §1 (review decision) | `PASS` / `REVISE` / `BLOCKED` |

The middle value differs, and both files say `PASS` gates progression:

- Student §21: *"Only `PASS` permits progression to the next lesson."*
- Reviewer §36: *"The Student Agent cannot certify itself as final authority.
  Reviewer `PASS` is the gate."*

Read literally, a student `PASS` both does and does not authorize advancement.

**Provisional handling**

The two vocabularies belong to two different actors and are kept distinct:

- The **student's** `PASS / REVIEW REQUIRED / BLOCKED` is a **self-assessment and a
  submission for review**. It never advances the course on its own.
- The **reviewer's** `PASS / REVISE / BLOCKED` is the **only** authorization.

`COURSE_PROGRESS.md` therefore carries two separate columns (`Student Mastery`,
`Reviewer`), and a lesson becomes `COMPLETE` only on reviewer `PASS`. This reading
satisfies Reviewer §36, which is the more specific statement about authority.

**Why this was not silently merged:** collapsing the vocabularies would either
delete the student's self-assessment step or imply the student can self-certify.
Both alter the governing design.

**Human confirmation requested:** confirm the two-vocabulary reading, or instruct
that both actors use a single shared vocabulary.

---

## I-002 — Review report filename is specified two ways

**Status:** `PROVISIONALLY HANDLED`

**Conflict**

| Source | Path |
|---|---|
| Reviewer file §7 | `18_REVIEW/VXX/VXX_REVIEW.md` |
| Reviewer file §31 | `V04_REVIEW_R1.md`, `V04_REVIEW_R2.md`, `V04_REVIEW_R3.md` |

§31 also says *"`V04_REVIEW.md` may contain or point to the latest accepted review
if desired"* — permissive, not directive — while insisting *"Never overwrite an
earlier review."*

**Provisional handling**

Versioned files are canonical: `18_REVIEW/VXX/VXX_REVIEW_R<n>.md`, one per round,
never overwritten. An optional `VXX_REVIEW.md` pointer file may be added but must
never replace the versioned files. This satisfies the non-negotiable requirement
(never overwrite) while remaining compatible with §7's directory layout.

**Impact:** low. `TEMPLATES/REVIEW_TEMPLATE.md` and `REVIEW_PROTOCOL.md` §11 use
the versioned form.

---

## I-003 — The two files specify different `00_SYSTEM/` contents

**Status:** `PROVISIONALLY HANDLED`

**Conflict**

| File | Present in Student §4 | Present in Reviewer §5 |
|---|---|---|
| `AGENT_ROLE.md` | ✅ | ✅ |
| `STUDY_PROTOCOL.md` | ✅ | ✅ |
| `MASTERY_STANDARD.md` | ✅ | ✅ |
| `COURSE_PROGRESS.md` | ✅ | ✅ |
| `DECISIONS.md` | ✅ | ✅ |
| `FILE_NAMING_STANDARD.md` | ✅ | ❌ |
| `SOURCE_MANIFEST.md` | ❌ (specified in §10 instead) | ✅ |
| `REVIEW_PROTOCOL.md` | ❌ | ✅ |

The Student file's tree also omits `18_REVIEW/`; the Reviewer file's tree omits
`.gitignore` and `CHANGELOG.md`.

**Provisional handling**

The **union** of both trees is created. Neither file forbids the other's
directories, and each omission is plainly a matter of scope (the Student file
describes the student's world, the Reviewer file the reviewer's). The Student
file's §10 explicitly requires `00_SYSTEM/SOURCE_MANIFEST.md` in prose even though
its tree omits it, which supports reading the trees as partial rather than
exclusive.

**Impact:** none. No content is lost by taking the union.

---

## I-004 — "Do not progress" is stated at two different gates

**Status:** `PROVISIONALLY HANDLED` — related to I-001

**Conflict**

Student §1.11 says do not progress until the lesson *"passes the mastery
standard"* (a student-side test). Reviewer §36 says the reviewer's `PASS` is the
gate. A student session reading only its own governing file could conclude it may
advance immediately after writing a `PASS` mastery report.

**Provisional handling**

Both conditions must hold, in order: the lesson must pass the student mastery
standard **and then** receive a reviewer `PASS`. The student mastery standard is a
precondition for *requesting review*, not for advancing.

`STUDENT_SESSION_PROMPT.md` makes this explicit as a hard stop, so a student
session cannot reach the wrong conclusion from its governing file alone.

---

## I-005 — Source videos are not yet available

**Status:** `OPEN` — blocking Phase 1

Not a governing-file conflict; recorded here because it blocks the project.

The infrastructure build session had no access to the bootcamp video library.
Consequently: `SOURCE_MANIFEST.md` has zero rows, `COURSE_PROGRESS.md` has zero
lesson rows, and no course content exists anywhere in the repository.

**Resolution requires:** the project owner making the video library locally
accessible to an agent session, then a Student session running
`SOURCE_INGESTION_PROTOCOL.md`.

**Expected but unverified:** ~21 usable lesson videos in a folder of ~24 files.
Recorded as an expectation only (see `DECISIONS.md` D-014).

---

## I-006 — Screenshot capture may require human assistance

**Status:** `OPEN` — to be resolved at first lesson

Both governing files treat screenshots as first-class evidence, and the reviewer
audits chart recognition against them. Whether an agent session can capture frames
from the source videos depends on the tooling available in the environment
(e.g. `ffmpeg` for frame extraction) — this is unknown until the videos and the
runtime are both present.

**If frame extraction is unavailable**, the options are: the project owner captures
screenshots manually at agent-specified timestamps, or the agent works from
detailed timestamped visual descriptions and records the limitation in every
affected artifact. The second option materially weakens the evidence base and must
be flagged to the reviewer, not hidden.

**Do not** substitute generated, illustrative, or reconstructed images for real
course screenshots under any circumstances.

---

## I-007 — Manual backtesting requires a chart data source

**Status:** `OPEN` — to be resolved before the first manual backtest

Manual backtesting on GBP/USD requires historical chart access with the ability to
hide future candles at the decision point (e.g. TradingView bar replay). Whether an
agent session can drive such a tool, or whether the project owner performs the
chart-walking with the agent directing and recording, is undetermined.

This affects the credibility of every manual backtest record, so it must be decided
and recorded in `DECISIONS.md` — including the data source, broker/feed, timezone,
and timeframes — before observations are collected. See `STUDY_PROTOCOL.md` §6
(reproducibility).

---

## HOW TO USE THIS FILE

- A **new session** should read this file during session start. An `OPEN` issue may
  block or reshape the planned work.
- A **reviewer** should check whether a lesson's work depends on an unresolved
  setup issue before issuing `PASS`.
- **Resolving an issue** means appending the resolution and changing the status —
  not deleting the entry. The history of how the project's rules were settled is
  part of the audit trail.
- New infrastructure conflicts get the next `I-0XX` number.
