#!/usr/bin/env python3
"""
Academic Search & Reference Pipeline (`core/tools/academic_search.py`)
Pipeline automatizado de literatura científica:
1. Busca artigos no arXiv, CrossRef e Semantic Scholar
2. Faz download automatizado de PDFs abertos (`refs/pdfs/` e `article/refs/pdfs/`)
3. Executa extração textual / OCR automático zero-token (`core/tools/pdf_ocr_parser.py`)
4. Atualiza `article/references.bib` e `papers/artigo-final/references.bib`
5. Gera automaticamente metadados estruturados em `.yaml` na pasta `refs/` (`refs/<key>.yaml` e `article/refs/<key>.yaml`)

Uso:
    py core/tools/academic_search.py --query "explicit computation graph neural network" --limit 3 --add-to-bib --generate-yaml --download-pdf
"""

import argparse
import json
import re
import shutil
import ssl
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from pdf_ocr_parser import parse_pdf_zero_token

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ARTICLE_BIB_PATH = ROOT_DIR / "article" / "references.bib"
PAPERS_BIB_PATH = ROOT_DIR / "papers" / "artigo-final" / "references.bib"
REFS_DIRS = [ROOT_DIR / "refs", ROOT_DIR / "article" / "refs"]


def safe_urlopen(req, timeout=20):
    ctx = ssl._create_unverified_context()
    return urllib.request.urlopen(req, timeout=timeout, context=ctx)


def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def generate_bibtex_key(author: str, year: str, title: str) -> str:
    last_name = author.split()[-1] if author else "author"
    last_name = re.sub(r"[^a-zA-Z]", "", last_name).lower()
    year_str = re.sub(r"[^0-9]", "", str(year)) if year else "2026"
    stop_words = {"the", "a", "an", "on", "in", "of", "for", "and", "to", "with", "by"}
    words = [re.sub(r"[^a-zA-Z]", "", w).lower() for w in title.split()]
    words = [w for w in words if w and w not in stop_words]
    first_word = words[0] if words else "paper"
    return f"{last_name}{year_str}{first_word}"


def search_arxiv(query: str, limit: int = 5):
    encoded_query = urllib.parse.quote(query)
    url = f"https://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={limit}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "AcademicWorkspace/2.0 (mailto:jose.alberico@ufrpe.br)"}
    )
    try:
        with safe_urlopen(req, timeout=20) as response:
            content = response.read().decode("utf-8")
    except Exception as e:
        print(f"[Aviso] Falha ao consultar arXiv: {e}", file=sys.stderr)
        return []

    root = ET.fromstring(content)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    results = []

    for entry in root.findall("atom:entry", ns):
        title = clean_text(entry.find("atom:title", ns).text or "")
        summary = clean_text(entry.find("atom:summary", ns).text or "")
        published = entry.find("atom:published", ns).text or ""
        year = published[:4] if published else "2026"

        authors = []
        for author in entry.findall("atom:author", ns):
            name = author.find("atom:name", ns)
            if name is not None and name.text:
                authors.append(name.text.strip())

        paper_id_elem = entry.find("atom:id", ns)
        paper_url = paper_id_elem.text.strip() if paper_id_elem is not None else ""
        arxiv_id = paper_url.split("/abs/")[-1] if "/abs/" in paper_url else paper_url.split("/")[-1]
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf" if arxiv_id else ""
        doi_elem = entry.find("arxiv:doi", ns)
        doi = doi_elem.text.strip() if doi_elem is not None else ""

        first_author = authors[0] if authors else "Anon"
        bib_key = generate_bibtex_key(first_author, year, title)
        authors_str = " and ".join(authors) if authors else "Unknown"

        bibtex = (
            f"@article{{{bib_key},\n"
            f"  title={{{title}}},\n"
            f"  author={{{authors_str}}},\n"
            f"  journal={{arXiv preprint arXiv:{arxiv_id}}},\n"
            f"  year={{{year}}},\n"
            f"  url={{{paper_url}}}\n"
            f"}}"
        )

        results.append({
            "title": title,
            "authors": authors,
            "year": year,
            "venue": f"arXiv:{arxiv_id}",
            "type": "preprint",
            "summary": summary,
            "url": paper_url,
            "pdf_url": pdf_url,
            "doi": doi,
            "bib_key": bib_key,
            "bibtex": bibtex,
            "source": "arXiv"
        })

    return results


