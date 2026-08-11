# V03 — HOMEWORK

| Field | Value |
|---|---|
| Video ID | V03 |
| Assigned | `[00:58:49]`–`[00:59:07]`, printed on the R&D slide at `[00:58:49]` |
| Attempted | 2026-08-10 |
| Data source | TradingView, FXCM feed, **4-hour** charts, **no account used, no login** |
| Charts | `05_HOMEWORK/V03/charts/` (4 files) |
| Raw data | `05_HOMEWORK/V03/data/weekly_bars_2026-08-02.json` (120 bars, exact OHLC) |
| Week analysed | **Sun 02 Aug 2026 21:00 UTC → Fri 07 Aug 2026 17:00 UTC** (30 × 4h bars) |

Two assignments were set. **11a is completed on real data with no substitution.**
**11b is completed as far as V03's own instructions allow, and the limit is stated** —
see §3.

---

## 0. NO DATA SUBSTITUTION WAS NEEDED THIS TIME

V02's homework required a substitution because the instructor asked for a specific 2012
week and TradingView's free tier could not reach it. **V03 does not have that problem,
and the reason is in the assignment itself:** the slide prints *"Any date range"*
(`V03_00-58-49_homework-rd-4-weekly-cycle-markups-slide.png`, §4f of the source notes),
and he says it aloud at `[00:59:07]`. The instructor explicitly delegated the date choice
to the student, so using a recent week is **compliance with the assignment, not a
departure from it.**

The most recent *complete* trading week at the time of work was chosen: Sun 02 Aug 2026
21:00 UTC to Fri 07 Aug 2026 17:00 UTC.

No account was created, no credentials were entered, no bot check was encountered or
bypassed, and no paywalled feature was used.

---

## 1. METHOD — AND WHY THE MEASUREMENT IS NOT PIXEL-DERIVED

V02's review (R1, `MAJOR`) turned on a real hazard: **the rendered price line shared a
colour with bullish candles, and reading prices off pixels produced a wrong answer.**
This homework therefore never reads a price from a pixel.

Instead, every number below comes from **TradingView's own OHLC legend, as DOM text.**
The chart was driven with synthetic mouse-move events across the price pane; after each
move the legend string (`O … H … L … C …`) was parsed. The legend is the platform's own
report of the hovered bar, not an interpretation of the image.

### Three independent validations were run, and all three passed

**1. The open-equals-previous-close chain.** Within a trading week, each 4h bar's open
must equal the prior bar's close on a continuous feed. Across all four pairs — 116
consecutive bar transitions — **every single one matched exactly, to five decimal places
(three for JPY). Zero breaks.** A pixel-derived or mis-harvested series would not do
this.

**2. Weekend gaps appear exactly where they should, and nowhere else.** Applying the same
test *across* week boundaries finds discontinuities at bar indices 25/26, 55, 85 and 115
— **perfectly 30 bars apart**, and 30 × 4h = 120 h = one five-day FX week. This is V02's
R2/R3 finding used as a positive test rather than an excuse: the chain is *expected* to
break at weekend boundaries and *expected* to hold within the week, and it does exactly
that. USDCHF is the one exception and it is instructive — its Sunday open equalled the
prior Friday close to five decimals, so its final weekend gap is genuinely zero rather
than missing. Its week boundary was taken from the cadence the other three pairs
establish, and this is disclosed rather than hidden.

**3. Two real-hover spot checks against a screenshot.** The synthetic-event harvest was
confirmed by driving a genuine browser mouse to the week-open bar and screenshotting:

| Pair | Harvested bar 0 | Real hover legend | Crosshair date label |
|---|---|---|---|
| USDCHF | O 0.80552 H 0.80742 L 0.80552 C 0.80685 | identical | `Sun 02 Aug '26 21:00` |
| EURUSD | O 1.15444 H 1.15588 L 1.15350 C 1.15423 | identical | `Sun 02 Aug '26 21:00` |

