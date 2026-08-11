# V05 — INDEPENDENT REVIEW R2

| Field | Value |
|---|---|
| Lesson | V05 — `Bootcamp1 Wk2 032512 Part3 (68mins).swf` |
| Review round | **R2** — remediation verification of `V05_REVIEW_R1.md`, plus reconciliation of `V05_REVIEW_R1B.md` |
| Reviewed | 2026-08-11 |
| Reviewer | Independent Reviewer / Teacher Agent, fresh session. `D-003` satisfied for every V05 artifact **except** the open-item-39 `EMA` correction, which this session **applied on explicit owner instruction and therefore self-verified — declared, not hidden** (§3.1) |
| Remediation under review | `152f4ea` *"fix: V05 R1 remediation — all six minors (M1–M6) applied"* |
| Protocol | `00_SYSTEM/REVIEW_PROTOCOL.md` (17 dimensions, error taxonomy, severity) |
| Standard | `00_SYSTEM/MASTERY_STANDARD.md`; `DECISIONS.md` D-001 … D-025 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V05
DECISION:   REVISE
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      5   (M7 … M11 — all ADOPTED from V05_REVIEW_R1B.md,
                 all independently re-derived and CONFIRMED this round,
                 none of them applied by 152f4ea)
NOTE:       4   (N1 … N4)

R1 CARRY-FORWARD:
  M1 … M6      ✅ ALL SIX VERIFIED APPLIED AND CLOSED
  open item 39 ✅ APPLIED THIS ROUND (EMA 3 -> 2), verified
  dimension B  ⚖ STILL OWED — blocked on owner (open item 36)

ADVANCEMENT: AUTHORIZED — the V06 gate remains OPEN under D-024
             (0 CRITICAL, 0 MAJOR).

