# Codex Prompt 03: AI Content Generator Adapter

Create an `AIContentGenerator` service.

It should accept:

- artifact
- platform
- campaign, optional
- release, optional
- Chloe canon context
- FrikShun brand context
- desired tone

Return:

- caption
- hashtags
- call_to_action
- archive_summary
- lore_expansion
- suggested_title

For now, create a mock adapter and an interface that can later call OpenAI, Anthropic, or another LLM.

Add prompt templates for:

- Facebook
- Instagram
- YouTube Short
- YouTube Community Post
- YouTube Video Description
- TikTok
- X
- FanVue
- Archive
- Email Transmission

Create a config file:

`config/chlokat_brand.yml`

Include:

- Chloe Katastrophe is also called ChloKat
- FrikShun is the archivist/engineer helping reconstruct Chloe’s memories
- Domain is `chlokat.frikshun.com`
- Primary CTA is “Join the Reconstruction”
- Secondary CTA is “Talk to Chloe about this fragment”
- Music distribution is handled by DistroKid
- Avoid spammy influencer language
- Prefer lore, mystery, beauty, music, and recovered-memory framing
- Do not invent canon facts unless explicitly allowed

Add tests for each platform template.
