# V04 — INDEPENDENT REVIEW — R2

| Field | Value |
|---|---|
| Lesson | V04 (`Bootcamp1 Wk2 032512 Part2 (86mins).swf`, SHA-256 `10d8fe7e…fe60fb7c`, 01:25:41) |
| Review version | R2 |
| Review date | 2026-08-11 |
| Previous review | `18_REVIEW/V04/V04_REVIEW_R1.md` — `REVISE`, HIGH, **0 CRITICAL / 0 MAJOR / 7 MINOR / 5 NOTE**; V05 gate `OPEN` under `D-024` |
| Remediation under review | commit `3a13441` — *"fix: V04 R1 remediation (M1-M7 + N1) and DECISIONS.md D-025"*, 15 files, +862/−77 |
| Reviewer independence | Fresh session. This session authored **no** V04 artifact and applied **none** of the R1 corrections (`D-003` satisfied). |
| Scope | Verification of the R1 remediation (`REVIEW_PROTOCOL.md` §4). Dimensions R1 graded on material the remediation did not touch were not re-audited. Every fix was **re-derived from the committed data or the source file**, not read off the diff. |

---

## FINAL DECISION

```text
PASS
```

**Decision:** `PASS` — **0 CRITICAL, 0 MAJOR, 1 MINOR (non-blocking), 3 NOTE.**

**Confidence:** HIGH

**All seven minors, note `N1`, and the owner action are applied, and all nine verify.**
The one item that mattered — `M1`, the only evidence fix in the round — was not merely
reworded: the dataset was re-sliced, and this reviewer reproduced the diagnosis, the
correction, and the corrected figures independently, including recomputing the old
committed data to confirm the defect was real and is now gone.

The single residual finding is a one-clause inaccuracy in a *justification sentence* written
during the remediation itself. It changes no number, no table and no conclusion — the output
it justifies was independently recomputed and **is** unchanged. Under `REVIEW_PROTOCOL.md`
§9 criterion 14 (*"remaining issues are minor and do not corrupt downstream learning"*) and
the precedent set at `V02_REVIEW_R3.md`, it does not withhold a `PASS`, and manufacturing an
R3 for it would be the artificial difficulty §16 forbids. It is carried to `REVIEW_INDEX.md`
for correction the next time the file is touched.

**V04 is `COMPLETE`.**

---

## 0. WORKING-TREE INTEGRITY — CHECKED FIRST

```text
HEAD                3a13441  fix: V04 R1 remediation (M1-M7 + N1) and DECISIONS.md D-025
Parent              a37f31d  feat: V05 transcript verified and adopted (I-008); Q-005 …
Working tree        clean except 05_HOMEWORK/V02/measure_usdchf_week.py (untracked)
validate_project.py 97 passed, 0 warnings, 0 failures   (re-run this session)
```

A **concurrent V05 session is active in this same working tree.** The remediation commit
touched **no** V05 file and left the untracked `05_HOMEWORK/V02/measure_usdchf_week.py`
alone, as its message claims — verified against `git show --stat`. The commit's own
`validate_project.py` line reports 1 warning ("V05 transcript absent"); it now reports 0,
because the V05 session has since committed that transcript. That is a change in the
environment, not a discrepancy in the fix.

---

## 1. `M1` (`E19`) — THE USDCHF 15-MINUTE RE-SLICE — **VERIFIED, INDEPENDENTLY AND IN BOTH DIRECTIONS**

This is the only evidence fix in the round and it received the bulk of this review. The
question asked was not "does the file now say 476" but **"does 476 fall out of the data"**,
and — separately — **"was the diagnosis actually right"**. Both were answered by
recomputation in this session, with a script written here, before the homework prose was
read.

### 1.1 The defect was real, and it is exactly what R1 said it was

Recomputed from the **parent commit's** JSON (`git show 3a13441^:…`):

| Test on the pre-fix data | Result |
|---|---|
| 15m discontinuities in USDCHF's committed "week" | **exactly one: `m[3] → m[4]`, −12.7 pips** |
| 15m discontinuities in the other three pairs | **zero** |
| Fixed-16 reconstruction of USDCHF 4h bar 0 | misses **open by 28.1 pips, high by 12.8** |
| `aggregate(m[4:16])` vs 4h bar 0 | `[0.80552, 0.80742, 0.80552, 0.80685]` — **equal on all four fields** |
| Whole-file 4h ↔ 15m total, pre-fix | **474/480**, 115/120 bars |

