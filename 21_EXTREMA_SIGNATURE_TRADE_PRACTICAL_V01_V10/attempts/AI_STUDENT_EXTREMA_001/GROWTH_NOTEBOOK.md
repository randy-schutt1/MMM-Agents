# Growth Notebook

**NON-GRADED SELF-REFLECTION**

This notebook records process observations from `AI_STUDENT_EXTREMA_001`. It does not score the examination, compare responses with an answer key, or claim that any classification, decision, extrema calculation, or markup was correct.

## Post-exam reflection — 2026-08-13

The examination required me to separate three kinds of work that can easily become entangled: extracting exact price extrema, classifying only the facts available at the decision timestamp, and later documenting completed-week extrema without revising the first answer. My strongest process habit was treating each case as a closed evidence set. I recorded the current chart and CSV facts, created a marked duplicate, hashed it, locked the response, and only then moved forward.

The attempt also exposed a recurring tension between being decisive and being evidence-controlled. When prerequisites were explicitly stipulated, I could state the resulting checklist classification or direction with higher confidence. When a prerequisite, direction, or named-trade definition was not available in the permitted materials, I often used an uncertainty state instead of inferring direction from a familiar-looking price shape. That restraint is important, but future practice should make the exact reason for each uncertainty state more precise and consistently tied to the allowed answer vocabulary for the case.

## What my process did consistently

- Kept the original source charts unchanged and created separate marked duplicates.
- Reported extrema as price-and-timestamp pairs rather than prices alone.
- Restricted target-day HOD/LOD extraction to the printed target-day window.
- Used the completed-week data only for HOW/LOW after Phase A was locked.
- Included evidence labels such as `EXPLICIT`, `VISUAL`, `IMPLIED`, and `UNRESOLVED`.
- Distinguished the official V10 safety trade from separately named V02/V04 teachings instead of silently relabeling them.
- Avoided treating a checklist classification as proof of profitability, stop placement, or later outcome.
- Recorded marked-chart paths and SHA-256 hashes for reproducibility.
- Preserved each Phase-A decision verbatim in Phase B.
- Answered that Phase A did not change when no administration error was identified.

These are process observations only. They do not establish that the underlying answers were correct.

## Recurring uncertainty patterns

### Missing prerequisite definitions

The permitted materials sometimes exposed a label without the full course definition needed to validate it independently. In those situations, I relied on an explicit stipulation when one existed and otherwise avoided reverse-engineering the label from raw shape.

Future improvement: name the missing prerequisite in one sentence, then select the permitted uncertainty state that best matches that exact deficiency.

### Explicit fact versus visual placement

A chart could explicitly stipulate a peak, stop hunt, or second-leg structure while leaving room for judgment about the exact candle to annotate. I sometimes had high confidence in the printed fact but only medium confidence in its spatial placement.

Future improvement: keep two confidence statements separate:

- Classification confidence: confidence in the printed/stipulated fact.
- Markup-location confidence: confidence in the exact candle or region selected for the annotation.

### Direction vocabulary

The attempt included checklist classifications and operational choices such as BUY, SELL, NO TRADE, DNC, WAIT, and UNRESOLVED. These are not interchangeable.

Future improvement: before locking, compare the planned answer with the choices printed for that specific case. If the case requests an operational decision, use its exact allowed vocabulary and keep any checklist assessment in a separate field.

### Named-trade separation

The 22 and straightaway concepts were not to be inferred merely from appearance. The official signature trade remained the V10 safety trade with a second-leg element.

Future improvement: use a dedicated line for each named teaching:

- Official V10 safety trade: classification.
- Separate 22 candidate: stipulated, not stipulated, or unresolved.
- Separate straightaway candidate: stipulated, not stipulated, or unresolved.

## Markup and readability lessons

- Horizontal extrema lines should be visually distinct and use stable colors throughout the attempt.
- Every extrema label should contain the exact price, full timestamp, and timezone.
- Labels should not cover candle wicks, other extrema labels, or the decision candle.
- Sequence annotations are easier to audit when numbered in chronological order.
- A decision arrow should be adjacent to the decision candle, not merely placed in a legend.
- Rejected directions should be visibly crossed out when the case requires that markup.
- `NO TRADE`, `DNC`, `WAIT`, or `UNRESOLVED` should appear directly on the chart when selected.
- The controlling invalidation or missing prerequisite should be short enough to read without obscuring price action.
- A bottom audit strip is useful for summarizing the sequence, but it should not replace on-chart placement.
- Before hashing, perform a final visual pass specifically for overlap, clipping, ambiguous arrows, and unreadable timestamps.

## Hindsight-integrity lessons

Phase A and Phase B answer different questions. Phase A records what could be concluded at the decision timestamp. Phase B reveals later candles for completed-week extrema. A later outcome may make the earlier chart look more obvious, but it cannot change what evidence existed at the decision time.

My reusable rule is:

> Later candles may expand the outcome record, but they cannot enter the locked decision-time evidence set.

For future attempts, I should continue to:

- Lock Phase A before opening the matching completed-week reveal.
- Copy the Phase-A decision verbatim into Phase B.
- Use Phase B only to mark HOW and LOW and document administration errors if any.
- Avoid outcome-based language such as “the decision was right because price later moved...”
- Keep profitability, stop placement, and trade management outside the claim unless the permitted task explicitly supplies and requests them.

