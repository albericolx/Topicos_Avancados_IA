import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

fig = plt.figure(figsize=(16, 11), dpi=220)
fig.patch.set_facecolor("#FAFAFC")

# Create 5 subplots with nice spacing
# Layout:
# Top row: (a) Baseline CNN Architecture (full flow)
# Middle row: (b) Mod 1: Residual Block | (c) Mod 2: Data Augmentation Pipeline
# Bottom row: (d) Mod 3: Squeeze-and-Excitation (SE-Block) | (e) Modelo Combinado Integrado

gs = fig.add_gridspec(3, 2, height_ratios=[1.2, 1.0, 1.1], hspace=0.35, wspace=0.25)

# ==============================================================================
# Subplot (a): Baseline CNN
# ==============================================================================
ax0 = fig.add_subplot(gs[0, :])
ax0.set_facecolor("#FFFFFF")
ax0.set_xlim(0, 16)
ax0.set_ylim(0, 4)
ax0.axis("off")

ax0.text(0.2, 3.5, "(a) Arquitetura Baseline de Referência (Dizabadi, 2026 — 552.874 parâmetros)",
         fontsize=12, fontweight="bold", color="#1A237E")

# Pipeline boxes
stages = [
    ("Entrada\nCIFAR-10\n(3×32×32)", "#E3F2FD", "#1565C0", 0.3, 1.0, 1.6, 2.0),
    ("Bloco 1 (32 canais)\n2x [Conv 3×3 + BN + ReLU]\n+ MaxPool (2×2)\n+ Dropout (0.30)", "#E8F5E9", "#2E7D32", 2.3, 0.8, 3.0, 2.4),
    ("Bloco 2 (64 canais)\n2x [Conv 3×3 + BN + ReLU]\n+ MaxPool (2×2)\n+ Dropout (0.50)", "#FFF3E0", "#E65100", 5.7, 0.8, 3.0, 2.4),
    ("Bloco 3 (128 canais)\n2x [Conv 3×3 + BN + ReLU]\n+ MaxPool (2×2)\n+ Dropout (0.50)", "#F3E5F5", "#6A1B9A", 9.1, 0.8, 3.0, 2.4),
    ("Classificador\nFlatten (2048)\nLinear (128) + BN\nDropout (0.50)\nLinear (10)", "#FCE4EC", "#AD1457", 12.5, 0.8, 2.2, 2.4),
    ("Predição\nSoftmax\n(10 classes)", "#EDE7F6", "#4527A0", 15.0, 1.0, 0.9, 2.0)
]

for label, bg, border, x, y, w, h in stages:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.15",
                                  facecolor=bg, edgecolor=border, linewidth=1.8)
    ax0.add_patch(rect)
    ax0.text(x + w/2, y + h/2, label, ha="center", va="center", fontsize=8.5, fontweight="medium", color="#212121")

# Arrows
arrows = [(1.9, 2.0, 2.3, 2.0), (5.3, 2.0, 5.7, 2.0), (8.7, 2.0, 9.1, 2.0), (12.1, 2.0, 12.5, 2.0), (14.7, 2.0, 15.0, 2.0)]
for x1, y1, x2, y2 in arrows:
    ax0.annotate("", xy=(x2, y2), xytext=(x1, y1),
                 arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=2, mutation_scale=14))

# ==============================================================================
# Subplot (b): Mod 1: Conexões Residuais
# ==============================================================================
ax1 = fig.add_subplot(gs[1, 0])
ax1.set_facecolor("#FFFFFF")
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 5)
ax1.axis("off")

ax1.text(0.1, 4.6, "(b) Modificação 1: Conexões Residuais (Skip Connections)",
         fontsize=10.5, fontweight="bold", color="#1565C0")

# Input
b_in = patches.FancyBboxPatch((0.3, 1.8), 1.4, 1.2, boxstyle="round,pad=0.1,rounding_size=0.1",
                              facecolor="#E3F2FD", edgecolor="#1565C0", lw=1.5)
ax1.add_patch(b_in)
ax1.text(1.0, 2.4, "Entrada x\n(C canais)", ha="center", va="center", fontsize=8, fontweight="bold")

# Main Branch
b_conv1 = patches.FancyBboxPatch((2.2, 2.8), 2.2, 1.2, boxstyle="round,pad=0.1,rounding_size=0.1",
                                facecolor="#E8F5E9", edgecolor="#2E7D32", lw=1.5)
ax1.add_patch(b_conv1)
ax1.text(3.3, 3.4, "Conv 3×3 + BN\n+ ReLU", ha="center", va="center", fontsize=7.5)

b_conv2 = patches.FancyBboxPatch((4.8, 2.8), 2.2, 1.2, boxstyle="round,pad=0.1,rounding_size=0.1",
                                facecolor="#E8F5E9", edgecolor="#2E7D32", lw=1.5)
