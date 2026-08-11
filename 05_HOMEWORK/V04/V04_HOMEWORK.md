# V04 — HOMEWORK

| Field | Value |
|---|---|
| Video ID | V04 |
| Assigned | `[00:16:06]`–`[00:18:36]`, restated `[00:22:46]` and `[00:26:27]` — **by the instructor**, in Segment A |
| Attempted | 2026-08-10 |
| Data source | TradingView, **FXCM** feed, 4-hour and 15-minute. **No login, no account, no paywalled feature, no CAPTCHA encountered or bypassed.** |
| Charts | `05_HOMEWORK/V04/charts/` (8 files, rendered from the committed data — not screenshots) |
| Raw data | `05_HOMEWORK/V04/data/v04_week_2026-08-02_4h_and_15m.json` — 120 × 4h bars + **1,916** × 15m bars, exact OHLC (**1,916, not 1,920**: USDCHF's week opens with a partial 4h bar of twelve 15m bars — §1.2 validation 3) |
| Scripts | `05_HOMEWORK/V04/scripts/` — both harvesters, plus `verify_reconstruction.py` |
| Week analysed | **Sun 02 Aug 2026 21:00 UTC → Fri 07 Aug 2026 17:00 UTC** (30 × 4h bars per pair) |

**Completed on real data. No substitution was needed.**

---

## 0. THE ASSIGNMENT, AS GIVEN

Quoted rather than paraphrased, because the grading depends on exactly what was asked:

> `[00:16:06]` *"Look at the four hour chart."*
> `[00:16:11]` *"Block off the first eight hours that draw a line all the way across your chart."*
> `[00:16:15]` *"Those are your psychological support and resistance levels."*
> `[00:16:18]`–`[00:16:19]` *"Go look at these charts. It's the homework this week."*
> `[00:18:00]` *"But I want you to do the assignment in the four hour chart."*
> `[00:18:04]` *"The four majors, any time range."*
> `[00:18:07]`–`[00:18:14]` *"I want you to start to understand the psychological support and resistance levels that the dealer creates in the first eight hours of the week."*
> `[00:18:24]`–`[00:18:28]` *"Mark the chart, try to identify the high of the week and the low of the week and trade away from those areas."*
> `[00:18:33]`–`[00:18:36]` *"Drill down to a 15 minute chart. Remember many view and start to identify the pattern within the pattern."*

Four deliverables: **(A)** the first-eight-hours block on the 4h chart, for **(B)** the four
majors, **(C)** the high and low of the week identified, **(D)** the 15-minute sub-pattern
at those extremes.

### Why no substitution was needed

*"The four majors, **any time range**"* `[00:18:04]`. As in V03, the instructor delegates
the date choice to the student, so using a recent week is **compliance with the
assignment, not a departure from it**. The most recent *complete* trading week at the time
of work was used.

### Two choices this session made, and they are the student's, not the course's

1. **"The four majors" = EURUSD, GBPUSD, USDJPY, USDCHF.** The instructor never enumerates
   them. This is the conventional set and it is the same four V03's homework used, which
   makes the two lessons' results directly comparable. **It is a choice, and a reviewer
   may disagree with it.**
2. **"The first eight hours of the week" = the first two 4-hour bars of the week on this
   feed**, i.e. Sun 21:00 → Mon 05:00 UTC. This follows V03's reading (`I2` there) and is
   **feed-dependent** — `A-019` (no timezone stated anywhere in the course) is still open,
   so a broker whose week opens at a different hour would block off a different eight
   hours.

---

## 1. METHOD

### 1.1 No price is read from a pixel

Every number below is **TradingView's own OHLC legend, read as DOM text.** The chart is
driven with synthetic mouse moves across the price pane; after each move the legend string
(`O … H … L … C …`) is parsed. The legend is the platform's report of the hovered bar, not
an interpretation of an image.

This is the V02 `MAJOR` (`E06`/`E19`) lesson applied: there, a price line rendered in the
same colour as bullish candles corrupted a pixel-based read. **Nothing here depends on a
colour.**

The eight chart images in `charts/` are **rendered from the committed JSON**, not
screenshots. They exist to be looked at; **no measurement is taken from them.**

### 1.2 Four independent validations were run

**1 — The open-equals-previous-close chain.** Within a trading week each 4h bar's open must
equal the prior bar's close.

**Over the committed data — 4 pairs × 30 bars = 116 transitions — the chain is
116/116 continuous, zero breaks.** That is the reproducible half of this test and it is
the half that matters: it is the evidence that the week slice used everywhere below is
one unbroken trading week and contains no weekend. `scripts/verify_reconstruction.py`
recomputes it from the committed JSON.

> **REPRODUCIBILITY CAVEAT — added 2026-08-11 per V04 review R1 finding `M5` (`E20`).**
> This paragraph originally reported **569 bar transitions, 549 continuous, 20 breaks**,
> with break indices **15, 45, 75, 105, 135** and a GBPUSD exception at index **143**,
> computed over the four pairs' **full ~144-bar harvests**. Those harvests are **not in
> this repository** — the committed JSON holds only the 30-bar week per pair, so a reader
> has 116 transitions available, not 569. **The 569 / 549 / 20 figures therefore cannot be
> independently re-verified from what is committed, and they are marked UNREPRODUCED.**
>
> They are not withdrawn and no downstream number depends on them: their only role was to
> locate the week boundary, and the same boundary is established by the committed data
> alone (116/116 continuous within the week, and V03's independently harvested dataset for
> the same week agrees on 476/480 fields — validation 2). `LOG.md` records this count
> being corrected 571 → 569 by recomputation during the session, so this is a
> **reproducibility** defect, not an accuracy one.
>
> **Why the arrays are not simply committed instead.** The full harvests were held in
> session memory and were not written to disk; re-harvesting today would produce a
> *different* dataset (a later "current bar", possibly revised feed values) and committing
> it would mean re-deriving every figure in this file from data the original claims were
> never computed on. Disclosing the gap is the honest option and is what is done here.
> This is the same promise `REVIEW_INDEX` open item 13 records against V02 §1.1.

For the record, the shape of the unreproduced result: every break but one fell on the
**30-bar cadence** — indices 15, 45, 75, 105, 135 (30 × 4h = 120 h = one five-day FX
week). The one exception was a GBPUSD break at index 143, the last bar of the harvest,
which is the still-forming current bar at the edge of the data and not a weekend. This is
V02's R2/R3 finding used as a positive test: continuity is *expected* to hold within a
week and *expected* to break at weekends, and it did exactly that.

USDCHF again showed only four breaks rather than five — its final weekend gap is genuinely
zero to five decimals, the same behaviour V03 recorded. **Its week boundary is taken from
the 30-bar cadence the other three pairs establish**, and that is disclosed rather than
hidden. *(USDCHF's week boundary needed a second correction on the 15-minute side — see
validation 3.)*

**2 — Cross-check against V03's independently committed dataset.** V03's homework covered
the same calendar week and the same four pairs, harvested in a different session by a
different script. This session's committed 4h data agrees with it on **476 of 480 OHLC
values (99.17%)**:

| Pair | Bars identical | Fields differing |
|---|---|---|
| EURUSD | 30/30 | none |
| GBPUSD | 29/30 | bar 29 high, by 0.1 pip |
| USDJPY | 29/30 | bar 29 low, by 0.1 pip |
| USDCHF | 28/30 | bar 27 low and bar 28 high, ≤ 0.4 pip |

All four differences are **≤ 0.4 pip, all in highs/lows, all in the final three bars of the
week, and none touches a weekly extreme.** Every open and every close matches exactly.

**3 — The 15-minute series reconstructs the 4-hour series.** Sixteen 15m bars aggregate to
one 4h bar. Aggregating the independently harvested 15m data and comparing against the
independently harvested 4h data:

| Pair | 4h bars reconstructed exactly | OHLC fields | Residual differences |
|---|---|---|---|
| EURUSD | **30/30** | 120/120 | — |
| USDJPY | **30/30** | 120/120 | — |
| GBPUSD | 28/30 | 118/120 | bar 22 low (0.1 pip), bar 29 high (0.1 pip) |
| USDCHF | 28/30 | 118/120 | bar 27 low (0.3 pip), bar 28 high (0.1 pip) |

**476 of 480 fields (99.17%).** Two harvests, two timeframes, two browser sessions,
reconstructing each other. **All four residual differences are ≤ 0.3 pip, all in highs or
lows, never in an open or a close** — which is exactly the signature of the ±0.4 pip dwell
defect measured in validation 4, and three of the four are the same fields validation 2
found differing against V03's independent dataset.

This is also what **anchors the 15m series to the calendar week** — the alignment offset
was found by maximising this reconstruction, not by reading a date label. The offsets are
**262, 261, 261, 265** (EURUSD, GBPUSD, USDJPY, USDCHF); the first three agree because the
three pairs share one week open, and USDCHF's differs for the reason set out immediately
below.

#### USDCHF's 4-hour week opens with a PARTIAL bar of twelve 15-minute bars

> **CORRECTED 2026-08-11 per V04 review R1 finding `M1` (`E19`). This paragraph previously
> reported USDCHF at 27/30 and attributed the difference to the ±0.4 pip dwell defect.
> That attribution was wrong, and the error it hid was two orders of magnitude larger.**

On this feed **USDCHF's first 4-hour bar of the week contains only twelve 15-minute bars**
— the pair's quoting session opens an hour later than the other three majors. The 15m
slice was originally cut with a fixed **sixteen-bars-per-4h-bar** assumption, so it began
four bars too early. The consequences, all recomputed from the committed data:

- The committed 480-bar slice at `offset_in_harvest = 261` carried **four previous-week
  bars at its head**.
- Those four bars dragged the **weekend gap inside the week**: a **−12.7 pip**
  discontinuity at `m[3] → m[4]`, which was the **only** 15m discontinuity anywhere in the
  1,920 bars as then committed.
- The reconstruction of 4h bar 0 therefore missed on the **open by 28.1 pips** and on the
  **high by 12.8 pips**. **An open can never differ by dwell latency** — validation 4 says
  so explicitly, and that contradiction is what should have caught this at the time. **The
  test worked; the diagnosis failed.**

**The fix, and it is exact.** Dropping the four leading bars leaves
**476 = 12 + 29 × 16** bars, which is the *complete* week for this pair — nothing was
missing from the tail. `aggregate(m[0:12])` now reproduces 4h bar 0 on **all four fields
exactly**, and USDCHF rises from 27/30 to **28/30**, its two residuals now genuinely in
the ±0.4 pip class. The committed JSON is re-sliced (`offset_in_harvest = 265`,
`bars_15m_week` length 476, `j_hi_15m` / `j_lo_15m` re-indexed), and every pair now carries
an explicit **`bars_15m_in_4h_bar_0`** field (16, 16, 16, **12**) so the aggregation is
reproducible rather than assumed.

**This is a limit of the 15-minute pipeline, and it is the pipeline V05 would inherit.**
Any future session slicing a 15m week by a fixed bar count must read
`bars_15m_in_4h_bar_0` rather than assume 16, and must assert zero in-week discontinuities
before trusting the slice — `scripts/verify_reconstruction.py` does both and is committed
for that purpose.

**No conclusion in this file changes.**

- The **4-hour data was never affected** — it is clean and continuous, 116/116, and every
  block figure, weekly extreme and duration in §2 and §3 is computed from it.
- USDCHF's week low is still `0.80552` at 4h bar 0, present in the corrected 15m series at
  `m[0]`.
- USDCHF is **already outside the scoped 2-of-4 result** in §3.2 — excluded because its
  week low falls on the week-open bar, where no anchor can have formed. That exclusion is
  a 4-hour fact and is **unchanged by this correction**.
- The §3.3 swing-descriptor windows are unchanged: the extreme's index and the 44-bar
  window shifted together by exactly four bars, so the bars examined are the same bars.
  Recomputed and confirmed identical.

**4 — A deliberate stability test of the harvest itself, which found a real defect.** The
4h harvest was run twice, at a 28 ms and a 75 ms hover dwell. The two runs disagree on
**5 of 480** OHLC fields — always a high or a low, never an open or a close — because the
legend updates asynchronously and a short dwell can latch a stale value. **The 75 ms run
is the committed one**, and it is the run that agrees with V03. This is recorded rather
than quietly discarded: it is a real limit on the method's precision, at roughly **±0.4
pip on extremes of individual bars**.

### 1.3 What is NOT validated

- **No timestamp is independently confirmed.** The crosshair date label is drawn on a
  canvas, not in the DOM, so it could not be harvested. The week is pinned by the 30-bar
  weekend cadence and by agreement with V03's dataset (whose week *was* confirmed against a
  crosshair label reading `Sun 02 Aug '26 21:00`). **Day-of-week labels below are derived
  from that anchor by arithmetic, not read off the chart.**
