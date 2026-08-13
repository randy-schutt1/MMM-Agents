# V06 — INDEPENDENT REVIEW R1

| Field | Value |
|---|---|
| Lesson | V06 — `Bootcamp1 Wk2 032612 Part1 (75mins).swf` — *"Micro Daily Trends"* |
| Review round | R1 |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent, fresh session (`D-003` satisfied — this session authored no V06 artifact) |
| Protocol | `00_SYSTEM/REVIEW_PROTOCOL.md` (17 dimensions, error taxonomy, severity) |
| Standard | `00_SYSTEM/MASTERY_STANDARD.md`; `DECISIONS.md` D-001 … **D-035** — this is the first review conducted with `D-033` (guest material normative), `D-034` (data source declared) and `D-035` (holdout pinned) in force |
| Owner directive for this round | Dimension **B (Recognition)** is permanently blocked because *push* was never defined in any lecture (`D-030`, no approximated definitions). **Directive: review it, document the block, and do not let this one blocked dimension count against the overall pass/fail verdict.** Applied at §B and §14 below. The carve-out covers the D-030/*push* issue on dimension B **only**; every other finding gates normally |

---

## EXECUTIVE BLOCK

```text
LESSON:     V06
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      1   (M1)
MINOR:      3   (M2, M3, M4)
NOTE:       3   (N1, N2, N3)

DIMENSION B: BLOCKED BY D-030 (term "push" undefined in the corpus).
             EXCLUDED FROM PASS/FAIL PER OWNER DIRECTIVE — documented at §B,
             not scored as a failure and not a factor in the REVISE verdict.
             The REVISE rests entirely on M1–M4, which are independent of the
             "push" definition gap.

ADVANCEMENT: NOT AUTHORIZED — the V07 gate stays CLOSED under D-024
             (1 MAJOR). Re-opens on remediation of M1 (and the minors with
             it) and re-review.
```

**Had M1 not existed, this round would have been a `REVISE` with minors only (gate OPEN),
or a `PASS` outright — dimension B's block would not have prevented it.** The carve-out was
applied, is documented explicitly, and did not need to be stretched: B is not what holds
V06 back this round.

---

## 0. WHAT THIS REVIEWER VERIFIED INDEPENDENTLY, BEFORE ANY DIMENSION WAS GRADED

Per §3 of the protocol, source first, student work second, comparison last. Everything
below was re-derived by this session from primary artifacts, not accepted from V06's files:

1. **The transcript body's mechanical properties, re-measured.** 1,304 markers, 1,304
   distinct, strictly increasing, zero same-second pairs; largest gap 15 s at `[01:05:36]`,
   then 14 s at `[00:02:00]`, 13 s at `[00:11:16]`, and four 12 s gaps at `[00:01:48]`,
   `[00:07:22]`, `[00:39:02]`, `[01:07:58]`. **All match the COVERAGE block exactly.**
2. **The negative-vocabulary claims, re-measured** over the verbatim body: `5/13` 0×,
   `5 EMA` 0×, `800 EMA` 0×, `Asian Box` 0×, `Shark Fin` 0×, `PFH`/`PFL` 0×, `HOD`/`LOD`
   0×, `EST` 0×, `TDI` 1×, `ADR` 3×, `EMA` 6×, `tracer` 10×. All as the student states.
   Two token counts do **not** reproduce — see `M2`, `M3`.
3. **The committed quote checker re-run** (`check_quotes.py`): **0 failures**, matching the
   mastery report's provenance table. The comprehension probe re-run: 33/33 positive,
   13/15 negative with the two documented "correct failures" (`N03`, `N13`) reproducing.
4. **The backtest re-run from committed data** (`run_pt023.py`, seed `20260812`): PT-024
   reproduces to the digit — Arm A median D +3.4 p, f 0.610, N-P percentile 89.6; Arm B
   −4.5 p, f 0.390, percentile 5.8; PT-023 reproduces its n = 12 `SAMPLE INSUFFICIENT`
   figures. The holdout is not touched by the script (verified in output and in code path:
   it slices DEVELOPMENT before computing anything).
5. **Pre-registration order verified in git history**: `582859e` (PT-022 + D-032) →
   `294441d` (PT-023) → `6d5d8e9` (PT-024) all precede `62aa3c4` (results). The D-028
   scoped boundaries recompute to the same dates (see `N1` for a convention nit).
6. **Frames read directly** — the title slide, the `V06_00-05-29` bullets slide (all six
   bullets verified verbatim, `HOD`/`LOD` printed as claimed), and the DMR curriculum
   frame `V06_00-48-29` re-read at magnification. The last of these produced **M1**.
7. **`validate_project.py`: structural validation passes** on the tree as reviewed.
8. **Registers spot-verified**: `A-050`–`A-054` and `C-006` exist with the content the
   mastery report claims; the D-033 re-assessment flags are present in both registers.

---

## FINDINGS

### M1 — `MAJOR` (`E07` false negative, co-code `E11`) — a printed clock time **with a timezone** was missed on frame 26, and its absence is asserted in two files

Frame `V06_00-48-29` (the DMR Curriculum 2012), Week 10, reads in full:

> *"Brinks Trade - 2nd Leg of a M or W pattern Falling inside the Shadow Box **and more
> specifically at 3:45am or 9:45am est.**"*

The bolded clause is **plainly legible at the committed capture resolution** — this
reviewer read it at 1× and confirmed it at 2× magnification of the committed PNG. The
student's frame-26 transcription (`04_SCREENSHOTS/V06/INDEX.md`) elides it with an
ellipsis under a protocol stating ellipses mark text *"present but not legible at this
capture resolution"*. It was legible.

The omission then hardens into a false universal, stated identically in two files:

- `04_SCREENSHOTS/V06/INDEX.md`, summary: *"no session clock appears on any of the 32
  frames (`A-019` untouched, sixth consecutive lesson)"*
- `V06_SOURCE_NOTES.md` §11d: *"No session clock appears on any of the 32 frames.
  `A-019` is untouched."*

Both are wrong as written. What the frame prints is not a session *boundary*, so the
narrower audio claim in §10 (*"no hour is attached to Asian, London or US anywhere"* —
scoped to audio) survives. But `9:45am est.` is a clock time **with a printed timezone
token**, and it is — on the corpus's own records — the **first printed `est` in the
evidence base**. That bears directly on two load-bearing open records:

- **`A-019`** (session timezone): the record's whole question is whether the course
  community's clock is EST/EDT/other. A course-adjacent 2012 document printing `est` is
  exactly the class of evidence `A-019` collects, and V06's artifacts assert it does not
  exist. The claim *"sixth consecutive lesson of silence"* is false for the frames.
- **`A-030`** (Brinks / Shadow Box): the frame attaches **two specific fire times** to the
  Brinks trade. The student's own §11b transcription of this frame captured *"Shadow
  Box"* and stopped exactly before the times. Under `D-033` (now in force) this printed
  line is admissible normative-eligible evidence, which raises the cost of the miss.

Why `MAJOR` and not `MINOR`: this is not wording — it is missed material evidence on a
standing foundational ambiguity, plus an affirmative false claim of absence in the
precise place a future session would look before deciding `A-019`'s stakes. Why not
`CRITICAL`: no adopted rule or methodology definition is corrupted; the defect is
localized to one frame's record and two summary sentences, and the correction is
mechanical.

**Required action:** re-transcribe frame 26's Week 10 line in full in
`04_SCREENSHOTS/V06/INDEX.md` (superseded text retained per `REMEDIATION_PROTOCOL.md`
§2); correct the two "no session clock on any frame" sentences; extend `A-019` and
`A-030` with the printed `3:45am / 9:45am est.` evidence, tagged to its provenance (DMR
syllabus, guest programme, printed not spoken); and re-sweep the other 31 frames for any
further elided-but-legible text before resubmission.

### M2 — `MINOR` (`E20`, token-count class — open items 15/39 lineage) — the transcript header's "Steve occurs 25 times, 23 + 2" is irreproducible

`V06_TRANSCRIPT.md` § ONE SPEAKER states the token `Steve` occurs **25** times
(word-boundary, case-sensitive) — **23** the speaker's own third-person references,
**2** inside read-aloud audience questions.

Re-measured by this session: **26** occurrences (the line at `[01:11:45]` contains the
token twice; two occurrences are possessives, which word-boundary matching includes —
no counting convention reproduces 25). And the read-aloud class has **three** members,
not two: the header catalogues `[01:03:56]` (Tom) and `[01:05:30]` (Micah) but not
**`[01:11:39]`** — *"I suppose Steve has simplified the presentation…"* — which sits
inside the quoted Isubio text the presenter is reading aloud (`[01:11:22]` *"this is
another Isubias thing"*). The speaker's own third-person references number 23, which
matches — the total and the read-aloud split do not.

**The identification conclusion is untouched and, if anything, strengthened** (one more
third-person reference in read-aloud material, zero first-person uses). Charged because
a numerically wrong count in the corpus's flagship speaker-identification argument is
precisely where a hostile audit would start, and because this is another member of the
verbatim/token-count class already at its escalation threshold (raise at
`CUMULATIVE_25.md`).

### M3 — `MINOR` (`E20`, same count class) — the *corrected* "Asian" count is itself wrong

`V06_SOURCE_NOTES.md` §10's remediated row states *"`Asian` is 4× word-boundary, plus
one `Asia`"*. Re-measured: `Asian` **4×** (`[00:31:58]`, `[00:32:05]`, `[00:49:53]`,
`[01:09:43]`) — correct — but `Asia` **2×**: `[01:09:55]` (*"is the first push in
Asia?"*) **and `[00:50:25]`** (*"level three will happen in Asia and won't come
back"*, inside David's read-out email). The row that was already corrected once by the
student's own probe (`N03`) is still miscounted on its second token. The substantive
conclusion — the term is in the room and the box is never defined — survives again.
Fix the count; the class note in M2 applies.

### M4 — `MINOR` (`E20`, status-staleness class — open item 14 lineage) — the D-033 propagation stopped short of the V06 lesson artifacts themselves

Commit `612f431` (*"propagate D-033/D-034/D-035 into every place they change"*) added
blocking-condition-changed notices to the mastery reports, both registers,
`COMMON_PROTOCOL.md` and `PRE_REGISTERED/INDEX.md`. It did **not** touch:

- `V06_TRANSCRIPT.md` (the D-025 consequence box: *"No statement in it may enter the
  canonical methodology… none may close an `A-xxx`…"*),
- `V06_SOURCE_NOTES.md` (the *"READ THIS BEFORE CITING"* fence, stated as live),
- `V06_INTERPRETATION.md` (§4 *"None… `D-025` excludes every normative statement"*),
- `V06_HOMEWORK.md` (the exclusion table, stated as live),
- `04_SCREENSHOTS/V06/INDEX.md` (the header fence, stated as live).

Each of these states `D-025`'s superseded prohibitions in present-tense, unqualified
form. A future session reading any one of them alone — and the fences are written
precisely to be obeyed by a session reading one file alone — would enforce a ruling the
owner has reversed. The propagation commit's own claim (*"every place they change"*) is
therefore overstated. The error is conservative (it over-restricts rather than
over-admits), which is why this is `MINOR` and not `MAJOR`.

**Required action:** add a short, dated `D-033` notice under each of the five fences
(superseded text retained), pointing at `DECISIONS.md` `D-033` and noting that `D-030`
still blocks operationalisation of *push*/*pullback*/*nameable pattern*/ADR-lookback
material regardless of the reversal.

