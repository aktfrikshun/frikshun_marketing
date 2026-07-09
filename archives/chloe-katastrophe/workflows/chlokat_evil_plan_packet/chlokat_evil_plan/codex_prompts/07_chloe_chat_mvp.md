# Codex Prompt 07: Chloe Chat MVP

Build Chloe chat MVP.

Goal:
Fans can talk to Chloe about approved public archive fragments, songs, lyrics, and canon.

Create:

- ChloeChatConversation
- ChloeChatMessage
- ChloeChatService
- CanonRetriever

Rules:

- Only public artifacts with `usable_in_chat=true` may be used
- Only approved CanonEntry records with `usable_in_chat=true` may be used
- FanVue-only or private artifacts must not be revealed in public chat
- Chloe should answer in character
- Chloe may say she does not remember something
- Chloe should occasionally invite the fan to explore related fragments
- Chloe should not claim facts outside approved canon

Public UI:

- `/chat`
- chat input
- conversation thread
- suggested questions

Admin:

- view chat logs
- flag useful questions
- convert good questions into FAQ/archive entries
- mark artifacts/canon as usable or not usable in chat

For now:

- use a mock LLM adapter
- retrieve relevant Artifact and CanonEntry records by keyword search
- design so a real LLM adapter can be added later

Add tests for retrieval boundaries.
