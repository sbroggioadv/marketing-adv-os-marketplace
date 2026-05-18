#!/usr/bin/env python3
"""
ebook-engine.py — Converte Markdown estruturado em PDF profissional aplicando
paleta + tipografia da marca do tokens.json.

Engine primario: WeasyPrint (CSS3 completo, layout profissional)
Fallback: pandoc (CLI nativa, mais ubiquo mas menos controle de design)
Ultimo fallback: HTML standalone (operador converte manual via browser print)

Pipeline:
1. Le manuscript.md + tokens.json
2. Renderiza Markdown -> HTML aplicando classes CSS calibradas pra impressao
3. Aplica CSS print-media (margens A4, hifenizacao, page-break, numeracao)
4. Converte HTML -> PDF via WeasyPrint OU pandoc

Uso:
    python3 ebook-engine.py --input manuscript.md \\
        --tokens ./marketing/design-tokens/tokens.json \\
        --output ebook.pdf \\
        --titulo "Titulo do Ebook" --autor "Autor" --capa cover.png

    python3 ebook-engine.py --check-deps

Deps: weasyprint OU pandoc + markdown (stdlib-friendly + pip).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional


# ============================================================
# Verificacao de deps
# ============================================================

def check_deps() -> dict:
    deps = {}
    try:
        import weasyprint  # noqa: F401
        deps['weasyprint'] = True
    except ImportError:
        deps['weasyprint'] = False
    try:
        import markdown  # noqa: F401
        deps['markdown'] = True
    except ImportError:
        deps['markdown'] = False
    # pandoc CLI (binario externo)
    try:
        r = subprocess.run(['pandoc', '--version'], capture_output=True, timeout=5)
        deps['pandoc'] = r.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        deps['pandoc'] = False
    return deps


def print_deps_status(deps: dict) -> None:
    print("Dependencias detectadas:", file=sys.stderr)
    for name, ok in deps.items():
        marker = "OK" if ok else "FALTANDO"
        print(f"  [{marker}] {name}", file=sys.stderr)
    if not deps['weasyprint'] and not deps['pandoc']:
        print("\nNenhum engine de PDF disponivel. Instale uma:", file=sys.stderr)
        print("  WeasyPrint (preferido): pip3 install weasyprint markdown", file=sys.stderr)
        print("  Pandoc (alternativo, requer LaTeX): brew install pandoc basictex", file=sys.stderr)


# ============================================================
# Carregar tokens
# ============================================================

def load_tokens(tokens_path: Path) -> dict:
    if not tokens_path.exists():
        raise FileNotFoundError(f"tokens.json nao encontrado em {tokens_path}")
    return json.loads(tokens_path.read_text(encoding="utf-8"))


# ============================================================
# Gerar CSS de impressao
# ============================================================

def build_print_css(tokens: dict, titulo: str, autor: str) -> str:
    """Gera CSS print-media calibrado para impressao A4."""
    palette = tokens.get('palette', {})
    typo = tokens.get('typography', {})
    primary_color = palette.get('primary', '#2C2C2C')
    secondary_color = palette.get('secondary', '#888888')
    accent_color = palette.get('accent', '#B8860B')
    n_dark = palette.get('neutral_dark', '#1A1A1A')
    n_light = palette.get('neutral_light', '#FAFAFA')
    font_primary = typo.get('primary', 'Georgia, serif')
    font_secondary = typo.get('secondary', 'Helvetica, sans-serif')
    font_primary_fb = typo.get('primary_fallback', 'serif')
    font_secondary_fb = typo.get('secondary_fallback', 'sans-serif')
    google_fonts_url = typo.get('google_fonts_url', '')

    fonts_import = f"@import url('{google_fonts_url}');" if google_fonts_url else ""

    return f"""{fonts_import}

@page {{
  size: A4;
  margin: 25mm 22mm 28mm 22mm;
  @bottom-center {{
    content: counter(page);
    color: {n_dark};
    font-family: '{font_secondary}', {font_secondary_fb};
    font-size: 9pt;
  }}
  @top-right {{
    content: "{titulo}";
    color: {secondary_color};
    font-family: '{font_secondary}', {font_secondary_fb};
    font-size: 8pt;
    font-style: italic;
  }}
}}

@page :first {{
  margin: 0;
  @bottom-center {{ content: none; }}
  @top-right {{ content: none; }}
}}

body {{
  font-family: '{font_secondary}', {font_secondary_fb};
  font-size: 11pt;
  line-height: 1.65;
  color: {n_dark};
  hyphens: auto;
  text-align: justify;
}}

