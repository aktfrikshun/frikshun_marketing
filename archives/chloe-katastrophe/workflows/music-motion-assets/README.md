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
| YouTube cover edition | `*-youtube-cover-edition.mp4` | Full song | 1920x1080 | Yes | Complete YouTube music-video inventory |

The Canvas intentionally contains no title or artist text. Spotify already displays those elements, lower-screen controls obscure part of the image, and a clean image loop travels better across device crops.

The YouTube cover edition uses the complete released master. Its approved cover moves subtly until a track-specific transition begins approximately 30 seconds before the end; the final frame is a deterministic credits layout colored and textured to match that cover. The separate `youtube-tracks.psv` manifest includes every released primary master, including newer archive entries and the Living Archive release.

## Build

Requires `ffmpeg`.

```sh
# Backfill every released track in all three formats
./archives/chloe-katastrophe/workflows/music-motion-assets/build-motion-assets.sh --all --format pack

# Build one track or one delivery format
./archives/chloe-katastrophe/workflows/music-motion-assets/build-motion-assets.sh --track before-hello --format canvas

# Verify codecs, dimensions, durations, and audio-stream rules
./archives/chloe-katastrophe/workflows/music-motion-assets/validate-motion-assets.sh

# Build full-length 16:9 YouTube cover editions
./archives/chloe-katastrophe/workflows/music-motion-assets/build-youtube-cover-editions.sh --all
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

The current release inventory is the complete manifest in `youtube-tracks.psv`, including `Родной дом` as Daughter of Echoes Track 12. Unreleased draft artifacts remain excluded.

The first backfill pass animates approved covers. A later, manually reviewed pass may replace selected loops with music-video clips, image-studio scenes, or recovered-photo motion where the source material and canon classification support it.

## Platform Notes

Spotify currently accepts a 3–8 second vertical 9:16 MP4 or JPG with a height between 720 and 1080 pixels. It recommends avoiding intense flashing, rapid cuts, lyric synchronization, and redundant artist/title typography. Platform rules change; verify the official Canvas guidance before changing render specifications.
