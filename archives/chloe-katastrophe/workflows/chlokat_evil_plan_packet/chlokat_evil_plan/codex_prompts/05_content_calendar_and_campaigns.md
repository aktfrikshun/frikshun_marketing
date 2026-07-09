# Codex Prompt 05: Content Calendar and Campaigns

Add campaign and content calendar functionality.

Goal:
Instead of creating one-off posts, organize content around weekly stories, releases, photoshoots, and lore drops.

Create Campaign model fields:

- title
- slug
- campaign_type
- status
- start_date
- end_date
- primary_release_id
- theme
- goals
- notes

Campaign types:

- new_single
- photoshoot
- lore_drop
- fanvue_exclusive
- youtube_short_batch
- general_weekly_content

Create CampaignTemplate service.

Templates:

## New Single

Generate:

- DistroKid checklist item
- Facebook announcement
- Instagram post/carousel draft
- YouTube Short draft
- YouTube Community Post draft
- TikTok draft
- X teaser
- FanVue exclusive draft
- Archive page draft
- Release-day post
- One-week follow-up post
- Recovered Transmission email draft

## Photoshoot

Generate:

- Instagram post
- Facebook gallery post
- X teaser
- FanVue gallery post
- Archive entry
- FrikShun lab note
- Chloe commentary prompt

## Lore Drop

Generate:

- Archive article
- Facebook discussion
- X thread
- Instagram quote-card copy
- YouTube narration script
- FanVue expanded version

Add calendar UI:

- monthly view
- weekly view
- platform filters
- draft status colors
- quick approve/reschedule actions

Add tests for campaign template generation.
