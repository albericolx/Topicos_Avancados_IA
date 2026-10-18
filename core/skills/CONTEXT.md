# Habilidades do Agente (`core/skills/`)
> Workflows e habilidades agnósticas de provedor (*skills*) para apoio à leitura/revisão bibliográfica, formulação metodológica e redação técnica científica.

As skills em `core/skills/` são a fonte canônica de capacidades operacionais do workspace e são espelhadas em [`.agents/skills/`](../../.agents/skills/CONTEXT.md) para descoberta nativa pelo harness (Antigravity, Claude Code, Copilot, OpenCode).

<!-- routing:start -->
## Roteamento de Habilidades

| Arquivo | Habilidade / Comando | Descrição |
|---|---|---|
| [`SPECS.md`](SPECS.md) | Contrato de Skills | Normas de autoria, frontmatter YAML e integração com os fluxos em `core/flows/research/` |
| [`research.md`](research.md) | `/research <fluxo>` | Dispatcher central da árvore de pesquisa (`literature`, `methodology`, `draft`, `review`, `audit`) |
| [`literature-review.md`](literature-review.md) | Revisão Bibliográfica | Busca sistemática, triagem por tiers (`[A]`, `[B]`, `[P]`), extração zero-token OCR e catalogação em `refs/*.yaml` |
| [`methodology-formulation.md`](methodology-formulation.md) | Formulação Metodológica | Desenho de arquitetura, formalização matemática, definição de baselines e protocolo de ablação |
| [`technical-writing.md`](technical-writing.md) | Redação Técnica LaTeX | Escrita científica enxuta no padrão Springer LNCS, compressão semântica e simulação de revisão por pares |
<!-- routing:end -->
