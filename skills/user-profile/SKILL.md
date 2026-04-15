---
name: user-profile
description: "Captures, updates, and consults the user profile — who they are, their professional context, projects, personal goals, and work preferences. Use when the user wants the system to learn more about them, says 'do you know me?', 'update my profile', 'I want you to know that...', 'I am...', or shares personally relevant information. Also trigger proactively when the user mentions a job change, new client, new personal goal, or change of context."
---

# Skill: user-profile

## What this skill does

Maintains a rich user profile that informs the behavior of all other skills. The more the system knows about the user, the more personalized and relevant the second brain becomes.

The profile has two dimensions:
- **Professional:** work context, clients, projects, responsibilities
- **Personal:** values, life goals, interests, work preferences

---

## When to trigger

- User mentions something new about themselves → capture it
- User asks the system to "remember" something → save it
- Context change (new job, new project, new life phase) → update
- Processing the first meeting with a new client → create client context

---

## Step 1 — Read current profile

Before anything else, read:
- `.auto-memory/user_profile.md` — user's base profile
- `.auto-memory/MEMORY.md` — index of all memories

Identify what is already known to avoid redundant questions.

---

## Step 2 — Capture new information

If updating from a conversation, extract from context:
- What is the user describing about themselves?
- Is it professional or personal information?
- Is it about a specific client/project or about the user themselves?

If capturing proactively (user mentioned something relevant), confirm before saving:
> "I noticed you mentioned [X]. Would you like me to save that to your profile?"

Also ask about the user's preferred language for vault content — this is saved to the profile and used by the `setup` skill when generating `CLAUDE.md`.

---

## Step 3 — Profile structure

Save to `.auto-memory/user_profile.md`:

```markdown
---
name: User Profile
description: Who the user is, their professional and personal context
type: user
---

## Identity
- Name: {name if provided}
- Role: {main role}
- Industry: {area of work}
- Preferred language: {e.g. English, Portuguese, Spanish}

## Professional context
- Company / model: {company or freelancer}
- Main responsibilities: {list}
- Active clients / projects: {list with brief context}
- Main tools: {daily tools}

## Professional goals
- Short-term (this year): {list}
- Long-term: {list}

## Personal context
- Interests: {list}
- Personal goals: {list}
- Work preferences: {how they prefer to collaborate, communicate, decide}

## How to interact
- Preferred tone: {formal/informal, direct/detailed}
- What not to do: {things that are annoying or don't work}
- What works well: {approaches the user appreciates}
```

---

## Step 4 — Create client contexts

For each client/project mentioned that doesn't yet have a folder in the vault:

1. Ask whether to create the structure: `clients/{slug}/`
2. If yes, create a basic dashboard with what was mentioned
3. Create an empty `Tasks {Client}.md`

---

## Step 5 — Confirm

Summarize what was saved/updated and where. Do not list sensitive details — just confirm it was recorded.

---

## Privacy

**Do not save to the vault** (pushed to GitHub if synced):
- Health data, diagnoses
- Detailed financial information (account numbers, passwords)
- Home address

These stay only in `.auto-memory/` (not synced to GitHub by default).
