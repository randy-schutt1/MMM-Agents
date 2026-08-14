# PT-044 — V16's **200-pip daily allotment**: a CEILING the dealers are told not to exceed, or a TYPICAL day?

> **COMMITTED BEFORE THE RUNNER EXISTS AND BEFORE ANY BAR IS READ.**
> `COMMON_PROTOCOL.md` §9 rule 7: if the runner and this file disagree, **this file governs**,
> neither is edited, and the disagreement is reported in `BT_V16_0001.md`.

---

## §0 — NUMBERING

`PT-043` was the last identifier used (V15). **This is `PT-044`.** No other test is opened by V16.

---

## §1 — THE CLAIM

V16 states a daily-range figure **twice, in two different grammatical moods**, and the moods are
not equivalent. Both are `[AUDIO]`, course author, Tier 1.

**Statement A — the TYPICAL reading**, `[00:22:44]`–`[00:22:50]`:

> *"this distance from here to here was the average daily range based on yesterday's projection
> that the dealer had to work with approximately what? **200 pips in every pair except GJ and some
> of the crosses.**"*

**Statement B — the CEILING reading**, `[00:30:12]`:

> *"these guys are told **do not exceed 200 pips on the average day** because of you'll do this.
> You'll destroy trade."*

### §1a — WHY THIS IS THE ONLY TESTABLE CLAIM IN V16, AND WHY THAT MATTERS

`V16_INTERPRETATION.md` §6 enumerates the lesson's propositions and finds **five of six are
blocked** — `M1`–`M4` are not computable (`A-101`), the ADR is not computable (`A-100`, `C-022`),
and the cycle has no start test. **This one is different in kind: it has a stated value, a stated
scope (*"every pair except GJ and some of the crosses"* — and `GBP/USD` is inside that scope), and
a stated period (*"the average day"*).** Nothing has to be invented to test it.

### §1b — WHAT IS **NOT** TESTED HERE, AND WHY

1. ⛔ **The `600–1000` pip week is NOT re-tested.** `BT_V10_0001` returned **CONTRADICTED AS
   STATED** (0 of 180 weeks; median 243.8). `D-027` forbids re-running a settled question, and
   `COURSE_PROGRESS.md`'s **V16 GATE (e)** rules on this exact case: V16's restatement at
   `[00:23:24]` is **durability evidence, logged in `A-095`**, not a new test.
2. ⛔ **The candle-colour rule, the fourth-day flip and the pivot×ADR confluence are NOT tested** —
   `A-101` blocks all three at the level construction. Declaring this **before** the run is the
   point: it is why `PT-044` tests an aside instead of the lesson's headline.
3. ⛔ **Multi-pair scope is NOT tested.** This project holds **GBP/USD only** (`D-036a`, `D-044`).
   The claim's *"every pair"* is therefore tested on **one** member of the set. **A negative on
   GBP/USD does not falsify the claim for other pairs; a positive does not confirm it for them.**
   Stated here so the result cannot be read wider than its data.
4. ⛔ **`GJ` (GBP/JPY) is the claim's own named exception and is not held by this project.** It is
   not tested and its absence is not evidence either way.

---

## §2 — THE QUESTION

**`Q1` (ceiling):** Does GBP/USD's daily range exceed 200 pips often enough that *"do not exceed
200 pips"* cannot be an operative limit?

**`Q2` (typical):** Is 200 pips a fair description of a typical GBP/USD day?

**These pull in opposite directions and that is deliberate.** A world in which `Q2` is YES is a
world in which `Q1`'s ceiling is breached on roughly half of all days. **The two readings of the
same sentence cannot both be right, and the test is designed so the data says which — or that
neither is.**

---

## §3 — CONSTRUCTION — every definition fixed here, before any data is read

