# V05 — SCREENSHOT INDEX

30 curated frames from `Bootcamp1 Wk2 032512 Part3 (68mins).swf`, plus 5 two-times-scale
re-renders in `hires/` for the frames whose fine print is quoted.

> ## ⚠ EVERY FRAME IN THIS DIRECTORY IS `GUEST` MATERIAL — `D-025` APPLIES TO ALL OF IT
>
> V05 has **no instructor segment**. A single presenter — not Steve Mauro, and not V04's
> guest — speaks the whole 01:08:20 (`02_TRANSCRIPTS/V05/V05_TRANSCRIPT.md`
> § "ONE SPEAKER…"; re-verified this session, see below). Under `DECISIONS.md` **D-025**
> every slide below is **SECONDARY, DESCRIPTIVE evidence**:
>
> - Printed text may be cited for **what the slide says** — that a term exists, how it is
>   spelled, that an object is displayed.
> - Printed text may **NOT** enter `12_MASTER_SPEC/`, `13_MACHINE_SPEC/`,
>   `08_CONCEPT_LIBRARY/` or any machine candidate as **normative** material, may **not**
>   be cited for or against an instructor rule, and may **never close** an `A-xxx` or
>   `C-xxx` record. It may **extend** one.
> - Several slides here are squarely **normative** in content (day counts, holding
>   periods, an accuracy figure). Those are flagged inline as `NORMATIVE — EXCLUDED`.

---

## CAPTURE PROVENANCE

| Field | Value |
|---|---|
| Method | Ruffle WASM + Playwright 10× fast sweep (`SWF_CAPTURE_RECIPE.md` §10, `D-021`) |
| Sweep | 829 frames, one per 5 presentation-seconds, 1024×786, full frame incl. control bar |
| Source SHA-256 | `c606520de74d8b0f1d4800b026f252f9a89d4ecc66bb5db9ff3992dcf896fcc1` — matches `SOURCE_MANIFEST.md` |
| Working copy | `v05_x10.swf`, frame rate 3.0 → 30.0 fps |
| Frames captured by | The prior (stalled) session of 2026-08-11 00:22–00:29. **Not** this session. |
| Frames verified by | **This session, independently, before any frame was used.** See below. |

**The sweep was inherited, so it was verified rather than trusted** (`D-022`, GOTCHA 4 —
a port collision once cost this project a 61-minute capture of the wrong lesson):

1. **The working copy is the right film, proved at the byte level.** The original SWF body
   was zlib-decompressed and compared to the served `v05_x10.swf` body: identical length
   (44,111,472 bytes) and **exactly one differing byte, offset 18** — the `frameRate`
   `UI16` (`0x0300` → `0x001e`, i.e. 3.0 → 30.0 fps). `frameCount` is 12,304 in both. No
   other byte differs, so no other film could have been served.
2. **The server was that capture's own.** `lsof` on the still-live listener shows its
   `cwd` is the capture's `serve/` directory, which contains **one** `.swf`; the bytes it
   returns hash-match the file on disk.
3. **The timecode advances linearly at 10×.** The player's burned-in OSD was read at 14
   sample points: frame 1 → `00:05`, 12 → `01:00`, 60 → `05:00`, 120 → `09:59`,
   240 → `19:59`, 360 → `29:59`, 480 → `39:59`, 600 → `49:58`, 720 → `59:58`,
   800 → `66:38`, 820 → `68:18`, 824/828 → `68:21` (clamped at the end). Error is
   **0–2 s, non-accumulating** — consistent with the OSD's 1-second lazy granularity
   (GOTCHA 2) plus capture latency, not with frame loss.
4. **Content matches the transcript.** Frame 0 prints **"Research & Development"**, which
   is the subject the presenter states at `[00:00:00]`. The deck's platform-tutorial
   section matches the audio's platform talk. This is the early sanity check GOTCHA 4
   requires.
