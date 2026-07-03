---
name: specialist
description: "Routes a request to the right domain specialists and produces a vault-grounded deliverable. The domain is the first argument. Use when the user says '/specialist marketing ...', 'aciona um especialista de marketing', 'analisa a performance da campanha ...', 'qual o ROAS/ROI de ...', 'que números temos sobre ...', or asks for data analysis, media performance, data consistency, or a data-driven recommendation. Today the only domain is `marketing` (with the `bi` discipline)."
arguments: [domain]
---

# Skill: specialist

## What this skill does

Acts as the single entry point to Mind++'s specialist agents. It captures the
user's request, loads the relevant vault history, discovers the specialist agents
for the requested domain, and hands routing and arbitration to the universal
`specialist-judge` agent. The judge picks the minimal set of specialists to run,
reconciles their (read-only) reports, and rules on every open doubt (bounce back to
a specialist, escalate to the user, or record as a gap). This skill executes the
judge's rulings — it is the only component that dispatches agents and the only one
that writes to the vault, **and it writes only after the user confirms.**

Specialists analyze and propose; the judge routes and arbitrates; **this skill is
what dispatches and writes.**

---

## Step 1 — Determine the domain

The domain is the first argument (`$domain` / `$0`), e.g. `marketing`.

- If provided (`/specialist marketing ...`), use it.
- If absent, infer it from the request (marketing signals: metrics, performance,
  ROI, ROAS, "que números", campaign, media, SEO, social, dashboard, attribution).
- If still ambiguous, ask one short question naming the available domains
  (today: `marketing`).

> Invocation note: use `/specialist marketing ...` (space, domain as argument).
> Do **not** use `/specialist:marketing` — the colon is reserved for plugin namespaces.
> For fully-qualified invocation use `/mind-plus-plus:specialist marketing <pedido>`.

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

## Step 4 — Discover the domain's agents

List `agents/` and select agents whose frontmatter contains
`domain: {domain}`. Do **not** parse agent names or paths — filter on the
`domain` field. The `discipline` field groups agents within a domain but is not
the routing key.

```bash
grep -rl '^domain: {domain}$' agents/
```

If none match, tell the user no specialists exist for that domain yet and stop.

Currently, for the `marketing` domain, discovery returns (all under the `bi`
discipline for now):
- `marketing-bi-data-analyst` — exploratory analysis, comparisons, "why"
- `marketing-bi-media-analytics` — ROI/ROAS, CPA, CTR, channels, attribution
- `marketing-bi-data-engineer` — provenance, reconciliation, metric definitions
- `marketing-bi-insights` — narrative and recommendation

---

## Step 5 — Judge triage (which specialists to run)

Do **not** route with a static table. Invoke `specialist-judge` in **TRIAGE mode**,
passing:
1. The user's request (the part after the domain argument).
2. The roster from Step 4 — each discovered agent's `name` and `description`.

Begin the prompt with `MODE: TRIAGE`. The roster spans every discipline and role in
the domain. The judge returns the **minimal** set of specialists whose `description`
matches the request, with a one-line justification for each selected and each
rejected agent. Dispatch exactly the selected set.

**Never dispatch all specialists by default** — only when the judge selects them
(e.g. a genuinely broad "análise completa"). Overlap across specialists is expected
when a request fires more than one lens.

> Fallback: if the judge is unavailable, route off the discovered agents'
> `description` fields yourself, selecting the minimal matching set — still never all
> by default.

---

## Step 6 — Dispatch the selected specialists in parallel

Dispatch the specialists the judge selected in Step 5 **in parallel**. Pass each one:
1. The user's request (the part after the domain argument).
2. The candidate file paths gathered in Step 3.

All agents are read-only. Each returns a markdown report that includes a
"Dúvidas em aberto" section and ends in a "Deliverable proposto" section.

---

## Step 7 — Judge arbitration and resolution loop

Invoke `specialist-judge` in **ARBITRATION mode** (begin the prompt with
`MODE: ARBITRATION`, and state the current round, starting at 1). Pass the user's
request and every selected specialist's full report. The judge returns:
- a **reconciled** view (dedup, ordered, wikilinks preserved, divergent numbers
  surfaced not merged); and
- a list of **unresolved items**, each tagged `[devolve]`, `[pergunta]`, or `[lacuna]`.

Resolve the items, capped at **2 bounce-back rounds** total:

1. **`[devolve]`** — re-dispatch the named specialist with the judge's specific
   question (Step 6 mechanics, one targeted question). Collect the refined point.
2. After collecting all bounce-backs for the round, re-invoke the judge in
   ARBITRATION mode with the incremented round number and the refined points.
3. Stop looping once there are no `[devolve]` items or after round 2. At round 3 the
   judge is instructed to force every remaining item to `[pergunta]` or `[lacuna]`.
4. **`[pergunta]`** items are handled in Step 8. **`[lacuna]`** items flow straight
   into the final answer's gaps.

## Step 8 — Escalate open questions to the user (batched)

If arbitration produced any `[pergunta]` items, ask them **all at once** with a
single `AskUserQuestion` call — one question per item, each offering the judge's **3
suggested answers** (the tool automatically adds a free-text "Other" option). Do not
ask them one at a time.

Feed the user's answers back to the relevant specialist(s) for a final refine (Step 6
mechanics), then re-invoke the judge in ARBITRATION mode once more to fold the answers
into the reconciled view.

## Step 9 — Present the reconciled answer

Present the judge's final reconciled output in chat:

### 📌 Resposta
The reconciled answer with inline `[[wikilinks]]`.

### 📄 Deliverable proposto
The vault-ready note content (the judge's assembled proposal).

### ⚠️ Lacunas
The `[lacuna]` items plus anything the vault did not cover.

---

## Step 10 — Propose, confirm, write

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
tags: [{domain}, analysis]
source: specialist/{domain}
---
```

If the user declines, leave the vault untouched — the analysis still stands in
the conversation.

---

## Edge cases

- **No domain and can't infer** — ask once, listing available domains
  (today: `marketing`).
- **Domain has no agents** — report it and stop (Step 4).
- **Subject not found in the vault** — say so honestly; offer to proceed with a
  general analysis only if the user asks.
- **Multiple clients match the subject** — ask which one before dispatching.
- **Agents return contradictory numbers** — surface both with sources; do not
  silently reconcile.

---

## Scaling note (for maintainers)

Agents are **flat** files in `agents/`, named
`agents/{domain}__{discipline}__{role}.md` (double underscore between hierarchy
levels, single underscore within a name — e.g. `marketing__bi__data_analyst.md`).
Adding a role = drop a new file with that name whose `name:` frontmatter is the
fully-qualified `{domain}-{discipline}-{role}` and whose `domain:`/`discipline:`
fields are set. Claude **auto-discovers** `agents/*.md` — no `plugin.json` edit
(discovery is non-recursive, so keep agents flat, never nested). This skill then
finds it automatically — Step 4's `grep '^domain:'` matches the frontmatter
regardless of filename. Routing keys off the `domain:` field, and the universal
`specialist-judge` in TRIAGE mode selects the specialists off their `description`
fields (Step 5), so a new discipline, role, or domain needs no routing-table edit
and no judge edit — just add the flat file and call `/specialist {domain} ...`.
This skill does not need to change.
