#!/usr/bin/env python3
"""Build a separate TheBitLab Content Pack from curated teaching sources."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/course/ai-software"
LESSONS = [
    ("S00-contesto.md", "Leggere il progetto e preparare il contesto", "A", "context-engineering",
     "Esegui lo starter, conserva i fallimenti attesi e collega tre regole a funzioni e test."),
    ("S01-specifiche.md", "Specifiche ed esempi di accettazione", "B", "spec-driven-development",
     "Scrivi sei casi e proponi separatamente la variante di durata 120 minuti con tracciabilità."),
    ("S02-implementazione.md", "Implementazione per porzioni verificabili", "C", "test-driven-development",
     "Dal lavoro precedente implementa R01-R04 in patch separate e aggiungi un caso indipendente."),
    ("S03-diagnosi.md", "Diagnosi e regressioni su codice esistente", "D", "debugging",
     "Riproduci il difetto degli intervalli, confronta due ipotesi e conserva il test di regressione."),
    ("S04-pattern.md", "Pattern applicativi e adapter", "E", "ports-and-adapters",
     "Completa R05-R06; nei rami avanzati aggiungi SQLite oppure valuta la proposta locale LLM."),
    ("S05-consegna.md", "Consegna e valutazione del processo", "F", "software-delivery",
     "Consegna R01-R06 verificati, report, diff, due casi indipendenti e spiegazione individuale."),
]


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def expected_files():
    refs = [{"id": f"ai-se-ref-{slug}", "kind": "book", "role": "teacher-reference",
             "provider": "manning", "title": title,
             "uri": f"https://www.manning.com/books/{slug}",
             "access": "public-catalog", "license_status": "reference-only"}
            for slug, title in [("spec-driven-development", "Spec-Driven Development"),
                                ("context-engineering", "Context Engineering"),
                                ("ai-powered-developer", "AI-Powered Developer"),
                                ("agent-design-patterns", "Agent Design Patterns"),
                                ("vibe-engineering", "Vibe Engineering")]]
    source = {"id": "ai-se-source-lessons", "kind": "source-package",
              "label": "Laboratori originali di sviluppo con coding agent", "type": "markdown",
              "provider": "local", "role": "course-content", "path": "docs/course/ai-software",
              "files": ["README.md", *[r[0] for r in LESSONS], "REPORT-template.md"],
              "license_status": "project-license-to-review", "indexing_status": "ready"}
    items, design_items, files = [], [], {}
    teacher = (DOCS / "TEACHER.md").read_text()
    sections = re.split(r"(?=^## S\d\d - )", teacher, flags=re.M)[1:]
    if len(sections) != len(LESSONS):
        raise ValueError("six curated teacher sections are required")
    for i, (filename, title, difficulty, topic, task) in enumerate(LESSONS):
        cid, aid = f"ai-se-content-s{i:02}", f"ai-se-activity-s{i:02}"
        href = f"docs/course/ai-software/{filename}"
        items.append({"id": cid, "kind": "module", "path": href, "order": i + 1,
                      "status": "draft", "curriculum_topics": [topic], "activity_ids": [aid],
                      "source_refs": [{"id": source["id"], "role": "content-origin", "locator": href},
                                      {"id": "ai-se-ref-ai-powered-developer", "role": "teacher-reference",
                                       "locator": "public catalog; original exercise"}]})
        design_items.append({"id": f"item-s{i:02}", "title": title, "source_id": source["id"],
                             "source": filename, "href": href, "level": 1, "activity_ids": [aid],
                             "frame": {"status": "draft", "objectives": task,
                                       "next_step": "Consegnare evidenze e completare la verifica individuale."}})
        base = ROOT / "activities/ai-software" / aid
        student = (f"# S{i:02} - {title}\n\n{task}\n\n"
                   "Leggi la lezione corrispondente nel Content Pack. L'attività continua "
                   "il progetto della lezione precedente; importa il tuo lavoro, non sovrascriverlo "
                   "con lo starter iniziale. Lo starter allegato serve per ripartire dalla baseline, "
                   "che presenta fallimenti intenzionali. Il docente può fornire un checkpoint "
                   "per il recupero.\n\n"
                   "Esegui `python3 -m unittest discover -s . -p 'test_*.py' -v`. "
                   "Mantieni i test pubblici e collega i casi aggiunti ai requisiti. "
                   "Fornisci al coding agent soltanto la cartella studente. "
                   "Compila REPORT-template.md con risultati reali.\n")
        assets = [{"type": "starter", "path": "student/README.md", "target_path": "README.md",
                   "visibility": "student", "description": "Consegna specifica della lezione"}]
        files[base / "student/README.md"] = student
        starter_sources = [(p, "visible_test" if p.name.startswith("test_") else "starter")
                           for p in sorted((ROOT / "labs/ai_software/starter").iterdir()) if p.is_file()]
        starter_sources.append((DOCS / "REPORT-template.md", "starter"))
        if i >= 4:
            starter_sources.append((ROOT / "labs/ai_software/proposal.py", "example"))
        for path, kind in starter_sources:
            files[base / "student" / path.name] = path.read_text()
            assets.append({"type": kind, "path": f"student/{path.name}", "target_path": path.name,
                           "visibility": "student", "description": "Materiale originale per il laboratorio"})
        files[base / "teacher/SOLUTION.md"] = "# Soluzione docente\n\n" + sections[i].strip() + "\n"
        files[base / "teacher/booking.py"] = (ROOT / "labs/ai_software/reference/booking.py").read_text()
        assets.extend([{"type": "teacher_only", "path": "teacher/SOLUTION.md", "visibility": "teacher",
                        "description": "Esiti, spiegazione e correzione della lezione"},
                       {"type": "teacher_only", "path": "teacher/booking.py", "visibility": "teacher",
                        "description": "Implementazione di riferimento R01-R08"}])
        files[base / "activity.json"] = json_text({
            "schema_version": "1.0", "id": aid, "titolo": title, "tipo": "laboratorio",
            "difficolta": difficulty, "argomenti": [topic], "consegna": task,
            "student_support_mode": "feedback-tecnico",
            "contesto": {"percorso": "percorso-ai-software", "uda": "uda-ai-software"},
            "content_ids": [cid], "source_refs": [{"source_id": source["id"], "href": href}],
            "assets": assets, "correzione": {"compila": False, "test": i >= 2,
                "sandbox": i >= 2, "ai_feedback": i != 5},
            "metriche": {"tempo_stimato_minuti": 120, "traccia_tempo_dichiarato": True,
                "traccia_sessioni_thebitlab": True, "traccia_eventi_didattici": True,
                "traccia_errori_compilazione": False},
            "rubrica": [{"criterio": "Requisiti ed esempi", "punti": 3},
                        {"criterio": "Correttezza e test indipendenti", "punti": 3},
                        {"criterio": "Riproducibilità", "punti": 2},
                        {"criterio": "Spiegazione individuale", "punti": 2}],
        })
    projected = {key: source[key] for key in
                 ("id", "label", "type", "provider", "path", "files", "indexing_status")}
    design = {"schema_version": "1.0", "id": "ai-se-course-2026-2027",
              "title": "Sviluppare software con coding agent", "description":
              "Supplemento pratico di 12 ore. Estensioni autonome: AI Engineer +6h, software engineer +6h.",
              "source_ids": [source["id"]], "sources": [projected], "years": [{
                  "id": "percorso-ai-software", "title": "Laboratorio pratico",
                  "description": "Sei incontri da due ore; non sottratti implicitamente al corso LLM annuale.",
                  "weekly_hours": 2, "weeks": 6, "udas": [{"id": "uda-ai-software",
                      "title": "Dal requisito alla consegna", "path": source["path"],
                      "weeks": 6, "items": design_items}]}]}
    pack = {"schema_version": "thebitlab.content-pack.v1", "id": "ai-se-pack-2026-2027",
            "title": "Coding agent e software engineering pratico", "version": "0.2.0",
            "status": "draft", "language": "it", "audience": {
                "school_level": "secondaria-secondo-grado-e-formazione-adulti", "subject": "Ingegneria del software con AI", "year": 0},
            "ownership": {"content_origin": "original-course-material",
                "redistribution_status": "project-license-to-review", "editorial_copying_allowed": False},
            "references": refs, "sources": [source], "coverage": {
                "path": "content/ai-software/COVERAGE.md", "status": "draft"},
            "content_items": items, "course_designs": [{"id": design["id"],
                "path": "doc/course_designs/ai_software_2026_2027.json", "status": "draft"}],
            "activity_roots": ["activities/ai-software"], "policies": {
                "provenance_required": True, "teacher_review_required_before_publish": True,
                "student_teacher_asset_separation_required": True, "ai_is_not_primary_source": True,
                "restricted_source_copying_forbidden": True}}
    files[ROOT / "content/ai-software/content-pack.json"] = json_text(pack)
    files[ROOT / "doc/course_designs/ai_software_2026_2027.json"] = json_text(design)
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    files = expected_files()
    different = []
    for path, text in files.items():
        if args.check:
            if not path.exists() or path.read_text() != text:
                different.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    if different:
        raise SystemExit("Generated artifacts differ: " + ", ".join(different))
    print(f"AI software pack: {len(LESSONS)} lessons, {len(files)} generated files OK")


if __name__ == "__main__":
    main()
