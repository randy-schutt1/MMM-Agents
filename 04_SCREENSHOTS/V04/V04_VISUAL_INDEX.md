# V04 — VISUAL INDEX

27 curated frames from a 1,037-frame sweep of
`Bootcamp1 Wk2 032512 Part2 (86mins).swf`
(SHA-256 `10d8fe7e…fe60fb7c`, duration 01:25:41).

## HOW THESE WERE CAPTURED

Method: `00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10, the **10× fast sweep** (D-021). A working
copy of the SWF was patched from its declared 3.0 fps to 30.0 fps; the original was
SHA-256-verified unchanged afterwards. Ruffle 0.5.0 WASM in headless Chrome via
Playwright, one screenshot every 500 ms of wall clock = every **5 presentation-seconds**,
1,037 frames covering 00:00:00 → 01:26:20. Wall clock ≈ 8.6 minutes.

**Port and byte verification (D-022) was performed and it mattered.** Three stale
`http.server` processes from earlier sessions were found holding ports **8899, 8917 and
8931** — exactly the GOTCHA 4 hazard that cost a previous session a 61-minute capture. A
fresh port (**8944**) was taken, confirmed to be owned by this session's own PID, and the
bytes served for `v04_x10.swf` were SHA-256-matched against the file on disk before any
capture ran.

**Content was sanity-checked against the transcript inside the first minute of work**, as
the recipe requires. The probe frame at burned timecode `05:00` carries a hand-drawn
**"-180"** annotation; the transcript at `[00:04:52]` reads *"Don't stand aside minus one
eighty."* Right film, right clock.

## HOW TO READ A FILENAME

`V04_HH-MM-SS_descriptor.png` — the timestamp is **presentation time**, and every frame
retains the full 1024×786 stage **including the player's control bar**, whose burned-in
timecode lets each image prove its own timestamp independently of its filename. Descriptors
say **what is shown**, not what it means.

Every frame below was **looked at before it was named.** Two names were corrected during
that pass rather than after it:

- `01-08-40` was first drafted as `gj-trade-example` from the transcript's nearby *"This is
  GJ"*. The frame's own title bar and OHLC legend read **AUDCAD,M15**. Renamed; the real
  GBPJPY frame is `01-04-10`, confirmed from its title bar.
- The archived pre-ingestion `VIDEO_05_SCREENSHOT_001_00-02-00.jpg` was matched against
  this sweep and is the frame at **`[00:00:00]`**, not `[00:02:00]` (Q-004 Finding 4).

## THE INDEX

| # | File (`V04_…`) | Pres. time | What is visible | Transcript anchor |
|---:|---|---|---|---|
| 1 | `00-00-00_four-trades-slide-powerpoint-edit-view` | 00:00:00 | PowerPoint **editing** view — ribbon, slide panel, "Click to add notes"; deck titled "1. Market Maker Method 1_2012". Slide reads **"4-Trades / Stop Hunt High "M" Formation / Stop Hunt Low "W" Formation / Straight Away Rise / Straight Away Drop"** | `[00:00:37]` *"stop-on-high, the M-o-form, stop-on-low W-form"* |
| 2 | `00-01-20_four-trades-slide-full-screen` | 00:01:20 | Same slide, full-screen slideshow mode | — |
| 3 | `00-04-40_flashcard-chart-blue-box-r27` | 00:04:40 | 15-minute candle chart: pale-blue horizontal box on the left, grey/white vertical bands, five coloured lines, label **"R = 27.0"** | `[00:08:09]` *"27 pips"*; `[00:11:25]` *"27 pips range"* |
| 4 | `00-05-20_chart-annotated-minus-180` | 00:05:20 | Same chart, hand-drawn **"-180"** circled top-right, drawn M and a down arrow | `[00:04:52]` *"Don't stand aside minus one eighty"* |
| 5 | `00-06-00_chart-m-drawn-with-minus-23` | 00:06:00 | Adds a second hand-drawn **"-23"** to the left and a long swing outline | `[00:05:53]`–`[00:05:59]` |
| 6 | `00-08-40_chart-second-leg-m-over-high` | 00:08:40 | Heavy M drawn over the high, vertical line dropped from it | `[00:08:38]` *"The dealer makes the M formation"* |
| 7 | `00-12-00_chart-asian-range-halved-annotation` | 00:12:00 | Bracket drawn inside the pale-blue box with a written figure beside it | `[00:11:48]`–`[00:12:14]` the 27 ÷ 2 ≈ 13.5 argument |
| 8 | `00-13-20_chart-stop-hunt-zone-marked` | 00:13:20 | Marks over the grey band above the box | `[00:12:53]`–`[00:13:03]` *"stop on Zone, Gray Box… Timing Shadow Box"* |
| 9 | `00-14-40_chart-hod-written-above-box` | 00:14:40 | **"HOD"** hand-written above the formation | `[00:08:42]` *"failure to break the high of the day"* |
| 10 | `00-19-20_chart-four-hour-fifteen-note` | 00:19:20 | Hand-written **"4:1 15"** at upper left | `[00:19:17]`–`[00:19:23]` four-hour vs 15-minute |
| 11 | `00-20-00_chart-how-hod-written` | 00:20:00 | **"HOW | HOD"** hand-written at upper left | `[00:19:34]`–`[00:19:47]` *"the HOW and the HOD are coordinated by the dealer"* |
| 12 | `00-24-00_chart-full-accumulated-markup` | 00:24:00 | The fully accumulated markup at the end of the instructor's segment | — |
| 13 | `00-27-20_mmfx-title-card` | 00:27:20 | **MMFx title card** — "When The Signals Appear……Trade Without Fear! / www.marketmakersforex.com" | **Speaker handover.** Instructor ends `[00:26:56]`; guest begins `[00:26:59]` |
| 14 | `00-30-00_guest-twelve-pair-check-down-screens` | 00:30:00 | Guest's MT4-style layout: hourly above 15-minute panes across a wide desktop | `[00:31:23]`–`[00:31:26]` *"hourly on top… 15 minutes on the bottom"* |
| 15 | `00-33-20_check-down-worksheet-twelve-pairs` | 00:33:20 | Blank worksheet, columns **Pair / Level - Direction / Confluence**, listing exactly **12 pairs**: AUDCHF, EURAUD, EURCHF, AUDJPY, EURJPY, GBPJPY, EURGBP, EURUSD, GBPUSD, AUDUSD, USDCHF, USDJPY | `[00:30:22]` *"I paired it down… to just 12 pairs"* |
| 16 | `00-34-00_pre-trade-question-checklist-slide` | 00:34:00 | **The guest's pre-trade checklist, fully legible** — see the transcription below | `[00:33:53]`–`[00:37:15]`, which walks it line by line |
| 17 | `00-40-40_trade-screen-checklist-tdi-adr` | 00:40:40 | Blank per-pair form: **TDI / Shark Fin / Stop / MM Candles / Divergence / Pivot / ADR / HOD LOD (Yesterday's)**, four copies | `[00:40:12]`–`[00:40:20]` |
| 17b | `00-41-05_the-set-ups-title-slide` | 00:41:05 | Title slide reading **"The Set-Ups"** — the divider between the guest's method walkthrough and his ~20 worked trade examples | `[00:40:58]` *"what I thought would be best, is just try to teach you some of the setups that I look for"* |
| 18 | `00-41-20_guest-trade-example-boxes` | 00:41:20 | First worked trade: red and pale-blue session boxes over 15-minute candles, oscillator sub-panel | `[00:41:11]` *"a trade that I took on Friday"* |
| 19 | `00-50-00_annotation-entered-after-fourth-retest-mayo` | 00:50:00 | Printed chart caption: **"Entered here after 4th retest Mayo"** | `[00:49:46]`–`[00:49:56]` *"four times it came up against the mail"* |
| 20 | `00-55-20_guest-chart-green-red-boxes` | 00:55:20 | Platform window, green and red session boxes, watchlist at left | `[00:54:51]` *"we're coming out of the box here"* |
| 21 | `01-04-10_gbpjpy-m15-platform-window` | 01:04:10 | Full trading platform, title bar **"MIG Bank Trading Station - Prime - [GBPJPY,M15]"**; watchlist of ~20 symbols; Navigator with a Scripts tree (`$$CloseAll`, `$Change_StopLosses_To_BreakEven`, `$Close_All_Orders_For_Symbol`, `$Delete_Pending_Orders`, `$Go_Long_With_Backup`, …); box labels **R = 33.2 / 58.4 / 15.5** | `[01:03:46]` *"This is GJ"*; `[00:53:36]` *"Yes, I do use the scripts that Steve provided"* |
| 22 | `01-08-40_audcad-m15-r-labels-adr-panel` | 01:08:40 | **AUDCAD,M15.** Legend prints OHLC `1.03286 1.03299 1.03199 1.03220`, `High: 1.0403`, `Low: 1.0285`, `Previous Days Range: 118.3`, `Current Days Range: 12.9`. Top-right panel prints **HOD / LOD / TDR / YDR / WADR / MADR / %DADR** with values. Box labels **R = 52.4 / 65.9 / 54.6**. Order row dated **2011.11.17** | `[01:08:35]` *"This was a November trade"*; the ADR discussion `[01:05:36]`–`[01:06:09]` |
| 23 | `01-12-00_annotation-hit-limit-entered-at-lod` | 01:12:00 | Printed captions **"Hit Limit here"** and **"Entered here at LOD"**; box label **R = 95.2** | `[01:11:41]`–`[01:12:30]` the "kindergarten M" entry walkthrough |
| 24 | `01-19-20_guest-platform-full-window` | 01:19:20 | Full platform window with watchlist and Navigator, one 15-minute chart | `[01:19:12]` *"This tree, this is from November"* |
| 25 | `01-20-40_chart-magenta-level-example` | 01:20:40 | Chart with a prominent horizontal **magenta** line across it, two red boxes | `[01:20:13]` *"last chart here"* |
| 26 | `01-25-20_final-chart-example` | 01:25:20 | Final chart still on screen as the session ends | `[01:25:37]` last genuine line |

## THE TWO SLIDES WORTH TRANSCRIBING IN FULL

These are the lesson's only two pieces of **printed, unambiguous, non-handwritten rule
text**, and both belong to the **guest presenter**, not the instructor (see
`02_TRANSCRIPTS/V04/V04_TRANSCRIPT.md` § TWO SPEAKERS).

### `00-34-00` — the pre-trade question checklist

```text
Where are we at in the Cycle?
Has there been 3 levels of rise or correction?
What are the anticipated moves for this week?
Are we at or near the mid week Reversal?

