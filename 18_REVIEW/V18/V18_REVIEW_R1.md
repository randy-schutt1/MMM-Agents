# V18 — INDEPENDENT REVIEW

**Round:** R1
**Reviewer:** Independent Reviewer / Teacher Agent, fresh session (`DECISIONS.md` `D-003`)
**Date:** 2026-08-14
**Lesson:** `Bootcamp1 Wk8 051312 Part2 (46mins).swf` · V18 · 2012-05-13 · 00:46:08
**Submission reviewed:** `video/v18` @ `aa0ba5e` (2 commits, `c1cb2c7`…`aa0ba5e`)
**Review branch:** `review/v18`, isolated worktree `MMM-Agents-v18-review` (`D-038`)

---

## FINAL DECISION

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 5 MINOR, 14 NOTE.**
**Confidence:** `HIGH`.

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the gate
for V19.** The five minors are carried in `REVIEW_INDEX.md` as items **264–268** and are owed before
V18 can reach `COMPLETE`.

**Every headline claim this submission makes was re-derived from source rather than checked against
the session's own working, and every one of them holds.** The transcript inversion is real and the
printed slides settle it; `PT-046` reproduces on independently written code with the baseline exact
to four decimal places; the `N3` fragility guard fires in reviewer code too; all 26 frame timecodes
verify against the pixels; `Q-019`'s corroboration of item 254 reproduces under a third,
independently written normalisation; and the gate-status correction is correct on the commit graph.

**The five minors are all arithmetic, ledger or citation-precision defects. None touches a rule,
a verdict, or a downstream conclusion.**

---

## §0 — THE GATE-STATUS CORRECTION, ANSWERED FIRST — AND THE SUBMISSION IS RIGHT

The submission's `§0.2` claims it was briefed that V17's R1 was *"currently in progress … not yet
returned"*, checked the commit graph rather than repeating the briefing, and found the premise
stale. **Re-derived here from the graph, not from the submission's account of it:**

| Fact | Verified value | Method |
|---|---|---|
| V17 R1 review committed | `0cd31a5` — **2026-08-14 18:50:38 −04:00** | `git log -1 --format=%cI` |
| V17 R1 merged to integration | `698c682` — **2026-08-14 18:51:07 −04:00** | same |
| V18's first content commit | `c1cb2c7` — **2026-08-14 19:18:04 −04:00** | same |
| `698c682` is an ancestor of `c1cb2c7` | ✅ **YES** | `git merge-base --is-ancestor` |
| `18_REVIEW/V17/V17_REVIEW_R1.md` present in `c1cb2c7`'s tree | ✅ **YES** | `git ls-tree -r c1cb2c7` |

**V17's review returned and merged 27 minutes before V18's first commit, and V18's worktree
genuinely descends from the merge that carries it.** The gate was open. The briefing was stale.
The submission checked, and recorded which.

⭐ **The reason given for checking is also verified:** V17 R1's item **246** does charge the V17
session with asserting a gate-timing fact that the graph refutes. **A session that had repeated its
briefing into four ledgers would have reproduced item 246 one lesson later.** It did not.

### §0.1 — V17'S ACTUAL STATUS, AND THE "NONE OF THEM TOUCHES V18" CLAIM — CHECKED ITEM BY ITEM

V17 R1 returned `REVISE` — **0 CRITICAL / 0 MAJOR / 6 MINOR / 13 NOTE**, HIGH confidence; status
**`IN REMEDIATION`**, items **244–249** owed. The submission claims **none bears on V18's subject
matter.** That claim was checked against the V18 diff (`git diff 698c682..aa0ba5e`, added lines
only), not against the submission's summary of it:

| V17 minor | Subject | Does it reach V18? |
|---|---|---|
| **244** | V17's `[00:11:22]` mishearing | ❌ **No.** V18 cites `[00:11:22]` exactly once, in its own §8 citation-check row, correctly labelled a **V17** marker. No V18 rule rests on it |
| **245** | `A-010`'s V17 addendum quotes an ASR error | ❌ **No.** V18 adds **zero** lines mentioning `A-010`. `A-010` is not advanced, quoted or relied on |
| **246** | V17's own gate-timing paragraph | ❌ **No.** V17-internal; and V18's equivalent paragraph is verified correct in §0 above |
| **247** | Arm B's ~25% exclusion is a property of `load_m1`, not of `mmm_lib` generally | ❌ **No — and this is the one worth checking properly.** Item 247's remediation names `load_m15` as **unaffected**. `run_pt046.py` calls **`L.load_m15`**, not `load_m1`. Confirmed by reading the runner |
| **248** | *"17:00 dealer time"* is an unmarked inference in five files | ❌ **No — V18 does the opposite.** The only V18-added line in this territory reads *"Whether it is 9:45 New York, London, or dealer time is **not determinable from V18**"* (`AUTOMATION_AMBIGUITIES.md`). The inference item 248 charges is explicitly declined |
| **249** | `Q-018`'s `RULES.md` diff count is wrong | ❌ **No.** `Q-019`'s counts are computed by script (`S3`) and are **verified correct here** — see §2 |

⭐ **The claim holds on all six.** Item 247 in particular is not a technicality: `PT-046` inherits
`mmm_lib`'s completeness machinery, and had it used `load_m1` the open V17 minor would have
propagated straight into V18's primary test. It does not.

---

## §1 — SOURCE MATERIAL REVIEWED, BEFORE ANY STUDENT CONCLUSION

Per `REVIEW_PROTOCOL.md` §3, source first.

