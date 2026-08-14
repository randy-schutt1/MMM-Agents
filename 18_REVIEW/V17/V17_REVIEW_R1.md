# V17 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V17** · `Bootcamp1 Wk8 051312 Part1 (57mins).swf` · session **2012-05-13, Week 8**, Part 1 of two (V18 is Part 2 of the same night) · lesson sections **`TREND`** (PRINTED) and a course-to-date progress audit |
| Review version | **R1** |
| Review date | 2026-08-14 |
| Previous review | none |
| Reviewer branch | `review/v17`, cut from the integration branch @ `1f58058` (**post-`review/v16` merge and post-`fix/v16-r1-minors`**) |
| Submission reviewed | `video/v17` @ `245c756` (8 commits, `f55c2f3`…`245c756`) |
| Independence | **`D-003` satisfied.** This session authored no V17 artifact. It located the source `.swf` from `SOURCE_MANIFEST.md` and **re-computed its SHA-256 and byte length**; extracted the audio itself and **re-transcribed every load-bearing passage on a third engine** (`faster-whisper` / CTranslate2 `large-v3`), with a **fourth and fifth engine** (`openai-whisper` `medium.en` and `large-v3-turbo`) brought in to arbitrate one disputed word; **re-derived `PT-045` end to end** in code sharing no line with `run_pt045.py` or `mmm_lib`, parsing the raw HistData M1 CSVs directly, written from the pre-registration at commit `7eaf4d1` **before the runner was opened**; **re-executed the superseded calendar-consecutive reading** to test whether the declared artefact actually reproduces; **recomputed the whole of `V17_HOMEWORK.md` §2/§2a/§3** in its own code; **re-hashed and re-diffed all 63 quarantined fabrication files**, not only V17's three; **opened six frames as images and read their burned-in timecodes and printed text**; and **re-derived the `D-047` renumbering from the commit graph** rather than accepting the handed-over mapping |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 6 MINOR, 13 NOTE.**

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the gate
for V18.** The six minors are carried in `REVIEW_INDEX.md` as items **244–249** and are owed before
V17 can reach `COMPLETE`. **None of them changes a lesson conclusion, a record's disposition or
`PT-045`'s verdict** — but **item 244 inverts an inference the submission itself put to this
reviewer**, and it is answered here rather than returned as a question.

**Confidence: HIGH.** Every quantitative claim in the submission that this review could re-derive,
it re-derived. `PT-045`'s arm-A figures reproduce **to four decimal places in every reported cell**.

---

## §0 — ⚠⚠ THE `D-004` TIMING DISCLOSURE, ANSWERED FIRST, AND IT IS WRONG IN THE SUBMISSION'S FAVOUR

The V17 session declared — in `COURSE_PROGRESS.md`, in `V17_MASTERY_REPORT.md` §0 and in `LOG.md` —
that it opened V17 with its `D-004` gate **CLOSED**, V16's R1 not having returned, on the owner's
2026-08-14 authorisation; and it invited a reviewer to treat the whole artifact set as
**PROVISIONAL**. Its addendum commit `245c756` then recorded that V16's R1 had landed and that
V17's provisionality was discharged.

**The discharge is real and this review verified it rather than accepting it.** V16's R1 is merged
to integration at `0fee48c` — `REVISE`, **0 CRITICAL / 0 MAJOR / 4 MINOR / 11 NOTE**, HIGH
confidence, **V17 GATE OPEN under `D-024`** — and its four minors (items 222–225) are closed at
`1f58058`. V17 is therefore reviewable under a **fully open** gate, and this review treats it so.

⚠ **But the addendum's account of the timeline is factually wrong**, and it is wrong in the
direction that *understates* V17's standing. From the commit graph:

```text
e7a51cd  16:41:31   V16 bookkeeping (video/v17's merge-base)
0fee48c  17:16:53   merge(review/v16) -- V16's R1 LANDS ON INTEGRATION
f55c2f3  17:20:11   capture(V17)      -- V17's FIRST content commit
  …
346417b  17:51:47   bookkeeping(V17)  -- V17's LAST content commit
245c756  17:53:33   bookkeeping(V17 addendum)
```

The addendum states *"V16's R1 RETURNED after this session's last content commit"* and *"V16's R1
had not returned at any point during this session's work, and every V17 artifact was produced under
a CLOSED gate."* **V16's R1 was on integration three and a half minutes before V17's first content
commit, and before all eight of them.** The session could not see it from its own worktree, so the
belief was honest — but the addendum says it *"Checked on the integration branch before reporting"*,
and the check that was run did not extend to the one question the paragraph asserts.

**The defensible statement survives and the narrow ones do not.** *"V17 was OPENED with its gate
closed"* is true — the session began work under `e7a51cd`. *"V16's R1 returned after this session's
last content commit"* and *"had not returned at any point during this session's work"* are refuted
by the graph. **Charged as `MINOR` item 246**, because it alters no lesson conclusion and no record;
it corrects the project's durable process record in the section that exists for process honesty.

⭐ **The consequence for the reader is the opposite of alarming: V17's `D-004` compounding never
happened.** The *"second consecutive lesson on unreviewed ground"* framing, which appears in three
files, is not true of V17's committed work.

---

## §1 — SOURCE MATERIAL REVIEWED, BEFORE ANY STUDENT CONCLUSION

