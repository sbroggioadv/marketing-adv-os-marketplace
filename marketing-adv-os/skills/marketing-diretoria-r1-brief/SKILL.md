---
name: marketing-diretoria-r1-brief
description: >
  DIRETORIA R1 BRIEF — Primeiro gate da Diretoria Criativa. Audita se uma peca de marketing parte de briefing COMPLETO antes de aprovar producao downstream. Verifica 5 itens: publico nomeado (NAO "todo mundo"), dor explicita, KPI definido (curtida NAO conta), canal escolhido, formato definido. Falha em qualquer item = volta com perguntas, nao com producao. Use quando o operador disser audita briefing, valida brief, R1 da peca, conferir briefing, primeira etapa Diretoria, briefing esta completo.
---

# DIRETORIA R1 BRIEF

> Skill Tier 3 (Diretoria Criativa — Gate 1). Audita briefing antes de aprovar producao.

## OBJETIVO

Validar que peca em producao parte de briefing claro e completo. Briefing fraco = peca fraca, independente do quao bem produzida. R1 economiza tempo bloqueando producao antes de virar arte ou copy.

## PRE-REQUISITOS

- Operador apresentou briefing OU descreveu peca que quer produzir
- Workspace marketing configurado (consultar MEMORY se preciso para validar coerencia com publico-alvo registrado)

## FLUXO

### 1. Receber briefing

> "Vou auditar R1 (Brief). Cole o briefing OU descreva o que voce quer produzir:
> - Peca: post / carrossel / LP / ebook / anuncio / email / video?
> - Para quem? (publico-alvo)
> - Resolve o que? (dor)
> - Qual o objetivo mensuravel?
> - Onde vai? (canal)
> - Que formato?"

### 2. Checklist 5 itens

```
GATE R1 — BRIEFING:

[1] PUBLICO NOMEADO
    OK: "advogados de imobiliario com 5-15 anos de experiencia em SP"
    OK: "empreendedoras de moda 30-45 anos faturamento R$ 20-80k/mes"
    FALHA: "todo mundo" / "pessoas" / "quem quer" / "interessados em direito"
    -> Se vago: perguntar "Que segmento ESPECIFICO? Para quem essa peca NAO e?"

[2] DOR EXPLICITA
    OK: "perde 4-6h/semana caçando jurisprudencia validada — quer encontrar Tema STJ em 30s"
    OK: "campanhas Meta com ROAS 0.8 — quer chegar em ROAS 3+ em 60 dias"
    FALHA: "ajudar pessoas" / "ganhar dinheiro" / "ter visibilidade"
    -> Se vago: perguntar "Qual a DOR ESPECIFICA que essa peca resolve?"

[3] KPI DEFINIDO
    OK: leads / cliques / vendas / agendamentos / saves / encaminhamentos / brand awareness mensuravel
    FALHA: "curtidas" / "viralizar" / "engajamento" (sem definir qual metrica)
    -> Curtida NAO e KPI primario. Comentario qualificado, salvamento e encaminhamento sim.
    -> "Como voce vai SABER que essa peca funcionou? Que numero?"

[4] CANAL ESCOLHIDO
    OK: Instagram feed / Instagram stories / LinkedIn / X / TikTok / email / LP / ads pago
    FALHA: "todas as redes" sem distincao de tom-por-canal
    -> Se "todas": pedir 1 PRIMARIO + ate 2 secundarios (mesma peca em todos = perde otimizacao)

[5] FORMATO DEFINIDO
    OK: post 1080x1350 / carrossel 7 slides 1080x1440 / reels 60s / story 5 telas / email com header / LP hero
    FALHA: "uma arte" / "um conteudo"
    -> Sem formato definido nao da pra ir pra arte/copy. Pedir agora.
```

### 3. Validacao adicional (coerencia com MEMORY)

Consultar `<cwd>/marketing/MEMORY.md`:
- **## Publico-alvo** registrado bate com publico do briefing? Senao, alertar (pode ser publico novo OU divergencia que indica peca fora-do-eixo)
- **## Oferta** registrada bate com o que essa peca promove? Senao, OK (pode ser conteudo educativo desvinculado de oferta) mas confirmar

### 4. Veredito

```
DIRETORIA R1 — BRIEF: <APROVADO | FALHA>

[1] Publico nomeado:     OK | FALHA (motivo: ...)
[2] Dor explicita:       OK | FALHA (motivo: ...)
[3] KPI definido:        OK | FALHA (motivo: ...)
[4] Canal escolhido:     OK | FALHA (motivo: ...)
[5] Formato definido:    OK | FALHA (motivo: ...)

DECISAO:
- APROVADO: prosseguir para R2 (Copy)
- FALHA: peca volta com perguntas. NAO produzir ainda. Resolver lacuna primeiro.

[Se FALHA] PERGUNTAS PENDENTES:
- ...
- ...
```

### 5. Quando passar pra R2

Se aprovado:
> "R1 OK. Recomendo seguir pra R2 (Copy). Voce ja tem o copy escrito? Ou quer rodar `marketing-copy-*` agora?"

## OUTPUT

Veredito estruturado dos 5 itens + perguntas pendentes (se falha) + recomendacao proxima etapa.

## VEDACOES ESPECIFICAS

- **NUNCA aprovar com "publico = todo mundo"** — destruir antes de produzir
- **NUNCA aceitar "curtidas" como KPI primario** — eh metrica de vaidade
- **NUNCA aprovar mesma peca para todos os canais** — cada um tem otimizacao propria
- **VE-04 (Track A):** se KPI promete "ganhar acao", invalido — substituir por "agendar consulta", "ler artigo"

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — esta skill E a checagem do protocolo
