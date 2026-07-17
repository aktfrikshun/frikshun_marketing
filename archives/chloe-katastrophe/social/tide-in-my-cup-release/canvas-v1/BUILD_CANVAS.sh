#!/bin/zsh
set -euo pipefail

dir="${0:A:h}"
out="$dir/tide-in-my-cup-spotify-canvas-v1.mp4"

# Six 1.6-second movements with 0.32-second dissolves produce an exact
# eight-second loop. The final image repeats the opening composition with
# reverse motion so the last frame returns to the first crop.
ffmpeg -nostdin -y -hide_banner -loglevel warning \
  -loop 1 -framerate 30 -t 1.6 -i "$dir/canvas-02-rock.jpeg" \
  -loop 1 -framerate 30 -t 1.6 -i "$dir/canvas-05-water.jpeg" \
  -loop 1 -framerate 30 -t 1.6 -i "$dir/canvas-04-walking.jpeg" \
  -loop 1 -framerate 30 -t 1.6 -i "$dir/canvas-03-palm.jpeg" \
  -loop 1 -framerate 30 -t 1.6 -i "$dir/canvas-01-sandcastle.jpeg" \
  -loop 1 -framerate 30 -t 1.6 -i "$dir/canvas-02-rock.jpeg" \
  -filter_complex "\
[0:v]scale=608:1080:force_original_aspect_ratio=increase,crop=608:1080,zoompan=z='1+0.015*on/47':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=48:s=608x1080:fps=30,setsar=1[v0];\
[1:v]scale=608:1080:force_original_aspect_ratio=increase,crop=608:1080,zoompan=z='1.015-0.012*on/47':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=48:s=608x1080:fps=30,setsar=1[v1];\
[2:v]scale=608:1080:force_original_aspect_ratio=increase,crop=608:1080,zoompan=z='1+0.014*on/47':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=48:s=608x1080:fps=30,setsar=1[v2];\
[3:v]scale=608:1080:force_original_aspect_ratio=increase,crop=608:1080,zoompan=z='1.012-0.009*on/47':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=48:s=608x1080:fps=30,setsar=1[v3];\
[4:v]scale=608:1080:force_original_aspect_ratio=increase,crop=608:1080,zoompan=z='1+0.012*on/47':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=48:s=608x1080:fps=30,setsar=1[v4];\
[5:v]scale=608:1080:force_original_aspect_ratio=increase,crop=608:1080,zoompan=z='1.015-0.015*on/47':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=48:s=608x1080:fps=30,setsar=1[v5];\
[v0][v1]xfade=transition=fade:duration=0.32:offset=1.28[x1];\
[x1][v2]xfade=transition=fade:duration=0.32:offset=2.56[x2];\
[x2][v3]xfade=transition=fade:duration=0.32:offset=3.84[x3];\
[x3][v4]xfade=transition=fade:duration=0.32:offset=5.12[x4];\
[x4][v5]xfade=transition=fade:duration=0.32:offset=6.40,eq=saturation=0.96:contrast=1.02,noise=alls=1.5:allf=t+u,scale=in_range=pc:out_range=tv,format=yuv420p[out]" \
  -map "[out]" -t 8 -an -r 30 -c:v libx264 -preset medium -crf 18 \
  -pix_fmt yuv420p -movflags +faststart "$out"

for second in 0 2 4 6 7.9; do
  label="${second//./_}"
  ffmpeg -nostdin -y -hide_banner -loglevel error -ss "$second" -i "$out" \
    -frames:v 1 "$dir/canvas-qa-${label}s.png"
done

ffmpeg -nostdin -y -hide_banner -loglevel error -i "$out" \
  -vf "fps=1,scale=304:-1,tile=8x1" -frames:v 1 "$dir/canvas-contact-sheet-v1.png"

print "$out"