### N1 — `NOTE` — the PT-023 `T1` is quoted under two conventions

`BT_V06_0001.md` §1 and the `D-028` append record PT-023's `T1` as `2026-08-13 10:30`
(the raw series' last bar); `run_pt023.py` prints `T1 = 2026-08-13 08:00` (after the
10-bar live-edge trim; 10 × 15 m = the 2.5 h difference exactly). The boundary date
(`2026-08-06`) and the DEVELOPMENT bar count (1,154) are identical under both, so
nothing changes; state which convention `T1` uses when the files are next touched.

### N2 — `NOTE` — the arm-B "CONTRADICTED AS TAUGHT" label is correctly quarantined

The runner prints a per-arm verdict and Arm B's is the sharp one. `BT_V06_0001.md` §3a
declines to promote it, applies the pre-registered conjunctive rule, and names the
temptation (`E09`+`E24`) explicitly. Verified against the pre-registration text and
the re-run output: the handling is exactly right, and it is the first live case of the
`D-031` both-arms discipline doing real work. Recorded as a positive observation.

### N3 — `NOTE` — the student's self-audit tooling found real defects before review

The comprehension probe's two "correct failures" (`N03` Asian box, `N13` the 90%
figure) both identified genuine omissions in the student's own artifacts, and both
fixes retained superseded text properly. The probe's own bug (`N06`, the `1:3`
timestamp-collision) is documented in the script rather than removed. This does not
offset M2/M3 — two of the counts it touched are still wrong — but the practice of
committing re-runnable audit tools with the lesson is worth carrying to V07–V21.

