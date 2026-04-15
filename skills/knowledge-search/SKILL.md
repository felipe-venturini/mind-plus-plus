---
name: knowledge-search
description: "Searches the vault by topic or question and returns a synthesized answer with wikilinks to the source notes. Use when the user says 'what do I know about X', 'everything we discussed about Y', 'find notes on Z', 'what did we decide about...', 'search the vault for...', or asks any question that should be answered from the user's own accumulated knowledge rather than general reasoning."
---

# Skill: knowledge-search

## What this skill does

Answers questions from the vault — treating the user's own notes, meetings, and decisions as the authoritative knowledge base. The output is a synthesis, not a raw file dump. Every claim in the answer must be backed by a wikilink to the source.

This skill is the opposite of hallucination: it prefers to say "nothing found in the vault" over inventing context.

---

## Step 1 — Parse the query

Extract:

1. **Subject** — what the user is asking about (a client, product, person, topic, decision)
2. **Intent** — are they looking for facts, a decision, a status, a history, or an overview?
3. **Time scope** — recent, all time, a specific period

If the query is vague ("what about the Acme thing"), ask one clarifying question before searching.

---

## Step 2 — Scope the search

Decide which folders are in-scope based on the query:

| Query type | Folders to search |
|-----------|-------------------|
| About a specific client | `clients/{slug}/` only |
| About a specific product | `products/{slug}/` only |
| About a decision | all `*/decisions/` folders |
| About a meeting | all `*/meetings/` folders |
| About a topic (no entity) | entire vault except `archive/` |
| About a person | cross-folder search for their name |
| Historical ("everything about X") | include `archive/` as well |

Never search `.auto-memory/` unless the question is about the user themselves.

---

## Step 3 — Execute the search

Use grep or equivalent to find candidate files. Strategies:

1. **Literal match** — exact phrase or keyword from the query
2. **Alias expansion** — if the subject has known aliases (check `operational/config/client-aliases.yml`), search for all of them
3. **Tag search** — if the query maps to a likely tag, check frontmatter
4. **Title match** — check filenames for topic keywords

Collect all matching files. Rank by:
- Recency (newer first)
- Title match > body match
- Dashboards and ADRs > meeting notes > raw inbox

Cap at ~15 candidate files. Read the top matches in full; skim the rest.

**If candidates exceed ~15 files, delegate to the `vault-researcher` agent.** Pass it the list of candidate file paths and the original query. It reads them in isolation and returns a clean synthesis — this keeps the main conversation context lean and avoids drowning the user in raw file content. Wait for the agent's report, then adapt it to the format in Step 4.

---

## Step 4 — Synthesize

Produce a structured answer in chat:

### 📌 Short answer
One or two sentences directly answering the query.

### 📖 Context
Three to five bullets of supporting detail, each with an inline wikilink to the source:
- Key fact ([[source file]])
- Decision made on {date} ([[ADR or meeting]])
- Status / current state ([[dashboard]])

### 🕰️ Timeline (only if relevant)
Chronological view for queries like "the history of X" — dates + wikilinks.

### ⚠️ Open threads
Anything in the matching notes that is explicitly unresolved, pending, or flagged as a risk.

### 🔗 All sources
Flat list of every file referenced, with wikilinks. Ordered by relevance.

---

## Step 5 — Be honest about gaps

If the vault has no relevant content, say so:

> Nothing in the vault directly addresses {query}. Closest matches: [[X]], [[Y]] — but neither is a direct answer.

Do not fill gaps with general knowledge. If the user wants you to reason beyond the vault, they can ask explicitly.

---

## Edge cases

- **Query resolves to too many files (>30 candidates)** — report the count, suggest narrowing ("about 40 files mention this — want me to scope to a specific client or time range?")
- **Contradictory notes** — surface the contradiction explicitly with both sources; do not silently pick one
- **Subject not found at all** — check for misspellings or aliases, then report "not found" with a list of similarly-named entities
- **Query is about a person's role or affiliation** — cross-reference dashboards of clients they appear in
