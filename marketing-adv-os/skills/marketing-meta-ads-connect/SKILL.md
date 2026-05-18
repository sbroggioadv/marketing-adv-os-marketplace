---
name: marketing-meta-ads-connect
description: >
  MARKETING META ADS CONNECT — Guia setup do MCP terceiro `mukulsethi1990/meta-ads-mcp` (NAO oficial Anthropic) para integracao com Facebook Ads + Instagram Ads via API Meta Graph. Verifica instalacao existente, orienta passo a passo claude mcp add, valida credenciais (App ID + App Secret + Long-Lived Access Token + Ad Account ID), salva config em integrations.json + warning de privacidade obrigatorio. Pre-requisito de marketing-meta-ads-campaign. Use quando o operador disser conectar meta ads, instalar mcp meta, integrar facebook ads, integrar instagram ads, configurar meta business.
---

# MARKETING META ADS CONNECT

> Skill Tier 2 (Executor — Integracao Opt-in). Setup do MCP de Meta Ads.

## OBJETIVO

Conectar o workspace a uma conta Meta Business (Facebook + Instagram Ads) via MCP de terceiro, com validacao de credenciais e warning explicito de privacidade.

## DISCLAIMER OBRIGATORIO

> **ATENCAO — INTEGRACAO COM TERCEIRO:**
>
> `mukulsethi1990/meta-ads-mcp` NAO e MCP oficial Anthropic. E um MCP comunitario disponivel no GitHub. Anthropic NAO endossa nem responsabiliza por este MCP.
>
> Riscos potenciais:
> - Credenciais (App Secret + Access Token) sao manipuladas pelo MCP
> - MCP de terceiro pode ser deprecado sem aviso
> - Atualizacoes do MCP podem mudar comportamento
>
> ALTERNATIVAS:
> - Usar Meta Ads Manager diretamente (web/app oficial)
> - Aguardar Anthropic lancar MCP oficial (sem previsao em 2026-05)
>
> Prosseguindo? (s/n) — operador confirma riscos antes de instalar.

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Operador tem conta Meta Business com ad account ativo
3. Operador tem permissao de admin do ad account
4. Node 18+ instalado (MCPs typicamente sao Node)

## FLUXO

### 1. Verificar instalacao existente

```bash
# Listar MCPs configurados no workspace
claude mcp list 2>&1 | grep -i meta
```

Se ja instalado: pular para passo 5 (validacao).

### 2. Apresentar warning + checklist Meta Business

> "Antes de instalar, voce precisa preparar credenciais no Meta Business:
>
> 1. Acesse https://developers.facebook.com/apps/
> 2. Crie um App (ou use existente) — tipo: Business
> 3. Adicione produto: Marketing API
> 4. Capture: **App ID** e **App Secret** (em Settings > Basic)
> 5. Em Business Manager: capture **Ad Account ID** (em Business Settings > Ad Accounts; formato 'act_XXXXXXXXXX')
> 6. Gere **Long-Lived Access Token** (60 dias):
>    a. Acesse Graph API Explorer: https://developers.facebook.com/tools/explorer/
>    b. Selecione seu App
>    c. Permissions necessarias: `ads_management`, `ads_read`, `business_management`
>    d. Generate Token (curto prazo, 1-2h)
>    e. Trocar por long-lived: https://developers.facebook.com/tools/debug/accesstoken/
>
> Tem TODAS essas 4 credenciais (App ID + Secret + Ad Account ID + Long-Lived Token)? (s/n)"

Se nao: pausar fluxo, dar tempo de operador preparar.

### 3. Instalar MCP

```bash
# Adicionar MCP ao workspace (project-scope para nao contaminar global)
claude mcp add --scope project meta-ads \\
  npx -y @mukulsethi1990/meta-ads-mcp@latest

# Verificar instalacao
claude mcp list | grep meta-ads
```

Se falhar (NPM erro, pacote inexistente, etc):
> "Falha na instalacao do MCP. Verificar:
> - Acesso a npm: `npm ping`
> - Versao Node: `node -v` (>= 18)
> - Permissao de instalacao
> - URL alternativa do MCP: https://github.com/mukulsethi1990/meta-ads-mcp
>
> Caso persista, usar Meta Ads Manager direto (web) e voltar a esta skill quando MCP corrigir."

### 4. Configurar credenciais

Cada MCP tem seu metodo. Para `meta-ads-mcp`, tipicamente envs:

```bash
# Editar .mcp.json do workspace (NUNCA commitar)
cat > <cwd>/.mcp.json <<EOF
{
  "mcpServers": {
    "meta-ads": {
      "command": "npx",
      "args": ["-y", "@mukulsethi1990/meta-ads-mcp@latest"],
      "env": {
        "META_APP_ID": "...",
        "META_APP_SECRET": "...",
        "META_ACCESS_TOKEN": "...",
        "META_AD_ACCOUNT_ID": "act_..."
      }
    }
  }
}
EOF

# Garantir que .mcp.json esta em .gitignore (credenciais NUNCA versionar)
grep -q "^.mcp.json$" .gitignore || echo ".mcp.json" >> .gitignore
```

### 5. Validar conexao

```bash
# Testar o MCP via claude
claude mcp test meta-ads
# OU rodar pergunta simples: "use meta-ads para listar minhas campanhas ativas"
```

Se OK: registrar config em `<cwd>/marketing/integrations.json`:

```json
{
  "meta_ads": {
    "status": "connected",
    "mcp_name": "meta-ads",
    "ad_account_id_masked": "act_***456789",
    "connected_at": "2026-05-17T17:00:00Z",
    "token_expires": "2026-07-16T17:00:00Z (long-lived 60d)",
    "permissions_granted": ["ads_management", "ads_read", "business_management"]
  }
}
```

### 6. Encerramento

```
OK Meta Ads MCP conectado.

INTEGRATIONS.json atualizado em <cwd>/marketing/integrations.json
Status: connected
Ad Account: act_***456789 (mascarado)
Token expira em: 60 dias (re-gerar pelo Graph API Explorer)

PROXIMOS PASSOS:
- Usar `marketing-meta-ads-campaign` para criar campanha real
- Token expira em 60 dias — agendar regeneracao
- Para revogar: claude mcp remove meta-ads
- Auditoria de uso: ver logs em <cwd>/.mcp-logs/meta-ads.log (se MCP loga)

WARNINGS PERSISTENTES:
- MCP de terceiro — verificar updates periodicamente
- Credenciais em .mcp.json — NUNCA versionar
- Long-lived token = ataque possivel se exposto — revogar imediatamente se vazado
```

## OUTPUT

MCP conectado + integrations.json atualizado + plano de regeneracao + warnings.

## VEDACOES ESPECIFICAS

- **NUNCA versionar .mcp.json** com credenciais reais
- **NUNCA armazenar Access Token em arquivo nao-gitignored**
- **NUNCA prosseguir sem confirmacao explicita do warning de terceiro**
- **VE-08, VE-09 (LGPD):** se o MCP processa dados de leads, garantir base legal + consentimento

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — verificacao de credenciais antes
- **2.4 Compliance** — disclaimer obrigatorio de MCP terceiro
