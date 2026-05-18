---
name: marketing-landing-page
description: >
  MARKETING LANDING PAGE — Gera landing page HTML5+CSS3 puro (sem framework, zero deps de runtime) consumindo tokens.css + voz + publico + oferta do MEMORY. Estrutura: hero + beneficios + prova social + oferta + FAQ + footer LGPD. Output `<cwd>/marketing/MARKETING/Landing-Pages/<slug>/index.html` pronto para deploy estatico (Vercel/Coolify/Netlify/CloudFlare Pages/GitHub Pages/qualquer hosting). Inclui Open Graph tags para preview em FB/LinkedIn/WhatsApp + favicon + politica de privacidade linkada. Track A: cuidado VE-04 e VE-06 (sem promessa de resultado e sem captacao agressiva). Use quando o operador disser gerar landing page HTML, LP estatica, pagina simples, LP sem framework, pagina pronta pra deploy.
---

# MARKETING LANDING PAGE

> Skill Tier 2 (Executor — Producao). Gera LP HTML5+CSS3 estatica.

## OBJETIVO

Produzir landing page em arquivo unico HTML (com tokens.css separado) pronta para deploy em qualquer hosting estatico. Output respeitando paleta + tipografia + voz da marca, com estrutura de conversao calibrada e compliance LGPD.

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Tokens gerados (`marketing-tokens-css` ou ja existe em `<cwd>/marketing/design-tokens/`)
3. Copy pronto para hero, beneficios, prova social, oferta, FAQ (se nao tem, sugerir rodar skills de copy antes)

## FLUXO

### 1. Briefing

> "Vou gerar LP HTML estatica. Confirme:
> - Slug da LP (URL path): [ex: 'curso-tributario', 'consultoria-juridica', 'lead-magnet-mes']
> - Titulo da pagina (vai pra <title> e og:title)
> - Tipo de LP: (a) venda direta (checkout) / (b) captura de lead (formulario) / (c) inscricao em evento / (d) demo agendamento
> - URL canonica (onde sera publicada)
> - URL do checkout/CTA primario
> - Output: `<cwd>/marketing/MARKETING/Landing-Pages/<slug>/`"

### 2. Coletar copy (consultar skills se faltam)

Verificar disponibilidade de:
- **Hero:** headline + subhead + eyebrow + CTA primario + CTA secundario
- **Beneficios:** 3-6 cards (titulo + descricao curta)
- **Prova social:** 2-4 depoimentos (fala + autor) — Track A: autorizacao escrita VE-15
- **Oferta:** titulo + descricao + preco + ancoragem (se aplicavel) + garantia + CTA final
- **FAQ:** 5-8 perguntas + respostas
- **Footer:** politica de privacidade URL + termos URL + disclaimer LGPD/OAB

Se algum bloco esta vazio: oferecer rodar skill correspondente (marketing-copy-headline-landing-page, marketing-copy-post-depoimento, marketing-copy-case-success, etc).

### 3. Gerar estrutura de arquivos

```
<cwd>/marketing/MARKETING/Landing-Pages/<slug>/
+-- index.html         (LP completa — substituicoes feitas)
+-- tokens.css         (copia de <cwd>/marketing/design-tokens/tokens.css)
+-- favicon.png        (placeholder ou favicon gerado se ha logo)
+-- assets/            (imagens de hero, og_image, depoimentos)
    +-- og-image.png   (gerado por marketing-export-multi-formato 1200x630)
+-- README.md          (instrucoes de deploy + checklist pre-go-live)
```

### 4. Renderizar HTML

Copiar `<plugin_root>/templates/landing-page/base.html` -> `<cwd>/.../index.html` substituindo TODOS os placeholders Mustache `{{...}}` pelos valores coletados.

