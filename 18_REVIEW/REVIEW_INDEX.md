# REVIEW INDEX

Master record of every independent review decision, and the project's running
error statistics.

Maintained by the Reviewer Agent. Append-only for decisions — a superseded decision
stays visible with its round number.

---

## STATUS

```text
LESSONS REVIEWED: 4
PASSED:           4  (V01, V02, V03, V04 — V04 PASS at R2, COMPLETE)
IN REMEDIATION:   0
AWAITING REVIEW:  0
```

V01 reviewed 2026-08-10 (R1): `REVISE`, confidence HIGH. 0 critical, 2 major.
V01 re-reviewed 2026-08-10 (R2): `REVISE`, confidence HIGH. 0 critical, 1 major.
V01 re-reviewed 2026-08-10 (R3): **`PASS`**, confidence HIGH. 0 critical, 0 major.
All 15 of R2's required actions verified applied against the source, not against the
commit message. R2 finding N1 (the only open MAJOR) is closed. **The V02 gate is now
open** — D-004 satisfied.

V02 reviewed 2026-08-10 (R1): **`REVISE`**, confidence HIGH. 0 critical, 1 major,
5 minor. Reviewed by a genuinely independent session (D-003 satisfied). The source
notes, interpretation, ambiguity and contradiction work are the strongest evidence
artifacts in the repository to date, and V01's recurring `E11` citation defect does
**not** recur. The single MAJOR is in the homework: the 11a markup contradicts the
chart it cites, and produces a false confirmation that a real week held away from its
Monday high for three days — bearing directly on `C-001`. **V03 remains gated** until
V02 receives reviewer `PASS`.

V02 re-reviewed 2026-08-10 (R2): **`REVISE`**, confidence HIGH. 0 critical, **0 major**,
3 minor — **plus 1 MAJOR process finding: the D-004 V03 gate is being breached.** **R1's MAJOR is CLOSED**, verified by re-measuring the committed PNG in the R2
session rather than by reading the new pipeline's self-description: every price, day,
direction and hour in the corrected markup reproduces to within 0.2 pip, as does the
72-hour `C-001` result. The `C-001` non-resolution is correct in both directions — the
datum is recorded and fenced, and no day-count value is committed anywhere. R2 returns
`REVISE` because the remediation deliberately escalated one item *to* R2 (the `PFH`/`PFL`
count R1 had signed off on, now adjudicated: both abbreviations occur **zero** times), and
because the corrected §1.1 measurement misplaces one bar at the Fri 31 Jul → Sun 2 Aug
boundary and rests on a *"self-validating on all six boundaries"* claim that does not
hold — continuity was tested at a weekend boundary, where it should not be expected. **No
conclusion in the homework changes**; §1.1 is charged only because two files advertise it
as the reusable pipeline for the dimension-G backtest.

**The V03 gate did NOT hold.** It had held at review start — `git status` showed no V03
artifact — and by the time R2 staged its files the tree contained an in-progress V03
student pass (`02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md`, 1,230 entries, marked COMPLETE;
`04_SCREENSHOTS/V03/` and `05_HOMEWORK/V03/` created; `QUARANTINE_REGISTER.md` +102 lines
adding `Q-003`, whose own text says it precedes *"writing V03's notes"*), from a session
other than the reviewer's, while `COURSE_PROGRESS.md` reads `V03 GATE: CLOSED` and V02 is
unpassed. **Second occurrence, and unlike R1's it is not moot** — V02 is `REVISE` with
three corrections outstanding, one of them in the measurement pipeline V03's chart work
would inherit. Charged as a **process** MAJOR, deliberately kept out of V02's mastery
counts, and left untouched and unstaged by R2. **V03 remains gated; the pass must stop
until V02 receives `PASS`.**

V02 re-reviewed 2026-08-10 (R3): **`PASS`**, confidence HIGH. 0 critical, 0 major,
2 minor — both non-blocking. **Both of R2's required student corrections are applied and
both were re-derived from the source in the R3 session, not read from the diffs.** The
chart was re-measured from the committed PNG with an independent pipeline (177 bars,
52.277 px per 0.00100, max residual 0.086 pip, validated against the header's *printed*
last-bar OHLC to 0.48 pip) and the transcript re-counted by regex over the verbatim body.
Everything reproduces: the day separators at `x = 147, 273, 429, 573, 717, 861, 987, 1149`;
Sun 2 Aug = **2 bars**, open **0.80552**, high **0.80737 `23:00`**; Fri 31 Jul open
**0.80578**, low **0.80538**, close **0.80678**; the weekend gap at **−12.63 pip**; the
`31` and `Aug` label centroids at **146.12** and **273.03**; and `PFH`/`PFL` at **zero**
occurrences with "peak formation" spelled out four times. `REMEDIATION_PROTOCOL.md` §2 was
verified line by line — every deleted line has a superseded-in-place counterpart.

**Open item 12 is DISCHARGED.** The two remaining minors are documentation-precision items
inside sentences that were themselves just corrected, neither of which changes any value or
conclusion: the `level count` clause in `V02_TRANSCRIPT.md` (the literal string occurs zero
times; the referent occurs once at `[00:33:11]`), and the *"174 of 176"* continuity figure,
which does not reproduce — R3 measures **172** at the stated 0.15-pip threshold or **175**
above 0.8 pip, with three genuine sub-pip gaps besides the weekend one. **The continuity
figure is recorded against R2, not against the student**, since required correction 1
instructed the student to state R2's number and the remediation did so accurately. This is
the second round in a row in which a reviewer's own verified figure failed to reproduce
under the next round's independent measurement (R1's `PFH`/`PFL` count at R2, R2's
continuity count at R3) — the pattern is worth carrying to `CUMULATIVE_25.md`.

**The V03 gate is now OPEN** — D-004 satisfied. Separately, the project owner has confirmed
the parallel V03 work as an **intentional override** of the closed gate rather than an error
to correct. R3 took no position on the override itself but recorded that it was **not yet
written down**: `DECISIONS.md` had no entry for it, so `COURSE_PROGRESS.md` and open item 9
below described an authorized action as a live violation. Recommended owner action —
record it as a numbered decision and reconcile both. **The mechanism finding behind open
item 9 survives the override and is not closed by it:** a written gate with no enforcement
failed twice in one day.

> **DISCHARGED 2026-08-10 by the project owner.** `DECISIONS.md` **D-023** records the
> override (one instance, V02 → V03, not precedent, not to be reverted) and
> `COURSE_PROGRESS.md` is reconciled to it; open item 17 is **CLOSED**. Recorded with it,
> **D-024** sets the standing rule this collision exposed: a review round with **0
> `CRITICAL` and 0 `MAJOR`** opens the next lesson's gate even on a `REVISE` verdict, with
> the minor fixes deferred but still owed before the lesson can reach `COMPLETE`; **any
> `CRITICAL` or `MAJOR`** holds the gate closed until fixed *and re-reviewed*. Under D-024,
> V02 R2 would have opened the V03 gate on its own terms and no override would have been
> needed. Open item 9 remains **OPEN** on its mechanism ground, unchanged.

V03 reviewed 2026-08-10 (R1): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
3 minor** — under D-024 the **V04 gate is OPEN**, with the minors owed before V03 reaches
`COMPLETE`. This is the strongest student submission to date, and the review was run
adversarially against the six audit items the mastery report itself nominated. Everything
load-bearing reproduced: the citation audit was independently re-performed (425 marker
citations checked for existence; **99 quote+timestamp pairs re-matched at exact marker
resolution, all 99 resolving**), the §4e fifteen-`R =`-label correction re-derived from
independent crops, A-026's spoken resolution read directly in a full-transcript pass, the
homework's 116/116 chain validation and every derived table figure recomputed from the raw
JSON, the dataset externally corroborated against ECB reference fixes on all five days and
all four pairs, and — the round's substantive addition — **the C-004 negative claim was
re-verified on the complete 857-frame sweep** (found intact in the prior session's
scratchpad, identity confirmed pixel-exactly, re-clustered into 76 states, every state
reviewed: no session-times slide exists in V03). The three minors are precision defects
that change no conclusion: the homework's ADR figures do not re-derive from the committed
data (E19), the transcript's coverage block claims "strictly monotonic, no duplicates"
against three benign same-second duplicate markers (E20), and the 2.5–3-day-window
finding is stated as 4-of-4 where only 2 of 4 measure the taught object (E02 — the datum
must be scoped before it is cited against `C-001`). Reviewer-side housekeeping in this
round: the DECISION TABLE below had never gained its V02 R3 row (same staleness class as
open item 14); added with this update.

**Student remediation applied 2026-08-10 (same day, post-R1).** All three minors were
corrected: M1 — the day-boundary convention is now stated in homework §2.5 (the 21:00 UTC
FX day, five days of six 4h bars) and the twenty per-pair daily ranges behind it are
committed in the file, with the four ADR figures recomputed under that stated convention
(46.5 / 55.7 / 138.9 / 54.4; the un-re-derivable 47.0 / 54.8 / 148.2 / 56.5 are retained
in a correction note); M2 — the transcript's I-008 coverage line now reads
"1,230 timestamps, 1,227 distinct, non-decreasing throughout, three benign same-second
adjacent pairs", the duplicates named; M3 — the duration finding is scoped to 2 of 4 in
homework §2.5 Finding A, homework §4 point 3, and mastery report §2 and §D. No conclusion
changed anywhere: 0 of 4 still reach 3 × ADR, and both supported pairs still exceed the
taught window. **Open items 18–20 move to APPLIED — PENDING VERIFICATION at R2.**

