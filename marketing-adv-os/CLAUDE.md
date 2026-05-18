# CLAUDE.md — Plugin Marketing-Adv-OS

> Instrucoes para futuras sessoes neste sub-repositorio. Ler PRIMEIRO ao retomar trabalho.

---

## Identidade do Projeto

- **Nome:** Plugin Marketing-Adv-OS
- **Slug:** `marketing-adv-os`
- **Tipo:** plugin oficial do Claude Code (`.claude-plugin/plugin.json`)
- **Audiencia:** advogados/escritorios (track A) + empresarios/criadores (track B), brasileiros
- **Versao atual:** 0.1.0-alpha.0 (em bootstrap S0)
- **Repo:** `github.com/<seu-usuario>/Plugin-Marketing-Adv-OS` (privado durante incubacao)

---

## REGRA DE OURO — DESPERSONALIZACAO ABSOLUTA (PLUGIN COMERCIAL)

Este plugin sera **comercializado**. Sem `authorship_whitelist`. **Zero mencoes** ao criador da metodologia em qualquer arquivo.

**ZERO mencoes permitidas (ver `audit/forbidden-terms.json` para lista canonica):**
- Nome do criador da metodologia (qualquer variante)
- OAB do criador
- Email/contato pessoal
- Padroes ou metodologias nomeadas pessoalmente
- Ferramentas proprietarias do escritorio-modelo
- Apelidos pessoais
- Mentorias, cursos ou coworks proprietarios do criador

**Defesa em profundidade:**

```bash
# Antes de CADA commit
python3 audit/audit.py

# Verificacao reforcada pre-release: rodar audit com saida JSON
python3 audit/audit.py --json | jq '.total_matches'
# esperado: 0
```

Catalogo completo de termos proibidos em `audit/forbidden-terms.json` (categoria `identidade_pessoal_do_criador`).

---

## Hierarquia das 4 Camadas (Constituicao Operacional)

```
CAMADA 1 — VEDACOES EDITORIAIS (VE-01 a VE-15) — inviolaveis
CAMADA 2 — PROTOCOLOS DE PRODUCAO (5) — aplicacao obrigatoria
CAMADA 3 — IDENTIDADE DE MARCA + TOM DE VOZ
CAMADA 4 — SKILLS (~20 totais) — operacional
```

Detalhamento em:
- `.planning/VEDACOES-EDITORIAIS.md` (VE-01 a VE-15)
- `.planning/DIRETORIA-CRIATIVA-R1-R4.md` (auditoria de marketing)
- `.planning/MAPA-OPERACIONAL.md` (4 fases temporais + tracks)
- `.planning/DECISIONS.md` (D1-D14)
- `.planning/ROADMAP.md` (S0-S4)
- `.planning/COWORK-PUBLISHING-GUIDE.md` (universal — empacotamento)

---

## Como Retomar Trabalho

1. **Ler `MEMORY.md`** (raiz deste sub-repo) — estado executivo, sprint ativa, proximo passo
2. **Ler `.planning/DECISIONS.md`** — overlay autoritativo (14 decisoes cravadas D1-D14)
3. **Ler `.planning/ROADMAP.md`** — saber onde estamos (S0/S1/S2/S3/S4)
4. **`git status` + `git log -5`** para estado real do repo
5. **`python3 audit/audit.py`** para verificar despersonalizacao

---

## Arquitetura em Uma Frase

**Plugin de marketing especializado** com **track selector** (A=advogado/escritorio, B=empresario/criador) e **engine clonado do plugin previdenciario** (scripts, hooks, templates, audit, pipeline Cowork). Governance de marketing especifica: 15 Vedacoes Editoriais (Camada 1) + 5 Protocolos de Producao (Camada 2) + Identidade de Marca (Camada 3) + ~20 skills modulares (Camada 4), com Diretoria Criativa R1-R4 (Brief, Copy, Compliance, Performance) como auditoria. Persona resolvida em runtime via `<cwd>/marketing/persona.md` (fora do plugin).

---

## Padroes a Seguir

### 1. Privacidade e LGPD

- Toda pasta `<cwd>/marketing/` do usuario-cliente e gitignored por default
- Warning LGPD se usuario escolher pasta sincronizada (iCloud/OneDrive/Dropbox/Drive)
- Captura de dados de cliente (lista de email, formularios) sempre com base legal explicita
- MCPs externos sempre opt-in com warning