| Evidence | What was done |
|---|---|
| The `.swf` itself | **SHA-256 re-computed: `cfa425ab059573a17276d3ed7ce187b039309b49a6ab99e47291641d0b1f7181`** — matches `SOURCE_MANIFEST.md` exactly. Size **17,852,174 bytes**, matches |
| Audio | Extracted independently (`ffmpeg`, 16 kHz mono PCM). Measured duration **2768.95 s = 00:46:08.95**, matches the manifest's `00:46:08` |
| **Independent ASR** | **`faster-whisper` / CTranslate2 `large-v3`, full-file pass**, plus targeted passes on the two disputed windows at `beam_size=10`, under **both** `vad_filter` settings, at `int8` **and** `float32`, and on **0.5×/0.35× time-stretched** audio. Also `medium.en` as a fourth reading |
| The printed slides | **Read directly from the committed PNGs at full resolution** — not from the index's description of them |
| Frame timecodes | **All 26 burned player readouts cropped from the pixels and read** |
| The quarantined trio | Re-hashed and re-diffed **in the reviewer's own shell** against all 21 lessons |
| GBP/USD M1 corpus | `mmm_lib`, DEVELOPMENT and EXTENDED scopes, both `D-031` arms |

---

## §2 — WHAT WAS RE-DERIVED RATHER THAN READ

### ⭐⭐ THE `[00:19:40]` INVERSION — CONFIRMED, AND THE PRINTED EVIDENCE IS DECISIVE

**The committed transcript really does invert the rule.** Line 1337 of
`02_TRANSCRIPTS/V18/V18_TRANSCRIPT.md`, under marker `[00:19:40]`, reads:

> *"Counter trends are advised."*

**Both slides were read here directly from the pixels, at full resolution, not from the index:**

| Frame | Printed text, read by this reviewer |
|---|---|
| `V18_00-11-29_up-trend-wvvm-counter-trend-ill-advised-v1.png` | `TREND` · `Market Maker Up Trend Can Be Labeled As Such` · **`W V V M`** · **`Counter Trend Is Ill Advised On V1`** |
| `V18_00-19-34_down-trend-maaw-counter-trend-ill-advised-a1.png` | `TREND` · `Market Maker Down Trend Can Be Labeled as Such` · **`M A A W`** · **`Counter Trend Is Ill Advised on A1`** |

**The rule is `Counter Trend Is Ill Advised`. The committed transcript states its opposite. The
submission's headline finding is correct**, and its handling is correct: the defective line is
**retained verbatim in the transcript body** (which is byte-for-byte source) and corrected in the
verification section, with every downstream artifact citing the correction. Checked by `grep` across
`V18_SOURCE_NOTES.md`, `V18_INTERPRETATION.md`, `04_SCREENSHOTS/V18/INDEX.md` and the mastery
report: **no V18 artifact quotes the raw line as a rule.**

**It is independently corroborated inside the committed transcript itself**, which carries
*"I can only say ill-advised… It's ill-advised."* at `[00:14:47]`, *"It's ill-advised."* at
`[00:15:20]`, and *"I do not want you to counter trend back here. It's a sucker's play, man."* at
`[00:13:03]`.

### ⚠ BUT THE ASR HALF OF THE CORROBORATION IS **CONFIGURATION-DEPENDENT**, AND THAT SHOULD BE ON THE RECORD

`V18_TRANSCRIPT.md` §5 presents the second engine as an independent refutation. **On the same engine
and the same model the submission names — `faster-whisper` / CTranslate2 `large-v3` — this reviewer
obtains both readings, depending on one decode flag:**

| Configuration (all `large-v3`) | Returned text at this marker |
|---|---|
| `vad_filter=True`, `int8` | *"A1, **counter trend is ill-advised**, going back towards the peak."* |
| `vad_filter=True`, `float32` | *"A1, **counter trend is ill-advised**, going back towards the peak."* |
| `vad_filter=False`, `int8` | *"A1, **countertrend is advised**. Going back towards the peak."* |
| `vad_filter=False`, `float32` | *"A1, **countertrend is advised**. Going back towards the peak."* |
| `vad_filter=False`, `beam_size=10`, full-file pass | *"A1, **countertrend is advised**, going back towards the peak."* |
| `medium.en` | *"A1, **counter trend is advised**, going back towards the peak."* |
| `large-v3` on **0.5×** and **0.35×** time-stretched audio | *"counter trend is **advised**"* |

**The submission's result reproduces — under VAD.** So the claim is not wrong. **But the word `ill`
is acoustically marginal here**: word-level alignment puts *"is"* at 1180.48 s and *"advised"* at
1180.54 s, 60 ms apart, which is too short for the two words and is the signature of a swallowed
syllable. **Six of this reviewer's ten decodes drop it.**

⭐ **This does not weaken the finding — it strengthens the reason the finding was made the way it
was.** The slide is Tier 2 in `REVIEW_PROTOCOL.md` §5 and the transcript is Tier 3; **the print
settles it and the ASR never had to.** `NOTE` item **270** asks only that the decode configuration
be recorded, because *"an independent engine returns X"* is reproducible only if the configuration is
stated — and on this line it is the configuration that decides.

### ⭐⭐ `PT-046` — INDEPENDENTLY RE-IMPLEMENTED FROM ITS PRE-REGISTRATION, AND IT REPRODUCES

`06_MANUAL_BACKTEST/scripts/rev_pt046_independent.py` was written **from
`PT-046_two_sessions_then_a_corrective_third.md` §§2a–6 alone, before `run_pt046.py` was opened**.
`mmm_lib` is used for data loading only (`load_m15`, `session_day`, `minute_of_day`, `SEED`).

*Disclosure: before writing it, this reviewer had seen three lines of `run_pt046.py` via a `grep`
for `load_m1` performed for the item-247 check above — the import, the `load_m15` call, and the
`assert_development` call. No measure, control or verdict logic was seen.*

