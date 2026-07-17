#!/bin/zsh
set -euo pipefail

workflow_dir="${0:A:h}"
archive_dir="${workflow_dir:h:h}"
audio_dir="$archive_dir/site/assets/audio"
image_dir="$archive_dir/site/assets/images"
output_dir="$workflow_dir/output"
manifest="$workflow_dir/tracks.psv"

usage() {
  cat <<'EOF'
Usage: build-motion-assets.sh [--track SLUG | --all] [--format canvas|vertical|square|pack]

Defaults to --all --format pack. Outputs are written under output/<track>/.
Spotify Canvas is silent, 8 seconds, 9:16, and 608x1080.
Social exports are 15 seconds with music: 1080x1920 vertical and 1080x1080 square.
EOF
}

selected="all"
format="pack"
while (( $# )); do
  case "$1" in
    --track) selected="$2"; shift 2 ;;
    --all) selected="all"; shift ;;
    --format) format="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) print -u2 "Unknown argument: $1"; usage >&2; exit 2 ;;
  esac
done

if [[ "$format" != canvas && "$format" != vertical && "$format" != square && "$format" != pack ]]; then
  print -u2 "Unknown format: $format"
  exit 2
fi

command -v ffmpeg >/dev/null || { print -u2 "ffmpeg is required"; exit 1; }
mkdir -p "$output_dir"

render_visual() {
  local cover="$1" width="$2" height="$3" seconds="$4" fps="$5" accent="$6" motion="$7" output="$8"
  local frames=$(( seconds * fps ))

  ffmpeg -nostdin -y -hide_banner -loglevel warning -loop 1 -framerate "$fps" -i "$cover" \
    -filter_complex "[0:v]split=2[bg0][card0];\
[bg0]scale=1500:1500,zoompan=z='1.50+${motion}*sin(2*PI*on/${frames})':x='iw/2-(iw/zoom/2)+8*sin(2*PI*on/${frames})':y='ih/2-(ih/zoom/2)+8*cos(2*PI*on/${frames})':d=${frames}:s=${width}x${height}:fps=${fps},gblur=sigma=28,eq=brightness=-0.30:saturation=0.78[bg];\
[card0]scale='min(${width}*0.86,iw)':'min(${width}*0.86,ih)':force_original_aspect_ratio=decrease,format=rgba[card];\
[bg]drawbox=x=0:y=0:w=iw:h=ih:color=0x${accent}@0.10:t=fill,vignette=PI/5[wash];\
[wash][card]overlay=x='(W-w)/2+5*sin(2*PI*t/${seconds})':y='(H-h)/2+7*cos(2*PI*t/${seconds})',noise=alls=3:allf=t+u,format=yuv420p[out]" \
    -map "[out]" -t "$seconds" -an -r "$fps" -c:v libx264 -preset medium -crf 19 \
    -pix_fmt yuv420p -movflags +faststart "$output"
}

render_canvas() {
  local slug="$1" cover="$2" accent="$3" motion="$4" dir="$5"
  render_visual "$cover" 608 1080 8 30 "$accent" "$motion" "$dir/${slug}-spotify-canvas.mp4"
}

render_social() {
  local slug="$1" audio="$2" cover="$3" start="$4" accent="$5" motion="$6" dir="$7" shape="$8"
  local width=1080 height=1920 suffix="vertical-teaser"
  [[ "$shape" == square ]] && { height=1080; suffix="square-animation"; }
  local silent="$dir/.${slug}-${shape}-silent.mp4"
  render_visual "$cover" "$width" "$height" 15 30 "$accent" "$motion" "$silent"
  ffmpeg -nostdin -y -hide_banner -loglevel warning -i "$silent" -ss "$start" -t 15 -i "$audio" \
    -map 0:v:0 -map 1:a:0 -c:v copy \
    -af "afade=t=in:st=0:d=0.25,afade=t=out:st=14.25:d=0.75" \
    -c:a aac -b:a 192k -ar 48000 -ac 2 -shortest -movflags +faststart \
    "$dir/${slug}-${suffix}.mp4"
  rm "$silent"
}

matched=0
while IFS='|' read -r slug title artifact audio cover teaser_start accent motion release_status; do
  [[ "$slug" == slug ]] && continue
  [[ "$selected" != all && "$selected" != "$slug" ]] && continue
  matched=1
  track_dir="$output_dir/$slug"
  mkdir -p "$track_dir"
  audio_path="$audio_dir/$audio"
  cover_path="$image_dir/$cover"
  [[ -f "$audio_path" ]] || { print -u2 "Missing audio: $audio_path"; exit 1; }
  [[ -f "$cover_path" ]] || { print -u2 "Missing cover: $cover_path"; exit 1; }
  print "Rendering $title ($artifact)"
  [[ "$format" == canvas || "$format" == pack ]] && render_canvas "$slug" "$cover_path" "$accent" "$motion" "$track_dir"
  [[ "$format" == vertical || "$format" == pack ]] && render_social "$slug" "$audio_path" "$cover_path" "$teaser_start" "$accent" "$motion" "$track_dir" vertical
  [[ "$format" == square || "$format" == pack ]] && render_social "$slug" "$audio_path" "$cover_path" "$teaser_start" "$accent" "$motion" "$track_dir" square
done < "$manifest"

(( matched )) || { print -u2 "No released track matched: $selected"; exit 1; }
print "Motion assets ready in $output_dir"
