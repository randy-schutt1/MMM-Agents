# V13 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | **V13** · `Bootcamp1 Wk5 041512 Part1 (65mins).swf` · session 2012-04-15, **Part 1 of a two-part recording** whose Part 2 is V14 |
| Review version | **R1** |
| Review date | 2026-08-14 |
| Previous review | none |
| Reviewer branch | `review/v13`, cut from the integration branch @ `f943c9b` (`D-038`), own worktree at `MMM-Agents-v13-review` |
| Submission reviewed | `video/v13` @ `9203b79` (7 commits, `9bc4afd`…`9203b79`) |
| Independence | **`D-003` satisfied.** This session authored no V13 artifact. It located the source `.swf` from `SOURCE_MANIFEST.md` and **re-computed its SHA-256**, extracted the audio and **ran its own ASR pass with a different runtime and a larger model** than the student's; it re-ran the 17-pattern handover scan in its own code; it **re-derived `PT-041` end to end** in code sharing no line with `run_pt041.py` or `mmm_lib`, parsing the raw HistData CSVs directly; it re-ran the `Q-014` `diff` and the 21-lesson clustering at source; and it opened the load-bearing frames as images |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 2 MINOR, 6 NOTE.**

Under `DECISIONS.md` **D-024**, a round carrying zero `CRITICAL` and zero `MAJOR` **opens the gate
for V14.** `COURSE_PROGRESS.md` currently reads *"V14 GATE: CLOSED until V13's R1 returns"* — that
was the correct state to hold, and **this review opens it.** The two minors are carried in
`REVIEW_INDEX.md` as items **154–155** and are owed before V13 can reach `COMPLETE`.

**Confidence: HIGH.**

Confidence is high because every load-bearing claim was **re-derived from source rather than read**:

- **`PT-041` was independently reproduced in full, to the printed decimal.** Reviewer-written code —
  its own CSV parser, its own M15 aggregation, its own DST arm shift, its own session-day and box
  construction, its own outcome measures — reproduces **every reported cell in both arms**:
  `n = 81 / 67`, `O4 = 0.7037 / 0.7015`, `O1 = 0.5432 / 0.5224`, `O2 = 0.6296 / 0.6418`,
  `O3 = 56.80 / 52.90`, and the completeness exclusions **down to the named days and their bucket
  counts** (`2014-12-24` box 26/26 post 44/56 · `2015-08-21` 26/26 55/56 · `2015-12-24` 26/26 44/56).
  The `C-LIKE` control was re-derived under **a different seed** and lands within 0.002 of every
  reported figure.
- **The `A-084` passage was re-transcribed from the source audio with a third engine.** SHA-256
  re-verified (`106bb863…67807`), audio extracted, measured **3922.3119 s** against the header's
  **3922.3118 s**. Passages re-transcribed with **`openai-whisper medium.en`** — a different runtime
  (PyTorch, not CTranslate2) and a **larger** model than the student's `faster-whisper small.en`.
  **All three ASR corrections confirm, and both halves of the `15 hours` / `21 hours`
  self-contradiction confirm verbatim.**
- **The handover scan was re-run in reviewer code** against the committed transcript: **exactly one
  hit**, `[00:00:00]` *"Welcome back"*, and **1,183 markers** — both figures as claimed.
- **The `Q-014` `diff` and the 21-lesson clustering were re-run at source** and return exactly what
  the register claims, cluster membership included.
- **Frames were opened and read as images** — and that is where `M1` came from.

---

## SOURCE MATERIAL REVIEWED — **FIRST, BEFORE ANY STUDENT CONCLUSION**

| Source | References | Purpose |
|---|---|---|
| `02_TRANSCRIPTS/V13/V13_TRANSCRIPT.md` verbatim body | **All 1,183 markers, `[00:00:00]`–`[01:05:21]`** | Primary evidence. Read **before** the source notes, interpretation, homework, backtest or mastery report were opened |
| **The source `.swf` itself** | SHA-256 re-verified; audio extracted to 16 kHz mono | **Independent ASR.** Eight segments re-transcribed by this reviewer |
| Frames `53:35`, `29:35`, `00:15` (V13); `01:27:17` (V10); the quarantined `VIDEO_14_SCREENSHOT_001` | Opened and read as images | Verify `C-020` both halves, the TDI level lines, the legend claim, and `Q-014` §3. **This is where `M1` came from** |
| `_QUARANTINE_UNVERIFIED_NOTES/per_lesson/**` — all 21 `VISUAL_INDEX.md`, `NOTES.md`, `RULES.md` | `diff`ed and normalised-hashed across the whole set | Independent re-derivation of `Q-014` §2 |
| `datasets/HISTDATA_GBPUSD_M1/raw/*.csv` | **1,297,781 M1 bars parsed directly** | Independent re-derivation of the whole of `PT-041` |
| `06_MANUAL_BACKTEST/tools/MMM_TDI.txt` (branch `feature/tradingview-mmm-indicator`, **unmerged**) | Read in full | Test the TDI level-line finding against the project's own tooling. **This is where `N1`/`N2` came from** |
| `DECISIONS.md` `D-003`, `D-004`, `D-024`, `D-026`/`D-029`, `D-030`, `D-031`, `D-035`, `D-036a`, `D-038`/`D-038a`, `D-039`–`D-043`; `SOURCING_HIERARCHY.md`; `REMEDIATION_PROTOCOL.md` | Read | Governing policy |

