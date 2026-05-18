---
name: marketing-diretoria-r3-compliance
description: >
  DIRETORIA R3 COMPLIANCE — Terceiro gate da Diretoria Criativa, condicional ao track. Track A: roda checklist OAB Provimento 205/2021 + Codigo de Etica + LGPD (VE-04, 05, 06, 07, 15 + VE-08, 09). Track B: roda checklist CONAR + LGPD (VE-10, 12, 13 + VE-08, 09). Universal para ambos: VE-01, VE-02, VE-03, VE-11, VE-14. Falha = BLOQUEIO ABSOLUTO, reformulacao obrigatoria, peca NAO sobe. Use quando o operador disser audita compliance, R3 da peca, conferir OAB, validar CONAR, terceira etapa Diretoria, peca passa OAB.
---

# DIRETORIA R3 COMPLIANCE

> Skill Tier 3 (Diretoria Criativa — Gate 3). Compliance track-aware. **BLOQUEIO ABSOLUTO em falha.**

## OBJETIVO

Validar conformidade legal e etica da peca antes de publicar. Falha aqui NAO e revisao — e bloqueio. Reformulacao obrigatoria. Track A: violacao pode gerar denuncia OAB. Track B: violacao pode gerar reclamacao CONAR ou multa LGPD.

## PRE-REQUISITOS

- R2 (Copy) aprovado
- Track definido em `cowork-state.json` (A ou B)
- Peca completa (copy + arte se houver)

## FLUXO

### 1. Carregar track + checklist condicional

```
Lendo cowork-state.json...
Track: {{A|B}}

Carregando checklist condicional:

Track A (Advogado/Escritorio):
- OAB Provimento 205/2021
- Codigo de Etica e Disciplina
- LGPD (universal)
- VEs aplicaveis: VE-04, 05, 06, 07, 15 (track A) + VE-01, 02, 03, 08, 09, 11, 14 (universais)

Track B (Empresario/Criador):
- CONAR (Codigo Brasileiro de Auto-Regulamentacao Publicitaria)
- LGPD (universal)
- CDC (Codigo de Defesa do Consumidor)
- VEs aplicaveis: VE-10, 12, 13 (track B) + VE-01, 02, 03, 08, 09, 11, 14 (universais)
```

### 2A. Checklist Track A — OAB Provimento 205/2021

```
TRACK A — OAB:

[VE-04] Promessa de resultado processual
- Buscar pattern: "voce vai ganhar", "garanto a acao", "vamos vencer", "100% de aprovacao no INSS"
- Buscar implicito: "recupere o que e seu", "seu direito esta garantido" (pode ser promessa velada)
- Status: APROVADO | VIOLACAO (trecho: "...")

[VE-05] Mercantilizacao da advocacia
- Buscar: tom comercial agressivo, "ULTIMA CHANCE!!!", "Compre agora", urgencia fabricada, preco de servico explicito em peca publica
- Status: APROVADO | VIOLACAO

[VE-06] Captacao indevida de clientela
- Buscar: "Ligue ja", "Atendimento imediato", "Atende 24h", "Consulta gratuita whatsapp"
- Buscar: oferta direta de servico em peca informativa (peca informativa NAO promove honorario)
- Status: APROVADO | VIOLACAO

[VE-07] Ofensa a colega/banca
- Buscar: nome de outro advogado/escritorio com tom negativo
- Buscar: "outros advogados NAO sabem", "escritorios que enganam"
- Status: APROVADO | VIOLACAO

[VE-15] Quebra de sigilo profissional
- Se ha case/depoimento: tem autorizacao escrita do cliente?
- Detalhes processuais sensiveis: anonimizados?
- Status: APROVADO | VIOLACAO | NAO_APLICAVEL (sem case na peca)
```

### 2B. Checklist Track B — CONAR + LGPD

```
TRACK B — CONAR + LGPD:

[VE-10] Comparativo desleal
- Compara com concorrente nominado: dado verificavel? imparcial?
- Buscar: "X (concorrente) e ruim porque...", "use Y, nao X"
- Status: APROVADO | VIOLACAO

[VE-12] Propaganda enganosa
- Numeros citados: verificaveis?
- Antes/depois: real ou exagerado?
- Garantia: termos claros?
- Imagem ilustrativa: corresponde ao produto real?
- Status: APROVADO | VIOLACAO

[VE-13] Parceria paga nao declarada
- Se ha parceria/patrocinio: #publi visivel nos primeiros 100 chars (regra IG/FB 2026)?
- Branded content: rotulado?
- Status: APROVADO | VIOLACAO | NAO_APLICAVEL (sem parceria)
```

