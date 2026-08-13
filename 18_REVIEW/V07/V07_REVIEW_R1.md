# V07 — INDEPENDENT REVIEW R1

| Field | Value |
|---|---|
| Lesson | V07 — *"Best Trade Grabs"* (`Bootcamp1 Wk2 032612 Part2 (48mins).swf`, 00:48:06) |
| Review round | R1 |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent |
| Student submission | `STUDENT STATUS: REVIEW REQUIRED`, `07_MASTERY_REPORTS/V07_MASTERY_REPORT.md` |
| `D-003` separation of duties | **SATISFIED.** This session authored **no** V07 artifact. It read the source first (`REVIEW_PROTOCOL.md` §3), re-derived every load-bearing count mechanically, re-read the frames that carry claims, and re-ran every script from the committed tree |
| Process disclosure | No owner directive was issued for this round. **Dimension B is therefore scored under the standard protocol**, not carved out as V06's was — see §14 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V07
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      3   (M1, M2 — E20 count class; M3 — E01+E11)
NOTE:       4   (N1 git, N2 stale count, N3 probe integrity, N4 dimension B)

DIMENSION B: NOT SATISFIED — blocked by D-030, structural and NOT
             attributable to the student. Scored, not carved out.
             Carries NO severity charge (see §14). Owner ruling owed
             on REVIEW_INDEX.md open item 36 — third lesson running.

DIMENSION F: the demo-account NOT APPLICABLE is UPHELD (see §11).

GIT CONCERN: REAL EVENT, ZERO DAMAGE. No lost commits, no corrupted
             file, no broken audit trail. Verified independently — §2.

ADVANCEMENT: AUTHORIZED under D-024 (0 CRITICAL, 0 MAJOR).
             V08 gate OPENS. The three MINORs are carried as owed
             and must be applied before V07 reaches COMPLETE.