**Source access was not limited.** The `.swf`, its audio, the transcript, all 30 curated frames, the
quarantined tree and the full M1 corpus were available. **Nothing in this review is capped by missing
evidence**, with the one exception the submission itself records (the 793 sweep frames are not
committed — the same limit V12 R1 recorded at item 140).

## STUDENT ARTIFACTS REVIEWED

| Artifact | Reviewed |
|---|---|
| `V13_TRANSCRIPT.md` header, speaker table, 8 strands, verification, 3 corrections | ✅ in full |
| `V13_SOURCE_NOTES.md` · `V13_INTERPRETATION.md` | ✅ in full |
| `04_SCREENSHOTS/V13/INDEX.md` + **frames opened** | ✅ |
| `05_HOMEWORK/V13/V13_HOMEWORK.md` | ✅ in full |
| `PT-041_…md` · `BT_V13_0001.md` · `data/pt041_output.txt` · `data/pt041_result.json` · `scripts/run_pt041.py` | ✅ in full |
| `07_MASTERY_REPORTS/V13_MASTERY_REPORT.md` | ✅ |
| `QUARANTINE_REGISTER.md` `Q-014` · `A-084` update · `A-087` · `A-088` · `C-020` | ✅ |
| `LOG.md`, `COURSE_PROGRESS.md`, `REVIEW_INDEX.md` items 145–153 | ✅ |

---

## CRITICAL FINDINGS

**NONE.**

The five places a `CRITICAL` could plausibly have arisen were checked directly and all five are clean:

1. **`A-084` closed on a passage that does not close it.** The temptation was real and is the single
   largest hazard in the lesson. **It was declined, and declined on the right ground.** See below.
2. **A threshold moved after the numbers were seen.** `PT-041`'s boundaries are in commit `3ca5beb`,
   and **`run_pt041.py` provably does not exist at that commit** — `git cat-file -e` returns ABSENT.
   The only change to the pre-registration at the run commit is the verdict banner; **`diff` shows no
   threshold, window, filter, arm or measure altered.**
3. **The `25 or 30 pip` drill stop adopted as the method's stop** — the `A-082` shape. **It did not
   happen.** `grep` across `12_MASTER_SPEC/` and `13_MACHINE_SPEC/` returns nothing, and the
   interpretation fences it four ways from the speaker's own words.
4. **A quarantined file's content leaking into a V13 artifact.** Tested independently: **no V13
   artifact cites `NOTES.md`, `RULES.md` or `VISUAL_INDEX.md` as evidence** — every reference is to
   `Q-014` itself. The `Week 5` lead inside the quarantined image was **seen, named, and refused.**
5. **A speaker determination assumed rather than tested on a new week and a new date.** Re-run
   independently; see below.

---

## MAJOR FINDINGS

**NONE.**

---

## ⭐ HOST-vs-GUEST — RE-TESTED INDEPENDENTLY, AND THE SCAN RE-RUN IN REVIEWER CODE

**Reviewer verdict: 100% course author is CORRECT and the determination is over-determined.
Confidence HIGH.**

The task put to this reviewer was to re-verify **at least 2–3** of the eight strands and the
17-pattern scan. **Five strands were re-verified at source and the scan was re-implemented.**

| Strand | Reviewer's independent check |
|---|---|
| **1** — addressed as "Steve" | ✅ Both cited entries confirmed at `[00:16:15]` and `[00:34:56]`. **A third instance the table does not cite** — `[00:43:30]` *"you go Steve, there's only two levels in a week"* — strengthens it |
| **2** — owns the course email | ✅ `[00:18:13]` *"I keep saying I'm going to terminate the address"*; `[00:18:30]` `Steve at MarketmakersForks.com` |
| **3** — owns the student folder | ✅ `[00:02:58]`, and `[00:03:03]` *"I stripped everything out of there. It's just the simple worktime ribbon with no GMT offset"* — quoted accurately across the two entries |
| **5** — owns and can cancel the schedule | ✅ `[00:01:55]` confirmed **on my own ASR pass**, verbatim |
| **6** — runs and pays for the live events | ✅ `[00:08:15]` *"The venue is locked up"*; `[00:09:50]` *"The venue is paid for and the insurance is bought"* |
| **8** — 17-pattern handover scan | ✅ **Re-implemented in reviewer code against the committed body. Exactly ONE hit, `[00:00:00]` "Welcome back".** Not a handover |

