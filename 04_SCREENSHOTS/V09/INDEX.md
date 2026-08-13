# V09 — SCREENSHOT INDEX

26 curated frames from `Bootcamp1 Wk2 032612 Part4 (53mins).swf`
(SHA-256 `b0f36b5540de7a76397c80202cf6a721a2a18aa9011c5698238c6bcc624168d4`).

## HOW THESE WERE PRODUCED

`SWF_CAPTURE_RECIPE.md` §10 fast sweep at **10×** (`D-021`), with `D-022`'s port-and-bytes
verification performed **before** capture and recorded below.

| Step | What was done |
|---|---|
| Working copy | The original `.swf` was **never modified**. A copy was patched `frameRate 3.0 → 30.0` in the scratchpad; the original's SHA-256 was re-verified afterwards and is unchanged |
| Port | `8931` was probed first and found **BUSY** — another session's `python3 -m http.server` was already on it. **This is `GOTCHA 4` firing in real time**, and it is the reason the check exists. Port **8947** was probed, found free, bound by this session, and confirmed by `lsof` to be this session's own PID |
| Bytes | `curl` of `http://127.0.0.1:8947/v09_x10.swf` piped to `shasum` **matched** the on-disk patched copy |
| Content sanity check, **before** the long capture | A 10-second probe render was compared against the transcript. Burned timecode `01:41 / 52:2x`; slide reads *"Risk in FOREX is DEFINED as what % of our account balance would be lost if our trade went to Stop Loss?"*; transcript `[00:01:17]` reads the same sentence. **Agreed, so the capture was trusted** |
| Sweep | 640 frames, one every **5 presentation-seconds**, 320 s of wall clock |
| Screen detection | Consecutive-frame greyscale diff, threshold `mean > 6.0`, runs collapsed within 10 presentation-seconds → **29 distinct screen states**. Contact sheets were built and **looked at** before anything was named |
| Naming | Every filename's time was verified against the frame's **own burned-in player timecode**, read at 2× magnification. **26 of 26 match exactly, zero drift across 52 minutes** — see the verification block below |

> ### ⚠ THE FIRST SWEEP WAS DISCARDED, AND WHY IT IS RECORDED RATHER THAN QUIETLY REDONE
>
> The first 638-frame sweep produced **638 identical frames of a static splash screen**.
> `SWF_CAPTURE_RECIPE.md` §3's `mouse.click(512, 300)` — the coordinate that starts the
> Camtasia player on V01–V08 — **misses on this file.** Before playback V09 renders its stage
> in a small centred box, not full-window, and the play button sits at **(512, 325)**; the
> recipe's coordinate lands in the transport strip above it.
>
> **Nothing downstream looked wrong.** The server was verified, the bytes matched, `__ready`
> went true, 638 valid PNGs were written. The only thing that caught it was **opening a frame
> and looking at it** — which is the same lesson `D-020`'s retraction records in a different
> costume: *verify the input reached the system under test before trusting any output.*
>
> The fix was a probe run that clicked (512, 325) and screenshotted at +3 s and +10 s, and it
> was checked against the transcript before the full sweep was re-run. **`SWF_CAPTURE_RECIPE.md`
> §3/§10 should record that the play-button coordinate is per-file and must be confirmed from a
> pre-click screenshot — that is a POLICY-ledger edit under `D-038a` and is therefore owed on
> the integration branch, not made here.**

### Timecode verification — all 26

Read from each frame's own burned-in player timecode, which is what makes a screenshot prove its
own timestamp. `expected` is `frame_index × 5 s`.

```text
00:00:10 ✓   00:01:15 ✓   00:02:05 ✓   00:02:50 ✓   00:03:45 ✓   00:04:40 ✓
00:05:25 ✓   00:06:00 ✓   00:07:05 ✓   00:08:20 ✓   00:09:20 ✓   00:10:15 ✓
00:11:40 ✓   00:14:35 ✓   00:16:00 ✓   00:17:05 ✓   00:21:40 ✓   00:22:45 ✓
00:25:00 ✓   00:26:00 ✓   00:26:40 ✓   00:28:45 ✓   00:31:50 ✓   00:34:35 ✓
00:41:25 ✓   00:52:25 ✓
26 / 26 exact.  Every value is < the measured runtime 00:52:26.8, so this set does
not trip Q-009's first fabrication screen -- which V08's own set did (V08 R1 M3,
REVIEW_INDEX.md open item 66).
```

## THE FRAMES

