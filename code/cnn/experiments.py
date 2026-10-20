"""
experiments.py
==============
Pipeline completo de reprodução empírica e estudo de ablação da Atividade 02 (CNNs):
- Modelo 1 (Baseline): 6 Conv (32-32-64-64-128-128) + 7 BN + Dropout + Dense 128 (25 épocas)
- Modelo 2 (Mod 1 - Conexões Residuais): Skip-connections nos 3 blocos duplos (15 épocas)
- Modelo 3 (Mod 2 - Data Augmentation): Baseline + RandomCrop 32/padding 4 + HorizontalFlip (15 épocas)
- Modelo 4 (Mod 3 - Squeeze-and-Excitation): Atenção por canal pós-blocos conv (15 épocas)
- Modelo 5 (Combined - 3 Modificações Integradas): Resíduos + SE-Block + Augmentation (25 épocas)

Gera:
- Checkpoints em `code/cnn/results/checkpoints/`
- Gráficos comparativos de Loss e Acurácia (treino e teste) em `code/cnn/figs/`
- Tabela resumo consolidada em `code/cnn/results/cnn_ablation_results.csv` e `.json`
"""
import os
import sys
import json
import time
import pandas as pd
import numpy as np
import torch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from core_cnn.dataset import get_loaders, CLASSES
from core_cnn.models import (
    BaselineCNN,
    Mod1_ResidualCNN,
    Mod3_SE_CNN,
    CombinedCNN,
    count_parameters
)
from core_cnn.train import fit_model, evaluate_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIGS_DIR = os.path.join(BASE_DIR, "figs")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
CKPT_DIR = os.path.join(RESULTS_DIR, "checkpoints")

os.makedirs(FIGS_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(CKPT_DIR, exist_ok=True)


def plot_comparative_curves(experiments_data):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    
    colors = {
        "Baseline (Artigo)": "#D32F2F",
        "Mod 1: Conexões Residuais": "#7B1FA2",
        "Mod 2: Data Augmentation": "#F57C00",
        "Mod 3: Squeeze-and-Excitation": "#0288D1",
        "Modelo Combinado (Res+SE+Aug)": "#2E7D32"
    }

    # Loss
    for exp in experiments_data:
        name = exp["name"]
        hist = exp["history"]
        epochs = hist["epoch"]
        c = colors.get(name, "#333333")
        axes[0].plot(epochs, hist["train_loss"], label=f"{name} (Treino)", linestyle="--", alpha=0.5, color=c)
        axes[0].plot(epochs, hist["test_loss"], label=f"{name} (Teste)", linewidth=2.0, color=c)

    axes[0].set_title("Evolução da Perda (Cross-Entropy Loss)", fontsize=11, fontweight="bold")
    axes[0].set_xlabel("Época")
    axes[0].set_ylabel("Loss")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=7.5, loc="upper right")

    # Acurácia
    for exp in experiments_data:
        name = exp["name"]
        hist = exp["history"]
        epochs = hist["epoch"]
        c = colors.get(name, "#333333")
        train_acc_pct = [a * 100.0 for a in hist["train_acc"]]
        test_acc_pct = [a * 100.0 for a in hist["test_acc"]]
        axes[1].plot(epochs, train_acc_pct, label=f"{name} (Treino)", linestyle="--", alpha=0.5, color=c)
        axes[1].plot(epochs, test_acc_pct, label=f"{name} (Teste)", linewidth=2.0, color=c)

    axes[1].set_title("Evolução da Acurácia no CIFAR-10 (%)", fontsize=11, fontweight="bold")
    axes[1].set_xlabel("Época")
    axes[1].set_ylabel("Acurácia (%)")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(fontsize=7.5, loc="lower right")

    fig.suptitle("Estudo de Ablação e Modificações Arquiteturais na CNN (CIFAR-10)", fontsize=13, fontweight="bold")
    fig.tight_layout()
    out_path = os.path.join(FIGS_DIR, "curvas_comparativas_ablation.png")
    fig.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Curvas salvas em: {out_path}")


