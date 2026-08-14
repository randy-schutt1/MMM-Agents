# PT-042 — "The lock": does a session extreme that holds for one hour become the day's extreme?

```text
STATUS:      PRE-REGISTERED — NOTHING BELOW HAS BEEN RUN
WRITTEN:     2026-08-14, by the V14 student session, branch video/v14
ATTESTATION: The session that wrote this file has loaded NO price series for this
             test, computed NO outcome, and opened NO chart. `run_pt042.py` DOES
             NOT EXIST at the commit that adds this file, and that is checkable:
                 git cat-file -e <this commit>:06_MANUAL_BACKTEST/scripts/run_pt042.py
             must return ABSENT.
             Every boundary in §6 was chosen from the lesson's own numbers and
             from PT-041's precedent, before any of them was measured.
```

Governing: `BACKTEST_EVIDENCE_STANDARD.md` · `COMMON_PROTOCOL.md` · `D-005`, `D-007`, `D-009`,
`D-010`, `D-026`, `D-027`, `D-029`, `D-030`, `D-031`, `D-035`, `D-036a`.

---

## 1. THE CLAIM, IN THE COURSE'S OWN WORDS

**V14 is the first lesson in this corpus to state a complete real-time method in numbers it
supplies itself.** The claim under test is **printed** on the assignment slide
(`04_SCREENSHOTS/V14/V14_00-26-50_assignment-slide-the-high-low-board-drill.png`):

```text
 •  At 1am NYC time record the high and low of the majors
 •  Find a pair that is trading in the middle of the range
 •  Wait for the dealer to extend either level mark it down, wait for him to hit it
    several more times write it down again.
 •  When the dealer pulls off of the level and fails to hit it again for 1 hour take a position
 •  Stop loss level is 5 pips above/ below that number that appears on the board.
```

and spoken, with the two figures the slide omits:

> `[00:27:28]` *"**Identify the pairs that have not made more than a 50 pip range.**"*
> `[00:32:38]` *"Let it run, **aim for 30 to 50 pips**."*

**The load-bearing premise is stated separately and more strongly:**

> `[00:35:51]` *"you're looking for **the lock** — you're looking for **the number that's the highest
> point on the board for the day**."*
> `[00:37:53]` *"the strongest resistance in the day is 32 30. **It's the high of the day.** The
> dealer doesn't want another pip, no more."*
> `[00:46:05]` *"An extension of the high or an extension of the low — **after that number is a lock
> for one hour**, one and a half hours, ninety minutes."*

**In one sentence: once an extended session extreme has gone one hour without being exceeded, the
course says it IS the day's extreme.** That is a falsifiable claim about price, and `O1` measures it.

### 1a. BINDING CAVEATS — reproduced here because a reader of the OUTPUT must see them

1. ⚠️ **THIS TESTS A DRILL'S OWN CLAIM, NOT ADOPTED DOCTRINE.** `[00:32:42]` *"That's a drill"*;
   `[00:37:12]` *"a very important drill **to help you understand the candles**"*; `[00:32:25]`
   *"open a long position **in demo**"*. The speaker also says `[00:46:20]` *"technically, Keith,
   **you will be able to trade off of the board only**"*. **The tension is real and unresolved
   (`V14_INTERPRETATION.md` Q4).** No result here may be cited as the method's stop or target, and
   **the 5-pip stop and 30-pip target appear nowhere in `12_MASTER_SPEC/` or `13_MACHINE_SPEC/`.**
   This is the `A-082` class of error and it is fenced in advance, not afterwards.
2. ⚠️ **ONE OF THE COURSE'S SIX STEPS IS EXCLUDED UNDER `D-030`.** *"Find a pair that is trading in
   the middle of the range"* has **no tolerance anywhere in Tier 1 or Tier 2**, and the speaker's own
   two worked examples sit at the **45.5th** and **20.0th** percentile of their ranges (`A-089`).
   **Excluding it makes the tested population LARGER and LESS SELECTIVE than the course intends**,
   so this test is a **lower bound** on the rule as taught. **Declared here, in advance.**
