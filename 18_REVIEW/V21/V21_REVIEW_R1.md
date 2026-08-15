# V21 — INDEPENDENT REVIEW

**Round:** R1
**Reviewer:** Independent Reviewer / Teacher Agent, fresh session (`DECISIONS.md` `D-003`)
**Date:** 2026-08-15
**Lesson:** `Bootcamp1 Wk10 061712 (75mins).swf` · V21 · 2012-06-17 · 01:14:47
**⭐⭐ THE FINAL LESSON OF THE 21-VIDEO COURSE**
**Submission reviewed:** `video/v21` @ `4bee5f4` (5 commits, `6c0ff15`…`4bee5f4`), forked from `19e6c2a`
**Review branch:** `review/v21`, isolated worktree `MMM-Agents-v21-review` (`D-038`)

---

## FINAL DECISION

**Decision:** `REVISE` — **0 CRITICAL, 1 MAJOR, 3 MINOR, 12 NOTE.**
**Confidence:** `HIGH`.

⛔ **V21 cannot reach `COMPLETE`** until `M1` is fixed and re-reviewed (`D-003`). **There is no V22,
so no lesson gate is held** — but **`M1` blocks the cumulative `FINAL_COURSE_REVIEW.md`** (§8).

**The `MAJOR` is `M1`, and it is the one thing the review brief asked to be tested hardest.** The
brief asked whether `A-141`'s *"the tool is unrecoverable"* is genuinely true before it is accepted
as a permanent gap. **It is not true as stated.** ⭐ **Four script filenames are plainly legible in a
frame this session captured, committed, and then described as containing no legible filename** —
and they independently corroborate two claims the corpus currently records as inferences.

**Everything else the brief flagged came back clean or better than claimed:** the template
permutation is exactly right, `Q-022`'s signature reproduces on all twenty comparisons, the item
numbering and collision history are exactly right, and **`PT-050`'s self-declared largest threat —
the borrowed event definition — is cleared by testing it** (§4).

---

## §1 — SOURCE MATERIAL REVIEWED, BEFORE ANY STUDENT CONCLUSION

| Evidence | What was done |
|---|---|
| The `.swf` | **SHA-256 re-computed: `9eb3b014b55ad18ef3d2ed4d6c5d2bddf14eb8ec6d1f7e60da390f2544ef23fc`** — matches `SOURCE_MANIFEST.md`. **33,002,964 bytes**, matches |
| Audio | Extracted independently: **4487.34 s = 01:14:47.3**, matching the manifest's `01:14:47` |
| **Independent ASR** | **Ten targeted decodes** on the `A-133` passage across **four model families** (`large-v3` at `float32`/`int8`, `medium.en`, `small.en`, `distil-large-v3`), both `vad_filter` settings, plus **0.6× time-stretched** audio — **plus a full-file `large-v3` pass** (§5a) |
| Frames | **All 17 burned timecodes cropped from the pixels and read**, and the install-walkthrough frames **read at magnification** |
| Quarantined corpus | **All 21 lesson folders** re-read for identifier stamps, and V21's trio diffed **against all twenty** others in this reviewer's shell |
| GBP/USD M1 corpus | `mmm_lib`, DEVELOPMENT, both `D-031` arms, `W-A` and `W-B` |

---

## §2 — ⛔⛔ `M1` — `A-141` IS WRONG ON THE FACT IT TURNS ON, AND THE FILENAMES ARE IN THE SESSION'S OWN FRAME

### §2.1 — WHAT THE RECORD SAYS

The claim appears **three times, in three files, as an affirmative negative:**

| File | Statement |
|---|---|
| `AUTOMATION_AMBIGUITIES.md` `A-141` | *"no part of the lesson exposes it: **no filename**, no code, no parameter dialog, no forum link that resolves"* |
| `V21_SOURCE_NOTES.md` §10.5 | *"**no frame in the install walkthrough shows a legible script filename** or parameter dialog"* |
| `V21_HOMEWORK.md` §2 | *"**no file, filename, code or parameter dialog is legible anywhere in the lesson**"* |

and a fourth time by implication in `V21_MASTERY_REPORT.md` §2.3: *"A reviewer wanting the script's
filename would need a denser sweep of `42:38`–`62:28`."*

### §2.2 — ⛔ WHAT IS ACTUALLY ON SCREEN

