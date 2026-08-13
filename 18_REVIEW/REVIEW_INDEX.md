# REVIEW INDEX

Master record of every independent review decision, and the project's running
error statistics.

Maintained by the Reviewer Agent. Append-only for decisions — a superseded decision
stays visible with its round number.

---

## STATUS

```text
LESSONS REVIEWED: 7
PASSED:           6  (V01, V02, V03, V04 — V04 PASS at R2, COMPLETE;
                      V05 — PASS at R3 2026-08-12, COMPLETE;
                      V06 — PASS at R2 2026-08-13, COMPLETE.)
IN REMEDIATION:   1  (V07 — R1 REVISE 2026-08-13, 0 CRITICAL / 0 MAJOR /
                      3 MINOR (open items 61-63). ALL THREE APPLIED
                      2026-08-13 on branch fix/v07-r1-minors (D-038),
                      PENDING VERIFICATION at R2 -- superseded text
                      retained in place per REMEDIATION_PROTOCOL.md §2 at
                      all three sites. Nothing is self-certified: D-003
                      reserves verification to an independent reviewer,
                      and this remediation session neither re-reviewed
                      nor closed anything. Gate to V08 remains OPEN under
                      D-024. V07 reaches COMPLETE only at R2. Dimension B
                      was SCORED, not carved out: NOT SATISFIED, blocked
                      by D-030, structural and not attributable to the
                      student, carrying NO severity charge -- UNCHANGED by
                      this remediation. No owner directive was issued for
                      this round -- open item 36 is now owed for the THIRD
                      lesson running.)
AWAITING REVIEW:  0  (V07 R2 is triggered: the remediation of items 61-63
                      is complete and submitted for verification.)
```

> *(Superseded STATUS text, retained — between V07's R1 and this remediation the
> `IN REMEDIATION` entry read `3 MINOR (open items 61-63). Gate to V08 OPENS under D-024 — the
> minors are deferred and still owed, and V07 reaches COMPLETE only at R2.` with `AWAITING
> REVIEW: 0` unqualified. The three minors are no longer deferred; they are applied and owed
> **verification**.)*

> *(Superseded STATUS text, retained — between V06's R2 and V07's R1 this block read
> `LESSONS REVIEWED: 6` / `PASSED: 6 (… V06 — PASS at R2 2026-08-13, COMPLETE. Dimension B
> carried as "blocked by D-030, excluded from pass/fail per owner directive". V07 gate OPEN.)`
> / `IN REMEDIATION: 0` / `AWAITING REVIEW: 0`.)*

> *(Superseded STATUS text, retained — between V06's R1 and R2 this block read
> `IN REMEDIATION: 1 (V06 — R1 REVISE 2026-08-13, 0 CRITICAL / 1 MAJOR / 3 MINOR
> (open items 57-60). Gate to V07 CLOSED under D-024 pending remediation of the
> MAJOR and re-review. Dimension B blocked by D-030 ("push" undefined), EXCLUDED
> from pass/fail per owner directive — it is not what holds the gate.)`. R2
> verified items 57-60 closed the same day; the item-57 sweep surfaced one further
> MINOR (M5), fixed and verified in-round. Same-session remediation and re-review
> were owner-directed and are disclosed in `V06_REVIEW_R2.md`'s header;
> `CUMULATIVE_25.md` should independently re-sample this round.)*

> *(Superseded STATUS text, retained — before V06's R1 this block read
> `LESSONS REVIEWED: 5` / `IN REMEDIATION: 0` / `AWAITING REVIEW: 0`.)*

> *(Superseded STATUS text, retained — before V05's R3 PASS this block read:
> `PASSED: 4 (V01, V02, V03, V04 — V04 PASS at R2, COMPLETE)` /
> `IN REMEDIATION: 1 (V05 — R2 REVISE, 0 CRITICAL / 0 MAJOR / 5 MINOR. R1
> REVISE (0/0/6) + R1B REVISE (0/0/4, parallel second opinion in the same
> round) = 10 R1-round minors. R1's 6 VERIFIED APPLIED at R2 and CLOSED; open
> item 39 (EMA 3 -> 2) APPLIED AT R2 and CLOSED; R1B's 4 + its note n1 are
> CONFIRMED VALID and were adopted as M7-M11 -> open items 47-51; ALL FIVE
> (M7-M11) APPLIED 2026-08-11, PENDING R3 VERIFICATION, with the M11
> marker-existence sweep run and CLEAN (no fourth cluster member); the
> dimension-B re-disposition remains blocked on an owner ruling (open item
> 36); V06 gate OPEN under D-024)`. R3 verified all five applied, re-derived
> from source, and re-ran the sweep independently; the dimension-B/G
> re-labelling stays owner-blocked on open item 36 and does not gate.)*

**V05 review lineage — four files, two rounds of remediation, closed at R3.**
`V05_REVIEW_R1.md` (`c41e686`) and `V05_REVIEW_R1B.md` (`8403914`) are **two independent
reviews of the same round**, produced concurrently by duplicate sessions; R1B declined to
overwrite R1 and named itself accordingly (`SETUP_ISSUES.md` I-002, `REVIEW_PROTOCOL.md` §11).
R1B was committed but **never indexed** — it was referenced zero times in this file and zero
times in `LOG.md` — so the remediation at `152f4ea` addressed R1's six minors only.
`V05_REVIEW_R2.md` verifies those six, applies open item 39, and **folds R1B into this lineage**:
its four findings plus its note `n1` are adopted as `M7`–`M11` (open items 47–51), its body is
**unedited and NOT marked invalid** (all five reproduce against `HEAD`), and an append-only
status footer points readers here. **`V05_REVIEW_R2.md` was the operative list of what V05
owed; `V05_REVIEW_R3.md` (2026-08-12) verifies all five applied — each re-derived from
primary source, the `M11` marker-existence sweep re-run independently and clean, frame 26's
disputed left label read a third time and upheld as *value not legible* — and closes V05 at
`PASS` (0 critical / 0 major / 0 minor).** The dimension-B/G re-labelling stays
owner-blocked (open item 36) and does not gate. Whether parallel reviews become policy is an
owner decision.

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

V05 reviewed 2026-08-11 (R1): **`REVISE`**, confidence HIGH. **0 critical, 0 major, 6 minor,
5 note** — under D-024 the **V06 gate is OPEN**, with the minors owed before V05 reaches
`COMPLETE`. Reviewed by a fresh session that authored no V05 artifact (`D-003`).

**The concurrency scare is unfounded and the repository needs no cleanup.** This round was
told V05 might carry duplicated or conflicting content from several sessions running the task
at once. Verified at the repository level first: `HEAD` is `b4b690b` with **no commits beyond
it**, the pipeline is exactly **nine** commits in correct protocol order, and the two findings
described as possible separate additions (`Zen_man`, the on-screen session date) are **inside
`8223224`**, part of the main pipeline. `A-001`…`A-049` and `C-001`…`C-005` are contiguous
with **zero duplicate headings and zero gaps**; no doubled V05 blocks in `LOG.md` or
`CHANGELOG.md`; `validate_project.py` 97/0/0. The one untracked file is open item 13,
correctly left alone.

**Everything load-bearing reproduced under independent measurement.** The transcript's
coverage block is **the first in the project to assert strict monotonicity and be right** —
1,353 markers, 1,353 distinct, zero decreasing transitions, zero same-second pairs, largest
gap 13 s at both named markers, final entry `[01:08:20]`, every component re-derived (V03's
identical claim took three rounds to close, open item 19). The speaker finding was re-counted
(`Steve` **21**, `Zen` **2**, `DMR` **9**, `TDI` **6**, all exact). `C-003`'s strike-off
re-measured: **zero clock-time tokens** in the body. The fabrication quarantine was discharged
at **full population** per open item 33 — both template markers 21/21, exactly two rules
21/21, `NUMERICAL PARAMETERS` **one hash 21/21** — and `Q-005`'s audio cross-check verified
word for word. **356 citations checked, 2 defective; 92 marker-cited quote fragments
re-matched verbatim, 90 exact.** `E11` does not recur as a class.

**The screenshot findings are real and were checked against the pixels, not the prose.**
`Zen_man / System Folder` is unambiguous in the Save As dialog; the taskbar clock reads
**`10:31 PM 3/25/2012`**, which is **the first in-recording corroboration of the session
date**, until now resting on the filename alone; frame 26's status bar (`4 Majors`,
`2012.01.04 01:15`, `O 1.56413 H 1.56418 L 1.56374 C 1.56381 V 352`) reads exactly as
transcribed; and `A-043`'s toolbar dialog shows precisely the two text objects claimed —
**`A Text`** in *Selected*, **`T Text label`** in *Available*.

**The homework answers the data question cleanly and fixes V04's defect at source.** The
harvester was read line by line: it parses TradingView's **Data Window `innerText`** for
`Date/Time/O/H/L/C`; **no pixel is sampled and no colour is tested anywhere.** Every committed
figure recomputed from the JSON and reproduces exactly — **480/480/480/476 bars, 1,912/1,912
continuity with zero breaks, the full `by_day` table, and all eight extremes with prices,
timestamps and pip ranges to the decimal.** Because each bar now carries its own timestamp,
the USDCHF anomaly that broke V04 silently (open item 25) is **caught by the tooling**:
476 = 480 − 4, the missing session hour visible directly in the data, independently
reproducing V04's corrected 476 on a different week, feed and method. The boundary-limited
USDCHF week low is disclosed and the pair excluded from every conclusion depending on it.

**Three rulings were rendered on items the student escalated.** (1) **`A-043`'s closure is
AFFIRMED** (open item 40) — a record whose subject is *a guest's own utterance or a platform
artifact*, not the method, may be closed on descriptive guest evidence; owner should record
the carve-out as a `D-025` refinement so it is a rule rather than a per-record judgement.
(2) **The third-disposition escalation is upheld** (open item 36): dimension **G**'s
`NOT APPLICABLE` stands on the purposive reading — `DEFERRED` would be false, since no future
lesson makes a V05 guest rule testable — but its **stated reason must change** to "excluded by
decision under D-025"; dimension **F** stands as graded; dimension **B**'s `NOT APPLICABLE`
is **not available**, since `D-019` grants it for F and G only (same class as V04 R1 `N1`,
carried the same way as a NOTE with a required action). The reviewer recommends the owner
adopt **`EXCLUDED BY DECISION`** as a third disposition. (3) **The `EMA` 3 → 2 correction is
CONFIRMED** (open item 39) and the fix belongs in `V05_TRANSCRIPT.md` and `Q-005`.

The six minors are precision defects, none of which changes any conclusion — and none could,
because V05 yields no doctrine for a defect to corrupt: the same quote miscited two different
ways in two files, neither a marker (`M1`, `E11`); a citation off by one marker (`M2`); one
smoothed quotation dropping "level three" (`M3`, `E01`); **three V05 files disagreeing about
V05's own evidence order** (`M4`, `E20` — `INDEX.md` discloses the process deviation
prominently and correctly, and `V05_INTERPRETATION.md` line 12 claims the opposite); a stale
"V05 is the next candidate" pointer in `A-039` (`M5`); and an unrecorded oscillator sub-panel
in curated frame 26 (`M6`, the V04 `M6` class exactly).

