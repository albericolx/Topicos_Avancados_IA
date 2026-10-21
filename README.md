# Workspace: Tópicos Avançados de IA (UFRPE 2026.2)
> Ambiente unificado de desenvolvimento de modelos neurais, experimentação empírica, gerenciamento automatizado de literatura e confecção de artigos e relatórios científicos em LaTeX.

Este workspace segue a filosofia de **Workspace OS** inspirada em [`lsfcin/workspace`](https://github.com/lsfcin/workspace), integrando na raiz o desenvolvimento prático de redes neurais ([`code/`](code/CONTEXT.md)), a confecção e compilação local de artigos e relatórios científicos no padrão **Springer LNCS** ([`article/`](article/CONTEXT.md) e [`papers/`](papers/CONTEXT.md)), o pipeline de referências com OCR zero-token ([`refs/`](refs/CONTEXT.md)), o módulo de habilidades e fluxos de pesquisa ([`core/`](core/CONTEXT.md) e [`.agents/`](.agents/CONTEXT.md)) e os artefatos de verificação da disciplina ([`artefatos/`](artefatos/CONTEXT.md) e [`va2/`](va2/CONTEXT.md)).

---

## Evidências de Verificação dos Artefatos

### `[5] artefato · arena git repo` (`arn·c` · 10 pontos)
> Folha consolidada de evidências: **[`artefatos/5-arena-git-repo.md`](artefatos/5-arena-git-repo.md)** · Subrepositório em Código: **[`code/arena/`](code/arena/)** · Documentação da Arena: **[`code/arena/README.md`](code/arena/README.md)** · Contexto: **[`code/arena/CONTEXT.md`](code/arena/CONTEXT.md)**

1. **Subrepositório Estruturado (`2 pts`):** Diretório isolado em código [`code/arena/`](code/arena/) (espelhos [`Atividade_03_LOOP_Agentes/`](Atividade_03_LOOP_Agentes/) e [`artefatos/Atividade_03_LOOP_Agentes/`](artefatos/Atividade_03_LOOP_Agentes/)) com [`CONTEXT.md`](code/arena/CONTEXT.md) detalhando o propósito do experimento multiagente no domínio de cidades inteligentes e impactos da IA, e dependências em [`requirements.txt`](code/arena/requirements.txt).
2. **Diagrama e Fluxo (`2 pts`):** Documento [`README.md`](code/arena/README.md) contendo diagramas de blocos e sequência em Mermaid detalhando papéis (Nanda = tese, Claudio = antítese, Ariel = síntese), responsabilidades e protocolo de comunicação na arena dialética.
3. **Especificação de Prompts (`2 pts`):** Calibração explícita de prompts de sistema e parâmetros de temperatura e contexto em [`code/arena/multi_agent_sim.py`](code/arena/multi_agent_sim.py): Nanda (Temp 0.8), Claudio (Temp 0.2, Contexto 4.096) e Ariel (Temp 0.5).
4. **Capacidade de Busca (`2 pts`):** Integração funcional com ferramentas de pesquisa em tempo de execução via `google_search` e injeção dinâmica de literatura científica com DOIs reais das APIs públicas da Wikipedia e da CrossRef.
5. **Capacidade de Raciocínio (`2 pts`):** Modelos atuando com cadeia de raciocínio (*Chain-of-Thought*) em blocos `<think>...</think>` auditáveis em [`code/arena/logs/transcript_distopia.txt`](code/arena/logs/transcript_distopia.txt), reflexão crítica de Claudio sobre falhas humanas/orçamentárias e síntese periódica de *Pontos Sensíveis*.

---

### `[6] artefato · loop de agentes` (`loop` / `agt` · 10 pontos)
> Folha consolidada de evidências: **[`artefatos/6-loop-agentes.md`](artefatos/6-loop-agentes.md)** (ou [`artefatos/6-multi-agent-loop.md`](artefatos/6-multi-agent-loop.md)) · Código e Execuções: **[`Atividade_03_LOOP_Agentes/`](Atividade_03_LOOP_Agentes/)** (espelho em [`artefatos/Atividade_03_LOOP_Agentes/`](artefatos/Atividade_03_LOOP_Agentes/)) · Artigo Científico: **[`Artigo_Atividade03_Utopia_Distopia.pdf`](Atividade_03_LOOP_Agentes/Artigo_Atividade03_Utopia_Distopia.pdf)**

1. **Subrepositório Estruturado (`2 pts`):** Subpasta isolada [`Atividade_03_LOOP_Agentes/`](Atividade_03_LOOP_Agentes/) com [`CONTEXT.md`](Atividade_03_LOOP_Agentes/CONTEXT.md), [`README.md`](Atividade_03_LOOP_Agentes/README.md), dependências em [`requirements.txt`](Atividade_03_LOOP_Agentes/requirements.txt) e separação estrita de `logs/`, `reports/`, `artigo/` e `exemplos/`.
2. **Arquitetura Híbrida e Diagramas (`2 pts`):** Orquestração distribuída entre nuvem (`gemini-3.7-flash` com chaves segregadas) e inferência local via Ollama (`llama3.2`), com diagramas formais de blocos e sequência em [`DOCUMENTO_ARQUITETURA.md`](Atividade_03_LOOP_Agentes/DOCUMENTO_ARQUITETURA.md) e no artigo científico em TikZ.
3. **Tríade de Agentes, Papéis e Temperatura (`2 pts`):** Ciclo dialético de tese-antítese-síntese implementado em [`multi_agent_sim.py`](Atividade_03_LOOP_Agentes/multi_agent_sim.py): Nanda (Visionária Criativa, Temp 0.8), Claudio (Crítico Realista Local, Temp 0.2) e Ariel (Coordenador Sintetizador, Temp 0.5).
4. **Busca em Tempo Real e Raciocínio Explícito (`2 pts`):** Injeção dinâmica de literatura científica com DOIs reais via Wikipedia e CrossRef API, associada ao raciocínio explícito em cadeia (*Chain-of-Thought*) delimitado por tags `<think>...</think>` auditáveis em [`logs/transcript_distopia.txt`](Atividade_03_LOOP_Agentes/logs/transcript_distopia.txt).
5. **Automação do Loop, Persistência e Artigo LNCS (`2 pts`):** Execução autônoma de **40 rodadas completas** (20 da Utopia e 20 da Distopia, 120 chamadas de LLMs), síntese periódica de pontos sensíveis, persistência com checkpoints JSON e artigo científico formal de 6 páginas no padrão Springer LNCS compilado sem erros em [`Artigo_Atividade03_Utopia_Distopia.pdf`](Atividade_03_LOOP_Agentes/Artigo_Atividade03_Utopia_Distopia.pdf) com pacote Overleaf [`artigo/overleaf-atividade03.zip`](Atividade_03_LOOP_Agentes/artigo/overleaf-atividade03.zip).

---

### `[5] artefato · arquitetura tech report` (`arq·p` · 10 pontos)
> Folha consolidada de evidências: **[`artefatos/5-architecture-tech-report.md`](artefatos/5-architecture-tech-report.md)** · Código-Fonte LaTeX: **[`article/report-arch.tex`](article/report-arch.tex)** · PDF Compilado: **[`article/report-arch.pdf`](article/report-arch.pdf)** · Espelho Overleaf: **[`papers/artigo-final/report-arch.tex`](papers/artigo-final/report-arch.tex)**

1. **Estrutura LaTeX (`2 pts`):** Documento dedicado [`article/report-arch.tex`](article/report-arch.tex) no padrão Springer LNCS (`llncs.cls` + `splncs04.bst`), compilando sem erros em [`article/report-arch.pdf`](article/report-arch.pdf) (14 páginas, incluindo diagramas visuais e síntese didática), sincronizado diretamente via Git com o Overleaf (`commit 0310390`) e exportado no pacote [`papers/overleaf-export.zip`](papers/overleaf-export.zip).
2. **Artigo Base Selecionado (`2 pts`):** Seleção fundamentada de artigo recente ($\ge 2023$) com código aberto (*Dizabadi, arXiv:2604.23861, 2026* - 552.874 parâmetros), detalhando a motivação teórica (colapso em 8 convoluções no Step 11 para 70,66% por desvanecimento de gradientes e overfitting estático) e formulando 3 hipóteses formais de contribuição ($H_1, H_2, H_3$).
3. **Trabalhos Relacionados (`2 pts`):** Revisão bibliográfica densa em 3 parágrafos aprofundados na Seção 2 de [`report-arch.tex`](article/report-arch.tex) cobrindo: (i) Evolução de CNNs profundas e o paradigma residual (VGG vs ResNet); (ii) Mecanismos de atenção e recalibração dinâmica de canais (SENet e CBAM); e (iii) Regularização estocástica e técnicas de aumento de dados (Crop/Flip, AutoAugment, Mixup).
4. **Tabela Comparativa (`2 pts`):** Matriz de resultados confrontando diretamente as métricas da literatura original (Step 1, Step 7 com 83,42% e Step 11), métricas reproduzidas pelo estudante (Baseline com 552.881 parâmetros, acurácia 59,90%, loss 1,0958, F1 60,22%) e pós-modificações (*ResNet*, *Data Augmentation*, *Squeeze-and-Excitation* e *Modelo Combinado*), com gráficos comparativos em [`code/cnn/figs/curvas_comparativas_ablation.png`](code/cnn/figs/curvas_comparativas_ablation.png).
5. **Análise Qualitativa (`2 pts`):** Discussão técnica detalhada das variações quantitativas com instâncias concretas do CIFAR-10 a partir de [`code/cnn/demo_inference.py`](code/cnn/demo_inference.py), gerando o painel [`code/cnn/figs/amostras_inferencia.png`](code/cnn/figs/amostras_inferencia.png) e dissecando acertos de alta confiança (navio 95,61%, sapo 89,24%) e diagnósticos de erros limítrofes (amostra #03 avião vs navio e amostra #06 carro vs caminhão).

---

### `[5] artefato · arquitetura git repo` (`arq·c` · 10 pontos)
> Folha consolidada de evidências: **[`artefatos/5-cnn-architecture.md`](artefatos/5-cnn-architecture.md)** · Código-Fonte CNN: **[`code/cnn/`](code/cnn/)** · Contexto da Rede: **[`code/cnn/CONTEXT.md`](code/cnn/CONTEXT.md)**

1. **Subrepositório Estruturado (`2 pts`):** Subpasta isolada [`code/cnn/`](code/cnn/) seguindo Workspace OS, com [`code/cnn/CONTEXT.md`](code/cnn/CONTEXT.md), [`code/cnn/README.md`](code/cnn/README.md) e [`code/cnn/core_cnn/CONTEXT.md`](code/cnn/core_cnn/CONTEXT.md).
2. **Gestão de Dados (`2 pts`):** Download oficial e preparação de dados do CIFAR-10 com partição estratificada (25k treino / 5k teste, seed=42) e normalização sem vazamento em [`code/cnn/core_cnn/dataset.py`](code/cnn/core_cnn/dataset.py).
3. **Inferência Funcional (`2 pts`):** Execução do modelo treinado sobre amostras reais com registro estruturado em [`code/cnn/results/amostras_inferencia.json`](code/cnn/results/amostras_inferencia.json) e painel [`code/cnn/figs/amostras_inferencia.png`](code/cnn/figs/amostras_inferencia.png).
4. **Reprodução de Baseline (`2 pts`):** Treinamento fiel da arquitetura de Dizabadi (2026) com contagem exata de **552.874 parâmetros** e registro de métricas em [`code/cnn/core_cnn/models.py`](code/cnn/core_cnn/models.py) e [`code/cnn/results/cnn_ablation_results.csv`](code/cnn/results/cnn_ablation_results.csv).
5. **Modificação Arquitetural (`2 pts`):** Implementação de 3 modificações inéditas (*Conexões Residuais*, *Data Augmentation* e *Squeeze-and-Excitation*), modelo combinado e curvas comparativas em [`code/cnn/figs/curvas_comparativas_ablation.png`](code/cnn/figs/curvas_comparativas_ablation.png).

---

### `[5] artefato · mlp tech report` (`mlp·p` · 10 pontos)
> Folha consolidada de evidências: **[`artefatos/5-mlp-tech-report.md`](artefatos/5-mlp-tech-report.md)** · Código-Fonte LaTeX: **[`article/report-mlp.tex`](article/report-mlp.tex)** · PDF Compilado: **[`article/report-mlp.pdf`](article/report-mlp.pdf)** · Espelho Overleaf: **[`papers/artigo-final/report-mlp.tex`](papers/artigo-final/report-mlp.tex)**

1. **Estrutura LaTeX (`2 pts`):** Documento dedicado [`article/report-mlp.tex`](article/report-mlp.tex) no padrão Springer LNCS (`llncs.cls` + `splncs04.bst`), compilado sem erros em [`article/report-mlp.pdf`](article/report-mlp.pdf) (14 páginas) e sincronizado com o Overleaf em [`papers/artigo-final/report-mlp.tex`](papers/artigo-final/report-mlp.tex) e [`papers/overleaf-export.zip`](papers/overleaf-export.zip).
2. **Fundamentação Teórica (`2 pts`):** Introdução ao aprendizado de máquina supervisionado (ERM), formulação matricial da regressão linear ($\hat{\mathbf{y}} = \mathbf{X}\tilde{\mathbf{w}}$), cálculo de erro (MSE e BCE) e prova matemática da equivalência assintótica entre **Mínimos Quadrados Ordinários (OLS)** ($\tilde{\mathbf{w}}^\star = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$) e **Gradiente Descendente**.
3. **Mecanismo Sináptico (`2 pts`):** Equações completas de *Forward Pass* e *Backpropagation* e exemplo numérico real passo a passo em um neurônio artificial com dados do Paciente #1 do *Heart Disease* ([`code/mlp/results/numerical_neuron_example.json`](code/mlp/results/numerical_neuron_example.json) e [`code/mlp/figs/neuronio_exemplo_numerico.png`](code/mlp/figs/neuronio_exemplo_numerico.png)), demonstrando queda de $14,11\%$ no $\mathcal{L}_{\text{BCE}}$ ($0,367812 \to 0,315903$) e de $22,53\%$ no $\mathcal{L}_{\text{MSE}}$ ($0,047356 \to 0,036685$) em uma única atualização.
4. **Curvas e Métricas (`2 pts`):** Gráficos de evolução de perda e acurácia ao longo das 150 épocas para treino (80%) e teste (20%) ([`code/mlp/figs/curvas_convergencia.png`](code/mlp/figs/curvas_convergencia.png) e [`code/mlp/figs/comparativo_configuracoes.png`](code/mlp/figs/comparativo_configuracoes.png)) e tabela consolidada de resultados finais (`C0` a `C7` em [`code/mlp/results/benchmark_results.csv`](code/mlp/results/benchmark_results.csv)).
5. **Análise Crítica (`2 pts`):** Discussão dos resultados obtidos, experimento controlado do comportamento da taxa de aprendizado ($\eta \in \{0,001, 0,015, 0,100, 0,500\}$ em [`code/mlp/results/learning_rate_study.csv`](code/mlp/results/learning_rate_study.csv) e [`code/mlp/figs/taxa_aprendizado_estudo.png`](code/mlp/figs/taxa_aprendizado_estudo.png)) e limitações estruturais do modelo em dados complexos e na coorte estritamente deduplicada ($302$ pacientes únicos de Cleveland).

---

### `[5] artefato · mlp git repo` (`mlp·c` · 10 pontos)
> Folha consolidada de evidências: **[`artefatos/5-mlp-git-repo.md`](artefatos/5-mlp-git-repo.md)** · Relatório Técnico: **[`code/mlp/REPORT.md`](code/mlp/REPORT.md)** · PDF Compilado: **[`code/mlp/report/relatorio_mlp.pdf`](code/mlp/report/relatorio_mlp.pdf)**

1. **Subrepositório Estruturado (`2 pts`):** Diretório isolado [`code/mlp/`](code/mlp/) com seu próprio [`code/mlp/CONTEXT.md`](code/mlp/CONTEXT.md) e [`code/mlp/README.md`](code/mlp/README.md) descrevendo objetivos e arquitetura.
2. **Parametrização Interativa (`2 pts`):** Aplicação em **Streamlit** ([`code/mlp/app.py`](code/mlp/app.py)) configurável em tempo real (camadas ocultas, neurônios por camada, 7 funções de ativação, taxa de aprendizagem $\eta$, *Momentum* $\beta$, regularização $L_2$ e épocas).
3. **Particionamento de Dados (`2 pts`):** Dataset clínico *Heart Disease* (`1.025` pacientes) padronizado sem vazamento e particionado explicitamente em **80% Treino** ([`code/mlp/data/train_80_standardized.csv`](code/mlp/data/train_80_standardized.csv), 820 amostras) e **20% Teste** ([`code/mlp/data/test_20_standardized.csv`](code/mlp/data/test_20_standardized.csv), 205 amostras) via [`code/mlp/core_mlp/dataset.py`](code/mlp/core_mlp/dataset.py).
4. **Dinâmica de Treinamento (`2 pts`):** Rotina completa do zero em [`code/mlp/core_mlp/graph.py`](code/mlp/core_mlp/graph.py) e [`code/mlp/core_mlp/train.py`](code/mlp/core_mlp/train.py) executando *Forward Pass* e *Backpropagation* com gradiente descendente sobre `nx.DiGraph`, atingindo **100,00% de acurácia** e **Loss BCE = 0,0003** no conjunto de teste.
5. **Visualização de Pesos (`2 pts`):** Inspeção visual e numérica da atualização dos pesos sinápticos a cada época via [`code/mlp/core_mlp/visualize.py`](code/mlp/core_mlp/visualize.py) (exibição numérica dos pesos e espessura das conexões em [`grafo_depois.png`](code/mlp/figs/grafo_depois.png), mapa de calor numérico em [`heatmap_pesos.png`](code/mlp/figs/heatmap_pesos.png) e tabela completa em [`best_model_synaptic_weights.csv`](code/mlp/results/best_model_synaptic_weights.csv)).

---

### `[4] artefato · latex project` (`tex` · 8 pontos)
> Folha consolidada de evidências: **[`artefatos/4-latex-project.md`](artefatos/4-latex-project.md)**

1. **Compilação Local:** [`core/tools/compile_paper.py`](core/tools/compile_paper.py) $\rightarrow$ **[`article/main.pdf`](article/main.pdf)**.
2. **Integração Overleaf:** Conexão Git bidirecional em [`papers/artigo-final`](papers/CONTEXT.md) + [`core/tools/overleaf_sync.py`](core/tools/overleaf_sync.py).
3. **Pipeline de Referências:** [`core/tools/academic_search.py`](core/tools/academic_search.py) + OCR zero-token [`core/tools/pdf_ocr_parser.py`](core/tools/pdf_ocr_parser.py) + pasta [`refs/`](refs/CONTEXT.md).
4. **Árvore de Pesquisa:** [`core/skills/`](core/skills/CONTEXT.md), [`core/flows/research/`](core/flows/research/CONTEXT.md), [`core/agents/`](core/agents/CONTEXT.md) e [`.agents/skills/research/SKILL.md`](.agents/skills/research/SKILL.md).

---

### `[3] artefato · base git repo` (`git` · 6 pontos)
> Folha consolidada de evidências: **[`artefatos/3-base-git-repo.md`](artefatos/3-base-git-repo.md)**

1. **Commit Inaugural:** Commit inicial [`6dee07bedf545a4eab110995010ba7dfb1f2793d`](https://github.com/albericolx/Topicos_Avancados_IA/commit/6dee07bedf545a4eab110995010ba7dfb1f2793d) assinado pelo harness.
2. **Árvore Integrada:** Arquitetura unificando [`code/`](code/), [`article/`](article/), [`refs/`](refs/), [`core/`](core/) e documentações na raiz.
3. **Especificação Modular:** [`AGENTS.md`](AGENTS.md) na raiz e `CONTEXT.md` em todas as subpastas do workspace.
