# AUTOMATION AMBIGUITIES

Every subjective phrase in the course that would be dangerous to code prematurely.

Template: `00_SYSTEM/TEMPLATES/AMBIGUITY_TEMPLATE.md`

---

## STATUS

```text
RECORDS: 0
```

**Intentionally empty.** No course material has been studied, so no course
ambiguity has been observed. Records appear here only when an actual lesson uses an
actual subjective phrase.

---

## PURPOSE

Trading instruction is full of judgement words. Left unexamined, they take a
predictable path:

```text
"strong push"
  → agent needs something codable
  → agent picks a threshold that fits the examples it saw
  → threshold enters the concept library
  → threshold enters the machine spec
  → Pine Script enforces it
  → backtest validates the threshold against the data it was fitted to
  → the number looks like a course rule and no one can remember it wasn't
```

This log stops that at step 2 by keeping judgement **visibly** judgement.

`DECISIONS.md` D-010 (machine-rule firewall) is the governing decision.

---

## PHRASES TO WATCH FOR

Not a claim that the course uses these — a checklist of the kind of language that
gets logged when encountered:

*strong, clean, obvious, significant, nice, enough space, high quality, weak,
extended, too extended, momentum, trapped, aggressive, proper, correct-looking,
textbook, healthy, decent, clear.*

Also: quantities stated with a hedge ("usually about 20 pips", "roughly the
London open"). The hedge is part of the teaching. Recording the number without the
hedge is error code E03.

---

## STATUS VALUES

| Status | Meaning | Phase |
|---|---|---|
| `DO NOT CODE` | Default. Subjective; no numeric representation permitted. | 1 |
| `RESEARCH CANDIDATE` | A measurable hypothesis is defined but unvalidated. | 4 |
| `EMPIRICALLY VALIDATED` | Tested against manually labelled history. | 6 |
| `RESOLVED BY COURSE` | A later lesson defines it explicitly. Cite the evidence. | any |

Promotion requires evidence, never convenience. Records are never deleted — a
resolved record keeps its history.

---

## INDEX

| ID | Phrase | First seen | Status | Impact if wrong |
|---|---|---|---|---|
| _(none)_ | | | | |

---

## RECORDS

_(none yet — records are appended below as A-001, A-002, …)_