| Object | Location | What this review did |
|---|---|---|
| Source `.swf` | `01_SOURCE_VIDEOS/Forex Bootcamp/Bootcamp/Bootcamp1 Wk8 051312 Part1 (57mins).swf` | SHA-256 **`2281fa8b…07f767`** and **20,210,746 bytes** re-computed, **both matching** `SOURCE_MANIFEST.md` |
| Audio | extracted here with `ffmpeg`, 16 kHz mono | duration **3,429.64 s = 00:57:09.6**, matching the manifest |
| ASR | `faster-whisper` / CTranslate2 **`large-v3`** over seven segments; `openai-whisper` **`medium.en`** and **`large-v3-turbo`** on one disputed span | **three engines, none of them the student's `large-v3-turbo`-only pass in isolation** |
| Frames | `04_SCREENSHOTS/V17/`, six opened as images | burned-in player timecodes read directly; printed text transcribed off the pixels |
| V16 slide | `V16_00-14-25_london-session-start-2-to-3am-est-slide.png` | re-read at full resolution — `C-024`'s printed side |
| Quarantined trios | all **63** files under `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/` | re-hashed and pairwise-diffed across **all 21 lessons**, not only V17's |
| Data | `datasets/HISTDATA_GBPUSD_M1/raw/*.csv` | parsed by this review's own CSV reader; `mmm_lib` not used for any re-derivation |

---

## §2 — WHAT WAS RE-DERIVED RATHER THAN READ

### ⭐⭐ `PT-045` — INDEPENDENTLY RE-DERIVED FROM ITS PRE-REGISTRATION, AND IT REPRODUCES TO FOUR DECIMAL PLACES

Reviewer code was written from `PT-045` §§3–6 alone, at commit `7eaf4d1`, **before `run_pt045.py`
or `mmm_lib` was opened** — own CSV parser, own `[D−1 17:00, D 17:00)` session-day builder, own
96-bucket completeness census, own arm-B `America/New_York` shift, own shuffle null.

| Cell | measure | reviewer | submission |
|---|---|---|---|
| `W-D` A | `O1` / `O2` | `0.5426` / `0.8372` | `0.5424` / `0.8371` |
| `W-D` A | `n` reversals | **117** | **117** |
| `W-D` A | median run / `P(2..4)` | **2** / **0.4957** | **2.0** / **0.4957** |
| `W-D` A | `P(≥3│rev)` / uncond | **0.2906** / **0.2715** | **0.2906** / **0.2715** |
| `W-D` A | `O6` | **+59.0** | **+58.99** |
| `W-E` A | `n` rev / median / `P(2..4)` | **288** / **1** / **0.4132** | **288** / **1.0** / **0.4132** |
| `W-E` A | `P(≥3│rev)` / uncond | **0.2465** / **0.2689** | **0.2465** / **0.2689** |
| `W-E` A | `O6` | **+48.6** | **+48.62** |
| `W-D` B | `n` rev / median / `P(≥3│rev)` / uncond | 106 / **2** / 0.3019 / **0.2981** | 107 / **2.0** / 0.2991 / **0.2981** |
| `W-E` B | `n` rev / median / `P(2..4)` / `P(≥3│rev)` / uncond | **267** / **2** / **0.4457** / **0.2509** / **0.2799** | **267** / **2.0** / **0.4457** / **0.2509** / **0.2799** |

**Arm A reproduces exactly in every reported figure.** Arm B reproduces every verdict; its `n`
differs by one day (a window-edge convention) and `W-D` arm B's `O6` differs materially
(**+66.9** here against **+79.79**). `O6` is disclosed as **partly tautological** in `BT_V17_0001`
§6c and **enters no verdict**; the divergence is recorded as `NOTE` item 258 and charged as nothing.

⭐ **The headline splits exactly as claimed.** `O1` real − shuffled = **+0.0051 / −0.0051 / +0.0112 /
−0.0017** — inside `±0.05` in four cells of four. `O2` real − shuffled = **+0.1014 / +0.0814 /
+0.1192 / +0.0791** — above `+0.05` in four cells of four. **The wick's SIZE is path geometry; its
PRESENCE ON BOTH ENDS is not.** The claim is upheld on independent code.

⭐ **And the §6 decision-table hole is real.** This reviewer's own `W-D` cells fall through all four
pre-registered branches: not both `> +0.05`, not both within `±0.05`, neither `< −0.05`, and the
legs do not disagree in sign. The submission found this itself (item 243) and **did not edit the
pre-registration to fix it**, which is the correct call under `COMMON_PROTOCOL.md` §9 rule 7.

### ⭐⭐ THE CALENDAR-CONSECUTIVE ARTEFACT — RE-EXECUTED, AND IT REPRODUCES AS A CLEAN 4-OF-4 REFUTATION

`BT_V17_0001` §6a claims the runner's first execution read `PT-045` §3a's *"consecutive"* as
**calendar**-consecutive, and thereby produced a confident four-of-four `CONTRADICTED AS STATED` on
V17's three-day cycle that was **entirely a weekend**.

This review implemented that reading independently:

| Cell | reviewer, calendar-consecutive run continuation | verdict under §6 |
|---|---|---|
| `W-D` A | median run **1**, `P(≥3│rev)` 0.2137 | **CONTRADICTED AS STATED** |
| `W-E` A | median run **1**, `P(≥3│rev)` 0.1285 | **CONTRADICTED AS STATED** |
| `W-D` B | median run **1**, `P(≥3│rev)` 0.1792 | **CONTRADICTED AS STATED** |
| `W-E` B | median run **1**, `P(≥3│rev)` 0.1011 | **CONTRADICTED AS STATED** |

**Four of four, median run 1, a clean refutation of the lesson — and an artefact.** A stricter
variant that also required `R−3 … R+4` to be eight *calendar*-consecutive days returns **zero**
reversal windows in every cell, which is the same defect at full strength.

⭐ **The retained evidence is genuine, not asserted.** `06_MANUAL_BACKTEST/V17/data/pt045_output_reading1.txt`
carries, in all four cells, `N3_p_run_ge3_matched  0.0` and `verdict_S  CONTRADICTED AS STATED`.
**A matched-random control returning exactly zero four times is the tell, and it is the pre-registered
control that fired.** `S2` is honest and the near-miss was real.

### ⭐ THE HOMEWORK — RECOMPUTED INDEPENDENTLY, AND BOTH HEADLINE NUMBERS HOLD

