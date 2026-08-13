# V10 — HOMEWORK

| Field | Value |
|---|---|
| Lesson | V10 · `Bootcamp1 Wk3 040112 (96mins).swf` · session 2012-04-01 |
| Assigned at | `[01:34:26]`–`[01:34:51]`, **printed** at frame `01-34-27` |
| Speaker | the **course author** (100% of V10's runtime) |
| Data source | **HistData GBP/USD M1 corpus** (`D-036a`), QA gate `PASS` · **not** TradingView/FXCM, because the window is 2013–2016 which that feed cannot reach (`D-035`, `D-036`) |
| Instrument | **GBP/USD** (`D-007`) |

---

## THE ASSIGNMENT, AS PRINTED

> **`R&D`**
> *"Finish flash cards — you should build your book every week by adding a few snapshots"*
> ***"Mark 10 Safety setups in any pairs / 5 long / 5 short"***
> *"Post in the forum for review."*
> *"I will try to organize the forum better going forward"*

Spoken addendum, `[01:34:36]`: *"if it's too easy, five and five and five — so easy, increase it."*
Standing from prior weeks (`§4` of the source notes): 4-hour chart markups, and the first-eight-hours
lines extended across the week.

---

## DISPOSITION SUMMARY

| Item | Disposition | Basis |
|---|---|---|
| **H1** — finish flashcards, build the book | **DONE** — §1 | Performable: the lesson prints a completed exemplar at frame `00-34-22` |
| **H2** — mark 10 safety **setups**, 5 long / 5 short | **PARTIAL: anchors DONE, setups `DEFERRED`** — §2 | `D-019` `DEFERRED`, blocked by `D-030` (`A-076`, `A-077`, `A-007`, `A-004`) |
| **H3** — post in the forum for review | **`NOT APPLICABLE`** — §3 | `D-018`: the 2012 forum has no present-day existence. No subject matter, now or ever |
| **Comprehension probe** (not assigned; project standard) | **DONE — 12/12** — §4 | |

> **On H2's disposition, stated carefully because `D-019` turns on it.** The distinction is
> `NOT APPLICABLE` (no subject matter, closed permanently) vs `DEFERRED` (subject matter exists,
> a prerequisite is missing). **H2 plainly has subject matter** — V10 spends fifty minutes on the
> setup. It is blocked by a **definitional** gap, which `D-030` says must **wait for the lesson
> that defines it**. That is `DEFERRED`, and it stays open. **It is not `NOT APPLICABLE` and
> claiming so would silently discard performable future research** — the exact error `D-019` was
> written to prevent.

---

## 1. H1 — FLASHCARDS

The lesson prints a completed flashcard at frame `00-34-22` and states what one must contain. Its
annotation block reads, verbatim from the frame:

```text
W is False
Dealer Vectors to S/H Zone
M formation
Shark fin above Resist band
Price action above blue tracer
Multisession  M
Level 3
SELL!!!!!!!!!!!!!
```

with a terminal row beneath dated `2011.09.30 16:37` — which **corroborates** `[00:34:30]`
*"this is dated September see it"*.

**What was produced:** `V10_FLASHCARDS.md` — five cards covering V10's own rule set, in the
exemplar's format. **They are cards about the LESSON's stated rules, not about charts**, because
producing chart-based cards requires classifying setups, which §2 explains is blocked.

**An honest limit, recorded rather than glossed.** The exemplar's own lines depend on `shark fin`,
`resist band`, `blue tracer` (`A-079`), `S/H zone` and `Level 3` (`A-004`) — **five undefined
terms in eight lines.** So a faithful chart flashcard cannot presently be produced at all, and the
cards in `V10_FLASHCARDS.md` deliberately do not imitate one. **The exemplar is evidence about what
the course expects; it is not a template this project can yet fill.**

---

## 2. H2 — TEN SAFETY SETUPS: ANCHORS DONE, SETUPS DEFERRED

### 2a. Why the full assignment is not performed

`V10_SOURCE_NOTES.md` §6c lists the setup's nine printed rules; `V10_INTERPRETATION.md` Q6 reduces
them to seven conditions and finds **two codable**:

| Condition | Codable? | Blocker |
|---|---|---|
| A weekly extreme exists (PFH/PFL = HOW/LOW) | **YES** | — V10 defines it at `[01:14:06]` |
| DNC — do not counter toward the peak | **YES**, as a prohibition | — |
| Price has moved away and "confirmed" (the lock) | **NO** | **`A-077`** — no distance, no duration, anywhere |
| Level-one consolidation is clear | **NO** | `consolidation` undefined; `A-004` |
| Visible stop hunt, preferably outside the blue box | **NO** | **`A-076`** — and V10 states **no session clock time at all** |
| Second leg M or W | **NO** | **`A-007`**, open since V04 |
| Third touch of the level | **NO** | **`A-004`** |

**`D-030` is explicit that a blocked test waits for the lesson that defines the term, and that no
session may substitute *"an approximation, a plausible reading, … or a 'reasonable' numeric
stand-in in order to make a blocked test runnable."*** Marking ten "setups" against invented
boundaries would produce ten classified charts that look like homework and are not.

### 2b. What WAS performed — the anchor, which V10 does define and does assign

`[01:33:43]`–`[01:33:51]`: *"Identifying the higher low point of the week … there's looks like the
lowest point on the chart right now, let me draw a line on the lowest point of the chart."*

**Ten anchors marked on real GBP/USD data** — five long-side (the week's low) and five short-side
(the week's high). Script: `scripts/h2_anchors.py`; output: `data/h2_anchors_output.txt`.

**Selection was mechanical and fixed before any price was read**, per `STUDY_PROTOCOL.md` §2's ban
on picking aesthetically clean examples: the long-side weeks are the 1st, 37th, 73rd, 109th and
145th usable weeks in chronological order; the short-side weeks are the 19th, 55th, 91st, 127th and
163rd. An even deterministic spread across `W-C'`.

| Side | Week | Anchor | Price | At | Week range |
|---|---|---|---|---|---|
| LONG | 2013-01-06 | LOW | 1.59913 | 2013-01-09 09:30 | 186.7 pips |
| LONG | 2013-09-15 | LOW | 1.58843 | 2013-09-17 06:14 | 277.6 |
| LONG | 2014-05-25 | LOW | 1.66915 | 2014-05-29 03:18 | 189.2 |
| LONG | 2015-02-08 | LOW | 1.51965 | 2015-02-10 04:56 | 225.4 |
| LONG | 2015-10-18 | LOW | 1.53058 | 2015-10-23 16:32 | 201.5 |
| SHORT | 2013-05-12 | HIGH | 1.53836 | 2013-05-13 07:43 | 226.7 |
| SHORT | 2014-01-19 | HIGH | 1.66671 | 2014-01-24 03:12 | 273.0 |
| SHORT | 2014-10-05 | HIGH | 1.62253 | 2014-10-09 07:45 | 272.5 |
| SHORT | 2015-06-14 | HIGH | 1.59296 | 2015-06-18 04:30 | 442.1 |
| SHORT | 2016-02-21 | HIGH | 1.43054 | 2016-02-21 17:43 | 451.8 |

### 2c. ⭐ THE INDEPENDENT CROSS-CHECK ON THIS CONCLUSION

**Every anchor was computed twice, by two paths sharing no code:**

1. from the **committed M15 aggregation**, via `mmm_week.build_weeks`;
2. from the **raw M1 series**, by direct masking on the week's span.

**Result: 10 of 10 agree exactly**, on price and on timestamp. The script **exits non-zero** on any
disagreement, so this is a gate rather than a report.

**What the cross-check is actually worth, stated plainly.** An M15 bar's high *is* the maximum of
its M1 constituents' highs, so **agreement is expected**. The check therefore does **not**
corroborate the market — it corroborates the **aggregation**, which is the thing that could
silently be wrong and which `mmm_lib`'s own docstring records having been wrong once before (a
`datetime64` re-cast that produced "1,297,781 M15 bars"). **A cross-check that could only have
found a tooling defect should be described as one**, not dressed up as independent confirmation of
a finding.

### 2d. What the ten anchors do NOT show

- **Whether any was tradeable.** That needs the lock (`A-077`).
- **Whether a stop hunt or second leg followed.** `A-076`, `A-007`.
- **Any entry, stop, target, or outcome.** None was computed and none may be inferred.

### 2e. The hindsight note, made unprompted

**A weekly extreme is knowable only after the week ends.** Marking one is a legitimate
chart-reading exercise and is exactly what `[01:33:43]` assigns — **but it is not a decision taken
at a decision point.** Nothing in §2b may be read as evidence that these anchors were identifiable
in advance. **Supplying that ability was the lock's job, and the lock has no threshold.** This is
the single most important limitation of V10's method as it currently stands in the corpus.

### 2f. A finding that falls out, and its status

**0 of the 10 selected weeks fall inside V10's own 600–1000 pip band** (median 249.6 pips). This is
**consistent with** `BT_V10_0001`'s corpus-wide result of 0/180 — and it is **not independent
evidence**, being the same instrument, window and measure on a 10-week subset. **Reported as
corroboration of internal consistency, not as a second result.**

---

## 3. H3 — POST IN THE FORUM: `NOT APPLICABLE`

`D-018`'s eligibility test is *"work no present-day agent can perform"* — and `D-019` requires
showing the dimension has **no subject matter**, not merely that it is blocked.

The forum is the 2012 Market Makers Boot Camp student board. It is not in the library, no URL is
given, and the instruction's purpose (peer review by the 2012 cohort) has no present-day analogue.
`[00:17:49]` *"do not mail me the homework post it in the forum"* and `[01:34:58]` *"I'm gonna try
to organize the form for you guys"* both make clear it is a specific 2012 venue.

**This is the V01 H1–H3 pattern** (an 18-item survey emailed to a 2012 address), which review R1
upheld as correctly `NOT APPLICABLE`. **There is nothing to do, now or ever.**

**However** — the *function* the forum serves is **independent review**, and this project supplies
that structurally under `D-003`. The work is submitted for review; only the 2012 venue is
inapplicable.

---

## 4. COMPREHENSION PROBE — 12 / 12

**Answers committed at `54b97f2`, before `score_comprehension.py` existed.** Scoring is
**mechanical, not self-graded**: each question is reduced to factual assertions the transcript
settles by itself — a quotation must appear at the cited marker, a claimed absence must be a
genuine zero count, a claimed count must reproduce. **44 assertions across 12 questions; all 44
hold.**

| Question | Assertions | Result |
|---|---|---|
| Q1 signature trade | 3 | RIGHT |
| Q2 PFH/PFL defined | 3 | RIGHT |
| Q3 blue box vs Asian range | 5 | RIGHT |
| Q4 preconditions in order | 5 | RIGHT |
| Q5 DNC | 2 | RIGHT |
| Q6 distance figure | 3 | RIGHT |
| Q7 stop loss ABSENT | 2 | RIGHT |
| Q8 lock duration conflict | 3 | RIGHT |
| Q9 trade count | 4 | RIGHT |
| Q10 timing prohibition | 4 | RIGHT |
| Q11 TDI deferred | 3 | RIGHT |
| Q12 session times ABSENT | 7 | RIGHT |

**Self-assessment recorded before scoring: *"Predicted score: 11 or 12 of 12"*, naming Q6 and Q8 as
the likely markdowns.** Both scored RIGHT, so the prediction was correct at its optimistic end.

### ⚠ WHAT 12/12 IS AND IS NOT EVIDENCE OF — the reviewer should read this before crediting it

**V09's probe scored 9/9 and its own write-up called that unimpressive on a lesson printed in plain
English. The same caution applies here, and more of it, for three reasons:**

1. **The scorer checks the answers' factual assertions, and the same session wrote both.** A
   question I understood badly would produce an answer whose assertions I also chose — and they
   would pass. **The mechanism catches misquotation and invented absence; it cannot catch
   misunderstanding that is internally consistent.**
2. **Four questions (Q3, Q6, Q9, Q11) were written *with* their attractive wrong answers in view.**
   Knowing the trap is most of avoiding it. **A probe whose author designs the distractors is
   weaker than one whose author does not.**
3. **The two hardest answers are refusals** — Q6 (*"the number is settled, its origin is not"*) and
   Q8 (*"the lesson gives five incompatible figures"*). Those are the answers this project's whole
   discipline trains toward, so scoring them right is **partly evidence about the protocol** rather
   than about comprehension of V10.

**The genuinely load-bearing evidence of comprehension is elsewhere** — in `Q-011` (six fabricated
citations refuted against the audio), in `C-016`/`C-017` (two conflicts found and both tidy
reconciliations refused in writing), and in `BT_V10_0001` §1 (declining to test the lesson's
headline trade rather than approximating it). **A reviewer weighing this lesson should weight those
above the 12/12.**

---

## 5. FILES

| Path | What |
|---|---|
| `V10_COMPREHENSION_ANSWERS.md` | 12 answers with reasoning traces — **committed `54b97f2`, before the scorer** |
| `V10_FLASHCARDS.md` | H1 — five cards on V10's stated rules |
| `scripts/score_comprehension.py` | Mechanical scorer, 44 assertions against the transcript |
| `scripts/h2_anchors.py` | H2-partial: ten anchors + the M1↔M15 independent cross-check (gate, exits non-zero) |
| `data/comprehension_score.txt` | Scorer output |
| `data/h2_anchors_output.txt` | Anchor output, with SHA-256 provenance and QA gate |

---

## 6. WHAT IS OWED, AND WHEN IT DISCHARGES

**H2's setup half is DEFERRED and stays open**, carried into `REVIEW_INDEX.md`. It discharges in
whichever lesson supplies:

- **the lock threshold** (`A-077`) — distance and/or duration for "price has moved away and
  confirmed"; **and**
- **`second leg`** (`A-007`) — open since V04; **and**
- ideally **`blue box`** (`A-076`), though the lesson's own *"obvious ones are still valid"* at
  `[00:46:43]` means the box is a preference rather than a strict requirement, so `A-076` may not be
  strictly necessary.

**`A-004` (*the level*) is NOT strictly required for the safety trade**, because the trade's stated
anchor is the week's extreme rather than a level count — a point worth recording, since `A-004` is
otherwise this project's largest blocker and it is easy to assume it blocks everything.

**`[01:13:03]` says TDI confirmation is *"next week's lesson"*, i.e. V11.** Whether V11 also supplies
the lock is not predicted here.
