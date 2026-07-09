# Architecture Clarification: Public ChloKat vs FrikShun Creator OS

Date: 2026-07-09

## Decision

`chlokat.frikshun.com` should be the public ChloKat fan surface, not the private creator operating system.

The public site is a superfan search engine and living archive where fans can discover Chloe Katastrophe artifacts, latest Chloe news, releases, fragments, lore, links, and public transmissions in one place.

The content creator operating system is a FrikShun tool. It can run locally at first and should remain admin/private until there is a deliberate decision to make a creator-facing SaaS or hosted tool for other artists.

## Public ChloKat Site

Primary identity:

- ChloKat public archive
- Superfan search engine
- Latest Chloe news hub
- Public artifact database
- Music/release discovery surface
- Canon-safe exploration layer

Primary users:

- Chloe fans
- Curious listeners
- Superfans
- People following the reconstruction

Core public functions:

- Search artifacts, songs, lore fragments, images, videos, lyrics, and public transmissions
- Browse latest Chloe news and updates
- Browse public archive fragments
- Find streaming links and release metadata
- Follow calls to action such as Join the Reconstruction, Talk to Chloe, follow socials, or visit FanVue where appropriate

## FrikShun Creator OS

Primary identity:

- Internal FrikShun publishing and archive management tool
- Creator operations cockpit
- Artifact-to-platform draft generator
- Campaign and calendar system
- Future multi-creator product candidate

Primary users:

- Allen / FrikShun
- Approved collaborators
- Potential future creators if this becomes a hosted product

Core private functions:

- Upload artifacts
- Generate platform-specific drafts
- Review, edit, approve, copy, and eventually publish posts
- Manage releases and metadata
- Manage campaigns and calendars
- Track funnel analytics
- Control what is visible on the public ChloKat site

## Product Boundary

Do not expose admin publishing workflows as the main public ChloKat experience.

Do expose approved artifacts, news, release data, search, archive pages, and fan-safe Chloe interaction.

For now, build the creator OS locally as a FrikShun tool. Later, it may become a separate web product for creators who want to manage fictional artists, virtual artists, music releases, social drafts, and public archive worlds.

