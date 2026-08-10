# CHANGELOG

Notable structural and methodological changes to the MMM-MASTERY project.

This file records **project-level** changes — architecture, protocols, standards,
phase transitions. Day-to-day study work belongs in `LOG.md`; review decisions
belong in `18_REVIEW/`.

Format is loosely based on [Keep a Changelog](https://keepachangelog.com/).
Newest first.

---

## [0.2.0] — 2026-08-10 — Phase 1 opens: source ingested, V01 studied

First release containing actual Market Maker Method content.

### Added

- **Source ingestion complete.** `00_SYSTEM/SOURCE_MANIFEST.md` populated with 42
  SWF files — 21 lesson videos (`V01`–`V21`, 21:52:38 total, all ordering `CERTAIN`)
  and 21 out-of-scope videos from two other series (`X01`–`X21`) — each with SHA-256,
  measured duration, and byte size. Plus four image collections (`X22`–`X26`).
- **`00_SYSTEM/QUARANTINE_REGISTER.md`** — new tracked file recording material that
  must never be used as evidence, with the evidence for that judgement.
- **V01 artifacts:** `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md`,
  `03_LESSON_NOTES/V01_SOURCE_NOTES.md`, `03_LESSON_NOTES/V01_INTERPRETATION.md`,
  `04_SCREENSHOTS/V01/INDEX.md`.
- **First course-level ambiguity and contradiction records:** `A-001`–`A-017` (all
  `DO NOT CODE`), `C-001` (foundational, unresolved), `C-002`.
- **`D-017`** — source arrangement, lesson order, duplicate handling, quarantine.
- **`I-008`** — 20 of 21 transcripts are unverified.

### Changed

- `COURSE_PROGRESS.md` expanded from zero rows to 21 verified lesson rows.
- Lesson folders under `Bootcamp Notes/` renumbered from alphabetical to
  chronological order (19 of 21 folders changed). Any external reference to the old
  numbering is now wrong. Source `.swf` files were not renamed.
- `I-006` (screenshot capture) updated with an investigated root cause: these SWFs
  contain no video stream, only a composited bitmap display list, so frame extraction
  requires a Flash renderer rather than `ffmpeg`.

### Removed

- 63 fabricated per-lesson notes files, an 8-file synthesized master rulebook, and a
  synthesized course-notes document — moved to a clearly-marked quarantine folder
  under the Git-ignored source tree, not deleted. See `QUARANTINE_REGISTER.md` Q-001.
- Stray housekeeping files from `01_SOURCE_VIDEOS/`: a 61 MB test-conversion `.mp4`,
  a 392-file temporary jpeg folder, 14 `.DS_Store` files.

### Notes

- **Week 6 is genuinely missing** from the source material and is documented as
  expected-missing. No session may fabricate or interpolate it.
- V01 was studied **without screenshots**. Roughly its last 21 minutes is narration
  over slides that could not be extracted, so about half the lesson's content was not
  recovered. No V01 interpretation is classified `VISUAL`. Every affected artifact
  states this.
- V01 yields no executable rule: no stop, no target, no risk-to-reward, no position
  size, and no indicator parameter is stated anywhere in the lesson.

---

## [0.1.1] — 2026-08-10 — Checkpoint commit cadence; audit fixes

### Changed

- Adopted D-015: commit and push at checkpoints during a session (roughly every
  5–10 artifacts, or at any natural boundary), rather than accumulating a whole
  session into one end-of-session commit. Propagated to `SESSION_CLOSE.md`,
  `README.md` §13, and both session prompts.

### Fixed (from infrastructure self-audit)

- Appended the missing `LOG.md` entry for the D-015 session — the change had been
  committed without a log entry, which the audit flagged as a session-close
  protocol violation.
- Added a clarifying comment to the `*.ts` pattern in `.gitignore` (MPEG transport
  stream, not TypeScript).

### Audit notes

- Verified all 38 required setup files present and non-empty; all D/I
  cross-references resolve; `COURSE_PROGRESS.md` columns match specification;
  README section references correct.
- Negative-tested `scripts/validate_project.py` — it fails correctly when a
  required file is removed, so its green result is not vacuous.
- Re-confirmed zero Market Maker Method content anywhere in the repository.

---

## [0.1.0] — 2026-08-10 — Phase 0: Infrastructure

### Added

- Governing files established as the project source of truth:
  - `MMM_MASTER_STUDENT_RESEARCH_AGENT.md`
  - `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md`
- Full directory structure `00_SYSTEM/` through `18_REVIEW/`, plus `scripts/`,
  created at the repository root.
- Root documents: `README.md`, `LOG.md`, `CHANGELOG.md`, `.gitignore`.
- `00_SYSTEM/` operating documents:
  - `AGENT_ROLE.md` — student and reviewer roles and boundaries
  - `STUDY_PROTOCOL.md` — per-lesson workflow and full phase roadmap
  - `MASTERY_STANDARD.md` — student self-assessment standard (A–J)
  - `REVIEW_PROTOCOL.md` — durable independent review methodology
  - `REMEDIATION_PROTOCOL.md` — PASS / REVISE / BLOCKED loop
  - `SOURCE_INGESTION_PROTOCOL.md` — video inventory and checksum procedure
  - `FILE_NAMING_STANDARD.md` — naming conventions and ID schemes
  - `COURSE_PROGRESS.md` — per-lesson progress table (no lessons yet)
  - `DECISIONS.md` — D-001 … D-014
  - `SOURCE_MANIFEST.md` — empty; zero videos ingested
  - `SESSION_START.md`, `SESSION_CLOSE.md` — session checklists
  - `SETUP_ISSUES.md` — I-001 … I-004, governing-file inconsistencies
  - `STUDENT_SESSION_PROMPT.md`, `REVIEWER_SESSION_PROMPT.md`
- Eleven reusable templates in `00_SYSTEM/TEMPLATES/`.
- Review infrastructure: `18_REVIEW/REVIEW_INDEX.md` and empty cumulative review
  templates (`CUMULATIVE_25/50/75`, `FINAL_COURSE_REVIEW`).
- Empty, clearly-labelled logs: `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`,
  `11_CONTRADICTIONS/CONTRADICTIONS.md`, `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`.
- `scripts/validate_project.py` — structural health check (no methodology
  judgement).
- A `README.md` contract in each numbered directory.

### Notes

- **No Market Maker Method content exists in this release.** No transcripts, notes,
  rules, concepts, screenshots, homework, backtests, or specifications were
  produced. The bootcamp source videos were not accessible to the session that
  built this infrastructure.
- Project status: `INFRASTRUCTURE READY / SOURCE VIDEOS NOT YET AVAILABLE`.
- Structure was built at the repository root rather than inside a nested
  `MMM-MASTERY/` directory, to avoid duplicate project nesting (see D-012).

---