| Quantity, `W-D` / arm A (primary) | Submission | **Reviewer, independent code** | |
|---|---|---|---|
| Sessions built | 2,691 | **2,691** | ✅ **exact** |
| Complete session days / excluded | 897 / 11 | **897 / 11** | ✅ **exact** |
| Zero-direction sessions | 4 | **4** | ✅ **exact** |
| **O2 — the pre-committed BASELINE** | **0.5124** `[0.4928, 0.5320]`, n=2,498 | **0.5124** `[0.4928, 0.5320]`, n=2,498 | ✅ **exact to 4 dp, interval and n** |
| **O1 — P(3rd corrects │ 2 same)** | 0.5080 `[0.4788, 0.5372]`, 571/1,124 | **0.5089** `[0.4797, 0.5381]`, **571**/1,122 | ✅ numerator **exact**; denominator differs by the 2 ties — see item **267** |
| **O3 — the lift** | −0.0044 | **−0.0035** | ✅ same sign, same magnitude class |
| **O5 — run-length mode** | **1**, not 2 | **1**, not 2 | ✅ **exact** |
| **Runs of exactly length 2** | **366** observed vs **367.2** expected | **366** observed vs **367.0** expected | ✅ **observed exact** |
| N1 percentile of observed O3 | 34.0 | **39.0** | ✅ both far below the 90 threshold |
| **VERDICT** | ⬜ **`NOT SUPPORTED`** | ⬜ **`NOT SUPPORTED`** | ✅ **reproduces** |

⭐ **The most-quoted figure in the submission is exact on independent code: runs of exactly length 2
occur 366 times against a coin-flip expectation of ~367.** The lesson's most emphatic rule — stated
four times with *"write that down"*, verified here at transcript lines 740/749/758/764/779/803, with
*"Write that down."* at line 746 — **occurs at 99.7% of the rate chance predicts, and the modal run
is one session, not two.**

**The null is real.** Both Wilson intervals overlap almost completely and both contain 0.5, exactly
as `BT_V18_0001.md` §0.1 says.

### ⭐⭐ THE `N3` FRAGILITY GUARD — THE METHODOLOGY POINT IS UPHELD

This is the claim the review brief asked to be confirmed rigorously, and it survives.

**On the replication window `W-E`, both arms return a positive lift at the primary boundary — the
direction the claim wants.** Reviewer code reproduces this:

| Cell | Submission O3 @ 09:00 | **Reviewer O3 @ 09:00** |
|---|---|---|
| `W-E` / A | **+0.0016** | **+0.0024** |
| `W-E` / B | **+0.0025** | **+0.0029** |

**And in both implementations that positive lift does not survive moving the one invented boundary.
`N3` fires on both arms, in both implementations, and the verdict is forced to `INCONCLUSIVE`:**

| Cell | Submission (08 / 09 / 10) | **Reviewer (08 / 09 / 10)** | N3 sign-flip? |
|---|---|---|---|
| `W-E` / A | −0.0025 / **+0.0016** / −0.0003 | −0.0013 / **+0.0024** / +0.0005 | ✅ **fires in both** |
| `W-E` / B | −0.0016 / **+0.0025** / −0.0006 | −0.0005 / **+0.0029** / +0.0000 | ✅ **fires in both** |

⭐⭐ **The claim under review is confirmed: a pre-registered, decision-overriding guard caught a
positive result on both arms and refused it.** Without `N3`, the sentence *"the replication window
shows a positive lift on both arms"* was available, true, and flattering to the lesson. **The lift
is a quarter of one shuffle SD.** The guard was fixed before any bar was read, and it was honoured —
this reviewer re-derived it independently and reached the same forced `INCONCLUSIVE`.

⚠ **One qualification, charged as `MINOR` item 267.** `BT_V18_0001.md` §4 says the sign *"flips
negative in **all four** of the four off-boundary cells"*. That is true of the submission's numbers
and false of this reviewer's, where two of the four sit at `+0.0005` and `+0.0000`. **The difference
is entirely the tie convention of item 267** — and the honest statement, which is *stronger* for the
submission's own conclusion, is that **the off-boundary sign is not stable at all: it sits at
approximately zero and its sign is convention-sensitive.** That is a better argument for
`INCONCLUSIVE` than "all four negative", not a worse one.

### ⭐ THE `W-D` / ARM B SEAL — FIRED IDENTICALLY IN REVIEWER CODE

```
HOLDOUT BREACH (REV PT-046 W-D/B): max timestamp 2016-07-01T00:45
    >= 2016-07-01T00:00. Stopping, per `D-035` / `E23`.
```

**Byte-for-byte the same boundary condition, from independently written code that merely called
`assert_development` where the pre-registration says to.** The submission recorded the abort and
moved on; it did not weaken the assertion or pass a custom window. **A seal that fires is a result.**
`W-D`/arm B replication remains owed and blocked on `I-010` Q2, exactly as `BT_V18_0001.md` §5 says.

### ⭐ §8a — ALL 26 FRAME TIMECODES VERIFIED FROM THE PIXELS

The falsifiable claim is `INDEX.md` §0.3's: *"Every one of the 26 frames is named from ITS OWN burned
timecode."* **Tested exhaustively:** the bottom-right `MM:SS / MM:SS` readout was cropped from all 26
PNGs, upscaled, and read.

**Result: 26 of 26 filenames match their own burned timecode exactly** — `00:20`, `02:09`, `03:34`,
`05:24`, `06:29`, `09:09`, `10:19`, `11:29`, `14:09`, `16:34`, `17:54`, `19:34`, `20:49`, `22:14`,
`23:30`, `25:24`, `26:39`, `27:53`, `32:03`, `32:33`, `35:53`, `39:58`, `41:28`, `42:28`, `44:07`,
`44:52`.

