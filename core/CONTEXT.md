# Módulo de Ferramentas e Utilitários (`core/`)
> Scripts agnósticos de provedor para suporte a pesquisa acadêmica, compilação de LaTeX e sincronização.

## Roteamento de Ferramentas (`core/tools/`)

| Script | Função | Exemplo de Execução |
|---|---|---|
| [`academic_search.py`](tools/academic_search.py) | Busca artigos científicos no arXiv / CrossRef e gera citações BibTeX | `py core/tools/academic_search.py --query "neural networks autograd" --limit 3` |
| [`compile_paper.py`](tools/compile_paper.py) | Compila o manuscrito LaTeX em PDF no ambiente local | `py core/tools/compile_paper.py` |
| [`overleaf_sync.py`](tools/overleaf_sync.py) | Auxilia na sincronização com Overleaf (Git ou pacote .zip) | `py core/tools/overleaf_sync.py --zip` |
