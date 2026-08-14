# V16 — HOMEWORK

**Assignment, as printed** (`V16_00-35-05_r-and-d-homework-six-majors-slide.png`):

> **`R&D`**
> *"Find the Expected High/Low for the day on the 6 majors, using Pivot calculations."*
> *"Do it pre London for Mon & Tues"*

**Assignment, as spoken** `[00:35:03]`–`[00:35:36]`:

> *"Find the expected high and low for the day on six majors using pivot calculations. Do it free
> \[pre\] London from Monday and Tuesday. So tomorrow night, Monday night and Tuesday night, go to
> mypivotcalculator.com, take the daily candle, take the open high, low close, calculate the values,
> post them in the forum for me to see."*

⭐ **This is the most completely-specified homework in the corpus** — instruments enumerated
(`[00:40:52]`–`[00:41:02]`), input named (daily OHLC), tool named, schedule named, output named.
**And it still cannot be completed.** §3 is where it stops, and §3 is the point of this file.

---

## §0 — SCOPE LIMITS, DECLARED BEFORE ANY NUMBER

1. **One instrument, not six.** This project holds **GBP/USD only** (`D-036a`, `D-044`). GBP/USD
   is one of the six he lists. The other five are not available and **are not simulated,
   estimated or filled in.**
2. **2015, not 2012.** The corpus starts 2013-01-06. The assignment is from 2012-05-06.
3. **`mypivotcalculator.com` was NOT used.** It is a 2012 third-party site; sending this project's
   data to it would be pointless and the arithmetic is four lines. **The standard floor-trader
   formulae are used and printed in §2 so the reader can check them.**
4. **The first attempt is preserved even where it was wrong** (`STUDENT_SESSION_PROMPT.md`). See
   §3a and §5.

**Dates chosen:** a **Monday and Tuesday**, as assigned — **2015-06-01** and **2015-06-02** —
picked from the `D-035` DEVELOPMENT window before any pivot was computed, on the sole criterion
that both are complete trading days inside it.

---

## §1 — H1: THE ARITHMETIC, WHICH IS NOT IN DISPUTE

Standard floor-trader pivots, the formulae the lesson's own tool implements:

```text
CPP = (H + L + C) / 3
R1  = 2·CPP − L        S1 = 2·CPP − H
R2  = CPP + (H − L)    S2 = CPP − (H − L)
```

Data: HistData GBP/USD M1, `D-035` DEVELOPMENT, arm A, read from the checksummed corpus. **The
file clock is a fixed UTC−5, i.e. New York STANDARD time**, so *"midnight"* below is EST midnight.
That choice is forced and it is one horn of `A-106` (§4).

---

## §2 — H1 RESULTS

### Target day **Monday 2015-06-01**

**Prior candle read two ways, because the lesson does not say which** (§4):

| Prior candle | O | H | L | C | Colour | R2 | R1 | **CPP** | S1 | S2 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Sun 2015-05-31**, 00:00→24:00 (418 M1 bars — a **stub session**) | 1.52923 | 1.52981 | 1.52588 | 1.52892 | **RED** | 1.53213 | 1.53053 | **1.52820** | 1.52660 | 1.52427 |
| **Fri 2015-05-29**, 00:00→24:00 (1,020 bars) | 1.53329 | 1.53412 | 1.52364 | 1.52898 | **RED** | 1.53939 | 1.53419 | **1.52891** | 1.52371 | 1.51843 |
| **Fri 2015-05-29**, 17:00→17:00 (project `C-1`, 1,439 bars) | 1.53142 | 1.53420 | 1.52364 | 1.52898 | **RED** | 1.53950 | 1.53424 | **1.52894** | 1.52368 | 1.51838 |

**Actual outcome, Monday 2015-06-01:** H **1.53044**, L **1.51705**, range **133.9 pips**
(identical under both day conventions).

### Target day **Tuesday 2015-06-02**

