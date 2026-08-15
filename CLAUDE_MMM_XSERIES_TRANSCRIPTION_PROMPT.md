# X-SERIES TRANSCRIPTION AGENT — TASK PROMPT

You are producing verified transcripts for the 21 supplemental videos in the Market Maker Method
repository at `/Users/randyschutt/Desktop/Trading/MMM-Agents`. Work on the current `main` branch.

## Mission

Transcribe all 21 files in
`01_SOURCE_VIDEOS/Forex Bootcamp/More videos/` — three Dean Malone TDI classes and eighteen
`SteveMauro060212` sessions, **18.9 hours total**. These are inventoried in
`00_SYSTEM/SOURCE_MANIFEST.md` as `X01`–`X21` with SHA-256 hashes already recorded.

The 21-video bootcamp (`V01`–`V21`) has been fully studied and its official final review returned
`STUDENT PHASE: INCOMPLETE` because foundational rules were never operationally defined. These
X-series recordings are the leading candidates to supply them. Your job is to produce transcripts
good enough that a later adjudication pass can decide whether they do.

## What you are NOT doing

Read this twice. The project has been damaged before by sessions that exceeded their remit.

- **You are not ingesting these as lessons.** `SOURCE_MANIFEST.md` anomaly `A-03` marks the
  X-series `NOT A LESSON` / `OPEN — DEFERRED`, pending an owner decision that has not been made.
  Transcription is not promotion.
- **Do not close any ambiguity or contradiction.** Do not edit
  `10_AMBIGUITIES/AUTOMATION_AMBIGUITIES.md`, `11_CONTRADICTIONS/CONTRADICTIONS.md`,
  `00_SYSTEM/MMM_SETUP_REGISTRY.md`, `00_SYSTEM/MMM_GAP_AND_DEPENDENCY_MATRIX.md`, or
  `08_CONCEPT_LIBRARY/`.
- **Do not populate** `12_MASTER_SPEC/` or `13_MACHINE_SPEC/`.
- **Do not write interpretation, source notes, or mastery reports.** Those are a later phase with
  its own gates.
- **Do not decide that a gap is answered.** You flag candidate passages with timestamps. Deciding
  what they mean, and at what evidence tier, is a separate pass with owner authority.
- **Never quote the quarantined notes corpus** (`QUARANTINE_REGISTER.md` Q-001/Q-002) or let any
  pre-existing derived notes seed what you expect to hear.

## Hard safety rules

1. **Never modify, rename, move, or re-encode a source file.** Verify each file's SHA-256 against
   `SOURCE_MANIFEST.md` **before** processing and **again after**, and record both. If a hash does
   not match the manifest, **stop and report** — do not proceed on that file.
2. **All derivatives go outside `01_SOURCE_VIDEOS/`**, per `SOURCE_INGESTION_PROTOCOL.md` §2.3.
   Write audio and intermediate files to `/Users/randyschutt/Desktop/Trading/MMM_DERIVATIVES/XSERIES/`.
   (Anomaly `A-07` exists because a previous session violated this. Do not add to it.)
3. **Never commit media.** Audio, video and WAV files stay Git-ignored. Only transcripts, logs and
   memos are committed.
4. Every artifact must be traceable to an `X` ID and through it to a SHA-256.

## Checkpointing — mandatory, not optional

This is a multi-hour job and the workspace has a standing rule about them
(`~/projects/CLAUDE.md` rule 6), written after a 2.5-hour transcription run buffered everything in
memory, was interrupted, and lost all of it because the log recorded only character counts.

- **Write each transcript to disk the moment that file completes.** Never hold results in memory
  across files.
- Use **atomic rename**: write `X07.partial` then `mv` to `X07_TRANSCRIPT.md`.
- **Be resumable**: on start, check what already exists and skip completed files.
- **Log real progress** — file ID, wall-clock, segment count, and a sample of actual transcript
  text, not just "done". A log that records only counts is what made the earlier loss
  unrecoverable.
- Append to `MMM_DERIVATIVES/XSERIES/run.log` continuously.

## Verified tooling and working commands

Confirmed available on this machine: `ffmpeg`, `whisper` (openai-whisper CLI), `whisper-cli`
(whisper.cpp), and Python modules `whisper` and `faster_whisper`.

These SWFs carry **mp3 audio at 22050 Hz stereo** (verified on `Part17`). Audio extraction works
normally even though **frame extraction does not** — `ffmpeg` cannot decode the screen-recording
video layer (`SETUP_ISSUES.md` I-006). You need audio only.

