# Codex Prompt 02: Artifact-to-Post Draft Generator

Implement `ArtifactDraftGenerator`.

When an admin uploads an Artifact, generate platform-specific drafts for each active PlatformAccount.

Platforms:

- Facebook
- Instagram
- YouTube
- TikTok
- X
- FanVue
- ChloKat Archive

Draft rules:

## Facebook

- Longer lore-forward post
- Framed as FrikShun documenting Chloe recovery
- Include a discussion question
- Include archive link

## Instagram

- Visual, poetic, concise
- Include “link in bio” when needed
- Include 5-12 hashtags

## YouTube

Generate variants depending on artifact type:

- YouTube Short caption for vertical video
- Community post text for images/lore
- Video description for longer video
- Include related release links if available

## TikTok

- Hook in first sentence
- Short caption
- 3-6 hashtags
- Invite curiosity

## X

- Very short post
- Optional thread starter
- 1-3 hashtags max
- Strong enough to stand alone without context

## FanVue

- Exclusive/private framing
- More intimate
- Mention unlocked archive access when appropriate

## ChloKat Archive

- Generate title
- Summary
- Lore text
- Suggested tags
- CTA: “Join the Reconstruction”
- CTA: “Talk to Chloe about this fragment”

Add admin button:

- Generate Drafts

Add tests:

- image generates Facebook, Instagram, YouTube, TikTok, X, FanVue, and Archive drafts
- video generates YouTube/TikTok/Instagram Reel-style drafts
- audio preview generates social drafts but does not replace DistroKid release flow
- private artifacts do not create public archive draft unless visibility is public
