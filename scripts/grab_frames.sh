#!/usr/bin/env bash
# grab_frames.sh — pull reference stills from the Pt 2 MP4s and the X-series SWFs.
#
#   ./scripts/grab_frames.sh pt2                      all 18 MP4s, 1 frame / 20s
#   ./scripts/grab_frames.sh pt2 "4. Timing" 10       matching files, 1 frame / 10s
#   ./scripts/grab_frames.sh at "5. Using EMAs" 22:22 28:46 34:12
#   ./scripts/grab_frames.sh xseries X20            one SWF via Ruffle + screen capture
#   ./scripts/grab_frames.sh xseries-all            the six §17 priority files, in order
#   ./scripts/grab_frames.sh keep <file.jpg> V20 34:12 tdi-band-dialog
#
# Pt 2 frames  → 01_SOURCE_VIDEOS/MMM Forex Bootcamp Pt 2/MMM pt2 Screenshots/
# X-series     → 01_SOURCE_VIDEOS/Forex Bootcamp/More videos/X-series Screenshots/
# Neither is in the repo tree that git tracks; promote keepers with `keep`.
set -uo pipefail

SRC="/Users/randyschutt/Desktop/Trading/MMM-Agents/01_SOURCE_VIDEOS"
PT2="$SRC/MMM Forex Bootcamp Pt 2"
XSER="$SRC/Forex Bootcamp/More videos"
OUT_PT2="$PT2/MMM pt2 Screenshots"
OUT_X="$XSER/X-series Screenshots"
SHOTS="/Users/randyschutt/Desktop/Trading/MMM-Agents/04_SCREENSHOTS"
mkdir -p "$OUT_PT2" "$OUT_X"

hms() { printf '%02d-%02d-%02d' $(( $1/3600 )) $(( ($1%3600)/60 )) $(( $1%60 )); }
tosec() { local t="${1//./:}"; awk -F: '{n=NF; s=0; for(i=1;i<=n;i++) s=s*60+$i; print s}' <<<"$t"; }

