#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Marketing-Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-diretoria`, `--quick`, `/diretoria off`.
3. Detecta GATILHO MARKETING via keywords (3 niveis):
   - Gatilho 1: prompt contem palavra "marketing" / "campanha" / "copy" / "anuncio" (CI)
   - Gatilho 2: keywords fortes do dominio (paleta, branding, posicionamento, landing page, etc.)
   - Gatilho 3: comandos `/start-marketing`, `/marketing-master`, etc.
4. Se gatilho dispara:
   - Verifica se `marketing/cowork-state.json` existe no path atual
   - SIM: injeta protocolo R1-R4 da Diretoria Criativa + aponta para skill `marketing-master`
   - NAO: sugere `/start-marketing` ao usuario (mas nao bloqueia)
5. Se ha bypass: reafirma em stdout que o bypass foi aceito (transparencia).
6. Se nao eh tarefa de marketing: silencio (exit 0 sem output).

Tambem respeita state.json: se `diretoria_criativa.enabled = false`, nunca injeta R1-R4.

Stdlib only.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

import importlib.util
spec = importlib.util.spec_from_file_location("hook_utils", PLUGIN_ROOT / "scripts" / "hook-utils.py")
hook_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook_utils)


# Gatilho 1: palavras genericas de marketing (alto recall)
TRIGGER_MARKETING = [
    r"\bmarketing\b",
    r"\bbranding\b",
    r"\bcampanha\b",
    r"\bcampanhas\b",
    r"\bcopy\b",
    r"\bcopywriting\b",
    r"\banuncio\b", r"\banúncio\b",
    r"\banuncios\b", r"\banúncios\b",
    r"\bpost\s+pra(\s+|s)\b",  # "post pro insta", "posts pras redes"
    r"\bcarrossel\b",
    r"\breels\b",
    r"\bstor(y|ies)\b",
    r"\bmidia\s+social\b", r"\bmídia\s+social\b",
    r"\bredes\s+sociais\b",
]

# Gatilho 2: keywords fortes do dominio marketing
DOMAIN_KEYWORDS = [
    # Estrategia e posicionamento
    r"\bposicionamento\b", r"\bpersona\b", r"\bpublico[- ]alvo\b",
    r"\bp[uú]blico[- ]alvo\b",
    r"\bfunil\s+de\s+vendas\b", r"\bbriefing\b", r"\bbrief\b",
    r"\bproposta\s+de\s+valor\b",
    # Identidade visual
    r"\bpaleta\s+de\s+cores\b", r"\bpaleta\b",
    r"\bidentidade\s+visual\b", r"\bbrand\s+guidelines\b",
    r"\btipografia\b", r"\bfontes?\b", r"\blogotipo\b",
    r"\btokens\s+de\s+design\b", r"\bdesign\s+tokens\b",
    r"\bmoodboard\b", r"\bmood\s+board\b",
    # Producao de conteudo
    r"\bheadline\b", r"\bhook\b", r"\bCTA\b", r"\bcall[- ]to[- ]action\b",
    r"\bgancho\b", r"\bchamada\b",
    r"\bconteudo\s+pra\b", r"\bconteúdo\s+pra\b",
    r"\blegenda\b", r"\bcaption\b",
    # Formatos
    r"\blanding\s+page\b", r"\bLP\b", r"\bone[- ]pager\b",
    r"\bebook\b", r"\be[- ]book\b",
    r"\bslide(s)?\b", r"\bpitch\s+deck\b",
    r"\bapresentacao\b", r"\bapresentação\b",
    # Email / Lead
    r"\blead\s+magnet\b", r"\blead(s)?\b",
    r"\bemail\s+marketing\b", r"\bnewsletter\b",
    r"\bsequencia\s+de\s+email\b", r"\bsequência\s+de\s+email\b",
    r"\bbroadcast\b",
    # Plataformas
    r"\bInstagram\b", r"\bFacebook\b", r"\bLinkedIn\b",
    r"\bTikTok\b", r"\bYouTube\b", r"\bMeta\s+Ads\b",
    r"\bGoogle\s+Ads\b", r"\bTikTok\s+Ads\b",
    # Mensuracao
    r"\bUTM\b", r"\bpixel\b", r"\bconversao\b", r"\bconversão\b",
    r"\bKPI\b", r"\bCAC\b", r"\bLTV\b", r"\bROAS\b", r"\bCTR\b",
    # Track A juridico
    r"\bmarketing\s+jur[ií]dico\b",
    r"\bprovimento\s+205\b",
    r"\bOAB\s+publicidade\b",
    # Compliance
    r"\bCONAR\b", r"\bLGPD\b",
    # Acoes
    r"\bostentar\b", r"\bdivulgar\b",
    r"\bcaptar\s+lead\b", r"\blanc(ar|amento)\b", r"\blançamento\b",
    r"\bestrategia\s+de\s+conteudo\b", r"\bestratégia\s+de\s+conteúdo\b",
    r"\beditorial\b", r"\bcalendario\s+editorial\b", r"\bcalendário\s+editorial\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-marketing",
    "/marketing-master",
    "/copy-marketing",
    "/campanha-marketing",
    "/conteudo-marketing",
    "/revisao-marketing-final",
    "/status-marketing",
    "/diretoria-criativa-marketing",
]

