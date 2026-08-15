# V13 — INTERPRETATION

`Bootcamp1 Wk5 041512 Part1 (65mins).swf` · 2012-04-15 · course author 100%

**Every item below is classified. `EXPLICIT` items are pointers back to
`V13_SOURCE_NOTES.md`; everything else is this session's reasoning and is labelled as such.**

| Grade | Meaning |
|---|---|
| `EXPLICIT` | The lesson says it in words |
| `VISUAL` | A frame shows it; the audio does not say it |
| `IMPLIED` | The lesson does not say it, but says something that entails it |
| `INFERRED` | This session's reasoning. **Not the course's.** Never codeable on this basis |
| `UNRESOLVED` | The lesson raises it and does not settle it |

---

## Q1 — ⭐ DOES V13 RESOLVE `A-084`, THE RSI-SMOOTHING BLOCKER?

**ANSWER: NO. It NARROWS it materially and it does not close it. `A-084` REMAINS AN ACTIVE
BLOCKER and V11's RSI threshold claims STAY BLOCKED.**

This is the question the `V13 GATE` carry-forward (a) put to this session, and it is answered
first because the temptation to answer it the other way is the largest single hazard in the
lesson.

### What `A-084` requires, quoted from the record

> *Either (a) a statement that the plotted line **is** the RSI — which would set `k = 1`, make
> `O2 ≡ 0` by construction and unblock V11's RSI half **immediately** — or (b) a smoothing length.*

### What V13 supplies · `EXPLICIT`

`[00:54:51]`–`[00:55:43]`, in the ASR-corrected form both engines give (`V13_TRANSCRIPT.md`
VERIFICATION corrections 1–2):

> *"here's the weakness with **any** indicator. **The indicator averages back**, in this example,
> **RSI is typically 14, we have it set to 21. It only looks back 21 periods.** … How come **this
> didn't rise very high**? There could be a level of rise in the price, but **because it only looks
> back, it's limited in what it sees**. If you compare this whole structure to the low down here,
> then yes, **it should plot higher**. But it may not, because it only looks back 21 hours."*

### The case FOR closure — stated at its strongest, because it must be beaten, not ignored

1. `INFERRED` — **He explains a PLOTTED LINE's HEIGHT by the RSI's LOOKBACK.** *"this didn't rise
   very high"* and *"it should plot higher"* are statements about **the line on screen**, and the
   entire causal account offered is *"it only looks back 21 periods"*. If the plotted line were an
   `MA_k` of the RSI, the natural explanation of a suppressed peak would be **the smoothing**, and
   he does not mention any.
2. `EXPLICIT` — **He names the plotted line "the RSI line."** `[00:54:15]` *"TDI is the same height
   **or the RSI line is the same height**"*; `[00:51:31]` *"**Separation between blood and RSI**"* —
   `blood` (the signal line) and `RSI` are the two things that can separate, i.e. **`RSI` is one of
   the plotted lines, not an unplotted input.**
3. `EXPLICIT` — **He speaks in the first person about configuring it**: *"we have **it** set to
   21"*. He is describing **this deployment**, not the RSI in general.

### Why that is NOT ENOUGH — four defeaters, each independently sufficient

1. `INFERRED` — ⭐ **THE LOOKBACK ARGUMENT DOES NOT DISCRIMINATE.** `MA_k(RSI(21))` **also** only
   sees 21 periods of price, because its input does. **Every sentence in the passage is equally
   true of the smoothed series.** The passage explains a property the two candidates SHARE, so it
   cannot distinguish them. *This is the defeater that matters, and it is the one a session hoping
   for closure would most want to miss.*
2. `EXPLICIT` — ⚠ **"The indicator averages back" is, if anything, evidence in the OTHER
   direction.** It is the only clause in the passage that mentions averaging at all, and it is
   applied to *"the indicator"*, not to the RSI's own internal averaging. **It is too vague to
   ground either reading**, and a session that read it as *"the RSI averages"* would be choosing
   the convenient parse of an ambiguous one.
3. `EXPLICIT` — **He treats `TDI` and `RSI` as two things a trader chooses BETWEEN.** `[00:55:58]`
   *"**if you don't like TDI, then use the RSI.** RSI is very cool. In fact I used the RSI for a
   long time… **TDI was cleaner** for good signals."* A speaker who held *the green line simply IS
   the RSI* has just described switching from a thing to itself.
4. `EXPLICIT` — ⚠ **The passage contains an arithmetic error the speaker does not catch**, and it
   is inside the very sentences a closure would rest on: *"on a one hour chart, **it looks back 15
   hours**"* `[00:55:07]` against *"it only looks back **21 hours**"* `[00:55:28]`. **Both ASR
   engines transcribe both.** `D-030` does not permit a blocker to be closed on a passage whose own
   numbers do not agree twenty-one seconds apart.

