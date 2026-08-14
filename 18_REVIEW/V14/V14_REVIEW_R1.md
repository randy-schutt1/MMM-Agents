# V14 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V14** · `Bootcamp1 Wk5 041512 Part2 (48mins).swf` · session 2012-04-15, **Part 2 of a two-part recording** whose Part 1 is V13 |
| Review version | **R1** |
| Review date | 2026-08-14 |
| Previous review | none |
| Reviewer branch | `review/v14`, cut from the integration branch @ `5218cce` (**post-`D-044`**), own worktree at `MMM-Agents-v14-review` (`D-038`) |
| Submission reviewed | `video/v14` @ `ba2e474` (6 commits, `aa18849`…`ba2e474`), branched from `e46d8f2` |
| Independence | **`D-003` satisfied.** This session authored no V14 artifact. It located the source `.swf` from `SOURCE_MANIFEST.md` and **re-computed its SHA-256**; extracted the audio itself and **ran two further ASR passes on a different runtime (`openai-whisper`, PyTorch) at `medium.en` and `large-v3-turbo`** — a larger model than the student's; **re-derived `PT-042` end to end** in code sharing no line with `run_pt042.py` or `mmm_lib`, parsing the raw HistData CSVs directly; re-ran the `Q-015` `diff`s and re-measured the quarantined image in its own code; opened the load-bearing frames as images and **measured every frame's burned-in timecode in code**; and re-derived both worked-example percentiles by hand |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 5 MINOR, 9 NOTE.**

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the gate
for V15.** `COURSE_PROGRESS.md` currently reads *"V15 GATE: CLOSED until V14's R1 returns"* — that
was the correct state to hold, and on the merits **this review opens it.**

> ⚠️ **THE GATE BEING OPEN IS NOT A RECOMMENDATION TO WALK THROUGH IT.** V14 is the owner's declared
> **hard stop**. `D-024` is a finding-severity rule; it has nothing to say about the owner's
> decision to pause for a comprehension/gap audit, and this review does not pre-empt that decision.
> **The gate is open and the owner's stop stands.** §*THE GAP AUDIT* below is this reviewer's own
> read, offered as input to it.

The five minors are carried in `REVIEW_INDEX.md` as items **172–176** and are owed before V14 can
reach `COMPLETE`.

**Confidence: HIGH.**

Confidence is high because every load-bearing claim was re-derived from source rather than read:

- **`PT-042` was independently re-implemented and reproduces.** Reviewer-written code — its own CSV
  parser, its own DST arm shift, its own session-day, board-range, extension, stopwatch, lock and
  resolution logic, written from `PT-042` §3's text before `run_pt042.py` was opened — returns
  **`O1` 0.3468 / 0.3030** against the committed **0.3461 / 0.3041**, **`O2` 0.4617 / 0.4483**
  against **0.4607 / 0.4433**, and **median MFE 40.20 / 42.35** against **40.10 / 40.40**. Every
  headline figure lands within **0.005**. `no-extension = 0` and `no-lock = 0` reproduce **exactly**
  in both arms, independently confirming the `N4` degeneracy.
- **The lesson's single most load-bearing sentence was re-transcribed by two further engines.**
  Source SHA-256 re-verified `e3dd2b80…7a1d01`; audio measured **2869.0025 s** against the
  submission's **2869.002449 s**. The compound TDI question and its split answer confirm **verbatim,
  including the words *"the green RSI line"***.
- **The two worked-example percentiles were recomputed by hand** — `45.5%` and `20.0%` — and both
  are right.
- **The `Q-015` measurements reproduce exactly**: `diff` 8 lines / 4 pairs / zero content lines;
  mean luminance **0.9964**, fraction above 60 **0.00321**, light rows **11–20 and 752**.
- **Frames were opened and measured** — and that is where `M3` came from.
- **`PT-042` re-run against the `D-044`-extended 13-file corpus reproduces both committed output
  files BYTE-IDENTICALLY.** `git status` clean afterwards.

---

## SOURCE MATERIAL REVIEWED — **FIRST, BEFORE ANY STUDENT CONCLUSION**

| Source | References | Purpose |
|---|---|---|
| `02_TRANSCRIPTS/V14/V14_TRANSCRIPT.md` verbatim body | **All 600 markers, `[00:00:00]`–`[00:47:46]`** | Primary evidence. Read **before** the source notes, interpretation, homework, backtest or mastery report were opened |
| **The source `.swf` itself** | SHA-256 re-verified; audio extracted to 16 kHz mono | **Independent ASR.** Five passages (~4½ min) re-transcribed on `openai-whisper medium.en`, and the critical 20 s adjudicated additionally on **`large-v3-turbo`** |
| All **29** committed frames | Opened; **all 29 burned-in timecodes cropped and read in code**; four opened at full resolution | Verify §2's slide transcription, §3's `D-043` ordering, and the frames' own timestamp claim. **This is where `M3` came from** |
| `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/13_…` and `14_…` | `diff`ed in full; the surviving `.jpg` measured in `numpy` and autocontrast-enlarged | Independent re-derivation of `Q-015` §1–§4 |
| `datasets/HISTDATA_GBPUSD_M1/raw/*.csv` | **Parsed directly**, 2013→2016H1 | Independent re-derivation of `PT-042` |
| `00_SYSTEM/SOURCE_MANIFEST.md`; the 21-folder library tree | Read in full | Independent check of the Week-6 claim. **This is where `M5` came from** |
| `15_Bootcamp1_Wk7_050612_Part1_52mins/TRANSCRIPT.md` | Opening 40 lines | Verify the `D3` datum **and** its provenance |
| `DECISIONS.md` `D-003`, `D-004`, `D-024`, `D-026`–`D-031`, `D-035`, `D-036a`, `D-038`/`D-038a`, `D-039`–`D-044`; `REVIEW_PROTOCOL.md`; `REMEDIATION_PROTOCOL.md`; `SOURCING_HIERARCHY.md` | Read | Governing policy |
| `02_TRANSCRIPTS/V12/V12_TRANSCRIPT.md` `[00:15:36]`–`[00:16:23]` | Read at source | Independent verification of `C-021` |

**Source access was not limited.** The `.swf`, its audio, the transcript, all 29 curated frames, the
quarantined tree, the full M1 corpus and the extended `D-044` corpus were all available. Nothing in
this review is capped by missing evidence, with the one standing exception the submission itself
records: **the 582 sweep frames are not committed**, so `§4`'s scan is not repository-reproducible —
the same limit V12 R1 recorded at item 140 and V13 R1 at item 160.

## STUDENT ARTIFACTS REVIEWED

| Artifact | Reviewed |
|---|---|
| `V14_TRANSCRIPT.md` header, speaker table, 6 strands, verification, 7 corrections | ✅ in full |
| `V14_SOURCE_NOTES.md` · `V14_INTERPRETATION.md` Q1–Q9 | ✅ in full |
| `04_SCREENSHOTS/V14/INDEX.md` §1–§4 **+ all 29 frames** | ✅ |
| `05_HOMEWORK/V14/V14_HOMEWORK.md` | ✅ in full |
| `PT-042_…md` · `BT_V14_0001.md` · `data/pt042_output.txt` · `data/pt042_result.json` · `scripts/run_pt042.py` | ✅ in full |
| `07_MASTERY_REPORTS/V14_MASTERY_REPORT.md` | ✅ |
| `QUARANTINE_REGISTER.md` `Q-015` · `A-089`–`A-094` · `C-021` · the V14 pass over 13 existing records | ✅ |
| `LOG.md`, `COURSE_PROGRESS.md`, `REVIEW_INDEX.md` items 162–171 | ✅ |

