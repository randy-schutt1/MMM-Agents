# V06 — SCREENSHOT INDEX

32 curated frames from `Bootcamp1 Wk2 032612 Part1 (75mins).swf` — *"Micro Daily Trends"*.

> ## ⚠ EVERY FRAME IN THIS DIRECTORY IS `GUEST` MATERIAL — `D-025` APPLIES TO ALL OF IT
>
> V06 has **no instructor segment**. A single presenter — not Steve Mauro — speaks the whole
> 01:14:32 (`02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md` § "ONE SPEAKER…"). Under `DECISIONS.md`
> **D-025** every frame below is **SECONDARY, DESCRIPTIVE evidence**:
>
> - Printed text may be cited for **what the frame shows** — that a term exists, how it is
>   spelled, that an object is displayed, what a dialog box contains.
> - Printed text may **NOT** enter `12_MASTER_SPEC/`, `13_MACHINE_SPEC/`,
>   `08_CONCEPT_LIBRARY/` or any machine candidate as **normative** material, may **not** be
>   cited for or against an instructor rule, and may **never close** an `A-xxx` or `C-xxx`
>   record. It may **extend** one.
> - **Most of this deck is squarely normative in content.** Twelve of the 27 slides carry an
>   `Enter` annotation on a chart. Those are flagged inline as `NORMATIVE — EXCLUDED`, and the
>   flag is on the majority of the deck rather than the minority. That is what V06 is.
>
> ### ⚖️ 2026-08-13 — THE FENCE ABOVE IS SUPERSEDED IN PART BY `D-033` (item 60)
>
> `DECISIONS.md` `D-033` makes guest material **NORMATIVE at equal weight**; the exclusions
> above no longer bind and the `NORMATIVE — EXCLUDED` verdicts below are historical. Retained
> unedited because they governed how this index was written. Still binding: speaker tagging
> (provenance) and **`D-030`** — printed *push*/pattern content stays un-operationalisable
> while those terms are undefined. See `V06_INTERPRETATION.md` §9.

