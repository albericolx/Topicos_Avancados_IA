# Módulo de Redes Neurais Convolucionais (`code/cnn/`)

Este subrepositório implementa o artefato **`[5] artefato · arquitetura git repo` (`arq·c` · 10 pontos)** da disciplina de Tópicos Avançados em IA (UFRPE 2026.2), seguindo os padrões do **Workspace OS** e convenções modulares.

## Artigo Base e Benchmark
* **Artigo Científico Base:** *Empirical Ablation and Ensemble Optimization of a Convolutional Neural Network for CIFAR-10 Classification* (arXiv:2604.23861v1, Abril de 2026).
* **Autor:** Naser Khatti Dizabadi (The University of Tulsa).
* **Benchmark:** Dataset canônico **CIFAR-10** (Krizhevsky, 2009) — 10 classes, imagens 32×32×3 RGB.
* **Protocolo Experimental do Artigo:** 25.000 amostras balanceadas de treino (2.500/classe) e 5.000 de teste (500/classe).

## Arquitetura Baseline Oficial (Seção 3.2 do Artigo)
* **6 Camadas Convolucionais:** 32, 32, 64, 64, 128 e 128 filtros $3 \times 3$ com padding 1.
* **7 Camadas de Batch Normalization:** após cada convolução e após a camada densa intermediária.
* **Max-Pooling:** janela $2 \times 2$ após cada bloco duplo de convolução.
* **Dropout:** taxas de 0.3, 0.5, 0.5 nas convoluções e 0.5 na camada densa.
* **Camada Densa:** 128 neurônios com ativação ReLU, antes da camada de classificação final de 10 logits.
* **Total Exato de Parâmetros:** **552.874 parâmetros** (551.722 treináveis + 1.152 buffers de BN).

---

## 3 Modificações Arquiteturais Inéditas Implementadas

Nenhuma das modificações abaixo foi testada nos 17 passos avaliados pelo artigo original:

### 1. Conexões Residuais (*Skip Connections* estilo ResNet)
* **Conceito:** Introduz caminhos diretos de fluxo de informação somando a entrada do bloco duplo convolucional à sua saída antes da ativação final: $y = \mathcal{F}(x) + \mathcal{W}_s x$. Para blocos onde o número de canais é expandido ($3 \to 32$, $32 \to 64$, $64 \to 128$), aplica-se uma projeção linear de convolução $1 \times 1$ com Batch Normalization.
* **Por que foi escolhida:** No artigo original, ao aumentar a profundidade ou alterar kernels de forma indiscriminada (Passos 8 e 9), a acurácia despencou de 79.5% para **70.66%**, evidenciando atenuação e degradação de gradientes. O artigo cita o trabalho seminal de He et al. (ResNet, 2016) mas nunca implementa conexões residuais na arquitetura convolucional direta.
* **Efeito esperado:** Alívio no problema de desvanecimento de gradientes em camadas profundas, estabilização dos pesos e aceleração da convergência nos estágios iniciais de treinamento.

### 2. Regularização por Aumento de Dados (*Data Augmentation*)
* **Conceito:** Aplicação dinâmica de transformações espaciais estocásticas durante o ciclo de treino: `RandomCrop(32, padding=4)` com espelhamento horizontal estocástico (`RandomHorizontalFlip(p=0.5)`).
* **Por que foi escolhida:** Todas as curvas de perda apresentadas nas Figuras 1 a 15 do artigo mostram um distanciamento acentuado entre a curva de treino ($\sim 95\%$) e teste ($\sim 80\%$), denotando *overfitting* marcante decorrente da ausência de aumentação de dados.
* **Efeito esperado:** Redução drástica do gap de generalização entre treino e validação, forçando a rede a aprender representações invariantes a translações e inversões espaciais de objetos no CIFAR-10.

### 3. Mecanismo de Atenção Squeeze-and-Excitation (*SE-Block*)
* **Conceito:** Mecanismo leve de atenção canal a canal (Hu et al., CVPR 2018). Executa um *squeeze* espacial via Global Average Pooling ($\mathbb{R}^{C \times H \times W} \to \mathbb{R}^C$) seguido de uma excitação não-linear via MLP com gargalo (fator de redução $r=16$) e sigmoid, recalibrando adaptativamente as respostas dos canais: $\tilde{X} = X \odot \sigma(\mathbf{W}_2 \text{ReLU}(\mathbf{W}_1 z))$.
* **Por que foi escolhida:** As convoluções padrão tratam todos os mapas de características igualmente. No CIFAR-10, certos canais detectam texturas de fundo irrelevantes enquanto outros capturam contornos fundamentais (asas de aviões, rodas de automóveis). O artigo não explora nenhum mecanismo atencional.
* **Efeito esperado:** Aumento no poder de representação da rede com um custo quase imperceptível de parâmetros ($\sim +0.7\%$), permitindo suprimir canais ruidosos e destacar filtros discriminativos.

---

## Estrutura do Módulo

```text
code/cnn/
├── CONTEXT.md                    # Documentação contextual e especificações formais
├── README.md                     # Guia de execução e resumo do subrepositório
├── core_cnn/                     # Módulos Python estruturados
│   ├── CONTEXT.md                # Especificação dos módulos internos
│   ├── dataset.py                # Gestão de dados oficial do CIFAR-10 (25k/5k estratificado)
│   ├── models.py                 # Baseline e as 3 variantes arquiteturais + modelo combinado
│   └── train.py                  # Rotinas de treino, inferência e métricas multimétricas
├── demo_inference.py             # Script de inferência funcional com amostras reais
├── experiments.py                # Pipeline automatizado de ablação e reprodução
├── data/                         # CIFAR-10 baixado e conferido
├── figs/                         # Gráficos de loss, acurácia e inferência amostral
└── results/                      # Checkpoints (.pth), tabelas CSV e sumários JSON
```

## Como Executar

1. **Inferência Funcional (Ponto de Verificação 3):**
   ```bash
   py demo_inference.py
   ```
2. **Execução do Treinamento e Estudo de Ablação (Pontos de Verificação 4 e 5):**
   ```bash
   py experiments.py
   ```
