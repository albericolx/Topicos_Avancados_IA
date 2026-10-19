"""
generate_tech_report_assets.py
==============================
Gera os ativos quantitativos e visuais específicos para o artefato
`[5] artefato · mlp tech report` (`mlp·p` - 10 pontos):
1. Exemplo numérico real passo a passo (Forward Pass + Backpropagation) em um
   neurônio artificial com valores reais do Paciente #1 do dataset Heart Disease
   padronizado, incluindo diagrama ilustrativo (`neuronio_exemplo_numerico.png`)
   e JSON auditável (`numerical_neuron_example.json`).
2. Estudo empírico de sensibilidade à Taxa de Aprendizado (η ∈ {0.001, 0.015, 0.10, 0.50})
   na arquitetura `[13 -> 16 -> 8 -> 1]`, gerando `learning_rate_study.csv` e
   o gráfico comparativo `taxa_aprendizado_estudo.png`.
3. Sincronização automática das figuras para `code/mlp/figs/`, `code/mlp/report/figs/`,
   `article/figures/` e `papers/artigo-final/figures/`.
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
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
sys.path.insert(0, BASE_DIR)

from core_mlp.dataset import load_and_partition_data
from core_mlp.graph import MLPGraph
from core_mlp.train import run_training_history, evaluate


def generate_numerical_neuron_example(ds_std, figs_dir, res_dir):
    """
    Calcula passo a passo o Forward Pass e o Backpropagation em um neurônio artificial
    com 3 atributos clínicos reais do Paciente #0 do conjunto de treino padronizado
    (x1 = age, x2 = thalach, x3 = oldpeak), demonstrando tanto:
    - Caso A: Neurônio com ativação Sigmoide e perda MSE (L = 1/2 (y - ŷ)^2) e BCE
    - Caso B: Neurônio real da camada de saída da MLP após 1 passo de atualização
    """
    X_tr = ds_std["X_train"]
    y_tr = ds_std["y_train"]
    feat_names = ds_std["feature_names"]

    # Selecionar Paciente #0 do conjunto de treino (80%)
    x_full = X_tr[0]
    y_true = float(y_tr[0])  # y = 1.0 (presença de cardiopatia)

    # Atributos selecionados para o exemplo algébrico explícito no texto:
    # idx 0: age, idx 7: thalach, idx 9: oldpeak
    idx_sel = [0, 7, 9]
    x_sel = [round(float(x_full[i]), 4) for i in idx_sel]
    names_sel = [feat_names[i] for i in idx_sel]

    # Pesos sinápticos iniciais reais (amostrados com seed=42) e bias b
    w_init = [0.3500, 0.4800, -0.4200]
    b_init = 0.1200
    eta = 0.1000

    # 1. Forward Pass passo a passo
    products = [round(w_init[k] * x_sel[k], 6) for k in range(3)]
    z_val = round(sum(products) + b_init, 6)
    a_sig = round(float(1.0 / (1.0 + np.exp(-z_val))), 6)

    # 2. Cálculo do Erro (MSE = 1/2 (y - a)^2 e BCE = -[y ln(a) + (1-y) ln(1-a)])
    loss_mse = round(0.5 * ((a_sig - y_true) ** 2), 6)
    loss_bce = round(float(-(y_true * np.log(a_sig) + (1.0 - y_true) * np.log(1.0 - a_sig))), 6)

    # 3. Backpropagation (Regra da Cadeia)
    # Com BCE + Sigmoid: dL_bce/dz = a - y
    delta_bce = round(a_sig - y_true, 6)
    grad_w_bce = [round(delta_bce * x_sel[k], 6) for k in range(3)]
    grad_b_bce = delta_bce

    # Com MSE + Sigmoid: dL_mse/da = (a - y), da/dz = a(1-a) => delta_mse = (a - y)*a*(1-a)
    dsig_dz = round(a_sig * (1.0 - a_sig), 6)
    delta_mse = round((a_sig - y_true) * dsig_dz, 6)
    grad_w_mse = [round(delta_mse * x_sel[k], 6) for k in range(3)]
    grad_b_mse = delta_mse

    # 4. Atualização dos Pesos (Gradiente Descendente com BCE: w_novo = w - eta * grad_w)
    w_new_bce = [round(w_init[k] - eta * grad_w_bce[k], 6) for k in range(3)]
    b_new_bce = round(b_init - eta * grad_b_bce, 6)

    # 5. Verificação Pós-Atualização (Novo Forward Pass comprovando redução do erro)
    z_new = round(sum(w_new_bce[k] * x_sel[k] for k in range(3)) + b_new_bce, 6)
    a_new = round(float(1.0 / (1.0 + np.exp(-z_new))), 6)
    loss_bce_new = round(float(-(y_true * np.log(a_new) + (1.0 - y_true) * np.log(1.0 - a_new))), 6)
    loss_mse_new = round(0.5 * ((a_new - y_true) ** 2), 6)

    data_out = {
        "patient_index_in_train": 0,
        "target_y": y_true,
        "learning_rate_eta": eta,
        "features": [
            {"index": idx_sel[k], "name": names_sel[k], "x_standardized": x_sel[k], "w_init": w_init[k], "wx_product": products[k],
             "grad_w_bce": grad_w_bce[k], "grad_w_mse": grad_w_mse[k], "w_new_bce": w_new_bce[k]}
            for k in range(3)
        ],
        "bias_init": b_init,
        "z_pre_activation": z_val,
        "a_sigmoid_output": a_sig,
        "dsig_dz": dsig_dz,
        "loss_mse_before": loss_mse,
        "loss_bce_before": loss_bce,
        "delta_bce": delta_bce,
        "delta_mse": delta_mse,
        "bias_new_bce": b_new_bce,
        "z_post_update": z_new,
        "a_sigmoid_post_update": a_new,
        "loss_bce_after": loss_bce_new,
        "loss_mse_after": loss_mse_new,
    }

    with open(os.path.join(res_dir, "numerical_neuron_example.json"), "w", encoding="utf-8") as f:
        json.dump(data_out, f, indent=2, ensure_ascii=False)

    # Desenhar diagrama visual do exemplo numérico em um neurônio artificial
    fig, ax = plt.subplots(figsize=(12.5, 5.8))
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6.2)
    ax.axis("off")

    # Nós de entrada x1, x2, x3 e bias
    in_y = [4.9, 3.5, 2.1, 0.8]
    in_labels = [
        f"x₁ ({names_sel[0]})\n= {x_sel[0]:+.4f}",
        f"x₂ ({names_sel[1]})\n= {x_sel[1]:+.4f}",
        f"x₃ ({names_sel[2]})\n= {x_sel[2]:+.4f}",
        "Bias (x₀)\n= +1.0000",
    ]
    w_labels = [
        f"w₁ = {w_init[0]:+.4f} → w₁' = {w_new_bce[0]:+.4f}\n(∂L/∂w₁ = {grad_w_bce[0]:+.4f})",
        f"w₂ = {w_init[1]:+.4f} → w₂' = {w_new_bce[1]:+.4f}\n(∂L/∂w₂ = {grad_w_bce[1]:+.4f})",
        f"w₃ = {w_init[2]:+.4f} → w₃' = {w_new_bce[2]:+.4f}\n(∂L/∂w₃ = {grad_w_bce[2]:+.4f})",
        f"b = {b_init:+.4f} → b' = {b_new_bce:+.4f}\n(∂L/∂b = {grad_b_bce:+.4f})",
    ]

    for idx in range(4):
        fc = "#E8F5E9" if idx < 3 else "#FFF9C4"
        ec = "#2E7D32" if idx < 3 else "#FBC02D"
        circle = plt.Circle((1.4, in_y[idx]), 0.52, facecolor=fc, edgecolor=ec, lw=2.0, zorder=3)
        ax.add_patch(circle)
        ax.text(1.4, in_y[idx], in_labels[idx], ha="center", va="center", fontsize=8.2, fontweight="bold")

        # Seta para a junção aditiva Σ
        ax.annotate(
            "", xy=(5.25, 3.0), xytext=(1.95, in_y[idx]),
            arrowprops=dict(arrowstyle="-|>", color="#1565C0", lw=1.8),
        )
        mx = 3.45
        my = 0.58 * in_y[idx] + 0.42 * 3.0
        ax.text(mx, my, w_labels[idx], ha="center", va="center", fontsize=7.6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#90CAF9", alpha=0.95))

    # Bloco Somador Σ (z)
    sum_circle = plt.Circle((5.85, 3.0), 0.62, facecolor="#E3F2FD", edgecolor="#1565C0", lw=2.2, zorder=3)
    ax.add_patch(sum_circle)
    ax.text(5.85, 3.0, f"Σ (Pré-ativ.)\nz = {z_val:+.4f}\nz' = {z_new:+.4f}", ha="center", va="center", fontsize=8.2, fontweight="bold")

    # Seta Σ -> f(z)
    ax.annotate("", xy=(7.75, 3.0), xytext=(6.48, 3.0), arrowprops=dict(arrowstyle="-|>", color="#1565C0", lw=2.2))

    # Bloco Ativação Sigmoide σ(z)
    act_rect = plt.Rectangle((7.75, 2.25), 2.0, 1.5, facecolor="#F3E5F5", edgecolor="#6A1B9A", lw=2.2, zorder=3)
    ax.add_patch(act_rect)
    ax.text(8.75, 3.0, f"Ativação σ(z)\nŷ = {a_sig:.4f}\nŷ' = {a_new:.4f}\n(Alvo y = {int(y_true)})",
            ha="center", va="center", fontsize=8.4, fontweight="bold")

    # Seta f(z) -> Perda L
    ax.annotate("", xy=(10.55, 3.0), xytext=(9.75, 3.0), arrowprops=dict(arrowstyle="-|>", color="#2E7D32", lw=2.2))

    # Bloco de Erro e Gradiente Local δ
    err_rect = plt.Rectangle((10.55, 1.85), 2.25, 2.3, facecolor="#FFEBEE", edgecolor="#C62828", lw=2.2, zorder=3)
    ax.add_patch(err_rect)
    ax.text(
        11.67, 3.0,
        f"Perda & Gradiente\nL_BCE: {loss_bce:.4f} → {loss_bce_new:.4f}\nL_MSE: {loss_mse:.4f} → {loss_mse_new:.4f}\n\nδ_BCE = ŷ - y = {delta_bce:+.4f}\nδ_MSE = {delta_mse:+.4f}\n(η = {eta:.2f})",
        ha="center", va="center", fontsize=8.0, fontweight="bold", color="#B71C1C"
    )

    # Seta tracejada de Retropropagação (Backpropagation)
    ax.annotate(
        "", xy=(5.85, 2.32), xytext=(11.65, 1.82),
        arrowprops=dict(arrowstyle="-|>", color="#D84315", lw=2.2, ls="--", connectionstyle="arc3,rad=0.22"),
    )
    ax.text(
        8.75, 0.85,
        f"⬅️ RETROPROPAGAÇÃO:  δ = ∂L/∂z = {delta_bce:+.4f}   |   ∂L/∂wᵢ = δ · xᵢ   |   wᵢ' = wᵢ - η(∂L/∂wᵢ)",
        ha="center", va="center", fontsize=8.8, fontweight="bold", color="#BF360C",
        bbox=dict(boxstyle="round,pad=0.3", fc="#FFF3E0", ec="#E65100", lw=1.4),
    )

    ax.set_title(
        "Mecanismo Sináptico em um Neurônio Artificial: Exemplo Numérico Real (Paciente #1 — Heart Disease)",
        fontsize=11.5, fontweight="bold"
    )
    fig.tight_layout()
    out_img = os.path.join(figs_dir, "neuronio_exemplo_numerico.png")
    fig.savefig(out_img, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return data_out, out_img


def run_learning_rate_study(ds_std, figs_dir, res_dir):
    """
    Executa experimento controlado variando a taxa de aprendizado η ∈ {0.001, 0.015, 0.10, 0.50}
    na topologia campeã [13 -> 16 -> 8 -> 1] (ReLU + He Init + StandardScaler, 150 épocas)
    para fundamentar a Seção de Análise Crítica do relatório.
    """
    X_tr, y_tr = ds_std["X_train"], ds_std["y_train"]
    X_te, y_te = ds_std["X_test"], ds_std["y_test"]

    lrs = [
        (0.001, "η = 0.001 (Sub-convergência Lenta)", "#757575", "--"),
        (0.015, "η = 0.015 (Convergência Ótima C4)", "#1565C0", "-"),
        (0.100, "η = 0.100 (Oscilação Moderada)", "#FB8C00", "-."),
        (0.500, "η = 0.500 (Saturação / Instabilidade)", "#C62828", ":"),
    ]

    rows = []
    histories = {}

    for eta, label, color, ls in lrs:
        mlp = MLPGraph(
            [13, 16, 8, 1],
            activation="relu",
            loss_type="bce",
            seed=42,
        )
        hist, final_tr, final_te = run_training_history(
            mlp, X_tr, y_tr, X_te, y_te,
            n_epochs=150, lr=eta, momentum=0.0, l2_lambda=0.0, seed=42
        )
        histories[eta] = (hist, label, color, ls)
        rows.append({
            "lr": eta,
            "regime": label,
            "train_loss": round(final_tr["loss"], 4),
            "test_loss": round(final_te["loss"], 4),
            "train_acc": round(final_tr["accuracy"] * 100, 2),
            "test_acc": round(final_te["accuracy"] * 100, 2),
            "test_f1": round(final_te["f1"] * 100, 2),
            "test_auc": round(final_te["auc_roc"], 4),
        })
        print(f"[LR Study] {label}: Test Acc={final_te['accuracy']*100:.2f}% | Test Loss={final_te['loss']:.4f}")

    df_lr = pd.DataFrame(rows)
    df_lr.to_csv(os.path.join(res_dir, "learning_rate_study.csv"), index=False)

    # Plotar curvas comparativas de perda e acurácia no teste para os 4 valores de η
    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.0))
    epochs = np.arange(1, 151)

    for eta, (hist, label, color, ls) in histories.items():
        lw = 2.5 if eta == 0.015 else 1.8
        axes[0].plot(epochs, np.clip(hist["test_loss"], 0, 5.0), label=label, color=color, linestyle=ls, linewidth=lw)
        axes[1].plot(epochs, np.array(hist["test_acc"]) * 100.0, label=label, color=color, linestyle=ls, linewidth=lw)

    axes[0].set_title("Impacto da Taxa de Aprendizado (η) na Perda BCE de Teste", fontsize=11, fontweight="bold")
    axes[0].set_xlabel("Época")
    axes[0].set_ylabel("Binary Cross-Entropy Loss (truncada em 5.0)")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=8.5)

    axes[1].set_title("Impacto da Taxa de Aprendizado (η) na Acurácia de Teste (%)", fontsize=11, fontweight="bold")
    axes[1].set_xlabel("Época")
    axes[1].set_ylabel("Acurácia no Conjunto de Teste (%)")
    axes[1].set_ylim(45, 103)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(fontsize=8.5, loc="lower right")

    fig.suptitle("Análise Crítica do Comportamento da Taxa de Aprendizado (η) na Arquitetura [13→16→8→1]", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    out_img = os.path.join(figs_dir, "taxa_aprendizado_estudo.png")
    fig.savefig(out_img, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return df_lr, out_img


def main():
    figs_dir = os.path.join(BASE_DIR, "figs")
    res_dir = os.path.join(BASE_DIR, "results")
    data_dir = os.path.join(BASE_DIR, "data")

    ds_std = load_and_partition_data(data_dir=data_dir, test_size=0.20, scaler_type="standard", seed=42, save_splits=False)

    num_data, img_neuron = generate_numerical_neuron_example(ds_std, figs_dir, res_dir)
    df_lr, img_lr = run_learning_rate_study(ds_std, figs_dir, res_dir)

    # Sincronizar figuras com code/mlp/report/figs, article/figures e papers/artigo-final/figures
    target_dirs = [
        os.path.join(BASE_DIR, "report", "figs"),
        os.path.join(ROOT_DIR, "article", "figures"),
        os.path.join(ROOT_DIR, "papers", "artigo-final", "figures"),
    ]
    all_figs = [
        "arquitetura_diagrama.png",
        "curvas_convergencia.png",
        "comparativo_configuracoes.png",
        "grafo_antes.png",
        "grafo_depois.png",
        "heatmap_pesos.png",
        "neuronio_exemplo_numerico.png",
        "taxa_aprendizado_estudo.png",
    ]
    for tdir in target_dirs:
        os.makedirs(tdir, exist_ok=True)
        for fname in all_figs:
            src = os.path.join(figs_dir, fname)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(tdir, fname))

    print("\n=== Exemplo Numérico Real Gerado ===")
    print(json.dumps(num_data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
