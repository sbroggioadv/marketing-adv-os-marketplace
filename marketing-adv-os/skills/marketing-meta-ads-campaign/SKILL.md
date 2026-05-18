---
name: marketing-meta-ads-campaign
description: >
  MARKETING META ADS CAMPAIGN — Cria campanha completa no Meta Ads (Facebook + Instagram) usando MCP ja conectado (pre-req: marketing-meta-ads-connect rodou). Orquestra: definicao de objetivo + segmentacao publico + budget + cronograma + consumo de copy (marketing-copy-ads-meta) + consumo de criativo (marketing-arte-png). MODO DRAFT por default — campanha sobe pausada no ad account, operador revisa e ativa manualmente. Track A: VE-04, VE-06 obrigatorias. Use quando o operador disser criar campanha meta ads, subir anuncio facebook, lancar campanha instagram ads, agendar campanha paga.
---

# MARKETING META ADS CAMPAIGN

> Skill Tier 2 (Executor — Integracao Opt-in). Cria campanha Meta Ads via MCP.

## OBJETIVO

Estruturar campanha completa no Meta Ads e criar via MCP em MODO DRAFT (pausada). Operador revisa no Ads Manager e ativa. Reduz erro manual + garante compliance OAB/CONAR antes de gastar.

## PRE-REQUISITOS

1. `marketing-meta-ads-connect` rodou — `<cwd>/marketing/integrations.json` tem `meta_ads.status = "connected"`
2. Workspace + MEMORY configurado
3. Copy + criativo da campanha JA produzidos (ou serao produzidos nesta skill)
4. Budget definido (orcamento minimo Meta: R$ 5/dia)

## FLUXO

### 1. Briefing

> "Vou criar campanha Meta Ads em MODO DRAFT. Confirme:
> - Objetivo: TRAFFIC (cliques pra LP) / CONVERSIONS (compra/lead) / ENGAGEMENT / VIDEO_VIEWS / LEADS (lead form nativo) / BRAND_AWARENESS / REACH
> - Nome interno da campanha: [ex: 'jun26-curso-tributario-frio']
> - Budget total OU diario: R$ X / R$ X/dia
> - Janela: data inicio + data fim (ou continuous)
> - Posicionamento: feed / stories / reels / explore / right-column / messenger / audience-network (multi-select; recomendado: 'automatic placements')
> - Publico:
>   (a) Salvar audiencia (lookalike, custom, salvada anteriormente) — passar ID
>   (b) Definir agora: idade + genero + localizacao + interesses + comportamentos
> - Tem criativo (PNG + copy) pronto? Senao, rodar marketing-arte-png + marketing-copy-ads-meta antes"

### 2. Coletar/produzir criativo

Se criativo nao existe:
- Rodar `marketing-copy-ads-meta` -> gera 9 copies (3 tamanhos x 3 variantes)
- Rodar `marketing-arte-png` -> gera PNG no formato correto (feed_portrait 1080x1350 ou stories 1080x1920)

Operador escolhe quais variantes subir (recomendado 3-5 variantes por campanha para A/B).

### 3. Diretoria Criativa R3 OBRIGATORIO antes de subir

```
RODANDO DIRETORIA CRIATIVA R3 (COMPLIANCE) ANTES DE GASTAR DINHEIRO:

Track A — OAB Provimento 205/2021:
- [ ] VE-04: copy NAO promete resultado processual
- [ ] VE-05: copy NAO tem tom mercantil agressivo
- [ ] VE-06: CTA NAO e captacao indevida ("ligue ja!")
- [ ] VE-07: NAO ofende colega ou banca nominalmente
- [ ] VE-15: cases citados tem autorizacao escrita

Track B — CONAR:
- [ ] VE-10: NAO compara desleal com concorrente nominado
- [ ] VE-12: dado/numero VERIFICAVEL
- [ ] VE-13: parceria paga DECLARADA com #publi

Universal — Meta Policy:
- [ ] NAO usa "voce" acusatorio ("se VOCE esta gordo...")
- [ ] NAO menciona atributo pessoal sensivel
- [ ] NAO promete resultado absoluto
- [ ] NAO usa antes/depois exagerado
- [ ] Linguagem positiva e aspiracional

LGPD:
- [ ] LP destino tem politica de privacidade publicada
- [ ] Lead form (se objetivo LEADS): opt-in explicito
- [ ] LP destino tem termos de uso

Falha em qualquer item: BLOQUEIO. Reformular antes de subir.
```

### 4. Estruturar via MCP

Usando MCP `meta-ads` conectado:

```
[Claude conversa com o MCP via tool calls]

1. Criar Campaign:
   POST /act_<id>/campaigns
   - name: <nome interno>
   - objective: <objetivo>
   - status: PAUSED (draft mode)
   - special_ad_categories: [] (Track A: cuidado — pode requerer "credit", "employment", "issues_elections_politics")

2. Criar Ad Set:
   POST /act_<id>/adsets
   - name: <nome>-<audiencia>
   - campaign_id: <id_campaign>
   - daily_budget OU lifetime_budget: <em centavos R$>
   - start_time + end_time
   - targeting: {
       age_min, age_max, genders,
       geo_locations: { countries: ['BR'], cities: [...], regions: [...] },
       interests: [...],
       behaviors: [...]
     }
   - optimization_goal: <conforme objetivo>
   - billing_event: IMPRESSIONS (default)
   - placements: 'automatic' OU manual array
   - status: PAUSED

3. Criar Ad Creative:
   POST /act_<id>/adcreatives
   - name: <nome>-creative-v1
   - object_story_spec: {
       page_id: <page_facebook_id>,
       link_data OU video_data: {
         message: <copy texto principal>,
         headline: <copy headline>,
         description: <copy descricao>,
         link: <URL destino com UTM>,
         image_hash: <hash do PNG ja uploaded>,
         call_to_action: { type: SHOP_NOW | LEARN_MORE | SIGN_UP | etc }
       }
     }

4. Criar Ad:
   POST /act_<id>/ads
   - name: <nome>-ad-v1
   - adset_id: <id>
   - creative: { creative_id: <id> }
   - status: PAUSED
```

### 5. Sumario para revisao

Apos criar, mostrar resumo:

```
CAMPANHA CRIADA EM MODO DRAFT (PAUSED):

Campaign ID: 23847234
Nome: jun26-curso-tributario-frio
Objetivo: TRAFFIC
Status: PAUSED <-- vai precisar ativar manualmente

Ad Sets: 1
  - Audiencia: ['curso tributario', interesses fiscais, 25-55, BR]
  - Budget: R$ 50/dia
  - Janela: 7 dias (R$ 350 total max)
  - Placements: automatic

Ads: 3 variantes (A/B test)
  - v1: copy curta + criativo PNG 1080x1350
  - v2: copy media + mesmo criativo
  - v3: copy longa + mesmo criativo

LINKS:
- Revisar no Ads Manager: https://business.facebook.com/adsmanager/manage/campaigns?act=<account>&selected_campaign_ids=23847234

REVISAO MANUAL OBRIGATORIA ANTES DE ATIVAR:
1. Visualizar cada Ad no preview do Ads Manager (DESKTOP + MOBILE + STORIES)
2. Confirmar que UI da Meta nao corta texto critico do criativo
3. Confirmar que LP destino esta no ar e converte
4. Confirmar UTMs nos links
5. Confirmar billing method com saldo disponivel
6. (Track A) Confirmar compliance OAB com socio/responsavel se aplicavel

PROXIMOS PASSOS:
- Ativar: no Ads Manager, mudar status de PAUSED para ACTIVE
- Monitorar: primeiras 24h para validar CTR + CPC + qualidade
- Otimizar: apos 48-72h com dados, escalar vencedoras + matar perdedoras
```

### 6. Registrar em integrations.json

Atualizar `<cwd>/marketing/integrations.json`:

```json
{
  "meta_ads": {
    "status": "connected",
    ...
    "campaigns_history": [
      {
        "campaign_id": "23847234",
        "name": "jun26-curso-tributario-frio",
        "created_at": "2026-05-17T17:15:00Z",
        "objective": "TRAFFIC",
        "status": "PAUSED (draft mode)",
        "budget_daily_brl": 50,
        "diretoria_r3_passed": true
      }
    ]
  }
}
```

## OUTPUT

Campanha em PAUSED + sumario + links pra Ads Manager + checklist pre-ativacao.

## VEDACOES ESPECIFICAS

- **NUNCA criar campanha em ACTIVE direto** — sempre PAUSED, operador revisa
- **NUNCA pular Diretoria R3** — bloqueio absoluto antes de gastar
- **VE-04, VE-06 (Track A) — CRITICAS:** falha = bloqueio
- **Meta Policy:** falha = Meta rejeita anuncio E ainda gera nota negativa na conta
- **Budget inicial conservador:** primeira campanha de tema novo NUNCA passa R$ 100/dia ate validar
- **NUNCA promover post (boost)** em Track A: viola VE-06 (captacao indevida)

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — objetivo + budget + publico
- **2.3 Producao** — consome copy + arte de skills anteriores
- **2.4 Compliance** — Diretoria R3 OBRIGATORIA antes de subir
- **2.5 Mensuracao** — UTM por variante + plano de otimizacao em 48-72h
