# Módulo de Artigo Científico (`article/`)
> Projeto LaTeX no padrão Springer LNCS unificado no repositório e sincronizado com o Overleaf.

Esta pasta abriga o manuscrito científico principal da disciplina de **Tópicos Avançados em Inteligência Artificial (UFRPE 2026.2)**, integrando na mesma árvore de versionamento o código-fonte ([`code/`](../code/CONTEXT.md)), as ferramentas de automação ([`core/`](../core/CONTEXT.md)) e a produção acadêmica.

## Estrutura do Diretório
* [`SPECS.md`](SPECS.md): Normas de rigor científico, estilo acadêmico e formatação Springer LNCS.
* [`main.tex`](main.tex): Documento mestre LaTeX com metadados de autoria (**José Albérico Rocha da Silva** — UFRPE).
* [`references.bib`](references.bib): Base de referências bibliográficas verificadas em BibTeX.
* [`llncs.cls`](llncs.cls) e [`splncs04.bst`](splncs04.bst): Classe oficial e estilo bibliográfico Springer *Lecture Notes in Computer Science*.
* [`sections/`](sections/CONTEXT.md): Capítulos modulares do artigo (`01_introducao.tex` a `05_conclusao.tex`).
* [`figures/`](figures/CONTEXT.md): Gráficos de convergência, topologias neurais e diagramas arquiteturais.

## Fluxo Operacional via Harness
1. **Edição Modular**: Cada seção do artigo é editada de forma isolada em [`sections/`](sections/CONTEXT.md) e incluída via `\input{}` no [`main.tex`](main.tex).
2. **Validação Bibliográfica**: Novas referências devem ser consultadas via [`core/tools/academic_search.py`](../core/tools/academic_search.py) e registradas em [`references.bib`](references.bib).
3. **Compilação Local**: Execute `py core/tools/compile_paper.py` na raiz do workspace para validar a geração do PDF sem erros de LaTeX.
4. **Sincronização Overleaf**: Utilize `py core/tools/overleaf_sync.py` para manter paridade bidirecional com o espelho em [`papers/artigo-final/`](../papers/CONTEXT.md).
