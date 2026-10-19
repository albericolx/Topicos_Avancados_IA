"""
core_mlp/visualize.py
=====================
Visualização da Rede Neural Multicamadas (MLPGraph):
1. Grafo direcionado (NetworkX + Matplotlib) com espessura e cor das conexões proporcionais
   à magnitude/sinal dos pesos sinápticos e exibição numérica dos valores de peso nas arestas.
2. Mapa de calor (Heatmap) com os valores numéricos de peso W^{(l)} e variação ΔW^{(l)} por camada.
3. Tabela estruturada (DataFrame) de pesos sinápticos, variações por época (Δw) e gradientes (∂L/∂w).
4. Curvas de perda (Loss) e acurácia (Treino vs. Teste).
"""
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _positions(mlp):
    """Calcula coordenadas (x, y) organizadas em colunas por camada para o grafo direcionado."""
    pos = {}
    xsp = 4.2
    for li in range(mlp.num_layers):
        n = mlp.layer_sizes[li]
        for i in range(n):
            pos[f"L{li}_N{i}"] = (li * xsp, ((n - 1) / 2.0 - i) * 1.4)
        if li < mlp.num_layers - 1:
            pos[f"L{li}_bias"] = (li * xsp, -((n - 1) / 2.0 + 1.35) * 1.4)
    return pos


def draw_network(
    mlp,
    fwd_edges=None,
    bwd_edges=None,
    node_hl=None,
    epoch=None,
    loss_val=None,
    acc_val=None,
    show_edge_weights=True,
    top_k_labels_per_layer=8,
):
    """
    Desenha a MLP como grafo direcionado exibindo:
    - Espessura e cor das conexões proporcionais aos pesos sinápticos w_ij
    - Valores numéricos dos pesos sinápticos diretamente sobre as conexões (show_edge_weights=True)
    - Valores numéricos de ativação dentro de cada neurônio
    """
    fig, ax = plt.subplots(figsize=(16, 10))
    G = mlp.graph
    pos = _positions(mlp)

    # 1. Cores e tamanhos dos nós
    ncolors, nsizes = [], []
    for nd in G.nodes():
        if node_hl and nd in node_hl:
            ncolors.append(node_hl[nd])
            nsizes.append(920)
        elif G.nodes[nd]["is_bias"]:
            ncolors.append("#FFD54F")  # Dourado: nó de bias (b = +1)
            nsizes.append(520)
        else:
            layer = G.nodes[nd]["layer"]
            if layer == 0:
                ncolors.append("#66BB6A")  # Verde: camada de entrada
            elif layer == mlp.num_layers - 1:
                ncolors.append("#EF5350")  # Vermelho: camada de saída
            else:
                ncolors.append("#42A5F5")  # Azul: camadas ocultas
            nsizes.append(700)

    # 2. Arestas com espessura e cor proporcionais a |w_ij|
    wmax = max((abs(G[u][v]["weight"]) for u, v in G.edges()), default=1.0)
    wmax = max(wmax, 1e-6)

    for u, v in G.edges():
        w = G[u][v]["weight"]
        nw = min(abs(w) / wmax, 1.0)
        c = plt.cm.Blues(0.30 + 0.65 * nw) if w >= 0 else plt.cm.Reds(0.30 + 0.65 * nw)
        lw = 0.45 + 3.2 * nw
        alpha = 0.35 + 0.55 * nw
        ax.annotate(
            "",
            xy=pos[v],
            xytext=pos[u],
            arrowprops=dict(
                arrowstyle="-|>",
                color=c,
                lw=lw,
                alpha=alpha,
                connectionstyle="arc3,rad=0.03",
            ),
        )

    # 3. Destaque de Forward Pass animado (verde neon)
    if fwd_edges:
        for u, v in fwd_edges:
            if G.has_edge(u, v):
                ax.annotate(
                    "",
                    xy=pos[v],
                    xytext=pos[u],
                    arrowprops=dict(
                        arrowstyle="-|>",
                        color="#00E676",
                        lw=3.0,
                        alpha=0.92,
                        connectionstyle="arc3,rad=0.03",
                    ),
                )

    # 4. Destaque de Backward Pass animado (laranja)
    if bwd_edges:
        for u, v in bwd_edges:
            if G.has_edge(u, v):
                ax.annotate(
                    "",
                    xy=pos[v],
                    xytext=pos[u],
                    arrowprops=dict(
                        arrowstyle="-|>",
                        color="#FF9100",
                        lw=3.0,
                        alpha=0.92,
                        connectionstyle="arc3,rad=0.03",
                    ),
                )

    # 5. Exibição numérica dos pesos sinápticos (w_ij) nas conexões
    if show_edge_weights:
        for li in range(mlp.num_layers - 1):
            layer_e = [
                (u, v, G[u][v]["weight"])
                for u, v in G.edges()
                if G[u][v].get("layer", -1) == li
            ]
            layer_e.sort(key=lambda item: abs(item[2]), reverse=True)
            selected = layer_e if top_k_labels_per_layer <= 0 else layer_e[:top_k_labels_per_layer]

            for idx_e, (u, v, w) in enumerate(selected):
                x1, y1 = pos[u]
                x2, y2 = pos[v]
                frac = 0.36 + 0.28 * ((idx_e % 3) / 2.0)
                xm = x1 + frac * (x2 - x1)
                ym = y1 + frac * (y2 - y1)
                txt_color = "#0D47A1" if w >= 0 else "#B71C1C"
                ax.text(
                    xm,
                    ym,
                    f"{w:+.2f}",
                    fontsize=6.5,
                    fontweight="bold",
                    color=txt_color,
                    ha="center",
                    va="center",
                    bbox=dict(
                        boxstyle="round,pad=0.14",
                        fc="white",
                        ec=txt_color,
                        lw=0.5,
                        alpha=0.82,
                    ),
                )

    # 6. Desenho dos nós e ativações numéricas
    nx.draw_networkx_nodes(
        G,
        pos,
        ax=ax,
        node_color=ncolors,
        node_size=nsizes,
        edgecolors="#263238",
        linewidths=0.9,
    )

    labels = {}
    for nd in G.nodes():
        if G.nodes[nd]["is_bias"]:
            labels[nd] = "b=+1"
        else:
            labels[nd] = f'{G.nodes[nd]["value"]:.2f}'
    nx.draw_networkx_labels(G, pos, labels, ax=ax, font_size=7, font_weight="bold")

    # Rótulos de cabeçalho das camadas
    for li in range(mlp.num_layers):
        n = mlp.layer_sizes[li]
        top_y = ((n - 1) / 2.0) * 1.4 + 1.15
        if li == 0:
            lname = f"Entrada (L0)\n[{n} atributos]"
        elif li == mlp.num_layers - 1:
            lname = f"Saída (L{li})\n[Sigmoide]"
        else:
            lname = f"Oculta {li} (L{li})\n[{n} neurônios · {mlp.activation}]"
        ax.text(
            li * 4.2,
            top_y,
            lname,
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="#ECEFF1", ec="#90A4AE", alpha=0.9),
        )

    title_parts = [f"Grafo Direcionado da MLP ({' → '.join(map(str, mlp.layer_sizes))})"]
    if epoch is not None:
        title_parts.append(f"Época {epoch}")
    if loss_val is not None:
        title_parts.append(f"Loss: {loss_val:.4f}")
    if acc_val is not None:
        title_parts.append(f"Acurácia Teste: {acc_val:.1%}")
    ax.set_title("  |  ".join(title_parts), fontsize=11.5, fontweight="bold", pad=28)
    ax.axis("off")
    fig.tight_layout()
    return fig


