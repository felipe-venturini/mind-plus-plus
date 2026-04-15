---
name: stakeholder-update
description: "Generates a status update for a client, product, or project from vault content — recent meetings, decisions, open tasks, risks, and next steps. Use when the user says 'status update on X', 'client report for X', 'update for {stakeholder}', 'weekly status for the X project', 'prep a client-facing summary', or needs to communicate progress to someone external."
---

# Skill: stakeholder-update

## What this skill does

Produces a stakeholder-facing status update from the vault — the kind of message you send to a client sponsor on Friday or paste into a weekly email. Unlike `weekly-review`, which is for the user's own consumption, this skill produces external-facing copy: no internal shorthand, no sensitive context, no speculation.

The output can be copied straight into an email, Slack message, or shared doc.

---

## Step 1 — Identify the target and audience

Extract from the user's request:

1. **Context** — which client, product, or project
2. **Audience** — who will read this (exec sponsor, project lead, whole team)
3. **Channel** — email, Slack, document (affects formatting)
4. **Period** — last week, last sprint, since last update (default: last 14 days)
5. **Tone** — formal or informal (default: professional but conversational)

If audience or channel is unclear, ask. They change the format significantly.

---

## Step 2 — Pull raw signals

Read from the relevant context folder:

1. **Meetings** in the period — `{context}/meetings/` filtered by date
2. **Decisions** made in the period — `{context}/decisions/`
3. **Open tasks** — `Tasks {Context}.md` — split into:
   - Done in the period (check completed markers)
   - In progress
   - Blocked or overdue
   - Upcoming
4. **Dashboard** — `{Context}.md` for overall status and active projects

Also check `.auto-memory/` for any project memory that gives context on goals or milestones.

---

## Step 3 — Filter for external consumption

Before drafting, strip out anything that should NOT go to a stakeholder:

- Internal team dynamics or personnel issues
- Raw cost discussions or margin data (unless audience explicitly needs them)
- Speculation, hypotheses, or half-formed plans
- Direct quotes from internal meetings
- Anything tagged `confidential`, `internal-only`, or `private` in frontmatter

When in doubt, leave it out. A clean, short update beats a comprehensive one that leaks.

---

## Step 4 — Draft the update

Default structure (adapt to audience and channel):

### 📅 {Context} — Status update, {date range}

### ✅ Progress since last update
Three to five bullets of concrete, shipped, verifiable work. Each bullet should be something the stakeholder can point to.

### 🎯 Decisions made
Notable decisions in the period, one line each. Link to ADRs only if the audience has access to the vault — otherwise, summarize inline.

### 🚧 In flight
What is actively being worked on. Include target dates where known.

### ⚠️ Risks & blockers
Honest but professional. If something is blocked on the stakeholder's side, say so clearly and propose a next step.

### 📌 Next steps
What happens between now and the next update. Dated when possible.

### ❓ Open questions for you
Only if there are real questions the stakeholder needs to answer. Skip this section if there are none — do not manufacture asks.

---

## Step 5 — Adapt to channel

- **Email** — greeting + sign-off, full sections, subject line suggestion
- **Slack** — leaner, fewer headers, use bold for section labels instead of `##`, no greeting
- **Shared doc** — full structure with headers, include a "Last updated" line at the top
- **Executive summary** — only the top two sections (progress, risks) in 5–7 lines total

---

## Step 6 — Offer before saving

Present the draft in chat. Ask:

> Want me to save this to `{context}/references/{YYYY-MM-DD} Update {audience}.md`, or is this just for copy-paste?

Default is copy-paste (ephemeral). Only save if confirmed.

If saved, also offer to add a dashboard line: "Last update to {audience}: {date}".

---

## Edge cases

- **Nothing shipped in the period** — do not pad; lead with "Quiet period — {reason}" and focus on what's coming next
- **Bad news to deliver** — draft it straight but offer a softer alternative. Never sugarcoat a missed deadline — stakeholders trust clarity over optimism.
- **Audience is hostile or a difficult relationship** — note it in chat and ask whether to adopt more defensive framing (facts-only, timeline-heavy, explicit citations)
- **Stakeholder has vault access** (rare) — include wikilinks; otherwise, always inline the substance
