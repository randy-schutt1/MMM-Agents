# V19 — INDEPENDENT REVIEW, ROUND 1

**Lesson:** `Bootcamp1 Wk9 052012 Part1 (67mins).swf` — Week 9 Part 1, 2012-05-20
**Printed subject:** `MARKET MAKER TRAP MOVE(S)` — `Trap Candle Patterns` / `Dealer Structures` /
`Behavioral Analysis`
**Branch reviewed:** `video/v19` @ `854d402` (7 commits, forked from `847ebd2`)
**Review branch / worktree:** `review/v19` in `/Users/randyschutt/Desktop/Trading/MMM-Agents-review-v19`
**Reviewer session:** independent, per `DECISIONS.md` `D-003`. This session authored no V19 student
artifact and did not participate in the ingestion.
**Date:** 2026-08-14

---

## FINAL DECISION

> ## **REVISE** — **0 CRITICAL / 1 MAJOR / 3 MINOR / 18 NOTE**
>
> **CONFIDENCE: HIGH.**
>
> ⛔ **THE `V20` GATE STAYS CLOSED.** `D-024` keys the gate to finding severity, not to the verdict
> word, and **one `MAJOR` holds it closed until fixed and re-reviewed.**
>
> **The single `MAJOR` is a REPORTING failure, not a data, method or integrity failure.** `PT-047`
> is the best-executed test in this corpus to date — pre-registered before its runner existed,
> reproducing **byte-identically** on re-run, reproducing **exactly** on independently written code,
> and surviving four robustness probes this reviewer invented after the fact. **What it does not do
> is report a single confidence interval anywhere**, while classifying itself `EVIDENTIAL`, which
> `BACKTEST_EVIDENCE_STANDARD.md` §5 defines as requiring one. **With the intervals computed, both
> legs of the `CONFIRMED` gate sit inside the 95 % interval of failing** — see `M1`.

⚠️ **The verdict `CONFIRMED` is NOT asked to change, and must not be.** The decision rule was
pre-registered on point estimates and re-opening it after seeing intervals would be exactly the
performance-chasing `REVIEW_PROTOCOL.md` §17.5 prohibits, run backwards. **The requirement is to
report the intervals and to qualify every downstream citation of the magnitude claim.**

---

## §1 — SOURCE MATERIAL REVIEWED, BEFORE ANY STUDENT CONCLUSION

`REVIEW_PROTOCOL.md` §3 order was followed. Source first, in this order:

| Source | What was done | Result |
|---|---|---|
| The `.swf` itself | SHA-256 re-computed independently | ⭐ **`7e8a1c2b…5c1ab28e` — matches `SOURCE_MANIFEST.md` exactly**; 25,694,598 bytes, also matching |
| Its audio | Extracted independently with `ffmpeg`, duration measured | **4042.005 s = 01:07:22.0** |
| **12 pre-registered ASR segments** | The **five** genuinely outstanding ones re-run by this reviewer on `whisper medium.en` | ⭐ **All five returned. Every one corroborates the student's reading; none overturns anything** — see `N7` |
| 3 further probe segments | Cut and transcribed to test `Q-020`'s load-bearing quotes | ⭐ **All three verbatim** — see `N8` |
| The committed transcript | Load-bearing markers read in the body, not in the summary | Every quote cited by `PT-047`, the mastery report and the interpretation **verifies in the body** |
| **6 deck frames** | Read as pixels, burned timecodes compared with filenames | ⭐ **Every one as described** — see `N5`, `N6` |
| The 3 quarantined `Q-020` files, ×7 lessons | SHA-256, byte length and `diff` re-run | ⭐ **Exact match to `Q-020` §0, including the enumeration** — see `N4` |

**No student conclusion was read until the source pass was complete.**

---

## §2 — WHAT WAS RE-DERIVED RATHER THAN READ

### 2.1 ⭐ `PT-047` reproduces byte-identically, and again on independently written code

`run_pt047.py` and `posthoc047.py` were re-run in a **clean worktree** with the git-ignored corpus
wired in. `pt047_results.json` came back **byte-identical to the committed file** (`git status`
clean), and `pt047_posthoc_disjoint.txt` matched line for line.

Then `06_MANUAL_BACKTEST/scripts/rev_pt047_independent.py` was written **from `PT-047` §3–§5 alone**
— vectorised event scan instead of a loop, classifier expressed as a close-count, **a different
permutation seed** (`77190419`), and a rank test the student's runner does not contain.

