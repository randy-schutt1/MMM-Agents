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
| *"EMAs: 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry)"* | No moving average is given a period, colour or nickname anywhere. `EMA` occurs **2×**, for the **50** and the **200** only — `[00:23:52]`, `[01:05:53]`. `800` occurs 0×. |
| *"5/13 EMA Cross: Execution confirmation on M15 close"* | `5/13` 0×. No timeframe is ever named for entry. |
| *"TDI Indicator: Green Price Line crossing Red Signal Line with Shark Fin confirmation outside Volatility Bands"* | `TDI` occurs 6× and is **never defined** — no lines, no bands, no rule. The speaker says *"I don't use it anymore"* `[00:36:50]`. |
| *"Stop loss positioned 10–15 pips past High/Low of Day with minimum 1:3 Risk-to-Reward"* | 0×. No stop rule and no risk-to-reward ratio is stated in V05. |
| Session clock table in EST (Asian 7:00 PM–3:00 AM, London 3:30 AM–9:00 AM, NY 9:30 AM–5:00 PM) | No session clock is stated. `EST` 0×. |
| *"Peak Formation High (PFH) & Low (PFL)"* | `PFH` 0×, `PFL` 0×. *"peak formation"* occurs once, `[00:11:48]`. |

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — `REVIEW_INDEX.md` open item
> 39, applied at V05 R2 2026-08-11. The first row previously read: "`EMA` occurs 3×, for the
> **50** and the **200** only." **The literal token occurs twice**, at `[00:23:52]` *"Nice
> close below the 50 EMA."* and `[01:05:53]` *"…below the 200 EMA."*; the third item the
> transcript's own note had listed, *"They'll induce by closing below the 200."* `[01:06:02]`,
> refers to the same object and **does not contain the token**. **No conclusion in `Q-005`
> changes** — the falsification of the fabricated `NOTES.md` rests on `800` = 0, `5/13` = 0,
> and the absence of any period, colour or nickname, all of which are unaffected and were
> independently re-measured at R1 and R2. The paired correction is at
> `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES.)*

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

---

## Q-006 — V06's three derived files, checked individually and confirmed fabricated; `VISUAL_INDEX.md` calls two SWF delta-tiles and one duplicated pair "Presentation Slide / Annotated Chart"

**Date:** 2026-08-12
**Files:** `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/06_Bootcamp1_Wk2_032612_Part1_75mins/`
— `RULES.md`, `NOTES.md`, `VISUAL_INDEX.md`
**Lesson:** V06, `Bootcamp1 Wk2 032612 Part1 (75mins).swf`, SHA-256 `382207b3…aac96e86`
**Disposition:** all three remain quarantined. `TRANSCRIPT.md` from the same folder was
checked independently and **PASSED** — adopted at `02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md`
(I-008 satisfied for V06).

### Finding 1 — `RULES.md` is the 21-lesson template, discharged in one step

Per `REVIEW_INDEX.md` open item 33 the per-lesson `RULES.md` audit is a solved problem and
may be discharged by confirming the template markers. **Confirmed for V06:**

| Template marker | V06 | Population |
|---|---|---|
| Rule 1 quote at `[00:05:00]` — *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | present | **21/21, re-measured this session** |
| Rule 2 quote at `[00:18:00]` — *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* | present | 21/21 |
| `NUMERICAL PARAMETERS` block byte-identical | present, hash `e75ace74e1f1` | **21/21, one hash** |
| Exactly two rules | present (`V07-R001`, `V07-R002`) | 21/21 |

> **The hash differs from the one Q-005 records (`7ae7bb6ef413`) because the slice differs,
> not because the block does.** Q-005 hashed the block after stripping; this session hashed
> `sed -n '/# NUMERICAL PARAMETERS/,/# AMBIGUITIES/p'`, inclusive of both delimiter lines,
> across four spread-out lessons (01, 05, 06, 21) and got **one** value, `e75ace74e1f1`, in
> all four. Both measurements support the same proposition — **one block, 21 files** — and
> Q-005's own warning about slice boundaries is the reason this note exists rather than a
> contradiction being recorded.

**Cross-checked against V06's real audio, and it fails on every load-bearing token:**

- `[00:05:00]` **is** a marker in this transcript, and it reads, in full: *"one day of it and
  you're looking for 3 levels of drop."* Chart-structure narration, not an entry rule.
- `[00:18:00]` **is not a marker at all.** Nor are `[00:22:00]` or `[00:07:00]`, both cited by
  the quarantined files. `[00:04:00]` **is** a marker and reads *"Look back to the 4-hour chart
  and you're going to realize you're only in level 2"* — not an EMA parameter list.
- **`5/13` occurs 0 times. `5 EMA` 0. `800 EMA` 0. `Asian Box` 0. `Shark Fin` 0. `PFH` 0.
  `PFL` 0. `HOD` 0. `LOD` 0. `10 to 15 pips` 0.**
- The one place V06 states a stop distance runs a different way entirely: *"if I take this
  trade here and if my stop is about 13-pips, I'm looking for minimum moves. 26-pips, I would
  prefer at least 30-pips"* `[01:03:19]`–`[01:03:26]` — a stop derived from **moving-average
  spacing**, not from a fixed 10–15 pip buffer beyond a daily extreme.
- **`13 EMA` does occur 3 times in genuine audio** (`[00:17:58]`, `[00:31:03]`, `[00:59:03]`).
  This is worth stating plainly because it is the first time a template token has had a real
  counterpart: it is **not** evidence for the template. The template's claim is a *5/13 cross
  confirmed on an M15 close*; V06's three uses are *"Price did not close above the 13 EMA"*,
  *"If it hits with 13 EMA, that's even better"* and *"13 EMA or 50% retrace of the shift
  bar"*. No cross, no `5`, no timeframe. **A token in common is not a rule in common.**

### Finding 2 — `NOTES.md` is fabricated, and V06 falsifies it on its own subject matter

Distinct per lesson (all 21 `NOTES.md` are pairwise distinct), so it was examined on its own
merits. Its stated subject is wrong before any rule is checked:

| `NOTES.md` claim | V06's audio and slides |
|---|---|
| *"Topic Focus: Asian Accumulation Boxes, London Session Breakouts & Stop Hunts"* | The lesson's title, **printed on its own title slide and spoken as its first words**, is **"Micro Daily Trends"**. `Asian` occurs 5× in 74 minutes, never as a defined box; the subject is **intraday pushes** (`push`/`pushes` 89×) |
| *"Session Timing: Asian 7:00 PM–3:00 AM EST; London 3:30 AM–9:00 AM EST; New York 9:30 AM–5:00 PM EST"* | **No session clock is stated anywhere.** `EST` occurs 0×. The nearest thing to a session statement is *"U.S. session you're looking for anywhere from 30 to 50 pips… They don't usually run like London"* `[00:31:14]`–`[00:31:20]` — a target size, not a clock |
| *"EMAs: 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry)"* | **Partly true by coincidence, and this is the one row that needs care.** V06 genuinely contains *"water"* (4×), *"mail"/"male"* (2×) and *"blueberry"* (2×) as moving-average nicknames, and the DMR curriculum in frame `V06_00-48-29` prints *"2 Pins to the **Mayo or Water**"*. But **no period is attached to any nickname anywhere in V06**, `mustard` occurs 0×, `raspberry` occurs 0×, and the pairing table is not derivable from this lesson. The file states as fact a five-row mapping the lesson does not contain. See `A-020` |
| *"5/13 EMA Cross: Execution confirmation on M15 close"* | `5/13` 0×. No timeframe is named for entry. The presenter's stated entry precondition is *"You've got to wait for the rejection of price before entering your trade"* `[00:08:06]` |
| *"TDI Indicator: Green Price Line crossing Red Signal Line with Shark Fin confirmation outside Volatility Bands"* | `TDI` occurs **once**, at `[00:49:16]`, reading out a **future curriculum item**. `shark` 0×. Nothing is shown or defined |
| *"Risk Management: Stop loss positioned 10–15 pips past High/Low of Day with minimum 1:3 Risk-to-Reward ratio"* | 0×. V06 states *"I usually like 2 to 1"* `[01:03:17]` — a **different ratio**, stated by a guest, in a different construction |
| *"Level Count Progression: 3 levels of drop or rise following peak formations before cycle reset"* | This one is close to something V06 does say — and that is exactly why the file is dangerous rather than merely wrong. A reader who spot-checks the plausible row and stops will certify the six rows above along with it |

### Finding 3 — `VISUAL_INDEX.md` indexes two SWF delta-tiles and one duplicated pair as five "Presentation Slide / Annotated Chart" screenshots

It claims *"Total Captured Presentation & Annotated Chart Screenshots: 5"*. Five files do
exist in the sibling `SCREENSHOTS/` folder. **Four of the five entries are false:**

| # | Claimed | Measured (PIL, this session) |
|---|---|---|
| 001 | *"Presentation Title & Session Mapping — Session schedule overview and Asian accumulation range rules"* at `[00:07:00]`, file `VIDEO_07_SCREENSHOT_001_00-02-00.jpg` | **1024×768 and genuine** — but it is the **title slide reading "Micro Daily Trends"**, which is neither a session map nor an Asian range rule. The timestamp `[00:07:00]` and the filename's `00-02-00` disagree with each other, and the slide is on screen from `[00:00:00]` |
| 002 | *"Asian Range High/Low Definition — Defining 15-25 pip Asian box boundaries"*, `extracted_jpeg_1008.jpg` | 444×322. **Byte-identical to entry 005** (SHA-256 `3077b92f…`) |
| 003 | *"London Open Stop Hunt Mechanics — Rapid vector push above Asian High"*, `extracted_png_27.png` | **267×51 pixels.** A Camtasia delta tile. It cannot depict a chart |
| 004 | *"Reversal Candlestick Rejection — Railroad track pattern forming at London High of Day"*, `extracted_png_290.png` | **137×14 pixels.** Likewise |
| 005 | *"Trade Entry & 5/13 EMA Confirmation"*, `raw_extracted_1008.jpg` | 444×322. **The same bytes as entry 002**, indexed again under a second filename at a different timestamp |

Three further defects of the same family as Q-005's:

1. **The timestamps are a generated grid** — `[00:07:00]`, `[00:12:00]`, `[00:17:00]`,
   `[00:22:00]`, `[00:27:00]`: exactly five minutes apart, ascending, in a 74-minute lesson.
   **Three of the five — `[00:07:00]`, `[00:12:00]`, `[00:22:00]` — are not markers in the
   transcript at all;** the other two, `[00:17:00]` and `[00:27:00]`, land on real markers by
   coincidence of the grid, and neither carries anything resembling its claimed content
   (`[00:17:00]` is *"Where is my trap volume right here?"*, `[00:27:00]` is *"It also hits the
   water."*).
2. **Every description is template prose**, attributing the lesson to *"Steve Mauro breaking
   down &lt;lowercased title&gt; and institutional market mechanics"*. **Steve Mauro does not
   speak in this lesson at all** (`V06_TRANSCRIPT.md` § "ONE SPEAKER"). The attribution is
   not merely unsourced, it is the opposite of what the recording contains.
3. **It claims to preserve visuals for "Video 07".** See the mislabel note below.

**For contrast, and as the measure of what the quarantined index was worth:** this session's
own sweep of the same file produced **903 frames on a 5-second grid**, from which **32** were
curated into `04_SCREENSHOTS/V06/`, each carrying the player's burned-in timecode so it proves
its own timestamp.

### The mislabel worth carrying forward

All three files call this lesson **"Video 07 of 21"**, and `RULES.md`'s rule IDs are
`V07-R001` / `V07-R002`. That is the **pre-ingestion alphabetical numbering D-017 corrected**.
Under the adopted order this file is **V06**. The same off-by-one appears in the sibling audio
file's name, **`audio_07.mp3`**, which sits in folder `06_…` — it was checked this session and
is the **correct** audio for V06 (duration 4473.626 s, matching the SWF's own extracted audio
to the millisecond, though re-encoded and therefore a different checksum). **Do not take
lesson numbers from quarantined material, and do not take them from the loose media filenames
either.**

### Running tally for the fabrication pattern

**V01, V02, V03, V04, V05, V06 — six of six individually confirmed.** The `RULES.md` half is
established for all 21 by direct measurement (Finding 1). `NOTES.md` and `VISUAL_INDEX.md`
remain pairwise distinct across the library and still require per-lesson examination for
V07–V21 — and V06 shows a **third** distinct failure mode: not V01's phantom-file inflation and
not V05's duplicate-pair inflation, but **sub-slide fragments of the SWF's own delta-tile
stream, indexed as if they were slides**. Three lessons, three different ways of being wrong.

---

## Q-007 — V07–V21 `RULES.md`, batch-discharged via the template-marker test (`REVIEW_INDEX.md` open item 33)

```text
STATUS:        QUARANTINED — DO NOT USE (discharged via template-marker test, not
                a fresh per-lesson audio cross-check)