ax1.add_patch(b_conv2)
ax1.text(5.9, 3.4, "Conv 3×3 + BN\nF(x)", ha="center", va="center", fontsize=7.5)

# Skip branch
b_skip = patches.FancyBboxPatch((3.2, 0.4), 2.8, 1.1, boxstyle="round,pad=0.1,rounding_size=0.1",
                               facecolor="#FFF9C4", edgecolor="#F57F17", lw=1.5, linestyle="--")
ax1.add_patch(b_skip)
ax1.text(4.6, 0.95, "Atalho: Identidade x ou\nProj. Conv 1×1 + BN (P(x))", ha="center", va="center", fontsize=7.5)

# Sum circle
sum_circ = patches.Circle((7.6, 2.4), 0.35, facecolor="#FFE0B2", edgecolor="#E65100", lw=1.8)
ax1.add_patch(sum_circ)
ax1.text(7.6, 2.4, "+", ha="center", va="center", fontsize=13, fontweight="bold", color="#BF360C")

# Out box
b_out = patches.FancyBboxPatch((8.3, 1.8), 1.5, 1.2, boxstyle="round,pad=0.1,rounding_size=0.1",
                              facecolor="#E1BEE7", edgecolor="#6A1B9A", lw=1.5)
ax1.add_patch(b_out)
ax1.text(9.05, 2.4, "ReLU +\nMaxPool +\nDropout", ha="center", va="center", fontsize=7.5)

# Connecting lines
ax1.annotate("", xy=(2.2, 3.4), xytext=(1.7, 2.4), arrowprops=dict(arrowstyle="-|>", color="#2E7D32", lw=1.5))
ax1.annotate("", xy=(4.8, 3.4), xytext=(4.4, 3.4), arrowprops=dict(arrowstyle="-|>", color="#2E7D32", lw=1.5))
ax1.annotate("", xy=(7.25, 2.6), xytext=(7.0, 3.4), arrowprops=dict(arrowstyle="-|>", color="#2E7D32", lw=1.5))
# skip connection line
ax1.annotate("", xy=(3.2, 0.95), xytext=(1.7, 2.4), arrowprops=dict(arrowstyle="-|>", color="#F57F17", lw=1.5, ls="--"))
ax1.annotate("", xy=(7.3, 2.2), xytext=(6.0, 0.95), arrowprops=dict(arrowstyle="-|>", color="#F57F17", lw=1.5, ls="--"))
ax1.annotate("", xy=(8.3, 2.4), xytext=(7.95, 2.4), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.5))

# ==============================================================================
# Subplot (c): Mod 2: Data Augmentation
# ==============================================================================
ax2 = fig.add_subplot(gs[1, 1])
ax2.set_facecolor("#FFFFFF")
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 5)
ax2.axis("off")

ax2.text(0.1, 4.6, "(c) Modificação 2: Protocolo de Data Augmentation Estocástico",
         fontsize=10.5, fontweight="bold", color="#2E7D32")

aug_steps = [
    ("Imagem Original\n(32×32)", "#E3F2FD", "#1565C0", 0.2, 1.8, 1.8, 1.6),
    ("Padding Reflexivo\n(+4 bordas → 40×40)", "#FFF3E0", "#E65100", 2.6, 1.8, 2.2, 1.6),
    ("Random Crop\n(Recorte 32×32)", "#E8F5E9", "#2E7D32", 5.2, 1.8, 2.0, 1.6),
    ("Random Horizontal\nFlip (p=0.50)", "#F3E5F5", "#6A1B9A", 7.6, 1.8, 2.2, 1.6),
]

for label, bg, border, x, y, w, h in aug_steps:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.1",
                                  facecolor=bg, edgecolor=border, lw=1.5)
    ax2.add_patch(rect)
    ax2.text(x + w/2, y + h/2, label, ha="center", va="center", fontsize=7.5, fontweight="medium")

# Flow arrows
ax2.annotate("", xy=(2.6, 2.6), xytext=(2.0, 2.6), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.8))
ax2.annotate("", xy=(5.2, 2.6), xytext=(4.8, 2.6), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.8))
ax2.annotate("", xy=(7.6, 2.6), xytext=(7.2, 2.6), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.8))

ax2.text(5.0, 0.6, "Efeito: Cria variações inéditas a cada época impedindo a memorização rasa\ne forçando a rede a aprender invariância de posição e espelhamento.",
         ha="center", va="center", fontsize=7.5, style="italic", color="#37474F",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#F5F5F5", edgecolor="#BDBDBD", lw=0.8))

# ==============================================================================
# Subplot (d): Mod 3: Squeeze-and-Excitation
# ==============================================================================
ax3 = fig.add_subplot(gs[2, 0])
ax3.set_facecolor("#FFFFFF")
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 5)
ax3.axis("off")

ax3.text(0.1, 4.6, "(d) Modificação 3: Mecanismo de Atenção Squeeze-and-Excitation (SE)",
         fontsize=10.5, fontweight="bold", color="#6A1B9A")

