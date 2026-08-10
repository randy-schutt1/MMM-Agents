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

## D-016 — Governing-file conflicts I-001 … I-004 resolved as read

**Date:** 2026-08-10
**Decision:** The provisional handling recorded for setup issues I-001, I-002,
I-003, and I-004 is confirmed by the project owner and is now binding. Those four
readings are no longer provisional and are not to be relitigated by a future
session:

| Issue | Confirmed resolution |
|---|---|
| I-001 | Student and Reviewer keep **separate status vocabularies**. Student: `PASS` / `REVIEW REQUIRED` / `BLOCKED` (self-assessment, a submission). Reviewer: `PASS` / `REVISE` / `BLOCKED` (sole authorization). Never merged; separate columns in `COURSE_PROGRESS.md`. |
| I-002 | Versioned review files `18_REVIEW/VXX/VXX_REVIEW_R<n>.md` are canonical and never overwritten. An optional `VXX_REVIEW.md` pointer is permitted but never replaces them. |
| I-003 | The two governing files' directory trees are **partial views of one structure**; the union stands. A file absent from one tree is not thereby forbidden. |
| I-004 | Both gates apply in order: the mastery standard authorizes *requesting review*; only a reviewer `PASS` authorizes *advancing*. |

**Reason:** These four conflicts sit at the foundation of the progression gate and
the review audit trail. Leaving them provisional would mean every future session
re-derives them from two files that genuinely disagree — and could derive them
differently. A confirmed decision makes the reading stable across sessions and
models, which is the point of D-001.
**Evidence:** Project owner confirmation, 2026-08-10, in response to the Phase 0
infrastructure report. Underlying analysis in `SETUP_ISSUES.md` I-001 … I-004.
**Alternatives considered:** Merging the two vocabularies into one shared set —
rejected; it would either delete the student's self-assessment step or imply the
student can self-certify, and both alter the governing design. Deferring
confirmation until the first lesson — rejected; the gate must be unambiguous
*before* any lesson is studied, not after.
**Consequences:** No implementation change was required; the infrastructure already
reflected all four readings. `SETUP_ISSUES.md` I-001 … I-004 move from
`PROVISIONALLY HANDLED` to `RESOLVED`, with resolution notes appended rather than
replacing the original analysis. The remaining open setup issues are I-005 (no
source videos — blocking), I-006 (screenshot capture tooling), and I-007 (chart
data source for manual backtesting).
**Status:** ACTIVE

---

## D-017 — Source library arrangement, lesson order, duplicate handling, and quarantine of pre-ingestion notes

**Date:** 2026-08-10
**Decision:** Four ingestion-time decisions, taken together because they were
established by a single pass over the library.

1. **Arrangement — in-repo, Git-ignored.** The library stays at
   `01_SOURCE_VIDEOS/Forex Bootcamp/`, excluded by `.gitignore`.
   `SOURCE_MANIFEST.md` is its Git-visible representation.
2. **Lesson order — 21 lessons, all `CERTAIN`, ordered by session date.** The on-disk
   folder numbering was an alphabetical artifact (`Wk1, Wk10, Wk2, …`) that placed
   Week 10 third and shifted everything from position 03 on. Order was re-derived
   from the `MMDDYY` date in each filename and cross-checked against the instructor's
   week labels; the two agree completely. Folders under `Bootcamp Notes/` were
   renumbered so folder `NN` = video `VNN`. **Source `.swf` files were not renamed.**
3. **Duplicates — the flat `Bootcamp/` copy is canonical.** All 21 lesson videos exist
   twice, byte-identical (confirmed by matching SHA-256): once flat in `Bootcamp/`,
   once inside the corresponding `Bootcamp Notes/NN_.../` folder. The manifest records
   the flat path. Duplicates get no `X` IDs. The 21 additional SWFs (3 Dean Malone, 18
   `SteveMauro060212`) are inventoried as `X01`–`X21`, `NOT A LESSON`, out of scope.
4. **Pre-ingestion derived notes — quarantined, not deleted.** 72 files moved to
   `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/`.

