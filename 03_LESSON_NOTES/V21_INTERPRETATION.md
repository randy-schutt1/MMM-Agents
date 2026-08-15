# V21 — INTERPRETATION

**What this file is:** the student session's reading of V21, graded per claim.
**What it is not:** evidence. Every claim traces to `V21_SOURCE_NOTES.md` → the marker grid.

**Scale:** `CERTAIN` / `HIGH` / `MEDIUM` / `LOW` / `BLOCKED` (`D-030`).

---

## §1 — THE ONE-SENTENCE READING

**V21 answers a question the previous twenty lessons never addressed: what a student should do
while they are still bad at the method.** Its answer is not a better entry — it is an **equity
structure** that converts a wrong entry into a smaller loss and a second chance, plus a **script
that enforces it** and a **diagnostic ladder** that tells the student when to stop using it.

That reading is the lesson's own: `[00:20:36]` *"Since I can trade like a dealer, it only makes
sense to **control my equity like a dealer** — **until I can improve my hit rates and my
entries**"*, and `[00:41:48]` *"**stop using the script** and place regular orders"*.
**CONFIDENCE: HIGH.**

---

## §2 — THE CLAIMS, GRADED

### 2.1 ⭐⭐ *"Lose at a discount"* — the equity argument

> Splitting a fixed lot budget between the entry and a level closer to the stop reduces the loss when
> the stop is hit, and buys a second entry at a better price.

**CONFIDENCE that this is taught: CERTAIN** (`[00:20:54]`–`[00:24:05]`, printed at `20:20`).

⭐ **CONFIDENCE that the arithmetic is correct: CERTAIN, and it needs no test.** `1×100 + 2×50 = 200`
against `3×100 = 300` is **arithmetic, not an empirical claim**. ⚠️ **`[00:22:10]` says so itself** —
*"I'm using these numbers to make the math simple."*

⛔⛔ **WHAT IS NOT ESTABLISHED, AND IT IS THE WHOLE QUESTION:** the split **also reduces the position
size at the best price**, so it lowers the win case as well as the loss case. **V21 never compares
the two structures on a WIN.** ⭐ **The honest description is a change in the payoff SHAPE, not an
edge**, and the lesson does not claim otherwise — but a reader could take it as one. **`A-140`.**

### 2.2 ⭐⭐⭐ The `High / Low Trainer` script

> A market order plus two pendings 20 pips apart, hard stop on all three, risk dialled 1–5 %,
> aggregated lot sizing, ~60-pip grid over an M/W.

**CONFIDENCE that it is taught and delivered: CERTAIN.** Spoken `[00:30:18]`–`[00:38:11]`,
**specified in the author's own handwriting at `31:25`**, and **installed live on camera**.

⭐⭐ **This is the corpus's first COURSE-SUPPLIED MECHANICAL ARTIFACT.** Every prior automation
question in this project has been the project's own inference; **this is the instructor shipping a
tool with a parameter set.**

⚠️⚠️ **AND THE ARTIFACT IS NOT IN THIS REPOSITORY.** V21 describes and installs it; **no file,
filename, code or parameter dialog is legible anywhere in the lesson.** ⛔ **`D-030` therefore blocks
implementing it**, and this session does **not** reconstruct it from the handwritten sheet.
**`A-141`.**

### 2.3 ⚠️ The script's numbers — and they do not fully agree

| Source | Figure |
|---|---|
| audio `[00:32:55]` | all three filled ⇒ *"cycle with **a hundred and fifty** pips"* |
| audio `[00:33:17]` | *"you'll get a **30 and a 50** — most often — cycle with **80**"* |
| ⭐ sheet `31:25` | *"Cycle w/the **30 + 50 + 70**. Most often **+150 pips** / **+80**"* |
| ⭐ sheet `31:25` | *"Take profit **+30 pips** from ORDER 1 = Market order"* · *"**Sell Cycle — 30 pips**"* |

**CONFIDENCE that `150` and `80` are both real and consistent: HIGH** — the sheet's `30+50+70` sums
to 150 and its `+80` is the two-order case, so **the two spoken figures are the two branches of one
scheme, not a contradiction.**

⚠️ **CONFIDENCE on `Take profit +30 from ORDER 1` and `Sell Cycle — 30 pips`: LOW.** **Neither is
ever spoken**, and the sheet does not say how they relate to the `30/50/70` ladder. **`C-031`.**

### 2.4 ⚠️ The blue tracer — `A-133` SURVIVES, and this section's original reason was wrong

> ### ⚠️⚠️ CORRECTED 2026-08-15 — V21 R1 item **366**
>
> **This section originally presented a *"near-miss"*: that the committed *"tracer **in** the ADR
> line"* is an apposition which DEFINES the tracer, and that an independent decode reading *"and"*
> is what kept `A-133` open.** ⛔ **Both halves are withdrawn.** The `and` substitution **does not
> replicate** — seven of ten decodes across four model families return `in`, including `medium.en`
> itself under time-stretch — **and *"X in Y"* is LOCATIVE, not appositive**, so `in` would not have
> closed `A-133` either.

`[00:05:21]`: *"Use the ADR and high-low markers, the light blue tracer **[in / and]** the ADR line,
to understand that if the dealer has **exceeded the ADR** you're looking for a **retrace back in**."*