5. **A fourth independent duration derivation, new this session.** The OSD's total field
   reads **`68:2x`** on every frame, agreeing with the audio (4101.15 s), the SWF header
   (12,304 ÷ 3.0 = 4101.3 s) and `SOURCE_MANIFEST.md` (01:08:21).

### Filenames carry each frame's OWN burned-in timecode

The timestamp in every filename below was **read off that frame's OSD**, not computed from
its sweep index. Nominal sweep time (`index × 5 s`) runs 0–2 s ahead of the OSD, so the two
differ by a second in most rows; the filename follows the frame, because the frame is what
proves its own timestamp. Transcript markers cited in the descriptions are the transcript's,
and are ±2 s against the OSD for the same reason.

### ⚠ PROCESS DEVIATION, DISCLOSED

`SWF_CAPTURE_RECIPE.md` §9 requires source notes and interpretation to be written from the
transcript **before** the screenshots are examined, so a reviewer can see which conclusions
survive on audio alone. **That order was not preserved for V05.** The inherited sweep had to
be validated before it could be used, and validating it required reading frame content
against the transcript (step 4 above is mandatory, not optional). Having opened the frames,
this session read the whole deck.

Consequences, stated rather than hidden:

- The audio-only / visual-corroborated separation is **weaker for V05 than for V01–V04**.
  `V05_SOURCE_NOTES.md` §§1–9 are still written from transcript text and cite transcript
  markers only, but this session cannot claim it was blind to the slides while writing them.
- Where a slide is the **only** support for a claim, the notes say so explicitly and cite
  this index rather than a marker.
- No conclusion in any V05 artifact rests on a slide reading that the transcript
  contradicts; where the two differ, both are recorded.

---

## THE ZEN_MAN FINDING — PROVENANCE, NOT EVIDENCE

Frame `V05_00-38-19_slide-save-as-picture-zen-man-folder.png` shows an MT4 **Save As**
dialog whose navigation pane prints **`Zen_man` / `System Folder`** — a Windows user-profile
folder. Read at 3× magnification; unambiguous.

**This does not make the V05 presenter Zen**, and the audio settles it in the other
direction. The speaker refers to Zen in the **third person twice**, and both times places
himself *below* Zen in skill:

- `[00:01:41]`–`[00:01:52]` — *"When you see the stuff enough, like Zen and how he pulls
  the trade, when there's just a little pin bar, **even I can't get that**, but, you know,
  he said, I've seen it enough. I know this is going to work. And he takes the trade."*
- `[00:30:32]`–`[00:30:35]` — *"Like Zen would probably get in here. **I can't see that
  stuff.**"*

> The transcript's speaker section cites only the second of these. The `[00:01:41]` passage
> is **stronger** — *"even I can't get that"* cannot be said by Zen about Zen — and is
> recorded here as an addition to that section's evidence, not a correction of it.

The consistent reading is that the **deck reuses chart images captured on Zen's machine**
while a third person presents it. That is a fact about a printed artifact, which is exactly
what D-025 admits as descriptive.

**Under `D-025` consequence 4 nothing depends on this being right:** identifying a guest is
provenance, not evidence. V05 is guest material and wholly non-normative whether the
presenter is a third voice or Zen himself. The finding changes no grade and no citation.

## THE SESSION DATE IS ON SCREEN — NEW THIS SESSION

`V05_00-40-04_live-mt4-gbpusd-m15-ohlc-status-bar.png` shows the Windows taskbar clock
reading **`10:31 PM  3/25/2012`**.

The transcript header records the session date as 2012-03-25 **from the filename
`032512` alone**, and states — correctly — that *"no date is spoken inside V05."* It is not
spoken, but it **is displayed**. This is independent corroboration of the date from inside
the recording, and it is descriptive evidence of the plainest kind (what a printed artifact
says). It agrees with the filename exactly.

---

## LESSON STRUCTURE AS THE FRAMES SHOW IT

