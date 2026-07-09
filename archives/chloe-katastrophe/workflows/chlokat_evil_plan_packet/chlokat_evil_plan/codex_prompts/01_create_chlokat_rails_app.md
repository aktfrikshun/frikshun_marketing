# Codex Prompt 01: Create ChloKat Rails App

Build a Rails 8 app named `chlokat`.

Purpose:
A creator operating system for FrikShun and Chloe Katastrophe, hosted at `chlokat.frikshun.com`.

Primary goal:
Allow Allen “FrikShun” Taylor to upload one image, video, audio preview, lyric, or lore artifact and generate platform-specific post drafts for Facebook, Instagram, YouTube, TikTok, X, FanVue, and the public ChloKat archive.

Use:

- Rails 8
- PostgreSQL
- Active Storage
- Sidekiq
- Redis
- RSpec
- Hotwire/Turbo
- Tailwind if available, otherwise simple Rails views

Create models:

- Artifact
- Release
- PlatformAccount
- PostDraft
- PostPublication
- Campaign
- CanonEntry
- Fan
- FanEvent
- Transmission
- ChloeChatConversation
- ChloeChatMessage

Artifact fields:

- title
- slug
- artifact_type
- summary
- lore_text
- visibility
- recovered_at
- fragment_code
- canonical_status
- mood_tags
- content_tags
- platform_tags
- source_notes
- usable_in_chat
- release_id

Release fields:

- title
- slug
- release_type
- release_date
- distro_status
- distro_url
- apple_music_url
- spotify_url
- youtube_music_url
- amazon_music_url
- soundcloud_url
- isrc
- upc
- lyrics
- genre
- mood_tags

PlatformAccount fields:

- platform
- handle
- profile_url
- oauth_status
- active

PostDraft fields:

- artifact_id
- campaign_id
- platform_account_id
- platform
- caption
- hashtags
- call_to_action
- status
- scheduled_at
- approved_at

Create:

- Admin dashboard
- Artifact upload/edit UI
- Release CRUD
- Post draft review UI
- Public artifact index
- Public artifact show page
- Basic landing page for `chlokat.frikshun.com`

Do not implement real external API posting yet.
Create placeholder publisher services.
Add RSpec tests.
