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
