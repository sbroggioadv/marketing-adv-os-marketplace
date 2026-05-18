---
name: marketing-copy-email-upsell
description: >
  MARKETING COPY EMAIL UPSELL — Gera email de upsell ou cross-sell para cliente ATIVO (ja comprou algo), oferecendo nivel superior, bonus pago, ou produto complementar. Aplica framework BASE-EXPANDIDA (reconhece o que ele ja tem + indica o que falta + reduz friccao da nova compra) sem pressao excessiva (cliente ja confia, pressao quebra confianca). Track A: precisa cuidado especial — upsell juridico nao pode soar como "voce nao recebeu meu melhor servico antes". Use quando o operador disser email de upsell, cross-sell, oferecer mais pra cliente, upgrade, expansao de cliente, oferta complementar.
---

# MARKETING COPY EMAIL UPSELL

> Skill Tier 2 (Executor — Copy). Email de upsell/cross-sell para base existente.

## OBJETIVO

Gerar 1-3 emails de upsell calibrados ao perfil do cliente (recencia + ticket + categoria do produto comprado), com framework que reconhece a base + indica a oportunidade + reduz friccao. Output: subject + corpo + CTA + UTM + segmentacao recomendada.

## PRE-REQUISITOS

Workspace + MEMORY. Operador fornece:
- **O que o cliente comprou:** produto/servico anterior + data aproximada
- **O que se quer vender (upsell):** versao premium / adicional / complementar
- **Diferenca real:** o que muda concretamente entre os dois
- **Preco do upsell + condicao especial pra cliente existente** (desconto, garantia estendida, etc)

## FLUXO

### 1. Validar coerencia do upsell

```
GATE DE COERENCIA:

1. O upsell adiciona valor REAL? (nao e so re-embalagem)
   - SIM (descreva o que muda)
   - NAO -> Bloqueio. Re-embalar produto antigo como "premium" e VE-12.

2. O cliente JA usou/extraiu valor do produto anterior?
   - SIM (esta no momento certo de expandir)
   - NAO (recem-comprou, ainda nao explorou) -> Esperar. Upsell prematuro destroe relacao.
   - DESCONHECIDO -> segmentar so quem usou ativamente

3. Track A — upsell juridico
   - Upsell de servico distinto (ex: tributario apos previdenciario): OK
   - Upsell como "agora oferecemos resultado melhor" -> BLOQUEIO. Implica que servico anterior era pior. VE-04+VE-07.
```

### 2. Segmentacao recomendada

Sugerir filtros para a lista:
- Comprou ha [X-Y] meses (nem novo demais nem antigo demais)
- Usou ativamente o produto (login recente, modulo concluido, contato com suporte)
- Ticket compativel (clientes que compraram baixo dificilmente sobem pra premium na primeira oferta)

### 3. Estrutura do email upsell

```
=== EMAIL UPSELL ===

Subject line (3 opcoes):
V1 — Reconhecimento: "Voce ja [acao do produto antigo]. Agora..."
V2 — Curiosidade: "[Beneficio especifico do upsell]"
V3 — Personal: "[Nome], uma proposta especifica pra voce"

Preview text: "[Reforco do beneficio + reducao de friccao]"

Corpo:

[BLOCO 1 — RECONHECIMENTO]
"Oi [Nome],
Voce ja [acao + tempo: 'esta com a gente ha 6 meses', 'concluiu o [modulo]', 'tem usado o [feature]']. Obrigado por isso."
- 2-3 linhas
- Especifico — usa dado real do CRM/sistema se possivel

[BLOCO 2 — INDICACAO]
"Notei que [contexto: 'voce tem usado [feature X] frequentemente', 'voce comentou que [Y]']. Achei que faria sentido te mostrar [upsell]."
- 2-3 linhas
- Conexao com comportamento OU pergunta direta do cliente

[BLOCO 3 — VALOR EXPANDIDO]
"O [upsell] adiciona:
- [Beneficio concreto 1]
- [Beneficio concreto 2]
- [Beneficio concreto 3]"
- 3-5 bullets
- Beneficios REAIS, nao re-embalagem

[BLOCO 4 — OFERTA]
"Pra voce, que ja [acao], tem uma condicao especial:
- Preco normal: R$ X
- Como cliente existente: R$ Y (com [garantia/bonus])
- Disponivel ate [data REAL]"
- 4-5 linhas
- Desconto REAL — nao "fake premium"

[BLOCO 5 — REDUCAO DE FRICCAO]
"Pra mudar pra [upsell], voce so precisa [acao simples: 'clicar no link abaixo', 'responder esse email', 'agendar 15 min']."
- 1-2 linhas
- Reduz objecao operacional

[CTA SINGULAR]
Botao: [Conhecer [upsell]] / [Quero saber mais] / [Mudar agora]

[Linha em branco]

[Assinatura pessoal — upsell e momento intimo, evitar "Equipe XYZ"]

[Linha em branco]

PS: "Se nao for o momento, sem problema — continue aproveitando seu [produto anterior]."
- PS importante: REDUZ pressao + abre permissao pra ignorar
```

### 4. Voz + tom

Voz do MEMORY com TOM PROXIMO (intensidade -1 do default). Upsell e momento de relacionamento, nao de impessoalidade comercial.

Track A: ainda mais cuidadoso — sem soar como "tenho um servico melhor agora" (insulta o servico anterior).
Track B: pode ser mais direto.

### 5. Diretoria Criativa R2 + R3 + R4

R2: subject + voz proxima + CTA singular + PS de saida (permissao).
R3:
- **Track A — VE-07:** NUNCA implicar que servico anterior era inferior. Upsell e EXPANSAO, nao SUBSTITUICAO.
- **Track A — VE-04:** Upsell NAO pode prometer resultado melhor.
- **Track B — VE-12:** Beneficios do upsell precisam ser VERIFICAVEIS.
- **Universal — VE-01:** Preco/desconto REAIS.
- **LGPD — VE-08, VE-09:** opt-out claro mesmo em email de cliente.

R4: UTM com identificacao do segmento (cliente-ativo / cliente-antigo / etc), target open-rate >30% (cliente abre mais), conversao >3-7%.

## OUTPUT

Email estruturado + 3 subject lines + segmentacao recomendada + UTMs + veredito.

## VEDACOES ESPECIFICAS

- **VE-07 (Track A) — CRITICA:** Upsell NUNCA pode rebaixar produto anterior
- **VE-04 (Track A):** Upsell NAO pode prometer resultado processual diferente
- **VE-12:** Re-embalagem do mesmo produto como "premium" = VIOLACAO
- **VE-01:** Desconto/condicao especial REAIS
- **NUNCA pressao excessiva** — cliente JA confia, pressao destroe relacao
- **PS de saida obrigatorio:** "se nao for o momento, tudo bem" — protege relacionamento

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — gate de coerencia + segmentacao
- **2.3 Producao** — voz proxima + tom relacional
- **2.4 Compliance** — VE-07 (Track A) prioritaria
- **2.5 Mensuracao** — segmentacao por comportamento real
