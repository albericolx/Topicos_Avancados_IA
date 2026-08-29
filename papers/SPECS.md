# Especificações de Escrita Acadêmica (`papers/SPECS.md`)
> Padrões de rigor metodológico, estilo de escrita e formatação em Springer LNCS.

## 1. Rigor e Evidência
- **Citações Reais**: Toda referência deve ter registro verificado (DOI, arXiv, Springer).
- **Estrutura Argumentativa**:
  - Introdução contextualiza modelos neurais, desafios de gradientes e objetivos da disciplina.
  - Trabalhos relacionados posicionam a implementação frente a bibliotecas como PyTorch e autograd moderno.
  - Metodologia formaliza a álgebra do grafo explícito, forward pass e backward pass.
  - Experimentos trazem curvas de convergência, valores numéricos e discussões empíricas.

## 2. Padrões de LaTeX (Springer LNCS)
- Usar `llncs.cls` e bibliografia com `splncs04.bst`.
- Citações com `\cite{chave}`.
- Figuras e tabelas numeradas e referenciadas no texto.
