# Mind++ for Claude

**Your second brain, powered by Claude — inside Obsidian.**

> 🌍 Available in: [English](README.md) · [Português (BR)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [বাংলা](README.bn.md) · [Русский](README.ru.md) · [اردو](README.ur.md)
>
> 📖 **Full docs & guides** → [GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki) · 🌐 **Website** → [felipe-venturini.github.io/mind-plus-plus](https://felipe-venturini.github.io/mind-plus-plus)

Mind++ is a free, open-source plugin for [Claude Cowork](https://claude.ai/download) that turns Claude into a proactive knowledge partner. It captures meetings, tracks commitments, delivers daily briefings, and maintains a living knowledge base for your professional and personal life — all stored as plain Markdown in an [Obsidian](https://obsidian.md) vault.

**Download the plugin → [latest release](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)**

---

## Never used this before? Start here.

If you've never heard of Obsidian or written a Markdown note, don't worry. Here's the one-paragraph version:

**Obsidian** is a free app ([obsidian.md](https://obsidian.md)) that reads a folder of `.md` (Markdown) text files on your computer and shows them as a beautiful, linked notebook. Because everything is plain text, **your notes are yours forever** — no cloud lock-in, no paid subscription, no vendor that can disappear. Mind++ uses Obsidian's folder structure as the foundation because it's the most durable and private format for personal knowledge that exists today.

**Claude Cowork** is the Claude desktop app ([claude.ai/download](https://claude.ai/download)) that can read and write files on your computer. When you install Mind++, Claude learns a specific way of organizing your notes inside that folder — so when you say "I had a meeting with John," it writes the note, extracts the action items, and updates your task list automatically.

**You do not need to be a developer.** You don't need to know Git. You don't need to know YAML. Mind++ handles the structure; you just talk to Claude.

---

## Why Mind++?

- **No vendor lock-in** — your data is plain `.md` files, readable in any text editor, anywhere
- **Privacy by default** — everything stays in your folder, on your computer
- **Obsidian-native** — graph view, backlinks, search, and tags work out of the box
- **AI-powered, human-verified** — Claude processes; you confirm before anything is moved or deleted
- **Proactive, not reactive** — surfaces overdue tasks and silent clients without being asked
- **Multilingual** — the plugin works in any language you write in; Claude adapts to you

---

## Quickstart in 5 minutes

> 👉 **Prefer a detailed walkthrough?** → [Installation Guide on the Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Installation-Guide)

### 1. Install the three tools

| Tool | What it does | Link |
|------|-------------|------|
| **Claude Cowork** (required) | The Claude desktop app that runs the plugin | [claude.ai/download](https://claude.ai/download) |
| **Obsidian** (highly recommended) | Visual navigator for your notes | [obsidian.md](https://obsidian.md) |
| **Your sync choice** (optional) | Back up and access notes anywhere — pick one: [Obsidian Git](https://github.com/Vinzent03/obsidian-git), Google Drive, iCloud Drive, OneDrive, or Dropbox | see [Sync Strategies](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) |

### 2. Choose where your vault will live

Pick a folder on your computer. This is where every note, meeting, and decision will be stored.

- **Simplest** — create a folder like `~/Documents/Mind++`
- **Backed up to the cloud automatically** — create the folder inside a cloud-synced location: `~/Google Drive/Mind++`, `~/OneDrive/Mind++`, `~/Dropbox/Mind++`, or `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++` (iCloud). Obsidian and Cowork will read the same files, and the cloud service versions and syncs them to all your devices.
- **Power user path** — use the [Obsidian Git plugin](https://github.com/Vinzent03/obsidian-git) to version your vault in a private GitHub repo (gives you commit history, rollback, and Android/iOS sync via the Obsidian mobile app)

> See the [Sync Strategies Wiki page](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) for trade-offs and a recommendation per use case.

### 3. Install the Mind++ plugin

1. Download the latest [`mind-plus-plus.plugin`](https://github.com/felipe-venturini/mind-plus-plus/releases/latest) file
2. Open Claude Cowork → **Plugins**
3. Drop the `.plugin` file into the plugins area (or click install)

### 4. Select your vault folder in Cowork

In Claude Cowork, select the folder you chose in step 2 as your workspace. Claude will read and write directly to it.

### 5. Run the setup

Tell Claude:

> **"set up my second brain"**

Setup will ask about your work context (clients, products, tools), create the folder structure, write a personalized `CLAUDE.md` with your context, and offer to schedule a daily brief and weekly review.

### 6. Start using it

- Say **"brief"** every morning → Claude shows today's agenda, overdue tasks, and follow-ups
- Say **"I just had a meeting with X"** after any call → Claude writes the note and updates your tasks
- Say **"weekly review"** every Friday → Claude consolidates the week

That's it. The more you use it, the more your vault becomes a true second brain.

---

## What's inside the plugin

### 12 skills

| Skill | What it does | Example trigger |
|-------|--------------|-----------------|
| `setup` | Bootstraps your vault from scratch | "set up my second brain" |
| `user-profile` | Captures your professional and personal profile | "update my profile" |
| `new-meeting` | Turns transcripts or notes into structured meeting records with action items | "I had a meeting with X" |
| `meeting-prep` | Pre-meeting briefing — last meetings, open tasks, talking points | "prep for meeting with X" |
| `capture-idea` | Quick low-friction idea capture, auto-classified to the right folder | "note this: …" |
| `new-decision` | Records an Architecture Decision Record (ADR) in the right scope | "record a decision" |
| `knowledge-search` | Semantic search across the vault with a synthesis and source links | "what do I know about X" |
| `stakeholder-update` | External-facing status report for a client, product, or project | "status update on X" |
| `daily-brief` | Morning briefing: agenda, overdue tasks, pending follow-ups | "brief" |
| `weekly-review` | Friday consolidation: what got done, what's at risk, what's next | "weekly review" |
| `process-inbox` | Triages files with no home, proposes a destination, waits for confirmation | "process inbox" |
| `process-meeting-emails` | Automatic pipeline: Gemini / Fireflies / Otter emails → structured notes | "run meeting pipeline" |

### 2 agents

Agents are autonomous subprocesses that run in isolation and return a clean result.

| Agent | What it does | When it runs |
|-------|-------------|-------------|
| `vault-researcher` | Deep read across many files without flooding your main conversation | Automatically, when `knowledge-search` matches >15 files |
| `vault-auditor` | Full vault health check: overdue tasks, silent clients, orphan files, stale decisions | On demand ("audit my vault") or scheduled weekly |

### Scheduled tasks

Cowork can run any skill on a schedule. Setup offers to create these:

| Task | Default schedule | Skill |
|------|------------------|-------|
| Daily brief | 8:00 AM, weekdays | `daily-brief` |
| Weekly review | 5:00 PM, Friday | `weekly-review` |
| Meeting-email pipeline | Every 2 hours | `process-meeting-emails` |
| Vault audit | 9:00 AM, Monday | `vault-auditor` agent |

You can create, edit, or remove schedules anytime — just ask Claude.

---

## How your vault gets organized

Mind++ creates and maintains this structure. You don't have to memorize it — Claude knows where things go.

```
clients/{client}/       ← one folder per client
  {Client}.md           ← dashboard with contacts, active projects, status
  meetings/             ← YYYY-MM-DD Meeting Title.md
  decisions/            ← ADRs — NNN Title.md
  references/           ← briefings, spreadsheets, supporting docs
  Tasks {Client}.md     ← open tasks tracker

products/{product}/     ← your own products (if any)
operational/            ← internal company work, team, config
personal/               ← personal projects, goals, notes
shared/                 ← templates, prompts, attachments
inbox/                  ← uncertain items — triage with process-inbox
archive/                ← closed items — moved here, never deleted
```

More detail on the [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki).

---

## Privacy

Everything stays on your computer. Mind++ does not send your data anywhere. The only external services involved are the ones you explicitly connect in Cowork (e.g., Gmail for the meeting-email pipeline, Google Calendar for the daily brief) — and those are opt-in.

If you use Obsidian Git or a cloud-synced folder (Drive, OneDrive, Dropbox, iCloud), your notes are replicated to that service — but you chose it and you control it.

Your user profile and memories live locally in a hidden `.auto-memory/` folder inside your vault.

---

## Frequently asked questions

A short list — full FAQ on the [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/FAQ).

**Do I need to know Markdown?** No. Claude writes the Markdown for you. You just talk in natural language.

**Can I use this without Obsidian?** Yes — the plugin only needs the folder. Obsidian is highly recommended because the graph view and backlinks make the vault useful, but technically you can browse the files in any editor.

**Can I use this in a language other than English?** Yes. Tell Claude your preferred language during setup (or at any time), and it will write notes, briefs, and reviews in that language. The plugin structure uses English folder names by design (for portability), but your content is in your language.

**What if I already have notes in Obsidian?** Point Mind++ at your existing vault. Setup detects existing files and integrates rather than overwriting.

**How do I get my notes on mobile?** Use Obsidian Git (syncs to a private GitHub repo you access via the Obsidian mobile app), or put your vault in a cloud folder (Drive / OneDrive / Dropbox / iCloud) and open it on your phone.

---

## Credits

**Co-authored by** [Felipe Venturini](https://github.com/felipe-venturini) and [sioux1to1](https://github.com/sioux1to1).

Built with [Claude](https://claude.ai) by Anthropic. Powered by [Claude Cowork](https://claude.ai/download) and inspired by the [Obsidian](https://obsidian.md) community.

---

## Contributing

Mind++ is open source under the MIT license. Contributions are welcome.

- **Bug reports and feature requests** → [open an issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Code contributions** → see [CONTRIBUTING.md](CONTRIBUTING.md)
- **Translations** → add a `README.{lang}.md` file and open a PR
- **New skills** → follow the format in `skills/*/SKILL.md` and open a PR

---

## License

MIT — free to use, modify, distribute, and commercialize. See [LICENSE](LICENSE).
