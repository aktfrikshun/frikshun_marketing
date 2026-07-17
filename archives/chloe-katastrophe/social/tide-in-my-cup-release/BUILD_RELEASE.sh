#!/bin/zsh
set -euo pipefail

release_dir="${0:A:h}"
source_audio="/Users/allentaylor/Downloads/Tide in My Cup.wav"
python_runtime="/Users/allentaylor/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"

"$python_runtime" "$release_dir/render_assets.py"

ffmpeg -y -hide_banner -loglevel error \
  -ss 55 -t 30 -i "$source_audio" \
  -af "afade=t=in:st=0:d=0.35,afade=t=out:st=29.15:d=0.85" \
  -c:a pcm_s16le \
  "$release_dir/tide-in-my-cup-teaser-v2.wav"

ffmpeg -y -hide_banner -loglevel error \
  -loop 1 -i "$release_dir/tide-in-my-cup-cover-v2.png" \
  -i "$release_dir/tide-in-my-cup-teaser-v2.wav" \
  -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=35,eq=brightness=-0.18:saturation=0.78[bg];[0:v]scale=980:980[cover];[bg][cover]overlay=(W-w)/2:(H-h)/2,fade=t=in:st=0:d=0.35,fade=t=out:st=29.15:d=0.85,format=yuv420p[v]" \
  -map "[v]" -map 1:a -t 30 -r 30 \
  -c:v libx264 -preset medium -crf 19 -c:a aac -b:a 192k -movflags +faststart \
  "$release_dir/tide-in-my-cup-vertical-teaser-v2.mp4"

ffmpeg -y -hide_banner -loglevel error \
  -loop 1 -i "$release_dir/tide-in-my-cup-cover-v2.png" \
  -i "$release_dir/tide-in-my-cup-teaser-v2.wav" \
  -vf "scale=1080:1080,fade=t=in:st=0:d=0.35,fade=t=out:st=29.15:d=0.85,format=yuv420p" \
  -t 30 -r 30 -c:v libx264 -preset medium -crf 19 -c:a aac -b:a 192k -shortest -movflags +faststart \
  "$release_dir/tide-in-my-cup-square-teaser-v2.mp4"

for second in 2 15 28; do
  ffmpeg -y -hide_banner -loglevel error \
    -ss "$second" -i "$release_dir/tide-in-my-cup-vertical-teaser-v2.mp4" \
    -frames:v 1 "$release_dir/qa-frame-${second}s.png"
done

ffmpeg -y -hide_banner -loglevel error \
  -i "$release_dir/tide-in-my-cup-vertical-teaser-v2.mp4" \
  -vf "fps=1/6,scale=270:-1,tile=5x1" -frames:v 1 \
  "$release_dir/teaser-contact-sheet-v2.png"

echo "$release_dir"