The crosshair label is what pins the calendar week, and it independently confirms the
week opens **Sunday 21:00 UTC** — inside the Asian session, which is what the lesson
claims ( *"it's the Asian session of the week. And it's ironic that it starts in Asia"*
`[00:13:08]` ).

### What is NOT validated

The `x` pixel positions in the raw data are hover coordinates only; nothing is measured
from them. Bar *times* after bar 0 are computed by adding 4 h per bar from the confirmed
Sunday 21:00 open, not read individually from the chart. Any DST shift inside the week
would move the labels but not the OHLC values or any conclusion below.

---

## 2. ASSIGNMENT 11a — FOUR WEEKLY-CYCLE MARKUPS ON THE 4HR CHART

> *"Research and development for the week. Do four weekly cycle markups on the four hour
> chart. Do one in each major. All right, any [date] range you want"* `[00:58:49]`–`[00:59:07]`

### 2.0 Which four pairs — a disclosed choice, not a course instruction

**V03 never enumerates "the majors"** (source notes §14 item 9). The four used here are
EURUSD, GBPUSD, USDJPY and USDCHF — the conventional four majors, and the same four V02's
homework used, so the two assignments stay comparable. **This is the student's choice and
is not attributable to the course.**

### 2.1 The procedure applied, per §5 of the source notes

For each pair: block the first eight hours of the week (bars 0–1), mark that block's high
and low, then read the rest of the week as trading away from and back to those two levels
— identifying which side the dealer cut, where the week's high (`HOW`) and low (`LOW`)
fell, and how long the run away from the extreme lasted.

### 2.2 Results — all four pairs, measured

| | EURUSD | GBPUSD | USDJPY | USDCHF |
|---|---|---|---|---|
| Block high (first 8 h) | 1.15588 | 1.35063 | 157.885 | 0.80947 |
| Block low (first 8 h) | 1.15269 | 1.34639 | 155.228 | 0.80552 |
| Block range | 31.9 p | 42.4 p | 265.7 p | 39.5 p |
| First bar cutting **below** block | bar 2 (Mon 05:00) | bar 2 (Mon 05:00) | **never** | **never** |
| First bar cutting **above** block | bar 17 (Wed 17:00) | bar 27 (Fri 09:00) | bar 9 (Tue 09:00) | bar 4 (Mon 13:00) |
| Week LOW | bar 4 — Mon 13:00 | bar 5 — Mon 17:00 | bar 0 — Sun 21:00 | bar 0 — Sun 21:00 |
| Week HIGH | bar 27 — Fri 09:00 | bar 28 — Fri 13:00 | bar 24 — Thu 21:00 | bar 22 — Thu 13:00 |
| Week range | 80.5 p | 91.2 p | 334.4 p | 80.4 p |
| Net (open → close) | +9.3 p | −1.9 p | +64.6 p | +20.2 p |
| Chain breaks within week | **0** | **0** | **0** | **0** |

### 2.3 What matched the taught pattern

**EURUSD and GBPUSD are close to textbook.** Both did exactly what §2b of the source
notes describes:

1. Built an 8-hour block (32 p and 42 p — a tight accumulation).
2. **Cut the block's low at bar 2 — Mon 05:00 UTC, the London session open** — by 26.6 p
   and 46.4 p respectively.
3. **Closed back inside the block on the very next bar** (bar 3, Mon 09:00). This is the
   false-move signature the lesson describes: take out the level, then return.
4. Put in the week's LOW on Monday (bar 4 / bar 5).
5. Ran away from that low for the rest of the week, reaching the week's HIGH on **Friday**
   (bar 27 / bar 28).

That both pairs cut the same side, on the same bar, at the London open, is the single
most striking thing in the data — and it is what the lesson predicts a dealer does.

### 2.4 What did NOT match — reported, not smoothed over

