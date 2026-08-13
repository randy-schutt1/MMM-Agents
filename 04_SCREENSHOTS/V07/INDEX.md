# V07 — SCREENSHOT INDEX

24 curated frames from `Bootcamp1 Wk2 032612 Part2 (48mins).swf` — **"Best Trade Grabs"**.

> ## EVERY FRAME IN THIS DIRECTORY IS `GUEST` MATERIAL — AND UNDER `D-033` THAT DOES NOT DEMOTE IT
>
> V07 has **no course-author segment**. A single presenter — not Steve Mauro — speaks the whole
> 00:48:05 (`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` § "ONE SPEAKER…"). Under `DECISIONS.md`
> **D-033** (2026-08-13, owner direction, *"all knowledge is created equal"*) this material is
> **NORMATIVE evidence at equal weight** with the course author's. It may define rules, enter
> the spec directories, close an `A-xxx` or `C-xxx` record, and be cited for or against any
> other statement in the corpus.
>
> **Two things `D-033` explicitly does not change, and both bite here:**
>
> 1. **Speaker tagging stays mandatory** (`D-033` provision 1). Every citation of a frame below
>    carries the tag `GUEST`, because two speakers can now both create doctrine and a future
>    conflict between them has to be attributable.
> 2. **`D-030` still binds.** A printed phrase that depends on a term the course has named and
>    never defined — *second leg* (`A-007`), *level* (`A-004`), *M/W* (`A-011`), *shark fin*
>    (`A-032`), TDI (`A-039`) — **remains un-operationalisable no matter who printed it.**
>    Frames `00-18-25` and `00-19-15` are the sharpest cases: they carry complete, printed,
>    executable-looking entry and exit instructions built entirely out of undefined terms. They
>    are recorded in full and **may not be coded**.

