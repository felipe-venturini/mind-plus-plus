# Mind++ for Claude

**Seu segundo cérebro, potencializado pelo Claude — dentro do Obsidian.**

> 🌍 Disponível em: [English](README.md) · [Português (BR)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [বাংলা](README.bn.md) · [Русский](README.ru.md) · [اردو](README.ur.md)
>
> 📖 **Docs completas e guias** → [GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki) · 🌐 **Site** → [felipe-venturini.github.io/mind-plus-plus](https://felipe-venturini.github.io/mind-plus-plus)

Mind++ é um plugin gratuito e open-source para o [Claude Cowork](https://claude.ai/download) que transforma o Claude em um parceiro de conhecimento proativo. Ele captura reuniões, rastreia compromissos, entrega briefings diários e mantém uma base de conhecimento viva para sua vida profissional e pessoal — tudo armazenado como Markdown simples dentro de um vault do [Obsidian](https://obsidian.md).

**Baixar o plugin → [release mais recente](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)**

---

## Nunca usou isso antes? Comece por aqui.

Se você nunca ouviu falar em Obsidian ou escreveu uma nota em Markdown, sem problema. Em um parágrafo:

**Obsidian** é um app gratuito ([obsidian.md](https://obsidian.md)) que lê uma pasta de arquivos `.md` (Markdown, texto puro) no seu computador e mostra como um caderno bonito e interconectado. Como tudo é texto simples, **suas notas são suas para sempre** — sem lock-in de nuvem, sem assinatura paga, sem fornecedor que pode desaparecer. O Mind++ usa a estrutura do Obsidian como base porque é o formato mais durável e privado para conhecimento pessoal que existe hoje.

**Claude Cowork** é o app de computador do Claude ([claude.ai/download](https://claude.ai/download)) que consegue ler e escrever arquivos na sua máquina. Quando você instala o Mind++, o Claude aprende um jeito específico de organizar suas notas dentro dessa pasta — assim, quando você diz "tive uma reunião com o João", ele escreve a ata, extrai os próximos passos e atualiza sua lista de pendências automaticamente.

**Você não precisa ser desenvolvedor.** Não precisa saber Git. Não precisa saber YAML. O Mind++ cuida da estrutura; você só conversa com o Claude.

---

## Por que Mind++?

- **Sem lock-in** — seus dados são arquivos `.md` puros, legíveis em qualquer editor, em qualquer lugar
- **Privacidade por padrão** — tudo fica na sua pasta, no seu computador
- **Nativo no Obsidian** — graph view, backlinks, busca e tags funcionam de fábrica
- **IA processa, humano confirma** — o Claude processa, você aprova antes de qualquer movimentação ou exclusão
- **Proativo, não reativo** — traz à tona tarefas vencidas e clientes sem contato sem precisar perguntar
- **Multilíngue** — o plugin funciona em qualquer idioma que você escreva; o Claude se adapta a você

---

## Início rápido em 5 minutos

> 👉 **Prefere um passo a passo detalhado?** → [Guia de Instalação no Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Installation-Guide)

### 1. Instale as três ferramentas

| Ferramenta | O que faz | Link |
|------------|-----------|------|
| **Claude Cowork** (obrigatório) | O app do Claude que roda o plugin | [claude.ai/download](https://claude.ai/download) |
| **Obsidian** (fortemente recomendado) | Navegador visual das suas notas | [obsidian.md](https://obsidian.md) |
| **Sua opção de sync** (opcional) | Backup e acesso em qualquer lugar — escolha uma: [Obsidian Git](https://github.com/Vinzent03/obsidian-git), Google Drive, iCloud Drive, OneDrive ou Dropbox | veja [Sync Strategies](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) |

### 2. Escolha onde o vault vai morar

Escolha uma pasta no seu computador. É aí que toda nota, reunião e decisão será guardada.

- **Mais simples** — crie uma pasta tipo `~/Documents/Mind++`
- **Com backup automático na nuvem** — crie a pasta dentro de um local sincronizado: `~/Google Drive/Mind++`, `~/OneDrive/Mind++`, `~/Dropbox/Mind++` ou `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++` (iCloud). O Obsidian e o Cowork vão ler os mesmos arquivos, e o serviço de nuvem versiona e sincroniza para todos os seus dispositivos.
- **Caminho para usuário avançado** — use o [plugin Obsidian Git](https://github.com/Vinzent03/obsidian-git) para versionar seu vault em um repo privado no GitHub (te dá histórico de commits, rollback e sync Android/iOS via o app mobile do Obsidian)

> Veja a [página Sync Strategies no Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) para trade-offs e recomendação por perfil de uso.

### 3. Instale o plugin Mind++

1. Baixe o arquivo [`mind-plus-plus.plugin`](https://github.com/felipe-venturini/mind-plus-plus/releases/latest) mais recente
2. Abra o Claude Cowork → **Plugins**
3. Arraste o arquivo `.plugin` para a área de plugins (ou clique em instalar)

### 4. Selecione a pasta do vault no Cowork

No Claude Cowork, selecione a pasta que você escolheu no passo 2 como seu workspace. O Claude vai ler e escrever diretamente nela.

### 5. Rode o setup

Diga ao Claude:

> **"configurar meu segundo cérebro"**

O setup vai perguntar sobre seu contexto de trabalho (clientes, produtos, ferramentas), criar a estrutura de pastas, escrever um `CLAUDE.md` personalizado e oferecer agendar o daily brief e o weekly review.

### 6. Comece a usar

- Diga **"brief"** toda manhã → o Claude mostra a agenda do dia, pendências vencidas e follow-ups
- Diga **"tive uma reunião com X"** depois de qualquer call → o Claude escreve a ata e atualiza suas pendências
- Diga **"weekly review"** toda sexta → o Claude consolida a semana

É isso. Quanto mais você usa, mais o vault vira um verdadeiro segundo cérebro.

---

## O que vem dentro do plugin

### 12 skills

| Skill | O que faz | Exemplo de gatilho |
|-------|-----------|--------------------|
| `setup-mind-plus-plus` | Faz o bootstrap do vault do zero | "configurar meu segundo cérebro" |
| `user-profile` | Captura seu perfil profissional e pessoal | "atualizar meu perfil" |
| `new-meeting` | Transforma transcrições ou notas em atas estruturadas com ações | "tive uma reunião com X" |
| `meeting-prep` | Briefing pré-reunião — últimas atas, tarefas abertas, pautas | "prep para reunião com X" |
| `capture-idea` | Captura rápida de ideia com baixa fricção, auto-classificada | "anota isso: …" |
| `new-decision` | Registra um ADR (Architecture Decision Record) no escopo certo | "registrar decisão" |
| `knowledge-search` | Busca semântica no vault com síntese e links das fontes | "o que eu sei sobre X" |
| `stakeholder-update` | Status report externo para cliente, produto ou projeto | "update do cliente X" |
| `daily-brief` | Briefing matinal: agenda, tarefas vencidas, follow-ups | "brief" |
| `weekly-review` | Consolidação de sexta: o que foi feito, o que está em risco, o que vem | "weekly review" |
| `process-inbox` | Triagem de arquivos sem destino, propõe onde vai, espera confirmação | "processar inbox" |
| `process-meeting-emails` | Pipeline automático: emails Gemini / Fireflies / Otter → notas estruturadas | "pipeline de reuniões" |

### 2 agents

Agents são subprocessos autônomos que rodam em contexto isolado e devolvem um resultado limpo.

| Agent | O que faz | Quando roda |
|-------|-----------|-------------|
| `vault-researcher` | Leitura profunda de vários arquivos sem sobrecarregar a conversa principal | Automaticamente, quando `knowledge-search` casa com >15 arquivos |
| `vault-auditor` | Health check completo: tarefas vencidas, clientes silenciosos, arquivos órfãos, decisões antigas | Sob demanda ("audita meu vault") ou agendado semanalmente |

### Tarefas agendadas

O Cowork pode rodar qualquer skill em um schedule. O setup oferece criar:

| Tarefa | Horário padrão | Skill |
|--------|----------------|-------|
| Daily brief | 8:00, dias úteis | `daily-brief` |
| Weekly review | 17:00, sexta | `weekly-review` |
| Pipeline de emails | A cada 2 horas | `process-meeting-emails` |
| Auditoria do vault | 9:00, segunda | agent `vault-auditor` |

Você pode criar, editar ou remover schedules depois — é só pedir ao Claude.

---

## Como seu vault fica organizado

Mind++ cria e mantém esta estrutura. Você não precisa decorar — o Claude sabe onde cada coisa vai.

```
clients/{cliente}/      ← uma pasta por cliente
  {Cliente}.md          ← dashboard com contatos, projetos ativos, status
  meetings/             ← YYYY-MM-DD Título.md
  decisions/            ← ADRs — NNN Título.md
  references/           ← briefings, planilhas, docs de apoio
  Tasks {Cliente}.md    ← lista de pendências

products/{produto}/     ← seus próprios produtos (se tiver)
operational/            ← trabalho interno, equipe, config
personal/               ← projetos pessoais, metas, notas
shared/                 ← templates, prompts, anexos
inbox/                  ← itens sem destino — triagem com process-inbox
archive/                ← itens encerrados — movidos para cá, nunca deletados
```

Mais detalhes no [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki).

---

## Privacidade

Tudo fica no seu computador. O Mind++ não envia seus dados para lugar nenhum. Os únicos serviços externos envolvidos são os que você conectar explicitamente no Cowork (por exemplo, Gmail para o pipeline de reuniões, Google Calendar para o daily brief) — e são opt-in.

Se você usar Obsidian Git ou uma pasta sincronizada na nuvem (Drive, OneDrive, Dropbox, iCloud), suas notas são replicadas para esse serviço — mas você escolheu e você controla.

Seu perfil e memórias ficam localmente em uma pasta oculta `.auto-memory/` dentro do vault.

---

## Perguntas frequentes

Lista curta — FAQ completo no [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/FAQ).

**Preciso saber Markdown?** Não. O Claude escreve o Markdown para você. Você conversa em linguagem natural.

**Posso usar sem Obsidian?** Pode — o plugin só precisa da pasta. O Obsidian é fortemente recomendado porque o graph view e os backlinks tornam o vault navegável, mas tecnicamente você pode abrir os arquivos em qualquer editor.

**Posso usar em outro idioma que não o inglês?** Sim. Diga ao Claude qual idioma você prefere no setup (ou a qualquer momento), e ele vai escrever atas, briefs e reviews nesse idioma. A estrutura de pastas do plugin usa nomes em inglês por design (para portabilidade), mas seu conteúdo é na sua língua.

**E se eu já tenho notas no Obsidian?** Aponte o Mind++ para o vault existente. O setup detecta arquivos existentes e integra, não sobrescreve.

**Como tenho as notas no celular?** Use Obsidian Git (sincroniza com um repo privado do GitHub que você acessa pelo app mobile do Obsidian), ou coloque o vault numa pasta de nuvem (Drive / OneDrive / Dropbox / iCloud) e abra no celular.

---

## Créditos

**Co-autoria** de [Felipe Venturini](https://github.com/felipe-venturini) e [sioux1to1](https://github.com/sioux1to1).

Construído com [Claude](https://claude.ai) da Anthropic. Potencializado pelo [Claude Cowork](https://claude.ai/download) e inspirado pela comunidade [Obsidian](https://obsidian.md).

---

## Contribuindo

Mind++ é open source sob licença MIT. Contribuições são bem-vindas.

- **Bugs e sugestões** → [abra uma issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **Contribuições de código** → veja [CONTRIBUTING.md](CONTRIBUTING.md)
- **Traduções** → adicione um arquivo `README.{idioma}.md` e abra um PR
- **Novas skills** → siga o formato em `skills/*/SKILL.md` e abra um PR

---

## Licença

MIT — livre para usar, modificar, distribuir e comercializar. Veja [LICENSE](LICENSE).
