---
name: marketing-brand-voice
description: >
  MARKETING BRAND VOICE — Define ou atualiza a voz da marca (tom, intensidade, expressoes assinatura, termos a evitar, exemplos validados). Persiste em `<cwd>/marketing/MEMORY.md` secao **## Voz da Marca**, consultada por TODA skill de copy. Track-aware: Track A (advogado) sugere perfis institucional-tecnico/didatico/autoral; Track B (empresario) sugere comercial-claro/storyteller/expert-autoridade/provocador. Use quando o operador disser definir voz, ajustar tom, mudar estilo, voz da marca, tone of voice, expressoes da marca, palavras a evitar, /marketing-master trocar tom.
---

# MARKETING BRAND VOICE

> Skill Tier 1 (Estado-maior — Brand). Define a voz da marca e persiste no MEMORY.

## OBJETIVO

Construir ou atualizar o perfil de voz da marca (tom + intensidade + expressoes aceitas + termos a evitar + exemplos), salvando em `<cwd>/marketing/MEMORY.md` secao `## Voz da Marca` + atualizando `<cwd>/marketing/cowork-state.json` campo `identity.voice`.

## PRE-REQUISITOS

- Workspace marketing configurado. Se nao: sugerir `/start-marketing` antes.
- Track ja definido (Track A ou B) — determina sugestoes de perfil.

## FLUXO

### 1. Carregar track e mostrar perfis sugeridos

Ler `state.track`. Mostrar perfis adequados:

**Track A — Advogado/Escritorio:**
> "Perfil de voz Track A:
> (1) **institucional-tecnico** *(recomendado)* — autoridade serena, sem captacao. OAB-safe.
> (2) **didatico** — explicativo, traduz tese juridica.
> (3) **autoral** — opinativo dentro dos limites OAB (sem captacao indevida)."

**Track B — Empresario/Criador:**
> "Perfil de voz Track B:
> (1) **comercial-claro** *(recomendado)* — direto, focado em conversao.
> (2) **storyteller** — narrativo, jornada do cliente, antes-depois.
> (3) **expert-autoridade** — tecnico, prova social, dado duro.
> (4) **provocador** — confrontacao saudavel, contracorrente."

### 2. Perguntar intensidade

> "Intensidade de afirmacao (1-10)?
> - 1-3: cauteloso, ponderado, muito 'pode-ser' e 'eventualmente'
> - 4-6: equilibrado (default 5)
> - 7-9: assertivo, afirmativo, postura clara
> - 10: combativo total — nunca relativiza, afirma sempre"

### 3. Expressoes assinatura (opcional)

> "Voce tem expressoes que sao 'marca da casa'? (ex: 'Em ultima analise', 'O que importa e:', 'Sem rodeios:'). Liste ate 10 ou pule."

Validar: nao podem violar VEs ativas. Track A: expressao nao pode soar como captacao ("garanto que", "voce vai ganhar"). Track B: nao pode soar enganosa ("milagre", "garantido 100%").

### 4. Termos a EVITAR

> "Quais palavras/expressoes NAO devem aparecer na sua marca? (ex: girias, jargao tecnico que afasta, palavras com conotacao negativa). Liste ate 10 ou pule."

### 5. Exemplos validados (opcional)

> "Tem 3-5 frases/posts/headlines que voce considera 'a melhor versao da marca'? Cole-as. Servem de referencia para skills de copy."

Validar contra VEs. Se algum exemplo viola VE-01 (promessa falsa) ou outras: avisar antes de salvar.

### 6. Preview

```
VOZ DA MARCA CONFIRMADA:

Perfil:      institucional-tecnico
Intensidade: 7/10 (assertivo)

Expressoes assinatura:
- "Aqui, a questao e tecnica"
- "Em ultima analise"
- "Sem rodeios"

Termos a evitar:
- "garantido"
- "100% de resultado"
- "milagre"

Exemplos validados: 3 cadastrados
```

### 7. Persistir

Atualizar `<cwd>/marketing/cowork-state.json` campo `identity.voice`:

```json
"identity": {
  "voice": {
    "profile": "institucional-tecnico",
    "intensity": 7,
    "signature_expressions": ["Aqui, a questao e tecnica", ...],
    "avoid_terms": ["garantido", "100% de resultado", "milagre"],
    "validated_examples": ["...", "..."],
    "version": 2,
    "last_update": "2026-05-17T14:00:00Z"
  }
}
```

Atualizar `<cwd>/marketing/MEMORY.md` secao `## Voz da Marca` (substituir conteudo da secao). Incrementar `version`. Atualizar `last_update`.

### 8. Confirmar e proximos passos

```
OK Voz da marca atualizada (v2).

PROXIMOS PASSOS:
- Toda skill de copy passa a usar essa voz automaticamente
- `/copy-marketing` para testar a nova voz em uma headline
- `/marketing-master` -> "regenerar BRAND-GUIDELINES" para consolidar
```

## OUTPUT ESPERADO

- `<cwd>/marketing/cowork-state.json` atualizado em `identity.voice`
- `<cwd>/marketing/MEMORY.md` secao `## Voz da Marca` atualizada
- Mensagem de confirmacao

## VEDACOES ESPECIFICAS

- **VE-01** — Rejeitar expressoes que prometam resultado falso
- **VE-04 (Track A)** — Rejeitar expressoes que pareçam captacao indevida
- **VE-12** — Rejeitar expressoes que configurem propaganda enganosa
- Validar exemplos contra TODAS as VEs aplicaveis ao track antes de salvar
- NUNCA salvar voz sem validacao do operador (preview + confirmacao)
- NUNCA sobrescrever voz existente sem perguntar

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — voz e parte da identidade
- **2.4 Compliance** — validacao das expressoes contra VEs aplicaveis
