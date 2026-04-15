---
name: capture-idea
description: "Captures a quick idea, note, or thought with minimum friction — auto-classifies the context (client, product, personal, operational) and saves it to the right place, or routes to inbox/ when uncertain. Use when the user says 'note this', 'quick note', 'idea:', 'capture this', 'jot down', 'save this thought', or shares a standalone thought without framing it as a task or meeting."
---

# Skill: capture-idea

## What this skill does

Saves an idea or fleeting note with as little ceremony as possible. The user should be able to dump a thought and trust that it lands in the right folder, with proper frontmatter and wikilinks, ready to be found later.

The core principle: **speed over perfection**. Better to save a note to `inbox/` and triage later than to make the user answer five questions before capturing.

---

## Step 1 — Extract the raw content

Treat whatever the user said after the trigger phrase as the idea body. Do not summarize or rewrite it unless obviously needed for clarity (e.g., fixing a broken sentence). Preserve the user's voice.

---

## Step 2 — Classify the context

Run quick heuristics to decide where it belongs. Stop at the first match:

1. **Does the idea mention a known client?** → `clients/{slug}/` (check against `operational/config/client-aliases.yml`)
2. **Does it mention a known product?** → `products/{slug}/`
3. **Is it about internal processes, team, or company strategy?** → `operational/`
4. **Is it personal (hobbies, life, relationships, personal projects)?** → `personal/`
5. **Is it a learning note or study topic?** → `personal/learning/`
6. **Uncertain?** → `inbox/`

Only go to `inbox/` when classification confidence is below ~80%. Do not over-ask.

---

## Step 3 — Decide the destination file

Within the chosen folder, pick one of:

- **New file** — if the idea is substantial (>3 sentences) or clearly a new topic. Name: `{YYYY-MM-DD} {short title}.md`
- **Append to existing file** — if the idea clearly continues a recent note (same topic, <7 days old). Append under a `## {today's date}` heading.
- **Append to a "notes" catch-all** — for short thoughts that don't warrant their own file. Use `{folder}/notes.md` or `{folder}/Ideas.md` depending on convention; create if missing.

Default to **new file** when in doubt. Small files are cheaper than misplaced appends.

---

## Step 4 — Write the file

Use standard frontmatter:

```yaml
---
title: {short title}
date: {YYYY-MM-DD}
tags:
  - idea
  - {context tag if applicable}
---
```

Body: the idea itself, cleaned minimally. Add wikilinks where entities are obvious (e.g., client name → `[[Client Name]]`).

If the idea references a task or action, add a closing line:
```
> Action item: {action}. Consider adding to [[Tasks {Context}]].
```
Do not add to the tasks file automatically — only mention.

---

## Step 5 — Confirm in chat

Respond with a one-line confirmation:

> Saved to `[[{path}]]`. {Optional: "Parked in inbox — triage with `process-inbox` when ready."}

Do not repeat the idea back. Do not summarize. Do not lecture about next steps. The user just wanted it captured.

---

## Edge cases

- **Idea contains multiple unrelated thoughts** — split into separate files, report back with all paths
- **Idea is actually a task in disguise** ("remind me to..." / "I need to...") — save as a note AND offer to add it to the relevant `Tasks {Context}.md`, waiting for confirmation
- **Idea is sensitive or personal** — never save to a client or operational folder under any circumstance; default to `personal/notes/` or memory
- **User is mid-meeting capture** — if the idea clearly belongs to a meeting being processed, defer to `new-meeting` skill instead