**USDJPY and USDCHF never cut below the block at all.** In both, the week's LOW *is bar
0's low* — the week opened at its lowest point and never traded below it. There was no
downside stop hunt to find.

Both instead cut **above** the block (bar 9 and bar 4) and both closed back inside
afterwards — but then went on to make the week's high in the same direction, closing the
week up (+64.6 p, +20.2 p). So the cut-above was followed by *more upside*, not by the
reversal the "false move" reading predicts.

**This is a negative result for the pattern as a directional rule, and it is recorded as
one.** The honest summary is:

- *"The dealer cuts one side of the first-eight-hours block"* — held in **4 of 4**.
- *"Price closes back inside the block after the cut"* — held in **4 of 4**.
- *"The cut is a false move, and price then runs the other way"* — held in **2 of 4**
  (EURUSD, GBPUSD). It failed in USDJPY and USDCHF, where the cut side and the week's
  direction were the same.

The 2-of-4 result is not evidence the method is wrong. It is evidence that **the method
as stated in V03 cannot tell you in advance which cut is false** — which is precisely
what the interpretation file already flags and what §4 below develops.

### 2.5 Two measured findings that bear on open register items

**Finding A — the run took longer than the taught window, in all four pairs.**

V03 teaches *"two and a half to three days"* of run away from the extreme (`[00:35:48]`,
`[00:36:05]`). Measured low-to-high duration:

| Pair | Low → high duration |
|---|---|
| EURUSD | 92 h = **3.8 days** |
| GBPUSD | 92 h = **3.8 days** |
| USDJPY | 96 h = **4.0 days** |
| USDCHF | 88 h = **3.7 days** |

**All four exceed the taught 2.5–3 day window**, by 0.7 to 1.0 days. This is real
evidence bearing on `C-001` (how long price runs away from the anchor point), which the
register carries as foundational and unresolved. One week of four pairs is a small
sample and settles nothing — but it points the same direction in 4 of 4, and it points
*away* from the shorter end of the spread the instructor kept offering.

**Finding B — the 3×ADR target was not reached in any pair.**

V03 gives the swing target as *"three times ADR over three days"* `[00:34:58]`.
Computing ADR from the week's own daily ranges:

| Pair | ADR | 3 × ADR (target) | Actual low→high swing | Achieved |
|---|---|---|---|---|
| EURUSD | 47.0 p | 140.9 p | 80.5 p | 1.71× ADR |
| GBPUSD | 54.8 p | 164.5 p | 91.2 p | 1.66× ADR |
| USDJPY | 148.2 p | 444.6 p | 334.4 p | 2.26× ADR |
| USDCHF | 56.5 p | 169.4 p | 80.4 p | 1.42× ADR |

**0 of 4 reached 3 × ADR.** Under the lesson's own exit rule — *"If ADR times three is
met or not met, but the three day time window is, and you get an outside structure high,
you better take your money"* `[00:36:11]`–`[00:36:16]` — every one of these weeks would
have been exited **on time, not on target**. That makes the time clause the operative
half of the rule in 4 of 4 cases, which is a point in the rule's favour: the instructor
appears to have added the time clause precisely because the target usually is not met.

Caveat stated plainly: ADR here is computed from **this week's own five daily ranges**,
because V03 never defines the ADR lookback period. A 14-day or 20-day ADR would give
different numbers. The lookback is undefined in the course, and that undefinedness is
itself the finding.

### 2.6 Per-pair bar tables

Full 30-bar tables with the block, the cuts and the week's extremes marked are in
`data/weekly_bars_2026-08-02.json`. The chart images are:

| Pair | Chart |
|---|---|
| EURUSD | `charts/EURUSD_4H_2026-08-10_tradingview-fxcm.png` |
| GBPUSD | `charts/GBPUSD_4H_2026-08-10_tradingview-fxcm.png` |
| USDJPY | `charts/USDJPY_4H_2026-08-10_tradingview-fxcm.png` |
| USDCHF | `charts/USDCHF_4H_2026-08-10_tradingview-fxcm.png` |

