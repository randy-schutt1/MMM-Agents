# 03_LESSON_NOTES

Two files per lesson, and the separation between them is the point.

## STATUS: EMPTY — NO LESSON PROCESSED

## STRUCTURE

```text
VXX_SOURCE_NOTES.md      ← only what the source states or shows
VXX_INTERPRETATION.md    ← the agent's reading, evidenced and classified
```

## WHY TWO FILES

Mixed into one document, an agent's inference becomes indistinguishable from the
instructor's teaching within weeks. That is failure mode 3, **rule drift**:

```text
instructor shows three examples
  → agent recognizes a pattern
  → agent writes a universal rule
  → the rule is later remembered as instruction
  → code enforces it as mandatory
```

The file boundary makes drift structurally visible: anything in
`VXX_INTERPRETATION.md` is, by location, not something the instructor said.

## SOURCE NOTES RULES

- Every entry carries a timestamp. No timestamp, not a source note.
- Quote or closely paraphrase; do not "improve" the instructor's wording.
- Use the instructor's terminology exactly.
- **Preserve qualifiers.** "Usually about 20 pips" is not "20 pips". Dropping the
  hedge turns an observation into a rule (E03).
- Leave cells empty rather than filling them with a reasonable guess. Empty cells
  are findings.
- Only `EXPLICIT` and `VISUAL` content belongs here.

## INTERPRETATION RULES

- Every item: evidence, timestamp, screenshot reference, confidence classification.
- Be hostile to your own generalizations — the reviewer will be.
- Subjective language goes to `10_AMBIGUITIES/` as `DO NOT CODE`.
- Quantification ideas are `INFERRED MACHINE CANDIDATE — NOT A COURSE RULE`.
- An honest "what I am not confident about" section is expected.

Templates: `00_SYSTEM/TEMPLATES/SOURCE_NOTES_TEMPLATE.md`,
`INTERPRETATION_TEMPLATE.md`
