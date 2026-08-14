# V16 — SCREENSHOT INDEX

**Source:** `Bootcamp1 Wk7 050612 Part2 (45mins).swf` · V16 · 2012-05-06 · 00:44:35
**34 curated frames** from a **544-frame** 10× sweep. Every frame is the full **1024 × 786** stage
**including the control bar**, so each image **proves its own timestamp** from the burned-in player
readout (`SWF_CAPTURE_RECIPE.md` §8).

---

## §0 — ⚠⚠ `SWF_CAPTURE_RECIPE.md` §8a — THE MANDATORY SWEEP→CLOCK OFFSET MEASUREMENT

**§8a is a numbered required step, added by the V14 R1 remediation (`REVIEW_INDEX.md` items 174 /
186) because V14 skipped it and shipped 29 frames whose filenames were all `+16 s` wrong. It was
run here, before any frame was named.**

### §0.1 — THE MEASUREMENT

`offset = burned_timecode − (i × 5)`, read from the pixels of the bottom-right `MM:SS / MM:SS`
readout, cropped `140 × 24` at `(900, 762)` and upscaled 5× with nearest-neighbour.

| Sweep index `i` | Filename second `i × 5` | **Burned timecode, read from pixels** | **Offset** |
|---|---|---|---|
| 0 | 0 | `00:15` | ⚠ **+15** — see §0.3 |
| 1 | 5 | `00:16` | ⚠ +11 |
| 2 | 10 | `00:16` | ⚠ +6 |
| 3 | 15 | `00:17` | ⚠ +2 |
| **4** | **20** | **`00:20`** | **0** |
| **5** | **25** | **`00:25`** | **0** |
| **10** | **50** | **`00:50`** | **0** |
| **20** | **100** | **`01:40`** | **0** |
| **60** | **300** | **`05:00`** | **0** |
| **100** | **500** | **`08:20`** | **0** |
| **200** | **1000** | **`16:40`** | **0** |
| **300** | **1500** | **`25:00`** | **0** |
| **400** | **2000** | **`33:20`** | **0** |
| **500** | **2500** | **`41:40`** | **0** |
| 535 | 2675 | `44:35` | **0** — and this is the **clamp**: `44:35` is the file's own duration |
| 543 | 2715 | `44:36` | clamped, as §8a says to expect |

⭐ **THE OFFSET IS ZERO for every frame from `i = 4` onward — measured at TEN points spread across
the file, plus the clamp.** V12 measured `+16`, V13 `+15`, V14 `+16` (unmeasured, shipped wrong),
V15 `+15`. **V16 is the first to measure zero, and that is not luck — see §0.2.**

### §0.2 — ⚠ WHY IT IS ZERO: A DECLARED DEVIATION FROM §10, AND IT CONFIRMS OPEN ITEM 188

**`REVIEW_INDEX.md` item 188 (V15 student) diagnosed the cause of the `+15/+16` band and proposed a
one-line fix: `set t0 immediately BEFORE the click and take the guard screenshot after`,** on the
argument that the dominant term was the recipe's own **fixed `1500 ms` guard** sitting between
`p.mouse.click()` and `const t0 = Date.now()` — which at `SPEED = 10` is **exactly 15 presentation
seconds**.

**This session's `sweep.mjs` has `t0` before the click.** That is a **deviation from
`SWF_CAPTURE_RECIPE.md` §10 as written**, and it is declared here rather than presented as a
compliant run.

**The measurement above is therefore item 188's prediction, tested:**

| | Predicted | Measured |
|---|---|---|
| Offset with `t0` **after** the click + guard | `+15` to `+16` s | V12 `+16`, V13 `+15`, V14 `+16`, V15 `+15` — **4 of 4** |
| Offset with `t0` **before** the click | **0**, leaving only sub-second latency | **0 at ten points** |

⭐ **Item 188's diagnosis is CONFIRMED, and its proposed fix WORKS.** ⚠ **It is NOT applied to the
recipe here.** `SWF_CAPTURE_RECIPE.md` is a **policy ledger** and `D-038a` puts policy edits on the
integration branch, never on a lesson branch. The edit is owed and is raised as open item **197**.

⚠ **§8a's per-lesson measurement requirement must survive the fix.** Zero here does not license
assuming zero next time — that is exactly the reasoning that produced V14's 29 wrong filenames.

