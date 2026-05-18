---
name: marketing-diretoria-r4-performance
description: >
  DIRETORIA R4 PERFORMANCE — Quarto e ultimo gate da Diretoria Criativa. Audita mensurabilidade da peca: gancho mensuravel + UTM/pixel + metrica primaria + threshold de sucesso + plano de iteracao A/B. Falha NAO bloqueia (e aviso de risco) mas alerta que peca pode subir e "operador nao saber se funcionou". Use quando o operador disser audita performance, R4 da peca, mensurabilidade, plano de mensuracao, ultima etapa Diretoria.
---

# DIRETORIA R4 PERFORMANCE

> Skill Tier 3 (Diretoria Criativa — Gate 4 final). Audita mensurabilidade. **Aviso, nao bloqueio.**

## OBJETIVO

Garantir que a peca pode ser medida apos publicacao. R4 nao bloqueia (peca ja passou R1-R3 = legal e bem-feita), mas avisa quando peca sai sem instrumentacao e operador vai publicar "no escuro" sem saber se converteu.

## PRE-REQUISITOS

- R1, R2, R3 todos aprovados
- Peca pronta (copy + arte + link de destino se aplicavel)

## FLUXO

### 1. Checklist 5 itens

```
GATE R4 — PERFORMANCE:

[1] GANCHO MENSURAVEL
    Cada peca precisa um gancho cuja eficacia pode ser medida:
    - Video: taxa de retencao no primeiro segundo (Reels/TikTok)
    - Carrossel: swipe-through-rate (% que chega no slide N)
    - Email: open-rate (sobre subject line + preview text)
    - Anuncio: CTR (% clicou)
    - Post organico: salvamento + encaminhamento (sobre conteudo)
    OK: gancho identificavel mesuravel
    AVISO: peca sem gancho claro mensuravel

[2] UTM / PIXEL / EVENTO INSTRUMENTADO
    Se peca tem link saindo: tem UTM?
    Formato recomendado: utm_source=<plataforma>&utm_medium=<tipo>&utm_campaign=<nome>&utm_content=<variante>
    - LinkedIn post: utm_source=linkedin&utm_medium=organic-post
    - Meta Ads: utm_source=facebook&utm_medium=cpc&utm_campaign=jun26-X
    - Email: utm_source=email&utm_medium=broadcast&utm_content=v1
    - Story sticker link: utm_source=instagram&utm_medium=story
    OK: UTM presente em TODOS os links saindo
    AVISO: UTM ausente -> trafego vira "direct" no analytics e perde atribuicao

[3] METRICA PRIMARIA DEFINIDA
    Uma peca = uma metrica primaria (max duas)
    Tipos por objetivo:
    - Awareness: alcance + frequencia
    - Engajamento: comentarios + saves + shares (NAO curtidas)
    - Lead gen: opt-ins + custo por lead (CPL)
    - Conversao: vendas + ROAS / ROI
    - Retencao: taxa de re-abertura (email) / repeat purchase
    AVISO: peca sem metrica primaria = "vou publicar e ver o que acontece" — nao escala

[4] THRESHOLD DE SUCESSO
    Qual o numero que define "deu certo"?
    OK: "se >= 100 saves: top performer; se >= 50: media; <50: refazer angulo"
    OK: "CPL <= R$ 15: validar; R$ 15-30: testar; > R$ 30: matar"
    AVISO: sem threshold = decisao subjetiva de continuar/parar

[5] PLANO DE ITERACAO A/B
    Se falhar: o que muda no proximo experimento?
    OK: "se hook fraco -> testar variantes 2-3 da skill marketing-copy-headline-ab-test"
    OK: "se CTA baixo -> trocar verbo (Comecar -> Ver demo)"
    AVISO: peca sem plano B = sem aprendizado se falhar
```

### 2. Veredito

```
DIRETORIA R4 — PERFORMANCE: <APROVADO | AVISO DE RISCO>

[1] Gancho mensuravel:        OK (gancho: X) | AUSENTE
[2] UTM / Pixel:              OK | AUSENTE (urls sem UTM: ...)
[3] Metrica primaria:         OK (metrica: X) | AUSENTE
[4] Threshold de sucesso:     OK (threshold: X) | AUSENTE
[5] Plano iteracao A/B:       OK (plano: X) | AUSENTE

DECISAO:
- APROVADO (tudo OK): peca PRONTA para publicar
- AVISO (>= 1 item ausente): peca pode subir, mas operador NAO vai saber se funcionou.
  Recomendacao: corrigir items AVISO antes de publicar (5 min de trabalho que vale ROI 10x).

ITENS AVISO + SUGESTOES:
- ...
```

### 3. Resumo final (apos R1+R2+R3+R4)

Se peca passou TODOS os 4 gates:

```
DIRETORIA CRIATIVA — VEREDITO FINAL: APROVADA

R1 Brief:        APROVADO
R2 Copy:         APROVADO
R3 Compliance:   APROVADO (track A | B)
R4 Performance:  APROVADO

Peca pronta para publicar. Recomendacao final:
- Publicar no horario otimo do publico (LinkedIn 9-11h ter/qua, IG 19-21h ter/qui)
- Monitorar primeiras 24-48h
- Aplicar plano A/B se metrica primaria abaixo do threshold
```

## OUTPUT

Veredito R4 + (se aplicavel) veredito consolidado R1-R4 + plano de monitoramento.

## VEDACOES ESPECIFICAS

- R4 e AVISO, nao bloqueio — diferente de R3
- Se operador escolhe publicar sem R4 OK, registrar em integrations.json que peca foi para o ar "no escuro"

## PROTOCOLOS ACIONADOS

- **2.5 Mensuracao** — esta skill E o gate central do protocolo
