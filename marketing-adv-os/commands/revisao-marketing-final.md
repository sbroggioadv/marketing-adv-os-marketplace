---
description: Roda a Diretoria Criativa R1-R4 completa em uma peca pronta. Auditoria de Brief, Copy, Compliance (OAB/CONAR/LGPD conforme track) e Performance. Bloqueia publicacao em falha de R3 (Compliance).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
argument-hint: [caminho da peca a auditar]
---

Voce foi acionado por `/revisao-marketing-final` do plugin Marketing-Adv-OS.

Argumento: `$ARGUMENTS` (caminho do arquivo ou descricao da peca)

## PROTOCOLO

1. Acionar `marketing-master` para carregar contexto (track + voz + paleta)
2. Identificar peca em `$ARGUMENTS`:
   - Se path -> ler arquivo
   - Se descricao -> pedir a peca em texto ou path
3. Acionar `marketing-diretoria-criativa-marketing` (orquestra os 4 gates)
4. Rodar gates em sequencia:
   - **R1 — Brief:** publico nomeado? dor explicita? KPI? canal? formato? -> falha = perguntar
   - **R2 — Copy:** hook? voz? gatilho? clareza? CTA singular? -> falha = revisao copy
   - **R3 — Compliance:** checklist condicional ao track. Track A: VE-04, VE-05, VE-06, VE-07, VE-15 (OAB Provimento 205). Track B: VE-10, VE-12, VE-13 (CONAR). Ambos: VE-08, VE-09 (LGPD) + VE-01, VE-02, VE-03, VE-11, VE-14 -> falha = BLOQUEIO ABSOLUTO + reformulacao
   - **R4 — Performance:** gancho mensuravel? UTM? metrica primaria? threshold? plano A/B? -> falha = aviso de risco (nao bloqueia)
5. Entregar veredito estruturado:

```
DIRETORIA CRIATIVA — VEREDITO

R1 Brief:       [APROVADO | FALHA — itens X, Y]
R2 Copy:        [APROVADO | FALHA — itens X, Y]
R3 Compliance:  [APROVADO | BLOQUEIO ABSOLUTO — VE-XX violada em trecho "..."]
R4 Performance: [APROVADO | AVISO — falta UTM no link]

DECISAO: [LIBERAR | REVISAR | BLOQUEAR]
```

**Skills:** marketing-master + marketing-diretoria-criativa-marketing + marketing-diretoria-r1-brief + marketing-diretoria-r2-copy + marketing-diretoria-r3-compliance + diretoria-r4-performance