3. ⚠️ **THE COURSE SAYS "THE MAJORS"; THIS TESTS GBP/USD ONLY** (`D-007`, and it is the only corpus
   on disk). The drill's own selection logic — *"narrow it down to two or three pairs"* `[00:38:15]`
   — **cannot be reproduced on one instrument.** A cross-sectional pick is part of the method and
   is not tested.
4. ⚠️ **THE BOARD IS A TICK OBJECT; M1 IS A PROXY.** MT4's pop-up prices board updates on every
   tick. This corpus is **M1 OHLC**. A one-minute bar's high/low is the best available proxy and it
   is **not** the same object: intra-minute excursions that set and lose a level inside 60 seconds
   are invisible here. **This biases toward FEWER extensions and FEWER stopwatch resets**, i.e.
   toward locks firing slightly **earlier** than a tick board would show.
5. **No spread, commission or slippage.** The lesson's own numbers are quoted *"with the spread"*
   `[00:09:43]`, so a 5-pip stop is materially inside a realistic 2012 GBP/USD spread band. **Every
   figure here is a distance, not a P&L**, and §7 says so again.

---

## 2. THE QUESTION

**Q1 (the premise).** After an extended session extreme has held one hour without being exceeded,
how often is it still the session day's extreme at the 17:00 close?

**Q2 (the trade).** Taking the drill exactly as specified — enter at the lock, stop 5 pips beyond
the locked number, target 30 pips — how often does the target come before the stop?

---

## 3. CONSTRUCTION — every definition fixed here, before any data is read

| ID | Definition |
|---|---|
| **`C-1`** | **Session day** `D` = `[D-1 17:00, D 17:00)` on the arm's clock — the project's standing convention (`mmm_lib.session_day`). ⭐ **Corroborated by the lesson itself**: `[00:41:50]` *"the high's all the way up here on the big board — **you can't reset your big board**"*, i.e. the board does **not** restart at the New York session |
| **`C-2`** | **`T0` = 01:00** on the arm's clock — printed *"1am NYC time"*, spoken `[00:27:05]` *"1 a.m. New York time"* |
| **`C-3`** | **Board range** = `[min low, max high]` over all M1 bars in `[D-1 17:00, T0]` inclusive. `boardHigh`, `boardLow` |
| **`C-4`** | **Extension** = the first M1 bar strictly after `T0` with `high > boardHigh` (UP) or `low < boardLow` (DOWN). **If one bar breaches both, the day is EXCLUDED as ambiguous** and the count is reported |
| **`C-5`** | **Running extreme** = the extreme so far in the extension direction, from the extension bar onward |
| **`C-6`** | **Stopwatch** = `[00:31:33]` *"every time the dealer extends the high or low, start a stopwatch"*. **Any strictly-new extreme RESETS the timer to zero** |
| **`C-7`** | **LOCK** fires at the first M1 bar `t` such that **60 consecutive minutes** have elapsed since the last new extreme. **`L` = the running extreme at that moment** |
| **`C-8`** | **Deadline.** The lock must fire **at or before `D 17:00`**. If it does not, the day yields **no trade** and is counted as `no-lock` |
| **`C-9`** | **Direction** = counter to the extension. UP-extension → **SHORT**; DOWN-extension → **LONG** |
| **`C-10`** | **Entry (PRIMARY)** = the **close of the lock bar**. Fully determined by the rule; invents nothing |
| **`C-11`** | **Stop** = `L + 5 pips` (short) / `L − 5 pips` (long) — printed |
| **`C-12`** | **Target** = **30 pips** from entry — the low end of *"30 to 50"* `[00:32:38]`. The 50 end is reported as `O3`, not used in the verdict |
| **`C-13`** | **Resolution** is walked forward bar by bar to `D 17:00`. **If both stop and target fall inside one M1 bar, the STOP is taken** — the conservative assignment, fixed here, not after seeing how often it happens |
| **`C-14`** | **Completeness gate.** A session day qualifies only if it carries M1 bars in **every** hour of `[D-1 17:00, T0]` and at least **90%** of expected minutes in `[T0, D 17:00)`. Excluded days are **named** in the output |
| **`C-15`** | **Pip** = `0.0001` (`COMMON_PROTOCOL.md` §1) |

