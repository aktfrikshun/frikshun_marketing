#!/bin/zsh
set -euo pipefail

release_dir="${0:A:h}"
archive_dir="${release_dir:h:h}"
source_audio="$archive_dir/site/assets/audio/tomorrow-we-met.wav"
cover_art="$archive_dir/site/assets/images/tomorrow-we-met-cover.png"
teaser_audio="$release_dir/tomorrow-we-met-teaser-001.wav"
teaser_video="$release_dir/tomorrow-we-met-teaser-cover-video-001.mp4"
python_runtime="/Users/allentaylor/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"

"$python_runtime" "$release_dir/RENDER_OVERLAYS.py"

ffmpeg -y -hide_banner -loglevel warning \
  -ss 147 -t 30 -i "$source_audio" \
  -af "afade=t=in:st=0:d=0.35,afade=t=out:st=29.15:d=0.85" \
  -c:a pcm_s16le -ar 48000 -ac 2 \
  "$teaser_audio"

ffmpeg -y -hide_banner -loglevel warning \
  -loop 1 -i "$cover_art" \
  -loop 1 -i "$cover_art" \
  -loop 1 -i "$release_dir/overlays/01-recovered-recording.png" \
  -loop 1 -i "$release_dir/overlays/02-question.png" \
  -loop 1 -i "$release_dir/overlays/03-feeling-first.png" \
  -loop 1 -i "$release_dir/overlays/04-comfort-warmth.png" \
  -loop 1 -i "$release_dir/overlays/05-out-now.png" \
  -i "$teaser_audio" \
  -filter_complex "\
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=42,eq=brightness=-0.30:saturation=0.72[bg];\
[1:v]scale=940:940,format=rgba[cover];\
[bg]drawbox=x=0:y=0:w=1080:h=355:color=0x08070a@0.56:t=fill,drawbox=x=0:y=1320:w=1080:h=600:color=0x08070a@0.62:t=fill,drawbox=x=64:y=364:w=952:h=952:color=0xe0b8a8@0.65:t=3[frame];\
[frame][cover]overlay=70:370[base];\
[2:v]format=rgba,fade=t=in:st=0:d=0.5:alpha=1,fade=t=out:st=4.5:d=0.5:alpha=1[o1];\
[3:v]format=rgba,fade=t=in:st=4.5:d=0.5:alpha=1,fade=t=out:st=10.5:d=0.5:alpha=1[o2];\
[4:v]format=rgba,fade=t=in:st=10.5:d=0.5:alpha=1,fade=t=out:st=16.5:d=0.5:alpha=1[o3];\
[5:v]format=rgba,fade=t=in:st=16.5:d=0.5:alpha=1,fade=t=out:st=23.5:d=0.5:alpha=1[o4];\
[6:v]format=rgba,fade=t=in:st=23.5:d=0.5:alpha=1,fade=t=out:st=29.5:d=0.5:alpha=1[o5];\
[base][o1]overlay=0:0:enable='between(t,0,5)'[v1];\
[v1][o2]overlay=0:0:enable='between(t,4.5,11)'[v2];\
[v2][o3]overlay=0:0:enable='between(t,10.5,17)'[v3];\
[v3][o4]overlay=0:0:enable='between(t,16.5,24)'[v4];\
[v4][o5]overlay=0:0:enable='between(t,23.5,30)',fade=t=in:st=0:d=0.35,fade=t=out:st=29.5:d=0.5[vout]" \
  -map "[vout]" -map 7:a \
  -t 30 -r 30 -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart \
  "$teaser_video"

printf '%s\n' "$teaser_audio" "$teaser_video"
