# Scripts e Ferramentas de Automação (`core/tools/`)
> Utilitários de linha de comando para busca bibliográfica, compilação LaTeX local e sincronização com Overleaf.

## Catálogo de Scripts

| Script | Responsabilidade | Uso via Harness |
|---|---|---|
| [`academic_search.py`](academic_search.py) | Consulta bases acadêmicas (arXiv / CrossRef) e extrai metadados e entradas BibTeX verificadas | `py core/tools/academic_search.py --query "termo" --limit 5` |
| [`compile_paper.py`](compile_paper.py) | Executa o pipeline de compilação LaTeX (`pdflatex` + `bibtex`) sobre o projeto do artigo | `py core/tools/compile_paper.py` |
| [`overleaf_sync.py`](overleaf_sync.py) | Sincroniza os arquivos `.tex`, `.bib` e figuras com o repositório remoto do Overleaf ou empacota `.zip` | `py core/tools/overleaf_sync.py --zip` |
