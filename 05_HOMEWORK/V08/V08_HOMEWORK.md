# V08 — HOMEWORK

**Lesson:** V08 — *"Jim's Journey in Learning and Trading MMFX"*, 2012-03-26. **100% `GUEST`.**
**Assignments as identified:** `03_LESSON_NOTES/V08_SOURCE_NOTES.md` §9.

| Field | Value |
|---|---|
| Data source | **HistData.com GBP/USD M1 → M15** (`D-036a`), `06_MANUAL_BACKTEST/datasets/HISTDATA_GBPUSD_M1/` |
| Instrument | **GBP/USD** (`D-007`) |
| Window | **2013-01-06 → 2016-06-30** — `W-C′` DEVELOPMENT. Holdout never on disk |
| Timeframe | **15-minute** (`D-034`) |
| Measurement | Numbers parsed from a checksummed file. **Nothing read off a rendering** (`E06` per `D-036a`) |
| No account | No login, no broker account, no paid tier. Nothing was purchased and no CAPTCHA encountered |

---

## 1. DISPOSITIONS — WHAT WAS PERFORMED, DEFERRED, OR HAS NO SUBJECT MATTER

`D-018` grants `NOT APPLICABLE` only where a lesson supplies **no subject matter**; `D-019`
insists `NOT APPLICABLE` ≠ `DEFERRED`, and that work which is merely *blocked* is `DEFERRED`.
Each item below states which and why.

| # | Assignment | Disposition | Ground |
|---|---|---|---|
| **H1** | Validate the method: two hours after Friday's close, ten or more pairs, count last week's M/W setups | **`DEFERRED`** | **Doubly blocked, and the second blocker is new.** (a) Counting M/W setups requires M/W anatomy, which is `A-011`, named across eight lessons and never defined — `D-030` forbids substituting a definition to make it runnable. (b) **The claim is about the week of 2012-03-19, and the project's deep-history corpus begins 2013-01-01.** The specific week the lesson offers as evidence is **outside the corpus entirely**, on any vendor the project has declared. Discharges when `A-011` closes *and* a source reaching 2012 exists |
| **H2** | Make flashcards of M/W setups as they happen during the week | **`DEFERRED`** | Same `A-011` blocker. The *technique* is performed under H3 on an object that is defined |
| **H3** | Build hard-right-edge movies — erase what follows, then what leads in | ✅ **PERFORMED** | §2 below. Twelve flashcards, predictions committed before the key was opened |
| **H4** | Practise the high-low drill on a **demo account** | **`NOT APPLICABLE`** | **Directly on V07 R1's ruling**, which upheld the identical item as `NOT APPLICABLE` and refused to overturn it to `DEFERRED`: *"`DEFERRED` implies a future in which it becomes doable and there is none."* An agent cannot open or trade a demo account, and no future lesson or infrastructure change makes it performable. Matches V01's H6/H7 disposition |
| **H5** | Go back to the course author's own recording for the **box tool** | **`DEFERRED`** | **Measured, not assumed: the token `box tool` occurs in NO V01–V07 transcript.** It appears only in V08, referring to a recording the studied corpus does not contain. Either it is in V09–V21, or it is outside the bootcamp library. A new `A-042` instance |
| **H6** | Join the DMR on Mondays for the flashcards | **`NOT APPLICABLE`** | A live 2012 session. No subject matter now or ever |

**Two `NOT APPLICABLE`, three `DEFERRED`, one performed.** The performed one is the substantive
technique; the deferrals are `D-030` debt, which `D-030` says is *"the correct behaviour, not a
backlog to be cleared by lowering the standard."*

---

## 2. H3 — THE HARD-RIGHT-EDGE FLASHCARD DRILL, PERFORMED

### 2.1 Why this is performable when H1 and H2 are not

V08's flashcards are built around M/W formations. A flashcard set keyed on M/W would be keyed on
**this session's** definition of M/W, which is `D-030` exactly.

**So the drill is built on the object `PT-034` established is arithmetic: the day's low.** That
needs no course definition — and it is *also* the object V08's own high-low drill targets
(`[00:36:27]` *"entries at the extremes of the high of the day or the low of the day"*), so the
exercise sits **closer** to the lesson than an invented M/W proxy would, not further away.

### 2.2 Construction

| Parameter | Value | Source |
|---|---|---|
| Entry | day **LOW + 10 pips** | **the lesson's own printed tolerance**, frame `V08_00-05-40`, *"within 10 pips of HOD/LOD"* |
| Target | **+50 pips** | the lesson's own exit, stated 8× |
| Stop | **−16.67 pips** | `IMPLIED` from *"three to one or greater"*. **V08 states no stop distance** |
| Cards | **12**, sampled with seed `20260813` from `W-C′` session days | |
| Visible | every bar of the day up to and including the decision bar; **nothing after it** | |
| Direction | LONG only, for a clean single-question card | |

