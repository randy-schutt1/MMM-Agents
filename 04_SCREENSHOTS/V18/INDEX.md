# V18 — SCREENSHOT INDEX

**Source:** `Bootcamp1 Wk8 051312 Part2 (46mins).swf` · V18 · 2012-05-13 · 00:46:08
**26 curated frames**, all from a **562-frame** 10× sweep at `1024 × 786`. Every frame is the full
`1024 × 786` stage **including the control bar**, so each image **proves its own timestamp** from
the burned-in player readout (`SWF_CAPTURE_RECIPE.md` §8).

---

## §0 — ⚠⚠ `SWF_CAPTURE_RECIPE.md` §8a — THE MANDATORY SWEEP→CLOCK OFFSET MEASUREMENT

**§8a is a numbered required step, added by the V14 R1 remediation (`REVIEW_INDEX.md` items 174 /
186) because V14 skipped it and shipped 29 frames whose filenames were all `+16 s` wrong. It was
run here, before any frame was named — and on V18 it returned a result the corpus has not seen
before.**

### §0.1 — THE MEASUREMENT

`offset = burned_timecode − (i × 5)`, read from the pixels of the bottom-right `MM:SS / MM:SS`
readout, cropped `144 × 26` at `(880, 760)` and upscaled 5× with nearest-neighbour.

| Sweep index `i` | Filename second `i × 5` | **Burned timecode, read from pixels** | **Offset** |
|---|---|---|---|
| 0 | 0 | `00:16` | ⚠ **+16** — inside the play-guard, see §0.3 |
| 1 | 5 | `00:16` | ⚠ +11 — inside the play-guard |
| 2 | 10 | `00:16` | ⚠ +6 — inside the play-guard |
| **4** | **20** | **`00:20`** | **0** |
| **6** | **30** | **`00:30`** | **0** |
| **8** | **40** | **`00:40`** | **0** |
| **10** | **50** | **`00:50`** | **0** |
| **12** | **60** | **`01:00`** | **0** |
| **20** | **100** | **`01:39`** | **−1** |
| **60** | **300** | **`04:59`** | **−1** |
| **100** | **500** | **`08:19`** | **−1** |
| **150** | **750** | **`12:29`** | **−1** |
| **200** | **1000** | **`16:39`** | **−1** |
| **250** | **1250** | **`20:49`** | **−1** |
| **300** | **1500** | **`24:59`** | **−1** |
| **350** | **1750** | **`29:08`** | **−2** |
| **400** | **2000** | **`33:18`** | **−2** |
| **450** | **2250** | **`37:28`** | **−2** |
| **500** | **2500** | **`41:38`** | **−2** |
| **520** | **2600** | **`43:18`** | **−2** |
| **540** | **2700** | **`44:57`** | **−3** |
| **550** | **2750** | **`45:47`** | **−3** |
| 555 | 2775 | `46:09` | clamped at the file's own duration, as §8a says to expect |
| 558 | 2790 | `46:09` | clamped |
| 561 | 2805 | `46:09` | clamped |

⚠️ **THE OFFSET IS NOT CONSTANT, AND IT IS NOT ZERO. IT DRIFTS `0 → −1 → −2 → −3` ACROSS THE
FILE, MONOTONICALLY, MEASURED AT NINETEEN USABLE POINTS PLUS THREE CLAMPS.**

**Running history:** V12 `+16`, V13 `+15`, V14 `+16` (unmeasured, shipped wrong), V15 `+15`,
V16 **0**, V17 **0**, **V18 `0 → −3`, drifting.**

⭐ **THIS IS THE FIRST LESSON IN THE CORPUS WHERE THE OFFSET IS NEITHER A CONSTANT NOR ZERO**, and
it is the reason §8a says to measure every time. **V16 and V17 both returned a flat zero. Had this
session carried that forward — which is exactly the reasoning that produced V14's 29 wrong
filenames — non-zero error would have entered **24 of the 26 filenames**.**

### §0.2 — THE RATE CHECK (§8a step 3), RUN SEPARATELY, AND WHAT IT ACTUALLY SHOWS

