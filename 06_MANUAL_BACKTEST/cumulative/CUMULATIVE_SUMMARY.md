# CUMULATIVE SUMMARY — every pre-registered test run through V16

```text
STATUS:   42 pre-registered PT files exist through V16 (PT-001…PT-036,
          PT-039…PT-044; there is no PT-037 and no PT-038 -- see §1a). 34 have a
          committed BT record; 33 were ACTUALLY EXECUTED AND REPORTED (PT-022 is superseded,
          its period unobtainable); 8 have never been run.
COVERAGE: this file lists EVERY test that has been run, whatever it found.
          `BACKTEST_EVIDENCE_STANDARD.md` §4.3: "A summary naming only the tests
          that worked is invalid." Nothing here is omitted for being null.
UPDATED:  2026-08-15, at the 75% cumulative checkpoint, adding PT-043 and PT-044.
```

> ### ⚠ WHY THIS FILE WAS REWRITTEN, AND WHAT WAS WRONG WITH IT
>
> `00_SYSTEM/GAP_AUDIT_2026-08-14.md` found this summary **stale and not quotable as current**,
> and it was right on every count. As of its previous revision (dated 2026-08-13) it:
>
> 1. headlined ***"21 of the 33 pre-registered PT files"*** — **both numbers wrong.** 40 PT
>    files exist, not 33, and 31 have been executed and reported, not 21;
> 2. **carried no row at all for `PT-034`, `PT-035`, `PT-036`, `PT-039`, `PT-040`, `PT-041` or
>    `PT-042`** — seven tests, comprising **every test run from V08 onward** and all three of
>    the recent honest negatives that the V14 review calls the project's strongest output;
> 3. **did not sum to its own headline.** §1's disposition column totalled **22** against a
>    stated total of **21**, and §2's three tables listed **24** rows against the same 21.
>
> This is the **maintained-prose-over-unmaintained-table** decay that `REVIEW_INDEX.md` open
> item 96 charges against `COURSE_PROGRESS.md` and `REVIEW_INDEX.md`'s own SEVERITY TOTALS. This
> was the third instance, and it was in the one file a reader would go to for the backtest
> picture. **Item 96's durable fix — declare which layer is authoritative, or delete the derived
> table — is still owed and is still unmade.** This refresh corrects the contents; it does not
> close item 96, and a fourth instance is expected until item 96 is actually done.
>
> Every figure below was re-read out of the named `BT_*` record for its refresh rather than
> carried forward. Through V16 the arithmetic is: **7 + 5 + 5 + 12 + 3 + 1 + 1 = 34 PT ids with
> a committed record, plus 8 never run, = 42 pre-registered PT files through PT-044.** Later
> lessons have their own records but are outside this V01–V16 checkpoint view.

**Summaries never replace individual observations.** Every figure below is a pointer;
the record is the `BT_VXX_NNNN.md` file named beside it, and the caveats that govern
each number live there, not here.

---

## 1. THE HEADLINE COUNT

Across the **34** PT ids through V16 that have a committed `BT_*` record:

| Disposition | Count | Tests |
|---|---:|---|
| **Clears its own pre-registered null** | **7** | `PT-007`, `PT-017`, `PT-018`, `PT-026`, `PT-027`, `PT-032`, `PT-034` |
| **`SPLIT` / `PARTIALLY SUPPORTED`** | **5** | `PT-004`, `PT-029`, `PT-039`, `PT-041`, `PT-044` |
| **`CONTRADICTED`** — the data runs against the taught claim | **5** | `PT-006`, `PT-028`, `PT-030`, `PT-035`, `PT-036` |
| **`NOT SUPPORTED` / `INDISTINGUISHABLE FROM THE NULL`** | **12** | `PT-002`, `PT-003`, `PT-005`, `PT-014`, `PT-015`, `PT-016`, `PT-020`, `PT-021`, `PT-025`, `PT-031`, `PT-042`, `PT-043` |
| **`INDETERMINATE` / `DESCRIPTIVE` only** | **3** | `PT-023`, `PT-024`, `PT-033` |
| **`MATERIAL`** — measures an *ambiguity*, not a taught claim | **1** | `PT-040` |
| **Superseded, period unobtainable** | **1** | `PT-022` |
| **Total with a committed record** | **34** | of which **33 executed and reported** |

