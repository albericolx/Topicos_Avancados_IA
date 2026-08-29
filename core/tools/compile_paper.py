#!/usr/bin/env python3
"""
LaTeX Paper Compiler - Compilador inteligente de artigos para Windows/Linux
Detecta o motor LaTeX instalado (latexmk, pdflatex, xelatex, tectonic) e gera o PDF final.

Uso:
    py core/tools/compile_paper.py           # Compila o artigo papers/artigo-final/main.tex
    py core/tools/compile_paper.py --clean   # Limpa arquivos temporários (.aux, .log, etc.)
    py core/tools/compile_paper.py --check   # Verifica se há compiladores LaTeX instalados
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
PAPER_DIR = ROOT_DIR / "papers" / "artigo-final"
MAIN_TEX = PAPER_DIR / "main.tex"
MAIN_PDF = PAPER_DIR / "main.pdf"

TEMP_EXTENSIONS = [
    ".aux", ".bbl", ".blg", ".brf", ".fdb_latexmk", ".fls",
    ".lof", ".log", ".lot", ".nav", ".out", ".snm", ".synctex.gz",
    ".toc", ".vrb", ".bcf", ".run.xml"
]


def check_compilers():
    compilers = {
        "latexmk": shutil.which("latexmk"),
        "pdflatex": shutil.which("pdflatex"),
        "xelatex": shutil.which("xelatex"),
        "tectonic": shutil.which("tectonic")
    }
    return compilers


def clean_auxiliary_files():
    print(f"\n[Limpeza] Removendo arquivos temporários em: {PAPER_DIR}")
    removed = 0
    for file in PAPER_DIR.iterdir():
        if file.suffix.lower() in TEMP_EXTENSIONS:
            try:
                file.unlink()
                removed += 1
            except Exception as e:
                print(f"Erro ao remover {file.name}: {e}")
    print(f"=> {removed} arquivo(s) temporário(s) removido(s).\n")


def compile_with_latexmk(latexmk_path: str):
    print("\n[Compilador] Usando latexmk para compilação automatizada...")
    cmd = [latexmk_path, "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]
    result = subprocess.run(cmd, cwd=PAPER_DIR)
    return result.returncode == 0


def compile_with_pdflatex(pdflatex_path: str):
    bibtex_path = shutil.which("bibtex")
    print("\n[Compilador] Executando ciclo pdflatex + bibtex...")
    
    # 1. Primeira passada do pdflatex
    print("Passo 1/4: pdflatex...")
    p1 = subprocess.run([pdflatex_path, "-interaction=nonstopmode", "main.tex"], cwd=PAPER_DIR, stdout=subprocess.DEVNULL)
    
    # 2. BibTeX se disponível
    if bibtex_path:
        print("Passo 2/4: bibtex...")
        subprocess.run([bibtex_path, "main"], cwd=PAPER_DIR, stdout=subprocess.DEVNULL)
    
    # 3. Segunda passada
    print("Passo 3/4: pdflatex (resolvendo referências)...")
    subprocess.run([pdflatex_path, "-interaction=nonstopmode", "main.tex"], cwd=PAPER_DIR, stdout=subprocess.DEVNULL)
    
    # 4. Terceira passada
    print("Passo 4/4: pdflatex final...")
    p4 = subprocess.run([pdflatex_path, "-interaction=nonstopmode", "main.tex"], cwd=PAPER_DIR)
    return p4.returncode == 0


def compile_with_tectonic(tectonic_path: str):
    print("\n[Compilador] Usando Tectonic (modern TeX engine)...")
    cmd = [tectonic_path, "main.tex"]
    result = subprocess.run(cmd, cwd=PAPER_DIR)
    return result.returncode == 0


def show_install_guide():
    print("""
========================================================================
[Aviso] Nenhum compilador LaTeX local foi encontrado no seu computador.
========================================================================

Você tem duas opções excelentes para compilar seus artigos:

Opção 1: Compilar na Nuvem via Overleaf (Já Sincronizado!)
---------------------------------------------------------
1. No diretório papers/artigo-final, você pode enviar alterações direto:
   cd "papers/artigo-final" && git push origin main
2. Ou gerar um zip para importação:
   py core/tools/overleaf_sync.py --zip
3. O Overleaf compila instantaneamente online!

Opção 2: Instalar o MiKTeX no Windows (Para compilar localmente offline)
----------------------------------------------------------------------
No terminal PowerShell como Administrador, execute:
    winget install MiKTeX.MiKTeX

Após a instalação, feche e reabra o terminal e execute novamente:
    py core/tools/compile_paper.py
========================================================================
""")


def main():
    parser = argparse.ArgumentParser(description="Compilador do Artigo Científico em LaTeX")
    parser.add_argument("--clean", action="store_true", help="Limpa arquivos temporários de compilação")
    parser.add_argument("--check", action="store_true", help="Verifica disponibilidade dos compiladores")
    args = parser.parse_args()

    if args.clean:
        clean_auxiliary_files()
        return

    compilers = check_compilers()
    
    if args.check:
        print("\n--- Status dos Compiladores LaTeX ---")
        for name, path in compilers.items():
            status = f"Disponível ({path})" if path else "Não encontrado"
            print(f" - {name:10}: {status}")
        print("-------------------------------------\n")
        return

    if not MAIN_TEX.exists():
        print(f"[Erro] Arquivo principal não encontrado: {MAIN_TEX}", file=sys.stderr)
        sys.exit(1)

    print(f"\n[Iniciando Compilação] Alvo: {MAIN_TEX}")
    success = False

    if compilers["latexmk"]:
        success = compile_with_latexmk(compilers["latexmk"])
    elif compilers["tectonic"]:
        success = compile_with_tectonic(compilers["tectonic"])
    elif compilers["pdflatex"] or compilers["xelatex"]:
        engine = compilers["pdflatex"] or compilers["xelatex"]
        success = compile_with_pdflatex(engine)
    else:
        show_install_guide()
        return

    if success and MAIN_PDF.exists():
        print(f"\n[SUCESSO] PDF gerado com êxito em:\n=> {MAIN_PDF}\n")
    else:
        print(f"\n[Atenção] A compilação terminou. Verifique o arquivo main.log para detalhes.")


if __name__ == "__main__":
    main()
