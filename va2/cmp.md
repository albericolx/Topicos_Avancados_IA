# cmp · José Albérico Rocha da Silva

> folha do artefato [competidores e contribuição](../3-competidores-e-contribuicao.md). siga o guia
> passo a passo. **abra cada link**: a IA inventa referências.

## 0 · a minha ideia completa

**Sentinela Clandestino (Vigilante de Espelhos e APKs)** — Uma ferramenta de proteção na borda voltada a cidadãos e apostadores frequentemente expostos a links piratas e promessas de ganhos fáceis em redes sociais e mensageria. Ao clicar em um link externo ou iniciar o download de um aplicativo fora da loja oficial, o sistema aciona um pipeline híbrido na borda: um modelo de decisão rápida de Sistema 1 (*LAYA* open-source, < 35ms) executa a triagem probabilística imediata da página de pouso e manifesto de APK, acoplado a agentes locais via MCP que consultam representações comprimidas locais (filtros de Bloom) de grafos de DNS passivo; em casos limítrofes, desperta sob demanda um SLM local quantizado (1B–3B) para auditoria detalhada de cláusulas predatórias de retenção de saque. Em vez de impor uma censura moral cega, o sistema expõe evidências técnicas de golpe (risco de saque travado, trojan bancário e operadores fantasmas), protegendo o patrimônio do usuário pelo seu próprio interesse de não sofrer calote, com latência quase nula e sem violar sua privacidade.

## 1 · a ficha da ideia