---

## CRITICAL FINDINGS

**NONE.**

The six places a `CRITICAL` could plausibly have arisen were checked directly and all six are clean:

1. **A holdout breach (`E23`).** `PT-042` runs `W-B` = 2014-01-05 → 2015-12-31, wholly inside
   `D-035` DEVELOPMENT; `assert_development()` is enforced at load; and the session **explicitly
   declined** the extended corpus because no owner decision had landed at its branch point. My own
   re-derivation clipped at 2016-06-30 independently and reproduces. **The 2016H2 holdout was never
   opened, and neither was `D-044`'s 2017-2025.**
2. **Post-hoc threshold movement (`E21`).** `git diff ae3b07a video/v14 -- PT-042_*.md` is **the RUN
   banner plus one line of the STATUS block, and nothing else.** No threshold, window, filter, arm,
   outcome measure or decision rule moved.
3. **Pre-registration ordering.** `git cat-file -e ae3b07a:06_MANUAL_BACKTEST/scripts/run_pt042.py`
   → **ABSENT**, at 10:22:43; the runner appears at `14ec97c`, 10:28:45. **Ordering PROVEN, not
   asserted.**
4. **Selective reporting (`E25`/`E09`).** Both `D-031` arms are reported, Arm A is the friendlier
   one and both are printed; every control statistic is computed and printed beside the rule arm's;
   the counter-intuitive `S1` sensitivity (which runs *against* the drill) is reported; and the two
   control defects are self-disclosed **before** a reviewer found them.
5. **`A-082` — a drill parameter adopted as doctrine.** `12_MASTER_SPEC/` and `13_MACHINE_SPEC/`
   contain **only `.gitkeep` and a README**; the 5-pip stop and 30–50-pip target appear in neither.
   Fence held.
6. **Quarantine leakage.** No V14 artifact cites `NOTES.md`, `RULES.md` or `VISUAL_INDEX.md`. The
   EMA claim rests on a frame this session opened itself, not on the quarantined EMA table — which
   matters, because that table is **wrong under `D-043`**.

## MAJOR FINDINGS

**NONE.**

Every substantive conclusion in the submission survived an attempt to break it. The two I attacked
hardest — the `A-084` compound-question defeater and the `A-056` non-closure — **both hold**, and
they hold for the reasons the session gives.

---

## ⭐ `A-084` — I ATTACKED THE DEFEATER FOUR WAYS AND IT HOLDS · answers item 163

Item 163 invited attack on the highest-value argument in the submission. It was attacked. **It
survives, and it is stronger than the submission claims.**

### The passage, from my own ASR — three engines, and the student is right

`openai-whisper large-v3-turbo` and `medium.en` (temp 0.2), on a 20 s cut from audio extracted from
the SHA-verified `.swf`:

```text
[00:44:42]  Steve, I know that you're not looking at comments, but I am right now.
[00:44:45]  The TDI — does the green RSI line represent the 15-minute chart candles?
[00:44:49]  Does the red trade signal line represent the one hour?
[00:44:52]  Yes.
[00:44:53]  Does the yellow market baseline represent the four-hour candles?
[00:44:55]  No.
[00:44:56]  The TDI line, RSI is green.
[00:44:59]  The red line, blood in the water, is the one hour.
[00:45:09]  The bands are two standard deviations away from the market base.
```

**Correction 5 in `V14_TRANSCRIPT.md` is confirmed verbatim by two further engines on a different
runtime, including the words *"the green RSI line"* and the compound structure.** My first pass at
`medium.en` on a wider window dropped *"green RSI"* to *"the TDI line"*; the larger model and a
second temperature both restore it, and the supplied transcript independently has *"green
r-siline"*. **Three sources, one reading.** The session's characterisation of this as the corpus's
best spoken opportunity is fair, and its transcription of it is right.

### The four attacks

| # | Attack | Result |
|---|---|---|
| 1 | **The *"Yes"* attaches only to the last clause asked** — ordinary conversational behaviour. If so it answers *red*, and green is untouched | **Fails to close.** This makes `A-084` *worse*, not better: the one half that would bear on `k` is then unanswered |
| 2 | **Take the *"Yes"* as answering the first half, red being an aside** | **Arbitrary.** It is exactly symmetric to the student's point, and `D-030` forbids selecting the reading that unblocks the most work. There is no textual warrant for either split |
| 3 | ⭐ **The strongest one: `[00:44:56]` *"The TDI line, RSI is green"* is the speaker's OWN unprompted restatement, not a student's premise being affirmed.** An unprompted identity statement is what `A-084`(a) asks for | **Defeated at source, and by the project's own tooling.** `MMM_TDI.txt`'s buffer is literally named **`RSI Price Line`** and — per item 157's `!SM_TDI` block — is `SMA(2)` of `RSI(21)`. **Naming a smoothed buffer after its input is the shipped convention**, so the sentence is lineage, not identity. The student's defeater 1 is correct |
| 4 | **Even granting the literal reading, does it fix `k`?** | **No.** *"The 15-minute"* on a 15-minute chart is satisfied by `k = 1` **and** by `k = 2` (a 2-period average spans 30 min, which the same speaker calls *"the one hour"* for a 7-period one). `PT-040` already measured `k = 1` vs `k = 2` at **5.16 pp at `t = 50`**, past its own materiality boundary. **The passage cannot separate them** |

### One reason the submission does not give, and should

**The student's question already presupposes the standard TDI buffer naming** — *"green RSI line"*,
*"red trade signal line"*, *"yellow market baseline"* are the indicator's own published buffer
names. A speaker affirming a question phrased in an indicator's own vocabulary has affirmed the
vocabulary, not a construction. **An affirmation of a naming convention carries no information about
smoothing length**, independently of the compound-question argument. This is a fifth, structurally
different defeater and it is worth adding to `A-093`.

```text
RULING ON ITEM 163: the defeater HOLDS. A-084 REMAINS AN ACTIVE BLOCKER.
V11's RSI threshold claims STAY BLOCKED. The invitation to attack was
answered, at source, four ways, and none of them reaches closure.
```

---

## ⭐ `A-056` — CLOSURE IS RIGHTLY DECLINED, AND THE RECORD SHOULD SAY MORE THAN IT DOES · answers item 162

**Verified first:** `A-056` is **not** marked `CLOSED` anywhere. The V14 pass records it as
`MATERIALLY ADVANCED` and puts closure to the reviewer. ✅ The session did what it said it did.

**The Required Research is genuinely answered.** `A-056` asked *"whether any later lesson — or
'Jim' — states **how** the day's extreme is identified before it is known."* V14 does, in print,
taught by the course author rather than deferred. I confirmed the printed six steps by opening
`V14_00-26-50_…png` at full resolution and reading them character by character against
`INDEX.md` §2 — **the transcription is verbatim-accurate, including punctuation.** I confirmed the
spoken superset by my own ASR (`[00:27:03]`–`[00:28:26]`), which returns all six steps in order.

**Closure is nevertheless wrong, and for a second reason the session does not give.**

1. The session's reason — step 2 has no tolerance, and the speaker's own examples sit at the
   **45.5th** and **20.0th** percentile. **I recomputed both by hand and both are right:**
   `(6142 − 6127) / 33 = 0.4545` and `(3162 − 3155) / 35 = 0.2000`. `A-089` is correctly opened.
