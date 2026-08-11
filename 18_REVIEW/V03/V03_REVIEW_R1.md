# V03 — INDEPENDENT REVIEW

| Field | Value |
|---|---|
| Lesson | V03 (`Bootcamp1 Wk2 032512 Part1 (71mins).swf`, SHA-256 `efe256d8…`) |
| Review version | R1 |
| Review date | 2026-08-10 |
| Previous review | none |
| Reviewer independence | Fresh session; no V03 material was authored by this reviewer (D-003 satisfied) |

---

## FINAL DECISION

```text
REVISE
```

**Decision:** `REVISE` — **0 CRITICAL, 0 MAJOR, 3 MINOR** (plus notes). Under
`DECISIONS.md` D-024, a minors-only round **opens the V04 gate**; the three minors
are tracked below and remain owed before V03 can reach `COMPLETE`.

**Confidence:** HIGH

This is the strongest student submission the project has produced. The review was
conducted adversarially — every load-bearing claim the student flagged for audit was
re-derived rather than accepted, including a full independent re-verification of the
citation audit, the homework dataset, and the screenshot sweep behind the C-004
negative finding. Nothing material broke. The three minors are precision defects in
otherwise sound work, and none alters a conclusion.

---

## SOURCE MATERIAL REVIEWED (FIRST, per protocol §3)

| Source | What was done | Purpose |
|---|---|---|
| `V03_TRANSCRIPT.md` | **Read in full** (all 1,230 entries), before any student conclusion | Fidelity baseline; anchoring avoidance |
| All 24 committed screenshots | Index read; 5 load-bearing frames inspected at full resolution (`00-12-39`, `00-27-39`, `00-28-44`, `00-44-19`, `00-58-49`); the AJ chart additionally re-examined in 2× crops | Verify slide transcriptions and the §4e correction |
| **The full 857-frame sweep** | Located intact in the prior session's scratchpad (`…/d9fffb67…/scratchpad/ruffle-test/sweep/`), identity confirmed by pixel-exact match of `s_0152.png` against the committed 12:39 slide; independently re-clustered into **76 screen states**; a representative of **every state** visually reviewed | Re-verify the C-004 negative claim on the material the student could not re-check (mastery report audit item 6) |
| `Q-003` quarantined files | `RULES.md` opened directly; `V04-R001` confirmed verbatim as documented; transcript confirmed to carry nothing of the kind at `[00:05:00]`; quarantine location and `.gitignore` coverage verified on disk | Confirm V03's fabricated derived files are properly quarantined |
| ECB reference rates (frankfurter.dev) | Daily USD/CHF, USD/JPY, EUR/USD, GBP/USD fixes for 3–7 Aug 2026 fetched | External, non-TradingView cross-check of the homework data |

## STUDENT ARTIFACTS REVIEWED (SECOND)

| Artifact | Reviewed |
|---|---|
| `03_LESSON_NOTES/V03_SOURCE_NOTES.md` | In full, against the transcript read first |
| `03_LESSON_NOTES/V03_INTERPRETATION.md` | In full |
| `05_HOMEWORK/V03/V03_HOMEWORK.md` + `data/weekly_bars_2026-08-02.json` + 4 charts | In full; every derived number recomputed from the raw JSON |
| `07_MASTERY_REPORTS/V03_MASTERY_REPORT.md` | In full; all six requested audit items executed |
| `AUTOMATION_AMBIGUITIES.md` (STATUS, A-026, A-029–A-036) | Records read; A-026 resolution verified against transcript and frame |
| `CONTRADICTIONS.md` (V03 evidence section, C-004) | In full |
| `04_SCREENSHOTS/V03/INDEX.md`, `LOG.md` V03 entries, `COURSE_PROGRESS.md`, `CONCEPT_INDEX.md` | Checked |
| `scripts/validate_project.py` | Re-run: structural validation passes |

---

## CRITICAL FINDINGS

**None.**

## MAJOR FINDINGS

**None.**

## MINOR FINDINGS

