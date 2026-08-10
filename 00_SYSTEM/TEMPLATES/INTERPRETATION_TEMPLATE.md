# VXX — INTERPRETATION NOTES

> Copy to `03_LESSON_NOTES/VXX_INTERPRETATION.md`. Delete these instruction blocks.

**Everything in this file is the agent's reading, not the instructor's words.**
Source facts belong in `VXX_SOURCE_NOTES.md`.

Every item requires: evidence, timestamp, screenshot reference where applicable,
and a confidence classification. An interpretation with no evidence is a guess and
must be labelled as one.

| Field | Value |
|---|---|
| Video ID | VXX |
| Interpreted | (date) |
| Source notes | `03_LESSON_NOTES/VXX_SOURCE_NOTES.md` |

### Classification

| Label | Meaning |
|---|---|
| `EXPLICIT` | Directly stated — should normally live in source notes; here only when restating for context |
| `VISUAL` | Clearly demonstrated on a chart or slide |
| `IMPLIED` | Strongly suggested by the lesson but not directly stated |
| `INFERRED` | Agent interpretation based on course material |
| `UNRESOLVED` | Still ambiguous or contradictory |

**The failure mode this file exists to prevent:** instructor shows three examples →
agent recognizes a pattern → agent writes a universal rule → later code treats it
as mandatory. If it was not clearly taught, it does not become doctrine.

---

## 1. WORKING UNDERSTANDING

Plain-language summary of what this lesson appears to teach, as currently
understood. State the confidence level for the summary as a whole.

## 2. INTERPRETED RULES

| # | Interpreted rule | Basis (timestamp + screenshot) | Classification | Confidence | Notes |
|---|---|---|---|---|---|
| I1 | | | INFERRED | Medium | |

For each: what exactly was said or shown that produces this reading, and what an
alternative reading would be.

## 3. GENERALIZATION AUDIT

For every rule stated more broadly than the evidence strictly supports:

| # | Rule as written | Evidence actually seen | Is the generalization warranted? |
|---|---|---|---|
| G1 | | e.g. "3 examples, all in London session" | Not established — relabel INFERRED |

Be hostile to your own generalizations here. The reviewer will be.

## 4. SEQUENCE AND DEPENDENCY

How this lesson's material appears to connect to earlier lessons — clearly marked
as the agent's connection unless the instructor made it.

| Concept | Depends on | Basis | Classification |
|---|---|---|---|

## 5. OPEN QUESTIONS

Questions this lesson raised that it did not answer. Include what evidence would
answer each.

| # | Question | What would resolve it |
|---|---|---|
| Q1 | | |

## 6. SUBJECTIVE LANGUAGE ENCOUNTERED

Every vague term used in the lesson. Each one gets an entry in
`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`.

| Term | Where used | Logged as | Status |
|---|---|---|---|
| | `[HH:MM:SS]` | A-0XX | DO NOT CODE |

## 7. MACHINE CANDIDATES — NOT RULES

Ideas about eventual measurement. **These are not course rules and must never be
written as if they were.**

| # | Subjective concept | Possible measurable representation | Course support |
|---|---|---|---|
| M1 | | | NONE — INFERRED MACHINE CANDIDATE |

```text
Classification:          INFERRED MACHINE CANDIDATE
Canonical Course Status: NOT A COURSE RULE
```

No numeric threshold from this section may enter the concept library or the master
specification during the Student Phase.

## 8. POSSIBLE CONTRADICTIONS

Tensions with earlier lessons. Log each in `11_CONTRADICTIONS/CONTRADICTIONS.md`.

| # | Tension | Source A | Source B | Logged as |
|---|---|---|---|---|

## 9. WHAT I AM NOT CONFIDENT ABOUT

An honest list. Correct uncertainty is valued by the reviewer; false certainty is
the more dangerous error.
