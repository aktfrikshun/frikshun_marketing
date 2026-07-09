# Core Architecture

## Product Boundary

There are two connected products:

1. Public ChloKat site at `chlokat.frikshun.com`
2. Private FrikShun creator OS, local-first for now

The public site should be a superfan search engine, latest Chloe news hub, and searchable public artifact archive.

The creator OS should be an internal FrikShun tool for uploads, draft generation, campaign planning, publishing assistance, and analytics. It may later become a hosted web product for other creators.

## Public Domain

`chlokat.frikshun.com`

## Internal Tool Name

`frikshun_creator_os` or `chlokat_admin` are both acceptable working names. Avoid making the public ChloKat site feel like an admin dashboard.

## Stack

- Rails 8
- PostgreSQL
- Active Storage
- Redis
- Sidekiq
- RSpec
- Hotwire/Turbo
- Tailwind or simple Rails views
- pgvector later for semantic archive search

## Core Models

### Artifact

Stores uploaded creative material. Approved public artifacts power the ChloKat search/archive experience; private artifacts remain internal to the FrikShun creator OS.

Fields:

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

### Release

Stores official music release metadata. DistroKid remains the distribution system.

Fields:

- title
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

### PlatformAccount

Stores social platform identity and publishing state.

Platforms:

- facebook
- instagram
- youtube
- tiktok
- x
- fanvue
- reddit later
- soundcloud optional

### PostDraft

A platform-specific draft generated from an artifact or campaign.

### PostPublication

An attempted or successful publication event.

### Campaign

A themed release/content push.

Examples:

- New Single
- Photoshoot
- Lore Drop
- FanVue Exclusive
- YouTube Short Batch

### CanonEntry

Approved lore, character information, timeline events, and world details.

### ChloeChatConversation / ChloeChatMessage

Stores fan chat interactions.

### Fan / FanEvent

Stores fan identity and behavioral analytics.

## Publishing Philosophy

The app should use a generic Publisher interface rather than hardcoding platform logic throughout the app.

Each publisher should support:

- validate
- prepare
- publish
- update
- delete when supported
- external URL capture
- error logging

## First Version Boundary

Do not implement external API publishing in the first version.

Start with:

- draft generation
- approval
- copy buttons
- archive pages

Then add API connectors one by one.
