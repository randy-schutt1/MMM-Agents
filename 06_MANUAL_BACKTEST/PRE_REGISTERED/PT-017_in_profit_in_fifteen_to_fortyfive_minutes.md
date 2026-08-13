# PT-017 — "In profit in 15 to 45 minutes. Guaranteed."

```text
STATUS:     PRE-REGISTERED — NOT YET RUN
LESSON:     V04 [00:08:56]–[00:09:04]  (CL1 — the strongest unevidenced claim in the course)
BLOCKERS:   I-007 · D-028 unpinned · A-007 blocks the instructor's actual entry — see §6
GOVERNING:  D-009 — this is a HYPOTHESIS TO TEST, never a target. Nothing is tuned toward it.
ATTESTATION: No chart in W-B was opened by the session that wrote this file.
```

Shared machinery: `COMMON_PROTOCOL.md`. Standard: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md`.

---

## 1. WHY THIS TEST IS WORTH RUNNING

> *"When you learn to grab these on the second leg close, **you're going to be in profit in
> 15 to 45 minutes. Guaranteed.**"* `[00:08:56]`–`[00:09:04]`

`V04_SOURCE_NOTES.md` §10 records this as `CL1` and calls it *"the strongest unevidenced
claim in the course so far"*. `BACKTEST_EVIDENCE_STANDARD.md` §2 cites it as one of the two
reasons a bare hit rate is unreadable here. It is the claim most likely to be repeated,
most likely to be believed, and least likely to have been checked.

It is also unusually shaped: it is a claim about **time-to-favourable-excursion**, not about
win rate. That is measurable directly, it needs no exit rule, and it produces a distribution
rather than a percentage — which is exactly what `D-009` wants, since a distribution cannot
be optimised toward.

**What blocks a faithful test, stated first:** the entry is *"the second leg close"*, and
"second leg" is `A-007`, undefined across V01–V06 and defined in V02 only by pointing at a
screen. Under `D-030` this test may not invent one. So it does what `PT-001` does — tests
the **prior** question the claim presupposes, with the substitution declared.

---

## 2. THE QUESTION

> After the location trigger the instructor names — a close 25–50 pips beyond the Asian
> range — how long does GBP/USD take to put an away-direction position into profit, and
> what share are in profit inside 15–45 minutes?

Null hypothesis: **time-to-profit after the trigger is no different** from time-to-profit
after a matched random entry in the same hours.

## 3. PRE-REGISTRATION — FIXED BEFORE ANY CHART IS OPENED

| Field | Value |
|---|---|
| Instrument | GBP/USD (`D-007`) |
| Timeframe | **5-minute preferred, 15-minute fallback.** A claim about 15 minutes cannot be resolved on 15-minute bars; the resolution actually used is recorded in the observation |
| Window | **W-B** — 2014-01-05 → 2015-12-31 |
| Block | PROVISIONAL DEVELOPMENT pending `D-028` |
| Timezone | **Both `D-031` arms** |
| Trigger | First close **25–50 pips** beyond the Asian range edge (V04 `[00:15:43]`) — identical to `PT-001`, so results compose |
| Direction | Away from the box (breach high → short; breach low → long) |
| Entry price | That bar's close. **No slippage or spread model is invented**; the raw figure is reported, and the fact that spread would worsen it is stated in the report |
| Measure 1 | Time until unrealised P&L first exceeds **0 pips** |
| Measure 2 | Time until it first exceeds **+10 pips** — a "meaningfully in profit" reading, pre-registered so it cannot be chosen afterwards |
| Measure 3 | **Share in profit at 15 min, 30 min, 45 min, 60 min, 120 min**, all five reported |
| Measure 4 | Maximum adverse excursion **before** first profit — the number that decides whether an 18-pip stop (V04 `[00:04:43]`) survives long enough to collect it |
| Sample | Whatever the trigger yields in W-B; `PT-014` predicts the count in advance. ≥ 30 required for any rate |

Measure 4 is the one that turns this from trivia into something usable. *"In profit within
45 minutes"* is worth nothing if the position was 25 pips underwater at minute 20 with an
18-pip stop in place. **The two must be reported in the same table.**

## 4. BASELINE

| Arm | Null |
|---|---|
| **Primary** | **N1 — matched random entry**: same window, same session hours, direction matched, entry bar randomised. 1,000 iterations, seed `20260812`. Reports the same five checkpoints |
| **Second — the natural control** | The same measures on days where **no** qualifying excursion occurred, entered at the same clock times. Isolates the trigger from the hour |
| **Third** | Random-direction arm, per `D-029`: answers whether *any* directional edge exists at these hours before asking whether this one does |

## 5. WHAT EACH OUTCOME MEANS

| Result | Reading |
|---|---|
| Trigger entries reach profit materially faster than N1 | Support for the *timing* half of `CL1`, on a **proxy entry**. The word *"Guaranteed"* is refuted by construction — any share below 100% refutes it — and that must be said explicitly in the report |
| No difference | `CL1`'s timing has no support at this sample even before the second-leg refinement. Report prominently (`E25`) |
| Fast to +0 but MAE routinely exceeds 18 pips | The most useful likely outcome: the claim is *true and untradeable at the stated stop*. Report both numbers together, always |
| Arms diverge | Report both; the trigger's clock moves with the box |

**Under `D-009` no parameter here may be adjusted to bring the result closer to 15–45
minutes.** If the observed median is 4 hours, the observed median is 4 hours.

## 6. MANDATORY SCOPE STATEMENT

> PT-017 measures time-to-profit after a **location trigger**, not after the instructor's
> entry. His entry is the **close of a second leg** of an M/W formation (`A-007`, `A-011`),
> confirmed by TDI (`A-039`) — none of which is defined in V01–V06. **This test therefore
> cannot confirm or refute `CL1` as stated**; it establishes what the location alone
> delivers, which is the necessary lower bound on any later test of the full rule. Under
> `D-009` the 15–45 minute figure is a hypothesis with provenance, never a target, and no
> `100%` result would make *"Guaranteed"* a supportable word.

## 7. TO RUN THIS

1. Close `I-007`; confirm W-B is DEVELOPMENT; establish whether 5-minute history covers the
   window and **record the answer before harvesting**.
2. Run `PT-014` first for the expected trigger count.
3. Harvest with timestamps from DOM text only.
4. Run all three baselines before looking at the trigger population's checkpoints.
5. Write `BT_V04_NNNN.md` from the template, §0 referencing this file.
