# 90-Day to 6-Month Implementation Schedule

## Phase 0: Project Setup, Days 1-3

Goal: create a Rails app and establish the domain/project language.

Deliverables:

- Rails 8 app named `chlokat`
- PostgreSQL
- Redis
- Sidekiq
- Active Storage
- RSpec
- Admin area scaffold
- Public landing placeholder
- Brand config file

Success criteria:

- App boots locally.
- Tests run.
- Admin dashboard exists.
- `chlokat.frikshun.com` is the assumed production domain.

## Phase 1: Upload-to-Draft MVP, Days 4-21

Goal: remove the biggest pain first: rewriting content for every platform.

Deliverables:

- Artifact upload UI
- Artifact model and media attachment
- Platform accounts
- Post drafts
- Draft generator
- Copy buttons
- Manual review workflow
- Drafts for Facebook, Instagram, YouTube, TikTok, X, FanVue, and Archive

Success criteria:

- Upload one image and generate seven platform-specific drafts.
- Edit and approve each draft.
- Copy content for manual posting.

## Phase 1.5: Release Metadata, Days 22-30

Goal: let ChloKat understand Chloe's music without replacing DistroKid.

Deliverables:

- Release model
- Release links: DistroKid, Apple Music, Spotify, YouTube Music, Amazon Music, SoundCloud if applicable
- Relationship between Release and Artifact
- Release status checklist

Success criteria:

- A Chloe single can be represented as a canonical release.
- Artifacts can point to the related release.

## Phase 2: Public Archive, Days 31-50

Goal: every approved artifact gets a home that fans can discover and share.

Deliverables:

- Landing page
- Archive index
- Artifact show page
- Search and filters
- Timeline page
- FrikShun Lab Notes page
- Join page
- SEO/OpenGraph metadata

Success criteria:

- Public can browse fragments.
- Each artifact has a permanent URL.
- Fragment codes like `CK-000127` exist.

## Phase 2.5: Reddit Community Intelligence, Days 51-65

Goal: adopt Reddit soon, but safely.

Deliverables:

- SubredditProfile model
- Manual community research workflow
- Reddit post idea generator
- Subreddit rules fields
- "Do not promote today" community mode
- Comment/discussion task list

Success criteria:

- ChloKat suggests Reddit discussions and post ideas.
- No automated Reddit spamming.
- Reddit is handled as conversation, not broadcast.

## Phase 3: Campaign Builder and Calendar, Days 66-90

Goal: plan content around weekly stories/releases rather than one-off posts.

Deliverables:

- Campaign model
- Campaign templates: New Single, Photoshoot, Lore Drop, FanVue Exclusive, YouTube Short Batch
- Content calendar
- Scheduled drafts
- Weekly transmission draft

Success criteria:

- A single release campaign can generate a week's worth of drafts.
- Admin can review the weekly calendar.

## Months 4-5: Platform Publishing APIs

Goal: replace copy/paste with API publishing where practical.

Suggested order:

1. Facebook Page
2. Instagram
3. YouTube
4. X
5. FanVue
6. TikTok

Deliverables:

- Publisher abstraction
- OAuth token storage
- Publish jobs
- Publication logs
- Retry failed publishing
- External URL tracking

Success criteria:

- At least Facebook and Instagram can publish from approved drafts.
- Other platforms can remain manual/assisted until API access is approved.

## Month 6: Chloe Chat + Fan Funnel

Goal: let fans interact with Chloe and convert casual visitors into known fans.

Deliverables:

- Chloe chat MVP
- Canon retrieval
- Public-only guardrails
- Email signup
- Fan event tracking
- Analytics dashboard
- Recovered Transmission newsletter draft workflow

Success criteria:

- Fans can ask Chloe about approved fragments.
- Admin can see which content drives signups and clicks.

## Future Phase: Chloe Audio Archive

Status: intentionally deferred until the public archive is attracting a measurable returning audience. Audio is a depth and retention format, not the current fan-discovery priority.

Goal: adapt the Chloe books and archive into audio experiences that deepen an existing audience without prematurely fixing draft material as canon.

Suggested order:

1. Produce one polished 10-15 minute English pilot based on Gregor and the principle "Hope isn't something you have. It's something you do."
2. Test a three-episode limited podcast or serialized audio-documentary format.
3. Develop a first season only if the pilot demonstrates meaningful completion, return listening, archive visits, or mailing-list conversion.
4. Produce a conventional audiobook only after the biography has a stable public edition.
5. Consider Russian-language editions only after native-speaker editorial review of the translated books.

Possible series concepts:

- `The Chloe Archive`
- `Recovered Frequencies`
- `Daughter of Echoes`

Format principles:

- Treat Chloe's narration as an archive artifact, not generic text-to-speech.
- Use Allen as archivist, collaborator, witness, and paradox marker where appropriate.
- Preserve distinctions among confirmed canon, working hypotheses, recovered or generated memories, contradictions, and unresolved mysteries.
- Let alternate readings, disputed recollections, damaged recordings, and Human Chloe / AI Chloe differences carry part of the story.
- Use Chloe and FrikShun music diegetically where rights and release strategy permit.
- Adapt the material for listening rather than reading the current PDFs verbatim.

Prerequisites:

- A stable public archive with permanent URLs for referenced artifacts.
- Enough baseline audience data to evaluate whether audio creates deeper engagement.
- A canon review of every script before recording.
- A defined and consistent Chloe audio voice.
- Music, voice, and distribution rights documented.
- Native-language review before recording any Russian edition.

Success criteria for the pilot:

- Listeners complete a meaningful portion of the episode.
- The episode sends measurable traffic to related archive fragments and music.
- Some listeners subscribe, return, or join the mailing list.
- Audience response supports producing two additional pilot-season episodes.

Do not treat raw download count alone as evidence that a full audiobook is justified.