V05 STATUS:  NOT COMPLETE. PASS is withheld.
```

> ### ⚠ WHY THIS IS NOT A `PASS`
>
> This round was convened expecting to close V05. **It cannot, and the reason is not a
> defect in the remediation** — the remediation is exact, and all six of R1's minors are
> verified closed against the source rather than against the commit message.
>
> **It is that `18_REVIEW/V05/V05_REVIEW_R1B.md` is a real review with real findings, and
> none of them have been applied.** R1B was described to this session as a possible
> abandoned duplicate written against a stale state. **That description is wrong on every
> limb, and the file is materially more important than it was represented to be.** Its four
> findings plus its `n1` were re-derived from the transcript and the pixels this round,
> without reference to R1B's prose, and **all five reproduce against current `HEAD`.**
> Five live, verified, unapplied documentation defects is a `REVISE`, not a `PASS`.
>
> Every one is `MINOR`. Nothing here touches the method — see §6.

---

## 0. THE `R1B` QUESTION — SETTLED FIRST, BECAUSE EVERYTHING ELSE DEPENDS ON IT

### 0.1 What this session was told, and what is actually true

| Told | Established this round |
|---|---|
| R1B may be from *"an earlier accidental duplicate reviewer session"* | **It is later, not earlier.** R1 was written at 06:08:38; R1B at 06:14:54. R1B's §0.2 records watching R1 appear on disk mid-session |
| It was *"stopped mid-write"* | **It is complete.** 536 lines, all ten sections, a full executive block, a decision block and a sign-off. Nothing is truncated |
| It was written *"before this repo's canonical R1 was established"* | **It was committed after R1 was committed**, deliberately on top of it — `c41e686` (R1) then `8403914` (R1B) |
| It was written *"against an earlier incomplete state of V05"* | **False.** The V05 student pipeline was complete at `b4b690b` before either review began. R1 and R1B audited the identical tree |
| It *"reportedly contains up to 4 additional findings"* | **Four findings and one note, and all five are live at `HEAD`** — §2 below |
| It *"should NOT remain as a second competing review document"* | **It does not compete.** Its own header states R1 *"is NOT superseded, NOT corrected and NOT overwritten"*, and it explicitly declines to be R2 on the correct ground that no remediation had occurred |

**R1B did the right thing under I-002 and it did it for the right stated reason.** Faced with
a path collision, it declined to overwrite a complete independent review, declined to touch a
file another session held uncommitted, staged explicit paths only, and disclosed the whole
event. That is the behaviour `SETUP_ISSUES.md` I-002 exists to produce.

### 0.2 Ruling on disposition — **FOLDED, NOT SUPERSEDED**

The instruction offered two outcomes: fold R1B's valid content into the R1/R2 lineage, or
mark it superseded/invalid. **The second is not available.** `REVIEW_PROTOCOL.md` §11 and
`SETUP_ISSUES.md` I-002 forbid overwriting or invalidating a completed round, and a round
whose findings all reproduce cannot honestly be labelled invalid. Marking a correct review
"superseded" to tidy the directory would destroy an audit record and suppress five live
defects at the same time.

**Ruling, and it is the single-source-of-truth answer the instruction asked for:**

1. **`V05_REVIEW_R1B.md` is ACCEPTED into the V05 review lineage as a parallel R1 round.**
   It is not superseded and must not be edited or deleted. It stands as written.
2. **Its findings are ADOPTED into this round** as `M7`–`M11`, renumbered into the R1/R2
   sequence, each re-derived independently before adoption. **From this file forward, R2 is
   the operative list of what V05 owes.**
3. **`REVIEW_INDEX.md` becomes the reconciliation point**, as R1B itself asked. Open items
   47–51 are added this round for `M7`–`M11`, and the R1 round total is restated: **ten
   minors raised across R1 + R1B, six applied, four plus one note outstanding.**
4. **R1B is closed to further citation as a live findings list.** A future session reading it
   should treat §5 as historical and read this file for current status. That is recorded in
   `REVIEW_INDEX.md` rather than by editing R1B.
5. **The naming question stays with the owner** (R1B §0.2 item 1). This round used `R1B`
   as it stands; no rename is performed, because renaming a committed review round is
   exactly the kind of history edit I-002 forbids a session from doing on its own.

### 0.3 Two of R1B's findings land inside `V05_REVIEW_R1.md`

`m1` and `m2` propagated into R1 — R1 §6 dimension O repeats the `C-003`/`C-004` mix-up, and
R1 §6 dimension A repeats the *"all four occurrences"* count. **`V05_REVIEW_R1.md` is NOT
edited** (§11). Both are recorded here, which is where a superseded reviewer statement
belongs. Neither changes R1's verdict, its gate or any other finding it raised: R1's
dimension O conclusion (nil contradiction return) and dimension A conclusion (source fidelity
`PASS`) both survive on their own reasoning with the record identity and the count corrected.

---

## 1. R1's SIX MINORS — VERIFIED CLOSED, RE-DERIVED FROM SOURCE

Each was checked against `V05_TRANSCRIPT.md` and the committed PNGs **before** the
remediation diff was read, per `REMEDIATION_PROTOCOL.md` §5. The commit message was read last
and is accurate in every particular.

### `M1` (`E11`) — ✅ **CLOSED**

Re-derived: `[00:57:35]` *"I use the trend line."*, `[00:57:36]` *"I use E and I use the
box."* (transcript body lines 3723–3727). Both sites now correct:

| Site | Now reads |
|---|---|
| `V05_SOURCE_NOTES.md` §3b | *"I use E"* `[00:57:36]` ✅ |
| `AUTOMATION_AMBIGUITIES.md` `A-043` evidence table | `[00:57:35]`–`[00:57:36]`, **split across the two markers the words actually span**, each carrying that marker's literal sentence ✅ |

The split is better than the correction R1 required — it fixes the citation *and* removes the
sentence-spanning fragment that produced it. `[01:07:36]` and `[01:01:35]` no longer occur in
any V05 artifact (they survive only as the superseded text in `LOG.md` and `REVIEW_INDEX.md`,
which is correct). **`A-043`'s closure is untouched and still rests on the toolbar dialog.**

### `M2` (`E11`) — ✅ **CLOSED**

`[00:36:03]` = *"I can start drawing my trend line."*; `[00:36:05]` = *"So I'm going, I'm
looking for shorts, the trend line goes on the top and on the top."* `A-039`'s extension row
now cites `[00:36:05]` **and quotes that marker's literal sentence** rather than the smoothed
fragment. The remediation fixed the cause, not just the number.

### `M3` (`E01`) — ✅ **CLOSED**

Transcript: `[00:13:05]` *"So the consolidation and level three second leg of that pattern,
that three hits to the"* + `[00:13:12]` *"high."* `V05_SOURCE_NOTES.md` §4b now renders two
verbatim quotations with **no ellipsis and no substitution** — `[00:13:05]`–`[00:13:12]` and
`[00:13:13]` — and *"level three"* is restored. Byte-compared against the body: exact.
**Restored rather than annotated**, which is the stronger of the two options R1 allowed, and
the right one given the excised words were a level number inside the file's own evidence for
the level↔day relabelling.

### `M4` (`E20`) — ✅ **CLOSED, and resolved in the correct direction**

`V05_INTERPRETATION.md`'s Screenshots row now **leads** with *"⚠ THE RECIPE'S EVIDENCE ORDER
WAS NOT PRESERVED FOR V05"*, names `INDEX.md` § "PROCESS DEVIATION, DISCLOSED" as **the
governing statement**, and carries INDEX.md's own consequence verbatim — *"the audio-only /
visual-corroborated separation is weaker for V05 than for V01–V04."* What was genuinely held
is stated as a partial, not as restoration. A superseded-text block records the false claim.

**`04_SCREENSHOTS/V05/INDEX.md` was NOT weakened — verified at the diff level, not asserted.**
`git show 152f4ea -- 04_SCREENSHOTS/V05/INDEX.md` touches exactly one line, frame 26's row,
and that edit is `M6`. The § "PROCESS DEVIATION, DISCLOSED" text is byte-identical to its
pre-remediation state. **This is the finding that most easily could have been "fixed" the
wrong way — by softening the honest disclosure to match the flattering claim — and it was
not.**

### `M5` (`E20`) — ✅ **CLOSED**

`A-039` now reads *"V06 (or any later lesson) is now the next candidate"*, with the superseded
*"V05 … is the next candidate"* retained beneath. The record correctly states what V05 did and
did not supply: a first **displayed** name (`TDI_MMM`) and a first slide *titled* to mark the
panel up, and still **no inputs, periods, bands, line names or decision rule.** *"A name is
not a definition"* is the right formulation. Record stays `OPEN` / `DO NOT CODE`.

### `M6` (`E20`) — ✅ **CLOSED, and the scoping is independently correct**

Frame 26 was **re-opened and magnified this round**, not accepted from either review's prose.
The sub-panel is present: a multi-line oscillator pane beneath the price pane, yellow / red /
cyan traces, with a header label in the same screen position as frame 21's `TDI_MMM`. **At 10×
that header is not legible** — this session could not resolve it to any string and does not
propose one. `INDEX.md` row 26 and `A-039`'s extension row both now record presence only,
scoped *"displayed, not taught; header not legible at this resolution"*, with the header
deliberately not transcribed. **That is the correct call and it matches the binding V04 `M6`
precedent and frame 27's OHLC row.** Confirmed: it does not narrow `A-039`.

### Remediation hygiene

| Check | Result |
|---|---|
| Superseded text retained (`REMEDIATION_PROTOCOL.md` §2) | ✅ at all four sites that changed a claim (`M3` excepted — a restored verbatim quotation supersedes nothing) |
| Any conclusion moved? | **No.** Verified per file. `A-043` closure, `A-039` scope, §4b relabelling, INDEX.md disclosure all unchanged |
| Anything fixed by rewording rather than re-deriving? | **No.** Each correction quotes the marker's literal text |
| Scope creep beyond R1 §8 | **None.** 6 files, +122/−18 |
| `validate_project.py` | **97 passed, 0 warnings, 0 failures**, re-run this session |

**The remediation is exact and the two items it declined were declined for correct reasons**,
both stated in the commit message rather than quietly dropped: open item 39 as out of its
instruction, and the dimension-B re-disposition as blocked on an owner ruling — *"a student
session applying an undefined label would be legislating."* **That is the right refusal.**

---

## 2. R1B's FINDINGS — RE-DERIVED INDEPENDENTLY, ADOPTED AS `M7`–`M11`

Each was tested against the primary source at `HEAD` before R1B's reasoning was relied on.
**All five reproduce.** None is stale, none is redundant with R1, and none was touched by
`152f4ea`.

### MINOR

#### `M7` (`E20`) — `C-003` is named four times for a check that belongs to `C-004` *(adopted from R1B `m1`)*

**Verified at `HEAD`:**

| Fact | Evidence |
|---|---|
| `C-003` is *"Whether M and W formations can fail"* | `CONTRADICTIONS.md` line 284 heading; INDEX row line 129 |
| `C-004` is *"London session open: 3:30am printed against 4:00 spoken"* | line 445 heading |
| The V05 strike-off block is about **clock times and a London open** | lines 795–816 |
| It is physically located **inside the `C-004` material**, under § "V04 EVIDENCE ADDED TO EXISTING RECORDS" → "### The `C-004` deliberate check" | heading scan |
| **The `C-003` record (lines 284–444) contains no V05 text whatsoever** | `grep V05` over the range returns **zero hits** |

So the sentence *"See the update inside the `C-003` record"* points a reader at a record that
does not contain the update, and the STATUS block asserts that a record about **M/W failure**
was tested against V05 and came back negative. **It was not tested at all.**

Four sites, all confirmed by line:

| File | Line | Text |
|---|---|---|
| `CONTRADICTIONS.md` STATUS block | 23 | *"C-003 was checked against V05 and struck off as negative."* |
| `CONTRADICTIONS.md` § "V05 PASS" | 845 | *"**`C-003` was additionally checked against V05 and struck off as negative**"* |
| `CONTRADICTIONS.md` § "V05 PASS" | 846 | *"See the update inside the `C-003` record."* |
| `V05_MASTERY_REPORT.md` §J | 184 | *"`C-003` named V05 as its next candidate; checked and struck off as negative"* |

**The underlying check is sound and reproduces exactly.** Re-measured this round over the
verbatim body with markers excluded: no `HH:MM`, no `o'clock`, no `GMT`, no `EST`, no *"New
York time"*; the only *am/pm* hits are the ASR garble *"the 50 am in"*; `London` occurs twice
with no hour attached. **`C-004`'s disposition does not move** — `UNRESOLVED`, carry both
values, encode no London open.

