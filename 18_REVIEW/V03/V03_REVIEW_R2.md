# V03 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | V03 (`Bootcamp1 Wk2 032512 Part1 (71mins).swf`, SHA-256 `efe256d8…`) |
| Review version | R2 |
| Review date | 2026-08-10 |
| Previous review | `V03_REVIEW_R1.md` — `REVISE` (HIGH), 0 CRITICAL / 0 MAJOR / 3 MINOR |
| Scope of this round | **Remediation verification only.** R1's substantive findings (RULE FIDELITY, CHART RECOGNITION, PROVENANCE, AMBIGUITIES, CONTRADICTIONS, TEACH-BACK, hindsight audit, the full-sweep C-004 re-verification) were adjudicated at R1 and are not re-opened. This round verifies the three MINOR corrections applied in commit `683a12a`, each re-derived from primary data rather than read for plausibility. |
| Reviewer independence | Fresh session; no V03 material and no part of the `683a12a` remediation was authored by this reviewer (D-003 satisfied) |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 1 MINOR.**

**Confidence:** HIGH

**Two of the three minors verify cleanly and close. The third does not.** M1 and M3 are
fully discharged — both were re-derived from the raw data this session and reproduce
exactly, to the last decimal, including every one of the twenty newly committed daily
ranges. M2 was applied to one of the two places the false sentence appears, and **the
place R1 explicitly named — the `COVERAGE` block — still carries the overclaim verbatim**.

This is not a re-litigation of M2's substance: the remediation's *replacement wording* is
correct and independently verified below. It is a placement defect. `V03` therefore stays
short of `COMPLETE` by one sentence.

The V04 gate is unaffected — it was already `OPEN` per D-024 and remains open (0 CRITICAL,
0 MAJOR again this round).

---

## WHAT WAS RE-DERIVED (primary sources, not the student's arithmetic)

