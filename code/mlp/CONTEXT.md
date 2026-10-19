# Subrepositório da Rede Neural Multicamadas (`code/mlp/`)
> Implementação do zero (*from scratch*) de uma Rede Neural Multicamadas (MLP) sobre Grafo Direcionado (`NetworkX DiGraph` + `NumPy`), com interface interativa em `Streamlit`, particionamento explícito 80/20 e visualização de pesos sinápticos a cada época — **`[5] artefato · mlp git repo` (`mlp·c`)**.

## 1. Objetivos do Subrepositório
1. **Desmistificar a Caixa-Preta Neural**: Implementar todas as operações matemáticas de *Forward Pass*, *Backpropagation* e *Gradiente Descendente* (com suporte a *Momentum* e regularização $L_2$) diretamente sobre os nós e arestas de um grafo direcionado `nx.DiGraph`, sem uso de frameworks de diferenciação automática (como PyTorch ou TensorFlow).
2. **Parametrização Interativa em Tempo Real (`app.py`)**: Permitir configurar dinamicamente no painel lateral do Streamlit o número de camadas ocultas (1 a 4), quantidade de neurônios por camada, função de ativação (`ReLU`, `Leaky ReLU`, `Tanh`, `Sigmoide`, `ELU`, `SELU`, `ReLU6`), taxa de aprendizagem ($\eta$), decaimento de LR, *Momentum* ($\beta$), regularização $L_2$ ($\lambda$) e número de épocas.
3. **Particionamento Explícito 80/20 Sem Vazamento (*Zero Data Leakage*)**: Carregar/baixar o dataset clínico *Heart Disease* (`1025` pacientes, `13` atributos), particionar estratificadamente em **80% Treino (`820` amostras)** e **20% Teste (`205` amostras)**, e ajustar o padronizador (`StandardScaler` ou `MinMaxScaler`) exclusivamente sobre o conjunto de treino.
4. **Inspeção Visual e Numérica dos Pesos Sinápticos**: Exibir no grafo a espessura e cor das conexões proporcionais a $w_{ij}$, os valores numéricos dos pesos escritos sobre as arestas, mapas de calor (*heatmaps*) de $W^{(l)}$ e $\Delta W^{(l)}$ e tabela interativa de conexões, pesos e gradientes a cada época.

## 2. Arquitetura de Pastas do Subrepositório (`code/mlp/`)
* [`app.py`](app.py): Aplicação interativa em **Streamlit** para experimentação em tempo real.
* [`run_experiments.py`](run_experiments.py): Script reprodutível que executa o estudo de ablação (8 configurações `C0` a `C7`), salva as partições 80/20 e gera todas as figuras e métricas reais.
* [`REPORT.md`](REPORT.md): Relatório técnico completo (conceitos matemáticos, desenho da arquitetura, funcionamento do grafo e justificativa de otimização de hiperparâmetros).
* [`core_mlp/`](core_mlp/CONTEXT.md): Núcleo modular da rede neural (`graph.py`, `train.py`, `dataset.py`, `visualize.py`).
* [`data/`](data/CONTEXT.md): Dataset bruto (`heart.csv`) e partições explícitas padronizadas (`train_80_standardized.csv` e `test_20_standardized.csv`).
* [`figs/`](figs/CONTEXT.md): Figuras geradas pelo modelo (`arquitetura_diagrama.png`, `grafo_antes.png`, `grafo_depois.png`, `heatmap_pesos.png`, `heatmap_delta_pesos.png`, `curvas_convergencia.png`, `comparativo_configuracoes.png`).
* [`results/`](results/CONTEXT.md): Métricas tabulares (`benchmark_results.csv`, `benchmark_summary.json`, `best_model_synaptic_weights.csv`).
* [`report/`](report/CONTEXT.md): Relatório técnico em LaTeX compilado em PDF (`relatorio_mlp.pdf`).

## 3. Como Executar
```bash
# 1. Instalar dependências
pip install -r code/mlp/requirements.txt

# 2. Iniciar interface interativa Streamlit
streamlit run code/mlp/app.py

# 3. Reproduzir benchmark experimental e gerar figuras
py code/mlp/run_experiments.py
```