**On the late correction at `9203b79`.** The submission's own last commit replaced strand 8's
*"returns two lines"* with *"returns exactly ONE"* and fixed strand 1's `[00:35:00]` → `[00:34:56]`.
**Both corrections are right, and my independent scan lands on the corrected figure, not the
draft's.** A session that greps its own transcript rather than trusting its draft is doing the thing
this review exists to check for; recorded as calibration, charged as nothing.

---

## ⭐ `A-084` — THE NARROWING IS CORRECT, THE CLOSURE IS RIGHTLY DECLINED, AND THE DEFEATER HOLDS

**Reviewer verdict: `A-084` REMAINS AN ACTIVE BLOCKER. The student's reasoning survives a direct
attempt to break it. Confidence HIGH.**

`REVIEW_INDEX.md` item 145 explicitly invited this reviewer to attack the argument, on the ground
that V11's entire RSI half unblocks if it fails. **It was attacked and it does not fail.**

### The passage, from my own ASR pass

`openai-whisper medium.en`, offsets from a clip starting at `[00:54:30]`:

| My pass | Committed record |
|---|---|
| `[00:54:51]` *"here's the weakness with **any** indicator"* | ✅ **correction 1 confirmed** — the supplied *"Fennie indicator"* is ASR noise |
| `[00:55:02]` *"**We have it set to 21.**"* | ✅ **correction 1 confirmed** — first-person, this deployment |
| `[00:55:05]` *"It only looks back **21 periods**"* | ✅ |
| `[00:55:08]` *"let's say you're on a one hour chart, it looks back **15 hours**"* | ✅ |
| `[00:55:22]` *"because it only looks back, it's **limited in what it sees**"* | ✅ **correction 2 confirmed** |
| `[00:55:34]` *"but it may not, because it only looks back **21 hours**"* | ✅ |
| `[00:55:56]` *"**Ralph, if you don't like TDI, then use the RSI.**"* | ✅ defeater 3 confirmed |

**The `15 hours` / `21 hours` self-contradiction is real and it is the speaker's, not the ASR's.**
Three engines now transcribe both halves. `D-030` does not permit a blocker to be closed on a
passage whose own arithmetic disagrees with itself twenty-six seconds apart.

**My pass also supplies a line the record does not quote, and it strengthens narrowing #2**:
`[00:55:39]` *"If you're on a 15 minute chart, it's **21 15-minute periods**, understand?"* — the
lookback is confirmed to scale with the chart timeframe rather than being a wall-clock window,
which is exactly what `A-087` claims and is now quotable rather than inferred.

### The defeater, tested rather than accepted

The load-bearing defeater is that **`MA_k(RSI(21))` inherits the same 21-period lookback**, so the
passage explains a property the two candidates share. **I tried to break it three ways and could
not:**

1. *"He explains a plotted line's height by the lookback"* — true, and equally true of the smoothed
   series, whose input sees exactly 21 periods of price. **The sentence discriminates nothing.**
2. *"He calls the plotted line the RSI line"* — he does, and `MMM_TDI`'s own buffer list calls the
   smoothed buffer **`RSI Price Line`**. **Naming a smoothed buffer after its input is the shipped
   convention**, so the name is evidence of lineage, not identity — which is precisely what `A-084`
   was raised to say.
3. *"'The indicator averages back' means the RSI averages"* — the clause is applied to *"the
   indicator"*, and reading it as the RSI's own internal averaging is the convenient parse of an
   ambiguous one. **The student names this itself and declines it.** Correct.

**The declining is the finding.** This is the second consecutive round in which a session has
reported that its own most attractive result did not deliver what it was hoped to deliver.

---

## ⭐ THE LEGEND ROUTE — THE CONCLUSION SURVIVES, THE WARRANT OVER-REACHES · `M1`

This is the review's principal correction, and it is raised **because** the claim is methodological:
it tells V14–V21 to stop looking for something.

**What is confirmed.** I opened `V13_00-53-35_…png` at full resolution. The sub-window legend reads
**`TDI_MMM 46.2640 42.8277 40.2789`** — indicator short name and three current values, **no
parameter tuple**. The reading is exact and the frame carries its own burned-in timecode
(`53:35 / 65:2`), so it proves its own timestamp. **The observation is correct.**

**What over-reaches.** `A-087` states the conclusion *"any lesson of this corpus, **on this
deployment**, can ever close `A-084`"* — with the qualifier. **Two of the three sites drop it:**

- `04_SCREENSHOTS/V13/INDEX.md` line 52 — *"no legend in **ANY** lesson of this corpus can ever
  close `A-084`"*
- `V13_INTERPRETATION.md` line 85 — the same sentence

**And the qualifier is load-bearing, not pedantry, because the corpus demonstrably runs more than
one TDI build.** I opened `04_SCREENSHOTS/V10/V10_01-27-17_audusd-15m-with-tdi-visual-panel.png`.
Its sub-window legend reads:

```text
Traders Dynamic Index Visual 67.7735 53.7329 39.6923 65.5667 61.7477 51.5016
```

