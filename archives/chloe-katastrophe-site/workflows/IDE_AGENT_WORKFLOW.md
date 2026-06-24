# IDE Agent Workflow

## Goal

Use Cursor or Codex as the repo-native Chloe agent while preserving the custom Chloe personality and canon discipline.

## Recommended Loop

1. Open this repository in Cursor or a terminal.
2. Start a new branch.
3. Give the agent a specific task.
4. Ask it to list files it plans to change.
5. Review the diff.
6. Commit only approved changes.
7. Push to GitHub if desired.

## Example Prompt for Codex/Cursor

You are Chloe Katastrophe's canon maintenance agent. Read `AGENTS.md`, `README.md`, `canon/CHLOE_CANON_MASTER.md`, and `visuals/VISUAL_REFERENCE_GUIDE.md` first. Then add a new character sheet for Gregor Volkov, update the character roster, update canon decisions, and show me the diff before committing.

## Suggested Git Commands

```bash
git checkout -b feature/gregor-reference
# edit files
git diff
git add .
git commit -m "Add Gregor Volkov visual planning files"
```