Each screenshot carries the crosshair on the week-open bar with the date label visible,
so the week under analysis is verifiable from the image itself.

> **On the word "markup".** The instructor's own markups are freehand pen strokes over a
> projected chart. These deliverables are the same analysis expressed numerically — block
> levels, cut bars, extremes, durations — because a number can be checked by a reviewer
> and a pen stroke cannot. The chart images are provided as the visual record; the
> analysis above is what is actually being submitted for review.

---

## 3. ASSIGNMENT 11b — FLASHCARD UPGRADE

> From §2h: open last week's cards in Paint, block out the data to the right of the entry
> candle, annotate with the eight checklist fields, compile a book of longs and a book of
> shorts, identify a signature trade.

**Status: completed to the limit V03's own instructions permit, which is not the whole
assignment. The reason is evidential.**

This assignment operates on **the 40 flashcards V02 asked the student to make**
(`[00:40:57]`). V02's homework 11b was **not completed**, and `V02_HOMEWORK.md` §2 records
why: the cards were to be made from *the student's own winning trades*, and this project
has no trading history. That reason has not changed, so there are no cards to upgrade.

What *can* be done without inventing trade history has been done — the notation standard
itself is recorded, verified against both the slide and the audio, in source notes §2h and
§4c/§4d:

- the eight-field checklist (Time / Position of indicator / Vectors / Asian Range /
  Distance out of Asian range / Type of Trap structure used / W/M / Candle Pattern),
  confirmed printed **and** spoken;
- the construction procedure (open in Paint, black-box everything right of the entry
  candle);
- the matching rule (*"matches… in every aspect including the level of the indicator"*);
- the worked sample card's eleven-line criteria list, transcribed exactly from the slide.

**What is deliberately NOT produced: fabricated flashcards.** Manufacturing example cards
from charts this project never traded would produce exactly the artifact class already
quarantined three times (`Q-001`, `Q-002`, `Q-003`) — plausible-looking, template-shaped,
and not derived from anything real. The assignment is marked incomplete rather than
faked.

**Additionally, six of the sample card's eleven criteria cannot be evaluated at all**, because
their terms are undefined in V01–V03: "3 vectors passed mayo" (A-035, A-020), "Outside
structure" (A-033), "In brinks shadow" (A-030), "TDI below lower support" (TDI deferred by
the course at `[01:01:53]`), "Shark fin" (A-032), "Blood in the water" (A-031). A card
annotated against undefined criteria would record judgement calls as if they were
measurements.

---

## 4. WHAT THIS HOMEWORK ACTUALLY ESTABLISHED

1. **The mechanical part of V03's method is real and reproducible.** Block the first two
   4h bars of the week; you get a definite high and low, on a definite bar, on any feed.
   Four pairs, no ambiguity, no judgement required. This is the most codable thing the
   course has taught in three lessons.
2. **The predictive part is not established.** The dealer cut a side in 4 of 4 and price
   returned inside the block in 4 of 4 — but the direction that followed matched the
   "false move" reading in only 2 of 4. Nothing in V03 tells you in advance which you are
   looking at.
3. **Two taught numbers did not survive contact with four weeks of real data**: the
   2.5–3 day run window (actual 3.7–4.0 days, 4 of 4) and the 3 × ADR target (actual
   1.42×–2.26×, 0 of 4 reached).
4. **The measurement pipeline is now trustworthy in a way V02's was not.** 116 of 116
   bar transitions validated exactly, weekend gaps landed exactly on a 30-bar cadence,
   and two real-hover spot checks matched the harvest to the last decimal.

Point 3 is the one that matters downstream. It does not mean the instructor is wrong —
one week is one week — but it means **no day-count and no ADR multiple should be encoded
from V03**, and the register entries that say so (`C-001`, and the machine candidates
parked in the interpretation file) are correct to say so.