BYPASS_TOKENS = [
    "--no-diretoria",
    "--no-corte",   # legado/compat
    "--quick",
    "/diretoria off",
    "/diretoria-off",
]


def _load_input() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _matches_any(text: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def _is_marketing(prompt: str) -> bool:
    """Detecta se o prompt e do dominio marketing (gatilhos 1, 2 ou 3)."""
    if _matches_any(prompt, TRIGGER_MARKETING):
        return True
    if _matches_any(prompt, DOMAIN_KEYWORDS):
        return True
    low = prompt.lower()
    for cmd in PLUGIN_COMMANDS:
        if cmd.lower() in low:
            return True
    return False


def _has_bypass(prompt: str) -> str | None:
    low = prompt.lower()
    for token in BYPASS_TOKENS:
        if token in low:
            return token
    return None


def _has_marketing_state(cowork: Path | None) -> bool:
    """Verifica se existe `marketing/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "marketing" / "cowork-state.json").exists()


def _diretoria_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica diretoria_criativa.enabled. Default true."""
    if cowork is None:
        return True
    sf = cowork / "marketing" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("diretoria_criativa", {}).get("enabled", True))
    except Exception:
        return True


def _get_track(cowork: Path | None) -> str:
    """Le state.json e retorna track (A ou B). Default A."""
    if cowork is None:
        return "A"
    sf = cowork / "marketing" / "cowork-state.json"
    if not sf.exists():
        return "A"
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return str(state.get("track", "A")).upper()
    except Exception:
        return "A"


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env MARKETING_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("MARKETING_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "marketing" / "cowork-state.json").exists():
            return p
    return hook_utils.find_cowork(Path.cwd())


def main() -> int:
    payload = _load_input()
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    cowork = _resolve_cowork()
    bypass = _has_bypass(prompt)
    is_mkt = _is_marketing(prompt)

    # Caso 1: bypass explicito
    if bypass and is_mkt:
        sys.stdout.write(
            f"[marketing-adv-os] Bypass detectado ({bypass}). "
            "Peca sera entregue SEM validacao da Diretoria Criativa (R1-R4). "
            "Use por sua conta e risco — VEs aplicam mesmo em bypass.\n"
        )
        return 0

    # Caso 2: tarefa de marketing + plugin configurado
    if is_mkt and _has_marketing_state(cowork):
        track = _get_track(cowork)
        compliance = (
            "OAB Provimento 205/2021 (Track A — VE-04, VE-05, VE-06, VE-07, VE-15)"
            if track == "A"
            else "CONAR + LGPD (Track B — VE-10, VE-12, VE-13, VE-08, VE-09)"
        )
        if not _diretoria_enabled(cowork):
            sys.stdout.write(
                "[marketing-adv-os] Demanda de marketing detectada. "
                "Diretoria Criativa DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: marketing-master.\n"
            )
        else:
            sys.stdout.write(
                f"[marketing-adv-os] Demanda de marketing detectada. Plugin ativo (Track {track}).\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `marketing-master` (Tier 0 — sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (VEs / Protocolos / Identidade / Skills)\n"
                "3. Consultar MEMORY: paleta + voz + publico + oferta\n"
                "4. Verificar 15 Vedacoes Editoriais — sempre VE-01 a VE-03, VE-08 a VE-14 + condicional ao track\n"
                f"5. Compliance ativo: {compliance}\n"
                "6. Antes de entregar peca publicavel: Diretoria Criativa R1->R2->R3->R4\n"
                "\n"
                "Bypass disponivel: `--no-diretoria`, `--quick`, `/diretoria off`.\n"
            )
        return 0

    # Caso 3: tarefa de marketing mas plugin NAO configurado
    if is_mkt and not _has_marketing_state(cowork):
        sys.stdout.write(
            "[marketing-adv-os] Detectei demanda de marketing, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-marketing para configurar (~7 min).\n"
            "Vou perguntar seu track (A=advogado, B=empresario), paleta de cores, voz da marca, "
            "publico-alvo e oferta. A partir disso TODA producao consulta essa identidade automaticamente.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Default: nao e tarefa de marketing — silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
