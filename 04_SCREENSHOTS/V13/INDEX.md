# V13 — SCREENSHOT INDEX

`Bootcamp1 Wk5 041512 Part1 (65mins).swf` · 30 curated frames from a 793-frame 10× sweep

---

## CAPTURE PROVENANCE

| Field | Value |
|---|---|
| Method | `SWF_CAPTURE_RECIPE.md` §10 fast sweep at **10×**, screenshots-only (no archival mp4 this lesson) |
| Declared frame rate | **3.0 fps**, read from **this file's own header** — not assumed (§10 as corrected by V10 R1 item 87) |
| Patch | `3.0 → 30.0` on a **working copy**. Original re-verified by SHA-256 afterwards: `106bb863…67807` ✅ unchanged |
| Stage size | **1024 × 786**, probed from the header before any click (`GOTCHA 5`) |
| Play coordinate | `(512, 300)` from `GOTCHA 5`'s table, **and confirmed by the mandatory before/after guard** — `sweep.log`: *"play click confirmed: stage changed"*. Not assumed |
| Port | Fresh port, **not** 8899. `lsof` proved this session's own `python` PID held it, and the served bytes were SHA-256-diffed against the local copy before capture (`GOTCHA 4` / `D-022`) ✅ |
| Sweep | 793 frames, one per **5 presentation-seconds**, `[00:00:15]`–`[01:06:15]` |
| Screen-state detection | Pairwise diff of consecutive frames at 256×190 greyscale, keep `mean > 6.0`, collapse runs within 10 s → **37 distinct screen states** |
| Curation | Contact sheets built and **looked at** before anything was named. Descriptors say **what is shown, not what it means** (`FILE_NAMING_STANDARD.md` §3) |

### ⭐ THE FRAME→TIMECODE RELATION WAS DERIVED AND VERIFIED, NOT ASSUMED

```text
burned_timecode = frame_index x 5 s + 15 s
```

The `+15 s` is the `GOTCHA 5` guard's **1.5 s of wall clock at 10×**, spent between the play click
and the sweep's `t0`. **Verified against the player's own burned-in timecode on two frames whose
OSD is legible at full resolution:**

| Frame | Predicted | Burned-in OSD | |
|---|---|---|---|
| `s_0352` | `29:35` | **`29:35 / 65:2`** | ✅ |
| `s_0384` | `32:15` | **`32:15 / 65:2`** | ✅ |

**Every committed frame retains the full 1024×786 stage including the control bar**, so each
screenshot proves its own timestamp independently of this index.

---

## ⚠ THE NEGATIVE RESULT, RECORDED FIRST BECAUSE IT IS THE MOST USEFUL THING HERE

> **NO INDICATOR-PROPERTIES DIALOG AND NO NAVIGATOR PANEL APPEARS ANYWHERE IN THIS LESSON.**
>
> `COURSE_PROGRESS.md` V13 GATE (a) named a TDI properties dialog as *"the cheapest remaining
> unblock in the project"* for `A-084`. **V12 was predicted to be that place and was not, at 672
> frames. V13 is not either, at 793.**
>
> ⭐ **And the frames close the route permanently.** The TDI sub-window legend reads
> **`TDI_MMM 46.2640 42.8277 40.2789`** — the indicator's **name and three current line values, and
> NO parameter tuple**. That is MT4's behaviour for this `TDI_MMM` deployment, whose `#property`
> short name omits its inputs. **CORRECTED 2026-08-15, item 154:** the inference is limited to this
> deployment. V10 shows a second build, `Traders Dynamic Index Visual`, with six current values and
> likewise no parameter tuple; the legend route is empirically dry across both observed builds,
> not deductively impossible for every build. The
> remaining routes are exactly three: a properties dialog, a Navigator/inputs tab, or a spoken
> identity statement. **This narrows the V14–V21 hunt and is recorded for the sessions that will
> run it.**
>
> ⚠ **VERIFIABILITY LIMIT, stated rather than glossed** — the same one V12 R1 recorded at its
> item 140. **The 793 sweep frames are NOT committed**, so the claim above is not reproducible by
> repository inspection. What IS repository-verifiable: the **30 frames below**, including all
> three TDI charts and the legend that grounds the argument.

---

## THE FRAMES

Timecodes are the **burned-in player timecode**, which is what the filenames carry.

### Announcements — `[00:00:15]`–`[00:16:15]`

