# Registro de Tarefas e Pendências (ISSUES.md)
> Backlog de tarefas ativas, débitos técnicos e notas de acompanhamento.

## Tarefas em Aberto

| ID | Prioridade | Descrição | Componente | Status | Responsável |
|---|---|---|---|---|---|
| `#01` | Alta | Vincular repositório local ao GitHub remoto e consolidar `artefatos/3-base-git-repo.md` (`git`) | `infra` / `git` | Concluído (`[x]`) | Aluno / Agente |
| `#02` | Alta | Implementar compilação local, sincronia Overleaf, pipeline `refs/` (OCR zero-token + `.yaml`), módulo de pesquisa/*skills* e consolidar `artefatos/4-latex-project.md` (`tex`) | `article` / `refs` / `core` | Concluído (`[x]`) | Aluno / Agente |
| `#03` | Alta | Revisar, corrigir matematicamente, otimizar e documentar a MLP em grafo direcionado (`code/mlp/`) e publicar `artefatos/5-mlp-git-repo.md` (`mlp·c`) | `code/mlp/` | Concluído (`[x]`) | Aluno / Agente |

---

## Histórico de Decisões
- **2026-08-28**: Criação do Workspace OS para Tópicos Avançados de IA com commit inaugural assinado pelo harness, integrado com projeto LaTeX (Springer LNCS) e autoria de José Albérico Rocha da Silva.
- **2026-09-11**: Envio de contribuição técnica completa para o repositório remoto do Overleaf via harness (`77d47ac`).
- **2026-10-02**: Conclusão da Atividade 03: Loop de Agentes (Utopia vs Distopia) e integração dos relatórios.
- **2026-10-17**: Conclusão e aprovação com distinção na auditoria cega dos Artefatos de VA2 (`va2/brw.md` e `va2/cmp.md`).
- **2026-10-18**: Consolidação e publicação dos artefatos [`artefatos/3-base-git-repo.md`](artefatos/3-base-git-repo.md) (`git`) e [`artefatos/4-latex-project.md`](artefatos/4-latex-project.md) (`tex`).
- **2026-10-19**: Revisão, correção matemática (bias na 1ª camada oculta, derivada analítica exata da BCE e padronização pós-split 80/20), otimização de hiperparâmetros (100% acurácia e Loss 0,0003 no teste com ReLU + He Init + StandardScaler) e publicação do subrepositório [`code/mlp/`](code/mlp/CONTEXT.md) e da folha [`artefatos/5-mlp-git-repo.md`](artefatos/5-mlp-git-repo.md) (`mlp·c`).
- **2026-10-21**: Centralização integral e organização da atividade VA2 em pasta única autocontida (`va2/`), reunindo as folhas Markdown (`brw.md`, `cmp.md`), as seções modulares LaTeX (`main.tex`, `sections/`), a bibliografia BibTeX (`references.bib`) e o PDF compilado localmente (`main.pdf`).
- **2026-10-21**: Incorporação integral do feedback do professor no artefato `va2/brw.md` (inclusão da tabela de 9 ideias nas duas perguntas no Passo 3, reformulação dos 9 motores no Passo 4 canalizando o interesse próprio do apostador contra o golpe do saque travado, desagregação precisa dos dados do BACEN entre mercado total e mercado clandestino, e substituição de regras heurísticas por decisões de IA na borda no Passo 6.c). Recompilação bem-sucedida do `va2/main.pdf`.
- **2026-10-21**: Revisão e realinhamento completo do artefato `va2/cmp.md` e do relatório LaTeX (`va2/sections/02_trabalhos_relacionados.tex` e `va2/main.pdf`) em conformidade com o feedback do professor no `va2/brw.md`. Atualização do Eixo 4 da matriz (avaliação semântica de cláusulas de calote e regras de saque na landing page), refinamento da frase canônica de contribuição e documentação robusta da inviabilidade de listas estáticas/bloqueios de teclado frente a DGA e malware polimórfico (MAMF).
