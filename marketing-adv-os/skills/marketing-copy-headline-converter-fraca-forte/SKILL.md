---
name: marketing-copy-headline-converter-fraca-forte
description: >
  MARKETING COPY HEADLINE CONVERTER — Recebe headline fraca/generica e diagnostica os 5 pontos que a tornam fraca (abstracao, falta de especificidade, ausencia de gatilho, voz inconsistente, sem promessa clara). Reescreve em 3 versoes progressivamente mais fortes: minima (corrige defeitos basicos), media (adiciona especificidade + gatilho), maxima (reposiciona com hook + promessa + reducao de risco). Util pra refinar headlines herdadas, copiadas de concorrentes, ou que nao estao convertendo. Use quando o operador disser melhorar headline, headline esta fraca, refinar headline, headline ruim, otimizar headline.
---

# MARKETING COPY HEADLINE CONVERTER FRACA FORTE

> Skill Tier 2 (Executor — Copy). Diagnostica e reescreve headline fraca.

## OBJETIVO

Receber headline fraca do operador, diagnosticar PRECISAMENTE os 5 pontos que a tornam fraca, e reescrever em 3 versoes (minima, media, maxima) com aumento progressivo de impacto.

## PRE-REQUISITOS

Workspace marketing configurado + MEMORY com publico+dor+voz. Operador fornece a headline.

## FLUXO

### 1. Receber headline fraca

> "Cole a headline que voce quer melhorar. Opcional: contexto (canal de uso, headline esta convertendo X%, comparacao com benchmark, etc)."

### 2. Diagnostico — 5 dimensoes

Pontuar a headline base em 5 eixos (0-2 pontos cada, total 0-10):

| Dimensao              | 0 (fraco)                  | 1 (medio)                | 2 (forte)                            |
|-----------------------|----------------------------|--------------------------|--------------------------------------|
| **Especificidade**    | "melhor", "muitos", "alto" | "5x maior", "centenas"   | "247 e-commerces", "ROAS 5x em 60d"  |
| **Promessa clara**    | beneficio implicito        | beneficio nomeado        | beneficio + tempo + reducao risco    |
| **Voz da marca**      | generica                   | parcial                  | totalmente alinhada ao MEMORY        |
| **Gatilho ativo**     | nenhum                     | um leve                  | um claro + bem aplicado              |
| **Tamanho**           | >18 palavras               | 13-18                    | <=12 palavras                        |

Score total: **X/10**.

Output do diagnostico:
```
DIAGNOSTICO da headline "<base>"

Score: <X>/10

Especificidade:     <0|1|2>  — <razao>
Promessa clara:     <0|1|2>  — <razao>
Voz da marca:       <0|1|2>  — <razao>
Gatilho ativo:      <0|1|2>  — <razao>
Tamanho:            <0|1|2>  — <X palavras>

PROBLEMAS PRINCIPAIS:
- <descricao item 1>
- <descricao item 2>
```

### 3. Reescrever em 3 versoes

**V1 MINIMA** — corrige defeitos basicos sem reposicionar:
- Substitui abstracao por especifico
- Reduz palavras (se acima de 12)
- Aplica voz do MEMORY

**V2 MEDIA** — adiciona especificidade + gatilho:
- Inclui numero/tempo/dado verificavel
- Adiciona UM gatilho (autoridade / prova social / curiosidade)
- Mantem promessa original mas explicita

**V3 MAXIMA** — reposiciona completamente:
- Reescreve com hook + promessa + reducao de risco
- Pode mudar o angulo se a base estava em angulo errado
- Aplica framework PROMESSA + ESPECIFICIDADE + URGENCIA (real) + PROVA

### 4. Comparacao final

```
ANTES:  "[base]"              [score X/10]
V1 MIN: "[v1]"                [score esperado Y/10]
V2 MED: "[v2]"                [score esperado Z/10]
V3 MAX: "[v3]"                [score esperado W/10]
```

### 5. Recomendacao

> "RECOMENDACAO:
> - Se headline e de hero de LP: usar V3 (maxima)
> - Se headline e de subject line email: usar V2 (media) — V3 pode parecer 'clickbait' em email
> - Se headline e de anuncio: testar V2 contra V3 em A/B
> - Se contexto e conservador (track A): partir de V1 ou V2; V3 pode tocar VE-05 (mercantilizacao)"

### 6. Diretoria Criativa R2 + R3

Cada versao passa R2 (clareza) e R3 (compliance VE-01/04/12 conforme track).

## OUTPUT

Diagnostico + 3 versoes + comparacao + recomendacao + veredito Diretoria.

## VEDACOES ESPECIFICAS

- **VE-01** — NUNCA aumentar superlativo na versao "maxima" — V3 deve ser FORTE, nao FALSA
- **VE-04 (Track A)** — V3 NUNCA pode virar promessa de resultado
- **VE-05 (Track A)** — V3 NUNCA pode soar mercantil agressivo (urgencia falsa)
- Diagnostico DEVE ser objetivo — operador precisa entender PORQUE a headline era fraca

## PROTOCOLOS ACIONADOS

- **2.3 Producao** — voz aplicada em todas as 3 versoes
- **2.4 Compliance** — R3 condicional ao track
