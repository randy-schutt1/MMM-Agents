# Claude MMM Diagnostic and Remediation Audit Prompt

You are conducting a forensic diagnostic and remediation audit of the Market Maker Method
repository located at:

`/Users/randyschutt/Desktop/Trading/MMM-Agents`

Work on the current `main` branch.

## Mission

The 21-video course has been fully ingested and reviewed. The targeted student remediation passed,
the 75% cumulative review passed with corrections, but the official final course review returned:

- `STUDENT PHASE: INCOMPLETE`
- Reconstruction: `PARTIALLY`
- Phase 3 authorization: `NOT GRANTED`

Your job is to determine exactly why the completed course still cannot produce a highly competent
MMM/BTMM agent and then design the evidence-acquisition and remediation program needed to resolve
it.

This is not a generic strategy summary. It is a source-forensic audit.

## Governing rule

Do not assume that “21 videos completed” means every required trading decision was actually taught.

For every missing rule, determine which of these diagnoses applies:

1. Present in the existing videos but missed during transcription or note-taking.
2. Present visually through chart gestures, drawing, cursor movement, or indicator display but not
   captured adequately.
3. Present in repository notes or supporting documents but not integrated into the knowledge system.
4. Mentioned but never operationally defined.
5. Assumed prerequisite knowledge that the instructor expected students to know.
6. Defined only in a proprietary indicator, template, or tool.
7. Genuinely absent from the course.
8. Contradicted by another lesson or source.
9. Understood by a human but still unsuitable for machine implementation.
10. Already adequately covered—the final review was overly strict or relied on a stale record.

Do not select thresholds, definitions, or rules merely to make the system complete.

## Mandatory starting files

Read these first:

1. `18_REVIEW/FINAL_COURSE_REVIEW.md`
2. `00_SYSTEM/MMM_GAP_AND_DEPENDENCY_MATRIX.md`
3. `00_SYSTEM/MMM_SETUP_REGISTRY.md`
4. `00_SYSTEM/MMM_CURRENT_STATE.md`
5. `00_SYSTEM/COURSE_PROGRESS.md`
6. `18_REVIEW/REVIEW_INDEX.md`
7. `18_REVIEW/CUMULATIVE_25.md`
8. `18_REVIEW/CUMULATIVE_50.md`
9. `18_REVIEW/CUMULATIVE_75.md`
10. `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`
11. `11_CONTRADICTIONS/CONTRADICTIONS.md`
12. `08_CONCEPT_LIBRARY/CONCEPT_INDEX.md`
13. `06_MANUAL_BACKTEST/cumulative/CUMULATIVE_SUMMARY.md`
14. `00_SYSTEM/SOURCE_MANIFEST.md`

Then inspect the relevant transcripts, source notes, interpretation files, screenshots, mastery
reports, and reviews for V01–V21.

Do not rely only on indexes or summaries. Verify important conclusions against transcripts,
screenshots, audio-derived evidence, and original lesson records.

## Part 1 — Audit whether the existing course was misunderstood

For every blocking item below, audit all 21 videos and their visual evidence.

### H1 — M/W first-leg anatomy

Determine whether the course defines:

- Where the first leg begins.
- Where it ends.
- What makes the move a leg rather than ordinary fluctuation.
- Whether the formation uses wicks, closes, pivots, TDI, or another series.
- Required candle count or duration.
- Permitted retracement or overshoot.
- What invalidates the first leg.
- How M and W rules differ.
- How first leg, second leg, neckline/middle, and entry leg relate.
- Whether the pattern can be identified prospectively.

Audit gap IDs including `A-011`, `A-007`, `C-029`, and `C-030`.

### H2 — Push, leg, and Level 1–3 segmentation

Determine whether the course defines:

- What begins and ends a push.
- What begins and ends a level.
- Whether levels are ordinal legs, price zones, ADR divisions, session phases, or another object.
- When level counting resets.
- How Levels 1, 2, and 3 align with days.
- How 22 relates to “second leg of a second leg.”
- How 33 relates to “three pushes on the third day of rise.”
- Whether 3333/3.33 is ever defined.
- How much overshoot is allowed in a 22.
- What invalidates 22 and 33 candidates.