| Presentation time | What is on screen |
|---|---|
| `00:00`–`00:10` | Title slide, "Research & Development" |
| `00:10`–`04:35` | One static slide ("What is R & D…") held ~4.5 min while the presenter talks |
| `04:35`–`39:15` | PowerPoint deck: R&D rationale → MT4 platform how-to → Find the Anchor → MM-cycle worked examples → M/W patterns → TDI/Shark Fin → save images → flash cards |
| `39:15`–`48:10` | Live MT4 desktop, GBPUSD M15, marking up charts |
| `50:43`–`52:00` | Back to slides: "Evolution of a Trader", the `~SM~` quote, then the deck's end-of-show black frame |
| `52:50`–`68:21` | Live MT4 desktop again, more chart markup, ending on the player's replay button |

80 distinct screen states were detected across the 829 sweep frames (consecutive-frame
mean-difference > 6.0 over a 1024×760 crop that excludes the control bar, so the ticking
timecode and moving progress bar cannot themselves register as content change; runs
collapsed within 10 s). 30 are curated below. The rest are mostly incremental drawing steps
on a chart already represented here and can be re-extracted from the sweep in seconds.

### The `hires/` subfolder

Five frames are also kept at **2048×1572**, re-rendered by a second 10× pass with the Ruffle
stage at `scale=2`. They exist because specific fine print is **quoted** from them in this
file and in `V05_SOURCE_NOTES.md`, and a reader should be able to check the quotation
against the same pixels the reading was taken from:

`V05_00-06-20_customizing-toolbar-available-selected-lists_2x.png`,
`V05_00-10-30_find-the-anchor-slide_2x.png`, `V05_00-25-55_mm-full-cycle-a1-a2_2x.png`,
`V05_00-36-55_shark-fin-slide-gbpusd-m15_2x.png`,
`V05_00-38-20_save-as-dialog-desktop-folders_2x.png`.

> **A limit of the 2× pass, stated because it bounds what may be claimed.** Rendering at 2×
> upscales the stage; it does not add information the SWF does not carry. The deck's
> embedded chart screenshots are themselves ~1024 px wide, so **the chart-header symbol
> strings on most deck slides stay illegible at any magnification** and are not transcribed
> anywhere in this file. The one deck slide whose header *is* legible is frame 21
> (`GBPUSD,M15`), and it is legible because that slide's screenshot was captured at a larger
> scale than the others. Where a header could not be read, this index says so rather than
> inferring the pair from price magnitude.

---

## FRAMES

### The deck — R&D rationale

| # | File | Timecode | What is shown |
|---|---|---|---|
| 1 | `V05_00-00-01_title-slide-research-and-development.png` | `00:01` | Title slide, single line: **"Research & Development"**. Corroborates the presenter's `[00:00:00]` renaming of homework. |
| 2 | `V05_00-00-10_slide-what-is-rd-and-why-do-it.png` | `00:10` | **"What is R & D and Why do it…"** — 7 bullets. Printed: *"R & D is the new name for Homework………lol."*; *"ONLY You can do your own R&D. You cannot cheat…"*; *"R&D will give YOU the confidence you need to pull the trigger on the hard right edge."*; *"The most successful students have done TONS of R&D."* Held on screen ~4.5 minutes. |
| 3 | `V05_00-04-35_slide-what-would-be-considered-rd.png` | `04:35` | **"What would be considered R&D……."** — the lesson's own task list: know your platform; add Indicators, Scripts & Templates; work the Toolbar; use SCRIPTS and customize settings using Meta Editor; **mark up your charts**; **SAVE the mark ups**; **make FLASH CARDS and have the Setups in-grained in your head**. This slide is the source of V05's homework. |

### The deck — MT4 platform mechanics

Six frames of pure tool operation. Descriptive by nature: they show *how to operate MT4*,
not what constitutes a setup. No normative trading content.

