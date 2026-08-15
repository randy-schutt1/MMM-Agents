# MMM REMEDIATION AND RETEST PLAN

**Date:** 2026-08-15
**Goal:** convert `STUDENT PHASE: INCOMPLETE` / Reconstruction `PARTIALLY` into a legitimate
`YES` without inventing rules. Phases execute in order; no phase pre-empts a later gate.
`12_MASTER_SPEC/` and `13_MACHINE_SPEC/` remain empty throughout this plan.

## Phase A — Recover (existing material only; no external ingestion)

1. **Targeted frame recovery at gesture timestamps.** Using the Ruffle capture pipeline
   (`SWF_CAPTURE_RECIPE.md`), pull dense frame sequences (1–2 fps) around every transcript
   passage where structure was defined deictically — starting with V02 `[00:35:22]` ("I'm going
   to define what a second leg is… If you see this…"), and the equivalent passages in
   V06/V07/V08/V10/V12/V16/V19/V20 identified in the H1/H2 audit. Goal: recover drawn legs,
   levels, and the V19 blue-tracer line visually.
2. **Blue-tracer frame hunt:** capture frames at all 15 V19 "tracer" mentions; check whether the
   line's color/behavior identifies it against the owner's template (Phase C cross-check).
3. **Indicator-dialog hunt:** sweep captured frames for any MT4 properties dialogs missed in the
   curated screenshot sets.
4. **Fix stale bookkeeping** so cause-attribution stays honest: update `SOURCE_MANIFEST.md` A-06
   and `SETUP_ISSUES.md` I-008 to record that all 21 transcripts were verified by 2026-08-14;
   record Ruffle screenshot resolution against I-006.
5. Exit criteria: a `PHASE_A_RECOVERY_REPORT.md` listing every gesture passage, frames captured,
   and whether the visual evidence adds a usable boundary — or explicitly does not.

## Phase B — Acquire

Ranked order (from `MMM_SUPPLEMENTAL_SOURCE_ACQUISITION_PLAN.md`):

1. **Owner ruling on A-03**, then ingest the in-repo X-series in gap order: X07 → X04/X05 →
   X08/X14 → X13 → X19/X20/X18 → X01–X03 → X21 → remainder. Full
   `SOURCE_INGESTION_PROTOCOL.md` treatment: hashes already exist; add transcripts, source
   notes, interpretation notes per lesson.
2. **Free tool source:** download and hash the Dean Malone TDI source (GitHub/EarnForex);
   record 13/2/7/34/1.6185 at tool tier alongside the course-spoken RSI(21) — both preserved.
3. **Wayback Machine** attempt for `btmm_ebook.pdf`.
4. **Browser-inspect** the DMR playlist and Course Day 1/2 re-uploads; record uploader identity,
   dates, durations before any use. Rights-unclear re-uploads are viewed for research
   corroboration only unless provenance clears.
5. **Owner artifacts** per the question packet (templates, HLT scripts, ADR/pivot settings,
   server-time config, trade journals).
6. **Quarantine tier-6 PDFs** (Peak Notes, CrysfoAnalysis 13-EMA rule, Studocu notes) in a
   `RESEARCH_CANDIDATES/` area with explicit `NOT DOCTRINE` banners.
7. Every acquisition logs: source tier, URL, date, hash, timestamps, rights/access status.

## Phase C — Integrate

For each accepted source, in ingestion order: transcript/source notes → separate interpretation
notes → ambiguity ledger updates (close only with the full decision rule, inputs, boundaries,
invalidation, examples) → contradiction ledger updates (supersede, never overwrite) → setup
registry and gap matrix refresh → add positive/negative/borderline/lookalike chart examples.
Cross-course rule: `SteveMauro060212` material is a **different course** (T3) — it may close a
bootcamp gap only with an explicit cross-course provenance note, never silently merged into
V01–V21 doctrine. Owner answers enter at `OWNER EMPIRICAL PRACTICE` tier only.

## Phase D — Validate

1. Build the sealed V11–V21 integrated practical on the existing 19–21 suite machinery:
   HistData development block, hard-truncated charts (no future bars in the file), case quotas
   per the H7 coverage matrix, two-phase lock/hash/reveal seal.
2. Case mix: positive, negative, borderline/insufficient, lookalikes, valid-losers,
   invalid-winners; forced-refusal cases remain for any boundary still undefined after Phase C.
3. Grade every hard gate independently — markup, classification, reasoning, provenance,
   lookahead (`FUTURE INFORMATION USED: NO` required per case), uncertainty. **No aggregate
   score overrides a failed hard gate.** First answers preserved.

## Phase E — Reopen the final gate

1. Repeat the reconstruction test; require `YES`, not `PARTIALLY`.
2. Repeat the official final course review with an independent reviewer session.
3. Populate the Master Specification only if that review explicitly authorizes it; machine
   approximations stay separate from human definitions.
4. No profitability claim without a complete out-of-sample strategy test (the D-035 holdout
   remains sealed until then).

## Safety rules carried through all phases

- No future bars in any entry-time rule; no development-sample finding converted to
  profitability; no indicator name treated as its algorithm; no third-party content promoted to
  doctrine; no gap closed on shared vocabulary alone; unresolved items preserved honestly.
- Diagnostic artifacts (this plan and its three companions) are committed separately from any
  later source ingestion.
