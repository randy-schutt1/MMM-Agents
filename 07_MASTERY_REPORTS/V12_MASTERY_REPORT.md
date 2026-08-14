# V12 — MASTERY REPORT

```text
LESSON:   V12 -- Bootcamp1 Wk4 040812 Part2 (55mins).swf -- "Traders Dynamic Index"
SESSION:  2012-04-08 (Easter Sunday). THE SAME SESSION AS V11, which is Part 1.
SPEAKER:  Course author, 100%, HIGH confidence, over-determined (9 strands, 0 handovers)
BRANCH:   video/v12, isolated worktree (D-038). NOT MERGED -- review comes first (D-004)
STATUS:   REVIEW REQUIRED
```

---

## 0. THE THREE THINGS A REVIEWER SHOULD READ FIRST

1. **⭐ `A-080` CLOSES — the course states a parameter, for the first time in this corpus.**
   *"I like the RSI line to be set at **21**"* `[00:07:24]`, three more times, with the reason and
   the default it replaces. **And it closes on the AUDIO, not on the frame everyone predicted.**
2. **⭐ `mayonnaise = 200` reaches Tier 1** — *"held by the mayonnaise perfectly. **Held by the
   200**"* `[00:31:22]`, with `PRICE HELD BY 200` printed on the slide at that instant.
3. **⛔ AND `PT-040` SAYS THE FIRST ONE DID NOT UNBLOCK WHAT IT WAS MEANT TO.** The
   pre-registered test returned **`MATERIAL`, `M = 10.48 pp`**, so V11's RSI threshold claims
   **stay blocked** and `A-084` becomes an active blocker. **The session's headline finding did not
   buy what it was supposed to buy, and the bar that says so was committed before the runner
   existed.**

---

## 1. THE TEN DIMENSIONS

### A. Recall — ✅ **SATISFIED**

The lesson's content is reproducible without the notes: the TDI's four components in build order
(RSI line → trade signal line → market baseline → volatility bands), the two setups (shark fin
short / long), the entry (`23` pips above the HOD), the two adds (MB break, then VB break during
the trend run and not during the stop hunt), the exit (all units on the RSI line's return inside
the bands), the *"checkpoints"* use for non-scalers, and the assignment.

**One numeric detail is deliberately NOT recalled as fact:** `[00:27:59]`'s *"this is the 67, this
is the 50"*. The `67` is unverified ASR, was not spot-checked, and is recorded as uncertain in
`V12_TRANSCRIPT.md` rather than carried into any artifact.

### B. Recognition — ⚠️ **NOT DEMONSTRATED, AND CANNOT BE**

**Stated plainly rather than claimed.** Recognition of this lesson's concepts on charts **not used
in the lesson** requires plotting the TDI, and **the TDI is not reconstructible** — three of four
parameters are unstated (`A-039`, `A-085`, `A-086`) and `PT-040` shows the fourth's ambiguity is
`MATERIAL`.

**No recognition claim is made on the lesson's own six worked charts**, which is the failure mode
`MASTERY_STANDARD.md` § SELF-ASSESSMENT HONESTY names first.

### C. Discrimination — ✅ **SATISFIED, on the lesson's own terms**

*What would make this NOT the setup?* The lesson answers directly and repeatedly:

- `[00:22:12]` *"**This is not a freaking long trade because it hit the Asian box twice**"* — an
  explicit counter-example, named as one.