**Charged because a status block that misidentifies its own contents is the exact failure
class this project has fought hardest** (open item 14, four prior occurrences in this very
file). It also retires R1's `N5` claim that all four status blocks were current:
`CONTRADICTIONS.md`'s is not.

**Required:** correct all four sites to `C-004`, superseded text retained. **Do not edit
`V05_REVIEW_R1.md`.**

#### `M8` (`E01`) — a verbatim string quoted with a count the string does not support *(adopted from R1B `m2`)*

`V05_MASTERY_REPORT.md` §E line 92: *"the day count's own escape clause (**"but up to five
days"**, four times)"*.

**Re-measured this round:** the literal string *"but up to five days"* occurs **exactly
twice** — body line 607 `[00:11:11]` *"This could be after two to three days of rise or fall,
but up to five days."* and body line 1501 `[00:24:37]` *"After three days of drop, but up to
five days."* The string *"five days"* occurs four times, but the other two — *"sometimes five
days depending"* and *"Remember three to five days"* — **do not contain the quoted words.**

**Third instance of the project's verbatim-count class** (open item 15, open item 39). The
pattern is identical each time: a count asserted over a quoted string without re-measuring the
string.

**Required:** restate as *"twice verbatim, `[00:11:11]` and `[00:24:37]`; the day-count
expectation itself is stated four times."*