2. ⭐ **The second reason: `PT-042` measured the method's own premise and it FAILED.** Closing
   `A-056` as *"RESOLVED BY COURSE"* would put on the record that the corpus supplies a working
   method for identifying the day's extreme — while the project's own pre-registered measurement
   says the premise holds on **30–35%** of days against a required 80%. **A record cannot be closed
   as resolved by a method the same submission measured and refuted.**

```text
RULING ON ITEM 162: A-056 is NOT CLOSED. Recommended disposition, mirroring
phrasing the register already uses elsewhere:

  A-056 -- NARROWED. RESOLVED BY COURSE as to the EXISTENCE of a stated
  real-time method (V14, printed, six steps, course author -- the Required
  Research is ANSWERED and should be marked so). OPEN as to COMPUTABILITY
  (step 2, A-089) and OPEN as to the PREMISE (PT-042 NOT SUPPORTED).

This is a larger status change than "stays open" and a smaller one than
"CLOSED", and it is the one the evidence supports. Owed as part of M4.
```

---

## ⭐ `PT-042` — INDEPENDENTLY RE-DERIVED, AND THE VERDICT IS THE PRE-REGISTERED ONE

### Method — genuinely independent

Reviewer code, written from `PT-042` §3's definition table **before `run_pt042.py` was opened**:
its own `pandas` CSV parse of `raw/DAT_MT_GBPUSD_M1_{2013,2014,2015,2016H1}.csv`, its own
`zoneinfo`-derived DST interval table and `+1h` Arm-B shift, its own session-day index, board
range, extension detection, running extreme, stopwatch reset, lock, entry, stop, target, bar-order
resolution and MFE.

### Every headline figure reproduces