Lista de placeholders:
- `{{TITULO}}`, `{{MARCA}}`, `{{META_DESCRIPTION}}`, `{{OG_IMAGE_URL}}`, `{{URL_CANONICA}}`, `{{FAVICON_URL}}`, `{{ANO}}`
- `{{EYEBROW}}`, `{{HEADLINE_HERO}}`, `{{SUBHEAD_HERO}}`, `{{CTA_PRIMARIO_TEXTO}}`, `{{CTA_PRIMARIO_URL}}`, `{{CTA_SECUNDARIO_TEXTO}}`, `{{CTA_SECUNDARIO_URL}}`
- `{{BENEFICIOS_TITULO}}`, `{{BENEFICIO_N_TITULO}}`, `{{BENEFICIO_N_DESC}}` (para N=1..6)
- `{{PROVA_SOCIAL_TITULO}}`, `{{DEPOIMENTO_N_FALA}}`, `{{DEPOIMENTO_N_AUTOR}}` (para N=1..4)
- `{{OFERTA_TITULO}}`, `{{OFERTA_DESCRICAO}}`, `{{PRECO_OFERTA}}`, `{{PRECO_ANCORAGEM}}` (opcional), `{{CTA_OFERTA_TEXTO}}`, `{{CHECKOUT_URL}}`, `{{GARANTIA_TEXTO}}`
- `{{FAQ_N_PERGUNTA}}`, `{{FAQ_N_RESPOSTA}}` (para N=1..8)
- `{{DISCLAIMER_LEGAL}}`, `{{POLITICA_PRIVACIDADE_URL}}`, `{{TERMOS_URL}}`

### 5. Gerar README.md de deploy

```markdown
# Landing Page: <slug>

## Deploy

### Vercel (recomendado para Next.js)
1. Subir pasta como repo GitHub
2. Importar no Vercel -> automatic deploy
3. Configurar dominio em vercel.com/dashboard

### Coolify (self-hosted)
1. Application -> Static Site
2. Apontar para o repo
3. Build command: (vazio — e HTML estatico)
4. Output dir: `.`

### Netlify / Cloudflare Pages
- Drag-and-drop a pasta inteira na dashboard
- OU conectar repo GitHub

### Local (teste)
- Abrir `index.html` no browser OU
- `python3 -m http.server 8000` na pasta -> http://localhost:8000

## Checklist pre-go-live

- [ ] index.html carrega corretamente em desktop + mobile
- [ ] tokens.css aplicado (paleta + tipografia visiveis)
- [ ] favicon.png aparece na aba
- [ ] og-image.png correto (1200x630) — testar preview em https://opengraph.dev
- [ ] Todos os links funcionam (CTA primario, secundario, checkout, FAQ deep-links)
- [ ] Politica de privacidade + Termos de uso publicados (LP-orfas violam LGPD)
- [ ] Formulario (se houver) submete pra endpoint correto + LGPD opt-in marcado
- [ ] Disclaimer legal visivel no footer
- [ ] Lighthouse score >= 90 em todas as categorias (performance, accessibility, SEO, best practices)

## Manutencao
Reeditar: ajustar diretamente o HTML OU re-rodar `marketing-landing-page` com mesmo slug (gera backup .bak).
```

### 6. Validacao + Diretoria Criativa R3

Antes de declarar concluido:
- Track A: rodar checklist VE-04 (sem promessa resultado), VE-05 (sem mercantilizacao), VE-06 (sem captacao agressiva). Disclaimer OAB obrigatorio no footer.
- Track B: VE-12 (sem propaganda enganosa), VE-01 (sem superlativo sem prova), VE-13 (se ha parceria paga declarar).
- Universal: VE-08, VE-09 (LGPD — link pra politica de privacidade obrigatorio + opt-in se ha formulario).

## OUTPUT

Pasta completa em `<cwd>/marketing/MARKETING/Landing-Pages/<slug>/` com index.html + tokens.css + README + checklist + assets.

## VEDACOES ESPECIFICAS

- **VE-08, VE-09 (LGPD) — CRITICA:** sem link pra politica de privacidade no footer = NAO publicar
- **VE-04 (Track A):** sem promessa de resultado em hero/beneficios/oferta
- **VE-05 (Track A):** sem "ULTIMA CHANCE!!" — sem urgencia fabricada
- **VE-13:** se ha parceria, declarar
- **NUNCA og:image faltando** — quebra preview em WhatsApp/FB/LinkedIn

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — slug + tipo de LP + URLs
- **2.3 Producao** — tokens + voz consumidos automaticamente
- **2.4 Compliance** — VEs track-aware + LGPD critica
- **2.5 Mensuracao** — sugerir UTMs nos links + analytics setup
