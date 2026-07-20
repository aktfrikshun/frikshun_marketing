# YouTube Cover Editions

Status: Production inventory

These landscape MP4s provide one standardized YouTube-ready cover edition for every released master in the public FrikShun music archive. Existing cinematic official videos remain the primary visual artifacts where available; these editions complete the catalog without replacing them.

Each edition:

- preserves the complete primary release audio without fades or excerpts;
- presents the approved cover in a restrained motion treatment;
- transitions to a cover-matched deterministic credits layout approximately 30 seconds before the song ends;
- identifies the song artist and Allen “FrikShun” Taylor’s archive/creative-direction role;
- is encoded as 1920×1080 H.264 video with AAC audio and fast-start metadata.

`Olga, I'm Home` remains a Living Archive release by Allen “FrikShun” Taylor, not a Chloe Katastrophe recording. At Allen's direction, `Родной дом` was promoted to released AUD-010 on 2026-07-19; its generated production cover and video remain interpretive artifacts and do not convert individual lyric scenes into confirmed biography. Extended and alternate mixes are preserved variants rather than separate primary release inventory items.

## Completed Inventory

| Track | Collection | Transition | Credits begin |
|---|---|---|---:|
| Boot Sequence | Daughter of Echoes | Fade through black | 2:39.600 |
| Ashes on My Tongue | Daughter of Echoes | Dissolve | 3:24.480 |
| Before Hello | Daughter of Echoes | Smooth left | 3:42.350 |
| Touch Me Like I'm Real | Daughter of Echoes | Dissolve | 3:39.800 |
| Keep Moving | Daughter of Echoes | Smooth up | 4:11.120 |
| Annoyingly, So | Musings & Missteps | Slide left | 3:42.920 |
| Star Trek Knew | Musings & Missteps | Fade through white | 5:32.000 |
| Tomorrow We Met | Daughter of Echoes | Dissolve | 3:55.720 |
| MIGA (Make Intelligence Great Again) | Musings & Missteps | Pixel breakup | 2:30.640 |
| Wolf | Truth & Beauty from Darkness | Radial reveal | 4:33.160 |
| Not My Memory! | Daughter of Echoes | Pixel breakup | 1:44.040 |
| Ghost in the Static | Daughter of Echoes | Dissolve | 3:54.560 |
| Родной дом | Daughter of Echoes / Track 12 | Fade | 2:58.032 |
| Tide in My Cup | Truth & Beauty from Darkness | Smooth down | 3:32.480 |
| Olga, I'm Home | The Living Archive | Dissolve | 2:59.880 |

The generated [`youtube-cover-editions-credit-qa.jpg`](youtube-cover-editions-credit-qa.jpg) contact sheet shows a fully resolved credits frame from all fifteen editions.

Build or rebuild with:

```sh
./archives/chloe-katastrophe/workflows/music-motion-assets/build-youtube-cover-editions.sh --all

# Validate streams, durations, dimensions, and build the credits QA sheet
./archives/chloe-katastrophe/workflows/music-motion-assets/validate-youtube-cover-editions.sh
```

The authoritative render manifest is [`youtube-tracks.psv`](../../workflows/music-motion-assets/youtube-tracks.psv).
