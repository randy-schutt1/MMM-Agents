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

## D-028 — Manual-phase development / holdout split is 70 / 30

**Date:** 2026-08-11
**Decision:** Whatever contiguous GBP/USD history the project uses for manual
backtesting is split by time: the **oldest 70% is DEVELOPMENT**, the **most recent 30%
is HOLDOUT**. The holdout is not opened by any session, for any reason, during the
Student Phase. Owner approved 2026-08-11.

**Concrete dates are pinned at first use, not now.** `I-007` is still open — no chart
data source, feed or timezone has been declared — so the available range is unknown and
any dates written today would be invented. The first session to establish the data
source computes the 70/30 boundary from the actual available range, records the exact
dates by appending to this decision, and only then opens a chart.
**Reason:** The rules are pre-registered by the course, but the *period* is not. A
holdout is what stops a favourable-looking stretch from being chosen, consciously or
not, and gives the end-of-course rule set one honest test against data no session has
seen.
**Evidence:** External methodological review, 2026-08-11 (question 3). Owner decision
same day.
**Alternatives considered:** 80/20 — rejected, leaves too thin a final exam for a
method with this many conditional branches. Random or interleaved sampling — rejected;
FX regimes cluster in time, so a random split leaks regime information across the
boundary.
**Consequences:** Opening the holdout is `E23` and converts it permanently into
development data — which must then be **disclosed**, not quietly absorbed. Once the
boundary dates are appended here, `validate_project.py` can check observation dates
against them.
**Status:** ACTIVE — boundary dates PENDING first data-source decision

> ### APPENDED 2026-08-13 — FIRST BOUNDARIES PINNED, AND THEY ARE SCOPED
>
> `D-028` requires that *"the first session to establish the data source computes the 70/30
> boundary from the actual available range, records the exact dates by appending to this
> decision, and only then opens a chart."* Executed here for the two series `PT-023` and
> `PT-024` used. Computed **before any window statistic was read**, by
> `06_MANUAL_BACKTEST/V06/run_pt023.py`.
>
> | Series | `T0` | `T1` | Boundary `B` (oldest 70%) | DEVELOPMENT | HOLDOUT |
> |---|---|---|---|---|---|
> | GBP/USD **15-minute, TradingView/FXCM** | 2026-07-20 23:15 | 2026-08-13 10:30 | **2026-08-06** | 07-20 → 08-05 | 08-06 → 08-13, **not opened** |
> | GBP/USD **30-minute, Yahoo Finance** | 2026-05-21 23:00 | 2026-08-13 08:00 | **2026-07-19** | 05-21 → 07-17 | 07-19 → 08-13, **not opened** |
>
> **These are SCOPED boundaries and must not be read as the project-wide `D-028` split.** Each
> is the 70/30 point of *one series on one vendor at one timeframe*, and the two disagree by
> three weeks because the vendors serve different depths. A standing project-wide boundary
> requires a standing data-source decision — **`I-007`, which is still OPEN and is the owner's
> to make.** Recording a scoped boundary executes `D-028` for the tests that needed it; it does
> not discharge `D-028` for the project.
>
> **`D-028`'s meaning is unchanged and it is not superseded** — this is the append the decision
> itself instructs, of the same kind as `D-019`'s citation fix.

> ### APPENDED 2026-08-13 (later, same day) — THE PROJECT-WIDE BOUNDARY IS NOW PINNED
>
> The scoped boundaries above stand, and the project-wide split they explicitly declined to
> make has since been made: **`D-035` pins it at 2016-07-01** over the corpus
> `2013-01-06 → 2017-12-29` (DEVELOPMENT `2013-01-06 → 2016-06-30`; HOLDOUT
> `2016-07-01 → 2017-12-29`), following `D-034`'s data-source declaration which closed
> `I-007`. This decision's status line — *"boundary dates PENDING first data-source decision"* —
> is **discharged by `D-035`**. `D-028` itself is still not superseded.


---

## D-029 — Baseline parameters for matched random entry

**Date:** 2026-08-11
**Decision:** Owner delegated these to the agent's judgement, 2026-08-11. Standing
parameters for the D-026 baseline:

| Parameter | Value | Why |
|---|---|---|
| Iterations | **1,000** for any headline result; **200** floor for exploratory runs | 1,000 is cheap and tightens the percentile estimate enough that a borderline result is not an artifact of the draw |
| Random seed | **Recorded in the observation**, every run | Without it the baseline is unreproducible, and an unreproducible control is not a control |
| Eligible entry window | **The same session window the rule under test uses** | Comparing against entries at hours the rule would never fire is a strawman that flatters the rule |
| Direction — primary arm | **Matched to the rule's direction** | Isolates the question actually asked: does the *setup* — timing and location — carry information, given direction? |
| Direction — secondary arm | **Random** (run where feasible) | Answers the different and larger question: is there directional edge at all? The two arms failing differently is diagnostic |
| Stop / target | **Identical to the rule's** | Any difference here changes the payoff geometry and invalidates the comparison |
| Reported | median, 5–95% range, iterations, seed, **and the rule's percentile within the distribution** | A bare "baseline was 55%" hides the spread that determines whether the rule is distinguishable from it |

**Reason:** A control that is not reproducible, or that is drawn from a different
opportunity set than the rule, cannot support or refute anything. The two-arm design
costs almost nothing and separates "the setup adds information" from "trading this
instrument in this session has an edge" — which are routinely conflated.
**Alternatives considered:** Single random-direction arm only — rejected; it conflates
the two questions above. 200 iterations flat — rejected as the headline standard; the
percentile estimate is noticeably noisier at borderline results, which is exactly where
the number matters.
**Consequences:** Every `BT_` observation records iterations, seed, and both arms where
run. `BACKTEST_EVIDENCE_STANDARD.md` §2.1 is amended by this decision where they differ.
**Status:** ACTIVE

---

## D-030 — Blocked tests wait for the course; definitions are never approximated

**Date:** 2026-08-11
**Decision:** Where a testable claim is blocked because the course has named a concept
it has not yet defined — M/W anatomy (`A-011`), "the level" (`A-004`), "trap move"
(`A-002`), TDI (`A-039`), session timezone (`A-019`) — the test **waits for the lesson
that defines it**. No session may substitute an approximation, a plausible reading, a
definition from another trading framework, or a "reasonable" numeric stand-in in order
to make a blocked test runnable. Owner direction, 2026-08-11: *"We have to wait until
those things are taught, which they are in the course, so we have to be patient."*

