---
name: marketing-email-broadcast
description: >
  MARKETING EMAIL BROADCAST — Envia broadcast de email marketing TOOL-AGNOSTIC via MCP do operador (categoria `~~email marketing` — Klaviyo, Mailchimp, Brevo, Resend, Customer.io, etc). Consome copy de email pre-produzido (marketing-copy-email-welcome / lancamento / upsell) + segmentacao + agendamento. Modo DRAFT por default. LGPD critica: opt-in obrigatorio + opt-out claro + base legal documentada. Track A: tom institucional (sem urgencia falsa em VE-05). Use quando o operador disser enviar broadcast, disparo de email, email para lista, email marketing, broadcast mailchimp/klaviyo/resend.
---

# MARKETING EMAIL BROADCAST

> Skill Tier 2 (Executor — Integracao Opt-in). Broadcast tool-agnostic.

## OBJETIVO

Disparar broadcast de email pra lista segmentada via MCP do operador (independente da plataforma — Klaviyo, Mailchimp, Brevo, Resend). Modo DRAFT garante revisao. LGPD critica (opt-in + opt-out + base legal).

## PRE-REQUISITOS

1. Workspace + MEMORY configurado
2. **Plataforma de email com MCP configurado:** Klaviyo, Resend, Mailchimp, Brevo, Customer.io etc — verificar `claude mcp list`
3. **Lista com opt-in valido** (LGPD — base legal documentada)
4. Copy do email pronto (rodar `marketing-copy-email-*` antes se nao tem)
5. Plataforma de envio tem dominio verificado (DKIM, SPF, DMARC) — caso contrario broadcast vai pra spam

## FLUXO

### 1. Detectar plataforma de email

```bash
claude mcp list | grep -iE "mailchimp|klaviyo|brevo|resend|customer|sendgrid"
```

Se nada:
> "Nenhum MCP de email marketing detectado. Opcoes:
> - Klaviyo: claude.ai/settings/connectors -> Klaviyo (OAuth oficial)
> - Mailchimp: instalar mcp-mailchimp ou usar conector claude.ai
> - Resend: instalar mcp-resend ou usar via API REST direto
> - Brevo: claude.ai/settings/connectors -> Brevo
> - Customer.io: idem
>
> Ou enviar broadcast manualmente pela dashboard da plataforma."

### 2. Validar lista + base legal

```
GATE LGPD OBRIGATORIO:

1. Lista tem base legal documentada para envio?
   (a) Consentimento explicito (opt-in com checkbox NAO pre-marcado) — preferido
   (b) Legitimo interesse documentado (cliente existente, contato comercial)
   (c) Outra base legal especifica
   (d) NAO TENHO CERTEZA -> BLOQUEIO. Documentar antes de enviar.

2. Qual a fonte da lista?
   - Formulario LP com opt-in
   - Lead magnet download
   - Compra/cliente existente
   - Lista comprada -> BLOQUEIO. Compra de lista viola LGPD + base legal nula.

3. Lista tem timestamp de opt-in?
   - SIM (idealmente em logs auditavel)
   - NAO -> documentar antes de prosseguir

4. Politica de privacidade publica?
   - URL: ___
   - Sem politica -> BLOQUEIO

5. Opt-out claro em TODO email?
   - SIM (link de descadastro visivel + funcional)
   - NAO -> BLOQUEIO
```

Se falhar qualquer item: NAO prosseguir. Documentar base legal antes.

### 3. Briefing

> "Vou criar broadcast em DRAFT. Confirme:
> - Plataforma de envio (qual MCP usar): klaviyo / mailchimp / resend / brevo / customer.io
> - Segmento da lista:
>   - Total opt-in valido (todos)
>   - Tag/segmento especifico (ex: 'baixou-ebook-X', 'cliente-curso-Y', 'cidade-sao-paulo')
> - Tipo de email:
>   (a) newsletter periodica (informativa)
>   (b) sequencia de welcome (rodar marketing-copy-email-welcome antes)
>   (c) lancamento (rodar marketing-copy-email-lancamento antes)
>   (d) upsell para cliente (rodar marketing-copy-email-upsell antes)
>   (e) anuncio pontual (post novo no blog, evento, etc)
> - Subject line + preview text (do email pronto)
> - HTML do email + versao texto-puro (fallback)
> - Hora de envio: agora / agendado para [timestamp + timezone]
> - Modo: DRAFT (recomendado) / SCHEDULED / SEND-NOW (PERIGOSO em primeira vez)"

### 4. Anti-spam check

