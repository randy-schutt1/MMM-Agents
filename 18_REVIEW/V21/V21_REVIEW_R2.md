# V21 — INDEPENDENT REVIEW, ROUND 2

**Round:** R2 — remediation re-review of `V21_REVIEW_R1.md`
**Reviewer:** Independent Reviewer / Teacher Agent (`D-003`)
**Date:** 2026-08-15
**Lesson:** `Bootcamp1 Wk10 061712 (75mins).swf` · V21 · 2012-06-17 · 01:14:47
**⭐⭐⭐ THE FINAL LESSON OF THE 21-VIDEO COURSE**
**Reviewed:** `video/v21` @ **`4342a22`** — **1 commit** on top of R1's `4bee5f4`
**Review branch:** `review/v21`, isolated worktree `MMM-Agents-v21-review` (`D-038`)

---

## FINAL DECISION

> # ⭐⭐⭐ **`PASS`**
>
> **0 CRITICAL, 0 MAJOR, 0 MINOR, 6 NOTE. Confidence: `HIGH`.**

**All four R1 findings are discharged, and every one was re-verified independently rather than taken
on the remediation's account of itself.** No new finding.

⭐⭐ **V21 reaches `COMPLETE`, and with it the 21-video corpus is ingested and independently reviewed
end to end.**

⚠️ **`PASS` is a verdict on V21's execution, not a claim that the corpus is finished.** Five lessons
still carry undischarged minors and the cumulative review is not yet warranted — §5.

---

## §1 — `M1` / ITEM 365 — ⛔ **CLOSED**

### §1.1 — THE FILENAMES, RE-READ FROM THE FRAME ON THE NEW TIP

**Not taken from the remediation's transcription.** The frame was extracted from `4342a22` itself and
re-cropped at **9×**:

```text
&sm_Buy_Order_Trainer
&sm_Buy_Order_Trainer_Pct
&sm_Sell_Order_Trainer
&sm_Sell_Order_Trainer_Pct
142 more…
```

⭐ **Character-for-character identical to what `A-141` now records.**

### §1.2 — AND THE NEW MATERIAL IT ADDS WAS CHECKED TOO, NOT ACCEPTED

The rewrite goes beyond what R1 required and enters four further readings from the same frame.
**All four verified from the pixels here:**

| `A-141` now records | Verified |
|---|---|
| Platform `MIG Bank Trading Station — Classic — Demo Account` | ✅ title bar, read at 4× |
| Chart `GBPUSD,M15` | ✅ title bar |
| Tabs `GBPUSD,M15` / `GBPCHF,M15` / `AUDUSD,H1` | ✅ read at 6× |
| Indicator pane `TDI_MMM`; EA `Heidi_Mauro_closeAll` | ✅ both legible |

⭐ **And the restraint is right.** `TDI_MMM` is recorded and **explicitly not pursued** — *"a 2012
instance name, and this session claims no relation to the owner's 2023-era `MMM_TDI.txt`"*
(`D-052`/`D-053`). **That relation would need separate evidence and none is offered.** Likewise the
`&sm_` prefix is flagged as *"a reading of a naming convention, not a stated fact."*

### §1.3 — THE GAP IS RESTATED INTACT, AND ALL FOUR PROPAGATION SITES ARE FIXED

⭐ **The substance survives exactly as R1 required:** *"No code. No entry trigger. No fill logic. No
order management. No exit logic. No parameter dialog."* **`D-030` still bars reconstruction.** The
superseded title is struck and retained per `REMEDIATION_PROTOCOL.md` §2.

**Checked by `grep` across the new tip — the false claim survives nowhere:**

| Site | State |
|---|---|
| `AUTOMATION_AMBIGUITIES.md` `A-141` | ✅ only inside its own *"WHAT THIS RECORD GOT WRONG"* section |
| `V21_SOURCE_NOTES.md` §10.5 | ✅ corrected — **and correctly keeps the true half** (no parameter dialog, no code) |
| `V21_HOMEWORK.md` §2 | ✅ **clean** |
| `V21_MASTERY_REPORT.md` §2.3 | ✅ **the misdirection is gone** — it no longer sends a reviewer to re-sweep `42:38`–`62:28` |

