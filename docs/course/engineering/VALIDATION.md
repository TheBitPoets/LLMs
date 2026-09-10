# Verifica dell'incremento engineering - 10 settembre 2026

Ambiente: Python 3.12.14, PyTorch 2.8.0+cpu, CPU x86_64.
Questo verbale riguarda codice e materiali; non chiude il rehearsal Mac/Ollama.

## Esiti

- Suite completa: **65 test superati**, inclusi casi negativi HTTP, citazioni,
  tool, MCP, causalità, cache, LoRA, corruzione e round trip.
- Export studente M19: copiati solo gli asset dichiarati per lo studente in
  una directory temporanea esterna al repository; MCP e training funzionano
  senza file docente o dipendenze implicite dal checkout autore.
- Training reale: 160 passi base e 120 adapter, checkpoint scelti su validation,
  report e piccoli pesi originali conservati in `output/engineering`.
- Inferenza: equivalenza prima del timing, sette ripetizioni dopo due warm-up,
  tempi individuali, mediana e memoria dei tensori KV conservati nel report.
- Codec: otto round trip misurati su quattro tipi di input, due predittori;
  ulteriori casi esaustivi e di corruzione nella suite automatica.
- Struttura: 20 moduli, 20 Activity LLM, 8 capitoli engineering, 6 lezioni
  software, 11 visuali interattive e 9 figure statiche; link locali validi.
- PDF: **114 pagine studente, 132 docente**, header/xref/EOF validi, lettura
  strict e stream/testo di ogni pagina verificati, capitoli E00-E07 e S00-S05
  presenti, apparati riservati assenti dal PDF studente. Render Poppler
  ispezionati per formule, figura, esempi CLI e soluzioni; corrette due righe
  che superavano il margine. Nessun contenuto tagliato nei campioni ispezionati.

## Contratto TheBitLab

Usato il validatore canonico dal checkout TheBitLab alla revisione
`736bbfddfb79e431b9dedbfd1d877f06aa8b02b5`:

```bash
python3 -m scripts.content_pack_contract validate \
  /percorso/LLMs/content/llm/content-pack.json \
  --root /percorso/LLMs
python3 -m scripts.validate_activity \
  /percorso/LLMs/activities/llm/*/activity.json
```

Entrambi superati. Passare esplicitamente i manifest `activity.json` al secondo
comando: le fixture JSON degli esempi sono dati, non manifest Activity.
Il Course Design conserva 34 settimane × 2 ore e proietta le fonti engineering;
`TEACHER.md` non è incluso nei file indicizzabili.

## Ripetizione locale

```bash
python3 scripts/scaffold_thebitlab_pack.py --check
python3 scripts/scaffold_ai_software_pack.py --check
python3 scripts/check_course.py
python3 scripts/check_pdfs.py
python3 -m unittest discover -s tests -v
```

Le misure CPU non provano qualità di un modello Ollama, compatibilità di ogni
tag o prestazioni sul Mac. La generazione libera del tiny LM è imperfetta,
l'adapter regredisce sul dominio base e il codec non batte gzip nei casi
misurati. I gate di revisione docente, rehearsal e freeze rimangono nello
[stato di rilascio](../release-status.md).