DATE:          2026-08-12
QUARANTINED BY: Batch pre-verification pass (proactive, ahead of per-video ingestion)
DECISION:      D-017 (Q-001 blanket action); RULES.md half already proven for all 21
                by direct measurement at Q-004 / REVIEW_INDEX.md open item 33
```

### Scope of this entry

This is **not** a per-lesson ingestion pass. It is a proactive batch check of `RULES.md`
only, run ahead of V07–V21's individual Student sessions, so that step doesn't have to be
re-derived from scratch 15 times. `NOTES.md` and `VISUAL_INDEX.md` are **explicitly out of
scope here** — per Q-001 through Q-006 they are pairwise distinct across the library and
still require their own per-lesson audio cross-check when each video's real ingestion runs.
`TRANSCRIPT.md`, `NOTES.md`, `INDEX.md` and `VISUAL_INDEX.md` were not touched.

### What was checked

Per the discharge method item 33 authorizes ("a future session may discharge the per-lesson
audit in one step by confirming those three markers and citing `V04_REVIEW_R1.md` + `Q-004`"),
all three template markers were re-measured mechanically across every `RULES.md` from
`per_lesson/07_.../` through `per_lesson/21_.../` (folder `NN` = video `VNN` per D-017):

| Template marker | Result, V07–V21 |
|---|---|
| Rule 1 quote at `[00:05:00]` — *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | present, all 15 |
| Rule 2 quote at `[00:18:00]` — *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* | present, all 15 |
| Exactly two `## Rule ID:` entries | true, all 15 |
| `NUMERICAL PARAMETERS` block (sed range `/# NUMERICAL PARAMETERS/,/# AMBIGUITIES/`), hashed | **one hash across all 15** — and re-hashing V01–V06 the same way returns the **identical** hash, confirming this is the same one block established at Q-004/Q-005/Q-006, not a new variant |