**A different short name and six values, against V13's `TDI_MMM` and three.** The `#property`
argument the record offers is a fact about one indicator's compiled short name; it cannot be
extended by deduction to a build it was not observed on.

**The conclusion nonetheless survives, and on better evidence than the record cites.** The legend
route is empirically dry across **three lessons and both builds**: V10's `Traders Dynamic Index
Visual` carries no parameter tuple either, `04_SCREENSHOTS/V12/INDEX.md` records **five legends
transcribed, not one with a parenthesised parameter**, and V11 R1 established the same for V11. **The
redirection of the V14–V21 hunt to properties dialogs, Navigator/inputs tabs and speech is right.**

> **`M1` — MINOR.** Adopt `A-087`'s qualified wording at all three sites, and cite the V10 build as
> the second observed instance. What is owed is a **restatement of the warrant as empirical rather
> than deductive**, not a retraction: the finding gets *stronger* when the second build is named.

---

## ⭐ `C-020` — BOTH HALVES CONFIRMED, FRAME AND AUDIO, INDEPENDENTLY

**Reviewer verdict: the double contradiction is real, correctly characterised, and correctly left
unadjudicated. Confidence HIGH.**

I opened the cited frame and re-transcribed the cited audio. **Both halves confirm exactly.**

| Half | Printed — read off `V13_00-29-35_…png` | Spoken — **my own ASR pass** | Reviewer |
|---|---|---|---|
| **1 — shadow box** | *"What time should the shadow box paint?"* / **`3 to 4 am NYYC`** | `[00:29:17]` *"3 to 4 am New York, 9 to 10, **I'm sorry**, 3 to 4 am **London**, and 9 to 10 US"* | ✅ **A live self-correction. Five hours apart** |
| **2 — stop-hunt box** | *"What distance should the stop Hunt box be from the blue box?"* / **`25 to 50`** | `[00:30:17]` *"**25 at the bottom or start, 50 pips on the top side** of the range"* → `[00:30:23]` *"**It's a 25 pip box. 25 pips away from the top or bottom** of the blue box"* | ✅ **A muddle, unresolved by the speaker** |

**Transcript correction 3 is confirmed** — the supplied *"So 25 pips box"* is *"It's a 25 pip box"*,
which is the form the symmetric reading rests on.

**The characterisation is right and matters.** These are different in kind — one is a speaker
correcting his own slide, the other is a speaker offering two incompatible readings thirteen seconds
apart — and collapsing them into one "printed vs spoken" bucket would have lost that. **Leaving
conflict 1 open rather than applying *"the recording wins"* is the correct call**, and the student's
own self-correction (item 151) is the reason: V06's printed DMR slide gives *"3:45am or 9:45am
**est**"*, which points at the **slide's** side, i.e. the side that rule would have discarded. **I
verified that V06 citation at `04_SCREENSHOTS/V06/INDEX.md` — it is accurate.**

---

## ⭐ THE TDI LEVEL LINES `63 / 50 / 37` — CONFIRMED, AND IT IS NOT A TOOLING DEFECT · `N1`/`N2`

**Reviewer verdict: the citation is CORRECT. The framing needs one sentence added. NO urgent tooling
attention is required — the opposite is true.**

**Confirmed at the frame.** The right-hand axis of `V13_00-53-35_…png` carries fixed gridlines
labelled **`63`**, **`50`**, **`37`**, with the dynamic band values `65.3876` above and `32.3876`
below. **And the audio corroborates from my own pass:** `[00:51:09]` *"Grab the pen, **shark fin
below the support, 37**."* — the number is spoken, and it is spoken **about the shark fin**.

**The premise that this exposes a wrong default in the project's shipped TDI tool is not correct,
and I checked it directly.** `06_MANUAL_BACKTEST/tools/MMM_TDI.txt` (branch
`feature/tradingview-mmm-indicator`) already ships:

```text
grpL = "Reference levels — [TOOLING] template levels 68 / 63 / 50 / 37 / 32"
//   level_0=68  level_1=63  level_2=50  level_3=37  level_4=32
//   The 63 / 37 pair are the SharkFin_Upper_Level / SharkFin_Lower_Level inputs (A-032).
```

**`68 / 50 / 32` is Dean Malone's publicly circulating TDI — not this project's tool.** §7.1b's
sentence *"The shipped Traders Dynamic Index's defaults are 68 / 50 / 32. These are not those"* is
**true**, and it is the sentence that invites the misreading, because a reader who does not already
know the tool file exists will take *"the shipped"* to mean *ours*. **Nothing is wrong; one clause is
missing.** `N1`.

> ### ⭐ `N2` — AND THE FINDING IS WORTH MORE THAN THE SUBMISSION CLAIMS FOR IT
>
> `MMM_TDI.txt` states its own weakness in terms: *"the file is dated 2016 and 2019, the course was
> recorded in 2012, and nothing in the template proves the settings are the instructor's rather than
> a later user's."* That is the stated reason `A-039` stays open on the template.
>
> **V13's frame is a 2012, Tier-1, instructor's-own-chart datum carrying the template's
> NON-DEFAULT `63 / 37` pair — and the audio ties `37` to the shark fin, matching the template's
> `SharkFin_Lower_Level=37`.** That is precisely the provenance bridge the tool file says is
> missing, arriving from the one source that outranks it.
>
> **The V13 session cannot be faulted for not making this connection** — the tool lives on an
> unmerged branch that is not in `video/v13`'s history, so it was not visible from where the session
> stood. **But the project should now act on it**, and it bears on more than `A-032`:
>
> **The same template block records `RSI_Price_Line=2`, `RSI_Price_Type=0` (MT4 `MODE_SMA`), and the
> tool file's own gloss — *"!SM_TDI does not plot the bare RSI, it plots the Fast MA of it"* — is a
> direct answer to `A-084`'s question, with `k = 2`.** `PT-040` has already measured that arm: `5.16
> pp` at `k=2, t=50`, past its own materiality boundary. **`A-084` cannot be closed on it today** —
> the template is an evidence class with no tier and no admitting decision, exactly as `MMM_TDI.txt`
> says — **but "is `!SM_TDI` admissible, and at what tier?" is now a decision worth putting to the
> owner, because V13 has materially improved the case that the template is his.** Raised as item
> 158; this is a project-level question, not a V13 remediation.

---

## ⭐ `PT-041` — INDEPENDENTLY REPRODUCED IN FULL, TO THE PRINTED DECIMAL

**Reviewer verdict: `PARTIALLY SUPPORTED` is the correct verdict, correctly derived, and the
pre-registration ordering is proven. Confidence HIGH.**

### Method — genuinely independent

Reviewer-written code, sharing no line with `run_pt041.py` or `mmm_lib.py`: its own CSV reader over
the raw HistData files (**1,297,781 M1 bars**), its own 15-minute bucketing, its own `zoneinfo`-derived
DST shift for Arm B, its own session-day / box / post-box construction from `C-1`/`C-2`/`C-3`, its own
`C-6` completeness gate, its own `F1`–`F5` and `O1`–`O4`.

### Every reported figure reproduces

| Measure | Arm A — committed | Arm A — **reviewer** | Arm B — committed | Arm B — **reviewer** | |
|---|---|---|---|---|---|
| `n` | 81 | **81** | 67 | **67** | ✅ |
| `O4` — the premise | 0.7037 | **0.7037** | 0.7015 | **0.7015** | ✅ |
| `O1` = P(MFE ≥ 50) | 0.5432 | **0.5432** | 0.5224 | **0.5224** | ✅ |
| `O2` = P(MFE ≥ 40) | 0.6296 | **0.6296** | 0.6418 | **0.6418** | ✅ |
| `O3` median MFE | 56.8 | **56.80** | 52.9 | **52.90** | ✅ |
| `C-LIKE` P(≥50) / P(≥40) / median | .094 / .167 / 14.41 | **.095 / .168 / 14.32** | .101 / .176 / 15.29 | **.103 / .178 / 15.29** | ✅ **different seed** |

**The completeness accounting reproduces down to the named days**: 512 complete session days in both
arms, **3 excluded**, and my run names the same three with the same bucket counts — `2014-12-24`
(box 26/26, post 44/56), `2015-08-21` (26/26, 55/56), `2015-12-24` (26/26, 44/56). **Zero
tie-exclusions, 2 no-bars-after-extreme, both arms** — all confirmed. I also checked the arm-B
day-count asymmetry that a reader might mistake for a defect: the extra session-day shells the DST
shift creates are **empty Saturdays**, correctly not counted as candidates. **No finding.**

### The verdict is the pre-registered one

`O4 = 0.704 / 0.701` against `≥ 0.80` **fails**. `O2 = 0.630 / 0.642` against `≥ 0.70` **fails**.
`O1 = 0.543 / 0.522` against `≥ 0.50` **passes**. `O2 ≥ 0.50` in both arms with `n ≥ 30`, so
**`PARTIALLY SUPPORTED`** is exactly what `§6` prescribes. **Two near-misses were honoured rather
than rounded**, and both boundaries predate the runner.

### Pre-registration ordering — PROVEN

```text
git cat-file -e 3ca5beb:06_MANUAL_BACKTEST/scripts/run_pt041.py   ->  ABSENT   ✅
git cat-file -e 3ca5beb:…/PT-041_the_range_arithmetic…md          ->  PRESENT  ✅
runner first added at 1136d94 (5 minutes later)
git diff 3ca5beb 1136d94 -- PT-041…md  ->  the verdict banner and the STATUS line. NOTHING ELSE.
```

**No threshold, window, filter, arm, outcome measure or decision boundary moved.** `D-026` satisfied
by ordering, not by assertion.

### `M2` — the one thing the control disclosure asserts but does not show

The `D3` self-disclosure (item 149) is **substantively right**: `C-LIKE` is a same-metric control,
it is stricter than what was pre-registered, both controls are reported, and the verdict does not
turn on either — `O4` and `O2` are pure rule-arm measurements. **That is honest handling and it is
credited.**

But §5's stated *direction* of the defect — *"it would have made the baseline look smaller than it
is"* — **is not demonstrated by the numbers committed, and the one comparable statistic points the
other way**: `C-PRE`'s median is **17.59 / 18.25**, *larger* than `C-LIKE`'s **14.41 / 15.29**.
`C-PRE`'s `P(≥50)` and `P(≥40)` — the statistics the §6 clause actually adjudicates — **are never
computed**: `run_pt041.py:172` takes only a median, and `data/pt041_output.txt` prints only the
median line.

The direction claim is very probably right *for the tail* — a stop/target-truncated MFE cannot reach
50 as often as an unbounded one — but **as committed it is asserted, not shown, and it sits in a
table where the only checkable figure contradicts the sentence.** Cheap to fix.

> **`M2` — MINOR.** Either compute and report `C-PRE`'s `P(≥50)` / `P(≥40)`, or narrow §5's sentence
> to the tail and say plainly that the median runs the other way and why. `PT-041` §5 is owed an
> amendment for any re-issue in either case, as item 149 already concedes.

---

## ⭐ `Q-014` — VERIFIED BY EXACT DIFF, AND THE CLUSTERING RE-RUN AT SOURCE

**Reviewer verdict: every measured claim reproduces exactly. Confidence HIGH.**

**The `diff`, re-run by me:**

```text
diff 12_…Wk4_040812_Part2/VISUAL_INDEX.md  13_…Wk5_041512_Part1/VISUAL_INDEX.md
  -> 8 differing lines = FOUR changed pairs: the .swf filename and three
     VIDEO_13 -> VIDEO_14 screenshot names.
     ZERO content lines differ.                                    ✅ EXACT
