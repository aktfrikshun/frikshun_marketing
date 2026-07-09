# Codex Prompt 10: YouTube and X Specific Enhancements

Add platform-specific support for YouTube and X.

## YouTube

Support draft types:

- YouTube Short
- YouTube Community Post
- YouTube Video Description
- YouTube Music/Lyric Video Description

Fields on PostDraft or related metadata:

- youtube_content_type
- video_title
- video_description
- thumbnail_suggestion
- chapters
- tags

Rules:

- YouTube Shorts should have tight captions and search-friendly titles.
- Community posts can be more conversational and visual.
- Video descriptions should include release links, archive links, and FanVue/subscribe CTA.

## X

Support draft types:

- single_post
- thread
- reply_prompt
- release_teaser

Rules:

- Keep single posts concise.
- Use no more than 1-3 hashtags.
- Generate optional thread versions for lore drops.
- Include strong standalone hooks.
- Avoid overusing links.

Add admin UI to choose:

- YouTube Short vs Community Post vs Video Description
- X single post vs thread

Add tests for platform-specific formatting.
