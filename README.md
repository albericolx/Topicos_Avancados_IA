# Workspace: Tópicos Avançados de IA (UFRPE 2026.2)
> Ambiente unificado de desenvolvimento de modelos neurais, experimentação empírica, gerenciamento automatizado de literatura e confecção de artigo científico em LaTeX.

Este workspace segue a filosofia de **Workspace OS** inspirada em [`lsfcin/workspace`](https://github.com/lsfcin/workspace), integrando na raiz o desenvolvimento prático de redes neurais ([`code/`](code/CONTEXT.md)), a confecção e compilação local do artigo científico no padrão **Springer LNCS** ([`article/`](article/CONTEXT.md) e [`papers/`](papers/CONTEXT.md)), o pipeline de referências com OCR zero-token ([`refs/`](refs/CONTEXT.md)), o módulo de habilidades e fluxos de pesquisa ([`core/`](core/CONTEXT.md) e [`.agents/`](.agents/CONTEXT.md)) e os artefatos de verificação da disciplina ([`artefatos/`](artefatos/CONTEXT.md) e [`va2/`](va2/CONTEXT.md)).

---

## Evidências de Verificação dos Artefatos

### `[4] artefato · latex project` (`tex` · 8 pontos)
> Folha consolidada de evidências: **[`artefatos/4-latex-project.md`](artefatos/4-latex-project.md)**

1. **Compilação Local (`.tex` $\rightarrow$ `.pdf` via harness):**
   - Compilador automatizado [`core/tools/compile_paper.py`](core/tools/compile_paper.py) executando ciclo MiKTeX (`pdflatex` + `bibtex` x3) com o PDF compilado e versionado em **[`article/main.pdf`](article/main.pdf)** (3 páginas, 6 referências BibTeX resolvidas, `0 warnings`).
2. **Integração Overleaf (conexão bidirecional e contribuições do harness):**
   - Conexão bidirecional Git (`https://git.overleaf.com/6a92242dbaaa2c6b6833bab0`) em [`papers/artigo-final`](papers/CONTEXT.md), gerenciada por [`core/tools/overleaf_sync.py`](core/tools/overleaf_sync.py), com commits enviados pelo harness (`3dc40d5` e `77d47ac`).
3. **Pipeline de Referências (busca, download de PDF, OCR zero-token e `.yaml` em `refs/`):**
   - Busca multi-base, download de PDFs e geração de `.yaml` em [`core/tools/academic_search.py`](core/tools/academic_search.py) + extração zero-token em [`core/tools/pdf_ocr_parser.py`](core/tools/pdf_ocr_parser.py) + pasta estruturada [`refs/`](refs/CONTEXT.md) (e espelho [`article/refs/`](article/refs/CONTEXT.md)) contendo [`refs/REFS.md`](refs/REFS.md), 6 fichas `.yaml`, PDF acadêmico em [`refs/pdfs/`](refs/pdfs/CONTEXT.md) e extrações em [`refs/ocr/`](refs/ocr/CONTEXT.md).
4. **Árvore de Pesquisa (módulo de pesquisa, *skills*, fluxos e agentes):**
   - Habilidades em [`core/skills/`](core/skills/CONTEXT.md) ([`research.md`](core/skills/research.md), [`literature-review.md`](core/skills/literature-review.md), [`methodology-formulation.md`](core/skills/methodology-formulation.md), [`technical-writing.md`](core/skills/technical-writing.md)) e [`.agents/skills/research/SKILL.md`](.agents/skills/research/SKILL.md); fluxos em [`core/flows/research/`](core/flows/research/CONTEXT.md) ([`literature.md`](core/flows/research/literature.md), [`methodology.md`](core/flows/research/methodology.md), [`draft.md`](core/flows/research/draft.md), [`review.md`](core/flows/research/review.md)); e agentes em [`core/agents/`](core/agents/CONTEXT.md).

---

### `[3] artefato · base git repo` (`git` · 6 pontos)
> Folha consolidada de evidências: **[`artefatos/3-base-git-repo.md`](artefatos/3-base-git-repo.md)**

1. **Commit Inaugural:** Commit inicial [`6dee07bedf545a4eab110995010ba7dfb1f2793d`](https://github.com/albericolx/Topicos_Avancados_IA/commit/6dee07bedf545a4eab110995010ba7dfb1f2793d) assinado pelo harness.
2. **Árvore Integrada:** Arquitetura unificando [`code/`](code/), [`article/`](article/), [`refs/`](refs/), [`core/`](core/) e documentações na raiz.
3. **Especificação Modular:** [`AGENTS.md`](AGENTS.md) na raiz e `CONTEXT.md` em todas as subpastas do workspace.

---

## Estrutura do Workspace

```text
Topicos_Avancados_IA/
├── AGENTS.md                 # Normas canônicas para agentes de IA (Harness)
├── README.md                 # Visão geral e guia rápido do workspace
├── ROADMAP.md                # Cronograma de entregas e fases dos experimentos
├── ISSUES.md                 # Registro de pendências e débitos técnicos
├── .agentrc.json             # Configuração multi-harness e mapeamento modular
│
├── code/                     # Modelos de IA e códigos experimentais
│   ├── CONTEXT.md            # Mapa e contexto da pasta code/
│   ├── SPECS-git.md          # Especificação detalhada do GitFlow
│   └── src/                  # Arquiteturas neurais, grafos explícitos e treinamento
│       └── CONTEXT.md        # Contexto da subpasta de código-fonte
│
├── article/                  # Projeto LaTeX unificado no repositório (Springer LNCS)
│   ├── CONTEXT.md            # Mapa e contexto da pasta article/
│   ├── SPECS.md              # Normas de formatação Springer LNCS
│   ├── main.tex              # Arquivo mestre (José Albérico Rocha da Silva — UFRPE)
│   ├── main.pdf              # PDF compilado localmente via harness
│   ├── references.bib        # Banco de referências bibliográficas (6 entradas)
│   ├── refs/                 # Espelho local de fichas .yaml, PDFs e OCR zero-token
│   ├── sections/             # Seções modulares (01_introducao a 05_conclusao)
│   └── figures/              # Gráficos de perda, acurácia e topologia de rede
│
├── refs/                     # Pipeline de referências acadêmicas e OCR zero-token
│   ├── CONTEXT.md            # Especificação do pipeline de referências
│   ├── REFS.md               # Índice Tier-1 ([A], [B], [L], [P])
│   ├── *.yaml                # 6 fichas catalográficas Tier-2 estruturadas
│   ├── pdfs/                 # PDFs acadêmicos baixados (vaswani2017attention.pdf)
│   └── ocr/                  # Extrações de texto zero-token (.txt)
│
├── papers/                   # Espelho de sincronização bidirecional com o Overleaf
│   ├── CONTEXT.md            # Mapa e contexto da pasta papers/
│   ├── SPECS.md              # Normas de formatação
│   └── artigo-final/         # Repositório vinculado ao Git do Overleaf
│
├── core/                     # Ferramentas, Skills, Fluxos de Pesquisa e Agentes
│   ├── CONTEXT.md            # Contexto geral do módulo core/
│   ├── tools/                # compile_paper.py, overleaf_sync.py, academic_search.py, pdf_ocr_parser.py
│   ├── skills/               # research.md, literature-review.md, methodology-formulation.md, technical-writing.md
│   ├── flows/research/       # literature.md, methodology.md, draft.md, review.md
│   └── agents/               # researcher.md, writer.md, reviewer.md
│
├── .agents/                  # Descoberta nativa de skills pelo harness
│   └── skills/research/      # SKILL.md
│
├── artefatos/                # Evidências estruturadas dos pontos de verificação
│   ├── CONTEXT.md            # Contexto dos artefatos da disciplina
│   ├── 3-base-git-repo.md    # Evidências do Artefato [3] · base git repo (git)
│   └── 4-latex-project.md    # Evidências do Artefato [4] · latex project (tex)
│
└── va2/                      # Segunda Verificação de Aprendizagem (AI4Good)
    ├── CONTEXT.md            # Contexto dos artefatos de VA2
    ├── brw.md                # Brainwriting Híbrido
    └── cmp.md                # Competidores e Contribuição
```
