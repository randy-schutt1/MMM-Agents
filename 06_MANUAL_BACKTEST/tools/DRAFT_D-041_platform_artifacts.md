# DRAFT — `D-041` — NOT ADOPTED, NOT IN FORCE

> **STATUS: DRAFT TEXT ONLY. THIS FILE IS NOT A DECISION AND GOVERNS NOTHING.**
>
> **Why it is sitting here instead of in `DECISIONS.md`.** `D-038a` classifies
> `00_SYSTEM/DECISIONS.md` as a **POLICY ledger — "Integration branch only. Never on a task
> branch."** This work is on `feature/tradingview-mmm-indicator`, so writing the entry here
> would be exactly the breach `D-038a` names. The owner approved the substance on 2026-08-13;
> **adopting it is a separate, deliberate act on the integration branch**, by a session that
> knows it is the only one performing it.
>
> **Number `D-041` is provisional.** `D-040` is the current highest. Re-check against the
> integration branch at adoption time — `D-038a` consequence 1 records that concurrent branches
> have already collided on identifiers.
>
> ### ⚠️ THE COLLISION PREDICTED ABOVE HAS HAPPENED — 2026-08-13
>
> **`D-041` and `D-042` are both TAKEN on the integration branch**, by entirely different
> decisions:
>
> | ID | What it actually is, on integration |
> |---|---|
> | **`D-041`** | The owner's definitive moving-average **nickname↔period** mapping, and the ketchup/mustard inversion it forces |
> | **`D-042`** | The exhaustive nickname search (**negative**), the owner's **colour** mapping, and the V07 `[00:25:34]` Tier 1 conflict (`SETUP_ISSUES.md` `I-011`) |
>
> **This draft is neither of them.** **Adopt it as `D-043`** — the next free identifier as at
> 2026-08-13 — and re-check that again at adoption time, because this file has now been wrong
> about its own number once.
>
> **Not renamed here.** Renumbering an unadopted draft is the adopting session's act, and this
> branch may not write `DECISIONS.md` at all (`D-038a`: policy ledger, integration only). The
> filename still reads `DRAFT_D-041_…`; **the filename is stale and the table above governs.**
> Recorded by the `D-042` session, which found the collision while doing something else.
>
> **Until this is adopted:** the `[TOOLING]` tag used in `MMM_Indicator.txt` / `MMM_TDI.txt` is
> **provisional**, closes no `A-xxx`, and is deliberately not called a tier.

---

## `D-041` — MT4 platform artifacts are admitted as evidence of PARAMETERS ONLY, never of doctrine

**Date:** 2026-08-13
**Decision:** The MT4 indicator binaries and chart templates in the owner's
`~/Desktop/Trading/Indicators/` are **admissible evidence of PARAMETER VALUES**, on the owner's
direct approval, 2026-08-13. They are **not** admissible evidence of method, rule, definition, or
intent.

**The scope line, which is the entire point of this entry:**

| An artifact MAY establish | An artifact MAY NOT establish |
|---|---|
| What number was in a settings box (`RSI_Period=21`) | What the instructor taught |
| That an object exists in the tooling (an `Alert800EMA` input) | What that object *means*, or when to act on it |
| A colour, a period, a level, a window length | A pattern definition, an entry rule, an invalidation |

**Why the split is exactly here.** A settings value is a *fact about a file* and is read off it
with no interpretation. A rule is a *claim about the method* and requires a speaker. `A-039` asks
for parameters and is therefore reachable by this class; `A-032` ("shark fin") asks what the
*pattern* is, and `SharkFin_Upper_Level=63` does not answer it — a threshold is not a shape.
**An artifact that supplies a number an `A-xxx` asks for may CONSTRAIN that record; it may close
one only where the record's whole question is the number.**

**Tier placement — deliberately NOT Tier 3.** `SOURCING_HIERARCHY.md` §1 defines Tier 3 as
*generic internet research … third-party commentary about a method that appears to be this
tradition*, and binds it as *"closes nothing, unblocks nothing, cited in no artifact."* These
files are not commentary about the tradition; they are the instrument, carrying first-party
naming (`!SM_TDI`, `!SM_Daily_HiLo`, `!sm_WorkTime`, internal name `mm4x-tdi`). Filing them at
Tier 3 would both mis-describe them and forbid the citation this project actually wants.
They are equally **not Tier 1** (not the recordings) and **not Tier 2** (not the Mauro PDF).

They therefore sit **below Tier 2 and above Tier 3**, as a class of their own, and **any Tier 1
or Tier 2 statement overrides an artifact on the same point.**

**Three limits that travel with every citation:**

1. **Provenance is unproven.** The files are dated **2015–2019**; the bootcamp was recorded in
   **2012**. Nothing in any artifact shows a setting is the instructor's rather than a later
   user's. This is weaker than `D-039`'s position, where the owner attested to *content*.
2. **Server clocks are not evidence of the timezone question.** Times inside these artifacts are
   raw broker server time — one binary is named `sm_WorkTime_no_autogmt`. Converting them needs
   an offset no artifact states. **`A-019` is untouched by this entry, and `D-031`'s two-arm
   requirement is undisturbed.** An offset inferred by fitting is a hypothesis to test as an arm,
   never a fact to adopt.
3. **`D-030` still binds.** Where an artifact supplies a number and the corpus supplies no
   meaning for it, the number is recorded and the meaning stays open.

