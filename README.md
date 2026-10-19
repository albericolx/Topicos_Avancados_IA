# Workspace: Tópicos Avançados de IA (UFRPE 2026.2)
> Ambiente unificado de desenvolvimento de modelos neurais, experimentação empírica, gerenciamento automatizado de literatura e confecção de artigos e relatórios científicos em LaTeX.

Este workspace segue a filosofia de **Workspace OS** inspirada em [`lsfcin/workspace`](https://github.com/lsfcin/workspace), integrando na raiz o desenvolvimento prático de redes neurais ([`code/`](code/CONTEXT.md)), a confecção e compilação local de artigos e relatórios científicos no padrão **Springer LNCS** ([`article/`](article/CONTEXT.md) e [`papers/`](papers/CONTEXT.md)), o pipeline de referências com OCR zero-token ([`refs/`](refs/CONTEXT.md)), o módulo de habilidades e fluxos de pesquisa ([`core/`](core/CONTEXT.md) e [`.agents/`](.agents/CONTEXT.md)) e os artefatos de verificação da disciplina ([`artefatos/`](artefatos/CONTEXT.md) e [`va2/`](va2/CONTEXT.md)).

---

## Evidências de Verificação dos Artefatos

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
