# Instalacao do Plugin Marketing-Adv-OS

Duas formas de instalar. Escolha a que funcionar.

---

## CAMINHO A — Claude Cowork (Desktop UI) — RECOMENDADO

1. Abrir Claude Desktop
2. Settings → Plugins
3. Se houver alguma versao anterior chamada `marketing-adv-os`, `marketing-adv-os-v3` ou similar, **DELETAR**
4. Clicar em "Add plugin" → "Upload"
5. Selecionar: `dist/Plugin-Marketing-Adv-OS-cowork-v0.1.0-alpha.3.zip`
6. Aguardar instalacao

Se aparecer **"Plugin validation failed"** mesmo assim, ir para o Caminho B.

---

## CAMINHO B — Claude Code CLI (Terminal) — FALLBACK GARANTIDO

Bypass completo do Cowork. Funciona em qualquer maquina onde Claude Code CLI esta instalado.

### B1. Carregar plugin para uma sessao (testar)

```bash
claude --plugin-dir <caminho-local-do-plugin>
```

Plugin fica ativo enquanto a sessao roda. Skills disponiveis via `/marketing-adv-os-v3:<nome-da-skill>`.

### B2. Instalar permanentemente (cli)

```bash
mkdir -p ~/.claude/plugins
ln -sfn <caminho-local-do-plugin> ~/.claude/plugins/marketing-adv-os-v3
```

Plugin disponivel em todas as sessoes do Claude Code CLI.

### B3. Testar uma skill

```bash
claude --plugin-dir <caminho-local-do-plugin>
# dentro da sessao:
/marketing-adv-os-v3:marketing-onboarding
```

---

## CAMINHO C — Se ambos A e B falharem

Marketplace do Cowork pode estar com estado ruim. Acoes:

1. Settings → Plugins → procurar "Manage marketplaces" → deletar marketplace `marketplace_014BgB8vebEXzMWM77HV8tXv`
2. Restart do Claude Desktop
3. Tentar Caminho A de novo (cria marketplace novo)

Se ainda assim falhar: o problema esta no backend Anthropic. Caminho B fica como solucao definitiva enquanto isso.

---

**Plugin instalado com sucesso:** invoque `/marketing-adv-os-v3:marketing-onboarding` (ou `/start-marketing` no caminho A) para iniciar o wizard.
