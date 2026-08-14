# PT-046 — V18's "TWO SESSIONS OF RISE OR FALL, THIRD SESSION CORRECTIVE IN NATURE"

**Pre-registered:** 2026-08-14, by the V18 student session.
**Status at commit time:** ⚠️ **NO BAR HAS BEEN READ. NO RUNNER EXISTS.** This file is committed
**before** `run_pt046.py` is written, per `COMMON_PROTOCOL.md` §9 rule 7. **If the runner and this
file ever disagree, THIS FILE GOVERNS**, neither is edited, and the disagreement is reported in
`BT_V18_0001.md`.

---

## §1 — THE CLAIM UNDER TEST

V18 states one rule more often, and more emphatically, than anything else in the lesson. It is
spoken **four times**, the class is told to write it down, and an independent ASR engine returns
all four repetitions verbatim:

> `[00:08:43]` *"**Two sessions of rise or fall with the third session being corrective in
> nature.**"*
> `[00:08:41]` *"**Write that down.**"*
> `[00:09:59]` *"Two sessions of rise or fall, third session corrective in nature, **fourth session
> should resume the trend** that was underway by the dealer."*

He defines `corrective` narrowly and **direction-relatively**, `[00:09:06]`: *"I'm just saying
corrective in nature meaning **it goes against the trend**"* — explicitly **not** "goes down"
(`[00:08:48]` *"I don't mean it's going to sell off"*).

**The testable core:** over a sequence of consecutive trading sessions, once **two** consecutive
sessions have moved in the **same** direction, the **third** is more likely to move **against** that
direction than the base rate would predict.

### §1a — ⚠ WHAT THIS TEST DELIBERATELY DOES **NOT** TEST

* **No entry, exit, stop, target, M, W, peak formation or level is computed anywhere.** This is a
  test of a *directional-sequence* claim only. It is not a strategy backtest and must not be cited
  as one.
* **The "fourth session resumes the trend" half is measured but NOT used as a decision criterion**
  (see §5 O4), because V18 gives **no discriminator** between *resume* and *reverse* (`A-129`), so a
  failure there would be uninterpretable.

---

## §2 — ⚠⚠ THE PRE-REGISTERED WEAKNESS, DECLARED BEFORE THE RUN

**V18 NEVER STATES A CLOCK TIME FOR ANY SESSION.** Token census over the committed transcript:
`Asian range` × 8, `London` × 2, `U.S. session` × 4, and **zero** hour figures attached to any of
them. `V18_SOURCE_NOTES.md` §8.1 and `A-131` record this.

**Consequence:** the session boundaries below are a **DECLARED CONVENTION OF THIS TEST**, not a
reading of the lesson. **They are the single largest threat to this test's validity and they are
stated here, before the run, rather than defended after it.**

⭐ **AND V18 EXPLICITLY REFUSES TO FIX WHICH SESSION PLAYS WHICH ROLE**, `[00:09:27]`: *"**Now I
can't say the U.S. sessions always corrective in nature. I cannot say that** because the dealers
change the session and who gets to be the corrector and who gets to be the correctee."*

**This refusal is a gift to the test design, not an obstacle**: it means the claim is about
*position in a run*, not about *named sessions*, so the test must be **invariant to which session is
labelled which**. The design below is: it counts runs over an unbroken session sequence and never
conditions on a session's name.

### §2a — THE DECLARED PARTITION

The session day is `mmm_lib` C-1's `[D−1 17:00, D 17:00)` on the arm's own clock. It is partitioned
into **exactly three** contiguous sessions, no gaps, no overlaps:

| Session | Window (arm clock) | Hours |
|---|---|---|
| `S1` "Asian" | `17:00 → 03:00` | 10 |
| `S2` "London" | `03:00 → 09:00` | 6 |
| `S3` "US" | `09:00 → 17:00` | 8 |

**Why these:** `03:00` and `17:00` are already load-bearing project constants (`BOX_END_MIN`,
`DAY_END_MIN`, conventions C-1/C-2/C-3), so two of the three boundaries are inherited rather than
invented. **`09:00` is invented for this test** and is the weakest line in the design.

**Sensitivity is therefore MANDATORY, not optional** — see §5a N3.

---

## §3 — CORPUS, ARMS, WINDOWS, INCLUSION

| Field | Value |
|---|---|
| Instrument | **GBP/USD**, HistData M1 corpus (`D-036a`), checksummed |
| Bars | **M15**, via `mmm_lib.load_m15()` |
| Arms | **A and B**, the `D-031` timezone arms. Reported **separately**, never pooled |
| Primary window `W-D` | `D-035` **DEVELOPMENT**, `mmm_lib` default scope |
| Replication window `W-E` | the `D-044` **extension**. Reported **separately from `W-D`, never pooled** (`COMMON_PROTOCOL.md` §4) |
| Holdout | `2016-07-01 → 2016-12-31` is **sealed, not on disk, not touched** |

**Completeness (`mmm_lib` C-6, generalised):** a session day is **INCLUDED** only if **all 96**
fifteen-minute buckets of its `17:00 → 17:00` span carry ≥ 1 M1 bar. **Exclusions are COUNTED AND
REPORTED beside `n`**, never dropped silently. Nothing is excluded for being unrepresentative — no
holiday, news or volatility filter.

