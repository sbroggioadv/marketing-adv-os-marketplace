---
name: marketing-tokens-css
description: >
  MARKETING TOKENS CSS — Gera `tokens.css` (CSS custom properties) + `tokens.json` (estruturado) em `<cwd>/marketing/design-tokens/` consumindo paleta + tipografia + scale registrados no MEMORY. Output direto-consumivel por landing pages HTML, Next.js, Tailwind CSS (config), React Native, scripts Python (Pillow). Inclui dark mode opcional. Use quando o operador disser gerar tokens, exportar tokens, tokens.css, tokens.json, gerar variaveis CSS, design tokens, tailwind config, exportar paleta para codigo.
---

# MARKETING TOKENS CSS

> Skill Tier 1 (Estado-maior — Brand). Exporta paleta + tipografia para formato consumivel por codigo.

## OBJETIVO

Materializar a identidade da marca (paleta + tipografia + scale) em arquivos consumiveis:
- `tokens.css` — CSS custom properties (`:root { --primary: #...; ... }`) usavel direto em qualquer HTML
- `tokens.json` — JSON estruturado consumivel por scripts Python (Pillow), JS, Tailwind config, design systems

## PRE-REQUISITOS

- Workspace marketing configurado
- Paleta definida (obrigatorio)
- Tipografia definida (recomendado — fallback system-ui se nao)

## FLUXO

### 1. Carregar dados do MEMORY

Ler `<cwd>/marketing/cowork-state.json`:
- `identity.palette` (5 hex codes + nomes)
- `identity.typography` (primary + secondary + scale + google_fonts_url)

Se paleta vazia: bloquear:
> "Tokens precisa de paleta definida. Rode `marketing-brand-palette` antes."

### 2. Gerar tokens.css

```css
/* Design Tokens — <MARCA>
 * Gerado por marketing-adv-os v<version>
 * Versao: <version> · <date>
 * NAO editar manualmente — re-rodar `marketing-tokens-css` apos qualquer mudanca em palette/typography
 */

@import url('<GOOGLE_FONTS_URL>');

:root {
  /* ===== PALETA ===== */
  --color-primary:        <PALETTE_PRIMARY>;
  --color-secondary:      <PALETTE_SECONDARY>;
  --color-accent:         <PALETTE_ACCENT>;
  --color-neutral-dark:   <PALETTE_NEUTRAL_DARK>;
  --color-neutral-light:  <PALETTE_NEUTRAL_LIGHT>;

  /* Aliases semanticos (uso comum) */
  --bg:        var(--color-neutral-light);
  --bg-dark:   var(--color-neutral-dark);
  --text:      var(--color-neutral-dark);
  --text-inv:  var(--color-neutral-light);
  --cta:       var(--color-accent);
  --cta-text:  var(--color-neutral-dark);
  --link:      var(--color-accent);

  /* Variantes com opacidade (gerar em runtime via mix) */
  --color-primary-10:   color-mix(in srgb, var(--color-primary) 10%, transparent);
  --color-primary-50:   color-mix(in srgb, var(--color-primary) 50%, transparent);
  --color-secondary-10: color-mix(in srgb, var(--color-secondary) 10%, transparent);

  /* ===== TIPOGRAFIA ===== */
  --font-primary:    '<TYPO_PRIMARY>', <TYPO_PRIMARY_FALLBACK>;
  --font-secondary:  '<TYPO_SECONDARY>', <TYPO_SECONDARY_FALLBACK>;
  --font-mono:       'JetBrains Mono', 'Courier New', monospace;

  /* Scale (mobile-first; desktop ajusta via media query) */
  --fs-h1:      <H1_SIZE>px;
  --fs-h2:      <H2_SIZE>px;
  --fs-h3:      <H3_SIZE>px;
  --fs-body:    <BODY_SIZE>px;
  --fs-caption: <CAPTION_SIZE>px;

  --fw-h1:      <H1_WEIGHT>;
  --fw-h2:      <H2_WEIGHT>;
  --fw-h3:      <H3_WEIGHT>;
  --fw-body:    <BODY_WEIGHT>;

  --lh-h1:      <H1_LINE_HEIGHT>;
  --lh-h2:      <H2_LINE_HEIGHT>;
  --lh-body:    <BODY_LINE_HEIGHT>;

  /* ===== ESPACAMENTO (escala 4px) ===== */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;
  --space-24: 96px;

  /* ===== BORDA / RADIUS ===== */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-pill: 999px;

  /* ===== SHADOWS ===== */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 24px rgba(0,0,0,0.15);

  /* ===== BREAKPOINTS (uso em media queries) ===== */
  --bp-mobile:  640px;
  --bp-tablet:  768px;
  --bp-desktop: 1024px;
  --bp-wide:    1280px;
}

/* Dark mode opcional (auto via prefers-color-scheme) */
@media (prefers-color-scheme: dark) {
  :root {
    --bg:        var(--color-neutral-dark);
    --bg-dark:   var(--color-neutral-light);
    --text:      var(--color-neutral-light);
    --text-inv:  var(--color-neutral-dark);
  }
}

/* Aplicacao default */
body {
  font-family: var(--font-secondary);
  font-size: var(--fs-body);
  font-weight: var(--fw-body);
  line-height: var(--lh-body);
  color: var(--text);
  background: var(--bg);
}

h1 { font-family: var(--font-primary); font-size: var(--fs-h1); font-weight: var(--fw-h1); line-height: var(--lh-h1); }
h2 { font-family: var(--font-primary); font-size: var(--fs-h2); font-weight: var(--fw-h2); }
h3 { font-family: var(--font-primary); font-size: var(--fs-h3); font-weight: var(--fw-h3); }
.caption { font-size: var(--fs-caption); }

.btn-cta {
  background: var(--cta);
  color: var(--cta-text);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: 600;
}
```

