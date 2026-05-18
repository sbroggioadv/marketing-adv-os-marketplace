---
description: Inicia o onboarding interativo do plugin Marketing-Adv-OS no diretorio atual. Cria pasta `marketing/` com configuracao da marca (track A advogado / track B empresario + paleta de cores persistente + voz + publico-alvo + oferta).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [--update | --reset]
---

Voce foi acionado pelo comando `/start-marketing` do plugin Marketing-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** conduzir o operador pelo wizard de onboarding, coletar identidade, track (A/B), paleta de cores e configuracao de marca, e gerar a pasta `marketing/` no diretorio atual com todo o estado.

## PROTOCOLO DE EXECUCAO

### 1. Acionar a skill `marketing-onboarding`

**IMPORTANTE:** Use Skill(skill="marketing-onboarding") imediatamente. Ela contem o fluxo completo do wizard de 11 blocos (Bloco 0 Track Selector + Bloco 3 Paleta sao os mais criticos).

### 2. Parsear argumentos

- Sem argumento -> wizard completo (primeira instalacao)
- `--update` -> re-executar wizard mantendo respostas anteriores como defaults
- `--reset` -> apagar state existente apos confirmacao dupla e rodar wizard limpo

### 3. Se ja existe `<cwd>/marketing/cowork-state.json`

Antes de sobrescrever, perguntar ao operador:

> "Detectei configuracao de marketing existente em `<cwd>/marketing/`.
> Marca: `<marca_nome>`. Track: `<A|B>`. Paleta: `<hex_primary>`. Skills ativas: `<N>`.
>
> (a) continuar com a configuracao existente
> (b) atualizar (--update)
> (c) recriar do zero (--reset, PERDE memoria)"

### 4. Produtos esperados apos o wizard

Apos `python scripts/render.py <cwd>`, devem existir:

- `<cwd>/marketing/cowork-state.json` (state completo com `track`, `identity.palette`, `identity.typography`, `publico`, `oferta`, `voz`)
- `<cwd>/marketing/persona.md` (identidade da marca gerada — vive FORA do plugin)
- `<cwd>/marketing/MEMORY.md` (memoria com secao **## Identidade Visual** populada com paleta + tipografia + **## Voz da Marca** com expressoes)
- `<cwd>/marketing/CLAUDE.md` (instrucoes especificas do workspace marketing)
- `<cwd>/marketing/MARKETING/` (subpastas Campanhas, Artes, Landing-Pages, Ebooks, Slides, Pesquisas)
- `<cwd>/.claude/settings.local.json` (envs `MARKETING_PERSONA` + `MARKETING_COWORK_PATH`)

### 5. Encerramento

Mostrar resumo amigavel:

```
OK Plugin Marketing-Adv-OS configurado!

Marca: <nome>
Track: <A=Advogado/Escritorio | B=Empresario/Criador>
Cidade: <cidade>/<UF>
Paleta: <hex codes>
Tom: <perfil> (intensidade <X>/10)
Diretoria Criativa: <ATIVA/DESATIVADA>

PROXIMOS PASSOS:
1. Reinicie a sessao do Claude Code (hook SessionStart passara a injetar sua persona)
2. Use /marketing-master para ativar a cadeia completa de skills
3. Ou simplesmente faca uma pergunta com termos de marketing — o plugin desperta automaticamente
4. Rode /status-marketing a qualquer momento para diagnostico
5. /revisao-marketing-final roda Diretoria Criativa R1-R4 em qualquer peca
```

**Skill a acionar:** `marketing-onboarding`.
