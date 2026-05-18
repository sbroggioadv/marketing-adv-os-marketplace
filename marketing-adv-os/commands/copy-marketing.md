---
description: Producao isolada de copy (headline, anuncio, post, email, CTA, storytelling). Aciona a skill de copy especifica conforme o canal/formato. Aplica voz da marca + Diretoria Criativa R2 (Copy) e R3 (Compliance).
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
argument-hint: [tipo: headline | ads | post | email | cta | storytelling]
---

Voce foi acionado por `/copy-marketing` do plugin Marketing-Adv-OS.

Argumento: `$ARGUMENTS`

## PROTOCOLO

1. Acionar `marketing-master` para carregar contexto (identidade + voz + Vedacoes)
2. Identificar tipo de copy a partir de `$ARGUMENTS` (ou perguntar)
3. Acionar skill Tier 2 especifica:
   - `headline` -> marketing-copy-headline-aida / landing-page / ab-test / converter-fraca-forte
   - `ads` -> marketing-copy-ads-meta / google-search / storytelling / remarketing
   - `post` -> marketing-copy-post-educativo-ig / autoridade / depoimento / calendario
   - `email` -> marketing-copy-email-welcome / lancamento / upsell
   - `cta` -> marketing-copy-cta
   - `storytelling` -> marketing-copy-storytelling-jornada-heroi / case-success
4. Consultar `<cwd>/marketing/MEMORY.md` para voz + paleta + publico
5. Rodar Diretoria Criativa R2 (Copy) + R3 (Compliance — track-aware)
6. Entregar copy aprovado

**Vedacoes aplicaveis:** VE-01 (sem promessa falsa), VE-02 (sem manipulacao ofensiva), VE-11 (sem apelo abusivo). Track A: + VE-04, VE-05. Track B: + VE-12, VE-13.

**Skills:** marketing-master + marketing-copy-* (especifica)
