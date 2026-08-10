# COURSE PROGRESS

Single source of truth for where the course stands.

Updated after every meaningful milestone by both Student and Reviewer sessions.

---

## SUMMARY

```text
PHASE:               1 — STUDENT  (unblocked; ingestion complete)
VIDEOS INGESTED:     21
VIDEOS IN PROGRESS:  0
VIDEOS PASSED:       2  (V01, V02)
CURRENT LESSON:      V02 — re-reviewed R3 2026-08-10: **PASS** (HIGH), 0 critical,
                     0 major, 2 minor (both non-blocking). **COMPLETE.**
                     Both of R2's required corrections applied and independently
                     re-derived at R3 — the chart re-measured from the committed PNG
                     with a fresh pipeline (177 bars, 52.277 px/0.00100, max residual
                     0.086 pip, validated against the header's printed last-bar OHLC
                     to 0.48 pip) and the transcript re-counted by regex. Every
                     corrected value reproduces. See 18_REVIEW/V02/V02_REVIEW_R3.md.
                     (R2 2026-08-10: REVISE (HIGH), 0 critical, 0 major, 3 minor,
                     plus 1 MAJOR process finding — the D-004 gate breach, since
                     confirmed by the project owner as an intentional override.
                     R1 2026-08-10: REVISE (HIGH), 0 critical, 1 major, 5 minor —
                     all ten required corrections applied and verified at R2.)
                     V01 — re-reviewed R3 2026-08-10: **PASS** (HIGH), 0 critical,
                     0 major. COMPLETE. All 15 of R2's required actions applied and
                     verified against the source; R2 finding N1 (A-006's trailing
                     block) closed by withdrawing it in place.
NEXT ACTION:         **Begin V03.** The V03 gate is OPEN as of V02 R3 PASS.
                     Four non-blocking carry-forward items from R3 (§9), none of
                     which opens a remediation round:
                     (a) V02_TRANSCRIPT.md — restate the `level count` clause; the
                     literal string occurs ZERO times, the referent once at
                     [00:33:11] ("you can't count the levels"). R3 gives the wording.
                     (b) V02_HOMEWORK.md §1.1/§1.4 + V02_MASTERY_REPORT.md + this
                     file — restate the continuity figure: 175 of 176 boundaries
                     within 1 pip, the only MATERIAL discontinuity is the -12.6 pip
                     weekend gap at x=273, and three sub-pip gaps (<=0.8 pip, at
                     x=285, 447, 933) also exist. The "174 of 176" figure does not
                     reproduce. **Charged against R2, not the student** — the
                     remediation was required to state R2's number and did so
                     accurately.
                     (c) ✅ DONE 2026-08-10. DECISIONS.md **D-023** records the
                     owner's V03 parallel-work override as a numbered decision; the
                     V03 GATE block below and REVIEW_INDEX.md open item 17 are
                     reconciled to it. Open item 9 stays OPEN on its mechanism
                     ground — a written gate with no enforcement failed twice in one
                     day, and the validate_project.py pre-flight guard is still the
                     fix. Recorded alongside it: **D-024**, the standing policy for
                     how finding severity governs the gate (see PROGRESSION RULE).
                     (d) REVIEW_INDEX.md — close open item 12 (discharged by R2
                     correction 1); item 13 stays open; item 14 now carries six
                     instances and becomes a work item at the 25% review.
                     ---- V02 R2 remediation history, retained ----
                     (1) ✅ DONE 2026-08-10. V02_HOMEWORK.md §1.1 — the Sun 2 Aug /
                     Fri 31 Jul day boundary is corrected (Sun 2 Aug = 2 bars, open
                     0.80552, high 0.80737 23:00; Fri 31 Jul open 0.80578, low
                     0.80538, close 0.80678), the superseded rows and the superseded
                     boundary reasoning are retained in place per
                     REMEDIATION_PROTOCOL.md §2, the day boundaries now come from the
                     chart's own dotted separators (x = 147, 273, 429, 573, 717, 861,
                     987, 1149), and the false "self-validating on all six boundaries"
                     claim is restated as what it actually establishes (174 of 176
                     BAR boundaries; cannot adjudicate the weekend gap, measured at
                     -12.6 pip at x=273). The overstated "reusable pipeline" claim is
                     corrected in the two files that carried it (V02_HOMEWORK.md §1.3
                     and CONTRADICTIONS.md C-001), plus the same false self-validation
                     claim in V02_MASTERY_REPORT.md and in this file. §1.2 and §1.3's
                     C-001 result were NOT touched — both verified correct at R2.
                     (2) ✅ DONE 2026-08-10 (commit d030a14) — the PFH/PFL count in
                     V02_SOURCE_NOTES.md §3 and V02_TRANSCRIPT.md. Both
                     abbreviations occur ZERO times; spelled out, "peak formation
                     high" x1 and "peak formation low" x2 (4 total). Independently
                     re-counted and confirmed at R3. I-008's transcript adoption is
                     unaffected and strengthened.
                     (3) ✅ Discharged by the reviewer sessions (R2 and R3), which
                     had to rewrite these lines to record their decisions.
                     → ✅ R3 written 2026-08-10 by a fresh session (D-003):
                     18_REVIEW/V02/V02_REVIEW_R3.md — **PASS**.
                     ---- R1 history, retained ----
                     ✅ DONE 2026-08-10 — all ten of V02 R1's required corrections are
                     applied (see V02_MASTERY_REPORT.md "Revision R1"). Homework 11a
                     was REDONE from pixel measurement of the committed chart, with
                     the invalid first pass preserved in place per
                     REMEDIATION_PROTOCOL.md §2. The "at least 3 days" confirmation is
                     WITHDRAWN; the corrected week is recorded against C-001 as
                     explicitly NON-RESOLVING and commits no day-count value.
                     → **AWAITING R2.** A FRESH reviewer session must write
                     18_REVIEW/V02/V02_REVIEW_R2.md. Per D-003 the session that
                     applied these fixes must NOT review them, and per the R1 closing
                     note R2 must re-measure the chart independently rather than
                     accept the new pipeline's self-description.
BLOCKED ON:          nothing. I-006 RESOLVED. I-007 open — blocks V01 H4/H5, which
                     R1 reclassified from NOT APPLICABLE to DEFERRED (D-019), and it
                     travels forward as an open research item rather than blocking
                     advancement.
V02 GATE:            OPEN as of V01 R3 PASS (D-004 satisfied).
                     NOTE: the V02 student pass was performed while this gate still
                     read CLOSED. V01's PASS makes it moot and no V02 work is
                     discarded, but the gate did not hold — see REVIEW_INDEX.md open
                     item 9.
V03 GATE:            **OPEN as of V02 R3 PASS, 2026-08-10 (D-004 satisfied).**
                     The V03 work performed in parallel while this gate read CLOSED
                     was an **owner-authorized override**, confirmed by the project
                     owner as intentional and not an error to correct. It is NOT to
                     be reverted, re-done or discarded. ✅ **Now recorded as a
                     decision — DECISIONS.md D-023, 2026-08-10.** The breach history
                     retained below is SUPERSEDED by that entry and must be read
                     through it: it is the record of how the override came to be
                     authorized, not a live instruction. R3 Note 3 is discharged;
                     REVIEW_INDEX.md open item 17 is CLOSED.
                     The override is one instance (V02 → V03) and is NOT precedent.
                     Separately, the standing rule for how review findings affect
                     this gate is now **D-024** — minors-only opens it, any
                     CRITICAL or MAJOR keeps it closed. See PROGRESSION RULE below.
                     **The mechanism finding survives the override:** a written
                     gate with no enforcement failed twice in one day. Open item 9
                     stays open on that ground alone, and the concrete fix is
                     unchanged — a validate_project.py pre-flight guard that
                     refuses VNN artifact creation while VNN GATE reads CLOSED.
                     ---- history, retained ----
                     CLOSED. D-004 requires reviewer PASS on V02 before V03 opens.
                     ⚠ **BREACHED — LIVE, as of V02 R2 (2026-08-10).** The gate held
                     at R2's start and did not hold at its end: an in-progress V03
                     student pass appeared in the working tree from another session
                     — 02_TRANSCRIPTS/V03/V03_TRANSCRIPT.md (1,230 entries, marked
                     COMPLETE), 04_SCREENSHOTS/V03/ and 05_HOMEWORK/V03/ created,
                     and QUARANTINE_REGISTER.md Q-003 appended, whose own text says
                     it precedes "writing V03's notes". **Second occurrence of this
                     violation** (see REVIEW_INDEX.md open item 9) and, unlike the
                     first, NOT moot: V02 is REVISE with three corrections
                     outstanding, one of them in the measurement pipeline V03's
                     chart work would inherit.
                     REQUIRED: stop the V03 pass until V02 receives reviewer PASS.
                     Do NOT delete the V03 work — hold it uncommitted, or commit it
                     explicitly labelled as produced in violation of D-004 — and
                     re-audit it against a passed V02. R2 left it untouched and
                     unstaged and drew no finding from it.
                     See 18_REVIEW/V02/V02_REVIEW_R2.md §7.
                     V02 is REVISE, not PASS, so this gate is live and must hold.
                     Open item 9 records that the last gate did not; this is the test.
                     No V03 work of any kind until V02 R2 returns PASS.
```

