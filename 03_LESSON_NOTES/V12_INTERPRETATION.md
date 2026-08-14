# V12 — INTERPRETATION

> **What this file is.** The judgement calls. `V12_SOURCE_NOTES.md` records what the lesson says;
> this records what this session concluded from it, **with a confidence grade on each and the
> reason the grade is not higher.** `D-008`: course evidence outranks agent interpretation, so
> nothing here is a source for anything.

---

## Q1 — Does `A-039` CLOSE? **NO — and this session had to argue itself out of closing it.**

**Confidence: HIGH that it does not close. MEDIUM that "narrowed again" is the right description
rather than "split".**

`A-039` reads *"TDI is a **required entry criterion** that the course has never taught."* V12 makes
the second half of that sentence indefensible. The lesson is 55 minutes on the TDI: four
components built one at a time, two named setups, a three-rung scale-in ladder, an exit rule, six
worked charts, a printed deck, and a homework drill that uses nothing else.

**The case FOR closing it, stated at its strongest:**

- V11 narrowed `A-039` partly *because* the band and signal-line treatment was promised and did
  not arrive. **It has now arrived.**
- `A-080`, the record's own headline blocker, is **closed** (`RESOLVED BY COURSE`, period 21).
- Every entry, add and exit in the ladder is stated **twice**, in print and in speech, and the two
  agree.
- The instructor gives the *rationale* for the one parameter he changed, which is more than most
  of the corpus offers about anything.

**Why it does not close anyway — and the reason is narrow and specific:**

`A-039`'s operative status is `DO NOT CODE`, and `DO NOT CODE` is a claim about **reconstructibility**,
not about pedagogy. To plot this indicator a machine needs four numbers. V12 supplies **one**:

| Component | Period / setting | Supplied? |
|---|---|---|
| RSI line | **21** | ✅ `[00:07:24]`, `[00:10:51]` |
| Trade signal line | smoothing length | ❌ *"polls the one-hour chart"* is a **metaphor for what it achieves**, not a construction — `A-085` |
| Market baseline | smoothing length | ❌ *"he took a moving average and lined it up very close to price action"* names the **type** and not the length |
| Volatility bands | basis + deviation | ❌ *"2%, I don't know, two standard deviations… I don't really know"* — `A-086`. And the **basis** is corrected mid-sentence from *price action* to *the RSI line* on a prompt from the chat |

**Three of four remain unstated, and the one the speaker attempts he explicitly disclaims
knowing.** `D-030` is not a technicality here: substituting Dean Malone's shipped defaults would
reconstruct *Dean Malone's* indicator, and the lesson's whole premise at `[00:07:20]` is that this
one has been **altered**.

```text
A-039 -- NARROWED AGAIN, NOT CLOSED.
Was (V11): "TAUGHT AS TO ITS SUBSTRATE AND ITS READING; UNSPECIFIED AS TO EVERY PARAMETER"
Now (V12): "TAUGHT IN FULL AS TO MECHANISM, SIGNALS, ENTRY, SCALING AND EXIT.
            ONE OF FOUR PARAMETERS SUPPLIED (RSI = 21).
            THE PEDAGOGICAL DEBT IS DISCHARGED; THE RECONSTRUCTION BLOCKER IS NOT."
```

> ### ⚠️ WHERE THIS SESSION THINKS IT MAY BE OVER- OR UNDER-CREDITING — flagged for R1
>
> V11's session flagged that it might be **over**-crediting. **This one's risk runs the other
> way: it may be UNDER-crediting.** A reviewer could reasonably hold that `A-039`'s subject is
> *"the course never taught the TDI"*, that V12 plainly teaches it, and that the surviving
> parameter gaps are properly `A-085`/`A-086`'s business — in which case **`A-039` closes and
> three narrower records carry the residue.** That reading is coherent and this session does not
> adopt it, for one reason only: **`A-039` is cited as a blocker by other records** (`A-031`'s
> third narrowing reason is *"`A-039` is upstream and still blocks"*), and closing it would
> silently unblock them. **If R1 prefers the split, the mechanism is clean** — close `A-039`,
> and re-point its dependents at `A-085`/`A-086`. **This session declines to make that call
> unilaterally because it changes other records' status as a side effect.**

---

## Q2 — What is actually unblocked by `A-080` closing? **V11's RSI half — with one caveat that may cost it.**

**Confidence: HIGH on the unblock. MEDIUM-LOW on whether it survives `A-084`.**

`A-080` blocked *"every RSI-dependent claim in V11"*: the 50-baseline bias rule, the 80/40 ↔ 60/20
range switch, the 80/20 overextension threshold, the 38–42 pullback band, the ~60 pullback
resistance, both divergence forms and the `[00:36:19]` composite entry. **All of those are
thresholds on a line whose period is now known.**

