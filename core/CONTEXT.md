# Módulo Core de Ferramentas, Skills, Fluxos e Agentes (`core/`)
> Infraestrutura agnóstica de provedor para suporte a pesquisa científica, revisão sistemática, compilação LaTeX local, sincronização com Overleaf e orquestração de habilidades (*skills*).

## Estrutura da Pasta
* [`tools/`](tools/CONTEXT.md): Scripts de automação em Python para busca acadêmica, download de PDFs, OCR zero-token, compilação LaTeX e sincronização Overleaf.
* [`skills/`](skills/CONTEXT.md): Especificação de habilidades operacionais (`research.md`, `literature-review.md`, `methodology-formulation.md`, `technical-writing.md`).
* [`flows/`](flows/CONTEXT.md): Fluxos operacionais passo a passo para condução da pesquisa (`literature.md`, `methodology.md`, `draft.md`, `review.md`).
* [`agents/`](agents/CONTEXT.md): Perfis de agentes especialistas (`researcher.md`, `writer.md`, `reviewer.md`).

## Roteamento de Ferramentas (`core/tools/`)

| Script | Função | Exemplo de Execução |
|---|---|---|
| [`academic_search.py`](tools/academic_search.py) | Busca artigos no Semantic Scholar / CrossRef / OpenAlex / arXiv, baixa PDFs Open Access, gera metadados `.yaml` em `refs/` e entradas BibTeX | `py core/tools/academic_search.py --query "neural networks autograd" --limit 3 --generate-yaml` |
| [`pdf_ocr_parser.py`](tools/pdf_ocr_parser.py) | Extrai texto nativo (`pdftotext`/`pypdf`) ou via OCR zero-token (`pdftoppm` + `tesseract`) a partir de PDFs em `refs/pdfs/` | `py core/tools/pdf_ocr_parser.py --file refs/pdfs/vaswani2017attention.pdf --pages 1-2 --out refs/ocr/vaswani2017attention.txt` |
| [`compile_paper.py`](tools/compile_paper.py) | Compila `article/main.tex` em `article/main.pdf` via MiKTeX (`pdflatex` + `bibtex`) e espelha o PDF em `papers/artigo-final/main.pdf` | `py core/tools/compile_paper.py` |
| [`overleaf_sync.py`](tools/overleaf_sync.py) | Sincroniza bidirecionalmente com o repositório Git do Overleaf (`papers/artigo-final`) ou gera pacote `.zip` | `py core/tools/overleaf_sync.py --push` |
