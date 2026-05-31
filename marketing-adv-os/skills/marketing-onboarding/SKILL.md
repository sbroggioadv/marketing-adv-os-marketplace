---
name: marketing-onboarding
description: >
  MARKETING ONBOARDING — Wizard interativo do plugin Marketing-Adv-OS. Configura o workspace COWORK do operador via fluxo estruturado em 10 blocos: track selector (Advogado vs Empresario), diretorio LGPD-aware, identidade da marca, PALETA DE CORES (3 modos: 5 presets, hex custom, extrair de URL via Pillow), publico-alvo + dor, oferta atual, tom de voz, tipografia, Diretoria Criativa R1-R4, ferramentas declaradas. Cria pasta `marketing/` com persona.md, MEMORY.md (com secao Identidade Visual persistente), CLAUDE.md e settings.local.json. Use quando operador disser: configurar marketing, instalar marketing, primeira vez, /start-marketing, /onboarding-marketing, configurar plugin marketing, comecar marketing.
---

> **🖱️ Escolhas = botoes:** em campos de **lista fechada** (AREA_FOCO, tom, modo, atualizar/recriar, sim/nao) use a ferramenta **AskUserQuestion** para mostrar **botoes clicaveis** (max. 4 por pergunta; se houver mais, divida em 2). **Texto livre** (nome, OAB, cidade, e-mail) segue como pergunta digitada normal.

# MARKETING ONBOARDING

> Wizard de configuracao inicial com TRACK SELECTOR (Advogado/Empresario). Linguagem acolhedora, didatica.

## REGRAS

1. Portugues (Brasil), tom acolhedor e direto
2. Uma pergunta por vez para campos criticos; agrupar relacionados em multi-select
3. Defaults inteligentes — operador pode aceitar com Enter ou "ok"
4. Validar em tempo real (URL valida, hex code valido, email valido)
5. Confirmar antes de commitar (resumo + "confirma? s/n")
6. Idempotencia — se ja tem state, perguntar atualizar vs recriar
7. Privacidade — NUNCA pedir CPF, dados pessoais de cliente, lista de email real
8. Plugin tem 2 tracks — perguntar PRIMEIRO no Bloco 0

## FLUXO

### Bloco 0 — TRACK SELECTOR (NOVO — distinguir de plugins juridicos)

> "Ola! Sou o assistente do **Plugin Marketing-Adv-OS**. Vou te guiar por ~7 minutos.
>
> Primeiro: qual e seu perfil?
>
> (A) **Advogado/Escritorio** — ativa governance OAB Provimento 205/2021 + skills de marketing juridico
> (B) **Empresario/Criador** — ativa governance CONAR + LGPD + skills de marketing comercial
>
> Track determina quais Vedacoes Editoriais carregam, quais skills ficam disponiveis e qual checklist roda em Compliance (R3 da Diretoria Criativa)."

Persistir: `python scripts/state.py set <cwd> track "<A|B>"`.

### Bloco 1 — Diretorio (cwd)

Detectar cwd. Mostrar:
> "Vou criar `marketing/` aqui em `<cwd>`.
>
> ATENCAO LGPD: pasta sincronizada (iCloud, OneDrive, Dropbox, Drive) pode subir dados a nuvem. Recomendo caminho local. Confirma?"

Se nao, perguntar path alternativo. Validar (alertar se sincronizado; permitir prosseguir com confirmacao explicita).

### Bloco 2 — Identidade da marca (track-aware)

**Comum (A e B):**
> "1. Nome da marca / empresa?
> 2. Cidade + UF?
> 3. Site (opcional)?
> 4. Instagram (opcional)?
> 5. LinkedIn (opcional)?"

**Track A adiciona:**
> "6. Nome do escritorio?
> 7. OAB (numero) — opcional, NAO vai aparecer em pecas comerciais
> 8. UF da OAB?"

**Track B adiciona:**
> "6. Nicho / segmento (ex: educacao, saude, e-commerce, B2B SaaS)?
> 7. CNPJ (opcional)?"

Validar email/URL se preenchidos. Persistir em `identity.<campo>`.

### Bloco 3 — PALETA DE CORES (★ pedido do operador)