se_blocks = [
    ("Tensor U\n(C×H×W)", "#E3F2FD", "#1565C0", 0.2, 1.8, 1.3, 1.5),
    ("Squeeze:\nGlobal Avg Pool\nz ∈ ℝ^C", "#E8F5E9", "#2E7D32", 1.8, 1.8, 2.0, 1.5),
    ("Excitation:\nFC(C/8) + ReLU\nFC(C) + Sigmoid\ns ∈ [0,1]^C", "#FFF3E0", "#E65100", 4.1, 1.8, 2.4, 1.5),
    ("Scale:\nMultiplicação\nCanal-a-Canal\n(U · s)", "#FCE4EC", "#C2185B", 6.8, 1.8, 1.8, 1.5),
    ("Tensor Saída\nRecalibrado\n(C×H×W)", "#EDE7F6", "#4527A0", 8.8, 1.8, 1.1, 1.5)
]

for label, bg, border, x, y, w, h in se_blocks:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.1",
                                  facecolor=bg, edgecolor=border, lw=1.5)
    ax3.add_patch(rect)
    ax3.text(x + w/2, y + h/2, label, ha="center", va="center", fontsize=7.2, fontweight="medium")

# Arrows
ax3.annotate("", xy=(1.8, 2.55), xytext=(1.5, 2.55), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.6))
ax3.annotate("", xy=(4.1, 2.55), xytext=(3.8, 2.55), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.6))
ax3.annotate("", xy=(6.8, 2.55), xytext=(6.5, 2.55), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.6))
ax3.annotate("", xy=(8.8, 2.55), xytext=(8.6, 2.55), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.6))

# Skip from U to Scale
ax3.annotate("", xy=(7.7, 1.8), xytext=(0.85, 1.8),
             arrowprops=dict(arrowstyle="-|>", color="#1565C0", lw=1.4, connectionstyle="arc3,rad=-0.35"))
ax3.text(4.2, 0.6, "Atalho de Conteúdo: canal original U multiplicado pela saliência s",
         ha="center", va="center", fontsize=7, color="#1565C0")

# ==============================================================================
# Subplot (e): Modelo Combinado
# ==============================================================================
ax4 = fig.add_subplot(gs[2, 1])
ax4.set_facecolor("#FFFFFF")
ax4.set_xlim(0, 10)
ax4.set_ylim(0, 5)
ax4.axis("off")

ax4.text(0.1, 4.6, "(e) Modelo Combinado Integrado (Resíduos + SE + Data Augmentation)",
         fontsize=10.5, fontweight="bold", color="#C2185B")

comb_steps = [
    ("Entrada\nData Augmentation\n(Crop + Flip)", "#E8F5E9", "#2E7D32", 0.3, 1.8, 2.0, 1.6),
    ("3x Super-Blocos\n[Resíduos Aditivos]\n+ [Módulo SE-Attention]\n+ MaxPool + Dropout", "#FFF3E0", "#E65100", 2.8, 1.6, 3.8, 2.0),
    ("Classificador\nLinear 128 (BN)\nDropout (0.50)\nLinear (10)", "#FCE4EC", "#AD1457", 7.1, 1.8, 2.6, 1.6)
]

for label, bg, border, x, y, w, h in comb_steps:
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.1",
                                  facecolor=bg, edgecolor=border, lw=1.6)
    ax4.add_patch(rect)
    ax4.text(x + w/2, y + h/2, label, ha="center", va="center", fontsize=7.5, fontweight="medium")

ax4.annotate("", xy=(2.8, 2.6), xytext=(2.3, 2.6), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.8))
ax4.annotate("", xy=(7.1, 2.6), xytext=(6.6, 2.6), arrowprops=dict(arrowstyle="-|>", color="#37474F", lw=1.8))

ax4.text(5.0, 0.6, "Síntese Sinérgica: Fluxo de gradiente protegido (Resíduos) +\nRecalibração dinâmica (SE) + Suporte amostral infinito (Augmentation).",
         ha="center", va="center", fontsize=7.5, style="italic", color="#37474F",
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#F5F5F5", edgecolor="#BDBDBD", lw=0.8))

# Save figure in all target locations
out_paths = [
    Path(r"C:\Users\Windows 10\OneDrive\Documentos\UFRPE\2026.2\Topicos Avancados IA\article\figures\diagramas_arquiteturas.png"),
    Path(r"C:\Users\Windows 10\OneDrive\Documentos\UFRPE\2026.2\Topicos Avancados IA\papers\artigo-final\figures\diagramas_arquiteturas.png"),
    Path(r"C:\Users\Windows 10\OneDrive\Documentos\UFRPE\2026.2\Topicos Avancados IA\code\cnn\figs\diagramas_arquiteturas.png")
]

for p in out_paths:
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(p, dpi=220, bbox_inches="tight")
    print(f"Diagrama salvo em: {p}")

plt.close(fig)
print("Geracao de diagramas finalizada com sucesso!")