**`04_SCREENSHOTS/V21/V21_00-49-33_scripts-pasted-into-folder.png` — a frame this session captured,
named, committed, and listed in `INDEX.md` §1 row 12–16.** Its MT4 **Navigator** panel, read here at
6× magnification, shows the `Scripts` tree expanded:

```text
Scripts
├── &sm_Buy_Order_Trainer
├── &sm_Buy_Order_Trainer_Pct
├── &sm_Sell_Order_Trainer
├── &sm_Sell_Order_Trainer_Pct
└── 142 more…
```

⭐ **These are the tool's filenames**, and they are not ambiguous: they carry the word `Trainer`, they
come in **Buy/Sell × plain/`_Pct`**, and they sit in the `experts/scripts` folder the lesson has just
pasted into.

### §2.3 — ⭐ AND THEY CORROBORATE TWO THINGS THE CORPUS RECORDS AS INFERENCES

| Currently recorded as | Now directly attested |
|---|---|
| `A-141`: *"`[00:26:52]`'s *'the one I recommend using is **by order percent**'*, which **implies** at least four variants shipped"* | ⭐ **The `_Pct` suffix is on exactly two of the four.** The *"by order percent"* variant is not an inference — it is on screen |
| `A-141`: *"`[00:41:49]` *'four scripts in there'*"* | ⭐ **Exactly four `&sm_…_Trainer` entries.** The count is attested, not just spoken |

### §2.4 — WHY THIS IS `MAJOR` AND NOT `MINOR`

1. **It is an affirmative false statement of fact about evidence**, not an omission — the session
   **looked** (§10.5 is a *"what the visual pass did NOT settle"* section) and reported the opposite.
2. **It is propagated across three files** and shapes a fourth.
3. **It is the terminal record of the corpus's largest missing artifact.** V21 is the last lesson;
   `A-141` is what a future reader will treat as settled about the only mechanical tool the course
   ever shipped.
4. **It actively misdirects.** The mastery report tells a reviewer to re-sweep `42:38`–`62:28` for the
   filename — **which is inside the range already captured, in a frame already committed.**
5. **It suppresses a citable identifier.** *"An unnamed tool is missing"* and *"`&sm_Buy_Order_Trainer`
   is missing"* are different records; only the second can ever be searched for.

⚠️ **What `M1` does NOT do — and this matters for the remediation's size.** ⭐ **The substance of
`A-141` survives**: the **code, the entry trigger, the fill logic, the order management and the exit
are still not recoverable**, no parameter dialog is legible (checked — the `51:38` frame is a bare
Windows desktop), and **`D-030` still bars reconstructing the tool from the handwritten sheet.**
**The gap is real. The record describing it is wrong on a checkable fact.**

---

## §3 — `A-133` — ⚠️ THE CONCLUSION IS RIGHT, THE CORRECTION BEHIND IT IS NOT

The brief asked this be re-verified *"since a wrong reading here would have wrongly closed the
project's oldest open ambiguity."* **Ten decodes were run.**

`V21_TRANSCRIPT.md` §2a records a **correction** to the committed grid at `[00:05:21]`:

> committed *"the light blue tracer **in** the a DR line"* → **corrected to** *"the light blue tracer
> **AND** the ADR line"*, on one `openai-whisper medium.en` decode.

**This reviewer's ten decodes:**

| Reading | Decodes |
|---|---|
| **"…tracer `in` the ADR line"** | **7** — `large-v3` `float32` (VAD on **and** off), `large-v3` `int8`, `small.en` (VAD on **and** off), `large-v3` on **0.6× stretched**, **`medium.en` on 0.6× stretched** |
| "…tracer `and` the ADR line" | 3 — `medium.en` `int8` (VAD on and off), `distil-large-v3` |

⛔ **The correction does not replicate.** Every `large-v3` configuration returns **`in`**, and
⭐ **`medium.en` itself — the family the session used — flips to `in` when the audio is slowed**,
which is the standard disambiguation test. **The committed grid's `in` is more likely correct, and
the recorded correction should be withdrawn or heavily qualified.**

### §3.1 — ⚠️ AND THE "NEAR-MISS" FRAMING IS GRAMMATICALLY UNSOUND IN BOTH DIRECTIONS

