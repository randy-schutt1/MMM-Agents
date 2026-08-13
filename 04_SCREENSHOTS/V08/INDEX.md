# V08 — SCREENSHOT INDEX

26 curated frames from `Bootcamp1 Wk2 032612 Part3 (43mins).swf` — **"Jim's Journey in Learning
and Trading MMFX"**.

> ## EVERY FRAME IN THIS DIRECTORY IS `GUEST` MATERIAL — AND UNDER `D-033` THAT DOES NOT DEMOTE IT
>
> V08 has **no course-author segment**. A single presenter — not Steve Mauro — speaks the whole
> 00:42:58 (`02_TRANSCRIPTS/V08/V08_TRANSCRIPT.md` § "ONE SPEAKER…"). Under `DECISIONS.md`
> **D-033** (2026-08-13, owner direction, *"all knowledge is created equal"*) this material is
> **NORMATIVE evidence at equal weight** with the course author's. It may define rules, enter
> the spec directories, close an `A-xxx` or `C-xxx` record, and be cited for or against any
> other statement in the corpus.
>
> **Two things `D-033` explicitly does not change, and both bite here:**
>
> 1. **Speaker tagging stays mandatory** (`D-033` provision 1). Every frame below is `GUEST`.
> 2. **`D-030` still binds.** A printed phrase resting on a term the course has named and never
>    defined — *M/W* (`A-011`), *second leg* (`A-007`), *trap area* (`A-002`), *level*
>    (`A-004`) — **remains un-operationalisable no matter who printed it.** Frames `00-38-10`
>    and `00-40-10` are the sharp cases here: they print a complete, confident, executable-
>    *looking* entry doctrine whose operative noun is *"the extremes of M and W formations"*.
>    Recorded in full; **may not be coded.**

---

## PROCESS DISCLOSURE — EVIDENCE ORDER

`SWF_CAPTURE_RECIPE.md` §9 asks that source notes be written from the transcript **before**
screenshots are examined, so a reviewer can see which conclusions survive on audio alone.

**V08 achieved that separation, and V07 did not.** `V07_SOURCE_NOTES.md` §0 records honestly that
all 31 of its detected screen states had been seen before its notes were drafted, because the
recipe's own §§7–8 require looking at contact sheets before naming frames. **This session
inverted the order**: the sweep ran in the background, and no contact sheet was built or examined
until `V08_SOURCE_NOTES.md` §§1–11 and the whole of `V08_INTERPRETATION.md` §§1–7 were written
and committed (commits `c83f4ca` and the interpretation commit that follows it).

**Two frames were exceptions, and both are verification steps the recipe mandates rather than
study:**

| Frame | Why it was looked at first |
|---|---|
| `V08_00-00-05` (title slide) | `SWF_CAPTURE_RECIPE.md` §8 and V07's precedent require the lesson title to come from **inside the recording**, not from a filename or a quarantined note |
| the sweep frame at presentation `20:00` | `GOTCHA 4` requires a content sanity check against the transcript **before** a long capture is trusted — the check that, when skipped, cost this project a 61-minute capture and produced `D-020` |

**This wording is identical in `V08_SOURCE_NOTES.md` §0 and `V08_INTERPRETATION.md` §0 on
purpose** (`V05_REVIEW_R1.md` `M4` charged V05 for three files disagreeing about V05's own
process).

---

## CAPTURE PROVENANCE

