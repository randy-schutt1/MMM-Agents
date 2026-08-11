# REVIEW INDEX

Master record of every independent review decision, and the project's running
error statistics.

Maintained by the Reviewer Agent. Append-only for decisions — a superseded decision
stays visible with its round number.

---

## STATUS

```text
LESSONS REVIEWED: 3
PASSED:           2  (V01, V02)
IN REMEDIATION:   1  (V03 — REVISE, minors only; V04 gate OPEN per D-024)
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
| E01 | Source misquote | 1 | V02 (R1 ×1) — two ASR garbles repaired inside quotation marks |
| E02 | Unsupported generalization | 4 | V01 (R1 ×1, R2 ×2) — all closed at R3; V03 (R1 ×1 — duration finding scoped 4-of-4 where 2-of-4 is supported, open as M3) |
| E03 | Missed qualifier | 0 | |
| E04 | Wrong sequence | 0 | |
| E05 | Wrong pattern boundary | 0 | |
| E06 | False positive | 1 | V02 (R1 ×1, also codes `E19`) — homework markup contradicts its own chart |
| E07 | False negative | 0 | |
| E08 | Hindsight contamination | 0 | |
| E09 | Cherry-picking | 0 | |
| E10 | Incomplete homework | 1 | V01 |
| E11 | Missing provenance | 9 | V01 (R1 ×1, R2 ×4, R3 ×4) — 8 closed at R3, 1 carried (open item 7) |
| E12 | Ambiguity treated as rule | 0 | |
| E13 | Contradiction ignored | 1 | V01 |
| E14 | Outcome confused with correctness | 0 | |
| E15 | Machine assumption introduced prematurely | 0 | |
| E16 | Terminology drift | 0 | |
| E17 | Missing negative examples | 0 | |
| E18 | Invalid manual-backtest procedure | 0 | |
| E19 | Data/timeframe inconsistency | 2 | V02 (R1 ×1 as a co-code with `E06` — closed at R2; R2 ×1 — day boundary off by one bar, open); V03 (R1 ×1 — ADR figures not reproducible from committed data, open as M1) |
| E20 | Other | 16 | V01 (R1 ×6, R2 ×2, R3 ×1) — all closed at R3; V02 (R1 ×4) — closed at R2; V02 (R2 ×2) — open; V03 (R1 ×1 — transcript coverage block overclaims "strictly monotonic, no duplicates", open as M2) |

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

| Severity | Total | Open | Closed |
|---|---:|---:|---:|
| CRITICAL | 0 | 0 | 0 |
| MAJOR | 4 | 0 | 4 |
| MINOR | 21 | 8 | 13 |
| NOTE | 22 | 4 | 18 |

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

| 18 | V03 R1 | **M1 — homework ADR figures not reproducible.** State the day-boundary convention and commit the five per-pair daily ranges (or recompute under a stated convention). The 0-of-4 conclusion survives every convention tried | `V03_HOMEWORK.md` §2.5 Finding B; `18_REVIEW/V03/V03_REVIEW_R1.md` M1 | OPEN |
| 19 | V03 R1 | **M2 — transcript coverage block overclaims.** "Strictly monotonic, no duplicates" is false: three benign same-second adjacent duplicate markers (`[00:35:21]`, `[01:00:13]`, `[01:04:30]`); sequence is non-decreasing. Fix the wording | `V03_TRANSCRIPT.md` COVERAGE; `V03_REVIEW_R1.md` M2 | OPEN |
| 20 | V03 R1 | **M3 — duration finding over-scoped.** "4 of 4 exceed the 2.5–3-day window" counts two pairs (USDJPY, USDCHF) whose low is the week-open bar with no formed anchor — supported sample is 2 of 4 (both 3.8 days, still exceeding). Scope it in homework §2.5A and mastery report §2 before it is cited against `C-001` | `V03_HOMEWORK.md` §2.5; `V03_MASTERY_REPORT.md` §2; `V03_REVIEW_R1.md` M3 | OPEN |
| 21 | V03 R1 | **N4 — manual-backtest debt, three lessons deep.** Each deferral individually sound (no testable entry rule yet), but the obligation accrues: when the first testable rule lands (plausibly the V03 exit once A-033 "outside structure" is defined), the hidden-future backtest backlog must be discharged against it. The reviewer will require it | `V03_REVIEW_R1.md` N4; `06_MANUAL_BACKTEST/` | OPEN |

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
