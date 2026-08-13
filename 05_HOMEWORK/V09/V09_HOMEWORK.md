# V09 — HOMEWORK

**Lesson:** V09 · `Bootcamp1 Wk2 032612 Part4 (53mins).swf`
**SHA-256:** `b0f36b5540de7a76397c80202cf6a721a2a18aa9011c5698238c6bcc624168d4`
**Speaker:** 100% `GUEST` — under `D-033` normative at equal weight; the tag is provenance

---

## 0. WHAT V09 ASSIGNS, AND WHAT WAS DONE WITH EACH

| # | Assignment | Marker | Disposition |
|---|---|---|---|
| **H1** | *"Type in a lot size calculator… tons of free ones. I suggest you go get one"* | `[00:02:56]`–`[00:03:16]` | ✅ **DONE — §1** |
| **H2** | *"Go back, study it, do what you can, take notes heavily, because this is everything"* | `[00:23:37]`–`[00:23:47]` | ✅ **DONE** — `V09_SOURCE_NOTES.md` §2–§6, and §2 below is the graded version of it |
| **H3** | **The USD/JPY arrow drill** — commit a directional arrow each day from the level count, score it the next day, alone | `[00:47:57]`–`[00:49:01]` | ⏸ **DEFERRED** (`D-019`), blocked by `A-004`. See §4 |
| **H4** | *"Slap some arrows on there and see what it does the next day"* — H3 generalized | `[00:51:31]`–`[00:51:43]` | ⏸ **DEFERRED**, same blocker |
| **H5** | Steve's week-1 assignment, referred to but **not reissued**: *"our homework from last week that Steve gave us was to mark up this chart"* | `[00:37:43]`–`[00:38:00]` | ▫ **NOT V09's assignment** — recorded as a pointer only |

**Plus, beyond what was assigned:** §3 executes V09's own sizing algorithm on real trade
sequences, under predictions committed in advance. It is not homework the lesson set; it is the
comprehension demonstration that H3 would have been if H3 were performable.

---

## 1. H1 — THE LOT-SIZE CALCULATOR, AND AN INDEPENDENT CROSS-CHECK

**Script:** `scripts/verify_v09_arithmetic.py` · **Output:** `data/h1_calculator_output.txt`

Downloading somebody's web calculator would demonstrate nothing and would be unauditable.
Instead the formula was **built from V09's own words** —

```text
risk_dollars = balance × 0.02          [00:01:53]–[00:02:03], printed frame 3
usd_per_pip  = risk_dollars ÷ stop_pips
lots         = usd_per_pip ÷ 10        (USD-quoted pair)
```

— and checked against **two sources that do not cite each other**.

### Cross-check A — V09's own worked example (Tier 1)

**7 / 7 reconcile exactly**: `$250`, `$10/pip`, `1 lot`, `10 minis`, `$9.20/pip`, `0.92 lots`,
`9.2 minis`.

### Cross-check B — `MMM-NOTES` p.67, the `RISK LEVEL` table (Tier 2, `D-039`)

**9 / 9 reconcile.** The notes print a 3 × 3 table of lots per $100,000 at 1% / 3% / 5% risk and
10 / 15 / 20-pip stops, and **never state the formula in words**. V09 states the formula and
never prints that table.

| | 1% | 3% | 5% |
|---|---|---|---|
| **10 pip** | 10 / **10.0000** | 30 / **30.0000** | 50 / **50.0000** |
| **15 pip** | 6.7 / **6.6667** | 20 / **20.0000** | 33 / **33.3333** |
| **20 pip** | 5 / **5.0000** | 15 / **15.0000** | 25 / **25.0000** |

<sub>printed / computed. Two cells carry source rounding: `6.7` from 6.6667 (1 dp) and `33` from
33.3333 (rounded **down**). Both are named in the script's output rather than hidden, and the
0.34-lot tolerance is stated rather than tuned.</sub>

> ### THIS IS THE INDEPENDENT CROSS-CHECK, AND IT IS GENUINELY INDEPENDENT
>
> `SOURCING_HIERARCHY.md` §1.3 warns that **Tier 3 agreeing with Tier 2 is one document quoted
> twice**, because the web material is probably copied from the PDF. **That trap does not apply
> here**: this is **Tier 1 against Tier 2** — a 2012 recording against an anonymous seminar
> account, neither derived from the other, reaching the same arithmetic from opposite directions
> (one gives the rule and no table, the other gives the table and no rule).
>
> **This is `C-015`'s corroboration half, verified in code.** It says **nothing** about the
> sizing *policy*, on which the same two sources contradict each other — see `C-015`.

### The cumulative constraint, exercised

`[00:19:29]` makes the 2% **account-wide**, not per trade. Materially:

| Simultaneous positions | $/pip **each** on a $12,500 account, 25-pip stop | Total risk |
|---|---|---|
| 1 | $10.00 | 2.00% |
| 2 | $5.00 | 2.00% |
| 3 | $3.33 | 2.00% |
| 4 | $2.50 | 2.00% |

