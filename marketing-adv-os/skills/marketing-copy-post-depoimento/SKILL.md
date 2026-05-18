---
name: marketing-copy-post-depoimento
description: >
  MARKETING COPY POST DEPOIMENTO — Gera post de depoimento/case de cliente, estruturado para sustentar prova social sem virar propaganda enganosa. Aplica framework SITUACAO+DESAFIO+TRANSFORMACAO+METRICA+FALA-DO-CLIENTE. Track A: exige autorizacao escrita do cliente (VE-15 — sigilo profissional) e NAO promete resultado generalizavel (VE-04). Track B: exige fala real do cliente, sem fabricacao (VE-12). Use quando o operador disser post de depoimento, case de cliente, post de transformacao, prova social, case de sucesso pro Instagram.
---

# MARKETING COPY POST DEPOIMENTO

> Skill Tier 2 (Executor — Copy). Post de depoimento/case de cliente.

## OBJETIVO

Produzir post de depoimento que apresente case real de cliente como prova social, sem violar VE-04 (promessa de resultado generalizavel), VE-15 (sigilo profissional em Track A) ou VE-12 (case fabricado).

## PRE-REQUISITOS

Workspace + MEMORY. **Critico:** operador precisa fornecer:
1. **Autorizacao escrita** do cliente (Track A: OBRIGATORIO. Track B: recomendado mas opt-in)
2. **Fala literal** do cliente OU fala consolidada com aprovacao do cliente (sem ficcao)
3. **Dado mensuravel** da transformacao (numero, tempo, porcentagem) — verificavel

## FLUXO

### 1. Validar autorizacao (critico)

```
GATE DE AUTORIZACAO:

Track A (advogado): Voce tem autorizacao ESCRITA do cliente (e-mail, mensagem, documento assinado)
                    permitindo uso publico do case?
                    - [ ] SIM (descreva o formato)
                    - [ ] NAO -> BLOQUEAR. Sugestao: pedir autorizacao OU usar persona representativa
                                 com declaracao explicita "case composto"
                    - [ ] NAO TENHO CERTEZA -> tratar como NAO

Track B (empresario): Voce tem confirmacao por escrito do cliente?
                    - SIM (preferido)
                    - NAO -> ainda passa, mas declarar publico nao-nominal
```

Se Track A SEM autorizacao escrita: **BLOQUEAR PRODUCAO**. Oferecer alternativas (persona representativa declarada, ou pedir autorizacao).

### 2. Coletar dados

> "Para gerar o post, preciso de:
> 1. **Quem e o cliente:** nome (se autorizado) OU descricao funcional ('empresa de [setor], faturamento [faixa]', 'segurado(a) [perfil profissional]')
> 2. **Situacao antes:** o que estava acontecendo, o problema concreto
> 3. **Desafio especifico:** o que tornava o problema dificil de resolver sozinho
> 4. **Solucao aplicada:** como sua oferta entrou (sem detalhes processuais sensiveis em Track A)
> 5. **Metrica de transformacao:** numero verificavel (tempo, percentual, valor recuperado, etc)
> 6. **Fala do cliente:** literal OU consolidada com aprovacao"

### 3. Estrutura do post

```
=== POST DEPOIMENTO ===

HOOK (1ª linha — sobrevive ao "ver mais"):
[Numero impactante OU pergunta sobre o problema OU afirmacao do antes/depois sem exagero]

CORPO:
[Bloco SITUACAO]
"Quando [cliente] me procurou, [contexto factual da situacao antes]."
- 2-3 linhas
- Especifico mas sem expor PII (CPF, processo, valor sensivel se Track A)

[Bloco DESAFIO]
"O desafio era [especifico — por que era dificil resolver sozinho]."
- 1-2 linhas

[Bloco SOLUCAO]
"Aplicamos [metodologia/abordagem — sem prometer que ela serve pra todos]."
- 2-3 linhas
- Track A: sem mencao a estrategia processual especifica que possa quebrar sigilo

[Bloco METRICA]
"Em [tempo], conseguimos [resultado mensuravel]."
- 1 linha
- Numero VERIFICAVEL — sem arredondar pra mais

[Bloco FALA DO CLIENTE]
"[Fala literal ou consolidada com aprovacao escrita]" — [Cliente/perfil]
- Entre aspas — sinal claro de citacao

[Bloco DISCLAIMER]
"*Resultado individual baseado em [contexto]. Cada caso e unico — nao constitui promessa de resultado."
- OBRIGATORIO em Track A
- Recomendado em Track B (reduz risco CONAR)

CTA:
- Track A: "Quer entender se sua situacao tem caminho parecido? Marca uma conversa." (NAO "ligue ja!")
- Track B: "Quer ver mais cases como esse? Link na bio" / "Comenta seu desafio que respondo"

#hashtag1 #hashtag2 ... (max 5-10)
```

### 4. Voz + autenticidade

Voz do MEMORY com TOM HUMANIZADO (intensidade -1 ou -2 do default — depoimento e momento de pausa, nao de combate).

Adicionar 1 elemento de imperfeicao no bloco SOLUCAO (autenticidade): "Tivemos que ajustar [X] no meio do caminho", "Nao foi linear — em [momento] precisamos [Y]".

### 5. Diretoria Criativa R2 + R3 + R4

R2: estrutura S-D-S-M-F clara, hook + voz humanizada + CTA singular.
R3:
- **Track A — VE-15 (CRITICO):** autorizacao escrita confirmada? Senao, BLOQUEIO TOTAL.
- **Track A — VE-04:** disclaimer presente? Disclaimer sem disclaimer = promessa de resultado generalizada = VE violada.
- **Track A — sigilo profissional:** detalhes processuais sensiveis omitidos?
- **Track B — VE-12:** fala literal ou consolidada com aprovacao? Sem fabricacao?
- **Universal — VE-01:** numero verificavel?

R4: KPI = engajamento + DM/conversas geradas + (Track A) qualidade de novas consultas.

## OUTPUT

Post estruturado + disclaimer + plano KPI + veredito + (se aplicavel) BLOQUEIO com motivo.

## VEDACOES ESPECIFICAS

- **VE-15 (Track A) — CRITICA:** Case real sem autorizacao escrita = BLOQUEIO TOTAL
- **VE-04 (Track A):** Disclaimer obrigatorio. Sem disclaimer, promessa generalizada = violacao.
- **VE-12:** Fala fabricada = BLOQUEIO. Fala precisa ser literal ou consolidada com aprovacao.
- **VE-01:** Numero precisa ser verificavel — sem arredondamento "pra mais"
- **PII (CPF, processo, valor sensivel)** — NUNCA aparece no post, mesmo com autorizacao

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — gate de autorizacao + coleta de dados
- **2.4 Compliance** — VE-15 e VE-04 sao prioritarias (Track A); VE-12 e VE-01 universais
- **2.5 Mensuracao** — KPI nao e curtida, e DM/conversa qualificada
