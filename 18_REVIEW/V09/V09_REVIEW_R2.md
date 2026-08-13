# V09 — INDEPENDENT VERIFICATION REVIEW R2

| Field | Value |
|---|---|
| Lesson | V09 — **no printed title** (`Bootcamp1 Wk2 032612 Part4 (53mins).swf`, 00:52:26) |
| Review round | R2 — **verification of the R1 remediation** |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent |
| Subject | `18_REVIEW/V09/V09_REVIEW_R1.md` items **73–78**, applied at `16c43ea` (`fix/v09-r1-minors`) and `89bb858` (`SWF_CAPTURE_RECIPE.md`) |
| `D-003` separation of duties | **SATISFIED — and this is the round where it matters.** This session authored **no** V09 artifact, did **not** write `V09_REVIEW_R1.md`, and did **not** perform the remediation. It re-derived every one of the six findings from primary sources before looking at any fix |
| Review basis | Branch **`review/v09-r2`, created FROM the integration branch at `5db04d8`** (`D-038`). `fix/v09-r1-minors` and `review/v09` are both **already merged** into integration; `origin` is in sync, zero divergence. Verified by `merge-base --is-ancestor` before any read |

---

## EXECUTIVE BLOCK

```text
LESSON:     V09
DECISION:   REVISE
CONFIDENCE: HIGH

R1 ITEMS 73-78:   ALL SIX APPLIED CORRECTLY. All six CLOSED — VERIFIED.
                  Every original finding was re-derived from source and
                  every one was REAL. Every fix was checked against the
                  primary source, not against the remediation's account
                  of itself. Superseded-text convention followed at every
                  one of the sites checked.

NEW THIS ROUND:   CRITICAL 0   MAJOR 0   MINOR 3   (items 81, 82, 83)

  81  E01  The mechanized quote check that item 73 REQUIRED was never
           run, and a FIFTH instance of the same defect survives in the
           same file, 38 lines from the corrected one.
  82  E11  Two frame cross-references still carry the stale ordinals
           item 76 was raised to eliminate — in the SHARED ambiguity
           register (A-069, A-073), which outlives the lesson.
  83  E19  The mastery report still puts escalation 5 to the owner as a
           live judgement call, after item 77 retired it.

PT-035:     BYTE-UNCHANGED FROM PRE-REGISTRATION. Verified by blob SHA,
            not by diff: c274088836a0… at 0f709d2 and at HEAD, one commit
            in its entire history. run_pt035.py likewise 9215e3ac79e5…
            at 7c3fe2d and at HEAD, one commit. RE-EXECUTED here: both
            output files reproduce byte-identically.

ITEM 78:    BOTH HALVES COMPLETE AND MUTUALLY CONSISTENT. The reviewer's
            policy-ledger edit is sound and its probe script was TESTED
            VERBATIM here on both stage classes. The student half cites
            it correctly.

ITEMS 79/80: accurately characterised as NON-BLOCKING. Confirmed, not
            resolved. They are forward work, not V09 debt.

V09 STATUS: **NOT COMPLETE.** R3 required. The three new minors are all
            small, none moves a conclusion, and none corrupts downstream
            learning — but two of them are LIVE WRONG POINTERS and one
            asks the owner to rule on a question the project has already
            closed. Under D-024 nothing gates: V10 remains OPEN.

MERGE:      NOT PERFORMED. The verdict is not clean, so per the standing
            instruction and D-038 this branch is NOT merged back.
```

---

## 0. WHAT THIS REVIEWER RE-DERIVED FROM PRIMARY SOURCES, BEFORE READING ANY FIX

The remediation's own account of what it changed was read **after** this table was complete. Nothing
below is taken from `LOG.md`, from the commit messages, or from the mastery report's revision block.

