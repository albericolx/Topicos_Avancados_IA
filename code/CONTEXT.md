# Módulo de Código (`code/`)
> Modelos neurais, algoritmos de retropropagação, grafos computacionais e experimentos de IA.

Esta pasta abriga todo o desenvolvimento prático da disciplina de Tópicos Avançados de Inteligência Artificial. O código desenvolvido aqui alimenta os experimentos, dados e resultados apresentados no artigo científico em [`article/`](../article/CONTEXT.md) e [`papers/`](../papers/CONTEXT.md).

## Diretrizes de Desenvolvimento
1. **Pequenos módulos**: Mantenha o código coeso e bem documentado.
2. **Reprodutibilidade**: Todo script de treinamento e análise de convergência deve possuir semente aleatória fixada (`seed`) e instruções claras de execução.
3. **Controle de Branches**: Todo desenvolvimento deve seguir as regras de [`SPECS-git.md`](SPECS-git.md).

## Estrutura da Pasta
* [`SPECS-git.md`](SPECS-git.md): Regras de branches, convenções de commits e GitFlow.
* [`src/`](src/CONTEXT.md): Diretório de código-fonte dos modelos neurais, camadas e funções de perda (documentado em [`src/CONTEXT.md`](src/CONTEXT.md)).
