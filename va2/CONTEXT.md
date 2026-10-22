# Contexto: VA2 - Atividades de Avaliação (`va2/`)
> Módulo autocontido da 2ª Verificação de Aprendizagem (VA2) da disciplina de Tópicos Avançados de IA (UFRPE 2026.2).

Esta pasta centraliza **todos** os artefatos, documentos de ideação, referências bibliográficas, fontes LaTeX e o PDF compilado do projeto **Sentinela Clandestino (Vigilante de Espelhos e APKs)**.

---

## Estrutura da Pasta

```text
va2/
├── brw.md                           # Folha de Brainwriting Híbrido (Ideação, crise, usuário e solução)
├── cmp.md                           # Folha de Competidores e Contribuição (Catálogo, matriz de 8 eixos e frase canônica)
├── PITCH.md                         # Guia de Defesa Oral sem a tela (Pitch de 2 minutos para checagem com o professor)
├── CONTEXT.md                       # Documentação canônica desta pasta
├── main.tex                         # Documento mestre LaTeX no padrão Springer LNCS
├── main.pdf                         # PDF compilado do artigo científico completo da VA2 (~396 KB)
├── compile.py                       # Script Python para compilação autônoma (py va2/compile.py)
├── references.bib                   # Base bibliográfica BibTeX com 14 referências auditadas
├── llncs.cls                        # Classe Springer LNCS
├── splncs04.bst                     # Estilo bibliográfico Springer LNCS
└── sections/                        # Seções modulares do artigo científico completo (Springer LNCS)
    ├── 01_introducao.tex            # Introdução com dados do BACEN, falha de abordagens sem IA e paradigma Waze
    ├── 02_trabalhos_relacionados.tex# Taxonomia, 3+3 mais próximos, matriz de 8 eixos e declaração canônica
    ├── 03_modelo_de_ameaca_e_formulacao.tex # Modelo de ameaça adversária (DGA, Pix, MAMF) e formulação matemática
    ├── 04_arquitetura_e_metodologia.tex # Arquitetura híbrida Fast-Path LAYA (<35ms) + Deep-Path SLM INT4 + MCP
    ├── 05_avaliacao_e_tradeoffs.tex # Protocolo experimental, decomposição de latência e trade-offs de hardware
    └── 06_conclusao.tex             # Síntese das contribuições, impacto socioeconômico e trabalhos futuros
```

---

## Componentes e Artefatos

1. **`brw.md` (Artefato Brainwriting Híbrido):**  
   Concepção do problema do aliciamento de apostas ilegais no Brasil, exploração de tecnologias de IA (SLMs locais, agentes MCP) e formulação da proposta do Sentinela Clandestino.

2. **`cmp.md` (Artefato Competidores e Contribuição):**  
   Mapeamento de 10 ferramentas de mercado e 10 artigos científicos Qualis A1 (0 do arXiv), seleção dos 3+3 competidores mais próximos (Trend Micro Check, Gamban, Netcraft Mobile, Muzakir et al., Álvarez-Ojeda et al., Nabeel et al.), matriz de 8 eixos com 3 perdas categóricas (`✘`) e frase canônica da contribuição. Aprovado com louvor em auditoria cega independente.

3. **`main.tex` e `main.pdf` (Relatório Técnico / Artigo da VA2):**  
   Artigo completo redigido no padrão Springer LNCS integrando as descobertas do `brw` e do `cmp` com formalização matemática, diagrama tabular de competidores e assunção rigorosa dos compromissos de engenharia.

4. **`PITCH.md` (Roteiro de Defesa Oral sem a Tela):**  
   Guia de sustentação oral em 4 blocos (2 minutos) com respostas prontas para as 5 perguntas críticas da banca sobre DGA, MAMF, canalização de interesse e modelos LAYA.

---

## Como Compilar o Relatório Localmente

Para recompilar o PDF a qualquer momento na sua máquina:
```powershell
py va2/compile.py
```
O script executa o ciclo completo de 4 passos (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`) e atualiza o `main.pdf` na própria pasta `va2/`.