### 2C. Checklist UNIVERSAL (ambos os tracks)

```
UNIVERSAL:

[VE-01] Promessa falsa ou superlativo sem prova
- "o melhor", "o unico", "100% garantido", "guaranteed"
- Status: APROVADO | VIOLACAO

[VE-02] Manipulacao emocional ofensiva
- Medo extremo, vergonha publica, culpa abusiva
- "voce ainda esta cometendo esse erro?" (com tom acusatorio)
- Status: APROVADO | VIOLACAO

[VE-03] Mistura de escopos
- Servico A vendido como B (consultoria como cura, ebook como aula completa)
- Status: APROVADO | VIOLACAO

[VE-08] Coleta de dados sem base legal LGPD
- Formulario ativo: tem politica de privacidade linkada?
- Opt-in claro (sem checkbox pre-marcada)?
- Status: APROVADO | VIOLACAO | NAO_APLICAVEL (sem coleta)

[VE-09] Opt-out impossivel ou enterrado
- Email/contato continuado: link de descadastro visivel + funcional?
- Status: APROVADO | VIOLACAO | NAO_APLICAVEL (peca unica)

[VE-11] Apelo abusivo a crianca/adolescente
- Peca direcionada a menor de idade?
- Linguagem manipulativa, urgencia falsa, gatilho de FOMO em adolescente?
- Status: APROVADO | VIOLACAO | NAO_APLICAVEL (publico adulto)

[VE-14] Conteudo IA-generated sem declaracao
- Texto longo (ebook, artigo) gerado por IA mas publico assume autoria humana?
- Depoimento sintetico (sem cliente real) sem rotulagem?
- Imagem-pessoa IA-gerada em area sensivel (juridica/medica)?
- Status: APROVADO | VIOLACAO | NAO_APLICAVEL
```

### 3. Veredito FINAL

```
DIRETORIA R3 — COMPLIANCE: <APROVADO | BLOQUEIO ABSOLUTO>

Track: <A | B>
Compliance ativo: <OAB Prov. 205/2021 | CONAR + LGPD>

UNIVERSAL:
[VE-01] OK | VIOLACAO
[VE-02] OK | VIOLACAO
[VE-03] OK | VIOLACAO
[VE-08] OK | VIOLACAO | NAO_APLICAVEL
[VE-09] OK | VIOLACAO | NAO_APLICAVEL
[VE-11] OK | VIOLACAO | NAO_APLICAVEL
[VE-14] OK | VIOLACAO | NAO_APLICAVEL

Track A (se aplicavel):
[VE-04] OK | VIOLACAO
[VE-05] OK | VIOLACAO
[VE-06] OK | VIOLACAO
[VE-07] OK | VIOLACAO
[VE-15] OK | VIOLACAO | NAO_APLICAVEL

Track B (se aplicavel):
[VE-10] OK | VIOLACAO
[VE-12] OK | VIOLACAO
[VE-13] OK | VIOLACAO | NAO_APLICAVEL

DECISAO:
- APROVADO (tudo OK ou NAO_APLICAVEL): prosseguir para R4 (Performance)
- BLOQUEIO ABSOLUTO: peca NAO sobe. Reformular antes de continuar.

[Se BLOQUEIO] VIOLACOES + REFORMULACOES SUGERIDAS:
- VE-XX (linha X): "trecho violado"
  Sugestao: "reformulacao que mantem essencia mas remove violacao"
```

## OUTPUT

Veredito completo + trechos violados + sugestoes de reformulacao + decisao.

## VEDACOES ESPECIFICAS

- **BLOQUEIO ABSOLUTO** em qualquer violacao — sem excecao
- **NUNCA aprovar sob reformulacao que mantem violacao** (apenas suaviza)
- **Track A — VE-04, VE-05, VE-06:** risco de denuncia OAB; auditoria rigorosa
- **VE-13:** parceria paga sem declaracao = multa IG/FB/CONAR

## PROTOCOLOS ACIONADOS

- **2.4 Compliance** — esta skill E o gate central do protocolo