| # | Finding | Error code | Evidence | Impact / required fix |
|---|---|---|---|---|
| M1 | **The homework's ADR figures do not reproduce from the committed data.** §2.5 Finding B states ADR 47.0 / 54.8 / 148.2 / 56.5 pips. Recomputing from `weekly_bars_2026-08-02.json` under three defensible day-boundary conventions gives 43.6–46.5 (EURUSD), 53.4–56.4 (GBPUSD), **128.0–138.9 (USDJPY)**, 52.8–54.9 (USDCHF) — none matches, USDJPY off by up to 14%. The file says "computed from the week's own five daily ranges" but never states where a day starts, and the five ranges used are not committed. | E19 | Reviewer recomputation, this session | **The conclusion is safe** — 0 of 4 reaches 3×ADR under every convention tried (multiples 1.46–2.61). But a number bearing on `C-001` must be re-derivable. Fix: state the day-boundary convention in §2.5 and add the five per-pair daily ranges to the file or the JSON. |
| M2 | **The transcript's I-008 verification block overclaims.** `COVERAGE` states *"timestamps strictly monotonic, no duplicates"*. The body contains **three same-second adjacent duplicate markers** — `[00:35:21]`, `[01:00:13]`, `[01:04:30]` (1,230 entries, 1,227 unique). The sequence is non-decreasing throughout, never decreasing, and the duplicates are benign short entries; but the claim as written is false, and it sits inside a verification record. | E20 | Reviewer marker scan, this session | Fix the wording (e.g. "non-decreasing; three benign same-second adjacent pairs"). Same class as REVIEW_INDEX open items 15/16 — a verified figure that fails to reproduce — now on the student side. |
| M3 | **"All four exceed the taught 2.5–3 day window" overstates its sample.** In USDJPY and USDCHF the week's low **is bar 0** — no stop hunt occurred, no anchor formed, and the homework itself rejects these as pattern instances in §2.4 on exactly that ground. Their low→high durations therefore measure *open-to-high of a trending week*, not *the run after the week's extreme forms*, which is what the taught window describes. The duration finding is genuinely supported by 2 of 4 (EURUSD, GBPUSD, both 3.8 days — still exceeding the window), not 4 of 4. | E02 | Homework §2.4 vs §2.5 Finding A; mastery report §2 | Bears on `C-001`, which is foundational — precision is required before this datum is cited there. Fix: add a scoping sentence to homework §2.5 Finding A and the mastery report §2 table ("supported 2 of 4; the other two measure a different object"). No conclusion changes: the supported half still points the same direction. |

## NOTES (no correction required)

| # | Note |
|---|---|
| N1 | **The C-004 negative claim is now verified on the full sweep, not 24 frames.** The student flagged (audit item 6) that "no session-times slide in V03" rested on a prior session's 50 detected states of which only 24 were personally examined. This review located the prior session's complete 857-frame sweep intact, confirmed its identity pixel-exactly, re-clustered it independently (76 states at a finer threshold than the student's 50), and visually reviewed a representative of every state. **No session-times slide exists anywhere in V03 at sweep resolution.** The one caveat is inherent to the capture cadence itself (a slide shown <5 s could fall between frames), which D-021/D-022 accepted. Mastery report item 6 is discharged; the C-004 record's "checked and negative" status is confirmed. |
| N2 | The re-sweep surfaced one screen state absent from the transcript, the notes, and the index: a housekeeping slide at ~10:50 (*"Easter is Coming… I will open the chat box and ask for a vote. Yes=I'm coming / No= skip the week"*). No operational content; the audio at that point covers the newsletter wrap-up and forum privacy, so the slide was displayed without being read aloud. Recommend one line in `INDEX.md`'s coverage note at the next natural touch. |
| N3 | `INDEX.md` cites `[00:02:00]` as a transcript sanity-check reference; it is not a marker (nearest `[00:01:57]`/`[00:02:05]`). Same class as V01 open item 7's six non-marker approximations; fold into the same deferred `STUDY_PROTOCOL.md` amendment at the 25% review. |
| N4 | **Manual-backtest debt is now three lessons deep** (V01 deferred per D-019/I-007, V02 deferred, V03 deferred). Each deferral has been individually well-reasoned — V03's "backtesting an undefined entry would measure my judgement, not the method" is correct — but the obligation accrues. The moment a testable rule first exists (plausibly the V03 exit rule once "outside structure"/A-033 is defined, or a later lesson's entry), the backlog must be discharged against it, and the reviewer will require it. |
| N5 | The mastery report's ±45 s fuzzy-match window (audit item 1) turned out not to have masked anything: this review re-matched every quote at **exact** marker resolution and found no case where a quote sits at a wrong marker inside the window. The concern was legitimate; the audit survives it. |

---

## RULE FIDELITY — **PASS**

