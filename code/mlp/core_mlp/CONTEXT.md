# Núcleo Matemático e Visual da MLP (`code/mlp/core_mlp/`)
> Pacote Python contendo a implementação do zero da MLP em grafo direcionado, particionamento de dados, treinamento e visualização sináptica.

## Módulos do Pacote
* [`__init__.py`](__init__.py): Exporta a API pública do pacote `core_mlp`.
* [`dataset.py`](dataset.py): Download/leitura de `heart.csv`, divisão estratificada **80% treino / 20% teste** e padronização pós-split (`StandardScaler` / `MinMaxScaler`).
* [`graph.py`](graph.py): Classe `MLPGraph` sobre `nx.DiGraph`, implementando inicialização He/Xavier, nós de bias em todas as camadas, `forward()` e `backward()` com derivada analítica exata da BCE, *Momentum* e regularização $L_2$.
* [`train.py`](train.py): Funções `bce_loss()`, `mse_loss()`, `train_epoch()`, `evaluate()` e `run_training_history()`.
* [`visualize.py`](visualize.py): Renderização do grafo direcionado com espessura proporcional e rótulos numéricos dos pesos nas arestas (`draw_network`), mapas de calor (`draw_weights_heatmap`), tabela de pesos (`get_weights_dataframe`) e curvas de aprendizado.
