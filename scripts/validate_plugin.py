#!/usr/bin/env python3
"""Validate the Mind++ plugin manifest against the files on disk.

Run locally before opening a PR:

    python3 scripts/validate_plugin.py

Checks:
  1. .claude-plugin/plugin.json is valid JSON.
  2. Every path listed under "skills" / "agents" exists on disk.
  3. Every skill folder (skills/**/SKILL.md) is registered under "skills".
  4. Every agent file (agents/**/*.md) is registered under "agents".
  5. Every SKILL.md and agent file declares a `name:` frontmatter field.

Exits non-zero (and prints each problem) if anything is off — this is what
guards the "unlisted file is silently not loaded" footgun, since the plugin
manifest *replaces* the default scans.
"""
from __future__ import annotations

import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, ".claude-plugin", "plugin.json")


def has_name_field(path: str) -> bool:
    """True if the markdown file has a `name:` line in its YAML frontmatter."""
    with open(path, encoding="utf-8") as fh:
        in_frontmatter = False
        for i, line in enumerate(fh):
            if i == 0 and line.strip() != "---":
                return False
            if line.strip() == "---":
                if in_frontmatter:
                    return False  # closed frontmatter without a name
                in_frontmatter = True
                continue
            if in_frontmatter and line.startswith("name:"):
                return True
    return False


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
    agents = manifest.get("agents", [])

    # 2 + 5: registered skill paths exist and declare name:
    listed_skill_dirs = set()
    for p in skills:
        d = p.strip("./").rstrip("/")
        listed_skill_dirs.add(d)
        skill_md = os.path.join(d, "SKILL.md")
        if not os.path.isfile(skill_md):
            problems.append(f"registered skill has no SKILL.md: {p}")
        elif not has_name_field(skill_md):
            problems.append(f"skill missing `name:` frontmatter: {skill_md}")

    listed_agent_files = set()
    for p in agents:
        f = p.strip("./")
        listed_agent_files.add(f)
        if not os.path.isfile(f):
            problems.append(f"registered agent missing: {p}")
        elif not has_name_field(f):
            problems.append(f"agent missing `name:` frontmatter: {f}")

    # 3: every skill folder on disk is registered
    for skill_md in glob.glob("skills/**/SKILL.md", recursive=True):
        d = os.path.dirname(skill_md)
        if d not in listed_skill_dirs:
            problems.append(f"UNREGISTERED skill (add to plugin.json \"skills\"): {d}")

    # 4: every agent file on disk is registered
    for f in glob.glob("agents/**/*.md", recursive=True):
        if f not in listed_agent_files:
            problems.append(f"UNREGISTERED agent (add to plugin.json \"agents\"): {f}")

    if problems:
        print("Plugin validation FAILED:\n")
        for p in problems:
            print(f"  - {p}")
        return 1

    print(
        f"Plugin validation OK: {len(skills)} skills + {len(agents)} agents "
        "registered, all present, all named."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