**The caveat, and it is not hypothetical.** `A-084` asks whether the green line in the TDI
sub-window **is** `RSI(21)` or a **smoothing of** it. Dean Malone's shipped TDI plots
`MA(n)` of `RSI(m)`. V12 says *"TDI is developed off of the RSI, so there's your RSI line"* —
lineage, not identity — and states no `n`.

**Why this matters concretely rather than pedantically:** V11's thresholds are read off *the line
in the sub-window*. If that line is a 2-period average of `RSI(21)`, then testing them against a
raw `RSI(21)` tests a **different series** — one that is strictly noisier, crosses 50 more often,
and spends a different fraction of its life beyond 80.

**This session's judgement:** a test of V11's threshold claims is **now possible on `RSI(21)`
directly**, and it must be **pre-registered as a test of `RSI(21)`, not of "the TDI line"**, with
`A-084` named as the gap in its own §2. **`PT-040` does exactly that** — see Q5.

---

## Q3 — Is the `mayonnaise = 200` evidence really Tier 1, or is this session over-reading it?

**Confidence: HIGH. This is the strongest single evidentiary moment the project has produced.**

The question is worth asking because **`D-041`, `D-042` and `D-043` are three rulings in
twenty-four hours on this exact family**, and a session arriving with a fourth answer should
expect scepticism. So the claim is stated at its narrowest:

**Claimed:** *mayonnaise* denotes the **200** moving average, on the course author's own statement.

**The evidence, and each limb independently:**

1. `[00:31:22]`–`[00:31:27]`, **two adjacent sentences, one object**: *"held by the mayonnaise
   perfectly. Held by the 200."* No chaining. No second warrant.
2. **The slide on screen at that second** prints `PRICE HELD BY 200`. **The identification does not
   depend on the audio.**
3. A **second passage, five minutes earlier, on a different chart** (`[00:26:20]`–`[00:27:19]`)
   moves between *"a 200 EMA"* and *"the mayonnaise"* four times as one subject.
4. **Two independent ASR engines** agree verbatim on both passages.
5. The **word is printed** — `Shark Fin Hold The Mayo`, burned `26:11` — at the same second the
   audio renders it *"mail"*.

**What would falsify it:** a reading on which *"held by the mayonnaise"* and *"held by the 200"*
name **two different lines that both held price at the same moment**. The chart makes that
strained — one line is doing the holding — but it is the only alternative and it is recorded here
so a reviewer can weigh it rather than having to construct it.

**Why this is not a fourth contradictory answer:** it **agrees** with `D-043`, with `D-039`, with
`MMM-NOTES` p.66, and with `A-020`'s original closure table. **Every source that has ever spoken on
the mayo row has said 200.** `D-041`/`D-042`/`D-043`'s three-state history is about **ketchup,
mustard and the colours** — rows on which **V12 is silent** and which are **unaffected**.

**What changes is the WARRANT, not the value:** `RESOLVED — OWNER ATTESTATION` → `RESOLVED BY
COURSE`. Under `SOURCING_HIERARCHY.md` that is a real upgrade, because owner attestations have now
twice been overturned within a day and Tier 1 has not.

> **And note what does NOT change.** `D-043` §1's **colour** row for mayo stays on owner
> attestation + `[TOOLING]`. Two frames show price held at a **white** line under captions naming
> *Mayo* and *200* — **suggestive, and not adopted**, because no legend says the white line is that
> line (`V12_SOURCE_NOTES.md` §10.3). **Refusing the free colour upgrade is the same discipline
> that made item 109 right about `RSI(21)`.**

---

## Q4 — Does the 23-pip stop discharge `A-066`?

**Confidence: MEDIUM. This session says NO, and is least sure of this answer.**

`A-066` records *"a stop SIZE with no placement rule."* V12 prints and speaks **`Stop Loss 23 Pips
above the HOD`** — a size **and** a reference object. On its face that is the missing half.

**Why this session still declines to discharge it:**

1. **`HOD` is `A-056`'s object.** *"23 pips above the high of the day"* is only operational if you
   can say **when the high of the day is the high of the day** — which is the Hi-Lo problem
   `A-056` has carried since V08, extended and not closed. **A placement rule anchored to an
   undefined anchor is not a placement rule.**
2. **A second, incompatible size is given in the same breath.** `[00:30:37]`: *"if you're a second
   leg trader… **seven to ten pips above the second leg**"*. Two stops, two anchors, one sentence
   apart, with no rule for which applies.
3. **⭐ And the lesson itself declines to state one when asked.** `[00:48:15]`–`[00:48:54]`, asked
   directly for a stop size for the homework, the instructor says ***"you tell me"***, invites
   guesses, hears *"10, 23, 25"* from the room, and endorses ***"seven, ten sounds great"***.
   **The lesson that printed `23` will not commit to `23` forty minutes later.**

