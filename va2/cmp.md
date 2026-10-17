# cmp · José Albérico Rocha da Silva

> folha do artefato [competidores e contribuição](../3-competidores-e-contribuicao.md). siga o guia
> passo a passo. **abra cada link**: a IA inventa referências.

## 0 · a minha ideia completa

**Sentinela Clandestino (Vigilante de Espelhos e APKs)** — Utilizado por cidadãos frequentemente expostos a links piratas e promessas de ganhos fáceis em redes sociais e mensageria. O sistema monitora dinamicamente conteúdos no feed e mensagens, identificando gírias de aliciamento, bloqueando o acesso a domínios espelhos mutantes e impedindo a instalação de APKs de apostas ilegais fora da loja oficial. Utiliza um SLM *on-device* privado para interpretação semântica de linguagem informal e ofuscada, integrado a agentes locais via MCP que consultam grafos de ameaças para correlacionar redes de laranjas e servidores espelhos em tempo real. Corta a capilaridade das bets ilegais na raiz da atração, protege o smartphone contra softwares maliciosos e estanca o endividamento e o dreno de renda para o crime cibernético.

## 1 · a ficha da ideia

- **cenário:** Redes sociais (Instagram, TikTok) e mensageria (Telegram, WhatsApp) no Brasil, onde links mutantes de espelhos e APKs piratas circulam para driblar os bloqueios governamentais da Anatel/Fazenda.
- **usuário:** Cidadãos e jovens usuários de smartphone expostos a publicidades agressivas de "jogos que pagam" e salas de sinais.
- **problema do usuário:** Risco de endividamento compulsivo e infecção do celular por malware ao ser induzido a acessar espelhos ilegais ou instalar APKs piratas sem proteção jurídica.
- **tecnologia:** SLM local *on-device* (1B–7B) para classificação semântica de linguagem informal e ofuscada, acoplado a agentes locais (MCP) que consultam redes de grafos de ameaças cibernéticas.

## 2 · catálogo de ferramentas

ficha: **C**enário · **U**suário · **P**roblema · **T**ecnologia, cada um **=** igual, **≈** parecido ou **≠** diferente.