V03 re-reviewed 2026-08-10 (R2): **`REVISE`**, confidence HIGH. 0 critical, 0 major,
**1 minor**. Remediation-verification round by a fresh session; each of the three minors
was re-derived from primary data rather than read for plausibility. **M1 and M3 verify
cleanly and close.** M1: the 21:00-UTC FX day is the only convention that splits the
30-bar dataset into five whole days, all twenty committed daily ranges reproduce exactly
from the raw JSON, all four ADR figures and their multiples re-derive, and 0 of 4 reaching
3 × ADR holds with margin (max 2.41×). M3: the 2-of-4 scoping is correct against the raw
OHLC — USDJPY and USDCHF never cut their block low, whose level *is* the week low at
bar 0 — and propagation was verified at all four named sites plus a whole-repo sweep for
surviving pre-correction figures; the `C-001` non-citation was independently confirmed by
reading the record, making the deferral legitimate. **M2 does not close.** The replacement
wording is correct in every component, but it was applied to the `PROVENANCE` I-008
criterion only — the `COVERAGE` block R1 explicitly named still reads *"strictly
monotonic, no duplicates"*, so `V03_TRANSCRIPT.md` now contradicts itself fourteen lines
apart. Carried as **R2 M2′ (`E20`)**; open item 19 stays open with a corrected status.
The V02 cross-check was re-tested independently and the remediation is right — V02 is
genuinely strictly monotonic (1,026 / 1,026). **Open items 18 and 20 CLOSE. V03 does not
reach `COMPLETE` this round**; the V04 gate was already OPEN per D-024 and is unaffected.

**Student remediation applied 2026-08-10 (commit `492bb11`).** The `COVERAGE` block's
residual sentence was replaced with the true statement; the verified I-008 wording at
lines 39–47 was correctly left alone. **Open item 19 moves to APPLIED — PENDING
VERIFICATION at R3.**

V03 re-reviewed 2026-08-10 (R3): **`PASS`**, confidence HIGH. **0 critical, 0 major,
0 minor.** Single-item closing round by a fresh session. `M2′` is discharged: the
`COVERAGE` and `PROVENANCE`/I-008 blocks now assert the same proposition, and it is true —
**1,230 markers, 1,227 distinct, zero decreasing transitions, exactly three adjacent
same-second pairs at `[00:35:21]` / `[01:00:13]` / `[01:04:30]`, largest gap 13 s at
`[01:09:02]`, final entry `[01:10:39]`** — every component re-derived this session by an
independent marker scan, with the header-block counting artifact explicitly ruled out (all
1,230 counted markers fall between lines 115 and 3,802, below the last `##` heading at 87).
The diff was read rather than the commit message: one file, five lines, `COVERAGE` only.
No third instance of the claim survives, and the **`E20` monotonicity class is now empty
project-wide** on a fresh scan of all four transcripts (V01 makes no claim; V02 is
genuinely strict at 1,026 / 1,026; V04 states the weaker true property). `LOG.md`
1746–1747 confirmed untouched and properly superseded at `LOG.md` 1848 ff. — append-only
handling is correct and must not be "fixed". `validate_project.py` clean: 97 / 0 / 0.
**Open item 19 CLOSES, completing 18–20. V03 is `COMPLETE`** — the V04 gate, already OPEN
under D-024, is now open on V03's own `PASS`.

V04 reviewed 2026-08-10 (R1): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
7 minor**, 5 note — under D-024 the **V05 gate is OPEN**, with the minors owed before V04
reaches `COMPLETE`. Reviewed by a fresh session (D-003). **This is the strongest submission
in the repository to date and it is not close.** Everything load-bearing reproduced under
independent measurement: **487 of 487** cited markers resolve to markers carrying their
words (`E11` absent for a third consecutive lesson — **de-escalated**); **320** italic-quoted
fragments were re-matched against the transcript body with only two inexact; the homework's
**476/480** cross-check against V03's dataset, its **474/480** 4h↔15m reconstruction, every
block figure, every weekly extreme and the **3.83-day** duration on both formed-anchor pairs
were recomputed from the committed JSON and match to the decimal; and the fenced 9-entry ASR
tail was confirmed properly fenced, terminated and uncited anywhere.

**The `M3` reproduction is genuine, not copied** — the two datasets *disagree* on four
fields, carry entirely different schemas, and both harvest scripts are committed. **This is
the project's first true cross-session replication.**

**The systemic-fabrication claim was verified at full population rather than spot-checked,
and is broader than the student claimed.** All 21 quarantined `RULES.md` files carry both
template quotes at `[00:05:00]` and `[00:18:00]`, exactly two rules each, **and a
byte-identical `NUMERICAL PARAMETERS` block (one hash, 21/21)**; `INFERRED VISUAL RULES` and
`TERMS` each have only two variants across 21 files. `EMA` occurs **zero** times in V04's
transcript. **Consequence for V05–V21: the per-lesson `RULES.md` audit is a solved problem**
and may be discharged in one step by confirming the three template markers and citing this
review plus `Q-004`. `NOTES.md` and `VISUAL_INDEX.md` are **not** covered — all 21 of each
are pairwise distinct and still need per-lesson examination.

**The `C-005` scope ruling is rendered in this review** — see open item 22. The
speaker-identification was verified independently, including reading *"Zen Jason … Alldredge"*
off frame 21's Navigator at 4× magnification; the boundary is confirmed by the speaker
referring to Steve in the third person 40+ times through segment B and, decisively, by
*"Steve is asking, do you ever take continuation trades?"* `[01:24:53]`. **69% measures at
68.5%.** The TDI gap was confirmed real at both cited markers and dimension G's `DEFERRED`
is upheld, as is `A-039`'s prohibition on dropping condition (c).

The seven minors are precision defects, none of which changes any conclusion: an undiagnosed
USDCHF 15-minute mis-slice at a partial week-open bar (`E19`), two smoothed quotations
inside the transcript's own verbatim-proof paragraph (`E01`), two ambiguity cross-references
pointing at the wrong records (`E20`/`E11`), a stale frame count and a stale index filename
(`E20`), a continuity validation not reproducible from committed data (`E20`), an unrecorded
visible TDI panel in two curated frames (`E20`), and four undeclared quality-control
checklist boxes (`E20`). **N1 additionally requires dimensions B and C to be re-dispositioned
from `PARTIAL`/`FAIL` to `DEFERRED` under `D-019`** — as labelled, V04 could never reach
`PASS`, because the cause sits in the source and will not change until TDI is taught.

**Pattern worth carrying to `CUMULATIVE_25.md`:** the student predicted its residual defects
would be in the interpretation file's prose. They were not — the interpretation came through
clean, and all four substantive minors landed in the **narrative describing mechanically
checked work** (the transcript's provenance paragraph, the homework's validation prose).
**The checked artifact is reliable; the paragraph describing the check is not, because it is
the one part nothing recomputes.**

V04 re-reviewed 2026-08-11 (R2): **`PASS`**, confidence HIGH. **0 critical, 0 major, 1 minor
(non-blocking)**, 3 note. **V04 is `COMPLETE`** (`D-004`). Reviewed by a fresh session that
authored no V04 artifact and applied none of the R1 corrections (`D-003`). **All seven minors,
note `N1` and the owner action are applied, and all nine verify.**

`M1`, the round's only evidence fix, was **re-derived from the data in both directions rather
than read off the diff**: the parent commit's JSON was recomputed to confirm the defect was
real (one −12.7 pip discontinuity at `m[3]→m[4]`, bar-0 open off by 28.1 pips,
`aggregate(m[4:16])` equal to 4h bar 0 on all four fields), and the corrected JSON was
recomputed to confirm the fix (**476/480 fields, 116/120 bars, zero in-week 15m
discontinuities in all four pairs**, all four residuals ≤ 0.3 pip and all in highs or lows).
The new array is exactly `old[4:]`, only USDCHF changed, and the 4h series is untouched and
continuous **116/116**. An independent cross-check the remediation did not claim: every pair's
re-indexed `j_hi_15m`/`j_lo_15m` maps through the new partial-first-bar arithmetic onto the
4h bar holding the same extreme, at an identical price — which closes under the new indices
and does not under the old ones. **The scoped 2-of-4 / 3.83-day result is unchanged**, USDCHF
still excluded on the 4-hour fact that its week low sits on bar 0.

`M5`'s judgement call was reviewed on the merits, not just for execution, and is **upheld**:
the harvest arrays were never written to disk, so committing a fresh harvest would attach data
to claims never computed on it — provenance fabrication, and worse than a declared gap. `M6`
was checked by opening both frames and magnifying them: the `Traders Dynamic Index Visual`
panel is there, the six-value readout is genuinely at the edge of legibility, and **declining
to transcribe it was correct**. `M7` accounts for all 19 `MASTERY_STANDARD.md` boxes
(13 + 2 `DEFERRED` + 4 UNCHECKED) and refuses to excuse the concept-library box by pointing at
`A-039`. `N1` follows `D-019`'s V01 F/G pattern exactly, with the original `PARTIAL`/`FAIL`
prose retained **verbatim** — diffed, not eyeballed. **`D-025` is faithful to the ruling** and
all four cross-references are live; the `REVIEW_PROTOCOL.md` §2 edit is the best of them,
because it makes future reviewers audit the **over-exclusion** direction too.

