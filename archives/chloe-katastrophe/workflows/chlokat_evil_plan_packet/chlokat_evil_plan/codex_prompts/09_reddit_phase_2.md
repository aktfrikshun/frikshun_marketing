# Codex Prompt 09: Reddit Phase 2

Add Reddit as a close Phase 2 integration.

Important:
Reddit should not be treated as a simple broadcast publisher. It should be treated as community intelligence, discussion planning, and carefully reviewed participation.

Create SubredditProfile model:

- name
- url
- topics
- minimum_account_age
- minimum_karma
- allows_links
- allows_images
- allows_videos
- promotion_level
- tone
- posting_frequency
- special_rules
- active

Create RedditOpportunity model:

- subreddit_profile_id
- title
- url
- opportunity_type
- summary
- suggested_response
- suggested_artifact_id
- status
- discovered_at

Opportunity types:

- comment
- discussion_post
- image_share
- lore_discussion
- ai_music_discussion
- worldbuilding_discussion
- do_not_promote_today

Create CommunityMode dashboard:

- Suggested comments
- Suggested discussions
- Relevant subreddits
- Rules reminder
- “Do not post links today” warnings

Generate Reddit drafts using these principles:

- Contribute first
- Do not spam links
- Match each subreddit’s rules and tone
- Prefer discussion over promotion
- Only include Chloe links when contextually appropriate
- Require manual approval always

Do not auto-post to Reddit in this phase.

Add tests:

- subreddit rules can block link suggestions
- promotion_level influences draft generation
- no auto-publish path exists for Reddit