```
CHECKLIST ANTI-SPAM (universal a TODA plataforma):

Subject line:
- [ ] Max 50 chars
- [ ] Sem CAPS LOCK
- [ ] Sem !!!
- [ ] Sem 'GRATIS' em capital
- [ ] Sem '100% off'
- [ ] Sem 'compre agora' / 'urgent' em capital

Conteudo:
- [ ] Texto-imagem ratio >= 60/40 (texto > imagem)
- [ ] Nunca enviar SO IMAGEM (vai pra spam imediato)
- [ ] Link de opt-out claro (texto + URL funcional)
- [ ] Pre-header text definido (Gmail mostra)
- [ ] From-name humano ("Luis de Marca X" > "no-reply@marca.com")
- [ ] Reply-to valido (nao "no-reply" — Gmail penaliza)

Dominio:
- [ ] DKIM configurado
- [ ] SPF configurado
- [ ] DMARC configurado (opcional mas recomendado)
- [ ] Dominio com historico de envios saudaveis (sem complaints recentes)

Track A — OAB:
- [ ] Sem promessa de resultado (VE-04)
- [ ] Sem captacao indevida ("Ligue hoje!", "Atendimento imediato!")
- [ ] Tom institucional, nao mercantil

Track B — CONAR/LGPD:
- [ ] Parceria paga DECLARADA (VE-13)
- [ ] Dados verificaveis (VE-12)
- [ ] Opt-out funcional (VE-09)
```

### 5. Criar campaign via MCP

Exemplo Klaviyo:
```
mcp__klaviyo__create_campaign \\
  --name "<nome interno>" \\
  --subject "<subject line>" \\
  --preview_text "<preview>" \\
  --from_email "<from>" \\
  --from_name "<from name>" \\
  --reply_to "<reply-to>" \\
  --list_id "<segmento_id>" \\
  --template_id OR --html "<HTML do email>" \\
  --send_time "<ISO timestamp>" \\
  --status "draft"  # SEMPRE draft
```

Outras plataformas: API similar com nomes diferentes. MCP abstrai conforme provider.

### 6. Sumario para revisao

```
BROADCAST CRIADO EM DRAFT:

Plataforma: <klaviyo|mailchimp|...>
Campaign ID: <id>
Nome interno: jun26-newsletter-decadencia
Segmento: 'lista-principal-opt-in' (4.823 contatos)
Subject: "Sobre decadencia em revisao previdenciaria"
From: "Marca X" <equipe@marca.com>
Reply-to: <equipe@marca.com>
Agendado para: 2026-05-20 09:30 BRT

DRAFT URL: https://klaviyo.com/campaigns/<id>/preview

REVISAO MANUAL OBRIGATORIA:
1. Acessar preview em DESKTOP + MOBILE + Gmail/Outlook
2. Validar:
   - Subject line nao corta no Gmail (max 50 chars)
   - Preview text aparece corretamente
   - Imagens carregam (alt text presente)
   - Link de opt-out funcional
   - CTA clicavel + UTM presente
3. Enviar TESTE pra voce + 1 colega antes de aprovar
4. Confirmar segmento correto (4.823 e o numero esperado?)

ATIVAR ENVIO:
- Plataforma: dashboard -> Approve & Send (ou agendar)
- Monitorar primeiras 1h: bounce rate < 2%, complaint rate < 0.1%
- Se complaint > 0.1%: pausar imediato (proveniencia da lista pode ter problema)
```

### 7. Registrar em integrations.json

```json
{
  "email_marketing": {
    "platform": "klaviyo",
    "broadcasts_history": [
      {
        "campaign_id": "abc",
        "subject": "...",
        "segment_size": 4823,
        "scheduled_at": "...",
        "lgpd_gate_passed": true,
        "antispam_gate_passed": true,
        "diretoria_r3_passed": true
      }
    ]
  }
}
```

## OUTPUT

Draft criado + URL de preview + checklist anti-spam + plano de monitoramento pos-envio.

## VEDACOES ESPECIFICAS

- **LGPD — VE-08, VE-09 (CRITICAS):**
  - Sem opt-in valido = BLOQUEIO TOTAL
  - Sem opt-out funcional = BLOQUEIO TOTAL
  - Lista comprada = BLOQUEIO TOTAL (base legal nula)
- **VE-04 (Track A):** email NAO promete resultado processual
- **VE-06 (Track A):** sem captacao agressiva ("Ligue hoje!")
- **NUNCA enviar de no-reply@** — Gmail penaliza
- **NUNCA enviar SO IMAGEM** — texto rico obrigatorio
- **NUNCA pular o teste pra voce + 1 colega antes** — typos viajam pra 5000 pessoas
- **NUNCA usar lista que voce nao sabe a origem** — auditar antes

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — plataforma + segmento + email pronto
- **2.3 Producao** — versao HTML + texto-puro + adaptacao por cliente (Gmail, Outlook)
- **2.4 Compliance** — LGPD critica + Track A VE-04, VE-06 + anti-spam universal
- **2.5 Mensuracao** — open-rate target >25%, click-rate >3%, complaint rate <0.1%
