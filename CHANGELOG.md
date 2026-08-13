# CHANGELOG

Notable structural and methodological changes to the MMM-MASTERY project.

This file records **project-level** changes — architecture, protocols, standards,
phase transitions. Day-to-day study work belongs in `LOG.md`; review decisions
belong in `18_REVIEW/`.

Format is loosely based on [Keep a Changelog](https://keepachangelog.com/).
Newest first.

---

## [0.10.0] — 2026-08-13 — V06 gets a real backtest; D-032; the probe that failed usefully

### Added

- **`DECISIONS.md` `D-032` (PROVISIONAL — owner ratification requested)** — *guest material may
  be **tested**, never adopted; a test is not a citation.* Refines `D-025` without superseding
  it and leaves `D-030` explicitly untouched.
- **`PT-022` → `PT-023` → `PT-024`** and **`06_MANUAL_BACKTEST/V06/BT_V06_0001.md`** — the
  project's **first executed manual backtest**. All three pre-registrations committed before the
  data existed.
- **`05_HOMEWORK/V06/scripts/comprehension_probe.py`** — 48 machine-checked claims, 33 recalled
  closed-book and 15 plausible falsehoods that must be absent.
- **`05_HOMEWORK/V06/scripts/crosscheck_second_source.py`** and `V06_HOMEWORK.md` §9 — an
  independent second-vendor cross-check.

### Changed

- **`D-028`** — first 70/30 boundaries pinned and appended, and **scoped** to one series each.
- **`V06_MASTERY_REPORT.md` dimension G** regraded `NOT APPLICABLE` → **PERFORMED**, superseded
  grade retained.
- **`V06_SOURCE_NOTES.md` §10 and §7** corrected — both by the probe, not by a reviewer.

### Notes — the three results worth carrying forward

- **The backtest returned `INDISTINGUISHABLE FROM THE NULL`, and the interesting part is the
  arm divergence.** A one-hour clock shift flips the sign of the raw London-vs-New-York
  difference. What survives both arms is the duration-normalised comparison: **London is the
  more active window per hour**. So the guest's claim looks **true about intensity and unproven
  about total range** — the exact asymmetry `PT-022` §2a predicted before any data existed,
  because the New York window is 36% longer. **The pre-registration earned its keep by
  predicting the confound that turned out to matter.**
- **A probe written to catch imported fabrications caught two omissions of my own instead** —
  a missing *"Asian box"* citation and an unrecorded 90% figure. **Negative controls are worth
  more than positive recall**, and this is the evidence for it.
- **A second vendor confirmed the homework's numbers and demoted one of its inferences.**
  *"480 bars in a trading week"* is a fact about the FXCM feed, not the market: Yahoo opens the
  FX week two hours later, 13 weeks out of 13. Six pre-registered weekly-window tests inherit
  that. And two vendors can differ by **37–45 pips on a single bar's low**, which constrains
  every future backtest that triggers on a specific bar.

---

## [0.9.0] — 2026-08-12 — V06 student pass; D-025 applied to a lesson that costs something

### Added

- **`02_TRANSCRIPTS/V06/V06_TRANSCRIPT.md`** — I-008 verified and adopted. 1,304 markers,
  strictly increasing, final `[01:14:32]` against measured audio 4473.63 s; SWF header and
  manifest agree to within 0.7 s. Five Whisper `small.en` windows spanning the lesson all
  match near-verbatim.
- **`04_SCREENSHOTS/V06/`** — 32 curated frames from a 903-frame 10× Ruffle sweep, each
  carrying the player's burned-in timecode, plus `INDEX.md` with a per-frame
  `DESCRIPTIVE` / `NORMATIVE — EXCLUDED` verdict and a 4× transcription of the **DMR
  Curriculum 2012**.
- **`03_LESSON_NOTES/V06_SOURCE_NOTES.md`**, **`V06_INTERPRETATION.md`**,
  **`07_MASTERY_REPORTS/V06_MASTERY_REPORT.md`**, **`05_HOMEWORK/V06/`**.
- **`A-050`–`A-054`** and **`C-006`** (guest-vs-guest stop-hunt divergence, corpus-hygiene
  class); **`Q-006`** (sixth of six fabrication audits).
- **Three committed, re-runnable tools**, all under `05_HOMEWORK/V06/scripts/`:
  - `check_quotes.py` — verifies that every `[HH:MM:SS]` citation in an artifact resolves
    to a transcript marker **and** that every quoted fragment occurs in the cited window.
    This is the `E01`/`E11` discipline from V05 R1–R2 turned into a gate the student runs
    **before** submission rather than a finding the reviewer raises after it.
  - `f0_profile.py` — a voice-pitch screen for an **unannounced speaker change inside one
    file**, validated against V04's known handover, which it finds unprompted. Explicitly
    **not** a cross-file speaker identifier.
  - `measure_v06.py` / `render_v06.py` — the homework's measurements and figures, computed
    from committed JSON.

### Changed

- **`00_SYSTEM/COURSE_PROGRESS.md`** — V05 reconciled to `COMPLETE` (its R3 `PASS` had been
  recorded in `REVIEW_INDEX.md` but not here); V06 row and `V06 GATE` block added; `NEXT
  ACTION` rewritten to name what the V06 reviewer should test hardest.
- **`10_AMBIGUITIES/`** and **`11_CONTRADICTIONS/`** status blocks re-derived in the same
  commit that added their records.

### Notes — what this release is actually about

- **V06 is the second consecutive lesson with zero course-author runtime, and the first
  where `D-025` is expensive.** V05 was excluded and gave up little. **V06 states a complete
  tradeable system** — trigger, pattern filter, location rule, counting rule, pullback band,
  stop geometry, 2:1 target, two-hour time stop, reversal exit — **and all of it is
  excluded.** Doctrine produced: **zero**. Interpreted rules: **zero**. Concept-library
  entries: **zero**, deliberately.
- **The reviewer's question changes shape here.** For V01–V04 it was *did the student find
  the rules*. For V06 it is *did the student keep them out*.
- **Two extensions that look like answers are recorded as weakening one.** `A-044`: V06
  enumerates the admissible patterns for the first time in the corpus, and the DMR
  curriculum prints six or seven where the audio says three. `A-011`: V06 supplies the first
  candle count ever attributed to the instructor for M/W, and its own reporter withdraws it
  four seconds later.
- **`A-018` records the corpus's first negative result** on the *"R = risk multiple"*
  reading: V06 states both a stop and a 2:1 ratio, and neither connects to any printed
  `R = ` label.
- **The homework's headline result is methodological, not market.** The undefined ADR
  lookback moves *"ADR ÷ 3"* by **31–60 %** across five reasonable windows on four pairs —
  GBP/USD's push is 15 pips or 23 pips depending on a parameter nobody has stated. That is
  `D-030`'s prohibition demonstrated in numbers rather than argued.
- **A negative reproducibility finding worth more than a clean one:** against V05's
  committed JSON for the same week, all 1,912 timestamps and bar counts match exactly, but
  120 USDJPY and 66 USDCHF bars differ in OHLC by up to ~1 pip. **Any future claim of exact
  reproducibility on this feed is false at that precision.**
- **A process deviation is disclosed rather than claimed away:** the recipe's §9
  transcript-before-screenshots order was **not** achieved, because §§7–8 require looking at
  contact sheets to curate. The disclosure is worded identically in the three files that
  carry it — the `V05 R1 M4` failure class, avoided by construction.
- **Three items are escalated to the owner/reviewer**, not decided here: a third mastery
  disposition (`EXCLUDED BY DECISION`) for work that has subject matter but is forbidden;
  whether the project needs to be able to say a record is **unresolvable in principle**; and
  making speaker identification a written **procedure** rather than a bare requirement.

---

## [0.8.0] — 2026-08-12 — V05 PASS at R3; lesson COMPLETE

### Added

- **`18_REVIEW/V05/V05_REVIEW_R3.md`** — remediation verification of R2's `M7`–`M11`
  (open items 47–51). All five verified applied, **each re-derived from primary source
  before the remediation diff was read**; the `M11` marker-existence sweep re-run from
  scratch (1,353 markers, 7 non-resolving citations, all accounted for — cluster closed
  at three); frame 26's disputed left `R = ` label read a third time and upheld as
  *value not legible* (R1B's `74.6` stays untranscribed). **PASS, HIGH, 0/0/0.**

### Changed

- **V05 is `COMPLETE`** — the first lesson closed on a four-file review lineage
  (R1 ∥ R1B → R2 → R3). `REVIEW_INDEX.md` STATUS now reads `PASSED: 5`,
  `IN REMEDIATION: 0`; open items 47–51 closed; decision table gains the R3 row.
- Owner items carried unchanged: open items 35, 36 (dimension-B/G re-labelling
  blocked on it), 40; R1B naming; parallel-session ruling.
- Next review trigger: **V06 submission**, or `CUMULATIVE_25.md` if it arrives first.

---

> ✅ **MERGE NOTE RESOLVED 2026-08-12.** Two lines of work branched from `3a13441` and each
> claimed `[0.7.0]`. Canonical numbering assigned by commit chronology: the V05 student pass
> (03:19 EDT) keeps **`[0.7.0]`**; the backtest-evidence-standard lineage (from 21:52 UTC the
> same day) is renumbered **`[0.7.1]` → `[0.7.3]`** (was `0.7.0`–`0.7.2`). No file outside
> this changelog cited any `0.7.x` string (verified by repo-wide grep), so no cross-reference
> breaks. Entries reordered newest-first; no entry's content was altered. The original merge
> note read: *"DUPLICATE VERSION NUMBER `[0.7.0]`, OWNER RECONCILIATION OWED … Neither was
> renumbered on merge … newest-first ordering is therefore broken across this region."*

## [0.7.3] — 2026-08-11 — Timezone as a tested variable; PT-001 unblocked

### Added

- **`D-031`** — session timezone is a **tested variable, not an assumption**. Two
  pre-registered arms: **A** fixed `UTC−5`, **B** DST-aware `America/New_York`. **Both
  always reported**; divergence is a finding, never a selection criterion.

### Changed

- **`A-019` updated and deliberately kept OPEN.** The source declines to specify, so it
  cannot close from evidence; `D-031` governs project method only and may never be cited
  as instruction.
- **`PT-001` is unblocked** and now carries the two-arm design, the two-draws caution,
  and a recommendation to choose a development window that **straddles a DST transition**
  so the arms can be compared within one sample.

### Fact of record

The bootcamp ran **2012-03-18 → 2012-06-17, entirely within US daylight saving**. Arm B
reproduces the instructor's own stated times during that window; **Arm A displaces every
one of them by an hour.** That is evidence about the source, not a resolution of what the
method requires — his table may genuinely have been taught as fixed clock numbers.

---

## [0.7.2] — 2026-08-11 — Owner decisions; PT-001 pre-registered

### Added

- **`D-028`** — manual-phase development/holdout split is **70/30** (oldest 70%
  development). Exact dates pinned at the first data-source decision, not invented now
  (`I-007` still open).
- **`D-029`** — baseline parameters: 1,000 iterations for headline results, random seed
  recorded, entry window matched to the rule, **two arms** (direction-matched primary,
  random-direction secondary).
- **`D-030`** — blocked tests wait for the course; definitions are **never**
  approximated. Generalizes `A-039`'s TDI prohibition to `A-011`, `A-004`, `A-002`,
  `A-019`. Accruing backtest debt is correct behaviour, not a backlog to clear.
- **`06_MANUAL_BACKTEST/PRE_REGISTERED/PT-001_…md`** — the one test available before
  the course teaches more: does the Asian range boundary carry predictive content?

### Changed

- `DECISIONS.md` open-decisions table: both `OWED NOW` items cleared.
- `REVIEW_INDEX.md`: item 53 closed; items 54–55 added *(renumbered from 35/36–37 on 2026-08-12 — see the resolved merge note in `REVIEW_INDEX.md`)*.

### Finding

**`PT-001` is blocked by exactly one thing — `A-019`, session times printed with no
timezone** — and unlike every other blocker in V01–V04 this one plausibly closes from
*existing* evidence rather than a future lesson. That makes a small timezone evidence
pass the highest-leverage work item currently available.

---

## [0.7.1] — 2026-08-11 — Backtest evidence standard

### Added

- `00_SYSTEM/BACKTEST_EVIDENCE_STANDARD.md` — baseline requirement, period
  pre-registration, holdout reserve, sample sufficiency, and the DESCRIPTIVE /
  EVIDENTIAL / INVALID classification.
- `DECISIONS.md` **D-026** (baseline mandatory, hard gate) and **D-027** (period
  pre-registration and holdout reserve).
- `REVIEW_PROTOCOL.md` §6.G checks **15–20** and error codes **E21–E25**.
- `MANUAL_BACKTEST_TEMPLATE.md` **§0 pre-registration block** (completed before any
  chart in the range is opened) and **§9b result classification**.
- `scripts/validate_project.py` — `check_backtest_evidence_gate()`: fails if a `BT_`
  observation exists without D-026/D-027, without a §0 block, without a classification,
  or quoting a bare percentage. Negative-tested on all four failure modes.

### Context

An external methodological review asked four questions: does a test run exhaustively
or search for matches; are losers filtered; is there a train/test split; what is the
baseline. Answers were: exhaustive by design but never exercised; retained and enforced
at three layers; **no split**; **no baseline anywhere in the repository**.

This release closes the last two. Adopted while `06_MANUAL_BACKTEST/` held **zero**
observations, so **nothing required rework** — the standard exists before the first
record, which is the only point at which that is free.

---

## [0.7.0] — 2026-08-11 — V05 student pass: the first lesson that yields no doctrine

Student round. Clean retry after a prior V05 attempt hung. **V05 is the first lesson in the
corpus with zero course-author runtime**, so `D-025` applies to 100% of it and the lesson
contributes **no admissible rule at all** — a correct result, not a failed study.

> **Numbering note.** This entry follows `[0.6.0]` directly because **V04's student pass and
> its two review rounds were never changelogged** — they are recorded in `LOG.md`,
> `18_REVIEW/V04/` and `COURSE_PROGRESS.md`, but not here. The gap is pre-existing and is
> flagged rather than papered over by skipping a version. `D-025`, which governs this
> lesson, was recorded during the V04 remediation and likewise has no changelog entry.

### Added

- **V05 student pass complete**, submitted as `REVIEW REQUIRED` (not `PASS`): source notes,
  interpretation, 30 curated screenshots (+5 at 2×), homework on real data, mastery report,
  `A-042`…`A-049`.
- **`05_HOMEWORK/V05/scripts/tv_harvest_v05.mjs`** — a TradingView harvester that captures
  each bar's **own Date and Time** alongside its OHLC, from the platform's Data Window.

### Changed

- **Week and day boundaries in homework are now READ, not INFERRED.** This is a
  methodological change to how the project harvests price data, made in response to V04
  review R1 finding `M1`. V04's harvesters captured OHLC only, so boundaries had to be
  inferred from bar cadence, and that inference failed silently on USDCHF. The class of
  error is now structurally unavailable.

### Verified

- **USDCHF's late session open is a reproducible property of the feed, not a one-off.** Its
  week opens at 22:00 against 21:00 for the other majors, giving 476 15-minute bars rather
  than 480 — **independently reproducing V04 review R1's corrected figure** from a different
  week by a different method, with the cause directly visible. 1,912/1,912 continuity
  transitions, zero breaks, across four pairs.
- **The capture served the right film, proved at the byte level:** the decompressed original
  and the working copy differ in **exactly one byte, at body offset 18** — the frameRate
  `UI16` — with `frameCount` 12,304 unchanged. Four stale servers from earlier sessions were
  found holding ports 8899/8917/8931/8945 (`D-022`, GOTCHA 4).

### Corrected

- **`EMA` occurs twice in V05, not three times** — a count carried by two already-committed
  files (`V05_TRANSCRIPT.md`, `QUARANTINE_REGISTER.md` `Q-005`). Recorded in place rather
  than silently patched elsewhere. No conclusion in either file changes.

### Open questions raised for the owner

- **`A-042` — an out-of-corpus dependency.** The V05 presenter repeatedly defers the
  operative detail for levels/reset, nameable patterns, railroad-track size and traps to the
  **DMR**, a programme this library does not contain. If that testimony holds, some `A-xxx`
  records may be **unresolvable from this corpus in principle** rather than merely unresolved,
  and the project has no way to express that distinction.
- **A third disposition may be needed** alongside `NOT APPLICABLE` and `DEFERRED` (`D-018`,
  `D-019`) for work that is **excluded by decision** rather than absent or postponed. V05 is
  the first lesson to need it, and it is the sole reason its mastery report is
  `REVIEW REQUIRED`.

### Notes

- **Nothing from V05 entered the master spec, machine spec or concept library**, including
  the sharpest idea in the lesson — a clean stop-hunt vs trap-move discriminator, held as
  research question `A-049`. The temptation to promote guest material because it is good is
  the exact failure mode `D-025` exists to prevent.
- **Speaker identification is now the first step of every remaining lesson.** Instructor
  runtime across one session date runs ~100% (V03) → ~31% (V04) → 0% (V05).

---

## [0.6.0] — 2026-08-10 — V03 student pass; first ambiguity resolved on spoken evidence

Student round. Clean retry after a prior session hung mid-write on `V03_SOURCE_NOTES.md`.

### Added

- **V03 student pass complete**, submitted as `REVIEW REQUIRED` (not `PASS`): source
  notes, interpretation, homework 11a, and `07_MASTERY_REPORTS/V03_MASTERY_REPORT.md`.
- **`A-029`–`A-036`** in `AUTOMATION_AMBIGUITIES.md`. Six of the eight are the vocabulary
  of a single slide — the sample flashcard's entry-criteria list — which asks the student
  to verify eleven conditions, six of which the course has never defined.
- **`05_HOMEWORK/V03/`** — four majors, 4H, one real week, with the raw 120-bar OHLC
  dataset committed alongside the analysis so a reviewer can recompute every number.

### Changed

- **`A-026` is RESOLVED — the first ambiguity this project has closed on *spoken*
  evidence.** V03 `[00:26:40]` spells the abbreviation out: "H-O-W high of the week".
  This settles the week-vs-day question and positively contradicts the quarantined
  `RULES.md` reading of "HOD/LOD", which is one more independent confirmation that the
  fabricated files invent detail. (`A-003`, the only prior resolution, was closed by text
  printed on a slide.)
- **`CONTRADICTIONS.md`: evidence on all four records, no new record opened.** `C-004`'s
  "Required to resolve" field named V03 specifically as the place to check; that check was
  performed and returned **negative** — no session-times slide, London open never
  mentioned. V03 is struck off the resolution route.
- `COURSE_PROGRESS.md`: V03 row → `AWAITING REVIEW`; **V04 GATE block added and CLOSED**.
- `CONCEPT_INDEX.md`: still zero concepts (deliberate — `A-026` is an abbreviation
  expansion, not a method concept); stale `LESSONS STUDIED` corrected 1 → 3.

### Methodology

- **Inherited artifacts are now audited before adoption, not trusted on sight.** The two
  files left untracked by the hung session were adopted only after a mechanical citation
  audit: 377 markers checked (375 verbatim), 96 quote+timestamp pairs matched at their
  cited marker, **5 minor defects found and corrected**. The audit distinguished
  *interrupted honest work* from the fabrication class quarantined in `Q-001`–`Q-003` —
  a distinction this project had not previously had to make.
- **Chart measurement no longer reads pixels.** V02's `MAJOR` came from pixel reading
  corrupted by a price line sharing a colour with bullish candles. V03's homework harvests
  the platform's own OHLC legend as DOM text and validates it three ways, including using
  V02's R2/R3 weekend-gap finding as a *positive* test: the open-equals-previous-close
  chain must hold within a week and break at weekends, and it did exactly that —
  116 of 116 transitions exact, gaps landing exactly 30 bars apart.

---

## [0.5.2] — 2026-08-10 — V02 R2: MAJOR closed, `REVISE` on three minors

Reviewer round only. **No student artifact was edited** — the reviewer does not remediate.

### Changed

- **V02 R1's MAJOR is CLOSED.** `18_REVIEW/V02/V02_REVIEW_R2.md` re-measured the committed
  USD/CHF PNG independently — own candle detection, own sub-pixel axis calibration
  (52.276 px per 0.00100, max residual 0.088 pip), own bar lattice, 177 bars — and **every**
  corrected price, day, direction and hour in `V02_HOMEWORK.md` §1.2 reproduces to within
  0.2 pip, as does §1.3's 72-hour `C-001` result. `E06` closed.
- **V02: `REVISE` (HIGH), 0 critical, 0 major, 3 minor.** Advancement not authorized.
- **⚠ The D-004 V03 gate is being breached.** A V03 student pass appeared in the working
  tree *during* R2 — transcript marked COMPLETE, `Q-003` register entry, two created
  directories — while `V03 GATE: CLOSED` and V02 is unpassed. **Second occurrence, and
  unlike the first it is not moot.** Recorded as a **process** MAJOR, kept out of V02's
  mastery counts, left untouched and unstaged. **The V03 pass must stop until V02 passes;
  the V03 work must not be deleted.** `REVIEW_INDEX.md` open item 9 escalated from
  `OPEN — process` to a live breach.
- **`REVIEW_INDEX.md` severity totals: no open MAJOR** for the first time since V01 R1.

### Added

- **Two chart-verification techniques that should become standard**, both used at R2 and
  neither used before in this project:
  1. **The chart header prints the last bar's own OHLC.** Comparing a measurement against
     it is absolute ground truth for the calibration, independent of the axis labels. This
     is what substantiates the `±0.5 pip` claim (measured error ≤ 0.3 pip) rather than
     leaving it asserted.
  2. **TradingView draws its own dotted vertical day separators.** They are in the PNG, in
     `rgb(213,213,213)`, and they state the day boundaries outright — which is the one thing
     both prior measurements of this chart got wrong.
- **`REVIEW_INDEX.md` open items 12–14** — the §1.1 day-boundary correction, the untracked
  measurement script, and the promotion of R1's proposed mechanical status-block check in
  `validate_project.py` from suggestion to work item.

### Methodological findings

- **A validity check must be applied where its assumption holds.** §1.1's *"measured open
  equals prior close"* test is sound *within* a session — it verified 174 of 176 bar
  boundaries at R2 — and worthless **across a weekend**, which is the one boundary it was
  used to settle. Choosing the day mapping that makes a real 12.6-pip weekend gap vanish is
  not validation. This is the round's generalisable lesson and is carried to
  `CUMULATIVE_25.md`.
- **The parts of a source you did not read are not thereby ambiguous.** §1.1 measured six of
  the eight date labels, got all six right, and declared the remaining two *"ambiguous"*.
  Measured, they land on their bars to 0.88 px and 0.03 px. This is the R1 lesson — *a chart
  is a source document* — one step further on.
- **A stated rule did not prevent the defect it was written for — twice, in one day.**
  `COURSE_PROGRESS.md`'s status view went stale inside the very commit that declared the
  SUMMARY authoritative (fifth occurrence of that class); and D-004's V03 gate was breached
  a second time while a review was naming it as the test. Both are written rules with no
  enforcement. **The answer to both is a check, not another sentence** — status blocks are
  arithmetic over their own file's contents, and a `VNN GATE: CLOSED` pre-flight guard in
  `validate_project.py` is mechanically checkable. Promote both at the 25% review.
- **Recorded against R1, not the student.** R1's provenance audit signed off on
  *"`PFH`/`PFL` each appear once"*; both occur **zero** times. The conclusion it supported
  (dropping the derived `Primary Topics` block) is **strengthened**, so I-008 stands. The
  remediation escalated this rather than silently fixing it, which is the only reason the
  reviewer error is visible — and is the behaviour the two-agent design exists to produce.

---

## [0.5.1] — 2026-08-10 — V02 R1 remediation applied; awaiting R2

### Changed

- **V02: `IN REMEDIATION` → remediation complete, awaiting R2.** All ten of R1's required
  corrections applied. Fix-only pass; no verdict rendered, per `D-003`.
- **Homework 11a redone from measurement, not reworded** (`REMEDIATION_PROTOCOL.md` §2).
  The invalid first pass is preserved in place as
  `SUPERSEDED — INVALID READING (R1 MAJOR 1)`.
- **The "at least 3 days" confirmation is WITHDRAWN.** The corrected week is recorded
  against `C-001` as **explicitly non-resolving**, and commits no day-count value. The
  measured result — price held below Monday's high for exactly 72 hours — is stated and
  then declined, because three defensible counting conventions give three different
  answers and the level itself was reader-selected (`A-004`).

### Added

- **A stated method for reading charts** (`V02_HOMEWORK.md` §1.1). This is the
  methodological point of the release: `E06` entered the register because *sources* were
  held to a citation standard and *price* was held to none. Chart readings are now
  pixel-measured, calibrated by least squares against the axis labels, and
  **self-validated** (measured daily open must equal the prior day's close). The first
  pass had no check of any kind.
- **A named authority for two chronically stale summary blocks.** `CONTRADICTIONS.md`'s
  STATUS defect was R1's *fourth* occurrence of the same class, so the values were not
  merely corrected: each file now names which block is authoritative (the INDEX table;
  the SUMMARY block) so duplicates are reconciled rather than re-incremented.

### Flagged

- `PFH`/`PFL` are stated in two files to *"each appear once"* in V02. Recount: the
  abbreviations appear **zero** times in the verbatim body. R1 recorded verifying this
  claim, so it is escalated to R2 unedited rather than silently corrected.

---

## [0.5.0] — 2026-08-10 — V02 reviewed: REVISE; V03 gate holds

### Added

- `18_REVIEW/V02/V02_REVIEW_R1.md` — first independent review of V02. **`REVISE`**,
  confidence HIGH, 0 critical, 1 major, 5 minor, 6 notes. Produced by a session that
  wrote none of V02's artifacts, so `D-003` is satisfied for the first time since
  V01 R2.

### Changed

- **V02: `AWAITING REVIEW` → `IN REMEDIATION`.** Ten required corrections.
- **`E06` (false positive) enters the error register**, and it is a new *class* for this
  project. Every prior defect concerned citing sources; this one concerns **reading
  price**. The V02 homework's chart markup states days and levels its own committed PNG
  does not show, and concludes from them that a real week confirms the "at least 3 days"
  doctrine — the exact quantity `C-001` has open. Measured from the image: Monday's high
  is 0.81150 not ~0.8130, and the reversal the markup places on Friday is Thursday's
  move, with Friday running the opposite way. **Protocol implication:** chart-derived
  claims need the same verifiability standard as transcript-derived ones — a markup keyed
  to dates and prices should be reproducible from the image by someone who was not there.
- **`E20` rises to 13, four open.** `CONTRADICTIONS.md`'s STATUS block is wrong for the
  **fourth** time, and this time the error was introduced by the R3 edit that was
  correcting that same block. Recommend the 25% review promote the session-close re-read
  to a requirement *and* consider a mechanical check in `validate_project.py` — every one
  of these failures is arithmetic over the file's own contents.
- **`E11` did not recur.** V01's dominant defect across three rounds; ~20 V02 citations
  sampled, all resolved to markers carrying their words.
- `REVIEW_INDEX.md` open items: **10 added** (C-001's only empirical datum was misread —
  record what the corrected week actually shows, including "nothing"); **11 added and
  closed** (the `A-006`/`A-003` spot-check R3 requested — both pass, verified against the
  frames).
- `COURSE_PROGRESS.md`: `V03 GATE` note strengthened. V02 is `REVISE`, not `PASS`, so the
  gate is live. Open item 9 records that the last one did not hold; this is the test.

### Upheld

- The V02 homework's **data substitution** (a 2026 week for the paywalled 2012 week) —
  honestly handled, evidenced, and better than deferring outright.
- **11b's `DEFERRED`** — verified independently that M/W anatomy is undefined across both
  lessons. Producing forty flashcards would require inventing it.
- **Q-002's quarantine** — verified complete at the filesystem level.
- **The wrong-file capture is contained** — nothing derived from it survives into the notes.

### Notes

- No student artifact was edited by the reviewer session. Findings 2–9 are remediation
  work for a separate session, per `D-003` and the R3 precedent.
- The 40× / 10× figures in `D-021`, `SWF_CAPTURE_RECIPE.md` §10 and
  `04_SCREENSHOTS/V02/INDEX.md` are **not** in conflict: 40× is the measured capability,
  10× the chosen operating point. Recorded because the two appear together often enough
  to read as a contradiction.

---

## [0.4.0] — 2026-08-10 — V01 PASSED at R3; V02 gate opens

### Changed

- **V01: `IN REMEDIATION` → `COMPLETE`.** `18_REVIEW/V01/V01_REVIEW_R3.md` returns
  **`PASS`** (HIGH, 0 critical, 0 major). All 15 required actions from R2 applied and
  verified against the source. The first lesson in the corpus to pass.
- **`D-004` gate: V02 opens; V03 does not.** `COURSE_PROGRESS.md` gains an explicit
  `V03 GATE: CLOSED` line. Logged with it: the V02 student pass ran while the V02 gate
  still read `CLOSED` (`REVIEW_INDEX.md` open item 9).
- `A-006`'s trailing "one candidate reading ELIMINATED" block **withdrawn in place** —
  header changed, original text retained and marked `DO NOT CITE`, refutation recorded
  beside it. This supersedes two statements in `[0.3.0]` below: *"`A-006` had one of its
  two competing readings eliminated"* and *"eliminated one of two competing readings"*.
  **Both are false.** The `[0.3.0]` entry is left unedited as the historical record;
  this line is the correction.
- `A-003` promoted from a record that contradicted itself in five fields to one that
  states its resolution consistently throughout.
- The stale *"no screenshot exists for V01"* assertion cleared from all 16 remaining
  ambiguity records — three with fresh visual determinations (`A-002`, `A-008`, `A-016`,
  all *materially constrained*, all still `DO NOT CODE`), three with slide-text evidence,
  one with an explicit "frame exists, defines nothing" note.
- **Eleven citations corrected across three review rounds.** Every quotation in the V01
  corpus now resolves to a transcript marker carrying its words.
- `SETUP_ISSUES.md` `I-006` now points to `D-021` (frame-rate speedup works at 40×)
  rather than describing it as untested.

### Notes

- **This round was remediation and review in one session**, contrary to `D-003`, at the
  project owner's direction. Disclosed at the head of `V01_REVIEW_R3.md`. Every
  determination was verified against the primary source, and three of R2's own claims
  were corrected in the process — but no independent session audited this round, and the
  V02 reviewer is asked to spot-check `A-006` and `A-003`.
- **Six timestamp approximations were deliberately left uncorrected.** They resolve to the
  right passage; fixing them is the `STUDY_PROTOCOL.md` amendment deferred to the 25%
  review, and applying an unadopted rule retroactively was judged the worse error.
- `C-001` (the day-count contradiction) travels forward `UNRESOLVED`. **V02 did not
  resolve it**, which matters — C-001 named "a later lesson refines it" as its most likely
  route out.

---

## [0.3.0] — 2026-08-10 — V01 screenshots; capture problem solved; V01 submitted for review

### Added

- **`00_SYSTEM/SWF_CAPTURE_RECIPE.md`** — reusable, fresh-session recipe for processing
  one lesson video end to end: Ruffle WASM in headless Chrome via Playwright, offset
  calibration, mux, sync verification, screen-state detection, curation, and the study
  order. Includes the routes already ruled out and three specific gotchas that each cost
  a debugging cycle.
- **22 screenshots** in `04_SCREENSHOTS/V01/`, indexed, each carrying the player's
  burned-in timecode so it proves its own timestamp.
- **`07_MASTERY_REPORTS/V01_MASTERY_REPORT.md`** — status `REVIEW REQUIRED`.
- **`D-018`** — dimensions F and G may be `NOT APPLICABLE` where a lesson supplies
  nothing to satisfy them. Sets the standard for all 21 lessons.
- **`A-018`** — the `R = <number>` box labels, logged rather than guessed.
- `V01_INTERPRETATION.md` **§10** — what the visuals changed, appended without editing
  §§1–9.

### Changed

- **`I-006` (screenshot capture) `OPEN` → `RESOLVED`.** These SWFs contain no video
  stream, so `ffmpeg` can never extract frames; Ruffle's WASM build renders them
  correctly. CloudConvert is no longer needed.
- `A-003` `DO NOT CODE` → **`RESOLVED BY COURSE`** — "pendings", printed on a slide,
  never spoken aloud.
- `A-004`, `A-006`, `A-015`, `A-001`, `A-009`, `A-017` gained visual-evidence updates.
  `A-006` had one of its two competing readings eliminated.
- `V01_SOURCE_NOTES.md` §4 replaced with thirteen real visual observations; the original
  "no screenshot exists" text preserved and marked superseded.
- V01 processing status → `STUDENT COMPLETE`; `COURSE_PROGRESS.md` → `AWAITING REVIEW`.

### Notes

- **Interpretation was written from the transcript alone, before any screenshot
  existed, and was not rewritten afterwards.** The visuals corrected one
  over-generalisation, resolved one word the record had refused to guess, eliminated one
  of two competing readings, and left `I7` open. Keeping the two passes separate is what
  makes that visible.
- **GBP/USD appears on screen at `[00:50:55]` and is never spoken aloud** — the project's
  designated primary research instrument, with the weekly cycle annotated.
- V01 still yields **no executable rule**: no stop, target, risk-to-reward, position size
  or indicator parameter. Better evidence did not make it a mechanics lesson.
- The review is **not** in this release. `18_REVIEW/V01/V01_REVIEW_R1.md` must be written
  by a separate session; the student cannot audit itself.

---

## [0.2.0] — 2026-08-10 — Phase 1 opens: source ingested, V01 studied

First release containing actual Market Maker Method content.

### Added

- **Source ingestion complete.** `00_SYSTEM/SOURCE_MANIFEST.md` populated with 42
  SWF files — 21 lesson videos (`V01`–`V21`, 21:52:38 total, all ordering `CERTAIN`)
  and 21 out-of-scope videos from two other series (`X01`–`X21`) — each with SHA-256,
  measured duration, and byte size. Plus four image collections (`X22`–`X26`).
- **`00_SYSTEM/QUARANTINE_REGISTER.md`** — new tracked file recording material that
  must never be used as evidence, with the evidence for that judgement.
- **V01 artifacts:** `02_TRANSCRIPTS/V01/V01_TRANSCRIPT.md`,
  `03_LESSON_NOTES/V01_SOURCE_NOTES.md`, `03_LESSON_NOTES/V01_INTERPRETATION.md`,
  `04_SCREENSHOTS/V01/INDEX.md`.
- **First course-level ambiguity and contradiction records:** `A-001`–`A-017` (all
  `DO NOT CODE`), `C-001` (foundational, unresolved), `C-002`.
- **`D-017`** — source arrangement, lesson order, duplicate handling, quarantine.
- **`I-008`** — 20 of 21 transcripts are unverified.

### Changed

- `COURSE_PROGRESS.md` expanded from zero rows to 21 verified lesson rows.
- Lesson folders under `Bootcamp Notes/` renumbered from alphabetical to
  chronological order (19 of 21 folders changed). Any external reference to the old
  numbering is now wrong. Source `.swf` files were not renamed.
- `I-006` (screenshot capture) updated with an investigated root cause: these SWFs
  contain no video stream, only a composited bitmap display list, so frame extraction
  requires a Flash renderer rather than `ffmpeg`.

### Removed

- 63 fabricated per-lesson notes files, an 8-file synthesized master rulebook, and a
  synthesized course-notes document — moved to a clearly-marked quarantine folder
  under the Git-ignored source tree, not deleted. See `QUARANTINE_REGISTER.md` Q-001.
- Stray housekeeping files from `01_SOURCE_VIDEOS/`: a 61 MB test-conversion `.mp4`,
  a 392-file temporary jpeg folder, 14 `.DS_Store` files.

### Notes

- **Week 6 is genuinely missing** from the source material and is documented as
  expected-missing. No session may fabricate or interpolate it.
- V01 was studied **without screenshots**. Roughly its last 21 minutes is narration
  over slides that could not be extracted, so about half the lesson's content was not
  recovered. No V01 interpretation is classified `VISUAL`. Every affected artifact
  states this.
- V01 yields no executable rule: no stop, no target, no risk-to-reward, no position
  size, and no indicator parameter is stated anywhere in the lesson.

---

## [0.1.1] — 2026-08-10 — Checkpoint commit cadence; audit fixes

### Changed

- Adopted D-015: commit and push at checkpoints during a session (roughly every
  5–10 artifacts, or at any natural boundary), rather than accumulating a whole
  session into one end-of-session commit. Propagated to `SESSION_CLOSE.md`,
  `README.md` §13, and both session prompts.

### Fixed (from infrastructure self-audit)

- Appended the missing `LOG.md` entry for the D-015 session — the change had been
  committed without a log entry, which the audit flagged as a session-close
  protocol violation.
- Added a clarifying comment to the `*.ts` pattern in `.gitignore` (MPEG transport
  stream, not TypeScript).

### Audit notes

- Verified all 38 required setup files present and non-empty; all D/I
  cross-references resolve; `COURSE_PROGRESS.md` columns match specification;
  README section references correct.
- Negative-tested `scripts/validate_project.py` — it fails correctly when a
  required file is removed, so its green result is not vacuous.
- Re-confirmed zero Market Maker Method content anywhere in the repository.

---

## [0.1.0] — 2026-08-10 — Phase 0: Infrastructure

### Added

- Governing files established as the project source of truth:
  - `MMM_MASTER_STUDENT_RESEARCH_AGENT.md`
  - `MMM_INDEPENDENT_REVIEWER_TEACHER_AGENT.md`
- Full directory structure `00_SYSTEM/` through `18_REVIEW/`, plus `scripts/`,
  created at the repository root.
- Root documents: `README.md`, `LOG.md`, `CHANGELOG.md`, `.gitignore`.
- `00_SYSTEM/` operating documents:
  - `AGENT_ROLE.md` — student and reviewer roles and boundaries
  - `STUDY_PROTOCOL.md` — per-lesson workflow and full phase roadmap
  - `MASTERY_STANDARD.md` — student self-assessment standard (A–J)
  - `REVIEW_PROTOCOL.md` — durable independent review methodology
  - `REMEDIATION_PROTOCOL.md` — PASS / REVISE / BLOCKED loop
  - `SOURCE_INGESTION_PROTOCOL.md` — video inventory and checksum procedure
  - `FILE_NAMING_STANDARD.md` — naming conventions and ID schemes
  - `COURSE_PROGRESS.md` — per-lesson progress table (no lessons yet)
  - `DECISIONS.md` — D-001 … D-014
  - `SOURCE_MANIFEST.md` — empty; zero videos ingested
  - `SESSION_START.md`, `SESSION_CLOSE.md` — session checklists
  - `SETUP_ISSUES.md` — I-001 … I-004, governing-file inconsistencies
  - `STUDENT_SESSION_PROMPT.md`, `REVIEWER_SESSION_PROMPT.md`
- Eleven reusable templates in `00_SYSTEM/TEMPLATES/`.
- Review infrastructure: `18_REVIEW/REVIEW_INDEX.md` and empty cumulative review
  templates (`CUMULATIVE_25/50/75`, `FINAL_COURSE_REVIEW`).
- Empty, clearly-labelled logs: `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`,
  `11_CONTRADICTIONS/CONTRADICTIONS.md`, `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`.
- `scripts/validate_project.py` — structural health check (no methodology
  judgement).
- A `README.md` contract in each numbered directory.

### Notes

- **No Market Maker Method content exists in this release.** No transcripts, notes,
  rules, concepts, screenshots, homework, backtests, or specifications were
  produced. The bootcamp source videos were not accessible to the session that
  built this infrastructure.
- Project status: `INFRASTRUCTURE READY / SOURCE VIDEOS NOT YET AVAILABLE`.
- Structure was built at the repository root rather than inside a nested
  `MMM-MASTERY/` directory, to avoid duplicate project nesting (see D-012).

---
