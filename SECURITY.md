# Security Policy

Mind++ is a pure-Markdown/JSON plugin for Claude Cowork — it contains no
executable code and runs entirely inside your own Claude Cowork environment,
reading and writing files in a folder you choose. Even so, we take reports
seriously, especially anything that could cause a skill to leak or mishandle
your data.

## Supported versions

The latest release is supported. Mind++ follows [Semantic Versioning](https://semver.org);
see [`CHANGELOG.md`](CHANGELOG.md) for what changed in each version.

## Reporting a vulnerability

Please report security issues by
[opening an issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
with the `security` label.

If the report is sensitive (for example, it could expose user data), prefer
**GitHub's private vulnerability reporting** instead of a public issue — open the
repository's **Security** tab → **Report a vulnerability**. (Maintainers: enable
this under *Settings → Security → Private vulnerability reporting*.)

When reporting, please include:

- The skill, agent, or file involved
- What the issue allows (e.g. unintended data exposure, a destructive action
  without confirmation)
- Steps to reproduce — **redact any personal or client data**

## What is in scope

- A skill or agent that writes, moves, or deletes vault data **without the
  confirmation the design requires**
- Instructions that could cause Claude to send vault contents to an external
  service that the user did not explicitly connect
- Leaking the contents of `.auto-memory/` or other private vault areas

## What is out of scope

- Vulnerabilities in Claude Cowork, Obsidian, or third-party sync services
  (Google Drive, iCloud, Dropbox, OneDrive) — report those to the respective
  vendors
- Risks from external connectors you chose to enable (these are opt-in)

Thank you for helping keep Mind++ users safe.
