# Protocolos de Fluxo (`core/flows/`)
> Fluxos de trabalho estruturados em etapas determinísticas para execução por agentes inteligentes.

## Princípios Inegociáveis
- **O artefato em disco é a memória**: Nenhuma etapa termina apenas no chat; todo fluxo grava seu resultado em arquivos versionados (`refs/*.yaml`, `article/sections/*.tex`).
- **Delegar coleta, centralizar síntese**: Agentes coletores buscam dados e extraem texto via OCR zero-token; o agente escritor consolida a prosa final.

<!-- routing:start -->
## Roteamento de Fluxos

| Subpasta | Descrição |
|---|---|
| [`research/`](research/CONTEXT.md) | Fluxos do módulo de pesquisa científica (`literature`, `methodology`, `draft`, `review`) |
<!-- routing:end -->