**Reason:** (1)–(3) are required by `SOURCE_INGESTION_PROTOCOL.md` Steps 1, 7 and 8
and had to be settled before V01 could be studied. (4) is the consequential one: the
existing `NOTES.md` / `RULES.md` / `VISUAL_INDEX.md` and the `00_MASTER/` rulebook
carry timestamps and `Source: Explicit` labels but are not traceable to the audio.
`RULES.md` for V01 cites *"Wait for the M15 candle to close before taking the 5/13 EMA
cross"* at `[00:05:00]`; `[00:05:00]` is the instructor complaining about last-minute
homework, and the token `EMA` appears in the whole 54-minute transcript exactly once
outside the word *email* — as survey question 10. `VISUAL_INDEX.md` describes 78
screenshots where one image exists. Feeding any of it to a Student session would
inject fabricated rules that look fully sourced.
**Evidence:** `00_SYSTEM/QUARANTINE_REGISTER.md` Q-001; `SOURCE_MANIFEST.md`
anomalies A-01 … A-08.
**Alternatives considered:** *Deleting the fabricated files* — rejected; deletion
destroys the record of what was discarded and why, and a future session would
re-derive the same material and possibly trust it. *Keeping them in place with a
warning header* — rejected; a warning at the top of a file does not survive being
read in fragments by a future agent, and proximity to the real transcript is itself
the hazard. *Renaming the `.swf` files to `V01.swf` etc.* — rejected; source files are
read-only evidence and the manifest already carries the mapping. *Treating the
`SteveMauro060212` series as additional lessons* — rejected; different course,
different date, no evidence it belongs to this curriculum.
**Consequences:** Folder numbering under `Bootcamp Notes/` changed for 19 of 21
folders; any external reference to the old numbering is now wrong. V01 study proceeds
from transcript only. `SETUP_ISSUES.md` gains I-008 (20 unverified transcripts).
Week 6 is confirmed absent and documented as expected-missing; **no session may
fabricate or interpolate it.**
**Status:** ACTIVE

---

## D-018 — Mastery dimensions F and G may be marked NOT APPLICABLE for lessons that state no testable rule

**Date:** 2026-08-10
**Decision:** In `07_MASTERY_REPORTS/VXX_MASTERY_REPORT.md`, dimension **F (Homework)**
and dimension **G (Manual Backtesting)** of `MASTERY_STANDARD.md` may be recorded as
`NOT APPLICABLE` when the lesson itself supplies nothing to satisfy them, provided
the report states the specific justification and enumerates what was checked.

A lesson is eligible for `F = NOT APPLICABLE` when it assigns no work that a present-day
agent can perform — for example, work that consists of emailing a survey to the
instructor in 2012.

A lesson is eligible for `G = NOT APPLICABLE` when it states **no entry trigger, no
stop, no target, and no position size** — i.e. there is no rule in it whose
application to a historical chart could be graded.

`NOT APPLICABLE` is not a pass. It is a positive claim that the dimension has no
subject matter in this lesson, and the reviewer audits that claim like any other. If
a reviewer finds a testable rule the student missed, the correct outcome is `REVISE`
with the dimension reinstated.

The remaining eight dimensions (A Recall, B Recognition, C Discrimination, D Sequence,
E Exceptions, H Provenance, I Ambiguity, J Contradictions) always apply and are never
waived.

**Reason:** V01 forced the question. It is a framing lesson: it argues a thesis about
the weekly cycle and issues prohibitions, but §6 of `V01_SOURCE_NOTES.md` has an empty
Confirmation column and an empty Invalidation column across all eight rows, and no
stop, target, risk-to-reward, position size, or indicator parameter is stated anywhere
in its 54 minutes. Its homework is a 2012 student survey. Without this decision, V01
could never reach `PASS` on the merits, the sequential gate would never open, and the
course could not proceed past its first lesson — not because the study was deficient
but because the standard was being applied to material it does not fit.