```

---

## 0. WHAT THIS REVIEWER VERIFIED INDEPENDENTLY, BEFORE ANY DIMENSION WAS GRADED

Nothing below is taken from the student's own attestation. Each item was re-derived.

| # | Check | Method | Result |
|---|---|---|---|
| 1 | Transcript structure | Regex over the verbatim body | **539 markers, 539 distinct, strictly increasing, zero same-second pairs, final `[00:48:05]`** — the COVERAGE block reproduces exactly |
| 2 | The gap enumeration | Full gap census | **Exact.** The block names gaps by their **end** marker and every one checks out: 19 s ending `[00:35:27]` *and* `[00:35:46]` (there are two); 18 s ending `[00:06:16]`, `[00:37:07]`, `[00:46:24]`; 17 s at `[00:47:37]`; 16 s at `[00:37:34]`, `[00:45:18]` |
| 3 | Word count | Token count over the body | **7,436** — as claimed |
| 4 | Speaker evidence | Token counts + context read | `Steve` **2**, `Jim` **3** — both `Steve` hits are the speaker's own third-person references, and `[00:35:46]` queues Steve as the **next questioner**. Confirmed |
| 5 | Every marker citation | Mechanical sweep, 7 artifacts | **300 distinct citations; every unresolved one is accounted for** — `[00:21:35]` / `[00:34:50]` are declared screenshot timestamps, `[00:30:22]` / `[00:38:19]` are labelled **V04** markers |
| 6 | Every quoted string | Normalised substring match against the body | **239 marker-cited quotes checked. One defect (M3).** All other apparent misses are printed slide text or the declared Whisper re-transcription, correctly labelled as such |
| 7 | §10's "measured negatives" | Re-counted every cell | `Asian` 1, `London` 2, `New York` 1, `EST` 0, `5/13` 0, `M15` 0, `PFH`/`PFL`/`HOD`/`LOD` 0, `mustard`/`mayo`/`raspberry` 0, `1:3` 0, `GBP` 0, `stop loss` 1, all six clock times 0 — **all correct except two (M1, M2)** |
| 8 | Screenshot claims | Re-read 4 load-bearing frames at full resolution | **All exact** — see §5 |
| 9 | `PT-033` pre-registration ordering | `git log --reverse` per file | **Pre-registration `81f9ae4` 08:22:38 → runner + results + report `a5ae7dc` 08:29:13.** Strict, and the runner did not exist in Git before the pre-registration |
| 10 | Backtest reproduction | Re-ran `run_pt033.py` from the committed tree | **Bit-exact.** Every figure in §§2–5 reproduces; `pt033_results.json` is byte-identical to the committed file; verdict `INDETERMINATE` reproduces |
| 11 | Sensitivity reproduction | Re-ran `sensitivity_pt033.py` | **Exact** — 118 stub days, 15.0 p median, `B · D-SESSION` 0.8462 → 0.9546 |
| 12 | Homework reproduction | Re-ran all three homework scripts | **Bit-exact**, including the 16-cell shape census and the M1-vs-M15 cross-check |
| 13 | Comprehension probe | Re-ran `comprehension_probe.py` | **75 probes, 1 failure — `R11`, still failing in committed code.** As reported |
| 14 | Git integrity | `git fsck`, per-file history, fetch | **Zero unreachable commits. No lost work.** §2 |
| 15 | Structural validator | `python3 scripts/validate_project.py` | **103 passed, 0 warnings, 0 failures** |

**Working-tree note.** A concurrent session is actively committing in this checkout (`PT-003`/`PT-004`/`PT-005` runners and V02 observations appeared *between* two `git status` calls during this review). Its files were read for context and **not touched, staged, or reverted** by this session.

---

## 1. FINDINGS

### M1 — `MINOR` (`E20`, count class — open items 15 / 39 / 48 / 58 / 59 lineage) — `V07_SOURCE_NOTES.md` §10 states the *level* count as 26; it is 56, and §5 of the same file says so

`V07_SOURCE_NOTES.md` §10's table row reads:

> | A definition of *level* | — | **26 uses**, no definition. `A-004` untouched |

**Re-measured over the verbatim body:** `level` 53 + `levels` 3 = **56**. The `level <N>` compound form is **35**. Entries containing the token are **44**. **26 matches none of them.**

The file **contradicts itself**: §5 opens with *"the bare token `level` / `levels` **56 times**"* — which is correct — and §10 then says 26. This is the V05 `M4` intra-corpus-disagreement class layered on the count class: the corpus holds one right record and one wrong record for the same object, fourteen sections apart.

**Materiality is low and was checked.** The conclusion the row exists to support — *level is used constantly and never defined, `A-004` untouched* — is **unaffected and, if anything, understated**. No other artifact cites 26.

**Charged because §10 explicitly invites this check.** Its own preamble says the counts are *"stated as measured negatives so a later session does not go looking, and so a reviewer can falsify them cheaply."* A reviewer took the invitation and the cell falsified.

**Fix:** correct §10's cell to **56** (or state which sub-count 26 was meant to be), retaining the superseded text per `REMEDIATION_PROTOCOL.md` §2.

### M2 — `MINOR` (`E20`, same count class) — §10's *"the peak"* row says 4×, lists 5 markers, and the true count is 5

Same table:

> | Peak formation | `peak formation` **0**, `PFH` **0**, `PFL` **0** | *"the peak"* is used **4×** as a location (`[00:00:26]`, `[00:03:18]`, `[00:03:20]`, `[00:14:02]`, `[00:16:44]`) and never defined |

**Re-measured: 5 occurrences, at exactly the five markers the row itself lists.** The marker list is right; the number is wrong, and the row is internally inconsistent on its own face.

The `peak formation` / `PFH` / `PFL` zero counts are **correct** and the row's conclusion is unaffected.

**Fix:** `4×` → **5×**, superseded text retained.

### M3 — `MINOR` (`E01` misquote, co-code `E11` wrong marker) — `V07_MASTERY_REPORT.md` §D alters a word inside quotation marks and cites the wrong marker, falsifying §H's own integrity claim

`V07_MASTERY_REPORT.md` §D, the Sequence table's **Invalidates** row:

> *"if it doesn't do what you expect **and** your flashcard isn't the same"* (`[00:28:28]`)

**The transcript reads, at `[00:28:31]`:**

> *"If it doesn't do what you expect **in** your flashcard isn't the same, you may just decide to pass on it."*

Two defects in one citation:

1. **`in` → `and` inside quotation marks.** The substitution is the *sensible* reading — the adopted ASR is garbled here — but it is a silent smoothing of a verbatim quote, which is the V04 `M2` / V05 `M3` class the project has charged twice before.
2. **`[00:28:28]` is the wrong marker.** It exists, and it carries a different sentence (*"We'll say whether it's something that you will take."*). The quoted words are at `[00:28:31]`. This is open item 7's class exactly — the neighbouring marker rather than the one the words fall under.

**Why this is charged rather than waved through.** `V07_MASTERY_REPORT.md` §H makes an explicit, unhedged self-certification:

> **"No quotation mark in any V07 artifact contains a word that is not in the source."**

**That sentence is false, by one word, and this is the instance that falsifies it.** The claim is otherwise extremely well earned — 239 marker-cited quotes were machine-checked by this reviewer and **this is the only defect in the set** — but a categorical claim that is 238/239 true must be either repaired or qualified, because a later session will rely on it rather than re-checking.

**Materiality to the method: none.** §D's grading does not turn on the word, and the source notes' rendering of the same passage (§6c) is **correct and unaltered**.

**Fix:** restore *"in your flashcard"* and re-cite to `[00:28:31]`; either repair §H's sentence or scope it (*"one smoothing found and corrected at R1"*). Superseded text retained.

### N1 — `NOTE` — the `I-009` git recurrence: a real event, independently verified as **zero damage**

Reported by the student as a concern. **Audited from git rather than from the report.** The event is real:

`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` was committed **once, ever**, inside **`8785c41`** — *"feat(data): D-036a — the CSV corpus is in, QA'd…"* — a commit about the HistData corpus that does not mention a transcript. The V07 ingestion session had it staged; the concurrent data session committed around it.

**Damage assessment — six independent checks, all clean:**

| Check | Result |
|---|---|
| Committed content complete? | **Yes.** 1,875 lines; 539 markers; strictly increasing; final `[00:48:05]` against measured audio 2886.95 s |
| Working tree == committed blob? | **Yes.** `git diff HEAD` empty |
| Any later fix-up, revert or partial re-commit? | **No.** Exactly one commit touches the file |
| Unreachable / orphaned commits? | **None.** `git fsck` reports dangling *trees and blobs* only — normal staging residue — and **zero dangling commits** |
| Authorship mangled? | **No.** Every commit in this repository is authored by the same human owner; git never recorded *which agent session* produced what, so no attribution that git ever held has been lost |
| Branch divergence? | **None.** In sync with `origin` after fetch |

**Verdict: the audit trail is intact.** What is wrong is *grouping and commit-message accuracy* — `git log` no longer tells you which session produced the transcript — and that is a documentation defect, not corruption. It is **disclosed in three places** (`c819cb5`'s message, `SETUP_ISSUES.md` I-009's table, the mastery report's escalation 2) and correctly **not** repaired by rewriting shared history while another session holds the tree.

**Credit where it is due, and it is the substantive part.** The session did not merely report the collision — it **diagnosed why I-009's existing mitigation was insufficient**: `git add <explicit paths>` writes into a *shared index* another session has already staged into, so staging discipline controls what you add and not what is already there. The corrected mitigation (`git status --porcelain` before staging; `git commit -m "msg" -- <paths>`, which bypasses the index for the named paths) is a genuine improvement to project method, and the argument-order trap is recorded too. **This reviewer used the corrected form for its own commit.**

**No finding is charged against the student for this.** The collision was caused by the other session's commit, the student's own staging was correct, and the disclosure exceeds what the protocol requires.

### N2 — `NOTE`, not charged — §H's "163 citations" is stale rather than wrong

`V07_MASTERY_REPORT.md` §H says a script extracted *"all 163 `[HH:MM:SS]` citations"* from the source notes. Current counts: **190 occurrences, 171 distinct** (182 / 168 excluding §11).

**Not charged as a count-class defect**, because the discrepancy is explained by the file growing after the sweep ran: §9b — the trap-family subsection — was added later, *after* `R11` failed, and it carries citations of its own. The number was true when measured. Recorded so a later reader does not mistake it for a live figure; refresh it whenever §H is next edited.

### N3 — `NOTE` — the `R11` failure is genuine, and it is the strongest integrity signal in the submission

Verified by re-running the committed probe: **75 items, 1 failure, and `R11` is still failing.** It predicted V07 does not use the compound *"trap move"*; the evidence line reads `"trap move" x1; trap-family x10`.

Three things were checked and all hold:

1. **The prediction was recorded as answer-not-known-in-advance** in the script's own docstring, before the answer existed.
2. **The failing probe was not reworded to pass.** It is in the committed tree, failing.
3. **The material it surfaced was written up rather than absorbed.** `V07_SOURCE_NOTES.md` §9b exists, carries an explicit provenance box naming the probe failure as its cause, states *"The probe FAILED. The prediction was wrong"*, and does not retract §§1–10.

The material is consequential — `[00:14:52]` attaches *"trap move"* to a **second leg**, and the subsection correctly extends `A-049` with a **negative datum** (both *trap move* and *stop hunt* occur in this lesson, neither is defined, they are never compared) rather than closing it. **This is a probe battery doing the job a probe battery exists to do, and the disclosure is complete rather than glossed.**

### N4 — `NOTE` — dimension B has now cost three lessons and still has no vocabulary

See §14. Raised here so it is visible in the findings list and not only in the dimension table.

---

## 2. THE 17 DIMENSIONS

### A. Source fidelity — **PASS**, with M1/M2/M3's caveats

Quotation accuracy is the best in the corpus to date: **239 marker-cited quotes machine-checked, one defect (M3)**. Qualifiers survive intact — the four candidate answers are preserved **as questions** (§3), `[00:04:38]`'s refusal to rank them is quoted, and the presenter's *"My personal opinion"* / *"I believe"* hedges are carried rather than flattened into rules. `[00:08:09]`'s *"I won't say all of the time"* is retained against the drawdown claim.

**No example is generalised into a universal rule.** The one place the temptation was strongest — the four-way second-leg taxonomy — is explicitly held open (`A-044` extended, not closed).

**Terminology is not altered.** ASR garble is preserved and separately reconstructed **outside** the quotation marks in every case checked: *"it's met"*, *"the 15 minute"*, *"mayo"*, and the 13/50/200 reading are each labelled as inferred or as the second ASR pass. M3 is the single exception and is charged.

### B. Completeness / Recognition — **NOT SATISFIED — BLOCKED BY `D-030`. Scored, not carved out. No severity charge.**

Full accounting in §14. In short: the objects V07 asks a student to recognise — *second leg* (`A-007`), *level* (`A-004`), *M/W* (`A-011`), *railroad tracks*, *tilted* (`A-058`), *A pattern* (`A-057`), *shark fin* (`A-032`), TDI (`A-039`) — are **named by the course and defined by none of it**. Recognition of an undefined object cannot be demonstrated, and demonstrating recognition of the *student's* definition would be the fabrication this project quarantined 72 files to avoid.

**Completeness in the ordinary sense is excellent** — concepts, sequence, confirmation, invalidation, exceptions, the assignment, the instructor's warnings and the operational meaning are all captured, and the lesson's *"do they tell the whole story?"* thesis is correctly identified as the spine.

### C. Provenance — **PASS**

Every rule in the interpreted-rules table carries a marker; **eight of ten also carry an explicit `D-030` blocker**, which is the discipline `REVIEW_PROTOCOL.md` §6C asks for and more. **Zero orphan rules.** The marker-existence sweep is clean across all seven artifacts, and the four non-resolving citations are declared in advance in the transcript header's own sweep block — the `E11` discipline from V05 R2 applied **before** submission.

**`V07_TRANSCRIPT.md`'s I-008 adoption argument was audited and it holds.** Length agrees three ways to within 0.05 s; the self-error criterion is genuine (five different ASR spellings of one student's name in one file); the not-the-template criterion is verified by this reviewer's own token counts (`5/13` 0, `M15` 0, `Shark Fin` 0, `mayo` 0, `PFH`/`PFL` 0, `EST` 0).

### D. Explicit vs inferred audit — **PASS**

`EXPLICIT` / `VISUAL` / `IMPLIED` / `INFERRED` / `UNRESOLVED` are used correctly throughout. The standard failure chain (three examples → pattern → universal rule → mandatory code) **does not occur**; it is actively resisted at `V07_INTERPRETATION.md` §2.3, which declines to merge V06's candle-name axis with V07's geometry axis precisely because doing so *"would manufacture a twelve-cell rule table neither speaker stated"* — the student naming `REVIEW_PROTOCOL.md` §17 failure mode 3 and then not committing it.

The homework's §2b repair proposal is correctly flagged `INFERRED` with *"The course does not say this. I do."*

### E. Chart recognition audit — **PASS (scope limited by `D-030`)**

No course-pattern classification is claimed, so there is nothing to mis-classify. What **is** classified — the seven flashcard days — is arithmetic (did a 50-pip run exist from the day's extreme), and it reproduces exactly. **No chart was used as a measurement source anywhere in V07**; the SVG cards are products of CSV numbers, which satisfies `E06` as restated by `D-036a`.

### F. Counterexample testing — **PASS, and it is this lesson's strongest dimension**

The lesson supplies unusually good discrimination material and the student captured all of it: the **deliberately-chosen losing chart shown first** (`[00:01:01]`–`[00:01:21]`, a correct-rule-application / losing-outcome case the presenter volunteers), the second non-payer at `[00:02:38]`, two traded geometries against two declined, the *reason* for declining (*"I haven't done enough homework on them"* — not invalidity), and a good-looking W passed for being at the wrong level.

**Applied, not just recorded.** The flashcard set carries one negative (2015-11-16, a 48.9-pip day where the target was arithmetically unreachable) and **four of six positives are half-failures, labelled as such rather than replaced with cleaner ones**. The positives are selected by an **even stride through the sorted qualifying days** — a stated anti-curation rule, verified in the script.

### G. Manual backtest review — **PASS**, audited against checks 1–20

| Check | Verdict |
|---|---|
| 1. GBP/USD primary | ✅ `D-007` |
| 2. Period reasonable | ✅ `W-C′` 2013-01-06 → 2016-06-30, 904–1,087 days per cell |
| 3–4. Sequential / future hidden | ⚠️ **Deliberately not applicable, and declared three times.** The rule arm *is* hindsight by design — see check 8 |
| 5. Rules known before result | ✅ Pre-registration `81f9ae4` **08:22:38** precedes runner and results `a5ae7dc` **08:29:13**; the runner did not exist in Git beforehand |
| 6–9. No result-dependent skipping; losers and borderlines retained; invalid separated | ✅ **No day excluded for its result.** The only drop is the pre-registered <4-bar rule, counted per cell (1, 0, 1, 0) and reproduced |
| 10–11. Consistent recording / R | ✅ |
| 12. Screenshots before and after | n/a — no chart was opened at any point |
| 13–14. Exact lesson rule identified; testing the lesson not an interpretation | ✅ **And this is the test's best feature.** `PT-033` §2 argues explicitly *why* this is the only V07 claim `D-030` lets through: HOD/LOD are arithmetic once a day boundary is fixed, so no undefined term is approximated. The most tempting target — the drawdown claim — is correctly refused |
| **15. Baseline present** | ✅ N1 matched random entry, 1,000 iterations, distribution reported per cell |
| **16. Baseline pre-registered** | ✅ In `PT-033` §4, with the seed `20260812`, committed before the runner existed |
| **17. Period pre-registered** | ✅ Instrument, window, timeframe, **both** timezone arms and **both** day definitions fixed in advance. Not changed mid-test |
| **18. Holdout intact** | ✅ **`E23` could not occur** — the holdout was never on disk; the vendor file was truncated on arrival and the untruncated copy deleted |
| **19. Sample sufficiency and interval** | ✅ n = 1,808–2,174 observations per cell; Wilson 95% CIs on every rate |
| **20. Negative results retained** | ✅ The headline verdict is **`INDETERMINATE`** and is reported as such; N1b's clean null is reported with equal prominence; the 100.0 percentile is reported *and* pre-emptively disqualified |

**Three features of this observation are better than the standard requires, and are recorded so `CUMULATIVE_25.md` can consider generalising them:**

1. **A pre-registered prohibition on the reviewer's most likely misreading.** `PT-033` §4 states, *before the numbers existed*, that the rule arm will beat N1 tautologically and that **no report may quote the percentile as support** — pre-committing against an `E24` the author could otherwise have committed honestly. The percentile came back 100.0 in every cell and the report holds the line.
2. **A disclosed sensitivity that does not replace the headline.** The 118 Arm-B Friday stub days were a genuine unanticipated interaction between a pre-registered drop rule and Arm B. The sensitivity is labelled post hoc, reported **alongside** the pre-registered numbers, `PT-033` was **not** edited, and the verdict is unchanged either way. Reproduced exactly by this reviewer.
3. **A `C8` addendum written against the result rather than around it.** A concurrent session found a 22-hour corpus hole *after* publication; §9a measures its effect per cell (≤ +0.0011), states the verdict is unchanged, and explicitly refuses to restate the headline figures to the excluding-`C8` column.

**The self-scoring of the pre-registered prediction (§3b) is accurate.** *"Part right and part wrong"* is the correct characterisation: the verdict call was **wrong**, the symmetry call **right**, the stated mechanism **right and load-bearing** — and the report identifies that `f50_day` tracks `frac(range ≥ 50)` to three decimals, i.e. that **`O2` collapses into `O1`**, which is a real finding against the author's own test design.

### H. Hindsight / lookahead audit — **PASS**

The rule arm is hindsight-contaminated **by construction**, and this is the correct disposition rather than a defect: the contamination is declared in `PT-033` §2a, §8, and `BT_V07_0001.md` §8, and the mandatory scope statement — carried verbatim into the observation — states that **no result may be read as evidence that Hi-Lo trading works or fails**. `REVIEW_PROTOCOL.md` §H is aimed at a test that pretends to be forward-executable; this one states in four places that it is not.

**Searched for the real thing and did not find it:** no setup boundary defined from future extremes in any *rule* claim, no classification requiring the later reversal, no entry justified after a target was hit, no aesthetically-selected sample (the stride rule), and no interpretation changed after an outcome was known — the one place an outcome *did* change a reading (`R11` → §9b) is disclosed with its provenance.

### I. Outcome vs rule application — **PASS**

`BT_V07_0001.md` §8 grades them separately and correctly: **application CORRECT** (mechanically so — every pre-registered element followed), **outcome NOT CONFIRMED**. The lesson's own correct-setup/losing-outcome case (`[00:01:06]`) is captured as exactly that. The homework's `SUCCESS AFTER CORRECTION` is the right label — the arithmetic was never wrong; the *reading* of a single year was.

### J. Sample quality — **PASS**

904–1,087 days and 1,808–2,174 observations per cell, four cells, two nulls at 1,000 iterations each, plus a second vendor. Far beyond what the lesson's complexity requires.

### K. Homework review — **PASS**

The assignment was correctly identified despite there being no slide headed "Homework" — the rename to *"R&D"* is printed (`V07_00-04-55`) and the operative sentence is `[00:12:09]`'s frequency count over a year.

**The preserved first attempt is real and it is instructive.** §2a records that 2015 alone returned 0.996, that the student read this as *"essentially every day"*, and that the reading was wrong — caught only because `PT-033`'s 0.9535 over a wider window disagreed. §2b then establishes that **the lesson's own instruction under-specifies its own answer by 12–14 percentage points** depending on which year a student picks. Reproduced exactly by this reviewer (2013 = 0.981, 2014 = 0.861, 2015 = 0.996).

**That is a finding about the assignment**, it is correctly flagged `INFERRED`, and it is the kind of result this project exists to produce.

**The §3 fence is properly constructed** — the shape census is explicitly *not* the course's M and W, the stand-in is fully stated, `n` and `tol` are **swept rather than chosen** (`D-010`), and the section states in bold that no number in it may be cited as a rule, hit rate or edge. The census reproduces exactly across all 16 cells.

**§5a is the strongest single check in the homework**: the count is recomputed from **raw M1**, bypassing an M15 aggregate a *different session* built, with exact agreement on day counts, hit counts and **the identity of every failing day**. §6a then correctly notes the limit of that check — *a cross-source check validates aggregation, not completeness* — which is why `C8` was needed.

### L. Teach-back — **PASS**

`V07_INTERPRETATION.md` §1 states the lesson in one sentence that is both accurate and non-trivial (*"a good trade is not the same thing as a big trade, and the difference is decided before the trade rather than after it"*), and the R&D → flashcard → patience loop is a fair reduction of the lesson's own structure. What comes before, what confirms, what invalidates, what is confused with what, the exceptions and what remains subjective are all present and separately located. §5.2's warning — that *"a session under pressure to extract doctrine could read this lesson as stating four rules"* when it states four **considerations** and one preference — is the mark of someone who has understood the lesson rather than mined it.

### M. Blind recognition — **NOT SATISFIED, with B.** Same `D-030` ground, same accounting (§14). Not separately charged.

### N. Ambiguity review — **PASS**

Four new records (`A-055` M0–M3 labels, `A-056` Hi-Lo, `A-057` "A pattern", `A-058` "tilted") — **none resolved**, all correctly opened rather than defined away. Eleven records extended and explicitly **not closed**.

**Two judgement calls are better than the alternative and are endorsed:** `A-057` is *not* merged with `A-047`'s *"M, A1, A2"* despite the surface similarity, and `A-044` is extended on a **new axis** (geometry) without being fused to V06's candle-name axis. **No subjective term is converted into a constant anywhere** — *tilted*, *strong*, *clean*, *enough space* all remain open, and `[00:31:29]`'s *"50% of what you see"* is explicitly *"recorded as a number, not adopted as a filter rate."*

### O. Contradiction review — **PASS**

No new `C-xxx` opened, and the one candidate — V07's *"10 from DMR"* against V04's *"just 12 pairs"* — is **checked and rejected with reasons** (different objects: a programme watchlist versus a guest's pared-down personal list), with the V04 markers correctly labelled as V04. That is the right disposition and it is recorded so a later session does not re-derive it.

**`C-005` and `C-006` gain material and neither is adjudicated** — correctly left to the reviewer under `D-003`. **This reviewer does not adjudicate them either**, and states why: the new material is a *student's* perception of divergence (`[00:29:34]`–`[00:29:55]`) plus a coach's **non-answer**, verified mechanically by probe `R07` and confirmed by this reviewer's own read of the twelve following entries. A non-answer is evidence that the question is open; it is not evidence of which side is right. Both records stay **`UNRESOLVED`** and neither is foundational to V07, so `PASS`-with-open-research is the correct outcome under §6O.

### P. Machine-rule firewall — **PASS**, and unusually strictly

Nothing is promoted to `12_MASTER_SPEC/` or `13_MACHINE_SPEC/`. Eight of the ten interpreted rules carry an explicit blocker; the only two the student will defend as codable (research-over-a-year, 50-pip sizing basis) are **not trading signals**, which the file says itself. The `D-030` refusals are applied *against the student's own interest* — the drawdown claim at `[00:08:04]` is identified as the most testable and consequential thing in the lesson and is **still refused**, because *second leg* is undefined. That is the firewall working.

### Q. Claimed accuracy — **PASS**

No 90–95% accuracy claim is made in V07 and none is imported. The nearest thing — *"you're going to make pips every day"* — is preserved verbatim, sourced, tested at its ceiling, and explicitly **not** treated as a required outcome.

---

## 14. DIMENSION B — EXPLICIT ACCOUNTING, AND WHY IT CARRIES NO SEVERITY CHARGE

**V06 R1/R2 carried B as *"blocked by `D-030`, excluded from pass/fail per owner directive."* No such directive exists for V07.** B is therefore **scored** here.

**The score is: NOT SATISFIED.** The student does not claim otherwise; the mastery report states it plainly and refuses the `NOT APPLICABLE` label on the correct ground that `D-019` grants it to dimensions F and G only. That refusal is right and is endorsed.

**It carries no `CRITICAL`, `MAJOR` or `MINOR` charge, for three reasons stated on the record:**

1. **The cause is the source material, not the student.** V07 names eight objects to be recognised and defines none of them. No amount of student effort produces recognition of an undefined object.
2. **The correct behaviour and the failing behaviour are indistinguishable in the score, and only one of them is safe.** A session that *had* satisfied B would have done so by inventing definitions — which is `REVIEW_PROTOCOL.md` §17 failure mode 1 and the exact fabrication `Q-007`/`Q-008` exist to catch. **Charging a severity here would penalise the discipline the project mandates and reward its violation.** §16 forbids creating artificial difficulty.
3. **The student did the maximum available and labelled it honestly** — `PT-033` on the one V07 object needing no course definition, and a base-rate census of a **declared non-course** shape family under an explicit fence, with both stated as *not* recognition of a course object.

**What this reviewer will not do is smuggle it into a `PASS`.** B is unsatisfied, it is recorded as unsatisfied, and `REVIEW_PROTOCOL.md` §9's PASS criteria 6 and 7 are consequently unmet. That is part of why this round is **`REVISE`** rather than `PASS`.

> ### ESCALATION — THIRD LESSON RUNNING, AND NOW A STANDING COST
>
> V05 R1 proposed the `EXCLUDED BY DECISION` vocabulary (`REVIEW_INDEX.md` **open item 36**). V06 R1/R2 needed an ad-hoc owner directive to proceed. V07 has no directive and must reason it out from first principles in a review file. **Three lessons, three different dispositions of the same structural fact — that is itself a corpus-hygiene defect.**
>
> **The owner owes a ruling on open item 36.** Until it lands, every reviewer will re-litigate this, and the decision table's `Major Issues` column will keep failing to express the one thing that is actually true about these lessons: *the course does not define its own terms, and that is not the student's error.*

---

## 15. REQUIRED CORRECTIONS (specific, per §10)

Three, all documentation. **None holds the gate** (`D-024`: 0 CRITICAL, 0 MAJOR). All must be applied before V07 reaches `COMPLETE`, with superseded text retained per `REMEDIATION_PROTOCOL.md` §2.

1. **`V07_SOURCE_NOTES.md` §10** — correct the *level* row from **26** to **56** uses, or state which sub-count was intended. §5's 56 is correct and must not be changed to match. *(M1)*
2. **`V07_SOURCE_NOTES.md` §10** — correct the *"the peak"* row from **4×** to **5×**. The five markers already listed are correct and must not be changed. *(M2)*
3. **`V07_MASTERY_REPORT.md` §D** — restore the quotation to the transcript's literal *"if it doesn't do what you expect **in** your flashcard isn't the same"* and re-cite it to **`[00:28:31]`** (not `[00:28:28]`). **In the same edit**, repair or scope §H's sentence *"No quotation mark in any V07 artifact contains a word that is not in the source"*, which this finding falsifies. `V07_SOURCE_NOTES.md` §6c already renders the passage correctly and must not be edited. *(M3)*

**Explicitly NOT required — do not do these:**

- **Do not re-run `PT-033`, the sensitivity, the cross-check, or any homework script.** All were re-run by this reviewer from the committed tree and reproduce **bit-exactly**, including `pt033_results.json` byte-for-byte.
- **Do not rewrite git history to repair the `I-009` sweep.** The audit trail is intact (§N1) and a rebase while a concurrent session holds this working tree can destroy uncommitted work. `SETUP_ISSUES.md` I-009 already says so and is correct.
- **Do not "fix" `R11`.** The failing probe is doing its job and must stay failing in the committed tree.
- **Do not refresh §H's "163 citations"** as a separate task; fold it in whenever §H is next edited (N2).

---

## 16. DISPOSITIONS THE STUDENT ASKED THE REVIEWER TO SET

The submission is `REVIEW REQUIRED` on two named uncertainties. Both are ruled on here.

| Item | Ruling |
|---|---|
| **Dimension B** — no vocabulary for "blocked by `D-030`" | **Scored NOT SATISFIED, no severity charge, escalated to the owner.** §14 |
| **Dimension F** — the demo-account part marked `NOT APPLICABLE` | **UPHELD as `NOT APPLICABLE`.** `D-018` forbids opening an account and `D-019`'s test is *is there anything here to do at all* — for an agent, there is not, and no future lesson or infrastructure change makes practising entries on a live demo account performable. This matches V01's H6/H7 disposition exactly. **Not overturned to `DEFERRED`**, because `DEFERRED` implies a future in which it becomes doable and there is none |

**Two escalations the student raised are endorsed and forwarded unchanged:**

- **`A-056` is the third instance of the `A-039` shape** — a component the course treats as load-bearing and never teaches (TDI, the DMR's operative detail, now Hi-Lo). **Raise at `CUMULATIVE_25.md` as a pattern, not three records.**
- **The day boundary moves a result by ~14 points and the project has no decision on it**, while it has a two-arm decision on the timezone (`D-031`). Every future daily-extreme test inherits this. **A `D-031`-shaped two-arm rule for the day boundary is the obvious repair; it is the owner's to make.**

---

## 17. DECISION

The V07 submission is the strongest student work in this repository to date on every dimension the protocol can score. The backtest chain is pre-registered, reproduces bit-exactly, returns an honest `INDETERMINATE`, scores its own prediction as part-wrong, discloses two unanticipated defects against itself (the Arm-B stubs and the `C8` hole), and pre-commits against the misreading its own author was most likely to make. The homework preserves a misleading first attempt and turns it into a finding about the assignment. A comprehension probe was allowed to fail and the failure was written up rather than smoothed. The one process collision in the round was diagnosed further than it needed to be and improved project method as a result.

Against that: **three documentation defects**, two of them in the same table of self-declared "cheaply falsifiable" counts, one a single altered word inside a quotation mark that happens to falsify a categorical self-certification. All three are corrections of the record, not of the method. **No finding of any severity touches a conclusion, a number, a verdict, or the audit trail.**

**Dimension B is unsatisfied and is not being waved through** — which is why this is not a `PASS`.

```text
LESSON: V07
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES: none

