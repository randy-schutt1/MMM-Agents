# V19 — SCREENSHOT INDEX

**Lesson:** `Bootcamp1 Wk9 052012 Part1 (67mins).swf` — V19, Week 9 Part 1, 2012-05-20
**Frames:** 27, all `1024 × 786`, full frame **including the control bar**, so every image proves
its own timestamp (`SWF_CAPTURE_RECIPE.md` §8).
**Method:** 10× fast sweep (`§10`), 817 frames at a 5-presentation-second grid, patched
`3.0 → 30.0 fps` from **this file's own header**.

---

## §0 — ⚠⚠ REQUIRED: THE SWEEP→CLOCK OFFSET, MEASURED THIS LESSON AND PUBLISHED

`SWF_CAPTURE_RECIPE.md` **§8a** makes this step mandatory and forbids carrying a previous lesson's
value forward. **V12 measured `+16 s`, V13 `+15 s`, V14 `+16 s`, V16 and V17 flat zero, V18
`0 → −3 s`. V19 is its own number again, and it is a fourth shape.**

### The measurement — read from the pixels, not from the filenames

Every value in the `burned` column was read off the player's own bottom-right readout in that
frame, upscaled 5×.

| sweep `i` | `i × 5` (s) | burned | burned (s) | **offset** |
|---|---|---|---|---|
| 0 | 0 | `00:16` | 16 | **+16** ⚠ see note |
| 1 | 5 | `00:16` | 16 | +11 ⚠ |
| 24 | 120 | `02:00` | 120 | **0** |
| 40 | 200 | `03:20` | 200 | **0** |
| 100 | 500 | `08:20` | 500 | **0** |
| 160 | 800 | `13:20` | 800 | **0** |
| 240 | 1200 | `20:00` | 1200 | **0** |
| 320 | 1600 | `26:40` | 1600 | **0** |
| 400 | 2000 | `33:20` | 2000 | **0** |
| 480 | 2400 | `40:00` | 2400 | **0** |
| 560 | 2800 | `46:40` | 2800 | **0** |
| 570 | 2850 | `47:30` | 2850 | **0** |
| 580 | 2900 | `48:20` | 2900 | **0** |
| 590 | 2950 | `49:10` | 2950 | **0** |
| **600** | **3000** | `49:59` | 2999 | **−1** ← the step |
| 640 | 3200 | `53:19` | 3199 | **−1** |
| 720 | 3600 | `59:59` | 3599 | **−1** |
| 800 | 4000 | `66:39` | 3999 | **−1** |
| 808 | 4040 | `67:19` | 4039 | −1 |
| 816 | 4080 | `67:22` | 4042 | **clamped** — expected, §8a step 2 |

**Result: offset `0 s` from `02:00` to `49:10`, and `−1 s` from `49:59` to the end.** The single
one-second step is **bracketed to the interval `49:10`–`49:59`** by the five probes at
`i = 560/570/580/590/600`, which were run specifically to narrow it.

### ⚠ Why `i = 0` and `i = 1` read `+16 s` and `+11 s` — and why it is NOT the §8a origin error

§8a warns that the play click's wall-clock latency is multiplied by the speed factor, so ~1.5 s of
latency becomes ~15 s of presentation time. **That is exactly what the first frames show.** It does
**not** propagate, because this session's sweep loop schedules each frame against an **absolute**
deadline (`t0 + i × STEP_MS`) rather than incrementally. Frames `i = 0,1,2` fire immediately
because their deadlines have already passed; by `i ≈ 3` the schedule catches up and stays caught up.
**The latency is absorbed instead of accumulated.** Recorded because it means a session using an
incremental sleep on this same file *would* have measured a constant `+16 s`, which is the value
V12 and V14 recorded.

### §8a step 3 — ORIGIN OR RATE? **ORIGIN.**

Consecutive filename deltas against consecutive burned deltas:

```text
i 40->100   Δname 300   Δburned 300   OK        i 400->480  Δname 400   Δburned 400   OK
i 100->160  Δname 300   Δburned 300   OK        i 480->560  Δname 400   Δburned 400   OK
i 160->240  Δname 400   Δburned 400   OK        i 560->640  Δname 400   Δburned 399   -1
i 240->320  Δname 400   Δburned 400   OK        i 640->720  Δname 400   Δburned 400   OK
i 320->400  Δname 400   Δburned 400   OK        i 720->800  Δname 400   Δburned 400   OK
```

**Ten of eleven intervals are exact.** The single `−1` is the one step above, not a rate error —
a rate error would make *every* interval short, and none of the other ten is. **The fps patch is
correct and no offset was applied to any filename.**