**Pattern worth carrying to `CUMULATIVE_25.md` — the status-staleness class did NOT recur.**
All four status blocks were checked against their own contents and **all four are current**.
Open item 14 has failed in six previous rounds and is the project's most persistent weakness;
**this is the first clean round**, achieved without the `validate_project.py` guard having
been built. Separately, this round records a reviewer error worth keeping: R1 initially scored
the six record extensions as missing, because they live in a consolidated block at the foot of
`AUTOMATION_AMBIGUITIES.md` (V02's precedent) rather than inside each record. The block is
real, the mastery report's claim is accurate, and the finding was withdrawn before it was
charged — **the third consecutive round in which a reviewer's own first reading failed to
survive its own verification step.**

**The counterfactual is the round's most important observation.** Instructor runtime across
one session date runs **~100% (V03) → ~31% (V04) → 0% (V05)**. A session that skipped speaker
identification would have written an entire lesson of false doctrine — anchor theory, level
assignment, a three-day reversal expectation, an 80% accuracy claim — and every downstream
file would have inherited it. `D-025` consequence 3 was written one lesson before it was
needed. **Open item 38 is upheld and should be read at the start of every remaining lesson.**

V05 reviewed 2026-08-11 (**R1B**): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
4 minor, 4 note.** A **second, independent R1** produced concurrently by a duplicate reviewer
session, which discovered R1 on disk mid-round, **declined to overwrite it** (`SETUP_ISSUES.md`
I-002, `REVIEW_PROTOCOL.md` §11), declined to race another session's uncommitted
`REVIEW_INDEX.md`, and disclosed the collision in full. It agrees with R1 on the verdict, the
gate and every finding R1 raised, and adds four of its own. **It was committed at `8403914`
but never indexed here or in `LOG.md`, so the remediation at `152f4ea` never saw it** — that
omission, not the file, is the single-source-of-truth defect, and it is corrected at R2.
Verified *within that round*: 1,353/1,353 markers; `Steve` 21, all third-person; `Q-005`'s
`VISUAL_INDEX` claim at the byte level (**12/12 SHA-256 pairs, 15 distinct images across 27
files**); all thirty ASR-garble citations; every homework figure from the committed JSON. **R2
did not re-run those** (`V05_REVIEW_R2.md` §4) — two independent confirmations already agree.
**What R2 did re-derive is R1B's five findings, and all five reproduce. Folded into the R1/R2
lineage at R2** — findings adopted as `M7`–`M11`, body unedited,
**not marked invalid**, append-only status footer added.

V05 re-reviewed 2026-08-11 (R2): **`REVISE`**, confidence HIGH. **0 critical, 0 major,
5 minor** — the V06 gate **remains OPEN** under D-024, and V05 is **NOT COMPLETE**.

**All six of R1's minors verify, re-derived from source rather than from the diff.** `M1` both
citations corrected to `[00:57:35]`–`[00:57:36]` and **split across the two markers the words
actually span**; `M2` corrected to `[00:36:05]` with that marker's literal sentence replacing
the smoothed fragment; `M3` restored verbatim with the elision removed rather than annotated —
the excised level number is back inside the file's own evidence for the level↔day relabelling;
`M4` reconciled **toward the honest file** — `V05_INTERPRETATION.md` now leads with the
deviation and names `INDEX.md` as governing, and `git show` confirms `INDEX.md` was **not
weakened** (one line touched, row 26, for `M6`); `M5` the stale TDI pointer updated with
*"a name is not a definition"*; `M6` frame 26's oscillator sub-panel recorded as **presence
only**, the illegible header verifiably **not** transcribed. **Zero scope creep, superseded
text retained at every site, and the two refusals were in the right direction.** Open item 39
(`EMA` 3 → 2) was re-derived a third time and **applied this round** at both sites — a declared
`D-003` deviation, scoped to two numerals, recorded at `V05_REVIEW_R2.md` §3.1.

**`PASS` was withheld for one reason: R1B's findings are real and none has been applied.**
All four plus its note `n1` were re-derived at R2 from the transcript and the pixels,
independently of R1B's prose, and **all five reproduce at `HEAD`** — adopted as `M7`–`M11`,
open items 47–51. `M7` is the consequential one: `CONTRADICTIONS.md`'s **STATUS block** states
that `C-003` — *"whether M and W formations can fail"* — was checked against V05 and struck
off, when the record checked was `C-004` and `C-003` contains no V05 text at all. **That also
retires R1's `N5` superlative** that all four status blocks were current; the improvement it
described is real, the superlative is not. `M11` shows R1's `M1` fixed two thirds of a single
defect — all three V05 citation errors map `00:57:3x` → `01:0x:3x`, one displaced cluster, and
a mechanical marker-existence sweep is owed with the fix.

**The honest summary: V05's understanding passed and V05's bookkeeping did not.** Across three
independent rounds V05 has drawn **ten minors, zero major, zero critical**, and every one lives
in counting, citing or cross-referencing — **not one touches what V05 was understood to mean.**
Its single load-bearing claim, *that the method is not in this lesson*, has now survived three
separate audits of the audio, the frames, the committed data and the registers. **Five small
corrections and an R3 verification pass and this lesson is `COMPLETE`.** Dimension B's
re-disposition remains **blocked on the owner** (open item 36) and is carried, not charged.

V05 re-reviewed 2026-08-12 (R3): **`PASS`**, confidence HIGH. **0 critical, 0 major,
0 minor** — **V05 is `COMPLETE`.** All five of R2's minors (`M7`–`M11`, open items 47–51)
verified applied, each **re-derived from primary source before the remediation diff was
read**: `M7`'s four `C-003`→`C-004` sites with superseded text retained and `C-004` still
`UNRESOLVED`; `M8`'s *"but up to five days"* re-counted at exactly two; `M9`'s frame-26
labels re-read from fresh 10× crops — `40.9` / `40.6` / `41.1` confirmed, and **the disputed
left label upheld as *value not legible* on a third independent read** (R1B's `74.6` stays
untranscribed); `M10`'s §4c framing verified two-of-four row by row; `M11`'s `A-042`
citation verified at `[00:57:39]`. **The `M11` marker-existence sweep was re-run from
scratch this round** — 1,353 markers, 7 non-resolving citations, all seven accounted for
(six cross-lesson cites, one burned-in slide time); **the displaced cluster is closed at
three.** The post-R2 merge (`9ad57b8`) touched no V05 artifact — verified by diff. The
dimension-B/G re-labelling stays owner-blocked (open item 36) and does not gate
(`REVIEW_PROTOCOL.md` §9 criterion 14; §1 forbids holding a lesson on an owner-blocked
label). Owner actions from R2 §5 (open items 35, 36, 40; R1B naming; parallel-session
ruling) are carried forward unchanged. **The next review trigger is the V06 submission, or
`CUMULATIVE_25.md` if that milestone arrives first.** `V05_REVIEW_R3.md`.

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
| V05 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |
| V05 | REVIEW REQUIRED | R1B | REVISE | 0 | 0 | ⏳ |
| V05 | REMEDIATION APPLIED | R2 | REVISE | 0 | 0 | ⏳ |
| V05 | REMEDIATION APPLIED | R3 | **PASS** | 0 | 0 | ✅ COMPLETE |
| V06 | REVIEW REQUIRED | R1 | REVISE | 0 | 1 | ⏳ |
| V06 | REMEDIATION APPLIED | R2 | **PASS** | 0 | 0 | ✅ COMPLETE |
| V07 | REVIEW REQUIRED | R1 | REVISE | 0 | 0 | ⏳ |

> **`R1B` is a parallel second opinion on the R1 round, not a separate round of remediation.**
> It is listed so the decision history is complete; the two R1-round rows describe **one**
> submission audited twice. R2 is the first remediation-verification round.

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
| E01 | Source misquote | 5 | **V07 (R1 ×1 — `M3`, co-code `E11`, APPLIED 2026-08-13, pending R2 verification, open item 63):** `V07_MASTERY_REPORT.md` §D renders `[00:28:31]`'s *"if it doesn't do what you expect **in** your flashcard isn't the same"* as *"…**and** your flashcard…"* — a silent smoothing of a garbled ASR passage inside quotation marks, **and** cited to `[00:28:28]`, which exists and carries a different sentence. **The defect falsifies §H's own categorical claim** *"No quotation mark in any V07 artifact contains a word that is not in the source"*. **Counterweight, measured:** this reviewer machine-checked **239 marker-cited quotes across seven V07 artifacts and this is the only defect in the set** — the narrative-prose-vs-evidence-table pattern (V04 `M2`, V05 `M3`) holds, and `V07_SOURCE_NOTES.md` §6c renders the same passage correctly | **V05 (R1B ×1 — `M8`, APPLIED 2026-08-11, pending R3 verification, open item 48):** `V05_MASTERY_REPORT.md` §E counts the verbatim string *"but up to five days"* **four times**; it occurs **twice**. **Third live instance of the verbatim-count class** (open items 15, 39) — three is `REVIEW_PROTOCOL.md` §7's escalation threshold, raise at `CUMULATIVE_25.md`. **V05 (R1 ×1 — `M3`, ✅ CLOSED — VERIFIED at R2 2026-08-11, open item 43):** `V05_SOURCE_NOTES.md` §4b renders *"…and **level three** second leg of that pattern…"* `[00:13:05]` as *"**the** second leg of that pattern…"*. Third occurrence overall and **second consecutive lesson** — both times inside supporting prose rather than the notes proper. Not an escalation trigger on its own, but the pattern is now "quotations in narrative paragraphs are less reliable than quotations in evidence tables", which is `N5`'s class from V04 R1 in a new guise. V02 (R1 ×1) — two ASR garbles repaired inside quotation marks; V04 (R1 ×1 — `M2`, **✅ CLOSED — VERIFIED at R2 2026-08-11** — both fragments restored to the adopted transcript's literal wording and the quoted side of the comparison stated: two of the six "matched near-verbatim" spot-check fragments in `V04_TRANSCRIPT.md` criterion 2 are smoothed readings, not the adopted wording. **The student self-caught and fixed ~20 instances of this class in its own draft before commit and the fix verifies** — an independent 320-fragment audit at R1 found only these two survivors, both in the provenance narrative rather than in the notes) |
| E02 | Unsupported generalization | 5 | **V05 (R1B ×1 — `M10`, APPLIED 2026-08-11, pending R3 verification, open item 50):** `V05_SOURCE_NOTES.md` §4c heads its table *"Repeated four times, always with the same escape clause"*; two of the four rows carry none. **The origin of `M8`** — a framing sentence becoming a false verbatim count one file downstream. V01 (R1 ×1, R2 ×2) — all closed at R3; V03 (R1 ×1 — duration finding scoped 4-of-4 where 2-of-4 is supported, M3 — **applied 2026-08-10, pending verification at R2**) |
| E03 | Missed qualifier | 0 | |
| E04 | Wrong sequence | 0 | |
| E05 | Wrong pattern boundary | 0 | |
| E06 | False positive | 1 | V02 (R1 ×1, also codes `E19`) — homework markup contradicts its own chart |
| E07 | False negative | 1 | **V06 (R1 ×1 — `M1`, `MAJOR`, co-code `E11`, open item 57):** frame `V06_00-48-29` Week 10 prints *"and more specifically at 3:45am or 9:45am est."* — legible at committed resolution, elided in the frame-26 transcription as "not legible", and its absence then asserted as *"no session clock appears on any of the 32 frames"* in both `04_SCREENSHOTS/V06/INDEX.md` and `V06_SOURCE_NOTES.md` §11d. First printed `est` in the corpus evidence; bears on `A-019` and `A-030`. The audio-scoped §10 claim (`EST` 0× spoken) is true and unaffected |
| E08 | Hindsight contamination | 0 | |
| E09 | Cherry-picking | 0 | |
| E10 | Incomplete homework | 1 | V01 |
| E11 | Missing provenance | 13 | **V07 (R1 ×1 — `M3` co-code, APPLIED 2026-08-13, pending R2 verification, open item 63):** `V07_MASTERY_REPORT.md` §D cites `[00:28:28]` for words that are at `[00:28:31]` — open item 7's class exactly (the neighbouring marker rather than the one the sentence's first words fall under). **The class is otherwise in excellent health and the de-escalation holds:** a mechanical marker-existence sweep over all seven V07 artifacts resolved **300 distinct citations**, with every non-resolving hit declared in advance by the student — `[00:21:35]` and `[00:34:50]` are screenshot timestamps, `[00:30:22]` and `[00:38:19]` are labelled **V04** markers. The transcript header carries its own pre-submission sweep block, which is V05 R2's `M11` discipline applied **before** review rather than after | **V05 (R1B ×1 — `M11`, APPLIED 2026-08-11, pending R3 verification, open item 51):** `A-042` cites `[01:01:39]`, not a marker; the words are at `[00:57:39]`. **Third member of one displaced cluster** — all three V05 citation defects map `00:57:3x` → `01:0x:3x`, so `M1`'s fix closed two thirds of a single defect. A mechanical marker-existence sweep is owed with the fix. **V05 (R1 ×2 — `M1`, `M2`, both ✅ CLOSED — VERIFIED at R2 2026-08-11, open items 41–42):** the *"I use E and I use the box"* quote cited at `[01:07:36]` in `V05_SOURCE_NOTES.md` and at `[01:01:35]` in `A-043` when it is at `[00:57:35]`–`[00:57:36]` — **two different wrong timestamps for one quote, neither a marker**; and `A-039`'s extension row citing `[00:36:03]` where the words are at `[00:36:05]`. **The de-escalation HOLDS**: 356 V05 citations were checked and 354 resolve, with 92 marker-cited quote fragments re-matched verbatim (90 exact). Two isolated instances, not a recurrence of the class. V01 (R1 ×1, R2 ×4, R3 ×4) — 8 closed at R3, 1 carried (open item 7). **DE-ESCALATED at V04 R1** — absent for a third consecutive lesson: V04's 487 cited markers were independently re-checked and **487 resolve** (V04 `M3` is a wrong *ambiguity-record* pointer, co-coded `E20`, not a wrong timestamp) |
| E12 | Ambiguity treated as rule | 0 | |
| E13 | Contradiction ignored | 1 | V01 |
| E14 | Outcome confused with correctness | 0 | |
| E15 | Machine assumption introduced prematurely | 0 | |
| E16 | Terminology drift | 0 | |
| E17 | Missing negative examples | 0 | |
| E18 | Invalid manual-backtest procedure | 0 | |
| E19 | Data/timeframe inconsistency | 2 | V02 (R1 ×1 as a co-code with `E06` — closed at R2; R2 ×1 — day boundary off by one bar, open); V03 (R1 ×1 — ADR figures not reproducible from committed data, M1 — **✅ CLOSED at R2 2026-08-10**: all twenty daily ranges and all four ADR figures re-derived exactly from the raw JSON under the stated 21:00-UTC convention); V04 (R1 ×1 — `M1`, **✅ CLOSED — VERIFIED at R2 2026-08-11** — partial 12-bar week-open 4h bar diagnosed and the slice corrected to 476 bars; 474/480 → 476/480; `bars_15m_in_4h_bar_0` and `verify_reconstruction.py` committed: USDCHF's 15-minute series is mis-sliced at a partial week-open bar, and the 27/30 reconstruction symptom was attributed to ±0.4 pip harvest noise when bar 0's open differs by **28.1 pips**. No conclusion changes; the 4h data is clean at 116/116) |
| E20 | Other | 32 | **V07 (R1 ×2 — `M1`, `M2`, both `MINOR`, count class, APPLIED 2026-08-13, pending R2 verification, open items 61–62):** `V07_SOURCE_NOTES.md` §10's table of "measured negatives" carries two wrong counts. `M1` — the *level* row states **26 uses**; the true count is **56** (`level` 53 + `levels` 3), the `level <N>` compound is 35, and entries containing the token are 44, so 26 matches nothing — **and §5 of the same file states 56 correctly**, so one file holds a right record and a wrong record for the same object fourteen sections apart (the V05 `M4` intra-file-disagreement class layered on the count class). `M2` — the *"the peak"* row states **4×** and then lists **five** markers; the true count is **5**, and the listed markers are all correct, so the row is internally inconsistent on its face. **Both conclusions are unaffected and, in `M1`'s case, understated.** Charged because §10's own preamble states the counts are given *"so a reviewer can falsify them cheaply"* — the invitation was taken and two cells falsified. **Sixth and seventh instances of the count class (open items 15, 39, 48, 58, 59) — it is now the single most durable defect class in the project and is well past `REVIEW_PROTOCOL.md` §7's threshold. Raise at `CUMULATIVE_25.md` together with V06 R2 `M5`'s one-ledger-per-lesson proposal, which would fix both classes at once** | **V06 (R2 ×1 — `M5`, ✅ CLOSED IN-ROUND at `4c89db1`):** `V06_SOURCE_NOTES.md` §11b's R-label cell carried **five wrong values of eight claims** (21.1→31.1; a 24.3 attributed to `V06_00-15-49`, which carries 80.6/41.5; 47.3→67.3; 38.8→80.6; 26.9→28.9), disagreeing with `04_SCREENSHOTS/V06/INDEX.md` and the `A-018` register row (both correct) on the same frames — the V05 R1B `M9` evidence-value class plus the V05 `M4` cross-file-disagreement class in one finding. Surfaced by R1 item 57's required frame sweep; corrected with superseded text retained; `A-018`'s negative conclusion survives the corrected value set. **Third consecutive round with a small-printed-value defect — raise the one-ledger-per-lesson rule at `CUMULATIVE_25.md`** | **V06 (R1 ×3 — `M2`, `M3`, `M4`, all `MINOR`, open items 58–60):** `M2` the transcript header's *"Steve occurs 25 times, 23 + 2"* is irreproducible — 26 tokens measured, and a **third** read-aloud instance (`[01:11:39]`, inside the Isubio quotation) is unclassified; speaker-identification conclusion unaffected and strengthened. **Token/verbatim-count class again (open items 15, 39, 48) — already at the escalation threshold, raise at `CUMULATIVE_25.md`.** `M3` the *already-corrected* `Asian`/`Asia` row in `V06_SOURCE_NOTES.md` §10 is still miscounted: `Asia` is 2× (`[00:50:25]`, `[01:09:55]`), not 1×. Same class. `M4` the `D-033` propagation (`612f431`, *"every place they change"*) did not touch the five live `D-025` fences in the V06 lesson artifacts themselves (transcript header, source notes, interpretation, homework, screenshot index) — each still states superseded prohibitions in present tense; status-staleness class, open item 14. | **V05 (R1B ×2 — `M7`, `M9`, both APPLIED 2026-08-11, pending R3 verification, open items 47, 49):** `M7` the V05 contradiction check that was actually run against `C-004` is named `C-003` at four sites including `CONTRADICTIONS.md`'s **STATUS block** — the record named contains no V05 text at all, and this retires R1's `N5` claim that all four status blocks were current; `M9` four printed `R =` labels unrecorded in curated frame 26, leaving `A-018`'s *"V05 adds four more labels"* an undercount of at least half — **the same frame and the same class as `M6`**. **V05 (R1 ×3 — `M4`, `M5`, `M6`, all ✅ CLOSED — VERIFIED at R2 2026-08-11, open items 44–46):** `M4` three V05 files disagreeing about V05's own evidence order, with `INDEX.md` disclosing the deviation correctly and `V05_INTERPRETATION.md` line 12 claiming the opposite — **a new sub-class: not stale text, but two files written in the same session asserting contrary things about that session's own process**; `M5` `A-039`'s *"V05 is the next candidate"* pointer left stale by the lesson that answered it — **eighth instance of the status-staleness class (open item 14), and the only staleness this round**; `M6` an unrecorded oscillator sub-panel in curated frame 26, the V04 `M6` class exactly. **Counterweight worth recording: V05 is the FIRST round in which all four STATUS blocks were current** (`AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `COURSE_PROGRESS.md`, `REVIEW_INDEX.md`), verified by re-deriving each against its own file's contents. Open item 14 has failed in six previous rounds; this one is clean, and it was achieved **without** the proposed `validate_project.py` guard existing. V01 (R1 ×6, R2 ×2, R3 ×1) — all closed at R3; V02 (R1 ×4) — closed at R2; V02 (R2 ×2) — open; V03 (R1 ×1 — transcript coverage block overclaims "strictly monotonic, no duplicates", M2 — **✅ CLOSED at R3 2026-08-10**: applied to the `PROVENANCE` I-008 criterion at `683a12a` and to the `COVERAGE` block at `492bb11`; both blocks now assert the same true proposition, re-derived component by component at R3. Carried as R2 M2′, never double-counted — one occurrence, remediated in two commits. The **monotonicity class is now empty project-wide**: V01 makes no such claim, V02 is genuinely strict (1,026 / 1,026), V04 states the weaker true property) | **V04 (R1 ×5 — all ✅ CLOSED — VERIFIED at R2 2026-08-11):** `M3` two ambiguity cross-references in `V04_TRANSCRIPT.md` pointing at `A-037`/`A-038` where the register holds `A-031`/`A-030` (co-codes `E11`); `M4` stale "26 frames" (27 exist) and stale `VISUAL_INDEX` filename — **sixth and seventh instances of the status-staleness class, open item 14**; `M5` homework validation 1's 569/549/20 continuity figures not reproducible from committed data (same promise as open item 13); `M6` a visible `Traders Dynamic Index Visual` panel in curated frames 21 and 22, unrecorded in `INDEX.md` and in `A-039`; `M7` four `MASTERY_STANDARD.md` quality-control boxes unchecked and undeclared (concept library, positive/negative/borderline examples) — **shared with V02 and V03, raise at `CUMULATIVE_25.md`** **V04 (R2 ×1 — `m1`, OPEN, non-blocking, open item 34):** the *"§3.3 windows are identical"* justification written during the R1 remediation is true for the high-side window and false for the low-side one; the descriptor row it justifies is genuinely unchanged (1/1/1/1, recomputed at R2). **Eighth instance of the narrative-about-a-check class R1's `N5` named** |

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

**V05 R1's delta:** **+6 MINOR (`M1`–`M6`, all open), +5 NOTE** (`N1` the withdrawn
extensions finding, `N2` the substituting bracket, `N3` the inclusive-endpoint window figures,
`N5` the first clean status-block round — all closed as observations; **`N4` restates the
now five-lesson-deep manual-backtest debt and is NOT double-counted**). Plus one **NOTE-level
required action** on dimension B's disposition, carried in the same class as V04 R1's `N1`.
**0 CRITICAL, 0 MAJOR — the V06 gate opens under D-024.**

