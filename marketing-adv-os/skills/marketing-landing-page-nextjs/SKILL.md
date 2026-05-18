---
name: marketing-landing-page-nextjs
description: >
  MARKETING LANDING PAGE NEXTJS — Gera scaffold Next.js 15 + Tailwind 3.4 (compatible com Tremor Blocks) para projeto que ja tem stack Next.js rodando. Output: app/<slug>/page.tsx + (opcional) componentes em components/ + tokens via globals.css. Stack alinhada com workspace moderno (Next 15 + Tailwind 3.4 + React 18.3). Diferente de marketing-landing-page (HTML puro), esta skill assume que ha repo Next.js ativo — apenas adiciona arquivos. Use quando o operador disser LP em Nextjs, scaffold Next, pagina Next.js, app router page, integrar com projeto Next existente.
---

# MARKETING LANDING PAGE NEXTJS

> Skill Tier 2 (Executor — Producao). Scaffold Next.js 15 + Tailwind 3.4.

## OBJETIVO

Adicionar pagina nova a projeto Next.js 15 existente (App Router) com:
- `app/<slug>/page.tsx` — pagina server component completa
- `components/<slug>/*.tsx` — componentes splittados (opcional)
- Atualizacao de `app/globals.css` com tokens da marca (se nao existe)
- Atualizacao de `tailwind.config.ts` com cores/fontes (se ainda nao tem)

## PRE-REQUISITOS

1. **Operador tem projeto Next.js 15 rodando** (com App Router, NAO Pages Router)
2. **Stack compativel:** Tailwind 3.4+ (NAO v4 que mudou config), React 18.2+
3. Tokens gerados em `<cwd>/marketing/design-tokens/tokens.css`
4. Copy pronto (mesmo de marketing-landing-page)

## FLUXO

### 1. Detectar projeto Next.js

> "Vou gerar scaffold Next.js. Confirme:
> - Path do projeto Next.js (onde fica o `app/` ou `apps/<app>/app/`): [...]
> - Stack confirmada: Next 15 + Tailwind 3.4 + React 18+? (s/n)
> - Slug da rota (URL): [ex: 'curso', 'consultoria', 'lead-magnet']
> - Tipo de LP: venda / captura / evento / demo"

Se Tailwind v4 ou Next < 15: alertar e oferecer ajuste OU usar `marketing-landing-page` (HTML puro) em vez.

### 2. Verificar tokens

Verificar se `<projeto>/app/globals.css` ja tem CSS custom properties da marca. Se nao:
- Copiar `<cwd>/marketing/design-tokens/tokens.css` -> `<projeto>/app/styles/marca-tokens.css`
- Adicionar import no `globals.css`: `@import './styles/marca-tokens.css';`

### 3. Atualizar tailwind.config.ts

Sugerir adicionar ao `theme.extend`:

```ts
// tailwind.config.ts
theme: {
  extend: {
    colors: {
      primary: 'var(--color-primary)',
      secondary: 'var(--color-secondary)',
      accent: 'var(--color-accent)',
      'n-dark': 'var(--color-neutral-dark)',
      'n-light': 'var(--color-neutral-light)',
    },
    fontFamily: {
      primary: ['var(--font-primary)', 'serif'],
      secondary: ['var(--font-secondary)', 'sans-serif'],
    },
  },
},
```

(Ou: copiar `<cwd>/marketing/design-tokens/tailwind.config.snippet.js` e mergir.)

### 4. Gerar app/<slug>/page.tsx

Copiar `<plugin_root>/templates/landing-page/nextjs-page.tsx.template` -> `<projeto>/app/<slug>/page.tsx` substituindo placeholders `{{...}}` pelos valores coletados.

Lista de placeholders (igual ao template HTML, mas com tipagem TS):
- Metadata: `{{TITULO}}`, `{{MARCA}}`, `{{META_DESCRIPTION}}`, `{{OG_IMAGE_URL}}`, `{{URL_CANONICA}}`
- Hero: `{{EYEBROW}}`, `{{HEADLINE_HERO}}`, `{{SUBHEAD_HERO}}`, CTAs
- Arrays tipados: `beneficios[]`, `depoimentos[]`, `faqs[]`
- Oferta: `{{OFERTA_TITULO}}`, `{{OFERTA_DESCRICAO}}`, precos, CTAs
- Footer: `{{DISCLAIMER_LEGAL}}`, `{{ANO}}`, URLs

### 5. Componentes opcionais

Se a LP for grande (>500 linhas), oferecer split em components:

```
app/<slug>/page.tsx           (orquestra)
components/<slug>/
+-- Hero.tsx
+-- Beneficios.tsx
+-- ProvaSocial.tsx
+-- Oferta.tsx
+-- FAQ.tsx
+-- Footer.tsx
```

Cada componente em arquivo proprio com tipagem TS.

### 6. Adicionar metadata SEO

Garantir que `page.tsx` exporta `metadata: Metadata` com:
- title
- description
- openGraph { title, description, images, url, type }
- twitter card

### 7. Verificar deploy

> "PROXIMOS PASSOS:
> 1. Rode `pnpm dev` (ou yarn/npm) no projeto Next
> 2. Acesse `http://localhost:3000/<slug>`
> 3. Validar visualmente: tokens aplicados, responsividade mobile, lighthouse score
> 4. Build de producao: `pnpm build` — checar bundle size < 100 KB First Load JS
> 5. Deploy: Vercel (drag-drop) ou Coolify (Application -> Next.js -> link repo)"

### 8. Diretoria Criativa R3

Mesma validacao da marketing-landing-page:
- VE-04, VE-05, VE-06 (Track A) / VE-12, VE-13 (Track B) / VE-08, VE-09 (LGPD)

## OUTPUT

Arquivos novos no projeto Next.js + instrucoes de uso + checklist pre-deploy.

## VEDACOES ESPECIFICAS

- **NUNCA assumir Tailwind v4** — quebra config; alertar e adaptar OU recusar
- **NUNCA mudar arquivos existentes** sem confirmacao explicita do operador
- **Server Component default** — usar 'use client' SO em componentes interativos (FAQ accordion, formulario)
- **Mesmos VEs da skill HTML** se aplicam aqui
- **Bundle size:** primary LP < 100 KB First Load JS — se passar, dividir componentes

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — confirmacao de stack + slug
- **2.3 Producao** — Tailwind + tokens consistentes
- **2.4 Compliance** — VEs aplicaveis
- **2.5 Mensuracao** — UTMs + Analytics integrado via Next Analytics ou Vercel Analytics
