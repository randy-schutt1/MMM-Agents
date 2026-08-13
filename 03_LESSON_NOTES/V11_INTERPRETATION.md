# V11 — INTERPRETATION NOTES

> **NOTHING IN THIS FILE IS INSTRUCTION.** It is this session's reading of what
> `V11_SOURCE_NOTES.md` records. Where the two appear to disagree, the source notes govern and the
> disagreement is a defect here (`D-008`). Every machine candidate is fenced under `D-010` and
> carries `NOT A COURSE RULE`.

**Confidence grades:** `HIGH` = the lesson states it and I can quote it · `MEDIUM` = a reading the
text supports and does not compel · `LOW` = my inference, flagged as such · `BLOCKED` = cannot be
resolved from the course (`D-030`).

---

## Q1 — What is V11 actually FOR, and what does it add to the corpus?

**Answer: two things, and they sit in different registers.**

**(a) It re-states the entry protocol with more force and more repetition than any prior lesson,
and adds nothing new to it.** §3 of the source notes lists eight statements of the same rule.
`[00:36:19]` is the tightest composite the corpus has: *"if it's 25 to 50 pips below the blue box
and the TDI or RSI is in the extreme 80 to 90 range and it gives me the formation, I got a pretty
good trade."* Every component of that sentence already exists in V02–V10. **The contribution is
emphasis, not content** — this is a lesson delivered in reaction to a mailbag, and it says so:
`[00:21:02]` *"After I read the same email I was pissed off for two days."*

**(b) It teaches the RSI substrate of the TDI, at length, for the first time in the corpus.**
`A-039` has stood since V04 as *"TDI — displayed, not taught."* **That is no longer accurate.**
V11 spends 25 minutes on why RSI is used, what its baseline means, what the 80/40 and 60/20 ranges
are, how the range switch signals a trend change, how peak formations appear *inside* the
indicator, and what divergence and hidden divergence look like. Six of those points are **printed
as well as spoken**.

**Confidence: HIGH** on both halves.

> **The asymmetry between (a) and (b) is the useful observation.** The half of the lesson that is
> most *codable* — the RSI numbers — is the half that is **least connected to the entry rule**. The
> RSI section states thresholds and never states an entry; the entry section states an entry and
> never states a threshold. `[00:36:19]` is the one sentence that joins them, and it joins them
> with *"the formation"* — an undefined term. **The lesson is two well-specified halves welded by
> an unspecified joint.**

---

## Q2 — ⭐ *"There's the mayonnaise. There's the 50."* — does V11 overturn `A-020`?

**Answer: I do not know, and I am not going to decide. `C-018` is opened and left open.**

This is the most consequential sentence in the lesson for the corpus, because
`SOURCING_HIERARCHY.md` §3.4 names `A-020` as one of **three highest-priority reconciliation
targets** — records closed on Tier 2 that a later video can overturn — and instructs that any
lesson touching the moving-average set **must** re-check them. V11 touches it.

### The standing position

`A-020` is **CLOSED** as `Mayo = 200`, on **owner attestation 2026-08-13** plus `MMM-NOTES` p.66
(*"Hold the Mayo – 200 Bounce"*). The record itself is emphatic that this is **not**
`RESOLVED BY COURSE`, and its *Required Research* asks for *"a screenshot showing the chart's
indicator list or a labelled average, at a timestamp where he says the word."*

**V11 `[00:46:45]` is the first timestamp in the corpus where he says the word AND a chart is on
screen.** That is exactly the condition `A-020` asked for, which is why this had to be run down
rather than noted in passing.

### Why the sentence does not settle it

The audio is not in doubt — the ASR and Whisper `small.en` produce the same seven words. **The
grammar is in doubt.**

| Reading | Parse | Implies |
|---|---|---|
| **Apposition** | *"There's the mayonnaise[ — that is], there's the 50"* | **Mayo = 50.** Contradicts `A-020` |
| **Enumeration** | *"There's the mayonnaise[,] there's the 50"* — two lines being pointed at in turn | **Mayo ≠ 50**, and `A-020` is untouched |

