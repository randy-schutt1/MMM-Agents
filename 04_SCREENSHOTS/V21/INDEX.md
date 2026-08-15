# V21 — SCREENSHOT INDEX

**Lesson:** `Bootcamp1 Wk10 061712 (75mins).swf` — Week 10, 2012-06-17 — **the final bootcamp session**
**17 frames**, `SWF_CAPTURE_RECIPE.md` §10 fast sweep at **10×**, 906 frames captured.

---

## §0 — ⚠️ REQUIRED §8a VERIFICATION

| Field | Value | Source |
|---|---|---|
| Stage | ⭐ **1280 × 738** | header RECT — **so the play click is `(512, 325)`, NOT `(512, 300)`** (`GOTCHA 5`) |
| Declared `frameRate` | **3.0** | header — patched to **30.0** (= ×10), derived from **this** file |
| `frameCount` | 13463 | ⇒ implied **4487.667 s** |
| Play-click guard | ⭐ **before/after differed — the click took effect** | `GOTCHA 5` |
| Port | free, then verified serving **my** bytes by SHA-256 | `GOTCHA 4` |

⭐ **`GOTCHA 5` EARNED ITS PLACE HERE.** V21 is one of the three `1280 × 738` files. Ruffle fits that
stage into the `1024 × 786` viewport at scale 0.8, **letterboxed with dark bands top and bottom**,
and the player chrome sits at `y ≈ 670` instead of `y ≈ 766`. **A session reusing V20's
`(512, 300)` click and V20's timecode crop would have swept a splash screen and then failed to read
any timecode.**

### The measurement — ⭐ A SIXTH SHAPE: A STARTUP TRANSIENT **PLUS** A SLOW NEGATIVE DRIFT

| frame `i` | `i × 5` | **burned** | offset |
|---|---|---|---|
| 0 | 00:00 | **00:16** | **+16 s** |
| 1 | 00:05 | **00:16** | **+11 s** |
| 2 | 00:10 | **00:17** | **+7 s** |
| 3 | 00:15 | **00:17** | **+2 s** |
| 6 | 00:30 | **00:30** | ⭐ **0 s** |
| 24 / 180 / 300 / 360 | 02:00 / 15:00 / 25:00 / 30:00 | **exact** | **0 s** |
| 420 | 35:00 | 34:59 | **−1 s** |
| 465 | 38:45 | 38:44 | −1 s |
| 477 | 39:45 | **39:45** | 0 s |
| 512 | 42:40 | 42:38 | **−2 s** |
| 595 / 620 | 49:35 / 51:40 | 49:33 / 51:38 | **−2 s** |
| 750 / 860 | 62:30 / 71:40 | **62:28 / 71:38** ⚠️ *(OSD shows MM:SS past the hour — `01:02:28` / `01:11:38`)* | **−2 s** |
| 897 | 74:45 | 74:43 | −2 s |
| 900 | 75:00 | **74:47** | ⚠️ **clamped at the file end — expected, §8a step 2** |

⭐⭐ **TWO EFFECTS, NOT ONE.** The `+16 s` startup transient is **the same value V19 and V20
measured** (`+16` / `+17`) and is **absorbed to zero by 30 seconds**, corroborating item 296's
absolute-deadline mechanism for a **third** sweep. **On top of it sits a slow NEGATIVE drift** that
reaches **−2 s** by `42:38` and holds. ⚠️ **The 0 s reading at `i = 477` between two −1 s readings
shows this is sub-second drift displayed at 1-second granularity, not a clean staircase** — so it is
described as a drift, not as steps.

**Rate check (§8a step 3):** consecutive burned deltas match consecutive filename deltas everywhere
except across a drift boundary, where they differ by the 1 s display quantum. **ORIGIN plus DRIFT,
not RATE** — a rate error would compound to minutes over 75 minutes, and the total excursion is 2
seconds.

⭐⭐ **EVERY FILENAME BELOW CARRIES ITS OWN BURNED TIMECODE, READ FROM THE PIXELS INDIVIDUALLY** —
not `i × 5`, and not a single global offset. **Seventeen frames, seventeen reads.**

> ### ⚠️ CORRECTED 2026-08-15 — V21 R1 item **368**
>
> ⛔ **Two frames were first named `00-62-28` and `00-71-38` — `62` and `71` in the MINUTES field,
> which `FILE_NAMING_STANDARD.md`'s `VXX_HH-MM-SS_…` does not permit.** ⭐ **Cause: the player OSD
> displays `MM:SS` PAST THE HOUR on a 75-minute file, and §8a step 4 correctly requires naming from
> the burned value — so the OSD string was pasted without converting the rollover.** **Renamed to
> `01-02-28` and `01-11-38`.** ⚠️ **V10 (01:36:16) resolved this correctly and V21's own transcript
> grid rolls over properly (`[01:14:24]`), so the standard was available and simply not applied at
> the naming step.** ⭐ **Recommended: `SWF_CAPTURE_RECIPE.md` §8a step 4 should state the conversion
> explicitly for files over an hour.**

---

## §1 — THE FRAMES

