#!/bin/bash
# Mind++ for Claude — Criar repositório GitHub e fazer push inicial
# Execute este script no terminal do seu Mac na pasta do plugin

set -e

echo "🚀 Criando repositório mind-plus-plus no GitHub..."

# Cria o repositório público no GitHub
gh repo create felipe-venturini/mind-plus-plus \
  --public \
  --description "Your second brain, powered by Claude — inside Obsidian. Open-source Cowork plugin for PKM, meetings, and knowledge management." \
  --homepage "https://github.com/felipe-venturini/mind-plus-plus" \
  --source . \
  --remote origin \
  --push

echo ""
echo "✅ Pronto! Repositório criado em:"
echo "   https://github.com/felipe-venturini/mind-plus-plus"
echo ""
echo "Próximos passos sugeridos:"
echo "  1. Adicione tópicos no GitHub: obsidian, pkm, claude, cowork, second-brain"
echo "  2. Adicione uma descrição social (Settings → Social Preview)"
echo "  3. Habilite Issues e Discussions para a comunidade"
