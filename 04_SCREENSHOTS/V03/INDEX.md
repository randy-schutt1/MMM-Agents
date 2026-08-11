# V03 — SCREENSHOT INDEX

| Field | Value |
|---|---|
| Video ID | V03 (`Bootcamp1 Wk2 032512 Part1 (71mins).swf`, SHA-256 `efe256d8…`) |
| Captured | 2026-08-10, by the 10× fast sweep (`SWF_CAPTURE_RECIPE.md` §10; D-021, D-022) |
| Method | 857 frames at one per 5 presentation-seconds; 50 distinct screen states found by pairwise diff; 24 curated |
| Timestamp proof | Every image retains the full 1024×786 frame including the control bar; the burned-in timecode at bottom-right proves each file's own timestamp. Filenames use the burned timecode (which trails the nominal sweep position by ~1 s of startup latency). |
| Port/bytes verification | Port 8931 owned by this session's PID; served SWF SHA-256 diffed equal against the patched working copy; content sanity-checked against the transcript at `[00:02:00]` and `[00:04:14]` before curation |

All images are of the instructor's shared screen (slides, MetaTrader charts, MS Paint,
photographs he displays). `Source type` uses `SLIDE` (presentation text), `CHART`
(live/annotated chart), `PAINT` (MS Paint walkthrough), `PHOTO` (photograph shown on
screen).

