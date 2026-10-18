# Fluxo: Auditoria e Revisão por Pares (`review.md`)
> Artefato produzido: relatório de verificação de citações, consistência metodológica e prontidão para submissão.

## Etapas de Execução
1. **Auditoria de Citações**:
   Conferir se toda chave `\cite{...}` em `article/sections/*.tex` existe em `article/references.bib` e possui ficha `refs/<key>.yaml` com link/DOI válido.
2. **Auditoria de Coerência**:
   Verificar se a lacuna apresentada em `01_introducao.tex` é respondida em `03_metodologia.tex` e concluída em `05_conclusao.tex`.
3. **Validação de Compilação**:
   Executar `py core/tools/compile_paper.py` e confirmar a geração limpa de `article/main.pdf`.
