---
name: marketing-postiz-publish
description: >
  MARKETING POSTIZ PUBLISH — Agenda peca em multiplas plataformas simultaneo via MCP Postiz (parte do marketplace claude-plugins-official). Suporta Instagram + Facebook + LinkedIn + X + TikTok + YouTube Shorts + Pinterest. Modo DRAFT obrigatorio por default — operador revisa antes de publicar. Track A: roda Diretoria R3 (Compliance OAB) ANTES de criar draft. Use quando o operador disser agendar post, publicar nas redes, postizpublish, multi-plataforma, agendamento, schedule post.
---

# MARKETING POSTIZ PUBLISH

> Skill Tier 2 (Executor — Integracao Opt-in). Agendamento multi-plataforma via Postiz.

## OBJETIVO

Agendar peca (post / carrossel / video / story) em multiplas plataformas via Postiz, em MODO DRAFT por default. Operador valida no Postiz dashboard antes de publicar.

## PRE-REQUISITOS

1. Plugin Postiz instalado no Claude Code (`claude plugin install postiz`)
2. Conta Postiz ativa (Cloud Standard ou Premium — Premium suporta mais plataformas)
3. Integracoes Postiz configuradas para cada plataforma destino (OAuth com IG/FB/LinkedIn/etc)
4. Peca pronta: copy + arte (PNG ou MP4)
5. Workspace + MEMORY configurado

## FLUXO

### 1. Verificar instalacao Postiz

```bash
claude mcp list | grep -i postiz
# OU
claude plugin list | grep -i postiz
```

Se nao instalado:
> "Plugin Postiz nao detectado. Instale:
> ```
> claude plugin install claude-plugins-official/postiz
> ```
>
> Depois conecte sua conta Postiz em claude.ai/settings/connectors (OAuth)."

### 2. Validar plataformas conectadas no Postiz

```
[via MCP Postiz]
mcp__postiz__integrationList

Retorna lista de plataformas conectadas:
- Instagram (@handle)
- Facebook (page name)
- LinkedIn (profile/company)
- X (handle)
- TikTok (handle)
- etc

Se plataforma desejada nao conectada: orientar configurar no postiz.com/launches
```

### 3. Briefing

> "Vou criar draft no Postiz. Confirme:
> - Plataformas alvo (multi-select dentre as conectadas): IG / FB / LinkedIn / X / TikTok / ...
> - Tipo de peca:
>   (a) post-imagem-unica (PNG)
>   (b) post-carrossel (multiplas PNGs)
>   (c) post-video (MP4)
>   (d) story (1 PNG por tela, sequencia)
>   (e) reels (MP4 9:16)
> - Path do arquivo de midia (PNG/MP4): [...]
> - Caption (texto que acompanha): [se nao tem, rodar marketing-copy-post-* antes]
> - Hashtags: max 10 (IG/FB) ou 5 (LinkedIn) ou conforme plataforma
> - Data/hora de publicacao: agora / agendado para [data + hora + timezone]
> - Modo: DRAFT (default — operador revisa) / SCHEDULED (vai publicar automaticamente no horario)"

### 4. Diretoria Criativa R3 OBRIGATORIO