---

## APPENDIX — FULL BAR TABLES (as harvested)

All values are TradingView/FXCM 4h OHLC read from the platform legend as text.
`block` = the first eight hours of the week (bars 0-1).


### EURUSD

Block high **1.15588**, block low **1.15269** (31.9 pips)

| # | Bar start (UTC) | O | H | L | C | Note |
|---|---|---|---|---|---|---|
| 0 | Sun 02 21:00 | 1.15444 | 1.15588 | 1.15350 | 1.15423 | **block** |
| 1 | Mon 03 01:00 | 1.15423 | 1.15457 | 1.15269 | 1.15340 | **block** |
| 2 | Mon 03 05:00 | 1.15340 | 1.15387 | 1.15206 | 1.15226 | L below block |
| 3 | Mon 03 09:00 | 1.15226 | 1.15350 | 1.15167 | 1.15279 | L below block |
| 4 | Mon 03 13:00 | 1.15279 | 1.15350 | 1.15003 | 1.15067 | L below block, **WEEK LOW** |
| 5 | Mon 03 17:00 | 1.15067 | 1.15147 | 1.15013 | 1.15059 | L below block |
| 6 | Mon 03 21:00 | 1.15059 | 1.15149 | 1.15048 | 1.15054 | L below block |
| 7 | Tue 04 01:00 | 1.15054 | 1.15144 | 1.15021 | 1.15102 | L below block |
| 8 | Tue 04 05:00 | 1.15102 | 1.15171 | 1.15037 | 1.15078 | L below block |
| 9 | Tue 04 09:00 | 1.15078 | 1.15233 | 1.15032 | 1.15148 | L below block |
| 10 | Tue 04 13:00 | 1.15148 | 1.15307 | 1.15092 | 1.15186 | L below block |
| 11 | Tue 04 17:00 | 1.15186 | 1.15340 | 1.15186 | 1.15303 | L below block |
| 12 | Tue 04 21:00 | 1.15303 | 1.15354 | 1.15251 | 1.15313 | L below block |
| 13 | Wed 05 01:00 | 1.15313 | 1.15404 | 1.15266 | 1.15361 | L below block |
| 14 | Wed 05 05:00 | 1.15361 | 1.15468 | 1.15311 | 1.15355 |  |
| 15 | Wed 05 09:00 | 1.15355 | 1.15571 | 1.15334 | 1.15455 |  |
| 16 | Wed 05 13:00 | 1.15455 | 1.15569 | 1.15400 | 1.15459 |  |
| 17 | Wed 05 17:00 | 1.15459 | 1.15593 | 1.15426 | 1.15530 | H above block |
| 18 | Wed 05 21:00 | 1.15530 | 1.15596 | 1.15488 | 1.15562 | H above block |
| 19 | Thu 06 01:00 | 1.15562 | 1.15578 | 1.15468 | 1.15488 |  |
| 20 | Thu 06 05:00 | 1.15488 | 1.15515 | 1.15389 | 1.15431 |  |
| 21 | Thu 06 09:00 | 1.15431 | 1.15468 | 1.15364 | 1.15385 |  |
| 22 | Thu 06 13:00 | 1.15385 | 1.15446 | 1.15147 | 1.15205 | L below block |
| 23 | Thu 06 17:00 | 1.15205 | 1.15257 | 1.15172 | 1.15240 | L below block |
| 24 | Thu 06 21:00 | 1.15240 | 1.15240 | 1.15179 | 1.15190 | L below block |
| 25 | Fri 07 01:00 | 1.15190 | 1.15256 | 1.15184 | 1.15235 | L below block |
| 26 | Fri 07 05:00 | 1.15235 | 1.15253 | 1.15177 | 1.15234 | L below block |
| 27 | Fri 07 09:00 | 1.15234 | 1.15808 | 1.15228 | 1.15726 | H above block, L below block, **WEEK HIGH** |
| 28 | Fri 07 13:00 | 1.15726 | 1.15753 | 1.15500 | 1.15589 | H above block |
| 29 | Fri 07 17:00 | 1.15589 | 1.15701 | 1.15537 | 1.15537 | H above block |

