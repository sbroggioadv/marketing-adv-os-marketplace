---
name: marketing-copy-headline-aida
description: >
  MARKETING COPY HEADLINE AIDA — Gera 10 headlines de alta conversao aplicando o framework AIDA (Atencao, Interesse, Desejo, Acao) ao briefing do operador. Cada headline e classificada pelo elemento AIDA dominante, recebe nota estimada de impacto (1-10) e vem com variacao A/B sugerida. Consulta voz da marca + publico-alvo + oferta do MEMORY automaticamente. Use quando o operador disser gerar headlines, criar titulos, headlines AIDA, headline pra landing page, headline pra anuncio, titulos de email, titulo de artigo, headline de venda.
---

# MARKETING COPY HEADLINE AIDA

> Skill Tier 2 (Executor — Copy). Gera headlines aplicando framework AIDA.

## OBJETIVO

Produzir 10 headlines de alta conversao usando AIDA, com classificacao por elemento dominante (A/I/D/A), nota 1-10 de impacto estimado, e variacao A/B para teste. Aplicavel a LP, anuncios, emails, posts de oferta, artigos.

## PRE-REQUISITOS

1. Workspace marketing configurado (`<cwd>/marketing/cowork-state.json` existe).
2. Consultar MEMORY:
   - `## Voz da Marca` -> perfil + intensidade + expressoes assinatura + termos a evitar
   - `## Publico-alvo` -> persona + dor principal
   - `## Oferta` -> servico/produto + ticket
3. Se faltam dados criticos (publico/dor/oferta), perguntar antes de gerar.

## FLUXO

### 1. Briefing rapido (se necessario)
Se MEMORY ja tem publico+dor+oferta, confirmar:
> "Vou gerar 10 headlines AIDA pra: [Oferta]. Publico: [persona]. Dor: [dor].
> Algum contexto adicional (canal especifico, prazo, beneficio em destaque)?"

Se faltar dado: perguntar antes.

### 2. Gerar 10 headlines

Aplicar AIDA — cada headline forte em UM elemento:
- **A (Atencao):** numero impactante, contraste forte, pergunta provocadora, afirmacao contraintuitiva
- **I (Interesse):** prova social, dado especifico, beneficio especifico mensuravel
- **D (Desejo):** transformacao concreta, antes/depois, resultado emocional
- **A (Acao):** verbo de comando + prazo + reducao de friccao ("comece em 5 min", "sem cartao")

Aplicar voz da marca: tom + intensidade + expressoes assinatura. Respeitar termos a evitar.

### 3. Tabela de saida

```
| #  | Headline                                            | AIDA | Nota | Variacao A/B           |
|----|-----------------------------------------------------|------|------|------------------------|
| 1  | ...                                                 | A    | 8    | ...                    |
| 2  | ...                                                 | I    | 7    | ...                    |
...
| 10 | ...                                                 | A    | 9    | ...                    |
```

### 4. Top 3 + justificativa

Apos a tabela, destacar as 3 melhores com explicacao curta (1-2 frases cada):
> "**TOP 1 (#X):** [headline]. Funciona porque [razao especifica]."

### 5. Submissao a Diretoria Criativa R2 + R3

Antes de declarar concluido, mensagem:
> "Rodando R2 (Copy) e R3 (Compliance) — track: <A|B>"

R2 valida: hook + clareza + CTA implicito + voz consistente.
R3 valida: Track A -> VE-04 (sem promessa de resultado em servico juridico). Track B -> VE-12 (sem propaganda enganosa), VE-01 (sem superlativo sem prova).

Headlines reprovadas: substituir com alternativas equivalentes.

## OUTPUT

Tabela de 10 headlines + top 3 com justificativa + nota da Diretoria Criativa (APROVADO ou REVISAR).

## VEDACOES ESPECIFICAS

- **VE-01** — NUNCA gerar headline com superlativo sem prova ("o melhor", "garantido", "100%")
- **VE-04 (Track A)** — NUNCA prometer resultado processual ("voce vai ganhar", "garanto sua aposentadoria")
- **VE-05 (Track A)** — NUNCA tom comercial agressivo ("ultima oportunidade!!", "vagas se esgotando!!" sem prova)
- **VE-12** — NUNCA dado/numero falso
- **VE-02** — NUNCA manipulacao emocional ofensiva (medo extremo, vergonha, culpa)

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — confirma publico+dor+oferta antes
- **2.3 Producao** — aplica voz + paleta de gatilhos
- **2.4 Compliance** — R3 OAB (A) ou CONAR (B)
