---
name: marketing-arte-png
description: >
  MARKETING ARTE PNG — Gera arte estatica em PNG-24 sRGB para qualquer formato Instagram/Facebook/LinkedIn, consultando paleta + tipografia do MEMORY e respeitando AI-SAFE zone (V3 2026). Le sizes.json (mapa canonico de medidas) + tokens.json (paleta) + template.json (layout) e produz arquivo pronto pra publicacao. Suporta 12+ formatos (feed_portrait 1080x1350, feed_grid_3x4 1080x1440, stories 1080x1920, reels 1080x1920, LinkedIn 1200x627, etc). Fallback SVG se Pillow indisponivel. Use quando o operador disser gerar arte PNG, criar imagem para Instagram, arte de feed, story PNG, post em PNG, exportar PNG.
---

# MARKETING ARTE PNG

> Skill Tier 2 (Executor — Arte). Gera arte PNG via `scripts/arte-engine.py`.

## OBJETIVO

Produzir arte estatica PNG-24 sRGB nas dimensoes corretas para plataforma escolhida, respeitando AI-SAFE zone V3 2026, com texto renderizado nas regioes do template + paleta/tipografia da marca aplicadas automaticamente.

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Paleta + tipografia definidas (rodar `marketing-brand-palette` e `marketing-tipografia` antes)
3. Tokens gerados (rodar `marketing-tokens-css` apos definir paleta)
4. Pillow instalado: `pip3 install pillow` (se faltar, gera SVG fallback)

## FLUXO

### 1. Coletar dados

> "Vou gerar PNG. Confirme:
> - Plataforma + formato: instagram.feed_portrait / instagram.feed_grid_3x4 / instagram.stories / instagram.reels / linkedin.post_quadrado / facebook.feed_post / outro
> - Template de layout: imagem-unica / carrossel-capa / carrossel-conteudo / story-cta / story-poll / reels-hook
> - Texto principal (headline): [max 14 palavras]
> - Subtexto opcional: [max 25 palavras]
> - Output path: `<cwd>/marketing/MARKETING/Artes/<slug>/<arquivo>.png`"

Consultar `sizes.json` (`${CLAUDE_PLUGIN_ROOT}/templates/arte-data/sizes.json`) para confirmar dimensoes.

### 2. Validar AI-SAFE zone

Antes de renderizar:
- Carregar `canvas_spec` do `sizes.json[plataforma][formato]`
- Verificar `ai_safe_v3` disponivel; senao usar `ai_safe_v2`
- Confirmar margens (top/base/lat) respeitadas pelo template escolhido

### 3. Verificar deps

Rodar:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py --check-deps
```

Se Pillow faltando: avisar operador
> "Pillow nao instalado. Quer:
> (a) Instalar agora (`pip3 install pillow`) — recomendado
> (b) Gerar SVG fallback — universal, converte depois no Canva"

### 4. Executar render

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py \\
  --template instagram.feed_portrait \\
  --texto "Headline aqui" \\
  --subtexto "Subhead opcional" \\
  --tokens <cwd>/marketing/design-tokens/tokens.json \\
  --sizes ${CLAUDE_PLUGIN_ROOT}/templates/arte-data/sizes.json \\
  --layout centered \\
  --output <cwd>/marketing/MARKETING/Artes/<slug>/peca-01.png
```

Layouts disponiveis:
- `centered` — texto no centro vertical (default para imagem-unica)
- `top-aligned` — texto no topo (default para carrossel-conteudo, story-poll)
- `hero-with-subtext` — titulo no terco superior + subtexto no terco inferior (default para imagem-unica com subhead)

### 5. Validacao pos-render

Apos gerar PNG, validar:
- [ ] Resolucao bate com canvas declarado
- [ ] Texto critico DENTRO da AI-SAFE zone (visualmente verificavel)
- [ ] sRGB color space (Pillow default)
- [ ] Tamanho do arquivo razoavel (PNG-24 raramente passa 1-2 MB em 1080x1350)

### 6. Mostrar resultado + proximos passos

```
OK PNG gerado.

LOCALIZACAO: <cwd>/marketing/MARKETING/Artes/<slug>/peca-01.png
RESOLUCAO: 1080x1350
TAMANHO: <bytes> KB

PROXIMOS PASSOS:
- Visualizar: `open <path>` (Mac) ou `xdg-open <path>` (Linux)
- Publicar via Postiz/Buffer (se integrado em S6) ou subir manualmente
- Para gerar PPTX equivalente (editavel no Canva): rodar marketing-arte-pptx com os mesmos parametros
- Para gerar TODOS os formatos de uma vez (PNG + PPTX): rodar marketing-export-multi-formato
```

## OUTPUT

PNG-24 sRGB no path especificado + validacao + proximos passos.

## VEDACOES ESPECIFICAS

- **NUNCA gerar abaixo de 1080 px de largura** — Instagram estica e fica borrado
- **NUNCA texto critico fora da AI-SAFE zone** — UI da plataforma cobre
- **NUNCA color space CMYK ou DCI-P3** — Instagram converte deslocando cores
- **NUNCA exceder 30 MB** por imagem (Instagram limita)
- **NUNCA renderizar sem consultar MEMORY** — paleta+tipografia tem que vir do workspace

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — formato + template + texto
- **2.3 Producao** — paleta + tipografia + tokens consultados automaticamente
- **2.4 Compliance** — texto submetido a Diretoria R2/R3 antes de renderizar (se peca for publicavel)
