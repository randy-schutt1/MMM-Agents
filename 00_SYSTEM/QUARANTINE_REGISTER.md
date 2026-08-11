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

---

## Q-003 — V03's three derived files, checked individually and confirmed fabricated

```text
STATUS:        QUARANTINED — DO NOT USE (confirmed, not assumed)
DATE:          2026-08-10
QUARANTINED BY: Student session (V03)
DECISION:      D-017 (Q-001 blanket action), now confirmed for V03 specifically
```

### Why this entry exists separately

Same reason as Q-002: the Q-001 blanket quarantine was evidenced on V01 only. Before
writing V03's notes this session checked V03's own three files against V03's own
verified transcript. They fail, and they fail in the same template-stamped way as V01's
and V02's. Three of three lessons checked now carry individually confirmed fabrications.

Files: `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/03_Bootcamp1_Wk2_032512_Part1_71mins/`
— `NOTES.md` (18 lines), `RULES.md` (69 lines), `VISUAL_INDEX.md` (25 lines).

### Finding 1 — the same fabricated rules, stamped a third time

`RULES.md` records `V04-R001` (note the ID: the generator still used the pre-D-017
alphabetical misordering under which this lesson was "Video 04") at `[00:05:00]`,
quoted as the instructor saying *"Wait for the M15 candle to close before taking the
5/13 EMA cross"*, marked `Source: Explicit`, `Coding Readiness: Ready`.

This is **the same sentence, at the same timestamp, with the same two fields** as the
fabricated `V01-R001` (Q-001 Finding 1) and `V02-R001` (Q-002 Finding 1). The parameter
table beneath it sources EMA periods 5 / 13 / 50 / 200 / 800 to `[00:04:00]` marked
`Explicit`, a stop-loss of 10–15 pips beyond HOD/LOD to `[00:18:00]`, and a "Peak Time
Gap 30–90 mins" to `[00:22:00]` — all identical to the V01/V02 fabrications.

What V03's verified transcript actually carries at those places:

| Cited | Claim | What is actually said there |
|---|---|---|
| `[00:04:00]` | five EMA periods, `Explicit` | *"Okay, quarter of the week. Very important."* — the "one trade should not define you" talk. No moving average of any kind. |
| `[00:05:00]` | M15 close before 5/13 EMA cross | *"…move on to the next segment of the journey… Let me do it in mail."* (mail segment begins). No indicator, no timeframe, no candle-close condition. Not even a marker — nearest are `[00:04:54]` and `[00:05:01]`. |
| `[00:18:00]` | stop loss 10–15 pips beyond HOD/LOD, `Explicit` | *"They rise most of the time three levels textbook. They pull back and the day back in consolidation."* No stop distance is stated. |
| `[00:22:00]` | "Peak Time Gap 30–90 mins", `Explicit` | *"…drill down to the mini view intraday looking for the stop hunt and then the micro view understanding the pushes."* No timing gap is stated. |

