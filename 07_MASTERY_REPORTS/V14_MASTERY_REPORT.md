# V14 — MASTERY REPORT

`Bootcamp1 Wk5 041512 Part2 (48mins).swf` · 2012-04-15 · **Part 2 of V13's session** ·
course author 100% · branch `video/v14`, worktree `MMM-Agents-v14` (`D-038`).

---

## 1. WHAT V14 IS, IN ONE PARAGRAPH

**V14 is the lesson V13 promised twice and deferred, and it arrives.** It has two halves: a candle
taxonomy in which every formation is read as **the footprint of work already done**, and then the
week's assignment — **the high/low board drill**, a printed six-step procedure for identifying the
day's extreme **in real time, from the price board, with no chart at all**. ⭐ **It is the most
completely specified method in the corpus to date**: six of its seven steps are arithmetic, which
is why V14 supports a pre-registered test where most lessons cannot.

---

## 2. ⚠️ DECLARED DEVIATIONS AND SELF-CORRECTIONS — READ BEFORE THE FINDINGS

**Five deviations and two self-corrections. All are recorded in the artifact a reader hits first,
not in a footnote.**

| # | Kind | What |
|---|---|---|
| **`D1`** | Deviation | **`SWF_CAPTURE_RECIPE.md` §9 ordering broken** — frames were opened before `V14_SOURCE_NOTES.md` was written. **Mitigation:** every source-note item carries `[AUDIO]`/`[PRINTED]`/`[AUDIO+PRINTED]`, falsifiable by `grep`, and every load-bearing conclusion is `[AUDIO]` or `[AUDIO+PRINTED]`. Disclosed in `V14_SOURCE_NOTES.md` **§0, before §1** |
| **`D2`** | Deviation | **The homework as set cannot be performed and a faked version was not written.** Both halves are live-market two-week exercises; the TDI half is additionally **BLOCKED** by `A-084`/`A-085`/`A-086`. Substituted with `PT-042`. Disclosed in `V14_HOMEWORK.md` §0 |
| **`D3`** | Deviation | ⭐ **A forward `grep` into V15's supplied transcript**, for week-number statements only, to settle `A-092`. **A corpus-level string check, not an ingestion** — no V15 artifact created, V15 gate untouched. Disclosed in `V14_INTERPRETATION.md` Q1 **at the point of use** |
| **`D4`** | Deviation | **`PT-042`'s `N1` control had its `O1` construction underspecified**, and `run_pt042.py`'s choice **flatters the rule arm**. Direction stated, magnitude given, amendment owed. `BT_V14_0001.md` §3a |
| **`D5`** | Deviation | **`PT-042`'s `N4` control is degenerate (`n = 0`)** — the contrast the pre-registration called *"the comparison that matters"* does not exist. `BT_V14_0001.md` §2b |
| **`S1`** | Self-correction | **Four sites said V12→V14 was *"five weeks"*. It is ONE week** (2012-04-08 → 2012-04-15). Corrected before the records commit; **the correction strengthens `C-021`**, since a one-week separation is a tighter contradiction than a five-week one |
| **`S2`** | Self-correction | **The frame-scan accounting was asserted as *"48 whiteboard / 2 title / 4 stray"* and re-measured as *"50 / 2 / 2"* in four contiguous runs.** Corrected in `V14_INTERPRETATION.md` Q3a before commit |
| **`S3`** | Self-correction | **Term counts for `A-002` were asserted as `trap ×7 / stop hunt ×4` and measured as `trap ×4 / stop hunt ×3` (+1 ASR variant).** Corrected in the record before commit |

⭐ **`S1`–`S3` were all caught by running the check rather than trusting the draft**, which is the
behaviour `REMEDIATION_PROTOCOL.md` §2 exists to produce. They are left visible.

---

## 3. THE FINDINGS, RANKED BY WHAT THEY CHANGE

### 3.1 ⭐⭐ `A-056` — a seven-lesson-old Required Research is ANSWERED

`A-056` asked: *"Whether any later lesson — or 'Jim' in any recording in this library — states
**how** the day's extreme is identified before it is known."* **V14 does, and the course author
teaches it himself rather than deferring to Jim as V07 did.**

**Not marked `CLOSED`.** Step 2 of six — *"Find a pair that is trading in the middle of the range"* —
is printed, spoken, and **has no tolerance anywhere in Tier 1 or Tier 2** (`A-089`), and the
speaker's own two worked examples sit at the **45.5th** and **20.0th** percentile of their ranges.
**A method with an undefined selection step is not computable**, so closure is **put to the
reviewer**, not taken by this session.

⭐ **This is the first time in the corpus that an `A-039`-shaped record — load-bearing component,
never defined — has been answered by a later lesson rather than deferred again.**

### 3.2 ⭐ `A-077` — the missing lock threshold arrives, PRINTED, at the wrong scale

`A-077` refused an inferred candidate and noted *"**N** and **M** appear in no lesson and in no
`MMM-NOTES` page."* **V14 supplies both** — `N` = **1 hour**, printed on the assignment slide;
`M` ≈ **15 pips** — and uses `A-077`'s own word, `[00:35:51]` *"you're looking for **the lock**"*.

