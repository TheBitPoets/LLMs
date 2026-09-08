#!/usr/bin/env python3
"""Verifica che le dispense PDF siano complete, apribili e non troncate."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    ROOT / "output/pdf/dispense-llm-studente.pdf": 70,
    ROOT / "output/pdf/dispense-llm-docente.pdf": 80,
}


def structural_check(path: Path) -> None:
    data = path.read_bytes()
    if len(data) < 100_000:
        raise ValueError(f"file troppo piccolo ({len(data)} byte)")
    if not data.startswith(b"%PDF-"):
        raise ValueError("intestazione %PDF mancante")

    tail = data[-4096:]
    match = re.search(rb"startxref\s+(\d+)\s+%%EOF\s*$", tail)
    if not match:
        raise ValueError("trailer startxref/%%EOF mancante: PDF probabilmente troncato")
    xref_offset = int(match.group(1))
    if not 0 < xref_offset < len(data):
        raise ValueError(f"offset startxref fuori dal file: {xref_offset}")
    xref_prefix = data[xref_offset : xref_offset + 128]
    if not (xref_prefix.startswith(b"xref") or b"/Type/XRef" in xref_prefix):
        raise ValueError("startxref non punta a una tabella o stream XRef")


def reader_check(path: Path, minimum_pages: int) -> int:
    reader = PdfReader(path, strict=True)
    pages = len(reader.pages)
    if pages < minimum_pages:
        raise ValueError(f"pagine insufficienti: {pages}, minimo {minimum_pages}")

    # Forza la lettura del content stream di ogni pagina: la sola apertura non
    # basta a rilevare tutti gli stream troncati o gli oggetti irraggiungibili.
    for page_number, page in enumerate(reader.pages, 1):
        try:
            page.get_contents()
        except Exception as exc:  # pypdf espone eccezioni diverse per stream/filtri
            raise ValueError(f"pagina {page_number} non leggibile: {exc}") from exc
    return pages


def main() -> int:
    errors: list[str] = []
    for path, minimum_pages in EXPECTED.items():
        try:
            structural_check(path)
            pages = reader_check(path, minimum_pages)
        except (OSError, PdfReadError, ValueError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
        else:
            print(
                f"PDF OK: {path.relative_to(ROOT)} — "
                f"{path.stat().st_size} byte, {pages} pagine"
            )

    if errors:
        print("PDF CHECK FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
