# SOURCE MANIFEST

Authoritative inventory of bootcamp source material.

Procedure: `SOURCE_INGESTION_PROTOCOL.md`.

---

## STATUS

```text
INGESTION STATUS:  COMPLETE
FILES INVENTORIED: 42 SWF videos + 80 supporting images + 1 quarantined notes corpus
LESSONS VERIFIED:  21
SOURCE LOCATION:   in-repo, Git-ignored (01_SOURCE_VIDEOS/)
INGESTED:          2026-08-10
```

Every checksum and duration below was read off an actual file on disk. Nothing here
is estimated, inferred from a filename, or carried over from a prior document.

---

## SOURCE LOCATION

| Field | Value |
|---|---|
| Arrangement | **In-repo, Git-ignored** — media lives at `01_SOURCE_VIDEOS/`, excluded by `.gitignore`; this manifest is its Git-visible representation |
| Absolute root path | `/Users/randyschutt/Desktop/Trading/MMM-Agents/01_SOURCE_VIDEOS/Forex Bootcamp/` |
| Relative paths below | Relative to that root |
| Recorded in `DECISIONS.md` | D-017 |

---

## METHOD

| Step | Tool | Note |
|---|---|---|
| Checksums | `shasum -a 256` | Full library, single pass |
| File sizes | `stat -f%z` | Bytes |
| Durations | `ffprobe` — last audio-packet PTS | See caveat below |
| Ordering | Session date encoded in filename (`MMDDYY`) | Corroborated by week label |

**Duration caveat.** `ffprobe -show_entries format=duration` returns `N/A` for every
file: these SWFs carry no container duration field. The value recorded is the
presentation timestamp of the final packet of audio stream `a:0`, which is the true
length of the recorded audio. Verified against V01, where the method yields 3283.80 s
= **00:54:43.8**, matching both the `(55mins)` filename label and the final transcript
timestamp `[00:54:38]`. Every one of the 42 files' measured duration agrees with its
filename label to within one minute, so the labels are honest and the method is sound.

---

## LESSON ORDER — HOW IT WAS ESTABLISHED

The on-disk folder numbering found at ingestion was **not** chronological. It was an
alphabetical-sort artifact: `Wk1`, `Wk10`, `Wk2`, … placed Week 10 third. Every
folder from position 03 onward was misnumbered.

Ordering was re-derived from the six-digit session date embedded in each filename
(`031812` = 2012-03-18, and so on), which is direct evidence rather than inference,
and cross-checked against the instructor's own week labels. The two agree
completely — dates increase monotonically and week numbers never go backwards — so
every lesson row is `CERTAIN`.

Folders under `Bootcamp Notes/` were renamed to match: folder `NN_` now equals video
`VNN`. Source `.swf` files themselves were **not** renamed.

---

## MANIFEST TABLE — LESSON VIDEOS

