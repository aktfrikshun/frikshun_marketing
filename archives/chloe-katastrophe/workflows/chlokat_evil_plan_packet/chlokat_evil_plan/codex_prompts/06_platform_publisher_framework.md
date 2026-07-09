# Codex Prompt 06: Platform Publisher Framework

Implement platform publishing architecture.

Create:

- `PlatformPublishers::BasePublisher`
- `PlatformPublishers::FacebookPublisher`
- `PlatformPublishers::InstagramPublisher`
- `PlatformPublishers::YouTubePublisher`
- `PlatformPublishers::TikTokPublisher`
- `PlatformPublishers::XPublisher`
- `PlatformPublishers::FanvuePublisher`

Each publisher exposes:

- `validate(post_draft)`
- `prepare(post_draft)`
- `publish(post_draft)`

Return object:

- success?
- external_post_id
- external_url
- error_message
- raw_response

For now:

- mock all API calls
- create PostPublication records
- support statuses: draft, approved, queued, publishing, published, failed
- run publishing through Sidekiq job `PublishPostDraftJob`
- make publishing idempotent
- log every attempt

Admin UI:

- Approve draft
- Queue draft
- Publish now
- Retry failed publish
- Copy manual posting text
- Mark manually published

Important:

Music platforms distributed by DistroKid should not be publisher adapters in this app. Store links only.
