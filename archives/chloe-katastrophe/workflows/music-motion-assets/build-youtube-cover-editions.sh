#!/bin/zsh
set -euo pipefail

workflow_dir="${0:A:h}"
archive_dir="${workflow_dir:h:h}"
audio_dir="$archive_dir/site/assets/audio"
image_dir="$archive_dir/site/assets/images"
output_dir="$archive_dir/releases/youtube-cover-editions"
manifest="$workflow_dir/youtube-tracks.psv"
font_regular="/System/Library/Fonts/Supplemental/Arial.ttf"
font_bold="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
python_bin="/Users/allentaylor/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
credits_renderer="$workflow_dir/render-youtube-credits.py"

selected="all"
force=0
while (( $# )); do
  case "$1" in
    --track) selected="$2"; shift 2 ;;
    --all) selected="all"; shift ;;
    --force) force=1; shift ;;
    -h|--help)
      print "Usage: ${0:t} [--all | --track SLUG] [--force]"
      exit 0 ;;
    *) print -u2 "Unknown argument: $1"; exit 2 ;;
  esac
done

for command_name in ffmpeg ffprobe; do
  command -v "$command_name" >/dev/null || { print -u2 "$command_name is required"; exit 1; }
done
[[ -f "$font_regular" && -f "$font_bold" ]] || { print -u2 "Required system fonts are missing"; exit 1; }
[[ -x "$python_bin" && -f "$credits_renderer" ]] || { print -u2 "Credits rendering runtime is missing"; exit 1; }
mkdir -p "$output_dir"

render_track() {
  local slug="$1" title="$2" collection="$3" track_label="$4" audio="$5" cover="$6"
  local accent="$7" transition="$8" artist="$9" credit_role="${10}" credit_name="${11}"
  local audio_path="$audio_dir/$audio" cover_path="$image_dir/$cover" output="$output_dir/${slug}-youtube-cover-edition.mp4"
  [[ -f "$audio_path" ]] || { print -u2 "Missing audio: $audio_path"; return 1; }
  [[ -f "$cover_path" ]] || { print -u2 "Missing cover: $cover_path"; return 1; }
  if [[ -f "$output" && $force -eq 0 ]]; then
    print "Skipping existing: ${output:t}"
    return
  fi

  local duration credit_start xfade_duration=2.5 fps=24 temp_dir
  duration="$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$audio_path")"
  credit_start="$(awk -v d="$duration" 'BEGIN { printf "%.3f", d - 30.0 }')"
  temp_dir="$(mktemp -d)"
  "$python_bin" "$credits_renderer" --cover "$cover_path" --main-out "$temp_dir/main.jpg" --out "$temp_dir/credits.jpg" \
    --accent "$accent" --collection "$collection" --track-label "$track_label" \
    --title "$title" --artist "$artist" --credit-role "$credit_role" --credit-name "$credit_name"

  print "Rendering ${title} — credits at ${credit_start}s of ${duration}s (${transition})"
  ffmpeg -nostdin -y -hide_banner -loglevel error \
    -loop 1 -framerate "$fps" -i "$temp_dir/main.jpg" -loop 1 -framerate "$fps" -i "$temp_dir/credits.jpg" -i "$audio_path" \
    -filter_complex "
      [0:v]zoompan=z='1.015+0.012*sin(2*PI*on/1800)':x='iw/2-(iw/zoom/2)+3*sin(2*PI*on/1100)':y='ih/2-(ih/zoom/2)+3*cos(2*PI*on/1300)':d=1:s=1920x1080:fps=${fps},format=yuv420p[main];
      [1:v]scale=1920:1080,format=yuv420p[credits];
      [main][credits]xfade=transition=${transition}:duration=${xfade_duration}:offset=${credit_start},format=yuv420p[outv]
    " \
    -map "[outv]" -map 2:a:0 -t "$duration" -r "$fps" \
    -c:v libx264 -preset veryfast -crf 20 -profile:v high -level 4.1 \
    -c:a aac -b:a 256k -ar 48000 -ac 2 -movflags +faststart "$output"
  rm -rf "$temp_dir"
}

matched=0
while IFS='|' read -r slug title collection track_label audio cover accent transition artist credit_role credit_name release_status; do
  [[ "$slug" == slug ]] && continue
  [[ "$release_status" != released && "$release_status" != inventory-exception ]] && continue
  [[ "$selected" != all && "$selected" != "$slug" ]] && continue
  matched=1
  render_track "$slug" "$title" "$collection" "$track_label" "$audio" "$cover" "$accent" "$transition" "$artist" "$credit_role" "$credit_name"
done < "$manifest"

(( matched )) || { print -u2 "No released track matched: $selected"; exit 1; }
print "YouTube cover editions ready in $output_dir"
