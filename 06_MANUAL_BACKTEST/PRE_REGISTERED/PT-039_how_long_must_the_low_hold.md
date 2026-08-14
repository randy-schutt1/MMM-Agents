# PT-039 — V11's hold-duration claim: *"the low has to hold — how long? 30 to 90 minutes"*

> ## ⛔ `SUPERSEDED — NUMBERING` · RE-ISSUED AS `PT-039` BY OWNER RULING, 2026-08-13
>
> **This test was filed, committed, run and reported as `PT-037`.** It is re-issued here as
> **`PT-039`** and **nothing but the label has changed** — no threshold, prediction, null, window,
> sample, seed or decision rule is touched, and **the result is retained in full, not deleted**
> (`REMEDIATION_PROTOCOL.md` §2, and the exact contingency §0's disclosure block below named in
> advance).
>
> **The ruling, owner, 2026-08-13:** ***"Move V11 not V10 since V11 is after."***
>
> **This REVERSES the resolution §0 proposed**, and the reversal is the correct outcome. §0
> reasoned from the artifact (*a run test should not move; a prose reservation is free to*); the
> owner ruled on **precedence** (*V10 filed first, so V10 keeps the number*). **The V11 session
> flagged this as reviewer/owner-reversible in terms and was right to** — the disclosure is what
> made the ruling cheap, and the file is re-issued exactly as it said it would be.
>
> | | Number | Holder | Status |
> |---|---|---|---|
> | **This file** | `PT-037` → **`PT-039`** | V11 — hold-duration | ⛔ **MOVED** (re-issued) |
> | V10's path-length reading of `M1` | **`PT-037`** | V10 | ✅ **UNCHANGED — keeps the number it reserved** |
> | V10's safety trade | **`PT-038`** | V10 | ✅ **UNCHANGED** |
> | *(`PT-040`)* | — | — | **NOT ALLOCATED.** See below |
>
> ### ⚠ `PT-040` WAS NOT NEEDED, AND A SESSION EXPECTING IT WILL BE CONFUSED
>
> The reversal was framed as *"V11 moves to `PT-039`/`PT-040`"*, on the reading that V11 held both
> numbers. **It did not.** V11 filed **exactly one** pre-registration — this one, at `PT-037`.
> Every `PT-038` reference anywhere in V11's artifacts is a reference to **V10's** safety-trade
> reservation, which stays at `PT-038` and was never V11's to move. **`PT-039` is therefore the
> only renumbering, and `PT-040` remains free and unallocated.**
>
> **Artifacts renamed with this file** (git-tracked renames, content unchanged):
> `06_MANUAL_BACKTEST/scripts/run_pt037.py` → `run_pt039.py`;
> `06_MANUAL_BACKTEST/V11/data/pt037_output.txt` → `pt039_output.txt`.
>
> **No stub is left at the old path, deliberately.** Leaving a `PT-037` placeholder here would
> squat the number the owner has just ruled belongs to V10 — the opposite of the ruling. Nothing
> is lost: the renames are tracked, the full pre-run history is below, and the commits that
> established the pre-registration ordering are named in §0 and unaltered.
>
> ### ⭐ THE COMMIT-TIMESTAMP ORDERING IS UNAFFECTED — read this before doubting the run
>
> `D-026`/`D-027` verification rests on **commit order**, not on the filename. The ordering that
> matters was established under the old number and is **unchanged and still auditable**:
> pre-registration `beee96a` → runner `6da82b3` → output `4d2bdcd` → scoring `735a458`. **This
> re-issue is a LATER commit than all four**, so it cannot and does not backdate anything. A
> reviewer verifying the ordering should follow those four hashes; `git log --follow` on the new
> paths reaches them through the renames.