Scripts: `scripts/build_flashcards.py`. Fronts: `data/v08_flashcards_FRONT.json` and twelve SVGs
in `charts/`. Answer key: `data/v08_flashcards_KEY.json`.

### 2.3 The discipline, and it is the part that makes the result mean anything

**The answer key was written to a separate file and was not opened before predicting.**
Predictions and per-card reasoning were written to `data/v08_predictions.json` and **committed to
Git** before `score` was run. That is `D-026`/`D-027`'s pre-registration discipline applied to a
comprehension exercise.

**The predictor was V08's own heuristic**, `[00:36:15]`–`[00:36:16]`:

> *"The fast move is false. The slow and steady move is the correct move."*

read as: *a fast approach into the entry is a false move, so expect the reversal (`TARGET`); a
slow steady grind is the real move, so expect continuation through the entry (`STOP`)*.

> **The operationalisation is MINE and is declared as mine in the predictions file.** *Fast* has
> no definition in V08 (`A-061`). This is a personal judgement in a comprehension exercise; it is
> **not** a coded rule, it enters no spec, and **no number below may be cited as a measurement of
> the course's rule** (`D-010`, `D-030`).

**Recorded before scoring:** `PT-034` measured the base rate for exactly this entry at **70–77%
`TARGET`**, so an always-`TARGET` guess scores ~0.75. I predicted only **5 of 12** `TARGET` — a
deliberately discriminating call — and stated in the predictions file that I expected to lose to
the baseline.

### 2.4 THE RESULT — THE HEURISTIC FAILED, AND FAILED WORSE THAN GUESSING

```text
score: 5/12 = 0.42
ALWAYS-TARGET baseline on this set: 10/12 = 0.83
```

| Card | Day | Predicted | Actual | | Bars to resolve |
|---|---|---|---|---|---|
| 01 | 2015-09-27 | `TARGET` | **`STOP`** | ✗ | 89 |
| 02 | 2013-10-14 | `STOP` | **`TARGET`** | ✗ | 18 |
| 03 | 2013-05-09 | `TARGET` | `TARGET` | ✓ | 62 |
| 04 | 2015-12-28 | `STOP` | **`TARGET`** | ✗ | 100 |
| 05 | 2013-05-06 | `TARGET` | `TARGET` | ✓ | 77 |
| 06 | 2015-02-02 | `TARGET` | `TARGET` | ✓ | 11 |
| 07 | 2015-02-26 | `STOP` | **`TARGET`** | ✗ | 16 |
| 08 | 2013-05-15 | `TARGET` | `TARGET` | ✓ | 26 |
| 09 | 2016-02-21 | `STOP` | **`TARGET`** | ✗ | 9 |
| 10 | 2013-12-30 | `STOP` | **`TARGET`** | ✗ | 23 |
| 11 | 2013-08-26 | `STOP` | **`TARGET`** | ✗ | 5 |
| 12 | 2013-07-31 | `STOP` | `STOP` | ✓ | 33 |

**The split by half is where the information is, and it is unflattering in one direction only:**

| Half of the heuristic | Calls | Correct | Rate |
|---|---|---|---|
| *"fast move is false"* → predict `TARGET` | 5 | **4** | 0.80 — **indistinguishable from the 0.83 base rate** |
| *"slow and steady is correct"* → predict `STOP` | 7 | **1** | **0.14 — far WORSE than the base rate** |

**The `TARGET` half added nothing; the `STOP` half was actively anti-predictive.** Every point I
lost came from believing a slow, orderly decline into the day's low meant the decline would
continue. **On these twelve cards it almost never did** — six of my seven `STOP` calls reversed
and made +50 first, three of them within 23 bars.

**Card 09 is the sharpest miss and it was my most confident call.** A ~91-pip sustained
one-directional decline in the February 2016 sterling downtrend — the textbook *"slow and steady
= the correct move"* case — **resolved to `TARGET` in nine bars.**

> **`SAMPLE INSUFFICIENT FOR INFERENCE — DESCRIPTIVE ONLY.`** `n = 12`, far below
> `BACKTEST_EVIDENCE_STANDARD.md` §4.1's floor of 30. **Nothing here measures V08's rule** — the
> rule is `D-030`-blocked because *fast* is undefined, and what failed is **my** reading of it.
> A different operationalisation of *fast* could score differently, which is precisely why
> `D-030` forbids treating any of them as the course's.

### 2.5 What I actually take from it

1. **My reading of the heuristic is wrong, or the heuristic is, and this exercise cannot tell
   which.** That is the honest statement and it is the whole content of `A-061`: an entry cue
   with no measurable boundary cannot be evaluated, only guessed at.
