# PT-043 — V15's DAILY restatement: does the session day close **25–50 pips off its own high or low**?

> ### RUN 2026-08-14 — **VERDICT: `O1` NOT SUPPORTED · `O2` CONTRADICTED AS STATED.** See `06_MANUAL_BACKTEST/V15/BT_V15_0001.md`.
> `O1` (V15's *"or"*) = **0.3640** against an `N1` random-intraday-close control of **0.3757** —
> **the real close does WORSE than an arbitrary minute of the same day.** `O2` (V10's *"and"*) =
> **0.0939**, below §6 clause (a)'s 0.10 floor for an *"always"*. **Identical verdicts in all four
> window × arm cells.** The median nearer-distance is **21.4 pips**, just under the band's 25-pip
> floor. **5 of 5 substantive predictions right, and discounted in `BT_V15_0001` §7 because P1–P3
> were largely one prediction inherited from `BT_V10_0001`.**

```text
STATUS:      PRE-REGISTERED -- RUN 2026-08-14 -- O1 NOT SUPPORTED / O2 CONTRADICTED
WRITTEN:     2026-08-14, V15 student session, branch video/v15
LESSON:      V15 -- Bootcamp1 Wk7 050612 Part1 (52mins).swf
             SHA-256 5308c350193b7cf9471ecb3f534b27fc7e8c1cd21e1cd94eb9521e7e56482b49
SPEAKER:     the COURSE AUTHOR, 100% of runtime (D-033 makes this immaterial to
             weight; recorded because provenance is owed)

ATTESTATION: The session that wrote this file had, at the moment of writing, loaded NO
             price series for this test, run NO aggregation, and computed NO outcome of
             any kind for the question below. Every threshold, window, filter, control
             and decision boundary in §§3-6 is fixed HERE and is committed BEFORE
             `scripts/run_pt043.py` exists in the repository.
             Verifiable by commit-timestamp ordering:
                 `git cat-file -e <this-commit>:06_MANUAL_BACKTEST/scripts/run_pt043.py`
             MUST return ABSENT at the commit that adds this file.
```

Governing: `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md` · `COMMON_PROTOCOL.md` §§1–4 ·
`D-005`, `D-007`, `D-009`, `D-010`, `D-026`, `D-027`, `D-029`, `D-030`, `D-031`,
`D-035`, `D-036a`, `D-044`.

---

## §0 — NUMBERING

`PT-043` is the next free number: `PT-001` … `PT-042` exist, `PT-042` being V14's.
Allocated against the **integration branch** state after this session's merge of
`origin/claude/add-documents-repository-fdfb3u` at `fb9eee5`, per `D-038a` consequence 1.

---

## §1 — THE CLAIM

V15 `[00:31:20]`–`[00:31:36]`, course author. **The wording is the second-ASR-arbitrated one**;
the committed grid reads *"off of the higher low"* and an independent `whisper` pass returns
*"off of the high or low"* (`V15_TRANSCRIPT.md`, correction 11):

> *"That tells you that the dealer has made his entire run for the day. **We know that they always
> complete the cycle. Twenty-five to fifty pips off of the high or low, depending on the pair,
> right? And they want to end back in the range to trap the traders for tomorrow.**"*

### §1a — WHAT THE CLAIM IS ABOUT, AND WHY IT IS NOT `PT-036`'s `M2`

⚠⚠ **THIS TEST EXISTS ONLY BECAUSE THE OBJECT IS DIFFERENT. READ THIS BEFORE ANYTHING ELSE.**

`PT-036` `M2` already tested a **25–50 pip** claim from V10 and `BT_V10_0001` reported it. **They
are not the same claim**, and the difference is stated here so that the reviewer can reject this
test on the spot if the difference does not hold up:

| | V10 `M2` (`PT-036`, already run) | **V15, this test** |
|---|---|---|
| Verbatim | *"the dealer will end **always 25 to 50 pips off of the high and 25 to 50 pips off of the low**"* | *"they always complete the cycle. **25 to 50 pips off of the high or low**"* |
| Context | `[00:13:03]`–`[00:13:52]`, explicitly about **Friday** and the weekend gap | `[00:31:20]`, explicitly about **the day**: *"his entire run **for the day**"*, *"trap the traders **for tomorrow**"* |
| Period | **weekly** — one observation per week | **daily** — one observation per session day |
| Conjunction | **AND** — both distances in band | **OR** — the weaker reading |
| n available in `W-B` | ~104 Fridays | ~520 session days |

**Two independent differences (period and conjunction), either of which alone would make this a
different measurement.** `PT-036` `M2` is nevertheless the natural comparator and §5 reports
against it.

### §1b — WHAT IS **NOT** TESTED HERE, AND WHY

⭐ **V15's other quantitative claim, *"The weekly range is 600 to 1000 pips"* (`[00:38:26]`,
`A-095` figure 2), is DELIBERATELY NOT RE-TESTED.**

`PT-036` `M1` tested exactly that figure on exactly this corpus and `BT_V10_0001` returned
**`CONTRADICTED AS STATED` — 0 of 180 weeks in band, upper Wilson bound 2.09%.** **Re-running a
contradicted claim because a second lesson repeats it would be a waste of the corpus and, worse,
an invitation to a second look at a question already answered.** `D-027` exists to stop exactly
that.

**What V15 contributes on that figure is DURABILITY, not a new question:** the same number is
restated **three weeks later, in a different lesson, with no hedge and no reference to the
earlier statement.** That strengthens the reading that it is doctrine rather than an aside — which
makes `BT_V10_0001`'s contradiction *more* consequential, not less. **Recorded in `A-095` and in
`V15_MASTERY_REPORT.md`; no runner is written for it.**

V15's third figure, *"limitations of about 200 pips"* (`[00:27:39]`), names no pair and is
**untestable as stated** (`A-095` figure 3). Not tested.

⛔ **AND THE LESSON'S HEADLINE — THE ADR CONFLUENCE RULE — IS NOT TESTABLE AT ALL RIGHT NOW.**
`A-100` records that the ADR's lookback, range definition, anchor and day boundary are stated
**nowhere in Tier 1**, and `C-022` records that the lesson says the levels *"creep up or creep
down to fit price action"* and are *"not repaint"* ten seconds apart. **Until `C-022` is settled,
any backtest reading an ADR level at a past timestamp would be guessing whether that level was
visible then — lookahead bias by construction.** This is the reason this session tests a
close-position claim and not the lesson's own rule, and it is stated in advance rather than
offered afterwards as an excuse.

---

## §2 — THE QUESTION

**Does the session day's close sit 25–50 pips away from the day's own high or low, at a rate that
a random intraday moment does not achieve?**

The second clause is the whole test. A day whose total range is, say, 90 pips will put *any*
moment somewhere; the claim has content only if **the close specifically** is placed in that band
more often than an arbitrary minute of the same day.

---

## §3 — CONSTRUCTION — every definition fixed here, before any data is read

| Object | Definition | Source |
|---|---|---|
| Instrument | **GBP/USD**, HistData M1 bid bars | `D-036a`; `COMMON_PROTOCOL.md` §1 |
| Pip | **`0.0001`** | `COMMON_PROTOCOL.md` §1 |
| Session day `D` | `[ D−1 17:00, D 17:00 )` — **Convention `C-1`**, `mmm_lib.session_day()`, unchanged | committed |
| `H_D`, `L_D` | max high / min low of all M1 bars in `D` | — |
| `C_D` | close of the **last** M1 bar in `D` | — |
| `d_hi` | `(H_D − C_D) / PIP`, in pips, **≥ 0 by construction** | — |
| `d_lo` | `(C_D − L_D) / PIP`, in pips, **≥ 0 by construction** | — |
| **Band** | `25 ≤ x ≤ 50` pips, **inclusive at both ends** | the claim's own numbers |

### §3a — THE ONE FILTER APPLIED

**Completeness.** A session day is included only if it is **complete** under the project's
existing rule (`mmm_lib` completeness machinery, as used by `PT-025`…`PT-032`). A partial session
cannot support a full-day high/low/close measurement — `D-036a`'s rule, and it applies whether the
cause is a data defect or a real holiday.

**Every excluded day is listed by date in the output.** No other filter is applied. **No day is
excluded for being large, small, newsy or "unrepresentative"** — that is `E09`.

**No exception is carved for the speaker's own qualifier *"depending on the pair"*.** It names no
pair and no adjustment; operationalising it would be inventing the claim's content. It is
recorded, not used. (`PT-036` §1 set this precedent on the same speaker's *"unless he's shifting
the zone"*.)

### §3b — BOTH `D-031` ARMS, BOTH REPORTED

Arm A and Arm B are run and **both are reported for every outcome and every control**, whatever
they show. The day boundary is a clock time, so this test is exactly the kind `D-031` binds.

---

## §4 — WINDOW AND DATA

| | |
|---|---|
| **Primary window** | **`W-B` = 2014-01-05 → 2015-12-31** (~520 weekdays). Chosen because this is a **daily** measure needing decision points, which is `COMMON_PROTOCOL.md` §3's stated use for `W-B` |
| **Pre-registered replication** | **`W-A` = 2015-01-04 → 2015-12-31**. Reported **every time**, and it is a replication, **not** a fallback: if `W-A` and `W-B` disagree, **both are reported and the verdict is taken from `W-B`**, which is fixed here |
| Scope | **DEVELOPMENT** (`D-035`), `mmm_lib.load_m1()`'s default. `assert_development()` runs. **No `D-044` year is read by this test** |
| QA gate | `qa_gate("development")` must pass `C1`–`C4` before any measurement (`COMMON_PROTOCOL.md` §1) |

⚠ **The `D-044` extension is deliberately not used.** It is available and this test does not need
it; reaching for more data on a question this narrow, before the pre-registered window has
answered it, is how a window becomes a choice.

---

## §5 — OUTCOME MEASURES

| ID | Measure | Reading |
|---|---|---|
| **`O1`** | fraction of complete days with **`min(d_hi, d_lo) ∈ [25, 50]`** | ⭐ **THE PRIMARY.** V15's literal *"or"* |
| **`O2`** | fraction with **`d_hi ∈ [25,50]` AND `d_lo ∈ [25,50]`** | V10's *"and"*, for comparability with `PT-036` `M2` |
| **`O3`** | fraction with **`max(d_hi, d_lo) ∈ [25,50]`** | the strictest single-sided reading; **descriptive only, changes no verdict** |
| **`D1`** | distributions of `d_hi`, `d_lo`, `d_hi + d_lo` (= the day range) and `min(d_hi,d_lo)`: n, median, IQR, deciles, and bootstrap CI on the median | descriptive |
| **`D2`** | the **five largest-range days** with their values, named | `COMMON_PROTOCOL.md` §3 disclosure 1, applied to days |

Wilson 95% intervals on every rate. Bootstrap 95% CI (2,000 resamples, seed fixed in the runner
and printed) on every median.

---

## §5a — CONTROLS — `D-026` / `D-029`, FIXED NOW

**`N1` — the random pseudo-close.** For each included day, draw a uniformly random M1 bar
**inside that same day** and use **its** close as a pseudo-close; recompute `O1`, `O2`, `O3`
against the **same** `H_D` and `L_D`. **2,000 iterations, seed fixed in the runner.** Report the
control's median rate and its 5th/95th percentiles.

> **This is the control that matters and it is the one that can kill the claim.** It holds the
> day's range fixed and varies only *where in the day the observation is taken*. If the real close
> is not distinguishable from an arbitrary minute, **the claim is a statement about GBP/USD's
> daily range distribution and not about the dealer placing the close**.

**`N2` — the day-boundary offset control.** Recompute `O1` with the session-day boundary shifted
by **−2h, −1h, +1h, +2h**. A result that survives only at exactly 17:00 is a boundary artifact.
**Reported; it does not by itself change the verdict** unless §6's clause (c) fires.

**`N3` — the band-width sanity check, DESCRIPTIVE ONLY.** Report `O1` for the bands
`[0,25]`, `[25,50]`, `[50,75]`, `[75,100]`, `[100,∞)`. ⚠ **This cannot change any verdict and must
never be used to propose a "better" band** — that would be fitting the claim to the data after
seeing it, which is `E09`/`E17`. It is here so the reader can see *where* the closes actually sit.

---

## §6 — DECISION RULE — FIXED NOW, BEFORE THE RUN

Applied to **`O1` in `W-B`, Arm A** as the headline; Arm B and `W-A` reported alongside.
`p̂` is the observed rate, `m` the `N1` control's median rate.

| Verdict | Condition |
|---|---|
| **SUPPORTED** | `p̂ ≥ 0.60` **AND** `p̂ − m ≥ +0.10` |
| **PARTIALLY SUPPORTED** | (`p̂ ≥ 0.40` **AND** `p̂ − m ≥ +0.10`) **OR** (`p̂ ≥ 0.60` **AND** `p̂ − m < +0.10`) |
| **NOT SUPPORTED** | `0.10 ≤ p̂ < 0.40`, **or** `p̂ ≥ 0.40` with `p̂ − m < +0.10` and `p̂ < 0.60` |
| **CONTRADICTED AS STATED** | `p̂ < 0.10` |

**Clause (a) — the word *"always"* is the speaker's and is scored against.** `p̂ < 0.10` against an
*"always"* is a contradiction, not a miss. This mirrors `PT-036`'s treatment of the same speaker's
same word.

**Clause (b) — `O2` is reported and verdicted on the identical thresholds**, and its verdict is
**secondary**. A divergence between `O1` and `O2` is itself the finding and is to be reported as
one.

**Clause (c) — the `N2` override.** If `O1` in `W-B` Arm A qualifies as SUPPORTED **but** at least
three of the four `N2` offsets return a rate within `±0.05` of it, the verdict is **downgraded one
step** and the reason printed. A "result" that is indifferent to the boundary is a fact about the
range distribution, not about the session.

**Clause (d) — no threshold in this section may be changed after the run.** A change is a new
`PT` number under `D-027`; this file is retained and marked.

---

## §7 — PREDICTIONS, COMMITTED BEFORE THE RUN

Scored honestly in the `BT` file, cheap ones tallied separately per the `BT_V10_0001` precedent.

| # | Prediction |
|---|---|
| **P1** | ⭐ **`O1` lands NOT SUPPORTED or CONTRADICTED.** Reasoning stated in advance: `BT_V10_0001` found GBP/USD's weekly range roughly 3× below the course's 600–1000 figure, so this speaker's pip scale appears calibrated to a wider-moving instrument than GBP/USD; a *daily* 25–50 band on a pair whose weekly range is ~300 pips implies a very tight daily close placement |
| **P2** | **`O2` is materially lower than `O1`** — necessarily so by construction, but the prediction is that the gap is **> 20 pp**, i.e. the *"and"* reading is far rarer than the *"or"* reading |
| **P3** | ⭐ **`O1` beats the `N1` control by LESS than +10 pp**, i.e. the close is not distinguishable from a random intraday minute on this measure |
| **P4** | **`N2` shows little sensitivity** — the four offsets sit within `±0.05` of the 17:00 result — which, combined with P3, would make the whole measure a statement about the range distribution |
| **P5** | **Arm A and Arm B differ negligibly on `O1`** (< 3 pp), because a whole-day high/low/close is far less clock-sensitive than a session-boundary measure |
| *P6* | *`D1`'s median day range is between 80 and 140 pips.* **Tallied as CHEAP** — it is a descriptive property of a corpus whose weekly range `BT_V10_0001` has already measured, and it is recorded only so that P1's reasoning is falsifiable |

---

## §8 — WHAT A RESULT HERE WOULD AND WOULD NOT MEAN

**A SUPPORTED result would mean:** on GBP/USD, in 2014–2015, the session close sat 25–50 pips from
the nearer daily extreme more often than an arbitrary intraday minute did. **It would NOT mean**
the dealer *places* it there, that this is tradeable, that it holds on other pairs, or that
V15's *"always"* is right — only that the band is not empty.

**A CONTRADICTED result would mean:** the figure does not describe GBP/USD in this window. **It
would NOT mean** the underlying idea (*the close returns into the range*) is false — only that
**this number** is. A separate, pre-registered test of *"they want to end back in the range"* as a
**relative** statement (e.g. the close's percentile within the day range) is the natural
follow-up and is **explicitly not run here**, because inventing it after seeing this result is
what `D-027` forbids.

**Either way it says nothing about `A-084`, `A-085`, `A-086`, `A-100` or `C-022`**, which are
blocked on evidence this corpus does not contain.

---

## §9 — LIMITATIONS DECLARED IN ADVANCE

1. **One instrument.** The claim says *"depending on the pair"* and this tests **GBP/USD only** —
   the pair the lesson's own chart shows (`V15_00-18-50_…png`, header `GBPUSD,H4`). A negative
   result is a result **about GBP/USD**, and the claim's own qualifier is a live defence.
2. **One window, 2014–2015, and a 2012 claim.** `COMMON_PROTOCOL.md` §3's regime caveat applies
   unchanged.
3. **Cross-vendor level caveat (`D-034`).** Price *levels* here are not comparable with the
   V02–V06 FXCM homework. This test uses **differences only**, so the caveat does not bite — stated
   so that is visible rather than assumed.
4. **The `2014-06-01` 22-hour hole (`D-036a`)** falls inside `W-B`. Any day it touches is excluded
   by §3a's completeness rule and **is named in the output**.
5. **`C-1` is a convention, not a finding.** `I-010` Q2 — which arm's clock the boundary is stated
   in — is an **open owner question**, and `N2` exists precisely because this test must not pretend
   otherwise.
6. **`n` is days, not independent events.** Consecutive days share regime; no independence
   correction is applied and the Wilson interval should be read with that in mind.
