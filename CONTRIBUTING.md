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

Add a `README.{language-code}.md` file (e.g., `README.fr.md` for French) following the structure of the existing `README.md`. Then open a PR.

### Contribute a new skill

New skills should follow the format in existing `skills/*/SKILL.md` files:

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
├── skills/
│   ├── setup/
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
│   └── process-meeting-emails/
│       ├── SKILL.md
│       └── references/          # (optional)
├── agents/
│   ├── vault-researcher.md      # Deep multi-file research (invoked by knowledge-search)
│   └── vault-auditor.md         # Scheduled or on-demand vault health check
├── CONNECTORS.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── README.pt-BR.md
└── README.es.md
```

---

## Questions?

Open an issue and tag it `question`. We're happy to help.