> "Vamos definir a paleta. Escolha um modo:
>
> (1) **Paleta sugerida** — escolha entre 5 presets:
>     a) Bege Champanhe + Charcoal (institucional/elegante)
>     b) Lime Kinetic + Black Obsidian (ousado/manifesto)
>     c) Azul Marinho + Branco Quente (corporativo)
>     d) Roxo Tech + Rose Coral (moderno/criativo)
>     e) Verde Folha + Creme Natural (organico/wellness)
>
> (2) **Customizada** — informe 5 hex codes:
>     - Primaria (cor principal de marca)
>     - Secundaria (cor de apoio)
>     - Accent (CTAs, destaques)
>     - Neutro escuro (texto, backgrounds escuros)
>     - Neutro claro (backgrounds, separadores)
>
> (3) **Importar de URL** — me passe a URL do seu site/portfolio/IG; vou extrair as cores dominantes (Pillow + analise de pixels)."

**Modo 1:** ler `state-schema.json` campo `palettes` para mapeamento hex.
**Modo 2:** validar regex `^#[0-9a-fA-F]{6}$` em cada hex. Rejeitar e perguntar de novo se invalido.
**Modo 3:** invocar `python scripts/extract-palette-from-url.py <url>` (a criar em S2). Mostrar paleta extraida e confirmar.

Persistir em `identity.palette.{primary, secondary, accent, neutral_dark, neutral_light}`.

> "Confirmado. Paleta sera persistida em `marketing/MEMORY.md` na secao **## Identidade Visual** — TODA skill de arte, landing page e PPTX consulta essa secao automaticamente. Se voce trocar a paleta depois (`/marketing-master` → "trocar paleta"), tudo se ajusta."

### Bloco 4 — Publico-alvo + Dor

> "Descreva em 1-2 frases:
> 1. Quem e seu publico ideal? (persona ou segmento — evite 'todo mundo')
> 2. Qual a DOR principal que sua oferta resolve?
> 3. Onde esse publico esta? (multi-select: Instagram, LinkedIn, Facebook, TikTok, YouTube, email, busca Google, presencial)"

### Bloco 5 — Oferta atual

> "1. Servico/produto principal?
> 2. Faixa de ticket (orientativo — Baixo <R$500 / Medio R$500-5k / Alto R$5k-30k / Premium >R$30k)?
> 3. Modalidade (presencial / online / hibrido)?"

### Bloco 6 — Tom de voz

**Track A (default acolhedor-tecnico):**
> "Perfil de voz:
> 1. **institucional-tecnico** *(default)* — autoridade serena, sem captacao
> 2. **didatico** — explicativo, traduz tese juridica
> 3. **autoral** — opinativo dentro dos limites OAB"

**Track B (default comercial-claro):**
> "Perfil de voz:
> 1. **comercial-claro** *(default)* — direto, focado em conversao
> 2. **storyteller** — narrativo, jornada do cliente
> 3. **expert-autoridade** — tecnico, prova social
> 4. **provocador** — confrontacao saudavel, contracorrente"

> "Intensidade combativa 1-10? (default 5 — equilibrado)"

### Bloco 7 — Tipografia (opcional)

> "Quer definir tipografia agora? (s/n — default n, pode rodar `/marketing-master` → 'definir tipografia' depois)
>
> Se s:
> - Fonte primaria? (sugestoes Track A: Playfair Display, EB Garamond. Track B: Inter, Space Grotesk, Manrope)
> - Fonte secundaria? (sugestoes ambos: Inter, system-ui)"

Salvar em `identity.typography.{primary, secondary}`.

### Bloco 8 — Diretoria Criativa R1-R4

> "O plugin tem **Diretoria Criativa** que audita TODA peca antes de publicar (R1=Brief, R2=Copy, R3=Compliance, R4=Performance). Adiciona ~30s por peca mas garante:
> - R3 Compliance: zero violacao de VE-04/VE-05 (track A: OAB) ou VE-12/VE-13 (track B: CONAR)
> - R4 Performance: peca sai com gancho mensuravel e CTA singular
>
> Manter ATIVA? (s/n — default s)"

### Bloco 9 — Ferramentas declaradas (opcional)