An open cannot differ by hover-dwell latency. The pre-fix attribution to ±0.4 pip harvest
noise was wrong, and R1's diagnosis — a **partial week-open 4h bar of twelve 15m bars**, so
the fixed-16 slice began four bars early and swallowed the weekend gap — is confirmed
mechanically.

### 1.2 The correction is exact, and it is the minimal one

Diffing the two committed JSONs field by field:

- **Only USDCHF changed.** EURUSD, GBPUSD and USDJPY's arrays are byte-identical.
- `bars_15m_week` **480 → 476**, and the new array is **exactly `old[4:]`** — the four
  leading previous-week bars dropped, nothing else altered, nothing re-harvested.
- `offset_in_harvest` **261 → 265**; `j_hi_15m` **363 → 359**; `j_lo_15m` **4 → 0** — each
  shifted by exactly 4, i.e. re-indexed rather than recomputed from a new source.
- New per-pair `bars_15m_in_4h_bar_0` = **16 / 16 / 16 / 12**.
- **The 4-hour arrays are untouched in all four pairs.**

**Nothing was missing from the tail**, as claimed: `476 = 12 + 29 × 16` consumes the array
exactly, and 4h bar 29 reconstructs cleanly for USDCHF.

### 1.3 The corrected figures reproduce

Recomputed here with an independently written aggregator, honouring `bars_15m_in_4h_bar_0`:

| Pair | first 4h bar | bars | fields | in-week 15m breaks | residuals |
|---|---|---|---|---|---|
| EURUSD | 16 × 15m | 30/30 | 120/120 | 0 | — |
| GBPUSD | 16 × 15m | 28/30 | 118/120 | 0 | bar 22 **low** 0.1 pip, bar 29 **high** 0.1 pip |
| USDJPY | 16 × 15m | 30/30 | 120/120 | 0 | — |
| USDCHF | **12 × 15m** | **28/30** | **118/120** | **0** | bar 27 **low** 0.3 pip, bar 28 **high** 0.1 pip |
| **Total** | | **116/120** | **476/480** | **0** | all ≤ 0.3 pip, **all in highs or lows** |

**476/480 confirmed. USDCHF 27/30 → 28/30 confirmed. Zero in-week discontinuities in all
four pairs confirmed.** The claim that all four residuals are now ≤ 0.3 pip and none touches
an open or a close is true, which is what makes the ±0.4 pip dwell attribution legitimate
*now* and illegitimate *before*.

The committed `scripts/verify_reconstruction.py` was also executed as shipped: it prints the
table above and **exits 0**. Its window generator, its `bars_15m_in_4h_bar_0` assertion and
its discontinuity test were read line by line and are not tautological — it asserts
`len(m) == n0 + 29 × 16` and recomputes the aggregation rather than reading a stored figure.

### 1.4 An independent cross-check the remediation did not claim

The re-indexed 15m extreme pointers were mapped back onto the 4h bar grid through the new
partial-first-bar arithmetic, for all four pairs:

| Pair | `j_hi_15m` → 4h bar | 4h week-high bar | `j_lo_15m` → 4h bar | 4h week-low bar | values equal |
|---|---|---|---|---|---|
| EURUSD | 447 → 27 | 27 | 74 → 4 | 4 | ✅ |
| GBPUSD | 449 → 28 | 28 | 84 → 5 | 5 | ✅ |
| USDJPY | 399 → 24 | 24 | 15 → 0 | 0 | ✅ |
| USDCHF | **359 → 22** | **22** | **0 → 0** | **0** | ✅ |

Every 15m extreme lands in the 4h bar that holds the same extreme, at an identical price.
Under the *old* USDCHF indices this arithmetic does not close; under the new ones it does.
**The re-index is right, not merely consistent.**

### 1.5 The key conclusion still holds — checked on the 4-hour data, not taken on trust

- USDCHF's week low is at **4h bar 0** (`0.80552`), the week-open bar, where no anchor can
  have formed. USDJPY's likewise. **Both exclusions are 4-hour facts and the 15m re-slice
  cannot reach them.**
- The 4h series is continuous **116/116** across all four pairs, zero breaks — recomputed.
- **EURUSD and GBPUSD remain the only two admissible pairs**, week high at bars 27 and 28,
  week low at bars 4 and 5 → **23 bars × 4 h = 92 h = 3.833 days** on both. The
  `2-of-4 / 3.83-day` result is unchanged, and it is unchanged for the reason the homework
  gives.