Own code, own Asian-box construction (`C-2`, `20:30 → 03:00`), same window `2013-01-06 → 2016-06-30`:

| Measure | reviewer arm A | submission arm A | reviewer arm B | submission arm B |
|---|---|---|---|---|
| **fraction passing `Asian range < 50 pips`** | **0.8512** | **0.8509** | **0.8893** | **0.8931** |
| median Asian-box range | **33.2** pips | 33.1 | **29.6** pips | 29.3 |
| IQR | `24.7 – 43.9` | `24.7 – 43.8` | `22.1 – 39.5` | `21.9 – 39.3` |
| fraction cutting either box edge | **0.9966** | 0.9967 | **0.9974** | 0.9978 |
| median downward extension | **25.5** pips | **25.5** | 29.2 | 27.0 |
| either extension inside `25–50` | **0.3635** | 0.3648 | 0.3552 | 0.3608 |
| in-band rate, passing vs failing | 0.3666 / 0.3459 | 0.3673 / 0.3507 | 0.3575 / 0.3372 | 0.3616 / 0.3542 |
| §3 median (today's low − yesterday's low) | **−2.2** pips | −2.8 | −5.1 | −2.9 |
| §3 either `25–75` | **0.4289** | 0.4243 | 0.4265 | 0.4214 |

⭐⭐ **`Asian range less than 50pips` passes 85.1% of GBP/USD days on arm A and 88.9% on arm B.**
The submission's *"85–89%"* is confirmed. **It is not a filter**, and the downstream rate moves by
**2.1 / 2.0 percentage points** here against the submission's 1.6 / 0.7 — the same finding, slightly
larger, and the conclusion is unchanged.

⭐ **The 2-of-7 completion is upheld on inspection of the printed key itself.** The slide
`V17_00-24-45_…png` was read off the pixels: `1. Visible Trap Yesterday (PFL) LOW` · `2. Dealer
Handles The BO Traders and 200 Traders` · `3. Dealer is Trading 25 to 75 pips off Y-LOD` ·
`4. Dealer Cuts the Asain Range as a visible stop hunt` *(printed typo preserved)* · `5. MM throws a
spike and comes above for 1 hour` · `6. W -TDI Blood` · `7. Consolidation TP`. **Points 3 and 4 are
the only two that reduce to a measurement without passing through `A-010`, `A-011`, `A-084`,
`A-097` or an undefined `consolidation`.** The homework's triage is correct.

### ⭐⭐ `C-023`'s EXPLANATION AND `C-024` — BOTH CONFIRMED FROM SOURCE

Third-engine ASR over `07:50 – 09:05`, verbatim:

> *"One of the biggest questions were my pivots don't match the pivots that you have on the chart.
> Yes, and here's the reason why. **When you measure the 24-hour period on a daily candle, that
> candle closes at 5 p.m.** Our indicator is designed to take the pivots **around 12, 1 o'clock in
> the morning, depending on your dealer and what his GMT offset is,** and recalculate the 24-hour
> period so the pivots are freshly put in place right before the London Open. **Late Asia going into
> London.** That's why that's set up like that, and **that's why your pivots will not match.**"*

**Every load-bearing element of the V17 addendum to `C-023` is confirmed**: the daily candle's
`5 p.m.` close, the indicator's separate re-cut, the dealer-GMT-offset qualifier, the *"right before
the London open"* purpose, and the fact that he treats the *difference* as the answer. ⭐ The
committed transcript's *"that can look closes at 5 p.m"* is an ASR garble for *"that candle closes
at 5 p.m."*; the records **quote it verbatim rather than smoothing it**, which is the right
handling, and the gloss is correct.

**The downgrade-not-closure is right.** V17 explains *why the numbers differ*; it does not say which
basis is normative, and it replaces a two-way fork with a broker parameter (`A-107`). `A-107` is
correctly built and correctly marked `DO NOT CODE`.

**`C-024`'s printed side is confirmed off the pixels.** `V16_00-14-25_…png` prints, under the
running title `Pivot Points`: **`London Session Start`** / **`2:00 To 3:00 AM, EST`**. The gap
against *"around 12, 1 o'clock in the morning"* is real, and the record's own reading — **two
clocks, neither anchored to the other** — is the correct one. ⭐ **This is the corpus's first
cross-lesson contradiction and it is filed at the right severity.**

⚠ **One unmarked inference rides inside the gloss.** Five files render the daily-candle close as
*"17:00 **dealer time**"*. **The source attaches no clock to `5 p.m.` at all**; the only clock
attribution in the passage — *"depending on your dealer and what his GMT offset is"* — belongs to
the **indicator's re-cut**, not to the candle. The inference is defensible but it is presented as
description, in exactly the record class where clock attribution is the load-bearing thing.
`MINOR` item 248.

### ⭐⭐ `C-027` — CONFIRMED ON A THIRD ENGINE. THE RETRACTION IS CORRECT AND THE TRANSCRIPT IS FAITHFUL

The submission's `S1` retracts its own first-commit headline: it had claimed `[00:21:10]`'s *"G U"*
was an ASR mishearing of *"G J"*, then withdrew it when its own pre-committed ASR pass rendered
`GU`. This review did not take the retraction on trust.

Third-engine ASR over `20:35 – 22:10`:

> `[20:37]` *"**Pound yen**, the second one, was a better trade."*
> `[20:54]` *"**GU**, pound dollar, we'll look at it in a second, uses one bar to confirm and shift…"*
> `[21:06]` *"All right, this is **GU**, safety trade."*
> `[21:50]` *"Now, this is **pound yen**."*

and, for contrast, at `[56:59]`: *"**G.J.** Safety confirmed a close above the mayonnaise and ketchup
or ketchup and mustard."*

