---
name: daily-brief
description: "Generates the morning situational briefing — today's agenda, urgent tasks, overdue follow-ups, and contexts without recent contact. Use ALWAYS when the user says 'brief', 'what do I have today', 'daily summary', 'what's overdue', 'catch me up', 'morning update', or opens the system in the morning without a specific request. Scans all task files in the vault, cross-references the day's calendar, and delivers a situation panel in under 2 minutes of reading."
---

# Skill: daily-brief

## What this skill delivers

A daily situation panel covering:

1. **Today's agenda** — calendar meetings
2. **Urgent** — overdue tasks or tasks due today
3. **Chase others** — items waiting on someone with an overdue follow-up date
4. **No recent contact** — contexts without a touchpoint in >14 days
5. **Preview** — what's coming in the next 3 business days

---

## Step 1 — Today's agenda

Use ~~calendar to list today's events. List in chronological order with time, title, and external participants. If a meeting has an identified context → note that `new-meeting` should be triggered after it.

---

## Step 2 — Scan tasks

Dynamically discover all task files in the vault:
- `clients/*/Tasks *.md` — one per client/project
- `products/*/Tasks *.md` — one per product
- `operational/tasks/Operational Tasks.md`

For each file, extract:
- Items `- [ ]` with `due` ≤ today → **overdue / due today**
- Items in `## Waiting on others` with a follow-up date ≤ today → **overdue chase**

---

## Step 3 — Check last touchpoint

For each active context in `clients/`, check the date of the last meeting:
1. "Last meeting" field in the `{Context}.md` dashboard
2. Most recent file in `clients/{context}/meetings/`

Contexts without a touchpoint in >14 days → list in the brief.

---

## Step 4 — Compose the brief

```markdown
# Brief — {weekday}, {YYYY-MM-DD}

## 🗓️ Today's agenda
- HH:MM — Title (External Participants)
[or "No meetings scheduled today"]

## 🔴 Urgent — overdue or due today
- **{Context}** — Description — due {date} — owner: Name
[or "Nothing urgent today ✓"]

## 🟡 Chase others
- **{Context}** — Waiting on: Name — follow up today
[or "None"]

## 🟢 No recent contact (>14 days)
- **{Context}** — last contact: {date} ({N} days ago)
[or "All contexts have recent contact ✓"]

## 📅 Next 3 business days
[upcoming meetings and tasks with near deadlines]

---
*Generated at {HH:MM} · [[Open Tasks]] for full view*
```

---

## Step 5 — Save (optional)

If the user says "save the brief", create:
`operational/daily/YYYY-MM-DD Brief.md`

```yaml
---
title: Brief YYYY-MM-DD
date: YYYY-MM-DD
tags:
  - operational
  - daily
  - brief
---
```

---

## Notes

- Do not include `[x]` items (already completed)
- If a context's task file doesn't exist → alert in the brief
- Keep it readable in <2 minutes — if many items, group and reference `[[Open Tasks]]`