| Measure | Committed A / B | **Reviewer A / B** | |
|---|---|---|---|
| `O1` P(`L` still the day's extreme) | 0.3461 / 0.3041 | **0.3468 / 0.3030** | ✅ |
| `O2` P(30 before the 5-pip stop) | 0.4607 / 0.4433 | **0.4617 / 0.4483** | ✅ |
| `O3` P(50 before the stop) | 0.2972 / 0.2719 | **0.2979 / 0.2783** | ✅ |
| `O4` median MFE (pips) | 40.10 / 40.40 | **40.20 / 42.35** | ✅ |
| `n` | 471 / 467 | **470 / 406** | ✅ / see note |
| `no-extension` | **0 / 0** | **0 / 0** | ✅ exact |
| `no-lock` | **0 / 0** | **0 / 0** | ✅ exact |

**The Arm-B `n` gap is my implementation, not the submission's.** My `C-14` pre-window gate demands
the specific hours `17…00`, which every DST-shifted Monday fails because the week opens at Arm-B
`18:00`; `run_pt042.py` gates on the *count* of distinct hour buckets, which is the better reading
of `C-14` as written. **The rates are unaffected** — Arm B's `O1` lands at 0.3030 against 0.3041 on
a 13% smaller sample.

**`O1` misses `≥ 0.80` by ~45 points in both arms and `O2` misses `≥ 0.50` in both. `NOT SUPPORTED`
is what §6 prescribes and it is what is recorded.** Confirmed independently.

### The population finding is real and is the most useful thing here

`no-extension = 0` and `no-lock = 0` across 938 arm-days reproduce **exactly** in my code. The
session's reading — *the lock selects a time, not a day; all the filtering is done by `F1`* — is
correct, was not knowable before the run, and is properly reported as a null rather than dropped.
**`N4`'s degeneracy is confirmed at `n = 0`.**

### Pre-registration ordering — PROVEN

`run_pt042.py` **ABSENT** at `ae3b07a` (10:22:43); present at `14ec97c` (10:28:45). The
pre-registration diff between them is the RUN banner and one STATUS line. ✅

### ⭐ The `D-044` cross-check the submission could not run

`video/v14` branched from `e46d8f2`, before `D-044` landed. In this merged worktree — **13 raw
files, 4.59 M bars, `mmm_lib` with the new `SCOPES`/default-DEVELOPMENT machinery** —
`python3 run_pt042.py` rewrites `pt042_output.txt` and `pt042_result.json` **byte-identically**;
`git status` is clean afterwards. **`D-044` does not move V14's result, and this is measured rather
than inferred from `D-044` §6** (which could not have covered a runner that did not yet exist).

### ⚠️ The `N1` control disclosure is accurate — and I can put a number on it · `N2`

The self-disclosure at `BT_V14_0001.md` §3a is **correct in direction and honest in kind**: it
names the defect, states that it runs against the session's own interest, and says the true gap
would be *"smaller still, possibly zero or negative."* That is a genuinely self-critical disclosure
and it is credited.

**It is not understated in kind. It is understated in magnitude, and the magnitude is decisive.**
I re-ran `N1` with the synthetic level's distance drawn from the rule arm's **own** `|entry − L|`
distribution (median 16.6 / 14.5 pips) instead of the hard-coded 10:

| | Rule arm `O1` | `N1` `O1` **as coded** | `N1` `O1` **distance-matched** |
|---|---|---|---|
| Arm A | 0.3461 | 0.3163 | **0.4544** |
| Arm B | 0.3041 | 0.2934 | **0.3961** |

**Under a distance-matched control the rule arm's `O1` is WORSE than matched-random in both arms.**
The committed *"`O1` percentile vs `N1`: 90.2"* does not merely shrink — **it inverts.** *"Possibly
zero or negative"* is measurably *negative*.

**And a second mismatch runs the other way and is not named:** the control draws its entry
uniformly over `[T0, 17:00−60)`, while rule-arm locks fire at a median of 178 / 200 minutes. A
later entry leaves less time for the level to be breached, which pushes the control's `O1` **up**.
So the *net* direction of `N1`'s incomparability was not established by the disclosure, only its
larger component. **The distance effect (+0.14) dominates any plausible timing effect, so the
disclosed direction is right — but the record should say that two biases were present, not one.**

**None of this touches the verdict**, exactly as the submission says: `O1` is adjudicated against
the pre-registered `0.80` and 0.30–0.35 misses it by 45 points regardless. The remedy is what the
session already proposes — **amend `PT-042` §5a before any re-issue** — plus the two numbers above.

---

## ⭐ `Q-015` — VERIFIED BY EXACT DIFF AND EXACT MEASUREMENT

Every measurement in `Q-015` was independently re-derived and **every one is exact.**

| Claim | Reviewer's own re-derivation |
|---|---|
| `VISUAL_INDEX.md` vs V13's: **8 lines = 4 pairs, ZERO content lines** | ✅ **exact** — the `.swf` name and three `VIDEO_14→VIDEO_15` filenames, nothing else |
| `NOTES.md`: **6 differing lines**, one invented `Topic Focus` | ✅ **exact** — *"GBPJPY / NAS100 Spread & Buffer Adjustments, Trailing Stops"* |
| `RULES.md`: **12 differing lines** | ✅ **exact** (see `N7` for one miscount inside the prose) |
| `002` and `003` absent from disk | ✅ the `SCREENSHOTS/` folder holds exactly one file |
| Image is `1024 × 768` | ✅ |
| **mean luminance ≈ 1.0 / 255** | ✅ **0.9964** |
| **fraction of pixels > 60 = 0.0032** | ✅ **0.00321** |
| **light pixels confined to rows 11–20 and 752** | ✅ **exact**, `numpy` row scan |
| Text reads *"End of slide show, click to exit."* | ✅ confirmed at 8× autocontrast enlargement — six words, PowerPoint's exit screen |
| Indexed as *"Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs"* | ✅ verbatim in the file |
| `V15-R001` *"Wait for the M15 candle to close before taking the 5/13 EMA cross"*, tagged **"Preserved verbatim rule from instructor"** | ✅ verbatim in the file |
| The lesson says *"there's no 15 minute, that's all bullshit, throw it out"* | ✅ `[00:31:52]` in the committed body, and I re-read the surrounding block |

**The inversion is real and it is the sharpest artifact this register has produced.** A fabricated
rule instructing a student to trade a **5/13 EMA cross on a closed M15 candle** is attached to the
one lesson in the corpus whose entire assignment is *"do not look at candles, do not look at TDI,
do not look at nothing but this board"* `[00:26:55]`, *"there's no 15 minute… that's all bullshit,
throw it out"* `[00:31:52]`, and *"No charts, Dave. No charts."* `[00:46:27]`. **And the one image
it indexes as a five-EMA chart is 99.7% pure black.**

`Q-015` is the strongest entry in the register and it is measured, not asserted. **No finding is
charged against it.**

---

## ⭐ `C-021` — CONFIRMED AT SOURCE IN V12, AND CORRECTLY LEFT UNADJUDICATED

I read V12's passage at source rather than accepting the submission's summary of it:

```text
V12 [00:15:47]  There's some formula deviation 2% I don't know two standard deviations away from
V12 [00:15:54]  The market baseline or something like that. I don't really know because I didn't invent it
V12 [00:16:03]  They're essentially Bollinger bands
V12 [00:16:07]  Based on the RSI line itself. That's what someone said telling me not sure
V12 [00:16:12]  But anyway, it's two standard deviations away
V12 [00:16:16]  from price action
V12 [00:16:20]  From the RSI line. Thank you. Okay now
```

**Every element of `C-021` §1 is confirmed**, including the detail most likely to have been
smoothed over: `[00:16:16]` *"from price action"* is a **third** basis stated between the other two,
and `C-021` includes it inside its elided quotation rather than dropping it. The *"Thank you"*
marking an accepted correction is there. **V12's terminal position is `the RSI line`, reached under
prompting.**

V14 `[00:45:09]` — *"The bands are two standard deviations away from the market base"* — confirmed
by my own ASR, unhedged and unprompted. **The reversion is genuine and the one-week separation is
correct** (`Wk4 040812` → `Wk5 041512`; the `S1` self-correction from *"five weeks"* to *"one week"*
is right, and it does tighten the contradiction).

**Leaving `C-021` unadjudicated is correct.** `SOURCING_HIERARCHY.md` §3.2's *"the recording wins"*
resolves Tier 1 against Tier 2, not Tier 1 against itself across lessons, and no decision in
`DECISIONS.md` supplies that rule. The session states three readings, adopts none, and notes that
the third reading also invalidates `A-086`'s current wording — which is the observation a careless
round would have missed. **`D-041`/`D-043` is the right precedent to cite.** Forwarded to the owner
as item 168, unchanged.

---

## ⭐ ITEM 157 — THE NEGATIVE IS CONFIRMED

| Check | Reviewer's own run |
|---|---|
| Marker count | **600** ✅ |
| `shark`, case-insensitive, whole file | **0** ✅ |
| `63` as a token, and `sixty-three` / `six three` | **0** ✅ |
| `37` as a spoken token | **0** — every hit is a `[00:xx:37]` marker line ✅ |
| `fin` as a word | **0** ✅ |

**V14 contributes nothing to the `!SM_TDI` / `63`-`37` provenance question.** The submission's
*"no help at all"* is exactly right, and it is worth noting that the session reported this as a
prominent negative in three places rather than letting it go unmentioned — which is what
`REVIEW_INDEX.md` item 107 asks for.

---

## ⭐ THE WEEK-6 GAP AND DEVIATION `D3` — RULING · answers item 165

### Both citations confirmed at source

| Claim | Reviewer's own check |
|---|---|
| V14 `[00:01:08]` *"that will be your boot camp for the week — to watch the recording that we did over there"* | ✅ **confirmed twice**: verbatim in the committed body, and in my own ASR at `[00:01:06]`–`[00:01:10]`, which also independently confirms correction 1's *"Tannen will take this recording, go home, render it"* |
| `Wk7 050612 Part1` opens *"Alright, week seven"* at `[00:00:02]` and *"Week seven."* at `[00:00:23]` | ✅ **confirmed verbatim**, lines 14 and 41 of that file, 21 seconds apart, in the opening breath |

### The ruling: legitimate in kind, unnecessary in fact, and unverified in substance

**On form, `D3` is not a boundary violation.** A string check for a *bibliographic* fact — what
number the speaker gives the next surviving file — creates no interpretation of V15, no V15
artifact, and no record about V15's content. `D-004` governs the **gate** (may V15 work begin) and
`D-017` governs **ingestion**; neither is engaged by reading a week number, any more than reading
`SOURCE_MANIFEST.md`'s filenames is. It was disclosed at the point of use, in the artifact a reader
hits first. **No gate breach, and the session was right to declare it rather than do it quietly.**

**But two things are wrong with it, and the second is the real one.**

**(1) It was not needed.** `SOURCE_MANIFEST.md` — which this session read to verify the SHA — and
the 21-folder library tree both show the corpus jumping **`Wk5 041512` → `Wk7 050612` with no
`Wk6` file at all.** Combined with V13 `[00:05:20]`'s *"Sunday the 29th"* and `[00:05:33]`'s *"week
six through ten"*, the conclusion **a Week 6 session is missing from this corpus** follows entirely
from material already ingested. The forward `grep` adds *"and the speaker himself numbers it
seven"* — which the file's own name already asserts. **A deviation taken to reach a conclusion that
was already reachable is a deviation that did not need to be taken**, and the cheaper route should
have been tried first and reported.

**(2) The datum it imported is unverified, and that asymmetry is the actual defect.** The file read
is a **pre-ingestion supplied transcript of exactly the class `Q-008`…`Q-015` have shown to be
fabricated in its headers** — and this very file's header reads *"Course Position: Video 16 of 21"*
and a *"Primary Topics"* line, the two fields `Q-015` §5 quarantines by name. The session applied
`I-008` rigorously to V14's body — 600 markers, monotonicity, a three-way duration agreement, an
independent ASR pass, seven corrections — and applied **none of it** to the V15 body it then made
load-bearing for `A-092`. **The direction of the read is not the problem; the unverified evidence
is.**

**In this instance the risk did not bite** — the string is corroborated by the filename, by V13, and
by the manifest's missing `Wk6`. **The conclusion stands.**

```text
RULING ON ITEM 165 -- and the precedent this reviewer recommends the owner adopt:

  A forward read into a not-yet-ingested lesson is PERMITTED when all four hold:
    (a) it seeks a BIBLIOGRAPHIC fact (numbering, date, filename, speaker
        identity), never doctrine, a rule, or a value;
    (b) it is disclosed AT THE POINT OF USE, not only in a deviations table;
    (c) no artifact, record or interpretation about the future lesson is created;
    (d) THE IMPORTED DATUM CARRIES THE SAME I-008 VERIFICATION AS ANY OTHER
        EVIDENCE, or is labelled UNVERIFIED wherever it is used.

  V14's D3 satisfies (a), (b) and (c) and FAILS (d). Because the conclusion is
  independently supported by SOURCE_MANIFEST.md, this is recorded as a NOTE and
  no finding is charged. The (d) clause is the part worth making standing policy.

  One live consequence, disclosed by the session itself: COURSE_PROGRESS.md
  V15 GATE (c) now carries V15's course-length statement, seen only through
  this grep. The mitigation written there -- "V15 should treat it as its own
  primary evidence" -- is the right one and should be kept.
```

---

## ⭐ `D-043` CORROBORATION — RE-OPENED THE FRAME, AS INVITED

Item 169 offered a ten-second falsification test: *re-open the frame and check whether yellow or red
is faster.* **Done.** `V14_00-13-05_emas-yellow-red-cyan-white-low-test-candle.png`, opened at full
resolution:

```text
YELLOW  weaves through the candle bodies, turning inside single candles   -- fastest
RED     tracks yellow and lags it at every turn                           -- second
CYAN    smooth, crosses price rarely, wide swings only                    -- third
WHITE   near-straight across the whole visible window                     -- slowest
```

**`yellow < red < cyan < white` is confirmed, unambiguously.** Under `D-043` that is
`5 < 13 < 50 < 200`, and it is inconsistent with `D-042` §2's superseded `5 = red` / `13 = yellow`.
The submission's framing is exactly right: **ordinal only, `A-020` does not close, no claim about
Blueberry/800 because no fifth line is in the window.** This is a genuine, cheaply-falsifiable
Tier-1 datum on a mapping `D-042` §1 recorded as thinly supported, and it is offered to the owner
at the right strength.

---

## THE SELF-DISCLOSED DEVIATIONS — CHECKED

| | Checked | Verdict |
|---|---|---|
| `D1` §9 ordering broken | `V14_SOURCE_NOTES.md` §0 read; the `[AUDIO]`/`[PRINTED]` tags spot-checked by `grep` | ✅ **Properly mitigated.** The load-bearing conclusions are `[AUDIO]` or `[AUDIO+PRINTED]` and the tags are falsifiable, as claimed. Same handling V13 R1 accepted at item 147 |
| `D2` homework substituted | `V14_HOMEWORK.md` §0 read | ✅ **Right call.** Both halves are live-market two-week exercises and the TDI half is additionally blocked by `A-084`. Refusing to fabricate a notebook is the correct behaviour |
| `D3` forward `grep` | Ruled on above | ⚠️ **Legitimate in kind, unnecessary in fact, unverified in substance.** No finding charged |
| `D4` `N1` `O1` underspecified | Re-measured; magnitude quantified above | ✅ **Accurate and self-critical.** Understated in magnitude, not in kind — `N2` |
| `D5` `N4` degenerate | Reproduced exactly at `n = 0` in independent code | ✅ **Correctly reported as a null** |
| `S1` *"five weeks"* → **one week** | `Wk4 040812` → `Wk5 041512` | ✅ Correct, and it does strengthen `C-021` |
| `S2` frame-scan `48/2/4` → **50/2/2** | Not independently reproducible — the 582 sweep frames are not committed | ⬜ **Accepted on the same terms as items 140 and 160.** The standing limit, not a V14 regression |
| `S3` `trap ×7 / stop hunt ×4` → **`trap ×4 / stop hunt ×3`** | Re-counted in the committed 600-marker body | ✅ **Confirmed at the corrected figures**, including the `stop-hon` ASR variant |

**Five deviations declared before a reviewer found any of them, three self-corrections left visible,
and the one that runs against the session's own interest (`D4`) named as such.** This is the
behaviour `REMEDIATION_PROTOCOL.md` §2 exists to produce and it is credited at `N9`.

---

## MINOR FINDINGS

### `M1` — `A-089` QUOTES THE SPEAKER'S VERDICT AS A DECLARATIVE; TWO INDEPENDENT ENGINES SAY IT IS A QUESTION HE ASKS AND ANSWERS

`A-089`'s evidence table — the record that blocks `A-056`'s closure and therefore the single
highest-stakes record in the submission — gives the speaker's verdict on the first worked example
as:

> *"**is in the middle of the range. Hell yeah, it is.** This is a possible candidate"*

**My own ASR, on two different models, returns an interrogative:**

```text
openai-whisper medium.en      [00:29:29]  Is he in the middle of the range?
                              [00:29:30]  Hell yeah he is.
openai-whisper large-v3-turbo [00:29:29]  Is he in the middle of the range?  Hell yeah, he is.
```

The supplied transcript splits the sentence across two markers — `[00:29:24]` *"…trading at one
o'clock at 61"* / `[00:29:28]` *"42 is in the middle of the range. Hell yeah, it is"* — and the
record copied that split reading without correcting it.

⚠️ **The substance is unaffected and the finding is not a retraction.** He does endorse `6142` as
*"the middle"*, the `45.5%` figure is right, and `A-089`'s conclusion stands entirely. **But the
record presents as an assertion what the audio has as a self-answered question**, inside quotation
marks, in the record that blocks the largest status change in the submission. This is the same
defect class charged at `V07_REVIEW_R1.md` `M3`, `V07_REVIEW_R2.md` `M1` and `V09_REVIEW_R2.md`
item 81 — and it is the one passage a reviewer would most want in the session's own twelve-passage
ASR sample, where it was not included.

**Owed:** correct the quotation in `A-089` (and anywhere it is repeated) to the interrogative form,
citing the two engines, per `REMEDIATION_PROTOCOL.md` §2.

### `M2` — THE ARTIFACTS SILENTLY MIX TWO CLOCKS: **20** DISTINCT `[HH:MM:SS]` CITATIONS DO NOT EXIST IN THE COMMITTED TRANSCRIPT'S OWN MARKER INDEX

A mechanical scan of every `` `[HH:MM:SS]` ``-plus-quotation pair in the V14 set returns **30 sites
across 9 files, at 20 distinct timestamps, none of which is one of the file's 600 markers.**

```text
V14_INTERPRETATION.md  00:07:40  00:07:43  00:32:25  00:34:35  00:37:12  00:44:59  00:46:20
V14_SOURCE_NOTES.md    00:07:40  00:27:28  00:32:25  00:37:12  00:46:20
AUTOMATION_AMBIGUITIES 00:08:04  00:08:11  00:32:25  00:44:49  00:45:09  00:45:21  00:46:20
BT_V14_0001.md         00:27:28        PT-042.md   00:27:28  00:37:12
V14_HOMEWORK.md        00:24:26        QUARANTINE_REGISTER.md  00:46:28
V14_TRANSCRIPT.md      00:24:26  00:40:49  00:44:43  00:45:16  00:46:20   <- its own correction table
```

**The cause is not carelessness and the finding must say so.** My own ASR clock puts *"does the red
trade signal line…"* at **44:49**, *"blood in the water"* at **44:59** and the bands sentence at
**45:09** — i.e. **the session's citations are audio-accurate**; they are the timestamps its own
`faster-whisper` pass produced. The committed transcript's marker grid is coarser and puts the same
words at `44:45`, `44:56` and `45:07`. **Two clocks, both defensible, cited interchangeably with no
statement of which is in use.**

**Why it is still a finding.** Every one of these is a pointer into `V14_TRANSCRIPT.md`, and a
reader who greps the committed file for `[00:44:49]` — the citation `A-085` gives for its
load-bearing sentence — **finds nothing.** The same sentence is cited at `[00:44:49]` in one record
and `[00:44:59]` in another, and its actual marker is `[00:44:56]`. `V14_TRANSCRIPT.md`'s own
seven-correction table — the file's verification record — misses on **three of seven** (`#1` cites
`[00:01:01]` for body text at `[00:01:03]`; `#6` `[00:45:16]` for `[00:45:18]`; `#7` `[00:46:20]`
for `[00:46:19]`).