# ---------------------------------------------------------------- pt2 (MP4)
cmd_pt2() {
  local filter="${1:-}" every="${2:-20}" n=0
  while IFS= read -r f; do
    local base; base="$(basename "$f" .mp4)"
    local d="$OUT_PT2/$base"; mkdir -p "$d"
    local dur; dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f" | cut -d. -f1)
    echo "▸ $base  (${dur}s, 1/${every}s → ~$((dur/every)) frames)"
    # -vsync passthrough + fps filter: one decode pass, deterministic spacing
    ffmpeg -nostdin -v error -i "$f" -vf "fps=1/$every" -q:v 3 \
           -frame_pts 1 "$d/${base// /_}_%04d.jpg" </dev/null
    # rename sequence index → real timestamp
    local i=0
    for img in "$d"/*_[0-9][0-9][0-9][0-9].jpg; do
      [ -e "$img" ] || break
      mv -n "$img" "$d/$(hms $((i*every))).jpg" 2>/dev/null
      i=$((i+1))
    done
    n=$((n+1))
  done < <(find "$PT2" -maxdepth 1 -name "*.mp4" | grep -i -- "$filter" | sort)
  echo "✔ $n file(s) → $OUT_PT2"
}

# ------------------------------------------------- at (specific timestamps)
cmd_at() {
  local filter="$1"; shift
  local f; f=$(find "$PT2" "$XSER" -maxdepth 1 \( -name "*.mp4" -o -name "*.swf" \) | grep -i -- "$filter" | head -1)
  [ -z "$f" ] && { echo "no match for '$filter'"; exit 1; }
  case "$f" in *.swf) echo "⚠ $f is an SWF — use 'xseries'. ffmpeg cannot composite these."; exit 1;; esac
  local base; base="$(basename "$f" .mp4)"; local d="$OUT_PT2/$base"; mkdir -p "$d"
  for t in "$@"; do
    local s; s=$(tosec "$t")
    ffmpeg -nostdin -v error -ss "$s" -i "$f" -frames:v 1 -q:v 2 -update 1 -y "$d/$(hms "$s").jpg" </dev/null \
      && echo "  ✔ $(hms "$s").jpg"
  done
  echo "→ $d"
}

# ------------------------------------------------------------ xseries (SWF)
# NOTE: the SWF video layer is MJPEG 1280x720 at 3fps, but it is stored as
# DIRTY-RECTANGLE partial updates — one full keyframe per file, everything else
# a small region patch with no offsets ffmpeg can use. Verified 2026-08-15 on
# X20: 1490 JPEGs extracted, exactly 1 at 1280x720. So frames must be captured
# from a RENDERER, not the container. That is SETUP_ISSUES.md I-006, refined.
# Requires: System Settings → Privacy → Screen Recording → allow Terminal.
cmd_xseries() {
  local filter="${1:-}" every="${2:-15}"
  local f; f=$(find "$XSER" -maxdepth 1 -name "*.swf" | grep -i -- "$filter" | head -1)
  [ -z "$f" ] && { echo "no SWF matching '$filter'"; exit 1; }
  local base; base="$(basename "$f" .swf)"; local d="$OUT_X/$base"; mkdir -p "$d"

  # true duration = last audio packet PTS (SWFs carry no container duration —
  # SOURCE_MANIFEST anomaly A-08)
  local dur; dur=$(ffprobe -v error -select_streams a:0 -show_entries packet=pts_time \
                   -of csv=p=0 "$f" 2>/dev/null | tail -1 | cut -d. -f1)
  [ -z "$dur" ] && dur=3600
  echo "▸ $base — ${dur}s real-time, 1/${every}s → ~$((dur/every)) frames"

  "$XSER/Ruffle.app/Contents/MacOS/ruffle" --volume 0 --width 1280 --height 720 \
      -q high "$f" >/dev/null 2>&1 &
  local pid=$!
  sleep 8
  # park the window at 0,0 so we can capture just its region instead of the
  # whole desktop; if this fails we fall back to a full-screen grab
  local region="0,0,1280,760"
  osascript -e 'tell application "System Events" to tell (first process whose name contains "ruffle") to set position of front window to {0, 0}' >/dev/null 2>&1 \
    || region=""
  sleep 4

  local i=0 t0; t0=$(date +%s)
  while kill -0 $pid 2>/dev/null; do
    local now; now=$(( $(date +%s) - t0 ))
    [ "$now" -gt "$dur" ] && break
    if [ -n "$region" ]; then
      screencapture -x -R "$region" -t jpg "$d/$(hms "$now").jpg" 2>/dev/null
    else
      screencapture -x -t jpg "$d/$(hms "$now").jpg" 2>/dev/null
    fi
    i=$((i+1)); sleep "$every"
  done
  kill $pid 2>/dev/null; wait $pid 2>/dev/null
  echo "✔ $i frames → $d"
}

# priority order from XSERIES_GAP_HIT_INDEX.md §17
cmd_xseries_all() {
  local every="${1:-15}"
  for k in "Steve's use of TDI" "Trap Moves" "Quiz Answers" "Daily Setup" \
           "Moving Averages" "Part17 (39mins) - TDI"; do
    cmd_xseries "$k" "$every"
  done
}

# ------------------------------------------- keep (promote into the repo)
cmd_keep() {
  local img="$1" vid="$2" ts="$3" slug="$4"
  local d="$SHOTS/$vid"; mkdir -p "$d"
  local dest="$d/${vid}_$(hms "$(tosec "$ts")")_${slug}.png"
  sips -s format png "$img" --out "$dest" >/dev/null
  echo "✔ $dest"
  echo "  ↳ add a row to $d/INDEX.md describing what it shows and why it matters."
}

case "${1:-}" in
  pt2)     shift; cmd_pt2 "$@" ;;
  at)      shift; cmd_at "$@" ;;
  xseries)     shift; cmd_xseries "$@" ;;
  xseries-all) shift; cmd_xseries_all "$@" ;;
  keep)    shift; cmd_keep "$@" ;;
  *) sed -n '2,16p' "$0" ;;
esac
