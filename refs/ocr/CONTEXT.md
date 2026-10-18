# Extrações de Texto e OCR Zero-Token (`refs/ocr/`)
> Saídas em texto puro (`.txt`) extraídas localmente via `core/tools/pdf_ocr_parser.py` (`pdftotext`/`pypdf` nativo com fallback OCR `pdftoppm` + `tesseract`), sem consumo de tokens de LLM.

## Arquivos Extraídos
* [`vaswani2017attention.txt`](vaswani2017attention.txt): Texto extraído localmente (zero-token) das páginas iniciais de *Attention Is All You Need* (`vaswani2017attention.pdf`).
* [`main_compiled_article.txt`](main_compiled_article.txt): Texto extraído localmente (zero-token) a partir do PDF compilado do próprio manuscrito (`article/main.pdf`), validando a renderização textual e bibliográfica das 6 referências citadas.
