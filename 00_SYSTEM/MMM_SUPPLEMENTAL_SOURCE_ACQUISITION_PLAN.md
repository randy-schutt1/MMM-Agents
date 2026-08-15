# MMM SUPPLEMENTAL SOURCE ACQUISITION PLAN

**Date:** 2026-08-15
**Companion to:** `MMM_SOURCE_COVERAGE_DIAGNOSTIC.md` · machine-readable table:
`MMM_SUPPLEMENTAL_ACQUISITION_TABLE.csv`
**Rules:** a source closes a gap only if it supplies the decision rule, inputs, boundaries,
invalidation, and usable examples. Third-party (T6) material is research-candidate only —
never doctrine. Nothing here is ingested by this plan; ingestion follows
`SOURCE_INGESTION_PROTOCOL.md` and Phase B of the remediation plan.

Tier key: T1 original course material · T2 official Mauro/BTMM upload · T3 original
seminar/webinar recording · T4 instructor-authored notes/manuals/tools · T5 owner practice ·
T6 third-party (quarantine).

---

## THE HEADLINE FINDING

**The highest-value supplemental corpus is already on disk.** `SOURCE_MANIFEST.md` X01–X21
inventories 18.9 hours of hashed, rights-clean video in `01_SOURCE_VIDEOS/`: three Dean Malone
TDI classes and eighteen `SteveMauro060212` sessions (same instructor, ~7 weeks after the
bootcamp). Anomaly A-03 defers them pending an owner decision — **that owner decision is the
single cheapest, highest-yield acquisition action available.** They have zero transcripts and
zero derivatives today.

## Priority 0 — required before reconstruction can pass

| Pri | Missing knowledge | Gap IDs | Candidate | Author/Channel | Location | Date | Duration | Timestamps | Tier | Appears to teach | Must verify | Blocker resolved | Rights/access |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P0 | Push/level counting, tracers | A-004, A-007, A-133 | **X07 — Part04 "Level Count and 4 Trades"** | Steve Mauro | in-repo `01_SOURCE_VIDEOS/` | 2012-06-02 | 1:00:57 | full | **T3** | Level counting method; four trades; possibly tracer identity | Whether a count-reset rule is stated; whether "4 Trades" ≈ the YouTube "4 Traces" tracer content | H2, possibly A-133 | **Owned; owner ingestion decision (A-03)** |
| P0 | Weekly structure, MM moves | A-011, A-010, C-001 | **X04 — Part01 "Weekly Structure and Market Maker Moves"** | Steve Mauro | in-repo | 2012-06-02 | 0:53:01 | full | T3 | Weekly cycle, structure anatomy | First-leg start/invalidation actually stated? | H1/H3 context | Owned; A-03 |
| P0 | Daily setup, session timing | A-019, A-105, A-131 | **X05 — Part02 "Daily Setup and Time Mapping"** | Steve Mauro | in-repo | 2012-06-02 | 0:45:53 | full | T3 | Session/time mapping | Timezone anchors; dealer clock | Clock conflicts (C-024) | Owned; A-03 |
| P0 | Complete lifecycle, exits | H5 columns 5–14 | **X08 "Trading Zone and Rules to Profit By" + X14 "Managing Stop Loss"** | Steve Mauro | in-repo | 2012-06-02 | 0:57 + 0:56 | full | T3 | Trade rules, stop management | Whether any entry→exit path is complete | H5/H6 | Owned; A-03 |
| P0 | Trap vs stop hunt | A-009, A-049, C-006 | **X13 — Part10 "Trap Moves"** | Steve Mauro | in-repo | 2012-06-02 | 0:52:25 | full | T3 | Trap-move anatomy | Discriminator vs stop hunt | SR-23 | Owned; A-03 |
| P0 | Live no-lookahead walkthroughs | H5 col 15 | **DMR playlist ("Daily Market Review")** | re-upload, uploader unverified | youtube.com/playlist?list=PL2e3WEFavy-H2Jvz-eRTXgHCsQlPFYmgg | unk | unk | unk | T3 if authentic | Live market reviews = prospective analysis | Uploader identity, dates, count; **fetch failed — browser inspection required** | H3/H5 prospective evidence | Free; re-upload, rights unclear |
| P0 | Bootcamp Day 1/2 (cycle, M/W) | A-011, A-004 | "BTMM COURSE DAY 1" (bCRbfmuHe2w) + DAY 2 (zgIog6tUarQ) | re-upload | YouTube | unk | unk | unk | T3 if authentic | 3-day/3-level cycle, M = stop hunt high, W = stop hunt low, vectors, Brinks | Watch directly; summary page only was verified | H1/H2 corroboration | Free; re-upload, rights unclear |
| P0 | Canonical doctrine (all) | all | **beatthemarketmaker.com CORE course** | Steve Mauro (official) | beatthemarketmaker.com | current | — | — | **T1** | Current official course + live reviews + forum | Curriculum/pricing (not shown on site) | Any residual P0 after X-series | **Paid — only guaranteed T1 route** |
| P0 | Official ebook | broad | btmm_ebook.pdf via Wayback Machine | Steve Mauro | web.archive.org for beatthemarketmaker.com/ebook/btmm_ebook.pdf | — | — | — | T1 | Unknown; live URL 404s | Snapshot existence | Cheapest possible T1 win | Free if archived |