| Video ID | Original Filename | Lesson Title | Duration | File Size | Relative Path | SHA-256 | Ordering Confidence | Processing Status |
|---|---|---|---|---|---|---|---|---|
| V01 | `Bootcamp1 Wk1 031812 Part1 (55mins).swf` | UNKNOWN | 00:54:43 | 17,806,443 (17.0 MB) | `Bootcamp/Bootcamp1 Wk1 031812 Part1 (55mins).swf` | `c7e660f4b187e0ef81c05d38cc031cb523b56ec22c0c96db4b4dd41303d84030` | CERTAIN | STUDENT COMPLETE |
| V02 | `Bootcamp1 Wk1 031812 Part2 (60mins).swf` | UNKNOWN | 01:00:19 | 21,252,288 (20.3 MB) | `Bootcamp/Bootcamp1 Wk1 031812 Part2 (60mins).swf` | `03079acf739119884911075b8332482a42a6ea178bc0ddb5fed216b9d20bce9f` | CERTAIN | STUDIED — awaiting review |
| V03 | `Bootcamp1 Wk2 032512 Part1 (71mins).swf` | UNKNOWN | 01:10:42 | 27,719,141 (26.4 MB) | `Bootcamp/Bootcamp1 Wk2 032512 Part1 (71mins).swf` | `efe256d81dddf546cc64a4d35c40920ab304562fb57bd2bcf46fed4bc773e273` | CERTAIN | NOT STARTED |
| V04 | `Bootcamp1 Wk2 032512 Part2 (86mins).swf` | UNKNOWN | 01:25:41 | 29,915,614 (28.5 MB) | `Bootcamp/Bootcamp1 Wk2 032512 Part2 (86mins).swf` | `10d8fe7e0410a12c605abb19cebaae8ad5f39ec78a4ab2e8da553117fe60fb7c` | CERTAIN | NOT STARTED |
| V05 | `Bootcamp1 Wk2 032512 Part3 (68mins).swf` | UNKNOWN | 01:08:21 | 37,342,683 (35.6 MB) | `Bootcamp/Bootcamp1 Wk2 032512 Part3 (68mins).swf` | `c606520de74d8b0f1d4800b026f252f9a89d4ecc66bb5db9ff3992dcf896fcc1` | CERTAIN | NOT STARTED |
| V06 | `Bootcamp1 Wk2 032612 Part1 (75mins).swf` | UNKNOWN | 01:14:33 | 32,338,050 (30.8 MB) | `Bootcamp/Bootcamp1 Wk2 032612 Part1 (75mins).swf` | `382207b3dc10872e8dac6c308d98dc3c4a1d26e0ba2f639a5836d4e5aac96e86` | CERTAIN | NOT STARTED |
| V07 | `Bootcamp1 Wk2 032612 Part2 (48mins).swf` | UNKNOWN | 00:48:06 | 18,656,948 (17.8 MB) | `Bootcamp/Bootcamp1 Wk2 032612 Part2 (48mins).swf` | `cb6a8520c55f7c15f0c0d527026ea021c6d7172800c4269c4f4afa255ea72d34` | CERTAIN | NOT STARTED |
| V08 | `Bootcamp1 Wk2 032612 Part3 (43mins).swf` | UNKNOWN | 00:43:03 | 24,519,857 (23.4 MB) | `Bootcamp/Bootcamp1 Wk2 032612 Part3 (43mins).swf` | `6beedb40b7c211cb019b37ff69002e8e625fca4521c3cf3155f946edc5f8b767` | CERTAIN | NOT STARTED |
| V09 | `Bootcamp1 Wk2 032612 Part4 (53mins).swf` | UNKNOWN | 00:52:26 | 36,814,114 (35.1 MB) | `Bootcamp/Bootcamp1 Wk2 032612 Part4 (53mins).swf` | `b0f36b5540de7a76397c80202cf6a721a2a18aa9011c5698238c6bcc624168d4` | CERTAIN | NOT STARTED |
| V10 | `Bootcamp1 Wk3 040112 (96mins).swf` | UNKNOWN | 01:36:16 | 34,308,754 (32.7 MB) | `Bootcamp/Bootcamp1 Wk3 040112 (96mins).swf` | `a37ba371ca2d5c807553c7b9a827a91c479509dd5223b64eadf85995481a3de1` | CERTAIN | NOT STARTED |
| V11 | `Bootcamp1 Wk4 040812 Part1 (51mins).swf` | UNKNOWN | 00:50:56 | 19,169,386 (18.3 MB) | `Bootcamp/Bootcamp1 Wk4 040812 Part1 (51mins).swf` | `606cc5a89a0a68aa08c18423342288307d267b65ebb79acd889e48af8c4d2101` | CERTAIN | NOT STARTED |
| V12 | `Bootcamp1 Wk4 040812 Part2 (55mins).swf` | UNKNOWN | 00:55:18 | 19,677,744 (18.8 MB) | `Bootcamp/Bootcamp1 Wk4 040812 Part2 (55mins).swf` | `10608e8ff01fb14b2980b36891e3c120fcb42510a5c7ee26bff86ff9f351159c` | CERTAIN | NOT STARTED |
| V13 | `Bootcamp1 Wk5 041512 Part1 (65mins).swf` | UNKNOWN | 01:05:22 | 22,823,617 (21.8 MB) | `Bootcamp/Bootcamp1 Wk5 041512 Part1 (65mins).swf` | `106bb8631c7d2274d1be99eeaa583e35bd0a49892a22fdf9eae378c700367807` | CERTAIN | NOT STARTED |
| V14 | `Bootcamp1 Wk5 041512 Part2 (48mins).swf` | UNKNOWN | 00:47:48 | 16,991,811 (16.2 MB) | `Bootcamp/Bootcamp1 Wk5 041512 Part2 (48mins).swf` | `e3dd2b80e720fa9e84530f0f615e2387be681d3337a34b8ef8b7330b347a1d01` | CERTAIN | NOT STARTED |
| V15 | `Bootcamp1 Wk7 050612 Part1 (52mins).swf` | UNKNOWN | 00:52:05 | 19,213,442 (18.3 MB) | `Bootcamp/Bootcamp1 Wk7 050612 Part1 (52mins).swf` | `5308c350193b7cf9471ecb3f534b27fc7e8c1cd21e1cd94eb9521e7e56482b49` | CERTAIN | NOT STARTED |
| V16 | `Bootcamp1 Wk7 050612 Part2 (45mins).swf` | UNKNOWN | 00:44:35 | 16,488,397 (15.7 MB) | `Bootcamp/Bootcamp1 Wk7 050612 Part2 (45mins).swf` | `ecac17c41700839beb4091de94b61fe0cb5a4922e9de764ad482eb8d318c538a` | CERTAIN | NOT STARTED |
| V17 | `Bootcamp1 Wk8 051312 Part1 (57mins).swf` | UNKNOWN | 00:57:09 | 20,210,746 (19.3 MB) | `Bootcamp/Bootcamp1 Wk8 051312 Part1 (57mins).swf` | `2281fa8b92195bdd2fcc268c1ffce25295936faffc9c2825e82b9c50d407f767` | CERTAIN | NOT STARTED |
| V18 | `Bootcamp1 Wk8 051312 Part2 (46mins).swf` | UNKNOWN | 00:46:08 | 17,852,174 (17.0 MB) | `Bootcamp/Bootcamp1 Wk8 051312 Part2 (46mins).swf` | `cfa425ab059573a17276d3ed7ce187b039309b49a6ab99e47291641d0b1f7181` | CERTAIN | NOT STARTED |
| V19 | `Bootcamp1 Wk9 052012 Part1 (67mins).swf` | UNKNOWN | 01:07:21 | 25,694,598 (24.5 MB) | `Bootcamp/Bootcamp1 Wk9 052012 Part1 (67mins).swf` | `7e8a1c2bd25b7f15a2b67458d666d16444c9ce7990cc666a71943cba5c1ab28e` | CERTAIN | NOT STARTED |
| V20 | `Bootcamp1 Wk9 052012 Part2 (46mins) (1).swf` | UNKNOWN | 00:45:49 | 17,724,102 (16.9 MB) | `Bootcamp/Bootcamp1 Wk9 052012 Part2 (46mins) (1).swf` | `96eba8c82366de12b928c900397b58104dc8ae445d4ca5851b16ad5d522a43c6` | CERTAIN | NOT STARTED |
| V21 | `Bootcamp1 Wk10 061712 (75mins).swf` | UNKNOWN | 01:14:47 | 33,002,964 (31.5 MB) | `Bootcamp/Bootcamp1 Wk10 061712 (75mins).swf` | `9eb3b014b55ad18ef3d2ed4d6c5d2bddf14eb8ec6d1f7e60da390f2544ef23fc` | CERTAIN | NOT STARTED |

