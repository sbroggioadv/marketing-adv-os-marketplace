---
description: Aciona a Diretoria Criativa R1-R4 de forma isolada (auditoria sem producao). Util para auditar peca de terceiros ou peca antiga antes de re-publicar.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
argument-hint: [path-da-peca | descricao]
---

Voce foi acionado por `/diretoria-criativa-marketing` do plugin Marketing-Adv-OS.

Argumento: `$ARGUMENTS`

## PROTOCOLO

1. Acionar `marketing-master` (contexto da marca + track)
2. Acionar `marketing-diretoria-criativa-marketing` (skill orquestradora dos 4 gates)
3. Rodar gates em sequencia (R1 -> R2 -> R3 -> R4)
4. Entregar veredito estruturado com diagnostico item-a-item

**Diferenca de `/revisao-marketing-final`:**
- `/revisao-marketing-final` -> tipicamente usado APOS producao, antes de publicar (fluxo natural)
- `/diretoria-criativa-marketing` -> auditoria isolada (peca de terceiros, peca antiga, peca recebida)

**Skills:** marketing-master + diretoria-criativa-marketing