---

## COURSE LENGTH — VERIFIED 2026-08-10

**21 lesson videos**, total runtime **21:52:38**, all ordering `CERTAIN`. Every row
below corresponds to a file that was hashed and probed during ingestion; see
`00_SYSTEM/SOURCE_MANIFEST.md`.

The owner's pre-ingestion expectation of "approximately 21" turned out to be exact.
That is a coincidence worth naming rather than treating as confirmation — the count
was established from the files, not from the expectation.

**Week 6 is genuinely absent** from the source material (session dates run 03/18,
03/25, 03/26, 04/01, 04/08, 04/15, then jump to 05/06). Confirmed by the project
owner as expected-missing, not a copy error. It gets no row. **No session may
fabricate, interpolate, or infer Week 6 content.**

---

## PROGRESS TABLE

| Video | Session | Duration | Source Verified | Transcript | Notes | Screenshots | Homework | Manual Backtest | Student Mastery | Reviewer | Final Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V01 | Wk1 P1 | 00:54:43 | ✅ | ✅ | ✅ | ✅ | ⏸ | — | REVIEW REQUIRED (resub) | ✅ R1 REVISE → R2 REVISE → **R3 PASS** | **COMPLETE** |
| V02 | Wk1 P2 | 01:00:19 | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⏸ | REVIEW REQUIRED (resub ×2) | ✅ R1 REVISE → R2 REVISE → **R3 PASS** | **COMPLETE** |
| V03 | Wk2 03/25 P1 | 01:10:42 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V04 | Wk2 03/25 P2 | 01:25:41 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V05 | Wk2 03/25 P3 | 01:08:21 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V06 | Wk2 03/26 P1 | 01:14:33 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V07 | Wk2 03/26 P2 | 00:48:06 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V08 | Wk2 03/26 P3 | 00:43:03 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V09 | Wk2 03/26 P4 | 00:52:26 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V10 | Wk3 | 01:36:16 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V11 | Wk4 P1 | 00:50:56 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V12 | Wk4 P2 | 00:55:18 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V13 | Wk5 P1 | 01:05:22 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V14 | Wk5 P2 | 00:47:48 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V15 | Wk7 P1 | 00:52:05 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V16 | Wk7 P2 | 00:44:35 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V17 | Wk8 P1 | 00:57:09 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V18 | Wk8 P2 | 00:46:08 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V19 | Wk9 P1 | 01:07:21 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V20 | Wk9 P2 | 00:45:49 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |
| V21 | Wk10 | 01:14:47 | ✅ | ⚠️ | ⬜ | ⬜ | ⬜ | ⬜ | — | — | NOT STARTED |

