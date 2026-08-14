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

> 📌 **POINTER ADDED 2026-08-14 — `D-046`.** `D-046` adopts **`EXCLUDED BY DECISION`** as a
> third mastery disposition, available to **any** dimension under a four-condition test.
> **This entry is REFINED, not superseded, and stays `ACTIVE`** — its `NOT APPLICABLE` grant to
> dimensions F and G is unchanged. **This entry's text is not edited** (append-only).

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

> 📌 **POINTER ADDED 2026-08-14 — `D-046`.** **This entry's two-row disposition table becomes
> THREE rows**: `D-046` adds **`EXCLUDED BY DECISION`** — subject matter exists, the work is
> permanently barred by a **numbered decision that is cited**, no future lesson can lift the bar,
> and the record states **what** was excluded. It closes like `NOT APPLICABLE` and **accrues no
> debt**, and it is available to **any** dimension. **This entry is REFINED, not superseded, and
> stays `ACTIVE`; its text is not edited** (append-only). The amended table is printed in `D-046`.

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

> 📌 **POINTER ADDED 2026-08-14 — `D-050` PART 2 REDUCES FACT 1 TO ITS EVIDENCE.**
> **Fact 1 is restated as: FXCM's week open is 21:00 UTC over the OBSERVED SUMMER WINDOW
> (`PT-023` §1, 2026-05-31 → 2026-08-13); its WINTER behaviour is UNMEASURED.** The sample lies
> entirely inside northern-hemisphere summer, over which *"fixed 21:00 UTC year-round"* and
> *"DST-anchored New York 17:00"* are **indistinguishable**. **`W-C` and `PT-008`–`PT-013` STAND
> and are NOT re-run**; **no NEW test may bind to a year-round FXCM week open by name**; and any
> cross-vendor comparison with the HistData series **states the open question at the point of
> comparison**. ⭐ **A WINTER PROBE IS OWED** — a standing obligation on the first session running
> after **1 November 2026**, on any week between November and February, compared against 22:00 UTC.
> **The result is APPENDED HERE and fact 1 is measured, never inferred.** `SETUP_ISSUES.md` `I-010`
> Q1 closes on that measurement and not before. **This entry's text is not edited** (append-only).

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

> 📌 **APPENDED 2026-08-14 — `D-050` PART 1 STATES THE CLOCK. `I-010` Q2 IS CLOSED.**
> **The DEVELOPMENT/HOLDOUT boundary at `2016-07-01` is ONE INSTANT, expressed in the corpus's
> native UTC−5 (Arm A) clock, and it is THE SAME INSTANT FOR BOTH `D-031` ARMS.** It is **not**
> re-cut per arm, and the rule is **general** — it governs the start and end of **every**
> pre-registered window at **every** timeframe unless a later decision says otherwise for a named
> window. **Measured consequence, so it is never mistaken for a holdout leak:** under Arm B the
> aggregation stamps **4 `M15` bars** and **1 `H1` bar** with a wall-clock date of `2016-07-01`;
> **those bars are DEVELOPMENT data** — their underlying M1 is entirely `≤ 2016-06-30` in the
> file's own clock. **The holdout remains sealed and unopened. No result is invalidated and no
> test is re-run.** **This entry's text is not edited** (append-only).

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