- `[00:23:30]`–`[00:24:12]` a gate list: right phase, right time (*"two to four o'clock in the
  morning eastern time"*), right cycle, box size — *"you got to be in the right parts of the
  cycle"*, given as the answer to a hypothetical student who sees *"an M or a W and TDI looks like
  it might give me something, I'm gonna take it. **No.**"*
- `[00:33:51]` the VB add is qualified — *"**not during the stop hunt** but during the actual trend
  run"*.
- `MMM-NOTES` p.46's location gate agrees and **the Tier 1 version is what is adopted**
  (`§3.2` Case B).

⚠️ **The discrimination is real and it is not codable**, because every gate term is an open record.

### D. Sequence — ✅ **SATISFIED**

| Stage | What the lesson says |
|---|---|
| Before | Asian session, bands tight, tight range, right market segment |
| Setup | Vector candle forces the RSI line **outside** the band; it turns back over — the fin |
| Confirms | Fin re-enters the band **and** crosses the TSL — **blood in the water** |
| Invalidates | Wrong phase, wrong clock, box hit twice, consolidation rather than stop hunt |
| Follows | MB break → VB break → run → RSI line returns inside the bands → **exit all units** |

**This is the most complete before/setup/confirm/invalidate/follows chain in the corpus to date.**

### E. Exceptions — ✅ **SATISFIED**

Shark fin long as the inverted short (`[00:23:26]`, printed); the non-scaling *"checkpoints"*
variant (`[00:29:16]`, printed `41:41`); the second-leg stop variant (`[00:30:37]`); the
multi-session RSI W (`[00:37:07]`); and `[00:40:26]` *"variation on the theme — just understand
there's gonna be variances, **but I took these slides out because in here I don't want you to have
any variations, I want you to trade a certain way**"*, which is the instructor **naming and
suppressing** a class of exception.

### F. Homework — ⛔ **`UNRESOLVED`** — `05_HOMEWORK/V12/V12_HOMEWORK.md`

**One `PERFORMED` (H6, the blackout method), one `NOT APPLICABLE` (H5, forum posting), five
`DEFERRED` (H1–H4, H7).** `D-019` is respected: the deferred items are work that **exists and is
blocked**, not work that does not apply.

**The classification is `UNRESOLVED` and not `SUCCESS AFTER SOURCE REVIEW`.** The lesson's central
assignment — five blind demo trades on the TDI alone — cannot be performed because the TDI cannot
be built, and the bounded demonstration of that blocker (`PT-040`) is **not a substitute for the
assignment** and is not counted as one.

**A correction is recorded in that file rather than applied silently:** the first draft cited
`D-006` as an independent blocker on H2. **`D-006` defers automated backtesting and says nothing
about demo orders.** The blocker count went from two to one and the record says so.

### G. Manual backtesting — ✅ **SATISFIED**, and the result is unfavourable to this session

`06_MANUAL_BACKTEST/V12/BT_V12_0001.md`, `PT-040`.

| `D-026`/`D-027` requirement | Status |
|---|---|
| Baseline defined before testing | ✅ `k = 1` identity control **and** `R` itself as comparator |
| Period pre-registered | ✅ `W-A` primary, `W-B` robustness, both named before the run |
| Holdout left closed | ✅ `assert_development` on every slice; exits non-zero on breach |
| Rates with sample size and interval | ✅ `n = 24,730` reported **before** any rate; the decision quantity is a proportion difference with both `D-031` arms, a second window and a second RSI formulation |
| Pre-registration precedes the runner | ✅ **verifiable by commit** — `83110f1` at 2026-08-13T22:00:37-04:00 contains the design and **no `run_pt040.py`** |
| Classification | ✅ `O2` **`EVIDENTIAL`**; `O1`, `O3`, `O4` **`DESCRIPTIVE`** (`O4` pre-registered as such) |

```text
RESULT:  M = 10.481 pp at k=5, t=50.  VERDICT: MATERIAL.
         Even k=2 -- the shipped TDI's own default -- gives 5.16 pp at t=50.
CONSEQUENCE (pre-registered): V11's RSI threshold claims STAY BLOCKED.
                              A-084 becomes an ACTIVE BLOCKER.
```

> **The unfavourable result is the point and it is reported first, not buried.** This session closed
> `A-080` two hours earlier and had every incentive to find the ambiguity immaterial. The `2 pp`
> and `5 pp` boundaries were fixed before a single RSI value was computed. **`M = 10.48` is close
> enough to a defensible-sounding *"10 pp"* that a post-hoc boundary would have been a live
> temptation, and `D-029` plus commit ordering foreclosed it.**

### H. Provenance — ✅ **SATISFIED**

Every rule in `V12_SOURCE_NOTES.md` carries a timestamp and a medium tag (`AUDIO` / `PRINTED` /
`BOTH`). Seven passages carry an independent Whisper `small.en` confirmation. All 28 frames carry a
burned timecode verified against the sweep index **6/6 with zero drift**, and confirmed a second
way on content.

**Orphan rules: NONE.** **One near-orphan, listed explicitly:** `[00:27:59]`'s *"the 67"* — a
number attached to a TDI level, unverified, **carried into no artifact**.

### I. Ambiguity — ✅ **SATISFIED**

Three opened (`A-084`, `A-085`, `A-086`), four closed (`A-080`, `A-064`, `A-031`, `A-032`), one
split (`A-020`), one narrowed (`A-039`), one **reframed on a falsified premise** (`A-082`), and
**ten checked and recorded as NOT advanced** (`A-004`, `A-011`, `A-066`, `A-076`, `A-077`,
`A-038`, `A-002`/`A-049`, `A-056`, `A-042`).

**Nothing was quietly turned into a rule.** The three most tempting candidates were all refused:
the band's *"two standard deviations"* (`A-086` — the speaker disclaims it), the TSL's
*"polls the one-hour chart"* (`A-085` — recorded, nothing built on it), and the **colour** upgrade
for mayo (§10.3 — two frames show a white line and no legend says it is that line).

### J. Contradictions — ✅ **SATISFIED**

**`C-019` opened and resolved in Tier 1's favour**: `MMM-NOTES` p.46 puts *blood in the water* on
the market base line; V12 puts it on the trade signal line, printed and spoken, three times.
`SOURCING_HIERARCHY.md` §3.2 Case A + §3.3. `EXTERNAL_VOCABULARY_REFERENCE.md` §5.6, §5.7 and
§9.2's two rows annotated in place, superseded text left visible.

**Two divergences were deliberately NOT filed as contradictions, with reasons:**

- **The band basis** (Tier 2 says market baseline, V12 says RSI line) — Tier 1 is **self-hedged**,
  so `§3.3`'s *"the recording wins"* has no clear recording to prefer. Carried in `C-019` §3 and
  `A-086` under `C-011`'s asymmetry.
- **`25 to 50 pips`** (Tier 2: distance above the range; V12: the size of the box) — **the corpus
  is internally inconsistent on this before Tier 2 is consulted at all** (V04 `[00:37:26]` uses the
  Tier 2 sense), so it is `A-076`'s business, not a Tier 1/Tier 2 conflict.

---

## 2. QUALITY-CONTROL CHECKLIST

| Item | |
|---|---|
| Transcript exists · timestamps usable | ✅ 690 markers, 690 distinct, strictly increasing |
| Source notes exist · interpretation in a separate file | ✅ |
| Screenshots captured and indexed | ✅ 28 curated from 672 swept; every legible legend transcribed |
| Major rules have provenance | ✅ |
| Homework complete | ⛔ **`UNRESOLVED`** — stated, not omitted (dimension F) |
| Manual chart testing complete | ✅ `PT-040` |
| Positive · negative · borderline examples | ✅ six worked charts; `[00:22:12]`'s explicit counter-example; `[00:41:18]`'s *"kind of a shoulder, not really"* |
| Failed setups recorded, not hidden | ✅ — and the **test's own unfavourable verdict** is reported first |
| Ambiguity logged · contradictions logged | ✅ |
| `COURSE_PROGRESS.md` · `LOG.md` updated | ✅ |
| `validate_project.py` passes | ✅ on every commit, **staged first, validated second** (item 108) |
| Git state clean after commit | ✅ |
| **Concept library entries** | ⚠️ **NO ENTRY CREATED — the one unchecked box, and it is a JUDGEMENT, not neglect.** `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md` holds **0 concepts** by a reasoned, **review-upheld** policy: a term is promoted only when the course defines it, and promoting an open ambiguity *"would launder an open ambiguity into a citable definition"* (its rules 2 and 5). **V12 is the first real test of that policy** — see carry-forward (j) |

---

## 3. STATUS

```text
REVIEW REQUIRED
```

**Not `PASS`, for three named reasons — each is a judgement a reviewer may take differently:**

1. **`A-039`'s disposition.** This session narrows it and **may be UNDER-crediting**
   (`V12_INTERPRETATION.md` Q1). A reviewer could reasonably close it and re-point its dependents
   at `A-085`/`A-086`. **The call is declined here because closing it would silently unblock
   `A-031`'s stated dependency.**
2. **`A-066`.** V12 supplies the corpus's first stop distance **with an anchor** (`23` pips above
   the HOD, printed and spoken) and this session still declines to discharge the record — largely
   because the lesson **refuses to restate the number when asked** 18 minutes later. **MEDIUM
   confidence, and the reasoning is set out in Q4 so it can be overturned.**