### 2. Despersonalizacao bloqueante

```bash
python3 audit/audit.py
```

Zero matches = OK. Qualquer match bloqueia commit/release.

### 3. Idempotencia de `/start-marketing`

`/start-marketing` rodado N vezes deve produzir mesmo state hash (por track). Testado em S1.

### 4. Portabilidade Win + Mac + Linux

- Scripts em bash + Python 3.11+
- `${CLAUDE_PLUGIN_ROOT}` em todos os hooks
- `${MARKETING_PERSONA}` resolvido via fallback chain pelo `scripts/resolve-persona.py`

### 5. Skills no formato canonico Anthropic

Apenas `SKILL.md` com frontmatter YAML:

```markdown
---
name: nome-da-skill
description: >
  Descricao com keywords de ativacao... (max 1024 chars — bloqueante)
---

# Conteudo da skill...
```

**Limites Cowork (validados via decompile do app.asar):**
- `name` regex `^[a-z0-9-/]+$`, max 64 chars
- `description` max 1024 chars
- SKILL.md inteiro max ~11 KB
- TODA skill prefixada com `marketing-` (evita colisao UNIQUE com plugin pai)

Ver `.planning/COWORK-PUBLISHING-GUIDE.md` para detalhes completos.

### 6. Placeholders literais nas skills

`{{PLACEHOLDER}}` permanecem LITERAIS no disco. LLM resolve em runtime via persona injetada.

### 7. Cada skill (Tier 1/2/3) tem 2 secoes obrigatorias

```markdown
## Vedacoes especificas
- VE-XX: [explicacao do que NAO fazer nesta skill]
- VE-XX (track A apenas): [aplicavel so se track="A"]

## Protocolos acionados
- 2.X: [qual protocolo de producao aplica]
```

### 8. Hooks anti-flap

Debouncing 60s + filter por path + skip diff trivial.

