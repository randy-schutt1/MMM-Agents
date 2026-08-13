# V07 — INDEPENDENT REVIEW R2 (remediation verification)

| Field | Value |
|---|---|
| Lesson | V07 — *"Best Trade Grabs"* (`Bootcamp1 Wk2 032612 Part2 (48mins).swf`, 00:48:06) |
| Review round | R2 — verification of R1 items 61–63 |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent |
| Prior round | `V07_REVIEW_R1.md` — REVISE, 0 CRITICAL / 0 MAJOR / 3 MINOR |
| Remediation under review | Commit `98d893a`, branch `fix/v07-r1-minors`, merged into the integration branch at `f3f9006` |
| `D-003` separation of duties | **SATISFIED.** This session authored no V07 artifact and performed no part of the remediation. Every count below was re-derived from `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` by this session, by **two independent methods**, before the remediated text was read. Neither the R1 figures nor the remediation's claimed figures were taken on trust |
| **Review basis** | Branch **`review/v07-r2`**, cut from the integration branch at `f3f9006` after `git fetch --all` confirmed no divergence (`D-038`). The V07 content under review is **already merged**, so no worktree isolation was needed; `REVIEW_INDEX.md` and `LOG.md` are written on this branch as **evidence ledgers** per `D-038a` and merged with the finding. See §5 |
| Process disclosure | No owner directive was issued for this round. Dimension B is carried from R1 unchanged — see §4 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V07
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      1 new   (M1 — E01, co-code E20; the item-63 §H repair is
                     itself false. Three located instances)
NOTE:       2       (N1 the sweep is unreproducible; N2 the count gap)

ITEM 61 (M1):  CLOSED — VERIFIED. 56 is correct, re-derived twice.
ITEM 62 (M2):  CLOSED — VERIFIED. 5 is correct, at the five listed
               markers, re-derived twice.
ITEM 63 (M3):  PARTIALLY VERIFIED.
               - The §D half — the quotation and the citation — is
                 CLOSED, VERIFIED against the transcript.
               - The §H half — the repaired categorical claim — is
                 NOT VERIFIED. The repaired sentence asserts that
                 exactly one such quotation existed and that "no
                 other instance exists". THREE OTHERS EXIST, two of
                 them in the file the review told the remediation
                 not to edit. Carried forward as open item 70.

SUPERSEDED-TEXT CONVENTION (REMEDIATION_PROTOCOL.md §2):
               SATISFIED at all three sites. No incorrect text was
               deleted. Verified by diffing 98d893a against its
               parent line by line — every removal is matched by a
               verbatim retention in a dated block.

ADVANCEMENT:   V08 gate stays OPEN (D-024: 0 CRITICAL, 0 MAJOR — R1's
               authorization is undisturbed). V07 does NOT reach
               COMPLETE. One MINOR is owed, plus the residue of 63.
```

---

## 0. WHAT THIS REVIEWER MEASURED, AND HOW

Nothing below is taken from R1's prose, from the remediation's commit message, or from the
remediated artifacts' own say-so. The verbatim body was extracted once —
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` from the `# VERBATIM TRANSCRIPT` heading to end of file,
with the `[HH:MM:SS]` marker lines removed — and every count was then taken **twice, by two
tools that share no code**: a Python `re` word-boundary pass, and a `grep -oiE` pass.

| # | Measurement | Python | `grep` | Artifact claims | Verdict |
|---|---|---|---|---|---|
| 1 | Body size | 7,439 / 7,447 tokens¹ | **7,436 words** | §10 preamble: *"the 7,436-word verbatim body"* | **Exact** |
| 2 | `level` | 53 | 53 | 53 | **Exact** |
| 3 | `levels` | 3 | 3 | 3 | **Exact** |
| 4 | `level` + `levels` | **56** | **56** | §10 **56**, §5 **56** | **Exact** |
| 5 | `level <N>` compound (digit or word-number) | **35** | — | commit msg: 35 | **Exact** |
| 6 | Marker entries containing the token | **44** | — | commit msg: 44 | **Exact** |
| 7 | `the peak` | **5** | **5** | §10 **5×** | **Exact** |
| 8 | `peak formation` / `PFH` / `PFL` | 0 / 0 / 0 | — | 0 / 0 / 0 | **Exact, unchanged** |
| 9 | `mayo` in the body | 0 | 0 | §10 `mayo` **0** | **Exact** |

