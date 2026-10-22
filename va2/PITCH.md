# Guia de Defesa Oral sem a Tela · Sentinela Clandestino
> **Disciplina:** Tópicos Avançados em Inteligência Artificial (UFRPE 2026.2)  
> **Aluno:** José Albérico Rocha da Silva  
> **Artefatos:** `va2/brw.md` e `va2/cmp.md`  
> **Objetivo:** Roteiro prático de 2 minutos para responder com autoridade e naturalidade às checagens do professor Lucas.

---

## O Roteiro em 4 Blocos (Pitch de 2 Minutos)

### Bloco 1 · A Crise Real e a Desagregação dos Números (30 segundos)
> *"Professor, o projeto não é um chatbot de dicas nem um aplicativo moralista de conscientização. Ele ataca a raiz técnica da crise das apostas ilegais no Brasil.*  
> *Segundo a Nota Técnica do Banco Central de agosto de 2024, o mercado total de apostas movimenta **R$ 20,8 bilhões por mês** via Pix. Desse total, o Ministério da Fazenda e o Ciberlab estimam que a fatia clandestina e não autorizada represente entre **30% e 50%**, drenando de **R$ 6 a R$ 10 bilhões mensais** para redes que operam em paraísos fiscais e lavagem de dinheiro.*  
> *A repressão da Anatel derrubou mais de 2.000 sites, mas os criminosos responderam gerando espelhos mutantes instantâneos e distribuindo APKs piratas fora das lojas oficiais."*

---

### Bloco 2 · Por que Alternativas sem IA Perdem Categoricamente (30 segundos)
> *"Se alguém sugerir que uma lista de bloqueio de teclado ou lista negra de chaves Pix resolveria sem IA, a resposta técnica é simples: **o crime organizado opera em dia zero**.*  
> 1. **DGA e Espelhos:** Eles usam algoritmos de geração de domínios sob extensões baratas (`.xyz`, `.top`) criados minutos antes das postagens. Nenhuma lista estática conhece o link;  
> 2. **Pix Dinâmico:** Eles não usam uma chave Pix fixa, mas gateways de pagamento (PSPs) que emitem QR Codes dinâmicos com CPFs rotativos de laranjas;  
> 3. **APKs Polimórficos (MAMF):** Conforme Li et al. (NDSS 2025), o código é recompilado automaticamente a cada download, mudando os hashes SHA-256 e anulando antivírus tradicionais.*  
> *Qualquer regra heurística fixa é cega para o que acabou de nascer."*

---

### Bloco 3 · A Inversão do Waze: O Interesse Próprio do Apostador (30 segundos)
> *"Por que as pessoas usariam? Ninguém instala um aplicativo para ser proibido de jogar ou tomar sermão moral — o usuário simplesmente desinstalaria.*  
> *Apoiado no princípio do Waze, nós canalizamos o **interesse egoísta do próprio apostador**: ele quer lucrar e tem pavor de cair no **golpe do saque travado (*honeypot*)**, onde o cassino aceita o Pix de depósito mas congela a conta quando ele tenta sacar o prêmio, além do risco de pegar um cavalo de Troia que roube seu banco real.*  
> *O Sentinela Clandestino não é um censor; ele é um **auditor de risco contratual e integridade**. Ele mostra as evidências de golpe na tela de redirecionamento, e o apostador desiste por vontade própria para não ser feito de bobo."*

---

### Bloco 4 · A Tecnologia: Pipeline Híbrido e Soberania Local (30 segundos)
> *"Para viabilizar isso no smartphone com privacidade total e sem travar a navegação, desenhamos uma **arquitetura híbrida de dois estágios na borda**.*  
> 1. **Fast-Path com LAYA (< 35ms):** Usamos o modelo de decisão rápida de Sistema 1 *LAYA* (open-source, pesos abertos baseados em ModernBERT). Ele roda na NPU do celular em menos de 35 milissegundos, com menos de 100 MB de RAM. Se for flagrante de golpe (> 90%), alerta na hora sem latência perceptível;  
> 2. **Deep-Path com SLM (Sob Demanda):** O SLM quantizado em 4-bit (1B–3B) só acorda se houver dúvida ou se o usuário pedir para auditar termos jurídicos de saque retido;  
> 3. **Grafos pDNS via MCP:** Agentes locais consultam um resumo comprimido (filtros de Bloom) de grafos de DNS passivo para correlacionar redes de servidores de laranjas;  
> 4. **Por que descartamos o JEV?** Porque o Jev é proprietário e roda na nuvem. Enviar a navegação do usuário para uma API externa destruiria a soberania local de dados;  
> 5. **Onde perdemos na matriz?** Assumimos com honestidade: empatamos em bateria/RAM (◐, pois qualquer modelo neural gasta mais que uma tabela em C) e perdemos categoricamente em prontidão de escala (✘, pois somos um protótipo acadêmico frente a ferramentas comerciais com milhões de usuários)."*

---

## As 5 Perguntas de Pegadinha que a Banca Pode Fazer

| Pergunta do Professor | Resposta Precisa e Direta |
|---|---|
| **"Por que não inspecionar direto o feed do Instagram?"** | *"Inviabilidade arquitetural do Android: o sistema impõe sandboxing rígido e TLS pinning. Nenhum app legítimo lê a memória de outro sem root. Por isso atuamos no evento de redirecionamento web e download de arquivos fora da loja."* |
| **"E se o apostador quiser jogar mesmo assim?"** | *"O sistema não bloqueia autocraticamente; exibe o Painel de Evidências Transparentes com escore de calote de saque. A decisão final é do usuário, garantindo autonomia e quebrando a impulsividade."* |
| **"Se você usa grafos de DNS, os dados não saem do celular?"** | *"Não. Os agentes locais via MCP operam sobre um digest comprimido pré-sincronizado em filtros de Bloom no aparelho, garantindo zero vazamento de telemetria."* |
| **"Por que a Trend Micro não resolve isso?"** | *"Porque ela depende de o usuário tirar print e enviar manualmente para a nuvem da empresa, além de avaliar apenas reputação genérica sem ler regras predatórias de saque em páginas dinâmicas."* |
| **"Qual o veículo do artigo mais próximo?"** | *"Nabeel et al. (2020) está publicado no ACM TOPS (Qualis A1) com inferência em grafos de DNS passivo; Álvarez-Ojeda et al. (2025) no COLING (A1); e Muzakir et al. (2025) no IEEE ICISIT."* |
