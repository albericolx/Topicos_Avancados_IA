"""
core_mlp/dataset.py
===================
Download/carregamento, padronização sem vazamento de dados (zero data leakage)
e particionamento explícito em Treino (80%) e Teste (20%) do dataset Heart Disease.
"""
import os
import urllib.request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

HEART_URLS = [
    "https://raw.githubusercontent.com/kb22/Heart-Disease-Prediction/master/dataset.csv",
    "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/heart/heart.csv",
]

FEATURE_DESCRIPTIONS = {
    "age": "Idade do paciente (anos)",
    "sex": "Sexo biológico (1 = masculino, 0 = feminino)",
    "cp": "Tipo de dor torácica (0 = típica, 1 = atípica, 2 = não-anginosa, 3 = assintomática)",
    "trestbps": "Pressão arterial em repouso (mm Hg)",
    "chol": "Colesterol sérico total (mg/dl)",
    "fbs": "Glicemia em jejum > 120 mg/dl (1 = verdadeiro, 0 = falso)",
    "restecg": "Resultados eletrocardiográficos em repouso (0, 1, 2)",
    "thalach": "Frequência cardíaca máxima alcançada (bpm)",
    "exang": "Angina induzida por exercício (1 = sim, 0 = não)",
    "oldpeak": "Depressão do segmento ST induzida por exercício",
    "slope": "Inclinação do segmento ST no pico do exercício (0, 1, 2)",
    "ca": "Número de vasos principais coloridos por fluoroscopia (0–4)",
    "thal": "Talassemia (0 = nulo, 1 = defeito fixo, 2 = normal, 3 = defeito reversível)",
}


def ensure_dataset(data_dir: str) -> str:
    """Garante que heart.csv exista em data_dir; baixa automaticamente se necessário."""
    os.makedirs(data_dir, exist_ok=True)
    csv_path = os.path.join(data_dir, "heart.csv")
    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 1000:
        return csv_path

    for url in HEART_URLS:
        try:
            urllib.request.urlretrieve(url, csv_path)
            if os.path.exists(csv_path) and os.path.getsize(csv_path) > 1000:
                return csv_path
        except Exception:
            continue

    raise FileNotFoundError(f"Não foi possível localizar ou baixar o arquivo {csv_path}")


def load_and_partition_data(
    data_dir: str = None,
    test_size: float = 0.20,
    scaler_type: str = "standard",
    deduplicate: bool = False,
    n_features: int = 13,
    seed: int = 42,
    save_splits: bool = True,
):
    """
    Carrega o dataset Heart Disease, particiona explicitamente em 80% treino e 20% teste
    (estratificado por classe) e padroniza os atributos ajustando o scaler APENAS no treino.

    Returns
    -------
    dict contendo:
        X_train, X_test, y_train, y_test, feature_names, df_raw, scaler, split_info
    """
    if data_dir is None:
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

    csv_path = ensure_dataset(data_dir)
    df = pd.read_csv(csv_path)
    if deduplicate:
        df = df.drop_duplicates().reset_index(drop=True)

    feature_cols = [c for c in df.columns if c != "target"][:n_features]
    X_raw = df[feature_cols].values.astype(float)
    y = df["target"].values.astype(float)

    # 1. Particionamento explícito 80% Treino / 20% Teste (estratificado)
    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X_raw, y, test_size=test_size, random_state=seed, stratify=y
    )

    # 2. Padronização sem Data Leakage (fit apenas no conjunto de treino)
    if scaler_type == "minmax":
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train_raw)
    X_test = scaler.transform(X_test_raw)

    # 3. Persistência opcional das partições 80/20 padronizadas em disco
    if save_splits:
        train_df = pd.DataFrame(X_train, columns=feature_cols)
        train_df["target"] = y_train.astype(int)
        test_df = pd.DataFrame(X_test, columns=feature_cols)
        test_df["target"] = y_test.astype(int)
        train_df.to_csv(os.path.join(data_dir, "train_80_standardized.csv"), index=False)
        test_df.to_csv(os.path.join(data_dir, "test_20_standardized.csv"), index=False)

    split_info = {
        "total_samples": len(df),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "train_ratio": len(X_train) / len(df),
        "test_ratio": len(X_test) / len(df),
        "train_pos_rate": float(np.mean(y_train)),
        "test_pos_rate": float(np.mean(y_test)),
        "scaler_type": scaler_type,
        "n_features": len(feature_cols),
    }

    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "feature_names": feature_cols,
        "df_raw": df,
        "scaler": scaler,
        "split_info": split_info,
    }