### `VISUAL` — and the frames close the other route too

**No indicator-properties dialog and no Navigator panel appears in any of the 793 swept frames**
(`V13_SOURCE_NOTES.md` §7.2). ⭐ **And the frames add a durable negative that is worth more than
this lesson:** the sub-window legend reads **`TDI_MMM 46.2640 42.8277 40.2789`** — **name and
current values, no parameter tuple**. This is MT4's behaviour for this `TDI_MMM` deployment, whose
short name omits its inputs. **CORRECTED 2026-08-15, item 154:** V10's separate
`Traders Dynamic Index Visual` build prints six current values and no tuple. The legend route is
empirically dry across both observed builds, but is not deductively closed for every possible build.
The remaining routes are exactly three: a properties dialog, a Navigator/inputs tab, or a spoken
identity statement.

### Disposition — recorded as `A-087`

```text
A-084 -- STILL AN ACTIVE BLOCKER. DO NOT CODE.
V11's RSI threshold claims STAY BLOCKED. PT-040's MATERIAL verdict is undisturbed.

A-084 NARROWS on three counts, none of which is closure:
  1. RSI period 21 is now corroborated from a SECOND lesson, first-person,
     as a configuration choice. A-080's closure is strengthened.
  2. The 21 is confirmed to be a LOOKBACK IN CHART PERIODS, scaling with
     timeframe -- not a wall-clock window. This constrains any future test.
  3. The legend route is CLOSED for the whole corpus, which redirects the
     V14-V21 hunt to dialogs and speech only.
```

> ⚠️ **A NOTE ON HOW THIS SESSION EXPECTED TO ANSWER THIS QUESTION.** The `V13 GATE` briefing called
> this *"the cheapest remaining unblock in the project"* and named V13 as the place it could land.
> The passage at `[00:54:51]` is, on first hearing, exactly the sentence that was being hoped for.
> **It is being declined on defeater 1, which is a point of construction, not of caution.** The
> same shape as V12's own headline: a session that closed `A-080` and reported that closing it did
> not unblock what it was meant to.

---

## Q2 — WHAT DOES THIS LESSON ACTUALLY CONTRIBUTE?

`INFERRED` — **It is the corpus's first ASSESSMENT, and its value is of a different kind from a
lesson's.** Weeks 1–4 taught; V13 asks nineteen questions about weeks 1–4 and prints the answers.
Three consequences:

1. `IMPLIED` — ⭐ **The answer slides are the instructor's own compression of four weeks of
   teaching into one line each.** Where a prior lesson gave a rule across ten minutes of
   qualification, V13 gives the version he considers **the answer**. That is materially different
   evidence from a re-statement, and it is why §4 and §5 of the source notes quote the slides
   verbatim rather than summarising them.
2. `IMPLIED` — **It is a redundancy check on this project's own reading of V01–V12.** Every answer
   is independently checkable against what earlier artifacts recorded. **The one that matters most
   is the safety trade**: V10 recorded nine printed rules with a `25–75` anchor distance, and V13
   prints `25 to 75 pips` again, in a different deck, five weeks later. **C-017 and the V10 anchor
   record are corroborated from an independent slide.** `EXPLICIT` + `VISUAL`.
3. `IMPLIED` — **It supplies a homework instrument that needs no invention.** See Q5.

---

## Q3 — ⚠ THE STOP-LOSS QUESTION, AND THE `A-082` TRAP

`COURSE_PROGRESS.md` V13 GATE (c) named *"the `A-082` class of error"* as **the V13/V14 audit
item**: adopting a number from a context that does not license it. This lesson contains a live
instance and it is recorded before it can be made.

| What the lesson gives | `[ts]` | Grade | Is it a method stop? |
|---|---|---|---|
| *"Use a **25 or 30 pip** stop loss, no limit order"* | `[00:19:04]` | `EXPLICIT` | ❌ **NO** |
| *"**Stop loss goes below the low**"* | `[00:48:12]` | `EXPLICIT` | ✅ Placement rule |
| *"**Stop loss goes below the day.** Everybody knows that" | `[00:59:19]` | `EXPLICIT` | ✅ Placement rule |
| *"why not **scratch yourself out with 10 or 12 pips** instead of giving the dealer 25"* | `[00:33:00]` | `EXPLICIT` | ❌ An **exit-early** rule, not a stop |
| *"your stop should be **a break even**"* | `[00:35:52]` | `EXPLICIT` | ❌ Inside a worked example |

