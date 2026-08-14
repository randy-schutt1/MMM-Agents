# V12 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V12** · `Bootcamp1 Wk4 040812 Part2 (55mins).swf` · session 2012-04-08 (Easter Sunday), **Part 2 of V11's recording** |
| Review version | **R1** |
| Review date | 2026-08-14 |
| Previous review | none |
| Reviewer branch | `review/v12`, cut from the integration branch @ `e70a6f6` (`D-038`), own worktree at `MMM-Agents-v12-review` |
| Submission reviewed | `video/v12` @ `ecc2f75` (7 commits, `85dc926`…`ecc2f75`) |
| Independence | **`D-003` satisfied.** This session authored no V12 artifact. It read the full 690-marker transcript before any student conclusion was opened; it **extracted the audio from the source `.swf` and ran its own ASR pass with a different engine and a different model** from the student's; it re-derived `PT-040` end to end in code sharing no line with `run_pt040.py` or `mmm_lib`; and it re-ran the `Q-013` `diff`, the flashcard census and the nickname census at source |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 2 MINOR, 6 NOTE.**

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the gate
for V13.** `COURSE_PROGRESS.md` currently reads *"V13 GATE: CLOSED until V12's R1 returns"* — that
was the correct state to hold pending this review, and **this review opens it.** The two minors are
carried in `REVIEW_INDEX.md` as items **137–138** and are owed before V12 can reach `COMPLETE`.

**Confidence: HIGH.**

Confidence is high because every load-bearing claim was **re-derived from the source rather than
read**:

- **`PT-040` was independently reproduced in full.** Reviewer-written code — its own CSV parser, its
  own M15 aggregation, its own Wilder RSI, its own US-DST rule, its own observation set —
  **reproduces every Wilder cell of the committed output to the printed decimal**, across `W-A`/Arm A,
  `W-A`/Arm B and `W-B`/Arm A: `O1`, `O2`, all `O3` ratios, `O4`, and the bar counts 24,755 / 24,730 /
  discarded 25. **`M = 10.4812 pp` at `k=5, t=50` and `5.1638 pp` at `k=2`.**
- **`A-080` was re-verified with a third ASR engine.** The audio was extracted from the source SWF
  (SHA-256 re-checked against the manifest) and **all four cited timestamps were re-transcribed with
  `faster-whisper medium.en`** — a different implementation *and* a different model from the
  student's `openai-whisper small.en`. **All four confirm.**
- **The `Q-013` `VISUAL_INDEX.md` `diff` was re-run at source** and returns exactly what the register
  claims: four differing lines, zero content lines, and **exactly ten** lessons sharing one body.
- **The flashcard census was re-run across all 21 lessons** and reproduces **119 occurrences across
  18 of 21**, every per-lesson cell.
- **Frames were opened and read as images** — and that is where `M1` came from.

---

## SOURCE MATERIAL REVIEWED — **FIRST, BEFORE ANY STUDENT CONCLUSION**