The alternative failure mode is worse: if F and G must always be satisfied, a session
under pressure to advance will manufacture a backtest of rules the lesson never stated.
That is precisely the fabrication this project quarantined 72 files to avoid
(`QUARANTINE_REGISTER.md` Q-001).
**Evidence:** `V01_SOURCE_NOTES.md` §6, §10, §11; `MASTERY_STANDARD.md` dimensions F
and G; project owner confirmation 2026-08-10.
**Alternatives considered:** *Leave V01 open until a later lesson supplies testable
rules, then backtest V01 retroactively* — rejected by the project owner; it stalls the
sequential gate indefinitely and makes every lesson's completion depend on
unknown future material. *Lower the bar for F and G rather than waive them* —
rejected; a token backtest of a rule the lesson did not state is not a weaker test, it
is a false one. *Treat V01 as `NOT A LESSON`* — rejected; it plainly teaches, and its
concepts (anchor point, trap moves, the weekly cycle) are foundational to what follows.
**Consequences:** Applies to all 21 lessons, not just V01 — this sets the standard.
Most later lessons are expected to state testable rules and will therefore *not*
qualify; the waiver is expected to be rare, and a session claiming it for a
mechanics-heavy lesson should be treated with suspicion by the reviewer. Each use must
name the justification in the mastery report. `MASTERY_STANDARD.md` is not rewritten;
this decision governs its application and is cited from the report.
**Status:** ACTIVE

---

## D-019 — `NOT APPLICABLE` and `DEFERRED` are different dispositions, and D-018 grants only the first

**Date:** 2026-08-10
**Decision:** Refines `D-018` (which remains `ACTIVE` and is not superseded). When a
mastery dimension cannot be satisfied, the report must choose between two dispositions
and must not use them interchangeably:

| Disposition | Meaning | Effect | Who can grant it |
|---|---|---|---|
| `NOT APPLICABLE` | The lesson supplies **no subject matter** for the dimension. There is nothing to do, now or ever, for this lesson. | The item is **closed permanently**. It is never revisited. | `D-018`, for dimensions F and G only, subject to reviewer audit |
| `DEFERRED` | Subject matter **exists** and the work is performable in principle, but repository infrastructure or a prerequisite is missing. | The item **stays open** and is carried in `18_REVIEW/REVIEW_INDEX.md` under open research items until the blocker clears, then performed. | Any dimension |

The test is **not** "can this be done today". It is **"is there anything here to do at
all"**. Work that is merely blocked is `DEFERRED`, never `NOT APPLICABLE`.

**Worked example — V01 dimension F.** The student marked all eight homework items
`NOT APPLICABLE` under D-018. Review R1 upheld six and overturned two:

- H1–H3 (an 18-item survey emailed to the instructor's 2012 address), H6 (read your own
  broker account agreement — no account exists), H7 (execute concepts in demo — and V01
  supplies no concept with an executable form), H8 (use the instructor's MT4 template —
  the template is not in the library) → **`NOT APPLICABLE`**, correctly. These match
  D-018's own eligibility test: work no present-day agent can perform.
