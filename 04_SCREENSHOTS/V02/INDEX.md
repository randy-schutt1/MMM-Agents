# V02 — SCREENSHOT INDEX

| Field | Value |
|---|---|
| Video ID | V02 |
| Source | `Bootcamp1 Wk1 031812 Part2 (60mins).swf` — SHA-256 `03079acf…20bce9f` |
| Captured | 2026-08-10 |
| Method | Ruffle 0.5.0 WASM in headless Chrome via Playwright, **10× fast sweep** (SWF header frame rate patched 3.0 → 30.0 in a working copy). See `00_SYSTEM/SWF_CAPTURE_RECIPE.md` §10 and D-021. |
| Sweep | 732 frames at 5 presentation-second spacing, 366 s wall clock for a 60:20 lesson |
| Frames retained | 25 |
| Frame size | 1024 × 786, full player frame including the control bar |

## How to read these

Every frame retains the Camtasia control bar at the bottom, which burns in
`MM:SS / 60:2` — **each screenshot proves its own timestamp.** That is deliberate: this
project quarantined 72 files for asserting timestamps that did not match content
(`QUARANTINE_REGISTER.md` Q-001, Q-002), and a self-proving frame cannot make that
mistake.

The filename timestamp and the burned-in timecode should always agree. If they ever
disagree, trust the burned-in value and raise it.

> **Provenance note.** An earlier capture attempt in this session produced a full hour of
> footage that was **V01, not V02**, because a stale HTTP server from the V01 session
> owned the port and served its own SWF. Every frame below comes from the corrected
> capture, and was validated against the transcript at four independent timestamps before
> anything was named (see `SETUP_ISSUES.md` I-009, `SWF_CAPTURE_RECIPE.md` GOTCHA 4).
> The burned-in total reads `60:2` on every frame here; the bad capture read `54:4`.

## Screens

| # | File | Time | What is shown |
|---|---|---|---|
| 1 | `V02_00-00-45_typical-week-chart-carried-from-v01.png` | 00:45 | The "Typical Week" GBPUSD M15 chart still on screen from the end of V01. V02 opens mid-topic on the same slide. |
| 2 | `V02_00-04-30_typical-week-green-annotations.png` | 04:30 | Same chart, green freehand annotation added over the midweek region while he explains the anchor point. |
| 3 | `V02_00-06-00_typical-week-annotations-extended.png` | 06:00 | Further green annotation; ADR × 3 discussion. |
| 4 | `V02_00-08-55_weekly-structure-text-slide.png` | 08:55 | **"Weekly Structure"** text slide — four printed bullets. The authored source for §2d. |
| 5 | `V02_00-11-40_weekly-structure-annotated-red-green.png` | 11:40 | Same slide with red and green freehand marks over bullets 2 and 3. |
| 6 | `V02_00-16-40_weekly-structure-annotations-final.png` | 16:40 | Final annotated state of the Weekly Structure slide. |
| 7 | `V02_00-18-00_weekly-market-structure-levels-chart.png` | 18:00 | **"Weekly Market Structure"** — GBPUSD H1, day-column dividers, the most information-dense slide in the lesson. Labels below. |
| 8 | `V02_00-19-20_weekly-market-structure-red-marks.png` | 19:20 | Same chart, red freehand marks added at the DNC region. |
| 9 | `V02_00-20-40_weekly-market-structure-level-numbering.png` | 20:40 | Same chart with hand-written "2" and "3" over the level columns. |
| 10 | `V02_00-22-55_higher-level-longs-trapped-chart.png` | 22:55 | **"Higher Level Longs Trapped"** chart — printed labels "Traders Feel It will come back and they can book", "End The Week Below Last Weeks LOW", "LOW", "Spike Issued →", "You will sit the rest of the week and still not see a profit". |
| 11 | `V02_00-23-40_higher-level-longs-trapped-annotated.png` | 23:40 | Same chart, red annotation over the accumulation range. |
| 12 | `V02_00-26-00_higher-level-longs-trapped-final-state.png` | 26:00 | Final annotated state; the M formation at the previous week's low is circled. |
| 13 | `V02_00-28-00_how-to-beat-the-market-maker-slide.png` | 28:00 | **"How To Beat The Market Maker"** — three printed bullets on reading the moves. |
| 14 | `V02_00-33-10_market-maker-moves-slide.png` | 33:10 | **"Market Maker Moves"** — four printed bullets, clean. Contains the 2-hour rule. |
| 15 | `V02_00-35-50_market-maker-moves-annotated.png` | 35:50 | Same slide with red annotation beside the NYC-reversal bullet. |
| 16 | `V02_00-40-00_market-maker-moves-annotations-final.png` | 40:00 | Final annotated state. |
| 17 | `V02_00-42-55_variations-on-the-theme-slide.png` | 42:55 | **"Variations On The Theme"** — four printed bullets on how the dealer varies delivery. |
| 18 | `V02_00-45-55_forex-trading-times-slide.png` | 45:55 | **"ForEx Trading Times"** — the complete session table. Highest-value frame in the set. |
| 19 | `V02_00-47-20_second-most-important-element-slide.png` | 47:20 | **"SECOND MOST IMPORTANT ELEMENT OF THIS METHOD"** — five printed bullets on time mapping. |
| 20 | `V02_00-50-50_forex-trading-times-revisited.png` | 50:50 | The trading-times slide shown again during the daylight-saving discussion. |
| 21 | `V02_00-52-25_pop-quiz-label-the-weekly-cycle.png` | 52:25 | PowerPoint in edit mode: "Pop Quiz / Label the weekly cycle". |
| 22 | `V02_00-52-40_pop-quiz-usdchf-chart.png` | 52:40 | The USD/CHF chart set as the pop quiz, on the grey template. |
| 23 | `V02_00-54-50_answer-posted-in-forum-slide.png` | 54:50 | "Answer will be posted in the forum tonight for review". |
| 24 | `V02_00-55-35_rd-assignment-40-flashcards.png` | 55:35 | **R & D assignment slide** — the flashcard homework, in full. |
| 25 | `V02_00-56-55_thanks-for-coming-slide.png` | 56:55 | "Thanks for coming! / Same time next week!" |

