---
name: marketing-visual-identity
description: >
  MARKETING VISUAL IDENTITY — Gera mood board HTML standalone (preview visual da identidade) a partir da paleta + tipografia + voz registrados no MEMORY. Output `<cwd>/marketing/visual-identity/moodboard.html` com paleta visualizada em cards, exemplos de tipografia aplicada, examplos de uso de accent em CTAs, e bloco de voz com expressoes assinatura. Abrivel em qualquer browser. Use quando o operador disser gerar mood board, ver preview da identidade, visualizar paleta aplicada, mockup da marca, validar identidade visual.
---

# MARKETING VISUAL IDENTITY

> Skill Tier 1 (Estado-maior — Brand). Gera mood board HTML pra validar identidade visual.

## OBJETIVO

Produzir um mockup visual (HTML standalone, sem dependencias externas) que mostra a identidade da marca aplicada em diversas situacoes: paleta em cards, tipografia em hierarquia (H1-Body), CTAs com accent, bloco de voz com expressoes assinatura. Util pra:
- Validar paleta antes de produzir artes em escala
- Apresentar identidade a equipe externa
- Detectar problemas (contraste baixo, fontes nao carregadas, accent muito apagado)

## PRE-REQUISITOS

- Workspace marketing configurado
- Paleta definida (obrigatorio)
- Tipografia definida (recomendado — fallback system-ui se nao)
- Voz definida (opcional — bloco de voz nao aparece se vazia)

## FLUXO

### 1. Carregar dados do MEMORY

Ler `<cwd>/marketing/cowork-state.json`:
- `identity.palette` (5 hex codes + nomes)
- `identity.typography.primary` + `identity.typography.secondary`
- `identity.voice.signature_expressions` (lista)
- `marca_nome`

Se paleta vazia: bloquear com:
> "Mood board precisa de paleta definida. Rode `marketing-brand-palette` antes."

### 2. Gerar HTML standalone

Estrutura do `moodboard.html`:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mood Board — <MARCA></title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=<TYPO_PRIMARY>:wght@400;600;700&family=<TYPO_SECONDARY>:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --primary: <PALETTE_PRIMARY>;
  --secondary: <PALETTE_SECONDARY>;
  --accent: <PALETTE_ACCENT>;
  --n-dark: <PALETTE_NEUTRAL_DARK>;
  --n-light: <PALETTE_NEUTRAL_LIGHT>;
  --typo-primary: '<TYPO_PRIMARY>', serif;
  --typo-secondary: '<TYPO_SECONDARY>', sans-serif;
}
body { font-family: var(--typo-secondary); background: var(--n-light); color: var(--n-dark); margin: 0; padding: 40px 20px; }
.container { max-width: 1200px; margin: 0 auto; }
h1, h2, h3 { font-family: var(--typo-primary); margin: 0; }
.palette { display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; margin: 32px 0 64px; }
.swatch { aspect-ratio: 1; border-radius: 8px; display: flex; flex-direction: column; justify-content: flex-end; padding: 16px; }
.swatch .hex { font-family: monospace; font-size: 12px; }
.swatch .name { font-size: 11px; opacity: 0.8; margin-top: 4px; }
.btn { display: inline-block; padding: 14px 28px; border-radius: 6px; font-weight: 600; text-decoration: none; transition: transform 0.2s; cursor: pointer; }
.btn-primary { background: var(--accent); color: var(--n-dark); }
.btn-secondary { background: transparent; color: var(--n-dark); border: 2px solid var(--n-dark); }
.section { margin: 64px 0; padding: 32px; background: white; border-radius: 12px; }
.voice-block { background: var(--secondary); color: var(--n-light); padding: 32px; border-radius: 12px; margin-top: 32px; }
.voice-block .expression { font-family: var(--typo-primary); font-size: 24px; font-style: italic; margin: 12px 0; }
</style>
</head>
<body>
<div class="container">
  <h1 style="font-size: 56px;"><MARCA></h1>
  <p style="font-size: 18px; opacity: 0.7;">Mood Board · Identidade Visual · Versao <VERSION></p>

  <div class="section">
    <h2 style="font-size: 32px; margin-bottom: 24px;">Paleta</h2>
    <div class="palette">
      <div class="swatch" style="background: var(--primary); color: var(--n-dark);">
        <div class="hex"><PALETTE_PRIMARY></div>
        <div class="name"><PALETTE_PRIMARY_NAME> · Primaria</div>
      </div>
      <div class="swatch" style="background: var(--secondary); color: var(--n-light);">
        <div class="hex"><PALETTE_SECONDARY></div>
        <div class="name"><PALETTE_SECONDARY_NAME> · Secundaria</div>
      </div>
      <div class="swatch" style="background: var(--accent); color: var(--n-dark);">
        <div class="hex"><PALETTE_ACCENT></div>
        <div class="name"><PALETTE_ACCENT_NAME> · Accent</div>
      </div>
      <div class="swatch" style="background: var(--n-dark); color: var(--n-light);">
        <div class="hex"><PALETTE_NEUTRAL_DARK></div>
        <div class="name">Neutro Escuro</div>
      </div>
      <div class="swatch" style="background: var(--n-light); color: var(--n-dark); border: 1px solid #ddd;">
        <div class="hex"><PALETTE_NEUTRAL_LIGHT></div>
        <div class="name">Neutro Claro</div>
      </div>
    </div>
  </div>

  <div class="section">
    <h2 style="font-size: 32px;">Tipografia</h2>
    <h1 style="font-size: 64px; margin-top: 24px;">Heading 1 — <TYPO_PRIMARY></h1>
    <h2 style="font-size: 40px; margin-top: 16px;">Heading 2 — <TYPO_PRIMARY></h2>
    <h3 style="font-size: 28px; margin-top: 16px;">Heading 3 — <TYPO_PRIMARY></h3>
    <p style="font-size: 18px; margin-top: 24px; max-width: 600px;">Body text — <TYPO_SECONDARY>. Voce esta lendo o estilo padrao de paragrafo da sua marca, com lorem ipsum apenas pra preencher e voce ver como o tipo se comporta em linhas longas com line-height 1.6.</p>
    <p style="font-size: 14px; opacity: 0.6; margin-top: 16px;">Caption — pequeno, neutro, baixo destaque.</p>
  </div>

  <div class="section">
    <h2 style="font-size: 32px;">CTAs</h2>
    <div style="margin-top: 24px;">
      <a class="btn btn-primary" href="#">Acao Primaria</a>
      <a class="btn btn-secondary" href="#" style="margin-left: 12px;">Acao Secundaria</a>
    </div>
    <p style="font-size: 14px; opacity: 0.6; margin-top: 16px;">Accent SEMPRE usa --accent. Secundaria usa borda neutra escura.</p>
  </div>

  <!-- Bloco de voz só se houver expressões -->
  <VOICE_BLOCK>

  <p style="margin-top: 64px; font-size: 14px; opacity: 0.5;">Gerado pelo plugin marketing-adv-os · <DATE></p>
</div>
</body>
</html>
```

Substituir `<MARCA>`, `<PALETTE_*>`, `<TYPO_*>`, `<VERSION>`, `<DATE>` pelos valores do state. Se ha expressoes assinatura, renderizar `<VOICE_BLOCK>` com:

```html
<div class="voice-block">
  <h2 style="color: var(--accent); font-size: 32px;">Voz da Marca</h2>
  <div class="expression">"Expressao 1"</div>
  <div class="expression">"Expressao 2"</div>
  ...
</div>
```

Caso contrario, omitir o bloco.

### 3. Salvar

Criar `<cwd>/marketing/visual-identity/` se nao existe. Escrever `moodboard.html`. Se ja existe: backup em `moodboard.html.<timestamp>.bak`.

### 4. Mostrar URL local

```
OK Mood board gerado.

LOCALIZACAO: <cwd>/marketing/visual-identity/moodboard.html
ABRIR: file://<absolute-path>

(Ou rode `open` no Mac / `xdg-open` no Linux pra abrir no browser default.)

PROXIMOS PASSOS:
- Revisar visualmente paleta + tipografia + CTAs
- Se algum elemento ficar ruim (contraste, fonte nao carregou): ajustar via marketing-brand-palette ou marketing-tipografia
- Compartilhar HTML com equipe externa pra validacao
```

## OUTPUT ESPERADO

- `<cwd>/marketing/visual-identity/moodboard.html` gerado
- Backup se existia previamente
- Mensagem de confirmacao com path absoluto

## VEDACOES ESPECIFICAS

- NUNCA gerar mood board sem paleta definida
- NUNCA omitir disclaimer de "preview, nao e versao final"
- Fonte Google externa requer internet — declarar isso na mensagem final
- NUNCA inserir JS externo sem opt-in

## PROTOCOLOS ACIONADOS

- **2.3 Producao** — preview visual antes de producao em escala
