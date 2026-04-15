# Mind++ for Claude

**Seu segundo cérebro, potencializado pelo Claude — dentro do Obsidian.**

> 🌍 Também disponível em: [English](README.md) · [Español](README.es.md)

Mind++ é um plugin open-source para o Claude Cowork que transforma o Claude em um parceiro de conhecimento proativo. Ele captura reuniões, rastreia compromissos, entrega briefings diários e mantém uma base de conhecimento viva para sua vida profissional e pessoal — tudo armazenado como Markdown simples no seu vault do Obsidian.

---

## Por que Mind++?

- **Sem lock-in** — seus dados são arquivos `.md` simples, legíveis em qualquer lugar
- **Privacidade por padrão** — tudo fica na sua pasta, no seu computador
- **Nativo no Obsidian** — wikilinks, frontmatter e estrutura de vault que você já conhece
- **IA processa, você confirma** — nenhum arquivo é movido sem sua aprovação
- **Proativo, não reativo** — surfacing de tarefas vencidas e clientes sem contato sem precisar perguntar

---

## Skills incluídas

| Skill | Descrição | Gatilho |
|-------|-----------|---------|
| `setup` | Bootstrap do vault do zero — cria estrutura de pastas, arquivos de config e um `CLAUDE.md` personalizado | "configurar meu segundo cérebro", "setup do vault" |
| `user-profile` | Captura e atualiza seu perfil profissional e pessoal para que o Claude conheça seu contexto | "atualizar meu perfil", "Claude, me conheça" |
| `new-meeting` | Processa qualquer reunião — transcrição, notas brutas ou relato verbal — em nota estruturada com ações | "tive uma reunião com X", "processa essa transcrição" |
| `meeting-prep` | Briefing pré-reunião — últimas atas, tarefas abertas, o que você deve, o que devem a você, pautas sugeridas | "prep para reunião com X", "o que falar com X" |
| `capture-idea` | Captura rápida de ideia com baixa fricção — classifica contexto automaticamente e salva na pasta certa (ou inbox se incerto) | "anota isso", "ideia:", "salva essa nota" |
| `new-decision` | Registra um ADR — contexto, decisão, consequências e alternativas rejeitadas — no escopo certo | "registrar decisão", "novo ADR", "decidimos X" |
| `knowledge-search` | Busca semântica no vault — retorna síntese com wikilinks das notas fonte | "o que eu sei sobre X", "tudo que falamos sobre Y" |
| `stakeholder-update` | Gera status report externo de cliente, produto ou projeto a partir do vault | "update do cliente X", "status report para X" |
| `daily-brief` | Briefing matinal com agenda do dia, tarefas vencidas e follow-ups pendentes | "brief", "o que tenho hoje" |
| `weekly-review` | Consolidação de sexta — o que foi feito, o que está em risco, o que vem | "weekly review", "fecha a semana" |
| `process-inbox` | Triagem de arquivos sem destino — propõe destino e aguarda confirmação antes de mover | "processar inbox", "triagem de arquivos" |
| `process-meeting-emails` | Pipeline automático: emails do Gemini Meeting Notes / Fireflies / Otter → notas no vault | "processa os emails do Gemini", "pipeline de reuniões" |

---

## Agents inclusos

Agents são subprocessos autônomos que rodam em contexto isolado. O Mind++ vem com dois:

| Agent | O que faz | Quando roda |
|-------|-----------|-------------|
| `vault-researcher` | Leitura profunda em muitos arquivos do vault — retorna síntese limpa sem sobrecarregar a conversa principal | Invocado automaticamente pelo `knowledge-search` em buscas com >15 arquivos |
| `vault-auditor` | Health check completo do vault — tarefas vencidas, clientes silenciosos, dashboards desatualizados, arquivos órfãos, ADRs velhos | Sob demanda ("audita meu vault"), ou agendado semanalmente |

---

## Tarefas agendadas

O Cowork pode rodar qualquer skill em um schedule — expressões cron avaliadas no seu fuso local. A skill `setup` oferece criar os schedules comuns:

| Tarefa | Horário padrão | Skill |
|--------|----------------|-------|
| Daily brief | 8:00, dias úteis | `daily-brief` |
| Weekly review | 17:00, sexta | `weekly-review` |
| Pipeline de emails | A cada 2 horas | `process-meeting-emails` |
| Auditoria do vault | 9:00, segunda | agent `vault-auditor` |

