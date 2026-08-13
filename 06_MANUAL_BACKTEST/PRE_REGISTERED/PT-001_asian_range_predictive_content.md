# PT-001 — Does the Asian range boundary carry predictive information?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
BLOCKER:    A-019 RESOLVED FOR TESTING PURPOSES 2026-08-11 via D-031 (two-arm design).
            A-019 itself remains OPEN — the source still declines to specify.
REMAINING:  I-007 (no declared chart data source / feed) and the D-028 boundary dates.
OWNER NOTE: recorded 2026-08-11 at the project owner's request so it is not forgotten
```

Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`
Decisions: `D-026` baseline · `D-027`/`D-028` period & holdout · `D-029` baseline
parameters · `D-030` no approximating untaught definitions

---

## 1. WHY THIS TEST IS WORTH RUNNING FIRST

Almost every claim in V01–V04 is blocked by a concept the course names but has not yet
defined — M/W anatomy (`A-011`), "the level" (`A-004`), "trap move" (`A-002`), TDI
(`A-039`). Under `D-030` those wait for the lesson that defines them.

**This one is different.** It requires no pattern recognition, no indicator, and no
judgement call. The Asian range is a measurement: the high and low of a fixed window.
The V04 homework already located it on four pairs.

And it tests the **load-bearing assumption underneath everything else.** The box
boundary is what V04's prohibition is about, what condition (a) measures from, and what
the "accumulation phase" framing in V03 rests on. If the boundary carries information,
the foundation has support before the elaborate parts arrive. If it carries none, that
is worth knowing at lesson 4 rather than after a Pine Script has been built on it.

> This test does **not** test Steve Mauro's rule. It tests a weaker, prior question that
> his rule presupposes. Any result must be reported as such — see §7.

---

## 2. THE QUESTION

> When price trades 25–50 pips beyond the Asian range, is subsequent price behaviour
> different from when it does not?

Null hypothesis: **it is not.** Excursions beyond the box are followed by the same
distribution of outcomes as matched entries with no regard to the box.

---

## 3. THE TIMEZONE — RESOLVED FOR TESTING BY `D-031`

V02's printed slide gives the window but **no timezone**:

```text
5pm            High / Low Reset (The MM Spread Is Set)
5pm – 8pm      Dead Gap
Asian Session  8:30pm – 3:00am     Gap 3:00–3:30
London Session 3:30am – 9:00am     Gap 9:00–9:30
New York       9:30am – 5pm
```

The instructor declines to specify — *"Listen, don't analyse it… These are the times"*
`[00:49:52]` — and the person who taught him has died `[00:49:22]`. `A-019` therefore
cannot close from source, and **is still open**.

Under `D-031` the ambiguity is **measured instead of guessed.**

### 3a. The two arms — both pre-registered, both always reported

| Arm | Chart timezone | Asian window in UTC |
|---|---|---|
| **A — fixed offset** | `UTC−5` year-round | 01:30 – 08:00 UTC, unchanging |
| **B — market-anchored** | `America/New_York` (DST-aware) | 00:30 – 07:00 UTC in summer; 01:30 – 08:00 in winter |

**Reporting rule (`D-031`, binding):** both arms are reported every time. Divergence is a
finding. **Reporting only the better arm is `E09` + `E24`.**

### 3b. Two draws are not two chances to be right

Running two arms means two samples. If A returns 58% and B returns 61%, that is **not**
a discovery that B is the correct timezone — it is one draw each from distributions that
may well overlap. Correct readings:

| Outcome | What it means |
|---|---|
| Arms behave alike | The timezone is **not load-bearing**. A robustness result, and good news |
| Arms diverge sharply | Real information — but needs a larger sample or independent confirmation before anyone concludes which reading is right |
| One arm looks better | **Not a conclusion.** Report both, state the overlap |

### 3c. Choose a test period that straddles a DST transition

The two arms are **identical outside US daylight saving** and differ by one hour inside
it. A period spanning a transition therefore yields a **within-sample** comparison on the
same instrument and the same regime, which is far stronger than two separate runs — and
it costs nothing but the choice of dates.

### 3d. Fact of record, from `D-031`

The bootcamp was recorded 2012-03-18 → 2012-06-17, **entirely within US daylight
saving**. Arm B reproduces the instructor's own stated times during that window; Arm A
displaces every one of them by an hour. This is evidence about the source. It does not
settle which reading the *method* requires, and it must not be reported as if it did.

---

## 4. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute, with 4-hour for context |
| Period | DEVELOPMENT block only, per `D-028` (oldest 70%). Exact dates pinned when the data source is declared |
| Holdout | **Not opened.** This test never touches the most recent 30% |
| Asian window | **8:30pm – 3:00am** per the V02 printed slide, run in **both `D-031` arms** (see §3a) |
| Box definition | High and low of the Asian window, per lesson |
| Trigger | 15m close ≥25 pips and ≤50 pips beyond the box edge |
| Decision point | That close. **No later bar is consulted for classification** |
| Direction | Away from the box, matching V04's geometry (breach high → short bias; breach low → long bias) |
| Stop / target | 18 pips / 50 pips — V04's stated maximum stop and stated target (`§2e`). **These are the instructor's numbers, not fitted** |
| Sample target | ≥30 decision points (`BACKTEST_EVIDENCE_STANDARD.md` §4.1) |

## 5. BASELINE — PER `D-029`

| Arm | Definition |
|---|---|
| **Primary** | Matched random entry: same session window, same stop/target, direction matched, entry bar randomized. 1,000 iterations, seed recorded |
| **Secondary** | Same, random direction — tests whether directional edge exists at all |
| **Third — the natural control** | Days where the box was **never** breached by 25–50 pips, sampled at the same clock times. This is the comparison that isolates the boundary itself |

The third arm is what makes this test worth running: it holds time, instrument and
payoff constant and varies **only** whether the box boundary was crossed.

## 6. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Rule arm indistinguishable from all baselines | The box boundary carries no detectable information at this sample. **A foundational finding — report prominently, do not bury** |
| Rule arm beats matched-random but not the never-breached arm | The edge is in the session/time window, not the box |
| Rule arm beats all three | The boundary carries information. Necessary support for the V04 prohibition — **not** proof of Mauro's full rule, which still needs (b) and (c) |
| n < 30 | `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`. No rate quoted anywhere |

## 7. MANDATORY SCOPE STATEMENT

Any report of this test carries this verbatim:

> PT-001 tests whether the Asian range boundary has predictive content. It is **not** a
> test of the Market Maker Method entry rule, which requires an M/W second leg
> (`A-011`) and TDI confirmation (`A-039`), neither of which is taught in V01–V04. A
> favourable result supports the *premise* of V04's prohibition. It does not validate
> the method.

## 8. TO RUN THIS

1. ~~Close `A-019`~~ — **done for testing purposes** via `D-031`'s two-arm design.
   `A-019` stays open on the course's side.
2. Declare the chart data source and feed (`I-007`). The timezone is no longer a
   blocker — it is a variable.
3. Pin the `D-028` 70/30 boundary dates from the actual available range, choosing a
   development window that **straddles a DST transition** (§3c).
4. Write `BT_PT001_NNNN.md` observations from the template, §0 referencing this file.
5. Run baselines **before** looking at the rule arm's aggregate result.
