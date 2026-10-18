#!/usr/bin/env python3
"""
PDF & Zero-Token OCR Parser (`core/tools/pdf_ocr_parser.py`)
Extrai texto estruturado de artigos em PDF localmente (zero-token, sem consumo de LLM),
combinando extração nativa (pdftotext / pypdf) com fallback automático de OCR (Tesseract).

Uso:
    py core/tools/pdf_ocr_parser.py --file refs/pdfs/vaswani2017attention.pdf --out refs/ocr/vaswani2017attention.txt
    py core/tools/pdf_ocr_parser.py --file refs/pdfs/vaswani2017attention.pdf --pages 1-3 --md
"""

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def extract_with_pdftotext(pdf_path: Path, pages: str = None, layout: bool = False) -> str:
    pdftotext_bin = shutil.which("pdftotext")
    if not pdftotext_bin:
        return ""
    cmd = [pdftotext_bin]
    if layout:
        cmd.append("-layout")
    if pages and "-" in pages:
        start, end = pages.split("-", 1)
        cmd.extend(["-f", start.strip(), "-l", end.strip()])
    cmd.extend([str(pdf_path), "-"])
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return res.stdout.strip() if res.returncode == 0 else ""


def extract_with_pypdf(pdf_path: Path, pages: str = None) -> str:
    try:
        import pypdf
        reader = pypdf.PdfReader(str(pdf_path))
        total = len(reader.pages)
        start_idx, end_idx = 0, total
        if pages and "-" in pages:
            s, e = pages.split("-", 1)
            start_idx = max(0, int(s) - 1)
            end_idx = min(total, int(e))
        chunks = []
        for idx in range(start_idx, end_idx):
            txt = reader.pages[idx].extract_text() or ""
            if txt.strip():
                chunks.append(f"--- [Página {idx + 1}] ---\n{txt.strip()}")
        return "\n\n".join(chunks)
    except Exception:
        return ""


def extract_with_tesseract_ocr(pdf_path: Path, pages: str = None) -> str:
    pdftoppm_bin = shutil.which("pdftoppm")
    tesseract_bin = shutil.which("tesseract")
    if not pdftoppm_bin or not tesseract_bin:
        return ""
    with tempfile.TemporaryDirectory() as tmpdir:
        cmd = [pdftoppm_bin, "-png", "-r", "150"]
        if pages and "-" in pages:
            start, end = pages.split("-", 1)
            cmd.extend(["-f", start.strip(), "-l", end.strip()])
        cmd.extend([str(pdf_path), f"{tmpdir}/page"])
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            return ""
        img_pages = sorted(Path(tmpdir).glob("page-*.png"))
        parts = []
        for img in img_pages:
            ocr = subprocess.run(
                [tesseract_bin, str(img), "stdout", "-l", "por+eng", "--oem", "1"],
                capture_output=True, text=True, encoding="utf-8", errors="replace"
            )
            if ocr.returncode == 0 and ocr.stdout.strip():
                parts.append(ocr.stdout.strip())
        return "\n\n--- [OCR PAGE] ---\n\n".join(parts)


def parse_pdf_zero_token(pdf_path: Path, pages: str = None, force_ocr: bool = False, layout: bool = False):
    """
    Executa pipeline zero-token para extração textual de PDF:
    1. Se force_ocr=True, aplica OCR direto via pdftoppm + tesseract.
    2. Tenta extração nativa rápida via pdftotext (Poppler/MiKTeX).
    3. Fallback para pypdf puro.
    4. Se o PDF for escaneado (texto extraído < 40 caracteres), aciona OCR automático via Tesseract.
    """
    method_used = "native_pdftotext"
    text = ""

    if force_ocr:
        text = extract_with_tesseract_ocr(pdf_path, pages)
        method_used = "tesseract_ocr"
    else:
        text = extract_with_pdftotext(pdf_path, pages, layout=layout)
        if len(text) < 40:
            text = extract_with_pypdf(pdf_path, pages)
            method_used = "native_pypdf"
        if len(text) < 40:
            ocr_text = extract_with_tesseract_ocr(pdf_path, pages)
            if len(ocr_text) >= 40:
                text = ocr_text
                method_used = "tesseract_ocr_fallback"

    return {
        "file": str(pdf_path),
        "method": method_used,
        "zero_token": True,
        "char_count": len(text),
        "text": text
    }


def main():
    parser = argparse.ArgumentParser(description="Extrator Zero-Token e OCR Automático para PDFs Acadêmicos")
    parser.add_argument("--file", "-f", type=Path, required=True, help="Caminho do arquivo PDF")
    parser.add_argument("--pages", "-p", type=str, default=None, help="Intervalo de páginas (ex: 1-5)")
    parser.add_argument("--ocr", action="store_true", help="Forçar OCR via Tesseract")
    parser.add_argument("--layout", action="store_true", help="Preservar layout visual de colunas")
    parser.add_argument("--out", "-o", type=Path, default=None, help="Salvar texto extraído em arquivo")
    parser.add_argument("--json", action="store_true", help="Retornar saída estruturada em JSON")

    args = parser.parse_args()
    if not args.file.exists():
        print(json.dumps({"error": f"Arquivo não encontrado: {args.file}"}), file=sys.stderr)
        sys.exit(1)

    result = parse_pdf_zero_token(args.file, pages=args.pages, force_ocr=args.ocr, layout=args.layout)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(result["text"], encoding="utf-8")
        print(f"[Zero-Token OCR] Texto extraído ({result['char_count']} caracteres via {result['method']}) salvo em: {args.out}")
    elif args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["text"][:4000])


if __name__ == "__main__":
    main()