h1, h2, h3, h4, h5, h6 {{
  font-family: '{font_primary}', {font_primary_fb};
  color: {primary_color};
  page-break-after: avoid;
  text-align: left;
}}

h1 {{
  font-size: 24pt;
  font-weight: 700;
  margin-top: 32pt;
  margin-bottom: 16pt;
  page-break-before: always;
  border-bottom: 2pt solid {accent_color};
  padding-bottom: 8pt;
}}

h2 {{
  font-size: 16pt;
  font-weight: 600;
  margin-top: 24pt;
  margin-bottom: 12pt;
}}

h3 {{
  font-size: 13pt;
  font-weight: 500;
  margin-top: 18pt;
  margin-bottom: 8pt;
  color: {accent_color};
}}

p {{ margin: 0 0 10pt 0; }}

blockquote {{
  border-left: 3pt solid {accent_color};
  padding-left: 12pt;
  margin: 16pt 0;
  font-style: italic;
  color: {primary_color};
}}

code, pre {{
  font-family: 'Menlo', 'Courier New', monospace;
  font-size: 10pt;
  background: {n_light};
  color: {n_dark};
  border-radius: 3pt;
}}
code {{ padding: 1pt 4pt; }}
pre {{ padding: 8pt; overflow-x: auto; }}

a {{ color: {accent_color}; text-decoration: none; }}

table {{
  border-collapse: collapse;
  width: 100%;
  margin: 12pt 0;
  font-size: 10pt;
}}
th, td {{
  border: 0.5pt solid {secondary_color};
  padding: 6pt 8pt;
  text-align: left;
}}
th {{
  background: {n_light};
  color: {primary_color};
  font-weight: 600;
}}

ul, ol {{ margin: 8pt 0; padding-left: 22pt; }}
li {{ margin: 4pt 0; }}

hr {{
  border: none;
  border-top: 0.5pt solid {secondary_color};
  margin: 18pt 0;
}}

.capa {{
  page-break-after: always;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  background: {primary_color};
  color: {n_light};
  padding: 40pt;
}}
.capa h1 {{
  font-size: 36pt;
  border: none;
  color: {n_light};
  margin: 16pt 0;
}}
.capa .autor {{
  font-family: '{font_secondary}', {font_secondary_fb};
  font-size: 14pt;
  color: {accent_color};
  margin-top: 24pt;
}}

.sumario {{
  page-break-after: always;
}}
.sumario h2 {{ border-bottom: 1pt solid {primary_color}; padding-bottom: 6pt; }}
.sumario ul {{ list-style: none; padding-left: 0; }}
.sumario li {{ padding: 4pt 0; border-bottom: 0.3pt dotted {secondary_color}; }}
"""


# ============================================================
# Markdown -> HTML
# ============================================================

def markdown_to_html(md_text: str, titulo: str, autor: str, css: str, capa_path: Optional[Path]) -> str:
    """Converte MD em HTML estruturado com capa + sumario + corpo."""
    try:
        import markdown as md_lib
    except ImportError:
        # Fallback: conversao minima sem markdown package
        body_html = _minimal_md_to_html(md_text)
    else:
        body_html = md_lib.markdown(
            md_text,
            extensions=['extra', 'codehilite', 'tables', 'toc'],
        )

    # Construir capa
    capa_img = f'<img src="{capa_path}" alt="capa" style="max-width: 200pt; margin-bottom: 24pt;">' if capa_path else ''
    capa_html = f"""
<div class="capa">
  {capa_img}
  <h1>{_escape_html(titulo)}</h1>
  <div class="autor">por {_escape_html(autor)}</div>
</div>
"""

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{_escape_html(titulo)}</title>
<style>{css}</style>
</head>
<body>
{capa_html}
{body_html}
</body>
</html>
"""


def _minimal_md_to_html(md: str) -> str:
    """Fallback minimo se markdown package nao instalado. Cobre h1-h3, p, listas."""
    lines = md.split('\n')
    out = []
    in_list = False
    for line in lines:
        s = line.rstrip()
        if not s:
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('')
            continue
        if s.startswith('# '):
            if in_list: out.append('</ul>'); in_list = False
            out.append(f'<h1>{_escape_html(s[2:])}</h1>')
        elif s.startswith('## '):
            if in_list: out.append('</ul>'); in_list = False
            out.append(f'<h2>{_escape_html(s[3:])}</h2>')
        elif s.startswith('### '):
            if in_list: out.append('</ul>'); in_list = False
            out.append(f'<h3>{_escape_html(s[4:])}</h3>')
        elif s.startswith('- '):
            if not in_list:
                out.append('<ul>')
                in_list = True
            out.append(f'<li>{_escape_html(s[2:])}</li>')
        else:
            if in_list: out.append('</ul>'); in_list = False
            out.append(f'<p>{_escape_html(s)}</p>')
    if in_list:
        out.append('</ul>')
    return '\n'.join(out)