**`GU` twice, on a third engine, in two separate sentences.** And the frame
`V17_00-21-10_…png` was opened and read: its MT4 header is **`GBPJPY,M15 128.848 128.876 128.760
128.813`**, burned-in timecode `21:10 / 57:1`.

⭐⭐ **The retraction is right and it is the correct call.** The transcript is faithful; **the speaker
misnamed his own chart**, and named it correctly forty seconds later. `C-027` is filed at the right
severity, and the derived suspicion the session also withdrew — that the transcript *"has at least
one currency-pair error… assume there are others"* — was correctly withdrawn: this review found
none.

### ⭐⭐ `A-010` AND `A-011` — NEITHER CLOSES, AND ONE OF THE TWO QUOTES IS WRONG

**`A-011` is confirmed verbatim.** Third engine, `[28:09]`–`[28:11]`: *"But you don't have a W in
price. **You have a W in the closing of price**, which is pretty good."* The record's *"It's pretty
good"* against *"which is pretty good"* is immaterial. **ADVANCED, NOT CLOSED is correct** — a
series is not a shape test.

**`A-010`'s number is confirmed and its quote and its production mode are not.** Third engine,
`[34:55]`–`[34:58]`:

> *"Okay, **how many candles does it take** to form a good M&W? **On a 15-minute chart, eight
> candles or above is a good solid M or W**, okay?"*

Three things follow. **(1)** *"eight candles or above"* is a **single contiguous utterance**, not a
reconstruction across a marker boundary — the record's reading is not merely defensible, it is
**stronger than the record claims**. **(2)** The committed transcript's *"how many **tails** that
take"* is an ASR error for *"how many **candles** does it take"*, and `A-010`'s addendum quotes the
error verbatim as though it were the source. **(3)** The addendum characterises the statement as
*"a two-word answer from the floor"* delivered *"answering a student"*, and links it to `C-025`'s
production mode. **It is neither.** It is the instructor posing his own question and answering it in
one continuous sentence, with the timeframe stated inside the answer. **The production mode is
stronger than the record credits, and the record uses the weaker characterisation as a reason not to
close.** `MINOR` item 245.

⭐ **`A-010` still does not close**, and this review agrees with that conclusion on the correct
evidence: no depth, no symmetry tolerance, and no statement of whether *"eight"* counts the whole
formation or one leg.

### ⚠⚠ `[00:11:22]` — THREE ENGINES SAY *"an extra WEEK in between"*, NOT *"an extra WEEKEND between"*, AND ITEM 238's INFERENCE INVERTS

Item 238 was `PUT TO R1`, asking a reviewer to decide whether V17's week count bears on `A-01`'s
missing Week 6. It reasons from a quoted phrase. **The phrase is misheard.**