## Priority 1 — confluence and faithful chart replication

| Pri | Missing knowledge | Gap IDs | Candidate | Author | Location | Tier | Appears to teach | Must verify | Rights |
|---|---|---|---|---|---|---|---|---|---|
| P1 | **TDI construction — RESOLVED at tool tier** | A-086, A-039 | Traders Dynamic Index `.mq4/.mq5` source: RSI 13, price line 2, signal line 7, band 34, StdDev 1.6185 | Dean Malone (EarnForex/GitHub mirror) | earnforex.com/indicators/Traders-Dynamic-Index/ · github.com/EarnForex/Traders-Dynamic-Index | T4-adjacent | Full reproducible TDI | Hash the download; **preserve conflict with course-spoken RSI(21) — do not merge tiers** | Free, source available |
| P1 | TDI as taught by its author | A-085, A-086, C-021 | **X01–X03 Dean Malone TDI classes (3.4 h)** | Dean Malone | in-repo | T3/T4 | TDI settings and reading | Band basis/period stated on tape? | Owned; A-03 |
| P1 | TDI, MAs, pivots as Mauro teaches them | A-039, C-023, C-024 | **X20 "TDI" + X19 "Moving Averages and Pivot Points" + X18 "Market Timing"** | Steve Mauro | in-repo | T3 | Indicator construction/reading | Pivot formula + clock; ADR mentions | Owned; A-03 |
| P1 | Blue tracer, ADR, EMA set as tools | A-133, A-100, C-011, C-022 | MQL5 Market "BTMM" MT5 ports (Multi EMAs / Session Boxes / ADR) — claim: blue tracer = prior-day H/L; ADR + 3×ADR lines | MQL5 vendors porting "original Mauro MT4 tools" | mql5.com/en/market/product/154431 · /154330 · /154444 | T4-adjacent | Tool identities/params | Closed source; snippet claims unverified; repaint undocumented | Paid, closed |
| P1 | DMR format | A-042 | **X21 "Kar and Kim on DMR"** | Mauro students/staff | in-repo | T3 | What DMR actually is | Tool vs video-format question | Owned; A-03 |
| P1 | BTMM TDI variant params | A-086 | TradingView "BTMM|TDI" (The_Trading_Jedi, open source) | third party | tradingview.com/script/ailrNbYh-BTMM-TDI/ | T6 | BTMM-specific TDI settings | Read Pine source; compare vs 13/2/7/34/1.6185 | Free |

## Priority 2 — remaining setup families

