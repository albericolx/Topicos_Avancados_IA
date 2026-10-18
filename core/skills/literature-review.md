---
name: literature-review
description: >
  Habilidade especializada para leitura crítica, busca sistemática de artigos,
  extração zero-token via OCR e catalogação estruturada em YAML na pasta refs/.
---

# Skill: Leitura e Revisão Bibliográfica (`literature-review`)

## Objetivo
Conduzir o levantamento sistemático do estado da arte, garantindo que toda referência citada no manuscrito possua evidência verificada (DOI/arXiv/ACL/IEEE), PDF processado sem desperdício de tokens e ficha estruturada em [`refs/`](../../refs/CONTEXT.md).

## Passo a Passo Operacional
1. **Busca Multicorpus**:
   Execute `py core/tools/academic_search.py --query "<tema>" --limit 5 --add-to-bib --generate-yaml --download-pdf`.
2. **Extração Zero-Token (PDF $\rightarrow$ Texto/OCR)**:
   Para qualquer PDF em `refs/pdfs/`, execute `py core/tools/pdf_ocr_parser.py --file refs/pdfs/<key>.pdf --out refs/ocr/<key>.txt`.
3. **Curadoria da Ficha YAML (`refs/<key>.yaml`)**:
   - Verifique o veículo e classifique o Tier em [`refs/REFS.md`](../../refs/REFS.md) (`[A]`, `[B]`, `[L]`, `[P]`).
   - Preencha `contributions` (o que o trabalho resolve), `gaps` (onde o trabalho falha frente à nossa proposta) e `relevance` (onde será citado no artigo).
4. **Síntese de Trabalhos Relacionados**:
   Redija ou atualize [`article/sections/02_trabalhos_relacionados.tex`](../../article/sections/02_trabalhos_relacionados.tex) contrastando cada referência pelas suas lacunas documentadas.