⚠️ **One is wrong on both clocks:** `V14_INTERPRETATION.md` Q4 cites `[00:34:35]` for *"Promise me
you will do this — this and the TDI are priceless"*. The line is at **`[00:35:37]`**, a **62-second**
miss; my own ASR of `34:20`–`35:20` contains no such sentence.

**Owed:** state the convention once (marker grid, with ASR times distinguished where used), and fix
the `[00:34:35]` citation. Correcting all twenty is not required if the convention is declared.
See `N8` for why the project's own checker did not catch this.

### `M3` — EVERY FRAME'S FILENAME TIMESTAMP IS EXACTLY **16 SECONDS** EARLIER THAN ITS OWN BURNED-IN TIMECODE, AND `INDEX.md` MISQUOTES THAT TIMECODE

`04_SCREENSHOTS/V14/INDEX.md` opens by claiming each frame *"carries its own burned-in timecode and
**proves its own timestamp** — the property the quarantined `VISUAL_INDEX.md` files lack."* **I
cropped and read the player timecode on all 29 frames in code. It does not.**

```text
filename 00-00-20 -> burned 00:36   filename 00-13-05 -> burned 13:21
filename 00-01-15 -> burned 01:31   filename 00-26-50 -> burned 27:06
filename 00-02-40 -> burned 02:56   filename 00-39-10 -> burned 39:26
   ... 28 of 29 frames at exactly +16 s; the 29th (00-47-35 -> 47:49) clamped at EOF, +14
```

