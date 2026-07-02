<!-- Thanks for contributing to Mind++! Keep this concise. -->

## What does this PR do?

<!-- One or two sentences. Link any related issue: Closes #123 -->

## Type

- [ ] New skill / agent
- [ ] Change to an existing skill / agent
- [ ] Translation
- [ ] Docs
- [ ] Tooling / CI

## Checklist

- [ ] `python3 scripts/validate_plugin.py` passes (skills & agents registered in `plugin.json`)
- [ ] No personal, company, or client data hardcoded — skills stay generic
- [ ] External tools referenced via `~~category` placeholders (see `CONNECTORS.md`)
- [ ] `name:` frontmatter is set and unchanged for existing skills/agents (renaming breaks references)
- [ ] `CHANGELOG.md` updated under `[Unreleased]` (for user-facing changes)
- [ ] Docs/README updated if behavior or structure changed
