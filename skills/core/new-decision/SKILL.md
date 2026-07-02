---
name: new-decision
description: "Records an architecture or business decision as a structured ADR (Architecture Decision Record) with context, decision, consequences, and rejected alternatives. Use when the user says 'record a decision', 'new ADR', 'document this decision', 'we decided X', 'create a decision doc', or describes a choice that deserves to be memorialized."
---

# Skill: new-decision

## What this skill does

Creates an ADR — a short, structured document that captures *why* a decision was made, *what* was decided, and *what alternatives were rejected*. ADRs prevent the same debate from happening twice six months later.

The goal is not completeness — it's traceability. A good ADR answers one question: "Why did we choose this?"

---

## Step 1 — Identify the decision and its scope

From the user's input, extract:

1. **What was decided** — one-sentence summary
2. **Who is affected** — which client, product, team, or the organization as a whole
3. **Why it needed a decision** — the problem or trigger

If the scope is unclear, ask: "Is this a client/product decision or an organizational one?"

Map scope to folder:
- Client decision → `clients/{slug}/decisions/`
- Product decision → `products/{slug}/decisions/`
- Organizational / team / operational decision → `operational/decisions/`
- Personal decision (career, learning path, tooling for own use) → `personal/decisions/` (create if missing)

---

## Step 2 — Determine the ADR number

List existing ADRs in the target folder. Find the highest number (ADRs follow `NNN Title.md`). The new number is the next integer, zero-padded to three digits.

If the folder doesn't exist yet, create it and use `001`.

---

## Step 3 — Gather the supporting context

Ask the user for what is missing (but only what is missing — do not re-ask what was already said):

1. **Context** — what situation prompted the decision? What constraints apply? What was the existing state?
2. **Decision** — what was chosen, stated plainly and in the present tense ("We will use X")
3. **Consequences** — what becomes true after this decision? What new risks, costs, or obligations?
4. **Alternatives considered** — what other options were on the table, and why were they rejected? This is the most valuable section and the most commonly skipped — push gently if the user leaves it blank.
5. **Status** — Proposed, Accepted, Deprecated, or Superseded (default: Accepted)
6. **Stakeholders** — who participated in the decision or needs to know

---

## Step 4 — Write the ADR

File path: `{scope-folder}/decisions/{NNN} {Title}.md`

Template:

```markdown
---
title: {Title}
date: {YYYY-MM-DD}
status: {Accepted|Proposed|Deprecated|Superseded}
tags:
  - adr
  - decision
  - {scope tag}
---

# ADR-{NNN}: {Title}

## Status
{Status} — {YYYY-MM-DD}

## Context
{Why this decision was needed. What situation or problem prompted it. What constraints apply.}

## Decision
{What we decided, stated in the present tense.}

## Consequences

### Positive
- {What gets better}

### Negative
- {What we give up, what risks we accept}

### Neutral
- {What changes but isn't strictly better or worse}

## Alternatives considered

### {Alternative 1}
{One paragraph. Why rejected.}

### {Alternative 2}
{One paragraph. Why rejected.}

## Stakeholders
- {Person / role / team}

## Related
- [[{link to related ADR, meeting, or doc}]]
```

Use the user's preferred vault language (read `.auto-memory/user_profile.md` if unclear).

---

## Step 5 — Update related files

After writing the ADR:

1. **Dashboard** — if there is a dashboard for the scope (`{Context}.md`), add a line under a "Recent decisions" section linking to the new ADR. Do not rewrite the dashboard wholesale.
2. **Superseded ADRs** — if this ADR replaces an older one, open the old file and set `status: Superseded by [[{NNN} {Title}]]`.
3. **No tasks auto-created** — if the decision implies follow-up actions, mention them in chat and offer to add them to the relevant tasks file. Do not add silently.

---

## Step 6 — Confirm

Report back in chat:

> Recorded as `[[{NNN} {Title}]]`. Status: {Status}.
> {If dashboard updated: "Linked from [[{Dashboard}]]."}
> {If follow-ups suggested: "Want me to add any of the implied next steps to the tasks file?"}

---

## Edge cases

- **User is brainstorming, not deciding** — if there is no clear decision yet, suggest saving the discussion as a note via `capture-idea` and offering to create the ADR once the decision lands
- **Decision reverses a prior ADR** — always mark the old one as `Superseded` and link bidirectionally
- **Scope spans multiple clients** — default to `operational/decisions/` and cross-link from each client's dashboard
