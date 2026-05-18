---
name: marketing-carrossel-pptx
description: >
  MARKETING CARROSSEL PPTX — Gera carrossel completo (7-10 slides) em PPTX multi-slide, todos os slides com MESMO canvas + mesma tipografia + mesma margem (regra critica: slide 1 define ratio de todos). Slide 1 usa template carrossel-capa (hook visual forte); slides 2-N-1 usam carrossel-conteudo (1 ideia por slide); slide N (ultimo) usa story-cta adaptado (CTA suave). Output pronto pra import no Canva ou edicao. Consome paleta + tipografia + voz do MEMORY. Use quando o operador disser gerar carrossel, criar carrossel Instagram, carrossel 7 slides, carrossel educativo, exportar carrossel pra Canva.
---

# MARKETING CARROSSEL PPTX

> Skill Tier 2 (Executor — Arte). Gera carrossel completo multi-slide via `scripts/arte-engine.py`.

## OBJETIVO

Produzir 7-10 slides em UM unico arquivo PPTX, cada slide respeitando AI-SAFE V3 + paleta + tipografia + voz da marca. Estrutura editorial: slide 1 capa (hook) + slides 2-N-1 conteudo (1 ideia cada) + slide N CTA (acao suave).

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Paleta + tipografia + tokens gerados
3. **Copy do carrossel JA produzido** — rodar `marketing-copy-post-educativo-ig` ou `marketing-copy-post-autoridade` ANTES desta skill
4. python-pptx instalado (fallback SVG se faltar)

## FLUXO

### 1. Validar copy disponivel

> "Vou gerar carrossel PPTX. Voce ja tem o copy estruturado em slides?
> (a) SIM — cole o copy ou indique o arquivo
> (b) NAO — rodar `marketing-copy-post-educativo-ig` ou `marketing-copy-post-autoridade` primeiro, retornar depois"

Se NAO: acionar skill de copy correspondente e retornar quando tiver copy estruturado em 7-10 slides.

### 2. Coletar dados

> "Confirme:
> - Numero de slides: 7 / 10 (max 20 pelo limite Instagram)
> - Aspect ratio: feed_portrait 4:5 (default 2026) / feed_grid_3x4 3:4 (NOVO Mosseri 2026)
> - Tema do carrossel: [titulo curto pro slug]
> - Output path: `<cwd>/marketing/MARKETING/Artes/<slug>/carrossel.pptx`"

### 3. Estrutura padrao

```
Slide 1 (CAPA — template carrossel-capa):
  - Hook visual + numero 1/N + seta de swipe
  - Texto de até 12 palavras
  - Background: paleta neutral_light com hook em primary

Slides 2 a N-1 (CONTEUDO — template carrossel-conteudo):
  - Numero do slide (2/N, 3/N, ...) + tema/tag opcional
  - Titulo curto + corpo (1 ideia por slide)
  - Mesma margem, mesma tipografia, mesma cor de fundo

Slide N (CTA — template story-cta adaptado pra carrossel):
  - Sintese / fechamento
  - CTA suave: "Salva pra consultar", "Marca alguem", "Comenta [palavra]"
  - NUNCA "compre agora" em carrossel educativo (VE-05 Track A)
```

### 4. Executar render por slide

A engine pode ser chamada N vezes (uma por slide) salvando todos no MESMO arquivo PPTX:

```bash
# Slide 1 (capa)
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py \\
  --template instagram.feed_portrait \\
  --texto "Hook do slide 1" \\
  --tokens <tokens.json> \\
  --output <cwd>/marketing/MARKETING/Artes/<slug>/carrossel.pptx

# Slides 2-N (acrescentar slides no mesmo arquivo — modo append)
# (Engine suporta modo append via flag --append-to-existing — sera adicionado em S4.1+)
```

**NOTA TECNICA:** versao atual do arte-engine.py gera 1 slide por chamada. Para carrossel multi-slide, gerar N PPTX e mergir via python-pptx OU usar implementacao manual. Versao v2 do engine (em S4 follow-up) tera flag `--multi-slide` que recebe JSON com array de slides.

### 5. Output estrutura

```
OK Carrossel gerado.

LOCALIZACAO: <cwd>/marketing/MARKETING/Artes/<slug>/
ARQUIVOS:
  - carrossel.pptx          (N slides em UM arquivo, editavel)
  - slide-1-capa.pptx       (capa isolada)
  - slide-2-conteudo.pptx   (conteudo slide 2 isolado)
  - ... (demais slides isolados)
  - carrossel.preview.html  (preview visual dos N slides em sequencia)

REGRA CRITICA: aspect ratio do slide 1 (4:5 ou 3:4) e o ratio do CARROSSEL TODO.
Se editor mudar 1 slide de ratio, Instagram cropa ao centro automaticamente.

PROXIMOS PASSOS:
- Abrir carrossel.pptx
- Importar no Canva (mantem 7-10 slides em 1 design)
- Exportar como sequencia PNG via Canva > Download > PNG (selecionar todas as paginas)
- OU usar marketing-export-multi-formato para gerar PNG simultaneamente
```

### 6. Pos-render: preview HTML

Gerar `carrossel.preview.html` com os N slides lado-a-lado (CSS grid) — operador valida visualmente a coerencia antes de publicar.

## OUTPUT

PPTX multi-slide + slides isolados (para edicao individual) + HTML preview + plano de publicacao.

## VEDACOES ESPECIFICAS

- **REGRA CRITICA:** todos os slides com MESMO aspect ratio (slide 1 define)
- **NUNCA misturar canvas:** se slide 1 e 1080x1350, TODOS sao 1080x1350
- **MARGEM consistente:** mesma margem lateral em todos os slides
- **TIPOGRAFIA consistente:** mesma hierarquia (h1=titulo, body=corpo) em todos os slides
- **Mais de 20 slides:** Instagram corta. Max recomendado: 10 (decay de swipe-through apos slide 7)
- **VE-05 (Track A):** carrossel educativo NAO pode ter slides finais com tom comercial agressivo

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — copy ja produzido + estrutura confirmada
- **2.3 Producao** — paleta + tipografia + voz consistentes
- **2.4 Compliance** — Diretoria R2/R3 aplicada AO COPY antes da geracao da arte