**A session that codes 2% per trade and opens three pairs has taken 6% risk**, which is triple
what the lesson permits and is its printed error #2.

---

## 2. COMPREHENSION PROBE — ANSWERS COMMITTED BEFORE THE SCORER EXISTED

**Answers + reasoning:** `data/v09_comprehension_ANSWERS.json`, committed at **`97d2c1b`**
**Scorer:** `scripts/comprehension_probe.py`, written afterwards
**Output:** `data/comprehension_probe_output.txt`

Ten questions. Each answer carries a **reasoning trace** written before scoring, so a reviewer
can see *why* an answer was given and not merely whether it was right (`REVIEW_PROTOCOL.md`
dimension L, applied to myself). The scorer checks mechanically against the transcript body or by
re-deriving the arithmetic independently. **No answer was revised after scoring, and the rule
saying so is in the answers file.**

**SCORE: 9 right, 0 wrong, 1 manual (9/9 of auto-scored).**

| Q | Subject | Result |
|---|---|---|
| Q1 | Lot size on the second consecutive loss | ✅ same size |
| Q2 | Balance and % after four 2% losses | ✅ $11,500, **8.0%** — and the reasoning names the trap (`1 − 0.98⁴ = 7.76%` is the wrong model because size is held constant) |
| Q3 | Is 2% per-trade or account-wide? | ✅ **account-wide** |
| Q4 | The two geometries and what gates the better one | ✅ 25/50 and 15/50, gated on **HOD/LOD skill** — and the answer flags that the "3:1" is arithmetically 3.33:1 |
| Q5 | Real break-even vs the ">50%" claim | ✅ **33.33%**; the claim is true and far above threshold |
| Q6 | V08's innermost ring | ✅ **discipline in keeping to the risk plan** |
| Q7 | Does V09 state stop *placement*? | ✅ **no** — verified by five absence checks against the transcript |
| Q8 | Whose practice is "the grape"? | ✅ the presenter's own; the **blueberry** is course furniture |
| Q9 | Is the 20%/week projection arithmetically wrong? | ✅ **no, it is exact** — what is omitted is the losses |
| Q10 | Can H3 be performed today? | ▫ **MANUAL** — disposition `DEFERRED`, blocker `A-004` |

> **A 9/9 is not self-congratulation and should not be read as one.** Seven of the ten are
> questions about a lesson whose material half is **printed on slides in plain English**, which is
> the easiest comprehension target in the corpus so far. The probe's value is in **Q2, Q5, Q7 and
> Q9**, each of which has an attractive wrong answer that a careless reading produces — 7.76%
> instead of 8%, ">50% is the threshold" instead of 33.3%, assembling a stop-placement rule that
> neither lesson states, and calling the projection an arithmetic error when every digit closes.
> **Those four are where a reviewer should look, and the reasoning traces are what should be
> audited, not the score.**

---

## 3. THE EQUITY-PATH SIMULATION — V09's OWN RULE, EXECUTED LITERALLY

**Script:** `scripts/run_equity_path.py` · **Output:** `data/equity_path_output.txt`
**Predictions `P-E1`…`P-E4`:** committed at **`97d2c1b`**, before the script was written.

**This is not a test of an entry rule.** V09 states none and none was invented (`D-030`). It is
the execution of a **fully specified algorithm** — the one printed on frame 10 — applied to the
same trade sequences `PT-035` generated, regenerated by the same committed code and seed.

| Cell | Trigger fired | Median max drawdown | > 8% | Median terminal (from $12,500) | Below start | Wipeouts |
|---|---|---|---|---|---|---|
| `A25` (−25/+50, arm A) | **100%** (median 21×) | **62.8%** | **100%** | $5,930 | 97.5% | **0 / 1000** |
| `B25` (−25/+50, arm B) | **100%** (median 21×) | **61.9%** | **100%** | $6,004 | 95.2% | **0 / 1000** |
| `A15` (−15/+50, arm A) | **100%** (median 31×) | **76.2%** | **100%** | $3,634 | 99.4% | **0 / 1000** |
| `B15` (−15/+50, arm B) | **100%** (median 31×) | **74.4%** | **100%** | $3,957 | 98.9% | **0 / 1000** |

**All four predictions RIGHT.**

### The finding, stated precisely, because it is easy to overstate

> **THE `8%` FIGURE IS NOT A DRAWDOWN CAP, AND IT IS VERY READABLE AS ONE.**
>
> V09's 8% is exactly what four consecutive losses cost, and the lesson uses it as the trigger for
> resizing. **It is not a bound on how far the account falls.** After recalculating, the rule
> permits a fifth, sixth and seventh loss, each costing 2% of a now-smaller balance — so drawdown
> compounds well past 8% while the plan behaves exactly as written. **Measured median peak-to-
> trough: 62–76%, and above 8% in 4,000 of 4,000 sequences.**
>
> Nothing in V09 says 8% is a cap. Nothing in V09 says it is not, either, and a student who reads
> the recovery example — *"we've had four losses and in two wins we came back"* — as a picture of
> the worst case will be badly wrong about the shape of a losing stretch.

