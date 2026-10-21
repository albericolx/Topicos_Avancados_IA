# Módulo de Código (`code/`)
> Modelos neurais, algoritmos de retropropagação, grafos computacionais e subrepositórios experimentais de IA.

Esta pasta abriga todo o desenvolvimento prático da disciplina de **Tópicos Avançados em Inteligência Artificial (UFRPE 2026.2)**. O código desenvolvido aqui alimenta os experimentos, dados, figuras e resultados apresentados nos relatórios técnicos e no artigo científico em [`article/`](../article/CONTEXT.md).

## Diretrizes de Desenvolvimento
1. **Isolamento em Subrepositórios Modulares**: Cada artefato de código da disciplina possui seu subdiretório isolado sob `code/` com seu próprio `CONTEXT.md`.
2. **Reprodutibilidade**: Todo script de treinamento, particionamento de dados e análise de convergência possui semente aleatória fixada (`seed=42`) e instruções claras de execução.
3. **Controle de Branches**: Todo desenvolvimento segue rigorosamente as regras de [`SPECS-git.md`](SPECS-git.md).

## Estrutura da Pasta (`code/`)
* [`SPECS-git.md`](SPECS-git.md): Regras de branches, convenções de commits e GitFlow.
* [`mlp/`](mlp/CONTEXT.md): **Subrepositório do Artefato `[5] · mlp git repo` (`mlp·c`)** — Implementação do zero de Rede Neural Multicamadas (MLP) sobre grafo direcionado (`nx.DiGraph` + `NumPy`), interface interativa em `Streamlit` (`code/mlp/app.py`), particionamento 80/20 sem vazamento (`code/mlp/data/`), inspeção visual e numérica dos pesos sinápticos (`code/mlp/figs/`) e relatório técnico (`code/mlp/REPORT.md` e `code/mlp/report/relatorio_mlp.pdf`).
* [`cnn/`](cnn/CONTEXT.md): **Subrepositório do Artefato `[5] · arquitetura git repo` (`arq·c`)** — Reprodução empírica da CNN para CIFAR-10 (Dizabadi, 2026, 552.874 parâmetros), 3 modificações arquiteturais inéditas (ResNet, Data Augmentation, SE-Block) e modelo combinado integrado.
* [`arena/`](arena/CONTEXT.md): **Subrepositório do Artefato `[5] · arena git repo` (`arn·c`)** — Ambiente experimental de múltiplos agentes em arena dialética hierárquica (Nanda, Claudio e Ariel) debatendo impactos de IA em cenários de Utopia e Distopia com 40 rodadas automatizadas, busca web em tempo real e raciocínio em cadeia.
* [`src/`](src/CONTEXT.md): Diretório base de protótipos e utilitários compartilhados.
