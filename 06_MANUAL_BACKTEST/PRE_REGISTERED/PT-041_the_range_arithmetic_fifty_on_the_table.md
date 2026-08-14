# PT-041 — The range arithmetic: is there "50 pips on the table" after a 25–50 pip stop hunt out of a 25–50 pip Asian range?

> ### RUN 2026-08-14 — **VERDICT: PARTIALLY SUPPORTED.** See `06_MANUAL_BACKTEST/V13/BT_V13_0001.md`.
> The distance is real and large (median MFE **56.8 / 52.9 pips**; `P(MFE ≥ 50)` beats a same-metric
> random-origin control by **+44.9 / +42.2 pp** against a `+10 pp` clause) — **but `O4`, the claim's
> own premise that *"the dealer comes back into the Asian levels"*, holds only **0.704 / 0.701**
> against a pre-registered `0.80`, and `O2` reaches only **0.630 / 0.642** against `0.70`. Both near
> misses; both boundaries were fixed before the runner existed and are honoured.
> ⚠ **§5's control was DEFECTIVE and the defect flattered the claim** — see `BT_V13_0001` §5.

```text
STATUS:      PRE-REGISTERED -- RUN 2026-08-14 -- PARTIALLY SUPPORTED
WRITTEN:     2026-08-14, V13 student session, branch video/v13
ATTESTATION: The session that wrote this file had, at the moment of writing, loaded NO
             price series for this test, run NO aggregation, and computed NO outcome of
             any kind for the question below. Every threshold, window, filter, control
             and decision boundary in SS4-SS6 is fixed HERE and is committed BEFORE
             `scripts/run_pt041.py` exists in the repository.
             Verifiable by commit-timestamp ordering:
                 `git cat-file -e <this-commit>:06_MANUAL_BACKTEST/scripts/run_pt041.py`
             MUST return ABSENT at the commit that adds this file.
```

