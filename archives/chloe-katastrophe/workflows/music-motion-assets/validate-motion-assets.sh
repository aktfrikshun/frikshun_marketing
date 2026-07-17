#!/bin/zsh
set -euo pipefail

workflow_dir="${0:A:h}"
output_dir="$workflow_dir/output"
manifest="$workflow_dir/tracks.psv"
failures=0

check_file() {
  local file="$1" expected_width="$2" expected_height="$3" expected_duration="$4" expected_audio="$5"
  if [[ ! -f "$file" ]]; then
    print -u2 "MISSING $file"
    failures=$(( failures + 1 ))
    return
  fi

  local video codec width height duration audio_count
  video="$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height -of csv=p=0 "$file")"
  IFS=',' read -r codec width height <<< "$video"
  duration="$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$file")"
  audio_count="$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$file" | wc -l | tr -d ' ')"

  if [[ "$codec" != h264 || "$width" != "$expected_width" || "$height" != "$expected_height" || \
        "${duration%.*}" != "$expected_duration" || "$audio_count" != "$expected_audio" ]]; then
    print -u2 "INVALID $file codec=$codec frame=${width}x${height} duration=$duration audio_streams=$audio_count"
    failures=$(( failures + 1 ))
  else
    print "OK ${file#$workflow_dir/}"
  fi
}

while IFS='|' read -r slug title artifact audio cover teaser_start accent motion release_status; do
  [[ "$slug" == slug || "$release_status" != released ]] && continue
  dir="$output_dir/$slug"
  check_file "$dir/${slug}-spotify-canvas.mp4" 608 1080 8 0
  check_file "$dir/${slug}-vertical-teaser.mp4" 1080 1920 15 1
  check_file "$dir/${slug}-square-animation.mp4" 1080 1080 15 1
done < "$manifest"

(( failures == 0 )) || { print -u2 "$failures validation failure(s)"; exit 1; }
print "All motion assets passed validation."
