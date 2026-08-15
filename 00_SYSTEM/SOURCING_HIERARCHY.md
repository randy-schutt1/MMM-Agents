# SOURCING HIERARCHY — WHERE A DEFINITION MAY COME FROM, AND WHICH ONE WINS

> **Created:** 2026-08-13 · **Branch:** `infra/add-steve-moro-reference-book` · **Status:** `ACTIVE`
> **Recorded as a decision:** `D-040`
>
> **This file adds no new authority to anything.** It is a **ranking layer** over rules that
> already exist in `DECISIONS.md`, `EXTERNAL_VOCABULARY_REFERENCE.md` and
> `EXTERNAL_REFERENCE/README.md`. Those files remain the substantive law; this one puts the three
> sources in a single visible order and specifies **what happens when a later video speaks.**
>
> If this file and a decision ever appear to disagree, **the decision governs** and the
> disagreement is a defect in this file — fix it here, do not read the decision down.

---

## 0. THE PROBLEM THIS SOLVES

The course teaches in named objects — *push*, *the level*, *anchor point*, *shark fin*, *the
trading zone* — and **names them long before it defines them**, sometimes never. A session that
hits an undefined term has three places it could look, and the failure mode is obvious: reach for
the most convenient source, write down a definition, and let it quietly harden into doctrine
before the lesson that actually defines the term is ever watched.

`D-030` forbids approximating a definition the course has not supplied. This file says **where a
session may look, in what order, and what it must do when the course finally speaks.**

---

## 1. THE THREE TIERS

| Tier | Source | Authority | May close an `A-xxx`? |
|---|---|---|---|
| **TIER 1** | **The course recordings** — `01_SOURCE_VIDEOS/` V01–V21, their transcripts in `02_TRANSCRIPTS/`, slides and screenshots in `04_SCREENSHOTS/` | **AUTHORITATIVE. Always wins.** This is the corpus the project exists to study | ✅ **Yes** — `RESOLVED BY COURSE`, the strongest status |
| **TIER 2** | **The Mauro seminar-notes PDF** — `00_SYSTEM/EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_anonymous.pdf`, 84 pp., cited `MMM-NOTES p.N` | **Admitted as normative evidence by `D-039`**, on the owner's attestation. Same lineage, **not** first party, **outranked by Tier 1** | ⚠️ **Yes, but weaker** — `RESOLVED BY MMM-NOTES`, and only where the document actually *supplies* a definition rather than hedging one |
| **TIER 3** | **Generic internet research** — `EXTERNAL_VOCABULARY_REFERENCE.md` **§5**: web pages, forums, indicator listings, Studocu / Course Hero / PDFCoffee | **`EXTERNAL — NON-NORMATIVE`, permanently.** Third-party commentary about a method that *appears* to be this tradition | ❌ **No. Never.** Closes nothing, unblocks nothing, cited in no artifact |

**Search order is Tier 1 → Tier 2 → Tier 3, and you stop at the first tier that answers.** A
lower tier is consulted only because the higher tier is *silent* — never because the higher tier
is inconvenient, unclear, or harder to code.

