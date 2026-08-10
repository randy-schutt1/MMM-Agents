# 09_CHART_EXAMPLES

Labelled chart evidence, sorted by classification.

## STATUS: EMPTY — NO EXAMPLE COLLECTED

## STRUCTURE

```text
09_CHART_EXAMPLES/
├── positive/     ← clearly satisfies the methodology
├── negative/     ← looks similar but violates an important rule
├── borderline/   ← reasonable experts might disagree
└── unresolved/   ← cannot yet be classified
```

Each example is an image **plus** a `.md` sidecar:

```text
VXX_concept-name_NNN.png
VXX_concept-name_NNN.md
```

**An image with no sidecar is not evidence.** The sidecar records what the example
shows, why it is classified this way, what was visible at the decision point, and
which rule it supports or violates.

## WHY NEGATIVE EXAMPLES ARE NOT OPTIONAL

> A recognition system requires **discrimination**, not merely pattern familiarity.

A library of only clean winning examples teaches an agent — and later a
detector — to say yes. The useful question is always:

> What would make this NOT the setup?

Negative examples must be genuine lookalikes rejected for a **specific rule
violation**. A straw man no one would confuse with the setup proves nothing, and
the reviewer will say so (E17).

## FAILED VALID SETUPS

Setups that met every rule and still lost belong in `positive/`, annotated as
valid-but-losing. They are correct applications with unfavourable outcomes, and
removing them would teach exactly the wrong lesson — that correctness means
profit.

## HINDSIGHT

Classification is based on what was visible at the decision point. An example
classified because of how the chart later resolved is contaminated and must be
redone, not relabelled.
