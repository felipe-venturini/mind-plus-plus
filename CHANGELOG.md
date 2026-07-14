# Changelog

All notable changes to Mind++ for Claude are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.5] - 2026-07-14

### Fixed

- **Agent description token limit resolved.** Removed `<example>` blocks from the
  `description` YAML field of all 68 agents — examples belong in the agent body
  (system prompt), not in the dispatch-trigger field. Total description tokens
  dropped from 17,817 to 5,682 (62% reduction), clearing the 15,000-token limit
  that produced the `Agent descriptions are over the 15.0k-token limit` warning in
  Claude Code.
- **`model` field added to all 68 agents.** Without it, agents inherited the
  session model (typically Opus — expensive for read-only vault work). 67 agents
  now declare `model: haiku`; `core__specialist_judge` declares `model: sonnet`
  because it performs cross-report synthesis and judgment.

### Changed

- **Installation docs: Claude Code CLI path added.** The README (root + `docs/`,
  all 12 language versions) now documents two installation paths side by side:
  - **Desktop app** (drag-and-drop `.plugin` file via Claude → Settings → Plugins)
  - **Claude Code CLI** (`claude plugins marketplace add` + `claude plugins install
    mind-plus-plus@felipe-venturini`)
- **"Claude Cowork" branding removed throughout.** Every file that referenced
  "Claude Cowork" (an unofficial name) has been updated to "Claude" or
  "Claude desktop app" as appropriate. Affected files: all 12 README variants,
  `CONTRIBUTING.md`, `SECURITY.md`, `CONNECTORS.md`, `docs/_config.yml`,
  `.github/ISSUE_TEMPLATE/bug_report.md`, and
  `skills/setup-mind-plus-plus/SKILL.md`.

## [1.2.4] - 2026-07-02

### Fixed

- **Plugin now passes `claude plugin validate --strict`.** Removed the non-schema
  `contributors` field from `plugin.json` — the plugin manifest schema does not
  define it, so strict validation (used when adding the repo as a marketplace in
  the Claude app) failed with "Falha ao criar marketplace." Co-author credit for
  sioux1to1 remains in the README and CHANGELOG.
- **Marketplace manifest** (`.claude-plugin/marketplace.json`, added this cycle)
  renamed to `felipe-venturini` so the marketplace name is distinct from the
  `mind-plus-plus` plugin name; install id is `mind-plus-plus@felipe-venturini`.

## [1.2.3] - 2026-07-02

### Changed

- **Skills are now flat under `skills/`** — each skill folder moved from
  `skills/core/<name>/` to `skills/<name>/`, mirroring the flat `agents/` layout.
  The `plugin.json` skill paths were updated accordingly; each skill's `name:`
  frontmatter (the invocation key) is unchanged.

### Removed

- **`scripts/validate_plugin.py` and the `Validate plugin` CI workflow** — the
  plugin validator and its GitHub Actions job were removed, along with the
  references in the PR template and `CONTRIBUTING.md`. The `scripts/` directory is
  no longer part of the repository.

## [1.2.2] - 2026-07-02

### Changed

- **Agent files are now flat in `agents/`**, named
  `{domain}__{discipline}__{role}` — double underscore between hierarchy levels,
  single underscore within a name (à la BI/database naming, e.g.
  `marketing__bi__data_analyst.md`). The nested
  `agents/{domain}/{discipline}/{role}.md` layout is gone.
- **`plugin.json` no longer lists `agents`** — agents are auto-discovered from the
  flat `agents/` directory. Agent `name:` frontmatter (the dispatch key) and
  domain-based routing are unchanged; only file locations/names changed.

### Fixed

