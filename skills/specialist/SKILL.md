---
name: specialist
description: "Routes a request to the right domain specialists and produces a vault-grounded deliverable. The discipline is the first argument. Use when the user says '/specialist bi ...', 'aciona um especialista de BI', 'analisa a performance da campanha ...', 'qual o ROAS/ROI de ...', 'que números temos sobre ...', or asks for data analysis, media performance, data consistency, or a data-driven recommendation. Today the only discipline is `bi` (Business Intelligence)."
arguments: [discipline]
---

# Skill: specialist

## What this skill does

Acts as the single entry point to Mind++'s specialist agents. It captures the
user's request, loads the relevant vault history, discovers the specialist
agents for the requested discipline, dispatches the right ones in parallel,
synthesizes their (read-only) reports into one answer, and writes a deliverable
to the vault **only after the user confirms**.

Specialists analyze and propose; **this skill is what writes.**

---

## Step 1 — Determine the discipline

The discipline is the first argument (`$discipline` / `$0`), e.g. `bi`.

- If provided (`/specialist bi ...`), use it.
- If absent, infer it from the request (BI signals: metrics, performance, ROI,
  ROAS, "que números", data, dashboard, attribution).
- If still ambiguous, ask one short question naming the available disciplines.

> Invocation note: use `/specialist bi ...` (space, discipline as argument).
> Do **not** use `/specialist:bi` — the colon is reserved for plugin namespaces.
> For fully-qualified invocation use `/mind-plus-plus:specialist bi <pedido>`.

---

## Step 2 — Parse the request

Extract:
1. **Subject** — client, product, or topic.
2. **Intent** — exploratory question, media performance, data consistency, or
   recommendation/narrative.
3. **Time scope** — recent, all time, a specific period.

If the subject is vague ("a campanha"), ask one clarifying question before
dispatching.

---

## Step 3 — Load relevant vault history

Before dispatching, gather the context the specialists need (reuse
`knowledge-search` scoping logic):

| Subject type | Folders to load |
|---|---|
| A specific client | `clients/{slug}/` — dashboard, recent `meetings/`, `decisions/`, `references/` |
| A specific product | `products/{slug}/` — same subfolders |
| No entity (portfolio/internal) | relevant `operational/` notes |

Collect candidate file paths (cap ~15, newest first). Never read
`.auto-memory/` unless the request is about the user themselves.

---

## Step 4 — Discover the discipline's agents

List `agents/` and select agents whose frontmatter contains
`discipline: {discipline}`. Do **not** parse agent names — filter on the
`discipline` field.

```bash
grep -rl '^discipline: {discipline}$' agents/
```

If none match, tell the user no specialists exist for that discipline yet and
stop.

Currently, for the `bi` discipline, discovery returns:
- `marketing-bi-data-analyst` — exploratory analysis, comparisons, "why"
- `marketing-bi-media-analytics` — ROI/ROAS, CPA, CTR, channels, attribution
- `marketing-bi-data-engineer` — provenance, reconciliation, metric definitions
- `marketing-bi-insights` — narrative and recommendation

---

## Step 5 — Route by intent

Route by matching the request's intent to each discovered agent's own
`description` field — every agent's description states what that specialist is
for. Select all agents whose focus matches the request; when the request spans
more than one specialist, dispatch all of them in parallel (overlap is intended,
not an error). For a broad request ("análise completa"), dispatch all of the
discipline's agents.

The table below is the worked routing for the `bi` discipline. For any other
discipline, route off the discovered agents' `description` fields the same way —
no table edit needed.

| Signals in the request | Agent(s) |
|---|---|
| ROI, ROAS, CPA, CTR, channel, campaign, media, attribution, funnel | `marketing-bi-media-analytics` |
| "por que", comparison, trend, a metric from the vault, exploration | `marketing-bi-data-analyst` |
| sources disagree, organize/structure data, metric definition/standardization, "where does this number come from" | `marketing-bi-data-engineer` |
| recommendation, presentation, "the read on this", client summary, narrative | `marketing-bi-insights` |
| broad request / "análise completa" | multiple, in parallel |

> If a request fires signals from more than one single-agent row, dispatch all matching agents in parallel — partial overlap is intended behavior, not a routing error. Example: "compare channels by ROAS" → both `marketing-bi-data-analyst` and `marketing-bi-media-analytics`.

---

## Step 6 — Dispatch in parallel

Dispatch the selected agents **in parallel**. Pass each one:
1. The user's request (the part after the discipline argument).
2. The candidate file paths gathered in Step 3.

All agents are read-only and return a markdown report ending in a
"Deliverable proposto" section.

---

## Step 7 — Synthesize

**This skill** merges the agents' reports into one answer (the specialists do
not consume each other's output):

- De-duplicate overlapping findings; keep one `[[source]]` per fact.
- Order by relevance to the request.
- Preserve every wikilink — traceability is non-negotiable.
- Surface any contradiction the agents flagged.
- Assemble a single **proposed deliverable** from the agents'
  "Deliverable proposto" sections.

Present in chat:

### 📌 Resposta
The synthesized answer with inline `[[wikilinks]]`.

### 📄 Deliverable proposto
The vault-ready note content.

### ⚠️ Lacunas
Anything the vault did not cover.

---

## Step 8 — Propose, confirm, write

Ask where to save (offer the default), then write **only after the user
confirms**:

| Request | Destination |
|---|---|
| Specific to a client | `clients/{slug}/references/{YYYY-MM-DD} {title}.md` |
| Specific to a product | `products/{slug}/references/{YYYY-MM-DD} {title}.md` |
| No entity | `operational/analytics/{YYYY-MM-DD} {title}.md` |

Frontmatter of the saved note:
```yaml
---
title: {title}
date: {YYYY-MM-DD}
tags: [{discipline}, analysis]
source: specialist/{discipline}
---
```

If the user declines, leave the vault untouched — the analysis still stands in
the conversation.

---

## Edge cases

- **No discipline and can't infer** — ask once, listing available disciplines
  (today: `bi`).
- **Discipline has no agents** — report it and stop (Step 4).
- **Subject not found in the vault** — say so honestly; offer to proceed with a
  general analysis only if the user asks.
- **Multiple clients match the subject** — ask which one before dispatching.
- **Agents return contradictory numbers** — surface both with sources; do not
  silently reconcile.

---

## Scaling note (for maintainers)

Adding a role to an existing discipline = drop a new
`agents/{dept}-{discipline}-{role}.md` with the right `discipline` field; this
skill discovers it automatically (Step 4). Routing is driven by the discovered
agents' `description` fields (Step 5), so a new discipline needs no
routing-table edit either. Adding a new discipline = create
agents with a new `discipline` value and call `/specialist {discipline} ...`.
This skill does not need to change.
