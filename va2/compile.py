#!/usr/bin/env python3
"""
Compilador LaTeX autônomo para os documentos da VA2 (va2/main.tex).
Executa o ciclo completo pdflatex + bibtex garantindo a resolução de citações.
"""

import os
import subprocess
import sys
from pathlib import Path

VA2_DIR = Path(__file__).resolve().parent
MAIN_TEX = VA2_DIR / "main.tex"
PDF_OUT = VA2_DIR / "main.pdf"

def compile_va2():
    print(f"[Compilador VA2] Diretório: {VA2_DIR}")
    print(f"[Compilador VA2] Compilando: {MAIN_TEX.name} -> {PDF_OUT.name}")

    if not MAIN_TEX.exists():
        print(f"[Erro] Arquivo {MAIN_TEX} não encontrado.", file=sys.stderr)
        return False

    env = os.environ.copy()
    cwd = str(VA2_DIR)

    steps = [
        (["pdflatex", "-interaction=nonstopmode", "main.tex"], "Passo 1/4: pdflatex inicial"),
        (["bibtex", "main"], "Passo 2/4: bibtex (resolvendo referências)"),
        (["pdflatex", "-interaction=nonstopmode", "main.tex"], "Passo 3/4: pdflatex intermediário"),
        (["pdflatex", "-interaction=nonstopmode", "main.tex"], "Passo 4/4: pdflatex final"),
    ]

    for cmd, desc in steps:
        print(f"  -> {desc}...")
        res = subprocess.run(cmd, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace")
        if res.returncode != 0 and cmd[0] != "bibtex":
            print(f"[Aviso no {desc}] Código de retorno: {res.returncode}")
            # Se for pdflatex e falhar, exibe últimas linhas do log
            log_file = VA2_DIR / "main.log"
            if log_file.exists():
                lines = log_file.read_text(encoding="latin1", errors="replace").splitlines()[-25:]
                print("\n".join(lines), file=sys.stderr)

    if PDF_OUT.exists():
        size = PDF_OUT.stat().st_size
        print(f"\n[SUCESSO] PDF compilado com êxito:")
        print(f"==> {PDF_OUT} ({size:,} bytes)")
        return True
    else:
        print(f"[ERRO] O PDF final não foi gerado em {PDF_OUT}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = compile_va2()
    sys.exit(0 if success else 1)
