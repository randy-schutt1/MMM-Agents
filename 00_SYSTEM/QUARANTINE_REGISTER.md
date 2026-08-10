# QUARANTINE REGISTER

Material found alongside the source library that **must not be used as evidence**,
what was wrong with it, and where it now lives.

This file is the Git-visible record. The quarantined files themselves sit under
`01_SOURCE_VIDEOS/`, which `.gitignore` excludes, so they are preserved on disk but
not committed.

---

## Q-001 — Pre-ingestion derived notes for all 21 lessons, and a synthesized master rulebook

```text
STATUS:        QUARANTINED — DO NOT USE
DATE:          2026-08-10
QUARANTINED BY: Student session (first ingestion run)
DECISION:      D-017
```

### What

| Files | Count | Original location | Now at |
|---|---|---|---|
| `NOTES.md`, `RULES.md`, `VISUAL_INDEX.md` | 63 (3 × 21 lessons) | `.../Bootcamp Notes/NN_.../` | `.../Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/NN_.../` |
| `MASTER_RULEBOOK.md`, `MASTER_GLOSSARY.md`, `SETUP_CATALOG.md`, `COURSE_SYNTHESIS.md`, `COURSE_INDEX.md`, `CONTRADICTIONS.md`, `AMBIGUITIES_AND_QUESTIONS.md`, `SCRIPT_REQUIREMENTS.md` | 8 | `.../Bootcamp Notes/00_MASTER/` | `.../_QUARANTINE_UNVERIFIED_NOTES/00_MASTER_rulebook/` |
| `Forex_Bootcamp_Complete_Training_Notes.md` | 1 | `.../Forex Bootcamp/` | `.../_QUARANTINE_UNVERIFIED_NOTES/00_MASTER_rulebook/` |

A `README_WHY_QUARANTINED.md` was written into the quarantine folder so the warning
travels with the files.

### Why — evidence

All three findings are against V01, the only lesson whose transcript has been
verified against its audio.

**Finding 1 — a rule cited to a timestamp that says nothing of the kind.**

`01_.../RULES.md` records `V01-R001` at `[00:05:00]`, quoted as the instructor
saying *"Wait for the M15 candle to close before taking the 5/13 EMA cross"*,
marked `Source: Explicit` and `Coding Readiness: Ready`.

The transcript from `[00:04:51]` to `[00:05:32]` is the instructor telling students
not to rush homework in the hour before class. No chart content appears in that
range. Across the whole 54:44 transcript, `EMA` matches 14 times; 13 are the
substring in *email*. The one real occurrence is `[00:19:15]` — *"Do you know how to
read the EMAs in real time?"* — item 10 of a student self-assessment survey. It
states no periods, no cross condition, and no candle-close requirement.

The same file's parameter table sources EMA periods 5 / 13 / 50 / 200 / 800 to
`[00:04:00]`, all marked `Explicit`. Nothing at `[00:04:00]` concerns moving
averages.

**Finding 2 — a visual index for screenshots that were never taken.**

`01_.../VISUAL_INDEX.md` claims "Total Captured Presentation & Annotated Chart
Screenshots: 78" and describes 78 numbered images with filenames, byte sizes, and
per-image descriptions of what is on screen. The lesson's `SCREENSHOTS/` folder
holds **one** image, whose name matches none of the entries.

**Finding 3 — the master rulebook predates ingestion.**

`MASTER_RULEBOOK.md` states `MR-001` … `MR-005` (5/13 EMA cross entry, 10–15 pip
stops beyond HOD/LOD, minimum 1:3 R:R, London 03:30–09:00 EST / New York
09:30–12:00 EST) each marked `Source: Explicit`, none carrying a video ID or
timestamp. It is a Phase-3-shaped consolidated specification produced before Phase 1
had run. Its relationship to the wider Beat The Market Maker literature is not the
issue; it is not derived from these source files and must not be cited as though it
were.

### Pattern

Plausible domain knowledge about the method, formatted in this repository's evidence
conventions, with timestamps attached that do not correspond to what is said at those
timestamps. This is more damaging than having no notes at all: it defeats the
source-traceability the project is built on, and it is specifically the failure mode
`00_SYSTEM/TEMPLATES/INTERPRETATION_TEMPLATE.md` exists to prevent.

### Not quarantined

`TRANSCRIPT.md` files were left in their lesson folders.

- **V01's transcript is verified and in use.** 2,930 lines, monotonic timestamps
  `[00:00:00]` → `[00:54:38]`, against a measured audio duration of 54:43.8. It
  preserves disfluency, crosstalk, student names, and ASR garble rather than
  smoothing them — a fabricated transcript does not contain its own transcription
  errors. **Copied** to `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md`.

> **CORRECTED 2026-08-10 (review R1 finding 12, `E20`).** This line read *"Relocated to
> `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md`"*, which was never accurate: the original file
> remains at
> `01_SOURCE_VIDEOS/.../01_Bootcamp1_Wk1_031812_Part1_55mins/TRANSCRIPT.md` (git-ignored,
> preserved on disk). It was copied, not moved. The two files are no longer identical
> either — the working copy has since gained the homework, screenshot-moment and
> transcription-notes appendices, so it is 3,097 lines against the original's 2,930. The
> **spoken content** is unchanged; only appendices were added. The original is retained
> deliberately as the untouched artifact.
- **The other 20 transcripts are UNVERIFIED.** No evidence against them, and none
  for them. Each must be checked against its own audio before that lesson is
  studied. Tracked as issue I-008.

### Handling rule

