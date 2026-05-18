---
name: marketing-export-multi-formato
description: >
  MARKETING EXPORT MULTI FORMATO — Recebe UMA peca (texto + template) e gera SIMULTANEAMENTE multiplos formatos otimizados para varias plataformas: Instagram feed_portrait + LinkedIn quadrado + Facebook post + Stories (mesmo hook redimensionado). Sai PNG + PPTX em paralelo. Util para distribuicao multi-plataforma com 1 unica peca conceitual. Use quando o operador disser exportar pra varias redes, gerar pra Instagram + LinkedIn + Facebook, multi-formato, multi-canal, distribuir peca em todas as redes.
---

# MARKETING EXPORT MULTI FORMATO

> Skill Tier 2 (Executor — Arte). Gera multi-formato simultaneo via `scripts/arte-engine.py`.

## OBJETIVO

A partir de UM texto + template, produzir multiplos arquivos otimizados para as plataformas selecionadas (PNG + PPTX cada). Economiza tempo quando a mesma peca conceitual sera distribuida em Instagram + LinkedIn + Facebook + Stories.

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Tokens + sizes prontos
3. Pillow + python-pptx instalados (fallback SVG se faltam)

## FLUXO

### 1. Coletar dados

> "Vou exportar multi-formato. Confirme:
> - Texto principal (headline): [max 14 palavras — sera adaptado por formato se necessario]
> - Subtexto opcional
> - Plataformas (multi-select):
>   [ ] Instagram feed (1080x1350 portrait)
>   [ ] Instagram stories (1080x1920)
>   [ ] LinkedIn post (1200x1200 quadrado)
>   [ ] Facebook feed (1200x630 horizontal)
>   [ ] Email header (600x200)
>   [ ] OG image / LP preview (1200x630)
> - Formatos a gerar: PNG / PPTX / ambos (default ambos)
> - Output base: `<cwd>/marketing/MARKETING/Artes/<slug>/multi-formato/`"

### 2. Validacao de texto pra cada formato

Cada formato tem AI-SAFE diferente — texto que cabe em 1080x1350 pode nao caber em 1200x630 (Facebook horizontal).

Aplicar regra:
- Headlines acima de 12 palavras: alertar e pedir versao mais curta pra formatos horizontais (FB feed, LinkedIn horizontal, email header)
- Subhead acima de 25 palavras: alertar similarmente

### 3. Executar render em loop

```bash
# Loop pelas plataformas selecionadas
for fmt in instagram.feed_portrait instagram.stories linkedin.post_quadrado facebook.feed_post email.header landing_page.og_image; do
  for ext in png pptx; do
    python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py \\
      --template $fmt \\
      --texto "<headline>" --subtexto "<sub>" \\
      --tokens <tokens.json> \\
      --output <cwd>/marketing/MARKETING/Artes/<slug>/multi-formato/${fmt//./_}.${ext}
  done
done
```

### 4. Output estrutura

```
OK Multi-formato exportado.

LOCALIZACAO: <cwd>/marketing/MARKETING/Artes/<slug>/multi-formato/
ARQUIVOS (PNG + PPTX cada):
  - instagram_feed_portrait.png       (1080x1350)
  - instagram_feed_portrait.pptx
  - instagram_stories.png             (1080x1920)
  - instagram_stories.pptx
  - linkedin_post_quadrado.png        (1200x1200)
  - linkedin_post_quadrado.pptx
  - facebook_feed_post.png            (1200x630)
  - facebook_feed_post.pptx
  - email_header.png                  (600x200)
  - email_header.pptx
  - landing_page_og_image.png         (1200x630)
  - landing_page_og_image.pptx
  - DISTRIBUICAO.md                   (instrucoes de uso por canal)

TOTAL: 12 arquivos (6 PNG + 6 PPTX)
```

### 5. Gerar DISTRIBUICAO.md

```markdown
# Plano de Distribuicao — <slug>

## Instagram Feed
- Arquivo: instagram_feed_portrait.png
- Posicao: feed organico (nao stories)
- Horario sugerido: [terca/quinta 19h]
- Caption: <usar copy gerado pela skill correspondente>
- Hashtags: max 10 mix amplo+medio+nicho

## Instagram Stories
- Arquivo: instagram_stories.png (ou sequencia se multi-tela)
- Sticker: link na CTA box (se aplicavel)
- Duracao: 24h (re-publicar destaque se relevante)

## LinkedIn
- Arquivo: linkedin_post_quadrado.png (preferido pra real estate mobile)
- Caption: versao longa + 5 hashtags max
- Horario: terca/quarta 9-11h

## Facebook
- Arquivo: facebook_feed_post.png (horizontal 1.91:1)
- Caption: similar ao IG mas adaptar tom (publico FB e mais cauteloso/conservador)

## Email (newsletter)
- Arquivo: email_header.png (600x200, fixed-width)
- Inserir no topo do email — antes da headline + corpo

## Landing Page (OG image)
- Arquivo: landing_page_og_image.png (1200x630)
- Inserir como og:image meta tag no <head> do HTML
- Aparece em previews de FB/LinkedIn/WhatsApp quando link e compartilhado
```

### 6. Validacao consolidada

Apos gerar, mostrar relatorio:

```
RELATORIO DE EXPORT MULTI-FORMATO:

Texto base: "<headline>"
Subtexto: "<sub>"
Paleta: primary=<hex> | secondary=<hex> | accent=<hex>
Tipografia: <primary> + <secondary>

Formatos gerados: 6 plataformas x 2 formatos = 12 arquivos
Total bytes: <X> KB

AVISOS:
- <Se houve aviso de texto longo para formato horizontal>
- <Se algum formato falhou>

PROXIMOS PASSOS:
- Revisar visualmente cada formato antes de distribuir
- Pequenos ajustes (corte, reposicionamento) podem ser feitos editando o PPTX
- Distribuir conforme DISTRIBUICAO.md
- Agendar via Postiz/Buffer (se integrado em S6)
```

## OUTPUT

12 arquivos (PNG + PPTX por plataforma) + DISTRIBUICAO.md + relatorio consolidado.

## VEDACOES ESPECIFICAS

- **VE-14:** se as artes vao com conteudo IA-gerado em area sensivel, declarar
- **NUNCA** assumir que mesmo texto cabe igualmente em 1080x1350 e em 1200x630 — alertar quando excede
- **NUNCA** ratio inconsistente entre formatos do MESMO carrossel (esta skill cobre PECAS diferentes, nao carrossel)
- **Atomicidade:** se um formato falha, AVISAR mas continuar gerando os outros — nao bloquear tudo

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — plataformas selecionadas
- **2.3 Producao** — paleta + tipografia consistentes em TODAS as plataformas
- **2.5 Mensuracao** — DISTRIBUICAO.md ja sugere horarios e formatos por plataforma