```bash
# Extract and resample to Whisper's expected format
ffmpeg -nostdin -v error -i "<source.swf>" -vn -ac 1 -ar 16000 -c:a pcm_s16le "<out.wav>"
```

Measure true duration from the last audio packet — these files have **no container duration
field** (`format=duration` returns `N/A`, manifest anomaly `A-08`):

```bash
ffprobe -v error -select_streams a:0 -show_entries packet=pts_time -of csv=p=0 "<source.swf>" | tail -1
```

Cross-check that figure against the manifest duration and the filename's minute label. All three
should agree within about a minute. Report any file where they do not.

## Processing order

Process in this order so the highest-value transcripts land first if the run is interrupted:

| Order | ID | File | Why first |
|---|---|---|---|
| 1 | X07 | `Part04 (61mins) - Level Count and 4 Trades` | Level/push segmentation is the #1 blocker (`A-004`, `A-007`); "4 Trades" may also name the tracer |
| 2 | X04 | `Part01 (53mins) - Weekly Structure and Market Maker Moves` | Weekly structure, M/W anatomy (`A-011`) |
| 3 | X13 | `Part10 (52mins) - Trap Moves` | Stop hunt vs trap discriminator (`C-006`, `A-049`) |
| 4 | X14 | `Part11 (56mins) - Managing Stop Loss` | Stops/management — absent for every setup |
| 5 | X19 | `Part16 (50mins) - Moving Averages and Pivot Points` | Pivot construction and clock (`C-023`, `C-024`); EMA set |
| 6 | X20 | `Part17 (39mins) - TDI` | TDI parameters (`A-086`, `A-039`) |
| 7 | X05 | `Part02 (46mins) - Daily Setup and Time Mapping` | Session/timezone anchors (`A-019`, `A-105`, `A-131`) |
| 8 | X08 | `Part05 (57mins) - Trading Zone and Rules to Profit By` | Trade rules, possible lifecycle |
| 9 | X01–X03 | Dean Malone TDI ×3 | TDI from its own author |
| 10 | X21 | `Part18 (44mins) - Kar and Kim on DMR` | What "DMR" actually is (`A-042`) |
| 11 | rest | X06, X09–X12, X15–X18 | Completeness |

## Two-tier verification — the core requirement

A single ASR pass is **not** acceptable output. The corpus already contains a fabricated-notes
incident (`Q-001`) and a period where 20 of 21 transcripts were unverified (`I-008`). Everything
you produce must be checkable.

### Tier 1 — baseline pass (whole file)

Run one primary engine over the full audio with word-level timestamps. Use a large model; these
are 2012 screen recordings with compressed 22 kHz audio and heavy domain vocabulary.

### Tier 2 — high-scrutiny verification (crucial passages)

For every passage matching the trigger list below, you must do **all** of:

1. **Re-run with a second, independent engine** (e.g. openai-whisper and faster-whisper, or
   whisper.cpp as a third). Different implementations fail differently — agreement is evidence,
   disagreement is a finding.
2. **Listen to the passage directly** by extracting that time slice
   (`ffmpeg -ss <start> -t <dur>`) and re-transcribing it in isolation with more context budget.
   Isolated re-transcription of a 30–60 second window frequently resolves what a long-form pass
   garbled.
3. **Preserve every disagreement.** Record what each engine produced. Do **not** silently pick the
   most plausible reading. If engines differ on a number, that is exactly the kind of finding the
   project needs to see.
4. **Flag any number you cannot confirm.** Pip figures, minute counts, candle counts, EMA periods
   and RSI periods are load-bearing and are the most common ASR failure in this corpus.

### What counts as a "crucial passage" — the trigger list

Any window containing these terms, or any numeric quantity spoken near them:

- **Structure:** level, push, first leg, second leg, leg, M formation, W formation, peak
  formation, PFH, PFL, high of the week, low of the week, anchor, neckline, reset, reversal
- **Named setups:** 22 / two-two, 33 / three-three, 3333, safety trade, straight away, outside
  structure, stop hunt, trap, half a batman, railroad tracks, two pins, star, dinosaur
- **Tools:** blue tracer, tracer, TDI, RSI, shark fin, blood in the water, volatility band, market
  base line, signal line, ADR, average daily range, repaint, pivot, dealer, High/Low Trainer, DMR,
  template, indicator, EMA, moving average, mustard, ketchup, water, mayo, blueberry
