# Regras do Workspace (AGENTS.md)
> Ponto de entrada canônico para qualquer agente de IA (Harness Principal ou de Backup). Leia antes de qualquer tarefa.

<!-- norms:start -->
- **SISTEMA DE ARQUIVOS É A FONTE DA VERDADE**: Nenhuma informação relevante deve existir apenas no histórico do chat ou memória volátil da IA. Se é real, vira arquivo versionado no repositório.
- **ARMAZENAMENTO AGNOSTIC DE PROVEDOR (MULTI-HARNESS)**: O workspace pertence ao aluno e aos arquivos locais, nunca a um provedor específico de IA. Se a IA atual (Antigravity, Claude, Copilot, Cursor, etc.) atingir limite de cota, a próxima IA deve poder assumir a tarefa lendo este arquivo e os arquivos `CONTEXT.md`.
- **SEGREDOS FORA DO GIT**: Senhas, tokens de API ou chaves pessoais devem ficar em arquivos `.env` ignorados no `.gitignore`.
- **PESQUISA E RIGOR ACADÊMICO**:
  - Proibido inventar/alucinar citações, autores ou métricas. Toda citação deve existir em `papers/artigo-final/references.bib` ou ser validada via `core/tools/academic_search.py`.
  - Terminologia técnica e acadêmica consistente em todas as seções do artigo de Tópicos Avançados de IA.
- **DISCIPLINA DE GITFLOW**:
  - Nunca comitar diretamente na branch `main`.
  - Desenvolvimento de novos modelos de IA, módulos de código ou seções do artigo deve ocorrer em branches `feature/<nome-da-tarefa>`.
  - A branch `develop` integra as funcionalidades prontas. A branch `main` reflete versões finais/entregas da disciplina.
- **AUTONOMIA E EXECUÇÃO DIRETA**: O agente deve agir com autonomia e proatividade. Tome decisões técnicas e de design razoáveis por padrão, execute as tarefas de ponta a ponta e entregue o resultado pronto, sem interromper o aluno com questionários ou pedidos desnecessários de aprovação. Pergunte apenas se for estritamente impossível prosseguir.
- **ATUALIZE O CONTEXTO**: Ao criar uma nova pasta ou projeto significativo, adicione ou atualize o `CONTEXT.md` correspondente.
- **TRABALHO CONCLUÍDO É REGISTRADO**: Atualize o `ROADMAP.md` e `ISSUES.md` ao finalizar entregas.
<!-- norms:end -->

## Navegação Rápida (Roteamento do Projeto)

| Pasta | Descrição |
|---|---|
| [`code/`](code/CONTEXT.md) | Modelos neurais, grafos computacionais, experimentos práticos e scripts de IA |
| [`papers/`](papers/CONTEXT.md) | Artigo científico em LaTeX (Springer LNCS) com sincronização Overleaf |
| [`core/`](core/CONTEXT.md) | Utilitários, scripts de pesquisa acadêmica, compilação de LaTeX e sincronização |

---

## Como Operar em Caso de Limite de Cota (Troca de Harness)
1. Antes de encerrar a sessão, certifique-se de salvar os arquivos editados e registrar qualquer pendência em [`ISSUES.md`](ISSUES.md).
2. Ao abrir o harness de backup (ex: VS Code com Copilot ou Claude Code), a IA deve iniciar lendo [`AGENTS.md`](AGENTS.md) e [`ISSUES.md`](ISSUES.md).
