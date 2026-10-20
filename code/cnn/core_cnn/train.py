"""
core_cnn/train.py
=================
Rotinas padronizadas de treinamento, avaliação multimétrica e inferência.
Calcula Acurácia, Loss, F1-Score (macro), Matriz de Confusão por classe,
tempo de treino e taxa de inferência (amostras/segundo).
"""
import time
import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import f1_score, confusion_matrix


def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, targets in loader:
        images, targets = images.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * targets.size(0)
        _, preds = outputs.max(1)
        correct += preds.eq(targets).sum().item()
        total += targets.size(0)

    epoch_loss = running_loss / total
    epoch_acc = correct / total
    return epoch_loss, epoch_acc


@torch.no_grad()
def evaluate_model(model, loader, criterion, device):
    model.eval()
    running_loss = 0.0
    all_preds = []
    all_targets = []
    start_time = time.time()

    for images, targets in loader:
        images, targets = images.to(device), targets.to(device)
        outputs = model(images)
        loss = criterion(outputs, targets)
        running_loss += loss.item() * targets.size(0)
        _, preds = outputs.max(1)
        all_preds.extend(preds.cpu().numpy().tolist())
        all_targets.extend(targets.cpu().numpy().tolist())

    eval_time = time.time() - start_time
    total = len(all_targets)
    all_preds = np.array(all_preds)
    all_targets = np.array(all_targets)

    acc = float(np.mean(all_preds == all_targets))
    loss = running_loss / total
    f1_macro = float(f1_score(all_targets, all_preds, average="macro"))
    cm = confusion_matrix(all_targets, all_preds).tolist()
    throughput = total / max(eval_time, 1e-6)

    return {
        "loss": float(loss),
        "accuracy": float(acc),
        "f1_macro": float(f1_macro),
        "confusion_matrix": cm,
        "eval_time_sec": float(eval_time),
        "throughput_samples_per_sec": float(throughput),
        "predictions": all_preds.tolist(),
        "targets": all_targets.tolist()
    }


def fit_model(model, train_loader, test_loader, epochs: int, lr: float = 0.001,
              device: str = "cpu", model_name: str = "Model", log_callback=None):
    model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    history = {
        "epoch": [],
        "train_loss": [],
        "train_acc": [],
        "test_loss": [],
        "test_acc": [],
        "epoch_time": []
    }

    print(f"\n==================================================")
    print(f" Treinando: {model_name} | Épocas: {epochs} | Device: {device}")
    print(f"==================================================")
    total_start = time.time()

    for ep in range(1, epochs + 1):
        ep_start = time.time()
        tr_loss, tr_acc = train_one_epoch(model, train_loader, criterion, optimizer, device)
        te_eval = evaluate_model(model, test_loader, criterion, device)
        ep_duration = time.time() - ep_start

        history["epoch"].append(ep)
        history["train_loss"].append(tr_loss)
        history["train_acc"].append(tr_acc)
        history["test_loss"].append(te_eval["loss"])
        history["test_acc"].append(te_eval["accuracy"])
        history["epoch_time"].append(ep_duration)

        msg = (f"Época [{ep:02d}/{epochs:02d}] - {ep_duration:.1f}s | "
               f"Tr Loss: {tr_loss:.4f} Tr Acc: {tr_acc*100:.2f}% | "
               f"Te Loss: {te_eval['loss']:.4f} Te Acc: {te_eval['accuracy']*100:.2f}%")
        print(msg)
        if log_callback:
            log_callback(ep, epochs, tr_loss, tr_acc, te_eval['loss'], te_eval['accuracy'])

    total_time = time.time() - total_start
    final_eval = evaluate_model(model, test_loader, criterion, device)
    final_eval["total_training_time_sec"] = total_time
    final_eval["history"] = history
    return model, final_eval