Zero exceptions. No `RULES.md` in `V07`–`V21` differs from the confirmed fabrication
signature — none required flagging as a pattern exception per step 4 of this pass's brief.

### Disposition

All 15 files (`V07`–`V21` `RULES.md`) remain quarantined in place at
`_QUARANTINE_UNVERIFIED_NOTES/per_lesson/NN_.../RULES.md`, already covered by the blanket
`README_WHY_QUARANTINED.md` warning header for the whole quarantine tree. No files were
moved, renamed, or deleted. This entry is the flag: a future Student session opening
`V07`–`V21` can cite `Q-007` (or the original `Q-004` measurement) instead of re-running the
`RULES.md` audit, but still owes `NOTES.md` and `VISUAL_INDEX.md` their own per-lesson check
per the Q-001…Q-006 precedent.

### Running tally for the fabrication pattern

**`RULES.md`: 21 of 21 lessons now covered by either individual audio cross-check (V01–V06,
`Q-001`…`Q-006`) or the mechanical template-marker discharge (V07–V21, this entry) — zero
exceptions found across the whole library.** `NOTES.md` and `VISUAL_INDEX.md` remain
unaudited for V07–V21 and are NOT covered by this entry; each still needs its own per-lesson
check, on its own merits, when that video's ingestion actually runs (they have shown three
distinct failure modes so far — V01, V05, V06 — so uniformity should not be assumed for them
the way it has now been proven for `RULES.md`).

---

## Q-008 — V07's `NOTES.md` and `VISUAL_INDEX.md`, checked individually and confirmed fabricated; `VISUAL_INDEX.md` indexes the **Camtasia player's own splash logo** as a TDI setup

```text
STATUS:        QUARANTINED — DO NOT USE
DATE:          2026-08-13
QUARANTINED BY: V07 Student session
DECISION:      D-017 (Q-001 blanket action). RULES.md is NOT re-derived here —
                it is discharged by Q-007's mechanical template-marker test, as
                Q-007 explicitly authorizes.
```

### Scope — what this entry does and does not cover

| File | Disposition | Basis |
|---|---|---|
| `RULES.md` | Already quarantined, **not re-audited** | **`Q-007`**, which measured all three template markers across `V07`–`V21` and found the identical `NUMERICAL PARAMETERS` hash. Q-007's own text says a later Student session "can cite `Q-007` … instead of re-running the `RULES.md` audit" |
| `NOTES.md` | **Fabricated — confirmed here** | Per-lesson audio cross-check, below |
| `VISUAL_INDEX.md` | **Fabricated — confirmed here** | Per-lesson image cross-check, below |
| `TRANSCRIPT.md` | **SOUND — adopted** | `SETUP_ISSUES.md` I-008, all four criteria, recorded in `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` § PROVENANCE AND VERIFICATION |

Q-007 required that `NOTES.md` and `VISUAL_INDEX.md` "still need their own per-lesson check, on
their own merits". This is that check.

### Method