- **Clocks:** London, New York, Asian, GMT, EST, DST, session, open, close, and any clock time
- **Trade mechanics:** entry, enter, stop loss, stop, target, take profit, exit, lot size, risk,
  percent, pips, spread
- **Any explicit definition attempt:** "what I mean by", "this is called", "the definition of",
  "so a level is", "you'll know it's a", "the rule is"

Also treat as crucial any passage where the speaker appears to be **pointing at or drawing on a
chart** — "right here", "this one", "you see that", "watch this". The bootcamp's central failure
was that structure got defined by gesture and the audio alone did not carry it. **You cannot
recover the visual, but you must mark the timestamp** so a later frame-recovery pass knows exactly
where to look. Maintain a dedicated list of these.

### Known ASR failure modes in this corpus — expect these

Real examples already documented against `V01`–`V21`. They show how badly domain terms degrade:

| ASR produced | Actually was |
|---|---|
| *"A yard"* | `ADR` |
| *"I low market the blue tracer"* | `Use ADR and Hi/Lo Markers` |
| *"the big boy, don't your movie average only"* | `Worked the Big Board` / `Moving AVG Only trades` |
| *"TDI RSI mine"* | TDI RSI **line** |
| *"MarketmakersForks.com"* | `marketmakersforex.com` |

⚠ **A methodological warning about biasing.** Whisper accepts an `initial_prompt` that biases it
toward supplied vocabulary. It is tempting to feed it the domain terms above. **Do not do this for
the baseline pass** — priming an ASR engine with the exact terms you hope to find is a mechanism
for hallucinating them into audio that never contained them, and this project has a fabrication
history that makes that unacceptable. If you use a domain-primed pass at all, use it **only as a
Tier-2 second opinion**, label those transcripts explicitly as prompt-biased, and never let a
primed-only reading stand as the recorded text.

## Output

For each file, write `02_TRANSCRIPTS/XSERIES/<ID>/<ID>_TRANSCRIPT.md` containing:

1. **SOURCE table** — ID, original filename, SHA-256 (verified before *and* after), duration by
   all three methods (audio PTS / manifest / filename label), extraction command used, ASR engine
   and model, date processed.
2. **Speaker note** — who is talking, on what evidence. Do not assume it is Steve Mauro because
   the filename says so; the bootcamp corpus has lessons that are 100% guest-presented. State your
   basis and your confidence.
3. **Body** — verbatim transcript with `[HH:MM:SS]` timestamps, matching the existing convention in
   `02_TRANSCRIPTS/V01/`–`V21/`. **Preserve mishearings in place**; put corrections in brackets
   beside them with the evidence, rather than overwriting.
4. **VERIFICATION section** — which passages got Tier-2 treatment, which engines were used, where
   they agreed, where they disagreed and what each said, and what remains uncertain.
5. **Transcription confidence** rating with reasons.

Then produce two cross-cutting deliverables:

- `02_TRANSCRIPTS/XSERIES/XSERIES_GAP_HIT_INDEX.md` — every trigger-term hit across all 21 files
  as `ID | timestamp | term | one-line quote | which known gap it may bear on`. This is the
  hand-off artifact for the later adjudication pass. **Sort by gap, not by file.**
- `02_TRANSCRIPTS/XSERIES/XSERIES_GESTURE_TIMESTAMPS.md` — every apparent point-at-the-chart moment,
  for the frame-recovery pass.

Finally, write a short `XSERIES_RUN_REPORT.md`: what was processed, what failed, hash
verification results, duration cross-checks, and an honest statement of what the transcripts do
and do not appear to contain. **If the X-series does not answer a gap, say so plainly** — a
negative result here is a genuine finding and directly informs whether more material needs buying.

## Commit discipline

Commit incrementally as transcripts complete, not in one batch at the end. Keep transcripts
separate from any later interpretation work. Suggested message form:

```
docs(xseries): verified transcripts for X07, X04 (level count, weekly structure)

Transcription and verification only. No ambiguity closed, no tier assigned,
no lesson ingested. A-03 remains OPEN — DEFERRED.
```

## Standing principles

Evidence before confidence. Understanding before automation. Preserve what is uncertain rather
than resolving it to look complete. If you cannot verify something, the correct output is to say
so with the timestamp attached.