---

## THE 17 DIMENSIONS

### A. Source fidelity — **PASS**, with M2/M3's count caveats

Spot-checks of the student's quotations against the verbatim transcript found no
misquote; the committed quote checker re-ran clean (0 failures over 32 + 24 + 11 + 2
matched fragments), and this reviewer independently verified the load-bearing passages
(the three-pattern enumeration `[00:07:22]`–`[00:07:44]`; the rejection prohibition
`[00:08:06]`–`[00:08:23]`; the second-leg counting rule `[00:15:19]`–`[00:15:36]`,
`[01:10:04]`; the two-hour clock `[00:13:19]`, `[00:23:36]`; the counter-trend failure
case `[00:37:29]`–`[00:37:47]`; the level-three-becomes-level-one relabelling
`[00:25:12]`). Qualifiers are preserved — notably *"approximately"* on ADR ÷ 3,
*"usually"* on the pullback band, and the presenter's own withdrawal of the 9-candle
minimum. ASR garble is quoted with bracketed repairs, never silently smoothed. The
two count errors (M2, M3) are the only fidelity defects found, and neither touches a
quotation.

### B. Completeness / Recognition — **BLOCKED BY D-030 — DOCUMENTED, EXCLUDED FROM PASS/FAIL PER OWNER DIRECTIVE**