| Term | Definition, fixed now |
|---|---|
| Instrument | **GBP/USD**, HistData M1, the only corpus this project holds |
| Pip | `0.0001` (`COMMON_PROTOCOL.md` §1, `mmm_lib.PIP`) |
| **Session day** | `mmm_lib.session_day` — the existing project definition, ending `17:00` New York. **Not invented here** |
| **Daily range** | `max(high) − min(low)` over the session day's M1 bars, in pips. ⚠ **This is a CHOICE and it is the generous one for the claim**: any narrower definition (body range, close-to-close) yields a *smaller* number and makes a 200-pip typical day *harder*, not easier |
| `ADR₁₅` | the mean of the previous **15** session days' ranges — **V16's own stated lookback**, `[00:09:31]` *"the last two weeks, 15 days"*. Used only as the descriptive control `N2`, never as a rule |

### §3a — THE ONE FILTER APPLIED

A session day is **included** iff all **96** fifteen-minute buckets of its 24-hour span carry at
least one M1 bar — the same completeness rule `PT-042` and `PT-043` used, unchanged. **Exclusions
are counted, named by date band, and reported.** No other filter.

### §3b — BOTH `D-031` ARMS, BOTH REPORTED

Arms `A` and `B` (the one-hour clock question) are both run and both reported. **A daily
high−low range is nearly arm-invariant by construction** — shifting the day boundary by an hour
moves a small amount of price in and out at the edges. **Prediction §7 commits to that in advance,
so an arm divergence would be a red flag about the harness rather than a finding about the market.**

---

## §4 — WINDOW AND DATA

| | |
|---|---|
| Primary window `W-D` | `D-035` **DEVELOPMENT**: 2013-01-06 → 2016-06-30 |
| Replication window `W-E` | `D-044` **EXTENSION**: 2017-01-01 → 2025-12-31 |
| Sealed | `2016-07-01 → 2016-12-31` — **`D-035` holdout, not on disk, not touched** |
| QA gate | `mmm_lib.qa_gate` must pass **per scope** before any bar is read |

⚠ **`W-E` is a REPLICATION, not a pooled sample.** The two windows are reported separately and are
never averaged. **The 2012 lesson is closer in time to `W-D`; `W-E` is the durability check.**

---

## §5 — OUTCOME MEASURES

| ID | Measure |
|---|---|
| **`O1`** | **`P(range > 200 pips)`** — the ceiling test |
| **`O2`** | **median daily range**, pips |
| **`O3`** | **mean daily range**, pips |
| **`O4`** | `P(150 ≤ range ≤ 250)` — the *"approximately 200"* band, generous at ±25% |
| **`O5`** | the **99th percentile** of daily range — what a real ceiling would look like |

## §5a — CONTROLS, FIXED NOW (`D-026` / `D-029`)

| ID | Control | Purpose |
|---|---|---|
| **`N1`** | Recompute every measure on **arm B** | `D-031`. Divergence here indicts the harness (§3b) |
| **`N2`** | Report `ADR₁₅`'s own distribution (median, mean, `P(ADR₁₅ > 200)`) | The lesson's *own* averaging window, so the claim is scored against the object the lesson names, not only against raw days |
| **`N3`** | Report the **per-year** median range across both windows | Guards against a single volatile regime (2016 Brexit, 2020) carrying the answer |
| **`N4`** | Report the count and date-band of **completeness exclusions** | `PT-043` lost ~24% of days at week boundaries and said so. Same disclosure here |

---

## §6 — DECISION RULE — FIXED NOW, BEFORE THE RUN

**Reading B, the CEILING** — *"do not exceed 200 pips on the average day"*:

| `O1` in `W-D` | Verdict on the ceiling reading |
|---|---|
| `≤ 0.02` | **SUPPORTED** — a real, rarely-breached limit |
| `0.02 < O1 ≤ 0.10` | **WEAKLY SUPPORTED** — a soft limit |
| `> 0.10` | ⛔ **CONTRADICTED AS STATED** — not a limit in any operative sense |

