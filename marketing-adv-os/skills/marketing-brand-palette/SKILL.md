---
name: marketing-brand-palette
description: >
  MARKETING BRAND PALETTE — Define ou atualiza a paleta de cores da marca, persistindo em `<cwd>/marketing/MEMORY.md` secao **## Identidade Visual** (consultada automaticamente por TODA skill de arte, landing page, ebook e slides). Suporta 3 modos: (1) preset entre 5 paletas curadas (Bege+Charcoal institucional, Lime+Black ousado, Azul+Branco corporativo, Roxo+Rose moderno, Verde+Creme natural); (2) custom com 5 hex codes informados (primary, secondary, accent, neutral_dark, neutral_light); (3) importar de URL — Pillow extrai cores dominantes do site/portfolio existente. Use quando o operador disser definir paleta, mudar cores, criar identidade visual, importar cores do site, paleta da marca, hex codes, cores da empresa, /marketing-master trocar paleta.
---

# MARKETING BRAND PALETTE

> Skill Tier 1 (Estado-maior — Brand). Define a paleta de cores da marca e persiste no MEMORY.

## OBJETIVO

Construir ou atualizar a paleta de 5 cores (primary, secondary, accent, neutral_dark, neutral_light) da marca, salvando em `<cwd>/marketing/MEMORY.md` secao `## Identidade Visual` + atualizando `<cwd>/marketing/cowork-state.json` campo `identity.palette`.

## PRE-REQUISITOS

- Workspace marketing configurado (`<cwd>/marketing/cowork-state.json` existe). Se nao, sugerir `/start-marketing` antes.

## FLUXO

### 1. Perguntar o modo

> "Vamos definir/atualizar a paleta. Qual modo?
>
> (1) **Preset** — escolha entre 5 paletas curadas
> (2) **Custom** — informe 5 hex codes
> (3) **Import URL** — extrai cores dominantes de site/portfolio existente"

### 2A. Modo PRESET

Mostrar 5 paletas com preview ASCII:

```
(a) BEGE CHAMPANHE + CHARCOAL — institucional, elegante (recomendado Track A)
    primary   #F4E5C5  (champanhe)
    secondary #2C2C2C  (charcoal)
    accent    #B8860B  (gold)
    n_dark    #1A1A1A
    n_light   #FAF7EE

(b) LIME KINETIC + BLACK OBSIDIAN — ousado, manifesto (recomendado para techn/cursos)
    primary   #CCFF00  (lime)
    secondary #101010  (obsidian)
    accent    #FFFFFF
    n_dark    #050505
    n_light   #F5F5F5

(c) AZUL MARINHO + BRANCO QUENTE — corporativo, confiavel (recomendado Track A institucional)
    primary   #1E3A8A  (navy)
    secondary #FFFCF5  (warm white)
    accent    #F59E0B  (amber)
    n_dark    #0F1729
    n_light   #F3F4F6

(d) ROXO TECH + ROSE CORAL — moderno, criativo (recomendado Track B SaaS/criadores)
    primary   #7C3AED  (violet)
    secondary #FB7185  (coral)
    accent    #FCD34D  (sun)
    n_dark    #18181B
    n_light   #FAFAFA

(e) VERDE FOLHA + CREME NATURAL — organico, wellness (recomendado Track B saude/sustentavel)
    primary   #16A34A  (leaf)
    secondary #FEF3C7  (cream)
    accent    #DC2626  (red)
    n_dark    #14532D
    n_light   #FAFAF9
```

Operador escolhe (a-e). Confirmar.

### 2B. Modo CUSTOM

Perguntar cada hex code com validacao regex `^#[0-9a-fA-F]{6}$`:

> "1. Primaria (cor de marca principal)?
> 2. Secundaria (cor de apoio)?
> 3. Accent (CTAs, destaques)?
> 4. Neutro escuro (texto)?
> 5. Neutro claro (background)?"

Se invalido: "Hex `<valor>` invalido. Use formato `#RRGGBB` (6 chars hexa)."

### 2C. Modo IMPORT URL

Solicitar URL:

> "Me passe a URL do site/portfolio/IG do qual extrair as cores dominantes:"

Validar URL (regex basico). Invocar:

```bash
python ${CLAUDE_PLUGIN_ROOT}/scripts/extract-palette-from-url.py "<url>"
```

Script retorna JSON com 5 cores ordenadas por frequencia. Apresentar:

> "Extrai estas cores dominantes do site: [preview]. Aceita assim ou quer ajustar manualmente?"

**NOTA:** script `extract-palette-from-url.py` sera criado em S2 (depende de Pillow + requests). Por enquanto, se nao existir, fallback para modo CUSTOM com sugestao "Visite o site, identifique as 5 cores principais e informe manualmente".

### 3. Mostrar preview

```
PALETA CONFIRMADA:

  primary    [#F4E5C5]
  secondary  [#2C2C2C]
  accent     [#B8860B]
  n_dark     [#1A1A1A]
  n_light    [#FAF7EE]

Origem: preset-bege-champanhe
```

Perguntar nomes amigaveis (opcional) para cada cor (ex: "Bege Champanhe", "Charcoal", "Gold").

### 4. Validar contraste

Calcular contraste WCAG entre `primary` x `n_dark` e `accent` x `n_light`. Se < 4.5 (AA), alertar:

> "ATENCAO: contraste entre primary e n_dark e 3.2 (abaixo do AA 4.5). Pode dificultar leitura. Confirma mesmo assim ou quer ajustar?"

### 5. Persistir

Atualizar `<cwd>/marketing/cowork-state.json` campo `identity.palette`:

```json
"identity": {
  "palette": {
    "primary": "#F4E5C5",
    "primary_name": "Bege Champanhe",
    "secondary": "#2C2C2C",
    "secondary_name": "Charcoal",
    "accent": "#B8860B",
    "accent_name": "Gold",
    "neutral_dark": "#1A1A1A",
    "neutral_light": "#FAF7EE",
    "source": "preset-bege-champanhe",
    "version": 2,
    "last_update": "2026-05-17T13:45:00Z"
  }
}
```

Atualizar `<cwd>/marketing/MEMORY.md` secao `## Identidade Visual` (subsecao "Paleta"). Incrementar `version`. Atualizar `last_update`.

### 6. Confirmar e proximos passos

```
OK Paleta atualizada (v2).

PROXIMOS PASSOS RECOMENDADOS:
- `/marketing-master` -> "gerar tokens.css" para CSS variables consumiveis por LP
- `/marketing-master` -> "atualizar BRAND-GUIDELINES" para regenerar guideline consolidado
- Toda producao visual (PNG, PPTX, LP) ja consome a nova paleta automaticamente
- `/status-marketing` para revisar estado completo do workspace
```

## OUTPUT ESPERADO

- `<cwd>/marketing/cowork-state.json` atualizado em `identity.palette`
- `<cwd>/marketing/MEMORY.md` secao `## Identidade Visual` -> subsecao Paleta atualizada
- Mensagem de confirmacao + proximos passos

## VEDACOES ESPECIFICAS

- **NUNCA** sobrescrever paleta sem confirmacao explicita do operador
- **NUNCA** sugerir cores que violem acessibilidade WCAG sem alertar
- **NUNCA** importar cores de URL sem mostrar preview e pedir confirmacao
- **NUNCA** persistir sem incrementar `version` (rastreabilidade)

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — define o que compoe identidade visual
- **2.3 Producao** — paleta vira input de TODA producao visual subsequente
