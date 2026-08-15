# MMM CURRENT STATE — PHASE 2 CANONICAL SNAPSHOT

**Status date:** 2026-08-15  
**Canonical working branch:** `main`
**Purpose:** the concise, current entry point for every future agent. This file reports state; it
does not adopt decisions, close evidence records, or authorize a later phase.

## 1. What is consolidated

The current branch preserves and combines:

1. integration through V21 R2, including the independently verified V21 `PASS`;
2. the owner/tooling sequence covering the entry ladder, canonical toolset, BTMM indicator survey,
   canonical EMA set, 5/13 pair and M15 timeframe;
3. the setup synthesis and its Phase 1 correction.

No source branch was deleted, rebased or force-updated. The draft files remain drafts. Their merge
into one readable branch does not change their evidence tier or adoption status.

## 2. Artifact census

| Artifact class | Current evidence |
|---|---:|
| Source lessons | 21 verified rows in `SOURCE_MANIFEST.md` / `COURSE_PROGRESS.md` |
| Transcripts | 21 (`V01`–`V21`) |
| Source notes | 21 |
| Interpretation notes | 21 |
| Mastery reports | 21 |
| V21 review result | R2 `PASS`, 0 critical / 0 major / 0 minor |
| Observation records checked by structural validator | 37, each with a pre-registration, classification and bare rate |
| Promoted `CL-NNN` concept files | 0 |
| Human setup families in the Phase 1 registry | 26 plus one owner timing rule |

`PROMOTED CONCEPT FILES: 0` is not a statement that the course contains no setups. The human setup
inventory is `MMM_SETUP_REGISTRY.md`.

## 3. Formal course status

These statements are simultaneously true:

- **The corpus is ingested end to end:** all 21 lessons have lesson artifacts.
- **V21 is complete:** its R1 findings were fixed and independently re-verified at R2.
- **Lesson review is complete:** all 21 lessons are reviewed and approved. Fourteen hold a formal
  independent reviewer `PASS`; V11, V13, V15 and V17–V20 are closed under owner ruling D-062 as
  `COMPLETE — OWNER-AUTHORIZED REVIEWER REMEDIATION`. Their historical `REVISE` verdicts remain
  preserved rather than being rewritten as later independent passes.
- **The cumulative remediation passed:** Targeted Retest 002 scored 59/60, cleared the 25%/50%
  gate, and the 75% review completed with two corrections resolved at `2a16e64`.
- **The final review is complete and returns `STUDENT PHASE: INCOMPLETE`.** Reconstruction remains
  `PARTIALLY`, so Phase 3 is `NOT GRANTED`; `12_MASTER_SPEC/` and `13_MACHINE_SPEC/` remain empty.

No future agent may shorten these facts to either *"the course is unfinished"* or *"the system is
fully mastered."* The correct state is: **lesson ingestion and cumulative review complete; human
reconstruction partial; Student Phase incomplete; Phase 3 not granted.**

## 4. Decision and evidence boundary

- Highest adopted decision in `DECISIONS.md`: `D-062`.
- D-062 records the owner's authorized reviewer-remediation workflow; it does not claim a later
  independent re-review or waive the cumulative student gate.
- The M15 `EMA(5)`/`EMA(13)` next-bar-close rule is recorded at `OWNER EMPIRICAL PREFERENCE` inside
  the `D-058` draft. It is computable as a **timing gate**, not a direction signal and not course
  evidence.
- The BTMM survey is tooling evidence. Compiled `.ex4` artifacts expose names/parameters, not
  algorithms.

## 5. Current knowledge surfaces

Read in this order for setup questions:

1. `MMM_CURRENT_STATE.md` — formal repository state.
2. `MMM_SETUP_REGISTRY.md` — what setups/signals are known and at what usability level.
3. `MMM_GAP_AND_DEPENDENCY_MATRIX.md` — what prevents each family from becoming operational.
4. `SETUP_SYNTHESIS_2026-08-15.md` — detailed source synthesis.
5. Source notes, ambiguity/contradiction ledgers and decisions — authority for individual claims.

The agent must answer *"what setups exist?"* from the registry. It must answer *"can I execute or
code this setup?"* from the operational/machine columns and the gap matrix. Those are different
questions.

## 6. Phase boundary

Phase 2 has completed the lesson-review closeout, sealed targeted remediation, all cumulative
checkpoints and the official final review. It has not satisfied the final review's reconstruction
standard, authorized or populated the Master Specification, or established a validated trading
edge. Required remediation is H1–H7 in `18_REVIEW/FINAL_COURSE_REVIEW.md`.