The source notes were checked against a full read of the transcript performed first.
Spot-audited systematically rather than exhaustively re-derived, weighted toward §2
(explicit teachings) and §6 (conditions) as the student requested:

| Student's rendering | Source | Assessment |
|---|---|---|
| §2a block-the-first-8-hours complex (5 quotes) | `[00:12:38]`–`[00:14:06]`, `[00:28:18]`, `[00:29:51]` | Verbatim, hedges retained (incl. the 8→12h extension) |
| §2d second-leg M/W discipline, with the instructor's own hedge | `[00:24:38]`–`[00:25:48]` | Accurate; the *"most of the time with the exception of the third leg"* hedge is preserved, not smoothed |
| §2f swing window/target/exit | `[00:34:54]`–`[00:36:32]` | Accurate; garble flagged rather than repaired |
| §6 conditions table, all 9 rows | markers as cited | All resolve; row 6's converse-inference is labelled as such |
| §10 numbers table | markers as cited | Every number carries its hedge, per the E03 rule |
| §4a/§4c/§4d/§4f slide transcriptions | frames | Word-for-word (independently re-read this session) |

The **citation audit was re-performed independently**: 425 marker citations across five
V03 files were checked for existence (only three non-markers, all legitimate: the
declared V01 cross-reference `[00:35:43]`, whose Friday-*extension* wording was verified
against V01's transcript; the mastery report *describing* a corrected defect; N3's index
reference), and **99 quote+citation pairs were fuzzy-matched at exact marker
resolution — all 99 resolve to real spoken text at the cited place.** The student's
"375 of 377, five defects corrected" claim is consistent with what this review measures,
and all five corrections were verified as actually applied — including §4e, where this
reviewer's own 2× crops of the AJ frame independently find **exactly fifteen `R =`
labels, thirteen fully legible and two partially occluded (`R = 80.x`, `= 47.0`)**,
matching the corrected enumeration.

No omitted qualifier, no example-to-rule promotion, no terminology drift, no
interpretation mislabelled as instruction was found.

## CHART RECOGNITION — **PASS**

The homework applied the block procedure to four charts the lesson never used and
graded honestly. The reviewer recomputed every classification from the raw OHLC:
block levels, first-cut bars, week extremes, and the inside-close-after-cut reads all
reproduce exactly. The 2-of-4 directional result is correctly scored — and audit item 3
(whether USDJPY/USDCHF should count as *successes* under a "ran away from the low"
reading) is resolved **in the student's favour**: with the week's low at bar 0, no cut
of the low exists, so the lesson supplies no long trigger to credit; and the cut-above
that did occur predicted a reversal that never came. Calling those two failures of the
directional reading is right. Boundaries respected, no credit claimed from later
profitability.

## HOMEWORK — **PASS with M1**

| # | Claimed result | Independently verified result | Assessment |
|---|---|---|---|
| 1 | 116/116 within-week open=prev-close transitions exact | **Reproduced: 116/116, zero breaks, all four pairs** | Confirmed |
| 2 | Weekend discontinuities exactly 30 bars apart; USDCHF's genuinely zero-gap boundary disclosed | Consistent with the committed single-week dataset and the stated cadence | Confirmed as disclosed |
| 3 | Block highs/lows, block ranges, cut bars, week extremes, net, week ranges (all four pairs) | **All reproduced exactly from the JSON** | Confirmed |
| 4 | Low→high durations 92/92/96/88 h | Reproduced | Confirmed (scope: M3) |
| 5 | ADR and 3×ADR figures | **Do not reproduce** under any of three conventions; conclusion (0/4 reached) robust under all | **M1** |
| 6 | Real-hover spot checks match harvest | USDCHF chart PNG inspected: crosshair `Sun 02 Aug '26 21:00`, legend `O 0.80552 H 0.80742 L 0.80552 C 0.80685` — identical to harvested bar 0 | Confirmed |
| 7 | Data is real market data | **Externally cross-checked**: ECB reference fixes (12:15 UTC) for all four pairs on all five days fall inside the harvested 09:00-UTC bar's range | Confirmed — the dataset is genuine |
| 8 | DST-inside-week caveat harmless (audit item 2) | No DST transition falls between 2 and 7 Aug 2026 in any relevant jurisdiction (US: 1 Nov; UK/EU: 25 Oct) | Confirmed — the +4h assumption cannot have shifted any label this week |