| Field | Value |
|---|---|
| Method | Ruffle WASM + Playwright 10× fast sweep (`SWF_CAPTURE_RECIPE.md` §10, `D-021`) |
| Sweep | **529 frames**, one per 5 presentation-seconds, 1024×786, **full frame including the control bar** so every image proves its own timestamp |
| Source SHA-256 | `6beedb40b7c211cb019b37ff69002e8e625fca4521c3cf3155f946edc5f8b767` — matches `SOURCE_MANIFEST.md` |
| Working copy | `v08_x10.swf` — a **copy**. Frame rate patched 3.0 → 30.0 fps; `frameCount` **7,752** unchanged. The original was re-hashed after patching and is byte-identical |
| Duration cross-check | 7,752 frames ÷ 3.0 fps = **2584.0 s**, against measured audio **2583.75 s** and `SOURCE_MANIFEST.md` 00:43:03 |
| Port discipline (`D-022`) | Port **8938**, verified free with `lsof` before binding, verified owned by this session's PID after binding, and the served bytes SHA-256-matched against the file on disk. Both checks, before any capture |
| Distinct screen states | **56** detected (frame-to-frame mean-difference > 6.0, runs collapsed within 10 presentation-seconds). 518 of 529 frames are pixel-distinct |
| Selection | 26 of 56, chosen for content coverage after **every candidate was viewed** on contact sheets and the text-bearing ones re-read at half or full resolution before being named |

> ### ⚠ THE FIRST SWEEP OF THIS LESSON WAS A COMPLETE FAILURE, AND IT IS RECORDED RATHER THAN QUIETLY REDONE
>
> The first 529-frame sweep produced **one distinct image, 529 times**: the Camtasia splash with
> its play button still showing. `SWF_CAPTURE_RECIPE.md` §3's `mouse.click(512, 300)` **misses
> the play target on this file** — V08's splash centres its play button at approximately
> `(512, 325)`, and the recipe's coordinate lands just above it.
>
> **Nothing downstream looked wrong.** The page loaded, Ruffle initialised, `__ready` went true,
> 529 valid 1024×786 PNGs were written, and the run reported `DONE`. This is the same shape as
> `GOTCHA 4`'s port collision — a pipeline that completes successfully while capturing nothing —
> and it was caught only by hashing the frames against each other.
>
> **The fix adopted, and it is general:** the sweep script now screenshots **before** and
> **1.5 s after** the play click and **aborts with a non-zero exit** if the two are byte-identical.
> A capture that cannot prove playback started should not be allowed to produce 529 files. The
> click target was established by a four-target probe rather than guessed.

---

## THE FRAMES

Descriptors are **what is shown, not what it means** (`FILE_NAMING_STANDARD.md` §3). Every frame
carries the player's burned-in timecode bottom-right, so each image proves its own position.

