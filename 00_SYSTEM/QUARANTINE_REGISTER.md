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

---

## Q-011 — V10's `NOTES.md` and `VISUAL_INDEX.md`, confirmed fabricated; and `RULES.md` is shown to be **V01's file with six identifier strings swapped**

```text
STATUS:        QUARANTINED — DO NOT USE
DATE:          2026-08-13
QUARANTINED BY: V10 Student session
DECISION:      D-017 (Q-001 blanket action). RULES.md is already quarantined and is NOT
                re-derived from audio for its own sake — Q-007's mechanical template-marker
                test discharges V07-V21. It IS re-measured here, for a different and
                stronger purpose: see §3, which upgrades Q-010's "two templates" result
                from a normalised-hash grouping to an EXACT TEXT IDENTITY.
```

### Scope

| File | SHA-256 (quarantined copy) | Disposition | Basis |
|---|---|---|---|
| `NOTES.md` | `a97ead37943dfd2383e672509772ea1f5a23c1a78466ae04f1e2150acad15252` | **Fabricated — confirmed here** | Per-lesson audio cross-check, §1 |
| `VISUAL_INDEX.md` | `a1cb25d10079b801499330cc7e87cbd5deb271cdcfad99fafd4d0027eefb2de0` | **Fabricated — confirmed here** | Per-lesson image cross-check, §2 |
| `RULES.md` | `3d769300409849ae882264394c9e2840bba58c964337b347cf41b4ab44671653` | Already quarantined; **re-measured**, not re-derived | `Q-007`; §3 |
| `TRANSCRIPT.md` | — | **SOUND — adopted** | `SETUP_ISSUES.md` `I-008`, four axes, recorded in `02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` § VERIFICATION |

### Method

Token counts are matches over the **verbatim body only** of
`02_TRANSCRIPTS/V10/V10_TRANSCRIPT.md` (the pre-ingestion `# VIDEO` header and all timestamp
lines excluded), **14,335 words**. Counts use **word boundaries**, not substring matching —
see the disclosure at the end of §1, which is a correction this session made against itself.
Every image claim is checked against the files actually present in the lesson folder's
`SCREENSHOTS/`, by SHA-256, by reading real pixel dimensions, **and by opening and looking**,
and additionally against **this session's own 1,164-frame sweep of the same `.swf`**.

---

### 1. `NOTES.md` — fabricated

| `NOTES.md` claims | Occurrences in V10's 14,335-word body |
|---|---|
| *"Session Timing: Asian Session 7:00 PM – 3:00 AM EST / London 3:30 AM – 9:00 AM EST / New York 9:30 AM – 5:00 PM EST"* | **`7:00` 0, `3:00 am` 0, `3:30` 0, `9:00` 0, `9:30` 0, `5:00 pm` 0. Six clock figures, six zeroes.** V10 discusses sessions constantly (`asian` **13**) and **never once states a clock time for any of them** |
| *"EMAs: 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry)"* | **`mustard` 0, `raspberry` 0, `ketchup` 0.** `mayo` **1** and `blueberry` **2** — all three inside one line, `[01:25:28]` *"Pins to the blueberry baby pins to the Mayo pins to the blueberry"*, which uses them as chart-line names and **maps neither to a period**. `water` **1**, and it is not an average: `[01:24:29]` *"Shark fin blood in the water"* |
| *"Time Gap: 30 to 90 minutes between peak 1 and peak 2 on M15 charts"* | **`30 to 90` 0, `M15` 0.** No time gap of any length is stated. The one interval V10 does give is different in both number and subject — `[00:39:14]` *"comes above leg two for 15 to 30 minutes and comes back below"* |
| *"M & W Pattern Anatomy: 2nd leg must fail to make a new extreme, showing rejection candles (Railroad tracks or pin bars)"* | **`pin bar` 0, `rejection` 0, `new extreme` 0.** `railroad` **4**, but never as a required confirmation — it is narration of specific charts (`[00:38:19]`, `[01:04:50]`) |
| *"TDI Indicator: Green Price Line crossing Red Signal Line after breaking outside Blue Volatility Bands (Shark Fin)"* | **`signal line` 0, `volatility band` 0, `divergence` 0.** `TDI` **1** — and it is a *deferral*, not a teaching: `[01:13:03]` *"do we use TDI to confirm these yes, that's next week's lesson my friend"* |
| *"Institutional Mechanics: … institutional order flow … panic/fear via spike candles and news events"* | **`institutional` 0, `order flow` 0, `spike` 0, `panic` 0, `news` 0** |
| *"Topic Focus: H4 Anchor Analysis, H1 Alignment, M15 Execution Timing"* — i.e. multi-timeframe analysis | **The lesson explicitly REFUSES this framing.** `[01:13:47]`–`[01:13:56]`: *"people posted in the form … that I'm using multiple time frame analysis. That's what you want to call it. That's fine, but that's not what we're doing here"* |

**The last row is the sharpest.** It is not an unsupported claim — it is a claim the lesson
**contradicts in terms**, about the lesson's own headline topic. `NOTES.md`'s framing device is
the one thing V10 goes out of its way to disown.

> **⚠ A COUNTING ERROR THIS SESSION MADE AND CAUGHT, DISCLOSED BECAUSE THE METHOD IS THE POINT.**
> An early screen of this lesson counted **`EMA` = 24** by substring match. That figure is
> **wrong and is retained here rather than deleted.** Twenty-two of the twenty-four are the word
> **`email`**, of which this lesson (a Q&A-heavy session opening on a mailbag) has a great many.
> The word-boundary count is **`EMA` = 2**, both incidental: `[00:59:45]` *"the EMA's are open
> wide open"* and `[01:02:53]` *"He uses the 200 EMA of support"*. **`800` = 0.**
>
> This matters beyond bookkeeping: a substring count would have let `NOTES.md`'s five-EMA table
> look *partially* supported by a busy token, when the truth is that V10 names exactly one
> moving average, once. **A fabrication screen that over-counts in the fabrication's favour is
> not a screen.** Every count in this record is word-boundary.

---

### 2. `VISUAL_INDEX.md` — fabricated, and it is the **second confirmed instance of `Q-010`'s sixth failure mode**

`VISUAL_INDEX.md` describes **three** screenshots. The lesson folder contains **one**.

| # | Claimed | Reality |
|---|---|---|
| 001 | `[00:02:00]` — *"Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs"* | **The file exists** (`b61063e68092fb97de640c31fc6faaac87566a137580da2b3ee07560507c014b`, 1024×768) **and it is a genuine frame of this lesson — the TITLE CARD**, reading *"Market Makers Boot Camp / Week 3"*. It contains **no chart, no box, no moving average of any kind.** Its timestamp is also wrong: this session's own sweep shows the screen at `01:39` and `01:58` is the *"Chat Box…"* housekeeping slide, and the title card precedes it |
| 002 | `[00:15:00]` — *"London Open Stop Hunt false breakout forming 2nd leg M-formation at High of Day"* | **No such file.** At `[00:15:02]` the lesson is answering a mailbag question about *"the price won't come back to a certain price point"* |
| 003 | `[00:30:00]` — *"TDI Shark Fin setup with green line hooking inside volatility bands + 5/13 EMA cross"* | **No such file.** At `[00:30:01]` the lesson is narrating *"the dealer fails to extend above the previous set"*. `TDI` is **deferred to next week** at `[01:13:03]`; `5/13` occurs **0** times in the lesson |

**Q-010 recorded a sixth failure mode — a genuine frame from the correct lesson carrying an
entirely invented description — and noted that hashing across lessons cannot catch it. V10 is
the second instance, and it is starker than V09's:** the frame here is a **title card**. There
is no reading of it, at any resolution, on which it depicts an Asian accumulation range with
five moving averages. The description is not a mislabel of an ambiguous chart; it is unrelated
to the pixels.

**The cheap screens and what each would have done:**

| Screen | Verdict on V10 |
|---|---|
| Timestamp past runtime | **Would NOT fire** — all three claimed stamps are inside 96 minutes |
| Constant timestamp delta | **Would fire** — `00:02:00 / 00:15:00 / 00:30:00`, and the file stops describing at minute 30 of a 96-minute lesson |
| Byte-duplicate across lessons | **Would NOT fire** — this image is unique in the library |
| Count files vs count entries | **Would fire** — 3 described, 1 present |
| **Open the image and look at it** | **Fires immediately, and is the only screen that catches the description** |

---

### 3. `RULES.md` — the strongest result in this record: it is **V01's file with six identifier strings swapped**

`Q-010` measured `RULES.md` as **two templates** library-wide by normalised hash, with V09 in
V01's group. This session tested the stronger claim directly, with `diff`, and it holds:

```text
diff  _QUARANTINE.../01_Bootcamp1_Wk1_031812_Part1_55mins/RULES.md
      _QUARANTINE.../10_Bootcamp1_Wk3_040112_96mins/RULES.md
```

returns **six changed lines, and all six are the lesson's name:**

| Line | V01 | V10 |
|---|---|---|
| title | `… - Bootcamp1 Wk1 031812 Part1 (55mins).swf` | `… - Bootcamp1 Wk3 040112 (96mins).swf` |
| rule id | `V01-R001` | `V11-R001` |
| visual | `VIDEO_01_SCREENSHOT_001_00-02-00.jpg` | `VIDEO_11_SCREENSHOT_001_00-02-00.jpg` |
| rule id | `V01-R002` | `V11-R002` |
| visual | `VIDEO_01_SCREENSHOT_002_00-15-00.jpg` | `VIDEO_11_SCREENSHOT_002_00-15-00.jpg` |
| setup | `Asian Box Stop Hunt Reversal (Week 1 - Part 1)` | `Asian Box Stop Hunt Reversal (Week 3)` |

**Every other line is byte-identical** — every rule, every `**Source:** Explicit` label, every
timestamp, every numeric parameter, every "Instructor Statement", the ambiguity section, the
contradiction section (*"None detected within this video"*), and the coding implications.

**`D-017` already proved V01's copy false against verified audio.** The same sentence, at the
same claimed marker, is therefore false here too — and V10's own audio is independently
decisive:

| `RULES.md` asserts, **`Source: Explicit`** | What is actually at that marker in V10 |
|---|---|
| `[00:05:00]` *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | `[00:04:59]`–`[00:05:09]` **a CompassFX seminar announcement** — *"On behalf of market makers 4x … we're gonna be hosting a seminar Tuesday April 3rd"*. `5/13` occurs **0** times in the lesson; `M15` **0**; `crossover` **0** |
| `[00:18:00]` *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* | `[00:18:04]` **homework housekeeping** — *"We are not in grade school. I don't need to see your homework and bring it home and hang it on my fridge with a magnet"*. `stop loss` occurs **0** times; `10 to 15` **0** |
| `[00:04:00]` the five-EMA parameter table, all five rows `Explicit` | `[00:04:03]` *"these are some of the problems that I'm coming across on the emails"*. **`EMA` = 2 in the whole lesson, `800` = 0** |
| `[00:22:00]` *"Peak Time Gap 30-90 mins"*, `Explicit` | `[00:22:09]` *"The dealer comes back issues a triple bottom in the shadow brinksy, baby"*. `30 to 90` = **0** |
| *"# CONTRADICTIONS — None detected within this video."* | This session files **`C-016`** and **`C-017`** from V10's own audio |

**Six citations, six misses, zero partial hits.** The failure is not drift or paraphrase; the
document was never about this lesson.

### 4. Template census — this session's own measurement

Normalising away per-lesson identifier tokens and digits, then hashing, across all 21 lessons:

| File | Distinct templates | Where V10 sits |
|---|---|---|
| `NOTES.md` | **17** | a **singleton** — so V10's `NOTES.md` is per-lesson generated, and needed the real audit in §1. **This reproduces `Q-010`'s count of 17 exactly** |
| `VISUAL_INDEX.md` | **8** under this session's stricter normalisation | in the **largest group, n = 10** (V03, V04, V09–V15, V21). `Q-010` measured 9 groups with one covering nine lessons; the two measurements agree in substance and differ only by normalisation strictness, which is **stated rather than reconciled away** |
| `RULES.md` | **5** under this session's stricter normalisation | a singleton **by hash** — but §3 shows that is an artifact of the normaliser, which masks digits but not the words *"Wk1 … Part1"* vs *"Wk3"*. **By `diff`, V10 and V01 are the same document.** `Q-010`'s two-template reading is the correct one and this session's hash grouping is the weaker instrument |

