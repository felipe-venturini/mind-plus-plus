# Design: Agent Descriptions Review & Best Practices Alignment

**Date:** 2026-07-13
**Status:** Approved
**Scope:** All 68 agents in `agents/`

---

## Problem

Claude Code enforces a 15,000-token limit on the combined `description` fields of all loaded agents. With 68 agents, the current total reaches **17,790 tokens** — 2,790 over the limit — causing the warning:

> `Agent descriptions are over the 15.0k-token limit`

Root cause: every agent embeds two `<example>` blocks inside its `description` YAML field. These examples were written for human readability but are not recommended by Anthropic's official documentation for the description field — they belong in the system prompt body.

---

## Best Practices Reference (Official Docs)

From `code.claude.com/docs/en/sub-agents` and `platform.claude.com/docs/en/build-with-claude/prompt-engineering`:

### `description` field
- Used **exclusively** for dispatch: Claude reads it to decide when to delegate
- Should be **1–2 sentences** — a precise trigger statement
- Official example: `"Expert code reviewer. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code."`
- `<example>` blocks are **not recommended** here; they inflate dispatch tokens without improving routing accuracy
- Include `"Use proactively"` for agents that should be auto-dispatched without explicit user request

### `model` field
- Omitting it causes agents to inherit the session model (typically Opus — expensive)
- Official recommendation: *"Control costs by routing tasks to faster, cheaper models like Haiku"*
- Read-only vault agents (the majority) are well-suited to Haiku — they read markdown files and return structured text reports, requiring no reasoning beyond retrieval and synthesis

### `tools` field
- Principle of least privilege: grant only tools the agent actually uses
- Current state is correct: `Read, Glob, Grep` for all read-only agents

### System prompt body
- Role statement, numbered workflow, output format template, "What NOT to do", completion signal
- `<example>` tags are recommended **here** to guide output format and tone
- Current bodies are well-structured and compliant — no changes needed

---

## Solution

Three changes, in priority order:

### Change 1 — Strip `<example>` blocks from all `description` fields (required)

Remove the two `<example>` blocks from every agent's description YAML field. Keep the first paragraph verbatim — it is already a precise, well-written dispatch trigger.

**Result:** 17,790 → ~5,700 tokens (~68% reduction, 9,300-token safety margin)

No dispatch quality is lost: the first paragraph already contains the "Use this agent when..." statement, the domain/discipline routing info, and key behavioral signals (read-only, proactive, etc.).

### Change 2 — Add `model` field to all agents (recommended)

- **66 agents** (all read-only specialists, vault agents, and support roles): `model: haiku`
- **2 agents** that perform cross-source synthesis or judgment:
  - `core__specialist_judge` → `model: sonnet` (compares multiple reports, needs better reasoning)
  - `core__vault_researcher` → `model: haiku` (read-only retrieval, still fine)

Rationale: Haiku is sufficient for tasks that read markdown files and produce structured reports following a defined template. The body already constrains the output format precisely, removing the need for stronger models.

### Change 3 — Strengthen dispatch triggers in descriptions (nice-to-have)

For self-dispatched agents (not routed by the `specialist` skill), add a "Use proactively" signal or explicit trigger phrases where missing. Affects primarily:
- `core__vault-auditor` — already has good triggers
- `core__vault-researcher` — dispatched by `specialist` skill; no change needed

This change is low priority and can be done opportunistically during Change 1.

---

## What Does NOT Change

- **Bodies (system prompts):** Well-structured, follow all best practices. No edits.
- **`tools` fields:** Correctly scoped. No edits.
- **`domain` / `discipline` fields:** Custom routing metadata for the `specialist` skill. No edits.
- **`name` fields:** No edits.

---

## File Scope

All 68 files in `agents/`:

```
admin/  (3 agents)   → model: haiku, strip examples
core/   (3 agents)   → specialist_judge: sonnet; others: haiku
dp/     (4 agents)   → model: haiku, strip examples
finance/ (5 agents)  → model: haiku, strip examples
hr/     (5 agents)   → model: haiku, strip examples
legal/  (5 agents)   → model: haiku, strip examples
marketing/ (27 agents) → model: haiku, strip examples
tech/   (8 agents)   → model: haiku, strip examples
```

---

## Success Criteria

1. Total description tokens ≤ 15,000 (target: ~5,700 with 9,300 margin)
2. No `Agent descriptions are over the 15.0k-token limit` warning
3. Descriptions retain their dispatch trigger clarity — first paragraph unchanged
4. Bodies unchanged
5. `model` field present in all 68 agents
6. All files parseable as valid YAML frontmatter

---

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Removing examples degrades dispatch routing | First paragraph already fully specifies the trigger; examples are redundant for routing |
| Haiku under-performs for complex synthesis | Only `specialist_judge` does multi-source synthesis → kept on `sonnet` |
| YAML parsing errors after edits | Script validates YAML after each change; fails fast |
| Marketplace cache not updated | Plugin must be re-installed after source changes to update the cached files |
