# PT-050 — V21's `High / Low Trainer` GRID: THE 20-PIP SPACING AND THE `50-PIP AVERAGE MOVE`

**Pre-registered:** 2026-08-15 by the V21 student session.
**Status at commit:** ⚠️ **NO BAR READ. NO RUNNER EXISTS.** Committed **before** `run_pt050.py` is
written (`COMMON_PROTOCOL.md` §9 rule 7). **If the runner and this file disagree, THIS FILE
GOVERNS**, neither is edited, and the disagreement is reported in `BT_V21_0001.md`.

---

## §1 — THE CLAIM UNDER TEST

V21 `[00:32:58]`, giving the reason the script's take-profit was set where it is:

> *"the take profit had to be adjusted down because **the average move even in stop [hunts] is about
> 50 pips**"*

and the grid it justifies — `[00:31:58]`, with the handwritten sheet at `31:25`:

> *"a market order […] **with two pending orders, 20 pips above [each]**, and a hard stop-loss on all
> three […] approximately a **60-pip grid**"* · sheet: *"↕ 20 pips ↕ 20 pips ↕ 20 pips"*

**Two testable cores:**

> **(A)** Is the excursion after a stop-hunt-type event **about 50 pips** at the median?
> **(B)** Given a 20/20 grid placed against that event, **how many of the three orders fill**, and
> is the *"most often"* case the two-order one the lesson describes?

### §1a — ⚠️ WHAT THIS DOES **NOT** TEST

* ⛔ **Not the script.** The artifact is not in this repository (`A-141`) and is not reconstructed.
* ⛔ **Not *"lose at a discount"*.** That is arithmetic, not an empirical claim
  (`V21_INTERPRETATION.md` §2.1), and its open question — the win side — needs a full trade model
  this test does not build (`A-140`).
* ⛔ **No P&L, expectancy, spread, slippage or lot sizing.** `D-006` defers all of it to Phase 8.
  ⚠️ **The risk dial (1–5 %) is a POSITION-SIZING parameter and nothing here touches it.**
* ⛔ **Not the assessment ladder.** Its inputs are one trader's fills over time, not a corpus.

---

## §2 — ⚠️ PRE-REGISTERED WEAKNESSES

**(a) *"Stop hunt"* is not defined by V21 as an algorithm.** ⭐ **This test therefore REUSES
`PT-047` §3's exceed-event definition verbatim** — first bar per session day whose high exceeds a
running day-high that is 8–24 bars old, with ≥16 bars remaining. ⚠️ **That is a DECLARED CONVENTION
BORROWED FROM ANOTHER TEST, not V21's**, chosen because it is already twice-reviewed and because
inventing a fresh one here would be a free parameter. **Named as the largest threat.**

**(b) The grid direction.** V21's example is *"you think you see an M"* — a **short**. The grid sits
**above** the entry, in the direction the dealer would push. **This test places it that way and does
not test the long side**, which the lesson mirrors but does not work through.

**(c) The 50-pip figure is *"about"*.** ⚠️ **A band must be fixed in advance or any result confirms
it.** ⭐ **FIXED NOW: `[40, 60]` pips**, i.e. 50 ± 20 %. **A median outside that band is not *"about
50"*.**

**(d) `M15`, GBP/USD, both `D-031` arms, DEVELOPMENT only** (`D-035`). Windows `W-A` (2015) primary,
`W-B` (2014-01-05 → 2015-12-31) — ⚠️ **`W-B` CONTAINS `W-A`; a wider-window replication, not an
independent one.**

**(e) ⚠️ The events are the same population `PT-047` measured.** **This is not an independent
sample from that test**, and any agreement between them is expected, not corroborative.

---

## §3 — OPERATIONAL DEFINITIONS — FIXED NOW

Event: **exactly `PT-047` §3** — level `L`, event bar `t`, one event per session day.

**Outcome A — the move.** `MFE` above `L` over `t+1 … t+16`, in pips. Report **median with a
bootstrap 95 % interval**, and the fraction landing in `[40, 60]` with a **Wilson 95 %**.

**Outcome B — the grid.** Place three orders relative to `L`: **`G0 = L`, `G1 = L + 20 pips`,
`G2 = L + 40 pips`.** Over `t+1 … t+16` count how many are touched. Report the **distribution over
{0,1,2,3} filled**, each with a Wilson 95 %, and **the modal cell**.

**Every rate carries a Wilson 95 %; every median a bootstrap 95 %; `n ≥ 30` per cell or the cell is
labelled `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`.**
⭐ **Mandatory per `BACKTEST_EVIDENCE_STANDARD.md` §4.2/§5 and `REVIEW_INDEX.md` item 302.**

---

## §4 — BASELINE AND GUARD

**`N1` — matched random windows.** Same-length windows from the same days and hours with **no exceed
condition**, both outcomes recomputed. **The null is that the 50-pip figure and the fill
distribution describe the instrument, not the event.**
⭐⭐ **`N1` IS AN EXPLICIT CONDITION OF EVERY NON-NULL VERDICT** (§5) — the defect `PT-048` §3a
self-reported and V20 R1 §2.5 ruled on.

**`N3` — fragility guard.** Fires ⇒ `FRAGILE`, reported as a null, if any of: arms A/B disagree on
band membership for Outcome A; `W-A`/`W-B` disagree; any cell `n < 30`; or the modal fill cell
differs between arms.

---

## §5 — DECISION RULE, FIXED NOW

On **arm A, `W-A`** (primary):

| Verdict | Condition |
|---|---|
| **CONFIRMED** | median MFE **and its whole bootstrap interval** lie inside **`[40, 60]`** **AND** the median differs from `N1`'s **AND** `N3` silent |
| **PARTIAL** | median inside `[40, 60]` but the interval escapes it, **or** `N1` is not beaten |
| **REFUTED** | the interval lies **entirely outside** `[40, 60]` |
| **FRAGILE** | any `N3` condition. **Reported as a null.** |

⚠️ **A median outside the band whose interval overlaps it falls to `PARTIAL` explicitly** — closing
the decision-table hole V20 R1 §2.6 found in `PT-048` §5.

⭐ **Outcome B is REPORTED, NOT SCORED.** V21's *"most often"* is not a quantified claim and this
file will not invent a threshold for it after the fact.

---

## §6 — WHAT WOULD MAKE THIS WRONG

1. **The borrowed event definition (§2a) is not V21's.** Largest attack.
2. **The `[40, 60]` band is this test's operationalisation of *"about 50"*.**
3. **Touch-to-fill assumes no spread and no slippage** — an order *"touched"* is not an order filled.
4. **The 16-bar horizon is `PT-047`'s convention**, not a V21 expiry.