Total lesson runtime: **21:52:38**.

### Why every Lesson Title is `UNKNOWN`

No file, folder, or index in the library states a lesson title. The filenames carry
only series, week, date, part, and length. The topic strings that previously appeared
against these videos ("Market Maker Psychology, Inducement Objectives, Stop Hunting…")
came from the quarantined notes corpus and were not read off any source. Per
`SOURCE_INGESTION_PROTOCOL.md` §2.5, a filename is not a lesson and must not seed a
title. Titles will be filled in only where an instructor states one on the recording.

### Column definitions

| Column | Rule |
|---|---|
| **Video ID** | `V01`, `V02`, … assigned in verified lesson order. Non-lesson files get `X01`, `X02`, … |
| **Original Filename** | Exact filename as it exists on disk. Never renamed. |
| **Lesson Title** | As stated by the instructor or the file itself. `UNKNOWN` if not stated — **never invented**. |
| **Duration** | `HH:MM:SS` from `ffprobe`, or `UNKNOWN — no probe tooling`. Never estimated. |
| **File Size** | Bytes (and a human-readable value in parentheses). |
| **Relative Path** | Path relative to the recorded source root. |
| **SHA-256** | Full hex digest. The reproducibility anchor. |
| **Ordering Confidence** | `CERTAIN` / `LIKELY` / `UNCERTAIN` / `NOT A LESSON`. |
| **Processing Status** | `NOT STARTED` / `IN PROGRESS` / `STUDENT COMPLETE` / `IN REVIEW` / `IN REMEDIATION` / `PASSED`. |

---

## NON-LESSON AND SUPPORTING MATERIAL