```

**The 21-lesson normalised clustering, re-implemented by me** — normalising the `.swf` filename, the
`VIDEO_NN` identifiers and the `VNN-R` prefixes, then hashing:

| File | Claimed | **Reviewer** | |
|---|---|---|---|
| `VISUAL_INDEX.md` | 8 distinct; cluster `03,04,09,10,11,12,13,14,15,21`; second cluster `16–20` | **8 distinct; identical membership, both clusters** | ✅ |
| `NOTES.md` | 17 distinct; cluster `16–20` | **17 distinct; `16,17,18,19,20`** | ✅ |
| `RULES.md` | cluster `16–20` | **17 distinct; `16,17,18,19,20`** | ✅ |

**"15 of 21 lessons covered by exactly two documents" is confirmed**, and the `16–20` row is a real
piece of forward information for sessions that have not started.

**The title-card claim, verified by opening the image.** `VISUAL_INDEX.md` indexes three screenshots;
**only `VIDEO_14_SCREENSHOT_001_00-02-00.jpg` exists on disk** — I confirmed `002` and `003` are
absent. I opened `001`: it is a **colour-corrupted title card reading `MARKET MAKER BOOT CAMP` /
`Week 5`**, indexed as *"Asian Box accumulation range with 5, 13, 50, 200, and 800 EMAs"*. **The
third-consecutive claim holds** — V11 (`Q-012`) and V12 (`Q-013`) each have exactly one surviving
image and each was found to be a title card, both under independent review.

**The negative string claims check out**: `30 to 90` — **0 occurrences** in the 1,183-entry
transcript; `10 to 15` — **0**; `ketchup` — **0**.

**The `raspberry` phrasing correction (item 151, self-correction 1) is accurate.** The string occurs
in `V07_TRANSCRIPT.md` at **line 202** — which is in the file's header/notes block, **56 lines above
the `# VERBATIM TRANSCRIPT` marker at line 258** — i.e. as a record of its own absence, exactly as
the corrected wording says. **The original draft's *"occurs zero times in the corpus"* would have
been false; the restatement is true.**

