# Seções do Relatório Técnico LaTeX (`code/mlp/report/sections/`)
> Capítulos modulares do relatório técnico da Rede Neural Multicamadas (MLP).

## Seções
* [`01_introducao.tex`](01_introducao.tex): Fundamentação teórica, domínio clínico (*Heart Disease*) e objetivos.
* [`02_arquitetura_e_metodo.tex`](02_arquitetura_e_metodo.tex): Desenho detalhado da arquitetura em grafo direcionado (`nx.DiGraph`), equações de *Forward Pass* e *Backpropagation*, correções matemáticas e particionamento 80/20 sem vazamento.
* [`03_otimizacao_e_resultados.tex`](03_otimizacao_e_resultados.tex): Estudo de ablação (`C0` a `C7`), justificativa dos hiperparâmetros modificados para otimização da acurácia e redução da perda, e inspeção visual/numérica dos pesos sinápticos.
