# Resultados Experimentais e Pesos Sinápticos (`code/mlp/results/`)
> Arquivos CSV e JSON gerados pela execução de `code/mlp/run_experiments.py`.

## Arquivos Gerados
* [`benchmark_results.csv`](benchmark_results.csv): Tabela comparativa das 8 configurações experimentais (`C0` a `C7`) com Loss, Acurácia, Precisão, Recall, Especificidade, F1-Score, AUC-ROC e Matriz de Confusão.
* [`benchmark_summary.json`](benchmark_summary.json): Sumário completo do particionamento 80/20 e métricas da configuração campeã.
* [`best_model_synaptic_weights.csv`](best_model_synaptic_weights.csv): Tabela completa de todos os pesos sinápticos ($w_{ij}$), variações por época ($\Delta w_{ij}$) e gradientes ($\partial \mathcal{L} / \partial w_{ij}$) do modelo otimizado.