### Notes on the marks above

- **V02 Transcript ✅** — verified 2026-08-10 against its own audio (four Whisper
  spot-checks plus structural checks) and adopted at `02_TRANSCRIPTS/V02/V02_TRANSCRIPT.md`.
  I-008 satisfied for V02. Its three companion files were confirmed fabricated (Q-002).
- **V02 Screenshots ✅** — 25 captured 2026-08-10 by the **10× fast sweep** (D-021), not
  by real-time recording: a 60-minute lesson swept in 6 minutes. An earlier capture this
  session was of the wrong lesson entirely and was discarded — see `SETUP_ISSUES.md` I-009.
- **V02 Homework ⚠️** — 11a (label the weekly cycle) attempted on real TradingView data
  for a substituted week, first pass preserved, ungraded — 2012 hourly data is
  account-gated. 11b (40 flashcards) `DEFERRED` on **A-011/A-007**, not on tooling.
  `05_HOMEWORK/V02/V02_HOMEWORK.md`.
  **Review R1 outcome:** the *substitution* is upheld as honestly handled and correctly
  evidenced, and 11b's `DEFERRED` is upheld after independent verification that M/W
  anatomy is undefined across both V01 and V02. The *markup* is the round's MAJOR — it
  contradicts the chart it cites and must be redone. See
  `18_REVIEW/V02/V02_REVIEW_R1.md`.
  **R1 remediation ✅ 2026-08-10:** the markup was **redone from pixel measurement** of
  the committed PNG (method: `V02_HOMEWORK.md` §1.1; ±0.5 pip; ~~self-validating on day
  boundaries~~ — **corrected 2026-08-10 per R2 Minor 1: day boundaries come from the
  chart's own dotted separators, and open = prior close is a within-session check that
  cannot adjudicate the Fri→Sun weekend boundary**), with the invalid first pass preserved in place per
  `REMEDIATION_PROTOCOL.md` §2. The "at least 3 days" confirmation is **withdrawn**; the
  corrected week is recorded against `C-001` as **non-resolving** and commits no
  day-count value. Labels remain unverified — no answer key exists — so dimension B
  stays **FAIL**. Awaiting R2.
