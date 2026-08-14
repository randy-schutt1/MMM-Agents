# V11 — MASTERY REPORT

```text
STUDENT STATUS:  REVIEW REQUIRED
```

> **This is a SELF-ASSESSMENT and a SUBMISSION, not an authorization** (`D-016` / `I-001`).
> Only an independent reviewer's `PASS` makes V11 `COMPLETE` (`D-003`, `D-004`).

| Field | Value |
|---|---|
| Lesson | **V11** · `Bootcamp1 Wk4 040812 Part1 (51mins).swf` |
| SHA-256 | `606cc5a89a0a68aa08c18423342288307d267b65ebb79acd889e48af8c4d2101` — verified against `SOURCE_MANIFEST.md` **and re-verified after the frame-rate patch** |
| Duration | 00:50:56 (3056.927 s audio; 9,171 frames ÷ **3.0** fps = 3057.0 s; manifest 3056 s) |
| Session date | **2012-04-08** — filename `040812`, **and corroborated in-recording** at `[00:25:33]` (*"it was sunday and it was easter"*; Easter Sunday 2012 = 8 April) |
| Printed banner | `MARKET MAKERS BOOT CAMP` / `Week 4` (title card, frame `00-00-40`) · **no topic title asserted** |
| Spoken subject | `[00:25:38]`–`[00:25:43]` — *"let's get to today's lesson"* → **`TDI`** |
| **Speaker** | **THE COURSE AUTHOR, 100% OF RUNTIME** — HIGH confidence, four non-acoustic strands, zero handover language in 51 minutes. Acoustic comparison **NOT run** (V07's ruling) |
| Branch | `video/v11`, dedicated worktree at `MMM-Agents-v11` (`D-038`). Gitignored assets symlinked. **No `I-009` collision.** |
| Gate | **Verified OPEN in `REVIEW_INDEX.md` before any V11 artifact was created.** V10 R1 returned `REVISE` with 0 `CRITICAL` / 0 `MAJOR` / 4 `MINOR` → opens under `D-024`; items 91–94 subsequently closed |

---

## ⭐ THE HEADLINE: A SLIDE HEADED *"PARAMETERS OF RSI"* THAT OMITS THE PARAMETER

V11 is two lessons welded together. The first 25 minutes **restate** the entry protocol with more
force than any prior lesson and add nothing to it. The last 25 minutes **teach the RSI substrate of
the TDI for the first time in the corpus** — six printed slides, eight substantive points — and
retire `A-039`'s standing description *"displayed, not taught."*

**And the most codable-looking content in the lesson is uncodable.** Frame `31:25` prints:

```text
Parameters of RSI:  1. Value of RSI:  0 - 100        4. Bear Range:    60/20
                    2. Normal Range:  70/30          5. Overbought/Oversold  80/20
                    3. Bull Range:    80/40          6. Mid Point or Basis Level of 50
```

**Six parameters, and not the lookback period.** `rsi` occurs 33 times in the audio with no period
attached; no frame among 28 detected screen states shows a settings dialog or a legend; and the
Tier 2 seminar-notes PDF is **also silent** (`D-040` step 2, searched). **`A-080`** opens on it.

**The near-miss is the hazard**: a session skimming for a parameter block **finds one**, and it
does not contain the parameter. The TDI's distributed default of **13** is refused explicitly —
and the trap is well-baited, because `MMM-NOTES` p.38 lists a **13 EMA**, so a session could reach
*"13"* by conflating two indicators and feel sourced doing it.

**The cost was measured rather than asserted** (`V11_HOMEWORK.md` §3): across six candidate periods
on the corpus, *"time above 80"* — V11's own **overextended** condition — ranges from **0.04% to
5.66%. A ratio of 144×.** Even the adjacent pair 13 vs 14 differs by ~20% relative.

---

## THE TEN DIMENSIONS

### A. Recall — **SATISFIED**

`V11_SOURCE_NOTES.md` reproduces the lesson across 12 sections with timestamps, basis-tagged
`AUDIO` / `PRINTED` / `AUDIO+PRINTED`. Independent corroboration:

- **Four Whisper `small.en` spot-checks** at passages chosen **before** results were seen, on the
  criterion *"a passage this session is about to build an artifact on"*. **All four agree**, and
  two *correct* the committed body (`rarer tracks` → **railroad tracks**; and the ASR beats Whisper
  at `[00:47:13]`, which is recorded because a disagreement running *against* the newer engine is
  worth stating).
- **The `GOTCHA 4` content sanity check**: the slide at burned `02:00` matches the transcript at
  `[00:01:37]`–`[00:01:54]`.
- **Print/speech agreement on all six RSI parameters**, independently.

**No comprehension probe was run.** V10's was 12/12 and its own homework argued against
over-crediting it (same session writes answers and scorer). This session did not run one rather
than run a weak one; **the reviewer is pointed at `Q-012`, `C-018` and `BT_V11_0001` §1 as the
load-bearing evidence instead.**

### B. Recognition — **NOT SATISFIED. `D-030`-BLOCKED. Scored, not carved out. NO severity charge.**

**Seventh consecutive lesson.** V11 makes it *worse-specified*, not better, and in a new way.

The `[00:36:19]` composite — *"25 to 50 pips below the blue box **and** the TDI or RSI in the
extreme 80 to 90 range **and** it gives me the formation"* — is the most nearly complete entry
sentence in the corpus. **Every one of its three clauses is blocked**: `blue box` (`A-076`), the
RSI range (**`A-080`, new**), and *"the formation"* (`A-011`, narrowed but not closed).

`push` stays blocked. `railroad tracks` — named at `[00:14:31]` and confirmed by a second engine —
is **a new undefined pattern** and occurs nowhere else in V01–V11.

### C. Discrimination — **SATISFIED**

The lesson is built on discrimination and states its negative cases explicitly: not-a-trade is
enumerated eight times (`§2`), the M/W negative case is named (*"a tiny tap off the low"*), and
`[00:23:38]` puts a number on the rejected class — *"they're 50 50 guesses, they're 60 40."*

The **printed** `Problems that are occurring as a group` slide (frame `13:20`) is a seven-item
discrimination list in the instructor's own hand.

### D. Sequence — **SATISFIED**

`[00:38:11]`–`[00:38:26]` gives the corpus's most explicit ordered sequence, inside the indicator:
*"Level one, day one: drop, pull back, sideways consolidation, stop hunt high, drop. Safety trade
going into level two, crosses back below the market baseline."* Continued at `[00:38:26]`–
`[00:39:01]` to the level-three extreme and the expected signal.

Recorded with the caveat that the sequence is stated **in RSI space** and its price-space
counterpart is `A-083`'s open question.

### E. Exceptions — **SATISFIED**

Carried rather than dropped (`E03`): the 30-minute case is **conditional** on *railroad tracks*; the
two-hour figure is a **ceiling on a different object**; `[00:33:34]`'s *"it may or may not come back
below the 50"*; `[00:28:10]`'s explicit openness of the indicator choice (*"if it's stochastic
that's fine"*), which cuts against reading TDI as mandatory; and `[00:42:41]`'s disowning of the
RSI deck's provenance.

**Dimension E's sharpest item is `Q7` of the interpretation**: the speaker **reads his own
`POSITIVE TREND` slide and then repudiates its stage-3 semantics** — *"they call that trend
acceleration… but we know better: trend acceleration is a sucker's play."* **The printed artifact
is not doctrine here; the audio is.**

### F. Homework — **PARTIALLY SATISFIED**

`V11_HOMEWORK.md`. **Two `NOT APPLICABLE`, two `DEFERRED`, one `PERFORMED`, one `PERFORMED IN
PART`.** Dispositions are `D-019`-typed, not merged.

**The headline is an absence**: `[00:00:46]` promises *"a really good assignment coming up this
week"* and **the lesson ends 50 minutes later without giving it**, mid-sentence. **Nothing is
inferred or reconstructed.** V11 is Part 1 of a two-part session; V12 is Part 2, same date.

**H6 — the one genuinely new exercise — is `DEFERRED`, blocked by `A-080`**, because rendering any
RSI requires choosing a period. In its place a **bounded demonstration of the blocker** was run,
adopting no period, and it is the most useful thing in the homework.

### G. Manual backtesting — **SATISFIED, WITH THE LIMITATION REPORTED AT EQUAL PROMINENCE**

`PT-039` pre-registered at `beee96a` **before the runner existed and before any bar was read**;
runner at `6da82b3`; output after that. **Commit-timestamp ordering is the evidence.**

| Measure | Verdict against §6's fixed thresholds |
|---|---|
| `M1a` — does duration inform at all? | **PARTIALLY SUPPORTED** (+15.80 pp over `N1`) |
| `M1b` — does the 30→90 band do work? | **CONFIRMED AS STATED** (+12.17 pp) |
| `M1c` — are the named numbers special? | **CONTRADICTED AS STATED** — no feature at 30, none at 90, in both arms |
| `M1d` — does it survive the confound? | **PARTIALLY SUPPORTED** — 3 of 6 strata |

**Headline:** *the claim's direction is supported and its numbers are not.* `N3` shows the margin
is **monotone in remaining session time** across a factor of eight (+5.5 pp → +44.0 pp, six strata
in the right order); `N4` puts the real 17:00 boundary at the **6.40th percentile** of 1,000
arbitrary 24-hour boundaries.

**⚠ THE LIMITATION, STATED AS PROMINENTLY AS THE RESULT** (`BACKTEST_EVIDENCE_STANDARD.md` §4.3,
`E25`):

1. **Most of V11 was not tested** — the entry rule and **every one of the six printed RSI
   thresholds**, all `D-030`-blocked. `BT_V11_0001` §1 is the first section of the file for this
   reason.
2. **The tested claim was NARROWED, and the narrowing was disclosed before the run** (`PT-039` §8).
   His *"the low"* is filtered by the blue box; `A-076` blocks that, so **every** running
   session-day M1 low was tested — **26,028 of them against the ~4–9 a chart reader would mark**.
   Prediction **P6 measured that gap and I got it badly wrong (predicted 4–9, actual 26)**, which
   is **his side of the argument, not mine**, and is reported as such.
3. **A design defect was found at run time**: `D-031` Arm B loses **117 session days** because the
   DST `+1 h` shift moves the Friday close to 18:00, failing every DST-week **Monday** on the
   completeness rule. **Arm A, the pre-registered primary cell, is unaffected**, and the arms still
   agree within 1.7 pp — but this is **not** the clean robustness check `D-031` intends, and **every
   future day-boundary test in the `PT` family inherits it.**

**Prediction score: 4 of 7 substantive (P2, P5, P7, P8 right; P3, P4, P6 wrong).** The cheap `P1`
**also failed** and is still reported separately, as `PT-039` §6a required in advance.

### H. Provenance — **SATISFIED**

Every substantive row carries a timestamp and a basis tag. **No rule rests on `PRINTED` alone.**
The evidence-order disclosure in `V11_SOURCE_NOTES.md` names the three images opened before the
transcript pass finished and states that none contributed a rule.

**`Q7` makes provenance load-bearing rather than ceremonial**: this lesson contains a printed
artifact of **uncertain third-party origin** (*"maybe 15 years ago… I'm not even sure these slides
came from that guy"*) whose semantics the course author **contradicts on the record**.

### I. Ambiguity — **SATISFIED**

Four new records — **`A-080`** (RSI period), **`A-081`** (*"a 25 risk"*, no unit), **`A-082`**
(flashcards), **`A-083`** (is V11's safety-trade confirmation V10's safety trade?) — plus status
updates narrowing **`A-039`** and **`A-011`** and annotating **`A-020`**.

**`A-083` is the discipline item**: two lessons describe *"the safety trade"* in two different
panes, the merge is probably right, and it is **recorded as `DO NOT MERGE` rather than merged.**

### J. Contradictions — **SATISFIED**

**`C-018`** filed: Tier 2 (`MMM-NOTES` p.66, *"Hold the Mayo – 200 Bounce"*) + owner attestation
versus Tier 1 (V11 `[00:46:45]`, *"There's the mayonnaise. There's the 50."*).

**Filed and NOT adjudicated.** `SOURCING_HIERARCHY.md` §3.3's *"the recording wins"* **cannot close
it**, because the recording is itself two-ways readable and the same phrase *"there's the 50"*
means the **RSI baseline** seven seconds later at `[00:46:52]`. The frame at `46:45` was extracted
**specifically to arbitrate** and shows four averages with no legend — reported as a **negative
result** rather than omitted.

**No `C-xxx` was opened for `Q7`** (the slide repudiation): a speaker disagreeing with a slide *and
saying so* is the method being stated, not a conflict between two asserted claims.

---

## `SOURCING_HIERARCHY.md` §3.1 RECONCILIATION — RUN

§3.1 step 1 is mandatory **before** notes are written, and §3.4 names `A-020` as one of three
highest-priority targets for any lesson touching the moving-average set. **V11 touches it. The
check was run first and is what found `C-018`.**

| Term | Case | Outcome |
|---|---|---|
| `mayonnaise` (`A-020`) | **C — genuine conflict** | `C-018`. **Not adjudicated**; `A-020` neither reopened nor re-closed |
| `TDI` (`A-039`) | **D — clarifies without defining** | **NARROWED.** Still no period, no component periods, no band settings |
| `push` | — | **Stays BLOCKED.** Used at `[00:05:52]`, not defined |
| `A-005` / `A-078` (25–50 pips) | **B — compatible** | Corroborated four times + drawn at `07:45`. **No status change**, no new number |

---

## QUARANTINE — `Q-012`

`NOTES.md` and `VISUAL_INDEX.md` confirmed fabricated; `RULES.md` discharged by `Q-007` and its
markers re-measured anyway.

**Two findings that advance the corpus-wide pattern:**

1. **`Q-011`'s "one generator" claim reproduces on a second lesson by exact `diff`.** V11's
   `RULES.md` is **V01's file with six identifier strings swapped** — 12 differing lines, **zero
   content lines**.
2. **The one real image is the TITLE CARD**, indexed as *"Asian Box accumulation range with 5, 13,
   50, 200, and 800 EMAs."* Third confirmed instance of the sixth failure mode.

**And the register cuts both ways**: that title card prints **`Week 4`**, independently
corroborating `D-017` §2's ordering. **The description is fabricated; the pixels are evidence.**

**A measurement correction is recorded inside `Q-012` because this session made it**: a naive
`grep -ci "EMA"` returns **11** (matching *email*, *them a*), and `grep -c "9:30"` returns **3** by
matching **timestamps**. The correct method strips marker lines and uses word boundaries. **`EMA` =
0.**

---

## ⭐ V10's CARRY-FORWARD (a)–(g) — ANSWERED, ITEM BY ITEM

`COURSE_PROGRESS.md`'s `V11 GATE` block set seven items for this session. **Each was checked and
each is answered here, including the ones that came back negative.**

### (a) Speaker identification — **TESTED, NOT ASSUMED. Result: the author continues.**

The instruction was *"DO NOT ASSUME IT CONTINUES THE AUTHOR, and do not assume it reverts. TEST
IT, on non-acoustic strands fixed before the answer is known."* Four strands were fixed before the
transcript was read for content, the acoustic screen was **not** run, and the handover-language
scan returned **zero matches in 51 minutes**. **Course author, 100%, HIGH confidence.** Runtime
series is now: ~100% (V03) → ~31% (V04) → 0% (V05–V09) → **100% (V10) → 100% (V11)**.

### (b) ⭐ V10's DATE PREDICTION — **CONFIRMED, AND CONFIRMED FROM INSIDE V11**

V10's end card, **printed and never spoken**, reads *"Looks like I will have a session for Easter
Sunday… So same time next week."* Easter Sunday 2012 was **8 April 2012**, which is V11's filename
date (`Wk4 **040812**`).

**V11 corroborates it from inside the recording**, in audio V10 could not have anticipated:

> `[00:25:33]` — *"I figured it was **sunday** and it was **easter**, I figured I'd get preach on
> you guys."*

**This is the corpus's first cross-lesson, dated continuity check to be predicted in advance and
then confirmed by independent in-recording evidence.** It is a genuine, if small, validation of
`D-017` §2's ordering — which until now rested on filenames and week labels.

### (c) ⭐ *"THAT'S NEXT WEEK'S LESSON"* — **THE COMMITMENT IS KEPT, AND `A-039` STILL DOES NOT CLOSE**

V10 `[01:13:03]`: *"do we use TDI to confirm these? Yes, **that's next week's lesson my friend.**"*
The carry-forward called this *"the single most specific forward commitment the corpus has ever
carried"* and said **if V11 teaches it, `A-039` closes and a five-lesson debt discharges.**

**V11 delivers the lesson. `A-039` does NOT close. Both halves matter and the second is the
finding.**

- **Delivered:** 25 minutes, six printed slides, eight substantive points — why RSI (closes, not
  spikes), the 50 baseline, the six range parameters, the 80/40 ↔ 60/20 switch, peak formations
  read **inside** the indicator, divergence and hidden divergence. `A-039`'s standing description
  *"displayed, not taught"* is **retired**.
- **Not closed:** the lesson supplies **no RSI period** (`A-080`), **no TDI component periods**, and
  **no volatility-band settings** — and the band is used as a trigger (*"above the double band,
  below the double band is gold"*, `[00:08:03]`). Worse, `[00:32:34]` promises *"I'm going to
  explain the TDI in a minute"* and **the file ends 18 minutes later without the band or
  signal-line treatment.**

**`A-039` NARROWS — `SOURCING_HIERARCHY.md` §3.2 Case D.** The five-lesson debt is **partially**
discharged: the *reading* of the indicator is now taught; **every parameter of it remains
unstated.** `D-030` binds on the parameters, and the parameters are what a test would need.

**The honest reading is that V11 is Part 1 and the commitment may complete in V12** — the same
session, same day, 55 minutes.

### (d) `A-077` (the lock) — **CHECKED. NOT DISCHARGED. Reported as a negative.**

The watch item was: *"any lesson attaching a number to 'price has moved away and confirmed'
discharges dimension B's block, V10's deferred H2, and `PT-038`."* **V11 attaches no such number.**
It restates the entry protocol six times and the anchor distance four times, and never supplies a
real-time confirmation threshold for the lock. **`A-077` stands untouched.**

*(V11's `[00:14:31]` hold-duration claim is a real-time confirmation threshold — but for a
**candidate low**, not for the lock, and `V11_SOURCE_NOTES.md` does not conflate them.)*

### (e) `A-004` (*the level*) — **CHECKED. NOT ADVANCED.**

V11 uses `level three` **11 times** and locates levels **inside the RSI** (`[00:29:52]`, *"the
levels can actually be counted inside the indicator"*), which is suggestive and is **not a
definition** — and it is doubly blocked, because counting them inside the indicator needs
`A-080`'s period. `[00:47:31]`–`[00:49:52]` counts three touches **at a level** without ever saying
how the level is located. **`A-004` unchanged.** The carry-forward's observation that the course may
route around it rather than define it is, on V11's evidence, **strengthened**.

### (f) ⭐ `C-017` (printed-vs-spoken) — **V11 SUPPLIES TWO MORE INSTANCES, AND THEY POINT OPPOSITE WAYS**

The carry-forward records that `C-017` is the corpus's first printed-vs-spoken conflict and *"the
project has NO standing rule for that class"*, and asks for a ruling. **V11 is directly relevant
and makes the case for a ruling stronger — while also showing that a simple precedence rule would
be wrong.**

| Instance | Which medium carries more | Disposition |
|---|---|---|
| **`A-081`** — the `Trade Strong` slide prints *"I will not overleverage my account"*; the **speech adds *"I will not take a 25 risk on one trade"*** | **SPEECH is the superset** | New ambiguity; no unit stated in either medium |
| **`Q7`** — the `POSITIVE TREND` slide prints *"Begins Upside Acceleration"*; **the speaker reads it and repudiates it** — *"trend acceleration is a sucker's play"* | **SPEECH is DOCTRINE and PRINT is the rejected third-party reading** | No `C-xxx` — a speaker disagreeing *and saying so* is not two asserted claims |

**`Q7` is the important one for the owner's ruling.** The printed artifact there is **third-party
material of uncertain origin that the course author explicitly disowns** (*"maybe 15 years ago…
I'm not even sure these slides came from that guy"*). **Any standing rule of the form "print beats
speech" would adopt, as doctrine, a slide the instructor rejected on the record.** Recorded as
evidence *against* a simple precedence rule, in a lesson that also supplies a case where speech
merely adds detail.

### (g) The `SWF_CAPTURE_RECIPE.md` §10 frame rate — **READ PER FILE, AND IT VARIES IN BOTH DIRECTIONS**

The corrected §10 rule (*"read `frameRate` from the header of the file you are about to capture…
Never type a literal"*) was followed. **V11 declares `3.0`.** V10 declared `2.0`; V01/V02 declare
`3.0`. **V11 is the demonstration that the field varies in both directions**, not merely that V10
was an exception — which is a stronger justification for the corrected rule than V10 alone
provided. The patch used was `3.0 → 30.0` and the resulting sweep grid is exactly the 5-second
spacing §7 assumes.

---

## SELF-ASSESSMENT — WHERE THIS SUBMISSION IS WEAKEST

Ordered by how much it would cost if the reviewer disagrees.

1. **`C-018` may be over-cautious.** A reviewer who listens to `[00:46:45]` and finds the
   apposition intonation decisive would be entitled to say the record manufactures doubt to avoid a
   decision. **My defence is `[00:46:52]`** — a fact about the transcript, not a preference — but I
   hold it at MEDIUM and an audio judgement would be better evidence than anything I have.
2. **`PT-039` may be a strawman for the instructor's claim.** `P6`'s miss (4–9 predicted, **26**
   actual) is the measure of it. **`M1c`'s contradiction does not reach his filtered version**, and
   the mastery report must not let that caveat drift.
3. **The Arm B defect was not caught in design.** `PT-039` §5 predicted the arms would differ and
   did not anticipate *why*. It cost no verdict here, and it is a latent defect across the `PT`
   family that a more careful pre-registration would have found.
4. **I may over-credit the RSI section's completeness.** The TDI *proper* — signal line, volatility
   bands — is promised at `[00:32:34]` and **not delivered in this file**. If V12 delivers it, V11's
   RSI section is a prologue and `A-039`'s narrowing is generous.
5. **The `PT-039` numbering collision was found late** (see below). The check `D-038a` requires was
   run — against **files**, which missed two **prose** reservations.

---

## ESCALATIONS — FOR THE REVIEWER AND THE OWNER

1. ⭐ **`C-018` needs an owner adjudication** (`SOURCING_HIERARCHY.md` §3.2 Case C). **V12 is the
   cheapest route to closing it on Tier 1 evidence** — same session, same day, same charts.
2. ⭐ **`SETUP_ISSUES.md` entry for `C-018` is OWED, NOT DONE.** §3.2 Case C requires it;
   `SETUP_ISSUES.md` is a **POLICY ledger** and may not be written from a task branch (`D-038a`).
   **This must be done at integration.**

   > ### ✅ DISCHARGED 2026-08-13 — `D-041`, AND **NOT** BY WRITING THE ENTRY
   >
   > **`C-018` is CLOSED by owner adjudication** (`00_SYSTEM/DECISIONS.md` `D-041`). §3.2 Case C is
   > *"genuine conflict — do **not** adjudicate, log it, surface it to the owner."* The owner has
   > now adjudicated, so **there is no live conflict for a `SETUP_ISSUES.md` entry to describe**,
   > and the obligation is discharged rather than performed. Reasoned in `D-041` consequence 5 on
   > the integration branch, not silently skipped. **This item is closed, not abandoned.**
3. ⭐ **`PT` NUMBERING COLLISION.** `BT_V10_0001` §9, `REVIEW_INDEX.md` item 86 and `LOG.md`
   reserved **`PT-037`** (path-length) and **`PT-038`** (safety trade) in prose, with no files. This
   session allocated `PT-037` to V11's test and **ran it**. **Proposed resolution: this file keeps
   `PT-037`; V10's reservations move to `PT-039` / `PT-040`.** `BT_V10_0001` and `V10_REVIEW_R1` are
   **not edited**. **The owner or reviewer may reverse this**, in which case `PT-037` is marked
   `SUPERSEDED — NUMBERING`, re-issued, and its result retained.

   > ### ✅ RESOLVED 2026-08-13 — OWNER RULED, AND **REVERSED** THE PROPOSAL ABOVE
   >
   > ***"Move V11 not V10 since V11 is after."*** **V11's test is re-issued as `PT-039`. V10 keeps
   > `PT-039` and `PT-038`.** The paragraph above is retained unedited per
   > `REMEDIATION_PROTOCOL.md` §2 and is the history, not the current state.
   >
   > **The proposal reasoned from the artifact** (a run test should not move; a prose reservation
   > is free to). **The owner ruled on precedence** (V10 filed first, so V10 keeps its numbers).
   > The remedy this item specified in advance is exactly what was applied: `SUPERSEDED —
   > NUMBERING`, re-issued, **result retained in full**, nothing in §§1–9 of the pre-registration
   > touched, `BT_V10_0001` and `V10_REVIEW_R1` still not edited.
   >
   > **⚠ `PT-040` was NOT allocated.** The reversal was framed as *"V11 moves to 039/040"*, but
   > **V11 only ever held one number.** Every `PT-038` reference in V11's artifacts points at
   > **V10's** safety-trade reservation, which never moved. `PT-040` remains free.
   >
   > **The disclosure is what made the ruling cheap**, and this session should be credited for
   > filing it rather than quietly keeping the number.
4. **`A-080` is the binding constraint on V11 and probably on V12.** One frame showing an MT4
   indicator-properties dialog closes it and unblocks the whole RSI half of this lesson.
5. **The Arm B day-boundary defect is a `PT`-family issue**, not a V11 issue.
6. **`A-077` (the lock), `REVIEW_INDEX.md` item 89's watch item for V11+: NOT DISCHARGED.** V11
   attaches no number to *"price has moved away and confirmed"*. Recorded as checked and negative.

---

## VALIDATOR

`scripts/validate_project.py` — **103 passed / 0 warnings / 0 failures**, run before every push.

**One failure occurred and is recorded rather than hidden:** the first `BT_V11_0001` commit shipped
without the `EVIDENTIAL`/`DESCRIPTIVE` classification `BACKTEST_EVIDENCE_STANDARD.md` requires,
because the validator was run **before** the file was staged rather than after. It was caught by
the validator on the next run and fixed in the following commit, with the cause stated in the
commit message.

---

## DECISION

```text
STUDENT STATUS: REVIEW REQUIRED

A submission, not an authorization (D-016 / I-001). This session did not
review itself (D-003) and did not merge to integration -- merge-back is a
separate, single-threaded act under D-038.

NEXT: independent review R1 of V11.
```