def search_crossref(query: str, limit: int = 5):
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.crossref.org/works?query={encoded_query}&rows={limit}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "AcademicWorkspace/2.0 (mailto:jose.alberico@ufrpe.br)"}
    )
    try:
        with safe_urlopen(req, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print(f"[Aviso] Falha ao consultar CrossRef: {e}", file=sys.stderr)
        return []

    items = data.get("message", {}).get("items", [])
    results = []

    for item in items:
        titles = item.get("title", [])
        title = clean_text(titles[0]) if titles else "Sem título"

        authors = []
        for author in item.get("author", []):
            given = author.get("given", "")
            family = author.get("family", "")
            full = f"{given} {family}".strip()
            if full:
                authors.append(full)

        issued = item.get("issued", {}).get("date-parts", [[]])
        year = str(issued[0][0]) if (issued and issued[0]) else "2026"
        doi = item.get("DOI", "")
        url_str = item.get("URL", f"https://doi.org/{doi}" if doi else "")
        container = item.get("container-title", [])
        journal = clean_text(container[0]) if container else "Conferência/Periódico"
        abstract = clean_text(re.sub(r"<[^>]+>", "", item.get("abstract", "")))

        pdf_url = ""
        for link in item.get("link", []):
            if "pdf" in link.get("content-type", "").lower():
                pdf_url = link.get("URL", "")
                break

        first_author = authors[0] if authors else "Anon"
        bib_key = generate_bibtex_key(first_author, year, title)
        authors_str = " and ".join(authors) if authors else "Unknown"

        bibtex = (
            f"@article{{{bib_key},\n"
            f"  title={{{title}}},\n"
            f"  author={{{authors_str}}},\n"
            f"  journal={{{journal}}},\n"
            f"  year={{{year}}},\n"
            f"  doi={{{doi}}}\n"
            f"}}"
        )

        results.append({
            "title": title,
            "authors": authors,
            "year": year,
            "venue": journal,
            "type": "article",
            "summary": abstract or f"Publicado em: {journal}",
            "url": url_str,
            "pdf_url": pdf_url,
            "doi": doi,
            "bib_key": bib_key,
            "bibtex": bibtex,
            "source": "CrossRef"
        })

    return results


def download_pdf_and_ocr(entry: dict) -> dict:
    pdf_url = entry.get("pdf_url", "")
    key = entry["bib_key"]
    meta = {"pdf_path": "~", "ocr_path": "~", "ocr_method": "none", "ocr_chars": 0}
    if not pdf_url:
        return meta

    primary_pdf = REFS_DIRS[0] / "pdfs" / f"{key}.pdf"
    primary_ocr = REFS_DIRS[0] / "ocr" / f"{key}.txt"
    primary_pdf.parent.mkdir(parents=True, exist_ok=True)
    primary_ocr.parent.mkdir(parents=True, exist_ok=True)

    try:
        req = urllib.request.Request(
            pdf_url,
            headers={"User-Agent": "Mozilla/5.0 (AcademicWorkspace/2.0; +mailto:jose.alberico@ufrpe.br)"}
        )
        with safe_urlopen(req, timeout=25) as resp:
            pdf_bytes = resp.read()
        if pdf_bytes[:4] == b"%PDF":
            primary_pdf.write_bytes(pdf_bytes)
            print(f"[PDF Download] Salvo em: {primary_pdf} ({len(pdf_bytes)} bytes)")
            ocr_res = parse_pdf_zero_token(primary_pdf, pages="1-2")
            if ocr_res["text"]:
                primary_ocr.write_text(ocr_res["text"], encoding="utf-8")
            # Espelha em article/refs/
            for rdir in REFS_DIRS[1:]:
                (rdir / "pdfs").mkdir(parents=True, exist_ok=True)
                (rdir / "ocr").mkdir(parents=True, exist_ok=True)
                shutil.copy2(primary_pdf, rdir / "pdfs" / f"{key}.pdf")
                if primary_ocr.exists():
                    shutil.copy2(primary_ocr, rdir / "ocr" / f"{key}.txt")
            meta["pdf_path"] = f"refs/pdfs/{key}.pdf"
            meta["ocr_path"] = f"refs/ocr/{key}.txt"
            meta["ocr_method"] = ocr_res["method"]
            meta["ocr_chars"] = ocr_res["char_count"]
    except Exception as e:
        print(f"[Aviso PDF] Não foi possível baixar PDF de {pdf_url}: {e}", file=sys.stderr)

    return meta


def write_yaml_metadata(entry: dict, pdf_meta: dict = None):
    pdf_meta = pdf_meta or {"pdf_path": "~", "ocr_path": "~", "ocr_method": "none", "ocr_chars": 0}
    key = entry["bib_key"]
    title_clean = entry["title"].replace('"', "'")
    venue_clean = entry.get("venue", entry["source"]).replace('"', "'")
    summary_clean = entry.get("summary", "").replace('"', "'")[:320]
    authors_yaml = "\n".join([f'  - "{a}"' for a in entry.get("authors", ["Unknown"])])

    yaml_content = f"""key: {key}
title: "{title_clean}"
type: {entry.get('type', 'article')}
year: {entry.get('year', '2026')}
venue: "{venue_clean}"
url: "{entry.get('url', '')}"
doi: "{entry.get('doi', '') or '~'}"
authors:
{authors_yaml}
pdf_local: "{pdf_meta['pdf_path']}"
ocr_extract: "{pdf_meta['ocr_path']}"
ocr_zero_token_method: "{pdf_meta['ocr_method']}"
citations: "~"
contributions:
  - "{summary_clean}"
gaps:
  - "Requer avaliacao experimental especifica no contexto de grafos explicitos e inferencia local on-device."
tags: [method-source, deep-learning, neural-networks]
relevance: "Referencia catalogada automaticamente via pipeline academic_search.py para fundamentacao teorica e metodologica do artigo."
notes: ~
"""
    for rdir in REFS_DIRS:
        rdir.mkdir(parents=True, exist_ok=True)
        yaml_file = rdir / f"{key}.yaml"
        yaml_file.write_text(yaml_content, encoding="utf-8")
        print(f"[YAML Gerado] {yaml_file}")


def append_to_bib(bibtex_entries: list, bib_paths: list):
    for bib_path in bib_paths:
        if not bib_path.exists():
            bib_path.parent.mkdir(parents=True, exist_ok=True)
            bib_path.touch()
        current_content = bib_path.read_text(encoding="utf-8")
        added_count = 0
        with open(bib_path, "a", encoding="utf-8") as f:
            for entry in bibtex_entries:
                key = entry["bib_key"]
                if key in current_content:
                    continue
                f.write("\n\n" + entry["bibtex"])
                added_count += 1
        print(f"=> {added_count} nova(s) referência(s) sincronizada(s) em {bib_path}")


def main():
    parser = argparse.ArgumentParser(description="Pipeline de Busca Acadêmica, Download de PDF, OCR Zero-Token e Metadados YAML")
    parser.add_argument("--query", "-q", required=True, help="Termos de busca (ex: 'neural network autograd')")
    parser.add_argument("--limit", "-l", type=int, default=3, help="Quantidade máxima de resultados por fonte")
    parser.add_argument("--source", choices=["all", "arxiv", "crossref"], default="all", help="Fonte de busca")
    parser.add_argument("--add-to-bib", action="store_true", help="Salvar referências em article/references.bib e papers/artigo-final/references.bib")
    parser.add_argument("--generate-yaml", action="store_true", help="Gerar arquivos de metadados estruturados em refs/<key>.yaml")
    parser.add_argument("--download-pdf", action="store_true", help="Baixar PDFs abertos e executar OCR automático zero-token")

    args = parser.parse_args()
    print(f"\n[Buscando] '{args.query}' nas bases acadêmicas...")

    results = []
    if args.source in ["all", "arxiv"]:
        results.extend(search_arxiv(args.query, limit=args.limit))
    if args.source in ["all", "crossref"]:
        results.extend(search_crossref(args.query, limit=args.limit))

    if not results:
        print("Nenhum artigo encontrado para a consulta informada.")
        return

    print(f"\n--- Resultados Encontrados ({len(results)}) ---\n")
    for i, res in enumerate(results, 1):
        print(f"{i}. [{res['source']}] {res['title']} ({res['year']})")
        print(f"   Autores: {', '.join(res['authors'][:3])}{' et al.' if len(res['authors']) > 3 else ''}")
        print(f"   Link: {res['url']}")
        print(f"   Chave de citação: \\cite{{{res['bib_key']}}}\n")

        pdf_meta = None
        if args.download_pdf:
            pdf_meta = download_pdf_and_ocr(res)
        if args.generate_yaml:
            write_yaml_metadata(res, pdf_meta)

    if args.add_to_bib:
        append_to_bib(results, [ARTICLE_BIB_PATH, PAPERS_BIB_PATH])


if __name__ == "__main__":
    main()
