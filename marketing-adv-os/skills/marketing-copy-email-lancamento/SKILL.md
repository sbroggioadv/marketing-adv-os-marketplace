---
name: marketing-copy-email-lancamento
description: >
  MARKETING COPY EMAIL LANCAMENTO — Gera sequencia de lancamento completa em 3 fases: PRE-LANCAMENTO (aquecimento — 3-5 emails entregando valor + criando urgencia narrativa REAL), ABERTURA (3 emails: oferta + ancoragem + bonus), FECHAMENTO (3 emails: ultimas vagas/horas + objecoes + ultima chamada). Aplica scarcity REAL (vagas/turma com numero verificavel) e urgencia REAL (prazo de matricula). NUNCA scarcity fake. Use quando o operador disser sequencia de lancamento, drip de lancamento, lancamento de curso, lancamento de produto, fechamento de turma.
---

# MARKETING COPY EMAIL LANCAMENTO

> Skill Tier 2 (Executor — Copy). Sequencia completa de lancamento (3 fases).

## OBJETIVO

Produzir sequencia de lancamento de ~10 emails distribuidos em 3 fases (Pre + Abertura + Fechamento). Calendario detalhado com dia/hora/email + subject + corpo + CTA + UTM + metrica esperada.

## PRE-REQUISITOS

Workspace + MEMORY. Operador define:
- Produto/curso em lancamento + preco + bonus + garantia
- Data de abertura + data de fechamento
- Lista (segmento) que recebe
- Plataforma de envio

## FLUXO

### 1. Briefing especifico de lancamento

```
GATE DE COERENCIA DO LANCAMENTO:

1. Vagas/turma: numero REAL e verificavel? (X alunos por turma, infraestrutura limita)
   - SIM (qual numero)
   - NAO (sem turma fechada) -> sem usar scarcity. Usar urgencia narrativa.

2. Data de fechamento: REAL ou movel?
   - REAL (data fixa, infraestrutura justifica)
   - MOVEL (so pra criar urgencia) -> ATENCAO VE-05. Reformular como "prazo recomendado".

3. Bonus: REAL (existem + tem prazo) ou fake (ficam pra sempre)?
   - REAL (com prazo curto)
   - FAKE (sempre disponivel mas chamado de "bonus por tempo limitado") -> VE-12 violacao.

4. Garantia: oferecida? Termos claros?
   - 7d / 14d / 30d / 60d / outros
   - SEM garantia (Track A juridico nao da garantia de resultado)

5. Preco: ancoragem REAL (de R$ X por R$ Y)? Numeros verificaveis?
   - Ancoragem com base real (preco anterior, valor de mercado, soma de bonus)
   - Ancoragem inventada -> VE-12 violacao.
```

Se qualquer item falha o gate: reformular ou bloquear.

### 2. Estrutura da sequencia

**FASE 1 — PRE-LANCAMENTO (D-10 a D-1) — 4 emails:**

```
Email PRE-1 (D-10): "Estou trabalhando em algo"
  Subject: "[teaser sem revelar tudo]"
  Corpo: Reflexao sobre a dor que o produto resolve. Sem mencionar o produto ainda.
  CTA: responder com sua dor especifica

Email PRE-2 (D-7): "O problema que me incomoda"
  Subject: "[pergunta provocadora sobre dor]"
  Corpo: Aprofundar a dor. Cases (com autorizacao Track A). Indicar que ha solucao.
  CTA: opt-in para "lista preferencial"

Email PRE-3 (D-4): "Tenho uma novidade"
  Subject: "[revela: produto X]"
  Corpo: Apresentar o produto. Sem preco ainda. So contexto + transformacao prometida.
  CTA: cadastrar interesse / participar live de pre-lancamento

Email PRE-4 (D-1): "Amanha abre"
  Subject: "[prepara: amanha as XX:XX]"
  Corpo: Confirmar abertura. Lembrar do beneficio. Construir antecipacao.
  CTA: salvar lembrete / agendar evento
```