| Source | What was done |
|---|---|
| `05_HOMEWORK/V03/data/weekly_bars_2026-08-02.json` | All 30 bars × 4 pairs read raw. Daily ranges, ADR, 3×ADR, swing multiples, block levels, first-cut bars, week-extreme indices, and the 116 open=prev-close transitions all recomputed independently |
| `02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md` | Full marker scan by regex: count, distinct count, monotonicity direction, every adjacent duplicate, largest inter-entry gap, final marker |
| `02_TRANSCRIPTS/V02/V02_TRANSCRIPT.md` | Same scan, to test the remediation's claim that V02's identically-worded line is true as written |
| `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md` | Same scan, to check whether the same class of claim exists a third time |
| `11_CONTRADICTIONS/CONTRADICTIONS.md` | `C-001` record and the V03 evidence section read in full, to test the remediation's stated ground for leaving C-001 unedited |
| `05_HOMEWORK/V03/V03_HOMEWORK.md`, `07_MASTERY_REPORTS/V03_MASTERY_REPORT.md`, `18_REVIEW/REVIEW_INDEX.md`, `00_SYSTEM/COURSE_PROGRESS.md` | Read at the edited sections; whole-repo grep for surviving pre-correction figures |
| `scripts/validate_project.py` | Re-run: **97 passed, 1 warning, 0 failures** (the single warning is `V04: 27 screenshots but no INDEX.md` — a live V04 session's in-progress work, not a V03 defect) |

---

## CRITICAL FINDINGS

**None.**

## MAJOR FINDINGS

**None.**

## MINOR FINDINGS

| # | Finding | Error code | Evidence | Impact / required fix |
|---|---|---|---|---|
| M2′ | **The M2 correction was applied to the wrong one of the two places the false claim appears — the `COVERAGE` block still reads *"timestamps strictly monotonic, no duplicates"*.** The sentence occurs twice in `V03_TRANSCRIPT.md`: once in the `COVERAGE` fenced block (lines 18–25) and once in the `PROVENANCE AND VERIFICATION` I-008 criterion 1 (lines 39–46). The remediation corrected the second and left the first untouched. R1's M2 named the first explicitly (*"`COVERAGE` states…"*) and required correction 2 read *"In `V03_TRANSCRIPT.md` **COVERAGE**: replace…"*. The claim is false in exactly the way R1 charged: three same-second adjacent duplicate markers exist, re-confirmed this session. | E20 (carried, not new) | `02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md` lines 23–24, still `timestamps strictly / monotonic, no duplicates.` The file now **contradicts itself**: line 24 asserts no duplicates, line 40–43 enumerates three. `REVIEW_INDEX.md` item 19 records the target as `V03_TRANSCRIPT.md` COVERAGE and reports it applied there; it was not | Replace lines 23–24 of the `COVERAGE` block with the true property (non-decreasing; 1,230 entries, 1,227 distinct; three benign same-second adjacent pairs). No other change needed — the corrected wording at lines 40–46 is accurate and stays. Update `REVIEW_INDEX.md` item 19's status text, which currently overstates what was applied |

---

## M1 — ADR REPRODUCIBILITY — **VERIFIED, CLOSED**

Three questions were put to the raw data.

**1. Does 21:00 UTC actually produce clean 6-bar splits?** **Yes, and it is the only
convention that can.** The dataset is 30 consecutive 4h bars opening Sun 02 Aug 21:00 UTC
(the committed per-pair bar tables independently confirm bars 0, 6, 12, 18, 24 each start
at 21:00). 30 ÷ 6 = 5 exactly, and the split aligns to bar 0. Any other 4h-aligned
boundary leaves a partial first and last day — so the file's stronger claim, *"no other
convention divides this dataset into five whole days"*, is not rhetoric; it is true within
the only class of conventions a 4h series admits. Bar continuity re-verified as a
precondition: **116 of 116** within-week open=prev-close transitions exact across all four
pairs, zero breaks.

**2. Do the ADR values re-derive from the 20 committed ranges?** **Yes — all twenty, exact.**
Recomputed as `max(high of six bars) − min(low of six bars)` per day:

| Pair | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | ADR computed | ADR committed |
|---|---|---|---|---|---|---|---|
| EURUSD | 58.5 | 31.9 | 34.2 | 44.9 | 63.1 | 46.52 | **46.5** ✅ |
| GBPUSD | 88.8 | 37.1 | 47.1 | 31.0 | 74.6 | 55.72 | **55.7** ✅ |
| USDJPY | 265.7 | 81.9 | 56.8 | 99.6 | 190.6 | 138.92 | **138.9** ✅ |
| USDCHF | 60.0 | 26.3 | 37.7 | 75.5 | 72.7 | 54.44 | **54.4** ✅ |

Every one of the twenty ranges matches the committed table to the tenth of a pip. The
derived rows follow: 3×ADR 139.6 / 167.2 / 416.8 / 163.3 ✅, multiples 1.730 / 1.637 /
2.407 / 1.477 → **1.73 / 1.64 / 2.41 / 1.48** as committed ✅.

**3. Does "0 of 4 reached 3×ADR" still hold?** **Yes, with margin.** The largest multiple
is USDJPY at 2.41× — not a near miss at the boundary, and the same conclusion the
superseded figures produced (1.71 / 1.66 / 2.26 / 1.42, re-checked here for the correction
note's accuracy). R1's finding that the conclusion is robust across conventions survives
the recomputation.

**Assessment.** The remediation did the harder and more honest of the two available
things: rather than reverse-engineer a convention that would reproduce the old numbers, it
declared the original unreconstructable, recomputed under a stated convention, committed
every input, and retained the superseded figures in an in-file correction note. The
E19 defect — *a number bearing on `C-001` that is not re-derivable* — is fully cured:
a reader with the JSON and the stated convention now reaches all four ADR figures by
inspection. **Open item 18 closes.**

## M2 — TRANSCRIPT DUPLICATE CLAIM — **WORDING VERIFIED; PLACEMENT DEFECTIVE**

**The replacement wording is exactly right.** Every component re-derived by independent
regex scan of `V03_TRANSCRIPT.md`:

| Claim in the corrected line | Reviewer measurement |
|---|---|
| 1,230 timestamps | **1,230** ✅ |
| 1,227 distinct | **1,227** ✅ |
| Non-decreasing throughout, never decreasing | **Zero decreasing transitions** ✅ |
| Three benign same-second adjacent pairs | **Exactly three** ✅ |
| At `[00:35:21]`, `[01:00:13]`, `[01:04:30]` | **Identical, all three** ✅ |
| Largest gap 13 s | **13 s, at `[01:09:02]`** ✅ (the cited marker is right too) |
| Final entry `[01:10:39]` | **`[01:10:39]`** ✅ |

**But the false sentence still stands where R1 charged it.** `COVERAGE` (lines 18–25)
continues to read *"timestamps strictly / monotonic, no duplicates."* The corrected text
sits fifteen lines below it, so the file now asserts both propositions. Of the two
locations, `COVERAGE` is the more load-bearing: it is the fenced status block a reader or
a downstream session consults first, and it is the one R1 quoted. E20 is not discharged —
see M2′ above.

The seriousness is bounded and worth stating plainly: this is a stale duplicate of a
sentence whose corrected form is present, verified, and adjacent. It misleads no
conclusion. It is `MINOR` under §8 and stays `MINOR` — §8's instruction not to inflate a
minor to hold a lesson applies, and the gate stays open accordingly. But §9's `PASS`
criterion 14 asks that remaining issues not corrupt downstream learning, and a
verification block that contradicts itself fourteen lines later is precisely the artifact
class this project has spent three lessons cleaning up. It gets fixed before `COMPLETE`.

**The V02 cross-check was independently re-tested and the remediation is correct.**
`V02_TRANSCRIPT.md` line 37 carries the identical wording. Scanned this session:
**1,026 markers, 1,026 distinct, zero decreasing transitions.** Strictly monotonic with no
duplicates is **true as written** for V02. Leaving it alone was right, and the
verification behind that call was real, not an assumption inherited from the wording's
similarity.

One observation the remediation did not reach, offered as a note rather than a finding:
`V01_TRANSCRIPT.md` has **974 markers, 969 distinct** — five same-second pairs — but its
`COVERAGE` block makes no monotonicity claim at all, so nothing there is false. The
class-wide sweep comes out clean at two of three files, with V03 the only offender. See N2.

## M3 — DURATION SCOPING — **VERIFIED, CLOSED**

**The scoping is factually correct.** Every element re-derived from the raw OHLC:

| Pair | Block low | First bar cutting it | Week-low bar | Week-high bar | Low→high | Anchor formed? |
|---|---|---|---|---|---|---|
| EURUSD | 1.15269 | **bar 2** | bar 4 | bar 27 | 92 h = 3.83 d | **Yes** — low forms after the cut ✅ |
| GBPUSD | 1.34639 | **bar 2** | bar 5 | bar 28 | 92 h = 3.83 d | **Yes** — low forms after the cut ✅ |
| USDJPY | 155.228 | **none** (`cut_lo` = 0 bars) | **bar 0** | bar 24 | 96 h = 4.00 d | **No** ✅ |
| USDCHF | 0.80552 | **none** (`cut_lo` = 0 bars) | **bar 0** | bar 22 | 88 h = 3.67 d | **No** ✅ |

In USDJPY and USDCHF the block low *is* the week low *is* bar 0's low — the block's lower
boundary is never taken out at any point in the week, so no stop hunt occurs and no anchor
point exists for a run to be measured *from*. Their low→high spans therefore measure
open-to-high of a trending week, exactly as the rescoped text states. The supported sample
is **2 of 4**, both at 3.8 days, both still exceeding the taught 2.5–3 day window — so
the direction of the finding is unchanged and the correction costs the student nothing
except an overclaim. This also stays consistent with §2.4, which rejected the same two
pairs as pattern instances on the same ground; R1's charge was that §2.5 had drifted from
§2.4, and the drift is now closed.

**Propagation verified at all four named sites, plus a fifth:**

| Site | State |
|---|---|
| `V03_HOMEWORK.md` §2.5 Finding A | ✅ Per-pair *"does this measure the taught object?"* column; explicit *"supported by 2 of 4, not 4 of 4"*; the two excluded pairs left unbolded on the record rather than deleted (right call — they are still measurements) |
| `V03_HOMEWORK.md` §4 point 3 | ✅ *"3.8 days in the **2 of 4** pairs where an anchor point actually formed"*, cross-referencing §2.5 |
| `V03_MASTERY_REPORT.md` §D (Sequence) | ✅ Line 143 rescoped |
| `V03_MASTERY_REPORT.md` §2 | ✅ Lines 265–269 rescoped, with the excluded pairs' 4.0 / 3.7 days retained and explained |
| Whole-repo sweep for surviving pre-correction figures | ✅ Clean. Grep for `3.7–4.0`, `1.42×`, `2.26×`, `148.2`, `all four exceed` finds no live assertion. Surviving `4 of 4` strings are all different claims (*"the signature fired 4 of 4"*, *"cut a side in 4 of 4"*, *"time clause operative in 4 of 4"*) — each checked and each correct in its own terms |

The one residue is `LOG.md` lines 1746–1747, which carry the original unscoped figures.
That is **correct and must not be edited**: `LOG.md` is an append-only chronological
journal, the superseding remediation entry appears at lines 1859/1892, and rewriting a
past log entry to match a later correction would falsify the project's own record. Noted
so a future session does not "fix" it.

**The `C-001` deferral is verified as legitimate.** The remediation declined to edit
`CONTRADICTIONS.md`, on the ground that `C-001` does not yet cite this datum. This
reviewer read the `C-001` record (lines 130–214) and the `V03 EVIDENCE ADDED TO EXISTING
RECORDS` §`C-001` (lines 523–539) in full rather than accepting the claim. The V03
evidence consists entirely of five transcript restatements of the taught window plus the
new exit rule at `[00:36:11]`–`[00:36:16]`; **no homework-measured duration appears
anywhere in the record**, and a whole-file grep for `3.8` / `3.7` / `4.0 days` returns
nothing. The claim is true. (The nearest analogue — the V02 section's *"Chart datum from
V02 homework 11a — recorded, NOT counted as support"* at line 372 — is a different
dataset and does not smuggle the V03 datum in.)

The requirement is therefore precisely as the remediation states it: **the scoping must
travel with the datum whenever it is first cited against `C-001`**, not before. That
standing instruction is committed in two places (homework §2.5 Finding A: *"Any citation
of this datum against `C-001` must carry this 2-of-4 scoping"*; mastery report §2: *"the
homework §2.5 Finding A scoping governs any citation of it"*), which is where a future
session will actually be standing when the obligation bites. Correct handling —
pre-emptively editing `C-001` would have inserted a datum the record does not yet make a
claim about. **Open item 20 closes.**

---

## NOTES (no correction required)

| # | Note |
|---|---|
| N1 | **The remediation changed no conclusion, and this was checked rather than assumed.** Every downstream statement that could have moved under M1's recomputation was re-derived: 0 of 4 reaching 3×ADR holds under the new figures (max 2.41×) and under the superseded ones (max 2.26×); the *"exited on time, not on target in 4 of 4"* reading in §2.5 follows from the target being unreached in all four, which remains true. M3 costs the finding two pairs and no direction. The commit message's *"no conclusion changed"* is accurate. |
| N2 | **The E20 class is now swept across all three transcripts.** V02 asserts strict monotonicity and is genuinely strictly monotonic (1,026 / 1,026). V01 has five same-second pairs (974 / 969) but asserts nothing about monotonicity, so has nothing to correct. V03 is the only file where the claim and the data diverge — and after M2′ is applied, the class is empty project-wide. Worth recording so the next reviewer does not re-run the sweep. |
| N3 | R1's N2 (the ~10:50 *"Easter is Coming"* housekeeping slide, absent from `INDEX.md`) and N3 (`INDEX.md`'s non-marker `[00:02:00]` reference) were offered at the student's discretion and were not folded into `683a12a`. Both remain open at the same non-blocking status R1 gave them; N3 is still parked against the deferred `STUDY_PROTOCOL.md` amendment at the 25% cumulative review. Neither bears on this round's verdict. |
| N4 | R1's N4 (manual-backtest debt, three lessons deep) is untouched by this round and remains `REVIEW_INDEX.md` open item 21. It is not a V03 remediation item and does not gate `COMPLETE`; it gates the first lesson that supplies a testable rule. |
| N5 | `validate_project.py`'s single warning (`V04: 27 screenshots but no INDEX.md`) belongs to a V04 session active in this working tree at review time, not to V03. V03's own artifacts pass structurally. |

---

## STUDENT MASTERY ASSESSMENT

Unchanged from R1 in every dimension — this round adjudicated no new mastery evidence.
Recorded for continuity:

| Dimension | R1 assessment | R2 |
|---|---|---|
| A. Recall | PASS | Unchanged |
| B. Recognition | PARTIAL | Unchanged |
| C. Discrimination | FAIL (honest) | Unchanged |
| D. Sequence | PARTIAL | Unchanged — the §D rescope is a precision fix, not a grade change |
| E. Exceptions | PASS | Unchanged |
| F. Homework | 11a FIRST-PASS SUCCESS / 11b UNRESOLVED | **Improved** — M1 and M3 were the two precision debts R1 attached to 11a's write-up; both are now discharged |
| G. Manual backtesting | DEFERRED | Unchanged (N4) |
| H. Provenance | PASS | Unchanged |
| I. Ambiguity | PASS | Unchanged |
| J. Contradictions | PASS | Unchanged — and the `C-001` deferral judgement above is a small positive data point for this grade |

---

## REQUIRED CORRECTIONS

1. **M2′** — In `02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md`, `COVERAGE` block, lines 23–24:
   replace *"timestamps strictly / monotonic, no duplicates."* with the true statement
   already established and verified at lines 40–43 — non-decreasing throughout; 1,230
   entries, 1,227 distinct; three benign same-second adjacent pairs at `[00:35:21]`,
   `[01:00:13]`, `[01:04:30]`. Do not alter lines 39–46, which are correct as they stand.
   Then correct `18_REVIEW/REVIEW_INDEX.md` open item 19's status text, which reports the
   fix as applied to `COVERAGE` when it was applied to the I-008 criterion instead.

That is the entire outstanding debt for V03. On its application and verification, V03
reaches `COMPLETE`.

---

## REVIEWER QUESTIONS

None. M2′ is mechanical and needs no student judgement.

---

## ADVANCEMENT DECISION

```text
LESSON: V03
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- none

MAJOR ISSUES:
- none

MINOR ISSUES:
- M2' Transcript COVERAGE block still reads "strictly monotonic, no duplicates"
  (E20, carried from R1 M2 — corrected in the I-008 block only, and the file now
  contradicts itself)

CLOSED THIS ROUND:
- M1 (E19) ADR reproducibility — all 20 daily ranges and all 4 ADR figures
  re-derived exactly from the raw JSON under the stated 21:00-UTC convention;
  0 of 4 reaching 3xADR confirmed with margin. Open item 18 CLOSED.
- M3 (E02) duration scoping — 2-of-4 scope confirmed correct against raw OHLC
  (USDJPY/USDCHF block low never cut, week low at bar 0); propagation verified at
  homework §2.5A and §4, mastery report §2 and §D; C-001 non-citation independently
  confirmed, deferral legitimate. Open item 20 CLOSED.

REQUIRED ACTIONS:
1. Apply M2' — one sentence in V03_TRANSCRIPT.md COVERAGE, plus the REVIEW_INDEX
   item 19 status text. Nothing else.

ADVANCEMENT:
AUTHORIZED — 0 CRITICAL + 0 MAJOR; the V04 gate was already OPEN per D-024 and
remains open. V03 does NOT reach COMPLETE this round: one MINOR is outstanding and
must be applied and verified first.
```