> ### ⭐ ADDED 2026-08-14 BY `D-045` — A FOURTH RUNG: `TOOLING — OWNER-ATTESTED PLATFORM ARTIFACT`
>
> | Rung | Source | Authority | May close an `A-xxx`? |
> |---|---|---|---|
> | **`TOOLING`** | **The owner's own MT4 platform artifacts**, supplied by the owner and **attested by the owner as his working configuration for this method** — chart templates, compiled indicators and their embedded strings | **Admitted by `D-045`**, and it ranks **BELOW TIER 1 AND ABOVE `[DEFAULT]`** — exactly as `D-042` already does for owner colour attestations. It is **not** Tier 1, **not** Tier 2, and **not** Tier 3 | ⚠️ **Yes, but only PROVISIONALLY** — `PROVISIONALLY RESOLVED — TOOLING`, **never `RESOLVED BY COURSE`**, and the closure carries its weakness in the record |
>
> **Three rules travel with this rung and none of them is optional:**
>
> 1. ⭐ **ADMISSION IS PER-ARTIFACT, as `D-039` is per-document.** `D-045` admits
>    `Ultimate Blue.tpl` / `!SM_TDI` (md5 `ea22c8cf527921cef072586b6fa28296`) **and nothing else.**
>    A second artifact needs its own owner attestation and its own entry. **There is no standing
>    licence to read files off the owner's disk.**
> 2. ⭐ **ADMITTING A SOURCE IS NOT READING IT AGAINST A RECORD.** This is the `D-039` caution
>    repeated, and `D-045` repeats it deliberately: admission makes a record **eligible**, and a
>    session that does the reading closes it, **or does not.** `D-045` itself declined to close
>    `A-086` and `A-032` on the artifact it admitted.
> 3. ⭐ **EVERY CLOSURE ON THIS RUNG IS PROVISIONAL AND JOINS THE §3.4 RE-CHECK LIST**, and a later
>    Tier 1 statement overturns it under §3.1. **Closed on `TOOLING` is not closed for good** —
>    the same sentence §3.4 already carries for Tier 2 and for owner attestation.
>
> **Citations from this rung carry the tag `[TOOLING]` with the artifact name**, so they are
> visibly distinct from `[TIER 1]`, `[TIER 2]` and `[DEFAULT]` at the point of use.
>
> ⚠️ **The search order is unchanged.** `TOOLING` is consulted because Tier 1 and Tier 2 are
> **silent**, never because they are inconvenient. `EXTERNAL_REFERENCE/README.md`'s default is
> untouched, and **Tier 3 remains `EXTERNAL — NON-NORMATIVE`, permanently.**

### 1.1 Tier 1 — what "the course" means here

`01_SOURCE_VIDEOS/` and everything derived from it under `02_TRANSCRIPTS/`, `03_LESSON_NOTES/`
and `04_SCREENSHOTS/`. Note that **Tier 1 has its own internal ranking**, which this file does
not disturb:

- **`D-025` / `D-033`** — the course author outranks a guest presenter, and guest-only material
  cannot close a record on its own.
- **`D-008`** — course evidence outranks agent interpretation.

So "Tier 1 said it" is not automatically dispositive; it must still be the *right speaker* under
`D-025`/`D-033`. A guest presenter is Tier 1 material subject to `D-033`, **not** demoted to
Tier 2.

### 1.2 Tier 2 — what it is, and the three limits that travel with it

> ### THE RULING IN ONE LINE — owner, 2026-08-13
>
> **Treat the Mauro PDF as authoritative/normative — exactly as `D-039` already established —
> UNLESS a video directly contradicts it, in which case the video always wins.**
>
> Both halves matter. The PDF is **not** demoted to "background" or "hints": where it supplies a
> definition and no video contradicts it, it is **normative and may close a record**. And the
> moment a video contradicts it, the video wins **on that point**, a `C-xxx` is filed, and the
> note is superseded there — not generally. `A-014` and `A-023` remain **CLOSED**; this ruling
> confirms `D-039` as-is and adds nothing but explicitness about the override.

An **anonymous student's notes** from Mauro's seminars — its own title page reads *"Private Study
Notes from Seminar of Steve Mauro — Authored by: Anonymous."* It is not a polished course
document and does not claim to be one. The owner has read it and attested that it is *"in
alignment with the instructor and should be trusted"* (`D-039`).

Three limits, all pre-existing, none relaxed by this file:

1. **It is not the recordings.** It describes seminars this project did not record. Where it and
   a lesson diverge, **the lesson is the corpus** — see §3.