Who has behaved in the London Session?

3 Swipes / False Move / Trap
Was there a long sustained move?
Was ADR met?
What confluences are present to justify entry?

IF they haven't followed the rules ..

DON'T PLAY WITH THEM!
```

### `00-40-40` — the per-pair trade-screen form

```text
TDI:
Shark Fin:
Stop:
MM Candles:
Divergence:
Pivot:
ADR
HOD LOD (Yesterday's)
```

## WHAT THE VISUALS ADDED THAT THE AUDIO DID NOT

Recorded here because the project deliberately writes notes from the transcript **before**
looking at frames, so that this delta stays visible (`SWF_CAPTURE_RECIPE.md` §9).

1. **"Mayo" printed a second time, by a different presenter.** Frame 19 prints *"Entered
   here after 4th retest **Mayo**"* on the guest's own chart. The ASR renders this word as
   *"the mail"* throughout V04, *"mayonnaise"* in V02, *"manays"/"minis"* in V03.

   **This is corroboration, not a first — and the claim is scoped accordingly.**
   `V03_INTERPRETATION.md` I5 already recorded a printed *"mayo"* on V03's criteria slide
   (*"3 vectors passed mayo"*), so the **spelling was already settled before V04**. What
   V04 adds is genuinely narrower and still worth having: a **second, independent** printed
   instance, in a **different presenter's** hand, on a **different platform**, used as a
   **price destination that price retests** rather than as a slide caption. That
   strengthens "mayo is a real, shared course term for a chart line" and weakens any
   reading of V03's slide as a one-off typo.

   **It does not resolve `A-020`.** No frame and no line in V04 states which moving average
   "Mayo" is. `A-020`'s actual open question — the period — is untouched. The record is
   extended with this evidence, not closed.
2. **The guest presenter is identifiable.** Frame 21's Navigator lists live accounts titled
   **"Zen Jason … Alldredge"** and **"Zen Jason … or Diana I. Alldredge"**. With the audio's
   *"my wife"* `[00:27:35]` and *"Diana's here with me now"* `[00:56:06]`, this identifies
   the otherwise-unnamed second presenter as **Jason Alldredge**. Recorded as a
   **VISUAL, high-confidence identification, not a caption** — it is an account title in his
   platform, not an on-screen introduction, and no line of the transcript names him.
   *(Account numbers are visible in the frame and are deliberately not transcribed here.)*
3. **The 12-pair claim is corroborated exactly.** Frame 15 lists twelve pairs; the audio says
   *"just 12 pairs"* `[00:30:22]` without enumerating them.
4. **"R = " box labels are everywhere and are never explained aloud — and V04 supplies the
   first spoken cross-check for them.** Frames 3, 21, 22 and 23 carry
   `R = 27.0 / 33.2 / 52.4 / 54.6 / 58.4 / 65.9 / 95.2`. Neither presenter ever says what
   `R` is.

   The useful part is frame 3: it is labelled **`R = 27.0`**, and on that same chart the
   instructor says *"What's the Asian range? 27 pips"* `[00:08:09]` and *"27 pips range"*
   `[00:11:25]`. **A printed `R` value and a spoken pip-range for the same box agree to
   0.0.** That is independent support for `A-018` candidate 1 (`R` = the boxed range in
   pips) and against candidate 2 (risk-multiple), from a lesson that states a stop and a
   target and *still* does not make the numbers work as an R-multiple (a 27.0 R-multiple
   on a 10–18 pip stop is absurd).

   **This is the second agreeing pair, and the first where one side is spoken.** V03
   already supplied a printed-vs-printed pairing (`R = 41.4` beside the criteria text
   *"Asian Range =41"*, recorded in the V03 evidence block of
   `AUTOMATION_AMBIGUITIES.md`). V04 adds a printed-vs-*spoken* one, on a different chart
   in a different lesson.

   `A-018` is **extended, not resolved** — two agreeing pairs are not a definition, and no
   presenter ever states one.
5. **The handover has a visual marker.** Frame 13's MMFx title card sits between the
   instructor's last line and the guest's first, corroborating a speaker boundary that the
   transcript itself does not label.
6. **Printed ADR vocabulary.** Frame 22's panel prints `TDR / YDR / WADR / MADR / %DADR`
   alongside `HOD / LOD` — a family of range measures the audio only gestures at
   (*"how do I determine the ADR… a lot of these indicators they'll tell you"*
   `[01:07:01]`–`[01:07:14]`). Carried as **`A-040`**.

## WHAT IS NOT CLAIMED

- **No price was read off any chart by pixel colour**, and no price level in any downstream
  artifact is derived from these images. Where a number is quoted above it is **printed
  text in the platform's own legend or panel**, read as text (V02's `E06`/`E19` lesson, and
  the standing instruction for V04).
- The `R =` values are transcribed as printed. **What `R` denotes is not claimed** (`A-018`).
- Session-box colours (red / pale-blue / grey / white) are described as seen. **No mapping
  from a colour to a named session is claimed** — V04 never states one.
- Frames 18, 20, 24, 25, 26 are worked examples whose **pair and date are not legible** at
  this resolution; they are indexed as examples only and nothing is derived from them.
