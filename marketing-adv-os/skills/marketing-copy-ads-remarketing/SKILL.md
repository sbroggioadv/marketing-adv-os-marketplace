---
name: marketing-copy-ads-remarketing
description: >
  MARKETING COPY ADS REMARKETING — Gera copy especifica para anuncios de remarketing (Meta/Google/LinkedIn), segmentados por estagio de drop-off do funil: (1) viu LP mas nao deu lead, (2) deu lead mas nao agendou demo, (3) agendou mas nao compareceu, (4) abandono de carrinho/checkout, (5) cliente antigo dormente (winback). Cada estagio tem tom + gatilho + reducao de friccao diferentes. NUNCA tom acusatorio ("voce esqueceu seu carrinho!"). Use quando o operador disser copy de remarketing, retargeting, carrinho abandonado, winback, anuncio pra quem ja conhece.
---

# MARKETING COPY ADS REMARKETING

> Skill Tier 2 (Executor — Copy). Remarketing por estagio de drop-off.

## OBJETIVO

Gerar 5 copies de remarketing, uma por estagio de drop-off (LP-view, lead, no-show, abandono-checkout, winback), cada uma calibrada com tom + gatilho + reducao de friccao adequados ao ponto do funil onde o usuario parou.

## PRE-REQUISITOS

Workspace + MEMORY. Operador precisa dizer quais estagios sao relevantes (nem todo funil tem todos os 5).

## FLUXO

### 1. Mapear funil do operador

> "Quais estagios de drop-off voce quer recuperar? (multi-select)
> (a) Visitou LP mas nao virou lead (formulario nao preenchido)
> (b) Virou lead mas nao agendou proximo passo
> (c) Agendou demo/consulta mas nao compareceu
> (d) Iniciou checkout mas abandonou (e-commerce ou produto digital)
> (e) Cliente antigo dormente (>6 meses sem comprar/contratar)
>
> Tambem confirme:
> - Plataforma de exibicao: Meta / Google Display / LinkedIn / mix
> - Janela de retargeting: 7d / 14d / 30d / 90d
> - Frequency cap: max impressoes/usuario/semana"

### 2. Aplicar copy por estagio

**Estagio (a) — LP-view sem lead:**
- Hipotese: nao se convenceu da promessa OU teve duvida nao respondida
- Tom: educativo, sem pressao
- Gatilho: prova social adicional, FAQ-style, garantia em destaque
- Exemplo de hook: "Voce viu nosso curso mas ficou na duvida. Veja [X] alunos que ja [resultado]"

**Estagio (b) — lead sem agendamento:**
- Hipotese: friccao no proximo passo (formulario longo, falta clareza do que esperar)
- Tom: especifico sobre o que acontece em seguida
- Gatilho: reducao de friccao + clareza do proximo passo
- Exemplo: "[Tempo] reunido. Voce escolhe o horario. Sem compromisso."

**Estagio (c) — agendou sem comparecer:**
- Hipotese: agenda virou conflito OU mudou de ideia OU esqueceu
- Tom: acolhedor, sem julgamento
- Gatilho: reagendamento facil, lembrete de valor
- Exemplo: "Acontece. Quer re-agendar? Link direto pra seu novo horario."

**Estagio (d) — abandono checkout:**
- Hipotese: preco, friccao no pagamento, segunda opiniao, distracao
- Tom: AJUDADOR, nao acusatorio (proibido: "voce esqueceu seu carrinho")
- Gatilho: garantia, prova social, escassez REAL se aplicavel
- Exemplo: "Sobrou alguma duvida? Estamos no chat. Ou termine aqui em 60 seg."

**Estagio (e) — winback de dormente:**
- Hipotese: cliente teve experiencia OK mas saiu do radar; lembrar de valor
- Tom: reconectar, atualizar, novidade
- Gatilho: novidade no produto, conteudo exclusivo, oferta personalizada
- Exemplo: "Voltamos com [novidade]. Vale dar uma olhada — leva 2 min."

### 3. Estrutura de cada copy

```
ESTAGIO (a) — LP-view sem lead

Texto principal (max 200 chars):
[copy]

Headline:
[curta, 30-40 chars]

Descricao:
[reforco do beneficio + reducao friccao]

CTA: [adequado ao estagio]
Gatilho: [prova social | reducao risco | clareza | reconectar]

UTM sugerido: utm_source=meta&utm_medium=remarketing&utm_campaign=<campanha>&utm_content=stage-a

NOTA: este copy NAO repete o copy de aquisicao. Assume contexto previo.
```

Repetir para cada estagio selecionado.

### 4. Frequency cap e janela

> "RECOMENDACOES DE EXIBICAO:
> - Estagio (a): 30 dias, max 3x/semana
> - Estagio (b): 14 dias, max 5x/semana
> - Estagio (c): 7 dias, max 4x/semana (urgencia maior)
> - Estagio (d): 7-14 dias, max 3x/semana
> - Estagio (e): 30-60 dias, max 2x/semana (sem fadiga)"

### 5. Diretoria Criativa R2 + R3 + R4

R2: voz + tom apropriado ao estagio + CTA singular.
R3:
- **NUNCA acusatorio:** proibido "voce esqueceu", "voce nao terminou" — soa intrusivo
- **VE-04 (Track A):** estagio (e) NAO pode prometer novo resultado
- **VE-12, VE-01:** estagio (c) sem urgencia falsa
R4: cada estagio com UTM unico, metrica de retorno definida (lead-rate, completion-rate, repeat-rate).

## OUTPUT

5 copies de remarketing (uma por estagio) + recomendacoes de exibicao + veredito.

## VEDACOES ESPECIFICAS

- **NUNCA tom acusatorio** — "voce esqueceu", "voce abandonou" sao intrusivos
- **VE-02** — NUNCA manipulacao via culpa ("voce vai perder essa chance")
- **VE-01** — NUNCA superlativo no winback ("sua ultima chance")
- **VE-04 (Track A)** — NUNCA promessa de resultado processual em winback de cliente juridico
- Frequency cap RESPEITADO — exceder gera fadiga + banimento de conta

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — mapeamento de funil + estagios relevantes
- **2.3 Producao** — voz adaptada ao estagio (tom diferente por etapa)
- **2.4 Compliance** — VE-02 (sem manipulacao) prioritario
- **2.5 Mensuracao** — UTM por estagio + metrica de retorno
