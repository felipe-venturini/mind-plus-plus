---
name: weekly-review
description: "Weekly review that consolidates tasks, unlogged meetings, at-risk contexts, and a preview of next week. Use ALWAYS when the user says 'weekly review', 'friday review', 'how was the week', 'close the week', 'week summary', or similar. Scans all task files in the vault, identifies what was completed, what is at risk, contexts without recent contact, and meetings without a logged note, then generates and saves the review."
---

# Skill: weekly-review

## What this skill delivers

A consolidated weekly review with:
- What was completed this week
- What is overdue or at risk
- Contexts without recent contact
- Meetings without a logged note
- Preview of next week
- Automatic task housekeeping

---

## Step 1 — Define the period

Calculate Monday through Friday of the current week (or the week the user specifies).

---

## Step 2 — Scan all tasks

Dynamically discover all `Tasks *.md` files in the vault (`clients/`, `products/`, `operational/tasks/`).

For each file:
- `[x]` items with a date from this week → **completed**
- `[ ]` items with due date < today → **overdue**
- `[ ]` items with due date in the next 3 business days → **at risk**
- Items in `## Waiting on others` with no update in >7 days → **chase**

---

## Step 3 — Housekeeping

In each task file, move items from `## Completed (last 30 days)` with a date >30 days ago to `## History`. Record how many items were moved.

---

## Step 4 — Check meetings from the week

Use ~~calendar to list events from the last 5 business days with external participants. Cross-reference with files in `clients/*/meetings/` — identify meetings with no corresponding note in the vault → list to be processed with `new-meeting`.

---

## Step 5 — Check touchpoints

For each context in `clients/`, check the date of the last meeting or update. Contexts without contact in >14 days go into the alert section.

---

## Step 6 — Preview next week

Use ~~calendar to list next week's events with external participants. List tasks with a due date in the coming week, sorted by priority.

---

## Step 7 — Generate and save the review

```markdown
---
title: Weekly Review YYYY-MM-DD
date: YYYY-MM-DD
tags:
  - operational
  - daily
  - weekly-review
---

# Weekly Review — week of MM/DD to MM/DD

## ✅ Completed this week
## 🔴 Overdue (urgent action needed)
## ⚠️ At risk (next 3 business days)
## 👥 No recent contact (>14 days)
## 📋 Meetings this week without a note
## 📅 Next week
## 🔁 Housekeeping
```

Save to `operational/daily/YYYY-MM-DD Weekly review.md`.

Update `operational/tasks/Open Tasks.md` with the current state of all contexts.
