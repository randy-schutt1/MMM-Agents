# V1 Scope Charter
**Approved by owner (Randy Schutt): 2026-08-16**
**Governing plan:** `/Users/randyschutt/Desktop/Trading/Audit/MASTER_A_PLAN_2026-08-16.md`

## Scope (locked)
- **Instrument:** GBPUSD only
- **Feed:** one named data feed (to be pinned at Phase 4 feature-engine build; HistData for historical work)
- **Timeframes:** H1 context + M15 decision
- **Clock:** one New York timezone/DST session contract (versioned table to be produced in Phase 1)
- **Decision basis:** bar-close only
- **V1 task:** market-state + WATCH/NO_TRADE classification first. **Entries/stops/targets are NOT in V1** — they arrive in Phase 8 only after blind-recognition gates pass. If P0 primitives pass, V1 may include one mirrored setup family: PFH+M / PFL+W.

## Evidence policy (four tiers)
1. **Course doctrine** — verified Bootcamp core teaching (Tier 1)
2. **Supplemental presenter material** — Part 2 / More Videos / guest presenters (Malone TDI etc.), never silently merged into doctrine
3. **Owner/research rules** — human-panel operational definitions, always labeled as such
4. **Empirical approximations** — data-derived conventions, never called MMM doctrine

## Transcript verification policy (owner decision 2026-08-16)
**Targeted verification.** Only spans carrying rule evidence (blue tracer, TDI parameters, session clocks, ADR, M/W timing, pivot construction, stop-hunt/trap language) are verified frame-accurate against the video before promotion. All other ASR content stays marked unverified and cannot be promoted to any tier above provisional.

## Standing rules
- No invented parameters: an unsourced rule is excluded, not guessed.
- No self-grading: labels, subject, and grader come from different lineages.
- `22_AGENT_BENCHMARK` is a development smoke test; its results are not competence evidence.
- Change control: any source decision, feature formula, label rule, or prompt change is versioned and can invalidate prior evaluation.
- Deferred from V1 (explicit): all named-only patterns (22, 33, 3333, Batman variants, Dinosaur, stars, RR tracks, safety trade), M1–M4 pivot layer, multi-pair, entries/execution.