- **Plugin upload** — the Claude plugin uploader treats `agents` manifest entries
  as directories and rejected explicit file paths ("No agent files found in
  specified directories"). Auto-discovery is non-recursive, so agents are now flat
  in `agents/`, which lets the uploader find all 68.

## [1.2.1] - 2026-07-02

> First published build of this work. The `1.2.0` tag was retired under GitHub
> immutable releases before its plugin bundle could be attached, so `1.2.1` ships
> the same changes plus the packaging fix below.

### Added

- **`specialist` orchestrator skill** — the single entry point to Mind++'s
  specialist agents. You invoke it by **domain** (`/specialist marketing ...`,
  `/specialist finance ...`) or through natural-language phrases such as "qual o
  ROAS/ROI de ...". It loads the relevant vault history, hands routing and
  arbitration to the universal judge, dispatches the selected read-only
  specialists, and is the only component that writes to the vault — always after
  the user confirms.
- **`specialist-judge` universal agent** (`agents/core/specialist-judge.md`) — a
  single, discipline-agnostic arbiter that serves every specialist. It runs in
  two modes:
  - **Triage** — selects the minimal set of specialists a request actually needs
    (never all of them by default), matching on each specialist's description.
  - **Arbitration** — reconciles the specialists' reports, surfaces divergent
    numbers instead of silently merging them, and rules on each open doubt:
    bounce it back to a specialist (capped at 2 rounds), escalate it to the user,
    or record it as a gap. User questions are batched into a single prompt with
    suggested answers. Read-only: it decides; the skill executes its rulings.
- **Specialists now surface open doubts** — every specialist report includes a
  "Dúvidas em aberto" section and accepts a targeted judge follow-up, which is
  what feeds the arbitration loop.
- **Full org-chart specialist roster — 65 read-only specialists across seven
  business domains** (all analyze-and-propose, never write), plus the 3
  cross-cutting `core` agents (68 agents total):
  - `marketing` (35 specialists): `bi`, `media`, `seo`, `social`, `planning`,
    `client-services`, `creative`, `production`, `ops`.
  - `tech` (8): `engineering`, `infrastructure`.
  - `finance` (5): `controllership`, `operations`.
  - `hr` (5): `people`.
  - `dp` (4): `personnel` (Departamento Pessoal).
  - `legal` (5): `advisory`, `compliance` (LGPD/DPO).
  - `admin` (3): `facilities`.

### Changed

- **Routing is by `domain`, and agents live at
  `agents/{domain}/{discipline}/{role}.md`.** The `/specialist` argument is the
  domain; discovery greps the `domain:` frontmatter field and the judge triages
  the disciplines and roles within it. The `discipline:` field is now grouping
  metadata, not the routing key. Agent `name:` fields stay fully-qualified
  (`{domain}-{discipline}-{role}`) and remain the authoritative dispatch key.
- Reorganized both `skills/` and `agents/` by **domain** for a single, coherent
  plugin layout:
  - `agents/core/` for cross-cutting agents (`vault-researcher`, `vault-auditor`,
    `specialist-judge`); business specialists nested under
    `agents/{domain}/{discipline}/`.
  - All 13 skills moved under `skills/core/` (the shared interaction layer);
    future domain-specific skills get their own subfolder.
  - Skill and agent paths are declared explicitly in `plugin.json` under
    `"skills"` and `"agents"`, which makes `name:` authoritative and is robust to
    nesting.
  - The `agents/{domain}/{discipline}/{role}.md` convention and the registration
    rule are documented in `CONTRIBUTING.md`.
- Deduplicated the per-language READMEs by moving them to `docs/` (the translated
  copies are no longer kept at the repository root).
- Documented the specialist skill, the judge, and the full agent roster in the
  README and `docs/`.
- Added open-source community-health files: `CODE_OF_CONDUCT.md` (Contributor
  Covenant 2.1), `SECURITY.md`, GitHub issue templates (bug, feature, new
  skill/agent, translation) and a pull-request template under `.github/`.

### Fixed

- **Packaging** — the release now ships a proper `mind-plus-plus.plugin` bundle (a
  zip of `.claude-plugin/`, `agents/`, and `skills/`) as a downloadable asset, so the
  Claude plugin uploader receives all 68 nested agent files.

### Internal

- Added `scripts/validate_plugin.py` and a GitHub Actions workflow
  (`.github/workflows/validate-plugin.yml`) that fail when a skill or agent is
  not registered in `plugin.json`, missing on disk, or missing a `name:` field.
- Moved internal planning artifacts out of `docs/` to a top-level `.planning/`
  (still git-ignored) so they can never leak into the GitHub Pages site.

## [1.1.0] - 2026-04-15

### Changed

- **BREAKING:** Renamed the `setup` skill to `setup-mind-plus-plus`. The
  original name was too generic and risked trigger collisions with other
  plugins. The slash command is now `/setup-mind-plus-plus`; natural-language
  phrases like "set up my second brain" continue to trigger it. All README
  tables (11 languages, root and `docs/`), `CONNECTORS.md`, and the
  `user-profile` skill reference were updated, and `plugin.json` bumped to
  1.1.0.

## [1.0.0] - 2026-04-15

### Added

- Initial release of Mind++ for Claude — a second brain that captures meetings,
  tracks commitments, delivers daily briefs, and maintains a living knowledge
  base.
- Multi-language README, GitHub Pages, and canonical GitHub Wiki source
  (Home, Installation Guide, FAQ, Sync Strategies).

[1.2.5]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.2.4...v1.2.5
[1.2.4]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.2.3...v1.2.4
[1.2.3]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.2.2...v1.2.3
[1.2.2]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.2.1...v1.2.2
[1.2.1]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.1.0...v1.2.1
[1.1.0]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/felipe-venturini/mind-plus-plus/releases/tag/v1.0.0
