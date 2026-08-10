# SETUP ISSUES

Inconsistencies, gaps, and open questions in the **project infrastructure** —
including places where the two governing files disagree.

This file is about the operating system of the project, not about the Market Maker
Method. Contradictions found *in the course* belong in
`11_CONTRADICTIONS/CONTRADICTIONS.md`.

Per the build instruction: where the governing files conflict, the conflict is
documented here rather than silently resolved. Provisional handling is applied so
work can proceed, and is marked as provisional.

Status values: `OPEN` / `PROVISIONALLY HANDLED` / `RESOLVED` / `ACCEPTED AS-IS`.

---

## I-001 — Two different status vocabularies for the same gate

**Status:** `RESOLVED` — provisional handling confirmed by the project owner,
2026-08-10 (see D-016)

**Conflict**

| Source | Vocabulary |
|---|---|
| Student file §21 (mastery report) | `PASS` / `REVIEW REQUIRED` / `BLOCKED` |
| Reviewer file §1 (review decision) | `PASS` / `REVISE` / `BLOCKED` |

The middle value differs, and both files say `PASS` gates progression:

- Student §21: *"Only `PASS` permits progression to the next lesson."*
- Reviewer §36: *"The Student Agent cannot certify itself as final authority.
  Reviewer `PASS` is the gate."*

Read literally, a student `PASS` both does and does not authorize advancement.

**Provisional handling**

The two vocabularies belong to two different actors and are kept distinct:

- The **student's** `PASS / REVIEW REQUIRED / BLOCKED` is a **self-assessment and a
  submission for review**. It never advances the course on its own.
- The **reviewer's** `PASS / REVISE / BLOCKED` is the **only** authorization.

`COURSE_PROGRESS.md` therefore carries two separate columns (`Student Mastery`,
`Reviewer`), and a lesson becomes `COMPLETE` only on reviewer `PASS`. This reading
satisfies Reviewer §36, which is the more specific statement about authority.

**Why this was not silently merged:** collapsing the vocabularies would either
delete the student's self-assessment step or imply the student can self-certify.
Both alter the governing design.

**RESOLUTION — 2026-08-10.** The project owner confirmed the two-vocabulary
reading. It is now binding, not provisional:

- Student mastery report status is `PASS` / `REVIEW REQUIRED` / `BLOCKED`, and is a
  self-assessment and submission for review.
- Reviewer decision is `PASS` / `REVISE` / `BLOCKED`, and is the sole authorization
  to advance.
- The two are never merged, and `COURSE_PROGRESS.md` keeps them in separate
  columns.

No implementation change was required — `MASTERY_STANDARD.md`,
`REVIEW_PROTOCOL.md`, and `COURSE_PROGRESS.md` already reflect this.

---

## I-002 — Review report filename is specified two ways

**Status:** `RESOLVED` — provisional handling confirmed by the project owner,
2026-08-10 (see D-016)

**Conflict**

| Source | Path |
|---|---|
| Reviewer file §7 | `18_REVIEW/VXX/VXX_REVIEW.md` |
| Reviewer file §31 | `V04_REVIEW_R1.md`, `V04_REVIEW_R2.md`, `V04_REVIEW_R3.md` |

§31 also says *"`V04_REVIEW.md` may contain or point to the latest accepted review
if desired"* — permissive, not directive — while insisting *"Never overwrite an
earlier review."*

**Provisional handling**

Versioned files are canonical: `18_REVIEW/VXX/VXX_REVIEW_R<n>.md`, one per round,
never overwritten. An optional `VXX_REVIEW.md` pointer file may be added but must
never replace the versioned files. This satisfies the non-negotiable requirement
(never overwrite) while remaining compatible with §7's directory layout.

**Impact:** low. `TEMPLATES/REVIEW_TEMPLATE.md` and `REVIEW_PROTOCOL.md` §11 use
the versioned form.