⭐⭐ **And the root cause is stated more sharply than R1 put it:** *"THE ROOT CAUSE OF `M1` IS NOT THE
SWEEP DENSITY I BLAMED IN §2.3 — IT IS THAT I DID NOT READ MY OWN EVIDENCE. I captured the frame,
named it 'scripts-pasted-into-folder', committed it, and then asserted four times that it contained
no filename."* **That is the correct diagnosis and it is worth more than the fix.**

---

## §2 — ITEM 366 — ⛔ **CLOSED**, AND A FRESH DECODE CONFIRMS IT

The correction is **withdrawn** in `V21_TRANSCRIPT.md` §2a, the grammatical error is **conceded**,
and `A-133` is restated on the ground R1 identified.

### §2.1 — ⭐ R2 RAN THE WORD COUNT AGAIN, ON A DIFFERENT WINDOW

**Deliberately not a re-run of R1's clip.** A different extraction window (296 s / 46 s against R1's
308 s / 30 s), so segmentation and context differ, plus a **0.5×** stretch against R1's 0.6×:

| Decode | Result |
|---|---|
| `large-v3` `float32`, normal | **`in`** |
| `large-v3` `int8`, **0.5× slowed** | **`in`** |
| `medium.en` `int8`, normal | **`in`** |
| `medium.en` `int8`, **0.5× slowed** | **`in`** |
| `small.en` `int8`, normal | `and` |
| `distil-large-v3` `int8`, **0.5× slowed** | **`in`** |

**R2 tally: 5 `in` / 1 `and`. Combined with R1's 7/3 → ⭐ 12 of 16 across four model families.**

⚠️ **The models are individually unstable** — `medium.en` returned `and` at R1's window and `in` at
both speeds here; `small.en` returned `in` at R1's window and `and` here; `distil-large-v3` flipped
the other way. ⭐ **That instability is itself the finding: no single decode should ever have carried
this correction**, which is exactly what the withdrawal now says.

### §2.2 — THE RESTATED GROUND IS THE RIGHT ONE

> *"`A-133` survives under BOTH readings, for the better reason that NEITHER DEFINES THE TRACER …
> the corrected reason is stronger because it does not depend on which word was said."*

⭐ **Correct, and it is the durable form of the record** — it cannot be overturned by a future decode.

---

## §3 — ITEM 367 — ⛔ **CLOSED**, AND NOTHING WAS RE-RUN

`BT_V21_0001.md` §5 is corrected from *"NONE"* to a full disagreement report, with a condition-by-
condition table showing that on §4's literal list `N3` does not fire and §5 gives **`REFUTED`**.

⭐ **Verified by `git diff` across `4bee5f4..4342a22` — all three are byte-identical:**

| Artifact | State |
|---|---|
| `PT-050_the_high_low_trainer_grid.md` | ✅ **UNCHANGED** — the pre-registration governs and was not edited |
| `run_pt050.py` | ✅ **UNCHANGED** |
| `pt050_results.json` | ✅ **UNCHANGED — the test was not re-run** |

⭐ **And the mitigations are stated by the submission before the charge, accurately:** §4 clause 2 is
genuinely ambiguous about *what* must disagree, and the direction is conservative — `FRAGILE`
understated a result the literal reading calls `REFUTED`, **against** the lesson rather than for it,
with the interval missing the band by 0.4 pips. **What was owed was the disagreement report, and
that is what landed.**

---

## §4 — ITEM 368 — ⛔ **CLOSED**

| Check | Result |
|---|---|
| `00-62-28` → `01-02-28`, `00-71-38` → `01-11-38` | ✅ |
| **Pure renames?** | ✅ **blob hashes identical across the rename** — no re-encode, no content change |
| Arithmetic | ✅ `62:28 = 3748 s = 01:02:28`; `71:38 = 4298 s = 01:11:38` |
| All 17 frames valid `HH-MM-SS` | ✅ **no minutes or seconds field ≥ 60 anywhere** |
| `INDEX.md` cross-references | ✅ updated in the §8a table, the frame table and the closing row |
| Cause recorded | ✅ the OSD shows `MM:SS` past the hour; **V10's correct precedent cited**, and a recipe recommendation raised rather than made |

