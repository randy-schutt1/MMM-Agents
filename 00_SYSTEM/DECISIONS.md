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

> **CROSS-REFERENCE added 2026-08-10. D-004's meaning is unchanged and it is not
> superseded** — this is a forward pointer only, of the same kind as D-019's citation fix.
> Read D-004 together with:
>
> - **D-024 — what holds the gate closed.** A `REVISE` carrying **only `MINOR`** findings
>   (0 `CRITICAL`, 0 `MAJOR`) **opens** the gate for lesson N+1; the minor fixes are still
>   tracked and must be completed before lesson N reaches `COMPLETE`. Any `CRITICAL` or
>   `MAJOR` finding, or a `BLOCKED`, keeps it **closed** until fixed **and re-reviewed**.
>   D-004's core is untouched: only the reviewer opens the gate, and only a reviewer
>   `PASS` makes a lesson `COMPLETE`.
> - **D-023 — the one authorized exception on record.** The parallel V03 work performed
>   while the V03 gate read `CLOSED` was an owner-authorized one-time override, not a
>   breach to correct. It is not precedent.
>
> **Added 2026-08-11:**
>
> - **D-025 — what a lesson N+1 session must do before it starts, when the lesson has more
>   than one voice.** An open gate is permission to begin, not permission to skip speaker
>   tagging. Guest-presenter material is secondary **descriptive** evidence and is excluded
>   as **normative** doctrine; tagging is mandatory before notes are written. This is a
>   precondition on the work N+1 does, not a condition on the gate itself.

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