> 📌 **POINTER ADDED 2026-08-14 — `D-047` CORRECTS THIS ENTRY'S STATED REASON.**
> **The premise that *"evidence ledgers are append-only and their additions are `git`-mergeable by
> construction"* is FALSE AS STATED AND IS WITHDRAWN.** Append-only makes a ledger
> **conflict-tolerant, not conflict-free** — two branches appending to the **same tail** conflict,
> and two branches allocating from the **same number series** collide invisibly. **Both have
> happened here** (the `review/v10` merge conflicted in `REVIEW_INDEX.md`, `LOG.md` and
> `COURSE_PROGRESS.md`, and `LOG.md`'s conflict spliced two session entries together).
> ⭐ **THE OPERATIVE POLICY/EVIDENCE SPLIT IS KEPT UNCHANGED AND IS NOT SUPERSEDED** — it stands on
> its remaining and sufficient ground. **`D-047` attaches three consequences:** identifier
> allocation is **integration-relative and re-checked at merge-back**; `LOG.md`,
> `COURSE_PROGRESS.md` and `REVIEW_INDEX.md` merge **single-threaded**; `REVIEW_INDEX.md` merges
> promptly. **This entry's text is not edited** (append-only).

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

---

## D-041 — The owner's definitive moving-average nickname mapping, and the ketchup/mustard inversion it forces

**Date:** 2026-08-13
**Decision:** The five condiment/food nicknames used across the corpus for the instructor's
moving averages map to periods as follows, on the owner's direct and definitive attestation:

| Nickname | **Period** | Prior project record | Effect of this entry |
|---|---|---|---|
| **Ketchup** | **5 EMA** | `A-020` closure table said **13** | ⚠️ **OVERTURNED — inverted with mustard** |
| **Mustard** | **13 EMA** | `A-020` closure table said **5** | ⚠️ **OVERTURNED — inverted with ketchup** |
| **Water** | **50 EMA** | `A-020`: 50 | ✅ Confirmed |
| **Mayonnaise / "Mayo"** | **200 EMA** | `A-020`: 200 (owner attestation + `MMM-NOTES` p.66) | ✅ **Confirmed and reinforced** |
| **Blueberry** | **800 EMA** | `A-020`: 800, `RESOLVED BY COURSE` on V09 `[00:41:43]` (15-minute chart) | ✅ Confirmed — and the **stronger** Tier 1 basis is retained, not replaced |

**The ruling, verbatim, owner, 2026-08-13:**

> *"Mayonnaise is the 200 EMA, period. 50 is water, 5 is ketchup, 13 is mustard, 800 is
> blueberry. These are the definitive names and numbers."*

**Two operative consequences, and they are of different kinds. Do not conflate them.**

1. **`C-018` is CLOSED** — V11's `[00:46:45]` *"There's the mayonnaise. There's the 50"* is
   resolved as **reading B (enumeration)**: two different lines pointed at in turn, **not** an
   apposition equating mayo with 50. `A-020` is untouched by that utterance. See *"What closing
   `C-018` rests on"* below — it does **not** rest on the owner outranking a recording.
2. **`A-020`'s ketchup and mustard rows are OVERTURNED**, on the same attestation. This half was
   **not** anticipated by the instruction that produced this entry, and it is recorded first
   rather than buried, because a session skim-reading this entry as *"the owner confirmed what we
   already had"* would carry the wrong number for two of the five lines.

### ⚠️ THE INVERSION — stated plainly, because every other source in this project says the opposite

`A-020`'s closure block (2026-08-13, `D-039`) records **Mustard = 5, Ketchup = 13**.
`EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 (Tier 3, non-normative) records the same assignment from
three independent BTMM web sources. The quarantined `Q-002` `NOTES.md` also opens *"5 Mustard"*.
The project further **reasoned toward** Ketchup = 13, from V06's *"closed below 13"* rule and its
13/50 relationship.

**None of that survives the owner's ruling, and none of it is deleted.** The owner has read the
numbers and named them *definitive*. Under `D-039` the owner's attestation is the warrant on which
`A-020` closed in the first place; an attestation that can close a record can correct the record it
closed. The prior assignment is retained everywhere it appears, marked superseded per
`REMEDIATION_PROTOCOL.md` §2, and this entry is the citation.

**What the inversion should do to a future session's confidence, and it is not nothing.** Tier 3
convergence was **wrong on a point where it was internally coherent, cross-source consistent, and
agreed with the project's own inference from V06.** That is the single best-calibrated warning this
project has yet produced against `EXTERNAL_VOCABULARY_REFERENCE.md` §5, and it is worth more than
the mapping itself. §1.3's *"one document quoted twice"* trap is now demonstrated in a case where
the copies were unanimous **and wrong**. `D-030` was right for the right reason.

### What closing `C-018` rests on — and what it must NOT be read as establishing

`C-018` filed the V11 utterance as `CONFLICT — OWNER ADJUDICATION REQUIRED` and stated in terms why
`SOURCING_HIERARCHY.md` §3.3's *"the recording wins"* **could not close it**: the recording is
**two-ways readable** (apposition vs. enumeration), so there is no single Tier 1 statement for the
rule to prefer. That analysis is correct and is **upheld**, not overridden.

**The owner has therefore supplied the missing thing — a disambiguation — and not a trump card.**
The closure selects between two readings of Tier 1; it does not defeat Tier 1. `C-018`'s own
reasoning already favoured reading B on three independent grounds (the plural *"averages"*; the
`[00:46:52]` recurrence where *"the 50"* is unambiguously the RSI market baseline; the frame
showing at least four unlabelled averages). **The owner's ruling agrees with the session's own
better reading.** That agreement is worth recording: the V11 session declined to adopt the
convenient reading and was right to.

**This entry does NOT establish an owner "Tier 0", and the phrasing matters.** There is no fourth
tier and no tier above Tier 1. Owner attestation is an **adjudication warrant that sits outside the
source hierarchy** — it is how the project resolves a question the sources leave open or leave
ambiguous, and `AUTOMATION_AMBIGUITIES.md`'s `STATUS VALUES` table still ranks
`RESOLVED — OWNER ATTESTATION` as the **weakest** of its three resolved statuses. Nothing here
promotes it.

### What this decision does NOT do

- **It does not make any nickname `RESOLVED BY COURSE`.** Ketchup, mustard, water and mayo remain
  `RESOLVED — OWNER ATTESTATION` and must be cited that way. **Only blueberry** is
  `RESOLVED BY COURSE`, on V09 `[00:41:43]`, and it keeps that stronger status **and its
  15-minute timeframe**, which this ruling does not supply and does not disturb.
- **It does not discharge `SOURCING_HIERARCHY.md` §3.4.** `A-020` stays on the standing re-check
  list. A later video that attaches a period to a nickname still governs, still triggers §3.1's
  six steps, and still outranks this entry on that point. **Closed on owner attestation is not
  closed for good** — and the fact that this entry had to overturn two rows of an owner-attested
  closure is the argument for keeping the obligation, not against it.
- **It supplies no threshold, and unblocks no rule.** `A-020`'s two surviving cautions are
  untouched: *"enough distance between the entry and the mayonnaise"* (`V02 [00:19:46]`) is still
  an undefined viability filter that `D-030` forbids numbering, and knowing a line's period gives
  the **line, not the threshold**. `[00:05:00]`'s *"manays"* is still PROBABLE, not confirmed.
- **It does not touch `C-010`.** The 800-vs-notes discrepancy is a question about what
  `MMM-NOTES` omits, not about which nickname carries which number. The notes still enumerate
  *"the 5, 13, 50 and 200"* with **no 800** in 84 pages, and the corpus's 800 still stands.
- **It does not rehabilitate `Q-002` or `Q-012`.** See the by-product below: the quarantine gets
  **stronger**, not weaker.
- **It changes no mastery grade and no review verdict.** Re-assessment is the independent
  reviewer's job under `D-003`/`D-004`.

### A by-product: the `Q-002` quarantine gets STRONGER, not weaker

`A-020` records that the fabricated `NOTES.md` mapping — *5 Mustard, 13 Water, 50 Mayo,
200 Blueberry, 800 Raspberry* — is *"the real sequence shifted one place"*, dropping *Ketchup* and
inventing *Raspberry*. **That analysis survives the inversion and gets cleaner.** Against the
corrected order — Ketchup(5), Mustard(13), Water(50), Mayo(200), Blueberry(800) — the fabricated
file is the genuine sequence with its **first** element removed and everything slid up a rung, plus
an invented tail. Under the old assignment the drop was mid-list; under the corrected one it is a
clean truncation from the front. `raspberry` still occurs **0×** in genuine audio anywhere in the
corpus. The same applies to `Q-012` §2's *"50 (Mayo)"*, which this entry confirms is wrong.

**Reason:** Five nicknames were spread across a closed `A-xxx` record, a non-normative Tier 3
table, a quarantined file and one open contradiction, with **no single place a session could look
up what a nickname means**. A mapping that must be reassembled from four files is a mapping a
session will get wrong — and the ketchup/mustard inversion proves the failure was already live,
because the wrong assignment sat in `A-020`'s closure table, in §5.16, and in the reasoning of both,
unchallenged. Owner ruling, 2026-08-13, issued directly and marked definitive.

**Evidence:** Owner attestation, 2026-08-13, verbatim above — same evidentiary weight as the
owner-attested closures of `A-014` and `A-023` and the normative status granted to `MMM-NOTES`, all
under `D-039`. Corroboration on **Mayo = 200** only: `MMM-NOTES` p.66 entry list, *"Hold the Mayo –
200 Bounce"*. Independent Tier 1 corroboration on **Blueberry = 800**: V09 `[00:41:43]`, *"The
blueberry is the 800 on the 15 minute time frame"* (`GUEST`, normative under `D-033`). Contradicted
on ketchup/mustard by: `A-020`'s closure table; `EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 and its
three cited web sources (Tier 3, closes nothing, `D-040`); `Q-002`'s fabricated `NOTES.md`. **No
Tier 1 statement attaches a period to *ketchup* or *mustard* anywhere in V01–V11** — `mustard`
occurs 0× in genuine audio in V05, V06, V07 and V08, and `ketchup` occurs nowhere at all — so the
inversion contradicts **no recording**, only the project's own lower-tier fill-in.

**Alternatives considered:** *Recording only the four rows the instruction described as confirmed,
and querying the ketchup/mustard inversion before acting* — rejected; the owner's sentence names all
five in one breath and calls them definitive, the two overturned rows rest on Tier 3 and inference
rather than on any recording, and holding the whole ruling hostage to a re-confirmation would leave
the wrong numbers standing in `A-020` and §5.16 in the meantime. **The inversion is instead recorded
in the loudest terms this file has, at the top of the entry, so it cannot be adopted unnoticed and
is trivially reversible if the owner reads it back and says otherwise.** *Silently swapping the two
rows in `A-020`* — rejected outright; `REMEDIATION_PROTOCOL.md` §2 and this file's append-only rule
both forbid it, and it would erase the most useful calibration datum the entry contains.
*Overriding blueberry's `RESOLVED BY COURSE` status down to owner attestation for consistency of
the table* — rejected; that would **downgrade** a record on the strength of an agreeing weaker
source, which is backwards. *Treating the owner as a new "Tier 0" that outranks the recordings* —
rejected; the owner adjudicated an **ambiguity in** Tier 1, which is a different act, and inventing
a tier above the corpus would retire `SOURCING_HIERARCHY.md` §3.4 by a side door. *Promoting the
mapping into `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`* — rejected on that file's own rule 5 and its
`A-026` precedent: a nickname's period is a **label expansion**, not a method concept, and it
supplies no rule for acting in real time.

**Consequences:**

1. **`A-020` is annotated, not reopened and not rewritten.** Its ketchup and mustard rows are
   marked superseded in place per `REMEDIATION_PROTOCOL.md` §2, with the corrected mapping and a
   pointer here. Its status line stays `RESOLVED — OWNER ATTESTATION. NOT "RESOLVED BY COURSE".`
2. **`EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 carries a superseding banner** naming the two wrong
   rows explicitly. It is a Tier 3 entry and stays non-normative — the banner exists because the
   table as printed is now known to be **wrong**, which is a stronger reason to annotate it than
   its tier is to leave it alone.
3. **`SOURCING_HIERARCHY.md` §3.4 gains a pointer**, so a session arriving at the standing
   re-check obligation finds the corrected mapping without reading this file end to end.
4. **`C-018` closes on `video/v11`, where it lives** — `11_CONTRADICTIONS/CONTRADICTIONS.md` is an
   **evidence ledger** under `D-038a` and `C-018` is unmerged. It is closed on the branch, in the
   branch's own commit, and lands at merge-back. This entry is written on the integration branch
   because `DECISIONS.md` is a **policy ledger**. The two halves are deliberately in two places
   and that is `D-038a` working, not a split-brain.
5. **`SETUP_ISSUES.md` is NOT logged, and the omission is deliberate.** `C-018` correctly recorded
   a `SOURCING_HIERARCHY.md` §3.2 **Case C** obligation as `OWED, NOT DONE`. That obligation is
   **discharged by this closure rather than performed**: Case C is *"genuine conflict, do not
   adjudicate, surface to the owner"*, and the owner has now adjudicated. There is no live conflict
   left to log. `REVIEW_INDEX.md` open item carrying it is closed against this entry rather than
   against a `SETUP_ISSUES.md` entry that would describe a resolved question.
6. **Any artifact citing a nickname must cite the period AND the warrant.** *"Mayo (200 EMA,
   `OWNER-ATTESTED`, `D-041`)"*, never *"the 200 EMA the instructor calls mayo"* — no instructor
   says that on any recording in V01–V11.
7. **The independent review of V11 inherits this, and should test it.** A reviewer is entitled to
   put the inversion back to the owner. Nothing here is protected from that.

**Status:** ACTIVE

---

## D-042 — The exhaustive nickname↔period search returns NEGATIVE; the owner's colour mapping is recorded; and one Tier 1 colour statement contradicts it

**Date:** 2026-08-13
**Bears on:** `D-041` (the nickname↔period mapping), `A-020`, `C-010`,
`EXTERNAL_VOCABULARY_REFERENCE.md` §5.16, `SOURCING_HIERARCHY.md` §3.4,
`06_MANUAL_BACKTEST/tools/MMM_Indicator.txt` (branch `feature/tradingview-mmm-indicator`).
**`D-041` is NOT amended, NOT superseded, and NOT reopened by this entry.** Its five rows stand
exactly as written. What this entry adds is (1) the discharged search obligation, (2) a new
owner-attested **colour** mapping, and (3) **one Tier 1 finding that the owner must adjudicate
before anything is changed.**

---

### 1. THE SEARCH — DISCHARGED, AND THE RESULT IS NEGATIVE

Owner direction, 2026-08-13:

> *"Let's go with whatever the course says. I'm sure it's 5 ketchup, 13 mustard but I could be
> wrong."*

That is a **conditional** instruction: the course governs **if the course speaks**. The search
was therefore run before anything was changed.

**What was searched, in full:**

| Corpus | Coverage | Method |
|---|---|---|
| **V01–V10 transcripts** | `02_TRANSCRIPTS/V01…V10/VXX_TRANSCRIPT.md`, complete files, verbatim bodies **and** the analysis headers | case-insensitive term sweep (`ketchup`, `catsup`, `catch up`, `mustard`, `mayonnaise`, `mayo`, `blueberry`, `water`, `condiment`) **plus** a ±4-line proximity scan of every hit against the token set `5 / 13 / 50 / 200 / 800` |
| **V11 transcript** | `02_TRANSCRIPTS/V11/V11_TRANSCRIPT.md` read from `origin/video/v11` (unmerged — it does **not** exist on the integration branch, and a search that skipped it would have been a false negative) | same |
| **`MMM-NOTES` (Tier 2)** | `00_SYSTEM/EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md`, all 84 pages | same |
| **On-screen / printed text** | every `04_SCREENSHOTS/VXX/INDEX.md`, plus `09_CHART_EXAMPLES/` | nickname terms and colour terms against period labels and legends |

**RESULT — NO NEW PAIRING EXISTS. Nothing found beyond what `D-041` already cites:**

| Nickname | Every explicit period pairing in the whole corpus | Tier |
|---|---|---|
| **Blueberry** | V09 `[00:41:43]` *"The blueberry is the 800 on the 15 minute time frame"* — **already cited by `D-041`** | 1 |
| **Mayo** | `MMM-NOTES` p.66 entry list, *"Hold the Mayo – 200 Bounce"* — **already cited by `D-041`** | 2 |
| **Water** | **none** | — |
| **Mustard** | **none.** Total corpus occurrences: **2**, both in V04, both with no number — `[00:14:42]` *"the averages open making an M formation with the mustard"*, `[00:14:47]` *"There's your M formation in your mustard right there."* (V01 `[00:19:24]` *"the man is the water that catch up in the mustard"* is logged garble and sources nothing) | — |
| **Ketchup** | **none.** The word **occurs zero times in genuine audio anywhere in V01–V11.** The only near-hits are V01 `[00:19:24]`'s garble above and V10 `[00:37:02]` *"I'll never catch up"*, which is the ordinary English phrase about falling behind on homework | — |

**Therefore: the condition in the owner's instruction is NOT met for ketchup and mustard. The
course never pairs either nickname with a period.** `D-041`'s **ketchup = 5, mustard = 13**
stands unchanged as the best-attested answer, on owner attestation, exactly as recorded.

**This also re-confirms `D-041`'s own statement in its Evidence block** — *"No Tier 1 statement
attaches a period to ketchup or mustard anywhere in V01–V11"* — by independent exhaustive search
rather than by inheritance. That claim is now **verified, not assumed**, and
`SOURCING_HIERARCHY.md` §3.4's standing re-check obligation on `A-020` is **discharged as at
V11** and **remains live for V12 onward**.

---

### 2. THE OWNER'S COLOUR MAPPING — NEW, UNCONTESTED ON THREE OF FIVE ROWS

Owner attestation, 2026-08-13. Recorded here because there was previously **no single place** a
session could look up a line's colour, which is the same failure `D-041` was written to fix for
periods.

| Period | Nickname (`D-041`) | **Colour** | Independent corroboration |
|---|---|---|---|
| **5** | Ketchup | **red** | ⚠️ **NONE — and CONTRADICTED by Tier 1. See §3.** |
| **13** | Mustard | **yellow** | ⚠️ **NONE — and CONTRADICTED by Tier 1. See §3.** |
| **50** | Water | **aqua** | ✅ `[TOOLING]` — owner's own MT4 template `3M-shadow-boxes-15M.tpl`, `period=50 color=16776960` → RGB(0,255,255) **AQUA** |
| **200** | Mayonnaise | **white** | ✅ `[TOOLING]` — same template, `period=200 color=16777215` → RGB(255,255,255) **WHITE** |
| **800** | Blueberry | **blue** | ✅ `[TOOLING]` — same template, `period=800 color=16711680` (MT4 BGR) → RGB(0,0,255) **BLUE** |

**The three corroborated rows are a genuinely good result and should be read as one.** The owner
stated these colours from memory; the owner's own charting template, read independently off disk
on a different branch by a different session, produces **the same three colours for the same
three periods**. That is agreement between an attestation and an artifact that were not
consulted against each other.

**It also makes the nicknames read as plain colour-naming** — *blueberry* = blue, and by the
same logic *ketchup* = red and *mustard* = yellow, which is internally consistent with the owner's
period mapping in `D-041`. **This is noted as consistency, NOT adopted as proof.** Colour
semantics as an inference route is `D-030` territory and the tooling README already refuses it
for `mayonnaise`/white on exactly those grounds.

**Warrant, stated precisely so no artifact overstates it:** `OWNER-ATTESTED (D-042)` — **not
observed on-screen**. No frame in `04_SCREENSHOTS/` carries a legend, and no speaker in V01–V11
names a colour and a nickname in the same sentence. The 50/200/800 rows carry the additional
`[TOOLING]` warrant; the 5 and 13 rows carry owner attestation **alone**.

---

### 3. ⚠️ THE CONFLICT — V07 `[00:25:34]` IS TIER 1 AND IT SAYS THE **5** IS **YELLOW**

**This is the finding of this session and it is not a small one.**

> V07 `[00:25:34]`, verbatim from `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md`:
>
> > *"The only other lines in here, look, **this yellow one is a five moving average.** I made it
> > dotted in the 13, 50 and the 200."*
>
> Frame: `04_SCREENSHOTS/V07/INDEX.md` row 22,
> `chart-eurjpy-m15-revisited-for-the-adr-and-ma-question`, `00:25:30` — the frame under
> discussion, `EURJPYm` M15.

**This is Tier 1, it is unambiguous on the colour-to-period join, and it is already on the
record** — `A-020`'s V07 reconciliation row calls it *"the first time in the corpus a colour is
attached to a period in genuine audio."* What is **new** is that **there was no owner colour
mapping for it to contradict until today.**

| Source | 5 EMA | 13 EMA |
|---|---|---|
| **Owner attestation, 2026-08-13 (§2 above)** | **red** | **yellow** |
| **V07 `[00:25:34]`, Tier 1** | **yellow** | — (dotted; no colour given) |

**And the transitive consequence is the part that matters.** The owner also supplies
ketchup = red and mustard = yellow. Joining that to V07's yellow = 5 gives **mustard = 5,
ketchup = 13** — which is **precisely the assignment `D-041` overturned**, the one that had agreed
with `EXTERNAL_VOCABULARY_REFERENCE.md` §5.16's three Tier 3 sources, with `Q-002`'s fabricated
`NOTES.md`, and with the project's own inference from V06's *"closed below 13"* rule.

**NOTHING IS CHANGED ON THIS BASIS, AND THE REASONS ARE THREE:**

1. **The join is not made by any speaker.** V07 says *yellow = 5*. The owner says
   *mustard = yellow*. **No source says both.** Chaining them is inference across two warrants of
   different kinds, which is the `D-030` error and the exact move the tooling README already
   refuses for white/mayonnaise. `SOURCING_HIERARCHY.md` §3.2 **Case C** governs: *"Do not
   adjudicate. Surface to the owner."*
2. **`D-041` was an explicit, definitive owner ruling.** Reversing it requires the owner, in
   terms, not a session's chain of inference. `REMEDIATION_PROTOCOL.md` §2 forbids the quiet edit
   in either direction.
3. **The alternative explanation is live and cheap.** The V07 speaker is a **guest**, on his own
   platform, whose charts elsewhere in that same lesson show *"the dashed ones… are 30 minute
   versions"* and *"the blue heavy ones are 60 minutes"* `[00:27:24]`–`[00:27:33]` — i.e. **this
   presenter's colour scheme is demonstrably his own multi-timeframe convention**, not
   necessarily the course palette. A guest's personal chart colours are weaker evidence about the
   shared palette than a guest's spoken doctrine is about method, and `D-033` does not flatten
   that difference.

**Disposition: `CONFLICT — OWNER ADJUDICATION REQUIRED`.** Logged in `00_SYSTEM/SETUP_ISSUES.md`
as **`I-011`** per §3.2 Case C. The owner's colour mapping in §2 is recorded and propagated **as
owner-attested**, and the conflict is recorded **beside it, in every file that carries it**, so
it cannot be adopted unnoticed. **`D-041` is untouched.**

**The question for the owner, in one line:** *V07's guest says on tape that the yellow line is the
5 EMA. You have said the 5 is red and the 13 is yellow. Is the guest using his own colours, or is
the 5 actually yellow — which would also put ketchup back on 13?*

---

### 4. A NUMBERING COLLISION, FOUND WHILE DOING THIS AND FLAGGED RATHER THAN FIXED

`feature/tradingview-mmm-indicator` carries
`06_MANUAL_BACKTEST/tools/DRAFT_D-041_platform_artifacts.md` — a **different, unadopted** draft
decision (*MT4 platform artifacts are admitted as evidence of PARAMETERS ONLY*) which reserved the
identifier **`D-041`** when `D-040` was the highest on integration. **`D-041` has since been taken
by the nickname mapping on this branch.** This is exactly the collision `D-038a` consequence 1
predicts and instructs the merging session to renumber. The draft file itself already says its
number is provisional and must be re-checked at adoption time.

**Not renumbered here.** That draft is unadopted policy on an unmerged branch; renaming it is the
adopting session's act, not this one's. **The next free identifier after this entry is `D-043`.**

---

**Reason:** The owner made the course the tie-breaker on ketchup/mustard, so the course had to be
searched before the ruling could be either confirmed or left standing — and a negative result that
is not written down gets re-searched by the next session, or worse, gets assumed to be positive.
The colour mapping needed a home for the same reason `D-041`'s period mapping did. And the V07
contradiction is a finding: `SOURCING_HIERARCHY.md` §3.3's rule that *"a divergence is a finding,
not noise"* applies with more force here, not less, because the divergence points back toward the
assignment `D-041` overturned.

**Evidence:** Owner attestation, 2026-08-13 (colours; and the conditional instruction quoted in
§1). Exhaustive search of V01–V10 on this branch, V11 on `origin/video/v11`, the 84-page
`MMM-NOTES` text extract, and all eleven `04_SCREENSHOTS/*/INDEX.md` files — method and coverage
in §1. Tier 1 conflict: V07 `[00:25:34]`, frame `V07/INDEX.md` row 22. `[TOOLING]` corroboration:
`3M-shadow-boxes-15M.tpl`, decoded in `06_MANUAL_BACKTEST/tools/MMM_Indicator_README.md`
(`feature/tradingview-mmm-indicator`).

**Alternatives considered:** *Adopting the V07 chain and re-inverting ketchup/mustard back to
13/5* — rejected on all three grounds in §3; it would overturn an explicit owner ruling on a
two-step inference no speaker makes. *Recording the colours and staying silent about V07 because
the mapping is "new, uncontested information"* — **rejected outright, and this was the live
temptation**: three of five rows are indeed uncontested, but two are contradicted by tape, and
shipping the palette into the Pine defaults without the flag would have put an unverified colour
on the chart under a strengthened warrant. *Filing the conflict as a `C-xxx` in
`CONTRADICTIONS.md`* — rejected; that file records contradictions **within the course sources**,
and this is a course source against an **owner attestation**, which is an infrastructure/adjudication
question and belongs in `SETUP_ISSUES.md`, per that file's own opening rule. *Withholding the
colours from the Pine script until the owner answers* — rejected; the 50/200/800 rows are
independently corroborated and were already shipping, and 5/13 were shipping **invented** cyan and
orange, which owner attestation strictly improves on even while contested.

**Consequences:**

1. **`D-041` stands unchanged.** Ketchup = 5, mustard = 13, on owner attestation.
2. **`A-020` gains an appended block** recording the negative search result, the colour mapping,
   and the V07 conflict. Nothing in it is edited or deleted (`REMEDIATION_PROTOCOL.md` §2).
3. **`EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 gains the colour rows and the same conflict flag.**
4. **`SOURCING_HIERARCHY.md` §3.4 records that the re-check obligation was performed as at V11 and
   returned negative.** The obligation itself **stays live** for V12 onward.
5. **`SETUP_ISSUES.md` `I-011` is opened** and stays `OPEN` until the owner answers §3's question.
6. **The Pine tool adopts the colours** on `feature/tradingview-mmm-indicator`, tagged
   **`[OWNER-ATTESTED] (D-042) — not observed on-screen`** for all five, with the additional
   `[TOOLING]` warrant retained on 50/200/800 and the V07 conflict written into the comment block
   above the 5 and the 13. **`[OWNER-ATTESTED]` ranks above `[DEFAULT]` and below `[TIER 1]`.**
7. **Any artifact citing a line's colour must cite the warrant**, exactly as `D-041` consequence 6
   requires for periods: *"the 5 EMA, red (`OWNER-ATTESTED`, `D-042`, contested by V07
   `[00:25:34]`)"* — never *"the red 5 EMA the instructor uses"*.

**Status:** ACTIVE — with `I-011` open against §3.

---

## D-043 — Owner ruling #2 REVERSES `D-041`'s nickname↔period mapping AND `D-042` §2's period↔colour mapping; the nickname↔**colour** pairing is the one thing that does NOT change; `I-011` closes with Tier 1 agreeing

**Date:** 2026-08-13
**Bears on:** `D-041` (**reversed in part**), `D-042` §2 (**reversed in part**), `D-042` §3
(**resolved**), `A-020`, `I-011` (**CLOSED**), `EXTERNAL_VOCABULARY_REFERENCE.md` §5.16,
`SOURCING_HIERARCHY.md` §3.4, `06_MANUAL_BACKTEST/tools/MMM_Indicator.txt` and
`MMM_Indicator_README.md` (branch `feature/tradingview-mmm-indicator`).
**Supersedes:** `D-041`'s **ketchup** and **mustard** rows; `D-042` §2's **5** and **13** rows.
Neither entry is edited, reopened or deleted — both stand on the record and this entry is the
correction (`DECISIONS.md` append-only; `REMEDIATION_PROTOCOL.md` §2).

**The ruling, verbatim, owner, 2026-08-13, issued after reading `I-011`:**

> *"I was wrong. It's the reverse. 5=mustard=yellow, 13=ketchup=red."*

---

### 1. THE FINAL MAPPING — ALL FIVE LINES, PERIOD **AND** COLOUR

| Nickname | **Period** | **Colour** | Warrant on the period | Warrant on the colour |
|---|---|---|---|---|
| **Mustard** | **5 EMA** | **yellow** | `RESOLVED — OWNER ATTESTATION` (`D-043`) — ⚠️ **CHANGED from `D-041`'s 13** | `OWNER-ATTESTED` (`D-043`) — ⚠️ **CHANGED from `D-042`'s 13=yellow → now 5=yellow.** ✅ **Corroborated by Tier 1**, V07 `[00:25:34]` |
| **Ketchup** | **13 EMA** | **red** | `RESOLVED — OWNER ATTESTATION` (`D-043`) — ⚠️ **CHANGED from `D-041`'s 5** | `OWNER-ATTESTED` (`D-043`) — ⚠️ **CHANGED from `D-042`'s 5=red → now 13=red.** No corroboration |
| **Water** | **50 EMA** | **aqua** | `RESOLVED — OWNER ATTESTATION` (`D-039`, `D-041`, reaffirmed) — ✅ unchanged | `OWNER-ATTESTED` + `[TOOLING]` `3M-shadow-boxes-15M.tpl` `color=16776960` → RGB(0,255,255) — ✅ unchanged |
| **Mayonnaise / Mayo** | **200 EMA** | **white** | `RESOLVED — OWNER ATTESTATION` (`D-039`, `D-041`) + `MMM-NOTES` p.66 (Tier 2) — ✅ unchanged | `OWNER-ATTESTED` + `[TOOLING]` same template, `color=16777215` → RGB(255,255,255) — ✅ unchanged |
| **Blueberry** | **800 EMA**, **on the 15-minute** | **blue** | ✅ **`RESOLVED BY COURSE`** — V09 `[00:41:43]`, `GUEST`, normative under `D-033`. **The stronger basis and its timeframe are RETAINED** — ✅ unchanged | `OWNER-ATTESTED` + `[TOOLING]` same template, `color=16711680` (MT4 BGR) → RGB(0,0,255) — ✅ unchanged |

**This is the authoritative mapping. Cite this entry, not `D-041` and not `D-042` §2, for the
5 and the 13 — on either axis.**

---

### 2. ⚠️ WHICH MAPPING REVERSED — AND THE ONE THAT DID NOT. **READ THIS BEFORE PROPAGATING ANYTHING.**

The owner's sentence bundles nickname, period and colour into one clause — *"5=mustard=yellow"* —
and the project stores those as **two separate decisions on two separate axes**. Mapping the
sentence onto the wrong axis is the single most likely way to get this correction wrong, so the
axes are separated here explicitly.

| Axis | Where it lives | Before (`D-041`/`D-042`) | After (`D-043`) | Verdict |
|---|---|---|---|---|
| **nickname ↔ period** | `D-041` | ketchup = 5 · mustard = 13 | **ketchup = 13 · mustard = 5** | 🔄 **REVERSED** |
| **period ↔ colour** | `D-042` §2 | 5 = red · 13 = yellow | **5 = yellow · 13 = red** | 🔄 **REVERSED** |
| **nickname ↔ colour** | neither, directly — it is the *composition* of the two | ketchup = red · mustard = yellow | **ketchup = red · mustard = yellow** | ✅ **UNCHANGED** |

**Both stored decisions reverse. The composition of them does not.** Because the two reversals
are on adjacent axes, they cancel where they meet: *ketchup* was red when it was the 5 and it is
still red now that it is the 13; *mustard* was yellow when it was the 13 and it is still yellow now
that it is the 5. The condiments keep their obvious colours throughout — the **periods moved
underneath them.**

**Three consequences of that, and none is cosmetic:**

1. **A session correcting only "the colour mapping" corrects nothing that was wrong and leaves
   both real errors standing.** Any artifact keyed on *nickname → colour* (*"mustard is yellow"*)
   was **already correct** under `D-041`/`D-042` and needs **no edit**. Every artifact keyed on
   *nickname → period* or on *period → colour* — which is the Pine script, `A-020`'s tables,
   §5.16's tables and §3.4's summary line — is **wrong** and must be corrected.
2. **`D-042`'s own observation that the nicknames "read as plain colour-naming" survives intact
   and is now the only part of that section that never moved.** It was noted there as consistency
   and explicitly *not* adopted as proof; it is still not proof, and it is still not adopted. But
   it is the invariant across two contradictory owner rulings, which is worth recording as the
   thing to hold onto if a third ruling ever arrives.
3. **The Pine script's five colour constants change on exactly two lines** — the 5-period EMA
   goes red → **yellow**, the 13-period EMA goes yellow → **red**. Because the *nickname* labels
   in that file are attached to *periods*, the nickname on each of those two lines changes too.
   50/200/800 are untouched on both axes and keep their `[TOOLING]` warrant.

---

### 3. `I-011` CLOSES — AND TIER 1 NOW **AGREES** WITH THE OWNER

`I-011` asked the owner one question, and it anticipated this exact outcome in its own
*"To close"* clause: *"If the owner reverses, that is a **new decision entry** superseding both
`D-041` and `D-042` §2 — not an edit to either."* **That is what this entry is.**

| Source | 5 EMA colour | 13 EMA colour | Agreement |
|---|---|---|---|
| **Owner ruling #1** — `D-042` §2, 2026-08-13 | red | yellow | ❌ contradicted by tape |
| **V07 `[00:25:34]`, Tier 1, `GUEST` (normative, `D-033`)** | **yellow** | — (dotted, no colour given) | — |
| **Owner ruling #2** — this entry | **yellow** | **red** | ✅ **agrees with tape** |

> V07 `[00:25:34]`, verbatim: *"The only other lines in here, look, **this yellow one is a five
> moving average.** I made it dotted in the 13, 50 and the 200."*
> Frame: `04_SCREENSHOTS/V07/INDEX.md` row 22, `00:25:30`, `EURJPYm` M15.

**What the agreement is worth, stated precisely so no artifact overstates it:**

- **It is corroboration, not the warrant.** The owner's attestation is authoritative here
  regardless of what the tape says — `I-011` was a Case C surfacing, and the owner adjudicated.
  Had the owner confirmed red/yellow instead, that would equally have closed `I-011`, with V07
  annotated as a guest's private palette. **The record must not read as though the tape forced
  the ruling.**
- **One cell does get a genuine warrant upgrade, and only one.** *"The 5 EMA is yellow"* is now
  stated **directly** by a Tier 1 speaker, on a single warrant, with no chaining: V07 joins a
  colour to a period in one sentence. That cell is `OWNER-ATTESTED` **+ Tier 1 corroborated**.
- **Nothing becomes `RESOLVED BY COURSE`.** *Mustard = 5* still requires chaining V07's
  *yellow = 5* through the owner's *mustard = yellow*, and **no speaker makes that join** — it is
  still the `D-030` two-warrant chain that `D-042` §3 refused to walk, and the fact that it now
  points the *convenient* way does not make it a different kind of inference. **Only blueberry is
  `RESOLVED BY COURSE`.** Mustard, ketchup, water and mayo remain `RESOLVED — OWNER ATTESTATION`
  on both axes and must be cited that way.
- **`D-042` §3's third reason is no longer needed, and it is not thereby disproven.** The guest's
  palette may still be his own — `[00:27:24]`'s *"the dashed ones… are 30 minute versions"* and
  `[00:27:33]`'s *"the blue heavy ones are 60 minutes"* still show a personal multi-timeframe
  convention, and the owner's ruling says nothing about that. What has gone away is the **need**
  to explain the divergence, because there is no divergence left.

**`I-011` is closed `RESOLVED — OWNER ATTESTATION`, in place, in `SETUP_ISSUES.md`, against this
entry.** No `C-xxx` is opened or closed by it: `I-011` was Tier 1 against an owner attestation,
which is an adjudication question, not a contradiction within the course sources.

---

### 4. THE THREE-STATE HISTORY — AND `D-041`'s HEADLINE CALIBRATION LESSON IS ITSELF NOW WRONG

**This is the most useful thing in this entry and it is not the mapping.**

| # | State | ketchup | mustard | Colours | Basis |
|---|---|---|---|---|---|
| **1** | `A-020` closure table, 2026-08-13 (`D-039`) | **13** | **5** | none recorded | Owner attestation as then recorded, agreeing with `EXTERNAL_VOCABULARY_REFERENCE.md` §5.16's three Tier 3 web sources and with the project's own inference from V06's *"closed below 13"* rule |
| **2** | `D-041` + `D-042` §2, 2026-08-13 | **5** | **13** | 5 = red, 13 = yellow | Owner ruling #1, *"definitive"* |
| **3** | **`D-043`, this entry** | **13** | **5** | **5 = yellow, 13 = red** | Owner ruling #2, correcting ruling #1 |

**On periods, state 3 is state 1.** The project's original assignment was right, `D-041`
overturned it, and it is now restored. The colours are genuinely new — state 1 had none — so this
is **not** a clean revert, and treating it as one would lose `D-042`'s three `[TOOLING]`-corroborated
rows and the V07 corroboration that state 1 never had.

**`D-041` drew a headline lesson from the inversion, and that lesson is false as written.** It
said, in `A-020`, in §5.16 and in §3.4, that Tier 3 convergence had been *"wrong on a point where
it was internally coherent, cross-source consistent, and agreed with the project's own inference
from V06"*, and called it *"the single best-calibrated warning this project has yet produced
against `EXTERNAL_VOCABULARY_REFERENCE.md` §5"* and *"the receipt"* for `D-030`. **§5.16's table
was right on the two rows in question.** Every place that claim is printed is superseded by this
entry and annotated in place.

**The correct lesson is a different one, and it is stronger, not weaker:**

- **`D-030` and §1.3 are NOT vindicated by this and are NOT retired by it either.** §5.16's three
  sources are still very probably **one document quoted three times**; their unanimity was never
  independent corroboration, and it still is not. **Being right once does not make a method
  reliable** any more than being wrong once made it worthless. Tier 3 stays non-normative, stays
  `DO NOT CODE` as a closure route, and closes nothing (`D-040`). The §5.16 table remains a thing
  a session must not cite — it is now *accidentally* correct on two rows, which is a worse trap
  than being plainly wrong, and the banner there says so.
- **The real calibration datum is about OWNER ATTESTATION, which is where this project actually
  gets its answers.** An attestation was issued in a single sentence, marked *definitive*,
  overturned a standing record on two rows, propagated into five files and a Pine script inside a
  day, and was **wrong**. It was corrected only because `D-042` ran a search it was not strictly
  required to run, found one Tier 1 sentence that contradicted a *different* axis of the same
  mapping, and **refused to adjudicate it**. `SOURCING_HIERARCHY.md` §3.2 Case C is what caught
  this. Had `D-042` chained the inference and "fixed" it, or suppressed the finding as a mere
  colour question, the error would have stood.
- **`D-041`'s alternatives block anticipated exactly this and chose correctly.** It rejected
  querying the inversion before acting, on the grounds that the ruling was reversible if recorded
  loudly enough — *"recorded in the loudest terms this file has… so it cannot be adopted unnoticed
  and is trivially reversible if the owner reads it back and says otherwise."* **The owner has now
  read it back and said otherwise, and the reversal cost one decision entry and five annotations
  rather than an archaeology exercise.** That design worked. It is the reason this correction is
  cheap.
- **The standing re-check obligation is vindicated twice over.** `SOURCING_HIERARCHY.md` §3.4's
  *"closed on owner attestation is not closed for good"* has now been demonstrated against an
  attestation **twice in one day, in opposite directions.** `A-020` stays on that list.

**A by-product: `D-041`'s `Q-002` analysis reverses with it, and the quarantine is unaffected
either way.** `D-041` argued that against ketchup(5)/mustard(13), the fabricated `NOTES.md`
sequence — *5 Mustard, 13 Water, 50 Mayo, 200 Blueberry, 800 Raspberry* — became *"a clean
truncation from the front"*. Against the corrected order — **Mustard(5), Ketchup(13), Water(50),
Mayo(200), Blueberry(800)** — the fabricated file's **first pair is now correct** (*5 Mustard*) and
the corruption is a **mid-list drop of *Ketchup*** with everything below it slid up one rung, plus
an invented *Raspberry* tail. That is `A-020`'s **original** pre-`D-041` reading — *"the real
sequence shifted one place"* — **restored verbatim**. `D-041`'s *"gets cleaner"* by-product claim
is superseded. **`Q-002` and `Q-012` are not rehabilitated by one accidentally-correct pair**:
`raspberry` still occurs **0×** in genuine audio anywhere in the corpus, `Q-012` §2's *"50 (Mayo)"*
is still wrong, and a fabricated file that gets its first row right is still fabricated.

---

### 5. WHAT THIS DECISION DOES **NOT** DO

- **It does not reopen `C-018`.** `D-041` had two operative halves and **only the second is
  reversed here.** Half 1 — `C-018` closed as reading B, V11 `[00:46:45]`'s *"There's the
  mayonnaise. There's the 50"* is an **enumeration**, not an apposition equating mayo with 50 — is
  untouched, because it concerns the **mayo** row, which does not move. `D-041` was explicit that
  that closure *"does not rest on the owner outranking a recording"* but on the V11 session's own
  three independent grounds, with the owner supplying a disambiguation the sources left open. **A
  closure that never leaned on the attestation's infallibility is not weakened by the attestation
  turning out to be fallible elsewhere.** `C-018` stays closed on `video/v11` where it lives.
- **It does not establish a "Tier 0", and it does not demote the owner either.** Owner attestation
  remains an **adjudication warrant sitting outside the source hierarchy**, and
  `AUTOMATION_AMBIGUITIES.md`'s `STATUS VALUES` table still ranks `RESOLVED — OWNER ATTESTATION`
  as the **weakest** of its three resolved statuses. Nothing here promotes it; the fact that it
  needed correcting is an argument for that ranking, not against it.
- **It does not discharge `SOURCING_HIERARCHY.md` §3.4.** `A-020` stays on the standing re-check
  list. `D-042`'s exhaustive search remains **discharged as at V11 and live for V12 onward**; its
  **negative result is unaffected** — no Tier 1 statement attaches a period to *ketchup* or
  *mustard* anywhere in V01–V11, and that was true before this ruling and is true after it. **This
  entry changes which owner-attested numbers fill the gap, not whether the gap exists.**
- **It does not touch water, mayo or blueberry on either axis**, nor their `[TOOLING]` warrants,
  nor blueberry's `RESOLVED BY COURSE` status or its 15-minute timeframe, nor `MMM-NOTES` p.66's
  Tier 2 corroboration of mayo = 200.
- **It does not touch `C-010`.** The 800-vs-notes discrepancy is about what `MMM-NOTES` omits, not
  about which nickname carries which number.
- **It supplies no threshold and unblocks no rule.** `A-020`'s surviving cautions stand: *"enough
  distance between the entry and the mayonnaise"* (V02 `[00:19:46]`) is still an undefined
  viability filter `D-030` forbids numbering, and `[00:05:00]`'s *"manays"* is still PROBABLE.
- **It changes no mastery grade and no review verdict**, and it corrects no completed review
  artifact. See §6.

---

### 6. DOWNSTREAM ARTIFACTS THAT ARE NOW STALE — FLAGGED, NOT EDITED

Completed review artifacts are not retro-edited (`REMEDIATION_PROTOCOL.md` §3.9 — *"`R1` is never
edited"*). Three are affected and are recorded here for the owner and for the next reviewer:

| Artifact | What is now stale | Disposition |
|---|---|---|
| `18_REVIEW/V11/V11_REVIEW_R1.md` § `N1` (item 114) and § REQUIRED CORRECTIONS item 3 | The reviewer **declined** `D-041` consequence 7's invitation to put the inversion back to the owner, and characterised `D-042` §3's V07 conflict as *"a question about COLOURS, not about the period mapping this review checked"*. **The colour conflict did in fact reach the period mapping** — it is the thread the owner pulled to reverse `D-041`. | **No correction owed and no fault charged.** The reviewer's *factual* work is untouched and remains correct: the body-only V01–V11 census (`ketchup` 0×, V04's two numberless `mustard` uses, V01 `[00:19:24]`'s garble) is **verified and unaffected** — the corpus still says nothing, which is precisely why an owner ruling was the only thing that could move this. The declined escalation was reasonable on what was in front of it, and the reviewer **explicitly recorded the V07 conflict rather than sweeping it past**, which is why it survived to be answered. The stale part is one *characterisation*, not a finding, a number or a verdict. **A note is owed in `REVIEW_INDEX.md` item 114, not an edit to `V11_REVIEW_R1.md`.** |
| `18_REVIEW/REVIEW_INDEX.md` item 97 (V11 student) | Its closing line reads *"⚠ The same ruling **overturned `A-020`'s ketchup/mustard rows** (now **ketchup = 5, mustard = 13**…)"*. | Stale. **Index rows are the live tracking surface, not a frozen review artifact** — a superseding note is appropriate here. Flagged for the owner rather than applied in this session, since items 109–113 are already owed against this index. |
| `18_REVIEW/V09/V09_REVIEW_R1.md` line ~290 | States the attested set as *"mustard 5, ketchup 13, water 50, mayo 200, blueberry 800"*. | **This was correct when written, was made stale by `D-041`, and is now correct again.** No action. Recorded because a session auditing for `D-041` staleness would have flagged it, and must now un-flag it. Its surrounding arithmetic (the 800×15m = 200×60m factor-of-four argument) never depended on the ketchup/mustard rows at all. |

`LOG.md`, `00_SYSTEM/QUARANTINE_REGISTER.md`, `00_SYSTEM/COURSE_PROGRESS.md` and
`03_LESSON_NOTES/V09_SOURCE_NOTES.md` also carry the nicknames. **None states a ketchup or mustard
period as a live fact** — they are narrative records of what happened on a date, and a dated record
of a ruling that was later reversed is **correct as a record**. They are not annotated, and that is
deliberate: annotating history for having been history is how an audit trail gets destroyed.

---

**Reason:** `I-011` asked the owner a question that only the owner could answer, and the owner
answered it. Recording that answer as an edit to `D-041` or `D-042` was forbidden twice over
(`DECISIONS.md` append-only; `REMEDIATION_PROTOCOL.md` §2), and recording it *without* separating
the two axes it moves would have propagated a half-correction into the Pine script and three
ledgers — the nickname↔colour pairing is unchanged and looks like the thing being corrected, which
is a trap laid by the shape of the owner's own sentence. Beyond the mapping, `D-041` printed a
confident calibration lesson against Tier 3 in three files, and that lesson is now known to be
drawn from a false premise; leaving it standing would mis-train every session that reads it.

**Evidence:** Owner attestation, 2026-08-13, verbatim in the header — issued in direct response to
`I-011`'s stated question, under the same `D-039` warrant as the owner-attested closures of
`A-014`, `A-020` and `A-023`. **Tier 1 corroboration on 5 = yellow:** V07 `[00:25:34]`, frame
`04_SCREENSHOTS/V07/INDEX.md` row 22 — `GUEST`, normative under `D-033`, and the only place in
V01–V11 where a speaker joins a colour to a period in one sentence. **`[TOOLING]` corroboration on
50/200/800 colours, carried forward unchanged from `D-042` §2:** `3M-shadow-boxes-15M.tpl`, decoded
in `06_MANUAL_BACKTEST/tools/MMM_Indicator_README.md` (`feature/tradingview-mmm-indicator`).
**Tier 3 agreement on the restored periods:** `EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 and its
three cited web sources (mustard = 5, ketchup = 13) — **noted, non-normative, closes nothing**
(`D-040`), and see §4 for why this is not a rehabilitation of that table. **Negative search result,
unchanged and still governing:** `D-042` §1 — no Tier 1 statement attaches a period to *ketchup* or
*mustard* anywhere in V01–V11, independently re-verified by the V11 R1 reviewer (`N1`).

**Alternatives considered:** *Editing `D-041` and `D-042` in place, since they are now known to be
wrong* — rejected outright; `DECISIONS.md` is append-only and `REMEDIATION_PROTOCOL.md` §2 requires
superseded text retained and marked, and the two-reversals-in-one-day sequence is itself the most
instructive thing in this record. *Recording this as a reversal of the nickname↔**colour** pairing,
which is how the owner's sentence and the raising instruction both frame it* — **rejected on the
evidence, and this was the live trap**: ketchup = red and mustard = yellow **before and after**, so
correcting that axis would have changed nothing while leaving both real errors — the periods and
the period↔colour assignment — in place in the Pine script and three ledgers. §2 exists to stop
that. *Treating the V07 agreement as promoting the mapping to `RESOLVED BY COURSE`* — rejected; the
nickname↔period join is still a two-warrant chain no speaker makes, and adopting a chain because it
now points the convenient way is the same `D-030` error `D-042` §3 correctly refused when it
pointed the inconvenient way. **The reasoning must not be run in one direction only.**
*Downgrading blueberry to owner attestation for table consistency* — rejected for the same reason
`D-041` rejected it. *Retro-editing `V11_REVIEW_R1.md`'s now-stale characterisation* — rejected;
`R1` is never edited (`REMEDIATION_PROTOCOL.md` §3.9), the reviewer's findings and census are
unaffected, and the review's own recording of the conflict is what made this correction possible.
*Deferring the Pine change until a legend is observed on-screen* — rejected; the script already
ships owner-attested colours under `D-042` consequence 6, and shipping the **superseded** pair
while a corrected one exists is strictly worse than shipping the corrected one under the same
warrant.

**Consequences:**

1. **`D-041` and `D-042` remain on the record, unedited, `ACTIVE` as historical entries, and are
   annotated as superseded in part by this one.** `D-041`'s `C-018` closure and `D-042`'s §1
   search result and §2 50/200/800 rows all stand.
2. **`A-020` gains a third annotation block** recording ruling #2, the restored periods, the
   corrected colours and the V07 agreement. Its two earlier blocks (`D-041`'s ⛔ SUPERSEDED IN PART
   and `D-042`'s 🎨 COLOURS) are **retained unedited** — the record now carries all three states in
   sequence and a session can read the history off the file (`REMEDIATION_PROTOCOL.md` §2).
3. **`EXTERNAL_VOCABULARY_REFERENCE.md` §5.16's banner is corrected**, including the withdrawal of
   its *"Tier 3 was unanimous and it was wrong"* claim, which is false. The Tier 3 table below it
   stays **non-normative and uncitable** — now on the stronger ground that an accidentally-correct
   source is a worse trap than a plainly wrong one.
4. **`SOURCING_HIERARCHY.md` §3.4 gains a third dated update block** carrying the final mapping,
   and the obligation on `A-020` **stays live for V12 onward**.
5. **`SETUP_ISSUES.md` `I-011` is CLOSED** `RESOLVED — OWNER ATTESTATION`, against this entry, with
   the note that the ruling agrees with the V07 tape.
6. **The Pine tool swaps two colour constants** on `feature/tradingview-mmm-indicator` — 5-period
   EMA → **yellow**, 13-period EMA → **red** — with their nickname labels following the periods,
   the comment block rewritten to cite `D-043`, and the V07 conflict note **replaced by a V07
   corroboration note** on the 5. 50/200/800 unchanged. **The branch is not merged.**
7. **Any artifact citing either axis must cite this entry and the warrant.** *"Mustard (5 EMA,
   yellow, `OWNER-ATTESTED`, `D-043`; colour corroborated by V07 `[00:25:34]`)"* and *"Ketchup
   (13 EMA, red, `OWNER-ATTESTED`, `D-043`)"*. **Never** *"the red ketchup 5 EMA"* — that phrasing
   is now wrong twice, and it is the exact string a session will copy from `D-041`.
8. **The next free identifier is `D-044`.** `feature/tradingview-mmm-indicator` still carries
   `06_MANUAL_BACKTEST/tools/DRAFT_D-041_platform_artifacts.md`, whose reserved number was taken on
   integration; that collision is unchanged by this entry and is still the adopting session's to
   renumber (`D-042` §4, `D-038a` consequence 1).

**Status:** ACTIVE — **AUTHORITATIVE. Supersedes `D-041`'s ketchup/mustard rows and `D-042` §2's
5/13 rows on both axes.** `I-011` CLOSED against it.

---

## D-044 — The corpus is EXTENDED to 2017-2025 for forward-testing and backtesting; `D-035`'s 2013-2016 split is untouched and the 2016H2 holdout stays sealed

**Date:** 2026-08-14
**Owner decision, given in session:** *"This can be used to forward test and backtest. Pull
2017-2025 if that's easiest."* · *"We can do some verification or have the student do it"*
(on re-measuring the format/clock past 2016) · *"I don't plan on redistributing"* (closing the
redistribution caveat `HISTDATA_RECENCY_CHECK.md` §4.4 left open).
**Extends:** `D-036a`'s HistData corpus, by adding data. **Amends nothing in it.**
**Adds a usage policy for a date range `D-035` had classified one way and the owner has now
classified another.** See §2, which states precisely what moved and what did not.
**Executes the feasibility finding in** `06_MANUAL_BACKTEST/datasets/HISTDATA_RECENCY_CHECK.md`
(2026-08-14), which established that the free tier serves 2016H2-2025 and authorised nothing.

---

### 1. WHAT WAS PULLED

| Field | Value |
|---|---|
| Source | **HistData.com**, free tier, no account — the `D-036a` vendor, the `D-036a` `get.php` method, unchanged |
| Product | `MetaTrader` format, **M1 bid bars**, GBP/USD |
| Files | `DAT_MT_GBPUSD_M1_{2017…2025}.csv` — **nine full-year files** |
| Retrieved | **2026-08-14**, HTTP POST to the public `get.php` form endpoint |
| Integrity | **SHA-256 per file**, `datasets/HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt` (the four `D-036a` hashes in it are **unchanged**) |
| Span as served | **2017-01-02 02:00 → 2025-12-31 16:57** |
| Rows as served | **3,297,475** · **3,297,055** after the §4 de-duplication |
| Corpus now on disk | **13 files, 4,594,836 M1 bars**, 2013-01-01 17:00 → 2025-12-31 16:57 |

**2016H2 WAS NOT PULLED, AND PULLING 2017 DID NOT REQUIRE IT.** `HISTDATA_RECENCY_CHECK.md`
§4.1 warned that the vendor sells past years whole, so 2016H2 is unreachable without the
2016 file and its holdout. That warning is about the **2016** file and does not reach 2017:
each year is an independent download, and 2017 was retrieved on its own with no 2016 request
issued. **`DAT_MT_GBPUSD_M1_2016H1.csv` was never re-fetched, re-read or rewritten** — its
SHA-256 is byte-identical to the one `D-036a` recorded.

### 2. WHAT THIS CHANGES ABOUT `D-035`, STATED PRECISELY

`D-035` is **NOT superseded, NOT reopened, and NOT reinterpreted.** Its ratio, its arithmetic,
its 2016-07-01 boundary and every conformance verdict it issued stand exactly as written. What
this entry does is record an **owner ruling on how one part of its HOLDOUT block, plus a range
lying entirely outside its corpus, may now be used.**

`D-035`'s corpus was `2013-01-06 → 2017-12-29` split at `2016-07-01`. The extension range
therefore lands in **two different relationships to it**, and conflating them is the error this
section exists to prevent:

| Range | Relationship to `D-035` | Status after this entry |
|---|---|---|
| **2013-01-06 → 2016-06-30** (1,272 d) | `D-035` DEVELOPMENT | **UNCHANGED.** Development, exactly as before. Not on this entry's account in any way. |
| **2016-07-01 → 2016-12-31** (184 d) | `D-035` HOLDOUT | **UNCHANGED — STILL SEALED.** Not pulled, not on disk, never read. The owner said *"2017-2025 if that's easiest"*, and it was. |
| **2017-01-01 → 2017-12-29** (362 d) | `D-035` HOLDOUT | **RELEASED FOR USE** by the ruling above. No longer a sealed pre-registration holdout. |
| **2017-12-30 → 2025-12-31** (2,924 d) | **Outside `D-035`'s corpus entirely** — beyond its `T1`. Never was development, never was holdout. | **AVAILABLE.** `D-035` says nothing about it and never did; this entry is the first to classify it at all. |

`184 + 362 = 546`, which is `D-035`'s HOLDOUT day count on its own difference convention. So
**exactly two thirds of the `D-035` holdout is released and one third remains sealed**, and the
sealed third is the part the corpus never held.

**THE COST OF THE RELEASE, STATED BEFORE IT CAN BE DISCOVERED LATER.** A holdout is worth what
it is worth because nothing has been fitted to it. `2017-01-01 → 2017-12-29` was a clean,
never-inspected 362-day out-of-sample block, and after this entry **it is not one, and cannot
be made one again.** That is a real loss and it is the owner's to accept; it is recorded here
so that no later session cites 2017 as out-of-sample evidence on the strength of `D-035`.
**`2016-07-01 → 2016-12-31` remains the project's only intact `D-035` holdout**, and it now
carries the whole of that role — including the **October 2016 flash crash** (`D-035`
consequence 3), which stays out of reach of the Student Phase.

**WHAT WAS ALREADY TESTED IS UNAFFECTED.** Every `PT` result committed before this entry was
measured on `W-A`, `W-B` or `W-C′`, all of which end on or before 2016-06-30. Verified rather
than asserted — see §6.

### 3. THE FORMAT AND CLOCK WERE RE-MEASURED, NOT ASSUMED — AND THEY DO NOT FULLY MATCH

`HISTDATA_RECENCY_CHECK.md` §4.2 recorded the column layout, the fixed clock, the zero volume
field and the week-open convention as **2013-2016 facts expected to hold, never checked on a
single post-2016 bar**, and `D-034` makes the clock probe mandatory. It was run on all nine
files, with the `D-036a` corpus as a control.

**HOLDS, on all nine years:**

| Fact | Result |
|---|---|
| Column layout `YYYY.MM.DD,HH:MM,O,H,L,C,V` | ✅ 3,297,475 / 3,297,475 rows |
| Quotes 6 d.p., positive | ✅ zero exceptions |
| **Volume structurally zero** | ✅ zero non-zero values. Still **not traded volume; no test may read it** |
| OHLC coherence (`C4`) | ✅ PASS |
| **Week open at stamp 17:00, no seasonal shift** | ✅ modal open is **17h in all twelve months**, pooled over 465 week opens |

> The **per-year** form of that last measurement says the opposite, and it is wrong. A year
> holds ~52 week opens, so a month holds ~4, and the modal open of 4 samples is decided by a
> minute of jitter — every year "shifts". Pooled (~39 per month) the answer is unambiguous.
> Recorded because the flawed version was run first and would have been a false alarm.

**DOES NOT HOLD — two differences, both absent from 2013-2018 and both dated to a vendor
pipeline change in 2019:**

1. **A DUPLICATED HOUR ON THE EU FALL-BACK SUNDAY.** The 60 minutes `19:00`-`19:59` are emitted
   **twice** on 2019-10-27, 2020-10-25, 2021-10-31, 2022-10-30, 2023-10-29, 2024-10-27 and
   2025-10-26 — **420 rows**. `D-036a`'s corpus has **zero** duplicate stamps in 1,297,781 rows,
   and so do 2017 and 2018. **This fails `C2` and `C3`, which are GATING checks.** Disposition
   in §4.
2. **OFF-HOUR WEEK OPENS IN THE US/EU DST-DISAGREEMENT WINDOWS.** 23 week opens sit at 16h
   instead of 17h, every one of them in the three March Sundays where the US is on DST and the
   EU is not, or the October Sunday where the EU is off and the US is not. The `D-036a` corpus
   has **0 of 181** off-hour opens; 2017 and 2018 have none either. **Any week-boundary claim
   inheriting `W-C′`'s 17:00 week open BY NAME (`D-034` fact 1, `D-036a`) does not automatically
   inherit it for 2019+**, and must state which convention it used.

**A THIRD FINDING, NOT A CLOCK FACT: 2023 IS MATERIALLY DEGRADED.** 322,467 bars against a
~372,000 median — **~13% light** — with the loss concentrated in **2023-02-26 → 2023-07-23**
(April is 36% down). Its gap census is **672 intra-week gaps totalling 32 d 15 h**, against
**≤ 7 gaps and ≤ 7 h for every other year in the corpus, old or new.** The remaining 16
off-hour week opens are all in this block, at 18h/19h. For scale: `D-036a` flagged a **22-hour**
hole (`2014-06-01`) as the corpus's one unexplained absence and required every test spanning it
to exclude it by name. **2023 is that defect roughly thirty-five times over.**
**`2023-02-26 → 2023-07-23` must carry an explicit pre-registered disposition in any test that
spans it, and the honest default is to exclude the block and say so.**

### 4. THE DUPLICATED HOUR — DISPOSITION

**Nothing is normalised silently, and the raw files are not edited.** The nine CSVs on disk are
byte-for-byte as the vendor served them and still match `raw/SHA256SUMS.txt`.

The repair is admissible for one reason and only that reason: **in all 420 cases the two rows
are IDENTICAL in open, high, low and close.** Nothing is being chosen between; one emission is
a copy of the other. So `mmm_lib._dedupe_exact()` and `aggregate_m15.dedupe_exact()` drop the
second copy, **report the count and the dates**, and **refuse to run** — rather than guessing —
if a duplicated stamp is ever found carrying a *different* bar, which is what a genuine
folded-back hour would look like.

**Both QA reports are committed, and one of them fails:**

| Report | Scope | Gate |
|---|---|---|
| `QA_REPORT.txt` | `D-035` DEVELOPMENT, 2013-2016 | **PASS** — unchanged from `D-036a`, every check identical |
| `QA_REPORT_EXT_RAW.txt` | 2017-2025 **as served** | **FAIL** — `C2` 420, `C3` 420. Kept as the honest record of the vendor's output |
| `QA_REPORT_EXT.txt` | 2017-2025 **as consumed**, post-de-duplication | **PASS** — `C1`-`C4` clean, 3,297,055 bars |

Gating only on the repaired report would hide the defect; gating only on the raw one would
block a corpus whose sole gating defect is 420 rows the vendor sent twice. **Both, committed.**

### 5. `C5`-`C8` HUMAN-JUDGEMENT REVIEW, FOR THE NEW YEARS

- **`C5` spikes — 2,042 flagged, nothing excluded.** The extremes are Christmas-Eve thin-book
  bars (2019-12-24 at ×216 of a 0.1-pip local median), i.e. the ratio is inflated by a near-zero
  denominator, not by a large numerator — 21.6 pips is not a corrupt tick. `D-036a`'s rule
  stands: **a news bar and a bad tick are indistinguishable to a threshold, so nothing is
  auto-excluded.**
- **`C6` gaps — 691 ≥ 30 min.** **672 of them are 2023.** Excluding that block the nine years
  total 19 gaps, comparable to the control corpus's 3.
- **`C7` week opens — 465 Sunday-delimited, 15 intra-week re-opens, 3 non-Friday weeks**
  (`2020-12-27`, `2023-04-02`, `2025-12-28`). Re-opens are **never** week boundaries — the
  `D-036a` correction applies verbatim.
- **`C8` sessions — 24 below 60% of nominal.** 15 are Dec/Jan closures, real. **Nine are not
  and are named here so no session has to rediscover them:** `2019-05-26` (absent),
  `2019-05-27`, `2020-11-30` (300 bars), `2021-05-31` (239 bars), `2023-03-17`, `2023-03-24`,
  `2023-04-06`, `2023-04-07` (absent), and the `2023-02-26 → 2023-07-23` block they sit in.
  The three May/November entries coincide with US Memorial Day / UK bank holidays; that is an
  explanation, not a clearance, and the `D-036a` rule stands — **a partial session cannot
  support a full-window measurement whether the cause is a defect or a real closure.**

### 6. NO COMMITTED `PT` RESULT MOVED — MEASURED, NOT ASSERTED

The extension broke an assumption ten runners relied on without stating it: that *"load the
corpus"* and *"load DEVELOPMENT"* were the same act, true only because `D-036a` had truncated
2016 on arrival. `PT-025`…`PT-032`, `PT-036` and `PT-039` derive their bar universe from the
whole corpus and then call `assert_development()` on it; unchanged, all ten would have raised
**HOLDOUT BREACH** on the first run after this entry.

**The fix makes the coupling explicit rather than redefining anything.** `mmm_lib.load_m1()`
and `load_m15()` now take a **scope** and **default to DEVELOPMENT** — precisely what every
existing runner was already getting. Reaching the `D-044` years requires naming them.
`SCOPES["development"]` is `D-035`'s block unchanged to the minute and `assert_development()`
is untouched.

**Verification: all 25 `run_ptNNN.py` scripts were re-run against the 13-file corpus. Every one
of the 27 committed `*_results.json` and every committed `*_report.txt` is BYTE-IDENTICAL.**
`git status` reports no change under `06_MANUAL_BACKTEST/V01…V13/`.

**One near-miss, recorded because it is the exact failure this entry could most easily have
caused.** The first draft clipped the scope on the **arm's own clock**, which looks more
principled and is a silent redefinition: under Arm B the `+1h` DST shift relabels the last four
development M15 bars to wall-clock 2016-07-01 (`I-010` Q2), so an arm-clock clip drops them and
**Arm-B DEVELOPMENT quietly becomes 86,820 M15 bars where `D-036a` committed 86,824** — moving
a boundary governed by an **open owner question**, while adding data unrelated to it.
`verify_against_committed("B")` caught it on row count. The clip is applied on the **raw file
clock**, both arms return 86,824, and **`I-010` Q2 is exactly as open as it was.**

### 7. THE THREE CODE HAZARDS, FIXED

1. **`_dst_intervals()` was `range(2012, 2018)`.** Not an error for a corpus ending in 2016;
   **silently wrong** the moment 2017-2025 arrived. Every Arm-B bar from 2018 on would have
   fallen through with `dst` False — **Arm B would have become Arm A for eight years and gone
   on reporting itself as Arm B.** No exception, no warning. Now derived from
   `CORPUS_YEAR_MIN/MAX` with a year of margin: **15 transition pairs, 2012-03-11 → 2026-11-01.**
2. **The M1 parse cache was keyed on nothing.** `m1_raw_v2.npz` was reused whenever it existed,
   so adding nine files would have served a stale parse of a corpus that no longer existed, with
   correct-looking bar counts. Now `m1_raw_v3.npz`, keyed on a `(name, size, mtime_ns)`
   fingerprint of the whole raw file set. *(A first draft stored the de-dup census as a numpy
   `U10` column, which truncated every date and round-tripped nonsense **out of the cache while
   the fresh-parse path was correct** — a cache returning a plausible wrong answer. Fixed and
   recorded rather than quietly repaired.)*
3. **`verify_against_committed()`'s row count.** `GBPUSD_M15_ARM{A,B}.csv` **remain
   DEVELOPMENT-scope files** — 86,824 bars, byte-identical to `D-036a`'s. Rebuilding them over
   the extended corpus would have failed the row-count arm against every runner, and the honest
   reading of that failure is *the reference moved*, not *the module drifted*. **So the
   reference does not move**, and `D-044`'s bars live separately under `derived_ext/`. Both arms
   verify `ts=True px=True`.

### 8. M15 AND H1 DERIVED FOR THE EXTENDED RANGE

Built by the project's own committed `aggregate_m15.py` — the `D-036a` / unmerged
`feature/m15-h1-chart-backtest` pattern, unchanged in rule: **open of the first M1 bar in the
bucket, high = max, low = min, close of the last; a bucket is emitted only if at least one M1
bar falls inside it**, so holidays and weekends stay absent rather than becoming flat synthetic
candles. **The bucket boundaries are ours** and that is deliberate (`D-031` makes the boundary
the tested variable); the vendor publishes no M15 or H1 at all.

| File (`datasets/HISTDATA_GBPUSD_M1/derived_ext/`) | Bars | Span |
|---|---|---|
| `GBPUSD_M15_ARM{A,B}.csv` | **307,576** per arm | 2013-01-01 17:00 → 2025-12-31 16:45 |
| `GBPUSD_H1_ARM{A,B}.csv` | **76,901** per arm | 2013-01-01 17:00 → 2025-12-31 16:00 |

Continuous 2013-2025, **not** 2017-2025 — a chart series with a hole where the development
corpus ends would be worse than useless for the study this data was pulled for, and the
development/extension distinction is enforced in code, not by which file a bar sits in.
Hashes in `derived_ext/SHA256SUMS.txt`. **Two independent implementations agree**:
`aggregate_m15.py` (dict-wise) and `mmm_lib.resample()` (numpy/pandas) return 307,576 and
76,901 for both arms. `aggregate_m15.py` gains `--from` / `--to` because the span used to be
decided by whatever the directory happened to hold; run with `--to 2016-06-30` it reproduces
both committed development M15 files at **identical SHA-256**.

### 9. WHAT IS STILL OWED

- **`I-010` Q2** — which arm's clock the `D-035` boundary is stated in — is **still an open
  owner call** and this entry deliberately does not settle it.
- **The 2019+ off-hour week opens (§3.2) mean `W-C′`'s 17:00 week open does not carry forward
  by name.** Any test using 2019-2025 week boundaries must state its convention.
- **`2023-02-26 → 2023-07-23` needs a pre-registered disposition** in any test spanning it.
- **The `2014-06-01` hole and the `D-034` cross-vendor level caveat are unaffected** and still
  stand. Price levels remain **not comparable** with the V02-V06 FXCM homework.
- **No `PT` is re-issued, re-scoped or unblocked by this entry.** It supplies data and a usage
  policy, not conformance. A test wanting the `D-044` years is a **new pre-registration**.
- **The 2026 partial year was not pulled** and remains subject to `HISTDATA_RECENCY_CHECK.md`
  §4.3 — it moves between fetches and must not be treated as stable.

**Reason:** `HISTDATA_RECENCY_CHECK.md` established the data was reachable and explicitly
authorised nothing, listing a new owner decision as the first thing owed. The owner gave one.
Recording it as a new entry rather than an append to `D-035` is the whole point: `D-035` pinned
a split *"final"* by explicit owner decision and its verdicts are cited across the batch, so
editing it to fit new data would be exactly the selection pressure `D-027` and `D-028` exist to
remove. A later ruling that **releases part of a holdout** is a different act from **moving a
boundary**, and only the first one happened.
**Evidence:** `datasets/HISTDATA_RECENCY_CHECK.md` (all sections); `raw/SHA256SUMS.txt`;
`QA_REPORT.txt`, `QA_REPORT_EXT_RAW.txt`, `QA_REPORT_EXT.txt`;
`derived_ext/SHA256SUMS.txt`; `datasets/HISTDATA_GBPUSD_M1/README.md`; `D-034` (fact 1, the
mandatory clock probe), `D-035`, `D-036`, `D-036a`, `D-031`, `I-010`.
**Alternatives considered:** *Amending `D-035` to move the boundary to 2026* — **rejected, and
this is the important one.** It would retroactively reclassify a block against which
conformance verdicts have already been issued, and it is indistinguishable from moving a
holdout to suit the data. *Pulling 2016H2 as well, for a continuous series* — rejected; the
owner scoped the pull to 2017-2025, it would have required downloading the whole 2016 file
including the sealed block, and `D-036a`'s truncate-on-arrival rule exists precisely to stop
that being done casually. *Editing the raw CSVs to remove the 420 duplicated rows* — rejected;
it breaks the vendor checksums and destroys the evidence that the defect exists. *Rebuilding
`GBPUSD_M15_ARM{A,B}.csv` over the extended corpus* — rejected; §7.3. *Letting the ten
whole-corpus runners keep meaning "whatever is in the directory"* — rejected; that is how a
holdout gets read by accident.
**Status:** ACTIVE

---

## D-045 — The owner's `!SM_TDI` MT4 template is admitted as a NEW TIERED EVIDENCE CLASS, and `A-084` closes PROVISIONALLY at k = 2

**Date:** 2026-08-14
**Decision:** Two parts, and the second does not follow from the first without it.

**Part 1 — the evidence class.** The owner's own MT4 platform artifacts, supplied by the owner and
attested by the owner as his working configuration for this method, are admitted as a named
evidence class: **`TOOLING — OWNER-ATTESTED PLATFORM ARTIFACT`**. It ranks **below Tier 1 and above
`[DEFAULT]`** in `SOURCING_HIERARCHY.md`, exactly as `D-042` already does for owner colour
attestations. Admission is **per-artifact**, as `D-039` is per-document: this entry admits
`Ultimate Blue.tpl` / `!SM_TDI` (md5 `ea22c8cf527921cef072586b6fa28296`) and nothing else.
A citation from this class carries the tag **`[TOOLING]`** with the artifact name.

**Part 2 — what it closes, and how weakly.** `RSI_Price_Line=2` with `RSI_Price_Type=0`
(MT4 `MODE_SMA`) states that the plotted green line is `SMA(2)` of `RSI(21)`. **`A-084` closes
`PROVISIONALLY RESOLVED — TOOLING` at `k = 2`**, and the closure carries, in the record itself,
the weakness in Part 3. `A-084`'s `ACTIVE BLOCKER` status is lifted **to the extent of `k`, and no
further**: V11's RSI threshold family (the 50 bias baseline, 80/40, 60/20, 80/20, the 38–42
pullback band, both divergence forms, the `[00:36:19]` composite) is unblocked **as against
`A-084`** and remains subject to every other blocker it carries.

**Part 3 — the weakness, stated at the closure and not glossed.** The template is dated **2016 and
2019**; the course was recorded in **2012**. V13 frame `00:53:35` — a 2012, Tier-1,
instructor's-own-chart datum — carries the template's **non-default** `63`/`37` pair, and the audio
ties `37` to the shark fin (`[00:51:09]`); the public Dean Malone TDI ships 68/50/32, so this is
**not** the public default. `RSI_Period=21` matches `A-080`'s Tier-1 closure exactly. **But
`RSI_Price_Line=2` — the one field that answers `A-084` — is NOT among the corroborated fields.**
The corroboration establishes that the template is of this lineage and plausibly this
instructor's; it does not establish the load-bearing value. Any artifact relying on `k = 2` cites
this decision and inherits this paragraph.

**Reason:** `A-084` is an `ACTIVE BLOCKER` on a *required* entry criterion the course has never
taught (`A-039`), and three lessons have now attacked it by three routes and failed. The legend
route is closed corpus-wide; 2,047 frames across V12–V14 contain no properties dialog; and
`A-093` shows the spoken route is structurally weak rather than merely untried — the speaker
answers what the indicator feels like, never what it computes. `PT-040` measured the cost of
guessing at **10.481 pp** at `k = 5, t = 50` and **5.16 pp** at `k = 2`, concentrated at `t = 50`,
V11's bias baseline. Waiting is not free and is not likely to work; and a fourth possibility —
smoothing outside the swept simple-MA family — would make even `PT-040`'s `M` the wrong quantity,
which the template answers and waiting does not.

**Evidence:** `06_MANUAL_BACKTEST/tools/MMM_TDI.txt` and `Ultimate Blue.tpl` (branch
`feature/tradingview-mmm-indicator`, **unmerged** — re-verify against the merged tree before
citing); V13 frame `00:53:35` and `[00:51:09]`; `A-080`; `PT-040` and its pre-registered
2 pp / 5 pp decision rule; `A-084`, `A-087`, `A-093`; `REVIEW_INDEX.md` item 157 (V13 R1 `N2`);
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §3. Owner attestation, 2026-08-14, that the template is his
own working configuration for this method.

**Alternatives considered:** *Admitting it at full weight and closing `A-084` outright* — rejected;
the dating gap is real and the corroborated fields are not the load-bearing field, so a
non-provisional closure would assert more than the evidence carries. *Continuing to wait for a
course-verified answer* — rejected on the record above; two of the three remaining routes are
empirically dead and the third is structurally weak, and the cost is up to seven more lessons with
a low prior. *Admitting the artifact without giving the class a tier* — rejected; an untiered
admission is re-litigated by the next artifact, which is the failure `D-040` was written to end.
*Closing `A-086`'s band period on `Volatility_Band=34` in this entry* — **rejected, and this is the
`D-039` caution repeated: admitting a source is not reading it against a record.** `A-086` is
**eligible** and is not closed here; a session that does the reading closes it, or does not.

**Consequences:**

1. `SOURCING_HIERARCHY.md` gains the `TOOLING` rung, its per-artifact admission rule, and a
   pointer to this entry. `EXTERNAL_REFERENCE/README.md`'s default is untouched.
2. **`A-084` moves to `PROVISIONALLY RESOLVED — TOOLING`, `k = 2`**, with Part 3 quoted in the
   record. It does **not** become `RESOLVED BY COURSE`.
3. **The re-check obligation of `SOURCING_HIERARCHY.md` §3.4 attaches to `A-084`**, and `A-084`
   joins `A-014`, `A-023` and `A-020` on that list. **A later Tier 1 statement overturns this
   under `D-040` §3.1**, and any session reaching a lesson that shows a TDI properties dialog,
   a Navigator panel or a smoothing length must run §3.1.
4. **`A-086` (`Volatility_Band=34`) and `A-032` (63/37) become ELIGIBLE and are NOT closed here.**
   Each needs a session that reads the artifact against the record and cites it.
5. **Nothing else is unblocked.** `A-085` is a mechanism claim with no construction and is
   untouched. `A-039` stays open on the TDI as a taught entry criterion. `D-030` is untouched.
6. Every `PT` or `BT` artifact that uses `k = 2` states in its own pre-registration that the value
   is `TOOLING`-tier and provisional, so a later overturn is traceable to the runs it affected.

**Status:** ACTIVE — `A-084`'s closure under it is PROVISIONAL

---

## D-046 — `EXCLUDED BY DECISION` is adopted as a third mastery disposition, available to any dimension

**Date:** 2026-08-14
**Refines:** `D-018` and `D-019`, both of which remain `ACTIVE` and neither of which is superseded.
`D-019`'s two-row table becomes three rows.
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **36**, ruled at V05 R1 on 2026-08-11 and open
since then **only on this adoption step**.

**Decision:** A mastery dimension may be recorded as **`EXCLUDED BY DECISION`** when **all four**
hold:

| # | Condition |
|---|---|
| 1 | **Subject matter exists.** The lesson supplies material the dimension would otherwise grade. This is what separates it from `NOT APPLICABLE`. |
| 2 | **The work is permanently barred by a numbered decision in this file**, and **the decision is cited by number in the report.** An exclusion with no citable decision is not available — the disposition is `DEFERRED`, or the work is done. |
| 3 | **No future lesson can lift the bar.** This is what separates it from `DEFERRED`. Where a future lesson *could* lift it — a definition the course has not yet given — the disposition is `DEFERRED` and `D-030` governs. |
| 4 | **The record states WHAT was excluded**, specifically enough that a reader can see the size of the hole. |

**Effect:** the item **closes like `NOT APPLICABLE` and accrues no debt** — it is not carried in
`REVIEW_INDEX.md` as open research — **and, unlike `NOT APPLICABLE`, it is a positive statement
that material was withheld.** It is available to **any** dimension, not only F and G.
`EXCLUDED BY DECISION` is **not a pass**; it is a claim the reviewer audits like any other, and a
reviewer who finds the cited decision does not in fact bar the work returns `REVISE` with the
dimension reinstated.

`D-019`'s table, as amended:

| Disposition | Meaning | Effect | Who can grant it |
|---|---|---|---|
| `NOT APPLICABLE` | The lesson supplies **no subject matter** | Closed permanently | `D-018`, dimensions F and G only |
| `DEFERRED` | Subject matter exists; a prerequisite is missing and **may arrive** | Stays open, carried in `REVIEW_INDEX.md` | Any dimension |
| **`EXCLUDED BY DECISION`** | Subject matter exists; the work is **permanently barred by a numbered decision**, which is cited | Closed; **no debt accrues**; the exclusion is auditable | **Any dimension**, subject to reviewer audit |

**Reason:** V05 forced it and five later lessons have restated it. V05 states several
testable-shaped rules that are withheld by `D-025`. `NOT APPLICABLE` asserts there was never
anything there, which is false — there is an hour of it. `DEFERRED` asserts the work becomes
possible later, which is also false — no future lesson makes a V05 guest rule testable. With
neither label fitting, mastery dimension **B** has been carried un-graded or
`NOT SATISFIED WITH NO SEVERITY CHARGE` for **six-plus consecutive lessons**, and reviewers have
correctly declined to charge it, because charging it would penalise the `D-030` discipline the
project mandates. **The gap is in the project's own standards, not in any lesson's understanding.**

**Evidence:** `REVIEW_INDEX.md` item 36 and its V05 R1 ruling (2026-08-11), which **upheld** the
escalation and recommended this adoption in these terms; restatements at V06, V07 (x2), V08, V09,
V10, each *"restated, not re-counted"*; `V05_MASTERY_REPORT.md` § F, G and Escalation;
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §5b, §6 `D2`, §7a.

**Alternatives considered:** *Widening `NOT APPLICABLE`* — rejected; it makes `D-018`'s own
eligibility test false and re-creates the confusion `D-019` exists to end. *Using `DEFERRED` and
letting the debt sit forever* — rejected; a debt that can never be discharged is not a debt, it is
a permanently misleading open item. *Leaving it open* — rejected; the ruling is fourteen weeks
of escalations old and costs one sentence.

**Consequences:**

1. `MASTERY_STANDARD.md` and the mastery report template gain the third disposition and the
   four-condition test. `REVIEW_PROTOCOL.md` gains the reviewer's audit of it.
2. **V05 dimensions B and G take `EXCLUDED BY DECISION`, citing `D-025`**; **dimension F stays as
   graded** (`SUCCESS AFTER SOURCE REVIEW`) — it correctly refused `NOT APPLICABLE` because the
   assignment is partly performable and the performable part was performed.
3. **Dimension G's reason changes from *"states no testable rule"* to *"states rules excluded by
   `D-025`"***, so V06–V21 do not inherit the wrong precedent — this was the V05 R1 ruling's
   specific requirement.
4. **No grade, verdict or gate state changes by operation of this entry**, and **no lesson is
   re-reviewed on account of it.** Re-labelling a disposition is not re-grading. Where an earlier
   report used a disposition this entry would have changed, the report is annotated in place per
   `REMEDIATION_PROTOCOL.md` §2 and the superseded text stays visible.
5. **It creates no new licence to exclude.** Condition 2 is the whole guard: **no numbered
   decision, no exclusion.** A session that cannot name the decision has not found a third
   disposition, it has found work it has not done.

**Status:** ACTIVE

---

## D-047 — `D-038a`'s mergeability premise is CORRECTED: tail-appended evidence ledgers are NOT mergeable by construction, and consequences attach

**Date:** 2026-08-14
**Amends:** `D-038a`, **its stated reason only.** `D-038a`'s operative split — POLICY ledgers on
the integration branch, EVIDENCE ledgers on the task branch with the work — is **kept unchanged
and is not superseded.** `D-038` is untouched.
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **91**, policy half. The numbering instance was
discharged mechanically at merge-back (V10's items renumbered 86–90) and is not reopened.

**On the identifier.** This entry is `D-047` and not `D-038b`. The `D-038a` precedent is for an
entry that **clarifies** a rule; this one **corrects a premise the rule was justified on**, which
is a different act and deserves its own number in the main series so that a reader of `D-038a`
is sent to a peer entry rather than to a footnote on itself.

**Decision:** `D-038a`'s premise that *"evidence ledgers are append-only and their additions are
`git`-mergeable by construction"* is **false as stated, and is withdrawn.** Append-only makes a
ledger **conflict-tolerant**, not conflict-free: two branches appending to the **same tail** of the
same table produce a conflict git cannot order, and two branches allocating from the **same number
series** produce a collision git cannot see. Both have happened in this project. `D-038a`'s split
stands on its remaining and sufficient ground — **an isolated session's evidence must travel with
the work that produced it, and the alternative re-introduces the shared write path `D-038` exists
to remove** — and gains three consequences:

**Consequence A — identifier allocation is against the INTEGRATION branch.** Every project-wide
number series — `REVIEW_INDEX.md` **open-item numbers**, `A-`, `C-`, `Q-`, `PT-`, `BT-`, `I-` — is
allocated against **the latest integration branch's state**, never against the task branch alone,
and is **re-checked at merge-back**. This is what `PT-036` §0 already does for `PT` numbers; it is
now general. The merging session renumbers the later arrival and fixes its cross-references, and
**discloses the renumbering in the merge rather than absorbing it.**

**Consequence B — tail-appended ledgers merge single-threaded.** `LOG.md`,
`00_SYSTEM/COURSE_PROGRESS.md` and `18_REVIEW/REVIEW_INDEX.md` are **tail-appended** ledgers: their
additions land at the end of the same table or status block every time. Merge-back of any branch
touching them is **single-threaded** — one branch merges to integration at a time, completely,
before the next begins — which `D-038` already requires and this entry makes explicit for these
three files by name. A session that must wait, waits; it does not merge in parallel and repair
afterwards.

**Consequence C — `REVIEW_INDEX.md` merges promptly.** Unchanged from `D-038a` obligation 2 and
restated because B makes it sharper: its gate rows govern whether the next lesson may start, and a
verdict left unmerged holds a gate closed that is actually open.

**Reason:** The premise was tested and failed, and the test is direct rather than argumentative.
The `review/v10` → integration merge **conflicted in three files** — `REVIEW_INDEX.md` (3 hunks),
`LOG.md` (2 hunks), `COURSE_PROGRESS.md` (1 hunk) — **every one of them a file `D-038a` names as
mergeable.** `LOG.md`'s conflict **interleaved two session entries**, splicing the V09 R2 entry's
Decision/Files/Git/Next-Action sections into the middle of the V10 R1 entry's fenced Decision
block: a silent corruption of the project's own audit trail, caught only because a human resolved
the conflict by hand. Separately, `video/v10` allocated open items **81–85** while the integration
branch concurrently allocated **81–83** to V09 R2. `D-038a`'s own safety evidence re-derived `A-`,
`C-` and `Q-` sets after the V08 merge and **did not check open-item numbers**, which are the one
series in its list that is not mergeable by construction. **The risk grows with concurrency, and
this project runs concurrent sessions by design.**

**Evidence:** `18_REVIEW/V10/V10_REVIEW_R1.md` `M1` and its RENUMBERING DISCLOSURE; the
`review/v10` → integration merge commit's own conflict set; `REVIEW_INDEX.md` item 91;
`D-038a`'s reason paragraph and its safety-evidence paragraph; `PT-036` §0;
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §6 `D3`.

**Alternatives considered:** *Reversing `D-038a` and returning the evidence ledgers to
integration-only* — rejected on `D-038a`'s own reasoning, which this entry does not disturb:
it forces an isolated session to reach across mid-work or to defer its own records to a session
that did not do the work. *Leaving the premise in place and treating the V10 merge as bad luck* —
rejected; it happened twice in different forms and the second form corrupted a `LOG.md` entry.
*Numbering this entry `D-038b`* — rejected for the reason stated above. *Locking `REVIEW_INDEX.md`
numbering behind a tool* — **not rejected, deferred**: a validator check that no open-item number
appears twice is cheap and would enforce Consequence A mechanically. Recorded as a follow-up, not
required by this entry.

**Consequences:** `D-038a` gains a pointer to this entry; **its text is not edited**, per this
file's append-only rule. `D-038`'s merge-back paragraph gains the three named files.
`scripts/validate_project.py` may add a duplicate-open-item-number check. No branch, merge or
ledger row already made is invalidated by this entry.
**Status:** ACTIVE

---

## D-048 — TIER 1 AGAINST ITSELF: a standing tie-break ladder, and `C-021`'s disposition under it

**Date:** 2026-08-14
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **168**; and the standing gap
`SOURCING_HIERARCHY.md` §3.3 leaves open. **Part 2 does NOT resolve `C-021`** — see Part 2.
**Does not disturb:** `D-039`, `D-040`, `D-030`, `D-025`/`D-033`, or `SOURCING_HIERARCHY.md`'s
between-tier rules. This entry governs **within Tier 1 only.**

**PART 1 — THE GENERAL RULE.** Where two Tier 1 statements conflict — printed against spoken, one
lesson against another, or one sentence against another in the same hour — `SOURCING_HIERARCHY.md`
§3.3's *"the recording wins"* does not apply, because both are the recording. A session applies
this ladder **in order** and **stops at the first rung that answers**, and **records which rung
answered**:

| Rung | Test | Outcome |
|---|---|---|
| **1** | **Is one statement a demonstrable misspeak, corrected by the same speaker in the same passage?** | The correction governs. Record both; note the correction. |
| **2** | **Does one statement carry a construction and the other only a characterisation?** A statement of *how a thing is computed* outranks a statement of *what it feels like or is built upon* (`A-093`) | The constructive statement governs. |
| **3** | **Is one statement unhedged, unprompted and LATER, with the earlier one hedged, prompted or retracted under correction?** | The later unhedged statement is the speaker's **standing position** — **but this rung records a POSITION, not a FACT.** Anything closed on it closes **`PROVISIONALLY RESOLVED — TIER 1 STANDING POSITION`**, never `RESOLVED BY COURSE`, and carries the conflicting statement in the record. |
| **4** | **Anything else — including any case where the rungs disagree, or where a rung would close a load-bearing record** | **DO NOT ADJUDICATE.** File/keep the `C-xxx`, keep the record `DO NOT CODE`, and put it to the owner. Owner adjudication sits **outside** the ladder, as `D-041` established it sits outside the tiers. |

**Three hard limits, and they are what makes the ladder safe:**

1. **The ladder never produces `RESOLVED BY COURSE`.** Only an *uncontradicted* Tier 1 statement
   does. A resolved internal conflict yields a **provisional** status at best.
2. **The `C-xxx` is never deleted or downgraded.** Both statements stay on the record, visible, per
   `REMEDIATION_PROTOCOL.md` §2. **A divergence is a finding about the corpus** — the same
   principle `SOURCING_HIERARCHY.md` §3.3 already states for Tier 1 vs Tier 2.
3. **Tier 2 corroboration is a tiebreaker input, never a warrant.** Where Tier 2 agrees with one
   arm it may be **noted** at rung 3, and it does not promote the outcome above provisional —
   `D-039`'s Tier 2 cannot outrank Tier 1, so it certainly cannot arbitrate between two Tier 1
   statements. **`D-045`'s `TOOLING` class is treated the same way and for the same reason:** it
   sits below Tier 1, so it is an input at rung 2 or rung 3 and never a warrant.

**PART 2 — `C-021`, PUT THROUGH PART 1, LANDS ON RUNG 4. IT IS NOT ADJUDICATED HERE.**

The owner directed that `C-021` be resolved with `D-045` if `D-045`'s newly admitted `TOOLING`
evidence bears on it, and not otherwise. **The check was run and the artifact does not bear on it.
`C-021` therefore stays `OPEN — UNADJUDICATED` and is returned to the owner for a direct pick.**

*The ladder, rung by rung, on the record:*

- **Rung 1 — arguably answers, FOR V12.** V12 `[00:16:16]`–`[00:16:20]` is a correction accepted on
  the record (*"from the RSI line. Thank you."*). **But the corrector is unidentified and is not
  the speaker**, so this is not cleanly *"corrected by the same speaker in the same passage"*, and
  the correction may be right about the **public** Dean Malone build and wrong about **this altered
  one** (V12 `[00:07:20]` *"I've altered it or tweaked it a little bit"*). Rung 1 is **not clean.**
- **Rung 2 — does not answer.** **Neither statement is a construction.** *"Two standard deviations
  away from the market base"* and *"Bollinger bands based on the RSI line itself"* are both
  characterisations of what the band is built upon. Neither states a computation. This is `A-093`'s
  pattern exactly.
- **Rung 3 — answers, FOR V14**, and would close `A-086`'s basis
  `PROVISIONALLY RESOLVED — TIER 1 STANDING POSITION`: V14 `[00:45:09]` is later, unhedged and
  unprompted; V12's position was reached under a chat prompt and is the least confident statement
  in that lesson; and Tier 2 (`MMM-NOTES` p.45) independently agrees.
- ⭐ **RUNG 1 AND RUNG 3 POINT OPPOSITE WAYS, AND THE LADDER'S OWN RUNG 4 GOVERNS THAT CASE:**
  *"including any case where the rungs disagree."* **DO NOT ADJUDICATE.**

*⭐ THE `D-045` TOOLING CHECK, RUN IN FULL AND REPORTED WHETHER OR NOT IT HELPED:*

The `!SM_TDI` block admitted by `D-045` was read field by field against the specific question
`C-021` asks — **what the volatility bands are two standard deviations OF**:

| Field | What it states | Does it answer C-021's basis question? |
|---|---|---|
| `Volatility_Band=34` | A **lookback period**, one number, shared by the band and the base line | ❌ **No.** This is `A-086`'s *missing third quantity*, not its basis |
| `SharkFin_Upper_Level=63` / `_Lower_Level=37` | Two **static horizontal levels** | ❌ No. These are `A-032`'s thresholds and do not touch the bands |
| `RSI_Period=21`, `RSI_Price_Line=2`, `Trade_Signal_Line=7`, and both `_Type=0` | The RSI and the two MA lines | ❌ No. These build the three **line** buffers, not the bands |
| The std-dev **multiplier** | **NOT EXPOSED.** `MMM_TDI.txt` states it in terms: *"The MT4 indicator exposes NO input for it, so it is compiled into the binary and the template cannot reveal it"* | ❌ No — the field that would have to carry a basis does not exist in the artifact |
| `MM4XSF_TDI.ex4` buffer names — *"MarketBase Line"*, *"RSI Price Line"*, *"Upper/Lower VB Break"* | That a market-base buffer and an RSI-price buffer **both exist and are both plotted** | ❌ **No, and this is the important negative.** A list of buffer **names** says which lines are drawn. It does not say which series the bands are a deviation **of** — which is precisely and only what `C-021` disputes |

**The template has NO basis field.** It exposes a period and a set of levels; the one parameter
that would have to encode a basis — the deviation multiplier — is compiled into the `.ex4` and
unreadable. **So the artifact is silent on `C-021` in the same way Tier 2 is loud on it: it speaks
to a different quantity.** Reading the buffer-name list as though it settled the basis would be the
`D-039` error — treating the admission of a source as a reading of it against a record — which
`D-045`'s own alternatives paragraph forbids by name.

**What the artifact DOES bear on, kept strictly separate:** `Volatility_Band=34` is a candidate for
`A-086`'s **never-stated period**, which is the quantity that keeps the bands unconstructible. That
is `D-045` consequence 4, it makes `A-086` **eligible and not closed**, and it is **not** a `C-021`
ruling. Confusing the two would answer a question nobody asked and leave the disputed one open.

**`C-021`'s disposition, therefore:**

```text
C-021 -- OPEN. UNADJUDICATED.
D-048 rung 4 applied and RECORDED: rungs 1 and 3 disagree, rung 2 is silent, and the
D-045 TOOLING artifact was checked field-by-field and does not speak to the basis.
Both statements stand on the record. Neither is coded. A-086 stays DO NOT CODE.
OWED: a direct owner pick between V12 / V14 / neither. It is not a session's call
and this entry does not take it.
```

**AND IN EVERY CASE, WHICHEVER WAY THE OWNER LATER PICKS: NOTHING IS UNBLOCKED.** **The bands'
PERIOD is never stated in Tier 1 or Tier 2**, so `A-086` stays `DO NOT CODE`, and `A-031`
(*"blood in the water"*) and `A-032` (*"shark fin"*) stay uncomputable. **A multiplier and a basis
do not build a band without a lookback.** A ruling on Part 2 settles the record; it does not settle
the indicator. Any session that reads Part 2 as an unblock has made the `D-039` error by another
route.

**Reason:** The class has arisen **three times** — `C-017` (printed vs spoken, item 88), `C-021`
(Tier 1 vs Tier 1 one week apart), and the `D-041`/`D-043` EMA-nickname family — and has consumed
**two owner rulings and one reversal**, and `SOURCING_HIERARCHY.md` has no rule for it because it
ranks *sources*, not two things one speaker said in one hour. Both the V14 session and the V14
reviewer declined `C-021` and forwarded it unchanged, correctly, on the ground that it is neither
a session's nor a reviewer's call. **A general rule retires a recurring stoppage; ruling `C-021`
alone does not** — and the next instance is already predictable, because the corpus keeps
producing them. **That the ladder's first live application returns rung 4 rather than an answer is
not a failure of the ladder — it is the ladder working.** A tie-break scheme that always produces
a winner is not a tie-break scheme, it is a preference; rung 4 is what keeps it honest, and
`D-042`/`D-043` are the project's own demonstration that a session declining to chain an inference
is what produced the correct answer.

**Evidence:** `C-021` in full, including §4's three readings and §5's operational note; `C-017`
and `REVIEW_INDEX.md` item 88; `D-041`, `D-042`, `D-043` and the reversal between them;
`SOURCING_HIERARCHY.md` §3.2 Case C and §3.3; `A-086`, `A-093`; `D-045` and, for the Part 2 check,
the verbatim `!SM_TDI` template block and the `MM4XSF_TDI.ex4` string list as recorded in
`06_MANUAL_BACKTEST/tools/MMM_TDI.txt` (branch `feature/tradingview-mmm-indicator`, **unmerged** —
re-verify against the merged tree before citing);
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §1d, §6 `D4`.

**Alternatives considered:** *Ruling `C-021` and nothing more* — rejected; it is the third instance
and would leave the fourth to another owner session. *Owner adjudication of every instance* —
rejected as the standing rule, and **retained as rung 4** for the instances that deserve it;
`D-043`'s reversal of `D-041` shows that routing everything to the owner does not by itself
produce correctness. *A pure "latest statement wins" rule* — rejected; it would have adopted
whichever EMA mapping was stated last and cannot see a misspeak, which rung 1 catches.
*Deleting the superseded `C-xxx` once a rung answers* — rejected outright; the divergence is
evidence about the corpus, and §3.3's principle applies unchanged.
⭐ *Applying rung 3 by default at Part 2 and adopting V14* — **rejected, and this is the one that
was live.** Rung 3 does answer for V14 in isolation, and the drafted caution against defaulting to
*"most recent"* stands: rung 1 answers for V12, the two disagree, and rung 4 exists for exactly
that. ⭐ *Treating the `!SM_TDI` buffer-name list as evidence of the basis* — rejected on the
field-by-field reading above; naming the buffers a build plots is not stating what one of them is
computed from, and `D-045` Part 1 admits an artifact, not a reading of it.

**Consequences:** `SOURCING_HIERARCHY.md` gains a §3.5 stating the ladder and pointing here.
`C-021` gains the rung-4 disposition and the `TOOLING` check above, **and stays `OPEN`**; `A-086`
stays `DO NOT CODE` and unchanged as to basis. **No other record changes status** — in particular
`C-017` is **not** ruled by this entry; it becomes eligible for a session to apply the ladder to
it, which is a different act. **No `A-xxx` is unblocked and no test becomes runnable.**
`REVIEW_PROTOCOL.md` gains a check that a session claiming a rung names it.
`REVIEW_INDEX.md` item 168 closes **as to Part 1** and a successor item carries the owner's
outstanding `C-021` pick.
**Status:** ACTIVE — Part 1 is the operative rule; Part 2 records a rung-4 non-adjudication and
`C-021` remains OPEN pending the owner's direct pick

---

## D-049 — A forward read of a not-yet-studied lesson is permitted under four cumulative conditions, and the fourth is the one that matters

**Date:** 2026-08-14
**Resolves:** `18_REVIEW/REVIEW_INDEX.md` open item **179**, raised by V14 R1 as a proposed
standing precedent. **Unblocks** item 176's second calendar gap.
**Does not disturb:** `D-004` (the progression gate), `D-002` (one lesson per session), `D-017`
(ingestion), `I-008` (unverified supplied transcripts). Nothing here permits **studying** a future
lesson.

**Decision:** A session may read files belonging to a lesson it is not studying — including a
lesson beyond the gate — **if and only if all four conditions hold. They are cumulative; failing
any one makes the read impermissible:**

| Clause | Condition |
|---|---|
| **(a)** | **It seeks a BIBLIOGRAPHIC fact** — a filename, a week label, a duration, a checksum, a spoken week number, an ordering. **Never doctrine, never a rule, never a value, never a definition.** A read that would answer an `A-xxx` is forbidden outright, whatever it finds. |
| **(b)** | **It is disclosed AT THE POINT OF USE** — in the artifact that relies on it, not only in `LOG.md`. A reader landing on the claim sees where it came from. |
| **(c)** | **No artifact, note or interpretation about the future lesson is created.** No `03_LESSON_NOTES/` entry, no screenshot index, no `A-xxx`, no mastery work. The read leaves no forward footprint. |
| **(d)** | ⭐ **The imported datum carries the SAME `I-008` VERIFICATION as any other evidence, or is labelled `UNVERIFIED` wherever it is used.** A supplied pre-ingestion transcript is not evidence merely because it is on disk. |

**Clause (d) is the operative one and the reason this entry exists.** V14's `D3` satisfied
(a)–(c) and **failed (d)**: the file it read is a pre-ingestion supplied transcript of exactly the
class `Q-008`…`Q-015` show to be fabricated in its headers — **its own header carries
*"Course Position: Video 16 of 21"* and a *"Primary Topics"* line, the two fields `Q-015` §5
quarantines by name** — and the session applied `I-008` rigorously to V14's own body and **none of
it** to the V15 body it made load-bearing for `A-092`.

**A fifth condition, implied by (a) and stated so it is not missed: PREFER THE INGESTED SOURCE.**
Where `SOURCE_MANIFEST.md`, the library tree or an already-studied lesson answers the question, the
forward read is **not permitted** — not because it is dangerous, but because it is unnecessary and
imports an unverified body for no gain. V14's `D3` failed this too: the manifest already showed
`Wk5 041512` → `Wk7 050612` with no `Wk6`.

**Reason:** The capability is genuinely useful and genuinely cheap — the second calendar anomaly
(`Wk9 052012` → `Wk10 061712`, a four-week jump with three missing weeks recorded nowhere) has a
forward read as its cheap decider, and that work is currently blocked on this ruling. Prohibiting
forward reads outright would forbid an act that is, in form, harmless: a bibliographic string check
creates no artifact and engages neither `D-004` nor `D-017`. But permitting them on disclosure
alone would leave untouched the thing that actually went wrong, which was not the boundary and not
the disclosure — **it was importing an unverified datum from a quarantined class and treating it as
established.** This project quarantined 72 files to avoid exactly that, and the hazard does not
change because the datum is bibliographic rather than doctrinal.

**Evidence:** `18_REVIEW/V14/V14_REVIEW_R1.md` § `D3` and `REVIEW_INDEX.md` item 179, which
proposed these four clauses; item 165; `A-092`; `SOURCE_MANIFEST.md`; `Q-015` §5 and
`Q-008`…`Q-015`; `I-008`; `COURSE_PROGRESS.md` V15 GATE (c);
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §6 `D5`, §7b.

**Alternatives considered:** *Prohibiting forward reads outright* — rejected; it forbids a
harmless and useful act and leaves the second calendar region unexamined. *Permitting on
disclosure alone, clauses (a)–(c)* — rejected; V14 satisfied all three and the defect survived
all three. *Charging V14 a finding retrospectively* — rejected and explicitly not done: V14 R1
charged nothing because the manifest independently supports the conclusion, and this entry is a
forward precedent, not a re-grading.

**Consequences:**

1. `STUDY_PROTOCOL.md` and both session prompts gain the four clauses and the prefer-the-ingested-
   source rule. `REVIEW_PROTOCOL.md` gains a check that a disclosed forward read names its clause
   (d) status.
2. **Item 176's second calendar gap is unblocked** and may be decided — by the manifest and the
   library tree first, and by a clause-compliant forward read only if those are silent, with any
   imported datum labelled `UNVERIFIED` wherever used.
3. **V14's `D3` is annotated, not reversed.** `A-092`'s conclusion stands on the manifest;
   the V15-sourced half is labelled `UNVERIFIED` at its point of use per clause (d).
4. **`I-008` is unchanged and is not weakened.** This entry extends its reach to imported data;
   it grants no exemption from it.

**Status:** ACTIVE

---

## D-050 — The two `I-010` clock questions are ruled: the `D-035` boundary is ABSOLUTE in the UTC−5 clock, and `D-034`'s FXCM week-open fact is REDUCED TO ITS EVIDENCE pending a winter probe

**Date:** 2026-08-14
**Resolves:** `00_SYSTEM/SETUP_ISSUES.md` `I-010` **Q2** outright; `I-010` **Q1** conditionally —
Q1 stays `OPEN` until the probe is run, but its handling is now decided rather than undecided.
**Amends:** `D-035` (Q2, one appended line); `D-034` fact 1 (Q1, scope of the claim only).
`D-031`'s two-arm requirement is untouched.

**PART 1 — Q2. THE `D-035` BOUNDARY IS ABSOLUTE, IN THE CORPUS'S NATIVE UTC−5 (ARM A) CLOCK.**

`D-035`'s DEVELOPMENT/HOLDOUT boundary at **2016-07-01** is **one instant**, expressed in the
corpus's native **UTC−5** clock, and it is **the same instant for both `D-031` arms.** It is **not**
re-cut per arm. **This rule is general**: it governs the start and end of **every** pre-registered
window, at **every** timeframe, now and in future, unless a later decision says otherwise for a
named window.

**The measured consequence, stated so it is never mistaken for a holdout leak:** under Arm B
(`America/New_York`, `+1h` during US DST) the aggregation stamps **4 fifteen-minute bars** and
**1 one-hour bar** with a wall-clock date of `2016-07-01`:

```text
M15:  2016.07.01,00:00 — 00:15 — 00:30 — 00:45
H1:   2016.07.01,00:00
```

**Those bars are DEVELOPMENT data.** Their underlying M1 data is entirely `<= 2016-06-30` in the
file's own UTC−5 clock; they are the same development-side minutes wearing a different clock label.
**The `D-035` holdout remains sealed and unopened, and this entry opens nothing.**

**PART 2 — Q1. `D-034` FACT 1 IS REDUCED TO WHAT ITS EVIDENCE SUPPORTS, AND A PROBE IS OWED.**

`D-034`'s statement that FXCM opens the week at 21:00 UTC *"consistently, week after week"* is
**true of its sample and is not established year-round.** The sample — `PT-023` §1's depth probe,
**2026-05-31 → 2026-08-13** — lies entirely inside northern-hemisphere summer, over which
*"fixed 21:00 UTC year-round"* and *"DST-anchored New York 17:00"* are **indistinguishable.**
`D-034` fact 1 is therefore **restated as: FXCM's week open is 21:00 UTC over the observed summer
window; its winter behaviour is UNMEASURED.**

**Until the probe is run:**

1. **No new test may bind to a year-round FXCM week open by name.** Existing tests bound to it —
   `W-C`, `PT-008`–`PT-013` — **stand and are not re-run**; their windows are summer-side or
   HistData-sourced, and the exposure is recorded here rather than assumed away.
2. **Any cross-vendor comparison** between the FXCM-sourced and HistData-sourced series **states
   this open question at the point of comparison.** HistData is provably fixed at 22:00 UTC
   year-round; if FXCM is DST-anchored the two **agree in winter and differ by an hour in summer**,
   and each series is internally consistent, so **nothing in the data would flag it.**
3. **The probe is a standing obligation on the first session running after 1 November 2026:**
   probe FXCM's week open on any week between **November and February** and compare against
   22:00 UTC. Record the result by appending to `D-034`. **`D-034` fact 1 is NOT amended from
   memory or inference — it is measured.** `I-010` Q1 closes on that measurement and not before.

**⚠️ Q1 IS NOT RESOLVED BY THIS ENTRY AND IS NOT TO BE READ AS RESOLVED.** What is decided is
**how Q1 is handled** — the claim is narrowed to its evidence, the exposure is written down, and
the closing test is named and dated. **The question itself stays `OPEN` and closes on a
measurement, not on a ruling.**

**Reason:** Both questions have the same shape — **a convention nobody stated, that no result
currently depends on, and that will silently corrupt a comparison the first time one does.** Q2's
spillage is 4 bars at `M15` and 1 at `H1`, which will not move a result; but the ambiguity recurs
at every window start and at every future timeframe, and the `H1` measurement taken 2026-08-14
established exactly that — it is not an `M15` artifact. Pinning it once, generally, costs one line.
Q1 is the more serious of the two because `D-034` states as a standing vendor fact something its
own evidence cannot support, and four pre-registered tests are bound to it **by name**; the failure
mode is invisible by construction, because each series is internally consistent.

**Absolute rather than per-arm, for Q2:** the boundary was computed on **calendar** grounds before
any chart existed, independent of any arm. Cutting per-arm would make Arm B's development block
4 bars shorter than Arm A's — so the two arms would no longer cover the same period, which
defeats the one thing `D-031`'s two-arm design exists to control.

**Evidence:** `SETUP_ISSUES.md` `I-010` Q1 and Q2 in full, including the 2026-08-14 `H1`
amendment; `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M15_H1/QA_REPORT_H1_ARMB.txt` check `C8`
and that dataset's `README.md` (branch `feature/m15-h1-chart-backtest`, **unmerged** — re-verify
against the merged tree before citing); `D-034` fact 1 and `PT-023` §1; `D-035`; `D-036a`'s three
independent confirmations of HistData's 22:00 UTC; `D-031`; `D-044` §6, whose near-miss is the
same clock ambiguity caught in code;
`00_SYSTEM/GAP_AUDIT_2026-08-14.md` §6 `D6`.

**Alternatives considered:** *Per-arm boundaries (Q2)* — rejected for the reason above.
*Leaving Q2 unstated because 4 bars cannot move a result* — rejected; the cost of stating it is one
line and the cost of discovering it in a review is a re-run. *Confirming `D-034` fact 1 as written
(Q1)* — rejected; `I-010` says in terms that it must be measured, not inferred, and the existing
probe provably cannot separate the two hypotheses. *Re-running `PT-008`–`PT-013` now against a
22:00 UTC boundary (Q1)* — rejected as premature: it would spend real work on a hypothesis nobody
has tested, and the winter probe costs one probe and settles it.

**Consequences:** `D-035` gains one appended line stating the clock. `D-034` fact 1 gains its
scope restatement and the probe obligation, appended rather than edited. `I-010` **Q2 closes**;
**Q1 stays `OPEN`** with its handling now decided and its closing test named and dated.
`BACKTEST_EVIDENCE_STANDARD.md` gains the general rule that a pre-registered window's boundaries
are absolute instants in the corpus's native clock, identical across `D-031` arms. **No existing
result is invalidated, no test is re-run, and the `D-035` holdout stays sealed.**
**Status:** ACTIVE — Q1 half PENDING the winter probe
