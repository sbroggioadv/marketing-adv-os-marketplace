---
name: marketing-diretoria-r2-copy
description: >
  DIRETORIA R2 COPY — Segundo gate da Diretoria Criativa. Audita se o copy de uma peca esta forte ANTES de mandar para Compliance (R3). Verifica 6 itens: hook nos primeiros 3s/7 palavras, voz consistente com MEMORY, gatilho psicologico nominado, clareza (frase media <=18 palavras), CTA singular, sem promessa falsa (VE-01). Falha = volta para revisao do copy. Use quando o operador disser audita copy, R2 da peca, revisa texto antes de publicar, segunda etapa Diretoria.
---

# DIRETORIA R2 COPY

> Skill Tier 3 (Diretoria Criativa — Gate 2). Audita copy antes de Compliance.

## OBJETIVO

Validar que o copy de uma peca cumpre os requisitos editoriais minimos para ser efetivo. Copy fraco nao salva nem com arte perfeita — R2 protege contra desperdicio de impressoes pagas e organicas.

## PRE-REQUISITOS

- R1 (Brief) ja aprovado (executar `diretoria-r1-brief` antes)
- Copy completo da peca (cole na sessao ou aponte path)
- MEMORY consultado: `## Voz da Marca`

## FLUXO

### 1. Receber copy

> "Vou auditar R2 (Copy). Cole o copy completo da peca OU me aponte o path.
> Identifique: qual e o canal e formato? (afeta o que conta como 'hook')"

### 2. Checklist 6 itens

```
GATE R2 — COPY:

[1] HOOK NOS PRIMEIROS 3S / 7 PALAVRAS
    Por canal:
    - Reels/TikTok: primeiros 3 segundos (texto on-screen ou fala)
    - Carrossel: slide 1 (capa)
    - Email: subject line (max 50 chars)
    - Anuncio: primeiras 7 palavras do texto principal
    - LP: H1 hero
    Hook FORTE: numero impactante, pergunta provocadora, afirmacao contraintuitiva, pain point especifico
    Hook FRACO: "hoje vou falar sobre...", "voce sabia que...", clickbait barato
    -> Se FRACO: dar 3 sugestoes baseadas em strategias validadas

[2] VOZ CONSISTENTE COM MEMORY
    Consultar <cwd>/marketing/MEMORY.md secao ## Voz da Marca
    Verificar:
    - Tom (institucional / didatico / comercial / storyteller) bate?
    - Intensidade (1-10) bate?
    - Expressoes assinatura aparecem onde natural?
    - Termos a evitar NAO aparecem?
    -> Se inconsistente: marcar trechos especificos que fogem da voz

[3] GATILHO PSICOLOGICO NOMINADO
    Cada peca de venda/copy precisa explicitar 1 (max 2) gatilhos:
    - Autoridade (dado, julgado, anos de experiencia)
    - Prova social (X clientes, Y empresas, Z testimonials)
    - Escassez REAL (turma fechada, vagas limitadas — sem urgencia falsa)
    - Reciprocidade (lead magnet, dica antes de pitch)
    - Curiosidade (lacuna informacional, "o que ninguem te conta sobre...")
    - Novidade (nova lei, novo metodo, primeira vez)
    Conteudo educativo pode ter gatilho mais sutil (autoridade implicita)
    -> Se NENHUM gatilho identificavel: copy provavelmente generico — sugerir refinar

[4] CLAREZA (frase media <= 18 palavras)
    Contar palavras das 5 frases mais longas:
    - Media >= 18 palavras: 1 ponto
    - Media >= 22 palavras: 2 pontos (perigo)
    - Media >= 28 palavras: 3 pontos (refazer)
    Subordinacao max 2 niveis (que ... que ... que = ruim)
    Voz ativa preferida sobre passiva
    -> Se complexo: marcar frases > 25 palavras pra reescrita

[5] CTA SINGULAR
    Conte os CTAs do copy. Quantos?
    - 1 CTA primario: OK
    - 2 CTAs (primario + secundario): OK se hierarquia clara
    - 3+ CTAs: FALHA — leitor congelado, paradoxo da escolha
    CTA primario deve aparecer:
    - LP: hero + meio + final (mesma acao)
    - Email: 1 botao primario + opcionalmente link de texto secundario
    - Post: 1 chamada implicita ou explicita
    - Anuncio: 1 CTA na chamada + 1 botao
    -> Se >= 3 acoes diferentes: pedir pra escolher 1

[6] SEM PROMESSA FALSA (VE-01)
    Buscar pattern matches:
    - Superlativos: "o melhor", "o unico", "a maior", "100% de..."
    - Garantias absolutas: "garanto que", "voce vai conseguir", "guaranteed"
    - Resultado universal: "todo mundo que aplica consegue", "todos os meus alunos"
    - Track A: "voce vai ganhar a acao", "garanto sua aposentadoria", "recupera 100%"
    -> Cada match: marcar trecho e sugerir reformulacao
```

### 3. Veredito

```
DIRETORIA R2 — COPY: <APROVADO | REVISAR | FALHA CRITICA>

[1] Hook nos primeiros 3s:    OK | FRACO (sugestoes: ...)
[2] Voz consistente MEMORY:   OK | INCONSISTENTE (trechos: ...)
[3] Gatilho psicologico:      OK (gatilho: ...) | AUSENTE
[4] Clareza (<=18 palavras):  OK (media X) | COMPLEXO (frases: ...)
[5] CTA singular:             OK | MULTIPLO (CTAs encontrados: ...)
[6] Sem promessa falsa:       OK | VIOLACAO (trecho: "..." -> sugestao: "...")

DECISAO:
- APROVADO: prosseguir para R3 (Compliance)
- REVISAR: ajustes pontuais antes de R3
- FALHA CRITICA: copy precisa reescrita substancial
```

### 4. Quando passar pra R3

Se aprovado:
> "R2 OK. R3 (Compliance) ja pode rodar — `diretoria-r3-compliance`. Track {{A|B}} carregado automaticamente."

## OUTPUT

Veredito estruturado + trechos a revisar (se aplicavel) + sugestoes especificas + decisao.

## VEDACOES ESPECIFICAS

- **VE-01 critica:** promessa falsa = BLOQUEIO ate corrigir
- **3+ CTAs:** falha de design — leitor nao age
- **Voz incoerente com MEMORY:** marca fica diluida — sempre marcar trechos

## PROTOCOLOS ACIONADOS

- **2.3 Producao** — checa producao contra padrao voz registrado
- **2.4 Compliance** — VE-01 universal e gate aqui