The session's reasoning is that `in` would make the phrase *"an apposition"* identifying the tracer
**as** the ADR line, and so would have closed `A-133`. ⛔ **It would not.** *"X **in** Y"* is
**locative**, not appositive — a thing *in* another thing is not that thing; if anything it
distinguishes them. Apposition would require *"the light blue tracer, the ADR line"*.

⭐ **So `A-133` survives under BOTH readings**, and it survives for a better reason than the one
recorded: **neither reading defines what the blue tracer IS.** The sentence lists things to *use*;
it never says what the tracer is or how to compute it.

⭐⭐ **The outcome — `A-133` NOT closed — is correct, and it is the conservative call.** Nothing was
wrongly closed and the corpus's oldest blocker is intact. **What is charged is that a transcript
correction which does not replicate was entered into the record, and that the stated reason for
`A-133`'s survival is not the real one.** `MINOR`, item **366**.

---

## §4 — `PT-050` — ⭐ THE SELF-DECLARED LARGEST THREAT IS CLEARED BY TESTING IT

`PT-050` §2a names its borrowed event definition — `PT-047`'s exceed event, reused verbatim — as
*"the largest threat"* to validity. The brief asked whether **a V21-native definition changes
anything.** **It does not, and this is the strongest thing this round can say for the submission.**

V21's own stop-hunt material is the `16:40` frame — *"**Hunt Stops!** … **Vary the Levels** that
these stops are triggered at! … **Spike Past** Support & Resistance/Pivots/Breakout levels/Fib
numbers"* — so a V21-native event keys on **spiking past a level**. Three alternatives were built
from that and measured with `PT-050`'s own Outcome A (MFE over `t+1…t+16`), band `[40, 60]`:

| Event definition, `W-A` / arm A | `n` | **median MFE** | boot 95 % | in `[40,60]`? |
|---|---|---|---|---|
| `PT-047` borrowed — **`PT-050`'s choice** | 100 | **29.70** | `[23.30, 38.40]` | ❌ |
| **V21-native:** spike past the **previous day's high** (a pivot) | 107 | 32.90 | `[25.10, 42.40]` | ❌ |
| **V21-native:** spike past the **Asian-box high** (a breakout level) | 190 | 24.75 | `[21.25, 30.85]` | ❌ |
| **V21-native:** exceed event **qualified as a spike** (bar range ≥ 1.5× trailing median) | 60 | 31.20 | `[21.50, 41.95]` | ❌ |

*(The borrowed-definition row reproduces the submission's published `n = 99`, median `29.70` — the
median exactly, `n` off by one on an edge condition. The implementation is faithful.)*

⭐⭐ **No definition reaches the band. All four sit in 24–33 pips against a claimed *"about 50"*,
and `PT-050`'s borrowed choice sits in the MIDDLE of the V21-native alternatives** (24.75 and 32.90
bracket 29.70) — **so the borrowed convention is neither flattering nor unfavourable to the lesson.**
**The null is a property of the claim, not of the imported event definition.** `NOTE` item **371**.

⚠️ **One honest qualification:** the previous-day-high definition's interval reaches `42.40`, i.e.
**into** the band. Under that definition the result would be inconclusive rather than refuted. **The
median is still 32.90 and outside.**

### §4.1 — ⚠️ BUT `N3` FIRED ON A CONDITION THE PRE-REGISTRATION DOES NOT LIST

`PT-050` §4 fixes `N3` as firing if **any of**: *"arms A/B disagree on band membership for Outcome A;
`W-A`/`W-B` disagree; any cell `n < 30`; or **the modal fill cell differs between arms**."*

`run_pt050.py` compares **every cell against the primary cell**, so the modal-fill test also fires
across **windows**. The results JSON records exactly that:

```text
n3_fired: ["A|W-B: modal fill differs", "B|W-B: modal fill differs"]
```

**Both fires are window differences.** Checked here: **the arms agree on modal fill inside every
window** (`W-A`: 3 and 3; `W-B`: 1 and 1), no cell has `n < 30` (99/206/98/207), and **all four cells
agree that the median is outside the band** — so on the pre-registration's literal list **`N3` does
not fire**, and §5's rule reaches `hi (39.60) < 40` → **`REFUTED`**.