| # | Claim under test | Method used here | Result |
|---|---|---|---|
| 1 | Item 73's four misquotes were real | read `V09_TRANSCRIPT.md` at the four cited markers | **ALL FOUR REAL.** `[00:03:49]` reads *"Example solid **high low-day** entries"*; `[00:41:25]` *"What is the **grade** Fred?"*; `[00:44:39]` *"**experiences show** me"*; `[00:19:55]` *"what **it's it's** titanium"*. R1's transcription of each is exact |
| 2 | Item 75's gap count | wrote my own scanner over lines fully matching `^\[\d\d:\d\d:\d\d\]$` | **721 markers, 718 distinct, ZERO decreasing transitions.** 11 s **twice** at `[00:07:03]`, `[00:44:56]`. 10 s **SEVEN** times at exactly `[00:02:38]`, `[00:03:23]`, `[00:19:18]`, `[00:23:05]`, `[00:45:41]`, `[00:49:35]`, `[00:49:47]`. R1's list is exactly right and the original *"four"* was wrong |
| 3 | Item 76's off-by-one | listed the 27 PNGs and mapped every ordinal R1 named | **REAL.** Position 15 is `V09_00-15-00_can-have-more-losers-than-winners.png`; every ordinal at 15+ shifts by one. Spot-verified: old *"frame 17 error 2"* → the five-errors slide is **18**; old *"frame 18"* 85% → **19**; old *"frame 22"* broker → **23** |
| 4 | Item 74's clause exists as R1 quotes it | read `PT-035` §6 **in the pre-registration blob**, not in the observation | **REAL AND VERBATIM.** §6's fourth row: *"**INDETERMINATE** — Cells disagree across the 5%/10% boundaries, **or `N3` fails**"*. §7b is headed *"WHAT WOULD MAKE THIS TEST VOID"*, item 1 *"`N3` fails"*. `N3` did fail. The clause was live and unapplied |
| 5 | The closed form the verdict now rests on | **wrote my own run-length DP recursion** — not the runner, not R1's code | **CONFIRMED TO THE REPORTED PRECISION.** P(≥1 four-loss run in 200) = **99.93%** at p=0.50, **54.13%** at p=0.73, **100.00%** at p=1/3. Threshold for ≤5% in 100 trades: **84.19%**. `CONTRADICTED AS STATED` genuinely needs no measurement |
| 6 | Item 77's set-level arithmetic | read `MMM-NOTES` **at source**, not via the corpus's quotation of it | **CONFIRMED.** p.38 line: *"The specific EMA's used in Mauro's charts are the **5, 13, 50 and 200** bar"* — four averages. **`800` occurs ZERO times in the whole extract.** The *"any other rapidly moving pair of EMA's would achieve the same goal"* quotation is verbatim. `A-020` independently records **Mayo = 200** and **Blueberry = 800** as two attested lines, so the identity does collide with it |
| 7 | Item 78's stage geometry | **parsed the SWF `RECT` from every file myself** | **CONFIRMED, exactly.** Of the 21 canonical `Bootcamp/` files, **exactly three** declare `1280×738` — Wk2 Part3 (V08), Wk2 Part4 (V09), Wk10 (V21). The other eighteen declare `1024×786`. R1's and the recipe's numbers are right |
| 8 | Item 78's V08 corroboration | read `04_SCREENSHOTS/V08/INDEX.md` | **REAL AND VERBATIM.** *"The first 529-frame sweep produced one distinct image, 529 times… `mouse.click(512, 300)` misses the play target on this file — V08's splash centres its play button at approximately `(512, 325)`."* Same coordinate, same correction, one lesson earlier |
| 9 | `PT-035` and its runner are untouched | **blob SHA at the pre-registration commit vs HEAD**, plus full file history | **BYTE-IDENTICAL.** `c274088836a0…` and `9215e3ac79e5…` at both ends. **One commit each in their entire history.** No diff of any kind |
| 10 | The backtest still reproduces | re-ran `run_pt035.py` from the committed tree | **`pt035_output.txt` and `pt035_results.json` byte-identical** (SHA-256 before and after), `git status` clean |
| 11 | The homework scripts still reproduce | re-ran all three | **All three exit 0 and rewrote their outputs with the working tree left clean** |
| 12 | Citation integrity survived the edits | re-parsed every `` `[hh:mm:ss]` `` citation in the six V09 artifacts against the transcript's 718 markers | **208 distinct citations, ZERO orphans.** The remediation did not break a single pointer |
| 13 | The GOTCHA 5 probe script works as written | **ran it verbatim, copied out of the recipe**, on one file of each class | **WORKS ON BOTH.** Returns `stage 1280 x 738` and `stage 1024 x 786`. The reviewer's claim to have tested it is true — and this matters, because my own first attempt at the same parse failed on a truncated read and the recipe's version does not |
| 14 | A load-bearing frame says what the new timecode convention claims | **opened the PNG** | **CONFIRMED.** `V09_00-21-40_…png` carries a burned player timecode reading `21:40 / 52:2…`, matching its filename, and its **error 2** is *"Putting on Multiple Positions which add up to GREATER than your % Risk"* — exactly what `A-065` cites it for. The letterbox bands the stage-geometry finding predicts are visible in the same image |
| 15 | No forbidden remediation act occurred | `git log` on every review file; deletion count in `LOG.md` | **CLEAN.** No prior review file has been touched since it was written — `V09_REVIEW_R1.md` has exactly two commits, both from R1. `LOG.md` gained **88 lines and deleted zero**. No history rewrite |
| 16 | Validator | `python3 scripts/validate_project.py` | **103 passed, 0 warnings, 0 failures** |