| # | File | Presentation time | What is on screen |
|---|---|---|---|
| 1 | `V08_00-00-05_title-slide-jims-journey.png` | 00:00:05 | Title slide: **"Jim's Journey in Learning and Trading MMFX"** over a photograph of a bird. **The lesson's title, from inside the recording** |
| 2 | `V08_00-01-40_photo-trading-desk-three-monitors.png` | 00:01:40 | Photograph of a home trading desk: three monitors on a wall mount, two further screens, a keyboard instrument, rack gear. *"This is my trading sanctuary"* `[00:01:25]` |
| 3 | `V08_00-05-00_section-1-map-of-stages.png` | 00:05:00 | **"Section 1: A brief MAP of the stages of learning this method -- what are our vulnerabilities at each stage -- how can we identify which stage we are at with it?"** over a rifle-scope reticle |
| 4 | `V08_00-05-40_section-2-high-low-drill-within-10-pips-hod-lod.png` | 00:05:40 | **"Section 2: A VIEW TO A KILL. The High Low Drill and Elements of Mastery for dealing within 10 pips of HOD/LOD. How DOING the High Low Drill Teaches one the TIMING ASPECT of Price Action or the SPEED of PRICE."** ★ **carries a number the audio does not** |
| 5 | `V08_00-06-05_section-3-defined-risk-lesson.png` | 00:06:05 | **"Section 3: How to not 'GET' Killed. A Defined Risk Lesson so that you will never again BLOW UP AN ACCOUNT !!!"** — **the section this file does not contain** |
| 6 | `V08_00-06-20_stages-map-empty-rings.png` | 00:06:20 | **"A Map of the Stages of Learning MMFX"** — four concentric rings, unlabelled |
| 7 | `V08_00-08-25_stages-map-four-bands-labelled.png` | 00:08:25 | The same rings, filled in: centre **"Steady Equity Growth"**; then **"Can instantly recognize confirmed M/W entries"**; then **"I am no longer skeptical about the method as I look to my own ACTIONS which need improvement"**; outer **"I am looking at the setups of the preivous week WITH MY OWN EYES to see if the method works"** *(sic — `preivous`)* |
| 8 | `V08_00-08-55_stages-map-outer-band-four-doubts.png` | 00:08:55 | The map plus four printed doubts outside the outermost ring: **"Steve's thing might be another FX scam!"** · **"'They Say' I may as well just trade the weather!"** · **"I wonder if anyeone is really dong well LIVE with this method?"** *(sic)* · **"I want to know what OTHERS think of it!!!"** |
| 9 | `V08_00-12-45_missing-puzzle-piece-brain.png` | 00:12:45 | Photograph: a sectioned model head with a jigsaw piece missing. The *"missing puzzle piece"* image `[00:12:41]` |
| 10 | `V08_00-13-55_prussian-origins-snow-white-mentality.png` | 00:13:55 | The same image captioned **"The Prussion based origins of modern education have perpetuated a SNOW WHITE mentality where we constantly look outside our self for our answers -- what someone 'says' about something -- all so that we unquestionably follow the heard when told to do so."** *(sic — `Prussion`, `heard`)* |
| 11 | `V08_00-15-05_rings-validate-the-method-arrow.png` | 00:15:05 | Rings, with **"Not sure with my own eyes if MMFX method is valid"** above and **"VALIDATE THE METHOD"** in green, an arrow pointing inward through the outermost ring |
| 12 | `V08_00-17-00_weather-report-29-setups.png` | 00:17:00 | **"MMFX Weather Report / Week of Mar 19th, 2012"** and, in a yellow hazard box, **"29 SETUPS !!!"**. ★ the slide prints **SETUPS**, not trades — see `C-007` |
| 13 | `V08_00-20-00_gallery-eurcad-multi-day-w.png` | 00:20:00 | MT4 M15 chart, `EURCAD,M15` tab active, `EC` watermark, x-axis 21–22 Mar 2012, shaded session boxes, TDI panel beneath. **The `GOTCHA 4` verification frame** — transcript `[00:19:57]` *"There's a multi-day W in E.C."* |
| 14 | `V08_00-22-00_mt4-terminal-two-closed-eurusd-shorts.png` | 00:22:00 | MT4 with the **account terminal panel open** — two closed `eurusd` rows. See the dedicated section below; **this frame required a 3× zoom before anything was read off it** |
| 15 | `V08_00-24-05_rings-outer-shell-broken.png` | 00:24:05 | Rings with **"VALIDATE THE METHOD"** completed — the first threshold crossed |
| 16 | `V08_00-27-20_two-training-methods-listed.png` | 00:27:20 | **"To get good at something just takes EXPERIENCE and REPETITION -- we need to bring our actions IN LINE with the method and leverage our SUBCONSCIOUS MIND to internalize setup recognition and near automatic ACTIONS."** then **"1. The High Low Drill / 2. Hard Righ Edge Pattern Training"** *(sic — `Righ`)* ★ **the lesson's two techniques, named and numbered in print** |
| 17 | `V08_00-27-45_rings-eliminate-skepticism-cant-see-before.png` | 00:27:45 | Rings, second threshold: **"Eliminate Skepticism"**, annotated **"Still not able to fully ACT in line with the method…"** and **"I can see an M or W Pattern clearly AFTER it forms but can't see it BEFORE it forms…"** ★ **the lesson's central problem, in print** |
| 18 | `V08_00-28-50_photo-bamboo-tablet-markup.png` | 00:28:50 | A chart captioned **"I would spend many hours on weekends marking up charts and decided to buy a bamboo tablet to be able to free hand mark up the charts"**, with a photograph of a graphics tablet and stylus |
| 19 | `V08_00-29-35_subconscious-strong-ideas-lodge.png` | 00:29:35 | Chart captioned **"The issue was I was spending hours LOOKING at FULLY FORMED M's and W's."** plus a diagram: **"Strong Ideas held in the conscious mind"** → red arrow → **"Lodge into the SubConscious Mind"** |
| 20 | `V08_00-31-50_mini-movies-of-candles.png` | 00:31:50 | Chart captioned **"I could create mini MOVIES of candles as they formed and could DRILL setups in a more realistic way"** |
| 21 | `V08_00-34-00_worked-example-cadjpy-flashcard-sequence.png` | 00:34:00 | The CAD/JPY worked example mid-replay — `CJ` watermark, shaded session boxes, TDI panel. Transcript `[00:33:29]`–`[00:35:05]` |
| 22 | `V08_00-35-40_high-low-drill-title-cadjpy.png` | 00:35:40 | The same CAD/JPY chart, captioned only **"The High Low Drill"** — the section's opening state, before any annotation is added |
| 23 | `V08_00-38-10_high-low-drill-confirmation-myth-safest-place.png` | 00:38:10 | Same chart, now annotated: **"It gives one insight into the TIMING of the Market Makers"** · **"It flushes out the big trading myth that one needs CONFIRMATION IN THE SAME DIRECTION to enter a trade…"** · **"Contrary to the MYTH it is the SAFEST PLACE TO ENTER TRADES"** · **"You will be Entering HERE"** with a leader line to the low. ★ **`C-009` in print** |
| 24 | `V08_00-40-10_high-low-drill-crown-jewel-3-to-1.png` | 00:40:10 | Same chart, fully annotated: **"When pulling it into live trading, the effects of this training are that entries will start to migrate toward the 'extremes' of 'M' and 'W' formations."** and **"Becomes the Crown Jewel of the Method as one can enter even Tighter Stops thus bringing Risk Reward to 3:1 or greater!"** ★ **the R:R claim, printed** |
| 25 | `V08_00-42-00_gbpcad-crosshair-on-the-low.png` | 00:42:00 | GBP/CAD chart (`GBPCAD,M15` tab active, `GC` watermark) blacked out except a **rifle-scope reticle** magnifying the candles at the low. The *"get out your microscope"* moment `[00:41:48]` |
| 26 | `V08_00-43-04_end-card-innermost-stage-unanswered.png` | 00:43:04 ✎ | The rings with three thresholds labelled — **"Validate the Method"**, **"Eliminate Skepticism"**, **"Learn to INSTANTLY Recognize Confirmation Candles"** — and **the centre containing a red question mark**, beside a `replay` button. ★ **the file's final frame — the POST-PLAYBACK END CARD**: playback has stopped, which is why the `replay` button is showing, and why `43:04` sits at the very end of the **00:43:03** runtime rather than past it. See the correction note below |

