"""
core_cnn/dataset.py
===================
Gestão de dados do CIFAR-10 seguindo o protocolo do artigo base
(Dizabadi, arXiv:2604.23861, 2026 - Seção 3.1):

* 25.000 imagens de treino e 5.000 de teste (fase de dados reduzidos);
* subconjuntos ESTRATIFICADOS (2.500 / 500 imagens por classe) com semente fixa,
  garantindo reprodutibilidade e balanceamento entre as 10 classes;
* normalização por canal com média/desvio calculados SOMENTE no subconjunto de treino;
* data augmentation opcional (RandomCrop 32 com padding 4 + flip horizontal),
  usada pela Modificação 2 e pelo modelo combinado.
"""
import json
import os
import shutil

import numpy as np
import torch
import torchvision
import torchvision.transforms as T

CLASSES = ("airplane", "automobile", "bird", "cat", "deer",
           "dog", "frog", "horse", "ship", "truck")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LEGACY_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "Atividade_02_CNN", "data")


def ensure_cifar10(data_dir: str = DATA_DIR) -> str:
    """Garante o CIFAR-10 oficial em `data_dir` (reaproveita a cópia local ou baixa da fonte oficial)."""
    target = os.path.join(data_dir, "cifar-10-batches-py")
    if os.path.isdir(target) and os.path.exists(os.path.join(target, "test_batch")):
        return data_dir
    os.makedirs(data_dir, exist_ok=True)
    legacy = os.path.join(LEGACY_DATA_DIR, "cifar-10-batches-py")
    if os.path.isdir(legacy):
        print(f"[dataset] Reaproveitando cópia local do CIFAR-10: {legacy}")
        shutil.copytree(legacy, target)
    else:
        print("[dataset] Baixando CIFAR-10 oficial (https://www.cs.toronto.edu/~kriz/cifar.html)...")
        torchvision.datasets.CIFAR10(root=data_dir, train=True, download=True)
        torchvision.datasets.CIFAR10(root=data_dir, train=False, download=True)
    return data_dir


def stratified_indices(targets, per_class: int, seed: int):
    rng = np.random.default_rng(seed)
    targets = np.asarray(targets)
    idx = []
    for c in range(10):
        cls_idx = np.where(targets == c)[0]
        idx.extend(rng.choice(cls_idx, size=per_class, replace=False).tolist())
    idx = np.array(sorted(idx))
    return idx


def compute_mean_std(dataset_raw, indices):
    data = dataset_raw.data[indices].astype(np.float32) / 255.0  # (N, 32, 32, 3)
    return data.mean(axis=(0, 1, 2)).tolist(), data.std(axis=(0, 1, 2)).tolist()


def get_loaders(n_train: int = 25000, n_test: int = 5000, batch_size: int = 64,
                augment: bool = False, seed: int = 42, data_dir: str = DATA_DIR,
                split_file: str = None):
    """Retorna (train_loader, test_loader, info) seguindo o protocolo 25k/5k do artigo."""
    ensure_cifar10(data_dir)
    raw_train = torchvision.datasets.CIFAR10(root=data_dir, train=True, download=False)
    raw_test = torchvision.datasets.CIFAR10(root=data_dir, train=False, download=False)

    tr_idx = stratified_indices(raw_train.targets, n_train // 10, seed)
    te_idx = stratified_indices(raw_test.targets, n_test // 10, seed)
    mean, std = compute_mean_std(raw_train, tr_idx)

    normalize = T.Normalize(mean, std)
    train_tf = [T.RandomCrop(32, padding=4), T.RandomHorizontalFlip()] if augment else []
    train_tf = T.Compose(train_tf + [T.ToTensor(), normalize])
    test_tf = T.Compose([T.ToTensor(), normalize])

    ds_train = torchvision.datasets.CIFAR10(root=data_dir, train=True, download=False, transform=train_tf)
    ds_test = torchvision.datasets.CIFAR10(root=data_dir, train=False, download=False, transform=test_tf)

    g = torch.Generator().manual_seed(seed)
    train_loader = torch.utils.data.DataLoader(torch.utils.data.Subset(ds_train, tr_idx),
                                               batch_size=batch_size, shuffle=True, generator=g, num_workers=0)
    test_loader = torch.utils.data.DataLoader(torch.utils.data.Subset(ds_test, te_idx),
                                              batch_size=256, shuffle=False, num_workers=0)

    info = {
        "dataset": "CIFAR-10 (Krizhevsky, 2009) - fonte oficial",
        "n_train": int(len(tr_idx)), "n_test": int(len(te_idx)),
        "per_class_train": n_train // 10, "per_class_test": n_test // 10,
        "seed": seed, "mean": mean, "std": std, "augment": augment, "batch_size": batch_size,
    }
    if split_file:
        os.makedirs(os.path.dirname(split_file), exist_ok=True)
        with open(split_file, "w", encoding="utf-8") as f:
            json.dump({**info, "train_indices": tr_idx.tolist(), "test_indices": te_idx.tolist()}, f, indent=2)
    return train_loader, test_loader, info
