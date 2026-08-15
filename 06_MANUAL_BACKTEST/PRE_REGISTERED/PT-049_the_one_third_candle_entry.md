# PT-049 — V20's ONE-THIRD ENTRY: `entry = high − (candle range ÷ 3)`

**Pre-registered:** 2026-08-15, by the V20 student session (remediation round for V20 R1).
**Status at commit time:** ⚠️ **NO BAR HAS BEEN READ. NO RUNNER EXISTS.** Committed **before**
`run_pt049.py` is written, per `COMMON_PROTOCOL.md` §9 rule 7. **If the runner and this file ever
disagree, THIS FILE GOVERNS**, neither is edited, and the disagreement is reported in
`BT_V20_0002.md`.

⚠️⚠️ **AND THE DISAGREEMENT CLAUSE IS NOT DECORATION THIS TIME.** `PT-048`'s runner bypassed its own
§3.1 swing scale, the divergence flipped the verdict, and `BT_V20_0001.md` §6 asserted there was no
such divergence (V20 R1 `M1`, item 332). **§3 below therefore states every scale ONCE, inside the
measure that uses it, and §6 requires the sensitivity to be published on every run.**

---

## §1 — WHY THIS TEST EXISTS

**`PT-048` §1a excluded this rule from testing on a false premise:** *"Not the one-third entry.
'Handle' is undefined — `A-136`, `D-030`."* ⛔ **There is no word *"handle"*.** The committed
transcript mis-hears `candle`; five independent ASR decodes agree (`V20_TRANSCRIPT.md` §2a), and
**`A-136` is closed as an ASR artifact** (V20 R1 `M2`, item 333).

**With the correct word the rule is complete**, `[00:29:14]`–`[00:29:53]`:

> *"I'm going to give you **the best way to decide the entry** […] Take the distance of this
> **candle** divided by three […] take your entry **one-third off the high of this candle** […] Take
> the length of the candle, let's say it's **100 pips** […] **Subtract 33 pips off the high**, a
> third, and put an entry right here."*

> ### THE RULE
> **`entry = high − (range ÷ 3)`** for a short off a candle's high; mirrored,
> **`entry = low + (range ÷ 3)`** for a long off its low.

⭐ **This is the first entry rule in the studied corpus whose arithmetic `D-030` does not block.**

---

## §2 — ⚠️⚠️ THE PRE-REGISTERED WEAKNESSES, DECLARED BEFORE THE RUN

### (a) ⭐⭐ WHICH CANDLE IS NOT STATED — `A-139`, AND IT IS THE WHOLE THREAT

The lesson points at *"**this** candle"* and gives **no selection rule in words**. **The bar choice
in §3 is A DECLARED CONVENTION OF THIS TEST AND IS NOT A COURSE RULE** (`D-010`, `D-030`).

⚠️⚠️ **`PT-048` was decided by an undeclared convention on its primary measure. This file will not
repeat that:** ⭐ **three bar-selection conventions are pre-declared below, ALL THREE are reported,
and the primary is named HERE before any number exists.**

### (b) THE TEST MEASURES FILL-AND-EXCURSION, NOT PROFIT

V20 gives an entry and **no stop and no target** in this passage. **No P&L, no R, no win rate is
computed.** What is measured is whether the entry **fills** and what price does afterwards. ⚠️ **A
high fill rate is NOT evidence the rule is good** — a deeper retracement fills more often and enters
worse. **Both are reported.**

### (c) NO DIRECTIONAL FILTER IS APPLIED, AND THE LESSON HAS ONE

V20's entry sits inside a short setup (railroad tracks at the high, `[00:28:55]`). **Identifying
that setup needs the *blue tracer* (`A-133`) and the eight-bar M/W count.** ⛔ **This test therefore
does NOT test the setup; it tests the ENTRY ARITHMETIC in isolation**, on both sides, and says so.

### (d) THE `÷ 3` IS EXACT AND THE COMPARISON SET IS NOT

To know whether one-third is special the test must compare it against other fractions. **`1/4`,
`1/3`, `1/2` and `2/3` are fixed now** as the comparison set. ⚠️ **Any of them "working better" is
NOT evidence against V20** — the lesson states a practice, not an optimum, and `D-009` bars
optimising toward a claimed rate.

### (e) SESSION AND TIMEFRAME

**M15**, now attested in print on three V20 charts (`04_SCREENSHOTS/V20/INDEX.md` §11), still never
spoken. GBP/USD, `D-011`. **Both `D-031` arms; no named session is conditioned on** — V20's only
clock reference timestamps a reading, not a boundary (`V20_INTERPRETATION.md` §2.6).

---

## §3 — OPERATIONAL DEFINITIONS — FIXED NOW

Data: HistData GBP/USD M1 → M15 via `mmm_lib.load_m15()`, arms **A** and **B**, scope **DEVELOPMENT
only** (`D-035`). Windows: **`W-A`** (2015) primary, **`W-B`** (2014-01-05 → 2015-12-31) as a
**wider-window replication — `W-B` CONTAINS `W-A` and is not independent.**

### The candidate candle — three conventions, all reported, primary named now

Within a session day's post-box bars (`03:00 → 17:00`):