**Point 3 is the one this session weighs most heavily**, and it is the reason the answer is `NO`
rather than `narrowed`. **A reviewer may well disagree** — a fair counter-argument is that the
printed slide is the doctrine and the Q&A is casual, which is exactly the printed-vs-spoken
precedence question **V10 carry-forward (f) asks the owner to rule on and which is still
unresolved.** *(V12 supplies a fourth data point for that ruling; see Q7.)*

```text
A-066 -- EXTENDED, NOT DISCHARGED. A placement rule was supplied and its anchor is
         A-056's undefined object; a second incompatible size sits one sentence away;
         and the lesson refuses to restate the number when asked.
```

---

## Q5 — What is testable, and what is `PT-040`?

**Confidence: HIGH that `PT-040`'s claim is testable. See `BT_V12_0001.md` for the result.**

**Not testable** (`D-030`): anything requiring the TDI itself — shark fin, blood in the water, the
MB/VB scale-in ladder, the VB-return exit. **Three of four parameters are missing** (Q1). This is
stated because the temptation is real: the ladder is the most completely specified trade
management in the corpus, and it is **still not reconstructible**.

**Testable, and only because of `A-080`:** the lesson opens with a **quantified empirical claim**
that is about **price action alone** —

> `[00:00:51]`–`[00:01:12]`, course author, reporting a student's multi-year back-test:
> *"Simply taking **the second leg** of an M or W spread out over **five bars**, that presents
> itself **above or below the blue box** within the appropriate times, **irrespective of any other
> indicator or criterion, is good for approximately 85%.**"*
> Restated `[00:01:48]`: *"that second leg… **outside above or below the blue box** — solid gold."*
> And escalated `[00:02:29]`: *"those are the things that will filter you out to **the 90%**."*

**This is the most falsifiable claim V12 makes**, it is **explicitly indicator-free**, and it is
the only one whose inputs the corpus can supply. **`PT-040` pre-registers a test of the `85%`
figure's *reachability*** — deliberately **not** of "the M/W second leg", which `A-011` blocks.
See `PT-040`'s §2 for the four things it does **not** test and why.

---

## Q6 — ⭐ The `A-082` error, and what it implies for the V13/V14 gap audit

**Confidence: HIGH. This is the most useful thing in this file.**

`V12_SOURCE_NOTES.md` §9a records that this session **asserted a corpus-wide negative and was
falsified by running the sweep it was describing.** `A-082` says the flashcards are *"never
specified"*; **V03 teaches them for twenty-five minutes**, with a quantity (40) and a timeframe
(15-minute).

**The generalisation, and it is the V13/V14 planning item:**

> **A record that says *"the corpus never says X"* is only as good as the sweep behind it, and
> late-raised records are systematically the least likely to have had one** — because a session
> working on lesson *N* is looking at lesson *N*, and asserting a negative over V01–V21 costs a
> search it did not budget for.

`A-082` was raised by **V11**, against material sitting in this repository with a completed review.
**It survived V11's own pass and V11 R1.** What caught it was a **carry-forward that named the
command**.

**Candidates for the same audit, listed so V13/V14 can run them rather than re-derive them.** Each
is a record whose current text asserts or implies a corpus-wide negative that this session has
**not** verified:

| Record | The asserted negative | Cheap test |
|---|---|---|
| `A-004` — "the level" | *"never defined"* across 9 lessons | Word-boundary sweep for `level` + `count` collocations, all 21 |
| `A-011` — M/W anatomy | *"nine lessons, zero definitions"* | Sweep for `M formation`/`W formation` near `bars`/`candles`/`legs` |
| `A-076` — `blue box` | *"the object every V10 trigger references, and it is never defined"* | Sweep for `blue box` + `pips`; V12 `[00:23:43]` already attaches a size |
| `A-056` — Hi-Lo | *"named as a primary method and never taught"* | Sweep for `hi lo`/`high low` + `drill` |
| `A-002` — trap move | *"fourth speaker, fourth role, still no definition"* | Sweep for `trap` across all 21 |

**None of these is asserted here to be wrong.** The point is that **`A-082` was wrong in exactly
this way and nobody noticed for a lesson and a review**, so the class deserves one deliberate
pass. **It is cheap** — the `A-082` sweep took one command — **and V13/V14 are the last two
lessons before the owner's hard stop**, which makes this the last scheduled opportunity.

---

## Q7 — Printed vs spoken: V12's contribution to the ruling V10 carry-forward (f) requests

**Confidence: MEDIUM-HIGH.**