Three considerations, and they do not point the same way:

1. **The plural cuts toward enumeration.** The sentence opens *"Look where the **averages** are"*
   — he is directing attention to more than one line, and the frame shows at least four. Listing
   two of them is the natural continuation.
2. **The immediate context cuts toward a DIFFERENT "50" entirely, and this is the strongest point
   against reading the sentence as a mapping at all.** Seven seconds later, `[00:46:52]`:
   *"Remember I told you **there's the 50**. RSI will find resistance where? Around 60."* That
   *"the 50"* is unambiguously the **RSI market baseline**, which he has just spent fifteen minutes
   on (§4b). **The phrase *"the 50"* is, in this lesson, overwhelmingly a sub-graph object: it
   occurs 14 times and all the unambiguous ones are the RSI baseline.** If `[00:46:45]`'s *"the
   50"* is also the baseline, the sentence maps nothing — it points at a price-pane average and
   then at a sub-graph line, in one breath, while explaining how he reads a downtrend from both
   panes at once. Which is precisely what he is doing.
3. **The frame cannot arbitrate.** `04_SCREENSHOTS/V11/INDEX.md` §4 reports this as a negative
   result: four averages, no legend, no settings dialog, no period label. `A-020`'s *Required
   Research* is **still unsatisfied**.

### Disposition

**`SOURCING_HIERARCHY.md` §3.2 Case C — genuine conflict, do not adjudicate.** `C-018` is opened,
tagged `MMM-NOTES` vs the course author, carrying both the page and the timestamp.

**What this session explicitly does NOT do**, each named because each is a live temptation:

- It does **not** reopen `A-020`. A record closed by owner attestation is not reopened by an agent
  finding an ambiguous sentence.
- It does **not** re-close `A-020` as `Mayo = 50`. That would be adopting reading 1 on no better
  evidence than reading 2.
- It does **not** blend — *"mayonnaise is the 200, and he also calls the 50 the mayonnaise
  sometimes"* is a composite no source states, and §3.1 forbids it in terms.
- It does **not** invoke §3.3's *"the recording wins"* as decisive. **That rule says which source
  is superseded when they conflict; it does not manufacture a determinate reading out of an
  indeterminate recording.** `C-011` established exactly this asymmetry, and the note there —
  *"a session that treats a won contradiction as licence to adopt whatever Tier 1 fragment is
  nearest has made the `D-030` error by another route"* — is the governing precedent.

**Confidence: HIGH that the conflict is real and must be recorded. BLOCKED on its resolution.**

**Cheap next step, recorded for whoever takes it:** V12 is the same session, same day, same charts,
and is 55 minutes long. If the nickname recurs there with a legend visible, `A-020`'s *Required
Research* is one frame away.

---

## Q3 — The printed *"Parameters of RSI"* slide omits the period. How much does that block?

**Answer: everything on the indicator side. All six RSI thresholds are uncodable, and that is not
a technicality.**

RSI is not a parameter-free object. RSI(2), RSI(9) and RSI(21) on the same GBP/USD chart cross 50
at different bars, spend wildly different fractions of their life above 80, and produce different
divergences. **A threshold without a period is not a rule; it is half of one.** *"Above 80 is
overextended"* is a claim about RSI(*n*) for some *n*, and the lesson never says which.

The near-miss is what makes this worth a record rather than a footnote. The slide is **headed**
*"Parameters of RSI"* and lists **six numbered parameters**. A session skimming for a parameter
block finds one — and it contains the ranges and not the lookback. **This is the shape of failure
`D-030` exists to prevent, and it would have been an easy one to walk into.**

**The hierarchy was run to exhaustion (`D-040`):**

| Tier | Result |
|---|---|
| **1 — the course** | Silent. 33 `rsi` tokens, no period; no frame shows a settings dialog or legend |
| **2 — `MMM-NOTES`** | **Also silent.** The extract describes the TDI's four components (RSI line, signal line, market baseline, volatility bands) and their *uses*, with no lookback for any of them |
| **3 — web** | Not consulted for a value, and **could not close anything if it were** |

