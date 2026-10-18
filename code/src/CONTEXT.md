# Código-Fonte e Implementações (`code/src/`)
> Implementação de arquiteturas neurais, grafos computacionais explícitos, autograd e pipelines experimentais.

Esta subpasta concentra os módulos executáveis em Python que sustentam as investigações empíricas da disciplina. Os resultados e figuras gerados aqui alimentam diretamente o manuscrito em [`article/`](../../article/CONTEXT.md).

## Organização Modular
- `models/`: Estruturas de grafos computacionais explícitos (`nx.DiGraph`), camadas densas/convolucionais e SLMs locais.
- `train/`: Loops de treinamento, retropropagação (*backpropagation*), funções de perda e otimizadores.
- `data/`: Scripts de carregamento, pré-processamento e particionamento determinístico (`seed` fixa).
- `plots/`: Geração automatizada de curvas de convergência e diagramas exportados para [`article/figures/`](../../article/figures/CONTEXT.md).