> **Process disclosure — evidence order.** `SWF_CAPTURE_RECIPE.md` §9 asks that source notes be
> written from the transcript *before* screenshots are examined. **This session did not achieve
> that separation.** §§7–8 of the same recipe require the curator to look at contact sheets
> before naming any frame, so all 31 detected screen states had been seen by the time
> `V07_SOURCE_NOTES.md` §§1–10 were drafted. What was held to: §§1–10 cite transcript markers
> only and reference no frame; the visual material is confined to §11, added last, and §§1–10
> were not rewritten. **This wording is identical in `V07_SOURCE_NOTES.md` §0 and
> `V07_INTERPRETATION.md` §0 on purpose** (`V05_REVIEW_R1.md` `M4` charged V05 for three files
> disagreeing about V05's own process).

---

## CAPTURE PROVENANCE

| Field | Value |
|---|---|
| Method | Ruffle WASM + Playwright 10× fast sweep (`SWF_CAPTURE_RECIPE.md` §10, `D-021`) |
| Sweep | **588 frames**, one per 5 presentation-seconds, 1024×786, full frame including the control bar |
| Source SHA-256 | `cb6a8520c55f7c15f0c0d527026ea021c6d7172800c4269c4f4afa255ea72d34` — matches `SOURCE_MANIFEST.md`, verified on **both** library copies (flat `Bootcamp/` and `Bootcamp Notes/07_…/`) |
| Working copy | `v07_x10_9631.swf` — a **copy**; frame rate patched 3.0 → 30.0 fps, `frameCount` 8,661 unchanged. The original was re-hashed after patching and is unchanged |
| Frames captured by | **This session**, 2026-08-13 |

**`D-022` and GOTCHA 4 were satisfied before capture, not after — and the hazard was live:**

1. **A fresh port.** `8963`, checked free with `lsof -nP -iTCP:8963 -sTCP:LISTEN` **before**
   starting the server, and confirmed to be this session's own `python3 -m http.server` PID
   (52628) after. **At the moment of that check, five other sessions' servers were listening on
   this machine — 8899, 8917, 8926, 8931, 8945.** `D-022` is not a historical precaution here;
   the exact collision it describes was one port-number reflex away.
2. **The served bytes were diffed against disk.** `curl … | shasum -a 256` against
   `shasum -a 256 serve/v07_x10_9631.swf` — identical. A `200` response was not accepted as
   evidence of anything.
3. **A uniquely named served file.** `v07_x10_9631.swf`, never a reused generic name, so HTTP or
   browser caching cannot hand back another lesson's body.
4. **Content was sanity-checked against the transcript inside the first look, not after the
   run.** Frame `s_0306` (25:30) shows a chart with a brown ADR line and a moving-average legend
   discussion in progress; `[00:25:21]`–`[00:25:44]` is the presenter answering Martha about
   exactly that brown line and *"this yellow one is a five moving average"*. The right film was
   confirmed before any frame was named.

**Timecode self-proof.** Every frame retains the player's burned-in timecode in the bottom-right
of the control bar, so each screenshot proves its own timestamp. Spot-checked: frame index 306 ×
5 s = 1530 s = **25:30**, and the burned-in clock reads `25:30 / 48:0…`. The filename timestamps
below are the sweep grid, which is the same number.

---

## ⚠ TWO LAYERS ARE VISIBLE IN EVERY SLIDE FRAME — READ BEFORE CITING ANY FRAME

**Every slide in this deck renders semi-transparent over a persistent MT4 chart**, and that chart
is visible through the slide text in all thirteen slide frames below. The underlying screen is
the same one throughout:

> `EURJPYm,M15  101.100 101.200 101.059 101.188` · `MIG Trading Station, © 2001-2011 MetaQuotes
> Software Corp.` · x-axis `13 Dec 2011` → `15 Dec 06:30` · boxes labelled `R = 17.4` and
> `R = 16.4` · right panel `Spread 3.2 / High 101.989 / Low 101.026 / Net Chg -56 / Pips To HOD
> 41.1 / Pips To LOD 15.4 / Candle Time 0:02 / Trade 1 Pips -3.1 / Trade 2 Pips -3.1`

**Whether that is how the original recording looked, or an artifact of this renderer's delta-tile
compositing, is NOT determined by this session and is not claimed either way.** The operative
rule is the same under both readings, and it is the rule this index follows:

> **Chart detail seen behind a slide belongs to a screen that is not that slide's subject, and
> is never cited as the slide's content.** The `R = 17.4` / `R = 16.4` boxes, the `101.188`
> quote and the December 2011 dates appear behind roughly half the frames in this directory and
> are **evidence about one background screen, not about thirteen different slides.**

**Two chart frames are partial repaints and keep the background's outer strips.** This is
measured, not assumed: each curated frame was compared pixel-for-pixel against a reference slide
frame (`s_0048`), and rows matching within 3/255 across >90% of their width were recorded.

| Frame | % identical to the reference slide frame | Stale row bands | Consequence |
|---|---|---|---|
| `00-17-35` | **27.8%** | rows 7–70 and 664–759 | The `EURJPYm,M15 101.100 101.200 101.059 101.188` header **in the top strip is the background's** and is 21 pips away from this chart's own quote. The frame's own header is the inner one at rows ≈105–150, reading `110.099 110.119 109.719 109.811` |
| `00-25-30` | **27.9%** | rows 7–70 and 664–759 | Same. **The symbol and quote for this frame were read from the inner header, not the top strip** |
| all 22 others | 2.4% – 5.3% | none ≥ 4 rows | No stale outer strip |

**Nothing in this index or in `V07_SOURCE_NOTES.md` §11 is read from a stale band or from a
background layer.** The two affected frames are named `…partial-repaint-over-slide-background`
and `…revisited…` precisely so a later reader cannot mistake the strip for the frame's own
content.

> **Both readings of the two headers were checked before either was used.** The stale strip and
> the live header on frames `00-17-35` / `00-25-30` **both say `EURJPY`**, so the symbol would
> have been right either way — and that is exactly why the check was run rather than skipped.
> The quotes differ by 21 pips, and a session that had taken the strip at face value would have
> published the wrong price band for the frame while being right about the instrument.

> **Why this is written up at length.** V06 R1 finding `M1` (`E07`+`E11`, `MAJOR`) was a frame
> whose printed text was wrongly called illegible, and the absence was then asserted as a fact
> about the corpus. This is the mirror-image hazard: text that is perfectly legible and belongs
> to a **different screen**. Both produce a confident false claim from a real pixel.

### Legibility, stated per frame rather than in a blanket sentence

The MT4 symbol/OHLC title bar is 5 px tall in the source and survives the delta-tile compression
unevenly. Each was inspected at up to 10× magnification (LANCZOS and NEAREST) before any call was
made:

| Frame | Symbol label | Call |
|---|---|---|
| `00-13-55`, `00-17-35`, `00-25-30` | `EURJPYm,M15  110.099 110.119 109.719 109.811` | **LEGIBLE** |
| `00-16-20` | `EURUSDm,M15  1.31744 1.31744 1.31507 1.31651` | **LEGIBLE** |
| `00-27-00` | `EURUSDm,M15  1.32623 1.32667 1.32612 1.32663` | **LEGIBLE** |
| `00-19-15`, `00-24-05` | `AUDUSDm,M15  1.0?9?? 1.07141 1.06968 1.06968` | **LEGIBLE for the symbol**; the open field is not |
| `00-00-50`, `00-02-30` | — | **NOT LEGIBLE.** Glyphs are smeared past recovery at 10×. **No symbol is claimed for these two frames, and their filenames name only what is visible** |
| `00-18-25` | — | **OBSCURED, not illegible** — the ADR readout box is drawn over the title bar. The visible quote band is 1.43457–1.44522 and the ADR box gives `T's High= 1.44522` |

---

## THE FRAMES

Structure of the lesson, established from the frames: a **PowerPoint deck runs `[00:00:00]` –
`[00:21:35]`**, with the presenter switching to **live MT4 charts** for the trade-graph review
from about `[00:13:34]` and for the whole Q&A. From **`[00:34:50]` to the end the "Final
Synopsis" slide simply stands on screen** while the presenter answers questions — which is why
the last 13 minutes contain no new visual evidence and are represented by one frame.

| # | Frame | Time | What is shown | What it adds | Class |
|---|---|---|---|---|---|
| 1 | `title-slide-best-trade-grabs` | 00:00:10 | Deck title: **"Best Trade Grabs"** / **"MMFx Breakout Session 03-26-2012"** | **Establishes the lesson title and the session date from inside the recording.** The first lesson in this corpus whose date is *printed*, not inferred from a filename. Also settles the ASR's *"best trade graphs / grab / grade"* — the word is **"Grabs"** | `PRINTED` |
| 2 | `slide-do-they-tell-the-whole-story` | 00:00:35 | *"Those charts have good trade entries. But do they tell the whole story?"* | The lesson's framing question, printed | `PRINTED` |
| 3 | `two-pane-chart-intraday-left-higher-timeframe-right` | 00:00:50 | Two chart panes side by side; left x-axis spans hours (6–9 Jan 2012), right spans weeks (20 Dec 2011 – 9 Jan 2012). TDI sub-panel under each | Shows the same two-pane layout the presenter names at `[00:02:25]` — *"On the left-hand side will be the 15 minute, right-hand side will be the one hour"*. **The frame does not print either timeframe**, so it corroborates the layout, not the periods. **Symbol not legible — no instrument is claimed** | `VISUAL` |
| 4 | `two-pane-chart-with-four-r-labelled-boxes` | 00:02:30 | Two-pane chart; shaded boxes labelled `R = 17.4` and `R = 16.4` | Fourth lesson running in which shaded boxes carry printed `R = <number>` labels — see `A-029`. **Symbol not legible** | `VISUAL` |
| 5 | `slide-what-makes-up-the-best-trade-grabs-title` | 00:03:30 | Section title, no bullets yet | Marks the transition from the graph gallery to the argument | `PRINTED` |
| 6 | `slide-what-makes-up-the-best-trade-grabs-bullets` | 00:04:00 | *"Setups – What level am I at? / – Gotta get that M or W! / – Straightaways or bust! / Entries – It's all about the pattern! / – If I know the pattern do I need levels?"* | **Settles the ASR garble at `[00:03:40]`** (*"MLW"* / re-transcription *"MOW"*) as **"M or W"**. Prints *"Straightaways"* — the object V05's *"straightaway"* named | `PRINTED` |
| 7 | `slide-personal-opinion-homework-struck-through-rd` | 00:04:55 | A paragraph slide ending *"I can do something else like Um.. ~~Homework~~.. I mean R&D."*, with **"Homework" struck through in red** | **The rename is printed, not just spoken.** `[00:05:14]` *"I won't even use the H word anymore"* and `[00:11:59]` *"R&D, what form they were known as homework"* now have a printed anchor. Also prints *"signature trade/setup"* as one object | `PRINTED` |
| 8 | `slide-setups-do-they-matter-levels-signature` | 00:06:00 | *"Setups • Do they matter? • Levels: Do they help? • Do I need a signature trade/setup?"* | The three setup questions, printed | `PRINTED` |
| 9 | `slide-entries-pattern-rules-hi-lo-drawdown` | 00:08:00 | *"Entries • The Pattern Rules! – Confirmed or not confirmed • **Hi-Lo** – Can this be all I need? • But What About The Drawdown – Does it really matter?"* | **First printed spelling of "Hi-Lo"** — the method the audio renders *"high low"* and defers to Jim three times. Also prints the **confirmed / not-confirmed** binary on patterns | `PRINTED` |
| 10 | `slide-exits-total-pips` | 00:09:00 | *"Exits • Total Pips. – Isn't That All That Matters?"* | The exit question, printed | `PRINTED` |
| 11 | `slide-money-management-those-pesky-stoplosses` | 00:10:00 | *"Money Management • Those pesky stoplosses. • Is it really important?"* | The fourth of the four factors, printed | `PRINTED` |
| 12 | `slide-requirement-patience-practice-rd` | 00:12:00 | *"What Is The Requirement For Good Trade Grabs? • Patience (Wait for the market to come to us) • Practice • R&D"* | The requirement list building, three of four items | `PRINTED` |
| 13 | `slide-requirement-plus-flashcards-screenshots` | 00:13:00 | Same slide, fourth bullet added: **"Flashcards (Screenshots)"** | **Defines the flashcard artifact as a screenshot**, in print. The audio uses *"flashcard"* 15 times and never says what one physically is | `PRINTED` |
| 14 | `chart-eurjpy-m15-adr-readout-reached-no` | 00:13:55 | `EURJPYm,M15`, 21–22 Mar 2012. Printed ADR readout: **`ADR Value= 1081, Reached= No, Today's Range= 732, T's High= 110.451, T's Low= 109.719 / Target High= 110.800, Target Low= 109.370 / To ADR High= 989, To ADR Low= 441`**. Boxes labelled `R = 44.2`, `R = 107.9`, `R = 44.3`, `R = 73.2`. Right panel: `Pips To HOD 64.0`, `Pips To LOD 9.2`, `Candle Time 0:56`. `TDI_MMM 46.6269 46.0035 47.9257` sub-panel | **The most informative single frame in the lesson.** It prints the ADR indicator's whole output — and **still does not state a lookback** (`A-038`). `Pips To HOD` / `Pips To LOD` are printed, which is the *"Hi-Lo"* distance made mechanical. `TDI_MMM` is displayed with three values and no legend (`A-039`) | `PRINTED` |
| 15 | `chart-eurusd-m15-adr-readout-reached-yes` | 00:16:20 | `EURUSDm,M15`, 19–21 Mar 2012. **`ADR Value= 1023, Reached= Yes, Today's Range= 1030, …`** Boxes `R = 18.9`, `R = 65.2`, `R = 38.1`, `R = 78.0` | **The `Reached=` flag in its other state.** Paired with frame 14 this is the mechanical meaning of `[00:25:26]` *"That brown line there is the ADR. It turns red when [it's met]"*: `Reached` flips when `Today's Range` ≥ `ADR Value` (1030 ≥ 1023 here; 732 < 1081 there). **That is an observation about this indicator's display, not a course rule** | `PRINTED` |
| 16 | `chart-eurjpy-m15-partial-repaint-over-slide-background` | 00:17:35 | The **same** `EURJPYm` screen as frame 14, repainted over the deck background — see the artifact section above | Evidence that the presenter holds one chart across several minutes; the transcript's *"I put that one in already"* `[00:17:41]` is the same observation | `VISUAL` |
| 17 | `chart-annotated-bias-level-1-short-shark-fin-in-tdi` | 00:18:25 | A **student's** chart (`[00:17:44]` *"let's look at some trades here that other people did"*). Printed annotations: **"BIAS LEVEL 1 SHORT"**, **"enter short pos 1"**, **"enter short pos 2"**, **"1 st TP 52 PIPS"**, **"2 ND TP 67 PIPS"**, **"SHARK FIN IN TDI"** with a red box drawn on the TDI sub-panel. Right panel `M0`/`M1`/`M2`/`M3` lines, `Pivot`, `ADR High 1.44522`, `Pips To HOD 69.4`, `Pips To LOD 37.1` | **The first frame anywhere in this corpus that points at a shark fin ON the TDI panel** — `A-032` has had the phrase since V03 and never a marked instance. Also the first printed **two-position scale-in with two take-profits**, and the first printed `M0`–`M3` level labels (**new — logged as `A-055`**) | `PRINTED` |
| 18 | `chart-audusd-m15-enter-after-2nd-leg-rr-tracks-exit-50-pips` | 00:19:15 | `AUDUSDm,M15`, 15–16 Feb 2012. Printed: **"Enter after 2nd leg RR tracks"**, **"Exit +50 pips & 8.57% gain"**, a hand-drawn **W** over the pattern, an orange rectangle around it. Boxes `R = 76.8`, `R = 86.7`. `Pivot` line, `DayHi`/`DayLo` lines. Platform strip: **"Go Trader 4, © 2001-2011 MetaQuotes Software Corp."** | **A complete printed entry-and-exit rule**: entry *after* the second leg's railroad tracks, exit at +50 pips. It corroborates `[00:30:52]`–`[00:31:03]` verbatim. **`D-030` blocks coding it** — *second leg* and *railroad tracks* are both undefined. The `8.57% gain` for 50 pips is the only account-percentage figure in the lesson | `PRINTED` |
| 19 | `slide-final-synopsis` | 00:19:30 | The full synopsis paragraph (transcribed in `V07_SOURCE_NOTES.md` §11f) | The lesson's own summary of itself, in the presenter's print | `PRINTED` |
| 20 | `slide-happy-trading-to-all` | 00:21:35 | *"Happy Trading to all! I look forward to posting trades here for those turning the corner who have not experienced that level of excitement that goes with good trades."* | The deck's closing slide — establishes that the deck ends at ~21:35 and everything after is Q&A | `PRINTED` |
| 21 | `chart-audusd-m15-day-separator-question` | 00:24:05 | The **same** `AUDUSDm` screen as frame 18, re-shown. The vertical dotted lines are visible | The frame the presenter is pointing at while answering Martha: `[00:24:03]` *"I'm talking about the vertical lines here. This is the day separator."* | `VISUAL` |
| 22 | `chart-eurjpy-m15-revisited-for-the-adr-and-ma-question` | 00:25:30 | The `EURJPYm` screen again (partial repaint — see artifact section) | The frame under discussion at `[00:25:21]`–`[00:25:44]`: the brown **ADR** line, and *"this yellow one is a five moving average… I made it dotted in the 13, 50 and the 200"* | `VISUAL` |
| 23 | `chart-eurusd-m15-stair-step-higher-timeframe-average` | 00:27:00 | `EURUSDm,M15`, 15–16 Feb 2012. A **brown stair-stepped line** is plotted among smooth cyan / white / blue / dotted averages. A white vertical dashed line marks the day boundary at 15 Feb 22:33 | The object of `[00:26:08]`–`[00:27:41]`: a higher-timeframe moving average brought down onto the 15-minute chart, which *"doesn't know how to fill in the gaps"* and therefore steps. **The visual confirms the mechanism the presenter describes** | `VISUAL` |
| 24 | `final-synopsis-standing-through-the-qa` | 00:34:50 | The Final Synopsis slide, unchanged | Recorded to establish the **negative** fact: from 00:34:50 to 00:48:05 — **27% of the lesson** — the screen does not change again. There is no visual evidence in the last quarter of this lesson, and a reader should not expect any | `VISUAL` |

---

## WHAT THE FRAMES ADDED, AND WHAT THEY DID NOT

**Added, and could not have come from the audio:**

1. **The lesson's title and date.** *"Best Trade Grabs / MMFx Breakout Session 03-26-2012"*.
2. **"M or W"**, settling a two-way ASR garble that both transcriptions got wrong.
3. **"Hi-Lo"** as the printed spelling of the entry method — and `Pips To HOD` / `Pips To LOD`
   printed on the chart panel, which is what makes it a measurable object at all.
4. **"Flashcards (Screenshots)"** — the physical definition of an artifact named 15 times in
   audio and never described.
5. **The struck-through "Homework"**, printed. The rename to *"R&D"* is a deliberate act, not a
   verbal tic.
6. **The full ADR indicator readout in two states** (`Reached= No` / `Reached= Yes`), which
   mechanises `[00:25:26]` *"It turns red when [it's met]"* — brackets marking the editorial
   reconstruction, matching row 15 of the frame table above. The source word is **unrecovered**:
   the transcript reads *"It turns red when **Beth**."*

> *(Superseded text, retained per `REMEDIATION_PROTOCOL.md` §2 — corrected 2026-08-13, V07 R2
> remediation, open item 70; `V07_REVIEW_R2.md` `M1`, instance (c), `E01` with co-code `E20`.)*
>
> **Item 6 previously read:** *"…which mechanises *"it turns red when **it's met**"*."* —
> unbracketed and with no adjacent marker, so a later session had no signal that it was reading a
> reconstruction. **Row 15 of this file's own frame table had the convention right** — it renders
> *"That brown line there is the ADR. It turns red when **[it's met]**"* — and is **not** edited.
> Verified against `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` at `[00:25:26]` for this correction.
> **No conclusion moves:** the two-state readout is read off the frames, not off the word.
7. **"SHARK FIN IN TDI"** with a box drawn on the oscillator — the first located instance of
   `A-032`'s object.
8. **`M0` / `M1` / `M2` / `M3`** printed level labels — a new undefined object (`A-055`).
9. **A complete printed entry/exit annotation** — *"Enter after 2nd leg RR tracks"* / *"Exit +50
   pips"*.

**Did NOT add, stated as negatives so a later session does not go looking:**

- **No moving-average period is attached to any nickname**, in print or in audio. `[00:25:34]`
  attaches a **colour** to a **period** (*"this yellow one is a five moving average"*) and
  `[00:27:24]` attaches **nicknames** to a **timeframe** (*"30 minute of the water, 30 minute of
  the male"*) — but the two are never joined. **`A-020`'s Required Research route fails for a
  sixth lesson running.**
- **No ADR lookback**, despite the indicator printing `ADR Value=` twice. `A-038` untouched.
- **No TDI definition.** `TDI_MMM` is displayed with three numbers and a marked shark fin, and
  no inputs, periods, band values or line names appear. `A-039` is **extended, not closed** —
  displayed is still not taught.
- **No session clock of any kind.** `EST` 0×, no time table, no London/New York window
  boundaries. The only clock objects are the MT4 x-axis stamps and `Candle Time`. **Checked on
  all 24 frames**, at full resolution, because this is the exact class of claim V06 R1 `M1`
  charged as a `MAJOR`.
- **No week-cycle or peak-formation diagram.** The quarantined `VISUAL_INDEX.md` for this lesson
  describes seven such slides; none of them exists (`QUARANTINE_REGISTER.md` **Q-008**).
