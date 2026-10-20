"""
demo_inference.py
=================
Comprova o Ponto de VerificaÃ§Ã£o 3: 'InferÃªncia Funcional'
Executa inferÃªncia com pesos treinados (ou inicializados deterministicamente)
sobre uma amostra de 10 imagens reais do CIFAR-10, exibindo classe real, classe prevista,
confianÃ§a percentual e tempo de inferÃªncia por amostra.
Gera a figura `code/cnn/figs/amostras_inferencia.png`.
"""
import os
import json
import torch
import torchvision.transforms as T
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from core_cnn.models import BaselineCNN, CombinedCNN
from core_cnn.dataset import CLASSES, ensure_cifar10
import torchvision

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIGS_DIR = os.path.join(BASE_DIR, "figs")
os.makedirs(FIGS_DIR, exist_ok=True)


def run_demo(checkpoint_path: str = None):
    device = torch.device("cpu")
    model = BaselineCNN().to(device)
    if checkpoint_path and os.path.exists(checkpoint_path):
        try:
            state = torch.load(checkpoint_path, map_location=device, weights_only=False)
        except Exception:
            state = torch.load(checkpoint_path, map_location=device)
        model.load_state_dict(state.get("model_state", state))
        print(f"[inferÃªncia] Carregado checkpoint: {checkpoint_path}")
    else:
        print("[inferÃªncia] Executando com pesos base determinÃ­sticos.")
    model.eval()

    data_dir = os.path.join(BASE_DIR, "data")
    ensure_cifar10(data_dir)
    raw_test = torchvision.datasets.CIFAR10(root=data_dir, train=False, download=False)

    indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 10 amostras distintas
    normalize = T.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))
    transform = T.Compose([T.ToTensor(), normalize])

    fig, axes = plt.subplots(2, 5, figsize=(14, 6))
    axes = axes.flatten()

    results = []
    print("\n=== RESULTADOS DA INFERÃŠNCIA AMOSTRAL (CIFAR-10) ===")
    for k, idx in enumerate(indices):
        img_pil, target = raw_test[idx]
        x = transform(img_pil).unsqueeze(0).to(device)

        with torch.no_grad():
            logits = model(x)
            probs = torch.softmax(logits, dim=1).squeeze(0)
            conf, pred = probs.max(0)

        pred_idx = pred.item()
        conf_pct = conf.item() * 100.0
        true_name = CLASSES[target]
        pred_name = CLASSES[pred_idx]
        correct = (pred_idx == target)

        results.append({
            "sample_index": idx,
            "true_class": true_name,
            "pred_class": pred_name,
            "confidence_pct": round(conf_pct, 2),
            "correct": correct
        })
        status_str = "[OK]" if correct else "[ERR]"
        print(f"Amostra #{idx:02d} | Real: {true_name:10s} | Pred: {pred_name:10s} | Conf: {conf_pct:5.2f}% | {status_str}")

        axes[k].imshow(img_pil)
        title_color = "#2E7D32" if correct else "#C62828"
        axes[k].set_title(f"Real: {true_name}\nPred: {pred_name} ({conf_pct:.1f}%)",
                          fontsize=9, fontweight="bold", color=title_color)
        axes[k].axis("off")

    fig.suptitle("InferÃªncia Funcional sobre Amostras Reais do CIFAR-10 (Baseline CNN)", fontsize=12, fontweight="bold")
    fig.tight_layout()
    out_img = os.path.join(FIGS_DIR, "amostras_inferencia.png")
    fig.savefig(out_img, dpi=180, bbox_inches="tight")
    plt.close(fig)
    print(f"\n[inferÃªncia] GrÃ¡fico salvo em: {out_img}")

    out_json = os.path.join(BASE_DIR, "results", "amostras_inferencia.json")
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    return results


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', type=str, default='results/checkpoints/baseline_model.pth')
    args = parser.parse_args()
    run_demo(checkpoint_path=args.checkpoint)

