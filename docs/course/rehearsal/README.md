# Rehearsal end-to-end

Il contenuto del corso può essere controllato automaticamente qui; le
affermazioni su Ollama richiedono invece una macchina reale supportata.

## Profilo prioritario

- MacBook Apple Silicon M4 Pro, 36 GB unified memory;
- versione macOS e Ollama registrate al momento della prova;
- un modello 4B–9B quantizzato scelto dal catalogo corrente;
- rete attiva solo per il pull, poi prova offline.

## Sequenza

```bash
git rev-parse HEAD
python3 -m unittest discover -s tests -v
python3 labs/course_lab.py system --output evidence/system.json
ollama --version
ollama pull '<tag>'
ollama show '<tag>'
python3 labs/course_lab.py ollama --model '<tag>' --prompt 'Rispondi solo: OK' --output evidence/smoke.json
python3 labs/course_lab.py benchmark --model '<tag>' --output evidence/benchmark.json
ollama ps
```

`--output` è accettato sia prima sia dopo il sottocomando; nei comandi sopra è
posto dopo per rendere più leggibile la sequenza del laboratorio.

## Gate

- tutti i test automatici passano sul commit;
- modello/digest/licenza/quantizzazione sono registrati;
- smoke online e offline passano senza dati personali;
- server spento e tag errato producono errori comprensibili;
- benchmark conserva prompt, conteggi e timing senza dichiarare qualità;
- un laboratorio M14 confronta baseline e almeno due configurazioni;
- docente annota difetti, tempo reale e modifiche necessarie.

Fino a questo rehearsal, lo stato è **contenuto completo, validazione hardware
pendente**, non “pronto in ogni classe”. Non creare il tag `course-v1` prima
del gate.
