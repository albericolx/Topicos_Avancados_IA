# Cronograma e Entregas (ROADMAP.md)
> Acompanhamento das etapas da disciplina Tópicos Avançados de Inteligência Artificial (UFRPE 2026.2).

## Fases do Projeto

### Fase 1: Fundação do Workspace & Alinhamento (`[3] artefato · base git repo`)
- [x] Commit inaugural registrado e assinado pelo harness com mensagem estruturada ([`6dee07b`](https://github.com/albericolx/Topicos_Avancados_IA/commit/6dee07bedf545a4eab110995010ba7dfb1f2793d))
- [x] Árvore integrada unificando `code/`, `article/` (`papers/`), `core/` e documentações em repositório único
- [x] Especificação modular com `AGENTS.md` na raiz e `CONTEXT.md` em todas as subpastas do workspace
- [x] Evidência consolidada publicada em [`artefatos/3-base-git-repo.md`](artefatos/3-base-git-repo.md)

### Fase 2: Infraestrutura Científica & Projeto LaTeX (`[4] artefato · latex project`)
- [x] Compilação local de `.tex` para `.pdf` funcional via harness (`core/tools/compile_paper.py` $\rightarrow$ [`article/main.pdf`](article/main.pdf))
- [x] Integração bidirecional com projeto Overleaf (`papers/artigo-final` & `core/tools/overleaf_sync.py`) com contribuições enviadas pelo harness (`3dc40d5`, `77d47ac`)
- [x] Pipeline de referências com busca acadêmica, download de PDF, OCR automático zero-token (`core/tools/pdf_ocr_parser.py`) e pasta [`refs/`](refs/CONTEXT.md) estruturada com metadados `.yaml`
- [x] Árvore de pesquisa e habilidades (*skills*) adicionada ao workspace ([`core/skills/`](core/skills/CONTEXT.md), [`core/flows/research/`](core/flows/research/CONTEXT.md), [`core/agents/`](core/agents/CONTEXT.md) e [`.agents/skills/research/SKILL.md`](.agents/skills/research/SKILL.md))
- [x] Evidência consolidada publicada em [`artefatos/4-latex-project.md`](artefatos/4-latex-project.md)

### Fase 3: Implementação dos Modelos Neurais & Experimentos
- [x] Implementação de experimentos práticos (MLP, CNN e Loop de Agentes em `Atividade_03_LOOP_Agentes/`)
- [ ] Consolidação da arquitetura final em `code/src/`
- [ ] Geração das figuras definitivas para `article/figures/`

### Fase 4: Análise de Resultados e Artigo Final
- [ ] Redação final da Metodologia (`article/sections/03_metodologia.tex`) e Experimentos (`article/sections/04_experimentos.tex`)
- [ ] Conclusão e Trabalhos Futuros (`article/sections/05_conclusao.tex`)

### Avaliação VA2: Ideação e Pesquisa (IA for Good)
- [x] Estruturação e ideação completa de brainwriting ([`va2/brw.md`](va2/brw.md))
- [x] Competidores e contribuição validada por auditoria cega ([`va2/cmp.md`](va2/cmp.md))
