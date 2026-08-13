# V07 — INDEPENDENT REVIEW R3 (remediation verification, closing round)

| Field | Value |
|---|---|
| Lesson | V07 — *"Best Trade Grabs"* (`Bootcamp1 Wk2 032612 Part2 (48mins).swf`, 00:48:06) |
| Review round | R3 — verification of R2 item 70, and the residue of item 63 |
| Reviewed | 2026-08-13 |
| Reviewer | Independent Reviewer / Teacher Agent |
| Prior rounds | `V07_REVIEW_R1.md` — REVISE, 0/0/3 · `V07_REVIEW_R2.md` — REVISE, 0/0/1 |
| Remediation under review | Commit `cc74051`, branch `fix/v07-r2-item70`, **not yet merged** at the time of review |
| `D-003` separation of duties | **SATISFIED.** This session authored no V07 artifact and performed no part of any remediation. Every marker text below was read directly from `02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` **before** the remediated artifact text, and every count was re-derived by **two independent methods**. Neither the remediation's claims nor R2's prose was taken on trust — including R2's own, which this round re-measured |
| **Review basis** | Branch **`review/v07-r3`, cut FROM `fix/v07-r2-item70` at `cc74051`**. `git fetch --all` confirms the fix branch is **exactly one commit ahead of** the integration branch `claude/add-documents-repository-fdfb3u` and **zero behind** — a clean fast-forward, no divergence (`D-038`). **The V07 content under review is UNMERGED**, so the review had to be taken from the fix branch or it would have reviewed an empty set. This follows `V08_REVIEW_R1.md` §3's precedent for exactly this situation. `REVIEW_INDEX.md` and `LOG.md` are written here as **evidence ledgers** per `D-038a` |
| Process disclosure | No owner directive was issued for this round. Dimension B is carried from R1 unchanged — see §6 |

---

## EXECUTIVE BLOCK

```text
LESSON:     V07
DECISION:   PASS
CONFIDENCE: HIGH

CRITICAL:   0
MAJOR:      0
MINOR:      0
NOTE:       4   (N1 verifier precision bounds; N2 the bracket-token
                 ruling; N3 the overwrite alarm, investigated and
                 dismissed; N4 a process gap the investigation exposed)

ITEM 70:    CLOSED — VERIFIED at R3. All three instances corrected at
            their sites, each re-checked against the transcript by this
            reviewer independently. §H's replacement claim is accurate,
            scoped, and machine-backed. Superseded text retained at
            all four sites.
ITEM 63:    CLOSED — VERIFIED at R3. Its §D half closed at R2; its §H
            half discharges with item 70.

N1 (R2) DISCHARGED: the sweep is committed code. This reviewer RE-RAN
            it rather than writing a fourth sweep, and then attacked
            it — see §4. It reproduces R2's three instances exactly
            against the pre-correction tree and returns zero against
            the corrected one.

ADVANCEMENT: V08 gate remains OPEN (undisturbed). **V07 REACHES
             COMPLETE.**
```

---

## 0. WHAT THIS REVIEWER MEASURED, AND HOW

Source first, per `REVIEW_PROTOCOL.md` §3. The two disputed markers were read from the transcript
**before** any remediated artifact text was opened:

```text
[00:27:24]
The dashed ones like this are 30 minute versions, 30 minute of the water, 30 minute of the male,

[00:25:26]
That brown line there is the ADR. It turns red when Beth.
```

**The transcript is untouched by the remediation.** `cc74051` changes six files and
`02_TRANSCRIPTS/V07/V07_TRANSCRIPT.md` is not among them. The measurement base is the base R1 and
R2 measured against.

R2's own verified numbers were then re-derived from scratch, by a Python `re` pass and a `grep -oiE`
pass that share no code, because a closing round should not inherit the previous round's
arithmetic either:

| Measurement | Python | `grep` | Artifact claims | Verdict |
|---|---|---|---|---|
| Body size | 7,436 | **7,436** (`wc -w`) | §10 preamble: 7,436 | **Exact** |
| `level` + `levels` | **56** (53 + 3) | **56** | §10 **56 uses**, §5 **56** | **Exact** |
| `"the peak"` | **5** | **5** | §10 **5×**, five markers | **Exact** |
| `peak`/`peaks` bare token | 5 | — | no sixth use | **Exact** |
| `mayo` | **0** | **0** | §10 `mayo` **0** | **Exact** |
| `male` | **3** | — | — | consistent with §9's nickname list |
| `Beth` | **1** | — | `[00:25:26]` | **Exact** |

Items 61 and 62 are therefore **still correct in the corrected tree** — the item-70 edit did not
disturb them, which R2's §7 forbade.

---

## 1. ITEM 70, INSTANCE (a) — `V07_SOURCE_NOTES.md` §9a — ✅ CORRECT

The narrative sentence now reads:

> **`[00:27:24]` is the first time a NICKNAME is attached to a TIMEFRAME**: *"30 minute of the
> water, 30 minute of the male,"* — where *"male"* is the ASR's rendering of **"mayo"** (`A-020`,
> settled by print in V04/V06), exactly as §9's evidence table above renders it.

- **The quoted string is literal**, trailing comma included, and matches `[00:27:24]` character for
  character against the transcript read in §0.
- **The reconstruction is outside the quotation marks**, with its `A-020` provenance named — the
  practice §9's evidence table already modelled ten lines above, which is what R2 required.