| cell | student `n_H`/`n_B` | reviewer `n_H`/`n_B` | student Δ | reviewer Δ |
|---|---|---|---|---|
| `A｜W-A｜30m` **(primary)** | 39 / 60 | **39 / 60** | +25.75 | **+25.75** |
| `A｜W-A｜45m` | 34 / 65 | **34 / 65** | +26.90 | **+26.90** |
| `A｜W-B｜30m` | 69 / 137 | **69 / 137** | +19.20 | **+19.20** |
| `A｜W-B｜45m` | 60 / 146 | **60 / 146** | +19.20 | **+19.20** |
| `B｜W-A｜30m` | 36 / 62 | **36 / 62** | +20.35 | **+20.35** |
| `B｜W-A｜45m` | 31 / 67 | **31 / 67** | +25.10 | **+25.10** |
| `B｜W-B｜30m` | 73 / 134 | **73 / 134** | +16.65 | **+16.65** |
| `B｜W-B｜45m` | 61 / 146 | **61 / 146** | +20.55 | **+20.55** |

**Every count, every median and every Δ reproduces exactly on code that shares no line with the
runner.** `p` differs only in the fourth decimal, which is the different seed doing its job.
**Day accounting also reproduces: 256 days included / 2 excluded on `W-A`, 512 / 3 on `W-B`.**

### 2.2 The four probes `PT-047` §6 asked for, or item 290 did

| Probe | Result |
|---|---|
| **P1 — the 60-minute arm** (item 290 asks for it by name) | ⭐ **The `n < 30` guard WOULD fire**: `A｜W-A｜60m` `n_H = 29`, `B｜W-A｜60m` `n_H = 27`. ⚠ **But Δ GROWS to +29.45 (`p` = 0.0003)** — see `N2` |
| **P2 — `MAX_AGE` sensitivity** (§6 attack 2) | ⭐ **Not load-bearing.** Δ runs 25.75–36.80 across `max_age` 12→∞, every `p ≤ 0.0005`. **Removing the bound entirely gives Δ = +27.50** — the convention is if anything conservative |
| **P3 — every event per day** (§6 attack 3) | ⭐ **Holds.** `A｜W-A` Δ = +26.05, `p` = 0.0002 on `n_H` = 50 / `n_B` = 71. The first-event rule is not producing the result |
| **P4 — Mann-Whitney U on `O1`** | ⭐ `U` = 1725, `z` = 3.975, **two-sided `p` = 7.0 × 10⁻⁵.** The separation is **distributional**, not an artifact of the median |

**Every attack `PT-047` §6 named against itself was run, and the test survived all of them.**

### 2.3 Everything else that was re-run

* `hw_v19.py` — reproduces **byte-identically** (`git status` clean on `05_HOMEWORK/`).
* `scripts/validate_project.py` — **103 passed / 0 warnings / 0 failures**, matching the commit claim.
* `Q-020` §0's SHA-256s, byte lengths, diff matrix and diff enumeration — **all exact** (`N4`).
* The `A-132` 9.0-second gap — **verified** (`N9`).

---

## §3 — FINDINGS

### CRITICAL — **NONE**

No lookahead, no hindsight contamination, no fabricated evidence, no silently-resolved
contradiction, no unsupported number entering the canonical methodology. **The `D-035` holdout was
not touched**: `assert_development()` re-checks every window and 2016-07-01→12-31 is not on disk.
**`D-030` is respected without exception** — six of seven homework items are refused rather than
approximated, four of them expressly on `D-030`.

---

### **`M1` — MAJOR — `E24` — NOT ONE CONFIDENCE INTERVAL IS REPORTED ANYWHERE IN THE V19 QUANTITATIVE CHAIN, AND THE REPORT CLASSIFIES ITSELF `EVIDENTIAL`**

**The rule.** `BACKTEST_EVIDENCE_STANDARD.md` §4.2: *"Every hit rate is reported with an interval."*
§5 defines `EVIDENTIAL` as *"Pre-registered rule and period, baseline run, n ≥ 30, **interval
reported**"*. §7: *"Any check failing is at least `MAJOR`."* `REVIEW_PROTOCOL.md` §6.G check 19 is
the check.

**The fact.** A grep for `Wilson`, `95%`, `confidence interval`, `boot_ci` and `CI` across
`BT_V19_0001.md`, `PT-047`, `run_pt047.py`, `posthoc047.py`, `pt047_results.json`,
`V19_HOMEWORK.md`, `hw_v19.py`, `V19_INTERPRETATION.md` and `V19_MASTERY_REPORT.md` returns
**zero hits in every file**. `BT_V19_0001.md` §0a nevertheless states *"This observation is
classified `EVIDENTIAL`."*