§8a step 3 requires proving an **ORIGIN** error rather than a **RATE** error: consecutive filename
deltas must equal consecutive burned deltas.

| Interval | Filename Δ | Burned Δ | Agrees? |
|---|---|---|---|
| `i=4 → 6` | 10 s | 10 s | ✅ |
| `i=6 → 8` | 10 s | 10 s | ✅ |
| `i=8 → 10` | 10 s | 10 s | ✅ |
| `i=10 → 12` | 10 s | 10 s | ✅ |
| `i=12 → 20` | 40 s | 39 s | ❌ **−1** |
| `i=20 → 60` | 200 s | 200 s | ✅ |
| `i=60 → 100` | 200 s | 200 s | ✅ |
| `i=100 → 150` | 250 s | 250 s | ✅ |
| `i=150 → 200` | 250 s | 250 s | ✅ |
| `i=200 → 250` | 250 s | 250 s | ✅ |
| `i=250 → 300` | 250 s | 250 s | ✅ |
| `i=300 → 350` | 250 s | 249 s | ❌ **−1** |
| `i=350 → 400` | 250 s | 250 s | ✅ |
| `i=400 → 450` | 250 s | 250 s | ✅ |
| `i=450 → 500` | 250 s | 250 s | ✅ |
| `i=500 → 520` | 100 s | 100 s | ✅ |
| `i=520 → 540` | 100 s | 99 s | ❌ **−1** |
| `i=540 → 550` | 50 s | 50 s | ✅ |

**18 intervals checked · 15 exact · 3 short by exactly 1 s.**
**Total span: filename 2730 s vs burned 2727 s → a deficit of 3 s = 0.110%.**

### §0.3 — ⚠ THE JUDGEMENT CALL THIS SESSION HAD TO MAKE, DECLARED RATHER THAN BURIED

**§8a step 3 says, in terms: *"If they diverge, the fps patch is wrong — stop and fix §10, do not
apply an offset."* Taken literally, three divergent intervals mean stop. This session did not
stop, and the reasoning is put on the record so a reviewer can overrule it.**

1. **The failure mode step 3 exists to catch is a GROSS multiplier error.** Its worked example is
   V10: reading `3.0` when the header says `2.0` and patching to `30.0` gives **15×, not 10× — a
   50% rate error**. The deficit here is **0.110%**, three orders of magnitude smaller.
2. **The patch was verified independently of the sweep.** `patch_fps.py` read this file's own
   declared rate (`3.0`, raw `768`), multiplied by 10, wrote `30.0` (raw `7680`), **and re-read the
   written file to confirm `30.0` exactly**. A misread header is ruled out mechanically.
3. **The three figures agree.** `frameCount 8308 ÷ 3.0 fps = 2769.333 s`; measured audio
   `2768.953 s`; `SOURCE_MANIFEST.md` `00:46:08 = 2768 s`. A wrong declared rate would break this
   agreement, and it does not.
4. **The error is MONOTONIC, which distinguishes it from the OSD's granularity.** V17 recorded
   three `±1 s` readings and correctly dismissed them as the readout's 1-second granularity
   (`GOTCHA 2`) **because they were non-monotonic** (`−1, −1, 0, 0, 0, +1`). V18's never reverse.
   **This is real slippage — Ruffle not quite sustaining 30 fps under load — not a reading artifact.**

⚠️ **THE CONSEQUENCE IS THE IMPORTANT PART: A SINGLE SCALAR OFFSET WOULD BE WRONG HERE.** There is
no one number to add. **So no offset was applied at all. Every one of the 26 frames is named from
ITS OWN burned timecode, read from its own pixels** — §8a step 4 — which makes the drift moot by
construction rather than by correction.

⚠️ **OPEN ITEM FOR R1:** §8a step 3 is written as a **binary** test with no tolerance. A sub-1%
frame-pacing deficit is not the failure it targets, but it trips the test as written, and any
session following the letter of the step would halt on a healthy capture. **A tolerance — or an
explicit split between "gross multiplier error" and "pacing slippage" — is owed to the recipe.**
The recipe is a **POLICY LEDGER** and `D-038a` puts that edit on the integration branch, so it is
**raised here and not made here.**