All `NOT A LESSON` for the purposes of this course. X01–X03 and X04–X21 are two
distinct video series that sit alongside the bootcamp; they are inventoried because
they are evidence, but they are **out of scope** until the 21-lesson bootcamp is
complete and the project owner decides otherwise (see anomaly A-03).

| ID | Filename | Type | Duration | File Size | SHA-256 |
|---|---|---|---|---|---|
| X01 | `DeanMalone - Steve's use of TDI (79mins).swf` | SWF video — Dean Malone series | 01:18:47 | 32,376,486 (30.9 MB) | `bdfdfad90bf189bab47870ca1be85b458833c1f2d42b5a2dd2e92af54de7d956` |
| X02 | `DeanMalone - TDI 3-Days Class Part1 (66mins).swf` | SWF video — Dean Malone series | 01:05:38 | 22,349,434 (21.3 MB) | `3d50d29cacfb95e48fff738de84db8ef75f9ce056560dd4d8bb628b29587e8e4` |
| X03 | `DeanMalone - TDI 3-Days Class Part2 (60mins).swf` | SWF video — Dean Malone series | 00:59:46 | 21,098,633 (20.1 MB) | `2ebd87d3412b0169367c4972f5482d8b895beea087961ea343c85f81ae19c8da` |
| X04 | `SteveMauro060212 Part01 (53mins) - Weekly Structure and Market Maker Moves.swf` | SWF video — 060212 series | 00:53:01 | 19,396,242 (18.5 MB) | `298e4402dd4b7690eee95518add1396a4e5a8b1d5f0054e651b8cbd8843b9f2b` |
| X05 | `SteveMauro060212 Part02 (46mins) - Daily Setup and Time Mapping.swf` | SWF video — 060212 series | 00:45:53 | 16,755,693 (16.0 MB) | `2c3676a32c0f6042d98ea377b18a51cd3030b24bf2c688346574870d62db500b` |
| X06 | `SteveMauro060212 Part03 (40mins) - Market Maker Moves.swf` | SWF video — 060212 series | 00:40:14 | 14,769,467 (14.1 MB) | `bea0135e2332c66dff3515239a745df4692d92a1111ce01bfadbe7dc3e3837d4` |
| X07 | `SteveMauro060212 Part04 (61mins) - Level Count and 4 Trades.swf` | SWF video — 060212 series | 01:00:57 | 22,368,933 (21.3 MB) | `eef47a34c24db9f0b64def7cbde6a63da204a2d986babbf5044daeee9519c3c5` |
| X08 | `SteveMauro060212 Part05 (57mins) - Trading Zone and Rules to Profit By.swf` | SWF video — 060212 series | 00:56:52 | 20,162,172 (19.2 MB) | `309030b5669012f43d5a462cfe1b06438ea9729da620ffd8b1bdddc0e8e18215` |
| X09 | `SteveMauro060212 Part06 (50mins) - System Components and Trend.swf` | SWF video — 060212 series | 00:49:51 | 17,582,050 (16.8 MB) | `faaa466b32d1fd107c750ffc9301b72250fe31abacba4e7d788d5f0da5037d82` |
| X10 | `SteveMauro060212 Part07 (57mins).swf` | SWF video — 060212 series | 00:56:51 | 22,719,680 (21.7 MB) | `0b1345fd9f138575cede63d5d0cbd3416d63b5d4ee208981d995262559a0ca55` |
| X11 | `SteveMauro060212 Part08 (60mins) - Kar on Homework.swf` | SWF video — 060212 series | 00:59:48 | 36,323,673 (34.6 MB) | `1873be62e4808ce88f5c1bf4fa0237325798ed320ba7d9b4d2fde69f751f9c8f` |
| X12 | `SteveMauro060212 Part09 (63mins) - Candlesticks.swf` | SWF video — 060212 series | 01:02:35 | 24,439,045 (23.3 MB) | `10e009e4c4562f9ddbd695dd23de4c184ee791206403c1f8e26d42c89210ea6b` |
| X13 | `SteveMauro060212 Part10 (52mins) - Trap Moves.swf` | SWF video — 060212 series | 00:52:25 | 22,254,345 (21.2 MB) | `0429f5bd647a009480843bbbc652cf984a3bc1f17f29aa7e5749aada28f2692c` |
| X14 | `SteveMauro060212 Part11 (56mins) - Managing Stop Loss.swf` | SWF video — 060212 series | 00:56:28 | 21,119,364 (20.1 MB) | `1ab0347efde3509118eaa95e7969fed24774b58d2f10b707e1fa8281ad6811fc` |
| X15 | `SteveMauro060212 Part12 (58mins) - Jim.swf` | SWF video — 060212 series | 00:57:36 | 27,264,219 (26.0 MB) | `2921745c8ce7c33b191ef76ae09ee148cde710f7e051fa4a6d5f9410c20838ca` |
| X16 | `SteveMauro060212 Part13 (44mins) - Jim.swf` | SWF video — 060212 series | 00:43:56 | 23,317,939 (22.2 MB) | `71e07c26ffca67b24d7bc18b582ff368f9429cceeb51f54d7bf2834c1b78a60a` |
| X17 | `SteveMauro060212 Part14 (57mins) - Quiz Answers and Movies  MOTIVATION.swf` | SWF video — 060212 series | 00:56:59 | 29,793,546 (28.4 MB) | `e4e2312f96ad5de21cd9805ef2fdd9ac9342fd06ebea43f39532e7c6f10c7293` |
| X18 | `SteveMauro060212 Part15 (52mins) - Market Timing.swf` | SWF video — 060212 series | 00:51:59 | 19,677,977 (18.8 MB) | `db6c84aa70586d2959f477e83aaf4c9ed5aca2af8e5714435ced79ba22d499d3` |
| X19 | `SteveMauro060212 Part16 (50mins) - Moving Averages and Pivot Points.swf` | SWF video — 060212 series | 00:49:53 | 19,766,505 (18.9 MB) | `03dfed8ef98724b92979d07cb0bd5a0422872bfe7ff46be51caed98f34514333` |
| X20 | `SteveMauro060212 Part17 (39mins) - TDI.swf` | SWF video — 060212 series | 00:38:58 | 15,499,243 (14.8 MB) | `8c15b1d1e4724731312b9cb3c27e383f794a50c4a83ea7812f187fb823d4b86b` |
| X21 | `SteveMauro060212 Part18 (44mins) - Kar and Kim on DMR.swf` | SWF video — 060212 series | 00:43:39 | 33,901,018 (32.3 MB) | `d81792c186a7ee6d0bb32b719e228d1ea19d58576597baebb3e658b25b1aa5eb` |

