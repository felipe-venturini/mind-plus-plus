---
name: new-meeting
description: "Processes a meeting and updates the vault. Use this skill whenever the user mentions a meeting, transcript, meeting notes, or automatic transcription email (Gemini, Fireflies, Otter). Trigger when the user says 'I had a meeting with X', 'process this transcript', 'save this meeting', 'log this call', or pastes raw notes. Every processed meeting results in a saved note + updated tasks + updated dashboard."
---

# Skill: new-meeting

## What this skill does

Transforms any meeting — raw transcript, automatic email, handwritten notes, or verbal summary — into three coordinated vault updates:

1. **Structured meeting note** → `clients/{context}/meetings/YYYY-MM-DD Title.md`
2. **Updated tasks** → `clients/{context}/Tasks {Context}.md`
3. **Updated dashboard** → `clients/{context}/{Context}.md`

**Invariant:** every processed meeting MUST generate at least one entry in the tasks file. If no actions came out of it, record explicitly: "no tasks generated in this meeting."

---

## Step 1 — Identify the context

Determine who or what the meeting was about. Try in order:

1. User stated explicitly ("meeting with [Name/Company]")
2. External participants' email domains → `operational/config/domain-mapping.yml`
3. Keywords in the content → `operational/config/client-aliases.yml`
4. Calendar context — if available via ~~calendar

**If confidence is <80%:** stop and ask before continuing.

**Internal meeting** (all participants from the same organization): save in `operational/meetings/` and update `operational/tasks/Operational Tasks.md`.

**Personal meeting** (no clear professional context): ask the user whether to log it in `personal/` or skip.

---

## Step 2 — Read existing context

Before writing anything, read:
- `clients/{context}/{Context}.md` — current dashboard (contacts, projects, history)
- `clients/{context}/Tasks {Context}.md` — open tasks

This allows closing already-resolved items and avoiding duplicates.

---

## Step 3 — Create the meeting note

Save to: `clients/{context}/meetings/YYYY-MM-DD Descriptive Title.md`

**Frontmatter:**
```yaml
---
title: YYYY-MM-DD Descriptive Title
date: YYYY-MM-DD
tags:
  - meeting
  - {context-tag}
participants:
  - Your Name
  - First Last (Organization)
---
```

**Structure:**
```markdown
# YYYY-MM-DD — Descriptive Title

> Meeting with [[{Context}]]. [[Tasks {Context}]] updated with N actions.

## Agenda
## Notes
## Decisions
## Next steps
- [ ] Action — due YYYY-MM-DD — owner: Name
```

Use wikilinks `[[]]` to reference contexts, task files, and other vault notes.

---

## Step 4 — Update tasks

Open `Tasks {Context}.md` and:

**Add** each action identified in the meeting to the correct section:
- Own action → `## Open (our side)` with due date and wikilink to the note
- Waiting on the other side → `## Waiting on others` with a follow-up date

**Close** items resolved during the meeting → move to `## Completed (last 30 days)` with date.

**Format:**
```
- [ ] Action — due YYYY-MM-DD — from [[YYYY-MM-DD Title]] — owner: Name
```

---

## Step 5 — Update the dashboard

Surgical edit to `clients/{context}/{Context}.md`:
- **Last meeting:** date + wikilink to the note
- **New contacts:** add if someone new appeared
- **Project status:** update if something relevant changed

---

## Step 6 — Confirm to the user

```
✅ Meeting processed: [[YYYY-MM-DD Title]]

Tasks added: N
Tasks closed: N
Dashboard updated: ✓

⚠️ Decisions worth an ADR (suggestion — not created automatically):
- [if any]
```

Suggest ADRs when an architectural or strategic decision was made — never create them automatically.