| Engine | Rendering of `[00:11:22]` |
|---|---|
| committed transcript (student's pass) | *"Actually nine because we took an extra **weekend** between"* |
| `faster-whisper large-v3` (this review) | *"actually nine because we took an extra **week in between**"* |
| `openai-whisper medium.en` (this review) | *"actually nine because we took an extra **week in between**"* |
| `openai-whisper large-v3-turbo` (this review) | *"actually nine because we took an extra **week in between**"* |

**Three independent engines, unanimous, against one.** And the reading changes the conclusion:

* On *"extra **weekend**"*, item 238 reasons that nine **sessions** against a week-label of eight is
  *"consistent with an extra session rather than a missing one, which is a DIFFERENT shape from
  `A-01`'s gap"*.
* On *"extra **week in between**"*, the arithmetic runs the other way: **nine calendar weeks
  carrying eight sessions means one week with no session** — which is **exactly `A-01`'s shape**,
  and it is corroborating, not contrasting, evidence.

**This review answers item 238 rather than returning it.** `MINOR` item 244; the disposition is
below in §5.

### `Q-018` — RE-HASHED AND RE-DIFFED, THE SUBSTANCE CONFIRMED, ONE COUNT WRONG, AND THE PATTERN SOLVED FOR THE REST OF THE COURSE

All three V17 files re-hashed here and **matching** the register's recorded SHA-256s. The diff was
re-run in this review's own shell:

| Pair | reviewer | `Q-018` |
|---|---|---|
| V16→V17 `NOTES.md` | **2 differing lines = 1 changed pair** | 2 lines = ONE pair ✅ |
| V16→V17 `VISUAL_INDEX.md` | **8 differing lines = 4 changed pairs** | 8 lines = FOUR pairs ✅ |
| V16→V17 `RULES.md` | **10 differing lines = 5 changed pairs** | ⚠ *"12 differing lines = SIX changed pairs"* ❌ |

⭐ **The substance is confirmed: ZERO content lines differ in any of the three files.** The only
changes are the `.swf` filename, `V17-R001/R002 → V18-R001/R002`, and three screenshot filenames.
**Item 236 is right and item 221's forward prediction is falsified** — a byte-`diff` against the
immediately preceding lesson flags V17 in one command.

⚠ `Q-018`'s `RULES.md` count is **one pair too high, and its own enumeration lists five** (*"the
`.swf` filename, `V17-R001/R002 → V18-R001/R002`, and two visual filenames"* = 1 + 2 + 2 = 5).
`MINOR` item 249 — the same class as V16 R1's item 225, in the same register, one lesson later.

⭐⭐ **AND THE PATTERN IS NOW SOLVED FOR THE WHOLE COURSE.** This review diffed **all 21 trios
pairwise**, which no prior round has done:

```text
14→15  NOTES  6   RULES 12   VISUAL_INDEX  8      (near-clone)
15→16  NOTES 32   RULES 30   VISUAL_INDEX 26      <-- PARAPHRASE
16→17  NOTES  2   RULES 10   VISUAL_INDEX  8      (byte clone)
17→18  NOTES  2   RULES 10   VISUAL_INDEX  8      (byte clone)
18→19  NOTES  2   RULES 10   VISUAL_INDEX  8      (byte clone)
19→20  NOTES  2   RULES 10   VISUAL_INDEX  8      (byte clone)
20→21  NOTES 32   RULES 30   VISUAL_INDEX 26      <-- REVERTS
15 vs 21  NOTES 6   RULES 12   VISUAL_INDEX 8     (V21 is template A again)
```

**There are exactly TWO content templates in the 63-file set.** Template **A** covers lessons
**1–15 and 21**; template **B** covers lessons **16–20**. **V18, V19 and V20's trios are byte clones
of V17's; V21's reverts to the V15-and-earlier text.** `Q-019`, `Q-020`, `Q-021` and `Q-022` are
therefore **answered in advance** — see `NOTE` item 254.

---

## §3 — FINDINGS

### `CRITICAL` — **NONE**

### `MAJOR` — **NONE**

Weighed and rejected: item 244 was weighed for `MAJOR` because it inverts a stated inference. It is
charged `MINOR` because the inference was **explicitly put to the reviewer rather than asserted as
settled**, it touches a calendar/provenance record and no methodological rule, and it is answered in
this round rather than left open.

### `MINOR`

| # | Finding |
|---|---|
| **244** | ⚠⚠ **`[00:11:22]` IS MISHEARD, AND ITEM 238's INFERENCE INVERTS ON THE CORRECT WORD.** Three independent engines render *"we took an extra **week in between**"*; the committed transcript and every record built on it read *"an extra **weekend** between"*. Item 238 reasoned that nine-against-eight is *"consistent with an extra session"* and so a **different shape** from `A-01`'s gap. On the correct word it is **nine calendar weeks carrying eight sessions — one week with no session — which is `A-01`'s shape exactly.** **Fix:** add the correction to `V17_TRANSCRIPT.md` §5's correction table (the body is not edited, per its own rule); amend item 238, `V17_SOURCE_NOTES.md` §12 and `COURSE_PROGRESS.md`'s V17 narrative and progress-table row; and record in `SOURCE_MANIFEST.md` `A-01` that **V17 supplies contemporaneous first-person corroboration of a skipped week.** |
| **245** | ⚠ **`A-010`'s V17 ADDENDUM QUOTES AN ASR ERROR AS SOURCE AND UNDERSTATES ITS OWN EVIDENCE.** The addendum quotes *"how many **tails** that take to form a good M and W on a on a 15-minute chart"*; three engines give *"how many **candles** does it take to form a good M&W? **On a 15-minute chart,** eight candles or above is a good solid M or W."* Two consequences: the timeframe belongs to the **answer**, not the question; and *"eight candles or above"* is a **single contiguous utterance**, not a reconstruction across a marker. ⭐ **And the production-mode characterisation is wrong in the direction that weakens the record** — *"a two-word answer from the floor"*, linked to `C-025`, when it is the instructor's own question answered by himself in one sentence. **Fix:** correct the quote, drop the `C-025` production-mode link, and restate the reason `A-010` does not close as **no depth, no symmetry tolerance, and no leg-vs-whole statement** — which is sufficient on its own. |
| **246** | ⚠ **THE GATE-TIMING ADDENDUM IS FACTUALLY WRONG ON THE COMMIT GRAPH — AND IN THE SUBMISSION'S FAVOUR.** `245c756` states V16's R1 *"RETURNED after this session's last content commit"* and that it *"had not returned at any point during this session's work"*. `0fee48c` (17:16:53) precedes `f55c2f3` (17:20:11) and all eight V17 content commits. The belief was honest — the worktree could not see integration — but the paragraph asserts a checked fact that was not checked. **Fix:** correct the addendum in `COURSE_PROGRESS.md`, `V17_MASTERY_REPORT.md` §0a and `LOG.md` to *"V16's R1 landed on integration at `0fee48c` 17:16:53, before this session's first content commit; the session did not see it and worked as though the gate were closed"*, and retire the *"second consecutive lesson on unreviewed ground"* framing as **not true of V17's committed work**. |
| **247** | ⚠ **ITEM 239's SCOPE IS OVERSTATED, AND THE COUNTEREXAMPLE IS INSIDE THE SAME SUBMISSION.** Item 239 says arm B's ~25% exclusion is *"a property of `mmm_lib`'s completeness rule that other `PT-` tests inherit"* and *"reaches past `PT-045` into every test"*. It is a property of the **`load_m1` path**, where the arm shift is applied to raw M1 timestamps and misaligns the 96-bucket census. Confirmed here both ways: this review's own M1 build excludes **244** arm-B days (`PT-045` reports 246); `L.load_m15` + `L.build_days(require_full=True)` excludes **6** — and `hw_v17.py`, in the same submission, reports **898 (6 excluded)** on arm B against 899 on arm A. **Fix:** narrow item 239 to the `load_m1` path, name `load_m15` as unaffected, and state which prior `PT-` tests use which loader so the inherited-risk claim is scoped rather than universal. |
| **248** | ⚠ **`"17:00 dealer time"` IS AN UNMARKED INFERENCE, IN FIVE FILES, IN THE RECORD CLASS WHERE THE CLOCK IS THE LOAD-BEARING THING.** The source says only *"that candle closes at 5 p.m."* The dealer/GMT qualifier attaches to the **indicator's** re-cut. `C-024`'s whole argument is that V17's clock and V16's `EST` slide are **unanchored to each other**; silently anchoring the `5 p.m.` figure to *"dealer time"* is the move that record says cannot be made. **Fix:** mark it `[INFERRED]` in `CONTRADICTIONS.md` (`C-023` addendum), `V17_SOURCE_NOTES.md` §2, `V17_MASTERY_REPORT.md` §4, `COURSE_PROGRESS.md` and `LOG.md`; leave `A-107`'s *"00:00–01:00 dealer time"* alone, where the qualifier **is** in the source. |
| **249** | **`Q-018`'s `RULES.md` DIFF COUNT IS WRONG, AND THE ENTRY'S OWN ENUMERATION CONTRADICTS IT.** Re-run here: **10 differing lines = 5 changed pairs**, against the recorded *"12 differing lines = SIX changed pairs"*. The entry then lists five (`.swf` filename, two rule IDs, two visual filenames). Every substantive claim — **zero content lines differ, in all three files** — is confirmed. **Fix:** correct the count. Same class as item 225, same register, one lesson later; **item 188's duplicate/count validator check is still unbuilt and would have caught both.** |

### `NOTE` — no action required

| # | Note |
|---|---|
| **250** | ⭐⭐ **`PT-045` INDEPENDENTLY RE-DERIVED FROM ITS PRE-REGISTRATION AND IT REPRODUCES.** Reviewer code written from `PT-045` §§3–6 **before `run_pt045.py` or `mmm_lib` was opened**; own CSV parser, own session-day builder, own completeness census, own arm shift, own shuffle null. **Arm A reproduces every reported figure to four decimal places** — `n_rev` 117 / 288, median run 2 / 1, `P(2..4)` 0.4957 / 0.4132, `P(≥3│rev)` 0.2906 / 0.2465, unconditional 0.2715 / 0.2689, `O6` +58.99 / +48.62. Arm B reproduces every **verdict**. |
| **251** | ⭐⭐ **THE `S2` ARTEFACT RE-EXECUTED, AND IT IS AS DANGEROUS AS THE SUBMISSION SAYS.** Calendar-consecutive run continuation returns **median run 1 in four cells of four** → `CONTRADICTED AS STATED` four times, a clean refutation of V17's three-day cycle. A stricter calendar reading returns **zero** reversal windows. And `pt045_output_reading1.txt` genuinely carries `N3 = 0.0` in all four cells — **the pre-registered control is what fired, exactly as claimed.** ⭐ The general lesson is worth carrying: *"consecutive"* is a trap in any multi-day FX test, and a control that can return an impossible value is what makes it survivable. |
| **252** | ⭐ **THE HOMEWORK'S TWO HEADLINE NUMBERS REPRODUCE.** `Asian range < 50pips` passes **0.8512** (arm A) and **0.8893** (arm B) here against **0.8509** / **0.8931**; median Asian box **33.2** / **29.6** against 33.1 / 29.3; cut-either-edge **0.9966** against 0.9967; **median downward extension 25.5 pips exact**. The downstream-rate delta is **2.1 / 2.0 points** here against 1.6 / 0.7 — larger, same conclusion. **The filter is inert on GBP/USD and `A-112` is correctly the place it lives.** |
| **253** | ⭐ **THE 2-OF-7 TRIAGE IS UPHELD FROM THE PIXELS.** All seven printed points read off `V17_00-24-45_…png`, printed typo `Asain` included. Points 3 and 4 are the only two reducible to a measurement without passing through `A-010`, `A-011`, `A-084`, `A-097` or an undefined `consolidation`. ⭐ **The most complete printed checklist in the corpus yields the least computable one** — that observation is correct and it is the right thing to have noticed. |
| **254** | ⭐⭐ **THE FABRICATION PATTERN IS SOLVED FOR THE WHOLE COURSE, AND `Q-019`–`Q-022` ARE ANSWERED IN ADVANCE.** All 21 trios diffed pairwise here. **There are exactly two content templates**: **A** for lessons 1–15 **and 21**, **B** for lessons 16–20. **V18, V19 and V20's trios are byte clones of V17's** (`NOTES` 2 / `RULES` 10 / `VISUAL_INDEX` 8 differing lines, all identifier-only); **V21's reverts to template A** and matches V15's at the 6/12/8 level. ⚠ **So neither *"the generator paraphrases"* nor *"the generator clones"* is the rule** — it does both, and the **invariant** is the only stable key, exactly as `Q-018` concludes. A V18 session should quarantine on sight, cite this note, and **spend no session time re-deriving it**. |
| **255** | ⭐ **SOURCE AND TRANSCRIPT INTEGRITY REPRODUCE EXACTLY.** `.swf` SHA-256 **`2281fa8b…07f767`** and **20,210,746 bytes** re-computed and matching; audio **3,429.64 s**. The committed 690-marker body is **byte-identical** to the pre-ingestion `TRANSCRIPT.md` body (reviewer SHA-256 `768ebf76…`), confirming the *"copied byte-for-byte"* claim. **690 markers, strictly monotonic, zero equal-adjacent pairs, zero backwards steps, gaps 1–12 s (mean 4.97 s), last marker 2.6 s before the measured end of audio** — every figure in the header table reproduces. |
| **256** | **THE WORD COUNT IS 8,862, NOT 8,870 — AND NOTHING RESTS ON IT.** Whitespace tokenisation over the 690-marker body returns **8,862** against the committed **8,870**, a 0.09% difference and plainly a tokenisation convention. Recorded only because the same class of discrepancy was item 230 one lesson ago and a reader should know it was checked. |
| **257** | ⭐ **FRAME TIMECODES AND PRINTED TEXT SPOT-CHECKED ON SIX FRAMES; ALL HOLD.** `V16_00-14-25` (`London Session Start / 2:00 To 3:00 AM, EST`), `V17_00-14-15` (flashcard, burned-in `14:14`), `V17_00-21-10` (`GBPJPY,M15`, burned-in `21:10`), `V17_00-24-45` (seven-point key, `24:45`), `V17_00-42-10` (`Trend Is Generally Setup As A 3 Day Cycle.` and the `News Is Use` typo, `42:10`), `V17_00-51-00` (`(Mayo ,Blue Berry)`, `The Reset Will Represent A New Peak Formation`, `3 More Days Can Be Expected.`, `However, If No One Falls For It…`, `51:00`). **All within the ±1 s the session itself declared**, and `A-113`'s *"ADR nearly filled(close enough)"* confirmed on the flashcard. |
| **258** | **`O6` ARM B `W-D` DIFFERS BETWEEN THIS REVIEW AND THE RUNNER, AND IT ENTERS NO VERDICT.** Reviewer **+66.9 pips**, submission **+79.79**, on samples differing by one reversal (106 vs 107). `BT_V17_0001` §6c already declares `O6` **partly tautological** and excludes it from every verdict. Recorded so a later session does not discover the gap and read it as a defect; **arm B's day set is convention-sensitive by construction** and item 247 is where that lives. |
| **259** | ⭐ **THE §6 DECISION-TABLE HOLE IS REAL AND WAS HANDLED CORRECTLY.** This reviewer's own `W-D` cells fall through **all four** pre-registered branches. The submission found it, reported it as *"a defect in my own decision table"*, returned `INDETERMINATE` as the only remaining branch, and **did not edit the pre-registration**. That is `COMMON_PROTOCOL.md` §9 rule 7 applied against the session's own interest. |
| **260** | ⭐⭐ **CALIBRATION — THE BEST DECISIONS IN THIS SUBMISSION ARE THE NEGATIVE ONES.** (1) `PT-045` §7 `P3` **predicts its own headline test will fail**, and the mechanism it names is exactly what `O1` shows. (2) §1b names **four of V17's five most interesting claims as untestable, before the run**, so a modest result on two peripheral claims cannot be read as a verdict on the lesson. (3) The independent ASR pass was **queued and committed at `f55c2f3` before the answer was known**, and it is the only reason `S1` is a retraction rather than a fact in the record. (4) `PT-045` §9 flagged in advance that `C-1`'s 17:00 boundary is the project's convention and not V17's — the same class of hidden dependency `A-107` names. **Four pre-commitments, three of which cost the session something.** |
| **261** | **THE `D-047` RENUMBERING WAS RE-DERIVED, NOT TRUSTED, AND THE HANDED-OVER MAPPING IS CORRECT.** `video/v17` allocated **201–208** against integration's pre-`review/v15` state; `cd6d1cb` then took 189–215 and `0fee48c` took 216–235. V17 is the later arrival, so **201–208 → 236–243** and every V16 item cited inside the V17 set shifts **+21** (197→218, 198→219, 199→220, 200→221; **188 is a V15 item and is unaffected**). Applied at this merge per `D-047` 4. ⭐ **The session anticipated the collision and handed over the mapping in `V17_MASTERY_REPORT.md` §0b** — re-derived here and correct. ⚠ **THIRD consecutive collision of this exact shape** (item 214, item 227, this) and **item 188's validator check is still unbuilt**. |
| **262** | **THE V17 PROGRESS-TABLE ROW IS STALE AGAINST THE NARRATIVE BLOCK ABOVE IT.** `COURSE_PROGRESS.md`'s row still reads *"OPENED WITH ITS `D-004` GATE CLOSED — V16's R1 HAS NOT RETURNED… SECOND CONSECUTIVE LESSON ON UNREVIEWED GROUND"* while the narrative block twenty lines earlier carries the addendum discharging it. This is the **status-staleness class, open item 14**, and item 246's fix should sweep the row at the same time. ⚠ Also unrepaired at the repository level: a **broken Git ref** `refs/heads/review/v16 2` (a filesystem-copy artefact) makes `git log --all` and `git branch -a` fail with `fatal: bad object`. **Not touched by this review** — deleting a ref is the owner's call. |

---

## §4 — AUDIT DIMENSIONS (`REVIEW_PROTOCOL.md` §6)

| Dimension | Grade | Basis |
|---|---|---|
| **A. Source fidelity** | ⚠ **MINOR ISSUE** | Three defects, all quotation-level: item 244 (a misheard word carrying an inverted inference), item 245 (an ASR error quoted as source, and an understated production mode), item 248 (an unmarked inference in five files). ⭐ Against these: `C-023`'s whole passage, `C-024`'s printed slide, `C-027`'s `GU`, `A-011`'s `W`-in-closes and `A-113`'s flashcard line all confirmed **verbatim on independent evidence**. |
| **B. Completeness** | ⭐ **PASS** | The three-day cycle reconstructed day by day from printed slides plus narration; the reset/reversal layer on top; two **non-entry** conditions captured (`A-115`, the corpus's first); the cycle length recorded as a **distribution he never bounds** (`A-121`) rather than smoothed to 3. |
| **C. Provenance** | ⭐ **PASS** | Source hash, byte length and duration all reproduce. Transcript body **byte-identical** to the pre-ingestion file. Every load-bearing quotation machine-checked at its own marker. Frame timecodes hold on six independent reads. |
| **D. Explicit vs inferred** | ⚠ **MINOR ISSUE** | `[AUDIO]`/`[PRINTED]`/`[VISUAL]` tagging is applied throughout and is `grep`-falsifiable. Item 248 is the exception, and it is the one place the distinction was load-bearing. |
| **E. Chart recognition** | ⛔ **BLOCKED BY `D-030`**, ninth consecutive lesson — excluded from pass/fail per owner directive. Item 36 (the project has no vocabulary for this disposition) still owed. |
| **F. Homework** | ⭐ **PASS** | Real checksummed data, both arms, scope limits declared **before any number**, and the sharpest finding in the submission. Recomputed independently here and it holds. |
| **G. Manual backtesting** | ⭐ **PASS** | Pre-registered before the runner existed, never edited; two windows, two arms, four controls, a volatility-matched null; **2½ of 6 predictions with the misses reported first**; two self-caught process defects and a self-declared hole in its own decision table. ⚠ `D7` — the runner was executed before it was committed, against the `PT-044` precedent. |
| **H. Hindsight / lookahead** | ⭐ **PASS** | No lookahead found. The reversal definition is fixed in `§3` before any bar is read and is **not retuned after the result**; the superseded reading is **retained and printed** rather than replaced. |
| **I. Ambiguity handling** | ⭐ **PASS** | Nineteen opened, eight amended, one closed **as a transcription question only**. ⭐ *"Nineteen opened against eight advanced is the finding"* is the right thing to say about this lesson. `A-107` is correctly identified as the most consequential and correctly marked `DO NOT CODE`. |
| **J. Contradictions** | ⭐ **PASS** | Four filed, including the corpus's **first cross-lesson** contradiction; `C-023` **downgraded, not closed**, with the reason it cannot close stated. |
| **K. Research integrity** | ⭐⭐ **PASS — the strongest dimension in this submission** | A pre-committed check overturned the session's own headline claim and the retraction is carried in four artifacts with the original text struck and retained; a pre-registered control caught a publishable-looking false refutation; a reproducibility defect in the session's own runner was found and disclosed; and the `D-004` gate was declared rather than glossed. **Item 246 is a factual error inside that declaration, not a failure of the practice.** |

---

## §5 — REQUIRED CORRECTIONS

1. **Item 244** — apply the `[00:11:22]` correction (*"an extra **week in between**"*) to
   `V17_TRANSCRIPT.md` §5's correction table; **do not edit the 690-marker body.** Amend item 238,
   `V17_SOURCE_NOTES.md` §12 and `COURSE_PROGRESS.md`. **Item 238 is answered, not returned:**
   ⭐ **V17's *"eight weeks, actually nine because we took an extra week in between"* is
   contemporaneous first-person corroboration that a week was SKIPPED, which is `A-01`'s shape.**
   Record it in `SOURCE_MANIFEST.md` `A-01` as **supporting evidence, not as a closure** — it fixes
   the *shape* of the gap, not its *date*.
2. **Item 245** — correct `A-010`'s V17 addendum quote to *"how many candles does it take to form a
   good M&W? On a 15-minute chart, eight candles or above is a good solid M or W"*, drop the
   `C-025` production-mode link, and restate the non-closure reason.
3. **Item 246** — correct the gate-timing addendum in `COURSE_PROGRESS.md`,
   `V17_MASTERY_REPORT.md` §0a and `LOG.md`; retire the *"second consecutive lesson on unreviewed
   ground"* framing as not true of V17's committed work.
4. **Item 247** — narrow item 239 to the `load_m1` path and name `load_m15` as unaffected.
5. **Item 248** — mark *"17:00 dealer time"* `[INFERRED]` in all five files. Leave `A-107`'s
   *"00:00–01:00 dealer time"* unchanged.
6. **Item 249** — correct `Q-018`'s `RULES.md` diff count to **10 lines / 5 pairs**.

**None of these is a prerequisite for V18 work** (`D-024`). All six are prerequisites for V17
reaching `COMPLETE`.

---

## §6 — REVIEWER QUESTIONS FOR THE OWNER

1. ⚠ **Item 185's gap audit is STILL NOT DISCHARGED**, and V17 says so itself. It has now survived
   V14, V15, V16 and V17. **This review does not discharge it either** and flags that four
   consecutive rounds have passed it forward.
2. **Item 188's duplicate-identifier / count validator is still unbuilt**, and it would have caught
   item 249 and V16's item 225 — the same defect, in the same register, one lesson apart — as well
   as pre-empting the **third consecutive** `D-047` collision (item 261). **Recommend it be built
   before V18.**
3. **A broken Git ref `refs/heads/review/v16 2` breaks `git log --all` repository-wide** (item 262).
   Deleting a ref is not this review's call; **one command from the owner clears it.**
4. **Item 36** — the project still has no vocabulary for a dimension that is `BLOCKED BY D-030` and
   excluded from pass/fail. Ninth consecutive lesson.
5. ⚠ **SELF-CHARGED, item 263 — this reviewer's own `git add -A` in commit `0cd31a5` swept 614
   files from four pre-existing untracked trees into the review commit.** They were removed from the
   index in the following commit and are untracked again, exactly as at session start; history was
   **not** rewritten. ⛔ **Whether `19_STUDENT_TEST_SUITE_V01_V10/`,
   `20_CHART_HEAVY_PRACTICAL_V01_V10/`, `21_EXTREMA_SIGNATURE_TRADE_PRACTICAL_V01_V10/` and
   `06_MANUAL_BACKTEST/tools/` SHOULD be committed is the owner's call and is deliberately left
   open.** It does not touch the V17 verdict.

---

## §7 — ADVANCEMENT

```text
LESSON: V17
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES: none
MAJOR ISSUES:    none
MINOR:           6   (items 244-249)
NOTE:           13   (items 250-262)

SELF-CHARGED:    1   (item 263 -- this reviewer's own staging error, not a
                     finding against the submission; PUT TO THE OWNER)

V18 GATE: OPEN under D-024 -- zero CRITICAL, zero MAJOR.
V17 STATUS: IN REMEDIATION. NOT COMPLETE until items 244-249 are applied and verified.

ADVANCEMENT: AUTHORIZED for V18. NOT a PASS for V17.
```

⭐ **Closing assessment.** This is the strongest research-integrity performance in the corpus to
date. Two of the submission's own most confident outputs — a transcript correction and a four-of-four
refutation of the lesson's central claim — were **destroyed by checks the session committed in
advance**, and both destructions are in the record with the original text retained. Every
quantitative claim this review could re-derive, it re-derived, and `PT-045`'s arm A reproduces to
four decimal places from code that shares no line with the runner.

⚠ **And the six minors have a shape worth naming: five of the six are quotation or bookkeeping
defects, and three of those five would have been caught by a check the project already knows it
needs** — an independent ASR arbitration extended past the *queued* passages (items 244, 245) and
the validator of item 188 (items 249, 261). **The session's method is sound; its coverage of that
method is not yet complete.**
