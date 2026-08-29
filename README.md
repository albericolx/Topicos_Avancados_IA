# Workspace: Tópicos Avançados de IA (UFRPE 2026.2)
> Ambiente unificado de desenvolvimento de modelos neurais, experimentação empírica e confecção de artigo científico em LaTeX.

Este workspace segue a filosofia de **Workspace OS** inspirada em [`lsfcin/workspace`](https://github.com/lsfcin/workspace), integrando na raiz o desenvolvimento prático de redes neurais e a confecção do artigo científico no padrão **Springer LNCS** (*Lecture Notes in Computer Science*), com suporte a múltiplos agentes de IA (**harness principal e de backup**), integração contínua com o **Overleaf** e governança por **GitFlow**.

---

## Estrutura do Workspace

```text
Topicos Avancados de IA/
├── AGENTS.md                 # Normas canônicas para agentes de IA
├── README.md                 # Visão geral e guia rápido do workspace
├── ROADMAP.md                # Cronograma de entregas e fases dos experimentos
├── ISSUES.md                 # Registro de pendências e débitos técnicos
├── .gitignore                # Regras de exclusão para Git (LaTeX, PyTorch, Python, etc.)
│
├── code/                     # Modelos de IA e códigos experimentais
│   ├── CONTEXT.md            # Mapa e contexto da pasta code/
│   ├── SPECS-git.md          # Especificação detalhada do GitFlow
│   └── src/                  # Arquiteturas neurais, grafos explícitos e treinamento
│
├── papers/                   # Produção acadêmica e artigo científico
│   ├── CONTEXT.md            # Mapa e contexto da pasta papers/
│   ├── SPECS.md              # Normas de formatação Springer LNCS
│   └── artigo-final/         # Projeto LaTeX sincronizado diretamente com o Overleaf
│       ├── main.tex          # Arquivo mestre (Investigação e Implementação de Modelos Neurais)
│       ├── llncs.cls         # Classe Springer LNCS
│       ├── splncs04.bst      # Estilo bibliográfico Springer
│       ├── references.bib    # Banco de referências bibliográficas
│       ├── sections/         # Seções modulares (01_introducao a 05_conclusao)
│       └── figures/          # Gráficos de perda, acurácia e topologia de rede
│
└── core/                     # Ferramentas auxiliares e automação
    ├── CONTEXT.md            # Contexto dos utilitários
    └── tools/                # Scripts de suporte
        ├── academic_search.py # Busca papers no arXiv / Semantic Scholar e gera BibTeX
        ├── compile_paper.py   # Compilador rápido de LaTeX para PDF local
        └── overleaf_sync.py   # Assistente de sincronização com Overleaf
```

---

## Guia Rápido de Uso

### 1. Harness Principal e Backup (Quando a cota acabar)
* **Harness Principal**: Antigravity (Gemini).
* **Harness de Backup**: VS Code (com GitHub Copilot / Claude Code / OpenCode).
* **Como trocar**: Abra esta pasta no VS Code e a IA continuará a tarefa lendo [`AGENTS.md`](AGENTS.md) e [`ISSUES.md`](ISSUES.md).

### 2. Sincronizar com o Overleaf
O projeto em `papers/artigo-final` está vinculado diretamente ao repositório do Overleaf:
* Para enviar alterações locais para o Overleaf:
  ```bash
  cd "papers/artigo-final"
  git push origin main
  ```
* Para puxar alterações feitas no Overleaf para o seu computador:
  ```bash
  cd "papers/artigo-final"
  git pull origin main
  ```
* Ou gere o pacote `.zip`: `py core/tools/overleaf_sync.py --zip`.

### 3. Compilar o Artigo LaTeX Localmente
```bash
py core/tools/compile_paper.py
```
O PDF gerado ficará disponível em `papers/artigo-final/main.pdf`.

### 4. Buscar Artigos Científicos para a Disciplina
```bash
py core/tools/academic_search.py --query "explicit computation graph neural networks" --limit 5
```