> **Process disclosure — evidence order.** `SWF_CAPTURE_RECIPE.md` §9 asks that source notes
> be written from the transcript *before* screenshots are examined. **This session did not
> achieve that separation.** §§7–8 of the same recipe require the curator to look at contact
> sheets before naming any frame, so all 40 detected screen states had been seen by the time
> `V06_SOURCE_NOTES.md` §§1–10 were drafted. What was held to: §§1–10 cite transcript markers
> only and reference no frame; the visual material is confined to §11, added last, and §§1–10
> were not rewritten. **This wording is identical in `V06_SOURCE_NOTES.md` and
> `V06_INTERPRETATION.md` §0 on purpose** (`V05_REVIEW_R1.md` `M4` charged V05 for three files
> disagreeing about V05's own process).

---

## CAPTURE PROVENANCE

| Field | Value |
|---|---|
| Method | Ruffle WASM + Playwright 10× fast sweep (`SWF_CAPTURE_RECIPE.md` §10, `D-021`) |
| Sweep | **903 frames**, one per 5 presentation-seconds, 1024×786, full frame including the control bar |
| Source SHA-256 | `382207b3dc10872e8dac6c308d98dc3c4a1d26e0ba2f639a5836d4e5aac96e86` — matches `SOURCE_MANIFEST.md`, verified on **both** library copies (flat `Bootcamp/` and `Bootcamp Notes/06_…/`) |
| Working copy | `v06_x10.swf` — a **copy**; frame rate patched 3.0 → 30.0 fps, `frameCount` 13,421 unchanged. The original was re-hashed after patching and is unchanged |
| Frames captured by | **This session**, 2026-08-12 |

**`D-022` and GOTCHA 4 were satisfied before capture, not after:**

1. **A fresh port.** `8926`, checked free with `lsof -nP -iTCP:8926 -sTCP:LISTEN` **before**
   starting the server, and confirmed to be this session's own `python3 -m http.server` PID
   after.
2. **The served bytes were diffed against disk.** `curl … | shasum -a 256` against
   `shasum -a 256 serve/v06_x10.swf` — identical. A `200` response was not accepted as
   evidence of anything.
3. **A uniquely named served file.** `v06_x10.swf`, never a reused generic name, so HTTP or
   browser caching cannot hand back another lesson's body.
4. **Content was sanity-checked against the transcript in the first minute.** A 60-second
   probe run was rendered before the long sweep; its burned-in timecode read `10:00 / 74:3…`
   (exactly 10×, and the total matches the manifest's 01:14:33) and the slide on screen was
   *"Push 1"* with an AUDUSD M15 chart — which matches the transcript at `[00:09:58]`
   *"That's your push one."* This is the check GOTCHA 4 says would have caught the V02-era
   port collision in two minutes instead of an hour.

**Every frame proves its own timestamp.** The Camtasia player burns its position into the
bottom-right of the frame and the full 1024×786 frame is kept, control bar included. Before
naming, the timecode strip of all 32 chosen frames was cropped and read: **every one is within
1 second of its filename**, the discrepancy being the player OSD's 1-second granularity. Each
file below is named by **the timecode the player displays in it**, not by the sweep index.

**Screen-state detection.** The 903 frames were pairwise diffed after cropping the control bar
away (so the ticking timecode does not register as a change), threshold mean-abs-difference
> 6.0, runs collapsed within 10 s: **70 raw changes → 40 distinct states**. Those 40 were laid
out on five contact sheets and looked at before any frame was named
(`SWF_CAPTURE_RECIPE.md` §8 — naming from the transcript alone is precisely what produced the
quarantined `VISUAL_INDEX.md` files). 32 were curated.

---

## THE FRAMES

Legend: **Class** is `SLIDE` (prepared deck), `LIVE` (a live application on the presenter's
machine). **Verdict** is this project's disposition of the frame's *content*.

| # | File (timecode + descriptor) | Class | What is on screen | Why it was kept | Verdict |
|---|---|---|---|---|---|
| 1 | `V06_00-00-05_title-slide-micro-daily-trends` | SLIDE | The single line **"Micro Daily Trends"** on a pink field | **Establishes the lesson's title from the recording itself** — the first in the corpus. Falsifies the quarantined `NOTES.md`'s *"Asian Accumulation Boxes…"* topic claim (`Q-006`) | `DESCRIPTIVE` — admissible |
| 2 | `V06_00-00-15_slide-what-do-you-mean-by-micro-daily-trend` | SLIDE | Six bullets: fractal market; macro = 4hr; mini = 1hr; micro = 15min; *"We also call the Micro View of the MM Cycle on the 15min charts Intra Day Pushes"*; *"The MM does not always do 3 pushes each day but when they do and you see your pattern, that is the ONE you should be focused on"* | The spoken timeframe map of `V06_SOURCE_NOTES.md` §2b, in print | `NORMATIVE — EXCLUDED` (the timeframe assignments); the *naming convention* is `DESCRIPTIVE` |
| 3 | `V06_00-02-24_slide-mm-cycle-macro-view-4h` | SLIDE | A 4-hour chart, boxed and labelled `Peak`, `Level 1`, `Level 2`, `Level 3` | The macro view as he draws it; four moving averages visible (red, cyan, white, blue) | `NORMATIVE — EXCLUDED` |
| 4 | `V06_00-03-15_slide-mm-cycle-mini-view-1h` | SLIDE | The same instrument on 1-hour, labelled `Level 1/2/3` and **`RESET`** | First `RESET` label of this lesson. The chart is a **screenshot of MT4 inside the slide**, window chrome included | `NORMATIVE — EXCLUDED` |
| 5 | `V06_00-04-39_slide-mm-cycle-micro-view-day-1-2-3` | SLIDE | 15-minute chart divided into `DAY 1`, `DAY 2`, `DAY 3` with `CHOP`, `BIG W`, `BIG M`, `Enter`, `W`, `Level 1/2/3` | The clearest single picture of what "micro view" means to him, and the only frame that labels days on a 15m chart | `NORMATIVE — EXCLUDED` |
| 6 | `V06_00-05-29_slide-micro-cycle-played-out-intra-day` | SLIDE | **The key text slide.** Six bullets: 3 pushes like 3 levels; *"Each push is approximately ADR divided by 3"*; *"The pullbacks are usually 25 to 50 pips"*; *"You can trade the pushes once you identify the **HOD** or **LOD** and the MM Trend direction"*; *"Each push is easy to identify as they usually Bounce or Trap to a moving average"*; *"Wait for the Rejection of PRICE before entering your trade"* | Prints, almost verbatim, `V06_SOURCE_NOTES.md` §3a–§3c. **`HOD` and `LOD` appear here in print and 0× in the audio** | `NORMATIVE — EXCLUDED`. The **abbreviations** are `DESCRIPTIVE` |
| 7 | `V06_00-09-00_slide-identify-the-pattern-to-setup-the-anchor` | SLIDE | 15m chart, shaded consolidation box, `Enter`, `W`, `RR`, and an `R = ` label whose value was **not transcribed** | The anchor-identification step | `NORMATIVE — EXCLUDED` |
| 8 | `V06_00-09-19_slide-push-1` | SLIDE | Same chart titled `Push 1`, with `Push 1` drawn on it, two `Enter` arrows, `W`, `RR` | Where the count starts | `NORMATIVE — EXCLUDED` |
| 9 | `V06_00-11-55_slide-complete-intra-day-cycle` | SLIDE | The same chart completed: `Push 1`, `Push 2`, `Push 3`, `Peak`, `Pull back`, `False Move`, `Enter`, `W`, `RR` | The full three-push cycle in one image, and the only frame printing **`False Move`** | `NORMATIVE — EXCLUDED` |
| 10 | `V06_00-13-09_slide-more-examples-three-hits-to-the-hi-reset` | SLIDE | 15m chart with `M`, `RR`, **`3 Hits to the Hi`**, **`RESET`**, `SS`, `Enter`, and an `R = ` label whose value was **not transcribed** | *"3 Hits to the Hi"* printed — the same phrase V05's anchor slide prints for the low side (`A-010`) | `NORMATIVE — EXCLUDED`; the printed phrase is `DESCRIPTIVE` |
| 11 | `V06_00-13-49_slide-structure-or-pattern` | SLIDE | The same chart under the title `Structure or Pattern` | He uses "structure" and "pattern" interchangeably, in a slide title — relevant to `A-011` | `DESCRIPTIVE` (terminology) |
| 12 | `V06_00-15-49_slide-push-1-m-rr-reset-markup` | SLIDE | `M`, `RR`, `3 Hits to the Hi`, `RESET`, `SS`, `Enter` ×2, `Push 1`, hand-drawn orange `1` `2` `3`, and **two** `R = ` labels read at 2× this session: **`R = 80.6`** and **`R = 41.5`**. The MT4 legend at top-left reads `AUDUSD,M15 1.05422 1.05431 1.05376 1.05376` | **`SS` first appears here.** Never spoken, never expanded → `A-053` | `NORMATIVE — EXCLUDED`; `SS` is `DESCRIPTIVE` |
| 13 | `V06_00-18-44_slide-pushes-can-also-happen-between-2-days` | SLIDE | Two-day 15m chart, day separator visible, `M`, `W`, `COW`, `Enter`, `Push 1` | The between-days claim, and a printed **`COW`** (`A-036`, `A-045`) | `NORMATIVE — EXCLUDED`; `COW` is `DESCRIPTIVE` |
| 14 | `V06_00-20-20_slide-push-2` | SLIDE | Same chart, `Push 2` added, `Straight Away` annotation | Printed **`Straight Away`** — the term he says he does not trade — *"I don't trade the straightaways"* `[00:54:14]` | `NORMATIVE — EXCLUDED` |
| 15 | `V06_00-21-59_slide-again-find-the-anchor-pattern` | SLIDE | 15m chart, `M`, `RR`, `Enter`, `Push 1`, an `R = ` label (value not transcribed), dashed white line | The restatement that pushes begin at the anchor | `NORMATIVE — EXCLUDED` |
| 16 | `V06_00-23-19_slide-if-they-give-you-an-m-restart-the-clock-2hrs` | SLIDE | Same chart; title states the rule; `M` twice, `RR`, `Push 1`, `Enter` | **The two-hour time stop, in print.** The only place in the corpus a holding-time rule is printed | `NORMATIVE — EXCLUDED` |
| 17 | `V06_00-23-54_slide-finally-push-2` | SLIDE | `Push 1`, `Push 2`, `SS`, `RR`, `M`, three `Enter` arrows | The completed sequence for that example | `NORMATIVE — EXCLUDED` |
| 18 | `V06_00-24-49_slide-another-way-to-see-pushes` | SLIDE | Same chart re-annotated with `Level 3`, `Push 1/2/3`, `SS`, `RR`, `M` | **Levels and pushes labelled on one chart** — the clearest picture of the §2c terminology decision | `NORMATIVE — EXCLUDED` |
| 19 | `V06_00-26-24_slide-more-examples-of-intra-day-pushes` | SLIDE | Wider 15m chart: `BIG W`, `COW`, `RR` ×2, `Push 1`, `Push 2`, `Enter` ×2 and **`R = 67.3`**, read at 2× this session; horizontal orange lines | A second worked example on another instrument | `NORMATIVE — EXCLUDED` |
| 20 | `V06_00-29-09_slide-pushes-can-happen-late-in-the-session` | SLIDE | 15m chart, `M`, `W`, `Push 1`, `Push 2`, `Enter`, **`Stop = 30+ pips`** (read at 2× this session), and an `R = ` label whose value was not transcribed | **The only frame in the corpus printing an explicit stop size**, and it is printed in order to be *rejected* in the audio (`[00:30:41]`–`[00:30:56]`) | `NORMATIVE — EXCLUDED` |
| 21 | `V06_00-31-30_slide-push-1-can-challenge-the-pattern-or-peak` | SLIDE | `COW`, `MS`, `RR`, `Push 1`, `Push 2`, `Enter`, a green ellipse around a three-candle group, **`Stop Hunt`**, `26 pips`, `30 pips`, `48 pips`, `W` | Printed **`Stop Hunt`** and printed **`MS`**; three measured distances on one chart | `NORMATIVE — EXCLUDED`; `MS` is `DESCRIPTIVE` → `A-053` |
| 22 | `V06_00-34-39_slide-sometimes-there-can-be-only-2-pushes` | SLIDE | 15m chart, **`3 Swipes`**, `W`, **`MS`** (read at 2×), `Push 1`, `Enter` ×2, and an `R = ` label whose value was not transcribed | Printed **`3 Swipes`** — V05's slide prints the same phrase for the W (`A-010`/`A-011`) | `NORMATIVE — EXCLUDED` |
| 23 | `V06_00-36-50_slide-pushes-not-clear-when-counter-trend` | SLIDE | `M`, `COW`, `Enter`, `Push 1`, `Push 2` on a chop-heavy chart | **The negative case, given its own slide.** Rare and worth recording: the deck shows its own failure mode | `NORMATIVE — EXCLUDED` |
| 24 | `V06_00-37-59_slide-homework-is-the-authority-jn` | SLIDE | One line: **"Homework is the Authority……… ~JN~"** | The lesson's own homework framing, attributed to *"my buddy Jim Nicholson"* `[00:37:59]`. **`~JN~` printed** | `DESCRIPTIVE` |
| 25 | `V06_00-47-39_live-browser-mmfx-forum-announcement` | LIVE | The *Market Maker's FOREX* forum: masthead **"WHEN THE SIGNALS APPEAR……TRADE WITHOUT FEAR!"**, a post by *"Kar Chen - New Jersey / Administrator"* announcing the *DAILY MARKET REVIEW … MON to THUR* and its cost — *"$102.50 per month ($100.00 plus $2.50 Paypal fee)"* — and *"Steve has given us a wonderful gift…… the Market Makers Method"* | **Documentary evidence of the DMR as a paid programme separate from the bootcamp**, which is what `A-042` is about | `DESCRIPTIVE` |
| 26 | `V06_00-48-29_live-browser-dmr-curriculum-2012` | LIVE | **The DMR Curriculum 2012**, twelve weeks, legible at 4× | **The most consequential frame in the lesson.** See the transcription below | `DESCRIPTIVE` — and see the warning below |
| 27 | `V06_00-52-59_slide-push-2-entry` | SLIDE | `M`, `RR`, `3 Hits to the Hi`, `RESET`, `Push 1`, `Push 2`, `Pull back`, `SS`, `Enter` ×3, an `R = ` label and two small pip annotations, **none of whose values were transcribed at this resolution** | Re-shown during Q&A; two more measured distances | `NORMATIVE — EXCLUDED` |
| 28 | `V06_01-13-10_live-mt4-desktop-folder-and-email-icons` | LIVE | The presenter's Windows desktop: folders `Homework_x`, `DMR Student Charts`, `DMR Vid`, `DMR Stax`, `DMR`, `Patterns Mar 2012`, `80_20 EA`, `80_20 EA1`, `LVOE 80.20 fix`, `Charts for Levels Perpt`, `R&D Perpt`, `Entries Perpt`, `Pushes Perpt`; email shortcuts `David email_3-23`, `Ted email`, `Scott email`, `David email` | **The "save your markups" half of V05's assignment as one man actually keeps it.** Also corroborates the read-out student email of `[00:49:46]` ff. as real correspondence | `DESCRIPTIVE` |
| 29 | `V06_01-13-35_live-mt4-rectangle-dialog-draw-as-background-checked` | LIVE | MT4 `Rectangle` properties dialog: tabs `Common / Parameters / Visualization`, `Name: Rectangle 408`, `Style: Blue`, **`Draw object as background` CHECKED**; behind it a `USDCAD,M15` chart with `Level 3`, `Level 2`, `M`, `RR`, `Push 1`, `Push 2` and two `R = ` labels whose values were not transcribed | **The platform mechanism behind V05's box convention**, shown rather than described | `DESCRIPTIVE` (platform) |
| 30 | `V06_01-13-50_live-mt4-rectangle-dialog-unchecked-solid-box` | LIVE | The same dialog with **`Draw object as background` UNCHECKED**, and a solid blue filled rectangle on the chart at left | The contrast case, in the same 15 seconds. Together, 29 and 30 answer the closing question completely | `DESCRIPTIVE` (platform) |
| 31 | `V06_01-14-09_live-mt4-usdcad-m15-levels-and-pushes` | LIVE | `Demo Account - [USDCAD,M15]` full screen: `Level 3`, `Level 1`, `M`, `RR`, `SS`, `Push 1`, `Push 2`, `Push 3`, `Enter` ×4 and an `R = ` label whose value was not transcribed; chart-tab strip `EURCAD,H1 · EURCAD,M15 · GBPUSD,M15 · GBPJPY,H1 · GBPJPY,M15 · GBPCHF,H1 · GBPCHF,M15 · AUDUSD,H1 · AUDUSD,M15 · AUDJPY,H1 · USDCHF,H1 · USDCHF,M15` | **His live working environment**: H1 + M15 pairs, which is the §2b timeframe claim visible as a workspace rather than asserted | `NORMATIVE — EXCLUDED` (the markup); the **tab strip** is `DESCRIPTIVE` |
| 32 | `V06_01-14-33_end-of-recording-replay` | LIVE | The final frame, dimmed, with Camtasia's `replay` control overlaid; player reads `74:33 / 74:33` | Proves the capture reached the end of the film | `DESCRIPTIVE` |

---

## FRAME 26 — THE DMR CURRICULUM, TRANSCRIBED

Read at 4× magnification from `V06_00-48-29_live-browser-dmr-curriculum-2012.png`. **Only text
this session could read confidently is transcribed; ellipses mark text that is present but not
legible at this capture resolution, and nothing is reconstructed from context.**

> **DMR Curriculum 2012**
>
> **Week 1** – *Patterns & Timing* – Presentation of Confirmed M & W patterns (Intra Day and
> Multi Day/Session pattern) – Students identify these patterns and mark them up on AU and EU
> for 3 months…….Research & Developments. A spreadsheet will be given to track how many
> patterns showed up, the extent of the move, the Timing of the entries and the Win/Loss ratios
> of these patterns. R&D is due the following week………
>
> **Week 2** – Watch for setups of these patterns on the Hard Right Edge in the LIVE market.
> Students can use only AU & EU and can add EJ and UCHF to make it 4 pairs in TOTAL. No trades
> will be taken, only Identify and MARK the entries on the hard right edge. Like doing R&D and
> marking it in the LIVE market. The Spreadsheet will be used to track entries like before.
>
> **Week 3** – Demo Trade the 2 pairs or 4 pairs depending on what the Student is comfortable
> with. Selecting only Confirmed M & W for entries. The spreadsheet will be used to track the
> performance.
>
> **Week 4** – *Patterns & Timing* – … – 2 Pins to the Mayo or Water along with Shooting Star,
> Evening Star, Morning Star and RR Tracks. Mark them off in AU & EU for the same months as
> above……… R&D is due the following week………. Track it like before using the Spreadsheet. Still
> Demo trading the confirmed M & W only.
>
> **Week 5** – Watch for setup of ALL the patterns on the Hard Right Edge in the Live market
> like in Week 2. Identify and MARK the entries only. The Spreadsheet will be used to track
> entries like before. Still Demo trading the confirmed M & W only.
>
> **Week 6** – Demo Trade the 2 or 4 pairs depending on what the student is comfortable with.
> Selecting confirmed M, W, 2 Pins to water or mayo, RR tracks, Shooting Star, Evening Star and
> Morning Star patterns. The spreadsheet will be used to track the performance.
>
> **Week 7** = ***Levels*** – Students will now go back and Mark the LEVELS in AU & EU for the
> same 3 months. R&D is due the following week………. Still Demo Trading all the Patterns learned.
>
> **Week 8** = ***Entry Candles*** – Understanding the Entry candle is very important to
> prevent anticipating the setup. The Entry Candle confirms the PATTERN and validates the trade
> setup.
>
> **Week 9** = ***Hi/Lo Drill*** – Want to catch the HOD or LOD within a few pips. This … when
> the pattern sets up.
>
> **Week 10** = ***Brinks & Safe Trade*** – Two great setups taught by Steve in class. Brinks
> Trade – 2nd Leg of a M or W pattern Falling inside the **Shadow Box** **and more
> specifically at 3:45am or 9:45am est.** Safe Trade – After the Anchor formation, the MM
> induce traders to trade towards the PEAK formation before trapping them and moving away
> from it.
>
> **Week 11** = ***Swing Trade*** – Want to be a Swing trader but using Intraday entries Steve
> taught us. You will learn how to do that during this week. (Guest Presenter)
>
> **Week 12** = ***Counter Trend Trades*** – Got to know when to take a Counter Trend trade
> and know what a high probable setup should look like. (MM Trade both ways why can't you…)
>
> **Week 13** = ***Trade Management & Position Sizing*** – Knowing how to manage the trade
> while its running and knowing proper RISK Management is key to growing your account
> *(partially cut by the frame's bottom edge — the syllabus has at least THIRTEEN weeks, not
> twelve; Week 13's topic matches the presenter's spoken forward curriculum at `[00:49:11]`)*
>
> #### ⚠ RE-TRANSCRIPTION NOTICE — 2026-08-13, R1 remediation (item 57, `V06_REVIEW_R1.md` M1)
>
> Every ellipsis in the original transcription above was re-examined at 2×–4×. **All of the
> elided text was legible**, contrary to the original protocol note ("text that is present but
> not legible"); the completions are now in place above with the superseded readings recorded
> here:
>
> | Week | Originally elided / misread | Actual printed text |
> |---|---|---|
> | 1 | *"(Intra Day and Multi Day/Session pattern)"*; *"Research & Developments"* | *"(Intra Day and Multi Day/Session **Anchor patterns**)"*; *"Research & Development"* (singular) |
> | 4 | *"Patterns & Timing – … – 2 Pins to the Mayo…"* | the elision is ***"Trading the A and V of the MM Trend Cycle"*** |
> | 5 | *"Hard Right Edge"* | the frame prints ***"Hard Ridge Edge"*** [sic] — Week 2 prints *"Hard Right Edge"*; the Week 5 typo is the source's own and is preserved |
> | 9 | *"This … when the pattern sets up"* | *"This **exercise will help you do just that. See how JIM waits for the setup and then enter on the 2nd LEG** when the pattern sets up"* |
> | 10 | *"Shadow Box and …"* / *"trade toward…"* | ***"and more specifically at 3:45am or 9:45am est."*** — the corpus's **first printed `est`** and first printed clock times (→ `A-019`, `A-030`); Safe Trade completed as above |
> | 11–12 | tails elided | completed as above |
> | 13 | not recorded at all | partially visible at the frame's bottom edge — the *"twelve weeks"* description throughout the V06 artifacts undercounts the syllabus |

### What this frame does and does not do

| It does | It does not |
|---|---|
| Give the corpus its **first printed occurrence of "Mayo"** as a moving-average nickname, in two separate weeks, which settles the ASR's *"mail"* / *"male"* as a **spelling** question (`A-020`) | **Attach a period to "Mayo" or to "Water".** `A-020`'s actual question — which average is which — is untouched, and stays `DO NOT CODE` |
| Give the corpus its **first printed occurrence of "Shadow Box"**, attached to the Brinks trade and to a *2nd leg of an M or W falling inside it* (`A-030`) | **Define the Shadow Box.** Nor may a guest programme's syllabus close a record about the instructor's term |
| Show that the DMR is a **structured 12-week programme with named topics**, several of which the bootcamp defers to it (`A-042`) | **Supply any of that content.** A syllabus is a table of contents. `A-042` is *extended and sharpened* — the corpus now knows exactly which twelve topics it does not contain |
| Corroborate that `Entry Candles`, `Levels`, `Hi/Lo`, `Brinks`, `Safe Trade`, `Swing`, `Counter Trend` are real course topics — the same list the presenter reads aloud at `[00:48:28]`–`[00:49:19]` | **Tell us which recorded lesson covers which.** The library's V07–V21 ordering is `SOURCE_MANIFEST.md`'s, and no mapping to this syllabus is claimed |

> ### ⚠ A NOTE ON READING THIS FRAME AT ALL
>
> The DMR curriculum is **the most rule-dense printed artifact yet found in the corpus**, and it
> is **a guest programme's syllabus**. It is also, uniquely, a document that tells students what
> to trade and when (*"Selecting only Confirmed M & W for entries"*, *"No trades will be taken"*,
> *"2 pairs or 4 pairs"*). **Those are `NORMATIVE` lines inside a frame classed `DESCRIPTIVE`,
> and the class applies per-claim, not per-frame.** Cite this frame for *"the DMR's week 4 names
> these patterns"*; never for *"the method requires these patterns"*.

---

## WHAT THE FRAMES ADDED, AND WHAT THEY DID NOT

Recorded in full at `V06_SOURCE_NOTES.md` §11. In summary:

**Resolved:** the lesson's title; the *"Mayo"* spelling; the printed form of the timeframe map.

**Added:** `HOD` / `LOD` in print (0× in audio); the printed chart vocabulary
(`M`, `W`, `RR`, `SS`, `MS`, `COW`, `RESET`, `3 Hits to the Hi`, `3 Swipes`, `Straight Away`,
`False Move`, `Stop Hunt`, `Enter`, `Push 1/2/3`, `Level 1/2/3`, `BIG W`, `BIG M`, `Pull back`);
further `R = ` labels on at least nine frames, two of them transcribed (`A-018`); `Shadow Box` in print (`A-030`); the DMR curriculum
(`A-042`); the MT4 rectangle mechanism; the presenter's own file organisation.

**Not settled:** no moving-average **period** is attached to any nickname anywhere, in audio or
in print (`A-020` stays open); no **session-boundary** clock appears on any of the 32 frames —
but frame 26 **does** print clock times with a timezone (*"3:45am or 9:45am est."*, the Brinks
trade's fire times; `A-019` **extended**, not untouched — corrected 2026-08-13, item 57;
superseded wording: *"no session clock appears on any of the 32 frames (A-019 untouched, sixth
consecutive lesson)"*); `SS` and `MS` are never expanded (`A-053`); the DMR's *content* remains
outside the corpus (`A-042` stays open); and **no frame shows the instructor** — every chart in
this lesson is the presenter's own.

### R-LABEL LEDGER — 2026-08-13, R1 remediation sweep (items 57, and `V06_REVIEW_R2.md` M5)

Every `R = ` label on the curated frames, re-read at 2×. This ledger **supersedes** the
per-row phrases *"value not transcribed"* above (rows 7, 10, 15, 20, 22, 27, 29, 31), which
are retained in place as the original record:

| Frame | Value(s) |
|---|---|
| `V06_00-09-00` / `V06_00-09-19` | `R = 31.1` (same AUDUSD markup) |
| `V06_00-13-09` / `V06_00-15-49` | `R = 41.5`; `V06_00-15-49` also `R = 80.6` |
| `V06_00-21-59` | `R = 24.3` |
| `V06_00-26-24` | `R = 67.3` |
| `V06_00-29-09` | `R = 44.4` |
| `V06_00-34-39` | `R = 82.7` (beside the printed `3 Swipes`) |
| `V06_00-52-59` | `R = 80.6` (the AUDUSD chart re-shown; also a printed `51 pips`, matching `[00:16:38]`) |
| `V06_01-13-35` | `R = 24.3`, `R = 28.9` |
| `V06_01-14-09` | `R = 24.3` |

The corrected value set (24.3, 28.9, 31.1, 41.5, 44.4, 67.3, 80.6, 82.7) remains not a
multiple of any stated stop or target — `A-018`'s negative result survives the correction.