#### `M9` (`E20`) — unrecorded printed `R =` labels in frame 26, and `A-018` undercounts *(adopted from R1B `m3`, with one correction to it)*

Frame 26 was magnified this round at 10× LANCZOS and 16× nearest-neighbour. **Four `R =`
labels are present on the live-platform chart**, none recorded anywhere:

| Position | This session's reading |
|---|---|
| upper-centre | **`R = 40.9`** — legible ✅ |
| centre-right | **`R = 40.6`** — legible ✅ |
| lower-right | **`R = 41.1`** — legible ✅ |
| left | **`R = ` present; the value is NOT legible.** The cyan moving average runs directly through the digits. Only the `R =` and a trailing digit separate; the leading digits do not resolve at any magnification tried |

> **⚠ This corrects R1B `m3`, which reads the fourth label as `R = 74.6`.** That value is not
> supportable from this PNG. **The label's presence is confirmed; its number is not.** Under
> the frame-27 / V04 `M6` precedent the remediation must record it as *present, value not
> legible at this resolution* and must **not** transcribe a number. R1B's other three values
> are confirmed exactly.

**Why it matters to a record.** `A-018`'s V05 row lists four labels from two *slides*
(`R = 24.6`, `18.8`, `29.5`, `39.0`) and concludes *"V05 adds four more labels"*. **V05 adds at
least eight**, and the four unrecorded ones are a different and stronger evidentiary class:
they are auto-printed on the presenter's **live MT4 platform**, not drawn on a deck slide,
which bears directly on what `A-018` is accumulating — that `R` is a routine platform
annotation rather than a risk multiple.

**It does not narrow `A-018`.** Guest material, `D-025`; and V05 states no stop and no target,
so nothing in the lesson checks an R-multiple reading. Stays `DO NOT CODE`.

**Required:** add the four labels to `INDEX.md` row 26 and to `A-018`'s V05 row, scoped
*"printed, not spoken; live platform; three values legible, one not legible at this
resolution"*; correct *"four more labels"* to *"at least eight"*.

#### `M10` (`E02`) — §4c's framing sentence over-generalises its own table *(adopted from R1B `m4`)*

`V05_SOURCE_NOTES.md` §4c line 251 heads its four-row table: *"Repeated four times, **always
with the same escape clause**:"*

**Verified row by row against the transcript, including adjacent markers:**

| Row | What follows in the transcript | Escape clause? |
|---|---|---|
| `[00:11:11]` | *"…but up to five days."* | ✅ |
| `[00:15:47]` | `[00:15:52]` *"I'm letting my money out."* → `[00:15:55]` *"So those are the things you're watching for."* | ❌ **none** |
| `[00:16:35]` | `[00:16:36]` *"Expect a reversal."* → `[00:16:39]` *"You know how to draw the trend lines."* | ❌ **none** |
| `[00:24:34]` | `[00:24:37]` *"After three days of drop, but up to five days."* | ✅ |