```
RODANDO DIRETORIA CRIATIVA R3 ANTES DE AGENDAR:

Track A — OAB Provimento 205/2021:
- [ ] VE-04: caption nao promete resultado processual
- [ ] VE-05: tom institucional-informativo, nao mercantil
- [ ] VE-06: CTA nao e captacao agressiva
- [ ] VE-07: nao ofende colega/banca
- [ ] VE-15: cases citados tem autorizacao

Track B — CONAR:
- [ ] VE-10: sem comparativo desleal
- [ ] VE-12: dado/numero verificavel
- [ ] VE-13: parceria paga declarada (#publi obrigatorio em FB/IG conforme guidelines)

Universal:
- [ ] VE-01: sem superlativo sem prova
- [ ] VE-02: sem manipulacao ofensiva
- [ ] VE-13: parceria paga (#publi) se aplicavel
- [ ] VE-14: se peca foi gerada por IA em area sensivel, declarar
- [ ] LGPD: link de politica de privacidade visivel (se peca direciona pra LP com formulario)

Por plataforma:
- IG: max 30 hashtags, caption max 2200 chars, image ideal 1080x1350
- LinkedIn: max 5 hashtags, caption max 3000 chars
- X: caption max 280 chars (ou thread), hashtags max 3 inline
- TikTok/Reels: video 9:16, max 90s, audio sem watermark de outra plataforma
- FB: caption longa OK, mas primeiras 100 chars decidem expansao "ver mais"

Falha em qualquer item: BLOQUEIO. Reformular antes de agendar.
```

### 5. Criar draft via MCP Postiz

```
Para cada plataforma selecionada:

mcp__postiz__integrationSchedulePostTool \\
  --platform <ig|fb|linkedin|x|tiktok|...> \\
  --message <caption> \\
  --media <upload do PNG/MP4> \\
  --schedule_at <ISO timestamp> \\
  --draft true   # DRAFT MODE (NUNCA pular)

Retorno: { "post_id": "...", "draft_url": "https://postiz.com/launches/.../post/...", "scheduled_at": "..." }
```

### 6. Sumario para revisao

```
DRAFTS CRIADOS NO POSTIZ:

Plataformas: IG (@handle) + LinkedIn (company) + X (handle)
Agendado para: 2026-05-20 19:00 BRT

Drafts:
- IG: https://postiz.com/launches/.../post/abc123 [DRAFT]
- LinkedIn: https://postiz.com/launches/.../post/abc124 [DRAFT]
- X: https://postiz.com/launches/.../post/abc125 [DRAFT]

REVISAO MANUAL OBRIGATORIA:
1. Acessar cada draft no Postiz
2. Validar preview por plataforma (cada uma renderiza diferente)
3. Ajustar caption se necessario (cada plataforma tem tom otimo diferente)
4. Confirmar media renderizou corretamente (preview)
5. Confirmar horario do agendamento

ATIVAR PUBLICACAO:
- No Postiz dashboard: clicar 'Approve & Publish' em cada draft
- OU desde ja em modo Auto-Publish se confianca alta (NAO recomendado primeira vez)

REGISTRO em integrations.json:
{
  "postiz": {
    "drafts_history": [
      { "draft_id": "abc123", "platform": "instagram", "scheduled_at": "...", "diretoria_r3_passed": true },
      ...
    ]
  }
}
```

### 7. Workflow recomendado pre-publicacao

```
plugin gera arte/copy -> Diretoria R3 valida -> Postiz draft -> operador revisa -> publica

NUNCA pular nenhum passo. Especialmente Track A: 1 publicacao com VE-04 violada pode gerar denuncia OAB.
```

## OUTPUT

Drafts criados no Postiz + URLs pra revisao + checklist pre-publicacao + registro em integrations.json.

## VEDACOES ESPECIFICAS

- **NUNCA pular Diretoria R3** antes de criar draft — gasto e publicidade
- **NUNCA modo Auto-Publish em primeira publicacao** — sempre DRAFT
- **NUNCA peca em mesma caption identica em todas plataformas** — cada uma tem tom otimo (LinkedIn formal, IG visual, X conciso)
- **Track A: VE-04, VE-06 — CRITICAS**. Falha = BLOQUEIO + alerta vermelho
- **VE-13:** se ha parceria paga, #publi visivel nas primeiras 100 chars (regra Instagram/FB 2026)

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — plataformas + tipo + agendamento
- **2.3 Producao** — caption por plataforma adaptada
- **2.4 Compliance** — Diretoria R3 OBRIGATORIA pre-draft
- **2.5 Mensuracao** — UTMs nos links + analytics por plataforma