| Source | References | Purpose |
|---|---|---|
| `02_TRANSCRIPTS/V12/V12_TRANSCRIPT.md` verbatim body | **All 690 markers, `[00:00:00]`–`[00:55:11]`, read in full** | Primary evidence for every finding below. Read **before** the source notes, interpretation, homework, backtest or mastery report were opened |
| **The source `.swf` itself** | SHA-256 verified; audio extracted to 16 kHz mono | **Independent ASR.** Nine passages re-transcribed by this reviewer |
| Frames `31:31`, `26:11`, `19:06`, `34:26`, `37:21`, `40:36`, `20:41`, `22:11` | Opened and read as images; four regions cropped and enlarged | Verify the mayo citation, the `C-019` printed bullet, and the categorical legend claim. **This is where `M1` came from** |
| `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/**` — all 21 `VISUAL_INDEX.md`, all 21 `NOTES.md` | `diff`ed and normalised-hashed across the whole set | Independent re-derivation of `Q-013` §1–§4 |
| `datasets/HISTDATA_GBPUSD_M1/raw/*.csv` | **1,297,781 M1 bars parsed directly** (not the student's `_cache`) | Independent re-derivation of the whole of `PT-040` |
| All 21 lesson transcripts (V01–V12 ingested, V13–V21 pre-ingestion) | Flashcard census; TDI-vocabulary census | Verify `A-082`'s reframing and test `Q-013` §4 |
| `EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md` pp.44–46 | Read at the page markers | Verify `C-019`'s Tier 2 citations |
| `DECISIONS.md` `D-003`, `D-004`, `D-024`, `D-026`/`D-027`, `D-030`, `D-031`, `D-038`/`D-038a`, `D-039`–**`D-043`**; `SOURCING_HIERARCHY.md` in full | Read in full | Governing policy |

**Source access was not limited.** The `.swf`, its audio, the transcript, all 28 curated frames, the
quarantined tree and the full M1 corpus were available. **Nothing in this review is capped by missing
evidence**, with the one exception recorded as `N2`.

## STUDENT ARTIFACTS REVIEWED

| Artifact | Reviewed |
|---|---|
| `02_TRANSCRIPTS/V12/V12_TRANSCRIPT.md` header, speaker table, coverage, verification, 7 spot-checks | ✅ in full |
| `03_LESSON_NOTES/V12_SOURCE_NOTES.md` · `V12_INTERPRETATION.md` | ✅ in full |
| `04_SCREENSHOTS/V12/INDEX.md` + **8 frames opened, 4 regions enlarged** | ✅ |
| `05_HOMEWORK/V12/V12_HOMEWORK.md` | ✅ |
| `PT-040_…md` · `BT_V12_0001.md` · `data/pt040_output.txt` · `scripts/run_pt040.py` | ✅ in full |
| `07_MASTERY_REPORTS/V12_MASTERY_REPORT.md` | ✅ |
| `QUARANTINE_REGISTER.md` `Q-013` · `A-080`/`A-064`/`A-020`/`A-031`/`A-032`/`A-039`/`A-082` updates · `A-084`–`A-086` · `C-019` | ✅ |
| `LOG.md`, `COURSE_PROGRESS.md`, `REVIEW_INDEX.md` items 121–136 | ✅ |

---

## CRITICAL FINDINGS

**NONE.**

The four places a `CRITICAL` could plausibly have arisen were checked directly and all four are clean:

1. **A number invented for the RSI period.** Re-verified at source with an independent engine. `21`
   is the instructor's own word, four times, with the rationale and the default it replaces.
   **Nothing was inferred.**
2. **A threshold moved after the numbers were seen.** `PT-040`'s decision boundaries (`2 pp` / `5 pp`)
   are in commit `83110f1`, and **`run_pt040.py` provably does not exist at that commit** — I checked
   with `git cat-file`. `M = 10.48` lands close enough to a defensible-sounding *"10 pp"* that a
   post-hoc boundary would have been a live temptation. It was foreclosed.
3. **The mayo upgrade quietly amending `D-043`.** Checked row by row. **No value moves; one warrant
   moves.** See § `A-020`.
4. **A fabricated file's content leaking into a V12 artifact.** `Q-013` §4 flags the hazard and I
   tested the negative independently: **no V12 artifact cites `NOTES.md`, `RULES.md` or
   `VISUAL_INDEX.md`.**

---

## MAJOR FINDINGS

**NONE.**

---

## ⭐ `A-080` — RE-VERIFIED AGAINST THE SOURCE AUDIO WITH A THIRD ENGINE

**Reviewer verdict: the closure is CORRECT and the evidence is stronger than the record claims.
Confidence HIGH.**

The task put to this reviewer was to re-verify **at least two** of the four cited timestamps.
**All four were re-verified**, plus the fifth restatement.

### Method — genuinely independent

The source `.swf` was located from `SOURCE_MANIFEST.md`, its **SHA-256 re-computed and matched
exactly** (`10608e8f…159b`), and audio extracted with `ffmpeg` to 16 kHz mono. Measured duration
**3318.543688 s** against the transcript's claimed **3318.543673 s** — agreeing to the seventh
significant figure, which independently confirms the header's own duration arithmetic.

Passages were then re-transcribed with **`faster-whisper` `medium.en`** — a different runtime
(CTranslate2, not PyTorch) and a **larger model** than the student's `openai-whisper small.en`.

### The four statements, verbatim from my own pass

| # | `A-080` cites | **Reviewer's independent transcription** | |
|---|---|---|---|
| 1 | `[00:07:24]` *"I like the RSI line to be set at 21"* | *"I like the RSI line to be set at **21**. Why? It just matches up with the averages a little better and lines up a price action for our purposes."* | ✅ **EXACT** |
| 2 | `[00:07:53]` *"21 slows it down a little bit"* | *"**21 slows it down a little bit**, you don't see as much noise, it smooths the line…"* | ✅ **EXACT** |
| 3 | `[00:08:09]` *"21 closing periods back… instead of 14 periods"* | *"That means we're looking at **21 closing periods back for our line. We're averaging that out instead of 14 periods.**"* | ✅ **EXACT** |
| 4 | `[00:10:51]` *"this line set to 21, 21 look back periods, that's all"* | *"For our group, in here, **we have this line set to 21, 21 look back periods that's all.**"* | ✅ **EXACT** |
| 5 | `[00:15:13]` restatement | *"So now, **we have RSI set to 21**, blood in the water, trade signal line, TSL, a moving liquid 50…"* | ✅ **EXACT** |

**Two ASR defects in the project's own transcript are resolved by my pass in the submission's
favour**, and both are recorded in its `TRANSCRIPTION NOTES`: `[00:10:51]`'s *"at all"* is **"that's
all"**, and `[00:15:13]`'s *"our SI"* is **"RSI"**. **Three engines now agree on the number in every
place it is spoken.**

**One further sentence my pass surfaced that the record does not cite, and it cuts in the closure's
favour:** `[00:08:22]` *"**You want to use it at 14, knock yourself out.**"* This is the instructor
explicitly contrasting his preset against the RSI's own default **as a choice he is making**, which
forecloses the reading that `21` is a misspeak or that he is describing someone else's setting.
Recorded as `N3`.

### The categorical frame claim — *"no properties dialog… checked across all 672 frames"*

**Verdict: the substantive claim is CORRECT. Its stated basis is partly unverifiable, and its
companion completeness claim is FALSE — see `M1` and `N2`.**

| Limb | Reviewer verification |
|---|---|
| *"No frame in the lesson shows an MT4 indicator-properties dialog or Navigator entry"* | ✅ **CONFIRMED across the 28 committed frames**, which I opened. No modal window, no properties dialog, no Navigator panel |
| *"MT4 prints an indicator's inputs in parentheses after the name; here there are none"* | ✅ **CONFIRMED at source and this is the load-bearing observation.** I read the TDI sub-window legend on two separate frames: `00-26-11` and `00-34-26` both print `Traders Dynamic Index Visual` followed by **six unparenthesised output values** and **no input list**. The claim is exactly right |
| *"All 672 sweep frames scanned at mean-difference threshold 2.0"* | ⚠️ **NOT VERIFIABLE from the repository** — the sweep frames are not committed. Recorded as `N2`, **not charged** |
| *"Every legend legible in any V12 frame is transcribed below"* | ❌ **FALSE — see `M1`** |
| The six timecode-sync rows in `INDEX.md` §0 | ✅ **SPOT-CHECKED and correct.** Frame `26:11` prints `Shark Fin Hold The Mayo` at burned `26:11 / 55:1`, and `[00:26:11]` reads *"Shark fin hold the mail"* — **the same second in both media**, exactly as claimed |

**`A-080` closes on the audio and the audio is not in doubt.** `M1` does not touch it — see below.

---

## ⭐ `M1` — THE ROUND'S PRINCIPAL FINDING: A SECOND CATEGORICAL CLAIM ABOUT IMAGES, FALSIFIED BY AN IMAGE

**This is the only finding in the round that a reading-only review could not have produced. It came
from cropping and enlarging a frame.**

### The claim

`04_SCREENSHOTS/V12/INDEX.md` §1 is headed **"⚠️ LEGENDS — RECORDED IN FULL, WHETHER OR NOT THEY
SEEMED RELEVANT"**, and states:

> *"**V11 R1 item 109 required this.** V11's `INDEX.md` recorded a frame's *pane count* and not its
> *legend stack*, and the legend turned out to carry `RSI(21)`. **Every legend legible in any V12
> frame is transcribed below, including the ones that carry no parameters** — the negative is the
> point."*

Five entries follow. **The table is genuinely good** — it includes the `UPPERLINE 67.8351` hover
tooltip and correctly calls it *"the closest thing in the lesson to an indicator dialog. It names an
output, not an input."* That is precisely the discipline item 109 asked for.

### It is not complete, and frame `00-34-26` is where it fails

The `EURJPY` frame carries **a sixth on-screen text block that the table does not mention**: a
multi-timeframe indicator dashboard in the top-right quadrant. Cropped and enlarged, it is plainly
legible:

```text
              1    5   15   30   H1   H4    D    W   MN
   MACD      [ ][ ][ ][ ][ ][ ][ ][ ][ ]      (coloured status cells)
   STR       [ ][ ][ ][ ][ ][ ][ ][ ][ ]
   EMA       [ ][ ][ ][ ][ ][ ][ ][ ][ ]

   108.093
   Spread         33
   Pips to Open    -
   Hi to Low     315
   Daily Av        -
```

The `INDEX.md` row for `00-34-26` transcribes only the **top-left** OHLC block
(`EURJPY,M15 … Previous Days Range= 180 …`). **The top-right dashboard — which names three
indicators, one of them `EMA` — is not recorded anywhere in the submission.**

### ⭐ Why this does NOT move `A-080`, and why it is `MINOR` rather than `MAJOR`

**The disposition is correct and untouched. `A-080` stays `RESOLVED BY COURSE`, closed on the audio.
Nothing is unblocked and no number changes.** Three independent reasons, each checked:

1. **The dashboard carries no lookback period.** Its columns are **timeframes** — `1 · 5 · 15 · 30 ·
   H1 · H4 · D · W · MN` — not periods. The `5` and `15` are minutes, and reading them as EMA periods
   would be exactly the error the project exists to prevent. **The `EMA` row has no number attached
   anywhere.**
2. **It is a student's chart, not the instructor's.** `[00:34:19]`–`[00:34:24]`: *"Another example,
   this came to me from my good friend… who graduated Harvard business school and he's hanging with
   us."* This is the same category V11 R1's `M1` identified, and `A-080`'s own closure text already
   states the rule — *"check whose chart a legend belongs to before reading a period off it."*
3. **I checked whether it recurs and it does not.** I cropped the same region from `00-37-21`,
   `00-40-36`, `00-22-11` and `00-20-41`: **the dashboard appears on no other frame.** It belongs to
   the guest chart's template alone.

**So the correction runs in the record's favour: it is one more on-screen text block that carries no
period, and the substantive negative — *the lesson never shows its own RSI setting on screen* —
survives and is strengthened.**

### But it is not cosmetic, and the reason is the section's own heading

**This section exists solely to discharge V11 R1 item 109**, whose entire content was *"a
categorical claim about images has to be tested against the images."* The submission understood the
lesson, wrote the section, transcribed five blocks including a hover tooltip nobody would have
noticed — **and then made a categorical completeness claim that a sixth block falsifies.** The
failure mode is identical to V11's and one turn further out: V11 recorded a pane count and missed a
legend; V12 recorded the legends and missed a **dashboard**.

**Charged as `MINOR`** (`REVIEW_PROTOCOL.md` §8 — *"completeness problem that does not alter the
method"*). Inflating it would close a gate that nothing in this round justifies closing.

### Required correction

Add the `00-34-26` dashboard to `INDEX.md` §1 as a sixth row, transcribed verbatim, with its
`Carries a period?` column reading **NO — the columns are TIMEFRAMES, not lookback periods**, and
note that the frame is a **student-supplied chart** per `[00:34:19]`. **Rescope the categorical
sentence** from *"every legend legible in any V12 frame"* to *"every legend and on-screen readout
block identified in the 28 curated frames"*. Superseded text retained in place
(`REMEDIATION_PROTOCOL.md` §2). **`A-080`'s status does not change.**

---

## ⭐ `PT-040` — RE-DERIVED INDEPENDENTLY, END TO END

### The re-derivation

I wrote `reviewer_pt040.py` from `PT-040` §§3–5 and `COMMON_PROTOCOL.md` §§1–3 **alone**, before
opening `run_pt040.py`. It parses the four raw HistData CSVs directly (**not** the student's
`_cache`, and **not** the pre-aggregated `GBPUSD_M15_ARMA.csv`), implements its own M15 aggregation,
its own Wilder RSI seeded by the simple mean of the first 21 gains and losses, its own simple-average
RSI variant, its own US-DST rule for Arm B, and its own `O1`–`O4`. **It shares no line with
`run_pt040.py` or `mmm_lib`.**

**Every Wilder cell reproduced to the printed decimal.**

| Quantity | Submission | **Reviewer, independently** | |
|---|---|---|---|
| M1 bars parsed | — | **1,297,781** | ✅ |
| `W-A` bars / valid / discarded | 24,755 / 24,730 / 25 | **24,755 / 24,730 / 25** | ✅ |
| `W-A` span | 2015-01-04T17:00 → 2015-12-31T16:45 | **identical** | ✅ |
| `W-B` bars / valid | 49,421 / 49,396 | **49,421 / 49,396** | ✅ |
| `O1`, all 20 cells, `W-A`/A | 99.74 … 0.04 | **all 20 exact** | ✅ |
| **`O2`, all 15 cells, `W-A`/A** | 0.08 … 10.48 | **all 15 exact** | ✅ |
| **`M`** | **10.481 pp** at `k=5, t=50` | **10.4812 pp at `k=5, t=50`** | ✅ |
| **`M` at `k = 2`** | **5.16 pp** | **5.1638 pp** | ✅ |
| `O3`, all 20 ratios | 1.000 … 0.200 | **all 20 exact** | ✅ |
| `O4`, all 16 cells | 85.03 … 0.21 | **all 16 exact** | ✅ |
| Arm A vs Arm B, worst `O2` gap | 0.000 pp | **0.0000 pp** | ✅ |
| `N2` — `W-B`/A max `O2` | 10.661 pp | **10.6608 pp** | ✅ |
| `D-035` holdout | never opened | **asserted in my own run: no bar ≥ 2016-07-01** | ✅ |

### The verdict, re-derived rather than read

```text
REVIEWER'S OWN COMPUTATION:
  M = 10.4812 pp   (k=5, t=50)
  PRE-REGISTERED BANDS:  <=2.0 IMMATERIAL | 2.0-5.0 INCONCLUSIVE | >5.0 MATERIAL
  VERDICT: MATERIAL
```

**I agree with the verdict, and I reach it from my own numbers.** The claimed **10.48 pp** and the
claimed **5.16 pp at `k = 2`** are both confirmed. `A-084`'s promotion to an **active blocker** and
the ruling that **V11's RSI threshold claims stay blocked** follow mechanically from the
pre-registered rule.

### All four pre-registered secondary checks — re-derived and all four hold

| Check | Expectation | **My measurement** | |
|---|---|---|---|
| Arm A vs Arm B | within `0.5 pp` | **exactly `0.0000 pp`** | ✅ |
| `O1(k=1, t=50)` | in `[45%, 55%]` | **49.11%** | ✅ |
| `O3(k,t) < 1.0` for `k ≥ 2` | a smoothed series crosses less | **0.200 – 0.737, all 15** | ✅ |
| `N2` — `W-B` same band | same band | **10.6608 pp → `MATERIAL`** | ✅ |

**The `0.000 pp` arm agreement is a check that could have failed and did not**, and `BT_V12_0001` §4
is right to call it positive evidence for `mmm_lib.shift_to_arm`. My own Arm B implementation — a
hand-written 2007-rule US-DST function — reproduces it independently.

### Pre-registration ordering — verified, not accepted

| # | Check | Result |
|---|---|---|
| 1 | Pre-registration committed before the runner | ✅ `83110f1` **22:00:37** → `69539c5` **22:04:22** |
| 2 | **The runner provably does not exist at the pre-registration commit** | ✅ **`git cat-file -e 83110f1:…/run_pt040.py` returns ABSENT.** So does the output. `D-026` satisfied **by ordering, not by assertion** — the report's §1a claim is exactly right |
| 3 | Pre-registration commit contains *only* the design | ✅ `--stat`: **1 file, 284 insertions** |
| 4 | Thresholds fixed before the numbers | ✅ §5's bands are in `83110f1` in full; **no boundary moved** |
| 5 | Window is inside `D-035` DEVELOPMENT | ✅ `W-A` and `W-B` both end 2015-12-31; my own run asserts no bar ≥ 2016-07-01 |
| 6 | QA gate cited as a precondition | ✅ `GATE: PASS — C1-C4 clean`, with the four-file SHA-256 manifest in the output header |
| 7 | Both `D-031` arms reported for every observable | ✅ four cells throughout |
| 8 | `EVIDENTIAL`/`DESCRIPTIVE` classification present and honest | ✅ §1, four rows. **`O1`, `O3` and `O4` are all `DESCRIPTIVE` and none is used in a verdict**; only `O2` is `EVIDENTIAL` |
| 9 | Not-measured content at equal prominence (`E25`) | ✅ `PT-040` **§2 is the file's second section, before the construction**, and `BT_V12_0001` §6 restates it |
| 10 | Deviations reported | ✅ §1a item 2: none, and I found none |

**One process observation, recorded as `N4` and not charged.** `PT-040`'s runner, its output, its
scoring report and the `A-084` record update are **all in the single commit `69539c5`**, where
`PT-039` used four separate commits. **No rule requires the split** — `D-026`'s requirement is that
the *pre-registration* precede the run, and that is demonstrated. But the repository can no longer
demonstrate *"output committed before the scoring"*, which V11's history could. Worth restoring as a
convention.

### The report's honesty is the thing worth naming

`BT_V12_0001` §3's boxed note — *"the session that had every incentive to find `A-084` immaterial
wrote the bar down first"* — is **accurate, and I verified the incentive is real**: `A-080` closed at
`3720833` (21:57:48), two hours of session time before the pre-registration, and its whole point was
to unblock V11's RSI half. **The test the session designed defeated its own headline finding, and
the report leads with that rather than burying it.**

### `O1`'s unanticipated reading — checked, and the handling is right

`RSI(21)` reaches `80` on **0.11%** of bars and falls below `20` on **0.26%** — I reproduce both.
The report gives **both** directions (the rarity matches `[00:25:38]`'s *"dropping for a few days"*;
but an overbought line touched once in nine hundred bars is an odd thing to print as a parameter),
**adopts neither**, and classifies `O1` `DESCRIPTIVE`. That is the correct handling of a number that
brushes against a trend-conditional claim `A-070`/`A-004` block.

---

## ⭐ THE MAYO / 200 UPGRADE — VERIFIED ON BOTH MEDIA

**Reviewer verdict: the citation is CORRECT, the upgrade is CORRECTLY SCOPED, and `D-043`'s mapping
is CORRECTLY LEFT UNCHANGED. This is the best-handled item in the submission.**

### The audio — my own third-engine pass

`faster-whisper medium.en`, `00:31:05`–`00:32:05`, verbatim:

> *"Look what happens here. You have a 28 pip Asian range, perfect. Price comes out and **it's held
> by the mayonnaise perfectly. It's held by the 200**, okay. Shark fin to the high side…"*

**Two adjacent sentences, one chart, one moment, the object named twice.** The project transcript's
own ASR garbles this to *"held by the man is"* / *"Tell by the 200"*; the student's `small.en` reads
*"held by the mayonnaise perfectly. Held by the 200"*; **mine reads the same.** Three engines.

And the second passage, `00:26:05`–`00:27:40`, my own pass:

> *"**Shark fin hold the mayo**, it's like a sandwich… if you add an extra filter like my friend
> Zaim had mentioned, **perhaps a 200 EMA**… **a spike to the mayonnaise would be it**… right past
> the mayonnaise, almost like the mayonnaise offers support… people take a **close below the 200** as
> a trade signal… but notice **the mayonnaise has risen**."*

**Confirmed at every point.** And a third, `00:37:12`: *"shark fin long, **hold the mayo. The dealer
works the mayonnaise.**"*

### The print — I opened both frames

| Frame | Burned | **What I read on the image** |
|---|---|---|
| `V12_00-31-31_…png` | `31:31 / 55:1` | **`TDI VB BREAK, PRICE HELD BY 200 FOLLOWED BY MB BREAK, LOWER VB BREAK EXIT`** — black on white, full width. ✅ The record's partial quote is accurate |
| `V12_00-26-11_…png` | `26:11 / 55:1` | **`Shark Fin  Hold The Mayo`** — large, centred, white on the chart. ✅ **Exactly as claimed** |

**The identification survives without the audio**, as `A-020` claims: the caption names the 200 at
the same second the speaker names the mayonnaise.

### Was `D-043` left alone? — checked row by row

**Yes. One warrant moves; no value moves.**

| Nickname | `D-043` value | V12 entry | Reviewer check |
|---|---|---|---|
| Mayonnaise | 200 | warrant → **`RESOLVED BY COURSE`**, value **unchanged** | ✅ **Correct.** `D-043` says mayo = 200; V12 says mayo = 200. **The first entry in this family that AGREES with what it supersedes** |
| Mustard | 5 | unchanged, `OWNER ATTESTATION` | ✅ **`mustard` occurs 0× in V12** — I verified by word-boundary census |
| Ketchup | 13 | unchanged, `OWNER ATTESTATION` | ✅ **`ketchup` 0×** |
| Water | 50 | unchanged, `OWNER ATTESTATION` | ✅ **and the `[00:03:53]` trap was correctly refused** — see below |
| Blueberry | 800 | unchanged, `RESOLVED BY COURSE` (V09) | ✅ **`blueberry` 0×** |

**`D-042` §1's exhaustive negative is therefore intact**, and the record says so: *"No Tier 1
statement attaches a period to ketchup or mustard anywhere in V01–V12."* I confirmed the V12 half of
that census myself — `mustard`, `ketchup`, `blueberry`, `raspberry` all **0×**.

### ⭐ The two refusals, and both are right

1. **The `[00:03:53]` student question was NOT used.** The instructor reads a chat message — *"is
   the 50 in the TDI the same as 50 in the MA — water? No, Greg"* — and **flags that he may have
   misread it** (*"I don't know if I read that right"*). My own `c1`-equivalent pass confirms both
   halves. **A-020 declines to treat his *"no"* as asserting the gloss inside the question**, citing
   §3.2 Case D. **That is correct and it was the cheapest available upgrade in the file.** Declining
   to correct a premise is not asserting it.
2. **The COLOUR axis was NOT upgraded** — item 124 explicitly asks a reviewer whether that restraint
   is right or excessive. **My ruling: the restraint is CORRECT, and I would have charged the
   upgrade had it been taken.** See § REVIEWER RULINGS.

---

## `C-019` — VERIFIED ON ALL FOUR LIMBS

**Reviewer verdict: the characterisation is ACCURATE, and the resolution is CORRECT under the
sourcing hierarchy.**

| Limb | Reviewer verification |
|---|---|
| **Tier 2 says the market base line** | ✅ **CONFIRMED AT SOURCE.** `EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md` line 1471, inside the `## PDF page 46` block: *"⋅ the Market base line cross (referred to as Blood in the Water) (2 nd)"*. **The page citation is right** |
| **Tier 1 says the trade signal line, SPOKEN** | ✅ **CONFIRMED BY MY OWN ASR.** `00:19:40`–`00:20:35`: *"When the fin goes back under the water line, back inside the band, and crosses the signal line, **the trade signal line, TSL**, that's where we get **blood in the water**."* Unambiguous |
| **Tier 1 says the trade signal line, PRINTED** | ✅ **CONFIRMED BY OPENING THE IMAGE.** Frame `19:06`, `TDI SIGNALS`, **fourth bullet**, read off the pixels: *"Fin Goes Back Under The Waterline and Crosses The Signal (**Red, Blood In The Water**)"*. The quote in `C-019` is **exact**, including the parenthetical |
| **The two lines are distinct objects in V12** | ✅ **CONFIRMED.** `[00:30:45]` makes the MB break the **first add**, not the entry, and `[00:31:49]` crosses the market baseline and the static 50 as **separate later events** in the same sentence. The ladder in print (`29:11`) reads `Add To The Trade At MB Break And VB Break` |

**The resolution is right.** `SOURCING_HIERARCHY.md` §3.2 **Case A** — Tier 1 clear and specific —
plus §3.3's *"the recording wins"*. Tier 1 here is printed **and** spoken **and** demonstrated on a
worked chart, by the course author, in the lesson that is explicitly the promised treatment of this
indicator. Tier 2 is an anonymous summary of a different seminar. **Filing the `C-xxx` was mandatory
under §3.3, not optional, and it was filed.**

### ⭐ And §3 — the subsidiary divergence — is the better piece of reasoning

`C-019` §3 finds a **second** Tier 1/Tier 2 divergence in the same chapter (the volatility bands'
basis: `MMM-NOTES` p.45 says the market baseline; V12 says the market baseline, then **corrects
himself on a prompt from the chat** to the RSI line) — and **refuses to resolve it in Tier 1's
favour**, because the speaker attaches *"I don't know"*, *"I don't really know"* and *"not sure"* to
every version he offers.

**I verified the p.45 citation** (line 1414, inside `## PDF page 45`: *"Volatility bands which are
similar to a Bollinger band but applied to the market baseline of the indicator instead of price"*)
**and the self-correction** (`[00:16:03]`–`[00:16:20]`, my own pass: *"based on the RSI line itself.
That's what someone said, telling me — not sure… from the RSI line. Thank you."*).

**Invoking `C-011`'s asymmetry here is exactly right**: *"the recording wins"* presupposes a
recording that is clear, and where Tier 1 is itself hedged, **Tier 2 is defeated without a
replacement and the blocker survives**. Carrying it in `A-086` rather than manufacturing a second
`C-xxx` is the correct scope. **This is the finding a session looking for a tidy result would have
skipped.**

---

## `Q-013` — RE-DERIVED AT SOURCE, AND ONE CLAIM DOES NOT SURVIVE

### §1 and §3 — the exact-`diff` claims: **BOTH CONFIRMED EXACTLY**

**I ran the `diff` myself.** Result, verbatim:

```text
$ diff 11_Bootcamp1_Wk4_040812_Part1_51mins/VISUAL_INDEX.md \
       12_Bootcamp1_Wk4_040812_Part2_55mins/VISUAL_INDEX.md
1c1   header:  …Wk4 040812 Part1 (51mins).swf  ->  …Wk4 040812 Part2 (55mins).swf
5c5   VIDEO_12_SCREENSHOT_001_00-02-00.jpg     ->  VIDEO_13_SCREENSHOT_001_00-02-00.jpg
13c13 VIDEO_12_SCREENSHOT_002_00-15-00.jpg     ->  VIDEO_13_SCREENSHOT_002_00-15-00.jpg
21c21 VIDEO_12_SCREENSHOT_003_00-30-00.jpg     ->  VIDEO_13_SCREENSHOT_003_00-30-00.jpg
```

**Four differing lines. Zero content lines. Both files 25 lines.** Every `Timestamp`, `Visual Type`,
`What is visible`, `Instructor's Explanation` and `Trading Significance` is byte-identical between
**Part 1 and Part 2 of the same session** — 51 and 55 minutes of entirely different material.
**`Q-013` §3's headline claim is exact.**

**And the ten-lesson claim is exact too.** I normalised the filename line and the `VIDEO_NN`
identifiers across all 21 lessons and hashed the remainder:

```text
ff040840514b29723b14eda39359ddc1   03, 04, 09, 10, 11, 12, 13, 14, 15, 21   <- TEN, exactly as claimed
3d51ec3c72e8eccdd8300c41d9eba412   16, 17, 18, 19, 20                       <- FIVE, exactly as claimed
```

**Ten of twenty-one share one body; a further five share a second.** Both figures reproduce, and
the upgrade from `Q-009`'s normalised hash to an exact `diff` on a named pair is warranted.

**Also confirmed: the substituted identifier is `V13`, not `V12`** — the generator inherited the
pre-ingestion *"Video 13 of 21"* numbering that `D-017` §2 corrects. I read it in the file.

### §2 — the `EMAs` line: **CONFIRMED, and the shift-by-one characterisation is exact**

```text
- **EMAs:** 5 (Mustard), 13 (Water), 50 (Mayo), 200 (Blueberry), 800 (Raspberry).
```

Against `D-043`: **mustard = 5 is right by accident; water, mayo and blueberry are each shifted one
position too fast; ketchup is absent; `Raspberry` is invented.** Four of five wrong. I confirmed
`Raspberry` occurs **0×** in V12's body. **The boxed note is right that V12 refutes this table from
the tape** — the lesson it is attached to says mayo = 200, in print and in speech, at the same
instant its own fabricated file says mayo = 50.

### §4 — ⚠️ **THE NOVELTY CLAIM IS FALSE. See `M2`.**

---

## ⭐ `M2` — `Q-013` §4's "FIRST TIME" IS THE THIRD TIME, AND THE REGISTER ITSELF RECORDS THE OTHER TWO

### The claim

`Q-013` §4 is headed **"⭐ THE FINDING THIS ENTRY EXISTS FOR: THE FIRST TIME THE GENERATOR'S TEXT IS
*ABOUT THE RIGHT SUBJECT*"**, and opens:

> *"**On eleven previous lessons the fabricated files were wrong in an obvious way** — they described
> Asian boxes and London stop hunts over lessons about equity curves, position sizing or the RSI.
> **On V12 they are not obviously wrong, because V12 really is about the TDI shark fin.**"*

### It is not the first time, and the register says so twice

| Record | What it already says |
|---|---|
| **`Q-003`** (V03), heading of Finding 2 | ***"the new hazard: this time some of the fabricated vocabulary is real"*** — *"Unlike V02… **V03 genuinely discusses TDI (13 mentions), shark fin (3), railroad tracks (5), and stop hunts (8)**. The fabricated `NOTES.md` happens to name real V03 subjects"* — **and it names the same sentence**, *"Green Price Line crossing Red Signal Line after breaking outside Blue Volatility Bands (Shark Fin)"* |
| **`Q-004`** (V04), heading of Finding 3 | ***"the `Q-003` hazard recurs and is worse here"*** — *"The recording really does discuss **TDI (11), shark fin (5)**, stop hunts (4), railroad tracks (4)… A reader skimming `NOTES.md` and the transcript together would find the vocabulary corroborated everywhere"* |

### My own measurement, which is what settles it

I ran a word-boundary census of the TDI vocabulary over every ingested transcript body:

| | `shark fin` | `volatility band` | `blood in the water` | `TDI` |
|---|---|---|---|---|
| **V03** | **3** | **2** | **2** | **12** |
| **V04** | **5** | 0 | **2** | **11** |
| V10 | 2 | 0 | 1 | 1 |
| V11 | 0 | 0 | 0 | 27 |
| **V12** | **20** | **4** | **14** | **46** |

**V03 and V04 both share the ten-lesson `VISUAL_INDEX.md` body with V12**, and I confirmed they also
share the **identical `NOTES.md` `TDI Indicator` sentence** — it is one of three variants across the
21 files, and V01–V04, V09–V15 and V21 all carry V12's exact wording. **So the two sentences §4
identifies as "on-topic for the first time" were equally on-topic for V03 and V04, and the register
recorded that fact at the time.**

### What the true claim is, and why making it strengthens the entry

**V12 is not the first lesson whose fabricated text is on-topic. It is the lesson where the accidental
overlap is most complete** — and that *is* worth saying, because the numbers support it: V03 mentions
the TDI 12 times in 71 minutes as one topic among many; **V12 is 55 minutes of nothing else**, titled
`Traders Dynamic Index` on a card held for eight and a half minutes.

**The correction makes the register stronger, not weaker.** As written, §4 reads as a one-off
curiosity. Corrected, it is **the third and most severe instance of a documented, escalating
hazard** — which is a far better argument for §4's actual conclusion (*"the defence is not
vigilance — it is `Q-007`'s blanket rule and the exact-`diff` test, which do not care whether the
text happens to be true"*). **A recurring hazard is a stronger case for a mechanical rule than a
novel one.**

**Charged as `MINOR`.** The disposition is untouched: all three files stay quarantined, nothing in
V12 draws on them, and I verified that independently. The defect is in a **novelty claim about the
register's own history**, and the register contains the refutation.

### Required correction

Rewrite `Q-013` §4's opening to name `Q-003` Finding 2 and `Q-004` Finding 3 as the **first and
second** instances, restate V12 as the **third and most complete**, and carry the measured counts
(V03: TDI 12 / shark fin 3 / VB 2; V04: TDI 11 / shark fin 5). **Add the observation that V03 and
V04 share both the `VISUAL_INDEX.md` body and the `NOTES.md` TDI sentence with V12**, which is what
makes the three instances one phenomenon rather than three coincidences. Superseded text retained
in place.

---

## `A-082` — THE FLASHCARD SELF-CORRECTION, RE-RUN IN FULL

**Reviewer verdict: the correction is ACCURATE, the census is EXACT, and the reframing is CORRECT.
This is the submission's best process moment.**

### The census — re-derived independently across all 21 lessons

I re-ran `\bflash ?cards?\b`, case-insensitive, word-boundary, marker lines stripped, over the
ingested bodies for V01–V12 and the pre-ingestion transcripts for V13–V21:

```text
V01  0   V02  3   V03 23   V04 17   V05 15   V06  0   V07 14
V08  3   V09  0   V10 12   V11  7   V12  1   V13  3   V14  4
V15  2   V16  1   V17  6   V18  2   V19  4   V20  1   V21  1
```

**TOTAL 119, across 18 of 21 lessons.** **Every one of the 21 per-lesson cells matches the
submission exactly.** Not the total alone — every cell.

### V03 teaches them — I checked seven of the eight citations at their markers

| Marker | Reviewer read at source |
|---|---|
| `[00:12:25]` | *"We're going to cover flash cards and then I'm going to cover the trading zone."* ✅ |
| `[00:40:57]` | *"**I asked you last week to make 40 flash cards** and identify."* ✅ **a QUANTITY** |
| `[00:53:04]` | *"Okay, save your flashcards"* ✅ |
| `[00:58:21]` | *"You know how to make a flash card now, right?"* ✅ |
| `[01:02:41]` | *"**The flashcards are on a 15 minute.**"* ✅ **a TIMEFRAME** |
| `[01:04:20]` | *"Having a flashcard of a loser is not going to help you stay out of it."* ✅ **a selection criterion** |
| `[01:06:51]` | *"Then make your flashcards on the compression you're looking for your entries. If you're going to take a one-hour entry,"* ✅ |

**All seven resolve verbatim at the cited marker.** `A-082`'s premise — *"referred to as already
existing, **never specified**"* — **is false, and the reframing is correct**: V03 supplies a
quantity, a timeframe, a labelling rule and a selection criterion, and what it does not supply is
what goes **on** a card, because that content is itself `A-011`/`A-002`/`A-007`/`A-076`, all open.

### The record was REFRAMED, not silently closed — verified

```text
A-082 -- REFRAMED, NOT CLOSED.
Was: "referred to as already existing, NEVER SPECIFIED"  <- FALSE
Now: "SPECIFIED AS A STUDY PRACTICE IN V03 …; UNSPECIFIED AS TO CONTENT …"
```

The original `A-082` entry is **appended to, not edited** — I confirmed the header block reads
*"Update to the record above, appended. The original `A-082` entry is UNEDITED"* and the prior text
is intact above it. `REMEDIATION_PROTOCOL.md` §2 satisfied.

### ⭐ And the session's own false claim is retained verbatim, which is the point

`V12_SOURCE_NOTES.md` **§9a** carries the superseded draft in a block quote:

> *"`flashcard`/`flashcards` occurs in V11 (×1) and V12 (×1) only — zero occurrences in V01–V10 and
> zero in V13–V21. The object is referred to twice, in one session, and specified nowhere in the
> entire corpus."*

followed by *"**Every clause of that is false.**"* and the diagnosis: it was written from a census
using `\bflashcard\b`, **which does not match the plural**. **I reproduced the error to confirm the
mechanism** — `\bflashcard\b` against V12's body returns **0**; `\bflash ?cards?\b` returns **1**.

**This is the correct handling and it is not self-flattery.** The session recorded an error nobody
would have found, named the mechanism, and generalised it (`V12_INTERPRETATION.md` Q6 lists five
further records that assert corpus-wide negatives without a sweep behind them, **and says plainly
that it did not run them**). The process finding — *"`A-082` was raised against already-ingested,
already-reviewed material; the claim was reachable and wrong on the day it was written, and it
survived V11's own pass **and V11 R1**"* — is **accurate, and it is a finding against this
reviewer's predecessor as much as against V11.** It is recorded without softening.

---

## `A-039` — THE DELIBERATE NON-CLOSURE, SANITY-CHECKED

**Reviewer verdict: the non-closure is CORRECT. I uphold it, and I supply a quantified ground the
session did not have.**

### The session's reasoning

`A-039` narrows to *"TAUGHT IN FULL AS TO MECHANISM, SIGNALS, ENTRY, SCALING AND EXIT. ONE OF FOUR
PARAMETERS SUPPLIED"* and **does not close**, on the stated ground that *"`A-039` is cited as an
upstream blocker by other records — `A-031`'s third narrowing reason is verbatim '`A-039` is upstream
and still blocks' — and closing it here would **silently unblock dependents as a side effect**."*
The record then states the **opposite case at full strength**, calls it *"coherent"*, and hands the
call to R1.

### Is the reasoning sound? — three checks

1. **Is the dependency real?** ✅ **Yes, and it is internally consistent.** `A-031` closes
   `RESOLVED BY COURSE` **as to meaning only**, and its own status block reads *"⚠ NOT YET CODABLE:
   `A-039`/`A-085`/`A-086` leave the TSL and the bands unspecified. The record is closed on MEANING;
   **the reconstruction blocker lives in `A-039`**."* So closing `A-039` without re-pointing would
   leave `A-031` closed with its blocker deleted rather than relocated. **The stated hazard is exact,
   not rhetorical.**
2. **Is the residue actually covered by the replacements?** ✅ **Yes.** `A-039`'s four V11 gaps map
   cleanly: gap 1 → `A-080` (closed), gap 2 → `A-085`, gap 3 → `A-086`, gap 4 → delivered. Plus
   `A-084` for the smoothing. **The split the session describes is mechanically clean.**
3. **How large is the dependency surface?** ⚠️ **Much larger than the record suggests, and this is
   the ground I add.** The session names **one** dependent. I measured it:

```text
git grep -c "A-039" -- '*.md'
  ->  287 references across 65 files
```

**including nine `PT-xxx` pre-registrations, `BACKTEST_EVIDENCE_STANDARD.md`, four mastery reports
and five prior reviews.** A record cited 287 times cannot be closed and re-pointed as a side effect
of a lesson pass.

### My ruling — and a reason stronger than the one given

**`A-039` stays NARROWED. The session was right to decline.**

But the decisive reason is not the one the record gives. *"Closing would unblock dependents"* is an
argument for doing the re-pointing carefully, not against closing. **The decisive reason is
`D-003`:** `A-084`, `A-085` and `A-086` were **opened by this same session**. Closing `A-039` and
re-pointing 287 references at three records the same session had just written would mean the
closure, the replacements **and** the completeness of the re-pointing were all authored by one
session with no independent check. **Deferring the split to a reviewer is not caution — it is the
separation of duties working correctly.**

**Condition for closing it later, stated so the next session does not have to re-derive it:**
`A-039` may close **only** in a dedicated pass that (a) enumerates all 287 references, (b) re-points
each at `A-084`/`A-085`/`A-086` or marks it historical, and (c) is reviewed independently of the
session that opened the three replacement records. **It is not V13's work and should not be bundled
into a lesson pass.**

---

## THE SPEAKER DETERMINATION — RE-VERIFIED

**Reviewer verdict: CORRECT. Confidence HIGH. Over-determined, and correctly tested rather than
inherited from V11.**

The strongest point is procedural and the submission gets it right: **V11 R1 confirmed the course
author at 100% for Part 1 of this same recording, and V12 tested it again anyway** on strands fixed
before the answer was known. Four of the nine strands are **new evidence unavailable in Part 1** —
forum ownership, the DMR paid tier, the New Jersey venue, and template distribution.

I checked the strands most capable of being wrong:

| Strand | Reviewer finding |
|---|---|
| 2 — owns the templates | ✅ `[00:07:46]` *"the way it's **preset in the templates** is the way **I** want us to learn how to use it"* — verified in **my own ASR**, not only the transcript |
| 4 — owns a forum section | ✅ `[00:42:25]`, `[00:42:37]`, `[00:45:43]` all verbatim: *"in the forum **I post in the homework section**"*, *"if you go under **my section**"*, *"Post under **my homework section**"* |
| 8 — disclaims the one thing he did not write | ✅ **the strongest strand, and verified in my own pass:** *"**TDI does not belong to me. I didn't invent it**, belongs to Compass and Dean Malone… **I've altered it or tweaked it a little bit**."* A guest has no standing to alter the group's preset |
| 9 — handover scan returns zero | ✅ **CONFIRMED, and I widened it.** I ran the 17-pattern superset plus *joining us · our guest · I'll turn it over · give you the (mic\|screen) · you're up*: the only hit is `[00:52:25]` *"I'll let you know, stand by"*, which is not a handover |

**And the safeguard holds.** `D-025` consequence 4 requires that nothing depend on the identification
being right. `PT-040` reads closes and never a speaker; `A-080`, `A-020`, `A-031` and `A-032` all
close on statements whose speaker is the same person under either hypothesis; `D-033` makes all
speakers equal in authority in any case. **If this determination were overturned tomorrow, not one
number or verdict in V12 would move.**

**The acoustic screen was correctly not run** — V07's prohibition honoured, as in V08–V11.

---

## RULE FIDELITY

**Grade: PASS.**

**Spoken quotations spot-checked at nine passages by independent ASR** — `[00:07:24]`, `[00:07:53]`,
`[00:08:09]`, `[00:10:51]`, `[00:15:13]`, `[00:19:51]`–`[00:20:14]`, `[00:26:11]`–`[00:27:30]`,
`[00:31:22]`–`[00:31:52]`, `[00:37:20]`. **All nine resolve verbatim at the cited marker.**

**Printed content checked by opening the images** at `19:06`, `26:11`, `31:31`, `34:26`. **All four
render exactly as transcribed**, including the `19:06` bullet's parenthetical `(Red, Blood In The
Water)`.

**Qualifiers are carried, not dropped.** The three most convenient to lose are all present:

- `[00:08:22]` *"**You want to use it at 14, knock yourself out**"* — the permissive that makes `21`
  a preference rather than a law, carried into `A-080` rather than suppressed.
- `[00:15:54]` *"**I don't really know because I didn't invent it**"* and `[00:16:12]` *"**not
  sure**"* — carried into `A-086` and into `C-019` §3, where they are the reason a contradiction is
  *not* resolved in Tier 1's favour.
- `[00:27:59]` *"this is the **67**"* — a number attached to a TDI level, **explicitly recorded as
  unverified and NOT adopted** in the transcript's own defect table. Correct: it is the one number
  in the file a session could have harvested and it was fenced instead.

---

## MACHINE-RULE FIREWALL

**Grade: PASS.**

`21` enters the corpus as **the RSI's period, on the instructor's own statement** — and `PT-040`
then demonstrates that this closure is **necessary and not sufficient**, because the series the
period belongs to is still ambiguous (`A-084`). **No smoothing length is adopted anywhere**;
`PT-040` §2.3 refuses it in advance, `BT_V12_0001` §6.3 restates it, and I confirmed that `k = 5`
attaining `M` is nowhere converted into a claim that the line is smoothed by 5.

**No TDI is built.** Three of four parameters are unstated and `A-039` keeps the `DO NOT CODE` fence
in place. **No colour is converted into a period** — see the ruling below. **`Raspberry`, invented by
the fabricated files, appears in no V12 artifact except as a refutation.**

---

## HINDSIGHT / LOOKAHEAD AUDIT

| Surface | Result |
|---|---|
| `PT-040`'s `O2` | **CLEAN — re-derived.** `(S_k ≥ t) XOR (R ≥ t)` is a contemporaneous comparison of two series at the same bar. `S_k` is a **trailing** mean of `R` over `k` bars — I verified my own implementation uses only bars `≤ i`, and it reproduces the submission exactly, which means the submission's does too |
| `PT-040`'s warm-up | **CLEAN.** 21 bars to the RSI seed plus 4 to the `k=5` window = 25 discarded, reproduced exactly. No bar is scored before its inputs exist |
| `PT-040`'s window | **CLEAN.** My own run asserts no bar ≥ 2016-07-01. The `D-035` holdout was not touched |
| Any threshold moved after the numbers | **NONE.** §5's bands are in `83110f1`, which provably contains no runner and no output |
| The homework | **No decision, no entry, no outcome.** It is a curriculum exercise; it computes nothing |

**No `E09`, no `E23`, no lookahead of any kind found.**

---

## HOMEWORK

**Grade: SATISFIED — and this discharges V11's outstanding gap.**

V11 `[00:00:46]` promised *"a really good assignment coming up this week… I'm gonna insist that you
do it"* and ended 50 minutes later without giving it; **V11 R1 graded that dimension `PARTIALLY
SATISFIED` and recorded the absence as the source's, not the work's.** **V12 gives the assignment**,
in print (`42:06`, `THIS WEEKS R & D`) and in speech at far greater length (`[00:42:09]`–`[00:49:08]`).

I read the assignment at source. It is the most specific homework in the corpus: black out price
action, stretch the TDI across the screen, **execute five live demo trades on EURUSD and GBPUSD using
nothing but the TDI and a wristwatch**, and post the results. The submission carries it accurately,
including the wristwatch condition (`[00:45:17]`, which exists to stop the student trading TDI
signals *"at two in the afternoon"*) and the pair restriction (`[00:46:27]`).

**The homework is correctly recorded as `UNRESOLVED` rather than performed or simulated.** It
requires a live demo account and a human at a screen; inventing results would have been the `D-030`
error in curriculum form. **Correct handling.**

---

## AMBIGUITIES AND CONTRADICTIONS

| Record | Reviewer assessment |
|---|---|
| **`A-080`** — CLOSED | **CORRECT.** Re-verified at source with a third ASR engine, all five citations. Its stated frame evidence is defective at one point — `M1` |
| **`A-064`** — CLOSED | **CORRECT.** The printed `Hold The Mayo` at the same second the ASR reads *"hold the mail"* closes the three-rendering hazard **by demonstration**, which is stronger than argument |
| **`A-020`** — mayo row to Tier 1 | **CORRECT AND CORRECTLY SCOPED.** One warrant moves, no value moves, `D-043` intact, the colour axis correctly refused, `A-020` correctly stays on `SOURCING_HIERARCHY.md` §3.4's list for the three owner-attested rows |
| **`A-031`** — CLOSED as to meaning | **CORRECT.** The "as to meaning / not yet codable" split is precise and the Tier 2 basis is **replaced**, not supplemented, per §3.1 step 5 |
| **`A-032`** — CLOSED | **CORRECT.** `[00:19:28]`–`[00:19:51]` defines the shark fin mechanically (vector candle forces the line outside the band; the pullback turns it over) **and** explains the metaphor. Printed at `19:06` |
| **`A-039`** — NARROWED, not closed | **UPHELD.** See § `A-039` |
| **`A-082`** — REFRAMED | **CORRECT.** Census reproduced exactly, 21 of 21 cells |
| **`A-084`** — new, promoted to ACTIVE BLOCKER | **CORRECT, and the promotion is earned by a pre-registered test I reproduced** |
| **`A-085`, `A-086`** — new | **CORRECT.** Both are genuine gaps. `A-086`'s handling of the retracted basis is the better of the two |
| **`C-019`** — opened and resolved | **CORRECT on all four limbs.** See § `C-019` |
| **`Q-013`** — fabrication | **CONFIRMED by exact `diff` at source**, with one false novelty claim — `M2` |

---

## REVIEWER RULINGS ON THE QUESTIONS PUT TO R1

The submission puts three questions to this reviewer. All three are answered.

### Item 124 — the colour axis: is the restraint right, or excessive?

**RULING: the restraint is CORRECT. I would have charged the upgrade as a finding had it been
taken.**

I opened both frames. The submission's description is accurate: on `31:31` and `26:11` price is held
at a **white** line under captions naming the 200 and the Mayo respectively. **It is genuinely
suggestive** — and it is not admissible, for a reason that is mechanical rather than a matter of
taste:

**`COMMON_PROTOCOL.md` §2 forbids measuring anything off a rendering.** *"A chart may be looked at;
nothing may be measured off one."* Reading *"the white curve is the 200 EMA"* off pixels is a
measurement off a rendering, and the fact that it would confirm `D-043` rather than contradict it
makes it **more** dangerous, not less — a convenient confirmation is exactly the kind that gets
adopted without scrutiny.

**And I add a strand the submission does not cite, precisely to show it still does not close the
gap.** On both frames the four price-pane curves are ordered by responsiveness — **yellow hugs price
most closely, then red, then cyan, then white as the slowest and flattest.** That ordering is
consistent with `D-043` on **all four** colour rows (5 = yellow, 13 = red, 50 = aqua, 200 = white),
and unlike the "which line held price" argument it appeals to a mathematical property rather than to
a caption. **It is still a read off a rendering and still closes nothing.** I record it as
**corroboration that must not be promoted** (`N5`), which is the same disposition the session
reached by a shorter route.

**Item 124 can be closed:** the restraint is upheld, and the record should note that a reviewer
examined the frames independently and reached the same refusal.

### Item 130 — should `A-039` close?

**RULING: NO. It stays NARROWED.** See § `A-039` for the reasoning and for the condition under which
it may close later. **Item 130 can be closed** as adjudicated.

### Item 135 — is `EXTERNAL_VOCABULARY_REFERENCE.md` a POLICY or an EVIDENCE ledger?

**RULING: EVIDENCE ledger. The session classified it correctly and edited it on the task branch
correctly.**

`D-038a`'s own test is *"does an unmerged edit to this file change what another session is permitted
to do?"* The tempting answer is yes, because §9.2 entries carry Tier 2 material that **can** close a
record. **But the permission to close on Tier 2 does not come from this file** — it comes from
`D-039` and `SOURCING_HIERARCHY.md`, both of which are POLICY ledgers and both of which live on
integration. `EXTERNAL_VOCABULARY_REFERENCE.md` records **what the external documents say**, not
**what may be done with them**. Under the test, it is evidence.

**Forward requirement:** `D-038a`'s table should name this file explicitly on the integration branch,
so the next session does not have to re-derive the classification. Recorded as `N6` and as a reviewer
question.

---

## STUDENT MASTERY ASSESSMENT

| Dimension | Student | Reviewer | Note |
|---|---|---|---|
| A. Recall | SATISFIED | **AGREE** | Nine passages re-verified by independent ASR, all verbatim |
| B. Recognition | SATISFIED | **AGREE** | The four-component build, two setups, three-rung ladder and exit are all carried with their sources |
| C. Discrimination | SATISFIED | **AGREE** | `[00:22:12]` *"this is not a freaking long trade because it hit the Asian box twice"* is a genuine negative example and is captured |
| D. Sequence | SATISFIED | **AGREE** | The ladder's ordering is carried in both print and speech |
| E. Exceptions | SATISFIED | **AGREE** | `[00:33:51]`'s *"not during the stop hunt but during the actual trend run"* is carried as a condition on the second add, not flattened |
| F. Homework | UNRESOLVED | **AGREE** | Correctly not simulated. **V11's gap is discharged by this lesson** |
| G. Manual backtesting | SATISFIED | **AGREE — and this is the strongest dimension.** Re-derived end to end; every Wilder cell reproduces to the printed decimal, and the test defeats the session's own headline finding | |
| H. Provenance | SATISFIED | **AGREE** | Nine strands, four of them new to Part 2, tested rather than inherited from V11 R1 |
| I. Ambiguity | SATISFIED | **AGREE**, subject to `M1`'s correction to `INDEX.md` §1 |
| J. Contradictions | SATISFIED | **AGREE**, subject to `M2`'s correction to `Q-013` §4 |

**Overall: this is the strongest submission in the sequence I have seen, and the reason is
structural rather than stylistic.** V12 had the corpus's single largest blocker fall in its lap — a
parameter, stated four times, by the author, about his own template — and the obvious move was to
bank the unblock. **Instead it opened `A-084`, pre-registered a test that could only take the unblock
away, and published the result that took it away.** The student status is correctly recorded as
`REVIEW REQUIRED` rather than self-certified, and the V13 gate was correctly held closed pending
this review (`D-004`).

---

## ALL FINDINGS BY SEVERITY

### CRITICAL — none
### MAJOR — none

### MINOR

| # | Item | Finding |
|---|---|---|
| `M1` | **137** | **`04_SCREENSHOTS/V12/INDEX.md` §1's categorical *"Every legend legible in any V12 frame is transcribed below"* is FALSE.** Frame `00-34-26` carries an untranscribed sixth text block: a multi-timeframe dashboard with rows `MACD / STR / EMA` over columns `1 · 5 · 15 · 30 · H1 · H4 · D · W · MN`, plus `108.093`, `Spread 33`, `Pips to Open`, `Hi to Low 315`, `Daily Av`. **`A-080` is UNAFFECTED and its negative is STRENGTHENED**: the columns are timeframes not lookback periods, the `EMA` row carries no number, and the chart is a **student's** (`[00:34:19]`). The dashboard appears on **no other frame** — I checked four. **This is the same class of defect V11 R1 item 109 charged, inside the very section written to discharge it.** Add the sixth row; rescope the categorical sentence |
| `M2` | **138** | **`Q-013` §4's *"THE FIRST TIME THE GENERATOR'S TEXT IS ABOUT THE RIGHT SUBJECT"* is FALSE, and the register itself records the other two instances.** `Q-003` Finding 2 is headed *"the new hazard: this time some of the fabricated vocabulary is real"* and names **the same `NOTES.md` sentence**; `Q-004` Finding 3 is headed *"the `Q-003` hazard recurs and is worse here"*. Measured: **V03 — TDI 12, shark fin 3, volatility band 2, blood in the water 2; V04 — TDI 11, shark fin 5** — and both share the ten-lesson `VISUAL_INDEX.md` body **and** the `NOTES.md` TDI sentence with V12. **The correction STRENGTHENS the entry**: V12 is the **third and most complete** instance of a documented escalating hazard, which is a better argument for §4's own conclusion than novelty was. Disposition unchanged; all three files stay quarantined |

### NOTE

| # | Item | Observation |
|---|---|---|
| `N1` | **139** | **⭐ `PT-040` REPRODUCED EXACTLY BY INDEPENDENT RE-DERIVATION — and one under-specification found in `N3`.** Every **Wilder** cell matches to the printed decimal across three cells (`W-A`/A, `W-A`/B, `W-B`/A): `O1` ×20, `O2` ×15, `O3` ×20, `O4` ×16, bar counts, spans, `M = 10.4812`, `k=2` max `5.1638`. **The `N3` simple-average cell differs by ≤ 0.02 pp** (e.g. `k=5,t=50`: 12.15 vs my 12.14). **Cause identified precisely:** `PT-040` §3.1 names *"the simple-average variant"* without giving its formula; the runner uses a **prefix-sum** rolling mean, I used a **direct windowed sum**. They differ by at most **5.16 × 10⁻¹¹** — but **48 bars in `W-A` sit at exactly `RSI = 50.0`** (up-sum equals down-sum exactly), and `O2`'s `≥` comparison is **tie-sensitive**, so float noise flips 15 of them. **No verdict moves; both are `MATERIAL`.** Not charged — `N3` is a reported line, not a decision. **Forward requirement: the next `PT` with a formula-robustness line should state the summation and the tie convention** |
| `N2` | **140** | **The *"all 672 sweep frames"* scan is NOT verifiable by repository inspection**, because the sweep frames are not committed — the same class of limit V11 R1 recorded at `N6` for push timing. **What IS verifiable was checked and holds:** the 28 committed frames contain no properties dialog and no Navigator panel; the six timecode-sync rows in `INDEX.md` §0 spot-check correct; the `26:11` print-vs-audio cross-check lands on the same second; and **the load-bearing observation — that MT4 prints inputs in parentheses after an indicator's name and here there are none — I confirmed by reading two TDI legends off the pixels.** Recorded so the claim's status is explicit. **Not charged** |
| `N3` | **141** | **A sentence supporting `A-080` that the record does not cite, and it forecloses the last alternative reading.** `[00:08:22]`, my own ASR: *"**You want to use it at 14, knock yourself out.**"* The instructor contrasts his preset against the RSI's own default **as a choice he is consciously making** — which rules out the readings that `21` is a misspeak, or that he is reporting someone else's setting. **Worth adding to `A-080`'s evidence table**, where it costs nothing and closes the last door |
| `N4` | **142** | **`PT-040` bundles the runner, the output, the scoring report and the `A-084` update into ONE commit (`69539c5`), where `PT-039` used four.** **No rule requires the split** and the load-bearing ordering is intact and verified — `83110f1` provably contains the design and **no runner and no output**, so `D-026` is satisfied by ordering. But the repository can no longer demonstrate *"output committed before scoring"*, which V11's history could and which V11 R1 checked as procedural checks 2–4. **Restore the convention in the next `PT`** |
| `N5` | **143** | **A colour strand this reviewer found, recorded WITH its refusal.** On frames `31:31` and `26:11` the four price-pane curves are ordered by responsiveness — **yellow hugs price most closely, then red, then cyan, then white slowest** — which is consistent with `D-043` on **all four** colour rows and appeals to a mathematical property rather than to a caption. **It still closes nothing:** `COMMON_PROTOCOL.md` §2 forbids measuring off a rendering, and a *convenient* confirmation is the kind most likely to be adopted without scrutiny. Recorded as corroboration that **must not be promoted**, which is the disposition the session reached by a shorter route — see the item 124 ruling |
| `N6` | **144** | **`D-038a`'s table should name `EXTERNAL_VOCABULARY_REFERENCE.md` explicitly.** Item 135 correctly classified it an **EVIDENCE** ledger and this reviewer upholds that (the permission to close on Tier 2 comes from `D-039` and `SOURCING_HIERARCHY.md`, both POLICY and both on integration; this file records what the sources *say*). **The classification was re-derived twice now — by the V12 session and by this reviewer — which is exactly the waste `D-041` complained of.** Write it into the table on the integration branch. **Policy-ledger change; not V12's to make** |

---

## REQUIRED CORRECTIONS

Carried as `REVIEW_INDEX.md` items **137–138**. **Neither holds the V13 gate** (`D-024`); both are
owed before V12 reaches `COMPLETE`.

1. **Item 137 (`M1`).** Add the `00-34-26` multi-timeframe dashboard to `04_SCREENSHOTS/V12/INDEX.md`
   §1 as a sixth row, transcribed verbatim, with `Carries a period?` = **NO — the columns are
   TIMEFRAMES, not lookback periods**, and a note that the frame is a **student-supplied chart**
   (`[00:34:19]`). **Rescope** the categorical sentence to *"every legend and on-screen readout block
   identified in the 28 curated frames"*. Superseded text retained in place
   (`REMEDIATION_PROTOCOL.md` §2). **`A-080`'s status does not change.**
2. **Item 138 (`M2`).** Rewrite `Q-013` §4's opening to name `Q-003` Finding 2 and `Q-004` Finding 3
   as the first and second instances, restate V12 as the **third and most complete**, and carry the
   measured V03/V04 counts and the fact that both share the `VISUAL_INDEX.md` body **and** the
   `NOTES.md` TDI sentence with V12. Superseded text retained in place.

**Two forward requirements, charged to no one:** state the summation and tie convention in the next
`PT` carrying a formula-robustness line (`N1`), and restore `PT-039`'s commit separation (`N4`).

---

## REVIEWER QUESTIONS

1. **`D-038a`'s table should be amended on the integration branch** to name
   `EXTERNAL_VOCABULARY_REFERENCE.md` as an EVIDENCE ledger (`N6`). This reviewer has ruled on the
   classification; writing it down is a policy-ledger act and belongs to the owner or to an
   integration-branch session.
2. **Item 113's `mmm_lib.provenance_header()` seed defect is still open** and `PT-040` inherits the
   misleading banner — harmlessly, because the test uses no randomisation, and **`PT-040` §7 said so
   in advance**, which is the right handling. The library fix is still owed. Carried unchanged from
   V11 R1 reviewer question 1.
3. **Item 95's standing question (from V10 R1) is still open** and V12 adds no instance either way.
   Carried unchanged.

**No question is put back to the owner on the nickname mapping.** `D-043` is agreed with by V12, not
challenged, and this reviewer verified that `mustard`, `ketchup`, `blueberry` and `raspberry` occur
**0×** in V12 — so `D-042` §1's exhaustive negative is undisturbed.

---

## ADVANCEMENT DECISION

```text
VERDICT:        REVISE
SEVERITY:       0 CRITICAL / 0 MAJOR / 2 MINOR / 6 NOTE
GATE TO V13:    OPEN  (D-024 -- zero CRITICAL, zero MAJOR)
V12 STATUS:     IN REMEDIATION (items 137-138 owed before COMPLETE)
CONFIDENCE:     HIGH
```

**`COURSE_PROGRESS.md` should be updated: the V13 gate reads `CLOSED until V12's R1 returns`, and
this is that R1.** It opens. Neither minor is capable of contaminating V13: `M1` corrects a
completeness claim about images while leaving the finding it supports intact and strengthened, and
`M2` corrects a claim about the quarantine register's own history while leaving every file
quarantined.

**One thing V13 inherits that is worth stating in the gate.** `A-084` is now an **active blocker**
and V11's RSI threshold claims are **still blocked** — so the single cheapest unblock available to
V13 is a course statement of the TDI's smoothing length, or a statement that the plotted line **is**
the RSI. `BT_V12_0001` §8 names all three forms this could take and says `V13` is the next place any
could appear. **That is the correct forward pointer and V13 should carry it.**

---

## REVIEWER'S SUMMARY JUDGEMENT

**This is the strongest submission in the sequence, and the reason is worth naming precisely because
it is the opposite of what a strong submission usually looks like.**

Three things it does that are hard:

1. **⭐ It built the instrument that destroyed its own headline.** V12 closed `A-080` — the corpus's
   largest single blocker — at 21:57. Three minutes later it opened `A-084`, which asks whether the
   closure is worth anything. Three minutes after that it committed a pre-registration with the bar
   set at 5 pp, **before the runner existed**, and then measured **10.48**. The unblock evaporated.
   **The session that had every incentive to find the ambiguity immaterial wrote the threshold down
   first and then published the number that took its own prize away**, and led the report with it.
   I reproduced the number from raw CSVs with code that shares nothing with theirs, and it is right.
2. **It overturned a record by running the sweep it was describing — after asserting the same
   falsehood itself.** `A-082`'s *"never specified"* was wrong, had been wrong since V11, and had
   survived V11's own pass **and V11 R1**. What caught it was a carry-forward naming the command and
   V11's disclosure that it had **not** run it. **And the V12 session's own first draft repeated the
   error**, from a regex that silently missed the plural — **and that draft is retained verbatim in
   `V12_SOURCE_NOTES.md` §9a rather than quietly replaced.** I reproduced both the error and the
   correction. 119 occurrences, 18 of 21 lessons, every cell.
3. **It refused three free upgrades in a row.** The colour axis (two frames practically hand it the
   mayo/white row); the `[00:03:53]` chat question (which appears to hand it water = 50); and
   `A-039` (which V12 plainly does teach). **Each refusal cost the session something and each is
   correct** — I checked all three and upheld all three, and on the colour axis I found a *further*
   strand and refused it too.

**`M1` is the finding a reading-only review would not have produced, and it is worth being precise
about what it means.** It does **not** mean `A-080` is wrong — `A-080` is right, verified at source
by a third ASR engine on all five citations, and the frame evidence was never load-bearing. It means
that a section written **specifically to discharge V11 R1 item 109** — and which did an unusually
good job, transcribing five blocks including a hover tooltip nobody would have thought to look for —
**still ended in a categorical sentence that a sixth block falsifies.** The generalisation is the
same one V11 R1 reached and it needs one more turn: *a categorical claim about images has to be
tested against the images, and the block you miss will be the one that is not shaped like the thing
you were told to look for.* V11 looked for legends and recorded a pane count. V12 recorded the
legends and missed a dashboard.

**`M2` is the more satisfying finding, because the correction helps.** `Q-013` §4 identifies a real
and genuinely dangerous phenomenon — fabricated text that happens to be true — and argues correctly
that the defence must be mechanical rather than vigilant. It then oversells it as novel, and the
register two hundred pages above already records it twice, on the same sentence, with the headings
*"the new hazard"* and *"the hazard recurs and is worse here"*. **Corrected, the entry is stronger:
three instances of an escalating pattern is a far better case for `Q-007`'s blanket rule than one
curiosity.**

**Nothing in this round changes confidence in any other V12 finding.** `A-080` is verified on the
audio by a third engine. The mayo/200 identification is verified in print and in speech, on three
passages, by three engines. `C-019` is verified on all four limbs including both Tier 2 page
citations. `Q-013`'s exact `diff` and its ten-lesson count reproduce precisely. `PT-040` reproduces
to the last printed decimal in every Wilder cell. And `A-039`'s non-closure — the one call the
session explicitly handed to a reviewer — is right, for a reason **stronger** than the one it gave.

---

## REVIEWER SELF-CHECK

| Question | Answer |
|---|---|
| Did I author any part of V12? | **No.** `D-003` satisfied. Separate session, separate worktree, separate branch, cut fresh from integration head |
| Did I read the source before the student's conclusions? | **Yes.** The full 690-marker body first, then the frames, then the quarantined tree, then the artifacts |
| Did I re-derive the numbers or read them? | **Re-derived.** `reviewer_pt040.py`, written from the pre-registration and `COMMON_PROTOCOL.md` alone, parsing 1,297,781 raw M1 bars — no shared line with `run_pt040.py` or `mmm_lib`, and `run_pt040.py` was not opened until after my run completed |
| Did I verify the audio independently, or trust the transcript? | **Independently.** Extracted the audio from the source SWF (SHA-256 re-matched), and re-transcribed nine passages with a **different engine and a larger model** than the student's. All nine confirm |
| Did I open the images rather than trust the index? | **Yes — and it is where `M1` came from.** Eight frames opened, four regions cropped and enlarged |
| Did I test the claims most likely to be right, or most likely to be load-bearing? | **Load-bearing.** The categorical negatives, the exact `diff`, the four verdict-bearing timestamps, the decision quantity, and the two Tier 2 page citations |
| Did I inflate a `MINOR` to hold a gate, or soften anything to open one? | **Neither.** Both minors are argued down to `MINOR` on `REVIEW_PROTOCOL.md` §8's own wording, with the reason stated in each case, and both corrections run **in the submission's favour** |
| Did I add evidence, or only check it? | **Added.** `[00:08:22]`'s *"use it at 14, knock yourself out"*; the V03/V04 TDI-vocabulary counts that produced `M2`; the 287-reference measurement of `A-039`'s dependency surface; the exact-tie mechanism behind `N1`; the curve-ordering strand in `N5`; and the four negative dashboard checks that bounded `M1` |
| Did I answer every question the submission put to me? | **Yes — all three.** Items 124, 130 and 135 are adjudicated in § REVIEWER RULINGS and may be closed |
| Anything I could not verify? | **One thing, stated in place.** The *"all 672 sweep frames"* scan is not recoverable from the repository (`N2`); everything it is offered in support of was verified by other means |
