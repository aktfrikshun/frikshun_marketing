#!/bin/zsh
set -euo pipefail

teaser_dir="${0:A:h}"
archive_dir="${teaser_dir:h:h:h}"
source_audio="$archive_dir/site/assets/audio/touch-me-like-im-real.wav"
cover_art="$archive_dir/site/assets/images/touch-me-like-im-real-cover.png"
output_video="$teaser_dir/touch-me-like-im-real-tiktok-teaser-002.mp4"

ffmpeg -y -hide_banner -loglevel warning \
  -loop 1 -i "$cover_art" \
  -loop 1 -i "$cover_art" \
  -ss 160 -t 30 -i "$source_audio" \
  -filter_complex "\
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=42,eq=brightness=-0.30:saturation=0.72[bg];\
[1:v]scale=940:940[cover];\
[bg]drawbox=x=64:y=484:w=952:h=952:color=0xd7aaa0@0.62:t=3[frame];\
[frame][cover]overlay=70:490,fade=t=in:st=0:d=0.35,fade=t=out:st=29.35:d=0.65[vout];\
[2:a]afade=t=in:st=0:d=0.25,afade=t=out:st=29.2:d=0.8[aout]" \
  -map "[vout]" -map "[aout]" \
  -t 30 -r 24 \
  -c:v libx264 -preset slow -crf 24 -maxrate 1800k -bufsize 3600k -pix_fmt yuv420p \
  -c:a aac -b:a 128k -ar 48000 -ac 2 \
  -movflags +faststart \
  "$output_video"

size_bytes=$(stat -f %z "$output_video")
limit_bytes=10000000

if (( size_bytes >= limit_bytes )); then
  print -u2 "Teaser exceeds the 10 MB decimal limit: $size_bytes bytes"
  exit 1
fi

printf '%s\n%s bytes\n' "$output_video" "$size_bytes"