⚠️ **This is a regression, not a novel demand.** `BT_V17_0001.md` carries a **Wilson 95 %** column;
`BT_V18_0001.md` opens with *"Wilson 95 % intervals on the primary window and arm"* and reads the
result **against** them. `mmm_lib` ships `boot_ci()`, and **twelve prior runners call `boot_ci` or a
Wilson helper** — including `hw_v17.py`, whose V19 counterpart `hw_v19.py` does not.

**Why it is `MAJOR` and not `MINOR` — the intervals change how the headline may be read.** Computed
by this reviewer on the primary cell (`A｜W-A｜30m`, `n_H` = 39, `n_B` = 60; bootstrap 20,000,
Wilson for rates):

| Quantity | Reported | **Interval this reviewer computes** | Consequence |
|---|---|---|---|
| **Δ (the decision statistic)** | **+25.75 pips** | **boot 95 % `[7.95, 38.60]`** | ⚠️⚠️ **the lower bound is BELOW the pre-registered `Δ ≥ 10` materiality floor** |
| **median `O1`(`HELD_ABOVE`)** | **43.20 pips**, *"inside the lesson's own `[25, 50]` band"* | **boot 95 % `[32.30, 54.50]`** | ⚠️⚠️ **straddles 50 — the upper edge of the band `CONFIRMED` requires it to lie inside** |
| `O2` `HELD` ≥ 25 pips | 76.9 % | Wilson 95 % `[61.7 %, 87.4 %]` | quoted in §2 to reinterpret `O3`'s weakness |
| `O2` `BACK` ≥ 25 pips | 45.0 % | Wilson 95 % `[33.1 %, 57.5 %]` | — |
| `O3` inside `[25, 50]` | 33.3 % | Wilson 95 % `[20.6 %, 49.0 %]` | — |
| `O3` inside `[25, 55]` | 43.6 % | Wilson 95 % `[29.3 %, 59.0 %]` | — |

⭐ **Both legs of the `CONFIRMED` gate — `Δ ≥ 10` and *median inside `[25, 50]`* — lie inside the
95 % interval of failing.** A reader of `BT_V19_0001.md` §0 as filed cannot know that. **That is
precisely the harm §4.2 exists to prevent** (*"Reporting '60 %' alone hides that"*), and it is the
harm `REVIEW_PROTOCOL.md` §18 asks about, because this is the number a machine rule would inherit.

⚠️ **WHAT IS NOT WRONG, AND MUST NOT BE READ AS WRONG.** The **direction** and the
**non-randomness** are solid and survive everything this reviewer threw at them: `p` = 0.0004 on an
independent seed, Mann-Whitney `p` = 7.0 × 10⁻⁵, all eight cells positive, the disjoint-window
re-measurement, and all four probes in §2.2. ⛔ **The `MAJOR` is that an `EVIDENTIAL` claim was
filed without the interval its own classification requires — not that the finding is unsound.**

**Secondary instance, same code:** `V19_HOMEWORK.md` §§4–6 quote rates (37.8 %, 46.3 %, 10.1 %, …)
without intervals. `n` is 234–474 there, so the intervals are tight and nothing misleads — **it is
listed for completeness of the fix, not as separate harm.**

---

### `m1` — MINOR — `E11` — THE ASR RETURNED/OWED LISTS ARE WRONG IN THREE PLACES: **`S8` RETURNED AND `S1` IS NOT MISSING**

`V19_TRANSCRIPT.md:144` states *"Seven of the twelve returned … (`S1`, `S2`, `S4`, `S5`, `S6`, `S7`,
`S11`)"*; line 282 and `REVIEW_INDEX.md` item **287** and `V19_MASTERY_REPORT.md` §2.2/§7 all state
that **`S3`, `S8`, `S9`, `S10`, `S12`** did not return.

