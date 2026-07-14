# Agent Descriptions Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the 15k-token limit error and align all 68 agents with Claude Code best practices by stripping `<example>` blocks from descriptions and adding the `model` field.

**Architecture:** A Python script (`scripts/fix_agent_descriptions.py`) applies two text-level transformations to each agent's YAML frontmatter — stripping `<example>` blocks via regex and inserting a `model` field — while leaving bodies and all other fields untouched. Tests cover each transformation function and the end-to-end file processing. Script runs from the repo root.

**Tech Stack:** Python 3 (stdlib only: `re`, `glob`, `yaml`, `pathlib`), pytest

**Spec:** `docs/superpowers/specs/2026-07-13-agent-descriptions-review-design.md`

---

## File Map

| Action | Path | Responsibility |
|---|---|---|
| Create | `scripts/fix_agent_descriptions.py` | Transformation logic + CLI runner |
| Create | `scripts/test_fix_agent_descriptions.py` | Unit + integration tests |
| Modify | `agents/*.md` (68 files) | Strip examples, add `model` field |

---

### Task 1: Write failing tests

**Files:**
- Create: `scripts/test_fix_agent_descriptions.py`

- [ ] **Step 1.1: Create the test file**

```python
# scripts/test_fix_agent_descriptions.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

import pytest
from fix_agent_descriptions import strip_examples_from_text, add_model_field_to_text, process_file

SAMPLE_FM_WITH_EXAMPLES = '''\
name: test-agent
description: |
  Use this agent for testing. Dispatched by the test skill. Read-only.

  <example>
  Context: User asks for something.
  assistant: "Dispatching test-agent..."
  <commentary>
  This shows the agent in use.
  </commentary>
  </example>

  <example>
  Context: Another scenario.
  assistant: "Using test-agent again..."
  </example>
tools: Read, Glob, Grep
'''

SAMPLE_FM_NO_EXAMPLES = '''\
name: test-agent
description: |
  Use this agent for testing. Dispatched by the test skill. Read-only.
tools: Read, Glob, Grep
'''

SAMPLE_BODY = '\nYou are `test-agent` — a read-only test specialist.\n\n## Your job\n\nDo tests.\n'


class TestStripExamples:
    def test_removes_example_blocks(self):
        result = strip_examples_from_text(SAMPLE_FM_WITH_EXAMPLES)
        assert '<example>' not in result
        assert '</example>' not in result

    def test_preserves_first_paragraph(self):
        result = strip_examples_from_text(SAMPLE_FM_WITH_EXAMPLES)
        assert 'Use this agent for testing.' in result

    def test_preserves_other_fields(self):
        result = strip_examples_from_text(SAMPLE_FM_WITH_EXAMPLES)
        assert 'tools: Read, Glob, Grep' in result
        assert 'name: test-agent' in result

    def test_idempotent(self):
        once = strip_examples_from_text(SAMPLE_FM_WITH_EXAMPLES)
        twice = strip_examples_from_text(once)
        assert once == twice

    def test_no_op_when_no_examples(self):
        result = strip_examples_from_text(SAMPLE_FM_NO_EXAMPLES)
        assert result == SAMPLE_FM_NO_EXAMPLES


class TestAddModelField:
    def test_adds_haiku(self):
        result = add_model_field_to_text(SAMPLE_FM_NO_EXAMPLES, 'haiku')
        assert 'model: haiku' in result

    def test_adds_sonnet(self):
        result = add_model_field_to_text(SAMPLE_FM_NO_EXAMPLES, 'sonnet')
        assert 'model: sonnet' in result

    def test_does_not_duplicate_existing_field(self):
        fm = SAMPLE_FM_NO_EXAMPLES + 'model: haiku\n'
        result = add_model_field_to_text(fm, 'haiku')
        assert result.count('model:') == 1

    def test_does_not_override_existing_model(self):
        fm = SAMPLE_FM_NO_EXAMPLES + 'model: opus\n'
        result = add_model_field_to_text(fm, 'haiku')
        assert 'model: opus' in result
        assert 'model: haiku' not in result


class TestProcessFile:
    def _make_content(self, fm=SAMPLE_FM_WITH_EXAMPLES, body=SAMPLE_BODY):
        return f'---\n{fm}---\n{body}'

    def test_specialist_judge_gets_sonnet(self):
        content = self._make_content()
        result = process_file(content, 'core__specialist_judge.md')
        fm_section = result.split('---\n')[1]
        assert 'model: sonnet' in fm_section

    def test_regular_agent_gets_haiku(self):
        content = self._make_content()
        result = process_file(content, 'marketing__creative__copywriter.md')
        fm_section = result.split('---\n')[1]
        assert 'model: haiku' in fm_section

    def test_removes_examples_from_frontmatter(self):
        content = self._make_content()
        result = process_file(content, 'test-agent.md')
        fm_section = result.split('---\n')[1]
        assert '<example>' not in fm_section

    def test_preserves_body_verbatim(self):
        content = self._make_content()
        result = process_file(content, 'test-agent.md')
        assert SAMPLE_BODY in result

    def test_output_starts_with_frontmatter_delimiter(self):
        content = self._make_content()
        result = process_file(content, 'test-agent.md')
        assert result.startswith('---\n')

    def test_returns_unchanged_if_no_frontmatter(self):
        content = 'No frontmatter here.'
        result = process_file(content, 'test-agent.md')
        assert result == content
```

