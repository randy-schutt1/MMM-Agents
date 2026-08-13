# PT-020 — The London-open conditional: cut the high, sell; extend the low, stand aside

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V03 [00:39:49]–[00:40:10]
BLOCKERS:   I-007 · D-028 unpinned · C-004 (3:30 printed vs 4:00 spoken) — handled in §3a
            RESOLVED 2026-08-13 (D-034 / D-035 / D-036a), I-007/D-028 PAIR ONLY: I-007
            CLOSED, D-028 PINNED at 2016-07-01, W-B confirmed inside DEVELOPMENT. Data
            source is now the HistData GBP/USD M1 CSV corpus. Data-availability blocker
            CLEARED. C-004 remains OPEN, unaffected by this entry — see §3a.
INTERPRETIVE DEPENDENCY: V03_INTERPRETATION.md I8 / Q-of-scope — declared in §3b
ATTESTATION: No chart in W-B was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

`V03_SOURCE_NOTES.md` §2e calls it *"the one crisp conditional in the lesson"*:

> *"If the dealer cuts the high at the beginning of the London, **you sell**. If he extends
> the low at the beginning of the session, **forget it**. Why? The dealer extended the low.
> **I don't know if it's a straightaway or if it's a stop hunt. So I don't take it.**"*
> `[00:39:49]`–`[00:40:10]`

Three properties make it worth testing above almost anything else in V03:

1. **It is asymmetric**, and asymmetry is hard to produce by accident. A rule that says
   *trade this side, stand aside on that side* makes two different predictions, and a
   symmetric market refutes both at once.
2. **Its stated reason is epistemic, not mechanical** — *"I don't know which it is"*. That
   is a claim about **outcome variance**, not outcome direction: the low-side branch should
   show *higher dispersion*, not merely worse returns. Almost nothing else in the corpus
   makes a variance claim, and variance claims are cheap to test and hard to fudge.
3. It is a **session-open** rule, so it is the natural London-side companion to `PT-005`'s
   New-York-side test.

---

## 2. THE QUESTION

> After the first breach of the Asian range at the London open: does a **high-side** breach
> lead to downside continuation, and does a **low-side** breach produce outcomes so
> dispersed that standing aside is justified?

Null hypotheses, both pre-registered: **(a)** a high-side breach is followed by no
directional edge; **(b)** the two branches show the same dispersion.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Data source | ~~TradingView / FXCM, `D-034`~~ **AMENDED 2026-08-13, `D-036a`: HistData GBP/USD M1 CSV corpus**, aggregated locally to 15m. `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/`, SHA-256 on record. Data-QA gate (`scripts/qa_histdata_m1.py`) is a precondition on this run — cite `QA_REPORT.txt` |
| Timeframe | 15-minute |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | ~~PROVISIONAL DEVELOPMENT pending `D-028`~~ **PINNED 2026-08-13, `D-035`: boundary `2016-07-01`. W-B conforms — wholly inside DEVELOPMENT (`COMMON_PROTOCOL.md` §3a)** |
| Timezone | **Both `D-031` arms** |
| Referent range | The **Asian range** (8:30pm–3:00am) — the only range the course places before London on the V02 printed table |
| Trigger window | **03:30 – 04:30**, which spans both readings of the London open (§3a) |
| Branch H — *"cuts the high"* | First 15m close above the Asian range high inside the trigger window |
| Branch L — *"extends the low"* | First 15m close below the Asian range low inside the trigger window |
| Branch N | Neither — reported, because a rule's frequency of firing matters as much as its accuracy |
| Trade proxy, branch H | Short at that close; stop 18 pips; target 50 pips (V04 `[00:04:43]`, `[00:05:07]`) |
| Trade proxy, branch L | **The same short, taken anyway**, purely to measure what standing aside avoids. It is a measurement, not a recommendation, and the report says so |
| Primary measures | Per branch: hit rate, expectancy in pips, **and the standard deviation / interquartile range of the outcome** — measure (2) above is the variance claim and is reported first |
| Sub-window split | Results reported separately for triggers in **03:30–04:00** and **04:00–04:30** — the `C-004` split |
| Decision point | The triggering close. **No later bar informs branch assignment** |
| Sample | ~520 days across three branches. ≥ 30 per branch expected; reported per branch |

### 3a. `C-004` is open and this test does not close it