### 3a. THE ONE FILTER APPLIED

**`F1` — board range ≤ 50 pips.** `[00:27:28]`, `[00:29:34]`, `[00:38:35]`. Inclusive at 50.

**`F2` — "trading in the middle of the range": EXCLUDED under `D-030`.** See §1a caveat 2 and
`A-089`. **It is not approximated and no percentile is invented.**

### 3b. THE PRE-REGISTERED SENSITIVITY ARM — `A-090`

The two spoken examples give **different** entry offsets: `[00:32:25]` **10 pips inside** `L`;
`[00:35:23]` **5 to 8 pips inside**. The printed slide gives none.

> **`S1` — limit entry 10 pips inside `L`**, same stop and target, filled only if price trades
> there before the stop or the 17:00 close. **The FILL RATE is reported alongside**, because an
> unfilled limit is not a winning trade. **`C-10` remains PRIMARY.**

---

## 4. WINDOW, ARMS AND DATA

| Item | Value |
|---|---|
| **Instrument** | **GBP/USD only** (`D-007`) |
| **Window** | **`W-B` = 2014-01-05 → 2015-12-31.** ✅ Wholly inside `DEVELOPMENT` (`D-035`, boundary 2016-07-01). **The same window `PT-041` used**, so the two are comparable |
| **Data** | HistData GBP/USD **M1** CSV corpus, `datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record (`D-036a`). **The 2017–2025 extension is NOT used**: `HISTDATA_RECENCY_CHECK.md` is a feasibility finding that "authorises nothing", and extending the corpus needs a new owner decision that has not been made |
| **Arms** | **BOTH `D-031` arms, both reported.** `A` = fixed `UTC−5`; `B` = `America/New_York`, DST-aware. Reporting only the better arm is `E09` + `E24` |
| **QA gate** | `qa_histdata_m1.py` C1–C4 must PASS; cite the report |

---

## 5. OUTCOME MEASURES

| ID | Measure | Role |
|---|---|---|
| **`O1`** | **P(`L` is still the session day's extreme at `D 17:00`)** | ⭐ **THE PREMISE.** Q1 |
| **`O2`** | **P(target 30 reached before stop)** | ⭐ **THE TRADE.** Q2 |
| **`O3`** | P(50 pips reached before stop) | reported, not in the verdict |
| **`O4`** | **Median MFE** in pips from entry, to the 17:00 close, ignoring the stop | descriptive |
| **`O5`** | Median time from `T0` to the lock, in minutes | descriptive — how long the drill asks a student to sit |
| **`O6`** | `S1` fill rate, and `O2` computed on filled `S1` entries only | the `A-090` sensitivity |

## 5a. CONTROLS — `D-026` / `D-029`, AND V13 R1's `M2` TAKEN UP EXPLICITLY

> ⚠️ **`V13_REVIEW_R1.md` `M2` charged `PT-041` with asserting a direction for a control that its
> committed numbers did not show, because the control's headline statistics were never computed.
> This test does not repeat that.** **Every control below reports the SAME four statistics as the
> rule arm — `O1`, `O2`, `O3`, `O4` — computed, printed, and committed.** No control is described
> in prose without its numbers next to it.

| ID | Control | Construction |
|---|---|---|
| **`N1`** | **Matched random entry** (`D-026` required form) | Same session days, same eligible clock window `[T0, 17:00)`, same 5-pip stop and 30-pip target, **direction drawn at random**, `n` matched to the rule arm. **1,000 iterations, seed `20260812`** (`COMMON_PROTOCOL.md` §5) |
| **`N4`** | **Natural control — the no-lock days** | Session days that pass `F1` and extend, but where **no lock fires before 17:00**. For these, `O1` is computed on **the 01:00 board extreme that was extended**. ⭐ **This is the comparison that matters**: it isolates what the *one-hour hold* adds over merely having extended |

**Baselines are computed and printed BEFORE the rule arm's aggregate is looked at**
(`COMMON_PROTOCOL.md` §9.1).

---

## 6. DECISION RULE — FIXED NOW, BEFORE THE RUN

**Boundaries and their justification, chosen before measurement:**

- **`O1 ≥ 0.80`.** The course's claim is not hedged — *"**It's** the high of the day"*, *"the
  dealer doesn't want another pip"*. **`PT-041` used `≥ 0.80` for its premise measure** and this
  reuses it rather than inventing a friendlier one.
- **`O2 ≥ 0.50`.** A 30-pip target against a stop 5 pips beyond `L` is a reward-to-risk well above
  1:1 on any entry offset in §3b, so **a coin-flip hit rate is the minimum that makes the drill
  worth a student's two weeks.** It is also the boundary `PT-041` used for its `O1`.
- **`n ≥ 30`** per arm (`BACKTEST_EVIDENCE_STANDARD.md` §4.1).

```text
SUPPORTED            O1 >= 0.80  AND  O2 >= 0.50   in BOTH arms, n >= 30 in both
PARTIALLY SUPPORTED  exactly ONE of the two holds  in BOTH arms, n >= 30 in both
NOT SUPPORTED        neither holds
SAMPLE INSUFFICIENT  n < 30 in either arm -> descriptive only, NO rate quoted
                     anywhere without that label in the same sentence
ARMS DISAGREE        if the two arms straddle a boundary, that is a FINDING and is
                     reported as the headline. It is NEVER a selection criterion.
```

**Every measure is reported whether or not it is flattering** (`E25`,
`BACKTEST_EVIDENCE_STANDARD.md` §4.3).

---

## 7. WHAT A RESULT HERE WOULD AND WOULD NOT MEAN

**Would:** `O1` is a clean test of a premise the course states in the strongest terms, on an object
(*"the day's high"*) that is arithmetic once `C-1` is fixed. **It needs no undefined term**, which
is why this test exists where most V01–V13 claims could not be tested at all.

**Would NOT:**

- It is **not** a P&L result. No spread, no slippage, and §1a caveat 5 notes a 5-pip stop sits
  inside a realistic 2012 spread band.
- It is **not** a test of the method **as taught**, because `F2` is excluded (`A-089`) and the
  cross-sectional pick across "the majors" is not reproducible on one instrument.
- It says **nothing** about `A-077`'s **weekly**-scale lock. `A-094` records that V14's one hour and
  V10's *"15, 16 hours"* are figures for different objects. **A result here must not be
  transplanted onto V10's safety trade.**
- A **pass** would not make the drill doctrine — see caveat 1.
- A **fail** would not show the course wrong about *"the majors"*; it would show it wrong about
  GBP/USD in 2014–2015 under the six computable steps.

---

## 8. LIMITATIONS DECLARED IN ADVANCE

1. `F2` excluded (`A-089`) — the population is **larger and less selective** than the course's.
2. One instrument, not six (`D-007`).
3. M1 as a proxy for a tick board (§1a caveat 4), biasing locks **earlier**.
4. Entry offset ambiguous (`A-090`) — handled by `C-10` primary + `S1` sensitivity, both declared.
5. `mmm_lib.SEED` is a single fixed constant, which `REVIEW_INDEX.md` **item 113** records as an
   open defect (a result's dependence on one seed is unmeasured). **This test inherits it.** V13 R1
   measured the practical size of that dependence at **≤ 0.002** on `PT-041`'s point estimates
   under a different seed; that is reassuring and it is **not** a discharge of item 113.
6. No sensitivity is run on the **60-minute** lock itself. `[00:46:05]` offers *"one hour, one and a
   half hours, ninety minutes"* and `[00:34:36]` *"45 minutes, an hour, hour and 15"*. **The
   PRINTED slide says `1 hour` and that is what is tested.** ⚠️ **A post-hoc sweep over the lock
   duration would be threshold-shopping** and is forbidden to the run session; **if it is ever
   wanted it is a NEW `PT` number**, pre-registered separately.