> **The methodological point, and it is against this session's own first instrument.** A
> normalised hash reported V10's `RULES.md` as *unique*. A `diff` reported it as *V01's file*.
> **The hash was wrong because the normaliser did not anticipate the identifier's shape**, and
> a session trusting it would have recorded V10's rules as independently generated — which is
> precisely the opposite of the truth, and would have made them look more credible. Both
> measurements are recorded above. `Q-010` was right; this session's stricter normalisation was
> not more rigorous, it was differently blind.

### Disposition

All three files remain quarantined in place at
`_QUARANTINE_UNVERIFIED_NOTES/per_lesson/10_Bootcamp1_Wk3_040112_96mins/`, covered by the
tree's blanket `README_WHY_QUARANTINED.md`. **No file was moved, renamed or deleted**
(`REMEDIATION_PROTOCOL.md` §2). The lesson folder's own `SCREENSHOTS/` is left untouched as
source-side evidence; this project's screenshots for V10 are the curated frames in
`04_SCREENSHOTS/V10/`, captured from the `.swf` by this session.

### One thing the quarantined material got right, recorded because the register must cut both ways

The single real image is the lesson's **title card, and it prints *"Week 3"***. That is an
**independent, in-recording corroboration of `D-017` §2's ordering for this file**, whose week
number until now rested on the filename (`Wk3 040112`) and the session-date derivation alone.
It is also the reason `V10` can assert a printed banner where `V09` could assert no title at
all. The *description* attached to it is fabricated; the *pixels* are evidence.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered. **Now shown by exact `diff` — not merely by normalised hash —
  to be a single document re-badged**, with V10 and V01 differing in six identifier strings only.
- **`NOTES.md`:** **10 of 21 audited** (V01–V10), **10 fabricated, zero exceptions.** V10 adds
  the first instance of a claim the lesson **contradicts in terms** (multi-timeframe analysis).
- **`VISUAL_INDEX.md`:** **10 of 21 audited** (V01–V10), **10 fabricated.** V10 is the **second
  confirmed instance of the sixth failure mode** — a genuine frame carrying an invented
  description — and confirms it is a repeating generator behaviour rather than a V09 one-off.

---

## Q-012 — V11's `NOTES.md` and `VISUAL_INDEX.md`, confirmed fabricated; the one real image is the **TITLE CARD**, indexed as *"Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs"*

```text
STATUS:        QUARANTINED — DO NOT USE
DATE:          2026-08-13
QUARANTINED BY: V11 Student session (branch video/v11, isolated worktree, D-038)
DECISION:      D-017 (Q-001 blanket action). RULES.md is NOT re-derived here — it is
               discharged by Q-007's mechanical template-marker test, as Q-007
               explicitly authorizes. The markers were nonetheless re-measured on this
               file (below) because the check is one command.
LOCATION:      01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/
               per_lesson/11_Bootcamp1_Wk4_040812_Part1_51mins/
               (in place; nothing moved, renamed or deleted)
```

### Scope — what this entry does and does not cover

| File | Disposition | Basis |
|---|---|---|
| `RULES.md` | Already quarantined, **not re-audited on the merits** | **`Q-007`**. Markers re-measured here as a free cross-check and all three hold |
| `NOTES.md` | **Fabricated — confirmed here** | Per-lesson audio cross-check, §2 |
| `VISUAL_INDEX.md` | **Fabricated — confirmed here** | Per-lesson image cross-check, §3 |
| `TRANSCRIPT.md` | **SOUND — adopted** | `SETUP_ISSUES.md` `I-008`, all four criteria, plus four Whisper spot-checks. Recorded in `02_TRANSCRIPTS/V11/V11_TRANSCRIPT.md` § VERIFICATION |

**Measurement note.** Every count in this entry was taken with **word-boundary matching against
the spoken body only**, after stripping the `[HH:MM:SS]` marker lines. This matters and is stated
because it caught an error in this session's own first pass: a naive case-insensitive
`grep -c "EMA"` returns **11** on the raw file — it matches *email*, *them a*, *problem* — and a
naive `grep -c "9:30"` returns **3** by matching **timestamps**. Both figures are artifacts. The
correct figures are below, and a future session repeating this audit should strip the markers
first.

---

### 1. `RULES.md` — Q-007's discharge re-confirmed, and V11 reproduces the Q-011 finding exactly

| Template marker | V11 |
|---|---|
| Rule 1 quote at `[00:05:00]` — *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | ✅ present |
| Rule 2 quote at `[00:18:00]` — *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* | ✅ present |
| Exactly two `## Rule ID:` entries | ✅ 2 |
| `NUMERICAL PARAMETERS` block hash | ✅ `e75ace74e1f12759…` — **identical to V01's and to V10's** |

> ### ⭐ `Q-011`'s FINDING REPRODUCES ON A SECOND LESSON
>
> `Q-011` showed that V10's `RULES.md` is **V01's file with six identifier strings swapped**.
> **V11's is the same.** An exact `diff` of V01's and V11's `RULES.md` returns **12 differing
> lines — six substitutions and nothing else**:
>
> ```text
> filename header      Wk1 031812 Part1 (55mins)  ->  Wk4 040812 Part1 (51mins)
> Rule ID x2           V01-R001 / V01-R002        ->  V12-R001 / V12-R002
> Relevant Visual x2   VIDEO_01_SCREENSHOT_00x    ->  VIDEO_12_SCREENSHOT_00x
> Setup Name           (Week 1 - Part 1)          ->  (Week 4 - Part 1)
> ```
>
> **Zero content lines differ.** Every rule, every timestamp, every parameter, every ambiguity
> and every "Coding Implication" is byte-identical across two lessons recorded three weeks apart
> on entirely different subjects. `Q-011` called this *"one generator"*; V11 is the second exact
> demonstration, and it upgrades the claim from *inferred from a normalised hash* to
> **twice-demonstrated by exact diff**.

**Note the `V12-` prefix.** The generator numbered this file against the **pre-`D-017` alphabetical
ordering**, in which `Wk10` sorted third. Under `D-017` §2 this lesson is **V11**. Recorded so no
future session reads `V12-R001` as a reference to the corpus's V12.

---

### 2. `NOTES.md` — fabricated. Its central vocabulary is absent from the audio

`NOTES.md` §3 asserts, without hedge:

> *"**EMAs:** 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry)."*
> *"**TDI Indicator:** Green Price Line crossing Red Signal Line after breaking outside Blue Volatility Bands (**Shark Fin**)."*

**Measured against the transcript body (word-boundary, markers stripped):**

| Token asserted by `NOTES.md` | Occurrences in 51 minutes |
|---|---|
| `EMA` / `EMAs` | **0** |
| `moving average` | **0** |
| `5/13` | **0** |
| `M15` | **0** |
| `shark` (hence *Shark Fin*) | **0** |
| `PFH`, `PFL` | **0** each |
| `mustard`, `water`, `blueberry`, `raspberry` | **0** each |
| `accumulation` | **0** |
| `institutional`, `order flow` | **0** each |
| `railroad`, `pin bar` | **0** each |
| `New York` | **0** |
| any clock time (`7:00`, `3:00`, `9:00`, `9:30`, `5:00`) | **0** |

**`RULES.md` presents as `Source: Explicit`, at `[00:05:00]`, a quotation whose central token
occurs zero times in the lesson.** `[00:05:00]` is in fact *"W formation don't you understand I
can't say it enough"*, in a passage about the second leg and the TDI bands.

#### 2a. The three specific claims, checked one by one

| `NOTES.md` claim | What the lesson actually says |
|---|---|
| *"**Session Timing:** Asian 7:00 PM – 3:00 AM EST; London 3:30 AM – 9:00 AM EST; New York 9:30 AM – 5:00 PM EST"* | **No clock time of any kind is spoken in this lesson.** `london` occurs **once** (`[00:49:30]`, *"from mid london into the us session"*) and `asian` **once** (`[00:06:01]`). The table is imported from elsewhere |
| *"**Time Gap:** 30 to 90 minutes between peak 1 and peak 2 on M15 charts"* | ⚠ **The number is real and the claim attached to it is not.** `[00:14:25]`–`[00:14:39]`: *"Understand that the **low** has to hold. How long? **30 to 90 minutes.** 30 minutes is for railroad tracks, but the long sideways consolidation should last **up to two hours**, then calmly take a trade."* It is a **hold duration for a candidate low**, not a **gap between two peaks**; `M15` is never mentioned; and the *"up to two hours"* half is dropped entirely. **This is the most dangerous item in the file**, because a real number carried on a false claim survives spot-checking |
| *"**M & W Pattern Anatomy:** 2nd leg must fail to make a new extreme, showing rejection candles (Railroad tracks or pin bars)"* | The lesson's actual anatomy statement is `[00:10:26]`–`[00:11:07]` — the formation *"needs to have a **pullback and another leg**"*, and *"needs to look like that"* (**aggressive and big**). It says nothing about the second leg failing to make a new extreme; `[00:12:31]` prefers *"a couple hammers to the downside wick and then rise"*. *"Railroad tracks"* **is** a real course term — confirmed present in a Whisper pass of `[00:14:31]` — but it is used there of the **30-minute hold case**, not of a rejection candle at a second leg |

**Verdict: `NOTES.md` is FABRICATED.** Its failure mode is the one `Q-009` named — a generic
market-maker template with a handful of genuine tokens embedded, which is exactly what makes it
survive a careless read.

---

### 3. `VISUAL_INDEX.md` — fabricated, and this is the **third** confirmed instance of the sixth failure mode

`VISUAL_INDEX.md` indexes **three** screenshots. The lesson folder contains **one**.

| Indexed | File on disk |
|---|---|
| `VIDEO_12_SCREENSHOT_001_00-02-00.jpg` | ✅ exists |
| `VIDEO_12_SCREENSHOT_002_00-15-00.jpg` | ❌ **does not exist** |
| `VIDEO_12_SCREENSHOT_003_00-30-00.jpg` | ❌ **does not exist** |

Two of the three entries describe, in confident detail, images that were never captured —
including *"London Open Stop Hunt false breakout forming 2nd leg M-formation at High of Day"* and
*"TDI Shark Fin setup with green line hooking inside volatility bands + 5/13 EMA cross"*.

#### 3a. And the one image that DOES exist is described as something it is not

`VISUAL_INDEX.md` Screenshot 001:

> *"**Visual Type:** Chart / Slide Overview.
> **What is visible:** Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs.
> **Instructor's Explanation:** Setting up session boundaries and explaining accumulation mechanics."*

**The image is the lesson's TITLE CARD.** It is a dark damask slide bearing a white box reading
**`MARKET MAKERS BOOT CAMP`** / **`Week 4`**, and **nothing else**. There is no chart, no box, no
candle, no axis, and no moving average of any kind anywhere in the frame. It was opened and
looked at by this session, and independently reproduced from the `.swf` by the frame sweep.

This is the **third** confirmed instance of the sixth failure mode — a genuine frame carrying an
invented description — after `Q-010` (V09) and `Q-011` (V10). `Q-008` (V07) is the same family
one step further: there the indexed "TDI setup" was the **Camtasia player's own splash logo**.

#### 3b. Cross-lesson duplicate check — negative, and worth recording as negative

The MD5 of every lesson's `SCREENSHOT_001` was compared across all 21 folders: **21 distinct
hashes, no duplicate pair.** V11's single image is a genuine, unique frame from V11. **The
fabrication here is entirely in the prose, not in the pixels** — which is precisely why an
image-count check alone would have passed this file.

---

### 4. One thing the quarantined material got right — the register cuts both ways

The single real image prints **`Week 4`**. That is an **independent, in-recording corroboration
of `D-017` §2's ordering for this file**, whose week number otherwise rests on the filename
(`Wk4 040812`) and the session-date derivation. It agrees with the spoken *"welcome to week four
of market maker boot camp"* `[00:00:00]` and with the `2012-04-08` Easter Sunday reference at
`[00:25:33]`. **The description attached to the frame is fabricated; the pixels are evidence.**

---

### 5. Disposition

All three files remain quarantined **in place**, covered by the tree-wide
`README_WHY_QUARANTINED.md` banner. Nothing was moved, renamed or deleted. **No V11 artifact
draws on any of them**, and `V11_SOURCE_NOTES.md` was written from the transcript alone before
these files were opened.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered. **Now shown by exact `diff` on TWO lessons — V10 (`Q-011`) and
  V11 (this entry) — to be a single document re-badged by six string substitutions.** The
  "one generator" claim no longer rests on a normalised hash.
- **`NOTES.md`:** **11 of 21 audited** (V01–V11), **11 fabricated, zero exceptions.** V11 adds the
  clearest instance yet of a **real number carried on a false claim** (*"30 to 90 minutes"*
  re-attributed from a low's hold duration to a peak-to-peak gap).
- **`VISUAL_INDEX.md`:** **11 of 21 audited** (V01–V11), **11 fabricated.** V11 is the **third**
  confirmed instance of the sixth failure mode, and the first in which the misdescribed frame is
  a **title card** — i.e. a frame containing no chart content at all.

---

## Q-013 — V12's `NOTES.md` and `VISUAL_INDEX.md`, confirmed fabricated; and `VISUAL_INDEX.md` is now shown by **exact `diff`** to be ONE document shared by **TEN lessons**, with V11's and V12's differing by **four identifier lines and ZERO content lines**

```text
STATUS:        QUARANTINED — DO NOT USE
DATE:          2026-08-13
QUARANTINED BY: V12 Student session (branch video/v12, isolated worktree, D-038)
DECISION:      D-017 (Q-001 blanket action). RULES.md is NOT re-derived here on the
               merits — it is discharged by Q-007's mechanical template-marker test,
               as Q-007 explicitly authorizes. An exact diff was nonetheless run
               because it is one command, and it is the THIRD such demonstration.
LOCATION:      01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/
               per_lesson/12_Bootcamp1_Wk4_040812_Part2_55mins/
               (in place; nothing moved, renamed or deleted)
```

### Scope

| File | Disposition | Basis |
|---|---|---|
| `RULES.md` | Already quarantined, **not re-audited on the merits** | **`Q-007`**. Exact `diff` against V01 re-run here as a free cross-check — §1 |
| `NOTES.md` | **Fabricated — confirmed here** | Per-lesson audio cross-check, §2 |
| `VISUAL_INDEX.md` | **Fabricated — confirmed here** | Per-lesson image cross-check, §3 |
| `TRANSCRIPT.md` | **SOUND — adopted** | `SETUP_ISSUES.md` `I-008`, all four criteria, plus **seven** Whisper `small.en` spot-checks. Recorded in `02_TRANSCRIPTS/V12/V12_TRANSCRIPT.md` § VERIFICATION |

**Measurement note — `Q-012`'s method was inherited, and it earned its keep immediately.**
Every count below uses **word-boundary matching against the spoken body only**, after stripping
`[HH:MM:SS]` marker lines. Two artifacts were caught in this session's own first pass and are
recorded rather than hidden:

- A naive `grep -ci "EMA"` over the raw file returns **7**; word-boundary against the stripped
  body returns **2**. The five extras are *them a*, *problem*, *systematically*.
- A naive `grep -ci "morning star"` returns **1**, which would have appeared to corroborate the
  `NOTES.md` claim *"Evening/Morning Stars"*. **It is a substring of `[00:30:20]` *"10 in the
  **morning star**ted the US session"*.** The true count is **0**. This is the same class of error
  as `Q-012`'s `9:30`-matches-a-timestamp trap, in a new costume, and it is the closest this
  register has come to a **false positive that would have flattered a fabricated file**.

---

### 1. `RULES.md` — the THIRD exact-`diff` demonstration of the one-generator finding

`diff 01_.../RULES.md 12_.../RULES.md` returns **12 differing lines — six substitutions — and
ZERO content lines.**

| Line | V01 | V12 |
|---|---|---|
| 1 | `…Bootcamp1 Wk1 031812 Part1 (55mins).swf` | `…Bootcamp1 Wk4 040812 Part2 (55mins).swf` |
| 3 | `## Rule ID: V01-R001` | `## Rule ID: V13-R001` |
| 15 | `VIDEO_01_SCREENSHOT_001_00-02-00.jpg` | `VIDEO_13_SCREENSHOT_001_00-02-00.jpg` |
| 19 | `## Rule ID: V01-R002` | `## Rule ID: V13-R002` |
| 31 | `VIDEO_01_SCREENSHOT_002_00-15-00.jpg` | `VIDEO_13_SCREENSHOT_002_00-15-00.jpg` |
| 41 | `Asian Box Stop Hunt Reversal (Week 1 - Part 1)` | `Asian Box Stop Hunt Reversal (Week 4 - Part 2)` |

**Every rule, threshold, timestamp, parameter, ambiguity and "coding implication" is byte-identical
across two lessons recorded three weeks apart on entirely different subjects** — V01 is week 1's
opening lesson, V12 is a 55-minute treatment of the Traders Dynamic Index. `Q-011` (V10) and
`Q-012` (V11) each demonstrated this once; **this is the third, and the identifier substituted in
is `V13`, not `V12`** — the generator inherited the pre-ingestion *"Video 13 of 21"* numbering that
`D-017` §2 corrects.

---

### 2. `NOTES.md` — fabricated, and wrong about the lesson's subject

The file's own §1 header reads **`Topic Focus: London/NY Overlap, Evening/Morning Stars, Dynamic
Targets`**, and the per-lesson `# VIDEO` block reads `Primary Topics: M & W Anatomy, Time Gaps
Between Peaks (30-90 Mins) & Rejection Signatures`.

**The lesson is a 55-minute treatment of the Traders Dynamic Index.** It is titled that, in print,
on the opening frame, held for eight and a half minutes.

| `NOTES.md` claim | Measured in the spoken body | Verdict |
|---|---|---|
| *"Evening/Morning Stars"* | `evening star` **0×**; `morning star` **0×** (the naive **1** is a substring of *"morning started"*) | ❌ **FALSE** |
| *"London/NY Overlap"* | `overlap` **0×**; `New York` **0×**; `London` **2×**, and neither is about an overlap | ❌ **FALSE** |
| *"Dynamic Targets"* | `dynamic target` **0×** | ❌ **FALSE** |
| *"Time Gap: 30 to 90 minutes between peak 1 and peak 2"* | `30 to 90` **0×** | ❌ **FALSE — and it is a MIGRATED REAL NUMBER.** `30 to 90 minutes` is **V11**'s figure for how long a candidate low must hold (`PT-039`), re-attributed here to a peak-to-peak gap. `Q-012` recorded the identical migration on V11's own file. **The same false claim is now attached to both halves of one session** |
| *"Peak Formation High (PFH) & Low (PFL)"* | `PFH` **0×**, `PFL` **0×**, `peak formation high` **0×** (`peak formation` **2×**, unabbreviated, in passing) | ❌ **FALSE as stated** |
| *"Asian Session: 7:00 PM – 3:00 AM EST"* etc. | `7:00` **0×**, `3:00` **0×**, `9:30` **0×**, `5:00 PM` **0×**. The lesson's only clock references are *"two to four o'clock in the morning eastern time"* `[00:23:35]`, *"between one and four in the morning"* and *"between eight and 10 in the morning"* `[00:30:13]`–`[00:30:20]` | ❌ **FALSE — no stated boundary matches** |
| *"M & W Pattern Anatomy: 2nd leg must fail to make a new extreme… Railroad tracks or pin bars"* | `railroad` **6×** ✅; `pin bar` **0×**; the anatomy is never stated | ⚠️ **PARTLY TRUE BY COINCIDENCE.** `railroad tracks` really is in this lesson. **Nothing else in the sentence is** |
| *"TDI Indicator: Green Price Line crossing Red Signal Line after breaking outside Blue Volatility Bands (Shark Fin)"* | Colours and mechanism are **broadly right** | ⚠️ ⭐ **TRUE-ISH, AND THIS IS THE HAZARD — SEE §4** |

#### ⚠️ The `EMAs` line — wrong on FOUR of five rows, and invariant across all 21 lessons

```text
- **EMAs:** 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry).
```

**Measured across the whole quarantined set: this line is byte-identical in 16 of the 21
`NOTES.md` files**, and the other five carry one variant with colours bolted on
(*"5 (Mustard/Yellow), 13 (Red/Water), 50 (Light Blue/Mayo), 200 (White/Blueberry), 800 (Dark
Blue/Raspberry)"*, lessons 16–20). **It is not a per-lesson observation. It is a constant.**

Against `D-043`, the authoritative mapping:

| Nickname | `D-043` (authoritative) | Fabricated table | |
|---|---|---|---|
| Mustard | **5** | 5 | ✅ right |
| Ketchup | **13** | **absent entirely** | ❌ |
| Water | **50** | **13** | ❌ |
| Mayonnaise | **200** | **50** | ❌ |
| Blueberry | **800** | **200** | ❌ |
| — | — | **800 = "Raspberry"** | ❌ **a nickname that occurs ZERO times in V01–V12's audio, in `MMM-NOTES`, and in every `EXTERNAL_VOCABULARY_REFERENCE.md` tier** |

**Four of five rows wrong, one invented from nothing, one real nickname missing.** The table is the
five real periods and four of the five real nicknames, **shifted by one position** — which is
precisely the shape of an error that survives a careless glance.

> ### ⭐ AND V12 IS THE LESSON THAT REFUTES IT FROM THE TAPE
>
> `[00:31:22]`–`[00:31:27]`, course author, two adjacent sentences, one object:
> ***"Price comes out and it's held by the mayonnaise perfectly. Held by the 200."***
> Confirmed by an independent Whisper `small.en` pass (`c5`), and the slide **on screen at that
> moment** prints **`TDI VB BREAK, PRICE HELD BY 200`** (`V12_00-31-31_…png`).
>
> **The fabricated table says mayo = 50. The lesson it is attached to says mayo = 200, in print
> and in speech, at the same instant.** `Q-010` recorded that V09's audio refutes this table;
> **V12 refutes it on the strongest evidence the corpus has produced.**

---

### 3. `VISUAL_INDEX.md` — the FIRST exact-`diff` demonstration on THIS file, and it covers TEN lessons

`diff 11_.../VISUAL_INDEX.md 12_.../VISUAL_INDEX.md` returns **four differing lines — the filename
header and three `VIDEO_12` → `VIDEO_13` identifiers — and ZERO content lines.** Every timestamp,
`Visual Type`, `What is visible`, `Instructor's Explanation` and `Trading Significance` is
byte-identical between **Part 1 and Part 2 of the same session, which are 51 and 55 minutes of
entirely different material.**

Normalising the `VIDEO_NN` identifiers and the filename line and hashing the remainder, **ten of
the twenty-one lessons share one identical body**:

```text
03, 04, 09, 10, 11, 12, 13, 14, 15, 21
```

and a further **five** (16–20) share a second. `Q-009` measured this across all 21 by
*normalised hash*; **this entry demonstrates it by exact `diff` on a specific pair**, which is the
upgrade `Q-011`/`Q-012` made for `RULES.md` and which `VISUAL_INDEX.md` had not yet had.

#### What is actually at the three claimed timestamps

Every frame below was **opened and looked at**. The burned-in player timecode is legible in each
and is quoted from the image, not computed.

| # | Claimed | `VISUAL_INDEX.md` says | **Actually on screen** | |
|---|---|---|---|---|
| 001 | `[00:02:00]` | *"Asian Box accumulation range with **5, 13, 50, 200, and 800 EMAs**"* | **THE TITLE CARD.** Burned `02:01`. Black-on-white: **`Traders Dynamic Index`** / *"Thank You Dean & CompassFX"*. **No chart. No candles. No axis. No moving average of any period.** | ❌ |
| 002 | `[00:15:00]` | *"London Open Stop Hunt false breakout forming 2nd leg M-formation at High of Day"* | Burned `15:01`. A **teaching slide**: `Traders Dynamic Index` / *"Market Base Line forecasts Market Reversals"*, over an **EURUSD Daily** panel with four red circles drawn on the yellow baseline. Daily, not intraday; no box, no London, no M | ❌ |
| 003 | `[00:30:00]` | *"TDI Shark Fin setup with green line hooking inside volatility bands + **5/13 EMA cross**"* | Burned `30:01`. A **black text bullet slide** headed `TDI`: *"You Are In The Right Market Segment / Price Is In The Channel / RSI Line Breaks Outside The Bands As A Stop Hunt / … / Enter The Trade Stop Loss 23 Pips above the HOD / Add To The Trade At MB Break And VB Break / Exit All Units @ VB Return Crossover"*. **No chart, no green line, no bands, no EMAs** | ❌ |