- **V02 Manual Backtest ⏸** — `DEFERRED` under D-019, not `NOT APPLICABLE`. V02 states a
  falsifiable structural claim ("does not cross the level for at least 3 days") but
  A-004 leaves "the level" without a price, and the lesson states no entry, so there is
  no decision point to hide.

- **V01 Screenshots ✅** — 22 captured 2026-08-10 and indexed. I-006 is `RESOLVED`;
  method in `00_SYSTEM/SWF_CAPTURE_RECIPE.md`. A full-length synced mp4 is retained
  outside the repo, so any further timestamp can be extracted on demand.
- **V01 Manual Backtest —** `NOT APPLICABLE` under **D-018**. **Audited and upheld**
  by R1: the lesson states no entry, stop, target or position size, so there is no rule
  whose application could be graded.
- **V01 Homework ⏸** — R1 **partially overturned** the D-018 claim. H1–H3 and H6–H8
  remain `NOT APPLICABLE` (a 2012 emailed survey, a broker agreement, a demo account, an
  MT4 template). **H4 and H5 are `DEFERRED`, blocked by `I-007`** — they are
  observational chart exercises needing a data source, not a rule definition, so they
  stay on the books rather than being closed. See `18_REVIEW/V01/V01_REVIEW_R1.md`
  finding 2.
- **V02–V21 Transcript ⚠️** — a `TRANSCRIPT.md` exists for each, but it came from the
  same pre-ingestion process that produced the quarantined fabrications, and **none
  has been verified**. Not a tick. See `SETUP_ISSUES.md` I-008.
- **V01 Notes ✅** — `V01_SOURCE_NOTES.md` and `V01_INTERPRETATION.md` are written
  from the transcript only. Nothing was carried over from the quarantined files.
- **V01 Homework ⬜, Manual Backtest ⬜** — deliberately not started. This session's
  scope stopped at interpretation.

---

## LEGEND

### Artifact columns

| Symbol | Meaning |
|---|---|
| ⬜ | Not started |
| ⏳ | In progress |
| ✅ | Complete |
| — | Not applicable to this lesson (e.g. no homework assigned) |
| ⚠️ | Complete but flagged by review — see the review file |

`Source Verified` means the file is inventoried in `SOURCE_MANIFEST.md` with a
SHA-256 and a non-`UNCERTAIN` ordering confidence.

### Student Mastery column

Values from `MASTERY_STANDARD.md` — a **self-assessment**, not an authorization:

```text
PASS | REVIEW REQUIRED | BLOCKED | —
```

### Reviewer column

Values from `REVIEW_PROTOCOL.md` — the **only** column that authorizes
advancement. Include the review round:

```text
PASS (R1) | REVISE (R1) | BLOCKED (R1) | —
```

### Final Status column

```text
NOT STARTED     ← no work begun
IN PROGRESS     ← student is working the lesson
AWAITING REVIEW ← student complete, reviewer session not yet run
IN REMEDIATION  ← reviewer returned REVISE or BLOCKED
COMPLETE        ← reviewer PASS; advancement authorized
```

