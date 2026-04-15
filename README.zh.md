# Mind++ for Claude

**你的第二大脑，由 Claude 驱动 —— 在 Obsidian 中。**

> 🌍 可用语言：[English](README.md) · [Português (BR)](README.pt-BR.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [中文](README.zh.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md) · [বাংলা](README.bn.md) · [Русский](README.ru.md) · [اردو](README.ur.md)
>
> 📖 **完整文档和指南** → [GitHub Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki) · 🌐 **网站** → [felipe-venturini.github.io/mind-plus-plus](https://felipe-venturini.github.io/mind-plus-plus)

Mind++ 是 [Claude Cowork](https://claude.ai/download) 的免费开源插件，将 Claude 转变为主动的知识伙伴。它捕捉会议、追踪承诺、交付每日简报，并为你的职业和个人生活维护一个活的知识库 —— 全部以纯 Markdown 存储在 [Obsidian](https://obsidian.md) vault 中。

**下载插件 → [最新版本](https://github.com/felipe-venturini/mind-plus-plus/releases/latest)**

---

## 从未用过？从这里开始。

如果你从未听说过 Obsidian 或写过 Markdown 笔记，别担心。一段话解释：

**Obsidian** 是一个免费应用（[obsidian.md](https://obsidian.md)），它读取你电脑上的 `.md`（Markdown，纯文本）文件夹，并将其显示为一个漂亮的互联笔记本。因为一切都是纯文本，**你的笔记永远属于你** —— 没有云端锁定，没有付费订阅，没有可能消失的供应商。Mind++ 使用 Obsidian 的文件夹结构作为基础，因为它是当今存在的最持久、最私密的个人知识格式。

**Claude Cowork** 是 Claude 的桌面应用（[claude.ai/download](https://claude.ai/download)），可以读写你电脑上的文件。当你安装 Mind++ 时，Claude 会学会在该文件夹中组织笔记的特定方式 —— 这样当你说"我和张三开了个会"时，它会写笔记、提取行动项并自动更新你的任务列表。

**你不需要是开发者。** 不需要懂 Git。不需要懂 YAML。Mind++ 处理结构；你只需要和 Claude 对话。

---

## 为什么选择 Mind++？

- **无供应商锁定** —— 你的数据是纯 `.md` 文件，可以在任何地方的任何编辑器中读取
- **默认隐私** —— 一切都保留在你的文件夹中，在你的机器上
- **Obsidian 原生** —— 图谱视图、反向链接、搜索和标签开箱即用
- **AI 处理，人类确认** —— Claude 处理；在任何移动或删除之前你确认
- **主动而非被动** —— 无需询问即可浮现逾期任务和沉默客户
- **多语言** —— 插件适用于你使用的任何语言；Claude 会适应你

---

## 5 分钟快速开始

> 👉 **想要详细的分步指南？** → [Wiki 上的安装指南](https://github.com/felipe-venturini/mind-plus-plus/wiki/Installation-Guide)

### 1. 安装三个工具

| 工具 | 作用 | 链接 |
|------|------|------|
| **Claude Cowork**（必需） | 运行插件的 Claude 应用 | [claude.ai/download](https://claude.ai/download) |
| **Obsidian**（强烈推荐） | 笔记的可视化导航器 | [obsidian.md](https://obsidian.md) |
| **你的同步选择**（可选） | 备份并在任何地方访问 —— 选一个：[Obsidian Git](https://github.com/Vinzent03/obsidian-git)、Google Drive、iCloud Drive、OneDrive 或 Dropbox | 参见 [Sync Strategies](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) |

### 2. 选择 vault 存放位置

选择电脑上的一个文件夹。每个笔记、会议和决定都将存储在这里。

- **最简单** —— 创建类似 `~/Documents/Mind++` 的文件夹
- **自动云备份** —— 在云同步位置创建文件夹：`~/Google Drive/Mind++`、`~/OneDrive/Mind++`、`~/Dropbox/Mind++` 或 `~/Library/Mobile Documents/com~apple~CloudDocs/Mind++`（iCloud）。Obsidian 和 Cowork 会读取相同的文件，云服务会对其进行版本控制并同步到你的所有设备。
- **高级用户路径** —— 使用 [Obsidian Git 插件](https://github.com/Vinzent03/obsidian-git) 将你的 vault 版本化到私有 GitHub 仓库（提供提交历史、回滚以及通过 Obsidian 移动应用的 Android/iOS 同步）

> 参见 [Wiki 上的 Sync Strategies 页面](https://github.com/felipe-venturini/mind-plus-plus/wiki/Sync-Strategies) 了解权衡和每种用例的推荐。

### 3. 安装 Mind++ 插件

1. 下载最新的 [`mind-plus-plus.plugin`](https://github.com/felipe-venturini/mind-plus-plus/releases/latest) 文件
2. 打开 Claude Cowork → **Plugins**
3. 将 `.plugin` 文件拖入插件区域（或点击安装）

### 4. 在 Cowork 中选择你的 vault 文件夹

在 Claude Cowork 中，将你在第 2 步选择的文件夹作为工作空间。Claude 将直接读写它。

### 5. 运行 setup

告诉 Claude：

> **"设置我的第二大脑"**

Setup 会询问你的工作上下文（客户、产品、工具），创建文件夹结构，写入个性化的 `CLAUDE.md`，并提供安排每日简报和每周回顾。

### 6. 开始使用

- 每天早晨说 **"brief"** → Claude 显示今日议程、逾期任务和待跟进事项
- 每次通话后说 **"我刚和 X 开了会"** → Claude 写笔记并更新你的任务
- 每周五说 **"weekly review"** → Claude 整合这一周

就这样。你用得越多，vault 就越成为真正的第二大脑。

---

## 插件内容

### 12 个 skills

| Skill | 作用 | 触发示例 |
|-------|------|---------|
| `setup-mind-plus-plus` | 从零引导你的 vault | "设置我的第二大脑" |
| `user-profile` | 捕捉你的职业和个人档案 | "更新我的档案" |
| `new-meeting` | 将转录或笔记转为带行动项的结构化会议记录 | "我和 X 开了个会" |
| `meeting-prep` | 会前简报 —— 最近会议、未完成任务、讨论要点 | "为和 X 的会议做准备" |
| `capture-idea` | 低摩擦的快速想法捕捉，自动分类 | "记一下：……" |
| `new-decision` | 在正确范围记录架构决策记录（ADR） | "记录一个决定" |
| `knowledge-search` | 跨 vault 的语义搜索，带综合和来源链接 | "我对 X 了解什么" |
| `stakeholder-update` | 面向客户、产品或项目的外部状态报告 | "X 的状态更新" |
| `daily-brief` | 早晨简报：议程、逾期任务、待跟进 | "brief" |
| `weekly-review` | 周五整合：完成了什么、风险、即将到来 | "weekly review" |
| `process-inbox` | 分类无归属文件，提议目的地，等待确认 | "处理 inbox" |
| `process-meeting-emails` | 自动管道：Gemini / Fireflies / Otter 邮件 → 结构化笔记 | "运行会议管道" |

### 2 个 agents

Agents 是在隔离上下文中运行的自主子进程，返回干净的结果。

| Agent | 作用 | 何时运行 |
|-------|------|---------|
| `vault-researcher` | 跨多个文件深度阅读，不使主对话过载 | 自动，当 `knowledge-search` 匹配 >15 个文件时 |
| `vault-auditor` | 完整 vault 健康检查：逾期任务、沉默客户、孤立文件、陈旧决策 | 按需（"审计我的 vault"）或每周安排 |

### 定时任务

Cowork 可以按计划运行任何 skill。Setup 提供创建：

| 任务 | 默认时间 | Skill |
|------|---------|-------|
| Daily brief | 工作日上午 8:00 | `daily-brief` |
| Weekly review | 周五下午 5:00 | `weekly-review` |
| 邮件管道 | 每 2 小时 | `process-meeting-emails` |
| Vault 审计 | 周一上午 9:00 | agent `vault-auditor` |

你可以随时创建、编辑或删除计划 —— 直接告诉 Claude。

---

## 你的 vault 如何组织

Mind++ 创建并维护这个结构。你不需要记住它 —— Claude 知道每样东西放在哪里。

```
clients/{客户}/         ← 每个客户一个文件夹
  {客户}.md             ← 带联系人、活跃项目、状态的仪表板
  meetings/             ← YYYY-MM-DD 标题.md
  decisions/            ← ADRs —— NNN 标题.md
  references/           ← 简报、电子表格、支持文档
  Tasks {客户}.md       ← 未完成任务跟踪

products/{产品}/        ← 你自己的产品（如果有）
operational/            ← 内部工作、团队、配置
personal/               ← 个人项目、目标、笔记
shared/                 ← 模板、提示、附件
inbox/                  ← 不确定项 —— 用 process-inbox 分类
archive/                ← 已关闭项 —— 移到这里，从不删除
```

更多细节在 [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki)。

---

## 隐私

一切都留在你的电脑上。Mind++ 不会将你的数据发送到任何地方。唯一涉及的外部服务是你在 Cowork 中明确连接的服务（例如，用于会议邮件管道的 Gmail，用于每日简报的 Google Calendar）—— 这些都是选择加入的。

如果你使用 Obsidian Git 或云同步文件夹（Drive、OneDrive、Dropbox、iCloud），你的笔记会复制到该服务 —— 但那是你选择的，由你控制。

你的用户档案和记忆存放在 vault 内一个隐藏的 `.auto-memory/` 文件夹中。

---

## 常见问题

简短列表 —— 完整 FAQ 在 [Wiki](https://github.com/felipe-venturini/mind-plus-plus/wiki/FAQ)。

**我需要懂 Markdown 吗？** 不需要。Claude 会为你写 Markdown。你只需用自然语言交流。

**我可以不用 Obsidian 吗？** 可以 —— 插件只需要文件夹。强烈推荐 Obsidian，因为图谱视图和反向链接让 vault 变得可导航，但技术上你可以在任何编辑器中打开文件。

**我可以用英语以外的语言吗？** 可以。在 setup 时（或任何时候）告诉 Claude 你的首选语言，它会用该语言写笔记、简报和回顾。插件的文件夹结构按设计使用英文名称（为了可移植性），但你的内容是你的语言。

**如果我已经在 Obsidian 中有笔记怎么办？** 将 Mind++ 指向你现有的 vault。Setup 会检测现有文件并进行整合，而不是覆盖。

**我如何在手机上访问笔记？** 使用 Obsidian Git（同步到你可以通过 Obsidian 移动应用访问的私有 GitHub 仓库），或将你的 vault 放入云文件夹（Drive / OneDrive / Dropbox / iCloud）并在手机上打开它。

---

## 致谢

由 [Felipe Venturini](https://github.com/felipe-venturini) 和 [sioux1to1](https://github.com/sioux1to1) **共同创作**。

使用 Anthropic 的 [Claude](https://claude.ai) 构建。由 [Claude Cowork](https://claude.ai/download) 驱动，受 [Obsidian](https://obsidian.md) 社区启发。

---

## 贡献

Mind++ 是 MIT 许可证下的开源项目。欢迎贡献。

- **Bug 报告和功能请求** → [提交 issue](https://github.com/felipe-venturini/mind-plus-plus/issues)
- **代码贡献** → 参见 [CONTRIBUTING.md](CONTRIBUTING.md)
- **翻译** → 添加一个 `README.{语言}.md` 文件并开 PR
- **新 skills** → 遵循 `skills/*/SKILL.md` 格式并开 PR

---

## 许可证

MIT —— 可自由使用、修改、分发和商用。参见 [LICENSE](LICENSE)。
