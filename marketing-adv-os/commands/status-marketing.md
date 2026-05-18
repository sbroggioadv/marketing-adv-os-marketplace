---
description: Diagnostico do workspace de marketing. Mostra estado do plugin, marca configurada, track ativo, paleta registrada, skills ativas, ultimas pecas produzidas e pendencias.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: nenhum
---

Voce foi acionado por `/status-marketing` do plugin Marketing-Adv-OS.

## PROTOCOLO

1. Ler `<cwd>/marketing/cowork-state.json` (se nao existe -> "Plugin nao configurado neste workspace. Rode /start-marketing")
2. Ler `<cwd>/marketing/MEMORY.md`
3. Listar `<cwd>/marketing/MARKETING/` recursivamente
4. Verificar env `MARKETING_PERSONA` e `MARKETING_COWORK_PATH`
5. Verificar audit do plugin (se possivel)

## RELATORIO

```
PLUGIN MARKETING-ADV-OS — STATUS DO WORKSPACE

CONFIGURACAO
- Marca:        <nome>
- Track:        <A=Advogado/Escritorio | B=Empresario/Criador>
- Cidade:       <cidade>/<UF>
- Versao state: <versao>
- Ultima att.:  <data>

IDENTIDADE VISUAL
- Paleta primaria:   <hex> (<nome do tom>)
- Paleta secundaria: <hex>
- Paleta accent:     <hex>
- Tipografia:        <primary> / <secondary>

VOZ DA MARCA
- Perfil:        <perfil>
- Intensidade:   <X>/10
- Expressoes:    <N> aceitas, <M> proibidas

PUBLICO-ALVO
- Persona:       <descricao>
- Dor principal: <descricao>
- Canais:        <lista>

OFERTA
- Servico/produto: <nome>
- Ticket:          <faixa>
- Modalidade:      <presencial/online/hibrido>

GOVERNANCE
- Diretoria Criativa R1-R4: <ATIVA/DESATIVADA>
- Vedacoes Editoriais:      15 ativas (universais + track-aware)
- Compliance:               <OAB Provimento 205 | CONAR + LGPD>

PRODUCAO RECENTE
- Campanhas:      <N>
- Artes (PNG):    <N>
- Artes (PPTX):   <N>
- Landing pages:  <N>
- Ebooks:         <N>
- Slides:         <N>

PENDENCIAS
- <lista de pendencias se houver>

PROXIMAS ACOES SUGERIDAS
- <sugestoes baseadas no estado>
```

**Skills:** sem skills externas — diagnostico puro