Você pode criar, editar ou remover schedules depois ("agenda o daily brief às 7h" / "remove a auditoria do vault"). Tasks agendadas só disparam quando o Cowork está rodando no seu Mac — tasks perdidas ficam na fila até a próxima sessão.

---

## Setup recomendado

Mind++ foi projetado para funcionar com três ferramentas juntas:

### 1. Claude Cowork (obrigatório)
O plugin roda dentro do [Claude Cowork](https://claude.ai/download), o app do Claude para computador. Selecione a pasta do seu vault do Obsidian como workspace — o Claude lê e escreve diretamente nela.

### 2. Obsidian (recomendado)
O [Obsidian](https://obsidian.md) é a melhor forma de navegar e visualizar seu vault. Abra a mesma pasta selecionada no Cowork. Você ganha graph view, busca, tags e backlinks em cima de tudo que o Claude escreve.

### 3. Obsidian Git (recomendado para versionamento)
Instale o [plugin Obsidian Git do Vinzent03](https://github.com/Vinzent03/obsidian-git) para sincronizar automaticamente seu vault com um repositório GitHub privado. Isso oferece:
- Histórico completo de versões de cada nota
- Acesso mobile via app do Obsidian + sincronização com GitHub
- Backup e recuperação em caso de problemas

**Fluxo recomendado:**
```
Claude Cowork  →  escreve arquivos .md  →  sua pasta do vault Obsidian
Obsidian       →  lê a mesma pasta     →  navegação visual + graph
Obsidian Git   →  sincroniza com GitHub →  versionamento + acesso mobile
```

---

## Primeiros passos

### 1. Instale o plugin
No Cowork, vá em **Plugins** e instale o **Mind++ for Claude**.

### 2. Selecione a pasta do vault
No Cowork, selecione a pasta onde você quer que o vault viva. Pode ser um vault Obsidian existente ou uma pasta nova vazia.

### 3. Execute o setup
Diga ao Claude: **"configurar meu segundo cérebro"**

O setup irá:
- Detectar se você começa do zero ou tem arquivos existentes
- Perguntar sobre seu contexto de trabalho (clientes, projetos, ferramentas)
- Criar a estrutura de pastas completa
- Gerar arquivos de configuração (mapeamento de domínios, aliases de keywords)
- Escrever um `CLAUDE.md` personalizado com seu contexto

### 4. Conecte ferramentas externas (opcional)
Em **Settings → Connectors**, conecte:
- **Google Calendar ou Outlook** — para agenda no daily brief
- **Gmail ou Outlook** — para o pipeline automático de emails de reunião
- **Google Drive** — para buscar transcrições completas no cloud

### 5. Comece a usar
Diga "brief" toda manhã. Diga "tive uma reunião com X" depois de cada call. Diga "weekly review" toda sexta.

---

## Estrutura do vault

```
clients/{client}/
  {Client}.md               # Dashboard do cliente
  meetings/                 # YYYY-MM-DD Título.md
  decisions/                # ADRs — NNN Título.md
  references/               # Docs, briefings, planilhas
  Tasks {Client}.md

products/{product}/
  {Product}.md
  Tasks {Product}.md

operational/
  tasks/                    # Operational Tasks.md, Open Tasks.md
  config/                   # domain-mapping.yml, client-aliases.yml
  meetings/                 # Reuniões internas
  daily/                    # Briefs e reviews salvos
  decisions/                # ADRs organizacionais

personal/
  projects/
  learning/
  goals/
  notes/
  daily/

shared/
  templates/
  prompts/
  attachments/

inbox/                      # Caixa de entrada — triagem com process-inbox
archive/                    # Encerrados — movidos aqui, nunca deletados
```

---

## Privacidade

Todos os seus dados ficam na pasta que você selecionou, no seu computador. O plugin não envia dados para servidores externos além das APIs que você conectar (Google Calendar, Gmail, etc.).

---

## Contribuindo

Mind++ é open source sob a licença MIT. Contribuições são bem-vindas.

- **Bugs e sugestões** → [abra uma issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Contribuições de código** → veja [CONTRIBUTING.md](CONTRIBUTING.md)
- **Traduções** → adicione um arquivo `README.{idioma}.md` e abra um PR
- **Novas skills** → siga o formato em `skills/*/SKILL.md` e abra um PR

---

## Licença

MIT — livre para usar, modificar, distribuir e comercializar. Veja [LICENSE](LICENSE).
