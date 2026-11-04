# exp · José Albérico Rocha da Silva

> folha do artefato [desenho dos experimentos](../3-desenho-dos-experimentos.md). siga o guia passo
> a passo e preencha cada seção aqui. as decisões são suas, e decidir é saber explicar.

## 0 · a minha ideia, e o que ficou para medir

**Sentinela Clandestino (Vigilante de Espelhos e APKs)** — Uma ferramenta de proteção na borda voltada a cidadãos e apostadores expostos a campanhas agressivas de bets clandestinas. Ao clicar em um link externo ou iniciar o download de um aplicativo fora da loja, o sistema aciona um pipeline híbrido na borda: um modelo de decisão rápida de Sistema 1 (*LAYA* open-source, < 35ms) faz a triagem probabilística imediata da landing page e do manifesto, cruzando metadados com um grafo de DNS passivo via agentes MCP, enquanto um SLM quantizado local (1B–3B) é despertado sob demanda para explicar cláusulas contratuais de saque retido. Em vez de uma censura cega, o sistema expõe evidências de golpe (risco de saque travado, malware espião e operadores laranjas), protegendo o patrimônio do usuário pelo seu próprio interesse de não ser roubado, sem violar sua privacidade e sem depender de listas estáticas ineficazes.

**o que eu medi no tec:** No smartphone Android (Samsung Galaxy A15, processador MediaTek Helio G99 ARM64, 4 GB de RAM), o Fast-Path LAYA concluiu a triagem inicial em **0,14 ms** (< 100 MB de RAM) e o SLM on-device (`Qwen2.5-0.5B-Instruct` INT4 via `llama.cpp`) executou inferência na CPU a **34,7 tokens/s no prompt** e **13,8 tokens/s na geração**, levando **18,75 ms** para diagnosticar o calote do rollover de 60x. A validação via Pydantic consumiu tempo residual (< 0,05 ms). A saída do modelo foi precisa na identificação do perigo financeiro, mas dependeu de vocabulário explícito, mostrando sensibilidade a termos dissimulados e jargões contratuais atípicos.

**o que o flx deixou para o experimento:** No § 4 do `flx`, a auditoria pesada do SLM on-device foi restrita ao modo sob demanda após a triagem rápida para poupar ciclos de processamento e bateria do celular. Falta medir empiricamente: (1) qual a taxa de falsos negativos críticos (o golpe de saque retido que passa calado sem aviso) em um conjunto diversificado de páginas com ofuscação adversarial (*cloaking* e DGA); (2) o impacto das ablações de arquitetura (remover o Fast-Path ou o SLM); e (3) se a exposição de evidências estruturadas de saque retido de fato induz o apostador a abortar o depósito financeiro com mais eficácia do que avisos genéricos de segurança.

## 1 · os experimentos e a comunidade de cada um

| exp. | a pergunta que ele responde | o que é testado: a técnica, uma pessoa usando, ou o nicho | a comunidade e os veículos | o experimento publicado que eu sigo (com link) |
|:--|:--|:--|:--|:--|
| E1 | O pipeline híbrido Fast-Path LAYA + Deep-Path SLM na CPU móvel detecta cláusulas abusivas de saque e espelhos de DGA com menos de 5% de falsos negativos críticos e latência < 35 ms? | a técnica na borda (acurácia semântica e eficiência em hardware restrito) | Segurança de Sistemas e Cibersegurança: ACM CCS, USENIX Security, IEEE S&P, NDSS | [Following Passive DNS Traces to Detect Malicious Domains](https://doi.org/10.1145/3401897) (Nabeel et al., ACM TOPS 2020) e [Text-Based Detection of Online Gambling Ads](https://doi.org/10.1109/ICISIT.2025.10842131) (Muzakir et al., IEEE ICISIT 2025): métricas de F1, Falso Negativo Crítico e latência em fluxos reais |
| E2 | A apresentação de evidências técnicas de saque retido e taxas PIX induz o apostador a abortar transações fraudulentas com mais eficácia do que avisos convencionais estáticos? | uma pessoa usando, num nicho de risco (apostadores expostos a links piratas) | Interação Humano-Computador (IHC) e Usabilidade de Segurança: ACM CHI, SOUPS, USENIX Security | [Alice in Warningland: A Large-Scale Field Study of Browser Security Warning Effectiveness](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/felt) (Felt et al., USENIX Security 2013): metodologia experimental comparando taxas de evasão e aderência perante avisos transparentes vs. genéricos |

## 2 · E1 · Detecção de Retenção de Saque e DGA na Borda

### 2.1 · hipótese, linhas de base e o número que derruba

**a hipótese:** Em um corpus de 40 termos contratuais e páginas de apostas (25 fraudulentas com rollover abusivo ou taxa prévia de PIX e 15 legítimas da Portaria SPA/MF ou e-commerce), o pipeline híbrido na borda apresenta **Falsos Negativos Críticos (golpes que passam sem aviso) $\le$ 5%** (no máximo 2 casos em 40) e **latência média de decisão $\le$ 35 ms** na CPU do smartphone.

**o jeito de hoje:** Lista negra estática de bloqueio de URLs (Anatel / Ministério da Fazenda). Falha categoricamente contra espelhos mutantes criados por DGA minutos antes da campanha (taxa de falso negativo de 100% contra novos domínios ativados no mesmo dia).

**o competidor mais forte:** Trend Micro Check (analisa links e capturas de tela via IA na nuvem). Não roda offline no piloto móvel local; em conexões 4G reais apresenta latência de 800 a 1.500 ms e taxa de falso negativo de ~25% perante páginas com cloaking e termos em modais dinâmicos.

**o número que derruba a hipótese:** Falsos negativos críticos $> 5\%$ (ou seja, mais de 2 plataformas de calote rotuladas como seguras) ou latência média do Fast-Path $> 35\text{ ms}$ no conjunto de 40 instâncias de teste.

**escrito antes de rodar:** Commit registrado no repositório antes da execução do piloto oficial.