| ID | Convention | Motivation |
|---|---|---|
| ⭐ **`S1`** — **PRIMARY** | the bar that sets the **running high of the day**, where its range is **≥ 25 pips** | closest to `[00:28:55]`'s railroad-track bar setting the HOD |
| `S2` | **any** bar whose range is **≥ 25 pips** (a *"big"* candle) | the loosest reading of *"this candle"* |
| `S3` | the bar **immediately after** an `S1` bar — *"shift his [zone] in the next candle"* `[00:28:36]` | the other contextual candidate |

**`S1` is primary and is named primary HERE, before any number exists.** The **25-pip** range floor
is fixed now; it is this test's convention (V20's own spike figure is *"25 to 50"*, `[00:22:15]`).

### The entry and the outcomes

For a candidate candle with high `H`, low `L`, range `R = H − L`, on bar `t`:

* **Short entry price:** `E = H − R/3`. **Long entry price:** `E = L + R/3`.
* **`O1` — FILLED?** Does any bar in `t+1 … t+8` (2 hours) trade at or beyond `E`?
* **`O2` — MFE after fill**, in pips, over the remainder of the 8 bars, in the trade's direction.
* **`O3` — MAE after fill**, in pips, against it.
* **`O4` — `O2 − O3`**, reported for scale only. ⛔ **NOT a P&L and NOT a verdict input.**

**Fractions compared:** `1/4`, `1/3`, `1/2`, `2/3` — `O1`/`O2`/`O3` computed for each.

**Every rate carries a Wilson 95 %; every median carries a bootstrap 95 %.**
**`n ≥ 30` per cell or the cell is labelled `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only`.**

---

## §4 — THE BASELINE (`D-026`) — ⭐ AND IT IS A CONDITION OF THE VERDICT THIS TIME

**`N1` — fraction-shuffled control.** For each candidate candle, compute the same outcomes at a
retracement fraction drawn uniformly from `[0.05, 0.95]`. **10,000 draws, `seed = mmm_lib.SEED`.**
**The null is that one-third is not distinguishable from an arbitrary fraction of the same candle.**

⚠️⚠️ **`PT-048` NAMED ITS NULL AND NEVER SCORED IT** (`BT_V20_0001.md` §3a; V20 R1 §2.5 ruled its
standing result a NULL). ⭐ **§5 below therefore makes `N1` an EXPLICIT CONDITION of every
non-null verdict.**

**`N3` — the fragility guard.** ⚠️ Fires and downgrades any positive result to `FRAGILE` if **any**
of:

* the three bar conventions `S1`/`S2`/`S3` **disagree in direction** on `O2`'s median;
* arms **A**/**B** or windows `W-A`/`W-B` disagree in direction;
* any cell has **`n < 30`** fills;
* ⭐ **the `1/3` result is not distinguishable from the `1/4` and `1/2` results** — i.e. their
  `O2` medians' bootstrap intervals all overlap `1/3`'s. *(Added because a fraction that is not
  special is the most likely real outcome and must not read as a confirmation.)*

---

## §5 — THE DECISION RULE, FIXED NOW

On **arm A, window `W-A`, convention `S1`, fraction `1/3`** (the primary cell):

| Verdict | Condition |
|---|---|
| **CONFIRMED** | `O1` fill rate **≥ 50 %** (Wilson lower bound above 50 %) **AND** median `O2` **>** median `O3` with non-overlapping bootstrap intervals **AND** the `1/3` cell **beats `N1`'s random-fraction median `O2 − O3`** **AND** `N3` does not fire |
| **PARTIAL** | the entry fills at ≥ 50 % **but** the excursion asymmetry or the `N1` comparison fails |
| **REFUTED** | fill rate's Wilson upper bound is **below 50 %**, **or** median `O3` exceeds median `O2` with non-overlapping intervals |
| **FRAGILE** | any `N3` condition fires. **Reported as a null.** |

⚠️ **A median outside a threshold whose interval overlaps it falls to `PARTIAL`, explicitly** —
closing the hole V20 R1 §2.6 found in `PT-048` §5 (same shape as V17 R1's item 259).

⭐ **What `CONFIRMED` would mean:** that the one-third retracement is a **reachable** entry that is
**better than an arbitrary fraction** of the same candle. ⛔ **It would NOT mean the rule is
profitable or tradeable** — no spread, slippage, cost, stop or target is modelled anywhere;
`D-006` defers all of it to Phase 8.

---

## §6 — WHAT WOULD MAKE THIS TEST WRONG, AND ONE MANDATORY OUTPUT

1. ⭐⭐ **The bar-selection convention (§2a) is this test's, not the course's.** Largest attack.
2. **The 25-pip range floor is arbitrary within its motivation.**
3. **The 8-bar (2 h) fill window is a convention.** V20 gives no expiry for an unfilled entry.
4. **No setup filter is applied** (§2c), so this measures the arithmetic and not the trade.
5. ⛔⛔ **MANDATORY OUTPUT: the runner MUST publish the outcome across all three bar conventions AND
   all four fractions on every run**, whether or not they are the primary. **`PT-048`'s verdict
   turned on a scale nobody could see; no figure this test depends on may be invisible again.**
