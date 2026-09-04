#!/usr/bin/env python3
"""Costruisce le dispense studente e docente in Markdown, HTML e PDF."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
PDF_OUT = ROOT / "output/pdf"
MODULES = sorted((ROOT / "docs/course/modules").glob("M??-*.md"))


def read(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()

    # Le tabelle Markdown molto larghe non hanno una colonna flessibile nel
    # template LaTeX predefinito. Nel volume il glossario diventa una lista di
    # definizioni, evitando qualsiasi testo oltre il margine A4.
    if path.name == "GLOSSARY.md":
        lines = text.splitlines()
        converted = [lines[0], "", lines[2], ""]
        for line in lines[6:]:
            if not line.startswith("|"):
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|", 1)]
            if len(cells) == 2:
                converted.extend([f"**{cells[0]}.** {cells[1]}", ""])
        text = "\n".join(converted).strip()

    def replace(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I) or target.startswith(("#", "mailto:")):
            return match.group(0)
        raw_path, marker, fragment = target.partition("#")
        if not raw_path:
            return match.group(0)
        absolute = (path.parent / raw_path).resolve()
        rebased = Path(os.path.relpath(absolute, OUT)).as_posix()
        return f"[{label}]({rebased}{marker}{fragment})"

    return re.sub(r"\[([^]]*)\]\(([^)]+)\)", replace, text)


def front_matter(title: str, subtitle: str) -> str:
    return f"""---
title: "{title}"
subtitle: "{subtitle}"
author: "TheBitPoets"
date: "Edizione 2026/27 — content pack 0.9.0"
lang: it-IT
rights: "Materiale originale del progetto; fonti esterne citate"
---

# Come usare queste dispense

Ogni capitolo offre un percorso **Practitioner**, intuitivo e pratico, e un
approfondimento **AI Engineer** con matematica e implementazione. Gli esercizi
A–F seguono la tassonomia TheBitLab: osserva, modifica, crea, diagnostica,
mini-progetto e prodotto integrato.

I nomi e le capacità dei modelli cambiano rapidamente: consultare il catalogo
datato nel repository e verificare sempre documentazione e licenze correnti.
I risultati hardware non presenti in un manifest di evidenza sono stime, non
misure.
"""


def compose(teacher: bool) -> str:
    title = "Dispense LLM — edizione docente" if teacher else "Dispense LLM — edizione studente"
    subtitle = "Practitioner e AI Engineer · teoria, matematica, laboratori e Pollicino"
    parts = [front_matter(title, subtitle), read(ROOT / "docs/course/modules/README.md")]
    parts.extend(read(path) for path in MODULES)
    parts.append(read(ROOT / "docs/course/handbook/GLOSSARY.md"))
    if teacher:
        parts.extend([
            "# Apparati riservati al docente",
            read(ROOT / "docs/course/teacher/teacher-guide.md"),
            read(ROOT / "docs/course/teacher/lab-guide.md"),
            read(ROOT / "docs/course/teacher/quick-check-solutions.md"),
            read(ROOT / "docs/course/assessments/diagnostic.md"),
            read(ROOT / "docs/course/assessments/final-practical.md"),
        ])
    # Con `documentclass=report` ogni H1 apre gia un capitolo. Un secondo
    # `\\newpage` produrrebbe pagine bianche fra capitoli.
    return "\n\n".join(parts) + "\n"


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def build_static_figures() -> None:
    target_dir = ROOT / "visuals/static/rendered"
    target_dir.mkdir(parents=True, exist_ok=True)
    for stale in target_dir.glob(".*.building.png"):
        stale.unlink(missing_ok=True)
    for source in sorted((ROOT / "visuals/static").glob("*.svg")):
        target = target_dir / f"{source.stem}.png"
        if target.exists() and target.stat().st_size > 1024 and target.stat().st_mtime >= source.stat().st_mtime:
            continue
        temporary = target_dir / f".{source.stem}.building.png"
        temporary.unlink(missing_ok=True)
        run([
            "inkscape", str(source), "--export-type=png",
            f"--export-filename={temporary}", "--export-width=1600",
        ])
        # Il rename atomico impedisce a Pandoc/LaTeX di osservare un PNG
        # parzialmente scritto durante build concorrenti.
        os.replace(temporary, target)


def build_one(kind: str, teacher: bool) -> None:
    markdown = OUT / f"dispense-llm-{kind}.md"
    html = OUT / f"dispense-llm-{kind}.html"
    pdf = PDF_OUT / f"dispense-llm-{kind}.pdf"
    markdown.write_text(compose(teacher), encoding="utf-8")
    common = ["--from=gfm+tex_math_dollars", "--resource-path=dist:.", "--toc", "--number-sections", "--metadata", "toc-title=Indice"]
    run(["pandoc", str(markdown), *common, "--standalone", "--mathml", "--css", "../docs/course/handbook/handbook.css", "-o", str(html)])
    run([
        "pandoc", str(markdown), *common, "--pdf-engine=xelatex",
        "-V", "documentclass=report", "-V", "papersize=a4", "-V", "geometry:margin=2cm",
        "-V", "mainfont=DejaVu Sans", "-V", "monofont=DejaVu Sans Mono",
        "-V", "colorlinks=true", "-V", "linkcolor=blue", "-V", "urlcolor=blue",
        "-o", str(pdf),
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="ricostruisce e verifica che gli output esistano e non siano vuoti")
    parser.parse_args()
    OUT.mkdir(exist_ok=True)
    PDF_OUT.mkdir(parents=True, exist_ok=True)
    build_static_figures()
    build_one("studente", False)
    build_one("docente", True)
    for path in [*OUT.glob("dispense-llm-*"), *PDF_OUT.glob("dispense-llm-*.pdf")]:
        if path.stat().st_size < 1000:
            raise SystemExit(f"artefatto troppo piccolo: {path}")
    print("Dispense costruite: studente e docente in Markdown, HTML e PDF")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