def run_all(fast_mode=False):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[experimentos] Executando pipeline completo no dispositivo: {device}")

    # Configuração dos experimentos
    configs = [
        {
            "id": "baseline",
            "name": "Baseline (Artigo)",
            "model_cls": BaselineCNN,
            "augment": False,
            "epochs": 2 if fast_mode else 25,
            "desc": "Réplica exata da arquitetura de 6 Convs do artigo (Dizabadi, 2026)"
        },
        {
            "id": "mod1_residual",
            "name": "Mod 1: Conexões Residuais",
            "model_cls": Mod1_ResidualCNN,
            "augment": False,
            "epochs": 2 if fast_mode else 15,
            "desc": "Inclusão de atalhos residuais (skip connections) estilo ResNet"
        },
        {
            "id": "mod2_augment",
            "name": "Mod 2: Data Augmentation",
            "model_cls": BaselineCNN,
            "augment": True,
            "epochs": 2 if fast_mode else 15,
            "desc": "RandomCrop(32, padding=4) + RandomHorizontalFlip()"
        },
        {
            "id": "mod3_se",
            "name": "Mod 3: Squeeze-and-Excitation",
            "model_cls": Mod3_SE_CNN,
            "augment": False,
            "epochs": 2 if fast_mode else 15,
            "desc": "Mecanismo de atenção por canal (SE-block) pós-convoluções"
        },
        {
            "id": "combined",
            "name": "Modelo Combinado (Res+SE+Aug)",
            "model_cls": CombinedCNN,
            "augment": True,
            "epochs": 2 if fast_mode else 25,
            "desc": "Integração cumulativa: Conexões Residuais + SE-Block + Data Augmentation"
        }
    ]

    results_table = []
    experiments_data = []

    for cfg in configs:
        model = cfg["model_cls"]()
        param_info = count_parameters(model)
        
        train_loader, test_loader, split_info = get_loaders(
            n_train=25000,
            n_test=5000,
            batch_size=64,
            augment=cfg["augment"],
            seed=42
        )

        trained_model, eval_res = fit_model(
            model=model,
            train_loader=train_loader,
            test_loader=test_loader,
            epochs=cfg["epochs"],
            lr=0.001,
            device=device,
            model_name=cfg["name"]
        )

        # Salvar checkpoint
        ckpt_file = os.path.join(CKPT_DIR, f"{cfg['id']}_model.pth")
        torch.save({
            "model_state": trained_model.state_dict(),
            "config": cfg,
            "eval": eval_res,
            "param_info": param_info
        }, ckpt_file)

        row = {
            "ID": cfg["id"],
            "Configuração": cfg["name"],
            "Épocas": cfg["epochs"],
            "Parâmetros Treináveis": param_info["trainable"],
            "Parâmetros Totais (c/ BN)": param_info["keras_param_count"],
            "Acurácia Teste (%)": round(eval_res["accuracy"] * 100.0, 2),
            "Loss Teste": round(eval_res["loss"], 4),
            "F1-Score Macro (%)": round(eval_res["f1_macro"] * 100.0, 2),
            "Tempo Treino (s)": round(eval_res["total_training_time_sec"], 1),
            "Throughput (amostras/s)": round(eval_res["throughput_samples_per_sec"], 1)
        }
        results_table.append(row)
        experiments_data.append({
            "id": cfg["id"],
            "name": cfg["name"],
            "history": eval_res["history"],
            "metrics": row
        })

    # Gerar gráficos e tabelas
    plot_comparative_curves(experiments_data)

    df = pd.DataFrame(results_table)
    csv_path = os.path.join(RESULTS_DIR, "cnn_ablation_results.csv")
    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"\n[resultados] Tabela CSV salva em: {csv_path}")

    json_path = os.path.join(RESULTS_DIR, "cnn_ablation_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(experiments_data, f, indent=2, ensure_ascii=False)
    print(f"[resultados] JSON salvo em: {json_path}")

    print("\n=== TABELA FINAL DE RESULTADOS CONSOLIDADOS ===")
    print(df.to_string(index=False))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true", help="Modo rápido para teste de pipeline (2 épocas)")
    args = parser.parse_args()
    run_all(fast_mode=args.fast)
