---
name: marketing-slides-pptx
description: >
  MARKETING SLIDES PPTX — Gera apresentacao comercial multi-slide em PPTX (10-30 slides) consumindo paleta + tipografia + voz do MEMORY. Aplicavel a pitch B2B (apresentar servico a cliente), proposta comercial, webinar slides, palestra, treinamento. Estrutura calibrada por tipo: pitch (problema-solucao-prova-oferta-call), proposta (escopo-cronograma-investimento), webinar (gancho-conteudo-pitch-Q&A). Consome arte-engine.py em modo multi-slide. Use quando o operador disser apresentacao comercial, pitch deck, slides de proposta, slides de webinar, slides de palestra, PPTX comercial.
---

# MARKETING SLIDES PPTX

> Skill Tier 2 (Executor — Producao). Apresentacao comercial multi-slide PPTX.

## OBJETIVO

Produzir apresentacao PPTX de 10-30 slides com tipografia + paleta + voz da marca aplicadas, calibrada ao tipo (pitch / proposta / webinar / palestra / treinamento). Output: arquivo unico PPTX editavel no PowerPoint / Keynote / LibreOffice / Canva (via import).

## PRE-REQUISITOS

1. Workspace + MEMORY configurado
2. Tokens gerados
3. python-pptx instalado (`pip3 install python-pptx`) — fallback HTML se faltar
4. Conteudo/copy da apresentacao definido (operador fornece estrutura + texto de cada slide)

## FLUXO

### 1. Briefing

> "Vou gerar apresentacao PPTX. Confirme:
> - Tipo: (a) pitch B2B / (b) proposta comercial / (c) webinar / (d) palestra / (e) treinamento / (f) custom
> - Numero de slides: 10 / 15 / 20 / 30
> - Titulo da apresentacao
> - Aspect ratio: 16:9 widescreen (default 1920x1080) / 4:3 classico (1280x960) / 1:1 social
> - Output: `<cwd>/marketing/MARKETING/Slides/<slug>/apresentacao.pptx`"

### 2. Estrutura padrao por tipo

**Pitch B2B (15-20 slides):**
1. Capa (titulo + cliente)
2. Quem somos (1-2 slides)
3. Problema do cliente (2-3 slides)
4. Nossa solucao (3-4 slides)
5. Prova (cases, dados, autoridade — 2-3 slides)
6. Como funciona (metodologia — 2-3 slides)
7. Investimento (1 slide)
8. Proximos passos / CTA (1 slide)
9. Thank you / contato (1 slide)

**Proposta comercial (12-18 slides):**
1. Capa
2. Contexto (problema/oportunidade do cliente)
3. Objetivo da proposta
4. Escopo detalhado (3-5 slides)
5. Metodologia
6. Cronograma
7. Equipe envolvida
8. Investimento + condicoes
9. Garantia / SLA
10. Cases relacionados
11. Proximos passos
12. Thank you

**Webinar (20-30 slides):**
1. Capa + boas-vindas (1-2 slides)
2. Quem sou eu (1 slide rapido)
3. O que voce vai aprender (agenda do webinar)
4. Bloco 1: Hook + tese (3-5 slides)
5. Bloco 2: Desenvolvimento (5-10 slides)
6. Bloco 3: Pratica / framework (5-8 slides)
7. Pitch suave (2-3 slides)
8. CTA + bonus se inscrever agora (1-2 slides)
9. Q&A (1 slide com "perguntas?")
10. Thank you (1 slide)

**Palestra (15-25 slides):**
- Sem pitch comercial
- Estrutura: hook + 3 atos + sintese + Q&A
- Foco em autoridade, nao em conversao

### 3. Aspect ratio + canvas

Mapear pra arte-engine:
- 16:9 widescreen: canvas 1920x1080 — slides padrao
- 4:3 classico: canvas 1280x960 — projetores antigos, ZOOM
- 1:1 social: canvas 1080x1080 — LinkedIn carousel longo (max 10 slides)

### 4. Renderizar slides

Atualmente o `arte-engine.py` gera 1 slide por chamada. Para multi-slide:

**Opcao A (atual):** gerar N PPTX e mergir via python-pptx
**Opcao B (futura):** flag `--multi-slide` no engine recebendo JSON com array

