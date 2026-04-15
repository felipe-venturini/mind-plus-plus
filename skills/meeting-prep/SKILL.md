---
name: meeting-prep
description: "Prepares a briefing for an upcoming meeting by pulling recent meetings, open tasks, pending decisions, and unresolved follow-ups for the relevant client, product, or person. Use when the user says 'prep for meeting with X', 'what should I talk about with X', 'brief me on X before the call', 'what's pending with X', or mentions a meeting that is about to happen."
---

# Skill: meeting-prep

## What this skill does

Produces a focused pre-meeting briefing for a specific context (client, product, team, or person). The goal is to walk the user into a call already knowing: what was last said, what is open, what decisions are pending, and what they owe the other side.

This skill is read-only — it never creates tasks, never moves files, never edits dashboards. Its single output is a briefing presented in chat.

---

## Step 1 — Identify the context

From the user's request, extract:

1. **Who or what** the meeting is about — client name, product, teammate, external contact
2. **When** the meeting is (today, tomorrow, a specific date) — optional
3. **Topic or goal**, if mentioned — optional

If the context is ambiguous (e.g., "prep for my meeting"), ask one targeted question: "Which meeting — who's it with?"

Match the context to a folder:
- `clients/{slug}/` for clients
- `products/{slug}/` for products
- `operational/` for internal meetings
- If no folder exists, ask whether to look under a different name

---

## Step 2 — Gather signals

Read from the vault, in this order:

1. **Dashboard** — `{Context}.md` at the root of the context folder. Extract: current status, active projects, key contacts.
2. **Last 3 meetings** — most recent files in `{context}/meetings/`. Summarize the arc — what was discussed, what was agreed, what was promised.
3. **Open tasks** — `Tasks {Context}.md`. List everything not yet done, flagged by:
   - Overdue (past due date) → highlight
   - Assigned to the user → "you owe"
   - Assigned to someone on the other side → "they owe"
4. **Recent decisions** — files in `{context}/decisions/` modified in the last 60 days
5. **Open questions or risks** — search recent meeting notes for phrases like "to confirm", "pending", "risk", "blocked" (adapt to user's language)

If `~~calendar` is connected, read the event details for the upcoming meeting: attendees, agenda, description.

---

## Step 3 — Produce the briefing

Output a structured briefing in chat with these sections:

### 📋 Context
One paragraph: who the meeting is with, what the relationship's current state is, what was last discussed.

### 🎯 Likely agenda
Based on open items and recent thread — 3–5 topics probably on the table.

### ⚠️ You owe them
Tasks assigned to the user that are open or overdue. Each line: what + original date + status.

### 🔄 They owe you
Tasks on the other side still open. Each line: what + who + how long it has been pending.

### ❓ Open questions
Unresolved points from recent meetings — things to clarify, confirm, or close today.

### 💡 Suggested talking points
3–5 concrete items the user should raise — framed as actions ("Confirm X", "Push for a decision on Y", "Ask about Z").

### 🔗 Recent artifacts
Wikilinks to the last meeting, the dashboard, the open tasks file — so the user can drill in if needed.

---

## Step 4 — Offer next steps

At the end of the briefing, offer (do not execute):

> Want me to draft a message to send before the meeting, or save this briefing to `operational/meetings/{YYYY-MM-DD} Prep {context}.md`?

Only save if confirmed. Default behavior is ephemeral — the briefing lives in the chat.

---

## Edge cases

- **No meetings folder yet** — produce a briefing from whatever exists (dashboard, tasks) and note "no prior meetings on record"
- **Context not found** — list the closest client/product slugs and ask which one the user meant
- **Recurring meeting** — if the last meeting was <7 days ago, lead with "since we last met on {date}" instead of a full history recap
- **No open tasks** — say so plainly; do not fabricate agenda items
