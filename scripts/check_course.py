#!/usr/bin/env python3
"""Controlli strutturali del corso senza dipendenze esterne."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^]]*]\(([^)]+)\)")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    modules = sorted((ROOT / "docs/course/modules").glob("M??-*.md"))
    if len(modules) != 20:
        fail(f"attesi 20 moduli, trovati {len(modules)}", errors)
    for index, path in enumerate(modules):
        expected = f"M{index:02d}"
        text = path.read_text(encoding="utf-8")
        if not path.name.startswith(expected + "-"):
            fail(f"sequenza modulo errata: {path}", errors)
        required_any = ["Obiettivi osservabili", "Risultato Practitioner"]
        if not any(heading in text for heading in required_any):
            fail(f"{path}: obiettivi mancanti", errors)
        if "Verifica" not in text and "Rubrica" not in text:
            fail(f"{path}: verifica/rubrica mancante", errors)
        if "Laboratorio" not in text and "Attività" not in text and expected != "M19":
            fail(f"{path}: laboratorio/attività mancante", errors)

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I) or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                fail(f"link locale rotto: {path.relative_to(ROOT)} -> {target}", errors)

    visuals = sorted((ROOT / "visuals").glob("*.html"))
    if len(visuals) < 6:
        fail(f"attese almeno 6 visuali, trovate {len(visuals)}", errors)
    for path in visuals:
        text = path.read_text(encoding="utf-8")
        for marker in ("prefers-reduced-motion", "Domanda diagnostica", "Limite della visuale"):
            if marker not in text:
                fail(f"{path}: marker visuale mancante: {marker}", errors)

    json.loads((ROOT / "labs/fixtures/rag-corpus.json").read_text(encoding="utf-8"))
    for line_no, line in enumerate((ROOT / "labs/fixtures/predictions.jsonl").read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"predictions.jsonl:{line_no}: {exc}", errors)

    forbidden = ["Licensed to Antonio", "Licensed to <"]
    for path in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.html")):
        text = path.read_text(encoding="utf-8", errors="replace")
        for marker in forbidden:
            if marker in text:
                fail(f"possibile materiale editoriale incorporato in {path}", errors)

    if errors:
        print("COURSE CHECK FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"COURSE CHECK OK: {len(modules)} moduli, {len(visuals)} visuali, link locali validi")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