| # | Frame (burned) | What is on screen |
|---|---|---|
| 1 | `00-20` schedule | The final-session schedule: June 17 final regular session, **June 24 live in New Jersey**, **July 1 two-month break** — ⭐ matching V19's printed schedule slide exactly |
| 2 | `02-45` manage-your-expectations | *"Manage Your Expectations"* — the recurring slide |
| 3 | `07-55` your-takeaways-checklist | *"Your Takeaways"* — can you spot a clean setup, identify the structures, the four-hour big picture |
| 4 | `15-00` the-article | The reprinted article: *"…there must be a loser. Winners' profits come from the losers."* |
| 5 | ⭐ `16-40` realities-of-trading | **`Realities Of Trading; What Dealers Do:` — `Hunt Stops! (as a collective)` / `Vary the Levels that these stops are triggered at!` / `Spike Past Support & Resistance/Pivots/Breakout levels/ Fib numbers/ etc….` / `This is part of the "Business As Usual" Mentality`** |
| 6 | ⭐ `20-20` control-equity-like-a-dealer | **`Since I Can Trade Like A Dealer, It Only Makes Sense To Control My Equity Like A Dealer Until I Can Improve My Hit Rates And Entries` / `I Will Allow For The Things The Dealer Will Do To Me, and Still Come Out On Top!`** |
| 7 | `21-20` blank-paint-canvas | An empty **MS Paint** window — the whiteboard the *"lose at a discount"* grid is drawn on |
| 8 | ⭐ `30-30` how-can-we-automatically-set-orders | **`How Can We Automatically Set Orders To Handle The Varying Levels Of The Dealer` / `How Can We Avoid Getting Stopped On An Otherwise Good Entry`** — the problem the script answers |
| 9 | ⭐⭐⭐ `31-25` **handwritten-high-low-trainer-spec-2010** | **THE MOST VALUABLE FRAME IN THE CORPUS TO DATE.** See §2 |
| 10 | ⭐ `38-44` measuring-success-1 | **`Measuring Your Success` / `All Three Orders Are Opening, Or You Are Getting Stopped.` / `Need More Screen Time, Boot Camp, R&D` / `You Are Simply Not Identifying The Entries`** |
| 11 | ⭐ `39-45` measuring-success-2 | **`2 Orders Are Opening, and You Are Moving Towards Profit.` / `Trader Is Getting Better, but Under Normal Conditions Would Have Been Stopped Out.` / `You Are Almost There. Perhaps You Are Too Impatient Or Too Aggressive?` / `Trader Should Be Able To Move To Next Level With Minor Adjustments, or Behavior Modifications`** |
| 12–16 | `42-38`, `44-24`, `49-33`, `51-38`, `01-02-28` | The **MT4 installation walkthrough** — right-click the broker icon, open file location, `experts/scripts`, paste, attach to chart |
| 17 | `01-11-38` closing-section | The closing stretch |

⭐ **Frames 12–16 are a live screen recording of a Windows desktop**, and **`6/17/2012` is legible in
the OS clock area on several of them** — ⭐⭐ **the recording dating itself from its own machine**,
independently agreeing with `SOURCE_MANIFEST.md`, the filename `061712`, and the spoken
`[00:00:17]` *"today is June 17th"*.

---

## §2 — FRAME 9, THE HANDWRITTEN SPECIFICATION — TRANSCRIBED FROM THE PIXELS

**A photograph of the instructor's own handwritten notes, dated `1-27-2010` in his hand.**

> **High / Low Trainer**
> Script That Allows Traders A Chance To Turn a profit While Becoming proficient @ Picking The
> **HOD/LOD**. **MAX RISK 5% on all orders**
> **Risk Setting 1% To 5% on all orders Combined.** A User Defined Field By Entering a 1 Thru 5
> Number. Ex: `[Risk %] 3` = 3%
> **Stop Loss** — ↕ **20 pips** ↕ **20 pips** ↕ **20 pips** — Open Live @ once, **2 pending** Are
> placed immediately following open order
> **Sell Cycle** — **30 pips**
> Take profit **+30 pips** from ORDER 1 = Market order
> If all Three (3) orders are filled you will Cycle w/the **30 + 50 + 70**. Most often **+150 pips**
> / **+80**

⭐⭐⭐ **THIS NAMES THE TOOL AND FIXES ITS PARAMETERS IN THE AUTHOR'S OWN HAND.**

⚠️⚠️ **AND IT CORRECTS THE TRANSCRIPT'S NAME FOR IT.** The committed grid renders `[00:30:18]` as
*"a script that was produced by Ray call **training wheels**"* and `[00:30:50]` as *"Meet the
**feeling script**"*. ⛔ **The tool's printed name is `High / Low Trainer`.** *"Training wheels"* is
plausibly a real phrase he also uses, but **the artifact's name is on the page.**

⚠️ **The handwritten sheet and the spoken account DISAGREE on one number** — see
`V21_INTERPRETATION.md` §2.3 and `C-031`. **The sheet says take profit `+30` from order 1 and a
`30 + 50 + 70` cycle; the audio at `[00:32:55]` says *"you will cycle with a hundred and fifty
pips"* and at `[00:33:17]` *"you'll get a 30 and a 50 … you will cycle with 80 pips"`.** ⭐ **The
sheet's `30 + 50 + 70 = 150` and its `+80` reconcile both figures**, which is why the frame matters.