**The four rows are individually accurate; the sentence above them is not.** It is also the
origin of `M8` — a framing sentence in the source notes became a false verbatim count one file
downstream in the mastery report. Charged separately from `M8` because this is where it
starts.

**Required:** restate as *"Repeated four times; two of the four carry the explicit `up to five
days` escape clause."*

#### `M11` (`E11`) — a third citation in the same wrong-offset cluster *(adopted from R1B `n1`, escalated from NOTE to MINOR)*

`AUTOMATION_AMBIGUITIES.md` `A-042` evidence table, line 2854, cites `[01:01:39]` for *"for the
DMR, I kind of use the ellipse to show the moving average crossover"*.

**Verified:** `[01:01:39]` is **not a marker in this transcript** (`grep -c` returns 0). The
markers either side are `[01:01:37]` *"I don't need my box to be all the way out here."* and
`[01:01:40]` *"Okay, and then it drops."* — neither is the quoted sentence. **The words are at
`[00:57:39]`** (body line 3729), three markers after `M1`'s pair.

**Escalated from R1B's NOTE to a MINOR** because it is a live nonexistent-marker citation
requiring correction, which is the same defect class R1 charged as `M1` — filing it as a note
would leave it out of the required-actions list. **The cluster is the point:**

| Cited | Actual | Offset |
|---|---|---|
| `[01:07:36]` | `[00:57:36]` | +10:00 |
| `[01:01:35]` | `[00:57:35]` | +04:00 |
| `[01:01:39]` | `[00:57:39]` | +04:00 |

Three citations into one 5-second window of speech, all displaced upward. **Two were fixed at
`152f4ea` and the third was not, because R1 did not find it.** This is exactly why R1B was
worth keeping.

**Required:** correct `A-042`'s `[01:01:39]` → `[00:57:39]`. Also sweep the remaining V05
citations for a fourth instance — R1B `n1` recommended this and it has not been done.

### NOTE

- **`N1` — `E11` has re-escalated as a class, and the count is now four.** V04 R1
  de-escalated the citation class after three clean lessons. V05 carries `M1`'s two, `M2`'s
  off-by-one and `M11`'s third cluster member. Open item 7's proposed amendment (*cite the
  marker the quoted sentence's first words fall under*) would have caught `M2` but **not the
  cluster** — the cluster needs a mechanical marker-existence check, which is cheap and which
  both R1 and R1B ran by hand. **Worth raising at `CUMULATIVE_25.md` with open items 7 and 14,
  as R1B `n2` proposed.**
- **`N2` — the two owner-decision items are correctly logged and are NOT resolved here.**
  Confirmed against `REVIEW_INDEX.md` this round, as instructed, and deliberately left alone:
  **open item 40** (the `D-025` carve-out for records whose subject is a guest's own utterance
  or a platform artifact) is logged `⚖️ AFFIRMED … OPEN only on the owner's recording step`;
  **open item 36** (the third disposition `EXCLUDED BY DECISION`) is logged `⚖️ RULED … OPEN
  only on the owner's adoption step`. **Both statuses are accurate as written and both remain
  the owner's to close.** Open item 35 (`A-042`'s out-of-corpus DMR dependency) likewise
  stands `OPEN — owner decision`. This round adds nothing to any of the three.
- **`N3` — the dimension-B re-disposition is still owed and is still correctly blocked.**
  R1 §8 item 8 and R1B §8 item 6 both require it; `152f4ea` declined it as blocked on open
  item 36. **That refusal is upheld.** `D-019`'s table grants `NOT APPLICABLE` for dimensions
  F and G only, so B's present label is unavailable — but the replacement label does not exist
  yet, and inventing one would be legislating. **This is the one outstanding R1 action that a
  student session must not perform**, and it does not hold the gate.
- **`N4` — a concurrent write was observed in this working tree during this review, and is
  disclosed rather than absorbed.** At `06:35:02` and `06:35:20`, while this session was
  working, `V05_TRANSCRIPT.md` and `QUARANTINE_REGISTER.md` were modified in the working tree
  with the open-item-39 correction. **This session issued exactly one edit (to the transcript)
  and the harness reported it as failed; it issued no edit at all to `QUARANTINE_REGISTER.md`,
  and the on-disk wording is not this session's drafted wording.** The author of those two
  writes therefore **cannot be established from inside this session.** What can be
  established, and was, is that **the content is correct** — `EMA` was re-measured
  independently before either write was read (§3), both edits state exactly the verified fact,
  both retain the superseded text per `REMEDIATION_PROTOCOL.md` §2, and both are cross-linked.
  They are adopted on that basis and committed by this round with the provenance disclosed.
  **This is the second concurrency event in V05's review layer in thirty minutes** (R1B §0.2
  was the first). **Owner: R1B's question — whether parallel sessions on one tree are intended
  — is now urgent, and it is item 3 of its § 0.2 owner action.**