3. **Dimension B is not demonstrated**, and dimension F is `UNRESOLVED`.

---

## 4. CARRY-FORWARD INTO V13

> `SOURCE_MANIFEST.md`: **V13 = `Bootcamp1 Wk5 041512 Part1 (65mins).swf`**, 2012-04-15, a **new
> week and a new date** — the first genuinely new session since V11. **V14 = `Part2 (48mins)`,
> same day.** The owner's hard stop is V14.

| # | Item |
|---|---|
| **(a)** | ⭐ **THE CHEAPEST REMAINING UNBLOCK IN THE PROJECT IS ONE SENTENCE OR ONE FRAME.** `A-084` needs either *"the plotted line **is** the RSI"* (which sets `k=1`, makes `O2 ≡ 0` and unblocks V11's whole RSI half immediately) or a smoothing length. **A TDI properties dialog in any of V13–V21 does the same job.** V12 was predicted to be that place and was not — **672 frames, no dialog, measured** |
| **(b)** | **SPEAKER: TEST IT, DO NOT ASSUME.** V13 is a **new week and a new date**, which is exactly the condition under which the corpus's course-author runtime has broken before (100% V03 → 31% V04 → 0% for five lessons → 100% V10). **V11 and V12 agreeing proves nothing about V13** — they are two halves of one recording |
| **(c)** | ⭐ **THE `A-082` CLASS OF ERROR IS THE V13/V14 AUDIT ITEM.** A record asserting *"the corpus never says X"* is only as good as the sweep behind it, and **`A-082` was wrong, was reachable on the day it was written, and survived a full review.** `V12_INTERPRETATION.md` Q6 lists five candidates — `A-004`, `A-011`, `A-076`, `A-056`, `A-002` — **with the cheap test for each. They were NOT run by this session** and that is stated, not implied |
| **(d)** | **A DIRECTLY ANSWERABLE VERSION OF (a), available now without any new lesson.** Extend `PT-040`'s sweep to **EMA and Wilder** smoothings of `RSI(21)` — `PT-040` §6 limitation 1 names this as the family the design deliberately does not cover. **It would not resolve `A-084`, but it would tell V13 whether the `MATERIAL` verdict is robust to the smoothing FAMILY or only to its length** |
| **(e)** | **`A-031` and `A-032` are CLOSED as to meaning and NOT COMPUTABLE.** Both definitions turn on the band, and the band is `A-086`. **A later session must not read *"`RESOLVED BY COURSE`"* as *"testable"*** — the records say so explicitly and this is the note that says it twice |
| **(f)** | **V12 gave V11's missing assignment.** If V13 promises one and does not give it, **check V14 before recording it as missing** — this session is the precedent that a two-part session splits promise from delivery |
| **(g)** | **`I-008` still stands.** V12's transcript has seven spot-checks over ~6 minutes of 55. **No lesson in the corpus has had a full independent re-transcription**, and the two records this session closed on audio (`A-080`, `A-020`) both rest on ASR confirmed by one other engine at the specific timestamps |
| **(h)** | **The library seed defect (`REVIEW_INDEX.md` item 113) is STILL OWED on the integration branch.** It was harmless in `PT-040` because that test uses no randomisation, and it will **not** be harmless in the next `PT` that bootstraps |
| **(i)** | ⚠️ **`EXTERNAL_VOCABULARY_REFERENCE.md` was edited on this task branch.** It is named in **neither** of `D-038a`'s two lists; classified here as an **evidence ledger** by `D-038a`'s own test, which is also what `SOURCING_HIERARCHY.md` §3.1 requires of the reconciling session. **Flagged for R1 to overrule if that classification is wrong** |
| **(j)** | ⭐ **`08_CONCEPT_LIBRARY/` IS THE ONE UNCHECKED BOX, AND V12 IS THE FIRST LESSON THAT GENUINELY TESTS ITS POLICY — the question is put to the reviewer rather than decided here.** The index holds **0 concepts** on a reasoned, review-upheld rule: promote a term only when the course defines it, never when it is an open `A-xxx`, because that *"would launder an open ambiguity into a citable definition"*. **Every prior lesson made that easy — nothing was defined.** V12 breaks the pattern: **`shark fin` and `blood in the water` are now `RESOLVED BY COURSE`, printed and spoken**, and `mayonnaise = 200` is Tier 1. **These are exactly the terms the index was written to wait for.** ⚠️ **This session did NOT create entries, and the reason is a real tension it does not think it should resolve alone:** all three are closed **as to meaning** and **not computable** (`A-086`), so promoting them would produce a concept entry a reader could mistake for a codable rule — a *different* laundering than the one the index's rules name, in the opposite direction. **The right answer is probably an entry that carries the closure AND the blocker in the same breath, and that is a change to the index's own rules, which a task branch should not make.** Put to R1 and to the owner as the decision V12 forces |
