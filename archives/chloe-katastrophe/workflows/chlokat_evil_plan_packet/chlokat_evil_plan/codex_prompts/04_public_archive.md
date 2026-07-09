# Codex Prompt 04: Public ChloKat Archive

Build the public ChloKat archive.

Routes:

- `/`
- `/archive`
- `/archive/:slug`
- `/songs`
- `/songs/:slug`
- `/timeline`
- `/frikshun-lab`
- `/join`
- `/chat`

Public pages:

- Landing page
- Archive index with search and filters
- Artifact detail page
- Songs/releases page
- Release detail page
- Timeline page
- FrikShun Lab Notes page
- Email signup page

Artifact page should show:

- Fragment code, e.g. `CK-000127`
- Title
- Recovered date
- Media
- Summary
- Lore text
- Related song/release if any
- Tags
- CTA: Talk to Chloe about this fragment
- CTA: Join the Reconstruction
- CTA: Follow Chloe

Release page should show:

- Title
- Release date
- Cover art
- Lyrics if available
- DistroKid/streaming links
- Related artifacts

Add basic SEO:

- meta title
- meta description
- Open Graph image
- canonical URL

Add tests for public visibility boundaries:

- public artifacts visible
- private artifacts hidden
- FanVue-only artifacts hidden from public archive unless teaser mode is explicitly implemented
