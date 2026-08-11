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