```text
STATUS:   PRE-REGISTERED. NOT RUN.
DATE:     2026-08-13
LESSON:   V11 -- Bootcamp1 Wk4 040812 Part1 (51mins).swf
          SHA-256 606cc5a89a0a68aa08c18423342288307d267b65ebb79acd889e48af8c4d2101
SPEAKER:  the COURSE AUTHOR, 100% of runtime (D-033 makes this immaterial to
          weight; recorded because provenance is owed). Established by four
          non-acoustic strands in V11_TRANSCRIPT.md; acoustic comparison NOT
          run, per V07's ruling.

THIS FILE IS COMMITTED BEFORE THE RUNNER EXISTS AND BEFORE ANY BAR IS READ.
No price, statistic, count or distribution from W-C' has been examined by the
session writing it. The predictions in 6a are committed in THIS commit; the
runner is a SEPARATE, LATER commit, and its output later still (D-026, D-027,
BACKTEST_EVIDENCE_STANDARD.md; the PT-035 / PT-036 precedent). Commit-timestamp
ordering is the verification.
```

## 0. NUMBERING

`PT-037` is the next free number: `PT-001` … `PT-036` exist, `PT-036` being V10's. Allocated
against the **integration branch** state (`a004e88`), per `D-038a` consequence 1, and re-checked at
merge-back.

> ### ⚠ APPENDED AFTER THE RUN — A NUMBERING COLLISION, DISCLOSED
>
> **The paragraph above is WRONG in one respect and is retained unedited** per
> `REMEDIATION_PROTOCOL.md` §2. `PT-037` was the next free **FILE** number, and it was not the next
> free **RESERVED** number.
>
> **`BT_V10_0001.md` §9, `REVIEW_INDEX.md` open item 86 and `LOG.md` had already reserved
> `PT-037`** for a different successor — *the path-length reading of V10's 600–1000-pip weekly-range
> claim* — and **`PT-038`** for *the safety trade*. Both are **prose reservations with no file**;
> `06_MANUAL_BACKTEST/PRE_REGISTERED/` contained neither when this file was written. §0's search was
> for existing files and it missed them. **This is exactly the concurrent-allocation hazard
> `D-038a` consequence 1 names, and it was found by the check that consequence requires** — just
> later than it should have been.
>
> **RESOLUTION, and it is proposed rather than imposed:**
>
> - **This file KEEPS the number `PT-037`.** It is a **committed, run** pre-registration whose
>   number appears in four commits, the runner, the output file and `BT_V11_0001`. Renumbering a
>   pre-registration after its run is the one move `D-027`'s retention rule exists to prevent.
> - **V10's two reservations move forward to `PT-039` (path-length) and `PT-040` (safety trade).**
>   A reservation with no file is free to move; a run test is not.
> - **`BT_V10_0001.md` and `V10_REVIEW_R1.md` are NOT edited.** They are a completed observation and
>   a completed review, and `REVIEW_PROTOCOL.md` §11 forbids overwriting the latter. The
>   re-designation is recorded in `REVIEW_INDEX.md` (an evidence ledger) and here.
> - **Carried to the reviewer as an open item.** If the owner or reviewer prefers the opposite
>   assignment, this file is marked `SUPERSEDED — NUMBERING` and re-issued, and its result is
>   retained, not deleted.
>
> **NOTHING IN §§1–9 CHANGES.** No threshold, prediction, null, window, or decision rule is
> touched by this block; the number is a label and the design is untouched.
>
> > ### ⛔ THE PROPOSED RESOLUTION ABOVE WAS **REVERSED** BY THE OWNER, 2026-08-13
> >
> > ***"Move V11 not V10 since V11 is after."*** **This file moved to `PT-039`; V10 keeps `PT-037`
> > and `PT-038`.** Everything in this §0 — including the proposal it makes and the paragraph it
> > corrects — is **retained unedited as the history of the collision**, per
> > `REMEDIATION_PROTOCOL.md` §2. It is a record of what was proposed, **not** a statement of the
> > current numbering. **The governing block is at the top of this file.**
> >
> > **The disclosure did its job.** This session named the reversal, specified the exact remedy
> > (`SUPERSEDED — NUMBERING`, re-issue, retain the result), and got the ruling because it asked.
> > That is the argument for self-disclosing a numbering error rather than quietly keeping the
> > number — and §§1–9 still change by nothing at all.

