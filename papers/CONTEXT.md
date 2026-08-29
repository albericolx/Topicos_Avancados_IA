# Módulo de Artigos e Relatórios (`papers/`)
> Redação do artigo científico em LaTeX no padrão Springer LNCS com sincronização direta com o Overleaf.

Esta pasta organiza a produção acadêmica da disciplina de Tópicos Avançados de Inteligência Artificial.

## Estrutura
* [`SPECS.md`](SPECS.md): Normas de rigor científico, formatação e convenções de escrita em LaTeX (Springer LNCS).
* [`artigo-final/`](artigo-final/): Projeto LaTeX sincronizado diretamente com o Overleaf (`git@git.overleaf.com/6a92242dbaaa2c6b6833bab0`).

## Como Trabalhar no Artigo
1. **Edição modular**: As seções estão divididas em `artigo-final/sections/` (`01_introducao.tex` a `05_conclusao.tex`).
2. **Citações**: Toda citação utiliza chaves definidas em `artigo-final/references.bib`. Utilize o assistente `py core/tools/academic_search.py` para pesquisar papers.
3. **Compilação**: Para compilar o PDF localmente, execute `py core/tools/compile_paper.py`.
4. **Sincronização com Overleaf**: No diretório `artigo-final`, utilize `git push origin main` ou `git pull origin main`.
