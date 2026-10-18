# Fluxo: Redação Técnica e Compilação LaTeX (`draft.md`)
> Artefato produzido: seções `.tex` atualizadas em `article/sections/`, PDF compilado em `article/main.pdf` e sincronização com Overleaf.

## Etapas de Execução
1. **Leitura de Contexto e Fichas YAML**:
   Ler `article/SPECS.md` e as fichas em `refs/*.yaml` correspondentes às chaves citadas.
2. **Escrita Modular**:
   Editar a seção alvo em `article/sections/` obedecendo ao padrão Springer LNCS e à compressão semântica.
3. **Compilação Local via Harness**:
   Executar `py core/tools/compile_paper.py` para gerar `article/main.pdf` e validar a ausência de erros de LaTeX/BibTeX.
4. **Sincronização Overleaf**:
   Replicar as alterações para `papers/artigo-final/` e sincronizar com o repositório remoto do Overleaf.