### GBPUSD

Block high **1.35063**, block low **1.34639** (42.4 pips)

| # | Bar start (UTC) | O | H | L | C | Note |
|---|---|---|---|---|---|---|
| 0 | Sun 02 21:00 | 1.34858 | 1.35063 | 1.34783 | 1.34873 | **block** |
| 1 | Mon 03 01:00 | 1.34873 | 1.34913 | 1.34639 | 1.34720 | **block** |
| 2 | Mon 03 05:00 | 1.34720 | 1.34780 | 1.34529 | 1.34547 | L below block |
| 3 | Mon 03 09:00 | 1.34547 | 1.34711 | 1.34481 | 1.34640 | L below block |
| 4 | Mon 03 13:00 | 1.34640 | 1.34670 | 1.34224 | 1.34253 | L below block |
| 5 | Mon 03 17:00 | 1.34253 | 1.34343 | 1.34175 | 1.34273 | L below block, **WEEK LOW** |
| 6 | Mon 03 21:00 | 1.34273 | 1.34327 | 1.34190 | 1.34243 | L below block |
| 7 | Tue 04 01:00 | 1.34243 | 1.34329 | 1.34200 | 1.34257 | L below block |
| 8 | Tue 04 05:00 | 1.34257 | 1.34423 | 1.34194 | 1.34421 | L below block |
| 9 | Tue 04 09:00 | 1.34421 | 1.34547 | 1.34361 | 1.34428 | L below block |
| 10 | Tue 04 13:00 | 1.34428 | 1.34561 | 1.34377 | 1.34462 | L below block |
| 11 | Tue 04 17:00 | 1.34462 | 1.34541 | 1.34397 | 1.34505 | L below block |
| 12 | Tue 04 21:00 | 1.34505 | 1.34561 | 1.34390 | 1.34507 | L below block |
| 13 | Wed 05 01:00 | 1.34507 | 1.34598 | 1.34440 | 1.34550 | L below block |
| 14 | Wed 05 05:00 | 1.34550 | 1.34703 | 1.34509 | 1.34564 | L below block |
| 15 | Wed 05 09:00 | 1.34564 | 1.34838 | 1.34548 | 1.34699 | L below block |
| 16 | Wed 05 13:00 | 1.34699 | 1.34861 | 1.34569 | 1.34599 | L below block |
| 17 | Wed 05 17:00 | 1.34599 | 1.34729 | 1.34552 | 1.34677 | L below block |
| 18 | Wed 05 21:00 | 1.34677 | 1.34710 | 1.34522 | 1.34667 | L below block |
| 19 | Thu 06 01:00 | 1.34667 | 1.34725 | 1.34580 | 1.34600 | L below block |
| 20 | Thu 06 05:00 | 1.34600 | 1.34656 | 1.34546 | 1.34642 | L below block |
| 21 | Thu 06 09:00 | 1.34642 | 1.34718 | 1.34520 | 1.34693 | L below block |
| 22 | Thu 06 13:00 | 1.34693 | 1.34794 | 1.34494 | 1.34560 | L below block |
| 23 | Thu 06 17:00 | 1.34560 | 1.34591 | 1.34484 | 1.34529 | L below block |
| 24 | Thu 06 21:00 | 1.34529 | 1.34551 | 1.34395 | 1.34499 | L below block |
| 25 | Fri 07 01:00 | 1.34499 | 1.34564 | 1.34486 | 1.34536 | L below block |
| 26 | Fri 07 05:00 | 1.34536 | 1.34581 | 1.34428 | 1.34429 | L below block |
| 27 | Fri 07 09:00 | 1.34429 | 1.35080 | 1.34341 | 1.34997 | H above block, L below block |
| 28 | Fri 07 13:00 | 1.34997 | 1.35087 | 1.34827 | 1.34961 | H above block, **WEEK HIGH** |
| 29 | Fri 07 17:00 | 1.34961 | 1.35034 | 1.34813 | 1.34839 |  |