The mastery standard's Recognition dimension requires the taught concepts to be
identified on charts not used in the lesson. V06's central taught concept is the
*push*. **The term is never precisely defined in any lecture** — the presenter gives a
counting rule (*"wherever the second leg is, that's my push one"*), boundary practice
(*"highest point to the lowest point"*), and failure modes, but no definition that
decides a boundary case, and `A-054` records him using *push three* three different
ways in one lesson. `D-030` (*"no approximated definitions"*) therefore blocks the
exercise: any operational definition of *push* used to mark unseen charts would be the
agent's own, and `D-033` explicitly declines to unblock it (*"a session that reads
`D-033` as unblocking the `D-030` list has misread it"* — with dimension B named).

**This is a structural gap in the course material, not a student failure.** The student
session said so itself, graded B `NOT APPLICABLE (with reason)` on the purposive
reading, and escalated the disposition question honestly (mastery report, ESCALATION
§1). This reviewer confirms: (a) the block is real and correctly attributed to D-030;
(b) no artifact smuggles in an approximated push definition to work around it — the
homework's refusal table and the PT-022 §1 blocked-claims table were both checked;
(c) **per the owner's standing directive for this review, dimension B is documented as
blocked and is not counted against the verdict.** The `REVISE` above owes nothing to B.

Completeness otherwise: the lesson's operational meaning — sequence, preconditions,
exceptions, negative cases, the Q&A definitions of rejection/trap/stop-hunt, the
administrative segment, the homework framing — is captured thoroughly. One completeness
defect exists and is charged at **M1** (the frame-26 elision).

### C. Provenance — **PASS**

Every normative statement carries a marker; the marker-existence sweep is pre-run and
its two deliberate non-resolvers are declared in advance. The mastery report's
provenance table reproduces. **Orphan rules: none — no rule was adopted**, and under
the D-033 re-assessment (§13 below) any statement promoted to doctrine already carries
its citation. M1's co-code (`E11`) reflects the one place evidence went unrecorded.

### D. Explicit vs inferred — **PASS**

