# Scripts e Ferramentas de Automação (`core/tools/`)
> Utilitários de linha de comando para busca bibliográfica, download de PDFs, OCR zero-token, compilação LaTeX local e sincronização com Overleaf.

## Catálogo de Scripts

| Script | Responsabilidade | Uso via Harness |
|---|---|---|
| [`academic_search.py`](academic_search.py) | Consulta bases acadêmicas (Semantic Scholar, CrossRef, OpenAlex, arXiv), baixa PDFs Open Access (`--download-pdf`), gera metadados `.yaml` (`--generate-yaml`) e entradas BibTeX (`--add-to-bib`) | `py core/tools/academic_search.py --query "termo" --limit 5 --generate-yaml --download-pdf` |
| [`pdf_ocr_parser.py`](pdf_ocr_parser.py) | Extrator local zero-token de texto de PDFs (`pdftotext` / `pypdf`) com fallback automático de OCR (`pdftoppm` + `tesseract`) | `py core/tools/pdf_ocr_parser.py --file refs/pdfs/artigo.pdf --out refs/ocr/artigo.txt` |
| [`compile_paper.py`](compile_paper.py) | Executa o pipeline completo de compilação LaTeX (`pdflatex` + `bibtex` x3) sobre `article/main.tex` e sincroniza `main.pdf` com `papers/artigo-final/main.pdf` | `py core/tools/compile_paper.py` |
| [`overleaf_sync.py`](overleaf_sync.py) | Sincroniza os arquivos `.tex`, `.bib` e figuras com o repositório remoto Git do Overleaf (`https://git.overleaf.com/6a92242dbaaa2c6b6833bab0`) ou empacota `.zip` | `py core/tools/overleaf_sync.py --push` |
