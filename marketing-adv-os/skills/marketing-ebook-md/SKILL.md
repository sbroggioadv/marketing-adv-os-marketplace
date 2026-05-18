---
name: marketing-ebook-md
description: >
  MARKETING EBOOK MD — Gera ebook em Markdown estruturado (5-10 capitulos) com capa + sumario + introducao + capitulos + conclusao + CTA + bio do autor + disclaimer. Estrutura calibrada para conversao em PDF profissional posterior (marketing-ebook-pdf). Consome voz + publico + oferta do MEMORY. Track A: cuidado VE-04 (ebook nao promete resultado processual generalizado) e VE-15 (cases reais com autorizacao escrita). Output em `<cwd>/marketing/MARKETING/Ebooks/<slug>/manuscript.md`. Use quando o operador disser gerar ebook, escrever ebook, manuscrito de ebook, ebook em markdown, conteudo de ebook, ebook como lead magnet.
---

# MARKETING EBOOK MD

> Skill Tier 2 (Executor — Producao). Gera manuscrito de ebook em Markdown.

## OBJETIVO

Produzir manuscrito Markdown estruturado e completo (10000-25000 palavras) com narrativa otimizada para conversao em PDF profissional. Aplica voz da marca + insights do publico + framework problema-solucao em cada capitulo.

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Voz + publico definidos no MEMORY
3. Operador fornece: tema central + numero de capitulos (5-10) + objetivo do ebook (autoridade / lead magnet / produto de entrada)

## FLUXO

### 1. Briefing

> "Vou gerar ebook em Markdown. Confirme:
> - Titulo do ebook: [...]
> - Subtitulo (opcional): [...]
> - Tema central: [1-2 frases descrevendo o que o ebook ensina]
> - Numero de capitulos: 5 / 7 / 10
> - Objetivo principal: (a) autoridade no nicho / (b) lead magnet (captura email) / (c) produto de entrada paga (R$ 27-97)
> - Tom: serio-tecnico / didatico-acessivel / provocativo-narrativo
> - Tamanho alvo: curto (10k palavras) / medio (15-20k) / longo (25k+)
> - Output: `<cwd>/marketing/MARKETING/Ebooks/<slug>/manuscript.md`"

### 2. Estrutura padrao

Para CADA capitulo, framework:

```
## Capitulo N — [Titulo declarativo, nao academico]

### O problema
[Apresenta a dor especifica que o capitulo enderecara — 2-3 paragrafos.
Use estatistica/dado verificado se houver.
Sem hiperbole. Especifico ao publico-alvo do MEMORY.]

### A virada
[Apresenta a perspectiva nova/contraintuitiva — 3-5 paragrafos.
Voz: assertiva mas humanizada.
Pode incluir 1 case (com autorizacao se Track A).
Pode incluir 1 quote de autoridade.]

### Como aplicar
[Passos praticos, frameworks, checklists — 4-6 paragrafos.
Numerar ou bullets quando houver sequencia.
Incluir 1 exemplo concreto OU 1 mini-case.]

**Resumo do capitulo:**
- [Takeaway 1 — frase curta]
- [Takeaway 2]
- [Takeaway 3]
```

### 3. Capa + Sumario + Intro + Conclusao + Bio + Disclaimer

Alem dos capitulos:

**Capa** (1 pagina):
- Titulo grande + subtitulo + autor
- Sem texto longo — capa e visual

**Sumario** (1 pagina):
- Gerado automaticamente pelo ebook-engine (apos render markdown)

**Introducao** (2-4 paginas):
- Para QUEM o ebook foi escrito
- O que o leitor vai aprender (resumo dos capitulos)
- Por que esse ebook em vez de outros
- Promessa final: o que muda na vida do leitor apos ler

**Conclusao** (2-3 paginas):
- Sintese dos capitulos
- Mensagem central reforcada
- Convite ao proximo passo (link, agendamento, comunidade)

**Bio do autor** (1 pagina):
- 2-3 paragrafos sobre quem voce e
- Track A: OAB + escritorio + areas de atuacao (sem captacao agressiva — VE-06)
- Track B: empresa + nicho + experiencia
- Contatos profissionais (LinkedIn, site)

**Disclaimer legal** (1 pagina):
- LGPD: declaracao de uso de dados do ebook (se ha formulario de download)
- OAB (Track A): "Este material e informativo, nao constitui orientacao juridica individualizada. Cada caso deve ser analisado especificamente."
- Direitos autorais: "© <ano> <marca>. Todos os direitos reservados."
- (Opcional) Licenca Creative Commons se aplicavel

### 4. Aplicar voz da marca

Consultar `<cwd>/marketing/MEMORY.md` secao `## Voz da Marca`:
- Aplicar perfil + intensidade ao tom de cada capitulo
- Usar expressoes assinatura quando se encaixar naturalmente
- Evitar termos a evitar (substituir por sinonimos)

### 5. Renderizar manuscrito

Copiar `<plugin_root>/templates/ebook/manuscript-base.md` -> `<cwd>/marketing/MARKETING/Ebooks/<slug>/manuscript.md` substituindo placeholders Mustache + preenchendo capitulos.

### 6. Gerar TODO de capa visual

```
TODO — CAPA VISUAL DO EBOOK:

Para gerar a capa, rode:
- `marketing-arte-png` com template `imagem-unica`
- Canvas: 1200x1800 (proporcao A4 para impressao)
- Texto principal: <titulo>
- Subtexto: por <autor>
- Output: `<cwd>/marketing/MARKETING/Ebooks/<slug>/cover.png`

Apos: a capa sera incluida automaticamente quando rodar `marketing-ebook-pdf`.
```

### 7. Diretoria Criativa R2 + R3

R2: tom consistente entre capitulos + estrutura clara.
R3:
- Track A: VE-04 (sem prometer resultado processual), VE-15 (cases com autorizacao)
- Track B: VE-12 (sem dado/case falso)
- Universal: VE-01 (sem superlativo), VE-14 (declarar se IA-generated em area sensivel)

## OUTPUT

Arquivo `manuscript.md` com 5-10 capitulos + paginas auxiliares + TODO de capa + veredito Diretoria.

## VEDACOES ESPECIFICAS

- **VE-04 (Track A):** Ebook NAO pode prometer resultado processual generalizado ("voce vai ganhar suas acoes apos ler este ebook")
- **VE-15 (Track A):** Cases com autorizacao escrita do cliente OU personas representativas declaradas
- **VE-01:** Sem "o unico ebook que voce precisa", "100% dos casos resolvidos"
- **VE-14:** Se inteiramente IA-generated em area sensivel (juridico/medico), declarar
- **NUNCA encher pagina com filler** — concisao > volume; ebook de 10k palavras forte > 50k palavras dispersas

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — titulo + tema + capitulos + objetivo
- **2.2 Pesquisa** — se cita lei/julgado/estatistica: validar antes (Track A: criticamente)
- **2.3 Producao** — voz aplicada + framework por capitulo
- **2.4 Compliance** — VEs prioritarias VE-04, VE-15 (A); VE-12 (B)
- **2.5 Mensuracao** — se lead magnet: definir taxa-alvo de conversao do download