### 0a. What this reviewer did NOT verify independently

**The frames were not re-captured**, as at R1 and V08 R1 — no Ruffle/Playwright rig was stood up.
What was done instead: the load-bearing frame was read as an image and its burned timecode checked
against its filename, and the stage-geometry finding was re-derived from the SWF headers and the
committed pixels, which needs no re-capture.

**The Whisper re-transcription was not re-run.** Nothing in this round turns on it; the four item-73
quotations were checked against the committed transcript body, which is the artifact the `AUDIO`
basis tag actually points at.

---

## 1. THE SIX ITEMS — ADJUDICATED ONE BY ONE

### Item 73 — `M1` (`E01`), four silent ASR corrections inside quotation marks — **CLOSED — VERIFIED**

**The finding was real.** All four markers were read in the transcript body and every one reads as
R1 said (§0 row 1).

**The fix is correct at all four sites**, and better than a minimum compliance:

| Site | Now reads | Correction placed |
|---|---|---|
| §3 / the 3:1 arm | *"Example solid **high low-day** entries…"* | outside the quote, with the printed `HOD/LOD` form named and the gate rows **retagged to quote the PRINTED text** — which is the stronger of the two remedies R1 offered |
| §9a | *"What is the **grade** Fred?… my own little twist **twist**"* | a table beneath the quote naming both artefacts, plus a retained superseded block |
| §7e | *"…and **experiences show** me…"* | superseded block naming the previous wording |
| §5 | *"what **it's it's** titanium or diamond"* | inline note, *"the doubled it's is the speaker's own stutter and is left standing"* |

**Superseded-text convention: FOLLOWED** at every site, in the `REMEDIATION_PROTOCOL.md` §2 form,
citing `V09_REVIEW_R1.md` `M1`.

**The transcript body was NOT edited, and this was verified rather than assumed.** I extracted the
verbatim body from the pre-remediation commit and from `HEAD` and hashed both:
`90fd603b7c69117f…` on each. **Byte-identical.** The only change to the file is in its header
COVERAGE block.

**Closed. But see new item 81** — the item's *other* required action, the mechanized sweep, was not
performed, and a fifth instance survives. That is charged separately rather than held against this
item, because the four sites R1 enumerated are all correctly repaired.

---

### Item 74 — `M2` (`E20`), `PT-035` §6's `INDETERMINATE` clause — **CLOSED — VERIFIED**

**The finding was real, and I checked it against the pre-registration blob rather than the
observation's quotation of it** (§0 row 4). §6's fourth row fires on `N3` failure; `N3` failed; the
word `INDETERMINATE` appeared nowhere.

**The fix is complete and correctly scoped:**

- `BT_V09_0001` §5 now carries a block quoting §6's decision table **in full**, states that the
  measured arm is `INDETERMINATE`, and carries `CONTRADICTED AS STATED` on the §2c/`O4` closed form
  **alone**. §1's verdict row carries the same qualification.
- **`P3` is re-scored** to *"RIGHT ON THE MEASUREMENT, VOID ON THE VERDICT CLAUSE"*, with the prior
  score retained in parentheses, and the tally moved `3/1/1` → `2/1/1/1` with the old tally quoted.
- **Propagated to all three places R1 named**: mastery report §G (line 146), the mastery report's
  self-assessment, and `LOG.md`. Verified by grep in each file.

**`PT-035` and `run_pt035.py` were NOT edited** — verified by blob SHA and by single-commit history,
which is a stronger check than a diff (§0 row 9). `COMMON_PROTOCOL.md` §9 rule 7 honoured.

**The conclusion the fix leans on holds.** I wrote my own run-length DP and got 99.93% / 54.13% /
100.00% / 84.19% (§0 row 5). The closed-form route genuinely needs no measurement, so reporting the
measured arm as `INDETERMINATE` costs the verdict nothing. **The remediation did not weaken a
finding to satisfy a reviewer; it relocated the finding onto the load-bearing evidence.**

