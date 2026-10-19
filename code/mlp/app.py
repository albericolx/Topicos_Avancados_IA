"""
app.py — Interface Interativa Streamlit para Experimentação da MLP do Zero
==========================================================================
Artefato [5] · mlp git repo (código no painel: mlp·c)
Implementação do zero de uma Rede Neural Multicamadas (MLP) como grafo direcionado
(NetworkX DiGraph + NumPy), com controle em tempo real de hiperparâmetros,
particionamento explícito 80/20, dinâmica completa de Forward/Backpropagation
e inspeção visual + numérica dos pesos sinápticos a cada época.

Execução:
    streamlit run code/mlp/app.py
"""
import os
import sys
import time
import warnings
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

sys.path.insert(0, os.path.dirname(__file__))

from core_mlp.dataset import load_and_partition_data, FEATURE_DESCRIPTIONS
from core_mlp.graph import MLPGraph
from core_mlp.train import train_epoch, evaluate
from core_mlp.visualize import (
    draw_network,
    draw_weights_heatmap,
    draw_loss,
    draw_accuracy,
    get_weights_dataframe,
    save_graph_image,
    layer_edges,
    all_forward_edges,
)


@st.cache_data
def get_partitioned_dataset(test_size, scaler_type, deduplicate, n_features, seed):
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    return load_and_partition_data(
        data_dir=data_dir,
        test_size=test_size,
        scaler_type=scaler_type,
        deduplicate=deduplicate,
        n_features=n_features,
        seed=seed,
        save_splits=True,
    )