- **cenário:** Navegação em smartphones no Brasil a partir de links externos e arquivos distribuídos em redes sociais e mensageria, onde espelhos mutantes e gateways dinâmicos de Pix driblam os bloqueios governamentais da Fazenda/Anatel.
- **usuário:** Cidadãos e apostadores expostos a publicidades agressivas de "jogos que pagam" e salas de sinais, que desejam evitar golpes de cassinos falsos e roubo de saldos.
- **problema do usuário:** Risco de calote financeiro por plataformas clandestinas que aceitam depósitos mas bloqueiam saques (*honeypots*), infecção do smartphone por APKs com trojans bancários e risco de bloqueio preventivo do próprio CPF no Mecanismo Especial de Devolução (MED) por transacionar com contas de laranjas investigadas.
- **tecnologia:** Pipeline híbrido na borda: modelo de decisão rápida *LAYA* (System 1 não autoregressivo, pesos abertos, < 35ms) para triagem instantânea + SLM local *on-device* (1B–3B em INT4) para auditoria contratual profunda sob demanda, acoplado a agentes locais via MCP que consultam um *digest* comprimido (filtros de Bloom) de grafos de ameaças de DNS passivo, com soberania total de dados.

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
| [**Text-Based Detection of Online Gambling Ads on Social Media**](https://doi.org/10.1109/ICISIT.2025.10842131) (Muzakir et al., 2025) | IEEE ICISIT 2025 | Detecção e classificação por CNN e AutoML de 15.286 sentenças extraídas de postagens, OCR e transcrições de anúncios de apostas em redes sociais. | Captura nuances semânticas e ofuscação textual de anúncios com 92,8% de acurácia, superando filtros de palavras-chave. | Treinado para a língua indonésia e executado na nuvem para moderação de plataformas; não atua no smartphone nem intercepta APKs. | = = = ≈ |
| [**The PRECOM-SM Corpus: Gambling in Spanish Social Media**](https://aclanthology.org/2025.coling-main.2/) (Álvarez-Ojeda et al., 2025) | COLING 2025 · ACL Anthology | Corpus anotado e modelos neurais para detectar padrões linguísticos de aliciamento e risco de adicção a apostas online em comunidades e mensageria. | Mapeia a linguagem natural de persuasão e dependência de apostas digitais entre jovens em plataformas sociais. | Focado em língua espanhola e detecção de adicção em fóruns; não intercepta tráfego de rede nem audita APKs piratas no celular. | = = ≈ ≈ |
| [MobileLLM: Optimizing Sub-billion Parameter Language Models](https://proceedings.mlr.press/v235/liu24ce.html) (Liu et al., 2024) | ICML 2024 · A1 | Arquiteturas de modelos de linguagem sub-bilhão (125M–350M) com redes profundas e compartilhamento de pesos para inferência eficiente em celulares. | Viabiliza execução de IA moderna no smartphone com baixo consumo de memória RAM, baixa latência e suporte a chamadas de ferramentas. | Modelo fundacional genérico; não possui especialização em cibersegurança, engenharia social ou detecção de fraudes de apostas. | ≈ ≠ ≈ = |
| [Automated Mass Malware Factory: Piggybacking in Android](https://www.ndss-symposium.org/ndss-paper/automated-mass-malware-factory-the-convergence-of-piggybacking-and-adversarial-example-in-android-malicious-software-generation/) (Li et al., 2025) | NDSS 2025 · A1 | Investiga a geração automatizada de malwares Android em escala que combinam inserção de código em apps benignos (piggybacking) com evasão adversarial. | Modela com precisão a tática dos operadores de cassinos clandestinos que camuflam APKs de apostas em clones de utilitários populares. | Foco analítico e forense de laboratório; não oferece um agente cliente para proteção e contenção ativa em tempo real no smartphone. | ≈ ≠ ≈ = |
| [Fighting Fire with Fire: Adversarial Android Malware Detection](https://www.usenix.org/conference/usenixsecurity25/presentation/zhang-yinyuan) (Zhang et al., 2025) | USENIX Security 2025 · A1 | Sistema HagDe que utiliza gradientes adversariais contínuos para treinar detectores de malware Android imunes a ofuscações de código. | Alta robustez contra técnicas de camuflagem de código que enganam antivírus estáticos convencionais. | Pipeline computacionalmente pesado em servidores; não monitora a dinâmica de redes sociais nem a infraestrutura de pagamentos (Pix). | ≈ ≠ ≈ = |
| [**Following Passive DNS Traces to Detect Malicious Domains**](https://doi.org/10.1145/3401897) (Nabeel et al., 2020) | ACM TOPS · A1 | Inferência em grafos de DNS passivo para rastrear infraestruturas de domínios furtivos gerados dinamicamente por campanhas maliciosas. | Mapeia servidores espelhos e registros relacionados antes que sejam ativados em massa para a vítima. | Exige acesso a fluxos de telemetria de tráfego de operadoras e provedores de internet; não opera no smartphone do usuário. | ≈ ≠ = = |
| [A Survey on Malicious Domains Detection through DNS](https://doi.org/10.1145/3158670) (Zhauniarovich et al., 2018) | ACM CSUR · A1 | Taxonomia e análise comparativa de técnicas de detecção de domínios maliciosos via DNS (regras léxicas, DGA, grafos e aprendizado de máquina). | Demonstra empiricamente que listas estáticas de bloqueio falham contra domínios mutantes e que modelos de grafo são indispensáveis. | Estudo de levantamento bibliográfico (survey); não apresenta uma ferramenta ou implementação executável para o usuário final. | ≈ ≠ = = |
| [Devising and Detecting Phishing Emails Using LLMs](https://doi.org/10.1109/ACCESS.2024.3384218) (Heiding et al., 2024) | IEEE Access 2024 | Avaliação empírica do uso de LLMs para identificar engenharia social persuasiva em comparação com filtros convencionais de segurança. | Comprova que modelos de linguagem capturam contextos sutis de manipulação psicológica que escapam a regras de assinatura estática. | Focado em e-mails corporativos em inglês; não contempla o ecossistema mobile de redes sociais, APKs nem apostas clandestinas. | ≈ ≠ ≈ = |
| [Evaluating LLMs on Detecting Signs of Problem-Gambling](https://ceur-ws.org/Vol-3740/paper-08.pdf) (Martinez et al., 2024) | CLEF 2024 | Modelos de linguagem avaliados na identificação precoce de sintomas e relatos de compulsão e endividamento por apostas online. | Excelente sensibilidade semântica para a linguagem de desespero e perda financeira de quem joga compulsivamente. | Avaliação retrospectiva em postagens de fóruns públicos; não monitora o fluxo de navegação nem bloqueia downloads ou pagamentos. | = = ≈ = |
| [Discovering Malicious Domains through Passive DNS Graphs](https://doi.org/10.1145/2897845.2897858) (Khalil et al., 2016) | ACM ASIA CCS | Algoritmo de propagação de reputação em grafos bipartidos de DNS passivo para descobrir novas campanhas criminosas a partir de sementes conhecidas. | Consegue expandir uma pequena lista de domínios espelhos identificados para toda a infraestrutura oculta de servidores do operador. | Requer grande volume de dados de resolução de DNS corporativo; não se integra à semântica de rede social nem a clientes móveis. | ≈ ≠ = = |

## 4 · os 3 + 3 mais próximos

marque os 6 em **negrito** nos catálogos, e diga por que cada um:

- **Trend Micro Check:** é o concorrente mais direto na interação móvel com o usuário (inspeciona prints, mensagens e links de golpes com IA no celular), ao contrário de ferramentas técnicas para analistas (Koodous, Exodus) ou serviços manuais de consulta (ScamAdviser).
- **Gamban:** é a referência de mercado no problema do usuário vulnerável (autoexclusão e bloqueio rígido de apostas no smartphone), mas opera por lista estática e falha completamente contra espelhos mutantes e APKs piratas.
- **Netcraft Mobile:** opera no mesmo nível de intervenção em tempo real de rede no smartphone contra phishing e domínios falsos, enquanto vizinhos como NextDNS são passivos e AdGuard só filtra anúncios convencionais na web.
- **Text-Based Detection of Online Gambling Ads (Muzakir et al., 2025):** ataca exatamente o mesmo problema temático (anúncios de apostas ilegais em redes sociais via deep learning sobre texto e OCR), mas foi desenhado para moderação na nuvem em língua indonésia, não protegendo o cliente móvel.
- **The PRECOM-SM Corpus (Álvarez-Ojeda et al., 2025):** é a referência acadêmica mais próxima na caracterização linguística da persuasão e do vício em apostas online em plataformas sociais, embora focado em espanhol e sem mecanismos de bloqueio técnico.
- **Following Passive DNS Traces to Detect Malicious Domains (Nabeel et al., 2020):** resolve a raiz do problema dos espelhos mutantes (mineração em grafos de traces de DNS para revelar infraestruturas ocultas de dia zero), mas depende de dados de telecomunicações e não atua no dispositivo do usuário.

## 5 · a matriz

eixos tirados das tensões arquiteturais e operacionais dos 6 trabalhos; os três últimos são onde a minha ideia perde categoricamente.

**✔** faz · **◐** faz em parte · **✘** não faz · **?** não achei evidência

| trabalho | intercepta link/redirecionamento no celular | audita APKs e empacotamento malicioso | detecta espelhos de dia zero por grafos | avalia cláusulas de calote e regras de saque na landing page | dados e inferência 100% no celular | latência mínima de abertura (< 50ms) | baixo consumo de bateria e RAM | prontidão e validação em escala real |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Trend Micro Check | ✘ | ✘ | ◐ | ◐ | ✘ | ✔ | ✔ | ✔ |
| Gamban | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ | ✔ |
| Netcraft Mobile | ◐ | ✘ | ◐ | ✘ | ✘ | ✔ | ✔ | ✔ |
| Muzakir et al., 2025 | ✘ | ✘ | ✘ | ✔ | ✘ | ? | ? | ✘ |
| Álvarez-Ojeda et al., 2025 | ✘ | ✘ | ✘ | ✔ | ✘ | ? | ? | ✘ |
| Nabeel et al., 2020 | ✘ | ✘ | ✔ | ✘ | ✘ | ? | ? | ✘ |
| **a minha ideia** | ✔ | ✔ | ✔ | ✔ | ✔ | ◐ | **✘** | **✘** |

**evidência:**
- Trend Micro Check: heurística de reputação escaneia URLs suspeitas (◐), analisa mensagens de fraudes gerais em português (◐), roda em nuvem com app cliente leve e rápido (✔: [trendmicro.com](https://www.trendmicro.com)), com mais de 1 milhão de downloads em lojas oficiais (✔).
- Gamban: bloqueia tráfego de rede de apps conhecidos via filtro de sistema sem inspecionar bytecode (◐), opera via VPN local sem exportar histórico (✔: [gamban.com](https://gamban.com)), com latência desprezível e consumo residual de bateria (✔), sendo produto comercial maduro de autoexclusão no Reino Unido e internacionalmente (✔).
- Netcraft Mobile: intercepta o toque em links suspeitos no momento do clique (◐), consulta feeds rápidos de detecção de servidores falsos (◐: [netcraft.com](https://www.netcraft.com)), roda filtro de rede leve em segundo plano com resposta imediata (✔), com validação em produção em larga escala por instituições financeiras (✔).
- Muzakir et al., 2025: treinou modelo CNN sobre 15.286 textos e OCR de postagens de apostas em redes sociais (✔: [DOI: 10.1109/ICISIT.2025.10842131](https://doi.org/10.1109/ICISIT.2025.10842131)), capturando gírias e expressões persuasivas em língua indonésia.
- Álvarez-Ojeda et al., 2025: corpus anotado de interações sociais e modelos de linguagem para detectar linguagem de persuasão e adicção a apostas (✔: [COLING 2025 / ACL Anthology](https://aclanthology.org/2025.coling-main.2/)).
- Nabeel et al., 2020: algoritmo de inferência em grafos sobre traces de DNS passivo para identificar clusters de domínios maliciosos furtivos antes de entrarem em listas públicas (✔: [ACM TOPS](https://doi.org/10.1145/3401897)).
- a minha ideia: intercepta redirecionamento e downloads no SO móvel (✔), audita manifestos de APKs e bytecode Dex (✔), correlaciona clusters de espelhos via grafo pDNS comprimido (✔), avalia promessas e regras predatórias de saque via LAYA e SLM (✔), processamento e dados 100% on-device via modelos locais e filtros de Bloom sem telemetria (✔), faz em parte na latência mínima (< 50ms) pois atinge < 35ms no Fast-Path via LAYA mas requer ~200ms na auditoria contratual profunda do SLM (◐), perde em consumo de bateria e RAM por mobilizar NPU/CPU local frente à leveza extrema dos filtros estáticos em C/C++ de rede (✘), e perde em prontidão de validação em escala real por ser investigação científica em fase de prototipagem (✘).

## 6 · a contribuição

**a frase:** o Sentinela Clandestino correlaciona a semântica de persuasão e regras de saque da página de pouso com a topologia de infraestrutura de espelhos e APKs diretamente na borda do smartphone, e por isso expõe fraudes de calote e malwares no momento do redirecionamento com total privacidade local, o que nem os filtros de rede estáticos (Gamban/Netcraft) nem os classificadores em nuvem (Muzakir/Álvarez-Ojeda) conseguem realizar isoladamente.

**o trabalho mais próximo, e por que ele não chega lá:** o Trend Micro Check analisa links e prints de golpes com IA na nuvem, mas depende de envio manual proativo pelo usuário e avalia apenas reputação genérica, falhando em auditar cláusulas de retenção de saque em espelhos mutantes e em inspecionar manifestos de APKs piratas no momento do clique.

## 7 · tentei derrubar

o que a conversa nova achou: na auditoria adversária e confronto com alternativas sem IA, foi levantada a hipótese de que *"uma lista atualizada de chaves Pix e de domínios de bets ilegais bloqueada no teclado já resolveria o problema"*. Além disso, apontou-se que se o sistema apenas atuasse como um bloqueador autoritário tradicional, o apostador simplesmente o desinstalaria para continuar jogando.

o que eu mudei: refinei a contribuição demonstrando detalhadamente por que **a alternativa sem IA perde categoricamente para a realidade do crime organizado**, e como a IA resolve cada um dos três aspectos:
1. **Listas estáticas e teclados bloqueados falham:** operadores clandestinos geram centenas de espelhos mutantes por dia via DGA (.xyz, .top, .live). Nenhuma lista estática ou bloqueio de palavras-chave no teclado possui esses links porque eles são registrados minutos antes do disparo de campanhas em redes sociais.  
   **Como a IA resolve (direto ao ponto):** o agente MCP consulta um *digest* local de inferência em grafos de DNS passivo (pDNS), calculando a proximidade topológica do novo domínio com servidores e clusters de operadores criminosos conhecidos, bloqueando o espelho no instante zero sem depender de lista prévia.
2. **Pix dinâmico não tem chave prévia:** depósitos não utilizam chaves Pix ou CNPJs fixos cadastrados em tabelas públicas, mas APIs de PSPs/gateways que geram QR Codes dinâmicos em tempo real atrelados a contas rotativas de laranjas.  
   **Como a IA resolve (direto ao ponto):** o SLM *on-device* audita a semântica da *landing page* e termos de serviço, desmascarando cláusulas predatórias de retenção de saque (*rollover* abusivo de 50x e taxas de desbloqueio) e expondo o risco de *honeypot* (calote) antes que o usuário confirme o Pix no banco.
3. **APKs recompilados em massa (*MAMF*):** criminosos usam compilação automatizada (*Automated Mass Malware Factory* - Li et al., NDSS 2025) que modifica hashes SHA-256 e ofusca código a cada download, tornando antivírus tradicionais por assinatura inúteis.  
   **Como a IA resolve (direto ao ponto):** o SLM *on-device* analisa semanticamente a discrepância funcional entre o manifesto e o fluxo de bytecode Dex descompilado (identificando abuso de *Accessibility Service*, leitura de SMS para 2FA e sobreposição de tela bancária), neutralizando o trojan independentemente do seu hash binário.
4. **Canalização do interesse próprio do apostador:** a solução não é um bloqueador moralizante (que o usuário desinstalaria), mas um **auditor de integridade e risco**, protegendo o patrimônio do apostador pela sua própria vontade de não levar calote;
5. **Confronto de Modelos de Decisão (JEV vs. LAYA):** Avaliou-se o uso de modelos de decisão rápida (*System 1 Models*). O **JEV (TypeSafe AI)** foi rejeitado por operar exclusivamente via API proprietária em nuvem, o que violaria o pilar de privacidade local ao expor URLs e tráfego a servidores de terceiros. Optou-se pelo **LAYA (Convai Innovations)**, modelo *open-weights* (licença Apache-2.0, baseado em ModernBERT), executado 100% *on-device* em < 35ms para triagem instantânea (*Fast-Path*), despertando o SLM local apenas sob demanda para auditoria contratual profunda (*Deep-Path*).

## 8 · resumo, sem IA

Trend Micro, Gamban e filtros de teclado tentam conter fraudes por listas de domínios ou assinaturas estáticas.  
Nenhum combina modelo de decisão rápida de Sistema 1 e auditoria semântica de calote com grafos de DNS direto no celular.  
A minha ideia une triagem instantânea via LAYA (< 35ms) e grafos na borda, protegendo o apostador do calote com privacidade total.  
O trade-off técnico assumido é honesto: mobilizar inferência neural no aparelho consome mais bateria e RAM que filtros estáticos de rede.