---

## 1. THE CLAIM UNDER TEST

> **V11 `[00:14:25]`–`[00:14:39]`** — *"Understand that **the low has to hold. How long? 30 to 90
> minutes.** 30 minutes is for **[railroad] tracks**, but the **long sideways consolidation should
> last up to two hours. Then calmly take a trade.**"*

**Two engines agree on this passage.** The committed transcript body reads *"rarer tracks"*; an
independent Whisper `small.en` pass returns *"railroad tracks"* and reproduces **every number**
(`V11_TRANSCRIPT.md` § SPOT-CHECK RESULTS, clip `c2`). The body is not edited
(`REMEDIATION_PROTOCOL.md` §2); the correction is cited.

**The context is what makes the claim a claim.** `[00:14:02]`–`[00:14:25]`:

> *"you guys are seeing a move out of the box, you're grabbing the trade **anticipating that's
> gonna be the low** because it's one candle; the dealer goes into consolidation, hits it again;
> you're like, oh well that wasn't [the low], **this ought to be the low**, you grab it again…"*

So the claim is a **confirmation requirement on a CANDIDATE low**: a low you think is the low is
not yet the low, and **elapsed time is the thing that tells you.** Three numbers are attached —
**30**, **90**, and **120** minutes — and a fourth object, *"railroad tracks"*, is attached to the
short case.

### 1a. `E03` — the qualifiers, carried rather than dropped

- **The 30-minute case is CONDITIONAL**, not a floor: *"30 minutes is for [railroad] tracks."*
  **`railroad tracks` is an undefined candlestick pattern in this corpus** — it occurs nowhere else
  in V01–V11 — so the condition **cannot be operationalised**. It is therefore **NOT used to
  exclude anything**, and the 30-minute threshold is tested **unconditionally**, which is the
  reading most favourable to the claim. Recorded here so a later session cannot invoke the
  condition retroactively to rescue a failed 30-minute result — that would be `E09`.
- **The two-hour figure is a CEILING on a different object** — *"the long sideways consolidation
  should last **up to** two hours"* — not a fourth point on the same scale. It is tested as a
  threshold anyway, and **labelled as the agent's extension of the claim**, not as the
  instructor's.
- *"Then calmly take a trade"* attaches an **action** to the confirmation. **No trade is simulated
  here** — see §2.

---

## 2. WHAT THIS TEST DELIBERATELY DOES **NOT** TEST, AND WHY

### 2a. It does not test V11's entry rule. Most of V11 is untestable today.

`V11_INTERPRETATION.md` Q4 enumerates it. **The lesson's normative core —** *"25 to 50 pips out of
the box, second leg W formation … inside the TDI … the double band"* `[00:07:52]` **— needs four
undefined terms in one sentence**: `blue box` (`A-076`), `second leg` (`A-007`), *"the formation"*
(`A-011`), and an **RSI period** (`A-080`). `D-030` forbids approximating any of them.

### 2b. ⭐ It does not test ANY RSI threshold, and that is the largest omission

V11's most codable-looking content is its six printed RSI parameters — `0–100`, `70/30`, `80/40`,
`60/20`, `80/20`, mid-point `50`. **Not one of them is tested here**, because the slide headed
*"Parameters of RSI"* **does not contain the lookback period**, Tier 1 is silent on it, and Tier 2
(`MMM-NOTES`) is silent on it too (`A-080`, `D-040`).

**The TDI default of 13 is refused explicitly.** Adopting it would produce a *number* for every
threshold in the lesson, attributed to the instructor, whose caveat would not survive being quoted
twice (`E06` + `E18`).

**Not testing them is itself the finding**, and it is reported in `BT_V11_0001` §1 and in the
mastery report's dimension G **with equal prominence to anything that is measured**
(`BACKTEST_EVIDENCE_STANDARD.md` §4.3, `E25`).

### 2c. It simulates no trade, so it has no stop, no target, and no barrier race