| `[ts]` | File | What is shown |
|---|---|---|
| `00:00:15` | `…_title-card-welcome-back-trade-strong.png` | Opening title card: `MARKET MAKER BOOT CAMP` / *"Welcome Back"* / *"Trade Strong!"*. **No topic title — this lesson has none** |
| `00:00:45` | `…_managing-your-expectations-slide.png` | *"Managing Your Expectations"* — the six-point weekly preamble (*"Give me 2 Hrs a week!"*, *"Execute in demo the concepts as illustrated"*, *"Refrain from negativity"*) |
| `00:02:45` | `…_catch-up-and-next-session-sunday-29th.png` | *"Take this time to Catch up"* · *"Spend another week with just the TDI"* · **`"Next session will be the following Sunday the 29th."`** — the printed source for the schedule gap (§2 / Q6) |
| `00:05:55` | `…_bohemian-hotel-website-orlando-meetup.png` | The Bohemian Hotel Celebration website, shown live in a browser |
| `00:07:05` | `…_bohemian-hotel-contact-details.png` | Printed address and phone for the April 21st Orlando meetup |
| `00:08:20` | `…_next-live-class-june-23-27-hoboken.png` | *"June 23rd -27th 2012 (Sat-Wed) / Steven's Institute Hoboken New Jersey / 6PM till 11PM"* and **`"I will NOT be streaming or recording this class!"`** |
| `00:12:15` | `…_san-francisco-meetup-forum-post.png` | A forum post by **Kim Krompass**, moderator, shown on screen — settles the spelling the ASR renders four ways |
| `00:15:10` | `…_why-should-you-go-to-a-meetup.png` | *"Why Should you go to one?"* — seven printed reasons |
| `00:16:15` | `…_new-email-address-slide.png` | *"Please e-mail me: steve@ marketmakersforex.com"* — the printed form of the address the ASR renders *"MarketmakersForks.com"* |

### The TDI drill, re-specified — `[00:21:00]`

| `[ts]` | File | What is shown |
|---|---|---|
| `00:21:00` | `…_tdi-drill-printed-instructions.png` | ⭐ **The drill printed in full**, including *"Use 25 or 30 pips as a stop loss, No limit order. **It is not about these items!**"*, *"A clean entry is a shark Fin at the extreme (nothing else!)"* and *"A check point is **MB Cross, VB Break, VB Return**"*. The first printed appearance of the `MB` / `VB` abbreviations |
| `00:24:45` | `…_take-aways-most-traders-never-do-the-exercise.png` | *"Take Aways…"* — the drill's rationale |

### The test — `[00:24:55]`–`[00:28:40]`

| `[ts]` | File | What is shown |
|---|---|---|
| `00:24:55` | `…_test-title-card.png` | A slide reading only **`TEST`**. The nearest thing this lesson has to a topic title |
| `00:26:15` | `…_test-covers-first-four-weeks-of-material.png` | *"Ok we are going to test on the first 4 weeks of material"* |
| `00:26:35` | `…_quiz-questions-weekly-cycle-list.png` | ⭐ **The eight weekly-cycle questions, unanswered** — the exam paper as the students saw it |
| `00:26:55` | `…_question-1-label-this-charts-weekly-cycle.png` | *"Question 1 / Label this chart's weekly cycle"* |
| `00:27:45` | `…_quiz-chart-two-unlabelled.png` | An unlabelled MMM-template chart, shown in silence |
| `00:28:25` | `…_quiz-walk-me-through-this-4hr-chart.png` | *"Walk me through this 4hr Chart?"* — unlabelled H4 candles |
| `00:28:40` | `…_quiz-tdi-label-the-signals.png` | *"Label the Signals"* — an unannotated TDI-only chart |

### The answers — `[00:29:35]`–`[00:49:40]`

| `[ts]` | File | What is shown |
|---|---|---|
| `00:29:35` | `…_answers-boxes-blue-shadow-red-and-stop-hunt-distance.png` | ⭐⭐ **The box answers, printed.** Blue box `1 or 2 AM NYC`; purpose *"Denotes the MM's spread. Measures Asian range"*; shadow box **`3 to 4 am NYYC`** ⚠; Brinks **`3:45a 9:45a`**; stop-hunt box **`25 to 50`** ⚠; red box `8-12am`, *"NYC Reversal area"*. **Both ⚠ rows are `C-020`** |
| `00:32:15` | `…_answers-weekly-cycle-bias-and-vacate-rule.png` | ⭐⭐ **The cycle answers, printed.** First two 4hr candles → *"Psychological Support and Resistance"*; `HOW`/`LOW`; direction *"Away from peak"*; bias **`2 to 3`**; **the vacate rule** — *"Dealer hits the level again and closes above / below it on 15m chart"*; traps *"Week begin, end, session day"*; data **`3 to 5`** |
| `00:39:05` | `…_answers-safety-trade-rules-and-straightaway-difference.png` | ⭐⭐ **The safety trade, printed** — *"PF is clearly identified, level one consolidation is identified, dealer is trading **25 to 75 pips** off of the previous hi / low, dealer issues a visible stop hunt M or W formation above or below the Asian level ( second leg)"*, and the straightaway difference. **Independently corroborates V10's `25–75` anchor distance from a different deck five weeks later** |
| `00:40:35` | `…_answer-chart-weekly-cycle-marked-up.png` | The Question-1 chart with the instructor's markup: `Mid Week`, level counts, the M/W formations |
| `00:42:30` | `…_answer-chart-weekly-cycle-pen-annotation.png` | The same chart with live screen-pen annotation added |
| `00:46:00` | `…_answer-4hr-chart-marked-up.png` | The H4 chart answered — first eight hours, the false move, the M formation |
| `00:47:35` | `…_answer-chart-straightaway-no-visible-stop-hunt.png` | *"What set-up is this?"* answered on-slide: **`"Straight away…no visible SH"`** |
| `00:49:40` | `…_answer-chart-safety-trade-stop-hunt-in-line-with-peak.png` | *"What is this trade? Why?"* answered on-slide: **`"Safety trade…dealer issues a stop hunt in-line with peak formation"`** |