**Never run:** **8** — `PT-008`, `PT-009`, `PT-010`, `PT-011`, `PT-012`, `PT-013`, `PT-019` (all
**retired unrun** as non-conforming under `D-035`, and **all re-issued**) and `PT-001`, which
still pins its period at run time. `PT-002`'s **W-C arm** is likewise retired unrun; its **W-A
arm** was run and is listed below.

⚠ **Two of the seven "clears its own null" results are partial and one is nearly empty.**
`PT-017` and `PT-018` clear on **timing only**, `PT-026` clears **trivially** (see §2a), and
`PT-034`'s headline form is **arithmetically guaranteed and was shown to be so before the run**
(see §2d). Read the count with §3 attached; it is not a scoreboard.

### 1a. There is no `PT-037` and no `PT-038`, and a session expecting them will be confused

Both numbers were **reserved by V10** — `PT-037` for a path-length reading of `M1`, `PT-038` for
the safety trade — and **neither was ever filed as a pre-registration.** V11's hold-duration test
was filed and run as `PT-037`, then **re-issued as `PT-039`** by owner ruling of 2026-08-13
(*"Move V11 not V10 since V11 is after"*), with nothing but the label changed. The full account
is in `PT-039`'s own banner. The gap between `PT-036` and `PT-039` in `PRE_REGISTERED/` is
therefore expected, not a missing file.

---

## 2. THE FULL TABLE

### 2a. Weekly-scale — the eight `D-035` re-issues, plus `PT-002`'s daily arm

All on **`W-C′` 2013-01-06 → 2016-06-30**, the HistData corpus (`D-036a`), 180 trading
weeks unless stated, both `D-031` arms, seed `20260812`.

| PT | Question | Record | **Disposition** |
|---|---|---|---|
| **PT-002** (W-A arm) | Do **daily** extremes cluster at the six printed boundaries? | `V01/BT_V01_0001` | **NOT SUPPORTED** — N2 pct 60.6 / 39.1. The apparent 35% excess is the **arcsine** endpoint artifact |
| **PT-025** | Do **weekly** extremes cluster at the six boundaries? | `V01/BT_V01_0002` | **NOT SUPPORTED** — N2 pct 76.6 / 76.8; **below** N3 (20.8 / 29.0) |
| **PT-026** | Is the first-eight-hours range of the week cut? | `V03/BT_V03_0003` | **SUPPORTED TRIVIALLY, NOT SPECIAL** — cut in **180/180** weeks; rank **7 of 23** on a matched basis |
| **PT-027** | Does the first move out of the week's opening range reverse? | `V01/BT_V01_0003` | **SUPPORTED** — the prohibited trade returns **−5.16 pips**, N1 pct **0.9** |
| **PT-028** | On which weekday does the week make its high and low? | `V01/BT_V01_0004` | **CONTRADICTED** — mode is **Friday** for both, not Tue/Wed; χ² p < 0.001 |
| **PT-029** | Is the rest of the week a unidirectional swing? | `V02/BT_V02_0008` | **SPLIT** — clears all three controls (100/100/96.5) at an absolute efficiency of **0.1153** |
| **PT-030** | Is the previous week's extreme a barrier? (n = 178) | `V02/BT_V02_0009` | **CONTRADICTED** as absolute; **NOT SUPPORTED** statistically — breached ~half the time |
| **PT-031** | Are Sunday and Monday the accumulation phase? | `V02/BT_V02_0010` | **NOT SUPPORTED** on the governing metric — mid-pack; **verdict depends on the normalisation** |
| **PT-032** | The weekend gap and the Friday-flat rationale | `V01/BT_V01_0005` | **SUPPORTED** — **20.0%** of weekends exceed the course's own 18-pip stop |

### 2b. Day-scale — the twelve run in the earlier batch (`df7eab6`, `9eb2d0c`)

W-A / W-B on the same corpus. Summarised from their own records.