| # | Screenshot | Timecode | Type | Concept | What to notice | Supports |
|---|---|---|---|---|---|---|
| 1 | `V03_00-00-05_welcome-week-two-no-bs-zone-slide.png` | 00:05 | SLIDE | Session opening | "Welcome Back / This is a NO BS Zone!! / Boot Camp will probably go 8 to 10 weeks…or how ever long it takes!!!" — resolves the `[00:00:03]` ASR garble "OBS zone" = "NO BS Zone", and corroborates the spoken 8–10/12-week extension | Transcript garble resolution |
| 2 | `V03_00-01-59_managing-your-expectations-slide.png` | 01:59 | SLIDE | Expectations | Six bullets: distraction-free attention, 2 hrs/week, assignments on time, "Execute in demo the concepts as illustrated", refrain from negativity, don't rush | S3; Q-003 Finding 3 (this — not a chart — is what is on screen at `[00:02:00]`) |
| 3 | `V03_00-04-59_this-weeks-quote-slide.png` | 04:59 | SLIDE | Psychology | "One Trade Should Not Define You As A Trader…..EVER!!!" — printed form of `[00:04:14]` | S4 |
| 4 | `V03_00-05-49_weather-chart-stop-hunt-annotation.png` | 05:49 | SLIDE | Rebuttal segment | The critics' weather chart with an orange "Stop Hunt" arrow the instructor added as a joke; a yellow consolidation box is highlighted | S6 (context only — not a trading chart) |
| 5 | `V03_00-09-49_annotated-chart-blue-boxes-wt-values.png` | 09:49 | CHART | "Same day the letter came out" examples | Intraday chart (19–20 Mar axis) with pale-blue range boxes labelled `wt = 24.8`, `wt = 116.1`, `wt = 18.5`, stepped blue DayHi/DayLo lines, subgraph below | S7; A-029 (`wt =` labels undefined) |
| 6 | `V03_00-12-09_agenda-slide-rd-cycle-flashcards-trading-zone.png` | 12:09 | SLIDE | Agenda | "R & D / Weekly Cycle / Flash Cards / Trading Zone" — the printed agenda names the trading zone; the recording ends before it is taught (deferral evidence for A-005) | S9; A-005 |
| 7 | `V03_00-12-39_weekly-cycle-4hr-block-first-8-hours-slide.png` | 12:39 | SLIDE | **Core teaching** | "Weekly Cycle on 4hr Chart / Block first 8 hours (2 bars) / This is the accumulation phase 1 (Asian of the week) / Dealer must cut the perceived support and resistance zone to make money and get traders in the game" | S10–S12 |
| 8 | `V03_00-14-14_four-hour-chart-pen-markup-week.png` | 14:14 | CHART | Worked example 1 | Four-hour chart, first-eight-hours block and levels being pen-marked while narrating the false-move week | S13 |
| 9 | `V03_00-15-29_four-hour-chart-second-week-example.png` | 15:29 | CHART | Worked example 2 | The "sloppy W" week: dealer spikes the high, no clean three levels, returns late-week; red pen box on the first two bars | S14 |
| 10 | `V03_00-16-44_four-hour-chart-outside-structure-pushes.png` | 16:44 | CHART | Worked example 3 | Pen-marked first-8h lines; the narrated "outside structure to the high, one-two-three pushes to the low, ends the range" week | S15 |
| 11 | `V03_00-17-24_four-hour-chart-choppy-week.png` | 17:24 | CHART | Worked example 4 | "A choppy week. Not as clean" — same structure claimed on an untidy week; red arrow at the late-week high | S16 |
| 12 | `V03_00-27-39_four-hour-chart-how-low-pen-markup.png` | 27:39 | CHART | HOW / LOW | Pen markup: "HOW" written above the early-week high with a box and down-arrow, "2", "3" and "LOW" written at the base of the decline. Companion to `[00:26:40]` "H-O-W high of the week" | S18; **resolves A-026** |
| 13 | `V03_00-28-44_aj-four-hour-paint-day-boxes-r-values.png` | 28:44 | PAINT | Student's AJ chart | Day-labelled boxes (Thursday…Friday) each carrying `R = <number>` (43.9, 62.3, 58.2, 34.4, 53.2, 33.7, 60.8, 47.2, 46.2, 46.6, 103.1, 98.0, 117.3…) — values consistent with per-day ranges in pips, not risk-reward | S19; A-018 (constrains) |
| 14 | `V03_00-33-19_four-hour-chart-week-example.png` | 33:19 | CHART | Net-zero week | The fake-low week re-shown clean (no pen) while narrating "net change for the week zero" `[00:33:36]` | S21 |
| 15 | `V03_00-41-54_flashcard-notation-checklist-slide.png` | 41:54 | SLIDE | **Flashcard notation** | "Note the Following: Time / Position of indicator / Vectors / Asian Range / Distance out of Asian range / Type of Trap structure used / W/M / Candle Pattern" | S25 |
| 16 | `V03_00-43-09_flash-card-sample-chart.png` | 43:09 | SLIDE | Flashcard sample | "Flash Card sample" over an EURJPY M15 chart (19 Mar 2012), pale-blue Asian box labelled `R = 41.4`, red boxes, two red arrows, TDI subgraph (`TDI_MMM`) | S26 |
| 17 | `V03_00-44-19_flash-card-sample-entry-criteria-text.png` | 44:19 | SLIDE | **Entry-criteria checklist** | Printed beside the sample card: "Asian Range =41 / 3 vectors passed mayo / Outside structure / In brinks shadow / LOD holds for 1H 30m / TDI below lower support / Shark fin / Blood in the water / 50 pip stop hunt / Entry executed on Green hammer / S/L 18 pips". Printed "mayo" resolves the transcript's "manays" garble | S27; A-020 (constrains); A-030–A-033, A-035 |
| 18 | `V03_00-46-24_desk-photo-flashcard-books.png` | 46:24 | PHOTO | Flashcard books | The instructor's desk: two monitors with charts, two labelled stacks of printed cards ("short trade sets… long trade sets") | S28 |
| 19 | `V03_00-47-19_holding-flashcard-photo.png` | 47:19 | PHOTO | Matching method | The instructor holding a printed card up beside the on-screen chart | S29 |
| 20 | `V03_00-48-14_memorize-setups-match-slide.png` | 48:14 | SLIDE | Matching rule | "Memorize these setups / Hold them up to your screen! / Make sure 'What you see' matches your successful trade card in every aspect including the level of the indicator" | S30 |
| 21 | `V03_00-49-54_paint-blockout-walkthrough.png` | 49:54 | PAINT | Card construction | Live MS Paint: black box drawn over all data right of the chosen entry candle | S31 |
| 22 | `V03_00-54-39_cow-on-lod-flashcard.png` | 54:39 | PAINT | "COW on LOD" | The instructor's own card labelled "COW on LOD" — quarter-of-wood consolidation lying on the low of the day (pale-blue box), after a red level-3 box | S33; A-036 |
| 23 | `V03_00-57-09_marked-up-flashcard-3x-lod.png` | 57:09 | PAINT | Card annotations | A heavily pen-annotated card ("3X", "LOD"), shown during the run of card examples immediately before the safety-trade description at `[00:57:20]` | S34 (context) |
| 24 | `V03_00-58-49_homework-rd-4-weekly-cycle-markups-slide.png` | 58:49 | SLIDE | **Homework** | "R&D / Do 4 Weekly cycle markups on the 4HR chart / 1 in each Major / Any date range" — the printed homework, including the date-range freedom | S36; homework §1 |

## Coverage note

The lesson's remaining visual content is: the housekeeping/mail slides (05:10–12:00,
three more letters), several near-duplicate re-showings of the four worked-example
charts, the full MS Paint walkthrough (49:15–53:00, one representative frame kept), the
remaining personal flashcards (53:15–58:00, three kept), and the closing raffle slide
(`steve@marketmakersforex.com`, 70:20). All 857 sweep frames are retained outside the
repo at the session scratchpad and any further timestamp can be re-captured from the
source in ~7 minutes via the recipe.

**No session-times slide appears anywhere in V03** — checked deliberately because
`C-004` names this lesson (recorded 25 March 2012, the DST date V02 cites) as the
natural place for an updated London-open table. The only session-time references are
spoken: `[00:55:05]` "right before the US session at 9.30" and `[01:03:21]` "3 30 in
the morning inside the shadow box".
