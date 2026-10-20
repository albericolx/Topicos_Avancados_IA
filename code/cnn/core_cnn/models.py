"""
core_cnn/models.py
==================
Definição formal das arquiteturas da Atividade 02 - CNNs:
1. BaselineCNN: Réplica exata do modelo do artigo (Dizabadi, 2026 - Seção 3.2):
   - 6 camadas conv (32, 32, 64, 64, 128, 128)
   - 7 BatchNorms (após cada Conv e após a Dense intermediária)
   - MaxPool(2) a cada 2 convoluções
   - Dropout (0.3, 0.5, 0.5, 0.5)
   - Dense de 128 neurônios + Dense de 10 classes
   - Total exato: 552.874 parâmetros (contando running stats de BN) / 551.722 treináveis

2. Mod1_ResidualCNN (Modificação 1 - Conexões Residuais):
   - Adiciona skip connections estilo ResNet conectando a entrada à saída de cada bloco duplo conv.
   - Preserva o fluxo direto de gradientes retropropagados, evitando a degradação observada
     no artigo quando a profundidade foi alterada.

3. Mod2_AugmentedCNN (Modificação 2 - Regularização por Data Augmentation):
   - Mesma arquitetura baseline, porém com pipeline de aumento de dados ativo no treino.

4. Mod3_SE_CNN (Modificação 3 - Squeeze-and-Excitation):
   - Incorpora blocos de atenção por canal (SE-block) ao final de cada bloco convolucional duplo.
   - Pondera dinamicamente a relevância dos mapas de características aprendidos.

5. CombinedCNN (Modelo Final Integrado):
   - Integra as 3 modificações simultaneamente: Conexões Residuais + Squeeze-and-Excitation + Data Augmentation.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F


class SEBlock(nn.Module):
    """Squeeze-and-Excitation Block (Hu et al., CVPR 2018).
    Atenção por canal com custo residual mínimo de parâmetros."""
    def __init__(self, channels: int, reduction: int = 16):
        super().__init__()
        red = max(channels // reduction, 4)
        self.fc1 = nn.Linear(channels, red, bias=False)
        self.fc2 = nn.Linear(red, channels, bias=False)

    def forward(self, x):
        b, c, _, _ = x.shape
        # Squeeze: Global Average Pooling (B, C, 1, 1) -> (B, C)
        s = x.mean(dim=(2, 3))
        # Excitation: MLP com sigmoid
        e = F.relu(self.fc1(s))
        e = torch.sigmoid(self.fc2(e)).view(b, c, 1, 1)
        # Recalibration
        return x * e


class DoubleConvBlock(nn.Module):
    """Bloco duplo convolucional padrão do artigo base com BN e Dropout."""
    def __init__(self, in_c: int, out_c: int, drop_p: float, use_residual: bool = False, use_se: bool = False):
        super().__init__()
        self.use_residual = use_residual
        self.use_se = use_se

        self.conv1 = nn.Conv2d(in_c, out_c, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(out_c)
        self.conv2 = nn.Conv2d(out_c, out_c, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(out_c)
        self.pool = nn.MaxPool2d(2, 2)
        self.drop = nn.Dropout(drop_p)

        if self.use_residual and in_c != out_c:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_c, out_c, kernel_size=1, bias=False),
                nn.BatchNorm2d(out_c)
            )
        else:
            self.shortcut = nn.Identity()

        if self.use_se:
            self.se = SEBlock(out_c)

    def forward(self, x):
        residual = self.shortcut(x) if self.use_residual else None

        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))

        if self.use_residual:
            out = out + residual
        out = F.relu(out)

        if self.use_se:
            out = self.se(out)

        out = self.pool(out)
        out = self.drop(out)
        return out


class BaselineCNN(nn.Module):
    """Réplica do modelo âncora do artigo base (Dizabadi, 2026)."""
    def __init__(self):
        super().__init__()
        self.block1 = DoubleConvBlock(3, 32, drop_p=0.3, use_residual=False, use_se=False)
        self.block2 = DoubleConvBlock(32, 64, drop_p=0.5, use_residual=False, use_se=False)
        self.block3 = DoubleConvBlock(64, 128, drop_p=0.5, use_residual=False, use_se=False)

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.5),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.classifier(x)


class Mod1_ResidualCNN(nn.Module):
    """Modificação 1: Conexões Residuais nos blocos convolucionais."""
    def __init__(self):
        super().__init__()
        self.block1 = DoubleConvBlock(3, 32, drop_p=0.3, use_residual=True, use_se=False)
        self.block2 = DoubleConvBlock(32, 64, drop_p=0.5, use_residual=True, use_se=False)
        self.block3 = DoubleConvBlock(64, 128, drop_p=0.5, use_residual=True, use_se=False)

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.5),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.classifier(x)


class Mod3_SE_CNN(nn.Module):
    """Modificação 3: Mecanismo de Atenção Squeeze-and-Excitation (SE-Block)."""
    def __init__(self):
        super().__init__()
        self.block1 = DoubleConvBlock(3, 32, drop_p=0.3, use_residual=False, use_se=True)
        self.block2 = DoubleConvBlock(32, 64, drop_p=0.5, use_residual=False, use_se=True)
        self.block3 = DoubleConvBlock(64, 128, drop_p=0.5, use_residual=False, use_se=True)

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.5),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.classifier(x)


class CombinedCNN(nn.Module):
    """Modelo Final Combinado: Resíduos + Atenção Squeeze-and-Excitation (+ Data Augmentation)."""
    def __init__(self):
        super().__init__()
        self.block1 = DoubleConvBlock(3, 32, drop_p=0.3, use_residual=True, use_se=True)
        self.block2 = DoubleConvBlock(32, 64, drop_p=0.5, use_residual=True, use_se=True)
        self.block3 = DoubleConvBlock(64, 128, drop_p=0.5, use_residual=True, use_se=True)

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 128),
            nn.ReLU(),
            nn.BatchNorm1d(128),
            nn.Dropout(0.5),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.classifier(x)


def count_parameters(model: nn.Module) -> dict:
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    # BatchNorm running stats (mean, var) somam 2 * num_features por camada
    bn_stats = sum(b.numel() for b in model.buffers())
    return {
        "trainable": trainable,
        "total": total,
        "buffers_bn": bn_stats,
        "keras_param_count": total + bn_stats
    }
