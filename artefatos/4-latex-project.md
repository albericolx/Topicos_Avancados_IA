# Evidências de Verificação — `[4] artefato · latex project`

- **Disciplina:** Tópicos Avançados em Inteligência Artificial (AI4Good — UFRPE 2026.2)
- **Atividade no Projeto:** `[4] artefato · latex project`
- **Código no Painel:** `tex`
- **Pontuação Total:** 8 pontos (4 itens de verificação · 2 pontos por item)
- **Discente:** José Albérico Rocha da Silva
- **Harness Operacional:** Antigravity (Google DeepMind — Agente Inteligente de Codificação)
- **Repositório Canônico:** [`https://github.com/albericolx/Topicos_Avancados_IA`](https://github.com/albericolx/Topicos_Avancados_IA)

---

## Descrição da Atividade
> *"infraestrutura de redação científica rigorosa, integrando compilação local via harness, sincronização com Overleaf e gerenciamento automatizado de literatura acadêmica."*

---

## Quadro-Resumo dos Pontos de Verificação

| # | Ponto de Verificação | Pontuação | Status | Evidência Principal no Repositório |
|---|---|---:|---|---|
| **1** | **Compilação Local** | 2 pts | Concluído | Compilador automatizado [`core/tools/compile_paper.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/compile_paper.py) + PDF compilado via harness em [`article/main.pdf`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/main.pdf) a partir de [`article/main.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/main.tex) |
| **2** | **Integração Overleaf** | 2 pts | Concluído | Conexão bidirecional Git (`https://git.overleaf.com/6a92242dbaaa2c6b6833bab0`) em [`papers/artigo-final`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/papers) + ferramenta [`core/tools/overleaf_sync.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/overleaf_sync.py) + commits enviados pelo harness (`3dc40d5` e `77d47ac`) |
| **3** | **Pipeline de Referências** | 2 pts | Concluído | Busca + download de PDF + geração `.yaml` em [`core/tools/academic_search.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/academic_search.py), OCR zero-token em [`core/tools/pdf_ocr_parser.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/pdf_ocr_parser.py) e pasta estruturada [`refs/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/refs) (espelhada em [`article/refs/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/article/refs)) |
| **4** | **Árvore de Pesquisa** | 2 pts | Concluído | Módulo de *skills* e fluxos de pesquisa em [`core/skills/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/core/skills), [`core/flows/research/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/core/flows/research), [`core/agents/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/core/agents) e [`.agents/skills/research/SKILL.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/.agents/skills/research/SKILL.md) |

---

## 1. Ponto de Verificação: Compilação Local (2 pontos)

> **Requisito:** *"ferramentas de compilação de .tex para .pdf funcionais no ambiente local, com o primeiro PDF compilado com sucesso via harness."*

### Evidências Instrumentais
- **Ferramenta de Compilação Local via Harness:** [`core/tools/compile_paper.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/compile_paper.py)
  - Detecta automaticamente os binários locais do MiKTeX (`pdflatex`, `bibtex`, `latexmk`) no ambiente Windows/Linux/macOS.
  - Executa o ciclo completo de 4 passos (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`) garantindo a resolução integral de referências cruzadas e citações bibliográficas.
- **Código-Fonte LaTeX Modular (Springer LNCS):**
  - Documento mestre: [`article/main.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/main.tex)
  - Base BibTeX (6 referências verificadas): [`article/references.bib`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/references.bib)
  - Seções modulares:
    - [`article/sections/01_introducao.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/sections/01_introducao.tex)
    - [`article/sections/02_trabalhos_relacionados.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/sections/02_trabalhos_relacionados.tex)
    - [`article/sections/03_metodologia.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/sections/03_metodologia.tex)
    - [`article/sections/04_experimentos.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/sections/04_experimentos.tex)
    - [`article/sections/05_conclusao.tex`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/sections/05_conclusao.tex)
- **Primeiro PDF Compilado com Sucesso via Harness:**
  - Arquivo PDF gerado e versionado: **[`article/main.pdf`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/main.pdf)** (3 páginas, `200.620 bytes`, 6 referências BibTeX compiladas com `0 warnings`).
  - Extração textual de verificação do PDF compilado: [`refs/ocr/main_compiled_article.txt`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/ocr/main_compiled_article.txt).

### Registro de Execução pelo Harness (`compile_paper.py` + `bibtex`)
```text
$ py core/tools/compile_paper.py
[Iniciando Compilação] Alvo: article/main.tex

[Compilador] Executando ciclo pdflatex + bibtex...
Passo 1/4: pdflatex...
Passo 2/4: bibtex...
  This is BibTeX, Version 0.99e
  The style file: splncs04.bst
  Database file #1: references.bib
  You've used 6 entries, 2850 wiz_defined-function locations,
  warning$ -- 0
Passo 3/4: pdflatex (resolvendo referências)...
Passo 4/4: pdflatex final...
  Output written on main.pdf (3 pages, 200620 bytes).

[SUCESSO] PDF gerado com êxito em:
=> article/main.pdf
```

---

## 2. Ponto de Verificação: Integração Overleaf (2 pontos)

> **Requisito:** *"conexão bidirecional estabelecida com projeto no Overleaf, registrando a primeira contribuição enviada diretamente pelo harness."*

### Evidências Instrumentais
- **Ferramenta de Sincronização Bidirecional:** [`core/tools/overleaf_sync.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/overleaf_sync.py)
  - Suporta verificação de status e histórico Git Overleaf (`--status`), configuração do remoto Git (`--git-setup`), exportação de pacote limpo (`--zip`) e importação (`--import-zip`), com sanitização automática de credenciais (`***TOKEN_REDACTED***`).
- **Documentação do Espelho Overleaf:** [`papers/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/CONTEXT.md) e [`papers/SPECS.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/papers/SPECS.md).
- **Conexão Git Bidirecional e Contribuições Registradas no Overleaf:**
  - Remoto Overleaf vinculado em `papers/artigo-final`: `https://git.overleaf.com/6a92242dbaaa2c6b6833bab0`
  - **Primeira contribuição enviada diretamente pelo harness ao Overleaf:**
    - Commit Overleaf `3dc40d5ac1bcaae13f20c4d88e46a612698fbf4f` — `Atualiza autoria para José Albérico Rocha da Silva` (`Author: José Albérico Rocha da Silva <jose.alberico@ufrpe.br>`).
  - **Segunda contribuição completa enviada pelo harness ao Overleaf:**
    - Commit Overleaf `77d47ac922641d187f68d9d19d30359b4f9dc38d` — `feat: relatorio tecnico completo Atividade 01 MLP` (6 arquivos alterados, 635 inserções em `main.tex`, `references.bib`, `sections/01_introducao.tex`, `sections/02_metodo.tex`, `sections/03_resultados.tex`).

### Saída Verificada via Harness (`py core/tools/overleaf_sync.py --status`)
```text
$ py core/tools/overleaf_sync.py --status
[Overleaf Sync] Verificando repositório espelho em: papers/artigo-final

[Remoto Configurado (Token Sanitizado)]:
origin  https://git:***TOKEN_REDACTED***@git.overleaf.com/6a92242dbaaa2c6b6833bab0 (fetch)
origin  https://git:***TOKEN_REDACTED***@git.overleaf.com/6a92242dbaaa2c6b6833bab0 (push)

[Histórico de Contribuições Sincronizadas com Overleaf]:
34df67b Estruturacao do artigo em ABNT com os 5 autores e introducao consolidada com os 4 problemas
aa41a1d Merge branch 'main' of https://git.overleaf.com/6a92242dbaaa2c6b6833bab0
7a259e2 Adiciona relatorio tecnico individual (Dayana): aprendizado personalizado como privilegio
98ad080 Remove arquivo antigo para forçar o Overleaf a ler o main.tex novo
97a5966 Atualiza artigo com normas ABNT e informações do aluno
ad46f6d fix: main.tex re-salvo em UTF-8 sem BOM, capa ABNT refinada
77d47ac feat: relatorio tecnico completo Atividade 01 MLP
b059248 Adiciona Dayana Cristina como coautora
3dc40d5 Atualiza autoria para José Albérico Rocha da Silva
e10610d Atualiza autoria em samplepaper.tex para Kauã Fabrício Pereira da Cunha
d79aea4 Atualiza autoria para Kauã Fabrício Pereira da Cunha
6f22efa Update on Overleaf.
```

---

## 3. Ponto de Verificação: Pipeline de Referências (2 pontos)

> **Requisito:** *"ferramentas de busca acadêmica com download de PDFs, OCR automático (zero-token) e pasta refs/ estruturada com geração automática de metadados em .yaml."*

### Evidências Instrumentais
1. **Ferramenta de Busca Acadêmica, Download de PDFs e Geração Automática de `.yaml`:**
   - Script: **[`core/tools/academic_search.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/academic_search.py)**
   - Integra busca multi-fonte (**Semantic Scholar API**, **CrossRef API**, **OpenAlex API** e **arXiv API**) com deduplicação automática por DOI/título.
   - Suporta flags de automação via linha de comando:
     - `--download-pdf`: baixa automaticamente PDFs *Open Access* para [`refs/pdfs/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/refs/pdfs).
     - `--generate-yaml`: gera automaticamente a ficha catalográfica `.yaml` estruturada em [`refs/`](https://github.com/albericolx/Topicos_Avancados_IA/tree/main/refs) e dispara a extração de texto zero-token quando há PDF disponível.
     - `--add-to-bib`: registra a entrada BibTeX verificada diretamente em [`article/references.bib`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/references.bib).
2. **Ferramenta de Extração de Texto e OCR Automático Zero-Token:**
   - Script: **[`core/tools/pdf_ocr_parser.py`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/tools/pdf_ocr_parser.py)**
   - Extrai texto localmente sem consumir tokens da janela de contexto do LLM:
     - **Camada 1 (Nativa):** `pdftotext` (Poppler) ou `pypdf` para PDFs digitais nativos.
     - **Camada 2 (Fallback OCR Automático):** quando o texto extraído é insuficiente (`< 80` caracteres) ou `--ocr` é acionado, rasteriza páginas em 300 DPI via `pdftoppm` e executa `tesseract` OCR localmente.
   - **Arquivos de PDF e OCR Zero-Token Gerados:**
     - PDF acadêmico baixado: [`refs/pdfs/vaswani2017attention.pdf`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/pdfs/vaswani2017attention.pdf)
     - Texto extraído zero-token (Vaswani et al., 2017): [`refs/ocr/vaswani2017attention.txt`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/ocr/vaswani2017attention.txt)
     - Texto extraído zero-token (Manuscrito compilado `main.pdf`): [`refs/ocr/main_compiled_article.txt`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/ocr/main_compiled_article.txt)
3. **Pasta `refs/` Estruturada (com espelho em `article/refs/`) e Metadados `.yaml`:**
   - Documentação e Especificação de Níveis (Tier-1 / Tier-2 / Tier-3): [`refs/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/CONTEXT.md)
   - Índice Tier-1 de Referências Capturadas (`[A]`, `[B]`, `[L]`, `[P]`): [`refs/REFS.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/REFS.md)
   - **Fichas de Metadados `.yaml` (Tier-2) sincronizadas com [`article/references.bib`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/references.bib):**

| Chave BibTeX | Tier | Ficha de Metadados `.yaml` (`refs/`) | Espelho em `article/refs/` |
|---|:-:|---|---|
| `rumelhart1986learning` | `[A]` | [`refs/rumelhart1986learning.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/rumelhart1986learning.yaml) | [`article/refs/rumelhart1986learning.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/refs/rumelhart1986learning.yaml) |
| `goodfellow2016deep` | `[L]` | [`refs/goodfellow2016deep.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/goodfellow2016deep.yaml) | [`article/refs/goodfellow2016deep.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/refs/goodfellow2016deep.yaml) |
| `vaswani2017attention` | `[A]` | [`refs/vaswani2017attention.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/vaswani2017attention.yaml) | [`article/refs/vaswani2017attention.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/refs/vaswani2017attention.yaml) |
| `nabeel2020following` | `[A]` | [`refs/nabeel2020following.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/nabeel2020following.yaml) | [`article/refs/nabeel2020following.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/refs/nabeel2020following.yaml) |
| `muzakir2025text` | `[B]` | [`refs/muzakir2025text.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/muzakir2025text.yaml) | [`article/refs/muzakir2025text.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/refs/muzakir2025text.yaml) |
| `alvarezojeda2025precom` | `[A]` | [`refs/alvarezojeda2025precom.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/refs/alvarezojeda2025precom.yaml) | [`article/refs/alvarezojeda2025precom.yaml`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/article/refs/alvarezojeda2025precom.yaml) |

---

## 4. Ponto de Verificação: Árvore de Pesquisa (2 pontos)

> **Requisito:** *"módulo de pesquisa e habilidades (skills) adicionado ao workspace para apoio a leitura/revisão bibliográfica, formulação metodológica e redação técnica."*

### Evidências Instrumentais
A arquitetura de pesquisa e habilidades (*skills*) foi estruturada em quatro camadas modulares e agnósticas de provedor:

#### 4.1. Módulo de Habilidades (`core/skills/` e `.agents/skills/`)
- [`core/skills/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/skills/CONTEXT.md): Mapa de roteamento das habilidades científicas do workspace.
- [`core/skills/SPECS.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/skills/SPECS.md): Padrão arquitetural de especificação de *skills* multi-harness.
- [`core/skills/research.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/skills/research.md): *Skill* mestra de pesquisa científica (roteador central para revisão bibliográfica, metodologia, redação e auditoria).
- [`core/skills/literature-review.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/skills/literature-review.md): Habilidade dedicada à leitura, fichamento YAML, extração OCR zero-token e revisão sistemática da literatura.
- [`core/skills/methodology-formulation.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/skills/methodology-formulation.md): Habilidade dedicada à formulação de questões de pesquisa, hipóteses falsificáveis, variáveis experimentais e reprodutibilidade.
- [`core/skills/technical-writing.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/skills/technical-writing.md): Habilidade dedicada à redação técnica em LaTeX, integração de citações verificadas e validação de compilação.
- [`.agents/skills/research/SKILL.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/.agents/skills/research/SKILL.md): Ponto de descoberta nativa da *skill* `research` pelo harness inteligente.

#### 4.2. Fluxos Operacionais de Pesquisa (`core/flows/research/`)
- [`core/flows/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/flows/CONTEXT.md) & [`core/flows/research/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/flows/research/CONTEXT.md): Roteamento dos fluxos de pesquisa.
- [`core/flows/research/literature.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/flows/research/literature.md): Fluxo passo a passo de busca acadêmica, download de PDF, OCR zero-token e catalogação em `refs/*.yaml`.
- [`core/flows/research/methodology.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/flows/research/methodology.md): Fluxo de desenho metodológico e alinhamento entre `code/` e `article/sections/03_metodologia.tex`.
- [`core/flows/research/draft.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/flows/research/draft.md): Fluxo de redação técnica incremental, compilação via `compile_paper.py` e sincronização com Overleaf.
- [`core/flows/research/review.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/flows/research/review.md): Fluxo de auditoria cega (consistência de citações, dados e compilação sem *warnings*).

#### 4.3. Agentes Especialistas de Pesquisa (`core/agents/`)
- [`core/agents/CONTEXT.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/agents/CONTEXT.md): Mapa de agentes especialistas.
- [`core/agents/researcher.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/agents/researcher.md): Agente pesquisador (busca bibliográfica, OCR zero-token e curadoria de `refs/`).
- [`core/agents/writer.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/agents/writer.md): Agente redator científico (escrita LaTeX modular e compilação local).
- [`core/agents/reviewer.md`](https://github.com/albericolx/Topicos_Avancados_IA/blob/main/core/agents/reviewer.md): Agente revisor metodológico e bibliográfico.

### Diagrama da Arquitetura Integrada (`[4] artefato · latex project`)

```mermaid
flowchart TD
    Root["AGENTS.md (Raiz do Workspace)"]
    Root --> Core["core/ (Automação & Pesquisa)"]
    Root --> Article["article/ (Projeto LaTeX Local)"]
    Root --> Papers["papers/artigo-final/ (Espelho Git Overleaf)"]
    Root --> Refs["refs/ (Pipeline de Referências)"]

    Core --> Tools["core/tools/\n• compile_paper.py\n• overleaf_sync.py\n• academic_search.py\n• pdf_ocr_parser.py"]
    Core --> Skills["core/skills/\n• research.md\n• literature-review.md\n• methodology-formulation.md\n• technical-writing.md"]
    Core --> Flows["core/flows/research/\n• literature.md\n• methodology.md\n• draft.md\n• review.md"]
    Core --> Agents["core/agents/\n• researcher.md\n• writer.md\n• reviewer.md"]

    Tools -->|Compila .tex -> .pdf| ArticlePDF["article/main.pdf (3 págs)"]
    Tools <-->|Git Pull / Push| Overleaf["Overleaf Remote\ngit.overleaf.com/6a92242dbaaa2c6b6833bab0"]
    Tools -->|Download PDF + OCR Zero-Token + YAML| Refs
    Refs --> RefsSub["• REFS.md (Tier-1)\n• *.yaml (Tier-2)\n• pdfs/*.pdf & ocr/*.txt (Tier-3)"]
```
