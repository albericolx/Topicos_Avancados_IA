# Sentinela Clandestino · Fluxograma e Arquitetura

O caminho completo da proteção, do clique do apostador no link até o alerta de evidências que volta para ele.  
Artefato **fluxograma e arquitetura** (`flx`) da disciplina de Tópicos Avançados de IA (UFRPE 2026.2).

Formas do diagrama:
- **Pessoa**: `([ ])` (estádio)
- **IA**: `{{ }}` (hexágono)
- **Regra**: `[ ]` (retângulo)
- **Armazenamento Local**: `[( )]` (cilindro)

---

## 1 · Diagrama do Fluxo Completo na Borda

```mermaid
flowchart TD
    subgraph AMB_EXT["1. Ambiente Externo: Redes Sociais e Navegação"]
        A(["1 · Usuário clica em link externo de aposta ou inicia download de APK em rede social"])
        I(["9 · Usuário visualiza evidências de calote e decide: aborta acesso ou prossegue consciente"])
    end

    subgraph BORDA_CEL["2. Smartphone do Usuário (Samsung Galaxy A15 / On-Device)"]
        subgraph INTERCEP["Camada de Interceptação do SO"]
            B["2 · Interceptor de Intent e Rede no SO captura URL e manifesto antes da abertura"]
        end

        subgraph TRIAGEM_FAST["Estágio 1: Triagem Imediata (< 35ms)"]
            C["3 · Consulta ao filtro de Bloom local do grafo pDNS para detecção de DGA de dia-zero"]
            D{{"4 · Fast-Path LAYA: triagem semântica probabilística do texto da página (< 35ms)"}}
            E{"5 · Risco flagrante ou conforme Portaria SPA/MF 1.475?"}
        end

        subgraph AUDITORIA_DEEP["Estágio 2: Auditoria Contratual Profunda (Sob Demanda)"]
            F{{"6 · Deep-Path SLM: Qwen2.5-0.5B INT4 via llama.cpp audita cláusulas de rollover e taxa PIX"}}
        end

        subgraph FORMAT_APRES["Camada de Apresentação e Tipagem Estruturada"]
            G["7 · Validador Pydantic tipa e estrutura o schema VereditoAuditoria"]
            H["8 · Painel Sentinela renderiza cartão de risco com evidências e latência"]
            DB[("Histórico Local Anônimo: contador de golpes prevenidos")]
        end
    end

    A --> B
    B --> C
    C --> D
    D --> E
    E -- "Sim (Flagrante ou SPA/MF direta)" --> G
    E -- "Dúvida / Cláusula complexa" --> F
    F --> G
    G --> H
    H --> I
    H --> DB
```

---

## 2 · Ciclo de Vida dos Dados Pessoais

| Dado Pessoal | De quem é | Onde fica | Quem vê | Por quanto tempo | Quando é apagado |
|:--|:--|:--|:--|:--|:--|
| **URL / Link de aposta clicado** | Usuário | Memória volátil (RAM) do app | Ninguém além do processo local do Sentinela | Menos de 1 segundo (tempo da inferência) | Imediatamente após a emissão do veredito |
| **Texto de termos de serviço / saque** | Da plataforma de apostas | Memória volátil (RAM) | Apenas o usuário ao ler o painel | Durante a exibição do alerta na tela | Ao fechar o painel de alerta |
| **Decisão do usuário (abortar / prosseguir)** | Usuário | Banco SQLite local seguro no aparelho | Apenas o usuário no seu resumo de proteção | Até a desinstalação do aplicativo | Sob demanda do usuário nas configurações do app |

> [!IMPORTANT]
> **Soberania Absoluta e Zero Telemetria:**  
> **Nenhum dado pessoal, URL ou texto de navegação sai do smartphone do usuário.** Não há tráfego de dados para servidores externos ou provedores de nuvem (zero dependência de rede para a auditoria semântica).