`PT-039` estimates **a conditional probability about a price extreme**, not a hit rate. It follows
`PT-036`'s design property, deliberately:

| Property of `REVIEW_INDEX.md` open item **80**'s censoring bias | `PT-039` |
|---|---|
| Requires a **barrier race** (target vs stop) | **No barrier of any kind** |
| Requires an **asymmetric horizon** that can expire | **A horizon exists** — the session close — and it is **symmetric between the two outcomes**, because both *"superseded"* and *"final"* are decided by the same 17:00 boundary |
| Produces **unresolved** observations | **Zero possible.** Every candidate is either superseded within its session day or it is not. `n_unresolved == 0` by construction, **and the runner asserts it** |

> ### ⚠ BUT `PT-039` HAS ITS OWN, DIFFERENT BIAS, AND IT IS DESIGNED FOR RATHER THAN AWAY
>
> **A low made at 16:30 is nearly certain to be the day's final low, on arithmetic alone** — there
> are 30 minutes left for anything to break it. So `P(final | held ≥ T)` will rise with `T`
> **whether or not the instructor's claim carries any information**, because surviving longer
> correlates mechanically with being later in the session.
>
> **This is the confound that would manufacture a spurious CONFIRMATION**, and it is the single
> most important thing about this design. It is handled in three ways, all fixed here:
>
> 1. **The eligibility rule (§3.1) removes the arithmetic impossibility**: a candidate enters the
>    denominator for threshold `T` only if **at least `T` minutes of session remain** when it is
>    created. Without this, the estimate is contaminated by candidates that *could not* have been
>    observed to hold that long.
> 2. **`N3` stratifies the whole curve by time-of-day** and reports median remaining-session-time
>    per stratum. **`M1d`'s verdict is taken from `N3`, not from the pooled number.**
> 3. **`N2` runs unnamed thresholds alongside the named ones**, so a smooth mechanical rise is
>    distinguishable from a feature at 30 / 90 / 120.

---

## 3. THE PRE-REGISTERED CONSTRUCTION

### 3.0 Objects

| Object | Definition, fixed here |
|---|---|
| **Session day `D`** | `COMMON_PROTOCOL` convention **C-1**: `[ D-1 17:00, D 17:00 )` on the arm's own clock. `mmm_lib.session_day` |
| **Bar series** | **M1**, direct from the `D-036a` corpus. **Not M15** — the claim is about 30/90/120-minute durations and M15 would quantise every measurement to 15 minutes, which is 50% of the smallest threshold |
| **Candidate low** | An M1 bar whose `low` is **strictly below** the running minimum of the session day so far. The session's first bar creates the first candidate |
| **Superseded** | The first later M1 bar in the same session day with a **strictly lower** low |
| **Hold duration `Δ`** | Minutes from the candidate bar's timestamp to its superseding bar's timestamp. For a candidate never superseded, `Δ` is **right-truncated** at the session close and is **not used as a duration** — only as *"never superseded"* |
| **`FINAL`** | A candidate never superseded within its session day. **Exactly one per session day** |
| **Remaining session time `R`** | Minutes from the candidate bar to the session day's 17:00 close |
| **HIGH arm** | The exact mirror: running maximum, strictly higher high. He names both — `[00:07:23]` *"the second attempt towards **the low of the day, or the high**"* |

**`FINAL` is knowable only at session close. That is not lookahead** — it is the *outcome variable*.
The *predictor* (`Δ ≥ T`) is knowable in real time at `t_candidate + T`. **Nothing in the
conditioning set uses information from after the moment the prediction would be made**, and the
runner asserts this by construction.

### 3.1 ⭐ THE ELIGIBILITY RULE — the design's load-bearing choice

**For threshold `T`, a candidate enters the denominator if and only if `R ≥ T`.**

Then, within that set:

```text
held(T)  :=  (superseded and Δ >= T)  OR  (never superseded)
O1(T)    :=  P( FINAL | held(T) )
n(T)     :=  #{ candidates with R >= T and held(T) }
```

