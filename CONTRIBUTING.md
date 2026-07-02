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
4. Run `python3 scripts/validate_plugin.py` — it checks that every skill and
   agent is registered in `plugin.json` and well-formed (CI runs the same check)
5. Open a pull request with a clear description

### Add a translation

Add a `docs/README.{language-code}.md` file (e.g., `docs/README.fr.md` for French) following the structure of the existing `docs/README.md`, and add it to the `include:` list in `docs/_config.yml`. Translations live only under `docs/` (they power the website at felipe-venturini.github.io/mind-plus-plus); the repo root keeps only the English `README.md`. Then open a PR.

### Contribute a new skill

New skills should follow the format in existing `skills/**/SKILL.md` files.
Skills are grouped by domain, one subfolder per domain (today everything is
cross-cutting and lives under `skills/core/`):

```
skills/
  <domain>/            ← e.g. core (shared), or a future domain like finance
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
skill's folder path explicitly (e.g. `"./skills/core/your-skill-name/"`).
Listing the folder directly makes the `name:` frontmatter the authoritative
invocation name, and the default `skills/` scan no longer reaches into the
domain subfolders. An unlisted skill is silently not loaded.

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
├── skills/                      # Grouped by domain (one subfolder per domain)
│   └── core/                    # Cross-cutting skills — the shared interaction layer
│       ├── setup-mind-plus-plus/
│       ├── user-profile/
│       ├── new-meeting/
│       ├── meeting-prep/
│       ├── capture-idea/
│       ├── new-decision/
│       ├── knowledge-search/
│       ├── stakeholder-update/
│       ├── daily-brief/
│       ├── weekly-review/
│       ├── process-inbox/
│       ├── process-meeting-emails/
│       │   ├── SKILL.md
│       │   └── references/      # (optional)
│       └── specialist/          # Orchestrator: routes requests to specialist agents
├── agents/                      # Grouped by domain (one subfolder per domain)
│   ├── core/                    # Cross-cutting agents, not tied to a business domain
│   │   ├── vault-researcher.md  # Deep multi-file research (invoked by knowledge-search)
│   │   ├── vault-auditor.md     # Scheduled or on-demand vault health check
│   │   └── specialist-judge.md  # Universal arbiter for the `specialist` skill
│   └── marketing/               # `marketing` domain
│       └── bi/                  # BI discipline (agents discovered by `domain` frontmatter)
│           ├── data-analyst.md
│           ├── media-analytics.md
│           ├── data-engineer.md
│           └── insights.md
├── scripts/
│   └── validate_plugin.py       # Checks every skill/agent is registered in plugin.json
├── .github/
│   ├── workflows/               # CI (runs the validator on push/PR)
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

Both `skills/` and `agents/` are grouped on disk by **domain** — one subfolder
per domain — so the plugin reads as a single, coherent unit:

- **`skills/`** is the shared interaction layer. Skills are cross-cutting by
  nature, so today they all live under `skills/core/`. A future domain-specific
  skill would get its own subfolder (e.g. `skills/finance/`).
- **`agents/`** is where the domain axis is actually populated — specialists
  live under the domain they serve:
  - `agents/core/` — cross-cutting agents that serve the whole vault and belong
    to no business domain (e.g. `vault-researcher`, `vault-auditor`).
  - `agents/marketing/` — the `marketing` domain. Today it holds the `bi`
    discipline specialists under `agents/marketing/bi/`. Future domains (e.g.
    `finance`, `personal`) and disciplines get their own nested subfolder.

The `specialist` skill (in `skills/core/`) is the bridge: it discovers the
domain's specialists, then hands routing and arbitration to the universal
`specialist-judge` agent (`agents/core/specialist-judge.md`) — which triages the
minimal set of specialists to run and reconciles their reports — while the skill
itself is the only component that dispatches agents and writes to the vault.

**Naming convention** for domain specialists: files live at
`agents/<domain>/<discipline>/<role>.md`, and the `name:` frontmatter is the
fully-qualified `<domain>-<discipline>-<role>` (e.g. `marketing-bi-data-analyst`).
The `name:` field — not the filename or folder — is what Claude Code and the
`specialist` skill dispatch on, so keep `name:` stable: renaming it silently breaks
every reference. Routing keys off the `domain:` frontmatter field: you invoke
`/specialist <domain> …` and the judge triages disciplines and roles.

**Domain slugs** (reference for future expansion; only `marketing` is populated
today): `marketing`, `tech`, `finance`, `hr`, `dp`, `legal`, `admin`. Create a
domain's folder and agents on demand — do not scaffold empty domains.

**Adding a new agent — two steps:**

1. Drop the `.md` file at `agents/<domain>/<discipline>/<role>.md` with a
   fully-qualified `name:` and both `domain: <domain>` and `discipline:
   <discipline>` frontmatter fields — the `specialist` skill discovers it by
   `domain` with a recursive `grep`, so no skill edit is needed.
2. **Register its path in `.claude-plugin/plugin.json` under `"agents"`.** This
   field *replaces* the default `agents/` scan, so every agent must be listed
   there explicitly; an unlisted file is silently not loaded by the plugin.

---

## Questions?

Open an issue and tag it `question`. We're happy to help.