### §8a step 4 — EVERY FILENAME BELOW IS ITS OWN FRAME'S BURNED TIMECODE

**27 of 27 frames had their readout cropped and read individually before naming.** Six of the
27 sit past the drift step and are named `−1 s` from `i × 5` accordingly — `00-50-19`, `00-50-34`,
`00-51-49`, `00-57-54`, `01-02-44`, `01-05-49`. **Naming those from `i × 5` would have produced six
wrong filenames**, which is the V14 failure this step exists to prevent.

### ⚠ WHAT IS NOT HERE

**The deck's cover slide (`MARKET MAKERS BOOT CAMP / WEEK 9`) is NOT in this set.** The 10× sweep's
first frame is already at `00:16`, by which point the schedule slide has replaced it. A 1× pass was
attempted specifically to capture it and **failed twice at the play click** — see
`V19_TRANSCRIPT.md` VERIFICATION §6. The `WEEK 9` legend is therefore **not independently captured
by this session**, and no V19 artifact rests on it: the week number is carried by
`[00:00:00]` *"Welcome back week nine"* and the date by the printed schedule slide at `02:00`.

---

## §1 — THE FRAMES

| # | File | Burned | What is shown |
|---|---|---|---|
| 1 | `V19_00-02-00_schedule-may20-to-july1.png` | `02:00` | Printed schedule: `May 20th Regular session`, `May 27th Memorial day weekend- enjoy ( no session)`, `June 3rd Web class 4 days`, `June 10th Recordings will be up review or retake the class as needed`, `June 17th Final boot camp regular session`, `June 24th Live in New Jersey!!!`, `July 1st 2 month break- retake the boot camp via recordings. Put everything into action` |
| 2 | `V19_00-04-10_managing-your-expectations-bullets.png` | `04:10` | `Managing Your Expectations……` — `Follow along free from distraction…`, `Give me 2 Hrs a week!`, `Make an honest effort at completing all assignments on time`, `Execute in demo the concepts as illustrated`, `Refrain from negativity in your own mind` |
| 3 | `V19_00-04-55_announcements-trade-strong.png` | `04:55` | `ANNOUNCEMENTS` slide, body reduced to `Trade Strong!` |
| 4 | `V19_00-05-55_progress-student-email.png` | `05:55` | `PROGRESS……` — a student email reproduced in full, signed `Ronny C` |
| 5 | `V19_00-06-45_by-now-you-should-checklist.png` | `06:45` | `Where are you?` / `By now you should…..` — `Have a set of Flash cards`, `Have 4hr Markups`, `Have Taken TDI only Trades`, `Worked the Big Board`, `Moving AVG Only trades`, `Understand Pivot Points`, `Use ADR and Hi/Lo Markers` |
| 6 | `V19_00-11-15_happy-birthday-steve.png` | `11:15` | `Happy Birthday, Steve! We love you very much! Love, Heidi, Chase, and Gemma`, with a cupcake photograph |
| 7 | `V19_00-12-00_trap-move-agenda-three-bullets.png` | `12:00` | `MARKET MAKER TRAP MOVE` — `Trap Candle Patterns` / `Dealer Structures` / `Behavioral Analysis` |
| 8 | `V19_00-12-25_half-a-batman-title-batman-image.png` | `12:25` | `MARKET MAKER TRAP MOVE` / `HALF- A -BATMAN` over a photograph of Batman |
| 9 | `V19_00-13-15_half-a-batman-definition-four-clauses.png` | `13:15` | `Half-A-Batman:` — the four-clause definition (see §2) |
| 10 | `V19_00-14-15_half-a-batman-chart-clean.png` | `14:15` | `Half – a - Batman` chart, un-annotated: white line, yellow line, red line, magenta/green candles |
| 11 | `V19_00-15-00_half-a-batman-chart-annotated.png` | `15:00` | The same chart with the instructor's live red annotations — the high boxed, the consolidation boxed, the shift arrow |
| 12 | `V19_00-16-30_inverted-half-batman-chart.png` | `16:30` | Chart of the inverted (low-side) case, cyan dashed level across |
| 13 | `V19_00-17-55_consolidation-off-the-low-chart.png` | `17:55` | Chart used for the `15 to 25 pips` consolidation numbers |
| 14 | `V19_00-19-30_ant-in-spider-web-photo-grid.png` | `19:30` | A photographic grid — the image the instructor calls *"an ant made out of a spider web, which is a trap"* |
| 15 | `V19_00-21-15_m-formation-slide-before-edit.png` | `21:15` | ⭐ The `"M" Formation` slide **as originally written** — final rule line ends *"…but must close below."* |
| 16 | `V19_00-23-10_powerpoint-editing-m-formation-slide.png` | `23:10` | ⭐⭐ The **PowerPoint editing window**, mid-edit, on the `"M" Formation` slide |
| 17 | `V19_00-23-25_m-formation-slide-30m-added.png` | `23:25` | ⭐⭐ The same slide **after the edit** — the line now reads *"…but must close below with in 30M"* |
| 18 | `V19_00-30-00_m-formation-chart-hand-drawn.png` | `30:00` | `MARKET MAKER TRAP MOVES` — an M drawn freehand in magenta over the candles, yellow and red moving averages, cyan dashed level |
| 19 | `V19_00-36-10_thirty-minute-example-chart.png` | `36:10` | The worked example of the 30-minute rule; grey-background chart with yellow / red / cyan lines |
| 20 | `V19_00-43-50_student-flashcard-the-pattern.png` | `43:50` | A student-made flashcard, `The Pattern The Pattern The Pattern!!`, with `Short Trade:` and `Long Trade:` numbered checklists |
| 21 | `V19_00-45-00_w-formation-slide-before-edit.png` | `45:00` | ⭐ The `"W"` slide **as originally written** — final rule line ends *"…but must close above."* |
| 22 | `V19_00-50-19_powerpoint-editing-w-formation-slide.png` | `50:19` | ⭐⭐ The **PowerPoint editing window** again, this time on the `"W"` slide |
| 23 | `V19_00-50-34_w-formation-slide-30-to-45-added.png` | `50:34` | ⭐⭐ The same slide **after the edit** — *"…but must close above with in 30 to 45 m"* |
| 24 | `V19_00-51-49_big-w-structure-chart.png` | `51:49` | The large W structure; moving averages compressing at the right edge |
| 25 | `V19_00-57-54_higher-timeframe-railroad-tracks.png` | `57:54` | Higher-timeframe chart, railroad tracks at a cyan dashed level |
| 26 | `V19_01-02-44_star-formation-definition.png` | `62:44` | `Evening Star` / `Morning Star` / `Simply put : An extra 15M for the Market Maker to take your money` |
| 27 | `V19_01-05-49_quasi-railroad-tracks-chart.png` | `65:49` | The "railroad track broken into four pieces" example |

