# PT-022 — "They don't usually run like London": is the New York session's realised range smaller than London's?

```text
STATUS:      SUPERSEDED — PERIOD UNOBTAINABLE. RE-ISSUED AS PT-023, 2026-08-13.
             NOT RUN. NOT EDITED INTO CONFORMANCE. Retained exactly as pre-registered.

             WHY: this file pre-registered W-A (2015-01-04 -> 2015-12-31) as its period,
             with a fallback of "the oldest contiguous 12 calendar months of 15-minute
             history the feed provides". BOTH are unobtainable. The declared feed
             (TradingView, FXCM) serves 15-minute GBP/USD history back to 2026-05-31
             ONLY -- about 2.5 months. Measured 2026-08-13 by walking the chart back
             368 drags until the left edge stopped moving for six consecutive drags
             (probe_back.mjs; DATES ONLY were read, no price).

             D-027 is explicit that changing a range creates a NEW TEST ID and that the
             abandoned test is retained and marked. That is what has happened. PT-023
             carries the same question, the same nulls, the same seed and the same
             decision rules, on a period that exists -- and declares, as costs rather
             than as details, everything the substitution loses.

             NOTHING IN THIS FILE WAS CHANGED except this status block.

--- original status block, as pre-registered and committed at 582859e ---
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
ATTESTATION: The session that wrote this file had, at the moment of writing, opened NO
             chart in any period before 2026-07-30, loaded NO price series predating
             2026-07-30, and inspected NO outcome data of any kind for this test. It HAD
             previously seen 2026-07-30..2026-08-13 data while performing V06's homework;
             that period is EXCLUDED from this test's window by construction and by the
             D-028 holdout, and the exclusion is stated here rather than discovered later.
             The period, the windows, the two outcomes, the two nulls, the seed and the
             four decision rules below were all fixed before any 2015 or 2016 bar was
             requested. That is the whole value of this file.
SCOPE:       GUEST claim. Tested under D-032, excluded from doctrine under D-025.
```

Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`
Shared machinery: `COMMON_PROTOCOL.md` (units, no-pixel rule, `D-031` arms, null models, seed)
Decisions: `D-007` instrument · `D-025` guest exclusion · **`D-032` guest material may be tested** ·
`D-026`/`D-029` baseline · `D-027`/`D-028` period & holdout · `D-030` no approximated definitions ·
`D-031` timezone arms

---

## 0. WHY THIS TEST EXISTS AT ALL, GIVEN `D-025`

`PRE_REGISTERED/INDEX.md` records **V06 — none — `D-025`**, and that was correct when written.
The project owner directed on 2026-08-13 that V06 receive a genuine pre-registered manual
backtest. `D-032` records the direction and the fence: **guest material may be tested, never
adopted; a test is not a citation.**

**This test does not test the Market Maker Method.** It tests one arithmetic claim, made by a
guest presenter, about the relative size of two session windows. Nothing about the anchor, the
pushes, the levels, the patterns or the entries is measured, and nothing here may be cited for
or against any statement by the course's author. See §8, which is mandatory and verbatim.

---

## 1. WHY THIS CLAIM AND NOT ANOTHER FROM V06

V06 states the most nearly complete trading system in the corpus. **Almost all of it is
untestable**, and not because of `D-025` — because of `D-030`:

| V06 claim | Blocked by |
|---|---|
| *"Each push is approximately ADR divided by 3"* `[00:05:45]` | *push* undefined; ADR's lookback undefined (`A-038`). V06's homework measured that the lookback alone moves the answer 31–60% |
| *"The pull marks [pullbacks] are usually 25 to 50 pips"* `[00:06:04]` | *pullback* undefined |
| *"If you can name the pattern, you can take the trade"* `[00:08:00]` | *nameable pattern* undefined (`A-044`), and the printed DMR list disagrees with the spoken one |
| *"they normally bounce off the 200 first, then the 50, then the 13"* `[00:55:17]` | the moving averages' **type** (EMA vs SMA) is stated nowhere in V01–V06 (`A-020`) |
| the two-hour time stop `[00:13:19]`, `[00:23:36]` | requires an entry, which requires the above |
| *"you get only two pushes"* counter-trend `[00:37:45]` | *push* undefined |

**One claim survives, and it survives cleanly:**

> *"U.S. session you're looking for anywhere from 30 to 50 pips."* `[00:31:14]`
> *"Whatever you're comfortable with."* `[00:31:18]`
> **"They don't usually run like London."** `[00:31:20]`

It needs no pattern, no indicator, no entry and no judgement call. It needs two session windows
and the arithmetic of a high minus a low.

---

## 2. THE QUESTION

> Within a trading day, is the realised price range of the **New York** session window smaller
> than the realised price range of the **London** session window?

**Null hypothesis: it is not.** The two windows are exchangeable — the difference between them
is what you would get from any two windows of the same lengths placed anywhere on the same
price path.

### 2a. A mechanical bias that runs AGAINST the claim, stated before the result

The V02 printed table makes **London 3:30am–9:00am (5.5 h)** and **New York 9:30am–5:00pm
(7.5 h)**. A longer window mechanically contains a larger range. **The New York window is
36% longer**, so the arithmetic is biased *towards* New York having the bigger range — which is
the opposite of what the guest claims.

**Therefore a confirmation of this claim is harder to obtain than it looks, and a contradiction
is easier.** This asymmetry is pre-registered here so that neither outcome can be presented as
more impressive than it is, and it is why §4 carries a duration-normalised outcome (`O1b`)
alongside the raw one.

---

## 3. THE OPERATIONALISATION, AND ITS ONE HONEST WEAKNESS

**V06 states no clock time for any session.** `EST` occurs 0×; no hour is attached to Asia,
London or the US anywhere in its 74 minutes, and no session clock appears on any of its 32
curated frames. `A-019` is untouched by V06 — a sixth consecutive lesson of silence.

So the windows come from the **V02 printed slide**, which is **instructor** material and is the
same table `PT-002`…`PT-021` use:

```text
5pm            High / Low Reset (The MM Spread Is Set)
5pm – 8pm      Dead Gap
Asian Session  8:30pm – 3:00am     Gap 3:00–3:30
London Session 3:30am – 9:00am     Gap 9:00–9:30
New York       9:30am – 5pm
```

> ### ⚠ THE WEAKNESS, PRE-REGISTERED RATHER THAN DISCOVERED
>
> **The claim is the guest's; the windows are the instructor's.** If the guest meant something
> different by *"London"* and *"the U.S. session"* than the instructor's printed table, then
> this test measures the instructor's windows and not the guest's intent, and **a null result
> would be ambiguous between "the claim is false" and "the windows are wrong".**
>
> This cannot be resolved from source — the guest never gives a clock. It is recorded as a
> **limitation of the test**, it is repeated in §8, and it constrains what any result licenses.
> A **confirmation** is less affected than a null: if two windows chosen by someone else still
> reproduce the guest's claimed ordering, that is a stronger result than if he had specified
> them himself.

---

## 4. PRE-REGISTRATION — FIXED BEFORE ANY BAR IN THE WINDOW WAS REQUESTED

| Field | Value |
|---|---|
| Instrument | **GBP/USD only** (`D-007`) |
| Timeframe | **15-minute.** Required: the 3:30 and 9:30 boundaries do not fall on hourly marks |
| Pip | `0.0001` |
| Data source | **TradingView, FXCM feed**, harvested by `05_HOMEWORK/V06/scripts/tv_harvest_v06.mjs` — OHLC read from the platform's **Data Window DOM text**, never from a pixel (`COMMON_PROTOCOL.md` §2) |
| Chart timezone | Recorded from the harvest and stated in the observation. It is the input to the two arms, not a detail |
| Period — primary | **W-A: 2015-01-04 → 2015-12-31**, the window `COMMON_PROTOCOL.md` §3 pre-registered on calendar grounds before any chart was opened |
| Period — **pre-registered fallback** | If the feed's 15-minute history does not reach W-A, use **the oldest contiguous 12 calendar months of 15-minute history the feed provides**, provided it lies wholly inside the `D-028` DEVELOPMENT block. The fallback is fixed **now**, on availability grounds alone, so that the period cannot be chosen after seeing a result. Any use of it is declared in the observation as a **deviation** |
| Holdout | `D-028` 70/30. The boundary is **pinned from the actual available range before any bar in the test window is examined**, and appended to `D-028`. The test window must lie **wholly inside DEVELOPMENT**; if it does not, the test is re-issued under a new PT number and this file is retained and marked |
| London window | **03:30–09:00** inclusive of 03:30, exclusive of 09:00 |
| New York window | **09:30–17:00** inclusive of 09:30, exclusive of 17:00 |
| Timezone arms | **Both**, always (`D-031`): **A** = fixed `UTC−5`; **B** = `America/New_York`, DST-aware |
| Day inclusion | A day is **included** iff **both** windows contain ≥ 1 bar. Days failing that are **excluded, counted, and reported** — a mechanical rule, fixed now |
| Exclusions | **None otherwise.** No day is dropped for being a holiday, an outlier, a news day, or anything else. Dropping one is `E09` |
| Sample target | ≥ 30 included days (`BACKTEST_EVIDENCE_STANDARD.md` §4.1). W-A should yield ~250 |

### 4a. The two pre-registered outcomes

| ID | Definition |
|---|---|
| **O1 — primary, raw** | Per included day, `D = range(London) − range(NY)` in pips, where `range(W) = max(high of bars in W) − min(low of bars in W)`. Reported: median `D`, mean `D`, and **`f = fraction of days with D > 0`** with a 95% interval |
| **O1b — duration-normalised** | The same, on **pips per hour**: `Dn = range(London)/5.5 − range(NY)/7.5`. This separates *"the window is shorter"* from *"the market is quieter"*. **Both O1 and O1b are reported whatever they show** |
| **O2 — secondary, descriptive only** | Fraction of included days whose **New York** window range reaches **≥ 30 pips** and **≥ 50 pips** — the guest's own stated target band `[00:31:14]`. Descriptive; no baseline; reported with an interval and no verdict |

### 4b. What is NOT measured, and will not be added later

No entry, no exit, no direction, no stop, no target, no hit rate, no expectancy. **This test has
no trades in it.** It is a distributional comparison of two windows. Adding an entry rule after
seeing `O1` would be a different test and would need a new PT number.

## 5. BASELINES — `D-026` / `D-029`, RUN BEFORE THE RULE ARM'S AGGREGATE IS READ

| ID | Null | Holds constant | Randomizes | Iterations | Seed |
|---|---|---|---|---|---|
| **N-P** | **Paired sign-flip permutation.** Under exchangeability the sign of each day's `D` is random | every day's pair of window ranges | the sign of each day's `D`, independently | 1,000 | `20260812` |
| **N2** | **Circular clock shift** (`COMMON_PROTOCOL.md` §5). Both window labels are shifted together by one offset drawn uniformly from ±12 h in 15-minute steps, wrapping within the day; ranges recomputed | the entire price path, unaltered; both window **lengths** | *where on the clock* the two windows sit | 1,000 | `20260812` |

**Why both.** `N-P` asks *"is the observed asymmetry bigger than chance given these two
windows?"*. `N2` asks the harder and more interesting question: *"is it these particular hours,
or would any 5.5 h window beat any 7.5 h window placed 6 h later?"* **A result that passes `N-P`
and fails `N2` means the asymmetry is real but not about London and New York** — and that
distinction is the reason `N2` is in `COMMON_PROTOCOL.md` at all.

The seed is the batch's fixed `20260812`, pre-registered so seed-shopping is impossible.

## 6. DECISION RULES — FIXED NOW, IN ADVANCE OF THE DATA

Stated as four exhaustive outcomes so that no post-hoc reading is available:

| Verdict | Condition |
|---|---|
| **CONFIRMED AS TAUGHT** | median `D` > 0 **and** `f` above the 95th percentile of **both** nulls, in **both** `D-031` arms |
| **CONTRADICTED AS TAUGHT** | median `D` < 0 **or** `f` below the 5th percentile of **both** nulls, in **both** arms |
| **INDISTINGUISHABLE FROM THE NULL** | anything else with n ≥ 30 |
| **SAMPLE INSUFFICIENT** | n < 30 — descriptive only, and no fraction quoted anywhere without that label in the same sentence |

**Arm divergence is a finding, reported in full, and is never a selection criterion**
(`D-031`; reporting only the better arm is `E09` + `E24`).

**`O1` and `O1b` may disagree.** If they do, **both are reported and neither is preferred**;
the disagreement is itself the result, and it means the guest's claim is true of *windows* and
false of *market activity*, or the reverse.

## 7. WHAT EACH OUTCOME WOULD MEAN

| Result | Reading — and its limits |
|---|---|
| **CONFIRMED** | One arithmetic claim by one coach, about GBP/USD in one year, using the instructor's session windows, survives two nulls. **It is not evidence that the method works, that pushes exist, or that the instructor endorses the claim.** It is a fact about session ranges |
| **CONTRADICTED** | The claim is false on this instrument, in this year, on these windows. **This is the more valuable outcome for the project**, because it is a concrete instance of exactly what `D-025` protects the corpus from: confident, specific, mechanically-stated guest guidance that does not hold |
| **INDISTINGUISHABLE** | The most likely outcome and the least quotable. Reported with the same prominence as either of the above (`E25`) |
| Arms diverge | The session clock is load-bearing for this claim. A finding about `A-019`'s stakes — **not** an answer to `A-019`, which V06 cannot touch |

## 8. MANDATORY SCOPE STATEMENT

Any report of this test carries this verbatim:

> **PT-022 tests a claim made by a GUEST PRESENTER in V06, not by the course's author.** V06
> carries zero course-author runtime and `D-025` excludes all of its normative content from the
> methodology; `D-032` permits the claim to be **measured** and continues to forbid it being
> adopted, coded, merged with an instructor rule, or cited for or against one. The session
> windows are taken from V02's printed table because **V06 supplies no clock time at all**, so a
> null result is ambiguous between *"the claim is false"* and *"the windows are not what the
> guest meant"*. **No result here may be reported as evidence about the Market Maker Method, and
> no result here may close any `A-xxx` or `C-xxx` record.**

## 9. TO RUN THIS

1. Declare the data source, feed and chart timezone in the observation (`I-007` remains open
   **project-wide** — this declaration is for this test, and a standing declaration is the
   owner's to make).
2. Pin the `D-028` 70/30 boundary from the feed's actual available range and append it to
   `D-028`. Confirm the test window lies wholly inside DEVELOPMENT **before** examining a bar
   in it.
3. Harvest 15-minute GBP/USD for the window, timestamps and OHLC together, no pixel reads.
4. Run **`N-P` and `N2` first**, then read the rule arm's aggregate.
5. Write `06_MANUAL_BACKTEST/V06/BT_V06_0001.md` from
   `00_SYSTEM/TEMPLATES/MANUAL_BACKTEST_TEMPLATE.md`, §0 referencing this file.
6. **This file is never edited to match what was found.**
