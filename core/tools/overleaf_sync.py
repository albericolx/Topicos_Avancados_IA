#!/usr/bin/env python3
"""
Overleaf Synchronization Assistant - Sincronização com o Overleaf
Suporta contas com Git nativo (Overleaf Premium/Institucional) e contas gratuitas via exportação/importação ZIP.

Uso:
    py core/tools/overleaf_sync.py --zip           # Gera o pacote ZIP pronto para o Overleaf
    py core/tools/overleaf_sync.py --git-setup     # Configura o Git remote do Overleaf
    py core/tools/overleaf_sync.py --import-zip    # Importa alterações baixadas do Overleaf
"""

import argparse
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
PAPER_DIR = ROOT_DIR / "papers" / "artigo-final"
ZIP_OUTPUT = ROOT_DIR / "papers" / "overleaf-export.zip"

EXCLUDE_EXTS = {
    ".aux", ".bbl", ".blg", ".brf", ".fdb_latexmk", ".fls",
    ".lof", ".log", ".lot", ".nav", ".out", ".snm", ".synctex.gz",
    ".toc", ".vrb", ".bcf", ".run.xml", ".pdf"
}


def create_overleaf_zip():
    print(f"\n[Empacotando] Criando arquivo ZIP para o Overleaf a partir de: {PAPER_DIR}")
    
    if not PAPER_DIR.exists():
        print(f"[Erro] Diretório {PAPER_DIR} não encontrado!", file=sys.stderr)
        return False

    with zipfile.ZipFile(ZIP_OUTPUT, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PAPER_DIR):
            if ".git" in root:
                continue
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in EXCLUDE_EXTS:
                    continue
                # Caminho relativo dentro do zip
                arcname = file_path.relative_to(PAPER_DIR)
                zipf.write(file_path, arcname)
                print(f" + Adicionado: {arcname}")

    print(f"\n=> SUCESSO! Pacote gerado em:\n   {ZIP_OUTPUT}")
    print("\nComo usar no Overleaf:")
    print(" 1. Abra o https://www.overleaf.com no seu navegador.")
    print(" 2. Clique em 'Novo Projeto' -> 'Carregar Projeto'.")
    print(f" 3. Selecione o arquivo: {ZIP_OUTPUT}")
    print(" 4. Seu artigo estará pronto para editar e compilar na nuvem!\n")
    return True


def setup_overleaf_git():
    print("""
========================================================================
Conexão Git com Overleaf (Já Configurada em papers/artigo-final)
========================================================================

A pasta papers/artigo-final já é um clone direto do repositório Overleaf:
  https://git.overleaf.com/6a92242dbaaa2c6b6833bab0

Para enviar alterações locais diretamente para o Overleaf:
   cd "papers/artigo-final"
   git add .
   git commit -m "Minhas alteracoes no artigo"
   git push origin main

Para puxar alterações feitas no Overleaf:
   cd "papers/artigo-final"
   git pull origin main
========================================================================
""")


def import_overleaf_zip(zip_path_str: str):
    zip_path = Path(zip_path_str)
    if not zip_path.exists():
        print(f"[Erro] Arquivo ZIP não encontrado: {zip_path}", file=sys.stderr)
        return False

    print(f"\n[Importando] Extraindo alterações de {zip_path} para {PAPER_DIR}...")
    with zipfile.ZipFile(zip_path, "r") as zipf:
        zipf.extractall(PAPER_DIR)
    print("=> Importação concluída com sucesso! Verifique as alterações com 'git status'.\n")
    return True


def main():
    parser = argparse.ArgumentParser(description="Assistente de Sincronização com o Overleaf")
    parser.add_argument("--zip", action="store_true", help="Gera arquivo .zip para carregar no Overleaf")
    parser.add_argument("--git-setup", action="store_true", help="Exibe guia de configuração do Git com Overleaf")
    parser.add_argument("--import-zip", type=str, help="Caminho do arquivo .zip baixado do Overleaf para importar")

    args = parser.parse_args()

    if args.zip:
        create_overleaf_zip()
    elif args.git_setup:
        setup_overleaf_git()
    elif args.import_zip:
        import_overleaf_zip(args.import_zip)
    else:
        create_overleaf_zip()


if __name__ == "__main__":
    main()
