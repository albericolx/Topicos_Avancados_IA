---
name: technical-writing
description: >
  Habilidade para redação técnica científica em LaTeX (padrão Springer LNCS),
  compressão semântica, coerência argumentativa e compilação/sincronização com Overleaf.
---

# Skill: Redação Técnica Científica (`technical-writing`)

## Objetivo
Garantir que o manuscrito em [`article/`](../../article/CONTEXT.md) e [`papers/artigo-final/`](../../papers/CONTEXT.md) atenda aos critérios internacionais de publicação no padrão **Springer LNCS** (`llncs.cls`, `splncs04.bst`).

## Cinco Pilares de Qualidade Textual
1. **Nuance Argumentativa**: Substitua adjetivos vagos ("muito rápido", "eficiente") por métricas verificáveis ("latência média de 42 ms", "92,80% de acurácia").
2. **Coerência de Longo Alcance**: A lacuna aberta na Introdução (`01_introducao.tex`) deve ser exatamente a lacuna respondida na Metodologia (`03_metodologia.tex`) e fechada na Conclusão (`05_conclusao.tex`).
3. **Compressão Semântica**: Cada frase deve carregar uma única unidade nova de informação.
4. **Rigor de Citação**: Toda afirmação factual ou comparativa deve vir acompanhada de `\cite{chave}` respaldada por ficha em [`refs/`](../../refs/CONTEXT.md).
5. **Simulação de Revisor Cético**: Antecipe limitações e *trade-offs* técnicos (ex.: custo energético e latência de SLMs *on-device*) no próprio texto antes do avaliador.

## Ciclo de Validação e Entrega
```bash
# 1. Compilar localmente via harness e verificar ausência de erros
py core/tools/compile_paper.py

# 2. Sincronizar alterações com o repositório remoto do Overleaf
py core/tools/overleaf_sync.py --status
```
