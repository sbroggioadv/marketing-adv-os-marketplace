---
name: marketing-copy-headline-ab-test
description: >
  MARKETING COPY HEADLINE AB TEST — Recebe uma headline base e gera 5 variacoes estrategicas para teste A/B/n. Cada variacao explora um angulo psicologico diferente (curiosidade, autoridade, especificidade, urgencia real, prova social) mantendo a mesma promessa central. Util para descobrir qual angulo o publico responde melhor antes de escalar investimento em ads ou hero de LP. Use quando o operador disser variar headline, criar variacoes A/B, testar headlines, variantes da headline, multiplas versoes da mesma headline.
---

# MARKETING COPY HEADLINE AB TEST

> Skill Tier 2 (Executor — Copy). Gera 5 variacoes A/B/n de uma headline base.

## OBJETIVO

A partir de UMA headline base do operador, gerar 5 variacoes mantendo a promessa central mas mudando o angulo psicologico. Output pronto para subir em A/B test em Meta Ads, Google Ads, hero de LP, subject line de email.

## PRE-REQUISITOS

Workspace marketing configurado + MEMORY com publico+dor. Operador precisa fornecer a headline base.

## FLUXO

### 1. Receber headline base

> "Cole a headline base que voce quer variar. Diga tambem:
> - Canal de teste (Meta Ads / Google Ads / LP hero / email subject)
> - Metrica de sucesso (CTR / CR / open rate / scroll depth)"

### 2. Identificar promessa central

Extrair da headline base:
- **Beneficio principal** (o que o leitor conquista)
- **Mecanismo/diferenciador** (como)
- **Reducao de risco** (o que ele NAO precisa fazer)
- **Especificidade temporal/quantitativa** (se houver)

> "Identifiquei a promessa central como: [beneficio] via [mecanismo]. Confirma?"

### 3. Gerar 5 variacoes por angulo

Cada variacao explora UM angulo distinto:

| Variacao | Angulo psicologico    | Estrategia                                                            |
|----------|----------------------|------------------------------------------------------------------------|
| V1       | Curiosidade          | Pergunta provocadora, lacuna de informacao                            |
| V2       | Autoridade           | Adicionar dado verificavel, fonte, numero especifico                  |
| V3       | Especificidade       | Trocar termo abstrato por numero/tempo concreto                       |
| V4       | Urgencia REAL        | Marcar prazo ou contexto real (sem urgencia falsa — VE-01)           |
| V5       | Prova social         | Citar quantidade de pessoas, casos, anos de aplicacao                 |

### 4. Tabela comparativa

```
HEADLINE BASE:
"[base]"

| V  | Angulo          | Variacao                                          | Hipotese de teste                   |
|----|-----------------|---------------------------------------------------|-------------------------------------|
| V1 | Curiosidade     | ...                                               | Aumenta CTR em publico frio         |
| V2 | Autoridade      | ...                                               | Reduz objecao em publico cetico     |
| V3 | Especificidade  | ...                                               | Melhora qualificacao do lead        |
| V4 | Urgencia real   | ...                                               | Acelera decisao em re-engajamento   |
| V5 | Prova social    | ...                                               | Reduz friccao em compra impulsiva   |
```

### 5. Plano de teste sugerido

> "PLANO A/B SUGERIDO:
> - Periodo: [N] dias (alcance amostral >= [N] impressoes/clicks por variacao)
> - Distribuicao: 16,6% por variacao (base + 5 variacoes em 6 grupos iguais)
> - Metrica primaria: [CTR/CR]
> - Threshold de significancia: aumentar tracking ate diferenca >= [valor] com p < 0.05
> - Stop criterio: se uma variacao bater [X]% acima da base com volume amostral suficiente, escalar."

### 6. Diretoria Criativa R2 + R3 + R4

R2: hook + clareza + voz.
R3: VE-01, VE-04 (A), VE-12 (B). **Urgencia REAL apenas** — VE-05 (track A) bloqueia urgencia falsa.
R4: cada variacao precisa ter metrica primaria identificavel.

## OUTPUT

Headline base + 5 variacoes por angulo + plano A/B + veredito Diretoria.

## VEDACOES ESPECIFICAS

- **VE-01** — NUNCA aumentar superlativo em variacao ("o melhor" -> "o unico" = pior)
- **VE-05 (Track A)** — V4 NUNCA fabrica urgencia ("ultima chance!" sem prazo real)
- Promessa central NAO muda entre variacoes — se mudou, virou outra headline

## PROTOCOLOS ACIONADOS

- **2.3 Producao** — variacoes mantem voz consistente
- **2.5 Mensuracao** — toda variacao vem com hipotese mensuravel
