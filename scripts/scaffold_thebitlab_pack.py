#!/usr/bin/env python3
"""Genera e controlla i metadati TheBitLab del corso LLM.

I testi delle dispense restano sorgenti curate a mano. Questo script genera
soltanto manifest, Course Design e scheletri ripetitivi delle Activity.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    ("M00-orientamento.md", "Orientamento e baseline", "baseline, limiti e uso responsabile", "A", "studio-guidato", 45, "baseline"),
    ("M01-ecosistema.md", "Mappa dell'ecosistema", "modello, runtime, applicazione, locale e cloud", "B", "esercizio-classe", 50, "ecosystem-map"),
    ("M02-next-token.md", "Predire il simbolo successivo", "probabilità e previsione next-token", "B", "laboratorio", 60, "next-token"),
    ("M03-token-byte-embedding.md", "Token, byte ed embedding", "tokenizzazione, byte ed embedding", "C", "laboratorio", 75, "token-inspector"),
    ("M04-apprendimento.md", "Apprendere dai dati", "loss, gradient descent e generalizzazione", "B", "laboratorio", 60, "learning-curve"),
    ("M05-attention-transformer.md", "Attention e Transformer", "attention causale e blocco Transformer", "C", "laboratorio", 90, "attention"),
    ("M06-architetture-moderne.md", "Architetture moderne", "RoPE, GQA, MoE e long context", "D", "debug-didattico", 75, "architectures"),
    ("M07-dati-scaling.md", "Pre-training, dati e scaling", "dataset, scaling law e data governance", "C", "esercizio-classe", 70, "data-card"),
    ("M08-post-training-reasoning.md", "Post-training e reasoning", "SFT, preferenze, RL e reasoning", "D", "debug-didattico", 75, "post-training"),
    ("M09-pesi-formati-licenze.md", "Pesi, formati e licenze", "model card, formati e licenze", "C", "esercizio-classe", 70, "model-selection"),
    ("M10-hardware-quantizzazione.md", "Hardware e quantizzazione", "memoria, throughput e quantizzazione", "C", "laboratorio", 90, "memory-budget"),
    ("M11-ollama.md", "Ollama e inferenza locale", "Ollama, API locale e riproducibilità", "E", "laboratorio", 120, "ollama"),
    ("M12-sampling-prompting.md", "Sampling e prompting", "temperature, top-k, top-p e output strutturato", "D", "debug-didattico", 75, "sampling"),
    ("M13-app-conversazionali.md", "Applicazioni conversazionali", "chat, stato, streaming ed error handling", "E", "laboratorio", 150, "chatbot"),
    ("M14-valutazione.md", "Valutazione", "dataset, metriche, judge e regressione", "C", "laboratorio", 100, "evaluation"),
    ("M15-rag.md", "Embedding, ricerca e RAG", "retrieval, grounding e prompt injection", "E", "laboratorio", 150, "rag"),
    ("M16-agenti-mcp.md", "Tool use, agenti e MCP", "tool use, autorizzazioni e MCP", "E", "laboratorio", 150, "safe-agent"),
    ("M17-fine-tuning.md", "Fine-tuning e adapter", "LoRA, distillazione e scelta dell'adattamento", "C", "esercizio-classe", 90, "adaptation"),
    ("M18-sistemi-kernel.md", "Sistemi e kernel d'inferenza", "prefill, decode, KV cache e kernel", "C", "laboratorio", 120, "inference-kernel"),
    ("M19-capstone-pollicino.md", "Costruire e integrare", "capstone, piccolo LM e Pollicino", "F", "laboratorio", 300, "pollicino"),
]

UDAS = [
    ("uda-01-fondamenti", "Fondamenti intuitivi", 6, range(0, 4)),
    ("uda-02-transformer", "Come si addestra e funziona un Transformer", 7, range(4, 8)),
    ("uda-03-modelli-locali", "Scegliere ed eseguire modelli locali", 7, range(8, 12)),
    ("uda-04-applicazioni", "Costruire e valutare applicazioni", 8, range(12, 16)),
    ("uda-05-engineering", "AI engineering, sistemi e capstone", 6, range(16, 20)),
]

TASKS = {
    0: "Costruisci baseline, ipotesi e manifest di evidenza per un compito LLM scelto.",
    1: "Disegna il percorso dei dati nelle varianti locale, cloud e ibrida e motiva la scelta.",
    2: "Calcola e simula distribuzioni next-token, sorpresa e costo ideale in bit.",
    3: "Ispeziona testo, byte, token e ID e dimostra un round trip senza perdita.",
    4: "Genera e interpreta curve train/validation distinguendo apprendimento, overfitting e leakage.",
    5: "Implementa o calcola scaled dot-product attention e verifica la causalità.",
    6: "Confronta MHA, GQA, MQA, RoPE e MoE collegando ogni tecnica a costo e beneficio.",
    7: "Crea una data card, deduplica un corpus giocattolo e controlla contaminazione degli split.",
    8: "Confronta risposta diretta, scomposizione e tool su problemi verificabili a budget fissato.",
    9: "Seleziona un artefatto locale documentando checkpoint, formato, quantizzazione e licenza.",
    10: "Stima e poi misura pesi, KV cache, TTFT e token/s per configurazioni confrontabili.",
    11: "Interroga Ollama da CLI e API, fissando digest e parametri e gestendo almeno due errori.",
    12: "Confronta strategie di sampling e valida un output strutturato con input non fidato.",
    13: "Costruisci un client conversazionale con adapter, timeout, cancel e test tramite mock.",
    14: "Progetta ed esegui un eval set preregistrato con baseline, soglie e categorie di errore.",
    15: "Costruisci una pipeline RAG con ranking osservabile, citazioni verificabili e test injection.",
    16: "Implementa un tool read-only e una macchina a stati con policy e conferma degli effetti.",
    17: "Motiva prompting/RAG/LoRA su casi dati e misura un adattamento senza contaminare il test.",
    18: "Confronta reference e kernel ottimizzato con test numerici e benchmark sincronizzato.",
    19: "Consegna l'app locale valutata oppure il ramo Pollicino con round trip e costi completi.",
}

EXPECTED = {
    0: "Ipotesi falsificabile, baseline, variabili controllate e distinzione misura/simulazione.",
    1: "Diagramma a strati con trust boundary, dati, rischi e matrice decisionale.",
    2: "Distribuzioni normalizzate, calcoli corretti e spiegazione del limite probabilità/verità.",
    3: "Catena byte-token-ID-embedding e uguaglianza dimostrata tra input e output.",
    4: "Curve annotate, split indipendenti e diagnosi supportata da evidenze.",
    5: "Righe softmax a uno, valori finiti e causal invariance verificata.",
    6: "Confronto quantitativo della KV cache e limiti delle tecniche dichiarati.",
    7: "Data card, hash/deduplica e controllo train-test documentato.",
    8: "Protocollo controllato con accuratezza, token, latenza e failure taxonomy.",
    9: "Scheda con repository, revisione/digest, tokenizer, runtime e licenza.",
    10: "Stime separate dai valori misurati, ripetizioni e margine di memoria.",
    11: "Richiesta riproducibile, risposta validata, timeout e diagnostica priva di segreti.",
    12: "Una variabile cambiata per volta, schema validato e limiti del decoder.",
    13: "Provider sostituibile, mock deterministico e stati di errore/cancel verificati.",
    14: "Dataset versionato, baseline, metrica/soglia preregistrata e report dei fallimenti.",
    15: "Metriche retrieval ed end-to-end, citazioni supportate e injection senza privilegi.",
    16: "Schema, allowlist, least privilege, conferma, idempotenza e audit.",
    17: "Decisione motivata, eval congelato, curve e controllo delle regressioni.",
    18: "Equivalenza entro tolleranza prima dell'accelerazione e protocollo di timing corretto.",
    19: "Artefatti riproducibili; nel ramo lossless uguaglianza byte-per-byte obbligatoria.",
}


def activity_id(index: int, slug: str) -> str:
    return f"llm-activity-m{index:02d}-{slug}"


def module_id(index: int) -> str:
    return f"llm-content-m{index:02d}"


def portable_id(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def build_manifest() -> dict:
    files = ["README.md", *[row[0] for row in MODULES]]
    references = [
        {"id": "llm-ref-course-curriculum", "kind": "curriculum", "role": "coverage-reference", "provider": "school", "title": "Curricolo LLM 2026/27 a doppio livello", "access": "project", "license_status": "reference-only"},
        {"id": "llm-ref-local-ai-manning", "kind": "book", "role": "teacher-reference", "provider": "manning", "title": "Build Applications with Local AI Models (MEAP v6)", "access": "licensed", "license_status": "licensed-reference-only"},
        {"id": "llm-ref-transformer", "kind": "paper", "role": "technical-reference", "provider": "arxiv", "title": "Attention Is All You Need", "uri": "https://arxiv.org/abs/1706.03762", "access": "public", "license_status": "reference-only"},
        {"id": "llm-ref-ollama", "kind": "documentation", "role": "technical-reference", "provider": "ollama", "title": "Ollama documentation", "uri": "https://docs.ollama.com/", "access": "public", "license_status": "reference-and-license-aware-reuse"},
        {"id": "llm-ref-papers", "kind": "bibliography", "role": "technical-reference", "provider": "local", "title": "Timeline ragionata dei paper LLM", "access": "project", "license_status": "project-license"},
    ]
    items = []
    for i, row in enumerate(MODULES):
        filename, _title, topics, _difficulty, _kind, _minutes, slug = row
        refs = [
            {"id": "llm-source-modules", "role": "content-origin", "locator": f"docs/course/modules/{filename}"},
            {"id": "llm-ref-papers", "role": "technical-reference", "locator": "docs/course/research/paper-timeline.md"},
        ]
        if i in {9, 10, 11, 13, 14, 15}:
            refs.append({"id": "llm-ref-local-ai-manning", "role": "teacher-reference", "locator": "indice e concetti pertinenti; nessuna riproduzione"})
        if i == 5:
            refs.append({"id": "llm-ref-transformer", "role": "technical-reference", "locator": "Scaled Dot-Product Attention"})
        if i == 11:
            refs.append({"id": "llm-ref-ollama", "role": "technical-reference", "locator": "API and model management"})
        items.append({
            "id": module_id(i), "kind": "module", "path": f"docs/course/modules/{filename}",
            "order": i + 1, "status": "reviewed", "curriculum_topics": [portable_id(x) for x in topics.split(",")],
            "activity_ids": [activity_id(i, slug)], "source_refs": refs,
        })
    return {
        "schema_version": "thebitlab.content-pack.v1", "id": "llm-pack-2026-2027",
        "title": "LLM 2026/27 — Practitioner e AI Engineer", "version": "0.9.0", "status": "reviewed", "language": "it",
        "audience": {"school_level": "secondaria-secondo-grado-e-formazione-adulti", "subject": "Intelligenza artificiale e LLM", "year": 0},
        "ownership": {"content_origin": "original-course-material", "redistribution_status": "project-license-to-review", "editorial_copying_allowed": False},
        "references": references,
        "sources": [
            {"id": "llm-source-modules", "kind": "source-package", "label": "Dispense originali LLM 2026/27", "type": "markdown", "provider": "local", "role": "approved-course-content", "path": "docs/course/modules", "files": files, "license_status": "project-license-to-review", "indexing_status": "ready"},
            {"id": "llm-source-glossary", "kind": "source-package", "label": "Glossario originale LLM", "type": "markdown", "provider": "local", "role": "approved-course-content", "path": "docs/course/handbook", "files": ["GLOSSARY.md"], "license_status": "project-license-to-review", "indexing_status": "ready"},
        ],
        "coverage": {"path": "content/llm/COVERAGE.md", "status": "reviewed"},
        "content_items": items,
        "course_designs": [{"id": "llm-course-2026-2027", "path": "doc/course_designs/llm_2026_2027.json", "status": "reviewed"}],
        "activity_roots": ["activities/llm"],
        "policies": {"provenance_required": True, "teacher_review_required_before_publish": True, "student_teacher_asset_separation_required": True, "ai_is_not_primary_source": True, "restricted_source_copying_forbidden": True},
    }


def find_uda(index: int) -> str:
    return next(uid for uid, _title, _weeks, indexes in UDAS if index in indexes)


def build_design(manifest: dict) -> dict:
    udas = []
    for uid, title, weeks, indexes in UDAS:
        items = []
        for i in indexes:
            filename, module_title, _topics, _difficulty, _kind, _minutes, slug = MODULES[i]
            items.append({"id": f"item-m{i:02d}", "title": module_title, "source_id": "llm-source-modules", "source": filename, "href": f"docs/course/modules/{filename}", "level": 1, "activity_ids": [activity_id(i, slug)], "frame": {"status": "reviewed", "objectives": f"Raggiungere gli obiettivi osservabili di M{i:02d} ai livelli Practitioner e AI Engineer.", "next_step": "Completare verifica rapida e Activity collegata."}})
        udas.append({"id": uid, "title": title, "path": "docs/course/modules", "weeks": weeks, "items": items})
    projected_sources = [
        {
            key: source[key]
            for key in ("id", "label", "type", "provider", "path", "files", "indexing_status")
            if key in source
        }
        for source in manifest["sources"]
    ]
    return {"schema_version": "1.0", "id": "llm-course-2026-2027", "title": "LLM 2026/27 — Practitioner e AI Engineer", "description": "Percorso annuale a doppio livello con teoria intuitiva, matematica, laboratori locali e capstone Pollicino.", "source_ids": ["llm-source-modules", "llm-source-glossary"], "sources": projected_sources, "years": [{"id": "percorso-annuale", "title": "Percorso annuale 2026/27", "description": "Tronco Practitioner per la classe; approfondimenti AI Engineer per studio avanzato.", "weekly_hours": 2, "weeks": 34, "udas": udas}]}


def build_activity(index: int, row: tuple[str, str, str, str, str, int, str]) -> dict:
    filename, title, topics, difficulty, kind, minutes, slug = row
    aid = activity_id(index, slug)
    compile_required = index in {3, 5, 10, 11, 13, 14, 15, 16, 18, 19}
    return {
        "schema_version": "1.0", "id": aid, "titolo": f"M{index:02d} — {title}", "tipo": kind, "difficolta": difficulty,
        "argomenti": [x.strip() for x in topics.split(",")],
        "consegna": TASKS[index],
        "student_support_mode": "senza-aiuto" if index in {0, 19} else "studio-guidato" if kind == "studio-guidato" else "feedback-tecnico",
        "contesto": {"percorso": "percorso-annuale", "uda": find_uda(index)},
        "content_ids": [module_id(index)],
        "source_refs": [{"source_id": "llm-source-modules", "href": f"docs/course/modules/{filename}"}],
        "assets": [
            {"type": "starter", "path": "student/README.md", "target_path": "README.md", "visibility": "student", "description": "Traccia e checklist consegnate allo studente"},
            {"type": "teacher_only", "path": "teacher/SOLUTION.md", "visibility": "teacher", "description": "Criteri, soluzione e domande per la discussione"},
        ],
        "correzione": {"compila": compile_required, "test": compile_required, "sandbox": compile_required, "ai_feedback": index not in {0, 19}},
        "metriche": {"tempo_stimato_minuti": minutes, "traccia_tempo_dichiarato": True, "traccia_sessioni_thebitlab": True, "traccia_eventi_didattici": True, "traccia_errori_compilazione": compile_required},
        "rubrica": [{"criterio": "Evidenze riproducibili", "punti": 4}, {"criterio": "Spiegazione e decisioni", "punti": 3}, {"criterio": "Correttezza tecnica", "punti": 2}, {"criterio": "Limiti dichiarati", "punti": 1}],
    }


def student_readme(index: int, title: str) -> str:
    return f"""# Activity M{index:02d} — {title}\n\n## Obiettivo\n\nApplica la dispensa M{index:02d} e produci un risultato verificabile.\n\n## Consegna specifica\n\n{TASKS[index]}\n\n## Procedura comune\n\n1. Leggi problema iniziale, teoria Practitioner ed esempio della dispensa.\n2. Completa il livello A–D assegnato; per E–F realizza il prodotto richiesto.\n3. Registra modello/revisione, runtime/versione, parametri, hardware, input e risultato.\n4. Distingui ciò che hai misurato da ciò che stai inferendo.\n5. Consegna artefatto, relazione breve e un limite osservato.\n\n## Evidenza attesa\n\n{EXPECTED[index]}\n\n## Autoverifica\n\n- [ ] Un compagno può ripetere il lavoro con le informazioni fornite.\n- [ ] Non ho inserito dati personali o segreti nei prompt.\n- [ ] Ho confrontato il risultato con una baseline.\n- [ ] Ho indicato almeno un caso in cui la soluzione può fallire.\n"""


