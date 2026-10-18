# Fluxos de Pesquisa Científica (`core/flows/research/`)
> Protocolos operacionais invocados pela skill [`core/skills/research.md`](../../skills/research.md).

<!-- routing:start -->
## Roteamento dos Protocolos de Pesquisa

| Arquivo | Comando | Finalidade |
|---|---|---|
| [`literature.md`](literature.md) | `research literature` | Busca acadêmica automatizada, download de PDF, OCR zero-token e geração de `.yaml` em `refs/` |
| [`methodology.md`](methodology.md) | `research methodology` | Estruturação matemática, especificação de algoritmos, baselines e estudo de ablação |
| [`draft.md`](draft.md) | `research draft` | Redação e atualização de seções modulares `.tex` no padrão Springer LNCS com compilação local |
| [`review.md`](review.md) | `research review` | Auditoria cega de citações, verificação de DOIs e simulação de parecer de revisão por pares |
<!-- routing:end -->