⭐ **The frames were named from burned timecodes, as claimed, and no stale flat-zero assumption was
carried forward.** The `0 → −3 s` monotonic drift is a genuine new-to-corpus result and §8a earned
its place here.

⚠ **The counterfactual count is wrong, in the conservative direction** — `MINOR` item 266. See §3.

### ⭐ `Q-019` — CORROBORATION REPRODUCED BY A THIRD INDEPENDENT METHOD, AND EVERY CELL CHECKS

**The clone block.** Re-derived here with independently written normalisation (different regexes,
different hash truncation) over all 21 lesson trios:

```text
RULES.md         c70f03468a3b -> lessons [16, 17, 18, 19, 20]   (21 is distinct)
NOTES.md         282cc07458ed -> lessons [16, 17, 18, 19, 20]   (21 is distinct)
VISUAL_INDEX.md  9a0fe85ba519 -> lessons [16, 17, 18, 19, 20]
```

**Item 254's V16–V20 block reproduces exactly, and V21 breaks it.** `Q-019` says first that it
corroborates rather than discovers, and that is the correct posture.

**The diff counts** — the ones `S3` says were computed rather than copied from `Q-018`, whose
equivalents V17 R1 charged at item 249. Re-run in this reviewer's shell:

| File | `Q-019` claims | **Reviewer `diff` 17→18** | |
|---|---|---|---|
| `RULES.md` | 10 lines / 5 pairs | **10 / 5** | ✅ |
| `NOTES.md` | 2 lines / 1 pair | **2 / 1** | ✅ |
| `VISUAL_INDEX.md` | 8 lines / 4 pairs | **8 / 4** | ✅ |
| Byte lengths | 3,173 / 1,712 / 1,253 | **3,173 / 1,712 / 1,253** | ✅ |

**Item 249's defect was available here and was avoided.**

**The "first true cell".** Verified directly against source, which is the claim the brief asked for:

| Assertion | Verified? |
|---|---|
| *"30 to 90 minutes"* is genuinely said in V18 | ✅ **Yes** — transcript line 2678, and independently at **42:13.0** (VAD) / **42:13.7** (no VAD) on this reviewer's own `large-v3` passes |
| It occurs **once** | ✅ **Yes** — one hit in the transcript body |
| The real marker is `[00:42:14]`, not the fabricated `[00:22:00]` | ✅ **Yes** |
| `[00:22:00]`–`[00:22:02]` carries something else | ✅ **Yes** — *"all the time compressions two or three times."* |
| The context is the dealer **building the next level's formation**, not a *"gap between M/W legs"* | ✅ **Yes.** Reviewer ASR, verbatim: *"Then he's going to make the new formation. **That takes, what, 30 to 90 minutes?** Add that together. You need to wait about two hours for the dealer to make the next level stop hunt."* |

⭐⭐ **`Q-019`'s reading is right, and its warning is right.** The one true cell sits in a table whose
other rows are refuted; a reviewer spot-checking a number would most likely check that one. **A true
cell in these files is evidence of nothing**, and `Q-019` says so before anyone has to rediscover it.

**On the judgement the submission flagged as most worth attacking (`§5.5`, coincidence vs. access):**
this reviewer attacked it and agrees with the submission. The same row is pure fabrication on V17;
the timestamp is wrong by twenty minutes; the context is wrong. **A generator with content access
would not miss the timestamp by twenty minutes on the one row it got right.** Coincidence is the
better reading.

### ⭐ THE HOMEWORK — RECOMPUTED INDEPENDENTLY, AND THE ROBUST RESULT HOLDS

