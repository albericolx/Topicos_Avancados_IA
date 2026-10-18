# Especificação de Habilidades (`core/skills/SPECS.md`)
> Contrato para criação, manutenção e execução de skills científicas no workspace.

## 1. Estrutura Obrigatória
Toda skill reside em `core/skills/<nome>.md` (e possui espelho em `.agents/skills/<nome>/SKILL.md`), iniciando com frontmatter YAML:

```yaml
---
name: <slug-da-skill>
description: <descrição concisa de quando e como ativar a skill>
---
```

## 2. Disciplina de Execução Científica
1. **Evidência em Disco**: Toda execução de skill de pesquisa deve produzir ou atualizar artefatos versionados (`refs/REFS.md`, `refs/<key>.yaml`, `article/sections/*.tex`), nunca apenas texto volátil no chat.
2. **Zero Alucinação Bibliográfica**: Nenhuma citação `\cite{key}` pode ser inserida no LaTeX sem antes passar pelo pipeline `core/tools/academic_search.py` e possuir ficha validada em `refs/<key>.yaml`.
3. **Leitura Zero-Token**: Antes de injetar PDFs longos no contexto do modelo, execute `py core/tools/pdf_ocr_parser.py` para extrair o texto localmente em `refs/ocr/<key>.txt`.