| # | File | Time | Type | What is visible — read from the image | Relates to |
|---|---|---|---|---|---|
| 1 | `V09_00-00-10_ring-diagram-carried-over-from-v08.png` | `00:10` | SLIDE | **V08's four-ring diagram, with the red `?` at the centre**, still on screen while the presenter says *"Welcome back everybody"*. Printed: *"Not sure with my own eyes if MMFX method is valid"*, *"Validate the Method"*, *"Eliminate Skepticism"*, *"Learn to INSTANTLY recognize confirmation Candles"*, *"Still not able to fully ACT in line with the method…"*, *"I can see an M or W Pattern clearly AFTER it forms but can't see it BEFORE it forms…"* | **Cross-file continuity evidence.** V08 ended on this frame; V09 opens on it |
| 2 | `V09_00-01-15_risk-defined-as-percent-of-balance-at-stop.png` | `01:15` | SLIDE | *"Risk in FOREX is DEFINED as what % of our account balance would be lost if our trade went to Stop Loss?"* | `[00:01:17]`; **A-065** |
| 3 | `V09_00-02-05_lot-size-formula-balance-times-point-02.png` | `02:05` | SLIDE | Adds: *"One of the great benefits of trading with Defined Risk is that we are emotionally prepared if a Stop Loss happens. There is no unknown drop in our account balance."* and — **the formula, printed** — *"What makes the Risk DEFINED is the lot size we CHOOSE to put on. We multiply our account balance by .02 and divide our Stop Loss in pips into that number. That will determine the lot size."* | `[00:01:53]`–`[00:02:03]`; **the corpus's first position-sizing rule** |
| 4 | `V09_00-02-50_free-lot-size-calculators-on-the-web.png` | `02:50` | SLIDE | *"There are many FREE Lot Size Calculators on the web! Use one for the health of your equity curve!"* | `[00:02:48]` |
| 5 | `V09_00-03-45_three-losses-in-a-row-and-pure-three-to-one.png` | `03:45` | SLIDE | *"With 2% risk at Stop Loss, one can lose THREE TRADES IN A ROW and still have enough margin to come back and NEGATE the LOSS with just one trade!"* and *"Mastering **HOD/LOD** entries can allow one to trade with a PURE 3:1 Risk to Reward Ratio! Meaning one can LOSE THREE TIMES in a row and with one WINNER they can NEGATE THE LOSS!"* | **Resolves an ASR garble**: the transcript's *"high low-day entries"* is printed **`HOD/LOD`**. Extends **A-056** |
| 6 | `V09_00-04-40_two-to-one-until-hod-lod-skill-25-and-50.png` | `04:40` | SLIDE | *"Until one develops the HOD/LOD SKILL they can use a 2:1 Risk to Reward Ratio. Example: -25 pip S/L, +50 pip T/P. In this case TWO Stop Outs can be Negated with One Win."* | `[00:04:49]`–`[00:05:01]` |
| 7 | `V09_00-05-25_same-lot-size-until-the-loss-is-negated.png` | `05:25` | SLIDE | Adds: *"The idea is that we use a consistent Lot Size for the Win Loss Cycle. After we take a Stop Out we come back with the same Lot Size until we Negate the Loss. If our balance is only set back 2% at each Loss, we are sure to avoid Margin Issues for the 3rd or 4th Trade which will be the one which Negates the Loss."* | `[00:05:08]`–`[00:05:40]` |
| 8 | `V09_00-06-00_fourth-stop-loss-recalculate-at-eight-percent.png` | `06:00` | SLIDE | *"If one takes FOUR Stop Losses in a row it's time to Re Calculate Lot size as the account balance has now drawn down to 8% of original equity. 12,500 is now 11,500. 2% of 11,500 is 9.2 mini's or .92 Lots"* | `[00:05:54]`–`[00:06:01]`. **See `A-066`** — `[00:06:01]` *"drawn down eight percent"* vs `12,500 → 11,500`, which is **8.0%**, so the wording is loose but the arithmetic is right |
| 9 | `V09_00-07-05_first-winner-brings-balance-to-11960.png` | `07:05` | SLIDE | Adds: *"With a 2:1 Ratio (-25/+50) First Winning Trade brings balance up to 11,960"* | `[00:07:03]` |
| 10 | `V09_00-08-20_four-step-recap-of-the-lot-size-rule.png` | `08:20` | SLIDE | *"To Recap: Calculate Lot Size in relation to % of Balance Draw Down at Stop Loss. 2% is a good place to start. If you take a loss at S/L come back with the SAME LOT SIZE / If you lose a 2nd time come back with the SAME LOT SIZE / If you lose a 3rd time come back with the SAME LOT SIZE / If you lose a FOURTH TIME re calculate LOT SIZE as you are now down 8% of Original Account Balance…"* | `[00:08:20]`–`[00:08:43]`. **The complete rule, printed** |
| 11 | `V09_00-09-20_basic-idea-increase-on-wins-diminish-on-losses.png` | `09:20` | SLIDE | *"The BASIC IDEA is that: as you hit Winning Trades you increase your lot size and as you hit losing cycles of 3 or 4 consecutive stop outs you diminish your lot size."* | `[00:09:14]`–`[00:09:23]` |
| 12 | `V09_00-10-15_equity-curve-minus-25-plus-50.png` | `10:15` | DIAGRAM | A green/red equity staircase labelled **`-25 pips S/L`**, **`+50 pip T/P`** | `[00:10:06]`–`[00:10:35]`, the *"eight wins and 11 losses"* example |
| 13 | `V09_00-11-40_equity-curve-minus-15-plus-50.png` | `11:40` | DIAGRAM | A second staircase labelled **`-15 pip S/L`**, **`+50 pip T/P`** | `[00:10:56]`–`[00:11:17]`, the *"seven wins and 12 losses"* example. **The 15-pip stop is the HOD/LOD-skill stop** |
| 14 | `V09_00-14-35_define-risk-two-numbered-rules.png` | `14:35` | SLIDE | *"1. Define Risk by choosing LOT SIZE which is -2% of Balance at Stop Out — Can then be able to withstand THREE CONSECUTIVE LOSSES / No Margin Issues ~ You can come back with SAME LOT SIZE / No Emotional turbulence because you have a PLAN to be able to ABSORB LOSSES. Just wait for NEXT MMFX SIGNAL. 2. Use greater than 1:1 Risk to Reward Ratio. T/P greater than S/L."* | `[00:12:46]`–`[00:14:35]` |
| 15 | `V09_00-16-00_greater-than-fifty-percent-accuracy-upward-equity.png` | `16:00` | SLIDE | *"3. Simply Trading with greater than 50% accuracy will bring UPWARD EQUITY !!!"* and *"Think of what your equity curve will look like when you can hit 70% accuracy ?"* | `[00:15:36]`–`[00:15:59]`. **`A-067`** — 50% is a *sufficient* condition stated where the break-even is far lower |
| 16 | `V09_00-17-05_no-impulsive-increases-in-lot-size.png` | `17:05` | SLIDE | Adds: *"Basic Idea is to keep a consistent RATIO of LOT size as your account grows or falls… AND to consistently Keep Take Profits LARGER then Stop Losses / **No Impulsive Increases in LOT SIZE to make up for a LOSS!!!**"* | `[00:16:11]`–`[00:17:03]` |
| 17 | `V09_00-21-40_five-possible-errors-to-guard-against.png` | `21:40` | SLIDE | The complete list, printed: *"Possible Errors to Guard Against: 1. Moving your Stop Loss After you have placed it: 1st S/L is always the cheapest 2. Putting on Multiple Positions which add up to GREATER than your % Risk 3. Not having the DISCIPLINE to KEEP TO the Risk Plan as described 4. Miscalculating Lot size on NON USD quote Pairs -- use a lot size calculator! 5. Not having HARD Stop Losses and Take Profits WITH THE BROKER"* | `[00:18:31]`–`[00:22:13]` |
| 18 | `V09_00-22-45_eighty-five-percent-win-rate-seven-wins-six-losses.png` | `22:45` | DIAGRAM | An equity staircase captioned *"Example of Equity Curve of **85% Win Rate** with 2:1 Risk Reward Profile"* and, one line below in the presenter's own green/red, *"**7 Wins, 6 Losses**"* | **`C-012`. 7 / 13 = 53.8%, not 85%.** The slide's caption and its own count disagree, and the audio at `[00:22:47]` repeats the caption |
| 19 | `V09_00-25-00_possible-equity-gain-scenario-twenty-percent.png` | `25:00` | SLIDE | *"Possible Equity Gain Scenario: 1. 2% Risk at S/L 2. 2:1 or greater R/R — -25 pip S/L - 2% / +50 pip T/P + 4% 3. Only FIVE successful trades per Week = **20% Gains for the Week!**"* | `[00:24:20]`–`[00:24:57]` |
| 20 | `V09_00-26-00_equity-scenario-with-compounding-spreadsheet.png` | `26:00` | SLIDE | The same slide with a spreadsheet revealed at the right | `[00:26:00]` |
| 21 | `V09_00-26-40_compounding-spreadsheet-full.png` | `26:40` | SLIDE | The spreadsheet, **fully legible**: `Base 5,000.00`, `% profit 0.2000`, then Week 1–4 blocks. Column K: `6,000.00 · 7,200.00 · 8,640.00 · 10,368.00` … running to a red-boxed final row **`Week 4 · 137,370.55 · 824,223.31`** | **`C-013`.** `5,000 × 1.2^4 = 10,368.00` exactly, and the table compounds **20% per week for 28 consecutive weeks with no losing week and no losing trade** — in a lesson whose own worked examples are 6 wins / 14 losses |
| 22 | `V09_00-28-45_live-mt4-eurusd-h1-level-count-and-reset.png` | `28:45` | LIVE | Full-screen MetaTrader. **Title bar, read from the platform's own text: `67352016: FXDD - MetaTrader - Demo Account - [EURUSD,H1]`.** Chart carries hand-drawn horizontal level lines, green/orange/yellow segments, the labels `1`, `2`, `3`, **`Reset`**, a vertical week divider, and a multi-line oscillator sub-panel beneath the price pane | **Broker/platform provenance** — `FXDD`, demo, **H1**. The account number **differs from V05's `67342442`** on the same broker, which is independent non-acoustic evidence of a different presenter |
| 23 | `V09_00-31-50_live-mt4-gbpjpy-h1-level-two-long.png` | `31:50` | LIVE | Same platform, a `GJ`-watermarked H1 chart with a `(3)` label at the left, `Reset`, numbered levels and the same oscillator sub-panel | `[00:31:50]`–`[00:32:04]` |
| 24 | `V09_00-34-35_ms-paint-presenter-email-address.png` | `34:35` | SLIDE | An **MS Paint** window on which the presenter has typed `jimn` and, below it, **`jimnicholson.dmr@hotmail.com`** | **Provenance only** (`D-025` c.4 / `D-033` p.2). Corroborates the spoken `[00:27:30]`. **Nothing in any V09 artifact depends on this** |
| 25 | `V09_00-41-25_multi-chart-tile-view-during-grape-question.png` | `41:25` | LIVE | Nine tiled MT4 charts (`EU`, `GU`, `AU`, `EJ`, `GJ`, `UJ`, `EC`, `GF`, `UC` watermarks) at the moment the audience asks *"What is the grape?"* | `[00:41:25]` → **A-020 / C-010 reconciliation** |
| 26 | `V09_00-52-25_final-frame-bird-photo.png` | `52:25` | SLIDE | Windows Photo Gallery displaying a photograph of a **fledgling bird on the ground** | Corroborates the audio-only reading that the file ends mid-sentence on `[00:52:23]` *"that was the whole idea of this bird right here — I mean he's got wings…"* |