- **The FXCM feed is one broker's.** Weekly extremes differ by a pip or two between feeds.
- **`A-019` is unresolved**, so "the first eight hours of the week" is feed-relative.
- **The full 4h harvests behind validation 1's 569 / 549 / 20 continuity figures are not
  committed**, so those three numbers are **unreproduced** — see the caveat in validation
  1. Everything else in this file recomputes from the committed JSON.
- **The 15m week slice depends on a per-pair first-bar length** (`bars_15m_in_4h_bar_0`),
  not on a fixed 16. USDCHF's is 12. This was found by review, not by this session — see
  validation 3.

---

## 2. DELIVERABLE A/B/C — THE BLOCK, AND THE WEEK'S HIGH AND LOW

Week of **Sun 02 Aug 2026 21:00 UTC → Fri 07 Aug 2026 17:00 UTC**. Bar 0 = Sun 21:00 UTC;
bar *i* covers Sun 21:00 + 4*i* hours.

### 2.1 The first-eight-hours block (bars 0–1)

| Pair | Block high | Block low | Block size | Week range | Block as % of week |
|---|---|---|---|---|---|
| EURUSD | 1.15588 | 1.15269 | **31.9 pips** | 80.5 pips | 39.6% |
| GBPUSD | 1.35063 | 1.34639 | **42.4 pips** | 91.2 pips | 46.5% |
| USDJPY | 157.885 | 155.228 | **265.7 pips** | 334.4 pips | 79.5% |
| USDCHF | 0.80947 | 0.80552 | **39.5 pips** | 80.4 pips | 49.1% |

