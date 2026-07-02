#!/usr/bin/env python3
"""Validate the Mind++ plugin manifest against the files on disk.

Run locally before opening a PR:

    python3 scripts/validate_plugin.py

Model (as of v1.2.2):
  - **Skills** are listed explicitly in plugin.json under "skills" (directory
    paths, each containing a SKILL.md).
  - **Agents** are auto-discovered by Claude Code from the top level of `agents/`
    (`agents/*.md`). The plugin.json does NOT list agents, because the Claude
    plugin uploader treats "agents" entries as directories and rejects file paths.
    Default discovery is NOT recursive, so every agent file must live flat in
    `agents/` — nested files would be silently ignored.

Checks:
  1. .claude-plugin/plugin.json is valid JSON.
  2. Every path listed under "skills" exists on disk and declares a `name:` field.
  3. Every skill folder (skills/**/SKILL.md) is registered under "skills".
  4. No agent .md file is nested below `agents/` (default discovery is flat/
     non-recursive — a nested agent would not load).
  5. Every top-level agent file (`agents/*.md`) declares a `name:` frontmatter
     field, and all agent names are unique.
"""
from __future__ import annotations

import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, ".claude-plugin", "plugin.json")


def frontmatter_name(path: str) -> str | None:
    """Return the `name:` value from a markdown file's YAML frontmatter, or None."""
    with open(path, encoding="utf-8") as fh:
        in_frontmatter = False
        for i, line in enumerate(fh):
            if i == 0 and line.strip() != "---":
                return None
            if line.strip() == "---":
                if in_frontmatter:
                    return None  # closed frontmatter without a name
                in_frontmatter = True
                continue
            if in_frontmatter and line.startswith("name:"):
                return line.split(":", 1)[1].strip()
    return None


def main() -> int:
    problems: list[str] = []

    os.chdir(ROOT)

    try:
        with open(MANIFEST, encoding="utf-8") as fh:
            manifest = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"plugin.json is not valid JSON: {exc}")
        return 1

    skills = manifest.get("skills", [])

    # 2 + 3: registered skill paths exist, declare name:, and every skill on disk
    # is registered.
    listed_skill_dirs = set()
    for p in skills:
        d = p.strip("./").rstrip("/")
        listed_skill_dirs.add(d)
        skill_md = os.path.join(d, "SKILL.md")
        if not os.path.isfile(skill_md):
            problems.append(f"registered skill has no SKILL.md: {p}")
        elif frontmatter_name(skill_md) is None:
            problems.append(f"skill missing `name:` frontmatter: {skill_md}")

    for skill_md in glob.glob("skills/**/SKILL.md", recursive=True):
        d = os.path.dirname(skill_md)
        if d not in listed_skill_dirs:
            problems.append(f"UNREGISTERED skill (add to plugin.json \"skills\"): {d}")

    # Agents are auto-discovered from the flat top level of agents/.
    # 4: nothing nested (default discovery is non-recursive).
    nested = [
        f for f in glob.glob("agents/**/*.md", recursive=True)
        if os.path.dirname(f) != "agents"
    ]
    for f in sorted(nested):
        problems.append(
            f"NESTED agent will not be discovered (must be flat in agents/): {f}"
        )

    # 5: every flat agent declares name:, and names are unique.
    seen_names: dict[str, str] = {}
    flat_agents = sorted(glob.glob("agents/*.md"))
    for f in flat_agents:
        name = frontmatter_name(f)
        if name is None:
            problems.append(f"agent missing `name:` frontmatter: {f}")
            continue
        if name in seen_names:
            problems.append(
                f"duplicate agent name `{name}`: {f} and {seen_names[name]}"
            )
        else:
            seen_names[name] = f

    if problems:
        print("Plugin validation FAILED:\n")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(
        f"Plugin validation OK: {len(skills)} skills registered + "
        f"{len(flat_agents)} agents auto-discovered (flat), all named and unique."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