def draw_weights_heatmap(mlp, mode="weight", epoch=None):
    """
    Exibe mapas de calor (heatmaps) com anotação numérica explícita dos pesos sinápticos (w_ij)
    ou das atualizações da época (Δw_ij) para cada camada da rede.
    """
    n_conn = mlp.num_layers - 1
    fig, axes = plt.subplots(1, n_conn, figsize=(6.2 * n_conn, 5.6))
    if n_conn == 1:
        axes = [axes]

    for li in range(n_conn):
        ax = axes[li]
        G = mlp.graph
        srcs = [f"L{li}_N{i}" for i in range(mlp.layer_sizes[li])] + [f"L{li}_bias"]
        dsts = [f"L{li+1}_N{j}" for j in range(mlp.layer_sizes[li + 1])]
        mat = np.zeros((len(srcs), len(dsts)), dtype=float)
        for r, s in enumerate(srcs):
            for c, d in enumerate(dsts):
                mat[r, c] = G[s][d].get(mode, 0.0)

        vmax = max(float(np.max(np.abs(mat))), 1e-4)
        im = ax.imshow(mat, cmap="coolwarm", vmin=-vmax, vmax=vmax, aspect="auto")
        ax.set_title(
            f"Camada L{li} → L{li+1}" + (f" (Época {epoch})" if epoch is not None else ""),
            fontsize=10,
            fontweight="bold",
        )
        ax.set_xticks(range(len(dsts)))
        ax.set_xticklabels([d.replace(f"L{li+1}_", "") for d in dsts], fontsize=7.5, rotation=45)
        ax.set_yticks(range(len(srcs)))
        ax.set_yticklabels([s.replace(f"L{li}_", "") for s in srcs], fontsize=7.5)

        # Anotar valores numéricos nas células se a matriz for legível
        if len(srcs) * len(dsts) <= 260:
            for r in range(len(srcs)):
                for c in range(len(dsts)):
                    val = mat[r, c]
                    fmt = f"{val:+.2f}" if mode == "weight" else f"{val:+.3f}"
                    ax.text(
                        c,
                        r,
                        fmt,
                        ha="center",
                        va="center",
                        fontsize=6.2,
                        color="white" if abs(val) > 0.55 * vmax else "black",
                    )
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    suptitle = (
        "Inspeção Numérica dos Pesos Sinápticos (w_ij)"
        if mode == "weight"
        else "Atualização dos Pesos Sinápticos na Época (Δw_ij)"
    )
    fig.suptitle(suptitle, fontsize=12, fontweight="bold")
    fig.tight_layout()
    return fig


def get_weights_dataframe(mlp):
    """
    Retorna um DataFrame com todos os pesos sinápticos, pesos anteriores,
    atualização na época (Δw) e gradiente instantâneo (∂L/∂w).
    """
    rows = []
    G = mlp.graph
    for u, v in G.edges():
        e = G[u][v]
        rows.append(
            {
                "Camada": f"L{e.get('layer', 0)} → L{e.get('layer', 0) + 1}",
                "Origem": u,
                "Destino": v,
                "Peso Atual (w)": round(float(e["weight"]), 5),
                "Peso Anterior": round(float(e.get("prev_weight", e["weight"])), 5),
                "Atualização (Δw)": round(float(e.get("delta_weight", 0.0)), 6),
                "Gradiente (∂L/∂w)": round(float(e.get("gradient", 0.0)), 6),
                "|w|": round(abs(float(e["weight"])), 5),
            }
        )
    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values(by="|w|", ascending=False).reset_index(drop=True)
    return df


def draw_loss(train_losses, test_losses=None, epochs=None):
    """Plota a curva de perda (BCE/MSE) ao longo das épocas."""
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    if train_losses:
        xs = epochs if epochs is not None else list(range(1, len(train_losses) + 1))
        ax.plot(xs, train_losses, "b-", lw=2.0, label="Treino (80%)")
        if test_losses and len(test_losses) == len(xs):
            ax.plot(xs, test_losses, "r--", lw=1.8, label="Teste (20%)")
        ax.set_xlabel("Época")
        ax.set_ylabel("Loss (BCE)")
        ax.set_title("Evolução da Perda (Loss)", fontweight="bold")
        ax.grid(True, alpha=0.3)
        ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    return fig


def draw_accuracy(train_accs, test_accs=None, epochs=None):
    """Plota a curva de acurácia no treino e no teste."""
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    if train_accs:
        xs = epochs if epochs is not None else list(range(1, len(train_accs) + 1))
        ax.plot(xs, train_accs, "g-", lw=2.0, label="Treino (80%)")
        if test_accs and len(test_accs) == len(xs):
            ax.plot(xs, test_accs, "m--", lw=1.8, label="Teste (20%)")
        ax.set_xlabel("Época")
        ax.set_ylabel("Acurácia")
        ax.set_title("Evolução da Acurácia", fontweight="bold")
        ax.set_ylim(0.4, 1.03)
        ax.grid(True, alpha=0.3)
        ax.legend(loc="lower right", fontsize=8)
    fig.tight_layout()
    return fig


def save_graph_image(mlp, path, **kwargs):
    """Salva o grafo da rede como imagem PNG de alta resolução."""
    fig = draw_network(mlp, **kwargs)
    fig.savefig(path, dpi=160, bbox_inches="tight")
    plt.close(fig)


def layer_edges(mlp, li):
    """Retorna o conjunto de arestas conectando a camada li à camada li+1."""
    edges = set()
    srcs = [f"L{li}_N{i}" for i in range(mlp.layer_sizes[li])] + [f"L{li}_bias"]
    for s in srcs:
        for j in range(mlp.layer_sizes[li + 1]):
            edges.add((s, f"L{li+1}_N{j}"))
    return edges


def all_forward_edges(mlp):
    """Retorna todas as arestas diretas da rede."""
    edges = set()
    for li in range(mlp.num_layers - 1):
        edges |= layer_edges(mlp, li)
    return edges