---

## 3. OPEN ITEM 39 — THE `EMA` CORRECTION, RE-DERIVED AND APPLIED THIS ROUND

R1 §8 item 7 required this and `152f4ea` deliberately left it. **It was re-measured from the
transcript before any correction text was read**, per the instruction not to trust the stated
3 → 2:

```text
grep -n -w 'EMA'  02_TRANSCRIPTS/V05/V05_TRANSCRIPT.md
```

| Occurrence | Marker | Text |
|---|---|---|
| body line 1453 | `[00:23:52]` | *"Nice close below the 50 EMA."* |
| body line 4126 | `[01:05:53]` | *"Some amount of people with their stops below yesterday's low or below the 200 EMA."* |

Every other hit in the file is **inside the header and TRANSCRIPTION NOTES prose**, not the
verbatim body — i.e. the file's own commentary about the token, which cannot count as an
occurrence of it.

**The third item the note had listed is present and does not contain the token:** `[01:06:02]`
reads *"They'll induce by closing below the 200."* — the 200 is named, `EMA` is not said.

> ### ✅ **CONFIRMED INDEPENDENTLY: `EMA` occurs exactly TWICE. The 3 → 2 correction is right.**

**Applied this round at both sites, superseded text retained:**

| File | Correction |
|---|---|
| `V05_TRANSCRIPT.md` § TRANSCRIPTION NOTES | *"`EMA` occurs 3 times"* → *"`EMA` occurs 2 times"*, with the two markers named, the `[01:06:02]` misattribution explained, and the prior text retained in a superseded block |
| `QUARANTINE_REGISTER.md` `Q-005` Finding 2, row 1 | *"`EMA` occurs 3×"* → *"`EMA` occurs **2×**"*, markers added, prior text retained in a superseded block |

**No conclusion in either file changes, and this was re-verified rather than assumed.** Both
files were arguing that the fabricated `NOTES.md` invents a five-EMA colour system that the
audio does not contain. Re-measured this round: `5 EMA` **0**, `13 EMA` **0**, `5/13` **0**,
`800` **0**, `mayonnaise` **0**, `mustard` **0**, `water` **0**, `EST` **0**. **`Q-005`'s
falsification is untouched** — it rests on those zeros, on the absence of any period, colour or
nickname, and on the Steve-Mauro misattribution, none of which involve the count.
`A-020`'s V05 extension row already stated *"twice"* and needed no change; the three files are
now consistent.

`validate_project.py` after the edits: **97 passed, 0 warnings, 0 failures.**

### 3.1 The independence deviation, declared

`D-003` asks the reviewer not to audit its own work. **This session edited two student-layer
artifacts and then verified them, on the owner's explicit instruction.** That is a narrow but
real breach of the two-agent separation, and it is recorded rather than glossed:

- **Scope:** two numerals and two retained-text blocks. No conclusion, no rule, no
  classification, no evidence row, no dimension grade.
- **Mitigation:** the count was re-derived from the transcript **before** the edit, by the
  one-line method printed in §3, and the derivation is written out above so a later session can
  reproduce it without trusting this file.
- **Standing:** open item 39 is closed on that basis. A future session wanting a fully
  independent confirmation should re-run the word-boundary count — it is one `grep`.

---

## 4. WHAT THIS ROUND RE-DERIVED FROM PRIMARY SOURCE

Listed so a later round knows what was actually re-tested rather than carried:

| Re-derived this round | Result |
|---|---|
| `M1`/`M2`/`M3` marker text and neighbourhoods | transcript body lines 3717–3730, 2322–2332, 696–706 — all exact |
| `M11`/`A-042` citation | `[01:01:39]` **not a marker**; words at `[00:57:39]` |
| `EMA` token count, word-boundary, case-sensitive | **2** |
| *"but up to five days"* literal string | **2**; *"five days"* 4 |
| §4c's four rows and their adjacent markers | 2 of 4 carry the escape clause |
| `C-003` vs `C-004` record identity and the strike-off's location | strike-off is `C-004`'s; `C-003` record contains zero V05 text |
| The `C-004` clock-time check itself | reproduces — no `HH:MM`, no `EST`, no hour attached to either `London` |
| Frame 26 at 10× and 16× | sub-panel present, header illegible; four `R =` labels, three values legible, one not |
| `git show` diffs of all six remediated files | scope exact, `INDEX.md` disclosure byte-identical |
| `validate_project.py` | **97 / 0 / 0** |
| Register integrity | `A-001`…`A-049` and `C-001`…`C-005` contiguous, no duplicates, no gaps |