### USDJPY

Block high **157.885**, block low **155.228** (265.7 pips)

| # | Bar start (UTC) | O | H | L | C | Note |
|---|---|---|---|---|---|---|
| 0 | Sun 02 21:00 | 157.114 | 157.885 | 155.228 | 156.125 | **block**, **WEEK LOW** |
| 1 | Mon 03 01:00 | 156.125 | 156.644 | 155.426 | 156.464 | **block** |
| 2 | Mon 03 05:00 | 156.464 | 156.986 | 156.326 | 156.985 |  |
| 3 | Mon 03 09:00 | 156.985 | 157.135 | 156.587 | 156.821 |  |
| 4 | Mon 03 13:00 | 156.821 | 157.034 | 156.239 | 156.890 |  |
| 5 | Mon 03 17:00 | 156.890 | 157.224 | 156.676 | 157.142 |  |
| 6 | Mon 03 21:00 | 157.142 | 157.667 | 157.140 | 157.503 |  |
| 7 | Tue 04 01:00 | 157.503 | 157.747 | 157.391 | 157.543 |  |
| 8 | Tue 04 05:00 | 157.543 | 157.840 | 157.498 | 157.802 |  |
| 9 | Tue 04 09:00 | 157.802 | 157.959 | 157.302 | 157.528 | H above block |
| 10 | Tue 04 13:00 | 157.528 | 157.637 | 157.216 | 157.578 |  |
| 11 | Tue 04 17:00 | 157.578 | 157.835 | 157.528 | 157.697 |  |
| 12 | Tue 04 21:00 | 157.697 | 157.809 | 157.449 | 157.557 |  |
| 13 | Wed 05 01:00 | 157.557 | 157.697 | 157.305 | 157.652 |  |
| 14 | Wed 05 05:00 | 157.652 | 157.873 | 157.536 | 157.819 |  |
| 15 | Wed 05 09:00 | 157.819 | 157.865 | 157.416 | 157.630 |  |
| 16 | Wed 05 13:00 | 157.630 | 157.754 | 157.311 | 157.744 |  |
| 17 | Wed 05 17:00 | 157.744 | 157.816 | 157.623 | 157.741 |  |
| 18 | Wed 05 21:00 | 157.741 | 157.758 | 157.557 | 157.726 |  |
| 19 | Thu 06 01:00 | 157.726 | 157.750 | 157.591 | 157.738 |  |
| 20 | Thu 06 05:00 | 157.738 | 157.896 | 157.708 | 157.838 | H above block |
| 21 | Thu 06 09:00 | 157.838 | 157.937 | 157.818 | 157.902 | H above block |
| 22 | Thu 06 13:00 | 157.902 | 158.553 | 157.820 | 158.509 | H above block |
| 23 | Thu 06 17:00 | 158.509 | 158.511 | 158.291 | 158.410 | H above block |
| 24 | Thu 06 21:00 | 158.410 | 158.572 | 158.364 | 158.526 | H above block, **WEEK HIGH** |
| 25 | Fri 07 01:00 | 158.526 | 158.535 | 158.216 | 158.377 | H above block |
| 26 | Fri 07 05:00 | 158.377 | 158.477 | 158.287 | 158.375 | H above block |
| 27 | Fri 07 09:00 | 158.375 | 158.414 | 156.666 | 157.386 | H above block |
| 28 | Fri 07 13:00 | 157.386 | 157.987 | 157.244 | 157.447 | H above block |
| 29 | Fri 07 17:00 | 157.447 | 157.867 | 157.371 | 157.760 |  |

