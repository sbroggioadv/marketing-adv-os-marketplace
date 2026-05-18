---
name: marketing-arte-pptx
description: >
  MARKETING ARTE PPTX — Gera arte estatica em PPTX (1 slide) com canvas dimensionado pra plataforma especifica (1080x1350 Instagram feed, 1080x1920 Stories/Reels capa, 1200x627 LinkedIn). Output e EDITAVEL no Canva, PowerPoint, Keynote ou LibreOffice — operador pode ajustar cor, fonte, posicao depois sem refazer do zero. Consome paleta + tipografia do MEMORY automaticamente. Use quando o operador disser gerar arte PPTX, criar PPT para edicao, exportar pra Canva, arte editavel, peca em PPTX, slide unico pra arte.
---

# MARKETING ARTE PPTX

> Skill Tier 2 (Executor — Arte). Gera arte PPTX editavel via `scripts/arte-engine.py`.

## OBJETIVO

Produzir 1 slide PPTX (single-slide presentation) com canvas exato da plataforma alvo, texto + paleta + tipografia ja aplicados — pronto pra import no Canva ou edicao em PowerPoint/Keynote/LibreOffice. Diferente de PNG (estatico), PPTX permite ajustes finais sem regenerar.

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Paleta + tipografia + tokens gerados (marketing-brand-palette + marketing-tipografia + marketing-tokens-css)
3. python-pptx instalado: `pip3 install python-pptx` (se faltar, gera SVG fallback que importa no Canva)

## FLUXO

### 1. Coletar dados (mesmo de marketing-arte-png)

> "Vou gerar PPTX (1 slide editavel). Confirme:
> - Plataforma + formato (igual marketing-arte-png)
> - Template de layout
> - Texto + subtexto
> - Output path: `<cwd>/marketing/MARKETING/Artes/<slug>/<arquivo>.pptx`"

### 2. Verificar deps

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py --check-deps
```

Se python-pptx faltando:
> "python-pptx nao instalado. Opcoes:
> (a) Instalar (`pip3 install python-pptx`) — recomendado
> (b) Gerar SVG fallback (Canva importa SVG diretamente)"

### 3. Executar render

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py \\
  --template instagram.feed_portrait \\
  --texto "Headline" --subtexto "Subhead" \\
  --tokens <cwd>/marketing/design-tokens/tokens.json \\
  --output <cwd>/marketing/MARKETING/Artes/<slug>/peca-01.pptx
```

Engine detecta `.pptx` no sufixo e usa python-pptx em vez de Pillow.

### 4. Output formato

```
OK PPTX gerado.

LOCALIZACAO: <cwd>/marketing/MARKETING/Artes/<slug>/peca-01.pptx
RESOLUCAO DO SLIDE: 1080x1350 (EMUs ajustadas)
EDITAVEL EM: Canva (import), PowerPoint, Keynote, LibreOffice

PROXIMOS PASSOS:
- Abrir: `open <path>`
- Importar no Canva: arrastar o arquivo PPTX para Canva > File > Import
- Ajustar cores/fontes diretamente — paleta + tipografia ja aplicadas
- Exportar como PNG final: Canva > Download > PNG-24, ou marketing-export-multi-formato
```

## QUANDO USAR PNG vs PPTX

| Cenario | Usar |
|---------|------|
| Arte pronta pra publicar imediatamente | PNG (marketing-arte-png) |
| Equipe externa (social media/designer) vai ajustar | PPTX (esta skill) |
| Importar no Canva pra editar | PPTX |
| Compatibilidade max (Photoshop, Affinity, etc) | PNG |
| Carrossel completo de 7-10 slides editaveis | marketing-carrossel-pptx (multi-slide) |

## OUTPUT

PPTX 1-slide com canvas correto + paleta + tipografia + texto aplicados + proximos passos.

## VEDACOES ESPECIFICAS

- **NUNCA usar canvas padrao 16:9 do PowerPoint** — perde resolucao mobile-first
- **Slide dimensions em EMU** (English Metric Units): 1 px = 9525 EMU em 96 dpi
- **NUNCA editar PPTX e re-exportar PNG sem revalidar AI-SAFE zone** — operador pode acidentalmente mover texto pra fora
- **sRGB obrigatorio** — Canva e PowerPoint mantem sRGB; nao usar PPTX gerado por Photoshop em CMYK

## PROTOCOLOS ACIONADOS

- **2.3 Producao** — paleta + tipografia auto-aplicadas
- **2.1 Briefing** — formato + template confirmados