def main():
    st.set_page_config(
        page_title="MLP do Zero — Grafo Direcionado & Inspeção Sináptica",
        page_icon="🧠",
        layout="wide",
    )
    st.title("🧠 Rede Neural Multicamadas (MLP) do Zero — Grafo Direcionado")
    st.caption(
        "Artefato [5] · mlp·c  |  NumPy + NetworkX DiGraph + Streamlit  |  "
        "Particionamento 80/20 Sem Vazamento  |  UFRPE 2026.2 — Tópicos Avançados em IA"
    )

    # ====================================================================
    #  PAINEL LATERAL: PARAMETRIZAÇÃO INTERATIVA EM TEMPO REAL (PONTO 2)
    # ====================================================================
    st.sidebar.header("⚙️ 1. Arquitetura da Rede")
    num_hidden_layers = st.sidebar.slider("Número de Camadas Ocultas", 1, 4, 2)

    default_neurons = [16, 8, 6, 4]
    hidden_layers = []
    for idx in range(num_hidden_layers):
        n_neur = st.sidebar.slider(
            f"Neurônios — Camada Oculta {idx + 1}",
            min_value=2,
            max_value=32,
            value=default_neurons[idx],
            key=f"hl_{idx}",
        )
        hidden_layers.append(n_neur)

    activation_map = {
        "ReLU (Recomendada)": "relu",
        "Leaky ReLU": "leaky_relu",
        "Tanh (Tangente Hiperbólica)": "tanh",
        "Sigmoide (Logística)": "sigmoid",
        "ELU": "elu",
        "SELU": "selu",
        "ReLU6": "relu6",
    }
    act_label = st.sidebar.selectbox("Função de Ativação (Ocultas)", list(activation_map.keys()))
    activation = activation_map[act_label]

    st.sidebar.header("⚡ 2. Hiperparâmetros de Treino")
    lr = st.sidebar.slider("Taxa de Aprendizagem (η)", 0.001, 1.0, 0.015, 0.001, format="%.3f")
    momentum = st.sidebar.slider("Momentum (β)", 0.0, 0.95, 0.85, 0.05)
    l2_lambda = st.sidebar.select_slider(
        "Regularização L2 (λ)",
        options=[0.0, 1e-5, 1e-4, 5e-4, 1e-3, 5e-3],
        value=1e-4,
    )
    lr_decay = st.sidebar.select_slider(
        "Decaimento de LR por época",
        options=[0.0, 0.002, 0.005, 0.01, 0.02],
        value=0.005,
    )
    n_epochs = st.sidebar.slider("Número de Épocas", 10, 500, 150, 10)
    upd_every = st.sidebar.slider("Atualizar visualização a cada N épocas", 1, 50, 5)
    seed = int(st.sidebar.number_input("Semente Aleatória (Seed)", value=42, step=1))

    st.sidebar.header("🗂️ 3. Particionamento de Dados (80/20)")
    scaler_label = st.sidebar.selectbox(
        "Padronização (ajustada no Treino)",
        ["StandardScaler (Z-Score: μ=0, σ=1)", "MinMaxScaler (Intervalo [0, 1])"],
    )
    scaler_type = "standard" if "Standard" in scaler_label else "minmax"
    deduplicate = st.sidebar.checkbox(
        "Remover duplicatas do dataset Kaggle (usar 302 únicos vs 1025)", value=False
    )
    n_feat = st.sidebar.slider("Número de Atributos de Entrada", 2, 13, 13)

    st.sidebar.header("🔎 4. Visualização de Pesos")
    show_edge_weights = st.sidebar.checkbox(
        "Exibir valores numéricos dos pesos nas arestas", value=True
    )
    top_k_labels = st.sidebar.slider(
        "Rótulos numéricos por camada (0 = todos)", 0, 30, 8
    )

    # Carregar e particionar dados (80% treino / 20% teste)
    dataset = get_partitioned_dataset(
        test_size=0.20,
        scaler_type=scaler_type,
        deduplicate=deduplicate,
        n_features=n_feat,
        seed=seed,
    )
    X_train = dataset["X_train"]
    X_test = dataset["X_test"]
    y_train = dataset["y_train"]
    y_test = dataset["y_test"]
    split_info = dataset["split_info"]

    layer_sizes = [n_feat] + hidden_layers + [1]

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        f"**Topologia**: `{' → '.join(str(s) for s in layer_sizes)}` (+ bias)\n\n"
        f"**Partição Explícita 80/20**:\n"
        f"- Treino (80%): **{split_info['train_samples']}** amostras\n"
        f"- Teste (20%): **{split_info['test_samples']}** amostras\n"
        f"- Total: **{split_info['total_samples']}** amostras"
    )

    # ====================================================================
    #  ESTADO DA SESSÃO
    # ====================================================================
    state_defaults = {
        "mlp": None,
        "trained": False,
        "history": None,
        "train_metrics": {},
        "test_metrics": {},
        "epoch_snapshots": {},
    }
    for k, v in state_defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    if st.session_state.mlp is None or (
        st.session_state.mlp.layer_sizes != layer_sizes
        or st.session_state.mlp.activation != activation
    ):
        st.session_state.mlp = MLPGraph(layer_sizes, activation=activation, seed=seed)
        st.session_state.trained = False
        st.session_state.history = None
        st.session_state.train_metrics = evaluate(st.session_state.mlp, X_train, y_train)
        st.session_state.test_metrics = evaluate(st.session_state.mlp, X_test, y_test)
        st.session_state.epoch_snapshots = {0: get_weights_dataframe(st.session_state.mlp)}

    if st.sidebar.button("🔄 Reinicializar Pesos da Rede", type="primary"):
        mlp = MLPGraph(layer_sizes, activation=activation, seed=seed)
        figs_dir = os.path.join(os.path.dirname(__file__), "figs")
        os.makedirs(figs_dir, exist_ok=True)
        save_graph_image(
            mlp,
            os.path.join(figs_dir, "grafo_antes.png"),
            epoch=0,
            show_edge_weights=show_edge_weights,
            top_k_labels_per_layer=top_k_labels,
        )
        st.session_state.mlp = mlp
        st.session_state.trained = False
        st.session_state.history = None
        st.session_state.train_metrics = evaluate(mlp, X_train, y_train)
        st.session_state.test_metrics = evaluate(mlp, X_test, y_test)
        st.session_state.epoch_snapshots = {0: get_weights_dataframe(mlp)}
        st.sidebar.success("Rede reinicializada! Grafo inicial salvo em code/mlp/figs/grafo_antes.png")

    mlp = st.session_state.mlp

    # ====================================================================
    #  RESUMO DO PARTICIONAMENTO DE DADOS 80/20 (PONTO 3)
    # ====================================================================
    with st.expander("📂 Inspecionar Particionamento Explícito 80% Treino / 20% Teste e Padronização", expanded=False):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total de Pacientes", f"{split_info['total_samples']}")
        c2.metric("Conjunto de Treino (80%)", f"{split_info['train_samples']} ({split_info['train_ratio']:.0%})")
        c3.metric("Conjunto de Teste (20%)", f"{split_info['test_samples']} ({split_info['test_ratio']:.0%})")
        c4.metric("Padronização Pós-Split", scaler_type.upper())
        st.caption(
            "Os arquivos padronizados `train_80_standardized.csv` e `test_20_standardized.csv` "
            "são salvos automaticamente em `code/mlp/data/` sem vazamento de dados (fit apenas no treino)."
        )

    # ====================================================================
    #  LAYOUT PRINCIPAL: GRAFO E CURVAS EM TEMPO REAL
    # ====================================================================
    col_graph, col_charts = st.columns([3.2, 1.3])
    with col_graph:
        graph_box = st.empty()
    with col_charts:
        info_box = st.empty()
        loss_box = st.empty()
        acc_box = st.empty()

    # Renderizar estado atual
    curr_ep = st.session_state.history["epoch"][-1] if st.session_state.history else 0
    curr_loss = st.session_state.test_metrics.get("loss", None)
    curr_acc = st.session_state.test_metrics.get("accuracy", None)
    fig_net = draw_network(
        mlp,
        epoch=curr_ep,
        loss_val=curr_loss,
        acc_val=curr_acc,
        show_edge_weights=show_edge_weights,
        top_k_labels_per_layer=top_k_labels,
    )
    graph_box.pyplot(fig_net)
    plt.close(fig_net)

    if st.session_state.history:
        h = st.session_state.history
        fl = draw_loss(h["train_loss"], h["test_loss"], h["epoch"])
        loss_box.pyplot(fl)
        plt.close(fl)
        fa = draw_accuracy(h["train_acc"], h["test_acc"], h["epoch"])
        acc_box.pyplot(fa)
        plt.close(fa)

    # ====================================================================
    #  DINÂMICA DE TREINAMENTO (PONTO 4)
    # ====================================================================
    st.markdown("---")
    st.subheader("🏋️ Dinâmica de Treinamento (Forward Pass + Backpropagation com Gradiente Descendente)")

    if st.button("▶️ Executar Treinamento em Tempo Real", type="primary"):
        rng = np.random.default_rng(seed)
        history = {
            "epoch": [],
            "train_loss": [],
            "test_loss": [],
            "train_acc": [],
            "test_acc": [],
        }
        snapshots = {0: get_weights_dataframe(mlp)}
        prog = st.progress(0)
        stat = st.empty()
        t0 = time.time()

        for ep in range(1, n_epochs + 1):
            curr_lr = lr / (1.0 + lr_decay * (ep - 1))
            tr_loss = train_epoch(
                mlp, X_train, y_train, lr=curr_lr, momentum=momentum, l2_lambda=l2_lambda, rng=rng
            )

            if ep % upd_every == 0 or ep == 1 or ep == n_epochs:
                tr_eval = evaluate(mlp, X_train, y_train)
                te_eval = evaluate(mlp, X_test, y_test)

                history["epoch"].append(ep)
                history["train_loss"].append(tr_loss)
                history["test_loss"].append(te_eval["loss"])
                history["train_acc"].append(tr_eval["accuracy"])
                history["test_acc"].append(te_eval["accuracy"])
                snapshots[ep] = get_weights_dataframe(mlp)

                fn = draw_network(
                    mlp,
                    epoch=ep,
                    loss_val=te_eval["loss"],
                    acc_val=te_eval["accuracy"],
                    show_edge_weights=show_edge_weights,
                    top_k_labels_per_layer=top_k_labels,
                )
                graph_box.pyplot(fn)
                plt.close(fn)

                fl = draw_loss(history["train_loss"], history["test_loss"], history["epoch"])
                loss_box.pyplot(fl)
                plt.close(fl)

                fa = draw_accuracy(history["train_acc"], history["test_acc"], history["epoch"])
                acc_box.pyplot(fa)
                plt.close(fa)

                with info_box.container():
                    m1, m2 = st.columns(2)
                    m1.metric("Loss Teste", f"{te_eval['loss']:.4f}", delta=f"Treino: {tr_loss:.4f}")
                    m2.metric("Acurácia Teste", f"{te_eval['accuracy']:.2%}", delta=f"Treino: {tr_eval['accuracy']:.1%}")

            prog.progress(ep / n_epochs)
            stat.text(
                f"Época {ep}/{n_epochs}  |  LR atual: {curr_lr:.5f}  |  Loss Treino: {tr_loss:.5f}  |  Tempo: {time.time() - t0:.1f}s"
            )

        figs_dir = os.path.join(os.path.dirname(__file__), "figs")
        os.makedirs(figs_dir, exist_ok=True)
        save_graph_image(
            mlp,
            os.path.join(figs_dir, "grafo_depois.png"),
            epoch=n_epochs,
            loss_val=history["test_loss"][-1],
            acc_val=history["test_acc"][-1],
            show_edge_weights=show_edge_weights,
            top_k_labels_per_layer=top_k_labels,
        )

        st.session_state.trained = True
        st.session_state.history = history
        st.session_state.train_metrics = evaluate(mlp, X_train, y_train)
        st.session_state.test_metrics = evaluate(mlp, X_test, y_test)
        st.session_state.epoch_snapshots = snapshots
        st.success("✅ Treinamento concluído! Pesos e figuras atualizados em code/mlp/figs/grafo_depois.png.")

    # ====================================================================
    #  VISUALIZAÇÃO E INSPEÇÃO DE PESOS SINÁPTICOS (PONTO 5)
    # ====================================================================
    st.markdown("---")
    st.subheader("🔬 Inspeção Visual e Numérica dos Pesos Sinápticos (w_ij e Δw_ij)")

    tab_heat, tab_delta, tab_table = st.tabs(
        [
            "🌡️ Mapa de Calor dos Pesos (w_ij)",
            "📈 Mapa de Calor das Atualizações (Δw_ij na Época)",
            "📋 Tabela Numérica de Conexões, Pesos e Gradientes",
        ]
    )

    with tab_heat:
        fig_hm = draw_weights_heatmap(mlp, mode="weight", epoch=curr_ep)
        st.pyplot(fig_hm)
        plt.close(fig_hm)

    with tab_delta:
        fig_dm = draw_weights_heatmap(mlp, mode="delta_weight", epoch=curr_ep)
        st.pyplot(fig_dm)
        plt.close(fig_dm)

    with tab_table:
        avail_epochs = sorted(st.session_state.epoch_snapshots.keys())
        sel_ep = st.selectbox(
            "Selecionar Época para Inspeção Numérica dos Pesos Sinápticos",
            options=avail_epochs,
            index=len(avail_epochs) - 1,
        )
        df_w = st.session_state.epoch_snapshots[sel_ep]
        st.dataframe(df_w, use_container_width=True, height=320)

    # ====================================================================
    #  MÉTRICAS DE AVALIAÇÃO NO CONJUNTO DE TESTE (20%)
    # ====================================================================
    if st.session_state.test_metrics:
        st.markdown("---")
        st.subheader("📊 Desempenho no Conjunto de Teste (20%)")
        m = st.session_state.test_metrics
        cols_m = st.columns(6)
        cols_m[0].metric("Acurácia", f"{m['accuracy']:.2%}")
        cols_m[1].metric("Loss (BCE)", f"{m['loss']:.4f}")
        cols_m[2].metric("Precisão", f"{m['precision']:.2%}")
        cols_m[3].metric("Recall (Sensibilidade)", f"{m['recall']:.2%}")
        cols_m[4].metric("F1-Score", f"{m['f1']:.2%}")
        cols_m[5].metric("AUC-ROC", f"{m['auc_roc']:.4f}")

        conf_df = pd.DataFrame(
            [[m["tn"], m["fp"]], [m["fn"], m["tp"]]],
            index=["Real: Saudável (0)", "Real: Doença Cardíaca (1)"],
            columns=["Predito: Saudável (0)", "Predito: Doença Cardíaca (1)"],
        )
        st.dataframe(conf_df, use_container_width=True)

    # ====================================================================
    #  ANIMAÇÃO DE INFERÊNCIA (FORWARD + BACKWARD PASS)
    # ====================================================================
    st.markdown("---")
    st.subheader("🔍 Simulação Animada de Propagação Camada a Camada")
    si = st.selectbox(
        "Amostra do conjunto de teste (20%)",
        range(len(X_test)),
        format_func=lambda i: f"Paciente #{i}  |  Diagnóstico Real: {'Doença Cardíaca (1)' if y_test[i] == 1 else 'Saudável (0)'}",
    )
    show_bwd = st.checkbox("Animar também Retropropagação do Gradiente (Backward Pass)", value=True)

    if st.button("🤖 Executar Propagação Passo a Passo"):
        xs = X_test[si]
        tgt = y_test[si]
        fwd_all = all_forward_edges(mlp)
        anim = st.empty()
        msg = st.empty()

        out = mlp.forward(xs)
        for li in range(mlp.num_layers - 1):
            le = layer_edges(mlp, li)
            nh = {u: "#76FF03" for u, v in le}
            for j in range(mlp.layer_sizes[li + 1]):
                nh[f"L{li+1}_N{j}"] = "#76FF03"
            fig = draw_network(
                mlp,
                fwd_edges=le,
                node_hl=nh,
                show_edge_weights=show_edge_weights,
                top_k_labels_per_layer=top_k_labels,
            )
            anim.pyplot(fig)
            plt.close(fig)
            msg.info(f"➡️ **Forward Pass**: Propagando sinais da Camada L{li} → Camada L{li+1}")
            time.sleep(0.7)

        if show_bwd:
            for li in range(mlp.num_layers - 2, -1, -1):
                le = layer_edges(mlp, li)
                nh = {v: "#FF6D00" for u, v in le}
                fig = draw_network(
                    mlp,
                    fwd_edges=fwd_all,
                    bwd_edges=le,
                    node_hl=nh,
                    show_edge_weights=show_edge_weights,
                    top_k_labels_per_layer=top_k_labels,
                )
                anim.pyplot(fig)
                plt.close(fig)
                msg.warning(f"⬅️ **Backward Pass**: Retropropagando gradientes ∂L/∂w da Camada L{li+1} ← Camada L{li}")
                time.sleep(0.7)

        pred_cls = 1 if out >= 0.5 else 0
        real_cls = int(tgt)
        conf = out if pred_cls == 1 else 1.0 - out
        if pred_cls == real_cls:
            msg.success(f"✅ Predição: **{pred_cls}** (prob={out:.4f}, confiança={conf:.2%}) | Real: **{real_cls}**")
        else:
            msg.error(f"❌ Predição: **{pred_cls}** (prob={out:.4f}, confiança={conf:.2%}) | Real: **{real_cls}**")


if __name__ == "__main__":
    main()
