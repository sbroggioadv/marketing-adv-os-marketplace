---
name: marketing-canva-import
description: >
  MARKETING CANVA IMPORT — Integra com MCP Canva oficial Anthropic (https://mcp.canva.com/mcp via OAuth). Importa PPTX gerados localmente (por marketing-arte-pptx, marketing-carrossel-pptx, marketing-slides-pptx) para o workspace Canva do operador. Suporta tambem: editar design existente, buscar templates de marca (brand templates), exportar como PNG/PDF/MP4. Setup via OAuth (claude.ai gerencia token). Use quando o operador disser importar pra canva, mandar pra canva, abrir no canva, exportar do canva, usar brand template canva, integrar canva.
---

# MARKETING CANVA IMPORT

> Skill Tier 2 (Executor — Integracao Opt-in). MCP Canva oficial Anthropic.

## OBJETIVO

Conectar workspace ao Canva via MCP oficial Anthropic e usar para: importar PPTX locais, editar designs existentes, aplicar brand templates, exportar em multiplos formatos. Diferente do Meta Ads (terceiro), Canva e MCP **oficial** e mais simples de configurar.

## PRE-REQUISITOS

1. Workspace marketing configurado
2. Conta Canva ativa (Pro recomendado para brand templates + import PPTX)
3. Login em claude.ai (MCP Canva e gerenciado via claude.ai web)
4. PPTX local pra importar (gerado por marketing-arte-pptx / carrossel / slides)

## FLUXO

### 1. Verificar conexao OAuth

```bash
# Canva MCP e oficial — claude.ai oferece direto
# Verificar disponibilidade
claude mcp list 2>&1 | grep -i canva
```

Se nao conectado:
> "Para conectar Canva (MCP oficial Anthropic):
>
> 1. Acesse claude.ai/settings/connectors
> 2. Buscar 'Canva' na lista de conectores oficiais
> 3. Clicar 'Connect' -> redireciona para login Canva
> 4. Autorizar permissoes: 'design:read', 'design:write', 'asset:upload', 'asset:read'
> 5. Voltar ao Claude Code — MCP fica disponivel automaticamente
>
> CONFIRMACAO: rode `claude mcp list` apos conectar — deve aparecer 'canva'.
>
> ALTERNATIVA: Canva Pro tem 'Bulk create' que importa CSV/Excel — pode ser alternativa em vez de MCP."

### 2. Mapear acoes disponiveis

MCP Canva expoe (tipicamente):

| Acao                        | Tool MCP                                    |
|-----------------------------|---------------------------------------------|
| Importar PPTX               | `mcp__canva__import-design-from-url` ou `upload-asset-from-url` |
| Criar design do zero        | `mcp__canva__generate-design` ou `create-design-from-brand-template` |
| Listar brand templates      | `mcp__canva__search-brand-templates`        |
| Buscar designs existentes   | `mcp__canva__search-designs`                |
| Exportar como PNG/PDF/MP4   | `mcp__canva__export-design`                 |
| Editar design existente     | `mcp__canva__perform-editing-operations`    |
| Gerar conteudo via IA       | `mcp__canva__generate-design` (com prompt)  |
| Folder/asset management     | `mcp__canva__create-folder`, etc            |

### 3. Briefing — qual operacao?

> "O que voce quer fazer com Canva?
> (a) Importar PPTX local (do plugin) pra editar no Canva
> (b) Criar novo design a partir de brand template Canva
> (c) Editar design Canva existente (passar URL/ID)
> (d) Buscar templates de marca disponiveis no meu workspace
> (e) Exportar design Canva como PNG/PDF (download local)
> (f) Gerar design novo via IA Canva (prompt textual)"

### 4A. Importar PPTX

```
PPTX a importar: <cwd>/marketing/MARKETING/Artes/<slug>/peca-01.pptx

Passos:
1. Upload do PPTX como asset:
   mcp__canva__upload-asset-from-url (precisa URL publica) OU
   mcp__canva__create-design-from-candidate (passa arquivo)

2. Canva converte PPTX em design editavel
3. Operador recebe URL do novo design Canva

NOTA: Canva tem limite de 100 MB por upload. PPTX grande (>100 MB) precisa otimizar antes.
```

### 4B. Brand template

```
1. Buscar templates de marca:
   mcp__canva__search-brand-templates --workspace_id=<do operador>

2. Apresentar opcoes:
   - Template A: "IG Feed Post — Brand 2026"
   - Template B: "LinkedIn Post — Brand 2026"
   - ...

3. Operador escolhe template + passa dados (titulo, subtitulo, imagem)

4. Gerar design:
   mcp__canva__create-design-from-brand-template \\
     --template_id=<id> \\
     --variables {"headline": "...", "subhead": "..."}

5. Retorna URL pro design pronto pra editar/exportar.
```

### 4C. Exportar design

```
1. Buscar design por URL/ID:
   mcp__canva__get-design --design_id=<id>

2. Listar formatos de export disponiveis:
   mcp__canva__get-export-formats --design_id=<id>
   # PNG, JPG, PDF, MP4, GIF, etc

3. Exportar:
   mcp__canva__export-design \\
     --design_id=<id> \\
     --format=PNG \\
     --pages=[1,2,3]  # se carrossel multi-slide

4. Receber URL temporaria do arquivo + baixar local:
   curl <url> -o <cwd>/marketing/MARKETING/Artes/<slug>/canva-export.png
```

### 5. Validar deps OAuth

```bash
# Testar conexao
claude mcp test canva
# OU simplesmente perguntar: "Liste meus designs no Canva"
```

### 6. Workflow recomendado completo

```
PLUGIN GERA -> CANVA EDITA -> PLUGIN PUBLICA:

1. plugin gera PPTX local (marketing-arte-pptx ou marketing-carrossel-pptx)
2. marketing-canva-import -> faz upload do PPTX no Canva
3. operador edita visual no Canva (mais fluido que python-pptx pra ajustes finos)
4. marketing-canva-import -> exporta PNG final do Canva
5. marketing-postiz-publish (S6.4) -> publica em redes
```

Workflow alternativo: ja editar tudo no Canva via brand-template (pular passo 1-2).

### 7. Registrar uso em integrations.json

```json
{
  "canva": {
    "status": "connected",
    "mcp_name": "canva",
    "connected_at": "2026-05-17T17:00:00Z",
    "workspace_id_masked": "***456789",
    "permissions": ["design:read", "design:write", "asset:upload", "asset:read"],
    "imports_history": [
      { "pptx_path": "...", "canva_design_url": "...", "imported_at": "..." }
    ]
  }
}
```

## OUTPUT

Conexao validada + acao executada + URL do design + (se aplicavel) arquivo baixado local.

## VEDACOES ESPECIFICAS

- **NUNCA armazenar credenciais OAuth localmente** — claude.ai gerencia
- **NUNCA exportar designs com PII** sem revisao (Canva pode ter dados sensiveis em layers ocultas)
- **VE-13:** Brand template usado com #publi obrigatorio se conteudo for parceria paga
- **PPTX upload max 100 MB** — pre-validar tamanho

## PROTOCOLOS ACIONADOS

- **2.1 Briefing** — qual acao Canva especifica
- **2.3 Producao** — Canva como editor visual final do workflow
- **2.4 Compliance** — Canva-generated com IA precisa declaracao VE-14