## Reusable pre-decision checklist

### Evidence boundary

- [ ] Confirm the case ID and assigned chart/CSV match.
- [ ] Confirm no adjacent or future chart is open.
- [ ] Confirm the CSV ends exactly at the printed decision timestamp.
- [ ] Identify the precise target-day start and end.

### Extrema extraction

- [ ] Filter only the target-day rows.
- [ ] Find the maximum `high` and its timestamp.
- [ ] Find the minimum `low` and its timestamp.
- [ ] Check for tied extrema and document the timestamp rule if a tie exists.
- [ ] Cross-check both extrema against the visible chart.

### Classification evidence

- [ ] Identify the official trade definition in scope.
- [ ] Identify the peak or candidate peak and its evidence label.
- [ ] Check pull-away/lock.
- [ ] Check consolidation.
- [ ] Check stop hunt and beyond-box condition where required.
- [ ] Check the second-leg M/W element.
- [ ] Check the direction-away fact.
- [ ] Keep 22 and straightaway candidates separate and only classify them when stipulated.
- [ ] Do not infer direction from raw shape when required definitions are missing.

### Decision vocabulary

- [ ] Read the exact allowed choices for the current case.
- [ ] Separate checklist classification from operational decision.
- [ ] Use BUY or SELL only when the permitted evidence supports a direction.
- [ ] Use NO TRADE, DNC, WAIT, or UNRESOLVED for the specific condition each term represents.
- [ ] State confidence and identify the controlling missing or invalidating prerequisite.

### Markup and lock

- [ ] Mark HOD and LOD lines, exact prices, and timestamps.
- [ ] Mark the peak/candidate, sequence elements, and decision candle as applicable.
- [ ] Add the decision arrow or crossed-out rejected direction.
- [ ] Add the controlling invalidation or missing prerequisite.
- [ ] Confirm all text is readable and does not hide essential candles.
- [ ] Save to the assigned marked-chart path.
- [ ] Calculate and record SHA-256.
- [ ] Write `FUTURE INFORMATION USED: NO`.
- [ ] Write the Phase-A lock timestamp before any reveal.

## Next-practice plan

### 1. Evidence-labeling drills

Goal: make every material statement traceable to one evidence type.

- Practice on five chart snippets.
- For each statement, write one label only: `EXPLICIT`, `VISUAL`, `IMPLIED`, `INFERRED`, or `UNRESOLVED`.
- Add one sentence explaining why the label fits.
- Review for places where an implied conclusion was accidentally called explicit.

### 2. Calibrated-uncertainty drills

Goal: distinguish invalid, not-yet, cannot-determine, and no-trade states.

- Build a small table of missing-prerequisite scenarios.
- For each scenario, choose among `NO TRADE`, `DNC`, `WAIT`, and `UNRESOLVED` using the case’s allowed vocabulary.
- State the single controlling fact.
- Do not view later candles during the drill.

### 3. Extrema-extraction drills

Goal: make HOD/LOD and HOW/LOW extraction exact and repeatable.

- Practice filtering a multi-day CSV to one printed 24-hour target window.
- Record maximum high/minimum low with full timestamps.
- Add tie handling and endpoint checks.
- Independently repeat the calculation and compare the two extractions.

### 4. Chart-markup drills

Goal: improve visual auditability.

- Use a fixed color legend for HOD, LOD, HOW, LOW, prerequisites, and decisions.
- Mark the decision candle and rejected direction explicitly.
- Run a readability check at full size and reduced size.
- Hash only after the visual check is complete.

### 5. Hindsight-separation drills

Goal: preserve first-answer integrity.

- Write and timestamp a decision from a truncated chart.
- Lock the response.
- Reveal later data and copy the original decision verbatim.
- Describe the later extrema without using later movement to defend or revise the earlier classification.

## Rolling journal — future independent feedback

Copy the blank entry below after each independently reviewed practice session. Feedback should be recorded without altering the original locked attempt.

### Entry ____

- Date:
- Practice case or exercise:
- Independent feedback source:
- Materials permitted:
- Original decision:
- Evidence labels used:
- What the feedback identified:
- What I understood well:
- What remained uncertain:
- Vocabulary correction to practice:
- Extrema-extraction lesson:
- Markup/readability lesson:
- Hindsight-integrity lesson:
- One rule to carry forward:
- Next drill:

### Entry ____

- Date:
- Practice case or exercise:
- Independent feedback source:
- Materials permitted:
- Original decision:
- Evidence labels used:
- What the feedback identified:
- What I understood well:
- What remained uncertain:
- Vocabulary correction to practice:
- Extrema-extraction lesson:
- Markup/readability lesson:
- Hindsight-integrity lesson:
- One rule to carry forward:
- Next drill:

### Entry ____

- Date:
- Practice case or exercise:
- Independent feedback source:
- Materials permitted:
- Original decision:
- Evidence labels used:
- What the feedback identified:
- What I understood well:
- What remained uncertain:
- Vocabulary correction to practice:
- Extrema-extraction lesson:
- Markup/readability lesson:
- Hindsight-integrity lesson:
- One rule to carry forward:
- Next drill:
