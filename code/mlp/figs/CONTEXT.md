# Figuras e Visualizações da MLP (`code/mlp/figs/`)
> Gráficos de arquitetura, evolução topológica dos pesos sinápticos, mapas de calor e curvas de convergência gerados automaticamente pela execução da MLP.

## Catálogo de Figuras
* [`arquitetura_diagrama.png`](arquitetura_diagrama.png): Desenho esquemático da arquitetura da MLP em grafo direcionado (`nx.DiGraph`) detalhando as equações do *Forward Pass* e *Backpropagation*.
* [`grafo_antes.png`](grafo_antes.png): Grafo direcionado da MLP antes do treinamento (Época 0), com valores numéricos dos pesos iniciais e espessura proporcional nas arestas.
* [`grafo_depois.png`](grafo_depois.png): Grafo direcionado da MLP após o treinamento, evidenciando a atualização numérica e visual (espessura e cor) dos pesos sinápticos.
* [`heatmap_pesos.png`](heatmap_pesos.png): Mapa de calor com anotação numérica das matrizes de pesos sinápticos $W^{(l)}$ por camada.
* [`heatmap_delta_pesos.png`](heatmap_delta_pesos.png): Mapa de calor com anotação numérica das atualizações sinápticas $\Delta W^{(l)}$.
* [`curvas_convergencia.png`](curvas_convergencia.png): Curvas de redução da perda (BCE Loss) e evolução da acurácia ao longo das épocas.
* [`comparativo_configuracoes.png`](comparativo_configuracoes.png): Comparativo experimental entre as 8 configurações avaliadas (`C0` a `C7`).
