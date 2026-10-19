# Artefatos de Verificação da Disciplina (`artefatos/`)
> Documentação estruturada e rastreamento de evidências para os pontos de verificação de Tópicos Avançados em IA (AI4Good — UFRPE 2026.2).

Esta pasta consolida as folhas de verificação e evidências instrumentais exigidas no cronograma e no painel de acompanhamento da disciplina (`lucassf.pages.dev/ai4good`).

## Artefatos Registrados

| Artefato | Código no Painel | Pontuação | Descrição |
|---|---:|---:|---|
| [`3-base-git-repo.md`](3-base-git-repo.md) | `git` | 6 pts | Configuração instrumental inicial do ambiente de trabalho e repositório de código (commit inaugural assinado pelo harness, árvore integrada `code/` + `article/` + docs, e especificação modular com `AGENTS.md` e `CONTEXT.md`). |
| [`4-latex-project.md`](4-latex-project.md) | `tex` | 8 pts | Infraestrutura de redação científica rigorosa, integrando compilação local via harness (`article/main.pdf`), sincronização bidirecional com Overleaf (`papers/artigo-final`), pipeline de referências com OCR zero-token e metadados `.yaml` (`refs/`), e módulo de pesquisa e *skills* (`core/skills/`, `core/flows/research/`). |
| [`5-mlp-git-repo.md`](5-mlp-git-repo.md) | `mlp·c` | 10 pts | Implementação do zero de uma Rede Neural Multicamadas (MLP) em grafo direcionado (`nx.DiGraph` + `NumPy`) no subrepositório [`code/mlp/`](../code/mlp/CONTEXT.md), com interface interativa em `Streamlit` ([`code/mlp/app.py`](../code/mlp/app.py)), particionamento 80/20 sem vazamento, dinâmica completa de *forward/backpropagation*, inspeção numérica e visual de pesos a cada época e relatório técnico ([`REPORT.md`](../code/mlp/REPORT.md) e [`relatorio_mlp.pdf`](../code/mlp/report/relatorio_mlp.pdf)). |
