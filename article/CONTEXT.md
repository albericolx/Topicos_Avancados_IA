# Módulo de Artigo Científico (`article/`)
> Projeto LaTeX no padrão Springer LNCS unificado no repositório, compilado localmente via harness e sincronizado com o Overleaf.

Esta pasta abriga o manuscrito científico principal da disciplina de **Tópicos Avançados em Inteligência Artificial (UFRPE 2026.2)**, integrando na mesma árvore de versionamento o código-fonte ([`code/`](../code/CONTEXT.md)), as ferramentas de automação ([`core/`](../core/CONTEXT.md)), o pipeline de referências ([`refs/`](../refs/CONTEXT.md)) e a produção acadêmica.

## Estrutura do Diretório
* [`SPECS.md`](SPECS.md): Normas de rigor científico, estilo acadêmico e formatação Springer LNCS.
* [`main.tex`](main.tex): Documento mestre LaTeX com metadados de autoria (**José Albérico Rocha da Silva** — UFRPE).
* [`main.pdf`](main.pdf): Artigo científico compilado localmente em PDF via harness (`py core/tools/compile_paper.py`).
* [`references.bib`](references.bib): Base de referências bibliográficas verificadas em BibTeX (6 referências reais sincronizadas com [`refs/`](../refs/CONTEXT.md)).
* [`refs/`](refs/CONTEXT.md): Espelho local das fichas catalográficas `.yaml`, índice `REFS.md` e extrações de texto zero-token (`ocr/`).
* [`llncs.cls`](llncs.cls) e [`splncs04.bst`](splncs04.bst): Classe oficial e estilo bibliográfico Springer *Lecture Notes in Computer Science*.
* [`sections/`](sections/CONTEXT.md): Capítulos modulares do artigo (`01_introducao.tex` a `05_conclusao.tex`).
* [`figures/`](figures/CONTEXT.md): Gráficos de convergência, topologias neurais e diagramas arquiteturais.

## Fluxo Operacional via Harness
1. **Edição Modular**: Cada seção do artigo é editada de forma isolada em [`sections/`](sections/CONTEXT.md) e incluída via `\input{}` no [`main.tex`](main.tex).
2. **Validação Bibliográfica e OCR Zero-Token**: Novas referências são consultadas via [`core/tools/academic_search.py`](../core/tools/academic_search.py), extraídas via [`core/tools/pdf_ocr_parser.py`](../core/tools/pdf_ocr_parser.py) e catalogadas em [`refs/`](../refs/CONTEXT.md) e [`references.bib`](references.bib).
3. **Compilação Local**: Execute `py core/tools/compile_paper.py` na raiz do workspace para validar a geração de [`main.pdf`](main.pdf) sem erros de LaTeX/BibTeX.
4. **Sincronização Overleaf**: Utilize `py core/tools/overleaf_sync.py --status` (ou `--zip`) para manter paridade bidirecional com o espelho em [`papers/artigo-final/`](../papers/CONTEXT.md).