**The declined lead is the right call.** The quarantined image does appear to print `Week 5`, and the
week number is independently established by `[00:17:52]` and the filename. Refusing to launder it out
of a quarantined file, and recording that the temptation was seen, is the correct handling.

---

## THE SELF-DISCLOSED DEVIATIONS — CHECKED, AND HANDLED PROPERLY

**Reviewer verdict: all six self-disclosures are accurate, none is smoothed over, and every one is
made in the artifact a reader hits first rather than in a footnote.**

| # | Deviation | Reviewer check |
|---|---|---|
| **147 / D1** | §9 ordering broken — frames viewed before the source notes were written | ✅ **Accurately described and properly mitigated.** Disclosed in `V13_SOURCE_NOTES.md` **§0, before §1**. Every item carries `[AUDIO]`/`[PRINTED]`/`[AUDIO+PRINTED]`, and the tags are falsifiable by grep — I spot-checked several. **The load-bearing conclusion is unaffected**: `A-087` rests on `[AUDIO]`, and I re-derived that passage from the audio myself without reference to any frame |
| **148 / D2** | Homework substituted — the repository graded against the key rather than a faked blind attempt | ✅ **The right call, and I would have made the same one.** The exam and its key are in one file and the protocol requires the transcript be read first, so a closed-book attempt was structurally impossible. **Fabricating one would have been the corrosive option** in a repository that has quarantined material for exactly that. **Both invited findings check out:** `vacate` occurs in **no** V01–V12 transcript or lesson note — only in V13's files — so `Q13`'s *"ABSENT from twelve lessons"* is exact; and `Q16`'s corroboration is real — V10's `25 to 75` is printed at `75:57`, and **my own ASR pass confirms V13 `[00:39:29]` *"25 to 75 pips"*** from a different deck five weeks later |
| **149 / D3** | Defective `PT-041` control that would have flattered the result | ✅ Substantively correct, honestly disclosed, verdict does not turn on it — **but see `M2`** on the one clause that is asserted rather than shown |
| **150 / D4** | `mmm_lib` seed defect (item 113) live for the first time | ✅ **Accurate.** `mmm_lib.py:116` `SEED = 20260812`; `run_pt041.py:180` `rng = np.random.default_rng(L.SEED)` and `boot_ci` inherits it. The escalation is correct and item 113 is genuinely owed. **Reassuring measurement from this review:** my `C-LIKE` re-derivation under a **completely different seed** moved the point estimates by ≤ 0.002 — so the dependence is real but small, which the record could not have known and can now cite |
| **151 (1)** | `Q-014` §4a over-claimed novelty | ✅ Verified above. The correction is right and the corrected `raspberry` phrasing is exactly true |
| **151 (2)** | `C-020` §1 first argued a direction V06 reverses | ✅ Verified at `04_SCREENSHOTS/V06/INDEX.md` — the DMR slide prints *"3:45am or 9:45am est"*. **The first draft's reasoning was wrong and the correction is right** |