**RESOLUTION — 2026-08-10.** Confirmed by the project owner. Versioned files
`18_REVIEW/VXX/VXX_REVIEW_R<n>.md` are canonical and are never overwritten. An
optional `VXX_REVIEW.md` pointer to the latest accepted round is permitted but must
never replace the versioned files.

---

## I-003 — The two files specify different `00_SYSTEM/` contents

**Status:** `RESOLVED` — provisional handling confirmed by the project owner,
2026-08-10 (see D-016)

**Conflict**

| File | Present in Student §4 | Present in Reviewer §5 |
|---|---|---|
| `AGENT_ROLE.md` | ✅ | ✅ |
| `STUDY_PROTOCOL.md` | ✅ | ✅ |
| `MASTERY_STANDARD.md` | ✅ | ✅ |
| `COURSE_PROGRESS.md` | ✅ | ✅ |
| `DECISIONS.md` | ✅ | ✅ |
| `FILE_NAMING_STANDARD.md` | ✅ | ❌ |
| `SOURCE_MANIFEST.md` | ❌ (specified in §10 instead) | ✅ |
| `REVIEW_PROTOCOL.md` | ❌ | ✅ |

The Student file's tree also omits `18_REVIEW/`; the Reviewer file's tree omits
`.gitignore` and `CHANGELOG.md`.

**Provisional handling**

The **union** of both trees is created. Neither file forbids the other's
directories, and each omission is plainly a matter of scope (the Student file
describes the student's world, the Reviewer file the reviewer's). The Student
file's §10 explicitly requires `00_SYSTEM/SOURCE_MANIFEST.md` in prose even though
its tree omits it, which supports reading the trees as partial rather than
exclusive.

**Impact:** none. No content is lost by taking the union.

**RESOLUTION — 2026-08-10.** Confirmed by the project owner. The two trees are read
as partial views of one structure, and the union stands. Both governing files'
directory listings are treated as non-exhaustive going forward — a file absent from
one tree is not thereby forbidden.

---

## I-004 — "Do not progress" is stated at two different gates

**Status:** `RESOLVED` — provisional handling confirmed by the project owner,
2026-08-10 (see D-016). Related to I-001.

**Conflict**

Student §1.11 says do not progress until the lesson *"passes the mastery
standard"* (a student-side test). Reviewer §36 says the reviewer's `PASS` is the
gate. A student session reading only its own governing file could conclude it may
advance immediately after writing a `PASS` mastery report.

**Provisional handling**

Both conditions must hold, in order: the lesson must pass the student mastery
standard **and then** receive a reviewer `PASS`. The student mastery standard is a
precondition for *requesting review*, not for advancing.

`STUDENT_SESSION_PROMPT.md` makes this explicit as a hard stop, so a student
session cannot reach the wrong conclusion from its governing file alone.

**RESOLUTION — 2026-08-10.** Confirmed by the project owner. Both conditions must
hold, in this order:

```text
1. lesson passes the student mastery standard   → authorizes REQUESTING REVIEW
2. lesson receives a reviewer PASS              → authorizes ADVANCING
```

Passing the mastery standard never advances the course by itself. This is now
binding and is enforced in `STUDENT_SESSION_PROMPT.md`, `SESSION_START.md` §6, and
`COURSE_PROGRESS.md`.

---

## I-005 — Source videos are not yet available

**Status:** `OPEN` — blocking Phase 1

Not a governing-file conflict; recorded here because it blocks the project.

The infrastructure build session had no access to the bootcamp video library.
Consequently: `SOURCE_MANIFEST.md` has zero rows, `COURSE_PROGRESS.md` has zero
lesson rows, and no course content exists anywhere in the repository.

**Resolution requires:** the project owner making the video library locally
accessible to an agent session, then a Student session running
`SOURCE_INGESTION_PROTOCOL.md`.

**Expected but unverified:** ~21 usable lesson videos in a folder of ~24 files.
Recorded as an expectation only (see `DECISIONS.md` D-014).

---

## I-006 — Screenshot capture may require human assistance