**`A-080` is opened, status `DO NOT CODE`.** The Tier 2 negative is recorded as a positive finding
per §2 step 3 — a silence in both admissible tiers is real evidence that the number was carried in
the room, on a chart everyone could see, and is not recoverable from this corpus.

> **The obvious wrong move, refused in advance.** The TDI indicator's widely-distributed default
> is RSI period 13. It would be easy, and it would be **`D-030`'s exact prohibition**: importing a
> number from outside the course to make a blocked test runnable. It is also not even safely
> *outside* — `MMM-NOTES` p.38 lists a **13 EMA** in the moving-average set, so a session could
> talk itself into "13" by confusing two different indicators. **No period is adopted. V11's
> dimension B contribution on the RSI side stays BLOCKED.**

**Confidence: HIGH.**

---

## Q4 — What in V11 is genuinely testable, and what is not?

**Answer: one claim, and it is not the entry rule.**

### Not testable, and why

| Claim | Blocker |
|---|---|
| The full entry protocol (§3.8) | Needs `blue box` (`A-076`), `second leg` (`A-007`), *"the formation"*, and an RSI period (`A-080`). **Four undefined terms in one sentence** |
| Every RSI threshold (80/40, 60/20, 80/20, the 50) | `A-080` — no period |
| The three-touch level mechanism (§4h) | `the level` (`A-004`). The mechanism is a *causal story*, and the corpus has no way to locate its subject |
| *"Trend acceleration"* mean-reversion (§4f.4) | *"separates away from moving averages"* — which averages, and how far? Neither is stated |
| Divergence and hidden divergence (§4g) | `A-080`, plus no stated lookback for the swing comparison |

**This is the majority of the lesson, and the honest report is that most of V11 is untestable
today.** It is reported with equal prominence to what *is* tested, per
`BACKTEST_EVIDENCE_STANDARD.md` §4.3 and `E25`.

### Testable — the hold-duration claim

> `[00:14:25]`–`[00:14:39]` — *"Understand that **the low has to hold. How long? 30 to 90
> minutes.** … the **long sideways consolidation should last up to two hours. Then calmly take a
> trade.**"*

This is a claim about **elapsed clock time between a low being made and that low being broken**.
Both quantities are directly observable in OHLC data with no indicator, no pattern recognition,
and no undefined term — **provided the candidate low is defined by something the course supplies
rather than by the agent.**

**The operationalisation, and its honest limit.** The lesson's *"the low"* is a candidate for the
**low of the day** — `[00:04:30]` *"anticipate the low of the day"*, `[00:13:22]` *"before the
lower [low] of the day … have locked in"*, and the hand-written **`LOD`** at frame `07:45`. So
*low of the day* is the course's own object here, not the agent's. What the course does **not**
supply is which *candidate* lows count — his are lows made after a stop hunt out of the blue box,
and `A-076` blocks that filter.

**`PT-037` therefore tests the claim's INFORMATIONAL CONTENT, not the instructor's setup**: given
a running session-day low that has held for *T* minutes, how does `P(this is the day's final low)`
behave as *T* crosses 30, 90 and 120? **If the durations he names carry no information about
whether a low is final, the claim is contradicted in the only form in which it is decidable. If
they do, that supports the claim and does not validate the setup**, because the setup's filter is
absent. Both directions are stated in `PT-037` §8 before the run.

**Confidence: MEDIUM** on the operationalisation being fair — it is a real narrowing of what he
said, and it is disclosed rather than smoothed.

---

## Q5 — Does V11 advance `A-011` (M/W anatomy)?

**Answer: it narrows it and does not close it, and the lesson says so itself.**

V11 adds three genuinely new constraints: the formation **must have a pullback and another leg**
(§3a.1); it must be **aggressive and big**, and *"if the formation doesn't look like that, it's a
gamble"* (§3a.3); and the negative case is named — *"a tiny tap off the low"* is not one (§3a.4).
It also supplies a **mechanism**: the pullback exists to hit the shorts' stops and induce longs,
which the dealer then also stops out (§3a.2).