2. **The result is consistent with `PT-034` and adds a caution to it.** `PT-034` found a large
   hindsight advantage from being at the day's extreme. This drill says that advantage is **not
   further improved by reading the approach**, at least not the way I read it — the base rate
   already contains the information, and my attempt to beat it destroyed 5 points of accuracy.
3. **A safe prediction would have scored 0.83 and taught nothing.** Predicting 10 or 11 `TARGET`
   would have looked better and tested nothing. The discriminating call was the point, and it
   failed cleanly enough to be informative.

---

## 3. COMPREHENSION PROBE — 58 ITEMS, FOUR BATTERIES

`scripts/comprehension_probe.py`, exit-1 on any failure so it can gate a commit.

| Battery | Items | Result | What it tests |
|---|---|---|---|
| **POSITIVE** | 23 | **23 pass** | Recall of specific claims, each found at a stated marker |
| **NEGATIVE** | 20 | **20 pass** | Plausible fabrications, **15 lifted verbatim from this lesson's own quarantined `NOTES.md` / `VISUAL_INDEX.md`** (`Q-009`). Each must be ABSENT |
| **REASONING** | 10 | **10 pass** | Predicates over the transcript — relations and arithmetic, not phrase matches |
| **VISUAL** | 5 | **5 pass** | **New in V08.** The falsifiable half of each frame claim: what the AUDIO must or must not say |

**Disclosed weakness, as V07 disclosed it:** the POSITIVE battery was written after
`V08_SOURCE_NOTES.md`, so it tests retention of this session's own work rather than first-exposure
recall. The NEGATIVE, REASONING and VISUAL batteries do not have that weakness — a fabrication
cannot be absorbed from notes that never contained it, and a relation between two passages cannot
be produced by fluency.

### 3.1 `R01` FAILED ON ITS FIRST WRITING, AND THE PROBE WAS WRONG — NOT THE TRANSCRIPT

`R01` checks that the lesson's day × session tally sums to its own headline of 29. The first
version **summed to 27** and failed.

**The transcript was right and the probe was wrong.** Eight of the ten figures are stated in the
lesson's usual form — *"two M&W set ups in the London session"* — and **two are not**:

```text
[00:15:53]  "On Tuesday we had one at London."
[00:15:56]  "We had one at New York."
```

Neither carries *"set ups"* nor *"session"*, which is what the first regex keyed on, so both were
silently dropped. The rewrite keys on the **venue**, which all ten figures name, and returns
**29 with all ten figures listed**.

**This is retained rather than quietly fixed** because it generalises: *a mechanical count over
this transcript that keys on the lesson's usual phrasing will silently undercount.* The failure
is preserved in the function's own docstring so the next session meets it before repeating it.

**`V08_SOURCE_NOTES.md` §4a's table was correct throughout** and was not changed.

---

## 4. INDEPENDENT CROSS-CHECK ON THE HOMEWORK'S CONCLUSIONS

Two, and neither is self-referential.

**1. The flashcard drill against `PT-034`.** The drill's always-`TARGET` baseline on twelve
sampled days is **0.83**; `PT-034`'s measured rate on **1,803–2,172 observations** across four
cells is **0.7046–0.7676**. The twelve-card sample sits **above** the full-corpus rate, which is
what a 12-draw sample from a ~0.73 process does often enough not to be surprising — and it is
stated here so the drill's baseline is not mistaken for a corpus-wide figure. **The drill's
conclusion does not depend on the baseline's exact value:** my 0.42 is below every version of it.

**2. `PT-034` against `PT-033`** — different session, different pre-registration, no shared code:
agreement to **+0.0007/+0.0010** at `X = 0` where the two entry rules are provably identical, and
divergence of **−0.0112 to −0.0190** at `X > 0` in the direction and rough magnitude predicted
**before** the comparison was run. Full detail:
`06_MANUAL_BACKTEST/V08/BT_V08_0001.md` §8.

---

## 5. WHAT THIS HOMEWORK DOES NOT ESTABLISH

- ❌ **Nothing about V08's rules.** *Fast* (`A-061`), *second leg* (`A-007`), *trap area*
  (`A-002`) and M/W (`A-011`) are all undefined; every rule that needs one stays `D-030`-blocked.
- ❌ **No stop distance.** −16.67 pips is `IMPLIED` arithmetic from the lesson's own ratio and
  target. **V08 states no stop.**
- ❌ **No support for the 29-setup claim.** H1 could not be attempted: the claim's own week
  (2012-03-19) is outside the corpus, and the count needs `A-011`.
- ❌ **Nothing enters `12_MASTER_SPEC/`, `13_MACHINE_SPEC/`, `08_CONCEPT_LIBRARY/` or any machine
  candidate.**