### USDCHF

Block high **0.80947**, block low **0.80552** (39.5 pips)

| # | Bar start (UTC) | O | H | L | C | Note |
|---|---|---|---|---|---|---|
| 0 | Sun 02 21:00 | 0.80552 | 0.80742 | 0.80552 | 0.80685 | **block**, **WEEK LOW** |
| 1 | Mon 03 01:00 | 0.80685 | 0.80947 | 0.80657 | 0.80867 | **block** |
| 2 | Mon 03 05:00 | 0.80867 | 0.80946 | 0.80785 | 0.80893 |  |
| 3 | Mon 03 09:00 | 0.80893 | 0.80938 | 0.80778 | 0.80902 |  |
| 4 | Mon 03 13:00 | 0.80902 | 0.81152 | 0.80863 | 0.81096 | H above block |
| 5 | Mon 03 17:00 | 0.81096 | 0.81148 | 0.80982 | 0.80986 | H above block |
| 6 | Mon 03 21:00 | 0.80986 | 0.81047 | 0.80883 | 0.81017 | H above block |
| 7 | Tue 04 01:00 | 0.81017 | 0.81052 | 0.80963 | 0.81015 | H above block |
| 8 | Tue 04 05:00 | 0.81015 | 0.81062 | 0.80960 | 0.81013 | H above block |
| 9 | Tue 04 09:00 | 0.81013 | 0.81041 | 0.80809 | 0.80884 | H above block |
| 10 | Tue 04 13:00 | 0.80884 | 0.81034 | 0.80799 | 0.81017 | H above block |
| 11 | Tue 04 17:00 | 0.81017 | 0.81024 | 0.80886 | 0.80893 | H above block |
| 12 | Tue 04 21:00 | 0.80893 | 0.80950 | 0.80847 | 0.80890 | H above block |
| 13 | Wed 05 01:00 | 0.80890 | 0.80923 | 0.80740 | 0.80819 |  |
| 14 | Wed 05 05:00 | 0.80819 | 0.81014 | 0.80748 | 0.80982 | H above block |
| 15 | Wed 05 09:00 | 0.80982 | 0.80992 | 0.80826 | 0.80940 | H above block |
| 16 | Wed 05 13:00 | 0.80940 | 0.80940 | 0.80637 | 0.80780 |  |
| 17 | Wed 05 17:00 | 0.80780 | 0.80807 | 0.80658 | 0.80709 |  |
| 18 | Wed 05 21:00 | 0.80709 | 0.80717 | 0.80605 | 0.80652 |  |
| 19 | Thu 06 01:00 | 0.80652 | 0.80749 | 0.80601 | 0.80735 |  |
| 20 | Thu 06 05:00 | 0.80735 | 0.80875 | 0.80715 | 0.80858 |  |
| 21 | Thu 06 09:00 | 0.80858 | 0.81013 | 0.80844 | 0.80982 | H above block |
| 22 | Thu 06 13:00 | 0.80982 | 0.81356 | 0.80884 | 0.81237 | H above block, **WEEK HIGH** |
| 23 | Thu 06 17:00 | 0.81237 | 0.81297 | 0.81155 | 0.81155 | H above block |
| 24 | Thu 06 21:00 | 0.81155 | 0.81292 | 0.81124 | 0.81279 | H above block |
| 25 | Fri 07 01:00 | 0.81279 | 0.81285 | 0.81221 | 0.81263 | H above block |
| 26 | Fri 07 05:00 | 0.81263 | 0.81276 | 0.81090 | 0.81126 | H above block |
| 27 | Fri 07 09:00 | 0.81126 | 0.81131 | 0.80565 | 0.80707 | H above block |
| 28 | Fri 07 13:00 | 0.80707 | 0.80862 | 0.80661 | 0.80769 |  |
| 29 | Fri 07 17:00 | 0.80769 | 0.80820 | 0.80685 | 0.80754 |  |