⚠️ **The pre-registration is genuinely ambiguous** — clause 2's bare *"`W-A`/`W-B` disagree"* can be
read to cover modal fill as well as band membership, and on that reading the runner is right. ⭐ **And
the direction is conservative**: `FRAGILE` understates a result that the narrow reading would call
`REFUTED`, which is the safe error, and with the interval missing the band by **0.4 pips** a
*"fragile"* characterisation is defensible on the merits. ⛔ **What is charged is that
`PT-050`'s own governance clause — *"if the runner and this file disagree … the disagreement is
reported in `BT_V21_0001.md`"* — was not exercised.** `MINOR`, item **367**.

---

## §5 — THE BRIEF'S REMAINING ITEMS — ALL VERIFIED, ALL CORRECT

### ⭐⭐ THE CLOSED PERMUTATION — EXACT

Read independently out of all 21 quarantine folders (`RULES.md` rule-IDs **and** `VISUAL_INDEX.md`
`VIDEO_` prefixes, which agree everywhere):

```text
L01→V01   L02→V02   L03→V04 … L20→V21   L21→V03
```

⭐ **It is a closed permutation: two fixed points and a single 19-cycle on {03…21}, every label used
exactly once — a bijection.** **`Q-022`'s claim is exactly right**, and its correction of the earlier
*"counts one ahead"* description (true for L03–L20, false at both ends) is a real improvement to
`Q-019`/`Q-020`/`Q-021`.

### ⭐⭐ `Q-022`'s DIFF SIGNATURE — EXACT ON ALL TWENTY COMPARISONS

| V21 vs | NOTES / RULES / VISUAL |
|---|---|
| **V16, V17, V18, V19, V20** | **32 / 30 / 26 — identical on all five** |
| V01–V15 | 6 or 24 / **12** / 8–718 |

**Byte lengths `3,023 / 1,299 / 1,250` and all three SHA-256s re-computed and matching.**
⭐ **Item 254's prediction is now confirmed from both sides of the boundary.**

### ⭐ ITEMS 357–364 AND THE COLLISION HISTORY — EXACT

| Claim | Verified |
|---|---|
| Integration tip `19e6c2a` carried review items **up to 356** | ✅ — V20 R1 took 332–347, V20 R2 took 348–356 |
| First allocation of **349–355** would have collided | ✅ |
| Renumbered to **357–363**, plus **364** recording the collision | ✅ 8 items, `357…364`, contiguous |
| `A-139`, `C-030`, `Q-021` were the tip's highest in their families | ✅ — so `A-140`/`A-141`, `C-031`, `Q-022` were free |

⭐ **Item 364 records the collision rather than quietly fixing it, and names item 297's lesson as the
one it should have followed.** Every particular checks out.

### ⭐ 17 OF 17 FRAME TIMECODES VERIFIED FROM THE PIXELS

`00:20 02:45 07:55 15:00 16:40 20:20 21:20 30:30 31:25 38:44 39:45 42:38 44:24 49:33 51:38 62:28
71:38` — **every one matches its filename's time field.** The §8a claim *"seventeen frames,
seventeen reads"* holds, and the two-effect model (a `+16 s` startup transient absorbed by 30 s,
plus a slow drift to `−2 s`) is consistent with what the readings show.

---

## §5a — THE FULL-FILE INDEPENDENT ASR PASS — RUN HERE, AND IT FINDS NOTHING FURTHER

The submission declares (mastery §2.2) that its independent pass was **targeted, not full-file** —
three passages, ~2 minutes of 75 — and calls the gap owed. **This round ran the full-file pass.**

⚠️ **Disclosed:** the `large-v3` pass entered a **repetition loop at `[01:07:39]`**, a known decoder
failure mode, after cleanly covering `00:00:00`–`01:07:32` (**90 % of the lesson**). The remaining
7 minutes were transcribed separately with **VAD enabled**, which resolved it — the real line is
*"No, not going to happen."* **Combined coverage is complete: 1,481 independent segments against the
committed grid's 928 markers, 11,867 words against 11,964 (0.8 %).**

**Result: no meaning-inverting error anywhere.** A polarity sweep over every committed line carrying
a negation flagged **five** candidates; **all five are window-alignment artifacts** on inspection,
not divergences.

⭐ **And every load-bearing V21 quote verifies verbatim:**