---

## §5 — ⭐⭐ CUMULATIVE `FINAL_COURSE_REVIEW.md` — READINESS, RE-ASSESSED

R1 named three blockers. **One is now cleared.**

| R1 blocker | State |
|---|---|
| **(1) Fix item 365** before a cumulative review inherits `A-141` verbatim | ✅ **CLEARED** — and the corrected record is materially better than the original |
| **(2) The remediation debt** | ⚠️ **STILL OPEN — and it is now the only substantive blocker.** V17 (244–249), V18 (264–268), V19 (303–304), V20 (348). ⭐ **V21 is fully discharged**, so the debt is **four lessons, twelve items, ALL `MINOR`** |
| **(3) The self-verify decision** | ⚠️ **STILL OPEN.** `SELF-VERIFIED AT OWNER DIRECTION` has no numbered decision and V14, V16 and V19 all used it |

### ⭐ MY READ: **CLOSE — AND THE REMAINING WORK IS A SWEEP, NOT A ROUND**

**Twelve `MINOR` items across four lessons, none of which requires re-capturing, re-transcribing or
re-testing anything.** ⚠️ **But `D-003` reserves closure of each to an independent reviewer**, so the
sweep is a fix round *plus* a verification round, not a single pass.

**Recommended sequence, unchanged from R1 minus the cleared item:**
**sweep V17–V20's twelve minors → obtain the self-verify decision → then write it.**

### ⭐⭐ AND V21 SHARPENS WHAT THE CUMULATIVE REVIEW WILL HAVE TO SAY

* ⛔ **`A-133` is now PERMANENTLY open.** The course ended without defining the *blue tracer*, so
  **dimension B (recognition) is permanently blocked corpus-wide** — not pending, not deferred.
  **Eight lessons carried it; V21 was the last chance and it did not come.**
* ⛔ **`A-141`** — the course's only mechanical artifact was **named, specified by hand and installed
  on camera**, and its code did not reach this project. ⭐ **It now has four filenames**, which is the
  difference between an unnamed absence and a searchable one.
* ⚠️ **The `PT-` series' aggregate.** `PT-044`–`PT-050` are overwhelmingly null, fragile or refuted.
  ⭐ **V21 R1 tested whether `PT-050`'s null was an artifact of its borrowed event definition and it
  was not** — three V21-native definitions returned 32.90 / 24.75 / 31.20 against a claimed *"about
  50"*. **That is one data point toward the real question: whether the null record is a fact about
  the method or about this project's operationalisations.** **The cumulative review is where that
  question gets asked, and it now has evidence rather than only a suspicion.**
* ⭐ **The fabricated-notes corpus is fully solved** — `Q-012`–`Q-022`, item 254's prediction
  confirmed from both sides, and the label scheme shown to be **a closed permutation** rather than an
  off-by-one.

---

## §6 — FINDINGS

### `CRITICAL` / `MAJOR` / `MINOR` — **NONE**

### `NOTE`