All token counts are word-boundary matches over the **verbatim body only** of
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` (header and timestamp lines excluded), 7,436 words.
All image claims are checked against the files actually present in the lesson folder's
`SCREENSHOTS/`, by SHA-256 and by opening each one.

---

### `NOTES.md` — finding 1: it describes a different lesson

`NOTES.md` gives the lesson's **Topic Focus** as *"Time Mapping, Session Overlaps & Peak
Formation Tracking"*.

The lesson is titled **"Best Trade Grabs"** — printed on its own title slide together with
*"MMFx Breakout Session 03-26-2012"* (frame `V07_00-00-10`). Its subject is what makes a good
trade: setups, entries, exits and money management, followed by 26 minutes of Q&A. The
vocabulary that actually dominates it is `second leg` **34×**, `flashcard` **15×**, `R&D`
**11×** (10 as a standalone token, plus one *"you've R&Ded it"* at `[00:20:50]`), `level three`
**13×**, `level one` **9×**.

### `NOTES.md` — finding 2: a session-time table that is not in the recording

It prints three sessions with clock boundaries:

> *"Asian Session: 7:00 PM – 3:00 AM EST … London Session: 3:30 AM – 9:00 AM EST … New York
> Session: 9:30 AM – 5:00 PM EST"*

Measured against the audio:

| Token | Occurrences in V07 |
|---|---|
| `EST` | **0** |
| `7:00`, `3:00`, `3:30`, `9:00`, `9:30`, `5:00` | **0** each |
| `Asian` | **1** — `[00:01:48]` *"A nice small W after inducing after the Asian session"*, describing one chart |
| `London` | **2** — `[00:38:03]` and `[00:39:17]`, both inside one student's question about a trade |
| `New York` | **1** — `[00:15:17]` *"Closer to New York session, got in in the shadow box"* |

**No session boundary, in any timezone, is stated anywhere in this lesson.** The three sessions
are named four times between them, always as the setting of a particular chart, never as a rule.
The same sweep was run over all 24 curated frames at full resolution: **no session clock appears
on any of them either.**

### `NOTES.md` — finding 3: structural objects that are absent

| Claim in `NOTES.md` | Occurrences in V07 |
|---|---|
| *"Peak Formation High (PFH) & Low (PFL)"* | `PFH` **0**, `PFL` **0**, `peak formation` **0** |
| *"market makers induce positions in low-volatility Asian accumulation boxes"* | `accumulation` **0**, `institutional` **0**, `Asian Box` **0** |
| *"3 levels of drop or rise following peak formations before cycle reset"* | `reset` appears **4×** (`[00:23:15]`, `[00:38:51]`, `[00:39:37]`, `[00:43:53]`), **never with a peak formation and never as a level count.** Three of the four are *"after a reset"* / *"from that reset"* attached to a **level number**, which is a different claim — see `V07_SOURCE_NOTES.md` §5 |

### `NOTES.md` — finding 4: the indicator and risk block, which is the shared template

| Claim in `NOTES.md` | Occurrences in V07 |
|---|---|
| *"EMAs: 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry)"* | `mustard` **0**, `mayo` **0**, `raspberry` **0**, `800` **0**. `water` 2×, `mail`/`male` 7×, `blueberry` 2× — **and not one of them is given a period** |
| *"5/13 EMA Cross: Execution confirmation on M15 close"* | `5/13` **0**, `M15` **0**. `EMA` occurs **twice**, both inside one Q&A about stair-stepped higher-timeframe averages (`[00:26:01]`, `[00:26:29]`) |
| *"TDI Indicator: Green Price Line crossing Red Signal Line with Shark Fin confirmation outside Volatility Bands"* | `shark fin` **0** *spoken*, `volatility band` **0**, `green line` **0**, `signal line` **0**. `TDI` occurs twice, `[00:24:08]` and `[00:31:16]`, both without any definition |
| *"Stop loss positioned 10–15 pips past High/Low of Day with minimum 1:3 Risk-to-Reward ratio"* | `10-15` **0**, `10 to 15` **0**, `1:3` **0**, `HOD` **0**, `LOD` **0**. `stop loss` occurs **once**, `[00:09:44]`, as *"Stop losses. If I can make them smaller and possible…"* — a wish, not a distance |

> **The last row is the fabrication template's own signature.** *"Place your stop loss 10 to 15
> pips beyond the High or Low of the Day"* is `RULES.md` rule 2, present in all 21 lessons and
> proven identical by `Q-007`. Finding it restated in prose inside `NOTES.md` shows the two
> files were generated from **one source**, which is what `Q-004` proved mechanically for
> `RULES.md` and what `Q-002`, `Q-003`, `Q-005` and `Q-006` found for `NOTES.md` individually.
> V07 is the sixth `NOTES.md` to fail, and it fails the same way.

### There is one accidental near-hit, and it is recorded so a later session does not mistake it for accuracy

`NOTES.md` says *"M & W Pattern Anatomy: 2nd leg failure test with candlestick rejection
(Railroad tracks, pin bars, star formations)"*. V07 **does** discuss second legs, railroad
tracks and star formations. **This is not evidence the file was written from the audio.** The
same sentence appears in the shared template, the lesson supplies no *"failure test"* language,
and the surrounding four claims in the same section are all zero-occurrence. A generator that
emits the course's general vocabulary will occasionally land on a topic the lesson happens to
cover; that is a property of the vocabulary, not of the file's provenance.

---

### `VISUAL_INDEX.md` — 7 claimed screenshots, 5 files, **2 distinct screens**

The file claims *"Total Captured Presentation & Annotated Chart Screenshots: 7"* and describes
seven numbered images, each with a timestamp, a filename, a byte size, a *"What is visible"*
description and a *"Trading Significance"*.

The folder holds **seven files** — and by SHA-256, **two pairs are byte-identical**:

| # | Filename in the index | Dimensions | SHA-256 (first 16) | Actually |
|---|---|---|---|---|
| 001 | `VIDEO_08_SCREENSHOT_001_00-02-00.jpg` | 1024×768 | `159292f29fe500e3` | **The title slide** — *"Best Trade Grabs / MMFx Breakout Session 03-26-2012"* |
| 002 | `extracted_jpeg_1001.jpg` | 1024×768 | `9e2a66db74b63688` | **The same title slide**, re-encoded (max per-pixel Δ = 18, mean Δ = 0.42 against 001) |
| 003 | `extracted_jpeg_1012.jpg` | **492×40** | `34ee0767916c438c` | **A delta-tile of the background chart's title bar**, reading `EURJPYm,M15 101.100 101.200 101.059 101.188` |
| 004 | `extracted_png_27.png` | **267×51** | `17e5622c255a753a` | **The Camtasia Studio / TechSmith splash logo** |
| 005 | `extracted_png_290.png` | **137×14** | `9791aacf64336fbe` | **The words "Camtasia Studio 6"** |
| 006 | `raw_extracted_1001.jpg` | 1024×768 | `9e2a66db74b63688` | **Byte-identical to 002.** The same title slide again |
| 007 | `raw_extracted_1012.jpg` | **492×40** | `34ee0767916c438c` | **Byte-identical to 003.** The same title-bar tile again |

**Seven entries. Five files. Three copies of one slide, two copies of one 492×40 tile, and two
pieces of player chrome. Zero annotated charts. Zero of the seven descriptions matches its
file.**

### The two entries that make the fabrication unmistakable

| Entry | What `VISUAL_INDEX.md` says is visible | What the file is |
|---|---|---|
| **004** | *"EMA Dynamic Support & Resistance — 50 EMA (Mayo) and 200 EMA (Blueberry) reaction bounces."* Visual Type: *"Presentation Slide / Annotated Chart"* | A **267×51** image of the words **"Camtasia Studio"** with the TechSmith logo |
| **005** | *"TDI Blood in the Water Setup — Green line crossing red line at volatility band boundary."* Visual Type: *"Presentation Slide / Annotated Chart"* | A **137×14** image of the words **"Camtasia Studio 6"** |

A 137×14-pixel strip carrying the player's version string is indexed as a TDI setup, at a
timestamp, with a trading significance. **`A-031` ("blood in the water") and `A-032` ("shark
fin") must not be read as having any V07 print evidence from this file.** V07 does have a real
printed shark fin — *"SHARK FIN IN TDI"*, boxed on the oscillator in frame `V07_00-18-25` — and
it was found by capturing the lesson, not by reading this index.

### Two further independent errors

1. **Every entry attributes the lesson to the wrong speaker.** All seven read *"Steve Mauro
   breaking down …"*. V07 carries **zero course-author runtime**; a single guest presenter
   speaks the whole 48 minutes and refers to Steve in the third person twice, once as the next
   questioner in the audience queue (`V07_TRANSCRIPT.md` § ONE SPEAKER…).
2. **The timestamps are wrong, and entry 001 disagrees with its own filename.** The index dates
   001 to `[00:07:00]` while the filename says `00-02-00`; the file is the **title slide**,
   which is on screen from about `00:00:05` to `00:00:45` in the capture and is gone by
   `00:02:00`. The remaining six are spaced at exactly five-minute intervals — `[00:12:00]`,
   `[00:17:00]`, `[00:22:00]`, `[00:27:00]`, `[00:32:00]`, `[00:37:00]` — which is a generated
   sequence, not an observation.

### One thing this audit is careful NOT to claim

`VISUAL_INDEX.md`'s **file listing is accurate** — the five files it names do exist, at the byte
sizes and dimensions it states. What is fabricated is every statement about **what is in them**.
That is worth recording precisely, because it shows the generator had directory access and did
not have image access, which is the same shape `Q-005` and `Q-006` found.

---

### Disposition

All three files remain quarantined in place at
`_QUARANTINE_UNVERIFIED_NOTES/per_lesson/07_Bootcamp1_Wk2_032612_Part2_48mins/`, covered by the
tree's blanket `README_WHY_QUARANTINED.md`. **No file was moved, renamed or deleted.** The
lesson's own `SCREENSHOTS/` folder is left untouched as source-side evidence; this project's
screenshots for V07 are the 24 frames in `04_SCREENSHOTS/V07/`, captured from the `.swf`.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered (V01–V06 individually, V07–V21 by `Q-007`'s mechanical
  discharge). Zero exceptions library-wide.
- **`NOTES.md`:** **7 of 21 audited** (V01–V07), **7 fabricated, zero exceptions.**
- **`VISUAL_INDEX.md`:** **7 of 21 audited** (V01–V07), **7 fabricated**, and now **four
  distinct failure modes**: 78 entries for 1 image (V01), 12 duplicate pairs sold as 24
  screenshots (V05), SWF delta-tiles indexed as annotated charts (V06), and — new here —
  **the player's own chrome indexed as course content** (V07). Uniformity still should not be
  assumed for V08–V21; each needs its own check.

---

## Q-009 — V08's `NOTES.md` and `VISUAL_INDEX.md`, confirmed fabricated; and the fabrication is now shown to be ONE GENERATOR, not four independent failures

```text
STATUS:        QUARANTINED — DO NOT USE
DATE:          2026-08-13
QUARANTINED BY: V08 Student session
DECISION:      D-017 (Q-001 blanket action). RULES.md is NOT re-derived here —
                it is discharged by Q-007's mechanical template-marker test, as
                Q-007 explicitly authorizes and COURSE_PROGRESS.md's V07 GATE
                carry-forward item (e) instructs.