2. **`D-030` still binds where the document is silent or hedged.** Where the notes give a
   *number* and then withdraw the regularity in the next sentence, that is not a rule. The
   canonical example is **`push`**: sizes are given (25–50 pips in *"3 pushes or candles"*) and
   immediately hedged (*"it is not that simple… do not simply expect a straight 3 candle
   movement"*). **`push` is not unblocked and V05/V06/V07 dimension B stays BLOCKED.**
3. **Admission is per-document.** `D-039` admits *this* PDF. Anything else dropped into
   `00_SYSTEM/EXTERNAL_REFERENCE/` stays under that directory's ⛔ default — not a source, not
   evidence, never cited — until it has a decision of its own.

### 1.3 Tier 3 — and the trap in it

`EXTERNAL_VOCABULARY_REFERENCE.md` §5. Non-normative forever. It exists so that a session can see
what the wider tradition believes and thereby ask a **sharper question of the course** — never so
it can answer one.

> **⚠️ THE ONE TRAP THAT WILL CATCH A CAREFUL SESSION.** §9.0 records that the Tier 2 PDF is very
> probably the **upstream original** much of the Tier 3 web material was copied from. Therefore
> **Tier 3 agreeing with Tier 2 is one document quoted twice** — it is *not* independent
> corroboration and must never be described as such. Two tiers agreeing raises confidence only
> when they are genuinely independent, and here they are not.

---

## 2. HOW TO USE THE HIERARCHY ON AN UNDEFINED TERM

1. **Search Tier 1 exhaustively first.** Transcripts, slides, screenshots. Silence in Tier 1 is a
   finding worth recording, not a formality to clear.
2. **If Tier 1 is silent, search Tier 2** — grep `EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md`,
   then verify the hit **against the PDF page itself** (the extract loses every diagram).
   Record the finding in `EXTERNAL_VOCABULARY_REFERENCE.md` §9.2 with `MMM-NOTES p.N`.
3. **If Tier 2 is also silent, that is itself a strong result** — record the negative. §9.3 already
   holds seven of these, and they are among the most useful entries in the file: *"zero
   occurrences of `anchor point` in 84 pages"* is real evidence that `A-001` is the instructor's
   own coinage and is **externally unresolvable**.
4. **Tier 3 last, and it decides nothing.** Use it to frame Required Research.
5. **Whatever tier answered, the `A-xxx` status must name the tier** — `RESOLVED BY COURSE`,
   `RESOLVED BY MMM-NOTES`, or (for Tier 3) no status change at all. A future reader must be able
   to tell at a glance how strong the ground under a definition is.

**Silence is never permission.** An undefined term stays undefined and stays `DO NOT CODE`.

---

## 3. ⭐ THE RECONCILIATION RULE — WHEN A LATER VIDEO SPEAKS

> ### A LATER TIER 1 STATEMENT ALWAYS TAKES PRIORITY OVER AN EARLIER TIER 2 OR TIER 3 FILL-IN.
>
> **This is the rule the whole file exists for.** Tier 2 and Tier 3 entries are *provisional
> occupants of a gap*. The moment Tier 1 fills that gap — in V08, in V15, in V21, in a slide
> nobody had read closely — the Tier 1 statement governs and the earlier fill-in **must be
> explicitly reconciled at that point.** It is **never** left standing to silently outrank real
> course content, and it is **never** blended with the course statement into a composite
> definition that no source actually states.

### 3.1 The reconciliation process — mandatory, and it is a process, not a slogan

A session that watches a lesson and finds it defines or clarifies a term already filled from
Tier 2 or Tier 3 **must** do all six steps before the session closes:

| # | Step |
|---|---|
| **1** | **Notice it.** Before writing lesson notes for any video, grep the new material's key terms against `EXTERNAL_VOCABULARY_REFERENCE.md` §5 and §9.2 and against `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`. This is a required step of the study protocol, not an optional courtesy — a fill-in that is never re-checked is exactly how a provisional entry hardens into doctrine. |
| **2** | **Classify the relationship** using the table in §3.2. |
| **3** | **Annotate the lower-tier entry in place** — §5 or §9.2 — with `SUPERSEDED BY COURSE`, `COMPATIBLE — COURSE IS NARROWER`, or `CONFLICT — OWNER ADJUDICATION REQUIRED`, plus the video ID and timestamp that triggered it. |
| **4** | **Leave the superseded text visible.** Strike it through or fold it into a `<details>` block per `REMEDIATION_PROTOCOL.md` §2. **Never delete it** — the audit trail of what was believed, on what basis, and for how long, is itself project evidence. |
| **5** | **Update the `A-xxx` record** to the Tier 1 basis, restating its status as `RESOLVED BY COURSE` (or the appropriate narrower status) and citing the video + timestamp. Where the record had been carrying `RESOLVED BY MMM-NOTES`, say explicitly that the Tier 2 basis has been **replaced**, not supplemented. |
| **6** | **Log it** in `LOG.md`, and — where Tier 1 and Tier 2 actually *contradict* — open a `C-xxx` in `11_CONTRADICTIONS/CONTRADICTIONS.md` per §3.3. |

### 3.2 The four cases

| Case | What it looks like | Action |
|---|---|---|
| **A — Tier 1 is clear and specific** | The lesson states the definition outright | **Tier 1 wins outright.** Close/narrow the `A-xxx` on the course evidence **alone**. Annotate the lower-tier entry `SUPERSEDED BY COURSE`. **Do not blend.** |
| **B — Compatible; the lower tier adds detail Tier 1 does not state** | The lesson defines the object; the notes add a number the lesson never gives | **Adopt only what Tier 1 states.** The extra detail stays where it is, at its own tier, and does **not** enter the spec. Annotate `COMPATIBLE — COURSE IS NARROWER`. The temptation to keep the extra number because it is codable is precisely what `D-030` forbids. |
| **C — Genuine conflict** | The lesson and the notes state incompatible things | **Do not adjudicate.** Open a `C-xxx`, annotate `CONFLICT — OWNER ADJUDICATION REQUIRED`, log in `SETUP_ISSUES.md`, surface to the owner. See §3.3 — the resolution rule is known, but the *finding* is still owed. |
| **D — Tier 1 clarifies without defining** | The lesson uses the term in a way that narrows it but stops short of a definition | The `A-xxx` **narrows**; it does not close. Annotate the lower-tier entry with the new constraint and say plainly that it is still not a definition. |

### 3.3 When Tier 1 and Tier 2 contradict — owner direction

> *"if at any time the videos contradict the pdf then we can call it out."* — owner, 2026-08-13

**Mandatory, not permissive.** Log a `C-xxx` in `11_CONTRADICTIONS/CONTRADICTIONS.md`, tagged
`MMM-NOTES` vs. the speaker, carrying **both** the page and the timestamp.

**Resolution rule: the recording wins.** Where the recording is clear it is doctrine, and the note
is superseded on that point.

**A conflict is NEVER resolved by:** reading the lesson down to fit the notes; treating the notes
as *"what he really meant"*; declaring the lesson a misspeak; or preferring whichever version is
easier to code.

**A divergence is a finding, not noise.** A disagreement between the recordings and an attested
account of the same teacher is **evidence about the corpus**. Tidying it away destroys the finding.

**Two divergences are known, and BOTH are now filed as contradiction records:**

| Divergence | Tier 2 says | Tier 1 says | Record |
|---|---|---|---|
| The moving-average set | **5 / 13 / 50 / 200, no 800**; the 200 is *"home base"* (`MMM-NOTES` p.38) | V06 audio uses ***"blueberry"***, confirmed by the owner as **800** | ✅ **`C-010`** — the corpus's **800 stands**; the notes' enumeration is superseded on this point. `A-020` closes on **owner attestation**, not on the notes |
| ADR lookback | *"the average daily trading range of the **last 2 weeks**"* (`MMM-NOTES` p.43) | V04 guest: **2 previous days** `[01:05:36]`; also an unbounded *"generally every day runs"* `[01:13:34]` | ✅ **`C-011`** — ***"2 weeks"* is NOT the ADR window.** `A-038` is **NOT** narrowed: Tier 1's three bases stay incompatible, so Tier 2 is defeated **without** a replacement. Stays `DO NOT CODE` |

> **Note the asymmetry `C-011` makes concrete.** "The video wins" is a rule about **which source
> is superseded**, not a promise that Tier 1 supplies a usable answer. Where Tier 1 contradicts
> Tier 2 but is itself incoherent, the correct outcome is that **both** the Tier 2 figure and the
> record's blocker survive. A session that treats a won contradiction as licence to adopt whatever
> Tier 1 fragment is nearest has made the `D-030` error by another route.

### 3.4 The records currently closed below Tier 1 — the standing re-check obligation

> ### ⭐ EXTENDED 2026-08-14 BY `D-045` — **`A-084` JOINS THIS LIST.** The heading above was
> ### *"the two records currently closed on Tier 2"* and is retained in the body below; the list
> ### is now **four records closed on three different sub-Tier-1 warrants.**
>
> **`A-084`** (*is the TDI's plotted green line `RSI(21)` or a smoothing of it?*) is
> **`PROVISIONALLY RESOLVED — TOOLING` at `k = 2`** under `D-045`, on the owner-attested
> `!SM_TDI` template's `RSI_Price_Line=2` / `RSI_Price_Type=0`. ⚠️ **Its weakness is on the record
> at the closure and is not glossed: the corroborated fields and the load-bearing field are NOT the
> same fields.** V13 frame `00:53:35` corroborates the non-default `63`/`37` and the `21`;
> **`RSI_Price_Line=2` is not among them**, and the artifact is dated 2016/2019 against a 2012
> course.
>
> ⭐ **THE TRIGGER FOR `A-084` IS NARROWER AND MORE ACTIONABLE THAN THE OTHERS' — name it, so a
> session knows exactly what to watch for: any lesson showing a TDI PROPERTIES DIALOG, a
> NAVIGATOR/INPUTS PANEL, or stating a SMOOTHING LENGTH in speech. That session MUST run §3.1
> against `A-084`.** The legend route is closed corpus-wide (`TDI_MMM <values>`, no parameter
> tuple) and **2,047 frames across V12–V14 hold no dialog** — so **stop scanning legends**, and
> watch for the dialog.
>
> **The provisional closure being provisional is the whole reason the scan is still worth running.**

*(Original heading and text, retained unedited per `REMEDIATION_PROTOCOL.md` §2:)*
### 3.4 The two records currently closed on Tier 2 — the standing re-check obligation

`A-014` (*fractional disparity*, `MMM-NOTES` p.52) and `A-023` (*the 33 trade*, `MMM-NOTES` p.64)
are marked **`RESOLVED BY MMM-NOTES`** under `D-039`. `A-020` (*Mayo = 200*) is resolved on
**owner attestation** with Tier 2 corroboration, and is explicitly *not* `RESOLVED BY COURSE`.

**These three are the highest-priority reconciliation targets in the project.** They are closed on
a tier that a later video can overturn. Any session reaching a lesson that touches cross-pair
analysis, the level-counting scheme, or the moving-average set **must** re-check these three
against the lesson and run §3.1 if Tier 1 speaks. Closed on Tier 2 is **not** closed for good.

> ### 📌 UPDATED 2026-08-13 — `D-041`, AND `A-020`'s OBLIGATION IS **NOT** DISCHARGED
>
> **The course-canonical nickname mapping, owner-attested and definitive (`D-041`):**
> **ketchup = 5 · mustard = 13 · water = 50 · mayonnaise = 200 · blueberry = 800**
> (blueberry alone is `RESOLVED BY COURSE`, V09 `[00:41:43]`, on the **15-minute**).
> Recorded here so a session arriving at this obligation does not have to reassemble the mapping
> from four files — which is the failure `D-041` exists to fix.
>
> **`A-020` STAYS ON THIS LIST.** `D-041` closed `C-018` and corrected two rows; it did **not**
> make any of ketchup/mustard/water/mayo a Tier 1 statement, and it created **no "Tier 0"** — the
> owner disambiguated an ambiguous Tier 1 sentence, which is not the same act as outranking one.
> A later video attaching a period to a nickname still governs and still triggers §3.1.
>
> **The strongest argument for this section is now `D-041` itself:** a *definitive* owner
> attestation had to **overturn two rows of an earlier owner-attested closure** that had agreed
> with three Tier 3 sources and with the project's own inference from V06. Fill-ins from below
> Tier 1 go stale silently. That is what this obligation is for.
>
> `A-014` was re-checked against V09 and **not** changed; `A-023` is untouched. Both remain listed.

> ### 🔎 UPDATED 2026-08-13 — `D-042`: THE `A-020` RE-CHECK WAS **PERFORMED** AND RETURNED **NEGATIVE**
>
> The obligation above was discharged **as at V11**, not deferred. V01–V10 (integration branch),
> **V11 (`origin/video/v11`, unmerged — a search that skipped it would have been a false
> negative)**, the full 84-page `MMM-NOTES` extract and every `04_SCREENSHOTS/*/INDEX.md` were
> swept for all five nicknames and proximity-scanned against `5 / 13 / 50 / 200 / 800`.
>
> **Tier 1 still does not speak on ketchup or mustard.** `ketchup` occurs **0×** in genuine audio
> anywhere in the corpus; `mustard` occurs **twice**, both V04, both numberless. The only explicit
> pairings in existence remain blueberry = 800 (V09 `[00:41:43]`, Tier 1) and mayo = 200
> (`MMM-NOTES` p.66, Tier 2). **§3.1 was therefore not triggered and `D-041` is unchanged.**
>
> **`A-020` STAYS ON THIS LIST for V12 onward.** A discharged re-check is a dated result, not a
> discharge of the obligation.
>
> **One thing the search did turn up, and it is Tier 1.** V07 `[00:25:34]` — *"this yellow one is
> a five moving average"* — attaches a **colour** to a period, and it **contradicts** the owner's
> new colour mapping (`D-042` §2: 5 = red, 13 = yellow). Chained through the owner's
> mustard = yellow it points back at **mustard = 5, ketchup = 13**. **Not adjudicated** — §3.2
> **Case C**, surfaced to the owner as `SETUP_ISSUES.md` `I-011`, `OPEN`. Note that Case C is the
> right rule even though this is Tier 1 vs. an **owner attestation** rather than Tier 1 vs. Tier 2:
> the hierarchy has no rung for the owner, because `D-041` established that owner attestation sits
> **outside** the tiers as an adjudication warrant. A source cannot be ranked against the
> adjudicator; it can only be put back to them.

> ### ⭐ FINAL 2026-08-13 — `D-043`: THE OWNER WAS PUT BACK TO AND **REVERSED**. THE TAPE WAS RIGHT.
>
> **The two blocks above are superseded on the ketchup/mustard rows and are retained unedited**
> (`REMEDIATION_PROTOCOL.md` §2). **`D-043` is the authoritative mapping:**
>
> > *"I was wrong. It's the reverse. **5=mustard=yellow, 13=ketchup=red.**"* — owner, 2026-08-13
>
> **mustard = 5 (yellow) · ketchup = 13 (red) · water = 50 (aqua) · mayonnaise = 200 (white) ·
> blueberry = 800 (blue)** — blueberry alone is `RESOLVED BY COURSE`, V09 `[00:41:43]`, on the
> **15-minute**. The other four are `RESOLVED — OWNER ATTESTATION` on **both** axes.
>
> **⚠️ Two mappings reversed and their composition did not.** `D-041`'s nickname↔period **and**
> `D-042` §2's period↔colour both flip; **nickname↔colour** (ketchup = red, mustard = yellow) is
> unchanged. Correcting only the colour pairing corrects nothing. See `D-043` §2.
>
> **`I-011` is CLOSED**, `RESOLVED — OWNER ATTESTATION`. V07 `[00:25:34]`'s *"this yellow one is a
> five moving average"* now **agrees** with the owner. That is **corroboration, not the warrant** —
> the attestation would have closed `I-011` either way. **One cell gains a real Tier 1 basis** —
> *"the 5 EMA is yellow"*, stated directly in one sentence — but **nothing becomes
> `RESOLVED BY COURSE`**: *mustard = 5* still needs V07's *yellow = 5* chained through the owner's
> *mustard = yellow*, and no speaker makes that join.
>
> #### THIS SECTION IS THE THING THAT WAS VINDICATED, TWICE, IN OPPOSITE DIRECTIONS
>
> `D-041` argued that its own existence — a definitive attestation overturning two rows of an
> earlier attested closure — was the strongest argument for this obligation. **`D-043` overturned
> `D-041` the same day, back to the original assignment.** *"Closed on owner attestation is not
> closed for good"* has now been demonstrated against an attestation **twice within twenty-four
> hours**, and the second time it restored what the first had discarded.
>
> **And §3.2 Case C is what caught it.** `D-042` found one Tier 1 sentence contradicting a
> *different axis* of the mapping, declined to chain the inference, and surfaced it. Had it
> adjudicated — in either direction — the error would have stood. **The rule that forbids a session
> from resolving a genuine conflict is what produced the correct answer here.**
>
> **`A-020` STAYS ON THIS LIST for V12 onward.** `D-042` §1's exhaustive negative is **unaffected
> and still governs**: no Tier 1 statement attaches a period to *ketchup* or *mustard* anywhere in
> V01–V11. `D-043` changes **which owner-attested numbers fill that gap, not whether the gap
> exists.** `A-014` and `A-023` remain listed and untouched.

---

### 3.5 ⭐ WHEN TIER 1 CONTRADICTS **ITSELF** — the `D-048` tie-break ladder

**Added 2026-08-14 by `D-048`.** §3.3's *"the recording wins"* **presupposes a recording that is
clear.** This file ranks **sources**; it has never had a rule for **two things one speaker said** —
printed against spoken, one lesson against another, or one sentence against another in the same
hour. **The class has arisen three times** (`C-017`, `C-021`, the `D-041`/`D-043` EMA-nickname
family) and consumed **two owner rulings and one reversal**. This section is that rule.

**Apply the rungs IN ORDER. Stop at the first rung that answers. RECORD WHICH RUNG ANSWERED.**

| Rung | Test | Outcome |
|---|---|---|
| **1** | Is one statement a **demonstrable misspeak, corrected by the same speaker in the same passage**? | The correction governs. Record both; note the correction |
| **2** | Does one statement carry a **construction** and the other only a **characterisation**? *How a thing is computed* outranks *what it feels like or is built upon* (`A-093`) | The constructive statement governs |
| **3** | Is one statement **unhedged, unprompted and LATER**, with the earlier one hedged, prompted or retracted under correction? | The later statement is the speaker's **standing position** — ⚠️ **this rung records a POSITION, not a FACT.** Anything closed on it closes **`PROVISIONALLY RESOLVED — TIER 1 STANDING POSITION`**, never `RESOLVED BY COURSE`, and carries the conflicting statement in the record |
| **4** | **Anything else — INCLUDING any case where the rungs DISAGREE, or where a rung would close a load-bearing record** | ⛔ **DO NOT ADJUDICATE.** File/keep the `C-xxx`, keep the record `DO NOT CODE`, put it to the owner. Owner adjudication sits **outside** the ladder, as `D-041` established it sits outside the tiers |

**Three hard limits, and they are what makes the ladder safe:**

1. **The ladder NEVER produces `RESOLVED BY COURSE`.** Only an *uncontradicted* Tier 1 statement
   does. A resolved internal conflict yields a **provisional** status at best.
2. **The `C-xxx` is never deleted or downgraded.** Both statements stay on the record, visible,
   per `REMEDIATION_PROTOCOL.md` §2. **A divergence is a finding about the corpus** — the same
   principle §3.3 already states for Tier 1 vs Tier 2.
3. **Tier 2 corroboration is a TIEBREAKER INPUT, NEVER A WARRANT.** It may be *noted* at rung 3
   and does not promote the outcome above provisional — `D-039`'s Tier 2 cannot outrank Tier 1, so
   it certainly cannot arbitrate between two Tier 1 statements. **§1's new `TOOLING` rung is
   treated identically and for the identical reason.**

> #### ⭐ THE LADDER'S FIRST LIVE APPLICATION RETURNED **RUNG 4** — and that is the ladder working
>
> `D-048` Part 2 put **`C-021`** (the TDI volatility bands' *basis*) through it: **rung 1 arguably
> answers for V12** and is not clean (the corrector is unidentified and is **not the speaker**);
> **rung 2 is SILENT** — neither statement is a construction, both are characterisations;
> **rung 3 answers for V14**. **Rungs 1 and 3 disagree → rung 4 → DO NOT ADJUDICATE.** The
> `D-045` `TOOLING` artifact was also checked field-by-field and is **silent on the basis**.
> **`C-021` stays `OPEN`, and a direct owner pick is owed** (`REVIEW_INDEX.md` item 187).
>
> **A tie-break scheme that always produces a winner is not a tie-break scheme, it is a
> preference.** Rung 4 is what keeps it honest — and §3.4's `D-042`/`D-043` history is this
> project's own demonstration that a session **declining** to chain an inference is what produced
> the correct answer.
>
> ##### ⭐⭐ AND THE OWNER PICK ARRIVED — 2026-08-14, `D-052`. **`C-021` IS CLOSED.**
>
> The paragraph above stands as written; the sentence *"a direct owner pick is owed"* is
> **discharged, not withdrawn.** The owner ruled by direct instruction — *"It's definitely not the
> market basis. It's the RSI [line]"* — and `C-021` closes at a tier of its own:
>
> | | |
> |---|---|
> | **Status** | `CLOSED — OWNER EMPIRICAL PREFERENCE` (`D-052`) |
> | **What it means** | The owner's judgment against his **lived experience of the indicator**. **Recollection of practice, NOT course evidence.** |
> | **Where it sits** | **OUTSIDE the ladder and OUTSIDE the tiers**, exactly as `D-041` established owner adjudication does. It is **not** a fifth rung and **not** a fifth tier — do not add one |
> | **Distinguish from** | `RESOLVED — OWNER ATTESTATION` (§3.4, `D-039`/`D-043`) = the owner testifying to **what was TAUGHT**. `OWNER EMPIRICAL PREFERENCE` = the owner judging **what the INSTRUMENT DOES** |
>
> ⚠️⚠️ **THE CORPUS IS OVERRIDDEN HERE, NOT RECONCILED.** **Tier 1 V14 `[00:45:09]`** and
> **Tier 2 `MMM-NOTES` p.45** *both* say the **market base**, both stand unretracted, and the
> ruling goes the other way. **This is the first time in the project that an owner ruling has
> overridden an unretracted Tier 1 statement rather than filled a Tier 1 silence** — §3.4's
> standing re-check obligation therefore applies to it with full force: **a later video that
> states a construction for the bands governs and triggers §3.1.**
>
> ⛔ **And it unblocks nothing:** the bands' **PERIOD** is still never stated at any tier, so
> `A-086` stays `DO NOT CODE` and `A-031`/`A-032` stay uncomputable. **`REVIEW_INDEX.md` item 187
> is CLOSED.** ✅ **Rung 4 is vindicated, not bypassed** — it named the one input that could settle
> this, and that input is what settled it.

**`C-017` is NOT ruled by `D-048`.** It becomes **eligible** for a session to apply this ladder to
it, which is a different act from having applied it.

---

## 4. WHAT THIS FILE DOES NOT CHANGE

- **`D-039` is untouched.** The Tier 2 PDF remains **normative** evidence and **may** close a
  record where it genuinely supplies a definition. Owner direction, 2026-08-13: the three-tier
  scheme is a **ranking layer**, and it does **not** downgrade `D-039` or reopen `A-014`/`A-023`.
- **`D-030` is untouched.** Definitions are never approximated. `push` stays blocked; dimension B
  stays blocked.
- **`D-025` / `D-033`** continue to govern authority *within* Tier 1.
- **No `A-xxx` record changed status because this file was written.** Establishing an order of
  precedence is not the same as applying it to a record.

---

## 5. WHERE THE SUBSTANTIVE RULES LIVE

| Topic | File |
|---|---|
| Admission of the Tier 2 PDF, and its four limits | `DECISIONS.md` → `D-039` |
| This hierarchy, as a binding decision | `DECISIONS.md` → `D-040` |
| The Tier 2 document, provenance warning, contents | `00_SYSTEM/EXTERNAL_REFERENCE/README.md` |
| The Tier 2 PDF itself | `00_SYSTEM/EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_anonymous.pdf` |
| Greppable page-indexed text of the PDF | `00_SYSTEM/EXTERNAL_REFERENCE/EXTERNAL_Mauro_MMM_seminar_notes_TEXT_EXTRACT.md` |
| Tier 3 material, and Tier 2 term-by-term findings | `00_SYSTEM/EXTERNAL_VOCABULARY_REFERENCE.md` (§5 = Tier 3, §9 = Tier 2) |
| Never approximate a definition | `DECISIONS.md` → `D-030` |
| Keeping superseded text visible | `00_SYSTEM/REMEDIATION_PROTOCOL.md` §2 |
| Open ambiguities and their statuses | `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` |
| Tier 1 vs Tier 2 contradictions | `11_CONTRADICTIONS/CONTRADICTIONS.md` |
