"""
core_mlp/graph.py
=================
Implementação do zero (from scratch) de uma Rede Neural Multicamadas (MLP)
representada explicitamente como um Grafo Direcionado (nx.DiGraph).

Correções e melhorias em relação à versão preliminar:
1. Bias corrigido em TODAS as camadas (incluindo L0_bias -> Camada Oculta 1).
2. Derivada analítica exata da perda Binary Cross-Entropy (BCE) com saída sigmoide:
   delta_out = (y_hat - y), eliminando a dupla multiplicação por sigmoid'(z) que
   causava desvanecimento prematuro de gradiente.
3. Suporte a Momentum (velocidade por aresta) e Regularização L2 (weight decay).
4. Rastreamento completo por aresta no nx.DiGraph: weight (w), prev_weight,
   delta_weight (Δw) e gradient (∂L/∂w), com referências diretas aos dicionários do grafo
   para execução rápida no Streamlit.
"""
import numpy as np
import networkx as nx


class MLPGraph:
    """
    Rede Neural Multicamadas (MLP) modelada como um grafo direcionado (nx.DiGraph).

    Parameters
    ----------
    layer_sizes : list[int]
        Número de neurônios em cada camada. Ex: [13, 16, 8, 1]
    activation : str
        Função de ativação das camadas ocultas:
        'relu', 'leaky_relu', 'tanh', 'sigmoid', 'elu', 'selu', 'relu6'
    loss_type : str
        'bce' (Binary Cross-Entropy - derivada exata) ou 'mse' (Erro Quadrático Médio)
    seed : int
        Semente pseudoaleatória para reprodutibilidade.
    """

    def __init__(self, layer_sizes, activation="relu", loss_type="bce", seed=42):
        self.seed = int(seed)
        self.rng = np.random.default_rng(self.seed)
        np.random.seed(self.seed)
        self.layer_sizes = [int(s) for s in layer_sizes]
        self.num_layers = len(self.layer_sizes)
        self.activation = activation
        self.loss_type = loss_type
        self.graph = nx.DiGraph()
        self._build()

    def _build(self):
        """
        Constrói os nós (neurônios + nós de bias para camadas 0..L-2) e arestas sinápticas
        ponderadas com inicialização He (para família ReLU/ELU) ou Xavier/Glorot (para Tanh/Sigmoid).
        """
        self.graph.clear()
        L = self.layer_sizes

        # 1. Criar nós de neurônios e nós de bias (camadas 0 até num_layers - 2 fornecem bias para a camada seguinte)
        for li in range(self.num_layers):
            for ni in range(L[li]):
                nid = f"L{li}_N{ni}"
                self.graph.add_node(
                    nid,
                    layer=li,
                    neuron=ni,
                    is_bias=False,
                    value=0.0,
                    z=0.0,
                    delta=0.0,
                )
            if li < self.num_layers - 1:
                bid = f"L{li}_bias"
                self.graph.add_node(
                    bid,
                    layer=li,
                    neuron=-1,
                    is_bias=True,
                    value=1.0,
                    z=1.0,
                    delta=0.0,
                )

        # 2. Criar arestas direcionadas entre camadas consecutivas (incluindo o nó de bias L{li}_bias)
        for li in range(self.num_layers - 1):
            srcs = [f"L{li}_N{i}" for i in range(L[li])] + [f"L{li}_bias"]
            dsts = [f"L{li+1}_N{j}" for j in range(L[li + 1])]
            fan_in = max(L[li], 1)
            fan_out = max(L[li + 1], 1)

            for s in srcs:
                is_bias_src = s.endswith("_bias")
                for d in dsts:
                    if is_bias_src:
                        w = 0.0
                    elif self.activation in ("relu", "leaky_relu", "relu6", "elu", "selu"):
                        w = float(self.rng.normal(0.0, np.sqrt(2.0 / fan_in)))
                    else:
                        w = float(self.rng.normal(0.0, np.sqrt(2.0 / (fan_in + fan_out))))

                    self.graph.add_edge(
                        s,
                        d,
                        layer=li,
                        is_bias=is_bias_src,
                        weight=w,
                        prev_weight=w,
                        delta_weight=0.0,
                        gradient=0.0,
                        velocity=0.0,
                    )

        # 3. Criar estruturas de acesso direto aos dicionários internos do nx.DiGraph
        G = self.graph
        self._input_nodes = [G.nodes[f"L0_N{i}"] for i in range(L[0])]
        self._output_node = G.nodes[f"L{self.num_layers - 1}_N0"]
        self._fwd_layers = []
        self._bwd_hidden = []

        for li in range(1, self.num_layers):
            src_names = [f"L{li-1}_N{i}" for i in range(L[li - 1])] + [f"L{li-1}_bias"]
            layer_spec = []
            for nj in range(L[li]):
                did = f"L{li}_N{nj}"
                dnode = G.nodes[did]
                in_links = [(G.nodes[s], G[s][did]) for s in src_names]
                layer_spec.append((dnode, in_links))
            self._fwd_layers.append((li == self.num_layers - 1, layer_spec))

        for li in range(self.num_layers - 2, 0, -1):
            hid_spec = []
            for nj in range(L[li]):
                nid = f"L{li}_N{nj}"
                nnode = G.nodes[nid]
                out_links = [(G[nid][dst], G.nodes[dst]) for dst in G.successors(nid)]
                hid_spec.append((nnode, out_links))
            self._bwd_hidden.append(hid_spec)

    @staticmethod
    def sigmoid(z):
        """Função logística sigmoide numericamente estável."""
        if z >= 0:
            ez = np.exp(-min(z, 500.0))
            return float(1.0 / (1.0 + ez))
        ez = np.exp(max(z, -500.0))
        return float(ez / (1.0 + ez))

    @staticmethod
    def sigmoid_deriv(a):
        """Derivada da sigmoide em função da ativação a = sigmoid(z)."""
        return float(a * (1.0 - a))

    @staticmethod
    def activate(z, activation):
        """Aplica a função de ativação não linear sobre a pré-ativação z."""
        if activation == "relu":
            return z if z > 0.0 else 0.0
        if activation == "leaky_relu":
            return z if z > 0.0 else 0.01 * z
        if activation == "relu6":
            return 6.0 if z > 6.0 else (z if z > 0.0 else 0.0)
        if activation == "elu":
            return z if z > 0.0 else float(np.expm1(max(z, -50.0)))
        if activation == "selu":
            scale, alpha = 1.0507009873554805, 1.6732632423543772
            return scale * (z if z > 0.0 else alpha * float(np.expm1(max(z, -50.0))))
        if activation == "tanh":
            return float(np.tanh(z))
        return MLPGraph.sigmoid(z)

    @staticmethod
    def activation_deriv(z, activation):
        """Derivada analítica f'(z) da função de ativação em relação a z."""
        if activation == "relu":
            return 1.0 if z > 0.0 else 0.0
        if activation == "leaky_relu":
            return 1.0 if z > 0.0 else 0.01
        if activation == "relu6":
            return 1.0 if (0.0 < z < 6.0) else 0.0
        if activation == "elu":
            return 1.0 if z > 0.0 else float(np.exp(max(z, -50.0)))
        if activation == "selu":
            scale, alpha = 1.0507009873554805, 1.6732632423543772
            return scale if z > 0.0 else float(scale * alpha * np.exp(max(z, -50.0)))
        if activation == "tanh":
            t = float(np.tanh(z))
            return 1.0 - t * t
        s = MLPGraph.sigmoid(z)
        return s * (1.0 - s)

    def forward(self, x):
        """
        Executa a propagação direta (Forward Pass) camada a camada pelo grafo.
        """
        for i, node_dict in enumerate(self._input_nodes):
            val = float(x[i])
            node_dict["value"] = val
            node_dict["z"] = val

        act = self.activation
        for is_out, layer_spec in self._fwd_layers:
            for dnode, in_links in layer_spec:
                z = 0.0
                for snode, edge in in_links:
                    z += edge["weight"] * snode["value"]
                dnode["z"] = z
                dnode["value"] = self.sigmoid(z) if is_out else self.activate(z, act)

        return self._output_node["value"]

    def backward(self, target, lr=0.01, momentum=0.0, l2_lambda=0.0):
        """
        Executa a retropropagação do erro (Backpropagation) pelo grafo direcionado
        e atualiza os pesos sinápticos via Gradiente Descendente.
        """
        y_hat = self._output_node["value"]
        y = float(target)

        # 1. Sinal de erro (delta) na camada de saída
        if self.loss_type == "mse":
            self._output_node["delta"] = (y_hat - y) * (y_hat * (1.0 - y_hat))
        else:
            # Derivada analítica exata da Binary Cross-Entropy com saída sigmoide: delta = y_hat - y
            self._output_node["delta"] = y_hat - y

        # 2. Retropropagação dos deltas para as camadas ocultas
        act = self.activation
        for hid_spec in self._bwd_hidden:
            for nnode, out_links in hid_spec:
                err_sum = 0.0
                for edge, dst_node in out_links:
                    err_sum += edge["weight"] * dst_node["delta"]
                nnode["delta"] = err_sum * self.activation_deriv(nnode["z"], act)

        # 3. Atualização dos pesos sinápticos e registro dos gradientes nas arestas do nx.DiGraph
        for _, layer_spec in self._fwd_layers:
            for dnode, in_links in layer_spec:
                delta_j = dnode["delta"]
                for snode, edge in in_links:
                    w_old = edge["weight"]
                    grad = snode["value"] * delta_j + (0.0 if edge["is_bias"] else l2_lambda * w_old)
                    vel = momentum * edge["velocity"] + grad
                    step = -lr * vel
                    w_new = w_old + step

                    edge["prev_weight"] = w_old
                    edge["weight"] = w_new
                    edge["delta_weight"] = step
                    edge["gradient"] = grad
                    edge["velocity"] = vel

    def snapshot_weights(self):
        """Retorna um dicionário {(u, v): weight} com o estado atual dos pesos."""
        return {(u, v): float(self.graph[u][v]["weight"]) for u, v in self.graph.edges()}

    def update_epoch_deltas(self, prev_snapshot):
        """Atualiza prev_weight e delta_weight em relação ao snapshot do início da época."""
        G = self.graph
        for (u, v), w_prev in prev_snapshot.items():
            if G.has_edge(u, v):
                w_curr = G[u][v]["weight"]
                G[u][v]["prev_weight"] = float(w_prev)
                G[u][v]["delta_weight"] = float(w_curr - w_prev)