> "Voce usa alguma dessas? (multi-select, todos opcionais)
> - Editor de arte: Canva / Figma / Adobe / nenhum
> - Email marketing: Mailchimp / Resend / Klaviyo / Brevo / nenhum
> - Ads: Meta Ads Manager / Google Ads / TikTok Ads / nenhum
> - Analytics: Google Analytics / Mixpanel / Amplitude / nenhum
> - Publishing: Postiz / Buffer / Hootsuite / nenhum
>
> Plugin nao impoe ferramentas — apenas registra. Em S6 oferecera integracoes opt-in."

### Bloco 10 — Renderizacao

```bash
python scripts/render.py <cwd>
```

Gera:
- `<cwd>/marketing/cowork-state.json` (estado completo com track + paleta)
- `<cwd>/marketing/persona.md` (identidade gerada — vive FORA do plugin)
- `<cwd>/marketing/CLAUDE.md` (instrucoes do workspace marketing)
- `<cwd>/marketing/MEMORY.md` (memoria — com secao **## Identidade Visual** populada com paleta + tipografia)
- `<cwd>/marketing/MARKETING/` (subpastas: Campanhas, Artes, Landing-Pages, Ebooks, Slides, Pesquisas)
- `<cwd>/.claude/settings.local.json` (apontando `MARKETING_PERSONA` + `MARKETING_COWORK_PATH`)

### Bloco 11 — Encerramento

```
OK Plugin Marketing-Adv-OS configurado!

Marca: <nome>
Track: <A=Advogado/Escritorio | B=Empresario/Criador>
Cidade: <cidade>/<UF>
Publico: <descricao curta>
Paleta: <preview hex codes>
Tom: <perfil> (intensidade <X>/10)
Diretoria Criativa: <ATIVA/DESATIVADA>

PROXIMOS PASSOS:
1. Reinicie a sessao (hook SessionStart passara a injetar sua persona em TODAS as sessoes)
2. Use /marketing-master para ativar a cadeia completa de skills de marketing
3. Ou faca pergunta com termos de marketing — desperta sozinho via hook UserPromptSubmit
4. /status-marketing a qualquer momento para diagnostico
5. /revisao-marketing-final para rodar Diretoria Criativa R1-R4 em qualquer peca
```

## FLUXOS ALTERNATIVOS

### `--update`
Ler state existente -> mostrar resumo -> perguntar quais blocos (2-9) atualizar -> re-rodar selecionados -> re-renderizar. Bloco 0 (track) e Bloco 1 (cwd) NAO podem ser atualizados sem `--reset`.

### State ja existente (sem flag)
> "Detectei configuracao existente. Marca: <nome>. Track: <A|B>. Paleta: <hex>. Skills ativas: <N>.
> (a) Continuar (mantem tudo)
> (b) Atualizar (escolhe blocos)
> (c) Recriar (PERDE memoria — confirma duas vezes)"

## CHECKLIST FINAL

- [ ] `<cwd>/marketing/cowork-state.json` valida no state-schema.json
- [ ] `cowork-state.track` esta em ["A", "B"]
- [ ] `cowork-state.identity.palette` tem 5 hex codes validos
- [ ] `<cwd>/marketing/persona.md` com placeholders resolvidos
- [ ] `<cwd>/marketing/CLAUDE.md`
- [ ] `<cwd>/marketing/MEMORY.md` com **## Identidade Visual** populada
- [ ] `<cwd>/.claude/settings.local.json` com `MARKETING_PERSONA` e `MARKETING_COWORK_PATH`
- [ ] Estrutura `marketing/MARKETING/{Campanhas, Artes, Landing-Pages, Ebooks, Slides, Pesquisas}` criada

## VEDACOES ESPECIFICAS

- **VE-08 LGPD** — NUNCA coletar dados sensiveis de cliente real (CPF, email pessoal de terceiro, lista de leads)
- NUNCA sobrescrever state existente sem confirmacao dupla
- NUNCA enviar dados a servicos externos durante wizard (extracao de paleta de URL faz scraping LOCAL via Pillow, sem upload)
- NUNCA pular o Bloco 0 (Track Selector) — track determina toda a governance

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — wizard e essencialmente um briefing estruturado de marca
- **2.4 Compliance** — track determinado aqui ativa checklist OAB ou CONAR no R3 da Diretoria Criativa
