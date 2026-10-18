# [3] artefato · base git repo · José Albérico Rocha da Silva

> **código no painel:** `git`  
> **pontuação total:** 6 pontos (3 itens de verificação · 2 pontos por item)  
> **repositório oficial:** [`albericolx/Topicos_Avancados_IA`](https://github.com/albericolx/Topicos_Avancados_IA)  
> **guia de referência:** [`lucassf.pages.dev/ai4good/artefatos/3-base-git-repo.md`](https://lucassf.pages.dev/ai4good/artefatos/3-base-git-repo.md)

---

## descrição

configuração instrumental inicial do ambiente de trabalho e repositório de código, assegurando soberania de versionamento e capacidade operacional via agentes inteligentes.

---

## pontos de verificação (checklist de evidências)

1. [x] **commit inaugural:** histórico do git com primeiro commit registrado e assinado pelo harness (agente inteligente) com mensagem estruturada.
2. [x] **árvore integrada:** arquitetura de pastas unificando `code/` (código-fonte), `article/` (projeto LaTeX) e documentações em um único repositório.
3. [x] **especificação modular:** presença de arquivos `.md` contextuais para cada diretório do workspace, iniciando com `AGENTS.md` na raiz e `CONTEXT.md` nas subpastas.

---

## 1 · evidência: commit inaugural

O repositório foi inicializado sob governança de **Workspace OS** e **GitFlow**, com o commit inaugural registrado e assinado pelo harness principal (**Antigravity / Gemini**) no padrão *Conventional Commits* (`feat(workspace): ...`) acompanhado de corpo descritivo estruturado e trailers `Signed-off-by` e `Co-Authored-By`.

- **Hash do Commit Inaugural:** [`6dee07bedf545a4eab110995010ba7dfb1f2793d`](https://github.com/albericolx/Topicos_Avancados_IA/commit/6dee07bedf545a4eab110995010ba7dfb1f2793d)
- **Histórico Completo de Commits (`main`):** [`github.com/albericolx/Topicos_Avancados_IA/commits/main`](https://github.com/albericolx/Topicos_Avancados_IA/commits/main)
- **Configuração Multi-Harness:** [`.agentrc.json`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/.agentrc.json) e [`code/SPECS-git.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/SPECS-git.md)

### Registro Literal do Commit Inaugural (`git show 6dee07b`)

```text
commit 6dee07bedf545a4eab110995010ba7dfb1f2793d
Author:     José Albérico Rocha da Silva <jose.alberico@ufrpe.br>
AuthorDate: Fri Aug 28 21:59:22 2026 -0300
Commit:     José Albérico Rocha da Silva <jose.alberico@ufrpe.br>
CommitDate: Fri Aug 28 21:59:22 2026 -0300

    feat(workspace): inicializar workspace de Topicos Avancados de IA com suporte a multi-harness, code, article LaTeX e core tools

    Configuracao instrumental inicial do ambiente de trabalho e repositorio de
    codigo (Workspace OS), assegurando soberania de versionamento via GitFlow
    e capacidade operacional via agentes inteligentes (multi-harness):

    - Ponto de entrada canonico na raiz (AGENTS.md, README.md, ROADMAP.md, ISSUES.md, .agentrc.json)
    - Arquitetura de pastas integrada unificando code/ (codigo-fonte), article/ e papers/ (projeto LaTeX) e core/ (automacao)
    - Especificacao modular com CONTEXT.md e SPECS.md em cada diretorio do workspace

    Signed-off-by: Antigravity Harness (Google DeepMind) <agent@antigravity.local>
    Co-Authored-By: Antigravity (Gemini) <noreply@google.com>
```

---

## 2 · evidência: árvore integrada

O repositório unifica em uma única árvore versionada o desenvolvimento de código-fonte ([`code/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/code)), o projeto completo do artigo científico em LaTeX ([`article/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/article) e espelho Overleaf em [`papers/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/papers)), o ferramental de automação ([`core/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/core)) e as documentações e artefatos da disciplina ([`artefatos/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/artefatos) e [`va2/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/va2)):

```text
Topicos_Avancados_IA/
├── AGENTS.md                        # Normas canônicas e ponto de entrada para agentes de IA (Harness)
├── README.md                        # Visão geral, arquitetura e guia operacional do workspace
├── ROADMAP.md                       # Cronograma de entregas e acompanhamento de fases
├── ISSUES.md                        # Registro de tarefas, pendências e histórico de decisões
├── .agentrc.json                    # Manifesto de configuração multi-harness e mapeamento de módulos
├── .gitignore                       # Exclusão de segredos (.env), caches e artefatos temporários
│
├── code/                            # [CÓDIGO-FONTE] Modelos neurais, grafos explícitos e experimentos
│   ├── CONTEXT.md                   # Especificação contextual do módulo de código
│   ├── SPECS-git.md                 # Regras de branches, commits estruturados e governança GitFlow
│   └── src/                         # Implementações dos modelos, treinamento e geração de gráficos
│       ├── CONTEXT.md               # Especificação contextual da subpasta de código-fonte
│       └── README.md                # Guia dos subpacotes (models, train, data, plots)
│
├── article/                         # [PROJETO LATEX] Manuscrito científico unificado (Springer LNCS)
│   ├── CONTEXT.md                   # Especificação contextual do projeto LaTeX
│   ├── SPECS.md                     # Normas de rigor bibliográfico e formatação Springer LNCS
│   ├── main.tex                     # Arquivo mestre LaTeX (José Albérico Rocha da Silva — UFRPE)
│   ├── references.bib               # Base de referências bibliográficas verificadas (BibTeX)
│   ├── llncs.cls                    # Classe oficial Springer LNCS
│   ├── splncs04.bst                 # Estilo bibliográfico Springer LNCS
│   ├── sections/                    # Seções modulares do artigo (01_introducao a 05_conclusao)
│   │   ├── CONTEXT.md               # Mapa contextual das seções do artigo
│   │   ├── 01_introducao.tex
│   │   ├── 02_trabalhos_relacionados.tex
│   │   ├── 03_metodologia.tex
│   │   ├── 04_experimentos.tex
│   │   └── 05_conclusao.tex
│   └── figures/                     # Figuras, diagramas e curvas experimentais do artigo
│       ├── CONTEXT.md               # Diretrizes contextuais de figuras científicas
│       └── fig1.eps
│
├── papers/                          # [ESPELHO OVERLEAF] Sincronização bidirecional com Overleaf
│   ├── CONTEXT.md                   # Contexto de integração com o repositório Overleaf
│   └── SPECS.md                     # Diretrizes de escrita e compilação
│
├── core/                            # [FERRAMENTAS DO WORKSPACE] Automação agnóstica de provedor
│   ├── CONTEXT.md                   # Especificação contextual do módulo core
│   └── tools/                       # Scripts de busca acadêmica, compilação LaTeX e sync Overleaf
│       ├── CONTEXT.md               # Especificação contextual das ferramentas CLI
│       ├── academic_search.py       # Busca de artigos (arXiv / CrossRef) e geração de BibTeX
│       ├── compile_paper.py         # Compilador local automatizado de LaTeX para PDF
│       └── overleaf_sync.py         # Assistente de sincronização com Overleaf
│
├── artefatos/                       # [EVIDÊNCIAS DE VERIFICAÇÃO] Documentação de artefatos da disciplina
│   ├── CONTEXT.md                   # Especificação contextual da pasta de artefatos
│   └── 3-base-git-repo.md           # Este documento de evidência (Artefato [3] · base git repo)
│
└── va2/                             # [PROJETO AI4GOOD — VA2] Ideação e Trabalhos Relacionados
    ├── CONTEXT.md                   # Especificação contextual das entregas da VA2
    ├── brw.md                       # Artefato Brainwriting Híbrido (Sentinela Clandestino)
    └── cmp.md                       # Artefato Competidores e Contribuição (auditado)
```

### Links Diretos para os Diretórios Unificados no GitHub
- **Raiz do Repositório:** [`github.com/albericolx/Topicos_Avancados_IA`](https://github.com/albericolx/Topicos_Avancados_IA)
- **Módulo de Código (`code/`):** [`github.com/albericolx/Topicos_Avancados_IA/tree/main/code`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/code)
- **Módulo de Artigo LaTeX (`article/`):** [`github.com/albericolx/Topicos_Avancados_IA/tree/main/article`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/article)
- **Módulo de Ferramentas (`core/`):** [`github.com/albericolx/Topicos_Avancados_IA/tree/main/core`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/core)
- **Documentações da Raiz:** [`AGENTS.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/AGENTS.md) · [`README.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/README.md) · [`ROADMAP.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/ROADMAP.md) · [`ISSUES.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/ISSUES.md)

---

## 3 · evidência: especificação modular (`AGENTS.md` e `CONTEXT.md`)

Cada diretório e subpasta do workspace possui seu respectivo arquivo `.md` contextual para orientar qualquer agente inteligente (harness principal ou de backup) sem depender de memória volátil de chat:

| Diretório | Arquivo Contextual (Link Direto) | Papel no Workspace |
|---|---|---|
| `/` *(Raiz)* | [`AGENTS.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/AGENTS.md) | Ponto de entrada canônico, regras inegociáveis (sistema de arquivos como fonte da verdade, multi-harness, GitFlow, rigor acadêmico) e tabela de roteamento |
| `/` *(Raiz)* | [`README.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/README.md) · [`ROADMAP.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/ROADMAP.md) · [`ISSUES.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/ISSUES.md) | Visão geral da arquitetura, cronograma de fases/entregas e registro de pendências/decisões |
| `code/` | [`code/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/CONTEXT.md) · [`code/SPECS-git.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/SPECS-git.md) | Diretrizes de desenvolvimento reprodutível (`seed` fixa, modularidade) e especificação de branches/commits (GitFlow) |
| `code/src/` | [`code/src/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/code/src/CONTEXT.md) | Organização dos pacotes de código-fonte (`models/`, `train/`, `data/`, `plots/`) |
| `article/` | [`article/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/CONTEXT.md) · [`article/SPECS.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/SPECS.md) | Estrutura do projeto LaTeX unificado (Springer LNCS), fluxo de compilação e normas de escrita acadêmica |
| `article/sections/` | [`article/sections/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/sections/CONTEXT.md) | Mapeamento das 5 seções modulares (`.tex`) que compõem o artigo científico |
| `article/figures/` | [`article/figures/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/figures/CONTEXT.md) | Padrões de resolução, formatos vetoriais e rastreabilidade dos gráficos gerados pelo código |
| `papers/` | [`papers/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/CONTEXT.md) · [`papers/SPECS.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/SPECS.md) | Configuração e instruções de sincronização direta com o projeto remoto no Overleaf |
| `core/` | [`core/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/CONTEXT.md) | Roteamento de ferramentas e utilitários de suporte do workspace |
| `core/tools/` | [`core/tools/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/CONTEXT.md) | Documentação operacional dos scripts `academic_search.py`, `compile_paper.py` e `overleaf_sync.py` |
| `artefatos/` | [`artefatos/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/artefatos/CONTEXT.md) | Índice de artefatos e folhas de verificação da disciplina |
| `va2/` | [`va2/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/va2/CONTEXT.md) | Contexto das atividades da 2ª Verificação de Aprendizagem (`brw.md` e `cmp.md`) |
| `Atividade_03_LOOP_Agentes/` | [`Atividade_03_LOOP_Agentes/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/Atividade_03_LOOP_Agentes/CONTEXT.md) · [`logs/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/Atividade_03_LOOP_Agentes/logs/CONTEXT.md) | Arquitetura e logs do experimento de simulação com loop de múltiplos agentes (Gemini + Ollama) |
