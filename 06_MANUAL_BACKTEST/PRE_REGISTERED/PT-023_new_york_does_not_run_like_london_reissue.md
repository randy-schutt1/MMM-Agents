# PT-023 — "They don't usually run like London" (RE-ISSUE of PT-022 on an obtainable period)

```text
STATUS:      PRE-REGISTERED — NOT YET RUN
WRITTEN:     2026-08-13
RE-ISSUES:   PT-022, which is SUPERSEDED — PERIOD UNOBTAINABLE, retained unedited.
ATTESTATION: At the moment of writing, this session had read from the pre-2026-07-30
             period NOTHING BUT DATES. The feed-depth probe (probe_back.mjs) walked the
             chart back 368 drags and printed only the left-edge DATE at each step; no
             open, high, low or close from any bar before 2026-07-30 has been loaded,
             printed, stored or inspected. The period rule, the windows, the outcomes,
             the nulls, the seed and the decision rules below are carried over UNCHANGED
             from PT-022 except where §1 marks a substitution, and every substitution is
             a consequence of availability, not of anything seen in the data.
SCOPE:       GUEST claim. Tested under D-032, excluded from doctrine under D-025.
```

**PT-022 governs everything not restated here.** Its §0 (why this test exists under `D-025`),
§1 (why this claim and no other survives `D-030`), §2 (the question and the null), §2a (the
mechanical bias that runs *against* the claim), §3 (the operationalisation and its weakness),
§4a/§4b (outcomes), §5 (nulls), §6 (decision rules), §7 (what each outcome means) and §8 (the
mandatory scope statement) are **carried over verbatim and are not repeated**. This file states
only what changed and what it costs.

---

## 1. WHAT CHANGED, AND WHAT EACH SUBSTITUTION COSTS

| Field | PT-022 | PT-023 | Cost, stated now |
|---|---|---|---|
| **Period** | W-A, `2015-01-04 → 2015-12-31` (~260 weekdays) | **The `D-028` DEVELOPMENT block of the declared feed's 15-minute GBP/USD series**, computed by the rule in §2 | Three real losses, §3 |
| **Everything else** | — | **unchanged** | — |

**Why the substitution is forced, and how it was measured.** The declared feed (TradingView,
**FXCM**) serves 15-minute GBP/USD back to **2026-05-31** and no further. Established
2026-08-13 by dragging the chart left 368 times until the left-edge date stopped moving for six
consecutive drags. **Only dates were read.** W-A is eleven years out of reach, and PT-022's own
fallback — *"the oldest contiguous 12 calendar months of 15-minute history the feed provides"* —
is equally unobtainable, because the feed provides about **2.5 months**.

`D-027` requires that a range change create a **new test ID** with the abandoned test retained
and marked. PT-022 is marked and unedited; this is the new ID.

## 2. THE PERIOD RULE — A RULE, NOT A DATE, AND FIXED BEFORE THE HARVEST

The dates are **not** written here, because writing them would require harvesting first, and
harvesting first is what pre-registration exists to prevent. What is fixed instead is the
**procedure**, which leaves no discretion at run time:

1. Harvest the **entire contiguous 15-minute GBP/USD series the feed provides**, timestamps and
   OHLC together, no pixel reads.
2. Drop the live-edge artifact (the trailing run of identical OHLC quadruples).
3. Let `T0` = first timestamp and `T1` = last timestamp of what remains. Per `D-028`, the
   **`D-028` boundary** `B = T0 + 0.70 × (T1 − T0)`, rounded **down** to the start of a
   calendar day in the chart's own timezone.
4. **DEVELOPMENT** = `T0 → B` (exclusive of `B`). **HOLDOUT** = `B → T1`, and the holdout is
   **not opened by this test for any purpose**, including bar counting.
5. The test window is the **whole DEVELOPMENT block**. No sub-selection, no trimming, no
   "representative" stretch.
6. `B`, `T0` and `T1` are appended to `D-028` **before any window statistic is computed**.

**This is `D-028`'s own instruction** (*"The first session to establish the data source computes
the 70/30 boundary from the actual available range… and only then opens a chart"*), executed
rather than deferred.

### 2a. The boundary this pins is SCOPED, and the scope matters

What §2 pins is the boundary **for the 15-minute GBP/USD series on the FXCM feed**. It is
**not** a project-wide `D-028` boundary and must not be read as one: the daily series on the
same feed reaches back to at least 2026-02-04, and other timeframes and providers will have
different ranges entirely. **A standing, project-wide boundary needs a standing data-source
decision, which is `I-007` and is the owner's to make.** Recording a scoped boundary is better
than inventing a global one and better than leaving `D-028` unexecuted; it is not a substitute
for the owner's decision.

## 3. WHAT THE SUBSTITUTION LOSES — THREE COSTS, DECLARED BEFORE THE RESULT

**1. Sample size falls from ~260 weekdays to roughly 38.** The available span is ~75 calendar
days; 70% of it is ~52 calendar days, of which ~38 are weekdays. That clears
`BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30 — **but only just**, and §4.2's interval
will be correspondingly wide. **Any fraction reported from this test carries its interval in the
same sentence, and no result from n≈38 may be described as establishing anything.**

**2. The DST straddle is lost, and with it the within-sample arm comparison.** `D-031` §3c and
`COMMON_PROTOCOL.md` §3 chose W-A partly because it spans daylight-saving transitions, making
Arm A and Arm B a **within-sample** comparison. The available period lies **entirely inside US
daylight saving**, so Arm A and Arm B differ by a **constant one hour throughout**. The two arms
still test something real — whether the claim survives a one-hour shift of both windows — but
they no longer test the DST question, and **no result here bears on `A-019`.**

**3. The regime is as far from the taught one as the corpus can get.** V06 was recorded in
March 2012. This period is mid-2026. V06's own homework already measured that GBP/USD's ADR20
is ~65 pips here against the 100–140 typical of 2012. **A claim about session behaviour may
simply be a different claim in a different volatility regime**, and neither a confirmation nor a
contradiction transfers automatically to 2012. This is stated as a limit on **both** outcomes,
so it cannot be deployed selectively against whichever one arrives.

> **The honest summary of §3: this is a weaker test than PT-022 would have been, on every axis
> that matters.** It is run because a weak test that is pre-registered, reported in full and
> declared as weak is worth more to this project than no test at all — and considerably more
> than a strong-looking test on a period chosen after the fact.

## 4. WHAT WOULD MAKE THIS TEST STRONG, FOR WHOEVER COMES BACK TO IT

Recorded now so the follow-up is not re-derived from scratch:

1. **A data source with real intraday history.** The binding constraint is not the method, it is
   the feed. Closing `I-007` with a provider that serves 15-minute history back to 2012–2015
   would let PT-022 run **as originally pre-registered**, and PT-022 is retained intact for
   exactly that reason.
2. **Re-running with the same seed and the same decision rules** on that period, and comparing
   against this result — a genuine out-of-sample replication rather than a re-fit.
3. **The 2012 regime itself**, if any provider reaches it: the only period where the claim can
   be tested against the market the guest was actually describing.

## 5. TO RUN THIS

1. Declare feed and chart timezone in the observation.
2. Harvest the full contiguous 15-minute series; drop the live edge.
3. Compute and **append** `T0`, `T1`, `B` to `D-028`. Confirm the test window is DEVELOPMENT.
4. Run **`N-P` and `N2` first**; only then read the rule arm's aggregate.
5. Write `06_MANUAL_BACKTEST/V06/BT_V06_0001.md`, §0 referencing **this** file and PT-022.
6. **Neither this file nor PT-022 is edited to match what was found.**