¹ The two Python figures are a punctuation-inclusive tokenizer and a whitespace split; `wc -w`
on the same extraction returns **7,436**, which is the figure the file states. The three-token
spread is tokenizer definition, not disagreement about the text.

**The transcript itself was not touched by the remediation** — `98d893a` changes four files and
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` is not among them. The measurement base is the same base
R1 measured against.

---

## 1. ITEM 61 (R1 `M1`, `E20` count class) — ✅ CLOSED, VERIFIED

**The claim under test:** §10's *level* row should read 56, not 26.

**Re-derived from scratch, ignoring both numbers.** `level` occurs **53** times and `levels`
**3** times over the verbatim body, word-boundary, case-insensitive — **56** — agreeing exactly
between the Python and `grep` passes. The two competing readings of "uses of the object" that a
writer might plausibly have meant were also measured, in case 26 was a defensible sub-count:
the `level <N>` compound form is **35** and the number of marker entries containing the token is
**44**. **26 is none of them.** R1's diagnosis holds and the remediation's is independently
correct.

**The corrected cell reads:** *"**56 uses** (`level` 53 + `levels` 3), no definition. `A-004`
untouched"*, with the correction dated and attributed to R1 item 61. **Correct.**

**The prohibitions were honoured.** §5 was **not** edited — it still reads *"level / levels
**56 times**"* — so the file's two records of the same object now agree, which is the point of
the fix. `A-004` is untouched in `AUTOMATION_AMBIGUITIES.md`. The row's conclusion (*level* is
used constantly and never defined) is unchanged and, as R1 said, was understated by the wrong
number rather than overstated.

---

## 2. ITEM 62 (R1 `M2`, same class) — ✅ CLOSED, VERIFIED

**The claim under test:** §10's *"the peak"* row should read 5×, not 4×.

**Re-derived from scratch.** The string *"the peak"* occurs **5** times, both methods agreeing,
and this reviewer enumerated the occurrences rather than only counting them:

| Marker | Sentence |
|---|---|
| `[00:00:26]` | *"Second leg trading away from the peak."* |
| `[00:03:18]` | *"Second leg here, trading away from the peak."* |
| `[00:03:20]` | *"That would have been on this third day of trading away from the peak, and it dropped nicely."* |
| `[00:14:02]` | *"The peak was here at level three and this was level one."* |
| `[00:16:44]` | *"I'm trading away from the peak."* |

**Those are exactly the five markers the row already listed**, in the order it listed them. A
separate sweep for the bare token `peak`/`peaks` returns the **same five hits and no others**,
so there is no sixth use hiding behind a different article. `peak formation`, `PFH` and `PFL` are
**0**, unchanged and correct.

**The corrected cell reads 5×, the marker list is unchanged.** **Correct.**

---

## 3. ITEM 63 (R1 `M3`, `E01` + co-code `E11`) — ⚠️ PARTIALLY VERIFIED

R1 required two things in one edit. They do not verify alike.

### 3a. The §D quotation and citation — ✅ CLOSED, VERIFIED

Read directly from the transcript, at the markers rather than from any artifact:

```text
[00:28:28]  We'll say whether it's something that you will take.
[00:28:31]  If it doesn't do what you expect in your flashcard isn't the same,
            you may just decide to pass on it.
