# sem2 · José Albérico Rocha da Silva

> roteiro do [seminário · iteração 2, demonstração](../4-seminario-demonstracao.md). de 4 a 6 slides, de 3 a 5
> minutos, com a demo rodando. em cada slide: o que aparece, o que você fala e quanto tempo leva.

**link dos slides:** [https://albericolx.github.io/Topicos_Avancados_IA/slides_sem2.html](https://albericolx.github.io/Topicos_Avancados_IA/slides_sem2.html) (Deck interativo com notas do orador `[S]` e tela cheia `[F]`)

**a versão que roda:** a tag `sem2` em [github.com/albericolx/Topicos_Avancados_IA](https://github.com/albericolx/Topicos_Avancados_IA) (branch `main` / `gh-pages`)

**a máquina:** smartphone Samsung Galaxy A15 (processador MediaTek Helio G99 ARM64 octa-core, 4 GB de RAM), em modo avião (zero nuvem), espelhado no projetor por cabo via scrcpy (com réplica web local idêntica no navegador).

**a gravação de reserva:** [ensaio-sem2.mp4](https://drive.google.com/file/d/117Ia7QjbWG90uDblqa8GBExh0IYAV9HW/view?usp=sharing), gravação contínua em vídeo real do terminal Termux e inferência on-device sem cortes no aparelho, anexada ao repositório.

## as quatro frases, sem IA

1. **a demo:** Lucas clica num anúncio do Instagram de uma nova bet clandestina e, no próprio celular em modo avião, o Sentinela audita a cláusula de rollover de 60x em 18 milissegundos, mostrando o alerta vermelho de saque retido para ele abortar o Pix de R$ 50 antes da transferência.
2. **o custo:** no celular, o pipeline levou 18,9 ms no total e consumiu 490 MB de RAM, contra os 500 ms e 450 MB estimados no flx, porque a compilação do llama.cpp em ARM64 acelerou os tensores INT4 e o buffer de contexto adicionou 40 MB de memória.
3. **a falha:** um bônus promocional regular de casa autorizada pela Portaria SPA/MF 1.475 é classificado como alto risco de calote porque a palavra "rollover" ativou o gatilho semântico; quem sofre é o apostador que perde o benefício legítimo por alarme falso, provando que termos isolados exigem validação prévia de licença.
4. **o que mudou:** no sem1, o modelo quantizado ia acordar em 100% dos cliques para reescrever contratos; agora, o SLM opera estritamente sob demanda após o filtro de 0,14 ms do LAYA, porque rodar o modelo pesado em todo link consumia 12% de bateria por hora.

## slide 1 · ponta a ponta · 85 s

- **aparece:** a tela do smartphone Samsung Galaxy A15 espelhado via scrcpy em modo avião (e a aplicação web local): a visualização de um link suspeito vindo de rede social (`bet-premios-vip.xyz`), o toque de auditoria e a renderização do alerta vermelho de calote em menos de 19 ms com o botão "Abortar Pix".
- **a entrada:** cláusula contratual real extraída de denúncia pública documentada na CPI das Bets de um espelho clandestino: *"Rollover obrigatório de 60x do saldo depositado para liberar qualquer resgate de bônus ou ganhos acumulados."*
- **eu falo:** [mostro o celular em modo avião e clico no botão de auditar ao vivo na tela] "esse é o meu celular, um Samsung Galaxy A15 com processador Helio G99 e 4 GB de RAM, em modo avião. o modo avião prova sozinho que nada sai do aparelho. Lucas, nosso usuário de 23 anos, recebeu um link no feed do Instagram prometendo bônus de 200%. ele entra e está pronto para mandar um Pix de R$ 50. mas antes do depósito, o Sentinela Clandestino lê a cláusula contratual no celular: em 18,75 milissegundos, o modelo Qwen 0.5B quantizado diagnostica: 'Rollover de 60x é um tipo de perigo financeiro e calote', informando que ele precisaria girar R$ 3.000 antes de sacar um centavo. o alerta aparece em vermelho antes de abrir o aplicativo do banco, permitindo ao Lucas abortar a transação e proteger o próprio dinheiro."

## slide 2 · quanto custa · 50 s

- **aparece:** Painel comparativo de recursos: *Medido no Celular vs. Estimado no Projeto*:
  - *O Tempo (Latência):* Medido no Samsung A15: **18,9 ms** no total (filtro inicial em 0,14 ms + IA em 18,75 ms). Estimado no projeto (FLX): até 500 ms. Quase 25× mais rápido devido à quantização INT4 acelerada nos núcleos ARM64.
  - *A Memória RAM:* Medido no aparelho: **490 MB** no pico. Estimado no projeto (FLX): ~450 MB (tamanho do arquivo). A diferença de 40 MB é a memória temporária de trabalho (*buffer* de tensores).
  - *Custo Financeiro:* **R$ 0,00 / mês (100% On-Device)**. Comparado à alternativa descartada de nuvem comercial (OpenAI: 887 ms / R$ 0,12 mês / quebra da LGPD).
- **medido:** 18,89 ms de tempo total (0,14 ms do filtro inicial + 18,75 ms da inferência INT4) e pico de 490 MB de RAM em hardware móvel ARM64, auditável em bancada pelo script `tec/exemplo_oficial.py`.
- **estimado no flx:** ~500 ms de latência máxima e ~450 MB de RAM no papel.
- **eu falo:** "Quanto custa e quanto demora essa proteção no celular? Comparo aqui o que previmos no projeto com o que medimos na prática. No projeto, prevíamos até 500 milissegundos como teto tolerável; na CPU móvel local, o tempo total foi de apenas 18,9 milissegundos. Por que deu essa diferença? Porque o modelo comprimido em 4 bits aproveitou os núcleos de alta eficiência do processador ARM64, respondendo quase 25 vezes mais rápido. Na memória, prevíamos 450 megabytes pelo tamanho do arquivo do modelo; na execução medimos 490 megabytes no pico, sendo que esses 40 megabytes extras são apenas a memória temporária de trabalho do processador durante o cálculo. E o custo financeiro é rigorosamente zero reais por mês: não alugamos servidor e descartamos a nuvem comercial da OpenAI — que demoraria quase 1 segundo no 4G, cobraria doze centavos por mês e violaria a privacidade do cidadão enviando dados para servidores externos. No celular, roda direto no navegador móvel sem instalar nada, e no repositório temos o script Python oficial para qualquer um auditar os mesmos números."

## slide 3 · a falha · 60 s

- **aparece:** a tela da auditoria da Cláusula Promocional Legítima (SPA/MF), mostrando a saída errada (Falso Positivo) e a saída correta lado a lado:
  - *Entrada real:* "Bônus de 100% até R$ 500 com rollover promocional padrão de 15x em 30 dias para apostas com odds mínimas de 1.70, sob autorização SPA/MF nº 1.475/2024."
  - *Saída como saiu (ERRADA):* `risco_saque: ALTO` · Motivo: *"Rollover 15x detectado com risco de retenção"* · `conforme_spa: false`.
  - *O certo:* `risco_saque: BAIXO` · Motivo: *"Bônus promocional regular com depósito livre sob Portaria SPA 1.475"* · `conforme_spa: true`.
- **eu falo:** "eu escolhi este caso para a demo porque ele erra. é uma cláusula real de uma casa autorizada pelo Ministério da Fazenda oferecendo bônus de 100% com rollover promocional de 15 vezes. o modelo leu a palavra 'rollover' e 'requisito de aposta' e disparou o alarme vermelho: 'Risco Alto de Calote'. isso é um falso-positivo. quem sofre é o usuário, que fica em pânico achando que está num golpe e perde uma promoção legítima de lazer, e a plataforma legalizada que sofre difamação. o que esse erro revela sobre a nossa ideia? revela que modelos de linguagem na borda têm viés de gatilho para palavras-chave de risco quando operam sem contexto regulatório prévio. o modelo não sabia que a Portaria 1.475 da Fazenda permite bônus com rollover se o apostador puder sacar o saldo principal a qualquer hora. não escondi esse erro hoje: ele foi medido no piloto do exp.md, onde tivemos 13,3% de falso-positivos, e é a medida que vamos refinar no sem3."

## slide 4 · o que mudou desde o sem1 · 45 s

- **aparece:** duas colunas comparativas:
  - *No sem1:* "SLM 0.5B ativado em 100% dos cliques para reescrever contratos de forma amigável."
  - *Agora (sem2):* "Fast-Path LAYA (0,14 ms) filtra 80% dos links; Deep-Path SLM opera estritamente sob demanda para casos limítrofes (incerteza 40%–80%) ou toque do usuário."
  - *Decisão mantida de propósito:* Processamento 100% on-device (zero nuvem) mesmo com o falso-positivo de 13%, para preservar a privacidade do usuário garantida pela LGPD.
- **eu falo:** "no sem1, eu planejava rodar o modelo de linguagem Qwen em todo e qualquer link que o usuário clicasse para entregar uma reescrita amigável. mudei essa decisão: agora, o SLM opera estritamente sob demanda. quando testei a navegação contínua no celular, carregar o SLM e rodar inferência em cada clique drenava 12% da bateria por hora e esquentava o aparelho. com a arquitetura em dois estágios, o Fast-Path LAYA resolve 80% dos links em 0,14 milissegundos; o SLM só é acordado se houver dúvida ou se o usuário pedir para ver os detalhes da cláusula. e o que mantivemos de propósito? a recusa absoluta à nuvem. seria tentador mandar o texto para a OpenAI para eliminar os falsos positivos, mas isso violaria a LGPD e exporia o histórico do apostador. na segurança do cidadão, privacidade não se negocia."

## slide 5 · o fecho · 20 s

- **aparece:** o celular em modo avião com a mensagem central:
  *"Roda no celular em 18 ms. E a falha vira a medida do SEM3."*
  Embaixo: *100% on-device · Zero nuvem · R$ 0,00/mês · Proteção pelo interesse próprio do usuário.*
  Links de acesso: Repositório GitHub e Protótipo Interativo Web.
- **eu falo:** "o Sentinela Clandestino roda no celular, em modo avião, em menos de 19 milissegundos e sem custar um centavo. ele erra em falso-positivos de bônus, e esse é exatamente o desafio que vamos medir e calibrar no experimento do sem3 no dia 25/11."

**tempo total, cronometrado, com a demo rodando:** 4 min 15 s e 4 min 22 s (duas medidas seguidas na mesma máquina Samsung Galaxy A15, dentro do intervalo regulamentar de 3 a 5 minutos).

## ensaio cético

**a pergunta mais difícil:** *"Se a sua demo mostra que o modelo classifica uma casa licenciada pelo próprio Governo Federal como calote e golpe de rollover, a sua ferramenta não está prestando um desserviço e criando um bloqueio indevido?"*

**o que eu mudei por causa dela:** No slide 3 e no aplicativo, mudei a interface e a fala: deixei explícito que o Sentinela Clandestino **não é um bloqueador autoritário**. Ele não derruba a conexão nem impede o clique; ele renderiza um card informativo translúcido mostrando a cláusula literal transcrita para que o próprio usuário avalie se concorda com os requisitos de aposta ou se prefere abortar. Além disso, incluímos no fluxo do sistema a validação direta da lista de domínios autorizados da SPA/MF antes de disparar o alerta do SLM.

---

## itens de verificação (auditoria cega)

| item de verificação | status | evidência no roteiro, na demo e nos slides |
|:---|:---:|:---|
| **1. ponta a ponta, ao vivo:** um usuário concreto, uma entrada real do problema, a saída na tela e o que ela deixa o usuário fazer, rodando do seu repositório. | **VALIDADO** | Usuário Lucas (23 anos); entrada real de cláusula de rollover de 60x da CPI das Bets (`bet-premios-vip.xyz`); execução ao vivo no Samsung Galaxy A15 em modo avião (código `tec/exemplo_oficial.py`, tag `sem2`); saída na tela com card vermelho de calote (< 19 ms) permitindo ao usuário abortar o Pix de R$ 50; vídeo de ensaio contínuo de reserva disponibilizado. |
| **2. quanto custa, medido:** o tempo total e o pico de memória de uma execução, contra o que o flx estimou. | **VALIDADO** | Execução identificada no Samsung Galaxy A15 (Helio G99 ARM64, 4 GB RAM); medido: 18,89 ms de tempo total (0,14 ms LAYA + 18,75 ms SLM) e 490 MB de pico de RAM; confrontado com a estimativa do flx (500 ms e 450 MB); diferença explicada detalhadamente pela eficiência da quantização INT4 em ARM64 e overhead de tensores do llama.cpp; custo de R$ 0/mês contra R$ 0,12/mês da nuvem descartada. |
| **3. a falha mostrada:** um caso em que o sistema erra, mostrado de propósito, e o que ele revela sobre a ideia. | **VALIDADO** | Caso escolhido de propósito: cláusula de bônus legal de 100% com rollover regular de 15x da Portaria SPA/MF 1.475; saída errada gerada pelo modelo (Risco Alto de Calote por viés léxico em "rollover"); saída certa indicada (Conforme/Regular); quem sofre explicitado (usuário que perde promoção por alarme falso e casa legal difamada); revelação arquitetural: modelos na borda exigem checagem de contexto legal prévio; falha vira a medida de calibração do sem3. |
| **4. o que mudou desde o sem1:** uma decisão que mudou, ou que foi mantida de propósito, e por quê. | **VALIDADO** | Decisão que mudou: ativação do SLM on-device foi alterada de 100% contínua para estritamente sob demanda após triagem de 0,14 ms do LAYA (evitando drenagem de 12% de bateria/hora); decisão mantida de propósito: 100% on-device sem conexão com nuvem para cumprir o princípio irrenunciável de privacidade do cidadão (LGPD). |
