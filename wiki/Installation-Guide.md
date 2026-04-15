# Installation Guide

A detailed, beginner-friendly walkthrough to get Mind++ running in under 15 minutes. If you've never used Obsidian or installed a Claude plugin before, this is for you.

## What you're installing

| Layer | Purpose | Required? |
|-------|---------|-----------|
| Claude Cowork (desktop app) | Runs the plugin and talks to your vault | **Yes** |
| Mind++ plugin (`.plugin` file) | Teaches Claude how to organize your notes | **Yes** |
| Obsidian (desktop app) | Visually navigate, graph, and link your notes | **Strongly recommended** |
| A sync strategy (cloud folder or Obsidian Git) | Backup and multi-device access | **Optional** |

You can run Mind++ without Obsidian — the plugin only needs a folder of `.md` files. But Obsidian is what turns the raw folder into a navigable second brain.

---

## Step 1 — Install Claude Cowork

1. Download from [claude.ai/download](https://claude.ai/download)
2. Open the app and sign in with your Claude account
3. Cowork works on macOS, Windows, and Linux

> **Note**: Cowork is Anthropic's desktop app that lets Claude read and write files on your computer. It runs locally — no notes leave your machine unless you explicitly connect a service like Gmail or Google Calendar.

## Step 2 — Install Obsidian (recommended)

1. Download from [obsidian.md](https://obsidian.md)
2. Open Obsidian — don't create a vault yet, we'll do that in step 3

## Step 3 — Choose where your vault will live

A "vault" is just a folder full of `.md` files. You decide where it lives. Pick one of these:

### Option A — simplest (local only)
```
~/Documents/Mind++
```
Fast, private, no sync. If your laptop dies, your notes die. Backups are your responsibility.

### Option B — cloud-synced folder (recommended for most)
Create the folder inside a cloud-synced path so your notes are backed up automatically:
- macOS: `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++` (iCloud)
- Any OS with Google Drive: `~/Google Drive/Mind++`
- Any OS with OneDrive: `~/OneDrive/Mind++`
- Any OS with Dropbox: `~/Dropbox/Mind++`

Claude Cowork and Obsidian both read the same files; the cloud service handles versioning and cross-device sync. You can open the same vault on your phone through the Obsidian mobile app pointing at the same cloud folder.

### Option C — Obsidian Git (power users)
Version your vault in a private GitHub repo using the [Obsidian Git plugin](https://github.com/Vinzent03/obsidian-git). You get commit history, rollback, and Android/iOS sync through Obsidian Mobile. Setup is more involved but gives you the strongest versioning.

See [Sync Strategies](Sync-Strategies) for a deeper comparison.

## Step 4 — Point Obsidian at the folder

1. Open Obsidian
2. "Open folder as vault" → select the folder you chose in step 3
3. Obsidian creates a `.obsidian/` subfolder for its settings. This is normal.

## Step 5 — Point Cowork at the same folder

1. Open Claude Cowork
2. Select a workspace folder → same folder from step 3
3. Claude now has read/write access to your vault

## Step 6 — Install the Mind++ plugin

1. Go to [Releases](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)
2. Download the `mind-plus-plus.plugin` file
3. In Cowork, open **Plugins**
4. Drag the `.plugin` file into the plugins area (or click Install)
5. Confirm the installation

## Step 7 — Run setup

In Cowork, tell Claude:

> **"set up my second brain"**

The setup skill will:
- Ask you about your work context (clients, products, tools)
- Create the folder structure (`clients/`, `products/`, `operational/`, `personal/`, `shared/`, `inbox/`, `archive/`)
- Write a personalized `CLAUDE.md` at the vault root so Claude remembers your preferences
- Offer to schedule the daily brief and weekly review

Say yes to whatever sounds useful — you can turn things off later.

## Step 8 — First use

Try these:

- **Morning brief**: say `brief` → Claude shows today's agenda, overdue tasks, follow-ups
- **Meeting capture**: say "I just had a meeting with X about Y" → Claude writes the note and extracts action items
- **Weekly review**: every Friday, say `weekly review` → Claude consolidates the week

That's it. Your second brain is running.

---

## Troubleshooting

### Cowork says it can't read my vault
- Make sure you've selected the exact folder (not a parent)
- Check macOS System Settings → Privacy → Files and Folders → Claude has access

### Obsidian shows the `.auto-memory/` folder in the sidebar
- This is where Claude stores your profile and memories
- Add `.auto-memory` to your Obsidian settings → Files & Links → Excluded files so it stays out of graph/search

### Claude isn't triggering the right skill
- Skills match on keywords in your message. Try more explicit phrasing: "process inbox", "weekly review", "prep me for X"
- If a skill never fires, open an issue on the repo — we may need to adjust the trigger phrases

### The plugin file won't install
- Confirm you downloaded the `.plugin` file, not the source zip
- Try re-downloading from [the latest release](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)

### I need help with something not here
- Check the [FAQ](FAQ)
- [Open an issue](https://github.com/felipe-venturini/mind-plus-plus/issues) — questions are welcome