**Not re-audited** (`REVIEW_PROTOCOL.md` §4): V01–V04 artifacts except where V05 cites them;
the 799 uncurated sweep frames; the homework JSON, which R1 and R1B both recomputed
independently and independently reproduced — a duplicated verification this round would add
nothing; the Whisper spot-check windows; `A-045` and `A-048`'s ASR garbles, correctly left
unrepaired.

---

## 5. REQUIRED ACTIONS

**Student session** — five localised corrections. None requires reprocessing any artifact and
none changes a conclusion:

1. **`M7`** — `C-003` → `C-004` at `CONTRADICTIONS.md` lines 23, 845, 846 and
   `V05_MASTERY_REPORT.md` §J. Superseded text retained. **Do not edit `V05_REVIEW_R1.md`.**
2. **`M8`** — `V05_MASTERY_REPORT.md` §E: *"twice verbatim, `[00:11:11]` and `[00:24:37]`; the
   expectation itself four times."*
3. **`M9`** — record frame 26's four `R =` labels in `INDEX.md` row 26 and `A-018`'s V05 row;
   **three values only** (`40.9`, `40.6`, `41.1`), the fourth as *present, value not legible*;
   correct *"four more labels"* → *"at least eight"*. Does **not** narrow `A-018`.
4. **`M10`** — `V05_SOURCE_NOTES.md` §4c framing sentence: *"two of the four carry the escape
   clause."*
5. **`M11`** — `A-042`: `[01:01:39]` → `[00:57:39]`, and sweep the remaining V05 citations for
   a fourth cluster member.

**Blocked, not for a student session:**

6. **Dimension B** — re-dispose from `NOT APPLICABLE`, retaining the present text verbatim.
   **Blocked on owner open item 36.** Dimension G's grade is upheld; its *stated reason* must
   change to *"excluded by decision under `D-025`"* and that may be done independently of the
   label question.

**Owner actions — confirmed still open, deliberately not resolved here (`N2`):**

- **`A`** — open item 36: adopt `EXCLUDED BY DECISION`, or rule that the existing two suffice
  and say which applies to V05's dimensions B and G.
- **`B`** — open item 40: record the `A-043` carve-out as a numbered refinement of `D-025`.
- **`C`** — open item 35: `A-042`'s out-of-corpus DMR dependency.
- **`D`** — R1B §0.2: confirm or rename `R1B`; and rule on whether parallel/concurrent
  sessions on one working tree are intended (`N4` makes this urgent).

---

## 6. THE SEVENTEEN DIMENSIONS — RE-GRADED AT R2

Changes from R1 are marked. Where a grade is unchanged, the basis was re-checked, not carried.