**`M1` is discharged.** The fix is an evidence fix, it is minimal, it is documented in place
with the misdiagnosis named rather than quietly replaced, and the limitation is written into
`scripts/README.md` as a warning to the session that inherits the harvester.

---

## 2. THE REMAINING SEVEN ITEMS

### `M2` (`E01`) — **VERIFIED against the transcript body, not against the diff**

| Restored fragment | Transcript body | Marker |
|---|---|---|
| *"There was a bunch of money **set up** here and they had to go after it."* | line 3047, **exact** | `[00:50:34]` ✅ |
| *"One, two, three, swipes."* / *"**Gaby** a nice ugly **look in** kindergarten **ma'am** there."* | lines 4138 / 4142, **exact** | `[01:10:33]` / `[01:10:36]` ✅ |

Both are now the adopted transcript's literal wording, both carry markers that resolve, and
the paragraph now states which side of the comparison it quotes — R1 offered restoration
*or* re-attribution and the stronger of the two options was taken. The correction is
disclosed in place rather than performed silently, which is the house standard.

### `M3` (`E20`/`E11`) — **VERIFIED; the new IDs are the right ones**

`A-031` is *"blood in the water" / "bloodline"* and `A-030` is *"brinks shadow" / "shadow
box"* in the register as it stands — the correct subjects. `A-037` (halving the Asian range)
and `A-038` (the guest's ADR lookback window) are confirmed to be the wrong subjects, as R1
charged. Every surviving `A-037` / `A-038` reference in the V04 artifacts was re-checked and
each is a legitimate citation of those actual records.

### `M4` (`E20`) — **VERIFIED by counting**

`04_SCREENSHOTS/V04/` holds **27** PNGs; source notes now say 27 and name `INDEX.md`
explicitly. `05_HOMEWORK/V04/scripts/` holds **3** scripts; FILES PRODUCED now says 3 and
`INDEX.md`. The only surviving `VISUAL_INDEX` string in the V04 artifacts is inside the
remediation log describing the fix.

### `M5` (`E20`) — **VERIFIED, and the judgement call was the right one**

R1 offered two remedies. The session took the second — restate over committed data, mark the
harvest-wide figures `UNREPRODUCED` — and I was asked to judge that choice rather than just
confirm it was executed.

**It is the correct choice, and the alternative would have been worse.** The 569/549/20
figures were computed on ~144-bar harvests held in session memory and never written to disk.
Re-harvesting today cannot recreate them: the "current bar" has moved and feed values can be
revised. Committing a *fresh* harvest under those numbers would attach data to claims that
were never computed on it — provenance fabrication, the `E19`/`E20` failure this project
exists to avoid, and materially worse than an honest gap. The remediation says exactly this,
in the file, and does not overstate it: the figures are **not withdrawn**, nothing downstream
depends on them, their only job was locating the week boundary, and that boundary is
independently established by the committed data (116/116 in-week continuity, which I
recomputed) and by agreement with V03's separate dataset. The caveat also appears in §1.3
"What is NOT validated", so a reader who skips validation 1 still meets it.

The reproducible half is real: **116 transitions, 116 continuous, zero breaks**, recomputed
here.

### `M6` (`E20`) — **VERIFIED, and the framing is accurate and appropriately conservative**

I opened both frames myself and magnified the lower third before reading the new text.

- Frame 21 (`01-04-10`, GBPJPY M15) and frame 22 (`01-08-40`, AUDCAD M15) each carry a
  sub-panel across the lower third titled **`Traders Dynamic Index Visual`**, followed by a
  six-value numeric readout. Green, red and yellow lines and pale/cyan volatility bands are
  rendered in both. The `INDEX.md` descriptions match what is on the frames, colour for
  colour.
- **The six-value readout is genuinely at the edge of legibility.** At 8× magnification the
  digit shapes resolve enough to guess and not enough to *read*; a transcription would be a
  reconstruction. **Declining to transcribe it was the right call**, and saying so in the
  index — rather than silently omitting it — is better than either transcribing a guess or
  pretending nothing is there.
- The scoping is correct on the merits, not just verbally. "Displayed, not taught" is
  accurate: no inputs, periods, band construction, geometry or decision rule is recoverable
  from either frame. `A-039` gains two evidence rows tagged **`GUEST` / DESCRIPTIVE ONLY**
  with an explicit statement that they do **not** narrow the record — which is precisely what
  `D-025` permits and forbids.
- One improvement beyond what R1 asked for, and it is a good one: `A-039`'s line *"the
  example chart carries no TDI panel"* is now scoped to **the instructor's own Segment-A
  chart**. Unscoped, that line would have read as contradicted by the very frames just added.
  The remediation saw that and fixed it.
- The descriptive gain is stated at the right weight: the frames settle that `TDI` expands to
  **Traders Dynamic Index**, which no line of V01–V04 audio states — terminology only.

### `M7` (`E20`) — **VERIFIED by counting against the standard**

`MASTERY_STANDARD.md` §"Quality-control checklist" carries **19** boxes. The new section
accounts for all 19: **13 checked + 2 `DEFERRED` + 4 UNCHECKED = 19**, and the four unchecked
are the four R1 named. The declarations are true against the repository: all four
`09_CHART_EXAMPLES/` subdirectories hold only `.gitkeep`, and `08_CONCEPT_LIBRARY/
CONCEPT_INDEX.md` reads `CONCEPTS: 0`.

Two things raise this above box-ticking. It **refuses to excuse the concept-library box** by
pointing at `A-039` — the three example boxes are genuinely blocked, the concept library is
not, and the section says so in those words. And the two `DEFERRED` boxes are argued rather
than asserted: *"failed valid setups are recorded"* is not ticked, because with no backtest
performed there are no setups, and ticking it would assert compliance with an untested
condition.

### `N1` — **VERIFIED, and it follows the `D-019` pattern exactly**

Checked against `D-019`'s own worked example (V01 dimension F, `NOT APPLICABLE` → `DEFERRED`
for H4/H5) rather than against the label alone:

| `D-019` requirement | V04 B and C |
|---|---|
| Subject matter exists and work is performable in principle | Yes — stated explicitly, `NOT APPLICABLE` **declined** |
| Blocker is a missing prerequisite, not a failure | `A-039` — condition (c)'s indicator never taught |
| Item **stays open**, carried in `REVIEW_INDEX.md` until the blocker clears | Yes — new open-items row, alongside dimension G |
| Grant is available for the dimension | `D-019`: `DEFERRED` may be granted for **any** dimension |

The original `PARTIAL` and `FAIL` prose is retained **verbatim** beneath the new labels —
diffed, not eyeballed: not one word of the body text changed. The self-criticism R1 upheld is
still on the page. The header note gives the mechanical reason (a `FAIL` whose cause sits in
the source can never be cleared by studying harder — the `D-018` trap arriving for B and C),
and the summary block's *"Dimensions B, C and G are all sub-`PASS`"* was updated to
`DEFERRED` for consistency. This is the same shape as the V01 fix, applied for the same
reason.

---

## 3. `D-025` — **PROPERLY RECORDED, WITH ALL FOUR CROSS-REFERENCES LIVE**

Read in full against R1's ruling text.

**Substance:** faithful. Normative/descriptive as the operative distinction; both extremes
rejected with the reasons R1 gave; the classification table carried over with V04's own
examples on each side; all four binding consequences present and not softened — a guest
statement can never resolve an ambiguity or contradiction; guest/instructor divergence is a
**corpus-hygiene** record; **speaker tagging mandatory from V04 forward**; identifying a guest
is provenance, not evidence. `Status: ACTIVE`. Alternatives-considered and Evidence fields
are populated to the standard of the surrounding entries.

**Structure:** it **refines** `D-008` and says so, with `D-008` explicitly *not* superseded
and the reason stated crisply — D-008 ranks the course against the agent; D-025 ranks
speakers inside the course, which D-008 could not contemplate because no lesson before V04
had more than one voice.

**Cross-references — all four present and pointing the right way:**

| Location | State |
|---|---|
| `DECISIONS.md` D-008 | Forward-pointer block added, "meaning unchanged, not superseded" ✅ |
| `DECISIONS.md` D-004 pointer block | Added under "Added 2026-08-11" — an open gate is permission to begin, **not** permission to skip speaker tagging ✅ |
| `COURSE_PROGRESS.md` PROGRESSION RULE | *"An open gate does not waive `D-025`"* ✅ |
| `REVIEW_PROTOCOL.md` §2 | Reviewer instruction to audit **both halves** — no guest statement admitted as a rule, **and** descriptive guest evidence not over-excluded ✅ |