### The TDI review — `[00:53:35]`–`[01:04:00]`

⚠ **These three frames are deliberately NOT labelled with timeframes.** The lesson says the three
charts are 15m, H4 and H1 in some order (`[00:57:45]`, `[01:04:10]`) and the speaker also says
*"I forgot. I was looking at so many of them"* `[01:04:07]`. Assigning a timeframe to a specific
frame would be inventing evidence — see `V13_INTERPRETATION.md` Q7.

| `[ts]` | File | What is shown |
|---|---|---|
| `00:53:35` | `…_tdi-chart-one-annotated-legend-tdi-mmm-levels-37-50-63.png` | ⭐⭐ **The single most evidentially useful frame in the lesson.** A full-width TDI sub-window, annotated live with `1 2 3`, `Diverge`, `Trend x-cel`. **Legend, top-left: `TDI_MMM 46.2640 42.8277 40.2789`** — name and current values, **no parameter tuple**. **Right-hand axis: fixed level lines at `63`, `50`, `37`**, with the dynamic band values `65.3876` / `32.3876` above and below. **The shipped Traders Dynamic Index defaults are `68 / 50 / 32`. These are not those.** The `37` grounds the otherwise-unreadable spoken *"Shark fin below the support. **37**, right?"* `[00:51:16]` |
| `00:58:35` | `…_tdi-chart-two-annotated-label-the-signals.png` | The second TDI chart, annotated — three pushes marked, market-baseline crosses, band break and return |
| `01:03:35` | `…_tdi-chart-three-annotated-three-pushes.png` | The third TDI chart — the *"three moves within three moves"* / `33 trade` example |
| `01:04:00` | `…_end-of-slide-show-deck-ends-before-audio.png` | ⚠ **`"End of slide show, click to exit."`** — **the deck ends here, with 1 min 22 s of audio still to run.** Committed as evidence for a small claim that would otherwise be unsupported: the closing exchange `[01:04:03]`–`[01:05:21]` (*"The last one was one hour… I forgot"*, and the sign-off) is spoken **over a blank screen**, which is why no frame can settle Q7's chart-order question |

> ⚠️ **A CURATION ERROR CAUGHT BY LOOKING, AND RECORDED RATHER THAN QUIETLY FIXED.** The frame at
> `01:04:00` was **first selected and named as the third TDI chart** on the strength of its
> position in the sweep. It is not — it is the blank end-of-show screen above. It was caught
> because the staged file was **9.5 KB against ~370 KB for every other chart frame**, and then
> **opened and looked at**. The real third chart is `01:03:35`. This is `SWF_CAPTURE_RECIPE.md`
> §8's *"look at each frame before naming it"* failing and then being caught by the check that
> exists for it — the same shape as `GOTCHA 4` and `GOTCHA 5`, at much smaller cost.

---

## WHAT THE FRAMES CORRECTED OR ADDED, RELATIVE TO THE AUDIO-ONLY PASS

`SWF_CAPTURE_RECIPE.md` §9's whole point is that this list should exist and be honest.

| # | Effect |
|---|---|
| 1 | ⭐ **ADDED** — the TDI's level lines `63 / 50 / 37`, and the indicator's name `TDI_MMM`. **Neither is spoken.** |
| 2 | ⭐ **RESOLVED A BARE NUMBER** — `[00:51:16]`'s *"37, right?"* has no referent in audio alone. The frame supplies it. **This is the V01 *"pendings"* case repeating**: a word the audio pass would have had to refuse |
| 3 | ⭐ **CREATED A CONTRADICTION THAT AUDIO ALONE COULD NOT SEE** — `C-020`. The shadow-box and stop-hunt-box conflicts are **printed-vs-spoken**, so they are invisible without frames |
| 4 | **CONFIRMED, did not correct, the lesson title** — the audio-only draft said `NOT PRINTED` and the frames agree. Unlike V12, where the same draft was wrong |
| 5 | **ADDED** the exam paper itself (`00:26:35`), which makes the homework instrument reproducible |
| 6 | ❌ **DID NOT** supply an indicator-properties dialog, a smoothing length, an MA period, or an EMA colour legend at readable size. **All four were looked for.** See the negative-result block above and `V13_SOURCE_NOTES.md` §10 |
