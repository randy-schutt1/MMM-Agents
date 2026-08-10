# DECISIONS

Durable project decisions. Append-only.

A decision recorded here binds all future sessions until it is explicitly
superseded by a **new** decision entry. Never edit a decision to change its
meaning; add a superseding entry and mark the old one `SUPERSEDED by D-0XX`.

Fields per decision: ID, date, decision, reason, evidence, alternatives
considered, consequences, status.

Status values: `ACTIVE` / `PROVISIONAL` / `SUPERSEDED` / `RETIRED`.

---

## D-001 — The repository is the persistent project memory

**Date:** 2026-08-10
**Decision:** The Git repository — not any chat session — is the authoritative
state of this project. Chat sessions are disposable.
**Reason:** Agent sessions have no durable memory and will be run by different
models at different times over a long project. Any knowledge that exists only in a
conversation is lost.
**Evidence:** Student governing file §33 (session resume) and §34 (session close);
Reviewer governing file §34–35.
**Alternatives considered:** Relying on long-running sessions or conversational
continuity — rejected as fragile and unauditable.
**Consequences:** Every meaningful session must append to `LOG.md` and update
`COURSE_PROGRESS.md`. Agents must read repository state before acting and must not
rely on conversational memory when the repository provides stronger evidence.
**Status:** ACTIVE

---

## D-002 — One lesson per Student session