**Reason:** This is the machine-rule firewall (`D-010`) applied to testing rather than
to notes, and it closes the more dangerous hole. A test run against an invented
definition produces a **number** — and a number in a research corpus acquires authority
that a note never does. Whatever it measures gets attributed to the instructor, and the
substitution is invisible a month later.
**Evidence:** `A-039` already carries this prohibition for TDI specifically
(*"a two-condition version of V04's rule is a different rule with a different hit
rate"*). D-030 generalizes it to every definitional blocker.
**Alternatives considered:** Testing an approximation and labelling it clearly —
rejected. The label degrades faster than the number travels; `E06` + `E18` describe
exactly this failure.
**Consequences:** Manual-backtest debt will keep accruing across lessons, and that is
the correct behaviour, not a backlog to be cleared by lowering the standard. Debt is
tracked in `REVIEW_INDEX.md` and discharges in the lesson that supplies the missing
definition. A test blocked only by a **measurement** gap (tooling, data access) is not
covered here — that is `DEFERRED` under `D-019` and may proceed once the tooling exists.
**Status:** ACTIVE

---

## D-031 — Session timezone is a tested variable, not an assumption

**Date:** 2026-08-11
**Decision:** The chart timezone used to place session windows is **not assumed**. Every
manual backtest that depends on session boundaries runs **two pre-registered arms**, and
**both are always reported**:

| Arm | Definition | Meaning |
|---|---|---|
| **A — fixed offset** | `UTC−5` year-round ("EST", New York, no DST) | His table is a set of fixed clock numbers that never move |
| **B — market-anchored** | `America/New_York` with DST active (i.e. `UTC−4` in summer) | His table tracks the wall clock of the market, shifting with DST |

Owner direction 2026-08-11: treat the timezone as something to test rather than
resolve, defaulting to fixed Eastern and testing the alternative.

**Binding rule — this is the part that matters:** both arms are pre-registered before any
chart is opened, and **both results are reported every time**. Divergence between them is
a **finding**, never a selection criterion. Reporting only the better-performing arm is
`E09` (cherry-picking) and `E24`, and is exactly how a timezone convention gets
"validated" by noise.

**Reason:** `A-019` cannot be closed from source — the instructor explicitly declines to
specify (*"Listen, don't analyse it… These are the times"*, `[00:49:52]`) and says the
person who taught him has died (`[00:49:22]`). An unresolvable ambiguity that materially
moves every session boundary is better converted into a measured variable than into a
guess.

**Arithmetic that must not be lost.** The bootcamp was recorded **2012-03-18 →
2012-06-17**, which lies **entirely within US daylight saving** (2012: Mar 11 – Nov 4).
So New York local clock throughout the course was **EDT (UTC−4)**, not EST (UTC−5):

```text
His "US session starts at 9:30 New York Eastern"  (V01 [00:46:09])
  = 09:30 EDT = 13:30 UTC   during the recording period

Chart on fixed EST (UTC−5)      → that event displays at 08:30   ✗ one hour early
Chart on America/New_York (DST) → that event displays at 09:30   ✓ matches
```

**Arm B therefore reproduces the instructor's own stated numbers during the period he
recorded them; Arm A shifts every one of them by an hour.** This does not settle which
arm the *method* wants — his table may genuinely have been taught as fixed numbers — but
it is a fact about the source and belongs on the record.

**Alternatives considered:** Picking one timezone and proceeding — rejected; a one-hour
error in the Asian window moves the box high/low, which moves the 25–50 pip band, which
changes every observation, invisibly. Deferring the second arm until "if need be" —
rejected; the marginal cost is one shifted harvest of the same data, and deferred
robustness checks reliably become skipped ones.
**Consequences:** `PT-001` and every future session-dependent test carry both arms.
`A-019` remains **OPEN** on the course's side — this decision governs project method, not
what the course teaches, and no session may cite D-031 as evidence of instruction.
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
| ~~Chart data source / broker feed for manual backtesting~~ | ✅ **DECIDED — D-034** (TradingView, FXCM feed; `I-007` closed 2026-08-13) |
| Timezone convention for session and daily boundaries | ⚖️ **CONVERTED — D-031** (tested as two arms, not resolved); `A-019` stays OPEN |
| ~~Default timeframes used in manual study~~ | ✅ **DECIDED — D-034** (15m primary; 1h / 4h / 1D where a test says so) |
| Manual-phase development / holdout boundary | ✅ **DECIDED — D-028** (70/30) · ✅ **PINNED — D-035** (boundary **2016-07-01**) |
| Baseline parameters (iterations, window, direction handling) | ✅ **DECIDED — D-029** |
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

**Status:** **SUPERSEDED IN PART by `D-033`, 2026-08-13.** The normative exclusion — the
entire "EXCLUDED from doctrine" column, and consequences 1 and 2 — is **reversed**. What
survives is consequence 3 (speaker tagging is mandatory) and consequence 4 (identification
is provenance, not evidence), both of which `D-033` re-adopts explicitly. The text above is
retained unedited per this file's append-only rule and per `REMEDIATION_PROTOCOL.md` §2; it
is the record of what the project believed between 2026-08-11 and 2026-08-13 and it is the
reason a large number of records were left open in that period.

---

## D-032 — Guest material may be TESTED, never adopted; a test is not a citation

**Date:** 2026-08-13
**Status:** **SUPERSEDED by `D-033`, 2026-08-13 (same day).** `D-032` was the narrow opening —
guest material may be *measured* but not *adopted*. `D-033` removes the distinction it was
built on by granting guest material full normative authority, so the "still forbidden" column
below no longer binds. **`PT-022`/`PT-023`/`PT-024` and `BT_V06_0001` are not withdrawn and
not re-scoped**: work performed under a narrower fence remains valid under a wider one, and
their mandatory scope statements are now *historical* rather than binding. Retained unedited.
The original status line follows.

**Original status:** **PROVISIONAL — OWNER RATIFICATION REQUESTED.** Written by the session that was
directed to act on it, so the direction is on the record rather than living only in a chat
session (`D-001`, and the `D-023` failure this avoids repeating). If the owner disagrees with
any clause, this entry is superseded and `PT-022` and its observations are marked
`WITHDRAWN — SCOPE`, not deleted.

**Refines:** `D-025`, which remains `ACTIVE` and is **not superseded**.

**Owner direction, 2026-08-13, in substance:** V06 is to receive *"a genuine manual backtest…
pre-register a testable prediction/rule from V06's lecture content BEFORE looking at outcome
data, then manually backtest it against real historical market data… and record the result
honestly whether it confirms or contradicts the rule as taught."*

**Decision:** Guest-presenter material may be **empirically tested** under the pre-registered
discipline, provided every one of the following holds. Testing is not adoption, and a measured
result about a guest's claim is not a claim about the method.

| Permitted | Still forbidden, unchanged from `D-025` |
|---|---|
| Pre-registering a guest claim as a hypothesis and measuring it | Entering the claim, or any result about it, into `12_MASTER_SPEC/`, `13_MACHINE_SPEC/`, `08_CONCEPT_LIBRARY/` or any machine candidate |
| Reporting the result, confirming or contradicting, with equal prominence | Citing the result **for or against** any instructor statement |
| Recording the observation in `06_MANUAL_BACKTEST/` under a `PT-NNN` file | **Closing** any `A-xxx` or `C-xxx` record on it |
| Using **instructor-sourced** objects (e.g. V02's printed session table) to operationalise the test | Merging the guest's rule with an instructor rule into one rule set |
| | Treating a confirmation as evidence the **method** works |

**Three constraints that are part of this decision, not commentary:**

1. **`D-030` is untouched and binds harder here than anywhere.** A guest claim that requires a
   concept the course has named and not defined — *push*, *pullback*, *nameable pattern*, ADR's
   lookback — **remains untestable**. Only claims decidable from measurements may be tested.
   The value of this decision is exactly that it does **not** create a route around `D-030`.
2. **A guest test carries a mandatory scope statement** on every report of it, in the form
   `PT-001` §7 establishes, naming the speaker, the exclusion, and what the result does **not**
   license.
3. **A confirmed guest claim does not become a rule.** It becomes a *measured fact about a
   claim a coach made*. The distinction is the whole content of this entry, and a future session
   that loses it has lost `D-025`.

**Reason:** `D-025` was written to stop guest material becoming doctrine, and it does. What it
did not contemplate is whether guest material may be **measured**. Reading it as a bar on
measurement has a perverse consequence: the corpus would record the most mechanically complete
system it contains as untested **forever**, while the project's own standard
(`BACKTEST_EVIDENCE_STANDARD.md` §4.3) requires that every testable claim examined be reported.
Testing a claim and refusing to adopt it are compatible; indeed a **contradicted** guest claim
is the strongest possible support for `D-025` having excluded it.

**Evidence:** `DECISIONS.md` `D-025`, `D-030`; `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-001` §7
(the scope-statement form); `COMMON_PROTOCOL.md` §8 (which reads V05/V06 as contributing
nothing — that reading is **narrowed by this entry to the normative half only**, and
`COMMON_PROTOCOL.md` governs `PT-002…PT-021`, which are unaffected). Project owner direction,
2026-08-13.

**Alternatives considered:** *Reading `D-025` as barring measurement, and declining the
direction* — rejected; the decision's own text bars adoption, citation and closure, none of
which a fenced test performs, and the owner is the authority on scope. *Testing the guest's
full push rule* — rejected outright under `D-030`: *push*, *pullback* and *nameable pattern*
are undefined, and a test of an approximated definition produces a number that outlives its
caveat. *Recording nothing and simply running the test* — rejected; that is the `D-023` failure,
where an authorized action lived only in a conversation and read afterwards as a violation.

**Consequences:** `PT-022` is written under this entry and cites it. `PRE_REGISTERED/INDEX.md`'s
coverage table, which reads *"V06 — none — `D-025`"*, is updated with the reason for the change
rather than silently corrected. **`PT-002`…`PT-021` are unaffected**: none of them draws on V05
or V06 and none is re-scoped here. If the owner declines to ratify, `PT-022` and its
observations are marked `WITHDRAWN — SCOPE` and retained.

---

## D-033 — Guest-presenter material is NORMATIVE evidence on equal footing with the course author

**Date:** 2026-08-13
**Supersedes:** `D-025` **in part** (the normative exclusion, and consequences 1 and 2) and
`D-032` **in whole** (the test-but-never-adopt fence, which this entry makes unnecessary).
Neither is deleted; both are marked in place and retained unedited.
**Does NOT supersede:** `D-030` (definitions are never approximated), `D-010` (machine-rule
firewall), `D-008` (course evidence outranks agent interpretation), `D-009`, `D-026`–`D-029`,
`D-031`. See the "What this decision does not do" block below — it is the load-bearing half.

**Owner direction, 2026-08-13:** guest-presented content is to be treated as **equal in
authority to main-host content** — *"all knowledge is created equal."* Guest material is not
to be demoted.

**Decision:** Material delivered by any speaker inside a course lesson — the course author, a
guest presenter, a coach, an invited student — is **admissible as NORMATIVE evidence at equal
weight**. Specifically, guest material:

| May now | Previously, under `D-025` |
|---|---|
| Define rules, gates, filters, thresholds, stops, targets, sessions, watchlists | Excluded from doctrine entirely |
| Enter `12_MASTER_SPEC/`, `13_MACHINE_SPEC/`, `08_CONCEPT_LIBRARY/` and machine candidates | Barred from all four |
| **CLOSE or RESOLVE** an `A-xxx` or `C-xxx` record on its own | Could `EXTEND` only, never close |
| Be cited **for or against** any other statement in the corpus | Barred both ways |
| Be adopted, not merely tested (`D-032`'s distinction dissolves) | Testable at most, from `D-032` onward |
| Be graded on all ten mastery dimensions like any other lesson | Dimensions withheld "by decision" |

**Three provisions of `D-025` are re-adopted verbatim and remain binding**, because none of
them demotes anything — they are provenance hygiene, and the reversal does not touch them:

1. **Speaker tagging stays MANDATORY** (`D-025` consequence 3) — transcript header speaker
   table, speaker tag on every source-note row, established *before* notes are written. Equal
   authority is not anonymity: the corpus must still record **who said what**, because two
   speakers can now both create doctrine and a future contradiction between them has to be
   attributable.
2. **Identifying a guest is provenance, not evidence** (`D-025` consequence 4). Nothing may
   depend on the identification being right.
3. **A guest/instructor divergence is now a real contradiction and IS logged as one.** This
   inverts `D-025` consequence 2 rather than re-adopting it: with equal authority, two
   speakers stating incompatible rules is a genuine `C-xxx` conflict in the method, not a
   corpus-hygiene note. `C-005` is affected — see the consequences below.

### What this decision does NOT do — read this before citing it

- **`D-030` is untouched and still binds.** A claim that needs a concept the course has named
  and never defined — *push*, *pullback*, *nameable pattern*, "the level" (`A-004`), M/W
  anatomy (`A-011`), the second leg (`A-007`), TDI (`A-039`), ADR's lookback — **remains
  untestable and uncodable no matter who said it.** Equal speaker authority changes *whose*
  statements count; it does not supply a missing definition. **A session that reads `D-033` as
  unblocking the `D-030` list has misread it.** Concretely: V06 dimension **B (Recognition)**
  is blocked because *push* is undefined, and it stays blocked.
- **It is not retroactive re-grading.** No mastery grade, review verdict or gate state changes
  by operation of this entry. Where a dimension or a record was blocked by `D-025`, the
  blocking condition is recorded as **CHANGED**, and re-assessment is the independent
  reviewer's job under `D-003`/`D-004`, not the job of the session that wrote this decision.
- **It does not make guest material *outrank* anything.** Equal is equal. `D-008` still ranks
  course evidence above agent interpretation, and no speaker's statement acquires priority
  over another's by seniority, runtime share, or how well it fits an existing artifact.

**Reason:** The owner is the authority on the corpus's scope, and this is the owner's ruling.
The recorded cost of `D-025` supports it. Two consecutive lessons (V05, V06) carry **zero
course-author runtime**; V06 states the most nearly complete trading system anywhere in
V01–V06 — trigger, filter, location rule, counting rule, stop, target, time stop, exit — and
`D-025` excluded all of it, producing a lesson that yielded *"zero doctrine"* by its own
mastery report. `D-032` was already an admission that the exclusion had over-reached, and it
bought a narrow measurement carve-out at the price of a distinction ("a confirmed claim is a
measured fact about a claim a coach made, not a rule") that every future session would have
had to keep straight. Removing the demotion removes that maintenance burden entirely.

**Evidence:** Owner direction, 2026-08-13. `DECISIONS.md` `D-025`, `D-032`.
`07_MASTERY_REPORTS/V05_MASTERY_REPORT.md` §F/§G and its Escalation (V05's `D-018`/`D-019`
disposition problem exists **only** because of the exclusion);
`07_MASTERY_REPORTS/V06_MASTERY_REPORT.md` `STUDENT STATUS: REVIEW REQUIRED`;
`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` STATUS block (*"It CLOSED none, and under D-025 it
cannot"*); `11_CONTRADICTIONS/CONTRADICTIONS.md` C-005;
`06_MANUAL_BACKTEST/PRE_REGISTERED/INDEX.md` §2 (*"V05 — none — `D-025`"*);
`06_MANUAL_BACKTEST/PRE_REGISTERED/COMMON_PROTOCOL.md` §8.

**Alternatives considered:** *Leaving `D-025` in force and widening `D-032` further* —
rejected; the owner's direction is about authority, not about measurement, and stacking a
third carve-out on a rule the owner has reversed would leave the corpus governed by a
distinction nobody wants. *Superseding `D-030` alongside it, on the reading that it is "a
related guest ruling"* — **rejected on the facts**: `D-030` names no speaker and applies to
instructor material identically (`A-004`, `A-011`, `A-019` are all instructor terms). It is
the machine-rule firewall applied to testing, and reversing it would license invented
definitions across the whole corpus, which no part of the owner's direction asks for. Flagged
to the owner rather than assumed either way. *Deleting `D-025` and `D-032`* — rejected;
append-only is `D-001`'s discipline and `REMEDIATION_PROTOCOL.md` §2's requirement, and the
period during which the exclusion was in force explains the shape of a dozen artifacts.

**Consequences:**

- **`D-025`** marked `SUPERSEDED IN PART`; **`D-032`** marked `SUPERSEDED`. Both retained
  unedited. `PT-022`/`PT-023`/`PT-024` and `BT_V06_0001.md` stand as run; their mandatory
  `D-032` scope statements become historical annotations, not live constraints.
- **`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`** — the standing bar on closing a record with
  guest evidence is lifted. Records left open *solely* on that ground are flagged
  `CLOSURE UNBLOCKED BY D-033 — RE-ASSESS` in the STATUS block. **No record is closed by this
  decision**; each still needs the ordinary evidentiary judgement, in a session that does the
  reading. `A-043`'s narrow platform-artifact closure needs no special justification any more.
- **`11_CONTRADICTIONS/CONTRADICTIONS.md`** — `C-005` changes category: a guest/instructor
  divergence is now a method-level conflict. `C-005` is **not** re-adjudicated here; it is
  flagged for the reviewer.
- **`18_REVIEW/REVIEW_INDEX.md` open item 40** — the proposed `D-025` carve-out for records
  whose subject is a guest's own utterance or a platform artifact is **MOOT**: it was an
  exception to a bar that no longer exists.
- **`COMMON_PROTOCOL.md` §8** and **`PRE_REGISTERED/INDEX.md` §2** are corrected in place with
  the superseded reading retained above the change, as `D-032`'s own edit did.
- **V05 and V06 mastery reports** gain a `D-033` note recording that the blocking condition has
  changed. **Neither is re-graded here.** Authoring V05/V06-derived test cases for the GBP/USD
  suite is follow-up work, not this session's.
- **Speaker tagging remains a gate item for every V07–V21 lesson.**

**Status:** ACTIVE

---

## D-034 — The GBP/USD chart data source is declared: TradingView, FXCM feed (closes `I-007`)

**Date:** 2026-08-13
**Closes:** `SETUP_ISSUES.md` `I-007` (open since 2026-08-10).
**Governs:** every manual backtest under `D-005`/`D-026`/`D-027`, and
`06_MANUAL_BACKTEST/PRE_REGISTERED/COMMON_PROTOCOL.md` §1 and §6.

**Decision:** The **standing** chart data source for the manual phase is the convention
already in unbroken use across V02–V06 homework, declared here rather than invented:

| Field | Value |
|---|---|
| Platform | **TradingView** |
| Feed | **FXCM** (`FX:GBPUSD`) |
| Access | **No login, no account, no paywalled feature.** No CAPTCHA is encountered or bypassed |
| Measurement | **Platform text only** — `Date`, `Time`, `Open`, `High`, `Low`, `Close` read together from the Data Window / OHLC legend DOM. **No price is ever read from a pixel** (`COMMON_PROTOCOL.md` §2) |
| Reference harvester | `05_HOMEWORK/V05/scripts/tv_harvest_v05.mjs` — each bar carries its own timestamp, so no boundary is inferred from bar cadence |
| Chart timezone | **Recorded explicitly per harvest, never assumed.** The chart clock is an input to `D-031`'s two arms, not a detail |
| Timeframes | 15-minute primary; 1-hour, 4-hour and 1-day where a test says so |
| Second vendor | **Yahoo Finance chart API** (`query1.finance.yahoo.com/v8/finance/chart/`) is the **corroboration** source only — used to cross-check the primary, as in `05_HOMEWORK/V06/scripts/crosscheck_second_source.py` and `PT-024`. It is not a substitute primary, and a test that runs on it says so in its own file |

**The convention was verified, not assumed.** Every homework file in the corpus that opened a
chart names the same platform and the same feed:

| Lesson | Declared source |
|---|---|
| V02 | TradingView, FXCM feed, 1-hour, no account |
| V03 | TradingView, FXCM feed, 4-hour, no account, no login |
| V04 | TradingView, **FXCM**, 4-hour and 15-minute, no login |
| V05 | TradingView, **FXCM**, 15-minute, no login |
| V06 | TradingView, **FXCM**, 15-minute and 1-day, no login |

V01's homework is `DEFERRED` (H4/H5, blocked by `I-007` itself) and opened no chart, so it is
silent rather than inconsistent. **There is no competing feed anywhere in V01–V06.** Yahoo
appears once, in V06, and is explicitly framed there as a second source for cross-checking.

**Two vendor-dependent facts that this decision carries forward as known, not as surprises:**

1. **The FX week open is vendor-dependent.** FXCM opens the week at **21:00 UTC**; Yahoo at
   **23:00 UTC**; both consistently, week after week (`V06_HOMEWORK.md` §4, cross-check
   script). *"480 bars in a trading week"* is therefore a fact about the FXCM feed's session
   definition, not about the market. **Every week-boundary test (`W-C`, `PT-008`–`PT-013`)
   inherits FXCM's 21:00 UTC week open** and must state it.
2. **Quotes differ by a small constant offset between vendors** — Yahoo minus FXCM measured at
   **+3.11 pips on highs, +3.94 pips on lows** (`V06_HOMEWORK.md` §4). A cross-vendor
   comparison is a corroboration of *shape*, not of *level*.

**A MANDATORY depth probe, because declaring a feed does not make history appear.**
Before any window is opened at a given timeframe, the running session performs and records a
**history-depth probe** at that timeframe — walking the chart back until the left-edge date
stops moving, **reading dates only, never OHLC** — and records the earliest served timestamp
in the observation. The reference implementation is `PT-023`'s `probe_back.mjs` (368 drags).

> **The probe already on record, and it is bad news for `PT-002`…`PT-021`.** Measured
> 2026-08-13: **TradingView/FXCM serves 15-minute GBP/USD back to 2026-05-31 and no further** —
> about **2.5 months**. `COMMON_PROTOCOL.md` §3's windows **W-A (2015)**, **W-B (2014–15)** and
> **W-C (2013–17)** are therefore **out of reach at 15-minute resolution on the declared feed.**
> This is why `PT-022` was superseded `PERIOD UNOBTAINABLE`.
>
> **Closing `I-007` does not by itself unblock `PT-002`…`PT-021`.** It removes the *declaration*
> blocker. A **data-availability** blocker remains, and it is a different thing — a measurement
> gap under `D-019`, not a definitional one under `D-030`. See `D-035` and the follow-up item
> recorded there.

**Reason:** `I-007` has blocked the manual phase since 2026-08-10 and has already forced two
test re-issues. The project does not need a *new* source; it needs the one it has been using
for five lessons to be written down as binding. Declaring the de facto standard costs nothing,
invents nothing, and makes every prior homework retroactively conformant rather than
retroactively irregular.
**Evidence:** `05_HOMEWORK/V02…V06/*_HOMEWORK.md` header tables (quoted above);
`05_HOMEWORK/V05/scripts/tv_harvest_v05.mjs`; `05_HOMEWORK/V06/scripts/crosscheck_second_source.py`
and `05_HOMEWORK/V06/data/crosscheck_second_source_output.txt`;
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-023` §1 (the depth probe);
`18_REVIEW/V02/V02_REVIEW_R1.md` (the `E06`/`E19` pixel-read `MAJOR` that produced the
text-only rule); `00_SYSTEM/SETUP_ISSUES.md` `I-007`.
**Alternatives considered:** *Declaring a paid deep-history vendor that reaches 2013* —
rejected **here**, not on the merits but on authority and evidence: no such feed has ever been
used in this project, choosing one is a cost and account decision that belongs to the owner,
and `I-007`'s own text says the decision must be recorded before observations are collected,
not guessed by a session. Recorded as the open follow-up in `D-035`. *Declaring Yahoo as
primary because its daily history is deeper* — rejected; it has been used exactly once, as a
cross-check, and promoting the corroboration source to primary would invalidate the
comparison that makes it useful. *Leaving `I-007` open until a deep-history feed exists* —
rejected; that conflates two separable blockers and leaves five lessons of chart work
formally unsourced.
**Consequences:** `COMMON_PROTOCOL.md` §1 ("Data source — UNDECLARED") and §6 (the `I-007`
row) are updated. `SETUP_ISSUES.md` `I-007` moves to `RESOLVED — D-034`, appended not deleted.
The `DECISIONS TO BE MADE AT INGESTION` table's *"Chart data source / broker feed"* and
*"Default timeframes used in manual study"* rows are marked decided. Every future `BT_` and
`PT_` file states platform, feed, chart timezone and the depth probe for its timeframe.
**Status:** ACTIVE

---

## D-035 — The project-wide `D-028` 70/30 boundary is pinned at 2016-07-01

**Date:** 2026-08-13
**Executes:** `D-028`, which fixes the 70/30 ratio and requires *"the first session to
establish the data source"* to compute and record the concrete dates. `D-034` establishes the
data source; this entry does the arithmetic. **`D-028` is not superseded** — its meaning is
unchanged and this is the append it asks for, recorded as its own entry because it is a
project-wide pin rather than the per-series scoped pins already appended under `D-028`.

**Decision:** The manual-phase GBP/USD corpus is the **union of the three pre-registered
windows** in `COMMON_PROTOCOL.md` §3 — `W-A` (2015), `W-B` (2014-01-05 → 2015-12-31) and
`W-C` (2013-01-06 → 2017-12-29) — i.e. **2013-01-06 → 2017-12-29**, 1,818 days. Split by
time at the oldest 70%:

| Block | Range | Days | Rule |
|---|---|---|---|
| **DEVELOPMENT** | **2013-01-06 → 2016-06-30** | 1,272 | Open freely during the Student Phase |
| **HOLDOUT** | **2016-07-01 → 2017-12-29** | 546 | **Not opened by any session, for any reason, during the Student Phase** (`D-027`, `D-028`) |

`B = T0 + 0.70 × (T1 − T0)` = `2013-01-06 + 1,272 days` = **2016-07-01**, rounded down to the
start of a calendar day, matching the rule `PT-023` §2 pre-registered. The corpus boundaries
were chosen on **calendar grounds before any chart was opened** (`COMMON_PROTOCOL.md` §3
attestation) and this arithmetic reads no price, so the pin is not outcome-informed.

**Three consequences that must not be discovered later:**

1. **`W-A` and `W-B` lie wholly inside DEVELOPMENT.** ✅ `PT-002`…`PT-007`, `PT-014`–`PT-018`,
   `PT-020`, `PT-021` and `PT-001` conform on the boundary test.
2. **`W-C` STRADDLES the boundary** — it runs to 2017-12-29, 546 days into HOLDOUT.
   ⚠ **`PT-008`, `PT-009`, `PT-010`, `PT-011`, `PT-012`, `PT-013` and `PT-019` do not conform.**
   Per `COMMON_PROTOCOL.md` §3a and `D-027`, each must be **re-issued under a new `PT` number**
   with a window inside DEVELOPMENT — the natural one being `W-C′ = 2013-01-06 → 2016-06-30`
   (~180 weeks, still comfortably over `n ≥ 30`). **The originals are retained and marked, not
   edited into conformance.** This session does not re-issue them; it records the defect.
3. **The 2016 events split across the boundary.** The EU referendum (2016-06-23) falls in
   **DEVELOPMENT**, one week before the boundary; the October flash crash (2016-10-07) falls in
   **HOLDOUT** and is therefore **not** available to the Student Phase at all. This is a
   consequence of a ratio fixed on 2026-08-11, not a choice made about those events, and
   `COMMON_PROTOCOL.md` §3 disclosure 1 (the sensitivity appendix) applies to whatever remains.

> **THE REMAINING BLOCKER, STATED PLAINLY.** `I-007` is closed (`D-034`) and the `D-028`
> boundary is pinned (this entry). **`PT-002`…`PT-021` still cannot run**, for a third and
> different reason: **the declared feed does not serve the data.** TradingView/FXCM reaches
> back **2.5 months** at 15 minutes; `W-A`/`W-B`/`W-C′` are 2013–2016. That is a **measurement
> blocker** (`D-019` `DEFERRED`), not a definitional one (`D-030`), and it has exactly three
> honest exits, all of which are **the owner's to choose**:
>
> | Option | What it costs |
> |---|---|
> | **A — a deep-history vendor** for the manual phase (a paid TradingView tier, a broker MT4/MT5 account with 2013 tick/minute history, or a bulk-download source), declared as an amendment to `D-034` | Money and/or an account; the `E06` text-only measurement rule must survive the change of tool |
> | **B — re-issue the batch onto reachable windows** under new `PT` numbers, on the ~2.5 months the feed serves | Guts the design: `n` collapses for weekly-structure tests, and `COMMON_PROTOCOL.md` §3's "proximity to the 2012 regime" rationale is lost entirely |
> | **C — split by timeframe**: run the daily-resolution tests (`PT-010`, `PT-012`, `PT-019`, parts of `PT-008`/`PT-013`) on whatever daily depth a probe shows the feed serves, and hold the 15-minute tests for option A | Requires a **daily-timeframe depth probe** (`D-034`), which no session has run. Cheapest next step and it is diagnostic either way |
>
> **No option is chosen here.** `D-030`'s discipline — wait rather than approximate — is the
> project's standing answer to a blocker, and inventing a data source the project has never
> used is the exact failure `I-007` was written to prevent. **Recorded as an open owner
> decision.**

**Reason:** `D-028` has carried *"boundary dates PENDING first data-source decision"* since
2026-08-11 and the two boundaries appended to it since are **scoped** to single vendor/timeframe
series, explicitly *"not the project-wide split"*. With `D-034` declaring the standing source,
the project-wide pin is owed. Pinning it against the pre-registered windows rather than against
one vendor's served depth is what makes it stable: the windows were fixed on calendar grounds
before any chart existed, so the split cannot be re-cut by a later change of feed.
**Evidence:** `DECISIONS.md` `D-027`, `D-028` (and its 2026-08-13 scoped append), `D-034`;
`06_MANUAL_BACKTEST/PRE_REGISTERED/COMMON_PROTOCOL.md` §3, §3a;
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-023` §1–§2 (the depth probe and the boundary rule).
**Alternatives considered:** *Pinning the boundary so that `W-C` fits wholly inside
DEVELOPMENT* — **rejected, and this is the important one**: it would mean choosing the split
to suit the tests, which is the selection pressure `D-027` and `D-028` exist to remove.
Better to report seven non-conforming tests than to move a holdout to accommodate them.
*Pinning against the feed's served depth (2026-05-31 → today)* — rejected; that is the scoped
per-series pin already appended to `D-028`, and it is not a project-wide split. *Leaving the
project-wide boundary unpinned until a deep-history feed is chosen* — rejected; the boundary
is computable from windows fixed before any chart was opened, and pinning it now is strictly
safer than pinning it after someone has seen 2013 data.
**Consequences:** `COMMON_PROTOCOL.md` §3a's `PROVISIONAL — PENDING D-028` marking is
resolved for `W-A`/`W-B` and converted into a **re-issue obligation** for the seven `W-C`
tests. `PRE_REGISTERED/INDEX.md`'s gate block is updated. `validate_project.py` may now check
observation dates against 2016-07-01. Opening the holdout remains `E23` and converts it
permanently into development data, which must be **disclosed**.
**Status:** ACTIVE — the split is final; the data-availability exit (A / B / C above) is an
**OPEN OWNER DECISION**

> ### APPENDED 2026-08-13 — THE CONFORMANCE TABLE ABOVE IS DEFECTIVE IN ONE ROW: `PT-002`
>
> Consequence 1 lists **`PT-002`** among the tests that *"conform on the boundary test"*. **It
> does not.** `PT-002` §3 pre-registers **two** windows — *"**W-A** (2015-01-04 → 2015-12-31)
> for daily extremes; **W-C** (2013-01-06 → 2017-12-29) for weekly extremes"* — and
> `PRE_REGISTERED/INDEX.md` §1 has recorded it as *"W-A, W-C"* since the batch was written. Its
> **`W-C` arm straddles this boundary by the same 546 days** as the seven named in consequence 2.
> The classification error was to file the test by its **first** window.
>
> **The corrected count is EIGHT, not seven**: `PT-002` (W-C arm), `PT-008`, `PT-009`, `PT-010`,
> `PT-011`, `PT-012`, `PT-013`, `PT-019`.
>
> **Nothing else in this entry changes.** The 2016-07-01 pin, the 1,272 / 546-day arithmetic, the
> `W-A`/`W-B` verdicts, the event split and the rejection of *"pinning the boundary so that W-C
> fits wholly inside DEVELOPMENT"* are all unaffected. The defective row is **retained above**
> rather than corrected away, because it is what the re-issue session worked against.
>
> **`PT-002` is marked PARTIALLY non-conforming, not superseded**: its `W-A` daily arm conforms,
> is unblocked by `D-036a`, and stays runnable in `PT-002` itself. Only its weekly arm is
> re-issued, as **`PT-025`**.
>
> The obligation this entry created is **discharged by `D-037`**, which re-issues all eight onto
> `W-C′` = 2013-01-06 → 2016-06-30 as `PT-025` … `PT-032`.

---

## D-036 — A paid TradingView tier is ruled out as a `D-035` option-A exit; only an import-capable platform reaches the windows

**Date:** 2026-08-13
**Narrows:** `D-035` option **A** ("a deep-history vendor … a paid TradingView tier, a broker
MT4/MT5 account with 2013 tick/minute history, or a bulk-download source"). `D-035`'s three-way
owner decision **remains open**; this entry removes one candidate from inside option A and
states what the surviving candidates actually require.
**Amends nothing in `D-034`.** TradingView/FXCM remains the declared standing source until an
owner decision amends it.

**Decision:** **Buying a higher TradingView tier for its larger bar allowance does not solve
the `PT-002`…`PT-021` data-availability blocker, and is recorded here as rejected on
arithmetic rather than on cost.** The only candidates inside option A that reach `W-A`, `W-B`
or `W-C′` are platforms that accept an **imported** third-party history file — in practice
MetaTrader 4/5 fed from a bulk-download source — or a paid vendor whose *served depth*, not
whose *bar allowance*, reaches 2013.

**The arithmetic, and it is not close.** At 15 minutes the declared feed's session definition
(`D-034` fact 1) gives **96 bars/day × 5 days = 480 bars/week**. Counting back from
2026-08-13 to the START of each pre-registered window:

| Window | Start | Days back | Weeks | 15-min bars required |
|---|---|---|---|---|
| **W-A** | 2015-01-04 | 4,239 | 605.6 | **≈ 291,000** |
| **W-B** | 2014-01-05 | 4,603 | 657.6 | **≈ 316,000** |
| **W-C** / **W-C′** *(same start)* | 2013-01-06 | 4,967 | 709.6 | **≈ 341,000** |

Holidays trim ~1–2% and are immaterial at this magnitude. Against that requirement:

| Option under consideration | Bars | Reaches back to | W-A | W-B | W-C′ |
|---|---|---|---|---|---|
| **Current TradingView plan** | 10,000 | ≈ 2026-03-20 (≈ 21 weeks) | ❌ | ❌ | ❌ |
| **Upgraded TradingView plan** | 20,000 | ≈ 2025-10-25 (≈ 42 weeks) | ❌ | ❌ | ❌ |
| **MetaTrader 4/5 — broker server history only** | broker-set | broker-dependent, commonly ≥ 2020 | ⚠ | ⚠ | ⚠ |
| **MetaTrader 4/5 — third-party history imported** | unbounded in practice | 2000 (HistData) / 15+ yrs (Dukascopy) | ✅ | ✅ | ✅ |

**Doubling the bar allowance closes ≈ 6% of the gap.** 20,000 bars buys about **ten months**
of 15-minute history against a shortfall of **11.6 years** at the shallowest window. There is
no TradingView tier in the 10k/20k family that changes the verdict, because the shortfall is
two orders of magnitude, not a factor of two.

**A second fact that must not be missed: the bar cap is not currently the binding constraint.**
`PT-023` §1's depth probe found the feed itself stopping at **2026-05-31 ≈ 5,074 bars** —
**shallower than the 10,000 bars the current plan already permits**. The limit being hit today
is the FXCM feed's served depth, not the plan's allowance. An unlimited-bar plan on the same
feed would return the same 2026-05-31 left edge. **Any option-A candidate must therefore be
evaluated on served depth, and a bar-allowance number is not evidence of depth.**

**What MetaTrader actually offers, sourced rather than assumed:**

1. **MetaTrader imposes no meaningful bar-count ceiling.** `Max bars in history` and
   `Max bars in chart` accept up to 2,147,483,647, and the chart setting can be set to
   *Unlimited* (Tools → Options → Charts). MT5 stores **M1** and derives every intraday
   timeframe from it, so **M15 depth equals M1 depth on that server**.
2. **Depth is set by the broker, and brokers have been trimming it.** IC Markets published
   that from **2022-06-10 pre-2020 history is no longer served to client trade accounts**;
   Darwinex publishes tick data **from October 2017**; demo and live accounts on the same
   broker frequently differ. **Opening an MT5 account and hoping for 2013 is not a plan** —
   it is a second depth probe with an account attached.
3. **The reliable path is import, not download.** MT4/MT5's History Center accepts CSV import
   per timeframe. **HistData.com** publishes free GBP/USD **M1 bars in native MT4/MT5 format,
   by pair/year/month, back to 2000**; **Dukascopy's Historical Data Export** publishes free
   tick-through-monthly CSV going back 15+ years. Either covers 2013–2016 at the required
   resolution outright.

> **THE CONSEQUENCE THAT IS NOT FREE, AND IT IS THE REASON THIS IS NOT A DECISION TO ADOPT.**
> Importing HistData or Dukascopy files makes **the bulk vendor the data source**, not FXCM.
> That is an **amendment to `D-034`**, and it moves two vendor-dependent facts that `D-034`
> carries forward as known:
>
> - **The 21:00 UTC week open is an FXCM fact.** `W-C` and `PT-008`–`PT-013` inherit it by name
>   (`D-034` fact 1, `COMMON_PROTOCOL.md` §6). A different vendor has a different week open,
>   which must be **re-measured and re-stated**, not carried over.
> - **Quote levels differ by a small constant between vendors** (`D-034` fact 2). A window
>   harvested from an imported file is not level-comparable with V02–V06 homework.
>
> Further, `E06`'s **text-only measurement rule** (`COMMON_PROTOCOL.md` §2) was written against
> a DOM-readable chart. It must be restated for a CSV-fed platform before a single bar is read
> — reading a value from an imported file is *more* auditable than a DOM read, not less, but
> the rule has to say so in writing first.

**Reason:** `D-035` left option A as a single line naming three dissimilar candidates, and the
owner asked which of the concrete ones actually work before spending money. Two of them —
10,000 and 20,000 bars — are answerable by arithmetic alone, cost nothing to check, and are
**both wrong by a factor of ~15 to ~34**. Recording that here prevents a purchase that would
close 6% of a gap, and prevents the same calculation being redone by a later session.
**Evidence:** `COMMON_PROTOCOL.md` §3 (window definitions `W-A`/`W-B`/`W-C`), §3a (`W-C′`),
§6 (the data-availability blocker row); `PT-002`…`PT-021` window declarations, read file by
file and confirmed against §3; `D-034` (480 bars/week as an FXCM session fact; the mandatory
depth probe; the two vendor-dependent facts); `D-035` options A/B/C; `PT-023` §1 (the
2026-05-31 left edge, 368 drags). MetaTrader depth claims:
[MetaTrader 5 Help — how the tester downloads historical data](https://www.metatrader5.com/en/terminal/help/algotrading/test_preparation);
[Myforex MT4/MT5 download-historical-data guide](https://myforex.com/en/mt5guide/download-historicaldata.html);
[IC Markets notice regarding client historical data](https://www.icmarkets.com/blog/notice-regarding-client-historical-data/);
[Darwinex tick data](https://www.darwinex.com/tick-data);
[HistData.com free forex data](https://www.histdata.com/download-free-forex-data/);
[Dukascopy Historical Data Export](https://www.dukascopy.com/swiss/english/marketwatch/historical/).
**Alternatives considered:** *Recording the upgrade as "probably insufficient" and leaving it
open* — rejected; the shortfall is arithmetic, not judgement, and an open item invites the
purchase. *Declaring HistData or Dukascopy as the new primary source in this entry* — rejected
on the same authority grounds `D-034` used: choosing a source is the owner's decision, the
week-open and level facts above must be re-measured before any such declaration, and no session
should amend `D-034` by side-effect of a feasibility check. *Treating "MetaTrader" as a single
option* — rejected; broker-served history and imported history have opposite verdicts, and
collapsing them would have recorded a ⚠ where the honest answer is one ❌ and one ✅.
*Recommending option C's daily-timeframe probe here* — declined as out of scope; it remains
`D-035`'s cheapest next step and is untouched by this entry.
**Consequences:** `D-035` option A is narrowed: **"a paid TradingView tier" is struck**, and
the surviving candidates are (i) an import-capable platform fed from a bulk vendor, or (ii) a
paid vendor evidenced by a **served-depth probe**, never by a bar allowance. `D-034`'s
mandatory depth probe is reaffirmed as the acceptance test for any candidate feed. No window
moves, no `PT` file is edited, no test is unblocked, and the seven `W-C` re-issues owed under
`D-035` are still owed regardless of which source wins. If the owner picks an import path, that
is a **new decision amending `D-034`**, and it must restate the week open, the level offset and
the `E06` measurement rule for the new tool before any observation is collected.
**Status:** ACTIVE — advisory to the still-**OPEN OWNER DECISION** in `D-035`

---

## D-036a — `D-035` option A is TAKEN: the historical windows are sourced from a HistData CSV corpus, amending `D-034`

**Date:** 2026-08-13
**Owner decision, given in session:** *"Let's just go with csv for now… Make the csv the
priority… We need to verify what the tests call for."*
**Amends:** `D-034`, **for the pre-registered historical windows only**.
**Resolves:** the data-availability blocker recorded in `D-034`, `D-035` and
`COMMON_PROTOCOL.md` §6 — the one that has stopped `PT-002`…`PT-021` since 2026-08-13.
**Numbered `D-036a` rather than `D-037`** because it executes the option `D-036` narrowed;
it is not an independent decision and must never be cited apart from `D-036`.

**Decision:** For `W-A`, `W-B` and `W-C′`, the data source is a **HistData.com GBP/USD
M1 CSV corpus**, aggregated locally to 15 minutes. `D-034` is **not revoked** — TradingView
/ FXCM remains the standing source for recent and live chart work, and for every homework
already recorded against it. What changes is that a window the declared feed cannot reach
is now sourced from a vendor that can.

| Field | Value |
|---|---|
| Source | **HistData.com**, free tier, no account, no login |
| Product | `MetaTrader` format, **M1 (1-minute) bid bars** — the finest the vendor publishes |
| Instrument | GBP/USD (`D-007`) |
| Files | `DAT_MT_GBPUSD_M1_{2013,2014,2015}.csv` + `DAT_MT_GBPUSD_M1_2016H1.csv` |
| Retrieved | **2026-08-13**, by HTTP POST to the vendor's public `get.php` form endpoint |
| Integrity | **SHA-256 recorded** per file in `datasets/HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt` |
| Span | **2013-01-01 17:00 → 2016-06-30 23:59**, **1,297,781** M1 bars |
| Timezone | **Fixed UTC−5 ("EST"), no DST** — vendor spec, and measured (below) |
| Column format | `YYYY.MM.DD,HH:MM,O,H,L,C,V` |
| Volume | **Structurally zero** in this vendor's data. Carried for format compatibility; **it is not traded volume and no test may read it** |
| Derived | `GBPUSD_M15_ARMA.csv`, `GBPUSD_M15_ARMB.csv` — 86,824 bars each, built by `06_MANUAL_BACKTEST/scripts/aggregate_m15.py` |
| Location | `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/` — **gitignored bulk data**, provenance committed, per that directory's standing README rule |

**Window coverage, verified rather than assumed:**

| Window | Range | M1 bars | 15-min bars | Covered |
|---|---|---|---|---|
| `W-A` | 2015-01-04 → 2015-12-31 | 370,787 | 24,755 | ✅ |
| `W-B` | 2014-01-05 → 2015-12-31 | 738,298 | 49,421 | ✅ |
| `W-C′` | 2013-01-06 → 2016-06-30 | 1,293,491 | 86,536 | ✅ |

**THE HOLDOUT WAS NEVER ON DISK.** The vendor publishes past years whole, with no monthly
granularity, so the 2016 file necessarily contained `2016-07-01 → 2016-12-31` — **holdout
under `D-035`**. It was truncated at `2016.06.30` **on arrival**, before any read: 186,608
post-boundary rows discarded, the untruncated CSV and its zip **deleted**, and no
post-boundary row was ever printed, parsed into a result, or displayed. `E23` did not
occur. Any future session extending this corpus past 2016-06-30 must repeat that
discipline or record the breach.

### The week open — the fact `W-C′` and `PT-008`…`PT-013` inherit BY NAME

`D-034` fact 1 binds every week-boundary test to its vendor's week open. That number
**changes** under this amendment, and the change is measured, not assumed:

| | FXCM (`D-034`) | **HistData (this entry)** |
|---|---|---|
| Week open | 21:00 UTC | **22:00 UTC** |
| Local anchor | — | **Sunday 17:00, fixed** |
| DST behaviour | **untested — see `I-010`** | **none — fixed offset year-round** |

Three independent confirmations, because a one-hour error moves every session boundary:

1. **Vendor spec:** *"Eastern Standard Time (EST) time-zone WITHOUT Day Light Savings
   adjustments."*
2. **Measured:** ~~187 week opens across the corpus; **172 land at exactly 17:00** … Five
   non-Sunday opens are the Christmas/New-Year breaks.~~ **CORRECTED — see the C7 block
   below; that count conflated week opens with mid-week re-opens.** The correct figure is
   **181 Sunday-delimited week opens**, of which **170 land at exactly 17:00**, the
   remainder at 17:01–17:10 (late opens), and the modal open is **17:00 in all twelve
   months** — no seasonal shift. **The DST conclusion is unchanged and slightly
   strengthened:** the fixed-offset finding now rests only on genuine week opens.
3. **Event-anchored:** the corpus's largest M1 bar is **2016-06-23 19:17 = 00:17 UTC
   2016-06-24**, coinciding with the Newcastle/Sunderland referendum declarations that
   moved sterling. An independent clock check that does not depend on the vendor's own
   documentation.

**`PT-008`–`PT-013` and `PT-019` must state 22:00 UTC, not 21:00 UTC.** Any draft already
carrying the FXCM number is wrong and must be corrected before it runs.

### `D-031` becomes cheap, and that is a methodological gain

The corpus is stamped in fixed UTC−5 — **natively `D-031` Arm A**. So:

- **Arm A** (fixed offset, no DST) = file timestamps **verbatim**, zero transformation.
- **Arm B** (`America/New_York`, DST active) = file stamp **+1h during US DST**, unchanged
  otherwise. Derivation: stamp `T` denotes `UTC = T+5h`; NY under DST is UTC−4, so local
  `= T+1h`.

On a rendered chart, `D-031`'s binding rule — **both arms always reported** — meant
harvesting each window twice by hand, which is precisely the cost that makes a robustness
check quietly get skipped. It is now one flag. This does not change what `D-031` requires;
it removes the incentive to cheat on it.

### What is LOST by leaving FXCM, stated plainly

**`D-034` fact 2 — the cross-vendor level offset — becomes unmeasurable for these
windows, permanently.** The offset (Yahoo − FXCM: +3.11 pips on highs, +3.94 on lows) was
measured on recent data. FXCM serves **no** 2013–2016 GBP/USD at 15 minutes, so there is
nothing to compare against. **Level-comparability between these windows and the V02–V06
homework cannot be established — only asserted, which this project does not do.** Every
report on this corpus states that its price *levels* are not comparable with prior
homework, and that only *shape* and *distance* claims travel.

### `E06` restated for a CSV corpus

`COMMON_PROTOCOL.md` §2's *"no price is ever read from a pixel"* was written against a
rendered chart. Restated, and **strengthened** rather than relaxed:

> Every quote enters an observation as a **number parsed from a checksummed file**. No
> value is read from a rendering of any kind — not a pixel, not a DOM node, not a chart
> screenshot. A chart may be **looked at**; nothing may be **measured off** one. Any
> figure appearing in a result is reproducible by re-running a committed script against a
> file whose SHA-256 is on record.

A CSV read satisfies `E06` more completely than the DOM-text method it replaces: the
input is fixed, hashed and re-runnable, where a Data Window read was manual and
unrepeatable.

### The data-QA gate, now a precondition

A chart makes a bad tick obvious; a column of numbers computes it silently into a result.
`06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py` is therefore a **precondition on every PT
test run against this corpus**, and its report is cited in each. First run, 2026-08-13:

| Check | Result |
|---|---|
| C1 parse integrity | **PASS** — 1,297,781 rows, zero malformed |
| C2 duplicate timestamps | **PASS** — none |
| C3 ordering | **PASS** — strictly increasing |
| C4 OHLC coherence | **PASS** — no `high < low`, no `high < max(O,C)`, no `low > min(O,C)`, no non-positive quote |
| C5 spike census | 578 bars > 12× rolling median range — **a list for human review, never an auto-exclusion** |
| C6 gap census | **3** intra-week gaps ≥ 30m, **4h43m total** across 3.5 years |
| C7 week-open census | ~~187 opens~~ **181 Sunday-delimited opens** + 6 intra-week re-opens + 3 non-Friday-closing weeks; fixed 17:00, no DST shift |

**C5 needs the human sign-off it asks for, and the ratio metric misleads.** Most of the
578 are thin holiday sessions where a 6-pip bar is 30× a 0.2-pip local median — arithmetic
noise, not corruption. By **absolute** magnitude only **six days** contain any M1 bar over
100 pips, and **26 of those bars fall on 2016-06-23** — the EU referendum, which `D-035`
places inside DEVELOPMENT. The census is finding real events, not artifacts. **Signed off
on that basis; no bar is excluded.**

> **CORRECTION, same day — THAT SIGN-OFF WAS INCOMPLETE, AND THE GATE HAD A BLIND SPOT.**
>
> The C5–C7 sign-off above was recorded without examining `C7`'s **non-Sunday** entries.
> One of them is a hole in the data:
>
> ```text
> last bar   Fri 2014-05-30 16:59
> ABSENT     Sun 2014-06-01              (0 bars; a normal Sunday holds ~399)
> ABSENT     Mon 2014-06-02 00:00–15:01
> resumes    Mon 2014-06-02 15:01        (521 bars vs ~1440 nominal)
> ```
>
> **~22 continuous hours are missing — an entire week open plus a Monday Asian and London
> session.**
>
> > **Two figures circulate for this hole and BOTH ARE CORRECT — do not read them as a
> > contradiction.** Wall-clock from last bar to next is **70h02m** (Fri 16:59 → Mon 15:01);
> > of that, **48h is the normal weekend closure** and is not missing anything. The
> > **missing *trading* time is 22h01m** (Sun 17:00 → Mon 15:01). Run artifacts citing "~70
> > hours" are measuring the elapsed gap; this entry measures the absent session time.
>
> It is the only unexplained absence in 3.5 years, and both relevant checks waved
> it through: **`C6` excluded it by construction** (the gap census skips anything ≥ 12h as
> "the weekend", and a missing session is indistinguishable from a weekend by duration
> alone), and **`C7` rendered it cosmetic** (it surfaced as a `Mon` entry in a weekday
> tally, where it reads as a holiday artifact rather than as an absence).
>
> **`C8` — session completeness** was added to `qa_histdata_m1.py` in response: bars present
> per session against the nominal count for that weekday on the corpus's own clock. It flags
> **11 sessions** — nine Dec/Jan closures, plus the two above. `C8` is a **report, not a
> gate**: a holiday closure is real market behaviour, not a defect, and only a human
> separates a closure from a hole.
>
> **Binding consequence.** Every session `C8` flags must carry an **explicit,
> pre-registered disposition** — include, exclude, or report separately — in any test whose
> window spans it, chosen on completeness grounds and **never** after seeing what it does to
> a result. Any test reporting `n` must report the **exclusion count** beside it.
> `QA_REPORT.txt` is regenerated and supersedes the run quoted in the table above.
>
> Recorded rather than quietly patched, because the failure is the instructive part: **the
> corpus passed four gating checks and three reports while missing a full trading session.**
> This is precisely the hazard named when this project left rendered charts — on a chart a
> 22-hour hole is a visible discontinuity; in a column of numbers it computes silently. The
> QA gate is the compensating control, and it was one check short.
>
> ---
>
> **SECOND CORRECTION — `C7` ITSELF WAS MIS-SPECIFIED, and this one nearly reached a run.**
>
> Raised by the re-issue session, which refused an instruction from this session rather
> than complying with it. It was right and this session was wrong.
>
> `C7` was implemented as *"the first bar after any gap ≥ 12h"* and every such bar was
> reported as a **week open**. That is not what a week open is. A Christmas or New Year
> closure produces a ≥ 12h gap **in the middle of a week that opened normally on Sunday**:
>
> ```text
> 2013-12-22 Sun 17:00   <- the actual week open, 418 bars
> 2013-12-24 Tue         <- closes early
> 2013-12-25 Wed         <- 0 bars, market shut
> 2013-12-26 Thu 06:02   <- a RE-OPEN, which C7 reported as a "week open"
> ```
>
> **A run session deriving week boundaries from that output would have split four weeks in
> two** — and `W-C′` and `PT-025`–`PT-032` are *entirely* weekly-structure tests.
>
> The inverse error is equally bad and was also missed: **when a holiday closure abuts the
> weekend, the affected week produces no anomalous open at all and `C7` stays silent.**
> Three weeks end on a **Thursday** — `2015-12-20`, `2015-12-27` (Christmas and New Year)
> and `2016-06-26` (an artifact of this corpus's own truncation at the `D-035` boundary).
> A Thursday close shortens every censoring horizon that runs to the week close.
>
> **Corrected counts:** ~~187 week opens~~ → **181 Sunday-delimited week opens**, **6
> intra-week re-opens** (never week boundaries), **3 non-Friday-closing weeks**.
>
> **Binding rule, now stated in every affected pre-registration:** *a week is delimited by
> its Sunday 17:00 open; an intra-week holiday re-open is never a week boundary.*
>
> **What this changes about the record.** Nothing about the timezone finding: the
> fixed-offset conclusion now rests on 181 genuine week opens instead of a contaminated
> 187, which strengthens it. What it changes is confidence in this session's own QA work —
> **two of the eight checks were wrong on first writing, and both were caught downstream
> rather than by the gate.** `C6` and `C7` were each wrong in the same direction: they
> treated an absence as a boundary. That is the characteristic failure of measuring a
> market from a file, and it argues for the checks themselves being reviewed, not merely
> their output.

**Reason:** `D-036` established that only an import-capable path reaches the windows, and
the owner chose it. The choice is well-matched to what this batch actually is:
`COMMON_PROTOCOL.md` §7 already excluded every visual concept the course left undefined —
M/W anatomy, second leg, TDI, "the level", anchor points — so all twenty tests resolve to
clock comparisons and price arithmetic. `PT-018` Measure 3 is the proof: the one place a
shape judgment would enter, the protocol already recorded as **NOT MODELLED**. Nothing in
`PT-002`…`PT-021` requires a rendered chart to produce its result.
**Evidence:** `datasets/HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt` (provenance);
`datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt` (the gate run quoted above);
`06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`, `aggregate_m15.py` (both committed);
HistData's published file specification (timezone, column format); `D-034`, `D-035`,
`D-036`; `COMMON_PROTOCOL.md` §2, §7; `PT-018` §3 Measure 3.
**Alternatives considered:** *Importing into MT4 and reading bars off its charts* —
rejected; it converts an auditable file into a rendering and then reads numbers back off
it, which is strictly worse under `E06`, and MT4's History Center path (M1-only import,
period-converter for M15, broker-server overwrite) adds failure modes for no measurement
gain. MT4 remains available for **looking**. *Trusting a vendor-published M15 file instead
of aggregating locally* — rejected; `D-031` makes the bucket boundary the tested variable,
so the boundaries must be ours and auditable. *Deleting the 578 flagged spikes* — rejected;
a news bar and a bad tick are indistinguishable to a threshold, and auto-exclusion would
have silently removed the referendum. *Running the tests before a QA gate existed* —
rejected; the failure mode that replaces "obvious spike on a chart" is "silent wrong
number", and it needed an explicit gate.
**Consequences:** `COMMON_PROTOCOL.md` §1 and §6 are updated — the data-availability
blocker is **CLEARED for `W-A`/`W-B`/`W-C′`**. `PT-002`…`PT-007`, `PT-014`–`PT-018`,
`PT-020`, `PT-021` are **unblocked and runnable**. The seven `W-C` tests are **still owed
their `D-035` re-issue** onto `W-C′` — this entry supplies their data, not their
conformance. Every `PT` file's source table changes from TradingView/FXCM to this corpus,
and every week-boundary test changes 21:00 UTC → **22:00 UTC**. Two open questions are
recorded as **`I-010`**: whether FXCM's 21:00 UTC is a fixed offset or a summer-only
artifact, and which arm's clock the `D-035` boundary is expressed in (Arm B spills **4
bars** past 2016-06-30 into wall-clock 2016-07-01).
**Status:** ACTIVE

---

## D-037 — `D-035`'s re-issue obligation is EXECUTED, and its conformance table was defective: the count is EIGHT, not seven

**Date:** 2026-08-13
**Executes:** `D-035` consequence 2, which recorded a re-issue obligation and explicitly
declined to discharge it (*"This session does not re-issue them; it records the defect"*).
**Corrects:** `D-035` consequence 1, which listed `PT-002` as conforming.
**Governs:** `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-025` … `PT-032`.
**`D-035` is NOT superseded.** Its split, its arithmetic and its reasoning stand unchanged. One
row of one table is corrected by append, in the manner of `D-028`'s and `D-019`'s appends.

> **INTEGRATION NOTE.** The body of this entry was drafted by the session that executed the
> re-issue and is integrated substantially as written; the executing session did not hold write
> access to this file, by design. **One terminology harmonisation:** where the findings table
> below says *"the corpus contains **186 week opens** in the window, of which only 181 open on a
> Sunday"*, read **181 Sunday-delimited week opens plus 5 non-Sunday boundary events**. `C7` was
> re-specified *after* that text was written — precisely because it had been conflating the two
> — and `qa_histdata_m1.py` now reports them as separate sets. **The substance is unchanged and
> the drafting session's point stands**: it was the session that caught the conflation, and it
> caught it by refusing an instruction from the main session rather than complying with it.

**Decision:** The eight `PT` tests whose pre-registered window `W-C` (`2013-01-06 →
2017-12-29`) straddles the `D-035` boundary are **re-issued under new `PT` numbers onto
`W-C′` = `2013-01-06 → 2016-06-30`**, which is `D-035`'s DEVELOPMENT block exactly. The
originals are **retained, marked and never run**; **none was edited into conformance.**

| Original | Question | Re-issued as | `W-C′` sample |
|---|---|---|---|
| `PT-002` **(W-C arm only)** | Do turning points cluster at the six printed boundaries? | **`PT-025`** | **180** weeks × 2 extremes = **360** |
| `PT-008` | "The dealer must cut" the first-eight-hours range | **`PT-026`** | **180** weeks |
| `PT-009` | Does the first move out of the opening range reverse? | **`PT-027`** | **≤ 180** weeks |
| `PT-010` | On which weekday does the week make its high and low? | **`PT-028`** | **180** weeks — **two cells below n = 30** |
| `PT-011` | Is the rest of the week a unidirectional swing? | **`PT-029`** | **180** weeks |
| `PT-012` | Previous week's extreme as barrier | **`PT-030`** | **178** weeks × 2 barriers = **356** |
| `PT-013` | Are Sunday and Monday the accumulation phase? | **`PT-031`** | **180** / **180** / **179** by arm |
| `PT-019` | The weekend gap and the Friday-flat rule | **`PT-032`** | **180** gaps |

**Every `n` above is denominated in TRADING WEEKS PRESENT IN THE CORPUS, never in calendar
weeks** — see the census below, which is the correction that matters most in this entry.

**`PT-002` is the correction, and it is the important half of this entry.** `D-035` consequence
1 lists `PT-002` among the conforming tests. **It is not.** `PT-002` §3 pre-registers **two**
windows — `W-A` for daily extremes and **`W-C` for weekly extremes** — and `INDEX.md` §1 has
recorded it as *"W-A, W-C"* since 2026-08-12. Its `W-C` arm straddles the boundary by the same
546 days as the other seven. `D-035` classified the file by its first window; the search that
found the seven was for files *whose window is W-C*, not for files *that use W-C*.

**`PT-002` is therefore marked PARTIALLY non-conforming, not superseded.** Its `W-A` daily arm
conforms, is unblocked by `D-036a`, and **stays runnable in `PT-002` itself**. Only the weekly
arm moves to `PT-025`. Marking the whole file superseded would have destroyed a conforming test
to fix a bookkeeping error.

**Six substantive changes the re-issues carry, none of them cosmetic:**

0. **Every `n` is denominated in TRADING WEEKS PRESENT IN THE CORPUS, not calendar weeks**, and
   each file carries a **pre-registered `C8` disposition by name** for all seven flagged weeks
   in `W-C′`. `C8` — the session-completeness check — was **added to `qa_histdata_m1.py` after
   these files were drafted**, and it found a **~22-hour hole at 2014-06-01** that `C6` had
   excluded by construction and `C7` had rendered cosmetic. See the findings table below; this
   is the change with the largest effect on the reported numbers.

1. **The data source is the HistData M1 CSV corpus** (`D-036a`), not TradingView/FXCM. Every new
   file states the corpus path, its SHA-256 provenance, the `aggregate_m15.py` derivation, and
   the QA gate (`qa_histdata_m1.py` → `QA_REPORT.txt`) as a **precondition on the run**.
2. **The week open is 22:00 UTC** — Sunday 17:00, fixed UTC−5, no DST — **not FXCM's 21:00
   UTC.** Every one of these eight is a week-boundary test; this is the single most consequential
   substitution and `D-036a` requires it in writing.
3. **Both `D-031` arms are carried and both are always reported** — Arm A = corpus stamps
   verbatim (the corpus is natively UTC−5), Arm B = +1h during US DST.
4. **Price levels are not comparable with the V02–V06 FXCM homework**; only shape and distance
   claims travel (`D-036a`). Stated in every new file's scope statement.
5. **The EU referendum (2016-06-23) is inside `W-C′` and inside DEVELOPMENT** and is **not
   excluded**; the **October 2016 flash crash is in HOLDOUT and unavailable to the Student Phase
   at all.** `COMMON_PROTOCOL.md` §3 disclosure 1's sensitivity appendix is carried in every new
   file and discharges only over what remains.

**Four honest sample findings, recorded because a shortened window is where numbers get
quietly rounded up:**

| Finding | Detail |
|---|---|
| **CALENDAR WEEKS ARE NOT TRADING WEEKS, and the first drafts confused them** | `W-C′` spans 1,272 days and holds **182 calendar Sundays** — but the corpus contains **186 week opens** in the window, of which only **181 open on a Sunday** and **5 do not**. **Four of those five are mid-week holiday RE-OPENS, not week starts**: `C7`'s detector emits the first bar after any gap ≥ 12 h, so a Christmas re-open is indistinguishable from a week open in that tally, and a run session taking week boundaries from it **would split four weeks in two**. Every re-issue now states: **a week is delimited by its Sunday 17:00 open; an intra-week holiday re-open is never a week boundary.** |
| **THE DATA HOLE — the fifth irregular open** | `2014-06-02 Mon 15:01` **is** a week start, and it is a **defect**: the corpus holds **zero bars** for `2014-06-01 Sun` (nominal ~420) and **521 of 1,440** for `2014-06-02 Mon` — **~22 continuous hours absent, covering the entire week open.** It is the **only unexplained hole in 3.5 years**. **Excluded by name from all eight re-issues, counted in every reported `n`.** |
| **The headline `n` is 180, not 181 and not ~260** | 182 calendar Sundays → **181** calendar-complete Sun→Fri weeks (the 182nd, opening 2016-06-26, is truncated by the boundary) → **180 trading weeks** after the data hole. `W-C` would have given **260** — its last Sunday, 2017-12-24, closes exactly on the window's final day. **A 30.8% loss, and every new file states its own number rather than inheriting "~260".** |
| **`PT-030` loses TWO weeks, and the second is not reported by any check** | The week of **2014-06-08** inherits the defect: its barrier **is** the holed week's high and low — a **systematically too-narrow barrier** that would look easier to breach. `n = 178` tested weeks × 2 barriers = **356**. |
| **`PT-032` would have FABRICATED its headline observation** | Applied mechanically, the `2014-05-30 → 2014-06-02` "weekend gap" spans **~22 hours of data the corpus does not contain**. It would be large, land in the tail and the `> 50 pip` bucket, and very likely appear in the five-largest-gaps appendix — **an artifact of absent data on the one test whose finding is gap size.** **Excluded by name.** |
| **`PT-028` goes marginal in two cells** | The trading week is **120 hours and not five equal days** — Sunday **7 h**, Mon–Thu **24 h**, Friday **17 h**. Under the exposure-weighted null at **180 trading weeks** the expected counts are **Sunday ≈ 10.5** and **Friday ≈ 25.5**, both **below `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30**. These are **equal-week upper bounds**: two included holiday weeks carry **zero Friday exposure**, so the realised Friday figure is lower still and the verdict is robust in the direction that matters. Sunday was already marginal at `W-C` (≈ 15.2 over 260 weeks); **Friday was not (≈ 36.8) and now is.** Both carry `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`. The focal Tue/Wed prediction is unaffected. **Correcting calendar → trading weeks moved these figures by less than one observation and changed no verdict; the inputs are now right.** |
| **`PT-028`'s joint table cannot carry inference** | Measure 3's 6 × 6 weekday table averages **5.0 observations per cell** at n = 180. **No χ² or p-value may be quoted for it**; it is printed as a raw count matrix, and the inferential summary is the **sign of `high_day − low_day`** at n = 180. |
| **`C8` dispositions are pre-registered and NOT uniform** | `QA_REPORT.txt`'s gate requires an explicit **pre-registered** disposition for every `C8`-flagged session. Eleven flagged sessions fall into **seven weeks** inside `W-C′`: **six Dec/Jan market closures → INCLUDE, report separately**; **one data hole → EXCLUDE by name**. The include disposition is **inherited, not newly chosen** — the originals already carried *"Excluded weeks: None; holiday-shortened weeks retained and reported separately"* and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping an observation as unrepresentative (`E09`). **Re-deciding it after a QA check surfaced them would be precisely the suit-the-result choice the gate exists to prevent.** Two of the six (`2015-12-20`, `2015-12-27`) **end on Thursday**, which shortens every censoring horizon and, in `PT-032`, produces two **genuine ≥ 72 h closure gaps** that are retained and flagged with their realised duration. |
| **The `E09` line, drawn explicitly** | `E09` forbids excluding an observation because of **what the market did**. The 2014-06-01 exclusion is because **the corpus does not contain what the market did**. That distinction is the entire reason `C8` was written, and it is stated in every affected file so no later reader mistakes a data-integrity exclusion for a convenience one. |
| **Subset cells across the batch** | `PT-027`'s second-breach control, `PT-030`'s breached/un-breached partition and its four-way direction × breach cells, `PT-031`'s extreme-inside-span complement, and `PT-032`'s >18 / >50 pip tails all have run-time-unknown counts. **Each new file pre-registers the `n < 30` label rather than leaving it to be negotiated after the number is seen.** |

**Three vendor-induced substantive changes that are findings in their own right:**

1. **`PT-026`: *"the first eight hours"* and *"the first two 4-hour bars"* are no longer the same
   span.** On FXCM's 16:00-local week open they coincided exactly. On this corpus's 17:00 open,
   midnight-anchored 4-hour buckets give **7 hours** in Arm A and **6** in Arm B, against 8 by
   clock. **Both readings are the instructor's own, in two lessons.** `D-030` forbids picking
   one, so `PT-026` **reports both and adopts neither**, with the 12-hour arm carried over.
2. **`PT-031`: *"Sunday + Monday"* is 31 hours, not two days**, against 48-hour controls. A raw
   range comparison is rigged by arithmetic alone, so the **length-normalised comparison is
   promoted to headline**. `PT-013` §3a's conditional also **resolves**: this corpus **does**
   print Sunday bars, so the Sunday-alone arm **runs** — at 7 hours.
3. **`PT-032`: the original's primary control does not survive.** This corpus trades continuously
   Sunday 17:00 → Friday 17:00 (QA `C6`: **three** intra-week gaps ≥ 30 m in 3.5 years), so
   *"intra-week daily-boundary gaps"* **do not exist on it**. The control is **retained,
   relabelled** as the bar-to-bar change across the 17:00 instant on Mon–Thu, declared a **floor
   rather than a matched comparator**, and the **N3 shifted-boundary sanity control is promoted
   to co-primary** because it is now the only control that separates a real discontinuity from a
   harvest defect. `PT-032` also declares that its bid-only gaps are a **lower bound** on
   execution risk — a measurement error that runs **in favour** of the instructor's rationale,
   and therefore stated before the result.

**Reason:** `D-035` created a re-issue obligation and left it undischarged; leaving it open meant
seven — in fact eight — tests that could not be run without either opening the holdout or
editing a pre-registration to fit, both of which `D-027` forbids. Discharging it now, while
nothing has been run and no result exists, is the only time it is free. The `PT-002` correction
is recorded rather than silently absorbed because **a conformance table that is wrong in one row
will be trusted in all of them** by the next session that reads it.
**Evidence:** `PT-002` §3, §7, attestation line (two windows declared);
`PRE_REGISTERED/INDEX.md` §1 (window recorded as *"W-A, W-C"*); `PT-008`, `PT-009`, `PT-010`,
`PT-011`, `PT-012`, `PT-013`, `PT-019` §3 (window `W-C`); a repository search of
`PRE_REGISTERED/` for `W-C` and `2017-12-29` returning exactly those eight files;
`COMMON_PROTOCOL.md` §3, §3a; `D-027`, `D-028`, `D-030`, `D-031`, `D-035`, `D-036`, `D-036a`;
`datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt` (`C6` gap census, `C7` week-open census);
`scripts/aggregate_m15.py` (bucket anchoring, arm derivation); `PT-022`/`PT-023` (the marking
and re-issue precedent this follows). Week counts are **calendar arithmetic over the window's
dates**; **no price was read from the corpus by the session that wrote these files.**
**Alternatives considered:** *Re-issuing only the seven `D-035` named and leaving `PT-002` for a
later session* — rejected; the defect was found while doing the work, and a known-wrong
conformance table left standing is worse than the original omission. *Marking `PT-002` wholly
superseded* — rejected; its `W-A` arm conforms and is runnable, and destroying a conforming test
to tidy a table is a net loss. *Editing `W-C` to `W-C′` in the seven originals* — rejected
outright; `D-027` requires a new test ID and a retained original, and this is the exact failure
mode the retention rule exists to prevent. *Re-issuing onto a window chosen to restore n ≈ 260
(e.g. starting in 2011)* — rejected; the windows were fixed on calendar grounds before any chart
existed (`COMMON_PROTOCOL.md` §3), and re-cutting one to recover sample size is choosing a period
for its size, which is the selection pressure `D-027` exists to remove. *Keeping the calendar
count because it is simpler, or because it happened to land near the right number* — rejected;
`n = 181` from calendar arithmetic and `n = 181` calendar-complete weeks agreed **by
coincidence**, and the correct trading-week figure is **180**. *Leaving the `C8` dispositions to
the run session* — rejected outright; that is the one choice that would certainly be made to
suit whatever the result looked like, and `QA_REPORT.txt`'s own gate line now forbids it.
*Rounding 180 up to
"~180" or "about 260 as before"* — rejected; the sample loss is the price of the pin and is
reported as such.
**Consequences:** `PT-025`…`PT-032` are pre-registered and **runnable** — `D-036a` supplies their
data, `D-035` supplies their window, and no blocker remains for them. `PT-002` is runnable **on
its W-A arm only**. `PT-008`–`PT-013` and `PT-019` are **permanently retired unrun** and must
never be run; any future session finding them must read their status block first.
`COMMON_PROTOCOL.md` §3a should record `W-C′` as a first-class window with its **180-trading-week**
count (182 calendar Sundays, 181 observable Sunday opens, less the 2014-06-01 hole),
and §1's 22:00 UTC row should name the eight new numbers — **owed, not done in the session that
wrote this text.** `validate_project.py` may now check that no observation cites `PT-008`–
`PT-013`, `PT-019`, or `PT-002`'s W-C arm.
**Status:** ACTIVE

---

## D-038 — Concurrent sessions get their own branch, and their own worktree where practical; merge-back is single-threaded

**Date:** 2026-08-13
**Governs:** every session, agent or human, that may run against this repository at the
same time as another.
**Adopts:** the durable fix `SETUP_ISSUES.md` `I-009` "Residual risk" has recommended and
left unadopted since 2026-08-10 (*"one working tree per session (git worktrees) … recommended
but not yet adopted"*).
**Refines, does not supersede:** `I-009`'s staging mitigations and `D-022`. Those remain in
force as the last line of defence for any work that still shares a tree.

**Decision:** Whenever more than one session may be writing to this project concurrently,
**each session works on its own dedicated git branch, and — where the environment supports it —
in its own git worktree (separate checkout directory).** Two write-heavy sessions never commit
to the same branch at the same time, and never share one working tree.

**Merging back is a distinct, single-threaded step.** One session at a time integrates its
branch into the default/integration branch — fetch, verify no divergence, merge or fast-forward,
push — and no other session merges while that is in flight. Integration is not something a
working session does incidentally at the end of its own work; it is its own act, performed
knowing it is the only one happening.

**Branch naming convention** (a convention, not a gate — a descriptive name that identifies the
session's task is what matters):

| Prefix | Use |
|---|---|
| `video/vNN` | lesson ingestion work for video *NN* — e.g. `video/v08` |
| `review/vNN` | an independent review round against video *NN* |
| `fix/<description>` | remediation of named open items or findings |
| `infra/<description>` | tooling, scripts, bookkeeping, governing-document work |

**Project-policy documents — `DECISIONS.md`, `SETUP_ISSUES.md`, `COURSE_PROGRESS.md`,
`LOG.md`, `REVIEW_INDEX.md` — are edited on the integration branch**, not on a task branch,
because they are append-only ledgers that every concurrent session reads, and a policy change
that sits unmerged on a task branch is a policy no other session can see. This entry itself was
written that way.
> ⚠️ **This paragraph is AMENDED by `D-038a`.** The list above conflates two kinds of file and,
> read literally, forbids a lesson or review session from writing the very records its job
> produces. `D-038a` splits it into **policy ledgers** (integration branch only) and **evidence
> ledgers** (written on the task branch, merged with the work). Read `D-038a` before applying
> this paragraph. The superseded text is retained above, unedited.

**Reason:** The shared-tree collisions are not hypothetical and they are not rare — they have
recurred across four days, against sessions that were following the mitigation correctly. The
mitigations `I-009` supplies are conventions enforced by nothing: `git add <explicit paths>`
writes into a **shared index another session has already staged into**, so staging discipline
controls what a session *adds* and not what is *already there*. The corrected
`git commit -m "…" -- <paths>` form is a genuine improvement and it is still a habit rather than
a control. Separate worktrees remove the shared index, the shared HEAD and the shared checkout
entirely, so the failure has no mechanism left. **This is the difference between a rule that
sessions must remember and a condition under which the failure cannot occur.**

The cost is real and worth naming: an extra checkout directory per session, and a merge step
that must be performed deliberately. That cost is paid once per session; the collision cost has
been paid repeatedly, in wrong commit authorship, in mislabelled history that `git log` can no
longer attribute, and — at `1c836df` — in a review that flags a gate breach being swept into the
very commit containing the breaching work, under a message describing only the latter.

**Evidence:** `SETUP_ISSUES.md` `I-009` (both collisions, the corrected mitigation, and the
"Residual risk" paragraph this entry discharges); `I-009` collision-2 table — `6e4adac`,
`4068db7`, `58e3d03`, `a6fa421` (recurred 2026-08-13, three days after the mitigation was
written), `8785c41` (a session that ran **no** `git add -A` and staged only its own five paths
and cross-committed anyway); `LOG.md` 2026-08-10 "Addendum — commit collision" (`1c836df`);
`LOG.md` V07 entry "⚠ Process — `I-009` recurred, against this session's work"
(`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` swept into `8785c41`); `18_REVIEW/V07/V07_REVIEW_R1.md`
§ on the collision, at commit `69c02ac` — the V07 review found a same-file collision between the
V07 session and a concurrent session and charged **no finding against the student**, because the
student's own staging was correct and the defect was structural; `COURSE_PROGRESS.md` V07 GATE
carry-forward (f) *"`I-009` IS LIVE ON THIS MACHINE"*; `18_REVIEW/REVIEW_INDEX.md` (two
independent R1 reviews of the same round produced concurrently by duplicate sessions).
**Verified in this environment, not assumed:** `git worktree add` **works here** — a worktree at
`/Users/randyschutt/Desktop/Trading/MMM-Agents-v08` on branch `video/v08` was created, checked
out 508 files, reports a clean `git status`, and passes `validate_project.py`. Branch-only
isolation is **not** the practical ceiling on this machine.

**Alternatives considered:** *Keeping the `I-009` conventions and trying harder* — rejected;
`8785c41` is a session that followed them exactly and collided anyway, which is the argument
against conventions stated in evidence rather than in principle. *Serialising all work — never
run two sessions at once* — rejected; it is the only alternative that is strictly safer, and it
costs the parallelism this project has actually used to run ingestion, review and data work
together, when branch isolation buys the same safety without it. *Branch-only isolation in one
shared tree* — rejected as the standing policy, though it is the fallback where worktrees are
unavailable; branches alone do not fix `I-009`, because the shared **index and checkout** are
the mechanism, not the branch pointer, and two sessions on two branches in one tree cannot both
have their branch checked out. *A `.git/index.lock`-style advisory lock or a pre-commit hook* —
rejected for now; it constrains the symptom (concurrent commits) rather than removing the shared
state, and it is more machinery than a second checkout directory. *Rewriting the polluted
history to correct authorship* — rejected, restating `I-009`: nothing was lost, all of it is
pushed, and rebasing while another session holds the same tree can destroy uncommitted work.

**Consequences:** A session spawned for concurrent work must be **told its branch** (and its
worktree path) at spawn time; a session that is not told is entitled to assume it is alone and
will work in the default tree. `I-009` may now be narrowed from `OPEN` toward its durable fix,
but should **not** be closed until a full round has run under this policy — **owed, not done by
the session that wrote this entry.** `I-009`'s staging discipline (`git status --porcelain`
before staging; `git commit -m "msg" -- <paths>`; never `git add -A`) **remains mandatory
everywhere**, including inside a private worktree, because the policy is a convention too and
the next session may not have read it.

**Two operational facts a worktree session must know, verified here:** (1) `.gitignore`d assets
do **not** materialise in a new worktree — `01_SOURCE_VIDEOS/**` and
`06_MANUAL_BACKTEST/datasets/**` (127 MB HistData corpus) arrive empty, and a session needing
them must symlink or reference the primary checkout; the `video/v08` worktree has both symlinked
and its `git status` stays clean because both paths are ignored. (2) A branch that is checked out
in one worktree **cannot** be checked out in another, which is the isolation working as intended
rather than a fault.

Merge-back to the integration branch happens **one branch at a time**, with a `git fetch` and a
divergence check immediately before the push, per the discipline already in use.
**Status:** ACTIVE

---

## D-038a — `D-038`'s integration-branch-only ledger list is split: POLICY ledgers vs EVIDENCE ledgers

**Date:** 2026-08-13
**Amends:** `D-038`, one paragraph only — the "Project-policy documents … are edited on the
integration branch" rule. Everything else in `D-038` (branch-per-session, worktree-per-session,
single-threaded merge-back, the naming convention, the `I-009` staging discipline) is
**unchanged and still in force**.
**Numbered `D-038a` rather than `D-039`** because it clarifies a rule `D-038` already made; it
is not an independent decision and must never be cited apart from `D-038`.
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **68**, raised by `18_REVIEW/V08/V08_REVIEW_R1.md`
(`N1`) after the V08 student session disclosed the deviation in its own `LOG.md` entry rather
than resolving it silently.

**Decision:** `D-038`'s single list of integration-branch-only files is **two categories, not
one**:

| Category | Files | Where edited |
|---|---|---|
| **POLICY ledgers** | `00_SYSTEM/DECISIONS.md`, `00_SYSTEM/SETUP_ISSUES.md`, `CHANGELOG.md`, and every standing protocol or standard — `06_MANUAL_BACKTEST/PRE_REGISTERED/COMMON_PROTOCOL.md`, `00_SYSTEM/REVIEW_PROTOCOL.md`, `00_SYSTEM/MASTERY_STANDARD.md`, `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`, `00_SYSTEM/STUDY_PROTOCOL.md`, `00_SYSTEM/SOURCE_INGESTION_PROTOCOL.md`, `00_SYSTEM/REMEDIATION_PROTOCOL.md`, `00_SYSTEM/FILE_NAMING_STANDARD.md`, `00_SYSTEM/SWF_CAPTURE_RECIPE.md`, the session prompts | **Integration branch only.** Never on a task branch. |
| **EVIDENCE ledgers** | `LOG.md`, `00_SYSTEM/COURSE_PROGRESS.md`, `00_SYSTEM/QUARANTINE_REGISTER.md`, `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`, `11_CONTRADICTIONS/CONTRADICTIONS.md`, `18_REVIEW/REVIEW_INDEX.md`, `00_SYSTEM/SOURCE_MANIFEST.md` | **On the task branch, in the same commits as the work that produced them**, and merged with it. |

**The test that separates them**, for any file this table does not name: *does an unmerged edit
to this file change what another session is permitted to do?* If yes it is a policy ledger and
belongs on integration. If it only records what a session found, it is an evidence ledger and
belongs with the finding.

**Reason:** `D-038`'s rule was written for the failure it had actually seen — a **policy** change
stranded on a task branch, invisible to the sessions it governs. Applied to evidence, the rule
inverts into an obstruction: a lesson session's whole output *is* new `A-xxx` records, a new
`Q-xxx` record, `C-xxx` records and a `LOG.md` entry, and a reviewer's output *is* a
`REVIEW_INDEX.md` verdict row. Forbidding those on the task branch would require every isolated
session to reach across to the integration branch mid-work — reintroducing precisely the shared
write path `D-038` exists to remove — or to defer its own records to a later session, which is
worse. **Evidence ledgers are append-only and their additions are `git`-mergeable by
construction**; policy ledgers are not the problem because they are rare, deliberate, and
already an owner-level act.

**Evidence that the split is safe, measured rather than assumed:** the `video/v08` and
`review/v08` merge-back performed on 2026-08-13 (merges `46d09ed` and `a025b97`) carried edits to
all five files the V08 session flagged. Result: **no conflict, no duplication, no overwrite.**
`LOG.md`, `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` merged as
**pure additions — zero deleted lines** against `23fe5e4`. `COURSE_PROGRESS.md` carried 74 deleted
lines, all of them the V07→V08 status rewrite the session intended, with superseded text retained
in place per project convention. Record-ID sets were re-derived after the merge: **no duplicate
`A-`, `C-` or `Q-` identifier**, and the pre-existing repeated `LOG.md` headings were counted
before and after the merge at the same 9, so the merge introduced none.

**Alternatives considered:** *Leave `D-038` as written and have sessions ask the owner each time*
— rejected; the V08 session did exactly that and it cost a review finding and an owner decision
to settle one predictable case. *Move all five files to integration-only and have the merging
session transcribe them* — rejected; transcription is a lossy manual step performed by a session
that did not do the work, and it puts the record further from the evidence rather than nearer.
*Declare everything an evidence ledger* — rejected; it is the failure `D-038` was written for.

**Consequences:** A session working in isolation writes its evidence ledgers on its own branch
and merges them with its work — this is now the expected behaviour, not a deviation. Two
obligations attach:

1. **Allocate record identifiers against the latest integration branch**, not against the task
   branch alone, and re-check them at merge-back. Concurrent branches can allocate the *same*
   `A-`/`C-`/`Q-` number to different records — **this has already happened**: `video/v08` and
   `infra/add-steve-moro-reference-book` both hold a `C-007` and a `C-008`, for four distinct
   contradictions. `git` cannot detect it, because the two branches append to different regions
   of the same file. The merging session renumbers the later arrival and fixes its
   cross-references.
2. **Merge back promptly.** `REVIEW_INDEX.md` is an evidence ledger, but its gate rows govern
   whether the next lesson may start; a verdict left unmerged holds a gate closed that is
   actually open. Prompt merge-back is what keeps it an evidence ledger rather than a policy one.

---

## D-039 — The Mauro seminar-notes PDF is admitted as NORMATIVE evidence on the owner's attestation

**Date:** 2026-08-13
**Decision:** `00_SYSTEM/EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_anonymous.pdf`
(84 pp., SHA-256 `67bdd3ff2a81aaa3f09a9745bdee94ea60363f93026849836161016f2e56b6f7`) is
**admissible evidence about the method**, on the owner's direct attestation, 2026-08-13:
*"I've read the pdf and can attest that it's in alignment with the instructor and should be
trusted."* The open question left by `00_SYSTEM/EXTERNAL_REFERENCE/README.md` — whether the
document may close a record — is **answered YES, subject to the ordinary evidentiary judgement
every other source is subject to.** The document's `EXTERNAL — NON-NORMATIVE` status, asserted
in `EXTERNAL_VOCABULARY_REFERENCE.md` §9 and written before this attestation existed, is
**superseded for this document only.**

**This is the `D-033` shape, and it carries `D-033`'s central caution verbatim: NOT ONE RECORD
IS CLOSED BY THIS ENTRY.** Admitting a source is not the same as reading it against a record.
Each `A-xxx` still needs the ordinary judgement, made by a session that does the reading, and
several will still fail it on the merits. `EXTERNAL_VOCABULARY_REFERENCE.md` §9.2 is a **flag
list for follow-up**, not a disposition.

**Scope — what is admitted.** The **PDF only.** The web material in `EXTERNAL_VOCABULARY_REFERENCE.md`
§5 is **NOT** admitted and stays `EXTERNAL — NON-NORMATIVE` under that file's §1 banner and §3
reconciliation rule. This matters more than it looks: §9.0 records that the PDF is very probably
the **upstream original** the §5 web sources were copied from, so a §5 page agreeing with the PDF
is **the same document quoted twice** and adds nothing. Admitting the original does not
retroactively admit its copies, and a session must not cite a web page as corroboration of the PDF.

**Reason:** The owner is the authority on the corpus's scope — the same authority exercised in
`D-025`, `D-033` and `D-035` — and the owner has read the document and attested to its alignment
with the instructor's teaching. The agent's standing objection was **provenance**: the document
is anonymous and self-describes as *"Private Study Notes from Seminar of Steve Mauro — Authored
by: Anonymous"*. That objection was raised in full, in writing, before the attestation
(`EXTERNAL_REFERENCE/README.md`; `EXTERNAL_VOCABULARY_REFERENCE.md` §9.0), and the owner has
ruled with it in view. An anonymous document read and vouched for by the project owner is no
longer anonymous testimony — it is the owner's testimony about a document, which is a different
and admissible thing.

**Evidence:** Owner attestation 2026-08-13 (above). Corroborating internal evidence that the
document is of this method and not another: its table of contents contains **seven** of this
corpus's idiosyncratic named objects — *Fractional Disparity* (`A-014`), *The Trading Zone*
(`A-005`), *The 33 Trade* (`A-023`), *The Anatomy of the Half Batman Pattern* (`A-022`),
*Anatomy of an M and W Formation* (`A-011`), *Midweek reversals* (`A-012`), *peak formation
highs and lows* (`A-010`) — which no unrelated trading school would share by chance.
`EXTERNAL_VOCABULARY_REFERENCE.md` §9.1.

### What this decision does NOT do — read this before citing it

- **`D-030` is NOT superseded and still binds.** `D-030` forbids *approximating* a definition the
  course has not supplied. Where this document **actually supplies** a definition, the blocker is
  discharged **by evidence**, which is what `D-030` always contemplated (*"the test waits for the
  lesson that defines it"* — the standard is a definition, not a video). Where it does **not**,
  `D-030` is untouched. **A session that reads `D-039` as a general unblocking has misread it**,
  exactly as `D-033` warned.
- **Specifically, `push` is NOT unblocked, and V05/V06/V07 dimension B stays BLOCKED.** The
  document gives push *sizes* (25–50 pips beyond the Asian range in *"3 pushes or candles"*) and
  then **withdraws the regularity in the next sentence**: *"it is not that simple and the 3 pushes
  may occur in increments of different sizes… do not simply expect a straight 3 candle movement."*
  The hedge is part of the teaching; recording the number without it is `E03`. **A push-size is
  not a push-recognition rule**, and Recognition is what dimension B grades. This is the single
  most likely over-reach from this entry and it is refused in advance.
- **It does not make the document outrank the recordings.** `D-008` still ranks course evidence
  above agent interpretation, and where this document and a lesson differ, **the lesson is the
  corpus.** The document describes seminars; `01_SOURCE_VIDEOS/` is what this project studies.

> ### THE VIDEOS WIN, AND A DIVERGENCE IS A FINDING — owner direction, 2026-08-13
>
> Owner direction, same day, in the same exchange as the attestation: *"if at any time the videos
> contradict the pdf then we can call it out."*
>
> **This is mandatory, not permissive.** A session that notices a lesson stating something this
> document contradicts **must** log it as a `C-xxx` in `11_CONTRADICTIONS/CONTRADICTIONS.md`,
> tagged `MMM-NOTES` vs the speaker, with the page and the timestamp. It is **never** resolved by:
> reading the lesson down to fit the notes; treating the notes as "what he really meant"; treating
> the lesson as a misspeak; or quietly preferring whichever is more codable.
>
> **Resolution rule when they conflict: the recording wins.** The notes are an attested account of
> seminars this project did not record; the videos are the primary material this project exists to
> study. Where the recording is clear, it is doctrine and the note is superseded on that point —
> annotate `EXTERNAL_VOCABULARY_REFERENCE.md` §9.2 accordingly and leave the superseded text
> visible per `REMEDIATION_PROTOCOL.md` §2.
>
> **Two live candidates already exist and are flagged now, not discovered later:** the **800 EMA /
> "blueberry"** (in V06 audio, absent from the document — consequence 4) and the **ADR lookback**
> (*"last 2 weeks"* in the document vs. the guests' 2-day and unbounded bases — consequence 3).
> Neither is adjudicated here. Both are the exact shape this direction anticipates.
>
> This cuts the other way too and that is the point: **a divergence is evidence about the corpus,
> not noise to be tidied.** If the recordings and an attested account of the same teacher diverge,
> that is a genuine and interesting finding about the course, and the register exists to hold it.
- **It is not retroactive re-grading.** No mastery grade, review verdict or gate state changes by
  operation of this entry. Re-assessment is the independent reviewer's job under `D-003`/`D-004`,
  not the job of the session that wrote this decision.
- **It does not admit anything else in `EXTERNAL_REFERENCE/`.** The directory's ⛔ banner still
  governs every other file placed there. Admission is per-document and per-attestation.

**Consequences:**

1. **Source tagging becomes mandatory for this document, as speaker tagging is for guests**
   (`D-025` consequence 3, re-adopted by `D-033`). Any citation carries the tag **`MMM-NOTES`**
   with a page number, e.g. *(`MMM-NOTES` p.45)*. Equal authority is not anonymity — with a third
   admissible source class now in play (author, guest, notes), attribution matters **more**.
2. **`EXTERNAL_VOCABULARY_REFERENCE.md` §9 is now a follow-up queue.** The records it flags —
   `A-031` (blood in the water = the TDI market base line cross), `A-055` (`M0`–`M3` = mid-pivots),
   `A-005` (the trading zone = 25–50 pips beyond the Asian range), `A-014`, `A-023`, `A-022`,
   `A-011`, `A-007` — are **eligible for closure on their own evidence** and each needs a session
   that reads the source, applies the judgement, and cites the page. Expect some to survive: `A-011`
   gains a geometric constraint but still no leg count or invalidation rule.
3. **`A-038` (ADR lookback) is NOT resolved and gets harder, not easier.** The document states
   *"the average daily trading range of the last 2 weeks"*. The corpus's guests used a **2-day**
   basis and an **unbounded** one. That is now **three** admissible numbers from three admissible
   sources — which under `D-033`'s logic is a live `C-xxx` contradiction, not a resolution.
4. **A genuine coverage gap is on the record and must not be papered over.** The document's EMA set
   is **5/13/50/200 with no 800**, while the corpus's V06 audio uses *"blueberry"*. And
   **"anchor point" does not occur once in 84 pages**, nor do *Brinks*, *shadow box*, *quarter of
   wood*/`COW`, *tracer* or *vector*. The attestation is that the document **aligns** with the
   instructor, which is not a claim that it is **complete**. `A-001` in particular remains open
   with no external route at all.
5. **`A-020` is eligible but is not closed here.** The document prints *"Hold the Mayo – 200
   Bounce"*, and the owner separately confirmed the condiment mapping on 2026-08-13. A session may
   now close the *Mayo = 200 EMA* half citing (`MMM-NOTES` p.66) plus this entry. It must **also**
   record that the 800/blueberry line is **not** covered by this document, so the record closes in
   part, not in whole.
6. **A future relocation is worth considering and is not done here.** A normative source arguably
   does not belong under a directory whose `README.md` opens *"⛔ NOTHING IN THIS DIRECTORY IS
   COURSE MATERIAL"*. Left in place deliberately: moving a source file mid-branch churns paths for
   no evidentiary gain, and the banners in both files are corrected by this entry. Flagged for the
   owner as a tidy-up, not an obligation.

**Alternatives considered:** *Admitting it as background only — trusted but non-citable* —
rejected as incoherent with the attestation; the owner said trusted, and a source you may believe
but never cite is a source you cannot use. *Admitting it and closing the flagged records in the
same session* — rejected on `D-033`'s precedent and `D-003`/`D-004`: the session that writes the
admitting decision is the worst-placed session to also exercise the judgement it authorises.
*Admitting the §5 web material along with it* — rejected; §9.0 shows those are probably copies of
this document, and admitting copies would manufacture false corroboration. *Declining on
provenance grounds* — rejected; the objection was made in writing, the owner read it and ruled,
and re-litigating a scope call the owner has made with the evidence in front of them is not the
agent's role.
**Status:** ACTIVE

---

## D-040 — The three-tier sourcing hierarchy, and the mandatory reconciliation when a later video speaks

**Date:** 2026-08-13
**Decision:** Definitions and vocabulary for this project are sourced in a fixed order of
precedence, recorded in full in `00_SYSTEM/SOURCING_HIERARCHY.md`:

| Tier | Source | May close an `A-xxx`? |
|---|---|---|
| **1** | The course recordings — `01_SOURCE_VIDEOS/` V01–V21, transcripts, slides, screenshots | ✅ Yes — `RESOLVED BY COURSE` |
| **2** | The Mauro seminar-notes PDF, cited `MMM-NOTES p.N` (`D-039`) | ⚠️ Yes but weaker — `RESOLVED BY MMM-NOTES`, only where it genuinely supplies a definition |
| **3** | Generic internet research — `EXTERNAL_VOCABULARY_REFERENCE.md` §5 | ❌ Never |

Search order is 1 → 2 → 3, stopping at the first tier that answers. A lower tier is consulted
only because the higher tier is **silent** — never because it is unclear or harder to code.

**The operative half of this entry is the reconciliation rule.** Tier 2 and Tier 3 entries are
**provisional occupants of a gap**. Where a **later** Tier 1 statement — in any video, including
ones not yet studied — defines or clarifies a term previously filled from Tier 2 or Tier 3, the
**Tier 1 statement takes priority**, and the earlier fill-in **MUST be explicitly reconciled at
that point**. It is never left standing to silently outrank real course content, and never blended
with the course statement into a composite definition no source actually states. The six-step
process — notice, classify, annotate in place, keep the superseded text visible per
`REMEDIATION_PROTOCOL.md` §2, update the `A-xxx` to the Tier 1 basis, log it (and open a `C-xxx`
on a true contradiction) — is specified in `SOURCING_HIERARCHY.md` §3.1, with the four
relationship cases in §3.2.

**Reason:** The precedence order already existed, but only implicitly, spread across `D-039`,
`EXTERNAL_VOCABULARY_REFERENCE.md` §3 and §9.6, and `EXTERNAL_REFERENCE/README.md`. A rule a
session has to reassemble from four files is a rule a session will get wrong — and the specific
way it gets wrong is the dangerous one: a Tier 2 definition written down early, never re-checked,
still sitting in the spec after the video that actually defines the term has been studied. Owner
instruction, 2026-08-13, requiring the hierarchy be stated once, plainly, with the reconciliation
process documented rather than merely asserted.

**Evidence:** Owner instruction 2026-08-13 setting out the three tiers and the critical rule that
*"if a LATER video ever defines or clarifies a term that was filled in from Tier 2 or 3, the later
video's definition takes priority."* Owner adjudication, same session, that this hierarchy is a
**ranking layer only** and does **not** downgrade `D-039`.

### What this decision does NOT do

- **It does not modify `D-039`.** The Tier 2 PDF stays **normative** and may still close a record.
  `A-014` and `A-023` remain `RESOLVED BY MMM-NOTES` and are **not** reopened by this entry —
  owner adjudication, 2026-08-13, asked directly and answered directly.
- **It does not modify `D-030`.** `push` is not unblocked; V05/V06/V07 dimension **B** stays
  **BLOCKED**.
- **It does not modify `D-025` / `D-033`**, which continue to rank speakers *within* Tier 1. A
  guest presenter is Tier 1 material subject to `D-033`, **not** demoted to Tier 2.
- **It closes, reopens and changes the status of no `A-xxx` whatsoever.** Establishing an order of
  precedence is not applying it. `SOURCING_HIERARCHY.md` §3.4 records the standing obligation to
  re-check `A-014`, `A-023` and `A-020` against Tier 1 when a relevant lesson is reached; that is a
  queue, not a disposition.

**Alternatives considered:** *Leaving the ordering implicit across the four existing files* —
rejected; that is the status quo this entry exists to fix, and the reconciliation trigger was
stated nowhere as a **forward** obligation on future videos. *Folding the hierarchy into `D-039`
by editing it* — rejected under this file's append-only rule. *Treating Tier 2 as non-closing, per
the literal Tier-2 framing in the instruction* — **raised with the owner rather than assumed**,
because it would have contradicted `D-039` and required reopening `A-014` and `A-023`; the owner
ruled that `D-039` governs and the tiers are a ranking layer.
**Status:** ACTIVE