11a is `FIRST-PASS SUCCESS` as claimed (the two self-caught pre-submission errors are
disclosed in the report, which is the disclosure standard working as intended). 11b
`UNRESOLVED` for the same evidential reason V02's was — fabricating cards would
recreate the quarantined artifact class — and the reviewer accepts that reasoning
again. The V02-era per-check disposition applies unchanged.

## MANUAL BACKTESTING — **DEFERRED (accepted; see N4)**

Not performed, for the stated and sound reason that V03 supplies no entry rule whose
decision point could be defined. The homework is correctly *not* presented as a
backtest. The fourteen §6.G checks are therefore N/A this round. The debt accrues.

## HINDSIGHT / LOOKAHEAD AUDIT — **CLEAN**

The homework analyses completed weeks descriptively and says so; it claims no
entry-decision validity, so hidden-future discipline is not implicated. Losing/
non-conforming pairs were retained and given equal analytic weight (USDJPY and
USDCHF get the same table depth as the conforming pairs). No boundary was drawn using
future data — the block is defined by the week's first two bars only. One structural
observation the student made and the reviewer endorses: **the flashcard method itself
is instructor-prescribed hindsight** (*"you have hindsight in your favor. Don't take
pictures of ones that didn't pay out"* `[01:02:49]`–`[01:02:52]`) — winners-only
memorisation is the course's own design, faithfully recorded, and the mastery report
correctly identifies it as the opposite of discrimination training rather than
adopting it as validation practice.

## POSITIVE / NEGATIVE / BORDERLINE EXAMPLES

Positive: EURUSD and GBPUSD conform to the taught sequence and were verified
bar-by-bar (both cut the block low at Monday 05:00 UTC — the London open — closed
back inside on the next bar, and ran to a Friday high). Negative: USDJPY and USDCHF
are genuine non-conformers, rejected for the correct reason, not straw men.
Borderline: the student's classification of those same two as the borderline cases is
reasonable and disclosed. This is the first lesson with real out-of-lesson chart
evidence in all three categories.

## PROVENANCE AUDIT — **PASS**

No orphan rules. Every §2/§5/§6/§10 assertion carries a marker or a named frame, and
the sampled set (99 quote-level pairs — effectively the file's full quote population)
verified at 100%. The `Q-001`-class failure mode is absent from V03's committed work.

## AMBIGUITIES — **PASS**

Eight new records (A-029–A-036) are properly scoped, all `DO NOT CODE`; six arise
from a single slide's undefined vocabulary and say so. Seven earlier records extended
correctly. **A-026's resolution was verified at the source**: the transcript carries
*"H-O-W high of the week"* at `[00:26:40]` with *"Low of the week"* at `[00:26:55]`
(this reviewer read it in the full-transcript pass before opening the student's
claim), and the 27:39 frame shows the HOW/LOW pen markup. The resolution's scope
guard — label codable, *levels* still A-010/A-033 `DO NOT CODE` — is exactly right,
and the mastery report's refusal to promote the expansion into a concept entry is the
correct application of the firewall. Audit item 4 discharged. The STATUS block
arithmetic (36 records, 2 resolved, 34 `DO NOT CODE`) re-checked: correct.

## CONTRADICTIONS — **PASS**

| Conflict | Student handling | Reviewer status |
|---|---|---|
| C-001 (run duration) | Five more restatements logged, no narrowing; first time-based exit noted as making the count load-bearing | `UNRESOLVED` — correct. Homework durations must carry M3's scoping before entering this record |
| C-002 (both-ways gating) | "Trade both ways" `[00:36:23]` logged as cutting against the V01 gate; two readings held open | `UNRESOLVED` — correct |
| C-003 (M/W failure) | V03's hedged restatement logged as supporting the rhetoric explanation, not resolving | `UNRESOLVED` — correct, and the reasoning (C-003 is internal to one V02 sentence) is precise |
| C-004 (London open) | Deliberate check performed, negative; "3 30 in the morning" on the DST date noted as weakly cutting against explanation 1; V03 struck off the resolution route | `UNRESOLVED` — correct, **and the negative is now confirmed on the full sweep (N1)** |
| The examined-and-not-logged candidate ("swing trades pay none" vs 3×ADR) | Reasoning recorded | Reviewer agrees — logging it would manufacture a conflict |

## MACHINE-RULE FIREWALL — **PASS**

Four candidates parked in the interpretation file as `INFERRED MACHINE CANDIDATE /
NOT A COURSE RULE / DO NOT CODE`, each with the reason it is not codable. The
card-specific numbers (18-pip stop, 25-pip pull-back, 1h30m hold) are held as
*example facts*, explicitly not parameters — the precise discipline the firewall
exists to enforce. Nothing quantified without support.

## TEACH-BACK ASSESSMENT — **PASS**

Mastery report §1A (unaided recall) plus §2 (the three-part decomposition:
measurement complete and codable-pending-A-019 / entry not testable with six of
eleven criteria undefined / exit closest-yet but failing on one undefined term)
constitutes an accurate, appropriately humble teach-back. The §2 decomposition is
better than a recitation — it states what confirms, what invalidates (nothing stated;
flagged as the three-lesson gap), and what remains subjective.

## BLIND RECOGNITION TEST

Not separately administered this round: the homework itself functions as one (four
charts outside the lesson, classified with a checkable procedure, two correctly
called as non-conforming), and dimension-B recognition of the *setup* — as opposed to
the measurement — is not yet testable for the reasons the student states. Carried
forward with the manual-backtest obligation (N4).

---

## STUDENT MASTERY ASSESSMENT

| Dimension | Student said | Reviewer assessment |
|---|---|---|
| A. Recall | PASS | **Agree** |
| B. Recognition | PARTIAL | **Agree** — the distinction "recognising a measurement is not recognising a setup" is the correct standard, applied to themselves |
| C. Discrimination | FAIL (honest) | **Agree**, and the 4-of-4-fires / 2-of-4-works argument is the best evidence yet recorded for *why* it fails |
| D. Sequence | PARTIAL | **Agree** — the missing-invalidation row is real and now three lessons deep |
| E. Exceptions | PASS | **Agree** |
| F. Homework | 11a FIRST-PASS SUCCESS / 11b UNRESOLVED | **Agree**, with M1/M3 as precision debts on 11a's write-up |
| G. Manual backtesting | DEFERRED | **Agree** (N4: the debt accrues and will be called) |
| H. Provenance | PASS | **Agree** — independently verified at 100% on the sampled population |
| I. Ambiguity | PASS | **Agree** |
| J. Contradictions | PASS | **Agree** |

The self-assessment required no downgrades. Audit items 1–6 from mastery report §4:
1 discharged (N5), 2 discharged (Homework row 8), 3 resolved in the student's favour
(Chart Recognition), 4 discharged (Ambiguities), 5 grades upheld as neither generous
nor harsh, 6 discharged by full re-sweep (N1).

---

## REQUIRED CORRECTIONS (all MINOR — gate-opening under D-024, owed before COMPLETE)

1. **M1** — In `V03_HOMEWORK.md` §2.5 Finding B: state the day-boundary convention
   used for the five daily ranges, and commit those ranges (in the section or in
   `weekly_bars_2026-08-02.json`) so the four ADR figures re-derive. If the original
   convention cannot be reconstructed, recompute under a stated one and update the
   four figures; the 0-of-4 conclusion will survive.
2. **M2** — In `V03_TRANSCRIPT.md` COVERAGE: replace *"timestamps strictly monotonic,
   no duplicates"* with an accurate statement (non-decreasing; 1,230 entries, 1,227
   unique; three benign same-second adjacent pairs at `[00:35:21]`, `[01:00:13]`,
   `[01:04:30]`).
3. **M3** — In `V03_HOMEWORK.md` §2.5 Finding A and `V03_MASTERY_REPORT.md` §2:
   scope the duration finding to the two pairs where a week extreme actually formed
   after a cut (EURUSD, GBPUSD — both 3.8 days), and state that USDJPY/USDCHF
   measure open-to-high of a trending week instead. Apply the same scoping to any
   future citation of this datum against `C-001`.

---

## REVIEWER QUESTIONS

None requiring student response this round. N2 and N3 may be folded into the
correction commit at the student's discretion.

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
- M1 ADR figures not reproducible from committed data (E19)
- M2 transcript coverage block overclaims monotonicity (E20)
- M3 duration finding scoped to 4 of 4 where 2 of 4 is supported (E02)

REQUIRED ACTIONS:
1. Apply corrections M1–M3 (documentation-precision; no conclusion changes).

ADVANCEMENT:
AUTHORIZED — per D-024, 0 CRITICAL + 0 MAJOR opens the V04 gate. The three
minors are carried in REVIEW_INDEX.md and must be applied (and verified at V03's
next review touch) before V03 is marked COMPLETE.
```
