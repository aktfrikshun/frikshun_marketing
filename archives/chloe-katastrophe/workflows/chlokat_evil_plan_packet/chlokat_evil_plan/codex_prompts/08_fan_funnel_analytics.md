# Codex Prompt 08: Fan Funnel and Analytics

Add analytics and fan funnel tracking.

Create FanEvent model:

- event_name
- source
- platform
- artifact_id
- fan_id
- metadata jsonb
- session_id
- occurred_at

Track:

- artifact views
- outbound social clicks
- FanVue clicks
- SoundCloud clicks if applicable
- DistroKid/smart-link clicks
- Apple Music clicks
- Spotify clicks
- YouTube Music clicks
- chat starts
- email signups
- transmission opens
- post draft source campaign

Create redirect links:

- `/go/facebook`
- `/go/instagram`
- `/go/youtube`
- `/go/tiktok`
- `/go/x`
- `/go/fanvue`
- `/go/soundcloud`
- `/go/apple-music`
- `/go/spotify`
- `/go/youtube-music`

Admin dashboard:

- Top artifacts
- Top platforms
- Best converting posts
- Email signups
- FanVue clicks
- Chat engagement
- Suggested next content based on engagement

Add UTM parameters to generated post links.

Add tests for event tracking and redirect safety.