**What is still missing is what `A-011` has always been missing: a leg count, a size measure, and
an invalidation rule.** *"Aggressive and big"* is a comparative with no comparator. And the lesson
defers the topic explicitly: `[00:10:18]` *"How many times have I explained the M&W? **I'm gonna
do it again next week.**"*

**`A-011` narrows — `SOURCING_HIERARCHY.md` §3.2 Case D. It does not close.** Under `D-030` the
M/W-dependent tests stay blocked, and V12/V13 is where the forward pointer lands.

**Confidence: HIGH.**

---

## Q6 — V11's *"confirmation of the safety trade"* vs V10's safety trade — same object?

**Answer: probably, and the corpus should not assume it.**

V10 defines the safety trade in the **price pane** (`V10_SOURCE_NOTES.md` §6). V11 `[00:33:19]`
defines *"the confirmation of the safety trade"* in the **sub-graph**: RSI comes off the bottom,
crosses the 50, pulls back to *"imaginary support slightly below the basis line"* around 38–42, and
turns back up.

Two readings. **(i)** They are the same trade seen in two panes — V11 is supplying the indicator
signature of V10's price pattern, which is exactly what a lesson on *"using the TDI for
confirmations"* `[00:26:04]` would be expected to do. **(ii)** *"Safety trade"* names a different
object in each.

I read **(i)** as much more likely, on three grounds: the shared *"day one, day two safety trade,
day three"* sequencing (`[00:33:51]`), the shared level-one/two/three vocabulary, and the word
*"confirmation"* itself, which presupposes something already identified elsewhere.

**But I am not merging them.** `A-083` is opened to record that V11 supplies an indicator-side
confirmation for an object V10 defined in the price pane, and that **the corpus has not verified
they are the same object**. Merging two lessons' definitions into one composite is the drift
`D-008` and `REVIEW_PROTOCOL.md` §17 failure mode 3 name, and it is cheap to avoid by writing the
uncertainty down. **In any case it changes nothing operationally**: both are blocked by `A-080` and
`A-076` respectively.

**Confidence: MEDIUM** on (i), **HIGH** on the decision not to merge.

---

## Q7 — What is the speaker doing at `[00:43:29]`, and does it matter?

**Answer: he is contradicting his own slide deck on screen, and it matters for provenance.**

The `POSITIVE TREND` / `NEGATIVE TREND` slides describe stage 3 as *"Begins Upside Acceleration"* —
i.e. **acceleration as trend confirmation**, the conventional reading. The speaker reads that off
the slide and then rejects it: *"**they call that** upside acceleration, trend acceleration. **But
we know better as a group: trend acceleration is a sucker's play.**"* `[00:43:42]` supplies his
alternative: acceleration is the dealer separating from the averages to catch latecomers, and *"then
the dealer applies the brakes."*

He also disowns the deck's provenance in advance: `[00:42:41]` *"this thing was written maybe 15
years ago. **I'm not even sure these slides came from that guy** I really like."*

**Two consequences, and the second is the one that generalises:**

1. **The slide's stage-3 semantics are NOT this course's doctrine.** A future session mining
   `04_SCREENSHOTS/V11/` for printed rules would find *"Begins Upside Acceleration"* in a clean
   printed frame and could reasonably take it as taught. **It is taught and then repudiated, 50
   seconds later, in audio only.**
2. **`PRINTED` is not automatically stronger than `AUDIO` in this corpus.** The project's basis
   tags carry no ranking, and this is the case that shows why one must not be assumed: here the
   printed artifact is **third-party material of uncertain origin that the course author
   disagrees with**, and the audio is the doctrine. Recorded in `V11_SOURCE_NOTES.md` §4f and
   flagged for the reviewer.

**No `C-xxx` is opened.** A speaker disagreeing with a slide he is presenting *and saying so* is
not a contradiction in the method — it is the method being stated. `C-xxx` is for incompatible
claims both asserted.

