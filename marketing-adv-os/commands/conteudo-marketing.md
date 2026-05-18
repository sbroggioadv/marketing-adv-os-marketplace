---
description: Producao isolada de conteudo editorial (post, carrossel, stories, reels, artigo, video script). Sem objetivo de venda direta — foco em autoridade, educacao, engajamento.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
argument-hint: [formato: post | carrossel | stories | reels | artigo | youtube]
---

Voce foi acionado por `/conteudo-marketing` do plugin Marketing-Adv-OS.

Argumento: `$ARGUMENTS`

## PROTOCOLO

1. Acionar `marketing-master`
2. Identificar formato a partir de `$ARGUMENTS` (ou perguntar)
3. Acionar skill Tier 2 especifica:
   - `post` -> marketing-copy-post-educativo-ig / autoridade / depoimento
   - `carrossel` -> marketing-carrossel-pptx (com copy estruturado em 7 slides)
   - `stories` -> marketing-stories-pptx (5 telas com CTA)
   - `reels` -> marketing-reels-roteiro (script ate 60s com hook + corpo + CTA)
   - `artigo` -> marketing-copy-post-autoridade + escrita longa
   - `youtube` -> marketing-reels-roteiro (versao longa)
4. Consultar MEMORY (voz + paleta + publico + canais)
5. Rodar Diretoria Criativa R2 (Copy) + R3 (Compliance)
6. Entregar em `<cwd>/marketing/MARKETING/Conteudo/<slug>/`

**Diferenca de `/campanha-marketing`:** conteudo nao tem objetivo de venda direta — KPI tipicamente e alcance, salvamento, comentario, encaminhamento, autoridade. CTA mais sutil (link em bio, "me segue", "comenta").

**Skills:** marketing-master + marketing-copy-post-* / marketing-carrossel-pptx / marketing-stories-pptx / marketing-reels-roteiro