---

## FRAME 14 IN DETAIL — THE ONLY ACCOUNT RECORD IN V08

`V08_00-22-00_mt4-terminal-two-closed-eurusd-shorts.png` is the single frame in this lesson that
shows an execution rather than a chart, and it is **the frame most likely to be misread**, so
what it actually says is set out here rather than compressed into the table.

At full resolution, magnified 3×, the terminal panel reads:

```text
Symbol    Price      S/L        T/P        Time                Price      Swap    Profit
eurusd    1.32424    1.32360    1.30596    2012.03.22 10:08    1.32056    0.00    3 680.00
eurusd    1.32449    1.32360    1.30596    2012.03.22 10:08    1.32070    0.00    3 790.00
```

**What can be read off it, and only this:**

- Two **EUR/USD** positions, both closed at **2012.03.22 10:08** — Thursday of the gallery week.
- Closes are **below** opens with **positive** profit, so both are **shorts**: −36.8 and −37.9
  pips respectively.
- Both carry **`S/L 1.32360`** and **`T/P 1.30596`**.
- The visible chart tab strip: `…PY,H1 | CADJPY,M15 | AUDJPY,M15 | GBPCAD,M15 | XAUUSD,H1 |
  GBPUSD,H1 | GBPUSD,H1 | EURUSD,M15` *(active)* `| EURUSD,M15`.

