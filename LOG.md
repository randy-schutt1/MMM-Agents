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