**Superseded-text convention: FOLLOWED**, inline at each changed cell.

---

### Item 75 — `M3` (`E19`), the COVERAGE block's 10-second gap count — **CLOSED — VERIFIED**

**The finding was real and I re-measured it from scratch** with the block's own stated method
(§0 row 2): seven 10-second gaps, at exactly the seven markers R1 listed. The original *"four"*
understated it by three.

**The fix is exact**: the block now reads *"Next largest 10 s, SEVEN times"* and lists all seven, in
order. A retained correction block quotes the superseded sentence in full and records that every
other assertion in the block reproduces — which I independently confirmed (721/718, zero decreasing,
11 s twice).

**Superseded-text convention: FOLLOWED.** **Body untouched, proven by hash.**

---

### Item 76 — `M4` (`E11`), fourteen off-by-one frame cross-references — **CLOSED — VERIFIED**

**The finding was real.** The 27-frame listing confirms `V09_00-15-00_…` sits at position 15, and
every reference R1 named maps as R1 said (§0 row 3).

**The fix took R1's *preferred* route rather than its minimum**, and that was the right call: bare
ordinals were replaced with **burned-in player timecodes**, which no future insertion can invalidate.
Verified by counting bare `frame N` references in each V09-scoped file:

```text
V09_SOURCE_NOTES.md        0
V09_INTERPRETATION.md      0
BT_V09_0001.md             0
V09_MASTERY_REPORT.md      0
V09_TRANSCRIPT.md          0
04_SCREENSHOTS/V09/INDEX.md  4  -- all legitimate (see below)
```

INDEX.md's four survivors are correct and were each checked: one is the table's own internal
reference (*"the same slide as frame 14"*), one is `frame 3` (below the insertion point, unaffected,
and correct), one is `frame 23, burned 28:45` (correct, and now carries the timecode), and one is a
**V05** frame reference, out of scope. The file states the governing rule explicitly — *"the numbered
column below is an index into this table only, and nothing outside this file cites it."*

Spot-verified conversions against the actual frame list: `C-013`'s *"frames 19–21"* → burned
`25:00`/`26:00`/`26:40` (= 20, 21, 22 ✓); its *"Frames 12, 13, 15, 18"* → burned
`10:15`/`11:40`/`15:00`/`22:45` (= 12, 13, 15, **19** ✓ — only the fourth shifted, and it shifted);
`C-015`'s *"frame 16"* → burned `17:05` (= 17 ✓); `A-065`'s *"frame 17 error 2"* → *"the five-errors
frame burned `21:40` — error 2"* (= 18 ✓, and **I opened that image**: error 2 is there, §0 row 14).