MAJOR ISSUES: none

REQUIRED ACTIONS:
1. V07_SOURCE_NOTES.md §10 — "level" 26 -> 56 uses (§5's 56 is correct).
2. V07_SOURCE_NOTES.md §10 — "the peak" 4x -> 5x (the five markers are correct).
3. V07_MASTERY_REPORT.md §D — restore "in your flashcard", re-cite to
   [00:28:31], and repair or scope §H's "no quotation mark ... contains a
   word that is not in the source".

ADVANCEMENT:
AUTHORIZED — under D-024 (0 CRITICAL, 0 MAJOR) the V08 gate OPENS with the
three MINORs deferred and still owed. V07 reaches COMPLETE only when they
are applied and verified at R2.

OWNER RULING OWED: REVIEW_INDEX.md open item 36 (dimension B vocabulary),
third lesson running. Not a gate.
```

---

## 18. LOGGING

`REVIEW_INDEX.md`: decision row (V07 R1 REVISE 0/0), open items 61–63 for M1–M3, E20 count-class and E01/E11 ledgers updated, STATUS block updated with the superseded text retained. `LOG.md`: reviewer R1 entry. Next review trigger: **student remediation of items 61–63**, then R2. `CUMULATIVE_25.md` should pick up the `A-039`/`A-056` untaught-component pattern, the day-boundary decision gap, and the `E20` count class — which item M1/M2 push to their sixth and seventh instances.
