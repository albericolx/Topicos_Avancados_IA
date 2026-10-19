# Regras do Workspace (AGENTS.md)
> Ponto de entrada canônico para qualquer agente de IA (Harness Principal ou de Backup). Leia antes de qualquer tarefa.

<!-- norms:start -->
- **SISTEMA DE ARQUIVOS É A FONTE DA VERDADE**: Nenhuma informação relevante deve existir apenas no histórico do chat ou memória volátil da IA. Se é real, vira arquivo versionado no repositório.
- **ARMAZENAMENTO AGNOSTIC DE PROVEDOR (MULTI-HARNESS)**: O workspace pertence ao aluno e aos arquivos locais, nunca a um provedor específico de IA. Se a IA atual (Antigravity, Claude, Copilot, Cursor, etc.) atingir limite de cota, a próxima IA deve poder assumir a tarefa lendo este arquivo e os arquivos `CONTEXT.md`.
- **SEGREDOS FORA DO GIT**: Senhas, tokens de API ou chaves pessoais devem ficar em arquivos `.env` ignorados no `.gitignore`.
- **PESQUISA E RIGOR ACADÊMICO**:
  - Proibido inventar/alucinar citações, autores ou métricas. Toda citação deve existir em `article/references.bib`, estar catalogada em `refs/REFS.md` + `refs/<key>.yaml` e ser validada via `core/tools/academic_search.py`.
  - Terminologia técnica e acadêmica consistente em todas as seções do artigo de Tópicos Avançados de IA.
- **DISCIPLINA DE GITFLOW**:
  - Nunca comitar diretamente na branch `main`.
  - Desenvolvimento de novos modelos de IA, módulos de código ou seções do artigo deve ocorrer em branches `feature/<nome-da-tarefa>`.
  - A branch `develop` integra as funcionalidades prontas. A branch `main` reflete versões finais/entregas da disciplina.
- **AUTONOMIA E ALINHAMENTO COM O USUÁRIO**: Sempre consulte o aluno quanto às opções arquiteturais e de design relevantes ao longo das implementações, mantendo transparência e rigor técnico.
- **ATUALIZE O CONTEXTO**: Ao criar uma nova pasta ou projeto significativo, adicione ou atualize o `CONTEXT.md` correspondente.
- **TRABALHO CONCLUÍDO É REGISTRADO**: Atualize o `ROADMAP.md` e `ISSUES.md` ao finalizar entregas.
<!-- norms:end -->

## Navegação Rápida (Roteamento Modular do Workspace)

| Pasta | Arquivo Contextual | Descrição |
|---|---|---|
| [`code/`](code/CONTEXT.md) | [`code/CONTEXT.md`](code/CONTEXT.md) · [`code/mlp/CONTEXT.md`](code/mlp/CONTEXT.md) · [`code/src/CONTEXT.md`](code/src/CONTEXT.md) | Modelos neurais, subrepositório da MLP (`code/mlp/` — `mlp·c`), grafos computacionais e experimentos |
| [`article/`](article/CONTEXT.md) | [`article/CONTEXT.md`](article/CONTEXT.md) · [`article/sections/CONTEXT.md`](article/sections/CONTEXT.md) · [`article/figures/CONTEXT.md`](article/figures/CONTEXT.md) · [`article/refs/CONTEXT.md`](article/refs/CONTEXT.md) | Projeto LaTeX unificado no repositório com PDF compilado (`article/main.pdf`) |
| [`refs/`](refs/CONTEXT.md) | [`refs/CONTEXT.md`](refs/CONTEXT.md) · [`refs/REFS.md`](refs/REFS.md) · [`refs/pdfs/CONTEXT.md`](refs/pdfs/CONTEXT.md) · [`refs/ocr/CONTEXT.md`](refs/ocr/CONTEXT.md) | Pipeline de referências acadêmicas, fichas `.yaml`, PDFs e OCR zero-token |
| [`papers/`](papers/CONTEXT.md) | [`papers/CONTEXT.md`](papers/CONTEXT.md) | Espelho de sincronização bidirecional com o projeto Overleaf |
| [`core/`](core/CONTEXT.md) | [`core/CONTEXT.md`](core/CONTEXT.md) · [`core/tools/CONTEXT.md`](core/tools/CONTEXT.md) · [`core/skills/CONTEXT.md`](core/skills/CONTEXT.md) · [`core/flows/CONTEXT.md`](core/flows/CONTEXT.md) · [`core/agents/CONTEXT.md`](core/agents/CONTEXT.md) | Ferramentas CLI, *skills* de pesquisa, fluxos operacionais e agentes especialistas |
| [`.agents/`](.agents/CONTEXT.md) | [`.agents/CONTEXT.md`](.agents/CONTEXT.md) · [`.agents/skills/CONTEXT.md`](.agents/skills/CONTEXT.md) · [`.agents/skills/research/SKILL.md`](.agents/skills/research/SKILL.md) | Habilidades nativas descobertas automaticamente pelo harness |
| [`artefatos/`](artefatos/CONTEXT.md) | [`artefatos/CONTEXT.md`](artefatos/CONTEXT.md) | Documentação de evidências da disciplina ([`3-base-git-repo.md`](artefatos/3-base-git-repo.md), [`4-latex-project.md`](artefatos/4-latex-project.md), [`5-mlp-git-repo.md`](artefatos/5-mlp-git-repo.md)) |
| [`va2/`](va2/CONTEXT.md) | [`va2/CONTEXT.md`](va2/CONTEXT.md) | Artefatos da 2ª Verificação de Aprendizagem (`brw.md`, `cmp.md`) |

---

## Como Operar em Caso de Limite de Cota (Troca de Harness)
1. Antes de encerrar a sessão, certifique-se de salvar os arquivos editados e registrar qualquer pendência em [`ISSUES.md`](ISSUES.md).
2. Ao abrir o harness de backup (ex: VS Code com Copilot ou Claude Code), a IA deve iniciar lendo [`AGENTS.md`](AGENTS.md) e [`ISSUES.md`](ISSUES.md).
