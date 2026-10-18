# Especificações de Escrita Acadêmica (`article/SPECS.md`)
> Padrões de rigor metodológico, estilo de escrita e formatação em Springer LNCS.

## 1. Rigor e Evidência Científica
- **Citações Verificadas**: Proibido alucinar referências. Toda entrada em [`references.bib`](references.bib) deve possuir DOI ou identificador canônico (arXiv, ACM, IEEE, ACL, Springer) validado.
- **Estrutura Argumentativa**:
  - **Introdução** (`sections/01_introducao.tex`): Contextualiza o problema, a motivação, a lacuna de pesquisa e as contribuições do trabalho.
  - **Trabalhos Relacionados** (`sections/02_trabalhos_relacionados.tex`): Posiciona a proposta frente ao estado da arte e matriz de competidores.
  - **Metodologia** (`sections/03_metodologia.tex`): Formaliza a arquitetura, modelos neurais, grafos computacionais e protocolo experimental.
  - **Experimentos e Resultados** (`sections/04_experimentos.tex`): Apresenta métricas quantitativas, curvas de perda/acurácia, estudo de ablação e análise crítica.
  - **Conclusão** (`sections/05_conclusao.tex`): Sintetiza achados, limitações técnicas assumidas e trabalhos futuros.

## 2. Padrões de Formatação LaTeX (Springer LNCS)
- Classe documental `\documentclass[runningheads]{llncs}` ([`llncs.cls`](llncs.cls)) e estilo bibliográfico `\bibliographystyle{splncs04}` ([`splncs04.bst`](splncs04.bst)).
- Citações no formato `\cite{chave}` e referências cruzadas com `\ref{}` / `\label{}`.
- Figuras vetoriais ou em alta resolução armazenadas em [`figures/`](figures/CONTEXT.md).