**FASE 2 — ABERTURA (D+0 a D+3) — 3 emails:**

```
Email ABR-1 (D+0): "Estamos abertos"
  Subject: "[ABERTURA com hora]"
  Corpo: Inscricoes abertas. Detalhes da oferta. Preco. Ancoragem. Garantia.
  CTA: link direto pro checkout

Email ABR-2 (D+1): "Quem ja entrou diz"
  Subject: "[prova social ou bastidor]"
  Corpo: Depoimentos de quem ja entrou nas primeiras 24h. OU bastidor de quem participou em turma anterior.
  CTA: link direto

Email ABR-3 (D+3): "Sobre as duvidas"
  Subject: "[FAQ central]"
  Corpo: 5-7 perguntas mais frequentes da abertura, respondidas. Reduz friccao.
  CTA: link direto + responder com duvida persistente
```

**FASE 3 — FECHAMENTO (D+4 a D+7) — 3 emails:**

```
Email FECH-1 (D+5): "Ultimas vagas / horas"
  Subject: "[contagem REAL — X vagas / Y horas]"
  Corpo: Numero VERIFICAVEL. NUNCA fake. Recapitular oferta + garantia.
  CTA: link direto

Email FECH-2 (D+6): "Objecoes finais"
  Subject: "[trata a maior objecao]"
  Corpo: Endereca a objecao #1 (geralmente preco, tempo, ou ceticismo). Reduz friccao.
  CTA: link direto

Email FECH-3 (D+7, dia do fechamento): "Hoje as XX:XX fecha"
  Subject: "[urgencia REAL com hora exata]"
  Corpo: Ultima chamada. Reforco da transformacao. Garantia. CTA forte.
  CTA: link direto
```

### 3. Subject lines (3 alternativas por email)

Para cada um dos 10 emails: 3 alternativas para A/B.

### 4. Voz + ancoragem narrativa

Voz do MEMORY com TOM ESCALANTE: pre-lancamento mais contemplativo, abertura energetico-claro, fechamento direto-urgente.

Ancoragem narrativa (Russell Brunson): construir 3-5 "stacks" de valor antes de mostrar preco:
- "Voce vai aprender X (vale R$ A)"
- "+ bonus Y (vale R$ B)"
- "+ comunidade Z (vale R$ C)"
- "Total: R$ X + R$ A + R$ B + R$ C = R$ D"
- "Hoje, por R$ E (X% menos que o valor total)"

### 5. Diretoria Criativa R2 + R3 + R4

R2: cada email tem CTA singular + voz adequada a fase.
R3:
- **VE-01:** scarcity REAL — fake scarcity = VE-01 + VE-12 violacao
- **VE-05 (Track A):** lancamento juridico nao pode ter "ultima chance!!" — reformular como "prazo de matricula"
- **VE-12:** ancoragem com numero verificavel
- **VE-04 (Track A):** nunca promessa de resultado processual em lancamento de curso juridico
- **VE-08, VE-09:** opt-out claro em TODOS os emails

R4: UTM por email, target open-rate >25%, click-rate >5%, conversao da sequencia em [N]%.

## OUTPUT

Sequencia completa (10 emails) estruturados + subject lines alternativas + UTMs + plano de envio + veredito.

## VEDACOES ESPECIFICAS

- **VE-01, VE-12 — CRITICAS:** scarcity ou ancoragem fake = BLOQUEIO TOTAL
- **VE-05 (Track A):** urgencia falsa em curso juridico = VE-05 violado
- **VE-04 (Track A):** "voce vai ganhar processos" = BLOQUEIO
- **NUNCA estender prazo apos email final "hoje fecha"** — quebra a confianca da lista para sempre
- LGPD: opt-out claro em TODOS os emails

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — gate de coerencia obrigatorio
- **2.3 Producao** — voz escalante por fase
- **2.4 Compliance** — VE-01, VE-12, VE-05 sao prioritarias
- **2.5 Mensuracao** — UTM por email + funil completo da sequencia