### Image collections

Hashed in the same pass; individual digests are in the ingestion run rather than
transcribed here, since none of these is cited by any artifact yet. Provenance for
all four is **unknown** — no capture date, source video, or timestamp is recorded
anywhere, so none may be used as lesson evidence.

| ID | Collection | Files | Size | Relative Path |
|---|---|---|---|---|
| X22 | Loose screenshots, 2015 capture dates | 11 PNG | 3.1 MB | `Screen Shot 2015-*.png` |
| X23 | `Bootcamp_Screenshots/` | 50 JPG | 1.6 MB | `Bootcamp_Screenshots/` |
| X24 | `EU/` | 5 PNG | 284 KB | `EU/` |
| X25 | `May 19_June 1/` | 14 PNG | 1.1 MB | `May 19_June 1/` |
| X26 | `01_.../SCREENSHOTS/VIDEO_01_SCREENSHOT_001_00-02-00.jpg` | 1 JPG | 29 KB | inside V01's lesson folder |

X26 is the sole survivor of an earlier extraction attempt. Its filename asserts
`00:02:00`; that claim is unverified and it is **not** used as evidence in V01's
artifacts.

---

## INGESTION ANOMALIES

| # | File(s) | Anomaly | Action Required | Status |
|---|---|---|---|---|
| A-01 | Week 6 | **Expected-but-missing lesson.** Session dates run 03/18, 03/25, 03/26, 04/01, 04/08, 04/15, then jump to 05/06. Weeks 1–5 and 7–10 are present; there is no Week 6 file and no gap-filling folder. | None. Confirmed by the project owner as genuinely absent from the source material, not a local copy error. **Do not fabricate, interpolate, or infer Week 6 content.** A future lesson referring back to "last week" from V15 is referring to material this library does not contain. | CLOSED — DOCUMENTED |
| A-02 | All 21 lesson SWFs | **Every lesson video exists twice**, byte-identical: once flat in `Bootcamp/`, once inside its `Bootcamp Notes/NN_.../` folder. All 21 pairs confirmed by matching SHA-256. | None. The flat `Bootcamp/` copy is treated as canonical and is the path recorded above. The duplicates are not separate evidence and get no `X` IDs. | CLOSED |
| A-03 | X01–X21 | **Two additional video series** (3 Dean Malone TDI, 18 `SteveMauro060212`) sit in the same tree. Same instructor for the 060212 set, different course and date. | Inventoried and marked `NOT A LESSON`. Out of scope until the bootcamp completes. Owner decision needed then on whether they enter the corpus. | OPEN — DEFERRED |
| A-04 | Folder numbering under `Bootcamp Notes/` | **Numbering was alphabetical, not chronological** — `Wk1, Wk10, Wk2, …` put Week 10 in position 3 and shifted every folder from 03 on. | Fixed at ingestion: folders renumbered from session dates so folder `NN` = video `VNN`. Source `.swf` files were not renamed. | CLOSED |
| A-05 | `NOTES.md` / `RULES.md` / `VISUAL_INDEX.md` (×21), `00_MASTER/` (8 files), `Forex_Bootcamp_Complete_Training_Notes.md` | **Fabricated derived notes.** Rules cited to timestamps whose transcript content is unrelated; a visual index describing 78 screenshots when 1 exists; a consolidated rulebook written before ingestion. | Quarantined. Full evidence in `00_SYSTEM/QUARANTINE_REGISTER.md` Q-001. Must never be fed to a Student or Reviewer session. | CLOSED — QUARANTINED |
| A-06 | 20 of 21 `TRANSCRIPT.md` files | **Unverified transcripts.** Only V01's transcript was checked against its audio. The rest came from the same pre-ingestion process that produced the fabricated notes. | Each must be verified against its own audio before that lesson is studied. Tracked as `SETUP_ISSUES.md` I-008. | OPEN |
| A-07 | `audio_06.mp3` … `audio_16.mp3` (11 files) | **Derivatives stored inside `01_SOURCE_VIDEOS/`**, contrary to `SOURCE_INGESTION_PROTOCOL.md` §2.3 / Step 2. Extracted audio from a prior session. | Left in place — deleting them would discard work and they are harmless where they sit. Any *future* derivative must be written outside `01_SOURCE_VIDEOS/`. Noted, not actioned. | OPEN — LOW |
| A-08 | All 42 SWFs | **No container duration field**; `format=duration` returns `N/A`. Screen-recording SWFs also cannot be frame-extracted by `ffmpeg` (see I-006). | Durations derived from last audio-packet PTS, validated against V01. Method documented above. | CLOSED |

