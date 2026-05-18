---
description: Ativa a cadeia completa de skills de marketing. Carrega Hierarquia das 4 Camadas, 15 Vedacoes Editoriais, 5 Protocolos de Producao e Diretoria Criativa R1-R4. Use para qualquer demanda de marketing (campanha, copy, conteudo, arte, landing page, ebook, slides).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
argument-hint: [demanda opcional]
---

Voce foi acionado pelo comando `/marketing-master` do plugin Marketing-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a skill orquestradora `marketing-master` (Tier 0) e operar a cadeia completa de skills do plugin para atender a demanda do operador.

## PROTOCOLO DE EXECUCAO

### 1. Acionar a skill `marketing-master`

Use Skill(skill="marketing-master") imediatamente. Ela carrega:
- Identidade do operador (persona resolvida em runtime)
- Hierarquia das 4 Camadas
- 15 Vedacoes Editoriais (track-aware)
- 5 Protocolos de Producao
- Pipeline de orquestracao Tier 0 -> 1 -> 2 -> 3
- Sistema R1-R4 da Diretoria Criativa

### 2. Confirmar contexto

Mostrar saudacao curta com identidade carregada:

> "Plugin Marketing ativado. Marca: `<marca>`. Track: `<A|B>`. Paleta primaria: `<hex>`. Voz: `<perfil>`.
> Estou em `<cwd>`. Posso ajudar com copy, campanha, conteudo, artes, landing page, ebook, slides, posicionamento ou qualquer demanda de marketing.
> Qual a demanda?"

### 3. Se ha argumento

Tratar `$ARGUMENTS` como a demanda inicial. Aplicar pipeline:
1. Identificar tipo (copy / arte / LP / ebook / etc)
2. Acionar Tier 1 (estado-maior) se demanda for estrategica
3. Acionar Tier 2 (executor) especifico
4. Acionar transversais (estilo + visual)
5. Acionar Diretoria Criativa R1-R4

### 4. Estado sem configuracao

Se `<cwd>/marketing/cowork-state.json` NAO existe, sugerir `/start-marketing` primeiro. Permitir prosseguir em modo fallback se operador insistir, com aviso de qualidade reduzida.

**Skill a acionar:** `marketing-master`.