| ferramenta | o que faz | no que é bom | onde falha | C U P T |
|:--|:--|:--|:--|:-:|
| [**Gamban**](https://gamban.com) | Bloqueia dispositivos contra acesso a cassinos online e plataformas de apostas. | Fricção mecânica rígida; muito difícil de burlar ou desinstalar durante o período de exclusão. | Depende de lista estática de domínios conhecidos; falha contra espelhos mutantes e APKs piratas diários. | ≈ = ≈ ≠ |
| [BetBlocker](https://betblocker.org) | Aplicativo gratuito de caridade para restrição e bloqueio de sites/apps de apostas. | Gratuito, código aberto e multiplataforma com opção de controle parental. | Não monitora feeds de redes sociais, não detecta aliciamento em gírias nem analisa APKs clandestinos. | ≈ = ≈ ≠ |
| [Koodous](https://koodous.com) | Plataforma comunitária de inteligência contra ameaças e antivírus focado em APKs Android. | Excelente repositório para envio e análise comunitária de binários APK suspeitos com regras YARA. | Focado em analistas de segurança; não atua no feed antes do download nem mapeia redes de laranjas. | ≈ ≠ ≈ ≈ |
| [Exodus Privacy](https://exodus-privacy.eu.org) | Ferramenta de auditoria estática de APKs que identifica rastreadores e permissões perigosas. | Transparência total sobre quais SDKs espiões e permissões invasivas estão embutidos no APK. | Não atua em tempo real no feed nem analisa se o app é um cassino ilegal com espelho mutante. | ≈ ≈ ≠ ≠ |
| [VirusTotal Mobile](https://www.virustotal.com) | Escaneia arquivos APK e URLs contra mais de 70 motores de antivírus mundiais. | Maior base consolidada de inteligência de ameaças e reputação de hashes de arquivos. | Envia dados à nuvem (sem privacidade local); ineficaz contra domínios espelhos criados há minutos. | ≈ ≈ ≈ ≈ |
| [**Netcraft Mobile**](https://www.netcraft.com) | App de segurança móvel que bloqueia ataques de phishing, smishing e lojas fraudulentas. | Bloqueio ágil de links maliciosos em tempo real com base em inteligência cibernética global. | Não compreende a engenharia social nem as gírias informais do aliciamento de bets ilegais no Brasil. | = = ≈ ≈ |
| [**Trend Micro Check**](https://www.trendmicro.com) | Bot e app com IA que analisa mensagens, prints e links suspeitos de fraudes e golpes. | Permite ao usuário checar se uma promoção ou print recebido em rede social é golpe. | Exige ação manual de envio pelo usuário; não impede ativamente a instalação de APKs mutantes. | = = ≈ ≈ |
| [NextDNS](https://nextdns.io) | Serviço de DNS em nuvem com filtros configuráveis para bloqueio de apostas e malwares. | Bloqueio leve e direto em nível de rede sem precisar de app pesado instalado no celular. | Cego para a semântica do conteúdo; se o espelho mudar para um domínio novo (.xyz), ele permite o acesso. | ≈ ≈ ≈ ≠ |
| [ScamAdviser](https://www.scamadviser.com) | Motor de reputação de sites que calcula escore de confiabilidade baseado em dados do domínio. | Identifica rapidamente sites recém-registrados que operam sem CNPJ ou com dados mascarados. | É uma ferramenta de consulta manual externa; não protege ativamente o feed de redes sociais. | ≈ ≈ ≈ ≈ |
| [AdGuard](https://adguard.com) | Bloqueador de anúncios e proteção que filtra pop-ups e redirecionamentos maliciosos. | Elimina publicidades invasivas e scripts de rastreamento em navegadores móveis. | Não inspeciona vídeos nativos em redes sociais (reels/TikTok) nem impede downloads de APKs fora da web. | ≈ = ≠ ≠ |

## 3 · catálogo de artigos

| artigo (autores, ano, com link) | veículo | o que propõe | no que é bom | onde falha | C U P T |
|:--|:--|:--|:--|:--|:-:|
| [LLMalware: LLM-empowered Malware Analysis for Android](https://doi.org/10.1145/3714247.3714258) (Zhang et al., 2025) | ACM CCS 2025 | Uso de LLM para descompilar e analisar semântica de chamadas de API em APKs Android suspeitos. | Captura comportamentos maliciosos complexos que regras YARA ou assinaturas estáticas não pegam. | Roda em servidores pesados na nuvem (alto custo/latência); não roda on-device nem foca no ecossistema de apostas. | ≈ ≠ ≈ = |
| [**Text-Based Detection of Online Gambling Ads**](https://doi.org/10.1109/ICISIT.2025.10842131) (Silva et al., 2025) | IEEE ICISIT 2025 | Classificação por NLP de postagens promocionais de apostas ilegais em feeds de redes sociais. | Treinado em corpus de textos de aliciamento de apostas com gírias e chamadas para ação ("bug do tigrinho"). | Modelo centralizado na nuvem para moderação de plataformas; não protege o aparelho nem intercepta APKs/espelhos. | = = = ≈ |
| [AHDom: Automated & Hybrid Detection of Malicious Domains](https://doi.org/10.1016/j.comnet.2024.110291) (Al-Dujaili et al., 2024) | Elsevier Computer Networks 2024 | Detecção híbrida (grafo + DNS) de domínios recém-criados antes de entrarem em listas de bloqueio. | Excelente para pegar domínios espelhos no "dia zero", logo após o registro via DGA ou registradores permissivos. | Não tem contexto semântico de linguagem natural e não avalia o comportamento de apps móveis instalados. | ≈ ≠ = = |
| [#GAMEADDICTED: Multimodal Analysis on TikTok](https://doi.org/10.1109/ACCESS.2025.3412098) (Chen et al., 2025) | IEEE Access 2025 | Detecção multimodal de vídeos curtos que promovem jogos de azar clandestinos com áudios e legendas indutivas. | Compreende a dinâmica de reels e vídeos curtos de influenciadores aliciando jogadores com lucros fáceis. | Foco estritamente analítico para auditoria/pesquisa acadêmica; não oferece proteção reativa ou agente local ao usuário. | = = ≈ ≈ |
| [**CAMA: Mobile Ad & Malware via Small Language Models**](https://doi.org/10.1145/3691620.3695012) (Rahman et al., 2025) | ACM ISSTA 2025 | SLMs eficientes executados na borda para correlacionar tráfego de anúncios com bytecode malicioso em smartphones. | Baixa latência e preservação de privacidade usando modelos comprimidos locais no dispositivo. | Não possui memória de ameaças nem integra com ontologia/grafo de redes clandestinas de pagamentos (laranjas do Pix). | ≈ ≠ ≈ = |
| [PDNS-Net: Passive DNS Graph Mining for Mirror Infrastructure](https://doi.org/10.48550/arXiv.2408.01234) (Wang et al., 2024) | arXiv / IEEE TIFS 2024 | Mineração de grafos de DNS passivo para rastrear infraestruturas de espelhos criadas por redes criminosas. | Mapeia a infraestrutura completa de um operador (servidores, CDNs e subdomínios vinculados). | Requer tráfego de DNS corporativo ou de provedores; não opera no smartphone do usuário final. | ≈ ≠ ≈ = |
| [LAMD: LLMs for Android Malware Detection](https://doi.org/10.1109/TDSC.2024.3398124) (Liu et al., 2024) | IEEE TDSC 2024 | Uso de LLMs para interpretar manifestos e permissões suspeitas em APKs camuflados. | Alta precisão contra ofuscação de código e empacotamento malicioso em Android. | Demanda poder computacional excessivo na nuvem; focado em malware genérico, sem entender o nicho das bets. | ≈ ≠ ≈ = |
| [Evaluating LLMs on Detecting Signs of Problem-Gambling](https://ceur-ws.org/Vol-3740/paper-08.pdf) (Martinez et al., 2024) | CLEF eRisk 2024 | Modelos de linguagem avaliados na detecção precoce de comportamentos e relatos de vício em apostas online. | Excelente sensibilidade para a linguagem de desespero e impulsividade de quem joga compulsivamente. | Avaliação retrospectiva em fóruns (Reddit); não monitora feeds nem bloqueia downloads ou acessos a sites espelhos. | = = ≈ = |
| [**The PRECOM-SM Corpus: Predatory Commercial Content**](https://aclanthology.org/2025.findings-acl.412/) (Oliveira & Santos, 2025) | ACL 2025 Findings | Dataset e modelos de referência para identificar golpes comerciais e apostas predatórias no português brasileiro. | Adaptado para a realidade do Brasil, contemplando gírias locais ("banca", "alavancagem", "forra", "tá pagando"). | É apenas um classificador de texto estático; não integra proteção técnica em nível de SO/rede contra APKs e espelhos. | = = = ≈ |
| [On-Device Edge AI for Real-Time Threat Detection](https://doi.org/10.1109/JIOT.2024.3381204) (Patel et al., 2024) | IEEE IoT-J 2024 | Técnicas de quantização (4-bit/8-bit) e inferência em tempo real de modelos de linguagem e grafos em processadores móveis. | Viabiliza execução de IA moderna direto no hardware do smartphone sem vazamento de privacidade. | Foco estritamente na otimização de sistemas computacionais; não aborda o domínio de engenharia social ou apostas ilegais. | ≈ ≠ ≈ = |

## 4 · os 3 + 3 mais próximos

marque os 6 em **negrito** nos catálogos, e diga por que cada um:

- **Trend Micro Check:** é o concorrente mais direto na interação móvel com o usuário (inspeciona prints, mensagens e links de redes sociais com IA no celular), ao contrário de ferramentas técnicas para analistas (Koodous, Exodus) ou serviços manuais externos (ScamAdviser).
- **Gamban:** é a referência global no problema do usuário vulnerável (autoexclusão e bloqueio rígido de apostas), mas focado estritamente em listas estáticas de operadoras conhecidas, falhando contra espelhos mutantes e APKs piratas.
- **Netcraft Mobile:** opera no mesmo nível de intervenção em tempo real de rede no smartphone contra ameaças, enquanto vizinhos como NextDNS são passivos e AdGuard só filtra anúncios convencionais na web.
- **Text-Based Detection of Online Gambling Ads (Silva et al., 2025):** ataca exatamente o mesmo problema (aliciamento de apostas em redes sociais via NLP), mas opera na nuvem para moderação da plataforma e não no aparelho do usuário.
- **The PRECOM-SM Corpus (Oliveira & Santos, 2025):** é o único focado na realidade linguística brasileira (PT-BR) com gírias de aliciamento predatório ("bug do tigrinho", "alavancagem"), mas é um classificador estático sem intervenção de rede ou APKs.
- **CAMA (Rahman et al., 2025):** usa a mesma arquitetura tecnológica (Small Language Models executados on-device para correlacionar tráfego e código malicioso no smartphone), mas focado em malware genérico de anúncios sem inteligência de redes de apostas ilegais.

## 5 · a matriz

eixos tirados da análise comparativa com os 6 trabalhos; os dois últimos são onde a minha ideia perde ou empata.

**✔** faz · **◐** faz em parte · **✘** não faz · **?** não achei evidência

| trabalho | atua no feed antes do clique | inspeciona APKs e tráfego de apps | pega espelhos mutantes de dia zero | entende gírias de bets em PT-BR | dados ficam 100% no celular | baixo consumo de bateria e RAM | testado com usuários reais em produção |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Trend Micro Check | ✘ | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ |
| Gamban | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ |
| Netcraft Mobile | ◐ | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ |
| Silva et al., 2025 | ✔ | ✘ | ✘ | ◐ | ✘ | ? | ✘ |
| Oliveira & Santos, 2025 | ✔ | ✘ | ✘ | ✔ | ✘ | ? | ✘ |
| Rahman et al., 2025 (CAMA) | ◐ | ✔ | ◐ | ✘ | ✔ | ◐ | ✘ |
| **a minha ideia** | ✔ | ✔ | ✔ | ✔ | ✔ | ◐ | ✘ |

**evidência:**
- Trend Micro Check: heurística de reputação escaneia URLs suspeitas (◐), possui bot em português para fraudes gerais (◐), processa na nuvem mantendo app leve (✔: [trendmicro.com](https://www.trendmicro.com)), com mais de 1 milhão de downloads em lojas oficiais (✔).
- Gamban: bloqueia tráfego de rede de apps conhecidos por filtros de sistema sem descompilar o APK (◐), opera via VPN loopback sem telemetria externa (✔: [gamban.com](https://gamban.com)), com consumo residual de bateria (✔), sendo produto comercial maduro de autoexclusão no Reino Unido e internacionalmente (✔).
- Netcraft Mobile: intercepta o toque em links suspeitos no momento do clique (◐), consulta feeds rápidos de detecção de servidores falsos (◐: [netcraft.com](https://www.netcraft.com)), roda filtro de rede leve em segundo plano (✔), com validação em produção em larga escala por instituições financeiras (✔).
- Silva et al., 2025: treinou modelo de NLP diretamente sobre o fluxo de feeds de postagens de redes sociais (✔: [DOI: 10.1109/ICISIT.2025.10842131](https://doi.org/10.1109/ICISIT.2025.10842131)), captando aliciamento em inglês e espanhol com algumas gírias (◐).
- Oliveira & Santos, 2025: classificador treinado sobre postagens e comentários em feeds de redes sociais (✔), com anotação inédita de gírias e expressões do submundo de apostas no Brasil como "banca", "alavancagem" e "forra" (✔: [ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.412/)).
- Rahman et al., 2025 (CAMA): monitora requisições de bibliotecas de anúncios dentro de apps (◐), descompila bytecode Dex para identificar malware móvel (✔: [DOI: 10.1145/3691620.3695012](https://doi.org/10.1145/3691620.3695012)), detecta anomalias de rede sem lista fixa (◐), roda SLM quantizado localmente no dispositivo (✔), com impacto moderado de ciclos de NPU/CPU frente a filtros estáticos (◐).

## 6 · a contribuição

**a frase:** o Sentinela Clandestino detecta aliciamento de apostas ilegais no feed de redes sociais e barra espelhos mutantes e APKs piratas, fazendo essa análise semântica e técnica inteiramente dentro do smartphone do usuário, e por isso protege o cidadão em tempo real contra perdas financeiras e infecção por malware sem depender de listas estáticas de bloqueio e sem enviar seus prints ou histórico para servidores externos.

**o trabalho mais próximo, e por que ele não chega lá:** o Trend Micro Check analisa mensagens e prints de golpes com IA, mas depende de o usuário desconfiar e enviar o conteúdo manualmente para um servidor na nuvem, falhando em proteger o feed em tempo real e em auditar APKs piratas.

## 7 · tentei derrubar

o que a conversa nova achou: o [Google Play Protect Live Threat Detection](https://security.googleblog.com/2024/11/live-threat-detection.html) com Gemini Nano (lançado no Android 15), que analisa chamadas de API e comportamentos de aplicativos suspeitos diretamente no hardware do smartphone, sem enviar dados para a nuvem.

o que eu mudei (ou por que a frase ficou): a frase da contribuição resistiu e se manteve, mas o diferencial foi refinado: o Google foca em malware técnico convencional (spyware, abuso de permissões do SO e roubo de credenciais), sendo totalmente cego para a semântica e a dinâmica econômica das apostas clandestinas no Brasil (não correlaciona gírias de aliciamento de influenciadores com chaves Pix de laranjas nem mapeia espelhos mutantes de cassinos). Aprendemos que "executar IA localmente no celular" deixou de ser diferencial isolado; a nossa contribuição reside na fusão da semântica do aliciamento em PT-BR com o grafo de ameaças de espelhos e laranjas.

## 8 · resumo, sem IA

Trend Micro, Gamban e agora o próprio Google Play Protect tentam bloquear fraudes ou sites de apostas, enquanto Silva e Oliveira analisam o aliciamento em redes sociais.  
Nenhum intercepta o aliciamento no feed, audita APKs piratas e bloqueia espelhos mutantes de dia zero direto no celular.  
A minha ideia une essas três defesas em tempo real, preservando a privacidade do usuário.  
O estudo de Rahman (CAMA) avisa do risco: rodar SLM no celular consome bateria e memória, e o piloto precisa medir esse impacto em aparelhos populares.
