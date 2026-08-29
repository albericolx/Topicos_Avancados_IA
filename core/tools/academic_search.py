#!/usr/bin/env python3
"""
Academic Search Tool - Busca de artigos científicos no arXiv e CrossRef
com geração automática de citações BibTeX para o artigo da disciplina.

Uso:
    py core/tools/academic_search.py --query "explicit computation graph neural network" --limit 5
    py core/tools/academic_search.py --query "deep learning backpropagation autograd" --add-to-bib
"""

import argparse
import json
import re
import ssl
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

DEFAULT_BIB_PATH = Path(__file__).resolve().parent.parent.parent / "papers" / "artigo-final" / "references.bib"


def safe_urlopen(req, timeout=15):
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
    first_word = title.split()[0] if title else "paper"
    first_word = re.sub(r"[^a-zA-Z]", "", first_word).lower()
    return f"{last_name}{year_str}{first_word}"


def search_arxiv(query: str, limit: int = 5):
    encoded_query = urllib.parse.quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={limit}"
    
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "AcademicWorkspace/1.0 (mailto:educacao@ufrpe.br)"}
    )
    
    try:
        with safe_urlopen(req, timeout=15) as response:
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
        paper_id = paper_id_elem.text.strip() if paper_id_elem is not None else ""
        doi_elem = entry.find("arxiv:doi", ns)
        doi = doi_elem.text.strip() if doi_elem is not None else ""

        first_author = authors[0] if authors else "Anon"
        bib_key = generate_bibtex_key(first_author, year, title)

        authors_str = " and ".join(authors) if authors else "Unknown"
        bibtex = (
            f"@article{{{bib_key},\n"
            f"  title={{{title}}},\n"
            f"  author={{{authors_str}}},\n"
            f"  journal={{arXiv preprint {paper_id}}},\n"
            f"  year={{{year}}}\n"
            f"}}"
        )

        results.append({
            "title": title,
            "authors": authors,
            "year": year,
            "summary": summary,
            "url": paper_id,
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
        headers={"User-Agent": "AcademicWorkspace/1.0 (mailto:educacao@ufrpe.br)"}
    )
    
    try:
        with safe_urlopen(req, timeout=15) as response:
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
        url = item.get("URL", f"https://doi.org/{doi}" if doi else "")
        container = item.get("container-title", [])
        journal = container[0] if container else "Conferência/Periódico"

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
            "summary": f"Publicado em: {journal}",
            "url": url,
            "doi": doi,
            "bib_key": bib_key,
            "bibtex": bibtex,
            "source": "CrossRef"
        })

    return results


def append_to_bib(bibtex_entries: list, bib_path: Path):
    if not bib_path.exists():
        bib_path.parent.mkdir(parents=True, exist_ok=True)
        bib_path.touch()

    current_content = bib_path.read_text(encoding="utf-8")
    added_count = 0

    with open(bib_path, "a", encoding="utf-8") as f:
        for entry in bibtex_entries:
            key = entry["bib_key"]
            if key in current_content:
                print(f"[Ignorado] Chave já existente no .bib: {key}")
                continue
            f.write("\n\n" + entry["bibtex"])
            added_count += 1
            print(f"[Adicionado] Citação salva no .bib: {key}")

    print(f"\n=> Total de {added_count} nova(s) referência(s) adicionada(s) em {bib_path}")


def main():
    parser = argparse.ArgumentParser(description="Busca de artigos acadêmicos e gerador BibTeX")
    parser.add_argument("--query", "-q", required=True, help="Termos de busca (ex: 'neural network autograd')")
    parser.add_argument("--limit", "-l", type=int, default=5, help="Quantidade máxima de resultados (padrão: 5)")
    parser.add_argument("--source", choices=["all", "arxiv", "crossref"], default="all", help="Fonte de busca")
    parser.add_argument("--add-to-bib", action="store_true", help="Salvar referências encontradas em references.bib")
    parser.add_argument("--bib-path", type=Path, default=DEFAULT_BIB_PATH, help="Caminho do arquivo .bib")

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

    if args.add_to_bib:
        append_to_bib(results, args.bib_path)
    else:
        print("Dica: Use a flag --add-to-bib para salvar essas citações automaticamente em references.bib!")


if __name__ == "__main__":
    main()
