"""
core_mlp/train.py
=================
Rotinas de treinamento (época a época e histórico completo) e avaliação multimétrica
da Rede Neural Multicamadas (MLPGraph).
"""
import numpy as np


def bce_loss(pred, target):
    """Binary Cross-Entropy (BCE) Loss numericamente estável."""
    p = np.clip(pred, 1e-7, 1.0 - 1e-7)
    return float(-(target * np.log(p) + (1.0 - target) * np.log(1.0 - p)))


def mse_loss(pred, target):
    """Mean Squared Error (MSE) Loss."""
    return float(0.5 * (pred - target) ** 2)


def train_epoch(mlp, X_train, y_train, lr=0.01, momentum=0.0, l2_lambda=0.0, rng=None):
    """
    Executa uma época completa de treinamento (Forward Pass + Backpropagation)
    e registra a variação líquida dos pesos sinápticos (Δw) na época.
    """
    if rng is None:
        idx = np.random.permutation(len(X_train))
    else:
        idx = rng.permutation(len(X_train))

    prev_snap = mlp.snapshot_weights()
    total_loss = 0.0

    for i in idx:
        out = mlp.forward(X_train[i])
        mlp.backward(y_train[i], lr=lr, momentum=momentum, l2_lambda=l2_lambda)
        if mlp.loss_type == "mse":
            total_loss += mse_loss(out, y_train[i])
        else:
            total_loss += bce_loss(out, y_train[i])

    # Atualiza prev_weight e delta_weight acumulando a mudança da época inteira
    mlp.update_epoch_deltas(prev_snap)
    return total_loss / len(X_train)


def evaluate(mlp, X_eval, y_eval):
    """
    Avalia a MLP em um conjunto de dados (treino ou teste), retornando loss,
    acurácia, precisão, recall, F1-Score, especificidade, AUC-ROC e matriz de confusão.
    """
    probas = np.array([mlp.forward(X_eval[i]) for i in range(len(X_eval))], dtype=float)
    preds = (probas >= 0.5).astype(int)
    labels = y_eval.astype(int)

    losses = [
        mse_loss(probas[i], labels[i]) if mlp.loss_type == "mse" else bce_loss(probas[i], labels[i])
        for i in range(len(labels))
    ]
    avg_loss = float(np.mean(losses)) if len(losses) > 0 else 0.0

    tp = int(np.sum((preds == 1) & (labels == 1)))
    tn = int(np.sum((preds == 0) & (labels == 0)))
    fp = int(np.sum((preds == 1) & (labels == 0)))
    fn = int(np.sum((preds == 0) & (labels == 1)))

    accuracy = (tp + tn) / len(labels) if len(labels) > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    f1 = (2.0 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
    auc_roc = _roc_auc(labels, probas)

    return {
        "loss": avg_loss,
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "specificity": float(specificity),
        "f1": float(f1),
        "auc_roc": float(auc_roc),
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "predictions": preds,
        "probas": probas,
    }


def _roc_auc(labels, scores):
    """Calcula a área sob a curva ROC (AUC-ROC) via integração trapezoidal."""
    thresholds = np.linspace(0.0, 1.0, 201)
    pos = np.sum(labels == 1)
    neg = np.sum(labels == 0)
    if pos == 0 or neg == 0:
        return 0.5

    tprs, fprs = [], []
    for t in thresholds:
        preds = (scores >= t).astype(int)
        tp = np.sum((preds == 1) & (labels == 1))
        fp = np.sum((preds == 1) & (labels == 0))
        tprs.append(tp / pos)
        fprs.append(fp / neg)

    tprs = np.array(tprs)
    fprs = np.array(fprs)
    order = np.argsort(fprs)
    if hasattr(np, "trapezoid"):
        return float(np.trapezoid(tprs[order], fprs[order]))
    return float(np.trapz(tprs[order], fprs[order]))


def run_training_history(
    mlp,
    X_train,
    y_train,
    X_test,
    y_test,
    n_epochs=150,
    lr=0.01,
    lr_decay=0.0,
    momentum=0.0,
    l2_lambda=0.0,
    eval_every=1,
    seed=42,
):
    """
    Executa o ciclo completo de treinamento registrando histórico época a época.
    """
    rng = np.random.default_rng(seed)
    history = {
        "epoch": [],
        "train_loss": [],
        "test_loss": [],
        "train_acc": [],
        "test_acc": [],
        "mean_abs_weight": [],
        "mean_abs_delta_w": [],
    }

    for ep in range(1, n_epochs + 1):
        curr_lr = lr / (1.0 + lr_decay * (ep - 1))
        tr_loss = train_epoch(
            mlp, X_train, y_train, lr=curr_lr, momentum=momentum, l2_lambda=l2_lambda, rng=rng
        )

        if ep % eval_every == 0 or ep == 1 or ep == n_epochs:
            tr_eval = evaluate(mlp, X_train, y_train)
            te_eval = evaluate(mlp, X_test, y_test)
            weights = [abs(mlp.graph[u][v]["weight"]) for u, v in mlp.graph.edges()]
            deltas = [abs(mlp.graph[u][v]["delta_weight"]) for u, v in mlp.graph.edges()]

            history["epoch"].append(ep)
            history["train_loss"].append(tr_loss)
            history["test_loss"].append(te_eval["loss"])
            history["train_acc"].append(tr_eval["accuracy"])
            history["test_acc"].append(te_eval["accuracy"])
            history["mean_abs_weight"].append(float(np.mean(weights)))
            history["mean_abs_delta_w"].append(float(np.mean(deltas)))

    final_train = evaluate(mlp, X_train, y_train)
    final_test = evaluate(mlp, X_test, y_test)
    return history, final_train, final_test
