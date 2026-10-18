# Workspace: Tópicos Avançados de IA (UFRPE 2026.2)
> Ambiente unificado de desenvolvimento de modelos neurais, experimentação empírica e confecção de artigo científico em LaTeX.

Este workspace segue a filosofia de **Workspace OS** inspirada em [`lsfcin/workspace`](https://github.com/lsfcin/workspace), integrando na raiz o desenvolvimento prático de redes neurais ([`code/`](code/CONTEXT.md)), a confecção do artigo científico no padrão **Springer LNCS** ([`article/`](article/CONTEXT.md) e [`papers/`](papers/CONTEXT.md)), ferramentas de automação ([`core/`](core/CONTEXT.md)) e artefatos da disciplina ([`artefatos/`](artefatos/CONTEXT.md) e [`va2/`](va2/CONTEXT.md)), com suporte a múltiplos agentes de IA (**harness principal e de backup**), integração contínua com o **Overleaf** e governança por **GitFlow**.

---

## Evidências de Verificação — `[3] artefato · base git repo` (`git`)

> Folha consolidada de evidências: **[`artefatos/3-base-git-repo.md`](artefatos/3-base-git-repo.md)**

1. **Commit Inaugural (assinado pelo harness com mensagem estruturada):**
   - Commit inicial [`6dee07bedf545a4eab110995010ba7dfb1f2793d`](https://github.com/albericolx/Topicos_Avancados_IA/commit/6dee07bedf545a4eab110995010ba7dfb1f2793d) registrado com mensagem estruturada (*Conventional Commits*) e assinado pelo harness (`Signed-off-by: Antigravity Harness` / `Co-Authored-By: Antigravity (Gemini)`).
2. **Árvore Integrada (`code/`, `article/` e documentações em repositório único):**
   - Código-fonte em [`code/`](code/), projeto LaTeX completo em [`article/`](article/) (com espelho Overleaf em [`papers/`](papers/)), automação em [`core/`](core/) e documentações na raiz ([`AGENTS.md`](AGENTS.md), [`README.md`](README.md), [`ROADMAP.md`](ROADMAP.md), [`ISSUES.md`](ISSUES.md)).
3. **Especificação Modular (`AGENTS.md` na raiz e `CONTEXT.md` nas subpastas):**
   - Raiz: [`AGENTS.md`](AGENTS.md)
   - Subpastas: [`code/CONTEXT.md`](code/CONTEXT.md), [`code/src/CONTEXT.md`](code/src/CONTEXT.md), [`article/CONTEXT.md`](article/CONTEXT.md), [`article/sections/CONTEXT.md`](article/sections/CONTEXT.md), [`article/figures/CONTEXT.md`](article/figures/CONTEXT.md), [`papers/CONTEXT.md`](papers/CONTEXT.md), [`core/CONTEXT.md`](core/CONTEXT.md), [`core/tools/CONTEXT.md`](core/tools/CONTEXT.md), [`artefatos/CONTEXT.md`](artefatos/CONTEXT.md), [`va2/CONTEXT.md`](va2/CONTEXT.md) e [`Atividade_03_LOOP_Agentes/CONTEXT.md`](Atividade_03_LOOP_Agentes/CONTEXT.md).

---

## Estrutura do Workspace

```text
Topicos_Avancados_IA/
├── AGENTS.md                 # Normas canônicas para agentes de IA (Harness)
├── README.md                 # Visão geral e guia rápido do workspace
├── ROADMAP.md                # Cronograma de entregas e fases dos experimentos
├── ISSUES.md                 # Registro de pendências e débitos técnicos
├── .agentrc.json             # Configuração multi-harness e mapeamento modular
├── .gitignore                # Regras de exclusão para Git (LaTeX, PyTorch, Python, .env)
│
├── code/                     # Modelos de IA e códigos experimentais
│   ├── CONTEXT.md            # Mapa e contexto da pasta code/
│   ├── SPECS-git.md          # Especificação detalhada do GitFlow
│   └── src/                  # Arquiteturas neurais, grafos explícitos e treinamento
│       ├── CONTEXT.md        # Contexto da subpasta de código-fonte
│       └── README.md         # Estrutura de pacotes (models, train, data, plots)
│
├── article/                  # Projeto LaTeX unificado no repositório (Springer LNCS)
│   ├── CONTEXT.md            # Mapa e contexto da pasta article/
│   ├── SPECS.md              # Normas de formatação Springer LNCS
│   ├── main.tex              # Arquivo mestre (José Albérico Rocha da Silva — UFRPE)
│   ├── llncs.cls             # Classe Springer LNCS
│   ├── splncs04.bst          # Estilo bibliográfico Springer
│   ├── references.bib        # Banco de referências bibliográficas
│   ├── sections/             # Seções modulares (01_introducao a 05_conclusao)
│   │   └── CONTEXT.md        # Contexto das seções do artigo
│   └── figures/              # Gráficos de perda, acurácia e topologia de rede
│       └── CONTEXT.md        # Contexto das figuras científicas
│
├── papers/                   # Espelho de sincronização direta com o Overleaf
│   ├── CONTEXT.md            # Mapa e contexto da pasta papers/
│   └── SPECS.md              # Normas de formatação Springer LNCS
│
├── core/                     # Ferramentas auxiliares e automação
│   ├── CONTEXT.md            # Contexto dos utilitários
│   └── tools/                # Scripts de suporte
│       ├── CONTEXT.md        # Contexto das ferramentas CLI
│       ├── academic_search.py # Busca papers no arXiv / CrossRef e gera BibTeX
│       ├── compile_paper.py   # Compilador rápido de LaTeX para PDF local
│       └── overleaf_sync.py   # Assistente de sincronização com Overleaf
│
├── artefatos/                # Evidências estruturadas dos pontos de verificação
│   ├── CONTEXT.md            # Contexto dos artefatos da disciplina
│   └── 3-base-git-repo.md    # Evidências completas do Artefato [3] · base git repo
│
└── va2/                      # Segunda Verificação de Aprendizagem (AI4Good)
    ├── CONTEXT.md            # Contexto dos artefatos de VA2
    ├── brw.md                # Brainwriting Híbrido
    └── cmp.md                # Competidores e Contribuição
```

---

## Guia Rápido de Uso

### 1. Harness Principal e Backup (Quando a cota acabar)
* **Harness Principal**: Antigravity (Gemini).
* **Harness de Backup**: VS Code (com GitHub Copilot / Claude Code / OpenCode).
* **Como trocar**: Abra esta pasta no VS Code e a IA continuará a tarefa lendo [`AGENTS.md`](AGENTS.md) e [`ISSUES.md`](ISSUES.md).

### 2. Compilar o Artigo LaTeX Localmente
```bash
py core/tools/compile_paper.py
```
O PDF gerado ficará disponível em `article/main.pdf`.

### 3. Sincronizar com o Overleaf
```bash
py core/tools/overleaf_sync.py --zip
```

### 4. Buscar Artigos Científicos para a Disciplina
```bash
py core/tools/academic_search.py --query "explicit computation graph neural networks" --limit 5
```
