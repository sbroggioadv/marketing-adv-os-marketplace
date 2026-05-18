---
name: marketing-copy-cta
description: >
  MARKETING COPY CTA — Gerador especializado de Call-to-Action calibrado por contexto: canal (LP hero / botao secundario / email / anuncio / post social), estagio do funil (frio / morno / quente), tipo de conversao (clique / lead / agendamento / compra / engajamento), e nivel de compromisso pedido (baixo / medio / alto). Aplica framework VERBO IMPERATIVO + OBJETO ESPECIFICO + REDUCAO DE FRICCAO. Track A: ajusta tom (sem "ligue ja!" — VE-06 captacao). Use quando o operador disser gerar CTA, melhorar CTA, alternativas de call to action, botao do hero, CTA pro email, CTA pro anuncio.
---

# MARKETING COPY CTA

> Skill Tier 2 (Executor — Copy). Gerador de CTAs calibrados por contexto.

## OBJETIVO

Gerar 7 variacoes de CTA calibradas ao contexto especifico (canal + estagio do funil + tipo de conversao). Output em tabela com hipotese de teste e veredito Diretoria.

## PRE-REQUISITOS

Workspace + MEMORY com voz da marca. Operador fornece:
- **Canal:** LP hero / botao secundario / banner / email body / email button / anuncio / post social / story
- **Estagio do funil:** frio (publico nunca viu) / morno (engajou antes) / quente (intencao alta)
- **Tipo de conversao desejada:** clique (apenas) / lead (formulario) / agendamento / compra / engajamento (comentario, salvamento, encaminhamento)
- **Friccao pedida:** baixa (1 clique, sem dados) / media (formulario curto, cadastro) / alta (compra, agendamento, demo)

## FLUXO

### 1. Briefing

> "Vou gerar 7 CTAs pra:
> - Canal: [...]
> - Estagio funil: [...]
> - Conversao: [...]
> - Friccao: [...]
> - Beneficio principal por tras (que o CTA referencia): [...]"

### 2. Framework de geracao

Cada CTA forte tem 3 componentes:

```
VERBO IMPERATIVO  +  OBJETO ESPECIFICO  +  REDUCAO DE FRICCAO
   ("Comece")        ("o teste gratis")     ("em 30 seg, sem cartao")
```

Bibliotecas de verbos por estagio:

**Frio** (publico nunca viu — verbos de baixo compromisso):
- Descobrir, Ver, Conhecer, Explorar, Entender, Receber

**Morno** (engajou antes — verbos de avancar):
- Comecar, Testar, Experimentar, Acessar, Baixar, Reservar, Salvar

**Quente** (intencao alta — verbos de acao):
- Comprar, Garantir, Inscrever, Agendar, Confirmar, Ativar, Avancar

**Track A — verbos seguros (sem captacao):**
- Informativo: Saber mais, Entender melhor, Aprofundar, Ler, Estudar
- Acesso: Acessar artigo, Baixar material
- Conversa: Marcar conversa (NUNCA "ligue ja", "consulte agora" — VE-06)

### 3. Gerar 7 variacoes por angulo

```
=== CTAs PARA [contexto] ===

| #  | CTA                                    | Angulo psicologico   | Funciona melhor em       | Hipotese de teste                |
|----|----------------------------------------|----------------------|--------------------------|----------------------------------|
| 1  | "Quero descobrir como"                 | curiosidade          | publico frio             | aumenta CTR em hero de LP        |
| 2  | "Comecar gratis em 30s"                | reducao friccao      | publico morno            | reduz friccao no formulario      |
| 3  | "Reservar minha vaga"                  | escassez REAL        | turma fechada (lancto)   | reduz hesitacao em fechamento    |
| 4  | "Ver demo (sem compromisso)"           | reducao compromisso  | enterprise/B2B           | atrai comprador cetico           |
| 5  | "Garantir [beneficio]"                 | promessa direta      | quente (alto intent)     | melhor conversao final           |
| 6  | "Falar com [especialista/equipe]"      | personalizacao       | alto-ticket              | qualifica lead via conversa      |
| 7  | "Receber [recurso] no email"           | troca de valor       | captura de lead          | maximiza opt-in                  |
```

### 4. Recomendacao por contexto

> "RECOMENDACAO pra [canal informado]:
> - [#X]: principal — angulo [Y] funciona melhor em [Z contexto]
> - [#A]: alternativo pra A/B teste
> - EVITAR: [CTAs que nao se encaixam no contexto]
>
> Track A — atencao: CTAs #X e #Y deveriam ser ajustados pra nao soar como captacao OAB"

### 5. Voz + termos a evitar

Aplicar voz do MEMORY. Termos a evitar removidos. Track A: substituir "ligue", "consulte agora", "atendimento imediato" por alternativas informativas.

### 6. Diretoria Criativa R2 + R3 + R4

R2: cada CTA tem VERBO + OBJETO + (REDUCAO opcional) + voz consistente.
R3:
- **Track A — VE-06:** sem captacao agressiva ("ligue ja", "atendimento 24h")
- **Track A — VE-04:** sem promessa de resultado embutida ("Garantir minha aposentadoria" -> "Marcar conversa sobre minha aposentadoria")
- **Track B — VE-01:** sem superlativo ("melhor oferta da sua vida")
- **Universal:** VE-02 (sem manipulacao via medo/culpa: "Nao perca essa unica oportunidade")

R4: target click-through-rate (CTR) por canal:
- LP hero: 25-40%
- Email: 3-7%
- Anuncio: 1-5%

## OUTPUT

Tabela de 7 CTAs + recomendacao por contexto + veredito Diretoria.

## VEDACOES ESPECIFICAS

- **VE-06 (Track A):** "Ligue ja", "Consulte agora", "Atendimento imediato" = captacao = BLOQUEIO
- **VE-04 (Track A):** "Garantir vitoria", "Conquistar processo" = promessa = BLOQUEIO
- **VE-02:** Manipulacao via medo/culpa ("Nao perca essa chance unica") = BLOQUEIO
- **VE-01:** Superlativo sem prova ("CTR melhor possivel") = BLOQUEIO
- CTAs com mais de 6 palavras tipicamente convertem pior — alertar

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — contexto + estagio + friccao
- **2.3 Producao** — voz + verbos adequados ao estagio
- **2.4 Compliance** — Track A com cuidado extra em verbos de captacao
- **2.5 Mensuracao** — CTR target por canal