**Date:** 2026-08-10
**Decision:** A Student session processes exactly one lesson, then stops.
**Reason:** Batching lessons defeats the mastery gate, dilutes attention, and makes
it impossible to attribute a defect to a specific lesson's work.
**Evidence:** Student governing file §1.11 ("Do not progress to the next lesson
until the current lesson passes the mastery standard").
**Alternatives considered:** Processing several lessons then reviewing in bulk —
rejected; errors compound across lessons before detection.
**Consequences:** More sessions, each smaller and auditable. `LOG.md` gains one
entry per lesson rather than per batch.
**Status:** ACTIVE

---

## D-003 — Review runs in a separate, independent session

**Date:** 2026-08-10
**Decision:** The Independent Reviewer runs in a fresh session that does not carry
the Student session's reasoning, and inspects source evidence before student
conclusions.
**Reason:** A reviewer that has just produced the work cannot independently
evaluate it; it inherits the student's anchoring and confidence.
**Evidence:** Reviewer governing file §2 (independence rule), §4 (required review
order), §36 ("The Student Agent cannot certify itself as final authority").
**Alternatives considered:** Self-review inside the student session — rejected;
this is precisely failure mode 1, "confident misunderstanding".
**Consequences:** Two sessions per lesson minimum. The reviewer must be able to
reconstruct context from the repository alone — which reinforces D-001.
**Status:** ACTIVE

---

## D-004 — Reviewer PASS is the only progression gate

**Date:** 2026-08-10
**Decision:** Lesson N+1 may not be opened until lesson N carries a reviewer `PASS`
recorded in `18_REVIEW/REVIEW_INDEX.md`. A student mastery report of `PASS` is a
submission for review, not an authorization.
**Reason:** Self-certification allows a misunderstanding to propagate into pattern
definitions, Pine Script, backtests, and eventually capital loss.
**Evidence:** Reviewer governing file §1 and §36 (course progression governance).
**Alternatives considered:** Student self-certification with periodic spot-checks —
rejected as insufficient for a system that will eventually trade real money.
**Consequences:** Progress is slower and gated. `COURSE_PROGRESS.md` separates the
student mastery column from the reviewer column for exactly this reason.
**Status:** ACTIVE

---

## D-005 — Manual historical backtesting is part of the Student Phase

**Date:** 2026-08-10
**Decision:** Manual chart study / backtesting is required during Phase 1, as an
educational and validation exercise, distinct from later automated backtesting.
**Reason:** Reading a lesson is not evidence of being able to apply it. Manual
testing is how application is demonstrated before any code exists.
**Evidence:** Student governing file §§17–19; Reviewer governing file §12.
**Alternatives considered:** Deferring all testing to the automated phase —
rejected; coding an unvalidated understanding produces confident, wrong software.
**Consequences:** Each applicable lesson produces per-observation records in
`06_MANUAL_BACKTEST/VXX/`, with future candles hidden at the decision point and
rule application graded separately from trade outcome.
**Status:** ACTIVE

---

## D-006 — Automated backtesting is deferred to Phase 8

**Date:** 2026-08-10
**Decision:** No automated backtesting, Pine Script strategy code, or performance
optimization occurs before the Master Specification (Phase 3) and Machine
Specification (Phase 4) exist.
**Reason:** Automating an unformalized method encodes guesses as rules and then
measures the guesses.
**Evidence:** Student governing file §2 and §27 (phase roadmap); §28–29.
**Alternatives considered:** Prototyping indicators early to "explore" — rejected;
exploratory code becomes de-facto doctrine.
**Consequences:** `14_PINE/`, `15_AUTOMATED_BACKTEST/`, `16_FORWARD_TEST/`, and
`17_EXECUTION_ROBOT/` stay empty of implementation until their phase is reached.
**Status:** ACTIVE

---

## D-007 — GBP/USD is the primary research instrument

**Date:** 2026-08-10
**Decision:** GBP/USD is the main environment for manual chart study, manual
backtesting, examples, formalization, TradingView validation, and automated
testing.
**Reason:** A single consistent instrument makes observations comparable across
lessons and phases.
**Evidence:** Student governing file §37; Reviewer governing file §12.1.
**Alternatives considered:** Multi-pair study from the start — rejected during
learning; it multiplies variables before the method is understood.
**Consequences:** Where the instructor teaches with another instrument, that
example is preserved faithfully as taught. No rule is assumed GBP/USD-specific
unless evidence supports it. Generalization to other pairs is a later research
question.
**Status:** ACTIVE

---

## D-008 — Course evidence outranks agent interpretation

**Date:** 2026-08-10
**Decision:** The evidence hierarchy is: original video/audio → original
screenshots/charts/slides → transcript → instructor homework and solutions →
student source notes → student interpretation → student machine ideas. Lower levels
never override higher levels.
**Reason:** Without a hierarchy, a confidently written interpretation becomes
indistinguishable from instruction, and the corpus drifts.
**Evidence:** Reviewer governing file §2; Student governing file §3.
**Alternatives considered:** Treating well-reasoned interpretation as equivalent to
instruction — rejected; this is failure mode 3, "rule drift".
**Consequences:** Every important rule carries a classification (`EXPLICIT` /
`VISUAL` / `IMPLIED` / `INFERRED` / `UNRESOLVED`) and a citable source. Orphan
rules may not enter the canonical methodology. External frameworks (ICT, SMC,
Wyckoff, Elliott Wave, generic price action) are not imported during the learning
phase.
**Status:** ACTIVE

---

## D-009 — No optimization toward a claimed win rate

**Date:** 2026-08-10
**Decision:** Any advertised accuracy claim (e.g. 90–95%) is recorded with
provenance and treated as a **hypothesis to test**, never as a performance
requirement or a pass/fail criterion.
**Reason:** Optimizing toward an expected number produces a system that reproduces
the marketing claim rather than the market's behaviour.
**Evidence:** Student governing file §23; Reviewer governing file §26.
**Alternatives considered:** Using the claim as a validation target — rejected;
this is failure mode 5, "performance chasing".
**Consequences:** No manipulation of parameters, setup selection, sample windows,
trade exclusions, risk/reward, entry timing, or labelling rules to reach a
percentage. Lessons are never passed or failed based on matching a claimed rate.
The system's real performance is discovered by honest testing.
**Status:** ACTIVE

---

## D-010 — No premature machine rules (machine-rule firewall)

**Date:** 2026-08-10
**Decision:** During the Student Phase, subjective course language is not converted
into numeric constants. Quantification proposals are recorded as
`INFERRED MACHINE CANDIDATE` / `NOT A COURSE RULE`, in interpretation notes and the
ambiguity log.
**Reason:** An arbitrary threshold ("strong = body > 1.5 ATR") invented during
study silently becomes doctrine, then code, then a backtested result that appears
to validate it.
**Evidence:** Reviewer governing file §25 and §24; Student governing file §15 and
§26.
**Alternatives considered:** Provisional constants "just to have something
codable" — rejected; this is failure mode 4, "premature quantification".
**Consequences:** `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` entries carry status
`DO NOT CODE` until Phase 4. The human definition is never overwritten by a machine
approximation; the two live in separate layers (`12_MASTER_SPEC/` vs
`13_MACHINE_SPEC/`).
**Status:** ACTIVE

---

## D-011 — Source videos are excluded from Git

**Date:** 2026-08-10
**Decision:** Bootcamp video files are never committed to normal Git history. They
are represented in Git solely by `SOURCE_MANIFEST.md` rows (filename, size,
duration, SHA-256, relative path).
**Reason:** Multi-gigabyte binaries destroy repository usability, and the material
is proprietary paid course content.
**Evidence:** Student governing file §9 and §10.
**Alternatives considered:** Git LFS — deferred; it remains available but requires
its own explicit decision. Committing directly to Git — rejected outright.
**Consequences:** `.gitignore` excludes `01_SOURCE_VIDEOS/**` and common video/audio
extensions repository-wide. Reproducibility is preserved through checksums rather
than through storing the media. Source files are never modified.
**Status:** ACTIVE

---

## D-012 — Project structure lives at the repository root

**Date:** 2026-08-10
**Decision:** The `00_SYSTEM/` … `18_REVIEW/` structure is created at the root of
the existing `MMM-Agents` repository, not inside a nested `MMM-MASTERY/` directory.
**Reason:** The governing file specifies `MMM-MASTERY/` as the project name but
explicitly permits an equivalent existing organization. This repository already
exists for exactly this project; nesting would create a redundant path segment on
every future file reference.
**Evidence:** Student governing file §4 ("unless the existing repository already
contains an equivalent organization").
**Alternatives considered:** Creating `MMM-MASTERY/` as a subdirectory — rejected
as duplicate nesting.
**Consequences:** All paths in documentation are repository-root-relative. The two
governing `.md` files remain at the root alongside `README.md`.
**Status:** ACTIVE

---

## D-013 — The GitHub repository must remain private

**Date:** 2026-08-10
**Decision:** `randy-schutt1/MMM-Agents` stays private. Verified private at
infrastructure build time.
**Reason:** The repository will contain detailed reconstruction of proprietary paid
course material, including transcripts and instructor screenshots. Public exposure
would redistribute that material.
**Evidence:** Student governing file §8 (commit hygiene, proprietary access data)
and §9 (copyright restrictions on source media).
**Alternatives considered:** Public repository with videos excluded — rejected; the
transcripts and notes are themselves substantially the course content.
**Consequences:** If the repository is ever made public, that is a material event
requiring a superseding decision and a review of what would be exposed. Screenshots
and transcripts are committed on the assumption of privacy.
**Status:** ACTIVE

---

## D-014 — Course length is unverified until ingestion

**Date:** 2026-08-10
**Decision:** No lesson count, lesson order, or lesson title is treated as known
until `SOURCE_INGESTION_PROTOCOL.md` has been run against real files. The owner's
expectation of "~21 usable videos in ~24 files" is recorded as an expectation only.
**Reason:** Pre-creating 21 or 24 placeholder rows would embed a guess into the
progress table and invite an agent to treat it as fact.
**Evidence:** Project owner's stated uncertainty; Student governing file §10
(manifest before processing).
**Alternatives considered:** Pre-populating placeholder lesson rows — rejected;
placeholders become assumptions.
**Consequences:** `COURSE_PROGRESS.md` and `SOURCE_MANIFEST.md` ship empty, with a
row template. Cumulative review trigger points (25/50/75%) are set once the real
count is known. Uncertain lesson ordering must be confirmed by a human before V01
is studied.
**Status:** ACTIVE

---

## D-015 — Commit at frequent checkpoints, not at session end

**Date:** 2026-08-10
**Decision:** Commit and push at checkpoints *during* a session — roughly every
5–10 artifacts, or at any natural boundary — rather than accumulating a session's
entire output into one commit at the end. The number is a guideline, not a rule;
the test is whether a checkpoint represents a coherent, self-contained unit of
work.
**Reason:** Three reasons, in order of importance. (1) An agent session can be
interrupted, run out of context, or fail at any point; uncommitted work is lost
work, and this project's memory *is* the repository. (2) Frequent commits produce a
granular audit trail that shows the order in which understanding was built — which
is exactly what the reviewer and the cumulative reviews need. A single commit of a
whole lesson hides that sequence. (3) Small commits are reviewable; a 78-file
commit is not.
**Evidence:** Project owner instruction, 2026-08-10. Consistent with Student
governing file §8 ("Create focused commits at logical checkpoints. Avoid giant
commits containing unrelated work") and D-001.
**Alternatives considered:** Committing once at session close — rejected; it was
the pattern used for the Phase 0 build and it concentrated all risk at the end.
Committing after every file — rejected as noise that obscures the audit trail
rather than clarifying it.
**Consequences:** `SESSION_CLOSE.md` §6 and `README.md` §13 describe checkpoint
commits. Both session prompts instruct agents to commit as they go. `LOG.md` is
still appended once per session at close — the log entry describes the session,
and its `### Git` section lists all of the session's commits, not just the last.
A checkpoint commit does not require the session's work to be complete, but it must
leave the repository in a coherent state: no half-written file that reads as
finished, and partial artifacts explicitly marked `STATUS: PARTIAL`.
**Status:** ACTIVE

---

## DECISIONS TO BE MADE AT INGESTION

Not yet decided; record as new entries when the information exists.

| Topic | Trigger |
|---|---|
| Source library location and arrangement (in-repo vs external path) | Ingestion |
| Verified lesson count and ordering | Ingestion |
| Handling of any duplicate or non-lesson files found | Ingestion |
| Chart data source / broker feed for manual backtesting | First manual backtest |
| Timezone convention for session and daily boundaries | First timing lesson |
| Default timeframes used in manual study | First chart lesson |
| Development / validation / holdout dataset boundaries | Phase 4–8 |
| Whether Git LFS is adopted for any media | Only if media must be versioned |
