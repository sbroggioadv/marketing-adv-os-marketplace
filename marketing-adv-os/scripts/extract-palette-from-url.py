#!/usr/bin/env python3
"""
extract-palette-from-url.py — Extrai 5 cores dominantes de uma URL via screenshot
ou imagem direta.

Cobre a pendencia da skill `marketing-brand-palette` (modo 3: importar de URL).

Estrategia:
1. URL aponta para imagem direta (jpg/png/webp) -> baixa direto via requests
2. URL aponta para pagina HTML -> tenta encontrar og:image / hero image OU
   sugere que operador forneca screenshot manual
3. Aplica k-means simples nas pixels para identificar 5 cores dominantes
4. Mapeia: primary (mais frequente em area grande), secondary, accent (mais saturada),
   neutral_dark (mais escura), neutral_light (mais clara)
5. Output JSON estruturado pronto pra alimentar marketing-brand-palette

Deps: Pillow + requests (ambos opt). Sem k-means externo — implementacao stdlib via
contagem ponderada de cores + ranking.

Uso:
    python3 extract-palette-from-url.py <url>
    python3 extract-palette-from-url.py file:///path/to/screenshot.png
    python3 extract-palette-from-url.py --check-deps
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


def check_deps() -> dict:
    deps = {}
    try:
        import PIL  # noqa: F401
        deps['pillow'] = True
    except ImportError:
        deps['pillow'] = False
    try:
        import requests  # noqa: F401
        deps['requests'] = True
    except ImportError:
        deps['requests'] = False
    return deps


def download_image(url: str, timeout: int = 15) -> bytes:
    """Baixa imagem direta. Lanca excecao se URL nao for imagem."""
    try:
        import requests
    except ImportError:
        raise RuntimeError("requests nao instalado. `pip3 install requests`")

    parsed = urlparse(url)
    if parsed.scheme == "file":
        return Path(parsed.path).read_bytes()

    # Verificar Content-Type
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; marketing-adv-os palette extractor)"
    }
    r = requests.get(url, timeout=timeout, headers=headers, stream=True)
    r.raise_for_status()
    content_type = r.headers.get("Content-Type", "").lower()
    if content_type.startswith("image/"):
        return r.content
    # HTML: tentar encontrar og:image
    if "html" in content_type or "text" in content_type:
        html = r.text
        og = _find_og_image(html)
        if og:
            # absolutizar URL relativa
            if og.startswith("//"):
                og = parsed.scheme + ":" + og
            elif og.startswith("/"):
                og = f"{parsed.scheme}://{parsed.netloc}{og}"
            elif not og.startswith("http"):
                og = f"{parsed.scheme}://{parsed.netloc}/{og.lstrip('/')}"
            r2 = requests.get(og, timeout=timeout, headers=headers, stream=True)
            r2.raise_for_status()
            return r2.content
        raise ValueError(
            f"URL {url} retornou HTML sem og:image detectavel. "
            f"Tire screenshot do site e use file:///path/to/screenshot.png como URL."
        )
    raise ValueError(f"Content-Type inesperado: {content_type!r}")


def _find_og_image(html: str) -> str | None:
    """Regex simples pra encontrar og:image em meta tag. Stdlib only."""
    import re
    patterns = [
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
        r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)["\']',
    ]
    for p in patterns:
        m = re.search(p, html, re.IGNORECASE)
        if m:
            return m.group(1)
    return None


def extract_palette_pillow(image_bytes: bytes, n_colors: int = 5) -> dict:
    """
    Usa Pillow para extrair cores dominantes.
    Returns: dict com primary, secondary, accent, neutral_dark, neutral_light.
    """
    try:
        from PIL import Image
    except ImportError:
        raise RuntimeError("Pillow nao instalado. `pip3 install pillow`")

    img = Image.open(_bytes_to_buffer(image_bytes))
    img = img.convert('RGB')
    # Reduzir para acelerar — mantem ratio
    img.thumbnail((400, 400))

    # Quantizar para palette de N*4 cores e pegar top N por frequencia
    quantized = img.quantize(colors=n_colors * 4)
    palette = quantized.getpalette()
    color_counts = Counter(quantized.getdata())

    # Top N cores por frequencia
    top_colors = []
    for color_idx, count in color_counts.most_common(n_colors * 4):
        rgb = (palette[color_idx * 3], palette[color_idx * 3 + 1], palette[color_idx * 3 + 2])
        top_colors.append({'rgb': rgb, 'count': count})

    # Filtrar muito proximas (deduplicacao)
    unique = _deduplicate_colors(top_colors, threshold=30)[:n_colors]

    # Mapear: primary (mais frequente), secondary, accent (mais saturada), neutrals
    primary = unique[0]['rgb']
    secondary = unique[1]['rgb'] if len(unique) > 1 else primary
    accent = max(unique, key=lambda c: _saturation(c['rgb']))['rgb']
    neutral_dark = min(unique, key=lambda c: _luminance(c['rgb']))['rgb']
    neutral_light = max(unique, key=lambda c: _luminance(c['rgb']))['rgb']

    return {
        'primary': _rgb_to_hex(primary),
        'secondary': _rgb_to_hex(secondary),
        'accent': _rgb_to_hex(accent),
        'neutral_dark': _rgb_to_hex(neutral_dark),
        'neutral_light': _rgb_to_hex(neutral_light),
        'source': 'extracted-from-url',
        'top_5_by_frequency': [_rgb_to_hex(c['rgb']) for c in unique[:5]],
    }


def _bytes_to_buffer(b: bytes):
    import io
    return io.BytesIO(b)


def _rgb_to_hex(rgb: tuple) -> str:
    return '#{:02X}{:02X}{:02X}'.format(*rgb)


def _luminance(rgb: tuple) -> float:
    """Luminancia relativa (WCAG)."""
    r, g, b = (c / 255.0 for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _saturation(rgb: tuple) -> float:
    r, g, b = (c / 255.0 for c in rgb)
    mx = max(r, g, b)
    mn = min(r, g, b)
    if mx == 0:
        return 0
    return (mx - mn) / mx


def _deduplicate_colors(colors: list, threshold: int = 30) -> list:
    """Remove cores muito proximas (distancia euclidiana RGB < threshold)."""
    if not colors:
        return []
    result = [colors[0]]
    for c in colors[1:]:
        is_dup = False
        for r in result:
            dist = sum((c['rgb'][i] - r['rgb'][i]) ** 2 for i in range(3)) ** 0.5
            if dist < threshold:
                is_dup = True
                break
        if not is_dup:
            result.append(c)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrai paleta de 5 cores dominantes de URL.")
    parser.add_argument("url", nargs="?", help="URL da imagem OU file:///path/to/img")
    parser.add_argument("--n", type=int, default=5, help="Numero de cores na paleta (default 5)")
    parser.add_argument("--check-deps", action="store_true", help="So checa deps e sai")
    parser.add_argument("--output", default=None, help="Salvar JSON em arquivo (senao stdout)")
    args = parser.parse_args()

    deps = check_deps()
    if args.check_deps:
        for name, ok in deps.items():
            print(f"[{('OK' if ok else 'FALTANDO')}] {name}")
        if not all(deps.values()):
            print("Instalar: pip3 install pillow requests", file=sys.stderr)
        return 0

    if not args.url:
        parser.print_help()
        return 1

    if not deps['pillow']:
        print("Erro: Pillow necessario. Instale: pip3 install pillow", file=sys.stderr)
        return 1
    if not deps['requests'] and not args.url.startswith('file:'):
        print("Erro: requests necessario para URLs http. Instale: pip3 install requests", file=sys.stderr)
        return 1

    try:
        image_bytes = download_image(args.url)
        palette = extract_palette_pillow(image_bytes, n_colors=args.n)
        palette['source_url'] = args.url
    except Exception as e:
        print(f"Erro ao processar URL {args.url}: {e}", file=sys.stderr)
        return 1

    output_json = json.dumps(palette, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(output_json, encoding='utf-8')
        print(f"Paleta salva em {args.output}", file=sys.stderr)
    else:
        print(output_json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
