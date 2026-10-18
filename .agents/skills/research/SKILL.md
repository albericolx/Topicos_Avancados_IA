---
name: research
description: >
  Módulo de pesquisa e habilidades (skills) do workspace Tópicos Avançados de IA para apoio a
  leitura/revisão bibliográfica, formulação metodológica e redação técnica em LaTeX (Springer LNCS).
---

# Skill Integrada de Pesquisa Acadêmica (`research`)

Ative esta skill para executar tarefas de:
1. **Leitura e Revisão Bibliográfica** ([`core/skills/literature-review.md`](../../../core/skills/literature-review.md)):
   - Busca automatizada via `py core/tools/academic_search.py --query "<tema>" --add-to-bib --generate-yaml --download-pdf`
   - Extração textual e OCR automático zero-token via `py core/tools/pdf_ocr_parser.py`
   - Catalogação estruturada de metadados em [`refs/`](../../../refs/CONTEXT.md) (`REFS.md` + fichas `<key>.yaml`).
2. **Formulação Metodológica** ([`core/skills/methodology-formulation.md`](../../../core/skills/methodology-formulation.md)):
   - Formalização algébrica de grafos computacionais e modelos neurais em [`article/sections/03_metodologia.tex`](../../../article/sections/03_metodologia.tex)
   - Definição de *baselines*, métricas e estudo de ablação em [`article/sections/04_experimentos.tex`](../../../article/sections/04_experimentos.tex).
3. **Redação Técnica e Compilação LaTeX** ([`core/skills/technical-writing.md`](../../../core/skills/technical-writing.md)):
   - Escrita científica em padrão Springer LNCS ([`article/`](../../../article/CONTEXT.md))
   - Compilação local `.tex` $\rightarrow$ `.pdf` via `py core/tools/compile_paper.py`
   - Sincronização bidirecional com o Overleaf via `py core/tools/overleaf_sync.py`.