- [ ] **Step 1.2: Run tests to confirm they all fail (module not found)**

```bash
cd /Users/felipeventurini/GitHub/felipe-venturini/mind-plus-plus
python3 -m pytest scripts/test_fix_agent_descriptions.py -v 2>&1 | head -30
```

Expected: `ModuleNotFoundError: No module named 'fix_agent_descriptions'`

---

### Task 2: Implement the transformation script

**Files:**
- Create: `scripts/fix_agent_descriptions.py`

- [ ] **Step 2.1: Create the script**

```python
#!/usr/bin/env python3
"""Fix agent descriptions: strip <example> blocks and add model field.

Usage:
  python3 scripts/fix_agent_descriptions.py [--dry-run]
"""

import re
import sys
import glob
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
```

- [ ] **Step 2.2: Run the tests — all should pass**

```bash
cd /Users/felipeventurini/GitHub/felipe-venturini/mind-plus-plus
python3 -m pytest scripts/test_fix_agent_descriptions.py -v
```

Expected output:
```
PASSED scripts/test_fix_agent_descriptions.py::TestStripExamples::test_removes_example_blocks
PASSED scripts/test_fix_agent_descriptions.py::TestStripExamples::test_preserves_first_paragraph
PASSED scripts/test_fix_agent_descriptions.py::TestStripExamples::test_preserves_other_fields
PASSED scripts/test_fix_agent_descriptions.py::TestStripExamples::test_idempotent
PASSED scripts/test_fix_agent_descriptions.py::TestStripExamples::test_no_op_when_no_examples
PASSED scripts/test_fix_agent_descriptions.py::TestAddModelField::test_adds_haiku
PASSED scripts/test_fix_agent_descriptions.py::TestAddModelField::test_adds_sonnet
PASSED scripts/test_fix_agent_descriptions.py::TestAddModelField::test_does_not_duplicate_existing_field
PASSED scripts/test_fix_agent_descriptions.py::TestAddModelField::test_does_not_override_existing_model
PASSED scripts/test_fix_agent_descriptions.py::TestProcessFile::test_specialist_judge_gets_sonnet
PASSED scripts/test_fix_agent_descriptions.py::TestProcessFile::test_regular_agent_gets_haiku
PASSED scripts/test_fix_agent_descriptions.py::TestProcessFile::test_removes_examples_from_frontmatter
PASSED scripts/test_fix_agent_descriptions.py::TestProcessFile::test_preserves_body_verbatim
PASSED scripts/test_fix_agent_descriptions.py::TestProcessFile::test_output_starts_with_frontmatter_delimiter
PASSED scripts/test_fix_agent_descriptions.py::TestProcessFile::test_returns_unchanged_if_no_frontmatter
15 passed in 0.XXs
```

- [ ] **Step 2.3: Commit the script and tests**

```bash
git add scripts/fix_agent_descriptions.py scripts/test_fix_agent_descriptions.py
git commit -m "feat(scripts): add fix_agent_descriptions script with tests"
```

---

### Task 3: Dry-run validation

**Files:**
- Read: `agents/*.md` (no writes yet)

- [ ] **Step 3.1: Run in dry-run mode**

```bash
cd /Users/felipeventurini/GitHub/felipe-venturini/mind-plus-plus
python3 scripts/fix_agent_descriptions.py --dry-run
```

Expected output (abridged):
```
Agents found: 68
Estimated description tokens before: 17790
  [dry-run] Would update: admin__facilities__manager.md
  [dry-run] Would update: admin__facilities__office_manager.md
  ...
  [dry-run] Would update: tech__infrastructure__infra_manager.md
Files changed: 68/68
```

If `Files changed: 0/68`, stop — investigate why no files are matching. Run:
```bash
python3 -c "
content = open('agents/core__vault_auditor.md').read()
print(repr(content[:100]))
"
```
and compare against the expected `---\nname: ...` format.

---

### Task 4: Apply changes and validate

**Files:**
- Modify: `agents/*.md` (68 files)

