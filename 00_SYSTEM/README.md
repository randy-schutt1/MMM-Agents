# 00_SYSTEM

The project's operating system: protocols, standards, prompts, and templates.

Everything here is **derived from** the two governing files at the repository root.
Where this directory and a governing file disagree, the governing file wins —
record the disagreement in `SETUP_ISSUES.md`.

**No file in this directory contains Market Maker Method trading content taken from the
course.** These are process documents.

> **One exception, and it is an exception to the wording only, not to the rule.**
> `EXTERNAL_VOCABULARY_REFERENCE.md` (added 2026-08-13) contains trading vocabulary — all of it
> **third-party and internet-sourced, none of it from any lesson in this library.** It is
> non-normative reference material for a human reader, it changes no project state, and it is
> never cited as evidence. Read its banner before using it.

## FILES

| File | Purpose |
|---|---|
| `AGENT_ROLE.md` | Student and Reviewer roles, boundaries, shared prohibitions |
| `STUDY_PROTOCOL.md` | Per-lesson workflow; manual backtest protocol; phase roadmap |
| `MASTERY_STANDARD.md` | Student self-assessment standard (dimensions A–J) |
| `REVIEW_PROTOCOL.md` | Independent review methodology, error taxonomy, severity |
| `REMEDIATION_PROTOCOL.md` | The PASS / REVISE / BLOCKED loop; redo-don't-reword rule |
| `SOURCE_INGESTION_PROTOCOL.md` | Video inventory, checksums, lesson ordering |
| `FILE_NAMING_STANDARD.md` | Naming conventions and ID schemes |
| `COURSE_PROGRESS.md` | Per-lesson progress table — the current-state file |
| `DECISIONS.md` | Durable project decisions, D-001 … |
| `SOURCE_MANIFEST.md` | Video inventory with SHA-256 checksums |
| `SESSION_START.md` | Boot checklist for every session |
| `SESSION_CLOSE.md` | Shutdown checklist for every session |
| `SETUP_ISSUES.md` | Infrastructure conflicts and open blockers, I-001 … |
| `STUDENT_SESSION_PROMPT.md` | Copy-paste prompt to start a Student session |
| `REVIEWER_SESSION_PROMPT.md` | Copy-paste prompt to start a Reviewer session |
| `EXTERNAL_VOCABULARY_REFERENCE.md` | ⛔ **NOT COURSE MATERIAL.** Third-party, internet-sourced candidate definitions for terms the corpus names and never defines. Non-normative, permanently. Closes no record, unblocks no test, never cited as a source |
| `EXTERNAL_REFERENCE/` | ⛔ **NOT COURSE MATERIAL.** Outside-the-corpus documents held for reference only — currently the anonymous Mauro seminar-notes PDF. Never cited as evidence; read its `README.md` first |
| `TEMPLATES/` | Eleven reusable artifact templates |

## READING ORDER FOR A NEW AGENT

1. Your governing file (Student or Reviewer)
2. `../README.md`
3. `SESSION_START.md` — then follow it

## THE FILES THAT CHANGE

`COURSE_PROGRESS.md` (every session), `DECISIONS.md` and `SETUP_ISSUES.md`
(append-only), `SOURCE_MANIFEST.md` (at ingestion).

The protocols and standards change rarely — when they do, record it in
`CHANGELOG.md`, and if the change alters what evidence is required, add a decision.