| Marker | Independent pass |
|---|---|
| `[00:04:43]` — item 361's claim | *"**The big board is the high-low board.**"* ✅ **exact** |
| `[00:33:02]` — `PT-050`'s claim under test | *"The average move, **even in stop hunts, is about 50 pips**, right?"* ✅ **exact** |
| `[00:32:58]` | *"Because the take profit had to be adjusted down."* ✅ **exact** |
| `[00:32:50]` / `[00:33:14]` — `C-031`'s reconciliation | *"If all three orders are filled, you will **cycle with 150 pips**"* / *"you'll get **a 30 and a 50** most often"* ✅ **both exact** |

⭐ **So V21's transcript is sound on everything a rule rests on, and the one correction the session
did make is the one that does not hold** (§3). **The targeted-not-full-file gap cost nothing on this
lesson** — unlike V20, where the same gap produced a `MAJOR`.

---

## §6 — FINDINGS

### `CRITICAL` — **NONE**

### `MAJOR`

| # | Item |
|---|---|
| **365** | ⛔⛔ **`M1` — `A-141`'s CENTRAL FACTUAL CLAIM IS FALSE, AND THE EVIDENCE IS IN THE SESSION'S OWN COMMITTED FRAME.** `A-141`, `V21_SOURCE_NOTES.md` §10.5 and `V21_HOMEWORK.md` §2 all state that **no script filename is legible anywhere in the lesson**; `V21_MASTERY_REPORT.md` §2.3 tells a reviewer to re-sweep `42:38`–`62:28` to find one. ⛔ **`V21_00-49-33_scripts-pasted-into-folder.png` — inside that range, already captured and committed — shows the MT4 Navigator `Scripts` tree with four legible entries: `&sm_Buy_Order_Trainer`, `&sm_Buy_Order_Trainer_Pct`, `&sm_Sell_Order_Trainer`, `&sm_Sell_Order_Trainer_Pct`.** ⭐ They also convert two recorded **inferences** into **direct attestation**: *"at least four variants"* (`[00:41:49]`) and *"by order percent"* (`[00:26:52]`) are both on screen. ⚠️ **`A-141`'s substance survives** — no code, no logic, no parameter dialog, `D-030` still bars reconstruction — **but the record is wrong on the one checkable fact it asserts, in four places, as the corpus's closing statement about its only mechanical artifact.** `E01` / `E11` |

### `MINOR`

| # | Item |
|---|---|
| **366** | ⚠️ **THE `[00:05:21]` CORRECTION DOES NOT REPLICATE, AND THE `A-133` "NEAR-MISS" REASONING IS UNSOUND — THOUGH THE OUTCOME IS RIGHT.** §2a records *"in"* → *"and"* on one `openai-whisper medium.en` decode. **Ten decodes here across four model families return `in` seven times**, including **every `large-v3` configuration** and **`medium.en` itself under 0.6× time-stretch**. ⛔ Separately, the claim that *"in"* would have **closed** `A-133` is wrong: *"X in Y"* is locative, not appositive. ⭐ **`A-133` survives under both readings, for the better reason that neither defines the tracer.** Withdraw or qualify the correction; restate the survival reason. `E01` |
| **367** | ⚠️ **`PT-050`'s `N3` FIRED ON A CONDITION ITS OWN §4 DOES NOT LIST, AND THE DIVERGENCE IS UNREPORTED.** §4's fourth condition is *"the modal fill cell differs **between arms**"*; the runner compares every cell to the primary, so it also fires **across windows** — and the JSON shows **both fires are window differences** (`A|W-B`, `B|W-B`). **Arms agree on modal fill in every window (3/3, 1/1); no cell `n < 30`; all four cells agree the median is out of band.** On the literal list `N3` does not fire and §5 gives **`REFUTED`**, not `FRAGILE`. ⭐ **§4 clause 2 is genuinely ambiguous and the direction is conservative** — with the interval missing the band by 0.4 pips, *"fragile"* is defensible. **What is charged is the unexercised governance clause.** `E20` |
| **368** | ⚠️ **TWO FRAME FILENAMES ARE NOT VALID `HH-MM-SS`, BREAKING A STANDARD THE CORPUS ALREADY FOLLOWS.** `FILE_NAMING_STANDARD.md` line 74 fixes `VXX_HH-MM-SS_short-descriptor.png`. V21 ships **`V21_00-62-28_…`** and **`V21_00-71-38_…`** — `62` and `71` in the minutes field. ⭐ **The cause is precise and partly exculpatory:** the player OSD displays elapsed time as **`MM:SS` past the hour** (*"62:28 / 74:4"*), and §8a correctly requires naming from the burned value — **so the burned value was pasted into an `HH-MM-SS` slot without conversion.** ⛔ **V10 (01:36:16) resolved this correctly** — `01-01-22`, `01-15-57`, `01-34-27` — and **V21's own transcript grid uses proper rollover** (`[01:14:24]`), so the lesson is internally inconsistent. Correct to `01-02-28` and `01-11-38`; the recipe should state the conversion. `E19` |

