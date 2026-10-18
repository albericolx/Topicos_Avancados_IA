---
name: research
description: >
  Executa fluxos estruturados de pesquisa acadêmica do workspace: revisão bibliográfica (literature),
  formulação metodológica (methodology), redação técnica em LaTeX (draft) e auditoria de pares (review).
flow: literature, methodology, draft, review
---

# Dispatcher do Módulo de Pesquisa (`research`)

Executa um fluxo de trabalho científico do sistema de pesquisa em [`core/flows/research/`](../flows/research/CONTEXT.md).

## Fluxos Disponíveis

| Comando | Protocolo em Disco | Aplicação |
|---|---|---|
| `literature` | [`core/flows/research/literature.md`](../flows/research/literature.md) | Levantamento bibliográfico, download de PDFs, OCR zero-token e geração de fichas `.yaml` em `refs/` |
| `methodology` | [`core/flows/research/methodology.md`](../flows/research/methodology.md) | Formulação matemática, desenho experimental, definição de *baselines* e estudo de ablação |
| `draft` | [`core/flows/research/draft.md`](../flows/research/draft.md) | Redação técnica modular em LaTeX (Springer LNCS) ancorada nas fichas de `refs/` |
| `review` | [`core/flows/research/review.md`](../flows/research/review.md) | Simulação de revisão cega por pares (*peer review*) e auditoria de citações/consistência |

## Protocolo de Execução pelo Harness
1. Leia o protocolo correspondente em `core/flows/research/<fluxo>.md`.
2. Utilize as ferramentas de CLI em [`core/tools/`](../tools/CONTEXT.md):
   - `py core/tools/academic_search.py --query "<termo>" --add-to-bib --generate-yaml --download-pdf`
   - `py core/tools/pdf_ocr_parser.py --file refs/pdfs/<key>.pdf --out refs/ocr/<key>.txt`
   - `py core/tools/compile_paper.py`
   - `py core/tools/overleaf_sync.py`
3. Invoque os perfis especialistas em [`core/agents/`](../agents/CONTEXT.md) (`researcher.md`, `writer.md`, `reviewer.md`).