### §0.3 — THE FOUR EARLY FRAMES, AND WHY THEY ARE NOT DRIFT

Frames `i = 0..3` read `00:15`–`00:17` instead of `00:00`–`00:15`. **They are not an offset and not
drift: they are four screenshots taken during the `1500 ms` guard, before the pacing loop's first
deadline had passed.** With `t0` before the click, deadlines `t0 + 0/500/1000/1500 ms` are all in
the past by the time the loop starts, so the first four shots fire back-to-back at ~`00:15`–`00:17`
of presentation time and the grid locks from `i = 4`.

**Consequence, and it is why this section exists: the first 15 seconds of V16 were NOT sampled on
the 5-second grid.** They are covered by four near-identical frames of the title slide. **No frame
from `i < 4` is used or named in this index.** The earliest committed frame is `i = 4`
(`V16_00-00-20`).

### §0.4 — THE ORIGIN/RATE CHECK (§8a step 3)

§8a step 3 requires proving the error is an **origin** error, not a **rate** error: consecutive
filename deltas must equal consecutive burned deltas.

| Pair | Filename Δ | Burned Δ | Match |
|---|---|---|---|
| `i=20 → 100` | 400 s | `01:40 → 08:20` = 400 s | ✅ |
| `i=100 → 200` | 500 s | `08:20 → 16:40` = 500 s | ✅ |
| `i=200 → 300` | 500 s | `16:40 → 25:00` = 500 s | ✅ |
| `i=300 → 400` | 500 s | `25:00 → 33:20` = 500 s | ✅ |
| `i=400 → 500` | 500 s | `33:20 → 41:40` = 500 s | ✅ |