## Verbatim text from the printed slides

Transcribed from the frames, not from audio. Slide text is authored material and is
better evidence than the ASR for anything it covers.

### #4 / #5 / #6 — "Weekly Structure" (08:55)

```text
Market Makers' Trap Traders On The First Day Of The Trading Week And Tie Up Your
  Margin For The Remaining Days By Aggressively Moving Away From The LOW or HOW.
They Will Trade Above / Below The Previous Peak Possibly Using It As The
  High / Low Of The Current Week
The Objective Is To Stay Above/Below The Perceived Support/Resistance Level
  For At Least 3 Days Causing Exhaustion And Panic.
In Turn Many Traders Will Cut The Position With A Huge Loss Or If The Account
  Was Over Leveraged Get Called Out
```

`HOW` is not expanded on the slide. Read alongside `LOW` in the same phrase it is most
likely "High Of Week" against "Low Of Week", but **the expansion is not stated** and is
not adopted.

### #7 — "Weekly Market Structure" (18:00)

GBPUSD H1. Vertical dashed dividers split the chart into day columns. Printed labels,
left to right:

```text
False Move Week Beginning
V-3            PFL
Straight Away-Level 1 DNC
Stop Hunt Low-Rise      Level 2
Stop Hunt Low-Rise      Level 3
33-Trade
Level 3 Exit and Reverse
Swing Traders Book- Day Traders Book
```

Shaded rectangles carry `R =` values: `15.0`, `~25`, `29.6`, `53.8`, `61.4`, `70.7`,
`86.7`, `100.6`. Same label family as V01's A-018.

### #14 — "Market Maker Moves" (33:10)

```text
Always Look To Take Profit At Session Change Over (Especially New Traders)
New Session Brings New Targets For Market Makers ( NYC Reversal)
If Trade Does Not See Substantial Profit In 2 Hours, Take Profit Or Small Loss.
If Second Leg Presents, Restart The Clock
```

### #17 — "Variations On The Theme" (42:55)

```text
Changing The Session In Which The Moves Come
Changing The Severity Of The Stop Hunts, Mild Or Extended
Concealing Them Behind News And Announcements.
Blaming Geo-political Events
```

### #18 / #20 — "ForEx Trading Times" (45:55)

```text
5pm High / Low Reset (The MM Spread Is Set)
5pm to 8pm Dead Gap
Asian Session:  8:30pm - 3:00am    Gap 3-3:30a
London Session: 3:30am - 9:00am    Gap 9-9:30a
New York Session: 9:30-5pm
```

**No timezone is printed on the slide.** See A-019.

### #19 — "SECOND MOST IMPORTANT ELEMENT OF THIS METHOD" (47:20)

```text
Time Mapping (Map Your Own Broker)
New Indicators Must Match Times
Identifying The Formations At The Appropriate Times
Don't Get Confused With Time Ribbon On The Bottom Of Broker's Platform (Server Times)
All Other Time References Are GARBAGE
```

### #13 — "How To Beat The Market Maker" (28:00)

```text
As A Trader You Must Understand How To Read These Moves
Anticipate When And How They Will Present.
Then, You Can Truly Beat The MM By Simply Trading Inline With Him
```

### #24 — R & D assignment (55:35)

```text
R & D assignment  Cycle 1 Week 1
Map out last weeks  Usd/Chf
Develop 40 flash cards
4 Majors: EUR/USD, GBP/USD, USD/CHF, USD/JPY
5Ms
5Ws
Out of the 40, Pick one perfect M and W (only 1)
Label it post it for review in the forum
```

The PowerPoint title bar in this frame reads **"Market Maker Boot Camp 3-18"**,
independently confirming the 18 March 2012 session date recorded in
`SOURCE_MANIFEST.md`.

## Not captured

The lesson's visual content ends at the "Thanks for coming" slide around 56:55; the
remaining ~3 minutes are the sign-off over a static final slide, then the player's
end/replay state. Nothing analytical is lost.