| Prior candle | O | H | L | C | Colour | R2 | R1 | **CPP** | S1 | S2 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Mon 2015-06-01**, 00:00→24:00 (1,439 bars) | 1.52892 | 1.53044 | 1.51705 | 1.52046 | **RED** | 1.53604 | 1.52825 | **1.52265** | 1.51486 | 1.50926 |
| **Mon 2015-06-01**, 17:00→17:00 (1,438 bars) | 1.52923 | 1.53044 | 1.51705 | 1.51990 | **RED** | 1.53585 | 1.52788 | **1.52246** | 1.51449 | 1.50907 |

**Actual outcome, Tuesday 2015-06-02:** H **1.53671**, L **1.51794**, range **187.7 pips**.

**Both prior candles are RED**, so under the lesson's printed rule
(`V16_00-00-50_pivot-points-four-bullets-slide.png`) both days are **`M1/M3` days**.

---

## §3 — ⛔ AND HERE THE ASSIGNMENT STOPS

The task is *"find the **expected high/low**"*. Under the lesson's own rules
(`V16_SOURCE_NOTES.md` §2, §3) the expected high of an `M1/M3` day is **`M3`** and the expected low
is **`M1`**.

**`M3` and `M1` cannot be computed.** `A-101`: V16 **prints their ORDER** — `R2 · M4 · R1 · M3 ·
CPP · M2 · S1 · M1 · S2` — and **never states their construction**, and the diagram that appears
to encode it is drawn with **all nine levels equally spaced to within one pixel**, which is what a
schematic looks like regardless of the underlying arithmetic (`V16_INTERPRETATION.md` §3).

⛔ **So the homework is completable to the CPP/R1/R2/S1/S2 grid and no further.** The five values
above are correct floor-trader pivots. **The two numbers the assignment actually asks for are the
two the corpus cannot produce.**

### §3a — ⚠ WHAT I DID FIRST, AND IT WAS WRONG

**My first attempt computed `M3` as the midpoint of `CPP` and `R1`, and `M1` as the midpoint of
`S2` and `S1`, and produced a tidy answer.** It is preserved here because it is the exact error
this file exists to demonstrate:

> *Monday 2015-06-01, Friday basis: `M3` = (1.52891 + 1.53419)/2 = **1.53155**;
> `M1` = (1.51843 + 1.52371)/2 = **1.52107**. Expected range **104.8 pips**.*

**Those numbers are not wrong arithmetic. They are arithmetic on a definition nobody gave**, and
`D-030` forbids exactly that. **They are struck.** They are shown so a reviewer can see how
plausible the fabrication looks — it produces a sane-looking expected range on a real pair, and
nothing downstream would have flagged it.

---

## §4 — ⭐ H2: THE ASSIGNMENT'S OWN AMBIGUITIES, MEASURED IN PIPS

**Doing the homework surfaced two undefined choices the lesson never addresses. Both are measured
rather than argued.**

### §4a — ⚠ THE MONDAY PROBLEM, AND IT IS LARGE

