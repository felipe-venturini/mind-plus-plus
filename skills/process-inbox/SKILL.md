---
name: process-inbox
description: "Triages the inbox/ folder — sorts files with no defined destination. Use this skill when the user says 'process inbox', 'what's in the inbox', 'organize inbox', 'triage files', 'clean inbox', or similar. Lists all files, identifies context via aliases and domain mapping, proposes a destination following vault conventions, and waits for confirmation before moving anything. Never moves files automatically."
---

# Skill: process-inbox

## What this skill does

Triage of the `inbox/` folder — processes each file without a defined destination, proposes where it should go in the vault, and waits for confirmation before moving anything.

**Inviolable rule:** never move files automatically. Always present the proposal first.

---

## Step 1 — List files in inbox

Read all files in `inbox/`. For each one, note: name, extension, creation date.

If the inbox is empty, inform the user and stop.

---

## Step 2 — Identify each file

For each file in the inbox:

1. **Read the content** (or metadata if binary)
2. **Identify its nature:**
   - Meeting transcript or note
   - Briefing, spec, or plan
   - Reference document or spreadsheet
   - Decision or ADR
   - Idea or brainstorm
   - Personal note
   - Archived / closed document

3. **Identify the context:**
   - Check `operational/config/domain-mapping.yml` and `operational/config/client-aliases.yml`
   - Look for mentions of clients/projects in the content

4. **Propose a destination** following vault conventions:
   - Transcript / meeting note → `clients/{context}/meetings/YYYY-MM-DD Title.md` + trigger `new-meeting`
   - Briefing / plan → `clients/{context}/references/`
   - Decision → `clients/{context}/decisions/` or `operational/decisions/`
   - Idea about a context → `clients/{context}/` or `products/{product}/`
   - General idea → `operational/` or `personal/notes/`
   - Shared reference → `shared/`
   - Closed document → `archive/`
   - Personal note → `personal/notes/`

---

## Step 3 — Present the proposal

List all files with their proposed destination and justification:

```
📥 inbox/ — N files to triage

1. **file-name.md**
   Nature: Meeting note
   Context identified: {Context} (confidence: 90%)
   Proposed destination: clients/{context}/meetings/YYYY-MM-DD Title.md
   Additional action: process with new-meeting after moving

2. **another-file.pdf**
   Nature: Reference / Spreadsheet
   Context: {Context}
   Destination: clients/{context}/references/

3. **ambiguous-file.md**
   Nature: Note (not clearly identified)
   ⚠️ Needs input: which context does this belong to?
```

Ask for confirmation: "Ready to proceed with these moves? You can adjust any destination before confirming."

---

## Step 4 — Execute after confirmation

After explicit user confirmation:

1. Move each file to the correct destination
2. Rename if needed (following vault conventions)
3. Add YAML frontmatter if missing
4. For transcripts: trigger `new-meeting` automatically
5. Update the context dashboard if relevant

---

## Step 5 — Confirm result

List what was moved and where. If any files needed input and the user did not respond, keep them in inbox and list them at the end.
