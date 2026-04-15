# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user
connects in that category. Plugins are tool-agnostic — they describe
workflows in terms of categories rather than specific products.

When you install a connector in Cowork (e.g., connect your Google Calendar),
Claude automatically maps `~~calendar` to that service.

## Connectors for this plugin

| Category      | Placeholder        | Used In                                         | Options                           |
| ------------- | ------------------ | ----------------------------------------------- | --------------------------------- |
| Email         | `~~email`          | `process-meeting-emails`                        | Gmail, Outlook                    |
| Calendar      | `~~calendar`       | `daily-brief`, `weekly-review`, `new-meeting`, `process-meeting-emails` | Google Calendar, Outlook Calendar |
| Cloud Storage | `~~cloud-storage`  | `process-meeting-emails` (full transcripts)     | Google Drive, OneDrive, Dropbox   |

## Which connectors are required?

| Connector      | Required for core workflows? | Without it...                                           |
| -------------- | ---------------------------- | ------------------------------------------------------- |
| `~~email`      | Optional                     | Automatic meeting-email pipeline does not run           |
| `~~calendar`   | Recommended                  | Daily brief and weekly review have no agenda context    |
| `~~cloud-storage` | Optional                  | Full transcripts are not fetched automatically          |

The plugin works without any connectors — the skills degrade gracefully,
reading local vault files only. Connectors unlock the full pipeline experience.

## Setup

1. In Cowork, open **Settings → Connectors**
2. Connect the services you use (Google Calendar, Gmail, etc.)
3. Run the `setup` skill to configure your vault
4. Done — Claude will route `~~category` calls to your connected services automatically
