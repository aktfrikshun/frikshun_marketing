#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ARCHIVE_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)
COVER_SOURCE="$ARCHIVE_ROOT/site/assets/images/rodnoy-dom-cover-v1.png"
AUDIO_SOURCE="$ARCHIVE_ROOT/site/assets/audio/rodnoy-dom.wav"
PYTHON_BIN=${PYTHON_BIN:-python3}

cp "$COVER_SOURCE" "$SCRIPT_DIR/rodnoy-dom-cover.png"
"$PYTHON_BIN" "$SCRIPT_DIR/render_credits.py"

ffmpeg -hide_banner -loglevel error -y \
  -loop 1 -t 22 -i "$SCRIPT_DIR/rodnoy-dom-cover.png" \
  -loop 1 -t 10 -i "$SCRIPT_DIR/rodnoy-dom-credits.png" \
  -ss 48 -t 30 -i "$AUDIO_SOURCE" \
  -filter_complex "[0:v]scale=1120:1120,crop=1080:1080,zoompan=z='min(zoom+0.00018,1.025)':d=660:s=1080x1080:fps=30,setsar=1[v0];[1:v]scale=1080:1080,fps=30,setsar=1[v1];[v0][v1]xfade=transition=fade:duration=2:offset=20,format=yuv420p[v];[2:a]afade=t=in:st=0:d=0.25,afade=t=out:st=29.2:d=0.8[a]" \
  -map "[v]" -map "[a]" -t 30 -r 30 \
  -c:v libx264 -preset medium -crf 18 -profile:v high -level 4.1 \
  -c:a aac -b:a 256k -movflags +faststart \
  "$SCRIPT_DIR/rodnoy-dom-teaser-30s.mp4"

echo "Built $SCRIPT_DIR/rodnoy-dom-teaser-30s.mp4"