### `NOTE` — no action required

| # | Item |
|---|---|
| **369** | ⭐ **SOURCE INTEGRITY EXACT.** SHA-256 `9eb3b014…44ef23fc` and **33,002,964 bytes** re-computed and matching; audio **4487.34 s = 01:14:47.3** against the manifest's `01:14:47` |
| **370** | ⭐⭐ **THE CLOSED-PERMUTATION CLAIM IS EXACTLY RIGHT**, re-derived from all 21 folders on two independent stamps (rule-IDs and `VIDEO_` prefixes, which agree everywhere). **Two fixed points plus a single 19-cycle — a bijection over all 21 labels.** `Q-022`'s correction of the earlier *"counts one ahead"* description is a real improvement to three prior entries |
| **371** | ⭐⭐ **`PT-050`'s SELF-DECLARED LARGEST THREAT IS CLEARED BY TEST, NOT BY ARGUMENT.** Three V21-native event definitions built from the `16:40` *"spike past …levels"* frame return medians of **32.90 / 24.75 / 31.20** against the borrowed definition's **29.70** — **none reaches `[40, 60]`, and the borrowed choice sits in the middle of them.** **The null belongs to the claim, not to the imported convention** |
| **372** | ⭐ **`Q-022`'s DIFF SIGNATURE REPRODUCES ON ALL TWENTY COMPARISONS** — `32/30/26` against every B-block member, `6-or-24 / 12 / 8–718` against the A block; three SHA-256s and byte lengths exact. **Item 254 is now confirmed from both sides of the boundary** |
| **373** | ⭐ **THE ITEM NUMBERING AND THE `D-047` COLLISION RECORD ARE EXACT IN EVERY PARTICULAR** — tip highest 356, first allocation 349–355 would have collided, renumbered 357–363 plus 364 for the record, and `A-139`/`C-030`/`Q-021` verified as the tip's family highs |
| **374** | ⭐ **17 OF 17 FRAME TIMECODES VERIFIED FROM THE PIXELS**, and §8a's two-effect model (a `+16 s` transient absorbed by 30 s, then a slow drift to `−2 s`) is consistent with the readings. **This is the third sweep corroborating item 296's absolute-deadline mechanism** |
| **375** | ⭐ **THE GATE IS OPEN AND IT IS THE FIRST IN THREE LESSONS OPENED WITHOUT A SELF-VERIFY IN THE CHAIN** — V21 forked from `19e6c2a`, the merge carrying V20's **independent** R2. The mastery report says so and it checks out |
| **376** | ⭐ **FRAME 9 (`31-25`) IS TRANSCRIBED FROM THE PIXELS AND IS THE MOST VALUABLE FRAME IN THE CORPUS** — the instructor's handwritten `High / Low Trainer` specification, dated `1-27-2010` in his own hand. ⚠️ **It specifies risk, grid spacing and cycle targets and NOT the entry logic**, which is why `A-141`'s substance survives `M1` |
| **377** | ⭐ **THE HOMEWORK IS HANDLED CORRECTLY** — all four items recorded `NOT DONE` or `NOT APPLICABLE` with reasons, none approximated, and the deliberate absence of a data block explained rather than left as a gap. ⚠️ Item 1's stated reason inherits `M1`'s error and should be re-worded with it |
| **378** | ⚠️ **THE SESSION'S ASR PASS WAS TARGETED, NOT FULL-FILE** — three passages, ~2 minutes of 75, declared and called owed. ⭐ **This round ran the full-file pass (§5a) and it found NOTHING FURTHER**: 1,481 independent segments, no meaning-inverting error, five polarity flags all alignment artifacts, and **every load-bearing quote verbatim** — `"The big board is the high-low board"`, `"the average move even in stop hunts is about 50 pips"`, `"cycle with 150 pips"`, `"a 30 and a 50 most often"`. **The gap cost nothing here** — unlike V20, where it produced a `MAJOR`. ⚠️ **Disclosed:** the pass hit a decoder repetition loop at `[01:07:39]` after covering 90 % of the lesson; the tail was re-run with VAD, which resolved it |
| **380** | ⭐ **`C-031` AND THE `31:25` HANDWRITTEN SPEC VERIFIED FROM THE PIXELS.** All four figures read directly: `MAX Risk 5% on all orders`, `Risk Setting 1% To 5% … Ex: [Risk % 3]`, three `20 pips` gaps, `Open Live order, 2 pendings … immediately following`, `Take profit +30 pips from ORDER 1 = Market order`, `Sell Cycle / 30 pips`, and `30+50+70 = +150 pips / Most often +80`. ⭐ **`C-031`'s reading is right on both halves** — the `150`/`80` pair reconciles an apparent spoken contradiction, and the other two figures are genuinely unglossed. ⛔ **And the sheet gives risk, spacing and targets but NO entry trigger, fill logic or exit** — which is why `A-141`'s substance survives `M1` |
| **379** | ⭐⭐ **CALIBRATION — THE SESSION SELF-CHARGED A WRONG FIGURE IT HAD ALREADY PUBLISHED MID-ROUND.** `BT_V21_0001.md` §0/§2 were first drafted from a **truncated terminal view** carrying a wrong primary median (26.05 for 29.70), caught by re-reading the JSON before commit, and **recorded as a near-miss of exactly the class items 265 and 332 describe** rather than silently corrected. ⚠️ **`M1` is the mirror image**: the same session that re-checked a number against its artifact did not re-check a claim against its own screenshot |

