#!/usr/bin/env bash
# grab_frames.sh — pull reference stills from the Pt 2 MP4s and the X-series SWFs.
#
#   ./scripts/grab_frames.sh pt2                      all 18 MP4s, 1 frame / 20s
#   ./scripts/grab_frames.sh pt2 "4. Timing" 10       matching files, 1 frame / 10s
#   ./scripts/grab_frames.sh at "5. Using EMAs" 22:22 28:46 34:12
#   ./scripts/grab_frames.sh xseries X20              Ruffle + screen capture (see NOTE)
#   ./scripts/grab_frames.sh keep <file.jpg> V20 34:12 tdi-band-dialog
#
# Output goes to  ~/Desktop/Trading/MMM_DERIVATIVES/FRAMES/  — NOT the repo.
# 04_SCREENSHOTS/ is committed evidence (.gitignore §INTENTIONALLY TRACKED); bulk
# interval frames would run to thousands of files. Promote keepers with `keep`.
set -uo pipefail

SRC="/Users/randyschutt/Desktop/Trading/MMM-Agents/01_SOURCE_VIDEOS"
PT2="$SRC/MMM Forex Bootcamp Pt 2"
XSER="$SRC/Forex Bootcamp/More videos"
OUT="/Users/randyschutt/Desktop/Trading/MMM_DERIVATIVES/FRAMES"
SHOTS="/Users/randyschutt/Desktop/Trading/MMM-Agents/04_SCREENSHOTS"
mkdir -p "$OUT"

hms() { printf '%02d-%02d-%02d' $(( $1/3600 )) $(( ($1%3600)/60 )) $(( $1%60 )); }
tosec() { local t="${1//./:}"; awk -F: '{n=NF; s=0; for(i=1;i<=n;i++) s=s*60+$i; print s}' <<<"$t"; }

# ---------------------------------------------------------------- pt2 (MP4)
cmd_pt2() {
  local filter="${1:-}" every="${2:-20}" n=0
  while IFS= read -r f; do
    local base; base="$(basename "$f" .mp4)"
    local d="$OUT/PT2/$base"; mkdir -p "$d"
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
  echo "✔ $n file(s) → $OUT/PT2"
}

# ------------------------------------------------- at (specific timestamps)
cmd_at() {
  local filter="$1"; shift
  local f; f=$(find "$PT2" "$XSER" -maxdepth 1 \( -name "*.mp4" -o -name "*.swf" \) | grep -i -- "$filter" | head -1)
  [ -z "$f" ] && { echo "no match for '$filter'"; exit 1; }
  case "$f" in *.swf) echo "⚠ $f is an SWF — use 'xseries'. ffmpeg cannot composite these."; exit 1;; esac
  local base; base="$(basename "$f" .mp4)"; local d="$OUT/PT2/$base"; mkdir -p "$d"
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
  local base; base="$(basename "$f" .swf)"; local d="$OUT/XSERIES/$base"; mkdir -p "$d"
  echo "▸ $base — launching Ruffle. Put it fullscreen; capture starts in 12s."
  echo "  Ctrl-C to stop. Frames → $d"
  "$XSER/Ruffle.app/Contents/MacOS/ruffle" "$f" >/dev/null 2>&1 &
  local pid=$!; sleep 12
  local i=0
  while kill -0 $pid 2>/dev/null; do
    screencapture -x -t jpg "$d/$(hms $((i*every))).jpg" 2>/dev/null
    i=$((i+1)); sleep "$every"
  done
  echo "✔ $i frames → $d"
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
  xseries) shift; cmd_xseries "$@" ;;
  keep)    shift; cmd_keep "$@" ;;
  *) sed -n '2,16p' "$0" ;;
esac