The one residual minor (`m1`, open item 34) is a mechanism clause inside a sentence written
*during* the remediation: the *"§3.3 windows are identical"* justification is true for the
high-side window (bar-for-bar identical) and false for the low-side one (clipped at the array
head; 5 bars → 1). **The descriptor table it justifies is genuinely unchanged — 1/1/1/1 on
both datasets, recomputed** — so under `REVIEW_PROTOCOL.md` §9 criterion 14 and the
`V02_REVIEW_R3.md` precedent it does not withhold the `PASS`, and an R3 for it would be the
artificial difficulty §16 forbids. **It is also one more instance of R1's own `N5` pattern**,
produced in the very commit that quoted `N5` approvingly: the paragraph describing the check
is the one part nothing recomputes.

---

## DECISION TABLE

| Video | Student Status | Review Version | Reviewer Decision | Critical Issues | Major Issues | Final |
|---|---|---|---:|---:|---:|---|
| V01 | REVIEW REQUIRED | R1 | REVISE | 0 | 2 | ⏳ |
| V01 | REVIEW REQUIRED | R2 | REVISE | 0 | 1 | ⏳ |
| V01 | REVIEW REQUIRED | R3 | PASS | 0 | 0 | ✅ |
| V02 | REVIEW REQUIRED | R1 | REVISE | 0 | 1 | ⏳ |
| V02 | REVIEW REQUIRED | R2 | REVISE | 0 | 0 | ⏳ |
| V02 | REVIEW REQUIRED | R3 | PASS | 0 | 0 | ✅ |
| V03 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V03 | REVIEW REQUIRED | R2 | REVISE | 0 | 0 | ⏳ |
| V03 | REVIEW REQUIRED | R3 | PASS | 0 | 0 | ✅ |
| V04 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V04 | REMEDIATION APPLIED | R2 | **PASS** | 0 | 0 | ✅ COMPLETE |

### Row template

```text
| V01 | PASS | R1 | REVISE | 0 | 2 | ⏳ |
| V01 | PASS | R2 | PASS   | 0 | 0 | ✅ |
```

Each review round gets its **own row**. Earlier rows are never edited or removed —
the progression from `REVISE` to `PASS` is part of the learning record.

### Legend

| Symbol | Meaning |
|---|---|
| ✅ | Reviewer PASS — advancement authorized |
| ⏳ | REVISE — in remediation |
| ⛔ | BLOCKED — substantial remediation required |
| 🔍 | Awaiting review |
| 👤 | Human review required |
| — | Not yet reached |

**Student Status** uses the student vocabulary (`PASS` / `REVIEW REQUIRED` /
`BLOCKED`); **Reviewer Decision** uses the reviewer vocabulary (`PASS` / `REVISE` /
`BLOCKED`). They are different actors' judgements and are deliberately not merged
(`SETUP_ISSUES.md` I-001).

---

## RECURRING ERROR COUNTS

Updated after every review. Reveals systematic weakness over time — a code that
keeps recurring is a training problem, not a lesson problem.