| # | Item |
|---|---|
| **381** | ⭐⭐ **ALL FOUR R1 FINDINGS DISCHARGED, AND EACH RE-VERIFIED FROM SOURCE RATHER THAN FROM THE REMEDIATION'S ACCOUNT.** 365 by re-reading the frame at 9× off the new tip; 366 by a **fresh 6-decode run on a different window**; 367 by `git diff` proving the pre-registration, runner and results JSON untouched; 368 by blob-hash comparison proving pure renames |
| **382** | ⭐ **THE `A-141` REWRITE ADDS FOUR NEW READINGS AND ALL FOUR CHECK OUT** — `MIG Bank Trading Station — Classic — Demo Account`, chart `GBPUSD,M15`, tabs `GBPUSD,M15`/`GBPCHF,M15`/`AUDUSD,H1`, and the `TDI_MMM` pane with the `Heidi_Mauro_closeAll` EA. ⭐ **And the restraint is right**: `TDI_MMM` is recorded and **explicitly not related** to the owner's 2023-era `MMM_TDI.txt` (`D-052`/`D-053`), and the `&sm_` prefix is flagged as a convention reading rather than a fact |
| **383** | ⭐ **THE R2 DECODE CONFIRMS ITEM 366 ON A DIFFERENT WINDOW: 5 `in` / 1 `and`, total 12 of 16.** ⚠️ **The per-model instability is the real lesson** — `medium.en`, `small.en` and `distil-large-v3` each flipped between R1's window and R2's. **No single decode should have carried the correction**, which is what the withdrawal now says |
| **384** | ⭐⭐ **THE ROOT-CAUSE STATEMENT IS BETTER THAN THE FIX.** *"The root cause is not the sweep density I blamed — it is that I did not read my own evidence. I captured the frame, named it, committed it, and then asserted four times that it contained no filename."* ⭐ **`M1` was a reading failure, not a capture failure, and the record now says so** |
| **385** | ⛔ **THE FIX ROUND WAS NOT SELF-VERIFIED**, and says so: *"`D-024` holds the gate on any `MAJOR` until it is fixed **and re-reviewed in a fresh round**. This goes back to V21 R1 for R2, exactly as V20's did."* ⭐ **Second consecutive lesson to decline the owner-authorised self-verify route.** ⚠️ **The owner question still stands** — the exception has no numbered decision — **but the practice has now corrected itself twice without one** |
| **386** | ⭐⭐⭐ **THE CORPUS IS COMPLETE: 21 OF 21 LESSONS INGESTED AND INDEPENDENTLY REVIEWED.** V21 is the first lesson to reach `COMPLETE` via a `PASS` on a clean re-review. ⚠️ **Four lessons still carry twelve `MINOR` items** (V17 244–249, V18 264–268, V19 303–304, V20 348) — **the cumulative review is close but not yet warranted (§5)** |

---

## §7 — ADVANCEMENT

```text
LESSON: V21  (FINAL LESSON OF THE COURSE)
DECISION: PASS
CONFIDENCE: HIGH

CRITICAL: 0    MAJOR: 0    MINOR: 0    NOTE: 6  (items 381-386)

R1 ITEM DISPOSITION - ALL FOUR CLOSED:
  365  M1  A-141's false claim      -> CLOSED. Four filenames recorded and
           re-read at 9x off the new tip; four propagation sites corrected;
           mastery-report misdirection removed; the real gap restated intact.
  366      [00:05:21] correction    -> CLOSED. Withdrawn; grammatical error
           conceded; A-133 restated on ground that does not depend on the word.
           R2's fresh 6-decode run: 5 "in" / 1 "and" (total 12 of 16).
  367      PT-050 N3 scope          -> CLOSED. BT §5 corrected from "NONE";
           pre-registration, runner and results JSON all verified UNCHANGED.
  368      Malformed timestamps     -> CLOSED. Pure renames to 01-02-28 /
           01-11-38; all 17 frames valid HH-MM-SS.

REQUIRED ACTIONS: none.

ADVANCEMENT: AUTHORIZED.
V21 STATUS: COMPLETE.
CORPUS STATUS: 21 of 21 ingested and independently reviewed.
FINAL_COURSE_REVIEW.md: NOT YET - one blocker cleared, two remain (§5).
```

---

## §8 — REVIEWER'S OWN DISCLOSURES

1. **Worktree isolation honoured** — `MMM-Agents-v21-review`, branch `review/v21`.
2. **Every fix was checked against source, not against the remediation's description of it.** The
   frame was extracted from `4342a22` and re-cropped; the decode used a **different window and
   stretch factor** from R1 so it could disagree; the "nothing re-run" claim was checked by `git
   diff` rather than accepted.
3. **The merge conflicts** in `COURSE_PROGRESS.md` (both sides rewrote the V21 row) and `LOG.md`
   (both appended) were resolved by taking the R2 row and **keeping both log entries**.
4. **Item numbering.** Items **381–386** allocated against integration at `19e6c2a`, where **356**
   remains the highest; `video/v21` holds 357–364 and R1 holds 365–380. **No collision.**