That last one is the best of the four: R1's ruling has a symmetric failure mode, and the
protocol edit makes future reviewers check the *over-exclusion* direction too, which is the
direction a cautious session is most likely to get wrong.

**`C-005`** is updated to record the ruling, its *"Required to resolve"* field discharged,
and the record correctly **stays open as corpus hygiene** — which is what the ruling itself
says the right category is. **`REVIEW_INDEX` open item 22 is `CLOSED`**; items 25–32 are
marked **APPLIED — PENDING VERIFICATION at R2**, which this round now discharges.

---

## 4. MINOR FINDING

### `m1` — `E20` — the "§3.3 windows are identical" justification is true for one window and false for the other

`05_HOMEWORK/V04/V04_HOMEWORK.md` §1.2 (M1 correction block) and
`07_MASTERY_REPORTS/V04_MASTERY_REPORT.md` §"Was any conclusion affected?", same sentence in
both:

> *"The §3.3 swing-descriptor windows are unchanged: the extreme's index and the 44-bar
> window shifted together by exactly four bars, so the bars examined are the same bars.
> Recomputed and confirmed identical."*

**The conclusion is correct. The stated reason is correct for the HIGH window and wrong for
the LOW window**, and I checked by extracting both windows from both committed datasets:

| USDCHF window | Pre-fix | Post-fix | Same bars? |
|---|---|---|---|
| At the week **high** (`j_hi` 363 → 359) | 44 bars | 44 bars | **Yes — bar for bar identical** |
| At the week **low** (`j_lo` 4 → 0) | **5 bars** (`m[0:5]`) | **1 bar** (`m[0:1]`) | **No** |

The low window was **clipped at the head of the array in both datasets**, so it could not
"shift together" with anything: pre-fix it held the extreme plus four bars that we now know
were *previous-week* bars; post-fix it holds the extreme alone. Those are different bars, and
four of the old ones did not belong to the week at all.

**Why this is MINOR and non-blocking, stated carefully:**

- **The output is genuinely unchanged**, which I verified rather than assumed: the USDCHF
  low-side descriptors are **1 / 1 / 1 / 1** across all four tolerances on *both* datasets,
  because the extreme is the only qualifying swing low in either window. The §3.3 table is
  correct as printed, and its note *"extreme is the week-open bar"* is correct.
- **Its direction is safe.** The corrected window is the *more* honest one — it no longer
  admits four out-of-week bars into a within-week descriptor.
- **Nothing downstream reads the justification**, only the table.
- It is a residue of the exact pattern R1 named at `N5`: *"the checked artifact is reliable;
  the paragraph describing the check is not, because it is the one part nothing recomputes."*
  The remediation quoted that sentence approvingly — and then produced one more instance of
  it, in a claim that recomputation would have caught.

**Required, whenever either file is next touched (not a re-review trigger):** replace the
mechanism clause with what is true — *"the high-side window is bar-for-bar identical; the
low-side window was clipped at the array head in both datasets and now correctly excludes the
four previous-week bars it previously contained. Both descriptor rows are unchanged
(1/1/1/1), recomputed."*

Carried to `REVIEW_INDEX.md` as a new open item. Under `REVIEW_PROTOCOL.md` §9 criterion 14
and the `V02_REVIEW_R3.md` precedent (`PASS` with two non-blocking documentation-precision
minors), this does not withhold the `PASS`.

---

## 5. NOTES

### `N1` — the remediation's self-report is accurate, which is itself the finding

Nine claims in the commit message were spot-checked against the repository rather than
accepted: only USDCHF's array changed; the 4h data is untouched; `476 = 12 + 29 × 16`; nothing
missing from the tail; V05 files untouched; the untracked V02 script untouched; 27 frames;
3 scripts; 19 QC boxes. **All nine hold.** No claim in the message overstates what was done —
including the uncomfortable ones (*"The test caught it; I misdiagnosed it"*), which are
carried into the mastery report rather than confined to a commit nobody re-reads. That is the
behaviour `REMEDIATION_PROTOCOL.md` asks for and it is rarer than it should be.

### `N2` — `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`'s STATUS block is stale, and it is **not** V04's to fix

The block reads `LESSONS STUDIED: 3 (… V03 studied, not yet reviewed)`. V03 is now `COMPLETE`
at R3 and V04 has been studied. This is the staleness class `REVIEW_INDEX` open item 14
tracks, it predates this remediation, and V04 correctly declared the concept-library box
**UNCHECKED** rather than touching the file. **Not charged against V04.** It belongs with the
concept-library debt at `CUMULATIVE_25.md`, and it is one more argument for the mechanical
staleness check open item 14 already proposes.