**Status:** `RESOLVED` 2026-08-10 — a working, repeatable capture path exists (see the second update below)

Both governing files treat screenshots as first-class evidence, and the reviewer
audits chart recognition against them. Whether an agent session can capture frames
from the source videos depends on the tooling available in the environment
(e.g. `ffmpeg` for frame extraction) — this is unknown until the videos and the
runtime are both present.

**If frame extraction is unavailable**, the options are: the project owner captures
screenshots manually at agent-specified timestamps, or the agent works from
detailed timestamped visual descriptions and records the limitation in every
affected artifact. The second option materially weakens the evidence base and must
be flagged to the reviewer, not hidden.

**Do not** substitute generated, illustrative, or reconstructed images for real
course screenshots under any circumstances.

### Update 2026-08-10 — investigated at V01, still `OPEN`, cause now understood

`ffmpeg` and `ffprobe` are both present. They are not sufficient, and the reason is
structural rather than a tooling gap:

- `ffmpeg` aborts on these files after roughly two minutes with
  `pixel format change unsupported`.
- Parsing the SWF tag stream directly shows why. V01 contains 9,853 `SHOWFRAME` tags
  (3.0 fps × 3,284 s — the full 54:44) but **no video stream**. The screen is
  composited from bitmap tiles placed on a display list: 389 `DefineBitsJPEG2`, 603
  `DefineBitsLossless`, 658 `DefineShape3`, 537 `PlaceObject2`. Extracting the image
  tags directly yields one full 1024×768 keyframe at `00:00:00` and 388 delta tiles
  of 26×38 to 72×56 pixels — cursor sprites and changed regions, not frames.
- Producing viewable frames therefore requires **evaluating the display list**, i.e.
  a Flash renderer. No `ffmpeg` invocation will do it.
- Ruffle was checked and ruled out inside its time box. Release v0.5.0 ships
  `ruffle-0.5.0-macos-universal.tar.gz`, a GUI desktop player; there is no headless
  exporter asset. Frame export lives only in the `ruffle_exporter` crate, which means
  a from-source Rust build — out of bounds after it hung a prior session. No download
  was made.

**Live route:** CloudConvert, converting `.swf` to a real video container that
`ffmpeg` can then sample normally. Blocked until the project owner is at his own
machine (expected Thursday). Nothing else in the project is blocked behind this.

**Interim handling:** V01's artifacts were produced from the transcript alone and say
so, in `V01_SOURCE_NOTES.md` §4, `V01_INTERPRETATION.md` §9 item 1, and
`04_SCREENSHOTS/V01/INDEX.md`. No item in `V01_INTERPRETATION.md` is classified
`VISUAL`, because nothing visual was seen. The approved TradingView-recreation
fallback has **not** been started; when it is, recreations go to `09_CHART_EXAMPLES/`
with sidecars, never to `04_SCREENSHOTS/`.

### RESOLUTION 2026-08-10 — Ruffle (WASM) in headless Chrome

The renderer that `ffmpeg` lacks exists as WebAssembly. Ruffle's `web-selfhosted`
build, served over `http://` and driven by Playwright, renders these SWFs correctly at
full 1024×786.

Full method, commands and gotchas: **`00_SYSTEM/SWF_CAPTURE_RECIPE.md`**.

Outcome for V01: a 54:44 mp4 with the SWF's own audio, sync verified against the
player's burned-in timecode at twelve points across the full runtime — all twelve exact,
zero drift. 22 curated screenshots extracted and indexed in
`04_SCREENSHOTS/V01/INDEX.md`. Four previously undefined terms were resolved or
materially constrained by text printed on slides that was never spoken aloud.

Routes ruled out, recorded so they are not retried:

| Route | Verdict |
|---|---|
| `ffmpeg` frame extraction | Impossible. No video stream; a composited bitmap display list. |
| Direct SWF tag parsing | Yields one keyframe plus delta tiles, not frames. |
| Ruffle desktop binary | GUI player only; no headless exporter in the release. |
| Building `ruffle_exporter` from source | **Forbidden** — hung a prior session. |
| Ruffle JS seek API | Does not exist. `goto_frame` / `seek` / `current_frame` are internal Rust symbols, absent from the JS bundle. |
| SWF `ExternalInterface` | Dead end. This SWF registers zero callbacks (`addCallback` appears 0 times in its AS2 string pool). |
| Camtasia scrubber drag | Works but lands imprecisely and non-linearly. Usable only closed-loop. |

The approved TradingView-recreation fallback is **no longer needed for screenshots**. It
remains available for illustrating concepts, and if used must go to
`09_CHART_EXAMPLES/` with sidecars, never to `04_SCREENSHOTS/` — the prohibition below
on substituting generated images for real course screenshots is unchanged.

**Cost:** capture is real-time, ~1 hour per video. An untested faster path (patching the
SWF header frame rate in a working copy) is described in the recipe.

---

---

## I-007 — Manual backtesting requires a chart data source

**Status:** `OPEN` — to be resolved before the first manual backtest

Manual backtesting on GBP/USD requires historical chart access with the ability to
hide future candles at the decision point (e.g. TradingView bar replay). Whether an
agent session can drive such a tool, or whether the project owner performs the
chart-walking with the agent directing and recording, is undetermined.

This affects the credibility of every manual backtest record, so it must be decided
and recorded in `DECISIONS.md` — including the data source, broker/feed, timezone,
and timeframes — before observations are collected. See `STUDY_PROTOCOL.md` §6
(reproducibility).

---

## HOW TO USE THIS FILE

- A **new session** should read this file during session start. An `OPEN` issue may
  block or reshape the planned work.
- A **reviewer** should check whether a lesson's work depends on an unresolved
  setup issue before issuing `PASS`.
- **Resolving an issue** means appending the resolution and changing the status —
  not deleting the entry. The history of how the project's rules were settled is
  part of the audit trail.
- New infrastructure conflicts get the next `I-0XX` number.

---

## I-008 — Twenty of twenty-one transcripts are unverified

**Status:** `OPEN` — must be resolved per-lesson, before that lesson is studied
**Progress:** V01 verified 2026-08-10. **V02 verified 2026-08-10** (see below).
19 remaining: V03–V21.

Each lesson folder arrived with a `TRANSCRIPT.md` produced by a pre-ingestion process
— the same process that produced the `NOTES.md`, `RULES.md`, and `VISUAL_INDEX.md`
files subsequently found to be fabricated and quarantined
(`00_SYSTEM/QUARANTINE_REGISTER.md` Q-001).

**V01's transcript was checked and passed.** Length matches measured audio (final
timestamp `[00:54:38]` against 00:54:43.8), timestamps are monotonic, and it preserves
its own ASR errors, crosstalk, and off-topic stretches rather than smoothing them —
a fabricated transcript does not invent its own mishearings. It was adopted and now
lives at `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md` with the verification recorded in its
header.

**V02 was checked on 2026-08-10 and passed.** It was tested against all four criteria
below, including the audio spot-check that V01's verification did not perform
mechanically: four 60-second windows (`00:03:00`, `00:20:00`, `00:40:00`, `00:59:00`)
were independently re-transcribed from the extracted audio with Whisper `small.en` and
compared against the corresponding transcript entries. All four matched near-verbatim,
including low-frequency specifics a fabricator would not invent. Divergences were
ASR-vs-ASR only. 1,026 timestamps, strictly monotonic, final entry `[01:00:16]` against
a measured 3619.81 s. Adopted at `02_TRANSCRIPTS/V02/V02_TRANSCRIPT.md`.

Note that V02's transcript passed while the three derived files **in the same folder**
were confirmed fabricated the same day (`QUARANTINE_REGISTER.md` Q-002). Two for two,
the transcripts have been sound and the derived notes have not. That is a useful prior
for V03–V21 but it is not a substitute for the check — the point of I-008 is that
provenance is not evidence in either direction.