**Both `151` corrections were caught by checking against the repository rather than against memory,
and both are left visible.** That is the behaviour `REMEDIATION_PROTOCOL.md` §2 exists to produce.

---

## THE V14 / WEEK-6 GAP — EVIDENCE CONFIRMED, FRAMING IS FAIR

**Reviewer verdict: all three quotes confirm verbatim on my own ASR pass, the calendar arithmetic is
right, and the deliberate refusal to decide is correct.**

| Cited | **My independent transcription** | |
|---|---|---|
| `[00:01:55]` | *"Alright, **there's going to be no boot camp next week**."* | ✅ verbatim |
| `[00:05:20]` | *"**Next session is going to be Sunday the 29th, that's two weeks.**"* | ✅ verbatim |
| `[00:05:33]` | *"we'll get started again with **week six through ten** or six through, **I don't know how many we're going to do yet**."* | ✅ verbatim |

**Calendar, checked independently:** 2012-04-15 is a Sunday; 2012-04-21 is the following Saturday
(the Orlando meetup, named at `[00:07:41]`); 2012-04-29 is a Sunday and exactly 14 days later; the
next surviving file is `Wk7 050612` = **2012-05-06**, one week *after* the announced return.

**The framing is fair and it is the harder of the two available framings to write.** A missing Week 6
recording and a schedule slip both fit these facts, and the record says so and stops. **Nothing here
decides between them**, and the artifact's value — that V14 now has one specific cheap thing to
listen for — is stated without inflation.

---

## MINOR FINDINGS

| # | Finding | Where |
|---|---|---|
| **`M1`** | **The "legend route is closed corpus-wide" claim is stated without `A-087`'s deployment qualifier at two of three sites, and the corpus demonstrably runs a second TDI build the `#property` argument does not cover** — `V10_01-27-17`'s legend reads `Traders Dynamic Index Visual` with **six** values against V13's `TDI_MMM` with three. **The conclusion survives and gets stronger** when the second build is named: the route is empirically dry across three lessons and both builds. What is owed is the qualifier and the citation, not a retraction | `04_SCREENSHOTS/V13/INDEX.md:52`; `V13_INTERPRETATION.md:85`; ✅ `A-087` already correct |
| **`M2`** | **`BT_V13_0001` §5 asserts a direction for the control defect that the committed numbers do not show, and the one comparable figure points the other way** — `C-PRE` median **17.59 / 18.25** vs `C-LIKE` **14.41 / 15.29**. `C-PRE`'s `P(≥50)` / `P(≥40)`, which the §6 clause adjudicates, are never computed. Compute them, or narrow the sentence to the tail | `BT_V13_0001.md` §5; `run_pt041.py:172`; `data/pt041_output.txt` |

---

## NOTES

