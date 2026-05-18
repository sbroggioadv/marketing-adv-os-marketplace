---
name: marketing-diretoria-criativa-marketing
description: >
  DIRETORIA CRIATIVA MARKETING — Skill orquestradora dos 4 gates da Diretoria. Roda R1 (Brief) -> R2 (Copy) -> R3 (Compliance) -> R4 (Performance) em sequencia em UMA peca, com short-circuit se R3 BLOQUEIA. Veredito consolidado: APROVADA / REVISAR / BLOQUEADA. Para peca passando R1-R4 completo, emite Selo Diretoria Criativa + plano de publicacao. Use quando o operador disser audita peca completa, Diretoria Criativa, R1 R2 R3 R4, validar peca antes de publicar, rodar todos gates, audit completo de peca.
---

# DIRETORIA CRIATIVA MARKETING

> Skill Tier 3 (Diretoria Criativa — Orquestradora). Roda R1->R2->R3->R4 em sequencia.

## OBJETIVO

Executar os 4 gates da Diretoria Criativa em UMA chamada, retornando veredito consolidado: APROVADA / REVISAR / BLOQUEADA. Substitui rodar `diretoria-r1-brief`, `diretoria-r2-copy`, etc separadamente — orquestracao automatica.

## PRE-REQUISITOS

- Workspace configurado + Track definido
- Peca completa (briefing + copy + arte se houver + link destino se aplicavel)

## FLUXO

### 1. Coletar peca

> "Vou rodar Diretoria Criativa COMPLETA (R1+R2+R3+R4). Cole:
> - Briefing (publico, dor, KPI, canal, formato)
> - Copy completo
> - Path da arte (se aplicavel)
> - Link de destino + UTM (se aplicavel)
> - Metrica primaria + threshold (se ja decidiu)"

### 2. Executar em sequencia

```
EXECUTANDO DIRETORIA CRIATIVA COMPLETA:

GATE R1 — BRIEF...
   Acionando skill: diretoria-r1-brief
   [aguarda resultado]
   Resultado: <APROVADO | FALHA>
   Se FALHA: PARAR. Reformular briefing antes.
   Se APROVADO: prosseguir.

GATE R2 — COPY...
   Acionando skill: diretoria-r2-copy
   [aguarda resultado]
   Resultado: <APROVADO | REVISAR | FALHA CRITICA>
   Se FALHA CRITICA: PARAR. Reescrever copy.
   Se REVISAR: ajustes pontuais OK pra prosseguir mas marcar.
   Se APROVADO: prosseguir.

GATE R3 — COMPLIANCE...
   Acionando skill: diretoria-r3-compliance
   [aguarda resultado]
   Resultado: <APROVADO | BLOQUEIO ABSOLUTO>
   Se BLOQUEIO: PARAR. Peca NAO sobe. Reformular.
   Se APROVADO: prosseguir.

GATE R4 — PERFORMANCE...
   Acionando skill: diretoria-r4-performance
   [aguarda resultado]
   Resultado: <APROVADO | AVISO DE RISCO>
   Se AVISO: peca pode subir mas com risco mensurabilidade.

VEREDITO FINAL: <APROVADA | REVISAR ANTES | BLOQUEADA>
```

### 3. Veredito consolidado

```
================================================================
DIRETORIA CRIATIVA — VEREDITO CONSOLIDADO
================================================================

Peca: <nome/slug>
Track: <A | B>
Data audit: <timestamp>
Compliance ativo: <OAB Prov. 205/2021 | CONAR + LGPD>

R1 BRIEF:        [APROVADO | FALHA: itens X, Y]
R2 COPY:         [APROVADO | REVISAR: trechos X, Y | FALHA: motivo]
R3 COMPLIANCE:   [APROVADO | BLOQUEIO: VE-XX em trecho "..."]
R4 PERFORMANCE:  [APROVADO | AVISO: itens ausentes X, Y]

----------------------------------------------------------------
DECISAO: APROVADA / REVISAR / BLOQUEADA
----------------------------------------------------------------

Se APROVADA:
- Selo Diretoria Criativa concedido
- Peca pronta para publicar
- Recomendacao de horario: <baseado em canal + publico>
- Plano de monitoramento: <KPI + threshold + ciclo de iteracao>

Se REVISAR:
- Lista de ajustes pendentes
- Pos-ajustes: rodar `diretoria-criativa-marketing` de novo

Se BLOQUEADA:
- Motivo: <violacoes especificas>
- Reformulacao sugerida: <texto especifico>
- NAO publicar sob nenhuma circunstancia
```

### 4. Registrar em integrations.json

```json
{
  "diretoria_criativa": {
    "audits_history": [
      {
        "peca_slug": "...",
        "audit_at": "...",
        "track": "A",
        "r1_status": "APROVADO",
        "r2_status": "APROVADO",
        "r3_status": "APROVADO",
        "r4_status": "AVISO_UTM_AUSENTE",
        "veredito_final": "APROVADA_COM_AVISO",
        "selo_concedido": true
      }
    ]
  }
}
```

### 5. Emitir Selo Diretoria Criativa

Se APROVADA: gerar bloco de Selo (texto + ID auditavel) que o operador pode anexar em registro interno:

```
+-----------------------------------------------+
|  SELO DIRETORIA CRIATIVA MARKETING-ADV-OS     |
|  Peca: <slug>                                 |
|  Track: <A|B>                                 |
|  Auditoria: <timestamp UTC>                   |
|  Status: APROVADA                             |
|  Hash: <sha256 do veredito>                   |
|  Compliance: <OAB|CONAR>                      |
+-----------------------------------------------+
```

## OUTPUT

Veredito consolidado dos 4 gates + decisao final + (se aprovado) selo + registro auditavel.

## VEDACOES ESPECIFICAS

- **NUNCA pular gate** — ordem R1->R2->R3->R4 obrigatoria
- **R3 BLOQUEIO = stop:** nao prosseguir mesmo se operador pressionar
- **Selo so para APROVADA pura** (sem REVISAR) — APROVADA COM AVISO recebe selo mas com nota de risco

## PROTOCOLOS ACIONADOS

- **2.1, 2.2, 2.3, 2.4, 2.5** — todos os 5 protocolos sao avaliados aqui