Audit `A-004`, `A-007`, `A-023`, `A-024`, `A-097`, and `A-138`.

### H3 — Prospective PFH/PFL identification

Determine:

- How a trader identifies a candidate PFH/PFL before the week is complete.
- When a candidate becomes confirmed.
- Whether confirmation depends on time, ADR, TDI, pivots, M/W completion, session behavior, or
  subsequent price.
- How to avoid selecting the weekly high or low with hindsight.
- Whether the course teaches only retrospective labeling.
- What invalidates or relocates the candidate.
- Whether PFH/PFL is an anchor, extreme, pattern, zone, or completed event.

Audit `A-010`, `A-056`, `A-061`, and all PFH/PFL examples.

### H4 — Tool and indicator definitions

Audit:

- Blue tracer identity: period, indicator type, input series, timeframe, and role.
- TDI construction: RSI period, price input, signal line, market base line, volatility-band period
  and multiplier.
- Definitions of blood in the water and shark fin.
- ADR lookback, session boundary, update behavior, and repaint behavior.
- Pivot construction and dealer/London clock.
- High/Low Trainer and DMR tool behavior.
- Relevant MT4 templates, `.mq4`, `.ex4`, indicator dialogs, screenshots, or manuals.

Audit `A-086`, `A-100`, `A-133`, `A-141`, `C-011`, `C-022`, `C-023`, and `C-024`.

Do not infer an algorithm from an indicator name or screenshot.

### H5 — Complete setup lifecycle

For each of these setups, determine whether the repository contains a complete lifecycle:

- 22 / 2-2.
- 33 / 3-3.
- PFH + M.
- PFL + W.
- Safety Trade.
- Stop Hunt High M.
- Stop Hunt Low W.
- Outside Structure.
- Hi-Lo entry.
- Owner M15 5/13 timing gate.

A complete lifecycle requires:

1. Market and weekly context.
2. Directional bias.
3. Setup recognition.
4. Required sequence.
5. Confirmation.
6. Exact entry event.
7. Entry timing and timeframe.
8. Invalidation.
9. Stop placement.
10. Position-sizing inputs.
11. Target.
12. Management.
13. Exit.
14. No-trade conditions.
15. Prospective observability.
16. Positive, negative, borderline, and lookalike examples.

Do not combine disconnected statements from different source tiers unless the combination is
explicitly labeled as a proposed synthesis.

### H6 — Conflicts and owner decisions

Determine which unresolved conflicts require:

- More Tier-1 instructor material.
- A lower-tier supporting source.
- Proprietary tool documentation.
- An explicit owner-practice decision.
- Empirical research after human definitions are established.

Do not let an owner decision silently rewrite what the course taught. Preserve separate evidence
tiers.

### H7 — Recognition assessment gap

Determine what is required to create a sealed V11–V21 practical containing:

- Visible-only partial charts.
- No future bars.
- Positive cases.
- Negative cases.
- Borderline/insufficient cases.
- Lookalikes.
- Valid setups that lose.
- Invalid setups that later win.
- Separate hard gates for markup, classification, reasoning, provenance, lookahead, and uncertainty.

## Part 2 — Search for supplemental evidence

After auditing the existing repository, conduct a web and YouTube research audit.

Search original Steve Mauro, BTMM, Market Maker Method, and related primary-source material first.

Use searches including, but not limited to:

- `Steve Mauro M formation W formation first leg second leg`
- `Steve Mauro BTMM M and W formation complete`
- `BTMM how to count levels pushes Level 1 Level 2 Level 3`
- `Steve Mauro 22 trade second leg of second leg`
- `Steve Mauro 33 trade three pushes third day`
- `BTMM peak formation high peak formation low live`
- `BTMM prospective PFH PFL`
- `Steve Mauro Safety Trade seven points`
- `BTMM complete trade setup entry stop target`
- `Steve Mauro TDI blood in the water shark fin settings`
- `BTMM TDI volatility band settings`
- `BTMM blue tracer`
- `BTMM ADR indicator settings repaint`
- `Steve Mauro pivots dealer time London`
- `BTMM High Low Trainer DMR`
- `BTMM stop hunt versus trap`
- `BTMM outside structure`
- `BTMM half Batman`
- `BTMM railroad tracks two pins`
- `BTMM 3333 trade`
- `Steve Mauro session times timezone DST`
- `BTMM live chart analysis M W PFH PFL`
- `BTMM full trade walkthrough`
- `Steve Mauro trade review entry stop target exit`

For every candidate video, directly inspect the video, transcript, captions, frames, description,
and source identity. A title or search snippet is not evidence.

Prioritize sources in this order:

1. Original instructor/course material.
2. Official Steve Mauro or official BTMM uploads.
3. Original seminar/webinar recordings.
4. Instructor-authored notes, manuals, slides, and tools.
5. Owner-supplied practice rules, clearly labeled as owner practice.
6. High-quality third-party explanations, kept as lower-tier research candidates only.

Do not silently promote third-party coaching content into course doctrine.

## Part 3 — Produce an exact acquisition list

Create a ranked acquisition table with these columns:

| Priority | Missing knowledge | Gap IDs | Candidate title | Channel/author | URL | Date | Duration | Relevant timestamps | Source tier | What it appears to teach | What must be verified | Expected blocker resolved | Rights/access status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Separate the list into:

### Priority 0 — Required before reconstruction can pass

Find material covering:

1. M/W first-leg anatomy and invalidation.
2. Push/leg/Level 1–3 segmentation.
3. Prospective PFH/PFL identification.
4. At least one complete setup lifecycle.
5. No-lookahead live chart walkthroughs.

### Priority 1 — Required for confluence and faithful chart replication

Find material covering:

1. Blue tracer identity.
2. TDI parameters and signal definitions.
3. ADR construction and repaint/update behavior.
4. Pivot calculation and dealer-time mapping.
5. High/Low Trainer or DMR tool documentation/source.

### Priority 2 — Required for remaining setup families

Find material covering:

1. 22 overshoot tolerance.
2. M/W 30-minute versus 30–45-minute conflict.
3. Outside-structure boundaries.
4. Stop hunt versus trap.
5. Level-3 quantification.
6. One-third entry-candle selection.
7. Half-Batman, upside-down Half-Batman, railroad tracks, two pins, stars, and 3333.
8. Exact stop, target, management, and exit rules.

## Part 4 — Supporting information to request

Produce a second acquisition list for non-video materials:

- Original course PDFs and workbooks.
- Seminar notes and slide decks.
- Annotated before/after charts.
- Homework answer keys.
- MT4 templates and profiles.
- TDI source code or parameter-dialog screenshots.
- ADR and pivot source/settings.
- Blue-tracer indicator identity and settings.
- High/Low Trainer and DMR `.mq4`, documentation, or parameter screenshots.
- Broker/server-time and DST configuration.
- Complete trade journals showing entry-time screenshots.
- Losing examples and invalid setups, not only winners.
- Owner-recorded screen walkthroughs explaining discretionary judgments.

For every proprietary file, record filename, version, hash, parameters, platform, timeframe, and
whether source code is available.

## Part 5 — Owner questions when no source exists

If the missing rule cannot be found, produce a concise owner-question packet.

Each question must request an operational answer and examples. For example:

- “Mark where the first leg of this M begins and ends. What exact event would make that marking
  wrong?”
- “On these three charts, mark each push and Level 1–3. State when the count resets.”
- “At this partial-chart cutoff, is this PFH/PFL merely a candidate or confirmed? What information
  available now makes that decision?”
- “Show one complete 22 trade from context through exit, including invalidation.”
- “Show one complete Safety Trade and identify which seven checklist points are satisfied at entry
  time.”