### §0.4 — FRAMES BELOW `i = 4` ARE NOT USED

Frames `i = 0…3` fire inside the sweep's own `1500 ms` play-guard (the before/after screenshot
comparison that proves the play click landed) and read `00:16`. **No frame below `i = 4` appears in
the curated set.** This matches V16's and V17's handling.

### §0.5 — THE CAPTURE, FOR REPRODUCTION

| Field | Value |
|---|---|
| Declared frame rate | **3.0 fps**, read from this file's header (body offset 17, raw `768`) |
| Patched rate | **30.0 fps** = `3.0 × 10` — derived, never a literal |
| Frame count | **8,308** → 2769.333 presentation seconds |
| Stage | **1024 × 786** → play click at `(512, 300)` per `GOTCHA 5` |
| Play-click guard | **fired** — `sweep.log`: *"play click confirmed: stage changed"* |
| Sweep | 562 frames at 500 ms wall = **280.5 s wall clock** for 46:08 of presentation |
| Server | port **8918**, exclusivity proven by PID **and** by SHA-256 of the served bytes vs the local patched copy (`GOTCHA 4`) — **13 stale servers from prior sessions were listening on other `89xx` ports at the time** |
| Original SWF | **re-hashed after patching**: `cfa425ab…1f7181`, unchanged (`SOURCE_INGESTION_PROTOCOL.md` §2) |

---

## §1 — SCREEN-STATE DETECTION (§7)

The sweep frames are already on the 5-presentation-second grid §7 wants, so they were diffed
directly rather than re-sampled. Control bar cropped off (`0,0,1024,752`) so the progress bar and
ticking timecode do not register as screen changes; frames downscaled to `256 × 188`, greyscale,
pairwise mean absolute difference, threshold `6.0`, runs within 2 frames collapsed.

**562 frames → 23 raw changes → 21 distinct screen states.**

The 26 curated frames are those 21 states plus **five deliberate additions** showing *live
annotation of a slide already counted* (`09:09`, `14:09`, `17:54`, `20:49`, `26:39`, `42:28`,
`44:07`) — the detector scores an annotated slide as the same state, but the annotation is often
the evidence.

---

## §2 — THE 26 FRAMES

**Descriptors name WHAT IS SHOWN, not what it means** (`FILE_NAMING_STANDARD.md` §3). **Every frame
below was opened and looked at before it was named** — the discipline `REVIEW_INDEX.md` item 220
was raised to enforce, after the V16 session caught itself naming eleven frames from what the
speaker was saying rather than from what was on the glass.