> **USDJPY's block is anomalous and is not swept under the rug.** 265.7 pips in eight hours,
> 79.5% of the entire week's range, is not a normal Asian accumulation. Its block low
> (155.228) *is* the week's low, set in the very first bar. This pair does not look like the
> lesson's picture, and saying so is part of the answer.

### 2.2 High and low of the week

| Pair | Week high | 4h bar | When (derived) | Week low | 4h bar | When (derived) |
|---|---|---|---|---|---|---|
| EURUSD | 1.15808 | 27 | Fri 09:00 UTC | 1.15003 | 4 | Mon 13:00 UTC |
| GBPUSD | 1.35087 | 28 | Fri 13:00 UTC | 1.34175 | 5 | Mon 17:00 UTC |
| USDJPY | 158.572 | 24 | Thu 21:00 UTC | 155.228 | **0** | Sun 21:00 UTC |
| USDCHF | 0.81356 | 22 | Thu 13:00 UTC | 0.80552 | **0** | Sun 21:00 UTC |

**Neither extreme fell inside the first-eight-hours block for EURUSD or GBPUSD.** For
USDJPY and USDCHF the week's low is the **week-open bar itself**.

---

## 3. WHAT THE WEEK SAYS ABOUT THE LESSON'S CLAIMS

### 3.1 *"The dealer is going to wear a track to the high on Sunday or Monday"* `[00:18:46]`

