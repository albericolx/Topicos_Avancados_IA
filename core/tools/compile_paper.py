#!/usr/bin/env python3
"""
LaTeX Paper Compiler - Compilador inteligente de artigos e relatórios para Windows/Linux
Detecta o motor LaTeX instalado (latexmk, pdflatex, xelatex, tectonic) e gera o PDF final.

Uso:
    py core/tools/compile_paper.py                        # Compila main.tex e report-mlp.tex
    py core/tools/compile_paper.py --target report-mlp.tex # Compila apenas report-mlp.tex
    py core/tools/compile_paper.py --clean                # Limpa arquivos temporários (.aux, .log, etc.)
    py core/tools/compile_paper.py --check                # Verifica se há compiladores LaTeX instalados
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
PAPER_DIR = ROOT_DIR / "article" if (ROOT_DIR / "article" / "main.tex").exists() else (ROOT_DIR / "papers" / "artigo-final")

TEMP_EXTENSIONS = [
    ".aux", ".bbl", ".blg", ".brf", ".fdb_latexmk", ".fls",
    ".lof", ".log", ".lot", ".nav", ".out", ".snm", ".synctex.gz",
    ".toc", ".vrb", ".bcf", ".run.xml"
]


def check_compilers():
    miktex_bin = Path(os.path.expanduser("~")) / "AppData" / "Local" / "Programs" / "MiKTeX" / "miktex" / "bin" / "x64"
    if miktex_bin.exists() and str(miktex_bin) not in os.environ.get("PATH", ""):
        os.environ["PATH"] = os.environ.get("PATH", "") + os.pathsep + str(miktex_bin)

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


def compile_with_latexmk(latexmk_path: str, tex_name: str):
    print(f"\n[Compilador] Usando latexmk para compilar {tex_name}...")
    cmd = [latexmk_path, "-pdf", "-interaction=nonstopmode", "-halt-on-error", tex_name]
    result = subprocess.run(cmd, cwd=PAPER_DIR)
    return result.returncode == 0


def compile_with_pdflatex(pdflatex_path: str, tex_name: str):
    bibtex_path = shutil.which("bibtex")
    stem = Path(tex_name).stem
    print(f"\n[Compilador] Executando ciclo pdflatex + bibtex para {tex_name}...")

    print("Passo 1/4: pdflatex...")
    subprocess.run([pdflatex_path, "-interaction=nonstopmode", tex_name], cwd=PAPER_DIR, stdout=subprocess.DEVNULL)

    if bibtex_path:
        print("Passo 2/4: bibtex...")
        subprocess.run([bibtex_path, stem], cwd=PAPER_DIR, stdout=subprocess.DEVNULL)

    print("Passo 3/4: pdflatex (resolvendo referências)...")
    subprocess.run([pdflatex_path, "-interaction=nonstopmode", tex_name], cwd=PAPER_DIR, stdout=subprocess.DEVNULL)

    print("Passo 4/4: pdflatex final...")
    p4 = subprocess.run([pdflatex_path, "-interaction=nonstopmode", tex_name], cwd=PAPER_DIR)
    return p4.returncode == 0


def compile_with_tectonic(tectonic_path: str, tex_name: str):
    print(f"\n[Compilador] Usando Tectonic para compilar {tex_name}...")
    cmd = [tectonic_path, tex_name]
    result = subprocess.run(cmd, cwd=PAPER_DIR)
    return result.returncode == 0


def compile_target(tex_name: str, compilers: dict):
    tex_path = PAPER_DIR / tex_name
    pdf_path = PAPER_DIR / f"{Path(tex_name).stem}.pdf"
    if not tex_path.exists():
        print(f"[Erro] Arquivo não encontrado: {tex_path}", file=sys.stderr)
        return False

    print(f"\n[Iniciando Compilação] Alvo: {tex_path}")
    success = False
    if compilers["latexmk"] and shutil.which("perl"):
        success = compile_with_latexmk(compilers["latexmk"], tex_name)
    if not success and compilers["tectonic"]:
        success = compile_with_tectonic(compilers["tectonic"], tex_name)
    if not success and (compilers["pdflatex"] or compilers["xelatex"]):
        engine = compilers["pdflatex"] or compilers["xelatex"]
        success = compile_with_pdflatex(engine, tex_name)

    if success and pdf_path.exists():
        mirror_dir = ROOT_DIR / "papers" / "artigo-final"
        if PAPER_DIR != mirror_dir and mirror_dir.exists():
            shutil.copy2(tex_path, mirror_dir / tex_name)
            shutil.copy2(pdf_path, mirror_dir / pdf_path.name)
        print(f"\n[SUCESSO] PDF gerado com êxito em:\n=> {pdf_path}\n")
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Compilador do Artigo Científico e Relatórios em LaTeX")
    parser.add_argument("--target", type=str, default=None, help="Arquivo .tex alvo (ex.: main.tex ou report-mlp.tex)")
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

    targets = [args.target] if args.target else [t for t in ["main.tex", "report-mlp.tex"] if (PAPER_DIR / t).exists()]
    for tgt in targets:
        compile_target(tgt, compilers)
    clean_auxiliary_files()


if __name__ == "__main__":
    main()
