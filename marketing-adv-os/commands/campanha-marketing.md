---
description: Orquestra campanha completa de marketing (briefing -> estrategia -> copy -> arte -> distribuicao -> mensuracao). Pipeline Tier 1 + Tier 2 + Diretoria Criativa R1-R4 completa.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
argument-hint: [tema da campanha]
---

Voce foi acionado por `/campanha-marketing` do plugin Marketing-Adv-OS.

Argumento: `$ARGUMENTS`

## PROTOCOLO

1. Acionar `marketing-master`
2. **Tier 1 — Estado-maior:**
   - marketing-briefing-de-campanha (estrutura o briefing)
   - marketing-descoberta-de-publico (refina publico-alvo)
   - marketing-diagnostico-de-canal (decide canais)
3. **Tier 2 — Executores:**
   - Copy: marketing-copy-* (conforme canal)
   - Arte: marketing-arte-* (conforme formato)
   - Producao: marketing-landing-page / ebook / slides (se aplicavel)
4. **Transversais:** estilo-de-marca + visual-de-marketing
5. **Diretoria Criativa R1-R4 completa** (R1 Brief -> R2 Copy -> R3 Compliance -> R4 Performance)
6. **Mensuracao:** definir metrica primaria + threshold + plano A/B

Entrega:
- Briefing estruturado em `<cwd>/marketing/MARKETING/Campanhas/<slug>/briefing.md`
- Copy aprovado em `<cwd>/marketing/MARKETING/Campanhas/<slug>/copy/`
- Artes em `<cwd>/marketing/MARKETING/Campanhas/<slug>/artes/` (PNG + PPTX)
- LP (se aplicavel) em `<cwd>/marketing/MARKETING/Landing-Pages/<slug>/`
- Plano de mensuracao em `<cwd>/marketing/MARKETING/Campanhas/<slug>/mensuracao.md`

**Skills:** marketing-master + cadeia Tier 1 + Tier 2 + diretoria-criativa-marketing