> ### ⭐ WHY `25 or 30 pips` MUST NOT BE ADOPTED AS THE METHOD'S STOP
>
> **The speaker disqualifies it himself, four times in thirty seconds**, `[00:19:07]`–`[00:19:37]`:
> *"It's not about a stop loss and a take profit, **it's not about those items**"*; *"Just throw a
> 30, 25, 30-pip stop loss on there and **don't worry about it**"*; *"**I don't care about that
> stuff for the drill. I don't care about it for the drill.**"* And the printed slide says it too:
> *"**It is not about these items!**"*
>
> **It is a placeholder chosen so the drill can run without the student thinking about stops.**
> Adopting it would be `A-082`'s exact shape — a real number, really printed, really spoken by the
> author, in a context that explicitly denies it authority.

`INFERRED` — **The method's actual stop-loss doctrine is STRUCTURAL, not numeric**: *below the
low*, *below the day*. **This is the first stop-loss placement material in the corpus since V10 was
recorded as containing none.** It is **not** a distance and must not be turned into one — doing so
would violate the hard rule against converting subjective/structural course language into a numeric
constant.

---

## Q4 — THE PRINTED-VS-SPOKEN CONFLICTS · `UNRESOLVED` → `C-020`

Two, on the same slide, and they are **different in kind**:

| # | Printed | Spoken | Character |
|---|---|---|---|
| 1 | shadow box *"3 to 4 am **NYYC**"* | *"3 to 4 a.m. New York… **I'm sorry**, 3 to 4 a.m. **London**"* | **A live self-correction.** The speaker audibly notices the slide is wrong and fixes it |
| 2 | stop-hunt box *"**25 to 50**"* | *"**25 at the bottom or start? 50 pips on the top side of the range**"* then *"**It's a 25 pip box. 25 pips away from the top or bottom**"* | **A muddle he does not resolve.** He offers an asymmetric reading (25 bottom / 50 top), then flatly restates a symmetric 25 |

`INFERRED` — **Conflict 1 is arguably resolvable and this session does NOT resolve it.** The
*"I'm sorry"* is strong evidence the spoken London figure supersedes the slide, and
`SOURCING_HIERARCHY.md`'s *"the recording wins"* would ordinarily apply. **It is left open anyway,
because the slide is also Tier 1** and because 3–4 AM London and 3–4 AM New York are **five hours
apart** — a silent adoption of either would put a box on the wrong side of a session. `D-030`
binds: a definition is never approximated.

`INFERRED` — **Conflict 2 is NOT resolvable from this lesson.** The asymmetric and symmetric
readings are both his, thirteen seconds apart, and the slide's *"25 to 50"* is consistent with
**either** a range or an asymmetry. Recorded, not adjudicated.

---

## Q5 — HOMEWORK: THE LESSON SUPPLIES ITS OWN INSTRUMENT

`EXPLICIT` — **The lesson IS an exam, and it prints both the questions and the answers.** No
assignment needs to be invented or approximated, which is a first in this corpus.

`INFERRED` — the honest way to use it is to **sit the exam closed-book from the question slides
and the corpus's own prior artifacts, grade against the printed answers, and preserve the first
attempt including every wrong answer** (`STUDY_PROTOCOL.md` step 6). See
`05_HOMEWORK/V13/`.

`EXPLICIT` — the lesson also sets forward work that this session **cannot** perform: `[00:23:28]`
widening the TDI drill to ten pairs, and `[00:22:56]` *"another blindfolded drill"* which is
**not specified in this file**.

---

## Q6 — ⭐ THE MISSING WEEK 6, AND WHAT THIS LESSON SAYS ABOUT IT

Flagged for the **V14 hard-stop gap audit**.

| Evidence | Grade |
|---|---|
| `[00:01:55]` *"There's going to be **no boot camp next week**"* | `EXPLICIT` |
| `[00:05:20]` *"Next session is going to be **Sunday the 29th**. That's two weeks"* — 2012-04-29 | `EXPLICIT` |
| `[00:05:33]` *"we'll get started again with **week six through ten** or six through — **I don't know how many we're going to do yet**"* | `EXPLICIT` |
| `SOURCE_MANIFEST.md`: the next file is `Bootcamp1 Wk7 050612` — **2012-05-06**, three weeks after this session | — |

`INFERRED` — **this is a real constraint on the gap audit and it is deliberately under-stated.**
The lesson establishes that **a scheduled two-week break falls exactly here**, that the instructor
did not yet know the remaining week count, and that the announced return date (**04-29**) is **one
week before the next surviving recording (05-06)**. `UNRESOLVED` — **that is consistent with
"Week 6 was recorded on 04-29 and is missing from this corpus" AND with "the break ran long and
Week 6 never happened."** ⚠ **Nothing here decides between them, and no session may fabricate,
interpolate, or infer Week 6 content on the strength of it.** The value is that **V14 now has a
specific, cheap thing to listen for**: any V14 statement about the return date or the week
numbering.

---

## Q7 — THE TIMEFRAME-INVARIANCE CLAIM · `EXPLICIT`, AND SELF-FENCED

