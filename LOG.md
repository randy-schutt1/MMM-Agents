# RESEARCH LOG

Chronological, **append-only** research journal for the MMM-MASTERY project.

Rules:

- Every meaningful work session appends one entry, newest at the bottom.
- Never rewrite or delete a historical entry because later understanding changed.
  Append a new correction entry instead and reference the entry it corrects.
- Both Student and Reviewer sessions log here. Reviewer entries are labelled
  `Reviewer Session`.
- Entry format is defined in `MMM_MASTER_STUDENT_RESEARCH_AGENT.md` §6 (student)
  and `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md` §6 (reviewer).

---

## 2026-08-10 — Session 1 — Infrastructure Build (Phase 0)

### Objective

Build the complete operational workspace for the Student Agent and the Independent
Reviewer Agent, derived from the two governing files, so that Video 1 can begin
immediately once the bootcamp source videos become locally available.

Infrastructure only. Explicitly **not** a study session.

### Work Completed

- Read both governing files in full:
  - `MMM_MASTER_STUDENT_RESEARCH_AGENT.md`
  - `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md`
- Created the full directory structure (`00_SYSTEM/` … `18_REVIEW/`, `scripts/`),
  built at the repository root rather than in a nested `MMM-MASTERY/` folder, to
  avoid duplicate project nesting.
- Created root documents: `README.md`, `LOG.md`, `CHANGELOG.md`, `.gitignore`.
- Created the `00_SYSTEM/` operating documents: agent roles, study protocol,
  mastery standard, review protocol, remediation protocol, source ingestion
  protocol, file naming standard, course progress, decisions, source manifest,
  session start/close checklists, setup issues, and both session prompts.
- Created 11 reusable templates in `00_SYSTEM/TEMPLATES/`.
- Created review infrastructure: `18_REVIEW/REVIEW_INDEX.md` and empty cumulative
  review templates for the 25% / 50% / 75% / final checkpoints.
- Created empty, clearly-labelled placeholder logs for ambiguities and
  contradictions, and a concept index with no concepts in it.
- Created `scripts/validate_project.py`, a structural-only health check.
- Added a `README.md` contract to every numbered directory.

### Key Findings

None relating to the Market Maker Method. **No course content was analysed,
inferred, or written**, because no source video was accessible in this session.

Four inconsistencies between the two governing files were identified and recorded
in `00_SYSTEM/SETUP_ISSUES.md` (I-001 … I-004) rather than silently resolved. The
most important is I-001: the Student file uses the mastery vocabulary
`PASS / REVIEW REQUIRED / BLOCKED` while the Reviewer file uses
`PASS / REVISE / BLOCKED`. Provisional handling: the two vocabularies belong to two
different actors and are kept separate, with the reviewer decision as the only
progression gate. Flagged for human confirmation.

### Manual Backtesting

None. No charts were studied, no trades were reviewed, and no historical data was
examined. Manual backtesting cannot begin before lesson content exists.

### Ambiguities

`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` created and intentionally empty — zero
course ambiguities recorded, because zero course material has been seen.

### Contradictions

`11_CONTRADICTIONS/CONTRADICTIONS.md` created and intentionally empty — zero course
contradictions recorded. (Governing-file setup inconsistencies are tracked
separately in `00_SYSTEM/SETUP_ISSUES.md`; that file is about project
infrastructure, not about the course.)

### Decisions

Recorded D-001 through D-014 in `00_SYSTEM/DECISIONS.md`, covering: repository as
persistent memory, one lesson per session, separate independent reviewer sessions,
reviewer PASS as the progression gate, manual backtesting inside the Student Phase,
automated backtesting deferred, GBP/USD as primary instrument, evidence hierarchy,
no win-rate optimization, no premature machine rules, source video exclusion from
Git, repository privacy, root-level layout, and unverified course length.

### Files Created/Updated

- Root: `README.md`, `LOG.md`, `CHANGELOG.md`, `.gitignore`
- `00_SYSTEM/`: `AGENT_ROLE.md`, `STUDY_PROTOCOL.md`, `MASTERY_STANDARD.md`,
  `REVIEW_PROTOCOL.md`, `REMEDIATION_PROTOCOL.md`,
  `SOURCE_INGESTION_PROTOCOL.md`, `FILE_NAMING_STANDARD.md`,
  `COURSE_PROGRESS.md`, `DECISIONS.md`, `SOURCE_MANIFEST.md`,
  `SESSION_START.md`, `SESSION_CLOSE.md`, `SETUP_ISSUES.md`,
  `STUDENT_SESSION_PROMPT.md`, `REVIEWER_SESSION_PROMPT.md`
- `00_SYSTEM/TEMPLATES/`: 11 templates
- `18_REVIEW/`: `REVIEW_INDEX.md`, `CUMULATIVE_25.md`, `CUMULATIVE_50.md`,
  `CUMULATIVE_75.md`, `FINAL_COURSE_REVIEW.md`
- `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`,
  `11_CONTRADICTIONS/CONTRADICTIONS.md`,
  `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`
- `scripts/validate_project.py`, `scripts/README.md`
- `README.md` in each numbered directory

### Source Material Status

**No bootcamp video files were accessible during this session.**

- `01_SOURCE_VIDEOS/` contains no media.
- `00_SYSTEM/SOURCE_MANIFEST.md` contains zero video rows.
- No filename, lesson count, lesson order, or lesson title has been assumed or
  recorded. The working figure of "~21 usable videos in a folder of ~24 files" is
  an unverified expectation carried from the project owner and is labelled as such
  everywhere it appears.

### Git

Branch: `claude/add-documents-repository-fdfb3u`
Remote: `https://github.com/randy-schutt1/MMM-Agents` — verified **private**.

Commits from this session:

```text
chore: initialize MMM mastery project structure
docs: add student and reviewer operating system
docs: add lesson and review templates
chore: add project validation workflow
```

(Exact hashes are visible via `git log`.)

### Next Action

**Blocked on human input.** Nothing further can be done until the bootcamp video
library is locally accessible to an agent session.

When it is, start a **Student** session with:

> "Source videos are now available. Run the ingestion protocol, verify the course
> order, and begin Video 1."

The session will then:

1. Run `00_SYSTEM/SOURCE_INGESTION_PROTOCOL.md` (inventory, SHA-256, duration,
   proposed order, ordering-confidence flags).
2. Populate `00_SYSTEM/SOURCE_MANIFEST.md` and expand
   `00_SYSTEM/COURSE_PROGRESS.md` to the real lesson count.
3. Pause for human confirmation of any lesson ordering marked uncertain.
4. Process **V01 only**, then stop and request an independent reviewer session.

Secondary, optional: confirm or correct setup issues I-001 … I-004 in
`00_SYSTEM/SETUP_ISSUES.md`.

---

## 2026-08-10 — Session 2 — Checkpoint Commit Cadence + Infrastructure Audit

### Objective

(1) Adopt the project owner's instruction to commit at frequent checkpoints rather
than at session end. (2) Independently re-audit the Phase 0 infrastructure build.

### Correction Note

The checkpoint-cadence change (commit `31fd4d8`) was committed and pushed
**without appending a LOG.md entry at the time** — a violation of the
session-close protocol this project itself defines. Per the log rules, this entry
corrects the omission rather than rewriting history. The audit below caught it.

### Work Completed

- Recorded D-015 (checkpoint commit cadence) in `00_SYSTEM/DECISIONS.md` and
  propagated it to `SESSION_CLOSE.md` §6, `README.md` §13, and both session
  prompts. Commit `31fd4d8`.
- Full infrastructure audit:
  - All 38 files required by the setup instruction verified present and non-empty.
  - All D-001…D-015 and I-001…I-007 cross-references resolve; no dangling
    file references (the `VXX`/`NNN` patterns are intentional placeholders).
  - `COURSE_PROGRESS.md` header matches the requested column set exactly.
  - `.gitignore` covers every item from the setup instruction's list.
  - README internal section references (§11, §13) verified against actual
    numbering.
  - Negative-tested `scripts/validate_project.py`: it fails correctly when a
    required file is removed (96/0/1) and passes when restored (97/0/0) — the
    green result is not vacuous.
- Fixes from the audit (this session's commit):
  - This LOG entry (finding 1: missing Session 2 log entry).
  - `CHANGELOG.md` 0.1.1 entry for the D-015 process change (finding 2).
  - Clarifying comment on the `*.ts` pattern in `.gitignore` (finding 3: it means
    MPEG transport stream; noted so it isn't mistaken for a stray TypeScript
    exclusion later).

### Key Findings

No Market Maker Method content anywhere in the repository — confirmed by direct
inspection: 0 manifest rows, 0 progress rows, 0 concepts, 0 ambiguity records,
0 contradiction records, 0 reviews, 0 backtests, 0 content files in any lesson
directory. All course-material directories contain only README contracts.

### Manual Backtesting

None. Not applicable before source ingestion.

### Ambiguities / Contradictions

None (course-level). Infrastructure issues remain I-001…I-007 in
`00_SYSTEM/SETUP_ISSUES.md`, unchanged.

### Decisions

D-015 (see above). No new decisions from the audit.

### Files Created/Updated

`LOG.md`, `CHANGELOG.md`, `.gitignore` (this commit);
`00_SYSTEM/DECISIONS.md`, `00_SYSTEM/SESSION_CLOSE.md`, `README.md`,
`00_SYSTEM/STUDENT_SESSION_PROMPT.md`, `00_SYSTEM/REVIEWER_SESSION_PROMPT.md`
(commit `31fd4d8`).

### Git

```text
31fd4d8 docs: adopt checkpoint commit cadence
<this commit> docs: log session 2 and record audit fixes
```

### Next Action

Unchanged from Session 1: **blocked on source video access.** When available,
start a Student session with the ingestion instruction in
`00_SYSTEM/STUDENT_SESSION_PROMPT.md` (first-run variant). Optional: confirm
I-001…I-004 provisional handling.

---

## 2026-08-10 — Session 3 — Setup Issues I-001 … I-004 Confirmed

### Objective

Record the project owner's confirmation of the provisional handling for
governing-file conflicts I-001 through I-004, converting four provisional readings
into binding project rules.

### Work Completed

- `00_SYSTEM/SETUP_ISSUES.md`: I-001, I-002, I-003, I-004 moved from
  `PROVISIONALLY HANDLED` to `RESOLVED`. Resolution notes were **appended** to each
  entry; the original conflict analysis and provisional reasoning were left intact,
  per the file's own rule that resolving an issue means appending the resolution
  and changing the status, not deleting the entry.
- `00_SYSTEM/DECISIONS.md`: recorded D-016, which states all four confirmed
  resolutions in one place so a future session does not have to re-derive them from
  two governing files that genuinely disagree.

### Key Findings

**No implementation change was required.** The Phase 0 infrastructure already
reflected all four readings — `MASTERY_STANDARD.md`, `REVIEW_PROTOCOL.md`,
`COURSE_PROGRESS.md`, `STUDENT_SESSION_PROMPT.md`, and `SESSION_START.md` §6 were
built against the provisional handling and remain correct as written. The
confirmation changes their status from "provisional reading" to "binding rule",
not their content.

Confirmed resolutions:

- **I-001** — Student and Reviewer keep separate status vocabularies, never merged.
- **I-002** — Versioned review files are canonical and never overwritten.
- **I-003** — The governing files' directory trees are partial views; union stands.
- **I-004** — Mastery standard authorizes requesting review; only a reviewer `PASS`
  authorizes advancing.

### Manual Backtesting

None. Not applicable before source ingestion.

### Ambiguities / Contradictions

No course-level records (still zero of each). Remaining open infrastructure issues:
I-005 (no source videos — blocking Phase 1), I-006 (screenshot capture tooling),
I-007 (chart data source for manual backtesting).

### Decisions

D-016 — governing-file conflicts I-001 … I-004 resolved as read.

### Files Created/Updated

`00_SYSTEM/SETUP_ISSUES.md`, `00_SYSTEM/DECISIONS.md`, `LOG.md`.

### Git

```text
<this commit> docs: confirm setup issues I-001..I-004 as resolved
```

### Next Action

Unchanged and unblocked only by source access: **Phase 1 remains blocked on I-005.**
When the bootcamp video library is locally accessible to an agent session, start a
Student session using the first-run variant in
`00_SYSTEM/STUDENT_SESSION_PROMPT.md`.

Note for that session: I-006 and I-007 are still open and will need decisions at
first lesson and first manual backtest respectively.

---

---

## 2026-08-10 — Session 4 — Source Ingestion + V01 Study (Phase 1 opens)

### Objective

Run `SOURCE_INGESTION_PROTOCOL.md` against the now-accessible bootcamp library, then
study V01 through interpretation. Deliberately stop before homework, manual backtest,
chart examples, concept library, and mastery report.

First session in which any source video has been seen by an agent.

### Work Completed

**Housekeeping.** Cleared stray files from `01_SOURCE_VIDEOS/`: a 61 MB
`_DELETE_ME_test_conversion_*.mp4`, a `.tmp_swf_test/` folder of 392 stray jpegs from
a prior extraction attempt, and 14 `.DS_Store` files. The two named items were moved
to the session scratchpad rather than hard-deleted.

**Ingestion (Steps 1–9).** All 42 SWFs hashed (SHA-256) and probed. `ffprobe
format=duration` returns `N/A` for every file — these containers carry no duration
field — so duration was taken from the last audio-packet PTS, validated against V01
(3283.80 s = 00:54:43.8, matching both the `(55mins)` label and the final transcript
timestamp `[00:54:38]`). All 42 filename labels agree with measured runtime to within
one minute.

Result: **21 lesson videos, 21:52:38 total, every row `CERTAIN`.**

**Lesson order corrected.** On-disk folder numbering was an alphabetical artifact
(`Wk1, Wk10, Wk2, …`) that put Week 10 in position 3 and shifted every folder from 03
onward. Re-derived from the `MMDDYY` date in each filename, cross-checked against the
instructor's week labels — the two agree completely. 19 of 21 folders renamed so
folder `NN` = video `VNN`. Source `.swf` files not renamed.

**Week 6 confirmed absent.** Session dates run 03/18, 03/25, 03/26, 04/01, 04/08,
04/15, then jump to 05/06. Documented as expected-missing (manifest anomaly A-01) per
Step 8. Not to be fabricated or interpolated by any future session.

**Duplicates resolved.** All 21 lesson videos exist twice, byte-identical — flat in
`Bootcamp/` and inside each `Bootcamp Notes/NN_.../` folder. Confirmed by matching
checksums across all 21 pairs. Flat copy taken as canonical. 21 further SWFs (3 Dean
Malone, 18 `SteveMauro060212`) inventoried as `X01`–`X21`, `NOT A LESSON`, out of
scope pending an owner decision after V21.

**Quarantine.** 72 files moved to
`01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/`: `NOTES.md`,
`RULES.md`, `VISUAL_INDEX.md` for all 21 lessons, the 8-file `00_MASTER/` rulebook,
and `Forex_Bootcamp_Complete_Training_Notes.md`. Three independent findings against
V01, each verified in this session rather than taken on report:

1. `RULES.md` cites `V01-R001` at `[00:05:00]` — *"Wait for the M15 candle to close
   before taking the 5/13 EMA cross"*, marked `Source: Explicit`, `Coding Readiness:
   Ready`. `[00:04:51]`–`[00:05:32]` is the instructor complaining about last-minute
   homework. Across the whole transcript `EMA` matches 14 times; 13 are the substring
   inside *email*. The one real occurrence is `[00:19:15]`, survey question 10 — *"Do
   you know how to read the EMAs in real time?"* — which states no periods, no cross,
   and no candle-close condition. The same file's parameter table sources EMA periods
   5/13/50/200/800 to `[00:04:00]`, where nothing concerns moving averages.
2. `VISUAL_INDEX.md` claims 78 captured screenshots with filenames, byte sizes, and
   per-image descriptions. One image exists and matches none of them.
3. `MASTER_RULEBOOK.md` states `MR-001`–`MR-005` all marked `Source: Explicit`, none
   carrying a video ID or timestamp — a Phase-3-shaped specification produced before
   Phase 1 ran.

Retained, not deleted, as the record of what was discarded and why. Registered in the
new tracked `00_SYSTEM/QUARANTINE_REGISTER.md` (Q-001), since the files themselves sit
under a Git-ignored path.

**V01 transcript verified and adopted.** Checked before use, given its provenance:
final timestamp `[00:54:38]` against measured 00:54:43.8; timestamps monotonic; it
preserves its own ASR garble (*"the man is the water that catch up in the mustard"*),
crosstalk, student names, and a 33-minute administrative opening. A fabricated
transcript does not invent its own mishearings, and the quarantined `NOTES.md` for
this same video describes content the transcript does not contain. Relocated to
`02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md` with a full provenance header; body copied
byte-for-byte and verified (974 timestamp markers identical).

**V01 studied.** `V01_SOURCE_NOTES.md` and `V01_INTERPRETATION.md` written from the
transcript alone. Nothing carried over from the quarantined files.

### Findings

**V01 is a framing lesson, not a mechanics lesson.** It teaches a thesis (the weekly
cycle is manufactured; traps occur at week/session boundaries; an anchor point commits
direction mid-week) and gives prohibitions. It delivers no executable method. Section
6 of the source notes — Conditions Stated — has an **empty Confirmation column and an
empty Invalidation column across all eight rows.** No stop-loss rule, no target, no
risk-to-reward, no position size, and no indicator parameter appears anywhere in 54
minutes.

**Seventeen load-bearing terms are used and none is defined** — anchor point, trap
move, level, trading zone, blue/red box, second leg, tracer, stop hunt high drop, peak
formation, M and W, midweek reversal, and more. All 17 logged as `A-001` … `A-017`,
all `DO NOT CODE`. The trading zone is explicitly deferred to V02.

**Two contradictions logged.** `C-001` (foundational, `UNRESOLVED`): the duration of
the move away from the anchor is given as "two and a half to three more days"
asserted "for sure" at `[00:35:05]`, then as "four days, three and a half days, three
days" hedged with "likely" at `[00:35:15]`. The instructor is told about the conflict
by students at `[00:36:07]`, acknowledges it — *"It's more than what I've told you. I
understand that"* — and moves on. `C-002`: the entry filter and direction restriction
exist in strict and relaxed forms selected by an unmeasurable skill threshold (A-013).

**The lesson assumes prior material.** `[00:34:33]` — *"**remember** we have the trap
moves"* — and `[00:36:07]`, where students quote his earlier teaching back at him.
V01 opens this bootcamp cycle, not his teaching. Some vocabulary may never be defined
inside this 21-video library.

**The one moving-average mention is bait, not signal.** `[00:39:26]` — *"Look at the
moving averages fan out. He shows something to the traders. He shows longs"* —
describes what the dealer displays to induce the wrong position. Logged as A-015 with
an explicit inversion warning: coding it as an entry condition would build a system
that does exactly what the lesson warns against. This is very likely the seed of the
fabricated 5/13 EMA rule.

### Screenshots — I-006 investigated, cause established

`ffmpeg` aborts on these files after ~2 minutes with `pixel format change
unsupported`. Direct SWF tag parsing shows why: V01 has 9,853 `SHOWFRAME` tags
(3.0 fps × 3,284 s — the full duration) and **no video stream**. The screen is
composited from bitmap tiles on a display list (389 `DefineBitsJPEG2`, 603
`DefineBitsLossless`, 658 `DefineShape3`, 537 `PlaceObject2`). Extracting image tags
directly yields one full 1024×768 keyframe at `00:00:00` plus 388 delta tiles of
26×38 to 72×56 px — cursor sprites and changed regions, not frames. Producing viewable
frames requires evaluating the display list, i.e. a Flash renderer. No `ffmpeg`
invocation will do it.

Ruffle checked and ruled out inside its time box: release v0.5.0 ships a GUI desktop
player (`ruffle-0.5.0-macos-universal.tar.gz`); there is no headless exporter asset.
Frame export lives only in the `ruffle_exporter` crate — a from-source Rust build,
out of bounds after it hung a prior session. **No download was made, no build
attempted.**

Live route remains CloudConvert when the owner is at his own machine. TradingView
recreations were **not** started; `04_SCREENSHOTS/V01/INDEX.md` records the ten
priority moments and the rule that recreations go to `09_CHART_EXAMPLES/` with
sidecars, never to `04_SCREENSHOTS/`.

Consequence: roughly the last 21 minutes of V01 is narration over slides, spoken
deictically ("this", "right here", "these two lines"). About half the lesson is in the
visual channel and none was recovered. **No item in `V01_INTERPRETATION.md` is
classified `VISUAL`.** Stated in every affected artifact.

### Manual Backtesting

None. Out of scope for this session by instruction.

### Ambiguities / Contradictions

First course-level records in the project: `A-001` … `A-017` (all `DO NOT CODE`),
`C-001` (foundational, `UNRESOLVED`), `C-002` (stated exception, condition
unmeasurable).

### Decisions

`D-017` — source arrangement, lesson order, duplicate handling, and quarantine of
pre-ingestion notes.

### Setup Issues

`I-005` closed by ingestion. `I-006` updated with the investigated cause, still
`OPEN`. `I-008` opened — 20 of 21 transcripts are unverified and must each be checked
against their own audio before that lesson is studied.

### Files Created/Updated

Created: `00_SYSTEM/QUARANTINE_REGISTER.md`, `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md`,
`03_LESSON_NOTES/V01_SOURCE_NOTES.md`, `03_LESSON_NOTES/V01_INTERPRETATION.md`,
`04_SCREENSHOTS/V01/INDEX.md`.
Updated: `00_SYSTEM/SOURCE_MANIFEST.md`, `00_SYSTEM/COURSE_PROGRESS.md`,
`00_SYSTEM/DECISIONS.md`, `00_SYSTEM/SETUP_ISSUES.md`,
`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`, `11_CONTRADICTIONS/CONTRADICTIONS.md`,
`LOG.md`, `CHANGELOG.md`.

### Validation

`python3 scripts/validate_project.py` — **97 passed, 0 warnings, 0 failures.**

### Next Action

V01 homework, manual backtest, and mastery report — the deliverables this session
stopped short of by instruction. Note before starting:

- V01 assigns homework (source notes §11 H1–H8) but most of it is a student survey
  emailed to an instructor in 2012. Only H4 ("on the one hour chart… look at the
  levels and the cycle"), H5 ("mark the chart up… go look at the pairs this week"),
  and H6 (read your broker agreement) are actionable now, and H4/H5 depend on
  concepts V01 never defines. Worth deciding how a 2012 survey is handled before
  writing `05_HOMEWORK/V01/`.
- Manual backtesting V01 requires labelling "anchor points" — an `A-001` `DO NOT
  CODE` concept. Consider whether V01 is backtestable at all, or whether observation
  should begin after V02 defines the trading zone.
- `I-007` (chart data source) is still open and blocks manual backtest.

---

## 2026-08-10 — Session 5 — V01 Screenshots, Full Capture, Mastery Submission

### Objective

Resolve I-006 (screenshot capture), upgrade V01's artifacts with visual evidence, and
submit V01 for independent review. Explicitly **not** to run the review — the student
does not audit itself.

### Work Completed

**Screenshot capture solved (I-006 → `RESOLVED`).** The renderer `ffmpeg` lacks exists
as WebAssembly: Ruffle's `web-selfhosted` build, served over HTTP and driven by
Playwright in headless Chrome, renders these SWFs correctly at 1024×786. Recorded V01's
full 54:44 playthrough, trimmed to the measured playback-start offset, and muxed with
audio taken straight from the SWF (`ffmpeg -vn -c copy`, 3283.83 s).

Routes tested and ruled out, recorded in I-006 so they are not retried: Ruffle desktop
(GUI only, no headless exporter); building `ruffle_exporter` (forbidden — hung a prior
session); Ruffle's JS seek API (does not exist — `goto_frame`/`seek`/`current_frame`
appear 0 times in the JS bundle; they are internal Rust symbols); SWF `ExternalInterface`
(this SWF registers zero callbacks — `addCallback` appears 0 times in its AS2 string
pool); Camtasia scrubber dragging (works, lands imprecisely and non-linearly).

**Sync verified, zero drift.** The Camtasia player burns its own timecode into every
frame, so each output frame is self-documenting. mp4 position vs burned timecode checked
at 00:05, 05:00, 10:00, 15:00, 20:00, 25:00, 30:00, 35:00, 40:00, 45:00, 50:00, 54:00 —
**all twelve exact.**

**22 screenshots curated.** 657 thumbnails sampled at 5 s intervals and pairwise-diffed
→ 20 distinct screen states; combined with transcript-flagged moments → 24 candidates,
reviewed as contact sheets, 2 dropped as duplicates. Frames keep the player's control
bar deliberately: the burned timecode makes each image prove its own timestamp.

**Artifacts upgraded without rewriting history.** `V01_SOURCE_NOTES.md` §4 gained
thirteen visual observations plus a corrections table; its original "no screenshot
exists" text is preserved and marked superseded. `V01_INTERPRETATION.md` §§1–9 were left
**unedited**; a new §10 records the delta.

### Findings — what the visuals changed

**Four terms resolved or constrained by text printed on slides that was never spoken
aloud:**

- **A-003 `RESOLVED BY COURSE`.** The word the ASR rendered "penings" — four occurrences
  in the core sequence, which the record correctly refused to guess — is **"pendings"**.
  The `[00:40:25]` slide prints **"Trigger The Pendings"** beside **"Trigger The Stops"**.
  Two distinct pools of resting orders.
- **A-006, one reading eliminated.** The blue and red "boxes" are shaded rectangles drawn
  over *price areas* — pale blue over flat consolidation, dark red over the extended
  trapped area. The session-time-rectangle reading is wrong. At `[00:48:35]` each carries
  a numeric label, so they are measured regions.
- **A-004 constrained.** A "level" is a horizontal price line on the template —
  `[00:50:55]` shows yellow/red/cyan dashed lines and prints *"Level Not Crossed Until
  Late Friday"*. Not a distance, not a swing count.
- **A-015 corroborated.** Four MA lines (yellow, red, cyan, white) are visibly present.
  Still no periods stated anywhere. The refusal to name EMA periods stands and is better
  supported.

**GBP/USD found, never spoken.** `[00:50:55]`'s chart header reads `GBPUSD,M15` — the
project's designated primary research instrument, with the full weekly cycle annotated
(*"Stops Are Triggered on The Weak long Holders"*, *"A uni-directional Swing The Rest Of
The Week"*, *"Higher Level Longs Are Now Trapped"*, *"Level Not Crossed Until Late
Friday"*, day separators Sunday→Friday). The transcript-only pass could not have found
this.

**One of my own readings corrected.** I had widened a *closed slide-list of six*
trap-move boundaries into "trap moves occur at session boundaries as a general property"
(I9/G5). The `[00:30:35]` slide lists exactly six. The generalisation was wider than the
evidence — the failure mode §3 of the interpretation template exists to catch, caught
only by a screenshot.

**One reading NOT confirmed.** I7 — that anchor point ≈ peak formation ≈ M/W — remains
`INFERRED / Low`. The lesson's fullest cycle chart carries five printed labels and
**none** uses those words. Neither confirmed nor refuted; a future session must not read
§10 as having settled it.

**A new ambiguity, and a trap avoided.** A-018: the `R = 70.5` / `R = 51…` / `= 43.1`
labels on the boxes. Read as *Range in pips* (the same template prints
`Previous Days Range= 146.4`), **not asserted**, and explicitly not read as
risk-to-reward — which would have manufactured a target rule from a label in a lesson
that states no stop and no target.

### Ambiguities / Contradictions

18 ambiguity records (A-001…A-018); A-003 now `RESOLVED BY COURSE`, the rest
`DO NOT CODE`. Contradictions unchanged: C-001 (foundational, unresolved), C-002.

### Decisions

`D-018` — mastery dimensions F (Homework) and G (Manual Backtesting) may be marked
`NOT APPLICABLE` for a lesson that supplies nothing to satisfy them, with justification
recorded. Sets the standard for all 21 lessons; expected to be rare after V01.

### Mastery Submission

`07_MASTERY_REPORTS/V01_MASTERY_REPORT.md` — status **`REVIEW REQUIRED`**, deliberately
not `PASS`. F and G claimed `NOT APPLICABLE` under D-018; four specific questions put to
the reviewer. Four QC boxes left unchecked and stated rather than omitted: no positive,
negative or borderline chart examples, and no concept-library entries — because V01
defines no concept precisely enough to classify against, and promoting an open
`DO NOT CODE` ambiguity to a concept entry would launder it into a definition.

### Files Created/Updated

Created: `00_SYSTEM/SWF_CAPTURE_RECIPE.md`, `07_MASTERY_REPORTS/V01_MASTERY_REPORT.md`,
22 PNGs in `04_SCREENSHOTS/V01/`.
Updated: `04_SCREENSHOTS/V01/INDEX.md`, `03_LESSON_NOTES/V01_SOURCE_NOTES.md`,
`03_LESSON_NOTES/V01_INTERPRETATION.md`, `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`,
`00_SYSTEM/SETUP_ISSUES.md`, `00_SYSTEM/DECISIONS.md`, `00_SYSTEM/SOURCE_MANIFEST.md`,
`00_SYSTEM/COURSE_PROGRESS.md`, `LOG.md`, `CHANGELOG.md`.

Derivative retained outside the repo: `/Users/randyschutt/Desktop/Trading/MMM_DERIVATIVES/V01.mp4`.

### Validation

`python3 scripts/validate_project.py` — **97 passed, 0 warnings, 0 failures.**

### Next Action

**An independent reviewer session** writes `18_REVIEW/V01/V01_REVIEW_R1.md` per
`REVIEW_PROTOCOL.md`. This session did not and must not perform it.

V02 is gated behind that `PASS`. When it opens, follow `00_SYSTEM/SWF_CAPTURE_RECIPE.md`
in a fresh session, and spend 15 minutes first on the untested frame-rate-patch idea in
§11 — if it works it removes the 1-hour real-time capture cost from the remaining 20
videos.

---

## 2026-08-10 — Reviewer Session

### Lesson
V01

### Review Objective
Independent mastery audit, round 1. Fresh session; produced none of the V01 artifacts
(`DECISIONS.md` D-003).

### Source Evidence Reviewed
Reviewed **before** any student artifact, per `REVIEW_PROTOCOL.md` §3.

- `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md` in full — all 974 markers, `[00:00:00]`–`[00:54:38]`.
- Source `.swf` SHA-256 recomputed: `c7e660f4…d84030`. **Matches** the claimed hash.
- Ten of the 22 screenshots opened and read at full resolution, including every image
  the interpretation depends on: `[00:02:35]`, `[00:16:55]`, `[00:19:20]`, `[00:30:35]`,
  `[00:38:50]`, `[00:39:10]`, `[00:39:40]`, `[00:40:25]`, `[00:43:58]`, `[00:44:40]`,
  `[00:48:35]`, `[00:50:55]`, `[00:54:30]`. Burned-in timecode matched the filename in
  every case.
- Quarantine folder inspected on disk: 73 files, `.gitignore`-covered, zero Git-tracked.

Not reviewed: the audio. The ASR-garbled session times remain unverified by the
reviewer as well as by the student — which affects no finding, since no artifact
asserts a value for them.

### Student Artifacts Reviewed
`V01_SOURCE_NOTES.md`, `V01_INTERPRETATION.md`, `V01_MASTERY_REPORT.md`,
`04_SCREENSHOTS/V01/INDEX.md`, `AUTOMATION_AMBIGUITIES.md` (A-001…A-018),
`CONTRADICTIONS.md` (C-001, C-002), `CONCEPT_INDEX.md`, `DECISIONS.md` D-017/D-018,
`QUARANTINE_REGISTER.md`, `SETUP_ISSUES.md` I-006/I-007/I-008. `validate_project.py`
re-run independently: 97/97.

### Findings

**No critical findings.** The evidence base was tested mechanically and is clean:
144 quotations were located in a word-level stream of the transcript and compared with
their cited timestamps. 122 land within 3 s; 20 more are passage-level citation; 2 are
genuine misdatings; **0 quote words the recording does not contain.** No fabricated
rule, no imported framework, no premature quantification, no hindsight contamination.

**Two major findings.**

1. `E02` — `V01_INTERPRETATION.md` §10.1 `U2` declares the session-time reading of the
   blue/red boxes "wrong", under a heading titled "Resolved outright". The images show
   rectangles with both a time extent and a price extent; blue rectangles abut vertical
   day separators at `[00:38:50]`, `[00:44:40]` and `[00:48:35]`. The price-zone reading
   is confirmed; the time reading was eliminated without evidence.

2. `E10` — dimension F marks all eight homework items `NOT APPLICABLE` under D-018.
   H4 `[00:37:58]` and H5 `[00:52:20]`/`[00:53:02]` are observational chart exercises
   that need a chart, not a rule definition. They are `DEFERRED` — blocked by `I-007` —
   not inapplicable. D-018 lacks the distinction, and as written the precedent would
   permanently close performable work across all 21 lessons.

Six minor and four note-level findings, all documentation-level: two misdated citations
(S19, X3 at `[00:36:38]`; the quote is at `[00:36:17]`), an unlogged six-vs-four
mismatch in the trap-move enumeration (`[00:30:35]` slide and `[00:36:38]`–`[00:37:09]`
give six; the `[00:45:44]` recap gives four), three stale statements now contradicted by
the repo's own state, and three over-claiming rows in the screenshot index.

**Upheld on audit**, after adversarial testing rather than acceptance:
dimension G `NOT APPLICABLE`; `C-001` does not justify `BLOCKED`; `I7` stays open at
`INFERRED / Low`, re-adjudicated at V02; empty `08_CONCEPT_LIBRARY` and
`09_CHART_EXAMPLES` are correct for a lesson that defines no concept. The quarantine is
verified real and effective — nothing quarantined is discoverable as valid evidence.

Two judgement calls deserve specific credit and should be preserved as practice: the
refusal to read `R = 70.5` as a risk-to-reward ratio, and the inversion warning on the
moving averages (V01's only MA mentions describe what the dealer *shows traders as
bait*, so coding them as an entry signal would invert the lesson).

### Required Corrections
Eight, all `edit` — no work requires a `redo`, because no test was performed. Full
detail in `18_REVIEW/V01/V01_REVIEW_R1.md` §REQUIRED CORRECTIONS. Plus one carried item:
re-check `[00:46:04]`, `[00:48:05]`, `[00:48:13]` against the retained mp4 before any
session-timing parameter is coded.

### Decision
REVISE — confidence HIGH. Advancement NOT AUTHORIZED.

### Git
Review written to `18_REVIEW/V01/V01_REVIEW_R1.md` (new file; nothing overwritten —
`18_REVIEW/V01/` did not previously exist). `REVIEW_INDEX.md` and `COURSE_PROGRESS.md`
updated.

### Next Review Trigger
Student resubmission of V01 after the eight corrections → `V01_REVIEW_R2.md`.

---

## 2026-08-10 — Remediation of V01 (Review R1)

### Objective
Apply four of the corrections required by `18_REVIEW/V01/V01_REVIEW_R1.md`, at the
project owner's direction: both `MAJOR` findings and two `MINOR` ones.

**Role note.** These corrections were applied by the same session that wrote R1.
`REVIEW_PROTOCOL.md` and the reviewer prompt both hold that the reviewer does not
perform the student's work, and `DECISIONS.md` D-003 holds that a session cannot
independently evaluate what it produced. The owner directed the work explicitly. The
consequence is recorded rather than glossed: **R1's verdict is unchanged and R1 was not
edited; this session cannot certify these corrections; V01 requires a fresh reviewer
session for R2.**

### Findings Addressed
- [E02 / MAJOR] R1 finding 1 — `V01_INTERPRETATION.md` §10.1 `U2` declared the
  session-time reading of the blue/red boxes "wrong" under a heading titled "Resolved
  outright" → `U2` **withdrawn** (stub retains the original claim); corrected entry added
  as `C5` in §10.2 "Materially constrained, still not defined". `A-006`'s Visual
  Characteristics rewritten from the frames; both candidate measures explicitly still
  live; `Q4` reopened; `A-006` remains `DO NOT CODE`.
- [E10 / MAJOR] R1 finding 2 — dimension F marked all eight homework items
  `NOT APPLICABLE` → **split**. H1–H3, H6–H8 remain `NOT APPLICABLE`; **H4 and H5 are
  `DEFERRED — BLOCKED BY I-007`**. New **`D-019`** records the general rule that
  `NOT APPLICABLE` (closed permanently) and `DEFERRED` (open, blocked) are distinct
  dispositions and that D-018 grants only the first. D-018 itself is unedited and remains
  `ACTIVE` — `DECISIONS.md` is append-only.
- [E13 / MINOR] R1 finding 4 — six-vs-four trap-move enumeration mismatch unflagged →
  recorded in `V01_SOURCE_NOTES.md` §14. The abbreviated-recap reading is recorded as a
  reading, not a resolution; the `[00:30:35]` slide is treated as the higher-tier evidence.
- [E20 / MINOR] R1 finding 6b — `CONCEPT_INDEX.md` still claimed "No course material has
  been studied" → corrected to state the real current reason for emptiness (V01 studied;
  zero concepts, because every candidate is an open `DO NOT CODE` ambiguity).
  `09_CHART_EXAMPLES/README.md` given the equivalent correction.
  **Two further instances found while checking, and worse:**
  `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` and `11_CONTRADICTIONS/CONTRADICTIONS.md`
  both declared `RECORDS: 0` and "Intentionally empty. No course material has been
  studied" while holding **18** and **2** records — a status block contradicting its own
  file's contents. Both corrected with accurate counts; original wording retained. These
  needed no new visual or interpretive claim (the counts are arithmetic over existing
  content), which is why they were fixed rather than referred to R2 like the 16 below.

### Work Redone (not edited)
**None, and none was required.** Every R1 finding was a documentation fix under
`REMEDIATION_PROTOCOL.md` §3.3. No test was invalid because no test was performed —
V01 states no rule whose application could be graded. No observation, classification or
sample exists to redo.

### Work Corrected (documentation only)
`V01_INTERPRETATION.md` (§10.1 `U2` withdrawn, §10.2 `C5` added);
`AUTOMATION_AMBIGUITIES.md` (`A-006`); `V01_MASTERY_REPORT.md` (dimension F, QC
checklist, the "visuals eliminated one reading" claim struck, `## Revision R1` appended,
pointer added to the original STATUS paragraph); `DECISIONS.md` (`D-019` appended);
`V01_SOURCE_NOTES.md` (§14); `CONCEPT_INDEX.md`; `09_CHART_EXAMPLES/README.md`;
`COURSE_PROGRESS.md`; `REVIEW_INDEX.md`.

Nothing was deleted. Superseded wording is retained in place and marked, per
`REMEDIATION_PROTOCOL.md` §§2 and 6.

### Retesting
Not applicable — no rule definition changed in a way that invalidates downstream work,
because there is no downstream work. `A-006` moved from "one reading eliminated" to "both
readings live", which *widens* uncertainty rather than narrowing it, so nothing
previously classified becomes suspect. `scripts/validate_project.py`: 97 passed,
0 warnings, 0 failures.

### New Finding Surfaced During Remediation
The stale *"Unknown — no screenshot exists for V01 (`SETUP_ISSUES.md` I-006)"* paragraph
is **not** confined to the three files R1 identified. It appears in the Visual
Characteristics section of **17** ambiguity records. `A-006` was fixed as a direct
dependency of finding 1; **16 remain** (`A-001`–`A-005`, `A-007`–`A-017`).

Deliberately not swept up. R1 scoped and counted this defect at three instances, and
fixing sixteen more it never assessed would put unreviewed work into the corpus. Several
are not mechanical — `A-009` ("stop hunt high drop"), `A-015` ("shows something to the
traders") and `A-017` ("big entry candle") all have captured frames bearing directly on
them, so updating those means making fresh visual claims, which is study work and needs
auditing. Logged as open item 6 in `REVIEW_INDEX.md`; **referred to R2**.

### Remaining Open Items
R1 findings **3, 5, 7, 8, 9, 10, 11, 12** were outside the directed scope and are **not**
applied. They stand open for R2. Carried research items unchanged: `C-001` (day count,
foundational, UNRESOLVED); `I7` (re-adjudicate at V02); H4/H5 pending `I-007`; the
`[00:46:04]` / `[00:48:05]` / `[00:48:13]` audio re-check before any session-timing
parameter is coded; dimension B pending V02.

### Files Created/Updated
Created: `DECISIONS.md` `D-019`; `V01_MASTERY_REPORT.md` `## Revision R1`;
`V01_INTERPRETATION.md` `C5`; `REVIEW_INDEX.md` open item 6.
Updated: as listed under "Work Corrected".
**Not touched:** `18_REVIEW/V01/V01_REVIEW_R1.md` — a review file is never edited
(`REVIEW_PROTOCOL.md` §11).

### Next Action
Request a **fresh** reviewer session for V01 R2. It must confirm the four applied
corrections, dispose of R1 findings 3, 5, 7, 8, 9–12, and rule on the newly-quantified
16-record staleness.

---

## 2026-08-10 — Reviewer Session — V01 Review R2

**Role:** Independent Reviewer / Teacher. This session produced no V01 artifact and
applied no correction (`DECISIONS.md` D-003).

### Decision

```text
LESSON: V01   DECISION: REVISE   CONFIDENCE: HIGH
0 critical · 1 major · 4 minor · 3 notes (new this round)
ADVANCEMENT: NOT AUTHORIZED — the V02 gate stays closed (D-004)
```

### Method

Source first, per `REVIEW_PROTOCOL.md` §3, and targeted rather than a repeat of R1's
full pass (§4). Transcript read line by line at `[00:35:55]`–`[00:37:28]`,
`[00:37:49]`–`[00:38:13]`, `[00:52:19]`–`[00:53:07]` and four shorter passages.
**Twelve screenshots opened at full resolution**; all twelve carried a burned-in
timecode matching the filename. `validate_project.py` re-run: 97 passed, 0 warnings,
0 failures. R1's hash check, 144-quotation sweep, quarantine audit and dimension-G
adversarial test were **not** repeated — no cause appeared to re-litigate them.

### The four applied corrections

| R1 finding | Verdict |
|---|---|
| 1 — box reading (`E02`, MAJOR) | **PARTIALLY APPLIED — reopened as R2 N1** |
| 2 — dimension F split (`E10`, MAJOR) | **APPLIED CORRECTLY — CLOSED** |
| 4 — six-vs-four trap-move count (`E13`, MINOR) | **APPLIED CORRECTLY — CLOSED** |
| 6b — stale concept-index status (`E20`, MINOR) | **APPLIED CORRECTLY, WIDENED HONESTLY — CLOSED** |

Finding 1 was applied in `V01_INTERPRETATION.md` §10.1 `U2`, §10.2 `C5`, the mastery
report, and `A-006`'s *Visual Characteristics* — but **not** in `A-006`'s trailing
`Visual Evidence Update` block, whose header still reads *"one candidate reading
ELIMINATED"* and whose body still reads *"This eliminates candidate 1… The boxes do not
align with session boundaries."* I checked that sentence against the three frames it
relies on: at `[00:38:50]`, `[00:44:40]` and `[00:48:35]` the pale-blue rectangle's left
edge sits on, or immediately right of, a vertical dotted separator. **It is refuted by
its own evidence**, it contradicts the corrected text 45 lines above it, and it survives
in the register that governs what may later be coded. That is the one open MAJOR.

Findings 2 and 4 were verified by re-deriving them from the transcript before reading
the artifacts. `D-019` is sound and sets the right 21-lesson precedent; its test —
*"is there anything here to do at all"*, not *"can this be done today"* — is correct.

### R1's remaining findings — all eight disposed of

3, 5, 6a, 6c, 7, 8, 9, 10, 11, 12: **all upheld and all still open.** Three needed
correcting or widening in the process:

- **3** — the `[00:36:38]` misdating occurs in **five** places, not two.
- **8** — **eight** screenshots are missing from §4, not seven, and the eighth
  (`[00:54:30]`) is a teaching frame, so R1's proposed remedy would have been false as
  stated.
- **10** — `A-003` has **five** self-contradicting fields, not one stale Risk cell. The
  project's one resolved ambiguity currently tells a reader who stops before the
  trailing block the opposite of the truth.

### Ruling on open item 6 (the 16-record staleness)

**Upheld, and it is real study work — but the item's own scope was wrong.** It named
`A-009`, `A-015` and `A-017` as needing fresh visual claims. All three already carry
visual updates; I audited all three against the frames and all three are sound. The
records that actually need a fresh visual determination are **`A-002`** (the lesson's
central object is printed on two chart slides), **`A-008`** ("these two lines" —
`[00:38:50]` shows exactly two vertical dotted separators bounding Sunday) and
**`A-016`** (`[00:44:40]` shows the spike-then-chop sequence). Determinations supplied
in R2 Part 3.3, all as *materially constrained*, none as resolved. `A-011` / `A-012` /
`A-014` gain slide-text evidence. `A-007` needs a "frame exists, defines nothing" note —
I declined to convert the `[00:43:58]` freehand into a leg definition. Eight are
mechanical.

### New findings

`N1` (MAJOR, `E02`) above. `N2`–`N4` (MINOR, `E11`): `S29` misdated; the `[00:36:38]`
error propagated to three files R1 did not list; H5 cited as `[00:52:20]` / `[00:53:02]`
in `D-019` and the mastery report when the assignment is at `[00:52:38]`–`[00:52:50]`
and `[00:53:07]`. `N5` (MINOR, `E02`): the corrected box text says pale blue covers
"flat, low-range consolidation", which `[00:38:50]` — cited in the same sentence —
contradicts. `N6`–`N8` (NOTE): enumeration range truncated; `INDEX.md` `[00:30:35]`
cites `S28–S33`; §4's omission count.

### Escalation triggered

Three error codes passed the threshold on one lesson. `E11` (5) is the substantive one:
eight statements across two rounds cite a timestamp that does not carry their words.
**No quotation was fabricated** — the words always exist and are quoted accurately; only
the citation is off. Recorded in `REVIEW_INDEX.md` with a proposed `STUDY_PROTOCOL.md`
amendment, to be raised at the 25% cumulative review. `E02` (3) is instructive in its
own right: two of the three were introduced *while remediating the first*.

### Also answered

R1 reviewer question 2 — the `[00:39:40]` freehand does **not** mark the anchor point.
It traces the week-opening advance inside the blue rectangle and the pre-open range; no
stroke isolates a turning point and nothing is named. `§10.3` should cite it as examined
and non-determinative.

### Credit where due

The remediation session marked every supersession, retained the wording it replaced,
refused to sweep up sixteen records it could not certify, and reported a defect that
widened its own scope. Hindsight discipline held through the round where it is most
likely to break. `N1` is a miss of coverage, not of honesty.

### Files Created/Updated

Created: `18_REVIEW/V01/V01_REVIEW_R2.md`.
Updated: `18_REVIEW/REVIEW_INDEX.md` (R2 row, error counts, escalation note, severity
ledger, open items 6–8), `00_SYSTEM/COURSE_PROGRESS.md`, this log.
**Not touched:** any student artifact, and `V01_REVIEW_R1.md` — a review file is never
edited (`REVIEW_PROTOCOL.md` §11).

### Next Action

A Student/remediation session applies the 15 required actions in
`V01_REVIEW_R2.md`. None requires re-studying V01. Then a **fresh** reviewer session
writes `V01_REVIEW_R3.md`. R3 should be short.

---

## 2026-08-10 — Student session — V02 ingested through interpretation

**Scope:** V02 (`Bootcamp1 Wk1 031812 Part2 (60mins).swf`, 01:00:19), one video per
session. Stopped before independent review, per `REVIEW_PROTOCOL.md`.

### A process failure, recorded first

Three confident conclusions reported during this session were **wrong**: that the SWF
frame-rate speedup does not work; that V02's `.swf` contained V01's video; and that all
21 lessons declare a 54:44 duration.

Single cause: a stale `python3 -m http.server 8899` left running by the V01 session owned
the port `SWF_CAPTURE_RECIPE.md` §2 specified. `python3 -m http.server` exits silently on
a busy port, so this session's server never started and every browser render was answered
by the V01 session's server, whose `index.html` hardcodes `v01.swf` and ignores `?swf=`.
A 61-minute capture, three frame-rate runs and a 21-file survey were all of V01.

The frame-rate experiment included a control and the control did not help, because
treatment and control were the same file. Caught only when slide content stopped matching
what the instructor was saying.

Corrections: D-020 retracted in place; D-021 and D-022 added; `SWF_CAPTURE_RECIPE.md` §10
rewritten and GOTCHA 4 added; I-009 opened. Work that never touched the HTTP server —
transcript verification, Q-002, source notes §§1–3/5–14, interpretation §§1–9, registers —
is unaffected.

### The frame-rate speedup works — 40×

Re-tested against a correctly served file: 120 fps patched gives 40:00 of presentation in
60 s of wall clock, linear, against a 3 fps control at 1:1. Neither of the two unknowns in
the original proposal bit — the Camtasia player does follow the root timeline, and
Ruffle's rAF tick is not a ceiling. Adopted at **10×** (D-021): a 60-minute lesson sweeps
in ~6 minutes. **The ~18 hours of real-time recording budgeted for V03–V21 is not
required for screenshots.**

### Work completed

| Artifact | Note |
|---|---|
| `02_TRANSCRIPTS/V02/V02_TRANSCRIPT.md` | Verified against audio — 1,026 monotonic timestamps, final `[01:00:16]` vs measured 3619.81 s, four Whisper spot-checks matching near-verbatim including "Subio", "half-Batman", "Screen Hunter". I-008 satisfied for V02. |
| `QUARANTINE_REGISTER.md` Q-002 | V02's `NOTES/RULES/VISUAL_INDEX` checked individually and confirmed fabricated. `V02-R001` is V01's fake rule re-stamped verbatim at the same timestamp. All 8 "EMA" matches in the transcript are the substring inside "email". `VISUAL_INDEX.md` claims 50 screenshots against 1 real file. |
| `V02_SOURCE_NOTES.md` | §§1–3, 5–14 transcript-only; §4 added after capture. |
| `V02_INTERPRETATION.md` | §§1–9 transcript-only and unedited; §10 records the visual upgrade. |
| `04_SCREENSHOTS/V02/` | 25 frames + `INDEX.md`, fast sweep, validated against the transcript at four timestamps before naming. |
| `05_HOMEWORK/V02/` | 11a attempted on real TradingView data; 11b `DEFERRED` on A-011/A-007. |
| `07_MASTERY_REPORTS/V02_MASTERY_REPORT.md` | `REVIEW REQUIRED`. |

### What the visuals added

The 2-hour session-changeover window and the full ForEx Trading Times table are printed
on slides and **never spoken**. The `[00:18:00]` chart prints `Level 1/2/3` as an ordinal
sequence of legs (A-004) and places `33-Trade` on **Level 3**, not calendar day 3 (A-023).
The R&D slide gives the homework exactly, resolving three ambiguities the ASR left.

The visuals did **not** resolve the foundational gaps: "second leg" (A-007) is now used in
print as well as speech and defined in neither; "mayonnaise" (A-020), the cycle letters
(A-021) and half-Batman (A-022) are absent from every frame.

### Registers

A-019 … A-028 added (ten). Six existing records extended. C-003 (M's and W's "will not
fail", self-contradicted in one sentence) and C-004 (London open 3:30 printed vs 4:00
spoken) added. **C-001 re-tested against V02 and not resolved** — which matters, because
C-001 named "a later lesson refines it" as its most likely route out and V02 is that
lesson.

### Honest finding

**V02 states no complete testable rule**, and the gap is in the same place as V01's: no
entry trigger (everything routes through the undefined "second leg", which he promises to
define at `[00:35:22]` and then defines by pointing at a screen), the trading zone
deferred a second time to V03, stop loss explicitly deferred, no position sizing. What
V02 does supply is exit and management parameters. For lesson 2 of 21 that is coherent;
it is not a pass.

### Note on concurrency

Three sessions ran against this checkout today. Beyond the port collision, `git add -A`
caused sessions to commit each other's in-progress files under unrelated messages
(I-009 collision 2). This session staged explicit paths only.

---

## 2026-08-10 — Remediation of V01 (Review R2) + Review R3

**One session, two roles, at the project owner's direction.** `DECISIONS.md` D-003
separates remediation from review; this session did both. That departure is disclosed at
the head of `18_REVIEW/V01/V01_REVIEW_R3.md` rather than glossed, and it is the single
thing a reader should weigh against the `PASS`.

### Objective

Apply the 15 required actions in `18_REVIEW/V01/V01_REVIEW_R2.md` (`REVISE`, HIGH,
0 critical, 1 major), then render R3.

### Findings addressed

- **[E02 / MAJOR] R2 finding N1** — `AUTOMATION_AMBIGUITIES.md` `A-006`'s trailing
  "Visual Evidence Update — one candidate reading ELIMINATED" block still asserted the
  claim R1 overturned, unmarked, 45 lines below the corrected text. **Withdrawn in
  place**: header changed, original text retained in full and marked `DO NOT CITE`,
  refutation recorded beside it. Verified independently at `[00:38:50]`, `[00:44:40]`
  and `[00:48:35]` — on all three the pale-blue rectangle's left edge sits on or begins
  at a vertical dotted separator, which refutes "the boxes do not align with session
  boundaries" on the block's own evidence.
- **[E02 / MINOR] N5** — "pale blue sits over flat, low-range consolidation" was
  contradicted by `[00:38:50]`, one of the four frames it cited. Replaced with a
  four-row per-frame table and an explicit refusal to offer a unifying rule for blue.
- **[E11 / MINOR] R1 finding 3 + N2 + N3 + N4** — seven citations corrected: `S19`,
  `X3`, the three further `[00:36:38]` instances, `X2`, `S29`, and H5 in `D-019` and the
  mastery report. Each re-derived from the transcript. `D-019` carries a dated
  `CITATION CORRECTED` note and is **not** superseded — its meaning is unchanged.
- **[E20 / MINOR] R1 findings 5, 6a, 6c, 7, 8, 9, 11, 12 and N6, N7, N8** — all applied.

### Work redone (not edited)

None. No test was performed for V01, so no evidence layer existed to redo. Every one of
the 15 actions is a documentation fix (`REMEDIATION_PROTOCOL.md` §3.3), which is what R2
said it would be and what it turned out to be.

### Study work performed

R2 supplied visual determinations for `A-002`, `A-008` and `A-016` as **findings, not
text to paste**. Nine frames were re-opened at full resolution and the determinations
re-made before anything was written into a record. All three are recorded as *materially
constrained*, none as resolved, each stating what it does **not** add. All three remain
`DO NOT CODE`.

### Corrections to R2 itself

Three of R2's supporting statements did not survive verification. All would have entered
the corpus as fact if pasted:

1. *"SHIFT appears nowhere in the transcript"* — refuted. It is spoken at `[00:17:45]`
   with the extra qualifier *"away from the level"*, which is more informative than the
   printed slide and ties `A-011` to `A-004`.
2. *"No item on the `[00:19:20]` slide bears on `A-013`"* — overstated. Q12 prints
   *"Have you doubled a demo account?"*, the printed origin of `A-013`'s candidate
   measure 1. R2's required change is still correct and is applied.
3. *"A byte-identical copy remains at the original path"* — the original remains, but the
   working copy has since gained appendices (3,097 lines vs 2,930).

### Widened beyond the directed scope

Four defects of the classes R2 escalated, found while applying its list, verified, and
corrected rather than left:

- `[00:36:17]` cited in **six** places for the day-count acknowledgement, which is at
  `[00:36:13]`–`[00:36:15]`.
- "Trap move / false move" first use cited `[00:33:33]` — not a marker, and not a passage
  about trap moves. It is `[00:30:40]`.
- `S33` cited `[00:45:40]`; the four-item recap is `[00:45:44]`.
- `AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` status blocks stale for the **third**
  time, invalidated again by the V02 pass adding `A-019`–`A-028` and `C-003`–`C-004`.

### Deliberately not done

Six cited timestamps in V01 files are not transcript markers — `[00:25:51]`, `[00:30:44]`,
`[00:35:38]`, `[00:38:02]`, `[00:39:43]`, `[00:40:26]`. Each lands inside the passage it
cites and resolves to the correct words. Fixing them **is** the `STUDY_PROTOCOL.md`
amendment R2 proposed and deferred to the 25% review. Retro-fitting an unadopted rule in
the round that certifies the lesson would apply a standard inconsistently, so they are
left in place and named as the case for adopting it (`REVIEW_INDEX.md` open item 7).

### Decision

```text
V01 R3: PASS — HIGH confidence. 0 critical, 0 major, 0 open minor, 2 open notes.
ADVANCEMENT AUTHORIZED. V02 opens; V03 does not.
```

### Process finding

`D-004` makes reviewer `PASS` the only progression gate and `COURSE_PROGRESS.md` recorded
`V02 GATE: CLOSED`, yet a complete V02 student pass ran while V01 was in remediation.
V01's `PASS` makes it moot and no V02 work is discarded — but the gate did not hold, which
is the whole value of a gate. Logged as `REVIEW_INDEX.md` open item 9. **V03 is gated
behind V02's reviewer `PASS`.**

### Files updated

`AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `V01_SOURCE_NOTES.md`,
`V01_INTERPRETATION.md`, `V01_MASTERY_REPORT.md` (`## Revision R2` appended),
`V01_TRANSCRIPT.md` (appendix note only — no transcribed speech touched),
`04_SCREENSHOTS/V01/INDEX.md`, `00_SYSTEM/DECISIONS.md` (`D-019` citation note),
`00_SYSTEM/SETUP_ISSUES.md` (`I-006`), `00_SYSTEM/QUARANTINE_REGISTER.md`,
`00_SYSTEM/COURSE_PROGRESS.md`, `18_REVIEW/REVIEW_INDEX.md`, `CHANGELOG.md`, and
`18_REVIEW/V01/V01_REVIEW_R3.md` (new). `R1` and `R2` untouched.

`validate_project.py`: 97 passed, 0 warnings, 0 failures.

### Next action

An **independent** reviewer session for V02 writes `18_REVIEW/V02/V02_REVIEW_R1.md`. It
should spot-check `A-006` and `A-003` while it is in those files, since no independent
session has audited this round.

---

## 2026-08-10 — Reviewer Session

### Lesson

V02 — `Bootcamp1 Wk1 031812 Part2 (60mins).swf`

### Review Objective

Independent mastery audit, round 1. Full 17-dimension protocol. Plus the `A-006` /
`A-003` spot-check that `V01_REVIEW_R3.md` requested, since R3 both remediated and
reviewed V01 in one session, departing from `D-003`.

**Independence:** this session produced none of V02's artifacts. `D-003` satisfied.

### Source Evidence Reviewed

`V02_TRANSCRIPT.md` read end to end (3,164 lines, 1,026 markers). Six V02 screenshots
opened at full resolution and their printed slide text compared character-by-character
against `INDEX.md` (`00:45`, `08:55`, `18:00`, `33:10`, `45:55`, `55:35`). Two V01
screenshots opened for the spot-check (`00-38-50`, `00-40-25`). The homework's USD/CHF
chart measured programmatically — candle pixels detected by colour, price axis
calibrated from its own labels, day boundaries taken from the chart's own gridlines.
Fifteen transcript term-counts verified directly against the verbatim body.

### Student Artifacts Reviewed

`V02_SOURCE_NOTES.md`, `V02_INTERPRETATION.md`, `V02_HOMEWORK.md` + charts,
`V02_MASTERY_REPORT.md`, `04_SCREENSHOTS/V02/INDEX.md`, `Q-002`, `A-019`–`A-028` and the
six extended V01 records, `C-003`/`C-004` and the `C-001` re-test, `COURSE_PROGRESS.md`,
`REVIEW_INDEX.md`, `D-003`/`D-004`/`D-018`/`D-019`/`D-020`/`D-021`,
`SWF_CAPTURE_RECIPE.md` §10, `V01_REVIEW_R3.md`.

### Findings

**0 critical. 1 major. 5 minor. 6 notes.**

**MAJOR — the 11a homework markup contradicts the chart it cites** (`E06`, also `E19`).
Measured off the committed PNG: "PFH Mon 3 Aug ~0.8130" — Monday's high is **0.81150**,
15 pips out against the file's own stated ±5 pip tolerance, and 0.8130 is not traded on
Monday at all. "Reverse | Fri 7 Aug | 0.8062 → 0.8130 sharp rise off the low" — that rise
is **Thursday's** (low 0.80601 early, 0.81355 at ~15:00); **Friday opened at its high and
fell to 0.80562**, the opposite direction. Rows 1, 4 and 5 are 10–15 pips out. The
consequence is what makes it major: §1 concludes *"the move away from the Monday high runs
Tuesday through Thursday — about three days — consistent with the printed 'For At Least
3 Days'"*, but price traded **back above** the Monday high on Thursday. That is a false
confirmation of the exact quantity `C-001` has open as foundational and unresolved — and
it is the only empirical datum the project has gathered about it. It propagates once, into
`V02_MASTERY_REPORT.md` §B ("the decisive extreme fell on Monday" — it fell on Thursday).

Contained, and not critical, because the student marked 11a ungraded and unverified,
self-graded Recognition **FAIL**, and neither the source notes nor the interpretation
cite the homework. `E09` (cherry-picking) and `E08` (hindsight) were considered and
**not** charged — the errors are consistent with hurried axis-reading, not selection.

**MINOR ×5:** three wrong occurrence counts in `V02_SOURCE_NOTES.md` §3 ("second leg"
~12 → 21; "the box"/"blue box" 6 → 9; "count the levels" 2 → 1); two ASR garbles repaired
inside quotation marks in a file that promises not to (`E01`); `CONTRADICTIONS.md` STATUS
says `UNRESOLVED: 1` when C-001, C-003 and C-004 are all unresolved — **fourth** occurrence
of this staleness class in that file, and introduced by the R3 edit correcting the same
block; `COURSE_PROGRESS.md` PHASE STATUS still reads Phase 1 blocked; a TradingView
history figure inconsistent between §0 and §2 of the homework.

**Upheld after independent verification:**

- **The homework data substitution is honest**, not silently faked. Flagged up front, the
  paywall evidenced with a screenshot that also shows how far back the free tier reaches,
  no account created, no bot check bypassed, and what is lost by substituting named
  precisely.
- **11b's `DEFERRED` holds and is not an excuse.** M/W formations are referenced ~14
  times across V01 and V02 and never described — no leg count, no proportion, no timing,
  no invalidation. `A-011` is correctly `Foundational` / `DO NOT CODE`, and the assignment
  asks for the *"one perfect"* M and W against a standard that does not exist. Producing
  forty cards would mean inventing the anatomy. Answering the mastery report's own
  question: a best-effort attempt with a labelled invented definition would be **worse**,
  because it becomes the anchor the next session reasons from.
- **The Q-002 quarantine is genuinely and completely done** — verified at the filesystem
  level. Three fabricated files in quarantine, none loose anywhere in the tree, README
  travelling with them, zero git-tracked.
- **The wrong-file capture is contained.** All 25 frames burn in `/ 60:2`; the discarded
  capture read `54:4`; content matches the transcript at every frame opened.
- **`A-006` and `A-003` both PASS** the requested spot-check, verified against the frames
  rather than R3's word. `[00:40:25]` prints "Trigger The Pendings"/"Trigger The Stops";
  `[00:38:50]` shows the pale-blue rectangle's left edge on the second vertical separator,
  over a sharp advance, confirming both the A-006 withdrawal and R2's narrowing. R3's
  remediation is substantively correct despite its `D-003` departure.
- **Gate state is coherent.** V02 OPEN with the ordering violation recorded rather than
  erased; V03 CLOSED; open item 9 still OPEN. This REVISE is the test of whether the next
  gate holds.
- **`E11`, V01's dominant defect across three rounds, does not recur.** ~20 sampled
  citations all resolved to markers carrying their words.

### Required Corrections

Ten, listed in `18_REVIEW/V02/V02_REVIEW_R1.md`. The first four concern the homework and
the mastery report; the rest are documentation. **The source notes and interpretation are
not to be rewritten** — they are sound. The original 11a markup must be preserved in
place per `REMEDIATION_PROTOCOL.md` §2.

### Decision

```text
REVISE — confidence HIGH. Advancement NOT AUTHORIZED.
```

Good work with one bad half-page in it. The evidence discipline — audio before visuals,
refusals recorded as refusals, inferences downgraded when they turn out to be the agent's
rather than the instructor's, a fabrication audit that confirms rather than assumes — is
the standard this project should keep. What failed is the one place the work left the
documents and touched a chart: sources were read rigorously, price was not.

### Git

`18_REVIEW/V02/V02_REVIEW_R1.md` (new). `18_REVIEW/REVIEW_INDEX.md`,
`00_SYSTEM/COURSE_PROGRESS.md`, `LOG.md`, `CHANGELOG.md` updated — reviewer-owned fields
only. **No student artifact was edited**, deliberately: findings 2–9 are remediation work
and belong to a separate session, per `D-003` and the R3 precedent.

### Next Review Trigger

Student resubmission of V02 → `18_REVIEW/V02/V02_REVIEW_R2.md`. **V03 stays closed.**

---

## 2026-08-10 — Remediation of V02 (Review R1)

### Objective

Address the ten required corrections from `18_REVIEW/V02/V02_REVIEW_R1.md`
(`REVISE`, HIGH — 0 critical, 1 major, 5 minor). **Fix-only pass.** No review verdict is
rendered here; R2 belongs to a fresh session per `D-003`.

### Findings Addressed

- **[E06/E19 / MAJOR] Homework 11a markup contradicts the chart it cites** → markup
  **redone from pixel measurement** of `charts/USDCHF_1H_2026-08-10_tradingview-fxcm.png`;
  the invalid first pass preserved in place as
  `SUPERSEDED — INVALID READING (R1 MAJOR 1)` per `REMEDIATION_PROTOCOL.md` §2. The
  "at least 3 days" confirmation is **withdrawn**. The `±5 pips` accuracy claim is
  withdrawn as untrue and replaced with a measured **±0.5 pip**.
- **[E20 / MINOR] Occurrence counts in `V02_SOURCE_NOTES.md` §3** → recounted by regex
  over the transcript's verbatim body only: "second leg" `~12`→**21**; "the box"/"blue
  box" `6`→**9**; "level count / counting the levels" `2`→**1**. Independently
  reproduced, not copied from the review.
- **[E01/E16 / MINOR] Two ASR repairs made silently inside quotation marks** → disclosed
  at the point of quotation with the transcript's verbatim wording, items 61 and 89.
  **A third undisclosed repair was found in the same quote** (`[00:45:39]` "That will
  draw" → "I will draw") and is disclosed too, along with the fact that item 61 silently
  merges two markers 7 s apart.
- **[E20 / MINOR] `CONTRADICTIONS.md` STATUS** → `UNRESOLVED: 3 (C-001 foundational;
  C-003; C-004)`.
- **[E20 / MINOR] `COURSE_PROGRESS.md` PHASE STATUS Phase 1** → `⛔ Blocked — no source
  videos` → `🔄 In progress`.
- **[E20 / MINOR] TradingView history figure** → `~7 months` withdrawn as unsourced;
  reconciled against the evidence screenshot.
- **[NOTE 9] Probable fourth "mayonnaise"** at `[00:05:00]` ("manays") → recorded as
  **probable, not confirmed**, in `V02_SOURCE_NOTES.md` §3 and `A-020`.

### Work Redone (not edited)

The 11a chart reading was **re-derived from the image**, not adjusted:

- Candle pixels selected by TradingView's exact body colours (±8).
- **Artifact caught:** the dashed current-price line at `y=434` is drawn in the *exact*
  bullish body colour and spans the chart. Uncorrected it reported the high of three
  separate days as exactly `0.81025` — the current price. Removed by requiring vertical
  continuity with `y=433`/`y=435`.
- Price axis calibrated by least squares over 13 unobstructed label centres:
  **52.27 px per 0.00100**, max residual **0.10 pip**.
- Day boundaries taken from the x-axis label lattice (bar pitch 6 px; labels centred on
  each day's first bar): Mon–Thu 24 bars, Fri 21, Sun 3.
- **Self-validation:** measured daily open equals the previous day's close on all six
  boundaries. This is what the first pass lacked — it had no check at all.

Corrected week (USD/CHF 1H FXCM, UTC): week low **0.80552** Sun 2 Aug 22:00; week high
**0.81356** Thu 6 Aug 15:00; Monday's high **0.81151** at 15:00 (first pass said
`~0.8130`, a price not traded that day); the sharp rise the first pass placed on Friday is
**Thursday's**, and Friday in fact opened at its high 0.81291 and fell to 0.80564.

### C-001 handling

Price held below Monday's high for **exactly 72 hours** before exceeding it. Recorded in
`CONTRADICTIONS.md` as **explicitly non-resolving**: three defensible counting conventions
give three different answers from the same series, and the choice of Monday's high as
"the level" is the reader's — `A-004` holds that the course's "level" is an ordinal leg,
not a price. **No day-count value is committed anywhere.**

### Containment preserved

R1 noted the error did not propagate. That was preserved deliberately: corrected numbers
were added **only** to the homework file, `V02_MASTERY_REPORT.md` §B (which cited the
withdrawn claim), and `CONTRADICTIONS.md` (as a non-resolving datum, which R1 required).
`V02_SOURCE_NOTES.md` and `V02_INTERPRETATION.md` still do not cite the homework, and no
new claim was introduced anywhere on the strength of one week.

### Flagged, not fixed

`V02_SOURCE_NOTES.md` §3 and `V02_TRANSCRIPT.md` both state `PFH`/`PFL` *"each appear
once"*. Counting the verbatim body: the **abbreviations appear zero times**; spelled out,
"peak formation high" once and "peak formation low" twice. R1 recorded verifying this
claim, so it is **left unedited and escalated to R2** rather than silently corrected.

### Git

Explicit paths only (I-009): `05_HOMEWORK/V02/V02_HOMEWORK.md`,
`03_LESSON_NOTES/V02_SOURCE_NOTES.md`, `07_MASTERY_REPORTS/V02_MASTERY_REPORT.md`,
`11_CONTRADICTIONS/CONTRADICTIONS.md`, `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`,
`00_SYSTEM/COURSE_PROGRESS.md`, `LOG.md`, `CHANGELOG.md`.
**`18_REVIEW/` was not touched** — it is reviewer-owned.

### Next Review Trigger

`18_REVIEW/V02/V02_REVIEW_R2.md`, by a **fresh session**. R2 should re-measure the chart
independently rather than accept the new pipeline's self-description. **V03 stays
closed.**

---

## 2026-08-10 — Reviewer Session

### Lesson

V02 — round R2.

### Review Objective

Verify the R1 remediation. Specifically: re-measure the homework chart independently rather
than accept `V02_HOMEWORK.md` §1.1's self-description (mastery audit request #1 and R1's
own closing instruction); confirm the five minor findings were applied; adjudicate whether
the `C-001` non-resolution is right in both directions; and rule on the two items the
remediation flagged rather than fixed.

### Working-Tree Integrity — checked before anything else

`HEAD` = `origin/<branch>` = `479ce72`, tracked tree clean, one untracked file
(`05_HOMEWORK/V02/measure_usdchf_week.py`). The reviewed content is the pushed content.
The untracked file was **excluded from the evidence base** — every finding was derived and
written from my own measurement before it was opened — then flagged as Note 8 and left in
place. It is not garbage: it runs, and it encodes the *correct* Sunday mapping.

### Source Evidence Reviewed

- `charts/USDCHF_1H_2026-08-10_tradingview-fxcm.png` — **re-measured from scratch.** Own
  candle detection, own sub-pixel axis calibration (**52.276 px per 0.00100**, max residual
  **0.088 pip**), own bar lattice (6 px, centres at `x ≡ 3 mod 6`), 177 bars extracted.
  Two absolute checks the remediation did not use: the **printed last-bar OHLC** in the
  chart header (my measurement matches it to **0.3 pip**, which is what actually
  substantiates the `±0.5 pip` claim), and the chart's **own dotted vertical day
  separators** at `x = 147, 273, 429, 573, 717, 861, 987, 1149`.
- `V02_TRANSCRIPT.md` — verbatim body isolated (line 86, 1,026 markers, 58,424 chars) and
  re-counted by regex for every changed count; all four quoted ASR passages retrieved and
  compared character-by-character against the new disclosures.

### Student Artifacts Reviewed

`V02_HOMEWORK.md` (whole), `V02_MASTERY_REPORT.md` §B + `Revision R1`,
`V02_SOURCE_NOTES.md` §§2e/2h/3, `CONTRADICTIONS.md`, `COURSE_PROGRESS.md`,
`AUTOMATION_AMBIGUITIES.md` A-020, `V02_INTERPRETATION.md` (containment only), the full
`9ab6645..479ce72` diff.

### Findings

**R1's MAJOR is CLOSED.** Every corrected price, day, direction and hour in §1.2
reproduces to within 0.2 pip — week low 0.80552 (Sun 22:00), week high 0.81355 (Thu
15:00), PFH 0.81150 (Mon 15:00), the rise being Thursday's at 75.4 pip in 13 hours, Friday
opening at its high and falling 72.7. So does §1.3's `C-001` result: first bar above
Monday's high is Thu 6 Aug 15:00, **72 hours exactly**. `E06`/`E19`-as-charged do not
recur. All five minor findings verified applied by re-derivation, not by reading the
corrected values ("second leg" 21, "the box"/"blue box" 9, "level count" 1, all confirmed).
Containment verified by grep: no homework-derived value appears in the canonical layer.

**3 MINOR, 0 MAJOR, 0 CRITICAL.**

1. `E19` — the Fri 31 Jul → Sun 2 Aug boundary is one bar out. Bar `x=267` is Friday's
   20:00, not Sunday's 21:00: the chart's own separators put 21 bars between `31` and
   `Aug` (a full Friday, matching Fri 7 Aug) and 26 between `Aug` and `4` (Sunday 2 +
   Monday 24); the two date labels §1.1 did **not** measure land on the correct bars to
   0.88 px and 0.03 px while missing §1.1's mapping by 5.1 px and 6.0 px; and the single
   open≠prior-close discontinuity in all 177 bars (**−12.63 pip at `x=273`**) is the
   weekend gap. §1.1's *"self-validating on all six boundaries"* claim therefore does not
   hold — the continuity test was applied at a weekend boundary, where continuity should
   not be expected, and the mapping was chosen to zero out a real gap. **No conclusion in
   the homework changes**; charged only because two files advertise §1.1 as the reusable
   pipeline for dimension G.
2. `E20` — the escalated `PFH`/`PFL` claim, adjudicated: **both abbreviations occur zero
   times**; spelled out, high 1 and low 2. Still live in `V02_SOURCE_NOTES.md` §3 and
   `V02_TRANSCRIPT.md`. The transcript-adoption decision (I-008) is **unaffected and
   strengthened**. Recorded against **R1**, which signed off on the check.
3. `E20` — `COURSE_PROGRESS.md`'s status view went stale in the same commit that declared
   the SUMMARY authoritative. Fifth occurrence of this class.

**`C-001` handled correctly, in both directions.** Not overreaching — the result is
refused twice, on the counting convention (three conventions, three answers) and on the
reader-selected level (`A-004`). Not too conservative — the datum is recorded in
`CONTRADICTIONS.md` with its precondition, so open item 10's warning against quietly
dropping it is satisfied. No day-count value is committed anywhere.

**Credit where due.** The third ASR repair (`[00:45:39]` *"That will draw"* → *"I will
draw"*) was found by the remediation and missed by R1, and disclosed unprompted along with
a two-marker merge nobody asked about. The `PFH`/`PFL` escalation is the reason a reviewer
error is visible at all. Neither is charged.

**PROCESS MAJOR — the V03 gate did NOT hold, and is being breached as I write.** It had
held at review start (`git status`: no V03 artifact). Re-running the integrity check before
staging showed the tree had since gained, from another session: `02_TRANSCRIPTS/V03/`
(`V03_TRANSCRIPT.md`, 1,230 entries, marked COMPLETE), empty `04_SCREENSHOTS/V03/` and
`05_HOMEWORK/V03/`, and `QUARANTINE_REGISTER.md` +102 lines adding `Q-003`, whose own text
says it was written *"before writing V03's notes"*. `COURSE_PROGRESS.md` reads `V03 GATE:
CLOSED` and V02 is unpassed. **Second occurrence, and unlike R1's it is not moot** — V02 is
`REVISE` with three corrections outstanding, one of them in the very measurement pipeline
V03's chart work would inherit. Charged as **process**, kept out of V02's mastery counts.
**Left untouched, unstaged, undeleted; no finding in R2 rests on it.** Disposition in
`V02_REVIEW_R2.md` §7: stop the V03 pass until V02 passes, do **not** discard the V03 work,
re-audit it afterwards, and enforce D-004 mechanically — two written rules failed in this
repository today (D-004 and the status-block rule of Minor 3), and the answer to both is a
check rather than another sentence.

### Required Corrections

Three, all narrow. §1.2 and §1.3 are **not** to be touched.
1. Correct the Sun 2 Aug and Fri 31 Jul rows in `V02_HOMEWORK.md` §1.1 (Sunday = 2 bars,
   open 0.80552, high 0.80737 at 23:00; Friday's open/low/close shift one bar), retaining
   the existing rows superseded in place per `REMEDIATION_PROTOCOL.md` §2, and restate the
   boundary reasoning using the chart's own day separators.
2. Correct the `PFH`/`PFL` count in both files; state that I-008 is unaffected.
3. Reconcile `COURSE_PROGRESS.md`'s PHASE STATUS row and `VIDEOS IN PROGRESS` to the
   SUMMARY.

Not required: 11b stays `DEFERRED`; G stays `DEFERRED`; A-019 stays open; the 2026-week
substitution stands; the `C-001` handling stands as written; source notes and interpretation
untouched.

### Decision

`REVISE` — confidence **HIGH**. 0 critical, 0 major, 3 minor. Advancement NOT AUTHORIZED.
**V03 remains gated.**

The generalisable lesson of the round, for `CUMULATIVE_25.md`: **a validity check must be
applied where its assumption holds**, and **the parts of a source you did not read are not
thereby ambiguous.** §1.1 measured six of eight date labels and declared the other two
ambiguous when they are decisive to better than one pixel — while the chart had been
drawing its own day boundaries the whole time.

### Git

Explicit paths only (I-009): `18_REVIEW/V02/V02_REVIEW_R2.md`,
`18_REVIEW/REVIEW_INDEX.md`, `00_SYSTEM/COURSE_PROGRESS.md`, `LOG.md`, `CHANGELOG.md`.
Student artifacts were **not** edited — the reviewer does not remediate.

**Deliberately NOT staged and NOT deleted** (three items, all from other sessions):
`05_HOMEWORK/V02/measure_usdchf_week.py`; `02_TRANSCRIPTS/V03/`, `04_SCREENSHOTS/V03/`,
`05_HOMEWORK/V03/`; and the unstaged `00_SYSTEM/QUARANTINE_REGISTER.md` Q-003 append. All
are reported in the review and none is incorporated into it.

### Next Review Trigger

Student resubmission of V02 after the three corrections → `18_REVIEW/V02/V02_REVIEW_R3.md`,
by a fresh session per D-003. **V03 stays closed, and the in-progress V03 pass must stop.**

### Addendum — commit collision, recorded 2026-08-10

**The R2 review was committed by another session, under a message that does not mention
it.** While this reviewer session was staging its five files, the concurrent V03 session
ran its own commit and swept the staged index into it. `1c836df`
*"feat: V03 transcript verified and adopted (I-008); Q-003 confirms V03 derived files
fabricated"* therefore contains **both** the gated V03 work **and** the entire R2 review
that flags that work as a D-004 breach — with a message describing only the former.

Verified before writing this: `18_REVIEW/V02/V02_REVIEW_R2.md` is in `HEAD`
**byte-for-byte identical** to what this session wrote (md5 `15fec440…`), the
`V03 GATE: CLOSED` line and its breach note survived intact, and nothing of this review was
altered or lost. **No content problem — a history problem.**

`1c836df` is **not** rewritten. It is already pushed, and rewriting shared history to tidy a
message would be worse than the untidiness, and would sit badly beside
`REVIEW_PROTOCOL.md` §12's *"never delete or rewrite old review decisions."* This addendum
exists so the R2 decision is findable in the log, and so the collision is recorded rather
than discovered later as a puzzle.

**Two process points, both mechanical rather than disciplinary:**

1. **This is the D-004 breach doing concrete damage**, not merely a paperwork violation. An
   ungated session running concurrently did not just create premature artifacts — it
   captured another session's staged work and mislabelled it. The `VNN GATE: CLOSED`
   pre-flight guard proposed at `REVIEW_INDEX.md` open item 14 would have prevented both.
2. **`git commit` with no pathspec is unsafe in this repository.** `I-009` already requires
   explicit paths for `git add`; it should require them for `git commit` too — `git commit
   -- <paths>` — so a session can never commit work it did not stage. Raise with the other
   two mechanical checks at the 25% review.

The R2 decision stands exactly as written: **`REVISE`, confidence HIGH, 0 critical, 0 major
on mastery, 3 minor, plus 1 MAJOR process finding (the live D-004 gate breach). Advancement
NOT AUTHORIZED. V03 remains gated.**

---

## 2026-08-10 — V02 R2 REMEDIATION, PART 1: §1.1's day boundary and the false self-validation

**Session:** Student (remediation). Applies **required correction 1** of
`18_REVIEW/V02/V02_REVIEW_R2.md` §9. Correction 2 (the `PFH`/`PFL` count) is **not**
applied in this pass and remains outstanding; correction 3 was discharged by the reviewer.

**What was wrong.** §1.1 placed bar `x=267` in Sunday 2 August when it belongs to Friday
31 July, and it settled that boundary with an open = prior-close continuity test — at the
one boundary in the week where a gap is the *normal* case. The test therefore selected the
mapping that made a real **−12.6 pip weekend gap vanish**, and the sentence *"it does, on
all six boundaries"* was never evidence that the mapping was right.

**What was applied.**

- `05_HOMEWORK/V02/V02_HOMEWORK.md` §1.1 — the day-boundary method row, the *"one boundary
  that had to be settled"* block and the daily OHLC table are **retained in place and
  superseded** per `REMEDIATION_PROTOCOL.md` §2, with corrected versions beside them. Day
  boundaries now come from **the chart's own dotted separators** at `x = 147, 273, 429,
  573, 717, 861, 987, 1149`. Sun 2 Aug = **2 bars**, open **0.80552**, high **0.80737
  `23:00`**; Fri 31 Jul open **0.80578**, low **0.80538 `00:00`**, close **0.80678**.
- The *"the `31` label is ambiguous"* and *"the same feed cannot give one Sunday three bars
  and the other two"* arguments are **withdrawn**, with the measurements that refute them
  (`31` centroid 146.12; `Aug` centroid 273.03; Sun 9 Aug carries three bars).
- The self-validation claim is **restated** rather than deleted: continuity holds on 174 of
  176 **bar** boundaries and is a valid *within-session* check; it cannot adjudicate a
  weekend boundary. Corrected in `V02_HOMEWORK.md` (§1.1 twice, §1.4), the R1 correction
  block at §1, `07_MASTERY_REPORTS/V02_MASTERY_REPORT.md`, `00_SYSTEM/COURSE_PROGRESS.md`
  and `11_CONTRADICTIONS/CONTRADICTIONS.md`.
- **The overstated reusability claim is corrected in both files that carried it** —
  `V02_HOMEWORK.md` §1.3 and `CONTRADICTIONS.md` C-001. §1.1's *price* measurement is
  verified and reusable; its *day-boundary* half was not, and §1.1 is explicitly **not** a
  fully general self-validating pipeline. Anything reusing it for dimension G must
  re-derive boundaries from that chart's separators and must not expect continuity across
  a weekend or session gap.
- §1.2 row 1's *"in its first four hourly bars"* → **the first bar of the week**.

**What was deliberately not touched.** §1.2's corrected markup and §1.3's 72-hour `C-001`
result — both independently reproduced at R2 and explicitly excluded from the correction
scope. `EFFECT ON C-001` remains **NONE**. No homework conclusion changed. The untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` is left in place, uncommitted and undeleted, per
R2 Note 8.

**Git discipline.** Per the R2 addendum's second process point, this commit used explicit
paths for **both** `git add` and `git commit`, with `git status` and `git diff --staged`
read immediately before committing, so no concurrent session's work could be swept in.

---

## 2026-08-10 — Reviewer Session

### Lesson

V02

### Review Objective

Independent verification of the R2 remediation (round 3). Both of R2's required
student corrections were to be **re-derived from the source**, not read from the diffs,
per the project's standing methodology that a correction is new work and carries the
same generalization risk as the original.

### Source Evidence Reviewed

- `05_HOMEWORK/V02/charts/USDCHF_1H_2026-08-10_tradingview-fxcm.png` — **re-measured
  from scratch** with an independent pipeline: exact-colour candle detection with the
  header, quote boxes and dashed last-price row masked; day separators detected by
  exact-colour column ink counts; price calibrated by least squares over the sub-pixel
  ink centroids of the 13 unobstructed right-axis labels; x-axis date labels measured
  the same way. **177 bars, 52.277 px per 0.00100, max residual 0.086 pip.** Validated
  against a ground truth external to the calibration — the chart header's *printed*
  last-bar OHLC — to **0.48 pip** worst case.
- `02_TRANSCRIPTS/V02/V02_TRANSCRIPT.md` — verbatim body isolated from the first
  `[00:00:00]` marker (58,424 characters, 1,026 markers) and re-counted by regex for
  `PFH`, `PFL`, the spelled-out forms, and `level count` / `count the levels`.
- Git history — `git status`, `git log`, and the full diffs of `8df7c32` and `d030a14`,
  read only **after** the independent measurements were complete.

### Student Artifacts Reviewed

`V02_HOMEWORK.md` §1.1–§1.4, `V02_SOURCE_NOTES.md` §3, `V02_TRANSCRIPT.md`
§"One thing was removed", `V02_MASTERY_REPORT.md`, `CONTRADICTIONS.md` C-001,
`COURSE_PROGRESS.md`, `REVIEW_INDEX.md`, `DECISIONS.md`.

### Findings

**Both required corrections are applied and both reproduce exactly.**

Correction 1 — every value verified independently: separators at
`x = 147, 273, 429, 573, 717, 861, 987, 1149`; bar counts 21/26/24/24/24/21/27; Sun 2 Aug
= **2 bars**, open **0.80552**, high **0.80737 `23:00`**; Fri 31 Jul open **0.80578**, low
**0.80538 `00:00`**, close **0.80678**; weekend gap **−12.63 pip**; `31` and `Aug` label
centroids **146.12** and **273.03**. The Mon–Fri rows and the 72-hour `C-001` datum were
re-derived too, to confirm the edit did not disturb what it was told not to touch — they
reproduce. `REMEDIATION_PROTOCOL.md` §2 verified line by line: all ten deleted lines have
superseded-in-place counterparts.

Correction 2 — `PFH` **0**, `PFL` **0**, "peak formation high" **1**, "peak formation low"
**2**, "peak formation" **4**. Exactly as stated, in both files, with the I-008 decision
correctly described as unaffected and strengthened.

**Two MINOR items remain, neither blocking:**

1. `V02_TRANSCRIPT.md` still asserts `level count` as a verbatim occurrence; the literal
   string occurs zero times (the referent occurs once, `[00:33:11]`). Ruled on at the
   student session's request: it **is** a real defect of the class just corrected, but
   `V02_SOURCE_NOTES.md` — the canonical layer — is already accurate and needs no change.
2. The *"174 of 176"* continuity figure does not reproduce (172 at the stated threshold,
   175 above 0.8 pip; three genuine sub-pip gaps besides the weekend one, confirmed
   visually at 4× zoom). **Recorded against R2, not the student** — the remediation was
   required to state R2's number and did so accurately.

**Notes:** every new positive claim in correction 1 reproduces to better than 0.1 px;
correction 2 shipped without a `LOG.md` entry; the V03 gate breach is now an
owner-authorized override that no `DECISIONS.md` entry records, so three files still
describe it as a live violation; `COURSE_PROGRESS.md` status staleness recurred for the
sixth time and was discharged by this session.

### Required Corrections

**None blocking.** Four carry-forward items, to be discharged at the next natural touch of
each file — `REVIEW_INDEX.md` open items 15, 16, 17 and the item-14 escalation. Item 12 is
**closed**. Do not open a remediation round for these.

### Decision

**PASS** — confidence HIGH. 0 critical, 0 major, 2 minor (non-blocking).
Advancement **AUTHORIZED**. `18_REVIEW/V02/V02_REVIEW_R3.md`.

### Git

Explicit paths for both `git add` and `git commit`; `git status` and `git diff --staged`
read immediately before committing. The untracked `05_HOMEWORK/V02/measure_usdchf_week.py`
is left in place, unmodified, unstaged and undeleted, and was excluded from this review's
evidence base.

### Next Review Trigger

V03 student pass. **The V03 gate is now OPEN** (D-004 satisfied by this `PASS`). The V03
work already performed in parallel is an owner-authorized override and is not to be
reverted; it should be recorded as a numbered decision in `DECISIONS.md`.

---

## Session — 2026-08-10 — V03 student pass (clean retry after a hung session)

### Situation inherited

A prior session began V03 and **hung while writing `V03_SOURCE_NOTES.md`**, producing no
output for a long time. This session was started as a clean retry. Verified state before
touching anything:

| Artifact | State found |
|---|---|
| `V03_TRANSCRIPT.md` | Committed (9f60f22 lineage), verified against I-008, adopted |
| 24 screenshots + `INDEX.md` | Committed |
| `V03_SOURCE_NOTES.md`, `V03_INTERPRETATION.md` | **Untracked**, 795 lines, unverified |
| `AUTOMATION_AMBIGUITIES.md` | Stopped at `A-028` while the notes cited `A-029`–`A-033` |
| `CONTRADICTIONS.md` | No V03 evidence at all |
| Homework, mastery report | Absent |

The hang landed between "notes written" and "registers touched", which is exactly where
the inherited state was inconsistent.

### Work performed, in commit order

1. **Citation audit of the inherited notes before adopting them.** 377 markers checked
   against the transcript (375 exist verbatim), 96 quote+timestamp pairs fuzzy-matched at
   their cited marker with ellipsis-elided quotes split fragment-by-fragment. All resolve
   to real spoken text. **5 minor defects found and fixed.** The notes were interrupted
   honest work, not fabrication — a materially different finding from Q-001/Q-002/Q-003.
2. **Visual verification of §4.** 4a/4c/4d/4f/4h transcribe their slides word for word;
   the burned-in player clock corroborates each filename timestamp. §4e listed 13 `R =`
   labels as complete when the frame carries **15** (two partially occluded) — corrected.
3. **`AUTOMATION_AMBIGUITIES.md`:** `A-029`–`A-036` added, 7 records extended, **`A-026`
   RESOLVED** — the project's first resolution on spoken evidence (`[00:26:40]`,
   "H-O-W high of the week"). ID collision between the notes and the screenshot index
   (both using `A-031`) reconciled across four files. STATUS recounted in the same commit.
4. **`CONTRADICTIONS.md`:** evidence on all four records, **no new record opened**.
   `C-004`'s deliberate V03 check performed as the record demanded → **negative**.
   One candidate examined and deliberately not logged.
5. **Homework 11a completed on real data, no substitution** — V03's slide prints "Any
   date range", so the 2012-data blocker that forced V02's substitution does not apply.
6. **`V03_MASTERY_REPORT.md`** — `REVIEW REQUIRED`.
7. `COURSE_PROGRESS.md`, `CONCEPT_INDEX.md`, this log, `CHANGELOG.md`.

### Homework method — the V02 lesson applied

V02's `MAJOR` was a measurement error caused by pixel reading (the price line shared a
colour with bullish candles). **This homework reads no pixels.** Every value is
TradingView's own OHLC legend harvested as DOM text, with three validations:

- **116 of 116** within-week bar transitions satisfied `open == previous close` exactly,
  to 5 dp (3 dp JPY), across all four pairs. Zero breaks.
- Weekend discontinuities landed at bar indices 25/26, 55, 85, 115 — **exactly 30 bars
  apart**, and 30 × 4h = one 5-day FX week. V02's R2/R3 finding used as a positive test.
- Two real-browser-hover spot checks matched the harvest to the last decimal, and their
  crosshair labels pin the week open at `Sun 02 Aug '26 21:00` UTC — the Asian session,
  as the lesson claims.

Two of my own intermediate errors were caught **by these checks before submission**: a
phase-lock that put EURUSD's window one bar out, and a day-label off by the Sunday open.

### What the homework actually found

- "dealer cuts one side of the block" — held **4 of 4**
- "price closes back inside the block after the cut" — held **4 of 4**
- "the cut is a false move and price runs the other way" — held **2 of 4**
- taught 2.5–3 day run window — measured **3.7–4.0 days, 4 of 4** (bears on `C-001`)
- taught 3 × ADR target — **reached 0 of 4** (1.42×–2.26×)

### Honest gaps

Homework 11b `UNRESOLVED` (no trading history to build flashcards from — same evidential
reason as V02's 11b; fabricating cards would reproduce the quarantined artifact class).
Manual backtesting `DEFERRED` (no testable entry rule to backtest). Recognition `PARTIAL`,
Discrimination `FAIL`, Sequence `PARTIAL`. Concept library still zero entries, deliberately.

`C-004`'s "no session-times slide" half rests on the prior session's 50-state sweep, of
which only the 24 committed frames were personally examined this session. **Flagged in
the mastery report rather than assumed sufficient.**

### Git

Explicit paths on every `git add`; `git diff --staged` read before every commit; six
incremental commits so a hang could not lose the work a second time. The untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` from another session was left in place,
unstaged and unmodified. `validate_project.py` 97 passed / 0 warnings / 0 failures at
each checkpoint.

### Next Review Trigger

**V03 independent review R1, in a fresh session.** The V04 gate is CLOSED until it
returns; D-024 governs what reopens it.

---

## 2026-08-10 — Reviewer Session

### Lesson

V03 — independent review R1, in a fresh session (D-003 satisfied; this reviewer
authored no V03 material).

### Review Objective

Independent mastery audit per REVIEW_PROTOCOL.md, run adversarially against the six
audit items nominated in V03_MASTERY_REPORT.md §4.

### Source Evidence Reviewed (first)

Full read of `V03_TRANSCRIPT.md` (1,230 entries) before any student conclusion; the
24 committed frames (5 inspected at full resolution, AJ chart re-cropped at 2×); the
**complete 857-frame sweep**, found intact in the prior session's scratchpad,
identity confirmed by pixel-exact match against the committed 12:39 slide,
independently re-clustered into 76 screen states, every state visually reviewed;
`Q-003`'s quarantined `RULES.md` opened directly and its fabrication confirmed
verbatim; ECB reference rates fetched as an external check on the homework data.

### Student Artifacts Reviewed (second)

Source notes, interpretation, homework (+ raw JSON + 4 charts), mastery report,
ambiguity records (A-026 resolution, A-029–A-036), contradiction updates (C-001–
C-004), screenshot index, LOG/COURSE_PROGRESS/CONCEPT_INDEX, validate_project.py
re-run.

### Findings

**0 CRITICAL, 0 MAJOR, 3 MINOR, 5 NOTES.** Everything load-bearing reproduced:
425 marker citations checked for existence and 99 quote+timestamp pairs re-matched
at exact marker resolution (all resolve — the student's 375-of-377 audit claim is
confirmed, and its ±45 s window masked nothing); the §4e fifteen-R-label correction
re-derived independently; A-026's "H-O-W high of the week" read directly at
[00:26:40]; the homework's 116/116 chain validation and every derived figure
recomputed from the committed JSON; the dataset corroborated externally (ECB fixes
inside the harvested bar ranges, all four pairs, all five days); no DST transition
falls inside the analysed week; **the C-004 negative claim verified on the full
sweep — no session-times slide exists in V03** (mastery report audit item 6
discharged). Minors: M1 ADR figures not re-derivable from committed data (E19);
M2 transcript coverage block falsely claims "strictly monotonic, no duplicates"
(E20 — three benign same-second duplicates); M3 the 2.5–3-day-window finding stated
as 4-of-4 where 2-of-4 measure the taught object (E02 — scope before citing against
C-001). Notes include the Easter-vote housekeeping slide absent from all coverage
(N2) and the three-lesson manual-backtest debt (N4, carried open).

### Required Corrections

M1–M3, specified in `18_REVIEW/V03/V03_REVIEW_R1.md`. Documentation-precision only;
no conclusion changes.

### Decision

**REVISE, confidence HIGH.** Under D-024 (0 critical, 0 major) the **V04 gate is
OPEN**; the minors are owed before V03 reaches COMPLETE.

### Git

Explicit paths on every `git add`; staged diff read before commit; the untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13, another session's artifact)
left in place unstaged. Files: `18_REVIEW/V03/V03_REVIEW_R1.md` (new),
`18_REVIEW/REVIEW_INDEX.md`, `00_SYSTEM/COURSE_PROGRESS.md`, `LOG.md`.

### Next Review Trigger

Student application of M1–M3 (verify at V03's next review touch, which may ride
along with V04's R1 rather than opening a dedicated round); V04 R1 after the V04
student pass.

---

## 2026-08-10 — V03 R1 REMEDIATION (M1–M3, minors only)

### Scope

Mechanical correction pass against `18_REVIEW/V03/V03_REVIEW_R1.md`. All three
minors applied. No conclusion in any file changed. V03 stays `REVIEW REQUIRED`
until a reviewer verifies the fixes; the V04 gate was already OPEN per D-024 and
is untouched by this pass.

### M1 (E19) — ADR figures now re-derivable

The committed figures (47.0 / 54.8 / 148.2 / 56.5) could not be reconstructed
under any convention, so they were **recomputed under an explicitly stated one**
rather than reverse-engineered. Convention now written into `V03_HOMEWORK.md`
§2.5 Finding B: the **FX day beginning 21:00 UTC**, which is the dataset's own
week-open boundary and the only convention that divides the 30 bars into five
whole days — day 1 = bars 0–5, day 2 = 6–11, day 3 = 12–17, day 4 = 18–23,
day 5 = 24–29; a day's range is max(high of its six bars) − min(low of its six).
All **twenty daily ranges are now committed in the file** (four pairs × five
days), so the ADR column re-derives by inspection.

New ADR: EURUSD 46.5, GBPUSD 55.7, USDJPY 138.9, USDCHF 54.4 → 3×ADR 139.6 /
167.2 / 416.8 / 163.3, multiples 1.73× / 1.64× / 2.41× / 1.48×. The superseded
figures are retained in an in-file correction note rather than deleted.
**0 of 4 reached 3 × ADR — unchanged**, as it was under every convention the
reviewer tested (1.46–2.61 across all of them).

### M2 (E20) — transcript coverage wording

`V03_TRANSCRIPT.md` I-008 block: *"1,230 timestamps, strictly monotonic, no
duplicates"* → **"1,230 timestamps, 1,227 distinct, non-decreasing throughout
(never decreasing), with three benign same-second adjacent pairs at
`[00:35:21]`, `[01:00:13]` and `[01:04:30]`"**, plus a correction note. Counts
re-verified this session by regex over the file (1,230 markers, 1,227 unique,
adjacent duplicates exactly the three named, sequence never decreasing).
**V02's identically-worded line was checked as well and is true as written**
(1,026 markers, all distinct, no adjacent duplicates) — no change made there.

### M3 (E02) — duration finding scoped to its real sample

`V03_HOMEWORK.md` §2.5 Finding A: the table gains a per-pair *"does this measure
the taught object?"* column (EURUSD low at bar 4 and GBPUSD low at bar 5 — both
after the block low was cut, both **Yes**; USDJPY and USDCHF have the week's low
at bar 0, no cut, no anchor formed, both **No**), an explicit statement that the
finding is **supported 2 of 4, not 4 of 4**, the note that the two excluded pairs
measure open-to-high of a trending week (a different object, retained unbolded as
raw measurement), and the standing instruction that **any citation of this datum
against `C-001` must carry the 2-of-4 scoping**. Same scoping applied to homework
§4 point 3 and to `V03_MASTERY_REPORT.md` §2 (exit-rule table) and §D (sequence
dimension row). Both supported pairs are 3.8 days — still exceeding the taught
2.5–3 day window, so the direction of the evidence is unchanged.

`CONTRADICTIONS.md` C-001 was left unedited: it does not yet cite the homework
duration datum, and M3's requirement is that the scoping travel with the datum
when it is first cited there.

### Git

Explicit paths on every `git add`; `git status` and `git log` checked first and
the staged diff read before commit. The untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13, another session's
artifact) was left in place, unstaged, again.

### Next Review Trigger

**R2 verification of M1–M3** — may ride along with V04's R1. V03 reaches
`COMPLETE` only when a reviewer confirms these three.

---

## 2026-08-10 — Reviewer Session

**V03 independent review, round 2 (`18_REVIEW/V03/V03_REVIEW_R2.md`).**
Verdict **`REVISE`**, confidence HIGH — **0 critical, 0 major, 1 minor.**

Remediation-verification round on commit `683a12a`. Fresh session; no V03 material
and no part of the remediation was authored here (D-003). R1's substantive
adjudications were not re-opened. Each of the three minors was **re-derived from
primary data** rather than read for plausibility.

### M1 (E19) — VERIFIED, CLOSED

Three questions put to the raw JSON. **(1)** 21:00 UTC does produce clean 6-bar
splits — the dataset is 30 consecutive 4h bars opening Sun 02 Aug 21:00 UTC, so
30 ÷ 6 = 5 aligned to bar 0, and it is the *only* 4h-aligned boundary that yields
five whole days (any other leaves a partial first and last day), which makes the
file's stronger claim true rather than rhetorical. 116/116 open=prev-close
continuity re-confirmed as the precondition. **(2)** All twenty committed daily
ranges reproduce **exactly**, to a tenth of a pip; ADR 46.52 / 55.72 / 138.92 /
54.44 → the committed 46.5 / 55.7 / 138.9 / 54.4; 3×ADR and the multiples
(1.730 / 1.637 / 2.407 / 1.477) follow. **(3)** 0 of 4 reaching 3×ADR holds with
margin — the largest multiple is 2.41×, not a boundary case — and the superseded
figures were re-checked too, so the correction note is accurate. The E19 defect
(a number bearing on `C-001` that is not re-derivable) is fully cured.

### M2 (E20) — WORDING VERIFIED, PLACEMENT DEFECTIVE — STILL OPEN

Every component of the replacement line was re-derived by regex and **all seven
check out**: 1,230 markers, 1,227 distinct, zero decreasing transitions, exactly
three adjacent same-second pairs at exactly `[00:35:21]` / `[01:00:13]` /
`[01:04:30]`, largest gap 13 s at `[01:09:02]`, final `[01:10:39]`. **But the
sentence lives in two places in the file.** The correction was applied to the
`PROVENANCE AND VERIFICATION` I-008 criterion (lines 39–46); the **`COVERAGE`
block (lines 23–24), which is what R1 quoted and what required correction 2
named, still reads *"timestamps strictly monotonic, no duplicates"***. The file
now asserts both propositions fourteen lines apart. Carried as **R2 M2′** — same
E20 occurrence, incompletely remediated, not double-counted.

The V02 cross-check was **independently re-tested, not trusted**: 1,026 markers,
1,026 distinct, zero decreasing transitions — strictly monotonic with no
duplicates is **true as written** for V02, and leaving it alone was correct.
Swept the class a third time: `V01_TRANSCRIPT.md` has five same-second pairs
(974 / 969) but makes no monotonicity claim, so nothing is false there. Once
M2′ is applied the E20 class is empty project-wide.

### M3 (E02) — VERIFIED, CLOSED

Re-derived from the raw OHLC: USDJPY and USDCHF have `cut_lo` = **0 bars** — the
block low is never taken out, and it *is* the week low at bar 0 — so no stop hunt
occurs and no anchor exists to measure a run from; EURUSD and GBPUSD cut the block
low at bar 2 and form their lows at bars 4 and 5, both 92 h = 3.83 days. The
2-of-4 scoping is correct, consistent with §2.4's rejection of the same two pairs,
and costs the finding no direction. Propagation confirmed at all four named sites
plus a whole-repo grep for surviving pre-correction figures — clean. The stale
numbers at `LOG.md` 1746–1747 are a historical journal entry superseded at
1859/1892 and **must not be edited**; noted so a future session does not "fix" the
record.

The `C-001` deferral was tested by **reading the record**, not by accepting the
claim: the `C-001` record and the V03 evidence section cite five transcript
restatements and the new exit rule at `[00:36:11]`–`[00:36:16]`, and no
homework-measured duration appears anywhere in the file. The datum is genuinely
not yet cited, so pre-emptively editing `C-001` would have inserted a claim the
record does not make. The standing instruction is committed in both homework
§2.5A and mastery report §2 — where a future session will actually be standing
when the obligation bites. Correct handling.

### Reviewer-side updates

`REVIEW_INDEX.md`: R2 row added to the DECISION TABLE; open items **18 and 20
CLOSED**, item 19 re-opened with a corrected status (it had recorded the fix as
applied to `COVERAGE` when it was applied to the I-008 criterion); `E19` marked
closed and `E20`'s V03 entry marked still-open; severity totals updated (MINOR
open 8 → 6). `COURSE_PROGRESS.md` reconciled. `validate_project.py`: 97 passed,
1 warning, 0 failures — the warning is `V04: 27 screenshots but no INDEX.md`,
belonging to a V04 session active in this working tree, not to V03.

### Git

Explicit paths on every `git add`; `git status` and `git log` checked first and
the staged diff read before commit. A V04 student session is active in this same
working tree — its untracked `05_HOMEWORK/V04/` and the untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13) were left in place,
unstaged, and no V04 file was touched.

### Next Review Trigger

**Application of M2′** — one sentence in `V03_TRANSCRIPT.md` `COVERAGE` lines
23–24, plus `REVIEW_INDEX.md` item 19's status text. On its verification V03
reaches `COMPLETE`. May ride along with V04's R1.

---

## 2026-08-10 — V04 student pass (Student session)

**Lesson:** V04 — `Bootcamp1 Wk2 032512 Part2 (86mins).swf`, 01:25:41, Week 2 part 2.
**Gate:** V04 gate was **OPEN** per `D-024` (V03 R1 returned `REVISE` with 0 `CRITICAL`,
0 `MAJOR`, 3 `MINOR`). Confirmed in `COURSE_PROGRESS.md` before any V04 artifact was created.
**Outcome:** student pass complete, submitted as **REVIEW REQUIRED**. V04 → `AWAITING REVIEW`.

### What V04 turned out to be

Two things make this lesson different from V01–V03, and both shaped the whole pass.

**1. It states the course's first near-complete entry rule.** At `[00:15:34]`–`[00:15:57]`
the instructor delivers a labelled three-condition list — 25–50 pips beyond the blue box,
second leg of an M/W, TDI shark fin out-and-back — and surrounds it with a stop (10–18
pips), a trigger (the second leg's close), an invalidation, a re-entry doctrine and a
2.5–3-day holding window. **But condition (c) requires TDI, which the course has deferred
twice** (V03 `[01:01:53]`, V04 `[00:22:11]`), and which the instructor could not even
display on his own example chart. So V04 states a rule it does not equip a student to
apply. That single gap is why dimensions B, C and G are all sub-`PASS`.

**2. 69% of the runtime is not the course's author.** The instructor teaches
`[00:00:00]`–`[00:26:56]`; an unidentified guest presenter takes the remaining 59 minutes.
The transcript has **no speaker labels** and the handover is unannounced. Every source row
is now tagged `INSTRUCTOR` or `GUEST`, no `GUEST` statement enters the methodology, and
`C-005` records the conflict — `UNRESOLVED` **pending a scope ruling, not pending
evidence**, since no future lesson can settle it.

### Capture

10× fast sweep per `SWF_CAPTURE_RECIPE.md` §10 / `D-021`: 1,037 frames at 5
presentation-second spacing, ~8.6 minutes wall clock. Original SWF SHA-256-verified
unchanged after patching the working copy. **`D-022` port/byte verification mattered
again** — ports 8899, 8917 and 8931 were all still held by stale servers from earlier
sessions, exactly the GOTCHA 4 hazard. Took 8944, confirmed own PID, SHA-256-matched the
served bytes. Content was sanity-checked against the transcript inside the first minute:
the probe frame at `05:00` carries a hand-drawn "-180" and `[00:04:52]` says *"Don't stand
aside minus one eighty."*

### Transcript (I-008)

Verified and adopted. Duration cross-checked two independent ways (audio 5141.03 s; SWF
header 15,425 frames ÷ 3.0 fps = 5141.7 s). Five Whisper `base.en` windows re-transcribed
and compared; all matched near-verbatim.

**A real defect was found and fenced rather than deleted:** the final 9 entries
`[01:25:40]`–`[01:26:04]` are a degenerate ASR repetition loop, and **8 of them are
timestamped up to 23 seconds past the end of the audio file.** Retained inside an explicit
fence; no artifact may cite them. The coverage block states the true weaker property
(non-decreasing, 6 same-second pairs) rather than repeating V03's *"strictly monotonic"*
overclaim (`M2`).

### Q-004 — and a finding that retires a question for all 21 lessons

V04's three derived files are individually confirmed fabricated (four of four lessons
checked now). **New this pass:** two greps establish mechanically that **all 21 `RULES.md`
files carry the same two fabricated "verbatim instructor statements" at the same two
timestamps** — `[00:05:00]` and `[00:18:00]`. The one-template theory is now measured
rather than inferred, and **no future per-lesson `RULES.md` audit can come back clean.**

Also: `VISUAL_INDEX.md`'s single real image is **authentic but doubly mislabelled** — it is
the frame at `[00:00:00]`, not `[00:02:00]` (matched to sweep frame `s_0000` at 0.65 mean
absolute difference), and its description is invented.

### Homework — completed on real data, no substitution

*"The four majors, any time range"* `[00:18:04]` delegates the date, so a recent week is
compliance. Week of Sun 02 Aug 2026 21:00 UTC. **No price read from a pixel** — platform
OHLC legend as DOM text. Both harvest scripts committed.

Four independent validations: the open==prev-close chain on the 30-bar weekend cadence;
**476/480 OHLC fields agree with V03's independently committed dataset** (different
session, different script, same week); **474/480 agree between this session's own 4h and
15m harvests** (which is also what anchors the 15m series, since the crosshair date is
canvas-drawn); and a deliberate harvest-stability test that **found a real defect** —
28 ms vs 75 ms hover dwell disagree on 5/480 fields — measured at ~±0.4 pip and disclosed.

Findings: the first-eight-hours block measured for all four majors; the week's high formed
Thu/Fri in **4 of 4** and the literal claim *"track to the high on Sunday or Monday"* is
**0 of 4**; duration from the early extreme to the opposite extreme is **3.83 days on both
formed-anchor pairs** — which **independently reproduces V03's corrected `M3` figure** from
a fresh harvest. **No M/W classification is claimed** on the 15-minute charts, because
`A-011` leaves the pattern undefined; peak descriptors are reported across four tolerances
instead. **`C-001` unaffected; no day-count value committed anywhere.**

### Registers

`A-037`–`A-041` added; **10 earlier records extended, none resolved.** `C-005` opened;
`C-001` extended with a source that restates V01 Source A near-verbatim and adds the
terminating condition it lacked. **`C-004` deliberately re-checked because its own
"Required to resolve" field named V04** — all 1,037 frames segmented into 47 states with
one representative per state reviewed, and all 47 time-related transcript entries read.
**Negative on both halves; V03 and V04 are now both struck off.**

### Defects in my own work, caught and fixed before commit

Recorded because the mastery report asks the reviewer to assume more of the same exists in
what was not mechanically checked.

1. **`E01` — ASR garble repaired inside quotation marks** in ~20 places in the source-notes
   draft (`"bibs"`→`"[pips]"`, `"an AM"`→`"an [M]"`). Caught by a verbatim audit of 172
   quoted fragments; all restored, glosses moved outside the quotes. 171/172 now exact.
2. **Three duplicate ambiguity IDs** — my draft's new records duplicated existing `A-018`,
   `A-030` and `A-031`. Caught by reading the register before writing. Remapped to extensions.
3. **An overclaim about "Mayo"** — I wrote that V04's printed caption settles the spelling;
   **V03 had already done that.** Rescoped to what V04 actually adds.
4. **A transposed digit** in USDJPY's block high (158.885 → 157.885) and an **inflated
   transition count** (571 → 569) in the homework, both caught by recomputing every figure
   from the committed file alone.
5. **A misnamed index file** — `V04_VISUAL_INDEX.md` where the project convention is
   `INDEX.md`; the V03 R2 reviewer's validator run flagged it. Renamed.

### Bookkeeping

`COURSE_PROGRESS.md` merged carefully around a **parallel session** that ran V03's
remediation and R2 review in this same working tree during this pass — their V03 content
was preserved, not overwritten. `V05 GATE: CLOSED` block added. `REVIEW_INDEX.md` gains
`AWAITING REVIEW: 1` and open items **22–24**. `validate_project.py`: **97 passed,
0 warnings, 0 failures.**

### Git

Explicit paths on every `git add`; `git status` and `git log` checked first and the staged
diff read before every commit. Seven checkpoint commits, each pushed. The untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13) was left untouched and unstaged
throughout, and no V03 file was modified.

### Next Review Trigger

**Independent review of V04 (R1)** by a fresh session (`D-003`). The mastery report
nominates **seven** items for audit, the first two being the `C-005` scope call and the
dimension-G `DEFERRED` disposition.

---

## 2026-08-10 — Reviewer Session

### Lesson

V03 — review round **R3** (closing round).

### Review Objective

Verify the single remaining minor from R2 — `M2′`/`E20`, the residual *"strictly
monotonic, no duplicates"* sentence in `V03_TRANSCRIPT.md`'s `COVERAGE` block — was
correctly applied by commit `492bb11`, and that the resulting text is **true**, re-derived
from primary data rather than read against the commit message. R1's and R2's substantive
adjudications were not re-opened; M1 and M3 closed at R2 and were not re-litigated.

### Source Evidence Reviewed

- `02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md` — full independent line-anchored marker scan over
  all 3,802 lines: totals, distinct count, every decreasing transition, every adjacent
  same-second pair, the four largest gaps, first/last entry, and the line span the counted
  markers occupy.
- `02_TRANSCRIPTS/V01,V02,V04/*_TRANSCRIPT.md` — same scan on all three, to re-test the
  "E20 class is empty project-wide" claim rather than inherit it.
- `git show 492bb11` — the diff itself.
- Repo-wide grep for `strictly monotonic`; `LOG.md` 1740–1752 and 1848–1917.
- `scripts/validate_project.py` — **97 passed, 0 warnings, 0 failures.**

### Student Artifacts Reviewed

`V03_TRANSCRIPT.md` `COVERAGE` (lines 18–26) and `PROVENANCE`/I-008 criterion 1
(lines 39–47), read against each other and against the scan.

### Findings

**0 CRITICAL, 0 MAJOR, 0 MINOR. `M2′` is discharged.**

Both blocks now assert the same proposition, and every component of it reproduces:
**1,230 markers, 1,227 distinct, 0 decreasing transitions, exactly 3 adjacent same-second
pairs at `[00:35:21]` / `[01:00:13]` / `[01:04:30]`, largest gap 13 s at `[01:09:02]`
(a clear maximum — next are 12 s, 12 s, 11 s), final entry `[01:10:39]`.** The
distinct-count and duplicate-count are mutually consistent (1,230 − 1,227 = 3, all three
duplicates adjacent). A counting artifact was explicitly ruled out: a naive whole-file
scan returns 1,256 brackets, but all 1,230 counted entries fall between lines 115 and
3,802, below the last `##` heading at line 87 — so none come from the header blocks.
The diff touches one file and five lines, inside `COVERAGE` only; lines 39–47 are intact.

No third instance of the claim survives. The `E20` monotonicity class is now **empty
project-wide** on a fresh scan: V01 974 / 969 with five same-second pairs but no
monotonicity claim; V02 1,026 / 1,026, genuinely strict, its identical wording true as
written; V04 states the weaker true property.

`LOG.md` 1746–1747 confirmed **untouched** by `492bb11` (which touches no log file) and
properly superseded in-file by the `V03 R1 REMEDIATION` entry at line 1848 — M1's figures
at ~1859–1875, M3's scoping at ~1892–1912, each naming the value it replaces. Correct
append-only handling; **must not be "fixed" by a future session.**

Four notes, all closed as observations: the fix commit appended no log entry (this entry
fills the hole); a marker-scan counting trap that produces a phantom decreasing transition
in V04 if its `COVERAGE` fence lines are not excluded (V04's own claim is **not**
contradicted — 1,601 genuine entries, as stated); `V04_TRANSCRIPT.md` line 30's now-stale
pointer to open item 19; and the clean validator run.

### Required Corrections

**None.** V03's remediation debt is discharged in full.

### Decision

**PASS** (confidence HIGH). **V03 is COMPLETE.** `REVIEW_INDEX.md` open item **19
CLOSES**, completing items **18–20**. The V04 gate, already OPEN under `D-024` since
V03 R1, is now open on V03's own `PASS`.

### Bookkeeping

`18_REVIEW/V03/V03_REVIEW_R3.md` written per protocol §11 (R1 and R2 untouched).
`REVIEW_INDEX.md`: `STATUS` block, R3 narrative, `DECISION TABLE` V03 R3 row, `E20`
row, severity totals (MINOR open 6 → 5; NOTE 27 → 31), open item 19 → CLOSED with its
prior status retained. `COURSE_PROGRESS.md`: summary counts, V03 status block, V04 gate,
"still owed" note, lesson table row, and the phase-1 line. A parallel V04 session is
active in this working tree; no V04 file was touched.

### Git

Explicit paths on every `git add`; `git status` and `git log` checked first and the staged
diff read before committing. The untracked `05_HOMEWORK/V02/measure_usdchf_week.py`
(open item 13) was left untouched and unstaged.

### Next Review Trigger

**Independent review of V04 (R1)** by a fresh session (`D-003`) — unaffected by this
decision, which only removes V03's dependence on the `D-024` deferral.

---

## 2026-08-10 — Reviewer Session

### Lesson

V04 — `Bootcamp1 Wk2 032512 Part2 (86mins).swf`, R1.

### Review Objective

Independent mastery audit of V04, the first structurally atypical lesson in the course, plus
an explicit **scope ruling on guest-presenter material** (`C-005`) requested by the student
session and carried as `REVIEW_INDEX.md` open item 22.

Fresh session; no V04 artifact was authored by this reviewer (`D-003`). Source read before
student conclusions (`REVIEW_PROTOCOL.md` §3): `DECISIONS.md` D-001…D-024,
`REVIEW_PROTOCOL.md`, `REVIEW_INDEX.md` and `MASTERY_STANDARD.md` first, then the V04
transcript and frames, then the student's files.

### Source Evidence Reviewed

- `V04_TRANSCRIPT.md` — the speaker seam at `[00:26:51]`–`[00:27:02]` read directly; every
  `Steve` and `Carl` occurrence in the body located and read in context; all 13 `TDI`
  occurrences read; `[00:15:22]`–`[00:16:31]` (the criteria list), `[00:13:40]`–`[00:14:06]`,
  `[00:22:02]`–`[00:22:21]`, `[00:04:52]`–`[00:05:14]`, `[00:17:51]`–`[00:18:14]`,
  `[00:50:32]`–`[00:50:42]`, `[01:10:32]`–`[01:10:54]` read verbatim; the fenced tail read
  in full.
- V03 `[01:01:53]` and V01 `[00:35:03]`–`[00:35:11]` read at source for the cross-references.
- Frames `01-04-10` and `01-08-40` opened and magnified 4× — Navigator account rows and the
  indicator sub-panel title read off the pixels, burned-in player timecodes checked against
  the filenames.
- All 21 quarantined `RULES.md` files, and the V04 `NOTES.md` / `VISUAL_INDEX.md` folder.

### Student Artifacts Reviewed

`V04_TRANSCRIPT.md`, `V04_SOURCE_NOTES.md`, `V04_INTERPRETATION.md`,
`04_SCREENSHOTS/V04/INDEX.md`, `V04_HOMEWORK.md` + its committed JSON and both harvest
scripts, `V04_MASTERY_REPORT.md`, `AUTOMATION_AMBIGUITIES.md` A-030…A-041,
`CONTRADICTIONS.md` C-004/C-005, `QUARANTINE_REGISTER.md` Q-004.

### What was re-derived rather than read

- **487 of 487** cited timestamps across five V04 artifacts resolved against parsed marker
  sets for all four transcripts. Zero unresolved. `E11` absent for a third lesson.
- **320** italic-quoted fragments extracted, ellipsis-split, gloss-stripped and matched
  against the normalised genuine transcript body. 44 initial misses triaged: 42 legitimate
  (printed slide/caption text, cross-lesson quotes each verified at source, the student's own
  prose). **2 genuine** — finding M2.
- Homework recomputed from the committed JSON with a script written this session:
  **476/480** vs V03's dataset with the four differing fields identified individually;
  **474/480** 4h↔15m with per-pair bar counts; every block figure and percentage; every
  weekly extreme and its bar index; **23 bars = 92 h = 3.833 days** on both formed-anchor
  pairs; **116/116** in-week 4h continuity. All match.
- Fabrication template measured over all 21 `RULES.md`: both quotes 21/21, both timestamps
  21/21, exactly 2 rules 21/21, **`NUMERICAL PARAMETERS` byte-identical, one hash, 21/21**;
  `INFERRED VISUAL RULES` and `TERMS` two variants each. `EMA` occurs 0× in V04's transcript.
- Transcript entry count re-parsed: **1,601**, matching the coverage block's 1,592 + 9.
- Guest share of runtime: 3,518 s / 5,137 s = **68.5%**.

### Findings

**0 CRITICAL, 0 MAJOR, 7 MINOR, 5 NOTE.**

`M1` (`E19`) USDCHF's 15-minute series mis-sliced at a partial week-open bar and its 27/30
symptom misdiagnosed as ±0.4 pip harvest noise when bar 0's open differs by 28.1 pips —
diagnosed here, `aggregate(m[4:16])` reproduces 4h bar 0 exactly; no conclusion changes.
`M2` (`E01`) two smoothed quotations inside the transcript's own verbatim-proof paragraph.
`M3` (`E20`/`E11`) `A-037`/`A-038` cross-references pointing at records that hold other
subjects; correct targets `A-031`/`A-030`. `M4` (`E20`) stale "26 frames" and stale
`VISUAL_INDEX` filename. `M5` (`E20`) homework validation 1's 569/549/20 figures not
reproducible from committed data. `M6` (`E20`) a visible `Traders Dynamic Index Visual`
panel in curated frames 21 and 22, unrecorded — does not weaken `A-039`. `M7` (`E20`) four
quality-control boxes unchecked and undeclared, shared with V02 and V03.

`N1` requires dimensions B and C to be re-dispositioned from `PARTIAL`/`FAIL` to `DEFERRED`
under `D-019` — as labelled, V04 could never reach `PASS`, because the cause is in the
source. `N2`–`N5` uphold the manual-backtest debt characterisation, the `I5` anchor-point
recommendation at its stated grade, the `E11` de-escalation, and record the round's most
transferable observation: the student predicted its residual defects would be in the
interpretation prose; they were not — all four substantive minors landed in the **narrative
describing mechanically checked work**, because that is the one part nothing recomputes.

### The C-005 ruling

**Guest-presenter material is admissible as SECONDARY, DESCRIPTIVE evidence and is EXCLUDED
from the canonical methodology as NORMATIVE material.** Not full weight (the guest disclaims
authority in his own words and describes a session where the instructor's necessary
condition mostly does not occur — merging would synthesise a rule set neither man stated);
not full exclusion (that would require retracting `A-040`, the *"Mayo"* corroboration and
half of `INDEX.md`, all of which are facts about printed artifacts rather than claims about
method). Speaker tagging is mandatory from V04 forward; a guest statement can never resolve
an `A-xxx` or `C-xxx`; a guest/instructor divergence is a corpus-hygiene record, never a
contradiction charged against the instructor; identification is provenance, not evidence.
**Retroactive effect on V04: none — it ratifies the student's handling exactly.** Owner to
record as `DECISIONS.md` D-025 before V05.

The speaker identification was verified independently and is correct: *"Zen Jason … or
Diana I. Alldredge"* read off frame 21's Navigator at 4× magnification (three account rows),
and segment B refers to Steve in the third person 40+ times, decisively at `[01:24:53]`
*"Steve is asking, do you ever take continuation trades?"*

### Required Corrections

`REVIEW_INDEX.md` open items 25–32; the executive block of
`18_REVIEW/V04/V04_REVIEW_R1.md` lists all nine actions including the owner's D-025 entry.

### Decision

**REVISE**, confidence HIGH. **V05 gate OPEN** under `D-024`. V04 is `IN REMEDIATION` and
does not reach `COMPLETE` until the seven minors and N1 are applied **and re-reviewed**.

### Git

Explicit paths on every `git add` and a pathspec on every `git commit`; `git status` and
`git diff --staged` read before each. A **concurrent session's V03 R3 work was staged in this
shared working tree** throughout the review — `18_REVIEW/V03/V03_REVIEW_R3.md` plus staged
edits to `COURSE_PROGRESS.md`, `REVIEW_INDEX.md` and `LOG.md`. It was left untouched and
unstaged, and the first commit used a pathspec restricted to `V04_REVIEW_R1.md` alone so
none of it was swept in; that session committed and pushed independently as `cda36c1` before
this session's bookkeeping began. The untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13) was left untouched, as at every
prior round. `validate_project.py`: 97 passed, 0 warnings, 0 failures.

### Next Review Trigger

Student remediation of V04's seven minors and N1, then a fresh round (R2). Independently,
V05 may begin at any time — the gate is open.

---

## 2026-08-11 — V04 R1 REMEDIATION (7 minors + N1) and DECISIONS.md D-025

### Objective

Address the required corrections from `18_REVIEW/V04/V04_REVIEW_R1.md` — seven `MINOR`
findings and note `N1` — and record the owner action, the `C-005` scope ruling, as
`DECISIONS.md` **D-025**.

Scope was held to exactly that (`REMEDIATION_PROTOCOL.md` §3.2, `REVIEW_PROTOCOL.md` §10).
Nothing already verified at R1 was re-derived.

### Findings Addressed

- **[E19 / MINOR] M1 — USDCHF's 15-minute series mis-sliced at the week open → EVIDENCE
  FIX, redone not reworded.** Diagnosed from the committed data: on this feed USDCHF's
  first 4-hour bar of the week is a **partial bar of twelve** 15-minute bars, not sixteen
  (the pair quotes an hour later than the other majors). The fixed 16-bar slicing therefore
  began four bars early — the committed 480-bar window carried four **previous-week** bars
  at its head, and the weekend gap (a −12.7 pip discontinuity, the only 15m discontinuity
  in the dataset) sat *inside* what the file called "the week". The bar-0 reconstruction
  missed by **28.1 pips on the OPEN**, which validation 4 says can never happen from dwell
  latency; that contradiction is what should have caught it at the time. **The test worked;
  the diagnosis failed.** Re-sliced: `bars_15m_week` 480 → **476 = 12 + 29 × 16** (the
  complete week — nothing was missing from the tail), `offset_in_harvest` 261 → **265**,
  `j_hi_15m` 363 → 359, `j_lo_15m` 4 → 0. Every pair now carries an explicit
  **`bars_15m_in_4h_bar_0`** field (16 / 16 / 16 / **12**). USDCHF 27/30 → **28/30**; the
  4h↔15m reconstruction **474/480 → 476/480**, its four residuals now genuinely ≤ 0.3 pip
  and all in highs or lows. The ±0.4 pip misattribution is replaced by the real diagnosis
  and the partial-first-bar behaviour is stated as a limit of the 15m pipeline V05 would
  inherit.
- **[E01 / MINOR] M2 — two "verification" quote fragments silently smoothed** in the one
  file whose purpose is to establish that the transcript is verbatim → both restored to the
  **adopted transcript's literal wording** (*"money **set up** here"* `[00:50:34]`;
  *"**Gaby** a nice ugly **look in** kindergarten **ma'am** there"* `[01:10:36]`), the
  paragraph now states which side of the comparison it quotes, and the correction is
  disclosed in place rather than made silently.
- **[E20/E11 / MINOR] M3 — two ambiguity cross-references orphaned** by the duplicate-ID
  remap performed in the register before commit and never propagated back → *"the water"*
  `A-037` → **`A-031`**; *"Timing Shadow Box / Brink Spox"* `A-038` → **`A-030`**.
- **[E20 / MINOR] M4 — stale count and stale filename** → `V04_SOURCE_NOTES.md` *"26
  frames"* → **27**; mastery report *"VISUAL_INDEX"* → **`INDEX.md`**, *"2 scripts"* → 3.
- **[E20 / MINOR] M5 — validation 1 not reproducible from committed data** → restated over
  the committed 30-bar week (**116/116 continuous**, recomputed mechanically) and the
  harvest-wide **569 / 549 / 20** figures explicitly marked **UNREPRODUCED**. The arrays
  were **not** fabricated back into the repo: they were never written to disk, and
  re-harvesting today would produce a *different* dataset from the one every figure in the
  file was computed on. Disclosure is the honest option and is what was done.
- **[E20 / MINOR] M6 — visible TDI panel unrecorded** → frames 21 (`01-04-10`) and 22
  (`01-08-40`) now record the **`Traders Dynamic Index Visual`** sub-panel in `INDEX.md`,
  with a new §"What the visuals added" item 7, and in `A-039`'s evidence table — both
  scoped **"displayed, not taught"** and both stating explicitly that this does **not**
  narrow `A-039`, because the frames are `GUEST` material and therefore descriptive only
  under D-025. The six-value numeric readout beside each panel title **is not legible at
  this resolution and was deliberately not transcribed** (the frames were opened and
  magnified before the descriptions were written).
- **[E20 / MINOR] M7 — four quality-control boxes unchecked and undeclared** → new
  **QUALITY-CONTROL CHECKLIST** section in the mastery report: 13 checked, 2 `DEFERRED`
  (manual chart testing, failed valid setups — both blocked by `A-039`), **4 UNCHECKED and
  stated** (concept library, positive / negative / borderline examples). The concept-library
  box is explicitly **not** excused by `A-039` — that work could have been done and was not.
  The project-wide instance goes to `CUMULATIVE_25.md`, per R1.
- **[NOTE N1] Dimensions B and C mislabelled** → **B `PARTIAL` → `DEFERRED`**, **C `FAIL` →
  `DEFERRED`**, both *"blocked by `A-039`"* under `D-019`, with the original text retained
  **verbatim** beneath the new label. `NOT APPLICABLE` declined — there is plainly subject
  matter. As labelled before, V04 could never have reached `PASS`, because the cause sits in
  the source.

### Decision Recorded — D-025

`DECISIONS.md` **D-025 — Guest-presenter material is secondary DESCRIPTIVE evidence and is
excluded as NORMATIVE doctrine.** Refines D-008 (which ranks the course against the agent
but does not distinguish speakers, because no lesson before V04 had more than one voice).
Normative content — entry criteria, gates, filters, stops, targets, sessions, thresholds,
watchlists, schedules — is **excluded**: it may not enter `12_MASTER_SPEC/`,
`13_MACHINE_SPEC/`, `08_CONCEPT_LIBRARY/` or any machine candidate, may not be cited for
**or against** an instructor rule, and may never be merged with instructor statements.
Descriptive content — that a term exists, how it is spelled, that an object is displayed,
what a printed artifact says — is **admissible below any instructor statement**, may
**EXTEND** an `A-xxx`/`C-xxx` record and may **NEVER RESOLVE or CLOSE** one. Speaker tagging
is **mandatory** for any multi-voice lesson from V04 forward. **Retroactive effect on V04:
none — it ratifies the existing work.** Prospective effect on V05–V21 is the tagging
obligation, which bites immediately: V05 shares V04's session date and "Carl" is queued.

Cross-referenced from `D-008` (forward pointer), `D-004`'s pointer block, the `PROGRESSION
RULE` block in `COURSE_PROGRESS.md` and `REVIEW_PROTOCOL.md` §2 — an open gate is permission
to begin, not permission to skip speaker tagging. `C-005` updated: the scope ruling is made,
the record stays open as corpus hygiene, and its "Required to resolve" field is discharged.

### Work Redone (not edited)

Only `M1`. The USDCHF slice was re-derived from the committed 15-minute array rather than
the paragraph describing it being reworded, and a new committed script,
`05_HOMEWORK/V04/scripts/verify_reconstruction.py`, recomputes validation 3 end to end —
the per-pair partial-first-bar length, the absence of any in-week discontinuity, and the
116/120 bars / **476/480** fields total — exiting non-zero on mismatch. Every other item is
a documentation fix under `REMEDIATION_PROTOCOL.md` §3.3.

### Verification — no conclusion changed

Checked rather than assumed, because `M1` touched data:

- The **4-hour** series was never affected — continuous **116/116** — and every figure in
  homework §2 and §3 is computed from it: block sizes and percentages, weekly extremes and
  their bars, and the **3.83-day** duration on both formed anchors.
- The **scoped 2-of-4 result stands**. USDCHF is excluded because its week low sits on 4h
  **bar 0**, the week-open bar, where no anchor can have formed — a 4-hour fact the re-slice
  does not touch. USDJPY is excluded on the same basis. EURUSD and GBPUSD remain the only
  admissible pairs, both at 3.83 days.
- The **§3.3 swing-descriptor tables are unchanged**, recomputed to confirm: USDCHF's
  extreme index and its 44-bar window shifted by exactly four bars together, so the bars
  examined are the same bars.
- **`M6` does not weaken `A-039`**, and D-025 is the reason: guest frames are descriptive
  evidence that may extend the record and may never close it. TDI is displayed; it is still
  never taught.

### Git

Explicit paths on every `git add` and `git commit`; `git status` and `git diff --staged`
read before committing. **A concurrent V05 student session is active in this shared working
tree** — `02_TRANSCRIPTS/V05/` appeared untracked during this session and was left
untouched and unstaged. The untracked `05_HOMEWORK/V02/measure_usdchf_week.py` (open item
13) was left untouched, as at every prior round. `validate_project.py`: **97 passed, 1
warning, 0 failures** — the warning is "V05 has no transcript", which is the concurrent
session's work in progress and is expected.

### Next Review Trigger

**A fresh reviewer session for V04 R2** (`D-003`). V04 stays `IN REMEDIATION` and reaches
`COMPLETE` only on a reviewer `PASS` (`D-004`). V05 is unaffected — the gate has been open
since R1 — but a V05 session must now apply **D-025** before writing notes.

---

## 2026-08-11 — Reviewer Session — V04 R2: PASS, V04 COMPLETE

**Session type:** Independent Reviewer (`D-003` satisfied — this session authored no V04
artifact and applied none of the R1 corrections).
**Scope:** verification of commit `3a13441`, the V04 R1 remediation (`REVIEW_PROTOCOL.md`
§4). Dimensions R1 graded on untouched material were not re-audited.
**Output:** `18_REVIEW/V04/V04_REVIEW_R2.md`.

**Verdict: `PASS`, confidence HIGH — 0 CRITICAL, 0 MAJOR, 1 MINOR (non-blocking), 3 NOTE.
V04 is `COMPLETE` (`D-004`). All nine items — M1–M7, N1 and the owner action — verify.**

### How the fixes were checked

Every item was re-derived from the committed data or the source file. The diffs were read
only afterwards, to confirm the fix matched what the recomputation already said.

- **`M1`, in both directions.** The **parent commit's** JSON was recomputed to confirm the
  defect was real: exactly one 15m discontinuity in USDCHF's committed "week"
  (`m[3]→m[4]`, **−12.7 pips**), zero in the other three pairs, a bar-0 reconstruction
  missing the **open by 28.1 pips** and the high by 12.8, and `aggregate(m[4:16])` equal to
  4h bar 0 on **all four fields**. The **current** JSON was then recomputed with an
  independently written aggregator: **476/480 fields, 116/120 bars, zero in-week 15m
  discontinuities in all four pairs**, all four residuals ≤ 0.3 pip and all in highs or
  lows. Field-by-field diff of the two JSONs: only USDCHF changed, the new array is
  **exactly `old[4:]`**, the three index fields each shifted by 4, and the 4h arrays are
  untouched. `verify_reconstruction.py` was run as shipped — exits 0 — and read line by
  line to confirm its checks are not tautological.
- **An independent cross-check the remediation did not claim.** Each pair's re-indexed
  `j_hi_15m` / `j_lo_15m` was mapped through the new partial-first-bar arithmetic onto the
  4h grid: all four land in the 4h bar holding the same extreme, at an identical price.
  This closes under the new indices and does **not** under the old ones — the re-index is
  right, not merely consistent.
- **The conclusion was re-checked on the 4-hour data**: 116/116 continuous; USDCHF's and
  USDJPY's week lows on bar 0; EURUSD and GBPUSD week high/low at bars 27/4 and 28/5 →
  23 bars × 4 h = **3.833 days** each. The scoped 2-of-4 result stands.
- **`M2`** against the transcript **body** (lines 3047, 4138, 4142 — exact). **`M3`**
  against the register (`A-031` = blood in the water; `A-030` = brinks shadow; `A-037` /
  `A-038` confirmed to be the wrong subjects). **`M4`** by counting (27 PNGs, 3 scripts).
  **`M7`** against `MASTERY_STANDARD.md` (19 boxes = 13 + 2 `DEFERRED` + 4 UNCHECKED, and
  the declarations are true of the repository). **`N1`** against `D-019`'s own V01 F/G
  worked example, with the retained `PARTIAL`/`FAIL` prose diffed rather than eyeballed.
  **`D-025`** against R1's ruling text, with all four cross-references opened.
- **`M6` by opening the frames.** Both were magnified before the new text was read. The
  `Traders Dynamic Index Visual` panel, its coloured lines and its bands are there as
  described; the six-value readout is **genuinely at the edge of legibility**, and
  declining to transcribe it was the right call.

### Two judgement calls the review was asked to make, and how they went

- **`M5` — honest caveat vs. committing data. UPHELD.** The arrays were never written to
  disk; re-harvesting today would produce a different dataset, and committing it would
  attach data to claims never computed on it. That is provenance fabrication and is worse
  than a declared gap. The figures are marked `UNREPRODUCED`, not withdrawn, nothing
  downstream depends on them, and the reproducible half recomputes exactly (116/116).
- **`M6` framing — accurate and appropriately conservative.** "Displayed, not taught" holds
  on the merits: no inputs, periods, band construction or decision rule is recoverable.
  Beyond what R1 asked, `A-039`'s *"the example chart carries no TDI panel"* line is now
  correctly scoped to the instructor's Segment-A chart, which it always meant.

### The one residual finding — `m1` (`E20`), non-blocking, open item 34

The sentence *"the extreme's index and the 44-bar window shifted together by exactly four
bars, so the bars examined are the same bars"* — in `V04_HOMEWORK.md` §1.2 and in
`V04_MASTERY_REPORT.md` — is **true for USDCHF's high-side window** (bar-for-bar identical)
and **false for the low-side one**: `j_lo` 4 → 0 was clipped at the head of the array in
both datasets, so it went from 5 bars (four of them previous-week bars) to 1 and could not
"shift". **The descriptor row it justifies is genuinely unchanged — 1/1/1/1 across all four
tolerances on both datasets, recomputed at R2** — so the direction is safe and nothing
downstream reads the justification. It is charged because it is one more instance of R1's
own `N5` pattern, produced in the commit that quoted `N5` approvingly: the paragraph
describing the check is the one part nothing recomputes. Fix it when either file is next
edited; **do not open an R3** (`REVIEW_PROTOCOL.md` §9 criterion 14, §16; `V02_REVIEW_R3.md`
precedent).

### Not charged against V04

`08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`'s STATUS block is stale (`LESSONS STUDIED: 3 … V03
studied, not yet reviewed`). It predates this remediation, V04 correctly declared the
concept-library box UNCHECKED rather than touching the file, and it belongs with open item
14 and the concept-library debt at `CUMULATIVE_25.md`.

### Git

Explicit paths on every `git add` and `git commit`; `git status` and `git diff --staged`
read before committing. **A concurrent V05 student session is active in this shared working
tree** — no V05 file was touched or staged, and the untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13) was left alone, as at every prior
round. `validate_project.py`: **97 passed, 0 warnings, 0 failures** (the R1 remediation
reported 1 warning for the then-absent V05 transcript; the V05 session has since committed
it). **Local commit only — pushes are batched until morning at the owner's request.**

### Next Review Trigger

**None for V04 — it is `COMPLETE`.** The next reviewer session is for **V05**, whose gate
has been open since V04 R1 and now rests on a `PASS`. A V05 session must apply **`D-025`**
before writing notes: establish how many voices the recording carries, mark the boundaries,
and speaker-tag every source-note row. `REVIEW_INDEX.md` open item 33 discharges the
`RULES.md` fabrication audit in one step; `NOTES.md` and `VISUAL_INDEX.md` are not covered.

---

## 2026-08-11 — Student Session — V05 student pass (clean retry after a hung attempt)

**Lesson:** V05, `Bootcamp1 Wk2 032512 Part3 (68mins).swf`, SHA-256 `c606520d…f896fcc1`,
01:08:21. **Status on close: student pass COMPLETE, submitted as `REVIEW REQUIRED`.**

### Starting state

A prior V05 attempt hung. On entry the transcript was already adopted and `Q-005` recorded
(commit `a37f31d`); `04_SCREENSHOTS/V05/` and `05_HOMEWORK/V05/` were empty. Read
`SWF_CAPTURE_RECIPE.md`, `DECISIONS.md` through `D-025`, `REVIEW_INDEX.md`, `Q-005`.

### The finding that governed the whole session

**V05 has no instructor segment at all** — a single unnamed presenter, not Steve Mauro and
not V04's guest, speaks the whole 01:08:20. Under `D-025` the lesson is 100% secondary
descriptive evidence, so **it yields no doctrine whatsoever**. This is the first lesson
decided entirely by that decision, and establishing it *before* writing notes is what
`D-025` consequence 3 exists to force.

### Capture

`D-022` / GOTCHA 4 mattered again: **four** stale `http.server` processes from earlier
sessions were holding **8899, 8917, 8931 and 8945**. Took a fresh port (**8953**), confirmed
the listener was this session's own PID, and byte-verified the served SWF against disk before
capturing. Additionally proved the working copy was the right film at the byte level:
decompressed both bodies and diffed — **equal length 44,111,472, exactly one differing byte
at offset 18** (frameRate `UI16` 3.0 → 30.0), `frameCount` 12,304 in both.

Content sanity-checked against the transcript **before** the long sweep, as the recipe
requires: the probe frame at burned `05:00` prints MT4 toolbar/Meta-Editor instruction,
matching `[00:04:57]`–`[00:05:05]` — and simultaneously corroborating `Q-005`, since the
fabricated `RULES.md` claims a "5/13 EMA cross" rule at that marker.

829-frame sweep at 10×, 414 s wall, **zero drift** (elapsed matched `i × 0.5 s` at every
checkpoint). 80 distinct screen states detected with the control bar excluded from the diff
crop, so the ticking timecode could not register as content change. 30 frames curated; a
second 2× pass re-rendered 5 frames whose fine print is quoted.

### Reconciliation with concurrent work

A concurrent process produced an overlapping screenshot set and `INDEX.md` in the same
working tree. Reconciled by content hash rather than by assumption: only 6 of my 26 copies
were byte-identical, the other 20 were the same slides one second apart. **Kept the existing
indexed set** (its filenames carry each frame's own burned-in OSD timecode, which is better
practice than my computed index), removed my duplicates by explicit path, and contributed the
two frames it lacked plus the `hires/` set. Verified its strongest claim independently before
adopting it — the one-differing-byte proof above is that verification.

### Corrections issued this session

- **`EMA` occurs twice in V05, not three times.** `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES
  and `QUARANTINE_REGISTER.md` `Q-005` both say three; the third listed item, *"closing below
  the 200"* `[01:06:02]`, does not contain the token. Re-measured word-boundary,
  case-sensitively, over the verbatim body only (body lines 1271, 3944). **Recorded in
  `V05_SOURCE_NOTES.md` §7 rather than silently patched in two committed files.** No
  conclusion in either changes.
- Two citation defects in my own draft, found and fixed **before** commit: `[00:11:48]`
  quoted verbatim with the ASR flagged rather than silently reconstructed; `[00:53:06]` →
  `[00:53:08]`.
- DMR mention count 12 → **9** during reconciliation.
- `A-048` **withdrawn before it was written**: the *"25 to 50 pips above or below the box"*
  attribution matches V04 `[00:15:43]`, which sits inside V04's **instructor** segment, so
  V05 is corroboration and not a new ambiguity. V05 numbering made contiguous.

### Homework — a method change made because of V04's review

V04's harvesters captured OHLC only, so week boundaries were **inferred** from bar cadence;
review R1 `M1` showed that inference failing on USDCHF. Built
`tv_harvest_v05.mjs`, which reads **Date and Time together with the OHLC** from TradingView's
Data Window, making boundaries a lookup.

**It paid for itself on the first run.** USDCHF's week opens at **22:00**, an hour after the
other three, giving **476** bars not 480 — verified directly (the 20:00–23:00 window holds 9
bars for the other pairs and 5 for USDCHF; the last pre-week bar is `2026-07-31T20:45` for
all four). This **independently reproduces V04 R1's corrected 476** from a different week by a
different method, with the cause visible rather than reconstructed. **1,912/1,912 continuity
transitions, zero breaks.** USDCHF's week low sits on its first available bar and is therefore
**boundary-limited**; USDCHF is excluded from every week-low conclusion.

`D-025` is enforced **in the artifacts**: charts mark day separators, week extremes and
body-to-body boxes, and omit levels, the anchor and every entry. Each rendered image says so
in its own footer. H3's MT4 save procedure is **substituted and declared**; H4's flashcards
are performed **in form but not content**.

### Records

`A-042`…`A-049` opened. Six existing records extended, **none narrowed or closed on guest
evidence**. `A-043` is the sole closure — the MT4 text tool, settled by the displayed
Customizing-toolbar dialog (`Text` icon `A` vs `Text label` icon `T`), a **platform artifact,
not methodology** — and its record tells a disagreeing reviewer how to downgrade it.
**No new contradiction**, with reasoning: a lesson with no instructor segment cannot produce
an instructor-vs-instructor conflict. **`C-003` checked against V05 and struck off as
negative** — zero clock times in the lesson, by a reproducible scan with the transcript's own
markers excluded. **Concept library deliberately not updated:** no V05 material is eligible.

### Submitted as `REVIEW REQUIRED`, not `PASS`

One reason: the `D-018`/`D-019` disposition of mastery dimensions **F and G**. V05 does not
*omit* testable rules — it *states* several that are **withheld by decision**, which is a
third case neither entry contemplates. Graded on the purposive reading with the strict reading
flagged. Two items escalated: whether a third disposition is needed for work **excluded by
decision**, and whether the project acknowledges an **out-of-corpus dependency** (`A-042`,
the DMR).

### Git

Explicit paths on every `git add`; `git diff --staged` read before every commit; **no
`git add -A`**. Eight checkpoint commits. The untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13) was left alone, as at every prior
round. `validate_project.py`: **97 passed, 0 warnings, 0 failures**.
**Local commits only — pushes batched until morning at the owner's request.**

### Next

**Stop before the review.** `V05_REVIEW_R1.md` is written by a separate session
(`REVIEW_PROTOCOL.md`); the student cannot audit itself. V06 does not begin until the V05
gate opens under `D-024`.

---

## 2026-08-11 — Reviewer Session

### Lesson

V05 — `Bootcamp1 Wk2 032512 Part3 (68mins).swf`

### Review Objective

Independent mastery audit, round R1. Fresh session; authored no V05 artifact (`D-003`).
Additionally tasked with verifying whether concurrent duplicate sessions had left duplicated
or conflicting content in the repository.

### Repository state verified FIRST, before any artifact was read

`HEAD` = `b4b690b`, **no commits beyond it**. The V05 pipeline is exactly nine commits,
`a34d2f2` → `b4b690b`, in correct protocol order. The `Zen_man` and on-screen-session-date
findings are **inside `8223224`**, part of the main pipeline, not separate additions.
`A-001`…`A-049` and `C-001`…`C-005` contiguous, **zero duplicate headings, zero gaps**. No
doubled V05 blocks in `LOG.md`/`CHANGELOG.md`. `validate_project.py` 97/0/0. One untracked
file, `05_HOMEWORK/V02/measure_usdchf_week.py` — open item 13, correctly left alone and left
alone again by this round. **No duplication or collision damage exists; no cleanup required.**

### Source Evidence Reviewed

`V05_TRANSCRIPT.md` header, coverage block, speaker section, transcription notes and the full
verbatim body scanned programmatically; the 30 curated frames and 5 `hires/` re-renders
**opened and magnified**; `QUARANTINE_REGISTER.md` Q-005 plus all 21 quarantined `RULES.md`
at population scale; `DECISIONS.md` D-001…D-025 (D-018, D-019, D-024, D-025 in full);
`REVIEW_INDEX.md` including open items 1–40.

### Student Artifacts Reviewed

`V05_SOURCE_NOTES.md`, `V05_INTERPRETATION.md`, `04_SCREENSHOTS/V05/INDEX.md`,
`V05_HOMEWORK.md` with its three scripts and two JSON datasets, `V05_MASTERY_REPORT.md`,
the `A-042`…`A-049` records and the `V05 EVIDENCE ADDED TO EXISTING RECORDS` block,
`CONTRADICTIONS.md` § "V05 PASS".

### Findings

**0 CRITICAL, 0 MAJOR, 6 MINOR, 5 NOTE.**

Everything load-bearing reproduced. The transcript's coverage block is the **first in the
project to assert strict monotonicity and be right** (1,353 / 1,353 / 0 / 0, gap 13 s at both
named markers). `Steve` 21, `Zen` 2, `DMR` 9, `TDI` 6 — all exact. `C-003`'s strike-off
re-measured: **zero clock-time tokens**. Quarantine discharged at full population per open
item 33 — both template markers 21/21, exactly two rules 21/21, `NUMERICAL PARAMETERS`
**one hash 21/21** — and Q-005's audio cross-check verified word for word. **356 citations
checked, 354 resolve; 92 marker-cited quote fragments re-matched, 90 exact.**

Screenshot claims checked against the pixels: `Zen_man / System Folder` confirmed; the taskbar
clock reads **`10:31 PM 3/25/2012`**, the first in-recording corroboration of the session date;
frame 26's status bar reads exactly as transcribed; `A-043`'s dialog shows **`A Text`** and
**`T Text label`** precisely as claimed.

Homework: the harvester parses TradingView's **Data Window `innerText`** — **no pixel sampled,
no colour tested**. Every figure recomputed from the committed JSON reproduces exactly —
480/480/480/476 bars, **1,912/1,912 continuity, zero breaks**, the full `by_day` table, and all
eight extremes with prices, timestamps and pip ranges. The USDCHF anomaly that broke V04
silently is now **caught by the tooling**, independently reproducing V04's corrected 476.

The six minors: `M1` one quote cited at two different wrong timestamps, neither a marker;
`M2` a citation off by one marker; `M3` a smoothed quotation dropping "level three";
`M4` three V05 files disagreeing about V05's own evidence order; `M5` a stale pointer in
`A-039`; `M6` an unrecorded oscillator sub-panel in curated frame 26.

**A reviewer error is recorded rather than hidden:** R1 initially scored the six record
extensions as missing, because they live in a consolidated block at the foot of
`AUTOMATION_AMBIGUITIES.md` (V02's precedent) rather than inside each record. The block is
real and the mastery report's claim is accurate; the finding was withdrawn before it was
charged. Third consecutive round in which a reviewer's own first reading failed to survive its
own verification step.

### Rulings Rendered

- **Open item 40 — `A-043`: AFFIRMED**, not downgraded. A record whose subject is a guest's
  own utterance or a platform artifact, **not the method**, may be closed on descriptive guest
  evidence. Owner to record the carve-out as a `D-025` refinement.
- **Open item 36 — the third disposition: UPHELD.** Dimension **G**'s `NOT APPLICABLE` stands
  on the purposive reading but its stated reason must change; **F** stands as graded;
  **B**'s `NOT APPLICABLE` is **not available** (`D-019` grants it for F and G only) and is
  carried as a NOTE-level required action, following V04 R1 `N1`. Reviewer recommends the
  owner adopt **`EXCLUDED BY DECISION`**.
- **Open item 39 — the `EMA` 3 → 2 correction: CONFIRMED.** Fix belongs in
  `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES and `Q-005`.

### Required Corrections

Eight (`V05_REVIEW_R1.md` §8), plus three owner actions. All localised; none requires
reprocessing any artifact.

### Decision

**REVISE**, confidence HIGH. **0 CRITICAL, 0 MAJOR** — the **V06 gate OPENS under D-024**,
with the six minors owed before V05 can reach `COMPLETE`.

### Git

`18_REVIEW/V05/V05_REVIEW_R1.md` (new); `18_REVIEW/REVIEW_INDEX.md`; `LOG.md`.
**Local commit only — pushes are batched until morning at the owner's instruction. NOT
pushed.** Explicit paths on `git add`; `git status` and `git diff --staged` checked before
commit. No V05 student artifact was edited by this session.

### Next Review Trigger

Student remediation of V05's six minors and the dimension-B re-disposition → `V05_REVIEW_R2.md`
by a fresh session.

---

## 2026-08-11 — V05 R1 Remediation Session

### Scope

The **six MINOR findings** of `18_REVIEW/V05/V05_REVIEW_R1.md` (`M1`–`M6`), and nothing else.
`REVIEW_INDEX.md` open items **41–46** move to `APPLIED — PENDING VERIFICATION at R2`.

**Deliberately NOT done, and why** — both were in R1 §8 but outside this session's instruction:

- **§8 item 7 (open item 39)** — the `EMA` 3 → 2 correction in `V05_TRANSCRIPT.md`
  § TRANSCRIPTION NOTES and `Q-005`. Still owed. Open item 39 stays `OPEN`.
- **§8 item 8** — dimension **B**'s re-disposition and dimension **G**'s stated reason.
  **Blocked on an owner ruling**: R1 §5.2 recommends a third disposition
  `EXCLUDED BY DECISION`, which does not exist in `D-019` yet. Applying a label the standard
  does not define would be a student session legislating. Open item 36 stays `OPEN`.

### Corrections Applied

- **`M1` (`E11`) — one quote, two wrong timestamps, neither a marker.**
  `V05_SOURCE_NOTES.md` §3b `[01:07:36]` → **`[00:57:36]`**; `A-043`'s evidence table
  `[01:01:35]` → **`[00:57:35]`–`[00:57:36]`**, split across the two markers it actually
  spans (`[00:57:35]` *"I use the trend line."* / `[00:57:36]` *"I use E and I use the
  box."*). Both re-verified against the transcript body, not against R1's prose.
  **`A-043`'s closure does not move** — it rests on the toolbar dialog.
- **`M2` (`E11`) — off by one marker.** `A-039`'s V05 extension row `[00:36:03]` →
  **`[00:36:05]`**, and the fragment replaced with that marker's literal sentence.
- **`M3` (`E01`) — a smoothed quotation.** The elision was **restored, not annotated**:
  §4b now carries *"So the consolidation and level three second leg of that pattern, that
  three hits to the high."* `[00:13:05]`–`[00:13:12]` and *"That's the third type, I guess
  the third leg begins your level one drop."* `[00:13:13]` as two verbatim quotations with
  no ellipsis. The excised words were a **level number** in the file's own evidence for the
  level↔day relabelling. **No conclusion in §4b changes** — the relabelling rests on
  `[00:12:50]` and `[00:12:57]`–`[00:13:03]`, both untouched.
- **`M4` (`E20`) — the process-order contradiction. Resolved TOWARD the honest disclosure.**
  `V05_INTERPRETATION.md`'s Screenshots row claimed V05 *"restored the recipe's evidence
  order"*; `04_SCREENSHOTS/V05/INDEX.md` disclosed, unprompted, that **the order was not
  preserved**. The interpretation now states the deviation first and in bold, names
  `INDEX.md` § "⚠ PROCESS DEVIATION, DISCLOSED" as the **governing statement**, and carries
  `INDEX.md`'s own consequence (*the audio-only separation is weaker for V05 than for
  V01–V04*). What was genuinely held — source notes §§1–8 from transcript alone, visuals
  confined to §9, one disclosed pre-sweep sanity frame — is stated as a partial, not as
  restoration. **`INDEX.md` was NOT edited.** Superseded text retained
  (`REMEDIATION_PROTOCOL.md` §2).
- **`M5` (`E20`) — stale pointer.** `A-039`'s *Required Research* now records that **V05 was
  checked and did not define TDI** — first *displayed* name (`TDI_MMM`), first slide titled
  to mark the panel up, and still no inputs, periods, bands, line names or decision rule.
  **A name is not a definition.** V06 or any later lesson named as next candidate.
  Superseded text retained. Record stays `OPEN`, `DO NOT CODE`.
- **`M6` (`E20`) — unrecorded sub-panel in curated frame 26.** The frame was **re-opened and
  looked at**, not taken from R1's description. `V05_00-40-04` does render a multi-line
  oscillator sub-panel beneath the price pane, with a header label in the same position as
  frame 21's `TDI_MMM`. Recorded in `INDEX.md` row 26 and in `A-039`'s extension row, scoped
  *"displayed, not taught; header not legible at this resolution"*. **Presence only — the
  header is deliberately NOT transcribed**, the same call frame 27's OHLC row gets and the
  binding V04 `M6` precedent. **It does not narrow `A-039`** (guest material, `D-025`).

### Owner Decisions Outstanding — not resolvable by a student session

- **R1 §5.1 / open item 40** — whether to carve out of `D-025` a numbered exception for
  records whose **subject is a guest's own utterance or a visible platform/UI artifact**
  rather than a taught trading method, making those closable on guest evidence alone.
  R1 affirmed `A-043`'s closure on exactly this reasoning; the class is not yet written down.
- **R1 §5.2 / open item 36** — whether to adopt a third disposition **`EXCLUDED BY
  DECISION`** for dimensions permanently barred by a numbered decision, distinct from
  `D-019`'s `NOT APPLICABLE` (*there was never anything here*) and `DEFERRED` (*this becomes
  possible later*). V05's dimension **B** fits neither.

### Verification

`validate_project.py` re-run. Every corrected timestamp re-derived from
`02_TRANSCRIPTS/V05/V05_TRANSCRIPT.md` in this session. Frame 26 re-opened. `git status` and
`git diff --staged` checked before commit; explicit paths on `git add`.

### Git

**Local commit only — pushes are batched by the owner. NOT pushed.**
The untracked `05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13) left untouched.

### Next

`V05_REVIEW_R2.md` by a fresh session (`D-003`). V05 reaches `COMPLETE` only on a reviewer
`PASS`. R2 must also account for open items 39 and 36, which this session did not close.

---

## 2026-08-11 — Reviewer Session (V05 R2)

### Lesson

V05 — `Bootcamp1 Wk2 032512 Part3 (68mins).swf`

### Review Objective

Remediation verification of `V05_REVIEW_R1.md` against commit `152f4ea`; application of
`REVIEW_INDEX.md` open item 39; and reconciliation of the orphaned parallel round
`V05_REVIEW_R1B.md` into the review lineage per `SETUP_ISSUES.md` I-002.

### Source Evidence Reviewed

`02_TRANSCRIPTS/V05/V05_TRANSCRIPT.md` (markers and verbatim body, re-scanned); curated frame
`V05_00-40-04.png` opened and magnified at 6× LANCZOS and 10× nearest-neighbour;
`11_CONTRADICTIONS/CONTRADICTIONS.md` records `C-003` and `C-004` read in full;
`00_SYSTEM/REVIEW_PROTOCOL.md`, `REMEDIATION_PROTOCOL.md` §2, `SETUP_ISSUES.md` I-002,
`DECISIONS.md` D-003 / D-018 / D-019 / D-024 / D-025.

### Student Artifacts Reviewed

`V05_SOURCE_NOTES.md`, `V05_INTERPRETATION.md`, `V05_MASTERY_REPORT.md`,
`04_SCREENSHOTS/V05/INDEX.md`, `AUTOMATION_AMBIGUITIES.md` (`A-018`, `A-039`, `A-042`,
`A-043`, `A-020`), `QUARANTINE_REGISTER.md` `Q-005`, plus the review files `V05_REVIEW_R1.md`
and `V05_REVIEW_R1B.md` (read and reconciled, **not** audited and **not** edited).

### Findings

**R1's six minors: all six VERIFIED APPLIED and CLOSED.** Each was re-derived from the
transcript or the pixels before the remediation diff was read. `M4` verified in the correct
direction — `git show 152f4ea -- 04_SCREENSHOTS/V05/INDEX.md` touches one line only (row 26,
for `M6`), so the honest disclosure was not weakened to match the interpretation. `M6` verified
in both halves — the sub-panel is present and its header is genuinely illegible at 9×, so the
refusal to transcribe it is correct.

**Open item 39 APPLIED.** `EMA` re-counted word-boundary over the verbatim body: **exactly 2**,
at `[00:23:52]` and `[01:05:53]`; `[01:06:02]` is present and does not contain the token. Both
sites corrected with superseded text retained.

**Five minors OPEN, all adopted from R1B, all independently confirmed at `HEAD`:** `M7`
`C-003`/`C-004` record identity at four sites including a STATUS block; `M8` *"but up to five
days"* counted four times, verbatim twice; `M9` four unrecorded printed `R =` labels in frame
26 leaving `A-018` undercounted; `M10` §4c's *"always with the same escape clause"* false for
two of four rows; `M11` `A-042` citing the non-marker `[01:01:39]` for words at `[00:57:39]`.

**Review-layer reconciliation.** `V05_REVIEW_R1B.md` is a complete, valid, committed parallel
review — later than R1, not earlier; not a mid-write fragment. Its real defect was invisibility:
zero references in `REVIEW_INDEX.md` and zero in `LOG.md`, so the remediation never saw it. It
is folded into the lineage, its body unedited, an append-only status footer added, and it is
**not** marked invalid — all five of its findings reproduce.

### Required Corrections

`M7`–`M11` (`V05_REVIEW_R2.md` §5), open items 47–51. Dimension B's re-disposition remains
**blocked on the owner** (open item 36) and is carried, not charged.

### Owner Items Confirmed Open, Not Resolved

Open item 36 (a third disposition, provisionally `EXCLUDED BY DECISION` — and it should cover
dimension **B**, which the student's own escalation omitted); open item 40 (a numbered `D-025`
carve-out for records whose subject is a guest's own utterance or a platform artifact); open
item 35 (`A-042`'s out-of-corpus DMR dependency); and a new one — whether parallel independent
reviews are intended policy or a tooling accident to be guarded against.

### Decision

**REVISE** — confidence HIGH. 0 CRITICAL, 0 MAJOR, 5 MINOR. **V06 gate remains OPEN** under
D-024. **V05 is NOT COMPLETE.**

### Independence Note

`D-003` is satisfied for every V05 artifact **except** the open-item-39 `EMA` correction, which
this reviewer session applied on explicit owner instruction and therefore self-verified. Scope:
two numerals and two retained-text blocks. Declared at `V05_REVIEW_R2.md` §3.1 rather than
glossed. `validate_project.py`: 97 passed, 0 warnings, 0 failures.

### Git

Local commit only, explicit paths, `git status` and `git diff --staged` checked before commit.
**NOT pushed** — pushes are batched by the owner. The untracked
`05_HOMEWORK/V02/measure_usdchf_week.py` (open item 13) left untouched.

### Next Review Trigger

Student remediation of `M7`–`M11` → `V05_REVIEW_R3.md` by a fresh session.

---

## 2026-08-11 — V05 R2 Remediation Session

**Scope: `V05_REVIEW_R2.md` §5 items 1–5 (`M7`–`M11`) only.** A mechanical fix pass. No
conclusion, grade, disposition or record status moves anywhere in the repository, and this
was verified per file rather than asserted. Superseded text retained at every site that
changed a claim (`REMEDIATION_PROTOCOL.md` §2), and `M11`'s citation fix supersedes nothing
because it replaces a nonexistent marker with the real one.

### `M7` (`E20`) — `C-003` → `C-004` at four sites

The V05 contradiction check that was run, and struck off as negative, is **`C-004`** (*"London
session open: 3:30am printed against 4:00 spoken"*) — its subject is clock times and the
strike-off block sits physically inside the `C-004` material. **`C-003`** is *"Whether M and W
formations can fail"* and **contains no V05 text at all**; it was never tested against V05.
Corrected at `CONTRADICTIONS.md` line 23 (**the STATUS block**), at both sentences in
§ "V05 PASS", and at `V05_MASTERY_REPORT.md` §J. **The check itself does not move** — V05
contains zero clock times, and `C-004` stays `UNRESOLVED`: carry both values, encode no London
open. **`V05_REVIEW_R1.md` was NOT edited**, per `REVIEW_PROTOCOL.md` §11 — its dimension O
carries the same error and R2 records that where a superseded reviewer statement belongs.

### `M8` (`E01`) — a count re-measured over the string it quotes

Re-measured before the edit, not taken from the review: *"but up to five days"* occurs
**exactly 2×** — body line 617 `[00:11:11]` and body line 1511 `[00:24:37]`. *"five days"*
occurs 4×; the other two are *"sometimes five days depending"* and *"Remember three to five
days"*, neither of which contains the quoted words. `V05_MASTERY_REPORT.md` §E now reads
*"twice verbatim, `[00:11:11]` and `[00:24:37]`; the day-count expectation itself is stated
four times."* The exception is still recorded and §E's grade does not move.

### `M9` (`E20`) — frame 26's four printed `R = ` labels, read at magnification

Frame 26 (`V05_00-40-04`) was **re-opened and magnified by this session** at 16×
nearest-neighbour and 16× LANCZOS rather than accepted from either review's prose. Four `R = `
labels are printed on the live MT4 chart:

| Position | Reading |
|---|---|
| upper-centre | `R = 40.9` — legible |
| centre-right | `R = 40.6` — legible |
| lower-right | `R = 41.1` — legible |
| left | `R = ` legible, **value NOT legible** — the cyan moving average runs directly through the digits; only a trailing glyph separates from it at any magnification tried |

**R2's correction of R1B is upheld independently: `R = 74.6` is not supportable from this PNG
and no number is transcribed for the fourth label.** That is the frame-27 OHLC / V04 `M6`
precedent, and it is the same call the frame-26 sub-panel header already gets. Recorded in
`04_SCREENSHOTS/V05/INDEX.md` row 26 and in `A-018`'s V05 row, scoped *printed, not spoken;
live platform; three values legible, one not legible at this resolution*, and `A-018`'s
*"V05 adds four more labels"* corrected to **"at least eight"** — the four platform-printed
labels are the stronger evidentiary class because they are **auto-generated MT4 annotations**
rather than hand-drawn deck labels, which is exactly the proposition `A-018` accumulates.
**`A-018` is extended, NOT narrowed** — guest material under `D-025`, and V05 states no stop
and no target, so nothing in this lesson checks an R-multiple reading. Stays `DO NOT CODE`.

### `M10` (`E02`) — the framing sentence that generated `M8`

`V05_SOURCE_NOTES.md` §4c headed its four-row table *"Repeated four times, **always with the
same escape clause**"*. Checked row by row against the transcript including adjacent markers:
**two of the four carry it, two do not** — `[00:15:47]` is followed by `[00:15:52]` *"I'm
letting my money out."* / `[00:15:55]` *"So those are the things you're watching for."*, and
`[00:16:35]` by `[00:16:36]` *"Expect a reversal."* / `[00:16:39]` *"You know how to draw the
trend lines."* The framing sentence is restated as *"two of the four carry the explicit
`up to five days` escape clause"* and the table gains an **Escape clause** column recording
✅ / ❌ per row with the negatives' neighbourhoods quoted. The four rows were and remain
individually accurate; no conclusion in §4c changes. **This is where `M8` started**, and the
superseded block says so.

### `M11` (`E11`) — the third member of the displaced citation cluster

`A-042`'s evidence table cited `[01:01:39]`, which **is not a marker in this transcript**
(`grep -c` returns 0); the words are at **`[00:57:39]`**, body line 3739. Corrected, and the
fragment replaced with that marker's literal sentence — *"And obviously for the DMR, I kind of
use the ellipse to show the moving average crossover"*. All three of V05's citation defects
map `00:57:3x` → `01:0x:3x`; `152f4ea` closed two of them as `M1`, and this closes the third.

**The mechanical marker-existence sweep R2 required was run, and it is CLEAN.** Every
`[hh:mm:ss]` citation on a V05-attributed line across `AUTOMATION_AMBIGUITIES.md`,
`CONTRADICTIONS.md`, `V05_SOURCE_NOTES.md`, `V05_INTERPRETATION.md`,
`V05_MASTERY_REPORT.md`, `04_SCREENSHOTS/V05/INDEX.md` and `05_HOMEWORK/V05/` was matched
against the **1,353** markers in `V05_TRANSCRIPT.md`. **No fourth cluster member exists.** The
only seven non-resolving hits are six explicit V01/V02/V04 cross-citations (e.g. *"V04
`[00:15:05]`"*) and one slide timecode — `CONTRADICTIONS.md` line 850's *"(slide,
`[00:15:49]`)"*, which is frame 11's own burned-in time, not a transcript marker. None is a
V05 marker citation, and none is touched here.

### What was NOT done, and why

`V05_REVIEW_R2.md` §5 item 6 — **dimension B's re-disposition and dimension G's stated
reason** — remains **blocked on the owner** (open item 36). `D-019` grants `NOT APPLICABLE`
for dimensions F and G only, so B's present label is unavailable, but the replacement label
`EXCLUDED BY DECISION` does not exist yet and a student session applying an undefined label
would be legislating. R2 §N3 upheld that refusal explicitly; it is upheld again here. The four
owner actions (open items 35, 36, 40, and the parallel-session ruling) are likewise untouched.
No review file was edited: `V05_REVIEW_R1.md`, `V05_REVIEW_R1B.md` and `V05_REVIEW_R2.md` all
stand as written.

### Verification

`validate_project.py`: **97 passed, 0 warnings, 0 failures.** Register integrity re-checked —
`A-001`…`A-049` and `C-001`…`C-005` contiguous, no duplicates, no gaps.
`REVIEW_INDEX.md` open items 47–51 → **APPLIED — PENDING VERIFICATION at R3**; taxonomy rows
`E01`/`E02`/`E11`/`E20` updated to match; the STATUS block records the sweep result.

### Git

Local commit only, explicit paths on `git add`, `git status` and `git diff --staged` checked
before commit. **NOT pushed.** The untracked `05_HOMEWORK/V02/measure_usdchf_week.py` (open
item 13) left untouched.

### Next Review Trigger

`V05_REVIEW_R3.md` by a fresh session. R2 expects R3 to close V05.

---

> **MERGE NOTE 2026-08-12.** The entries below were committed on a parallel line of work that
> branched from `3a13441` (the backtest-evidence-standard / `D-026`…`D-031` lineage) and were
> pushed before this branch's V05 entries. Both lines are dated 2026-08-11, so this journal is
> not strictly chronological across the merge point. Nothing was edited or reordered within
> either block. See the numbering collisions flagged in `18_REVIEW/REVIEW_INDEX.md` and
> `CHANGELOG.md`.

---

## 2026-08-11 — Session — Backtest Evidence Standard (D-026 / D-027)

### Objective

Close two methodological gaps identified by an external review of this repository,
before the first manual-backtest observation is written.

### The four questions asked, and the honest answers at the time

| # | Question | Answer |
|---|---|---|
| 1 | Exhaustive, or search-for-matches? | **Exhaustive by design, never exercised.** `STUDY_PROTOCOL.md` §2 + reviewer checks 3 and 6. |
| 2 | Losers/ambiguous filtered? | **Retained**, enforced at three layers (template checklist voids the observation, `INSUFFICIENT INFORMATION` is first-class, reviewer checks 7-9). |
| 3 | Train/test split? | **NO.** Only Phase-8 language existed, and its boundaries were an unmade decision. |
| 4 | Baseline? | **NONE.** Repository-wide grep for baseline / coin-flip / random entry / null hypothesis / control returned one hit, unrelated. |

(1) and (2) needed no change. (3) and (4) are closed by this session.

### Work Completed

- **`00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`** (new) — matched random-entry baseline
  (>=200 iterations, distribution reported); period pre-registration; holdout reserve;
  n>=30 for any quoted rate; intervals mandatory; `DESCRIPTIVE` / `EVIDENTIAL` /
  `INVALID` classification; multiple-comparison discipline.
- **`DECISIONS.md` D-026 / D-027** — baseline mandatory with a hard gate; period
  pre-registration and holdout reserve. Two concrete parameters marked **`OWED NOW`**
  in the open-decisions table (owner action).
- **`REVIEW_PROTOCOL.md`** — §6.G checks **15-20**, error codes **E21-E25**. Missing or
  post-hoc baseline is `CRITICAL`; the rest are `MAJOR`.
- **`MANUAL_BACKTEST_TEMPLATE.md`** — new **§0 PRE-REGISTRATION** block completed before
  any chart in the range is opened, four added integrity-checklist boxes, and **§9b
  RESULT CLASSIFICATION**.
- **`scripts/validate_project.py`** — `check_backtest_evidence_gate()`. Silent while no
  observation exists; once one does, fails on: missing D-026/D-027, unresolved
  `OWED NOW` parameters, missing §0 block, missing classification, or a bare percentage
  with no interval/baseline/insufficiency label.
- Wired into `STUDY_PROTOCOL.md` §2, `MASTERY_STANDARD.md` dimension G,
  `06_MANUAL_BACKTEST/README.md`; `REVIEW_INDEX.md` open items **34-35**;
  `CHANGELOG.md` 0.7.0.

### Key Findings

**The course supplies its own natural control and the project had not noticed.** V04's
central claim is that *location* changes the outcome — the same M formation is a loser
inside the blue box and a winner outside it (`[00:03:04]`-`[00:03:27]`). Running both
arms removes the pattern confound. If they perform alike, the prohibition that forms
V04's spine is not doing the work the course claims. This is now required where the
sample permits, and a null result there is to be reported with equal prominence.

**Adopted at zero cost.** `06_MANUAL_BACKTEST/` held **0** observations, so no existing
work required rework. The V02/V03/V04 homework is `DESCRIPTIVE` and **already labels
itself correctly** — `V04_HOMEWORK.md`: *"One week is one week — this is a single
observation."* No retroactive correction was owed and none was made.

### Verification

The gate was **negative-tested**, not assumed. A deliberately sloppy `BT_V04_0001.md`
(no pre-registration, bare "62%", no classification) was created in a scratch copy:
validation returned **4 failures**, one per defect, then **99/0/0** after removal. A
green run on zero observations proves nothing; this does.

### Manual Backtesting

None performed. This session governs how it will be done, not what it found.

### Ambiguities / Contradictions

No new course-level records. `A-039` still blocks the backtest debt.

### Decisions

**D-026**, **D-027**. Two parameters left `OWED NOW` for the owner — deliberately not
invented by this session.

### Files Created/Updated

`00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md` (new); `DECISIONS.md`; `REVIEW_PROTOCOL.md`;
`STUDY_PROTOCOL.md`; `MASTERY_STANDARD.md`; `TEMPLATES/MANUAL_BACKTEST_TEMPLATE.md`;
`06_MANUAL_BACKTEST/README.md`; `18_REVIEW/REVIEW_INDEX.md`; `scripts/validate_project.py`;
`CHANGELOG.md`; `LOG.md`.

### Git

```text
<this commit> docs: add backtest evidence standard (D-026/D-027) with mechanical gate
```

### Next Action

**Owner:** decide the two `OWED NOW` parameters in `DECISIONS.md` — development/holdout
boundary, and baseline parameters. Until then `validate_project.py` will fail the moment
a `BT_` file appears, which is the intended behaviour.

**Project:** V05 is complete locally but **uncommitted** — commit and push it before any
further work, then the V05 review and the V04 R2 review. The backtest debt discharges
when `A-039` clears, under this standard.

---

## 2026-08-11 — Session — Owner decisions D-028/029/030; PT-001 pre-registered

### Objective

Record the owner's answers to the two decisions owed under D-026/D-027, record the
owner's direction on blocked tests, and pre-register the one test that is available
before the course teaches more.

### Owner input, 2026-08-11

1. **70/30 development/holdout** — approved.
2. **Baseline parameters** — delegated to the agent's judgement.
3. **"We have to wait until those things are taught… so we have to be patient."**
4. **"The blue box boundary is the Asian range. He'll go over it."** Plus: record the
   Asian-range test so it is not forgotten.

### Work Completed

- **D-028** — 70/30 split. Exact dates deliberately **not** pinned: `I-007` is open, no
  data source is declared, so the available range is unknown and any dates written today
  would be invented. The first session to declare a data source computes and appends them.
- **D-029** — baseline parameters, per the delegation: 1,000 iterations for headline
  results (200 floor for exploratory), **random seed recorded every run**, entry window
  matched to the rule, and **two arms** — direction-matched primary (does the setup carry
  information given direction?) and random-direction secondary (is there directional edge
  at all?). Those two questions are routinely conflated; separating them costs nothing.
- **D-030** — the owner's patience point recorded as a binding rule. This is the
  machine-rule firewall (`D-010`) applied to *testing*, which is the more dangerous hole:
  an approximated definition inside a test produces a **number**, and a number acquires
  authority in a research corpus that a note never does.
- **`PT-001`** pre-registered in full.
- `REVIEW_INDEX.md` item 53 closed; 54–55 opened. `CHANGELOG.md` 0.7.2. *(Item numbers and version renumbered 2026-08-12 from 35/36–37 and 0.7.1 — see the resolved merge notes in `REVIEW_INDEX.md` and `CHANGELOG.md`.)*

### Key Findings

**PT-001 is blocked by exactly ONE thing, and it is the cheap one.** The Asian range
needs a window; V02 prints *"Asian Session: 8:30pm - 3:00am"* on a slide **with no
timezone** — `A-019`. Unlike `A-011`, `A-004`, `A-002` or `A-039`, this plausibly closes
from **existing** V01–V05 evidence rather than a future lesson: V04 `[00:07:01]` *"It's
809 Eastern Time on 325"*, V01 `[00:46:09]` *"the US session starts at 930 Eastern"*.
**A focused timezone evidence pass is therefore the highest-leverage work item currently
available** — small, and it unblocks the only runnable test.

`C-004` is the standing caution: London open is printed 3:30am against 4:00 spoken, so
session times in this course are demonstrably messy. **US Eastern must not be assumed to
unblock PT-001** (`D-030`).

**On the owner's statement that the blue box is the Asian range:** V04 supports it —
the instructor uses the two interchangeably (`C1`, `[00:14:36]` *"25 to 50 pips higher
than the Asian range"* against `[00:15:43]` *"25 to 50 pips above and below the blue
box"*). Recorded here as **owner statement corroborated by V04 evidence**, not as a
resolution of `A-006`, whose open question is different: whether the box is a *temporal*
session rectangle or a *positional* price zone. Both readings still survive the frames.

### Manual Backtesting

None. PT-001 is pre-registered and **not run** — it is blocked by `A-019`.

### Ambiguities / Contradictions

No new records. `A-019` is promoted in practical importance: it now gates the only
runnable test.

### Decisions

**D-028**, **D-029**, **D-030**.

### Files Created/Updated

`00_SYSTEM/DECISIONS.md`; `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-001_…md` (new);
`18_REVIEW/REVIEW_INDEX.md`; `CHANGELOG.md`; `LOG.md`.

### Git

```text
<this commit> docs: record D-028/029/030 and pre-register PT-001
```

### Next Action

1. **Commit and push V05** — still uncommitted, still a single copy.
2. **Timezone evidence pass** to close or characterize `A-019` — small, and unblocks
   PT-001.
3. Then V05 review, V04 R2 review.

---

## 2026-08-11 — Session — D-031: timezone as a tested variable; PT-001 unblocked

### Objective

Resolve the `A-019` timezone blocker on `PT-001` following owner direction, without
closing an ambiguity the source itself declines to settle.

### Owner direction

*"Originally I thought it'd be Eastern Standard Time in New York, but we have to test
daylight savings versus non-daylight savings. So just default to Eastern Standard Time
in New York and then test with the extra if need be."*

The instinct is right and is the reason this closed cleanly: an ambiguity that cannot be
resolved from source **can** be converted into a measured variable.

### Work Completed

- **`D-031`** — session timezone is a tested variable. Two pre-registered arms:
  **A** fixed `UTC−5`; **B** DST-aware `America/New_York`. **Binding rule: both are
  always reported.** Divergence is a finding, never a selection criterion.
- **`A-019` updated and deliberately kept OPEN.** `D-031` governs project method, not
  course content, and may never be cited as instruction.
- **`PT-001` unblocked** — §3 rewritten with the two-arm design, the two-draws caution,
  and the straddle-a-DST-transition recommendation. Remaining prerequisites are `I-007`
  (data source) and the `D-028` boundary dates — no longer the timezone.
- `REVIEW_INDEX.md` item 55 updated, item 56 added. `CHANGELOG.md` 0.7.3. *(Item numbers and version renumbered 2026-08-12 from 37/38 and 0.7.2 — see the resolved merge notes.)*

### Key Findings

**The owner's stated default may be inverted, and the arithmetic is now on the record.**
The bootcamp ran 2012-03-18 → 2012-06-17, **entirely inside US daylight saving**
(2012: Mar 11 – Nov 4). So:

```text
V01 [00:46:09] "the US session starts at 9:30 New York Eastern"
  = 09:30 EDT = 13:30 UTC during the recording period

Fixed EST (UTC−5) chart      → displays 08:30   one hour early, every session
America/New_York (DST-aware) → displays 09:30   matches
```

Arm B reproduces the instructor's own numbers during the window he spoke them; Arm A
displaces every one by an hour. **This is evidence about the source and does not settle
what the method requires** — his table may genuinely have been taught as fixed clock
numbers (`A-019` candidate reading 1). Recorded, not acted on unilaterally.

Supporting fragment for the market-anchored reading: `[00:50:26]` *"we back up the London
session in the winter"* — part of his table already moves seasonally, which is what a
DST-following table does and a fixed-offset table does not.

**Two arms are two draws, not two chances to be right.** Flagged explicitly in `PT-001`
§3b: if A returns 58% and B returns 61%, that is one draw each from possibly overlapping
distributions, not a discovery that B is correct. Reporting only the better arm is
`E09`+`E24`.

**Design improvement found while writing this up:** the two arms are *identical* outside
US daylight saving and differ by one hour inside it. Choosing a development window that
**straddles a DST transition** therefore gives a within-sample comparison on the same
instrument and regime — strictly stronger than two separate runs, at zero cost.

### Manual Backtesting

None. `PT-001` remains pre-registered and unrun.

### Ambiguities / Contradictions

`A-019` updated, **still OPEN**. No new records.

### Decisions

**D-031**.

### Files Created/Updated

`00_SYSTEM/DECISIONS.md`; `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`;
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-001_…md`; `18_REVIEW/REVIEW_INDEX.md`;
`CHANGELOG.md`; `LOG.md`.

### Git

```text
<this commit> docs: D-031 timezone as tested variable; PT-001 unblocked
```

### Next Action

1. **Commit and push V05** — still uncommitted, still a single copy.
2. Declare the chart data source and feed (`I-007`), then pin the `D-028` boundary dates
   choosing a window that straddles a DST transition.
3. `PT-001` becomes runnable at that point.
4. V05 review, V04 R2 review.

---

## 2026-08-12 — Reviewer Session (V05 R3)

### Lesson

V05

### Review Objective

Remediation verification of `V05_REVIEW_R2.md` `M7`–`M11` (open items 47–51), applied at
`5bcb720`. Convened by the owner after the branch merge (`9ad57b8`) was pushed.

### Source Evidence Reviewed

`V05_TRANSCRIPT.md` (marker set re-extracted: 1,353; the `M8`/`M10` neighbourhoods and
`[00:57:39]` re-read from the body); frame 26 `V05_00-40-04` re-opened, all four `R = `
labels re-cropped and read at 10× by this session.

### Student Artifacts Reviewed

`CONTRADICTIONS.md` (M7's four sites), `V05_MASTERY_REPORT.md` §E/§J, `V05_SOURCE_NOTES.md`
§4c, `AUTOMATION_AMBIGUITIES.md` `A-042`/`A-018`, `04_SCREENSHOTS/V05/INDEX.md` row 26 —
each re-derived from source **before** `git show 5bcb720` was read. Also verified: the
merge commit touched no V05 artifact (diff `5bcb720..9ad57b8`).

### Findings

All five minors verified applied and correct; superseded text retained at every site that
changed a claim. The `M11` marker-existence sweep was **re-run from scratch**: 7
non-resolving citations, all accounted for (6 cross-lesson, 1 burned-in slide time) —
identical to the remediation's stated result; the displaced cluster is closed at three.
Frame 26's disputed left label read a third time: `R = ` legible, **value not legible**
(cyan MA through the digits) — R2's refusal to transcribe R1B's `74.6` is upheld.
Zero new findings. Three notes (`V05_REVIEW_R3.md` §3).

### Required Corrections

None for the student. Owner actions carried unchanged from R2 §5: open items 35, 36, 40;
R1B naming; parallel-session ruling. Dimension-B/G re-labelling stays blocked on open
item 36 and does not gate (§9 criterion 14).

### Decision

**PASS** — confidence HIGH. 0 critical, 0 major, 0 minor. **V05 is COMPLETE.**
`REVIEW_INDEX.md` STATUS, decision table, lineage note and open items 47–51 updated.

### Git

`V05_REVIEW_R3.md` added; `REVIEW_INDEX.md`, `LOG.md`, `CHANGELOG.md` updated. Committed
and pushed this session (owner instruction: push immediately).

### Next Review Trigger

V06 submission, or `CUMULATIVE_25.md` if that milestone arrives first.

---

## 2026-08-12 — Session — Bookkeeping: open item 13 discharged by `1fa087f`

### Objective

Close the record on `05_HOMEWORK/V02/measure_usdchf_week.py`, which the project owner
committed directly in `1fa087f` after this journal had recorded, sixteen separate times,
that the file was being left untracked and untouched on purpose. Documentation
only — no study work, no review work, no new content.

### Work Completed

- **`REVIEW_INDEX.md` open item 13 → `CLOSED`**, citing `1fa087f`. The row's body is
  unchanged; only its status cell moves. The closure is stated as covering the **tracking
  half** of the item only — the file is now under version control, so §1.1's promise of a
  reproducible method is discharged by a committed script rather than by a working-tree
  artifact, and the standing *"leave it in place, do not delete"* instruction is spent.
- **Item 12 deliberately untouched.** The substantive half of item 13's charge —
  committed §1.1's *"settled"* against the script's *"uncertain by one bar"* — is item
  12's business and is neither adjudicated nor re-opened here.
- **This entry.** Every prior session that met this file logged what it did with it
  (LOG.md 1578, 1670, 1764, 1836, 1908, 2000, 2134, 2228, 2356, 2486, 2585, 2708, 2739,
  2905, 2995, 3108 — all variations on *"left in place, uncommitted, undeleted"*). The
  commit that finally resolved it logged nothing. That gap is what this entry fills.

### Key Findings

**The file the journal kept describing was never anyone's to commit until the owner
committed it.** Sixteen entries across two days recorded the same non-action, correctly:
`D-003` independence and the R2 Note 8 instruction both told each session to leave another
session's artifact alone. The instruction had no terminating condition that a session could
satisfy by itself — which is precisely why it kept being restated instead of resolved.
`1fa087f` supplies the condition from outside the review loop.

`1fa087f` is 166 lines, matching the size V02 R2 (`V02_REVIEW_R2.md` line 90) and V02 R3
(line 53) both recorded for the untracked copy, so nothing changed in the file between the
review that noticed it and the commit that captured it.

### Manual Backtesting

None. No change to `06_MANUAL_BACKTEST/`; `PT-001` remains pre-registered and unrun.

### Ambiguities / Contradictions

None created, none closed. No `A-xxx` or `C-xxx` record touched.

### Decisions

None. No `DECISIONS.md` entry — committing a file the review record already instructed be
kept is not a project-level decision.

### Files Created/Updated

`18_REVIEW/REVIEW_INDEX.md` (item 13 status cell); `LOG.md` (this entry). **No
`CHANGELOG.md` entry** — that file records architecture, protocols, standards and phase
transitions, and this is bookkeeping on a single open item. The precedent is
`scripts/verify_reconstruction.py`, a committed script from the V04 R1 remediation that
likewise carries no changelog entry.

### Verification

`scripts/validate_project.py`: **98 passed, 1 warning, 0 failures.** The single warning is
`non-media files in 01_SOURCE_VIDEOS/ … .DS_Store` — a Finder artifact created outside this
session, already covered by `.gitignore` line 74, therefore never a candidate for commit.
Left in place rather than deleted: it is not project content and removing files the task
did not touch is not this session's business.

### Git

Explicit paths on `git add` (two files, never `-A`); `git status` and `git diff --staged`
read before committing. Committed and pushed this session, per the standing owner
instruction to push immediately.

### Next Action

Unchanged and owner-blocked. V06 ingestion is **paused by owner instruction** — nothing in
this session starts it. Open items 35, 36, 40 and the parallel-session ruling still await
the owner; `I-007` (data source) and the `D-028` boundary dates still gate `PT-001`.

---

## 2026-08-12 — Session — `validate_project.py`: the `.DS_Store` warning, fixed at the check

### Objective

Take the repository back to **0 warnings**. Continuation of the entry immediately above,
which recorded `98 passed, 1 warning, 0 failures` and left the warning in place. The owner
asked for it fixed; this entry records the fix and supersedes that entry's disposition
(the entry itself is left as written, per this journal's append-only rule).

### Work Completed

- **`scripts/validate_project.py`, `check_source_videos_dir()`** — `.DS_Store` added to the
  allowlist beside `README.md` and `.gitkeep`, with a comment stating why.
- **`01_SOURCE_VIDEOS/.DS_Store` deleted.** Verified as `Apple Desktop Services Store`
  before removal; gitignored at `.gitignore:74`, so it was never tracked and nothing left
  the repository's history.

### Key Findings

**Deleting the file is not a fix; it is a fix with a timer on it.** Finder rewrites
`.DS_Store` the next time anyone opens `01_SOURCE_VIDEOS/`, and this project's source
directory is opened by hand every ingestion. A check that goes yellow on a file the
operating system recreates teaches the reader to skim past the warning line — which is the
failure mode that produced the `E20` status-block class six times over. So the fix belongs
in the check, and the deletion is only housekeeping alongside it.

**The check's scope is unchanged and still bites.** It exists to catch *generated study
artifacts* — transcripts, JSON, screenshots — written into the source-media directory.
`.DS_Store` is OS metadata, not a study artifact and not a candidate for commit; it is the
one class of file that can be excluded without weakening what the check was written to
find. Any real stray still warns.

### Manual Backtesting

None.

### Ambiguities / Contradictions

None.

### Decisions

None. A one-name allowlist entry in a structural linter is not a project-level decision and
gets no `DECISIONS.md` or `CHANGELOG.md` entry.

### Files Created/Updated

`scripts/validate_project.py` (four comment lines and one set literal); `LOG.md` (this
entry). `01_SOURCE_VIDEOS/.DS_Store` deleted (untracked).

### Verification

`scripts/validate_project.py`: **99 passed, 0 warnings, 0 failures.** The count rises by one
because the check now reports its `PASS` branch — `01_SOURCE_VIDEOS/ holds no generated
artifacts` — instead of its warning branch.

### Git

Explicit paths on `git add`; `git status` and `git diff --staged` read before committing.
Committed and pushed this session.

### Next Action

Unchanged. V06 ingestion stays paused by owner instruction.

---

## 2026-08-12 — Session — Batch quarantine pre-verification, `RULES.md` V07–V21

### Objective

Owner-requested proactive batch pass, ahead of any per-video ingestion: check every
remaining lesson's `RULES.md` (`V07` through `V21`, the last video in the corpus) against
the fabrication signature independently confirmed for `V01`–`V06` (`Q-001`…`Q-006`), and
flag/quarantine any that match — so future per-video Student sessions don't re-derive this
check from scratch. Scoped to `RULES.md` only. `NOTES.md`, `INDEX.md`, and
`VISUAL_INDEX.md` were explicitly out of scope and not touched, per owner instruction —
those remain pairwise distinct across the library and still need per-lesson examination
when each video's real ingestion runs.

### Work Completed

- **Located** all 21 `RULES.md` files. All 21 already physically sit under
  `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/NN_.../RULES.md` (moved there at `D-017`/`Q-001`,
  before this session), already covered by the tree-wide `README_WHY_QUARANTINED.md` header.
  Nothing needed to be moved.
- **Verified, did not assume.** Re-ran the three-marker mechanical test `REVIEW_INDEX.md`
  open item 33 authorizes for a one-step discharge, across `V07`–`V21`: both fabricated quotes
  (`[00:05:00]` M15/5-13-EMA line; `[00:18:00]` 10–15-pip stop line) present in all 15;
  exactly two `## Rule ID:` entries in all 15; the `NUMERICAL PARAMETERS` block hashed
  identical across all 15 — and, as a cross-check, re-hashing `V01`–`V06` the same way
  returned the same hash, confirming it is the one block already established at `Q-004`, not
  a coincidentally-matching new one. **Zero exceptions** — no `RULES.md` in the corpus
  differs from the confirmed pattern.
- **`00_SYSTEM/QUARANTINE_REGISTER.md`** — added `Q-007`, covering `V07`–`V21` `RULES.md` as
  a single batch entry (they are mechanically identical, so 15 near-duplicate per-video
  entries would misrepresent 15 separate audits as having been run; `Q-007` states plainly
  that this is the template-marker discharge, not a fresh audio cross-check, and that
  `NOTES.md`/`VISUAL_INDEX.md` remain unaudited for these 15).

### Key Findings

**All 21 lessons' `RULES.md` now carry either an individual audio-cross-check confirmation
(`V01`–`V06`) or a mechanical template-marker discharge (`V07`–`V21`) — no exceptions found.**
This closes the `RULES.md` half of the fabrication question for the whole corpus; nothing
found here overturns or narrows `Q-001`–`Q-006`. The `NOTES.md`/`VISUAL_INDEX.md` half stays
open for 15 lessons and should not be assumed uniform — `V01`, `V05`, and `V06` alone already
show three distinct fabrication mechanisms for those two file types.

### Manual Backtesting

None.

### Ambiguities / Contradictions

None.

### Decisions

None. This discharges an audit the register and `REVIEW_INDEX.md` open item 33 already
authorized in one step; it states no new project-level rule and gets no `DECISIONS.md` entry.

### Files Created/Updated

`00_SYSTEM/QUARANTINE_REGISTER.md` (new entry `Q-007`); `LOG.md` (this entry). No files
under `01_SOURCE_VIDEOS/` were moved, renamed, or deleted; that directory is git-ignored and
carries no tracked changes from this session.

### Verification

`scripts/validate_project.py` run before push; see Git section for result.

### Git

Explicit paths on `git add`; `git status` and `git diff --staged` read before committing.
Committed and pushed this session.

### Next Action

`V07`–`V21` ingestion (transcripts, notes, homework, etc.) is unstarted and out of scope for
this session — proceeds one video at a time in its own dedicated session, per the owner's
existing per-video protocol. Each of those sessions still owes its own `NOTES.md` and
`VISUAL_INDEX.md` fabrication check; `RULES.md` no longer needs re-checking, citing `Q-007`.

---

## 2026-08-12 — Student Session — V06 student pass ("Micro Daily Trends")

### Lesson

V06 — `Bootcamp1 Wk2 032612 Part1 (75mins).swf`, SHA-256 `382207b3…aac96e86`, 01:14:33.
Gate verified OPEN in `18_REVIEW/REVIEW_INDEX.md` (V05 R3 `PASS`, 2026-08-12) **before any
V06 artifact was created**. No override was needed and none was used.

**A state discrepancy was found and reconciled, not papered over.** `REVIEW_INDEX.md`
recorded V05's R3 `PASS` and `COMPLETE`; `COURSE_PROGRESS.md` still read *"V05 — AWAITING
REVIEW R1"* in both its summary block and its table. `REVIEW_INDEX.md` is the gate authority
under `D-004`, so the gate was genuinely open; `COURSE_PROGRESS.md` was stale — the eighth
instance of the `E20` status-staleness class (open item 14). Reconciled in this session's
bookkeeping commit.

### Source Evidence Reviewed

Transcript verified against extracted audio (`ffmpeg -vn -c copy` off the `.swf`, 4473.63 s)
under all four `I-008` criteria. 903-frame Ruffle sweep at 10× on a **patched copy**
(`D-021`), with `D-022`'s port and byte checks run **before** capture and a content
sanity-check against the transcript inside the first minute (GOTCHA 4). Originals re-hashed
after patching: unchanged.

### Work Completed

`02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md`; `04_SCREENSHOTS/V06/` (32 frames + `INDEX.md`);
`03_LESSON_NOTES/V06_SOURCE_NOTES.md`; `03_LESSON_NOTES/V06_INTERPRETATION.md`;
`05_HOMEWORK/V06/` (document, 6 charts, 4 data files, 5 scripts);
`07_MASTERY_REPORTS/V06_MASTERY_REPORT.md`; `QUARANTINE_REGISTER.md` `Q-006`;
`A-050`–`A-054` and ten extended records; `C-006`; `COURSE_PROGRESS.md`; `CHANGELOG.md`.

### Key Findings

**1. V06 has zero course-author runtime — the second consecutive lesson — and this is the
first time `D-025` costs the project something substantial.** V05 yielded no doctrine and
gave up little. V06 states a complete tradeable system: rejection-of-price trigger, a
nameable-pattern filter over a closed set of three, a moving-average location rule, a
counting rule (the second leg takes out `2`), a 25–50 pip pullback band, a stop derived from
moving-average spacing, a 2:1 reward preference, a **two-hour time stop** and a
reversal-pattern exit. **All of it is excluded.** Doctrine produced: zero. Interpreted rules:
zero. Concept library: deliberately untouched.

**2. Speaker identification was run with a method rather than an impression.** 25 `Steve`
tokens, 23 of them the speaker's own third-person references; the two inside read-aloud
questions are each explained. Backed by an F0 profile with **V04 as a positive control** —
the method finds V04's independently established handover at ≈26 minutes unprompted
(≈182 Hz → ≈158 Hz), and finds nothing in V06 (37 of 38 two-minute blocks inside a 13.5 Hz
band). Its limit is stated in three places: it screens for a handover **inside** a file and
**cannot** identify a speaker across files.

**3. Two ambiguity extensions that look like answers are recorded as weakening one.**
`A-044` — V06 enumerates the admissible patterns for the first time in the corpus, and the
DMR curriculum **prints six or seven** where the audio says three, and the presenter breaks
his own filter at `[00:23:25]`. `A-011` — V06 supplies the first candle count ever attributed
to the instructor for M/W, and its own reporter withdraws it four seconds later. **Neither
closes anything.**

**4. `A-018`'s first negative result.** V06 states a stop and a 2:1 ratio and never connects
either to a printed `R = ` label. That is the corpus's best chance so far to test the
"R = risk multiple" reading, and it comes out empty.

**5. `C-006` — two guests, two incompatible definitions of "stop hunt", zero from the
instructor.** V05's is geometric and chart-checkable; V06's is causal and partly
unobservable (spread widening). Filed as corpus hygiene, `C-005` class, **not** charged
against the instructor.

**6. An error this session made and corrected before submission, recorded because the
correction is the point.** An early draft of `INDEX.md` asserted six `R = ` values read off
downscaled contact sheets. Three were re-checked at 2× magnification and **one was wrong**
(`R = 41.5`, recorded as `40.0`). All unverified values were then removed rather than
carried, leaving three transcribed and the rest declared **not transcribed** — the V04 `M6` /
V05 R2 precedent that declining to transcribe an illegible value is correct.

### Manual Backtesting

**None, and the reasoning is in the homework's §0 rather than implied.** V06's rules are
excluded by `D-025`, so there is nothing this project may test; `D-030` blocks it
independently, since *push*, *pullback*, *nameable pattern* and ADR's lookback are all
undefined. `06_MANUAL_BACKTEST/` was not written to by this session and **no `BT_*` observation exists
anywhere in it**, so `D-026`/`D-027`'s gate is not engaged. **A parallel session on this same
branch added `PT-002`–`PT-021` pre-registrations while V06 was being studied** (commits
`2d62e87`, `138fc86`, `6951d1c`, `bfa0b2d`), and separately batch-discharged the `RULES.md`
fabrication check for V07–V21 (`a5ab604`, which cites this session's `Q-006`). **None of that
work is this session's, none of it is V06-derived, and none of it was audited here** — it is
recorded so the interleaved commit history is legible to a reviewer. `PT-001` remains
pre-registered and unrun.

### Homework

Completed on real market data — TradingView **FXCM**, prices read from the platform's Data
Window **DOM text**, never from a pixel (the V02 `MAJOR`, `E06`/`E19`).

- **The assignment as stated is normative in its entirety** (*"find your anchor in today and
  look for three pushes"*), so it was **not performed as stated**. What was performed, and
  what was refused, is listed line by line. The most tempting measurement in the lesson — the
  25–50 pip pullback band — was **refused**, because *pullback* has no definition in this
  corpus (`D-030`).
- **Headline result, methodological:** the undefined ADR lookback moves *"ADR ÷ 3"* by
  **31–60 %** across five windows on four pairs. GBP/USD's push is 15 pips or 23 pips
  depending on a parameter nobody has stated.
- **Second result:** the lesson's two headline figures are on **different scales** — *"ADR ÷
  3"* relative, *"25 to 50 pips"* absolute — so they can agree at only one volatility level.
  Reported with the 2012-vs-2026 regime caveat as prominently as the result.
- **USDCHF's late week open reproduced a third time** (476 = 480 − 4) from a fresh harvest,
  caught by a bar-count check run **before** measuring — the standing V04 lesson applied.
- **A negative reproducibility result:** against V05's committed JSON for the same week, all
  1,912 timestamps and bar counts match exactly, but **120 USDJPY and 66 USDCHF bars differ
  in OHLC by up to ~1 pip.** Any future claim of exact reproducibility on this feed is false
  at that precision.
- 1,908/1,908 continuity, four pairs. Daily extremes reported under **both** `D-031` timezone
  arms, with no conclusion drawn from either.

### Ambiguities / Contradictions

`A-050`–`A-054` opened. Ten records extended (`A-020`, `A-044`, `A-049`, `A-042`, `A-030`,
`A-018`, `A-019`, `A-038`, `A-036`/`A-045`, `A-011`); **none closed** — `D-025` bars it.
`C-006` opened. `C-004` re-checked against V06 and struck off as negative. **`C-003`
deliberately NOT tested** against V06 — its subject is M/W and V06's failure cases are about
pushes; stretching them to fit would repeat the V05 R2 `M7` error. That non-test is stated in
the status block rather than left silent.

### Decisions

**None recorded by this session.** Three items are **escalated** in the mastery report for
the owner or reviewer to decide: (1) a third mastery disposition, `EXCLUDED BY DECISION`,
for work that has subject matter but is forbidden by a standing ruling — re-escalated from
V05 on stronger evidence; (2) whether the project needs to be able to say a record is
**unresolvable in principle** (`A-042`, and now `C-006` from a second direction); (3) whether
speaker identification should become a written **procedure** rather than a bare requirement.

### Process Deviation, Disclosed

`SWF_CAPTURE_RECIPE.md` §9's transcript-before-screenshots order was **not achieved**,
because §§7–8 require looking at contact sheets before naming frames. §§1–10 of the source
notes cite transcript markers only and were not rewritten when §11 arrived, but this session
**cannot claim it was blind to the slides**. Stated as a deviation, worded identically in
`V06_SOURCE_NOTES.md`, `V06_INTERPRETATION.md` §0 and `04_SCREENSHOTS/V06/INDEX.md` — the
`V05 R1 M4` failure class, avoided by construction.

### Files Created/Updated

Created: `02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md`; `04_SCREENSHOTS/V06/` (32 PNG + `INDEX.md`);
`03_LESSON_NOTES/V06_SOURCE_NOTES.md`; `03_LESSON_NOTES/V06_INTERPRETATION.md`;
`05_HOMEWORK/V06/V06_HOMEWORK.md` + `charts/` (6) + `data/` (4) + `scripts/` (5);
`07_MASTERY_REPORTS/V06_MASTERY_REPORT.md`.
Updated: `00_SYSTEM/QUARANTINE_REGISTER.md`; `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`;
`11_CONTRADICTIONS/CONTRADICTIONS.md`; `00_SYSTEM/COURSE_PROGRESS.md`; `CHANGELOG.md`;
`LOG.md`.

### Verification

`scripts/validate_project.py`: **99 passed, 0 warnings, 0 failures.**

`check_quotes.py` over every V06 artifact — `V06_SOURCE_NOTES.md` 259 citations / 0
non-resolving / 32 of 32 quotes matched; `V06_INTERPRETATION.md` 53 / 0 / 24 of 24;
`V06_HOMEWORK.md` 21 / 0 / 11 of 11; `INDEX.md` 8 / 0 / 2 of 2; the new ambiguity records
76 / 5 (all V05 markers, each labelled and each verified against `V05_TRANSCRIPT.md`) / 22 of
22. The transcript header's two declared non-resolvers are `[00:18:00]` (the fabricated
template's timestamp, cited to record that it does **not** exist) and V04 `[00:26:56]`.

### Git

Explicit paths on every `git add` — **never `-A`**; `git status` and `git diff --staged` read
before each of the six commits. Committed at checkpoints throughout the session rather than
in one lump (`D-015`).

### Next Action

**A fresh reviewer session for V06 R1 (`D-003`).** This session authored every V06 artifact
and must not review any of them. The six things the reviewer should test hardest are listed
in `COURSE_PROGRESS.md`'s `NEXT ACTION` block, headed by the one that matters most: **not
"did the student find the rules" but "did the student keep them out".**

---

## 2026-08-13 — Student Session (continuation) — V06 backtest, comprehension probe, second-vendor cross-check

### Objective

Owner direction, 2026-08-13, expanding V06's student scope: a **genuine pre-registered manual
backtest**, **independent comprehension checks** that would expose fabrication or shallow
pattern-matching, and a **cross-check of the homework by an additional independent method**.
Same session as the V06 pass; the stop-before-self-review rule is unchanged and honoured.

### Decisions

**`D-032` written — PROVISIONAL, owner ratification requested.** *Guest material may be TESTED,
never adopted; a test is not a citation.* It refines `D-025` without superseding it: adoption,
citation for or against an instructor rule, merging, and closing an `A-xxx`/`C-xxx` record all
remain forbidden, and **`D-030` is explicitly untouched** — the entry deliberately creates no
route around it. Recorded because an authorized action that lives only in a chat session reads
afterwards as a violation, which is the `D-023` failure.

**`D-028` appended** — the first 70/30 boundaries are pinned, from the actual available ranges,
and **scoped**: each is one series on one vendor at one timeframe, and the two disagree by three
weeks. A project-wide split still needs `I-007`.

### Manual Backtesting — THE MAIN ADDITION

**`PT-022` → `PT-023` → `PT-024`, all committed before the data existed; `BT_V06_0001.md`.**

Only **one** claim in V06 survives `D-030`: *"They don't usually run like London"* `[00:31:20]`.
`PT-022` §1 tabulates why every other claim is blocked — *push*, *pullback*, *nameable pattern*
and the moving-average type are all undefined.

| | |
|---|---|
| **Overall verdict** | **`INDISTINGUISHABLE FROM THE NULL`** (PT-024, n = 41, `EVIDENTIAL`) |
| Second run | `SAMPLE INSUFFICIENT` (PT-023, n = 12, `DESCRIPTIVE`) — reported in full anyway |
| Nulls | N-P sign-flip, N2 circular clock shift; 1,000 iterations; seed `20260812`; **run before the rule arm was read** |
| Holdout | never opened in either test |

**Two re-issues, neither of them period-shopping, and the files argue it rather than asserting
it.** PT-022's period (2015) was out of reach — the feed serves 15m back to 2026-05-31 only,
measured by walking the chart back 368 drags reading **dates only**. PT-023's period was
reachable but not harvestable at n ≥ 30 — the DOM-hover harvester advances ~8 net bars per drag,
so 200 screens returned 24 days. **No result existed at either change**, and both superseded
files are retained unedited.

**The finding is the arm divergence.** Arm A (`UTC−5`) gives median `D` = +3.4 pips, London
ahead; Arm B (`UTC−4`) gives −4.5 pips, New York ahead. Same price path, same window lengths,
same days — the clock moved one hour and the sign flipped. What survives both arms is the
**duration-normalised** comparison: London is the more active window per hour in both
(+1.66, +1.16 pips/h). **So the guest's claim looks true about intensity and unproven about
total range** — precisely the asymmetry `PT-022` §2a predicted before any data existed, because
the New York window is 36% longer.

**The runner prints a per-arm label calling Arm B `CONTRADICTED`. That is not the verdict.**
`PT-022` §6 is conjunctive across arms; quoting Arm B would be arm-selection, `E09` + `E24`.

### Comprehension Verification

`comprehension_probe.py` — **48 machine-checked claims**: 33 written closed-book from memory
(**33/33 pass**) and 15 plausible falsehoods that must be absent (**13/15**), six of them lifted
from the quarantined `NOTES.md`/`RULES.md` for this very lesson.

**Both failures were true, and both corrected my own work:**

- **`N03`** — *"Asian box"* **is** in V06, once, at `[01:09:43]`, inside an audience question.
  My §10 row miscounted the token (4× not 5×, conflating `Asian` and `Asia`) and **omitted the
  one instance containing the literal phrase**, in a row whose entire purpose was to establish
  the box is undefined. Conclusion survived; the evidence was missing where it mattered.
- **`N13`** — a **90% figure** exists at `[00:46:55]` and appeared nowhere in my artifacts.
  In context it is a permission threshold, not a performance claim — but `D-009` has no
  exception for figures used modestly.

**`N06` was a bug in the probe itself** (the pattern `1:3` matched twenty timestamp markers).
Fixed and **documented in the script rather than removed**.

Also added: the lesson in my own words with the inferences labelled as mine; three reasoning
traces each naming the step most likely to be wrong; discrimination probes including the two
places the presenter breaks his own rules; six falsifiable commitments.

### Homework — second-vendor cross-check

`V06_HOMEWORK.md` §9, against the **Yahoo Finance chart API** — a different vendor, JSON
numbers, **nothing rendered at all**.

- **CONFIRMED:** all eight week extremes agree across vendors to ≤4.5 pips; the chart timezone
  is **UTC**, derived rather than assumed (219–230 of 236 bars on three pairs).
- **DEMOTED:** *"480 bars in a trading week"* is a property of the **FXCM feed**, not of the
  market. Yahoo opens the FX week at 23:00 UTC against FXCM's 21:00, consistently, 13 weeks of
  13. Weekly-window tests `PT-008`/`009`/`010`/`012`/`013`/`019` inherit this.
- **REFUSED:** whether USDCHF's missing hour is market or feed **cannot** be settled by this
  vendor — it carries no bar before 23:00 for any pair, so the disputed hour is outside what it
  serves. Reported as unresolved rather than resolved by the 13-of-13 agreement, which concerns
  a different hour.
- **NEW:** two vendors differ on the same bar by sub-pip typically but up to **37–45 pips** on
  an individual low. Any rule triggering on a specific bar's low can fire on one vendor and not
  another.

### Ambiguities / Contradictions

None opened. `A-054`'s interpretation pointer renumbered after `V06_INTERPRETATION.md` §5.3 was
inserted. No record closed — `D-025` and `D-032` both forbid it.

### Deviations, all declared

1. **`MANUAL_BACKTEST_TEMPLATE.md` does not fit** — it is trade-shaped and this test has no
   trades, by pre-registration. §0/§1 followed; §§2–8 replaced by the pre-registered outcome
   structure.
2. **The `D-026` matched-random-**entry** baseline is `NOT APPLICABLE`** and justified: it
   randomizes an entry bar and there is no entry. N2 is the correct null for a clock claim.
3. **PT-023's DEVELOPMENT block is contaminated** — it overlaps the fortnight this session had
   already seen. Disclosed in `BT_V06_0001.md` §1; one more reason its result carries no weight.
4. **The cross-vendor overlap check `PT-024` §5 required was NOT performed** — the two
   DEVELOPMENT blocks do not overlap and the region where the series do is PT-024's holdout.

### Files Created/Updated

Created: `PT-022`, `PT-023`, `PT-024`; `06_MANUAL_BACKTEST/V06/BT_V06_0001.md`, `run_pt023.py`,
`data/` (3 files); `05_HOMEWORK/V06/scripts/comprehension_probe.py`,
`crosscheck_second_source.py`; four `yh30_*.json` and the cross-check output.
Updated: `DECISIONS.md` (`D-032`, `D-028` append); `PRE_REGISTERED/INDEX.md`;
`V06_SOURCE_NOTES.md`; `V06_INTERPRETATION.md`; `V06_HOMEWORK.md`; `V06_MASTERY_REPORT.md`;
`AUTOMATION_AMBIGUITIES.md`; `COURSE_PROGRESS.md`; `LOG.md`.

### Verification

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures** (four new checks, from the
first real backtest observation). `check_quotes.py` clean on every V06 artifact.
`comprehension_probe.py`: 46/48, with both failures explained in-file.

### Git

Explicit paths on every `git add`; `git diff --staged` read before each commit. **The two
pre-registrations were committed before the data existed**, which is the point of them.

### Next Action

**Unchanged: a fresh reviewer session for V06 R1 (`D-003`).** This session authored every V06
artifact, including the backtest, and must not review any of it. Two items now head the
reviewer's list: whether the two backtest re-issues constitute period-shopping (the single most
attackable thing here), and whether `D-032` should be ratified, amended or rejected.

---

## 2026-08-13 — Owner Policy Session — D-033 reverses the guest demotion; D-034 closes I-007; D-035 pins the D-028 boundary

### Objective

Execute two owner instructions and record them as decisions. **Not a study session and not a
review session** — no lesson was studied, no grade was issued, no record was closed.

1. **Reverse the guest-content demotion.** Owner direction: guest-presented content is equal in
   authority to main-host content — *"all knowledge is created equal."*
2. **Formalise the data source (`I-007`) and pin the `D-028` 70/30 boundary dates**, both of
   which gate `PT-001`…`PT-021`.

### Work Completed

**`D-033` — guest material is NORMATIVE on equal footing with the course author.** Supersedes
`D-025` **in part** (the normative exclusion and consequences 1–2) and `D-032` **in whole** (its
test-but-never-adopt fence is now unnecessary). Both retained unedited and marked in place, per
`REMEDIATION_PROTOCOL.md` §2. Guest material may now define rules and thresholds, enter
`12_MASTER_SPEC/` / `13_MACHINE_SPEC/` / `08_CONCEPT_LIBRARY/` and machine candidates, **close**
an `A-xxx` or `C-xxx` on its own, and be cited for or against any other statement.

Three provisions carry over rather than being reversed: **speaker tagging stays mandatory**
(equal authority is not anonymity — with two speakers both able to create doctrine, attribution
matters more), identification is provenance not evidence, and — **inverted** — a guest/instructor
divergence is now a **genuine method contradiction** rather than a corpus-hygiene note.

> **A correction to the instruction as given, made deliberately and on the record.** The task
> named **`D-030`** as a related guest-content ruling to be superseded. **It is not one.**
> `D-030` is *"blocked tests wait for the course; definitions are never approximated"* — it names
> no speaker and bites hardest on **instructor** terms (`A-004` "the level", `A-011` M/W anatomy,
> `A-019` session timezone, `A-039` TDI). The actual guest-content companion to `D-025` is
> **`D-032`**, and that is what `D-033` supersedes instead. Reversing `D-030` would license
> invented definitions across the whole corpus, which no part of the owner's direction asks for.
> **`D-030` is left `ACTIVE` and untouched, and this is flagged to the owner rather than assumed
> either way.** The concrete consequence: **V06 dimension B (Recognition) stays blocked** —
> recognition needs *push* identified on unseen charts and *push* is undefined, which the V06
> report already stated (*"no owner ruling about guest material can unblock it"*).

**`D-034` — the chart data source is declared, closing `I-007`** (open since 2026-08-10).
Nothing was invented: every homework file that opened a chart names the same platform and feed,
so the de facto standard was written down as binding. **TradingView, FXCM feed (`FX:GBPUSD`)**,
no login / no account / no paywalled feature; **platform text only**, never a pixel (the
`E06`/`E19` `MAJOR` from V02 R1); **chart timezone recorded per harvest, never assumed**;
15-minute primary; **Yahoo Finance as a corroboration second vendor only**. Verified across V02
(1h), V03 (4h), V04 (4h + 15m), V05 (15m), V06 (15m + 1D) — **no competing feed exists anywhere
in V01–V06**, and V01 opened no chart. Two vendor-dependent facts carried forward as known: the
FXCM week opens at **21:00 UTC** (Yahoo at 23:00), so *"480 bars in a week"* is a feed fact not a
market fact; and Yahoo−FXCM runs a constant **+3.11/+3.94 pip** offset. `D-034` also makes a
**history-depth probe mandatory per timeframe** before any window is opened.

**`D-035` — the project-wide `D-028` boundary is pinned at `2016-07-01`.** Corpus = the union of
the three pre-registered windows, `2013-01-06 → 2017-12-29` (1,818 days). Oldest 70% =
DEVELOPMENT `2013-01-06 → 2016-06-30`; HOLDOUT `2016-07-01 → 2017-12-29`. The windows were fixed
on calendar grounds before any chart existed and this arithmetic reads no price, so the pin is
not outcome-informed.

### Findings — three, and two of them are unwelcome

1. **Closing `I-007` does not unblock `PT-002`…`PT-021`.** The depth probe already on record
   (`PT-023` §1, 368 drags, dates only) shows **TradingView/FXCM serves 15-minute GBP/USD back
   only to 2026-05-31** — about 2.5 months. `W-A` (2015), `W-B` (2014–15) and `W-C` (2013–17) are
   **out of reach at 15-minute resolution**. This is a **`D-019` measurement** gap, not a
   **`D-030`** definitional one, and it is an **open owner decision** with three honest exits
   recorded in `D-035`: (A) declare a deep-history vendor as an amendment to `D-034`; (B) re-issue
   the batch onto reachable windows, which guts the design; (C) split by timeframe and run a
   **daily-timeframe depth probe** first — cheapest, and diagnostic either way.
2. **`W-C` straddles the pinned holdout boundary by 546 days.** `PT-008`, `PT-009`, `PT-010`,
   `PT-011`, `PT-012`, `PT-013` and `PT-019` therefore **do not conform** and must be re-issued
   under new `PT` numbers with a window inside DEVELOPMENT (`W-C′ = 2013-01-06 → 2016-06-30`,
   ~180 weeks, still well over `n ≥ 30`). Originals retained and marked, never edited. **The
   alternative — moving the boundary so `W-C` fits — was rejected outright**: choosing the split
   to suit the tests is precisely the selection pressure `D-027`/`D-028` exist to remove.
   Consequence of the honest pin: the EU referendum (2016-06-23) lands in DEVELOPMENT, the
   October 2016 flash crash (2016-10-07) lands in HOLDOUT and is unavailable to the Student Phase.
3. **`REVIEW_INDEX.md` open item 40 is MOOT.** The proposed `D-025` carve-out for records whose
   subject is a guest's own utterance or a platform artifact was an exception to a bar that no
   longer exists. `A-043`'s closure **stands** and no longer needs its special argument.

### What was deliberately NOT done

- **No re-grade, no re-certification.** V05 and V06 mastery reports each gain a *"blocking
  condition changed"* block and nothing else; both stay `REVIEW REQUIRED`. Re-assessment is the
  independent reviewer's job under `D-003`/`D-004`.
- **No ambiguity or contradiction closed.** `A-044`, `A-049`, `A-011`, `A-020`, `C-005`, `C-006`
  and V05's "nil return" finding are **flagged for re-assessment**, with the honest note that
  `A-011` should probably stay open anyway (its 9-candle figure is withdrawn by its own reporter
  four seconds later — an evidentiary defect `D-033` does nothing for) and `A-020`'s open half is
  a **period nobody ever stated**.
- **No V05/V06 test cases authored**, and no `PT` file re-issued. Both are follow-up work.
- **`PT-022`/`PT-023`/`PT-024` and `BT_V06_0001` not withdrawn** — work done under a narrower
  fence is valid under a wider one.

### Files Touched

Updated: `00_SYSTEM/DECISIONS.md` (`D-033`, `D-034`, `D-035`; `D-025` and `D-032` marked
superseded in place; `D-028` append; ingestion table); `00_SYSTEM/SETUP_ISSUES.md` (`I-007`
resolved, appended not deleted); `06_MANUAL_BACKTEST/PRE_REGISTERED/COMMON_PROTOCOL.md` (§1, §3a,
§6, §8); `06_MANUAL_BACKTEST/PRE_REGISTERED/INDEX.md` (gate block, §2 coverage, §5);
`07_MASTERY_REPORTS/V05_MASTERY_REPORT.md`; `07_MASTERY_REPORTS/V06_MASTERY_REPORT.md`;
`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`; `11_CONTRADICTIONS/CONTRADICTIONS.md`;
`18_REVIEW/REVIEW_INDEX.md` (open items 3, 40, 55); `CHANGELOG.md`; `LOG.md`.

### Verification

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Git

Explicit paths on every `git add`; `git diff --staged` read before each commit; `git fetch` and
divergence check before push.

### Next Action

**Owner decision owed on the data-availability exit (`D-035` options A / B / C).** Nothing in
`PT-001`…`PT-021` may run until it is made — and option C's daily-timeframe depth probe is the
cheapest next move whichever way the owner leans. **Second, and independent: a fresh reviewer
session** to re-assess V05 and V06 against `D-033`, and to re-read `C-005` as a live method
contradiction. **Third:** re-issue the seven `W-C` tests under conforming windows.

---

## 2026-08-13 — Reviewer Session (V06 R1)

### Lesson
V06 — *"Micro Daily Trends"*

### Review Objective
Independent mastery audit of the V06 student pass (`D-003` — this session authored no V06
artifact). First review conducted with `D-033`/`D-034`/`D-035` in force. Standing owner
directive applied: dimension B (Recognition) is permanently blocked by `D-030` (*push* never
precisely defined in any lecture) — reviewed, documented, and **excluded from pass/fail**.

### Source Evidence Reviewed
`V06_TRANSCRIPT.md` (full read; coverage block re-measured — 1,304 markers, strictly
increasing, gap table reproduces); negative-vocabulary counts re-measured; frames
`V06_00-00-05`, `V06_00-05-29`, `V06_00-48-29` read directly, the last at 2× magnification;
`DECISIONS.md` D-024–D-035; git history for the pre-registration order.

### Student Artifacts Reviewed
`V06_SOURCE_NOTES.md`, `V06_INTERPRETATION.md`, `V06_HOMEWORK.md` (+ data, scripts, charts),
`04_SCREENSHOTS/V06/INDEX.md`, `06_MANUAL_BACKTEST/V06/BT_V06_0001.md` (+ `PT-022/023/024`),
`V06_MASTERY_REPORT.md` incl. comprehension-verification section. Re-ran `check_quotes.py`
(0 failures), `comprehension_probe.py` (48 probes, the two documented correct-failures
reproduce), `run_pt023.py` on both committed datasets (PT-024 reproduces to the digit;
holdout untouched), `validate_project.py` (clean).

### Findings
**0 CRITICAL, 1 MAJOR, 3 MINOR, 3 NOTE** — full detail in `18_REVIEW/V06/V06_REVIEW_R1.md`.
- **M1 (MAJOR, `E07`+`E11`, item 57):** frame `V06_00-48-29` Week 10 prints *"and more
  specifically at 3:45am or 9:45am est."* — legible at committed resolution, elided as
  "not legible", and its absence asserted as *"no session clock appears on any of the 32
  frames"* in two files. First printed `est` in the corpus; bears on `A-019` and `A-030`.
- **M2 (MINOR, item 58):** transcript header's "Steve 25× = 23+2" irreproducible (26 tokens;
  third read-aloud at `[01:11:39]` unclassified). Speaker conclusion unaffected.
- **M3 (MINOR, item 59):** the once-corrected `Asian`/`Asia` row still miscounts (`Asia` 2×).
- **M4 (MINOR, item 60):** `D-033` propagation left the five live `D-025` fences in the V06
  lesson artifacts stating superseded prohibitions in present tense.
- Dimension G audited against §6.G checks 1–20 including the new 15–20: **all clean** —
  pre-registration order verified in git, holdout intact, PT-023 contamination properly
  disclosed and downgraded, both `D-031` arms reported, conjunctive verdict correctly
  preferred over the sharper per-arm label.

### Required Corrections
Items 57–60 (`V06_REVIEW_R1.md` §15). No re-recording, re-harvest or re-test required.

### Decision
**REVISE — 0 CRITICAL / 1 MAJOR / 3 MINOR. The V07 gate stays CLOSED under `D-024`** pending
remediation of item 57 and re-review. Dimension B: blocked by `D-030`, excluded from
pass/fail per owner directive — explicitly not the cause of the REVISE; absent M1 this round
would have opened the gate. Confidence: HIGH.

### Git
Review file `18_REVIEW/V06/V06_REVIEW_R1.md`; `REVIEW_INDEX.md` updated (STATUS, decision
row, E07/E20 counts, severity delta + totals, open items 57–60); this entry.

### Next Review Trigger
Student resubmission of V06 (items 57–60).

---

## 2026-08-13 — Remediation Session (V06 R1 items 57–60) — owner-directed same-session remediation

**Process note, stated up front:** the owner directed this session — the same session that
produced `V06_REVIEW_R1.md` — to perform the remediation and then re-review as R2. Recorded
here per the `D-023` precedent (owner authorization on the record, not in a chat log). The
R1 findings being remediated were this session's own, so R2's verification is of fixes
against primary sources this session re-read frame-by-frame, not self-certification of
student work it authored — the V06 student artifacts remain another session's.

### Item 57 (M1, MAJOR) — APPLIED
- Frame 26 (`V06_00-48-29`) fully re-transcribed at 2×–4×: Week 10's *"and more
  specifically at **3:45am or 9:45am est.**"* and Safe Trade tail completed; Week 1
  ("Anchor patterns", "Research & Development"), Week 4 ("Trading the A and V of the MM
  Trend Cycle"), Week 5 ("Hard **Ridge** Edge" [sic]), Week 9, 11, 12 completed; **Week 13
  (Trade Management & Position Sizing) found partially cut at the frame edge — the syllabus
  has at least thirteen weeks, not twelve.** Superseded readings tabled in the INDEX notice.
- Both false "no session clock on any of the 32 frames" sentences corrected
  (`04_SCREENSHOTS/V06/INDEX.md` summary; `V06_SOURCE_NOTES.md` §11d), superseded text kept.
- `A-019` extended (first printed `est` in the corpus) and `A-030` extended (Brinks fire
  times) in `AUTOMATION_AMBIGUITIES.md`; `V06_SOURCE_NOTES.md` §11b Week-10 quote completed;
  DMR syllabus week-count corrected.
- **Sweep of the other frames performed as required, and it found a further defect:**
  every `R = ` label re-read at 2× across ten frames. Full ledger added to the INDEX
  (24.3, 28.9, 31.1, 41.5, 44.4, 67.3, 80.6, 82.7). `V06_SOURCE_NOTES.md` §11b's original
  R-label cell carried **five wrong values of eight claims** (21.1→31.1; a 24.3 attributed
  to `V06_00-15-49` which carries 80.6/41.5; 47.3→67.3; 38.8→80.6; 26.9→28.9), disagreeing
  with the INDEX and the `A-018` register row (both of which were right) on the same frames
  — the V05 R1B `M9` class. Cell corrected, superseded text retained, `A-018` row completed.
  Charged as `V06_REVIEW_R2.md` **M5** so the error statistics capture it.

### Item 58 (M2) — APPLIED
`V06_TRANSCRIPT.md` § ONE SPEAKER: token total corrected to **26** (accounting stated),
read-aloud class corrected to **three** (adding `[01:11:39]`, the Isubio quotation), own
third-person references 23. Superseded text retained.

### Item 59 (M3) — APPLIED
`V06_SOURCE_NOTES.md` §10: `Asia` corrected to **2×** (`[00:50:25]`, `[01:09:55]`).

### Item 60 (M4) — APPLIED
Dated `D-033` supersession notices added under all five live `D-025` fences
(`V06_TRANSCRIPT.md`, `V06_SOURCE_NOTES.md`, `V06_INTERPRETATION.md`, `V06_HOMEWORK.md`,
`04_SCREENSHOTS/V06/INDEX.md`), each noting `D-030` still blocks the *push*-family
material. **`V06_INTERPRETATION.md` §9 added**: the restated V06 corpus contribution under
`D-033` — seven doctrine-eligible statements (eligibility, not promotion) and the
`D-030`-blocked remainder, per `V06_REVIEW_R1.md` §13.2.

### Verification before commit
`check_quotes.py` 0 failures; `validate_project.py` clean.

### Next
R2 verification review, this session, owner-directed.

---

## 2026-08-13 — Reviewer Session (V06 R2)

### Lesson
V06 — *"Micro Daily Trends"*

### Review Objective
Verification of R1 items 57–60 (remediation at `4c89db1`). Owner-directed same-session
remediation and re-review, disclosed in `V06_REVIEW_R2.md`'s header; `CUMULATIVE_25.md`
should independently re-sample this round.

### Findings
All four items ✅ CLOSED, each verified against a primary-source re-read (frame 26 re-read
at 2× character-by-character; Steve/Asia counts re-measured mechanically and reproducing
exactly; five `D-033` fence notices and `V06_INTERPRETATION.md` §9 checked against markers).
The required item-57 sweep surfaced one further defect — **M5** (`E20`): `V06_SOURCE_NOTES.md`
§11b's R-label cell wrong on five of eight values while the INDEX and `A-018` register row
were right — **fixed and verified in-round**. `A-018`'s negative conclusion survives the
corrected value set. +1 NOTE (N1, closed). `check_quotes.py` 0 failures; validator clean.

### Decision
**PASS — 0 CRITICAL / 0 MAJOR / 0 open MINOR. V06 is COMPLETE. The V07 gate OPENS under
`D-024`.** Dimension B carried as "blocked by `D-030`, excluded from pass/fail per owner
directive" — documented, not scored, per the standing carve-out.

### Git
`18_REVIEW/V06/V06_REVIEW_R2.md`; `REVIEW_INDEX.md` (STATUS, decision row, items 57–60
closed, E20 M5 entry, R2 severity delta + totals); this entry.

### Next Review Trigger
V07 student pass (gate open); `CUMULATIVE_25.md` at its threshold.

---

## 2026-08-13 — Student Session (V07)

### Lesson
**V07 — "Best Trade Grabs"** (`Bootcamp1 Wk2 032612 Part2 (48mins).swf`, 00:48:06).
**Title and session date established from inside the recording** — the title slide prints
*"Best Trade Grabs / MMFx Breakout Session 03-26-2012"*. First lesson in this corpus whose
**date** is printed rather than inferred from a filename.

### Gate
**Verified OPEN in `18_REVIEW/REVIEW_INDEX.md` before any V07 artifact was created** —
*"V06 — PASS at R2 2026-08-13, COMPLETE … V07 gate OPEN."* `D-004` satisfied outright.

### Speaker — step one, before any note
**100% `GUEST`. Zero course-author runtime — the third consecutive lesson** (V05, V06, V07).
Four independent lines: `Steve` occurs exactly twice, both third-person, one of them queueing
Steve as the **next questioner**; `Jim` three times, third-person, credited with a method the
presenter says he cannot do; the staff first-person-plural voice about the DMR; and a flat F0
profile (median 142.9 Hz, sd 6.4 across 25 two-minute blocks, no step). **The acoustic screen
was used only for in-file handover detection** — `COURSE_PROGRESS.md`'s V06 GATE item (a)
prohibition on cross-file use was observed.

Under **`D-033`** the tag records who spoke and does **not** demote. Under **`D-030`**, 8 of the
10 interpreted rules remain blocked.

### Work performed
- **Transcript.** `I-008` all four criteria **PASS**: 539 markers strictly increasing, zero
  duplicates, largest gap 19 s; duration triangulated three ways (audio 2886.95 s, SWF header
  8,661 ÷ 3.0 = 2887.00 s, manifest 2886 s); five 60-second Whisper `small.en` windows match
  near-verbatim; the file preserves its own mishearings (**five different spellings of one
  student's name**); it carries none of the 21-lesson fabrication template. Adopted.
- **Quarantine — `Q-008`.** `RULES.md` **not re-derived** (cited to `Q-007`'s mechanical
  discharge, as `Q-007` authorizes). `NOTES.md` and `VISUAL_INDEX.md` audited individually and
  **both fabricated**. The index claims 7 screenshots; there are **5 files** (two byte-identical
  pairs by SHA-256) and **2 distinct screens**. Entry 004, described as *"50 EMA (Mayo) and 200
  EMA (Blueberry) reaction bounces"*, is a 267×51 image of the words **"Camtasia Studio"**;
  entry 005, *"TDI Blood in the Water Setup"*, is a 137×14 image of **"Camtasia Studio 6"**.
- **Screenshots.** 24 curated frames, Ruffle 10× sweep (588 frames). **`D-022` was load-bearing,
  not ceremonial**: five other sessions' HTTP servers were listening on this machine when the
  port was chosen. Two visual hazards measured and written up — every slide renders
  semi-transparent over a persistent MT4 chart (cause **not** determined and not claimed), and
  two frames are partial repaints keeping the background's outer strips.
- **Notes.** Source notes and interpretation, **every quote machine-verified** against the
  marker range it is cited to. **20 citation errors found and corrected before commit.** Four
  editorial reconstructions moved outside the quotation marks.
- **Homework.** The assignment (`[00:12:09]`, *"How many times over a year…"*) performed on the
  new corpus. **First attempt preserved and it was misleading** — 2015 alone returned 0.996,
  which disagreed with `PT-033`'s wider-window 0.954 and prompted the year-by-year run:
  **2013 0.981, 2014 0.861, 2015 0.996 — the answer moves 12–14 points depending on the year
  chosen.** Seven SVG flashcards built (the artifact the slide defines), positives at an even
  stride and the single negative retained.
- **Manual backtest.** `PT-033` pre-registered and **committed at `81f9ae4` before the runner
  existed**; `BT_V07_0001` run on `D-036a`'s HistData corpus. **The first test in this project
  to reach the pre-registered historical windows.**
- **Comprehension probe.** 75 items across three batteries (45 positive, 16 negative, 14
  reasoning). **74 pass, 1 fails and stays failing.**

### Findings
1. **`PT-033` verdict: `INDETERMINATE`** under its own pre-registered rule (cells 0.9535 /
   0.8096 / 0.8462 / 0.8086 straddle the 0.95 boundary). **My pre-registered prediction
   (`OVERSTATED`, 0.70–0.90) was part right and part wrong**, and is scored as such.
2. **`O2` collapses into `O1`.** At perfect hindsight, *"was a 50-pip run available today"* and
   *"did the day have 50 pips of range"* agree to three decimals in every cell. The claim's
   whole content is *"most days have 50 pips in them"*.
3. **The day boundary is load-bearing (~14 points); the `D-031` timezone arm is not.** A
   pre-registered drop rule interacted with Arm B to create 118 one-hour Friday stub days;
   removing them moves `B · D-SESSION` from 0.8462 to 0.9546, matching Arm A. **Disclosed as a
   post-hoc sensitivity, labelled, reported alongside the headline. `PT-033` not edited. Verdict
   unchanged either way.**
4. **The untaught skill is worth +0.29 to +0.37** in hit rate against a matched random entry.
   The rule arm's percentile within `N1` is 100.0 **and means nothing** — `PT-033` §4 said so
   before the numbers existed.
5. **Comprehension probe `R11` FAILED.** It predicted V07 never uses the compound *"trap move"*.
   It does — once, `[00:14:52]`, **attached to a second leg**. That bears on `A-049`, and the
   first pass of the source notes had missed it. `V07_SOURCE_NOTES.md` §9b is what the failure
   produced; the failing probe is retained rather than reworded.
6. **A student names the inter-presenter divergence out loud** — *"Do all the DM[R] speaker[s]
   agree on this?"* `[00:29:49]` — and **is not told that they do**. Verified mechanically by
   reasoning probe `R07`.
7. **`A-020` fails its Required Research route for a sixth lesson running**, and fails it while
   the lesson has both halves on screen: a **colour** attached to a **period** (`[00:25:34]`) and
   **nicknames** attached to a **timeframe** (`[00:27:24]`), never joined.

### Registers
- **`10_AMBIGUITIES`:** four new records — **`A-055`** (`M0`–`M3` printed level labels),
  **`A-056`** (Hi-Lo, named and untaught), **`A-057`** (*"an A pattern"*, opened with a warning
  it may be ASR garble, **deliberately not merged with `A-047`**), **`A-058`** (*"tilted"* /
  *"slanted"*). **Nine existing records extended, none closed** — under `D-033` a guest *can*
  now close one; the bar is evidentiary and not one of the nine meets it. `A-032` gains its
  **first located instance** in the corpus; `A-044` is extended on a **new axis** (geometry,
  where V06 gave candle names) and the two are **deliberately not merged**.
- **`11_CONTRADICTIONS`:** **no new record.** One candidate — V04's *"12 pairs"* against V07's
  *"the 10 from DMR"* — **checked and rejected** (different objects). `C-005` and `C-006`
  extended and **neither adjudicated** (`D-003`, and `D-033`'s own instruction). `C-001` and
  `C-004` struck off as negative; `C-003` declined deliberately.
- **`00_SYSTEM/QUARANTINE_REGISTER.md`:** `Q-008`.
- **`08_CONCEPT_LIBRARY`:** **not updated, and stated rather than omitted** in the mastery
  report's checklist. Every concept V07 adds is `D-030`-blocked, and the library takes
  definitions. Fourth lesson to leave this box unchecked (V04 R1 `M7`).

### ⚠ Process — `I-009` recurred, against this session's work
A **concurrent session** committing in the same working tree swept
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` — staged by this session, not yet committed — into
**`8785c41`**, a commit about the HistData corpus. **No content was lost; the authorship and the
commit message are wrong.** That session recorded the same class of event against itself in the
same commit. **Not rewritten:** rewriting shared history while another session is actively
committing is worse than the defect. Recorded here, in the mastery report's escalations, and in
`COURSE_PROGRESS.md`'s V07 GATE carry-forward (f). Mitigation adopted mid-session: commit own
work promptly, in small explicit-path chunks, and re-`fetch` before every push.

### Verification before commit
Every marker citation and every quoted string in the transcript header, source notes,
interpretation and the new ambiguity records checked programmatically against the transcript
body — **0 mismatches at commit**, after 20 citation errors and 4 quote-integrity issues were
corrected. Comprehension probe run. `validate_project.py` clean.

### Git
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` *(swept into `8785c41` — see above)*; `aedffbb`
screenshots + `INDEX.md`; `a237220` `Q-008`; `83a3171` source notes + interpretation; `81f9ae4`
`PT-033` pre-registration; `a5ae7dc` `BT_V07_0001` + runner + sensitivity + cross-check;
`450d1ff` homework; `a5369d1` comprehension probe + `A-055`–`A-058` + mastery report; this
entry with `COURSE_PROGRESS.md` and `CONTRADICTIONS.md`.

### Student status
**`REVIEW REQUIRED`** — not `PASS`. Two dimensions are not cleanly satisfiable and the
disposition is the reviewer's: **B (Recognition)** is `D-030`-blocked with no vocabulary to
express that (third lesson running; `REVIEW_INDEX.md` open item 36 is the live proposal), and
**F** carries one `NOT APPLICABLE` a reviewer may overturn to `DEFERRED`.

### Next
**A fresh independent reviewer session writes `18_REVIEW/V07/V07_REVIEW_R1.md`** (`D-003` — this
session must not review its own work). **The V08 gate is CLOSED** until it returns.

---

## 2026-08-13 — Reviewer Session

### Lesson
V07 — *"Best Trade Grabs"* (`Bootcamp1 Wk2 032612 Part2 (48mins).swf`, 00:48:06)

### Review Objective
Independent mastery audit, R1. **`D-003` satisfied** — this session authored no V07
artifact. Source read first per `REVIEW_PROTOCOL.md` §3; every load-bearing count
re-derived mechanically; every script re-run from the committed tree.

### Source Evidence Reviewed
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` in full (all 1,875 lines, header and body);
four load-bearing frames re-read at full resolution (`V07_00-04-00`, `V07_00-13-55`,
`V07_00-18-25`, `V07_00-19-15`); `00_SYSTEM/REVIEW_PROTOCOL.md`, `SETUP_ISSUES.md` I-009,
git history of every V07 artifact.

### Student Artifacts Reviewed
`V07_SOURCE_NOTES.md`, `V07_INTERPRETATION.md`, `04_SCREENSHOTS/V07/INDEX.md`,
`05_HOMEWORK/V07/V07_HOMEWORK.md` + all four scripts, `PT-033`, `BT_V07_0001.md` + all
three scripts, `V07_MASTERY_REPORT.md`.

### What Was Re-Derived Rather Than Accepted
- **Transcript structure** — 539 markers, 539 distinct, strictly increasing, final
  `[00:48:05]`, 7,436 words. Coverage block reproduces exactly, **including its gap
  enumeration** (named by end-marker; all seven values check out).
- **Citation sweep** — 300 distinct marker citations across seven artifacts; every
  non-resolving one declared in advance by the student.
- **Quote sweep** — **239 marker-cited quotes machine-matched against the body. One
  defect (`M3`).**
- **§10's measured negatives** — every cell re-counted. **Two wrong (`M1`, `M2`)**;
  all others correct.
- **Backtest** — `run_pt033.py` re-run: **bit-exact**, `pt033_results.json`
  byte-identical to the committed file, verdict `INDETERMINATE` reproduces.
  `sensitivity_pt033.py` re-run: exact (118 stub days, 15.0 p, 0.8462 → 0.9546).
- **Pre-registration ordering** — `PT-033` `81f9ae4` **08:22:38** precedes runner and
  results `a5ae7dc` **08:29:13**; the runner did not exist in Git beforehand, and it is
  standalone (no dependency on the concurrently-modified `mmm_lib.py`).
- **Homework** — all three scripts re-run: **bit-exact**, including the 16-cell census
  and the raw-M1 cross-check.
- **Comprehension probe** — re-run: **75 items, 1 failure, `R11` still failing.**
- **`validate_project.py`** — 103 passed, 0 warnings, 0 failures.

### Findings
**0 CRITICAL, 0 MAJOR, 3 MINOR, 4 NOTE.**

- **`M1`** (`E20`, count class) — `V07_SOURCE_NOTES.md` §10 states *level* at 26 uses;
  it is **56**, and §5 of the same file says 56. Conclusion unaffected.
- **`M2`** (`E20`, same class) — §10's *"the peak"* row says 4×, lists five markers,
  true count **5**. Row self-inconsistent; conclusion unaffected.
- **`M3`** (`E01`+`E11`) — `V07_MASTERY_REPORT.md` §D renders `[00:28:31]`'s *"in your
  flashcard"* as *"and your flashcard"* and cites `[00:28:28]`. **Falsifies §H's
  categorical claim** that no quotation mark in any V07 artifact contains a word not in
  the source. Only defect in 239 checked quotes.
- **`N1`** — the `I-009` git recurrence: **real event, zero damage** (see below).
- **`N2`** — §H's "163 citations" is stale, not wrong (§9b was added after the sweep ran).
- **`N3`** — the `R11` probe failure is genuine, still failing in committed code, and
  correctly written up as source-notes §9b with its provenance. Verified, not taken on trust.
- **`N4`** — dimension B's missing vocabulary, third lesson running (open item 36).

### The Concurrent-Commit Concern — Audited From Git, Not From The Report
`V07_TRANSCRIPT.md` was indeed swept into **`8785c41`** (the HistData/D-036a commit) by a
concurrent session. **Six checks, all clean: content complete (539 markers, ends
`[00:48:05]`, agrees with measured audio three ways); working tree == committed blob;
exactly one commit ever touched the file; `git fsck` reports ZERO dangling commits; no
authorship git ever held was lost; no branch divergence.** The audit trail is intact.
What is wrong is grouping and commit-message accuracy — a documentation defect, fully
disclosed in three places, and correctly **not** repaired by rewriting shared history.
**No finding charged against the student.** The session's diagnosis went further than
required and improved project method: `git add <paths>` writes into a **shared index**, so
staging discipline cannot prevent this; the corrected form is
`git commit -m "msg" -- <paths>`. **This reviewer used that form.**

### Dimension B — Scored, Not Carved Out
No owner directive was issued for this round, so B was scored under the standard protocol.
**NOT SATISFIED — blocked by `D-030`, structural, not attributable to the student, and
carrying NO severity charge**: the cause is a course that names eight objects and defines
none, and charging it would penalise the discipline the project mandates while rewarding
its violation. It is not smuggled into a `PASS` either — `REVIEW_PROTOCOL.md` §9's PASS
criteria 6–7 are unmet, which is part of why this round is `REVISE`.

### Dispositions Set For The Student
- **Dimension F** — the demo-account `NOT APPLICABLE` is **UPHELD** (`D-018` bars the
  account; `D-019`'s test finds nothing for an agent to do, now or later; matches V01 H6/H7).
- **Dimension B** — scored as above and escalated to the owner.

### Required Corrections
1. `V07_SOURCE_NOTES.md` §10 — *level* 26 → **56** (do not change §5).
2. `V07_SOURCE_NOTES.md` §10 — *"the peak"* 4× → **5×** (the marker list is correct).
3. `V07_MASTERY_REPORT.md` §D — restore *"in your flashcard"*, re-cite to `[00:28:31]`,
   and repair or scope §H's categorical sentence (do not edit source-notes §6c).

**Explicitly not required:** re-running any script (all reproduce bit-exactly), rewriting
git history, or "fixing" the failing `R11` probe.

### Decision
**REVISE** — confidence **HIGH**. 0 CRITICAL / 0 MAJOR / 3 MINOR.
**ADVANCEMENT AUTHORIZED under `D-024`: the V08 gate OPENS**, with the three minors
deferred and still owed. V07 reaches `COMPLETE` only when they are applied and verified
at R2.

The submission is the strongest student work in this repository to date on every
dimension the protocol can score — a pre-registered backtest that reproduces bit-exactly
and returns an honest `INDETERMINATE`, a prediction scored part-wrong against itself, two
self-disclosed defects (the Arm-B stub days and the `C8` hole) measured rather than
assumed away, a preserved misleading first attempt turned into a finding about the
assignment, and a comprehension probe allowed to fail in the committed tree. The three
findings are corrections of the record, not of the method.

### Git
`18_REVIEW/V07/V07_REVIEW_R1.md` (new); `18_REVIEW/REVIEW_INDEX.md` (STATUS with
superseded text retained, decision row, `E01`/`E11`/`E20` ledgers, severity totals,
open items 61–63); this entry. Committed with `git commit -m "…" -- <paths>` per the
corrected `I-009` mitigation — a concurrent session was actively committing in this
working tree throughout the review and its files were read for context and **not touched**.

### Next Review Trigger
Student remediation of open items 61–63, then **V07 R2**. `CUMULATIVE_25.md` should pick
up the `E20` count class (now at seven instances), the `A-039`/`A-056` untaught-component
pattern, and the day-boundary decision gap `PT-033` exposed.

---

## 2026-08-13 — Student Session — V08

### Lesson

**V08 — "Jim's Journey in Learning and Trading MMFX"**, `Bootcamp1 Wk2 032612 Part3 (43mins).swf`,
SHA-256 `6beedb40b7c211cb019b37ff69002e8e625fca4521c3cf3155f946edc5f8b767`, 00:43:03,
session date 2012-03-26.

### Branch and isolation — first full lesson under `D-038`

Worked in a **dedicated git worktree** at `MMM-Agents-v08` on branch **`video/v08`**, per
`D-038`. Merged `origin/claude/add-documents-repository-fdfb3u` at session start — clean
fast-forward, `D-038` (`823458d`) the only incoming commit.

**No `I-009` collision occurred.** `git add -A` was never used; every commit staged explicit
paths and was preceded by `git diff --staged`. **This is the first complete lesson run under the
branch-isolation policy and it is the evidence `D-038`'s consequences section asked for before
`I-009` can be narrowed toward closure.**

**One `D-038` tension, flagged for the owner rather than resolved:** `D-038` says the
append-only ledgers — `DECISIONS.md`, `COURSE_PROGRESS.md`, `LOG.md`, `REVIEW_INDEX.md`,
`SETUP_ISSUES.md` — are edited **on the integration branch**, not on a task branch. This session
was instructed to work only in its worktree and not to merge back, so `COURSE_PROGRESS.md`,
`LOG.md`, `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` were
appended **here**. All are append-only additions in regions no concurrent session is touching,
so the merge should be clean — but it is a deviation from `D-038` and is recorded rather than
absorbed.

### Gate

**Verified OPEN in `18_REVIEW/REVIEW_INDEX.md` before any V08 artifact was created.** V07 R1,
2026-08-13: `REVISE`, **0 `CRITICAL` / 0 `MAJOR` / 3 `MINOR`** → `D-024` opens the gate with the
minors deferred and owed. No override needed or used. `COURSE_PROGRESS.md`'s `V08 GATE` block
still read `CLOSED` (written before R1 returned) and is reconciled in this session's update,
with the superseded text retained.

### Source Evidence Processed

- **Transcript** — verified on four axes and committed (`I-008`). Audio identity by **energy
  envelope cross-correlation r = 0.978–0.981** at a 0.02 s re-encode lag; the waveform Pearson
  `r` is ~0 and that is an artifact, recorded because it read as a disconfirmation for a minute.
  Six Whisper `small.en` spot windows, 0.797–0.977 word similarity, each engine keeping its own
  mishearings. 848 markers, strictly increasing, **measured not asserted**.
- **Speaker tagged FIRST**, per `D-033` provision 1. **100% `GUEST` — the fourth consecutive
  lesson with zero course-author runtime.**
- **26 screenshots** captured by Ruffle 10× sweep, port and served bytes verified (`D-022`).
- **`Q-009`** — `NOTES.md` and `VISUAL_INDEX.md` audited and confirmed fabricated. `RULES.md`
  not re-audited (discharged by `Q-007`).

### Findings

**1. The lesson is incomplete, and that is a finding rather than a defect of the file.** Three
sections plus the DMR planned over ~2 hours; this 43-minute file carries section 1 and most of
section 2 and **ends mid-argument**. The final frame shows a literal `?` at the centre of the
presenter's own ring diagram — the audio-only reading corroborated, not corrected. **Section 3,
the defined-risk lesson, is announced twice and is not in the file.**

**2. `A-056` extended, not closed.** V08 gives the first account anywhere in V01–V08 of what
"Hi-Lo" asks a trader to do — where (the extreme), where in the structure (second leg, at a prior
trap area), what cues it (speed), and — **printed only** — a **10-pip tolerance from HOD/LOD**.
It does not give **how to identify the extreme before it is one**. Under `D-033` this speaker
*could* close the record; the evidence does not reach it.

**3. `C-009` — a normative speaker calls the course's own confirmation requirement a "myth"**, in
printed slide text, having just stated the rule in the course's own voice (*"in **our** basic
training, **we** do say"*). Under `D-025` this was hygiene; **`D-033` provision 3 makes it a real
method-level conflict on an entry condition.** `PROVISIONAL`: the lesson supplies a staging rule
(confirmed live, extremes on demo) that defers rather than dissolves it.

**4. The slides carry a number the audio does not.** Frame `V08_00-05-40` prints *"dealing within
**10 pips of HOD/LOD**"*. The transcript renders it *"with intent pips"* — the ASR's rendering of
*in ten pips*. This is `SWF_CAPTURE_RECIPE.md` §9's case exactly, and it **changed a test design**:
`PT-033` had to invent its tolerance grid; `PT-034` takes `X = 10` from the lesson.

**5. Six new ambiguities.** `A-059` (`CM35`), `A-060` (*"no week that there hasn't been at least
five"* — the strongest empirical claim in V08, wholly `D-030`-blocked), **`A-061`** (*fast* /
*slow* — an **entry cue** whose only criterion is an undefined adjective), `A-062` (a
**fractional** level count, the first in V01–V08), `A-063` (the stop hunt box's **size**, 25 pips,
with no placement rule), `A-064` (Mayo/mail/male).

**6. `A-019` NOT closed, and it was tempting.** `[00:33:30]`'s *"1.30 AM Eastern Daylight Time"*
is the most precise clock reference in the corpus. The bootcamp ran **wholly inside US DST**, so
it is consistent with **both** of `D-031`'s hypotheses and distinguishes them **not at all**.

**7. `Q-009` — the fabrication is ONE GENERATOR, not four failure modes.** `COURSE_PROGRESS.md`'s
V07 item (e) warned *"four lessons, four ways of being wrong, do not assume uniformity"*. The
opposite is true and more useful: `extracted_png_27.png` and `extracted_png_290.png` are
**byte-identical across V05–V08** — the Camtasia Studio logo and the words *"Camtasia Studio 6"* —
and are described as **eight different trading topics**, with timestamps tracking only their
position in the folder listing. V08's own index puts **three timestamps after the file ends**,
sells **four byte-duplicates as separate screenshots**, indexes **one printed sentence split
across two delta tiles** as two unrelated candlestick topics, and attributes **all eleven** entries
to a speaker who does not appear in the lesson.

**8. `PT-034` / `BT_V08_0001`.** Pre-registered at `a4ab65a` **before the runner existed and
before this session parsed a row of the corpus.** The **primary result needed no data and was
stated in advance**: within a day, an entry within `X` pips of the extreme has `MAE ≤ X` by
construction, so *"Risk Reward to 3:1 or greater"* **cannot fail** for any `X ≤ 16.67`. The
empirical arm returned **`CONFIRMED AS TAUGHT`** — 70.5–76.8% vs a matched-random null of
**24.2–24.5%** against a 25.00% break-even. **The observation discloses a defect in its own
pre-registered decision rule** and does **not** edit it. **Independent cross-check against
`PT-033` passes every pre-registered band.**

**9. The homework produced a clean negative.** Twelve hard-right-edge flashcards, answer key
sealed, predictions and reasoning committed to Git before scoring. Using V08's own *"the fast move
is false"* as the predictor: **5/12 = 0.42 against an always-`TARGET` baseline of 0.83.** The
*fast → `TARGET`* half matched the base rate (4/5); the *slow → `STOP`* half went **1/7** and was
actively anti-predictive. Labelled `SAMPLE INSUFFICIENT FOR INFERENCE`.

### Corrections made against this session's own work

- **22 quotations carried silent ASR corrections inside the quote marks** (*"I can see M and W
  patterns"* for the source's *"I can see him in W patterns"*; `CAD-JPY` for `CAD-YEN`; *"go long
  here"* for *"go along here"*). All made literal, glosses moved outside. **This is the defect V07
  R1 charged as `M3`, caught here by a checker rather than by reading.**
- **A frame was misread at half resolution.** The terminal panel's `S/L 1.32360` looked like a
  6.4-pip *initial* stop, which beside *"tighter stops, 3:1 or greater"* would have been the
  corroborating number of the session. It is a **trailed** stop on a short, therefore in profit.
  Died at 3× magnification; a standing prohibition is written into the screenshot `INDEX.md`.
- **The first screenshot sweep captured nothing** — 529 valid PNGs of a static splash, reported
  `DONE`. `SWF_CAPTURE_RECIPE.md` §3's click coordinate misses this file's play button. The sweep
  now aborts non-zero if the frame does not change after the click.
- **Probe `R01` failed on first writing** and the probe was wrong, not the transcript: two of the
  ten tally figures are stated as *"one at London"* / *"one at New York"*, with neither token the
  regex keyed on. Retained in the docstring.

### Student Artifacts Produced

`02_TRANSCRIPTS/V08/` · `03_LESSON_NOTES/V08_SOURCE_NOTES.md` + `V08_INTERPRETATION.md` ·
`04_SCREENSHOTS/V08/` (26 + `INDEX.md`) · `05_HOMEWORK/V08/` · `06_MANUAL_BACKTEST/V08/` ·
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-034_…` · `07_MASTERY_REPORTS/V08_MASTERY_REPORT.md` ·
`00_SYSTEM/QUARANTINE_REGISTER.md` `Q-009` · `10_AMBIGUITIES/` `A-059`–`A-064` ·
`11_CONTRADICTIONS/` `C-007`–`C-009`

### Student Status

```text
REVIEW REQUIRED — not PASS.
8 SATISFIED · 1 SUCCESS AFTER CORRECTION (F) · 1 BLOCKED BY D-030, NOT GRADED (B)
```

**Dimension B is `D-030`-blocked for the FOURTH lesson running**, and the project still has no
vocabulary for that disposition. **That is why this is `REVIEW REQUIRED`.**

### Escalations

1. **`REVIEW_INDEX.md` open item 36 is four lessons old.** Owner ruling owed.
2. **Day-boundary decision, second data point** — 13.8 points on a within-day observable, 2.9 on a
   no-deadline one. A `D-031`-shaped two-arm rule remains the recommendation.
3. **`Q-009`'s three-check screen** for V09–V21's `VISUAL_INDEX.md`. Not a batch discharge.
4. **`A-061`** is the highest-value definitional gap V08 leaves.
5. **`PT-034` §6's defect** suggests a follow-up test against a non-hindsight benchmark — a new
   test, not an edit.
6. **`D-038` ledger-location tension**, above.

### Validator

`python3 scripts/validate_project.py` — **103 passed, 0 warnings, 0 failures.** One failure was
raised and fixed in-session: `BT_V08_0001.md` lacked its `DESCRIPTIVE`/`EVIDENTIAL`/`INVALID`
classification, now `EVIDENTIAL` with the caveat that a sound measurement is not a supported claim.

### Git

Branch `video/v08`, pushed after every checkpoint. Commits, in order: `0c7069a`, `c83f4ca`,
`3026a81`, `20d9938`, `56e2d14`, `cff710c`, `e545d46`, `a4ab65a`, `e3a8e66`, `1d206ab`, `e586db2`,
`c04ef2c`, plus this bookkeeping commit. **No merge to the integration branch was attempted** —
that is a separate, deliberate, single-threaded step under `D-038`.

### Next Review Trigger

**Independent review of V08 — `18_REVIEW/V08/V08_REVIEW_R1.md`, by a session that is not this
one (`D-003`).** The V09 gate is **CLOSED** until it returns.

---

## 2026-08-13 — Reviewer Session (V08 R1)

### Lesson

V08 — *"Jim's Journey in Learning and Trading MMFX"*
(`Bootcamp1 Wk2 032612 Part3 (43mins).swf`, 00:43:03, 100% `GUEST`).

### Review Objective

Independent mastery audit, R1. `D-003` separation of duties **SATISFIED** — this session
authored no V08 artifact.

### Branch basis, and the merge-status question

**Reviewed on `review/v08`, branched FROM `video/v08` at `d9e4f9e`**, in its own worktree at
`/Users/randyschutt/Desktop/Trading/MMM-Agents-review-v08` (`D-038`). `git fetch` established
that **`video/v08` is NOT merged into `claude/add-documents-repository-fdfb3u`** — it descends
directly from `823458d` with no divergence, so a clean fast-forward is available, and
`origin/video/v08` is in sync. Branching from integration would have reviewed an empty set.

**The V08 session's `D-038` deviation is confirmed and is NOT charged against the student.** It
wrote `LOG.md`, `COURSE_PROGRESS.md`, `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md` and
`CONTRADICTIONS.md` on its own branch, and **disclosed it in its own log** rather than resolving
it silently. The policy is one day old, the additions are append-only in untouched regions, and
disclosing a tension is what `D-038`'s consequences section asked the first session under it to
produce. **Flagged to the owner as open item 68**, with the reviewer's observation that the last
three files are not in `D-038`'s enumerated list at all and are exactly what a lesson session
must write — the list may need splitting into *policy* ledgers and *evidence* ledgers.
**Neither `video/v08` nor `review/v08` was merged by this session.**

### Source Evidence Reviewed

The `.swf` itself (SHA-256 re-hashed, `6beedb40…f8b767`, matches `SOURCE_MANIFEST.md`); its
audio, re-extracted and re-measured at **2583.745313 s**; the full verbatim transcript body; the
load-bearing frames **read as images** (the C-009 myth slide, the 3:1 crown-jewel slide, the
section-3 slide, the end card); and the quarantined `NOTES.md` / `VISUAL_INDEX.md` with their
referenced image assets, opened and looked at.

`ffmpeg`'s inability to extract frames past **00:08:56** was reproduced independently, which
corroborates `SWF_CAPTURE_RECIPE.md` §1 as structural. The limit is disclosed in the review
(§0a); frames after that point were verified by reading the student's captures against their own
burned-in timecodes, platform pair-tabs and chart dates rather than by re-capture.

### Student Artifacts Reviewed

`02_TRANSCRIPTS/V08/`, `03_LESSON_NOTES/V08_SOURCE_NOTES.md` and `V08_INTERPRETATION.md`,
`04_SCREENSHOTS/V08/` (26 frames + `INDEX.md`), `05_HOMEWORK/V08/`,
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-034`, `06_MANUAL_BACKTEST/V08/BT_V08_0001.md` and its
scripts and data, `07_MASTERY_REPORTS/V08_MASTERY_REPORT.md`, `00_SYSTEM/QUARANTINE_REGISTER.md`
`Q-009`, `10_AMBIGUITIES` `A-059`–`A-064`, `11_CONTRADICTIONS` `C-007`–`C-009`.

### What was re-derived rather than accepted

- **`PT-034` re-executed**: `pt034_output.txt` **byte-identical** bar the absolute worktree path;
  `pt034_results.json` differs in the single field `runtime_s`. The `PT-033` cross-check re-ran
  **byte-identical** (`CROSS-CHECK: PASS`). The comprehension probe re-ran **byte-identical**,
  58/58.
- **Pre-registration ordering verified in Git**: `a4ab65a` 11:34:31 (prereg) → `e3a8e66` 11:37:43
  (runner) → `1d206ab` 11:44:33 (results), and `--follow` shows the prereg and the runner each
  have **exactly one commit** — neither was ever amended.
- **Homework re-scored** from raw JSON with the reviewer's own code: **5/12 = 0.42**, always-
  `TARGET` baseline **10/12 = 0.83**, `TARGET`-half 4/5, `STOP`-half **1/7**. Commit structure
  confirms predictions were committed **without** the answer key (`e586db2` 11:49:45 vs
  `c04ef2c` 11:52:14).
- **`Q-009` verified by hash and by eye**: `17e5622c255a…` and `9791aacf6433…` present in exactly
  quarantine folders 05–08 and nowhere else; four duplicate pairs byte-identical at the stated
  byte counts; images confirmed to be the Camtasia/TechSmith wordmark, the two halves of one
  printed sentence, and an office photograph.
- **Citations and quotations re-derived mechanically**: 272 marker citations, 193 distinct,
  **zero orphans**; 220 quoted passages checked ellipsis-aware, **zero misquotations** — the 17
  non-matches are all printed slide text or quotations of other documents, each correctly
  attributed.

### Findings

**0 CRITICAL, 0 MAJOR, 3 MINOR, 5 NOTE.**

- **`M1`** (`E11`) — `C-009` Source A omits available corroboration from V07
  `[00:28:02]`–`[00:28:31]`. New sub-class: omitted corroboration, not an absent or wrong
  citation.
- **`M2`** (`E20`) — `PT-034` §4 leaves the matched-random null's entry-**price** convention to
  the runner, which fixes it to the bar's close. Mitigated: committed before it ran, natural
  neutral choice, and the null landed at 0.2424–0.2450 against a closed-form break-even of
  0.2500.
- **`M3`** (`E19`) — a screenshot filename and `INDEX.md` row 26 assert `00:43:10` on a
  `00:43:03` recording; the frame's own burned timecode reads `43:04`. Charged because `Q-009`
  proposes exactly that check as its first fabrication screen.
- **`N1`** branch/merge state and the `D-038` ledger question (open item 68); **`N2`**
  `SOURCE_MANIFEST.md` staleness, pre-existing and not charged; **`N3`** the "186 citations"
  figure is conservative, not inflated; **`N4`** dimension B, fourth lesson (open item 36);
  **`N5`** the reviewer's own delta-tile and 267×51 measurements independently corroborating
  `Q-009`'s mechanism from the source side.

### The seven submitted claims, adjudicated

All seven **CONFIRMED**. The speaker identification, the incompleteness (accurately
characterised, neither overstated nor understated), the backtest figures (70.5–76.8% vs
24.2–24.5%, break-even 25.00%) **and** the correct identification of the 3:1 claim as
arithmetically empty **stated before the run rather than discovered after it**, the `Q-009`
one-generator reduction (a reframing, not a retraction), `C-009` as a genuine method-level
contradiction, dimension B's standard treatment, and the homework's clean negative disclosed
without softening.

### Dispositions set

`A-056` **not closed** — upheld. `C-009` **`PROVISIONAL`** — upheld. `PT-034` **not re-run** —
upheld; a corrected rule is a new test (open item 67). Homework's two `NOT APPLICABLE`s —
upheld. The presenter's name as *probable and unresolved* — upheld.

### Required Corrections

Three, all `MINOR`, none blocking: apply `M1`, `M2` (forward requirement only — `PT-034` must
not be edited), and `M3`. Open items 64–66.

### Decision

```text
DECISION:    REVISE
CONFIDENCE:  HIGH
CRITICAL 0 · MAJOR 0 · MINOR 3 · NOTE 5
ADVANCEMENT: AUTHORIZED under D-024. The V09 gate OPENS.
```

### Validator

`python3 scripts/validate_project.py` — **103 passed, 0 warnings, 0 failures.**

### Git

Branch `review/v08`, branched from `video/v08` at `d9e4f9e`, in its own worktree. Explicit paths
staged only; `git add -A` never used; `git diff --staged` inspected before the commit. Pushed to
`origin/review/v08` as backup. **Not merged** — `D-038` makes merge-back a separate, deliberate,
single-threaded step, and both branches await the owner.

### Next Review Trigger

V08 R2, on student resubmission with `M1`–`M3` applied.

---

## 2026-08-13 — Integration Session — merge-back of `video/v08` and `review/v08`, and `D-038a`

### Objective

The `D-038` merge-back step, performed as its own deliberate act: land `video/v08` and then
`review/v08` on `claude/add-documents-repository-fdfb3u`, and settle `REVIEW_INDEX.md` open
item 68. **No lesson or review work was done by this session** — it merges and rules, nothing else.

### Single-threaded, and verified so before touching anything

`git fetch --all --prune`. `origin/claude/add-documents-repository-fdfb3u` stood at **`23fe5e4`**,
exactly the last known state (the historical-data-import merge) — **no divergence, no surprises**.
Performed in a dedicated worktree at `MMM-Agents-integ`, so none of the four live worktrees
(`MMM-Agents`, `-histdata`, `-review-v08`, `-v08`) was disturbed.

**Topology confirmed before merging rather than assumed:** `video/v08` (13 commits) branches from
`823458d`; integration had advanced **11 commits** since, so this was a real merge and *not* the
clean fast-forward the V08 review recorded as available when it looked — that report was accurate
when written and had been overtaken by the historical-data import. `review/v08` carries **exactly
one** unique commit (`0fe482d`) on top of `video/v08`, so merging it second was guaranteed to
contribute only the review.

### The append-only ledger question — verified, not assumed

The V08 session flagged that it wrote `LOG.md`, `COURSE_PROGRESS.md`, `QUARANTINE_REGISTER.md`,
`AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` from inside its own branch. Checked **before**
merging: the set of files changed by `video/v08` and the set changed by integration since `823458d`
have **zero intersection** — the historical-data import touched only `06_MANUAL_BACKTEST/**`, so
there was no shared ledger region at all. Checked **after** merging:

- `LOG.md`, `QUARANTINE_REGISTER.md`, `AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md` — **pure
  additions, zero deleted lines** against `23fe5e4`.
- `COURSE_PROGRESS.md` — 136 added / 81 changed lines, **74 deletions, all of them the intended
  V07→V08 status rewrite**, superseded text retained. No concurrent edit was overwritten because
  no concurrent branch had touched the file.
- **No duplicate `A-`, `C-` or `Q-` identifier** after the merge. The repeated `LOG.md` section
  headings are pre-existing — counted at **9 before and 9 after**, so the merge introduced none.

**Conclusion: no duplication, no overwrite, no corruption. The deviation cost nothing**, and that
is the measured evidence `D-038a` rests on.

### The one real defect this merge found

**A cross-branch record-ID collision `git` cannot see.** `infra/add-steve-moro-reference-book`
(unmerged, `1728287`) holds a `C-007` and a `C-008` that are **different contradictions** from the
`C-007` and `C-008` `video/v08` has now landed on integration. Both branches append to different
regions of `CONTRADICTIONS.md`, so it will merge cleanly and silently leave four records under two
identifiers. **Not fixed here** — the offending records are on a branch this session was not asked
to merge, and renumbering them belongs to whoever merges it. **Raised as open item 69**, and the
general obligation is written into `D-038a` consequence 1.

### `D-038a` — open item 68 ruled

`D-038`'s single list of integration-branch-only ledgers is split into **POLICY ledgers**
(integration only) and **EVIDENCE ledgers** (task branch, merged with the work), adopting the V08
reviewer's proposal substantially as offered, with a test for files the table does not name: *does
an unmerged edit change what another session is permitted to do?* `D-038`'s superseded paragraph is
**retained unedited** with an amendment pointer, per project convention. The V08 session's handling
is **retroactively correct, not a deviation.** `REVIEW_INDEX.md` is classified as an evidence
ledger with an explicit prompt-merge obligation, because its gate rows do govern other sessions.

### Validator

`python3 scripts/validate_project.py` — **103 passed, 0 warnings, 0 failures** at the baseline,
after the `video/v08` merge, after the `review/v08` merge, and after this bookkeeping commit.

### Git

Merges `46d09ed` (`video/v08`) and `a025b97` (`review/v08`), both `--no-ff` so the merge-back is
legible in `git log`, in that order, one at a time, pushed after the pair. Explicit paths staged
only; `git add -A` never used; `git diff --staged` inspected before each commit.

### Next

`V09` — the gate is **OPEN** under `D-024` (V08 R1: `REVISE`, 0 `CRITICAL` / 0 `MAJOR` / 3 `MINOR`),
with open items 64–66 owed. **Item 69 must be discharged before
`infra/add-steve-moro-reference-book` is merged.**

---

## 2026-08-13 — Remediation Session (V07 R1 items 61–63) — the three MINORs applied on a dedicated branch

**Process note, stated up front.** This session authored **no** V07 artifact and performed
**no** review. It applied the three corrections `V07_REVIEW_R1.md` §15 requires and stopped.
**Nothing here is self-certified:** `D-003` reserves verification to an independent reviewer,
so all three open items move to `APPLIED — PENDING VERIFICATION at R2`, never to `CLOSED`.

**Branch isolation, per `D-038` (adopted earlier the same day).** Work was done on
`fix/v07-r1-minors`, branched from the integration branch after a `git fetch` with a clean
tree and zero divergence (`0 0` against `origin`). **Merge-back was deliberately not
performed** — `D-038` makes integration its own single-threaded act, and it is the owner's.

### Item 61 (`M1`, `E20` count class) — APPLIED
`03_LESSON_NOTES/V07_SOURCE_NOTES.md` §10's *level* row: **26 uses → 56 uses**
(`level` 53 + `levels` 3). **Re-derived from the verbatim body this session, not taken from
the review's prose** — the `level <N>` compound form is 35 and entries containing the token
are 44, so 26 matches no measurement of the object. **§5, which already said 56, was NOT
edited**, as the review requires. The row's conclusion is unaffected and was already
understated: *level* is used constantly and never defined; `A-004` remains untouched.

### Item 62 (`M2`, same class) — APPLIED
Same file, same table, the *"the peak"* row: **4× → 5×**. Re-measured this session at exactly
the five markers the row already listed (`[00:00:26]`, `[00:03:18]`, `[00:03:20]`,
`[00:14:02]`, `[00:16:44]`) — **the marker list was right and is unchanged**, and the
`peak formation` / `PFH` / `PFL` zero counts are unchanged. The row no longer contradicts
itself on its face.

### Item 63 (`M3`, `E01` + co-code `E11`) — APPLIED
`07_MASTERY_REPORTS/V07_MASTERY_REPORT.md` §D, the Sequence table's **Invalidates** cell.
Both defects fixed in one edit, re-derived from `V07_TRANSCRIPT.md`:

- **The quotation** now reads *"If it doesn't do what you expect **in** your flashcard isn't
  the same"* — the transcript's literal wording. The previous *"**and** your flashcard"* was
  the *sensible* reading of a garbled ASR passage, which is exactly why it must not be made
  silently inside quotation marks (V04 `M2` / V05 `M3` class, third instance).
- **The citation** now reads `[00:28:31]`. `[00:28:28]` exists and carries a **different**
  sentence — *"We'll say whether it's something that you will take."*

**§H repaired rather than merely scoped, and the repair was earned.** The falsified sentence
— *"No quotation mark in any V07 artifact contains a word that is not in the source"* — now
states that one such quotation existed, was found at R1, and is corrected. Before re-asserting
a clean claim, a **fresh sweep was run this session rather than trusting the reviewer's 239**:
every `*"…"*` fragment carrying an adjacent `[HH:MM:SS]` citation across all seven V07
artifacts was re-matched against the transcript body — **167 marker-cited quotes, and after
the §D fix, zero contain a word that is not in the source.** The nine flags raised were each
opened by hand and cleared, none a §H exception:

| Flag | Disposition |
|---|---|
| *"Go Trader 4"*, *"Exit +50 pips & 8.57% gain"* (×2), the `V07_00-04-00` bullet slide | **Printed** slide/chart text, labelled `PRINTED` at the point of use — printed source is source |
| *"And so I have 12 pairs that I look at."* (`[00:38:19]`) | A **V04** quote at a **V04** marker, labelled as such and declared in advance in the transcript header's sweep block |
| *"essentially every day"* | **The student's own first reading**, framed as such. Not a source quote |
| *"an M pattern"* (`[00:14:10]`) | A **hypothesised ASR alternative** (*"could be ASR garble for…"*), offered as a candidate. `A-057` logged rather than reconstructed |
| *"tell the whole story"* (`[00:00:32]`) | Every word is in the spoken source (*"do they tell **us** the whole story?"*) **and the string is verbatim in the printed source**, slide `V07_00-00-35`. An un-elided partial, not a substituted word — outside the sentence's class either way |
| *"…I made it dotted in the 13, 50 and the 200"* (`[00:25:44]`) | Elision marked with an explicit `…`; the reading is the declared second ASR pass |

**`N2` folded into the same edit as the review directed** (*"do not refresh it as a separate
task"*): §H's *"163 citations"* is now recorded as **true when measured and since gone stale**
— 190 occurrences / 171 distinct (182 / 168 excluding §11) — with the cause named, §9b having
been added after the sweep ran in response to probe `R11`'s failure. The 163 is left in place
as the record of what the pre-commit sweep actually covered.

**`V07_SOURCE_NOTES.md` §6c was NOT edited**, as the review requires — it renders the same
passage correctly.

### Superseded text, retained at all three sites
Per `REMEDIATION_PROTOCOL.md` §2 and the convention prior rounds established (V05 R1 `M4`,
V06 R1/R2), **no incorrect text was deleted**. Each correction carries the old wording
verbatim in a dated block naming the round, the open item and the finding: one block beneath
§10's table covering `M1` and `M2` together, one beneath §D's table, one inside §H. A note in
§H records that **re-running the sweep now returns a higher raw count precisely because those
retained blocks re-quote the defective renderings on purpose** — expected, not a regression.

### Explicitly NOT done, per `V07_REVIEW_R1.md` §15
No re-run of `PT-033`, the sensitivity, the cross-check or any homework script (all reproduce
bit-exactly). No git history rewritten for `I-009`. **`R11` left failing in the committed
tree.** No re-review, no certification, no merge to the integration branch.

### Verification before commit
`python3 scripts/validate_project.py` — clean. Explicit paths staged; `git diff --staged`
read in full before committing.

### Next
**V07 R2** — an independent reviewer verifies items 61–63. Owner merges `fix/v07-r1-minors`
as a separate deliberate act per `D-038`. Open item 36 (dimension B vocabulary) remains owed
and is untouched by this remediation.

---

## 2026-08-13 — `D-040`: the three-tier sourcing hierarchy is stated once, in one file

**Branch:** `infra/add-steve-moro-reference-book` (off `fix/v07-r1-minors`, per `D-038`)
**Owner instruction:** locate the Steve Mauro seminar-notes PDF, place it in the repo as a
labelled secondary source, extract its contents, and set up a documented three-tier sourcing
hierarchy for vocabulary gaps with an explicit reconciliation rule.

### The PDF was already here — most of this task was done on 2026-08-13 by an earlier session

The document is `Steve **Mauro**` (not "Moro"). Four **byte-identical** copies exist on the
owner's disk (md5 `513d3846e791b42128d40d388079d5b4`, 3,064,761 bytes, 84 pp.) — three loose
copies outside the repo, and one already committed at
`00_SYSTEM/EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_anonymous.pdf`. The loose copies
were left untouched by owner direction.

Commits `7dc53db` → `14f0c70` had already delivered, before this session began:

- the PDF in `00_SYSTEM/EXTERNAL_REFERENCE/` under a 108-line README carrying the provenance
  warning (the title page reads *"Private Study Notes from Seminar of Steve Mauro — Authored by:
  **Anonymous**"*);
- a **2,906-line page-indexed `pypdf` text extract**, so any `MMM-NOTES p.N` citation is greppable
  without opening a binary;
- `EXTERNAL_VOCABULARY_REFERENCE.md` §9 — the PDF read **term by term** against the open records;
- `D-039`, admitting the document as **normative** evidence on the owner's attestation;
- a first pass of the `D-039` queue through `10_AMBIGUITIES/`, resolving `A-014`, `A-023`,
  `A-020` and narrowing `A-031`, `A-032`, `A-055`, `A-005`, `A-022`.

**Steps 1–3 and most of 5 were therefore already satisfied and were not redone.**

### The conflict this session surfaced instead of resolving

The instruction described the PDF as **Tier 2 — "not authoritative"**, and directed that it must
**not** close ambiguity records. **`D-039` says the opposite**: it admits the document as
normative, and `A-014` and `A-023` are **already closed on it**. Adopting the Tier-2 framing
literally would have silently downgraded a standing owner decision and required reopening two
resolved records.

**Raised with the owner rather than assumed.** Owner adjudication, 2026-08-13: **`D-039`
governs; the three tiers are a ranking layer only.** No record was reopened. This is recorded in
`D-040`'s *"Alternatives considered"*.

### What was actually built

| File | Change |
|---|---|
| `00_SYSTEM/SOURCING_HIERARCHY.md` | **NEW.** The canonical statement: the three tiers, the search order, the four relationship cases, and the six-step reconciliation process |
| `00_SYSTEM/DECISIONS.md` | **`D-040`** appended — the hierarchy as a binding decision, with an explicit list of what it does *not* change |
| `00_SYSTEM/EXTERNAL_VOCABULARY_REFERENCE.md` | Header pointer (§5 = Tier 3, §9 = Tier 2); **new §9.2a** on `A-039` |
| `00_SYSTEM/EXTERNAL_REFERENCE/README.md` | Header pointer — the PDF is Tier 2, and a Tier 2 fill-in is provisional |
| `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` | Banner recording the forward obligation and the three standing re-check targets |

**The reconciliation rule is the operative half.** Tier 2 and Tier 3 entries are *provisional
occupants of a gap*. When a **later** video defines the term, **Tier 1 takes priority** and the
fill-in **must be reconciled at that point** — never left standing to silently outrank course
content, never blended into a composite definition no source states. The process is specified as
six steps and four cases, not asserted as a slogan. `A-014`, `A-023` and `A-020` are named as the
highest-priority re-check targets, because each is closed on a tier a later video can overturn.

### The one substantive gap found in the earlier pass — `A-039`

The 2026-08-13 pass recorded the two TDI *signals* (`A-031`, `A-032`) but gave **`A-039` itself no
§9 row**, despite a dedicated *"TDI (Traders Dynamic Index)"* chapter at `MMM-NOTES` **p.45–47**.
Read this session: the chapter names the four lines and their roles (RSI line, trade signal line,
dynamic market baseline, volatility bands applied to the baseline rather than to price) and gives
the shark-fin exit — and supplies **zero numeric parameters**: no period, no band deviation, no
price source, no timeframe, across all 84 pages and all 13 `TDI` occurrences.

**`A-039` was NOT narrowed and NOT closed.** A structure is not a specification, and
reconstructing settings from *"an improved version of the RSI"* is the approximation `D-030`
exists to forbid. Recorded at `EXTERNAL_VOCABULARY_REFERENCE.md` §9.2a.

The §9.3 honest negatives were independently re-verified against the extract this session and all
hold exactly: **zero occurrences** of `anchor`, `Brinks`, `shadow box`, `quarter of wood`,
`tracer`, `vector`, and `800`.

### Explicitly NOT done

No `A-xxx` record was closed, reopened, or changed status. `push` is not unblocked;
V05/V06/V07 dimension **B** stays **BLOCKED**. `D-030`, `D-025`, `D-033`, `D-039` are all
untouched. The three loose duplicate PDFs outside the repo were left alone. **Not merged to the
integration branch** — that is the owner's separate act per `D-038`.

### Verification before commit
`python3 scripts/validate_project.py` — clean, 103 passed / 0 warnings / 0 failures, both before
and after. The 84-page PDF was already tracked, so no new binary entered the index. Explicit
paths staged; `git diff --staged` read in full before committing.

### Next
The `D-039` queue is still only partly worked — the records not named in the 2026-08-13 banner
have not been read against the source. Any session reaching a lesson that touches cross-pair
analysis, the level-counting scheme, or the moving-average set must run `SOURCING_HIERARCHY.md`
§3.1 against `A-014`, `A-023` and `A-020`.

---

## 2026-08-13 — the `D-040` ruling is applied, and §9.6's second divergence is finally filed as `C-011`

**Branch:** `infra/add-steve-moro-reference-book` (continued; no merge)

### The owner's ruling

> Treat the Mauro PDF as **authoritative/normative — same as `D-039` already established — UNLESS
> a video directly contradicts it, in which case the video always wins.** Keep `A-014` and `A-023`
> **CLOSED**; do not reopen them.

This **confirms `D-039` as-is** and makes the override explicit for future cases. It matches the
hierarchy already committed in `b1cb0a3`, so `SOURCING_HIERARCHY.md` and `D-040` needed no
reversal — only the ruling stated in the owner's own words, which is now §1.2's opening block.

**`A-014` and `A-023` were not touched.** Both remain `RESOLVED BY MMM-NOTES`. No `A-xxx` record
had its status changed by any part of this work.

### The real finding: `C-011` was owed and had never been filed

`EXTERNAL_VOCABULARY_REFERENCE.md` §9.6 flagged **two** video-versus-notes divergences on
2026-08-13 and its own rule required a `C-xxx` for **each**. Only one was ever filed:

| Divergence | Record | Was it filed? |
|---|---|---|
| The moving-average set — notes enumerate *"5, 13, 50 and 200"* with **zero** `800` in 84 pp.; V06 audio has *"blueberry"*, owner-confirmed as the **800** | **`C-010`** | ✅ Already filed, and thorough |
| **ADR lookback** — notes say *"the average daily trading range of the **last 2 weeks**"* (`MMM-NOTES` **p.43**); V04's guest says ***"the two previous days"*** `[01:05:36]` **and** an unbounded *"generally every day runs"* `[01:13:34]` | **`C-011`** | ❌ **Never filed — corrected here** |

Both sat in §9.6 marked *"⚠️ Unadjudicated"*, which under the ruling is no longer accurate: the
videos win both, so the notes are **superseded on those two specific points** and must not be
cited as authoritative there. §9.6's table, `SOURCING_HIERARCHY.md` §3.3 and the
`CONTRADICTIONS.md` STATUS block were all updated to say so.

### The asymmetry `C-011` makes concrete, and why `A-038` did NOT move

`C-010` and `C-011` resolve differently in an instructive way. In `C-010` Tier 1 is coherent — the
corpus uses an 800 — so the notes lose and the corpus's answer stands. In `C-011` **Tier 1 is
itself incoherent**: the guest gives *two previous days* and *"generally every day runs"* in one
lesson, with a third variant implied by the template's `TDR/YDR/WADR/MADR/%DADR` panel (`A-040`).

So *"the video wins"* **defeats the notes' clean *"2 weeks"* without installing a replacement.**
`A-038` had three incompatible bases before this record and has three after — a fourth number from
Tier 2 makes four, not one. **`A-038` stays `DO NOT CODE`, unnarrowed**, with `D-030` in full
force and its Required Research unchanged. This is recorded prominently in both `C-011` and
`SOURCING_HIERARCHY.md` §3.3, because the tempting error is precisely to read a won contradiction
as licence to adopt whichever Tier 1 fragment is nearest to hand.

Note also that `A-038` is a **`GUEST`** record: under `D-040` §1.1 a guest is still **Tier 1** and
is *not* demoted to Tier 2, so the video-wins rule applies in full — but `D-033` still means guest
material cannot close the record on its own.

### Files changed
`11_CONTRADICTIONS/CONTRADICTIONS.md` (**`C-011` added**, STATUS counts → 8 records / 7 unresolved
/ 1 resolved-other) · `00_SYSTEM/EXTERNAL_VOCABULARY_REFERENCE.md` (§9.6 table: both rows now
`FILED`) · `00_SYSTEM/SOURCING_HIERARCHY.md` (§1.2 ruling block; §3.3 table + the asymmetry note)
· `LOG.md`.

### Verification before commit
`python3 scripts/validate_project.py` — clean. Explicit paths staged; `git diff --staged` read in
full. **Not merged to the integration branch** — the owner's separate act per `D-038`.

---

## 2026-08-13 — record-ID collision with `video/v08`: this branch's `C-007`/`C-008` renumbered to `C-010`/`C-011`

**Branch:** `infra/add-steve-moro-reference-book` · **Act:** merge-back preparation, per `D-038a`
consequence 1 ("Allocate record identifiers against the latest integration branch … re-check them
at merge-back … The merging session renumbers the later arrival and fixes its cross-references").

### The collision

`video/v08` and this branch ran concurrently under `D-038` isolation and each allocated `C-007`
and `C-008` — to **four distinct contradictions**. `git` could not detect it: the two branches
appended to different regions of `11_CONTRADICTIONS/CONTRADICTIONS.md`, so the merge is a clean
textual addition on both sides and the duplicate identifier survives it silently. `D-038a` names
this exact pair as the worked example of the failure mode.

| ID | `video/v08` (merged first, `46d09ed`) | This branch (later arrival) |
|---|---|---|
| `C-007` | Twenty-nine "set ups" become twenty-nine "trades" inside eight minutes | The moving-average SET: the corpus's `800` against the notes' four-EMA enumeration |
| `C-008` | *"Go off my faith here"* and *"big scientific reason"*, four sentences apart | The ADR lookback window: notes *"2 weeks"* vs corpus *"2 previous days"* |

`video/v08` also holds `C-009` (a normative speaker calls the confirmation requirement a "myth"),
so `C-009` is **taken** and the next free identifiers are `C-010` and `C-011`.

### Resolution

**Merged-first wins the number.** `video/v08`'s `C-007`/`C-008` are untouched. This branch's two
records are renumbered **`C-007` → `C-010`** and **`C-008` → `C-011`**, with the original numbers
recorded in a provenance banner on each record so no citation from before the merge is orphaned.

### Files changed — every reference, not only the records

| File | References renumbered |
|---|---|
| `11_CONTRADICTIONS/CONTRADICTIONS.md` | 13 — both record headings, both STATUS banners, the class-label row; two banner count-lines marked superseded; provenance banner added to each record |
| `LOG.md` | 9 — the `D-040` application entry and its finding tables |
| `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` | 6 — `A-020` disposition, the `RESOLVED BY MMM-NOTES` class row, the blueberry/`800` decode table and its contradiction row |
| `00_SYSTEM/SOURCING_HIERARCHY.md` | 3 — §3.3 table rows for the MA set and the ADR lookback, and the asymmetry note |
| `00_SYSTEM/EXTERNAL_VOCABULARY_REFERENCE.md` | 3 — §9.6's two `FILED` rows and the closing note |

**34 references in 5 files**; zero occurrences of `C-007`/`C-008` remain on this branch.

### Cross-check for further collisions — systematic, not assumed

Every identifier namespace was re-derived on both sides against the merge base `823458d`, rather
than checking only the one namespace the collision was known to be in:

| Namespace | Integration adds | This branch adds | Collision |
|---|---|---|---|
| `C-xxx` | `C-007`, `C-008`, `C-009` | `C-007`, `C-008` | ⚠️ **YES — resolved above** |
| `D-xxx` | `D-038a` | `D-039`, `D-040` | None |
| `A-xxx` | `A-059`…`A-064` | *none* (records moved, none created) | None |
| `Q-xxx` | `Q-009` | *none* (`Q-002` cited only) | None |
| `PT-xxx` | `PT-034` | *none* (`PT-033` cited only) | None |
| `I-xxx` | *none* (`I-010` pre-dates the split) | *none* (`I-008`/`I-009` cited only) | None |
| `18_REVIEW/REVIEW_INDEX.md` items | 64–69 | *none created* — 61–63 updated in place | None |

### Verification before commit
`python3 scripts/validate_project.py` — clean. Explicit paths staged; `git diff --staged` read in
full.

---

## 2026-08-13 — Merge-back — `infra/add-steve-moro-reference-book` (and its two ancestors) integrated; open item 69 discharged

**Act:** integration, single-threaded, per `D-038`. No new research, no new record, no review.

### The topology, established before anything was touched

Three branch names were nominated as possibly-unmerged. They are **one chain, not three parallel
lines** — `git log --graph` settles it and assuming otherwise would have produced two redundant
merges:

```
823458d (D-038)
 └─ 98d893a  fix/v07-r1-minors  — V07 R1 items 61-63 applied
     ├─ 7dc53db … 10a8dc6  infra/external-vocabulary-reference
     └─ 14f0c70  merge: external-vocabulary-reference INTO fix/v07-r1-minors
         └─ b1cb0a3 (D-040) → 1728287 (C-008) → 6ba1024 (renumber)
                              infra/add-steve-moro-reference-book
```

`fix/v07-r1-minors` and `infra/external-vocabulary-reference` are both **ancestors** of
`infra/add-steve-moro-reference-book` (`git merge-base --is-ancestor`, verified for each). Merging
the tip carries all three. Already merged and confirmed so: `video/v08` (`46d09ed`), `review/v08`
(`a025b97`), `infra/gbpusd-historical-data` (`23fe5e4`).

### Open item 69 discharged first, then the merge

`C-007`/`C-008` were renumbered to `C-010`/`C-011` **on the task branch at `6ba1024`, before the
merge**, so the collision never reached the integration branch. 34 references in 5 files; see that
commit's LOG entry for the per-file breakdown and the namespace-by-namespace collision sweep.
`infra/external-vocabulary-reference` needed no separate treatment — being an ancestor, its `C-007`
is the same record.

### Conflicts: four files, all of them two sessions appending at the same place

| File | Conflict | Resolution |
|---|---|---|
| `00_SYSTEM/DECISIONS.md` | `D-038a` (integration) vs `D-039`/`D-040` (branch), appended at the same point | **Both kept**, in numeric order. No decision text altered |
| `11_CONTRADICTIONS/CONTRADICTIONS.md` | `C-007`–`C-009` (V08) vs `C-010`/`C-011` (branch) | **Both kept**, in numeric order — which is what the renumbering was for |
| `LOG.md` | V08 session entry vs the remediation and `D-040` entries | **Both kept** |
| `18_REVIEW/REVIEW_INDEX.md` | 4 hunks — STATUS block, `E11`, `E19`/`E20`, rows 61–69 | **Hand-merged, not taken from one side.** STATUS now carries **both** lessons in remediation (V07 applied-pending-R2 *and* V08); rows 61–63 take the branch's `APPLIED` dispositions, rows 64–69 the integration side's V08 findings; the `E11`/`E20` ledger cells take the integration side's higher counts (14/3/33 — they include the V08 findings) with the branch's `APPLIED 2026-08-13, pending R2 verification` annotation folded into the V07 segments |

Taking either side wholesale in `REVIEW_INDEX.md` would have silently dropped real content — the
V08 findings on one side, the V07 remediation dispositions on the other. Both survive.

### Verification after the merge, re-derived rather than assumed
- **No duplicate `D-`, `A-` or `C-` heading identifier.** `C-001`…`C-011` present exactly once each;
  `D-` tail reads `D-037, D-038, D-038a, D-039, D-040`.
- **No duplicate `Q-`, `I-` or `PT-` record.** One apparent `Q-004` repeat is a `LOG.md` sub-heading
  citing the record, present identically at the merge base `823458d` — pre-existing, not introduced.
- **No duplicate `REVIEW_INDEX.md` open-item number.** Rows 61–69 each appear once.
- **No conflict marker anywhere** in the tree.
- `python3 scripts/validate_project.py` — **103 passed / 0 warnings / 0 failures.**

### Consequences
`REVIEW_INDEX.md` open item **69 → CLOSED**. Open items **61–63** are `APPLIED — PENDING
VERIFICATION at R2` and now visible on the integration branch, so **V07 R2 is triggered**. Items
**64–67** (V08 R1) remain OPEN and are owed. The V09 gate is unchanged: OPEN under `D-024`.

---

## 2026-08-13 — Reviewer Session — V07 INDEPENDENT REVIEW R2 (verification of open items 61–63)

**Role:** Independent Reviewer / Teacher Agent.
**Act:** verification of an applied remediation. **No V07 artifact was authored or edited by this
session, and no remediation was performed** — `D-003` reserves those to other sessions, and a
reviewer that fixes what it finds has stopped being a reviewer.
**Branch:** `review/v07-r2`, cut from the integration branch at `f3f9006` after `git fetch --all`
confirmed no divergence (`D-038`). `REVIEW_INDEX.md` and this entry are written here as **evidence
ledgers** per `D-038a`, and merged with the finding.

### Why a branch, when the content under review is already merged

`D-038`'s rule is branch-per-session whenever concurrent sessions may write, and it does not carve
out review rounds — `review/v08` is the precedent and it used a branch and a worktree. The one
thing that differs here is that V07's artifacts are **already on the integration branch**, so there
was nothing to isolate *from*: no worktree was needed, only a branch, and the merge-back is a
separate single-threaded act. `D-038a` settles the ledger question that `review/v08` had to escalate
— `REVIEW_INDEX.md` and `LOG.md` are evidence ledgers and belong with the work.

### Method — every count re-derived, nothing taken on trust

`D-003` means the remediation's claims get the same treatment R1's did: none. The verbatim body was
extracted once (from `# VERBATIM TRANSCRIPT` to end of file, marker lines stripped) and **every
count was taken twice, by two tools sharing no code** — a Python `re` word-boundary pass and a
`grep -oiE` pass — before the remediated text was read. `wc -w` on that extraction returns **7,436**,
exactly the body size `V07_SOURCE_NOTES.md` §10 states, which anchors the base. The transcript was
verified untouched by `98d893a`.

### Verdicts

| Item | Verdict |
|---|---|
| **61** (`M1`, `E20`) | ✅ **CLOSED — VERIFIED.** `level` **53** + `levels` **3** = **56**, both methods agreeing. The two plausible sub-counts were measured too — compound `level <N>` **35**, marker entries containing the token **44** — so 26 matches nothing, independently confirming R1's diagnosis. §5 verified unedited at 56; `A-004` untouched |
| **62** (`M2`, `E20`) | ✅ **CLOSED — VERIFIED.** *"the peak"* **5**, and **enumerated** rather than only counted: `[00:00:26]`, `[00:03:18]`, `[00:03:20]`, `[00:14:02]`, `[00:16:44]` — exactly the five markers the row listed, in order. A bare `peak`/`peaks` sweep returns the same five and no others. `peak formation`/`PFH`/`PFL` re-measured at 0/0/0 |
| **63** (`M3`, `E01`+`E11`) | ⚠️ **PARTIALLY VERIFIED — STAYS OPEN.** §D half closed and correct; §H half **not verified** — see below |

### The finding: the repair to §H is itself a false categorical claim

R1 required §H's sentence be **repaired or scoped**. The remediation chose repair, explicitly
declined to take R1's count on trust, ran its own sweep, and re-asserted: *"One quotation in the V07
set contained a word that is not in the source… **no other instance exists**"*, with *"it's met"*
and *"mayo"* named among reconstructions *"moved **outside** the quotes"*. **Three quotations
falsify it:**

1. `V07_SOURCE_NOTES.md` **§9a** — `[00:27:24]` quoted as *"30 minute of the water, 30 minute of the
   **mayo**."*; the marker reads *"…30 minute of the **male**,"*. **§10 of the same file measures
   `mayo` at 0** and says the audio only garbles it to *mail*/*male* — so the file again holds a
   right record and a wrong record for one object, which is what item 61 had just been fixed for.
   **§9's evidence table ten lines above renders it correctly**, reconstruction outside the quotes
   with `A-020` provenance.
2. `V07_SOURCE_NOTES.md` **§11** — the row headed *"`[00:25:26]`'s **unrecovered** word"* then quotes
   *"it turns red when **it's met**"*; `[00:25:26]` reads *"…It turns red when **Beth**."*
3. `04_SCREENSHOTS/V07/INDEX.md` **item 6** — same substitution, unbracketed, where **row 15 of its
   own frame table brackets it correctly** as `[it's met]`.

Charged as **one** `MINOR` (`E01`, co-code `E20`), not three: one falsified claim, three sites, one
lapse of a single sweep. **Fourth instance of V04 R1's `N5` class** — narrative prose restating an
evidence table and losing the table's quotation discipline in the restatement; in two of three cases
the correct rendering is in the same file.

**Materiality: none.** `A-020` is not moved, §10's `mayo` 0 row is correct, the ADR observation is
correctly fenced as display behaviour rather than a course rule in both places. It is charged for
R1's own reason: a categorical self-certification is what a later session relies on **instead of
re-checking**, which is precisely what the remediation itself argued when it chose to repair.

### The superseded-text convention — verified SATISFIED

Checked by reading `git diff 98d893a^ 98d893a` in full rather than the commit's description of it.
**21 lines deleted across four files, and every deletion is reproduced verbatim inside a dated
retention block** naming round, open item and finding code — more than `REMEDIATION_PROTOCOL.md` §2
asks for. No incorrect text was silently removed anywhere. The remediation also anticipated
correctly that a re-run sweep would return a higher raw count because the retention blocks re-quote
the defects on purpose: measured at **238 → 252** under this reviewer's definition, all 14 of the
delta retention text.

### Two NOTES, neither a required correction

- **`N1`** — the sweep that earned the repaired claim is **not reproducible**; `98d893a` commits no
  script. In a project that commits its homework scripts so a reviewer can re-execute them, a
  load-bearing count from an uncommitted throwaway is an evidence gap, and it is the gap the three
  instances passed through. Forwarded to `CUMULATIVE_25.md` as a candidate standing rule, not
  invented as an obligation R1 never set.
- **`N2`** — three sweeps of one corpus returned **239** (R1), **238** (this session, pre-remediation
  tree, independently written matcher) and **167** (the remediation). R1 and this session agree to
  one fragment; the 30% gap is the remediation's. One candidate mechanism was **tested**: a
  `\*"(.+?)"\*` pattern without `DOTALL` returns 164 fragments over `V07_SOURCE_NOTES.md` and misses
  the §9a quotation because it wraps across a line break; with `DOTALL` it returns 180 and catches
  it. Candidate, not determination — without the script (`N1`) the cause cannot be established.

### Scope discipline of the remediation — recorded in its favour

Every prohibition in `V07_REVIEW_R1.md` §15 was obeyed, verified individually: `PT-033`, the
sensitivity, the cross-check and the homework scripts were not re-run; no git history was rewritten
for `I-009`; `R11` is still failing in the committed tree; `V07_SOURCE_NOTES.md` §6c and §5 are
untouched and both still correct. The defect found here is a defect of a **sweep**, not of scope.

### Dimension B

Carried from R1 **unchanged** — NOT SATISFIED, blocked by `D-030`, structural, not attributable to
the student, **no severity charge**. No owner directive was issued for this round either.
`REVIEW_INDEX.md` open item **36** is now owed for the **fifth** lesson-round running. Restated,
not re-argued, and not counted again.

### Files produced / updated
- `18_REVIEW/V07/V07_REVIEW_R2.md` — new.
- `18_REVIEW/REVIEW_INDEX.md` — V07 R2 decision row; STATUS block updated with its superseded text
  retained; items 61–62 → CLOSED — VERIFIED; item 63 → PARTIALLY VERIFIED, stays open; new open item
  **70**; `E01` 5 → 6 and `E20` 33 → 34 with the count class recorded as **discharged**; severity
  table and its arithmetic.
- `LOG.md` — this entry.

### Consequences
**V07 does NOT reach `COMPLETE`.** Open item **70** is owed and item **63** stays open until it
discharges. The **V08 gate is unchanged: OPEN** — R1's `D-024` authorization is undisturbed and
nothing found here is CRITICAL or MAJOR. **Next review trigger: remediation of item 70, then R3.**
`python3 scripts/validate_project.py` — **103 passed / 0 warnings / 0 failures.**

---

## 2026-08-13 — Remediation Session (V07 R2 item 70) — the false categorical claim corrected, and the sweep that failed twice replaced by committed code

### Objective

Discharge `REVIEW_INDEX.md` open item **70** — `V07_REVIEW_R2.md` `M1` (`E01`, co-code `E20`), the
sole outstanding item keeping V07 from `COMPLETE`. Branch `fix/v07-r2-item70`, cut from the
integration branch at `6d86272` after `git fetch --all --prune` confirmed no divergence (`D-038`).

**This is a Student remediation session. It verifies nothing and closes nothing** — `D-003`
reserves both to an independent reviewer.

### The defect, and why it is the same defect twice

R1's `M3` was a word substituted inside quotation marks. The remediation of `M3` was asked to
**repair or scope** §H's categorical claim; it chose to repair, on the strength of a sweep it ran
itself and **did not commit** — and the repair was false. R2 located **three** further instances,
two of them the very reconstructions the repaired sentence named as having been moved outside the
quotes.

**The instructive part is not the three words. It is that a stronger categorical claim was asserted
on weaker evidence than the claim it replaced.** `N1` said the sweep was unreproducible; `N2` showed
three sweeps of one corpus returning 239 / 238 / **167**, a ~30% spread. This round treats `N1` as
the finding.

### Verification performed BEFORE any edit

Both markers were re-derived from `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` directly, not taken from
the review's prose:

```text
[00:27:24]  The dashed ones like this are 30 minute versions, 30 minute of the water,
            30 minute of the male,
[00:25:26]  That brown line there is the ADR. It turns red when Beth.
```

**The review's claim is correct at both markers.** *mayo* does not occur in the V07 body at all,
which §10 of `V07_SOURCE_NOTES.md` already measured at **0** — so that file held a right record and
a wrong record for the same object, fourteen sections apart, inside the round that had just
corrected it for the same fault.

### Work completed

- **`V07_MASTERY_REPORT.md` §H** — the false categorical claim corrected. It now states that
  **four** quotations contained a word not in the source (one found at R1, three at R2), and it
  **cites committed code** rather than asserting the completeness of a hand sweep.
- **`V07_SOURCE_NOTES.md` §9a** — `[00:27:24]` restored to the literal *"30 minute of the water,
  30 minute of the male,"*, with *mayo* outside the quotation marks carrying its `A-020`
  provenance, exactly as §9's evidence table ten lines above already had it.
- **`V07_SOURCE_NOTES.md` §11**, the `[00:25:26]` row — *met* taken out of the quotation and
  bracketed as *"it turns red when [it's met]"*, matching `INDEX.md` row 15.
- **`04_SCREENSHOTS/V07/INDEX.md` item 6** — same, bracketed, and given the marker and the
  unrecovered source word it previously lacked.
- **Superseded text retained at all four sites** per `REMEDIATION_PROTOCOL.md` §2, each block
  naming round, open item, finding code and instance letter.

### `N1` discharged — `05_HOMEWORK/V07/scripts/verify_quotes.py`, committed

The substantive change of the round. Every quotation in the seven V07 artifacts is checked against
the transcript body by **committed, re-runnable code**, in two tiers:

- **Tier 1, cited** — a quotation with an `[HH:MM:SS]` in its own context must resolve to the
  transcript exactly. Instances (a) and (b) are tier-1 catches.
- **Tier 2, uncited** — a quotation with no marker is *not* required to match, but is flagged when
  it **tracks a transcript sentence for ≥4 consecutive words and then diverges**, which is the
  shape of this defect. **Instance (c) is a tier-2 catch and is reachable no other way**: it
  carries no adjacent marker, so no citation-windowed sweep could ever have found it. That is the
  mechanism behind `N2`'s 30% spread, and it is now closed rather than hypothesised.

Three design choices were made against measurement rather than intuition, and are recorded in the
script's own docstring: a similarity **ratio** for tier 2 was tried first and **rejected** (it
cannot see *"it turns red when it's met"* against *"It turns red when Beth"*, because the two differ
in length); the quotation pattern was narrowed so a match cannot run past its own closing mark and
swallow the next quotation; and the citation window was stopped at Markdown table-row boundaries,
because extending across them made every printed-slide row inherit its neighbour's marker.

**Results.** Against the **pre-correction** tree: 338 fragments extracted, **exactly the three
instances R2 found, and nothing else**. Against the **corrected** tree: **0 flags**. Non-transcript
quotations are dispositioned rather than ignored — 64 by a reasoned allowlist (printed slide/chart
text, labelled V04 quotes, a hypothesised ASR alternative, the declared second ASR pass), each entry
carrying **its reason** so a later round audits the excuses instead of inheriting them, and 23 by
the retention-block rule. Retained fragments rose 14 → 23 across this remediation: **the expected
audit-trail inflation `V07_REVIEW_R2.md` §4 predicted**, not a regression.

### One further flag, hand-checked and deliberately NOT edited

`V07_MASTERY_REPORT.md` renders `[00:29:49]` as *"Do all the DM[R] speaker[s] agree on this?"*,
bracketing a correction **inside** a token where the transcript reads *"Do all the **DMS** speaker
agree on this?"*. Hand-checked: the bracket convention working as designed, not a substitution.
**R2 did not raise it, and this remediation does not widen its own scope** (`REMEDIATION_PROTOCOL.md`
§3.2). It is recorded in the script's allowlist **with its reason**, so it is visible rather than
silently passing, and **R3 can rule** on whether intra-word bracketing should be spelled
differently.

### Prohibitions honoured, verified individually

`V07_SOURCE_NOTES.md` §9's evidence table, §10's `mayo` **0** row, §5 and §6c are **unedited**;
`INDEX.md` row 15 is **unedited**; items **61** and **62** were **not re-opened**; no V07 script,
homework, backtest or probe was re-run; `R11` is **still failing**; no git history was rewritten;
**no retention block was deleted**, including the ones that re-quote defective text.

### Files produced / updated
- `03_LESSON_NOTES/V07_SOURCE_NOTES.md` — §9a and §11 corrected, superseded text retained at both.
- `04_SCREENSHOTS/V07/INDEX.md` — item 6 corrected, superseded text retained.
- `07_MASTERY_REPORTS/V07_MASTERY_REPORT.md` — §H corrected, superseded text retained.
- `05_HOMEWORK/V07/scripts/verify_quotes.py` — **new**, the discharge of `N1`.
- `18_REVIEW/REVIEW_INDEX.md` — item 70 → ⚠️ **APPLIED — PENDING VERIFICATION at R3**; STATUS block
  updated with its superseded text retained.
- `LOG.md` — this entry.

### Consequences
**V07 still does not reach `COMPLETE`, and this session cannot make it do so.** Item **70** is
applied and owed **verification**; item **63** stays open until 70 discharges; `D-003` reserves both
to an independent reviewer. The **V08 gate is unchanged: OPEN**. **Next trigger: V07 R3**, which
should **re-run `verify_quotes.py` rather than write a fourth sweep** — that is the point of
committing it. For `CUMULATIVE_25.md`: this round is the argument for the standing rule `N1`
proposed — **a numeric or categorical claim asserted in an artifact must be produced by committed,
re-runnable code** — now with a worked instance showing a hand sweep failing twice on the same
corpus and the committed one reproducing the reviewer's findings exactly.

---

## 2026-08-13 — Reviewer Session (V07 R3) — the closing round: items 70 and 63 verified, V07 COMPLETE

### Lesson

V07 — *"Best Trade Grabs"*.

### Review Objective

Independent verification of R2 open item **70** (and the residue of item **63**), plus a standard
pass confirming nothing regressed. Three questions were put to this round explicitly: is
`verify_quotes.py` a sound and reproducible check; is the flagged intra-word bracket a real defect;
and did the remediation overwrite another session's work.

### Review basis, and the `D-038` branch question

Branch **`review/v07-r3`, cut FROM `fix/v07-r2-item70` at `cc74051`**. `git fetch --all` confirmed
the fix branch is **1 ahead / 0 behind** the integration branch — a clean fast-forward, no
divergence. **The V07 content under review was UNMERGED**, so reviewing from the integration branch
would have reviewed an empty set; this follows `V08_REVIEW_R1.md` §3's precedent for exactly this
situation. `REVIEW_INDEX.md` and `LOG.md` written here as evidence ledgers per `D-038a`.

### `D-003` separation of duties

**SATISFIED.** This session authored no V07 artifact and performed no remediation. Per
`REVIEW_PROTOCOL.md` §3 the source was read first: `[00:27:24]` and `[00:25:26]` were read from
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` **before** any remediated artifact text. R2's own verified
numbers were re-derived from scratch by two tools sharing no code, because a closing round should
not inherit the previous round's arithmetic either.

### Source Evidence Reviewed

`V07_TRANSCRIPT.md` verbatim body (7,436 words, `wc -w`, re-measured); markers `[00:25:26]`,
`[00:27:24]`, `[00:28:28]`, `[00:28:31]`, `[00:29:34]`–`[00:29:55]`; the transcript's own
ASR-garble inventory; `V01_SOURCE_NOTES.md` S63 and `V08_TRANSCRIPT.md` `[00:08:58]` for the
bracket-convention precedent.

### Student Artifacts Reviewed

`V07_SOURCE_NOTES.md` §9, §9a, §10, §11, §5, §6c; `V07_MASTERY_REPORT.md` §D, §H;
`04_SCREENSHOTS/V07/INDEX.md` item 6 and row 15; `V07_INTERPRETATION.md`;
`05_HOMEWORK/V07/scripts/verify_quotes.py` (read line by line, re-run, and mutation-tested);
`git diff 6d86272 cc74051` in full.

### Findings

**Items 70 and 63 — ✅ CLOSED, VERIFIED.** All three instances corrected at their sites and matching
the transcript literally. `INDEX.md` item 6 **exceeds** what R2 required — it also adds the missing
`[00:25:26]` citation and prints the literal *Beth*. §H's categorical claim is replaced by a
**historical count** backed by committed code, which is the structurally correct fix rather than a
third attempt at the same sentence. Superseded text retained at all four sites: `V07_SOURCE_NOTES.md`
has exactly **two** deletion lines in the whole commit, both reproduced verbatim. Every prohibition
honoured, verified individually — §9's table, §10's `mayo` **0** row, §5, §6c and `INDEX.md` row 15
byte-identical to `6d86272`; `R11` re-run and **still FAIL**; no history rewritten.

**`N1` — the verifier: re-run, then attacked.** 3 flags on the pre-correction tree at exactly R2's
three sites, 0 after. Mutation testing then found **four precision bounds**: allowlist matching by
`startswith` **can** excuse a longer differently-worded quotation, *although the docstring at line
105 claims it cannot*; `MIN_WORDS = 3`; only `*`-emphasised quotations are extracted; and
`in_blockquote()` is tested **before** the cited-FLAG branch. **All four were then searched by
hand and are empty** — the 22 unemphasised ≥3-word fragments all have a near-miss run of 0, and
every `RETAINED` fragment with a run ≥4 sits in a genuine retention block. **Recorded, not
charged:** §H's surviving claim is true and R3 established it independently of the tool.

**`N2` — the bracket-token item RULED, not deferred.** `DM[R] speaker[s]` against `[00:29:49]`'s
*"DMS speaker"* is **not a defect**. The brackets are a visible signal — whose *absence* is exactly
what R2 charged in instances (a)–(c) — so §H's *"or inside square brackets"* is not falsified;
intra-word bracketing spans V01/V07/V08; the literal *DMS* is recorded in the transcript's own
garble inventory; and *DM* is not a corpus object while *DMR* is heavily attested, so nothing can
mislead. **The remediation was right to flag rather than fix it** — that behaviour is what would
have prevented item 70 a round earlier.

**`N3` — the possibly-overwritten file: investigated, FALSE ALARM, no work lost.** Seven tests:
`verify_quotes.py` exists in **exactly one commit ever**; **not one of the 31 unreachable blobs is
a Python file**; no stash; no `*.orig`/`*.rej`/`*~`/`*.bak`; `git status --untracked-files=all`
clean; no sibling worktree holds one; and the committed diff carries no foreign content. **The
decisive test is the clean untracked set** — R2, the only other session in this working directory,
would have left its sweep visible at any other path, and R2's own LOG lists three files and no
script, describing its sweep in prose *because* it was uncommitted. Most probably the session
observed **its own in-run draft** (the docstring records its design iteration; mtimes fall ~7
minutes inside the session). **Stated honestly: an untracked file leaves no git trace, so this is
"no evidence of loss plus positive evidence of sole authorship", not proof of a negative.**
`D-038` branch isolation is **not** implicated.

**`N4` — the process gap that investigation exposed.** The concern was reported in session output
but **never written to `LOG.md`** — its entry calls the script *"new"* with no mention of the
observed pre-existing state. That omission is the only reason a forensic reconstruction was needed.
Forwarded to `CUMULATIVE_25.md`: record the `git status` observed **at start**, not only the one
produced at commit.

### Required Corrections

**None.** Three recommendations are recorded as explicitly **not owed** and must not open a round:
tighten the allowlist match and fix the line-105 comment when `verify_quotes.py` is next touched;
adopt V08's inline *"the ASR prints `DMS`"* form at the four `DM[R]` sites when they are next edited
for another reason; and carry the `N1`/`N4` standing-rule candidates to `CUMULATIVE_25.md`.

### Dimension B

Carried from R1 and R2 **unchanged** — NOT SATISFIED, blocked by `D-030`, structural, not
attributable to the student, **no severity charge**. No owner directive was issued for this round.
Open item **36** is owed for the **sixth** lesson-round running. Restated, not re-argued, not
counted again, and **it did not hold V07**.

### Decision

**PASS** — 0 CRITICAL / 0 MAJOR / 0 MINOR / 4 NOTE. **V07 is `COMPLETE`.** V08 gate undisturbed.

### Files produced / updated

- `18_REVIEW/V07/V07_REVIEW_R3.md` — new.
- `18_REVIEW/REVIEW_INDEX.md` — V07 R3 decision row (**PASS**, ✅ COMPLETE); items **70** and **63**
  → ✅ CLOSED — VERIFIED at R3; STATUS block moves V07 from `IN REMEDIATION` to `PASSED` with its
  superseded text retained; severity table and R3 arithmetic.
- `LOG.md` — this entry.

### Git

Explicit paths on every `git add`; `git diff --staged` read before every commit. No `git add -A`.
Per `D-038` merge-back discipline the reviewer merges `fix/v07-r2-item70`, with these review commits
on top, into the integration branch — the verdict being clean — after re-fetching to confirm no
divergence. `python3 scripts/validate_project.py` — **103 passed / 0 warnings / 0 failures.**

### Next Review Trigger

**None for V07 — the lesson is closed.** V08 R2 awaits remediation of items 64–66.

---

## 2026-08-13 — Remediation Session (V08 R1 minors, items 64–66)

**Branch:** `fix/v08-r1-minors`, cut from the integration branch
`claude/add-documents-repository-fdfb3u` at `a886585` after `git fetch --all --prune`, per `D-038`.
`video/v08` and `review/v08` were confirmed **already merged** into the integration branch before
branching, so V08's content and its R1 review were both present at the cut.

**Scope:** the three `MINOR` items from `18_REVIEW/V08/V08_REVIEW_R1.md` — open items **64**
(`M1`/`E11`), **65** (`M2`/`E20`) and **66** (`M3`/`E19`). `REMEDIATION_PROTOCOL.md` §3 rule 2
honoured: nothing outside the reviewer's enumerated findings was reprocessed.

**All three are documentation fixes, not evidence fixes** (`REMEDIATION_PROTOCOL.md` §3 rule 3).
No test was re-run, no observation re-derived, no test ID reissued — because no underlying
procedure was found invalid. R1 reproduced `PT-034` bit-for-bit and re-scored the homework
independently.

### Item 64 — `M1` (`E11`) — `C-009` Source A under-sourced

`11_CONTRADICTIONS/CONTRADICTIONS.md` `C-009` gains a **Source A′** block citing **V07
`[00:28:02]`–`[00:28:31]`**, tagged `GUEST`, cross-referenced to `V07_SOURCE_NOTES.md` **§6c**.

**The citation was verified against `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` in this session rather
than copied from the review.** The marked lines read *"Yes, David, it's tough to know when second
legs will be above or below the first leg"* `[00:28:02]`, *"You can only go by the second rail
tracks"* `[00:28:15]`, and the flashcard-pass sentences through `[00:28:31]`. §6c's gloss — *"an
admission of indeterminacy: the direction question is answered 'you can only go by' the
confirmation candle, not by a prior rule"* — was read at source.

**Nothing is superseded.** The defect was an omission of available corroboration, not an error, so
the original Source A stands verbatim. The `PROVISIONAL` disposition is **unchanged**, as R1
directed.

**⚠ One deliberate narrowing of the review's own wording, flagged for R2.** `M1` describes V07's
presenter as *"a different guest presenter"* and REVIEW_INDEX item 64 as *"a different equally-
normative `GUEST`"*. **This session could not verify that and did not repeat it.**
`V07_SOURCE_NOTES.md` records V07 as *"a single unidentified presenter"*; `V08_SOURCE_NOTES.md`
records V08's as unnamed (`D-033` provision 2); and `SOURCE_MANIFEST.md` shows V07 and V08 are
**Part 2 and Part 3 of the same day's bootcamp**, so they may be the **same** person. The added
block therefore claims *a second **lesson***, not *a second **speaker***, and carries that limit —
plus the narrower limit that V07 `[00:28:15]` attests the requirement **in use** rather than
restating V08's two-candle specification — in its own text. Adopting the review's stronger framing
would have written an unverified claim into a contradiction record to discharge a finding about
under-sourcing, which is the failure this item exists to prevent.

### Item 65 — `M2` (`E20`) — the null's entry-price convention

Applied at **two** sites, and **`PT-034` was not edited** — `COMMON_PROTOCOL.md` §9 rule 7 binds a
*completion* exactly as it binds a *correction*, and `git diff` confirms
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-034_crown_jewel_three_to_one.md` is byte-unchanged.

1. **`00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md` §2.1a — new, and this is the binding half.** The
   null's entry-**price** convention is now a **required pre-registration field**; §2.1's
   held-constant table gains an *Entry PRICE convention* row; the requirement to state it **even
   when it differs from the rule arm's** is spelled out; the specific bias it guards — giving a
   null its bar's low for a long or high for a short — is named; and an unstated convention is set
   at minimum a `MINOR` `E20` for reviewer enforcement.
2. **`06_MANUAL_BACKTEST/V08/BT_V08_0001.md` §5** — the results file, at the section where the
   nulls actually are (R1 and the task brief both say *"§4"*, which is `O3`; §5 `O4` is where
   `N1`/`N1b` are computed and printed, so the block was placed there). It states **forward**:
   `N1`/`N1b` enter at the chosen bar's **CLOSE**; the rule arm enters **extreme-anchored** at
   `LOD + X`, or the bar's low where that price falls outside its range. Both traced to the
   implementing functions (`precompute_close_entries()` / `entry_for()`), with a table making the
   asymmetry explicit and the rationale stated so a reader can disagree with it.

**No number changes and nothing is superseded.** The convention was fixed in committed code
(`e3a8e66`) **before** the run (`1d206ab`) and never amended — ordering independently verified by
R1 §0 row 12. Only its *location* was wrong, not its timing. The validating evidence is recorded
with the block: `N1` returned **0.2424–0.2450** against a closed-form break-even of **25.00%**, so
the convention introduced no measurable bias.

### Item 66 — `M3` (`E19`) — the end-card frame's timecode

**The timecode was verified in this session, not taken on the review's word.** The PNG's
bottom-right player chrome was cropped and magnified: the burned-in elapsed field reads **`43:04`**
(the total field is truncated at `43:0` by the frame edge).

`git mv` to **`04_SCREENSHOTS/V08/V08_00-43-04_end-card-innermost-stage-unanswered.png`** — Git
records it as `R`, so the blob and its history survive. **Three** prose references updated:
`04_SCREENSHOTS/V08/INDEX.md` row 26; its *"What the frames settled"* item 7; and
**`03_LESSON_NOTES/V08_SOURCE_NOTES.md` §12 item 4**, which R1 did not enumerate but which carried
the same wrong timecode and was found by sweeping the repo for the old string. Row 26 now states
the frame is the **post-playback end card**, making its relationship to the 00:43:03 runtime
explicit.

**Retention under `REMEDIATION_PROTOCOL.md` §2.** The rename is a file operation, not prose, so the
old filename and all three old values are retained by **explicit naming** in a dated correction
block in `INDEX.md`; `V08_SOURCE_NOTES.md` §12 additionally carries an inline `SUPERSEDED` bracket.

**⚠ One residual found by this session and disclosed rather than glossed, for R2 to adjudicate.**
`00:43:04` is **2,584 s**; the runtime is **2,583.75 s**. The *corrected* label therefore **still
exceeds the runtime, by 0.25 s**, and a naive implementation of `Q-009`'s screen will still flag
row 26. This is unavoidable rather than a further defect — a player's whole-second elapsed field
cannot print `43:03.75` and shows the ceiling, so the frame **cannot** carry both its true burned
timecode and a strictly-under-runtime label, and matching the artifact's own internal evidence is
the correct choice. `INDEX.md` records the consequence for whoever implements the screen: **flag
`timestamp > ceil(runtime)`, not `timestamp > runtime`**, or it false-positives on the legitimate
final frame of any recording whose duration is not a whole number of seconds. Under that form
`00:43:10` remains a true positive and `00:43:04` is not. A mechanical sweep of all **26** V08
filenames confirmed row 26 was the only one over runtime.

### NOTHING IS SELF-CERTIFIED

**`D-003` reserves verification and closure to an independent reviewer.** This session neither
re-reviewed V08 nor closed anything. Items 64–66 move to **`APPLIED — PENDING VERIFICATION at
R2`**, not to `CLOSED`. Two of the three carry an explicit disagreement or residual addressed to
R2 rather than resolved here, and both are stated in the artifacts themselves, not only in this
log.

### Files produced / updated

- `11_CONTRADICTIONS/CONTRADICTIONS.md` — `C-009` Source A′ (item 64).
- `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md` — §2.1a new, §2.1 table row (item 65).
- `06_MANUAL_BACKTEST/V08/BT_V08_0001.md` — §5 convention block (item 65).
- `04_SCREENSHOTS/V08/V08_00-43-04_…png` — renamed from `…00-43-10…` (item 66).
- `04_SCREENSHOTS/V08/INDEX.md` — row 26, item 7, dated correction block (item 66).
- `03_LESSON_NOTES/V08_SOURCE_NOTES.md` — §12 item 4 (item 66).
- `18_REVIEW/REVIEW_INDEX.md` — items 64–66 → APPLIED, PENDING VERIFICATION; STATUS block with
  its superseded text retained.
- `LOG.md` — this entry.

**NOT edited, deliberately:** `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-034_crown_jewel_three_to_one.md`
and `18_REVIEW/V08/V08_REVIEW_R1.md`.

### Git

Explicit paths on every `git add`; `git diff --staged` read before every commit. No `git add -A`.
Four commits on `fix/v08-r1-minors` — one per item, one for the ledgers — then pushed.
`python3 scripts/validate_project.py` — **103 passed / 0 warnings / 0 failures.**

**MERGED TO INTEGRATION, on the owner's instruction, later the same day.** The remediation branch
was **first pushed unmerged** — `D-038` makes merge-back a separate, deliberate, single-threaded
act and this session does not take it on its own initiative. The owner then directed the merge.
Performed per `D-038`: re-fetched, verified **no divergence** (the integration branch had not
moved from `a886585` since the branch was cut), merged **`--no-ff`** so the merge-back is legible
in `git log`, validator re-run **clean after the merge**, then pushed.

**The merge changes nothing about the items' status.** They remain `APPLIED — PENDING
VERIFICATION at R2`. Merging is a code-movement act, not a verification act, and `D-003` reserves
closure to an independent reviewer. Project precedent is explicit that a `REVISE` with 0
`CRITICAL` / 0 `MAJOR` does not block a merge (V03–V07, and `V08_REVIEW_R1.md` §3 item 1).

### Next Review Trigger

**V08 R2**, on verification of items 64–66.

---

## 2026-08-13 — Reviewer Session (V08 R2) — the closing round: items 64–66 verified, the presenter question ruled, V08 COMPLETE

### Lesson

V08 — *"Jim's Journey in Learning and Trading MMFX"* (`Bootcamp1 Wk2 032612 Part3 (43mins).swf`).

### Review Objective

Independent verification of the remediation of `V08_REVIEW_R1.md`'s three `MINOR` findings
(open items 64–66), plus a full standard pass for regression. `D-003`: this session authored
**no** V08 artifact and **no** part of the remediation, and re-derived every claim from primary
sources **before** reading the remediation's account of itself.

### Review Basis

Branch **`review/v08-r2`, cut from the integration branch at `a6ee013`**, in a **dedicated
worktree** at `/Users/randyschutt/Desktop/Trading/MMM-Agents-review-v08-r2` (`D-038`).
**`fix/v08-r1-minors` was ALREADY MERGED** when the round opened (`dd787d9` / `a6ee013`), so the
review was taken on the integration tip rather than on the fix branch. `git fetch` confirmed the
integration branch level with `origin` — 0 ahead, 0 behind.

### Source Evidence Reviewed

`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` `[00:27:41]`–`[00:28:40]` and its whole `Ray`/`Jim` token
set; `02_TRANSCRIPTS/V08/V08_TRANSCRIPT.md` `[00:00:32]`–`[00:06:05]`, `[00:17:29]`, `[00:20:49]`
and its speaker-identification section; `02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md` (`Ray` sweep);
`00_SYSTEM/SOURCE_MANIFEST.md` (part ordering); `03_LESSON_NOTES/V02_SOURCE_NOTES.md` and
`V03_SOURCE_NOTES.md` (the coach roster); and
`04_SCREENSHOTS/V08/V08_00-43-04_end-card-innermost-stage-unanswered.png` **read as pixels**.

### Student Artifacts Reviewed

`11_CONTRADICTIONS/CONTRADICTIONS.md` `C-009` `Source A′`; `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`
§2.1a; `06_MANUAL_BACKTEST/V08/BT_V08_0001.md` §5; `06_MANUAL_BACKTEST/V08/run_pt034.py`;
`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-034_crown_jewel_three_to_one.md`;
`04_SCREENSHOTS/V08/INDEX.md`; `03_LESSON_NOTES/V08_SOURCE_NOTES.md` §12.

### Findings

**Items 64, 65 and 66 are all ✅ CLOSED — VERIFIED. 0 `CRITICAL`, 0 `MAJOR`, 0 `MINOR`, 3 `NOTE`.**

Nothing was taken on the remediation's word:

- **Item 64** — the V07 `[00:28:02]`–`[00:28:31]` citation was **read at source**. All four
  fragments verbatim; the `[00:28:28]` omission honestly marked with an ellipsis; and
  `[00:28:31]`'s garble *"if it doesn't do what you expect **in** your flashcard isn't the same"*
  **preserved** — the exact passage V07's item 63 was charged for smoothing to *"and"*, avoided
  in the one file where tidying it would have been easiest. `GUEST` tag, §6c cross-reference and
  `PROVISIONAL` all correct; Source A verbatim and the block purely additive.
- **Item 65** — `entry_for()` and `precompute_close_entries()` were **read**, and both documented
  descriptions are **exact** (`resolve(hi, lo, i, cl[i], d, n)` — the null's entry price is
  literally the bar's close). **`PT-034` is byte-unchanged**: `git log --follow` shows exactly
  one commit ever and `git diff a4ab65a HEAD` on the file is **empty**. All four `N1` medians
  re-read from the committed output — 0.2450 / 0.2426 / 0.2424 / 0.2429 — so the claimed
  `0.2424–0.2450` is exact, and the break-even recomputes to 0.250037. §2.1a goes **beyond**
  R1's ask: it names the bias it guards and sets a reviewer-enforcement floor.
- **Item 66** — the player chrome was cropped, linear-stretched and magnified 20×, and the
  burned-in elapsed field **reads `43:04`**. Four references verified updated; an independent
  repo sweep for the old string found **no fifth** (every survivor is a retention block, the R1
  file, `LOG.md` history, or a real `[00:43:10]` marker in V01/V06). The rename preserves the
  blob at 100 %. All 26 frame timecodes re-derived: row 26 is the only one over raw runtime, at
  exactly `ceil(2583.745) = 2584`, and nothing flags under `> ceil(runtime)`.

**`N1` — the presenter-identity question is RULED, not deferred a second time.**
**V07's and V08's presenters are DIFFERENT MEN, `HIGH` confidence, on textual evidence only.**
V08's speaker names **Ray** three times in the third person, at `[00:00:49]` — forty-nine seconds
into Part 3 — as the man who *"was"* taking the questions, and again at `[00:05:59]` handing the
baton; `Ray` occurs **zero** times in V07's body and **zero** in V06's. V07 is the Q&A part
(sixteen named questioners read aloud); V08 reads none. Independently, V07's presenter defers to
**Jim** ×3 and at `[00:07:43]` **disclaims** the high-of-day skill that V08's second half teaches
under a deck titled *"Jim's Journey"*, and the programme roster names Ray and Jim as distinct
coaches. Probable names (V07 = Ray, V08 = Jim) at `MEDIUM` — provenance, not evidence, per
`D-033` provision 2 — held back by one residual stated rather than smoothed: V08 `[00:17:29]`
*"Jim's right about that one"* is unexplained, and does **not** touch the different-men finding,
which does not require the identification. **No cross-file F0 comparison was used**:
`COURSE_PROGRESS.md` V06 GATE item (a) prohibits it, and the ruling is unchanged without it.
**R1's *"a different guest presenter"* is SUPPORTED — and the remediation's refusal to write it
unverified was still the right act**, so no finding is charged. Carried as item 71, a
documentation follow-up not owed as a defect.

**`N2` — a concurrency incident, charged to process and not to V08.** Partway through this review
a concurrent session moved the **shared main working directory** onto `review/v09` (`bb4097b`), a
tree descended from `f3f9006` that predates **both** the V07 R2/R3 merge **and** the entire V08
remediation. The failure mode is **silent** — plausible file contents, no error, and a reviewer
would have found the remediation's work simply absent. It surfaced only because `18_REVIEW/V07/`
listed one file where three are committed ancestors. **Contained:** a dedicated worktree was
created and every post-switch read re-run there before use; two stale `REVIEW_INDEX.md` reads
were discarded and redone. **No conclusion rests on a read from the wrong tree**, and the main
directory was left on `review/v09` as found. Carried as item 72.

**`N3`** — the bracketed ASR expansion *"second rail[road] tracks"*, already ruled not-a-defect at
V07 R3; recorded only so a future mechanical verbatim sweep does not re-charge a closed question.

**Regression: none.** The remediation touched 8 files — additive but for three replaced timecode
strings, each read individually. No script, data file, transcript, homework artifact or
pre-registration was altered. `crosscheck_pt034_vs_pt033.py` re-runs to `CROSS-CHECK: PASS`.

**Dimension B** carried from R1 **unchanged**: `NOT SATISFIED`, blocked by `D-030`, structural,
not attributable to the student, **no severity charge**. Open item 36 is owed for the **fifth**
lesson-round and needs an **owner** ruling; it is not a gate and it did not hold V08.

### Required Corrections

**None. Nothing is owed by V08.** Items 67 (a `PT-034` successor), 71 and 72 are carried as
recommendations and process matters, none of them a gate.

### Decision

**`PASS`. CONFIDENCE `HIGH`. V08 is `COMPLETE`.** The V09 gate was already OPEN under `D-024` and
is unaffected.

### Git

Commits on `review/v08-r2`, all with explicit paths (`git add -A` never used), `git diff --staged`
inspected before each:

```text
18_REVIEW/V08/V08_REVIEW_R2.md   (new)
18_REVIEW/REVIEW_INDEX.md        (STATUS, decision table, delta, severity totals,
                                  E11/E19/E20 rows, items 64-66 closed, items 71-72 opened)
LOG.md                           (this entry)
```

`REVIEW_INDEX.md` and `LOG.md` are written on the task branch as **evidence ledgers** per
`D-038a`, and the branch is merged back by this reviewer as the deliberate `D-038` merge-back
step, the verdict being clean.

### Next Review Trigger

**Independent review R1 of V09.** Its student submission exists on the unmerged branch
`video/v09` (`bb4097b`) and was **not** part of this round.

---

## 2026-08-13 — Student Session — V09

### Lesson

**V09** — `Bootcamp1 Wk2 032612 Part4 (53mins).swf`,
SHA-256 `b0f36b5540de7a76397c80202cf6a721a2a18aa9011c5698238c6bcc624168d4`, 00:52:26.
**No printed title** — none is asserted anywhere.

**Branch `video/v09`, in a dedicated worktree (`D-038`). No `I-009` collision.**
Evidence ledgers written on the task branch, as `D-038a` now expects rather than tolerates.

### Gate

**Verified OPEN in `18_REVIEW/REVIEW_INDEX.md` before any V09 artifact was created** — V08 R1
returned `REVISE` 0 CRITICAL / 0 MAJOR / 3 MINOR, which opens the gate under `D-024`.
`COURSE_PROGRESS.md`'s `V09 GATE` block still read `CLOSED`; it was written before V08 R1 returned
and was correct when written. Reconciled this session, superseded text retained.

### The carry-forward hypothesis was predicted, tested, and confirmed

The V09 gate block set a falsifiable test written by the previous session: *if V09 opens with
V08's announced-but-missing section 3, V09 is the same presenter continuing.* **It does.** Four
non-acoustic strands: a resumption opening, the announced content (defined risk), V08's ring
diagram resumed by name (*"inner shell"*, *"the circle within the circle"*), and V09's own
pre-playback splash frame being V08's closing card. **The `f0_profile.py` acoustic screen was NOT
run across files**, as V07's carry-forward prohibits.

**Fifth consecutive lesson with zero course-author runtime (V05–V09), and the first whose
cross-file continuity was predicted in advance and then confirmed on evidence chosen in advance.**

### What V09 contributes

**The corpus's first position-sizing rule, and it is complete.** `balance × 0.02 ÷ stop_pips`,
**cumulative across all open positions** (stated twice — the easiest thing in V09 to code wrong),
same lot size through losses 1–3, recalculate on loss 4 and after every win, 25/50 at 2:1 and
15/50 once HOD/LOD entries are mastered. Printed on slides, so it does not rest on ASR.

**It also answers V08's unanswered question.** V08 ends on a literal red `?` at the centre of its
four-ring model; V09 `[00:19:48]`–`[00:20:27]` says the innermost ring is **discipline in keeping
to the risk plan**.

### Artifacts

| Artifact | Note |
|---|---|
| `02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md` | 721 markers, verified on four axes. Stated **MONOTONIC NON-DECREASING**, not strict — three same-second pairs exist and the block says so |
| `04_SCREENSHOTS/V09/` | **27 frames + INDEX.md.** 27/27 burned timecodes verified, zero drift over 52 minutes, every value below the runtime |
| `03_LESSON_NOTES/V09_SOURCE_NOTES.md`, `V09_INTERPRETATION.md` | Every substantive row carries a **basis tag** — see the deviation below |
| `05_HOMEWORK/V09/` | H1 + comprehension + equity-path simulation, 4 scripts, 8 data files |
| `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-035…`, `06_MANUAL_BACKTEST/V09/BT_V09_0001.md` | Pre-registration `0f709d2`, runner `7c3fe2d`, both before execution |
| `07_MASTERY_REPORTS/V09_MASTERY_REPORT.md` | `REVIEW REQUIRED` |
| Registers | **`A-065`–`A-075`** (11), **`C-012`–`C-015`** (4), **`Q-010`** |

### The backtest — and the control that killed half of it

`PT-035` / `BT_V09_0001`. **CONTRADICTED AS STATED** on *"it's highly unlikely we're gonna lose
three or four times in a row"* — `run4_obs` 27.4–48.7% across four cells against a 10% threshold
fixed before any number existed.

**The verdict needs no measurement at all**, and that is the part worth quoting: at V09's own
advertised `>50%` accuracy, P(any 4-loss run in 200 trades) = **99.9%**; at `PT-034`'s measured
73%, still **54.1%**. `O4`: you would need **p ≥ 84.2%**.

**`N3`, the pre-registered sanity control, FAILED — and the estimator it condemned was this
session's own.** Comparing a fixed-composition sequence against `(1 − p̂)⁴` is wrong by the
sampling-without-replacement factor. `PT-035` §7b said in advance that an `N3` failure voids
`O3`, so **`CLUSTERING CONFIRMED` is not reported even though the runner printed it**, and
prediction `P4` is scored **VOID**, not `RIGHT`. **The runner's decision logic does not encode
§7b's gate; the pre-registration is right and the runner is wrong, and neither is edited**
(`COMMON_PROTOCOL.md` §9 rule 7). `BT_V08_0001` precedent, second application.

A third defect is disclosed against the run's own interest: 34.6–49.8% of drawn trades were
unresolved at the horizon, which biases `p̂` **downward** because a 50-pip target is censored more
often than a 15/25-pip stop. `P2` was WRONG for exactly that reason.

**`REVIEW_INDEX.md` open item 65 is discharged** — the null's entry-price convention is fixed in
`PT-035` §4's parameter table rather than in the runner.

### Homework

H1 done and cross-checked **16/16 against two sources that do not cite each other** — V09's own
worked example (7/7) and `MMM-NOTES` p.67's `RISK LEVEL` table (9/9), which never states the
formula in words. This verifies `C-015`'s corroboration half in code.

Comprehension: **9 right / 0 wrong / 1 manual**, ten answers with reasoning traces **committed at
`97d2c1b` before the scorer was written**. The write-up says plainly that 9/9 is unimpressive on a
lesson printed in plain English and points the reviewer at the four questions with attractive
wrong answers.

Equity-path simulation of V09's own algorithm: **all four predictions RIGHT**. The 4-loss trigger
fires in 100% of sequences, median 21–31 times per 200 trades; median drawdown 62–76%, above 8% in
4,000 of 4,000; **0 wipeouts**. **The 8% is not a drawdown cap and is very readable as one.** What
it does *not* show is stated as prominently: the streams are matched-random at a below-break-even
hit rate, and no sizing rule survives a negative edge.

**H3/H4 `DEFERRED` (`D-019`), blocked by `A-004`** — and **a substitute predictor was proposed in
an earlier draft, then refused in writing**, with the superseded text retained.

### The `SOURCING_HIERARCHY.md` §3.4 obligation — discharged

**Tier 1 spoke on the moving averages.** `A-020`'s *Blueberry* is upgraded from owner attestation
to **`RESOLVED BY COURSE`** on `[00:41:43]` — *"the 800 on the 15 minute time frame"* — and gains
a **timeframe** no source previously carried. All six §3.1 steps run; superseded basis retained.
**The grape is kept out of the mapping** on the speaker's own disclaimer (*"Steve doesn't teach
it"*).

**`C-010` is NARROWED and NOT closed.** `[00:41:48]` *"which makes this a 200"* would dissolve the
conflict — and `MMM-NOTES` states no timeframe anywhere in its EMA section, so adopting it means
supplying Tier 2 with a fact it does not contain. **Refused per §3.2's *"Do not blend."***

### Q-010 — the fabrication generator, measured rather than inferred

Normalising away per-lesson tokens and hashing all 21 lessons: **`RULES.md` is TWO templates**
(V09 sits with V01, whose copy `D-017` proved false against verified audio); **`VISUAL_INDEX.md`
is NINE**, one covering nine lessons — it was **not** previously known to be templated;
**`NOTES.md` is 17**, and is therefore the only one still needing a genuine per-lesson audit.

**V09's own audio REFUTES the EMA nickname table** rather than merely failing to support it:
`NOTES.md` says *"200 (Blueberry), 800 (Raspberry)"*; V09 `[00:41:43]` says the blueberry **is**
the 800.

**A sixth failure mode, and it defeats the cheapest screen:** V09's one real image is **a genuine
frame from the correct lesson** carrying an entirely invented description. Hashing across lessons
— `Q-009`'s proposed screen — cannot catch that. **This session's first reading was that the image
was stolen from V08; that was WRONG and the correction is recorded in the register rather than
deleted.**

### ⚠ Process — one checklist box unchecked, disclosed rather than omitted

**`SWF_CAPTURE_RECIPE.md` §9's transcript-first evidence ordering was NOT met.** Auditing a
fabricated `VISUAL_INDEX.md` and naming 27 frames both require opening images, and both
necessarily preceded typing the notes. **Every substantive note row instead carries a basis tag**
(`AUDIO` / `PRINTED` / `AUDIO+PRINTED` / `VISUAL`) so a reviewer can strike every non-`AUDIO` row
and see what survives — which is what the ordering rule exists to enable. **Submitted as a genuine
deviation, not as a compliant alternative.**

### ⚠ Process — the recipe's play-button coordinate is wrong for this file

`SWF_CAPTURE_RECIPE.md` §3/§10's `mouse.click(512, 300)` **misses on V09**, whose stage renders in
a small centred box before playback with the play button at `(512, 325)`. The first sweep produced
**638 identical frames of a static splash** and everything downstream looked healthy — server
verified, bytes matched, `__ready` true, 638 valid PNGs. **The only thing that caught it was
opening a frame and looking at it.** Same lesson as `D-020`'s retraction in a different costume.

**`D-022` also fired for real**: port 8931 was probed first and found **BUSY**, held by another
session's `http.server`. Port 8947 was bound and confirmed by `lsof` to be this session's own PID.

**The recipe fix is a POLICY-ledger edit under `D-038a` and is owed on the integration branch.**

### Citation discipline

Mechanical citation sweeps were run over every file before commit and caught **thirty-two**
off-by-one marker citations. Final: 36/36, 39/39, 112/112, 7/7, 66/66, 22/22, 7/7, 6/6, 16/16 —
every citation resolves to a real marker whose words contain the quoted text.

### Escalations

1. **Dimension B `D-030`-blocked for the fifth consecutive lesson** — `REVIEW_INDEX.md` open item
   36 needs an **owner** ruling; a student session cannot supply one.
2. **`SWF_CAPTURE_RECIPE.md`'s play-button coordinate** — policy edit, integration branch.
3. **Two `PT` successors specified and not run**: the clustering test `PT-035` could not perform,
   and the resolution-censoring bias, **which may affect other tests in the `PT-002`…`PT-032`
   family** sharing a day-end horizon with asymmetric geometry.
4. **`C-010`'s tidy reconciliation is available and refused** — an **owner** call, flagged rather
   than made silently.
5. **`A-004` is now the project's largest single blocker.** Undefined after nine lessons and 50
   uses in V09 alone; it blocks dimension B, V09's own homework, `A-070`, `A-073`, `A-075` and
   every one of V09's twelve directional calls.

### Git

Commits on `video/v09`, all with explicit paths (`git add -A` never used):

```text
5cd3680  transcript(V09) — four-axis verification; continuity predicted, tested, confirmed
9ab0e71  screenshots(V09) — 26 curated frames, 26/26 timecodes, first sweep discarded
ff7b8bd  quarantine(Q-010) — fabrication REFUTED by V09's own audio; generator measured
3cef607  notes(V09) — position sizing; A-020 reconciliation; refusals recorded
a94d009  registers(V09) — A-065..A-075, C-012..C-015, A-020/C-010 reconciliation
0f709d2  pre-register(PT-035) — committed before any bar was read
7c3fe2d  runner(PT-035) — committed before execution
572c87a  backtest(BT_V09_0001) — CONTRADICTED; clustering VOID on a failed control
97d2c1b  homework(V09) — answers and predictions committed before the scorer
1b29c61  homework(V09) — H1 cross-check, 9/9 comprehension, equity path
```

### Decision

**STUDENT STATUS: `REVIEW REQUIRED`** — a submission, not an authorization (`D-016`/`I-001`).

### Next Review Trigger

**Independent review R1 of V09** (`D-003`). This session did not review itself and **did not merge
to integration** — merge-back is a separate single-threaded act under `D-038`.

---

## 2026-08-13 — Reviewer Session (V09 R1)

### Lesson

**V09** — **no printed title** · `Bootcamp1 Wk2 032612 Part4 (53mins).swf`,
SHA-256 `b0f36b5540de7a76397c80202cf6a721a2a18aa9011c5698238c6bcc624168d4`, 00:52:26.

**Role:** Independent Reviewer / Teacher Agent. `D-003`: this session authored **no** V09
artifact and performed **no** remediation.

**Branch:** `review/v09`, branched **FROM `video/v09` at `bb4097b`**, which was **unmerged and
diverged 11 commits each way** from the integration branch. Reviewing it from integration would
have reviewed an empty set — the `V08_REVIEW_R1.md` §3 precedent.

### Review Objective

Independent mastery audit of the V09 student submission, plus adjudication of the nine items the
submission and the review brief put forward for checking.

### Source Evidence Reviewed

The `.swf` itself (re-hashed, audio re-extracted and re-measured, header parsed);
`02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md` in full, with its timestamp structure re-derived
mechanically; the pre-ingestion `audio_10.mp3`; **six frames read as images** —
`V09_00-00-10` (the ring diagram), `V09_00-02-05` (the printed formula), `V09_00-22-45` (the 85%
caption), `V09_00-28-45` (the FXDD title bar, and its oscillator sub-panel **magnified**), plus
`V08_00-43-10_end-card…` for the strand-4 comparison; and the SWF headers of **all 21** files in
`01_SOURCE_VIDEOS/Forex Bootcamp/Bootcamp/`.

### Student Artifacts Reviewed

`03_LESSON_NOTES/V09_SOURCE_NOTES.md`; `V09_INTERPRETATION.md`; `04_SCREENSHOTS/V09/INDEX.md`;
`05_HOMEWORK/V09/` (all scripts and data); `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-035_…md` **at its
commit `0f709d2`**; `06_MANUAL_BACKTEST/V09/BT_V09_0001.md` and `run_pt035.py`;
`07_MASTERY_REPORTS/V09_MASTERY_REPORT.md`; `Q-010`; `A-065`–`A-075`; `C-012`–`C-015`;
`COURSE_PROGRESS.md`.

### Findings

**`REVISE`, `HIGH` confidence. 0 `CRITICAL`, 0 `MAJOR`, 6 `MINOR`, 8 `NOTE`.**

Nothing load-bearing was accepted on the submission's authority:

- **`PT-035` re-ran to a byte-identical `data/pt035_output.txt`**, and all three homework scripts
  re-ran to byte-identical output.
- **The headline binomial result was re-derived from first principles** in this reviewer's own
  run-length recursion, not checked against the runner: P(≥1 four-loss run in 200) = **99.93%** at
  p = 0.50, **54.13%** at p = 0.73, and the ≤5%-in-100 threshold at **p ≥ 84.19%**. Every reported
  figure confirms. A shared bug in `run_pt035.py` would survive a re-run and not survive this.
- **The continuity prediction is genuine and is verified in Git:** `3026a81` at **11:10:45** and
  `d9e4f9e` at **11:59:51**, both authored by the **V08** session, against V09's first artifact at
  **13:21:36**. Strand 4 was confirmed by **comparing V08's end card and V09's opening frame
  image-to-image**. The unrun acoustic screen is **not a gap** — running it was prohibited.
- **The `N3` self-correction is real, not narrated.** The committed runner output prints
  `CLUSTERING CONFIRMED` and scores `P4 RIGHT`; `BT_V09_0001` withdraws both and scores `P4`
  **VOID**, with correct sampling-without-replacement algebra.
- **312 marker citations machine-checked, ZERO orphans**; 217 quotations checked; all seven of the
  mastery report's citation counts re-derived and reconciling.
- **The capture bug is confirmed and generalised** from the SWF headers of all 21 files: **V08,
  V09 and V21 declare a 1280×738 stage; the other 18 declare 1024×786.** It is stage geometry,
  not a per-file fluke — confirmed against the letterbox bands in the committed pixels.

**The six `MINOR`s:** `M1` four silent ASR corrections inside quotation marks under `AUDIO` tags;
`M2` `PT-035` §6's `INDETERMINATE`-on-`N3`-failure clause neither applied nor disclosed for the
empirical arm; `M3` a false MEASURED count in the transcript's COVERAGE block (four 10-second gaps
claimed, seven measured); `M4` fourteen frame cross-references off by one across five files; `M5`
the candidate `C-010` reconciliation held at *"more likely than not"* when it breaks three of four
set members and collides with `A-020`; `M6` the capture-bug escalation's claim that the coordinate
worked on V01–V08, when V08's own index records the identical failure.

**Rulings on what the submission asked:** the evidence-order deviation is **NOT charged** — the
basis-tag replacement was tested and the position-sizing system, the innermost-ring answer and the
`A-020` resolution all survive on `AUDIO`-only rows. `A-065`'s `CODABLE AS STATED — DO NOT EXTEND`
is **UPHELD**. `C-014` is **already at the note grade** and needs no change. **`C-010`'s refusal to
close is UPHELD** — and on stronger ground than the submission gives, which retires its own
escalation 5 to the owner. The censoring-bias concern is **well-founded and escalated**, with the
scope tightened from `PT-002`…`PT-032` to the tests that actually race asymmetric barriers.

**Dimension B: NOT SATISFIED, blocked by `D-030`, scored rather than carved out, carrying NO
severity charge.** Fifth consecutive lesson; open item **36** escalated for the fifth time.

**`N8` is against this reviewer, not the student.** `REVIEW_INDEX.md` item 72 — the concurrent
session that moved the shared main working directory onto `review/v09` partway through the V08 R2
round — **was this session**, and this round did **not** use a dedicated worktree. Disclosed in the
review rather than left to be inferred.

### Required Corrections

Six, all `MINOR`, carried as open items **73–78**. Plus **79** (the `PT-035` successor,
recommended not owed) and **80** (the censoring-bias investigation, escalated). None blocks V10.

### Decision

```text
LESSON:      V09
DECISION:    REVISE
CONFIDENCE:  HIGH
CRITICAL 0 / MAJOR 0 / MINOR 6 / NOTE 8
ADVANCEMENT: AUTHORIZED under D-024. The V10 gate OPENS.
             V09 reaches COMPLETE only at R2.
```

### Git

`18_REVIEW/V09/V09_REVIEW_R1.md` written on `review/v09`. The integration branch was merged
**into** `review/v09` first — it had advanced through V07 R2/R3 and, mid-round, V08 R2 — so this
round's `REVIEW_INDEX.md` and `LOG.md` additions sit on top of that work rather than reverting it.
Both are **evidence ledgers** under `D-038a` and are written here.

**This round DOES merge back, and it must.** `SWF_CAPTURE_RECIPE.md` is a **policy ledger** under
`D-038a` and the confirmed capture fix can be made nowhere else. The merge-back is the deliberate
single-threaded `D-038` act and carries `video/v09` with it, which `D-024` permits — 0 `CRITICAL`,
0 `MAJOR`. The recipe fix is committed **separately**, on the integration branch, after the merge.

`validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Review Trigger

**V09 R2**, on student resubmission with items **73–78** applied.

---

## 2026-08-13 — Integration (V09 R1 merge-back and the `SWF_CAPTURE_RECIPE.md` fix)

**Act:** the deliberate, single-threaded `D-038` merge-back, plus the one policy-ledger edit that
could not be made anywhere else. Performed by the V09 R1 reviewer, knowing it was the only merge
in flight.

### What was merged

| Step | Detail |
|---|---|
| Fetch and divergence check | Integration at **`4a291fe`**, level with `origin`. `review/v09` **14 ahead, 0 behind** — a clean fast-forward |
| Merge | `--no-ff`, so the deliberate act is visible in the graph rather than disappearing into a fast-forward. **`f7a72a2`** |
| What it carries | `18_REVIEW/V09/V09_REVIEW_R1.md` and this round's ledger rows — **and `video/v09` with them**, which `D-024` permits: `REVISE` with 0 `CRITICAL` and 0 `MAJOR` opens the gate with the minors deferred |
| Validator | **103 passed, 0 warnings, 0 failures**, before the push |

### The recipe fix — `89bb858`

`SWF_CAPTURE_RECIPE.md` is a **POLICY ledger** under `D-038a`. The V08 session hit the
play-coordinate defect, diagnosed it and could not fix it; the V09 session hit it again, escalated
it, and correctly declined to fix it from a task branch. **V09 R1 confirmed it, established the
cause, and made the fix here.**

**The cause is a declared header field, not a per-file oddity.** The stage rectangle of every
`.swf` in the library was parsed: **V08, V09 and V21 declare `1280 × 738`; the other eighteen
declare `1024 × 786`.** At the recipe's `1024 × 786` viewport Ruffle letterboxes the first class at
scale 0.8 — measurable in the committed frames as uniform bands at rows ~0–160 and ~685–785, absent
from V06/V07 frames — so every coordinate calibrated on the second class is displaced on the first.
`(512, 300)` misses; `(512, 325)` hits. On **both** V08 and V09.

**What changed:** §3 and §10 no longer carry `(512, 300)` as a constant; a new **`GOTCHA 5`**
records the failure history, the cause, a one-command stage-size probe (**tested as written, on
both classes**) and the coordinate table, with an explicit warning not to trust the table alone;
and §10's sweep now **screenshots before and 1.5 s after the play click and exits non-zero if they
are byte-identical**. That last part is V08's own remedy, promoted from one lesson's screenshot
index to the standard — it needs no table, and it converts a silent hour-long failure into an
immediate abort.

**`REVIEW_INDEX.md` open item 78's reviewer half is discharged by this commit.** Its student half —
correcting the *"the coordinate that starts the Camtasia player on V01–V08"* sentence in
`04_SCREENSHOTS/V09/INDEX.md` and `V09_MASTERY_REPORT.md` — **remains OPEN and owed at V09 R2**.

### Gate

**V10 OPENS** under `D-024`. `COURSE_PROGRESS.md`'s V10 GATE block still reads `CLOSED` — it was
written before this verdict returned and was correct when written; `REVIEW_INDEX.md` is the
authoritative register and it records the opening. Reconciling `COURSE_PROGRESS.md` is the V10
session's first bookkeeping act, exactly as V09's was.

---

## 2026-08-13 — Remediation Session (V09 R1 minors, items 73–78)

### Objective

Address the six required corrections in `18_REVIEW/V09/V09_REVIEW_R1.md` §15.

**Branch:** `fix/v09-r1-minors`, cut from the integration branch at `c8d4d80` after `git fetch`
confirmed no divergence (`D-038`, `fix/v08-r1-minors` precedent).

### ⚠ PROCESS DISCLOSURE FIRST — A `D-003` DEVIATION, AT OWNER DIRECTION

**This remediation was performed by the same session that wrote `V09_REVIEW_R1.md`, because the
owner instructed it directly.** The project's normal loop puts an independent session between
review and fix, and this file states the reason in its own words at the V07 R2 entry: *"a reviewer
that fixes what it finds has stopped being a reviewer."*

**What is done about it, rather than around it:**

1. **Nothing is closed.** `REVIEW_INDEX.md` items 73–78 read
   `APPLIED — PENDING VERIFICATION at R2`, exactly as the V07 and V08 minors remediations did.
   `D-003` reserves closure to an independent reviewer and this session closes nothing.
2. **V09 R2 must be an independent session**, and it should re-derive each of the six **from
   source** rather than from the remediation's own account of itself — which is precisely what the
   V08 R2 round did, and why it was able to confirm that the `[00:28:31]` garble had been
   preserved rather than smoothed.
3. The deviation is recorded here and in `V09_MASTERY_REPORT.md` Revision R1, not smoothed over.

### Findings Addressed

**All six are documentation fixes.** `REMEDIATION_PROTOCOL.md` §2's redo-do-not-reword rule was
checked against each and does **not** bite: no test was invalid, no sample cherry-picked, no
classification hindsight-dependent, no rule left unsourced. **`PT-035` was not re-run, and
`run_pt035.py` and the pre-registration are byte-unchanged** — `COMMON_PROTOCOL.md` §9 rule 7.

| Item | Class | What changed |
|---|---|---|
| **73** | `E01` | All four `AUDIO`-tagged quotations restored to the transcript's literal wording — *"high low-day"*, *"the grade Fred"*, *"experiences show me"*, the doubled *"it's it's"* — with the expansions moved **outside** the quote marks and a table naming each ASR artefact. The two `HOD/LOD` gate rows retagged as quoting the **printed** form, which is what they always were. **The transcript body is untouched.** Re-verified against the body: all four now match |
| **74** | `E20` | `BT_V09_0001` §1 and §5 now quote `PT-035` §6's decision table in full, report the **measured** arm as **`INDETERMINATE`** on the `N3` failure, and carry `CONTRADICTED AS STATED` on the **§2c/`O4` closed form alone**. `P3` re-scored *right on its measurement, void on its verdict clause*; the prediction tally moves 3/1/1 → 2/1/1/1. Propagated to the mastery report §G and to its self-assessment item 2 |
| **75** | `E19` | The COVERAGE block's 10-second gap count corrected **four → seven**, all seven markers listed |
| **76** | `E11` | **Structural, not arithmetic.** Every frame cross-reference in `V09_SOURCE_NOTES.md`, `04_SCREENSHOTS/V09/INDEX.md`, `A-065`, `A-067`, `C-013`, `C-015` and the mastery report now names the frame by its **burned-in player timecode**. Ordinals survive only inside `INDEX.md`'s own table, which nothing outside that file cites |
| **77** | `E02` | `V09_INTERPRETATION.md` Q5 downgraded **`MEDIUM` → `LOW`** with the set-level arithmetic written out; Q8's falsification row corrected; the same reasoning added to `C-010` and to `V09_SOURCE_NOTES.md` §9d. **`C-010` stays OPEN and its disposition is unchanged** |
| **78** | `E20` | The *"V01–V08"* claim corrected in both files, citing `04_SCREENSHOTS/V08/INDEX.md`'s record of the identical failure and the reviewer's stage-geometry cause. **The reviewer's half was already discharged at `89bb858`** (`SWF_CAPTURE_RECIPE.md` `GOTCHA 5`) |

### Work Redone (not edited)

**None, and that is the correct answer here.** No finding touched the validity of a test, a
sample, or a classification. `data/pt035_output.txt` and `pt035_results.json` are untouched and
still reproduce byte-identically.

### Verification performed by this session on its own fixes

- Item 73: re-matched all four corrected quotations against the marker-stripped transcript body —
  **4/4 exact**.
- Item 75: re-derived the gap distribution — **7 gaps of 10 s, 2 of 11 s, 721/718 markers, zero
  decreasing transitions** — unchanged from the review's measurement.
- Item 76: swept all five files for surviving bare frame ordinals in V09 regions — **none**,
  except `INDEX.md`'s own table and one correct in-table reference.
- `validate_project.py`: **103 passed, 0 warnings, 0 failures.**

**None of this is verification in the `D-003` sense.** It is a session checking its own work, and
it is recorded as that.

### Decision

```text
V09:  REVISE (R1) -> REMEDIATION APPLIED -> AWAITING R2
      Items 73-78 APPLIED, PENDING VERIFICATION. NOT CLOSED.
      Items 79 and 80 are unaffected: 79 is recommended-not-owed, and
      80 is an escalation for a scoped investigation, not a defect.
      V10 gate remains OPEN under D-024 -- this remediation neither
      opens nor closes it.
```

### Git

`COURSE_PROGRESS.md` reconciled in the same round: `VIDEOS IN PROGRESS` 3 → **1**, `VIDEOS PASSED`
6 → **8** (V07 and V08 had reached `COMPLETE` at R3 and R2 and the block had not been updated —
the status-staleness class, open item 14), `NEXT LESSON` and the `V10 GATE` block moved to
**OPEN**, and `GOTCHA 5`'s stage-size requirement added as a V10 carry-forward. Superseded text
retained at both sites.

### Next Review Trigger

**V09 R2** — verification of items 73–78 by an **independent** session.


---

## 2026-08-13 — Reviewer Session (V09 R2 — INDEPENDENT VERIFICATION)

### Objective

Verify the R1 remediation of `18_REVIEW/V09/V09_REVIEW_R1.md` items **73–78**, applied at
`16c43ea` (`fix/v09-r1-minors`) and `89bb858` (`SWF_CAPTURE_RECIPE.md`).

**Why this round exists and why it could not be skipped.** The R1 remediation was performed by the
**same session that wrote R1**, on the owner's explicit direction — a `D-003` deviation. **The
authorization covered the fix-it-yourself step, not a waiver of independent verification.** That
session correctly closed nothing, leaving all six items at `APPLIED — PENDING VERIFICATION at R2`.
This session authored no V09 artifact, did not write R1, and did not perform the remediation.

### Method — primary sources first, the remediation's account of itself last

**Every one of the six original findings was re-derived from source BEFORE any fix was read.**
Nothing was taken from `LOG.md`, from the commit messages, or from the mastery report's revision
block.

- The transcript was read at all four `M1` markers. **All four misquotes were real**, exactly as R1
  transcribed them.
- A gap scanner was written from scratch: **721 markers, 718 distinct, zero decreasing transitions,
  11 s twice, 10 s SEVEN times** at exactly the seven markers R1 listed. The original *"four"* was
  wrong.
- The 27-frame listing was mapped against every ordinal R1 named. **The off-by-one is real**;
  position 15 is the inserted `V09_00-15-00_…png`.
- `PT-035` §6 was read **in the pre-registration blob**, not in the observation's quotation of it.
  The `INDETERMINATE`-on-`N3`-failure row is there verbatim and was live and unapplied.
- The binomial was **re-derived in this session's own run-length DP**: 99.93% at p=0.50, 54.13% at
  p=0.73, 100.00% at p=1/3, threshold 84.19%. `CONTRADICTED AS STATED` genuinely needs no
  measurement.
- `MMM-NOTES` was read **at source**: four averages enumerated (*"the 5, 13, 50 and 200"*), and
  **`800` occurs zero times in 84 pages**. `A-020` attests Mayo = 200 and Blueberry = 800 as two
  lines, so the identity does collide with it.
- The **SWF `RECT` was parsed from every file**. Of the 21 canonical `Bootcamp/` files **exactly
  three** declare 1280×738 — V08, V09, V21 — as R1 and the recipe state.
- `GOTCHA 5`'s probe script was **run verbatim on one file of each class** and works on both.
- One load-bearing frame was **opened as an image**: burned timecode matches filename, error 2 is
  where `A-065` says it is, letterbox bands visible.

### Findings — items 73–78 ALL CLOSED — VERIFIED

**Every original finding was real. Every fix was correct. The superseded-text convention was
followed at every site checked.**

| Item | Verdict |
|---|---|
| **73** `E01` | **CLOSED — VERIFIED.** All four sites repaired, two by the stronger `PRINTED`-retag route. **Transcript body byte-identical by hash.** ⚠ The item's other required action — the mechanized sweep — was not performed: **new item 81** |
| **74** `E20` | **CLOSED — VERIFIED.** Clause quoted in full, measured arm reported `INDETERMINATE`, verdict carried on §2c/`O4` alone, `P3` re-scored and the tally moved with both prior values retained, propagated to all three files R1 named |
| **75** `E19` | **CLOSED — VERIFIED.** Corrected to seven, all listed, superseded text retained, body untouched and proven so |
| **76** `E11` | **CLOSED — VERIFIED.** Took the **preferred structural route** — burned timecodes. Zero bare ordinals in any V09-scoped file. ⚠ Two survive in the shared register at sites R1 mis-attributed: **new item 82** |
| **77** `E02` | **CLOSED — VERIFIED.** `MEDIUM`→`LOW`, arithmetic written out, Q8 corrected, `C-010` annotated and still **OPEN**. ⚠ The escalation it retires was not marked retired: **new item 83** |
| **78** `E20` | **CLOSED — VERIFIED, BOTH HALVES**, and they are mutually consistent |

**`PT-035` and `run_pt035.py` are BYTE-UNCHANGED from pre-registration** — verified by **blob SHA and
single-commit history**, a stronger check than a diff: `c274088836a0…` at `0f709d2` and at `HEAD`;
`9215e3ac79e5…` at `7c3fe2d` and at `HEAD`. Both re-executed; `pt035_output.txt` and
`pt035_results.json` reproduce **byte-identically**.

**Item 78's split disposition holds up.** The reviewer's policy-ledger edit is in scope under
`D-038a`, confined to one file, correctly hedged (*"do not trust the table alone"*), and makes the
**table-free** before/after guard the standard rather than publishing a coordinate table as
authority. The student half cites it accurately. No live *"V01–V08"* claim remains anywhere — the
surviving occurrences are all inside retained superseded blocks.

**Items 79 and 80 are accurately characterised as non-blocking.** Read, confirmed, not resolved.
Neither is V09 debt.

### New Findings — 3 MINOR

- **81** `E01` — item 73's required mechanized sweep was never run (`verify_quotes.py` still
  V07-specific, one commit, untouched since V07 R2/R3), and a **fifth instance survives** at
  `V09_SOURCE_NOTES.md`:410 — *"experience shows me"* for *"experiences show me"*, **38 lines from
  the corrected block that states the transcript reads the latter.** The file contradicts itself
  about its own source.
- **82** `E11` — `A-069` and `A-073` still carry *"frames 22, 23 and 25"* in the **shared** register.
  Under the current numbering those point at a **spreadsheet** and an **MS Paint email**, neither a
  chart. The miss originates in R1's enumeration, not the remediation's execution; charged anyway
  because the register outlives the lesson.
- **83** `E19` — mastery report escalation 5 still asks the owner to rule on `C-010`'s closure after
  item 77 retired the question, while escalation 2 one row away was given a `DISCHARGED` marker in
  the same remediation.

### Retesting

Nothing was owed a redo: all six items are documentation defects and **no underlying test was
invalid**, so `REMEDIATION_PROTOCOL.md` §2's redo rule was correctly not triggered. Re-run anyway
for regression: `run_pt035.py` and all three V09 homework scripts — **all byte-identical, tree
clean**. Marker citation integrity re-checked across the six V09 artifacts: **208 distinct
citations, ZERO orphans**. `REMEDIATION_PROTOCOL.md` §6 forbidden acts: **none committed** — no
review file edited since it was written, `LOG.md` gained 88 lines and deleted zero, no history
rewritten.

### Decision

```text
V09 R2:  REVISE, HIGH confidence
         CRITICAL 0   MAJOR 0   MINOR 3  (new items 81-83)

         R1 items 73-78: ALL SIX CLOSED — VERIFIED.
         The D-003 deviation is DISCHARGED: the remediating session
         closed nothing, and this independent round supplied the
         verification the owner's authorization did not waive.

         V09 does NOT reach COMPLETE. R3 required.
         V10 gate REMAINS OPEN under D-024 -- nothing here gates.
```

**Why `REVISE` and not `PASS`, stated so it can be argued with.** This was close. The remediation
did what it was asked, on all six items, correctly, and twice chose the stronger of two offered
remedies. Nothing it did is wrong. It is not a `PASS` because **two of the three new findings are
live wrong pointers**, one of them the very defect the round was convened to remove, surviving in a
register that outlives V09. `REVIEW_PROTOCOL.md` §9 condition 2 is breached the same way `M4`
breached it. Condition 14 is comfortably met — nothing corrupts downstream learning — which is why
the gate stays open.

**Recorded in the remediating session's favour.** Item 74 required it to report its own headline arm
as `INDETERMINATE`, re-score its own prediction downward and move its own tally from `3/1/1` to
`2/1/1/1`. It did all of it, and wrote *"item 74 is the finding this session should have made
against itself and did not"* — while holding the pen on both the review and the fix, with nobody yet
checking. **That is what the separation-of-duties rule exists to guarantee when it cannot be
guaranteed structurally.**

### Files Created/Updated

- **Created:** `18_REVIEW/V09/V09_REVIEW_R2.md`
- **Updated:** `18_REVIEW/REVIEW_INDEX.md` — items 73–78 → `CLOSED — VERIFIED at R2`, new items
  **81–83**, V09 R2 decision row, `IN REMEDIATION` status block (superseded text retained)
- **Updated:** `LOG.md` — this entry

### Git

Branch **`review/v09-r2`**, cut from the integration branch at `5db04d8`. `fix/v09-r1-minors`,
`review/v09` and `video/v09` were **all already merged** into integration and `origin` was in sync
(0/0 divergence), verified with `merge-base --is-ancestor` before any read — so unlike R1 this round
needed no merge of integration into the task branch.

**THE MERGE-BACK IS NOT PERFORMED.** The standing `D-038` instruction conditions the deliberate
merge-back on a clean verdict, and **this verdict is not clean.** The branch is pushed and left
unmerged. Recorded as a decision, not an omission.

`validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Action

**V09 R3** — on resubmission with items 81–83 applied.

---

## 2026-08-13 — V09 R2 REMEDIATION: items 81–83 APPLIED and ⚠ SELF-VERIFIED AT OWNER DIRECTION

> ## ⚠⚠ PROCESS DISCLOSURE — READ BEFORE THE REST OF THIS ENTRY ⚠⚠
>
> **This round was fixed AND verified by ONE session. It is `SELF-VERIFIED AT OWNER DIRECTION,
> NOT independently verified per the standard `D-003` process.**
>
> The owner explicitly authorised combining the fix and the verification **for this round
> specifically**, on the grounds that the three items are small. That authorisation is real, it is
> recorded, and it was followed. **It does not manufacture independence.** Items 81–83 are closed
> as **`CLOSED — SELF-VERIFIED AT OWNER DIRECTION`** — a status string that exists for no purpose
> other than being visibly unlike `CLOSED — VERIFIED` — and V09's `COMPLETE` carries the same
> qualification in `REVIEW_INDEX.md`, in the decision table, and in `V09_MASTERY_REPORT.md`
> Revision R2.
>
> **The precedent, and the difference from it.** V09's own R1 remediation used the same
> owner-authorised pattern. But R1 authorised the **fix** only, and that session **closed
> nothing** — `REVIEW_INDEX.md` read `APPLIED — PENDING VERIFICATION at R2`, and R2 supplied the
> verification the authorisation had not waived. **This round closes its own items.** That is the
> stronger deviation of the two, and pretending otherwise would be the failure this project
> exists to avoid.
>
> **The honest statement of what is and is not established.** What is established: the three
> findings were real, they are fixed, sixteen more defects of the same class were found and fixed,
> and the fixes were re-derived from primary sources — the transcript, the PNGs, `MMM-NOTES` —
> rather than from any document's account of them. What is **not** established: that a session
> with no stake in the answer would reach the same verdict. Nothing here substitutes for that.

### What the review charged, and what was done

`18_REVIEW/V09/V09_REVIEW_R2.md` closed R1's items 73–78 as `VERIFIED` and opened three new
`MINOR`s. All three are documentation fixes; `REMEDIATION_PROTOCOL.md` §2's redo-do-not-reword rule
was checked against each and does not bite — no test was invalid, no sample cherry-picked, no
classification hindsight-dependent, no rule stripped of provenance.

| Item | Charge | Disposition |
|---|---|---|
| **81** `E01` | The mechanized sweep item 73 required was never run; a **fifth** instance survived 38 lines from the corrected one | **Both halves discharged.** `verify_quotes.py` generalised **and** run. **19 genuine defects found and fixed** against the one the review named |
| **82** `E11` | `A-069`/`A-073` still carried *"frames 22, 23 and 25"*, pointing at a spreadsheet and an email | Converted to burned timecodes `28:45`/`31:50`/`41:25`. Verified **by opening all five images** |
| **83** `E19` | Escalation 5 still put the owner a question item 77 had retired | Marked ✅ **RETIRED**, in escalation 2's form, with the arithmetic that retires it restated |

### Item 81 is the substance of the round, and it got worse the harder it was looked at

`V09_REVIEW_R1.md` `M1` required two things: **generalise** `verify_quotes.py` and **run** it. The
R1 remediation did neither, and hand-fixed the four sites it was pointed at. `V09_REVIEW_R2.md`
charged that *"hand-fixing an enumerated list leaves the un-enumerated ones."*

**That charge was demonstrated three times over.**

1. **The fifth instance, which the review named.** `V09_SOURCE_NOTES.md` line 410 read *"experience
   shows me"*; `[00:44:39]` reads *"experiences show me"*. The same file had corrected the same
   phrase 38 lines above, at R1.
2. **A sixth, which nobody found.** `04_SCREENSHOTS/V09/INDEX.md` row 26 quoted the audience as
   *"What is the grape?"*, cited to `[00:41:25]`, where the transcript reads *"What is the **grade**
   Fred?"*. `V09_SOURCE_NOTES.md` §9a had corrected its own copy of that exact quotation at R1. **The
   twin in a different file survived both review rounds. The sweep found it in one run.**
3. **A seventh — and five more beside it — in a file the sweep could not see.** The seven V09
   artifacts the review named do **not** include the shared registers.
   `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` `A-072` was carrying a **third** live copy of
   *"experience shows me"*, with `A-066`, `A-071`, `A-073` and `A-075` carrying five more misquotes
   beside it. **The script was extended** to scan `10_AMBIGUITIES/` and `11_CONTRADICTIONS/` for
   every lesson, restricted to table rows whose first cell names that lesson — the register's own
   declaration of which transcript a row asserts, which is what makes the check sound on a
   cross-lesson file.

**This third one is item 82's argument in the quotation class rather than the pointer class: a
defect in a shared register outlives the lesson that put it there.** The register was carrying
**both** kinds of debt simultaneously, which is the strongest available evidence for R2's point.

The remaining eleven were the same class in milder forms — *"2%"* for the spoken *"two percent"*,
*"brings"* for *"will bring"*, *"forex"* for the ASR's *"4x"*, *"DMR"* for *"dmor"*, *"USD JPY"* for
*"USD JP why"*, a Claim row that blended audio and slide into a quotation verbatim in neither, and
four unmarked elisions joining non-adjacent markers with a comma or a full stop. **None moves a
conclusion. All nineteen are now either literal or explicitly elided, with superseded text retained
at every site.**

### The script, and what was done to it beyond generalising

`ARTIFACTS` and `ALLOWLIST` are now per-lesson dicts keyed by lesson id; the transcript path is
derived; usage is `verify_quotes.py {V07|V09}`. **`V07_REVIEW_R3.md` §4 listed three precision
fixes to apply "when the file is next touched". This was that touch. Two are adopted; one is
refused, with reasons:**

- **ADOPTED** — allowlist matching anchored to the **full** normalised fragment instead of a
  prefix, closing the hole R3 found by mutation testing. Three V07 fragments the prefix rule had
  been excusing silently now carry their own written reasons; six that were being excused for no
  reason at all now fall through to `uncited, unrelated`, where they belong.
- **ADOPTED** — the docstring claim that prefix matching *could not* excuse a longer differently
  worded quotation, which was false, is corrected.
- **REFUSED** — ordering `in_blockquote()` after the cited-FLAG test. `REMEDIATION_PROTOCOL.md` §2
  retention blocks re-quote the defective rendering **on a `>` line** and carry its marker, so the
  reorder would FLAG every correctly-retained superseded quotation, of which this round alone
  creates several. **R3's actual concern was masking, not ordering**, and it is addressed instead
  by having every `RETAINED` fragment report its near-miss run against the transcript — the hand
  check R3 performed, mechanised, without mechanising a wrong verdict.

**The file stays at `05_HOMEWORK/V07/scripts/` deliberately**, though it is no longer V07-specific.
Six committed documents already cited it there and three are review files `REMEDIATION_PROTOCOL.md`
§6 forbids editing; moving it would create exactly the dangling-pointer defect item 82 charges. The
path is historical rather than descriptive and the docstring says so. **A later round willing to
accept the stale citations may move it to `scripts/`.**

### What the self-verification pass actually did — and what it caught against itself

This is the part that carries whatever weight this round has, so it is stated in detail.

| Check | Method | Result |
|---|---|---|
| Every cited marker | A parser written for this pass, **not** `verify_quotes.py`'s, dumping marker → text | **Two of this session's own edits were WRONG.** §6's Claim row was cited `[00:24:52]`–`[00:24:55]`; **`[00:24:55]` does not exist**. And the superseded block claimed *"for the week"* was imported from the slide — **the audio says it, at `[00:24:59]`**. The real defect was one dropped word, *"it"*. Q6's block likewise cited one marker for a two-marker sentence and called a two-word elision three. **Both corrected in place and reported** |
| Item 82's three frames | **Opened all five PNGs as images** | `28:45` = `EURUSD,H1`, hand-drawn levels, level count 1/2/3, **`Reset` printed twice**, DayHi/DayLo tracer lines. `31:50` = `GBPJPY,H1`, `Reset`, numbered levels. `41:25` = nine tiles, `Reset` on `EU` and `GU`. **All three are charts and fit both records.** `26:40` = the compounding spreadsheet, `34:35` = the MS Paint email — **confirmed not charts**, which is what made the stale ordinals harmful |
| Item 83's premise | `MMM-NOTES` **at source**, not item 77's account of it | p.38: *"The specific EMA's used in Mauro's charts are the **5, 13, 50 and 200** bar EMA's"* — four. **`800` occurs ZERO times in the extract.** p.66: *"Hold the Mayo – 200 Bounce"*, independently corroborating `A-020`'s Mayo = 200. **The premise is false on any owner ruling** |
| The script | **Mutation-tested three ways** | Reintroduce item 81's defect at line 410 → **FLAG, exit 1**. Reintroduce the *grape* instance → **FLAG, exit 1**. Append words to an allowlisted fragment (*"7 Wins, 6 Losses, and a partridge in a pear tree"*) → **FLAG**, which proves the prefix hole is genuinely closed |
| Live defects anywhere | grep for the phrase outside retention blocks | **Found the seventh instance**, in the shared register, and led to the six-defect find and the script extension |
| Final sweep | Both lessons | **V09 → 315 fragments, 0 FLAGGED. V07 → 353 fragments, 0 FLAGGED** — the register extension adds V07 rows and finds **no** V07 debt |
| Validator | `python3 scripts/validate_project.py` | **103 passed, 0 warnings, 0 failures** |

**The two own-errors are the point of reporting this table.** A self-verification pass that returns
"all clear" is worth nothing. This one found six defects the fix pass had missed and two mistakes of
its own, including a citation to a marker that does not exist. That is offered as evidence the pass
did work — **not** as a substitute for independence.

### One defect found and deliberately NOT fixed

`PT-035` §Source quotes `[00:06:08]` as *"…risk management. **However** I believe that with our
training…"*. **The transcript reads *"…risk management. **How are** I believe that with our
training?"*** — an ASR garble smoothed inside quotation marks, the same `E01` class as item 81.

**It is not fixed and it must not be.** `COMMON_PROTOCOL.md` §9 rule 7 forbids editing a
pre-registration after the fact, and `V09_REVIEW_R2.md` verified `PT-035` byte-identical to its
pre-registration blob by SHA. **Editing it to fix a typo would destroy a stronger guarantee than the
typo violates.** Recorded in `V09_MASTERY_REPORT.md` Revision R2, in `REVIEW_INDEX.md` item 81 and
in the script's own allowlist so that a later round rules on it deliberately rather than
rediscovering it. **Nothing turns on it** — *How are* is transparently *However*, and the
load-bearing clause of the quotation is verbatim.

### What did NOT change

- **No conclusion of the lesson moves.** No marker, status, disposition, `DO NOT CODE` verdict,
  grade, evidence count or Tier 2 negative changes anywhere.
- **`C-010` stays `UNRESOLVED`.** Item 83 retires a *question about* `C-010`, not `C-010`.
- **The transcript body is untouched**, as at R1.
- **`PT-035`, `run_pt035.py` and `data/pt035_output.txt` are untouched.** No test was re-run.
- **No review file was edited**, no history rewritten, no retention block deleted, no test ID
  renumbered.

### Files Created/Updated

- **Updated:** `05_HOMEWORK/V07/scripts/verify_quotes.py` — generalised, extended to the shared
  registers, two of V07 R3's three precision fixes adopted and the third refused with reasons
- **Updated:** `03_LESSON_NOTES/V09_SOURCE_NOTES.md` §2c, §5, §6, §8, §11 — nine quotation fixes
- **Updated:** `03_LESSON_NOTES/V09_INTERPRETATION.md` Q6 — heading elision
- **Updated:** `05_HOMEWORK/V09/V09_HOMEWORK.md` — H1/H2 elisions
- **Updated:** `04_SCREENSHOTS/V09/INDEX.md` row 26 — the sixth `E01` instance
- **Updated:** `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` — items 82 (`A-069`, `A-073`) **and** 81
  (`A-066`, `A-071`, `A-072`, `A-073`, `A-075`), plus a register-level correction block
- **Updated:** `07_MASTERY_REPORTS/V09_MASTERY_REPORT.md` — escalation 5 retired; **Revision R2**
  appended, led by the `D-003` disclosure
- **Updated:** `18_REVIEW/REVIEW_INDEX.md` — items 81–83 → `CLOSED — SELF-VERIFIED AT OWNER
  DIRECTION`, V09 → `COMPLETE` with the qualification stated in three places, status block and
  decision table updated (superseded text retained)
- **Updated:** `LOG.md` — this entry

### Git

Branch **`fix/v09-r2-minors`**, cut from `review/v09-r2` at `dc427dc` after `git fetch --all`
confirmed zero divergence from `origin` (`D-038`). Four commits, every one carrying the `D-003`
disclosure in its message. Paths staged explicitly; `git diff --staged` read before each commit;
`git add -A` never used.

**THE `D-038` MERGE-BACK IS PERFORMED THIS ROUND**, because this session's own verdict is what
closes the round — there is no later session to hand it to. `review/v09-r2` and `fix/v09-r2-minors`
both go to integration. **That is itself part of the deviation and is recorded as such**, not
presented as routine.

`validate_project.py`: **103 passed, 0 warnings, 0 failures.**
`verify_quotes.py V09`: **PASS, 0 flags.** `verify_quotes.py V07`: **PASS, 0 flags.**

### Next Action

**V10** — the gate has been open under `D-024` since V09 R1 and nothing here closes it. **A later
session that wants V09 verified at arm's length has a short, specific list to re-derive; it is in
`REVIEW_INDEX.md`'s V09 status block.**

---

## 2026-08-13 — Student Session — V10

### Lesson

**V10** — `Bootcamp1 Wk3 040112 (96mins).swf`,
SHA-256 `a37ba371ca2d5c807553c7b9a827a91c479509dd5223b64eadf85995481a3de1`, 01:36:16.
**Printed banner** `Market Makers Boot Camp` / `Week 3` — the first title card since V08 — but
**no topic title is asserted**. Session date **2012-04-01**, from the filename **and stated in the
recording** at `[00:21:25]`.

**Branch `video/v10`, in a dedicated worktree (`D-038`). No `I-009` collision.**
Evidence ledgers written on the task branch, as `D-038a` expects.

### Gate

**Verified OPEN in `18_REVIEW/REVIEW_INDEX.md` before any V10 artifact was created** — V09 R1
returned `REVISE` 0 CRITICAL / 0 MAJOR / 6 MINOR, which opens the gate under `D-024`.
`COURSE_PROGRESS.md`'s V10 GATE block **already read OPEN** (reconciled by the V09 remediation
session), so unlike V09 there was no staleness to fix.

### ⭐ The five-lesson guest run ENDS. V10 is 100% course author.

V05–V09 each carried **zero** author runtime. The V10 GATE carry-forward (a) called a new week and
a new date *"a REASON TO EXPECT A CHANGE, not a reason to assume one"* and required it be **tested**.

**Tested, on five non-acoustic strands fixed before the answer was known:** the speaker claims
Steve's mailbox in the first person (`[00:07:12]`, printed `steve@marketmakersforex.com`); **all 13
`Steve` tokens are vocative or self-quoting** — he voices students addressing him and answers in the
first person, where V04–V09's guests referred to Steve in the **third person as an absent
authority**; he reads mail whose slide prints *"Hello Steve"*; he claims authorship of the method,
the course and the slides; and he owns the homework loop. **A scan for handover language returns zero
matches in 96 minutes.** The cross-file acoustic screen was **NOT** run, as V07's carry-forward
prohibits.

### What V10 contributes

**THE SAFETY TRADE** — the author's officially designated *"signature trade"*. Nine rules **printed
on two consecutive slides** and narrated, plus target (*"plus 50"*), anchor distance (**25–75 pips**,
printed), anticipation lead (12–24 h) and frequency (2 per pair per week).

**And the first operational definition of `peak formation` in ten lessons.** `[01:14:06]`:
*"the highest point on a chart within the week, or the lowest point on the chart within the week."*
**`A-010` NARROWS on Tier 1 evidence alone** (`SOURCING_HIERARCHY.md` §3.2 case A) — **not blended**
with `MMM-NOTES`. It is positional and needs no pattern recognition at all.

**What V10 does NOT supply, recorded because absence is evidence:** **no stop loss anywhere** —
`stop loss` occurs **zero** times; no session clock time; no ADR lookback; no EMA nickname mapping
despite using two nicknames.

### Artifacts

| Artifact | Note |
|---|---|
| `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` | 1,184 markers, **strictly increasing** (zero decreasing, zero same-second — measured, not asserted), verified on four axes |
| `04_SCREENSHOTS/V10/` | **32 frames + INDEX.md.** 32/32 burned timecodes read from a verification strip, all ≤ runtime |
| `03_LESSON_NOTES/V10_SOURCE_NOTES.md`, `V10_INTERPRETATION.md` | Basis tags on every substantive row; every §6 rule is `AUDIO` or `AUDIO+PRINTED` |
| `05_HOMEWORK/V10/` | H1 flashcards, H2 anchors + cross-check, 12/12 comprehension, 2 scripts, 2 data files |
| `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-036…`, `06_MANUAL_BACKTEST/V10/BT_V10_0001.md` | Pre-registration `f58dce7`, runner `e53409e`, both before execution |
| `07_MASTERY_REPORTS/V10_MASTERY_REPORT.md` | `REVIEW REQUIRED` |
| Registers | **`A-076`–`A-079`** (4) + **`A-010` NARROWED**, **`C-016`–`C-017`** (2), **`Q-011`** |

### The backtest — both claims contradicted, and the null did more damage than the magnitude

`PT-036` / `BT_V10_0001`.

**`M1` — weekly range 600–1000 pips: 0 of 180 weeks.** Median 243.8; 600 sits at the **99.44th
percentile**; the claim overshoots by **3.28×**. **The pip-vs-point rescue fails too** — 600 "points"
on a 5-digit feed is 60 pips, and only 4/180 weeks fall in [60,100]. **There is no unit reading on
which the number describes GBP/USD here.** The one week above 600 is the EU referendum at 1789.5 —
**1.8× the band's ceiling**. `N4`: a roster shifted +24 h is **indistinguishable** (medians 243.8 vs
244.1), so `M1` measures five days of travel, not week structure.

**`M2` — Friday close 25–50 off both extremes: 7.30% (A) / 5.62% (B)** against the word *"always"*.
**The `N2` matched uniform-close null — computed per-Friday from that Friday's own range — expects
7.12%.** Observed − null = **+0.19 pp**; on Arm B observed sits **below** the null. **`M2a` carries
essentially no information beyond range width.** And `N3`: **Friday ranks fourth of five weekdays**;
Thursday satisfies the band nearly twice as often. The claim's mechanism is weekend-specific by its
own terms, and **there is no Friday effect at all.**

**The safety trade was NOT tested, and not testing it is reported as a finding** with the hazard
named: its anchor is **retrospective**, so a naive test would use the actual weekly extreme and
commit **lookahead** (`E08`) while producing a flattering number. Five of seven conditions are
`D-030`-blocked.

**Open item 80's censoring bias was designed out AND verified** — `censored = 0` on both arms,
enforced as a hard assert that would have **voided** both measures.

**Predictions 6/6, and the record argues that down**: P1/P2 are one finding, P3/P4/P5 are one
finding, only P6 was independent. **Honest count ≈ two independent forecasts plus one
low-confidence call.** P7 was flagged structurally cheap before the run and is tallied separately.

### Homework

H1 done. **H2 is the honest one:** the assignment is *"Mark 10 Safety setups, 5 long 5 short"*, and
five of the setup's seven conditions are undefined, so the **setup half is `DEFERRED` under `D-019`
— not `NOT APPLICABLE`**, because it plainly has subject matter. The **anchor half was performed**:
ten weekly anchors on real GBP/USD, selected by a **fixed index rule stated before any price was
read**. H3 `NOT APPLICABLE` (`D-018`) — a 2012 forum.

**Independent cross-check:** every anchor computed twice by paths sharing no code (raw M1 vs
committed M15 aggregation), 10/10 exact on price and timestamp, gated by a non-zero exit — **and the
write-up states what it is worth**: an M15 high *is* the max of its M1 constituents, so it
corroborates the **aggregation**, not the market.

**Comprehension 12/12 on 44 mechanical assertions**, answers committed at `54b97f2` before the
scorer existed — **and `V10_HOMEWORK.md` §4 argues against crediting it**, in three specific ways,
pointing the reviewer at `Q-011`, `C-016`/`C-017` and `BT_V10_0001` §1 instead.

### `Q-011` — the fabrication finding gets stronger

**`RULES.md` is not merely "templated": by exact `diff`, V10's is V01's file with SIX identifier
strings swapped** — every rule, timestamp and parameter byte-identical to the copy `D-017` already
disproved. **Six cited markers, six misses, zero partial hits.** `NOTES.md`'s headline framing
(multi-timeframe analysis) is **contradicted in terms** by the lesson at `[01:13:47]`, not merely
unsupported — the first of that kind. And the **second confirmed instance of `Q-010`'s sixth failure
mode**: the one real image is a **genuine V10 frame — the title card** — carrying an entirely
invented description of an "Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs".

**Two self-corrections recorded rather than deleted:** an early `EMA` count of 24 that was `email`
substring matches (true count **2**), and this session's stricter hash normaliser calling `RULES.md`
unique where `diff` calls it V01's — **`Q-010`'s instrument was the better one.**

### Three corrections the screenshot pass made to this session's own audio-only conclusions

`SWF_CAPTURE_RECIPE.md` §9 keeps the passes separate so this can happen, and on V10 it did, twice
against the session:

1. **The lesson HAS a formal close** — printed on the end card, **never spoken**: *"Thank you all
   GOOD NIGHT"*. This session had written from audio alone that it ends without a sign-off. Same
   shape as V01's *"pendings"*.
2. **The email-address note had its confidence exactly BACKWARDS.** The slide reads
   `steve@marketmakersforex.com`, so the ASR's `marketmakers4x.com` is the *mis*-rendering.
3. **The anchor distance was settled** — printed `25 to 75 pips off of the LOW/HOW anchor` — against
   six spoken renderings in four forms.

All three are corrected **in place with the superseded text retained**.

### Contradictions, and two refusals

**`C-016`** — the directional lock is *"one-day"* and *"good for three days"* **two seconds apart**,
with *"at least two days"* twice more. It matters because **the safety trade has no stop**: its only
non-target exit is time. **`C-017`** — the anchor distance is measured from the **LOW/HOW anchor in
print** and from the **blue tracer in speech** (4 of 6 spoken instances). **The corpus's first
printed-vs-spoken conflict.**

**A tidy reconciliation was available for both and both are refused in writing**, per the `C-010`
precedent. For `C-017` the refusal is argued: `D-008` would settle it by source class and is **not
applied**, because `D-008` ranks *capture reliability* — it was written to stop an agent's reading
outranking the course, not to adjudicate between two things one speaker said in one hour.

### Citation discipline

**408 marker citations across six files, ZERO orphans** (one labelled V09 cross-reference). A first
sweep caught **18 off-by-a-few-seconds citations**, all corrected. **134 quotations checked; 127
resolve verbatim in audio**, and the 7 that do not are 5 `PRINTED`-tagged slide texts, 1 project
label, and 1 that is the **documented ASR garble** at `[00:15:12]` — all self-consistent.

### ⚠ Process disclosures

1. **`SWF_CAPTURE_RECIPE.md` §10's frame rate is not a constant.** §10 states the patch as
   `3.0 → 30.0` fps from V01/V02. **V10 declares 2.0.** Applied literally it sweeps at **15×, not
   10×**, and **fails silently** — well-formed, correctly-timecoded frames at 7.5-second spacing,
   under-sampling the screen detector by a third. Same family as `GOTCHA 4`/`GOTCHA 5`: a varying
   header field quoted as a constant. **POLICY ledger under `D-038a` — escalated, NOT patched from
   this branch.** This session avoided it by reading the header first, as `GOTCHA 5` teaches.
2. **`D-022` fired for real, for the third lesson running.** The first candidate port was **BUSY**,
   held by another session's `http.server`. A fresh port was bound and confirmed by `lsof` to be
   this session's own PID, and the served bytes were hashed against disk.
3. **The runner crashed on first execution and produced no result** (`BT_V10_0001` §8) — an
   off-by-one session-day label emptied the Friday set. Fixed before any number existed; **nothing
   in `PT-036` changed.** Argued to be outside `COMMON_PROTOCOL.md` §9 rule 7, which governs
   disagreements found *after* a result exists.
4. **Evidence ordering met in substance, not perfectly.** The full transcript was read and the notes'
   understanding formed before any frame was curated, but two image categories were opened earlier
   because the protocol requires it (the quarantined image for `Q-011`; the `GOTCHA 4` sanity
   frame). **Neither contributed a rule**, and basis tags let a reviewer verify that.

### Escalations

1. **Dimension B `D-030`-blocked for the SIXTH consecutive lesson** — open item **36** needs an
   **owner** ruling.
2. **`SWF_CAPTURE_RECIPE.md` §10's frame rate** — policy edit, integration branch.
3. **`A-077` (the lock) is now the highest-value gap in the project** — the only thing between V10's
   defined anchor and a prospectively identifiable setup.
4. **`A-004` after ten lessons — and V10 shows the course ROUTING AROUND it** (`[01:16:36]`). This
   may be a term the course never defines.
5. **`C-017` is the first printed-vs-spoken conflict and the project has no standing rule for that
   class.**
6. **Two `PT` successors specified and not run** — `PT-037` (the path-length reading of `M1`, which
   **must be pre-registered before measuring**) and `PT-038` (the safety trade, `D-030`-blocked).

### Git

Commits on `video/v10`, all with explicit paths (`git add -A` never used):

```text
2591720  transcript(V10) + Q-011 — four-axis verification; the guest run ENDS
4c58436  screenshots(V10) — 32 curated frames, 32/32 burned timecodes verified
cc45fce  notes(V10) — the safety trade; A-010 NARROWED; A-076..A-079, C-016, C-017
f58dce7  pre-register(PT-036) — before the runner existed and before any bar was read
e53409e  runner(PT-036) — before execution
2856631  backtest(BT_V10_0001) — BOTH claims CONTRADICTED AS STATED
54b97f2  homework(V10) — 12 comprehension answers, before the scorer
d27c67f  homework(V10) — H1, H2 anchors + cross-check, comprehension 12/12
```

### Decision

**STUDENT STATUS: `REVIEW REQUIRED`** — a submission, not an authorization (`D-016`/`I-001`).

### Next Review Trigger

**Independent review R1 of V10** (`D-003`). This session did not review itself and **did not merge
to integration** — merge-back is a separate single-threaded act under `D-038`.

---

## 2026-08-13 — Reviewer Session

### Lesson

**V10** · `Bootcamp1 Wk3 040112 (96mins).swf` · session 2012-04-01 · 01:36:16

### Review Objective

Independent mastery audit, round **R1**. Fresh session under `D-003` — this session
authored no V10 artifact. Branch `review/v10`, cut from `video/v10` @ `e5262b2` per `D-038`
and the V07/V08/V09 precedent.

### Source Evidence Reviewed — FIRST, before any student conclusion

- `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` **verbatim body, all 3,557 lines**, read in full.
- **Four frames opened and read as images**: `43:17` and `46:17` (the two safety-trade rules
  slides), `75:57` (the 25–75 pip slide), `96:16` (the printed-and-never-spoken end card).
- All 21 quarantined `RULES.md` files, `diff`ed pairwise.
- `GBPUSD_M15_ARM{A,B}.csv` — 86,536 / 86,532 M15 bars in `W-C′`.
- `02_TRANSCRIPTS/V01`–`V09` — `peak formation` census.
- `00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10.

### Student Artifacts Reviewed

Transcript header, both lesson-notes files, `04_SCREENSHOTS/V10/INDEX.md`, all of
`05_HOMEWORK/V10/`, `PT-036`, `BT_V10_0001`, `pt036_output.txt`, `run_pt036.py` and its
post-commit diff, the mastery report, `Q-011`, `A-010`, `A-076`–`A-079`, `C-016`, `C-017`.

### Findings

**Everything load-bearing was RE-DERIVED rather than read.**

- **`PT-036` recomputed on both `D-031` arms by a reviewer-written script importing no project
  module. Every figure reproduced exactly** — 0/180 in band; median 243.8; 600 at the 99.44th
  percentile; overshoot 3.28×; pip-vs-point rescue 4/180; joint 7.30% / 5.62%; matched uniform
  nulls 7.12% / 7.00%; Thursday 13.41%; Friday − best other −6.10 / −8.91 pp; Friday range in
  [50,100] 40.45% at median 107.0; `censored = 0`. **Both `CONTRADICTED AS STATED` verdicts and
  the specificity failure are UPHELD on independent computation.**
- **`Q-011`'s `diff` reproduced exactly** — six changed lines, all identifiers — **and extended
  library-wide: three distinct `RULES.md` documents across 21 lessons, thirteen of them
  (including V10) the same file re-badged.** V10's file is **not a new fabrication variant**; it
  is the same shared template, now proved by byte identity rather than inferred from a hash, so
  confidence in the one-template finding **rises**.
- **Nine printed rules and two load-bearing slide texts transcribed with ZERO substitutions**,
  including three typographic infelicities a tidying pass would have removed.
- **Host-vs-guest: the determination is CORRECT, HIGH confidence, over-determined.** All five
  strands verified; the 13 `Steve` tokens counted independently; the handover scan re-run with
  zero matches; **four further first-person-ownership strands found and added** (the forum, the
  seminar, the recordings, the starfish story). Crucially, `D-025` consequence 4 holds: **nothing
  in V10 depends on the identification being right.**
- **`[01:14:06]` verified verbatim, and its novelty confirmed independently** — *"highest point
  on/in a chart"* and *"lowest point on/in a chart"* occur in **zero** of V01–V09. `A-010
  NARROWED, not CLOSED` is the right disposition.
- **`stop loss` = 0 confirmed by the reviewer's own search**, over body and whole file.
- **`C-016` and `C-017` refusals both UPHELD.** Neither is over-conservative; `C-017`'s declining
  of `D-008` is the best-argued passage in the submission, and `A-078`'s split application of
  `D-008` (to the number, not the reference point) is **principled, not opportunistic** —
  capture reliability is at issue for a garbled numeral and not for a cleanly-rendered name.
- **The safety trade was correctly identified as untestable, not dodged** — five of seven
  conditions `D-030`-blocked, with the specific lookahead hazard named in three files.
- **`SWF_CAPTURE_RECIPE.md` §10's frame-rate defect is REAL; V10's own capture was NOT harmed**
  (1,164 frames confirms a correct 2.0 → 20.0 patch). Escalate-don't-patch was correct under
  `D-038a`; **fixed by this reviewer on the integration branch.**

**Findings: 0 CRITICAL · 0 MAJOR · 4 MINOR · 7 NOTE.** All four minors are documentation or
register hygiene; **not one moves a measurement, classification, disposition or rule**, and three
of the four correct the record in the direction that *strengthens* the finding they belong to.

### Required Corrections

1. **`M1`** — open-item ID collision: `video/v10` allocated 81–85 while integration concurrently
   allocated 81–83 to V09 R2. **Renumbered 86–90 by this reviewer at merge-back, disclosed in
   place.** Student still owes the citation updates in `04_SCREENSHOTS/V10/INDEX.md` and the
   mastery report. **The policy half — `D-038a` does not require open-item numbers to be
   allocated against integration state — is open item 91 and needs an owner ruling.**
2. **`M2`** — `A-078`/`C-017` census: `[01:00:20]` is a seventh spoken rendering and it names the
   blue tracer. The true figure is **five of seven**, not four of six.
3. **`M3`** — `V10_SOURCE_NOTES.md` §15's *"no hour is ever stated"* is overstated; reword to a
   session-boundary-scoped claim.
4. **`M4`** — add the ASR caveat to `C-016` as a **further** reason for `UNRESOLVED`.

### Decision

```text
REVISE — CONFIDENCE HIGH
0 CRITICAL / 0 MAJOR / 4 MINOR / 7 NOTE
ADVANCEMENT AUTHORIZED. The V11 gate OPENS under D-024.
V10 is NOT COMPLETE until items 91-94 are applied and re-reviewed.
```

**Reviewer's summary judgement: this is the strongest submission the corpus has received** — and
the reason is less what it did than what it *declined* to do. It declined to test the lesson's
headline trade, naming the exact lookahead mechanism that would have produced a flattering
number; declined two tidy reconciliations; declined an unregistered alternative after seeing a
failure; declined to code two numbers that are stated *and printed*; pre-registered the
diagnostic that would otherwise have become a post-hoc rescue and reported that it fails too; and
argued its own 12/12 and its own 6/6 **down**, in writing.

### Git

Branch `review/v10` from `video/v10` @ `e5262b2`. Files: `18_REVIEW/V10/V10_REVIEW_R1.md` (new),
`18_REVIEW/REVIEW_INDEX.md`, `00_SYSTEM/COURSE_PROGRESS.md`, `LOG.md`. Explicit-path staging only;
`git diff --staged` read before each commit. Validator **103 passed / 0 warnings / 0 failures**.
Merge-back to integration performed as a separate, single-threaded act under `D-038`, carrying
the `SWF_CAPTURE_RECIPE.md` §10 policy fix (item 87) and the 86–90 renumbering.

### Next Review Trigger

**V10 R2**, on student resubmission with items 91–94 applied. V11 may start meanwhile under
`D-024`.

---

## 2026-08-13 — Reviewer Session (V10 R1 — MERGE-BACK)

Single-threaded `D-038` merge-back of `video/v10` + `review/v10` into the integration branch,
performed as its own act after the review was written and pushed. `git fetch --all` first;
divergence read before merging (7 integration commits ahead, all V09 R2).

### The `SWF_CAPTURE_RECIPE.md` §10 policy fix — open item 87 CLOSED

**The defect is real** and all three sites were read: the header table, the prose *"Patch
3.0 → 30.0 fps"*, and the speedup table's *"3 fps control"* column all quote 3.0 as if it were
the library's constant. **V10 declares 2.0.** Applied literally it sweeps at **15×, not 10×**,
and fails silently at 7.5-presentation-second spacing.

**V10's own capture was NOT harmed, and that was checked rather than assumed:** the realised
sweep of **1,164 frames** (5776.2 ÷ 5 + 8 = 1,163) is arithmetically consistent only with a
correct 2.0 → 20.0 patch. The defect was **latent**, avoided by a session following `GOTCHA 5`'s
read-the-header advice rather than §10's prose — the kind of luck a recipe must not depend on.

**Fixed on the integration branch** (`SWF_CAPTURE_RECIPE.md` is a POLICY ledger under `D-038a`
and a task branch may not touch it). The V10 student session's escalate-don't-patch handling was
**correct**, and is the second consecutive lesson to get that boundary right.

### ⭐ THE MERGE ITSELF PRODUCED EVIDENCE, AND IT WIDENS OPEN ITEM 91

**The merge CONFLICTED in three files** — `REVIEW_INDEX.md` (3 hunks), `LOG.md` (2 hunks),
`COURSE_PROGRESS.md` (1 hunk) — **every one of them an evidence ledger `D-038a` calls
*"append-only and `git`-mergeable by construction"*. They are not.** Both branches appended to
the tail of the same tables and status blocks. `LOG.md`'s conflict **interleaved two session
entries**, splicing the V09 R2 entry's Decision/Files/Git/Next-Action sections into the middle
of the V10 R1 entry's fenced Decision block.

All were resolved by hand, the status blocks reconciled rather than concatenated, and the
`LOG.md` interleave repaired by moving the V09 R2 tail back to its own entry. **Disclosed rather
than absorbed.** `D-038a`'s safety evidence was the V08 merge, which had no concurrent second
writer on the same tails; **this one did, and the premise failed in three files at once.**

### Open-item renumbering, applied

V10's items **81-85 → 86-90**, with the old→new map disclosed in place beneath the open-items
table. V09 R2's 81-83 keep their numbers, having been allocated on the integration branch.
Two committed V10 artifacts still cite *"open item 82"* for the recipe defect and are carried as
item 91's student-owed half.

### Git

Merge commit on `claude/add-documents-repository-fdfb3u`. Paths staged explicitly; `git diff
--staged` read before committing; `git add -A` never used. `validate_project.py`:
**103 passed, 0 warnings, 0 failures.**

### Next Action

**V11 may start** — the gate is OPEN under `D-024`. **V10 R2** on student resubmission with
items 91-94 applied.

---

## 2026-08-13 — V10 R1 REMEDIATION: items 91 (student half), 92, 93, 94 APPLIED and ⚠ SELF-VERIFIED AT OWNER DIRECTION

### ⚠⚠ READ THIS FIRST — THIS ROUND DOES NOT SATISFY `D-003`

**One session both FIXED and VERIFIED all four of `V10_REVIEW_R1.md`'s MINORs, on the owner's
explicit authorisation**, given on the ground that all four are small documentation edits and
citing the V09 R2 items 81–83 precedent set on this same date. **That authorisation is real and it
is recorded here — but it does not manufacture independence.** There was **no R2** and **no
independent `PASS`**. Every item carries the status **`CLOSED — SELF-VERIFIED AT OWNER
DIRECTION`**, never `CLOSED — VERIFIED`, and the same string is used in `REVIEW_INDEX.md`
(open-item rows, STATUS block, DECISION TABLE row and its notice), in `COURSE_PROGRESS.md`
(SUMMARY, CURRENT LESSON, NEXT LESSON) and in every artifact block written this session. **The
string exists for no other purpose than to be visibly different, so a later reader can never
mistake it for an arm's-length verdict.**

**This is the SECOND use of the pattern**, after V09 R2. Recorded in the same words deliberately,
so the two are comparable and countable.

### What was fixed

| Item | Finding | What was done |
|---|---|---|
| **91** (student half) | `M1` — open-item ID collision; `video/v10` allocated 81–85 while integration gave 81–83 to V09 R2 | **Renumbering 81–85 → 86–90 VERIFIED COMPLETE by repo-wide sweep.** `grep -rn "item 8[1-5]"` over every `.md` returns **no V10-scoped hit**; every survivor is V09 R2's, which correctly keeps those numbers; 86–90 each appear exactly once with the mapped subjects. **⚠ AND THE REVIEW IS WRONG ON A POINT OF FACT** — see below |
| **92** | `M2` — the spoken census of the anchor-distance reference object is *"four of six"* | Corrected to **five of seven** at **seven sites**, three more than the review named |
| **93** | `M3` — §15's *"no hour is ever stated"* is falsified by four incidental clock times | Rescoped to **"No session-boundary clock time is stated"**, with all four times listed and characterised |
| **94** | `M4` — `C-016` does not apply its own transcript's ASR caution to its own evidence | **ASR caution block added**, superseding nothing |

### ⚠ `M1`: THE REVIEW'S FACTUAL CLAIM IS FALSE, AND IT IS CORRECTED IN PLACE RATHER THAN ABSORBED

`V10_REVIEW_R1.md` `M1`, its REQUIRED CORRECTIONS item 1, its ADVANCEMENT block and the
RENUMBERING DISCLOSURE all state that `04_SCREENSHOTS/V10/INDEX.md` § ESCALATION and
`07_MASTERY_REPORTS/V10_MASTERY_REPORT.md` escalation 2 **cite *"open item 82"***, and that
correcting them is the student's owed half.

**They do not, and never did.** Both referred to the recipe defect **by description and carried no
item number at all.** Verified by grepping `82` in each file: the only hits are the source `.swf`'s
SHA-256 and an `R = 82.0` chart label in the frame table. **The renumbering therefore orphaned
nothing, and there were no stale pointers to fix.**

**What was actually owed is the opposite act, and it is done:** both artifacts have **gained** a
pointer naming open item **87**, recording that it is ✅ `CLOSED`, that it was `82` on `video/v10`,
and that the collision and the `D-038a` gap behind it are carried at item 91. **Nothing in either
artifact is superseded** — each block says so on its face.

**The review file itself is NOT edited** (`REMEDIATION_PROTOCOL.md` §6). The correction lives in
`REVIEW_INDEX.md` item 91's status cell, in a retention block beneath the RENUMBERING DISCLOSURE
whose wrong paragraph is left standing, and in both artifacts.

**The policy half of item 91 stays OPEN and was not touched.** Amending `D-038a` requires an owner
ruling; neither a student nor a reviewer session may make one.

### `M2`: the sweep found three sites beyond the four the review named

`[01:00:20]` was **re-derived from `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` at source** — body line
2452 reads *"75 pips off of the blue tracer"*. So does `[00:54:02]` (line 2203), *"25 to 50 pips
the dealer falls into the shadow box"* — an eighth **distance** utterance that names **no reference
object** and is therefore **recorded in `A-078` and `C-017` but deliberately NOT counted** in
either census.

The review named `A-078`, `C-017`, `V10_MASTERY_REPORT.md` §J and this register's item text. **A
repo-wide sweep for the undercount found three more:**

- **`04_SCREENSHOTS/V10/INDEX.md`** — *"the audio gives it six times"*
- **`05_HOMEWORK/V10/V10_COMPREHENSION_ANSWERS.md` Q6** — *"four of six spoken instances"*
- **`02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` TRANSCRIPTION NOTE 1** — *"given six times"*, with its
  own six-marker list

**The transcript note is the one that mattered most to catch**, because it is the note `M4` relies
on: leaving it stale would have left two V10 records disagreeing about the same census while a
third cited one of them as authority.

**The comprehension answer was NOT rewritten.** It is a preserved first attempt, committed before
the scorer existed, so the correction is **appended as a block** and the original wording stands
(`REMEDIATION_PROTOCOL.md` §2). **The transcript's verbatim body is UNTOUCHED** — only the header
note is corrected.

**The direction of the correction matters and is recorded everywhere it appears: a 5/7 spoken
majority makes the misspeak reading `C-017` refuses LESS available than 4/6 did.** The correction
strengthens the finding.

### `M3`: rescoped, and `A-076` checked and left alone

§15 now reads **"No session-boundary clock time is stated"**, states that sessions are named
constantly and not one is given an opening or closing hour on any clock, and lists all four
incidental times with what each actually is — `[00:02:24]` *"at 830"* (a chart students are being
told to stop watching), `[00:05:09]` *"seven o'clock New York time"* (the seminar announcement),
`[00:42:52]` *"3 o'clock in the morning"* (the speaker's own readiness, rhetorical), `[01:03:57]`
*"5 6 o'clock at night"*. **All four re-derived at source; all four resolve verbatim.**

**`A-076`'s parallel sentence was checked as the review directed and is CORRECT AS WRITTEN.** It
reads *"V10 states no clock time for any session"* and backs it with six zero-counts (`7:00`,
`3:00 am`, `3:30`, `9:00`, `9:30`, `5:00 pm`, all **0** in the body, `Q-011` §1). **It never
overshot, it is left untouched, and it is cited in the fix as the model.**

**The same unscoped sentence was ALSO found in `00_SYSTEM/COURSE_PROGRESS.md`'s V10 block**
(*"no session clock time"*) and corrected there too — that block is a summary later sessions read
*instead of* the source notes, so leaving it would have reproduced M3's exact defect one file over.

### `M4`: a caution added, and what it does NOT license stated with it

The block records that `[01:00:41]`'s *"one-day"* and `[01:00:43]`'s *"three days"* are **both ASR
renderings and NEITHER is printed on any slide**, cites TRANSCRIPTION NOTE 1 (*"Numeric ranges
wobble, and one of them is load-bearing"*) and the transcript's own **`MEDIUM–HIGH`** self-rating,
and concludes it is a **further independent reason to refuse** the reconciliation: the refused
reading is a *construction over the two numerals*, and a construction over figures that may be
rendering artifacts is unsafe.

**Re-derived, not taken on the review's word:** TRANSCRIPTION NOTE 1 and the confidence rating were
read at source, and **the absence of any printed holding period was checked against all 32 curated
frames** via `04_SCREENSHOTS/V10/INDEX.md`. That check is what makes *"neither is printed"* a
verified claim rather than a repeated one.

**The block also states what the caution does not license**, which the review did not ask for:
it is **not** grounds to discard either figure (`D-030`, `SOURCING_HIERARCHY.md` §3.2 forbid
selecting the convenient one), and the contradiction is **over-determined without them** — strike
both ASR-suspect figures and `[00:41:45]` *"at least two days"*, `[01:32:07]` *"two days"* and
`[01:26:39]` *"three days … maybe one more"* still state the duration three incompatible ways.

**Nothing above the block is superseded** — the review is explicit that the omission *"strengthens
nothing and undermines nothing in the disposition"*. `C-016`'s Related section now cites
TRANSCRIPTION NOTE 1 and `A-078`. Cross-referenced to item **95**, the owner question about tagging
this class at filing.

### ⚠ A BOOKKEEPING DEFECT THIS ROUND FOUND AND DISCLOSED RATHER THAN QUOTED AROUND

**`REVIEW_INDEX.md`'s SEVERITY TOTALS table is stale at V09 R1** — it still reads `MINOR 57 / 12
open / 45 closed`, predating **V09 R2's +3** and **V10 R1's +4**, because **neither round posted
the per-round arithmetic paragraph** that every round from V07 R1 onward had posted.

This round's delta is therefore recorded as **−4 open MINOR / +4 closed MINOR** and **absolute
figures are deliberately not quoted**, because quoting a total off a stale table would manufacture
a number rather than record one. **A warning block is added under the table and item 96 is widened
to cover it**: item 96 charged exactly this decay in `COURSE_PROGRESS.md`, and **the same shape is
present in `REVIEW_INDEX.md` itself** — a maintained prose/delta layer above an unmaintained table,
where the table is the part a reader scans. Reconciling it means re-auditing the pre-V03 rows
carried unreconciled since V02 R1: a sweep, not an edit, and not one this session was authorised
to make.

### What did NOT change

**No marker, quotation, figure, disposition, `DO NOT CODE` verdict, grade, machine-rule
classification or conclusion moves anywhere.** `A-078`'s number stays `RESOLVED BY COURSE`; its
reference point stays `DO NOT CODE`; `C-016` and `C-017` stay `UNRESOLVED`; `A-010` stays
`NARROWED`; every `PT-036` figure and both `CONTRADICTED AS STATED` verdicts are untouched. **No
pre-registration, runner or output file was opened for editing** (`COMMON_PROTOCOL.md` §9 rule 7).
**Superseded text is retained at every site** per `REMEDIATION_PROTOCOL.md` §2.

**Still OPEN and NOT covered by this round's verdict:** items **86** (recommended `PT-037`),
**88** (printed-vs-spoken precedence — owner), **89** (`A-077`, the lock), **91's policy half**,
**95** (owner question), **96** (bookkeeping sweep, now widened) and **36** (the `D-030`
dimension-B disposition, owed for the sixth consecutive lesson-round). **`N1` and `N2` from R1 were
recommended-not-required and were deliberately left undone**, to keep this round to the four
minors the owner authorised.

### Files

- **Updated:** `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` (`A-078`);
  `11_CONTRADICTIONS/CONTRADICTIONS.md` (`C-016`, `C-017`);
  `03_LESSON_NOTES/V10_SOURCE_NOTES.md` §15; `07_MASTERY_REPORTS/V10_MASTERY_REPORT.md`
  (§J, escalation 2); `04_SCREENSHOTS/V10/INDEX.md` (§ ESCALATION, screenshot-value block);
  `05_HOMEWORK/V10/V10_COMPREHENSION_ANSWERS.md` Q6;
  `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` TRANSCRIPTION NOTE 1 (**header only — body untouched**);
  `18_REVIEW/REVIEW_INDEX.md` (STATUS, DECISION TABLE + notice, SEVERITY TOTALS warning, items 88,
  91, 92, 93, 94, 96, RENUMBERING DISCLOSURE); `00_SYSTEM/COURSE_PROGRESS.md`; this log.
- **NOT touched:** `18_REVIEW/V10/V10_REVIEW_R1.md` (`REMEDIATION_PROTOCOL.md` §6);
  `00_SYSTEM/DECISIONS.md`; `06_MANUAL_BACKTEST/**`; the transcript body.

### Git

Branch `fix/v10-r1-minors`, cut from the integration branch at `9c00a60` after `git fetch --all`
confirmed **zero divergence** (`D-038`). Paths staged **explicitly**; `git diff --staged` read
before every commit; **`git add -A` never used.** Merge-back performed as its own deliberate
`D-038` step, with a second `fetch` and a divergence check first.

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Action

**V11 may start — the gate is CONFIRMED OPEN under `D-024`**, and it opened at R1 on 0 CRITICAL /
0 MAJOR, never depending on these four minors. **A V11 session inherits V10's qualification:
V10 is `COMPLETE` only in the ⚠ SELF-VERIFIED AT OWNER DIRECTION sense.** If a later reviewer wants
the independence this round lacks, the cheap re-derivations are: `[01:00:20]` and `[00:54:02]` in
the transcript body (`M2`); `[00:02:24]`, `[00:05:09]`, `[00:42:52]`, `[01:03:57]` (`M3`); a scan
of the 32 curated frames for any printed holding period (`M4`); and `grep -rn "item 8[1-5]"`
(`M1`). **None of it takes long.**

---

## 2026-08-13 — V11 STUDENT SESSION · `Bootcamp1 Wk4 040812 Part1 (51mins).swf`

**Branch:** `video/v11`, dedicated git worktree at `/Users/randyschutt/Desktop/Trading/MMM-Agents-v11`,
cut fresh from `origin/claude/add-documents-repository-fdfb3u` (`a004e88`) per `D-038`. Gitignored
**child** directories symlinked back to the primary checkout (`01_SOURCE_VIDEOS/Forex Bootcamp`,
`06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1`) — the V08/V09/V10 pattern. **`git status` stayed
clean throughout; no `I-009` collision.**

**Gate:** verified **OPEN** in `REVIEW_INDEX.md` and `COURSE_PROGRESS.md` **before any V11 artifact
was created.** V10 R1 returned `REVISE` 0 `CRITICAL` / 0 `MAJOR` / 4 `MINOR` → opens under `D-024`.
**V10's ⚠ SELF-VERIFIED qualification is inherited and recorded.**

### What V11 is

**Week 4, Part 1 · 2012-04-08 · course author, 100% of runtime · HIGH confidence.**

Two lessons welded together. The first 25 minutes are a mailbag-driven **restatement** of the entry
protocol — *"25 to 50 pips out of the box, second leg W formation… inside the TDI… the double
band"* — stated eight ways and adding nothing new. The last 25 minutes **teach the RSI substrate of
the TDI for the first time in the corpus**, across six printed slides.

**The session date is corroborated from inside the recording** — `[00:25:33]` *"I figured it was
sunday and it was easter"*; Easter Sunday 2012 = **8 April 2012** — which **confirms V10's printed
end-card prediction**, made from inside V10 and recorded in the carry-forward before V11 was opened.

### The headline finding

**A printed slide headed *"Parameters of RSI"* lists six parameters and NOT the lookback period.**
`rsi` occurs 33 times in the audio with no period attached; no frame among 28 detected screen
states shows a settings dialog; and the **Tier 2 `MMM-NOTES` PDF is also silent** (`D-040` step 2,
searched). **`A-080`** opens. The TDI's distributed default of 13 was **refused explicitly**, and
the trap named — `MMM-NOTES` p.38 lists a **13 EMA**, so a session could reach *"13"* by conflating
two indicators and feel sourced doing it.

**The cost was measured rather than asserted**: across six candidate periods on the `D-036a`
corpus, *"time above 80"* — V11's own overextended condition — ranges **0.04% → 5.66%, a 144×
ratio**. Even adjacent 13 vs 14 differ ~20% relative.

### Capture

`SWF_CAPTURE_RECIPE.md` §10 at 10×, **using the corrected per-file frame-rate rule** (open item 87).
**V11 declares 3.0 fps; V10 declared 2.0** — V11 is the demonstration that the field varies in
**both** directions. Port **8931 was BUSY** on first try and `GOTCHA 4`'s check caught it; 8953 was
verified by PID and by SHA-256 of the served bytes. The `GOTCHA 5` pre/post-click guard fired and
passed. 620 frames; the frame→time offset was **measured** (`t = i×5 + 15`) against frame `0021`'s
burned timecode `02:00`, not assumed. 28 screen states → **27 curated frames**, each opened and
looked at before naming.

### Q-012 — the quarantine audit

`NOTES.md` and `VISUAL_INDEX.md` **fabricated**. `RULES.md` discharged by `Q-007`, markers
re-measured anyway. Two findings that advance the corpus pattern:

1. **`Q-011`'s "one generator" claim reproduces on a second lesson by EXACT `diff`** — V11's
   `RULES.md` is **V01's file with six identifier strings swapped**: 12 differing lines, **zero
   content lines**.
2. **The one real image is the TITLE CARD**, indexed as *"Asian Box accumulation range with 5, 13,
   50, 200, and 800 EMAs."* Third instance of the sixth failure mode, first on a frame with no
   chart content at all. **`EMA` occurs ZERO times in 51 minutes.**

**The register cuts both ways:** that title card prints **`Week 4`**, independently corroborating
`D-017` §2's ordering.

### Records

**New:** `A-080` (RSI period), `A-081` (*"a 25 risk"*, no unit — **spoken, not printed**), `A-082`
(flashcards — a **curriculum** blocker that gates trading for the week and is specified nowhere),
`A-083` (is V11's sub-graph *"safety trade confirmation"* V10's price-pane safety trade? probably —
**`DO NOT MERGE`**).
**Narrowed:** `A-039` (TDI — *"displayed, not taught"* **retired**; still no parameters),
`A-011` (M/W — pullback + another leg, *"aggressive and big"*, negative case, mechanism; still no
count/size/invalidation).
**Annotated:** `A-020` → `CONFLICT — OWNER ADJUDICATION REQUIRED`, on its `Mayo = 200` half only.

**`C-018` filed and NOT adjudicated.** Tier 2 (`MMM-NOTES` p.66) + owner attestation vs Tier 1
(V11 `[00:46:45]` *"There's the mayonnaise. There's the 50."*). §3.3's *"the recording wins"*
**cannot close it**: the recording is two-ways readable, and the identical phrase means the **RSI
baseline** seven seconds later at `[00:46:52]`. The frame at `46:45` was extracted specifically to
arbitrate and **could not** — reported as a negative result.

### Manual backtest

**`PT-039`** *(filed, committed and run as `PT-037`; re-issued by owner ruling 2026-08-13 — see
the entry at the end of this log)* pre-registered at `beee96a` **before the runner existed and
before any bar was read**;
runner at `6da82b3`; output after that. **Commit-timestamp ordering is the evidence.**

Claim: *"the low has to hold — how long? 30 to 90 minutes… the long sideways consolidation should
last up to two hours."* Estimand `P(FINAL | held ≥ T)` on M1, 894 session days, 26,028 candidate
lows, `W-C′`, holdout never opened.

| | Verdict |
|---|---|
| `M1a` duration informs at all | **PARTIALLY SUPPORTED** (+15.80 pp) |
| `M1b` the 30→90 band does work | **CONFIRMED AS STATED** (+12.17 pp) |
| `M1c` the named numbers are special | **CONTRADICTED AS STATED** — no feature at 30 or 90, both arms |
| `M1d` survives the confound | **PARTIALLY SUPPORTED** — 3 of 6 strata |

**The claim's direction is supported and its numbers are not.** `N3`'s margin is **monotone in
remaining session time** across a factor of eight (+5.5 pp → +44.0 pp, six strata in the right
order); `N4` puts the real 17:00 boundary at the **6.40th percentile** of 1,000 arbitrary 24-hour
boundaries. `O5` cuts the other way and says so: the **median candidate low is superseded in TWO
MINUTES**, so *"held 30 minutes"* is a ~1-in-7 event at the 85.6th percentile — **his threshold IS
selective; it is just not distinguished.**

**Predictions: 4 of 7 substantive** (P2, P5, P7, P8 right; P3, P4, P6 wrong). **The cheap P1 also
failed** and is still reported separately. **P6 is the instructive miss** — predicted 4–9 candidate
lows per day, actual **26** — and it is **his side of the argument**: it measures exactly how far
this unfiltered test sits from the setup he described.

**Most of V11 was NOT tested** and `BT_V11_0001` §1 says so first: the entry rule and **every one of
the six printed RSI thresholds**, all `D-030`-blocked.

### Three things this session got wrong or found late, recorded rather than absorbed

1. **A validator failure was pushed.** The first `BT_V11_0001` commit shipped without the required
   `EVIDENTIAL`/`DESCRIPTIVE` classification, because the validator was run **before** the file was
   staged rather than after. Caught on the next run, fixed in the following commit. **The durable
   lesson is ordering:** `stage → validate → commit`. Item **108**.
2. **A `PT` numbering collision was found late.** `PT-037` and `PT-038` were reserved **in prose**
   by `BT_V10_0001` §9, item 86 and this log; `PRE_REGISTERED/` held neither as a **file**, and
   `PT-037` §0's search was for files. **Proposed: V11 keeps `PT-037`; V10's reservations move to
   `PT-039` / `PT-040`.** Disclosed by append in `PT-037` §0, changing nothing in §§1–9. **A second,
   distinct instance of item 91's finding.** Item **99**.
3. **A `D-031` Arm B design defect was found at run time**, not in design. Arm B's DST `+1 h` shift
   moves the Friday close to 18:00, failing **every DST-week Monday** on the completeness rule:
   **11 exclusions on Arm A, 245 on Arm B.** Arm A is the pre-registered primary cell and no verdict
   moves — but **every session-day-unit test in the `PT` family inherits this.** Item **101**.

### V10's carry-forward (a)–(g) — all seven answered

(a) speaker **tested**, author continues · (b) V10's Easter-Sunday date prediction **CONFIRMED from
inside V11** · (c) the TDI *is* taught — **`A-039` narrows, does not close**, because no parameters
and the bands are promised at `[00:32:34]` and never delivered · (d) `A-077` **checked, not
advanced** · (e) `A-004` **checked, not advanced — and V10's "the course routes around it" reading
is strengthened** · (f) `C-017`'s printed-vs-spoken question gets **two more instances pointing
opposite ways**, and `Q7` is **evidence against a simple "print beats speech" rule** · (g) the
frame rate was **read per file** and varies in both directions.

### Files

- **New:** `02_TRANSCRIPTS/V11/V11_TRANSCRIPT.md`; `03_LESSON_NOTES/V11_SOURCE_NOTES.md`,
  `V11_INTERPRETATION.md`; `04_SCREENSHOTS/V11/` (27 PNG + `INDEX.md`);
  `05_HOMEWORK/V11/V11_HOMEWORK.md`, `scripts/rsi_period_sensitivity.py`, `data/…_output.txt`;
  `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-037_how_long_must_the_low_hold.md`
  *(→ re-issued as `PT-039_how_long_must_the_low_hold.md`)*,
  `scripts/run_pt037.py` *(→ `run_pt039.py`)*, `V11/BT_V11_0001.md`,
  `V11/data/pt037_output.txt` *(→ `pt039_output.txt`)*;
  `07_MASTERY_REPORTS/V11_MASTERY_REPORT.md`.
- **Appended (evidence ledgers, `D-038a`):** `00_SYSTEM/QUARANTINE_REGISTER.md` (`Q-012`);
  `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` (`A-080`–`A-083`, `A-039`/`A-011`/`A-020` updates);
  `11_CONTRADICTIONS/CONTRADICTIONS.md` (`C-018`); `18_REVIEW/REVIEW_INDEX.md` (V11 verdict row,
  items **97–108**); `00_SYSTEM/COURSE_PROGRESS.md` (V11 row, `V11 STATUS`, `V12 GATE`); this log.
- **NOT touched:** `00_SYSTEM/DECISIONS.md`, `SETUP_ISSUES.md`, `SOURCING_HIERARCHY.md`,
  `SWF_CAPTURE_RECIPE.md`, `COMMON_PROTOCOL.md` — **POLICY ledgers, integration branch only**
  (`D-038a`). `18_REVIEW/V10/**`, `06_MANUAL_BACKTEST/V10/**` — completed work.

### Git

Branch `video/v11` in its own worktree. Paths staged **explicitly**; `git diff --staged` read before
every commit; **`git add -A` never used.** Eight commits, each pushed. **No merge to integration —
that is a separate, single-threaded act under `D-038`, performed after independent review.**

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Action

**Independent review R1 of V11 (`D-003`).** The **V12 gate is CLOSED** until it returns.

**Owner decisions owed:** `C-018` (item 97) · the `PT` numbering resolution (item 99) · the
`SETUP_ISSUES.md` entry for `C-018`, which only the integration branch can write (item 100).

**⭐ V12 is the cheapest route to closing the two biggest things V11 leaves open** — same session,
same day, same charts, 55 minutes. **One frame showing an indicator-properties dialog closes
`A-080` and unblocks the whole RSI half of this lesson; one recurrence of *"mayonnaise"* with a
legend visible closes `C-018` / `A-020` on Tier 1 evidence.** Look for both deliberately.

---

## 2026-08-13 — Integration Session — `D-041`: the owner's definitive MA nickname mapping

**Branch:** `claude/add-documents-repository-fdfb3u` (integration) · **Act:** POLICY-ledger decision
under `D-038a`, made directly on integration after `git fetch origin` confirmed **zero divergence**
(`0 0`, `git rev-list --left-right --count`).

### What happened

The owner issued a direct, definitive ruling on the moving-average nicknames:

> *"Mayonnaise is the 200 EMA, period. 50 is water, 5 is ketchup, 13 is mustard, 800 is blueberry.
> These are the definitive names and numbers."*

Recorded as **`D-041`**, on the same evidentiary footing as the owner-attested closures of `A-014`
and `A-023` and the normative admission of `MMM-NOTES` (all `D-039`).

### ⚠ THE FINDING THIS SESSION DID NOT EXPECT — ketchup and mustard are INVERTED

The task that produced this entry described the ruling as **confirming** `A-020`. It confirms three
rows and **overturns two**:

| Nickname | `A-020` said | **Owner says** | |
|---|---|---|---|
| Ketchup | 13 | **5** | ⚠ **OVERTURNED** |
| Mustard | 5 | **13** | ⚠ **OVERTURNED** |
| Water | 50 | 50 | ✅ |
| Mayo | 200 | 200 | ✅ reaffirmed |
| Blueberry | 800 | 800 | ✅ (keeps its stronger `RESOLVED BY COURSE` basis, V09 `[00:41:43]`, 15-min) |

**This was recorded loudly rather than swapped silently**, and it is flagged to the owner and to
the incoming V11 reviewer as reversible on a word. The superseded assignment agreed with **three
independent Tier 3 web sources**, with `Q-002`'s fabricated *"5 Mustard"*, **and** with the
project's own inference from V06's *"closed below 13"* and its 13/50 relationship — four coherent
lines of reasoning, all wrong. **No recording is contradicted:** `ketchup` occurs nowhere in
genuine audio in the corpus and `mustard` occurs 0× in V05–V08.

**That is the most useful thing this session produced.** `EXTERNAL_VOCABULARY_REFERENCE.md` §5's
Tier 3 material was **unanimous and wrong** on a point where it looked strongest. `D-030` was right
for the right reason, and §5.16 now carries the receipt.

### `C-018` — closed, and on what basis

V11 `[00:46:45]` *"Look where the averages are. There's the mayonnaise. There's the 50"* resolves
as **reading B (enumeration)**, not apposition. `A-020` is untouched by the utterance.

**The V11 session was right and is credited.** It refused reading A, gave three grounds for B, and
declined to adjudicate — `C-018` states in terms why §3.3's *"the recording wins"* could **not**
close it, because the recording is two-ways readable. The owner supplied the **disambiguation**
that was missing, which is not the same act as outranking a recording. **No "Tier 0" is created**,
and `SOURCING_HIERARCHY.md` §3.4's re-check obligation on `A-020` **stays live** — argued in
`D-041` rather than asserted.

**`C-018` itself is closed on `video/v11`, not here.** `CONTRADICTIONS.md` is an **evidence
ledger** (`D-038a`) and `C-018` is unmerged. Closing it on its own branch is the rule working, not
a split-brain; it lands at merge-back.

**`SETUP_ISSUES.md` was NOT written, deliberately.** `C-018` carried a `SOURCING_HIERARCHY.md` §3.2
**Case C** logging obligation as `OWED, NOT DONE`. Case C is *"genuine conflict — do not adjudicate,
surface to the owner."* The owner has adjudicated, so the obligation is **discharged rather than
performed**; there is no live conflict to log. Reasoned in `D-041` consequence 5 rather than
silently skipped.

### The mapping is now discoverable centrally — three places, deliberately

`D-041` (authoritative) · `EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 (where a session looking up a
nickname actually lands, and where the wrong table lives) · `SOURCING_HIERARCHY.md` §3.4 (where the
re-check obligation lives). **`08_CONCEPT_LIBRARY/CONCEPT_INDEX.md` was considered and rejected**
on that file's own rule 5 and its `A-026` precedent: a nickname's period is a **label expansion**,
not a method concept, and promoting it would launder a label into a definition.

### Files

- **Updated:** `00_SYSTEM/DECISIONS.md` (`D-041`); `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`
  (`A-020` — INDEX row, ⚠️ banner above the mapping table, `⛔ SUPERSEDED IN PART` block, Related
  table); `00_SYSTEM/EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 (⛔ superseding banner + canonical
  table); `00_SYSTEM/SOURCING_HIERARCHY.md` §3.4; this log.
- **NOT touched:** `CHANGELOG.md` (no prior decision entry sets that convention — `D-038a`,
  `D-039` and `D-040` are absent from it); `00_SYSTEM/SETUP_ISSUES.md` (reasoned above);
  `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md` (reasoned above); every `A-020` row of superseded text,
  retained unedited per `REMEDIATION_PROTOCOL.md` §2; all `18_REVIEW/**` review files
  (`REVIEW_PROTOCOL.md` §11).

### Git

`git fetch origin` first; **zero divergence** confirmed before any edit. Paths staged
**explicitly**; `git diff --staged` read before the commit; **`git add -A` never used.**

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Action

**The V11 independent review is not unblocked by this and does not depend on it.** Two things are
put to the reviewer: (1) the **ketchup/mustard inversion** — a reviewer is entitled to put it back
to the owner, and nothing here is protected from that; (2) `C-018`'s closure arrives on
`video/v11`, so a reviewer reading integration alone will not see it until merge-back.

---

## 2026-08-13 — V11 branch — two owner rulings applied: `C-018` closed, `PT-037` re-issued as `PT-039`

**Branch:** `video/v11` (worktree `MMM-Agents-v11`, `D-038`) · **Act:** applying two owner rulings
to V11's artifacts **before** the independent review starts. **Still not merged** — merge-back
still waits on R1. `git fetch origin` first; **zero divergence** confirmed (`0 0`).

### 1. `C-018` — CLOSED by owner adjudication (`D-041`)

> *"Mayonnaise is the 200 EMA, period. 50 is water, 5 is ketchup, 13 is mustard, 800 is blueberry.
> These are the definitive names and numbers."* — owner, 2026-08-13

**`[00:46:45]` resolves as reading B — enumeration.** *"There's the mayonnaise. There's the 50"*
points at two lines in turn. **Mayo is the 200; `A-020` is untouched by the utterance.**

**This session's own record was right.** `C-018` gave three grounds for reading B and **declined to
adjudicate anyway**. The owner's ruling agrees with the reading it already held. Filing the
conflict rather than adopting the convenient answer cost nothing and is why the closure is clean.

**What the closure does NOT establish, and `C-018`'s closure block says so at length:**
§3.3's *"the recording wins"* was **neither applied nor overridden** — it cannot close a record
whose recording is two-ways readable. **The owner supplied a DISAMBIGUATION, not a trump card.
There is no "Tier 0."** `A-020` stays `RESOLVED — OWNER ATTESTATION` (the weakest resolved status)
and **`SOURCING_HIERARCHY.md` §3.4's re-check obligation on it REMAINS LIVE.** *Required Research*
is still unsatisfied and **V12 is still the cheapest route to Tier 1 closure.**

**⚠ The same ruling overturned two rows of `A-020`** — **ketchup = 5, mustard = 13**, inverting the
prior record. It contradicts **no recording** (`ketchup` occurs nowhere in genuine audio; `mustard`
0× in V05–V08) and overturns only Tier 3 and the project's own V06 inference. Recorded on the
integration branch at `D-041`; flagged here and in `REVIEW_INDEX.md` item 97 because **a reviewer
is entitled to put it back to the owner.**

**`SETUP_ISSUES.md` was NOT written and item 100 is closed anyway.** §3.2 **Case C** is *"genuine
conflict — do not adjudicate, log it, surface to the owner."* The owner has adjudicated; there is
no live conflict for an entry to describe. **Discharged, not performed** — `D-041` consequence 5.

### 2. ⭐ `PT-037` → `PT-039` — owner REVERSED this session's proposed resolution

> ***"Move V11 not V10 since V11 is after."*** — owner, 2026-08-13

**V10 KEEPS `PT-037` and `PT-038`. V11's hold-duration test is re-issued as `PT-039`.**

This session proposed the **opposite** (V11 keeps 037; V10's reservations move to 039/040), and
reasoned from the **artifact**: a committed, run pre-registration should not move, a prose
reservation is free to. **The owner ruled on precedence** — V10 filed first, so V10 keeps its
numbers. **The reversal is applied exactly as this session said it would be if reversed:**
`SUPERSEDED — NUMBERING`, re-issued, **result retained in full**, nothing in the pre-registration's
§§1–9 touched.

**⚠ `PT-040` WAS NOT ALLOCATED, AND A SESSION EXPECTING IT WILL BE CONFUSED.** The reversal was
framed as *"V11 moves to `PT-039`/`PT-040`"*, on the reading that V11 held both numbers. **It did
not — V11 filed exactly ONE pre-registration.** Every `PT-038` reference anywhere in V11's
artifacts points at **V10's** safety-trade reservation, which was never V11's to move. **`PT-039`
is the only renumbering; `PT-040` remains free.**

**V10's numbering was NOT touched, at all.** `BT_V10_0001.md` §9, `V10_REVIEW_R1.md`,
`V10_MASTERY_REPORT.md`, `REVIEW_INDEX.md` items 86 and 89, and every V10 `LOG.md` and
`COURSE_PROGRESS.md` line keep `PT-037`/`PT-038` unchanged — verified by grep after the edit, not
assumed. `REVIEW_PROTOCOL.md` §11 (no overwriting a completed review) is intact.

**Renames are git-tracked, and no stub was left at the old paths.** A `PT-037` placeholder would
squat the number the owner has just ruled belongs to V10 — the opposite of the ruling. Nothing is
deleted: content is unchanged, `git log --follow` reaches the full history, and the pre-run
ordering is recorded in the file.

**⭐ The `D-026`/`D-027` commit-timestamp ordering is UNAFFECTED**, and this is the thing a reviewer
should check first. Verification rests on **commit order, not filename**:
`beee96a` (pre-registration) → `6da82b3` (runner) → `4d2bdcd` (output) → `735a458` (scoring).
**This re-issue is a later commit than all four**, so it cannot backdate anything.

**The self-disclosure is what made this cheap.** The collision was found late — by the check
`D-038a` consequence 1 requires, run against **files** when the reservations were **prose** — but it
was disclosed with a specific remedy attached, and the owner could therefore rule in one sentence.

### Files

- **Renamed (git-tracked, content unchanged):**
  `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-037_how_long_must_the_low_hold.md` → `PT-039_…md`;
  `06_MANUAL_BACKTEST/scripts/run_pt037.py` → `run_pt039.py`;
  `06_MANUAL_BACKTEST/V11/data/pt037_output.txt` → `pt039_output.txt`.
- **Updated (V11-owned references only):** the re-issued pre-registration (governing block + §0
  reversal note; §§1–9 self-references relabelled, **design untouched**);
  `06_MANUAL_BACKTEST/V11/BT_V11_0001.md`; `07_MASTERY_REPORTS/V11_MASTERY_REPORT.md`;
  `03_LESSON_NOTES/V11_INTERPRETATION.md`, `V11_SOURCE_NOTES.md`;
  `05_HOMEWORK/V11/V11_HOMEWORK.md`; `02_TRANSCRIPTS/V11/V11_TRANSCRIPT.md` (**notes only — the
  verbatim body is untouched**); `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` (`A-020` V11
  annotation cleared; one `PT` reference); `11_CONTRADICTIONS/CONTRADICTIONS.md` (`C-018` closed);
  `18_REVIEW/REVIEW_INDEX.md` (items **97**, **98**, **99**, **100**, **101**);
  `00_SYSTEM/COURSE_PROGRESS.md` (V11 row, carry-forwards **(g)** and **(h)**); this log.
- **NOT touched, deliberately:** `18_REVIEW/V10/V10_REVIEW_R1.md`, `06_MANUAL_BACKTEST/V10/**`,
  `07_MASTERY_REPORTS/V10_MASTERY_REPORT.md`, `REVIEW_INDEX.md` items **86**/**89**, and every
  other V10-owned `PT-037`/`PT-038` reference — **V10's numbering stays exactly as filed**;
  `00_SYSTEM/DECISIONS.md` and `00_SYSTEM/SETUP_ISSUES.md` (**POLICY** ledgers — `D-041` was made
  on the integration branch, `D-038a`); all superseded text, retained per
  `REMEDIATION_PROTOCOL.md` §2.

### Git

Branch `video/v11`, own worktree. `git fetch origin` first, **zero divergence** confirmed. Paths
staged **explicitly**; `git diff --staged` read before the commit; **`git add -A` never used.**

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Action

**V11's independent review (R1) — unchanged, still owed, still the only thing that can make V11
`COMPLETE`.** Three things are handed to the reviewer: (1) the **ketchup/mustard inversion** in
`D-041`, reversible on a word; (2) `PT-039`'s re-issue and the commit-ordering audit trail above;
(3) `PT-040` is **free**, not V11's, despite the framing of the ruling that produced this entry.

---

## 2026-08-13 — Integration Session — `D-042`: the nickname↔period search returns NEGATIVE; the owner's colour mapping; and a Tier 1 conflict flagged

**Branch:** `claude/add-documents-repository-fdfb3u` (integration) — `DECISIONS.md`,
`SETUP_ISSUES.md` and the standing standards are **policy ledgers** under `D-038a`.
Also touched: `feature/tradingview-mmm-indicator` (Pine tool defaults) — logged in its own entry.

### What was asked

Two things, and they turned out to be of different sizes.

1. **Resolve the open ketchup/mustard question** against the course. Owner direction: *"Let's go
   with whatever the course says. I'm sure it's 5 ketchup, 13 mustard but I could be wrong."*
   A **conditional** instruction — the course governs **if the course speaks**.
2. **Add the owner's colour mapping** — described as new and uncontested: 5/ketchup = red,
   13/mustard = yellow, 50/water = aqua, 200/mayonnaise = white, 800/blueberry = blue.

### 1 — The search: exhaustive, and NEGATIVE

Coverage: **V01–V10** transcripts in full on this branch; **V11 read from
`origin/video/v11`**, which is unmerged and whose omission would have made the result a **false
negative**; the full 84-page `MMM-NOTES` text extract; every `04_SCREENSHOTS/VXX/INDEX.md` and
`09_CHART_EXAMPLES/`. Method: case-insensitive sweep for `ketchup` / `catsup` / `catch up` /
`mustard` / `mayonnaise` / `mayo` / `blueberry` / `water` / `condiment`, then a **±4-line
proximity scan of every hit** against `5 / 13 / 50 / 200 / 800` — so a pairing split across a
sentence boundary would still have been caught. Every proximity hit was then read in context by
hand; all of them resolved to unrelated numbers (*"25 to 50 pips"*, *"50 pip stop hunt"*, the RSI
50 baseline) except the two already on the record.

**Result: not one new pairing.** `ketchup` occurs **0× in genuine audio anywhere in V01–V11**
(V01 `[00:19:24]`'s *"catch up in the mustard"* is logged garble; V10 `[00:37:02]` *"I'll never
catch up"* is the ordinary English phrase). `mustard` occurs **twice**, both V04 `[00:14:42]` /
`[00:14:47]`, both numberless. The only explicit pairings in existence are the two `D-041` already
cites: **blueberry = 800** (V09 `[00:41:43]`, Tier 1) and **mayo = 200** (`MMM-NOTES` p.66,
Tier 2).

**So the owner's condition is not met, and `D-041` stands unchanged.** Ketchup = 5,
mustard = 13, on owner attestation. `D-041`'s own Evidence-block claim that no Tier 1 statement
attaches a period to either nickname is now **verified by independent search rather than
inherited**, and `SOURCING_HIERARCHY.md` §3.4 is **discharged as at V11** while staying **live for
V12 onward**.

### 2 — The colours: three rows corroborated, and **two rows contradicted by tape**

The 50/200/800 rows are corroborated `[TOOLING]` by the owner's own MT4 template
`3M-shadow-boxes-15M.tpl` (aqua/white/blue), read off disk on `feature/tradingview-mmm-indicator`
by an earlier session. The attestation and the artifact were never consulted against each other,
so that agreement is a real result.

**The 5 and 13 rows are not uncontested, and this is the finding of the session.**

> V07 `[00:25:34]`: *"The only other lines in here, look, **this yellow one is a five moving
> average.** I made it dotted in the 13, 50 and the 200."*

**Tier 1 says the 5 is yellow; the owner says the 5 is red and the 13 is yellow.** The utterance
was already on the record — `A-020` calls it *"the first time in the corpus a colour is attached
to a period in genuine audio"* — but **there was no owner colour mapping for it to contradict
until today**, which is why it had never been read this way.

**And the chain is the part that matters.** Owner: mustard = yellow. V07: yellow = 5. Joined:
**mustard = 5, ketchup = 13** — precisely the assignment `D-041` overturned, arriving by a
**second, independent route that starts from a recording** rather than from the Tier 3 table.

**Nothing was changed on it, for three reasons.** (1) **No speaker makes the join** — colour→period
is V07's, nickname→colour is the owner's, nothing gives colour→nickname on a single warrant, and
chaining them is the `D-030` error the tooling README already refuses for white/mayonnaise;
`SOURCING_HIERARCHY.md` §3.2 **Case C** governs — *do not adjudicate, surface to the owner*.
(2) **`D-041` was an explicit definitive owner ruling** and only the owner reverses it;
`REMEDIATION_PROTOCOL.md` §2 forbids the quiet edit in either direction. (3) **A cheap innocent
reading is live** — the V07 speaker is a **guest** who describes his own multi-timeframe palette
minutes later (`[00:27:24]`, `[00:27:33]`), so his colours may simply not be the course's.

**Filed as `SETUP_ISSUES.md` `I-011`, `OPEN`.** Deliberately **not** a `C-xxx`:
`CONTRADICTIONS.md` records course-source against course-source, and this is a course source
against an **owner attestation** — an adjudication question, not a doctrinal one.

### The temptation this session had, named because it was live

The instruction described the colour mapping as *"new, uncontested information, just add it."*
On three rows that is exactly right. On two it is not, and the fastest path was to take the
sentence at face value, ship red and yellow into the Pine defaults under a **strengthened**
warrant, and never open V07 at all — the file's own README says no colour for the 5 or 13 exists
in any source, so nothing would have looked wrong. **The conflict was only visible because the
colour search was run over the transcripts as part of the nickname sweep rather than as a
separate, skippable step.** That is worth remembering as a method point: sweeping for the
adjacent attribute costs nothing and is what caught this.

### A numbering collision, flagged not fixed

`feature/tradingview-mmm-indicator` holds `DRAFT_D-041_platform_artifacts.md` — a **different,
unadopted** draft (MT4 artifacts as parameter-only evidence) that reserved `D-041` when `D-040`
was the highest on integration. `D-041` is now taken. Exactly the collision `D-038a` consequence 1
predicts; the draft already says its number is provisional. **Renumbering is the adopting
session's act, not this one's.** Next free identifier: **`D-043`**.

### Files

- **Updated:** `00_SYSTEM/DECISIONS.md` (**`D-042`**, appended — `D-041` **not edited**, per the
  file's append-only rule); `00_SYSTEM/SETUP_ISSUES.md` (**`I-011`**, appended);
  `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` (`A-020` — two appended blocks + two Related rows);
  `00_SYSTEM/EXTERNAL_VOCABULARY_REFERENCE.md` §5.16 (search-negative note + colour table +
  conflict flag); `00_SYSTEM/SOURCING_HIERARCHY.md` §3.4 (re-check performed, result recorded);
  this log.
- **NOT touched, deliberately:** `00_SYSTEM/DECISIONS.md` `D-041` (append-only; and its mapping is
  correct as far as anything here shows); every block of superseded text in `A-020` and §5.16,
  retained unedited per `REMEDIATION_PROTOCOL.md` §2; `11_CONTRADICTIONS/CONTRADICTIONS.md`
  (reasoned above); `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md` (a colour is a label expansion, not a
  method concept — same `A-026` reasoning `D-041` used); `CHANGELOG.md` (no prior decision entry
  sets that convention); all `18_REVIEW/**` (`REVIEW_PROTOCOL.md` §11).

### Git

`git fetch --all` first; **zero divergence** against `origin/claude/add-documents-repository-fdfb3u`
confirmed before any edit. Paths staged **explicitly**; `git diff --staged` read in full before the
commit; **`git add -A` never used.** The two untracked directories present at session start
(`19_STUDENT_TEST_SUITE_V01_V10/`, `20_CHART_HEAVY_PRACTICAL_V01_V10/`) were **left untracked and
unstaged** — they are not this session's work.

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Action

**One owner sentence closes `I-011`.** *V07's guest says on tape the yellow line is the 5 EMA; you
have said the 5 is red and the 13 is yellow. Is he using his own colours, or is the 5 actually
yellow — which would also put ketchup back on 13?* If the owner confirms red/yellow, `I-011`
closes and V07 is annotated as a guest's private palette. If the owner reverses, that is a **new
decision entry superseding both `D-041` and `D-042` §2** — never an edit to either.

---

## 2026-08-13 — Reviewer Session (V11 R1) — INDEPENDENT AUDIT

**Branch:** `review/v11`, dedicated git worktree at
`/Users/randyschutt/Desktop/Trading/MMM-Agents-v11-review`, cut from the **integration** branch
(`e63e85e`) per `D-038`. **Act:** the independent review `D-003`/`D-004` require.

### ⭐ Independence — `D-003` SATISFIED, and the branch choice was deliberate

This session **authored no V11 artifact**. It cut from **integration rather than from
`video/v11`**, so the transcript, the frames and the quarantined tree could be read **before the
submission existed on the branch at all** — `REVIEW_PROTOCOL.md` §4's required review order,
enforced structurally rather than by intention. `origin/video/v11` was merged in only **after the
verdict was written and committed** at `c6ebbac`, so the evidence-ledger entries could be appended
on top of V11's own additions rather than spliced into a file that did not yet contain them.

**This is the first fully independent round since V09 R1.** V09 R2 and V10 R1's fix round were
both `SELF-VERIFIED AT OWNER DIRECTION` and both said so; this one is not, and the distinction is
recorded because the two preceding rounds made it worth recording.

### Verdict

```text
REVISE — 0 CRITICAL / 0 MAJOR / 5 MINOR / 7 NOTE.  Confidence HIGH.
GATE TO V12: OPEN (D-024, zero CRITICAL and zero MAJOR).
V11 STATUS:  IN REMEDIATION. Items 109-113 owed before COMPLETE.
```

**The gate to V12 is open and this review does not qualify that.** The owner has already begun
V12 on the correct reading of `D-024`, and **nothing found here is capable of contaminating it.**
The one finding that touches V12's own work-list — item 109 — makes that list *more* precise.

### What was re-derived rather than read

- **`PT-039`, END TO END.** `reviewer_pt039.py` was written from the pre-registration §§3–6 alone
  and parses the **raw HistData CSVs** directly — not the student's `_cache/m1_raw_v2.npz` — with
  its own DST rule, its own `C-1` labelling, its own 96-bucket gate, its own candidate detector,
  its own Wilson interval. **It shares no line with `run_pt039.py` or `mmm_lib`.**
  **Every number in all four cells reproduced exactly**: the `O1` curve to four decimal places,
  every `n(T)`, every Wilson bound, all six `N3` strata, `O3`/`O4`/`O5`, 894 / 777 session days,
  11 / 245 exclusions, `n_unresolved = 0`, one `FINAL` per day. **All four verdicts reproduce** —
  `M1a` PARTIAL (+15.80 pp), `M1b` CONFIRMED (+12.18 pp), `M1c` CONTRADICTED (no feature at 30 or
  90, both arms), `M1d` PARTIAL (3 of 6 strata).
- **Homework H6**: an independent Wilder RSI over the committed M15 file reproduced **all 36 cells
  to two decimal places**, including the `144.04×` spread.
- **`Q-012` §1**: the `diff` was re-run at source — **12 differing lines, 6 substitutions, ZERO
  content lines**, both files 69 lines. §3a's title card was **opened and looked at**: it is a
  title card. §3b's negative was re-derived — 21 `SCREENSHOT_001` files, **21 distinct MD5s**.
- **Lookahead**: re-derived rather than accepted. `held(T)` is logically identical to
  *"not superseded within `[t, t+T)`"* and is real-time knowable at `t+T`. **CLEAN.**
- **Host-vs-guest**: four strands confirmed at their markers, the handover scan re-run with a
  **17-pattern superset** (zero matches in 51 minutes), and **five further strands added** —
  including `[00:23:06]`'s **checkable back-reference to V01's own week-1 blue-box instruction**,
  the only cross-file strand in the determination and the one that most resists an impersonation
  hypothesis.
- **`A-080` on both admissible tiers**: every `rsi`/`tdi` line containing an integer was printed
  and inspected (three, none a lookback), and the 84-page Tier 2 extract was swept for any RSI
  numeral. **Both silent — verified, not repeated.**

### The five MINORs (items 109-113)

1. **⭐ 109** — the categorical *"no frame shows an indicator legend or a settings dialog"* is
   **FALSE** at six sites. **Frame 14 (`27:35`) carries `GBPUSD,H1`, `RSI(21)`, `ATR(14)`,
   `CCI(14)`, `MACD(12,26,9)`, `Sto(5,3,3)`, `Mom`, `AO`.** **`A-080`'s disposition is CORRECT and
   does not move** — the chart is the lesson's **disowned anti-example** on `H1`, and the
   instructor's own charts carry no legend at all — **but `RSI(21)` is a nearer near-miss trap than
   the `13` the record names, and it sits inside V11's own curated frames.** This is the one
   finding a reading-only review would not have produced.
2. **110** — `C-018`'s *"every unambiguous instance of 'the 50' is the sub-graph baseline"* is
   false: `[00:12:42]` *"out to the 50 in no time"*, fourteen minutes before RSI is introduced.
   **The correction RUNS IN THE CLAIM'S FAVOUR** — it is a fourth ground for reading B.
3. **111** — `pt039_output.txt` is still titled `PT-037`; the body must **not** be edited, a banner
   is owed. The only un-annotated stale reference in the tree.
4. **112** — `V11_MASTERY_REPORT.md:391` says *"V10 keeps `PT-039` and `PT-038`"*; must read
   `PT-037`. **Invisible to a `PT-037` grep** because the defect is that number's absence.
5. **113** — the run output prints two seeds (`20260812` banner vs `20260813` actual). No number
   affected; the durable fix is in `mmm_lib.provenance_header()` and is a policy-branch act.

### What was checked and found sound

**`C-018`'s closure is faithful to `D-041` in both directions** — no "Tier 0", no Tier 1 override,
`§3.4` stays live, superseded status retained, the inversion flagged not buried. **V10's
`PT-037`/`PT-038` numbering is verified untouched at every site**, `REVIEW_PROTOCOL.md` §11
intact, and `PT-040` is correctly **not** allocated. **Items 101 and 108 are accurate and not
understated** — Arm B's DST defect reproduces exactly (Mon 118 / Sat 117; 119 days at `92/96` and
118 at `4/96`; **64.8% of Mondays lost**), and `735a458` does contain zero `EVIDENTIAL` tokens
against a validator that enforces them. **Item 105's requested judgement is answered: `A-039`'s
narrowing is NOT generous, it is accurate, and item 105 can close.**

### `D-042` arrived mid-review, and the convergence is recorded

`D-042` (`195970d`) was committed to integration while this review was being written. It ran the
same nickname↔period search this reviewer ran, returned the same exhaustive negative, and **named
the same two near-hits independently** (V01 `[00:19:24]`'s garble, V10 `[00:37:02]`'s ordinary
English). **Two sessions, two branches, two search designs, one negative — `D-041` is doubly
verified rather than inherited.** `D-042` §3's new **colour** conflict (`I-011`) touches **no V11
artifact** and changes no finding here. Item 114 carries it.

### Git

Own branch, own worktree (`D-038`). Paths staged **explicitly**; `git diff --staged` read before
every commit; **`git add -A` never used.**

**⚠ `LOG.md` conflicted on the `video/v11` merge and the conflict was a FALSE-COMMON-CONTEXT
SPLICE** — `git` aligned two different session entries on their identical `### Git` / validator /
`### Next Action` boilerplate. Taking both sides in place would have welded integration's `D-041`
entry and `video/v11`'s entries into one entry with two Next Actions, which is the class of damage
the V10 merge-back had to repair. **Resolved by rebuilding from the parents rather than editing
the conflicted file**: both sides proved to be pure appends to a byte-identical 7,301-line prefix;
the three entries were reassembled **whole, contiguous and in true chronological order**, split
only at a heading boundary; and the result was **verified by multiset** — every line from both
sides present exactly once, none invented, none dropped. Record-ID sets re-derived after the
merge: **no duplicate `A-`, `C-`, `Q-` or `D-` identifier**, `REVIEW_INDEX` max item 108 before
this round's additions.

`scripts/validate_project.py`: **103 passed, 0 warnings, 0 failures.**

### Next Action

**Items 109-113 are owed before V11 can reach `COMPLETE`**, and they are documentation
corrections — none alters a method, a threshold, a disposition or a number. **V12 work is NOT held
by them** (`D-024`).

**Two things are handed forward.** (1) **Reviewer question 1 to the owner:** should
`mmm_lib.provenance_header()` print the *calling runner's* seed rather than the batch constant?
Every future `PT` that overrides the seed inherits item 113's contradiction. (2) **Item 109
sharpens V12's own instruction** — the V12 session is told to hunt frames for an
indicator-properties dialog, and it must check **whose chart** a legend belongs to before reading
a period off it.

**No question is put back to the owner on the `D-041` period mapping.** The escalation `D-041`
consequence 7 invited was checked independently and **declined**, and `D-042` §1 reached the same
conclusion.
