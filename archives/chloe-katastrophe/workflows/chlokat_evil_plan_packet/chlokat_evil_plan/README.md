# ChloKat / FrikShun Evil Plan

Public domain: `chlokat.frikshun.com`

ChloKat is Chloe Katastrophe's nickname. FrikShun is the archivist, engineer, producer, and creator building the recovery system around Chloe.

This package contains the implementation plan, build schedule, architecture notes, and Codex prompts for creating the ChloKat content engine.

## Product Split

`chlokat.frikshun.com` should be the public fan-facing ChloKat archive: a superfan search engine, latest Chloe news hub, public artifact database, release guide, and canon-safe exploration surface.

The content creator operating system should be a FrikShun tool. It can run locally for now, with the option to become a hosted creator product later for other artists and fictional/virtual artist projects.

## Primary Goal

Reduce creative friction:

> Upload one image, video, audio preview, lyric, or lore artifact and generate polished platform-specific drafts for Facebook, Instagram, YouTube, TikTok, X, FanVue, and the ChloKat archive.

Music distribution to Apple Music, Spotify, YouTube Music, Amazon Music, and similar platforms remains managed by DistroKid. ChloKat stores release metadata and streaming links, but does not replace DistroKid.

See `docs/architecture_clarification_2026-07-09.md` for the updated boundary between the public ChloKat site and the private FrikShun creator OS.

## Recommended Codex Order

1. `codex_prompts/01_create_chlokat_rails_app.md`
2. `codex_prompts/02_artifact_to_post_draft_generator.md`
3. `codex_prompts/03_ai_content_generator_adapter.md`
4. `codex_prompts/04_public_archive.md`
5. `codex_prompts/05_content_calendar_and_campaigns.md`
6. `codex_prompts/06_platform_publisher_framework.md`
7. `codex_prompts/07_chloe_chat_mvp.md`
8. `codex_prompts/08_fan_funnel_analytics.md`
9. `codex_prompts/09_reddit_phase_2.md`
10. `codex_prompts/10_youtube_x_specifics.md`

## First Milestone

The first useful version should do this:

Upload one Chloe image → generate Facebook, Instagram, YouTube, TikTok, X, FanVue, and Archive drafts → give copy buttons for each → create public archive page.

Manual review first. API posting later.