`[00:57:45]` *"**I mixed them up.** The first one's a 15 minute. The second one's a four hour and
the third one's a one hour. **It's the same shit. I wanted to trick you.**"* — a deliberate
pedagogical experiment, and the strongest form of the claim in the corpus so far.

⚠ `EXPLICIT` — **the speaker fences it himself**, `[01:04:38]`: *"I don't want you to go, oh,
since there's no difference, **I'm going to start trading in one minute. It's not what I'm telling
you.**"*

⚠ `EXPLICIT` — **and he gives the chart ORDER two different ways.** `[00:57:50]`: 15m, 4h, 1h.
`[01:04:10]`: *"They were 15 minutes, four hours, and one hour"* — same order — but `[01:04:03]`
prefaces it *"**The last one was one hour**"* while also saying *"I'm not sure if it was E.J. …
**I forgot. I was looking at so many of them.**"* `UNRESOLVED` — **which chart is which timeframe
is not reliably recoverable**, and the three committed TDI frames are therefore **not** labelled
with timeframes in `04_SCREENSHOTS/V13/INDEX.md`.

`INFERRED` — **the claim is not testable as stated and is not being turned into a test.** *"The
patterns look alike across timeframes"* is a claim about visual similarity, not about a measurable
edge. Recorded, not coded. Related: `A-039`.

---

## Q8 — WHAT IS SAFE TO CODE FROM THIS LESSON

`INFERRED` — this session's judgement, offered for R1 to overrule.

| Item | Codeable? | Why |
|---|---|---|
| Bias duration `2–3` days after PF | ❌ Not on V13's authority alone | Depends on `peak formation` being detectable; `A-010` narrowed but not closed |
| Evaluation window `3–5` days | ⚠ As a **parameter**, yes; as a **rule**, no | It is a statement about how the instructor looks at charts, not a signal condition |
| Vacate rule — *"dealer hits the level again and closes above/below on 15m"* | ⚠ **Closest thing in the lesson to a codeable exit** | Turns on `the level`, which is `A-039`-adjacent and not independently defined here |
| Safety-trade anchor `25–75 pips` | ❌ | Corroborates V10; still gated on `peak formation` + `level one consolidation` |
| Stop-hunt box distance `25` / `25–50` | ❌ | `C-020` |
| Shadow box / Brinks times | ❌ | `C-020` on the shadow box; Brinks `3:45`/`9:45` is clean but is a **template setting**, not a signal |
| Blue box stop-paint `1 AM NYC` | ⚠ Template setting, clean, and **already `D-031`-relevant** | Not a signal |
| TDI levels `63 / 50 / 37` | ❌ | `VISUAL` only, and `A-086` blocks band construction regardless |
| RSI period `21` | ❌ **still** | `A-084` |
| Range arithmetic (5.10) | ✅ **as a pre-registered TEST, not as a rule** | `PT-041` |
| Timeframe invariance | ❌ | Q7 |
| `25 or 30 pip` drill stop | ❌ **and emphatically** | Q3 |

---

## Q9 — CONFIDENCE IN THE SPEAKER DETERMINATION

`EXPLICIT` — **100% course author, HIGH confidence, over-determined.** Eight non-acoustic strands,
zero handover language across a 17-pattern superset returning a single non-handover hit, and
twenty-nine third-party names of whom **none speaks**.

`INFERRED` — **the V13 GATE (b) worry was well-founded and did not materialise.** A new week and a
new date is genuinely the condition under which this corpus's author runtime has broken before
(100% V03 → 31% V04 → 0% for five lessons → 100% V10). It was tested on strands fixed in advance,
**without** the cross-file acoustic screen, which remains prohibited per V07's ruling. **The
run of course-author lessons now stands at four (V10, V11, V12, V13).**

---

## Q10 — WHAT THIS SESSION COULD NOT DO

| Limitation | Consequence |
|---|---|
| `I-008` — **no full independent re-transcription.** Five spot-checks, 7.9% of runtime | The transcript is adopted on partial verification, as for every lesson except V01/V05 |
| **§9 ordering broken** — frames were viewed before the source notes were written | Disclosed in `V13_SOURCE_NOTES.md` §0; every item tagged; open item for R1 |
| **The sweep frames are not committed** | The *"no properties dialog in 793 frames"* claim is **not** repository-verifiable — only the 29 committed frames are. Same limit V12 R1 recorded at item 140 |
| **No archival mp4** | The real-time pass (§3) was not run. Screenshots-only, per the §10 default |
| **The `25 to 50` vs `25` conflict cannot be settled** | `C-020` stays open |
| **Nothing here unblocks `A-086`** | Band construction is still impossible; `shark fin` and `blood in the water` are still not testable, despite this lesson using them ~20 times |