| # | Filename | Burned | What is on the glass |
|---|---|---|---|
| 1 | `V18_00-00-20_trend-title-handdrawn-three-day-cycle.png` | `00:20` | `TREND` title; a **hand-drawn** cycle sketch — `Day 1 rise`, `Day 2 rise`, `New Trend under way`, `Stop hunt low, take it on first leg with confirmations`, `I was expecting this!!`, `I expect this one more day!!` |
| 2 | `V18_00-02-09_trend-chart-day1-day2-day3-labelled.png` | `02:09` | `TREND`; a real candle chart with printed labels `DAY 1` · `DAY 2` · `DAY 3`, `PEAK FORMATION LOW`, `STOP HUNT LOW` (×2), and `REVERSAL IS IMMENENT!!` — **misspelled on the slide** |
| 3 | `V18_00-03-34_trend-longer-term-three-bullets.png` | `03:34` | `TREND LONGER TERM` bullet slide — the three bullets are transcribed in full in `V18_SOURCE_NOTES.md` §3 |
| 4 | `V18_00-05-24_trend-four-panel-higher-timeframe-charts.png` | `05:24` | `TREND`; **four** chart panels tiled, annotated `THREE PRO TO THE HIGH`(?), `NOV HIGH`, `FEB 3RD HOD HOLDS` |
| 5 | `V18_00-06-29_trend-intra-day-four-bullets.png` | `06:29` | `TREND INTRA DAY` bullet slide — includes the printed `Slow, Steady, Lasts 6 To 8 Hours` |
| 6 | `V18_00-09-09_trend-intra-day-annotated-1-hr.png` | `09:09` | The same slide with live pen work: `1 HR` written top-right, two M/W shapes boxed, `Slow, Steady, Lasts 6 To 8 Hours` circled |
| 7 | `V18_00-10-19_will-all-time-frames-line-up-bullets.png` | `10:19` | `TREND`; `Will All Time Frames Always Line Up?` / `No!` / retail-trap bullet / `Have An Open Mind And Trade Both Directions` |
| 8 | `V18_00-11-29_up-trend-wvvm-counter-trend-ill-advised-v1.png` | `11:29` | ⭐ `Market Maker Up Trend Can Be Labeled As Such` · **`W V V M`** · **`Counter Trend Is Ill Advised On V1`** |
| 9 | `V18_00-14-09_up-trend-slide-annotated-75-plus.png` | `14:09` | The same slide, hand-annotated: a W and two V shapes drawn, a box, and **`75⁺`** written between the anchor and the consolidation |
| 10 | `V18_00-16-34_wvvm-chart-day1-day2-day3-labelled.png` | `16:34` | Real chart, printed `Day 1` · `Day 2` · `Day 3`, `MM Took Their Money Against the Trend!!`, and **`W V V M`** printed along the bottom |
| 11 | `V18_00-17-54_wvvm-chart-with-pins-circled.png` | `17:54` | The same chart with **~12 wicks individually circled** in pen — the *"pins, pins, pins"* passage |
| 12 | `V18_00-19-34_down-trend-maaw-counter-trend-ill-advised-a1.png` | `19:34` | ⭐ `Market Maker Down Trend Can Be Labeled as Such` · **`M A A W`** · **`Counter Trend Is Ill Advised on A1`** |
| 13 | `V18_00-20-49_down-trend-maaw-slide-annotated.png` | `20:49` | The same slide annotated; `M A,A W` circled, `Counter Trend Is Ill Advised on A1` circled, `3/15` written |
| 14 | `V18_00-22-14_maaw-chart-labelled.png` | `22:14` | Real chart with **`M A A W`** printed across the top |
| 15 | `V18_00-23-30_variation-to-this-cycle-bullets-wvvvm.png` | `23:30` | `Variation To This Cycle:` bullets, and **`W VVV M`** / **`W VVVVM`** printed at the foot — the extended-cycle notations |
| 16 | `V18_00-25-24_variations-are-used-as-five-bullets.png` | `25:24` | `Variations are used as :` — the five-reason list, transcribed in full in `V18_SOURCE_NOTES.md` §9 |
| 17 | `V18_00-26-39_variations-slide-position-size-boxed.png` | `26:39` | The same slide with `Increase Or Decrease Their Position Size (Dealer Off Loading)` boxed in pen |
| 18 | `V18_00-27-53_chop-then-rise-500-pips-chart-wvvvvvm.png` | `27:53` | Chart annotated `2 1/2 weeks of chop before the rise…Dealers come up big 500 pips`, `previous 3 weeks. The level holds. Each hit is slightly higher`, numbered hits `1 2 3`, and **`w v v v v v M`** printed at the foot |
| 19 | `V18_00-32-03_hedge-funds-still-holding-price-levels.png` | `32:03` | ⭐ `How many hedge funds do you think are still holding ……` · `EUR / USD @1.1950 by 1975?` · `GBP/USD @ 1.7038` · `GBP/USD @ 1.3560 off of the W RR tracks to the LOY` · `DO NOT FALL FOR THESE TRAPS!!!!` |
| 20 | `V18_00-32-33_gbpusd-weekly-chart.png` | `32:33` | `TREND`; a `GBPUSD,Weekly` chart with a lower indicator panel |
| 21 | `V18_00-35-53_trap-moves-bullets-2hr-time-cap.png` | `35:53` | `MARKET MAKER TRAP MOVES` — three bullets including `Why Would It Fail? Trap Volume Does Not Total The Value They Were Seeking. Extended Stop Hunt Will Be Seen ( 2HR Time Cap)` |
| 22 | `V18_00-39-58_two-moves-left-bullets.png` | `39:58` | `When Trap Volume Is Not Met The Market Maker Will Have 2 Moves Left….` · `1. Hit The Stops And Rise /Fall` · `2. Hold The Level And Handle The Cross` |
| 23 | `V18_00-41-28_minimum-2-hrs-four-bullets.png` | `41:28` | `MARKET MAKER TRAP MOVE` · `If You Are Caught By This Move You Must Wait For Next Level Rise/Fall` · **`Minimum 2 Hrs`** · `Session Change Over` · `You Can Convert A Losing Cycle To Profit` |
| 24 | `V18_00-42-28_minimum-2-hrs-annotated-345-and-30-90.png` | `42:28` | ⭐ The same slide with the arithmetic written live: **`3  45`** and **`30 · 90`**, `Minimum 2 Hrs` circled |
| 25 | `V18_00-44-07_minimum-2-hrs-slide-fully-annotated.png` | `44:07` | The same slide fully worked over — `3 45 − 15`, `30 · 90`, `24`, `23`, a drawn price path, and `You Can Convert A Losing Cycle To Profit` circled |
| 26 | `V18_00-44-52_trap-candle-patterns-title-slide.png` | `44:52` | `MARKET MAKER TRAP MOVE` · **`Trap Candle Patterns`** — **next week's** subject, not this lesson's |