- **The intra-file disagreement is resolved.** §10 still measures `mayo` at **0** and still says the
  audio only garbles it to *mail*/*male*; §9a no longer contradicts it. The file's two records of
  the same object now agree, which was the point.

---

## 2. ITEM 70, INSTANCES (b) AND (c) — the `[00:25:26]` reconstruction — ✅ CORRECT

Both sites now bracket rather than assert:

| Site | Now reads | Verdict |
|---|---|---|
| `V07_SOURCE_NOTES.md` §11, `[00:25:26]` row | *"it turns red when **[it's met]**"*, "the brackets marking the editorial reconstruction of the unrecovered word" | ✅ |
| `04_SCREENSHOTS/V07/INDEX.md` frames-add item 6 | *"It turns red when **[it's met]**"*, **with the marker `[00:25:26]` now adjacent** and the literal *"It turns red when **Beth**."* stated in the same item | ✅ |

Item 6's repair is **better than the minimum R2 asked for.** R2 required the brackets; the
remediation added the missing marker citation *and* printed the literal source word. The specific
defect R2 named for instance (c) — *"unbracketed, no adjacent marker,"* so a later session has no
signal it is reading a reconstruction — is fixed on both limbs.

**The self-contradiction in (b) is gone.** The row headed *"`[00:25:26]`'s **unrecovered** word"* no
longer quotes a recovered version of it.

**Both prohibited models are unedited**, verified by diff: `INDEX.md` row 15 and §9's evidence
table are byte-identical to `6d86272`.

---

## 3. §H's REPLACEMENT CLAIM — ✅ VERIFIED, AND IT IS THE RIGHT KIND OF CLAIM

§H now reads:

> **"Four quotations in the V07 set contained a word that is not in the source. One was found at R1
> (§D, `[00:28:31]`); three more were found at R2 and are corrected here."** As of this correction
> the claim is **machine-checked rather than asserted**, by `verify_quotes.py`, which is
> **committed and re-runnable**.

Three things changed, and all three matter:

1. **It is a historical count, not a completeness assertion.** R1's claim and R2's repair both
   asserted that a search had found everything. This one states what was found, by which round.
   Four is arithmetically right: R1's §D instance plus R2's three.
2. **It names its evidence and the evidence is executable.** This is the correction R2's `N1`
   argued for and did not require.
3. **The one categorical residue is true.** §H still says reconstructions are outside the quotes or
   bracketed *"at **every** site rather than at most of them."* This reviewer did not take that from
   the script — the script's blind spots are the subject of §4, and every one of them was searched
   **by hand**. Nothing survives. The claim holds.

The **superseded-text convention** (`REMEDIATION_PROTOCOL.md` §2) is satisfied at all four sites,
verified by reading `git diff 6d86272 cc74051` in full rather than the remediation's description of
it. `V07_SOURCE_NOTES.md` has exactly **two** deletion lines in the whole commit — the two defective
renderings — and both are reproduced verbatim in dated retention blocks naming the round, the open
item, the finding code and the instance letter. **No incorrect text was silently removed anywhere.**

---

## 4. `verify_quotes.py` — RE-RUN, THEN ATTACKED

R2's `N1` asked for committed code. The remediation delivered it. **A committed script is only
worth what its logic is worth**, so this round did three things: re-ran it, read it line by line,
and tried to break it with mutation tests.

### 4a. It reproduces — ✅

| Tree | Fragments extracted | Flags | Where |
|---|---|---|---|
| `6d86272` (pre-correction) | 338 | **3** | `V07_SOURCE_NOTES.md:360` (cited), `:478` (cited), `04_SCREENSHOTS/V07/INDEX.md:186` (**uncited**) |
| `cc74051` (corrected) | 338 | **0** | — |

Run by this reviewer, the pre-correction tree materialised in a detached worktree with the script
copied in. **Exactly R2's three instances and nothing else**, and instance (c) is indeed a tier-2
catch that no citation-windowed sweep could reach — which is the mechanism behind `N2`'s
239 / 238 / 167 spread, now explained rather than merely noted.

**The design is sound in its core choice.** Two tiers is the right shape: a flat "every quotation
must be in the transcript" rule is unusable over artifacts that also quote slides and predictions,
and the citation-windowed rule is precisely what let two of three instances through. The
matched-run test in `near_miss()` is better than the similarity ratio the docstring says was tried
and rejected, and the docstring's reason for rejecting it is correct.

### 4b. Four precision bounds, found by mutation testing — `N1`

Deliberate defects were injected into a scratch worktree to find what the script cannot see. A
positive control (a substituted word in a cited, emphasised, line-wrapped quotation) **flags
correctly**. Four classes do not:

| # | Injected defect | Result | Cause |
|---|---|---|---|
| L1 | A longer, differently-worded quotation beginning with an allowlisted prefix — *"M or W and the ZEBRA ate the level three peak"* | **Not flagged** | `allow_reason()` matches by `norm.startswith(prefix)` |
| L2 | A two-word misquote inside quotation marks, cited | Not flagged | `MIN_WORDS = 3` |
| L3 | A substituted word inside a quotation with **no** `*` emphasis | Not flagged | `QUOTE_RE` requires `*{1,3}` |
| L4 | A **new** substitution introduced on a Markdown block-quote line | Not flagged | `in_blockquote()` is tested **before** the cited-FLAG branch |

**L1 is the one worth naming precisely, because the docstring asserts the opposite.** Line 105
says matching is by prefix *"so an entry cannot silently excuse a longer, differently-worded
quotation."* **It can, and the mutation above demonstrates it.** Several allowlist prefixes are
short enough for this to be reachable in practice — `m or w`, `do they help`, `do they matter`,
`hi lo`, `exit 50 pips`. This is a false self-certifying statement in committed code, of the same
family R2 charged as `M1`.

**It is charged as a `NOTE`, not a `MINOR`, and the reasoning is stated rather than assumed.** R2's
`M1` was charged because a false categorical claim about *the evidence* would be relied on instead
of re-checking, and three real misquotes stood behind it. Here the claim is about *a tool's
precision bound*, and the load-bearing claim it supports — §H's *"at every site"* — **is true**,
established by this reviewer independently of the script:

- **L3 searched by hand.** 22 unemphasised quoted fragments of ≥3 words exist across the seven
  artifacts. All 22 were extracted and matched; the 12 that do not resolve were read in context.
  **None is a defect** — every one has a `near_miss` run of **0**, i.e. none tracks a transcript
  sentence at all. The two that are marker-cited are both explicitly self-labelled: §11a's *"M or
  W"* is named in the same cell as **slide print, with `MLW` identified as the ASR garble**, and
  §9's *"made the M there"* appears in a cell that states **it is not read that way**.
- **L4 searched by hand.** All 23 `RETAINED` fragments were enumerated with their near-miss runs
  and the opening line of their enclosing block quote. Every one with a run of ≥4 sits inside a
  genuine `REMEDIATION_PROTOCOL.md` §2 retention block re-quoting a *known, already-charged*
  defect — which is what the disposition is for. The single large run outside a retention block
  (49 words, `V07_SOURCE_NOTES.md:217`) is the bracket-token item ruled on in §5, not a
  substitution.
- **L1 and L2** produced no live instance: no current fragment is excused by prefix-widening, and
  no sub-three-word quotation in the set is a misquote.

**Recommended, NOT required, and V07 is not held for it.** Whenever `verify_quotes.py` is next
touched: anchor allowlist matching to the whole normalised fragment (or store the exact string),
and correct the line-105 comment either way. Test the `in_blockquote` branch *after* the
cited-FLAG branch so a retention block cannot mask a new defect. Both are one-line changes; neither
is worth opening a round, and **this round does not invent an obligation R2 did not raise** — the
same restraint R2 applied to `N1` itself.

---

## 5. THE BRACKET-TOKEN ITEM — RULED, NOT DEFERRED FURTHER — `N2`

The remediation surfaced one further flag, hand-checked it, deliberately did **not** fix it, and
recorded it in the allowlist for this round to rule on. **That was the correct handling** — it is
the opposite of the sweep-and-self-certify failure that produced item 70. The ruling is owed here
and is given here.

**The object.** `[00:29:49]`–`[00:29:52]` reads, literally:

```text
Do all the DMS speaker agree on this?
If so, how do I see it?
```

Four artifact sites render it *"Do all the **DM[R] speaker[s]** agree on this? If so, how do I see
it?"* — brackets **inside** the tokens. Strip the brackets, as the convention invites, and you get
*"DM speaker"*, which is not the source token *"DMS speaker"*. The bracket does not only insert;
it also silently deletes the *S*.

### RULING: **NOT a defect. No correction is required, and none should be made.**

Four reasons, in order of weight:

1. **It is not the R2 `M1` class, and the distinction is the whole point of that finding.** R2
   charged instances (a)–(c) because *a later session had no signal it was reading a
   reconstruction*. Here the signal is present and unmissable: the brackets are visible in the
   quotation itself. A reader cannot mistake `DM[R]` for verbatim audio. **§H's surviving
   categorical claim is not falsified** — it says reconstructions are *"outside the quotes or
   inside square brackets"*, and this one is inside square brackets.
2. **Intra-word bracketing is an established corpus convention, not a V07 invention.** It appears
   in `V01_SOURCE_NOTES.md` S63 (*"Fast mov[ing] markets"*) and in `V08_TRANSCRIPT.md`
   `[00:08:58]` (*"another FX sca[m]"*). Charging V07 for it would charge a convention three
   lessons wide on the strength of one lesson's review — outside this round's scope and outside
   `REVIEW_PROTOCOL.md` §4.
3. **The source token is recorded, in the right place.** `V07_TRANSCRIPT.md`'s own ASR-garble
   inventory carries it correctly and explicitly: *"do all the **DMS** speaker agree"* `[00:29:49]`
   for "DMR speakers". The corpus does not lose the literal word.
4. **Nothing is at risk.** *DMR* is a heavily attested corpus object (`[00:33:56]`, `[00:34:20]`,
   `[00:21:36]`, and three further transcript lines); *DM* is not an object at all, so the lossy
   strip cannot mislead a reader into a wrong referent. No conclusion turns on it: §6a's point is
   that a student named the inter-presenter divergence out loud and the presenter did not answer,
   and `C-005`'s extension rests on the non-answer, not the acronym.

### One observation, recorded and non-blocking

V08's transcript uses the **disciplined form** of this convention: it pairs the intra-word bracket
with an inline statement of what the ASR actually printed — *"another FX sca[m]."* — **the ASR
prints `scan`**. V07's four sites carry no such adjacent disclosure; the reader must reach the
transcript's PROVENANCE section ~190 lines away. **Recommendation, not a correction:** when any of
those four lines is next edited for another reason, append the V08 form. **Do not open an edit for
this alone**, and do not treat it as owed. If the convention is to be settled project-wide, that
belongs to `CUMULATIVE_25.md`, which is where the question of whether intra-word bracketing should
be spelled differently at all should land.

---

## 6. THE POSSIBLY-OVERWRITTEN FILE — INVESTIGATED — **FALSE ALARM** — `N3`

The remediation session reported that at its start, `git status` already showed
`V07_SOURCE_NOTES.md` as modified and `05_HOMEWORK/V07/scripts/verify_quotes.py` as untracked,
**before it did any work**, and that its own `Write` may have destroyed another session's work.
This matters for trust in the `D-038` branch-isolation system, so it was investigated rather than
waved off.

**Finding: no work was lost. No evidence of any pre-existing file at that path exists, and there is
positive evidence of sole authorship.**

| # | Test | Result |
|---|---|---|
| 1 | Does `verify_quotes.py` exist in any other commit, on any ref? | **No.** `git rev-list --all` — the blob appears in **exactly one** commit, `cc74051` |
| 2 | Does any unreachable or dangling object hold another version? | **No.** All 31 unreachable blobs were read; **not one is a Python file**, let alone a quote verifier |
| 3 | Is there a stash? | **No.** `git stash list` empty |
| 4 | Editor/backup leftovers (`*.orig`, `*.rej`, `*~`, `*.bak`)? | **None** anywhere in the tree |
| 5 | Any leftover untracked file in the main working tree? | **None.** `git status --untracked-files=all` is clean |
| 6 | Does any other worktree hold a `verify_quotes.py`? | **No.** All four sibling worktrees checked |
| 7 | Does the committed `V07_SOURCE_NOTES.md` diff contain foreign content? | **No.** Two deletion lines in the whole commit, both the known defective renderings, both retained verbatim |

**Test 5 is the decisive one.** The only other session that worked in *this* working directory in
the relevant window is the R2 reviewer (reflog: `13:14:56`–`13:22:23`), and R2 did run a sweep of
its own. Had R2 left that sweep on disk at **any** path other than the exact one the remediation
later wrote, it would still be sitting there untracked today — nothing in the intervening history
deletes untracked files. The tree is clean. So either R2's sweep never touched the repository, or
it occupied precisely that one path.

**R2's own record settles which.** Its `LOG.md` entry lists *"Files produced / updated"* as exactly
three files, no script; and `V07_REVIEW_R2.md` §6 `N1` describes its sweep **in prose**,
explicitly *because* it was not committed. This project has a strong, repeatedly exercised
convention of naming untracked working-tree files in the LOG's git section — V02's
`measure_usdchf_week.py` is named in a dozen entries across five sessions and became open item 13.
**R2 named none.**

**Timeline is consistent with sole authorship.** The remediation branch was checked out at
`13:28:45` (reflog); `verify_quotes.py` has mtime `13:35:16` and `V07_SOURCE_NOTES.md` `13:35:52` —
both roughly seven minutes **inside** the session, with `INDEX.md`, the mastery report,
`REVIEW_INDEX.md` and `LOG.md` following at `13:51`–`13:53` and the commit at `13:54:16`. (An mtime
cannot by itself exclude an in-place overwrite; it is offered as consistency, not as proof.)

**The most probable explanation is the benign one the question anticipated: the session observed
its own in-run draft.** The script's docstring records its own design iteration — *"A similarity
RATIO was tried first and rejected"* — so a first draft existed and was rewritten. A `git status`
taken after that first draft returns exactly what was reported: `verify_quotes.py` untracked and
`V07_SOURCE_NOTES.md` modified, both by that session's own hand, roughly seven minutes in.

**Stated honestly: repository forensics cannot prove a negative about an untracked file overwritten
in place, because an untracked file leaves no git trace at all.** The finding is *no evidence of
loss, plus positive evidence of sole authorship*, not a mathematical proof. **Nothing is owed, and
`D-038` branch isolation is not implicated** — every worktree checked is clean or carries only its
own live work.

### `N4` — the process gap the investigation exposed

**The remediation reported this concern in its session output but did not record it in `LOG.md`.**
Its LOG entry lists the script as *"**new**"* with no mention of the observed pre-existing state.
That omission is why a forensic reconstruction was needed at all — a two-line note of the
working-tree state observed at session start would have answered it in seconds, and the project's
own convention (test 5's V02 precedent) already does exactly this for untracked files.

**Recommendation for `CUMULATIVE_25.md`, not a correction owed by V07:** make it explicit in
`COMMON_PROTOCOL.md` that a session records the `git status` it observes **at start**, not only the
one it produces at commit. A concern raised in session output but absent from the durable log is,
for every later reader, a concern that was never raised.

---

## 7. STANDARD PASS — WHAT ELSE WAS CHECKED, AND WHAT DID NOT REGRESS

This round is a verification round, but `REVIEW_PROTOCOL.md` §6 was not narrowed to item 70.

| Check | Result |
|---|---|
| **A. Source fidelity** | Both disputed markers read from the transcript before any artifact; all three corrected sites literal. Items 61/62 re-derived twice and still exact |
| **C. Provenance** | `[00:25:26]` now carries its marker at `INDEX.md` item 6, which it previously lacked. `A-020` provenance restored to §9a's reconstruction |
| **D. Explicit vs inferred** | This is the dimension item 70 lived in, and it is the one that improved: three reconstructions moved from inside quotation marks to outside or inside brackets |
| **O. Contradiction review** | The two intra-file disagreements R2 named (§9a vs §10; §11's row vs its own heading) are both resolved. `CONTRADICTIONS.md` untouched — correctly, no `C-xxx` moves |
| **Regression, whole-lesson** | `git diff 98d893a cc74051` over every V07 path: only the four artifact files plus the new script. **Transcript, homework, interpretation, backtest and pre-registration are untouched since the R1 remediation** |
| **R2 §7 prohibitions** | All honoured, verified individually: items 61/62 not re-opened; §9's table, §10's `mayo` **0** row, §5, §6c and `INDEX.md` row 15 all byte-identical to `6d86272`; no retention block deleted; no git history rewritten |
| **`R11` must stay failing** | Re-run: **`R11  FAIL`**. Correct |
| **No V07 script re-run** | R1 forbade it and this round did not. `comprehension_probe.py` was executed only to read `R11`'s state, which R2 also required; nothing was recomputed or restated from it |
| **`validate_project.py`** | **103 passed / 0 warnings / 0 failures** |

**Dimension B is carried from R1 and R2 unchanged: NOT SATISFIED, blocked by `D-030`, structural,
not attributable to the student, carrying NO severity charge.** No owner directive was issued for
this round either. `REVIEW_INDEX.md` **open item 36** — the `EXCLUDED BY DECISION` vocabulary — is
now owed for the **sixth** lesson-round running. **It is restated, not re-argued, and it is not a
gate.** It is not the student's to fix, and it must not hold V07.

---

## 8. DECISION

The remediation did what R2 required, at every site, and did one thing more that R2 explicitly
declined to require. All three instances are corrected against the primary source, verified here by
reading the transcript first. The categorical claim that failed twice has been replaced by a
historical count with executable evidence behind it — which is the structurally correct fix, not
merely a third attempt at the same sentence. The superseded-text convention is satisfied at all
four sites, better than the minimum. Every prohibition was obeyed.

**The substantive advance is `verify_quotes.py`, and it survives being attacked.** It reproduces
R2's findings exactly, returns clean on the corrected tree, and its two-tier design is the right
answer to the failure mode that produced item 70. This reviewer found four precision bounds in it,
one of which is a comment that overstates the allowlist's tightness — and then searched all four
blind spots by hand and found nothing living in them. **The claim §H now rests on is true, and this
round establishes that independently of the tool that also establishes it.** The bounds are
recorded as `N1` so the next round tightens them cheaply; they are not charged, because charging a
tool's documented-but-harmless precision limit as a defect in a *lesson* would be the artificial
difficulty `REVIEW_PROTOCOL.md` §16 forbids.

The bracket-token item is ruled: **not a defect**, and the remediation was right to flag rather than
fix it. The overwrite alarm is investigated and **dismissed**, with the one real lesson in it —
record the working-tree state you *observe*, not only the one you *create* — carried as `N4`.

**Nothing remains owed on V07.**

```text
LESSON: V07
DECISION: PASS
CONFIDENCE: HIGH

CRITICAL ISSUES: none
MAJOR ISSUES:    none
MINOR ISSUES:    none

VERIFIED CLOSED: item 70, and item 63 in full (its §D half at R2, its
                 §H half here). Items 61 and 62 were verified at R2 and
                 re-derived again here; both still hold.

REQUIRED ACTIONS: none.

RECOMMENDED, NOT REQUIRED — do NOT open a round for these:
1. verify_quotes.py — anchor allowlist matching to the full normalised
   fragment and correct the line-105 comment; order the in_blockquote
   test after the cited-FLAG test. Whenever the file is next touched.
2. The four DM[R] sites — adopt V08's inline "the ASR prints `DMS`"
   form, whenever those lines are next edited for another reason.
3. CUMULATIVE_25.md — the standing rule N1 proposed (a numeric or
   categorical claim in an artifact must be produced by committed,
   re-runnable code) now has a worked instance on both sides: two hand
   sweeps failing on this corpus, and committed code reproducing an
   independent reviewer's findings exactly. Also the N4 start-state
   logging rule, and whether intra-word bracketing should be spelled
   differently project-wide.

ADVANCEMENT:
V08 gate remains OPEN and undisturbed. **V07 IS COMPLETE.**

OWNER RULING OWED: REVIEW_INDEX.md open item 36 (dimension B
vocabulary), SIXTH lesson-round running. Not a gate, and it does not
hold V07.
```

---

## 9. LOGGING

`REVIEW_INDEX.md`: decision row (V07 R3 **PASS** 0/0/0, ✅ COMPLETE); items **63** and **70** → ✅
**CLOSED — VERIFIED at R3**; STATUS block moves V07 from `IN REMEDIATION` to `PASSED`, with its
superseded text retained. `LOG.md`: reviewer R3 entry.

**Merge-back:** per `D-038`, this reviewer merges `fix/v07-r2-item70` — with these review commits on
top — into the integration branch, the verdict being clean. `git fetch` re-checked for divergence
immediately before.

**Next review trigger:** none for V07. The lesson is closed. `CUMULATIVE_25.md` carries the three
recommendations above.

**For `CUMULATIVE_25.md`:** the `E01`/`E20` classes are now **discharged in V07** — three rounds,
seven items, all closed and verified. The durable lesson of this lesson is not the misquotes: it is
that **two successive hand sweeps of the same corpus produced a false categorical claim, and
committed code produced a true scoped one.** Record also that the remediation which finally got it
right did so by *flagging* an item it was unsure of instead of ruling on it — the behaviour that
would have prevented item 70 had the previous round used it.
