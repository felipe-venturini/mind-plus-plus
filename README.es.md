# Mind++ for Claude

**Tu segundo cerebro, impulsado por Claude — dentro de Obsidian.**

> 🌍 También disponible en: [English](README.md) · [Português (BR)](README.pt-BR.md)

Mind++ es un plugin de código abierto para Claude Cowork que transforma a Claude en un compañero de conocimiento proactivo. Captura reuniones, rastrea compromisos, entrega briefings diarios y mantiene una base de conocimiento viva para tu vida profesional y personal — todo almacenado como Markdown simple en tu vault de Obsidian.

---

## ¿Por qué Mind++?

- **Sin dependencia de plataforma** — tus datos son archivos `.md` simples, legibles en cualquier lugar
- **Privacidad por defecto** — todo se queda en tu carpeta, en tu computadora
- **Nativo en Obsidian** — wikilinks, frontmatter y estructura de vault que ya conoces
- **IA procesa, tú confirmas** — ningún archivo se mueve sin tu aprobación
- **Proactivo, no reactivo** — muestra tareas vencidas y clientes sin contacto sin que tengas que preguntar

---

## Skills incluidas

| Skill | Descripción | Disparador |
|-------|-------------|------------|
| `setup` | Bootstrap del vault desde cero — crea estructura de carpetas, archivos de configuración y un `CLAUDE.md` personalizado | "configurar mi segundo cerebro", "setup del vault" |
| `user-profile` | Captura y actualiza tu perfil profesional y personal para que Claude conozca tu contexto | "actualizar mi perfil", "Claude, conóceme" |
| `new-meeting` | Procesa cualquier reunión — transcripción, notas brutas o relato verbal — en nota estructurada con acciones | "tuve una reunión con X", "procesa esta transcripción" |
| `meeting-prep` | Briefing previo a la reunión — últimas actas, tareas abiertas, lo que debes, lo que te deben, puntos sugeridos | "prep para reunión con X", "qué hablar con X" |
| `capture-idea` | Captura rápida de ideas con baja fricción — clasifica el contexto automáticamente y guarda en la carpeta correcta (o inbox si hay duda) | "anota esto", "idea:", "guarda esta nota" |
| `new-decision` | Registra un ADR — contexto, decisión, consecuencias y alternativas rechazadas — en el ámbito correcto | "registrar decisión", "nuevo ADR", "decidimos X" |
| `knowledge-search` | Búsqueda semántica en el vault — devuelve síntesis con wikilinks a las notas fuente | "qué sé sobre X", "todo lo que hablamos de Y" |
| `stakeholder-update` | Genera un status report externo para cliente, producto o proyecto a partir del vault | "update del cliente X", "status report para X" |
| `daily-brief` | Briefing matinal con agenda del día, tareas vencidas y follow-ups pendientes | "brief", "qué tengo hoy" |
| `weekly-review` | Consolidación del viernes — qué se hizo, qué está en riesgo, qué viene | "weekly review", "cierra la semana" |
| `process-inbox` | Clasificación de archivos sin destino — propone destino y espera confirmación antes de mover | "procesar inbox", "clasificar archivos" |
| `process-meeting-emails` | Pipeline automático: emails de Gemini Meeting Notes / Fireflies / Otter → notas en el vault | "procesa los emails de Gemini", "pipeline de reuniones" |

---

## Agents incluidos

Los agents son subprocesos autónomos que se ejecutan en contexto aislado. Mind++ incluye dos:

| Agent | Qué hace | Cuándo se ejecuta |
|-------|----------|-------------------|
| `vault-researcher` | Lectura profunda de muchos archivos del vault — devuelve síntesis limpia sin saturar la conversación principal | Invocado automáticamente por `knowledge-search` cuando la búsqueda supera los 15 archivos |
| `vault-auditor` | Health check completo del vault — tareas vencidas, clientes silenciosos, dashboards desactualizados, archivos huérfanos, ADRs obsoletos | A demanda ("audita mi vault"), o agendado semanalmente |

---

## Tareas programadas

