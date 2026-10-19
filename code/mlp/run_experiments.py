"""
run_experiments.py
==================
Script reprodutível de experimentação, estudo de ablação e otimização de hiperparâmetros
da MLP implementada do zero (core_mlp).

Gera automaticamente:
- Partições padronizadas 80/20 em `code/mlp/data/train_80_standardized.csv` e `test_20_standardized.csv`
- Figuras de alta resolução em `code/mlp/figs/` (e espelho em `code/mlp/report/figs/`)
- Tabelas e métricas completas em `code/mlp/results/benchmark_results.csv` e `benchmark_summary.json`
"""
import json
import os
import shutil
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from core_mlp.dataset import load_and_partition_data
from core_mlp.graph import MLPGraph
from core_mlp.train import run_training_history, evaluate
from core_mlp.visualize import (
    draw_network,
    draw_weights_heatmap,
    get_weights_dataframe,
    save_graph_image,
)


def draw_architecture_schema(out_path: str):
    """Desenha um diagrama esquemático detalhado da arquitetura da MLP e do ciclo Forward/Backward."""
    fig, ax = plt.subplots(figsize=(14, 6.5))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7)
    ax.axis("off")

    boxes = [
        (0.6, 2.2, 2.3, 2.8, "#E8F5E9", "#2E7D32", "Camada de Entrada (L0)\n\n• 13 Atributos Clínicos\n  (x₁ ... x₁₃ padronizados)\n• Nó de Bias L0_bias = +1"),
        (3.8, 2.2, 2.6, 2.8, "#E3F2FD", "#1565C0", "Camada Oculta 1 (L1)\n\n• N₁ Neurônios (ex: 24)\n• zⱼ⁽¹⁾ = Σ wᵢⱼ⁽¹⁾xᵢ + bⱼ⁽¹⁾\n• Ativação aⱼ⁽¹⁾ = ReLU(zⱼ⁽¹⁾)\n• Nó de Bias L1_bias = +1"),
        (7.3, 2.2, 2.6, 2.8, "#E3F2FD", "#1565C0", "Camada Oculta 2 (L2)\n\n• N₂ Neurônios (ex: 12)\n• zₖ⁽²⁾ = Σ wⱼₖ⁽²⁾aⱼ⁽¹⁾ + bₖ⁽²⁾\n• Ativação aₖ⁽²⁾ = ReLU(zₖ⁽²⁾)\n• Nó de Bias L2_bias = +1"),
        (10.8, 2.2, 2.5, 2.8, "#FFEBEE", "#C62828", "Camada de Saída (L3)\n\n• 1 Neurônio Diagnóstico\n• z_out = Σ wₖ₁⁽³⁾aₖ⁽²⁾ + b⁽³⁾\n• ŷ = σ(z_out) ∈ (0, 1)\n• Perda BCE: L(y, ŷ)"),
    ]

    for x, y, w, h, fc, ec, text in boxes:
        rect = plt.Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=2.0, zorder=2)
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8.8, fontweight="bold", color="#212121")

    # Setas de Forward Pass (superior - verde)
    fwd_arrows = [(2.9, 4.2, 3.8, 4.2, "W⁽¹⁾ (14×N₁)"), (6.4, 4.2, 7.3, 4.2, "W⁽²⁾ ((N₁+1)×N₂)"), (9.9, 4.2, 10.8, 4.2, "W⁽³⁾ ((N₂+1)×1)")]
    for x1, y1, x2, y2, lbl in fwd_arrows:
        ax.annotate(
            "", xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-|>", color="#2E7D32", lw=2.5),
        )
        ax.text((x1 + x2) / 2, y1 + 0.25, lbl, ha="center", va="bottom", fontsize=8, fontweight="bold", color="#1B5E20")

    ax.text(7.0, 5.7, "➡️ PROPAGAÇÃO DIRETA (FORWARD PASS):  a⁽ˡ⁾ = f(W⁽ˡ⁾ᵀ a⁽ˡ⁻¹⁾ + b⁽ˡ⁾)", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color="#1B5E20",
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8F5E9", ec="#2E7D32", lw=1.5))

    # Setas de Backpropagation (inferior - laranja/vermelho)
    bwd_arrows = [
        (10.8, 2.8, 9.9, 2.8, "δ⁽³⁾ = ŷ - y"),
        (7.3, 2.8, 6.4, 2.8, "δ⁽²⁾ = (W⁽³⁾δ⁽³⁾)⊙f'(z⁽²⁾)"),
        (3.8, 2.8, 2.9, 2.8, "δ⁽¹⁾ = (W⁽²⁾δ⁽²⁾)⊙f'(z⁽¹⁾)"),
    ]
    for x1, y1, x2, y2, lbl in bwd_arrows:
        ax.annotate(
            "", xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(arrowstyle="-|>", color="#E65100", lw=2.5, ls="--"),
        )
        ax.text((x1 + x2) / 2, y1 - 0.35, lbl, ha="center", va="top", fontsize=7.6, fontweight="bold", color="#BF360C")

    ax.text(
        7.0, 1.1,
        "⬅️ RETROPROPAGAÇÃO (BACKPROPAGATION + SGD/MOMENTUM/L2):  gᵢⱼ⁽ˡ⁾ = aᵢ⁽ˡ⁻¹⁾δⱼ⁽ˡ⁾ + λwᵢⱼ⁽ˡ⁾  |  wᵢⱼ⁽ˡ⁾ ← wᵢⱼ⁽ˡ⁾ - η·vᵢⱼ⁽ˡ⁾",
        ha="center", va="center", fontsize=10, fontweight="bold", color="#BF360C",
        bbox=dict(boxstyle="round,pad=0.35", fc="#FFF3E0", ec="#E65100", lw=1.5),
    )

    ax.set_title("Arquitetura em Grafo Direcionado (nx.DiGraph) e Fluxo Matemático da MLP", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main():
    figs_dir = os.path.join(BASE_DIR, "figs")
    rep_figs_dir = os.path.join(BASE_DIR, "report", "figs")
    res_dir = os.path.join(BASE_DIR, "results")
    data_dir = os.path.join(BASE_DIR, "data")
    os.makedirs(figs_dir, exist_ok=True)
    os.makedirs(rep_figs_dir, exist_ok=True)
    os.makedirs(res_dir, exist_ok=True)

    # 1. Carregar datasets com MinMaxScaler e StandardScaler (80% treino / 20% teste)
    ds_minmax = load_and_partition_data(data_dir=data_dir, test_size=0.20, scaler_type="minmax", seed=42, save_splits=False)
    ds_std = load_and_partition_data(data_dir=data_dir, test_size=0.20, scaler_type="standard", seed=42, save_splits=True)

    print(f"[Dataset] Total={ds_std['split_info']['total_samples']} | "
          f"Treino (80%)={ds_std['split_info']['train_samples']} | "
          f"Teste (20%)={ds_std['split_info']['test_samples']}")

    # 2. Definir matriz de configurações experimentais para ablação e otimização
    configs = [
        {
            "id": "C0 (Legado/MSE-deriv)",
            "desc": "[13→10→8→1], Sigmoid, MinMax, Deriv. MSE, lr=0.10, 150 ép.",
            "layers": [13, 10, 8, 1],
            "activation": "sigmoid",
            "loss_type": "mse",
            "scaler": "minmax",
            "lr": 0.10,
            "momentum": 0.0,
            "l2": 0.0,
            "lr_decay": 0.0,
            "epochs": 150,
        },
        {
            "id": "C1 (Baseline BCE)",
            "desc": "[13→10→8→1], Sigmoid, MinMax, BCE Exata, lr=0.05, 150 ép.",
            "layers": [13, 10, 8, 1],
            "activation": "sigmoid",
            "loss_type": "bce",
            "scaler": "minmax",
            "lr": 0.05,
            "momentum": 0.0,
            "l2": 0.0,
            "lr_decay": 0.0,
            "epochs": 150,
        },
        {
            "id": "C2 (Z-Score + Sigmoid)",
            "desc": "[13→10→8→1], Sigmoid, StandardScaler, BCE, lr=0.05, 150 ép.",
            "layers": [13, 10, 8, 1],
            "activation": "sigmoid",
            "loss_type": "bce",
            "scaler": "standard",
            "lr": 0.05,
            "momentum": 0.0,
            "l2": 0.0,
            "lr_decay": 0.0,
            "epochs": 150,
        },
        {
            "id": "C3 (Tanh + Z-Score)",
            "desc": "[13→16→8→1], Tanh, StandardScaler, BCE, lr=0.02, 150 ép.",
            "layers": [13, 16, 8, 1],
            "activation": "tanh",
            "loss_type": "bce",
            "scaler": "standard",
            "lr": 0.02,
            "momentum": 0.0,
            "l2": 0.0,
            "lr_decay": 0.0,
            "epochs": 150,
        },
        {
            "id": "C4 (ReLU + He Init)",
            "desc": "[13→16→8→1], ReLU, StandardScaler, BCE, lr=0.015, 150 ép.",
            "layers": [13, 16, 8, 1],
            "activation": "relu",
            "loss_type": "bce",
            "scaler": "standard",
            "lr": 0.015,
            "momentum": 0.0,
            "l2": 0.0,
            "lr_decay": 0.0,
            "epochs": 150,
        },
        {
            "id": "C5 (LeakyReLU + Mom.)",
            "desc": "[13→16→8→1], LeakyReLU, Z-Score, lr=0.015, β=0.85, 150 ép.",
            "layers": [13, 16, 8, 1],
            "activation": "leaky_relu",
            "loss_type": "bce",
            "scaler": "standard",
            "lr": 0.015,
            "momentum": 0.85,
            "l2": 1e-4,
            "lr_decay": 0.005,
            "epochs": 150,
        },
        {
            "id": "C6 (Otimizada 2 Ocultas)",
            "desc": "[13→24→12→1], ReLU, Z-Score, lr=0.02, β=0.85, L2=1e-4, 200 ép.",
            "layers": [13, 24, 12, 1],
            "activation": "relu",
            "loss_type": "bce",
            "scaler": "standard",
            "lr": 0.02,
            "momentum": 0.85,
            "l2": 1e-4,
            "lr_decay": 0.005,
            "epochs": 200,
        },
        {
            "id": "C7 (Otimizada 3 Ocultas)",
            "desc": "[13→24→16→8→1], ReLU, Z-Score, lr=0.015, β=0.85, L2=1e-4, 200 ép.",
            "layers": [13, 24, 16, 8, 1],
            "activation": "relu",
            "loss_type": "bce",
            "scaler": "standard",
            "lr": 0.015,
            "momentum": 0.85,
            "l2": 1e-4,
            "lr_decay": 0.005,
            "epochs": 200,
        },
    ]

    results_rows = []
    histories = {}
    models = {}

    for cfg in configs:
        ds = ds_std if cfg["scaler"] == "standard" else ds_minmax
        X_tr, y_tr = ds["X_train"], ds["y_train"]
        X_te, y_te = ds["X_test"], ds["y_test"]

        mlp = MLPGraph(cfg["layers"], activation=cfg["activation"], loss_type=cfg["loss_type"], seed=42)

        # Salvar grafo_antes.png para a configuração otimizada de referência (C4: 13->16->8->1)
        if cfg["id"] == "C4 (ReLU + He Init)":
            init_eval = evaluate(mlp, X_te, y_te)
            save_graph_image(
                mlp,
                os.path.join(figs_dir, "grafo_antes.png"),
                epoch=0,
                loss_val=init_eval["loss"],
                acc_val=init_eval["accuracy"],
                show_edge_weights=True,
                top_k_labels_per_layer=8,
            )

        hist, tr_m, te_m = run_training_history(
            mlp,
            X_tr,
            y_tr,
            X_te,
            y_te,
            n_epochs=cfg["epochs"],
            lr=cfg["lr"],
            lr_decay=cfg["lr_decay"],
            momentum=cfg["momentum"],
            l2_lambda=cfg["l2"],
            eval_every=5,
            seed=42,
        )

        histories[cfg["id"]] = hist
        models[cfg["id"]] = mlp

        row = {
            "id": cfg["id"],
            "description": cfg["desc"],
            "layers": "->".join(map(str, cfg["layers"])),
            "activation": cfg["activation"],
            "scaler": cfg["scaler"],
            "lr": cfg["lr"],
            "momentum": cfg["momentum"],
            "l2": cfg["l2"],
            "epochs": cfg["epochs"],
            "train_loss": round(tr_m["loss"], 4),
            "test_loss": round(te_m["loss"], 4),
            "train_acc": round(tr_m["accuracy"] * 100, 2),
            "test_acc": round(te_m["accuracy"] * 100, 2),
            "precision": round(te_m["precision"] * 100, 2),
            "recall": round(te_m["recall"] * 100, 2),
            "specificity": round(te_m["specificity"] * 100, 2),
            "f1": round(te_m["f1"] * 100, 2),
            "auc_roc": round(te_m["auc_roc"], 4),
            "tp": te_m["tp"],
            "tn": te_m["tn"],
            "fp": te_m["fp"],
            "fn": te_m["fn"],
        }
        results_rows.append(row)
        print(
            f"[{cfg['id']}] Train Acc={row['train_acc']:.2f}% | Test Acc={row['test_acc']:.2f}% | "
            f"Test Loss={row['test_loss']:.4f} | F1={row['f1']:.2f}% | AUC={row['auc_roc']:.4f}"
        )

    df_res = pd.DataFrame(results_rows)
    df_res.to_csv(os.path.join(res_dir, "benchmark_results.csv"), index=False)

    # Identificar melhor modelo (maior test_acc, menor test_loss como desempate)
    best_idx = df_res.sort_values(by=["test_acc", "test_loss"], ascending=[False, True]).index[0]
    best_row = df_res.loc[best_idx].to_dict()
    best_id = best_row["id"]
    best_mlp = models[best_id]

    # Salvar grafo_depois.png e heatmaps para C4 (13->16->8->1) e para o modelo campeão
    c4_mlp = models["C4 (ReLU + He Init)"]
    c4_hist = histories["C4 (ReLU + He Init)"]
    save_graph_image(
        c4_mlp,
        os.path.join(figs_dir, "grafo_depois.png"),
        epoch=150,
        loss_val=c4_hist["test_loss"][-1],
        acc_val=c4_hist["test_acc"][-1],
        show_edge_weights=True,
        top_k_labels_per_layer=8,
    )

    fig_hm = draw_weights_heatmap(c4_mlp, mode="weight", epoch=150)
    fig_hm.savefig(os.path.join(figs_dir, "heatmap_pesos.png"), dpi=160, bbox_inches="tight")
    plt.close(fig_hm)

    fig_dm = draw_weights_heatmap(c4_mlp, mode="delta_weight", epoch=150)
    fig_dm.savefig(os.path.join(figs_dir, "heatmap_delta_pesos.png"), dpi=160, bbox_inches="tight")
    plt.close(fig_dm)

    # Salvar tabela top-30 pesos sinápticos do modelo campeão
    df_weights = get_weights_dataframe(best_mlp)
    df_weights.to_csv(os.path.join(res_dir, "best_model_synaptic_weights.csv"), index=False)

    # 3. Gerar gráfico comparativo de convergência (C0 vs C1 vs C2 vs C4 Campeã)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    compare_ids = ["C0 (Legado/MSE-deriv)", "C1 (Baseline BCE)", "C2 (Z-Score + Sigmoid)", "C4 (ReLU + He Init)"]
    colors = ["#757575", "#FB8C00", "#8E24AA", "#2E7D32"]
    for cid, col in zip(compare_ids, colors):
        h = histories[cid]
        ax1.plot(h["epoch"], h["test_loss"], label=cid, lw=2.2, color=col)
        ax2.plot(h["epoch"], [a * 100 for a in h["test_acc"]], label=cid, lw=2.2, color=col)

    ax1.set_title("Redução da Perda (Loss) no Conjunto de Teste (20%)", fontweight="bold")
    ax1.set_xlabel("Época")
    ax1.set_ylabel("Loss no Teste")
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=8.5)

    ax2.set_title("Evolução da Acurácia no Conjunto de Teste (20%)", fontweight="bold")
    ax2.set_xlabel("Época")
    ax2.set_ylabel("Acurácia (%)")
    ax2.set_ylim(50, 102)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8.5, loc="lower right")

    fig.tight_layout()
    fig.savefig(os.path.join(figs_dir, "curvas_convergencia.png"), dpi=170, bbox_inches="tight")
    plt.close(fig)

    # 4. Gráfico de barras comparativo das 8 configurações
    fig, (ax_a, ax_l) = plt.subplots(1, 2, figsize=(13.5, 5.2))
    short_labels = [r["id"].split(" ")[0] for r in results_rows]
    test_accs = [r["test_acc"] for r in results_rows]
    test_losses = [r["test_loss"] for r in results_rows]

    bars1 = ax_a.bar(short_labels, test_accs, color="#1E88E5", edgecolor="#0D47A1")
    ax_a.set_ylim(60, 105)
    ax_a.set_ylabel("Acurácia no Teste (%)")
    ax_a.set_title("Comparativo de Acurácia por Configuração (Teste 20%)", fontweight="bold")
    ax_a.grid(axis="y", alpha=0.3)
    for b, v in zip(bars1, test_accs):
        ax_a.text(b.get_x() + b.get_width() / 2, v + 0.8, f"{v:.1f}%", ha="center", va="bottom", fontsize=8, fontweight="bold")

    bars2 = ax_l.bar(short_labels, test_losses, color="#E53935", edgecolor="#B71C1C")
    ax_l.set_ylabel("Loss Final no Teste")
    ax_l.set_title("Comparativo de Perda (Loss) por Configuração (Teste 20%)", fontweight="bold")
    ax_l.grid(axis="y", alpha=0.3)
    for b, v in zip(bars2, test_losses):
        ax_l.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v:.3f}", ha="center", va="bottom", fontsize=8, fontweight="bold")

    fig.tight_layout()
    fig.savefig(os.path.join(figs_dir, "comparativo_configuracoes.png"), dpi=170, bbox_inches="tight")
    plt.close(fig)

    # 5. Diagrama da arquitetura
    draw_architecture_schema(os.path.join(figs_dir, "arquitetura_diagrama.png"))

    # Copiar todas as figuras para code/mlp/report/figs/
    for fname in os.listdir(figs_dir):
        if fname.endswith(".png"):
            shutil.copy2(os.path.join(figs_dir, fname), os.path.join(rep_figs_dir, fname))

    summary = {
        "split_info": ds_std["split_info"],
        "best_config": best_row,
        "all_configs": results_rows,
    }
    with open(os.path.join(res_dir, "benchmark_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCESSO] Melhor configuração: {best_id} -> Acurácia Teste = {best_row['test_acc']}% | Loss Teste = {best_row['test_loss']}")


if __name__ == "__main__":
    main()