**Sequence breaks.** A run of same-direction sessions may **only** be counted across sessions that
are **adjacent in the corpus**. Where a session day is excluded, or where the weekend intervenes,
**the run counter RESETS**. ⚠️ **This is pre-registered deliberately**: the V17 R1 round found that
allowing calendar-consecutive-but-not-actually-adjacent readings produced an artefact, and the
control that exposed it is reproduced here as §5a N5.

---

## §4 — DIRECTION OF A SESSION

`dir(S) = sign(close(S) − open(S))`, where `open(S)` is the open of the **first** M15 bar whose
timestamp falls in the window and `close(S)` the close of the **last**.

* `+1` rise · `−1` fall · `0` exact tie.
* **A `0` session BREAKS a run and is counted separately.** It is neither a continuation nor a
  correction. Expected to be very rare on M15 GBP/USD; the count is reported.

---

## §5 — MEASURES

Let a **prior pair** be two adjacent sessions with the same non-zero direction `d`.

| ID | Measure |
|---|---|
| **O1 — PRIMARY** | `P(dir(S₃) = −d │ dir(S₁) = dir(S₂) = d)` — the probability the third session corrects |
| **O2 — THE BASE RATE** | `P(dir(Sₙ₊₁) = −dir(Sₙ))` unconditionally — the probability *any* session reverses the one before it |
| **O3 — THE LIFT** | `O1 − O2`. **This is the quantity the claim lives or dies on** |
| **O4 — reported, NOT decisional** | `P(dir(S₄) = d │ S₁,S₂ = d and S₃ = −d)` — does the fourth resume? (`A-129`: no discriminator exists, so this is descriptive only) |
| **O5** | Distribution of run lengths; **median and modal run length**. The claim implies mode 2 |
| **O6** | `n` prior pairs, `n` sessions, `n` excluded days, `n` zero-direction sessions |

---

## §5a — CONTROLS, ALL PRE-REGISTERED

| ID | Control |
|---|---|
| **N1** | **Matched-random.** Shuffle the session-direction sequence within each window/arm, preserving the counts of `+1`/`−1`/`0` exactly, `SHUFFLE_ITER = 200`, seeded from `mmm_lib.SEED`. Recompute O1/O2/O3. **Report the percentile of the observed O3 in the shuffled distribution.** A real cycle must sit in the tail |
| **N2** | **Run-length null.** Under an i.i.d. fair sequence the run-length distribution is geometric with mode **1**, not 2. Report observed vs geometric |
| **N3** | ⚠ **MANDATORY BOUNDARY SENSITIVITY.** Re-run the whole test with the invented `09:00` boundary moved to **`08:00`** and to **`10:00`**. **If O3's sign or decision flips across those three, the result is DECLARED FRAGILE and the verdict is downgraded to `INCONCLUSIVE` regardless of the primary figure.** This is the pre-registered guard on §2's weakness |
| **N4** | **Exclusion accounting.** Report excluded-day count and the completeness line for every window/arm |
| **N5** | **Adjacency artefact control.** Re-run allowing runs to bridge weekend/excluded gaps (i.e. calendar-consecutive rather than corpus-adjacent). **Reported beside the primary, never substituted for it.** This is the V17 R1 artefact test, reproduced |

---

## §6 — THE DECISION RULE, FIXED NOW

Evaluated on **`W-D`, Arm A** as primary; `W-D`/Arm B and `W-E` are replication.

| Verdict | Condition |
|---|---|
| ✅ **SUPPORTED AS STATED** | `O3 ≥ +0.05` **AND** observed O3 above the **95th percentile** of N1 **AND** N3 does not flip sign |
| 🔶 **WEAKLY SUPPORTED** | `+0.02 ≤ O3 < +0.05`, N1 percentile ≥ 90, N3 stable |
| ⬜ **NOT SUPPORTED** | `−0.02 < O3 < +0.02`, or N1 percentile < 90 |
| ❌ **CONTRADICTED AS STATED** | `O3 ≤ −0.05` with N1 percentile ≤ 5 |
| ⚠️ **INCONCLUSIVE** | N3 flips the sign or the decision, **overriding any of the above** |

**Replication is reported, and disagreement between arms or windows is reported as disagreement.
It does not change the primary verdict.**

---

## §7 — WHAT A NULL RESULT WOULD AND WOULD NOT MEAN

**A `NOT SUPPORTED` here does NOT refute V18.** The lesson's rule is stated about *the dealer's*
sessions with **no clock times** (§2) and V18 explicitly says which session corrects **varies**
(`[00:09:30]`). This test necessarily substitutes a fixed clock partition for a thing the lesson
leaves floating.

**What a null WOULD establish** is narrower and still worth having: *that the claim, under the most
natural fixed-clock reading available, does not survive contact with 2013–2025 GBP/USD.* That is a
constraint on **coding** it, which is the only reason this project tests anything.

**Pre-registered honesty clause:** if the result is null, `BT_V18_0001.md` **states it plainly in
its first line** and does not go looking for a partition that rescues it. N3 exists precisely to
stop that search from happening after the fact.