Governing: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md` · `COMMON_PROTOCOL.md` §§1–4 ·
`D-005`, `D-007`, `D-009`, `D-010`, `D-026`, `D-027`, `D-028`→`D-035`, `D-029`, `D-030`,
`D-031`, `D-036a`.

---

## §1 — THE CLAIM

V13 `[00:35:24]`–`[00:35:59]`, course author, independently ASR-confirmed:

> *"if the **Asian range is 25 to 50 pips**, and the **dealer makes a 25 to 50 pips stop hunt**,
> that's **50 to 100 pips on the table**. If you're trying to **carve out 50** of that, and **you
> catch absolute zero, the bottom or the top**, and the dealer comes back into the Asian levels,
> **you'll hit your 50 pips. You'll hit 40, your stop should be a break even, you should not get
> hurt.**"*

### §1a — PROVENANCE AND SCOPE CAVEATS, BINDING ON THE RUN

1. ⚠ **THIS IS A BEST-CASE TEST BY THE SPEAKER'S OWN STIPULATION.** *"you catch absolute zero, the
   bottom or the top"* is a **perfect-entry** assumption. The measured quantity is therefore a
   **maximum favourable excursion from the exact extreme** — an **upper bound** on what any real
   entry could achieve. **A supported result does NOT mean the trade is profitable; it means the
   distance the speaker claims is on the table is, or is not, actually there.** Every report of
   this test must carry that sentence.
2. ⚠ **THE ARITHMETIC IS STATED INSIDE A WORKED EXAMPLE, NOT AS A RULE.** V13's own
   `V13_INTERPRETATION.md` Q8 marks it *"✅ as a pre-registered TEST, not as a rule"*. **Whatever
   this finds, `25–50`, `50` and `40` may NOT enter `12_MASTER_SPEC/` or `13_MACHINE_SPEC/` on the
   strength of it.**
3. ⚠ ⭐ **`25 to 50` IS A COLLIDING TOKEN IN THIS CORPUS AND THIS TEST IS SCOPED EXPLICITLY.**
   `C-020` §2 records that `25 to 50` now denotes **at least three distinct quantities** across
   V04/V11/V12/V13: the blue box's own **width**, a stop-hunt **excursion beyond** the Asian range,
   and the offset of the **stop-hunt box** from the blue box. **This test uses:**
   - the **first** sense for the range filter (box width 25–50 pips), and
   - the **second** sense for the stop-hunt filter (excursion beyond the box edge 25–50 pips).

   **Both are the senses V13 `[00:35:24]` itself uses**, and they are the senses `PT-014`/`PT-016`
   already measure. **The third sense (box offset) plays no part in this test.** Stated here so
   that no reader can take a result about this arithmetic as evidence about `C-020` §2.
4. **This test does NOT depend on `A-084`, `A-086` or any TDI construction.** It is pure price
   geometry. That is deliberate — it is the only V13 material that is testable at all while the
   indicator records stay blocked.
5. **`A-039` is not engaged.** The test never identifies *"the level"*, a peak formation, or a
   level count. It conditions only on box geometry and excursion size.

---

## §2 — WHAT IS BEING TESTED, IN ONE SENTENCE

> **Conditional on an Asian box of 25–50 pips AND a subsequent excursion of 25–50 pips beyond a box
> edge, does price, measured from the excursion extreme, subsequently travel back at least 40 / at
> least 50 pips within the same session day?**

---

## §3 — DATA, WINDOW AND ARMS

| Item | Value |
|---|---|
| Instrument | **GBP/USD only** (`D-007`) |
| Pip | `0.0001` |
| Source | **HistData GBP/USD M1 corpus**, aggregated locally to M15 (`D-036a`). SHA-256 on record in `datasets/HISTDATA_GBPUSD_M1/raw/SHA256SUMS.txt` |
| Data-QA gate | `scripts/qa_histdata_m1.py` must be cited and C1–C4 must PASS (`COMMON_PROTOCOL.md` §1) |
| **Window** | **`W-B` — 2014-01-05 → 2015-12-31.** Chosen because `COMMON_PROTOCOL.md` §3 designates `W-B` for **conditional-event tests needing more decision points**, and this test applies **two** stacked conditions. Chosen **before** any count of how many days survive them |
| Holdout | **Untouched.** `W-B` is entirely inside the `D-035` development side of the 2016-07-01 boundary; `mmm_lib.assert_development` enforces it and will raise if violated |
| **Arms (`D-031`)** | **BOTH arms, reported separately and never pooled.** A result that holds in one arm and not the other is reported as **arm-dependent**, not averaged |
| Box / post-box definition | `mmm_lib.build_days` as used by `PT-014`/`PT-015`/`PT-016` — box `20:30 → 03:00`, post-box `03:00 → 17:00`. **Unchanged for this test.** Completeness gate `C-6` applied; exclusions reported beside `n` per `completeness_line` |

> **No new box definition is invented for V13.** V13 does not restate the box hours, and inventing
> one to fit its arithmetic would be the `A-082` class of error. The existing, already-reviewed
> definition is reused as-is, and the fact that it comes from earlier lessons rather than from V13
> is a **stated limitation**, §6.

---

## §4 — THE TRIGGER, FIXED NOW

Per session day in `W-B`, in this order:

```text
F1  BOX FILTER.  box_range_pips in [25, 50] inclusive.
F2  EXCURSION.   Let  up_exc = max(post_hi - box_hi, 0) / PIP
                      dn_exc = max(box_lo - post_lo, 0) / PIP
    The day's stop-hunt side is the side with the LARGER excursion.
    Ties (exactly equal, incl. both zero) are EXCLUDED and counted.
F3  EXCURSION FILTER.  the chosen side's excursion in [25, 50] inclusive.
F4  DECISION POINT.  the M15 bar, within the post-box window, at which that
    side's extreme (post_hi for up, post_lo for down) is first attained.
    This is the "absolute zero" entry of SS1.
F5  DIRECTION.  Short if the stop hunt was UP; long if DOWN.
    (V13: "the dealer comes back into the Asian levels".)
```

> ⚠️ **F4 USES A FORWARD-LOOKING EXTREME AND THIS IS DECLARED, NOT HIDDEN.** The bar at which the
> post-box extreme occurs is only knowable after the fact. **That is the speaker's stipulation**
> (*"you catch absolute zero"*), not an oversight, and it is the reason §1a caveat 1 exists. **This
> test is therefore NOT a trading rule and produces NO tradeable signal.** It measures whether a
> distance exists, nothing more. `STUDY_PROTOCOL.md`'s prohibition on using future information to
> make an **initial classification** is not engaged: no classification is being made — the
> excursion extreme is the *measurement origin*, declared as such in advance.

---

## §5 — OUTCOME MEASURES, FIXED NOW

From the F4 bar (exclusive of it), over the remainder of the post-box window of the **same session
day**, in the F5 direction:

```text
MFE  = maximum favourable excursion, in pips, from the F4 extreme price.
       up-hunt  (short): MFE = (extreme_price - min(low of remaining bars)) / PIP
       down-hunt (long): MFE = (max(high of remaining bars) - extreme_price) / PIP
       If no bars remain after F4, the day is EXCLUDED and counted.

