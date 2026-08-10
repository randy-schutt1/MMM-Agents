# 13_MACHINE_SPEC — PHASE 4 (FORMALIZER)

Formal measurable interpretation required for software.

## STATUS: EMPTY — DO NOT POPULATE YET

Target file: `MMM_MACHINE_SPECIFICATION.md`

## PRECONDITION

`12_MASTER_SPEC/MMM_MASTER_SPECIFICATION.md` must be complete and authoritative.
Formalizing an unfinished methodology encodes guesses as rules and then measures
the guesses.

## MMM-HUMAN vs MMM-MACHINE

Human concept:

> Strong displacement away from the level.

Machine research candidates might eventually include: candle body relative to ATR,
close location value, distance travelled, number of candles, retracement size,
velocity, relative volume where applicable.

**These are not automatically rules.** They are candidate measurable
representations that must be validated empirically against manually labelled
GBP/USD history in Phase 6.

**Never overwrite the human definition with the machine approximation.** The two
layers stay separate permanently, so that a coded approximation can always be
checked against what was actually taught.

## EVERY MACHINE RULE IS CLASSIFIED

```text
DIRECT TRANSLATION       ← the course states objective criteria
EMPIRICAL APPROXIMATION  ← a measurable stand-in, validated against labelled data
HEURISTIC                ← a working rule with weak support
UNRESOLVED               ← no defensible representation yet
```

**This distinction must survive into the code** — in comments, in variable names,
in the debug output. A heuristic that looks like a direct translation in Pine
Script is how an invented threshold becomes indistinguishable from doctrine.

## SOURCE MATERIAL FOR THIS PHASE

`10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md` is the work queue: each `DO NOT CODE`
record becomes a `RESEARCH CANDIDATE` with a defined hypothesis, then either
`EMPIRICALLY VALIDATED` or `UNRESOLVED`. Nothing is promoted by convenience.
