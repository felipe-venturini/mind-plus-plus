# Mind++ for Claude

**Tu segundo cerebro, impulsado por Claude — dentro de Obsidian.**

> 🌍 Disponible en: [English](README.md) · [Português (BR)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [বাংলা](README.bn.md) · [Русский](README.ru.md) · [اردو](README.ur.md)
>
> 📖 **Docs completas y guías** → [GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki) · 🌐 **Sitio web** → [felipe-venturini.github.io/mind-plus-plus](https://felipe-venturini.github.io/mind-plus-plus)

Mind++ es un plugin gratuito y de código abierto para [Claude Cowork](https://claude.ai/download) que convierte a Claude en un compañero de conocimiento proactivo. Captura reuniones, rastrea compromisos, entrega briefings diarios y mantiene una base de conocimiento viva para tu vida profesional y personal — todo almacenado como Markdown simple dentro de un vault de [Obsidian](https://obsidian.md).

**Descargar el plugin → [última release](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)**

---

## ¿Nunca usaste esto? Empieza aquí.

Si nunca escuchaste sobre Obsidian ni escribiste una nota en Markdown, tranquilo. En un párrafo:

**Obsidian** es una app gratuita ([obsidian.md](https://obsidian.md)) que lee una carpeta de archivos `.md` (Markdown, texto plano) en tu computadora y los muestra como un cuaderno hermoso e interconectado. Como todo es texto simple, **tus notas son tuyas para siempre** — sin lock-in de nube, sin suscripción pagada, sin proveedor que pueda desaparecer. Mind++ usa la estructura de Obsidian como base porque es el formato más duradero y privado para conocimiento personal que existe hoy.

**Claude Cowork** es la app de escritorio de Claude ([claude.ai/download](https://claude.ai/download)) que puede leer y escribir archivos en tu computadora. Cuando instalas Mind++, Claude aprende una forma específica de organizar tus notas dentro de esa carpeta — así, cuando dices "tuve una reunión con Juan", escribe el acta, extrae las acciones y actualiza tu lista de pendientes automáticamente.

**No necesitas ser desarrollador.** No necesitas saber Git. No necesitas saber YAML. Mind++ se encarga de la estructura; tú solo hablas con Claude.

---

## ¿Por qué Mind++?

- **Sin lock-in** — tus datos son archivos `.md` puros, legibles en cualquier editor, en cualquier lugar
- **Privacidad por defecto** — todo se queda en tu carpeta, en tu máquina
- **Nativo en Obsidian** — graph view, backlinks, búsqueda y tags funcionan de fábrica
- **IA procesa, humano confirma** — Claude procesa, tú apruebas antes de cualquier movimiento o eliminación
- **Proactivo, no reactivo** — muestra tareas vencidas y clientes sin contacto sin que preguntes
- **Multilingüe** — el plugin funciona en el idioma que escribas; Claude se adapta a ti

---

## Inicio rápido en 5 minutos

> 👉 **¿Prefieres un paso a paso detallado?** → [Guía de Instalación en el Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Installation-Guide)

### 1. Instala las tres herramientas

| Herramienta | Qué hace | Link |
|-------------|----------|------|
| **Claude Cowork** (obligatorio) | La app de Claude que corre el plugin | [claude.ai/download](https://claude.ai/download) |
| **Obsidian** (muy recomendado) | Navegador visual de tus notas | [obsidian.md](https://obsidian.md) |
| **Tu opción de sync** (opcional) | Backup y acceso en cualquier lugar — elige una: [Obsidian Git](https://github.com/Vinzent03/obsidian-git), Google Drive, iCloud Drive, OneDrive o Dropbox | ver [Sync Strategies](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) |

### 2. Elige dónde vivirá tu vault

Elige una carpeta en tu computadora. Ahí se guardará cada nota, reunión y decisión.

- **Más simple** — crea una carpeta tipo `~/Documents/Mind++`
- **Con backup automático en la nube** — crea la carpeta dentro de una ubicación sincronizada: `~/Google Drive/Mind++`, `~/OneDrive/Mind++`, `~/Dropbox/Mind++` o `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++` (iCloud). Obsidian y Cowork leerán los mismos archivos, y el servicio de nube versiona y sincroniza a todos tus dispositivos.
- **Camino para usuario avanzado** — usa el [plugin Obsidian Git](https://github.com/Vinzent03/obsidian-git) para versionar tu vault en un repo privado de GitHub (te da historial de commits, rollback y sync Android/iOS vía la app mobile de Obsidian)

> Ver la [página Sync Strategies en el Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) para trade-offs y recomendación por caso de uso.

### 3. Instala el plugin Mind++

1. Descarga el archivo [`mind-plus-plus.plugin`](https://github.com/felipe-venturini/mind-plus-plus/releases/latest) más reciente
2. Abre Claude Cowork → **Plugins**
3. Arrastra el archivo `.plugin` al área de plugins (o haz clic en instalar)

### 4. Selecciona la carpeta del vault en Cowork

En Claude Cowork, selecciona la carpeta que elegiste en el paso 2 como tu workspace. Claude leerá y escribirá directamente en ella.

### 5. Corre el setup

Dile a Claude:

> **"configurar mi segundo cerebro"**

El setup preguntará sobre tu contexto de trabajo (clientes, productos, herramientas), creará la estructura de carpetas, escribirá un `CLAUDE.md` personalizado y ofrecerá agendar el daily brief y el weekly review.

### 6. Empieza a usarlo

- Di **"brief"** cada mañana → Claude muestra la agenda del día, tareas vencidas y follow-ups
- Di **"tuve una reunión con X"** después de cada call → Claude escribe el acta y actualiza tus pendientes
- Di **"weekly review"** cada viernes → Claude consolida la semana

Eso es todo. Mientras más lo uses, más se vuelve tu vault un verdadero segundo cerebro.

---

## Qué viene dentro del plugin

### 12 skills

| Skill | Qué hace | Ejemplo de gatillo |
|-------|----------|--------------------|
| `setup-mind-plus-plus` | Bootstrap del vault desde cero | "configurar mi segundo cerebro" |
| `user-profile` | Captura tu perfil profesional y personal | "actualizar mi perfil" |
| `new-meeting` | Convierte transcripciones o notas en actas estructuradas con acciones | "tuve una reunión con X" |
| `meeting-prep` | Briefing pre-reunión — últimas actas, tareas abiertas, temas | "prep para reunión con X" |
| `capture-idea` | Captura rápida de ideas con baja fricción, auto-clasificada | "anota esto: …" |
| `new-decision` | Registra un ADR (Architecture Decision Record) en el ámbito correcto | "registrar decisión" |
| `knowledge-search` | Búsqueda semántica en el vault con síntesis y links a las fuentes | "qué sé sobre X" |
| `stakeholder-update` | Status report externo para cliente, producto o proyecto | "update del cliente X" |
| `daily-brief` | Briefing matinal: agenda, tareas vencidas, follow-ups | "brief" |
| `weekly-review` | Consolidación de viernes: qué se hizo, qué está en riesgo, qué viene | "weekly review" |
| `process-inbox` | Triage de archivos sin destino, propone destino, espera confirmación | "procesar inbox" |
| `process-meeting-emails` | Pipeline automático: emails Gemini / Fireflies / Otter → notas estructuradas | "pipeline de reuniones" |

### 2 agents

Los agents son subprocesos autónomos que corren en contexto aislado y devuelven un resultado limpio.

| Agent | Qué hace | Cuándo corre |
|-------|----------|--------------|
| `vault-researcher` | Lectura profunda de muchos archivos sin saturar la conversación principal | Automáticamente, cuando `knowledge-search` encuentra >15 archivos |
| `vault-auditor` | Health check completo: tareas vencidas, clientes silenciosos, archivos huérfanos, decisiones viejas | A demanda ("audita mi vault") o agendado semanalmente |

### Tareas programadas

Cowork puede correr cualquier skill en un schedule. El setup ofrece crear:

| Tarea | Horario por defecto | Skill |
|-------|---------------------|-------|
| Daily brief | 8:00, días hábiles | `daily-brief` |
| Weekly review | 17:00, viernes | `weekly-review` |
| Pipeline de emails | Cada 2 horas | `process-meeting-emails` |
| Auditoría del vault | 9:00, lunes | agent `vault-auditor` |

Puedes crear, editar o eliminar schedules después — solo pídele a Claude.

---

## Cómo queda organizado tu vault

Mind++ crea y mantiene esta estructura. No necesitas memorizarla — Claude sabe dónde va cada cosa.

```
clients/{cliente}/      ← una carpeta por cliente
  {Cliente}.md          ← dashboard con contactos, proyectos activos, status
  meetings/             ← YYYY-MM-DD Título.md
  decisions/            ← ADRs — NNN Título.md
  references/           ← briefings, planillas, docs de apoyo
  Tasks {Cliente}.md    ← lista de pendientes

products/{producto}/    ← tus productos propios (si tienes)
operational/            ← trabajo interno, equipo, config
personal/               ← proyectos personales, metas, notas
shared/                 ← templates, prompts, adjuntos
inbox/                  ← items sin destino — triage con process-inbox
archive/                ← items cerrados — movidos aquí, nunca eliminados
```

Más detalle en el [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki).

---

## Privacidad

Todo se queda en tu computadora. Mind++ no envía tus datos a ningún lado. Los únicos servicios externos involucrados son los que conectes explícitamente en Cowork (por ejemplo, Gmail para el pipeline de reuniones, Google Calendar para el daily brief) — y son opt-in.

Si usas Obsidian Git o una carpeta sincronizada en la nube (Drive, OneDrive, Dropbox, iCloud), tus notas se replican a ese servicio — pero tú lo elegiste y tú lo controlas.

Tu perfil y memorias viven localmente en una carpeta oculta `.auto-memory/` dentro del vault.

---

## Preguntas frecuentes

Lista corta — FAQ completa en el [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/FAQ).

**¿Necesito saber Markdown?** No. Claude escribe el Markdown por ti. Tú hablas en lenguaje natural.

**¿Puedo usarlo sin Obsidian?** Sí — el plugin solo necesita la carpeta. Obsidian es muy recomendado porque el graph view y los backlinks hacen que el vault sea navegable, pero técnicamente puedes abrir los archivos en cualquier editor.

**¿Puedo usarlo en un idioma que no sea inglés?** Sí. Dile a Claude tu idioma preferido en el setup (o en cualquier momento), y escribirá actas, briefs y reviews en ese idioma. La estructura de carpetas del plugin usa nombres en inglés por diseño (para portabilidad), pero tu contenido está en tu idioma.

**¿Y si ya tengo notas en Obsidian?** Apunta Mind++ a tu vault existente. El setup detecta archivos existentes e integra, no sobrescribe.

**¿Cómo accedo a mis notas en el móvil?** Usa Obsidian Git (sincroniza con un repo privado de GitHub que accedes vía la app mobile de Obsidian), o pon el vault en una carpeta de nube (Drive / OneDrive / Dropbox / iCloud) y ábrela en tu teléfono.

---

## Créditos

**Co-autoría** de [Felipe Venturini](https://github.com/felipe-venturini) y [sioux1to1](https://github.com/sioux1to1).

Construido con [Claude](https://claude.ai) de Anthropic. Potenciado por [Claude Cowork](https://claude.ai/download) e inspirado por la comunidad [Obsidian](https://obsidian.md).

---

## Contribuir

Mind++ es open source bajo licencia MIT. Las contribuciones son bienvenidas.

- **Bugs y sugerencias** → [abre un issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Contribuciones de código** → ver [CONTRIBUTING.md](CONTRIBUTING.md)
- **Traducciones** → agrega un archivo `README.{idioma}.md` y abre un PR
- **Nuevas skills** → sigue el formato en `skills/*/SKILL.md` y abre un PR

---

## Licencia

MIT — libre para usar, modificar, distribuir y comercializar. Ver [LICENSE](LICENSE).
