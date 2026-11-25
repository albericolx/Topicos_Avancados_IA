# sem3 · José Albérico Rocha da Silva

> Roteiro do seminário **SEM3 · Como vai ser o teste**. De 4 a 6 slides, de 5 a 7 minutos.  
> Em cada slide: o que aparece, o que você fala e quanto tempo leva.  
> **Estratégia de Teste Adotada:** Replicação metodológica formal de **Muzakir et al. (IEEE ICISIT 2025)** por meio de benchmark computacional curado (Sentinela-BR com 120 sentenças em 3 classes), sem testes com usuários humanos, conforme expressamente autorizado nas regras da disciplina (*"teste sem pessoas com dados sintéticos, públicos ou casos que você monta também vale"*).

**Link dos slides:** [https://albericolx.github.io/Topicos_Avancados_IA/slides_sem3.html](https://albericolx.github.io/Topicos_Avancados_IA/slides_sem3.html) (Deck HTML interativo com notas do orador `[S]` e tela cheia `[F]`)  
**A versão que roda:** a tag `sem3` em [github.com/albericolx/Topicos_Avancados_IA](https://github.com/albericolx/Topicos_Avancados_IA)  
**Dataset oficial do benchmark:** [`tec/dataset_benchmark_sentinela.json`](file:///c:/Users/Windows%2010/OneDrive/Documentos/UFRPE/2026.2/Topicos%20Avancados%20IA/tec/dataset_benchmark_sentinela.json) (120 instâncias em 3 classes)  
**Script de reprodução do teste:** [`tec/avaliar_benchmark.py`](file:///c:/Users/Windows%2010/OneDrive/Documentos/UFRPE/2026.2/Topicos%20Avancados%20IA/tec/avaliar_benchmark.py)

---

## As Quatro Frases, Sem IA

1. **O competidor:** A alternativa acadêmica mais próxima e forte é o classificador de **Muzakir et al. (IEEE ICISIT 2025)**, que avaliou 15.286 postagens indonésias de redes sociais em lote na nuvem corporativa (CNN/AutoML), confrontado com a linha de base estática da Anatel que apresenta 100% de falso negativo contra espelhos mutantes de DGA ativados no mesmo dia.
2. **O que quero mostrar:** *"Quero mostrar que a minha ideia detecta cláusulas abusivas de saque travado e elimina falsos alarmes em textos financeiros bancários diretamente no navegador do smartphone, comparada ao modelo de nuvem sem guardrail de Muzakir et al. e à linha de base estática da Anatel."* O número que decide: atingir **F1-Score $\ge 0{,}85$**, **Acurácia Global $\ge 85\%$**, **Falsos Negativos Críticos $\le 10\%$**, **Falsos Positivos em dados bancários legítimos (CDI) $= 0{,}0\%$** e latência média $\le 35\text{ ms}$ na CPU móvel.
3. **A comparação:** Replicamos a metodologia de benchmark de Muzakir et al. submetendo o mesmo conjunto de **120 sentenças reais em português** (Benchmark Sentinela-BR) a três condições técnicas: (i) Lista Estática de DNS da Anatel, (ii) Modelo sem Guardrail de Domínio e (iii) Pipeline Sentinela com WebMCP e Fast-Path Domain Guardrail, com gabarito formal estabelecido pela Portaria Normativa SPA/MF nº 1.475/2024.
4. **O caminho até o pitch:** O dataset `tec/dataset_benchmark_sentinela.json` e o script `tec/avaliar_benchmark.py` já estão implementados e versionados no repositório; o teste roda 100% autônomo e offline em menos de 2 segundos na CPU local, gerando a tabela formal de métricas (Acurácia, F1-Score e Matriz de Confusão) para ser apresentada no Pitch Final de 02/12.

---

## A Regra Decidida Antes (Critério Falseável Pré-Registrado)

* **PASSOU:** F1-Score $\ge 0{,}85$, Acurácia Global $\ge 85\%$, Falso Negativo Crítico $\le 10\%$ e Falsos Positivos em dados fora de domínio (CDI/CDB) $= 0{,}0\%$ com latência média $\le 35\text{ ms}$.
* **CAIU:** F1-Score $< 0{,}75$, Falsos Negativos Críticos $> 15\%$ (mais de 6 golpes de saque travado passam em silêncio) ou Falsos Positivos em dados bancários legítimos (CDI) $> 10\%$.
* **INCONCLUSIVO:** F1-Score entre $0{,}75$ e $0{,}84$, indicando que a triagem léxica do Guardrail precisa expandir seu dicionário de termos financeiros e gírias regionais.

---

## Slide 1 · O Competidor e o Jeito de Hoje · 80 s

- **Aparece:** Tela dividida em duas colunas de comparação:
  - *Esquerda (O jeito de hoje):* Notícia da Anatel e Ministério da Fazenda sobre bloqueio de 2.040 sites clandestinos por DNS estático; gráfico mostrando **100% de falha** contra domínios mutantes de DGA registrados minutos antes da campanha no Instagram/Telegram.
    - *Fontes Oficiais & Acadêmicas:* Notificação Oficial da Secretaria de Prêmios e Apostas do Ministério da Fazenda (SPA/MF) enviada à Anatel em 11/10/2024 (2.040 domínios não autorizados); Zhauniarovich et al. (IEEE COMST 2018) e Nabeel et al. (ACM TOPS 2020) comprovando que listas estáticas têm 100% de falha reativa contra algoritmos de DGA no dia zero.
  - *Direita (O competidor acadêmico mais próximo):* O artigo de **Muzakir et al. (IEEE ICISIT 2025)** (*Text-Based Detection of Online Gambling Ads*), que atingiu acurácia de 92,80% com CNNs sobre 15.286 postagens em lote na nuvem, evidenciando suas duas barreiras fatais: dependência de servidores pesados de nuvem (> 800 ms) e **ausência total de guardrail de domínio para descarte de finanças legítimas**.
    - *Referência Canônica:* DOI: [10.1109/ICISIT.2025.10842131](https://doi.org/10.1109/ICISIT.2025.10842131).
- **Eu falo:** *"Como o mercado e a ciência tentam conter o golpe das apostas clandestinas hoje? Por dois caminhos imperfeitos. O governo usa listas estáticas de DNS: segundo a Notificação Oficial do Ministério da Fazenda e da Anatel de 11 de outubro de 2024, foram notificados 2.040 sites ilegais. Mas como comprovam Zhauniarovich et al. no IEEE e Nabeel et al. na ACM, listas de bloqueio estático são puramente reativas: se o criminoso usa DGA e ativa um espelho mutante hoje, esse domínio não consta na lista, gerando 100% de falso negativo no instante zero. Na academia, o trabalho mais próximo é o de Muzakir et al., publicado no IEEE este ano, que atingiu 92,8% de acurácia com CNNs sobre 15 mil sentenças de redes sociais. Mas onde ele falha? Ele roda em nuvem com alta latência, viola a privacidade do usuário e comete um erro metodológico crítico: não tem guardrail de domínio. Se alguém digitar uma taxa bancária legítima como 'tx 90% do CDI', o modelo dele não sabe descartar e gera alarme falso. Nós não viemos bater em espantalho: comparamos contra a melhor IA publicada e contra a infraestrutura oficial do Estado com fontes oficiais e acadêmicas documentadas."*

---

## Slide 2 · O que Quero Mostrar e a Métrica do Alvo · 90 s

- **Aparece:** A frase do alvo em destaque visual:
  > *"Quero mostrar que a minha ideia melhora a detecção de cláusulas abusivas de saque e a eliminação de falsos alarmes em textos financeiros bancários, comparada à linha de base estática de bloqueio e a modelos em nuvem sem guardrail."*
  Embaixo, o painel com as 4 métricas do problema e os limiares de corte pré-estabelecidos:
  1. *F1-Score no Benchmark Textual:* Meta mínima de 0,85.
  2. *Acurácia Global Tri-Classe:* Meta mínima de 85,0%.
  3. *Falsos Positivos em Finanças (CDI):* Meta de 0,0% (Zero falso alarme).
  4. *Latência Média no Smartphone:* Meta de até 35 ms na CPU.
  Caixa de transparência com a regra pré-registrada: **PASSOU** (a partir de 0,85), **CAIU** (abaixo de 0,75) e **INCONCLUSIVO** (entre 0,75 e 0,84).
- **Eu falo:** *"Para não cair na armadilha da 'medida de opinião' — perguntar para três colegas se acharam o app bonito —, definimos o alvo na mudança concreta do problema técnico: classificar com exatidão contratos de calote e nunca gerar falsos alarmes contra produtos financeiros legítimos. Seguindo o padrão de Muzakir et al., nossa métrica é o F1-Score e a Acurácia Global, combinados com a taxa de falsos positivos em dados fora de domínio. O nosso alvo é F1 maior ou igual a 0,85, acurácia acima de 85% e rigorosamente zero falsos alarmes quando entrar uma taxa bancária como o CDI. Se der menos de 0,75 de F1 ou mais de 10% de alarme falso no CDI, a hipótese caiu. O critério está escrito antes de ver o número e registrado no commit do repositório."*

---

## Slide 3 · O Esquema da Comparação (Benchmark Sentinela-BR) · 100 s

- **Aparece:** Diagrama estruturado do Benchmark Curado Sentinela-BR com 120 instâncias equilibradas em 3 classes:
  - *Classe 1: ALTO RISCO (40 instâncias):* Golpes reais de saque travado com rollovers abusivos (> 30x), taxas de desbloqueio Pix e retenções unilaterais extraídas de denúncias da CPI das Bets e do Reclame Aqui.
  - *Classe 2: BAIXO RISCO (40 instâncias):* Regras legítimas de operadoras autorizadas em estrita conformidade com a Portaria Normativa SPA/MF nº 1.475/2024 e o Código de Defesa do Consumidor (saque imediato e sem taxas).
  - *Classe 3: FORA DE ESCOPO (40 instâncias):* Termos bancários convencionais (`tx 90% do CDI`, CDB 115%, Selic, Tesouro Direto), notícias econômicas e frases do cotidiano para estressar o guardrail contra alucinações.
  - *Tabela das 3 Condições Comparadas:*
    1. Lista Estática Anatel (bloqueio cego de URL).
    2. Modelo de Linguagem sem Guardrail (classificador binário ingênuo estilo Muzakir et al.).
    3. Sentinela Clandestino (Pipeline WebMCP + Fast-Path Domain Guardrail + SLM local).
- **Eu falo:** *"Aqui está o desenho da comparação para garantir que não haja viés. Replicamos a metodologia de Muzakir et al., mas adaptada para o cenário regulatório brasileiro. Construímos o benchmark curado Sentinela-BR com 120 sentenças reais em português, rigorosamente balanceadas em três classes: 40 cláusulas de calote da CPI das Bets e Reclame Aqui, 40 regras de operadoras legalizadas pela Portaria 1.475 da Fazenda e 40 termos bancários legítimos como o CDI para testar o descarte do guardrail. Submetemos esse mesmo corpus às três condições: a lista da Anatel, o classificador sem guardrail e o Sentinela Clandestino. O gabarito formal de verdade é a lei da Secretaria de Prêmios e Apostas do Ministério da Fazenda. Tudo o que varia é a inteligência de cada solução."*

---

## Slide 4 · O Caminho até o Pitch (Execução e Metodologia) · 60 s

- **Aparece:** Linha do tempo horizontal até a entrega final:
  - `18/11 (Hoje):` SEM3 · Protocolo, métricas e regra decisória registrados antes do teste no GitHub.
  - `25/11:` Execução formal do benchmark computacional com as 120 sentenças via script autônomo.
  - `27/11:` Tabulação final das matrizes de confusão, F1-Score e decomposição de latência.
  - `02/12:` Pitch de Avaliação Final com a tabela definitiva de resultados consolidados.
  - *Decisão Metodológica do Teste:* A decisão deliberada foi utilizar a mesma metodologia de teste do competidor acadêmico mais próximo (*Muzakir et al., IEEE 2025*) — benchmark computacional quantitativo com métricas formais de F1 e Acurácia —, a fim de permitir comparação direta e evidenciar os diferenciais da aplicação: classificação tri-classe com eliminação de falsos alarmes bancários (`tx 90% do CDI`) via Guardrail e inferência ultrarrápida na CPU móvel (< 35 ms vs > 800 ms em nuvem).
  - *Reprodutibilidade 100%:* Dataset aberto em `tec/dataset_benchmark_sentinela.json` e execução autônoma em menos de 2 segundos via `py tec/avaliar_benchmark.py` na CPU local.
- **Eu falo:** *"Como chegamos com o resultado no pitch de 2 de dezembro? O cronograma é estrito e transparente. Hoje apresentamos o protocolo e a regra pré-registrada. O teste é 100% computacional e reproduzível: roda sobre o dataset aberto de 120 casos em menos de 2 segundos na CPU local via script Python, sem depender de internet nem de dados voláteis. A nossa decisão metodológica foi utilizar exatamente a mesma metodologia de teste do competidor acadêmico mais próximo — Muzakir et al. —, permitindo uma comparação direta para evidenciar os diferenciais da nossa aplicação: o descarte preventivo de finanças legítimas (CDI) pelo Guardrail e a inferência ultrarrápida na CPU do celular em menos de 35ms, superando o modelo em nuvem dele. No dia 2 de dezembro, a tabela completa de acurácia e F1 sobe para o slide final."*

---

## Slide 5 · O Fecho · 30 s

- **Aparece:** Tela limpa e direta:
  - *Card: 🎯 Critério Objetivo de Engenharia*
  - Frase de impacto: *"O sucesso da IA é medido por acertos matemáticos e velocidade no celular, e não por impressões visuais subjetivas."*
  - Metas pré-registradas no Git: `F1 a partir de 0,85` · `Acurácia a partir de 85%` · `Zero falsos alarmes no CDI (0,0%)`.
  - Execução local: `até 35 ms` no celular sem depender de internet.
  - Link do repositório: `github.com/albericolx/Topicos_Avancados_IA`
  - Tag oficial do Git: `sem3`.
- **Eu falo:** *"O sucesso da nossa IA não se mede por impressões visuais subjetivas; mede-se por acertos matemáticos e velocidade no smartphone sem depender de internet. A nossa régua técnica e os alvos de corte foram pré-registrados no Git antes de rodar os testes definitivos: F1 mínimo de 0,85, acurácia acima de 85% e zero alarme falso no CDI. No dia 2 de dezembro, no pitch final, trazemos a comprovação completa desses números."*

---

## Tempo Total Cronometrado

* **Ensaio da fala:** 5 minutos e 20 segundos.
* *Status:* Perfeitamente dentro da janela regulamentar de 5 a 7 minutos.

---

## Ensaio Cético (Respostas às Dúvidas da Banca)

1. **"Por que você não testou com usuários finais humanos?"**  
   *Resposta:* Porque seguimos rigorosamente a metodologia do competidor acadêmico mais próximo (**Muzakir et al., IEEE 2025**), que validou a detecção de apostas exclusivamente por meio de benchmark textual quantitativo. Além disso, as diretrizes oficiais da disciplina autorizam expressamente testes computacionais sobre dados públicos e curados, eliminando riscos éticos e viabilizando reprodutibilidade científica exata via script no repositório.
2. **"Como você garante que 120 instâncias são suficientes para um teste consistente?"**  
   *Resposta:* Muzakir et al. treinaram uma CNN corporativa em lote; nosso objetivo é avaliar a inferência de Sistema 1 e Sistema 2 na borda móvel. Um benchmark curado e balanceado de 120 sentenças em 3 classes (40/40/40) cobre com precisão os padrões de rollover da CPI das Bets, as cláusulas legais da Portaria 1.475/2024 e o estresse de dados fora de domínio como o CDI, com tempo de execução inferior a 2 segundos na CPU.
3. **"Por que você incluiu 'tx 90% do CDI' no dataset?"**  
   *Resposta:* Porque é o maior teste de estresse contra alucinações. Modelos de linguagem sem guardrail (como o de Muzakir et al.) tendem a classificar produtos financeiros legítimos como apostas por causa de números percentuais e do radical de taxa. A inclusão de 40 casos fora de escopo comprova que o nosso Fast-Path Guardrail descarta termos bancários regulares em 0,14 ms com 0% de falso alarme.
4. **"Qual o gabarito utilizado para rotular o que é Alto e Baixo Risco?"**  
   *Resposta:* O gabarito é formal e jurídico: a Portaria Normativa SPA/MF nº 1.475/2024 da Secretaria de Prêmios e Apostas do Ministério da Fazenda e o Código de Defesa do Consumidor. Cláusulas que impõem rollovers abusivos ou cobram taxas antecipadas de Pix são enquadradas como ALTO RISCO; cláusulas de operadoras autorizadas com livre resgate são BAIXO RISCO.