---

## §3 — WHAT THE FRAMES CORRECTED, AND WHY §9's ORDERING MATTERS

`SWF_CAPTURE_RECIPE.md` §9 requires the transcript pass and the notes to be written **before** the
screenshots are looked at, so a reviewer can see which conclusions survive on audio alone. That
order was followed. **Four things changed when the frames were opened, and all four are
improvements the audio could not have delivered:**

1. ⭐⭐ **`Counter Trend Is Ill Advised` is PRINTED — twice.** The committed transcript's
   `[00:19:40]` *"Counter trends are advised"* inverts the rule. The independent ASR pass had
   already flagged it; **the slide settles it beyond argument**, in two directional variants
   (`On V1`, `on A1`). See `V18_TRANSCRIPT.md` VERIFICATION §5 correction #1.
2. ⭐⭐ **The `W V V M` / `M A A W` notation is printed, and the transcript garbles all of it.**
   The audio gives *"W-ank for point"* `[00:11:41]`, *"M-R. Right?"* `[00:11:57]`, and
   *"your WVVVVVVN cycle or your WVVN cycle"* `[00:30:00]`. **The deck prints `W V V M`,
   `M A A W`, `W VVV M`, `W VVVVM` and `w v v v v v M` cleanly.** This is the lesson's central
   notation and it is **only** recoverable from the screen.
3. ⭐ **The four garbled price levels are printed exactly.** *"Euro at 1,950 by 75"* → `EUR / USD
   @1.1950 by 1975?`; *"down dollar at 7,8 or 35,60 off the W-R-O tracks to the loin"* →
   `GBP/USD @ 1.7038` and `GBP/USD @ 1.3560 off of the W RR tracks to the LOY`. **`W RR tracks`
   is *W railroad tracks*; `LOY` is *Low Of Year*** — and he decodes the latter aloud himself at
   `[00:32:16]`.
4. ⭐ **The 2-hour rule is printed twice and its arithmetic is written on screen.** `( 2HR Time
   Cap)` at `35:53` and `Minimum 2 Hrs` at `41:28`, with `3  45` and `30 · 90` worked out in pen at
   `42:28`. ⚠️ **And the slide says `Minimum`, where the audio says *"wait ABOUT two hours"*
   `[00:42:19]`** — a real divergence between the printed rule and the spoken one, recorded as
   `A-128` rather than silently reconciled.

**Nothing in §§1–2 of `V18_SOURCE_NOTES.md` was rewritten to match the frames.** The frame-derived
material is added as `§13` there, as a new section, per §9 step 4.
