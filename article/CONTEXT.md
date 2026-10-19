# Módulo de Artigos e Relatórios Científicos (`article/`)
> Projeto LaTeX no padrão Springer LNCS unificado no repositório, compilado localmente via harness e sincronizado com o Overleaf.

Esta pasta abriga o manuscrito científico principal da disciplina ([`main.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/main.tex)) e o relatório técnico formal dedicado da MLP ([`report-mlp.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-mlp.tex)), integrando na mesma árvore de versionamento o código-fonte ([`code/`](../code/CONTEXT.md)), as ferramentas de automação ([`core/`](../core/CONTEXT.md)), o pipeline de referências ([`refs/`](../refs/CONTEXT.md)) e a produção acadêmica.

## Estrutura do Diretório
* [`SPECS.md`](SPECS.md): Normas de rigor científico, estilo acadêmico e formatação Springer LNCS.
* [`report-mlp.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-mlp.tex): Documento LaTeX dedicado do artefato `[5] artefato · mlp tech report` (`mlp·p`), contemplando Fundamentação Teórica (Aprendizado de Máquina, Regressão Linear, Mínimos Quadrados vs. Gradiente Descendente), Mecanismo Sináptico com exemplo numérico real, Curvas e Métricas e Análise Crítica.
* [`report-mlp.pdf`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-mlp.pdf): PDF compilado localmente sem erros a partir de `report-mlp.tex` (14 páginas).
* [`main.tex`](main.tex) e [`main.pdf`](main.pdf): Documento mestre LaTeX e PDF compilado do artigo científico da disciplina.
* [`references.bib`](references.bib): Base de referências bibliográficas verificadas em BibTeX (12 referências reais).
* [`refs/`](refs/CONTEXT.md): Espelho local das fichas catalográficas `.yaml`, índice `REFS.md` e extrações de texto zero-token (`ocr/`).
* [`llncs.cls`](llncs.cls) e [`splncs04.bst`](splncs04.bst): Classe oficial e estilo bibliográfico Springer *Lecture Notes in Computer Science*.
* [`sections/`](sections/CONTEXT.md): Capítulos modulares do artigo (`01_introducao.tex` a `05_conclusao.tex`).
* [`figures/`](figures/CONTEXT.md): Gráficos de convergência, exemplo numérico em neurônio artificial, estudo de taxa de aprendizado, topologias neurais e diagramas arquiteturais.

## Fluxo Operacional via Harness
1. **Compilação Local (`main.tex` e `report-mlp.tex`)**: Execute `py core/tools/compile_paper.py` (ou `py core/tools/compile_paper.py --target report-mlp.tex`) na raiz do workspace para validar a geração de [`main.pdf`](main.pdf) e [`report-mlp.pdf`](report-mlp.pdf) sem erros de LaTeX/BibTeX.
2. **Sincronização Overleaf**: Utilize `py core/tools/overleaf_sync.py --status` (ou `--zip`) para manter paridade bidirecional com o espelho em [`papers/artigo-final/`](../papers/CONTEXT.md).
