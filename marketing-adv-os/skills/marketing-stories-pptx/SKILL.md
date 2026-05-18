---
name: marketing-stories-pptx
description: >
  MARKETING STORIES PPTX — Gera sequencia de 3-5 telas de Stories (9:16, 1080x1920) em PPTX, cada tela com template apropriado (story-cta para tela com link, story-poll para tela com enquete). AI-SAFE V2 (margem top 280 + base 300 = UI agressiva do Stories). Cada tela e UM arquivo PPTX para upload individual no Postiz/Buffer. Use quando o operador disser gerar stories, sequencia de 5 telas, story PPTX, story para Instagram, story para edicao.
---

# MARKETING STORIES PPTX

> Skill Tier 2 (Executor — Arte). Gera sequencia de telas de Stories via `scripts/arte-engine.py`.

## OBJETIVO

Produzir 3-5 PPTX (1 por tela) no formato Stories 9:16, com tipografia + paleta + tema da marca aplicados. Cada tela pode ter template diferente conforme funcao (intro/CTA/poll/quiz).

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Tokens gerados
3. **Copy/roteiro das telas JA produzido** — operador escreveu o que vai em cada tela

## FLUXO

### 1. Coletar roteiro das telas

> "Vou gerar sequencia de Stories. Confirme:
> - Quantas telas: 3 / 4 / 5
> - Tema da sequencia: [slug curto]
> - Para cada tela, qual o tipo + texto:
>   Tela 1: [tipo: intro / pergunta / dado / cta] + texto
>   Tela 2: ...
>   ...
> - Output: `<cwd>/marketing/MARKETING/Artes/<slug>/stories/`"

### 2. Mapear template por tipo de tela

| Tipo de tela | Template (templates/arte/) | Layout            |
|--------------|----------------------------|-------------------|
| Intro        | story-cta                  | centered          |
| Pergunta     | story-poll                 | top-aligned       |
| Dado/fato    | story-cta (variacao)       | centered          |
| Tese         | story-cta (variacao)       | hero-with-subtext |
| Quiz         | story-poll                 | top-aligned       |
| CTA final    | story-cta                  | centered          |

### 3. Renderizar cada tela

```bash
# Tela 1 (intro)
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py \\
  --template instagram.stories \\
  --texto "Sabia que [pergunta]?" \\
  --tokens <tokens.json> \\
  --layout centered \\
  --output <cwd>/marketing/MARKETING/Artes/<slug>/stories/tela-01.pptx

# Tela 2 (poll)
python3 ... --texto "Voce ja [pergunta]?" --output .../tela-02.pptx

# Tela 3 (dado)
python3 ... --texto "[numero impactante]" --output .../tela-03.pptx

# Tela 4 (tese)
python3 ... --texto "Eis a tese tecnica" --subtexto "Detalhe" --output .../tela-04.pptx

# Tela 5 (CTA)
python3 ... --texto "Quer aprofundar?" --subtexto "Link na bio" --output .../tela-05.pptx
```

### 4. Output estrutura

```
OK Sequencia de Stories gerada.

LOCALIZACAO: <cwd>/marketing/MARKETING/Artes/<slug>/stories/
ARQUIVOS:
  - tela-01.pptx   (intro — story-cta)
  - tela-02.pptx   (pergunta — story-poll: AREA RESERVADA para sticker poll do IG)
  - tela-03.pptx   (dado — story-cta)
  - tela-04.pptx   (tese — story-cta)
  - tela-05.pptx   (CTA final — story-cta com sticker link)
  - SEQUENCIA.md   (instrucoes de publicacao + sticker placement)

INSTRUCOES DE PUBLICACAO:
1. Importar telas no Instagram Stories (manual ou via Postiz/Buffer)
2. Tela 02 (poll): adicionar sticker de poll do Instagram NA AREA reservada (Y 800-1200)
3. Tela 05 (CTA): adicionar sticker de link do Instagram SOBRE o CTA box
4. Publicar como sequencia (uma de cada vez, em ordem)

REGRA: storys expiram em 24h — agendar publicacao no mesmo dia/horario otimo do publico.
```

### 5. Gerar SEQUENCIA.md

Arquivo de instrucoes detalhadas:

```markdown
# Sequencia de Stories — <tema>

## Tela 01 — Intro
- Texto: "<texto>"
- Tipo: story-cta (layout centered)
- Sticker: nenhum

## Tela 02 — Pergunta/Poll
- Texto: "<pergunta>"
- Tipo: story-poll (layout top-aligned)
- Sticker: POLL (2 opcoes) na area reservada (Y 800-1200)
- Opcoes sugeridas: [opcao A] | [opcao B]

## Tela 03 — Dado
- Texto: "<numero impactante>"
- Tipo: story-cta (layout centered)
- Sticker: nenhum

## Tela 04 — Tese
- Texto: "<tese>"
- Subtexto: "<detalhe>"
- Tipo: story-cta (layout hero-with-subtext)
- Sticker: nenhum

## Tela 05 — CTA Final
- Texto: "<chamada>"
- Subtexto: "Link na bio" OU URL direta
- Tipo: story-cta (layout centered)
- Sticker: LINK no CTA box (cobrir botao)
```

## OUTPUT

3-5 PPTX (1 por tela) + SEQUENCIA.md com instrucoes de publicacao + sticker placement.

## VEDACOES ESPECIFICAS

- **AI-SAFE V2 obrigatoria:** margem top 280 + base 300 (UI agressiva do Stories)
- **Sticker placement:** NUNCA sobrepor texto critico — sticker fica em area reservada
- **Sequencia max 5 telas:** alem disso decay de view-through-rate (viewer cansa)
- **VE-04 (Track A):** CTA final NAO promete resultado processual
- **VE-06 (Track A):** CTA suave ("Link na bio") em vez de captativo ("Ligue ja")

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — quantidade + tipos das telas confirmados
- **2.3 Producao** — paleta + tipografia consistentes nas telas
- **2.4 Compliance** — copy de cada tela passa por Diretoria R2/R3 antes