**Fourth confirmed instance of the sixth failure mode** — a genuine frame carrying an invented
description — **and the SECOND CONSECUTIVE one in which the misdescribed frame is a TITLE CARD**,
indexed with **the identical sentence** used on V11 (`Q-012`).

---

### 4. ⭐ THE FINDING THIS ENTRY EXISTS FOR: THE **THIRD AND MOST COMPLETE** TIME THE GENERATOR'S TEXT IS *ABOUT THE RIGHT SUBJECT*

> **⚠️ CORRECTED AT V12 R1 item 138 (`M2`) — ⚠ SELF-VERIFIED AT OWNER DIRECTION.**
> **NOT `VERIFIED`.** This correction was applied **and** verified by **one session** on the owner's
> explicit authorisation. It does **not** satisfy `D-003` and must never be read as an arm's-length
> verdict. Full disclosure at `REVIEW_INDEX.md` item 138 and `LOG.md`.
>
> **`REMEDIATION_PROTOCOL.md` §2 — the superseded heading and opening are retained, not deleted.**
> This section was originally headed **"THE FIRST TIME THE GENERATOR'S TEXT IS *ABOUT THE RIGHT
> SUBJECT*"** and opened:
>
> > *"On eleven previous lessons the fabricated files were wrong in an obvious way — they described
> > Asian boxes and London stop hunts over lessons about equity curves, position sizing or the RSI.
> > **On V12 they are not obviously wrong, because V12 really is about the TDI shark fin.**"*
>
> **The novelty claim was FALSE, and THIS REGISTER RECORDS THE OTHER TWO INSTANCES ITSELF** — which
> is what makes the error charged rather than excusable. It is **the third occurrence**, not the
> first. See the table immediately below.
>
> **⭐ THE CORRECTION STRENGTHENS THIS ENTRY, IT DOES NOT WEAKEN IT.** As originally written, §4 read
> as a **one-off curiosity**. Corrected, it is the **third and most severe instance of a documented,
> escalating hazard** — and a recurring hazard is a **far stronger** argument for §4's own conclusion
> (*"the defence is not vigilance — it is `Q-007`'s blanket rule and the exact-`diff` test, which do
> not care whether the text happens to be true"*) than a novel one was. A rule that must catch a
> repeating pattern is better justified than one guarding against a fluke.
>
> **The disposition is UNCHANGED.** All three V12 files stay quarantined, no V12 artifact draws on
> any of them, and that negative was re-tested at source during this fix.

**This is the THIRD lesson on which the generator's fabricated text happens to be on-topic, and the
register already recorded the first two:**

| # | Record | What it already said |
|---|---|---|
| **1st** | **`Q-003`** (V03), Finding 2 — *"the new hazard: this time some of the fabricated vocabulary is real"* | *"Unlike V02… **V03 genuinely discusses TDI (13 mentions), shark fin (3), railroad tracks (5), and stop hunts (8)**. The fabricated `NOTES.md` happens to name real V03 subjects"* — **and it quotes the SAME `NOTES.md` sentence** this section quotes below |
| **2nd** | **`Q-004`** (V04), Finding 3 — *"the `Q-003` hazard recurs and is worse here"* | *"The recording really does discuss **TDI (11), shark fin (5)**, stop hunts (4), railroad tracks (4)… A reader skimming `NOTES.md` and the transcript together would find the vocabulary corroborated everywhere"* |
| **3rd** | **`Q-013`** (V12), this section | **The most complete overlap of the three** — see the counts below |

**Word-boundary census, re-run at source by this session over the VERBATIM BODY of each transcript**
(not copied from the review):

| | `TDI` | `shark fin` | `volatility band` | `blood in the water` |
|---|---|---|---|---|
| **V03** | **12** | **3** | **2** | **2** |
| **V04** | **11** | **5** | 0 | **2** |
| V10 | 1 | 2 | 0 | 1 |
| V11 | 27 | 0 | 0 | 0 |
| **V12** | **46** | **21** | **5** | **14** |

> **⚠ Two cells differ by one from `V12_REVIEW_R1.md`'s table**, and the divergence is stated rather
> than absorbed: the review reports V12 `shark fin` = 20 and `volatility band` = 4; this session's
> exact-regex census returns **21** and **5**. **For `shark fin` the cause is located** — `[00:23:17]`
> carries **two** occurrences on one line (*"So now you have two setups what do you have shark fin
> short shark fin long?"*), which a per-line count scores once. **For `volatility band` the cause is
> NOT determinable** from the review file, which states its counts without its pattern; this session
> records its own figure and the method behind it (`\bvolatility\s+bands?\b`, case-insensitive, over
> the verbatim body) rather than reconciling to a number it cannot reproduce. **Nothing turns on
> either cell**: V12 exceeds V03 and V04 by four to seven times on every row under either count.
> **`Q-003`'s own *"TDI (13 mentions)"* likewise counts the whole file; the body figure is 12**, and
> both are recorded above for the same reason.

**And the three are ONE phenomenon, not three coincidences — verified mechanically this session:**

- **V03, V04 and V12 share the same ten-lesson `VISUAL_INDEX.md` body.** `diff` against V12 returns
  **exactly four differing lines for each — the title and three `Filename:` stems — and ZERO content
  lines.**
- **V03, V04 and V12 carry the byte-identical `NOTES.md` `TDI Indicator` sentence, at the same line
  18 of each file.** It is one of three variants across the 21 files; V01–V04, V09–V15 and V21 all
  carry V12's exact wording.

**So the two sentences this section identifies as on-topic were EQUALLY on-topic for V03 and V04 —
because they are literally the same two sentences.** What is true of V12 is not that the overlap is
new, but that it is **most complete**: V03 mentions the TDI 12 times in 71 minutes as one topic among
many, while **V12 is 55 minutes of nothing else**, titled `Traders Dynamic Index` on a card held for
eight and a half minutes.

**On eleven of the twelve audited lessons the fabricated files were wrong in an obvious way** — they
described Asian boxes and London stop hunts over lessons about equity curves, position sizing or the
RSI. **On V12, as on V03 and V04 before it, they are not obviously wrong, because V12 really is about
the TDI shark fin — and V12 is the lesson where that accidental overlap is most complete.**

- `NOTES.md` §3 says *"TDI Indicator: **Green Price Line** crossing **Red Signal Line** after
  breaking outside **Blue Volatility Bands** (**Shark Fin**)"*. **Every one of those four objects
  is real, correctly coloured, and correctly related** — the lesson's own printed deck is
  `Step 1: RSI Price Line` (green) → `Step 2: Trade Signal Line` (red) → `Step 3: Market Base Line`
  (yellow) → `Step 4: Volatility Bands` (blue), and `[00:20:07]` really does put the fin crossing
  the TSL at the entry.
- `VISUAL_INDEX.md` 003 says *"TDI Shark Fin setup with green line hooking inside volatility
  bands"*. **That is a fair description of this lesson's central claim.**

**Neither is evidence of anything, and both must still be refused**, for a reason that is
mechanical rather than a matter of judgement:

> **Those exact sentences are attached to TEN OTHER LESSONS, including lessons in which the token
> `TDI` occurs zero times** (`Q-009` measured `TDI` = 0 in V08's audio while a TDI panel sat on
> screen for 43 minutes). **A sentence that is printed identically on ten lessons cannot be an
> observation about any one of them.** It is right about V12 the way a stopped clock is right
> twice a day, and the clock did not start working.

**This is the most dangerous form the fabrication has taken so far**, and it is dangerous
*specifically to a reviewer working quickly*: a spot-check of V12's `NOTES.md` against V12's audio
would return *"broadly correct"* on the one line a spot-check is most likely to sample. The defence
is not vigilance — it is **`Q-007`'s blanket rule and the exact-`diff` test**, which do not care
whether the text happens to be true.

**No V12 artifact draws on any of these three files.** `V12_SOURCE_NOTES.md` was written from the
transcript alone, before they were opened, per `SWF_CAPTURE_RECIPE.md` §9.

---

### 5. Disposition

All three files remain quarantined **in place**, covered by the tree-wide
`README_WHY_QUARANTINED.md` banner. Nothing was moved, renamed or deleted.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered. **Shown by exact `diff` on THREE lessons — V10 (`Q-011`),
  V11 (`Q-012`), V12 (this entry) — to be a single document re-badged by six string
  substitutions.**
- **`NOTES.md`:** **12 of 21 audited** (V01–V12), **12 fabricated, zero exceptions.** V12 adds the
  measurement that the `EMAs` nickname line is a **constant across all 21 files**, wrong on four of
  five rows against `D-043`, and containing one nickname (`Raspberry`) with **zero occurrences
  anywhere in the corpus or in either external tier**.
- **`VISUAL_INDEX.md`:** **12 of 21 audited** (V01–V12), **12 fabricated.** V12 is the **fourth**
  confirmed instance of the sixth failure mode and the **second consecutive** one whose
  misdescribed frame is a **title card** — and the **THIRD** lesson on which the file's text is
  *about the right subject* (after `Q-003`/V03 and `Q-004`/V04), and the one on which that overlap
  is **most complete**, for the reason given in §4.
  ⚠️ **CORRECTED AT V12 R1 item 138 — ⚠ SELF-VERIFIED AT OWNER DIRECTION** (see §4). Retained per
  `REMEDIATION_PROTOCOL.md` §2, this clause originally read *"and the first lesson on which the
  file's text is about the right subject"*. **`first` was false; it is the third.**

---

## Q-014 — V13's three derived files, confirmed fabricated; `VISUAL_INDEX.md` differs from V12's by **four identifier lines and ZERO content lines**; and the fabricated `EMAs` table is now shown to be **period↔colour-CORRECT and nickname-SHIFTED-BY-ONE**

**Filed:** 2026-08-14, V13 student session, branch `video/v13`
**Files:** `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/13_Bootcamp1_Wk5_041512_Part1_65mins/{RULES.md, NOTES.md, VISUAL_INDEX.md}`
**Disposition:** **QUARANTINED IN PLACE.** Nothing moved, renamed or deleted. Covered by the
tree-wide `README_WHY_QUARANTINED.md` banner.
**Quarantined ON SIGHT, before being read for content**, per the standing directive.

---

### 1. The identifier tell, visible before any content check

The V13 files carry rule IDs **`V14-R001` / `V14-R002`** and image filenames
**`VIDEO_14_SCREENSHOT_00N_…`** — while sitting in the folder indexed **`13_`**, for the file
`SOURCE_MANIFEST.md` numbers **V13** under `D-017` §2. The generator's own numbering is
**internally inconsistent with its own folder index**, and it is the same off-by-one the V12
session recorded in its transcript header (*"Course Position: Video 13 of 21"* on the V12 file).

### 2. `VISUAL_INDEX.md` — measured, not asserted

`diff` against V12's file, which `Q-013` already proved to be one document shared by ten lessons:

```text
diff 12_…Wk4_040812_Part2/VISUAL_INDEX.md  13_…Wk5_041512_Part1/VISUAL_INDEX.md
  -> 8 differing lines = FOUR changed pairs, and all four are identifiers:
       the .swf filename, and the three VIDEO_13 -> VIDEO_14 screenshot names.
     ZERO content lines differ.
```

**⭐ THE FULL 21-LESSON CLUSTERING WAS RE-RUN AND `Q-013`'s FINDING EXTENDS.** Normalising away the
`.swf` filename, the `VIDEO_NN` identifiers and the `VNN-R` rule prefixes, then hashing:

| File | Distinct bodies across 21 lessons | Largest clusters |
|---|---|---|
| `VISUAL_INDEX.md` | **8** | **10 lessons** share one body — `03,04,09,10,11,12,13,14,15,21` — and **5 more** share a second — `16,17,18,19,20`. **15 of 21 lessons are covered by exactly TWO documents** |
| `NOTES.md` | **17** | **5 lessons** share one body — `16,17,18,19,20` |
| `RULES.md` | **17** | **5 lessons** share one body — `16,17,18,19,20` |

**The `16–20` cluster is new information and is recorded although those lessons are not yet
studied**: for five consecutive unstudied lessons, **all three derived files are literally
identical after identifier substitution.** A future session opening V16 does not need to re-derive
the fabrication finding; it needs only this row.

### 3. The images — indexed three, exist one, and the one is a **title card**

`VISUAL_INDEX.md` indexes three screenshots. **Only `VIDEO_14_SCREENSHOT_001_00-02-00.jpg`
exists**; `002` and `003` are indexed and **absent from disk**. That is a falsification requiring
no judgement.

The one image that does exist is a **colour-corrupted render of a title card** reading
`MARKET MAKER BOOT CAMP / Week 5`. It is indexed as:

> *"Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs… Setting up session boundaries
> and explaining accumulation mechanics."*

⭐ **This is `Q-012`'s V11 finding repeating VERBATIM — same failure, same caption, different
lesson.** `Q-012` recorded *"the one real image is the **TITLE CARD**, indexed as *'Asian Box
accumulation range with 5, 13, 50, 200, and 800 EMAs'*"*. **Third consecutive lesson whose
misdescribed frame is a title card.** It is now unreasonable to read these as independent errors.

> ⚠️ **A LEAD IS DECLINED HERE, DELIBERATELY.** The quarantined image appears to carry the printed
> words **`Week 5`**, which would be a printed confirmation of the week number — and this session's
> own 793 legitimate frames do **not** show that subtitle. **It is NOT adopted.** Evidence is not
> laundered out of a quarantined file, and nothing turns on it: the week number is independently
> established by `[00:17:52]` *"Please, **this is week five**"* and by the filename. Recorded so a
> reviewer can see the temptation was seen and refused.

### 4. `NOTES.md` — and the `EMAs` line, measured across all 21 files

V13's `NOTES.md` asserts *"**Topic Focus:** Stop Loss Buffers, Account Preservation, Position
Sizing"* and *"**Time Gap:** 30 to 90 minutes between peak 1 and peak 2 on M15 charts"*.

**This lesson is a pop quiz on weeks 1–4 plus a TDI chart review.** It contains **no** position-
sizing material, **no** account-preservation material, and the string `30 to 90` — and any minute
figure for a peak-to-peak gap — occurs **zero times** in its 1,183-entry transcript. The
`RULES.md` "verbatim instructor statements" attributed to `[00:05:00]` and `[00:18:00]` (*"Wait for
the M15 candle to close before taking the 5/13 EMA cross"*; *"Place your stop loss 10 to 15 pips
beyond the High or Low of the Day"*) **appear nowhere in the transcript at those or any
timestamps.** `10 to 15 pips` occurs zero times; the lesson's actual stop material is *below the
low* / *below the day* and a **drill** placeholder of `25 or 30`.

#### 4a. THE `EMAs` TABLE — `Q-013` ALREADY MEASURED THIS. ONE AXIS IS ADDED.

> ⚠️ **CORRECTION MADE BEFORE THIS ENTRY WAS COMMITTED, AND LEFT VISIBLE.** This section was first
> drafted as *"a new and sharper measurement than `Q-013`'s"*. **It is not.** `Q-013` already
> records: the 16/5 split, the colour-carrying variant, that the variant belongs to lessons 16–20,
> the four-of-five wrongness against `D-043`, the shift-by-one shape, the missing `Ketchup`, and
> the invented `Raspberry`. `D-042`'s *"by-product"* section records the shift-by-one analysis
> **again**, and notes it got **cleaner** under the `D-043` inversion. **The draft would have
> re-reported three prior findings as this session's.** It was caught by checking the claim against
> the register instead of against memory. Recorded per `REMEDIATION_PROTOCOL.md` §2, because a
> student session over-claiming novelty is exactly what an independent reviewer is looking for.

**What this session actually adds is ONE axis, and only because `Q-013` quoted the colour-carrying
variant without decomposing it.** The five lessons 16–20 carry:

```text
EMAs: 5 (Mustard/Yellow), 13 (Red/Water), 50 (Light Blue/Mayo),
      200 (White/Blueberry), 800 (Dark Blue/Raspberry).
```

Splitting that into its two mappings and testing each separately against `D-043`
(mustard=5=yellow · ketchup=13=red · water=50=aqua · mayonnaise=200=white · blueberry=800=blue):

| Axis | Verdict | Previously recorded? |
|---|---|---|
| **nickname ↔ period** | ❌ **WRONG ON FOUR OF FIVE**, shifted one rung too fast, `Ketchup` dropped, `Raspberry` invented | ✅ `Q-013`; `D-042` by-product |
| **period ↔ colour** | ✅ ⭐ **CORRECT ON ALL FIVE ROWS** — 5=yellow, 13=red, 50=light blue, 200=white, 800=dark blue, exactly `D-043` §2 | ❌ **not previously decomposed** |

> **Why the one new axis is worth recording rather than dropping.** `D-041` → `D-042` → `D-043`
> cost the project three decision records and two owner rulings, and `D-043` **reversed** `D-041`
> on the nickname↔period axis while **leaving the nickname↔colour pairing untouched** — that
> invariance is `D-043`'s own headline. **These files get the axis `D-043` reversed WRONG and the
> axis `D-043` did not touch RIGHT.** A session that had reached for them as corroboration at any
> point in that chain would have been pushed toward the reading the owner ultimately rejected,
> **while finding the colour column reassuringly correct.** That is a sharper description of the
> hazard than "four of five rows are wrong", and it is the reason `D-039`/`D-040` exclude this
> material as a source rather than merely discounting it.

**A phrasing correction carried over from the same draft:** it is **not** accurate to say
`Raspberry` *"occurs zero times in the corpus"*. The string appears in `V07_TRANSCRIPT.md`,
`V07_SOURCE_NOTES.md`, `DECISIONS.md`, `COURSE_PROGRESS.md` and this register — **in every case as
a record of its absence**, never as course speech. The accurate claim, which is `Q-013`'s and
`D-042`'s: **`raspberry` occurs 0× in genuine course audio anywhere in V01–V13, 0× in `MMM-NOTES`,
and 0× in every `EXTERNAL_VOCABULARY_REFERENCE.md` tier.** Re-verified this session across V01–V13.

### 5. Independence of the V13 artifacts

`V13_TRANSCRIPT.md`'s header block is copied **only** as the verbatim body; the pre-ingestion
`# VIDEO` header — including its *"Primary Topics: Risk Management Fundamentals, Stop Loss
Placement & Position Sizing"* — is **not carried over**, and the transcript's SOURCE table says so.

`V13_SOURCE_NOTES.md` was written from the transcript alone. **These three files were opened only
to quarantine them**, and no V13 artifact draws on any of them. `V13_SOURCE_NOTES.md` §10 records
that the corpus's own `mayonnaise` evidence was checked **against `D-043` and returned a negative
result**, without reference to the table in §4a.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered. Shown by exact `diff` on **four** lessons — V10 (`Q-011`),
  V11 (`Q-012`), V12 (`Q-013`), V13 (this entry) — to be one document re-badged by string
  substitution. **Newly measured: lessons 16–20 share a single `RULES.md` body verbatim.**
- **`NOTES.md`:** **13 of 21 audited** (V01–V13), **13 fabricated, zero exceptions.** V13 adds only the
  period↔colour decomposition in §4a — the rest of that table was `Q-013`'s. **Newly measured:
  lessons 16–20 share a single `NOTES.md` body verbatim, not merely a shared `EMAs` line.**
- **`VISUAL_INDEX.md`:** **13 of 21 audited** (V01–V13), **13 fabricated.** V13 is the **third
  consecutive** lesson whose one surviving image is a **title card** described as a chart, and the
  clustering now shows **15 of 21 lessons covered by exactly two documents**.

---

## Q-015 — Lesson 14 (`Bootcamp1 Wk5 041512 Part2`): `NOTES.md`, `RULES.md`, `VISUAL_INDEX.md`

**Filed:** 2026-08-14 by the V14 student session
**Location:** `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/14_Bootcamp1_Wk5_041512_Part2_48mins/`
**Status:** **QUARANTINED ON SIGHT.** No V14 artifact cites any of these three files as evidence.
Every reference in the V14 set is to **this register entry**, never to the files.

**This is the FOURTH CONSECUTIVE lesson carrying the `VISUAL_INDEX.md` pattern** — `Q-012` (V11),
`Q-013` (V12), `Q-014` (V13), and now V14.

---

### 1. `VISUAL_INDEX.md` — a byte-level clone of V13's, with ZERO content lines changed

`diff` against lesson 13's file, re-run this session:

```text
diff 13_…Wk5_041512_Part1/VISUAL_INDEX.md  14_…Wk5_041512_Part2/VISUAL_INDEX.md
  -> 8 differing lines = FOUR changed pairs:
       the .swf filename, and three VIDEO_14 -> VIDEO_15 screenshot names.
     ZERO content lines differ.
```

**Identical to the V12→V13 result `Q-014` §2 measured.** The three "What is visible" strings, the
three "Instructor's Explanation" strings and the three "Trading Significance" strings are **the same
sentences**, describing a **48-minute lesson on the price board** with text written for a lesson
about EMAs, M-formations and TDI shark fins.

### 2. ⭐ THE SURVIVING IMAGE IS A BLANK POWERPOINT EXIT SCREEN DESCRIBED AS A FIVE-EMA CHART

`VISUAL_INDEX.md` indexes **three** screenshots. **Only `VIDEO_15_SCREENSHOT_001_00-02-00.jpg`
exists on disk** — `002` and `003` are absent, confirmed this session.

**`001` was opened and measured.** It is `1024 × 768`, and:

```text
mean luminance          1.0   (of 255)
fraction of pixels > 60   0.0032
light pixels confined to  rows 11-20 and rows 11 / 752 (the window border)
```

**It is 99.7% pure black.** The only content is one line of small light text at rows 11–20,
which at 10× autocontrast reads:

```text
End of slide show, click to exit.
```

**It is PowerPoint's end-of-slideshow screen.**

`VISUAL_INDEX.md` describes it as:

> - Visual Type: **Chart / Slide Overview**
> - What is visible: **Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs.**
> - Instructor's Explanation: *Setting up session boundaries and explaining accumulation mechanics.*
> - Trading Significance: *Defines initial liquidity boundaries for session manipulation.*

⭐ **A blank black screen is indexed as a chart carrying five named moving averages.** This is the
strongest single demonstration of fabrication in this register: the three preceding entries found
**title cards** described as charts, and a title card at least carries pixels. **This one carries
none.**

**And the timestamp is wrong too.** The file claims `[00:02:00]`. At `[00:02:00]` this lesson is
showing the `CANDLES` formation list (`V14_00-01-15_…png` through `V14_00-02-40_…png`); the actual
end-of-slideshow state occurs at the **end** of the file. The image is real — it came off some
machine — but **nothing about how it is labelled is true.**

### 3. `NOTES.md` and `RULES.md` — near-clones, and this lesson REPUDIATES their central rule

`diff` against lesson 13's files, re-run this session:

| File | Differing lines | What actually differs |
|---|---|---|
| `NOTES.md` | **6** | the `.swf` filename, `Part 1`→`Part 2`, and **one invented `Topic Focus` line** |
| `RULES.md` | **12** | the `.swf` filename, `V14-R`→`V15-R` rule prefixes, three `VIDEO_14`→`VIDEO_15` visual references, `Part 1`→`Part 2` |

**The only substantive difference between V13's and V14's `NOTES.md` is a fabricated topic line:**

| Lesson | Invented `Topic Focus` |
|---|---|
| 13 | *"Stop Loss Buffers, Account Preservation, Position Sizing"* |
| 14 | *"GBPJPY / NAS100 Spread & Buffer Adjustments, Trailing Stops"* |

**Negative string checks against the 600-marker verbatim body, run this session:**

| String | Occurrences in V14 |
|---|---|
| `GBPJPY` / `GBP/JPY` | **0** |
| `NAS100` | **0** — the only `nas` substring in the file is *"some **nas**ty emails"* `[00:04:09]` |
| `trailing` | **0** |
| `Asian Box` | **0** — the speaker says *"Asian range"* and *"blue box"* |
| `800` | **0** |
| `Mustard` / `Mayo` / `Blueberry` / `Raspberry` | **0 each** |
| `Water` | **1**, and it is *"blood in the **water**"* `[00:44:59]` — **the TDI's red signal line, not a moving average** |
| `30 to 90` | **0** |
| `10 to 15` | **0** |
| `Peak Formation` / `PFH` / `PFL` | **0 each** |
| `5/13` | **0** |
| `RRR` | **0** — from the `TRANSCRIPT.md` header's *"Risk-to-Reward Optimization (1:3 to 1:5 RRR)"* |

⭐ **`NAS100` is an anachronism as well as a fabrication.** It is a CFD index ticker, in a 2012
retail-forex bootcamp whose entire content is the GBP/USD price board.

### 4. ⭐ THE FABRICATED RULE IS THE OPPOSITE OF WHAT THE LESSON TEACHES

`RULES.md` `V15-R001`, presented as a **verbatim** instructor quotation:

> **Instructor Statement:** *'Wait for the M15 candle to close before taking the 5/13 EMA cross.'*
> **Timestamp:** `[00:05:00]`
> **Notes:** *"Preserved verbatim rule from instructor."*

**The actual `[00:05:04]` line is:** *"Okay, so this is a picture what I just discussed."*

**And the rule is contradicted by the lesson's entire assignment.** V14's week's work is:

> `[00:26:55]` *"Look at the high low board. **Do not look at candles, do not look at TDI, do not
> look at nothing but this board.** So help me God."*
> `[00:31:40]` *"**No Gordon, there's no 15 minute period, there's no periods here.** You're not
> looking at candles… **there's no 15 minute, there's no one hour, that's all bullshit, throw it
> out.**"*
> `[00:46:28]` *"**No charts, Dave. No charts.**"*

**A fabricated rule instructing the student to trade a 5/13 EMA cross on a closed M15 candle has
been attached to the one lesson in the corpus that forbids looking at candles, EMAs, the 15-minute
timeframe and charts altogether.**

`V15-R002` — *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day"* at
`[00:18:00]` — is fabricated on the same pattern. **The lesson's actual stop rule is `5` pips**,
stated four times and **printed on the assignment slide**; `10 to 15` occurs **0** times.

### 5. The `TRANSCRIPT.md` header block is fabricated; the BODY is not

The pre-ingestion `TRANSCRIPT.md` carries a `# VIDEO` header claiming
*"Primary Topics: **Risk-to-Reward Optimization (1:3 to 1:5 RRR) & Capital Protection Rules**"*.
The lesson contains **no risk-to-reward material of any kind**; `RRR` and `1:3` occur **0** times.

**The verbatim body is a different matter and passed verification** — 600 monotonic markers, a
3.0 s tail against measured audio, and it preserves its own mishearings. `V14_TRANSCRIPT.md`
copies **only the body** and says so in its SOURCE table. **The header is not carried over**, and
its *"Course Position: Video 15 of 21"* is wrong under `D-017` §2 in any case.

### 6. Independence of the V14 artifacts

**These three files were opened only to quarantine them.** No V14 artifact draws on any of them.
`V14_SOURCE_NOTES.md` and `V14_INTERPRETATION.md` were written from the verified transcript and the
session's own frames; every EMA statement in the V14 set rests on
`V14_00-13-05_emas-yellow-red-cyan-white-low-test-candle.png`, **which this session opened and read
itself**, and on `D-043` — **not** on `NOTES.md`'s EMA table, which this entry shows to be
unsourced and, on the `Water = 13` row, **wrong under `D-043`** (Water is the **50**).

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered. Shown by exact `diff` on **five** lessons — V10 (`Q-011`),
  V11 (`Q-012`), V12 (`Q-013`), V13 (`Q-014`), V14 (this entry) — to be one document re-badged by
  string substitution.
- **`NOTES.md`:** **14 of 21 audited** (V01–V14), **14 fabricated, zero exceptions.**
- **`VISUAL_INDEX.md`:** **14 of 21 audited** (V01–V14), **14 fabricated.** ⭐ **V14 is the FOURTH
  CONSECUTIVE lesson whose one surviving image is a non-chart described as a chart** — and the
  first where the image is **blank**. V11, V12 and V13 were title cards; V14 is PowerPoint's
  *"End of slide show, click to exit."* screen described as *"Asian Box accumulation range with
  5, 13, 50, 200, and 800 EMAs."*

---

## Q-016 — Lesson 15 (`Bootcamp1 Wk7 050612 Part1`): `NOTES.md`, `RULES.md`, `VISUAL_INDEX.md`

**Filed:** 2026-08-14 by the V15 student session
**Location:** `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/15_Bootcamp1_Wk7_050612_Part1_52mins/`
**Status:** **QUARANTINED ON SIGHT.** No V15 artifact cites any of these three files as evidence.
Every reference in the V15 set is to **this register entry**, never to the files.

**SHA-256, recorded so the audited objects are pinned:**

| File | Bytes | SHA-256 |
|---|---|---|
| `RULES.md` | 3,036 | `3474afcd3c2c707053f4e426b13ec72120177377427fd17570be631d2eacf11f` |
| `NOTES.md` | 1,297 | `a5dc9a38aa6949a8997448ee8d28db050ba15fb05741f21e7b5bf7b75a5002bb` |
| `VISUAL_INDEX.md` | 1,255 | `4998185adcb931218735bbc380f6d7ba1bb4c452f0008d03d47a809a034a3832` |

**This is the FIFTH CONSECUTIVE lesson carrying the `VISUAL_INDEX.md` pattern** — `Q-012` (V11),
`Q-013` (V12), `Q-014` (V13), `Q-015` (V14), and now V15.

---

### 1. `VISUAL_INDEX.md` — a byte-level clone of V14's, with ZERO content lines changed

`diff` against lesson 14's file, run this session:

```text
diff 14_…Wk5_041512_Part2/VISUAL_INDEX.md  15_…Wk7_050612_Part1/VISUAL_INDEX.md
  -> 8 differing lines = FOUR changed pairs:
       the .swf filename, and three VIDEO_15 -> VIDEO_16 screenshot names.
     ZERO content lines differ.
```

**Identical in kind to the V12→V13 and V13→V14 results `Q-014` §2 and `Q-015` §1 measured — and
this is now the third consecutive lesson at which the measurement returns exactly the same
number.** The three *"What is visible"* strings, the three *"Instructor's Explanation"* strings
and the three *"Trading Significance"* strings are **the same sentences**, describing a
**52-minute lesson whose entire second half is the ADR** with text about Asian boxes, London-open
stop hunts and 5/13 EMA crosses. **The word `ADR` does not appear in any of the three files.**

### 2. THE SURVIVING IMAGE IS THE TITLE CARD, DESCRIBED AS A FIVE-EMA CHART

`VISUAL_INDEX.md` indexes **three** screenshots. **Only `VIDEO_16_SCREENSHOT_001_00-02-00.jpg`
exists on disk** — `002` and `003` are absent, confirmed this session.

**`001` was opened and measured.** It is `1024 × 768`, `mean luminance 3.48 / 255`,
`fraction of pixels > 60 = 0.0262` — a heavily under-exposed capture. At autocontrast it reads,
unambiguously:

```text
Market Makers Boot Camp
Week 7
```

**It is the lesson's title card** — the same slide this session captured cleanly as
`04_SCREENSHOTS/V15/V15_00-00-15_title-slide-week-seven.png`.

`VISUAL_INDEX.md` describes it as:

> - Visual Type: **Chart / Slide Overview**
> - What is visible: **Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs.**
> - Instructor's Explanation: *Setting up session boundaries and explaining accumulation mechanics.*
> - Trading Significance: *Defines initial liquidity boundaries for session manipulation.*

**A title card carrying two lines of text is indexed as a chart carrying five named moving
averages.** This is `Q-012`/`Q-013`/`Q-014`'s exact failure — and note that it is **the same
sentence `Q-015` applied to a BLANK screen.** The description is a constant; the image behind it
is whatever happened to be captured.

**And the timestamp is wrong.** The file claims `[00:02:00]`. This session's sweep shows the title
card on the 5-second grid at **00:00:15 and 00:00:20**, replaced by `Welcome Back / TRADESTRONG`
by **00:00:25**, and at `00:02:00` the lesson is showing the
`Managing Your Expectations` list (`V15_00-01-10_…png`, which holds until `04:30`).
⭐ **The claimed time and the actual time are not merely different — the claimed time is the one
this register has now recorded FIVE times in a row**, `[00:02:00]`, on five different lessons
with five different openings.

### 3. `RULES.md` — the same two rules, re-badged, and NEITHER IS IN THE LESSON

`diff` against lesson 14's file: **24 differing lines**, and every one is a string substitution —
the `.swf` filename, `V15-R`→`V16-R` rule prefixes, three `VIDEO_15`→`VIDEO_16` visual references,
and `(Week 5 - Part 2)`→`(Week 7 - Part 1)` in the setup name.

**The two "Instructor Statements" are presented in quotation marks. Neither is spoken in this
lesson, and the search is exhaustive over 492 markers:**

| Claimed at | Claimed quotation | Occurrences in `V15_TRANSCRIPT.md` |
|---|---|---|
| `[00:05:00]` | *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | **0.** `M15` occurs 0 times; `5/13` occurs 0 times |
| `[00:18:00]` | *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* | **0.** `10 to 15` occurs 0 times |

At the claimed `[00:05:00]` the lesson is announcing the New Jersey live class; at `[00:18:00]`
it is on the *"symbiotic / synergy"* aside before the weekly breakdown. **Neither timestamp
contains anything resembling either sentence.**

⚠ **The second one is the dangerous one.** *"Place your stop loss 10 to 15 pips beyond the High
or Low of the Day"* is a **fabricated stop-loss rule in quotation marks**, in a lesson that says
only *"That is why you use a stop loss. Okay. A tight stop loss"* (`[00:42:15]`) with **no
number attached**. It is precisely the `A-082` class, manufactured.

### 4. `NOTES.md` — a near-clone whose ONE substantive difference is an invented topic line

`diff` against lesson 14's file: **10 differing lines** — the `.swf` filename, `Week 5 - Part 2`→
`Week 7 - Part 1`, and **one invented `Topic Focus`**:

| Lesson | Invented `Topic Focus` | What the lesson is actually about |
|---|---|---|
| V14 (`Q-015`) | *"GBPJPY / NAS100 Spread & Buffer Adjustments, Trailing Stops"* | candles and the high/low board |
| **V15 (this entry)** | *"Mid-Week Resets, Consolidation Traps, Level Re-counts"* | **the ADR, replotted as horizontal levels, as one leg of a New York-reversal confluence** |

**And the EMA table is wrong under `D-043` on FOUR of its five rows** — a clean shift-by-one down
the nickname list, with a fifth nickname invented:

| `NOTES.md` claims | `D-043` (authoritative) |
|---|---|
| `5 (Mustard)` | ✅ correct |
| `13 (Water)` | ❌ **13 is KETCHUP.** Water is the **50** |
| `50 (Mayo)` | ❌ **50 is WATER.** Mayo is the **200** |
| `200 (Blueberry)` | ❌ **200 is MAYO.** Blueberry is the **800** |
| `800 (Raspberry)` | ❌ **"Raspberry" is not a nickname in this course.** It appears in **no** transcript, **no** slide and **no** decision |

⚠ **`Q-015` §6 already recorded V14's copy of this same table as wrong on the `Water = 13` row.
It is the identical table, in a file that is otherwise a clone — so the error propagates
unchanged across lessons, which is what a clone does and what a note taken from a lesson could
not.**

### 5. The pre-ingestion `TRANSCRIPT.md` header — fabricated; the BODY is a different matter

The pre-ingestion `TRANSCRIPT.md` carries a `# VIDEO` header claiming
*"Primary Topics: **Trap Moves, Level 1/2/3 Progression & Fake Breakouts Identification**"*.
**The lesson contains no trap-move segment, no level-1/2/3 segment and no fake-breakout segment.**
`fake breakout` occurs **0** times. `trap` occurs **three** times and **none is a lesson segment**:
`[00:08:11]` *"stop triggers and **trap moves**"* — one clause inside the printed Week-7 take-away
list, i.e. a **back-reference to V14's material**, not a topic; `[00:31:27]` *"end back in the
range to **trap** the traders for tomorrow"*; `[00:40:45]` *"where the dealer sets his **traps**"*.
`level` never appears as `level 1` or `level one`; `level three` occurs three times and every one
is the instructor **refusing to count** (`[00:23:46]` *"Is this level three yet? **I don't know.**"*).
Its *"Course Position: Video 16 of 21"* is wrong under `D-017` §2 in any case — this file is **V15**.

**The verbatim body is a different matter and passed verification** — 492 monotonic markers, zero
equal-adjacent pairs, a 9.4 s tail against measured audio, and it preserves its own mishearings.
`V15_TRANSCRIPT.md` copies **only the body** and says so in its SOURCE table. **The header is not
carried over.**

### 6. Independence of the V15 artifacts

**These three files were opened only to quarantine them.** No V15 artifact draws on any of them.
`V15_SOURCE_NOTES.md` and `V15_INTERPRETATION.md` were written from the verified transcript and
this session's own 623-frame sweep; every EMA statement in the V15 set rests on
`V15_00-18-50_…png` and `V15_00-46-00_…png`, **which this session opened and read itself**, and on
`D-043`.

### Running tally for the fabrication pattern

- **`RULES.md`:** 21 of 21 covered. Shown by exact `diff` on **six** lessons — V10 (`Q-011`),
  V11 (`Q-012`), V12 (`Q-013`), V13 (`Q-014`), V14 (`Q-015`), V15 (this entry) — to be one
  document re-badged by string substitution.
- **`NOTES.md`:** **15 of 21 audited** (V01–V15), **15 fabricated, zero exceptions.**
- **`VISUAL_INDEX.md`:** **15 of 21 audited** (V01–V15), **15 fabricated.** ⭐ **V15 is the FIFTH
  CONSECUTIVE lesson whose one surviving image is a non-chart described as a chart.** V11, V12,
  V13 and V15 are **title cards**; V14 is a **blank** PowerPoint exit screen. **All five carry the
  same claimed timestamp, `[00:02:00]`, and the same claimed content, an Asian-box chart with
  five EMAs.** The description does not vary with the lesson because it was never derived from one.

---

## Q-017 — Lesson 16 (`Bootcamp1 Wk7 050612 Part2`): `NOTES.md`, `RULES.md`, `VISUAL_INDEX.md`

**Filed:** 2026-08-14 by the V16 student session
**Location:** `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/16_Bootcamp1_Wk7_050612_Part2_45mins/`
**Status:** **QUARANTINED ON SIGHT**, exactly as `COURSE_PROGRESS.md`'s V16 GATE (j) instructed.
No V16 artifact cites any of these three files as evidence. Every reference in the V16 set is to
**this register entry**, never to the files.

**SHA-256, recorded so the audited objects are pinned:**

| File | Bytes | SHA-256 |
|---|---|---|
| `RULES.md` | 3,173 | `cd549eea7ce01e23feb59a7fb8801bcc884184eec8ae0eea127423f56af66e26` |
| `NOTES.md` | 1,712 | `53d609ba5fb5db5f261d4a01c3ce127a511cd9656b790de90ba85073b4ab952a` |
| `VISUAL_INDEX.md` | 1,253 | `733abb55569b85311e92c0f4d9cdb5bbf6402d6357d0e2ce02bf5341abe0a0de` |

**This is the SIXTH CONSECUTIVE lesson carrying the `VISUAL_INDEX.md` pattern** — `Q-012` (V11),
`Q-013` (V12), `Q-014` (V13), `Q-015` (V14), `Q-016` (V15), and now V16.

---

### 0. ⭐ WHAT IS NEW HERE: THE CLONE IS NOW A PARAPHRASE

`Q-016` found V15's `VISUAL_INDEX.md` to be a **byte-level clone** of V14's with **zero content
lines changed**. **V16's is not a byte clone — it is a REWORDING of V15's with the same skeleton.**

> ⛔ **CORRECTED 2026-08-14 — `REVIEW_INDEX` item 225. THIS ENTRY PREVIOUSLY SAID *"every content
> line differs"*. THAT IS FALSE.** Nine content lines are **byte-identical**, and the correction
> makes the detector **cheaper**, not weaker — see the exact census below. The thesis (a paraphrase,
> not a clone) is unaffected and stands.

```text
diff 15_…Wk7_050612_Part1/VISUAL_INDEX.md  16_…Wk7_050612_Part2/VISUAL_INDEX.md
  -> 13 lines REWRITTEN, 9 content lines BYTE-IDENTICAL, and NOTHING
     STRUCTURAL differs.

  BYTE-IDENTICAL (9) -- these survive the rewrite unchanged and are therefore
  EXACT-MATCH DETECTABLE with a fixed-string grep:
       3 x header        "## Screenshot 001" / "002" / "003"
       3 x timestamp     "- Timestamp: [00:02:00]" / "[00:15:00]" / "[00:30:00]"
       3 x visual type   "- Visual Type: Chart / Slide Overview"
                         "- Visual Type: Annotated Chart Example"
                         "- Visual Type: Indicator / Strategy Diagram"

  REWRITTEN (13) -- paraphrased, so NOT exact-match detectable:
       1 x title line    (Part1 52mins -> Part2 45mins)
       3 x "- Filename:" (VIDEO_16_… -> VIDEO_17_…)
       9 x prose         "- What is visible:" / "- Instructor's Explanation:"
                         / "- Trading Significance:", three of each

  The three claimed SUBJECTS are preserved in MEANING but reworded, e.g.
     V15: "Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs."
     V16: "Initial setup slide / chart template with 5, 13, 50, 200, 800 EMAs
           and Asian Box boundaries."
```

⚠ **This matters for how the pattern should be detected from here on, and the correction sharpens
it.** A **whole-file `diff`** — which is what `Q-016` used and what GATE (j) implicitly assumed —
**would not have flagged this file**, because the file genuinely is not a byte clone: 13 of its
lines were rewritten. **But the invariant is only PARTLY non-byte-level, and the byte-level part is
the cheap part:**

| Invariant axis | Survives the rewrite? | Exact-match detectable? |
|---|---|---|
| The three **timestamps** | ✅ byte-identical | ✅ **yes** |
| The three **`Visual Type`** values | ✅ byte-identical | ✅ **yes** — ⭐ a FOURTH axis this entry did not previously name |
| The three **`## Screenshot NNN`** headers | ✅ byte-identical | ✅ yes, but generic — weak on its own |
| The three claimed **subjects** | ✅ in meaning | ⛔ **no** — reworded, needs a semantic check |

⭐ **So three of the four axes are a fixed-string grep, not a semantic comparison.** The detector for
`V17`–`V21` does **not** need to start with meaning-matching: **grep the timestamp triple and the
`Visual Type` triple first**, and fall back to subject comparison only for a file that changes
those too.

### ⭐⭐ THE CORRECTED DETECTOR WAS RUN, AND `V17`–`V21` ALL ALREADY MATCH — 2026-08-14

**Running the fixed-string check the moment it was written cost one `grep` and answered the
question the `DETECTION NOTE` was written to leave open.** Across
`_QUARANTINE_UNVERIFIED_NOTES/per_lesson/`:

- `Visual Type: Chart / Slide Overview` matches **15 lessons' `VISUAL_INDEX.md`** — `03`, `04`,
  `09`, `10`, `11`, `12`, `13`, `14`, **`15`, `16`**, and **`17`, `18`, `19`, `20`, `21`**;
- **every one of `17`–`21` carries all three of the `[00:02:00]` / `[00:15:00]` / `[00:30:00]`
  timestamps and exactly three `Visual Type` lines** — i.e. the full invariant, unchanged.

⛔ **The pattern does not stop at V16. It runs to the end of the material this project holds.**
`V17`–`V21`'s `VISUAL_INDEX.md` files are therefore **presumptively fabricated on the same
generator**, and each is to be **quarantined on sight** when its lesson is reached, exactly as GATE
(j) required for V16.

⚠ **This is a DETECTION result, not a verification result.** Matching the invariant is what makes a
file presumptively fabricated; **nobody has yet checked `V17`–`V21`'s three claimed frames against
their actual video**, which is the step that turned `Q-017` from a suspicion into §1's table. **That
work is still owed, one lesson at a time, and this note does not discharge it.**

---

### 1. `VISUAL_INDEX.md` — three screenshots that cannot exist

**All three claimed frames were checked against the 544-frame sweep this session captured
(`04_SCREENSHOTS/V16/INDEX.md` §0 — offset measured at zero, so the claimed timestamps map
directly onto sweep indices `24`, `180` and `360`).**

| Claimed | What is claimed | What is ACTUALLY on screen |
|---|---|---|
| `[00:02:00]` | *"chart template with 5, 13, 50, 200, 800 EMAs and Asian Box boundaries"* | ⛔ **The `Pivot Points` grid diagram** — a slide, not a chart. No EMA, no box, no candles. `V16_00-01-40_…png` and `V16_00-02-30_…png` bracket it |
| `[00:15:00]` | *"Stop Hunt move out of Asian Box during London Open session transition"* | ⛔ **A black slide reading `London Session Start / 2:00 To 3:00 AM, EST` with a red `SELL` and a green `BUY` capsule.** No chart at all. `V16_00-15-00_…png` |
| `[00:30:00]` | *"TDI … Shark Fin setup and 5/13 EMA cross confirmation"* | ⛔ **The `Pivots Are Intraday Support And Resistance / YOU Are The Filter!` bullet slide.** `V16_00-29-10_…png` |

⭐ **The `[00:15:00]` row is the sharpest instance the register has recorded.** The fabricated entry
claims a London-open stop hunt. **The real frame is a slide that says `London Session Start`** — so
the fabrication is adjacent to a real fact and lands on the wrong object. **A reader who trusted it
would have missed the corpus's first printed session boundary** (`A-105`) while believing they had
read about it.

---

### 2. `RULES.md` — two rules, neither in the file, and one census that settles it

Both claimed rules carry `Coding Readiness: Ready`.

| Rule | Claimed at | Claimed text | Reality |
|---|---|---|---|
| `V17-R001` | `[00:05:00]` | *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | ⛔ `[00:04:59]` is *"ahead and consolidate right around level 2 to make up some fake support and resistance."* **`5/13` occurs ZERO times in the transcript** |
| `V17-R002` | `[00:18:00]` | *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* | ⛔ `[00:18:01]` is *"are possible day highs. They are located above the central pivot point."* **`stop loss` occurs ZERO times in the transcript** |

**Token census over the committed 377-marker transcript (6,453 words), run this session and
reproduced as the absence half of `05_HOMEWORK/V16/` §6:**

```text
"stop loss"        0        "Asian box"       0        "shark"          0
"shark fin"        0        "railroad"        0        "peak formation" 0
"evening star"     0        "5/13"            0
```

⚠ **Eight for eight. Every load-bearing term in `RULES.md` and `NOTES.md` is absent from the lesson
they are attached to.** The `NUMERICAL PARAMETERS` table's seven rows — five EMA periods at
`[00:04:00]`, a `10-15 pip` stop buffer at `[00:18:00]`, a `30-90 min` peak gap at `[00:22:00]` —
are **all** marked `Explicit` and **none** is in the file.

**`RULES.md` also states `# CONTRADICTIONS: None detected within this video.`** V16 contains
`C-023`, a Tier-1-against-itself conflict on the pivot computation basis, stated **41 seconds
apart** in the same Q&A.

---

### 3. `NOTES.md` — a methodology summary wearing a lesson's filename

`NOTES.md` describes Asian-box accumulation, London/New York session times, `PFH`/`PFL` peak
formations, a *"30 to 90 minutes on M15"* peak gap, the five EMAs with nicknames, and TDI shark
fins. **V16 is forty-five minutes on floor-trader pivot points and the ADR grid.** The two
documents share **no subject**.

⚠ **Note the EMA nickname mapping it asserts** — *"5 (Mustard/Yellow), 13 (Red/Water), 50 (Light
Blue/Mayo), 200 (White/Blueberry), 800 (Dark Blue/Raspberry)"*. **`A-020` has been open for eleven
lessons precisely because the corpus never attaches a period to a nickname.** V16 says *"blueberry"*
twice (`[00:28:34]`, `[00:28:53]`) and attaches **no period**. **This file supplies the mapping
`A-020` wants, from nowhere, and it must not be used.**

---

### 4. WRONG ID, WHICH IS A CHEAP INDEPENDENT TELL

Every rule is numbered `V17-Rxxx` and every screenshot `VIDEO_17_…`. Under `D-017` §2's
re-derived ordering this file is **V16**. The `17` comes from the pre-ingestion folder numbering
that `SOURCE_MANIFEST.md` showed to be an alphabetical-sort artefact.

### Current Status

```text
Q-017 -- QUARANTINED. All three files. No V16 artifact cites them.
  DO NOT use RULES.md's parameters, NOTES.md's EMA nickname mapping, or any of
  VISUAL_INDEX.md's three timestamps for any purpose.
  DETECTION NOTE FOR V17-V21 [CORRECTED 2026-08-14, REVIEW_INDEX item 225]:
  the generator now PARAPHRASES rather than clones, so a WHOLE-FILE byte-diff
  will NOT flag it -- but 9 content lines are still BYTE-IDENTICAL and three of
  the four invariant axes are a plain fixed-string grep:
    1. the three timestamps  [00:02:00] [00:15:00] [00:30:00]   [byte-identical]
    2. the three Visual Type values: "Chart / Slide Overview",
       "Annotated Chart Example", "Indicator / Strategy Diagram"
                                                               [byte-identical]
    3. the three "## Screenshot NNN" headers        [byte-identical, generic]
    4. the three subjects                    [PARAPHRASED -- semantic check only]
  Check 1 and 2 FIRST; they are exact matches and cost nothing. Quarantine on
  any hit. Only fall through to 4 if a file has changed 1 and 2 as well.
```

---

## Q-018 — Lesson 17 (`Bootcamp1 Wk8 051312 Part1`): `NOTES.md`, `RULES.md`, `VISUAL_INDEX.md`

**Filed:** 2026-08-14 by the V17 student session
**Location:** `01_SOURCE_VIDEOS/Forex Bootcamp/_QUARANTINE_UNVERIFIED_NOTES/per_lesson/17_Bootcamp1_Wk8_051312_Part1_57mins/`
**Status:** **QUARANTINED ON SIGHT.** No V17 artifact cites any of these three files as evidence.
Every reference in the V17 set is to **this register entry**, never to the files.

**SHA-256, recorded so the audited objects are pinned:**

| File | Bytes | SHA-256 |
|---|---|---|
| `RULES.md` | 3,173 | `da6c56a665293c32f185f9788f86e1ff4f296c57fc6f77ef7da5dc63862c4701` |
| `NOTES.md` | 1,712 | `80c3db870302bc5be68df9bc79353cf895979559d65d945272e864e46d11ecee` |
| `VISUAL_INDEX.md` | 1,253 | `ebfe0c6d77fa4cc41aac6ec73c4c53bbe76b1f464422f3429299d5d6128c3b35` |

**This is the SEVENTH CONSECUTIVE lesson carrying the `VISUAL_INDEX.md` pattern** — `Q-012` (V11),
`Q-013` (V12), `Q-014` (V13), `Q-015` (V14), `Q-016` (V15), `Q-017` (V16), and now V17.

---

## 0. ⭐⭐ WHAT IS NEW HERE: THE PATTERN REVERTS TO A BYTE CLONE, AND `REVIEW_INDEX.md` ITEM 221'S PREDICTION IS **HALF RIGHT**

**Item 221**, raised by the V16 session, reads: *"`Q-017`'s detection note: the generator now
**paraphrases**, so a byte-`diff` will not flag V17–V21."*

**It was checkable and it has now been checked. The prediction is half right, and the half that is
wrong is the important half.**

`Q-017` found V16's trio to be a **rewording** of V15's — every content line differed, nothing
structural did. **V17's trio is NOT a further rewording. It is a BYTE CLONE of V16's**, and the
`diff` is as small as any in this register's history:

```text
diff 16_…Wk7_050612_Part2/VISUAL_INDEX.md  17_…Wk8_051312_Part1/VISUAL_INDEX.md
  -> 8 differing lines = FOUR changed pairs:
       the .swf filename, and three VIDEO_17 -> VIDEO_18 screenshot names.
     ZERO content lines differ.

diff 16_…/RULES.md  17_…/RULES.md
  -> 12 differing lines = SIX changed pairs:
       the .swf filename, V17-R001/R002 -> V18-R001/R002, and two visual filenames.
     ZERO content lines differ.  ZERO rule text, condition, trigger, threshold or
     numerical parameter differs.

diff 16_…/NOTES.md  17_…/NOTES.md
  -> 2 differing lines = ONE changed pair: the .swf filename.
     ZERO content lines differ.
```

⭐ **WHAT THIS MEANS FOR DETECTION, AND IT IS THE OPPOSITE OF WHAT ITEM 221 EXPECTED.** The generator
did not "move to paraphrasing". **It paraphrased ONCE, at V15→V16, and then propagated that
paraphrase verbatim.** A byte-`diff` against the immediately preceding lesson **would** have flagged
V17 in one command. Item 221's warning is still correct in its narrow form — *a `diff` against V15
would have missed V16* — but its forward-looking claim, that `diff` will not flag V17–V21, is
**FALSIFIED at the first opportunity**.

⚠ **The right detection rule is therefore neither "byte-diff" nor "paraphrase-aware".** It is the
**invariant**, which has now survived seven lessons and both mutation modes:

```text
THREE screenshots.  THREE timestamps: [00:02:00] [00:15:00] [00:30:00].
THREE subjects: 5/13/50/200/800 EMA template + Asian Box
                London-open stop hunt out of the Asian Box
                TDI shark-fin + 5/13 cross confirmation
TWO rules, at [00:05:00] and [00:18:00], each with a quoted "Instructor Statement".
```

**Open item 236 carries this forward.**

---

## 1. THE THREE CLAIMED SCREENSHOTS, AGAINST THE REAL FRAMES AT THOSE TIMECODES

**V17 is the first lesson in this register audited against a `§8a`-verified frame set with a
MEASURED ZERO offset**, so the comparison below is exact to ±5 s rather than approximate.

| Claimed | `VISUAL_INDEX.md` says | **What is actually on screen** |
|---|---|---|
| `[00:02:00]` | *"Initial setup slide / chart template with 5, 13, 50, 200, 800 EMAs and Asian Box boundaries."* | **The printed session-schedule slide** — `May 13th – Regular Session … July 1st 2 month break`. No chart. No EMA. No box. (`i = 24`) |
| `[00:15:00]` | *"Stop Hunt move out of Asian Box during London Open session transition."* | **The `Level 3 week after a correction / Confuse traders` chart**, annotated `HOW` / `LOW`. A week-in-review of GBP/USD. (`i = 180`) |
| `[00:30:00]` | *"TDI (Traders Dynamic Index) Shark Fin setup and 5/13 EMA cross confirmation."* | **The seven-point `Answer Key` slide under heavy hand annotation.** A TDI sub-window *is* present at the bottom of the embedded chart — see §1a. (`i = 360`) |

### §1a — ⚠⚠ THE THIRD CLAIM PARTLY LANDS, AND THAT IS THE MOST INSTRUCTIVE THING IN THIS ENTRY

`Q-016` recorded V15's surviving image as *"the title card, described as a five-EMA chart"*, i.e. a
clean miss. **Here, one of the three cloned claims brushes against something real**: the `00:30:00`
screen does contain a TDI panel, and V17 genuinely does discuss shark fins (`shark` returns **4**).

**This is coincidence, and it is exactly why claim-plausibility is not the test.** The claim was
written for a different lesson, copied unchanged into two more, and happened to intersect the third.
**`5/13` — the other half of the same sentence — returns ZERO in V17's 690-marker transcript.**

> **The rule this entry adds to the register: a cloned claim that happens to be true is still a
> fabricated claim.** The audit must be against **provenance**, never against plausibility.

---

## 2. THE TWO `RULES.md` "EXPLICIT INSTRUCTOR STATEMENTS", MACHINE-CHECKED

Both are presented as **`Source: Explicit`** with a timestamp and a quotation.

| | `V18-R001` | `V18-R002` |
|---|---|---|
| Claimed marker | `[00:05:00]` | `[00:18:00]` |
| Claimed quote | *"Wait for the M15 candle to close before taking the 5/13 EMA cross."* | *"Place your stop loss 10 to 15 pips beyond the High or Low of the Day."* |
| **What is at that marker** | `[00:05:03]` *"the recordings will be left up during the live event"* — **web-class logistics** | `[00:18:00]` *"One two three four one hour one two three four two hours…"* — **a student counting quarter-hour candles aloud** |

**Machine counts on the committed 690-marker transcript:**

```text
'5/13'        : 0
'M15'         : 0
'800'         : 0
'Asian Box'   : 0
'10 to 15'    : 0
'10-15'       : 0
'candle close': 0
'EMA'         : 4   (all "20 EMA" or moving-average glosses; none is 5, 13, 50 or 800)
```

⚠⚠ **`V18-R001`'s quoted sentence contains two terms that occur ZERO times in the lesson.** It is
not a paraphrase of anything said; it is text.

⚠⚠ **`V18-R002` is worse than absent — it CONTRADICTS the lesson.** V17 does state a stop-loss
distance, once, at `[00:53:42]`: *"**15 25's** \| Total above the high below the low"* — **15–25
pips**, not 10–15, and *"total"* is itself unresolved (`A-123`). **A fabricated file states a
confident number where the real lesson states a garbled one**, and the fabricated number is wrong.

**The `NUMERICAL PARAMETERS` table compounds it**, asserting `EMA Fast 5 / EMA Fast Confirm 13 /
EMA Baseline 50 / EMA Major 200 / EMA Macro 800`, all marked **`Explicit`** at `[00:04:00]` — where
the real lesson is reading out web-class dates — and a `Peak Time Gap 30-90 mins Between M/W Legs`
marked **`Explicit`** at `[00:22:00]`, where the real lesson is comparing the two pop-quiz entries.

⭐ **And the `CONTRADICTIONS` section reads `- None detected within this video.`** The V17 session
files **three** (`C-024`, `C-025`, `C-026`), two of them arithmetic errors made on air.

---

## 3. THE SURVIVING IMAGE

`VISUAL_INDEX.md` indexes **three** screenshots. **Only `VIDEO_18_SCREENSHOT_001_00-02-00.jpg`
exists on disk** — `002` and `003` are absent, confirmed this session.

**`001` was opened and measured:** `1024 × 768`, mean luminance `138.8`, 96% of pixels above 60 —
**not blank**, unlike `Q-015`'s.

**It is the deck's `MARKET MAKERS BOOT CAMP` diagonal title card**, described by `VISUAL_INDEX.md`
as *"chart template with 5, 13, 50, 200, 800 EMAs and Asian Box boundaries"*. **The same failure as
`Q-016` §2: a title card described as a five-EMA chart.**

⭐ **AND IT IS COLOUR-CORRUPTED, WHICH IS NEW.** The deck's title cards are orange and blue
throughout V17's 694 frames (`V17_00-02-40_…png`, `V17_00-03-55_…png`, `V17_00-30-10_…png`). **This
JPEG renders the same card in magenta, pink, cyan and violet** — a channel/palette failure in
whatever produced it. **Nothing in the three quarantined files mentions it**, and a note-writer who
had opened the image could not have missed it.

⚠ **It is also at the wrong timecode.** At the burned `02:00` the real screen is the **schedule
slide**; the title card is at `02:40`.

---

## 4. WHAT THIS ENTRY DOES **NOT** CLAIM

* It does not claim the files were produced maliciously, or by whom. **The register records what is
  in them and what is in the lesson.**
* It does not claim the underlying `TRANSCRIPT.md` in the same folder is defective. **The transcript
  is separately verified and passes** — `V17_TRANSCRIPT.md` VERIFICATION §§1–4. The three
  fabricated files sit beside a good transcript, which is what makes the folder dangerous rather
  than obviously worthless.
* It does not depend on the committed transcript being right. The `5/13`, `800`, `Asian Box` and
  `M15` zeroes are re-checkable against the independent ASR pass (`V17_TRANSCRIPT.md` §5), as
  `Q-017` §5 did for V16.
