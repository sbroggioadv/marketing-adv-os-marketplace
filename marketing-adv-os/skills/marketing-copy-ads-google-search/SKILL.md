---
name: marketing-copy-ads-google-search
description: >
  MARKETING COPY ADS GOOGLE SEARCH — Gera anuncios para Google Ads (rede de pesquisa) seguindo limites exatos da plataforma: ate 15 headlines de 30 caracteres + 4 descriptions de 90 caracteres + 1 display path + 2 paths de URL. Aplica intent-matching (o usuario que pesquisa "X" esta no estagio Y do funil). Diferente de Meta Ads — usuario chegou por INTENCAO especifica, copy precisa CONFIRMAR no primeiro segundo que o anuncio responde a busca. Use quando o operador disser copy pra Google Ads, anuncio Google, anuncio de busca, rede de pesquisa, search ads, copy de SERP.
---

# MARKETING COPY ADS GOOGLE SEARCH

> Skill Tier 2 (Executor — Copy). Copy para Google Ads search com limites exatos.

## OBJETIVO

Gerar 15 headlines (30 chars cada) + 4 descriptions (90 chars cada) + paths para um conjunto de anuncios responsivos (RSA) no Google Ads. Cada headline alinhada a uma keyword/intent.

## PRE-REQUISITOS

Workspace + MEMORY com publico+dor+oferta. Operador precisa fornecer keywords-alvo (ou pedir sugestao).

## FLUXO

### 1. Briefing

> "Vou gerar anuncios Google Ads pra: [Oferta].
> Confirme:
> - Keywords-alvo (ate 10): [lista, ex: 'aposentadoria especial professor', 'INSS auxilio doenca']
> - Tipo de match: exata / frase / ampla modificada
> - URL final (destino do clique): [URL completa]
> - Display path 1+2 (max 15 chars cada): [ex: '/curso' '/garantia']"

### 2. Intent mapping

Para cada keyword, identificar estagio do funil:
- **TOFU (top of funnel)** — pesquisa informacional. Ex: "o que e [X]"
- **MOFU (middle)** — pesquisa comparativa. Ex: "[X] vs [Y]", "melhor [X]"
- **BOFU (bottom)** — pesquisa transacional. Ex: "comprar [X]", "preco [X]", "[X] em [cidade]"

Copy adaptada ao estagio:
- TOFU: educa + convida a saber mais
- MOFU: diferencia + valida com prova
- BOFU: confirma intencao + reduz friccao na compra

### 3. Gerar 15 headlines (30 chars max cada)

```
HEADLINES (RSA — Google rotaciona):

H1  (30): [...] | <ESTAGIO> | <KEYWORD>
H2  (30): [...] | <ESTAGIO> | <KEYWORD>
...
H15 (30): [...] | <ESTAGIO> | <KEYWORD>
```

Mix recomendado:
- 5 headlines com **brand/oferta** (nome do produto, garantia, prazo)
- 5 headlines com **keyword match** (espelham termos da busca)
- 5 headlines com **diferenciador** (numero, dado, autoridade)

### 4. Gerar 4 descriptions (90 chars max cada)

```
D1 (90): [Beneficio + diferencial + CTA suave]
D2 (90): [Prova social + reducao risco + CTA]
D3 (90): [Urgencia REAL (se houver) + chamada]
D4 (90): [Pergunta provocadora + chamada]
```

### 5. Validar contagem de caracteres

Cada headline e description: contar caracteres incluindo espacos. Se excede:
- 30 chars: cortar ou reformular
- 90 chars: cortar ou dividir em duas

Mostrar contagem em cada item:
```
H1: "Aposentadoria sem INSS te enganar"  [33] ❌
H1: "Aposentadoria sem ser enganado"     [30] ✅
```

### 6. Paths e URL

```
URL final: https://exemplo.com/aposentadoria
Display URL: exemplo.com/curso/garantia
Path 1: curso (5)
Path 2: garantia (8)
```

### 7. Diretoria Criativa R2 + R3 + R4

R2: cada headline tem hook + voz consistente.
R3: VE-04 (A), VE-12 (B), VE-01. Google Policy: sem clickbait extremo, sem capitalizacao excessiva ("COMPRE AGORA").
R4: UTM nas URLs sugerido. Plano de quality score (estimar).

## OUTPUT

15 headlines + 4 descriptions + paths + URL + contagem chars + veredito.

## VEDACOES ESPECIFICAS

- **Google Policy** — sem capitalizacao excessiva, sem pontuacao excessiva ("!!!!"), sem clickbait
- **VE-01** — NUNCA superlativo sem prova
- **VE-04 (Track A)** — NUNCA promessa de resultado processual
- **VE-12** — NUNCA propaganda enganosa
- Contar caracteres SEMPRE — exceder 30/90 reprova no Google Ads

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — keywords + intent + URL
- **2.3 Producao** — voz + paleta de gatilhos por estagio
- **2.4 Compliance** — Google Policy + VEs
- **2.5 Mensuracao** — UTM por anuncio para tracking
