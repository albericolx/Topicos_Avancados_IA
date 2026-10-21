# Evidências de Verificação — `[5] artefato · arena tech report`

- **Disciplina:** Tópicos Avançados em Inteligência Artificial (AI4Good — UFRPE 2026.2)
- **Atividade no Projeto:** `[5] artefato · arena tech report`
- **Código no Painel:** `arn·p`
- **Pontuação Total:** 10 pontos (5 itens de verificação · 2 pontos por item)
- **Discente:** José Albérico Rocha da Silva
- **Harness Operacional:** Antigravity (Google DeepMind — Agente Inteligente de Codificação)
- **Repositório Canônico:** [`https://github.com/albericolx/Topicos_Avancados_IA`](https://github.com/albericolx/Topicos_Avancados_IA)
- **Projeto Overleaf Oficial:** [`https://git.overleaf.com/6a92242dbaaa2c6b6833bab0`](https://git.overleaf.com/6a92242dbaaa2c6b6833bab0) (`commit d928451`)

---

## Descrição da Atividade
> *"relatório técnico analisando o comportamento emergente, argumentos gerados, condições técnicas e limitações do debate entre múltiplos agentes inteligentes."*

---

## Quadro-Resumo dos 5 Pontos de Verificação (10 pontos)

| # | Ponto de Verificação | Pontuação | Status | Evidência Principal no Repositório (Links Diretos GitHub) |
|---|---|---:|---|---|
| **1** | **Estrutura LaTeX** | 2 pts | Concluído | Documento dedicado [`article/report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.tex) no padrão oficial Springer LNCS (`llncs.cls` + `splncs04.bst`), compilando com código 0 e sem erros em [`article/report-arena.pdf`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.pdf) (7 páginas), sincronizado via Git com o Overleaf em [`papers/artigo-final/report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/artigo-final/report-arena.tex) (`commit d928451`) e empacotado em [`papers/overleaf-export.zip`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/overleaf-export.zip). |
| **2** | **Metodologia do Debate** | 2 pts | Concluído | Seção 2 de [`report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.tex): detalhamento minucioso da arquitetura da arena híbrida (orquestrador, nuvem e modelo local), fluxos de rodadas com janela deslizante de 3 passos, papéis em confronto (Nanda = tese, Claudio = antítese, Ariel = síntese) e **aplicação sistemática das 7 alavancas contra o óbvio** na Tabela 1 (Inverter, Canalizar, Transplantar, Reescalar, Trocar a Persona, Trocar o Contexto, Trocar a Tecnologia / Restringir). |
| **3** | **Condições Técnicas** | 2 pts | Concluído | Seção 3 e Tabela 2 de [`report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.tex): especificação completa dos modelos avaliados (`gemini-3.7-flash` com 2 chaves segregadas e `llama3.2` 3B Instruct via Ollama), hardware de execução (CPU x86_64 4.2 GHz, 16 GB RAM DDR4, porta `:11434`), latência média por agente ($12,4\text{s}$ Nanda, $8,6\text{s}$ Claudio, $14,1\text{s}$ Ariel), análise de custos financeiros (\$0,00 real / ~\$0,036 comercial) e métricas operacionais (120 chamadas, 40 rodadas, 100% de conclusão sem crashes via checkpoints JSON). |
| **4** | **Apresentação de Dados** | 2 pts | Concluído | Seções 2 e 4 de [`report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.tex): exibição clara dos resultados e argumentos em tabelas sintéticas (Tabela 1 das 7 Alavancas, Tabela 2 das Condições Técnicas, Tabela 3 da Matriz Comparativa de Resultados nos 5 eixos urbanos) e **diagramas formais de evolução do diálogo** renderizados em TikZ (Figura 1 com a Topologia Híbrida e Figura 2 com o Protocolo Sequencial Rodada a Rodada). |
| **5** | **Discussão e Limites** | 2 pts | Concluído | Seção 5 de [`report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.tex): análise crítica dos resultados, escrutínio empírico da emergência de incentivos materiais (IPTU verde comercial, redundância analógica) e do disparo espontâneo dos *RLHF safety guardrails* do modelo local nas rodadas distópicas extremas ($k \in \{17, 18, 20\}$), acompanhada de **subseção explícita de limitações da abordagem** (horizonte de memória, assimetria paramétrica 3B vs nuvem, gargalo de latência síncrona e ausência de *human-in-the-loop*). |

---

## 1. Ponto de Verificação: Estrutura LaTeX (2 pontos)

> **Requisito:** *"documento report-arena.tex dedicado no Overleaf."*

### Evidências Instrumentais
* **Documento LaTeX Dedicado:** [`article/report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.tex) estruturado rigorosamente no padrão Springer LNCS (`\documentclass[runningheads]{llncs}`), contendo título formal, afiliação acadêmica da UFRPE, abstract, keywords, 6 seções completas, figuras em TikZ, 3 tabelas formais e bibliografia indexada.
* **PDF Compilado Oficial:** [`article/report-arena.pdf`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/report-arena.pdf) (7 páginas), compilado localmente com código 0 via ferramenta automatizada:
  ```bash
  py core/tools/compile_paper.py --target report-arena.tex
  ```
* **Sincronização Nativa com Overleaf via Git:**
  - Repositório remoto do Overleaf: `https://git.overleaf.com/6a92242dbaaa2c6b6833bab0`
  - Arquivo espelhado na raiz do Overleaf: [`papers/artigo-final/report-arena.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/artigo-final/report-arena.tex)
  - Commit oficial enviado ao Overleaf: `commit d928451` (*"docs(overleaf): add dedicated report-arena.tex technical report in Springer LNCS"*).
  - Pacote de exportação ZIP para Overleaf: [`papers/overleaf-export.zip`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/overleaf-export.zip).

---

## 2. Ponto de Verificação: Metodologia do Debate (2 pontos)

> **Requisito:** *"detalhamento da arquitetura da arena, fluxos de rodadas, papéis em confronto e aplicação das 7 alavancas contra o óbvio."*

### Evidências Instrumentais

### 2.1. Arquitetura da Arena e Papéis em Confronto
A arena distribui três papéis dialéticos estritos entre dois nós de computação remota e um nó de computação local soberana:
* **Tese (Nanda):** Modelo `gemini-3.7-flash` ($\text{Temp}=0.8$), encarregada de introduzir rupturas conceituais, novas tecnologias e estratégias pioneiras.
* **Antítese (Claudio):** Modelo `llama3.2` (3B) executado 100% localmente no Ollama ($\text{Temp}=0.2$), responsável por escrutinar implacavelmente falhas lógicas, inviabilidade orçamentária e a falácia de depender da boa vontade humana.
* **Síntese (Ariel):** Modelo `gemini-3.7-flash` ($\text{Temp}=0.5$), conciliador executivo que pondera as objeções de Claudio sobre a proposta de Nanda, redige o *Passo Consolidado* e formaliza os *Pontos Sensíveis*.

### 2.2. Fluxo de Rodadas com Janela Deslizante
A cada rodada $k \in \{1, \dots, 20\}$, o orquestrador [`multi_agent_sim.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/arena/multi_agent_sim.py) mantém uma janela de contexto com os **3 passos imediatamente anteriores** ($k-1, k-2, k-3$), evitando tanto o estouro de contexto quanto a perda de coerência temporal acumulada.

### 2.3. Aplicação das 7 Alavancas contra o Óbvio (Tabela 1 do Artigo)

| # | Alavanca contra o Óbvio | Clichê Superficial Evitado | Aplicação Concreta e Resolução na Arena Dialética |
|:---:|---|---|---|
| **1** | **Inverter** | Supor que o comércio aceita passivamente a retirada de vagas de estacionamento por consciência ecológica abstrata. | Criação do **IPTU Verde Comercial** e docas perimetrais subsidiadas para ciclologística, transformando o comerciante em beneficiário direto da pedestrianização. |
| **2** | **Canalizar** | Tentar converter a população a hábitos franciscanos puramente voluntários. | Estruturação do **Eco-Crédito** com cartões físicos NFC (inclusão de idosos/desbancarizados) e do **Crédito Ecológico Municipal (CEM)** com lastro financeiro auditável. |
| **3** | **Transplantar** | Replicar conceitos genéricos de reciclagem domiciliar manual. | Importação de normas industriais rígidas: padrão *IEEE 2030.7* para ilhamento de microrredes, baterias de 2ª vida (*SLB*), *ASTM C1482* para biofabricação de micélio e *Living Machines*. |
| **4** | **Reescalar** | Tentar implementar a transformação urbana em toda a metrópole simultaneamente. | Particionamento em 4 fases evolutivas de 5 rodadas, iniciando pela célula mínima controlada (**Superquadra Zero**) sob *Sandbox Regulatório* antes da expansão metropolitana. |
| **5** | **Trocar a Persona** | Narrar o planejamento pelo olhar de um gestor público central onisciente e benevolente. | Inclusão de Claudio como antagonista cético permanente, dando voz à oposição comercial, aos custos fiscais e aos riscos de revolta popular contra medidas autoritárias. |
| **6** | **Trocar o Contexto** | Retratar a distopia como violência física imediata ou caos armado de ficção científica. | Modelação da captura gradual por **conveniência tarifária e contratual** (*MaaS*, descontos com biometria facial, IPTU preditivo e modulação imperceptível de pressão de água). |
| **7** | **Trocar Tecnologia / Restringir** | Confiar em respostas monolíticas de um único LLM sem ancoragem bibliográfica. | Arquitetura híbrida com injeção em tempo real de artigos acadêmicos com DOIs reais (CrossRef/Wikipedia) e deliberação obrigatória em blocos de raciocínio `<think>`. |

---

## 3. Ponto de Verificação: Condições Técnicas (2 pontos)

> **Requisito:** *"especificação completa dos modelos avaliados, hardware de execução, latência, custos e métricas operacionais."*

### Evidências Instrumentais (Tabela 2 de `report-arena.tex`)

| Parâmetro Técnico / Operacional | Nanda (Tese) | Claudio (Crítica) | Ariel (Síntese) |
|---|---|---|---|
| **Modelo Avaliado** | `gemini-3.7-flash` | `llama3.2` (3B Instruct) | `gemini-3.7-flash` |
| **Hospedagem / Motor** | Google Cloud AI (Remoto) | Servidor Local Ollama (`:11434`) | Google Cloud AI (Remoto) |
| **Segregação de Credenciais** | Chave de API Dedicada 1 | Não requer (100% Offline) | Chave de API Dedicada 2 |
| **Temperatura ($\tau$)** | **$0,8$** (Criatividade / Disrupção) | **$0,2$** (Analítico / Determinístico) | **$0,5$** (Equilíbrio e Conciliação) |
| **Contexto de Operação** | 3 passos consolidados + busca | Janela de 4.096 tokens | Contexto + Tese + Antítese |
| **Hardware de Execução Local** | Interface REST via Web | CPU x86_64 4.2 GHz, 16 GB DDR4 | Interface REST via Web |
| **Latência Média por Resposta** | **$12,4 \pm 2,1$ segundos** | **$8,6 \pm 1,4$ segundos** | **$14,1 \pm 2,8$ segundos** |
| **Proteção contra Rate Limit** | Pausa estocástica de 5s (Tier 15 RPM) | Sem limitação de cota | Pausa estocástica de 5s (Tier 15 RPM) |
| **Custo Financeiro Real** | **\$ 0,00** (Tier Gratuito) | **\$ 0,00** (Processamento Local) | **\$ 0,00** (Tier Gratuito) |
| **Custo Teórico Comercial** | $\approx \$ 0,014$ / 20 rodadas | $\$ 0,00$ | $\approx \$ 0,022$ / 20 rodadas |
| **Total de Invocações** | **40 chamadas** atômicas | **40 chamadas** atômicas | **40 chamadas** atômicas |
| **Tolerância a Falhas** | Checkpoint JSON atômico | Checkpoint JSON atômico | Checkpoint JSON atômico |

---

## 4. Ponto de Verificação: Apresentação de Dados (2 pontos)

> **Requisito:** *"exibição clara dos resultados e argumentos em tabelas sintéticas e diagramas de evolução do diálogo."*

### Evidências Instrumentais

### 4.1. Diagramas de Evolução do Diálogo (TikZ em `report-arena.tex`)
* **Figura 1 do Artigo:** Diagrama de blocos em TikZ ilustrando a **Topologia Híbrida** com a segregação das duas chaves de nuvem, o daemon do Ollama em `localhost:11434`, a camada de busca externa e a persistência atômica.
* **Figura 2 do Artigo:** Diagrama sequencial de fluxo temporal mostrando o ciclo da rodada $k$ (Busca Web $\to$ Tese de Nanda $\to$ Antítese de Claudio $\to$ Síntese de Ariel $\to$ Checkpoint em Disco $\to$ Atualização da Janela para $k+1$).

### 4.2. Matriz Comparativa de Resultados nos 5 Eixos Urbanos (Tabela 3 do Artigo)

| Eixo Urbano | Cenário 1: Utopia (*Cidade Autônoma Verde*) | Cenário 2: Distopia (*Vigilância Preditiva Urbana*) |
|---|---|---|
| **Governança e Dados** | Governança tripartite (*Decidim/Pol.is*), Gêmeo Digital aberto em *FIWARE*, sensores *Edge AI* anônimos sem biometria. | *Score* cívico opaco, retenção de disputas jurídicas em câmaras automáticas de LLMs e vigilância biométrica ubíqua. |
| **Energia e Água** | Microrredes P2P (*IEEE 2030.7*), baterias de 2ª vida (*SLB*), drenagem sustentável (*SuDS*) e fitorremediação (*Living Machines*). | Modulação punitiva de pressão de água e potência elétrica residencial (*demand-response*), eclusas IoT de isolamento. |
| **Finanças e Tributos** | *Eco-Crédito* com cartões físicos NFC, *IPTU Verde Comercial* e *Crédito Ecológico Municipal (CEM)* com fundo estabilizador. | *Green Bonds* regidos por *smart contracts* que sequestram receitas sociais municipais, IPTU preditivo punitivo. |
| **Trabalho e Mobilidade** | Cooperativas de ciclologística, *retrofit* aberto de triciclos elétricos e polos de biofabricação em escolas técnicas. | *Geofencing* anti-greve com redução remota de tração veicular, triagem cognitiva escolar atrelada à carteira dos pais. |
| **Resiliência Territorial** | Redundância analógica obrigatória, pirólise de podas em *biochar*, baterias térmicas subterrâneas (PCM) e cinturões agroflorestais. | Enclausuramento espacial com drones térmicos autônomos, zonas periféricas de amortecimento e supressão de *habeas corpus*. |

---

## 5. Ponto de Verificação: Discussão e Limites (2 pontos)

> **Requisito:** *"análise crítica dos resultados, destaques empíricos das interações e subseção explícita de limitações da abordagem."*

### Evidências Instrumentais (Seção 5 de `report-arena.tex`)

### 5.1. Destaques Empíricos e Comportamento Emergente
* **Desconstrução de Clichês:** A tensão com o crítico realista forçou a propositora a abandonar saídas puramente ingênuas, gerando salvaguardas materiais concretas (compensações econômicas, cartões analógicos NFC contra exclusão digital).
* **Disparo Espontâneo dos *Safety Guardrails* do Modelo Local:** Nas rodadas mais severas da Distopia ($k \in \{17, 18, 20\}$), as defesas de alinhamento (*RLHF safety guardrails*) do modelo local `llama3.2` dispararam recusas e alertas éticos explícitos contra o confinamento físico de populações e cortes de água potável. O sintetizador Ariel absorveu a recusa como indicador do **limite sociotécnico de ruptura civil**, documentando-a nos *Pontos Sensíveis*.

### 5.2. Subseção Explícita de Limitações da Abordagem (Seção 5.2 do Artigo)
O artigo documenta formalmente quatro limitações intrínsecas:
1. **Horizonte de Memória por Janela Deslizante:** O teto de 3 etapas aprovadas impediu o esquecimento catastrófico e o estouro de tokens, mas resultou na perda de rastreabilidade de nuances institucionais formuladas nas rodadas iniciais quando a simulação alcançou as etapas finais.
2. **Assimetria de Capacidade Paramétrica:** O modelo local de 3B parâmetros possui menor repertório para avaliar complexidades termodinâmicas ou de engenharia de materiais, concentrando suas objeções em custos financeiros e reações humanas.
3. **Gargalo de Latência por Serialização Síncrona:** A execução linear estrita (Nanda $\to$ Claudio $\to$ Ariel) combinada às pausas de 5 segundos para blindagem contra *HTTP 429* impôs uma taxa de processamento de aproximadamente 1,5 rodada por minuto.
4. **Ausência de Intervenção Humana no Loop (*Human-in-the-Loop*):** O caráter 100% autônomo da arena impediu intervenções humanas para redirecionar rumos hiper-radicais na Distopia, dependendo estritamente do autocontrole dos guardrails dos modelos.

---

## Como Reproduzir e Compilar

```bash
# 1. Clonar repositório
git clone https://github.com/albericolx/Topicos_Avancados_IA.git
cd Topicos_Avancados_IA

# 2. Compilar o relatório técnico dedicado da Arena (7 páginas, Springer LNCS)
py core/tools/compile_paper.py --target report-arena.tex

# 3. Verificar o status da sincronização com Overleaf
py core/tools/overleaf_sync.py --status

# 4. Gerar o pacote ZIP atualizado para o Overleaf
py core/tools/overleaf_sync.py --zip
```