## WHAT THE FRAMES ADDED THAT THE TRANSCRIPT DID NOT

Written **after** `V09_SOURCE_NOTES.md` and `V09_INTERPRETATION.md` were complete from the
transcript alone, per `SWF_CAPTURE_RECIPE.md` §9. The transcript-only sections were **not
rewritten**; every item below is added as a new section there.

1. **`HOD/LOD` — the biggest single gain, and it is a spelling.** The transcript renders the
   phrase as *"high low-day"* throughout (`[00:03:33]`, `[00:04:49]`, `[00:10:56]`), which reads
   as a compound nobody could look up. Frames 5 and 6 print **`HOD/LOD`** — High Of Day / Low Of
   Day, a term the corpus already carries from V08. **This is the V01 *"pendings"* case exactly:
   a word the audio refused to yield, settled by printed text.**
2. **The lot-size formula is printed, not merely spoken** (frame 3), so the corpus's first
   position-sizing rule does not rest on ASR.
3. **`C-012` and `C-013` are both PRINTED contradictions**, not transcription artifacts. A
   reader who doubted the *"85% win rate / 7 wins, 6 losses"* line as a mishearing can see it
   set in the presenter's own slide, and the 28-week compounding table is legible cell by cell.
4. **The broker and platform are legible** (frame 22): `FXDD`, MetaTrader, **demo** account
   `67352016`, `EURUSD,H1`. `D-034`'s text-only measurement rule is satisfied — this is read
   from the platform's own title bar, not inferred from pixels.
5. **The account number is different from V05's**, on the same broker. Recorded as provenance
   corroboration that does no evidentiary work.
6. **The opening frame is V08's closing frame.** The strongest single piece of the cross-file
   continuity finding, and the one that needs no interpretation at all.

## WHAT WAS DELIBERATELY NOT TRANSCRIBED

- **The oscillator sub-panel** visible beneath the price pane on frames 22, 23 and 25 carries a
  header label in the same position as V05 frame 26's `TDI_MMM`. At this resolution it is at the
  edge of legibility and is **not transcribed** — only its presence is recorded. **Displayed,
  not taught**: the presenter never refers to it. This row does **not** narrow `A-039`.
- **The hand-drawn level markings** on frames 22, 23 and 25 are recorded as *present* and their
  labels (`1`, `2`, `3`, `Reset`) transcribed, but **no geometry is measured off them** —
  `D-036a`'s restated `E06` forbids measuring anything off a rendering.
- **The spreadsheet's intermediate rows** on frame 21 are legible but only the first block and
  the red-boxed final row are transcribed above, because those are the two the argument uses.