Implementacao atual (loop por slide):

```bash
# Slide 1 (capa)
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/arte-engine.py \\
  --template instagram.feed_square \\
  --texto "<titulo>" --subtexto "<cliente>" \\
  --tokens <tokens.json> \\
  --output <cwd>/.../slide-01.pptx

# Slides 2-N: loop com texto + template apropriado por slide
# ...

# Merge final via python-pptx:
python3 -c "
from pptx import Presentation
import sys
files = sys.argv[1:-1]
master = Presentation(files[0])
for f in files[1:]:
    p = Presentation(f)
    for slide in p.slides:
        # copia layout + shapes
        ...
master.save(sys.argv[-1])
" slide-01.pptx slide-02.pptx ... apresentacao.pptx
```

### 5. Output esperado

```
OK Apresentacao PPTX gerada.

LOCALIZACAO: <cwd>/marketing/MARKETING/Slides/<slug>/apresentacao.pptx
SLIDES: <N>
TAMANHO: <X> MB
ASPECT RATIO: <16:9 / 4:3 / 1:1>

EDITAVEL EM: PowerPoint, Keynote, LibreOffice, Canva (via import)

CHECKLIST DE REVISAO:
- [ ] Capa com titulo + cliente (se pitch B2B)
- [ ] Paleta aplicada consistentemente
- [ ] Tipografia hierarquica respeitada (titulos vs corpo)
- [ ] Cada slide com UMA ideia central
- [ ] Densidade textual razoavel (max 6 linhas por slide)
- [ ] CTA claro (se pitch/proposta/webinar)
- [ ] Disclaimer no ultimo slide (Track A obrigatorio)

PROXIMOS PASSOS:
- Abrir: `open <path>`
- Ajustar timing e transicoes manualmente (engine nao gera animacoes)
- Importar no Canva pra ajustes finais visuais
- Exportar como PDF para envio: PowerPoint -> Export -> PDF
- Subir em Google Slides para colaboracao em equipe
```

### 6. Notas tecnicas para slides comerciais

**Densidade textual:**
- Capa: 3-5 palavras (titulo) + 1 linha contexto
- Slides de conteudo: max 6 linhas (regra 6x6: max 6 bullets, max 6 palavras por bullet)
- Slides de dado: 1 numero gigante + 1 frase de contexto
- Slides de transicao: 1 frase forte centralizada

**Cores:**
- Background slide: neutral_light OU primary
- Texto: neutral_dark (sobre neutral_light) OU neutral_light (sobre primary)
- Destaques: accent SEMPRE (titulos de secao, numeros gigantes, CTAs)

**Tipografia:**
- Titulos: primary (do MEMORY)
- Corpo: secondary
- Numero gigante: primary BOLD 96-128pt
- Caption/footer: secondary 12-14pt

### 7. Diretoria Criativa R2 + R3 + R4

R2: titulo + corpo + CTA presentes; 1 ideia por slide; voz consistente.
R3:
- Track A: slide de oferta NAO promete resultado processual (VE-04); disclaimer OAB no rodape
- Track B: dados verificaveis (VE-12); parceria paga declarada se aplicavel (VE-13)
- Universal: VE-01 (sem superlativo); VE-14 (se IA-generated em area sensivel, declarar)
R4: CTA singular + proximo passo claro no slide final.

## OUTPUT

Apresentacao PPTX completa + checklist + proximos passos.

## VEDACOES ESPECIFICAS

- **Densidade textual excessiva** (>6 linhas/slide): plateia para de ler — usar speaker notes em vez
- **Slide so com imagem sem alt-text:** quebra acessibilidade e SEO se PDF gerado
- **VE-04 (Track A):** apresentacoes comerciais NAO podem prometer resultado processual
- **NUNCA mais de 30 slides** em pitch B2B — plateia perde atencao
- **NUNCA fonte abaixo de 18pt** em texto de corpo — ilegivel em projetor

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — tipo + numero + aspect ratio
- **2.3 Producao** — tokens + voz consumidos
- **2.4 Compliance** — disclaimer + VEs
- **2.5 Mensuracao** — pitch B2B: medir taxa de conversao em proposta; webinar: medir conversao em compra