The V02 slide prints London open **3:30am**; the audio says *"3 to 3:30 is the gap, **4
o'clock session open**"* `[00:50:32]`. The trigger window covers both, and the sub-window
split reports them separately. If one half carries the effect and the other does not, that
is evidence recorded against `C-004` — **it does not resolve it**, because `C-004` is about
what the source says, and only the source can settle that.

### 3b. The interpretive dependency, declared

`V03_INTERPRETATION.md` `I8` reads this conditional **narrowly** — as scoped to a week
whose bias is already short — and records that the broad symmetric reading is defensible,
that the choice was the interpreter's, and that a reviewer disagreeing *"changes condition
table row 1's scope"*.

**This test uses the broad reading**, deliberately and with the disagreement on the record:
it applies the conditional to every day regardless of weekly bias. Reason: the narrow
reading requires knowing the week's bias at 03:30, which requires the anchor point
(`A-001`), which is undefined — so the narrow reading is **not testable today** and testing
the broad one is the only honest option available. **The result is therefore evidence about
the broad reading only, and is silent about the narrow one.** Any report that forgets this
converts an untestable rule into a tested one, which is the failure `D-030` names.

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry** in the same 03:30–04:30 window, direction matched per branch, same stop/target, 1,000 iterations, seed `20260812` |
| **Second — the natural control** | Branch N days — no breach at London open — entered short at 04:30. Isolates the breach from the hour |
| **Third** | Direction-symmetry control: the mirror rule (*long* after a low-side breach). If the mirror performs like branch H, the asymmetry is in the instructor's framing rather than in GBP/USD |

The third arm is the sharpest. The rule's whole claim is that the two sides are **not**
mirror images; running the mirror is the cheapest way to find out.

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Branch H beats N1; branch L shows visibly higher dispersion | **The conditional holds, asymmetry and all** — the strongest available V03 result, and the only variance-based confirmation the corpus could produce |
| Both branches beat N1 symmetrically | The stand-aside half is unnecessary on this instrument. Report it: a rule that forgoes half its opportunities without cause is expensive, and this is exactly the sort of thing a backtest is for |
| Neither branch beats N1 | The conditional has no support at this sample under the broad reading. Report prominently, with §3b's caveat attached in the same paragraph |
| The 03:30–04:00 and 04:00–04:30 halves disagree | Report both, record against `C-004`, resolve nothing |

## 6. MANDATORY SCOPE STATEMENT

> PT-020 tests a **broad reading** of one V03 conditional, using the Asian range as the
> referent for *"the high"* and *"the low"*. `A-006` (what "the box" is), `A-002` (trap
> move), `A-049`/`C-006` (stop hunt versus trap) and `A-001` (the anchor, on which the
> narrow reading depends) all remain **open**, and this test closes none of them. It is not
> a test of the Market Maker Method entry rule, which additionally requires an M/W second
> leg and TDI.

## 7. TO RUN THIS

1. ~~Close `I-007`; confirm W-B is DEVELOPMENT.~~ **Both resolved — `D-034` closed I-007,
   `D-035` pinned D-028 at 2016-07-01, W-B confirmed inside DEVELOPMENT
   (`COMMON_PROTOCOL.md` §3a). Run the data-QA gate
   (`06_MANUAL_BACKTEST/scripts/qa_histdata_m1.py`) as a precondition and cite
   `datasets/HISTDATA_GBPUSD_M1/QA_REPORT.txt`.**
2. ~~Harvest with timestamps from DOM text only;~~ **Source is the HistData GBP/USD M1
   CSV corpus (`D-036a`), aggregated locally to 15m by
   `06_MANUAL_BACKTEST/scripts/aggregate_m15.py` (`GBPUSD_M15_ARMA.csv` /
   `GBPUSD_M15_ARMB.csv` per `D-031` arm); every quote is a number parsed from the
   checksummed file, per `COMMON_PROTOCOL.md` §2's restated `E06` — no value is read
   from a chart rendering.** Build the Asian box per day, both arms.
3. Run the mirror control and N1 **before** looking at branch H's result.
4. Report branch frequencies (H / L / N) with the outcome table — a rule that fires on 8%
   of days is a different object from one that fires on 60%.
5. Write `BT_V03_NNNN.md` from the template, §0 referencing this file.
