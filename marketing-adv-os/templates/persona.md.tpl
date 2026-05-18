# Persona — {{MARCA_NOME}}

> **Arquivo de identidade da marca.** Vive em `<COWORK>/marketing/persona.md`. Injetado em TODA sessao do Claude Code via hook SessionStart deste plugin. Edite quando quiser ajustar tom, paleta, oferta.

---

## Identidade da Marca

**{{MARCA_NOME}}**
**Track:** {{TRACK}} ({{TRACK_DISPLAY}})
{{#CIDADE}}{{CIDADE}}{{#UF}}/{{UF}}{{/UF}}{{/CIDADE}}

{{#FIRM_NAME}}**Escritorio:** {{FIRM_NAME}}{{/FIRM_NAME}}
{{#OAB_NUMERO}}**OAB (Track A):** OAB/{{OAB_UF}} {{OAB_NUMERO}} — NAO aparece em pecas comerciais, registrado para compliance{{/OAB_NUMERO}}
{{#NICHO}}**Nicho (Track B):** {{NICHO}}{{/NICHO}}

{{#SITE}}**Site:** {{SITE}}{{/SITE}}
{{#INSTAGRAM}}**Instagram:** {{INSTAGRAM}}{{/INSTAGRAM}}
{{#LINKEDIN}}**LinkedIn:** {{LINKEDIN}}{{/LINKEDIN}}

---

## Identidade Visual

**Paleta de Cores (5 hex codes):**
- Primaria:        `{{PALETTE_PRIMARY}}` — {{PALETTE_PRIMARY_NAME}}
- Secundaria:      `{{PALETTE_SECONDARY}}` — {{PALETTE_SECONDARY_NAME}}
- Accent:          `{{PALETTE_ACCENT}}` — {{PALETTE_ACCENT_NAME}}
- Neutro escuro:   `{{PALETTE_NEUTRAL_DARK}}`
- Neutro claro:    `{{PALETTE_NEUTRAL_LIGHT}}`

**Tipografia:**
- Primaria:    {{TYPO_PRIMARY}}
- Secundaria:  {{TYPO_SECONDARY}}

**Origem da paleta:** {{PALETTE_SOURCE}} (preset | custom | extracted-from-url)

---

## Voz da Marca

**Perfil de tom:** `{{TOM_VOZ_PERFIL}}`
**Intensidade combativa:** {{TOM_VOZ_INTENSIDADE}}/10

{{#EXPRESSOES_ASSINATURA}}
**Expressoes assinatura (use livremente):**
{{#EXPRESSOES_ASSINATURA_LIST}}
- "{{.}}"
{{/EXPRESSOES_ASSINATURA_LIST}}
{{/EXPRESSOES_ASSINATURA}}

{{#TERMOS_A_EVITAR}}
**Termos a EVITAR (anti-voz):**
{{#TERMOS_A_EVITAR_LIST}}
- "{{.}}"
{{/TERMOS_A_EVITAR_LIST}}
{{/TERMOS_A_EVITAR}}

---

## Publico-alvo

**Persona:** {{PUBLICO_PERSONA}}
**Dor principal:** {{PUBLICO_DOR}}
**Canais ativos:**
{{#PUBLICO_CANAIS_LIST}}
- {{.}}
{{/PUBLICO_CANAIS_LIST}}

---

## Oferta

**Servico/Produto principal:** {{OFERTA_PRINCIPAL}}
**Faixa de ticket:** {{OFERTA_TICKET}} ({{OFERTA_TICKET_RANGE}})
**Modalidade:** {{OFERTA_MODALIDADE}}

---

## Ferramentas Declaradas (opcionais)

> Plugin nao impoe ferramentas — apenas registra. Skills consultam para sugerir integracoes adequadas. Campos vazios = ferramenta nao utilizada.

{{#TOOLS_EDITOR}}- **Editor de arte:** {{TOOLS_EDITOR}}{{/TOOLS_EDITOR}}
{{#TOOLS_EMAIL_MKT}}- **Email marketing:** {{TOOLS_EMAIL_MKT}}{{/TOOLS_EMAIL_MKT}}
{{#TOOLS_ADS}}- **Plataforma de ads:** {{TOOLS_ADS}}{{/TOOLS_ADS}}
{{#TOOLS_ANALYTICS}}- **Analytics:** {{TOOLS_ANALYTICS}}{{/TOOLS_ANALYTICS}}
{{#TOOLS_PUBLISHING}}- **Publishing/scheduler:** {{TOOLS_PUBLISHING}}{{/TOOLS_PUBLISHING}}

---

## Conectores MCP Ativos

{{#CONNECTORS_AVAILABLE}}
{{#CONNECTORS_AVAILABLE_LIST}}
- `{{.}}`
{{/CONNECTORS_AVAILABLE_LIST}}
{{/CONNECTORS_AVAILABLE}}

{{^CONNECTORS_AVAILABLE}}
_Nenhum conector MCP declarado. Sugestoes de automacao serao omitidas ou sinalizadas como "requer conector X"._
{{/CONNECTORS_AVAILABLE}}

---

## Diretrizes Permanentes

- Responder sempre em **portugues (Brasil)**.
- Output preferido: **`{{OUTPUT_FORMAT_PREFERIDO}}`** quando aplicavel.
- **Diretoria Criativa (R1->R2->R3->R4) e {{DIRETORIA_CRIATIVA_STATUS}}** por default em pecas publicaveis (artes, copy, LP, ebook). Bypass via `--no-diretoria` ou `/diretoria off`.
- **Compliance ativo:** {{COMPLIANCE_ACTIVE}} (Track A: OAB Provimento 205/2021; Track B: CONAR + LGPD).
- **Skills invariantes (nao removiveis):** `marketing-master`, 4 skills R1-R4 da Diretoria Criativa, `marketing-diretoria-criativa-marketing`.
- **Skills opt-in ativas:** {{SKILLS_OPT_IN_COUNT}} configurada(s) no `/start-marketing`.

---

## O Que Esta Persona Faz Pelo Claude

Quando o Claude le este arquivo no inicio de cada sessao, ele:

1. Sabe **qual e a marca** ({{MARCA_NOME}}) e **qual o track** ({{TRACK}}).
2. Adapta **tom de voz** ao perfil `{{TOM_VOZ_PERFIL}}` em todas as pecas, copy, conteudo, artes.
3. Aplica **paleta + tipografia** automaticamente em toda producao visual (arte PNG, PPTX, LP, ebook, slides).
4. Sabe **quem e o publico-alvo** e ajusta tom + gatilhos psicologicos a essa persona.
5. Aplica **Diretoria Criativa R1-R4** automaticamente antes de declarar peca aprovada.
6. Carrega **Vedacoes Editoriais condicionadas ao track** (Track A: OAB; Track B: CONAR).
7. Resolve **placeholders** `{{...}}` nas skills do plugin usando os valores deste arquivo.

---

## Como Atualizar

Edite este arquivo manualmente — mudancas sao lidas na proxima sessao do Claude Code.

Ou rode no Claude Code:
- `/start-marketing --update` para refazer o wizard inteiro
- `/marketing-master` -> "atualizar paleta" / "trocar voz" para alterar campo especifico
- `/status-marketing` para diagnostico atual

---

**Versao deste arquivo:** gerado automaticamente em {{GENERATED_AT}}
**Plugin:** `marketing-adv-os` v{{PLUGIN_VERSION}}
**State source:** `{{COWORK_PATH}}/marketing/cowork-state.json`
