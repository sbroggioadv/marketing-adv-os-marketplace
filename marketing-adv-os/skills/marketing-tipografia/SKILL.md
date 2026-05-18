---
name: marketing-tipografia
description: >
  MARKETING TIPOGRAFIA — Define fontes primary e secondary da marca + hierarquia tipografica (h1-h6, body, caption) + tamanhos sugeridos. Persiste em `<cwd>/marketing/MEMORY.md` secao **## Identidade Visual** subsecao Tipografia + `cowork-state.json` campo `identity.typography`. Suporta Google Fonts (carregadas via URL Fonts API) ou fontes do sistema (Inter, system-ui, Georgia, etc). Track-aware: Track A sugere serifa editorial (Playfair Display, EB Garamond, Lora); Track B sugere sans-serif moderno (Inter, Manrope, Space Grotesk, Outfit). Use quando o operador disser definir tipografia, escolher fonte, fonte da marca, typography, mudar fonte.
---

# MARKETING TIPOGRAFIA

> Skill Tier 1 (Estado-maior — Brand). Define fontes da marca e persiste no MEMORY.

## OBJETIVO

Construir ou atualizar tipografia da marca (fonte primaria + secundaria + hierarquia), salvando em `<cwd>/marketing/MEMORY.md` secao `## Identidade Visual` subsecao Tipografia + atualizando `<cwd>/marketing/cowork-state.json` campo `identity.typography`.

## PRE-REQUISITOS

- Workspace marketing configurado. Se nao: sugerir `/start-marketing` antes.
- Track ja definido — determina sugestoes.

## FLUXO

### 1. Mostrar sugestoes track-aware

**Track A — Advogado/Escritorio:**
> "Sugestoes de tipografia institucional (use serifa para titulos):
>
> **Combos validados:**
> (a) Playfair Display + Inter — editorial elegante (default Track A)
> (b) EB Garamond + Inter — classico, sobrio
> (c) Lora + Source Sans Pro — humanizado
> (d) Crimson Pro + Source Serif Pro — academico
> (e) Custom — informe as duas fontes manualmente"

**Track B — Empresario/Criador:**
> "Sugestoes de tipografia moderna (sans-serif para titulos + body):
>
> **Combos validados:**
> (a) Inter + Inter — neutro, versatil (default Track B)
> (b) Space Grotesk + Inter — tech, ousado
> (c) Manrope + Inter — geometrico, premium
> (d) Outfit + Inter — moderno, jovem
> (e) DM Sans + DM Serif Display — contraste serifa+sans
> (f) Custom — informe as duas fontes manualmente"

### 2. Opcao Custom

> "Fonte primaria (titulos)? Pode ser Google Font (ex: 'Playfair Display') ou system (ex: 'system-ui', 'Georgia')."
> "Fonte secundaria (corpo)? Idem."

Validar se fonte parece valida. Aviso se nome contem caracteres estranhos.

### 3. Confirmar via mood board

Sugerir gerar mood board imediato:
> "Vou aplicar essa tipografia. Quer que eu rode `marketing-visual-identity` agora pra voce ver a tipografia aplicada na hierarquia? (s/n)"

Se sim: invocar skill correspondente apos persistir.

### 4. Definir hierarquia padrao

Hierarquia sugerida automaticamente:

```
H1: <primary> bold     56-72px line-height 1.1
H2: <primary> semibold 36-48px line-height 1.15
H3: <primary> medium   24-32px line-height 1.2
H4: <primary> medium   20-24px line-height 1.3
Body: <secondary> regular  16-18px line-height 1.6
Caption: <secondary> regular  13-14px line-height 1.4
Quote: <primary> italic  20-24px line-height 1.5
Code: monospace regular  14-15px line-height 1.5
```

Perguntar se aceita os defaults ou quer ajustar tamanhos.

### 5. Persistir

Atualizar `<cwd>/marketing/cowork-state.json` campo `identity.typography`:

```json
"identity": {
  "typography": {
    "primary": "Playfair Display",
    "primary_fallback": "Georgia, serif",
    "primary_weights": [400, 600, 700],
    "secondary": "Inter",
    "secondary_fallback": "system-ui, sans-serif",
    "secondary_weights": [400, 500, 600],
    "scale": {
      "h1": { "size": 64, "weight": 700, "line_height": 1.1 },
      "h2": { "size": 40, "weight": 600, "line_height": 1.15 },
      "h3": { "size": 28, "weight": 500, "line_height": 1.2 },
      "body": { "size": 17, "weight": 400, "line_height": 1.6 },
      "caption": { "size": 14, "weight": 400, "line_height": 1.4 }
    },
    "source": "google-fonts | system | custom",
    "version": 2,
    "last_update": "2026-05-17T14:30:00Z"
  }
}
```

Atualizar `<cwd>/marketing/MEMORY.md` secao `## Identidade Visual` -> subsecao Tipografia.

### 6. Gerar URL Google Fonts (se aplicavel)

Se primary OU secondary sao Google Fonts, gerar URL pronta:

```
https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@400;500;600&display=swap
```

Salvar em `identity.typography.google_fonts_url`. Skill `marketing-tokens-css` consome.

### 7. Confirmar e proximos passos

```
OK Tipografia atualizada (v2).

Primaria:   Playfair Display (Google Fonts — pesos 400, 600, 700)
Secundaria: Inter (Google Fonts — pesos 400, 500, 600)

URL Google Fonts gerada: https://fonts.googleapis.com/css2?family=...

PROXIMOS PASSOS:
- `marketing-visual-identity` -> ver fonte aplicada em mood board
- `marketing-tokens-css` -> gerar tokens.css com font-family + scale
- `marketing-brand-guidelines` -> regenerar guideline consolidado
```

## OUTPUT ESPERADO

- `<cwd>/marketing/cowork-state.json` atualizado em `identity.typography`
- `<cwd>/marketing/MEMORY.md` secao Tipografia atualizada
- URL Google Fonts gerada (se aplicavel)
- Mensagem de confirmacao

## VEDACOES ESPECIFICAS

- NUNCA aceitar fonte sem fallback definido (system-ui ou serif/sans-serif)
- NUNCA usar mais de 2 fontes principais (primary + secondary) — terceira so se for monospace para code blocks
- NUNCA pular validacao de pesos disponiveis (Google Fonts: se pediu peso 900 mas fonte so tem 400/700, alertar)

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — tipografia compoe identidade
- **2.3 Producao** — skills de arte/LP consomem tipografia