```

### Scope

| File | Disposition | Basis |
|---|---|---|
| `RULES.md` | Already quarantined, **not re-audited** | **`Q-007`**, the mechanical template-marker discharge for `V07`–`V21` |
| `NOTES.md` | **Fabricated — confirmed here** | Per-lesson audio cross-check, below |
| `VISUAL_INDEX.md` | **Fabricated — confirmed here, and mechanically so** | Per-lesson image cross-check, below |
| `TRANSCRIPT.md` | **SOUND — adopted** | `SETUP_ISSUES.md` I-008, four axes, recorded in `02_TRANSCRIPTS/V08/V08_TRANSCRIPT.md` § VERIFICATION |

### Method

Token counts are word-boundary matches over the **verbatim body only** of
`02_TRANSCRIPTS/V08/V08_TRANSCRIPT.md` (header and timestamp lines excluded), **7,315 words**.
Every image claim is checked against the files actually present in the lesson folder's
`SCREENSHOTS/`, by SHA-256, by reading the real pixel dimensions, **and by opening and looking at
each one**.

---

### 1. `NOTES.md` — fabricated

`NOTES.md` states four blocks of doctrine. Measured against the lesson's own audio:

| `NOTES.md` claims | Occurrences in V08's 7,315-word body |
|---|---|
| *"EMAs: 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry)"* | **`EMA`: 0.** `mustard` 0, `blueberry` 0, `raspberry` 0 |
| *"5/13 EMA Cross: Execution confirmation on M15 close"* | **`5/13`: 0.** `moving average`: 0 |
| *"TDI Indicator: Green Price Line crossing Red Signal Line with Shark Fin confirmation outside Volatility Bands"* | **`TDI`: 0. `shark fin`: 0. `signal line`: 0. `volatility band`: 0. `divergence`: 0** |
| *"Asian Session: 7:00 PM – 3:00 AM EST / London: 3:30 AM – 9:00 AM EST / New York: 9:30 AM – 5:00 PM EST"* | **`7:00` 0, `3:00 am` 0, `3:30` 0, `9:00` 0, `9:30` 0, `5:00 pm` 0. Six clock figures, six zeroes** |
| *"Peak Formation High (PFH) & Low (PFL)"* | **`peak formation`: 0. `PFH`: 0. `PFL`: 0** |
| *"M & W Pattern Anatomy: 2nd leg failure test with candlestick rejection (Railroad tracks, pin bars, star formations)"* | **`pin bar`: 0.** `star` occurs twice as a standalone token and **both are "Death Star"** — the deck's own metaphor for bad trading ideas (`[00:15:30]`, `[00:16:51]`). `railroad` occurs 3× **as an unexplained chart label** and is never defined |
| *"Multi-Timeframe Alignment"* (header topic) | **`multi-timeframe` 0, `confluence` 0, `H4` 0, `H1` 0, `four hour` 0, `one hour` 0.** The lesson's single multi-timeframe remark is `[00:41:56]` *"I'm almost convinced there's going to be an M on the one minute time frame"*, immediately declined as *"advanced stuff"* he will not go into |
| *"Institutional Mechanics: … institutional order flow … news events"* | **`institutional` 0, `order flow` 0, `news` 0** |

**One claim is adjacent to something real, and it is the most dangerous entry in the file:**

> *"Risk Management: Stop loss positioned **10–15 pips past High/Low of Day** with minimum
> **1:3 Risk-to-Reward** ratio."*

- The **1:3** is right by V08's own words — `[00:39:58]` *"bringing risk we reward to three to one
  or greater"*.
- The **10 pips** is adjacent to a real printed slide — `04_SCREENSHOTS/V08/V08_00-05-40…` prints
  *"dealing **within 10 pips of HOD/LOD**"*.
- **But the rule stated is not V08's.** V08's 10 pips is a **tolerance on how close your ENTRY
  gets to the extreme**. `NOTES.md` converts it into a **stop-loss placement 10–15 pips PAST the
  extreme** — a different object, on the other side of the price, doing a different job. The
  string `10-15` and the phrase `stop loss` as a rule appear **nowhere** in the audio; the one
  occurrence of *"stop loss"* is `[00:09:48]`, inside a caricature of a **doubter**: *"I moved my
  stop loss and took a 25% hit on my account. Steve's thing just doesn't work."*

> **This is the failure mode that makes these files dangerous rather than merely useless.** A
> file that is wrong about everything is discarded on sight. A file that attaches a **real
> number** to a **rule the lesson never states** reads as sourced, survives a skim, and puts an
> invented stop rule into a corpus that is going to generate trading code. Recorded at length so
> the next session recognises the shape rather than the instance.

**Verdict: `NOTES.md` is fabricated.** Its trading content is imported from elsewhere in the
course — the food-named EMA scheme is real corpus doctrine, and V08 does brush it twice (*"back
to the water"* `[00:21:28]`, *"off the Mayo"* `[00:22:13]`, `[00:23:12]`) as casual references to
already-named lines — but **presenting it as this lesson's content is misattribution**, and the
session table, PFH/PFL, TDI block and stop rule are not in the course-adjacent category at all.
Either way it is disqualified as V08 evidence.

---

### 2. `VISUAL_INDEX.md` — fabricated, and provably so without any judgement call

Eleven entries. **Four independent mechanical proofs, before anyone looks at an image.**

**Proof 1 — three timestamps are after the file ends.** The lesson is **00:43:03**
(2,583.75 s measured; SWF header 7,752 frames ÷ 3.0 fps = 2,584.0 s). Screenshots 009, 010 and
011 are timestamped **`[00:47:00]`, `[00:52:00]`, `[00:57:00]`**.

**Proof 2 — the timestamps are a generated arithmetic sequence, not observations.** All eleven
are exactly five minutes apart: `07:00, 12:00, 17:00, 22:00, 27:00, 32:00, 37:00, 42:00, 47:00,
52:00, 57:00`. Screenshot 001 compounds it — its timestamp field says `[00:07:00]` while its own
filename says `…_00-02-00.jpg`.

**Proof 3 — four of the eleven are byte-identical duplicates of four others.** Verified by
SHA-256:

| Pair | Bytes | Sold as |
|---|---|---|
| `extracted_jpeg_1001.jpg` = `raw_extracted_1001.jpg` | 32,833 | Screenshots 002 `[00:12:00]` **and** 008 `[00:42:00]` |
| `extracted_jpeg_1004.jpg` = `raw_extracted_1004.jpg` | 5,640 | Screenshots 003 `[00:17:00]` **and** 009 `[00:47:00]` |
| `extracted_jpeg_1005.jpg` = `raw_extracted_1005.jpg` | 5,380 | Screenshots 004 `[00:22:00]` **and** 010 `[00:52:00]` |
| `extracted_jpeg_1013.jpg` = `raw_extracted_1013.jpg` | 14,892 | Screenshots 005 `[00:27:00]` **and** 011 `[00:57:00]` |

**Eleven claimed screenshots are seven distinct images.**

**Proof 4 — the images are not what they are said to be.** Every file was opened and looked at:

| Entry | Claimed | **Actually is** |
|---|---|---|
| 001 `[00:07:00]`, 1280×720 | *"Reversal Candlestick Patterns — Railroad Tracks, Evening Stars, High-Volume Pins"* | **the title slide** — *"Jim's Journey in Learning and Trading MMFX"* over a photograph of a bird. No chart, no candle |
| 002 `[00:12:00]` / 008 `[00:42:00]`, 1280×720 | *"Railroad Track Structure on M15 — equal-bodied opposing candles at key market maker swing extremes"* | **the title slide again** — same image, different JPEG encode |
| 003 `[00:17:00]` / 009 `[00:47:00]`, **558×50** | *"Morning Star / Evening Star Anatomy — 3-candle reversal confirmation at session High/Low of Day"* | **a 50-pixel-tall sliver of green text reading `Hopefully my Path can Sm`** — the left half of the slide caption *"Hopefully my Path can Smooth the way for others…"* (`[00:01:12]`) |
| 004 `[00:22:00]` / 010 `[00:52:00]`, **558×50** | *"Multi-Timeframe Confluence (H4/H1/M15)"* | **the right half of the SAME SENTENCE — `ooth the way for others…`** |
| 005 `[00:27:00]` / 011 `[00:57:00]`, 592×360 | *"TDI Divergence & Momentum Hooks — regular and hidden divergence between price peaks and TDI indicator peaks"* | **a photograph of the presenter's home office** — the *"trading sanctuary"* desk shot, `[00:01:25]`. No chart, no indicator |
| 006 `[00:32:00]`, **267×51** | *"Session Recap & Execution Rules — final summary of weekly execution checklist and risk-to-reward targets"* | **the Camtasia Studio / TechSmith logo** |
| 007 `[00:37:00]`, **137×14** | *"Reversal Candlestick Patterns — Railroad Tracks, Evening Stars, High-Volume Pins"* | **the words `Camtasia Studio 6`** |

**One printed sentence, split across two SWF delta tiles, is indexed as two unrelated
candlestick and multi-timeframe topics.** That single fact is sufficient on its own.

**Proof 5 — the attribution is wrong on all eleven, in a way `D-033` makes material.** Every
entry says *"**Steve Mauro** breaking down [topic] and institutional market mechanics."*
**The course author does not speak in this lesson at all** — V08 carries 100% `GUEST` runtime
(`V08_TRANSCRIPT.md` § ONE SPEAKER). Under `D-033` provision 1 speaker attribution is mandatory
precisely because two speakers can both create doctrine; a file that misattributes every entry
to the wrong speaker is disqualified on that ground alone, independently of its content.

---

### 3. THE FINDING THAT GENERALISES — FOUR LESSONS, FOUR DESCRIPTIONS, **TWO FILES**

`COURSE_PROGRESS.md`'s V07 GATE carry-forward item (e) warns: *"Four lessons, four ways of being
wrong. Do not assume uniformity."* **This audit finds the opposite, and the opposite is more
useful:** the four ways of being wrong are **four outputs of one generator**.

`extracted_png_27.png` and `extracted_png_290.png` are **byte-identical across V05, V06, V07 and
V08** (SHA-256 `17e5622c255a…` and `9791aacf6433…`, present in exactly those four lesson folders
and no others). They are the Camtasia player's own chrome. They are described as **eight
different trading topics**:

| File | V05 | V06 | V07 | V08 |
|---|---|---|---|---|
| `extracted_png_27.png` **= the Camtasia Studio logo** | *"Level 1 Drop & Asian Box"* | *"London Open Stop Hunt Mechanics"* | *"EMA Dynamic Support & Resistance"* | *"Session Recap & Execution Rules"* |
| `extracted_png_290.png` **= the words "Camtasia Studio 6"** | *"Level 2 Retracement & EMA Cross"* | *"Reversal Candlestick Rejection"* | *"TDI Blood in the Water Setup"* | *"Reversal Candlestick Patterns"* |

Their timestamps track only their **position in the folder listing** — V05 `07:00`/`12:00`,
V06 `17:00`/`22:00`, V07 `22:00`/`27:00`, V08 `32:00`/`37:00` — stepping through the same
five-minute arithmetic sequence in each file.

> **This is a fabrication FINGERPRINT, and it is mechanically testable.** The generator (a) walks
> the extracted-asset list in filename order, (b) assigns timestamps from a fixed 5-minute
> sequence with no reference to the recording's length, and (c) writes a plausible
> lesson-appropriate trading topic for each, from a topic pool, **without looking at the image**.
> It does not distinguish a 1280×720 title slide from a 137×14 wordmark.

**Recommendation to the reviewer and to V09–V21 sessions — the `Q-007` shape, applied to
`VISUAL_INDEX.md`.** Three of these checks need no audio and no image inspection, and together
they are close to conclusive:

1. **Any timestamp exceeding the lesson's runtime** in `SOURCE_MANIFEST.md`.
2. **A constant inter-entry timestamp delta** across all entries.
3. **Any byte-duplicate pair** among the referenced files, or any referenced file smaller than
   ~300×300 pixels described as a chart or slide.

**This entry does NOT batch-discharge V09–V21**, and deliberately so: `Q-007` earned its
discharge by measuring a marker across all 15 remaining lessons, and this session has measured
four. The three checks above are offered as a **cheap screen a future session can run in
minutes**, with the per-lesson audio cross-check still owed. Recorded as an open item for
`REVIEW_INDEX.md`.

---

### Disposition

All three files remain quarantined in place at
`_QUARANTINE_UNVERIFIED_NOTES/per_lesson/08_Bootcamp1_Wk2_032612_Part3_43mins/`, covered by the
tree's blanket `README_WHY_QUARANTINED.md`. **No file was moved, renamed or deleted**
(`REMEDIATION_PROTOCOL.md` §2). The lesson's own `SCREENSHOTS/` folder is left untouched as
source-side evidence; this project's screenshots for V08 are the **26 frames in
`04_SCREENSHOTS/V08/`**, captured from the `.swf` by this session.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered (V01–V06 individually, V07–V21 by `Q-007`'s mechanical
  discharge). Zero exceptions library-wide.
- **`NOTES.md`:** **8 of 21 audited** (V01–V08), **8 fabricated, zero exceptions.**
- **`VISUAL_INDEX.md`:** **8 of 21 audited** (V01–V08), **8 fabricated.** The count of *"distinct
  failure modes"* stops being the useful statistic here: V08 exhibits **all** of the previously
  named modes at once — duplicate pairs sold as separate screenshots (V05's mode), delta-tiles
  indexed as charts (V06's), player chrome indexed as content (V07's) — **plus** two new
  mechanical tells, timestamps past the end of the recording and a generated arithmetic timestamp
  sequence. **The right conclusion is not that there are five modes but that there is one
  generator**, and §3 above shows it directly.

---

## Q-010 — V09's `NOTES.md` and `VISUAL_INDEX.md`, confirmed fabricated; the "one generator" finding is now MEASURED across all 21 lessons for `VISUAL_INDEX.md`, and V09's own audio refutes the EMA nickname table

```text
STATUS:        QUARANTINED — DO NOT USE
DATE:          2026-08-13
QUARANTINED BY: V09 Student session
DECISION:      D-017 (Q-001 blanket action). RULES.md is NOT re-derived from audio here —
                it is discharged by Q-007's mechanical template-marker test, as Q-007
                explicitly authorizes and COURSE_PROGRESS.md's V08 GATE carry-forward
                item (e) instructs. It IS re-measured mechanically, for a different
                purpose: see §3.
