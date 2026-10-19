# Dados e Particionamento 80/20 (`code/mlp/data/`)
> Dataset clínico Heart Disease (UCI/Kaggle) bruto e partições explícitas padronizadas em conjuntos de treino (80%) e teste (20%).

## Arquivos
* [`heart.csv`](heart.csv): Dataset original com 1.025 registros clínicos, 13 atributos preditivos e variável alvo binária `target` (`0` = saudável, `1` = doença cardíaca).
* [`train_80_standardized.csv`](train_80_standardized.csv): Conjunto de **Treino (80% — 820 amostras)** padronizado via `StandardScaler` ($\mu=0, \sigma=1$ ajustado exclusivamente no treino).
* [`test_20_standardized.csv`](test_20_standardized.csv): Conjunto de **Teste (20% — 205 amostras)** padronizado com os parâmetros estatísticos aprendidos no conjunto de treino (zero *data leakage*).