| # | File | Timecode | What is shown |
|---|---|---|---|
| 4 | `V05_00-05-55_slide-know-your-toolbar.png` | `05:55` | **"Know your Toolbar… Tools you will use"** — MT4 toolbar screenshot, annotation *"Right CLICK anywhere on the Toolbar to see a list of choices"*. |
| 4a | `V05_00-06-20_customizing-toolbar-available-selected-lists.png` | `06:20` | MT4 **"Customizing toolbar"** dialog, both list boxes legible at 2× (`hires/`). **Available:** `Fibonacci Arcs`, `Fibonacci Expansion`, `Fibonacci Channel`, **`Rectangle`** (highlighted), `Triangle`, `Andrews' Pitchfork`, `Cycle Lines`, **`Text label`** (icon: a boxed **T**). **Selected:** `Crosshair`, `Vertical Line`, `Horizontal Line`, `Trendline`, `Ellipse`, **`Text`** (icon: a plain **A**), `Arrows`. Annotations *"Select"* → `Insert ->` and *"then Click"*. <br><br>**This frame settles `U1` / the text-tool question, and it does so descriptively.** The transcript at `[00:09:55]`–`[00:10:00]` is self-contradictory — *"There's one that says E and one that says T. Just use the one that says **A**. Don't use the one that says **T**."* The dialog shows MT4 carries exactly two text objects and that their **icons are literally the letters `A` and `T`**: `Text` (`A`) and `Text label` (`T`). So the instruction reads *use `Text`, not `Text label`*, and the transcript's *"E"* is an ASR mishearing of *"A"*. <br><br>**Why this is admissible.** It is a fact about **what a displayed dialog shows** — D-025's descriptive class — and it concerns a **platform artifact, not a market rule**. It resolves an ambiguity this session raised about V05's own ASR, not an open question about the methodology, so no instructor record is closed on guest evidence. See the flag in `V05_SOURCE_NOTES.md` §4a. |
| 5 | `V05_00-06-40_slide-draw-rectangle-box-mt4.png` | `06:40` | Toolbar with the rectangle tool called out; a blue filled box drawn on a chart. Annotations *"Click this and draw Box"*, *"Double Click to make sure you see these dots."* |
| 6 | `V05_00-07-35_slide-rectangle-properties-colour-width.png` | `07:35` | MT4 **Rectangle** properties dialog, Common tab. Fields legible: `Name: Rectangle 49536`, `Style: DarkOrange`. Annotations *"Click & Select Color"*, *"Select Width"*, *"Uncheck"* (pointing at `Draw object as background`). |
| 7 | `V05_00-09-24_slide-trendline-parameters-uncheck-ray.png` | `09:24` | MT4 **Trendline** properties, **Parameters** tab. Both anchor points printed: `Time: 2012.03.22 13:15  Value: 111.402468` and `Time: 2012.03.22 18:15  Value: 111.483132`. Annotation *"Uncheck Ray"*. **The values imply a JPY-quoted pair** (~111.4) on a 2012-03-22 chart — three days before this session. Recorded as a fact about the dialog; the pair is **not** named on the slide and is not inferred here. |
| 8 | `V05_00-11-59_slide-anchor-or-peak-boxed-three-hits.png` | `11:59` | First worked chart. Printed labels: `3 Hits to the Hi`, `Level 3`, `Label`, annotations *"Find your ANCHOR"* and *"Draw a box around the Peak"*. Cyan boxes and orange rectangles are the drawing objects taught in frames 5–7. |
| 9 | `V05_00-12-39_slide-write-out-the-days.png` | `12:39` | Same chart advanced: `Day 1` / `Day 2` separators added, annotation *"Write out the Days"*, plus *"Know where your Drops begin & Ends"*. |

### The deck — the Anchor and the MM cycle ⚠ NORMATIVE CONTENT

