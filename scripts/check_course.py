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
        if len(text.split()) < 500:
            fail(f"{path}: dispensa troppo breve ({len(text.split())} parole)", errors)
        for heading in (
            "Problema iniziale",
            "Esempio minimo",
            "Esercizi A–F",
            "Sintesi inclusiva",
            "Fonti e collegamenti",
        ):
            if heading not in text:
                fail(f"{path}: sezione richiesta mancante: {heading}", errors)

    pack_path = ROOT / "content/llm/content-pack.json"
    try:
        pack = json.loads(pack_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"Content Pack non leggibile: {exc}", errors)
        pack = {}
    if pack.get("schema_version") != "thebitlab.content-pack.v1":
        fail("Content Pack: schema_version non conforme", errors)
    if pack.get("status") not in {"draft", "reviewed", "approved"}:
        fail("Content Pack: stato editoriale non valido", errors)
    content_items = pack.get("content_items", [])
    if not isinstance(content_items, list) or len(content_items) != 20:
        fail(f"Content Pack: attesi 20 content item, trovati {len(content_items) if isinstance(content_items, list) else 'n/d'}", errors)
    activity_ids = {
        aid
        for item in content_items if isinstance(item, dict)
        for aid in item.get("activity_ids", []) if isinstance(aid, str)
    }
    activities = sorted((ROOT / "activities/llm").glob("*/activity.json"))
    if len(activities) != 20:
        fail(f"attese 20 Activity TheBitLab, trovate {len(activities)}", errors)
    for activity_path in activities:
        try:
            activity = json.loads(activity_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"{activity_path}: JSON non valido: {exc}", errors)
            continue
        if activity.get("id") not in activity_ids:
            fail(f"{activity_path}: id non collegato dal Content Pack", errors)
        if activity.get("schema_version") != "1.0":
            fail(f"{activity_path}: schema Activity non supportato", errors)
        for asset in activity.get("assets", []):
            target = activity_path.parent / str(asset.get("path", ""))
            if not target.is_file():
                fail(f"{activity_path}: asset mancante {asset.get('path')}", errors)

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

    static_visuals = sorted((ROOT / "visuals/static").glob("*.svg"))
    rendered_visuals = sorted((ROOT / "visuals/static/rendered").glob("*.png"))
    if len(static_visuals) != 7 or len(rendered_visuals) != 7:
        fail(f"attese 7 figure statiche SVG+PNG, trovate {len(static_visuals)}+{len(rendered_visuals)}", errors)

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
    print(
        f"COURSE CHECK OK: {len(modules)} dispense, {len(activities)} Activity, "
        f"{len(visuals)} visuali interattive, {len(static_visuals)} figure statiche, link locali validi"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
