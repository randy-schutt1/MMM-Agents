# MMM SOURCE COVERAGE DIAGNOSTIC

**Date:** 2026-08-15
**Scope:** Forensic audit of why the completed 21-video course returns `STUDENT PHASE: INCOMPLETE`,
Reconstruction `PARTIALLY`, Phase 3 `NOT GRANTED` — and which of the ten governing diagnoses
applies to each blocker.
**Authority:** diagnostic only. This file adopts no rules, closes no ambiguities, and does not
populate `12_MASTER_SPEC/` or `13_MACHINE_SPEC/`.

---

## EXECUTIVE CONCLUSION

1. **Is the existing course sufficient?** No. The verdict of `FINAL_COURSE_REVIEW.md` is
   confirmed, not overturned. The blocking primitives — M/W first-leg anatomy, push/level
   segmentation, prospective PFH/PFL, tool construction, and one complete setup lifecycle — are
   **genuinely absent or internally contradicted in the 21-video corpus**, not merely
   mis-extracted.
2. **Were important teachings missed by the pipeline?** Largely no. Transcript verification
   (all 21 verified against audio by 2026-08-14) and Ruffle-based frame capture (577 screenshots,
   mean ~28/lesson) are sound. One systemic capture limit is real: **the instructor repeatedly
   defined structure by pointing/drawing** ("If you see *this*, that's not a trade… *That's* a
   trade" — V02 `[00:35:22]`), across at least V02/V06/V07/V08/V10/V12/V16/V19/V20. Those
   passages carry recoverable visual content that targeted frame-pulls (Phase A) may partially
   recover, but audio+frames cannot conjure boundaries the instructor never stated.
3. **Are more videos required?** Yes — and **~18.9 hours of them are already on disk.** The
   X-series (X01–X03 Dean Malone TDI; X04–X21 `SteveMauro060212`, same instructor) sits in
   `01_SOURCE_VIDEOS/`, inventoried, hashed, and never ingested (anomaly A-03, `OPEN — DEFERRED`).
   Session titles map directly onto the P0/P1 gap list (X07 *Level Count and 4 Trades*, X04
   *Weekly Structure*, X13 *Trap Moves*, X14 *Managing Stop Loss*, X19 *Moving Averages and Pivot
   Points*, X20 *TDI*, X21 *Kar and Kim on DMR*).
4. **What must new videos cover?** M/W first-leg start/end/invalidation; push/level segmentation
   and count reset; prospective PFH/PFL certification; at least one full entry→exit lifecycle;
   live no-lookahead walkthroughs; ADR/pivot/blue-tracer construction.
5. **Which answers cannot come from videos?** High/Low Trainer internals (`.mq4` scripts —
   zero external sources exist), the owner's MT4 templates/parameter dialogs, timezone/DST
   policy, and every genuinely discretionary boundary — these need **owner artifacts and owner
   decisions** (see `MMM_OWNER_QUESTION_PACKET.md`).
6. **Shortest credible route to Phase 3:** Phase A targeted re-extraction of gesture passages →
   owner authorization to ingest X04–X21 (an owner decision already queued as A-03) plus the
   free canonical TDI source → owner question packet for tool artifacts → sealed V11–V21
   practical → re-run reconstruction test. Detail in `MMM_REMEDIATION_AND_RETEST_PLAN.md`.

---

## PART 1 — PER-BLOCKER DIAGNOSIS

Diagnosis codes: (1) present but missed in extraction · (2) present only visually, not captured ·
(3) in repo notes, not integrated · (4) mentioned, never operationally defined · (5) assumed
prerequisite · (6) defined only in proprietary tool · (7) genuinely absent · (8) contradicted
between sources · (9) human-usable but not machine-suitable · (10) adequately covered, review
overly strict.

### H1 — M/W first-leg anatomy

| Sub-question | Diagnosis | Evidence |
|---|---|---|
| First-leg start/end | **7**, with a **2** component | No start rule anywhere V01–V21; best floor is V17 "eight candles minimum". Gesture-only definition attempts recur (V02 `[00:35:22]`–`[00:35:25]`) |
| Leg vs fluctuation | **2 → 7** | Defined by pointing at charts; never verbally bounded |
| Series used (wicks/closes/…) | Partial **10** | Closing-price basis is recorded; the rest open |
| Candle count / duration | **8** | Eight-candle floor exists; second-leg cap is 30M vs 30–45m in the same V19 deck (C-029/C-030) |
| Retracement/overshoot | **4** | "Slightly" never quantified (A-024) |
| Invalidation | **7** | Never stated |
| M vs W differences | **8** | Instructor calls W "exactly the opposite" while the deck prints different caps |
| Neckline/middle | **7** | "Neckline" appears nowhere in the corpus |
| Prospective identifiability | **7** | No live trigger; A-011 open across all 21 lessons |

### H2 — Push / leg / Level 1–3 segmentation

| Sub-question | Diagnosis | Evidence |
|---|---|---|
| What begins/ends a push or level | **8** + **2** | "Level" has two unreconciled Tier-1 senses: drawn price line (V01) vs ordinal leg (V02 slide) (A-004); segmentation shown only by gesture (A-007) |
| Count reset | **7** | No reset rule found (also absent externally) |
| Level–day alignment | **8** | C-001 (3-day vs up-to-5) remains open |
| 22 = second leg of a second leg | **10** for the definition; **4** for its inputs | V02/V15 confirm the definition on multiple ASR engines; "second leg" itself is undefined |
| 33 = three pushes on third day | **8** | V13 Tier-1 push account vs MMM-NOTES Tier-2 level/day account; not mechanically identical |
| 3333 / 3.33 | **7** | Name only (A-097); renderings inconsistent across V15–V17 |
| 22 overshoot tolerance | **4** | "Slightly" unbounded (A-024) |
| Invalidation of 22/33 candidates | **7** | Never stated |

### H3 — Prospective PFH/PFL

| Sub-question | Diagnosis | Evidence |
|---|---|---|
| Live candidate identification | **7** | V10 `[01:14:06]` defines PFH/PFL as the completed week's extreme — inherently retrospective |
| Candidate → confirmed | **4** | "The lock" (price moves away and stays away) has no distance/duration threshold (A-077); the related HOD/LOD lock failed its own backtest (PT-042: 0.35/0.30 vs ≥0.80) |
| Dependence on ADR/TDI/pivots/session | **7** | No linkage taught anywhere |
| Invalidation/relocation | **7** | Absent |
| Object identity (anchor/extreme/zone/event) | **8** | "Anchor", "peak", "lock", "box around the anchor" used interchangeably |

### H4 — Tools and indicators

| Item | Diagnosis | Evidence / resolving artifact |
|---|---|---|
| Blue tracer | **4** | Spoken 15× in V19, never defined (A-133); no credible external source (one closed-source paid MQL5 snippet claims prior-day H/L — unverified) |
| TDI RSI period | **10** | RSI(21) resolved (A-080→A-039). Note: canonical Dean Malone TDI ships RSI(13) — a tool-tier conflict to preserve, not merge |
| TDI signal line / base line / band period | **7**/**4**/**6** | Base-line period "STILL MISSING"; band basis closed only by owner preference (C-021/D-052); band period never stated. Canonical `.mq4` (13/2/7/34/1.6185) is freely available at tool tier |
| Blood in the water / shark fin | **4** | Meanings resolved; computation blocked by band gap |
| ADR lookback / anchor / repaint | **8** | "2 days" vs "2 weeks" vs "15 days" (C-011, V16); "changes during the day" vs "not repaint" 20 s apart (C-022). The sources name a missing "Indicator chart setup day" session |
| Pivot basis / dealer clock | **8** | C-023/C-024: midnight-to-midnight vs daily candle; spoken London-open recut vs printed 2–3 AM EST |
| High/Low Trainer | **6** | Four script filenames legible on camera; zero code in repo; zero external sources exist |
| DMR | **7** (likely **naming confusion**) | Externally DMR = "Daily Market Review" video format, not a tool; X21 covers it |
| MT4 templates/dialogs | **7** in repo | No `.mq4/.ex4/.tpl/.set` anywhere; only 15 MT4 screenshots + text descriptions |

### H5 — Setup lifecycles

Across all ten setups, five lifecycle elements are **NO for every setup**: confirmation, position
sizing, management, exit, no-trade conditions. The closest thing to a complete lifecycle in the
corpus is the V04 W-formation walkthrough (`~[01:03:58]–[01:06:15]`): quantified stop (7 pips +
spread below the day's low) and an ADR watch-trigger, but gesture-only entry, target = "the
water", no invalidation/sizing/no-trade rule. **Diagnosis 7 dominates the lifecycle columns;
no combination of extraction fixes closes them.** Full 10×16 matrix in the audit working papers.

### H6 — Conflict resolution requirements

Of the open contradictions: C-001, C-003, C-004, C-006, C-020, C-022, C-024, C-029, C-030, C-031
require **more Tier-1 instructor material** (several may be answered by X04–X21); C-023 requires
**tool documentation**; C-025/C-026/C-027 are low-severity and closable with lower-tier evidence;
C-021 stands as the model for an explicit **owner-practice decision** correctly recorded at its
tier.

### H7 — Recognition assessment gap

The V01–V10 practical machinery (truncated-chart generation, case-quota validators, lock/hash/
reveal sealing, independent hard gates) is reusable as-is. The blocker is answer keys: blind
positive/negative discrimination of V11–V21 primitives cannot be keyed while A-011/A-004/A-007/
A-010/A-133/A-086/A-100/C-023/A-141 are open. **Buildable today:** stipulated-fact recognition,
retrospective measurement, provenance/contradiction cases, and forced-refusal cases at each
undefined boundary.

---

## PART 6 — ROOT-CAUSE VERDICT

| Blocker | Course coverage | Extraction quality | Retrieval quality | Genuinely absent? | More video needed? | Tool/doc needed? | Owner decision? | Recommended resolution |
|---|---|---|---|---|---|---|---|---|
| M/W first-leg anatomy | Gesture + partial floors | Good; gestures uncapturable in text | Good | **Largely yes** | **Yes** (X04, X06, external M/W lessons) | No | Fallback if sources fail | Phase A frame-pulls at gesture timestamps → X-series → owner markup |
| Push/level segmentation | Two conflicting senses | Good | Good | **Yes** (reset rule absent everywhere) | **Yes** (X07 is the single best candidate) | No | Fallback | X07 ingestion first |
| Prospective PFH/PFL | Retrospective only | Good | Good | **Yes** | Maybe (X04/X05, DMR recordings) | No | **Likely required** | Owner partial-chart protocol; label owner-tier |
| Blue tracer | Named 15×, undefined | Frame-pulls may show the line | Good | In-corpus yes | X07 ("4 Trades/Traces") possible | **Owner MT4 template** | Yes if template lost | Template export request |
| TDI construction | RSI(21) only | Good | Good | Yes beyond RSI period | X01–X03, X20 | **Canonical `.mq4` free (13/2/7/34/1.6185)** | Adoption decision | Acquire source; keep course/tool tiers separate |
| ADR / pivots / clocks | Contradicted | Good | Good | Partially (missing setup session named) | X19 + missing indicator-setup session | Indicator settings/source | DST/timezone ruling | Acquire + owner platform evidence |
| High/Low Trainer | Names + ladder only | N/A | Good | **In-course yes; externally zero sources** | No | **The four `.mq4` files** | Owner must supply | Owner artifact request |
| Complete lifecycle | Best fragment: V04 | Good | Good | **Yes** | **Yes** (X08 *Rules to Profit By*, X14 *Managing Stop Loss*, DMR) | No | Possibly for exits | X-series then owner walkthrough |
| Blind V11–V21 practical | N/A | N/A | N/A | Assessment never built | No | No | Seal/administer | Build after primitives close (Phase D) |

**The ten answers:**

1. **Did the student fail because the repository missed present material?** No — with one
   bounded exception: gesture-defined structure (diagnosis 2) was under-captured and merits a
   targeted Phase A frame-recovery pass. Stale bookkeeping (manifest A-06/I-008 claiming
   unverified transcripts after verification completed) misattributes cause and must be fixed.
2. **Did the course use visuals transcripts couldn't capture?** Yes, systematically — the
   "second leg" was literally defined by pointing (V02 `[00:35:22]`).
3. **Did the instructor assume prerequisite knowledge?** Partially — candlestick vocabulary and
   basic MT4 operation; not the blocking primitives, which he gestured at rather than assumed.
4. **Genuinely absent:** first-leg start/invalidation, level reset rule, prospective PFH/PFL,
   3333 definition, five lifecycle columns (confirmation/sizing/management/exit/no-trade),
   neckline concept, HLT behavior, ADR/pivot construction.
5. **Resolvable by more video:** level counting (X07), weekly structure/timing (X04/X05/X18),
   trap vs stop hunt (X13), stop management (X14), MAs/pivots (X19), TDI (X01–X03, X20), DMR
   walkthroughs (X21 + external DMR playlist).
6. **Require tool files/settings:** TDI (canonical source available), HLT `.mq4` (owner only),
   MT4 templates incl. blue tracer, ADR indicator, pivot indicator, broker/server-time config.
7. **Require owner-practice decisions:** prospective PFH/PFL certification protocol, 22
   overshoot tolerance, timezone/DST policy, entry-ladder integration, any conflict a new
   Tier-1 source fails to settle.
8. **Permanently discretionary / `DO NOT CODE` candidates:** "trading in the middle of the
   range" judgement, dealer-open-volume causation (A-137), spike-as-context, any gesture rule
   the owner cannot state as an event.
9. **Can a competent human learn and trade the method after the additions?** Plausibly yes for
   a discretionary human — if X-series + owner markup close H1–H3 and one lifecycle — but that
   is a hypothesis for Phase D/E to test, not a claim.
10. **Can a machine spec be written without inventing rules?** Not today. After remediation,
    only for whatever subset then has objective inputs; anything else stays at its honest tier.

---

*Working papers for this diagnostic (per-hypothesis audit files with full citations) were
produced in the session scratchpad; their substantive findings are summarized above with their
key citations. Sources: transcripts `02_TRANSCRIPTS/V01–V21`, ambiguity/contradiction ledgers,
`SOURCE_MANIFEST.md`, setup registry, practical suites 19–21, and external web research logged
in `MMM_SUPPLEMENTAL_SOURCE_ACQUISITION_PLAN.md`.*