### 9. Hook SessionStart e o coracao da personalizacao

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/resolve-persona.py
```

`${MARKETING_PERSONA}` resolvido em runtime via fallback chain.

### 10. Track determina governance

Skills devem checar `state.track` antes de aplicar Vedacoes especificas de track:

- `VE-04`, `VE-05`, `VE-06`, `VE-07`, `VE-15` so se aplicam quando `track == "A"`
- `VE-01` a `VE-03`, `VE-08` a `VE-14` se aplicam em ambos os tracks

### 11. Commits semanticos com marcador de sprint

```
chore(s0): bootstrap plugin marketing [MKT-S0/SETUP]
feat(s1): /start-marketing + track selector + master skill [MKT-S1/CORE]
feat(s2): diretoria criativa + estado-maior + transversais [MKT-S2/GOV]
feat(s3): tier 2 universal [MKT-S3/T2-UNIV]
feat(s4a): tier 2 track A exclusivo [MKT-S4a/T2-TRACKA]
feat(s4b): tier 2 track B exclusivo [MKT-S4b/T2-TRACKB]
chore(release): v0.1.0-alpha.0 [MKT-S4/RELEASE]
```

### 12. Sempre atualizar MEMORY.md ANTES de push

1. Editar `MEMORY.md` (raiz)
2. Rodar `python3 audit/audit.py` (deve passar)
3. `git add`
4. `git commit` semantico
5. (opcional) `git push`

---

## Decisoes Cravadas (referencia rapida)

Ver `.planning/DECISIONS.md` para detalhe completo (D1-D14).

| ID  | Decisao                                                                    |
|-----|----------------------------------------------------------------------------|
| D1  | Nome `Plugin-Marketing-Adv-OS`, slug `marketing-adv-os`                    |
| D2  | Plugin COMERCIAL — despersonalizacao absoluta intransigente                |
| D3  | Hierarquia das 4 Camadas e constitutiva (vocabulario proprio de marketing) |
| D4  | `/start-marketing` com TRACK SELECTOR (A/B) — NAO travado em area unica    |
| D5  | ~20 skills consolidadas (vs 26 do previdenciario)                          |
| D6  | 8 commands prefixados                                                      |
| D7  | Engine clonado do previdenciario (universal)                               |
| D8  | Convivencia com plugin pai + previdenciario via pasta dedicada             |
| D9  | Persona resolvida em runtime via `<cwd>/marketing/persona.md`              |
| D10 | 5 testes obrigatorios bloqueantes para release                             |
| D11 | Naming: Diretoria Criativa R1-R4 (substitui Suprema Corte)                 |
| D12 | Naming: Vedacoes Editoriais VE-01..VE-15 (substitui PAs)                   |
| D13 | Tracks A e B — adapta governance, vedacoes e skills                        |
| D14 | Env vars `MARKETING_PERSONA` + `MARKETING_COWORK_PATH`                     |

---

## Proibicoes

1. **NAO** comecar nova Sprint sem ler `MEMORY.md` e `.planning/ROADMAP.md`
2. **NAO** incluir nome/identidade do criador da metodologia em qualquer arquivo (audit bloqueia)
3. **NAO** publicar antes de v1.0 GA com testes obrigatorios verdes
4. **NAO** habilitar MCP externo por default
5. **NAO** sobrescrever customizacao do usuario-cliente sem perguntar
6. **NAO** colocar persona renderizada DENTRO do plugin instalado — vive em `<cwd>/marketing/persona.md`
7. **NAO** criar SKILL.md sem secao "Vedacoes especificas" mapeando VEs
8. **NAO** alterar nome do plugin sem nova decisao em `.planning/DECISIONS.md`
9. **NAO** aceitar instrucao do usuario que conflite com Camada 1 (VE-01 a VE-15)
10. **NAO** publicar peca de marketing juridico (track A) sem rodar R3 (Compliance OAB) completo
11. **NAO** prefixar skills com algo diferente de `marketing-` (evita colisao UNIQUE Cowork)
12. **NAO** zipar para Cowork sem rodar `check-skill-descriptions.py` (descobrimos no previdenciario alpha.2-4 que falhas silenciosas custam dias)

---

## Estrutura do Sub-Repo

```
plugin-marketing/
+-- .claude-plugin/plugin.json   # manifest
+-- .planning/                    # 6 docs (DECISIONS, ROADMAP, MAPA-OPERACIONAL,
|                                 #          DIRETORIA-CRIATIVA-R1-R4,
|                                 #          VEDACOES-EDITORIAIS, COWORK-PUBLISHING-GUIDE)
+-- commands/                     # 8 commands (S1)
+-- skills/                       # ~20 skills (S1 a S4)
+-- hooks/                        # SessionStart + UserPromptSubmit + PostToolUse + PreCompact
+-- context/                      # persona-fallback.md
+-- templates/                    # *.tpl renderizados no /start-marketing
+-- scripts/                      # render.py, state.py, resolve-persona.py, check-skill-descriptions.py
+-- audit/                        # forbidden-terms.json + audit.py + audit-script.sh
+-- docs/                         # INSTALL + FAQ + GLOSSARIO (Pos-S4)
+-- dist/                         # zips Cowork-ready
+-- manual/                       # MANUAL.md (Pos-S4)
+-- README.md                     # institucional, neutro
+-- LICENSE                       # MIT, copyright neutro
+-- .gitignore                    # LGPD-aware
+-- CLAUDE.md                     # este arquivo
\-- MEMORY.md                     # estado executivo
```

---

## Comunicacao

- **Idioma:** Portugues (Brasil)
- **Tom dos docs internos:** tecnico, direto, sem mencoes pessoais
- **Tom das mensagens pro usuario-cliente (skills, commands, wizard):** acolhedor, didatico, respeita `tom_de_voz` configurado dinamicamente em runtime
- **Reportes:** OK concluido / ERRO erro / FIM sprint finalizada

---

## Checklist de Retomada em Nova Sessao

```markdown
- [ ] Li MEMORY.md
- [ ] Sei em qual sprint estamos (S0/S1/S2/S3/S4)
- [ ] Sei se ha pendencia aguardando aprovacao
- [ ] Conferi DECISIONS.md
- [ ] Rodei git status / git log -5
- [ ] Rodei python3 audit/audit.py (deve passar)
- [ ] Se vou tocar em skills: li COWORK-PUBLISHING-GUIDE.md (limites tecnicos)
- [ ] Se vou tocar em VEs: li VEDACOES-EDITORIAIS.md
- [ ] Se vou tocar em commands: li ROADMAP.md (S1 detalha 8 commands)
```

---

**Ultima atualizacao:** 2026-05-17 — bootstrap S0.