Do not mine this material for leads. A fabricated rule that happens to be correct is
still not evidence, and going looking for it in a transcript is how a session talks
itself into finding it. The files are retained only as the record of what was
discarded and why.

---

## Q-002 — V02's three derived files, checked individually and confirmed fabricated

```text
STATUS:        QUARANTINED — DO NOT USE (confirmed, not assumed)
DATE:          2026-08-10
QUARANTINED BY: Student session (V02)
DECISION:      D-017 (Q-001 blanket action), now confirmed for V02 specifically
```

### Why this entry exists separately

Q-001 quarantined all 63 per-lesson files on evidence drawn from **V01 only**. For
V02 that was a precaution, not a finding. Before writing V02's notes this session
checked V02's own three files against V02's own verified transcript. They fail, and
they fail in the same way. This entry records the V02-specific evidence so that no
later session has to take the blanket action on trust.

Files: `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/02_Bootcamp1_Wk1_031812_Part2_60mins/`
— `NOTES.md` (18 lines), `RULES.md` (69 lines), `VISUAL_INDEX.md` (453 lines).

### Finding 1 — V02's "explicit" rules are V01's fabricated rules, re-stamped

`V02-R001` is recorded at `[00:05:00]`, quoted as the instructor saying
*"Wait for the M15 candle to close before taking the 5/13 EMA cross"*, marked
`Source: Explicit`, `Coding Readiness: Ready`.

This is **the same sentence, at the same timestamp, with the same two fields**, as
the fabricated `V01-R001` documented in Q-001 Finding 1. The parameter table beneath
it sources EMA periods 5 / 13 / 50 / 200 / 800 to `[00:04:00]` marked `Explicit` —
again identical to V01's. The generator was stamping a template across lessons, not
transcribing them.

What V02's transcript actually says in those places:

| Cited | Claim | What is actually said there |
|---|---|---|
| `[00:04:00]` | five EMA periods, `Explicit` | *"I bestow upon you trend traders… start looking for the anchor points."* No moving average of any kind. |
| `[00:05:00]` | M15 close before 5/13 EMA cross | *"You should not be looking for longs… What I see is the M here… You always get out on Friday."* No indicator, no timeframe, no candle-close condition. |
| `[00:18:00]` | stop loss 10–15 pips beyond HOD/LOD, `Explicit` | *"False move week beginning… Asian session… peak formation low… DNC. Do not counter trade back into the range."* No stop distance is stated. |
| `[00:22:00]` | "Peak Time Gap 30–90 mins", `Explicit` | *"…he issues a beautiful 33 trade… fills the ADR completely."* No timing gap is stated. |

### Finding 2 — the vocabulary the rules are built from is absent from the lesson

Counted across the full 3,619-second transcript:

```text
"EMA"            8 matches — all 8 are the substring inside "email" / "emails".
                            Zero real references to a moving average by that name.
"M15"            0        "5/13"            0        "moving average"  0
"Asian box"      0        "TDI"             0        "shark fin"       0
"railroad"       0        "pin bar"         0
"mustard"        0        "blueberry"       0        "raspberry"       0
```

`NOTES.md` nonetheless states an EMA colour scheme
(*5 Mustard, 13 Water, 50 Mayo, 200 Blueberry, 800 Raspberry*), a TDI "Shark Fin"
signal, and Asian/London/New York session clock times to the half-hour. None of it
is in this recording. **One caveat, recorded so it is not lost:** the instructor does
say *"mayonnaise"* three times (`[00:19:46]`, `[00:25:18]`, `[00:25:45]`) as a
nickname for a moving average visible on his chart. So the food-nickname system is
real in this course — but V02 never states which average "mayonnaise" is, and the
other four names never occur. The quarantined mapping remains unsourced, and the
existence of one true-sounding fragment inside a fabricated list is exactly why the
Q-001 handling rule forbids mining this material for leads.

### Finding 3 — a 50-entry visual index for one image

`VISUAL_INDEX.md` opens *"Total Captured Presentation & Annotated Chart Screenshots:
50"* and describes 50 numbered images with filenames, byte sizes, timestamps and
per-image descriptions. The lesson's `SCREENSHOTS/` folder contains **one** file.

That one file is real: `VIDEO_02_SCREENSHOT_001.jpg`, 82,843 bytes — matching entry
001's claimed size exactly. Entries 002–050 describe 49 files that do not exist and
never did, with invented byte sizes. And entry 001's *description* is still wrong:
it is titled "Weekly Cycle Anatomy & 22-Trade Setup Diagram", whereas the image is a
slide headed **"Typical Week"** showing an annotated GBPUSD M15 chart. Its claimed
timestamp `[00:01:15]` is unverified — the image is a 1024×768 crop with no control
bar, so it carries no burned-in timecode to check against.

### Disposition

All three files stay quarantined. `TRANSCRIPT.md` from the same folder was checked
independently and **passed** — it is adopted at `02_TRANSCRIPTS/V02/V02_TRANSCRIPT.md`
(I-008 satisfied for V02). `VIDEO_02_SCREENSHOT_001.jpg` is a genuine frame of this
lesson and may be looked at, but nothing written *about* it in `VISUAL_INDEX.md` may
be cited.

### What this implies for V03–V21

Two of two lessons checked have fabricated derived files built from a shared template.
The blanket quarantine is now supported by evidence at both ends it has been tested.
Each remaining lesson should still be confirmed individually — the check costs about
ten minutes once the transcript is verified — but a session finding the same pattern
in V03 should treat it as expected rather than surprising.