---

## §7 — REQUIRED CORRECTIONS

1. ⛔ **Item 365 (`MAJOR`).** Read `V21_00-49-33_scripts-pasted-into-folder.png` at magnification and
   **record the four script filenames** in `A-141`. **Correct the false statement in all three
   places** (`A-141`, `V21_SOURCE_NOTES.md` §10.5, `V21_HOMEWORK.md` §2) and **remove the misdirection
   in `V21_MASTERY_REPORT.md` §2.3.** **Re-state what remains missing** — code, entry trigger, fill
   logic, order management, exit — so `A-141`'s substance is preserved and its scope is accurate.
   ⭐ **Move *"four variants"* and *"by order percent"* from INFERRED to ATTESTED**, citing the frame.
2. **Item 366.** Withdraw or heavily qualify the `[00:05:21]` correction in `V21_TRANSCRIPT.md` §2a,
   recording that it does not replicate (7 of 10 decodes, including every `large-v3` and `medium.en`
   under time-stretch, return **`in`**). **Restate `A-133`'s survival on the sound reason** — neither
   reading defines the tracer — in `V21_INTERPRETATION.md` §2.4.
3. **Item 367.** Report the `N3` scope divergence in `BT_V21_0001.md` per `PT-050`'s governance
   clause, state that the literal list gives **`REFUTED`**, and keep `FRAGILE` with its reasoning.
   **Do not re-run and do not edit the pre-registration.**
4. **Item 368.** Rename the two frames to `01-02-28` and `01-11-38` and update the `INDEX.md`
   references. ⭐ **Recommend to the owner** that `SWF_CAPTURE_RECIPE.md` §8a state the OSD-to-filename
   conversion explicitly, since the OSD is `MM:SS` and the standard is `HH-MM-SS`.

---

## §8 — ⭐⭐ IS A CUMULATIVE `FINAL_COURSE_REVIEW.md` WARRANTED NEXT?

**Assessment only — this round does not write it.**

### ⭐ YES, AND THE CORPUS IS CLOSER TO READY THAN ANY PRIOR CHECKPOINT