**CONFIDENCE that `A-133` is closed: ⛔ NONE — and the reason no longer depends on which word was
said.** ⭐ **Neither reading defines the tracer.** *"And"* lists it beside the ADR line; *"in"*
locates it relative to the ADR line. **Neither states what it is computed from, and computation is
what `A-133` asks for.**

⭐ **What V21 does add, and it stands either way:** the tracer is **light blue**, and it belongs to
the **ADR / high-low marker family** — chart furniture used to judge whether the dealer has exceeded
the ADR. **That narrows the search and defines nothing.**

⚠️⚠️ **AND THE METHODOLOGICAL LESSON IS THE OPPOSITE OF THE ONE FIRST DRAWN.** This session framed
the episode as *"an independent pass caught a defect"*. ⛔ **What actually happened is that a
SINGLE-DECODE correction was made with more confidence than one decode supports, and a grammatical
claim was built on top of it.** ⭐ **The correct lesson: a substitution against a committed grid needs
the same replication the project demands of a backtest** — V20's `candle` finding carried **five**
decodes and held; this one carried **one** and did not.

### 2.5 The big board — ⭐ a V19 gap closed

`[00:04:41]` *"**the big board is the high low board**"*, confirmed verbatim independently.
**CONFIDENCE: CERTAIN that V21 defines the term.** ⚠️ **It does not say what instrument or venue
displays it, or how the *"dealer's pushes"* are read off it** — so it is a **named object, not yet a
procedure.**

### 2.6 The assessment ladder

**CONFIDENCE: CERTAIN** it is taught (spoken and printed). ⭐ **It is the first SELF-DIAGNOSTIC
instrument in the corpus** — it maps an observable (how many of three orders filled) onto a
diagnosis and a remedy, and its top rung is *"stop using the tool"*.

⚠️ **It is not a performance metric and must not be read as one:** it says nothing about P&L,
expectancy or hit rate, and its inputs are order fills, not outcomes.

### 2.7 The pivot condition

`[00:18:08]` *"the pivot level is **only valid if the dealer throws an M or a W on the pivot
level**"*. **CONFIDENCE: HIGH that this is stated.** ⭐ **It is a genuine constraint on a tool the
course otherwise uses freely**, and it is consistent with V16's pivot material. ⚠️ **`M3`, the
*"25-pip box"* and *"shark fin"* are named in the same sentence and none is defined here.**

---

## §3 — HOW V21 FITS THE COURSE

| Relation | Reading | Confidence |
|---|---|---|
| **V19 → V21** | V19 `[00:02:12]` promised the scripts *"on the last night"* and `[00:00:52]` fixed that as June 17. **V21 is that night and delivers them** | **CERTAIN** — and it was a forward *expectation*, not a forward read; `D-049` was never invoked |
| **V19/V20 → V21** | V19 printed the seven-item checklist; **V21 speaks it and defines two items V19's audio could not recover** (`big board`, `MA-only trades`) | **CERTAIN** |
| **V20 → V21** | V20 taught the entry arithmetic; **V21 supplies the position structure around it.** They compose: V20 says where to enter, V21 says with how much and what else to place | **MEDIUM** — coherent, and **V21 never references V20's one-third entry** |
| **V21 → the corpus** | ⭐ **The course ENDS here.** `[00:00:20]` *"the final bootcamp regular session"* | **CERTAIN** |

---

## §4 — WHAT I GOT WRONG OR COULD NOT DO

1. ⚠️⚠️ **I nearly closed `A-133` on a preposition.** Reading the committed *"tracer **in** the ADR
   line"* I drafted the conclusion that V21 defines the blue tracer — **the single most valuable
   closure available in this corpus.** ⭐ **The independent ASR pass said `and` and I withdrew it
   before it reached any artifact.** **Recorded as the near-miss it was.**
2. ⚠️ **I read the script's name from the audio as *"training wheels"* before the `31:25` frame
   showed `High / Low Trainer`.**
3. ⚠️ **The install walkthrough is ~20 minutes of screen recording and I captured five frames of
   it.** A reviewer wanting the script's filename would need more.
4. ⚠️ **I did not chase `M3`, the *"25-pip box"* or *"shark fin"*** — all named at `[00:18:18]`,
   all undefined here, all plausibly defined in earlier lessons this session did not re-open.

---

## §5 — RECORDS OPENED

| ID | Subject |
|---|---|
| `A-140` | ***"Lose at a discount"* is demonstrated only on the LOSS side** — the split also reduces size at the best price and V21 never compares the win case |
| `A-141` | **The `High / Low Trainer` artifact is described and installed but NOT PRESENT** — no file, code, filename or parameter dialog anywhere in the lesson or the repository |
| `C-031` | **The handwritten sheet carries two figures the audio never gives** (*"Take profit +30 from ORDER 1"*, *"Sell Cycle — 30 pips"*) and does not state how they relate to the `30 + 50 + 70` ladder |

⭐ **`A-133` (blue tracer) SURVIVES V21 and therefore survives the whole course.** **Dimension B has
been blocked for eight consecutive lessons and the bootcamp has now ended without defining it.**