| PT | Question | Record | **Disposition** |
|---|---|---|---|
| PT-003 | Is 5pm the day boundary? | `V02/BT_V02_0003` | **INDISTINGUISHABLE FROM THE NULL** |
| PT-004 | Are the Dead Gap and the session gaps quiet? | `V02/BT_V02_0004` | **SPLIT** — the Dead Gap holds, the half-hour gaps do not |
| PT-005 | The 8:00 / 9:30 stop-hunt | `V02/BT_V02_0005` | **INDISTINGUISHABLE FROM THE NULL** — peak is 08:30–09:00, not 09:30 |
| PT-006 | Does a new session reverse the old one? | `V02/BT_V02_0006` | **CONTRADICTED** on Arm A — London **continues** |
| PT-007 | The 8:31 and 4:30 vector-candle windows | `V02/BT_V02_0007` | **SUPPORTED** on Arm A — ranks 1 and 2 of 96; cause unidentified |
| PT-014 | Is 25–50 pips the modal excursion? | `V04/BT_V04_0001` | **INDISTINGUISHABLE FROM THE NULL** |
| PT-015 | Does a >50-pip ceiling exist? | `V04/BT_V04_0002` | **INDISTINGUISHABLE FROM THE NULL** on hit rate |
| PT-016 | "Asian range under 50" as a filter | `V03/BT_V03_0001` | **INDISTINGUISHABLE FROM THE NULL** |
| PT-017 | "In profit in 15 to 45 minutes. Guaranteed." | `V04/BT_V04_0003` | **SUPPORTED** on timing of meaningful profit; null on anything bankable |
| PT-018 | The two-hour time stop | `V02/BT_V02_0001` | **SUPPORTED** on the underlying claim; hit rate `DESCRIPTIVE` |
| PT-020 | The London-open asymmetric conditional | `V03/BT_V03_0002` | **INDISTINGUISHABLE FROM THE NULL**; variance claim **contradicted in direction** |
| PT-021 | DNC and the straightaway test | `V02/BT_V02_0002` | **INDISTINGUISHABLE FROM THE NULL** |

### 2c. Guest-material and concurrent-session tests

| PT | Record | **Disposition** |
|---|---|---|
| PT-022 | `V06/BT_V06_0001` | **SUPERSEDED** — the period is unobtainable. Not executed, and it is counted as superseded rather than as a result |
| PT-023 | `V06/BT_V06_0001` | **`DESCRIPTIVE`** — n = 12, below the floor **by design**, and partly contaminated |
| PT-024 | `V06/BT_V06_0001` | **`DESCRIPTIVE`** — the same question on a second vendor; see that file |
| PT-033 | `V07/BT_V07_0001` | **`INDETERMINATE`** — and the day boundary is why |

### 2d. ⭐ V08 onward — the seven tests this summary was missing until 2026-08-14

All figures re-read from the named record for this refresh. Where two numbers appear separated by
a slash they are the two `D-031` arms, reported separately and **never pooled**.

