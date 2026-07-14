#!/usr/bin/env python3
"""Fix agent descriptions: strip <example> blocks and add model field.

Usage:
  python3 scripts/fix_agent_descriptions.py [--dry-run]
"""

import re
import sys
import yaml
from pathlib import Path

AGENTS_DIR = Path(__file__).parent.parent / 'agents'
LIMIT_TOKENS = 15_000


def strip_examples_from_text(frontmatter_text: str) -> str:
    """Remove <example>...</example> blocks from YAML frontmatter text."""
    cleaned = re.sub(
        r'\n\s+<example>.*?</example>',
        '',
        frontmatter_text,
        flags=re.DOTALL,
    )
    # Collapse triple+ blank lines left behind
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    return cleaned


def add_model_field_to_text(frontmatter_text: str, model: str) -> str:
    """Append model field if not already present."""
    if re.search(r'^model:', frontmatter_text, re.MULTILINE):
        return frontmatter_text
    return frontmatter_text.rstrip() + f'\nmodel: {model}\n'


def process_file(content: str, filename: str) -> str:
    """Apply transformations to a single agent file's content."""
    if not content.startswith('---\n'):
        return content

    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return content

    _, fm_text, body = parts

    model = 'sonnet' if 'specialist_judge' in filename else 'haiku'
    fm_text = strip_examples_from_text(fm_text)
    fm_text = add_model_field_to_text(fm_text, model)

    return f'---\n{fm_text}---\n{body}'


def count_description_tokens(agents_dir: Path) -> int:
    """Estimate combined token count of all agent descriptions."""
    total_chars = 0
    for filepath in sorted(agents_dir.glob('*.md')):
        content = filepath.read_text()
        parts = content.split('---', 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1])
            desc = fm.get('description', '') or ''
            total_chars += len(desc)
        except yaml.YAMLError:
            continue
    return total_chars // 4


def main(dry_run: bool = False) -> None:
    files = sorted(AGENTS_DIR.glob('*.md'))
    print(f'Agents found: {len(files)}')

    tokens_before = count_description_tokens(AGENTS_DIR)
    print(f'Estimated description tokens before: {tokens_before}')

    changed = 0
    for filepath in files:
        original = filepath.read_text()
        processed = process_file(original, filepath.name)
        if processed != original:
            changed += 1
            if not dry_run:
                filepath.write_text(processed)
                print(f'  Updated: {filepath.name}')
            else:
                print(f'  [dry-run] Would update: {filepath.name}')

    if not dry_run:
        tokens_after = count_description_tokens(AGENTS_DIR)
        print(f'\nEstimated description tokens after:  {tokens_after}')
        print(f'Reduction:                           {tokens_before - tokens_after}')
        within_limit = 'YES' if tokens_after <= LIMIT_TOKENS else 'NO'
        print(f'Within 15k-token limit:              {within_limit}')
    print(f'Files changed: {changed}/{len(files)}')


if __name__ == '__main__':
    main(dry_run='--dry-run' in sys.argv)