The corpus has no standing rule on precedence. V11 supplied two instances pointing opposite ways
(item 106). **V12 supplies two more, and both point the same way as V11's (ii): the speech
governs, because the speaker is overriding a deck he did not write.**

| # | Printed | Spoken | Reading |
|---|---|---|---|
| 1 | `09:41`, Dean Malone's definition: *"trend direction, **momentum**, and **market volatility**"* | `[00:09:51]`–`[00:10:03]` *"**momentum we know is bullshit**… volatility is the speed of the candles during the stop hunt"* | **Speech repudiates print, on the record, with the reason given.** Same shape as V11's `POSITIVE TREND` case |
| 2 | `29:11`: *"Enter The Trade **Stop Loss 23 Pips** above the HOD"* | `[00:48:24]`–`[00:48:54]` *"what size stop loss? **You tell me**… seven, ten sounds great"* | ⚠️ **Speech DOES NOT repudiate print — it declines to restate it.** This is a **third polarity**: not agreement, not contradiction, but **abandonment** |
| 3 | `42:06`: the assignment, four lines | `[00:43:18]`–`[00:49:08]`: the assignment, **six minutes**, adding the demo account, the blind constraint, the wristwatch and the pair restriction | **Speech is a strict SUPERSET.** Same shape as V11's `A-081` |

**What this session takes from it, and the recommendation it puts to the owner:**

- **The corpus's slides are, repeatedly, borrowed or older material the speaker talks over.**
  `[00:08:32]` *"they're kind enough to let me use the slides"*; V11 `[00:xx]` *"maybe 15 years
  ago… I'm not even sure these slides came from that guy"*. **A blanket "print beats speech" rule
  would make doctrine of decks the instructor did not write and sometimes rejects.**
- **A blanket "speech beats print" rule is also wrong**, because row 3's superset and row 2's
  abandonment are not the speaker disagreeing — they are the speaker being loose.
- **Recommended to the owner as the narrow rule that fits all six instances (V11's two, V12's
  three, and `C-017`):** *the print and the speech are both Tier 1; where they conflict, **the
  medium in which the speaker gives a reason wins**; where neither gives a reason, the record
  carries both and codes neither.* **Rows 1 and 2 both resolve under it, in opposite directions,
  which is the property a blanket rule lacks.**

**Not adopted, not applied, and no record's status turns on it here.** It is put forward as a
proposal because V10 carry-forward (f) asked for the material and V12 is the fourth lesson to
supply it.

---

## Q8 — Confidence self-assessment

| Conclusion | Confidence | The reason it is not higher |
|---|---|---|
| `A-080` closes; RSI = 21 | ⭐ **VERY HIGH** | Four statements, two engines, a stated rationale, and a group-preset declaration. **The only residue is `A-084`** — 21 is the RSI's period, and whether the plotted green line *is* that RSI is unstated |
| `mayonnaise` = 200, Tier 1 | ⭐ **VERY HIGH** | Q3. The one alternative reading is recorded there |
| `A-064` closes | **HIGH** | Printed `Mayo` + spoken *"mail"* at the same second |
| `A-031`, `A-032` close; `C-019` opened | **HIGH** | Printed **and** spoken definitions, three times. The contradiction with `MMM-NOTES` p.46 is plain and `§3.3` is unambiguous about which wins |
| `A-039` narrows, does not close | **MEDIUM** | Q1 — this session may be under-crediting, and says so |
| `A-066` not discharged | **MEDIUM** | Q4 — turns partly on the unresolved printed-vs-spoken question |
| `A-082` reframed | **HIGH** on the finding, **MEDIUM** on the new status text | Q6. The finding is measured; the right *wording* of a reframed record is a judgement |
| Speaker = course author | ⭐ **VERY HIGH** | Nine strands, zero handovers, four strands new to this half of the session |
| `PT-040`'s design | **MEDIUM-HIGH** | It tests a **reachability envelope**, not the instructor's claim, and says so in its own §2. See `BT_V12_0001.md` §1a |

### What this session did NOT do

- **No independent full re-transcription.** Seven spot-checks, ~6 minutes of 55. `I-008` stands.
- **No archival mp4.** Screenshots-only path (`SWF_CAPTURE_RECIPE.md` §10). The mp4 is a per-lesson
  choice and was not wanted here.
- **The `A-084` question was not tested empirically.** Whether `MA(2)` of `RSI(21)` differs
  materially from `RSI(21)` on this corpus is answerable with the HistData corpus and **was not
  answered.** It is the cheapest single thing V13 could do to finish unblocking V11's RSI half,
  and it is recommended in `V12_MASTERY_REPORT.md`.
- **The Q6 audit sweeps were not run** — only the `A-082` one that gate (e) named. Listing them
  without running them is deliberate: they belong to a gap audit, not to a lesson pass.