The interpretation file's `EXPLICIT`/`VISUAL`/`IMPLIED`/`INFERRED`/`UNRESOLVED` tags
were audited row by row. The student labels its own characterisations (`"frequency
upgrade with a filter attached"`, the §5.1 arithmetic tension, the §5.4 push-three
asymmetry) as `INFERRED`/`UNRESOLVED` and lists five things it expects to be wrong
about. The standard failure chain (examples → pattern → universal rule → code) does
not appear; the machine-rule firewall was not tested by any artifact. `[00:44:55]`
(the instructor trades level threes and holds for days) is correctly held at arm's
length rather than promoted to a fact about the instructor.

### E. Chart recognition audit — **PASS (limited scope by D-030)**

No chart classifications were produced (see B), so the audit reduces to: (a) the
homework charts — verified to contain only day separators and daily extremes, rendered
from committed JSON with the disclaimer in the image footer; (b) the screenshot index's
per-frame content descriptions — spot-verified against three frames read directly
(title slide, `00-05-29` bullets, `00-48-29` curriculum), which is how M1 was found;
31 of 32 frame descriptions stand, one is incomplete (M1).

### F. Counterexample testing — **PASS**

The lesson's own negative cases are captured in a dedicated section
(`V06_SOURCE_NOTES.md` §5) and the student's CV-4 discrimination table correctly
identifies the two places the presenter breaks his own rules (the non-nameable entry
at `[00:23:25]`; the push-three triple usage). No positive/negative example files were
created — correct under the B block, and the checklist says so rather than hiding it.

### G. Manual backtest review — **PASS** — audited against checks 1–20

The procedure, not the result, per protocol:

| Check | Verdict |
|---|---|
| 1 GBP/USD | ✅ (`D-007`) |
| 2–4 period reasonable, sequential, future hidden | ✅ — distributional test, no per-bar decisions; DEVELOPMENT sliced before any statistic |
| 5 rules known before result | ✅ — pre-registration commits precede data commits, verified in git (§0.5) |
| 6–9 skips/losers/borderline/invalid | N/A by design — no trades exist, deviation declared up front |
| 10–11 outcomes/R consistent | ✅ / N/A |
| 12 screenshots | N/A — no chart decisions; data committed instead |
| 13–14 exact rule identified; testing the lesson not an interpretation | ✅ — verbatim rule quoted with marker; the window-substitution caveat (V02's table, V06 states no clock) is declared in the scope statement rather than discovered by review |
| **15 baseline present** | ✅ — N-P sign-flip + N2 clock-shift, 1,000 iterations each; matched-random-**entry** correctly argued inapplicable (no entry exists) with the substitute nulls drawn from `COMMON_PROTOCOL.md` §5 |
| **16 baseline pre-registered** | ✅ — in the PT files and `D-032`, committed before data; nulls printed before the rule arm in the same run (verified by re-execution) |
| **17 period pre-registered** | ✅ — two re-issues (PT-022 → 023 → 024) each got a **new test ID** with the prior file retained and marked; both re-issues occurred before any result existed (git order verified). This is the mechanism working, not period-shopping — the student invited scrutiny on exactly this point and it was applied |
| **18 holdout intact** | ✅ — never opened in either test; PT-023's overlap with previously-seen homework data is **disclosed as contamination and the test downgraded to `DESCRIPTIVE`**, which is the required behaviour |
| **19 n ≥ 30, intervals** | ✅ — PT-024 n = 41 with 95% CIs on every fraction; PT-023 n = 12 labelled `SAMPLE INSUFFICIENT FOR INFERENCE` at every quotation |
| **20 negative results retained** | ✅ — the null-indistinguishable headline result *is* the reported result; the sharper per-arm label is explicitly declined (N2 above); PT-023's nothing-result is reported in full |

`E21`–`E25`: none found. The V04 inside/outside-box natural control is inapplicable to
this claim. **This is the cleanest dimension in the round and the first `G` in the
corpus to exercise checks 15–20 end to end.**

### H. Hindsight / lookahead audit — **PASS**

Actively searched: the homework measures properties of data with no outcomes attached;
the backtest is distributional with pre-registered windows and mechanical inclusion
(zero-bar days dropped by pre-registered rule, reflected in n, no other exclusions);
the one contamination vector (PT-023's window overlapping previously-seen data) is
self-disclosed and quarantined. No setup boundaries, no classifications, no entries
exist to contaminate. Nothing found.

### I. Outcome vs rule application — **PASS**

No trades, so the four-quadrant grading is inapplicable; `BT_V06_0001.md` §4 says so
explicitly rather than skipping it. The `O2` descriptive band-fit (*"30 to 50 pips"
describes the median NY session*) is kept separate from the comparative verdict.

### J. Sample quality — **PASS**

n = 41 for the evidential arm, above the pre-registered floor; the n = 12 arm correctly
downgraded. The one-week, four-pair homework observation draws no conclusions. The
student's own regime caveat (2012 rules vs 2026 volatility) is stated wherever the §3
comparison appears.

### K. Homework review — **PASS**

The assignment as stated (*"find your anchor… look for three pushes"*) is push-defined
and thus D-030-blocked; the student performed the mechanical half, tabulated every
item with its disposition, and refused the single most tempting measurement (the
25–50 pip pullback band) on correct grounds. Classification `SUCCESS AFTER SOURCE
REVIEW` is honest — the scope was set by reading the decisions first, and no first
attempt was discarded because none existed. Under `D-033` the *refused* half changes
status (see §13): the refusals were correct under the rules in force when performed,
and `D-030` independently sustains most of them, so no rework is ordered.

### L. Teach-back — **PASS**

CV-2 reconstructs the lesson's causal structure accurately (verified against the
transcript), separates the presenter's reasoning from the student's own reading, and
names where the student's reading exceeds the source. The weakest joint — *"level
three becomes level one"* — is flagged by the student itself as not fully understood
rather than papered over. That is the correct behaviour under §15's "do not force
certainty".

### M. Blind recognition — **BLOCKED with B** — same D-030 ground, same carve-out, documented, not scored.

### N. Ambiguity review — **PASS**

`A-050`–`A-054` verified present and correctly scoped; ten extensions verified against
the register. No subjective term was converted to a constant anywhere — the ADR-family
table is the *demonstration* of why not, and it is the strongest single artifact in
the round. `A-054` (push three used three ways) is correctly an ambiguity rather than
a contradiction.

### O. Contradiction review — **PASS**

`C-006` verified: the V05 and V06 stop-hunt accounts are quoted accurately from both
transcripts and the divergence is real (geometric/chart-observable vs
causal/spread-based). Filed under D-025 as corpus hygiene; the D-033 propagation
correctly flags it for re-categorisation as a live method contradiction (two
equal-authority speakers), and the register carries the flag. `C-004`'s negative
re-check against V06 verified (`EST` 0× in audio — though see M1 for the frames).
The deliberate non-test of `C-003` is correctly reasoned.

### P. Machine-rule firewall — **PASS**

No `INFERRED MACHINE CANDIDATE` was created; no number in the lesson was promoted; the
homework and backtest artifacts each state what may not be built on them. `D-010`
untested by any artifact — nothing tried to cross it.

### Q. Claimed accuracy — **PASS**

The 90% figure is recorded with provenance and context (permission threshold, not
performance claim), which is `D-009` applied correctly — and the student's own probe
caught its initial omission. The guest's *"5,000 trades"* report about the instructor
is recorded as reported testimony under D-009. No sample was shaped toward any figure.

---

## 13. THE `D-033` RE-ASSESSMENT THE PROPAGATION COMMIT OWED THIS REVIEW

`D-033` (owner, 2026-08-13) makes guest material normative at equal weight, and the
mastery report's blocking-condition-changed note explicitly hands re-assessment to this
review. Findings:

1. **No prior finding of this review flips under `D-033`, and one sharpens.** M1's
   missed printed evidence *matters more* under D-033 (the DMR frame is now
   normative-eligible); M2–M4 are unaffected. Nothing the student excluded was wrongly
   excluded *at the time it was written* — every exclusion cites D-025, which was then
   in force.
2. **V06's corpus contribution is now understated by its own artifacts.** "Doctrine
   produced: zero" was true under D-025 and is no longer the operative description:
   the entry sequence, filters, time stop and exit recorded (and fenced) in
   `V06_SOURCE_NOTES.md` §4 are admissible doctrine-candidates — **subject to D-030**,
   which still blocks everything requiring *push*, *pullback*, *nameable pattern* or an
   ADR lookback. What survives D-030 for potential promotion is modest but real: the
   wait-for-rejection prohibition (defined in Q&A via the trap-completion close), the
   two-hour time stop, the contrary-pattern exit, the 2:1 preference, the
   moving-average-distance stop geometry, and the three-views timeframe map. **This
   review does not promote them** — promotion is a session's work with the reading done
   (D-033's own consequence note) — but the restatement obligation is recorded as a
   required action rather than left implicit, and M4's fence updates are its
   prerequisite.
3. **`C-006` and `A-049`** are correctly flagged in the registers for re-categorisation;
   nothing further owed this round.
4. **Dimension B stays blocked** under D-033, exactly as D-033 itself states. The
   owner's carve-out and the decision text agree; there is no tension to resolve.

---

## 14. THE DIMENSION-B CARVE-OUT — EXPLICIT ACCOUNTING

Per the owner's directive for this review:

- **Reviewed:** yes — §B above, including verification that no artifact works around
  the block with an approximated definition.
- **Documented as blocked, and why:** yes — *push* is never precisely defined in any
  lecture (host or guest); `D-030` forbids approximated definitions; `D-033` names
  dimension B as staying blocked. Structural gap, not student error.
- **Counted against pass/fail:** **no.** The `REVISE` verdict rests on M1 (MAJOR) and
  M2–M4 (MINOR), all independent of the *push* gap. If M1–M4 are remediated and R2
  finds nothing new, the expected outcome is a PASS with dimension B carried as
  *"blocked by D-030, excluded from pass/fail per owner directive"* — not a failure,
  not a blocker.
- **Scope of the carve-out:** the D-030/*push* issue on dimension B only. M1–M4 gate
  normally, and did.

---

## 15. REQUIRED CORRECTIONS (SPECIFIC, PER §10)

1. **(M1)** In `04_SCREENSHOTS/V06/INDEX.md`, complete the Week 10 transcription with
   *"and more specifically at 3:45am or 9:45am est."* (superseded text retained);
   correct the two *"no session clock appears on any of the 32 frames"* sentences
   (INDEX summary and `V06_SOURCE_NOTES.md` §11d); extend `A-019` and `A-030` with the
   printed evidence and its provenance; re-sweep the remaining frames' elided text.
2. **(M2)** Correct `V06_TRANSCRIPT.md` § ONE SPEAKER: token total 26 (state the
   possessive/double-line accounting), read-aloud instances three (add `[01:11:39]`,
   Isubio quotation), speaker's own references 23. Superseded text retained.
3. **(M3)** Correct `V06_SOURCE_NOTES.md` §10: `Asia` 2× (`[00:50:25]`, `[01:09:55]`).
4. **(M4)** Add dated `D-033` notices under the five live D-025 fences
   (`V06_TRANSCRIPT.md`, `V06_SOURCE_NOTES.md`, `V06_INTERPRETATION.md`,
   `V06_HOMEWORK.md`, `04_SCREENSHOTS/V06/INDEX.md`), each noting that `D-030` still
   blocks the *push*-family material.
5. **(§13.2)** With M4, record (in the interpretation or a successor artifact) the
   restated V06 corpus contribution under D-033: which fenced statements are now
   doctrine-eligible and which remain D-030-blocked. Promotion itself is separate work
   and is not required for R2.
6. **(N1, optional)** State the `T1` convention in `BT_V06_0001.md` §1 when next edited.

No re-recording, re-transcription, re-harvest or re-test is required. The backtest and
homework stand as run.

---

## 16. LOGGING

Review logged in `LOG.md` (Reviewer Session, 2026-08-13). `REVIEW_INDEX.md`: decision
row added (V06 R1 REVISE 0/1/3), error counts updated (E07 +1, E20 +3), open items
**57–60** opened for M1–M4, severity delta appended. Next review trigger: student
resubmission of V06 (remediation of items 57–60).