**The rate is exact. The fps patch (`3.0 → 30.0`, read from this file's own header) was correct.**

---

## §1 — CAPTURE PROVENANCE

| Field | Value |
|---|---|
| Source SHA-256 | `ecac17c41700839beb4091de94b61fe0cb5a4922e9de764ad482eb8d318c538a` — verified **before** the frame-rate patch and **re-verified after**, unchanged |
| SWF header, read this session | `frameRate 3.0` · `frameCount 8029` · stage **1024 × 786** |
| Patch | `3.0 → 30.0` fps on a **copy** in the scratchpad (`v16_x10.swf`); original never opened for writing |
| Server | fresh port **8941**, `lsof` verified as this session's own `python3`, and the served bytes SHA-matched against the local file (`GOTCHA 4`) |
| Play click | `(512, 300)` from `GOTCHA 5`'s table for a `1024 × 786` stage, and **confirmed by the before/after guard** — `sweep.log`: *"play click confirmed: stage changed"* |
| Sweep | 544 frames, one every **5 presentation-seconds** |
| Curated | **34** frames, 7.4 MB |
| Screen detection | pairwise mean-luminance diff on `256 × 190` downscales, runs collapsed within 10 s → **26 distinct screen states** at threshold `1.5` (and **25** at `6.0` — the threshold barely matters here, see §3) |

---

## §2 — NEGATIVES, STATED BEFORE THE POSITIVES

Across all **544** sweep frames — not just the 34 committed:

| Sought | Found |
|---|---|
| An indicator **properties dialog** | **NONE** |
| The MT4 **Navigator** panel | **NONE** |
| An **inputs tab** or parameter tuple in any legend | **NONE** |
| A **TDI** sub-panel at legible resolution | **NONE** — the word occurs once in audio, on the drill roll-call |
| A **stop-loss** annotation of any kind | **NONE** — consistent with `stop loss` occurring **0** times in the transcript |
| An **Asian box** drawn and labelled | **NONE** — `Asian box` occurs **0** times; the two blue rectangles at `34:30`/`34:50` are unlabelled |

⭐ **`A-084`'s in-corpus frame hunt is now `3,214` frames across V12–V16 with no dialog.**
`COURSE_PROGRESS.md`'s V16 GATE (b) said **do not spend V16 hunting for it**, and this session did
not — the negative is a by-product of a sweep run for other reasons, which is the only reason it is
cheap enough to report.

⚠ **VERIFIABILITY LIMIT, same class as items 140, 146 and 194:** the **544** sweep frames are
**NOT** committed; the **34** curated ones are. Every negative above is directly verifiable for the
34 and rests on this session's reading for the other 510. **Reproducible from §1 in about five
minutes.**

---

## §3 — ⭐ THE SHAPE OF THIS LESSON, VISIBLE IN THE DETECTOR OUTPUT

**The screen-state detector found NO change between `i = 19` (`01:35`) and `i = 173` (`14:25`) at
either threshold.** That is **thirteen minutes on one slide** — and it is a finding, not a
detector failure: the two largest diffs in the whole file are exactly those two transitions
(`152.3` and `147.9`, against a next-largest of `31.4`).

**V16 is a lecture delivered over a whiteboard, not a deck.** The `Pivot Points` grid slide is put
up at `01:35` and drawn on continuously until `14:25`. The annotation strokes are individually too
small to trip a `256 × 190` mean-luminance detector, so the curated frames through that span were
chosen **from transcript-flagged moments**, not from the detector — declared here because it means
those eleven frames are a **judgement sample**, not an automatic one.

---

## §4 — THE FRAMES

**Naming:** `V16_HH-MM-SS_descriptor.png`, timestamp taken **from the burned-in player timecode**
(§8a step 4), descriptor = *what is shown, not what it means* (`FILE_NAMING_STANDARD.md` §3).
**Every frame below was opened and looked at before it was named.**

### The deck

| # | Frame | What is on screen | Cited by |
|---|---|---|---|
| 1 | `V16_00-00-20_title-slide-pivot-points` | ⭐ `Pivot Points` / *"How to Project High and Low"* / *"Intra-Day Support and Resistance"* / *"Possible Trading Range"* — **the lesson's printed title** | notes §1 |
| 2 | `V16_00-00-50_pivot-points-four-bullets-slide` | ⭐ *"Calculated on Daily Candles"* · *"Yesterday's Price Action Gives Tomorrow's Pivot Points"* · *"Red Candle Indicates M1/M3 Day"* · *"Green Candle Indicates M2/M4 Day"* | notes §3 |
| 3 | `V16_00-01-40_pivot-grid-diagram-100-pips-annotated` | ⭐⭐ **Three columns.** Centre: the nine-level grid `R2 M4 R1 M3 CPP M2 S1 M1 S2` with `OVER BOUGHT` (red) / `SHADES OF GREY` / `OVER SOLD` (green) zones. Left, labelled **`M1/M3`**: a capsule spanning `M1`→`M3`, red above `CPP`, green below. Right, labelled **`M2/M4`**: a capsule spanning `M2`→`M4`. **The two capsules ARE the two projected ranges of §3's colour rule, drawn as candles.** Bottom-right: `PRICE AT LONDON OPEN` → red `SELL`, green `BUY`. Plus a hand-written yellow `100` | notes §2, §3, §4; interp §3 |
| 4 | `V16_00-02-30_grid-annotated-100-and-cpp-tick` | Grid + the yellow `100`; one short stroke beside `CPP` | notes §4 |
| 5 | `V16_00-03-30_grid-annotated-25-and-m1-circled` | A yellow `25` written at upper-left; `M1` circled | notes §4 |
| 6 | `V16_00-04-30_grid-annotated-100-and-drawn-price-path` | A second `100` written lower-left; a freehand price path drawn beside the `M1/M3` capsule | notes §4 |
| 7 | `V16_00-05-30_grid-annotated-price-path-with-3` | The price path extended, with a hand-written `3` beside it | notes §4 |
| 8 | `V16_00-07-00_grid-annotated-rising-curve-to-right-column` | A long rising freehand curve drawn from the left capsule across to the `M2/M4` column | notes §4 |
| 9 | `V16_00-08-00_grid-annotated-sketch-right-of-grid` | A freehand sketch to the right of the `M2/M4` column | notes §4 |
| 10 | `V16_00-09-30_grid-annotated-right-column-circled` | The `M2/M4` column enclosed in a yellow loop. ⚠ **`ADR` is NOT yet written here** — see §6 below | notes §6 |
| 11 | `V16_00-10-00_grid-annotated-adr-written-top-left` | ⭐ `ADR` written in capitals at top-left, ~30 s after the lookback line, with the `M2/M4` column still looped | notes §6 |
| 12 | `V16_00-11-00_grid-annotated-adr-and-right-sketch` | `ADR` still on screen; further freehand sketching to the right of the `M2/M4` column | notes §5 |
| 13 | `V16_00-13-00_grid-annotated-bottom-sketch` | Freehand strokes across the lower third of the slide, over the legend | notes §5 |
| 14 | `V16_00-14-00_grid-annotated-final-state` | The whiteboard's final state before the slide changes at `14:25` | notes §4 |
| 15 | `V16_00-14-25_london-session-start-2-to-3am-est-slide` | ⭐⭐ `London Session Start` / **`2:00 To 3:00 AM, EST`** / red→`SELL`, green→`BUY`. **The corpus's first printed, timezone-stamped session boundary** | notes §9a; interp §5 |
| 16 | `V16_00-15-00_london-start-slide-m1m3-down-m2m4-up` | Same slide, annotated `M1/M3 DOWN DAY` (red) and `M2/M4 UP DAY` (green) | notes §3 |
| 17 | `V16_00-16-50_pivot-grid-on-price-scale-chart` | The grid overlaid on a live price scale ⚠ **price axis not legible at this resolution — see interp §3** | interp §3 |
| 18 | `V16_00-17-30_pivot-grid-chart-annotated-range` | Same, with the range bracketed by hand | interp §3 |
| 19 | `V16_00-18-00_m3-m4-hods-m1-m2-lods-slide` | ⭐ *"M3 And M4 Are Possible HODs"* / *"M1 And M2 Are Possible LOD's"* / *"Subtract The Value Of Today's Projection And This Is The Trading Range · Ex: ( M1 – M3)"* | notes §2 |
| 20 | `V16_00-20-10_pivot-points-m1-m3-day-chart` | Worked example, titled `Pivot Points M1/M3 Day` | notes §1 |
| 21 | `V16_00-21-00_pivot-points-m2-m4-day-chart` | Worked example, titled `Pivot Points M2 /M4 Day` | notes §1 |
| 22 | `V16_00-23-10_m2-m4-day-chart-annotated-200` | Same chart, hand-written `200` bracketing the day's range | notes §10 |
| 23 | `V16_00-25-10_price-fails-at-m3-pivot-4-times` | ⭐ Printed captions **on the chart**: `Price Fails at M3 Pivot 4 Times` and `Signal Line Cross` | notes §1 |
| 24 | `V16_00-26-10_level-three-day-chart` | The *"level three day"* example | notes §1 |
| 25 | `V16_00-27-10_asian-range-half-batman-annotated` | The *"half a batman"* example, annotated | notes §13 |
| 26 | `V16_00-27-45_pp-are-an-adr-grid-slide` | ⭐⭐ *"PP Are An ADR Grid, The Extremes Are Representative Of ADR High /Low."* / *"Since The Grid Is Fixed, And Trading Ranges Are Not, We Couple Pivots With ADR Markers For Strong Confirmations"* | notes §7 |
| 27 | `V16_00-29-10_pivots-intraday-sr-you-are-the-filter-slide` | ⭐ *"Pivots Are Intraday Support And Resistance"* / *"A Break Of One Level Is Almost Always Certain To Give Way To The Next Pivot Level"* / **`YOU Are The Filter!`** | notes §8 |
| 28 | `V16_00-32-05_big-market-moves-disrupt-pivots-slide` | ⭐ *"Big Market Moves Will Often Disrupt The Pivot Points…"* / *"…Wrong Segment Of The Trading Zone…."* / **`Ignore The Pivots and Identify the Pattern`** | notes §8 |
| 29 | `V16_00-34-10_price-in-wrong-segment-m-sell-chart` | Caption `Price in wrong Segment M is clearly visible….Sell` | notes §8 |
| 30 | `V16_00-34-50_straight-away-sell-blue-box-annotated` | Caption `Straight Away….Sell`, with an **unlabelled** blue rectangle over the pre-London range | notes §8; §2 above |
| 31 | `V16_00-35-05_r-and-d-homework-six-majors-slide` | ⭐⭐ `R&D` / *"Find the Expected High/Low for the day on the 6 majors, using Pivot calculations."* / *"Do it pre London for Mon & Tues"* | notes §11; homework |
| 32 | `V16_00-36-35_boot-camp-r-and-d-roll-call-slide` | ⭐ `Market Maker Boot Camp` / `R& D` · `Continue with your flash cards` · `TDI only trades` · **`Big board only entries`** · `Moving Avg Only Trades` · `Estimate the High and Low using pivots` ⚠ audio says *"big board only **trades**"* | notes §11 |
| 33 | `V16_00-39-55_good-night-see-you-next-sunday-slide` | `Good night` / `See You Next Sunday!` — shown, then **abandoned**; he returns to the roll-call for five more minutes of Q&A | notes §1 |
| 34 | `V16_00-44-35_end-of-file-r-and-d-slide` | The final frame. Timecode reads `44:35 / 44:35` — the clamp, and the proof the sweep covered the whole file | §0.1 |

---

## §5 — WHAT THE FRAMES CORRECTED OR RESOLVED THAT THE AUDIO COULD NOT

`SWF_CAPTURE_RECIPE.md` §9 says this is the whole point of keeping the two passes separate.

| # | The audio alone | The frames |
|---|---|---|
| 1 | *"the top, upside of the pivot grid, you're a seller"* — **no level names, no order** | ⭐ The **complete nine-level order**, printed (frame 3) |
| 2 | *"At the moment open"* — an ASR failure with no recoverable content | ⭐ A **printed session boundary with a timezone** two seconds later (frame 15) |
| 3 | *"M1 M3 day"* / *"M2 M4 day"* — spoken as jargon | The **colour rule printed as two bullets** (frame 2) and **hand-drawn as `DOWN DAY` / `UP DAY`** (frame 16) |
| 4 | *"there's like 150 pips possible for the day"* — an unattributed number | The chart it is read off, with `Pivot Points M1/M3 Day` in its own title (frame 20) |
| 5 | The lesson *sounds* like a deck talk | ⭐ It is **thirteen minutes on one whiteboard** (§3) — which is why the annotation frames, not the slides, carry the argument |

### ⚠ AND ONE THING THE FRAMES DID **NOT** RESOLVE, RECORDED BECAUSE IT IS THE EXPENSIVE ONE

**The price axis on frames 17 and 18 is not legible at `1024 × 786`.** Those two frames are the
only place in the file where the pivot grid and real prices appear together, and reading them
**would settle whether `M1`–`M4` are arithmetic midpoints** (interp §3). **I could not read them
and I did not guess.** A higher-resolution re-capture of those two moments is the cheapest open
route to closing `A-101`, and is raised as open item **198**.

---

## §6 — ⚠ SELF-CORRECTION, CHARGED AGAINST THIS SESSION

**Eleven of these thirty-four frames were first named from the transcript, and the names were
wrong.** The whiteboard span `02:30`–`14:00` has no slide changes, so the detector supplied no
candidates and the eleven frames through it were chosen by clock position against the transcript.
The first-draft descriptors then described **what the speaker was saying at that second** —
`asian-range-forms-at-central-pivot`, `m-formation-m3-target-m1-annotated`,
`three-intraday-pushes-annotated`, `candle-overlap-annotated`, `fourth-day-offset-annotated` — and
**not one of those things is visible in the frame it was attached to.**

**This is precisely the failure `SWF_CAPTURE_RECIPE.md` §8 names** (*"Naming from the transcript
alone reproduces the exact failure that produced the quarantined `VISUAL_INDEX.md`"*) — and this
session reproduced it, in a file whose whole job that week was to quarantine a fabricated
`VISUAL_INDEX.md` for doing the same thing.

**It was caught by rendering the eleven frames at `490 × 370` and looking at them**, which is the
remedy §8 already prescribes and which the first pass had done only at `300 × 225`. All eleven are
renamed above to what is actually on the glass.

⭐ **The sharpest instance, because it changes a citation and not just a name:**
`V16_00-09-30` was named `adr-written-on-grid-annotated` on the strength of `[00:09:31]` — the ADR
lookback line, the most important line in the lesson. **The word `ADR` is not written on that frame.**
It is written on `V16_00-10-00`, about thirty seconds later. The corrected index says so, and
`V16_SOURCE_NOTES.md` §6 cites the **audio** for the lookback, which is where the claim always
belonged.

⚠ **The reviewer should treat these eleven as a sample, not the population.** They are the ones a
second look caught.
