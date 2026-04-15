---
name: process-meeting-emails
description: "Automatic pipeline that ingests meeting transcription emails and creates structured notes in the vault. Use this skill when the user says 'process meeting emails', 'new meeting in email', 'run meeting pipeline', 'process transcripts', or when triggered by an automatic scheduled task. Searches for transcription emails (Gemini Meeting Notes, Fireflies, Otter, or similar), extracts meeting content, classifies contexts with ≥80% confidence, and generates formatted notes in the vault — no action is lost."
---

# Skill: process-meeting-emails

## What this skill does

Automatic pipeline that transforms meeting transcription emails (Gemini Meeting Notes, Fireflies, Otter, Read.ai, or similar) into structured notes in the vault, with tasks and dashboards updated.

**Phase 1 (default):** reads and processes, **does not archive** emails — the user validates manually.
**Phase 2 (after authorization):** applies labels and archives emails automatically.

---

## Step 1 — Configuration check

Verify `operational/config/domain-mapping.yml` and `operational/config/client-aliases.yml`. If they don't exist or are empty, alert the user and guide them to configure before continuing.

Identify which transcription service is being used (verified during setup or via email content):
- **Gemini Meeting Notes:** `from:(gemini-notes@google.com)` in ~~email
- **Fireflies:** `from:(noreply@fireflies.ai)`
- **Otter:** `from:(noreply@otter.ai)`
- **Custom:** user defines the query

---

## Step 2 — Fetch emails

Use ~~email with the configured query. Fetch only unprocessed emails (in inbox, without a processed label).

If no emails are found: log "0 emails found" and stop.

---

## Step 3 — For each email found

**a. Extract data:**
- Meeting title, date, time, duration
- Participant list with email addresses
- Link to full transcript (if available) → fetch via ~~cloud-storage
- Auto-generated summary from the transcription service
- Action items automatically identified by the service

**b. Classify the context:**
1. External participant email domains → `domain-mapping.yml`
2. Keywords in the title → `client-aliases.yml`
3. Cross-reference time with ~~calendar
4. If confidence <80% → save to `inbox/PENDING-CLASSIFY YYYY-MM-DD Title.md` and log

**c. If context identified with ≥80% confidence:**
- Generate note following the same format as the `new-meeting` skill
- Save to `clients/{context}/meetings/YYYY-MM-DD Title.md`
- Extract follow-ups → add to `Tasks {Context}.md`
- Extract decisions → log as ADR suggestion
- Update context dashboard

**d. Internal meeting** (all participants on the same internal domain):
- Save to `operational/meetings/YYYY-MM-DD Title.md`
- Update `operational/tasks/Operational Tasks.md`

**e. Personal meeting** (no corporate domain):
- Ignore by default — log as "ignored/personal"

---

## Step 4 — Log the run

Update `operational/tasks/Processing Log.md`:

```markdown
## YYYY-MM-DD HH:MM
- Emails found: N
- Processed: N
- Pending classification: N (saved to inbox/)
- Ignored (personal): N
- Errors: N
```

---

## Step 5 — Phase 2 (only if authorized)

If the user has explicitly authorized Phase 2:
- Apply label `Processed/{Context}` to the email via ~~email
- Remove from inbox

**Never activate Phase 2 without explicit user authorization.**