**All 21 lessons are ingested, and every one has been through an independent round.** The
per-lesson evidence base is unusually solid: source checksums verified lesson by lesson, frames named
from burned timecodes, the fabricated-notes corpus fully characterised and closed (`Q-012`–`Q-022`,
and item 254's prediction now confirmed from both sides), and a pre-registered test attached to most
lessons.

### ⛔ BUT NOT YET — THREE THINGS SHOULD LAND FIRST

1. ⛔ **`M1` (item 365).** A cumulative review will inherit `A-141` verbatim as the corpus's account
   of its only shipped tool. **Fix it before it is quoted forward.**
2. ⚠️ **THE REMEDIATION DEBT IS FIVE LESSONS DEEP AND NONE OF IT IS DISCHARGED.** V17 (244–249),
   V18 (264–268), V19 (303–304), V20 (348), V21 (365–368). **A cumulative review that says the corpus
   is sound while thirteen items are owed across five lessons would be describing a state that does
   not exist.** ⭐ **They are all `MINOR` except `M1`** — so this is a short sweep, not a re-run.
3. ⚠️ **THE OWNER QUESTION FROM V20 R1/R2 IS STILL UNANSWERED** — `SELF-VERIFIED AT OWNER DIRECTION`
   has no numbered decision authorising it for `MAJOR` closure, and V14, V16 and V19 all used it.
   **A cumulative review must state which lessons rest on an independent close and which do not**, and
   that is much easier with a decision on the books than without one.

### ⭐ WHAT IT SHOULD COVER THAT NO PER-LESSON ROUND COULD

* **`A-133` is now permanently open** — the course ended without defining the blue tracer, so
  dimension **B** (recognition) is **permanently blocked** corpus-wide, not merely pending. **That is
  a finding about the course, and only a cumulative review can make it.**
* **`A-141`** — the course's only mechanical artifact was shipped and did not reach the project.
* **The `PT-` series' aggregate result.** `PT-044`–`PT-050` are overwhelmingly null, fragile or
  refuted. ⚠️ **Whether that is a fact about the method or about this project's operationalisations
  is the single most important question the corpus can now ask**, and it cannot be asked one lesson
  at a time.
* **`D-030`'s cumulative cost** — how many rules the corpus can state but not code, and why.

**Recommended sequence: fix 365 → sweep the five lessons' minors → obtain the self-verify decision →
then write `FINAL_COURSE_REVIEW.md`.**

---

## §9 — ADVANCEMENT

```text
LESSON: V21  (FINAL LESSON OF THE COURSE)
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES: none

MAJOR ISSUES:
- M1  E01/E11  A-141's central factual claim is false. "No script filename is
      legible anywhere in the lesson" is stated in three files and implied in a
      fourth; V21_00-49-33_scripts-pasted-into-folder.png shows four legible
      filenames (&sm_Buy_Order_Trainer, _Pct, &sm_Sell_Order_Trainer, _Pct) in
      the MT4 Navigator. They also convert "four variants" and "by order
      percent" from inference to attestation. A-141's SUBSTANCE survives - the
      code and logic remain unrecoverable.

REQUIRED ACTIONS:
1. Record the four filenames in A-141; correct the false claim in three files
   and the misdirection in a fourth; re-state what is still missing.    (365)
2. Withdraw/qualify the [00:05:21] correction; restate A-133's survival
   on the sound reason.                                                 (366)
3. Report PT-050's N3 scope divergence; note the literal list gives
   REFUTED. Do not re-run.                                              (367)
4. Rename two frames to valid HH-MM-SS.                                 (368)

ADVANCEMENT: NOT AUTHORIZED for COMPLETE.
NO LESSON GATE IS HELD - V21 is the final lesson.
FINAL_COURSE_REVIEW.md: NOT YET - see §8.
```

⚠️ **There is no V22, so `D-024`'s gate has nothing to open or close.** What `M1` holds is **V21's own
`COMPLETE` status and the cumulative review**, not another lesson's start.

**V21 STATUS: `IN REMEDIATION` on items 365–368.**

---

## §10 — REVIEWER'S OWN DISCLOSURES

1. **Worktree isolation honoured** — `MMM-Agents-v21-review`, branch `review/v21`, created from
   `4bee5f4`. Separate from the V18 and V20 worktrees. Nothing written in the shared checkout.
2. **The dataset was symlinked, not copied**, into this worktree's Git-ignored
   `06_MANUAL_BACKTEST/datasets/`. Not committed.
3. **Order of work.** Source integrity and the frames first; `PT-050`'s pre-registration read before
   its runner; the V21-native event definitions written from V21's own `16:40` frame rather than from
   the runner.
4. **`M1` was found by magnifying a frame, not by a tool** — the Navigator panel is legible at 6× in
   the committed PNG at its original resolution. **No re-capture was needed.**
5. **Item numbering.** Items **365–379** allocated against integration at `19e6c2a`, where **356** was
   the highest item and `video/v21` holds **357–364**. **No collision.** Re-check at merge-back per
   `D-047`.
