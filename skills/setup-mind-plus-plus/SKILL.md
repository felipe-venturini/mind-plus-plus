---
name: setup-mind-plus-plus
description: "Sets up the Mind++ second brain from scratch — creates vault folder structure, captures the user profile, and generates configuration files. Use this skill when the user installs the plugin for the first time, says 'set up my second brain', 'set up mind plus plus', 'setup-mind-plus-plus', 'start from scratch', 'configure vault', or when no vault structure is found. Also trigger when the user wants to reset or update the base configuration of the system."
---

# Skill: setup-mind-plus-plus

## What this skill does

Bootstraps the second brain from zero: creates the Obsidian vault folder structure, captures who the user is and their context, and generates the configuration files that all other skills will use.

Can be run in two modes:
- **First time:** empty vault — create everything
- **Reconfiguration:** existing vault — update context and config without deleting data

---

## Step 1 — Detect current state

Check whether the vault already has structure:
- Does `operational/config/` exist? → reconfiguration mode
- Does `clients/` exist with subfolders? → list existing clients
- Does `CLAUDE.md` exist? → read and preserve customizations

---

## Step 2 — Capture user profile

Ask conversationally (not as a form — keep it natural):

1. **Who are you?** — name, role, area of work
2. **What's your work context?** — company or freelancer, main clients, active projects
3. **What do you want to track?** — client meetings, personal projects, learning, all of the above?
4. **Do you use a meeting transcription tool?** — Gemini Meeting Notes, Fireflies, Otter, other
5. **What's your work email domain?** — to classify internal vs. external meetings
6. **What's your preferred language for vault content?** — English, Portuguese, Spanish, other

Save the answers to `.auto-memory/user_profile.md` using the memory system format.

---

## Step 3 — Create folder structure

Create only the folders that make sense for the user's context:

### Base structure (always create)
```
clients/            # One directory per client/project
products/           # Own products or services (if applicable)
operational/
  tasks/            # Open tasks and aggregate
  config/           # domain-mapping.yml, client-aliases.yml
  daily/            # Saved briefs and reviews
  meetings/         # Internal meetings
  decisions/        # Organizational ADRs
  mocs/             # Maps of Content
personal/
  notes/
  learning/
  goals/
  daily/
  projects/
shared/
  templates/
  prompts/
  attachments/
inbox/              # Inbox — triage with process-inbox skill
archive/            # Closed items — move here, never delete
```

For each client mentioned in Step 2, create:
```
clients/{client-slug}/
  {Client}.md           # Dashboard (using template)
  meetings/
  references/
  decisions/
  Tasks {Client}.md
```

---

## Step 4 — Generate configuration files

### `operational/config/domain-mapping.yml`
Generate with the domains mentioned by the user:
```yaml
# Email domain → client context mapping
# Add your clients' email domains here

domains:
  # example-company.com: client-slug

internal:
  - {user-domain}  # your work email domain = internal meeting
```

### `operational/config/client-aliases.yml`
```yaml
# Keywords that identify each context in meeting titles and content
# aliases:
#   acme: acme-corp
#   project-name: client-slug

aliases: {}

internal: []
```

### `operational/tasks/Open Tasks.md`
Create the aggregate file with the identified clients listed.

---

## Step 5 — Create or update CLAUDE.md

If it doesn't exist, create `CLAUDE.md` at the vault root with:
- Vault identity (personalized to the user)
- Obsidian conventions (wikilinks, frontmatter)
- Trigger flows for each plugin skill
- Folder structure
- Reference to config files
- User's preferred language for content

If it already exists, preserve the content and only add missing sections.

---

## Step 6 — Offer scheduled tasks

Cowork supports scheduled tasks — recurring runs evaluated in the user's local timezone. Offer to create any of the following (one by one, waiting for explicit confirmation for each):

| Task | Suggested cron | Purpose |
|------|----------------|---------|
| Daily brief | `0 8 * * 1-5` (8:00 AM, weekdays) | Run `daily-brief` every weekday morning |
| Weekly review | `0 17 * * 5` (5:00 PM, Friday) | Run `weekly-review` at end of week |
| Meeting email pipeline | `0 */2 * * *` (every 2 hours) | Run `process-meeting-emails` to triage new Gemini / Fireflies / Otter emails |
| Vault audit | `0 9 * * 1` (9:00 AM, Monday) | Run `vault-auditor` agent weekly to catch inconsistencies |

For each, ask: "Want me to schedule {task} at {time}? You can customize the time or skip."

When confirmed, call the `create_scheduled_task` tool with:
- A `taskName` in kebab-case (e.g., `mind-plus-plus-daily-brief`)
- A `cronExpression` in the user's local timezone
- A self-contained `prompt` that re-triggers the skill (example: "Run the daily-brief skill for today")

Important caveat to mention: **Scheduled tasks only fire when Cowork is running on the user's Mac.** Missed tasks queue until next session. This is client-side, not cloud-based.

---

## Step 7 — Confirm and guide next steps

At the end, inform the user:
- What was created (folders, configs, CLAUDE.md, scheduled tasks)
- How to add new clients (`clients/{name}/`)
- How `new-meeting` will capture meetings
- How to set up GitHub sync (optional, for mobile access via Obsidian Git)
- How to trigger other skills on demand (`capture-idea`, `new-decision`, `knowledge-search`, `stakeholder-update`, `meeting-prep`)
- That the user can always say "schedule X at Y" later to create or edit any scheduled task

---

## Template: CLAUDE.md

When creating CLAUDE.md from scratch, use this structure:

```markdown
# Mind++ for Claude

Personal and professional knowledge management system.

## Preferred language
{user's preferred language}

## Core principles
1. Wikilinks always — internal links use [[]], never [text](path.md)
2. Markdown is the source of truth — everything persists in files
3. Every meeting generates tasks — absolute invariant
4. Proactive coverage — surface overdue items and silent contacts unprompted

## Skill triggers
| Trigger | Skill |
|---------|-------|
| Meeting, transcript, notes | new-meeting |
| "prep for meeting with X" | meeting-prep |
| "note this", "idea:", "save this" | capture-idea |
| "record a decision", "new ADR" | new-decision |
| "what do I know about X" | knowledge-search |
| "status update for X" | stakeholder-update |
| "brief", "what do I have today" | daily-brief |
| "weekly review", "close the week" | weekly-review |
| "process inbox", "triage files" | process-inbox |
| "process emails", automatic pipeline | process-meeting-emails |

## Agents (autonomous subprocesses)
- `vault-researcher` — invoked by `knowledge-search` for large queries; reads many files in isolation and returns a synthesis
- `vault-auditor` — runs on schedule or on demand; finds inconsistencies, orphan tasks, stale dashboards

## Conventions
- File names: readable, date-prefixed when relevant (YYYY-MM-DD Title.md)
- Folder names: lowercase with hyphens, no accents
- Frontmatter: title, date, tags (YAML list)
- Tags: always as a list — never inline
- Confidence threshold for auto-classification: 80%
```
