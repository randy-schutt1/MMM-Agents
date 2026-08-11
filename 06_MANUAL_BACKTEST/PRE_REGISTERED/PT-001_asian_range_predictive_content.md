# PT-001 — Does the Asian range boundary carry predictive information?

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
BLOCKED BY: A-019 (session times have no timezone) — ONE blocker, see §3
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

## 3. THE ONE BLOCKER — `A-019`

V02 `[00:37:xx]` prints session times on a slide:

```text
Asian Session:  8:30pm - 3:00am    Gap 3-3:30a
```

**No timezone is stated anywhere on the slide or in the audio.** That is `A-019`.
Without it the window cannot be placed on a chart, and placing it by assumption would
violate `D-030`.

### Why this blocker may be cheaply resolvable — unlike the others

Unlike `A-011` or `A-039`, this probably does **not** require a future lesson. Existing
evidence in V01–V04 bears on it:

| Evidence | Video | Marker |
|---|---|---|
| *"It's 809 Eastern Time on 325"* | V04 | `[00:07:01]` |
| *"We know that the US session starts at 930 [New York] Eastern"* | V01 | `[00:46:09]` |
| London open printed 3:30am against 4:00 spoken — **caution: session times in this course are demonstrably messy** | — | `C-004` |

A focused evidence pass over V01–V05 for timezone statements could plausibly close
`A-019` — or establish that it cannot be closed, which is equally useful. **That pass is
the prerequisite work item, and it is small.**

Do **not** assume US Eastern to unblock this test. `C-004` exists precisely because a
plausible-looking session time in this course turned out to conflict with the source.

---

## 4. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | 15-minute, with 4-hour for context |
| Period | DEVELOPMENT block only, per `D-028` (oldest 70%). Exact dates pinned when the data source is declared |
| Holdout | **Not opened.** This test never touches the most recent 30% |
| Asian window | `PENDING A-019` — filled only from source evidence, never assumed |
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

1. Close `A-019` from source evidence, or establish that it cannot be closed.
2. Declare the chart data source, feed and timezone (`I-007`).
3. Pin the `D-028` 70/30 boundary dates from the actual available range.
4. Write `BT_PT001_NNNN.md` observations from the template, §0 referencing this file.
5. Run baselines **before** looking at the rule arm's aggregate result.
