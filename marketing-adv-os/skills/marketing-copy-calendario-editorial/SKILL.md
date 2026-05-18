---
name: marketing-copy-calendario-editorial
description: >
  MARKETING COPY CALENDARIO EDITORIAL — Gera calendario editorial mensal (30 dias) ou trimestral, distribuindo formatos (educativo, autoridade, depoimento, oferta, bastidores, pergunta-engajamento) em proporcao otimizada por canal (Instagram, LinkedIn, Facebook). Calcula frequencia, gera dia-a-dia com tema sugerido + formato + objetivo + KPI primario. Bloqueia excesso de posts-oferta (regra: max 20% do calendario em peca de venda direta — alem disso vira saturacao). Use quando o operador disser calendario editorial, planejamento mensal, conteudo do mes, 30 posts, ritmo de publicacao, cronograma de conteudo.
---

# MARKETING COPY CALENDARIO EDITORIAL

> Skill Tier 2 (Executor — Copy). Calendario editorial mensal ou trimestral.

## OBJETIVO

Gerar calendario editorial estruturado com mix balanceado de formatos para 30 dias (ou 90), respeitando proporcoes que sustentam autoridade SEM saturar o publico com vendas. Output em tabela markdown + arquivo CSV opcional.

## PRE-REQUISITOS

Workspace + MEMORY com publico+oferta+canais. Operador define periodo + canais.

## FLUXO

### 1. Briefing

> "Vou montar calendario editorial pra:
> - Periodo: 30 dias (mes) / 90 dias (trimestre)
> - Canais primarios (multi-select): Instagram, LinkedIn, Facebook, X, blog, email
> - Frequencia desejada por canal (sugestao: IG 3-4x/sem, LinkedIn 2-3x/sem, Facebook 2x/sem, X diario, blog 1x/sem, email 1x/sem)
> - Tema central do periodo (opcional — ex: 'Lancamento curso X', 'Mes da decadencia tributaria', 'Black Friday')
> - Datas comerciais relevantes (Dia das Maes, Black Friday, fim de exercicio, etc)"

### 2. Calcular volume

Frequencia padrao por canal por semana:
- Instagram: 3 (1 carrossel educativo + 1 reels + 1 stories series)
- LinkedIn: 2 (1 post autoridade + 1 reflexao)
- Facebook: 2 (replica do IG + 1 dialogo de grupo se aplicavel)
- X: 5 (3 tweets soltos + 2 threads)
- Blog: 1 (artigo longo)
- Email: 1 (newsletter ou nutricao)

Em 30 dias (~4 semanas): IG=12, LinkedIn=8, FB=8, X=20, blog=4, email=4. Total ~56 pecas.

### 3. Aplicar mix de formatos (regra 5-3-1-1)

Para cada 10 pecas:
- **5 EDUCATIVAS** — ensinar, dar valor, gerar salvamento (sem venda)
- **3 AUTORIDADE / OPINIAO** — tese tecnica, dado verificavel, posicionamento
- **1 BASTIDOR / HUMANIZACAO** — equipe, processo, momento real
- **1 OFERTA / VENDA DIRETA** — CTA explicito de conversao

**Regra critica:** posts-oferta nunca passam de 20% do calendario. Em 30 dias com 56 pecas, max ~11 sao de oferta. Acima disso = saturacao + queda de alcance organico.

Adicionar 1 post-depoimento por semana (se ha cases disponiveis com autorizacao).

### 4. Gerar tabela dia-a-dia

```
=== CALENDARIO EDITORIAL — [MES/PERIODO] ===

| Data        | Dia | Canal     | Formato        | Tema sugerido                      | KPI primario | Status   |
|-------------|-----|-----------|----------------|------------------------------------|--------------|----------|
| 2026-06-01  | Seg | LinkedIn  | Autoridade     | [Tema do briefing aplicado]        | Comentarios  | A fazer  |
| 2026-06-02  | Ter | Instagram | Carrossel-edu  | [Tema relacionado a dor #1]        | Salvamentos  | A fazer  |
| 2026-06-03  | Qua | X         | Thread         | [Tema com dado verificavel]        | Retweets     | A fazer  |
| 2026-06-04  | Qui | Instagram | Reels          | [Hook visual + 1 dica em 30s]      | View-rate    | A fazer  |
| 2026-06-05  | Sex | Email     | Newsletter     | [Sintese da semana + valor]        | Open-rate    | A fazer  |
| 2026-06-06  | Sab | -         | (descanso)     | -                                  | -            | -        |
| 2026-06-07  | Dom | Stories   | Bastidor       | [Equipe/processo/momento real]     | Replies      | A fazer  |
...
```

### 5. Distribuir datas comerciais

Marcar datas relevantes destacadas:
- Black Friday / Cyber Monday
- Dia da[s] Mae[s]/Pai[s] (se relevante ao nicho)
- Fim de exercicio fiscal (Track A tributario)
- Dia do Advogado (Track A)
- Datas do nicho especifico

Calendario adapta peca pra surfar a data (com cuidado: nao oportunismo barato).

### 6. Tema central (se houver)

Se operador definiu tema central ("lancamento curso X"):
- Semana 1: pre-aquecimento (educativo + autoridade sobre o problema que o curso resolve)
- Semana 2: pre-lancamento (depoimentos + bastidor de quem ja foi)
- Semana 3: lancamento (oferta + ancoragem + urgencia REAL)
- Semana 4: pos-lancamento (depoimento de novos alunos + autoridade reafirmando)

### 7. Output adicional

Gerar:
- Tabela markdown completa (acima)
- CSV opcional para import em Google Sheets / Notion / Trello
- Resumo executivo:
  ```
  RESUMO:
  - Total de pecas: 56
  - Distribuicao: 28 educativas (50%), 17 autoridade (30%), 6 bastidor (11%), 5 oferta (9%)
  - KPIs primarios variam por formato — definidos por linha
  - Datas comerciais marcadas: [lista]
  ```

### 8. Diretoria Criativa R2 + R3 + R4

R2: mix balanceado, voz consistente entre pecas.
R3: distribuicao respeita 20% max de oferta direta (VE-05 track A).
R4: cada formato tem KPI primario definido (R4 = mensurabilidade ja embutida).

## OUTPUT

Calendario tabular + CSV opcional + resumo executivo + veredito Diretoria.

## VEDACOES ESPECIFICAS

- **VE-05 (Track A)** — Mais de 20% de oferta direta = mercantilizacao. BLOQUEIA.
- **VE-04 (Track A)** — Pecas de venda direta NAO podem prometer resultado processual
- **VE-13** — Pecas com parceria paga: marcadas explicitamente no calendario
- Datas comerciais oportunistas (Track A) = atencao — nao toda data se converte em conteudo

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — periodo + canais + tema + datas
- **2.3 Producao** — mix balanceado evita saturacao
- **2.5 Mensuracao** — KPI primario definido peca-por-peca
