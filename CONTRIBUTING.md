# Contributing to Mind++ for Claude

Thank you for your interest in contributing! Mind++ is designed to be forked, extended, and improved by the community. This document explains how.

---

## Ways to contribute

### Report bugs or request features
Open an issue at https://github.com/felipe-venturini/mind-plus-plus/issues

Include:
- What you expected to happen
- What actually happened
- Steps to reproduce (if a bug)
- Your Claude Cowork version

### Submit a pull request

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature-name`
3. Make your changes (see guidelines below)
4. Open a pull request with a clear description

### Add a translation

Add a `docs/README.{language-code}.md` file (e.g., `docs/README.fr.md` for French) following the structure of the existing `docs/README.md`, and add it to the `include:` list in `docs/_config.yml`. Translations live only under `docs/` (they power the website at felipe-venturini.github.io/mind-plus-plus); the repo root keeps only the English `README.md`. Then open a PR.

### Contribute a new skill

New skills should follow the format in existing `skills/*/SKILL.md` files.
Each skill is a **flat** folder directly under `skills/` (one folder per skill):

```
skills/
  your-skill-name/
    SKILL.md         ← required
    references/      ← optional: detailed reference files
```

**`SKILL.md` frontmatter:**
```yaml
---
name: your-skill-name
description: "Third-person description with specific trigger phrases the user would say."
---
```

**Then register it** in `.claude-plugin/plugin.json` under `"skills"` — list the
skill's folder path explicitly (e.g. `"./skills/your-skill-name/"`).
Listing the folder directly makes the `name:` frontmatter the authoritative
invocation name. An unlisted skill is silently not loaded.

**Guidelines for skill content:**
- Write the body as instructions FOR Claude, not documentation for the user
- Use imperative sentences: "Read the file", not "You should read the file"
- Keep the SKILL.md body under 3,000 words — move detail to `references/`
- Use `~~category` placeholders for external tools (e.g., `~~email`, `~~calendar`)
- Never hardcode personal names, company names, or specific client data

---

## Code guidelines

- **No personal data** — skills must be fully generic, with no names, companies, or client-specific logic
- **Use `~~` placeholders** for any external service reference (see `CONNECTORS.md`)
- **Markdown only** — the plugin is pure `.md` and `.json`, no code execution required
- **Preserve conventions** — wikilinks (`[[]]`), YAML frontmatter, and vault structure should be consistent across skills

---

## Plugin structure

```
mind-plus-plus/
├── .claude-plugin/
│   └── plugin.json              # Manifest
├── skills/                      # FLAT — one folder per skill directly under skills/
│   ├── setup-mind-plus-plus/
│   ├── user-profile/
│   ├── new-meeting/
│   ├── meeting-prep/
│   ├── capture-idea/
│   ├── new-decision/
│   ├── knowledge-search/
│   ├── stakeholder-update/
│   ├── daily-brief/
│   ├── weekly-review/
│   ├── process-inbox/
│   ├── process-meeting-emails/
│   │   ├── SKILL.md
│   │   └── references/          # (optional)
│   └── specialist/              # Orchestrator: routes requests to specialist agents
├── agents/                      # FLAT — auto-discovered; files named {domain}__{discipline}__{role}.md
│   ├── core__vault_researcher.md    # name: vault-researcher — deep multi-file research
│   ├── core__vault_auditor.md       # name: vault-auditor — vault health check
│   ├── core__specialist_judge.md    # name: specialist-judge — universal arbiter
│   ├── marketing__bi__data_analyst.md
│   ├── marketing__media__paid_traffic_analyst.md
│   ├── …                            # 65 business specialists across the 7 domains
│   └── admin__facilities__receptionist.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── CONNECTORS.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE
├── README.md                    # English (repo landing); translations live in docs/
└── docs/                        # GitHub Pages site — README.md + per-language README.{lang}.md
```

> **Where docs live:** `docs/` is the **website** source (GitHub Pages) — the
> English `README.md` plus per-language translations. **User-facing
> documentation** (installation, FAQ, sync strategies) lives in the
> [GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki).
> Internal planning notes are kept locally in `.planning/` (git-ignored).

---

## Domain organization

Both `skills/` and `agents/` are **flat** on disk so the plugin reads as a
single, coherent unit:

- **`skills/`** is the shared interaction layer — one folder per skill directly
  under `skills/` (e.g. `skills/new-meeting/SKILL.md`), each registered in
  `plugin.json`. Skills are cross-cutting, so the domain axis lives in the agents,
  not in skill subfolders.
- **`agents/`** holds every specialist as a **flat** `.md` file (Claude
  auto-discovers `agents/*.md`; discovery is not recursive, so agents must not be
  nested). The domain axis lives in the **filename** and the **frontmatter**, not
  in folders: files are named `{domain}__{discipline}__{role}.md` and carry
  `domain:`/`discipline:` fields. `core__*` files are cross-cutting agents
  (`vault-researcher`, `vault-auditor`, `specialist-judge`) that belong to no
  business domain; the other files cover the seven business domains
  (`marketing`, `tech`, `finance`, `hr`, `dp`, `legal`, `admin`).

The `specialist` skill (in `skills/specialist/`) is the bridge: it discovers the
domain's specialists, then hands routing and arbitration to the universal
`specialist-judge` agent (`agents/core__specialist_judge.md`) — which triages the
minimal set of specialists to run and reconciles their reports — while the skill
itself is the only component that dispatches agents and writes to the vault.

**Naming convention** for domain specialists: files live **flat** at
`agents/<domain>__<discipline>__<role>.md` — a **double underscore** (`__`)
between hierarchy levels and a **single underscore** (`_`) within a name (BI /
database style, e.g. `marketing__bi__data_analyst.md`,
`marketing__creative__art_director.md`). The `name:` frontmatter stays the
fully-qualified `<domain>-<discipline>-<role>` (e.g. `marketing-bi-data-analyst`)
— that `name:`, not the filename, is what Claude Code and the `specialist` skill
dispatch on, so keep it stable: renaming it silently breaks every reference.
Routing keys off the `domain:` frontmatter field: you invoke `/specialist <domain>
…` and the judge triages disciplines and roles.

> **Why flat?** The Claude plugin uploader treats `agents` manifest entries as
> directories and rejects file paths, and default agent discovery is not
> recursive. A flat `agents/` with encoded filenames is the layout that both the
> uploader and local tooling accept.

**Domain slugs:** `marketing`, `tech`, `finance`, `hr`, `dp`, `legal`, `admin`
(plus `core` for cross-cutting agents). All seven business domains are populated.

**Adding a new agent — one step:** drop the `.md` file at
`agents/<domain>__<discipline>__<role>.md` with a fully-qualified `name:` and
`domain:`/`discipline:` frontmatter fields. Claude auto-discovers it (no
`plugin.json` edit needed) and the `specialist` skill routes to it by `domain`.

---

## Questions?

Open an issue and tag it `question`. We're happy to help.