| # | File | Timecode | What is shown |
|---|---|---|---|
| 10 | `V05_00-10-29_slide-find-the-anchor.png` | `10:29` | **"Find the Anchor…"** — the single densest slide in the lesson. Transcribed verbatim from a 2× upscale: <br>• *"The Anchor or Peak formation High or Low is where the MM start their move after Trapping volume."* <br>• *"You will find the Anchor usually in Level 3.  (Level 1 in a Reset…… which was covered in the DMR last week)"* <br>• *"This could be after 2 to 3 days of rise or fall but up to 5 days."* <br>• *"Level 3 or the 3rd day of the movement cycle is usually very choppy."* <br>• *"Identify a Multi-Day, Multi Session M or W pattern; 3 Hits to the Hi or Lo; Extended Peak formation and draw a BOX around the Anchor."* <br><br>**`NORMATIVE — EXCLUDED` on bullets 2–4.** Bullets 2 and 3 are a day-count / holding-period claim and bullet 4 a characterisation of the 3rd day. `C-001` (day count away from the anchor) is **unresolved in the instructor's own words**, and D-025 forbids citing guest material for **or against** an instructor rule. **These bullets may not be used to settle `C-001` and are not.** They are recorded against `C-001` as a corpus-hygiene extension only. Bullets 1 and 5 are admissible descriptively as **terminology** (that "Anchor", "Peak formation", "Trapping volume", "3 Hits to the Hi or Lo", "Extended Peak formation" are the terms in use, and that they are spoken of as one object) — which bears on open item 2 (`I7`: whether anchor point / peak-formation high-low / M-or-W formation are one concept) and **extends** it without closing it. |
| 11 | `V05_00-15-49_slide-three-days-of-drop-expect-reversal.png` | `15:49` | Chart with `Day 1`/`Day 2`/`Day 3` separators and a red callout box printing **"3 Days of Drop Expect a Reversal"**. `NORMATIVE — EXCLUDED`, same ground as frame 10, and the sharpest single instance of it in the lesson. |
| 12 | `V05_00-17-44_slide-mm-cycle-played-out-over-three-days.png` | `17:44` | **"The MM Cycle played out over 3 days…"** — the same chart fully marked, `MM Cycle` label, `Level 1`/`Level 2`/`Level 3` bands, `Day 1`–`Day 3`. |
| 13 | `V05_00-18-19_slide-mark-the-patterns-and-entries.png` | `18:19` | **"Mark the Patterns and Entries…"** — `Multi Day M`, `M`, `Enter` labels on the marked chart. |
| 14 | `V05_00-20-19_slide-level-1-drop-1-from-the-peak.png` | `20:19` | **"Level 1 or Drop 1 from the Peak…"**, callout printing *"Level 1 = Expect Stop Hunt & Drop"*. |
| 15 | `V05_00-23-14_slide-level-2-drop-2-from-the-peak.png` | `23:14` | **"Level 2 or Drop 2 from the Peak…"**, callout *"Level 2 = Expect Stop Hunt & Drop"*. |
| 16 | `V05_00-24-24_slide-level-3-new-peak-or-anchor-formation.png` | `24:24` | **"Level 3 or New Peak or Anchor formation…"**, callout, read at 3× and transcribed exactly: *"Level 3 = Expect Reversal after 3 days of Drop (up to 5 days)   Identify the Pattern and mark the Entry if CLEAR"* (no full stop after the parenthesis; the gap before *"Identify"* is the slide's own spacing). `NORMATIVE — EXCLUDED` on the day count, as frames 10–11. A label reading **`R = 39.0`** sits beneath the cyan box on this frame — descriptive evidence extending `A-018` (the meaning of `R`), which V03 §4e enumerated and did not close. |
| 17 | `V05_00-25-54_slide-mm-full-cycle-drawn-out.png` | `25:54` | **"MM Full Cycle drawn out…"** — the complete cycle on one chart: `3 Hits to the Hi`, `BIG M`, `A1`, `A2`, `Level 1`–`Level 3`, `Day 1`–`Day 3`, entries boxed. The most complete single visual statement of the cycle anywhere in V01–V05. |

### The deck — patterns, TDI, flash cards

| # | File | Timecode | What is shown |
|---|---|---|---|
| 18 | `V05_00-33-29_slide-m-pattern.png` | `33:29` | **"If you do not like the Cycle… Go with the Patterns…"** / underlined **"M pattern"**. Chart with `M` labelled and an `Enter` box. |
| 19 | `V05_00-35-19_slide-w-pattern-three-swipes.png` | `35:19` | Underlined **"W pattern"**. Chart labels `3 Swipes`, numbered `1` `2` `3`, `W`, `Divergence`. A **TDI-style sub-panel is visible at the bottom** with `Divergence` written on it. |
| 20 | `V05_00-35-54_slide-mark-up-the-tdi-as-well.png` | `35:54` | **"Mark up the TDI as well…"** — chart plus a lower sub-panel carrying oscillator lines, with `Divergence` labelled on **both** the price chart and the sub-panel. <br><br>**Bearing on `A-039` (TDI is a required condition of V04's entry rule and has never been taught):** this is the **first slide in the corpus whose title instructs the student to mark up the TDI**, and it is still **"displayed, not taught"** — no inputs, no periods, no band construction, no numeric thresholds and no decision rule are recoverable from it. It also **cannot** narrow `A-039`: it is guest material, and under D-025 only an instructor statement can close a record. Recorded as a **descriptive extension** of `A-039`, exactly as V04's frames 21–22 were under review `M6`. **`A-039`'s prohibition on dropping condition (c) to make the rule testable is untouched.** |
| 21 | `V05_00-36-54_slide-shark-fin-half-batman.png` | `36:54` | **"Shark Fin…"** — chart printing `1/2 Batman` at the peak and `Enter`; the lower sub-panel prints **`Shark Fin`** inside a drawn box. Descriptive evidence that `Shark Fin` names a shape **on the oscillator sub-panel**, and that `1/2 Batman` is a distinct printed term. Both **extend** `A-039`'s vocabulary and close nothing. <br><br>**Three further readings taken from the 2× re-render, which is the one deck slide whose embedded screenshot is large enough to read.** <br>• **Price-chart header: `GBPUSD,M15  1.58700 1.58719 1.58691 1.58703`.** Internally consistent as an OHLC quadruple — `L 1.58691 ≤ O 1.58700 ≤ C 1.58703 ≤ H 1.58719` — which is the same ordering check frame 26 uses, and the check that distinguishes a reading from a guess. **This is the only place in V05 where a deck slide names its own timeframe**, and it is `M15`. <br>• **Sub-panel header: `TDI_MMM 54.6718 55.0688 53.6150`.** The oscillator is **named `TDI_MMM`** on screen and plots **three** values. This is the first time the corpus has the indicator's *displayed name*. It remains **untaught**: no inputs, periods, band construction or thresholds are shown, so `A-039` is **extended, not narrowed**. <br>• **Date axis: `14 Feb 2012`, ticks `07:30` … `18:30`.** <br><br>**This refines "WHAT THE VISUALS ADDED" item 9 below.** The deck is **not** drawn from a single data period: this slide is **14 Feb 2012**, while frames 16 and 26 are **early Jan 2012**. The claim that the taught examples and the live demonstration share one dataset holds for the Jan frames only. |
| 22 | `V05_00-38-19_slide-save-as-picture-zen-man-folder.png` | `38:19` | MT4 **Save As** dialog. Navigation pane prints `Libraries`, `Homegroup`, **`Zen_man` / `System Folder`**; `File name: M Pattern`; `Save as type: GIF File (*.gif)`. See § "THE ZEN_MAN FINDING" above. The preceding frame (sweep idx 457, `38:05`, not curated) shows the **Save As Picture** dialog with `Active workspace` selected and MT4's own notice permitting free reproduction of screenshots bearing its copyright notice. |
| 23 | `V05_00-38-34_slide-flash-card.png` | `38:34` | **"Flash Card…"** — verbatim from a 2× upscale: <br>• *"Once you have the Mona Lisa of the M & W pattern, you need to make a Flash Card out of it."* <br>• *"You need to have the Flash Card handy when you trade so that you can cross reference it when you think you see your Pattern."* <br>• *"Write a Checklist of what makes the setup good while doing R&D.  (that's what R&D is for)"* <br>• *"The R&D and the flash card should make you confident in your setups and know that you are going to be **80%+ accurate**."* <br><br>**⚠ `D-009` — a new advertised accuracy claim.** *"80%+ accurate"* is recorded **with provenance as a hypothesis to test**, never as a performance requirement or a pass/fail criterion. It is a **second, lower, guest-sourced** figure alongside V01's instructor 90–95% claim, and the two are **not** reconciled here. `NORMATIVE — EXCLUDED` as well: it is guest material and may not be cited for or against the instructor's figure. |

### The deck — closing slides

| # | File | Timecode | What is shown |
|---|---|---|---|
| 24 | `V05_00-50-43_slide-evolution-of-a-trader.png` | `50:43` | **"Evolution of a Trader…."** — a three-panel cartoon captioned `DAY & NIGHT TRADER`, `DAY TRADER`, **`Steve Mauro Method`**, with a red bubble reading *"thanks to Gary T"* (or `Gary T J` — the final glyph is not certainly legible and is **not** resolved here). |
| 25 | `V05_00-51-28_slide-hindsight-foresight-sm-attribution.png` | `51:28` | Text-only slide: **"If you never see it in hindsight, you will never see it in foresight…….~SM~"**. <br><br>**Read carefully:** this is a **guest-authored slide printing a quotation attributed to `~SM~`**. It is **not** an instructor statement in this recording, and it is not treated as one. What it evidences descriptively is that the guest attributes this maxim to Steve Mauro. Under D-025 a printed attribution cannot promote guest material to instructor weight, so **it may not be cited as an instructor rule**, and the underlying maxim is **not** entered into the concept library on this basis. Re-displayed with red freehand annotation at `60:35` and `62:50` (sweep idx 727, 754). |

### The live MT4 session

| # | File | Timecode | What is shown |
|---|---|---|---|
| 26 | `V05_00-40-04_live-mt4-gbpusd-m15-ohlc-status-bar.png` | `40:04` | Full Windows desktop, live MT4. **Title bar: `67342442: FXDD - MetaTrader - Demo Account - [GBPUSD,M15]`** — a **demo** account, broker FXDD, and `GBPUSD`, which is `D-007`'s primary research instrument. Taskbar clock **`10:31 PM  3/25/2012`** (see above). **MT4 status bar, read from the platform's own text at 9× magnification:** profile `4 Majors`, cursor bar **`2012.01.04 01:15`**, **`O: 1.56413  H: 1.56418  L: 1.56374  C: 1.56381  V: 352`**. The reading is **internally consistent as an OHLC bar** — `L ≤ C ≤ O ≤ H`, i.e. `1.56374 ≤ 1.56381 ≤ 1.56413 ≤ 1.56418`, so low is the lowest and high the highest of the four. That consistency is the check that the digits were read rather than guessed; a misread digit would almost certainly break the ordering. Chart is marked with `3 Hits to the Hi`, `Level 3`, cyan boxes and orange level rectangles. **A multi-line oscillator sub-panel is displayed beneath the price pane** — the same object family recorded on frames 19, 20 and 21. It carries a header label in the same position as frame 21's `TDI_MMM` header, but **that header is at the edge of legibility at this resolution and is deliberately NOT transcribed**; only its presence is recorded. **Displayed, not taught** — the presenter neither points at nor discusses this panel at `40:04`, and this row **does not narrow `A-039`** (guest material, `D-025`). |
| 27 | `V05_01-04-58_live-mt4-level-2-big-w-markup.png` | `64:58` | Live MT4, later markup: `Level 2` band, `BIG W` labelled at the right-hand rise, cyan entry boxes. **The status-bar OHLC row in this frame is NOT transcribed** — at 9× magnification its glyphs are genuinely ambiguous (the `L:` label is overwritten and the `H:` field reads implausibly), and an internally inconsistent reading is worse than a declared gap. Following the V04 review `M6` precedent: declining to transcribe an illegible readout is the correct call, and saying so beats a guess. |
| 28 | `V05_01-07-38_live-mt4-reset-level-3-markup.png` | `67:38` | Live MT4, final substantive screen: `Level 3` band, **`RESET`** printed on the chart, full cycle marked. `RESET` is the term the "Find the Anchor" slide (frame 10) parenthesises as *"Level 1 in a Reset"*; this frame is descriptive evidence that the term is applied to a specific chart location. |
| 29 | `V05_01-08-25_end-of-recording-replay.png` | `68:2x` | The recording's final state: the Camtasia player's **replay** button over a dimmed last chart. Carried for one reason only — it is the frame that shows the sweep reached the **end** of the film. Together with the burned total `68:2x` it closes the coverage claim: the capture ran from the title slide to the replay button with no fenced tail, so no section of V05 is unrepresented because the capture stopped early. |

---

## WHAT THE VISUALS ADDED

1. **A fourth independent duration derivation** and the burned-in `68:2x` total, tightening
   the transcript's I-008 length check.
2. **The session date, on screen** — `3/25/2012`, corroborating a date the transcript could
   only take from the filename.
3. **`Zen_man`** — provenance for the deck's chart images, and (with the `[00:01:41]`
   passage) a strengthening of the transcript's "third voice" finding rather than a
   challenge to it.
4. **The homework, printed.** Frame 3 is an explicit task list. V05's homework does not have
   to be inferred from prose.
5. **The MM cycle drawn out end to end** (frames 8, 9, 11–17) — the fullest visual statement
   of `Level 1`/`Level 2`/`Level 3`, `Day 1`–`Day 3`, `A1`/`A2` and entry placement in the
   corpus so far. All `GUEST`; none of it enters the methodology.
6. **`Shark Fin` and `1/2 Batman` located on the oscillator sub-panel**, and a slide titled
   *"Mark up the TDI as well"* — the strongest descriptive evidence yet that TDI is
   **displayed and marked up** in this course while remaining **untaught**. `A-039` is
   extended, not narrowed.
7. **Real, verifiable price data from platform text** — one GBPUSD M15 bar
   (`2012.01.04 01:15`, FXDD server time) with full OHLC, read from MT4's own status bar
   rather than from pixel colour, and internally consistent. Used in `V05_HOMEWORK.md`.
8. **A second accuracy claim, `80%+`** (frame 23), recorded under `D-009` as a hypothesis.
8a. **The text-tool instruction, made readable** (frame 4a). MT4's `Text` and `Text label`
   objects carry the literal icons `A` and `T`, so the transcript's garbled *"E … T … A"*
   resolves to *use `Text`, not `Text label`*. A platform fact, not a market rule.
8b. **`TDI_MMM`, the indicator's displayed name**, and a legible `GBPUSD,M15` deck header
   (frame 21) — the only deck slide that names its own timeframe.
9. **The deck's charts and the live session are the same data period.** Frame 16's x-axis
   labels read `4 Jan 20:15`, `4 Jan 22:15`, `5 Jan 00:15`, `5 Jan 03:15` … and the live
   session's status bar reads `2012.01.04 01:15` — so the worked examples in the slides and
   the live markup are both **early January 2012 GBPUSD M15**, about eleven weeks before the
   2012-03-25 session. This matters for the homework: the taught examples and the live
   demonstration can be checked against **one** historical dataset.

## WHAT THE VISUALS DID NOT SETTLE

- **The presenter's name.** No frame names him. `Zen_man` is a folder on the machine that
  produced the deck's images, and the audio places the speaker beside Zen, not as Zen.
- **`C-001`.** Four slides state a day count. All four are guest and normative, so under
  D-025 not one of them may be cited for or against the instructor's self-contradiction.
  **`C-001` remains `UNRESOLVED` and this lesson cannot resolve it.**
- **`A-039` / TDI.** Displayed, marked up, named — still not defined. No inputs, bands or
  thresholds are recoverable.
- **The pair in frame 7's Trendline dialog** (~111.4). JPY-quoted, unnamed, not inferred.
- **The `Gary T` attribution** in frame 24 — final glyph not certainly legible.
- **Frame 27's OHLC row** — declared illegible rather than transcribed.