> ### ⚠ WHAT THIS DOES **NOT** SHOW, AND THE DISTINCTION IS THE WHOLE POINT
>
> **It does not show that V09's sizing rule loses money.** The trade streams are **matched-random
> entries at a hit rate below break-even** (0.28 against 0.333; 0.17 against 0.231) — and
> `PT-035` §3 established that even those figures are biased **low** by resolution censoring.
> **Any sizing rule loses on a negative edge.** That is arithmetic, not a defect in the rule.
>
> What the simulation demonstrates is narrower and more useful:
>
> 1. **Sizing discipline cannot rescue a negative edge**, and V09 never claims it can — it is
>    explicit that the method must supply the edge (*"you've been given the method that will
>    work… we are now trying to give you the tools of the math"*, `[00:04:27]`–`[00:04:29]`).
> 2. **The 4-loss trigger is not an exception path. It is the normal operating mode** at these hit
>    rates — a median of 21–31 firings per 200 trades. A rule described as the response to an
>    unusual event fires roughly every 7–9 trades.
> 3. **The one protection the rule genuinely delivers, it delivers completely**: fixed-fractional
>    sizing cannot reach zero, and **0 of 4,000 sequences wiped out** despite median drawdowns
>    above 60%. `P-E4` predicted exactly this. **It is the strongest thing this simulation says in
>    the rule's favour and it is stated as prominently as the criticisms.**

---

## 4. H3 / H4 — DEFERRED, AND WHY THAT IS NOT AN EXCUSE

**H3 is the best-designed exercise anywhere in V01–V09**, and this is worth saying plainly because
the disposition below reads like a dodge and is not one:

> `[00:47:57]`–`[00:49:01]` — take a pair **the paid service does not cover** (so no answer can
> leak), form a level read, **commit an arrow at the end of every day**, and check it the next
> day. `[00:48:41]` — *"I wouldn't even talk about it with anybody. I'd frankly do this on your
> own."*

**That is a pre-registration discipline**, invented by a 2012 trading coach, and it is
structurally the same thing `D-026`/`D-027` impose on this project.

### It cannot be performed, and the blocker is definitional

**H3's predictor is the level count.** *Level*, as a countable unit, is **`A-004`** — open since
V02, used at **50 markers** in V09 alone, and still undefined at the end of the ninth lesson.

Performing H3 would require this session to **invent a level-counting rule**. That is `D-030`
exactly: *"no session may substitute an approximation, a plausible reading, a definition from
another trading framework, or a 'reasonable' numeric stand-in in order to make a blocked test
runnable."* And it is worse here than usual, because an arrow drill **produces a score** — and a
score in a research corpus acquires an authority a note never does.

### The disposition is `DEFERRED`, not `NOT APPLICABLE` — `D-019`

| Test | H3 |
|---|---|
| Is there subject matter? | **Yes** — a concrete, repeatable daily exercise |
| Is it performable in principle? | **Yes**, the moment *level* is defined |
| Is it blocked by a missing prerequisite? | **Yes** — `A-004` |

**`D-019`: work that is merely blocked is `DEFERRED`, never `NOT APPLICABLE`.** It stays open,
is carried in `REVIEW_INDEX.md`, and **is performed in the lesson that defines a level.**

### What was NOT done, and this is the part that matters

**No substitute predictor was invented.** An earlier draft of `V09_SOURCE_NOTES.md` §11 proposed
running "H3's structure with one of V09's own explicit numbers as the predictor"; **that was
dropped**, because V09's explicit numbers are risk parameters, not directional signals, and
dressing one up as an arrow predictor would have been the `D-030` substitution wearing a
disclosure. §3 above is what replaced it: the **same commit-before-you-look discipline**, applied
to something V09 actually specifies in full.

---

## 5. DATA, PROVENANCE, GATES

| Field | Value |
|---|---|
| Market data | HistData GBP/USD M1 (`D-036a`), SHA-256 on record, aggregated by the committed `aggregate_m15.py`, re-derived and diffed by the runner — MATCH both arms |
| Window | `W-C′` `2013-01-06` → `2016-06-30`, `D-035` DEVELOPMENT. **Holdout not opened** |
| QA gate | `GATE: PASS` asserted before any bar was read |
| `C8` | `2014-06-01`, `2014-06-02` excluded **by name**; nine Dec/Jan closures included — as `PT-035` §7a pre-registered |
| `D-031` | Both arms run and both reported in every table above |
| Levels vs prior homework | Price **levels** are not comparable with V02–V06's TradingView/FXCM harvests (`D-036a`). Nothing here makes a level claim |
| `D-009` | No figure here is a target; no parameter was tuned toward one |

## 6. REPRODUCTION

```bash
python3 05_HOMEWORK/V09/scripts/verify_v09_arithmetic.py
python3 05_HOMEWORK/V09/scripts/comprehension_probe.py
python3 05_HOMEWORK/V09/scripts/run_equity_path.py
```

Deterministic under seed 20260812.