**`INDEX.md` §2 states the assignment slide's burned timecode as `26:50 / 47:4`. The image reads
`27:06 / 47:4`** — a direct misquotation of a frame the section says was read at full resolution.

**This is a V14 regression, not a standing capture defect.** I measured V12's and V13's committed
frames the same way: **offsets of 0–1 s.** Something in this lesson's sweep introduced a constant
16-second lag between the harness's index→time mapping and the player's own clock.

⚠️ **Nothing substantive moves.** The frames show what `INDEX.md` says they show; the assignment
slide is on screen across the whole `26:50`–`27:06` span; the `D-043` ordering is unaffected. **The
defect is in the claim, not the evidence** — but the claim is the specific one used to distinguish
this session's frames from the fabricated `VISUAL_INDEX.md` entries, so it should be true.

**Owed:** correct §2's quoted timecode; restate the opening claim as *"each frame carries a
burned-in timecode; in this lesson it runs `+16 s` against the filename and the filename is the
sweep index, not the player clock"*; and record the offset so V15's sweep is checked for it.

### `M4` — TWELVE RECORDS V14 MOVED CARRY NO UPDATE OR POINTER IN THEIR OWN BODY, AND TWO OF THEM NOW READ FALSE

Every V14 effect on an existing record is written into a single **`# THE V14 PASS OVER EXISTING
RECORDS`** table at the end of `AUTOMATION_AMBIGUITIES.md` (line 7564). **Not one of the twelve
records it moves carries an update block, a pointer, or a `see the V14 pass` line in its own body.**

```text
A-056  A-077  A-085  A-086  A-076  A-020  A-011  A-004  A-002  A-019  A-082
   -- none mentions V14 anywhere in the record itself
A-084  -- mentions V14 only in V13's forward-looking sentence, which V14 has now answered
```

**Two are now factually stale to a reader who lands on the record, which is how these records are
actually read:**

1. ⭐ **`A-056`.** Its `### Current Status` still reads *"`DO NOT CODE` — the target is computable,
   **the method is absent**"* and its `### Required Research` still asks the question V14 answered.
   **The submission's own headline finding is invisible from the record it is about.**
2. **`A-084`.** Its body still ends *"The next place (a) or (b) could appear is V14… **Stop scanning
   legends.**"* — a live prediction about a lesson that has now been checked and returned a
   narrow-not-close.

**This is a convention choice, not an invention** — `# THE V12 PASS` uses the same trailing form.
But **V13, the immediately preceding session, wrote its update into `A-084`'s own body** (*"UPDATED
2026-08-14 BY THE V13 SESSION"*), which is why `A-084` is legible today. The finding is charged on
the two stale statements, not on the choice of form.

**Owed:** a pointer in each moved record to the V14 pass block, and — at minimum — corrected
`Current Status` / `Required Research` text on `A-056` and a closing line on `A-084`, superseded
text retained per `REMEDIATION_PROTOCOL.md` §2. **The `A-056` rewording recommended above under the
item-162 ruling is the one to apply.**

### `M5` — `A-092`'s HEADLINE COUNT IS CORPUS-WIDE AND WRONG; THE LIBRARY HAS AT LEAST ONE FURTHER UNRECORDED GAP

`A-092` is titled *"**TWO** artifacts are missing **from this corpus**"* and `V14_MASTERY_REPORT.md`
§3.5 and `COURSE_PROGRESS.md` repeat the count. **Scoped to the Week-6 question the record is
right. As a corpus-wide count it is not.**

The 21-folder library and `SOURCE_MANIFEST.md` show a **second, larger calendar gap**:

```text
V19/V20  Bootcamp1 Wk9  052012   =  2012-05-20
V21      Bootcamp1 Wk10 061712   =  2012-06-17     <- FOUR weeks later, one week number apart
```

Between them lie **2012-05-27, 06-03 and 06-10** with no file and no week number. Either ~3 further
sessions are absent, or the numbering skipped four weeks — **and nothing in `DECISIONS.md`,
`SOURCE_MANIFEST.md` or `AUTOMATION_AMBIGUITIES.md` records either possibility.** I checked.

⚠️ **This matters more than its size** because the owner is about to use the gap audit to decide
whether to continue to V15+, and *"two artifacts are missing"* is precisely the kind of headline
that gets carried into that decision as a bound on what the corpus lacks. **It is not a bound.**

**Owed:** narrow `A-092`'s title and headline to the Week 5→7 region it actually evidences, and
open a companion record (or extend `A-092`) for the `Wk9 → Wk10` four-week gap, flagged as
**unexamined** — the cheap decider is one string check in `Wk10`'s own opening, which is exactly the
`D3` shape and should wait for the precedent ruling.

---

## NOTES

### `N1` — `PT-042` reproduces independently, and `D-044` does not move it
Reviewer-written code reproduces every headline figure within 0.005 on both arms, and `no-lock` /
`no-extension` exactly at zero. Separately, re-running the committed `run_pt042.py` in this
post-`D-044` worktree — 13 raw files, the new scope machinery — rewrites both committed data files
**byte-identically**. **No action; recorded so a later round does not have to re-establish it.**

### `N2` — the `N1` control's incomparability is larger than disclosed, and it inverts the `O1` comparison
Distance-matching the synthetic level to the rule arm's own `|entry − L|` distribution moves the
control's `O1` from **0.3163 → 0.4544** (A) and **0.2934 → 0.3961** (B), i.e. **above** the rule
arm's 0.3461 / 0.3041. The disclosed *"possibly zero or negative"* is measurably negative. A second,
unnamed mismatch (entry-time distribution) runs the other way but is far smaller. **The verdict is
untouched.** Fold both numbers into the `PT-042` §5a amendment item 167 already owes.

### `N3` — deviation `D3`: ruling above, and the `(d)` clause is the part worth making policy
See the `D3` section. Recorded as a NOTE because the conclusion is independently supported by
`SOURCE_MANIFEST.md`. **The recommended four-part precedent is put to the owner as item 179.**