**V03–V21 have not been checked.** There is no evidence against them and none for
them. Sharing a provenance with fabricated material is not proof of fabrication, but
it is enough that adoption without checking would be negligent.

**Cost, now measured:** the V02 check took about 12 minutes end to end, most of it
unattended Whisper runs, and it was performed while the screen capture recorded in the
background. It is not an expensive gate.

**Required before each lesson is studied**, at minimum:

1. Final timestamp against the measured duration in `SOURCE_MANIFEST.md`.
2. Timestamps monotonic, with no implausible gaps.
3. Spot-check several passages against the actual audio.
4. Confirm the content is consistent with a live webinar rather than a clean summary
   — disfluency, crosstalk, and administrative stretches present.

A transcript that fails these is quarantined and re-transcribed, not repaired.

**Why this is not resolvable in bulk now:** study is strictly sequential and gated
(`SOURCE_INGESTION_PROTOCOL.md` §10). Verifying V03–V21 today would front-load work
ahead of the lessons that need it. The audio route is now settled — `ffmpeg -vn -c copy`
straight off the `.swf`, no third-party conversion — so the earlier concern about
redoing the work if the audio route changed no longer applies; the remaining reason to
keep this per-lesson is sequencing, not risk.

---

## I-009 — Concurrent sessions share this machine and this repository, and they collide

**Status:** `OPEN` — mitigations adopted (D-022), root condition remains

Three agent sessions ran against this checkout on 2026-08-10: the V02 student session,
a V01 review R1 session, and a V01 review R2 session. They are not isolated from each
other, and two distinct collisions caused real damage.

### Collision 1 — a stale HTTP server served the wrong lesson for an hour

The V01 session left `python3 -m http.server 8899` running. `SWF_CAPTURE_RECIPE.md` §2
told the V02 session to serve on 8899. `python3 -m http.server` **exits silently when
the port is busy**, so the V02 server never started, and every request went to the V01
session's server — whose `index.html` is hardcoded to `v01.swf` and ignores the `?swf=`
parameter.

Consequences: a 61-minute capture of the wrong lesson; a frame-rate experiment whose
treatment and control were the same unpatched file, producing a confident false negative
recorded as D-020; a false conclusion that V02's `.swf` contained V01's video; and a
false survey suggesting all 21 lessons declare a 54:44 duration.

Nothing in the failure looked like a failure. The page loaded, Ruffle initialised,
playback ran, the timecode burned in, and a valid hour-long `.webm` was produced.

**What caught it:** the slides did not match what the instructor was saying at that
timestamp. **Mitigations:** D-022 (verify the port owner and the served bytes; unique
filename per served file; check content against the transcript before any long capture)
and `SWF_CAPTURE_RECIPE.md` GOTCHA 4.

### Collision 2 — `git add -A` cross-commits other sessions' work

Sessions sharing one working tree that each run `git add -A` will commit each other's
in-progress files under their own commit messages. Observed:

| Commit | Message | Also contained |
|---|---|---|
| `6e4adac` | "adopt V02 transcript and record Q-002" | authored by the *review* session, not the V02 session |
| `4068db7` | "apply V01 review R1 corrections" | `V02_SOURCE_NOTES.md`, `V02_INTERPRETATION.md` |
| `58e3d03` | "correct stale RECORDS:0 status" | the 422-line A-019…A-025 block |

No content was lost, but authorship and grouping in the history are wrong, so `git log`
no longer identifies which session produced which artifact.

**Mitigation:** stage explicit paths. **Never `git add -A` in this repository** while
concurrent sessions are possible. Check `git status --porcelain` before staging and
leave anything you did not write alone.

### Residual risk

These mitigations are conventions, not enforcement. A session that does not read this
file will repeat both failures. The durable fixes — one working tree per session (git
worktrees), and a port derived from the lesson number — are recommended but not yet
adopted.
