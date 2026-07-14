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

    def test_removes_commentary_inside_examples(self):
        result = strip_examples_from_text(SAMPLE_FM_WITH_EXAMPLES)
        assert 'This shows the agent in use.' not in result


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

    # Routing: process_file keys on 'specialist_judge' substring in filename
    def test_specialist_judge_gets_sonnet(self):
        content = self._make_content()
        result = process_file(content, 'core__specialist_judge.md')
        fm_section = result.split('---\n', 2)[1]
        assert 'model: sonnet' in fm_section

    def test_regular_agent_gets_haiku(self):
        content = self._make_content()
        result = process_file(content, 'marketing__creative__copywriter.md')
        fm_section = result.split('---\n', 2)[1]
        assert 'model: haiku' in fm_section

    def test_removes_examples_from_frontmatter(self):
        content = self._make_content()
        result = process_file(content, 'test-agent.md')
        fm_section = result.split('---\n', 2)[1]
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

    def test_handles_frontmatter_without_description(self):
        fm = 'name: test-agent\ntools: Read, Glob, Grep\n'
        content = f'---\n{fm}---\n{SAMPLE_BODY}'
        # Should not raise, should still add model field
        result = process_file(content, 'test-agent.md')
        assert 'model: haiku' in result.split('---\n', 2)[1]