### `N4` — *"six-step method"* and *"six of its seven steps are arithmetic"* are both used, and cannot both be right
The printed slide carries **six method bullets plus *"Good luck"***. `A-089` correctly says *"step 2
of 6"*. But `V14_MASTERY_REPORT.md` §1, `V14_INTERPRETATION.md` Q2 and Q9, and
`COURSE_PROGRESS.md` all say *"six of its seven steps are arithmetic"* — over a seven-row table that
silently swaps out printed step 6 (*"Record your results and post in the forum"*) for two
**speech-only** additions (*"range ≤ 50 pips"*, *"aim for 30 to 50"*) that `INDEX.md` §2 itself
identifies as **not printed**. The defensible statements are *"five of the printed six steps are
arithmetic"* or *"one of six is not"*. **The conclusion — one uncomputable step — is unaffected.**

### `N5` — `A-089`'s short example contains **two** dealer prices, and only one is used
`[00:33:15]` gives `3162` (→ 20.0%) and `[00:33:57]`, inside the same worked example, gives
*"the deal is trading at 31 60"* (→ **14.3%**). Both confirmed in my own ASR. **The record uses the
higher — i.e. the one *less* favourable to its own argument** — so there is no selection problem
and no finding. But naming both would strengthen `A-089`: the spread between the two examples is
25 pp on the record's figures and **31 pp** on the alternative, and *"the speaker gives two prices
for the same example"* is itself evidence that no tolerance is in play.

### `N6` — `BT_V14_0001.md` §5's *"half"* is nearer two-thirds
*"Half the trades that reach 30 go on to reach 50"* — `0.2972 / 0.4607 = 64.5%` (A) and
`0.2719 / 0.4433 = 61.3%` (B). Reproduced in my own run. The sentence understates the submission's
own result. Trivial, and recorded only because §5 is the paragraph most likely to be quoted.

### `N7` — one miscount inside `Q-015`, in an otherwise exact entry
`Q-015` §3 describes `RULES.md`'s 12 differing lines as including *"**three** `VIDEO_14`→`VIDEO_15`
visual references"*. The `diff` carries **two** (`SCREENSHOT_001` and `SCREENSHOT_002`); the six
changed pairs are the filename, two rule IDs, two visual references and the setup name. **The
`VISUAL_INDEX.md` count of three is correct** — the two were transposed. Everything else in `Q-015`
verified exact, to the fourth decimal.

### `N8` — the project's own quotation checker was never generalised past `V07|V09`, and it would have caught `M2`
`05_HOMEWORK/V07/scripts/verify_quotes.py` documents its own generalisation at V09 R2 item 81 —
*"it now takes a lesson identifier"* — but its argument parser still accepts only
`{V07|V09}` and refuses `V14`. It has therefore not run on V10, V11, V12, V13 or V14. **This is a
standing project gap, not a V14 regression, and no finding is charged against this session** — but
item 81's whole argument was that an un-run check is how the fifth instance survives, and `M1` and
`M2` are the fifth and sixth instances. **Raised project-wide as item 180.**

### `N9` — calibration, charged as nothing
Four things this session did that the record should say worked, because a review that lists only
defects gives the next session no signal (`N6` at item 161):
**(1)** `S1`–`S3` were caught by measuring rather than trusting the draft, and all three verify at
the corrected figures. **(2)** `D4` — the control defect that flatters its own result — was found
and published by the session before any reviewer saw it, with the direction stated; my measurement
*strengthened* it rather than contradicting it. **(3)** `C-021` states three readings and adopts
none, and notices that the third reading invalidates `A-086`'s own current wording — the observation
a careless round drops. **(4)** The `A-082` fence was set **before** the run, in `PT-042` §1a, and
it held: `12_MASTER_SPEC/` and `13_MACHINE_SPEC/` contain no V14 number. **On the two occasions
where taking the attractive reading would have unblocked the most work — `A-084` and `A-056` — the
session declined and put the call to a reviewer. Both times it was right.**

---

## ⭐ THE GAP AUDIT — THIS REVIEWER'S INDEPENDENT READ

The owner asked for a hard stop here and for an honest picture before deciding on V15+. **The
submission's summary is fair and I found no place where it flatters the project.** Four of its
claims I verified directly, and I would add four things it does not say.

### Verified

| Claim | Independent check |
|---|---|
| **Zero lines of `12_MASTER_SPEC/` / `13_MACHINE_SPEC/` content after 14 lessons** | ✅ **True.** Both hold only `.gitkeep` and a README. ⚠️ **But this is not drift — it is a precondition working.** Both READMEs read *"STATUS: EMPTY — DO NOT POPULATE YET"* and name the gate: every lesson holding a reviewer `PASS`, **plus** `18_REVIEW/FINAL_COURSE_REVIEW.md` authorising the phase. Neither has happened. The emptiness is **compliance**, and the owner should read it that way |
| **Most ambiguity records are still `DO NOT CODE`** | ✅ **True, and the real figure is worse than "80 of 94."** The register holds **94 distinct records** (`A-001`…`A-094`, 9 with re-used headings). **87 of 94** carry `DO NOT CODE` in their own `Current Status` block; a handful have been closed in later update blocks. Note the *"80 of 94"* figure **is not asserted anywhere in the V14 submission** — I could not find it there, and my own count is the one above |
| **V09 / V10 / V12's fixes are self-verified and carry weaker confirmation** | ✅ **True, correctly recorded, and it is the project's most under-weighted risk.** `COURSE_PROGRESS.md` marks all three *"COMPLETE — SELF-VERIFIED AT OWNER DIRECTION, NOT independently verified, `D-003` is NOT satisfied"* and points to `REVIEW_INDEX.md` notices. **Correction to the framing in the brief: V13 is not in this class** — V13 got a genuine independent R1 (`review/v13`), and its two minors are open, not self-closed. The class is **V09, V10, V12** |
| **`09_CHART_EXAMPLES/` empty across all 14 lessons** | ✅ **True** — `.gitkeep` and a README only, as item 159 recorded. Also empty: `14_PINE/`, `15_AUTOMATED_BACKTEST/`, `16_FORWARD_TEST/`, `17_EXECUTION_ROBOT/` — all Phase 2+, all correctly gated |

### What I would add before the owner decides

1. ⭐ **The corpus's calendar gaps are not two — they are at least two regions, and one is
   unexamined.** `M5`. A gap audit that goes to the owner saying *"two artifacts are missing"* when
   `Wk9 → Wk10` skips four weeks with no record is understating the hole in the source material by
   more than the Week-6 finding fills.
2. ⭐ **The single highest-value unblock in the project is now an OWNER decision, not a lesson
   session's find.** `A-084` has been narrowed and not closed for **two consecutive lessons**, on
   the corpus's best spoken opportunity, and `A-093` establishes the failure is **structural** — the
   speaker answers what the indicator *feels like*, never what it computes, and says so. **Item
   157's `!SM_TDI` question is the live route**: that template answers `A-084` at `k = 2` directly,
   and `PT-040` has already measured that arm. **Continuing to V15+ to hunt for a properties dialog
   is the low-probability path; ruling on `!SM_TDI`'s admissibility is the high-probability one, and
   it costs one owner decision rather than seven more lessons.** I would put that squarely in front
   of the owner as the audit's main finding.
3. **Two Tier-1-against-itself conflicts now await the owner** — `C-021` (item 168) and the `A-020`
   nickname family that `D-041`/`D-043` already consumed two rulings on. `SOURCING_HIERARCHY.md`
   has no rule for this class, and it has now arisen three times. **A general rule would cost one
   decision and retire a recurring stoppage**; deciding `C-021` alone will not.
