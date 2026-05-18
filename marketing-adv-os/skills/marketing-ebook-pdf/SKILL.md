---
name: marketing-ebook-pdf
description: >
  MARKETING EBOOK PDF — Converte manuscript.md em PDF profissional via WeasyPrint (primario) ou pandoc (fallback) ou HTML standalone (ultimo fallback). Aplica paleta + tipografia + scale do tokens.json. Layout A4 com margens calibradas (25mm top, 22mm laterais, 28mm bottom), numero de pagina, header com titulo, capa dedicada, sumario automatico, hifenizacao, page-break inteligente entre capitulos. Use quando o operador disser converter ebook em PDF, gerar PDF do ebook, exportar ebook, ebook final, PDF para download.
---

# MARKETING EBOOK PDF

> Skill Tier 2 (Executor — Producao). Converte MD em PDF via `scripts/ebook-engine.py`.

## OBJETIVO

Transformar `manuscript.md` (gerado por `marketing-ebook-md`) em PDF profissional pronto para distribuicao (download de lead magnet, produto de entrada, material pra equipe externa). Layout A4 com tipografia e paleta da marca aplicadas.

## PRE-REQUISITOS

1. Workspace + MEMORY configurado
2. Tokens gerados (`<cwd>/marketing/design-tokens/tokens.json`)
3. Manuscrito MD existente (`marketing-ebook-md` ja rodou)
4. Pelo menos UMA das dependencies:
   - WeasyPrint: `pip3 install weasyprint markdown` (preferido — CSS3 completo)
   - Pandoc CLI: `brew install pandoc basictex` (fallback — requer LaTeX)
   - Sem nenhum: gera HTML standalone para conversao manual via browser

## FLUXO

### 1. Verificar deps

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ebook-engine.py --check-deps
```

Se nenhum disponivel:
> "Nenhum engine PDF disponivel. Opcoes:
> (a) Instalar WeasyPrint (recomendado): `pip3 install weasyprint markdown`
>     - Mais profissional, controle CSS completo
>     - Requer libs nativas (Cairo, Pango) — Mac: ja vem; Linux: `apt install libcairo2`
> (b) Instalar pandoc (alternativo): `brew install pandoc basictex` (Mac) ou `apt install pandoc texlive-xetex` (Linux)
>     - Mais ubiquo mas menos controle de design
> (c) Prosseguir com HTML standalone — abrir no Chrome > Imprimir > Salvar como PDF"

### 2. Briefing

> "Vou gerar PDF do ebook. Confirme:
> - Path do manuscrito: `<cwd>/marketing/MARKETING/Ebooks/<slug>/manuscript.md`
> - Titulo do ebook (para header e capa)
> - Autor
> - Path da capa (opcional, gerado por marketing-arte-png): `cover.png`
> - Engine preferida: weasyprint (default) / pandoc / html (forcar fallback)
> - Output: `<cwd>/marketing/MARKETING/Ebooks/<slug>/ebook.pdf`"

### 3. Executar render

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/ebook-engine.py \\
  --input <cwd>/marketing/MARKETING/Ebooks/<slug>/manuscript.md \\
  --tokens <cwd>/marketing/design-tokens/tokens.json \\
  --titulo "<titulo>" \\
  --autor "<autor>" \\
  --capa <cwd>/marketing/MARKETING/Ebooks/<slug>/cover.png \\
  --output <cwd>/marketing/MARKETING/Ebooks/<slug>/ebook.pdf
```

Engine aplica:
- Capa dedicada (page 1) com background `primary` color + titulo grande + autor em accent
- Sumario automatico (page 2)
- Header com titulo em cada pagina (exceto capa)
- Footer com numero de pagina
- Page-break antes de cada `## Capitulo N`
- Margens A4 calibradas (25mm/22mm/28mm/22mm)
- Hifenizacao automatica
- Codigo em `pre/code` com background neutral_light
- Blockquote com border-left em accent color
- Tabelas com borda discreta e header em neutral_light

### 4. Output esperado

```
OK PDF gerado.

LOCALIZACAO: <cwd>/marketing/MARKETING/Ebooks/<slug>/ebook.pdf
TAMANHO: <X> MB
PAGINAS: <N>
ENGINE USADO: weasyprint (ou pandoc / html)

QUALIDADE:
- Capa: <com imagem cover.png | sem imagem (so texto)>
- Sumario: gerado automaticamente
- Numero de paginas: footer center
- Header: titulo + linha superior
- Tipografia: <fonte_primary> (titulos) + <fonte_secondary> (corpo)

PROXIMOS PASSOS:
- Abrir: `open <path>`
- Revisar visualmente: capa, primeira pagina de cada capitulo, quebras
- Subir como lead magnet em LP (consumir via marketing-landing-page)
- Hospedar em CDN/S3 se for download massivo
- Versionar: re-rodar com versao incrementada (v1.0 -> v1.1 -> ...)
```

### 5. Otimizacao opcional

Apos gerar, oferecer:
- Compressao: `qpdf --linearize ebook.pdf ebook-optimized.pdf` (reduz tamanho de download)
- Versao light (so texto, sem imagens): para email marketing leve
- Versao print-ready (CMYK): se for impressao fisica

### 6. Diretoria Criativa R4 (Performance)

Validar:
- [ ] Tamanho do PDF razoavel (< 5 MB para 30 paginas; < 15 MB para 100 paginas)
- [ ] Carrega em < 3 segundos em conexao 4G
- [ ] Acessibilidade: PDF com texto selecionavel (NAO raster-only)
- [ ] OG image gerada para preview ao compartilhar link de download
- [ ] UTM no link de download para tracking de quem baixou

## OUTPUT

PDF profissional + relatorio + plano de distribuicao.

## VEDACOES ESPECIFICAS

- **NUNCA gerar PDF raster-only** (texto como imagem) — quebra acessibilidade + busca interna
- **NUNCA encarpetar o PDF** com cores que dificultam impressao (preto puro de fundo gasta toner)
- **PDF > 20 MB:** alertar — pode quebrar email marketing (limites Gmail/Outlook)
- **CMYK so se for print real:** PDF digital em CMYK desloca cores em browsers

## PROTOCOLOS ACIONADOS

- **2.3 Producao** — paleta + tipografia aplicadas via tokens
- **2.4 Compliance** — disclaimer LGPD + (Track A) OAB presente no rodape do PDF
- **2.5 Mensuracao** — UTM no link de download + tracking de aberturas

## TROUBLESHOOTING

### WeasyPrint falha "libcairo not found"
Mac: `brew install cairo pango gdk-pixbuf libffi`
Linux Ubuntu: `apt install libcairo2 libpango-1.0-0 libpangocairo-1.0-0`

### Pandoc falha "xelatex not found"
Mac: `brew install --cask mactex` (~4 GB) ou `brew install basictex` (~200 MB)
Linux: `apt install texlive-xetex texlive-fonts-recommended`

### HTML standalone — converter para PDF manualmente
1. Abrir HTML no Chrome
2. Cmd/Ctrl + P
3. Destino: "Salvar como PDF"
4. Configurar:
   - Tamanho: A4
   - Margens: padroes
   - Mais configuracoes -> Cabecalhos e rodapes: desativar (engine ja gera)
5. Salvar