Cowork puede ejecutar cualquier skill en un cronograma — expresiones cron evaluadas en tu zona horaria local. La skill `setup` ofrece crear los schedules comunes:

| Tarea | Horario por defecto | Skill |
|-------|---------------------|-------|
| Daily brief | 8:00, días hábiles | `daily-brief` |
| Weekly review | 17:00, viernes | `weekly-review` |
| Pipeline de emails | Cada 2 horas | `process-meeting-emails` |
| Auditoría del vault | 9:00, lunes | agent `vault-auditor` |

Puedes crear, editar o eliminar schedules más tarde ("agenda el daily brief a las 7am" / "elimina la auditoría del vault"). Las tareas programadas solo se disparan cuando Cowork está corriendo en tu Mac — las tareas perdidas quedan en cola hasta la próxima sesión.

---

## Configuración recomendada

Mind++ está diseñado para funcionar con tres herramientas juntas:

### 1. Claude Cowork (obligatorio)
El plugin corre dentro de [Claude Cowork](https://claude.ai/download), la app de escritorio de Claude. Selecciona la carpeta de tu vault de Obsidian como workspace — Claude lee y escribe directamente en ella.

### 2. Obsidian (recomendado)
[Obsidian](https://obsidian.md) es la mejor forma de navegar y visualizar tu vault. Abre la misma carpeta seleccionada en Cowork. Obtienes graph view, búsqueda, tags y backlinks encima de todo lo que Claude escribe.

### 3. Obsidian Git (recomendado para versionado)
Instala el [plugin Obsidian Git de Vinzent03](https://github.com/Vinzent03/obsidian-git) para sincronizar automáticamente tu vault con un repositorio GitHub privado. Esto te da:
- Historial completo de versiones de cada nota
- Acceso móvil via app de Obsidian + sincronización con GitHub
- Respaldo y recuperación ante desastres

**Flujo recomendado:**
```
Claude Cowork  →  escribe archivos .md  →  tu carpeta del vault de Obsidian
Obsidian       →  lee la misma carpeta  →  navegación visual + graph
Obsidian Git   →  sincroniza con GitHub →  versionado + acceso móvil
```

---

## Primeros pasos

### 1. Instala el plugin
En Cowork, ve a **Plugins** e instala **Mind++ for Claude**.

### 2. Selecciona la carpeta del vault
En Cowork, selecciona la carpeta donde quieres que viva tu vault. Puede ser un vault de Obsidian existente o una carpeta nueva vacía.

### 3. Ejecuta el setup
Dile a Claude: **"configurar mi segundo cerebro"**

El setup:
- Detectará si empiezas desde cero o tienes archivos existentes
- Preguntará sobre tu contexto de trabajo (clientes, proyectos, herramientas)
- Creará la estructura de carpetas completa
- Generará archivos de configuración (mapeo de dominios, aliases de keywords)
- Escribirá un `CLAUDE.md` personalizado con tu contexto

### 4. Conecta herramientas externas (opcional)
En **Settings → Connectors**, conecta:
- **Google Calendar u Outlook** — para agenda en el daily brief
- **Gmail u Outlook** — para el pipeline automático de emails de reuniones
- **Google Drive** — para buscar transcripciones completas en la nube

### 5. Empieza a usarlo
Di "brief" cada mañana. Di "tuve una reunión con X" después de cada call. Di "weekly review" cada viernes.

---

## Privacidad

Todos tus datos se quedan en la carpeta que seleccionaste, en tu computadora. El plugin no envía datos a servidores externos más allá de las APIs que conectes (Google Calendar, Gmail, etc.).

---

## Contribuir

Mind++ es de código abierto bajo la licencia MIT. Las contribuciones son bienvenidas.

- **Bugs y sugerencias** → [abre un issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Contribuciones de código** → ver [CONTRIBUTING.md](CONTRIBUTING.md)
- **Traducciones** → agrega un archivo `README.{idioma}.md` y abre un PR
- **Nuevas skills** → sigue el formato en `skills/*/SKILL.md` y abre un PR

---

## Licencia

MIT — libre para usar, modificar, distribuir y comercializar. Ver [LICENSE](LICENSE).
