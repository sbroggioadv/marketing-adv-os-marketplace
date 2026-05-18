# CLAUDE.md — Workspace COWORK de {{MARCA_NOME}}

> Identidade e regras de trabalho deste workspace de marketing. Lido pelo Claude no inicio de cada sessao dentro desta pasta.

---

## Identidade do Workspace

- **Marca:** {{MARCA_NOME}}
- **Track:** {{TRACK}} ({{TRACK_DISPLAY}})
- **Plugin operacional:** `marketing-adv-os` v{{PLUGIN_VERSION}}
- **Persona:** `<COWORK>/marketing/persona.md` (injetada por hook SessionStart)
- **State:** `<COWORK>/marketing/cowork-state.json`
- **MEMORY:** `<COWORK>/marketing/MEMORY.md` (com secao **## Identidade Visual** consultada por TODA skill visual)

---

## Estrutura do Workspace

```
<COWORK>/marketing/
+-- cowork-state.json     (estado completo: track + paleta + voz + publico + oferta)
+-- persona.md            (identidade da marca renderizada)
+-- MEMORY.md             (memoria persistente com paleta + voz + producao)
+-- CLAUDE.md             (este arquivo)
+-- MARKETING/
    +-- Campanhas/        (campanhas estruturadas por slug)
    +-- Artes/            (PNG + PPTX por formato/plataforma)
    +-- Landing-Pages/    (LPs HTML/Next.js por slug)
    +-- Ebooks/           (MD + PDF)
    +-- Slides/           (apresentacoes comerciais PPTX)
    \-- Pesquisas/        (briefs de pesquisa, analise de mercado)
```

---

## Como Trabalhar Aqui

### Ao iniciar uma demanda de marketing

A skill `marketing-master` (orquestradora) e acionada automaticamente em **toda demanda de marketing**. Ela aplica o **protocolo de 6 etapas**:

1. **Identifica tipo** — copy / arte / LP / ebook / campanha / conteudo
2. **Aciona ESTADO-MAIOR** (Tier 1) — `marketing-brand-*`, `marketing-descoberta-de-publico`, `marketing-briefing-de-campanha`
3. **Aciona EXECUTORES** (Tier 2) — skill especifica do tipo
4. **Consulta MEMORY** — paleta + voz + publico + oferta (consulta automatica)
5. **Aplica DIRETORIA CRIATIVA** — R1 Brief -> R2 Copy -> R3 Compliance -> R4 Performance
6. **Entrega** — output no formato preferido ({{OUTPUT_FORMAT_PREFERIDO}}); arquivo gerado em pasta certa de `MARKETING/`

### Modo planejamento

Antes de executar tarefa nao-trivial, o Claude apresenta:
- **Briefing estruturado** — publico + dor + KPI + canal + formato
- **Plano de acao** — quais skills serao acionadas
- **Duvidas** — o que falta para fazer com qualidade

Aguarda confirmacao ou ajuste antes de comecar.

### Comandos disponiveis

- `/start-marketing` — re-rodar wizard (`--update` mantem respostas, `--reset` apaga state)
- `/marketing-master` — ativar cadeia completa
- `/copy-marketing [tipo]` — producao isolada de copy
- `/campanha-marketing [tema]` — campanha completa
- `/conteudo-marketing [formato]` — conteudo editorial
- `/revisao-marketing-final [path]` — Diretoria Criativa em peca pronta
- `/diretoria-criativa-marketing [path]` — auditoria isolada
- `/status-marketing` — diagnostico do workspace

---

## MEMORY SYSTEM

Esta pasta tem `MEMORY.md`. Funciona como memoria persistente da marca.

**No inicio de cada sessao:** O Claude le `MEMORY.md` antes de responder. Usa secoes:
- **## Identidade Visual** — paleta + tipografia + tokens (TODA skill visual consulta)
- **## Voz da Marca** — tom + expressoes + exemplos (TODA skill de copy consulta)
- **## Publico-alvo** — persona + dor + canais
- **## Oferta** — servico/produto + ticket + modalidade

**Escrita automatica em skills `marketing-brand-*`:** essas skills SIM atualizam o MEMORY automaticamente (definir paleta, voz, etc). Outras skills NAO escrevem sem voce pedir.

**Escrita user-triggered (outras skills):** "lembre disso", "anote", "salve no MEMORY".

---

## Privacidade & LGPD

- **Dados da marca:** ficam APENAS nesta pasta `<COWORK>/`. Nunca saem da maquina sem opt-in explicito.
- **Lista de email/leads:** **NUNCA** colar dados pessoais reais (CPF, email de cliente). Plugin recusa se detectar.
- **MCPs externos** (Meta Ads, Canva, Postiz, HubSpot, Klaviyo): so ativados via `/start-marketing` ou `/marketing-master` com warning explicito.
- **Track A (advogado):** restricoes extras — VE-15 (sigilo profissional) bloqueia inclusao de testemunho de cliente sem autorizacao escrita.

---

## Governance Track-Aware

Track ativo: **{{TRACK}}**

{{#TRACK_A}}
**Track A — OAB Provimento 205/2021 + Codigo de Etica:**
- Sem promessa de resultado (VE-04)
- Sem mercantilizacao da advocacia (VE-05)
- Sem captacao indevida (VE-06)
- Sem ofensa a colegas (VE-07)
- Sem quebra de sigilo (VE-15)
- Conteudo informativo, nao publicitario
{{/TRACK_A}}

{{#TRACK_B}}
**Track B — CONAR + LGPD:**
- Sem propaganda enganosa (VE-12)
- Sem comparativo desleal (VE-10)
- Declarar parceria paga (VE-13)
- LGPD em qualquer coleta (VE-08, VE-09)
{{/TRACK_B}}

**Universais (ambos os tracks):** VE-01 (sem promessa falsa), VE-02 (sem manipulacao ofensiva), VE-03 (sem mistura de escopos), VE-11 (sem apelo abusivo crianca/adolescente), VE-14 (declarar IA quando publico assume autoria humana).

---

## Atualizacao desta Configuracao

Esta pasta e **gerada e mantida pelo plugin `marketing-adv-os`**. Para reconfigurar:

```
/start-marketing --update
```

Versao do schema deste workspace: {{SCHEMA_VERSION}}
Ultima atualizacao: {{GENERATED_AT}}
