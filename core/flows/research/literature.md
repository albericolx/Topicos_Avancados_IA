# Fluxo: Revisão Bibliográfica Automatizada (`literature.md`)
> Artefato produzido: entradas em `article/references.bib`, PDFs em `refs/pdfs/`, extrações zero-token em `refs/ocr/` e fichas estruturadas `refs/<key>.yaml`.

## Etapas de Execução
1. **Consulta Automatizada**:
   Execute `py core/tools/academic_search.py --query "<tópico>" --limit 5 --add-to-bib --generate-yaml --download-pdf`.
2. **Processamento Zero-Token (OCR / Extração)**:
   Verifique a extração gerada em `refs/ocr/<key>.txt` via `core/tools/pdf_ocr_parser.py`.
3. **Qualificação em `refs/<key>.yaml` e `refs/REFS.md`**:
   Classifique o veículo (`[A]`, `[B]`, `[L]`, `[P]`) e sintetize `contributions`, `gaps` e `relevance`.
4. **Integração no Manuscrito**:
   Atualize `article/sections/02_trabalhos_relacionados.tex` posicionando cada trabalho frente à nossa proposta.