---

## §2 — WHAT THE PRINTED SLIDES SETTLE THAT THE AUDIO DOES NOT

**This is the §9 step-4 pass and it is kept separate on purpose.** `V19_SOURCE_NOTES.md` and
`V19_INTERPRETATION.md` were written from the transcript alone, before these frames were read.
Everything below is a correction or a confirmation the visuals supply.

### (a) ⭐⭐ THE LESSON'S OWN TITLE IS UNREADABLE IN THE COMMITTED TRANSCRIPT

| Source | Text |
|---|---|
| Committed transcript `[00:12:02]` | *"**Track King patterns fuel structures** behavioral analysis"* |
| ⭐ The printed agenda slide at `12:00` | **`Trap Candle Patterns`** / **`Dealer Structures`** / **`Behavioral Analysis`** |

**Two of the lesson's three announced subjects are unrecoverable from the audio transcript alone.**
*"Track King"* is *"Trap Candle"*; *"fuel structures"* is *"Dealer Structures"*.

### (b) ⭐ `HALF-A-BATMAN` — THE SPELLING, AND THE DECK IS NOT SELF-CONSISTENT

The committed transcript renders it *"half a bad man"* / *"half of that man"* / *"Back man"*
throughout — **seven** variants. The deck prints it **three different ways**:

| Frame | Printed |
|---|---|
| `12:25` | `HALF- A -BATMAN` |
| `13:15` | `Half-A-Batman:` |
| `14:15`, `15:00` | `Half – a - Batman` |

**The concept name is settled; its typography is not.** Artifacts use **`Half-A-Batman`**, the form
on the definition slide.

### (c) ⭐ THE `HALF-A-BATMAN` DEFINITION, PRINTED — AND THE TRANSCRIPT INVERTS ONE CONNECTIVE

Printed at `13:15`, verbatim:

```text
Half-A-Batman:
The dealer has spiked the High or Low as a means to set it for the session
The Dealer is now trading off of that level (Outside Structure)
He will not repeat the level again, or he will allow some type of profit booking by the traders.
Price appears to roll off of the level and the trend is underway
```