def teacher_solution(index: int, title: str) -> str:
    return f"""# Guida docente M{index:02d} — {title}\n\nQuesto file è riservato al docente e non va incluso nello scaffold studente.\n\n## Esito di riferimento\n\n{EXPECTED[index]}\n\nNon esiste un unico testo da copiare: la soluzione è l'insieme di artefatto, misura e motivazione che soddisfa questo criterio.\n\n## Evidenze minime\n\n- artefatto coerente con la consegna specifica;\n- manifest di evidenza completo;\n- confronto con baseline e almeno un caso limite;\n- distinzione esplicita tra misura, simulazione e aspettativa.\n\n## Correzione\n\nUsare la rubrica nell'`activity.json`. Non premiare una demo isolata come capacità generale. Se l'attività usa un modello, la risposta testuale da sola non basta: devono essere dichiarati revisione, template, parametri, runtime e hardware.\n\n## Domande orali\n\n1. Quale decisione cambieresti passando da locale a cloud?\n2. Qual è il principale limite della tua prova?\n3. Quale controllo renderebbe la conclusione più robusta?\n"""


def expected_files(manifest: dict, design: dict) -> dict[Path, str]:
    files = {
        ROOT / "content/llm/content-pack.json": json_text(manifest),
        ROOT / "doc/course_designs/llm_2026_2027.json": json_text(design),
        ROOT / "doc/course_design.json": json_text(design),
    }
    for i, row in enumerate(MODULES):
        _filename, title, _topics, _difficulty, _kind, _minutes, slug = row
        base = ROOT / "activities/llm" / activity_id(i, slug)
        files[base / "activity.json"] = json_text(build_activity(i, row))
        files[base / "student/README.md"] = student_readme(i, title)
        files[base / "teacher/SOLUTION.md"] = teacher_solution(i, title)
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="non scrive; fallisce se gli artefatti divergono")
    args = parser.parse_args()
    manifest = build_manifest()
    design = build_design(manifest)
    mismatches = []
    for path, content in expected_files(manifest, design).items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                mismatches.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if mismatches:
        print("Artefatti TheBitLab non aggiornati:")
        print("\n".join(f"- {item}" for item in mismatches))
        return 1
    print("Content Pack TheBitLab coerente" if args.check else "Content Pack TheBitLab generato")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
