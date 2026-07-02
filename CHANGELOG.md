# Changelog

All notable changes to Mind++ for Claude are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/felipe-venturini/mind-plus-plus/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/felipe-venturini/mind-plus-plus/releases/tag/v1.0.0