| Committed transcript | Printed slide | Independent ASR |
|---|---|---|
| `[00:13:37]` *"**You** will not repeat that level again"* | *"**He** will not repeat the level again"* | *"**He** will not repeat that level again"* |
| `[00:13:42]` *"**If he does you** will allow some type of **profit-looking**"* | *"**or he** will allow some type of **profit booking**"* | *"**if he does, he** will allow some type of **profit booking**"* |

⚠ **Note the slide and the speech genuinely differ on the connective** — the slide says *"or"*, and
the independent engine confirms he *said* *"if he does"*. That is a real speech/deck divergence, not
an ASR defect. The ASR defects are **`you`** for **`he`** and **`profit-looking`** for
**`profit booking`**.

### (d) ⭐ `HOD / HOS` AND `LOD / LOS` ARE PRINTED ABBREVIATIONS

The `"M" Formation` slide prints *"set the **HOD or HOS**"*; the `"W"` slide prints *"set the
**LOD or LOS**"*. The transcript at `[00:19:50]` gives *"Here's a new term for you or the **HLS**"*
followed by *"high of the session"*. **The printed form is `HOS`, not `HLS`.**

### (e) ⭐ FOUR CHECKLIST ITEMS ARE UNRECOVERABLE FROM AUDIO

The `06:45` checklist settles a passage the transcript mangles badly:

| Committed transcript `[00:08:01]`–`[00:08:12]` | Printed |
|---|---|
| *"If you haven't worked **the big boy, don't your movie average only**"* | `Worked the Big Board` / `Moving AVG Only trades` |
| *"review the recording used to **I low market the blue tracer** / **A yard**"* | `Use ADR and Hi/Lo Markers` |

⭐ ***"A yard"* is `ADR`.** Recorded because `00_SYSTEM/DECISION_DRAFT_D-051_ADR_INDICATOR.md`
concerns exactly this indicator; **this frame is Tier 1 evidence that the course prescribes an
`ADR` marker as standing homework**, which the draft should see. **No adoption is proposed here.**

### (f) ⭐ THE STUDENT EMAIL'S NUMBERS, PRINTED

The `05:55` frame reproduces the email the instructor reads aloud at `[00:06:10]`–`[00:06:29]`,
where the ASR is poor. Printed: *"I have taken 12 trades (10 wins / 2 losses) where I lost about
$1k a netted just under $16k"*. **The spoken *"nearly just under 16"* is `$16k`, and the *"16 to
one ratio"* is the ratio those two printed figures make.** Both are the student's claims, reported;
**neither is a course rule and no V19 artifact treats them as one.**

### (g) MOVING-AVERAGE COLOURS — CONSISTENT WITH `D-043`, AND NOT PROBATIVE

Every chart frame carries a **yellow** and a **red** moving average, and most carry a **cyan** and a
**white** one. `[00:31:29]` names the yellow one *"the mustard"* in a passage where the trade is
*"collapsed inside the mustard"*. **This is consistent with `D-043`'s ruling (5 = mustard = yellow,
13 = ketchup = red)** and it is recorded as consistency, **not** as new evidence: no frame in this
lesson prints a period next to a colour, so the pairing is not measured here. `ketchup` is spoken
**zero** times in V19.

### (h) ⚠ THE `blue tracer` IS NOT IDENTIFIED BY THESE FRAMES

*"Blue tracer"* is spoken **15 times** and is load-bearing for the entry rule at `[00:31:29]`. The
charts carry **two** candidate blue-family lines — a **cyan dashed horizontal** level and a **cyan
solid sloping** average — and the lesson never says which. **This session did not resolve it and
does not guess.** Opened as `A-133`.

---

## §3 — PROVENANCE

| Field | Value |
|---|---|
| Sweep | 817 frames, `s_0000.png` … `s_0816.png`, 5-presentation-second grid at 10× |
| Served from | `http://127.0.0.1:8919/` — port checked free before binding, listener PID confirmed, and the served bytes SHA-256-matched against the on-disk copy before any capture (`D-022`, `GOTCHA 4`) |
| Play-click guard | Pre-click / post-click screenshot comparison, **fired and passed** on the patched copy; **fired and correctly aborted** twice on the unpatched copy (`GOTCHA 5`) |
| Content sanity check | Frame at `13:20` compared against transcript `[00:13:10]` **before** the long capture was trusted — `Half-A-Batman` definition slide against *"The definition of a half a bad man"*. Matched (`GOTCHA 4`, final paragraph) |
| Original SHA-256 | `7e8a1c2b…1ab28e`, re-verified after patching |
| Retained outside the repo | The full 817-frame sweep, in this session's scratchpad; anything not curated here can be pulled again |
