# Subrepositório da Rede Neural Multicamadas (`code/mlp/CONTEXT.md`)
> Implementação do zero (*from scratch*) de uma Rede Neural Multicamadas (MLP) sobre Grafo Direcionado (`NetworkX DiGraph` + `NumPy`), com interface interativa em `Streamlit`, particionamento explícito 80/20 e visualização de pesos sinápticos a cada época — **`[5] artefato · mlp git repo` (`mlp·c`)**.

## 1. Objetivos do Subrepositório
1. **Desmistificar a Caixa-Preta Neural**: Implementar todas as operações matemáticas de *Forward Pass*, *Backpropagation* e *Gradiente Descendente* (com suporte a *Momentum* e regularização $L_2$) diretamente sobre os nós e arestas de um grafo direcionado `nx.DiGraph`, sem uso de frameworks de diferenciação automática (como PyTorch ou TensorFlow).
2. **Parametrização Interativa em Tempo Real ([`app.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/app.py))**: Permitir configurar dinamicamente no painel lateral do Streamlit o número de camadas ocultas (1 a 4), quantidade de neurônios por camada, função de ativação (`ReLU`, `Leaky ReLU`, `Tanh`, `Sigmoide`, `ELU`, `SELU`, `ReLU6`), taxa de aprendizagem ($\eta$), decaimento de LR, *Momentum* ($\beta$), regularização $L_2$ ($\lambda$) e número de épocas.
3. **Particionamento Explícito 80/20 Sem Vazamento (*Zero Data Leakage*)**: Carregar/baixar o dataset clínico *Heart Disease* (`1.025` pacientes, `13` atributos), particionar estratificadamente em **80% Treino (`820` amostras)** e **20% Teste (`205` amostras)**, e ajustar o padronizador (`StandardScaler` ou `MinMaxScaler`) exclusivamente sobre o conjunto de treino.
4. **Inspeção Visual e Numérica dos Pesos Sinápticos**: Exibir no grafo a espessura e cor das conexões proporcionais a $w_{ij}$, os valores numéricos dos pesos escritos sobre as arestas, mapas de calor (*heatmaps*) de $W^{(l)}$ e $\Delta W^{(l)}$ e tabela interativa de conexões, pesos e gradientes a cada época.

## 2. Arquitetura de Pastas e Arquivos do Subrepositório (`code/mlp/`)
* [`README.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/README.md): Visão geral ilustrada do subrepositório.
* [`REPORT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/REPORT.md): Relatório técnico completo em Markdown (conceitos, tabelas de atributos e funções de ativação, desenho da arquitetura, funcionamento do grafo, estudo de ablação `C0`–`C7`, interpretabilidade clínica dos pesos, dinâmica no Streamlit e conclusão).
* [`app.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/app.py): Aplicação interativa em **Streamlit** para experimentação em tempo real.
* [`run_experiments.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/run_experiments.py): Script reprodutível que executa o estudo de ablação (`C0` a `C7`), salva as partições 80/20 e gera todas as figuras e métricas reais.
* [`core_mlp/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/code/mlp/core_mlp) ([`core_mlp/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/core_mlp/CONTEXT.md)): Núcleo modular da rede neural ([`graph.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/core_mlp/graph.py), [`train.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/core_mlp/train.py), [`dataset.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/core_mlp/dataset.py), [`visualize.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/core_mlp/visualize.py)).
* [`data/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/code/mlp/data) ([`data/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/data/CONTEXT.md)): Dataset bruto ([`heart.csv`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/data/heart.csv)) e partições explícitas padronizadas ([`train_80_standardized.csv`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/data/train_80_standardized.csv) e [`test_20_standardized.csv`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/data/test_20_standardized.csv)).
* [`figs/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/code/mlp/figs) ([`figs/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/figs/CONTEXT.md)): Figuras geradas pelo modelo (`arquitetura_diagrama.png`, `grafo_antes.png`, `grafo_depois.png`, `heatmap_pesos.png`, `heatmap_delta_pesos.png`, `curvas_convergencia.png`, `comparativo_configuracoes.png`).
* [`results/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/code/mlp/results) ([`results/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/results/CONTEXT.md)): Métricas tabulares ([`benchmark_results.csv`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/results/benchmark_results.csv), [`benchmark_summary.json`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/results/benchmark_summary.json), [`best_model_synaptic_weights.csv`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/results/best_model_synaptic_weights.csv)).
* [`report/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/code/mlp/report) ([`report/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/report/CONTEXT.md)): Relatório técnico em LaTeX compilado em PDF ([`relatorio_mlp.pdf`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/mlp/report/relatorio_mlp.pdf)).

## 3. Como Executar
```bash
# 1. Instalar dependências
pip install -r code/mlp/requirements.txt

# 2. Iniciar interface interativa Streamlit
streamlit run code/mlp/app.py

# 3. Reproduzir benchmark experimental e gerar figuras
py code/mlp/run_experiments.py
```
