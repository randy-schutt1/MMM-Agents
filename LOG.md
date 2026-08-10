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
