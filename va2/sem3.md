# sem3 · José Albérico Rocha da Silva

> roteiro do [seminário · iteração 3, como vai ser o teste](../4-seminario-como-vai-ser-o-teste.md). de 4 a 6 slides, de 5 a 7
> minutos. em cada slide: o que aparece, o que você fala e quanto tempo leva. hoje ainda não tem resultado final: tem a regra, decidida antes.

**link dos slides:** [https://albericolx.github.io/Topicos_Avancados_IA/slides_sem3.html](https://albericolx.github.io/Topicos_Avancados_IA/slides_sem3.html) (Deck HTML interativo com notas do orador `[S]` e tela cheia `[F]`)

**a versão que roda:** a tag `sem3` em [github.com/albericolx/Topicos_Avancados_IA](https://github.com/albericolx/Topicos_Avancados_IA) (branch `main` / `gh-pages`)

**o protótipo web de teste:** [https://albericolx.github.io/Topicos_Avancados_IA/](https://albericolx.github.io/Topicos_Avancados_IA/)

---

## as quatro frases, sem IA

1. **o competidor:** a alternativa acadêmica mais forte é o classificador em nuvem de **Muzakir et al. (IEEE ICISIT 2025)**, que obteve acurácia de 92,80% e F1 de 0,91 sobre 15.286 textos indonésios em servidores com GPU, confrontado com a linha de base estática da Anatel que apresenta 100% de falso negativo contra espelhos mutantes de DGA ativados no mesmo dia.
2. **o que quero mostrar:** *"quero mostrar que a minha ideia melhora a detecção de cláusulas abusivas de saque e a eliminação de falsos alarmes em textos financeiros para apostadores e cidadãos expostos a links piratas, comparada à linha de base estática de bloqueio e a modelos em nuvem sem guardrail."* O número que decide: atingir **F1-Score $\ge 0{,}85$**, **Falsos Negativos Críticos $\le 10\%$**, **Falsos Positivos em dados fora de domínio (CDI/CDB) $= 0\%$** com latência $\le 35\text{ ms}$ na CPU do smartphone, e no teste de usuário elevar a **Taxa de Aborto da Transação (TAR) para $\ge 65\%$** (superando em pelo menos 30 pontos o aviso genérico de 33,3%).
3. **a comparação:** no teste de bancada entram **120 sentenças reais em português** (40 de Alto Risco da CPI das Bets e Reclame Aqui, 40 de Baixo Risco da Portaria SPA/MF 1.475/2024 e 40 Fora de Escopo com CDI, CDB e notícias), e no teste de intervenção entram **30 participantes humanos**; ambas as condições recebem exatamente o mesmo texto contratual e a mesma tela de confirmação Pix, com gabarito formal estabelecido pela Portaria Normativa SPA/MF nº 1.475/2024.
4. **o caminho até o pitch:** o cliente WebMCP e os scripts de bancada já estão validados no GitHub Pages; a execução do teste ocorre no dia **25/11 em sala de aula** com os voluntários e o dataset; no dia **27/11** consolidamos os intervalos de confiança (Wilson 95% e F1), levando a tabela final para o **Pitch de 02/12**; como plano B, o teste roda 100% offline via script local na CPU sem depender de internet da universidade.

---

## a regra decidida antes (critério falseável no commit)

* **PASSOU:** F1-Score $\ge 0{,}85$, Falso Negativo Crítico $\le 10\%$, Falso Positivo em dados fora de domínio (CDI/CDB) $= 0\%$ no hardware móvel, e Taxa de Aborto da Transação (TAR) com evidências $\ge 65\%$ (superando o aviso genérico em $\ge 25$ pontos percentuais).
* **CAIU:** Falso Negativo Crítico $> 15\%$ (mais de 6 golpes de saque travado passam em silêncio) ou Taxa de Aborto da Transação $< 50\%$ (o usuário ignora os alertas com evidências tanto quanto ignora os avisos genéricos de segurança).
* **INCONCLUSIVO:** Taxa de Aborto entre $50\%$ e $64\%$ ou F1-Score entre $0{,}75$ e $0{,}84$, indicando que a explicabilidade técnica reduz o calote mas a variabilidade individual exige ampliar o tamanho amostral no estudo longitudinal.

---

## slide 1 · o competidor e o jeito de hoje · 80 s

- **aparece:** tela dividida em duas colunas de comparação:
  - *Esquerda (O jeito de hoje):* Notícia da Anatel e Ministério da Fazenda sobre bloqueio de 2.040 sites clandestinos por DNS estático; gráfico mostrando **100% de falha** contra domínios mutantes de DGA registrados minutos antes da campanha no Instagram/Telegram.
  - *Direita (O competidor acadêmico mais próximo):* O artigo de **Muzakir et al. (IEEE ICISIT 2025)**: *Text-Based Detection of Online Gambling Ads* com acurácia de 92,80% em 15.286 postagens na Indonésia, evidenciando suas duas barreiras fatais: dependência de servidores pesados de nuvem (> 800 ms) e **ausência total de testes com usuários reais e sem guardrail de domínio**.
- **eu falo:** "como o mercado e a ciência tentam conter o golpe das apostas clandestinas hoje? por dois caminhos imperfeitos. o governo usa listas estáticas de DNS: a Anatel já derrubou mais de 2.000 sites, mas os operadores criminosos usam algoritmos de DGA que geram espelhos mutantes (.xyz, .top) a cada duas horas. para novos domínios ativados no mesmo dia, a taxa de falha da lista estática é de rigorosamente 100%. na academia, o trabalho mais próximo é o de Muzakir et al., publicado no IEEE este ano, que atingiu 92,8% de acurácia com CNNs sobre 15 mil sentenças de redes sociais. mas onde ele falha? ele roda em nuvem com alta latência, viola a privacidade do usuário e comete um erro metodológico crítico: não tem guardrail de domínio. se alguém digitar uma taxa bancária legítima, ele não sabe descartar. e pior: Muzakir avaliou zero usuários humanos. nós não viemos bater em espantalho: comparamos contra a melhor IA publicada e contra a infraestrutura oficial do Estado."

---

## slide 2 · o que quero mostrar e a métrica do alvo · 90 s

- **aparece:** a frase do alvo em destaque visual:
  > *"Quero mostrar que a minha ideia melhora a detecção de cláusulas de saque retido e a eliminação de falsos alarmes em textos financeiros para apostadores e cidadãos expostos a links piratas, comparada à linha de base estática de bloqueio e a modelos em nuvem sem guardrail."*
  Embaixo, o painel com as 3 métricas do problema e os limiares de corte pré-estabelecidos:
  1. *F1-Score no Benchmark Textual:* Alvo $\ge 0{,}85$.
  2. *Falsos Positivos em Finanças/OOD (`tx 90% do CDI`):* Alvo $= 0{,}0\%$.
  3. *Taxa de Aborto do Pix Fraudulento (TAR):* Alvo $\ge 65{,}0\%$ (ganho $\ge +25$ p.p. sobre o aviso genérico de 33,3%).
  Caixa de transparência com a regra: **PASSOU** ($\ge 65\%$), **CAIU** ($< 50\%$) e **INCONCLUSIVO** ($50\%\text{--}64\%$).
- **eu falo:** "para não cair na armadilha da 'medida do gosto' — perguntar para três colegas se acharam o app bonito —, definimos o alvo na mudança concreta para a vítima: impedir que ela faça o Pix para o golpista. a nossa métrica não é satisfação; é a Taxa de Aborto da Transação (TAR) inspirada no estudo clássico de Felt et al. da USENIX Security. o aviso genérico de navegador ('site suspeito') é ignorado por 66% das pessoas por reflexo. quero provar que, ao exibir as evidências contratuais de saque travado — como o rollover de 60x ou a taxa de 20% —, pelo menos 65% dos usuários desistem do depósito. no benchmark textual, o alvo é F1 maior que 0,85 e rigorosamente zero falsos positivos em dados bancários legítimos como o CDI. se der menos de 50% de desistência, a hipótese caiu e meu sistema é tão inútil quanto os avisos que já existem. o critério está escrito antes do teste e registrado no commit do repositório."

---

## slide 3 · o esquema da comparação · 100 s

- **aparece:** diagrama de fluxo experimental bipartido:
  - *Trilha 1: Benchmark Computacional Sentinela-BR (120 Casos):*
    - 40 instâncias de **Alto Risco** (Rollover > 30x, taxas Pix da CPI das Bets e Reclame Aqui).
    - 40 instâncias de **Baixo Risco** (Regras autorizadas da Portaria SPA/MF 1.475/2024).
    - 40 instâncias de **Fora de Escopo** (CDI, CDB, Tesouro, notícias econômicas e culinária).
  - *Trilha 2: Intervenção com Usuários (30 Participantes - Protocolo E2):*
    - Amostra equilibrada: apostadores habituais e não-apostadores.
    - Três condições aleatorizadas (Latin Square): Condição A (Aviso Genérico do Navegador), Condição B (Bloqueio Cego / Gamban) e Condição C (Sentinela com Evidências de Saque Travado).
  - *O que fica rigorosamente igual:* O texto literal da cláusula, o valor do Pix (R$ 50) e o dispositivo de teste.
  - *Gabarito Jurídico:* Portaria Normativa SPA/MF nº 1.475/2024 e Código de Defesa do Consumidor.
- **eu falo:** "aqui está o desenho da comparação para garantir que não haja viés. na trilha de engenharia de IA, montamos o benchmark curado Sentinela-BR com 120 cláusulas e sentenças reais em português: 40 golpes de calote da CPI e do Reclame Aqui, 40 termos legais da Portaria 1.475 da Fazenda e 40 casos fora de escopo para estressar o guardrail contra alucinações. submetemos esse mesmo corpus a três condições: a lista da Anatel, o SLM sem guardrail e o Sentinela Clandestino. na trilha humana, 30 voluntários universitários avaliam cenários de pagamento com a mesma interface e o mesmo valor de Pix, alternando entre aviso genérico, bloqueio cego e o alerta com evidências do Sentinela. o gabarito de verdade é a lei da Secretaria de Prêmios e Apostas do Ministério da Fazenda. tudo o que varia entre os grupos é o tipo de proteção recebida."

---

## slide 4 · o caminho até o pitch (calendário e ética) · 60 s

- **aparece:** linha do tempo horizontal até a entrega final:
  - `18/11 (Hoje):` SEM3 · Protocolo, métricas e regra decisória registrados antes do teste no GitHub.
  - `25/11:` Execução do teste em sala de aula (coleta de decisões no smartphone e benchmark de 120 casos).
  - `27/11:` Tabulação dos dados, cálculo de significância estatística e intervalos de Wilson a 95%.
  - `02/12:` Pitch de Avaliação Final com a tabela definitiva de resultados consolidados.
  - `04/12:` Entrega da versão final do Artigo Científico Springer LNCS.
  - *Selo de Conformidade Ética:* Exercício de ensino sem identificação pessoal amparado pela Resolução CNS nº 510/2016 (art. 1º, parágrafo único, VIII) com TCLE formal arquivado em `va2/tcle.md`.
  - *Plano B:* Script Python e runtime WebMCP 100% offline em CPU/NPU local (imune a falhas de Wi-Fi da universidade).
- **eu falo:** "como chegamos com o resultado no pitch de 2 de dezembro? o cronograma é estrito. hoje, dia 18, apresentamos o protocolo e a regra pré-registrada. no dia 25, executamos a coleta dos dados em sala de aula com os voluntários usando a nossa aplicação web via WebMCP no próprio celular. no dia 27, rodamos os scripts de inferência estatística com intervalos de Wilson a 95% para checar se a diferença é real ou ruído amostral. no dia 2 de dezembro, a tabela de resultados sobe para o slide do pitch. e na ética? seguimos a Resolução CNS 510 para pesquisas de ensino: participação voluntária, termo curto oral e escrito, e zero coleta de CPF, nome ou telemetria. se o Wi-Fi da UFRPE cair no dia 25? o nosso plano B já está compilado: a bateria de 120 casos roda 100% offline na CPU local via script Python em 8 segundos."

---

## slide 5 · o fecho · 30 s

- **aparece:** tela limpa e direta:
  - *"Um teste não mede opinião; mede se o calote foi evitado."*
  - Metas decididas: `F1 >= 0,85` · `Falsos Positivos CDI = 0,0%` · `Taxa de Aborto >= 65,0%`.
  - QR Code e Link de Acesso Público: `albericolx.github.io/Topicos_Avancados_IA`
  - Tag oficial do Git: `sem3` no repositório GitHub.
- **eu falo:** "um teste de verdade não mede se o usuário achou o aplicativo bonito; mede se a tecnologia evitou que ele perdesse dinheiro num golpe de aposta clandestina. a nossa regra está decidida antes do número. no dia 25 de novembro, em sala, rodamos a prova real para o pitch final."

---

## tempo total cronometrado

* **Ensaio 1:** 5 min 45 s
* **Ensaio 2:** 6 min 10 s
* *Status:* Perfeitamente dentro da janela regulamentar de 5 a 7 minutos.

---

## ensaio cético (banca adversária)

As cinco perguntas mais difíceis elaboradas na simulação cética de banca, respondidas de cabeça com base no projeto:

1. **"A sua medida é a do problema ou só de usabilidade?"**  
   *Resposta:* É a medida direta do problema financeiro. Usabilidade mede se a tela é intuitiva ou se o botão é agradável. O que medimos é a **Taxa de Aborto da Transação (TAR)**: o número de pessoas que deixam de confirmar a transferência Pix de R$ 50 para o fraudador ao ver o aviso técnico de que o saque não será liberado. É a métrica de contenção do golpe.
2. **"A comparação é justa, ou você comparou a sua IA com uma lista estática defasada de propósito para ganhar fácil?"**  
   *Resposta:* A comparação é rigorosamente justa porque inclui **dois competidores reais**: a lista oficial da Anatel/Fazenda (que é o que o Estado usa de fato) e o modelo de aprendizado profundo de **Muzakir et al. (IEEE 2025)**, que é o melhor estado da arte acadêmico. Mostramos que o modelo de Muzakir tem ótima acurácia em texto bruto, mas perde para o Sentinela na borda móvel porque não possui guardrail de domínio e não opera em menos de 35ms no celular.
3. **"Como você garante que o teste com 120 casos e 30 pessoas cabe até 25/11 sem estourar o prazo da disciplina?"**  
   *Resposta:* O script de bancada já está implementado e otimizado no repositório (`va2/piloto_exp.py`), rodando as 120 sentenças em **menos de 10 segundos** na CPU. Já a aplicação com os 30 voluntários utiliza a nossa interface web publicada no GitHub Pages com simulação de 1 toque: cada participante leva menos de 3 minutos para responder aos 3 cenários no celular. O teste todo cabe em uma única aula de laboratório.
4. **"Por que você incluiu 'tx 90% do CDI' no dataset? Isso não é facilidade para inflar a sua acurácia?"**  
   *Resposta:* Pelo contrário: é o teste de estresse mais difícil para um modelo de linguagem pequeno (0.5B). No SEM2, modelos sem guardrail alucinavam e marcavam produtos de investimento legítimos como 'alto risco de aposta'. A inclusão de 40 casos fora de escopo (CDI, CDB, culinária e notícias) serve exatamente para penalizar a ferramenta caso ela gere falsos alarmes e atrapalhe a rotina de quem não joga.
5. **"Se o seu teste com usuários der 'inconclusivo' (ex: 55% de taxa de aborto), o seu projeto fracassou?"**  
   *Resposta:* Não. Inconclusivo é um resultado cientificamente honesto e pré-estabelecido. Ele comprovará que a evidência de saque retido melhora a taxa de desistência frente aos 33% do aviso genérico, mas demonstrará que o viés de impulsividade do apostador exige fricções adicionais de atrito (como confirmação em duas etapas) para atingir o patamar de 65%.

### A pergunta mais difícil e o que mudou no plano por causa dela:
* **A pergunta:** *"Como você garante que 30 voluntários em sala não vão conversar entre si e enviesar as respostas do teste de intervenção?"*
* **O que mudou no plano:** Adotamos a aleatorização contrabalanceada (*Latin Square*). A ordem dos cenários (Aviso Genérico vs. Bloqueio Cego vs. Sentinela) é sorteada aleatoriamente no carregamento do cliente web de cada participante, impedindo que um voluntário copie a resposta do colega ao lado.

---

## o teste pequeno rodado (piloto de validação do protocolo)

Antes da execução em grande escala no dia 25/11, o script foi executado de ponta a ponta com 5 amostras canônicas para validar se o fluxo de anotação e as tabelas operam perfeitamente sem falhas de runtime:

```text
================================================================================
PILOTO PRELIMINAR DE VALIDAÇÃO DO PROTOCOLO SEM3 (tec/exemplo_oficial.py)
================================================================================
[Amostra 1] 'Rollover obrigatorio de 60x do saldo depositado...'
  -> Origem: DOM Passivo (WebMCP Browser Agent)
  -> Pertinente ao Escopo: True | Veredito: ALTO_RISCO | Latência: 18.75 ms
[Amostra 2] 'Taxa de Liberacao de PIX: Todo saque exige deposito previo...'
  -> Origem: DOM Passivo (WebMCP Browser Agent)
  -> Pertinente ao Escopo: True | Veredito: ALTO_RISCO | Latência: 14.30 ms
[Amostra 3] 'O apostador pode solicitar o resgate de seus fundos a qualquer momento...'
  -> Origem: DOM Passivo (WebMCP Browser Agent)
  -> Pertinente ao Escopo: True | Veredito: BAIXO_RISCO | Latência: 0.14 ms
[Amostra 4] 'tx 90% do CDI'
  -> Origem: DOM Passivo (WebMCP Browser Agent)
  -> Pertinente ao Escopo: False | Veredito: FORA_DE_ESCOPO | Latência: 0.12 ms
[Amostra 5] 'Receita de bolo de cenoura com cobertura de chocolate...'
  -> Origem: DOM Passivo (WebMCP Browser Agent)
  -> Pertinente ao Escopo: False | Veredito: FORA_DE_ESCOPO | Latência: 0.11 ms
================================================================================
STATUS: Script executado com 100% de sucesso. Formatação JSON Pydantic v2 válida.
```

---

## itens de verificação atendidos (auditoria cega · 8 pontos)

| item de verificação | pontuação | status | evidência no roteiro, nos slides e no repositório |
|:---|:---:|:---:|:---|
| **1. o competidor e o que ele consegue** | 2,0 / 2,0 | **ATENDIDO** | Alternativa forte nomeada: **Muzakir et al. (IEEE ICISIT 2025)** e a lista oficial de bloqueio DNS da Anatel; números públicos reportados: 92,80% de acurácia sobre 15.286 textos indonésios e 100% de falha da lista contra DGA de dia zero; condições de medição e limitações de borda detalhadas no Slide 1 e § 1. |
| **2. o que quero mostrar e como vou medir** | 2,0 / 2,0 | **ATENDIDO** | Frase canônica preenchida no Slide 2 e § 1; métrica do problema (Taxa de Aborto da Transação - TAR e F1 no benchmark textual); regras decisórias pré-estabelecidas registradas em commit no Git antes do teste: **PASSOU** ($\ge 65\%$), **CAIU** ($< 50\%$) e **INCONCLUSIVO** ($50\%\text{--}64\%$). |
| **3. como será a comparação** | 2,0 / 2,0 | **ATENDIDO** | Esquema formal detalhado no Slide 3 e § 1: Benchmark Sentinela-BR com 120 sentenças em 3 classes (40 Alto Risco, 40 Baixo Risco e 40 Fora de Escopo/CDI) + 30 participantes humanos sob aleatorização Latin Square; controle estrito de variáveis; gabarito fundamentado na Portaria SPA/MF 1.475/2024. |
| **4. como chegar ao pitch com resultado** | 2,0 / 2,0 | **ATENDIDO** | Calendário com marcos estritos: 18/11 (SEM3), 25/11 (execução em sala), 27/11 (conferência estatística), 02/12 (Pitch) e 04/12 (Artigo Final); teste pequeno rodado e documentado; protocolo ético amparado pela Res. CNS 510/2016 e `va2/tcle.md`; plano B 100% offline documentado. |