### `N3` — what R2 did not re-audit, stated so nobody assumes otherwise

Per `REVIEW_PROTOCOL.md` §4 this round verified the remediation, not the lesson. The 487
citations, the 320 quoted fragments, the two-speaker finding, the full-population `RULES.md`
fabrication audit, the hindsight and machine-rule firewall audits and the dimension grades on
untouched material were **verified at R1 and were not re-run here** — except where a fix
touched them, in which case they were. The homework figures *were* re-run in full, because
`M1` touched the dataset they come from.

---

## 6. DIMENSION AUDIT — DELTA ONLY

| Dim | R1 | R2 | Basis |
|---|---|---|---|
| B Recognition | `PARTIAL` → re-label ordered | **`DEFERRED` — accepted** | `D-019` satisfied on all four tests; original text retained verbatim; carried open |
| C Discrimination | `FAIL` → re-label ordered | **`DEFERRED` — accepted** | Same; `NOT APPLICABLE` correctly declined |
| F Homework | `UPHELD` subject to M1, M5 | **`UPHELD`, conditions discharged** | M1 re-derived and reproduced; M5 rescoped honestly. `476/480` now stands on both cross-checks |
| A, D, E, G, H, I, J | — | **unchanged** | Not re-audited (§4); nothing in the remediation touched their basis |

**Overall student disposition:** `REVIEW REQUIRED` was the right submission at the time and
the remediation is complete. The lesson's own limits are unchanged and correctly labelled:
B, C and G stay `DEFERRED` behind `A-039`, and V04 reaching `COMPLETE` is **not** a claim that
the TDI-dependent entry rule has been mastered — it is a claim that V04 is accurately and
honestly recorded, including about what it cannot do.

---

## 7. REQUIRED ACTIONS

**None blocking.** One deferred documentation correction:

1. **`m1`** — fix the "§3.3 windows are identical" mechanism clause in
   `V04_HOMEWORK.md` §1.2 and `V04_MASTERY_REPORT.md`, whenever either file is next edited.
   Do **not** open an R3 for it.

Carry forward, unchanged and not V04's debt: `A-039` (TDI required, untaught, condition (c)
must not be dropped), the four-lesson manual-backtest debt, dimensions B/C/G `DEFERRED`, the
concept-library and chart-example gap, V03's open items 18–20, and V01's dimension B deferral.

---

## EXECUTIVE SUMMARY

```text
LESSON: V04
DECISION: PASS
CONFIDENCE: HIGH

CRITICAL ISSUES: 0
MAJOR ISSUES:    0
MINOR ISSUES:    1  (m1 E20 — non-blocking; see §4)
NOTES:           3

REMEDIATION VERIFIED — 9 of 9:
  M1  USDCHF 15m re-slice        VERIFIED — re-derived from data, both directions
  M2  two smoothed quotes        VERIFIED against the transcript body
  M3  A-031 / A-030 repointed    VERIFIED against the register
  M4  27 frames / INDEX.md       VERIFIED by counting
  M5  validation 1 rescoped      VERIFIED — and the honest-caveat route was correct
  M6  TDI panel recorded         VERIFIED — frames opened; scoping accurate, conservative
  M7  QC checklist declared      VERIFIED — 13 + 2 + 4 = 19 boxes
  N1  B and C -> DEFERRED        VERIFIED — follows D-019's V01 F/G pattern exactly
  D-025 recorded                 VERIFIED — faithful; all 4 cross-references live

KEY RE-DERIVATIONS THIS ROUND:
  4h <-> 15m reconstruction      476/480 fields, 116/120 bars      CONFIRMED
  In-week 15m discontinuities    0 in all four pairs               CONFIRMED
  In-week 4h continuity          116/116                           CONFIRMED
  USDCHF week low                4h bar 0 -> exclusion stands      CONFIRMED
  2-of-4 / 3.83 days             EURUSD + GBPUSD, 23 bars each     CONFIRMED
  15m extremes -> 4h extreme bar all 4 pairs, exact prices         CONFIRMED

ADVANCEMENT:
V04 STATUS: COMPLETE  (D-004 — reviewer PASS)
V05 GATE:   OPEN, and D-025 applies before V05 notes are written
```
