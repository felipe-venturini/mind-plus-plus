# Mind++ for Claude

**Dein zweites Gehirn, angetrieben von Claude — in Obsidian.**

> 🌍 Verfügbar in: [English](README.md) · [Português (BR)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [বাংলা](README.bn.md) · [Русский](README.ru.md) · [اردو](README.ur.md)
>
> 📖 **Vollständige Docs und Guides** → [GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki) · 🌐 **Website** → [felipe-venturini.github.io/mind-plus-plus](https://felipe-venturini.github.io/mind-plus-plus)

Mind++ ist ein kostenloses Open-Source-Plugin für [Claude Cowork](https://claude.ai/download), das Claude in einen proaktiven Wissenspartner verwandelt. Es erfasst Meetings, verfolgt Verpflichtungen, liefert tägliche Briefings und pflegt eine lebendige Wissensbasis für dein berufliches und persönliches Leben — alles als einfaches Markdown in einem [Obsidian](https://obsidian.md)-Vault gespeichert.

**Plugin herunterladen → [neueste Release](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)**

---

## Noch nie benutzt? Fang hier an.

Falls du noch nie von Obsidian gehört oder eine Markdown-Notiz geschrieben hast, keine Sorge. In einem Absatz:

**Obsidian** ist eine kostenlose App ([obsidian.md](https://obsidian.md)), die einen Ordner voller `.md`-Dateien (Markdown, reiner Text) auf deinem Computer liest und sie als wunderschönes, verknüpftes Notizbuch anzeigt. Weil alles reiner Text ist, **gehören deine Notizen für immer dir** — kein Cloud-Lock-in, kein kostenpflichtiges Abo, kein Anbieter, der verschwinden kann. Mind++ nutzt Obsidians Ordnerstruktur als Grundlage, weil es das haltbarste und privateste Format für persönliches Wissen ist, das es heute gibt.

**Claude Cowork** ist die Claude-Desktop-App ([claude.ai/download](https://claude.ai/download)), die Dateien auf deinem Computer lesen und schreiben kann. Wenn du Mind++ installierst, lernt Claude eine bestimmte Art, deine Notizen in diesem Ordner zu organisieren — sodass, wenn du sagst „ich hatte ein Meeting mit Jan", er die Notiz schreibt, die Action Items extrahiert und deine Aufgabenliste automatisch aktualisiert.

**Du musst kein Entwickler sein.** Du musst Git nicht kennen. Du musst YAML nicht kennen. Mind++ kümmert sich um die Struktur; du sprichst einfach mit Claude.

---

## Warum Mind++?

- **Kein Anbieter-Lock-in** — deine Daten sind einfache `.md`-Dateien, überall in jedem Editor lesbar
- **Privatsphäre standardmäßig** — alles bleibt in deinem Ordner, auf deinem Rechner
- **Obsidian-nativ** — Graph View, Backlinks, Suche und Tags funktionieren sofort
- **KI verarbeitet, Mensch bestätigt** — Claude verarbeitet; du bestätigst, bevor etwas verschoben oder gelöscht wird
- **Proaktiv, nicht reaktiv** — bringt überfällige Aufgaben und stille Kunden ans Licht, ohne dass du fragst
- **Mehrsprachig** — das Plugin funktioniert in jeder Sprache, in der du schreibst; Claude passt sich dir an

---

## Schnellstart in 5 Minuten

> 👉 **Lieber eine detaillierte Schritt-für-Schritt-Anleitung?** → [Installation Guide im Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Installation-Guide)

### 1. Installiere die drei Tools

| Tool | Was es tut | Link |
|------|-----------|------|
| **Claude Cowork** (erforderlich) | Die Claude-App, die das Plugin ausführt | [claude.ai/download](https://claude.ai/download) |
| **Obsidian** (dringend empfohlen) | Visueller Navigator für deine Notizen | [obsidian.md](https://obsidian.md) |
| **Deine Sync-Wahl** (optional) | Backup und Zugriff überall — wähle eins: [Obsidian Git](https://github.com/Vinzent03/obsidian-git), Google Drive, iCloud Drive, OneDrive oder Dropbox | siehe [Sync Strategies](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) |

### 2. Wähle, wo dein Vault leben soll

Wähle einen Ordner auf deinem Computer. Dort wird jede Notiz, jedes Meeting und jede Entscheidung gespeichert.

- **Am einfachsten** — erstelle einen Ordner wie `~/Documents/Mind++`
- **Automatisch in der Cloud gesichert** — erstelle den Ordner in einem Cloud-synchronisierten Pfad: `~/Google Drive/Mind++`, `~/OneDrive/Mind++`, `~/Dropbox/Mind++` oder `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++` (iCloud). Obsidian und Cowork lesen dieselben Dateien, und der Cloud-Dienst versioniert und synchronisiert zu allen deinen Geräten.
- **Power-User-Weg** — nutze das [Obsidian Git Plugin](https://github.com/Vinzent03/obsidian-git), um dein Vault in einem privaten GitHub-Repo zu versionieren (gibt dir Commit-Historie, Rollback und Android/iOS-Sync über die Obsidian Mobile App)

> Siehe die [Sync Strategies-Seite im Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) für Trade-offs und eine Empfehlung pro Anwendungsfall.

### 3. Installiere das Mind++ Plugin

1. Lade die neueste [`mind-plus-plus.plugin`](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)-Datei herunter
2. Öffne Claude Cowork → **Plugins**
3. Ziehe die `.plugin`-Datei in den Plugin-Bereich (oder klicke auf Installieren)

### 4. Wähle deinen Vault-Ordner in Cowork

Wähle in Claude Cowork den in Schritt 2 gewählten Ordner als deinen Workspace. Claude liest und schreibt direkt darin.

### 5. Führe das Setup aus

Sag Claude:

> **„richte mein zweites Gehirn ein"**

Das Setup fragt nach deinem Arbeitskontext (Kunden, Produkte, Tools), erstellt die Ordnerstruktur, schreibt ein personalisiertes `CLAUDE.md` und bietet an, Daily Brief und Weekly Review zu planen.

### 6. Fang an, es zu benutzen

- Sag **„brief"** jeden Morgen → Claude zeigt die heutige Agenda, überfällige Aufgaben und Follow-ups
- Sag **„ich hatte gerade ein Meeting mit X"** nach jedem Call → Claude schreibt die Notiz und aktualisiert deine Aufgaben
- Sag **„weekly review"** jeden Freitag → Claude konsolidiert die Woche

Das war's. Je mehr du es benutzt, desto mehr wird dein Vault zu einem echten zweiten Gehirn.

---

## Was im Plugin drin ist

### 12 Skills

| Skill | Was sie tut | Beispiel-Trigger |
|-------|------------|-----------------|
| `setup-mind-plus-plus` | Bootstrap deines Vaults von Null | „richte mein zweites Gehirn ein" |
| `user-profile` | Erfasst dein berufliches und persönliches Profil | „aktualisiere mein Profil" |
| `new-meeting` | Verwandelt Transkripte oder Notizen in strukturierte Meeting-Einträge mit Action Items | „ich hatte ein Meeting mit X" |
| `meeting-prep` | Vor-Meeting-Briefing — letzte Meetings, offene Aufgaben, Gesprächspunkte | „bereite mich aufs Meeting mit X vor" |
| `capture-idea` | Schnelle Ideenerfassung mit wenig Reibung, automatisch klassifiziert | „notier das: …" |
| `new-decision` | Dokumentiert einen Architecture Decision Record (ADR) im richtigen Scope | „eine Entscheidung festhalten" |
| `knowledge-search` | Semantische Suche im Vault mit Synthese und Quellenlinks | „was weiß ich über X" |
| `stakeholder-update` | Externes Status-Update für Kunde, Produkt oder Projekt | „Status-Update zu X" |
| `daily-brief` | Morgendliches Briefing: Agenda, überfällige Aufgaben, Follow-ups | „brief" |
| `weekly-review` | Freitags-Konsolidierung: was erledigt, was gefährdet, was kommt | „weekly review" |
| `process-inbox` | Triagiert Dateien ohne Heimat, schlägt ein Ziel vor, wartet auf Bestätigung | „inbox verarbeiten" |
| `process-meeting-emails` | Automatische Pipeline: Gemini / Fireflies / Otter E-Mails → strukturierte Notizen | „Meeting-Pipeline ausführen" |

### 2 Agents

Agents sind autonome Subprozesse, die in isoliertem Kontext laufen und ein sauberes Ergebnis zurückgeben.

| Agent | Was er tut | Wann er läuft |
|-------|-----------|--------------|
| `vault-researcher` | Tiefes Lesen über viele Dateien, ohne die Hauptkonversation zu überladen | Automatisch, wenn `knowledge-search` >15 Dateien matcht |
| `vault-auditor` | Kompletter Vault-Gesundheitscheck: überfällige Aufgaben, stille Kunden, Waisen-Dateien, alte Entscheidungen | Auf Abruf („audit my vault") oder wöchentlich geplant |

### Geplante Aufgaben

Cowork kann jede Skill auf einem Schedule ausführen. Das Setup bietet an, diese zu erstellen:

| Aufgabe | Standard-Schedule | Skill |
|---------|------------------|-------|
| Daily Brief | 8:00 Uhr, werktags | `daily-brief` |
| Weekly Review | 17:00 Uhr, freitags | `weekly-review` |
| E-Mail-Pipeline | Alle 2 Stunden | `process-meeting-emails` |
| Vault-Audit | 9:00 Uhr, montags | agent `vault-auditor` |

Du kannst Schedules jederzeit erstellen, bearbeiten oder entfernen — frag einfach Claude.

---

## Wie dein Vault organisiert wird

Mind++ erstellt und pflegt diese Struktur. Du musst sie nicht auswendig lernen — Claude weiß, wo was hingehört.

```
clients/{kunde}/        ← ein Ordner pro Kunde
  {Kunde}.md            ← Dashboard mit Kontakten, aktiven Projekten, Status
  meetings/             ← YYYY-MM-DD Titel.md
  decisions/            ← ADRs — NNN Titel.md
  references/           ← Briefings, Spreadsheets, Support-Docs
  Tasks {Kunde}.md      ← Tracker für offene Aufgaben

products/{produkt}/     ← deine eigenen Produkte (falls vorhanden)
operational/            ← interne Arbeit, Team, Config
personal/               ← persönliche Projekte, Ziele, Notizen
shared/                 ← Templates, Prompts, Anhänge
inbox/                  ← unsichere Items — Triage mit process-inbox
archive/                ← abgeschlossene Items — hierher verschoben, nie gelöscht
```

Mehr Details im [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki).

---

## Privatsphäre

Alles bleibt auf deinem Computer. Mind++ sendet deine Daten nirgendwohin. Die einzigen involvierten externen Dienste sind die, die du explizit in Cowork verbindest (z. B. Gmail für die Meeting-Pipeline, Google Calendar für den Daily Brief) — und die sind opt-in.

Wenn du Obsidian Git oder einen Cloud-synchronisierten Ordner (Drive, OneDrive, Dropbox, iCloud) nutzt, werden deine Notizen zu diesem Dienst repliziert — aber du hast ihn gewählt und du kontrollierst ihn.

Dein Nutzerprofil und Erinnerungen leben lokal in einem versteckten `.auto-memory/`-Ordner im Vault.

---

## Häufig gestellte Fragen

Kurze Liste — vollständige FAQ im [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/FAQ).

**Muss ich Markdown können?** Nein. Claude schreibt das Markdown für dich. Du sprichst in natürlicher Sprache.

**Kann ich es ohne Obsidian nutzen?** Ja — das Plugin braucht nur den Ordner. Obsidian ist dringend empfohlen, weil Graph View und Backlinks den Vault navigierbar machen, aber technisch kannst du die Dateien in jedem Editor öffnen.

**Kann ich es in einer anderen Sprache als Englisch nutzen?** Ja. Sag Claude deine bevorzugte Sprache beim Setup (oder jederzeit), und er schreibt Notizen, Briefs und Reviews in dieser Sprache. Die Ordnerstruktur des Plugins nutzt englische Namen per Design (für Portabilität), aber dein Inhalt ist in deiner Sprache.

**Was, wenn ich schon Notizen in Obsidian habe?** Richte Mind++ auf dein bestehendes Vault. Das Setup erkennt bestehende Dateien und integriert, statt zu überschreiben.

**Wie kriege ich meine Notizen aufs Handy?** Nutze Obsidian Git (synchronisiert mit einem privaten GitHub-Repo, den du über die Obsidian Mobile App erreichst), oder leg dein Vault in einen Cloud-Ordner (Drive / OneDrive / Dropbox / iCloud) und öffne ihn auf deinem Handy.

---

## Credits

**Mitverfasst von** [Felipe Venturini](https://github.com/felipe-venturini) und [sioux1to1](https://github.com/sioux1to1).

Gebaut mit [Claude](https://claude.ai) von Anthropic. Angetrieben von [Claude Cowork](https://claude.ai/download) und inspiriert von der [Obsidian](https://obsidian.md)-Community.

---

## Mitwirken

Mind++ ist Open Source unter der MIT-Lizenz. Beiträge sind willkommen.

- **Bug-Reports und Feature-Requests** → [eröffne ein Issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Code-Beiträge** → siehe [CONTRIBUTING.md](CONTRIBUTING.md)
- **Übersetzungen** → füge eine `README.{sprache}.md`-Datei hinzu und öffne einen PR
- **Neue Skills** → folge dem Format in `skills/*/SKILL.md` und öffne einen PR

---

## Lizenz

MIT — frei zur Nutzung, Änderung, Verteilung und kommerziellen Nutzung. Siehe [LICENSE](LICENSE).