O1 = P(MFE >= 50)      <- "you'll hit your 50 pips"
O2 = P(MFE >= 40)      <- "You'll hit 40"
O3 = median MFE, with a 2,000-iteration bootstrap CI
O4 = P(price returns INTO the box at all), i.e. re-enters [box_lo, box_hi]
     <- "the dealer comes back into the Asian levels", the claim's own premise
```

**`O4` is reported first in the result table.** If the premise fails, `O1`/`O2` are answering a
question whose antecedent does not hold, and the report must say so.

### The control — `D-029`, fixed now

`mmm_lib.n1_matched_random`: **matched random entry** over the same trade grid, same directions,
same session days, `ITERATIONS` and `SEED` as the library defines. The control answers *"is 40–50
pips simply what GBP/USD does in a London/NY afternoon?"* — which is the obvious deflationary
explanation and must be measured, not argued about.

---

## §6 — DECISION RULE, FIXED NOW, BEFORE ANY NUMBER EXISTS

The claim is stated as an **expectation** (*"you'll hit"*), not a guarantee. Fixed boundaries:

| Verdict | Condition — **all** clauses required |
|---|---|
| ✅ **SUPPORTED** | `n ≥ 30` in **both** arms · `O4 ≥ 0.80` · `O2 ≥ 0.70` · `O1 ≥ 0.50` · `O1` exceeds the matched-random control by **≥ 10 pp** · holds in **both** `D-031` arms |
| ⚠️ **PARTIALLY SUPPORTED** | `n ≥ 30` · `O2 ≥ 0.50` but the SUPPORTED clauses are not all met |
| ❌ **NOT SUPPORTED** | `O2 < 0.50`, **or** `O1` fails to beat the control by ≥ 10 pp |
| 🚫 **INCONCLUSIVE** | `n < 30` in either arm after F1–F4 and the exclusions |

**Stated explicitly so it cannot be softened later:** if `O1` clears 0.50 but does **not** beat the
matched-random control by 10 pp, the verdict is **NOT SUPPORTED**, however large `O1` is. A
distance that random entry also reaches is not evidence for the claim. This mirrors `PT-040`'s
discipline, where a boundary fixed in advance produced an inconvenient verdict and was honoured.

### Known limitations, recorded now rather than as post-hoc excuses

1. **The box definition is inherited from earlier lessons, not from V13.** V13 states no box hours.
2. **Perfect entry** — §1a caveat 1. Upper bound only.
3. **No spread, no commission, no slippage.** Distances only.
4. **`W-B` is 2014–2015; the lesson is 2012.** `COMMON_PROTOCOL.md` §1 records that price *levels*
   are not comparable across vendors and eras; **only shape and distance claims travel**, and this
   is a distance claim.
5. **Same-session-day horizon.** V13 gives no time stop for this example. A multi-day horizon is a
   different test and is not run.
6. **`25–50` and `40`/`50` are the speaker's numbers, tested as given.** No sweep over neighbouring
   thresholds is performed, because a sweep would convert a claim test into a search for an edge.

---

## §7 — RUN ORDER, FIXED NOW

```text
1. Cite the qa_histdata_m1.py report; abort if C1-C4 do not PASS.
2. Load M1 -> M15 for BOTH D-031 arms; window to W-B; assert_development.
3. build_days(); report completeness_line() exclusions.
4. Apply F1; report n. Apply F2/F3; report n and tie-exclusions.
5. Compute O4 FIRST, then O1, O2, O3.
6. Compute the matched-random control.
7. Apply SS6 verbatim. Write BT_V13_0001.md.
```

**Steps 5 and 6 are ordered so that `O4` — the claim's own premise — is computed before the
headline rates, and the control before the verdict.**

### Related

`PT-014` (excursion size distribution beyond the box), `PT-015` (does the 50-pip ceiling exist),
`PT-016` (Asian range under 50 as a filter), `PT-001`; `C-020` §2; `A-076`;
`03_LESSON_NOTES/V13_SOURCE_NOTES.md` §5.10; `V13_INTERPRETATION.md` Q8.
