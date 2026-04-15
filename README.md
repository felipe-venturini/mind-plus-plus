# Mind++ for Claude

**Your second brain, powered by Claude — inside Obsidian.**

> 🌍 Also available in: [Português (BR)](README.pt-BR.md) · [Español](README.es.md)

Mind++ is an open-source Claude Cowork plugin that transforms Claude into a proactive knowledge partner. It captures meetings, tracks commitments, delivers daily briefings, and maintains a living knowledge base for your professional and personal life — all stored as plain Markdown in your Obsidian vault.

---

## Why Mind++?

- **No vendor lock-in** — your data is plain `.md` files, readable anywhere
- **Privacy by default** — everything stays in your folder, on your machine
- **Obsidian-native** — wikilinks, frontmatter, and vault structure you already know
- **AI-powered, human-verified** — Claude processes, you confirm before anything moves
- **Proactive, not reactive** — surfaces overdue tasks and silent clients without being asked

---

## Skills included

| Skill | Description | Trigger |
|-------|-------------|---------|
| `setup` | Bootstrap your vault from scratch — creates folder structure, config files, and a personalized `CLAUDE.md` | "set up my second brain", "configure vault" |
| `user-profile` | Capture and update your professional and personal profile so Claude knows your context | "update my profile", "Claude, learn about me" |
| `new-meeting` | Process any meeting — transcript, raw notes, or verbal summary — into a structured note with action items | "I had a meeting with X", "process this transcript" |
| `meeting-prep` | Pre-meeting briefing — last meetings, open tasks, what you owe them, what they owe you, suggested talking points | "prep for meeting with X", "what should I talk about with X" |
| `capture-idea` | Quick low-friction idea capture — auto-classifies the context and saves to the right folder (or inbox if uncertain) | "note this", "idea:", "save this thought" |
| `new-decision` | Record an ADR — context, decision, consequences, and rejected alternatives — in the right scope | "record a decision", "new ADR", "we decided X" |
| `knowledge-search` | Semantic search across your vault — returns a synthesis with wikilinks to the source notes | "what do I know about X", "everything we discussed about Y" |
| `stakeholder-update` | Generate an external-facing status update for a client, product, or project from vault content | "status update on X", "client report for X" |
| `daily-brief` | Morning briefing with today's agenda, overdue tasks, and pending follow-ups | "brief", "what's on my plate today" |
| `weekly-review` | Friday consolidation — what got done, what's at risk, what's coming | "weekly review", "close the week" |
| `process-inbox` | Triage files with no home — proposes a destination and waits for your confirmation before moving anything | "process inbox", "triage files" |
| `process-meeting-emails` | Automatic pipeline: Gemini Meeting Notes / Fireflies / Otter emails → structured notes in your vault | "process Gemini emails", "run meeting pipeline" |

---

## Agents included

Agents are autonomous subprocesses that run in isolated contexts. Mind++ ships with two:

| Agent | What it does | When it runs |
|-------|--------------|--------------|
| `vault-researcher` | Deep read across many vault files — returns a clean synthesis instead of flooding the main conversation | Invoked automatically by `knowledge-search` for queries matching >15 files |
| `vault-auditor` | Full vault health check — overdue tasks, silent clients, dashboard drift, orphan files, stale ADRs | On demand ("audit my vault"), or scheduled weekly |

---

## Scheduled tasks

Cowork can run any skill on a schedule — cron expressions evaluated in your local timezone. The `setup` skill offers to create the common schedules:

| Task | Default schedule | Skill |
|------|------------------|-------|
| Daily brief | 8:00 AM, weekdays | `daily-brief` |
| Weekly review | 5:00 PM, Friday | `weekly-review` |
| Meeting-email pipeline | Every 2 hours | `process-meeting-emails` |
| Vault audit | 9:00 AM, Monday | `vault-auditor` agent |

You can create, edit, or remove any schedule later by asking ("schedule daily brief at 7am" / "remove the vault audit schedule"). Scheduled tasks only fire when Cowork is running on your Mac — missed tasks queue until the next session.

---

## Recommended setup

Mind++ is designed to work with three tools together:

### 1. Claude Cowork (required)
The plugin runs inside [Claude Cowork](https://claude.ai/download), the Claude desktop app. Select your Obsidian vault folder as your workspace — Claude reads and writes directly to it.

### 2. Obsidian (recommended)
[Obsidian](https://obsidian.md) is the best way to navigate and visualize your vault. Open the same folder you selected in Cowork. You get graph view, search, tags, and backlinks on top of everything Claude writes.

### 3. Obsidian Git (recommended for versioning)
Install the [Obsidian Git plugin by Vinzent03](https://github.com/Vinzent03/obsidian-git) to automatically sync your vault to a private GitHub repository. This gives you:
- Full version history of every note
- Mobile access via the Obsidian mobile app + GitHub sync
- Backup and disaster recovery

**Recommended flow:**
```
Claude Cowork  →  writes .md files  →  your Obsidian vault folder
Obsidian       →  reads same folder →  visual navigation + graph
Obsidian Git   →  syncs to GitHub  →  versioning + mobile access
```

---

## Getting started

### 1. Install the plugin
In Cowork, go to **Plugins** and install **Mind++ for Claude**.

### 2. Select your vault folder
In Cowork, select the folder where you want your vault to live. This can be an existing Obsidian vault or a new empty folder.

### 3. Run setup
Tell Claude: **"set up my second brain"**

The setup skill will:
- Detect whether you're starting fresh or have existing files
- Ask about your work context (clients, projects, tools)
- Create the full folder structure
- Generate config files (domain mapping, keyword aliases)
- Write a personalized `CLAUDE.md` with your context baked in

### 4. Connect external tools (optional)
In **Settings → Connectors**, connect:
- **Google Calendar or Outlook** — for agenda items in daily brief
- **Gmail or Outlook** — for the automatic meeting email pipeline
- **Google Drive** — to fetch full transcripts from cloud storage

### 5. Start using it
Say "brief" every morning. Say "I just had a meeting with X" after every call. Say "weekly review" every Friday.

---

## Vault structure

Mind++ creates and maintains this structure:

```
clients/{client}/
  {Client}.md              # Client dashboard
  meetings/                # YYYY-MM-DD Meeting Title.md
  decisions/               # ADRs — NNN Title.md
  references/              # Docs, briefings, spreadsheets
  Tasks {Client}.md        # Open tasks tracker

products/{product}/
  {Product}.md
  Tasks {Product}.md

operational/
  tasks/                   # Operational Tasks.md, Open Tasks.md, Processing Log.md
  config/                  # domain-mapping.yml, client-aliases.yml
  meetings/                # Internal meetings
  daily/                   # Saved daily notes and briefs
  decisions/               # Organizational ADRs
  mocs/                    # Maps of Content

personal/
  projects/
  learning/
  goals/
  notes/
  daily/

shared/
  templates/
  prompts/
  attachments/

inbox/                     # Inbox — triage with process-inbox skill
archive/                   # Closed items — moved here, never deleted
```

---

## Conventions

- **Wikilinks everywhere** — internal links always use `[[]]`, never markdown links
- **Required frontmatter** — every file has `title`, `date`, and `tags`
- **Every meeting generates tasks** — absolute invariant; no meeting is processed without updating the tasks file
- **80% confidence threshold** — automatic classification only happens with ≥80% confidence; below that, files go to `inbox/` for manual review
- **Never delete** — closed items move to `archive/`, they are never permanently deleted

---

## Privacy

All your data stays in the folder you selected, on your computer. The plugin does not send data to external servers beyond the APIs you explicitly connect (Google Calendar, Gmail, etc.). Your user profile and memories are stored locally in `.auto-memory/`.

---

## External connectors

See [CONNECTORS.md](CONNECTORS.md) for details on email, calendar, and cloud storage integrations.

---

## Contributing

Mind++ is open source under the MIT license. Contributions are welcome and encouraged.

- **Bug reports and feature requests** → [open an issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Code contributions** → see [CONTRIBUTING.md](CONTRIBUTING.md)
- **Translations** → add a `README.{lang}.md` file and open a PR
- **New skills** → follow the skill format in `skills/*/SKILL.md` and open a PR

The plugin is designed to be forked, modified, and adapted to your own workflow. See the license below.

---

## License

MIT — free to use, modify, distribute, and commercialize. See [LICENSE](LICENSE).
