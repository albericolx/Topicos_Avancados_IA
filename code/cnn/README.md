# Subrepositório CNN: Arquitetura, Reprodução e Modificações Inéditas (`code/cnn/`)

Este diretório contém a implementação completa do artefato **`[5] artefato · arquitetura git repo` (`arq·c`)** da disciplina de Tópicos Avançados de IA (UFRPE 2026.2).

## Resumo Rápido

* **Artigo Reproduzido:** *Empirical Ablation and Ensemble Optimization of a Convolutional Neural Network for CIFAR-10 Classification* (arXiv:2604.23861v1, 2026).
* **Dataset Oficial:** CIFAR-10 (25.000 imagens de treino / 5.000 de teste, balanceamento estrito de 2.500 e 500 imagens por classe).
* **Baseline Oficial:** 6 camadas convolucionais (32-32-64-64-128-128), 7 camadas de Batch Normalization, MaxPool a cada 2 convs, Dropout 0.3 a 0.5, Dense 128 (Total exato: 552.874 parâmetros).
* **3 Modificações Inéditas Propostas:**
  1. **Conexões Residuais (*Skip Connections* estilo ResNet)** nos blocos convolucionais duplos.
  2. **Data Augmentation** dinâmico (`RandomCrop 32` padding 4 + `RandomHorizontalFlip`).
  3. **Mecanismo de Atenção Squeeze-and-Excitation (*SE-Block*)** após os blocos de convolução.

## Guia de Execução

### 1. Inferência Funcional Imediata
Para testar a inferência comprovada sobre amostras reais do dataset:
```bash
python demo_inference.py
```
O script exibirá no terminal a predição para 10 amostras do teste e salvará o painel visual em `figs/amostras_inferencia.png`.

### 2. Pipeline de Reprodução e Treinamento
Para executar os treinamentos do baseline e das variantes arquiteturais:
```bash
python experiments.py
```
As curvas comparativas serão geradas em `figs/curvas_comparativas_ablation.png` e os resultados numéricos tabulados em `results/cnn_ablation_results.csv`.