**Confidence: HIGH.**

---

## Q8 — What is the strongest reason to doubt this session's reading of V11?

Three, ordered by how much they would cost if right.

1. **I may be wrong about `[00:46:45]`, in the direction of excessive caution.** A reader hearing
   the audio might find the apposition reading obvious and think `C-018` manufactures doubt to
   avoid a decision. **My defence is `[00:46:52]`** — the same phrase, seven seconds later,
   demonstrably meaning the RSI baseline — and that is a fact about the transcript, not a
   preference. But I hold this at **MEDIUM**, and a reviewer who listens to the clip and finds the
   intonation decisive should say so; that would be better evidence than anything I have.
2. **`PT-037`'s operationalisation may be a strawman.** Testing *"does a session-day low that has
   held T minutes tend to be final"* is a weaker, more general claim than *"the stop-hunt low out
   of the blue box has to hold 30–90 minutes."* If the general version fails, that is **not**
   evidence the specific version fails. §8 of `PT-037` states this before the run, and the mastery
   report must not let the caveat drift.
3. **I may be over-reading the RSI section's completeness.** It is 25 minutes and six printed
   slides, which *feels* like a full treatment — but the TDI's own components (signal line,
   volatility bands) are promised at `[00:32:34]` and **not delivered in this file**. If V12
   delivers them, V11's RSI section is a prologue, not a lesson, and calling it *"the first real
   teaching of the TDI substrate"* over-credits it. **`A-039` is narrowed, not closed**, partly
   for this reason.

---

## Q9 — Machine candidates, recorded and fenced

`D-010`: these are **`INFERRED MACHINE CANDIDATE` / `NOT A COURSE RULE` / `DO NOT CODE`**. They are
written down so a later phase has a record of what was *considered* and rejected, not so it can be
picked up.

| # | Candidate | Fence |
|---|---|---|
| MC-1 | `low_confirmed := (now − t_low) ≥ 30 min` | **NOT A COURSE RULE.** The lesson gives a *band* (30–90) and a *different* number for the sideways case (120). Collapsing three numbers into one threshold is the `D-010` failure |
| MC-2 | `rsi_bias := RSI(n) > 50 ? up : down` | **DO NOT CODE — `n` UNDEFINED (`A-080`)** |
| MC-3 | `overextended := RSI(n) > 80 or < 20` | **DO NOT CODE — `A-080`** |
| MC-4 | `regime_switch := oscillation band moves 80/40 → 60/20` | **DO NOT CODE — `A-080`, and "oscillation band" has no stated estimator** |
| MC-5 | `entry_distance ∈ [25, 50] pips beyond box` | **DO NOT CODE — `A-076`.** Unchanged from V02/V04; V11 adds no measurement rule |
| MC-6 | `touch_count == 3 at a level → expect reversal` | **DO NOT CODE — `A-004`** |

---

## Q10 — Confidence summary

| Reading | Grade |
|---|---|
| The lesson is a mailbag-driven restatement of the entry protocol plus a first teaching of RSI | **HIGH** |
| Single speaker, course author, 100% | **HIGH** |
| The 25–50 pip / second-leg / outside-the-box protocol is restated and unchanged | **HIGH** |
| The six printed RSI ranges are stated exactly as recorded | **HIGH** (print + audio + a second ASR engine) |
| **No RSI period is supplied by Tier 1 or Tier 2** | **HIGH** (as a negative) |
| The hold-duration claim is `30–90 min`, with a `2 h` sideways variant | **HIGH** |
| `[00:46:45]` conflicts with `A-020` | **HIGH that a conflict exists** |
| Which reading of `[00:46:45]` is right | **BLOCKED** |
| V11's *"confirmation of the safety trade"* is V10's safety trade in the sub-graph | **MEDIUM** |
| `A-011` narrows but does not close | **HIGH** |
| `A-039` narrows from *"displayed, not taught"* but does not close | **HIGH** |
| `PT-037`'s operationalisation is a fair narrowing of the claim | **MEDIUM** — disclosed as such |