**Superseded-text convention: FOLLOWED** — `INDEX.md` carries a retained block naming the cause
(`ff7b8bd`'s insertion), the fourteen references, and the reason the fix is structural.

**Closed for the fourteen enumerated references. See new item 82** — two references carrying the
identical stale string survive in the shared ambiguity register at sites R1 mis-attributed.

---

### Item 77 — `M5` (`E02`), the `C-010` reconciliation held at `MEDIUM` — **CLOSED — VERIFIED**

**The finding was real, and I verified its arithmetic against the primary source rather than the
corpus's report of it** (§0 row 6). `MMM-NOTES` enumerates four averages and contains no `800` in
84 pages; `A-020` attests Mayo = 200 and Blueberry = 800 as two distinct lines. The factor-of-four
identity therefore lands one member of four and collides with `A-020`. R1's arithmetic is sound.

**All three required actions performed:**

1. `V09_INTERPRETATION.md` Q5 **downgraded `MEDIUM` → `LOW`**, with the set-level mapping written
   out as a code block and the member-by-member outcome tabulated.
2. Q8's falsification row corrected to *"**Nothing, on its own**"*, with the reason and the
   superseded row quoted.
3. `C-010`'s V09 block annotated with the same reasoning, a per-member table, and the `A-020`
   collision — and it explicitly restates **`C-010` STAYS UNRESOLVED. Disposition unchanged.**

**The decision was not moved, only the confidence** — which is exactly what R1 charged and exactly
what R1 asked for. The remediation also went one step further and identified that this retires the
submission's escalation 5. That is correct. **It then did not carry it into the file where the
escalation lives — see new item 83.**

**Superseded-text convention: FOLLOWED**, with an explicit note that *"the **decision** is unchanged;
only the confidence and the reasoning are."*

---

### Item 78 — `M6` (`E20`), the split item — **CLOSED — VERIFIED, BOTH HALVES**

This item was flagged for special scrutiny because a reviewer edited a policy ledger directly. **Both
halves check out, and the split was handled correctly.**

**The reviewer's half — `SWF_CAPTURE_RECIPE.md` at `89bb858`.** The edit is in-scope for a policy
ledger under `D-038a`, is confined to one file, and is on the integration branch as `D-038a`
requires. On the substance:

- **The stage-geometry claim is true and I re-derived it independently** — exactly three of the 21
  canonical files are `1280×738` (§0 row 7).
- **The probe script works verbatim** (§0 row 13). This is worth stating because a recipe is a
  document whose only value is that it runs, and it does.
- **The edit is correctly hedged.** It does not merely publish a two-row coordinate table; it says
  *"Do not trust the table alone"*, notes a third stage size may exist in unopened material, and
  makes the **general** remedy — screenshot before and after the play click, exit non-zero if
  identical — the standard. That remedy needs no table and is credited to V08's own index rather
  than reinvented. **A policy edit that reduces its own authority in favour of a mechanical check is
  the right shape for a policy edit.**
- **It does not overreach into the student's territory:** it makes no claim about V09's artifacts.

*One small imprecision, not charged:* GOTCHA 5 says *"this library holds two sizes… the other
eighteen files"*, which is true of the 21 canonical `Bootcamp/` files but not of the wider
`01_SOURCE_VIDEOS/` tree — the `More videos/` directory holds 18 further `1280×738` files. **Nothing
turns on it**, because the recipe's operative instruction is to read the header per file and the
guard is table-free. Recorded so a later session capturing from `More videos/` is not surprised.

**The student's half.** `04_SCREENSHOTS/V09/INDEX.md` and `V09_MASTERY_REPORT.md` escalation 2 both
now state that the coordinate **also failed on V08**, quote and cite `04_SCREENSHOTS/V08/INDEX.md`,
and carry the stage-geometry cause. I verified the V08 quotation is verbatim (§0 row 8). Grep
confirms **no live *"V01–V08"* claim remains** in either file — the three surviving occurrences of
that string are all inside retained superseded-text blocks, which is the convention working
correctly rather than a miss.

**The two halves are mutually consistent.** Both give `(512, 325)` for the `1280×738` class, both
name V08/V09/V21, both attribute the cause to the declared stage size against a `1024×786` viewport,
and the student half cites `89bb858` and `GOTCHA 5` by name. The `REVIEW_INDEX.md` row for item 78
correctly tracks the two halves separately. **No daylight between them.**

**Superseded-text convention: FOLLOWED** in both files.

---

## 2. ITEMS 79 AND 80 — CONFIRMED NON-BLOCKING, NOT RESOLVED

Read, as asked, and not adjudicated on the merits.

| Item | Characterisation in `REVIEW_INDEX.md` | This reviewer |
|---|---|---|
| **79** — the `PT-035` successor | 🔶 **OPEN — recommended.** *"RECOMMENDED, NOT OWED"* | **ACCURATE.** It is forward work under a new `PT` number, not debt against V09. Its premise is sound and is corroborated by this round: `BT_V09_0001` §4 names the correct comparator and **declines to compute it** because it was not pre-registered, which is the `D-026`/`E21` refusal working. The requirement it carries — *both `N3` gates encoded in code, not prose* — is the right lesson from item 74 |
| **80** — resolution-censoring bias | 🔶 **OPEN — escalated.** Scope tightened to `PT-033`/`PT-034`/`PT-035` | **ACCURATE.** Correctly framed as an escalation over the `PT` family, explicitly **not** a retroactive invalidation of `PT-034`, with the direction-of-bias argument stated. It is a standing research item, not a V09 correction |

**Neither is owed by V09 and neither blocks `COMPLETE`.** Both are correctly filed against the
project rather than against the lesson. **No action taken on either here.**

---

## 3. NEW FINDINGS THIS ROUND

### Item 81 — `MINOR` (`E01`) — item 73's required mechanized check was never run, and a fifth instance of the same defect survives

`V09_REVIEW_R1.md` §15 item 1 required **two** things: generalise and **run**
`05_HOMEWORK/V07/scripts/verify_quotes.py` over the seven V09 artifacts, *and* fix each hit. **The
four enumerated hits were fixed by hand. The sweep was not run.**

- `verify_quotes.py` exists only at `05_HOMEWORK/V07/scripts/`, still V07-specific.
- Its entire history is one commit, `cc74051`, from the **V07 R2/R3** round. **Nothing has touched it
  since**, so it was neither generalised nor re-run.

**And the omission has a demonstrable cost, not a theoretical one.** `V09_SOURCE_NOTES.md` line 410:

```text
| **50 pips** | What market makers *"can grab all their stuff at"* | `[00:44:44]` | **ANECDOTAL** — *"experience shows me"* |
```

The transcript at `[00:44:39]` reads *"**experiences show** me"*. **This is the same phrase, in the
same file, that item 73 corrected 38 lines above** — where a retained superseded block now states in
terms that *"the transcript reads **experiences show** me"* and that *"an `AUDIO`-tagged quotation
may not be tidied."* **The file now contradicts itself about what the audio says.**

**Why this is charged at `MINOR` and not waved through.** Nothing moves — it is a plural, in a
descriptive basis column. But the project's settled position, restated by R1, is that this is its
most durable defect class (V02 R1, V04 `M2`, V05 `M3`, V07 `M3`, V09 `M1`), and **the specific
remedy prescribed for it is mechanization precisely because hand-fixing an enumerated list leaves the
un-enumerated ones.** That is what happened. The four sites a human was pointed at are clean; the
fifth, which only a sweep would have found, is not.

**Required:** generalise `verify_quotes.py` to take a lesson identifier, **run it over the seven V09
artifacts**, commit the run, and fix every hit it returns — starting with line 410. Retain superseded
text.

---

### Item 82 — `MINOR` (`E11`) — two stale frame ordinals survive in the shared ambiguity register

Item 76 was raised because bare ordinals became wrong when a frame was inserted. The fix eliminated
them from every V09-scoped file. **Two survive in `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`:**

| Line | Record | Text | Should be |
|---|---|---|---|
| 4982 | **`A-069`** — *"high low tracer"* | *"Visible on **frames 22, 23 and 25** as chart furniture"* | **23, 24 and 26** — burned `28:45`, `31:50`, `41:25` |
| 5173 | **`A-073`** — *"reset"* | *"Also printed on **frames 22, 23 and 25** as a chart label"* | **23, 24 and 26** — same three |

**These are live wrong pointers, and I confirmed where they now land.** Under the current numbering,
frame 22 is the **compounding spreadsheet** (`00-26-40`) and frame 25 is the **MS Paint email
address** (`00-34-35`). Neither is a chart. A reader following `A-069` to see a *"high low tracer"*
lands on a spreadsheet — which is `M4`'s stated harm, verbatim, still present.

**Why this is not simply held against item 76.** R1's `M4` table attributed the string *"frames 22,
23 and 25"* to `04_SCREENSHOTS/V09/INDEX.md` only. **It occurred in three places, and R1 found one.**
The remediation fixed what it was pointed at — including the two `AUTOMATION_AMBIGUITIES.md`
references R1 *did* enumerate (`A-065`, `A-067`), both correctly converted to timecodes. **The miss
originates in R1's enumeration, not in the remediation's execution**, and it is recorded that way.

**It is still charged**, and at the same severity R1 charged the class, for the reason R1 gave:
these are the provenance handle for `PRINTED`-basis rows, and they sit in a **shared register that
outlives V09** — `A-069` and `A-073` will be read by every later session working on *tracer* and
*reset*, long after `04_SCREENSHOTS/V09/INDEX.md` is closed.

**Required:** convert both to burned timecodes, matching the convention item 76 established. Retain
superseded text.

---

### Item 83 — `MINOR` (`E19`) — the mastery report still puts a retired question to the owner

Item 77's own `REVIEW_INDEX.md` row states: *"**This also retires the submission's escalation 5 to
the owner** — the route does not reach, so no blending judgement is owed."* `C-010`'s new block says
the same in its own words: *"**This also retires the escalation `V09_MASTERY_REPORT.md` put to the
owner**… It does not close."*

**`V09_MASTERY_REPORT.md` escalation 5 is unchanged:**

> *"`C-010` is narrowed and a tidy reconciliation is available and refused. **If the owner judges
> that reading a timeframe into `MMM-NOTES` is acceptable, `C-010` closes immediately.**"* — flagged
> **OWNER**.

**It does not close immediately, and the project now knows why.** Escalation 2 in the same table was
given a `✅ DISCHARGED` marker in this same remediation, so the mechanism was available and was
applied one row away.

**Charged because the owner-escalation table is an action list, not prose.** Its whole function is to
tell a human what is owed, and it currently owes them a judgement the project has established is
moot. This is the *"files that disagree with each other about their own state"* class the project
charges (V05 R1 `M4`), here between the mastery report and both `C-010` and the review index.

**Required:** mark escalation 5 retired, citing item 77 and `C-010`'s V09 block, with the superseded
text retained — in the form escalation 2 already uses.

---

## 4. THE STANDARD REVIEW PASS — WHAT WAS CHECKED FOR REGRESSION

Per the instruction to run a full pass rather than the narrow six-item re-check.

| Check | Result |
|---|---|
| **Validator** | **103 passed, 0 warnings, 0 failures** |
| **Marker citation integrity** | **208 distinct citations across the six V09 artifacts, ZERO orphans.** The remediation touched nine content files and broke no pointer |
| **Transcript body integrity** | **Byte-identical** pre- and post-remediation (hash, §0 row 1 / item 73) |
| **`PT-035` + runner immutability** | **Blob-identical to the pre-registration commits; one commit each in history** |
| **Backtest reproducibility** | `run_pt035.py` re-executed: **both outputs byte-identical**, tree clean |
| **Homework script reproducibility** | all three re-executed, **exit 0, tree clean** |
| **`REMEDIATION_PROTOCOL.md` §2 — redo vs reword** | **CORRECTLY APPLIED.** All six items are genuinely documentation defects — a misquote, an unapplied decision clause, a miscount, wrong pointers, an over-graded confidence, a mischaracterisation. **No underlying test was invalid**, so nothing was owed a redo, and nothing was redone. The remediation states this and it is right |
| **`REMEDIATION_PROTOCOL.md` §6 — forbidden acts** | **NONE COMMITTED.** No review file edited since it was written; `LOG.md` gained 88 lines and deleted zero; no test ID renumbered; no sample narrowed; no rule redefined; no history rewritten |
| **`COURSE_PROGRESS.md` reconciliation** | **CORRECT**, and the staleness it fixed was real: V07 reached `COMPLETE` at R3 and V08 at R2, and the block still said 6 passed / 3 in progress. Now 8 passed / 1 in progress, V10 `GATE OPEN`, with the whole superseded block retained verbatim |
| **`08_CONCEPT_LIBRARY/` / `12_MASTER_SPEC/` / `13_MACHINE_SPEC/` firewall** | **HELD.** The remediation touched none of the three |
| **Nothing closed prematurely** | **CONFIRMED.** Items 73–78 were left at `APPLIED — PENDING VERIFICATION at R2, NOT CLOSED` and `COURSE_PROGRESS.md` at `IN REMEDIATION`. The remediating session did **not** close its own items — which, given the `D-003` deviation, is the single most important thing it got right |
| **`D-003` deviation disclosure** | **DISCLOSED, PROMINENTLY, AND AGAINST ITSELF** — in the commit message with a ⚠ marker, in the mastery report's revision block, and in `LOG.md`. It names the owner authorization, states that authorization covered the fix and not the verification, and specifies that R2 must be an independent session that re-derives each item from source. **This session is that, and it did that** |

**No regression found.** Every check that passed at R1 passes here.

---

## 5. DECISION

```text
LESSON:     V09 — no printed title
DECISION:   REVISE
CONFIDENCE: HIGH

R1 ITEMS 73-78:  ALL SIX CLOSED — VERIFIED AT R2.
                 Every finding re-derived from primary source: all real.
                 Every fix checked against source: all correct.
                 Superseded-text convention followed at every site.
                 Item 78 verified on BOTH halves and found consistent.
                 PT-035 and run_pt035.py BYTE-UNCHANGED.

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

MINOR ISSUES (new):
- 81  E01  The mechanized quote sweep item 73 required was not run;
           a fifth instance survives at V09_SOURCE_NOTES.md:410 and
           contradicts the corrected block 38 lines above it.
- 82  E11  A-069 and A-073 still carry "frames 22, 23 and 25" — the
           stale ordinals item 76 exists to eliminate — in the shared
           register, pointing at a spreadsheet and an email frame.
- 83  E19  Mastery report escalation 5 still asks the owner to rule on
           C-010's closure after item 77 retired the question.

REQUIRED ACTIONS:
1. Generalise and RUN verify_quotes.py over the seven V09 artifacts;
   commit the run; fix every hit, beginning with line 410.
2. Convert A-069's and A-073's frame ordinals to burned timecodes.
3. Mark escalation 5 retired, in the form escalation 2 already uses.

ADVANCEMENT:
V10 gate REMAINS OPEN under D-024 (0 CRITICAL, 0 MAJOR). Nothing here
gates. V09 does NOT reach COMPLETE — the three minors are owed and
V09 reaches COMPLETE at R3.
```

### Why `REVISE` and not `PASS`

**This was close, and the reasoning is stated so it can be argued with.** The remediation did what it
was asked to do, on all six items, correctly, and in two places chose the stronger of the two
remedies offered. Nothing it did is wrong. A `PASS` would be defensible on the six items alone.

It is not given, for one reason: **two of the three new findings are live wrong pointers, and one of
them is exactly the defect the round was convened to remove, surviving in the shared register.**
`REVIEW_PROTOCOL.md` §9's condition 2 — important rules have provenance — is breached by item 82 in
the same way `M4` breached it, and item 81 leaves a file contradicting itself about its own source.
Condition 14 is comfortably satisfied — these do not corrupt downstream learning — which is why the
gate stays open and V10 is unaffected.

**The honest summary is that the remediation is good and the enumeration it was working from was
incomplete.** Item 82's miss originates in R1's own table; item 81's does not, and is the one the
next round should treat as instructive.

### Why `HIGH` and not `MEDIUM`

Nothing was accepted on the remediation's authority, which mattered more than usual this round
because the remediating session was also the reviewing session. Every one of the six original
findings was **re-derived from the primary source before the fix was read**: the transcript at four
markers, a scanner I wrote for the gap counts, the SWF headers parsed from all 21 files, `MMM-NOTES`
read at source, `PT-035` §6 read in the pre-registration blob, and the binomial result re-derived in
my own run-length recursion. The immutability claim was checked by **blob SHA and commit count**
rather than by diff. The backtest and all three homework scripts were **re-executed**. The recipe's
probe script was **run verbatim**. One load-bearing frame was **opened as an image**. The three new
findings were each confirmed by reading the current file, not inferred.

The `D-003` deviation is disclosed and it was handled correctly by the remediating session — it
closed nothing. **This round supplies the independent verification that authorization did not
waive**, and it reaches a different verdict than the remediating session would have, which is the
point of running it.

### A statement this review should make plainly

**The remediating session applied a correction against its own interest and it should be recorded.**
Item 74 required it to report its own headline arm as `INDETERMINATE`. It did — quoting the clause
in full, re-scoring its own prediction `P3` downward, moving its own tally from `3/1/1` to
`2/1/1/1`, and writing *"item 74 is the finding this session should have made against itself and did
not."* It did that while holding the pen on both the review and the fix, with nobody yet checking.
**That is the behaviour the separation-of-duties rule exists to guarantee when it cannot be
guaranteed structurally**, and this round found it present.

---

## 6. BRANCH, MERGE AND LOGGING

**Branch state established by `git fetch --all` and `merge-base --is-ancestor` before any read:**

```text
claude/add-documents-repository-fdfb3u   5db04d8   integration. In sync with origin, 0/0 divergence.
fix/v09-r1-minors                                  ALREADY MERGED into integration (5db04d8)
review/v09                                         ALREADY MERGED into integration
video/v09                                          ALREADY MERGED into integration
review/v09-r2                            THIS REVIEW. Branched FROM integration at 5db04d8.
```

Unlike R1, this round required **no** merge of integration into the task branch: integration already
carried every V09 artifact and both remediation commits, so the review was taken against the current
state directly.

**THE MERGE-BACK IS NOT PERFORMED.** The standing `D-038` instruction conditions the deliberate
merge-back on a clean verdict. **This verdict is not clean** — three MINOR findings are open — so
this branch is pushed and left unmerged. That is a deliberate decision recorded here rather than an
omission.

`18_REVIEW/REVIEW_INDEX.md` updated in the same round: items **73–78** moved to
`CLOSED — VERIFIED at R2`, the V09 decision row and severity totals updated, and new open items
**81**, **82** and **83** filed. `LOG.md` appended.

**Next review trigger:** V09 R3, on resubmission with items 81–83 applied.
