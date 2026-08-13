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
