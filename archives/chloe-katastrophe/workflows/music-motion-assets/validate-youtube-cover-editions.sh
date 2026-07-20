#!/bin/zsh
set -euo pipefail

workflow_dir="${0:A:h}"
archive_dir="${workflow_dir:h:h}"
audio_dir="$archive_dir/site/assets/audio"
output_dir="$archive_dir/releases/youtube-cover-editions"
manifest="$workflow_dir/youtube-tracks.psv"
python_bin="/Users/allentaylor/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
frames_dir="$(mktemp -d)"
trap 'rm -rf "$frames_dir"' EXIT

failures=0
checked=0
while IFS='|' read -r slug title collection track_label audio cover accent transition artist credit_role credit_name release_status; do
  [[ "$slug" == slug ]] && continue
  [[ "$release_status" != released && "$release_status" != inventory-exception ]] && continue
  (( checked += 1 ))
  video="$output_dir/${slug}-youtube-cover-edition.mp4"
  audio_path="$audio_dir/$audio"
  if [[ ! -f "$video" ]]; then
    print -u2 "MISSING $video"; (( failures += 1 )); continue
  fi
  video_duration="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$video")"
  audio_duration="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$audio_path")"
  delta="$(awk -v v="$video_duration" -v a="$audio_duration" 'BEGIN { d=v-a; if(d<0)d=-d; printf "%.4f", d }')"
  dimensions="$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$video")"
  video_codec="$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of csv=p=0 "$video")"
  audio_codec="$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 "$video")"
  audio_streams="$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$video" | wc -l | tr -d ' ')"
  if awk -v d="$delta" 'BEGIN { exit !(d > 0.10) }' || [[ "$dimensions" != 1920x1080 || "$video_codec" != h264 || "$audio_codec" != aac || "$audio_streams" != 1 ]]; then
    print -u2 "FAIL $slug duration_delta=$delta dimensions=$dimensions codecs=$video_codec/$audio_codec audio_streams=$audio_streams"
    (( failures += 1 ))
  else
    print "PASS $slug duration=${video_duration}s transition=$(awk -v d="$audio_duration" 'BEGIN {printf "%.3f", d-30}')s"
  fi
  credit_frame="$(awk -v d="$audio_duration" 'BEGIN { printf "%.3f", d-20 }')"
  ffmpeg -nostdin -y -hide_banner -loglevel error -ss "$credit_frame" -i "$video" -frames:v 1 "$frames_dir/${slug}-credits.jpg"
done < "$manifest"

[[ $checked -eq 15 ]] || { print -u2 "FAIL expected 15 inventory entries, checked $checked"; (( failures += 1 )); }
"$python_bin" "$workflow_dir/build-youtube-contact-sheet.py" --frames "$frames_dir" --out "$output_dir/youtube-cover-editions-credit-qa.jpg"
(( failures == 0 )) || exit 1
print "Validated $checked YouTube cover editions. Credit QA sheet written to $output_dir."