**V05 R1B's delta:** **+4 MINOR (`m1`–`m4`), +4 NOTE** (`n1` the third cluster citation —
**escalated to MINOR at R2 and counted there, not here**, so it is not double-counted; `n2`
the `E11` re-escalation, `n3` the `A-043` affirmation on a narrower basis, `n4` the mastery
report's honesty — all closed as observations). Raised concurrently with R1 against the same
tree; **not double-counted against R1's six, which are distinct findings.** The R1-round total
is therefore **10 MINOR**. **0 CRITICAL, 0 MAJOR.**

**V05 R2's delta:** **+1 MINOR (`M11`, R1B's `n1` escalated from NOTE), +4 NOTE** (`N1` the
`E11` class re-escalation, `N2` the two owner-decision items confirmed accurately logged and
deliberately unresolved, `N3` the dimension-B re-disposition still correctly blocked, `N4` the
second review-layer concurrency event — all closed as observations). **`M7`–`M10` are R1B's
`m1`–`m4` adopted, NOT new findings, and are counted once at R1B.** **Closed this round: R1's
`M1`–`M6` (all six verified against source) and open item 39.** 0 CRITICAL, 0 MAJOR — the V06
gate stays open; **V05 does not reach `COMPLETE`.**

**V05 R3's delta (for the table below):** R3 raised nothing and verified `M7`–`M11`
(open items 47–51) closed — MINOR open 11 → 6. V05 is `COMPLETE`.

