#!/bin/zsh
set -euo pipefail

release_dir="${0:A:h}"
archive_dir="${release_dir:h:h}"
source_audio="$archive_dir/site/assets/audio/miga.wav"
cover_art="$archive_dir/site/assets/images/miga-cover.png"
output_video="$release_dir/miga-cover-video-001.mp4"
audio_duration="$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$source_audio")"

ffmpeg -y -hide_banner -loglevel warning \
  -loop 1 -i "$cover_art" \
  -i "$source_audio" \
  -filter_complex "[0:v]scale=1080:1080:force_original_aspect_ratio=decrease,pad=1080:1080:(ow-iw)/2:(oh-ih)/2:black,format=yuv420p[v]" \
  -map "[v]" -map 1:a:0 \
  -t "$audio_duration" -r 30 \
  -c:v libx264 -preset medium -crf 20 -tune stillimage -pix_fmt yuv420p \
  -c:a aac -b:a 256k -ar 48000 -ac 2 \
  -movflags +faststart \
  "$output_video"

printf '%s\n' "$output_video"