⚠️ **It does not close `A-077`.** V14's lock is on a **session** extreme at **1 hour**; V10's is on a
**weekly** extreme at *"15, 16 hours"*. **Same word, same mechanism, thresholds ~10× apart, nothing
reconciles them** → `A-094`. **V14's figure must not be transplanted onto V10's safety trade** —
that is precisely the lookahead hazard `A-077` exists to prevent.

### 3.3 ⭐ `PT-042` — NOT SUPPORTED, and the failure is informative

| Measure | Arm A | Arm B | Boundary | |
|---|---|---|---|---|
| `O1` P(`L` is still the day's extreme) | **0.3461** | **0.3041** | ≥ 0.80 | ❌ **misses by 45 pp** |
| `O2` P(30 pips before the 5-pip stop) | **0.4607** | **0.4433** | ≥ 0.50 | ❌ |
| `O4` median MFE | **40.10** | **40.40** | — | ⭐ |
| `O2` vs matched-random `N1` | 0.4607 vs **0.2251** | 0.4433 vs **0.2355** | — | **100th percentile, both arms** |

**The course's premise is measurably wrong about two days in three.** But `O4` shows the **move is
there** — median 40 pips — so *"aim for 30 to 50"* is about the right size, and the trade fails
because **the 5-pip stop is too tight for the level it is attached to**, not because the move is
absent. **The same shape `PT-041` found, reached independently.**

⭐ **And the rule carries real signal**: `O2` roughly doubles matched-random entry. **`NOT
SUPPORTED` is not the same as "there is nothing here", and the record says both.**

⭐ **The lock does not select days.** `no-extension = 0` and `no-lock = 0` across 938 arm-days: over
a 16-hour window a 60-minute gap always eventually occurs. **The rule picks a time, never whether
to trade the day.** Not knowable before the run.

### 3.4 ⭐ `A-084`/`A-085`/`A-086` — one direct student question, three different effects

`[00:44:41]`–`[00:45:14]`, confirmed verbatim by two ASR engines.

| Record | Effect |
|---|---|
| **`A-084`** | ⚠️ **NARROWED, NOT CLOSED — second consecutive lesson. STAYS AN ACTIVE BLOCKER; V11's RSI threshold claims STAY BLOCKED** |
| **`A-085`** | ⚠️ **EXTENDED AND MADE WORSE** — fifth statement, flat identity phrasing, still no construction |
| **`A-086`** | ⭐ **ADVANCED on the multiplier** — *"two standard deviations"*, unhedged. ⚠️ **BASIS reverts to the retracted answer → `C-021`.** ❌ **Period still never stated, so it stays `DO NOT CODE`** |

**The `A-084` defeater, which is this session's own argument:** the answer *"Yes"* covers a
**compound** question — green = the 15-minute **and** red = the one hour. **The red half is
demonstrably a lag-gloss** (no TDI build reads another timeframe), so **the green half cannot be
taken literally from the same "Yes"**. Either the answer describes construction, in which case it
is **false for red**, or it describes felt equivalence, in which case **it says nothing about `k`**.

> ⚠️ **This is the second consecutive round in which this session's most attractive result did not
> deliver what it was hoped to deliver** — and V14 was the corpus's **best** spoken opportunity.
> `A-093` records **why**: the speaker answers what the indicator *feels like*, never what it
> *computes*, and says so himself (V12 `[00:15:40]` *"I don't know the math on it"*).

### 3.5 ⭐ `A-092` — the Week 6 question is SETTLED, and TWO artifacts are missing

`V13_REVIEW_R1.md` GATE (c) asked for the cheap decider. **The decider is the week numbering in the
next surviving file**: `Wk7 050612` opens *"Alright, **week seven**"* twice in 25 seconds. Had the
04-29 session not happened, 05-06 would have been **week six**.

**Missing from this corpus:** the **Week 6 session** (≈2012-04-29) **and the Orlando meetup
recording** (2012-04-21), which `[00:01:08]` says *"will be your boot camp for the week"*.

⚠️ **The claim is "absent from this corpus", not "never recorded".** Three defeaters are stated in
`V14_INTERPRETATION.md` Q1.

### 3.6 ⭐ `D-043` gets Tier-1 corroboration from a 2012 instructor chart

`V14_00-13-05_…png` carries four MAs with speed ordering **yellow < red < cyan < white** = exactly
`5 < 13 < 50 < 200` under `D-043`'s colours — **and inconsistent with `D-042` §2's superseded
`5 = red` / `13 = yellow`.** `D-042` §1 recorded that the mapping had thin Tier-1 support; **this is
support on the one axis a picture can carry.** ⚠️ **Ordinal, not a printed period. `A-020` does not
close.** Falsifiable: re-open the frame and check whether yellow or red is faster.

### 3.7 `Q-015` — the fabrication pattern's fourth consecutive instance, and its worst artifact

`VISUAL_INDEX.md` diffs against V13's at **8 lines = 4 changed pairs, ZERO content lines**.
⭐ **The one surviving image was opened and MEASURED: mean luminance 1.0/255, 0.32% of pixels above
60 — PowerPoint's black *"End of slide show, click to exit."* screen — indexed as *"Asian Box
accumulation range with 5, 13, 50, 200, and 800 EMAs."*** V11/V12/V13 were title cards; **a title
card at least carries pixels.**

⭐ **And the fabricated rule inverts the lesson**: `V15-R001` tells the student to trade a 5/13 EMA
cross on a closed M15 candle, attached to the one lesson that says *"do not look at candles, do not
look at TDI"* and *"there's no 15 minute, that's all bullshit, throw it out."*

---

## 4. SPEAKER — TESTED, NOT INHERITED

**100% course author, HIGH confidence, six non-acoustic strands.** `V13_REVIEW_R1.md` GATE (d)
required this be re-tested rather than carried forward. **The 17-pattern handover scan returns
ZERO** across all 600 markers, re-run in this session's own code — **V13 returned one
(*"Welcome back"*, not a handover); V14 returns none at all.**

---

## 5. WHAT V14 DOES NOT DO

| ❌ | |
|---|---|
| **`A-084` stays blocked** | And `A-093` explains why the spoken route is structurally weak |
| **Item 157 gets NO help** | ⭐ `shark` and `63` occur **ZERO** times in 600 markers. **V14 contributes nothing to the `!SM_TDI` / 63-37 provenance question** |
| **The TDI bands are still not constructible** | No period, in Tier 1 or Tier 2 |
| **`A-011` untouched for a tenth lesson** | `[00:08:11]` uses the M to **forbid** a trade and still does not describe it |
| **`A-002`/`C-006` uncompared for a tenth lesson** | ⭐ **V14 is the first lesson to use both families heavily in the SAME slide sequence and still not distinguish them** |
| **`A-004`, `A-038` unmoved** | Checked, reported as negatives |

---

## 6. SELF-ASSESSMENT AGAINST `MASTERY_STANDARD.md`

| Criterion | Grade | Basis |
|---|---|---|
| Source verified before use | ✅ | SHA-256 before **and after** the patch; 600 markers checked monotonic; three-way duration agreement to 1.33 s |
| Transcript independently checked | ✅ | `faster-whisper medium.en` on twelve passages; **seven corrections**, and **one passage left UNRESOLVED rather than guessed** |
| Notes before interpretation | ⚠️ | **`D1` — §9 ordering broken.** Mitigated by falsifiable `[AUDIO]`/`[PRINTED]` tags |
| Screenshots looked at before naming | ✅ | Contact sheet, then four frames opened at full resolution |
| Ambiguities logged, not resolved by guessing | ✅ | `A-089`–`A-094`; **`A-089` deliberately excluded from `PT-042` rather than approximated** |
| Contradictions logged, not adjudicated | ✅ | `C-021` left **OPEN — UNADJUDICATED**, three readings stated, none adopted |
| Pre-registration before results | ✅ | **PROVEN**: `run_pt042.py` ABSENT at `ae3b07a`; prereg byte-identical since, except the RUN banner |
| Null results reported | ✅ | `NOT SUPPORTED` is the headline; `N4`'s degeneracy and `S1`'s inversion both reported |
| Drill parameters not adopted as doctrine | ✅ | `A-082` fence held — 5-pip stop and 30-pip target appear in **no** spec file |
| Quarantine on sight | ✅ | `Q-015` filed; **no V14 artifact cites the quarantined files** |
| Speaker tested, not assumed | ✅ | Six strands, scan re-run in code |

**Overall: the lesson is understood, the method is specified, one step of it is not computable and
the record says so, and the test the lesson invited returns `NOT SUPPORTED` with its own controls
disclosed as defective.**

---

## 7. FOR THE REVIEWER — WHERE TO ATTACK

1. ⭐ **`V14_INTERPRETATION.md` Q3a, the `A-084` defeater.** If the compound-question argument fails,
   `A-084` may close on `k = 1` and **V11's entire RSI half unblocks.** This is the highest-value
   thing in the submission to try to break.
2. ⭐ **Q5 / `A-056`.** Should it be marked `CLOSED`? This session says no, on `A-089` alone. **A
   reviewer may reasonably disagree**, and it is the single biggest status change available.
3. **Q1 / `A-092`.** The Week-6 conclusion rests on a **forward `grep` into V15**. Is `D3` an
   acceptable deviation, and does the *"week seven"* datum bear the weight put on it?
4. **`BT_V14_0001.md` §3a.** The `N1` `O1` disclosure — is the stated direction right, and is
   disclosing it sufficient, or is a re-run owed?
5. **`04_SCREENSHOTS/V14/INDEX.md` §3.** The `D-043` corroboration is an **eyeball ordering** of
   four coloured lines. **Re-open the frame.** If red is faster than yellow, the claim is wrong.
6. **`C-021`.** Is leaving it unadjudicated right, or does `SOURCING_HIERARCHY.md` in fact supply a
   rule this session missed?