- H4 `[00:37:58]` ("on the one hour chart… start looking at the levels and the cycle")
  and H5 `[00:52:20]`, `[00:53:02]` ("mark the chart up once or twice", "go look at the
  pairs this week") → **`DEFERRED`**. These are observational chart exercises. They
  require a chart and a declared data source, **not** a rule definition — the instructor's
  own framing is to mark up a week and see whether the shape repeats. They are blocked by
  `I-007`, not inapplicable.

**Reason:** `NOT APPLICABLE` closes an item permanently. Applied to merely-blocked work
it silently discards performable research — in V01's case the only cheap empirical check
available against `CL3` ("Is it always like this?" — "Yeah"), the lesson's largest
unevidenced claim. D-018 as written did not distinguish the two, and V01 was about to set
that precedent for all 21 lessons.
**Evidence:** `18_REVIEW/V01/V01_REVIEW_R1.md` finding 2 (`E10`, MAJOR) and its
Homework section; `SETUP_ISSUES.md` I-007.
**Alternatives considered:** *Widening D-018 so blocked work also counts as
`NOT APPLICABLE`* — rejected; it converts an infrastructure gap into a permanent
research gap, and does so invisibly. *Reinstating dimension F in full and marking V01
incomplete* — rejected; six of the eight items genuinely have no subject matter, and
failing the lesson over a 2012 email address is the bureaucracy `REVIEW_PROTOCOL.md` §1
forbids. *Performing H4/H5 immediately* — rejected; with no data source, feed or
timezone declared, the observations would be unreproducible, which
`STUDY_PROTOCOL.md` §6 forbids.
**Consequences:** V01 dimension F becomes split (six `NOT APPLICABLE`, two `DEFERRED`).
H4/H5 are carried as open item 3 in `REVIEW_INDEX.md` and are performed when `I-007`
closes. Every future mastery report claiming `NOT APPLICABLE` must show the dimension
has no subject matter, not merely that it is currently blocked. The reviewer audits the
disposition, not just the conclusion.
**Status:** ACTIVE

---

## DECISIONS TO BE MADE AT INGESTION

Not yet decided; record as new entries when the information exists.

| Topic | Trigger |
|---|---|
| ~~Source library location and arrangement~~ | **Decided — D-017** |
| ~~Verified lesson count and ordering~~ | **Decided — D-017** |
| ~~Handling of any duplicate or non-lesson files found~~ | **Decided — D-017** |
| Whether the `SteveMauro060212` and Dean Malone series (X01–X21) enter the corpus | After V21 passes review |
| Chart data source / broker feed for manual backtesting | First manual backtest |
| Timezone convention for session and daily boundaries | First timing lesson |
| Default timeframes used in manual study | First chart lesson |
| Development / validation / holdout dataset boundaries | Phase 4–8 |
| Whether Git LFS is adopted for any media | Only if media must be versioned |

---

## D-020 — The SWF frame-rate speedup is ruled out; every lesson costs one real-time playthrough

**Date:** 2026-08-10
**Decision:** The frame-rate patching idea recorded as untested in
`SWF_CAPTURE_RECIPE.md` §11 was tested on V02 and **does not work**. §11 is rewritten
from a proposal into a ruled-out record. Capture planning for V03–V21 assumes one
real-time playthrough per lesson — roughly 18 further hours of unattended recording —
with no shortcut available.

Two consequences are adopted as standing practice:

1. **Start the recording before any other work in the session.** It needs no attention
   and it is the long pole. On V02 it was launched ~7 minutes in, and transcript
   verification, the quarantine audit, source notes, interpretation and register updates
   all completed while it ran. The hour cost effectively nothing in wall clock.
2. **Record once and keep the mp4.** The archival pass and the screenshot pass are the
   same pass; there is no separate "is the mp4 worth it" decision to make per lesson,
   because the recording has to happen anyway to get screenshots at all. Retaining it
   makes every future timestamp an `ffmpeg -ss` away and removes any reason to record a
   lesson twice.

**Reason:** the test was cheap (~6 minutes) and the stakes were 18 hours, so it was
worth running before committing. It failed for the first of the two reasons §11 had
flagged as unknown: the Camtasia player drives its slides from an internal timer or
audio position, not from the SWF root timeline.

**Evidence:** three runs at 120 fps, 1 fps and 3 fps (unmodified control), all showing
the player's burned-in timecode reading exactly `01:00` after 60 seconds of wall clock.
The 1 fps run is the decisive one — a frame-rate ceiling could explain a missing
speed-*up*, but nothing can explain a missing slow-*down*. Full method and numbers in
`SWF_CAPTURE_RECIPE.md` §11.

**Alternatives considered:** *Accepting the idea untested and skipping real-time capture
for V03–V21* — rejected before testing; it would have produced screenshot sets with no
archival source and no way to verify a timestamp. *Declaring it ruled out on the 120 fps
run alone* — rejected as insufficient; that run cannot distinguish "header ignored" from
"header honoured but rate-capped", and the recipe's own §11 had named the cap as a live
possibility. *Re-testing on a third lesson* — rejected; the control run already
establishes the header has no effect on this player, and all 21 files are the same
Camtasia export family.

**Note on the arithmetic that made the idea attractive.** It was not a bad hypothesis.
V02's frame count (10861) ÷ its declared 3 fps = 3620.3 s against a measured audio length
of 3619.8 s — the root timeline really is exactly as long as the presentation. It is just
not what the player uses as its clock.
