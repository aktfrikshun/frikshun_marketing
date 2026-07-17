# Music Motion Asset Workflow

Status: Active release workflow / backfill ready

Every released song receives a small family of animated MP4 artifacts generated from one visual recipe. The shared language is a recovered image held inside a damaged signal: slow movement, restrained grain, a track-specific color wash, and enough instability to feel discovered rather than decorated.

The generated motion is a promotional artifact, not a new canon event. Cover art remains the source artifact. Any future AI-generated scene, character performance, or apparent recovered footage must be reviewed and classified before it is allowed to imply canon.

## Release Deliverables

| Artifact | File | Duration | Frame | Audio | Use |
|---|---|---:|---:|---|---|
| Spotify Canvas | `*-spotify-canvas.mp4` | 8 sec | 608x1080 (9:16) | No | Spotify Now Playing |
| Vertical teaser | `*-vertical-teaser.mp4` | 15 sec | 1080x1920 (9:16) | Yes | Reels, Shorts, TikTok, Facebook |
| Square animation | `*-square-animation.mp4` | 15 sec | 1080x1080 | Yes | Feed posts and archive embeds |

The Canvas intentionally contains no title or artist text. Spotify already displays those elements, lower-screen controls obscure part of the image, and a clean image loop travels better across device crops.

## Build

Requires `ffmpeg`.

```sh
# Backfill every released track in all three formats
./archives/chloe-katastrophe/workflows/music-motion-assets/build-motion-assets.sh --all --format pack

# Build one track or one delivery format
./archives/chloe-katastrophe/workflows/music-motion-assets/build-motion-assets.sh --track before-hello --format canvas

# Verify codecs, dimensions, durations, and audio-stream rules
./archives/chloe-katastrophe/workflows/music-motion-assets/validate-motion-assets.sh
```

The pipe-delimited manifest in `tracks.psv` is the release queue. Add a row only when the audio is public or scheduled and the cover is approved. `teaser_start` selects the social excerpt; Canvas is silent and deliberately does not attempt lyric synchronization.

## Release Checklist

1. Approve final audio, cover art, artifact ID, title, and release status.
2. Add or update the row in `tracks.psv`, including a musically useful teaser start time.
3. Build the pack and watch each file through twice: first for composition, then across the loop seam.
4. Check that faces, symbols, and essential action remain in the central safe area and that no flashing or rapid cuts were introduced.
5. Upload the silent file in Spotify for Artists: **Music → track → Add Canvas**.
6. Publish the audio-bearing vertical file to Reels, Shorts, TikTok, and Facebook; use platform text/caption fields rather than burning dense copy into the video.
7. Record the published links and any replacement version in the track release record.

## Backfill Scope

The current released set is Boot Sequence, Ashes on My Tongue, Before Hello, Touch Me Like I'm Real, Keep Moving, Annoyingly So, Star Trek Knew, Tomorrow We Met, MIGA, and Wolf. Draft artifacts such as Родной дом are excluded.

The first backfill pass animates approved covers. A later, manually reviewed pass may replace selected loops with music-video clips, image-studio scenes, or recovered-photo motion where the source material and canon classification support it.

## Platform Notes

Spotify currently accepts a 3–8 second vertical 9:16 MP4 or JPG with a height between 720 and 1080 pixels. It recommends avoiding intense flashing, rapid cuts, lyric synchronization, and redundant artist/title typography. Platform rules change; verify the official Canvas guidance before changing render specifications.