Taking *"Sunday or Monday"* as bars 0–6 (Sun 21:00 → Mon 21:00 UTC):

| Reading | Result |
|---|---|
| **Literal — the week's HIGH forms Sun/Mon** | **0 of 4** |
| Mirror — the week's LOW forms Sun/Mon | **4 of 4** |

**This week the early extreme was the low in all four pairs, and the high was made late
(Thu/Fri) in all four.** Three of the four pairs closed up on the week (+9.3, +64.6, +20.2
pips; GBPUSD −1.9).

**What this does and does not show.** It does **not** refute the instructor: he is
describing a down-week shape, and a symmetric reading ("an extreme forms early and price
trades away from it") holds 4 of 4. It does show that **the direction is not fixed**, which
the lesson's phrasing does not say. One week is one week — this is a single observation,
not a sample.

**Scope discipline (`REVIEW_INDEX` open item 20 / V03 `M3`).** For USDJPY and USDCHF the
early extreme is the **week-open bar**, where no anchor could have formed before it — the
"extreme" is just where trading started. Counting those as confirmations is exactly the
over-scoping V03's review charged. **The supported count for the mirror reading is 2 of 4**
(EURUSD bar 4, GBPUSD bar 5), not 4 of 4.

### 3.2 *"Now you trade away from the high of the week for two and a half to three days"* `[00:20:28]`

Measuring from the early extreme to the opposite extreme:

| Pair | From bar | To bar | Bars | **Days** | Formed anchor? |
|---|---|---|---|---|---|
| EURUSD | 4 | 27 | 23 | **3.83** | **YES** |
| GBPUSD | 5 | 28 | 23 | **3.83** | **YES** |
| USDJPY | 0 | 24 | 24 | 4.00 | NO — week-open bar |
| USDCHF | 0 | 22 | 22 | 3.67 | NO — week-open bar |

**Scoped result: 2 of 4 measure the taught object, and both give 3.83 days — exceeding the
2.5–3 day window.** All four exceed it under any reading, but only two are admissible.

> **This independently reproduces V03's corrected finding.** V03 R1's `M3` required that
> finding be re-scoped from "4 of 4" to "2 of 4 (both 3.8 days, still exceeding)". This
> session measured the same week from a **freshly harvested** dataset and a
> **separately written** script, and got **the same two pairs and the same 3.83 days**.
> That is a reproduction, not a citation.

**Effect on `C-001`: NONE. No day-count value is committed anywhere.** Two observations
from one week cannot adjudicate a source-level conflict, and the instructor's own
terminating condition — *"until the dealer issues another signal"* — is undefined, so
"3.83 days" may simply mean the signal came later that week.

### 3.3 Deliverable D — the 15-minute sub-pattern at the weekly extreme

> `[00:18:52]`–`[00:18:58]` *"within that pattern on a 15 minute chart, you will see an M or
> W formation. That formation will coincide with the high of the week will be the high of
> the day."*

**A classification is deliberately not attempted.** `A-011` records that **"M formation" is
undefined across V01–V04** — no leg count, no symmetry tolerance, no time gap, no depth
requirement is ever stated, and V04 itself tolerates *"a pre-school M or maybe a
kindergarten"* `[01:12:09]`. Writing a detector here would invent the definition the course
withholds and then grade the course against my own invention (`E15`, `E18`). 

Instead: an **objective descriptor**, reported across four tolerances so it cannot be
tolerance-fitted. A "swing high" is a bar whose high exceeds both neighbours; the window is
the 44 bars (11 hours) up to and including the extreme.

**At the weekly HIGH — distinct swing highs within X pips of it:**

| Pair | ≤2 pips | ≤5 | ≤10 | ≤20 | Gap to the 2nd-highest peak |
|---|---|---|---|---|---|
| EURUSD | **1** | 1 | 1 | 1 | — |
| GBPUSD | **2** | 2 | 2 | 2 | 30 min |
| USDJPY | **2** | 4 | 10 | 13 | 510 min |
| USDCHF | **1** | 1 | 1 | 1 | — |

**At the weekly LOW — distinct swing lows within X pips of it:**

| Pair | ≤2 pips | ≤5 | ≤10 | ≤20 | Note |
|---|---|---|---|---|---|
| EURUSD | **2** | 2 | 3 | 6 | formed anchor |
| GBPUSD | **1** | 3 | 4 | 4 | formed anchor |
| USDJPY | 1 | 1 | 1 | 1 | extreme is the week-open bar |
| USDCHF | 1 | 1 | 1 | 1 | extreme is the week-open bar |

**And what the charts actually look like, having looked at all eight:**

- **EURUSD at the high** (`EURUSD_15m_week-high…png`): a **single near-vertical green bar**
  into the high, then immediate decline. One touch. There is no two-peak structure of any
  kind.
- **GBPUSD at the high**: same shape — one large vertical bar — but the two bars *after* it
  hold within 2 pips of the extreme, giving **two separated touches 30 minutes apart.**
- **USDCHF at the high**: a steady rise into a single top, then sideways. One touch.
- **USDJPY at the high**: the only chart with a genuinely **multi-peak** approach — a long
  band of roughly equal highs over ~9 hours, the last of which is the extreme.
- **EURUSD at the low**: a decline into the low, then a **retest within 2 pips a few bars
  later**, then the rise — the closest thing in the set to a textbook double bottom.

**Honest reading:** on this week, at the weekly high, **a two-touch structure is present in
at most 2 of 4 pairs, and in only 1 of 4 (GBPUSD) with a tight time gap**; the modal shape
is a **single vertical spike**, which is not an M under any reading. At the weekly low the
picture is better — EURUSD in particular shows a clean two-touch — but only 2 of the 4 lows
are formed anchors at all.

**A caveat that matters more than the counts.** The instructor's claim is *compound*: the
dealer tracks to the high **on Sunday or Monday**, and *that* extreme carries the 15m M.
Since §3.1 found the high never formed Sun/Mon this week, **the object his claim is about
did not occur**, and testing the 15m structure at a late-week high is testing something
adjacent to, not identical with, what he said. The counts above are reported for what they
are.

---

## 4. WHAT WAS NOT DONE, AND WHY

| Item | Status | Reason |
|---|---|---|
| Post the marked charts in the 2012 forum | **NOT APPLICABLE** (D-018 test: no subject matter for a present-day agent) | The forum thread is a 2012 artifact. Note `A-041`: the instruction as transcribed is internally inconsistent anyway |
| Compare against the instructor's **answer key** | **BLOCKED** | He promises to post one `[00:26:41]`; it is not in the library. **This is why no label below is graded — there is nothing to grade against**, exactly as in V02 |
| Apply V04's **entry rule** to this week | **DEFERRED, not attempted** | Condition (c) requires TDI, which the course has never taught (`A-039`). Testing a two-condition version of a three-condition rule and calling it the instructor's rule would be `E06`/`E18`. See the mastery report, dimension G |
| Next week's assignment | Not applicable | Drafted and withheld on air, `[00:17:15]`–`[00:17:33]` |

---

## 5. SUMMARY OF FINDINGS

1. The first-eight-hours block was measured for all four majors on real 4h data:
   **31.9 / 42.4 / 265.7 / 39.5 pips**, i.e. **39.6% / 46.5% / 79.5% / 49.1%** of each
   pair's weekly range. USDJPY is a clear outlier and is flagged, not smoothed.
2. The week's high and low were identified for all four. **The high formed late (Thu/Fri) in
   4 of 4; the low formed Sun/Mon in 4 of 4.** The literal claim (*high* on Sun/Mon) is
   **0 of 4** this week.
3. Duration from the early extreme to the opposite extreme: **3.83 days on the 2 pairs with
   a formed anchor**, exceeding the stated 2.5–3 day window. **Independently reproduces
   V03's corrected `M3` figure** from a fresh harvest. **`C-001` unaffected; no day-count
   value committed.**
4. On the 15-minute chart the modal shape at the weekly high is a **single vertical spike**,
   not a two-peak structure. **No M/W classification is claimed**, because the course has
   never defined one (`A-011`).
5. Method quality: **476/480** OHLC fields agree with V03's independent dataset;
   **476/480** agree between this session's own 4h and 15m harvests. A harvest-stability
   defect was found, measured (±0.4 pip on individual bar extremes) and disclosed.
6. **Two defects were found by review and corrected on 2026-08-11** (V04 R1 `M1`, `M5`):
   USDCHF's 15-minute week was mis-sliced at a **partial** week-open 4h bar of twelve 15m
   bars, and the symptom was misdiagnosed as harvest noise (§1.2 validation 3); and
   validation 1's 569 / 549 / 20 continuity figures are **not reproducible** from the
   committed data and are now marked as such (§1.2 validation 1). **Neither changes any
   conclusion above** — both live on the 15-minute side or in the harvest-wide narrative,
   and every figure in §2 and §3 is computed from the 4-hour data, which is unaffected and
   continuous 116/116.

**Nothing here is graded**, because no answer key exists. These are observations, not
scored answers.