Counted across the full 4,243-second transcript: `M15` 0 matches, `5/13` 0 matches,
`EMA` 1 real match outside *email* (`[00:57:54]`, "Stop onto the 50 EMA out of the
mail" — a single flashcard caption, not a parameter list), and none of the colour
names (*mustard, water, mayo-as-colour-scheme, blueberry, raspberry*) occur.

### Finding 2 — the new hazard: this time some of the fabricated vocabulary is real

Unlike V02, where the fabricated files' vocabulary (TDI, shark fin, session tables) was
almost entirely absent from the recording, **V03 genuinely discusses TDI (13 mentions),
shark fin (3), railroad tracks (5), and stop hunts (8)**. The fabricated `NOTES.md`
happens to name real V03 subjects — while still fabricating everything specific it says
about them:

- `NOTES.md` defines the TDI signal as *"Green Price Line crossing Red Signal Line
  after breaking outside Blue Volatility Bands (Shark Fin)"*. The transcript never
  states line colours or a crossing rule; what it states is position-based
  (`[00:45:35]`–`[00:45:54]`: outside the volatility band and beyond the support/
  resistance bands ⇒ "probably level three") and the instructor explicitly defers TDI:
  *"I am going to cover TDI later"* `[01:01:53]`.
- `NOTES.md` gives session clock times to the half-hour (Asian 7:00 PM–3:00 AM EST,
  London 3:30–9:00 AM, NY 9:30 AM–5:00 PM). No session table is stated anywhere in
  V03's audio.
- `NOTES.md` claims *"Time Gap: 30 to 90 minutes between peak 1 and peak 2"* — never
  stated in V03.
- *"Asian Box"*, the headline topic, is never spoken in this recording (the spoken
  terms are "Asian range" and "the first eight hours").

This makes V03's fabrications **more** dangerous than V02's, not less: a future session
skimming both the notes and the transcript would find the vocabulary corroborated and
could be tempted to import the fabricated specifics. The Q-001 handling rule (do not
mine quarantined material for leads) matters most exactly here.

### Finding 3 — a 3-entry visual index for one image, and the one entry is wrong

`VISUAL_INDEX.md` describes 3 numbered screenshots. The lesson's `SCREENSHOTS/` folder
contains **one** file, `VIDEO_04_SCREENSHOT_001_00-02-00.jpg` — entries 002 and 003
describe files that do not exist. Entry 001's description (*"Asian Box accumulation
range with 5, 13, 50, 200, and 800 EMAs"*) does not match this session's verified
capture of `[00:02:00]` (sweep frame at burned timecode `01:59`), which shows the
housekeeping slide titled "Managing Your Expectations" ("I expect you to: Follow along
free from distraction… Give me 2 Hrs a week!…"), not a chart. Its filename timestamp is
additionally
unverifiable — the image is a 1024×768 crop with no control bar and no burned-in
timecode.

### Disposition

All three files stay quarantined. `TRANSCRIPT.md` from the same folder was checked
independently and **passed** — it is adopted at `02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md`
(I-008 satisfied for V03). `VIDEO_04_SCREENSHOT_001_00-02-00.jpg` is a plausible frame
of this lesson but its timestamp claim is unverified and nothing written about it in
`VISUAL_INDEX.md` may be cited.

### Running tally for the fabrication pattern

V01, V02, V03: three of three lessons individually confirmed. The generator stamped one
template across lessons, re-using the same fabricated sentences and timestamps
regardless of content. Sessions processing V04–V21 should continue to confirm
individually (the check costs ~10 minutes once the transcript is verified) and should
treat finding the same pattern as expected.

---

## Q-004 — V04's three derived files, checked individually and confirmed fabricated; plus the first mechanical proof that ONE template was stamped across all 21 lessons

```text
STATUS:        QUARANTINED — DO NOT USE (confirmed, not assumed)
DATE:          2026-08-10
QUARANTINED BY: Student session (V04)
DECISION:      D-017 (Q-001 blanket action), now confirmed for V04 specifically
```

### Why this entry exists separately

Same reason as Q-002 and Q-003: the Q-001 blanket quarantine was evidenced on V01 only,
and each lesson's own files are re-checked against that lesson's own verified transcript
before its notes are written. V04's three files fail, in the same template-stamped way.
**Four of four lessons checked now carry individually confirmed fabrications.**

Files: `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/04_Bootcamp1_Wk2_032512_Part2_86mins/`
— `NOTES.md` (18 lines), `RULES.md` (69 lines), `VISUAL_INDEX.md` (25 lines).

### Finding 1 — NEW: the template is now proven mechanically across all 21 lessons at once

Q-001, Q-002 and Q-003 each established the fabrication for one lesson and *inferred* that
the same generator produced the rest. **That inference is now a measurement.** Two greps
over the whole quarantine tree:

```text
$ grep -rl "Wait for the M15 candle to close before taking the 5/13 EMA cross" \
      _QUARANTINE_UNVERIFIED_NOTES/per_lesson/ | wc -l
21
$ grep -rl "Place your stop loss 10 to 15 pips beyond the High or Low of the Day" \
      _QUARANTINE_UNVERIFIED_NOTES/per_lesson/ | wc -l
21
$ ls _QUARANTINE_UNVERIFIED_NOTES/per_lesson/*/RULES.md | wc -l
21
```

**All 21 `RULES.md` files carry both sentences, and both are presented as
`Source: Explicit` verbatim instructor statements at the same two timestamps —
`[00:05:00]` and `[00:18:00]` — in every one of them.** The 21 lessons are 21 different
recordings, on 10 different dates, running 43 to 96 minutes. No instructor says the same
two sentences at the same two clock times in 21 consecutive sessions.

This is worth stating plainly because it retires an open question rather than re-answering
a settled one: **no further per-lesson fabrication audit can turn up a clean `RULES.md`.**
The remaining per-lesson checks (V05–V21) are still worth their ~10 minutes for the
*other* two files and for lesson-specific hazards like Finding 3 below, but the
`RULES.md` verdict is now known in advance for every one of them.

### Finding 2 — the fabricated content against V04's own verified transcript

`RULES.md` records `V05-R001` — note the ID: the generator still used the pre-D-017
alphabetical misordering under which this lesson was "Video 05" (Q-003 saw the same
off-by-one in the other direction, V03's files carrying `V04-` IDs).

What V04's verified transcript actually carries at the cited places:

| Cited | Claim | What is actually there |
|---|---|---|
| `[00:02:00]` | screenshot of "Asian Box accumulation range with 5, 13, 50, 200, 800 EMAs" | The **"4-Trades"** slide (Stop Hunt High "M" Formation / Stop Hunt Low "W" Formation / Straight Away Rise / Straight Away Drop). No chart, no moving average. Verified against this session's own capture. |
| `[00:04:00]` | five EMA periods, `Explicit` | **Not a marker.** Nearest are `[00:03:56]` and `[00:04:01]`, both mid-sentence in *"if the dealer takes your money away from you… you hit them again. You don't go on vacation. Control the losses to a reasonable amount."* No indicator of any kind. |
| `[00:05:00]` | M15 close before 5/13 EMA cross | **Not a marker.** Nearest are `[00:04:59]` and `[00:05:03]`: *"If you take minus eighteen, you're out and then the dealer does this. / Again, you got them."* No indicator, no timeframe, no candle-close condition. |
| `[00:15:00]` | screenshot of "London Open Stop Hunt false breakout forming 2nd leg M-formation at High of Day" | **Not a marker.** Nearest are `[00:14:58]` (*"Do not take any more garbage trades inside the range of the blue box"*) and `[00:15:05]` (*"Are you going to miss some good setups?"*). |
| `[00:18:00]` | stop loss 10–15 pips beyond HOD/LOD, `Explicit` | A real marker — and it is the **homework assignment**: *"But I want you to do the assignment in the four hour chart."* No stop distance is stated. |
| `[00:22:00]` | "Peak Time Gap 30–90 mins", `Explicit` | **Not a marker.** Nearest are `[00:21:59]` and `[00:22:02]`, mid-sentence in *"…that's your peak formation high, then you're looking for stop on high drop, stop on high drop W get out."* No timing gap is stated anywhere in the lesson. |
| `[00:30:00]` | screenshot of "TDI Shark Fin … + 5/13 EMA cross" | **Not a marker.** Nearest are `[00:29:57]` and `[00:30:01]`, mid-digression about how many pairs the guest presenter watches (*"…and so this was my son, Ken"*). |

**Six of the seven cited timestamps are not transcript markers at all.** The one that is
carries the homework, not a rule.

Token counts over the full 5,141-second transcript body:

| Token | Occurrences in V04 |
|---|---|
| `EMA` (word-boundary) | **0** — the 13 raw substring hits are all *email* (7) and *emails* (6) |
| `5/13` | **0** |
| `Asian Box` (the headline topic of `NOTES.md`) | **0** — the spoken terms are *"Asian range"*, *"Asian accumulation range"*, *"the blue box"* |
| `PFH` / `PFL` | **0** / **0** |
| `mayo`, `raspberry` (2 of the 5 claimed EMA colour nicknames) | **0** / **0** |
| `volatility band` (singular, as `NOTES.md` phrases it) | **0** (the transcript has *"volatility ban"* once, `[00:13:50]`) |
| `pin bar` | **0** |
| `railroad` | 4 — real, but never with the claimed 30–90-minute gap |

The `NOTES.md` session table (Asian 7:00 PM–3:00 AM EST, London 3:30–9:00 AM, NY
9:30 AM–5:00 PM) is stated nowhere in V04. What V04 actually says about session timing is
*"From one to five AM New York, one to four AM New York, four or five hours. Take a break
from eight to 11 New York time"* `[00:21:33]`–`[00:21:37]` — different numbers, different
structure, and spoken by the instructor about **when to be at the screen**, not as a
session-boundary definition.

### Finding 3 — the Q-003 hazard recurs and is worse here

Q-003 warned that V03's fabrications were *more* dangerous than V02's because some of the
fabricated vocabulary was genuinely present in the lesson. That is truer for V04. The
recording really does discuss TDI (11), shark fin (5), stop hunts (4), railroad tracks (4),
M formations (9), the second leg, and 10–15-pip stops. A reader skimming `NOTES.md` and the
transcript together would find the vocabulary corroborated everywhere — and every
*specific* the fabricated files attach to that vocabulary is still invented:

- the EMA set and their colour nicknames (0 EMA references in the lesson);
- the 30–90-minute peak gap (never stated);
- the session clock table (never stated);
- *"2nd leg must fail to make a new extreme, showing rejection candles (Railroad tracks or
  pin bars)"* — the lesson's actual second-leg criterion is different and is stated at
  `[00:15:43]`–`[00:15:56]`;
- `V05-R002`'s stop rule *"10 to 15 pips beyond the High or Low of the Day"* is
  **adjacent to a real number and still wrong**: the instructor's figure is a 10–15–18-pip
  stop measured from the *entry* `[00:04:24]`–`[00:04:43]`, and the guest presenter's is
  *"seven pips plus the spread below the low of the day"* `[01:04:41]`, totalling 13–15 pips
  all-in `[01:05:07]`. The fabricated rule reads as a plausible blend of the two and
  matches neither.

The Q-001 handling rule — **do not mine quarantined material for leads** — matters most
exactly here.

### Finding 4 — a 3-entry visual index for one image; the image is real, and both of its labels are wrong

`VISUAL_INDEX.md` describes 3 numbered screenshots. The lesson's `SCREENSHOTS/` folder
contains **one** file, `VIDEO_05_SCREENSHOT_001_00-02-00.jpg` — entries 002 and 003
describe files that do not exist.

Entry 001 is the interesting one, and it splits from the V03 case:

- **The image is a genuine frame of this lesson.** It was matched against this session's
  own 1,037-frame sweep: it is pixel-equivalent to sweep frame `s_0000` (mean absolute
  difference **0.65** per RGB channel, i.e. JPEG-recompression noise), against **3.45 or
  worse** for every other frame in the first three minutes. It shows PowerPoint's editing
  view — ribbon, slide panel, "Click to add notes" — which exists in this recording only
  during roughly its first 32 seconds; the presenter is in full-screen slideshow mode from
  then on.
- **Its filename timestamp is wrong.** `s_0000` carries the player's burned-in timecode
  `00:00 / 85.4`. The file claims `00-02-00`. The frame at the real `[00:02:00]`
  (`s_0024`, burned timecode `02:00 / 85.4`) is the *same slide in slideshow mode* — which
  is presumably how the mislabelling survived a casual glance, and is a good argument for
  this project's rule of keeping the control bar and its burned timecode in every
  screenshot.
- **Its description is fabricated.** *"Asian Box accumulation range with 5, 13, 50, 200,
  and 800 EMAs"* describes nothing in the image, which is a four-line text slide.

So: the timestamp claim is off by two minutes and the content claim is invented, but unlike
V03's case the underlying image is authentic and locatable. Nothing written about it in
`VISUAL_INDEX.md` may be cited.

### Disposition

All three files stay quarantined. `TRANSCRIPT.md` from the same folder was checked
independently and **passed**, with a 9-entry ASR-degeneration tail fenced rather than
deleted — it is adopted at `02_TRANSCRIPTS/V04/V04_TRANSCRIPT.md` (I-008 satisfied for
V04). `VIDEO_05_SCREENSHOT_001_00-02-00.jpg` is an authentic frame of this lesson at
`[00:00:00]`, not `[00:02:00]`; this session's own capture supersedes it and it is not
used.

### Running tally for the fabrication pattern

V01, V02, V03, V04: four of four lessons individually confirmed — and per Finding 1 the
`RULES.md` half of the pattern is now established for **all 21** by direct measurement
rather than by inference. Sessions processing V05–V21 should still check `NOTES.md` and
`VISUAL_INDEX.md` individually and should treat finding the same pattern as expected.

---

## Q-005 — V05's three derived files, checked individually and confirmed fabricated; `VISUAL_INDEX.md` indexes 12 duplicate image pairs as 24 distinct screenshots

**Date:** 2026-08-11
**Files:** `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/05_Bootcamp1_Wk2_032512_Part3_68mins/`
— `RULES.md`, `NOTES.md`, `VISUAL_INDEX.md`
**Lesson:** V05, `Bootcamp1 Wk2 032512 Part3 (68mins).swf`, SHA-256 `c606520d…f896fcc1`
**Disposition:** all three remain quarantined. `TRANSCRIPT.md` from the same folder was
checked independently and **PASSED** — adopted at `02_TRANSCRIPTS/V05/V05_TRANSCRIPT.md`
(I-008 satisfied for V05).

### Finding 1 — `RULES.md` is the 21-lesson template, discharged in one step

Per `REVIEW_INDEX.md` open item 33, the per-lesson `RULES.md` audit is a solved problem and
may be discharged by confirming the three template markers. **Confirmed for V05:**

| Template marker | V05 | Population |
|---|---|---|
| Rule 1 quote at `[00:05:00]` — *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | present | 21/21 |
| Rule 2 quote at `[00:18:00]` — *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* | present | 21/21 |
| `NUMERICAL PARAMETERS` block byte-identical | present, hash `7ae7bb6ef413` | **21/21, one hash** |
| Exactly two rules | present (`V06-R001`, `V06-R002`) | 21/21 |

> **A measurement note that corrects nothing but is worth recording, because it is a trap.**
> A first pass hashed from the `NUMERICAL PARAMETERS` heading **to end of file** and got
> **two** hashes (16 + 5), appearing to contradict V04 R1's *"one hash, 21/21"*. Diffing the
> two groups shows the entire difference is a **missing trailing newline** in five files.
> Hashing the block itself gives **one** hash across all 21. **V04 R1's finding is correct
> and is independently re-confirmed here**; the apparent discrepancy was an artifact of the
> slice boundary. Future sessions: hash the block, not the tail.

**Cross-checked against V05's real audio, and it fails on every load-bearing token:**

- `[00:05:00]` **is not a marker in this transcript at all.** Nor are `[00:02:00]`,
  `[00:04:00]` or `[00:22:00]`, all cited by the file. The real markers either side of
  `[00:05:00]` are `[00:04:57]` (*"how to use scripts and customize them… using that
  editor"*) and `[00:05:05]` (*"how to mock up your charts"*) — MT4 toolbar instruction,
  not an entry rule.
- `[00:18:00]` **does** exist and reads, in full: *"We have our levels."* It is not a stop
  rule.
- **`5/13` occurs 0 times. `5 EMA` 0. `13 EMA` 0. `800` 0. `Asian Box` 0. `PFH` 0. `PFL` 0.
  `LOD` 0. `10 to 15 pips` 0.** (`HOD` returns one apparent hit — the letters inside
  *"metHOD"* at `[00:51:33]`.)
- The one nearby real number runs the **opposite** way: the presenter rejects a stop as too
  wide at *"Like 25 pips, I don't like it"* `[00:47:57]`.

### Finding 2 — `NOTES.md` is fabricated, and V05 falsifies it twice over

Distinct per lesson (all 21 `NOTES.md` are pairwise distinct), so it was examined on its
own merits. Every substantive claim is unsupported by the audio:

| `NOTES.md` claim | V05's audio |
|---|---|
| *"EMAs: 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry)"* | No moving average is given a period, colour or nickname anywhere. `EMA` occurs 3×, for the **50** and the **200** only. `800` occurs 0×. |
| *"5/13 EMA Cross: Execution confirmation on M15 close"* | `5/13` 0×. No timeframe is ever named for entry. |
| *"TDI Indicator: Green Price Line crossing Red Signal Line with Shark Fin confirmation outside Volatility Bands"* | `TDI` occurs 6× and is **never defined** — no lines, no bands, no rule. The speaker says *"I don't use it anymore"* `[00:36:50]`. |
| *"Stop loss positioned 10–15 pips past High/Low of Day with minimum 1:3 Risk-to-Reward"* | 0×. No stop rule and no risk-to-reward ratio is stated in V05. |
| Session clock table in EST (Asian 7:00 PM–3:00 AM, London 3:30 AM–9:00 AM, NY 9:30 AM–5:00 PM) | No session clock is stated. `EST` 0×. |
| *"Peak Formation High (PFH) & Low (PFL)"* | `PFH` 0×, `PFL` 0×. *"peak formation"* occurs once, `[00:11:48]`. |

**And an independent falsification that needs no token counting:** the file is headed
*"Instructor Core Concepts"* and every `VISUAL_INDEX.md` entry attributes the content to
*"Steve Mauro"*. **Steve Mauro does not speak in V05.** The lesson is presented start to
finish by a third party who refers to Steve in the third person 21 times
(`V05_TRANSCRIPT.md` § ONE SPEAKER). A file that misattributes the entire lesson to a
presenter who is not on the recording was not written from the recording.

### Finding 3 — `VISUAL_INDEX.md`: 27 entries, 27 files, **15 distinct images**

This is the sharpest instance the project has found, and it differs in kind from V01's
(78 entries / 1 file) and V04's (3 entries / 1 file). Here the **file inventory is
accurate** — 27 entries, 27 files present in `SCREENSHOTS/`, every claimed filename
resolves. What is fabricated is everything *about* them.

1. **Twelve of the images are byte-identical duplicate pairs.** `extracted_jpeg_NNNN.jpg`
   and `raw_extracted_NNNN.jpg` match on SHA-256 for all twelve of
   `1012, 1013, 1017, 1019, 1020, 1022, 1023, 1025, 1027, 1029, 1030, 1032`. Across all 27
   files there are **15 distinct images**. Each duplicate pair is indexed as **two
   different screenshots, at two different timestamps, with two different descriptions.**
2. **The timestamps are a generated grid, not observations.** They run
   `07:00, 12:00, 17:00, 22:00, 27:00, 32:00, 37:00, 42:00, 47:00, 52:00, 57:00,`
   **`62:00`**, then restart at `02:00` and cycle again — three passes of the same
   12-step, 5-minute ladder. **`[00:62:00]` is not a valid time.** A minute field of 62 is
   arithmetic that was never checked against a clock, and it appears twice.
3. **Entry 001 contradicts itself.** Its `Timestamp:` is `[00:07:00]` while its
   `Filename:` is `VIDEO_06_SCREENSHOT_001_00-02-00.jpg`. Neither is `[00:00:00]`.
4. **The descriptions are template prose.** Every one of the 27 reads *"Steve Mauro
   breaking down <lowercased title> and institutional market mechanics"* and *"Preserves
   exact visual presentation and chart setups for Video 06"*. They describe TDI shark fins,
   Asian Box accumulation and 5/13 EMA crosses — none of which V05's audio contains.

### The mislabel worth carrying forward

All three files, and the source `TRANSCRIPT.md`'s dropped header, call this lesson
**"Video 06 of 21"**, and `RULES.md`'s rule IDs are `V06-R001` / `V06-R002`. That is the
**pre-ingestion alphabetical numbering D-017 corrected** (the `Wk1, Wk10, Wk2, …` artifact
that put Week 10 third). Under the adopted order this file is **V05**. A future session
reading a quarantined file's own ID will be off by one from V03 onward — do not take
lesson numbers from quarantined material.

### Running tally for the fabrication pattern

**V01, V02, V03, V04, V05 — five of five individually confirmed.** The `RULES.md` half is
established for all 21 by direct measurement (Finding 1, re-confirmed this session).
`NOTES.md` and `VISUAL_INDEX.md` remain pairwise distinct across the library and still
require per-lesson examination for V06–V21 — and V05 shows why: its `VISUAL_INDEX.md`
failure mode (duplicate images indexed as distinct screenshots on a generated time grid)
would not have been caught by checking for V01's failure mode.
