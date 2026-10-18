---
name: methodology-formulation
description: >
  Habilidade para formulação metodológica rigorosa: modelagem matemática,
  arquitetura de sistema, definição de baselines e protocolo de estudo de ablação.
---

# Skill: Formulação Metodológica (`methodology-formulation`)

## Objetivo
Transformar a hipótese de pesquisa e a implementação em [`code/src/`](../../code/src/CONTEXT.md) em uma seção metodológica formal, reprodutível e matematicamente precisa em [`article/sections/03_metodologia.tex`](../../article/sections/03_metodologia.tex) e [`article/sections/04_experimentos.tex`](../../article/sections/04_experimentos.tex).

## Estrutura Metodológica Obrigatória
1. **Formulação do Problema e Notação**:
   Defina formalmente o espaço de entrada $\mathcal{X}$, espaço de saída $\mathcal{Y}$, estrutura do grafo $G = (V, E)$ e função objetivo $\mathcal{L}(\theta)$.
2. **Arquitetura e Fluxo Algorítmico**:
   Descreva os módulos implementados (propagação direta, retropropagação explícita, inferência local com SLM e orquestração via agentes MCP).
3. **Desenho Experimental e Baselines**:
   - Fixe sementes determinísticas (`seed = 42`).
   - Estabeleça *baselines* comparáveis e métricas quantitativas (acurácia, F1-score, latência em ms, consumo de RAM/bateria).
4. **Estudo de Ablação (*Ablation Study*)**:
   Isole cada componente da arquitetura para demonstrar empiricamente sua contribuição marginal.
