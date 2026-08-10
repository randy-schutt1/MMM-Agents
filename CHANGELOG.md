# CHANGELOG

Notable structural and methodological changes to the MMM-MASTERY project.

This file records **project-level** changes — architecture, protocols, standards,
phase transitions. Day-to-day study work belongs in `LOG.md`; review decisions
belong in `18_REVIEW/`.

Format is loosely based on [Keep a Changelog](https://keepachangelog.com/).
Newest first.

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
