# Módulos Internos da CNN (`code/cnn/core_cnn/`)

Este diretório contém a lógica modular da arquitetura convolucional e do fluxo de treinamento:

## Módulos
* **`dataset.py`**: Gerenciador do dataset CIFAR-10. Realiza o download ou reaproveitamento local, particiona os subconjuntos de 25k (treino) e 5k (teste) de forma estratificada e calcula média e desvio padrão reais dos canais de treino para normalização sem vazamento (*zero data leakage*). Fornece loaders com ou sem *data augmentation*.
* **`models.py`**: Define formalmente a arquitetura do **BaselineCNN** (fiel à Seção 3.2 do artigo de Dizabadi com 552.874 parâmetros), a variante com **Conexões Residuais** (`Mod1_ResidualCNN`), a variante com **Squeeze-and-Excitation** (`Mod3_SE_CNN`) e o modelo final integrado (`CombinedCNN`).
* **`train.py`**: Funções padronizadas de loop de treino (`train_one_epoch`), avaliação multimétrica (`evaluate_model`: acurácia, loss, F1 macro, matriz de confusão e throughput) e rotina de treinamento por épocas (`fit_model`).
