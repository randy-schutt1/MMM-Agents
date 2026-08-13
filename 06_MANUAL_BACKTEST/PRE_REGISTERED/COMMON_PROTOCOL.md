# COMMON PROTOCOL — PT-002 … PT-021

```text
STATUS:     PRE-REGISTERED — NOTHING IN THIS BATCH HAS BEEN RUN
WRITTEN:    2026-08-12
ATTESTATION: The session that wrote this file and PT-002…PT-021 opened NO chart,
             loaded NO price series, and inspected NO GBP/USD outcome data of any
             kind. Every date range below was chosen on calendar grounds alone,
             stated in §3. This is the pre-registration discipline PT-001 sets and
             it is the whole value of these files.
```

Governing: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md` · `DECISIONS.md` `D-005`, `D-007`,
`D-009`, `D-010`, ~~`D-025`~~ → **`D-033`**, `D-026`, `D-027`, `D-028` → **`D-035`**, `D-029`,
`D-030`, `D-031`, **`D-034`**.

This file holds the machinery **shared** by PT-002 … PT-021 so that twenty files do not
repeat it twenty times and drift. **It does not replace a test's own pre-registration**:
every `PT-NNN` file carries its own question, its own window, its own trigger, its own
decision point and its own outcome table. If this file and a `PT-NNN` file ever disagree,
**the `PT-NNN` file governs** — it is the pre-registered artifact; this one is support.

---

## 1. INSTRUMENT AND UNITS

| Item | Value |
|---|---|
| Instrument | **GBP/USD only** (`D-007`). No other pair appears in this batch |
| Pip | `0.0001`. A "pip" anywhere in PT-002…PT-021 means exactly this |
| Timeframes | 15-minute primary; 1-hour and 4-hour where a test says so |
| Data source | ~~**UNDECLARED — `I-007` is OPEN.**~~ **DECLARED 2026-08-13 — `D-034`: TradingView, FXCM feed (`FX:GBPUSD`), no login, platform text only, chart timezone recorded per harvest.** `I-007` is CLOSED. See §6 — a **data-availability** blocker replaces it and it is not the same thing |

## 2. MEASUREMENT — THE HARD RULE

> **No price is ever read from a pixel.** Every open, high, low, close and timestamp is
> the charting platform's **own text report** of the bar, read from the DOM / Data
> Window / OHLC legend.

This is not a preference. `18_REVIEW/V02/V02_REVIEW_R1.md` charged a `MAJOR`
(`E06`/`E19`) because a price line drawn in TradingView's exact bullish body colour
`rgb(8,153,129)` was harvested as candle ink, and the corrupted read produced a **false
confirmation of `C-001`** — the project's foundational open contradiction. A colour-based
measurement can be confidently wrong and internally consistent at the same time.

The working reference implementation is `05_HOMEWORK/V05/scripts/tv_harvest_v05.mjs`,
which reads `Date`, `Time`, `Open`, `High`, `Low`, `Close` together, so **every bar
carries its own timestamp and no session or week boundary is ever inferred from bar
cadence** (the V04 `M1` defect, fixed at source in V05).

Three harvest hazards that must be handled before any test in this batch is run:

| Hazard | Handling |
|---|---|
| **Live-edge artifact** — hovering past the last real bar repeats the forming bar's OHLC | Harvest complete past periods only; drop the trailing run of identical quadruples (`slice_week.py`) |
| **Chart timezone** — every timestamp is the chart's own | Record it explicitly; it is the input to §4's two arms, not a detail |
| **Partial opening bars** — a week can open with a partial 4h bar | Boundaries are looked up from timestamps, never counted in bars |

## 3. THE THREE PRE-REGISTERED WINDOWS

Chosen **before any chart was opened**, on these grounds only: (a) proximity to the 2012
recording period, so the regime is as close to the taught one as history allows;
(b) coverage of US **and** UK daylight-saving transitions, which `D-031` §3c requires;
(c) enough calendar length to reach `n ≥ 30` (`BACKTEST_EVIDENCE_STANDARD.md` §4.1).

| ID | Range (inclusive) | Size | Used by |
|---|---|---|---|
| **W-A** | **2015-01-04 → 2015-12-31** | ~260 weekdays | Clock- and session-structure tests |
| **W-B** | **2014-01-05 → 2015-12-31** | ~520 weekdays | Conditional-event tests needing more decision points |
| **W-C** | **2013-01-06 → 2017-12-29** | ~260 weeks | Weekly-structure tests |

**Disclosures that belong on the record now, not after a result exists:**

1. **W-C contains 2016-06-23 (the EU referendum) and 2016-10-07 (the flash crash).**
   **No day, week or observation is excluded, anywhere in this batch, for any reason.**
   Excluding an event because it is "not representative" is `E09`. Each test that uses
   W-C reports a **pre-registered sensitivity appendix** listing its five largest-range
   weeks with their contribution — as an appendix, never as the headline, and never as a
   filtered re-run.
2. **W-A and W-B do not contain those events.** That is a consequence of choosing years
   adjacent to the course, not a selection for calm. It is stated here so nobody has to
   reconstruct the motive later.
3. **No window may be changed once its test is run.** A range change is a **new test ID**
   under `D-027`; the abandoned test is retained and marked `ABANDONED — PERIOD CHANGED`.

### 3a. `D-028` — the boundary is not yet pinned, and this batch does not pin it

`D-028` fixes the split at **oldest 70% DEVELOPMENT / most recent 30% HOLDOUT** and
records that the concrete dates are computed from the actual available range **by the
session that declares the data source** — not invented in advance.

All three windows above are therefore **`PROVISIONAL — DEVELOPMENT, PENDING D-028`**.
Before opening a chart, the runner **must** confirm the window lies wholly inside
DEVELOPMENT. If the pinned boundary falls inside a window, that test is **re-issued under
a new PT number** with a conforming window; the original file is retained and marked. It
is not edited into conformance.

> **RESOLVED 2026-08-13 — `D-035` pins the boundary at `2016-07-01`, and the clause above now
> bites.** The superseded `PROVISIONAL — PENDING D-028` marking is retained immediately above
> rather than corrected away, because it is what these files were written under.
>
> | Window | Range | Verdict against `DEVELOPMENT 2013-01-06 → 2016-06-30` |
> |---|---|---|
> | **W-A** | 2015-01-04 → 2015-12-31 | ✅ **conforms** — wholly inside DEVELOPMENT |
> | **W-B** | 2014-01-05 → 2015-12-31 | ✅ **conforms** |
> | **W-C** | 2013-01-06 → 2017-12-29 | ❌ **STRADDLES the boundary** by 546 days |
>
> **Consequence, and it is not optional.** The seven W-C tests — **`PT-008`, `PT-009`,
> `PT-010`, `PT-011`, `PT-012`, `PT-013`, `PT-019`** — must be **re-issued under new `PT`
> numbers** with a conforming window (the natural one being `W-C′ = 2013-01-06 → 2016-06-30`,
> ~180 weeks, still well over `n ≥ 30`). The originals are retained and marked
> `ABANDONED — PERIOD CHANGED`; **they are not edited.** The session that recorded `D-035` did
> not re-issue them — it recorded the defect. **This is follow-up work owed before any W-C
> test runs**, and it is separate from the data-availability blocker in §6.
>
> Also pinned by the same entry: the EU referendum (2016-06-23) falls in **DEVELOPMENT**; the
> October 2016 flash crash (2016-10-07) falls in **HOLDOUT** and is therefore unavailable to
> the Student Phase. Disclosure 1 above applies to whatever remains inside `W-C′`.

## 4. THE TWO TIMEZONE ARMS — `D-031`, BINDING

Every test in this batch that references a clock time runs **both** arms, and **both are
reported every time**:

| Arm | Chart timezone | Effect on the V02 printed table |
|---|---|---|
| **A — fixed offset** | `UTC−5` year-round | Session boundaries never move |
| **B — market-anchored** | `America/New_York`, DST-aware | Boundaries shift one hour in summer |

The session map both arms place, printed on the V02 slide at `[00:45:55]`:

```text
5pm            High / Low Reset (The MM Spread Is Set)
5pm – 8pm      Dead Gap
Asian Session  8:30pm – 3:00am     Gap 3:00–3:30
London Session 3:30am – 9:00am     Gap 9:00–9:30
New York       9:30am – 5pm
```

**No timezone is printed on that slide** and the instructor declines to specify —
*"Listen, don't analyse it… These are the times"* `[00:50:02]`, *"I can't ask the guy, he
died"* `[00:49:22]`. `A-019` stays **OPEN**; `D-031` converts it into a measured variable
and nothing in this batch may be cited as evidence about what the course teaches on it.

**Reporting only the better-performing arm is `E09` + `E24`.** Divergence between arms is
a *finding*, never a selection criterion. All three windows straddle DST transitions, so
every comparison is within-sample.

## 5. BASELINES — `D-026` / `D-029`

Four null models are used across the batch. Each `PT-NNN` file names the ones it runs.

| ID | Null | What it holds constant | What it randomizes |
|---|---|---|---|
| **N1** | **Matched random entry** (the `D-026` required form) | instrument, window, session, eligible hours, stop, target, direction, n | the entry bar |
| **N2** | **Circular clock shift** | the entire price path, unaltered | the clock: all session/boundary labels shifted by an offset drawn uniformly from ±12 h in 15-minute steps |
| **N3** | **Week-anchor shift** | the entire price path, unaltered | the week boundary: shifted by `k` days, `k` drawn uniformly from 1…4, plus a random 15-minute intraday offset |
| **N4** | **Natural control** | as specified per test | the course's own contrast — usually the un-triggered population at the same clock times |

`N2` and `N3` exist because most of this batch asks *"does the clock/the week boundary
carry information?"*, and a matched-random-entry control cannot answer that: it randomizes
the entry, not the calendar. Shifting the labels while leaving prices untouched isolates
exactly the claim.

Fixed for every test in the batch, pre-registered here so no discretion survives to run
time:

| Parameter | Value |
|---|---|
| Iterations | **1,000** (`D-029`) |
| **Random seed** | **`20260812`**, for every test, every arm. Pre-registered to make seed-shopping impossible |
| Reported | median, 5–95% range, iterations, seed, **and the rule's percentile within the distribution** |
| Baselines run | **before** the rule arm's aggregate is looked at |

## 6. BLOCKERS THAT APPLY TO THE WHOLE BATCH

| Blocker | Effect |
|---|---|
| ~~**`I-007`** — no chart data source, feed or timezone is declared~~ | ✅ **CLOSED 2026-08-13 — `D-034`.** TradingView / FXCM, no login, platform text only. The feed's week open is **21:00 UTC**, and that is the boundary W-C and `PT-008`–`PT-013` inherit; every such test must state it |
| ~~**`D-028` dates unpinned**~~ | ✅ **PINNED 2026-08-13 — `D-035`: boundary `2016-07-01`.** See §3a — W-A and W-B conform; **the seven W-C tests do not** |
| 🔴 **DATA AVAILABILITY — the blocker that replaced `I-007`, and it still stops this batch** | The declared feed serves 15-minute GBP/USD back only to **2026-05-31** (depth probe, `PT-023` §1). **W-A / W-B / W-C are out of reach at 15 minutes.** This is a `D-019` **measurement** gap, not a `D-030` definitional one — resolvable by tooling or by an owner decision, and `D-035` records the three options. **Nothing in this batch may be run until it is resolved** |
| **`D-030`** — definitions are never approximated | §7 — **unchanged by `D-033`**, and this is the part a future session is most likely to get wrong |
| ~~**`D-025`** — guest material is excluded as normative~~ | ⚖️ **REVERSED 2026-08-13 — `D-033`.** Guest material is normative on equal footing with the course author. §8 is corrected in place |

## 7. WHAT THIS BATCH DELIBERATELY DOES NOT TEST — `D-030`

Every test in PT-002…PT-021 is built from objects that are **measurements** — a clock
time, a session window, a range high, a range low, a distance in pips, a weekday, a
calendar week. None requires a definition the course has named and not given.

Excluded by `D-030`, with the record that blocks each one:

| Concept | Record | Why excluded |
|---|---|---|
| M / W anatomy | `A-011` | Named across V01–V04, never defined |
| "Second leg" | `A-007` | Promised at V02 `[00:35:22]`, defined only by gesture. 21 uses in V02 alone |
| TDI, shark fin, blood in the water, the band | `A-039`, `A-031`, `A-032` | A *required* criterion (V04 `[00:15:49]`) deferred twice by the course itself |
| "The level" as a countable unit | `A-004` | Ordinal legs, spacing and count all unstated |
| "Trap move" / "false move" as a pattern | `A-002` | Testable only as a *clock* claim, which is what PT-002 does instead |
| "Anchor point" / "peak formation" | `A-001`, `A-010` | V04 `[00:21:55]` equates them; it does not say how to find one in real time |
| "Outside structure" | `A-033` | Half-defined at V04 `[00:21:04]`; the promised card was never shown |
| "Mayo" / the moving averages | `A-020` | The spelling is settled; **no period is printed anywhere in V01–V06** |
| ADR × 3 | — | "Cycle" is undefined and no ADR lookback is stated by the instructor |
| The 2.5 / 3 / 3.5 / 4-day count | `C-001` | Open contradiction. PT-012 **measures the distribution** and adopts no value |
| Halving the Asian range (27 → 13.5) | `A-037` | Stated for one chart; whether it is a method is not said |
| "Slightly above" (the 22-trade tolerance) | `A-024` | Unbounded; any tolerance would be this session's invention |
| 22 / 33 trades, half-Batman | `A-023`, `A-022` | Rest on the above |

**A test that needed one of these and quietly approximated it would produce a number, and
a number in this corpus acquires authority a note never does** (`D-030`). That is the
failure this section exists to prevent.

## 8. ~~`D-025` — WHY V05 AND V06 CONTRIBUTE NOTHING HERE~~ — **REVERSED 2026-08-13, `D-033`**

> **CHANGED BY OWNER DIRECTION, and the superseded reading is retained below the change rather
> than corrected away** — the same handling `D-032` used on `INDEX.md` §2.
>
> **`D-033`, 2026-08-13: guest-presenter material is NORMATIVE evidence on equal footing with
> the course author** — *"all knowledge is created equal."* `D-025`'s normative exclusion is
> superseded, and `D-032`'s narrower "test but never adopt" fence is superseded with it. The
> paragraphs below were correct under the decision set of 2026-08-11 → 2026-08-13 and are
> **no longer the rule**.
>
> **What this changes for this batch: nothing, mechanically.** `PT-002`…`PT-021` were built
> only from measurements and none of them draws on V05, V06 or V04 Segment B — so no test here
> is re-scoped, no window moves, and no pre-registration is touched. What changes is that the
> absence is **no longer a ruling**: V05/V06-derived tests are now permissible and are
> **owed**. Authoring them is follow-up work under a new `PT` range, not an edit to any file in
> this directory.
>
> **What does NOT change: `D-030` (§7) is untouched.** V06's system needs *push*, *pullback*,
> *nameable pattern* and a moving-average type, none of which the course defines — so most of
> it stays untestable on the definitional ground, exactly as it did before, and equal speaker
> authority supplies no missing definition. A session that reads `D-033` as unblocking §7 has
> misread it.

*(Superseded text, retained unedited:)*

> V05 and V06 carry **zero course-author runtime**. V06 in particular states the most nearly
> complete trading system anywhere in V01–V06 — entry, filter, stop, target, time stop, exit
> — and **all of it is guest material and all of it is excluded**. So is Segment B of V04
> (69% of that lesson): the ADR ~90–95% gate, the 7-pips-plus-spread stop, the 35–50 pip
> target, the 12-pair watchlist, *"don't trade Mondays"*.
>
> No test in this batch draws a condition, a threshold, a session or a target from any of
> it. A future session must not read the absence as an oversight: it is the ruling.

## 9. INTEGRITY RULES FOR THE RUN SESSION

1. **Run the baselines before looking at the rule arm's aggregate.**
2. **Report both `D-031` arms, always.**
3. **Report null results with equal prominence** (`E25`).
4. `n < 30` → `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`; no rate quoted
   anywhere without that label in the same sentence.
5. Every hit rate carries an interval and a baseline percentile (`E24`).
6. **Every test in this batch is reported whether or not it found anything.** A summary
   naming only the tests that worked is invalid (`BACKTEST_EVIDENCE_STANDARD.md` §4.3).
7. Observations are written to `06_MANUAL_BACKTEST/VXX/BT_VXX_NNNN.md` from
   `00_SYSTEM/TEMPLATES/MANUAL_BACKTEST_TEMPLATE.md`, with §0 referencing the `PT-NNN`
   file. The `PT-NNN` file is never edited to match what was found.