**Why this and not the naive version.** Without the rule, a candidate created at 16:50 is counted
in the `T = 30` denominator and can never satisfy `held(30)` by superseding — it can only satisfy
it by being final. That is not a test of the claim; it is a test of the clock. **The rule is
stated before any number exists and may not be changed afterwards.**

**The cost is disclosed:** `n(T)` shrinks as `T` grows, and the `T = 240` cell will be the
smallest. **Every cell reports its own `n`** and any cell below 30 carries
`SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` (`E24`,
`BACKTEST_EVIDENCE_STANDARD.md` §4.1).

### 3.2 The observables

| # | Observable |
|---|---|
| **`O1`** | The **survival-confirmation curve**: `P(FINAL \| held ≥ T)` for `T ∈ {5, 10, 15, 30, 45, 60, 90, 120, 180, 240}` minutes, with Wilson 95% CIs and `n(T)`. **Both arms (low and high). Both `D-031` clocks.** |
| **`O2`** | The **named thresholds** in isolation — `T = 30`, `T = 90`, `T = 120` — and the two increments the claim implies: `P(90) − P(30)` and `P(120) − P(90)` |
| **`O3`** | The **hold-duration distribution of SUPERSEDED candidates**: n, median, quartiles, 5th/95th percentiles, and **the proportion falling in `[30, 90]`**. This answers *"is 30–90 minutes even where the action is?"* directly and without any conditioning |
| **`O4`** | **Candidates per session day** — distribution of the count of new session-day lows (and highs). This fixes the base rate: with `k` candidates, the unconditional `P(FINAL)` is `1/k` |
| **`O5`** | **The named numbers' percentile position** in `O3`'s distribution. If 30 minutes is the 85th percentile of hold durations, then *"held 30 minutes"* is a rare event and a strong filter; if it is the 20th, it is nearly free |

### 3.3 Reported but explicitly NOT the instructor's

| # | Observable | Label |
|---|---|---|
| **`O6`** | The `T = 120` cell | **AGENT'S EXTENSION.** The lesson gives two hours as a **ceiling on a sideways consolidation**, not as a confirmation threshold (§1a). Reported in its own row, and **`M1a`/`M1b`'s verdicts do not use it** |

---

## 4. THE NULLS — `D-026`, `D-029`

`D-026`'s named default is **matched random entry**, which is the correct control for **a rule that
takes trades**. **`PT-039` takes no trades**, so a random-entry baseline would control for a
quantity this test does not estimate. The matched controls for a **conditional-probability claim**
are used instead, following the `PT-028` / `PT-036` precedent in this corpus.

**Stated plainly so it is not read as an evasion: the nulls are listed HERE, IN ADVANCE, and each
is a genuine comparator the claim can fail against.**

### `N1` — the unconditional base rate

`P(FINAL)` over all candidates in the same eligible set, i.e. `O1(T = 0)`. **This is the
comparator `M1a` is scored against.** The claim is that *duration adds information*; `N1` is what
you know without it. Equivalently `1 / E[candidates per day]`, cross-checked against `O4`.

### `N2` — the unnamed-threshold control ⭐

`O1` is computed at **five thresholds the lesson never names** — `5, 10, 15, 45, 240` — alongside
the four it does. **This is the null that decides `M1c`.** If the curve is smooth and monotone
through 30, 90 and 120 with no feature distinguishable from the unnamed points, then the claim's
numbers are **not measuring anything about those numbers**; they are measuring *"later is later"*.

**Feature test, fixed now:** a named threshold `T*` shows a *feature* if the increment in
`P(FINAL)` across the interval ending at `T*` exceeds the **mean increment per minute of the two
adjacent unnamed intervals** by **≥ 5 percentage points, scaled to interval width**. Anything less
is reported as **no feature**.

### `N3` — the time-of-day stratification ⭐ (the confound control)

`O1` recomputed within **six 4-hour strata** of the candidate's minute-of-day on the arm's own
clock, each reporting **`n` and median `R`**. **`M1d`'s verdict is taken from here.**