4. **What the project has actually produced is stronger than the empty directories suggest, and the
   audit should say so.** Fourteen lessons have yielded 94 ambiguity records, 21 contradictions, 15
   quarantine entries documenting a systematic fabrication in the supplied notes, and **42
   pre-registered tests with committed runners, committed outputs and proven ordering** — of which
   the last three (`PT-040`, `PT-041`, `PT-042`) all returned honest negatives on the course's own
   claims. **The verified conclusion after 14 lessons is not "we have not started the spec"; it is
   "the corpus does not yet support one, and we can now say so with measurements."** That is a real
   result and it is the answer to the question the hard stop is asking.

**On whether to continue to V15+ — this reviewer's view, offered as input and not as a
recommendation the owner asked for:** the marginal lesson is still producing genuine Tier-1 evidence
(V14 supplied `A-077`'s missing `N`, answered `A-056`'s Required Research, corroborated `D-043` and
opened `C-021`), so the corpus is **not** exhausted. But the two things that would unblock the most
downstream work — `A-084` and the band period — are **owner decisions and template admissibility
questions, not lesson-content questions**, and V14 is the evidence that lessons will not supply
them. **Continuing has value; continuing *instead of* making those two decisions does not.**

---

## WHAT V14 CONTRIBUTES, IN THIS REVIEWER'S JUDGEMENT

1. ⭐⭐ **The corpus's first stated real-time method for the day's extreme, printed and complete**,
   answering a seven-lesson-old Required Research — and **the first pre-registered measurement of
   it**, which says the method's premise is wrong about two days in three while its distance
   estimate is about right. **Both halves are the contribution; neither alone would be.**
2. ⭐ **A structural account of why the spoken route to `A-084` is weak** (`A-093`), which converts
   two lessons of failure from bad luck into a reason to stop looking.
3. ⭐ **`Q-015` — the fabrication register's strongest artifact**: a 99.7%-black PowerPoint exit
   screen indexed as a five-EMA chart, attached to a rule that inverts the lesson it is filed under.
4. **A Tier-1 ordinal corroboration of `D-043`** from a 2012 instructor chart, offered at exactly
   the strength the evidence supports.
5. **`C-021`, left unadjudicated** — a Tier-1-against-itself conflict raised rather than resolved by
   a session that had every incentive to resolve it in the direction Tier 2 supports.

---

## REVIEW_INDEX ITEMS RAISED

Numbering continues from **171**, the highest item raised by the V14 student session.

| # | Severity | Item |
|---|---|---|
| **172** | 🔶 **MINOR** | `M1` — `A-089` quotes the middle-of-range verdict as a declarative; two engines return an interrogative |
| **173** | 🔶 **MINOR** | `M2` — two clocks mixed; 20 distinct citations absent from the 600-marker index; `[00:34:35]` wrong on both |
| **174** | 🔶 **MINOR** | `M3` — all 29 frames `+16 s` from their own burned timecode; `INDEX.md` §2 misquotes it; the "proves its own timestamp" claim fails |
| **175** | 🔶 **MINOR** | `M4` — twelve moved records carry no pointer; `A-056` and `A-084` now read false in their own bodies |
| **176** | 🔶 **MINOR** | `M5` — `A-092`'s corpus-wide count is wrong; the `Wk9 → Wk10` four-week gap is unrecorded |
| **177** | ⬜ NOTE | `N2` — the `N1` control's incomparability inverts the `O1` comparison; two numbers for the §5a amendment |
| **178** | 🔷 **RULING** | Item 162 answered — `A-056` **NOT CLOSED**; recommended `NARROWED` wording supplied |
| **179** | 🔷 **PUT TO THE OWNER** | Item 165 answered — `D3` legitimate in kind, unnecessary in fact, unverified in substance; a four-part forward-read precedent is proposed |
| **180** | ⬜ NOTE | `N8` — `verify_quotes.py` still accepts only `V07\|V09`; un-run on V10–V14; **project-wide** |
| **181** | ⬜ NOTE | `N4`/`N5`/`N6`/`N7` — four small internal inconsistencies, none touching a conclusion |
| **182** | ⬜ NOTE | `N1` — `PT-042` independently reproduced, and byte-identical under the `D-044` corpus |
| **183** | ⬜ NOTE | `N9` — calibration; four things that worked, charged as nothing |
| **184** | ⬜ NOTE | Item 163 answered — the `A-084` defeater survives four attacks; a fifth defeater is offered for `A-093` |
| **185** | 🔷 **FOR THE GAP AUDIT** | This reviewer's independent read, and the four additions above |

Items **162, 163, 165** are **DISPOSITIONED** by this review. Item **168** (`C-021`) is
**forwarded to the owner unchanged** — this reviewer agrees it is not a lesson session's or a
reviewer's call. Items **164, 166, 167, 169, 170, 171** are **CONFIRMED as recorded**; item 167's
owed `PT-042` §5a amendment is extended by `N2`.

---

## GATE

```text
V15 GATE:  OPEN under D-024 -- 0 CRITICAL, 0 MAJOR.

           AND THE OWNER'S HARD STOP STANDS. D-024 rules on finding severity
           and says nothing about the comprehension/gap audit the owner
           scheduled for this point. This review does not authorise V15 work;
           it removes the review-severity obstacle to it. The decision is the
           owner's.

V14:       NOT COMPLETE. D-003/D-004 reserve closure to a reviewer PASS.
           Items 172-176 (MINOR) are owed before V14 can reach COMPLETE and
           are NOT gating.
```

**Carry into V15, if the owner continues:**

**(a)** ⭐ **`A-084`'s spoken route is now empirically and structurally dry.** Do not treat a sixth
restatement as new evidence (`A-093`, and the fifth defeater added above). 2,047 frames across
V12–V14 hold no properties dialog. **The live route is item 157's owner ruling, not another
lesson.**

**(b)** ⭐ **V15 is *"week seven"* and week six is missing** — plus the Orlando recording, plus the
unexamined `Wk9 → Wk10` gap (`M5`). Expect back-references to absent material; **do not reconstruct
it, and do not read the absence as your own error.**

**(c)** **Check the frame sweep's clock.** V14's frames run `+16 s` against their own burned
timecode where V12's and V13's do not (`M3`). **Measure the offset before naming frames**, and if it
recurs, name the cause.

**(d)** **State your timestamp convention once, at the top** (`M2`). Marker grid or ASR clock — both
are defensible, mixing them silently is not.

**(e)** **`A-082` remains the audit target.** V14's 5-pip stop and 30–50-pip target are **drill**
parameters and are fenced out of every spec file. If V15 restates either as method, that is a
finding; if a V15 artifact adopts them, that is the error.

**(f)** **`C-021` and item 168 are owner decisions.** So is item 157. So is the `D3` precedent at
item 179. **Do not resolve any of them from a lesson session.**

**(g)** **The board drill runs for two weeks and V15 is when it reports back.** *"Record your
results and post it in the forum."* If V15 discusses student results, that is Tier-1 evidence about
the drill's real-world behaviour, and **`PT-042` returned `NOT SUPPORTED` on its six computable
steps.** Compare them, and do not reconcile them by adjusting either.

**(h)** **Speaker: test it, do not assume.** V15 is a new week, a new date and a three-week gap —
the exact condition under which this corpus's author runtime has broken before (V03→V04). **V14's
100% proves nothing about V15.**
