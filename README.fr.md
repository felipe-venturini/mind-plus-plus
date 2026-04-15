# Mind++ for Claude

**Votre second cerveau, propulsé par Claude — à l'intérieur d'Obsidian.**

> 🌍 Disponible en : [English](README.md) · [Português (BR)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [বাংলা](README.bn.md) · [Русский](README.ru.md) · [اردو](README.ur.md)
>
> 📖 **Docs complètes et guides** → [GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki) · 🌐 **Site web** → [felipe-venturini.github.io/mind-plus-plus](https://felipe-venturini.github.io/mind-plus-plus)

Mind++ est un plugin gratuit et open-source pour [Claude Cowork](https://claude.ai/download) qui transforme Claude en un partenaire de connaissance proactif. Il capture les réunions, suit les engagements, livre des briefings quotidiens et maintient une base de connaissance vivante pour votre vie professionnelle et personnelle — le tout stocké en Markdown simple dans un vault [Obsidian](https://obsidian.md).

**Télécharger le plugin → [dernière release](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)**

---

## Jamais utilisé auparavant ? Commencez ici.

Si vous n'avez jamais entendu parler d'Obsidian ou écrit une note Markdown, pas de souci. En un paragraphe :

**Obsidian** est une application gratuite ([obsidian.md](https://obsidian.md)) qui lit un dossier de fichiers `.md` (Markdown, texte brut) sur votre ordinateur et les affiche comme un beau carnet interconnecté. Comme tout est en texte simple, **vos notes sont à vous pour toujours** — pas de verrouillage cloud, pas d'abonnement payant, pas de fournisseur qui peut disparaître. Mind++ utilise la structure d'Obsidian comme fondation car c'est le format le plus durable et privé pour la connaissance personnelle qui existe aujourd'hui.

**Claude Cowork** est l'application de bureau de Claude ([claude.ai/download](https://claude.ai/download)) qui peut lire et écrire des fichiers sur votre ordinateur. Quand vous installez Mind++, Claude apprend une façon spécifique d'organiser vos notes dans ce dossier — ainsi, quand vous dites « j'ai eu une réunion avec Jean », il écrit la note, extrait les actions et met à jour votre liste de tâches automatiquement.

**Vous n'avez pas besoin d'être développeur.** Pas besoin de connaître Git. Pas besoin de connaître YAML. Mind++ gère la structure ; vous parlez juste à Claude.

---

## Pourquoi Mind++ ?

- **Pas de verrouillage fournisseur** — vos données sont des fichiers `.md` simples, lisibles dans n'importe quel éditeur, partout
- **Confidentialité par défaut** — tout reste dans votre dossier, sur votre machine
- **Natif Obsidian** — graph view, backlinks, recherche et tags fonctionnent d'office
- **IA traite, humain valide** — Claude traite ; vous confirmez avant tout déplacement ou suppression
- **Proactif, pas réactif** — fait remonter les tâches en retard et les clients silencieux sans qu'on demande
- **Multilingue** — le plugin fonctionne dans la langue que vous écrivez ; Claude s'adapte à vous

---

## Démarrage rapide en 5 minutes

> 👉 **Vous préférez un pas-à-pas détaillé ?** → [Guide d'Installation sur le Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Installation-Guide)

### 1. Installez les trois outils

| Outil | Ce qu'il fait | Lien |
|-------|--------------|------|
| **Claude Cowork** (obligatoire) | L'app Claude qui fait tourner le plugin | [claude.ai/download](https://claude.ai/download) |
| **Obsidian** (fortement recommandé) | Navigateur visuel pour vos notes | [obsidian.md](https://obsidian.md) |
| **Votre choix de sync** (optionnel) | Sauvegarde et accès partout — choisissez-en un : [Obsidian Git](https://github.com/Vinzent03/obsidian-git), Google Drive, iCloud Drive, OneDrive ou Dropbox | voir [Sync Strategies](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) |

### 2. Choisissez où votre vault va vivre

Choisissez un dossier sur votre ordinateur. C'est là que chaque note, réunion et décision sera stockée.

- **Le plus simple** — créez un dossier comme `~/Documents/Mind++`
- **Sauvegarde automatique dans le cloud** — créez le dossier dans un emplacement synchronisé : `~/Google Drive/Mind++`, `~/OneDrive/Mind++`, `~/Dropbox/Mind++` ou `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++` (iCloud). Obsidian et Cowork liront les mêmes fichiers, et le service cloud versionne et synchronise sur tous vos appareils.
- **Voie utilisateur avancé** — utilisez le [plugin Obsidian Git](https://github.com/Vinzent03/obsidian-git) pour versionner votre vault dans un repo GitHub privé (vous donne historique des commits, rollback et sync Android/iOS via l'app mobile d'Obsidian)

> Voir la [page Sync Strategies sur le Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) pour les trade-offs et une recommandation par cas d'usage.

### 3. Installez le plugin Mind++

1. Téléchargez le dernier fichier [`mind-plus-plus.plugin`](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)
2. Ouvrez Claude Cowork → **Plugins**
3. Glissez le fichier `.plugin` dans la zone plugins (ou cliquez installer)

### 4. Sélectionnez le dossier de votre vault dans Cowork

Dans Claude Cowork, sélectionnez le dossier choisi à l'étape 2 comme votre workspace. Claude lira et écrira directement dedans.

### 5. Lancez le setup

Dites à Claude :

> **« configure mon second cerveau »**

Le setup vous demandera votre contexte de travail (clients, produits, outils), créera la structure de dossiers, écrira un `CLAUDE.md` personnalisé et proposera de planifier le daily brief et la weekly review.

### 6. Commencez à l'utiliser

- Dites **« brief »** chaque matin → Claude montre l'agenda du jour, les tâches en retard et les suivis
- Dites **« j'ai eu une réunion avec X »** après chaque appel → Claude écrit la note et met à jour vos tâches
- Dites **« weekly review »** chaque vendredi → Claude consolide la semaine

Voilà. Plus vous l'utilisez, plus votre vault devient un vrai second cerveau.

---

## Ce qu'il y a dans le plugin

### 12 skills

| Skill | Ce qu'elle fait | Exemple de déclencheur |
|-------|----------------|------------------------|
| `setup-mind-plus-plus` | Bootstrap du vault depuis zéro | « configure mon second cerveau » |
| `user-profile` | Capture votre profil professionnel et personnel | « mets à jour mon profil » |
| `new-meeting` | Transforme transcriptions ou notes en comptes-rendus structurés avec actions | « j'ai eu une réunion avec X » |
| `meeting-prep` | Briefing pré-réunion — dernières notes, tâches ouvertes, points de discussion | « prépare la réunion avec X » |
| `capture-idea` | Capture rapide d'idée à faible friction, auto-classée | « note ça : … » |
| `new-decision` | Enregistre un ADR (Architecture Decision Record) dans le bon scope | « enregistre une décision » |
| `knowledge-search` | Recherche sémantique dans le vault avec synthèse et liens sources | « que sais-je sur X » |
| `stakeholder-update` | Rapport de statut externe pour un client, produit ou projet | « status update sur X » |
| `daily-brief` | Briefing matinal : agenda, tâches en retard, suivis | « brief » |
| `weekly-review` | Consolidation du vendredi : fait, à risque, à venir | « weekly review » |
| `process-inbox` | Tri des fichiers sans destination, propose un emplacement, attend confirmation | « process inbox » |
| `process-meeting-emails` | Pipeline automatique : emails Gemini / Fireflies / Otter → notes structurées | « pipeline de réunions » |

### 2 agents

Les agents sont des sous-processus autonomes qui tournent en contexte isolé et renvoient un résultat propre.

| Agent | Ce qu'il fait | Quand il tourne |
|-------|--------------|----------------|
| `vault-researcher` | Lecture profonde de nombreux fichiers sans surcharger la conversation principale | Automatiquement, quand `knowledge-search` matche >15 fichiers |
| `vault-auditor` | Health check complet du vault : tâches en retard, clients silencieux, fichiers orphelins, décisions obsolètes | À la demande (« audite mon vault ») ou planifié hebdomadairement |

### Tâches planifiées

Cowork peut faire tourner n'importe quelle skill sur un schedule. Le setup propose de créer :

| Tâche | Horaire par défaut | Skill |
|-------|-------------------|-------|
| Daily brief | 8h00, jours ouvrés | `daily-brief` |
| Weekly review | 17h00, vendredi | `weekly-review` |
| Pipeline emails | Toutes les 2 heures | `process-meeting-emails` |
| Audit du vault | 9h00, lundi | agent `vault-auditor` |

Vous pouvez créer, modifier ou supprimer des schedules plus tard — demandez à Claude.

---

## Comment votre vault s'organise

Mind++ crée et maintient cette structure. Pas besoin de la mémoriser — Claude sait où va chaque chose.

```
clients/{client}/       ← un dossier par client
  {Client}.md           ← dashboard avec contacts, projets actifs, statut
  meetings/             ← YYYY-MM-DD Titre.md
  decisions/            ← ADRs — NNN Titre.md
  references/           ← briefings, tableurs, docs d'appui
  Tasks {Client}.md     ← tracker des tâches ouvertes

products/{produit}/     ← vos propres produits (si applicable)
operational/            ← travail interne, équipe, config
personal/               ← projets personnels, objectifs, notes
shared/                 ← templates, prompts, pièces jointes
inbox/                  ← items incertains — tri avec process-inbox
archive/                ← items fermés — déplacés ici, jamais supprimés
```

Plus de détails sur le [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki).

---

## Confidentialité

Tout reste sur votre ordinateur. Mind++ n'envoie vos données nulle part. Les seuls services externes impliqués sont ceux que vous connectez explicitement dans Cowork (par exemple, Gmail pour le pipeline de réunions, Google Calendar pour le daily brief) — et c'est opt-in.

Si vous utilisez Obsidian Git ou un dossier cloud-synced (Drive, OneDrive, Dropbox, iCloud), vos notes sont répliquées vers ce service — mais vous l'avez choisi et vous le contrôlez.

Votre profil et vos mémoires vivent localement dans un dossier caché `.auto-memory/` dans le vault.

---

## Questions fréquentes

Liste courte — FAQ complète sur le [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/FAQ).

**Dois-je savoir Markdown ?** Non. Claude écrit le Markdown pour vous. Vous parlez en langage naturel.

**Puis-je l'utiliser sans Obsidian ?** Oui — le plugin a juste besoin du dossier. Obsidian est fortement recommandé parce que le graph view et les backlinks rendent le vault navigable, mais techniquement vous pouvez ouvrir les fichiers dans n'importe quel éditeur.

**Puis-je l'utiliser dans une langue autre que l'anglais ?** Oui. Dites à Claude votre langue préférée au setup (ou à tout moment), et il écrira notes, briefs et reviews dans cette langue. La structure de dossiers du plugin utilise des noms anglais par design (pour la portabilité), mais votre contenu est dans votre langue.

**Et si j'ai déjà des notes dans Obsidian ?** Pointez Mind++ sur votre vault existant. Le setup détecte les fichiers existants et intègre, il n'écrase pas.

**Comment avoir mes notes sur mobile ?** Utilisez Obsidian Git (synchronise avec un repo GitHub privé accessible via l'app mobile d'Obsidian), ou mettez votre vault dans un dossier cloud (Drive / OneDrive / Dropbox / iCloud) et ouvrez-le sur votre téléphone.

---

## Crédits

**Co-écrit par** [Felipe Venturini](https://github.com/felipe-venturini) et [sioux1to1](https://github.com/sioux1to1).

Construit avec [Claude](https://claude.ai) d'Anthropic. Propulsé par [Claude Cowork](https://claude.ai/download) et inspiré par la communauté [Obsidian](https://obsidian.md).

---

## Contribuer

Mind++ est open source sous licence MIT. Les contributions sont bienvenues.

- **Bugs et suggestions** → [ouvrez une issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Contributions de code** → voir [CONTRIBUTING.md](CONTRIBUTING.md)
- **Traductions** → ajoutez un fichier `README.{langue}.md` et ouvrez une PR
- **Nouvelles skills** → suivez le format dans `skills/*/SKILL.md` et ouvrez une PR

---

## Licence

MIT — libre d'usage, modification, distribution et commercialisation. Voir [LICENSE](LICENSE).
