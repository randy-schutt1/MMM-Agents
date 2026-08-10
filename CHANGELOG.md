# CHANGELOG

Notable structural and methodological changes to the MMM-MASTERY project.

This file records **project-level** changes — architecture, protocols, standards,
phase transitions. Day-to-day study work belongs in `LOG.md`; review decisions
belong in `18_REVIEW/`.

Format is loosely based on [Keep a Changelog](https://keepachangelog.com/).
Newest first.

---

## [0.5.0] — 2026-08-10 — V02 reviewed: REVISE; V03 gate holds

### Added

- `18_REVIEW/V02/V02_REVIEW_R1.md` — first independent review of V02. **`REVISE`**,
  confidence HIGH, 0 critical, 1 major, 5 minor, 6 notes. Produced by a session that
  wrote none of V02's artifacts, so `D-003` is satisfied for the first time since
  V01 R2.

### Changed

- **V02: `AWAITING REVIEW` → `IN REMEDIATION`.** Ten required corrections.
- **`E06` (false positive) enters the error register**, and it is a new *class* for this
  project. Every prior defect concerned citing sources; this one concerns **reading
  price**. The V02 homework's chart markup states days and levels its own committed PNG
  does not show, and concludes from them that a real week confirms the "at least 3 days"
  doctrine — the exact quantity `C-001` has open. Measured from the image: Monday's high
  is 0.81150 not ~0.8130, and the reversal the markup places on Friday is Thursday's
  move, with Friday running the opposite way. **Protocol implication:** chart-derived
  claims need the same verifiability standard as transcript-derived ones — a markup keyed
  to dates and prices should be reproducible from the image by someone who was not there.
- **`E20` rises to 13, four open.** `CONTRADICTIONS.md`'s STATUS block is wrong for the
  **fourth** time, and this time the error was introduced by the R3 edit that was
  correcting that same block. Recommend the 25% review promote the session-close re-read
  to a requirement *and* consider a mechanical check in `validate_project.py` — every one
  of these failures is arithmetic over the file's own contents.
- **`E11` did not recur.** V01's dominant defect across three rounds; ~20 V02 citations
  sampled, all resolved to markers carrying their words.
- `REVIEW_INDEX.md` open items: **10 added** (C-001's only empirical datum was misread —
  record what the corrected week actually shows, including "nothing"); **11 added and
  closed** (the `A-006`/`A-003` spot-check R3 requested — both pass, verified against the
  frames).
- `COURSE_PROGRESS.md`: `V03 GATE` note strengthened. V02 is `REVISE`, not `PASS`, so the
  gate is live. Open item 9 records that the last one did not hold; this is the test.

### Upheld

- The V02 homework's **data substitution** (a 2026 week for the paywalled 2012 week) —
  honestly handled, evidenced, and better than deferring outright.
- **11b's `DEFERRED`** — verified independently that M/W anatomy is undefined across both
  lessons. Producing forty flashcards would require inventing it.
- **Q-002's quarantine** — verified complete at the filesystem level.
- **The wrong-file capture is contained** — nothing derived from it survives into the notes.

### Notes

- No student artifact was edited by the reviewer session. Findings 2–9 are remediation
  work for a separate session, per `D-003` and the R3 precedent.
- The 40× / 10× figures in `D-021`, `SWF_CAPTURE_RECIPE.md` §10 and
  `04_SCREENSHOTS/V02/INDEX.md` are **not** in conflict: 40× is the measured capability,
  10× the chosen operating point. Recorded because the two appear together often enough
  to read as a contradiction.

---

## [0.4.0] — 2026-08-10 — V01 PASSED at R3; V02 gate opens

### Changed

- **V01: `IN REMEDIATION` → `COMPLETE`.** `18_REVIEW/V01/V01_REVIEW_R3.md` returns
  **`PASS`** (HIGH, 0 critical, 0 major). All 15 required actions from R2 applied and
  verified against the source. The first lesson in the corpus to pass.
- **`D-004` gate: V02 opens; V03 does not.** `COURSE_PROGRESS.md` gains an explicit
  `V03 GATE: CLOSED` line. Logged with it: the V02 student pass ran while the V02 gate
  still read `CLOSED` (`REVIEW_INDEX.md` open item 9).
- `A-006`'s trailing "one candidate reading ELIMINATED" block **withdrawn in place** —
  header changed, original text retained and marked `DO NOT CITE`, refutation recorded
  beside it. This supersedes two statements in `[0.3.0]` below: *"`A-006` had one of its
  two competing readings eliminated"* and *"eliminated one of two competing readings"*.
  **Both are false.** The `[0.3.0]` entry is left unedited as the historical record;
  this line is the correction.
- `A-003` promoted from a record that contradicted itself in five fields to one that
  states its resolution consistently throughout.
- The stale *"no screenshot exists for V01"* assertion cleared from all 16 remaining
  ambiguity records — three with fresh visual determinations (`A-002`, `A-008`, `A-016`,
  all *materially constrained*, all still `DO NOT CODE`), three with slide-text evidence,
  one with an explicit "frame exists, defines nothing" note.
- **Eleven citations corrected across three review rounds.** Every quotation in the V01
  corpus now resolves to a transcript marker carrying its words.
- `SETUP_ISSUES.md` `I-006` now points to `D-021` (frame-rate speedup works at 40×)
  rather than describing it as untested.

### Notes

- **This round was remediation and review in one session**, contrary to `D-003`, at the
  project owner's direction. Disclosed at the head of `V01_REVIEW_R3.md`. Every
  determination was verified against the primary source, and three of R2's own claims
  were corrected in the process — but no independent session audited this round, and the
  V02 reviewer is asked to spot-check `A-006` and `A-003`.
- **Six timestamp approximations were deliberately left uncorrected.** They resolve to the
  right passage; fixing them is the `STUDY_PROTOCOL.md` amendment deferred to the 25%
  review, and applying an unadopted rule retroactively was judged the worse error.
- `C-001` (the day-count contradiction) travels forward `UNRESOLVED`. **V02 did not
  resolve it**, which matters — C-001 named "a later lesson refines it" as its most likely
  route out.

---

## [0.3.0] — 2026-08-10 — V01 screenshots; capture problem solved; V01 submitted for review

### Added

- **`00_SYSTEM/SWF_CAPTURE_RECIPE.md`** — reusable, fresh-session recipe for processing
  one lesson video end to end: Ruffle WASM in headless Chrome via Playwright, offset
  calibration, mux, sync verification, screen-state detection, curation, and the study
  order. Includes the routes already ruled out and three specific gotchas that each cost
  a debugging cycle.
- **22 screenshots** in `04_SCREENSHOTS/V01/`, indexed, each carrying the player's
  burned-in timecode so it proves its own timestamp.
- **`07_MASTERY_REPORTS/V01_MASTERY_REPORT.md`** — status `REVIEW REQUIRED`.
- **`D-018`** — dimensions F and G may be `NOT APPLICABLE` where a lesson supplies
  nothing to satisfy them. Sets the standard for all 21 lessons.
- **`A-018`** — the `R = <number>` box labels, logged rather than guessed.
- `V01_INTERPRETATION.md` **§10** — what the visuals changed, appended without editing
  §§1–9.

### Changed

- **`I-006` (screenshot capture) `OPEN` → `RESOLVED`.** These SWFs contain no video
  stream, so `ffmpeg` can never extract frames; Ruffle's WASM build renders them
  correctly. CloudConvert is no longer needed.
- `A-003` `DO NOT CODE` → **`RESOLVED BY COURSE`** — "pendings", printed on a slide,
  never spoken aloud.
- `A-004`, `A-006`, `A-015`, `A-001`, `A-009`, `A-017` gained visual-evidence updates.
  `A-006` had one of its two competing readings eliminated.
- `V01_SOURCE_NOTES.md` §4 replaced with thirteen real visual observations; the original
  "no screenshot exists" text preserved and marked superseded.
- V01 processing status → `STUDENT COMPLETE`; `COURSE_PROGRESS.md` → `AWAITING REVIEW`.

### Notes

- **Interpretation was written from the transcript alone, before any screenshot
  existed, and was not rewritten afterwards.** The visuals corrected one
  over-generalisation, resolved one word the record had refused to guess, eliminated one
  of two competing readings, and left `I7` open. Keeping the two passes separate is what
  makes that visible.
- **GBP/USD appears on screen at `[00:50:55]` and is never spoken aloud** — the project's
  designated primary research instrument, with the weekly cycle annotated.
- V01 still yields **no executable rule**: no stop, target, risk-to-reward, position size
  or indicator parameter. Better evidence did not make it a mechanics lesson.
- The review is **not** in this release. `18_REVIEW/V01/V01_REVIEW_R1.md` must be written
  by a separate session; the student cannot audit itself.

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