**V06 R1's delta:** **+1 MAJOR (`M1`, open item 57 — the frame-26 elided `3:45am /
9:45am est.` line and the false "no session clock on any frame" claim, `E07`+`E11`),
+3 MINOR (`M2`–`M4`, open items 58–60), +3 NOTE** (`N1` the PT-023 `T1` convention,
`N2` the arm-B label correctly quarantined under `D-031`, `N3` the student's
self-audit tooling — all closed as observations). **Dimension B is blocked by `D-030`
and is EXCLUDED from pass/fail per the owner's directive — documented in
`V06_REVIEW_R1.md` §B/§14, not scored, and not the cause of the `REVISE`.**
**1 MAJOR — the V07 gate stays CLOSED under D-024** until item 57 is remediated and
re-reviewed. First round audited under `D-033`/`D-034`/`D-035`; first exercise of
`REVIEW_PROTOCOL.md` §6.G checks 15–20 against a run backtest, all clean.

**V06 R2's delta:** **+1 MINOR (`M5`, found by the item-57 sweep, ✅ CLOSED IN-ROUND),
+1 NOTE (`N1`, closed as an observation — the sweep design validated).** **Closed this
round: R1's `M1` (the MAJOR) and `M2`–`M4`, all verified against primary sources**
(frames re-read at 2×–4×, transcript re-measured). Same-session remediation and
re-review were owner-directed and disclosed; `CUMULATIVE_25.md` re-samples this round.
**0 CRITICAL, 0 MAJOR — V06 PASSES at R2 and is `COMPLETE`; the V07 gate OPENS.**

**V07 R1's delta:** **+3 MINOR (`M1`, `M2` — `E20` count class, `M3` — `E01`+`E11`; all
open as items 61–63), +4 NOTE** (`N1` the `I-009` git recurrence — audited independently and
**closed as an observation: zero damage**; `N2` §H's stale citation figure — closed, explained
by §9b being added after the sweep ran; `N3` the `R11` probe failure — closed, verified genuine
and correctly written up; `N4` the dimension-B vocabulary gap — **carried OPEN**, it restates
open item 36 for the third lesson and is counted once here as this round's escalation).
**0 CRITICAL, 0 MAJOR — the V08 gate OPENS under `D-024` with three minors deferred and owed.**
**Dimension B was scored rather than carved out** (no owner directive this round) and returned
**NOT SATISFIED with no severity charge** — the cause is the source material, and charging it
would penalise the `D-030` discipline the project mandates. See `V07_REVIEW_R1.md` §14.

| Severity | Total | Open | Closed |
|---|---:|---:|---:|
| CRITICAL | 0 | 0 | 0 |
| MAJOR | 5 | 0 | 5 |
| MINOR | 47 | 9 | 38 |
| NOTE | 56 | 6 | 50 |

*(V07 R1 arithmetic: CRITICAL and MAJOR unchanged. MINOR 44 → 47 (+`M1`–`M3`), open
6 + 3 = 9 (items 61–63; nothing closed this round — V07 is the submission under review, and
the six carried minors are V02's and V04's), closed 38 unchanged. NOTE 52 → 56 (+`N1`–`N4`),
open 5 + 1 = 6 (`N4` carried open), closed 47 + 3 = 50.)*

*(V06 R1 arithmetic: MAJOR 4 → 5, open +1 (item 57). MINOR 40 → 43, open
11 − 5 (V05 R3 closures, items 47–51) + 3 (items 58–60) = 9; closed 29 + 5 = 34.
NOTE 48 → 51, all three closed as observations, 43 + 3 = 46.
V06 R2 arithmetic: MAJOR open 1 → 0 (item 57 closed), closed 4 → 5. MINOR 43 → 44
(+`M5`), open 9 − 3 (items 58–60) = 6, closed 34 + 3 + 1 = 38. NOTE 51 → 52 (+`N1`,
closed), closed 46 + 1 = 47.)*

**Arithmetic of the V05 R1B + R2 update, written out so it can be checked.**
`MINOR` 35 → 40: **+4** (R1B `m1`–`m4`) **+1** (R2 `M11`, R1B's `n1` escalated). Open 12 →
11: **−6** (R1's `M1`–`M6` verified closed at R2) **+5** (open items 47–51). Closed 23 → 29.
`NOTE` 44 → 48: **+3** (R1B `n2`, `n3`, `n4`) **+1** (R2 `N4`, the second review-layer
concurrency event). **R2's `N1`, `N2` and `N3` restate carried items — the `E11` class
re-escalation, the two owner-decision items, and the blocked dimension-B action — and are
deliberately NOT double-counted**, on the V03 R2 / V04 R2 precedent for restated notes.
**`M7`–`M10` are counted once, at R1B, not again at R2.**

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
| 3 | V01 R1 | H4 / H5 `DEFERRED` pending `I-007` (chart data source). Reclassified in the mastery report 2026-08-10; `D-019` records the general rule. Perform when I-007 closes | `SETUP_ISSUES.md` I-007; `DECISIONS.md` D-019, **D-034** | ⚠️ **UNBLOCKED IN PART 2026-08-13 — `I-007` is CLOSED (`D-034`: TradingView / FXCM).** H4/H5 are observational chart exercises, so they need chart access rather than deep history; whether the declared feed's depth suits them is for the performing session to state. **OPEN — now actionable** |
| 4 | V01 R1 | Re-check `[00:46:04]`, `[00:48:05]`, `[00:48:13]` against the retained mp4 before any session-timing parameter is coded (`M3`) | `V01_INTERPRETATION.md` M3 / Q7 | OPEN |
| 5 | V01 R1 | Dimension B (Recognition) deferred to after V02 defines the trading zone | `V01_MASTERY_REPORT.md` B | OPEN |
| 6 | V01 R1 remediation | The stale *"no screenshot exists for V01"* paragraph appears in **17** ambiguity records, not the 3 instances R1 counted. `A-006` fixed as a dependency; **16 remain** (`A-001`–`A-005`, `A-007`–`A-017`). **Adjudicated by R2 (Part 3) — this is partly study work, but the scope stated here was wrong.** `A-009`, `A-015` and `A-017` were named as needing fresh visual claims; all three already carry sound visual updates, audited and upheld in R2. The records that actually need a fresh visual determination are **`A-002`, `A-008`, `A-016`** (determinations supplied in R2 Part 3.3), plus `A-003`'s five self-contradicting fields. `A-011` / `A-012` / `A-014` gain slide-text evidence; `A-007` needs a "frame exists, defines nothing" note; the remaining eight are mechanical | `AUTOMATION_AMBIGUITIES.md`; `18_REVIEW/V01/V01_REVIEW_R2.md` Part 3 | **CLOSED at R3** — all 16 records corrected; `A-002`, `A-008`, `A-016` determinations written and audited against the frames; two of R2's supporting claims corrected in the process (see `V01_REVIEW_R3.md` Part 3) |
| 7 | V01 R2 | Citation hygiene is the project's recurring weakness (`E11` ×5). Eight statements across two rounds cite a timestamp that does not carry their words. No quotation is fabricated. Consider requiring in `STUDY_PROTOCOL.md` that a quoted sentence cite the marker its first words fall under, and that passage-level citation be written as an explicit range | `18_REVIEW/REVIEW_INDEX.md` escalation note; raise at `CUMULATIVE_25.md` | OPEN |
| 8 | V01 R2 | `SETUP_ISSUES.md` I-006 described the SWF header frame-rate speedup as "an untested faster path". **R2's own framing was stale in turn:** it cited `D-020` as having ruled the speedup out, but `D-020` is `RETRACTED` and `D-021` records that the speedup **works at 40×** and is the default method. `I-006` now points to `D-021` | `SETUP_ISSUES.md` I-006; `DECISIONS.md` D-021 | **CLOSED at R3** |
| 9 | V01 R3 | **The V02 gate was not honoured.** `D-004` makes reviewer `PASS` the only progression gate, and `COURSE_PROGRESS.md` recorded `V02 GATE: CLOSED`, yet a full V02 student pass (transcript, notes, interpretation, 25 screenshots, homework, mastery report, `A-019`–`A-028`, `C-003`–`C-004`) was completed while V01 was in remediation. V01's `PASS` makes this moot going forward, and none of the V02 work is discarded — but the gate did not hold, and the next one (V02 `PASS` before V03) must | `DECISIONS.md` D-004; `COURSE_PROGRESS.md` | OPEN — process. **First test PASSED at R2:** V02 R1 returned `REVISE` and no V03 artifact was created — verified at the filesystem level across `03_LESSON_NOTES/`, `04_SCREENSHOTS/`, `05_HOMEWORK/`, `07_MASTERY_REPORTS/`. Stays open until a second gate holds. **ESCALATED at R2 to a LIVE BREACH — the second occurrence, and this one is not moot.** A V03 student pass appeared in the working tree during R2 while V02 was unpassed. **Two failures of the same written gate in one day is a mechanism problem, not a discipline problem:** D-004 has no enforcement, exactly like the status-block rule in R2 Minor 3. Concrete fix — a pre-flight guard in `validate_project.py` that refuses `VNN` artifact creation while `VNN GATE: CLOSED`. Required disposition in `18_REVIEW/V02/V02_REVIEW_R2.md` §7: stop the V03 pass, **do not delete the V03 work**, re-audit it against a passed V02. **UPDATED 2026-08-10 — `DECISIONS.md` D-023 and D-024.** The second occurrence is now recorded as an **owner-authorized override** (D-023): R2 §7's "stop the V03 pass" disposition is discharged and the V03 work stands as committed — nothing to revert or re-audit. **This item stays OPEN on its mechanism ground alone**, which the override does not touch: an unenforced written gate failed twice, and the override explains only why the second failure was authorized, not why an unauthorized one would have been caught. D-024 now defines what holds the gate (minors-only opens it; any `CRITICAL`/`MAJOR` closes it), so the `validate_project.py` pre-flight guard should implement **D-024's severity table**, not D-004's simpler `PASS`-only reading, plus an explicit override flag that must name the authorizing decision entry |
| 10 | V02 R1 | ~~**`C-001` has one empirical datum and it was misread.**~~ The 11a homework is the only independent observation the project has made about the day-count doctrine, and its "runs Tuesday through Thursday, consistent with 'At Least 3 Days'" claim is contradicted by the chart (price traded back above the Monday high on Thursday). Once 11a is corrected, record what the week **actually** shows against `C-001` — including "nothing", which is a legitimate result. Do not let a corrected reading quietly drop the C-001 entry | `CONTRADICTIONS.md` C-001; `18_REVIEW/V02/V02_REVIEW_R1.md` MAJOR 1 | **CLOSED at R2** — 11a redone from measurement and independently re-verified; the "three days" confirmation withdrawn; the corrected result (level 0.81150 set Mon 3 Aug 15:00 UTC, first bar above it Thu 6 Aug 15:00, **72 hours exactly**) recorded in `CONTRADICTIONS.md` under C-001 as explicitly non-resolving. The entry was **not** quietly dropped. `EFFECT ON C-001: NONE` is correct in both directions — three counting conventions give three answers, and the level was reader-selected against `A-004`. No day-count value is committed anywhere |
| 11 | V02 R1 | **A-006 / A-003 spot-check requested by V01 R3 — completed, both PASS.** Verified against the frames, not against R3's word: `[00:40:25]` prints "Trigger The Pendings"/"Trigger The Stops" as A-003 claims; `[00:38:50]` shows the pale-blue rectangle's left edge on the second vertical separator and covering a sharp advance, confirming both A-006's withdrawal and R2's narrowing. R3's remediation is substantively correct despite its D-003 departure — though two records is not an audit of fifteen actions | `18_REVIEW/V02/V02_REVIEW_R1.md` Ambiguities | **CLOSED** |
| 12 | V02 R2 | **`V02_HOMEWORK.md` §1.1's measurement pipeline is advertised as reusable for the dimension-G backtest but places one bar on the wrong side of the Fri 31 Jul → Sun 2 Aug boundary**, and its *"open = prior close on all six boundaries"* self-validation was applied at a weekend boundary where continuity should not be expected. The chart's own dotted day separators (`x = 147, 273, 429, 573, 717, 861, 987, 1149`) settle it. No conclusion in the homework changes. Must be corrected before the pipeline is reused | `V02_HOMEWORK.md` §1.1; `18_REVIEW/V02/V02_REVIEW_R2.md` Minor 1 | **CLOSED at R3** — corrected in `8df7c32` and independently re-derived at R3 from the PNG: separators, bar counts, both corrected rows, the −12.63 pip weekend gap and the `31`/`Aug` label centroids (146.12 / 273.03) all reproduce exactly. The two refuted arguments are withdrawn with the measurements that kill them, the superseded reasoning is retained in place per `REMEDIATION_PROTOCOL.md` §2, and the pipeline's real limits are now written into the file: read the chart's own separators, and do not expect continuity across a session gap |
| 13 | V02 R2 | **Two measurements of the same chart disagree, and one is untracked.** `05_HOMEWORK/V02/measure_usdchf_week.py` is a working, uncommitted measurement script that encodes the *correct* Sun 2 Aug mapping and calls the boundary *"uncertain by one bar"*, contradicting committed §1.1's "settled". **Leave it in place, adjudicate with item 12, do not delete.** §1.1 promises a reproducible method and commits no script; committing a corrected one discharges that promise | `05_HOMEWORK/V02/`; `18_REVIEW/V02/V02_REVIEW_R2.md` Note 8 | ✅ **CLOSED 2026-08-12 — `1fa087f`.** The project owner committed `05_HOMEWORK/V02/measure_usdchf_week.py` (166 lines) directly. The file is now tracked, so §1.1's promise of a reproducible method is discharged by a script under version control rather than by an untracked working-tree artifact, and the standing *"leave in place, do not delete"* instruction — honoured by every session from V02 R2 through V05 R3 — is spent. The script reads only the committed PNG (no network, no TradingView account), so any session can re-derive the per-bar highs and lows. **This closes the tracking half of the item only.** The substantive question the row also raises — committed §1.1's *"settled"* against the script's *"uncertain by one bar"* — belongs to **item 12** and is neither adjudicated nor altered here |
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
| 25 | V04 R1 | **`M1` — USDCHF's 15-minute series is mis-sliced at a partial week-open bar.** On this feed USDCHF's first 4h bar of the week holds only twelve 15m bars; the fixed 16-bar aggregation therefore puts four previous-week bars at the head of the committed 480-bar slice (`offset_in_harvest = 261`) and leaves it four short at the tail. The `−12.7` pip weekend gap sits *inside* the committed week at `m[3]→m[4]`, and `aggregate(m[4:16])` reproduces 4h bar 0 exactly on all four fields. The 27/30 symptom was reported as ±0.4 pip harvest noise when bar 0's **open** differs by 28.1 pips. **No conclusion changes** — the 4h data is continuous 116/116 and USDCHF is already outside the scoped 2-of-4 result — but the 15m harvest is the pipeline V05 inherits. Same class as open item 12 | `05_HOMEWORK/V04/`; `V04_REVIEW_R1.md` M1 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Diagnosed and re-sliced from the committed data. USDCHF's week is **476 = 12 + 29 × 16** bars, not 480 — the four leading bars were previous-week and nothing was missing from the tail. `offset_in_harvest` 261 → **265**, `j_hi_15m` 363 → 359, `j_lo_15m` 4 → 0, and a new per-pair **`bars_15m_in_4h_bar_0`** field (16/16/16/**12**) makes the aggregation explicit rather than assumed. USDCHF 27/30 → **28/30**; the 4h↔15m total **474/480 → 476/480**, its four residuals now all ≤ 0.3 pip and all in highs or lows. The ±0.4 pip misattribution is replaced by the real diagnosis in `V04_HOMEWORK.md` §1.2 validation 3, with the partial-first-bar behaviour stated as a limit of the 15m pipeline and a standing instruction to future sessions not to assume 16. New committed script **`scripts/verify_reconstruction.py`** recomputes it and exits non-zero on mismatch. **No conclusion changed, verified not assumed:** the 4h data is untouched (116/116), USDCHF stays excluded from the scoped 2-of-4 result on 4h grounds, and the §3.3 descriptor windows are identical because index and window shifted together ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Re-derived in both directions from the parent and current JSON by an independent script: the defect was real (one −12.7 pip discontinuity at `m[3]→m[4]`; bar-0 open off by 28.1 pips; `aggregate(m[4:16])` equal to 4h bar 0 on all four fields) and the fix is exact and minimal (new array is exactly `old[4:]`, only USDCHF changed, 4h untouched, `476 = 12 + 29×16` consumes the array, bar 29 reconstructs). **476/480 fields, 116/120 bars, zero in-week 15m discontinuities in all four pairs**, all residuals ≤ 0.3 pip and all in highs/lows. `verify_reconstruction.py` run as shipped: exits 0, and its checks are not tautological. Every pair's re-indexed 15m extreme maps onto the 4h bar holding the same extreme at an identical price — closes under the new indices, not the old. Scoped 2-of-4 / 3.83-day result unchanged, USDCHF still excluded on 4h bar 0 |
| 26 | V04 R1 | **`M2` — two smoothed quotations inside the transcript's own verbatim-proof paragraph** (`E01`): *"sitting up here"* for *"set up here"* `[00:50:34]`, and *"gave you a nice ugly looking kindergarten"* for *"Gaby a nice ugly look in kindergarten ma'am there"* `[01:10:36]`. Either restore both or state that the list quotes the Whisper re-transcription. **The student self-caught ~20 instances of this class before commit and that fix verifies** — these two are survivors in the provenance narrative, not in the notes | `V04_TRANSCRIPT.md` criterion 2; `V04_REVIEW_R1.md` M2 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Both restored to the **adopted transcript's** literal wording — *"There was a bunch of money **set up** here…"* `[00:50:34]` and *"One, two, three, swipes. **Gaby** a nice ugly **look in** kindergarten **ma'am** there."* `[01:10:33]`–`[01:10:36]` — and the paragraph now states explicitly that the six specifics are quoted from the adopted transcript. The smoothing is disclosed in place rather than silently corrected ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Checked against the transcript **body**, not the diff: line 3047 *"There was a bunch of money set up here and they had to go after it."* `[00:50:34]` and lines 4138/4142 *"One, two, three, swipes. / Gaby a nice ugly look in kindergarten ma'am there."* `[01:10:33]`/`[01:10:36]` — both exact. Restoration taken rather than re-attribution, and the paragraph now states which side it quotes |
| 27 | V04 R1 | **`M3` — two ambiguity cross-references point at the wrong records.** `V04_TRANSCRIPT.md` `TRANSCRIPTION NOTES` sends *"the water"* to `A-037` and *"Timing Shadow Box / Brink Spox"* to `A-038`; the register holds the Asian-range halving and the guest's ADR window at those IDs. Correct targets **`A-031`** and **`A-030`**. Orphaned pre-assignments — the transcript shipped at `d6acbf8`, the register at `4235df1` | `V04_TRANSCRIPT.md`; `V04_REVIEW_R1.md` M3 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. *"the water"* → **`A-031`**; *"Timing Shadow Box / Brink Spox"* → **`A-030`**. A dated note in `TRANSCRIPTION NOTES` records the orphaned pre-assignments and their cause ✅ **CLOSED — VERIFIED at R2 2026-08-11.** `A-031` is *"blood in the water"/"bloodline"* and `A-030` is *"brinks shadow"/"shadow box"* — the correct subjects. `A-037` (Asian-range halving) and `A-038` (guest ADR lookback) confirmed to be the wrong ones, and every surviving `A-037`/`A-038` reference in the V04 artifacts re-checked and legitimate |
| 28 | V04 R1 | **`M4` — stale count and stale filename.** `V04_SOURCE_NOTES.md` says *"26 frames"* (27 exist); `V04_MASTERY_REPORT.md` FILES PRODUCED says `VISUAL_INDEX` (renamed to `INDEX.md` in the same session). **Sixth and seventh instances of the status-staleness class** — both are arithmetic or a filename check over the repository's own contents and belong in the `validate_project.py` check proposed at open item 14 | `V04_REVIEW_R1.md` M4; open item 14 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `V04_SOURCE_NOTES.md` now reads *"27 frames, indexed in `04_SCREENSHOTS/V04/INDEX.md`"*; the mastery report's FILES PRODUCED block reads `INDEX.md` (and *"2 scripts"* → 3, since `verify_reconstruction.py` was added under item 25) ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Counted: 27 PNGs in `04_SCREENSHOTS/V04/`, 3 scripts in `05_HOMEWORK/V04/scripts/`. Both files corrected; the only surviving `VISUAL_INDEX` string is inside the remediation log describing the fix |
| 29 | V04 R1 | **`M5` — homework validation 1 is not reproducible from committed data.** *"569 bar transitions, 549 continuous, 20 breaks"* with break indices 15/45/75/105/135 and a GBPUSD exception at 143 requires full harvests; the JSON holds only the 30-bar week per pair (116 transitions available, and those reproduce 116/116). Accuracy is not in doubt — reproducibility is. Same promise as open item 13 | `V04_HOMEWORK.md` §1.2; `V04_REVIEW_R1.md` M5 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Restated over the committed data — **116/116 continuous**, recomputed by `verify_reconstruction.py` — and the harvest-wide **569 / 549 / 20** figures explicitly marked **UNREPRODUCED**, in validation 1 and again in §1.3 "What is NOT validated". **The arrays were deliberately not manufactured back into the repo:** they were never written to disk, and re-harvesting today would produce a *different* dataset from the one every figure in the file was computed on. The week boundary the figures existed to establish is independently supported by the committed data (116/116, plus 476/480 agreement with V03's dataset) ✅ **CLOSED — VERIFIED at R2 2026-08-11, and the judgement call upheld on the merits.** The honest-caveat route was the correct one: the arrays were never written to disk, so committing a fresh harvest would attach data to claims never computed on it — provenance fabrication, worse than a declared gap. Figures are marked UNREPRODUCED, not withdrawn; nothing downstream depends on them; the caveat also appears in §1.3. The reproducible half recomputes here: **116 transitions, 116 continuous, zero breaks** |
| 30 | V04 R1 | **`M6` — a visible TDI panel is unrecorded.** Curated frames 21 (`01-04-10`) and 22 (`01-08-40`) each render a sub-panel titled **`Traders Dynamic Index Visual`** with its parameter list and cyan volatility bands — the very object condition (c) refers to — on the guest's platform. Both frames are otherwise described in detail. **This does not weaken `A-039`**: displayed is not taught, and no settings or decision rule is recoverable. Add to `INDEX.md` and to `A-039`'s evidence table scoped *"displayed, not taught"*; as descriptive evidence under the item-22 ruling it also settles that "TDI" denotes the **Traders Dynamic Index**, which no line of V01–V04 audio states | `04_SCREENSHOTS/V04/INDEX.md`; `A-039`; `V04_REVIEW_R1.md` M6 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Recorded in `INDEX.md` on both frame rows and as a new §"What the visuals added" item 7, and in `A-039`'s evidence table as two rows tagged **`GUEST`, DESCRIPTIVE ONLY**, each scoped **"displayed, not taught"** with an explicit statement that they do **not** narrow `A-039` — guest evidence may extend a record and may never close it (`D-025`). The frames were opened and magnified before the descriptions were written: the six-value numeric readout beside each panel title is **not legible** at this resolution and is deliberately **not transcribed**. `A-039`'s *"the example chart carries no TDI panel"* line is now scoped to the instructor's own Segment-A chart, which is what it always meant ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Both frames opened and magnified before the new text was read. The `Traders Dynamic Index Visual` panel, its coloured lines and its bands are on both frames as described. **The six-value readout is genuinely at the edge of legibility — declining to transcribe it was the right call** and saying so in the index beats a guess or a silent omission. "Displayed, not taught" is accurate on the merits: no inputs, periods, band construction or decision rule is recoverable. Beyond what was asked, `A-039`'s *"the example chart carries no TDI panel"* line is now correctly scoped to the instructor's Segment-A chart |
| 31 | V04 R1 | **`M7` — four quality-control boxes unchecked and undeclared**: concept library, positive / negative / borderline examples. `08_CONCEPT_LIBRARY/` and all four `09_CHART_EXAMPLES/` subdirectories are empty four lessons in. `MASTERY_STANDARD.md` requires unchecked boxes to be *stated*. **Shared with V02 and V03, not a V04 lapse** — but V04 is the first lesson with a complete entry rule and a body of named terms, so the library should begin here. **Raise the underlying debt at `CUMULATIVE_25.md`** | `MASTERY_STANDARD.md`; `V04_REVIEW_R1.md` M7 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. New **QUALITY-CONTROL CHECKLIST** section in `V04_MASTERY_REPORT.md`: of nineteen boxes, **13 checked, 2 `DEFERRED`** (manual chart testing and failed-valid-setups, both blocked by `A-039` and stated rather than ticked), **4 UNCHECKED and declared** with a reason each. The concept-library box is explicitly **not** excused by `A-039` — unlike the three example boxes it was performable and was not done. **The project-wide instance is still owed at `CUMULATIVE_25.md`** — V02's and V03's reports omit the same four boxes ✅ **CLOSED — VERIFIED at R2 2026-08-11.** All 19 `MASTERY_STANDARD.md` boxes accounted for: **13 checked + 2 `DEFERRED` + 4 UNCHECKED**. Declarations true against the repository (`09_CHART_EXAMPLES/` subdirs hold only `.gitkeep`; `CONCEPT_INDEX.md` reads `CONCEPTS: 0`). Notably **refuses to excuse the concept-library box** by pointing at `A-039`, and argues the two `DEFERRED` boxes rather than ticking them |
| 32 | V04 R1 | **`N1` — dimensions B and C are mis-dispositioned.** Graded `PARTIAL` and `FAIL` for one reason: condition (c)'s indicator has never been taught. That is `D-019`'s definition of **`DEFERRED`**, not a failure of mastery. **As labelled, V04 can never reach `PASS`**, because the cause sits in the source and will not change until TDI is taught — the same trap `D-018` was written to escape for dimensions F and G, arriving now for B and C. Re-disposition as `DEFERRED — blocked by A-039`, retaining the present honest text beneath the new label. **`NOT APPLICABLE` is not available and must not be used** | `V04_MASTERY_REPORT.md` B, C; `DECISIONS.md` D-019; `V04_REVIEW_R1.md` N1 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. **B `PARTIAL` → `DEFERRED`, C `FAIL` → `DEFERRED`**, both labelled *"blocked by `A-039`"* under `D-019`, with the original text retained **verbatim** beneath the new label and a dated note giving the mechanical reason (a `FAIL` whose cause sits in the source can never be cleared by studying). `NOT APPLICABLE` explicitly declined. Both are carried in `CARRIED FORWARD` as open items alongside the manual-backtest debt, to be performed in the lesson that teaches TDI ✅ **CLOSED — VERIFIED at R2 2026-08-11.** Checked against `D-019`'s own V01 F/G worked example, not the label: subject matter exists, `NOT APPLICABLE` explicitly declined, blocker is a missing prerequisite (`A-039`), items stay **open** and are carried. Original `PARTIAL`/`FAIL` prose retained **verbatim** — diffed, not eyeballed; not one word of body text changed |
| 33 | V04 R1 | **The `RULES.md` fabrication audit is a SOLVED PROBLEM for V05–V21 — a time-saver, recorded so it is not re-discovered 17 times.** Verified at full population this round: all 21 files carry both template quotes at `[00:05:00]` and `[00:18:00]`, exactly two rules each, **and a byte-identical `NUMERICAL PARAMETERS` block (one hash, 21/21)**; `INFERRED VISUAL RULES` and `TERMS` have only two variants each across 21 files. A future session may discharge the per-lesson audit in one step by confirming those three markers and citing `V04_REVIEW_R1.md` + `Q-004`. **No `RULES.md` in this library can come back clean.** `NOTES.md` and `VISUAL_INDEX.md` are **NOT** covered — all 21 of each are pairwise distinct and still require per-lesson examination | `QUARANTINE_REGISTER.md` Q-001…Q-004; `V04_REVIEW_R1.md` | OPEN — informational, no action owed |
| 34 | V04 R2 | **`m1` — the *"§3.3 windows are identical"* justification is true for one window and false for the other** (`E20`). Both `V04_HOMEWORK.md` §1.2 (M1 correction block) and `V04_MASTERY_REPORT.md` §"Was any conclusion affected?" state that *"the extreme's index and the 44-bar window shifted together by exactly four bars, so the bars examined are the same bars"*. True for USDCHF's **high**-side window (`j_hi` 363→359, bar-for-bar identical); **false for the low-side one** — `j_lo` 4→0 was clipped at the head of the array in **both** datasets, so it went from 5 bars (four of them previous-week bars) to 1 and could not "shift". **The descriptor row it justifies is genuinely unchanged — 1/1/1/1 across all four tolerances on both datasets, recomputed at R2** — the direction is safe (the new window correctly excludes out-of-week bars) and nothing downstream reads the justification. Charged because it is one more instance of R1's `N5` pattern, produced in the commit that quoted `N5` approvingly | `V04_HOMEWORK.md` §1.2; `V04_MASTERY_REPORT.md`; `18_REVIEW/V04/V04_REVIEW_R2.md` §4 | 🔧 **OPEN — NON-BLOCKING, deferred by design.** Fix the mechanism clause whenever either file is next edited: the high-side window is bar-for-bar identical; the low-side window was clipped at the array head in both datasets and now correctly excludes the four previous-week bars it previously contained; both descriptor rows are unchanged, recomputed. **Do NOT open an R3 for this** — `REVIEW_PROTOCOL.md` §9 criterion 14 and the `V02_REVIEW_R3.md` precedent (`PASS` with non-blocking documentation-precision minors); §16 forbids the artificial extra round |
| 35 | V05 student pass | **`A-042` — AN OUT-OF-CORPUS DEPENDENCY. Owner decision needed, not a reviewer finding.** The V05 presenter defers the operative detail for **levels and reset** `[00:10:51]`, **what makes a pattern nameable and how big railroad tracks must be** `[00:26:45]`, **traps** `[00:56:48]` and **signature trades/checklists** `[00:33:17]` to the **DMR** — a separate programme with its own video library that **this repository does not contain**. Four of those are questions the bootcamp has left open across five lessons. **If this testimony holds, some `A-xxx` records are unresolvable from this corpus IN PRINCIPLE, not merely unresolved so far** — and the project currently has no vocabulary for that state. `D-019` separates `NOT APPLICABLE` from `DEFERRED`; neither describes "the source that would answer this is not in the library". **Explicit warning attached to the record: an unavailable source is a reason to leave a record OPEN, never a reason to infer what it said** (`D-008`, `D-010`) | `AUTOMATION_AMBIGUITIES.md` `A-042`; `V05_INTERPRETATION.md` §2.3 | OPEN — **owner decision** |
| 36 | V05 student pass | **A THIRD DISPOSITION may be needed for work EXCLUDED BY DECISION.** `D-018` grants `NOT APPLICABLE` for lessons stating **no testable rule**; `D-019` insists `NOT APPLICABLE` ≠ `DEFERRED` and that `D-018` grants only the first. **V05 is a third case neither contemplates:** it *states* several testable-shaped rules and they are **withheld by `D-025`**. `DEFERRED` is wrong — deferral implies the work becomes possible later, and **no future lesson makes a V05 guest rule testable**. Dimensions **F** and **G** were graded on a *purposive* reading of `D-018` with the *strict* reading flagged, and **this is the sole reason V05 is submitted `REVIEW REQUIRED` rather than `PASS`** | `V05_MASTERY_REPORT.md` §F, §G, Escalation; `DECISIONS.md` D-018, D-019, D-025 | ⚖️ **RULED 2026-08-11 at V05 R1 — OPEN only on the owner's adoption step.** The escalation is **upheld: the project needs a third disposition and V05 is the lesson that proves it.** Neither label fits work permanently excluded by decision — `NOT APPLICABLE` says *there was never anything here* (false; there is an hour of it), `DEFERRED` says *this becomes possible later* (false; it never does). **Dimension G's `NOT APPLICABLE` is UPHELD** on the purposive reading, because `DEFERRED` would be affirmatively false — no future lesson makes a V05 guest rule testable — **but its stated reason must change** from *"states no testable rule"* to *"states rules excluded by D-025"*, or V06–V21 will inherit the wrong precedent. **Dimension F is UPHELD as graded** (`SUCCESS AFTER SOURCE REVIEW`): it correctly refuses `NOT APPLICABLE`, since the assignment is partly performable and the performable part was performed on real data. **Dimension B's `NOT APPLICABLE` is NOT AVAILABLE** — `D-019`'s table grants it for dimensions **F and G only**; this is the same mis-disposition as V04 R1 `N1` and is carried the same way, as a **NOTE with a required action**, because the prose beneath the label is accurate. **Reviewer recommendation to the owner: adopt `EXCLUDED BY DECISION`** — subject matter exists; the work is permanently barred by a numbered decision, which must be cited; the item closes like `NOT APPLICABLE` and accrues no debt; the record states *what* was excluded and *under which decision*, so the exclusion is auditable rather than invisible; available to **any** dimension. On adoption, V05's **B** and **G** take it and **F** stays as graded. **This ruling does not hold the gate** — it is a vocabulary gap in the project's own standards, not a defect in V05's understanding, and the student diagnosed it correctly and declined to resolve it unilaterally |
| 37 | V05 student pass | **`A-049` — the stop-hunt vs trap-move discriminator is the highest-priority research question the project now carries.** V05's guest gives a clean two-limb test — **close beyond the level vs pin beyond without closing**, plus **immediate directional shift vs continued oscillation** — for two objects the instructor uses constantly across V01–V04 and has **never distinguished on the record**. It is `GUEST` material and **excluded**. Standing question for V06–V21: **does the instructor ever draw this distinction himself?** If he does, his statement becomes the record and this becomes corroboration; if no lesson does, the project must state that the corpus does not contain the distinction. **Named failure mode:** a future session reconciling this with an instructor passage would manufacture a rule neither man stated and would feel like good scholarship doing it | `AUTOMATION_AMBIGUITIES.md` `A-049`; `V05_SOURCE_NOTES.md` §5h | OPEN — carry to every remaining lesson |
| 38 | V05 student pass | **SPEAKER IDENTIFICATION MUST BE THE FIRST STEP OF EVERY REMAINING LESSON — evidenced, not just asserted.** Instructor runtime across the single 2012-03-25 session date runs **~100% (V03) → ~31% (V04) → 0% (V05)**. `D-025` consequence 3 already mandates speaker tagging; V05 shows the cost of skipping it — **a session that assumed V05 was the instructor would have written an entire lesson of false doctrine, and every downstream file would have inherited it.** Whether the trend is structural (a multi-presenter programme) or incidental (one long day split among coaches) is **not settled**, and the actionable consequence holds either way | `V05_INTERPRETATION.md` §3; `DECISIONS.md` D-025 | OPEN — informational, standing procedure |
| 39 | V05 student pass | **A correction issued against two ALREADY-COMMITTED files, recorded rather than silently patched.** `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES and `QUARANTINE_REGISTER.md` `Q-005` both state *"`EMA` occurs 3 times"*. **The literal token occurs twice** (verbatim body, word-boundary, case-sensitive; body lines 1271 and 3944); the third item in the transcript's own list, *"closing below the 200"* `[01:06:02]`, does not contain the token. **No conclusion in either file changes** — the point both were making (no 5/13/800 EMA, no colours or nicknames) is unaffected and re-confirmed. Logged in `V05_SOURCE_NOTES.md` §7 for the reviewer to disposition; a correction that leaves no trace is worse than the error | `V05_SOURCE_NOTES.md` §7 note 1 | ✅ **CONFIRMED 2026-08-11 at V05 R1 — the fix location is `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES and `Q-005`.** Re-measured independently (word-boundary, case-sensitive, verbatim body): **`EMA` occurs exactly twice** — `[00:23:52]` *"Nice close below the 50 EMA."* and `[01:05:53]` *"…below the 200 EMA."* The third item in the transcript's own list, *"closing below the 200"* `[01:06:02]`, is present and **does not contain the token**. **The student is right, and logging the correction rather than silently patching was the correct call.** No conclusion in either file changes: the point both were making is independently re-confirmed here — `5 EMA` **0**, `13 EMA` **0**, `800` **0**, `mayonnaise` **0**, `mustard` **0**, `water` **0**. **Required:** correct both files in place, retaining the superseded text per `REMEDIATION_PROTOCOL.md` §2. ✅ **CLOSED — APPLIED AND VERIFIED at V05 R2 2026-08-11.** The count was re-derived a third time before any edit (`grep -n -w EMA`, verbatim body only: body lines 1271 and 3944 — the same two the student found) and then corrected at both sites with the superseded text retained. **Applied by the R2 reviewer session on explicit owner instruction — a declared `D-003` deviation, scoped to two numerals and recorded at `V05_REVIEW_R2.md` §3.1.** `A-020`'s V05 row already stated *"twice"* and needed no change |
| 41 | V05 R1 | **`M1` (`E11`) — the same quote is cited at two different wrong timestamps, neither a marker.** *"I use the trend line. I use E and I use the box."* is at **`[00:57:35]`–`[00:57:36]`**; `V05_SOURCE_NOTES.md` §3b cites `[01:07:36]` and `A-043`'s evidence table cites `[01:01:35]`. The quotation is accurate; only the citations are wrong, and being wrong two different ways means neither was checked against the other. **`A-043`'s closure does not rest on this row** — it rests on the toolbar dialog, verified at pixel level at R1 | `V05_SOURCE_NOTES.md` §3b; `AUTOMATION_AMBIGUITIES.md` `A-043`; `V05_REVIEW_R1.md` M1 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Both citations corrected to the marker the words actually carry. `V05_SOURCE_NOTES.md` §3b now cites *"I use E"* at **`[00:57:36]`** (was `[01:07:36]`); `A-043`'s evidence table now cites **`[00:57:35]`–`[00:57:36]`** (was `[01:01:35]`) and splits the fragment across the two markers it spans — `[00:57:35]` *"I use the trend line."*, `[00:57:36]` *"I use E and I use the box."* Both re-verified against `V05_TRANSCRIPT.md`. **`A-043`'s closure is untouched**; it rests on the toolbar dialog, not on this row |
| 42 | V05 R1 | **`M2` (`E11`) — citation off by one marker.** `A-039`'s V05 extension row cites `[00:36:03]` for *"looking for shorts, the trend line goes on the top and on the top"*; `[00:36:03]` reads *"I can start drawing my trend line."* and the quoted words are at **`[00:36:05]`**. Open item 7's class — the passage marker rather than the sentence's first words | `AUTOMATION_AMBIGUITIES.md` `A-039`; `V05_REVIEW_R1.md` M2 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `A-039`'s V05 extension row now cites **`[00:36:05]`** and quotes that marker's literal text — *"So I'm going, I'm looking for shorts, the trend line goes on the top and on the top."* — rather than a smoothed fragment under the preceding marker. `[00:36:03]` (*"I can start drawing my trend line."*) verified as the adjacent, different sentence |
| 43 | V05 R1 | **`M3` (`E01`) — a smoothed quotation.** `V05_SOURCE_NOTES.md` §4b quotes *"**the** second leg of that pattern, that three hits to the high"* `[00:13:05]`; the transcript reads *"…and **level three** second leg of that pattern…"*. Same class as V04 `M2`, and again in supporting prose rather than the notes proper — but the passage is the file's evidence for the **level↔day relabelling** and the excised words are a level number | `V05_SOURCE_NOTES.md` §4b; `V05_REVIEW_R1.md` M3 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. The elision was **not** marked; the literal wording was **restored**, and the sentence boundary the ellipsis had hidden is now explicit — `[00:13:05]`–`[00:13:12]` *"So the consolidation and level three second leg of that pattern, that three hits to the high."* and `[00:13:13]` *"That's the third type, I guess the third leg begins your level one drop."* The excised level number is back in the file's evidence for the level↔day relabelling. **No conclusion in §4b changes** — the relabelling claim is carried by `[00:12:50]` and `[00:12:57]`–`[00:13:03]`, both unaltered |
| 44 | V05 R1 | **`M4` (`E20`) — three V05 files disagree about V05's own evidence order.** `04_SCREENSHOTS/V05/INDEX.md` discloses, prominently and unprompted, that *"that order was **not** preserved for V05"* and that the audio-only separation is *"**weaker** for V05 than for V01–V04"*; `V05_INTERPRETATION.md` line 12 says V05 *"**restored** the recipe's evidence order that V03 and V04 deviated from"*. Opposite claims about the same fact, and the interpretation's is the self-flattering one. **Fix the interpretation; do NOT weaken the `INDEX.md` disclosure to match** | `V05_INTERPRETATION.md` line 12; `04_SCREENSHOTS/V05/INDEX.md`; `V05_REVIEW_R1.md` M4 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `V05_INTERPRETATION.md`'s Screenshots row now states, first and in bold, that **the recipe's evidence order was NOT preserved for V05**, names `INDEX.md`'s § "⚠ PROCESS DEVIATION, DISCLOSED" as **the governing statement**, gives the cause, and carries `INDEX.md`'s own consequence — the audio-only / visual-corroborated separation is **weaker for V05 than for V01–V04**. What *was* held (source notes §§1–8 from transcript only, visuals confined to §9, one disclosed pre-sweep sanity frame) is stated as a partial, not as restoration. Superseded text retained beneath the table per `REMEDIATION_PROTOCOL.md` §2. **`04_SCREENSHOTS/V05/INDEX.md` was NOT edited** — the disclosure is verbatim as R1 found it |
| 45 | V05 R1 | **`M5` (`E20`) — a stale pointer inside `A-039`.** It still reads *"The promised TDI lesson. V05 … is the next candidate."* V05 has now been studied and did **not** define TDI. **Eighth instance of the status-staleness class (open item 14) — and the only one this round**; see `N5`, the first round in which the four status blocks were all current | `AUTOMATION_AMBIGUITIES.md` `A-039`; `V05_REVIEW_R1.md` M5 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. `A-039`'s *Required Research* now records that **V05 was checked and did NOT define TDI** — it supplies the first *displayed* name (`TDI_MMM`, frame `V05_00-36-54`) and the first slide titled to mark the panel up, but no inputs, periods, bands, line names or decision rule; **a name is not a definition**. **V06 (or any later lesson) is named as the next candidate.** Superseded text retained per `REMEDIATION_PROTOCOL.md` §2. Record stays **OPEN** and `DO NOT CODE` |
| 46 | V05 R1 | **`M6` (`E20`) — an unrecorded oscillator sub-panel in curated frame 26.** `V05_00-40-04` renders a multi-line sub-panel of the same family the index records carefully on frames 19–21; the frame-26 row describes the frame down to the taskbar clock and a 9× status-bar read and does not mention it. **Directly the V04 `M6` class, whose precedent is binding.** R1 magnified the header and confirms it is at the edge of legibility and **should not be transcribed**. Record scoped *"displayed, not taught; header not legible"* in `INDEX.md` and in `A-039`'s extension row. **It does NOT narrow `A-039`** (`D-025`) | `04_SCREENSHOTS/V05/INDEX.md` frame 26; `A-039`; `V05_REVIEW_R1.md` M6 | ✅ **CLOSED — VERIFIED at R2 2026-08-11**, re-derived from `V05_TRANSCRIPT.md` and the committed PNGs rather than from the remediation diff. Frame 26's row in `04_SCREENSHOTS/V05/INDEX.md` now records the multi-line oscillator sub-panel beneath the price pane, scoped **"displayed, not taught"**, noting the presenter neither points at nor discusses it at `40:04`. The header sits in the same position as frame 21's `TDI_MMM` header and is **deliberately NOT transcribed** — presence only, at the edge of legibility, the same call frame 27's OHLC row gets. Added to `A-039`'s extension row on the same terms. **It does NOT narrow `A-039`** (guest material, `D-025`) |
| 40 | V05 student pass | **`A-043` is the project's first ambiguity closed on GUEST evidence, and the precedent is deliberately narrow.** The MT4 text tool is settled by the displayed *Customizing toolbar* dialog: MT4 carries exactly two text objects whose icons are the literal letters **`A`** (`Text`) and **`T`** (`Text label`), so *"use the one that says A, don't use the one that says T"* means **use `Text`**, and the transcript's *"E"* is a mishearing of *"A"*. **Claimed basis:** the record concerns a **platform artifact**, not methodology, and closes an ambiguity about **this lesson's own ASR** rather than about the method — so no instructor record is closed on guest evidence and no precedent for that is claimed. **A reviewer who disagrees should downgrade it to `EXTENDED, NOT CLOSED`; nothing downstream depends on it** | `AUTOMATION_AMBIGUITIES.md` `A-043`; `04_SCREENSHOTS/V05/INDEX.md` frame 4a | ⚖️ **AFFIRMED 2026-08-11 at V05 R1 — closure UPHELD, not downgraded; OPEN only on the owner's recording step.** The evidence was verified at the pixel level on the 2× re-render and is exactly as described: MT4's *Customizing toolbar* dialog carries two text objects — **`A Text`** in *Selected* (icon: a plain letter A) and **`T Text label`** in *Available* (icon: a boxed T). *"Just use the one that says A. Don't use the one that says T."* therefore means **use `Text`**, and the transcript's *"one that says E"* is an ASR mishearing of *"A"*. **Why `D-025` does not bar it, stated as a class rather than a one-off excuse:** D-025 bars guest evidence from closing records *about the method*, because that would give a guest's normative claims operative standing. `A-043`'s subject is **which button this speaker's own mouth referred to** — a question about *this lesson's ASR* and *a platform artifact*, answered by a screenshot of a dialog box. Closing it promotes no guest statement into doctrine and nothing downstream depends on it. **Ruling: a record whose subject is a guest's own utterance or a platform artifact, and not the method, may be closed on descriptive guest evidence; a record about the method may not be, ever, however clear the guest evidence.** `A-020`, `A-039`, `A-032`, `A-018`, `A-010`/`A-011` and `A-019` sit on the far side of that line and the student correctly left every one open. **Owner action:** record the carve-out as a numbered refinement of `D-025` — D-025's own "Alternatives considered" rejected *case-by-case adjudication with no standing rule*, and the student's per-record justification is exactly that even though it reaches the right answer. Writing the class down converts a good judgement call into an enforceable rule. **Recording step only; the finding stands either way** · ✅ **CLOSED — MOOT, 2026-08-13.** `D-033` reverses `D-025`'s normative exclusion outright: guest material may now close any record, method or otherwise. A numbered carve-out is an exception to a bar that no longer exists. `A-043`'s closure **stands** and no longer needs the special argument. The general ruling quoted here — *"a record about the method may not be closed on guest evidence, ever"* — is **superseded** |
| 47 | V05 R1B (adopted at R2 as `M7`) | **`M7` (`E20`) — `C-003` is named four times for a check that belongs to `C-004`.** The V05 check actually performed and struck off is `C-004` — *"London session open: 3:30am printed against 4:00 spoken"* — and it is written correctly inside the `C-004` record. **`C-003` is *"Whether M and W formations can fail"*; it contains no V05 text at all and names no next candidate.** Four sites name the wrong record: `CONTRADICTIONS.md` line 23 (**the STATUS block**), lines 845 and 846, and `V05_MASTERY_REPORT.md` §J. A future session reading the status block learns that the *"M's and W's will not fail"* record was tested against V05 and came back negative — **it was never tested.** Same class as V04 R1's `M3`. The underlying check reproduces exactly and `C-004`'s disposition does not move. **`V05_REVIEW_R1.md` §6 dimension O carries the same error and must NOT be edited** (`REVIEW_PROTOCOL.md` §11); it also retires R1's `N5` superlative that *"all four status blocks are current"* | `CONTRADICTIONS.md` lines 23, 845, 846; `V05_MASTERY_REPORT.md` §J; `V05_REVIEW_R1B.md` `m1`; `V05_REVIEW_R2.md` `M7` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** All four sites now name **`C-004`**: `CONTRADICTIONS.md`'s STATUS block, the two sentences in § "V05 PASS", and `V05_MASTERY_REPORT.md` §J. Superseded text retained at each location per `REMEDIATION_PROTOCOL.md` §2, each naming `C-003` as the wrong record and stating that `C-003` (M/W failure) contains no V05 text and was never tested. **The check itself does not move** — V05 contains zero clock times and `C-004` stays `UNRESOLVED`. **`V05_REVIEW_R1.md` was NOT edited** (`REVIEW_PROTOCOL.md` §11) |
| 48 | V05 R1B (adopted at R2 as `M8`) | **`M8` (`E01`) — a verbatim string quoted with a count the string does not support.** `V05_MASTERY_REPORT.md` §E records the day count's escape clause *"but up to five days"* as occurring **four times**. **The literal string occurs twice**, at `[00:11:11]` and `[00:24:37]`; *"five days"* occurs four times, but `[00:11:16]` (*"sometimes five days depending"*) and `[00:12:39]` (*"Remember three to five days"*) do not contain the quoted words. **Third live instance of the project's verbatim-count class** — with open item 15 (V02 *"level count"*) and open item 39 (`EMA`, closed at R2). The generative rule is identical every time: **a count asserted over a string inside quotation marks, without re-measuring the string.** Three instances is `REVIEW_PROTOCOL.md` §7's systematic-weakness threshold — raise at `CUMULATIVE_25.md` | `V05_MASTERY_REPORT.md` §E; `V05_REVIEW_R1B.md` `m2`; `V05_REVIEW_R2.md` `M8` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** `V05_MASTERY_REPORT.md` §E now reads *"**twice verbatim**, `[00:11:11]` and `[00:24:37]`; the day-count expectation itself is stated four times"*. Re-measured this session before the edit: the literal string *"but up to five days"* occurs **2**, *"five days"* occurs **4**. Superseded text retained, naming the two non-matching hits and pointing at `V05_SOURCE_NOTES.md` §4c as the origin (`M10`). The exception is still recorded and the §E grade does not move |
| 49 | V05 R1B (adopted at R2 as `M9`) | **`M9` (`E20`) — unrecorded printed `R =` labels in curated frame 26, and `A-018` undercounts.** `V05_00-40-04` carries **four printed `R = <number>` labels** on its cyan boxes, confirmed at R2 by magnification: three legible (`R = 40.9`, `R = 40.6`, `R = 41.1`) and one **partly occluded by the moving-average line** (`R = 7?.6`, most consistent with `74.6` — R1B read it flat as `74.6`; **R2 corrects that to a scoped reading**). `INDEX.md`'s frame-26 row records none of them despite describing the frame down to a taskbar clock. `A-018`'s V05 row lists only the four **slide** labels and concludes *"V05 adds four more labels"* — **V05 adds at least eight**, and the unrecorded four are the *stronger* evidentiary class because they are auto-rendered on the presenter's **live MT4 platform**, which is exactly the proposition `A-018` accumulates. **It does NOT narrow or close `A-018`** — guest material, `D-025`, and V05 states no stop and no target. Stays `DO NOT CODE`. Same class as R1's `M6`, in the same frame | `04_SCREENSHOTS/V05/INDEX.md` frame 26; `A-018`; `V05_REVIEW_R1B.md` `m3`; `V05_REVIEW_R2.md` `M9` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** Frame 26 was **re-opened and magnified by this session** (16× nearest-neighbour and 16× LANCZOS) rather than taken from either review's prose. Four `R = ` labels confirmed: **`R = 40.9`** (upper-centre), **`R = 40.6`** (centre-right), **`R = 41.1`** (lower-right) all legible, and a **fourth at the left where `R = ` is legible but the value is NOT** — the cyan moving average runs directly through the digits and only a trailing glyph separates. **R2's correction of R1B is upheld: `74.6` is not supportable from this PNG and is NOT transcribed**, per the frame-27 / V04 `M6` precedent. Recorded in `INDEX.md` row 26 and in `A-018`'s V05 row, scoped *printed, not spoken; live platform; three values legible, one not*; *"four more labels"* → **"at least eight"**. Superseded text retained. **`A-018` is extended, not narrowed** — stays `DO NOT CODE` |
| 50 | V05 R1B (adopted at R2 as `M10`) | **`M10` (`E02`) — a framing sentence over-generalises its own table.** `V05_SOURCE_NOTES.md` §4c heads its four-row table *"Repeated four times, **always with the same escape clause**"*. **Two of the four rows carry no escape clause**, in the quoted text or its neighbourhood — `[00:15:47]` and `[00:16:35]`, verified at R2 by reading the surrounding markers. The rows are accurate; the sentence above them is not. **This is `M8`'s origin** — the generalisation hardened into a false verbatim count one file downstream in the mastery report, which is `REVIEW_PROTOCOL.md` §17 failure mode 3 in miniature. Charged separately because this is where it starts | `V05_SOURCE_NOTES.md` §4c line 251; `V05_REVIEW_R1B.md` `m4`; `V05_REVIEW_R2.md` `M10` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** §4c's framing sentence now reads *"Repeated four times; **two of the four carry the explicit "up to five days" escape clause**"*, and the table gains an **Escape clause** column recording ✅ / ❌ per row with the adjacent markers quoted for the two negatives (`[00:15:52]`/`[00:15:55]` and `[00:16:36]`/`[00:16:39]`). Superseded text retained, naming this sentence as `M8`'s origin. The four rows were and remain individually accurate; no conclusion in §4c changes |
| 51 | V05 R1B (adopted at R2 as `M11`) | **`M11` (`E11`) — a third citation in the same wrong-offset cluster, escalated from `NOTE` to `MINOR` at R2.** `AUTOMATION_AMBIGUITIES.md` `A-042` cites `[01:01:39]` for *"for the DMR, I kind of use the ellipse to show the moving average crossover"*; **`[01:01:39]` is not a marker** and the words are at **`[00:57:39]`**. All three of V05's defective citations map `00:57:3x` → `01:0x:3x` — `[01:01:35]` (`A-043`), `[01:07:36]` (§3b), `[01:01:39]` (`A-042`) — which is **one bad offset applied to a neighbourhood, not three independent slips**, so R1's `M1` fix closed two thirds of a single defect. R1B graded it a note only because it filed it alongside `M1`; on its own merits it is a nonexistent-marker citation in a live register, which is what `M1` and `M2` were charged as. **Required with the fix: a mechanical marker-existence sweep of every `[hh:mm:ss]` citation in the V05 artifacts**, to confirm no fourth cluster member survives — R1 hand-checked 356 citations and missed this one | `AUTOMATION_AMBIGUITIES.md` `A-042`; `V05_REVIEW_R1B.md` `n1`; `V05_REVIEW_R2.md` `M11` | ✅ **APPLIED 2026-08-11; VERIFIED CLOSED at R3 2026-08-12 (`V05_REVIEW_R3.md` §1, re-derived from source).** `A-042`'s evidence table now cites **`[00:57:39]`** and carries that marker's literal sentence — *"And obviously for the DMR, I kind of use the ellipse to show the moving average crossover"*. **The required mechanical sweep was run and is CLEAN:** every `[hh:mm:ss]` citation on a V05-attributed line across `AUTOMATION_AMBIGUITIES.md`, `CONTRADICTIONS.md`, `V05_SOURCE_NOTES.md`, `V05_INTERPRETATION.md`, `V05_MASTERY_REPORT.md`, `04_SCREENSHOTS/V05/INDEX.md` and `05_HOMEWORK/V05/` was matched against the 1,353 markers in `V05_TRANSCRIPT.md`. **No fourth cluster member exists** — the only non-resolving hits are six explicit V01/V02/V04 cross-citations and one slide timecode (`CONTRADICTIONS.md` line 850, `(slide, [00:15:49])`, frame 11's own burned-in time), none of which is a V05 marker citation. The displaced cluster is closed at three |

> ✅ **MERGE NOTE RESOLVED 2026-08-12 (owner instruction).** Two lines of work branched from
> `3a13441` and each appended rows starting at **34**. The upper block (**34–51**, V04 R2 / V05
> student pass / V05 R1 / V05 R1B) **keeps its numbers** — it is the more heavily cited
> (`LOG.md` *"open item 34/36/39"*, the V05 review files, `COURSE_PROGRESS.md`). The lower
> block (backtest-evidence-standard lineage, `D-026`…`D-031`, `PT-001`) is **renumbered
> 34→52, 35→53, 36→54, 37→55, 38→56**, and its citing references were updated in the same
> pass: `CHANGELOG.md` (the `[0.7.2]` entry) and `LOG.md` (the D-028/029/030 and D-031
> session entries). No row's content was altered. The original note read: *"DUPLICATE ITEM
> NUMBERS 34–38, OWNER RECONCILIATION OWED … Neither block was renumbered on merge …
> Renumbering either side would silently break live cross-references."*

| 52 | External methodological review 2026-08-11 | **Baseline + pre-registration standard adopted (`D-026`/`D-027`, `BACKTEST_EVIDENCE_STANDARD.md`).** The four-lesson manual-backtest debt is now owed under it: each discharged test needs a pre-registered period and a matched random-entry baseline, exactly as a fresh test would. **Reviewer must audit checks 15-20 on the first discharged test.** Where the sample permits, V04's inside-box vs outside-box contrast is the course's own natural control and should be run | `BACKTEST_EVIDENCE_STANDARD.md`; `REVIEW_PROTOCOL.md` §6.G 15-20 | OPEN |
| 53 | Same | **Owner owed two decisions before the first `BT_` file.** ✅ **CLOSED 2026-08-11** — `D-028` (70/30 development/holdout, exact dates pinned at first data-source decision) and `D-029` (baseline parameters: 1,000 iterations, seed recorded, matched window, direction-matched primary + random-direction secondary arm). `OWED NOW` markers cleared | `DECISIONS.md` D-028, D-029 | ✅ CLOSED |
| 54 | Owner direction 2026-08-11 | **`D-030` — blocked tests wait for the course; definitions are never approximated.** Generalizes `A-039`'s TDI prohibition to every definitional blocker (`A-011` M/W anatomy, `A-004` the level, `A-002` trap move, `A-019` timezone). Manual-backtest debt will keep accruing and **that is correct behaviour**, not a backlog to clear by lowering the standard. Reviewer: treat an approximated definition inside a test as `E06`+`E18`, **CRITICAL** | `DECISIONS.md` D-030 | OPEN — standing |
| 55 | Owner request 2026-08-11 | **`PT-001` — the one test available before the course teaches more.** Pre-registered at `06_MANUAL_BACKTEST/PRE_REGISTERED/PT-001_asian_range_predictive_content.md`: does the Asian range boundary carry predictive content? No pattern recognition, no indicator — the box is pure measurement. Tests the **load-bearing premise** under V04's prohibition, V03's accumulation phase and condition (a). ~~Blocked by `A-019`~~ **— UNBLOCKED 2026-08-11 by `D-031`'s two-arm timezone design.** Remaining prerequisites are `I-007` (data source) and the `D-028` boundary dates — and unlike the other blockers this plausibly closes from existing V01–V05 evidence rather than a future lesson (V04 `[00:07:01]` Eastern; V01 `[00:46:09]` US session 9:30 Eastern; but `C-004` warns session times in this course are messy). **Prerequisite work item: a focused timezone evidence pass.** Do NOT assume Eastern to unblock it (`D-030`) | `PT-001…md`; `A-019`; `C-004` | ⚠️ **PREREQUISITES DISCHARGED 2026-08-13 — and a new one appeared.** `I-007` CLOSED (`D-034`); `D-028` boundary PINNED at 2016-07-01 (`D-035`); `PT-001`'s window `W-A` **conforms**. **Still blocked by DATA AVAILABILITY**: the declared feed serves 15m GBP/USD back only to 2026-05-31, and `W-A` is 2015. `D-035` records the three exits and they are the **owner's** to choose. **OPEN — owner flagged, do not lose** |
| 56 | Owner direction 2026-08-11 | **`D-031` — session timezone is a TESTED VARIABLE, two arms, both always reported.** Arm A fixed `UTC−5`; Arm B DST-aware `America/New_York`. **Reviewer must check that BOTH arms are reported** on any session-dependent test — reporting only the better one is `E09`+`E24`. Fact of record: the bootcamp ran 2012-03-18→06-17, entirely inside US DST, so **Arm B reproduces the instructor's own stated times and Arm A displaces them by an hour**; this is evidence about the source and does not settle which reading the method needs. `A-019` remains **OPEN** — `D-031` governs project method, not course content, and may never be cited as instruction | `DECISIONS.md` D-031; `A-019`; `PT-001` §3 | OPEN — standing |
| 57 | V06 R1 | **`M1` (`E07`+`E11`, `MAJOR`) — frame `V06_00-48-29` Week 10 prints *"and more specifically at 3:45am or 9:45am est."*, legible at committed resolution, elided as "not legible" in the frame-26 transcription; its absence then asserted as *"no session clock appears on any of the 32 frames"* in `04_SCREENSHOTS/V06/INDEX.md` and `V06_SOURCE_NOTES.md` §11d.** First printed `est` in the corpus evidence; two fire times attached to the Brinks trade. Fix: complete the transcription (superseded text retained), correct both sentences, extend `A-019` and `A-030` with the printed evidence and its provenance (DMR syllabus, guest programme, printed not spoken), re-sweep the other 31 frames for elided-but-legible text. **Holds the V07 gate closed (`D-024`)** | `V06_REVIEW_R1.md` M1 | ✅ **CLOSED — APPLIED at `4c89db1`, VERIFIED at R2 2026-08-13** (`V06_REVIEW_R2.md` §1). Week 10 transcribed in full, both false sentences corrected, `A-019`/`A-030` extended, full-frame sweep run — the sweep surfaced `M5` (see E20 ledger), fixed in-round |
| 58 | V06 R1 | **`M2` (`E20`, count class) — transcript header "Steve 25× = 23 + 2" irreproducible: 26 tokens; third read-aloud instance `[01:11:39]` (Isubio quotation) unclassified.** Speaker conclusion unaffected and strengthened. Count class is at its escalation threshold (items 15, 39, 48) — raise at `CUMULATIVE_25.md` | `V06_REVIEW_R1.md` M2 | ✅ **CLOSED — VERIFIED at R2** (26 tokens with accounting; three read-alouds incl. `[01:11:39]`; re-measured, reproduces exactly) |
| 59 | V06 R1 | **`M3` (`E20`, count class) — `V06_SOURCE_NOTES.md` §10's once-corrected row still miscounts: `Asia` is 2× (`[00:50:25]`, `[01:09:55]`), not 1×.** Conclusion (Asian box undefined) unaffected | `V06_REVIEW_R1.md` M3 | ✅ **CLOSED — VERIFIED at R2** (`Asia` 2× with both markers cited; re-measured) |
| 60 | V06 R1 | **`M4` (`E20`, staleness class, item 14 lineage) — the `D-033` propagation (`612f431`) left the five live `D-025` fences in the V06 lesson artifacts untouched** (transcript header, source notes, interpretation, homework, screenshot index — each states superseded prohibitions in present tense). Fix: dated `D-033` notice under each fence, noting `D-030` still blocks the *push*-family material; with it, record the restated V06 corpus contribution under `D-033` (`V06_REVIEW_R1.md` §13.2). Error is conservative (over-restricts), hence MINOR | `V06_REVIEW_R1.md` M4, §13 | ✅ **CLOSED — VERIFIED at R2** (five dated `D-033` notices in place; `V06_INTERPRETATION.md` §9 delivers the §13.2 restatement, seven doctrine-eligible statements checked against markers, nothing promoted) |
| 61 | V07 R1 | **`M1` (`E20`, count class — items 15/39/48/58/59 lineage) — `V07_SOURCE_NOTES.md` §10 states the *level* count as 26 uses; it is 56, and §5 of the same file says 56 correctly.** Re-measured: `level` 53 + `levels` 3 = **56**; the `level <N>` compound is 35; entries containing the token are 44. **26 matches none of them.** The file therefore holds one right record and one wrong record for the same object fourteen sections apart — the V05 `M4` intra-file-disagreement class on top of the count class. **Conclusion unaffected and understated** (*level* is used constantly and never defined; `A-004` untouched); no other artifact cites 26. Charged because §10's preamble offers the counts *"so a reviewer can falsify them cheaply"*. **Fix:** correct §10's cell to **56** (or name the sub-count intended); **do NOT change §5**; retain superseded text | `V07_SOURCE_NOTES.md` §10, §5; `V07_REVIEW_R1.md` M1 | ✅ **APPLIED 2026-08-13 — PENDING VERIFICATION at R2.** §10's cell reads **56 uses** (`level` 53 + `levels` 3), re-derived from the verbatim body this session rather than taken from the review's prose (compound `level <N>` 35, entries containing the token 44 — all three re-measured, 26 matches none). **§5 not edited.** Superseded cell retained in a dated block beneath the table per `REMEDIATION_PROTOCOL.md` §2. Conclusion unchanged; `A-004` untouched |
| 62 | V07 R1 | **`M2` (`E20`, same count class) — `V07_SOURCE_NOTES.md` §10's *"the peak"* row says 4×, lists five markers, and the true count is 5.** The five markers listed (`[00:00:26]`, `[00:03:18]`, `[00:03:20]`, `[00:14:02]`, `[00:16:44]`) are **all correct**; only the number is wrong, so the row contradicts itself on its face. The row's `peak formation` / `PFH` / `PFL` zero counts are correct and its conclusion is unaffected. **Fix:** `4×` → **5×**; leave the marker list alone; retain superseded text | `V07_SOURCE_NOTES.md` §10; `V07_REVIEW_R1.md` M2 | ✅ **APPLIED 2026-08-13 — PENDING VERIFICATION at R2.** The row reads **5×**; re-measured from the verbatim body this session at exactly the five markers already listed. **Marker list unchanged**, `peak formation`/`PFH`/`PFL` zeros unchanged. Superseded cell retained in the same dated block as `M1` per `REMEDIATION_PROTOCOL.md` §2. Conclusion unchanged |
| 63 | V07 R1 | **`M3` (`E01` misquote, co-code `E11` wrong marker) — `V07_MASTERY_REPORT.md` §D alters a word inside quotation marks and cites the wrong marker, falsifying §H's own categorical integrity claim.** §D's Sequence table quotes *"if it doesn't do what you expect **and** your flashcard isn't the same"* at `[00:28:28]`; the transcript reads *"…**in** your flashcard…"* at **`[00:28:31]`**, and `[00:28:28]` exists carrying a different sentence (*"We'll say whether it's something that you will take."*). The `in` → `and` substitution is the *sensible* reading of a garbled ASR passage, which is exactly why it must not be made silently inside quotes (V04 `M2` / V05 `M3` class). **§H states, unhedged, *"No quotation mark in any V07 artifact contains a word that is not in the source"* — this is the instance that falsifies it.** Materiality to the method is nil: §D's grading does not turn on the word and `V07_SOURCE_NOTES.md` §6c renders the passage correctly. **Counterweight, measured by the reviewer:** 239 marker-cited quotes across seven artifacts were machine-checked and **this is the only defect**. **Fix:** restore *"in your flashcard"*, re-cite to `[00:28:31]`, and **in the same edit** repair or scope §H's sentence; **do NOT edit `V07_SOURCE_NOTES.md` §6c**; retain superseded text | `V07_MASTERY_REPORT.md` §D, §H; `V07_REVIEW_R1.md` M3 | ✅ **APPLIED 2026-08-13 — PENDING VERIFICATION at R2.** §D's Invalidates cell now reads *"If it doesn't do what you expect **in** your flashcard isn't the same"* cited to **`[00:28:31]`**, re-derived from `V07_TRANSCRIPT.md` this session. §H's categorical sentence **repaired, not merely scoped**: it now states that one such quotation existed, was found at R1 and is corrected. **The repair was earned by a fresh sweep, not assumed from the review's count** — every `*"…"*` fragment with an adjacent citation across all seven V07 artifacts re-matched against the transcript: **167 marker-cited quotes, zero remaining word-substitutions after the §D fix**; the nine flags raised were opened by hand and cleared (printed slide/chart text, a labelled **V04** quote, the student's own first reading, a hypothesised ASR alternative, and two explicitly-marked elisions). **`N2` folded into the same edit as the review directed** — §H's *"163 citations"* is recorded as true-when-measured and now stale (190 occurrences / 171 distinct; 182 / 168 excluding §11), with the cause named (§9b added after the sweep, following `R11`'s failure). **`V07_SOURCE_NOTES.md` §6c not edited.** Superseded text retained at both §D and §H per `REMEDIATION_PROTOCOL.md` §2 |

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