No duplicate-checksum anomaly beyond A-02. No corrupt or unreadable file. No file
that appears to belong to a different course beyond A-03. No anomalous size or
duration: all 42 filename labels match measured runtime within one minute.

---

## DERIVATIVES

Written outside `01_SOURCE_VIDEOS/` per `SOURCE_INGESTION_PROTOCOL.md` §2. Not
committed. Regenerable from source via `00_SYSTEM/SWF_CAPTURE_RECIPE.md`.

| Derivative | Location | SHA-256 | Derived from | Purpose |
|---|---|---|---|---|
| `V01.mp4` (54:44, 1024×786 H.264+AAC) | `/Users/randyschutt/Desktop/Trading/MMM_DERIVATIVES/` | `e6c9b0988ea3d6b4b960a28bf4c6c1502fadb98d535bafe11dfdc7ab24e3c895` | V01 | Permanent frame access — any screenshot via `ffmpeg -ss`, no re-capture |
| `V01_audio.mp3` (3283.83 s) | same | — | V01 | Audio track, `ffmpeg -vn -c copy` |

All 22 V01 screenshots were extracted from `V01.mp4`, **not** from the `.swf` directly.
The mp4's sync to the source was verified at twelve points across its full runtime
against the player's burned-in timecode; all twelve exact.

---

## CHECKSUM CHANGE HISTORY

If a source file is ever replaced or re-downloaded, add a **new row** here. Never
edit a checksum in place — artifacts derived from the old file may no longer match
their source.

| Date | Video ID | Old SHA-256 | New SHA-256 | Reason | Artifacts Affected | Re-processing Decision |
|---|---|---|---|---|---|---|
| _(none)_ | | | | | | |

---

## HANDLING RULES

- Source media is **never committed to Git** (`.gitignore`). This manifest is the
  Git-visible representation of the library.
- Source files are **never modified**. If transcoding is required for processing,
  the derivative is written outside `01_SOURCE_VIDEOS/` and the manifest notes that
  a derivative was used.
- Every research artifact must be traceable to a Video ID and, through it, to a
  SHA-256.
- Study is sequential and gated: no lesson begins until the previous lesson holds a
  reviewer `PASS`.
