---
name: marketing-reels-roteiro
description: >
  MARKETING REELS ROTEIRO — Gera roteiro estruturado de Reels Instagram (45-60s) com hook nos primeiros 3 segundos + corpo + CTA, dividido em cenas (0-3s, 3-15s, 15-45s, 45-60s) com texto on-screen + indicacao de B-roll + transicoes. NAO renderiza video — gera o ROTEIRO completo + capa PPTX (frame inicial) + instrucoes de gravacao. Operador grava no celular ou contrata editor. Use quando o operador disser roteiro de reels, script de reels, reels Instagram, reels 60 segundos, roteiro de video curto, script TikTok.
---

# MARKETING REELS ROTEIRO

> Skill Tier 2 (Executor — Arte). Gera roteiro estruturado de Reels.

## OBJETIVO

Produzir roteiro completo de Reels 45-60s em 4 cenas (hook + desenvolvimento + corpo + CTA) com: texto on-screen por cena, indicacao de B-roll/cenario, transicoes, audio sugerido. Adicionalmente: capa PPTX (frame inicial otimizado pra thumbnail).

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Voz + publico definidos no MEMORY

## FLUXO

### 1. Briefing

> "Vou gerar roteiro de Reels. Confirme:
> - Tema central: [...]
> - Duracao alvo: 45s / 60s / 90s
> - Estilo: (a) talking head (operador na camera) / (b) screen recording (tutorial) / (c) misto / (d) so texto on-screen + B-roll
> - CTA primario: comentar / salvar / encaminhar / link na bio
> - Output path: `<cwd>/marketing/MARKETING/Artes/<slug>/reels-roteiro/`"

### 2. Estrutura padrao do roteiro

```
=== REELS ROTEIRO — <tema> ===

CENA 1 — HOOK (0-3s)
DURACAO: 3 segundos (CRITICO)
TEXTO ON-SCREEN: "<HOOK FORTE, ate 8 palavras>"
NARRACAO/FALA: <fala do operador OU sem fala (so texto)>
B-ROLL: <cenario sugerido — closeup de algo, ambiente, gesto>
TRANSICAO PRA CENA 2: corte seco / zoom in / cut on action
NOTA: usuario decide em 3s se continua. Hook PRECISA prometer valor concreto.

CENA 2 — DESENVOLVIMENTO (3-15s)
DURACAO: 12 segundos
TEXTO ON-SCREEN: "<contextualiza o problema/oportunidade>"
NARRACAO: "<2-3 frases curtas>"
B-ROLL: <complementa o texto>
TRANSICAO: corte sincronizado / dissolve

CENA 3 — CORPO/VALOR (15-45s)
DURACAO: 30 segundos
TEXTO ON-SCREEN: "<entrega o valor prometido — pode mudar texto a cada 5-7s>"
NARRACAO: "<7-10 frases — a maior parte da fala>"
B-ROLL: <mostra o que se fala — screen recording, gesto, exemplo>
TRANSICOES INTERNAS: 3-4 cortes para manter ritmo

CENA 4 — CTA (45-60s)
DURACAO: 15 segundos
TEXTO ON-SCREEN: "<CTA singular>"
NARRACAO: "<chamada clara em 1-2 frases>"
B-ROLL: <gesto de chamada / direcionamento>
FINAL: pode terminar com pergunta convidando comentario
```

### 3. Texto on-screen — regras

**Font size mobile:** 32-40pt minimo (legivel em tela de 5-6")
**Posicao:** dentro da AI-SAFE V2 dos Reels (margem base 460px — UI do Reels cobre)
**Cor:** primary background + neutral_dark texto OU accent background + neutral_light texto
**Duracao por texto:** cada texto on-screen permanece visivel 3-7s
**Quantidade:** max 5-7 trocas de texto on-screen em 60s (excesso confunde)

### 4. Audio sugerido

> "Sugestoes de audio (verificar disponibilidade na biblioteca Reels):
> - Audio com som direto da camera (fala do operador) — Track A (autoridade) prefere
> - Audio trending da biblioteca Instagram — Track B com publico jovem prefere
> - Musica de fundo licenciada (artist tag) — neutro
> - NUNCA usar audio com watermark TikTok ou que ja saiu da biblioteca Reels"

### 5. Gerar capa PPTX (thumbnail)

Acionar `marketing-arte-pptx` automaticamente para gerar capa:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py \\
  --template instagram.reels \\
  --texto "<HOOK do reels>" \\
  --tokens <tokens.json> \\
  --output <cwd>/marketing/MARKETING/Artes/<slug>/reels-roteiro/capa.pptx
```

Capa serve como:
- Cover thumbnail no Instagram (escolher manual na publicacao)
- Frame inicial do video se filmando com texto on-screen

### 6. Output estrutura

```
OK Reels roteiro gerado.

LOCALIZACAO: <cwd>/marketing/MARKETING/Artes/<slug>/reels-roteiro/
ARQUIVOS:
  - roteiro.md          (4 cenas detalhadas + tempos + textos + B-roll + audio)
  - capa.pptx           (thumbnail/frame inicial em PPTX editavel)
  - capa.png            (versao PNG ja exportada se Pillow disponivel)
  - shotlist.md         (lista de takes a gravar, em ordem de gravacao)

INSTRUCOES DE GRAVACAO:
1. Ler roteiro completo + checar audio + B-roll antes
2. Gravar todos os takes (talking head + cenas extras + B-rolls)
3. Editar no celular (Reels nativo / InShot / CapCut) ou enviar pra editor
4. Aplicar texto on-screen conforme cenas — usar tipografia que combine com paleta
5. Validar antes de publicar: AI-SAFE respeitada? texto legivel mobile? hook em 3s? CTA claro?
6. Cover thumbnail: pode usar `capa.png` OU frame mid-video que represente a tese

CHECKLIST PRE-PUBLICACAO:
- [ ] Duracao 45-90s (ideal 45-60)
- [ ] Hook nos primeiros 3 segundos ESTA CLARO
- [ ] Texto on-screen LEGIVEL EM MOBILE (>=32pt)
- [ ] Conteudo critico na AI-SAFE V2 (margem base 460)
- [ ] Audio sem watermark TikTok
- [ ] Bitrate >= 4000 kbps, fps >= 30
- [ ] sRGB color space
- [ ] CTA singular alinhado ao objetivo
- [ ] Sem promessa falsa (VE-01)
- [ ] Track A: sem promessa resultado processual (VE-04)
```

## OUTPUT

Roteiro estruturado em 4 cenas + capa PPTX + shotlist + checklist pre-publicacao.

## VEDACOES ESPECIFICAS

- **NUNCA hook fraco** (>3 segundos sem promessa concreta) — viewer desliza
- **AI-SAFE V2 Reels obrigatoria:** margem base 460px
- **Texto on-screen <= 7 trocas em 60s** — excesso confunde
- **Audio sem watermark** TikTok / CapCut gratis (penaliza alcance)
- **VE-04 (Track A):** Reels juridico NAO promete resultado processual
- **VE-13:** Se parceria paga, declarar com #publi (CONAR + Instagram policy)

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — tema + duracao + estilo + CTA
- **2.3 Producao** — voz + tipografia mobile-safe
- **2.4 Compliance** — VE-04, VE-13 prioritarias
- **2.5 Mensuracao** — KPI Reels = view-through rate + saves + comments + shares (NAO so curtidas)
