# Sync Strategies

Your vault is just a folder of `.md` files. How you back it up and sync it across devices is up to you. This page compares the three common strategies so you can pick the right one.

## TL;DR — pick one

| Your situation | Pick this |
|---------------|-----------|
| Just want it to work, don't care about history | **Cloud folder** (iCloud / Drive / OneDrive / Dropbox) |
| Want version history and easy rollback | **Obsidian Git** |
| Laptop-only, happy with Time Machine / Windows Backup | **Local folder**, no sync plugin |
| Multi-device including phone, non-technical | **Cloud folder** |
| Multi-device including phone, want Git history | **Obsidian Git** |

---

## Option 1 — Local folder (no sync)

**What it is**: Vault lives somewhere like `~/Documents/Mind++`. No cloud, no Git, no extra tools.

**Pros**
- Simplest setup — just pick a folder and go
- Fastest performance
- Zero configuration overhead

**Cons**
- No automatic backup — if the laptop dies, you lose everything
- No access from another device
- No history — a bad edit is a lost note

**Recommended for**: Users with strong local backup discipline (Time Machine, Windows File History) who work on a single machine.

---

## Option 2 — Cloud-synced folder

**What it is**: Create your vault *inside* a cloud-synced folder path. The cloud service handles backup, versioning, and multi-device sync transparently. Obsidian and Cowork just see a regular folder.

### Paths to use

| Service | macOS path | Windows path |
|---------|-----------|--------------|
| iCloud Drive | `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++` | N/A (macOS only practically) |
| Google Drive | `~/Google Drive/My Drive/Mind++` | `%USERPROFILE%\Google Drive\My Drive\Mind++` |
| OneDrive | `~/OneDrive/Mind++` | `%USERPROFILE%\OneDrive\Mind++` |
| Dropbox | `~/Dropbox/Mind++` | `%USERPROFILE%\Dropbox\Mind++` |

**Pros**
- Near-zero setup — you probably already have one of these installed
- Multi-device sync works out of the box
- Cloud providers retain recent versions (rollback within the cloud service)
- Works on mobile: open the same folder via Obsidian Mobile pointing at the cloud app's synced folder

**Cons**
- Version history is limited and service-specific (not a true commit log)
- Occasional sync conflicts if you edit from two devices simultaneously (usually resolved by the cloud service, but review `*conflict*` files)
- Large vaults (thousands of files) may hit some services' rate limits

**Recommended for**: Most users. Unless you specifically want Git semantics, this is the lowest-friction path.

### Cowork + cloud folder: does it work?
Yes. Cowork reads files from disk; it doesn't care that the disk location is a cloud-synced path. The cloud service syncs changes in the background.

### Tip
Some cloud services do "on-demand" file download by default (files show up but aren't actually downloaded until opened). Make sure your vault folder is set to "always keep on this device" to avoid Claude hitting files that aren't locally present.

---

## Option 3 — Obsidian Git

**What it is**: Version your vault in a private GitHub repo using the [Obsidian Git plugin](https://github.com/Vinzent03/obsidian-git) by Vinzent03. Every change is a commit.

**Setup in short**
1. Create a private GitHub repo (e.g. `username/my-mind-vault`)
2. Initialize your vault folder as a Git repo (`git init` + add remote)
3. Install Obsidian Git from Obsidian's community plugins
4. Configure auto-commit + auto-push intervals in the plugin settings
5. On mobile: Obsidian Mobile + Obsidian Git works on both Android and iOS

**Pros**
- True commit history — see exactly what changed, when, and revert anything
- Works across any number of devices
- Private GitHub repo is free for unlimited collaborators
- Mobile sync through Obsidian Mobile + Obsidian Git

**Cons**
- Steeper learning curve — you need to understand what Git is doing
- Merge conflicts if two devices diverge before syncing
- Requires a GitHub account and comfort with the Obsidian plugin settings

**Recommended for**: Power users who want strong version control, or anyone who already uses GitHub and wants consistency.

### Combining Cowork + Obsidian Git
Totally fine. Cowork reads/writes files; Obsidian Git commits the changes in the background. If you want cleaner commit messages, you can configure Obsidian Git to commit with a message template like "vault: auto-sync from Cowork".

---

## Mobile access

All three options support mobile:

| Option | Mobile path |
|--------|------------|
| Local folder | ❌ (no sync = no mobile access) |
| Cloud folder | Open Obsidian Mobile, point it at the cloud-synced folder |
| Obsidian Git | Obsidian Mobile + Obsidian Git plugin on iOS/Android |

Obsidian Mobile is free on both iOS and Android.

---

## My recommendation (Felipe's take)

If you're not sure, **start with a cloud folder** (iCloud if you're on Mac, OneDrive if you're on Windows, Google Drive if you're ecosystem-agnostic). It gives you backup + multi-device + zero setup.

Upgrade to Obsidian Git later if you find yourself wanting real version history — you can migrate by `git init`-ing your existing cloud-synced folder and pushing it to a private repo.

---

## Common questions

### Can I combine cloud folder + Obsidian Git?
Technically yes, but it's redundant and risks race conditions between the cloud sync and Git's internal files. Pick one.

### Does Claude Cowork store anything in the cloud?
No. The plugin files, your vault, and Cowork's state all stay on disk. What goes to Anthropic's servers is just the parts of your conversation Claude needs to process your request — not your whole vault.

### What about end-to-end encryption?
Cloud services (iCloud, Drive, OneDrive, Dropbox) are encrypted in transit and at rest, but the cloud provider can technically access your files. If you need true E2E, use Obsidian Git with a private repo (still not E2E from GitHub's perspective, but more auditable) or a provider like Proton Drive with E2E.

### Can I migrate between options?
Yes, and it's easy:
- **Local → Cloud**: move the folder into the cloud-synced path
- **Cloud → Git**: `cd vault && git init && git add . && git commit -m "initial" && git remote add origin ... && git push -u origin main`
- **Git → Cloud**: copy files out, `rm -rf .git`, move to cloud folder

Your `.md` files are always portable.
