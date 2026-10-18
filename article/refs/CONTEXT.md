# Pipeline de Referências e Literatura (`refs/`)
> Repositório estruturado de referências científicas do workspace — fichas de revisão em `.yaml` (Tier-2), índice de captura em [`REFS.md`](REFS.md) (Tier-1), PDFs locais (`pdfs/`) e extrações textuais via OCR zero-token (`ocr/`).

## Esquema de Metadados (`.yaml`)

Cada entrada citada em [`article/references.bib`](../article/references.bib) possui seu respectivo arquivo estruturado `refs/<bib_key>.yaml` gerado automaticamente por [`core/tools/academic_search.py`](../core/tools/academic_search.py) ou curado pelo harness:

```yaml
key: <bib-key>
title: "<título completo do artigo>"
type: article | book | conference | preprint | thesis
year: <ano>
venue: "<periódico ou conferência>"
url: "<DOI ou link canônico>"
doi: "<identificador DOI>"
authors:
  - "<Autor 1>"
pdf_local: "refs/pdfs/<bib-key>.pdf"
ocr_extract: "refs/ocr/<bib-key>.txt"
ocr_zero_token_method: "native_pdftotext | native_pypdf | tesseract_ocr"
citations: <contagem ou "~N">
contributions:
  - "<contribuição central verificada no texto>"
gaps:
  - "<limitação ou lacuna frente ao nosso projeto>"
tags: [<role-tag>, <domain-tags>...]
relevance: "<como esta referência fundamenta o nosso manuscrito>"
notes: ~
```

## Vocabulário de Tags
- **Role Tags (sempre na primeira posição):** `foundational` · `survey` · `competing-work` · `baseline` · `ground-truth` · `method-source` · `tool` · `application`
- **Domain Tags:** `deep-learning` · `backpropagation` · `computation-graph` · `transformers` · `on-device-slm` · `gambling-detection` · `graph-inference` · `mobile-security`

## Fluxo Automatizado (Zero-Token OCR + YAML)
```bash
# Busca acadêmica + download de PDF + OCR zero-token + geração automática de .yaml e .bib
py core/tools/academic_search.py --query "explicit computation graph neural networks" --limit 2 --add-to-bib --generate-yaml --download-pdf

# Extração direta de texto/OCR zero-token sobre um PDF local
py core/tools/pdf_ocr_parser.py --file refs/pdfs/vaswani2017attention.pdf --out refs/ocr/vaswani2017attention.txt
```

<!-- routing:start -->
## Roteamento da Pasta

| Caminho | Descrição |
|---|---|
| [`REFS.md`](REFS.md) | Índice Tier-1 com marcadores de qualidade (`[A]`, `[B]`, `[P]`) e mapeamento para os arquivos `.yaml` |
| [`rumelhart1986learning.yaml`](rumelhart1986learning.yaml) | Ficha YAML: Rumelhart, Hinton & Williams (1986) — *Nature* (Retropropagação de erros) |
| [`goodfellow2016deep.yaml`](goodfellow2016deep.yaml) | Ficha YAML: Goodfellow, Bengio & Courville (2016) — *MIT Press* (Fundamentos de Deep Learning) |
| [`vaswani2017attention.yaml`](vaswani2017attention.yaml) | Ficha YAML: Vaswani et al. (2017) — *NeurIPS* (Arquitetura Transformer e Autoatenção) |
| [`nabeel2020following.yaml`](nabeel2020following.yaml) | Ficha YAML: Nabeel et al. (2020) — *ACM TOPS* (Inferência em grafos DNS contra domínios maliciosos) |
| [`muzakir2025text.yaml`](muzakir2025text.yaml) | Ficha YAML: Muzakir et al. (2025) — *IEEE ICISIT* (Detecção textual de anúncios de apostas ilegais) |
| [`alvarezojeda2025precom.yaml`](alvarezojeda2025precom.yaml) | Ficha YAML: Álvarez-Ojeda et al. (2025) — *COLING* (Corpus PRECOM-SM sobre apostas em redes sociais) |
| `pdfs/` | Armazenamento local de PDFs baixados pelo pipeline |
| `ocr/` | Textos extraídos localmente sem custo de tokens (Zero-Token OCR) |
<!-- routing:end -->