*"Yesterday's price action gives you tomorrow's pivot points"* — **for a Monday, what is
yesterday?** FX Sunday is a partial session (here, **418 M1 bars against a full day's 1,440**).
The lesson **assigns Monday explicitly** and **never says.**

**Sunday-stub basis minus Friday basis, same target day, in pips:**

| Level | Difference |
|---|---|
| `CPP` | **−7.1** |
| `R1` | **−36.6** |
| `S1` | **+28.9** |
| **`R2`** | **−72.6** |
| **`S2`** | **+58.4** |

⭐ **A 72.6-pip disagreement on `R2`, on a day whose entire realised range was 133.9 pips.** The
two readings of *"yesterday"* do not differ at the margin; **they produce different grids.**
Filed as **`A-106`**.

⚠ **AND ONE DAY'S COINCIDENCE, REPORTED WITH ITS OWN WARNING ATTACHED.** Monday's actual high
**1.53044** sits **0.9 pips** below the Sunday-stub `R1` of **1.53053**, and **37.5 pips** below the
Friday-basis `R1`. **This is `n = 1`. It is not evidence for the Sunday reading and it is not
offered as any.** It is here because it is precisely the kind of single striking coincidence that
selects a convention by accident, and naming it is cheaper than being fooled by it later. **The
same Sunday grid missed the day's low by 72.2 pips (below its own `S2`).**

### §4b — `C-023` QUANTIFIED, AND THE RESULT WEAKENS MY OWN CONTRADICTION RECORD

`C-023` records that `[00:40:22]`–`[00:40:34]` says pivots are computed *"from midnight to
midnight"* while `[00:41:09]`–`[00:41:18]`, forty seconds later, says *"just do it on the daily
candle."* **Measured on these two days, the fork costs:**

| Target day | `CPP` | `R1` | `S1` | `R2` | `S2` |
|---|---|---|---|---|---|
| Mon 2015-06-01 (Friday basis) | −0.3 | −0.5 | +0.3 | −1.1 | +0.5 |
| Tue 2015-06-02 | +1.9 | +3.7 | +3.7 | +1.9 | +1.9 |

**Under 4 pips on every level, on both days.** ⚠ **That is a finding against `C-023`'s practical
importance and it is recorded in `C-023` itself.** The contradiction is real — the speaker does
give two different instructions — but on this instrument, in this window, **the two instructions
produce nearly the same grid**, and `A-106`'s Monday fork is an order of magnitude larger. **A
reviewer weighing which of the two to escalate should escalate `A-106`.**

⚠ **`n = 2` days, one pair.** This is an illustration, not a measurement of the general case, and
it is not a pre-registered test.

---

## §5 — H3: THE DESCRIPTIVE OUTCOME, WHICH IS **NOT** A TEST

**Reported because the numbers exist, and flagged hard because two days is nothing.**

| Day | Basis | Actual H vs `R1` | Actual L vs `S1` | `R1 − S1` span | Actual range |
|---|---|---|---|---|---|
| Mon 06-01 | Friday | **−37.5** pips (short) | **−66.6** pips (**through `S1` and through `S2`**) | 104.8 | **133.9** |
| Tue 06-02 | Monday | **+84.6** pips (**above `R1`, and +6.7 above `R2`**) | **+30.8** pips (held) | 133.9 | **187.7** |

**On both days the realised range exceeded the `R1`–`S1` span, and on both days one extreme broke
clean through the outer pivot on its side.** ⛔ **`n = 2`. No verdict, no record, no claim. This is
not `PT-044` and it is not pre-registered.** It is recorded so that a later session designing a
real test of the projection rule — which will need `A-101` closed first — knows the descriptive
shape it is up against.

---

## §6 — H4: COMPREHENSION PROBE — **22/22**, AND THE SCORE IS WEAK EVIDENCE

Twenty-two machine-checked claims: **14 recall claims** asserted to be IN the lesson and **8
falsehoods** asserted to be ABSENT. **Answers were committed before the checker was run**, and the
checker greps the committed transcript.

**Result: recall 14/14, absence 8/8.**

The eight absence claims are the fabrication set from `Q-017`: `stop loss`, `Asian box`, `shark`,
`shark fin`, `railroad`, `peak formation`, `evening star`, `5/13` — **every one of which the
quarantined `RULES.md`/`NOTES.md` attributes to this lesson, and every one of which occurs ZERO
times in it.**

⚠ **WHY 22/22 IS WORTH LESS THAN V06's 46/48.** V06's probe was written against a lesson its
author had read once; **this one was written after reading V16's transcript closely three times and
after writing four artifacts about it.** A clean score under those conditions measures short-term
memory, not comprehension. **The probe's real value is the eight absence rows, which are a direct
mechanical check on `Q-017` rather than a check on me.**

---

## §7 — WHAT THE HOMEWORK PRODUCED, IN ONE LINE

**The best-specified assignment in the corpus is completable to five of its seven numbers, and the
two it cannot reach are the two it asks for.** That is `A-101` stated as a consequence rather than
as a record, and it is the single most useful thing V16's homework could have shown.