- [ ] **Step 4.1: Apply all changes**

```bash
cd /Users/felipeventurini/GitHub/felipe-venturini/mind-plus-plus
python3 scripts/fix_agent_descriptions.py
```

Expected output:
```
Agents found: 68
Estimated description tokens before: 17790
  Updated: admin__facilities__manager.md
  ...
  Updated: tech__infrastructure__infra_manager.md

Estimated description tokens after:  5XXX
Reduction:                           12XXX
Within 15k-token limit:              YES
Files changed: 68/68
```

If `Within 15k-token limit: NO`, stop. Run:
```bash
python3 -c "
import yaml, glob
files = sorted(glob.glob('agents/*.md'))
total = 0
for f in files:
    parts = open(f).read().split('---', 2)
    fm = yaml.safe_load(parts[1])
    desc = fm.get('description','') or ''
    tokens = len(desc)//4
    if tokens > 150:
        print(f'{tokens:4d}  {f}')
    total += tokens
print(f'TOTAL: {total//4} tokens')
"
```
Fix any outliers manually before continuing.

- [ ] **Step 4.2: Validate YAML is still valid for all files**

```bash
python3 -c "
import yaml, glob, sys
errors = []
for f in sorted(glob.glob('agents/*.md')):
    parts = open(f).read().split('---', 2)
    if len(parts) < 3:
        errors.append(f'{f}: missing frontmatter delimiters')
        continue
    try:
        fm = yaml.safe_load(parts[1])
        assert fm.get('name'), f'missing name'
        assert fm.get('description'), f'missing description'
        assert fm.get('model'), f'missing model'
    except Exception as e:
        errors.append(f'{f}: {e}')
if errors:
    print('ERRORS:')
    for e in errors: print(f'  {e}')
    sys.exit(1)
else:
    print(f'All {len(list(glob.glob(\"agents/*.md\")))} files valid.')
"
```

Expected: `All 68 files valid.`

- [ ] **Step 4.3: Spot-check specialist_judge has sonnet**

```bash
python3 -c "
import yaml
content = open('agents/core__specialist_judge.md').read()
fm = yaml.safe_load(content.split('---', 2)[1])
print('model:', fm.get('model'))
print('description excerpt:', fm['description'][:100])
assert fm['model'] == 'sonnet', 'Expected sonnet for specialist_judge'
assert '<example>' not in fm['description'], 'Examples not stripped'
print('specialist_judge: OK')
"
```

Expected:
```
model: sonnet
description excerpt: Use this agent as an independent judge ...
specialist_judge: OK
```

- [ ] **Step 4.4: Spot-check a regular agent has haiku**

```bash
python3 -c "
import yaml
content = open('agents/marketing__creative__copywriter.md').read()
fm = yaml.safe_load(content.split('---', 2)[1])
print('model:', fm.get('model'))
assert fm['model'] == 'haiku', 'Expected haiku'
assert '<example>' not in fm['description'], 'Examples not stripped'
print('copywriter: OK')
"
```

Expected:
```
model: haiku
copywriter: OK
```

- [ ] **Step 4.5: Confirm body of one agent is unchanged**

Pick any agent and verify the body (after `---`) matches the original body from git:

```bash
git diff agents/core__vault_auditor.md | grep '^[+-]' | grep -v '^---' | grep -v '^+++' | head -30
```

Expected: Only `description:` block and new `model:` line appear in the diff. Body lines should be unchanged.

---

### Task 5: Commit changes

- [ ] **Step 5.1: Run tests one final time to confirm nothing broke**

```bash
python3 -m pytest scripts/test_fix_agent_descriptions.py -v
```

Expected: `15 passed`

- [ ] **Step 5.2: Stage and commit agent changes**

```bash
git add agents/
git commit -m "$(cat <<'EOF'
fix(agents): strip examples from descriptions, add model field

Reduces combined description tokens from ~17790 to ~5700, resolving
the 15k-token limit warning in Claude Code. Adds model: haiku to
all 67 read-only vault agents and model: sonnet to specialist_judge.

Follows official Claude Code best practices: descriptions are dispatch
triggers only (1-2 sentences); <example> blocks belong in the body.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 5.3: Verify final state**

```bash
git log --oneline -3
git diff HEAD~1 --stat
```

Expected:
```
<hash> fix(agents): strip examples from descriptions, add model field
...
 68 files changed, ...
```

---

## Post-Implementation

After merging to main, the plugin must be re-published and re-installed for the cached marketplace files to reflect the changes:

```bash
# Bump version in mind-plus-plus.plugin if needed, then:
# Re-install the plugin via the marketplace
```

The warning `Agent descriptions are over the 15.0k-token limit` should no longer appear when the updated plugin is loaded.
