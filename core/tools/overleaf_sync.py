#!/usr/bin/env python3
"""
Overleaf Synchronization Assistant - Sincronização Bidirecional com o Overleaf
Suporta Git nativo do Overleaf (https://git.overleaf.com/6a92242dbaaa2c6b6833bab0)
e exportação/importação de pacote ZIP a partir de article/ e papers/artigo-final/.

Uso:
    py core/tools/overleaf_sync.py --status        # Verifica conexão bidirecional e histórico Git Overleaf
    py core/tools/overleaf_sync.py --zip           # Gera pacote ZIP pronto para o Overleaf
    py core/tools/overleaf_sync.py --git-setup     # Exibe instruções de configuração do remote Overleaf
    py core/tools/overleaf_sync.py --import-zip    # Importa alterações baixadas do Overleaf
"""

import argparse
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ARTICLE_DIR = ROOT_DIR / "article"
PAPER_DIR = ROOT_DIR / "papers" / "artigo-final"
ZIP_OUTPUT = ROOT_DIR / "papers" / "overleaf-export.zip"

EXCLUDE_EXTS = {
    ".aux", ".bbl", ".blg", ".brf", ".fdb_latexmk", ".fls",
    ".lof", ".log", ".lot", ".nav", ".out", ".snm", ".synctex.gz",
    ".toc", ".vrb", ".bcf", ".run.xml", ".pdf"
}


def sanitize_token(text: str) -> str:
    """Remove qualquer token olp_... de saídas de log por segurança."""
    return re.sub(r"olp_[A-Za-z0-9]+@", "***TOKEN_REDACTED***@", text)


def check_overleaf_status():
    """Verifica a conexão bidirecional com o Overleaf via Git e exibe os commits registrados."""
    print(f"[Overleaf Sync] Verificando repositório espelho em: {PAPER_DIR}")
    if not (PAPER_DIR / ".git").exists():
        print("[Aviso] Sub-repositório Git do Overleaf não encontrado localmente.", file=sys.stderr)
        return False

    res_remote = subprocess.run(
        ["git", "-C", str(PAPER_DIR), "remote", "-v"],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    print("\n[Remoto Configurado (Token Sanitizado)]:")
    print(sanitize_token(res_remote.stdout.strip()))

    res_log = subprocess.run(
        ["git", "-C", str(PAPER_DIR), "log", "--all", "-n", "12", "--oneline"],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    print("\n[Histórico de Contribuições Sincronizadas com Overleaf]:")
    print(sanitize_token(res_log.stdout.strip()))
    return True


def create_overleaf_zip():
    source_dir = ARTICLE_DIR if ARTICLE_DIR.exists() else PAPER_DIR
    print(f"\n[Empacotando] Criando arquivo ZIP para o Overleaf a partir de: {source_dir}")

    if not source_dir.exists():
        print(f"[Erro] Diretório {source_dir} não encontrado!", file=sys.stderr)
        return False

    with zipfile.ZipFile(ZIP_OUTPUT, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            if ".git" in root or "refs" in Path(root).parts:
                continue
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in EXCLUDE_EXTS:
                    continue
                arcname = file_path.relative_to(source_dir)
                zipf.write(file_path, arcname)
                print(f" + Adicionado: {arcname}")

    print(f"\n=> SUCESSO! Pacote gerado em:\n   {ZIP_OUTPUT}\n")
    return True


def setup_overleaf_git():
    print("""
========================================================================
Conexão Git Bidirecional com Overleaf (Configurada em papers/artigo-final)
========================================================================

Projeto Overleaf vinculado:
  https://git.overleaf.com/6a92242dbaaa2c6b6833bab0

Comandos de sincronização via Harness:
   py core/tools/overleaf_sync.py --status
   git -C "papers/artigo-final" fetch origin
   git -C "papers/artigo-final" push origin main
========================================================================
""")


def import_overleaf_zip(zip_path_str: str):
    zip_path = Path(zip_path_str)
    if not zip_path.exists():
        print(f"[Erro] Arquivo ZIP não encontrado: {zip_path}", file=sys.stderr)
        return False

    print(f"\n[Importando] Extraindo alterações de {zip_path} para {ARTICLE_DIR}...")
    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(ARTICLE_DIR)
    print("=> Importação concluída com sucesso!\n")
    return True


def main():
    parser = argparse.ArgumentParser(description="Assistente de Sincronização Bidirecional com o Overleaf")
    parser.add_argument("--status", action="store_true", help="Verifica status e histórico do repositório Overleaf")
    parser.add_argument("--zip", action="store_true", help="Gera arquivo .zip para carregar no Overleaf")
    parser.add_argument("--git-setup", action="store_true", help="Exibe guia de configuração do Git com Overleaf")
    parser.add_argument("--import-zip", type=str, help="Caminho do arquivo .zip baixado do Overleaf para importar")

    args = parser.parse_args()

    if args.status:
        check_overleaf_status()
    elif args.zip:
        create_overleaf_zip()
    elif args.git_setup:
        setup_overleaf_git()
    elif args.import_zip:
        import_overleaf_zip(args.import_zip)
    else:
        check_overleaf_status()
        create_overleaf_zip()


if __name__ == "__main__":
    main()