> ### ⚠ THE `S/L` IN THIS FRAME IS NOT AN INITIAL STOP, AND MUST NOT BE READ AS ONE
>
> `1.32360` sits **6.4 and 8.9 pips *below* the two entries**. For a **short**, a stop below the
> entry is **in profit** — it is a trailed stop locking a small gain, not the risk the trade was
> opened with. **The initial stop distance is not visible in this frame and is not recoverable
> from it.**
>
> This matters because V08's one performance claim is about stops (*"tighter stops… Risk Reward
> to 3:1 or greater"*, frame `00-40-10`), and a 6.4-pip number sitting in an `S/L` column is
> exactly the kind of figure that would get quoted as *"his stop was 6 pips"* and then coded.
> **It is not that number.** Recorded here so the misreading is closed off before it is made.

**What it does corroborate, and this is worth having:** the transcript at `[00:21:36]`–`[00:21:53]`
narrates a EUR/USD *"continuation M formation… This was your high of weak… First leg, second leg,
railroad track, entry. Down you go"* and then `[00:21:52]` *"Oh, goodness. **I got that one
too.**"* The panel shows two EUR/USD shorts closed that same week. **A claim to have taken a
trade is supported by a visible account record** — which is more than any other *"I took it"* in
the lesson gets, and is recorded as evidence about that one claim, not about the other 28.

**What it does not do:** no lot size and no account balance are visible, so the money figures
imply nothing about risk as a fraction of capital, and nothing here bears on `C-007` (the count
of *setups* becoming a count of *trades*).

---

## WHAT THE FRAMES ADDED THAT THE AUDIO DID NOT

Cross-referenced in `V08_SOURCE_NOTES.md` §12 and `V08_INTERPRETATION.md` §8. Summarised here:

| # | Addition | Frame |
|---|---|---|
| 1 | **"within 10 pips of HOD/LOD"** — a numeric tolerance for the high-low drill that is **nowhere in the audio**. The transcript's `[00:05:35]` renders it *"dealing with intent pips of high day and low day"*; **`intent pips` is the ASR's rendering of *in ten pips*, and the slide proves it** | `00-05-40` |
| 2 | **"FX scam"** — the transcript's `[00:08:58]` reads *"another FX scan"*. The slide prints **scam** | `00-08-55` |
| 3 | **"Prussion [Prussian] based origins"** — the transcript's `[00:13:44]` reads *"Depression-based origins of modern education"*. The slide prints **Prussion** | `00-13-55` |
| 4 | **The two techniques are numbered doctrine**, not an aside: *"1. The High Low Drill / 2. Hard Righ Edge Pattern Training"* | `00-27-20` |
| 5 | **The R:R claim and the confirmation-myth claim are printed**, not spoken asides — which raises what `C-009` and `A-056` are weighing | `00-38-10`, `00-40-10` |
| 6 | **The lesson's central problem is a printed slide bullet**: *"I can see an M or W Pattern clearly AFTER it forms but can't see it BEFORE it forms…"* | `00-27-45` |
| 7 | **The end card confirms the file ends on an unanswered question** — the innermost ring holds a literal **"?"**. The audio-only reading in `V08_SOURCE_NOTES.md` §1 is corroborated, not corrected | `00-43-04` ✎ |
| 8 | **A TDI panel is displayed on every chart in this lesson** and is never mentioned in the audio. *Displayed, not taught* — the `A-039` formula, unchanged | `00-20-00`, `00-34-00`, `00-40-10` |

**What the frames did NOT settle:** *fast* and *slow* remain undefined (`A-061`) — no frame prints
a speed criterion. The stop hunt box's **placement** rule is still absent (`A-063`); frames show
shaded boxes but nothing states where they are anchored. And no frame names the presenter, so
`[00:17:29]`'s *"Okay, Jim's right about that one"* stays unresolved.

---

## ✎ CORRECTION, 2026-08-13 — ROW 26'S TIMECODE WAS WRONG BY ~6 SECONDS AND THE FILE HAS BEEN RENAMED

Applied in remediation of `18_REVIEW/V08/V08_REVIEW_R1.md` **`M3`** (`E19`, `REVIEW_INDEX.md`
open item **66**). Recorded here rather than as an inline `SUPERSEDED` block because the fix is a
**file rename**, not a passage of prose — `REMEDIATION_PROTOCOL.md` §2's retention requirement is
satisfied by naming the old value explicitly below, so the audit trail survives the rename.

