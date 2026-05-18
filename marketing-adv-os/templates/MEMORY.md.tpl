# MEMORY.md — {{MARCA_NOME}}

> Memoria persistente da marca. Lida automaticamente no inicio de cada sessao do Claude Code. Algumas secoes (Identidade Visual, Voz da Marca) sao atualizadas por skills `marketing-brand-*`; outras sao user-triggered.

---

## Como Funciona

**Leitura automatica:** O Claude le este arquivo no inicio de cada sessao. Secoes especiais sao consultadas por TODA skill que produz peca visual ou textual.

**Escrita automatica em skills marketing-brand-*:**
- `marketing-brand-palette` atualiza **## Identidade Visual** (paleta hex)
- `marketing-brand-voice` atualiza **## Voz da Marca** (tom + expressoes)
- `marketing-tipografia` atualiza **## Identidade Visual** (fontes)
- `marketing-tokens-css` gera arquivos em `<COWORK>/marketing/design-tokens/` (nao escreve aqui)

**Escrita user-triggered (outras skills):** Claude NAO escreve sem voce pedir. Comandos para escrita explicita:
- "lembre disso"
- "anote esta informacao"
- "salve para proximas sessoes"
- "registre na memoria"
- "memorize"

**Persistencia:** Itens permanecem ate voce pedir para remover ou alterar.

**Conflitos:** Se voce pedir para lembrar algo que conflita com item existente, o Claude flagga em vez de sobrescrever silenciosamente.

---

## ## Identidade Visual

**(Atualizada por skills `marketing-brand-palette` e `marketing-tipografia`. TODA skill de arte/LP/PPTX consulta esta secao.)**

### Paleta
- **Primaria:**       `{{PALETTE_PRIMARY}}` — {{PALETTE_PRIMARY_NAME}}
- **Secundaria:**     `{{PALETTE_SECONDARY}}` — {{PALETTE_SECONDARY_NAME}}
- **Accent (CTAs):**  `{{PALETTE_ACCENT}}` — {{PALETTE_ACCENT_NAME}}
- **Neutro escuro:**  `{{PALETTE_NEUTRAL_DARK}}` (texto, backgrounds escuros)
- **Neutro claro:**   `{{PALETTE_NEUTRAL_LIGHT}}` (backgrounds, separadores)

**Origem:** {{PALETTE_SOURCE}}
**Versao:** {{PALETTE_VERSION}}
**Ultima atualizacao:** {{PALETTE_LAST_UPDATE}}

### Tipografia
- **Primaria:**   {{TYPO_PRIMARY}} (titulos, hero, hierarquia alta)
- **Secundaria:** {{TYPO_SECONDARY}} (corpo de texto, UI)

### Tokens
Arquivos gerados em `<COWORK>/marketing/design-tokens/`:
- `tokens.css` — CSS custom properties consumiveis por LP/site
- `tokens.json` — JSON estruturado consumivel por scripts Python/JS

---

## ## Voz da Marca

**(Atualizada por skill `marketing-brand-voice`. TODA skill de copy consulta esta secao.)**

### Perfil
- **Tom:** {{TOM_VOZ_PERFIL}}
- **Intensidade combativa:** {{TOM_VOZ_INTENSIDADE}}/10

### Expressoes assinatura
{{#EXPRESSOES_ASSINATURA_LIST}}
- "{{.}}"
{{/EXPRESSOES_ASSINATURA_LIST}}

### Termos a EVITAR (anti-voz)
{{#TERMOS_A_EVITAR_LIST}}
- "{{.}}"
{{/TERMOS_A_EVITAR_LIST}}

### Exemplos validados
{{#EXEMPLOS_VOZ_LIST}}
- {{.}}
{{/EXEMPLOS_VOZ_LIST}}

---

## ## Publico-alvo

**Persona:** {{PUBLICO_PERSONA}}
**Dor principal:** {{PUBLICO_DOR}}
**Canais ativos:**
{{#PUBLICO_CANAIS_LIST}}
- {{.}}
{{/PUBLICO_CANAIS_LIST}}

**Objecoes comuns:**
- _A definir conforme producao de campanhas — atualizar quando descobrir._

---

## ## Oferta

**Servico/Produto principal:** {{OFERTA_PRINCIPAL}}
**Faixa de ticket:** {{OFERTA_TICKET}} ({{OFERTA_TICKET_RANGE}})
**Modalidade:** {{OFERTA_MODALIDADE}}

---

## ## Producao

### Campanhas
_(Vazio. Skills `marketing-master` e `/campanha-marketing` adicionam aqui.)_

### Pecas publicadas
_(Vazio. Skill `marketing-diretoria-criativa-marketing` registra quando peca passa R1-R4.)_

### KPIs acompanhados
_(Vazio. Definir conforme campanha for ao ar.)_

---

## ## Itens Memorizados (User-Triggered)

_(Vazio. Adicione itens pedindo "lembre disso" ao Claude durante uma sessao.)_

---

**Workspace:** `{{COWORK_PATH}}`
**Marca:** {{MARCA_NOME}}
**Track:** {{TRACK}}
**Plugin:** `marketing-adv-os` v{{PLUGIN_VERSION}}
**Inicializado em:** {{GENERATED_AT}}
