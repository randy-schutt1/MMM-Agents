# V06 — HOMEWORK

| Field | Value |
|---|---|
| Video ID | V06 — *"Micro Daily Trends"* |
| Assigned | `[00:37:59]`–`[00:38:44]` (the *"Homework is the Authority……… ~JN~"* slide and the task read off it) and `[01:14:29]`–`[01:14:32]` (*"All right, homework it first, guys."* / *"Homework it first."*) — **by a guest presenter, not the instructor** |
| Attempted | 2026-08-12 |
| Data source | TradingView, **FXCM** feed. **No login, no account, no paywalled feature, no CAPTCHA encountered or bypassed.** |
| Raw data | `data/v06_harvest_15m_full.json` (957 bars/pair, 15m, 2026-07-30 → 2026-08-13) and `data/v06_daily_full.json` (147 bars/pair, 1D, 2026-02-04 → 2026-08-13) |
| Week slice | `data/v06_week_2026-08-02_15m.json` — 480/480/480/**476** bars |
| Charts | `charts/` — 6 images, **rendered from the committed JSON, not screenshots** |
| Scripts | `scripts/` — harvester, measurement, renderer, plus the two audit tools this session wrote (`check_quotes.py`, `f0_profile.py`). All committed and re-runnable |
| Week analysed | **Sun 02 Aug 2026 21:00 → Fri 07 Aug 2026 20:45**, chart clock |

**Completed on real data. No substitution was needed.**

---

> ## ⚠ WHAT THIS HOMEWORK DELIBERATELY DOES NOT DO
>
> V06 is **100% guest-presented** (`V06_SOURCE_NOTES.md` header). Under `DECISIONS.md` **D-025**
> its **normative** content is **excluded from doctrine** and may not be coded, backtested, or
> cited for or against an instructor rule.
>
> **The lesson's homework, as stated, is normative in its entirety.** *"If you find your anchor
> in today and look for three pushes"* `[00:38:15]`–`[00:38:23]` names two guest constructs and
> nothing else. Performing it as stated would mean **applying the guest's cycle theory to real
> charts and writing the result into the corpus** — which is exactly what D-025 forbids and
> exactly what a session under pressure to produce output would do.
>
> So this homework does **not** perform the assignment as stated. It performs the part of it
> that survives the fence, and it says clearly which part that is:
>
> | Performed | Why it is allowed |
> |---|---|
> | Day separators at each day's **own first bar** | A fact read from the data's timestamps |
> | Each day's **high and low**, with exact prices | Objects the **instructor** himself names — V04 `[00:18:24]` *"try to identify the high of the week and the low of the week"*; the daily analogue is `HOD`/`LOD`, printed on V06's own slide `V06_00-05-29` |
> | **ADR**, measured over a family of lookbacks | ADR is arithmetic on daily bars. **No single value is adopted** — see §2 |
> | The lesson's own two numbers **compared to each other** on measured data | Arithmetic on figures the lesson states. Not a test of a rule |
> | Bar-count and continuity verification | Data hygiene, and the discipline V04 review R1 established |
> | Time-of-day of each day's extremes, under **both** `D-031` timezone arms | A fact about the data, reported both ways as D-031 requires |
>
> | NOT performed | Why |
> |---|---|
> | Finding the **anchor** | Guest normative. `[00:21:55]`, `[00:38:15]` |
> | Counting **pushes** — one, two or three | Guest normative, and the lesson's central construct |
> | Labelling **Level 1 / 2 / 3** | Guest normative |
> | Naming any **pattern** (railroad tracks, quarter wood, star) | Guest normative, and `A-044` is open |
> | Marking any **entry, stop or target** | Guest normative, and `D-010`'s machine-rule firewall applies independently |
> | Measuring **"pullbacks"** against the 25–50 pip band | **`D-030`.** A pullback has no definition in this corpus; any threshold I chose to make it measurable would be *mine*, and the number it produced would be attributed to the course. This is the single most tempting measurement in the lesson and it is the one most firmly refused |
>
> **A homework artifact that marked anchors, pushes and entries would look far more like the
> lesson and would be wrong.** The exclusion is the assignment being done correctly under this
> project's rules, not the assignment being skipped.
>
> **⚖️ 2026-08-13 — the `D-025` grounds above are SUPERSEDED IN PART by `D-033` (item 60):**
> guest material is now normative at equal weight, so rows excluded solely as "guest
> normative" lose that ground. **The work performed does not change**, because every excluded
> item except H2's anchor half is *independently* blocked by `D-030` (*push*, *pullback*,
> *consolidation*, pattern names — all undefined), and that block survives. Retained
> unedited; see `V06_INTERPRETATION.md` §9.

---

## 0. IS THIS A BACKTEST? NO — AND THE DISTINCTION IS LOAD-BEARING

`D-026`/`D-027` require a pre-registered baseline, a pre-registered period and a reserved
holdout **before any manual backtest observation exists**, and `validate_project.py` enforces it.
**This file is not a backtest and creates no `BT_*.md` observation.**

The test is whether a **rule** is being evaluated. Nothing here evaluates a rule: there is no
entry, no exit, no direction, no outcome and no hit rate. Every number is either a property of
the data (bar counts, ranges, extremes, clock times) or arithmetic on figures the lesson itself
states. There is nothing for a matched-random-entry baseline to be a baseline *of*.

**`06_MANUAL_BACKTEST/` was not written to by this session, and no `BT_*` observation exists
anywhere in it.** A parallel session working the same branch added `PT-002`–`PT-021` to
`06_MANUAL_BACKTEST/PRE_REGISTERED/` while this lesson was being studied; **none of them is
V06-derived**, none is run, and this session neither authored nor audited them — they are
named here only so a reader does not mistake this file's claim for a survey of the directory's
whole contents. `PT-001` remains pre-registered and unrun.

If a future session wants to test V06's push rule, it will need the baseline, the period
pre-registration, the holdout — **and a definition of "push" that this corpus does not
contain**, which is `D-030`'s wall.

---

## 1. METHOD

### 1.1 No price is read from a pixel

Every number in this file is **TradingView's own Data Window text, read from the DOM.** The
chart is driven with synthetic mouse moves across the price pane; after each move the Data
Window panel is parsed for `Date`, `Time`, `Open`, `High`, `Low`, `Close`. That panel is the
platform's report of the hovered bar.

This is the V02 `MAJOR` (`E06`/`E19`) lesson applied — there a price line drawn in the same
colour as bullish candles corrupted a pixel-based read. **Nothing here depends on a colour.**

The six images in `charts/` are **rendered from the committed JSON**, not screenshots. They
exist to be looked at; **no measurement is taken from them.**

### 1.2 The harvester is V05's, unchanged

`scripts/tv_harvest_v06.mjs` is `05_HOMEWORK/V05/scripts/tv_harvest_v05.mjs` with only its
header comment changed. **It was deliberately not re-derived**: using the same instrument on two
lessons is what makes §4's cross-check meaningful. Every bar carries its own `Date` and `Time`,
so week and day boundaries are a **lookup, not an inference from bar cadence** — the V04 review
R1 `M1` defect, fixed at source and staying fixed.

### 1.3 The live-edge artifact, and why trailing bars are dropped

Hovering past the last real bar makes TradingView report the still-forming bar's OHLC for every
projected future slot, producing trailing rows with **distinct timestamps and identical OHLC**.
`scripts/measure_v06.py` drops the trailing run of identical quadruples: **10 rows per pair** on
the daily series (147 → 137). The analysed 15m week ends 2026-08-07, five days clear of the live
edge, so no analysed bar is affected either way. Disclosed because a reader diffing the raw and
sliced JSON will see the difference.

---

## 2. RESULT — ADR, AND WHY NO SINGLE VALUE IS ADOPTED

V06 states *"Each push is approximately ADR divided by 3"* `[00:05:45]` and attributes it to the
instructor at `[00:05:50]`. **ADR is used three times in the lesson and defined zero times**;
`A-038` records that its lookback window is unspecified anywhere in the corpus.

So ADR was computed over **five lookbacks**, and the family is the result. Chart:
`charts/adr_family.png`.

| Pair | ADR5 | ADR10 | ADR14 | ADR20 | ADR30 | spread | as % of smallest |
|---|---|---|---|---|---|---|---|
| EURUSD | 32.5 | 42.4 | 51.9 | 48.4 | 49.5 | **19.4** | **60 %** |
| GBPUSD | 44.3 | 52.0 | 63.7 | 64.7 | 70.1 | **25.8** | **58 %** |
| USDJPY | 106.9 | 140.3 | 151.9 | 123.6 | 108.4 | **45.0** | **42 %** |
| USDCHF | 44.2 | 50.7 | 57.9 | 52.5 | 54.6 | **13.8** | **31 %** |

*(pips; daily bars to 2026-08-12 after the live-edge trim; JPY pip = 0.01)*

### What this establishes, and it is a methodological result rather than a market one

**The undefined lookback moves the answer by 31–60 %.** GBP/USD — this project's primary
instrument (`D-007`) — is 44 pips on a 5-day window and 70 pips on a 30-day one, so
*"ADR ÷ 3"* is **15 pips or 23 pips** depending entirely on a parameter nobody has stated.

That is the concrete, measured case for `D-030`. A session that wanted V06's push rule to be
testable would have to pick one of those numbers. It would then measure something, get a result,
and the result would enter the corpus attributed to the instructor — **and the choice that
produced it would be invisible a month later.** `A-038` stays `DO NOT CODE`, and this table is
the evidence for why.

**Realised range agrees with the family, which is a sanity check on the arithmetic, not a
finding:** over the four full days of the analysed week the mean realised daily range was
EURUSD 41.2, GBPUSD 51.0, USDJPY 123.2, USDCHF 50.5 pips — inside each pair's ADR family in every
case.

---

## 3. RESULT — THE LESSON'S OWN TWO NUMBERS, ON ONE SCALE

Chart: `charts/push_size_vs_pullback_band.png`.

The lesson states both of these within twenty seconds of each other:

> *"Each push is approximately ADR divided by 3."* `[00:05:45]`
> *"The pull marks [pullbacks] are usually 25 to 50 pips."* `[00:06:04]`

and adds that a 10–15 pip channel is *"not really pulling it back"* `[00:06:19]`.

Put on one scale at ADR20:

| Pair | ADR20 | ADR20 ÷ 3 (= one push) | 25 pips as % of a push | 50 pips as % of a push |
|---|---|---|---|---|
| EURUSD | 48.4 | **16.1** | 155 % | 310 % |
| GBPUSD | 64.7 | **21.6** | 116 % | 232 % |
| USDJPY | 123.6 | **41.2** | 61 % | 121 % |
| USDCHF | 52.5 | **17.5** | 143 % | 286 % |

**On three of four pairs, at 2026 volatility, the stated pullback is larger than the stated
push** — up to three times larger. A structure whose retracements exceed its advances is not the
three-push trend the lesson describes. Only USDJPY, the highest-volatility pair here, puts the
two figures in the same range.

### How to read that, and how not to

**This is not a refutation of the lesson and it is not offered as one.** Three reasons, and all
three matter:

1. **Volatility regime.** V06 was recorded in **March 2012**. EUR/USD's daily range then was
   routinely 100–140 pips; the 48 pips measured here is a different market. The lesson's two
   numbers may well have been mutually consistent when it was recorded, and the mismatch may be
   entirely an artifact of comparing 2012 rules of thumb to 2026 data.
2. **ADR is undefined** (§2). A different lookback moves *"one push"* by up to 60 %.
3. **The comparison is arithmetic, not a test.** No pullback was measured — measuring one would
   require a definition this corpus does not have (`D-030`).

**What it does establish, and this is worth carrying forward:** *"25 to 50 pips"* is an
**absolute** number and *"ADR ÷ 3"* is a **relative** one, so the two can only agree at one
volatility level. **Any future automation of a rule of this family must decide which of the two
is the invariant**, and the corpus currently gives no basis for choosing. That is a real finding
about the *codability* of the material, produced without coding any of it.

> **Related, and it is a guest statement not a rule:** the lesson's own target guidance is
> absolute too — *"U.S. session you're looking for anywhere from 30 to 50 pips"* `[00:31:14]` —
> and would today be **more than the entire measured ADR20 of EUR/USD divided by one**, let
> alone by three.

---

## 4. RESULT — THE 15-MINUTE WEEK, VERIFIED RATHER THAN ASSUMED

| Pair | Week bars | First bar | Last bar | Continuity breaks |
|---|---|---|---|---|
| EURUSD | **480** | `2026-08-02 21:00` | `2026-08-07 20:45` | **0 / 479** |
| GBPUSD | **480** | `2026-08-02 21:00` | `2026-08-07 20:45` | **0 / 479** |
| USDJPY | **480** | `2026-08-02 21:00` | `2026-08-07 20:45` | **0 / 479** |
| USDCHF | **476** | `2026-08-02 22:00` | `2026-08-07 20:45` | **0 / 475** |

**Continuity test:** within a trading week each bar's open must equal the prior bar's close.
Over the committed slice — **1,912 bars, 1,908 transitions — the chain is 1,908 / 1,908
continuous, zero breaks, in all four pairs.**

Bars per calendar day, counted from the bars' own timestamps:

| Pair | 08-02 | 08-03 | 08-04 | 08-05 | 08-06 | 08-07 | total |
|---|---|---|---|---|---|---|---|
| EURUSD | 12 | 96 | 96 | 96 | 96 | 84 | 480 |
| GBPUSD | 12 | 96 | 96 | 96 | 96 | 84 | 480 |
| USDJPY | 12 | 96 | 96 | 96 | 96 | 84 | 480 |
| **USDCHF** | **8** | 96 | 96 | 96 | 96 | 84 | **476** |

### 4.1 USDCHF's late open reproduces for the third time, from a fresh harvest

**476 = 480 − 4**, and 4 × 15m is exactly the missing hour. USDCHF's first bar of the week is
22:00 where the other three open at 21:00.

This is now **three independent arrivals at the same figure**: V04 review R1's corrected count,
V05's timestamped harvest of this same week, and this session's fresh harvest a day later. The
standing lesson from V04 — *"verify actual bar counts against expected before computing"* — was
applied here **before** any measurement, and it found the same thing it was written to catch.

**USDCHF's 08-02 low (`0.80552`, at its first available bar, 22:00) is therefore
boundary-limited**, exactly as in V05: if USDCHF traded in the missing hour on another feed, its
true low for that day could be lower. USDCHF's Sunday-stub extremes are reported with that
caveat and are excluded from any comparison across pairs.

### 4.2 An independent reproducibility check against V05's committed data — and it is not perfect

The analysed week is deliberately the **same week V05 committed**, so the two harvests can be
diffed. Result, comparing this session's harvest against `05_HOMEWORK/V05/data/v05_harvest_15m_full.json`:

| Pair | Bars, V05 | Bars, V06 | Timestamps matching | OHLC quadruples differing | Largest difference |
|---|---|---|---|---|---|
| EURUSD | 480 | 480 | **480 / 480** | **0** | — |
| GBPUSD | 480 | 480 | **480 / 480** | **0** | — |
| USDJPY | 480 | 480 | **480 / 480** | **120** | 0.011 (**1.1 pips**) |
| USDCHF | 476 | 476 | **476 / 476** | **66** | 0.00004 (**0.4 pips**) |

**Structure reproduces exactly; prices do not, on two of four pairs.** Every timestamp, every
bar count and every day boundary is identical across two harvests a day apart. But 120 of
USDJPY's 480 bars and 66 of USDCHF's 476 carry slightly different OHLC values — sub-pip on
USDCHF, up to about a pip on USDJPY.

**This is reported because it is the kind of thing that quietly breaks a reproducibility claim
later.** The likely cause is ordinary: retail chart feeds revise recent tick history, and a
15-minute bar's high or low can move by a tick when a late print arrives. The consequences worth
recording:

- **A "reproducible" result computed to sub-pip precision on this feed is not reproducible**,
  even by the same tool a day later. Any future backtest tolerance must exceed ~1 pip on JPY
  crosses.
- **It does not affect anything in this file.** Every figure here is a range, a count, a
  timestamp or a several-pip magnitude; a 1-pip revision changes none of them.
- **It strengthens the case for committing the data**, not just the method. The JSON in
  `data/` is the exact input to every number above, and it is now fixed.

---

## 5. RESULT — DAILY EXTREMES AND THEIR CLOCK TIMES, BOTH `D-031` ARMS

Charts: `charts/<PAIR>_15m_week_days_marked.png` — the week with day separators at each day's
own first bar and each day's high and low drawn with its exact price. **No anchor, no push, no
level, no pattern, no entry**, and the footer says so inside the image.

Per `D-031`, session-dependent times are reported under **both** arms, always. Arm A is fixed
`UTC−5` ("EST", no DST); Arm B is `America/New_York` with DST, i.e. `UTC−4` in August. The two
differ by exactly one hour. Full table in `data/v06_measurements.json`; GBP/USD, the project's
primary instrument, is reproduced here:

| Day | Bars | Range | High | at (chart) | A | B | Low | at (chart) | A | B |
|---|---|---|---|---|---|---|---|---|---|---|
| 08-02 | 12 | 28.0 p | `1.35063` | 22:00 | 17:00 | 18:00 | `1.34783` | 21:30 | 16:30 | 17:30 |
| 08-03 | 96 | 85.2 p | `1.35027` | 00:30 | 19:30 | 20:30 | `1.34175` | 18:00 | 13:00 | 14:00 |
| 08-04 | 96 | 36.8 p | `1.34562` | 16:00 | 11:00 | 12:00 | `1.34194` | 05:45 | 00:45 | 01:45 |
| 08-05 | 96 | 42.2 p | `1.34861` | 14:15 | 09:15 | 10:15 | `1.34439` | 01:30 | 20:30 | 21:30 |
| 08-06 | 96 | 39.9 p | `1.34794` | 13:45 | 08:45 | 09:45 | `1.34395` | 21:45 | 16:45 | 17:45 |
| 08-07 | 84 | 74.9 p | `1.35089` | 13:15 | 08:15 | 09:15 | `1.34340` | 10:30 | 05:30 | 06:30 |

**No conclusion is drawn from the clock times, and none can be.** Reporting them is what
`D-031` requires of any measurement that could later be used in a session-dependent test; the
arms are recorded now so that a future session does not have to re-harvest to get them, and so
that neither arm can be quietly selected later. `A-019` — the course's own session-timezone
question — is **untouched by this**: V06 states no clock time for any session, so there is
nothing here to compare against.

---

## 6. THE ASSIGNMENT, ITEM BY ITEM

| # | Assignment, as stated | Performable? | Disposition |
|---|---|---|---|
| H1 | *"Homework is the Authority"* — sit down, look at it, absorb it `[00:38:04]`–`[00:38:12]` | **Yes** | ✅ The whole of this session |
| H2 | *"find your anchor in today"* `[00:38:15]` | **Excluded** | ❌ Guest normative (`D-025`) |
| H3 | *"look for three pushes"* — the same sentence, `[00:38:15]` | **Excluded** | ❌ Guest normative (`D-025`) |
| H4 | *"Of the peak formation, you're looking for three clear pushes. One, two, and then three"* `[00:38:35]`–`[00:38:39]` | **Excluded** | ❌ Guest normative |
| H5 | *"It should end the day back into consolidation"* `[00:38:41]` | **Excluded** | ❌ Guest normative, and *"consolidation"* is undefined |
| H6 | Mark up real charts and look at real days | **Yes, in the mechanical half** | ✅ §5 — day separators and daily extremes, no cycle labels |
| H7 | Measure things rather than eyeball them — *"you have to measure it… you have to measure them"* `[00:06:28]`–`[00:06:34]` | **Yes** | ✅ §2, §3, §4 — and this is the one piece of the lesson's *method* that is admissible, because measuring is a procedure, not a market claim |
| H8 | Send it to a coach for the *"accountability factor"* `[00:50:59]` | **No** — 2012 programme, no coach | `NOT APPLICABLE` |

---

## 7. WHAT THIS HOMEWORK ESTABLISHED

1. **The undefined ADR lookback moves *"ADR ÷ 3"* by 31–60 %** across five reasonable windows,
   on four pairs. `A-038` now has a measured consequence rather than only a gap, and `D-030`'s
   prohibition has a concrete demonstration behind it.
2. **The lesson's two headline numbers are on different scales** — one absolute, one relative —
   and at 2026 volatility they disagree by up to 3× on three of four pairs. **Recorded as a
   codability finding, with the 2012-versus-2026 regime caveat stated as prominently as the
   result.**
3. **USDCHF's late week open reproduces a third time, from a fresh harvest**, and was caught by
   a check run *before* the measurements rather than by a review afterwards.
4. **A negative reproducibility result worth more than a clean one:** structure reproduces
   exactly between two harvests, prices do not — 120 USDJPY bars and 66 USDCHF bars differ by up
   to ~1 pip. Any future claim of exact reproducibility on this feed is false at that precision.
5. **1,908 / 1,908 continuity** across four pairs, and every measurement traceable to committed
   JSON by committed scripts.
6. **A second worked demonstration of the D-025 boundary**, on much harder material than V05's:
   the assignment as stated was *entirely* normative, and what remains after the fence is applied
   is still substantial — but it is a different exercise, and this file says so rather than
   blurring the two.

## 8. WHAT IT DID NOT, AND COULD NOT, ESTABLISH

- **Nothing about whether the method works.** No entry, no exit, no outcome. By design.
- **Nothing about pushes, anchors or levels.** They were not marked, counted or looked for.
- **Nothing about the 25–50 pip pullback claim.** It was not tested, because testing it requires
  a definition of "pullback" the corpus does not contain (`D-030`). §3 compares the lesson's
  numbers to each other; it does not measure a single pullback.
- **Nothing that closes `A-038`, `A-019`, `A-044`, `A-049` or any other record.** V06 is guest
  material and `D-025` bars closure regardless of what was measured.
- **A one-week, four-pair observation is not evidence of a pattern**, and §5 draws no conclusion
  from the clock times.
- **The regime caveat cuts both ways.** §3's mismatch is evidence about 2026 data, not about
  2012 instruction, and a future session must not cite it as though the lesson were shown wrong.

---

## 9. INDEPENDENT CROSS-CHECK AGAINST A SECOND DATA VENDOR

**Added 2026-08-13 at the owner's direction: cross-check the homework's conclusions by an
additional independent method rather than a single pass.**

§4.2 already compared this session's harvest against **V05's committed harvest** — but that is
the *same platform, same feed, same script*, a day apart. It tests the harvester's determinism,
not the data. This section uses a genuinely different vendor.

| | Source 1 | Source 2 |
|---|---|---|
| Vendor | **TradingView / FXCM** | **Yahoo Finance** |
| Transport | Data Window **DOM text**, driven by synthetic mouse moves | Chart **JSON API**, `query1.finance.yahoo.com/v8/finance/chart/<SYM>=X` |
| Timestamps | chart-clock strings | **UTC epoch integers** |
| Rendering involved | a chart is drawn, then its text panel is read | **none — nothing is rendered at all** |

The JSON path is a *stronger* form of the no-pixel rule than DOM text: there is no chart in the
loop to misread. Script: `scripts/crosscheck_second_source.py`, committed and re-runnable.

**A constraint that shaped the design:** Yahoo serves only ~7 days of 15-minute FX history but
~60 days at 30 minutes. So the comparison aggregates **FXCM's 15m bars up to 30m** and compares
like with like — **236 matched 30-minute bars per pair** across the analysed week.

### 9.1 The chart timezone, derived instead of assumed

§5 of this file reports times as *"chart clock"* and never proved what that clock was. It is now
derived: for each candidate UTC offset, count matched bars whose **high and low both** agree
within 3 pips, and take the argmax.

| Pair | Best offset | Agreement at that offset | Agreement at UTC+0 |
|---|---|---|---|
| GBPUSD | **UTC+0** | 219 / 236 | 219 / 236 |
| USDJPY | **UTC+0** | 227 / 236 | 227 / 236 |
| USDCHF | **UTC+0** | 230 / 236 | 230 / 236 |
| EURUSD | UTC−2 | 52 / 237 | **2 / 236** |

**The TradingView chart was on UTC.** Three pairs agree unanimously and overwhelmingly. **The
homework's implicit assumption is confirmed by an independent vendor**, and the `D-031` arm
arithmetic in §5 (Arm A = chart − 5 h, Arm B = chart − 4 h) is therefore correct as applied.

**EURUSD's disagreement is a vendor price bias, not a timezone.** The signed median difference
(Yahoo − FXCM) is **+3.11 pips on highs and +3.94 pips on lows** — a *constant offset in one
direction*, which no time shift can produce. Against a 3-pip tolerance that offset alone knocks
every bar out of agreement, so the argmax wanders to a meaningless offset. **Reported rather
than dropped**: it is the one place the cross-check disagrees with itself, and the explanation
is checkable from the signed medians rather than asserted.

### 9.2 The week extremes — the numbers §2.3 and §5 actually report

| Pair | FXCM high | Yahoo high | diff | FXCM low | Yahoo low | diff |
|---|---|---|---|---|---|---|
| EURUSD | `1.15808` | `1.15821` | **1.3 p** | `1.15003` | `1.15048` | **4.5 p** |
| GBPUSD | `1.35089` | `1.35075` | **1.4 p** | `1.34175` | `1.34187` | **1.2 p** |
| USDJPY | `158.574` | `158.576` | **0.2 p** | `155.228` | `155.215` | **1.3 p** |
| USDCHF | `0.81356` | `0.81358` | **0.2 p** | `0.80559` | `0.80558` | **0.1 p** |

**Two independent vendors agree on all eight of the week's extremes to within 4.5 pips, and on
six of the eight to within 1.4 pips.** EURUSD's 4.5 pips is almost exactly its systematic bias
from §9.1. This is the homework's headline measurement standing up to a vendor it was not
derived from.

### 9.3 USDCHF's late week open — the cross-check REFUSES to answer, and that is the result

The obvious question: is `476 = 480 − 4` a fact about the **market** or about the **FXCM feed**?

Across **13 consecutive week opens** on the second source, **all four pairs open at the same
timestamp, every week**: Sunday **23:00 UTC**, including USDCHF, including the analysed week.

**That does not settle it, and reporting it as though it did would be wrong.** Yahoo carries
**no bar before 23:00 UTC for any pair**, while FXCM opens three pairs at 21:00 and USDCHF at
22:00. **The disputed hour — 21:00 to 22:00 — lies entirely outside what the second vendor
serves.** It cannot see the hour in question, so it can neither confirm nor refute that USDCHF
traded in it.

> **`Q3` — UNRESOLVED.** The second source is blind to the exact interval at issue.

**What the attempt did establish, and it is worth more than the question it failed to answer:**

> **The week-open timestamp is vendor-dependent.** FXCM opens the FX week at **21:00 UTC**;
> Yahoo opens it at **23:00 UTC**; both are perfectly consistent week after week. So
> **"480 bars in a trading week" is a property of the FXCM feed's session definition, not a
> property of the market.**

That has a direct consequence for this project. §4.1 of this file, V05's homework, and V04
review R1 all treat 480 (and USDCHF's 476) as if it were a market fact reproduced three times.
**It was reproduced three times on one vendor.** Any future backtest whose week boundary is
load-bearing — `PT-008`, `PT-009`, `PT-010`, `PT-012`, `PT-013`, `PT-019`, all of which use
weekly windows — **will get a different week from a different provider**, and a two-hour
difference at the open is more than enough to move a weekly extreme.

### 9.4 How far apart are two vendors on the same bar?

The question no single-source measurement can ask, and the one that bounds what
*"reproducible"* can mean for retail FX data.

| Pair | bars | median \|ΔH\| | median \|ΔL\| | 95th \|ΔH\| | 95th \|ΔL\| | max \|ΔH\| | max \|ΔL\| |
|---|---|---|---|---|---|---|---|
| EURUSD | 236 | 3.11 | 3.94 | 4.16 | 5.33 | 8.5 | 37.3 |
| GBPUSD | 236 | 0.33 | 1.09 | 1.63 | 4.13 | 5.7 | 44.6 |
| USDJPY | 236 | 0.10 | 0.70 | 0.50 | 2.40 | 2.5 | 6.1 |
| USDCHF | 236 | 0.10 | 0.30 | 0.50 | 1.00 | 5.9 | 6.9 |

*(pips; EURUSD's medians are its systematic bias, §9.1)*

**Typical agreement is sub-pip to a few pips; worst-case disagreement reaches 37–45 pips on a
single bar's low.** The large outliers are one-off bad prints, which retail FX feeds have.

**This sharpens §4.2's finding rather than repeating it.** There, two harvests of the *same*
feed differed by up to ~1 pip. Here, two *different vendors* differ by up to ~45 pips on an
individual bar. **Any rule whose trigger depends on a specific bar's low — a stop placement, a
breach of a level by a few pips, a 25-vs-50-pip band — can fire on one vendor and not on
another.** That is a first-order constraint on every backtest this project will run, and it was
invisible until a second source was consulted.

### 9.5 What this cross-check changed, and what it did not

| Homework claim | Status after cross-check |
|---|---|
| Week extremes (§2.3, §5) | **CONFIRMED** by an independent vendor, ≤4.5 pips |
| Chart timezone = UTC, and the `D-031` arm arithmetic built on it (§5) | **CONFIRMED**, 3 of 4 pairs, ~230/236 bars |
| 480 / 480 / 480 / **476** bar counts (§4) | **UNCHANGED as a measurement, RESCOPED as a claim** — it is an FXCM-feed fact, not a market fact |
| USDCHF's missing hour is market structure | **NOT ESTABLISHED, and never was.** §4.1 called it *"a property of the feed's session open for this symbol"*, which was the careful reading and survives; anything stronger does not |
| ADR family (§2) and the scale comparison (§3) | **UNTOUCHED** — daily-bar arithmetic, not re-derived here. A daily-resolution second source is the follow-up |

**The honest summary: the cross-check confirmed what the homework measured and demoted what
the homework implied.** The numbers held; one of the inferences drawn around them did not.