If the effect is a real property of *hold duration*, it survives inside a stratum where remaining
session time is roughly constant. **If it exists only in the pooled figure, it is the clock.**

### `N4` — circular clock shift

`COMMON_PROTOCOL.md` §5's `N2` control, via `mmm_lib.n2_offsets`: the entire price path is held and
every session/day label is shifted by an offset drawn uniformly from ±12 h in 15-minute steps,
**1,000 iterations**. Answers whether the 17:00 session boundary matters at all to this result, or
whether any 24-hour window gives the same curve.

**Seed for every bootstrap, shuffle and shift: `20260813`. Iterations: 1,000 (`D-029`).**
Recorded here, before the run.

---

## 5. CELLS — TWO `D-031` ARMS, BOTH ALWAYS REPORTED

| Arm | Clock | Session day |
|---|---|---|
| **A** | corpus stamps verbatim, fixed UTC−5, no DST | `[ D-1 17:00, D 17:00 )` on file stamps |
| **B** | `America/New_York`, DST active (stamp +1 h in US DST) | same physical boundary relabelled during DST |

**`D-031`'s binding rule: BOTH arms are reported for every observable, every time. Divergence is a
finding; reporting only the better arm is `E09` + `E24`.**

**Predicted in advance so a near-identity is not later sold as robustness:** the two arms differ
only in *which physical instant* the 17:00 boundary falls on during US DST. That **does** move
session-day membership for bars near the boundary and **does** change `R` for every candidate by
up to an hour, so unlike `PT-036`'s `M1` the arms here are **not** structurally identical. **A
difference is expected; its size is not predicted.**

---

## 6. THE DECISION RULE — FIXED NOW, BEFORE ANY NUMBER EXISTS

| Measure | `CONFIRMED AS STATED` | `PARTIALLY SUPPORTED` | `CONTRADICTED AS STATED` |
|---|---|---|---|
| **`M1a`** — does duration carry information? `P(FINAL \| held ≥ 30) − N1` | **≥ 20 pp** | 5–20 pp | **< 5 pp** |
| **`M1b`** — does the 30→90 band do work? `P(90) − P(30)` | **≥ 10 pp** | 3–10 pp | **< 3 pp** |
| **`M1c`** — are the NAMED numbers special? (`N2`) | a feature at **30 AND 90** | a feature at one | **no feature at either: the curve is smooth** |
| **`M1d`** — does it survive the confound? (`N3`) | `M1a`'s margin holds (**≥ 20 pp**) in **every** stratum with `n ≥ 30` | holds in **some** strata | **holds in none / vanishes once `R` is controlled** |

**`M1a` is the weakest test and is labelled as such here rather than after the fact.** A low that
has survived 30 minutes being more likely final than a random new low is close to arithmetically
guaranteed. **`M1c` and `M1d` are where the claim can actually fail**, and the headline verdict in
`BT_V11_0001` is taken from **all four**, with `M1c`/`M1d` weighted as the substantive ones. A
result of *"`M1a` confirmed, `M1c` and `M1d` contradicted"* is to be reported as **the claim's
NUMBERS being unsupported while its DIRECTION is trivially true** — not as a confirmation.

**Thresholds are fixed here and may not be moved after the numbers are seen.** Moving one is `E09`.

### 6a. THIS SESSION'S PREDICTIONS, COMMITTED BEFORE THE RUN

Written before any bar of `W-C′` was read by this session, and committed in this file.