**A lesson is `COMPLETE` only on reviewer `PASS`.** A student mastery `PASS` moves
the row to `AWAITING REVIEW`, never to `COMPLETE`.

---

## PROGRESSION RULE

```text
Lesson N+1 may be opened when lesson N's latest review carries
        0 CRITICAL and 0 MAJOR findings.
Lesson N itself becomes COMPLETE only on reviewer PASS.
```

**The gate follows the finding severity, not the verdict word — see `DECISIONS.md`
D-024.** D-004 still holds: only the reviewer opens the gate, and only a reviewer `PASS`
moves a row to `COMPLETE`.

| Lesson N's latest review | Gate for N+1 | Row status for N |
|---|---|---|
| `PASS` | **OPEN** | `COMPLETE` |
| `REVISE`, 0 `CRITICAL` + 0 `MAJOR` (minors only) | **OPEN** — start N+1 now; the minors need not be applied first | `IN REMEDIATION` |
| `REVISE` with any `CRITICAL` or `MAJOR` | **CLOSED** until fixed **and re-reviewed** | `IN REMEDIATION` |
| `BLOCKED` | **CLOSED**, unconditionally | `IN REMEDIATION` |

Outstanding minors from a gate-opening `REVISE` are **deferred, never dropped**: each is
carried in `18_REVIEW/REVIEW_INDEX.md` as an open item and named in `NEXT ACTION` above,
and all must be applied and verified before lesson N reaches `COMPLETE`. An open gate buys
parallelism, not amnesty.

Working ahead past a `CRITICAL` or `MAJOR` corrupts the dependency chain the mastery gate
exists to protect — V02 R1's `MAJOR` sat in the pixel-measurement pipeline V03's chart
work would have inherited, which is the concrete case. A `MINOR` is defined by
`REVIEW_PROTOCOL.md` §8 as not altering the method, so it cannot carry that hazard.

A session may **not** downgrade a `MAJOR` to a `MINOR` to open a gate. Dispute a severity
in the next review round, like any other finding.

The one authorized exception on record is `DECISIONS.md` D-023 (owner-authorized parallel
V03 pass). It is not precedent.

---

## CUMULATIVE REVIEW CHECKPOINTS

Triggered at roughly 25% / 50% / 75% / 100% of verified lessons. Exact trigger
points are set once the real lesson count is known at ingestion.

| Checkpoint | Trigger (lessons passed) | File | Status |
|---|---|---|---|
| 25% | TBD at ingestion | `18_REVIEW/CUMULATIVE_25.md` | Not started |
| 50% | TBD at ingestion | `18_REVIEW/CUMULATIVE_50.md` | Not started |
| 75% | TBD at ingestion | `18_REVIEW/CUMULATIVE_75.md` | Not started |
| 100% | All lessons passed | `18_REVIEW/FINAL_COURSE_REVIEW.md` | Not started |

---

## PHASE STATUS

| Phase | Name | Status |
|---|---|---|
| 0 | Environment | ✅ Complete |
| 1 | Student | 🔄 In progress — V01 **PASS** (R3); V02 **PASS** (R3, 0 critical, 0 major, 2 minor non-blocking); V03 gate open, V03 next |
| 2 | Scholar | Not started |
| 3 | Expert (Master Spec) | Not started |
| 4 | Formalizer (Machine Spec) | Not started |
| 5 | Observer (Pine indicators) | Not started |
| 6 | Evaluator | Not started |
| 7 | Strategist | Not started |
| 8 | Automated Backtester | Not started |
| 9 | Researcher | Not started |
| 10 | Forward Tester | Not started |
| 11 | Risk Engine | Not started |
| 12 | Execution Robot | Not started |

> **CORRECTED 2026-08-10 (V02 review R1, finding 5, `E20`).** The Phase 1 row read
> `⛔ Blocked — no source videos`. That was true at project start and became false when
> ingestion completed; it contradicted this file's own SUMMARY block
> (`PHASE: 1 — STUDENT (unblocked; ingestion complete)`) and the 21 ingested videos
> recorded below. Same staleness class as the `CONTRADICTIONS.md` STATUS defect
> (finding 4): a hand-maintained table duplicating state that lives elsewhere in the same
> file. **The SUMMARY block at the top of this file is the authority for phase state;
> this table is a view of it and must be reconciled against it, not edited independently.**

Full phase definitions: `STUDY_PROTOCOL.md` §4.