**Reading A, the TYPICAL day** — *"approximately 200 pips"*:

| `O2` (median) in `W-D` | Verdict on the typical reading |
|---|---|
| `150 ≤ O2 ≤ 250` | **SUPPORTED** |
| `100 ≤ O2 < 150` or `250 < O2 ≤ 300` | **PARTIALLY SUPPORTED** — right order of magnitude, wrong number |
| otherwise | ⛔ **CONTRADICTED AS STATED** |

**`W-E` is scored under the identical rule and reported beside `W-D`. If the two windows disagree,
BOTH are reported and NEITHER is called the answer** — that is a finding about regime, and it is
`A-095`'s recurring problem (a figure stated with no period) made concrete.

⚠ **NO MEASURE IS ADDED AFTER THE RUN.** If something interesting shows up that is not in §5, it
is reported as an **observation**, explicitly marked as not pre-registered, and it does not enter
any verdict.

---

## §7 — PREDICTIONS, COMMITTED BEFORE THE RUN

Written now so they can be wrong in public.

1. **`O2` will land between 90 and 130 pips**, i.e. **PARTIALLY SUPPORTED at best and more likely
   CONTRADICTED**. Basis: `BT_V10_0001` measured a **median weekly** range of 243.8 pips on this
   same corpus. A week containing five days cannot have a 243.8-pip median range if its days
   typically span 200.
2. **`O1` will be between 0.02 and 0.10** — so the CEILING reading will come out **WEAKLY
   SUPPORTED**, and *"200 pips"* will turn out to be a decent description of an unusually large
   day rather than an average one.
3. ⭐ **Therefore I predict the two readings of the same sentence will receive DIFFERENT verdicts**,
   and that the *ceiling* reading — the throwaway conspiratorial aside at `[00:30:12]` — will
   score **better** than the *typical* reading the lesson builds its arithmetic on.
4. **Arms A and B will agree to within 2 pips on `O2`** (§3b).
5. **`W-E` will show a LOWER median than `W-D`** — post-2017 GBP/USD is generally quieter than
   2013–2016 outside 2016 itself.

---

## §8 — WHAT A RESULT HERE WOULD AND WOULD NOT MEAN

**Would:** settle whether a specific, twice-stated, scope-carrying number in V16 describes the one
instrument this project holds.

**Would NOT:**
- say anything about pairs other than GBP/USD (§1b.3);
- test *why* the number is what it is — the lesson's mechanism (*"they are told by somebody"*) is
  **untestable in principle** from price data and is not being tested;
- bear on `A-100`. **A measured daily range is not the lesson's ADR**, because the lesson's ADR is
  still undefined (`A-100`) and its markers may repaint (`C-022`). **`ADR₁₅` in `N2` is THIS
  SESSION'S construction from V16's stated lookback, and it is a descriptive control, not the
  course's object.** Any later session that treats `N2` as *"the MMM ADR, measured"* is making the
  `A-082` error;
- unblock anything. **No `M`, `W`, entry, exit or level is computed anywhere in this test.**

---

## §9 — LIMITATIONS DECLARED IN ADVANCE

1. **One instrument** (§1b.3). The claim is about many.
2. **2013→2025 data against a 2012 claim.** The corpus does not reach 2012. Every previous test in
   this project carries the same gap and it is not smaller here.
3. **`max(high) − min(low)` is the most generous range definition available** (§3). If the claim
   fails on this definition it fails on every narrower one; if it passes, the pass is on the
   friendliest possible reading.
4. **The completeness filter removes days, and days are not missing at random** — week boundaries
   and holidays go first. `N4` reports the count and the bands.
5. **`ADR₁₅` uses "15 days" and the lesson also says "two weeks", which is 10 or 14** (`A-100`,
   source notes §6). **`N2` is computed at 15 because that is the number actually spoken; the
   ambiguity is NOT resolved by running it.**