| # | Prediction | Confidence | Reasoning |
|---|---|---|---|
| **P1** | **`M1a` is CONFIRMED** — `P(FINAL \| held ≥ 30) − N1 ≥ 20 pp` | **High** | Near-mechanical. Flagged as a **cheap** prediction (see below) |
| **P2** | **`M1c` is CONTRADICTED** — the curve is smooth, **no feature at 30 or at 90** | **Medium-high** | I know of no mechanism that would put a kink in a survival curve at exactly 30 or 90 minutes on a 24-hour FX session. This is the prediction I most want to be wrong about, because a feature would be a genuine discovery |
| **P3** | **`M1d` is PARTIALLY SUPPORTED** — the margin survives in the **early and middle** strata and **collapses in the last (13:00–17:00)** stratum, where `R` is small | **Medium** | The confound bites hardest where remaining time is shortest |
| **P4** | **`M1b` is CONTRADICTED** — `P(90) − P(30) < 3 pp` | **Medium** | If the curve is smooth (P2) and already high at 30, there is little headroom left by 90 |
| **P5** | `O3`'s **median superseded-hold duration is under 30 minutes**, and **fewer than 25%** of superseded holds fall in `[30, 90]` | **Medium** | A numeric forecast, stated so it can be plainly wrong. If most supersessions happen within minutes, the instructor's band sits in the tail |
| **P6** | `O4`'s **median candidate-low count per session day is between 4 and 9** | **Low-medium** | The prediction I am least confident in and the easiest to falsify |
| **P7** | The two `D-031` arms differ by **< 5 pp** at every named threshold | **Medium** | Cheaper than it looks but not structural — see §5 |
| **P8** | The **HIGH arm and LOW arm agree within 5 pp** at every named threshold | **Medium-high** | Symmetry; a large asymmetry would itself be a finding worth chasing |

> **P1 is flagged as cheap ON PURPOSE.** A prediction tally that banks a near-certainty alongside
> genuine forecasts inflates itself. `BT_V11_0001` reports **P1 separately from P2–P8**, and the
> headline prediction score is taken from P2–P8.

---

## 7. WINDOW, HOLDOUT, DATA — `D-027`, `D-028`, `D-035`, `D-036a`

| Field | Value |
|---|---|
| Instrument | **GBP/USD** (`D-007`) |
| Window | **`W-C′` = 2013-01-06 → 2016-06-30** — `D-035`'s DEVELOPMENT block **exactly** |
| Holdout | **2016-07-01 → 2017-12-29 — NOT OPENED.** Cannot be: it is not on disk (`D-036a` truncated it on arrival). `mmm_lib.assert_development` re-checks every slice |
| Timeframe | **M1**, direct from the corpus — **not** aggregated |
| Source | **HistData.com M1 CSV corpus** (`D-036a`), SHA-256 in `raw/SHA256SUMS.txt` |
| Timezone | Corpus is **fixed UTC−5, no DST** — natively `D-031` Arm A. Arm B = stamp +1 h during US DST |
| Week open | Sunday 17:00 local = **22:00 UTC** — HistData's, **NOT** FXCM's 21:00 UTC. *(Carried for completeness; **`PT-039` is a DAY-boundary test, not a week-boundary test**, so nothing here inherits the week open.)* |
| QA gate | `qa_histdata_m1.py` → `QA_REPORT.txt` is a **precondition on the run** and is cited in `BT_V11_0001` |
| Level comparability | **Price LEVELS are not comparable with the V02–V06 FXCM homework** (`D-036a`). **`PT-039` reads no price level at all** — only orderings (*is this low below that low*) and clock differences. **This test is structurally immune to the limitation**, and that is stated because it is the rare case where it does not bite |

### 7a. INCLUSION AND `C8` DISPOSITIONS — PRE-REGISTERED BY NAME

**Session-day inclusion rule (the general form of `COMMON_PROTOCOL` convention `C-6`):** a session
day is included only if **all 96 fifteen-minute buckets of its 24-hour span are present** in the
corpus. **Exclusions are COUNTED AND REPORTED beside every `n`, never dropped quietly.**

**Why the rule is at the bucket and not the minute:** a bid feed legitimately prints no tick in a
quiet minute, and requiring 100% M1 coverage would exclude most of the corpus for a non-defect.
**But a missing 15-minute bucket directly and silently INFLATES a hold duration**, which is this
test's measured quantity — so the rule is applied to the exact resolution the measurement is
sensitive to.