> **CROSS-REFERENCE added 2026-08-11. D-008's meaning is unchanged and it is not
> superseded** — this is a forward pointer only, of the same kind as D-004's.
> Read D-008 together with:
>
> - **D-025 — the hierarchy *inside* the course.** D-008 ranks the course against the
>   agent; it does not distinguish speakers, because no lesson before V04 had more than
>   one voice. Guest-presenter material is **secondary DESCRIPTIVE** evidence, sitting
>   strictly below any instructor statement, and is **excluded as NORMATIVE** doctrine. It
>   may **extend** an `A-xxx`/`C-xxx` record and may **never close** one. Speaker tagging
>   is mandatory for any multi-voice lesson from V04 forward.

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
  and H5 `[00:52:38]`–`[00:52:50]`, `[00:53:07]` ("mark the chart up once or twice", "go
  look at the pairs this week") → **`DEFERRED`**. These are observational chart exercises. They
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

> **CITATION CORRECTED 2026-08-10 per review R2 finding N4 (`E11`).** H5 was cited above
> as `[00:52:20]`, `[00:53:02]`. Those markers carry *"Is this the cycle?"* and
> *"Sometimes it might start on Thursday"* — neither is the assignment. The assignment is
> at `[00:52:38]`–`[00:52:50]` ("if you haven't marked the chart up once or twice and
> looked at Wow, same shit every week…") and `[00:53:07]` ("Go look at the pairs this
> week"), which is what `V01_SOURCE_NOTES.md` §11 has always had. The error originated in
> review R1 and was propagated into this record.
>
> **The decision's meaning is unchanged and it is not superseded** — this is a citation
> fix made in place, as `DECISIONS.md` is append-only *as to meaning*, not as to
> typography. D-019 remains `ACTIVE` in its original form.

---

## D-026 — Every manual backtest requires a pre-registered baseline

**Date:** 2026-08-11
**Decision:** No manual backtest result may be recorded, summarized, or cited without
a **baseline defined in advance**. The required baseline is **matched random entry**
(same instrument, session, eligible window, stop and target distances, and n; entry
bar randomized; ≥200 iterations, distribution reported). Where the sample permits, the
course's own inside-box / outside-box contrast is run as a second arm. Full
specification: `BACKTEST_EVIDENCE_STANDARD.md` §2.

A **hard gate** applies: no `BT_*.md` file may be written until the baseline decision
for that rule exists in this file. `scripts/validate_project.py` fails the build if a
backtest observation exists without it.

**Reason:** A hit rate with no comparator is unreadable. The method claims ~1:2.8 R:R
and *"in profit in 15 to 45 minutes, guaranteed"* (V04 `[00:08:56]`); against those
claims a 60% hit rate cannot be distinguished from random entry in the same sessions,
or from any long taken in a week that trended up. The repository had **zero** mentions
of a baseline before this decision — an external methodological review identified the
gap.
**Evidence:** External review, 2026-08-11, four questions on backtest implementation.
Repository grep for baseline / coin-flip / random entry / null hypothesis / control:
one hit, unrelated.
**Alternatives considered:** Baseline "where practical" — rejected; optional rigour is
skipped exactly when a result looks good. Deferring to Phase 8 — rejected; the manual
results would already be in the corpus, cited by later work, unlabelled.
**Consequences:** Adds work to every test. `MANUAL_BACKTEST_TEMPLATE.md` gains a
pre-registration block that must be filled before charts are opened.
`REVIEW_PROTOCOL.md` §6.G gains checks 15–20 and codes `E21`–`E25`; a missing or
post-hoc baseline is `CRITICAL`. Recorded before any observation existed, so **nothing
required rework**.
**Status:** ACTIVE

---

## D-027 — Test periods are pre-registered; a holdout is reserved

**Date:** 2026-08-11
**Decision:** The instrument, date range, timeframe and session boundaries of a
manual backtest are recorded in this file **before any chart in that range is
examined**. A contiguous holdout block — recommended: the most recent 30% of
available history — is **not opened during the Student Phase** by any session for any
reason. Changing a range mid-test creates a **new test ID**; the abandoned test is
retained and marked. Full specification: `BACKTEST_EVIDENCE_STANDARD.md` §3.

**Reason:** The rules themselves are genuinely pre-registered — transcribed from 2012
lectures, fixed before any chart was opened, and never fitted to price data. That is
stronger than a conventional train/test split on that axis, and it is **not
sufficient**: it does nothing about a *period* selected, consciously or not, because
it looked cooperative. The holdout also gives the end-of-course rule set one honest
test against data no session has seen.
**Evidence:** External review question 3 ("is there a train/test split"). Answer at
the time: none for the manual phase; the only holdout language sat in
`15_AUTOMATED_BACKTEST/README.md` for Phase 8, where boundaries were still an unmade
decision.
**Alternatives considered:** Relying on rule pre-registration alone — rejected for the
reason above. Setting the boundaries here — rejected; the specific split is the
owner's call and no agent may invent it. This decision requires that boundaries exist
and be recorded, and supplies a recommended default only.
**Consequences:** The concrete development/holdout boundary remains **an open decision
owed by the owner** before the first observation (see the table below). Inspecting the
holdout is `E23` and converts it into development data — which must then be disclosed,
not quietly ignored.
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
| **Manual-phase development / holdout boundary (D-027)** | **OWED NOW — before the first BT_ observation** |
| **Baseline parameters per rule (D-026): iterations, eligible window, direction handling** | **OWED NOW — before the first BT_ observation** |
| Development / validation / holdout dataset boundaries (automated, Phase 4–8) | Phase 4–8 |
| Whether Git LFS is adopted for any media | Only if media must be versioned |

---

## D-020 — RETRACTED — "the SWF frame-rate speedup is ruled out"

```text
STATUS: RETRACTED 2026-08-10, same session, before push.
        The finding was WRONG. Superseded by D-021.
```

**This decision is left in place rather than deleted, because the way it was reached
matters more than the conclusion.** It recorded that the frame-rate speedup does not
work, on the strength of three runs including a control. The runs were real and the
reasoning about them was sound. The inputs were not: **none of the three runs was
playing the file it was supposed to be playing.**

A leftover `python3 -m http.server 8899` from the V01 session still owned port 8899.
This session's own server silently failed to bind, and the check that was supposed to
confirm it — `curl -sI http://127.0.0.1:8899/index.html` returning `200` — was answered
by the V01 session's server. That server's `index.html` is hardcoded to load `v01.swf`
and ignores the `?swf=` parameter entirely. So every browser render in this session,
including all three frame-rate runs and a 61-minute "V02" capture, played **V01's
unpatched SWF**. Patched files were written to disk and never served.

The control run is the sharpest lesson. A control is supposed to protect against exactly
this class of error, and this one did not, because the treatment and the control were
*the same file*. A control only isolates the variable you think you are changing if you
have independently confirmed you are changing it. **Verify the input reached the system
under test before trusting any comparison between conditions.**

What the retraction does and does not touch:

| Invalidated | Unaffected |
|---|---|
| The frame-rate finding and this decision | V02 transcript verification (audio was read from disk with `ffmpeg`, never through the server) |
| `SWF_CAPTURE_RECIPE.md` §11 as first rewritten | Q-002, the V02 fabrication audit (text analysis of files on disk) |
| The 61-minute capture, its 3.52 s offset, its sync strip and its 21-state contact sheet | `V02_SOURCE_NOTES.md`, `V02_INTERPRETATION.md` (written from the transcript alone) |
| A transient reading that V02's SWF contained V01's video | A-019…A-025, C-003, the C-001 re-test (all transcript-derived) |
| A "screen" of all 21 files that appeared to show a shared 54:44 duration | SWF header/tag parsing (read from disk: 3.0 fps, 10861 frames) |

The V02-contains-V01's-video alarm was the same artifact: the renders really were V01,
because V01 is what was being served.

**Original decision text follows, retained for the record.**

**Date:** 2026-08-10
**Decision (RETRACTED):** The frame-rate patching idea recorded as untested in
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

---

## D-021 — The SWF frame-rate speedup WORKS at 40×; it is the default screenshot method

**Date:** 2026-08-10
**Supersedes:** D-020 (retracted — see above for why it was wrong)

**Decision:** Patching the declared frame rate in a working copy of the `.swf` makes
Ruffle advance the presentation proportionally faster. Measured at **exactly 40×** with
a 120 fps patch. This becomes the default method for screenshot capture. Real-time
capture is now only required when a synced audio+video mp4 is specifically wanted.

**Measurements** (V02, patched copy vs unpatched control, both served from a
port-verified local server):

| Wall clock | 120 fps patched | 3 fps control |
|---|---|---|
| 20 s | 13:20 | 00:20 |
| 40 s | 26:40 | 00:40 |
| 60 s | 40:00 | 01:00 |

40:00 of presentation in 60 s of wall clock is 40.0×, sustained and linear across all
three sample points. **The `requestAnimationFrame` ceiling named as unknown #2 in the
original §11 is not a constraint** — Ruffle advances as many timeline frames per tick as
the declared rate requires, so the practical ceiling is well above the 20× that was
feared. The player's burned-in timecode advances correctly at speed, so each screenshot
still proves its own timestamp.

**Chosen operating point: 10× (patch 3.0 → 30.0 fps), not 40×.** At 10× a full 60-minute
lesson sweeps in about 6 minutes, and a screenshot every 0.5 s of wall clock yields the
same 5-second sampling grid the recipe's thumbnail step already assumes. 40× is available
but compresses the screenshot cadence to the point where Playwright's own capture latency
becomes the limit, and it leaves less margin for correct delta-tile compositing. Speed is
no longer the bottleneck, so the safer rate is the right default.

**Effect on the V03–V21 estimate:** the ~18 hours of unattended real-time recording that
D-020 budgeted is not required for screenshots. Per-lesson capture drops from ~60 minutes
to ~6.

**Evidence:** `SWF_CAPTURE_RECIPE.md` §11, rewritten from the corrected runs.

**Alternatives considered:** *Standing by D-020 and re-recording in real time* — rejected;
D-020's inputs were demonstrably wrong and the corrected test is unambiguous.
*Adopting 40× as the default* — rejected for the cadence and compositing-margin reasons
above; the marginal saving over 10× is minutes, and the risk is a silently corrupted
frame.

---

## D-022 — Every locally served capture must verify the port and the bytes before use

**Date:** 2026-08-10
**Decision:** Before any Ruffle capture, the session must confirm (a) that the HTTP
server on the chosen port is **its own**, and (b) that the bytes served for the target
URL match the file on disk. Both checks, every time. A `200` response is not evidence of
either.

```bash
PORT=8917
lsof -nP -iTCP:$PORT -sTCP:LISTEN && { echo "PORT BUSY - pick another"; exit 1; }
cd serve && python3 -m http.server $PORT & sleep 2
lsof -nP -iTCP:$PORT -sTCP:LISTEN            # must be this session's PID
diff <(curl -s http://127.0.0.1:$PORT/target.swf | shasum -a 256 | cut -d' ' -f1) \
     <(shasum -a 256 serve/target.swf        | cut -d' ' -f1) || exit 1
```

Also: **give each served file a unique name.** Reusing one filename such as
`probe_tmp.swf` across files lets HTTP/browser caching return a stale body, which
produced a second false result in this session (a "screen" of all 21 lessons that
appeared to show every file declaring the same 54:44 duration — it was one file, 21
times).

**Reason:** `python3 -m http.server` fails to bind a busy port and exits, leaving any
previously running server on that port to answer instead. Multiple concurrent sessions
share this machine and this repository, so a stale server from another session is not a
remote possibility — it is what happened. The failure is silent, produces confident and
internally consistent results, and cost this session a 61-minute capture, a wrong
decision record, and two spurious findings about the source library.

**Evidence:** D-020 retraction; `SETUP_ISSUES.md` I-009.

---

## D-023 — The parallel V03 work performed under a closed gate was an owner-authorized override of D-004, not an error

**Date:** 2026-08-10
**Decision:** The V03 student work that appeared in the working tree while
`COURSE_PROGRESS.md` read `V03 GATE: CLOSED` — V03 transcript, `04_SCREENSHOTS/V03/`,
`05_HOMEWORK/V03/`, `QUARANTINE_REGISTER.md` Q-003, and the V03 screenshot capture
committed as `1c836df` and `9f60f22` — was started **deliberately and with the project
owner's explicit authorization**, as a one-time override of the D-004 progression gate.
It is **not** a discipline failure, **not** to be reverted, re-done, discarded or
re-audited as tainted, and no session may treat it as such.

The override is **retroactive in recording only, not in authorization**: the owner made
the call at the time; what was missing was the written record. This entry supplies it.

**Scope of the override — deliberately narrow:**

| Covered | Not covered |
|---|---|
| Beginning V03 source-side work (transcript verification, screenshot capture, quarantine audit) while V02 was in remediation | Any V03 mastery report, review, or `PASS` claim while V02 was unpassed |
| The specific artifacts named above, as committed | Any *future* instance — D-004 is not weakened, and this entry is not precedent |
| One instance, V02 → V03, 2026-08-10 | Any lesson pair beyond V02 → V03 |

D-004 remains `ACTIVE` and is **not superseded**. An override is a single authorized
exception to a standing rule, recorded as such; it is not a change to the rule. The
general standing refinement of when the gate holds is `D-024`, which is a rule change and
is written separately for exactly that reason.

**Reason:** the repository currently records an authorized action as an unresolved
violation, in `COURSE_PROGRESS.md`'s `V03 GATE` block (*"⚠ BREACHED — LIVE"*, *"No V03
work of any kind until V02 R2 returns PASS"*), in `REVIEW_INDEX.md` open items 9 and 17,
and in `V02_REVIEW_R2.md` §7's required disposition (*"stop the V03 pass"*). Both the R2
and R3 reviewers flagged this correctly on the evidence available to them — nothing was
written down, so from the repository's point of view nothing was authorized. That gap is
the expensive kind: a future session reading `COURSE_PROGRESS.md` will either halt work
the owner authorized, or conclude the gate register is unreliable and stop trusting it.
Under D-001 the repository *is* the project memory, so an owner decision that lives only
in a chat session does not exist.

**Evidence:** `18_REVIEW/V02/V02_REVIEW_R2.md` §7 and finding 9 (`MAJOR`, process,
`E20`); `18_REVIEW/V02/V02_REVIEW_R3.md` NOTE 3 (*"the breach is now an authorized
override, and the repository does not say so"*), which explicitly asks the owner to record
it as a numbered decision and reconcile the three locations to it;
`18_REVIEW/REVIEW_INDEX.md` open items 9 and 17; `COURSE_PROGRESS.md` `V03 GATE` block
and `NEXT ACTION` carry-forward item (c), which names this as **owner action, not student
action**. Project owner confirmation, 2026-08-10.

**Alternatives considered:** *Reverting the V03 work to restore the gate's integrity* —
rejected by the owner; the work is sound on its own terms, R2 examined it and drew no
content finding from it, and discarding correct work to satisfy a rule the owner chose to
waive is pure cost. *Leaving it unrecorded on the grounds that V02's R3 `PASS` opened the
V03 gate anyway and the question is forward-moot* — rejected; forward-moot is not
backward-clean. The three locations above still read as a live violation, and R3 named
that as a documentation-integrity defect independent of the gate's current state.
*Silently editing `COURSE_PROGRESS.md` and `REVIEW_INDEX.md` to remove the breach
language* — rejected outright; that erases the record of a real process event, and the
audit trail of how a rule came to be overridden is worth more than a tidy file.
*Amending D-004 itself to permit parallel work* — rejected as the wrong instrument for a
one-time exception; see D-024 for the part that genuinely is a rule change.

**Consequences:** `COURSE_PROGRESS.md`'s `V03 GATE` block is reconciled to this entry,
with its breach history retained in place rather than deleted. `REVIEW_INDEX.md` open
item 17 (*"an owner-authorized override is recorded in the repository as an unresolved
violation"*) is **CLOSED** by this entry. `V02_REVIEW_R2.md` is **not** edited —
`REVIEW_PROTOCOL.md` §11 forbids overwriting an earlier review, and R3 is the correct
place the update was made.

**Open item 9 is NOT closed by this entry, and must not be.** Its mechanism finding
survives the override intact: *a written gate with no enforcement failed twice in one
day.* The override explains why the second occurrence was authorized; it says nothing
about why an unauthorized one would have been caught. The concrete fix is unchanged — a
pre-flight guard in `validate_project.py` that refuses `VNN` artifact creation while
`VNN GATE` reads `CLOSED`, with an explicit owner-override flag that must name the
decision entry authorizing it.
**Status:** ACTIVE

---

## D-024 — Finding severity, not review verdict alone, determines whether the progression gate holds

**Date:** 2026-08-10
**Refines:** D-004, which remains `ACTIVE` and is **not superseded**. D-004 established
*that* there is a gate and that the reviewer alone opens it. This entry defines *what
holds it closed*.

**Decision:** A review round's effect on the progression gate is determined by the
severity of its findings, per `REVIEW_PROTOCOL.md` §8:

| Review outcome | Gate for lesson N+1 | Lesson N's own status |
|---|---|---|
| `PASS` | **OPEN** | `COMPLETE` |
| `REVISE` with **0 `CRITICAL` and 0 `MAJOR`** — minor findings only | **OPEN.** Work on lesson N+1 may begin immediately; the minor corrections do not have to be applied first | Stays `IN REMEDIATION`, **not** `COMPLETE` |
| `REVISE` with **any `CRITICAL` or `MAJOR`** finding | **CLOSED.** No lesson N+1 work of any kind until those findings are fixed **and re-reviewed** in a fresh round | `IN REMEDIATION` |
| `BLOCKED` | **CLOSED**, unconditionally | `IN REMEDIATION` |

Three points that are part of the decision, not commentary on it:

1. **Minor findings are deferred, never dropped.** Every outstanding minor from a
   gate-opening `REVISE` is carried in `18_REVIEW/REVIEW_INDEX.md` as an open item and
   named in `COURSE_PROGRESS.md`'s `NEXT ACTION`, and must be applied and verified before
   lesson N can reach `COMPLETE`. Opening the gate buys parallelism, not amnesty.
2. **An open gate is not a `PASS`.** Lesson N's row reaches `COMPLETE` only on a reviewer
   `PASS` — D-004 and `COURSE_PROGRESS.md`'s Final Status legend are untouched on that
   point. The gate and the lesson's status are two different facts and must not be
   collapsed into one.
3. **The reviewer's severity classification is the input, and it is not negotiable by the
   student session.** A session may not downgrade a `MAJOR` to a `MINOR` in order to open
   a gate. Disagreement with a severity is raised as a finding in the next review round,
   the same as any other dispute.

**Reason:** D-004 as written treats every non-`PASS` identically, which makes the gate
maximally strict but also makes it expensive in exactly the cases where strictness buys
nothing. `REVIEW_PROTOCOL.md` §8 already defines `MINOR` as *"documentation, wording, or
completeness problem that does not alter the method"* — by the protocol's own definition,
a minor finding cannot corrupt what lesson N+1 inherits, which is the entire hazard D-004
exists to prevent (*"a misunderstanding to propagate into pattern definitions, Pine
Script, backtests, and eventually capital loss"*). Holding an 18-lesson course on a
wording fix converts a safety rule into bureaucracy, which `REVIEW_PROTOCOL.md` §1
explicitly forbids.

The V02 history is the worked example and the reason this is being written now rather
than at the next collision. V02 R1 returned `REVISE` with 1 `MAJOR` — the gate correctly
should have held, and the hazard was real: the `MAJOR` was in the pixel-measurement
pipeline V03's chart work would have inherited. V02 R2 returned `REVISE` with 0
`CRITICAL`, 0 `MAJOR`, 3 `MINOR` (plus a process finding charged against the project, not
the lesson) — nothing there could contaminate V03, and V02 R3 subsequently confirmed
`PASS` on the merits after those minors were applied. Under this decision R2 would have
opened the gate on its own terms and no override would have been needed. **The rule this
produces is the one that would have made D-023 unnecessary**, which is the test of whether
a policy is right rather than merely convenient.

The converse half matters as much and is stated as flatly: **a `CRITICAL` or `MAJOR`
finding closes the gate, full stop.** Not "closes it pending judgement", not "closes it
unless the finding looks localized". `REVIEW_PROTOCOL.md` §8 already holds that a lesson
with unresolved `CRITICAL` issues cannot pass; this extends the same treatment to the
gate, and to `MAJOR`. Fixed **and re-reviewed** — a student session applying its own fix
and declaring itself satisfied is precisely the self-certification D-003 and D-004 exist
to prevent.

**Evidence:** `REVIEW_PROTOCOL.md` §8 (severity definitions), §2 (decision vocabulary),
§9 (decision standards — `PASS` criterion 14, *"remaining issues are minor and do not
corrupt downstream learning"*, which is this decision's principle already stated for the
`PASS` case), §1 (*"The purpose is quality control, not bureaucracy"*).
`18_REVIEW/V02/V02_REVIEW_R1.md` (1 `MAJOR`, gate correctly held),
`18_REVIEW/V02/V02_REVIEW_R2.md` (0 `CRITICAL`, 0 `MAJOR`, 3 `MINOR`),
`18_REVIEW/V02/V02_REVIEW_R3.md` (`PASS`). Project owner instruction, 2026-08-10.

**Alternatives considered:** *Leaving D-004 absolute* — rejected; it is what forced an
override on the first occasion the distinction mattered, and a rule that gets overridden
the first time it binds is a rule that was mis-specified, not a rule that was disobeyed.
*Opening the gate on any `REVISE` regardless of severity* — rejected outright; that
deletes the gate. The V02 R1 `MAJOR` sat in the measurement pipeline V03 would have
inherited, which is the concrete case for keeping the strict half strict. *Letting the
reviewer decide per-round whether the gate opens* — rejected; it makes the gate a
judgement call that varies by reviewer session, and the reviewer already encodes exactly
the needed judgement in the severity classification. Deriving the gate mechanically from
severity keeps it auditable and keeps `validate_project.py` able to enforce it.
*Allowing minor fixes to be waived rather than deferred once the gate opens* — rejected;
minors that are never applied accumulate silently into the corpus, and the project has
already recorded staleness of exactly this kind six times (`V02_REVIEW_R3.md` NOTE 4).

**Consequences:** `COURSE_PROGRESS.md`'s `PROGRESSION RULE` block, which read *"No
exceptions"*, is restated in terms of this decision and points here. `REVIEW_PROTOCOL.md`
§2 and §8 gain a cross-reference so a reviewer session classifying a finding can see that
the classification now carries gate consequences. D-004 gains a forward pointer. Future
review rounds must state their `CRITICAL` / `MAJOR` / `MINOR` counts explicitly enough
that the gate state follows mechanically from the review file — R1–R3 of V01 and V02
already do this in their executive blocks, so no format change is required. The
`validate_project.py` pre-flight guard proposed under `REVIEW_INDEX.md` open item 9 should
implement this table rather than D-004's simpler `PASS`-only reading.
**Status:** ACTIVE

---

## D-025 — Guest-presenter material is secondary DESCRIPTIVE evidence and is excluded as NORMATIVE doctrine

**Date:** 2026-08-11
**Refines:** D-008 (course evidence outranks agent interpretation), which remains `ACTIVE`
and is **not superseded**. D-008 ranks *the course* against *the agent*. This entry ranks
speakers *inside* the course, which D-008 did not contemplate because no lesson before V04
had more than one voice.

**Decision:** When a lesson contains material delivered by someone other than the course's
author — a guest presenter, a coach, an invited student — that material is admissible as
**SECONDARY, DESCRIPTIVE evidence** and is **EXCLUDED from the canonical methodology as
NORMATIVE material.** The operative distinction is **normative versus descriptive**, not
"in or out". Neither extreme is correct: guest material is not course doctrine, and it is
not to be discarded.

| Class | What it is | Treatment |
|---|---|---|
| **NORMATIVE** — what to do: entry criteria, gates, filters, stops, targets, sessions, thresholds, watchlists, schedules, holding periods | The V04 guest's ADR ~90–95% gate; 7 pips + spread below the LOD; 35–50 pip targets; *"don't trade Mondays"*; the 12-pair list **as a rule**; *"no second legs in the US session"* | **EXCLUDED from doctrine.** May not enter `12_MASTER_SPEC/`, `13_MACHINE_SPEC/`, `08_CONCEPT_LIBRARY/`, or any machine candidate. May not be cited as evidence **for or against** an instructor rule. May **never** be merged with instructor statements into one rule set. Recorded, speaker-tagged, fenced |
| **DESCRIPTIVE** — that a term exists, how it is spelled, that an object is displayed, what a printed artifact says | The printed *"Mayo"* caption; the printed `TDI / Shark Fin / Stop / MM Candles / Divergence / Pivot / ADR / HOD LOD` form; the `TDR / YDR / WADR / MADR / %DADR` panel (`A-040`); the 12-pair worksheet **as a fact about the frame**; the visible `Traders Dynamic Index Visual` panel in frames 21 and 22 | **ADMISSIBLE**, at a weight **strictly below any instructor statement**. May **EXTEND** an `A-xxx` or `C-xxx` record. May **never CLOSE or RESOLVE** one, and may never outweigh an instructor statement |

Four consequences that are part of this decision, not commentary on it:

1. **A guest statement can never resolve an ambiguity or a contradiction.** `A-020`'s
   period, `A-018`'s `R`, `A-031`'s *"water"* stay open regardless of how clearly or how
   often a guest uses the terms. Descriptive guest evidence **extends** a record; only an
   instructor statement can close one.
2. **A guest/instructor divergence is not a contradiction in the method** and must not be
   logged against the instructor. `C-005` is correctly filed as a **corpus-hygiene**
   record, and that is the right category for every future instance.
3. **Speaker tagging is MANDATORY from V04 forward** — in the transcript header and on
   every source-note row — for any lesson with more than one voice. A session must
   determine whether a lesson has guest content **before** writing notes from it, not
   after. This is the mechanism that makes the rest of this decision enforceable.
4. **Identifying a guest is provenance, not evidence.** Nothing in any artifact may depend
   on the identification being right.

**Reason:** V04 is the first lesson in the corpus where the course's author speaks for only
~31% of the runtime; an unannounced, unlabelled handover at `[00:26:56]`→`[00:26:59]` gives
the remaining ~69% to a guest presenter. Without a rule, the next session reading that
transcript has two ways to go wrong and no way to tell which it has chosen.

*Granting the guest full weight* would synthesise a rule set **neither man stated** —
`REVIEW_PROTOCOL.md` §17 failure mode 3 (rule drift) in its purest form — and would do so
inside the one lesson that finally states a complete entry rule. The guest disclaims
authority in his own words (*"this is just me"* `[00:46:19]`, *"that's simply just my
opinion"* `[01:00:10]`), attributes the entire method to the instructor, and describes a
session in which the instructor's **necessary** condition, the second leg, *mostly does not
occur* (*"in the US session, you generally don't get a lot of second lads [legs]. You just
don't get them"* `[01:14:13]`–`[01:14:18]`).

*Excluding the guest entirely* — from rules **and** interpretation — is the error in the
opposite direction and it is not free. It would require retracting `A-040`, half of
`04_SCREENSHOTS/V04/INDEX.md` §"What the visuals added", and the corroboration of the
*"Mayo"* spelling, all of which are facts about **printed artifacts**, not claims about
method. It would also discard the strongest available corroboration that the instructor's
own vocabulary means what this project thinks it means — the guest's pre-trade checklist
slide prints *"Has there been 3 levels of rise or correction?"*, *"Are we at or near the mid
week Reversal?"*, *"3 Swipes / False Move / Trap"*, *"Was ADR met?"*: the instructor's
terms, in print, written by someone who learned them directly from him. That is genuine
evidence about **terminology**, and throwing it away buys nothing.

**Evidence:** `18_REVIEW/V04/V04_REVIEW_R1.md` § "THE C-005 RULING — GUEST-PRESENTER
MATERIAL" (the ruling in full, with the speaker identification independently verified at
that round: 3,518 s of 5,137 s = 68.5% guest runtime; 40+ third-person references to Steve
across segment B; `[01:24:53]` *"Steve is asking, do you ever take continuation trades?"* —
the instructor in the audience, asking a question).
`11_CONTRADICTIONS/CONTRADICTIONS.md` C-005. `02_TRANSCRIPTS/V04/V04_TRANSCRIPT.md`
§ "TWO SPEAKERS — A PROVENANCE BOUNDARY THAT MATTERS". `DECISIONS.md` D-008.
`REVIEW_PROTOCOL.md` §17 failure mode 3. `REVIEW_INDEX.md` open item 22.

**Alternatives considered:** *Full weight — treat the guest as course doctrine* — rejected;
it manufactures a rule set neither speaker stated, and it would let a practitioner's US-
session habits overwrite the instructor's London stop-hunt method inside the very lesson
that states it. *Full exclusion — strike guest material from rules **and** interpretation* —
rejected; it destroys descriptive evidence about printed artifacts and terminology that
costs nothing to keep and cannot mislead, because a printed caption makes no claim about
what to do. *Case-by-case adjudication with no standing rule* — rejected; it makes
admissibility a per-session judgement call, which is exactly the drift D-001 and D-004
exist to prevent, and V05 begins under the same session date with a third presenter
("Carl") already queued at `[01:19:02]`.

**Consequences:**

- **Retroactive effect on V04: NONE. This decision ratifies the work already done.** V04's
  interim handling — tag every row, admit no `GUEST` row into the methodology, adopt no
  `GUEST` number — is exactly the normative half of this ruling, and the descriptive uses
  it made (`A-040`, the *"Mayo"* corroboration, the printed forms transcribed in source
  notes §3b/§4f, the visible TDI panel added under review R1 `M6`) are exactly what the
  descriptive half permits. **No V04 grade changes and no V04 artifact is rewritten on this
  ground.** `C-005` stays open as a corpus-hygiene record; the *scope* question it raised
  is now answered.
- **Prospective effect on V05–V21: speaker tagging is mandatory.** Before writing notes
  from any future lesson, the session must establish how many voices the recording carries
  and mark the boundaries; where there is more than one, every source-note row carries a
  speaker tag and the transcript header carries a speaker table. `REVIEW_INDEX.md` open
  item 22 is discharged.
- A future session that reads `C-005` must **not** take it as an instruction to *delete*
  guest-derived corroboration. That misreading is what this entry exists to prevent.
- `A-039` gains guest frames as **descriptive** evidence that TDI is displayed, and is
  **not** narrowed by them — "displayed, not taught".

**Status:** ACTIVE
