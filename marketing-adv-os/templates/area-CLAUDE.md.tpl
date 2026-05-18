# CLAUDE.md — {{AREA_DISPLAY_NAME}}

> Subpasta de **{{AREA_DISPLAY_NAME}}** do workspace de marketing de {{MARCA_NOME}}. Contextualiza o Claude para producoes desta categoria.

---

## Proposito da Pasta

Gestao e producao de material de **{{AREA_DISPLAY_NAME}}**.

{{#CAMPANHAS}}
Esta pasta centraliza campanhas estruturadas: briefing, copy, artes, distribuicao, plano de mensuracao. Cada campanha em sua subpasta por slug (ex: `lancamento-curso-2026/`, `black-friday/`).
{{/CAMPANHAS}}

{{#ARTES}}
Esta pasta centraliza artes finalizadas (PNG, PPTX) por formato. Estrutura sugerida por subpasta:
- `instagram-feed/` (1080x1080)
- `instagram-story/` (1080x1920)
- `instagram-reels-capa/` (1080x1920)
- `facebook-post/` (1200x630)
- `linkedin-post/` (1200x627)
{{/ARTES}}

{{#LANDING_PAGES}}
Esta pasta centraliza landing pages produzidas. Cada LP em sua subpasta por slug com `index.html` + `assets/` + (se aplicavel) `tokens.css`.
{{/LANDING_PAGES}}

{{#EBOOKS}}
Esta pasta centraliza ebooks. Cada ebook em sua subpasta por slug com `manuscript.md` + `cover.png` + `<slug>.pdf` gerado.
{{/EBOOKS}}

{{#SLIDES}}
Esta pasta centraliza apresentacoes comerciais (proposta, pitch, webinar) em PPTX.
{{/SLIDES}}

{{#PESQUISAS}}
Esta pasta centraliza pesquisas de mercado, briefs de descoberta de publico, analise de concorrencia, julgados verificados (Track A).
{{/PESQUISAS}}

---

## Skills Sugeridas para Esta Pasta

> A skill `marketing-master` e acionada SEMPRE. As listadas abaixo sao complementares conforme tipo de producao.

{{#SKILLS_SUGERIDAS_LIST}}
- `{{.}}`
{{/SKILLS_SUGERIDAS_LIST}}

{{^SKILLS_SUGERIDAS_LIST}}
*(`marketing-master` orquestra automaticamente conforme a demanda.)*
{{/SKILLS_SUGERIDAS_LIST}}

---

## Instrucoes Especificas

- Toda producao consulta `<COWORK>/marketing/MEMORY.md` (paleta, voz, publico, oferta)
- Paleta primaria: `{{PALETTE_PRIMARY}}` · Voz: `{{TOM_VOZ_PERFIL}}`
- Output preferido: `{{OUTPUT_FORMAT_PREFERIDO}}`
- **Diretoria Criativa R1-R4** aplicada automaticamente antes de declarar peca aprovada
- **Track {{TRACK}}** ativo — Vedacoes Editoriais condicionadas (OAB ou CONAR conforme track)
- Sempre **mostrar cadeia de raciocinio** e **plano de acao** antes de executar
- **Nunca inventar dado** (estatistica, julgado, depoimento) — usar so verificado

---

## MEMORY SYSTEM Local

Esta pasta pode ter seu proprio `MEMORY.md` (opcional). Memoria especifica desta categoria de producao (ex: campanhas que deram certo, formatos de arte que viraram padrao).

**Memoria e user-triggered:** so escreve quando voce pedir explicitamente.

---

**Pasta gerada por:** Plugin `marketing-adv-os` v{{PLUGIN_VERSION}}
**Configuravel em:** `/start-marketing --update` ou edicao manual
**Ultima atualizacao:** {{GENERATED_AT}}