| # | Note |
|---|---|
| **`N1`** | **§7.1b's TDI-level sentence invites a wrong inference.** *"The shipped Traders Dynamic Index's defaults are 68/50/32"* means **Dean Malone's public TDI**; the project's own tool already ships **68 / 63 / 50 / 37 / 32** with 63/37 named as the SharkFin levels. One clause naming which "shipped" is meant removes the ambiguity. **No tooling fix is required** |
| **`N2`** | ⭐ **The `63 / 37` finding is worth more than it is claimed for, and it raises an owner-level question.** V13 supplies the 2012 Tier-1 corroboration `MMM_TDI.txt` says the `!SM_TDI` template lacks — including the audio tie of `37` to the shark fin. The same template records `RSI_Price_Line=2`, which is a candidate answer to `A-084` at `k=2`, an arm `PT-040` has already measured. **Put to the owner: is `!SM_TDI` admissible, and at what tier?** Not a V13 remediation |
| **`N3`** | **Item 152 — V13's exam is a genuine reusable instrument and the session was right not to extend `19_STUDENT_TEST_SUITE`'s scope from a task branch.** Both the unlabelled question frames and the instructor's answered versions are committed. **Endorsed to the owner** |
| **`N4`** | **Item 153 — `09_CHART_EXAMPLES/` is empty project-wide, confirmed: all four directories hold only `.gitkeep`, across thirteen lessons.** Agreed that V13 is a poor lesson to close it on, since its charts are the instructor's own worked answers. **Standing project gap, not a V13 regression** |
| **`N5`** | **Item 147's verifiability limit is real and correctly stated** — the 793 sweep frames are not committed, so *"no properties dialog in 793 frames"* is not repository-reproducible. Same class as V12 R1 item 140. **The 30 committed frames do include all three TDI charts and the legend**, so the claims this review turned on **were** checkable, and I checked them |
| **`N6`** | **Calibration, charged as nothing.** The submission's own final commit `9203b79` corrected strand 8 from *"two"* hits to *"exactly ONE"* and fixed a timestamp — and **my independent scan returns the corrected figure.** A session that greps its own transcript rather than trusting its draft, twice more at `Q-014` §4a and `C-020` §1, is the behaviour this round was checking for |

---

## WHAT V13 CONTRIBUTES, IN THIS REVIEWER'S JUDGEMENT

**V13 is not a lesson and the submission is right to say so first.** Its value is of three kinds, and
all three survive review:

1. **A near-miss on the corpus's highest-value blocker, correctly declined.** `A-084` narrows on
   three counts and closes on none. **The narrowing that will matter most to V14–V21 is #2** — the
   lookback is a count of chart periods, not a wall-clock window — which my pass can now quote
   directly (`[00:55:39]`).
2. **The first internal Tier-1 contradiction found by comparing print against speech on one slide.**
   `C-020` exists only in the comparison, which is `SWF_CAPTURE_RECIPE.md` §9's stated rationale
   producing its intended effect.
3. **An unexpected corroboration of the project's own tooling from 2012 audio and pixels** — the
   `63 / 37` SharkFin levels. The submission under-reads this; `N2` re-reads it.

**And one thing it establishes negatively:** after two lessons predicted to carry a properties
dialog and 1,465 swept frames between them, **the frame route to `A-084` has produced nothing**, and
the reasons are now understood rather than guessed at.

---

## REVIEW_INDEX ITEMS RAISED

Items **154–161**. Items 145–153 are the student session's own, raised for this round, and are
dispositioned in `REVIEW_INDEX.md` alongside these.

---

## GATE

```text
V14 GATE: OPEN.

D-024: this round carries 0 CRITICAL and 0 MAJOR, so the gate for V14 opens.
Items 154-155 (MINOR) are owed before V13 reaches COMPLETE.
D-004 is untouched: V13 is NOT COMPLETE and does not become COMPLETE until a
reviewer PASS. This is a REVISE.

V14 is Part 2 of the SAME recording session (Wk5 041512 Part2, 48 mins).
Carry forward to V14:
  (a) A-084 remains an ACTIVE BLOCKER. V11's RSI threshold claims STAY BLOCKED.
      The remaining routes are three: a properties dialog, a Navigator/inputs
      tab, or a spoken identity statement. The legend route is dry across three
      lessons and two builds -- but state that as MEASURED, not DEDUCED (M1).
  (b) The promised "new lesson" content is deferred to V14 by the speaker
      himself, twice. V14 is where it should arrive; if it does not, THAT is
      when a gap is recorded.
  (c) Listen for anything about the return date or the week numbering -- it is
      the cheap decider between "Week 6 missing" and "the break ran long".
  (d) Speaker determination must be TESTED again. V14 is the same date and the
      same session, which is the weakest case for a break, but the strands are
      cheap and V03->V04 is why the rule exists.
  (e) N2's question -- the admissibility of !SM_TDI -- is an OWNER decision and
      must not be resolved by a lesson session on its own authority.
```

---

**Reviewed by:** independent reviewer session, branch `review/v13`, worktree
`MMM-Agents-v13-review`, 2026-08-14.
**`D-003` satisfied.** No V13 artifact was authored by this session.
`validate_project.py`: **PASS** before push.
