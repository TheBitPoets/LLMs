# LLM 2026/27 — Content Pack TheBitLab

Questa directory contiene il manifest di authoring conforme a
`thebitlab.content-pack.v1` e la matrice di copertura. Le dispense canoniche
sono in `docs/course/modules/`: il manifest le espone come source Markdown
indicizzabile senza crearne una seconda copia.

Il pack collega quattro contratti distinti:

- contenuti e provenienza: `content/llm/content-pack.json`;
- copertura: `content/llm/COVERAGE.md`;
- calendario e composizione: `doc/course_designs/llm_2026_2027.json`;
- proiezione leggibile: `doc/PERCORSO_DIDATTICO.md`;
- attività eseguibili o valutabili: `activities/llm/*/activity.json`.

Lo stato `reviewed` indica che struttura, collegamenti e controlli automatici
sono completi. Il passaggio ad `approved` richiede revisione esplicita del
docente e rehearsal sull'hardware dichiarato.

## Comandi

```bash
python3 scripts/scaffold_thebitlab_pack.py --check
python3 scripts/check_course.py
python3 scripts/build_handbook.py
```

La conformità al validatore canonico va inoltre verificata dal checkout di
TheBitLab:

```bash
python -m scripts.content_pack_contract validate \
  /percorso/LLMs/content/llm/content-pack.json --root /percorso/LLMs
```
