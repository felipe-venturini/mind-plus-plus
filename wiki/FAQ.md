# Frequently Asked Questions

Short answers to the things people ask most. Longer walkthroughs live in the [Installation Guide](Installation-Guide) and [Sync Strategies](Sync-Strategies).

## The basics

### What is Mind++?
A free, open-source Claude Cowork plugin that turns Claude into a proactive knowledge partner. It captures meetings, tracks commitments, delivers daily briefs, and maintains a living knowledge base — all stored as plain Markdown inside an Obsidian vault.

### What is Obsidian and why is the plugin tied to it?
Obsidian is a free app that reads a folder of `.md` files and displays it as a beautifully interlinked notebook with graph view, backlinks, and semantic navigation. Mind++ uses Obsidian's folder structure as its foundation because plain Markdown is the most durable, portable, and private format for personal knowledge. **Your notes are yours forever** — no vendor lock-in.

### Do I need to be a developer?
No. You don't need Git. You don't need YAML. You don't need Markdown knowledge. Mind++ handles the structure; you just talk to Claude in natural language.

### Is this free?
Yes — MIT-licensed open source. The only costs are whatever you pay for Claude Cowork itself (check [claude.ai](https://claude.ai) for current pricing) and optional tools like a cloud sync service if you choose one.

---

## Using Mind++

### Do I need to know Markdown?
No. Claude writes the Markdown for you. You speak in natural language; Claude structures, links, and files.

### Can I use it in a language other than English?
Yes. Tell Claude your preferred language during setup (or anytime — `update my profile` works). Claude will write notes, briefs, and reviews in that language. The folder structure uses English names by design (for portability across languages and tools), but your *content* is in your language.

### What if I already have notes in Obsidian?
Point Mind++ at your existing vault. The setup skill detects existing files and integrates without overwriting. New structure is added alongside what's already there.

### Can I use it without Obsidian?
Yes — the plugin only needs a folder of `.md` files. But Obsidian is strongly recommended because graph view and backlinks are what make a vault feel like a second brain rather than just a folder.

### How do I access my notes on mobile?
Two options:
1. **Obsidian Git** → syncs with a private GitHub repo; access via Obsidian Mobile app
2. **Cloud folder** → put your vault in Google Drive / OneDrive / Dropbox / iCloud; open it in Obsidian Mobile pointing at that cloud-synced folder

See [Sync Strategies](Sync-Strategies) for detail.

---

## Privacy & data

### Does Mind++ send my data anywhere?
No. Everything stays on your machine. The plugin is local code + local Markdown files. The only external services involved are ones *you* explicitly connect in Cowork (like Gmail for the meeting email pipeline, or Google Calendar for the daily brief) — and those are opt-in per service.

### What about when Cowork talks to Claude's servers?
When Claude processes your request, the relevant parts of the conversation go to Anthropic's servers (that's how Claude works). But your vault files don't get uploaded wholesale — Claude only reads what's needed to answer the current request.

### Where does Mind++ store its own memory about me?
In a hidden `.auto-memory/` folder inside your vault. It stays on your computer like everything else.

### What if I use a cloud sync folder?
Your notes get replicated to that cloud service (Drive, OneDrive, Dropbox, iCloud, or GitHub). That's your choice and your control — revoke access or change services anytime.

---

## Skills, agents, and schedules

### What's the difference between a skill and an agent?
- **Skills** run in your main conversation with Claude. They're like specialized modes Claude enters when you ask for something specific (`brief`, `new meeting`, `process inbox`).
- **Agents** run in an isolated sub-conversation. They don't clutter your main chat — they do heavy work (like reading 30 files) and return a clean result.

### Can I edit or disable a skill?
Yes. Each skill lives in `skills/{name}/SKILL.md` inside the plugin. You can open it, modify it, or create your own. See [CONTRIBUTING.md](https://github.com/felipe-venturini/mind-plus-plus/blob/main/CONTRIBUTING.md) on the main repo.

### Can I change the schedule of the daily brief / weekly review?
Yes. Tell Claude "change my daily brief to 9am" or "disable the weekly review". Scheduled tasks in Cowork are editable anytime.

### What if I don't want the email pipeline running every 2 hours?
Say "disable the email pipeline" or "only run it when I ask". It's opt-in and configurable.

---

## Common issues

### Claude isn't triggering the right skill when I ask
Skills match on keywords. Try more explicit phrasing — "weekly review", "process inbox", "prep me for the meeting with X". If a skill reliably fails to trigger on natural phrasing, it's worth an issue on the repo.

### My vault is getting messy
Use `process-inbox` regularly to clean up stuck files. Use the `vault-auditor` agent ("audit my vault") to get a full health check — overdue tasks, silent clients, orphan files, stale decisions.

### Claude is forgetting things between conversations
Check `.auto-memory/MEMORY.md` in your vault. That's Claude's long-term memory. If something important isn't there, tell Claude to remember it.

### Something else
[Open an issue](https://github.com/felipe-venturini/mind-plus-plus/issues) — we read all of them.

---

## Contributing

### I want to add a new skill
Follow the format in any existing `skills/{name}/SKILL.md` and open a PR. See [CONTRIBUTING.md](https://github.com/felipe-venturini/mind-plus-plus/blob/main/CONTRIBUTING.md).

### I want to translate the README
Add `README.{lang}.md` in the root and update the language banner in all existing READMEs. Open a PR.

### I want to improve the wiki
Suggest changes via an issue on the main repo. Wiki edits are currently curated.

---

## Credits

Mind++ is co-authored by [Felipe Venturini](https://github.com/felipe-venturini) and [sioux1to1](https://github.com/sioux1to1). MIT-licensed.