**`06_MANUAL_BACKTEST/V19/data/asr_segment_results.txt` contains seven headers — `S2 S4 S5 S6 S11
S7 S8` — and no `S1` header at all.** Reading the `S8` block shows why: it runs from the genuine
`32:45–33:15` content (*"bar one is the bar that forms the high of the day or high of the
session"*) straight into *"Okay, so let's talk about this for a second. The definition of a half of
Batman…"*, which is **`S1`'s window, 13:05–14:00**. This reviewer's own `S1` run reproduces that
text line for line, and the committed transcript shows the Half-A-Batman definition is spoken
**once**, at `[00:13:06]`–`[00:13:52]` — **at `[00:33:15]`–`[00:33:55]` the lesson is on an entirely
different passage.**

⭐ **So `S1` and `S8` BOTH returned and their outputs were concatenated under one header, with
`S1`'s header lost.** The true counts are **eight of twelve returned** and **four owed** — `S3`,
`S9`, `S10`, `S12`.

⭐ **The three `S1` citations are therefore SOUND, not unsupported** — `V19_TRANSCRIPT.md` lines 178,
261 and 272 rest on text that genuinely exists and that this reviewer reproduced independently. ⚠️
**But an evidence file that merges two runs under one label, and three summary statements that
misreport which evidence exists, is a provenance defect in a self-disclosure the session
specifically handed to the reviewer.** The error runs in the conservative direction — the debt was
**overstated** — which is why it is `MINOR`.

---

### `m2` — MINOR — `E20` — `V19_INTERPRETATION.md` §2.6 MISDESCRIBES WHAT ITS OWN BACKTEST TESTED

§2.6, on star formations: *"It is also the most directly testable claim V19 makes, **which is why
the manual backtest goes after it** (`BT_V19_0001.md`)."*

⛔ **It does not.** `PT-047` tests the **second-leg time cap and the 25–50 pip extension** — §2.1 and
§2.2 of the same file — and `PT-047` §1a expressly states *"It does not test the M or W
formation"*. **No star formation is measured anywhere in the runner.** A later session reading §2.6
would believe V19's star claim has been tested. It has not.

---

### `m3` — MINOR — `E20` — `SWF_CAPTURE_RECIPE.md` §9's TWO-PASS ORDER WAS NOT FOLLOWED (item **286**, answered)

**The violation is real and the disclosure is exemplary** — led with, in three files, and offered
for a finding rather than defended.

⭐ **This reviewer ran the leak test the disclosure invites, because "structural mitigation" is only
worth what an audit says it is worth.** Every frame-only string was grepped across §§1–9 (the
transcript-only sections, lines 35–382 of `V19_SOURCE_NOTES.md`): `HOD`, `LOD`, `LOS`, `30M`,
`with in`, `Hi/Lo`, `ADR`, `Half – a - Batman`, `Trap Candle Patterns`, `Dealer Structures`,
`Behavioral Analysis`, `Memorial day weekend`, `Live in New Jersey`, `PowerPoint`, and every
frame-referring word.

> **Result: §§1–9 contain exactly ONE frame-derived datum — `HOS` at line 122 — and it is
> explicitly bracketed, attributed and cross-referenced to §10.** The three `30 to 45 m` hits are
> the substring inside *"30 to 45 **minutes**"*, spoken, cited to markers, and **verified from the
> audio by this reviewer** at `[00:26:12]` and `[00:47:21]`.

**The claimed mitigation holds under test.** It stays `MINOR` rather than dropping to `NOTE` because
a written protocol was not followed and verifying that cost the reviewer real work — which is
exactly what the session said it had pushed downstream. ⭐ **And see `N16`: two of the three drivers
were mandated by the same document, which is a defect in the recipe, not in this session.**

---

## §4 — NOTES

| # | Note |
|---|---|
| `N1` | ⭐⭐ **`PT-047` reproduces BYTE-IDENTICALLY on re-run and EXACTLY on independently written code** — every `n`, every median, every Δ, every day count. §2.1 |
| `N2` | ⭐ **Item 290 ANSWERED, and sharpened from "very likely" to certain.** At 60 minutes the `n < 30` guard **fires on two cells** (`A｜W-A` `n_H` = 29, `B｜W-A` `n_H` = 27). ⚠ **But Δ GROWS — 25.75 → 29.45, `p` = 0.0003.** `N3` would have returned `FRAGILE` on a **strengthening** result: its `n < 30` condition guards precision and here it would have fired against the effect's own direction. **An observation about `N3`'s design, not a defect in `PT-047`.** ⭐ **And the 30/45 arm choice is SOURCE-DERIVED, not chosen for the result** — `30M` is on the M slide and `30 to 45 m` on the W slide, both verified from the pixels by this reviewer. **60 minutes is nowhere in the lesson and 90 is expressly excluded by it** (`[00:47:21]`) |
| `N3` | ⭐ **Item 289 ANSWERED.** The post-hoc disjoint-window check reproduces exactly (Δ +26.90, `p` = 0.0005 on the primary cell). **The session is right to label it post-hoc and a reviewer is entitled to discount it — so this reviewer did not rely on it**, and instead ran P2/P3/P4 (§2.2), which are independent of the objection and all hold. ⭐ **Raising an objection against your own pre-registration, testing it, and reporting the test as discountable is the behaviour `REVIEW_PROTOCOL.md` §17 is trying to produce** |
| `N4` | ⭐ **Item 291 VERIFIED INDEPENDENTLY, in full.** All three V19 SHA-256 values match the pinned figures; byte lengths 3,173 / 1,712 / 1,253 match; the diff matrix is **exactly** `2/10/8` against V16, V17, V18 **and** V20, and **exactly** `32/30/26` against **both** V15 and V21. ⭐ **`V21` diffs against V19 precisely as V15 does — the V17 review's block prediction is confirmed from inside the block, in both directions.** The `V18 → V19` enumeration matches the count line for line (5 pairs at `1c1,3c3,16c16,20c20,33c33`; 1 at `1c1`; 4 at `1c1,5c5,13c13,21c21`), **zero content lines** — item 249's specific complaint honoured |
| `N5` | ⭐ **Item 285 VERIFIED FROM THE PIXELS.** All four slide frames read; burned timecodes match filenames (`21:15`, `23:25`, `45:00`, `50:34`). The M slide gains **`with in 30M`**; the W slide gains **`with in 30 to 45 m`**. ⭐ **The two edits DO differ — `C-029` is real and is a Tier-1-vs-Tier-1 conflict inside one deck, forty-five minutes apart** |
| `N6` | ⭐ **Item 294 VERIFIED FROM THE PIXELS, all three.** `02:00` = the printed **course schedule** (May 20 → July 1), not an EMA chart template. `15:00` = the **`Half – a - Batman`** chart. `30:00` = `MARKET MAKER TRAP MOVES`, a freehand magenta M over candles with a yellow and a red MA and a cyan dashed level — **no TDI panel anywhere on screen**, so *"TDI Shark Fin"* is refuted |
| `N7` | ⭐⭐ **ITEM 287's DEBT IS DISCHARGED BY THIS REVIEWER.** All four genuinely-owed segments plus `S1` were cut and transcribed. **Every one corroborates; none overturns anything.** `S3`: *"push it 15 to 20 pips … consolidation off of the low should be, depending on the pair, 15 to 25 pips … as high as 50 on some of the crosses."* `S9`: ⭐ *"**An M formation** that is 8 candles or greater to form, **which is by the way 2 hours**"* — settling item 288 and item 301 **from the audio**. `S10`: *"can be slightly below the first but must close above … He must close back above in 30 minutes. 45 max."* `S12`: *"Railroad track consists of 30 minutes, 15 in, 15 out … he gets an extra 15 minutes."* `S1`: the four Half-A-Batman clauses, verbatim |
| `N8` | ⭐ **`Q-020`'s three load-bearing quotes VERIFIED VERBATIM from audio by this reviewer.** *"90 minutes is too long, 30 to 45 minutes back above the previous low"*; *"in order for the 50 to cross the 200 and to get separation on it"*; *"30 to 90 minutes up to two hours the dealer holds the level"* (in the Half-A-Batman consolidation context). **Item 292's central claim — that the fabricated row attaches `30–90` to the one quantity the lesson caps below 90 — stands on verified audio** |
| `N9` | ⭐ **`A-132` IS NOW VERIFIED and its measurement arm can close.** Independently extracted audio measures **4042.005 s**; the last marker `[01:07:13]` = 4033 s; **the gap is 9.005 s**, matching the session's 9.0 s to the centisecond |
| `N10` | ⭐ **Provenance verified at the top of the hierarchy.** The `.swf`'s SHA-256 re-computes to `7e8a1c2b…5c1ab28e` and its length to 25,694,598 bytes — **both matching `SOURCE_MANIFEST.md` exactly** |
| `N11` | ⭐ **Item 286's mitigation VERIFIED, not accepted** — see `m3`. One labelled frame-derived datum in §§1–9 |
| `N12` | **`REVIEW_PROTOCOL.md` §6a check (3), `D-049` — ENGAGED IN FORM, SATISFIED ON EVERY CLAUSE, AND NEVER NAMED.** `Q-020` §0 diffs V19's trio against **V20's and V21's** quarantined files. That is a forward read in form. **(a)** a diff line-count is maximally bibliographic ✅; **(b)** disclosed in the artifact that relies on it ✅; **(c)** no artifact about the future lesson created — the claim is about quarantined fabricated metadata, not lesson content ✅; **(d)** independently reproduced by this reviewer ✅; **fifth** — no ingested source could answer it ✅. ⭐ **And the practice is established by item 254, where the V17 REVIEWER did it first, and by `Q-019`.** **No finding.** Recommended: `Q-020` should say so in a line, so the next session does not have to re-derive the permission |
| `N13` | **§6a check (1), `D-046` — NOT ENGAGED, and the abstention is correct.** `grep` returns **zero** occurrences of `EXCLUDED BY DECISION` across the whole V19 set. Dimension B is recorded **`BLOCKED — D-030`**, and `D-030` was **read, not taken on trust**: it bars substituting *"an approximation, a plausible reading … or a 'reasonable' numeric stand-in"* for a named-but-undefined concept, which is exactly the *"blue tracer"*. **The disposition is right and `D-018`/`D-019` are correctly distinguished from it** |
| `N14` | **§6a check (2), `D-048` — NOT ENGAGED.** No rung is claimed and none is needed. ⭐ **`C-029` is a genuine Tier-1-against-Tier-1 conflict — two printed slides from one deck — and the session records it OPEN rather than picking a winner.** That is what rung 4 would require in any case, reached without the ladder |
| `N15` | `validate_project.py` reproduces **103 / 0 / 0**; `hw_v19.py` reproduces **byte-identically** |
| `N16` | ⚠️ **`SWF_CAPTURE_RECIPE.md` CONTRADICTS ITSELF, AND EVERY FUTURE SESSION WILL HIT IT.** §9 step 2 requires the source notes to be written *"from the transcript alone, before looking at screenshots"* — but **§8a's offset verification cannot be done without reading frames**, and **`GOTCHA 4` requires a frame/transcript content check *"in the first two minutes instead of after an hour"***. **Two mandatory steps make the prescribed order impossible as written.** ⛔ **This is not the student's to fix**: the recipe is a policy file and `D-038a` bars a lesson branch from touching one. **Recommended to the owner in §6** |
| `N17` | ⭐ **Item 297 VERIFIED.** `A-131` is genuinely V18's (*"V18 supplies NO clock time for any trading session"*); V19's four records sit at `A-132`–`A-135`; **no collision remains at merge-back**. `PT-047` still reads `A-132` and the correction lives in `BT_V19_0001.md` §6 — ⭐ **which is the right place. Reverting the bulk renumber of a pre-registration was the correct call**, and `COMMON_PROTOCOL.md` §9 rule 7 means what it says |
| `N18` | ⭐ **The strongest judgement in the submission is in the HOMEWORK, not the backtest.** §6 measures a median 2-hour pullback of 41–46 pips against V19's stated `15 to 25`, and **refuses to read the gap as a refutation** because a maximum excursion and a resting distance are different quantities and *"a gap in this direction is expected a priori"*. It then records the **size** of the gap as a starting distribution for a future test. **`REVIEW_PROTOCOL.md` §6.I, unprompted** |
| `N19` | ⭐ **`A-135` opened and closed in one session is the right form, and it is now doubly settled.** The `25 to 55` readings at `[00:23:57]`/`[00:24:32]` are ASR defects; this reviewer's own `S5` window is not among the segments re-run, but the committed file's later `25 to 50` readings, the student's `S5` result and **the printed slide chain** all agree. **The number is `25 to 50 pips`** |

---

## §5 — AUDIT DIMENSIONS (`REVIEW_PROTOCOL.md` §6)

| Dim | Grade | Basis |
|---|---|---|
| **A** Source fidelity | ✅ **PASS** | Every load-bearing quote verified in the transcript body, and eight of them verified again from the audio. No omitted qualifier — `[00:40:53]` *"Is it hard and fast? No"* is carried everywhere the `25–50` rule is cited |
| **B** Completeness | ✅ **PASS** | Four structures, the five-stage M sequence, the W mirror, the exception, the sizing rule, and `§11 — WHAT V19 DOES NOT CONTAIN` |
| **C** Provenance | ⚠️ **MINOR** | `m1` — three statements misreport which ASR evidence exists |
| **D** Explicit vs inferred | ✅ **PASS** | The 15-minute timeframe is graded **HIGH and DERIVED**, with *"the lesson never says M15 — the string does not occur"* stated in three files |
| **E** Chart recognition | ⚠️ **BLOCKED, correctly** | `D-030`. Not claimed as `NOT APPLICABLE`; recorded as a debt (`N13`) |
| **F** Counterexamples | ✅ **PASS** | The Half-A-Batman is the lesson's own counterexample to the M/W and is treated as the unifying idea, not a footnote |
| **G** Manual backtest | ⚠️ **MAJOR** | `M1`. Checks 1–18 and 20 pass; **check 19 fails** |
| **H** Hindsight / lookahead | ✅ **PASS** | `O1` measured strictly forward of `t`; holdout sealed and re-asserted per window; the disjoint-window objection **self-raised** |
| **I** Outcome vs rule | ✅ **PASS** | No P&L, no fills, no win rate — §1a says so first, and §5 repeats *"an excursion is not a fill"* |
| **J** Sample quality | ⚠️ **see `M1`** | `n` ≥ 31 on every cell, so §4.1's floor is met; **§4.2's interval is what is missing** |
| **K** Homework | ✅ **PASS** | Six of seven refused **with reasons**; the executable one run with its convention declared three times |
| **L** Teach-back | ✅ **PASS** | `V19_MASTERY_REPORT.md` §1 is an accurate one-paragraph teach-back |
| **M** Blind recognition | ⚠️ **BLOCKED** | `D-030`, same cause as E |
| **N** Ambiguity | ✅ **PASS** | `A-134` opened rather than picking a cap; the `[00:17:11]` near-miss recorded as a near-miss |
| **O** Contradictions | ✅ **PASS** | `C-029` recorded `OPEN`, not resolved |
| **P** Machine-rule firewall | ✅ **PASS** | The ADR lookback is declared *"this session's convention, not V19's"*, and three periods are reported so none is privileged |
| **Q** Claimed accuracy | ✅ **PASS** | The `90 %` and the *"high 80 percent"* are preserved, cited, **and expressly not tested** — `D-009` invoked by name |

---

## §6 — REQUIRED CORRECTIONS

**Specific and bounded. The student should redo only these.**

1. ⭐⭐ **`M1` — ADD THE INTERVALS.** In `BT_V19_0001.md`:
   * §2 — add a **Wilson 95 %** column to the `O2`/`O3` table and a **bootstrap 95 %** figure beside
     `Δ` and beside `median O1(HELD_ABOVE)` on the primary cell. The values are computed above and
     may be re-derived with `mmm_lib.boot_ci()`; `06_MANUAL_BACKTEST/V19/data/rev_pt047_intervals.txt`
     carries this reviewer's run.
   * §0 — add one sentence directly under the verdict: **the `Δ ≥ 10` leg and the *median inside
     `[25, 50]`* leg are each inside the 95 % interval of failing, and the magnitude claim is
     therefore not resolvable at that precision on this sample.**
   * §5 — add to *"It does NOT establish"*: **that the extension magnitude is `25–50` rather than
     merely positive and material.**
   * ⛔ **Do NOT change the verdict, the decision rule, or `PT-047`.** The rule was pre-registered on
     point estimates and stays that way (`COMMON_PROTOCOL.md` §9 rule 7).
   * `V19_HOMEWORK.md` §§4–6 — add intervals to the quoted rates for completeness.
2. **`m1` — CORRECT THE ASR ACCOUNTING** in `V19_TRANSCRIPT.md` (lines 144 and 282),
   `V19_MASTERY_REPORT.md` §2.2 and §7 item 1, and `REVIEW_INDEX.md` item 287: **eight of twelve
   returned; `S3`, `S9`, `S10`, `S12` were owed.** Split `asr_segment_results.txt`'s `S8` block at
   *"Okay, so let's talk about this for a second"* and restore the `===== S1 =====` header. **Then
   mark all four remaining segments DISCHARGED**, citing `06_MANUAL_BACKTEST/V19/data/rev_asr_owed_segments.txt`
   from this round.
3. **`m2` — FIX THE CROSS-REFERENCE** at `V19_INTERPRETATION.md` §2.6: the manual backtest tests
   §2.1/§2.2, **not** the star formation. State that V19's star claim **remains untested**.
4. **`m3` — no artifact change is owed by the student.** The disclosure is already correct and
   complete. **The fix belongs to the recipe** — see §7 question 1.

---

## §7 — REVIEWER QUESTIONS FOR THE OWNER

1. ⭐ **`SWF_CAPTURE_RECIPE.md` §9 vs §8a and `GOTCHA 4` — the recipe mandates an order it also makes
   impossible** (`N16`). Recommended amendment: §9 step 2 permits reading frames **for offset
   verification and the `GOTCHA 4` sanity check only**, requiring the datum to be labelled at point
   of use and confined to §10 — which is what this session actually did and what the leak test
   confirms works. **A policy file; not the student's to change.**
2. **`N2` — should `N3`'s `n < 30` condition be able to fire against a strengthening effect?** As
   written it is a precision guard reported as a fragility verdict. Not a V19 question; a
   `BACKTEST_EVIDENCE_STANDARD.md` question the 60-minute arm has now made concrete.
3. **`C-029` / `A-134` — the deck contradicts itself on camera about the time cap** (`30M` vs
   `30 to 45 m`). One owner sentence or one later lesson closes it. Until then `PT-047`'s primary
   arm rests on `[00:26:12]` *"30 minutes is a good rule"*, which is the defensible choice.
4. **`A-133` — the *"blue tracer"* is spoken 15 times and never defined**, and it blocks dimensions
   E and M for the sixth lesson running. **V19 was the lesson expected to supply it and did not.**
5. **Item 298 / `DECISION_DRAFT_D-051`** — the `06:45` frame prints `Use ADR and Hi/Lo Markers` as
   standing homework. **Tier 1, flagged, no adoption proposed by either session.** The draft's owner
   should see it.

---

## §8 — ADVANCEMENT

```text
LESSON: V19
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- none

MAJOR ISSUES:
- M1  E24  No confidence interval is reported anywhere in the V19 quantitative chain,
           while BT_V19_0001.md §0a classifies the observation EVIDENTIAL, which
           BACKTEST_EVIDENCE_STANDARD.md §5 defines as requiring one. With the intervals
           computed, BOTH legs of the CONFIRMED gate lie inside the 95% interval of
           failing: Delta = +25.75 [7.95, 38.60] against a pre-registered floor of 10,
           and median O1(HELD) = 43.20 [32.30, 54.50] against a band closing at 50.
           The direction and the non-randomness are unaffected and robust.

REQUIRED ACTIONS:
1. Add Wilson / bootstrap intervals to BT_V19_0001.md §2, a qualifying sentence to §0,
   a line to §5's "does NOT establish", and intervals to V19_HOMEWORK.md §§4-6.
   Do not change the verdict, the decision rule, or PT-047.
2. Correct the ASR returned/owed lists in four places; split the S8 block; record the
   four owed segments as DISCHARGED by this round.
3. Fix V19_INTERPRETATION.md §2.6's cross-reference to BT_V19_0001.md.

ADVANCEMENT: NOT AUTHORIZED
```

⛔ **`V20`'s GATE IS CLOSED** under `D-024` — one `MAJOR`. It opens when actions 1–3 land and are
re-reviewed. ⭐ **Action 1 is the only one that touches a number, and it adds figures rather than
changing any.** This is a short round of remediation, not a re-run.

---

## §9 — REVIEWER'S OWN DISCLOSURES

1. ⚠️ **The primary checkout was in use by another session during this review.** `HEAD` moved from
   `review/v19` to `tools/indicator-folder-survey-and-owner-risk-rule` underneath this session
   mid-audit. **All work from that point was moved into a dedicated worktree**
   (`MMM-Agents-review-v19`, `D-038`) and **every quantitative result reported here was re-run there
   from a clean tree.** No commit was made to the shared checkout.
2. ⭐ **Wiring the git-ignored corpus into the review worktree was done by symlinking the CSVs
   individually**, never the directory, and `git status` was checked for type-changes afterwards —
   **zero**. This is the exact step item **300** warns about, and the warning was useful.
3. **`mmm_lib` was used for corpus loading, the arm clocks and the C-1…C-6 calendar** in
   `rev_pt047_independent.py`. That layer is shared, checksummed by `qa_gate()` and audited in
   earlier rounds; re-deriving it would have tested the vendor CSVs, not `PT-047`. **The event scan,
   classifier, outcomes, permutation and rank test are this reviewer's own code.**
4. **`run_pt047.py` was read before `rev_pt047_independent.py` was written**, for the reproduction
   check. ⚠️ **Independence is therefore weaker than V18 R1's**, where the reviewer's code came
   first. Mitigation: the implementation is structurally different at every step and uses a
   different seed. **Stated rather than claimed away.**
5. **The reviewer's ASR used `whisper medium.en`, the same engine the session pre-registered.** That
   makes the five owed segments a **completion of the session's own pass**, not a third-engine
   check. A genuinely independent engine on those segments is still available and was not run.
6. **Not everything was re-derived.** The 27-frame timecode census, the §8a offset bracketing, and
   the `04_SCREENSHOTS/V19/INDEX.md` grid were **spot-checked on six frames, not all 27**. V18 R1
   verified 26/26; **this round did not**, and the §8a *"fourth shape"* hypothesis at item 296 is
   **recorded as unverified by this reviewer**.
7. **No policy file was modified.** `DECISIONS.md`, `REVIEW_PROTOCOL.md`,
   `BACKTEST_EVIDENCE_STANDARD.md` and `SWF_CAPTURE_RECIPE.md` are untouched; §7's recommendations
   are put to the owner, not applied.