- “What exact indicator is the blue tracer?”
- “Provide the complete TDI parameters visible in your platform.”
- “Which timezone and DST policy control each session and pivot calculation?”

Require positive, negative, and borderline chart examples for every discretionary answer.

Owner answers must be labeled `OWNER EMPIRICAL PRACTICE`, not retroactively treated as Tier-1
course doctrine.

## Part 6 — Root-cause verdict

Produce a root-cause table:

| Blocker | Existing course coverage | Extraction quality | Retrieval quality | Genuine source absence? | Additional video needed? | Tool/document needed? | Owner decision needed? | Recommended resolution |
|---|---|---|---|---|---|---|---|---|

Then answer:

1. Did the student fail because the repository missed material that was present?
2. Did the course use visuals or gestures that the transcript could not capture?
3. Did the instructor assume prerequisite knowledge?
4. Which rules are genuinely absent?
5. Which missing rules can be resolved by more videos?
6. Which require tool files or indicator settings?
7. Which require an owner-practice decision?
8. Which should remain permanently discretionary or `DO NOT CODE`?
9. Can a competent human learn and trade the method after the proposed additions?
10. Can a machine specification be written without inventing rules?

## Part 7 — Remediation plan

Design the solution in this order:

### Phase A — Recover

- Reinspect existing videos, audio, screenshots, gestures, and supporting documents.
- Correct missed extraction or indexing.
- Do not add external material yet.

### Phase B — Acquire

- Obtain the ranked supplemental videos and supporting artifacts.
- Record source tier, URL, date, hashes, timestamps, and rights/access status.
- Quarantine unverified third-party interpretations.

### Phase C — Integrate

For each accepted source:

- Create transcript/source notes.
- Create interpretation notes separately.
- Update ambiguity and contradiction ledgers.
- Update setup registry and dependency matrix.
- Add positive, negative, borderline, and lookalike chart examples.
- Preserve superseded statements instead of silently overwriting them.

### Phase D — Validate

- Create a sealed V11–V21 integrated chart practical.
- Use partial charts with future bars hidden.
- Preserve first answers.
- Grade every hard gate independently.
- Require explicit `FUTURE INFORMATION USED: NO`.
- Do not allow aggregate score to override a failed hard gate.

### Phase E — Reopen the final gate

Only after the new evidence and assessment are complete:

1. Repeat the reconstruction test.
2. Require `YES`, not `PARTIALLY`.
3. Repeat the official final course review.
4. Populate the Master Specification only if explicitly authorized.
5. Keep machine approximations separate from human definitions.
6. Do not claim profitability without a complete OOS strategy test.

## Required deliverables

Create:

1. `00_SYSTEM/MMM_SOURCE_COVERAGE_DIAGNOSTIC.md`
2. `00_SYSTEM/MMM_SUPPLEMENTAL_SOURCE_ACQUISITION_PLAN.md`
3. `00_SYSTEM/MMM_OWNER_QUESTION_PACKET.md`
4. `00_SYSTEM/MMM_REMEDIATION_AND_RETEST_PLAN.md`
5. A CSV or Markdown acquisition table of candidate videos and supporting files.
6. A concise executive conclusion answering:

   - Is the existing course sufficient?
   - Were important teachings missed?
   - Are more videos required?
   - Exactly what subjects must those videos cover?
   - Which missing answers cannot be obtained from videos?
   - What is the shortest credible route to Phase 3 authorization?

## Safety and evidence rules

- Do not populate `12_MASTER_SPEC/` or `13_MACHINE_SPEC/`.
- Do not claim a trading edge.
- Do not use future bars to define entry-time rules.
- Do not convert development-sample findings into profitability.
- Do not treat an indicator name as proof of its algorithm.
- Do not treat third-party content as instructor doctrine.
- Do not close a gap because a source uses the same vocabulary.
- A source closes a gap only if it supplies the missing decision rule, inputs, boundaries,
  invalidation, and usable examples.
- Preserve unresolved items honestly.
- Commit the diagnostic artifacts separately from any later source ingestion.

Lead the final report with the direct answer, not the process.