| PT | Lesson | Question | Record | **Disposition** |
|---|---|---|---|---|
| **PT-034** | V08 | *"Risk Reward to 3:1 or greater"* — the "crown jewel" | `V08/BT_V08_0001` | **`CONFIRMED AS TAUGHT`** — resolution rate **0.7046–0.7676** across all four cells against a 0.25 break-even, `n` = 1,803–2,172 per cell. ⚠ **Read narrowly.** The headline 3:1 form is **arithmetic, not a finding** — an entry within `X` pips of the day's extreme cannot draw down more than `X`. The real result is the size of the **hindsight** advantage (`N1` = **0.243** → 0.705–0.768, a factor of **2.9–3.2**), and **that advantage is entirely attributable to knowing where the day's extreme is, which neither V07 nor V08 teaches** (`A-056`, `A-061`). The record also discloses a **defect in its own decision rule** (§6): the second condition — beating `N1`'s 95th percentile — came back **100.0 in all four cells** and is near-tautological under hindsight |
| **PT-035** | V09 | *"It's highly unlikely we're gonna lose three or four times in a row"* | `V09/BT_V09_0001` | **`CONTRADICTED AS STATED`** — and the contradiction rests on **closed-form arithmetic written into `PT-035` §2c before the corpus was touched**, at every hit rate this corpus has ever measured. A four-loss run reaches ≥10% in all four cells. ⚠ **The MEASURED route is `INDETERMINATE`**: `N3`, the pre-registered sanity control, **FAILED**, which voids `O3`'s clustering statistic entirely (`INVALID`, not hedged). The verdict survives because it never needed the measurement |
| **PT-036** | V10 | The **600–1000 pip week** and the **Friday close 25–50 off both extremes** | `V10/BT_V10_0001` | **`CONTRADICTED AS STATED`, twice.** `M1`: a 600–1000 pip week occurs in **0 of 180 weeks (0.00%)**; observed median **243.8** pips. `M2`: the joint band is met in **13/178 = 7.30%** (arm B 5.62%) against a `< 20%` contradiction threshold — and it **fails its own specificity control**, with Friday ranking **4th of 5 weekdays** and Thursday satisfying the band nearly twice as often. ⚠ **V10's headline SAFETY TRADE was NOT tested, and that omission is itself a reported finding** — five of its seven conditions rest on undefined terms and `D-030` forbids approximating them |
| **PT-039** | V11 | *"the low has to hold — how long? 30 to 90 minutes"* | `V11/BT_V11_0001` | **`SPLIT` / `PARTIALLY SUPPORTED`** — four measures, and they disagree by design. `M1a` **PARTIALLY SUPPORTED** (19.24% vs `N1` 3.43%, margin **+15.80 pp**); `M1b` **CONFIRMED AS STATED** (+12.17 pp across the 30→90 band); `M1c` **CONTRADICTED AS STATED** — **no feature at 30 and none at 90, in both arms**; `M1d` **PARTIALLY SUPPORTED** — the margin survives in only **3 of 6** time-of-day strata. **The direction is supported and the named numbers are not**, and most of the apparent effect tracks **how much of the session is left**, not how long the low held |
| **PT-040** | V12 | Does `A-084`'s smoothing ambiguity change the RSI thresholds V11 states? | `V12/BT_V12_0001` | **`MATERIAL`** — this measures **an ambiguity, not a taught claim**, and so appears in no supported/contradicted column. Side disagreement `M = 5.16 pp` on the 50-line against a pre-registered **`> 5.0 pp` = MATERIAL** boundary, `n = 24,730` bars; `N2` (**10.661 pp**) and `N3` (**12.147 pp**) land in the same band. ⚠ **The result is the opposite of what the session wanted:** `A-084` is not a bookkeeping ambiguity, and every RSI threshold V11 states is under-determined until it is resolved |
| **PT-041** | V13 | *"50 to 100 pips on the table… you'll hit your 50 pips"* | `V13/BT_V13_0001` | **`PARTIALLY SUPPORTED`** — **the distance is real, the promise is not.** Median MFE **56.8 / 52.9 pips**, and `O1` beats a same-metric control by **+44.9 / +42.2 pp** against a `≥ +10 pp` clause — four times the margin required. But `O4`, **the claim's own premise** that the dealer comes back into the Asian levels, holds only **0.704 / 0.701** against a pre-registered `≥ 0.80`, and `O2` reaches **0.630 / 0.642** against `≥ 0.70`. Both boundaries were fixed before the runner existed and both are honoured. ⚠ §5's named control was **DEFECTIVE in a direction that flattered the claim**; a like-for-like control was added at run time and **both are reported** |
| **PT-042** | V14 | "The lock" — does a session extreme that holds one hour become the day's extreme? | `V14/BT_V14_0001` | **`NOT SUPPORTED`** — **the distance is real, the premise is not.** `O1` = **0.3461 / 0.3041** against `≥ 0.80` — a **45-point miss**, wrong about two days in three; `O2` = **0.4607 / 0.4433** against `≥ 0.50`; `n` = **471 / 467**. ⚠ **This is a precisely located negative, not an empty one:** median MFE from entry is **40.10 / 40.40 pips** against a matched-random **18.90 / 20.30**, and `O2` **doubles** matched-random (0.4607 vs 0.2251). The record also discloses **two defects in `PT-042` itself**, owed an amendment before any re-issue: `N4` is degenerate (`n = 0`), and §5a underspecified `N1`'s `O1` construction in a direction that flatters the rule arm |

### 2e. V15–V16 additions required by the 75% checkpoint

| PT | Lesson | Question | Record | **Disposition** |
|---|---|---|---|---|
| **PT-043** | V15 | Does the daily close normally sit 25–50 pips off its own high or low? | `V15/BT_V15_0001` | **`NOT SUPPORTED`** on the headline `or` reading: 36.4% versus a same-day random-minute control of 37.6%. The stricter `and` reading is **CONTRADICTED AS STATED** at 9.4%. All four cells agree; no closing-location edge is established. |
| **PT-044** | V16 | Is roughly 200 pips a typical GBP/USD day or a ceiling? | `V16/BT_V16_0001` | **`SPLIT` across fixed windows.** The typical-day reading is **PARTIALLY SUPPORTED** in W-D (median 102.6 pips under the test's half-of-200 interpretation) and **CONTRADICTED AS STATED** in W-E (92.3); both are reported and neither is selected. The 200-pip ceiling reading is only **WEAKLY SUPPORTED**. One pair cannot establish the claim's every-pair scope. |

---

## 3. WHAT SURVIVES, AND WHAT DOES NOT

**Four claims clear their own pre-registered nulls in a way that means anything**, and none of
them is an entry rule:

1. **`PT-032` — the Friday-flat rationale.** One weekend in five gaps past the 18-pip stop
   the course itself teaches, and the figure is a **lower bound** (no spread in the corpus).
   **The clearest supportable instruction in V01**, and the only one whose rationale is
   mechanical rather than pattern-based.
2. **`PT-027` — "do not take the first move of the week".** The prohibited trade loses
   5.16 pips where a matched random entry is break-even; **N1 percentile 0.9**. The
   prohibition is doing real work.
3. **`PT-007` — the 8:31 and 4:30 clock windows.** Ranks 1 and 2 of 96 on Arm A. **The cause
   is unidentified and the mundane candidate — the release calendar — is strongly indicated.**
4. **`PT-017` / `PT-018`** — partial, on timing rather than on anything bankable.

**Three more clear a null and should not be read as support.** `PT-026` clears **trivially** —
the week's first eight hours are cut in 180/180 weeks, but rank **7 of 23** on a matched basis.
`PT-034` clears on a form that is **arithmetically guaranteed**, and what it actually measures is
the size of a hindsight advantage the course does not teach a trader to obtain.

**Five claims are contradicted by the data**, not merely unsupported:

- **`PT-028`** — the week's extremes print on **Friday**, and Tuesday/Wednesday are the two
  most *depleted* cells. The taught mid-week turn is the opposite of what GBP/USD did.
- **`PT-030`** — *"they will not go below last week's peak formation"* is stated absolutely
  and is breached in about half of weeks, by a median of 76–101 pips.
- **`PT-006`** — a new session **continues** the old one's direction rather than reversing it.
- **`PT-035`** — *"highly unlikely to lose three or four in a row"* is false at the course's own
  claimed accuracy. At >50%, P(a four-loss run in 200 trades) ≈ **99.9%**; you would need
  **p ≥ 84.2%** for the claim to hold.
- **`PT-036`** — **both** of V10's quantitative claims, and the second also fails its own
  specificity control.

### 3a. ⭐ THE HONEST HEADLINE, NOW THAT V08–V14 ARE IN THE TABLE

The seven tests added in §2d change what this summary says, and the change is the finding:

> **The direction and the distance are frequently real. The specific numeric premise almost
> never holds as stated.**

The three most recent tests say it three different ways, and **each was pre-registered before its
runner existed**: `PT-041` — *the distance is real, the promise is not*; `PT-042` — *the distance
is real, the premise is not*; `PT-036` — contradicted as stated, twice, with the pip-vs-point
rescue also failing. **A `NOT SUPPORTED` verdict of this shape is not an empty result — it is a
precisely located one**, and it is the strongest output the project has produced.

**A recurring mechanism explains several of the nulls, and it is worth stating once.** The
extremes of a random-walk path concentrate at the **edges of any window**, wherever the edges
are placed — the arcsine law. It is measured directly in `BT_V01_0001` §2 at day scale and
reappears in `BT_V01_0004` §3 at week scale. **It makes boundary-clustering claims look true
against a naive uniform-time expectation and false against a shift control**, and it is why
`PT-002` and `PT-025` both return null while their raw excess looks like +31–35%.

---

## 4. SIX PLACES WHERE THE MEASUREMENT ALMOST PRODUCED A FALSE POSITIVE

Recorded because each was caught by a pre-registered control or a disclosed check, and
each would otherwise have been reported as a finding:

| # | Test | What would have been reported | What the check showed |
|---|---|---|---|
| 1 | `PT-002` / `PT-025` | "+35% clustering at the six boundaries" | The arcsine artifact. N2 absorbs it; the analytic null cannot |
| 2 | `PT-026` | "the week-open block ranks **1 of 30**" | Outcome-window confound. Matched basis: **7 of 23** |
| 3 | `PT-031` | "Sun+Mon is the quietest span in 63% of weeks" | A 31-hour span against 48-hour ones. Normalised: **mid-pack** |
| 4 | `PT-025` | N3 percentile 8.3 (raw share) | The real week boundaries coincide with 17:00 and add no covered area; corrected: **20.8** |
| 5 | `PT-027` | 66,443 "later breaches" in 180 weeks | Bars spent outside the block, not breach events. Corrected: **1,586** |
| 6 | **`PT-041`** | *the claim clears its control comfortably* | §5's **named control was not like-for-like** and would have **understated the baseline and flattered the claim**. A same-metric control was added at run time; **both are reported**, and the verdict does not rest on the clause either way |

**And two places where a pre-registration's own expectation was reversed:** `PT-032` §3a‴
expected the two ≥ 72 h extended closures to be the sample's strongest evidence — they are two
of its **smallest** gaps (−7.10 and +0.40 pips), because they are Christmas and New Year. And
`PT-034` §6a predicted a verdict of `OVERSTATED` at a rate of 0.30–0.55; the run returned
`CONFIRMED AS TAUGHT` at **0.7046–0.7676**, which the record scores **WRONG, and badly**.

**Two tests disclose a defect in their own pre-registration**, which is recorded here because a
summary that hid it would be the `E20` class again: `PT-034` §6 (a near-tautological second
condition under hindsight) and `PT-042` (`N4` degenerate at `n = 0`; §5a underspecified `N1`'s
`O1` construction, in a direction that flatters the rule arm). Neither pre-registration was
edited — `COMMON_PROTOCOL.md` §9 rule 7 forbids it — and both defects are owed an amendment
before any re-issue.

---

## 5. WHAT NO SUMMARY HERE MAY BE READ AS SAYING

- **No win rate anywhere in this corpus validates the method** (`D-009`). Every claimed
  accuracy figure from the course is a **hypothesis under test**, never a target.
- **Nothing here is an entry rule.** The supported results are a prohibition, a risk rationale,
  a clock observation with an unidentified cause, and a timing observation. **The course's actual
  entry machinery has never been tested, because `D-030` blocks it** — five of the safety trade's
  seven conditions are undefined, and `PT-033`'s own mandatory scope statement says a Hi-Lo test
  *"can never be executed forward"* because the corpus does not teach real-time extreme
  identification.
- **Price levels on this corpus are not comparable with the V02–V06 FXCM homework**
  (`D-036a`). Only **shape and distance** claims travel.
- **The `D-035` HOLDOUT (2016-07-01 → 2017-12-29) has never been opened** and is not on
  disk; `D-044`'s 2017–2025 extension is likewise sealed. Every result above is a
  **DEVELOPMENT-block** result and carries whatever optimism that implies.
- **The undefined vocabulary is still undefined.** `A-001`, `A-002`, `A-004`, `A-006`,
  `A-010`, `A-011`, `A-012`, `C-001` and the rest are untouched by any test above;
  `D-030` blocked them and still does. `PT-040` now measures that one of them (`A-084`) is
  **`MATERIAL`** rather than cosmetic.
