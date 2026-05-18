---
name: marketing-brand-guidelines
description: >
  MARKETING BRAND GUIDELINES — Gera o documento `<cwd>/marketing/BRAND-GUIDELINES.md` consolidado a partir da paleta + voz + tipografia + publico + oferta registrados no MEMORY. Documento exportavel para Notion, Confluence, Google Docs. Inclui regras de uso da paleta, exemplos de aplicacao da voz, mapa de medidas de arte por plataforma e checklists track-aware (OAB para Track A; CONAR+LGPD para Track B). Use quando o operador disser gerar brand guidelines, manual da marca, documento de identidade visual, manual de uso, brandbook, consolidar identidade.
---

# MARKETING BRAND GUIDELINES

> Skill Tier 1 (Estado-maior — Brand). Gera o documento consolidado da identidade da marca.

## OBJETIVO

Consolidar paleta + voz + tipografia + publico + oferta do MEMORY em UM documento exportavel (`BRAND-GUIDELINES.md`) que serve de referencia para:
- Equipe interna (social media, designers, copywriters terceirizados)
- Skills internas do plugin (consulta rapida sem ler MEMORY inteiro)
- Documentacao pro Canva/Notion/Drive

## PRE-REQUISITOS

- Workspace marketing configurado
- Recomendado: paleta + voz + tipografia ja definidas (via `marketing-brand-palette`, `marketing-brand-voice`, `marketing-tipografia`). Se algum estiver vazio, alertar e oferecer rodar antes.

## FLUXO

### 1. Verificar prerequisitos no MEMORY

Ler `<cwd>/marketing/cowork-state.json` campos:
- `identity.palette` (5 cores)
- `identity.voice` (perfil + intensidade + expressoes)
- `identity.typography` (primary + secondary)
- `publico` (persona + dor + canais)
- `oferta` (servico + ticket + modalidade)
- `track` (A ou B)

Se algum campo critico esta vazio: alertar e perguntar:
> "Detectei que voz da marca nao esta definida ainda. Quer rodar `marketing-brand-voice` agora ou prosseguir gerando guideline parcial?"

### 2. Gerar documento

Estrutura do BRAND-GUIDELINES.md:

```markdown
# Brand Guidelines — <MARCA_NOME>

> Documento consolidado da identidade visual e voz da marca.
> Versao: <version> · Atualizado em: <date> · Track: <A|B>

---

## 1. Identidade da Marca
- Nome: <marca>
- Track: <Advogado/Escritorio | Empresario/Criador>
- Cidade: <cidade>/<UF>
- Site / Instagram / LinkedIn

## 2. Publico-alvo
- Persona: <descricao>
- Dor principal: <descricao>
- Canais ativos: <lista>

## 3. Oferta
- Servico/produto: <nome>
- Ticket: <faixa>
- Modalidade: <presencial/online/hibrido>

## 4. Paleta de Cores
### Primaria — <hex> (<nome>)
Uso: cor de marca principal — logos, hero sections, elementos de identidade
### Secundaria — <hex> (<nome>)
Uso: cor de apoio — backgrounds secundarios, divisores
### Accent — <hex> (<nome>)
Uso: CTAs, destaques, links, badges — usar com PARCIMONIA (5-10% da peca)
### Neutro Escuro — <hex>
Uso: texto principal em fundo claro
### Neutro Claro — <hex>
Uso: background principal, separadores claros

### Regras de uso
- CTA SEMPRE usa accent
- Hero usa primary OU secondary (escolher conforme contraste)
- Texto longo: neutro_dark sobre neutro_light (contraste AA garantido)

## 5. Tipografia
### Primaria — <fonte>
Uso: titulos, hero, hierarquia alta
### Secundaria — <fonte>
Uso: corpo de texto, UI

### Hierarquia
- H1: <primary> bold 48-72px
- H2: <primary> semibold 32-40px
- H3: <primary> medium 24-28px
- Body: <secondary> regular 16-18px line-height 1.6
- Caption: <secondary> regular 14px

## 6. Voz da Marca
- Perfil: <perfil>
- Intensidade: <X>/10
- Expressoes assinatura: <lista>
- Termos a EVITAR: <lista>
- Exemplos validados: <lista>

### Regras de voz
- Frase media <= 18 palavras
- Subordinacao maxima 2 niveis
- CTA singular (uma acao primaria)
- Hook nos primeiros 3 segundos (video) ou 7 palavras (escrito)

## 7. Mapa de Medidas — Artes por Plataforma

### Instagram
- Feed quadrado: 1080x1080 px
- Feed vertical: 1080x1350 px
- Stories / Reels capa: 1080x1920 px
- Carrossel: 1080x1080 (max 10 slides)

### Facebook
- Post: 1200x630 px
- Stories: 1080x1920 px
- Capa de pagina: 1640x624 px

### LinkedIn
- Post horizontal: 1200x627 px
- Post quadrado: 1200x1200 px
- Stories (mobile): 1080x1920 px
- Artigo capa: 1200x644 px

### Outros
- Email header: 600x200 px
- LP hero (desktop): 1920x1080 px
- LP hero (mobile): 1080x1920 px

## 8. Compliance — Track <A|B>

### Track A (OAB Provimento 205/2021)
- VE-04: sem promessa de resultado
- VE-05: sem mercantilizacao agressiva
- VE-06: sem captacao indevida
- VE-07: sem ofensa a colegas
- VE-15: sem quebra de sigilo

### Track B (CONAR + LGPD)
- VE-10: sem comparativo desleal
- VE-12: sem propaganda enganosa
- VE-13: declarar parceria paga (#publi)

### Universais
- VE-01: sem promessa falsa
- VE-02: sem manipulacao ofensiva
- VE-08, VE-09: LGPD em coleta
- VE-11: sem apelo abusivo a crianca/adolescente
- VE-14: declarar IA em conteudo de autoria humana

## 9. Diretoria Criativa R1-R4

Toda peca publicavel passa por:
- R1 Brief: publico + dor + KPI + canal + formato
- R2 Copy: hook + voz + gatilho + clareza + CTA singular
- R3 Compliance: checklist track-aware (acima)
- R4 Performance: gancho mensuravel + UTM + metrica + threshold

## 10. Como usar este documento
- Equipe: ler integralmente no onboarding
- Brief de fornecedor externo: colar secoes 4-8
- Checklist de aprovacao: usar secoes 8 e 9
- Atualizacao: re-rodar `marketing-brand-guidelines` apos qualquer mudanca em palette/voice/tipografia

---

**Plugin:** marketing-adv-os v<version> · Gerado em <date>
```

### 3. Salvar

Escrever em `<cwd>/marketing/BRAND-GUIDELINES.md`. Se ja existe: backup automatico em `BRAND-GUIDELINES.md.<timestamp>.bak` antes.

### 4. Confirmar

```
OK BRAND-GUIDELINES.md gerado (versao <X>).

LOCALIZACAO: <cwd>/marketing/BRAND-GUIDELINES.md
TAMANHO: <bytes>
SECOES: 10

PROXIMOS PASSOS:
- Compartilhar com equipe (social media, designers terceirizados)
- Subir para Notion/Confluence/Drive (opcional)
- Atualizar sempre que paleta/voz/tipografia mudar (re-rodar este comando)
```

## OUTPUT ESPERADO

- `<cwd>/marketing/BRAND-GUIDELINES.md` criado/atualizado
- Backup automatico da versao anterior se existia
- Mensagem de confirmacao com localizacao e proximos passos

## VEDACOES ESPECIFICAS

- NUNCA sobrescrever guideline sem backup
- NUNCA gerar guideline sem ler MEMORY atual (paleta/voz/tipografia)
- NUNCA inventar regras nao registradas pelo operador
- NUNCA omitir track-aware section (Track A precisa OAB, Track B precisa CONAR)

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — guideline consolida o briefing
- **2.3 Producao** — guideline serve de input pra produtores externos