### 3. Gerar tokens.json

```json
{
  "_generated_by": "marketing-adv-os",
  "_version": "<version>",
  "_generated_at": "<date>",
  "marca": "<MARCA>",
  "palette": {
    "primary": "<PALETTE_PRIMARY>",
    "primary_name": "<PALETTE_PRIMARY_NAME>",
    "secondary": "<PALETTE_SECONDARY>",
    "secondary_name": "<PALETTE_SECONDARY_NAME>",
    "accent": "<PALETTE_ACCENT>",
    "accent_name": "<PALETTE_ACCENT_NAME>",
    "neutral_dark": "<PALETTE_NEUTRAL_DARK>",
    "neutral_light": "<PALETTE_NEUTRAL_LIGHT>"
  },
  "typography": {
    "primary": "<TYPO_PRIMARY>",
    "primary_fallback": "<TYPO_PRIMARY_FALLBACK>",
    "primary_weights": [400, 600, 700],
    "secondary": "<TYPO_SECONDARY>",
    "secondary_fallback": "<TYPO_SECONDARY_FALLBACK>",
    "secondary_weights": [400, 500, 600],
    "google_fonts_url": "<GOOGLE_FONTS_URL>"
  },
  "scale": {
    "h1": { "size": 64, "weight": 700, "line_height": 1.1 },
    "h2": { "size": 40, "weight": 600, "line_height": 1.15 },
    "h3": { "size": 28, "weight": 500, "line_height": 1.2 },
    "body": { "size": 17, "weight": 400, "line_height": 1.6 },
    "caption": { "size": 14, "weight": 400, "line_height": 1.4 }
  },
  "spacing": [4, 8, 12, 16, 24, 32, 48, 64, 96],
  "radius": { "sm": 4, "md": 8, "lg": 12, "xl": 16, "pill": 999 },
  "breakpoints": { "mobile": 640, "tablet": 768, "desktop": 1024, "wide": 1280 }
}
```

### 4. Gerar tailwind.config.snippet.js (bonus)

Operador pediu Tailwind? Gerar snippet pronto:

```js
// tailwind.config.snippet.js — colar em theme.extend do tailwind.config.ts
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '<PALETTE_PRIMARY>',
        secondary: '<PALETTE_SECONDARY>',
        accent: '<PALETTE_ACCENT>',
        'n-dark': '<PALETTE_NEUTRAL_DARK>',
        'n-light': '<PALETTE_NEUTRAL_LIGHT>',
      },
      fontFamily: {
        primary: ['<TYPO_PRIMARY>', '<TYPO_PRIMARY_FALLBACK>'],
        secondary: ['<TYPO_SECONDARY>', '<TYPO_SECONDARY_FALLBACK>'],
      },
    },
  },
};
```

### 5. Salvar

Criar `<cwd>/marketing/design-tokens/` se nao existe. Escrever:
- `tokens.css`
- `tokens.json`
- `tailwind.config.snippet.js` (bonus)
- `README.md` curto explicando uso

Se arquivos ja existem: backup automatico `.bak.<timestamp>`.

### 6. Confirmar

```
OK Design tokens gerados.

LOCALIZACAO: <cwd>/marketing/design-tokens/
ARQUIVOS:
  - tokens.css      (CSS custom properties — usar em LP/site)
  - tokens.json     (JSON estruturado — usar em Python/JS)
  - tailwind.config.snippet.js   (Tailwind config — colar em theme.extend)
  - README.md

USO:
  HTML/CSS:        <link rel="stylesheet" href="path/tokens.css">
  Tailwind:        copiar snippet pra tailwind.config
  Python (Pillow): json.load(open('tokens.json'))['palette']
  Next.js:         importar via PostCSS ou copiar custom properties para globals.css

PROXIMOS PASSOS:
- Atualizar LPs existentes pra consumir tokens.css
- Compartilhar pasta `design-tokens/` com desenvolvedores externos
- Re-rodar quando palette/typography mudar
```

## OUTPUT ESPERADO

- `<cwd>/marketing/design-tokens/tokens.css`
- `<cwd>/marketing/design-tokens/tokens.json`
- `<cwd>/marketing/design-tokens/tailwind.config.snippet.js`
- `<cwd>/marketing/design-tokens/README.md`
- Backups se existiam
- Mensagem confirmacao

## VEDACOES ESPECIFICAS

- NUNCA gerar tokens sem ler MEMORY atual
- NUNCA sobrescrever sem backup
- NUNCA omitir versao + timestamp no header dos arquivos

## PROTOCOLOS ACIONADOS

- **2.3 Producao** — tokens sao input direto de toda producao em codigo