**NOT ONE RECORD IS CLOSED BY THIS ENTRY** — the `D-033` / `D-039` caution, repeated because it
has been needed both previous times. Admitting a class is not reading it against a record. Each
`A-xxx` still needs the ordinary evidentiary judgement by a session that does the reading.

**Reason.** The class was forced by a demonstrated failure, not a hypothetical. `MMM_TDI.txt`
shipped the publicly circulating TDI defaults because `A-039` records that the course never
parameterises TDI. The owner's `!SM_TDI` block gives **`RSI_Period=21`**. The Tier-3 default was
**13** — wrong, on the single most consequential number in the indicator, so every rendering it
produced was a different oscillator. `D-030`'s prohibition on approximation was correct and the
approximation was made anyway for want of anywhere better to look. This entry supplies the
somewhere better, with a scope narrow enough that it cannot become a back door for doctrine.

**Alternatives considered.**
*Tier 3* — rejected: mis-describes first-party tooling as third-party commentary, and its
"cited in no artifact" rule would force the TDI parameters back to a value now known to be wrong.
*Tier 2 alongside the Mauro PDF* — rejected: `D-039` rests on the owner having **read** the
document and attested to its alignment. No comparable attestation is possible for a compiled
`.ex4`, and the 2012/2019 date gap is real.
*Leave unadmitted* — rejected: the evidence exists and is already in use in the tools; an
unadmitted class means it gets cited informally and inconsistently, which is worse than a
narrow written rule.

**Consequences.**
- A new tag `[TOOLING]` is legitimate in tool code and notes, and must carry the artifact name
  and, where practical, a hash.
- `SOURCING_HIERARCHY.md` needs a row for the class and a note that its §1 three-tier table is no
  longer exhaustive. *(That file is a standing standard — policy ledger, integration branch.)*
- The artifacts should be manifested (`SOURCE_MANIFEST.md`) with hashes. Two already recorded:
  `MM4XSF_TDI.ex4` md5 `42e97991cd6af1dfec95fbb333ae45ac`;
  `Ultimate Blue.tpl` md5 `ea22c8cf527921cef072586b6fa28296`.
- The `.ex4` binaries are compiled: parameter **names** and **template-saved values** are
  recoverable, **hardcoded internals are not**. The TDI band's standard-deviation multiple is the
  live example and remains unrecovered.

**Status:** DRAFT — awaiting adoption on the integration branch.

---

## Records this bears on, for the session that adopts it

None of these are actioned by this draft. Each needs its own reading.

| Record | What the artifacts add | Suggested disposition |
|---|---|---|
| `A-039` — TDI never taught | `!SM_TDI`: `RSI_Period=21`, `Volatility_Band=34`, `RSI_Price_Line=2`, `Trade_Signal_Line=7`, both `*_Type=0` (SMA), `RSI_Price=0` (close) | **Strong candidate for CONSTRAINED, possibly RESOLVED-BY-ARTIFACT.** The record's question *is* the parameters. Blocker: the std-dev multiple is still unrecovered, so the indicator is not fully reproducible. |
| `A-032` — "shark fin" | `SharkFin_Upper_Level=63`, `SharkFin_Lower_Level=37`, dedicated Upper/Lower Shark Fin buffers | **NARROWED, not closed.** First numbers ever attached to the term. A threshold is not a pattern definition. |
| `A-020` — the MA nicknames | `3M-shadow-boxes-15M.tpl`: 15-minute template, `method=1` (EMA), 50 = **AQUA**, 200 = **WHITE**, 800 = **BLUE** | **EVIDENCE ADDED, DO NOT CLOSE.** 800 = blue makes "blueberry" read as colour-naming, which makes white = 200 = "mayonnaise" a strong candidate for the open half. It is inference from colour semantics with no speaker behind it — `D-030` territory. Log the lead; do not adopt the mapping. |
| `C-010` — the MA set (corpus 800 vs MMM-NOTES silence) | `!sm_WorkTime` has `Alert50EMA` / `Alert200EMA` / **`Alert800EMA`**; `3M-shadow-boxes` plots an 800 on a 15m chart; `Bo.tpl` carries a Bollinger at `period=800` | **Corroborates the corpus side; closes nothing.** `C-010` is about what the *sources* say, and the artifacts are not a source under this entry. |
| `A-038` — ADR lookback | `MM_ADR`: `ADRPeriod=21`. The same template's own ADR readout prints *"(10 days)"* | **GOT HARDER.** Admissible numbers were already 3 (`MMM-NOTES` "last 2 weeks", a guest's 2 days, an unbounded average). Now 21 and 10 as well. A contradiction to log, not a resolution. |
| `A-019` — session timezone | `!sm_WorkTime` windows; 284 rectangles in `3M-shadow-boxes-15M.tpl` clustering on 03:30/10:00/16:00/16:30/23:45 server | **UNTOUCHED — see limit 2 above.** A GMT+3 server would align the large boxes with `MMM-NOTES` p.8 (Asian `00:30–07:00 GMT` exactly) and put the two one-hour boxes at the London and NY opens — but that offset is a curve-fit, not a source. Register as a `D-031` arm. |
| The "prime box" | `draw_mktopen_box` = two one-hour windows, independently reproduced by the 284 rectangles | **The closest documented analogue, and still never called "prime" by anyone.** `prime` remains 0 occurrences in `03_LESSON_NOTES/` and 0 in `MMM-NOTES`. |