def _escape_html(s: str) -> str:
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ============================================================
# Render HTML -> PDF
# ============================================================

def render_pdf_weasyprint(html: str, output_path: Path) -> Path:
    try:
        from weasyprint import HTML
    except ImportError:
        raise RuntimeError("weasyprint nao instalado")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html).write_pdf(str(output_path))
    return output_path


def render_pdf_pandoc(md_path: Path, output_path: Path, titulo: str, autor: str) -> Path:
    """Fallback via pandoc CLI."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        'pandoc', str(md_path), '-o', str(output_path),
        '--pdf-engine=xelatex',
        '-V', f'title={titulo}',
        '-V', f'author={autor}',
        '-V', 'geometry:margin=22mm',
        '--toc',
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        raise RuntimeError(f"pandoc falhou: {result.stderr}")
    return output_path


def render_html_fallback(html: str, output_path: Path) -> Path:
    """Ultimo fallback: HTML standalone — operador imprime via browser."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding='utf-8')
    return output_path


# ============================================================
# CLI
# ============================================================

def main() -> int:
    parser = argparse.ArgumentParser(description="Converte Markdown estruturado em PDF profissional.")
    parser.add_argument("--input", help="Arquivo manuscript.md")
    parser.add_argument("--tokens", help="Caminho para tokens.json")
    parser.add_argument("--output", help="Caminho do PDF de saida")
    parser.add_argument("--titulo", default="Ebook", help="Titulo do ebook (vai pra capa + header)")
    parser.add_argument("--autor", default="", help="Autor (vai pra capa)")
    parser.add_argument("--capa", default=None, help="Path opcional pra imagem de capa (PNG)")
    parser.add_argument("--engine", choices=["weasyprint", "pandoc", "html"], default=None,
                        help="Forcar engine especifico. Default: auto-detect (weasyprint > pandoc > html)")
    parser.add_argument("--check-deps", action="store_true", help="So checa dependencias e sai")
    args = parser.parse_args()

    deps = check_deps()
    if args.check_deps:
        print_deps_status(deps)
        return 0

    missing = [a for a in ("input", "tokens", "output") if not getattr(args, a)]
    if missing:
        parser.error(f"Argumentos obrigatorios: {', '.join('--' + m for m in missing)}")
        return 2

    md_path = Path(args.input).resolve()
    tokens_path = Path(args.tokens).resolve()
    output_path = Path(args.output).resolve()
    capa_path = Path(args.capa).resolve() if args.capa else None

    if not md_path.exists():
        print(f"Erro: {md_path} nao encontrado", file=sys.stderr)
        return 1

    tokens = load_tokens(tokens_path)
    md_text = md_path.read_text(encoding='utf-8')
    css = build_print_css(tokens, args.titulo, args.autor)

    # Decidir engine
    engine = args.engine
    if not engine:
        if deps['weasyprint']:
            engine = 'weasyprint'
        elif deps['pandoc']:
            engine = 'pandoc'
        else:
            engine = 'html'

    try:
        if engine == 'weasyprint':
            html = markdown_to_html(md_text, args.titulo, args.autor, css, capa_path)
            render_pdf_weasyprint(html, output_path)
            print(f"PDF gerado via WeasyPrint: {output_path}")
        elif engine == 'pandoc':
            if output_path.suffix != '.pdf':
                output_path = output_path.with_suffix('.pdf')
            render_pdf_pandoc(md_path, output_path, args.titulo, args.autor)
            print(f"PDF gerado via pandoc: {output_path}")
        else:  # html
            html = markdown_to_html(md_text, args.titulo, args.autor, css, capa_path)
            html_path = output_path.with_suffix('.html')
            render_html_fallback(html, html_path)
            print(f"HTML standalone gerado: {html_path}", file=sys.stderr)
            print("Para gerar PDF: abra no Chrome -> Imprimir -> Salvar como PDF", file=sys.stderr)
    except Exception as e:
        print(f"Erro no engine {engine}: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