```

- **The word is `in`.** The remediated §D cell reads *"If it doesn't do what you expect **in**
  your flashcard isn't the same"* — literal, including the capital *If* the transcript carries.
  **Correct.**
- **The marker is `[00:28:31]`.** The remediated cell cites `[00:28:31]`. **Correct.**
- **`[00:28:28]` exists and carries a different sentence**, exactly as both R1 and the
  remediation state. Confirmed above. The original citation was wrong, not merely imprecise.
- **`V07_SOURCE_NOTES.md` §6c was not edited** — it still renders the passage correctly, with
  *"in your flashcard"*, inside the `[00:28:02]`–`[00:28:31]` block quote. The prohibition was
  honoured.

This half is correct in every particular.

### 3b. The §H repair — ❌ NOT VERIFIED. It is the finding of this round

R1 required that §H's categorical sentence be **repaired or scoped**, because the M3 defect
falsified it. The remediation chose to **repair** rather than scope, and said so explicitly — it
re-asserted a clean categorical claim on the strength of a fresh sweep it ran itself. §H now
reads:

> **"One quotation in the V07 set contained a word that is not in the source. It was found at
> R1, it is corrected, and no other instance exists."** Four editorial reconstructions —
> *"it's met"*, *"the 15 minute"*, *"mayo"*, the 13/50/200 reading — were moved **outside** the
> quotes and labelled as inferred or as the second ASR pass.

**Both sentences are false.** This reviewer ran its own sweep — see §6 for the method — and then
hand-checked the flagged fragments against the transcript. **Three further instances exist**, and
two of them are the very reconstructions the second sentence names as having been moved outside
the quotes.

#### Instance (a) — `V07_SOURCE_NOTES.md` §9a, marker-cited, the strongest of the three

> **`[00:27:24]` is the first time a NICKNAME is attached to a TIMEFRAME**: *"30 minute of the
> water, 30 minute of the mayo."*

`[00:27:24]` reads, literally:

```text
The dashed ones like this are 30 minute versions, 30 minute of the water,
30 minute of the male,
```

**The source word is *male*. *mayo* is not in the V07 body at all** — this reviewer measured it
at **0** occurrences, and **§10 of the same file states `mayo` 0 and says the audio only garbles
it to *mail*/*male***. So the file asserts, fourteen sections apart, both that *mayo* never
occurs in V07 and that the presenter said it at `[00:27:24]`. **This is the M1 pattern of R1 —
one file holding a right record and a wrong record for the same object — recurring in the same
file, in the same remediation round, uncaught.**

It is also `E11`-adjacent in the same way M3 was: the substituted word is carried at a live V07
marker, so a later session reading §9a has no signal that it is reading a reconstruction.

**The correct practice exists ten lines above it.** §9's evidence table renders the same
sentence properly:

> `[00:27:24]` | *"…30 minute of the water, 30 minute of the **male**,"* — *"male"* is the ASR's
> rendering of **"mayo"** (`A-020`, settled by print in V04/V06)

— quotation literal, reconstruction outside the quotes, provenance named. **§9a is the same
session's narrative restatement of §9's table cell, with the reconstruction silently promoted
into the quotation marks.** That is `N5`'s class from V04 R1, named again at V05 `M3` and again
at V07 `M3`: *quotations in narrative prose are less reliable than quotations in evidence
tables.* Fourth instance.

#### Instance (b) — `V07_SOURCE_NOTES.md` §11, the `[00:25:26]` row

> | **`[00:25:26]`'s unrecovered word** | … The flag flips when today's range reaches the ADR
> value — which is *"it turns red when it's met"*. …

`[00:25:26]` reads: *"That brown line there is the ADR. It turns red when **Beth**."* The word
*met* is not in the source; it is the reconstruction. The row's own label — *"'s unrecovered
word"* — states that the word was never recovered, and then the cell quotes a recovered version
of it. **Same cell, self-contradicting.**

#### Instance (c) — `04_SCREENSHOTS/V07/INDEX.md`, "what the frames add", item 6

> 6. **The full ADR indicator readout in two states** (`Reached= No` / `Reached= Yes`), which
>    mechanises *"it turns red when it's met"*.

Same substitution, unbracketed, no adjacent marker. **The correct practice again exists in the
same file**: row 15 of the frame table writes *"That brown line there is the ADR. It turns red
when **[it's met]**"* — brackets marking the editorial insertion, which is the project's
convention and is unimpeachable. Item 6 drops the brackets.

#### Disposition

**Charged as one `MINOR`, `M1`, `E01` with co-code `E20`** — one falsified categorical claim,
three located instances, all the same class. Not three charges: they are one defect in the
discipline of a single sweep.

**Materiality to any conclusion: none, and this is stated as plainly as R1 stated it for M3.**
`A-020` is not moved — the record's whole point is that no period is ever attached to *water* or
*mayo*, and that survives. §10's `mayo` **0** row is correct and stays. The ADR observation in
§11 and `INDEX.md` is an observation about an indicator's display, correctly fenced as not a
course rule in both places, and it does not turn on the word. **No number, verdict, or audit
trail is touched.**

**Why it is charged anyway.** R1 charged M3 for exactly one reason: a categorical
self-certification that a later session will rely on **instead of re-checking** must be true.
The remediation understood that — it is why it repaired rather than scoped, and it said so:
*"A categorical claim that is 238/239 true must be repaired or scoped, not left standing, because
a later session will rely on it rather than re-checking."* **That reasoning is correct and it
now applies to the repair.** The repaired sentence is a stronger claim than the one it replaced
(it asserts completeness of a search, not just a count), it is wrong, and it is wrong about the
specific words it names.

**Required correction is in §7.**

### 3c. The `N2` fold-in — verified as accurate, and it was the right call

R1 directed that §H's stale *"163 citations"* be folded into whichever edit next touched §H
rather than chased separately. It was. §H now records 163 as **true-when-measured and now stale**,
names the cause (§9b was appended after the sweep ran, in response to probe `R11`'s failure), and
gives current figures. Spot-checked: §9b does exist, does postdate the sweep, does carry its own
citations, and `R11` is still **failing** in the committed tree as R1 required. The 163 figure is
left in place as the record of what the pre-commit sweep covered, which is the correct handling.

---

## 4. THE SUPERSEDED-TEXT CONVENTION — ✅ SATISFIED AT ALL THREE SITES

Verified by reading `git diff 98d893a^ 98d893a` in full, not by reading the remediation's
description of it. **`REMEDIATION_PROTOCOL.md` §2 requires that old, invalid text is marked and
retained, not deleted.**

| Site | Removed | Retained where | Verdict |
|---|---|---|---|
| `V07_SOURCE_NOTES.md` §10, *level* row | *"26 uses, no definition. `A-004` untouched"* | Block quote beneath the table, dated 2026-08-13, naming round R1, open item 61 and finding `M1`, quoting the old cell **verbatim** | ✅ |
| `V07_SOURCE_NOTES.md` §10, *"the peak"* row | *"used 4× as a location (…)"* | Same block, naming item 62 and `M2`, old wording quoted | ✅ |
| `V07_MASTERY_REPORT.md` §D, Invalidates cell | *"if it doesn't do what you expect **and** your flashcard isn't the same"* (`[00:28:28]`) | Block quote immediately beneath the table, both defects itemized, old wording and old marker both quoted | ✅ |
| `V07_MASTERY_REPORT.md` §H, categorical sentence | *"No quotation mark in any V07 artifact contains a word that is not in the source."* | Block quote beneath the replacement, old sentence quoted verbatim and explicitly labelled false | ✅ |
| `REVIEW_INDEX.md` STATUS block | prior `IN REMEDIATION` / `AWAITING REVIEW` text | Superseded-STATUS block quote, appended above the pre-existing chain | ✅ |

**Line accounting:** 21 lines deleted across the four files, and every deletion is reproduced
verbatim inside a retention block. **No incorrect text was silently removed anywhere in the
commit.** The convention is followed better than the minimum — each block names the round, the
open item and the finding code, which is more than §2 asks for.

**One consequence the remediation anticipated correctly and this reviewer confirms:** re-running
any quote sweep over the current tree returns a *higher* raw count than over the pre-remediation
tree, because the retention blocks re-quote the defective renderings on purpose. Measured:
**238 → 252** marker-cited fragments under this reviewer's own definition, a delta of 14, all of
it retention text. **Expected, not a regression** — exactly as §H says.

---

## 5. DIMENSION B, AND WHAT THIS ROUND DOES NOT RE-OPEN

**Dimension B is carried from R1 unchanged: NOT SATISFIED, blocked by `D-030`, structural, not
attributable to the student, carrying NO severity charge.** No owner directive was issued for
this round either, so R1's reasoning stands as written and is not re-litigated here.

`REVIEW_INDEX.md` **open item 36** — the `EXCLUDED BY DECISION` vocabulary — is now owed for the
**fifth** lesson-round running (V05 R1, V06 R1/R2, V07 R1, V08 R1, and here). It is not a gate
and it is not the student's to fix. **It is restated, not re-argued.**

**Deliberately not re-done, per R1 §15's prohibitions, all of which the remediation honoured:**
`PT-033`, the sensitivity, the cross-check and the homework scripts were not re-run (R1 already
reproduced them bit-exactly and forbade repetition); no git history was rewritten for `I-009`;
`R11` is still failing in the committed tree, verified; `V07_SOURCE_NOTES.md` §6c is untouched,
verified. **Every "do not do this" in R1 §15 was obeyed.** That is worth recording — the
remediation's discipline about scope was good, and the defect found here is a defect of a
*sweep*, not of scope.

---

## 6. NOTES

### `N1` — the sweep that earned the repaired claim is not reproducible

`98d893a` changes four files. **No sweep script is among them.** §H asserts a mechanical sweep
over seven artifacts returning 167 marker-cited quotes and nine hand-cleared flags, and none of
it can be re-run. In a project whose `BACKTEST_EVIDENCE_STANDARD.md` requires committed,
re-runnable evidence for numeric claims, and whose homework scripts are all committed precisely
so a reviewer can re-execute them, **a load-bearing count produced by an uncommitted throwaway is
an evidence gap** — and it is the gap through which the three instances in §3b passed.

This reviewer's own sweep is described here so that it *is* reproducible: extract the verbatim
body, strip marker lines, normalize both sides (lowercase, straighten quotes, collapse
non-alphanumerics to spaces), then take every `*"…"*` fragment across the seven V07 artifacts
that has a `[HH:MM:SS]` citation within 120 characters and require a normalized substring match,
splitting on explicit `…` elisions. **Flags are not findings** — every flag was then read by hand
in context, and the great majority are correctly-labelled `PRINTED` slide and chart text, student
chat read aloud, labelled V04 markers, or bracketed editorial insertions, none of which are
defects. The three in §3b are what survived that reading.

**Not a required correction.** Committing the script would be an improvement; R1 did not ask for
it and this round will not invent an obligation. It is recorded so `CUMULATIVE_25.md` can decide
whether "a numeric claim asserted in an artifact must be produced by committed code" should
become a standing rule.

### `N2` — the 167 / 238 / 239 gap is itself informative

Three sweeps of the same corpus returned three counts: R1's **239**, the remediation's **167**,
this reviewer's **238** (pre-remediation tree, so directly comparable to R1's 239). R1 and this
session agree to within one fragment under independently written matchers; **the remediation's
number is 30% lower than either**, which means its sweep was capturing a materially smaller set
than it believed and than §H's wording implies.

One candidate mechanism, tested rather than asserted: a `\*"(.+?)"\*` pattern **without**
`DOTALL` returns 164 fragments over `V07_SOURCE_NOTES.md` and **does not capture the §9a
quotation**, because that quotation wraps across a Markdown line break; the same pattern **with**
`DOTALL` returns 180 and does capture it. Instance (a) is line-wrapped. Instances (b) and (c) sit
further than a short window from their nearest marker. **This is a candidate, not a
determination** — without the script (`N1`) the actual cause cannot be established, which is the
point of `N1`.

---

## 7. REQUIRED CORRECTIONS

One, documentation only. **It does not hold the V08 gate** (`D-024`: 0 CRITICAL, 0 MAJOR — R1's
advancement authorization is undisturbed). It **does** hold V07 short of `COMPLETE`.

1. **`V07_MASTERY_REPORT.md` §H** — the repaired categorical claim is false and must be corrected
   with the superseded text retained per `REMEDIATION_PROTOCOL.md` §2. Both sentences are in
   scope: *"no other instance exists"*, and the list asserting that *"it's met"* and *"mayo"*
   *"were moved **outside** the quotes"*. **In the same edit**, fix the three instances at their
   sites:
   - **`V07_SOURCE_NOTES.md` §9a** — restore `[00:27:24]`'s quotation to the transcript's literal
     *"30 minute of the water, 30 minute of the male,"* and move *mayo* outside the quotation
     marks with its `A-020` provenance, as §9's table already does ten lines above.
   - **`V07_SOURCE_NOTES.md` §11**, the `[00:25:26]` row — take *met* out of the quotation marks,
     or bracket it as `[it's met]`, matching `INDEX.md` row 15.
   - **`04_SCREENSHOTS/V07/INDEX.md`**, "what the frames add" item 6 — same, and bracket it to
     match row 15 of its own frame table.

   **`V07_SOURCE_NOTES.md` §10's `mayo` 0 row is correct and must not be changed.** `A-020` must
   not be moved — no conclusion in this finding disturbs it. §9's evidence table and `INDEX.md`
   row 15 are **correct as written and must not be edited**; they are the model the three
   defective sites should be brought into line with. *(R2 `M1`)*

**Explicitly NOT required — do not do these:**

- **Do not re-run any V07 script, homework, backtest or probe.** R1 reproduced them bit-exactly
  and forbade repetition; nothing in this round touches them.
- **Do not re-open items 61 or 62.** They are verified closed. §10's *level* and *"the peak"*
  cells are correct and must not be edited again.
- **Do not edit `V07_SOURCE_NOTES.md` §6c or §5.** Both are correct; both were correctly left
  alone by the last remediation.
- **Do not "fix" `R11`.** It must stay failing.
- **Do not rewrite git history**, for `I-009` or for anything else.
- **Do not delete the retention blocks** added by `98d893a`, including the ones that re-quote
  defective text. They are the audit trail (§4) and their raw-count effect is expected.

---

## 8. DECISION

Two of the three items verify cleanly, by two independent methods, against the primary source.
The count-class fixes (61, 62) are exactly right, the prohibited edits were not made, and the
superseded-text convention was followed at every site — better than the minimum, since each
retention block names its round, item and finding code. The §D quotation and citation are
literal and correct. The scope discipline was good throughout: every "do not do this" in R1 §15
was obeyed.

What failed is narrower and more interesting than a missed fix. The remediation was **asked** to
repair *or* scope a categorical claim; it chose the harder option, said explicitly that it would
not take the reviewer's count on trust, ran its own sweep, and re-asserted the claim on that
basis. **That instinct was right, and its execution left three instances standing** — two of them
in a file the remediation correctly did not edit, one of them in the very section that already
renders the same sentence properly ten lines above. A categorical claim was replaced by a
different, stronger categorical claim, and it is also false.

**No conclusion, number, verdict or audit trail moves.** The defect is exactly what R1's M3 was:
a self-certification that a later session would rely on instead of re-checking.

```text
LESSON: V07
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES: none

MAJOR ISSUES: none

VERIFIED CLOSED: items 61, 62 — and the §D half of item 63.

REQUIRED ACTIONS:
1. V07_MASTERY_REPORT.md §H — correct the repaired categorical claim
   ("no other instance exists", and the "moved outside the quotes"
   list), retaining superseded text. In the same edit, fix the three
   instances: V07_SOURCE_NOTES.md §9a ([00:27:24] "male", not "mayo"),
   V07_SOURCE_NOTES.md §11 ([00:25:26] "it's met"), and
   04_SCREENSHOTS/V07/INDEX.md item 6 (same). Do NOT edit §9's table,
   §10's mayo row, §5, §6c, or INDEX.md row 15 — all are correct.

ADVANCEMENT:
V08 gate remains OPEN — R1's D-024 authorization is undisturbed and
nothing found here is CRITICAL or MAJOR. V07 does NOT reach COMPLETE:
open item 70 is owed, and item 63 stays open until 70 discharges.

OWNER RULING OWED: REVIEW_INDEX.md open item 36 (dimension B
vocabulary), FIFTH lesson-round running. Not a gate.
```

---

## 9. LOGGING

`REVIEW_INDEX.md`: decision row (V07 R2 REVISE 0/0/1); items **61** and **62** → ✅ **CLOSED —
VERIFIED at R2**; item **63** → ⚠️ **PARTIALLY VERIFIED** (§D half closed, §H half not), stays
open until item 70 discharges; new open item **70** for R2 `M1`; `E01` and `E20` ledger rows
updated; STATUS block updated with its superseded text retained. `LOG.md`: reviewer R2 entry.

**Next review trigger:** remediation of item 70, then **R3**.

**For `CUMULATIVE_25.md`:** the `E20` count class is now verified-closed twice in V07 and is not
recurring here — record that. The live pattern this round adds is different and worth naming
separately: **a remediation's own re-verification sweep, run to earn back a categorical claim,
missed instances the claim then denied.** Together with `N1` (the sweep is uncommitted) this is
the argument for a standing rule that a numeric or categorical claim asserted in an artifact must
be produced by committed, re-runnable code. Also carry the fourth instance of V04 R1's `N5`
class — narrative prose restating an evidence table and losing its quotation discipline in the
restatement.