Reviewer code, own week-keying and own inclusion rule (exactly five complete session days per week,
giving 172 arm-A weeks against the submission's 181 — a different, stricter rule):

| Session | Submission (arm A) HIGH / LOW | **Reviewer (arm A)** HIGH / LOW |
|---|---|---|
| `S1` Asian (10 h) | 27.1% / 16.6% | **26.2% / 17.4%** |
| `S2` London (6 h) | 36.5% / 43.1% | **36.6% / 43.6%** |
| `S3` US (8 h) | 36.5% / 40.3% | **37.2% / 39.0%** |

⭐ **The headline reproduces: the Asian session is the longest of the three and produces the fewest
weekly extremes.** Per hour, London is **2.3×** as likely as Asian to hold the weekly high — the
submission's figure, confirmed.

⚠ **The companion figure is wrong** — `4.8×` should be **4.3×**. `MINOR` item **265**; see §3.

**The three-of-four not-done disposition is correct and is the right call**, not a gap. Items 1, 2
and 4 rest on a drawing task, on `peak formation` (used 17× in V18, constructed 0×), and on a V17
artifact. Approximating any of them would have tested the student's inventions. `REVIEW_PROTOCOL.md`
§K is satisfied.

### ⭐ QUOTE-VS-TRANSCRIPT FIDELITY — A STRONGER CHECK THAN THE SESSION'S OWN

`verify_citations.py` checks that a cited marker **exists**. It cannot check that the **quoted text**
is what that marker carries. This reviewer ran the stronger check: every ``​`[HH:MM:SS]`​`` + quoted
string pair across the six V18 artifacts plus the pre-registration, normalised and matched against
the committed grid.

**58 quote-marker pairs · 52 exact matches · 6 flagged · 5 of the 6 explained on inspection:**

| Flagged | Disposition |
|---|---|
| `[00:09:37]` *"switch positions"* | ✅ **Correct** — this is declared `CORRECTION #3`; the notes quote the corrected form deliberately |
| `[00:14:47]` *"I can only say ill-advised… It's ill-advised."* | ✅ **Correct** — an ellipsis-elided quote, marked with `…` |
| `[00:01:03]` *"the first W's low"* | ✅ **Correct** — the matcher mis-paired; the notes attribute that phrase to `[00:12:39]` in the same sentence |
| `[00:31:06]` *"my math is horrible"* | ✅ **Correct** — same mis-pairing; the notes attribute it to `[00:31:53]` |
| `[00:42:02]` *"45 minutes"* | ✅ **Correct** — appears only inside the `S2` self-charge narrative, exactly as the mastery report's §8 enumerates |
| **`[00:42:13]`** *"Then he's going to make the new formation. That takes what?"* | ⚠ **Real** — the first sentence is at `[00:42:11]`. `MINOR` item **268** |

⭐ **52 of 58 exact, and five of the six flags are the checker's fault rather than the submission's.
Source fidelity at the quotation level is strong.**

---

## §3 — FINDINGS

### `CRITICAL` — **NONE**

### `MAJOR` — **NONE**

**Weighed and rejected.** Item **267** (the tie convention) was weighed for `MAJOR` because it makes
a published characterisation implementation-contingent. It is charged `MINOR` because the primary
verdict is `NOT SUPPORTED` under **both** conventions, the `N3` guard fires under **both**, the tie
count is **disclosed inline** in the runner's own output (`ties 2`), and the affected quantity moves
by 0.0009 on a measure whose Wilson interval is 0.058 wide. It alters no rule and no decision.

### `MINOR`

| # | Item |
|---|---|
| **264** | ⚠ **`08_CONCEPT_LIBRARY/CONCEPT_INDEX.md` WAS NOT UPDATED, BREAKING A CONVENTION V16 AND V17 BOTH FOLLOWED.** Both prior lessons updated `CONCEPT_INDEX.md` in their bookkeeping commits (`e7a51cd`, `346417b`); the V18 diff `698c682..aa0ba5e` does not touch it. The file mentions V16 **9×** and V17 **9×** and V18 **0×**, and its `STATUS` block still reads *"LESSONS STUDIED: **17**"*. ⚠ The mastery report's §3 row 10 self-grades ledger hygiene `ADEQUATE` on the basis that *"`COURSE_PROGRESS.md` and `LOG.md` updated"* — **`CONCEPT_INDEX.md` is owed and was not noticed.** `E20` |
| **265** | ⚠ **THE `4.8×` PER-HOUR FIGURE IS WRONG IN THREE FILES; IT IS `4.3×`.** From the submission's **own** §3.2 table: Asian lows `16.6% / 10 h = 1.660 %/h`; London lows `43.1% / 6 h = 7.183 %/h`; ratio **4.33**, not 4.8. (Arm B gives 4.35.) The companion high-side figure `2.3×` **is** correct (`6.083 / 2.710 = 2.24`). Appears in `05_HOMEWORK/V18/V18_HOMEWORK.md` §3.2, `07_MASTERY_REPORTS/V18_MASTERY_REPORT.md` §4.5, and `LOG.md`. **Same class as V17 R1's item 249 and V16 R1's item 225 — an arithmetic figure quoted onward without recomputation.** `E20` |
| **266** | ⚠ **§8a's *"12 of 26 filenames"* COUNTERFACTUAL IS NOT DERIVABLE FROM ITS OWN TABLE, AND IT UNDERSTATES THE CASE.** `INDEX.md` §0.1 says carrying V16/V17's flat zero forward would have put *"up to 3 seconds of error into 12 of the 26 filenames"*. Reconstructed from the 26 verified burned timecodes: under a flat-zero assumption **24 of 26** filenames would carry a non-zero error (15 at 1 s, 7 at 2 s, 2 at 3 s); only **2** frames sit in the offset-zero region. Under the stricter reading *"error ≥ 2 s"* the figure is **9**. **Neither is 12.** ⭐ **The error is in the conservative direction — the submission understates its own finding** — but the number is in a permanent ledger and does not derive. Show the working or correct it. `E20` |
| **267** | ⚠ **THE `PT-046` RUNNER COUNTS TIE-THIRDS IN O1's DENOMINATOR; THE PRE-REGISTRATION §4 SAYS A TIE IS *"NEITHER A CONTINUATION NOR A CORRECTION"*, AND THE PRE-REGISTRATION'S OWN GOVERNANCE CLAUSE WAS NOT EXERCISED.** `run_pt046.py` increments `pair_n` for a prior pair whose third session is a tie and scores it as a non-correction (`pair_zero` is tracked and printed, but the case stays in the denominator): `571/1,124`. Reviewer code, reading §4 literally, excludes it: `571/1,122` → O1 **0.5089** not 0.5080. ⚠ **The pre-registration states: *"If the runner and this file ever disagree, THIS FILE GOVERNS, neither is edited, and the disagreement is reported in `BT_V18_0001.md`."*** The tie count is disclosed **numerically** (`ties 2`) but the §4-vs-§5 divergence is **not reported as a divergence**, so the clause the pre-registration wrote for exactly this case did not fire. **Consequence:** `BT_V18_0001.md` §4's *"the sign flips negative in **all four** of the four off-boundary cells"* is convention-contingent — under §4's reading two of the four sit at `+0.0005` and `+0.0000`. ⭐ **No verdict changes under either reading** and the honest restatement is stronger for the submission (see §2). `E20` |
| **268** | **A TWO-MARKER QUOTE IS CITED UNDER ONE MARKER, IN THE ENTRY WHOSE WHOLE POINT IS TIMESTAMP PRECISION.** `V18_SOURCE_NOTES.md` §8 and `QUARANTINE_REGISTER.md` `Q-019` §1 both quote ``[00:42:13]`` *"Then he's going to make the new formation. That takes what?"*. The second sentence is at `[00:42:13]`; **the first is at `[00:42:11]`.** The quote is verbatim and the content claim is correct — but `Q-019` charges a fabricated file for citing `[00:22:00]` instead of `[00:42:14]`, and carries a merged-marker citation two paragraphs later. Cite the span `[00:42:11]`–`[00:42:13]`. ⚠ **This is precisely the class `verify_citations.py` cannot catch, because it tests marker existence and not quote attribution** — see `NOTE` 281. `E11` |

### `NOTE` — no action required

| # | Item |
|---|---|
| **269** | ⭐⭐ **THE TRANSCRIPT INVERSION IS CONFIRMED FROM THE PIXELS.** Both slides read directly at full resolution: `Counter Trend Is Ill Advised On V1` (`W V V M`) and `Counter Trend Is Ill Advised on A1` (`M A A W`). The committed `[00:19:40]` states the opposite. **Handling is correct**: the raw line is retained verbatim in the byte-for-byte body and corrected in the verification section, and no V18 artifact quotes it as a rule (`grep`-verified across all six) |
| **270** | ⚠ **THE ASR HALF OF THAT CORROBORATION IS VAD-DEPENDENT, AND THE CONFIGURATION SHOULD BE RECORDED.** On the same engine and model the submission names, this reviewer gets *"ill-advised"* with `vad_filter=True` (both `int8` and `float32`) and *"advised"* with `vad_filter=False`, at `beam_size` 5 and 10, on the full-file pass, on `medium.en`, and on 0.5×/0.35× time-stretched audio. Word alignment puts *"is"* and *"advised"* 60 ms apart — a swallowed syllable. **The submission's result reproduces; the finding is sound and rests on Tier-2 print, not on the ASR.** Recording the decode flags would make the ASR claim reproducible rather than merely true |
| **271** | ⭐⭐ **`PT-046` REPRODUCES ON INDEPENDENTLY WRITTEN CODE.** Sessions **2,691**, complete days **897**, exclusions **11**, zero-direction **4**, and the run-length histogram's length-2 count **366** are all **exact**. The pre-committed **baseline O2 = 0.5124 `[0.4928, 0.5320]`, n = 2,498, is exact to four decimal places, interval and sample size.** Verdict `NOT SUPPORTED` reproduces |
| **272** | ⭐ **THE HEADLINE NULL IS AS CLEAN AS CLAIMED.** Run-length **mode 1, not 2**; runs of exactly length 2 at **99.7%** of the coin-flip rate; both Wilson intervals overlapping and both containing 0.5. **The lesson's most-repeated rule — verified here as stated four times, with *"Write that down."* at transcript line 746 — is indistinguishable from a coin flip on 2013–2016 GBP/USD under the most natural fixed-clock reading** |
| **273** | ⭐⭐ **THE `N3` GUARD FIRES IN REVIEWER CODE TOO, ON BOTH ARMS, AND THE METHODOLOGY POINT IS UPHELD.** `W-E` returns a positive lift at the primary boundary on both arms in both implementations, and in both implementations the sign is not stable across the pre-registered boundary moves, forcing `INCONCLUSIVE`. **A pre-registered decision-overriding guard prevented a true-but-spurious positive from being written up as support.** The lift is a quarter of one shuffle SD |
| **274** | ⭐ **THE `W-D`/ARM B SEAL FIRED IDENTICALLY IN REVIEWER CODE**, at the same timestamp (`2016-07-01T00:45`), from code that merely called `assert_development` where the pre-registration said to. The submission did not weaken, narrow or route around it |
| **275** | ⭐ **ALL 26 BURNED FRAME TIMECODES VERIFIED AGAINST THEIR FILENAMES — 26 OF 26 EXACT.** The §8a claim that every frame was named from its own burned timecode is confirmed exhaustively from the pixels. The `0 → −3 s` monotonic drift is genuine and new to the corpus; the decision to apply **no** scalar offset at all was the right one |
| **276** | ⭐ **`Q-019`'s CORROBORATION OF ITEM 254 REPRODUCES UNDER A THIRD, INDEPENDENTLY WRITTEN NORMALISATION.** V16–V20 clone identically on all three files; V21 breaks the block. Diff counts **10/5, 2/1, 8/4** and byte lengths **3,173 / 1,712 / 1,253** all verified in the reviewer's own shell — **item 249's defect was available and was avoided** |
| **277** | ⭐ **`Q-019`'s "FIRST TRUE CELL" IS VERIFIED IN FULL.** *"30 to 90 minutes"* occurs exactly once in V18, at `[00:42:14]`, independently timed by this reviewer's ASR at 42:13.0/42:13.7 under both VAD settings — and it is about the dealer **building the next level's formation**, not a *"gap between M/W legs"*. `[00:22:02]` carries *"all the time compressions two or three times."* **The coincidence reading was attacked here and upheld** |
| **278** | ⭐ **THE GATE-STATUS CORRECTION IS CORRECT ON THE GRAPH** — V17's R1 committed 18:50:38, merged 18:51:07, V18's first commit 19:18:04, with `698c682` a verified ancestor and `V17_REVIEW_R1.md` present in the tree. **The session checked instead of repeating its briefing, and it was right to** |
| **279** | ⭐ **THE "NONE OF V17's SIX MINORS TOUCHES V18" CLAIM HOLDS ON ALL SIX**, checked against added lines rather than against the submission's summary. Item **247** is the substantive one: `run_pt046.py` uses **`load_m15`**, which item 247's own remediation names as unaffected. Item **248** is *declined* rather than inherited — V18 records the session clock as *"not determinable from V18"* |
| **280** | ⭐ **THE HOMEWORK's ONE ROBUST RESULT REPRODUCES ON INDEPENDENT CODE WITH A STRICTER WEEK RULE.** Asian 26.2%/17.4%, London 36.6%/43.6%, US 37.2%/39.0% against the submission's 27.1/16.6, 36.5/43.1, 36.5/40.3. **The `2.3×` high-side per-hour figure is confirmed.** The three-of-four not-done disposition is the correct call, not a gap |
| **281** | **QUOTE-VS-TRANSCRIPT FIDELITY IS STRONG: 58 PAIRS, 52 EXACT, AND FIVE OF THE SIX FLAGS ARE THE CHECKER'S FAULT.** Only item 268 survives. ⚠ **Offered to the recipe rather than to the student:** `verify_citations.py` tests marker *existence*; extending it to test that the quoted text appears in the cited marker's span would have caught 268 mechanically, as the existence check caught `S2` |
| **282** | ⭐⭐ **CALIBRATION — THE BEST DECISIONS IN THIS SUBMISSION ARE THE ONES THAT DECLINED.** (1) `PT-046` tests the rule that *can* be tested and says up front that V18's centrepiece — the safety trade — cannot be, rather than testing a proxy and calling it the thing. (2) The `A-129` "fourth session resumes" measure is computed and **explicitly excluded from the decision** because no discriminator exists. (3) The `N3` guard was written to override a favourable result and then did. (4) `Q-019` says it corroborates rather than discovers, before saying anything else. (5) Three of four homework items are refused with reasons. (6) The `§9` two-pass violation (`S1`), the two bad citations (`S2`), the post-hoc runner edit (`S4`) and the un-recaptured frame (`S5`) are all self-charged. **`REVIEW_PROTOCOL.md` §17's five failure modes are being actively defended against, not merely avoided** |

---

## §4 — AUDIT DIMENSIONS (`REVIEW_PROTOCOL.md` §6)

| Dimension | Grade | Basis |
|---|---|---|
| **A. Source fidelity** | ✅ **PASS** | 52 of 58 quote-marker pairs exact; the single real defect (268) is a merged span, not a misquote. The `[00:19:40]` inversion is *corrected*, not propagated, and the raw body is untouched |
| **B. Completeness** | ⚠ **MINOR ISSUE** | Concepts, sequence, timing, warnings and the undefined-vocabulary census are thorough. **`CONCEPT_INDEX.md` is the hole** (264) |
| **C. Provenance** | ✅ **PASS** | 108 citations machine-verified by the session; the stronger text-level check run here passes at 52/58. No orphan rules — `Lights Out`, `HOW`, `level one`, `pins` are all recorded as used-and-undefined rather than reconstructed |
| **D. Explicit vs inferred** | ✅ **PASS** | `[AUDIO]`/`[PRINTED]`/`[VISUAL]` applied throughout and `grep`-falsifiable. The A–D + `DO NOT CODE` ladder is used honestly, with `DO NOT CODE` on 4 items including the lesson's own `Lights Out` |
| **E. Chart recognition** | **NOT EXERCISED** | V18 supplies no classification task and the submission attempts none. Correctly `NOT APPLICABLE`, not excluded |
| **F. Counterexamples** | ✅ **PASS** | `N1`, `N3` and `N5` are all counterexample machinery, all pre-registered, and `N3` actually bit |
| **G. Manual backtest procedure** | ✅ **PASS — the strongest dimension** | Baseline present **and pre-registered** (checks 15–16); period pre-registered at `c1cb2c7` before the runner existed (17); **holdout intact — the seal fired and was honoured** (18); n = 1,124 with Wilson intervals on every rate (19); **the null is the headline and every cell including the unrun one is reported** (20) |
| **H. Hindsight / lookahead** | ✅ **PASS** | Pre-registration precedes the runner in the commit graph, verified. The `S4` post-hoc edit is disclosed and touched no measure, threshold, control or window — confirmed by reading the runner |
| **I. Outcome vs rule application** | ✅ **PASS** | `PT-046` scores directional sequence only and says so; no trade outcome enters anywhere |
| **J. Sample quality** | ✅ **PASS** | 2,691 sessions / 1,124 prior pairs on the primary cell; 9,216 and 8,178 on replication. Exclusions counted and reported |
| **K. Homework** | ✅ **PASS** | One item executed, three refused **with reasons and without approximation**. `UNRESOLVED` is used correctly rather than papered over |
| **L. Teach-back** | ✅ **PASS** | `V18_INTERPRETATION.md` §1 restates the lesson in the student's own words, and §8 states what it would be wrong about first |
| **M. Blind recognition** | **NOT APPLICABLE** | No chart set in this lesson |
| **N. Ambiguity** | ✅ **PASS** | `A-126`–`A-131` opened; the session clock is recorded as *not determinable* rather than assumed — **which is how item 248 was avoided rather than inherited** |
| **O. Contradictions** | ✅ **PASS** | `C-028` filed. `A-128` (`Minimum 2 Hrs` vs *"about two hours"*) is carried as an ambiguity rather than forced into a contradiction, and the choice is put to the reviewer |
| **P. Machine-rule firewall** | ✅ **PASS** | `DO NOT CODE` on 4 items; §3 states plainly that V18 unblocks no coding |
| **Q. Claimed accuracy** | ✅ **PASS** | The *"nine for nine… that is 100%"* passage is preserved, cited, and explicitly given **no evidential weight** |
| **6a(1) `EXCLUDED BY DECISION`** | **NOT ENGAGED** | No dimension carries this disposition |
| **6a(2) `D-048` rung** | **NOT ENGAGED** | No Tier 1 vs Tier 1 conflict resolved |
| **6a(3) `D-049` forward read** | **NOT ENGAGED** | No forward read. The one backward read (V17, same recording) is declared at `V18_SOURCE_NOTES.md` §0 D3 and imports no rule, number or interpretation — verified |

---

## §5 — REQUIRED CORRECTIONS

Specific and bounded, per `REVIEW_PROTOCOL.md` §10. **None requires re-running any test.**

1. **Item 264** — add V18's rows to `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md` in the form V16 and V17
   used, and update its `STATUS` block from *"LESSONS STUDIED: 17"* to 18.
2. **Item 265** — correct `4.8×` to **`4.3×`** in `05_HOMEWORK/V18/V18_HOMEWORK.md` §3.2,
   `07_MASTERY_REPORTS/V18_MASTERY_REPORT.md` §4.5 and `LOG.md`. Leave `2.3×`, which is correct.
3. **Item 266** — in `04_SCREENSHOTS/V18/INDEX.md` §0.1, either show the derivation of
   *"12 of the 26"* or correct it to **24 of 26 at ≥ 1 s** (of which 9 at ≥ 2 s).
4. **Item 267** — add a subsection to `BT_V18_0001.md` recording the §4-vs-§5 tie divergence as a
   runner/pre-registration disagreement (the pre-registration's own clause requires it), state that
   the pre-registration governs, and report O1 under both conventions (`0.5080` / `0.5089`).
   **Re-word §4's *"all four"* sentence** to the stronger and convention-independent statement: the
   off-boundary lift sits at approximately zero and its sign is not stable. **Do not re-run the
   test and do not edit the pre-registration.**
5. **Item 268** — change the citation in `V18_SOURCE_NOTES.md` §8 and `QUARANTINE_REGISTER.md`
   `Q-019` §1 to the span `[00:42:11]`–`[00:42:13]`.

**Recommended, not required** (item 270): record the `faster-whisper` decode configuration —
`vad_filter`, `beam_size`, `compute_type` — in `V18_TRANSCRIPT.md` §5, so the second-engine result is
reproducible rather than merely correct.

---

## §6 — REVIEWER QUESTIONS FOR THE OWNER

1. **`SWF_CAPTURE_RECIPE.md` §8a step 3 needs a tolerance — the submission's open item 1 is upheld.**
   Its binary test halts on a **0.110%** pacing deficit while targeting a **50%-class** multiplier
   error. **This reviewer agrees with the judgement call made in `INDEX.md` §0.3 and with the
   decision not to make the edit here** (`D-038a` puts policy on integration). Recommended wording:
   split "gross multiplier error" from "pacing slippage" and set the halt threshold at a rate
   deviation of **≥ 5%**.
2. **`verify_citations.py` should be promoted and extended** (`NOTE` 281). Extending it from marker
   existence to quote-span containment would have caught item 268 mechanically. Whether it becomes a
   recipe step is the owner's call.
3. **`A-128`** — the submission asks whether `Minimum 2 Hrs` vs *"about two hours"* is a real
   conflict. **This reviewer's view: carry it.** The slide's own on-screen derivation
   (`45 min vector + 30–90 min formation`) admits **75 minutes**, which the word `Minimum`
   contradicts. That is a divergence between the deck and its own arithmetic, not loose wording.
4. **`I-010` Q2** remains the blocker on `W-D`/arm B for `PT-046` and now for a second test. It has
   now cost two backtests a replication cell.

---

## §7 — ADVANCEMENT

```text
LESSON: V18
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES: none
MAJOR ISSUES:    none
MINOR:           5   (items 264-268)
NOTE:            14  (items 269-282)

REQUIRED ACTIONS:
  1. Add V18 to CONCEPT_INDEX.md and update its STATUS block.        (264)
  2. Correct 4.8x -> 4.3x in three files.                            (265)
  3. Derive or correct the "12 of 26" counterfactual.                (266)
  4. Report the PT-046 tie divergence in BT_V18_0001.md and re-word
     the "all four off-boundary cells" sentence. Do not re-run.      (267)
  5. Cite [00:42:11]-[00:42:13] as a span.                           (268)

ADVANCEMENT: AUTHORIZED
V19 GATE: OPEN under D-024 -- zero CRITICAL, zero MAJOR.
V18 STATUS: IN REMEDIATION. NOT COMPLETE until items 264-268 are applied
            and verified by an independent reviewer (D-003).
```

**On the gate.** V18 is the second consecutive lesson opened on a gate that was genuinely open, and
the first to have *checked* that rather than assumed it. **V19's gate is open on this round's merit —
zero CRITICAL, zero MAJOR — and the five minors are deferred, not waived.**

⚠️ **One standing caution, repeated from V17 R1 and not addressed to this submission.** The
remediation debt is now **two lessons deep**: V17's items 244–249 and V18's 264–268 are both owed,
and `D-003` reserves closure of each to an independent reviewer. **The pace instruction is being met
without cost to gate compliance so far. That is a fact about V17 and V18, not a forecast about V19.**

---

## §8 — REVIEWER'S OWN DISCLOSURES

1. **Worktree isolation honoured.** All work in `MMM-Agents-v18-review` on branch `review/v18`,
   created from `aa0ba5e`. The shared checkout was read for Git-ignored source media and the
   quarantined corpus only, and nothing in it was written.
2. **The dataset was symlinked, not copied**, into this worktree's Git-ignored
   `06_MANUAL_BACKTEST/datasets/` so `mmm_lib`'s path resolution would find it. The link and the
   stub it displaced are outside Git's index and are not committed.
3. **Order of work.** Source evidence (checksum, audio, ASR, slides, frame timecodes) was inspected
   before any student conclusion. `PT-046` was re-implemented **from the pre-registration before
   `run_pt046.py` was opened**, with the single exception disclosed inline in §2: three lines of the
   runner were seen earlier via a `grep` for `load_m1` run for the item-247 check.
4. **Reviewer code is committed** as `06_MANUAL_BACKTEST/scripts/rev_pt046_independent.py` so its
   figures are re-runnable and falsifiable. It is reviewer apparatus, not a project artifact.
5. **Item numbering.** Items **264–282** allocated against the integration branch's state at
   `6cd01aa`, where **263** was the highest existing item. Re-check at merge-back per `D-047`.