```

### Scope

| File | Disposition | Basis |
|---|---|---|
| `RULES.md` | Already quarantined, **not re-audited from audio** | `Q-007`, the mechanical template-marker discharge for `V07`–`V21` |
| `NOTES.md` | **Fabricated — confirmed here** | Per-lesson audio cross-check, §1 |
| `VISUAL_INDEX.md` | **Fabricated — confirmed here** | Per-lesson image cross-check, §2 |
| `TRANSCRIPT.md` | **SOUND — adopted** | `SETUP_ISSUES.md` I-008, four axes, recorded in `02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md` § VERIFICATION |

### Method

Token counts are matches over the **verbatim body only** of
`02_TRANSCRIPTS/V09/V09_TRANSCRIPT.md` (header and timestamp lines excluded), **9,164 words**.
Every image claim is checked against the files actually present in the lesson folder's
`SCREENSHOTS/`, by SHA-256, by reading real pixel dimensions, **and by opening and looking**.

---

### 1. `NOTES.md` — fabricated

| `NOTES.md` claims | Occurrences in V09's 9,164-word body |
|---|---|
| *"Session Timing: Asian Session 7:00 PM – 3:00 AM EST / London 3:30 AM – 9:00 AM EST / New York 9:30 AM – 5:00 PM EST"* | **`7:00` 0, `3:00 am` 0, `3:30` 0, `9:00` 0, `9:30` 0, `5:00 pm` 0. Six clock figures, six zeroes.** `asian` **0** (the lesson says *"the asia range"* once, `[00:46:52]`) |
| *"Peak Formation High (PFH) & Low (PFL): Structural anchors formed at cycle turns"* | `peak formation` **3** — and **`PFH` 0, `PFL` 0**. The three real uses are unglossed chart-walkthrough labels (`[00:32:32]`, `[00:38:00]`, `[00:39:21]`); the abbreviations are invented |
| *"M & W Pattern Anatomy: 2nd leg must fail to make a new extreme, showing rejection candles (Railroad tracks or pin bars)"* | **`railroad` 0, `pin bar` 0, `rejection` 0, `new extreme` 0** |
| *"Time Gap: 30 to 90 minutes between peak 1 and peak 2 on M15 charts"* | **`30 to 90` 0, `M15` 0.** No time gap of any length is stated anywhere in this lesson |
| *"TDI Indicator: Green Price Line crossing Red Signal Line after breaking outside Blue Volatility Bands (Shark Fin)"* | **`TDI` 0, `shark` 0, `signal line` 0, `volatility band` 0, `divergence` 0** |
| *"Institutional Mechanics: … institutional order flow … news events"* | **`institutional` 0, `order flow` 0, `news` 0** |
| *"Topic Focus: Trade Entry Filtering, Position Sizing, Minimum R:R Targets"* | **Position sizing and R:R targets are genuinely this lesson's subject** — the only claim in the file that is true, and it is a topic label, not a rule |

**And the entry that is not merely unsupported but REFUTED by this lesson's own words:**

> *"**EMAs: 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry).**"*

| Token | Occurrences in V09 |
|---|---|
| `mustard`, `water`, `mayo`, `ketchup`, `raspberry` | **0, 0, 0, 0, 0** |
| `blueberry` | **6** |
| `grape` | **3** |

`[00:41:43]`, in the presenter's own words, answering an audience question:

> *"**The blueberry is the 800 on the 15 minute time frame.**"*

**`NOTES.md` says the blueberry is the 200 and invents *"raspberry"* for the 800. The lesson
says the blueberry IS the 800.** This is the first time a lesson's own audio directly refutes
the quarantined nickname table rather than merely failing to support it, and it independently
reproduces the **off-by-one** finding `A-020`'s closure block already recorded from the other
direction: the fabricated table is the real sequence shifted one rung, with `ketchup` dropped
and `raspberry` invented for the end. **`raspberry` occurs 0× in genuine audio anywhere in the
corpus, across nine audited lessons.**

### 2. `VISUAL_INDEX.md` — fabricated

It indexes **three** screenshots. The folder contains **one**.

| Claim | Reality |
|---|---|
| `VIDEO_10_SCREENSHOT_001_00-02-00.jpg` — *"Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs"*, *"Setting up session boundaries and explaining accumulation mechanics"* | The file exists (1280×720, SHA-256 `60684428…`, **not** a byte-duplicate of any other lesson's). **It is V08's four-ring self-assessment diagram** — *"Validate the Method / Eliminate Skepticism / Learn to INSTANTLY recognize confirmation Candles"* around a red `?`. **No chart. No EMA. No box. No session boundary.** At `00:02:00` this lesson's real screen is the lot-size formula slide (`04_SCREENSHOTS/V09/V09_00-02-05_…`) and its audio is `[00:02:00]` *"We multiply our account balance by point / [00:02:03] O2 and divide our stop loss and pips into that number"* |
| `VIDEO_10_SCREENSHOT_002_00-15-00.jpg` — *"London Open Stop Hunt false breakout forming 2nd leg M-formation at High of Day"* | **File does not exist.** At `00:15:00` the real screen is the defined-risk recap slide (`04_SCREENSHOTS/V09/V09_00-15-00_…`, burned timecode `15:00`), whose last printed line is *"Can have MORE Losers than Winners and still have UPWARD EQUITY"* |
| `VIDEO_10_SCREENSHOT_003_00-30-00.jpg` — *"TDI Shark Fin setup with green line hooking inside volatility bands + 5/13 EMA cross"* | **File does not exist.** At `00:30:00` the real screen is a live MetaTrader chart watermarked `EC` (EUR/CAD), verified by opening the frame. `TDI` and `shark` occur **0×** in this lesson |

> **WHERE THE ONE REAL IMAGE CAME FROM — and a correction this entry makes against itself.**
>
> The first reading recorded in this session's working notes was that the jpg had been *stolen
> from V08's folder*. **That reading is wrong and is corrected here rather than deleted.** V09's
> `.swf` renders **that same ring diagram as its own pre-playback splash frame** — this session
> captured it directly from V09's own file before clicking play, and it is also this lesson's
> genuine screen for the first ~15 seconds (`04_SCREENSHOTS/V09/V09_00-00-10_…`, burned timecode
> `00:10`).
>
> So the image is **authentically V09's**. What is fabricated is everything asserted about it:
> its timestamp, its content description, and its trading significance. **That is a worse
> failure mode than theft, not a better one** — a stolen frame can be caught by hashing against
> other lessons, which is exactly the screen `Q-009` proposed. **A real frame from the right
> lesson with an invented description defeats that screen entirely**, and V09 is the first
> audited instance of it. The screen that does catch it is the one `Q-009` listed third and
> this session actually used: **open the image and compare it against the transcript at the
> claimed time.**

### 3. THE "ONE GENERATOR" FINDING, NOW MEASURED — and it extends to `VISUAL_INDEX.md`

`Q-009` established that V08's fabrication was *"one generator, not four failure modes"*, from
byte-identical PNGs. This session tested the stronger claim — that the **prose itself** is
stamped from a template — mechanically, across all 21 lessons, by normalising away the only
per-lesson tokens (`Bootcamp1 …swf`, `VNN-RNNN`, `VIDEO_NN_SCREENSHOT`, the `(Week … Part …)`
suffix) and hashing what remained:

| File | Distinct normalised hashes across 21 lessons | V09's group |
|---|---|---|
| `RULES.md` | **2** — 16 lessons share one hash, 5 share the other | The 16-lesson group, **which also contains V01**, whose copy `D-017` proved false against verified audio |
| `VISUAL_INDEX.md` | **9** — the largest group holds **9 lessons** | The 9-lesson group (V03, V04, **V09**, V10, V11, V12, V13, V14, V21) |
| `NOTES.md` | **17** — mostly per-lesson, one group of 5 (V16–V20) | V09's is unique |

**`RULES.md` was already known to be templated (`Q-004`, `Q-007`). `VISUAL_INDEX.md` was not**,
and the register's running tally has been counting its *"distinct failure modes"* lesson by
lesson. **Nine lessons share one byte-identical `VISUAL_INDEX.md` after normalisation.** Its
three screenshot descriptions — Asian Box + five EMAs, London stop hunt M-formation, TDI shark
fin — are **the same three sentences in nine different lessons**, and at least two of the three
name files that do not exist.

Direct consequence: **`NOTES.md` is where the residual per-lesson variation lives, and it is
therefore the only one of the three that still needs a genuine per-lesson audit.** For
`VISUAL_INDEX.md` a future session can now cite this measurement, then run the one check the
template cannot survive — *does the described image exist, and is it what the transcript says
is on screen at that time?*

**This entry does NOT batch-discharge V10–V21.** The measurement above establishes shared
provenance; it does not establish falsity for a lesson whose audio nobody has read. The
per-lesson audio cross-check is still owed for all of `NOTES.md`, and the existence/content
check for `VISUAL_INDEX.md`.

### Disposition

All three files remain quarantined in place at
`_QUARANTINE_UNVERIFIED_NOTES/per_lesson/09_Bootcamp1_Wk2_032612_Part4_53mins/`, covered by the
tree's blanket `README_WHY_QUARANTINED.md`. **No file was moved, renamed or deleted**
(`REMEDIATION_PROTOCOL.md` §2). The lesson's own `SCREENSHOTS/` folder is left untouched as
source-side evidence; this project's screenshots for V09 are the **26 frames in
`04_SCREENSHOTS/V09/`**, captured from the `.swf` by this session.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered. **Now also shown to be TWO templates library-wide**, with
  V09 in the same 16-lesson group as V01.
- **`NOTES.md`:** **9 of 21 audited** (V01–V09), **9 fabricated, zero exceptions.** V09 supplies
  the first *refutation* rather than mere non-support, and it lands on the EMA nickname table.
- **`VISUAL_INDEX.md`:** **9 of 21 audited** (V01–V09), **9 fabricated** — and now measured as
  **9 distinct templates across the library, one of which covers 9 lessons including V09.**
  V09 adds a sixth failure mode and it is the one that defeats the cheapest screen: **a genuine
  frame from the correct lesson, carrying an entirely invented description.**