| Code | Description | Count | Lessons |
|---|---|---:|---|
| E01 | Source misquote | 2 | V02 (R1 ×1) — two ASR garbles repaired inside quotation marks; V04 (R1 ×1 — `M2`, **✅ CLOSED — VERIFIED at R2 2026-08-11** — both fragments restored to the adopted transcript's literal wording and the quoted side of the comparison stated: two of the six "matched near-verbatim" spot-check fragments in `V04_TRANSCRIPT.md` criterion 2 are smoothed readings, not the adopted wording. **The student self-caught and fixed ~20 instances of this class in its own draft before commit and the fix verifies** — an independent 320-fragment audit at R1 found only these two survivors, both in the provenance narrative rather than in the notes) |
| E02 | Unsupported generalization | 4 | V01 (R1 ×1, R2 ×2) — all closed at R3; V03 (R1 ×1 — duration finding scoped 4-of-4 where 2-of-4 is supported, M3 — **applied 2026-08-10, pending verification at R2**) |
| E03 | Missed qualifier | 0 | |
| E04 | Wrong sequence | 0 | |
| E05 | Wrong pattern boundary | 0 | |
| E06 | False positive | 1 | V02 (R1 ×1, also codes `E19`) — homework markup contradicts its own chart |
| E07 | False negative | 0 | |
| E08 | Hindsight contamination | 0 | |
| E09 | Cherry-picking | 0 | |
| E10 | Incomplete homework | 1 | V01 |
| E11 | Missing provenance | 9 | V01 (R1 ×1, R2 ×4, R3 ×4) — 8 closed at R3, 1 carried (open item 7). **DE-ESCALATED at V04 R1** — absent for a third consecutive lesson: V04's 487 cited markers were independently re-checked and **487 resolve** (V04 `M3` is a wrong *ambiguity-record* pointer, co-coded `E20`, not a wrong timestamp) |
| E12 | Ambiguity treated as rule | 0 | |
| E13 | Contradiction ignored | 1 | V01 |
| E14 | Outcome confused with correctness | 0 | |
| E15 | Machine assumption introduced prematurely | 0 | |
| E16 | Terminology drift | 0 | |
| E17 | Missing negative examples | 0 | |
| E18 | Invalid manual-backtest procedure | 0 | |
| E19 | Data/timeframe inconsistency | 2 | V02 (R1 ×1 as a co-code with `E06` — closed at R2; R2 ×1 — day boundary off by one bar, open); V03 (R1 ×1 — ADR figures not reproducible from committed data, M1 — **✅ CLOSED at R2 2026-08-10**: all twenty daily ranges and all four ADR figures re-derived exactly from the raw JSON under the stated 21:00-UTC convention); V04 (R1 ×1 — `M1`, **✅ CLOSED — VERIFIED at R2 2026-08-11** — partial 12-bar week-open 4h bar diagnosed and the slice corrected to 476 bars; 474/480 → 476/480; `bars_15m_in_4h_bar_0` and `verify_reconstruction.py` committed: USDCHF's 15-minute series is mis-sliced at a partial week-open bar, and the 27/30 reconstruction symptom was attributed to ±0.4 pip harvest noise when bar 0's open differs by **28.1 pips**. No conclusion changes; the 4h data is clean at 116/116) |
| E20 | Other | 22 | V01 (R1 ×6, R2 ×2, R3 ×1) — all closed at R3; V02 (R1 ×4) — closed at R2; V02 (R2 ×2) — open; V03 (R1 ×1 — transcript coverage block overclaims "strictly monotonic, no duplicates", M2 — **✅ CLOSED at R3 2026-08-10**: applied to the `PROVENANCE` I-008 criterion at `683a12a` and to the `COVERAGE` block at `492bb11`; both blocks now assert the same true proposition, re-derived component by component at R3. Carried as R2 M2′, never double-counted — one occurrence, remediated in two commits. The **monotonicity class is now empty project-wide**: V01 makes no such claim, V02 is genuinely strict (1,026 / 1,026), V04 states the weaker true property) | **V04 (R1 ×5 — all ✅ CLOSED — VERIFIED at R2 2026-08-11):** `M3` two ambiguity cross-references in `V04_TRANSCRIPT.md` pointing at `A-037`/`A-038` where the register holds `A-031`/`A-030` (co-codes `E11`); `M4` stale "26 frames" (27 exist) and stale `VISUAL_INDEX` filename — **sixth and seventh instances of the status-staleness class, open item 14**; `M5` homework validation 1's 569/549/20 continuity figures not reproducible from committed data (same promise as open item 13); `M6` a visible `Traders Dynamic Index Visual` panel in curated frames 21 and 22, unrecorded in `INDEX.md` and in `A-039`; `M7` four `MASTERY_STANDARD.md` quality-control boxes unchecked and undeclared (concept library, positive/negative/borderline examples) — **shared with V02 and V03, raise at `CUMULATIVE_25.md`** **V04 (R2 ×1 — `m1`, OPEN, non-blocking, open item 34):** the *"§3.3 windows are identical"* justification written during the R1 remediation is true for the high-side window and false for the low-side one; the descriptor row it justifies is genuinely unchanged (1/1/1/1, recomputed at R2). **Eighth instance of the narrative-about-a-check class R1's `N5` named** |

**Escalation rule:** any code reaching 3 occurrences is a systematic weakness.
Note it in the next cumulative review and consider whether the student protocol
itself needs strengthening — not just the individual lesson.

### ESCALATION TRIGGERED 2026-08-10 (R2)

Three codes have reached or passed the threshold on a single lesson.

- **`E11` — missing provenance (5).** The substantive defect. Across two rounds,
  eight statements were found citing a timestamp that does not carry their words:
  `S19`, `S27`-collision ×3 more locations, `X2`, `X3`, `S29`, and H5 in three
  files including an `ACTIVE` decision record. **No quotation was fabricated** — in
  every case the words exist in the recording and are quoted accurately; only the
  citation is off, typically by 10–40 s and usually because the passage start was
  cited instead of the sentence. This is the same reflex that produced `Q-001`,
  caught at the cheap end. **Protocol implication:** `STUDY_PROTOCOL.md` should
  require that a quoted sentence cite the marker its *first words* fall under, and
  that passage-level citation be written as a range (`[a]`–`[b]`), never as a bare
  start. Raise at the 25% cumulative review.
- **`E20` — other (8).** Almost entirely stale status text: files asserting a state
  of the world that was true when written and is now false. Same class as `Q-001`
  in miniature. **Protocol implication:** any file carrying a `STATUS` block or a
  "none / empty / not captured" assertion should be re-read at the close of every
  session that changes what it describes.
- **`E02` — unsupported generalization (3).** All three concern the blue/red boxes.
  Two of the three were *introduced during remediation of the first*, which is
  itself the lesson: a correction is new work and carries the same generalization
  risk as the original.

### ESCALATION UPDATE 2026-08-10 (R3)

All three escalated codes are **closed for V01**. The counts above are cumulative and are
not reset — a closed finding still happened.

- **`E11` rose from 5 to 9 at R3**, eight of them closed. R3 found three further misdatings of
  the same class while applying R2's action 4: the instructor's day-count acknowledgement
  cited at `[00:36:17]` in six places when it is at `[00:36:13]`–`[00:36:15]`; "trap move"
  first-use cited at `[00:33:33]`, which is neither a marker nor a passage about trap
  moves; and `S33` cited at `[00:45:40]` when the four-item recap is at `[00:45:44]`. All
  corrected. **Every V01 quotation now resolves to a marker carrying its words.**
- **Deliberately not corrected, and carried as open item 7:** seven cited timestamps in
  V01 files are not transcript markers at all — `[00:25:51]`, `[00:30:44]`, `[00:35:38]`,
  `[00:38:02]`, `[00:39:43]`, `[00:40:26]` (and `[00:33:33]`, which *was* corrected
  because it also pointed at the wrong content). The remaining six each land inside the
  passage they cite, 2–4 s past the marker, and resolve to the right words. Fixing them is
  precisely the `STUDY_PROTOCOL.md` amendment proposed below and deferred to the 25%
  review; applying an unadopted rule retroactively was judged worse than leaving six
  resolvable approximations. **This is the strongest concrete argument for adopting the
  amendment**, and it should be quoted at `CUMULATIVE_25.md`.
- **`E20` rose to 9.** `AUTOMATION_AMBIGUITIES.md` and `CONTRADICTIONS.md` status blocks
  had gone stale **a third time** — corrected at R1 finding 6b, then invalidated again by
  the V02 pass adding `A-019`–`A-028` and `C-003`–`C-004`. The R2 protocol implication
  ("any file carrying a `STATUS` block should be re-read at the close of every session
  that changes what it describes") is not a theoretical concern; it has now failed three
  times on the same two blocks. **Recommend promoting it from a suggestion to a
  `STUDY_PROTOCOL.md` session-close requirement at the 25% review**, alongside the
  citation amendment.

### ESCALATION UPDATE 2026-08-10 (V02 R1)

- **`E11` — missing provenance — did NOT recur.** This is the headline. It was V01's
  dominant defect across three rounds (9 occurrences) and prompted the proposed
  `STUDY_PROTOCOL.md` citation amendment. V02's R1 sampled ~20 cited timestamps against
  the transcript, weighted toward numbers and load-bearing claims, and **every one
  resolved to a marker carrying its words.** The amendment is still worth adopting at the
  25% review, but the behaviour it targets has already improved without it.
- **`E20` — other — rose from 9 to 13, four of them open on V02.** Same class as before:
  status text asserting a state of the world that has gone stale, plus occurrence counts
  that do not match the artifact they count. Two are especially instructive. The
  `CONTRADICTIONS.md` STATUS block is now wrong for the **fourth** time — and this time
  the error was *introduced by the R3 edit that was correcting that same block*, which is
  the R2 lesson repeating ("a correction is new work and carries the same risk as the
  original"). The `COURSE_PROGRESS.md` PHASE STATUS row contradicts the same file's own
  SUMMARY. **This code has now failed on status blocks in four separate rounds and is the
  project's most persistent weakness.** Promote the session-close re-read from suggestion
  to requirement at the 25% review, and consider a mechanical check in
  `validate_project.py` — every one of these is arithmetic over the file's own contents
  and could be verified automatically rather than by eye.
- **`E06` — false positive (1), new.** V02's homework markup states price levels and days
  that its own committed chart does not show, and draws a confirmation of the C-001 day
  count from them. Novel class for this project: the previous defects were all about
  *citing sources*; this is the first about *reading price*. **Protocol implication:**
  chart-derived claims need the same verifiability standard as transcript-derived ones.
  A markup keyed to dates and prices should be reproducible from the image by someone
  who was not there — which means naming how the day boundaries were established, not
  estimating them from axis ticks.
- **`E01` — source misquote (1), new.** Minor in effect — both repairs are almost
  certainly correct — but it is the first time this project has smoothed ASR garble
  inside quotation marks, and the file it happened in explicitly promises not to.

---

## SEVERITY TOTALS

Last fully reconciled at V02 R1; the pre-V03 rows below are carried as found and were
not re-audited by the V03 round (reconciling them against V02 R2/R3 is folded into
open item 14's arithmetic-check work item). **V03 R1's delta is authoritative:
+3 MINOR (M1–M3, all open), +5 NOTE (N1, N2, N3, N5 closed as observations; N4 —
the three-lesson manual-backtest debt — carried open).** The V02 R1 open MAJOR
recorded below this table closed at R2/R3.

**V03 R2's delta:** +0 MINOR, +5 NOTE (all closed as observations). R2 raised no new
finding — its single minor, M2′, is R1's M2 carried forward as incompletely remediated,
not a fresh defect, and is not double-counted. **2 of V03 R1's 3 minors close** (M1, M3),
leaving MINOR open at 6.

**V03 R3's delta:** +0 MINOR, +4 NOTE (N1 the missing log entry for `492bb11`, N2 the
V04 marker-scan counting trap, N3 the now-stale pointer in `V04_TRANSCRIPT.md` line 30,
N6 the clean validator run — all closed as observations; R3's N4 and N5 restate carried
items and are **not** double-counted). R3 raised no new finding of any severity.
**V03 R1's last remaining minor closes** (M2, via M2′), leaving MINOR open at 5 — none of
them V03's. All of V03's own findings across three rounds are now closed.

**V04 R1's delta:** **+7 MINOR (M1–M7, all open), +5 NOTE** (N3, N4, N5 closed as
observations; **N1 — re-disposition dimensions B and C as `DEFERRED` under `D-019` — carried
open as a required action**; N2 restates the carried manual-backtest debt and is **not**
double-counted). **0 CRITICAL, 0 MAJOR — the V05 gate opens under D-024.**

**V04 R2's delta:** **+1 MINOR (`m1`, open item 34 — non-blocking and deferred by design),
+3 NOTE** (all closed as observations: N1 the accuracy of the remediation's own self-report,
N2 the stale `CONCEPT_INDEX.md` STATUS block — **not charged against V04**, it belongs with
open item 14 and the concept-library debt, N3 the statement of what R2 did not re-audit under
`REVIEW_PROTOCOL.md` §4). **All seven of V04 R1's minors close, and `N1` closes as a required
action discharged.** 0 CRITICAL, 0 MAJOR. **V04 PASSES and is `COMPLETE`.**

| Severity | Total | Open | Closed |
|---|---:|---:|---:|
| CRITICAL | 0 | 0 | 0 |
| MAJOR | 4 | 0 | 4 |
| MINOR | 29 | 6 | 23 |
| NOTE | 39 | 5 | 34 |

**Open MAJOR — V02 R1 finding 1.** The 11a homework markup contradicts the chart it
cites (PFH misplaced by 15 pips; the reversal attributed to Friday when it is Thursday's
move and Friday ran the opposite way), producing a false confirmation of the "at least
3 days" doctrine that `C-001` has open. Blocks V02 advancement. See
`18_REVIEW/V02/V02_REVIEW_R1.md`.

A lesson with unresolved CRITICAL issues cannot pass.

**MAJOR ledger — closed.** R1 raised 2. Finding 2 (`E10`, dimension F) closed at R2.
Finding 1 (`E02`, the box reading) closed in three of four locations at R2, reopened as
R2 finding N1, and **closed at R3**: `A-006`'s trailing block is withdrawn in place with
its original wording retained and its refutation recorded beside it.

**Closed at R3:** every remaining R1 and R2 finding. Three new `E11` defects were found
and closed in the same round, and one new `E20` (status blocks stale a third time) was
found and closed. **Two NOTES stay open** and neither bears on V01's mastery: the six
non-marker timestamp approximations, deferred with the `STUDY_PROTOCOL.md` amendment to
the 25% review (open item 7); and the V02 gate finding (open item 9), which is a process
observation about how the project sequenced its sessions, not about what V01 understood.

---

## OPEN RESEARCH ITEMS CARRIED FORWARD

Non-foundational issues that permitted a `PASS` but must not be forgotten.

| # | From | Item | Where tracked | Status |
|---|---|---|---|---|
| 1 | V01 R1 | `C-001` — day-count away from the anchor is self-contradicted in source and unresolved by the instructor. No artifact may commit a value. Re-examine at every weekly-holding-period lesson and at the 25% cumulative review | `CONTRADICTIONS.md` C-001 | OPEN |
| 2 | V01 R1 | `I7` — whether "anchor point", "peak formation high/low" and "M or W formation" are one concept. Stays `INFERRED / Low`; **re-adjudicate at V02** | `V01_INTERPRETATION.md` I7 / G4 | OPEN |
| 3 | V01 R1 | H4 / H5 `DEFERRED` pending `I-007` (chart data source). Reclassified in the mastery report 2026-08-10; `D-019` records the general rule. Perform when I-007 closes | `SETUP_ISSUES.md` I-007; `DECISIONS.md` D-019 | OPEN |
| 4 | V01 R1 | Re-check `[00:46:04]`, `[00:48:05]`, `[00:48:13]` against the retained mp4 before any session-timing parameter is coded (`M3`) | `V01_INTERPRETATION.md` M3 / Q7 | OPEN |
| 5 | V01 R1 | Dimension B (Recognition) deferred to after V02 defines the trading zone | `V01_MASTERY_REPORT.md` B | OPEN |
| 6 | V01 R1 remediation | The stale *"no screenshot exists for V01"* paragraph appears in **17** ambiguity records, not the 3 instances R1 counted. `A-006` fixed as a dependency; **16 remain** (`A-001`–`A-005`, `A-007`–`A-017`). **Adjudicated by R2 (Part 3) — this is partly study work, but the scope stated here was wrong.** `A-009`, `A-015` and `A-017` were named as needing fresh visual claims; all three already carry sound visual updates, audited and upheld in R2. The records that actually need a fresh visual determination are **`A-002`, `A-008`, `A-016`** (determinations supplied in R2 Part 3.3), plus `A-003`'s five self-contradicting fields. `A-011` / `A-012` / `A-014` gain slide-text evidence; `A-007` needs a "frame exists, defines nothing" note; the remaining eight are mechanical | `AUTOMATION_AMBIGUITIES.md`; `18_REVIEW/V01/V01_REVIEW_R2.md` Part 3 | **CLOSED at R3** — all 16 records corrected; `A-002`, `A-008`, `A-016` determinations written and audited against the frames; two of R2's supporting claims corrected in the process (see `V01_REVIEW_R3.md` Part 3) |
| 7 | V01 R2 | Citation hygiene is the project's recurring weakness (`E11` ×5). Eight statements across two rounds cite a timestamp that does not carry their words. No quotation is fabricated. Consider requiring in `STUDY_PROTOCOL.md` that a quoted sentence cite the marker its first words fall under, and that passage-level citation be written as an explicit range | `18_REVIEW/REVIEW_INDEX.md` escalation note; raise at `CUMULATIVE_25.md` | OPEN |
| 8 | V01 R2 | `SETUP_ISSUES.md` I-006 described the SWF header frame-rate speedup as "an untested faster path". **R2's own framing was stale in turn:** it cited `D-020` as having ruled the speedup out, but `D-020` is `RETRACTED` and `D-021` records that the speedup **works at 40×** and is the default method. `I-006` now points to `D-021` | `SETUP_ISSUES.md` I-006; `DECISIONS.md` D-021 | **CLOSED at R3** |
| 9 | V01 R3 | **The V02 gate was not honoured.** `D-004` makes reviewer `PASS` the only progression gate, and `COURSE_PROGRESS.md` recorded `V02 GATE: CLOSED`, yet a full V02 student pass (transcript, notes, interpretation, 25 screenshots, homework, mastery report, `A-019`–`A-028`, `C-003`–`C-004`) was completed while V01 was in remediation. V01's `PASS` makes this moot going forward, and none of the V02 work is discarded — but the gate did not hold, and the next one (V02 `PASS` before V03) must | `DECISIONS.md` D-004; `COURSE_PROGRESS.md` | OPEN — process. **First test PASSED at R2:** V02 R1 returned `REVISE` and no V03 artifact was created — verified at the filesystem level across `03_LESSON_NOTES/`, `04_SCREENSHOTS/`, `05_HOMEWORK/`, `07_MASTERY_REPORTS/`. Stays open until a second gate holds. **ESCALATED at R2 to a LIVE BREACH — the second occurrence, and this one is not moot.** A V03 student pass appeared in the working tree during R2 while V02 was unpassed. **Two failures of the same written gate in one day is a mechanism problem, not a discipline problem:** D-004 has no enforcement, exactly like the status-block rule in R2 Minor 3. Concrete fix — a pre-flight guard in `validate_project.py` that refuses `VNN` artifact creation while `VNN GATE: CLOSED`. Required disposition in `18_REVIEW/V02/V02_REVIEW_R2.md` §7: stop the V03 pass, **do not delete the V03 work**, re-audit it against a passed V02. **UPDATED 2026-08-10 — `DECISIONS.md` D-023 and D-024.** The second occurrence is now recorded as an **owner-authorized override** (D-023): R2 §7's "stop the V03 pass" disposition is discharged and the V03 work stands as committed — nothing to revert or re-audit. **This item stays OPEN on its mechanism ground alone**, which the override does not touch: an unenforced written gate failed twice, and the override explains only why the second failure was authorized, not why an unauthorized one would have been caught. D-024 now defines what holds the gate (minors-only opens it; any `CRITICAL`/`MAJOR` closes it), so the `validate_project.py` pre-flight guard should implement **D-024's severity table**, not D-004's simpler `PASS`-only reading, plus an explicit override flag that must name the authorizing decision entry |
| 10 | V02 R1 | ~~**`C-001` has one empirical datum and it was misread.**~~ The 11a homework is the only independent observation the project has made about the day-count doctrine, and its "runs Tuesday through Thursday, consistent with 'At Least 3 Days'" claim is contradicted by the chart (price traded back above the Monday high on Thursday). Once 11a is corrected, record what the week **actually** shows against `C-001` — including "nothing", which is a legitimate result. Do not let a corrected reading quietly drop the C-001 entry | `CONTRADICTIONS.md` C-001; `18_REVIEW/V02/V02_REVIEW_R1.md` MAJOR 1 | **CLOSED at R2** — 11a redone from measurement and independently re-verified; the "three days" confirmation withdrawn; the corrected result (level 0.81150 set Mon 3 Aug 15:00 UTC, first bar above it Thu 6 Aug 15:00, **72 hours exactly**) recorded in `CONTRADICTIONS.md` under C-001 as explicitly non-resolving. The entry was **not** quietly dropped. `EFFECT ON C-001: NONE` is correct in both directions — three counting conventions give three answers, and the level was reader-selected against `A-004`. No day-count value is committed anywhere |
| 11 | V02 R1 | **A-006 / A-003 spot-check requested by V01 R3 — completed, both PASS.** Verified against the frames, not against R3's word: `[00:40:25]` prints "Trigger The Pendings"/"Trigger The Stops" as A-003 claims; `[00:38:50]` shows the pale-blue rectangle's left edge on the second vertical separator and covering a sharp advance, confirming both A-006's withdrawal and R2's narrowing. R3's remediation is substantively correct despite its D-003 departure — though two records is not an audit of fifteen actions | `18_REVIEW/V02/V02_REVIEW_R1.md` Ambiguities | **CLOSED** |
| 12 | V02 R2 | **`V02_HOMEWORK.md` §1.1's measurement pipeline is advertised as reusable for the dimension-G backtest but places one bar on the wrong side of the Fri 31 Jul → Sun 2 Aug boundary**, and its *"open = prior close on all six boundaries"* self-validation was applied at a weekend boundary where continuity should not be expected. The chart's own dotted day separators (`x = 147, 273, 429, 573, 717, 861, 987, 1149`) settle it. No conclusion in the homework changes. Must be corrected before the pipeline is reused | `V02_HOMEWORK.md` §1.1; `18_REVIEW/V02/V02_REVIEW_R2.md` Minor 1 | **CLOSED at R3** — corrected in `8df7c32` and independently re-derived at R3 from the PNG: separators, bar counts, both corrected rows, the −12.63 pip weekend gap and the `31`/`Aug` label centroids (146.12 / 273.03) all reproduce exactly. The two refuted arguments are withdrawn with the measurements that kill them, the superseded reasoning is retained in place per `REMEDIATION_PROTOCOL.md` §2, and the pipeline's real limits are now written into the file: read the chart's own separators, and do not expect continuity across a session gap |
| 13 | V02 R2 | **Two measurements of the same chart disagree, and one is untracked.** `05_HOMEWORK/V02/measure_usdchf_week.py` is a working, uncommitted measurement script that encodes the *correct* Sun 2 Aug mapping and calls the boundary *"uncertain by one bar"*, contradicting committed §1.1's "settled". **Leave it in place, adjudicate with item 12, do not delete.** §1.1 promises a reproducible method and commits no script; committing a corrected one discharges that promise | `05_HOMEWORK/V02/`; `18_REVIEW/V02/V02_REVIEW_R2.md` Note 8 | OPEN |
| 14 | V02 R2 | **A stated rule did not prevent the defect it was written for.** `COURSE_PROGRESS.md`'s status view went stale in the same commit that declared the SUMMARY authoritative — fifth occurrence of this class. Promote R1's proposed mechanical check in `validate_project.py` from suggestion to work item at the 25% review; all five occurrences are arithmetic over a file's own contents | `18_REVIEW/REVIEW_INDEX.md` escalation notes; raise at `CUMULATIVE_25.md` | OPEN — **sixth occurrence at R3**, again inside a remediation: correction 2 shipped in `d030a14` without updating `COURSE_PROGRESS.md`, which still read `⏳ OUTSTANDING` for it, and the PROGRESS TABLE's V02 row had never been reconciled to R2 at all. Discharged by the R3 session, which had to rewrite those lines to record its decision. Six instances, all arithmetic over a file's own contents. **This is a work item at the 25% review, not a suggestion** |
| 15 | V02 R3 | **`level count` is presented as a verbatim transcript occurrence and the literal string occurs zero times.** The referent is real — *"you can't count the levels"*, `[00:33:11]` — and `A-004` rests on the passage, not the string. `V02_SOURCE_NOTES.md` §3 needs **no** change (its row is headed *"Level count / counting the levels"* and quotes the actual words); only `V02_TRANSCRIPT.md`'s "One thing was removed" paragraph does. Notable because it is the residue of the same false claim: three verbatim counts were asserted, two were checked and found to be zero, the third was carried forward unchecked in the edit that corrected the other two. **Non-blocking; fix at the next natural touch** — exact wording in `V02_REVIEW_R3.md` §3 | `V02_TRANSCRIPT.md` §"One thing was removed"; `18_REVIEW/V02/V02_REVIEW_R3.md` Minor 1 | OPEN |
| 16 | V02 R3 | **The *"174 of 176"* continuity figure does not reproduce.** R3's independent measurement finds **172** boundaries continuous at the stated 0.15-pip threshold, or **175** above 0.8 pip; three genuine sub-pip gaps exist besides the weekend one (`x=285` −0.19 pip, `x=447` +0.77, `x=933` −0.77, confirmed visually at 4× zoom), so *"the only open ≠ prior-close discontinuity"* is overstated. **174 is unreachable under any threshold. Charged against R2, not the student** — required correction 1 instructed the student to state R2's number and the remediation did so accurately. Changes nothing and errs in the safe direction: continuity is *weaker* than claimed, which strengthens the corrected reasoning. **Non-blocking**; restate as 175 of 176 within 1 pip, only material discontinuity −12.6 pip at `x=273`, three sub-pip gaps besides | `V02_HOMEWORK.md` §1.1/§1.4; `V02_MASTERY_REPORT.md`; `COURSE_PROGRESS.md`; `18_REVIEW/V02/V02_REVIEW_R2.md` §1c | OPEN |
| 17 | V02 R3 | **An owner-authorized override is recorded in the repository as an unresolved violation.** The project owner confirmed the parallel V03 work as an intentional override of the closed D-004 gate, but `DECISIONS.md` carries no entry for it (last entry D-022), so `COURSE_PROGRESS.md`'s `V03 GATE` block and open item 9 above still read as a live breach. A future session will either halt authorized work or conclude the gate register is unreliable. **Owner action:** record the override as a numbered decision and reconcile both locations to it. **Does not close item 9's mechanism finding** — a written gate with no enforcement failed twice in one day, and the `validate_project.py` pre-flight guard is still the fix | `DECISIONS.md`; `COURSE_PROGRESS.md`; `18_REVIEW/V02/V02_REVIEW_R3.md` Note 3 | ✅ **CLOSED 2026-08-10 — `DECISIONS.md` D-023** records the override as a numbered decision (scope: one instance, V02 → V03, source-side work only; not precedent; not to be reverted), and `COURSE_PROGRESS.md`'s `V03 GATE` block and `NEXT ACTION` item (c) are reconciled to it. `V02_REVIEW_R2.md` is deliberately left unedited per §11. Item 9 below is **not** closed by this — see its own row |

| 18 | V03 R1 | **M1 — homework ADR figures not reproducible.** State the day-boundary convention and commit the five per-pair daily ranges (or recompute under a stated convention). The 0-of-4 conclusion survives every convention tried | `V03_HOMEWORK.md` §2.5 Finding B; `18_REVIEW/V03/V03_REVIEW_R1.md` M1 | ✅ **CLOSED 2026-08-10 — VERIFIED at R2.** Convention stated (21:00 UTC FX day; bars 0–5 / 6–11 / 12–17 / 18–23 / 24–29); all twenty daily ranges committed in §2.5; ADR recomputed to 46.5 / 55.7 / 138.9 / 54.4 with a correction note retaining the superseded figures. R2 re-derived every one of the twenty ranges from the raw JSON — all match to a tenth of a pip — plus 3×ADR, the four multiples (1.73 / 1.64 / 2.41 / 1.48), and the 116/116 bar continuity the split depends on. 21:00 UTC confirmed as the only 4h-aligned boundary yielding five whole days. 0 of 4 reaching 3×ADR holds with margin |
| 19 | V03 R1 | **M2 — transcript coverage block overclaims.** "Strictly monotonic, no duplicates" is false: three benign same-second adjacent duplicate markers (`[00:35:21]`, `[01:00:13]`, `[01:04:30]`); sequence is non-decreasing. Fix the wording | `V03_TRANSCRIPT.md` COVERAGE; `V03_REVIEW_R1.md` M2 | ✅ **CLOSED 2026-08-10 — VERIFIED at R3.** Commit `492bb11` replaced the `COVERAGE` sentence with the true statement and left the verified I-008 text at lines 39–47 untouched (diff read: one file, five lines). R3 re-derived every component from the transcript itself — 1,230 markers, 1,227 distinct, 0 decreasing transitions, exactly 3 adjacent same-second pairs at the three named markers, largest gap 13 s at `[01:09:02]`, final entry `[01:10:39]` — and ruled out the header-block counting artifact (all counted markers fall between lines 115 and 3,802; last `##` heading at 87). Both blocks now agree and both are true; no third instance survives; the `E20` monotonicity class is empty project-wide on a fresh scan of all four transcripts. **This closes items 18–20 as a set and takes V03 to `COMPLETE`.** `LOG.md` 1746–1747 re-confirmed untouched and properly superseded at 1848 ff. — do not "fix" them. **Prior status, retained for the record:** ⚠️ *STILL OPEN after R2 — applied to the wrong location.* The corrected line ("1,230 timestamps, 1,227 distinct, non-decreasing throughout, three benign same-second adjacent pairs at `[00:35:21]`, `[01:00:13]`, `[01:04:30]`", plus a correction note) was added to the **`PROVENANCE AND VERIFICATION` I-008 criterion 1**, lines 39–46. R2 re-derived every component of it by regex and **all seven check out exactly** — that wording stands. But the sentence R1 charged lives in the **`COVERAGE`** block, lines 23–24, which was left untouched and still reads *"timestamps strictly monotonic, no duplicates"*; the file now asserts both propositions fourteen lines apart. **Required: replace `COVERAGE` lines 23–24 with the true statement; leave lines 39–46 alone.** V02's identical-sounding line was independently re-scanned at R2 and is confirmed **true as written** (1,026 markers, 1,026 distinct, zero decreasing transitions) — leaving it unchanged was correct. Note: `V01_TRANSCRIPT.md` has five same-second pairs (974 / 969) but makes no monotonicity claim, so nothing is false there — the E20 class is empty project-wide once this row closes. Carried as `V03_REVIEW_R2.md` M2′ |
| 20 | V03 R1 | **M3 — duration finding over-scoped.** "4 of 4 exceed the 2.5–3-day window" counts two pairs (USDJPY, USDCHF) whose low is the week-open bar with no formed anchor — supported sample is 2 of 4 (both 3.8 days, still exceeding). Scope it in homework §2.5A and mastery report §2 before it is cited against `C-001` | `V03_HOMEWORK.md` §2.5; `V03_MASTERY_REPORT.md` §2; `V03_REVIEW_R1.md` M3 | ✅ **CLOSED 2026-08-10 — VERIFIED at R2.** Homework §2.5 Finding A now carries a per-pair "does this measure the taught object?" column, an explicit 2-of-4 scope statement, and the instruction that any citation against `C-001` must carry it; homework §4 point 3 and mastery report §2 and §D re-scoped to match. R2 re-derived the basis from the raw OHLC: USDJPY and USDCHF have `cut_lo` = 0 bars — the block low is never taken out and *is* the week low at bar 0 — while EURUSD and GBPUSD cut at bar 2 and form their lows at bars 4 and 5, both 92 h = 3.8 days. Propagation confirmed at all four sites, plus a whole-repo sweep finding no surviving pre-correction figure (the stale numbers in `LOG.md` 1746–1747 are a historical journal entry, superseded at 1859/1892, and must **not** be edited). The `C-001` deferral was tested by reading the record rather than trusting it: the V03 evidence section cites only transcript restatements and the new exit rule, and no homework duration appears anywhere in the file — so the datum is genuinely not yet cited, and the standing "scoping travels with it" instruction is committed in both homework §2.5A and mastery report §2, where a future session will be standing when it bites |
| 21 | V03 R1 | **N4 — manual-backtest debt, three lessons deep.** Each deferral individually sound (no testable entry rule yet), but the obligation accrues: when the first testable rule lands (plausibly the V03 exit once A-033 "outside structure" is defined), the hidden-future backtest backlog must be discharged against it. The reviewer will require it | `V03_REVIEW_R1.md` N4; `06_MANUAL_BACKTEST/` | OPEN |

| 22 | V04 student pass | **`C-005` needs a SCOPE RULING on guest-presenter material — owner or reviewer, not a student session.** V04 is 69% presented by someone who is not the course author, and the student session fenced all of it as non-doctrine. That is a large unilateral exclusion. **Should be settled before V05**, which shares V04's 2012-03-25 session date and may contain the same guest or the third presenter ("Carl", queued at V04 `[01:19:02]`). The record is `UNRESOLVED` *pending a ruling, not pending evidence* — no future lesson can resolve it | `CONTRADICTIONS.md` C-005; `V04_MASTERY_REPORT.md` audit item 1; `18_REVIEW/V04/V04_REVIEW_R1.md` §"The C-005 ruling" | ⚖️ **RULED 2026-08-10 at V04 R1 — OPEN only on the recording step.** **Guest-presenter material is admissible as SECONDARY, DESCRIPTIVE evidence and is EXCLUDED from the canonical methodology as NORMATIVE material.** Neither extreme is correct. *Normative* content (entry criteria, gates, filters, stops, targets, sessions, thresholds, schedules) may not enter the master spec, machine spec, concept library or any machine candidate, may not be cited **for or against** an instructor rule, and may never be merged with instructor statements into one rule set. *Descriptive* content (that a term exists, how it is spelled, that an object is displayed, what a printed artifact says) is admissible at a weight strictly below any instructor statement — it may **extend** an `A-xxx`/`C-xxx` record and may **never close** one. Four binding consequences: a guest statement can never resolve an ambiguity or contradiction; a guest/instructor divergence is a **corpus-hygiene** record, never a contradiction charged against the instructor; **speaker tagging is mandatory** from V04 forward for any multi-voice lesson; identifying a guest is provenance, not evidence. **Retroactive effect on V04: none — the ruling ratifies the student's existing handling exactly, and no V04 grade changes.** The reviewer verified the identification independently (*"Zen Jason … Alldredge"* read off frame 21's Navigator; segment B refers to Steve in the third person 40+ times and at `[01:24:53]` *"Steve is asking…"* places him in the audience; 69% measures at 68.5%). ~~**Owner action, before V05: record as `DECISIONS.md` D-025.**~~ ✅ **CLOSED 2026-08-11 — RECORDED as `DECISIONS.md` D-025**, refining `D-008`, with the ruling's four consequences carried into the entry verbatim in substance and cross-referenced from `D-008`, `D-004`'s pointer block, `COURSE_PROGRESS.md`'s `PROGRESSION RULE` and `REVIEW_PROTOCOL.md` §2. `C-005` updated: its "Required to resolve" field is discharged, and the record stays open as a **corpus-hygiene** record, which the ruling says is the right category. The recording step was the only thing left open here. |
| 23 | V04 student pass | **`A-039` — TDI is a REQUIRED condition of V04's entry rule and the course has never taught it.** Deferred at V03 `[01:01:53]` and again at V04 `[00:22:11]`; the instructor could not even display it on his own example chart. This is what blocks V04's dimension G. The record carries an explicit prohibition: **no session may drop condition (c) to make the rule testable** — a two-condition version is a different rule with a different hit rate (`E06`/`E18`) | `AUTOMATION_AMBIGUITIES.md` A-039 | OPEN — **UPHELD at V04 R1.** Both deferrals read at their markers and exact; all 13 `TDI` occurrences in V04 read in context and not one defines the indicator, its inputs, its bands, the shark-fin geometry or "blood in the water". Dimension G's `DEFERRED` upheld and `NOT APPLICABLE` correctly declined. The counter-argument (test (a)∧(b) alone) is **rejected**: dropping a *necessary* condition does not shrink the sample, it changes the population, because the discarded condition is the confirmation step. See also item 30 — TDI is *displayed* on the guest's platform, which changes nothing here |
| 24 | V04 student pass | **Manual-backtest debt is now FOUR lessons deep, and its character has changed.** Through V03 the deferral was "no testable entry rule exists". From V04 it is "a testable rule exists and one named input is missing". Item 21's obligation therefore has a concrete trigger for the first time: **when TDI is taught, the hidden-future backlog becomes dischargeable and must be discharged** | `REVIEW_INDEX.md` item 21; `A-039`; `06_MANUAL_BACKTEST/` | OPEN — **UPHELD at V04 R1.** The reviewer will require the backlog to be discharged in the lesson that teaches TDI |
| 25 | V04 R1 | **`M1` — USDCHF's 15-minute series is mis-sliced at a partial week-open bar.** On this feed USDCHF's first 4h bar of the week holds only twelve 15m bars; the fixed 16-bar aggregation therefore puts four previous-week bars at the head of the committed 480-bar slice (`offset_in_harvest = 261`) and leaves it four short at the tail. The `−12.7` pip weekend gap sits *inside* the committed week at `m[3]→m[4]`, and `aggregate(m[4:16])` reproduces 4h bar 0 exactly on all four fields. The 27/30 symptom was reported as ±0.4 pip harvest noise when bar 0's **open** differs by 28.1 pips. **No conclusion changes** — the 4h data is continuous 116/116 and USDCHF is already outside the scoped 2-of-4 result — but the 15m harvest is the pipeline V05 inherits. Same class as open item 12 | `05_HOMEWORK/V04/`; `V04_REVIEW_R1.md` M1 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** Diagnosed and re-sliced from the committed data. USDCHF's week is **476 = 12 + 29 × 16** bars, not 480 — the four leading bars were previous-week and nothing was missing from the tail. `offset_in_harvest` 261 → **265**, `j_hi_15m` 363 → 359, `j_lo_15m` 4 → 0, and a new per-pair **`bars_15m_in_4h_bar_0`** field (16/16/16/**12**) makes the aggregation explicit rather than assumed. USDCHF 27/30 → **28/30**; the 4h↔15m total **474/480 → 476/480**, its four residuals now all ≤ 0.3 pip and all in highs or lows. The ±0.4 pip misattribution is replaced by the real diagnosis in `V04_HOMEWORK.md` §1.2 validation 3, with the partial-first-bar behaviour stated as a limit of the 15m pipeline and a standing instruction to future sessions not to assume 16. New committed script **`scripts/verify_reconstruction.py`** recomputes it and exits non-zero on mismatch. **No conclusion changed, verified not assumed:** the 4h data is untouched (116/116), USDCHF stays excluded from the scoped 2-of-4 result on 4h grounds, and the §3.3 descriptor windows are identical because index and window shifted together ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Re-derived in both directions from the parent and current JSON by an independent script: the defect was real (one −12.7 pip discontinuity at `m[3]→m[4]`; bar-0 open off by 28.1 pips; `aggregate(m[4:16])` equal to 4h bar 0 on all four fields) and the fix is exact and minimal (new array is exactly `old[4:]`, only USDCHF changed, 4h untouched, `476 = 12 + 29×16` consumes the array, bar 29 reconstructs). **476/480 fields, 116/120 bars, zero in-week 15m discontinuities in all four pairs**, all residuals ≤ 0.3 pip and all in highs/lows. `verify_reconstruction.py` run as shipped: exits 0, and its checks are not tautological. Every pair's re-indexed 15m extreme maps onto the 4h bar holding the same extreme at an identical price — closes under the new indices, not the old. Scoped 2-of-4 / 3.83-day result unchanged, USDCHF still excluded on 4h bar 0 |
| 26 | V04 R1 | **`M2` — two smoothed quotations inside the transcript's own verbatim-proof paragraph** (`E01`): *"sitting up here"* for *"set up here"* `[00:50:34]`, and *"gave you a nice ugly looking kindergarten"* for *"Gaby a nice ugly look in kindergarten ma'am there"* `[01:10:36]`. Either restore both or state that the list quotes the Whisper re-transcription. **The student self-caught ~20 instances of this class before commit and that fix verifies** — these two are survivors in the provenance narrative, not in the notes | `V04_TRANSCRIPT.md` criterion 2; `V04_REVIEW_R1.md` M2 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** Both restored to the **adopted transcript's** literal wording — *"There was a bunch of money **set up** here…"* `[00:50:34]` and *"One, two, three, swipes. **Gaby** a nice ugly **look in** kindergarten **ma'am** there."* `[01:10:33]`–`[01:10:36]` — and the paragraph now states explicitly that the six specifics are quoted from the adopted transcript. The smoothing is disclosed in place rather than silently corrected ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Checked against the transcript **body**, not the diff: line 3047 *"There was a bunch of money set up here and they had to go after it."* `[00:50:34]` and lines 4138/4142 *"One, two, three, swipes. / Gaby a nice ugly look in kindergarten ma'am there."* `[01:10:33]`/`[01:10:36]` — both exact. Restoration taken rather than re-attribution, and the paragraph now states which side it quotes |
| 27 | V04 R1 | **`M3` — two ambiguity cross-references point at the wrong records.** `V04_TRANSCRIPT.md` `TRANSCRIPTION NOTES` sends *"the water"* to `A-037` and *"Timing Shadow Box / Brink Spox"* to `A-038`; the register holds the Asian-range halving and the guest's ADR window at those IDs. Correct targets **`A-031`** and **`A-030`**. Orphaned pre-assignments — the transcript shipped at `d6acbf8`, the register at `4235df1` | `V04_TRANSCRIPT.md`; `V04_REVIEW_R1.md` M3 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** *"the water"* → **`A-031`**; *"Timing Shadow Box / Brink Spox"* → **`A-030`**. A dated note in `TRANSCRIPTION NOTES` records the orphaned pre-assignments and their cause ✅ **CLOSED — VERIFIED at R2 2026-08-11.** `A-031` is *"blood in the water"/"bloodline"* and `A-030` is *"brinks shadow"/"shadow box"* — the correct subjects. `A-037` (Asian-range halving) and `A-038` (guest ADR lookback) confirmed to be the wrong ones, and every surviving `A-037`/`A-038` reference in the V04 artifacts re-checked and legitimate |
| 28 | V04 R1 | **`M4` — stale count and stale filename.** `V04_SOURCE_NOTES.md` says *"26 frames"* (27 exist); `V04_MASTERY_REPORT.md` FILES PRODUCED says `VISUAL_INDEX` (renamed to `INDEX.md` in the same session). **Sixth and seventh instances of the status-staleness class** — both are arithmetic or a filename check over the repository's own contents and belong in the `validate_project.py` check proposed at open item 14 | `V04_REVIEW_R1.md` M4; open item 14 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** `V04_SOURCE_NOTES.md` now reads *"27 frames, indexed in `04_SCREENSHOTS/V04/INDEX.md`"*; the mastery report's FILES PRODUCED block reads `INDEX.md` (and *"2 scripts"* → 3, since `verify_reconstruction.py` was added under item 25) ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Counted: 27 PNGs in `04_SCREENSHOTS/V04/`, 3 scripts in `05_HOMEWORK/V04/scripts/`. Both files corrected; the only surviving `VISUAL_INDEX` string is inside the remediation log describing the fix |
| 29 | V04 R1 | **`M5` — homework validation 1 is not reproducible from committed data.** *"569 bar transitions, 549 continuous, 20 breaks"* with break indices 15/45/75/105/135 and a GBPUSD exception at 143 requires full harvests; the JSON holds only the 30-bar week per pair (116 transitions available, and those reproduce 116/116). Accuracy is not in doubt — reproducibility is. Same promise as open item 13 | `V04_HOMEWORK.md` §1.2; `V04_REVIEW_R1.md` M5 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** Restated over the committed data — **116/116 continuous**, recomputed by `verify_reconstruction.py` — and the harvest-wide **569 / 549 / 20** figures explicitly marked **UNREPRODUCED**, in validation 1 and again in §1.3 "What is NOT validated". **The arrays were deliberately not manufactured back into the repo:** they were never written to disk, and re-harvesting today would produce a *different* dataset from the one every figure in the file was computed on. The week boundary the figures existed to establish is independently supported by the committed data (116/116, plus 476/480 agreement with V03's dataset) ✅ **CLOSED — VERIFIED at R2 2026-08-11, and the judgement call upheld on the merits.** The honest-caveat route was the correct one: the arrays were never written to disk, so committing a fresh harvest would attach data to claims never computed on it — provenance fabrication, worse than a declared gap. Figures are marked UNREPRODUCED, not withdrawn; nothing downstream depends on them; the caveat also appears in §1.3. The reproducible half recomputes here: **116 transitions, 116 continuous, zero breaks** |
| 30 | V04 R1 | **`M6` — a visible TDI panel is unrecorded.** Curated frames 21 (`01-04-10`) and 22 (`01-08-40`) each render a sub-panel titled **`Traders Dynamic Index Visual`** with its parameter list and cyan volatility bands — the very object condition (c) refers to — on the guest's platform. Both frames are otherwise described in detail. **This does not weaken `A-039`**: displayed is not taught, and no settings or decision rule is recoverable. Add to `INDEX.md` and to `A-039`'s evidence table scoped *"displayed, not taught"*; as descriptive evidence under the item-22 ruling it also settles that "TDI" denotes the **Traders Dynamic Index**, which no line of V01–V04 audio states | `04_SCREENSHOTS/V04/INDEX.md`; `A-039`; `V04_REVIEW_R1.md` M6 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** Recorded in `INDEX.md` on both frame rows and as a new §"What the visuals added" item 7, and in `A-039`'s evidence table as two rows tagged **`GUEST`, DESCRIPTIVE ONLY**, each scoped **"displayed, not taught"** with an explicit statement that they do **not** narrow `A-039` — guest evidence may extend a record and may never close it (`D-025`). The frames were opened and magnified before the descriptions were written: the six-value numeric readout beside each panel title is **not legible** at this resolution and is deliberately **not transcribed**. `A-039`'s *"the example chart carries no TDI panel"* line is now scoped to the instructor's own Segment-A chart, which is what it always meant ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Both frames opened and magnified before the new text was read. The `Traders Dynamic Index Visual` panel, its coloured lines and its bands are on both frames as described. **The six-value readout is genuinely at the edge of legibility — declining to transcribe it was the right call** and saying so in the index beats a guess or a silent omission. "Displayed, not taught" is accurate on the merits: no inputs, periods, band construction or decision rule is recoverable. Beyond what was asked, `A-039`'s *"the example chart carries no TDI panel"* line is now correctly scoped to the instructor's Segment-A chart |
| 31 | V04 R1 | **`M7` — four quality-control boxes unchecked and undeclared**: concept library, positive / negative / borderline examples. `08_CONCEPT_LIBRARY/` and all four `09_CHART_EXAMPLES/` subdirectories are empty four lessons in. `MASTERY_STANDARD.md` requires unchecked boxes to be *stated*. **Shared with V02 and V03, not a V04 lapse** — but V04 is the first lesson with a complete entry rule and a body of named terms, so the library should begin here. **Raise the underlying debt at `CUMULATIVE_25.md`** | `MASTERY_STANDARD.md`; `V04_REVIEW_R1.md` M7 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** New **QUALITY-CONTROL CHECKLIST** section in `V04_MASTERY_REPORT.md`: of nineteen boxes, **13 checked, 2 `DEFERRED`** (manual chart testing and failed-valid-setups, both blocked by `A-039` and stated rather than ticked), **4 UNCHECKED and declared** with a reason each. The concept-library box is explicitly **not** excused by `A-039` — unlike the three example boxes it was performable and was not done. **The project-wide instance is still owed at `CUMULATIVE_25.md`** — V02's and V03's reports omit the same four boxes ✅ **CLOSED — VERIFIED at R2 2026-08-11.** All 19 `MASTERY_STANDARD.md` boxes accounted for: **13 checked + 2 `DEFERRED` + 4 UNCHECKED**. Declarations true against the repository (`09_CHART_EXAMPLES/` subdirs hold only `.gitkeep`; `CONCEPT_INDEX.md` reads `CONCEPTS: 0`). Notably **refuses to excuse the concept-library box** by pointing at `A-039`, and argues the two `DEFERRED` boxes rather than ticking them |
| 32 | V04 R1 | **`N1` — dimensions B and C are mis-dispositioned.** Graded `PARTIAL` and `FAIL` for one reason: condition (c)'s indicator has never been taught. That is `D-019`'s definition of **`DEFERRED`**, not a failure of mastery. **As labelled, V04 can never reach `PASS`**, because the cause sits in the source and will not change until TDI is taught — the same trap `D-018` was written to escape for dimensions F and G, arriving now for B and C. Re-disposition as `DEFERRED — blocked by A-039`, retaining the present honest text beneath the new label. **`NOT APPLICABLE` is not available and must not be used** | `V04_MASTERY_REPORT.md` B, C; `DECISIONS.md` D-019; `V04_REVIEW_R1.md` N1 | ✅ **APPLIED 2026-08-11 — PENDING VERIFICATION at R2.** **B `PARTIAL` → `DEFERRED`, C `FAIL` → `DEFERRED`**, both labelled *"blocked by `A-039`"* under `D-019`, with the original text retained **verbatim** beneath the new label and a dated note giving the mechanical reason (a `FAIL` whose cause sits in the source can never be cleared by studying). `NOT APPLICABLE` explicitly declined. Both are carried in `CARRIED FORWARD` as open items alongside the manual-backtest debt, to be performed in the lesson that teaches TDI ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Checked against `D-019`'s own V01 F/G worked example, not the label: subject matter exists, `NOT APPLICABLE` explicitly declined, blocker is a missing prerequisite (`A-039`), items stay **open** and are carried. Original `PARTIAL`/`FAIL` prose retained **verbatim** — diffed, not eyeballed; not one word of body text changed |
| 33 | V04 R1 | **The `RULES.md` fabrication audit is a SOLVED PROBLEM for V05–V21 — a time-saver, recorded so it is not re-discovered 17 times.** Verified at full population this round: all 21 files carry both template quotes at `[00:05:00]` and `[00:18:00]`, exactly two rules each, **and a byte-identical `NUMERICAL PARAMETERS` block (one hash, 21/21)**; `INFERRED VISUAL RULES` and `TERMS` have only two variants each across 21 files. A future session may discharge the per-lesson audit in one step by confirming those three markers and citing `V04_REVIEW_R1.md` + `Q-004`. **No `RULES.md` in this library can come back clean.** `NOTES.md` and `VISUAL_INDEX.md` are **NOT** covered — all 21 of each are pairwise distinct and still require per-lesson examination | `QUARANTINE_REGISTER.md` Q-001…Q-004; `V04_REVIEW_R1.md` | OPEN — informational, no action owed |
| 34 | V04 R2 | **`m1` — the *"§3.3 windows are identical"* justification is true for one window and false for the other** (`E20`). Both `V04_HOMEWORK.md` §1.2 (M1 correction block) and `V04_MASTERY_REPORT.md` §"Was any conclusion affected?" state that *"the extreme's index and the 44-bar window shifted together by exactly four bars, so the bars examined are the same bars"*. True for USDCHF's **high**-side window (`j_hi` 363→359, bar-for-bar identical); **false for the low-side one** — `j_lo` 4→0 was clipped at the head of the array in **both** datasets, so it went from 5 bars (four of them previous-week bars) to 1 and could not "shift". **The descriptor row it justifies is genuinely unchanged — 1/1/1/1 across all four tolerances on both datasets, recomputed at R2** — the direction is safe (the new window correctly excludes out-of-week bars) and nothing downstream reads the justification. Charged because it is one more instance of R1's `N5` pattern, produced in the commit that quoted `N5` approvingly | `V04_HOMEWORK.md` §1.2; `V04_MASTERY_REPORT.md`; `18_REVIEW/V04/V04_REVIEW_R2.md` §4 | 🔧 **OPEN — NON-BLOCKING, deferred by design.** Fix the mechanism clause whenever either file is next edited: the high-side window is bar-for-bar identical; the low-side window was clipped at the array head in both datasets and now correctly excludes the four previous-week bars it previously contained; both descriptor rows are unchanged, recomputed. **Do NOT open an R3 for this** — `REVIEW_PROTOCOL.md` §9 criterion 14 and the `V02_REVIEW_R3.md` precedent (`PASS` with non-blocking documentation-precision minors); §16 forbids the artificial extra round |
---

## HUMAN REVIEW QUEUE

| # | Lesson | Issue | Why a human is needed | Status |
|---|---|---|---|---|
| _(none)_ | | | | |

---

## CUMULATIVE REVIEWS

| Checkpoint | Trigger | File | Status |
|---|---|---|---|
| 25% | TBD at ingestion | `CUMULATIVE_25.md` | Not started |
| 50% | TBD at ingestion | `CUMULATIVE_50.md` | Not started |
| 75% | TBD at ingestion | `CUMULATIVE_75.md` | Not started |
| Final | All lessons passed | `FINAL_COURSE_REVIEW.md` | Not started |

---

## REVIEW FILE LOCATIONS

```text
18_REVIEW/VXX/VXX_REVIEW_R1.md
18_REVIEW/VXX/VXX_REVIEW_R2.md
```

Never overwrite a round (`SETUP_ISSUES.md` I-002).