| Pri | Missing knowledge | Gap IDs | Candidate | Tier | Must verify | Rights |
|---|---|---|---|---|---|---|
| P2 | Confirmed vs Advanced M/W, Half-Batman types, London types 1–3, railroad tracks | A-022, SR-10..15 | "PATTERNS AND SETUPS.pdf" (CourseHero 100489987) | T4/T6 | Provenance; paywalled | Paid/partial |
| P2 | Stop-hunt definition | A-049 | "BTMM Secrets.pdf" (PDFCoffee) — fetched; defines stop hunt; no 22/ADR/TDI | T4 | Authorship | Free mirror, rights unclear |
| P2 | Peak formation (third-party account) | A-010 | "Peak Notes.pdf" — Atherstone Makaure (PDFCoffee/Studocu/Scribd) | **T6 — quarantine** | Hindsight-flavored by its own text | Free mirrors |
| P2 | Seminar notes (broad) | broad | "Private Study Notes from Seminar of Steve Mauro" (PDFCoffee); "steve mauro's btmm pdf.pdf" (CourseHero, BTMM-branded header) | T4 if genuine | Provenance check mandatory | Free/paywalled |
| P2 | Level definition fragment | A-004 | Studocu seminar notes ("a level is a long sustained run; consolidation days are not levels") | T4/T6 | In-page verification | Account-gated |
| P2 | M/W 13-EMA leg rule (third-party consensus) | A-011 | CrysfoAnalysis walkthrough + repeated T6 claim: "first leg closes beyond 13 EMA; second closes outside then back inside" | **T6 — research hypothesis only** | Needs T1 confirmation; never doctrine | Free |
| P2 | Community live-posted charts | H5 col 15 | Forex Factory threads 816894, M&W-Trading | T6 | — | Free |
| P2 | Candlesticks, quiz answers, homework | prerequisite | X12 "Candlesticks", X17 "Quiz Answers", X11 "Kar on Homework", X15/X16 "Jim" | T3 | — | Owned; A-03 |

**Explicitly rejected:** missionforex.com 11.83 GB course dump — piracy; recorded only as
evidence that the full corpus exists as 4 courses / 101 files. Telegram redistribution archives —
unvetted, rights unclear; do not ingest.

## Items with NO credible external source (owner-only)

1. **High/Low Trainer** — zero external results; the four `.mq4` scripts must come from the owner.
2. **Blue tracer identity** — only a closed-source paid snippet; owner MT4 template is the
   authoritative route (X07 is the one video lead).
3. **ADR construction/repaint** — no formula published anywhere found.
4. **All P2 numerics** — 22 overshoot, 30 vs 30–45 cap, Level-3 thresholds, one-third candle,
   exact stop/target/exit numbers: names appear, numbers do not.

## Part 4 — supporting (non-video) materials to request

| Item | Why | Record on receipt |
|---|---|---|
| Original course PDFs/workbooks, seminar slides | Close H1/H2 print-side | filename, version, hash, source |
| Owner MT4 **templates and profiles** (`.tpl`, profile dir) | Blue tracer, EMA set, chart replication | file, hash, platform, timeframe |
| **High/Low Trainer + DMR `.mq4`** or parameter-dialog screenshots | A-141; only possible source | filename, version, hash, params, source-code availability |
| TDI parameter dialog screenshot from owner's platform | Tier-separates owner practice vs canonical 13/2/7/34/1.6185 | hash, platform |
| ADR + pivot indicator files/settings | C-011/C-022/C-023 | hash, params, repaint test at two intraday times |
| Broker/server-time + DST configuration | A-019/A-105/A-131 | broker, server offset, DST policy |
| Annotated before/after charts; homework answer keys | Positive/negative/borderline examples | provenance per chart |
| Complete trade journals with entry-time screenshots — **including losers and invalid setups** | H5 col 16; anti-survivorship | timestamps, pair, platform |
| Owner-recorded screen walkthroughs of discretionary judgements | Converts gesture knowledge to reviewable evidence | label `OWNER EMPIRICAL PRACTICE` |
