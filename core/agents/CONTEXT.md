# Perfis de Agentes Especialistas (`core/agents/`)
> Definições de papéis para atuação coordenada em pesquisa bibliográfica, escrita científica e revisão crítica.

<!-- routing:start -->
## Roteamento de Perfis

| Papel | Responsabilidade |
|---|---|
| `researcher` | Coleta de literatura via `academic_search.py`, extração zero-token via `pdf_ocr_parser.py` e preenchimento de `refs/*.yaml` |
| `writer` | Formulação metodológica e redação técnica em LaTeX (Springer LNCS) em `article/sections/` |
| `reviewer` | Auditoria cega de referências, validação de DOIs e revisão crítica do manuscrito |
<!-- routing:end -->