| Session / week | Disposition | Reason |
|---|---|---|
| **2014-06-01 → 2014-06-02** (the ~22 h data hole, `D-036a` `C8`) | **EXCLUDE by name** | The corpus does not contain what the market did. **A data-integrity exclusion, not an `E09` convenience one** — the distinction `C8` exists to make, and it bites hardest on a *duration* test |
| The six Dec/Jan closure weeks flagged by `C8` | **INCLUDE where the 96-bucket rule passes; EXCLUDED BY THAT RULE where it does not** | Holiday closures are **real market behaviour** and `COMMON_PROTOCOL.md` §3 disclosure 1 forbids dropping them as unrepresentative. They are removed here **only** by the completeness rule, applied identically to every day, and the count is reported |
| Saturday and Sunday session days | **STRUCTURALLY ABSENT** | `[Fri 17:00, Sat 17:00)` and `[Sat 17:00, Sun 17:00)` contain no bars. Not an exclusion; there is nothing there |

**Expected `n` before the run**, from calendar arithmetic only, **no price read**: `W-C′` spans
1,272 days ≈ **180 trading weeks** (`D-037`), so **≈ 900 session days** before completeness
exclusions. **The realised numbers are reported as realised**, not rounded to this.

### 7b. WHAT WOULD MAKE THIS TEST VOID

Stated in advance so it cannot be negotiated afterwards:

1. **Any unresolved observation.** §2c asserts the design admits none. If the runner reports
   `n_unresolved > 0`, the design claim is false and the test is **VOID**, not merely weakened.
2. **More or fewer than exactly one `FINAL` candidate per included session day.** Asserted.
3. **Any bar outside `W-C′`.** `assert_development` fires per slice.
4. **A `QA_REPORT.txt` that does not gate clean on C1–C4.**
5. **Any candidate entering a denominator with `R < T`.** §3.1's rule is the design; a violation
   voids `O1`.
6. **Fewer than 30 observations** in any cell whose rate is quoted **without** the
   `SAMPLE INSUFFICIENT FOR INFERENCE — descriptive only` label (`E24`).

---

## 8. MANDATORY SCOPE STATEMENT

**What a result here does and does not license** — the `PT-001` §7 form.

- The speaker is the **course author**. Under `D-033` his material is normative; **no speaker-based
  fence applies.**
- ⭐ **THE OPERATIONALISATION IS A NARROWING, AND IT IS DISCLOSED BEFORE THE RESULT.** The
  instructor's *"the low"* is a candidate low **made after a stop hunt, out of the blue box**.
  `A-076` blocks that filter, so **`PT-039` tests EVERY running session-day low instead.**
  Consequently:
  - **A CONTRADICTION here does NOT show the instructor's rule fails.** It shows that *hold
    duration alone*, on *unfiltered* candidate lows, carries no information at the numbers he
    names. His filtered version is untested and remains so.
  - **A CONFIRMATION here does NOT validate his setup.** It would show duration is informative in
    general, which is weaker than, and does not imply, his conditional claim.
- **`FINAL` means *final within the session day*, on the `C-1` 17:00 boundary.** It is not
  *"the low of the move"* and not *"the weekly low"*.
- **Results are GBP/USD-specific** (`D-007`). Nothing here transfers to another pair.
- **The window is 2013–2016; the lesson was recorded 2012-04-08.** The corpus does not reach 2012
  at any usable resolution. **A real external-validity limit, stated before the result.**
- **No RSI threshold, no entry rule, no stop, no target and no position size is tested** (§2).
  Whatever this test returns, **it says nothing about whether the method is profitable.**

---

## 9. TO RUN THIS

```bash
python3 06_MANUAL_BACKTEST/scripts/run_pt039.py \
  > 06_MANUAL_BACKTEST/V11/data/pt039_output.txt
```

The runner is committed **separately and after this file**, and its output after that.
`COMMON_PROTOCOL.md` §9 rule 7 applies: **if the runner and this pre-registration disagree, the
pre-registration governs and neither is edited** — the disagreement is reported in
`BT_V11_0001.md`. That rule has already fired **three** times in this project (`BT_V08_0001`,
`BT_V09_0001`, and once in the `D-037` re-issue batch), **every time against the runner.**