| Field | Before | After |
|---|---|---|
| Filename | `V08_00-43-10_end-card-innermost-stage-unanswered.png` **← SUPERSEDED, INCORRECT TIMECODE** | `V08_00-43-04_end-card-innermost-stage-unanswered.png` |
| Row 26 timecode | `00:43:10` **← SUPERSEDED** | `00:43:04` |
| "What the frames settled" item 7 | `00-43-10` **← SUPERSEDED** | `00-43-04` |
| `V08_SOURCE_NOTES.md` §12 item 4 | `00-43-10` **← SUPERSEDED** | `00-43-04` |

**What was wrong.** `00:43:10` is **past the lesson's measured runtime of 00:43:03** (2583.75 s,
established on three independent bases in `V08_TRANSCRIPT.md` and re-measured by the R1
reviewer). The recording does not contain a `00:43:10`. The label was simply mis-typed at
capture.

**How the correct value was established, in this remediation and not taken from the review.** The
PNG was opened and the player chrome at the bottom-right of the frame was cropped and
magnified. **The burned-in timecode reads `43:04 / 43:0…`** — the elapsed field reads `43:04` and
the total field is truncated by the frame edge at `43:0`. This is an independent confirmation of
the reviewer's reading, made by looking at the same pixels.

**Why `43:04` is consistent with a 00:43:03 runtime and is not a second defect.** The frame is
the **post-playback end card**: the `replay` button is visible, so playback has already
terminated. A player's elapsed field at rest on the final frame rounds up to the ceiling of the
duration. `43:04` is the end of the file; `43:10` was **six seconds beyond the frame's own
timecode and seven seconds beyond the runtime**.

**The frame is genuine and no content claim changes.** The literal red `?` at the centre of the
innermost ring — the observation row 26 and item 7 exist to record — was confirmed by the R1
reviewer reading the image and again here. **The defect was purely the label.**

**Why a six-second label error was charged at all.** `Q-009` (`QUARANTINE_REGISTER.md`), authored
in this same V08 submission, proposes as its **first** cheap fabrication screen: *"any timestamp
exceeding the lesson's runtime in `SOURCE_MANIFEST.md`."* V08's own screenshot set tripped that
screen. A future session running the test this project itself recommends would have had to stop
and establish that the project's own capture was not a fabrication. **Internal consistency with a
test the corpus authors against itself is worth more than six seconds normally would be.**

**No other V08 frame trips the screen** — verified in this remediation by parsing the timecode
out of all **26** filenames and comparing each against 2583.75 s. Row 26 was the only one.

> #### ⚠ ONE RESIDUAL, STATED RATHER THAN GLOSSED
>
> **`00:43:04` is 2,584 s and the runtime is 2,583.75 s, so the corrected label still exceeds
> the runtime — by 0.25 of a second.** A naive implementation of `Q-009`'s screen (*"any
> timestamp exceeding the lesson's runtime"*) will therefore **still flag row 26**, and this note
> exists so that the next session hits an explanation instead of a mystery.
>
> **This is not a further defect and the label is not wrong.** `43:04` is what the player's own
> burned-in chrome prints on the final frame, and a player's whole-second elapsed field cannot
> print `43:03.75`; it displays the ceiling. The frame therefore **cannot** be labelled with its
> true timecode *and* fall strictly under the runtime. Choosing the burned-in value is correct:
> the label now matches the artifact's own internal evidence, which is the property that
> distinguishes a genuine capture from a fabricated one.
>
> **Consequence for `Q-009`'s screen, recorded for whoever implements it:** the screen needs a
> **one-second tolerance** — flag `timestamp > ceil(runtime)`, not `timestamp > runtime` — or it
> will produce a false positive on the legitimate final frame of any recording whose duration is
> not a whole number of seconds. `00:43:10` exceeded `ceil(2583.75) = 2584` by six seconds and is
> a true positive under either form; `00:43:04` equals it exactly and is not.
