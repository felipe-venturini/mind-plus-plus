# Wiki source

This folder holds the canonical Markdown source for the [Mind++ GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki).

GitHub wikis live in a separate git repo (`mind-plus-plus.wiki.git`) that only materializes after the first page is created through the web UI. Keeping the source here gives us:

- A single, reviewable source of truth (wiki edits can be proposed via PR)
- Easy bootstrap for forks that want their own wiki
- Version history alongside the plugin itself

## Pages

- [Home.md](Home.md) — wiki landing page
- [Installation-Guide.md](Installation-Guide.md) — step-by-step installation walkthrough
- [FAQ.md](FAQ.md) — frequently asked questions
- [Sync-Strategies.md](Sync-Strategies.md) — Obsidian Git vs. cloud folders vs. local-only

## How to sync changes to the live wiki

### Initial bootstrap (first time only)

GitHub doesn't expose a wiki-creation API. To initialize the wiki repo:

1. Visit https://github.com/felipe-venturini/mind-plus-plus/wiki
2. Click **Create the first page**
3. Paste the contents of [Home.md](Home.md) into the editor
4. Save — this creates the `.wiki.git` repo

After that, you can clone and push like any git repo:

```bash
git clone https://github.com/felipe-venturini/mind-plus-plus.wiki.git
cd mind-plus-plus.wiki
# copy the updated source files from ../mind-plus-plus/wiki/
cp ../mind-plus-plus/wiki/*.md .
git add -A
git commit -m "Sync wiki pages from repo source"
git push origin master
```

### Ongoing updates

Edit the files in this folder. Open a PR. Once merged, sync to the live wiki with the clone-copy-push flow above (or edit the wiki directly through the web UI — whichever is easier).