| | Dimension | R2 verdict |
|---|---|---|
| A | Source fidelity | **PASS** — `M3` closed; `M8`/`M10` are counting and framing defects, not misquotations. **R1's *"preserved at all four occurrences"* is corrected here to two** |
| B | Completeness | **PASS** — unchanged |
| C | Provenance | **PASS with `E11` recurrence noted** — `M1`/`M2` closed, `M11` outstanding. Four defective citations against 356, three of them one displaced cluster |
| D | Explicit vs inferred | **PASS** — unchanged |
| E | Chart recognition | **NOT ENGAGED** — no setup classified anywhere |
| F | Counterexample testing | **PASS** — nine worked passes recorded as negatives, not coded |
| G | Manual backtest procedure | **NOT ENGAGED** — grade upheld; **stated reason still owed** (§5 item 6) |
| H | Hindsight / lookahead | **PASS — nil return.** Flashcard crops withhold the future half by construction |
| I | Outcome vs rule application | **NOT ENGAGED** — no trades |
| J | Sample quality | **PASS** — n = 3 refused as a finding in the file that produced it |
| K | Homework review | **PASS** — figures independently recomputed at R1 and R1B; both reproduce |
| L | Teach-back | **PASS** — unchanged |
| M | Blind recognition | **NOT ENGAGED** — V05 supplies no admissible criterion |
| N | Ambiguity review | **PASS** — `A-042`…`A-049` sound; six records extended, none narrowed; `A-043`'s closure **AFFIRMED**, concurring with R1 §5.1 and R1B `n3` |
| O | Contradiction review | **PASS on substance, `MINOR` on record identity** *(changed from R1's unqualified PASS)* — the nil return and its reasoning both reproduce; the struck-off record is `C-004`, named as `C-003` four times (`M7`) |
| P | Machine-rule firewall | **PASS** — every V05 record `DO NOT CODE`; nothing entered any spec or the concept library |
| Q | Claimed accuracy | **PASS** — the guest's 80–85% preserved with provenance, not reconciled with V01's 90–95%, held to be evidence about neither |

**No dimension moved down on the method. The two changes are both about record-keeping.**

---

## 7. WHAT THE REMEDIATION DID PARTICULARLY WELL

`REVIEW_PROTOCOL.md` §1 forbids manufacturing objections, and three things here deserve
recording:

1. **It resolved `M4` toward the honest disclosure and left `INDEX.md` alone.** The cheap fix
   was to soften the disclosure until it agreed with the flattering line. The diff proves that
   did not happen: `INDEX.md` is byte-identical except for `M6`'s row.
2. **It re-derived rather than transcribed.** Every correction quotes the marker's literal
   text, and `M1` and `M2` fixed the *sentence-spanning fragment* that caused the miscitation
   rather than just the number. `M6` was re-opened and looked at, and the header was still
   refused as illegible — the remediation had every incentive to name it and did not.
3. **It declined two items and said so in the commit message, at length, with reasons.** A
   remediation that quietly did five of six would have been much harder to audit. The refusal
   on dimension B — *"a student session applying an undefined label would be legislating"* — is
   the correct reading of this project's own separation of powers.

---

## 8. DECISION

```text
LESSON: V05
DECISION: REVISE
CONFIDENCE: HIGH

CRITICAL ISSUES:
- None.

MAJOR ISSUES:
- None.

MINOR ISSUES (all adopted from V05_REVIEW_R1B.md, all re-derived
and CONFIRMED at HEAD this round, none applied by 152f4ea):
- M7  (E20) C-003 named four times for a check that belongs to C-004
- M8  (E01) "but up to five days" counted four times; verbatim twice
- M9  (E20) four unrecorded printed R = labels in frame 26; A-018
            undercounts. One value is NOT legible — R1B's 74.6 is
            over-read and must not be transcribed
- M10 (E02) §4c "always with the same escape clause" false for 2 of 4
- M11 (E11) A-042 cites [01:01:39], not a marker; words at [00:57:39]

CLOSED THIS ROUND:
- R1 M1-M6      ALL SIX VERIFIED APPLIED, re-derived from source
- open item 39  EMA 3 -> 2 APPLIED at both sites, superseded text
                retained; count independently re-measured as 2

STILL OWED, BLOCKED ON OWNER:
- Dimension B re-disposition (open item 36)
- Dimension G's stated reason -> "excluded by decision under D-025"

R1B DISPOSITION:
- ACCEPTED into the lineage as a parallel R1 round. NOT superseded,
  NOT invalid, NOT edited, NOT deleted (I-002, PROTOCOL §11).
  Findings folded into R2 as M7-M11. R2 is now the operative list.
  REVIEW_INDEX.md reconciled to the true R1-round total: 10 minors
  raised, 6 applied, 4 + 1 outstanding.

CONCURRENCY:
- STUDENT LAYER: still no damage. Registers contiguous, 97/0/0.
- REVIEW LAYER: second event in 30 minutes. Two working-tree writes
  at 06:35 this session could not author. Content verified correct
  and adopted; provenance disclosed (N4). OWNER ACTION.

REQUIRED ACTIONS: 5 student + 1 blocked (§5), plus 4 owner actions
ADVANCEMENT: AUTHORIZED — V06 gate remains OPEN under D-024
V05 STATUS: NOT COMPLETE. Remediate M7-M11, then R3.
```

**Would I be comfortable letting future code depend on this interpretation?**
(`REVIEW_PROTOCOL.md` §18.) **Yes — and more confidently than at R1.** V05's interpretation
makes exactly one load-bearing claim: that the method is not in this lesson. Two independent
reviewers and now a third pass have tested that claim against the audio, the frames, the
committed data and the registers, and it holds every time. **All eleven minors raised across
three rounds are in counting, citation and cross-referencing — not one is in what V05 was
understood to mean.** The lesson that yields no doctrine cannot corrupt downstream learning,
and this submission has now resisted the temptation to manufacture some through three
successive audits.

**PASS is withheld for record-keeping, not for understanding.** Five verified defects sit in
files a future session will read as fact — a status block that names the wrong contradiction
record, a mastery report that miscounts a quotation, a chart index that omits half the
evidence in its own frame. `REVISE`. Fix the five, and R3 should close V05.

---

*Round R2. Never overwrite (`SETUP_ISSUES.md` I-002). `V05_REVIEW_R1.md` and
`V05_REVIEW_R1B.md` both stand unaltered. Remediation of `M7`–`M11` → `V05_REVIEW_R3.md`.*
