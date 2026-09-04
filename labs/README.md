# Laboratori eseguibili

Il kit base usa solo Python 3.11+ e non richiede credenziali. Ogni comando
produce JSON su stdout; con `--output report.json` salva lo stesso evidence
report. I comandi `ollama` e `benchmark` richiedono un servizio Ollama locale.

```bash
python3 labs/course_lab.py system
python3 labs/course_lab.py softmax --logits 2.1 1.25 0.9 0.25 --temperature 0.8
python3 labs/course_lab.py bytes --text "Caffè 🤖"
python3 labs/course_lab.py gradient --steps 12
python3 labs/course_lab.py attention
python3 labs/course_lab.py memory --parameters 4 --bits 4 --context-k 8 --available 16
python3 labs/course_lab.py sample --seed 7 --draws 100
python3 labs/course_lab.py evaluate --predictions labs/fixtures/predictions.jsonl
python3 labs/course_lab.py rag --query "Perché serve una baseline?"
python3 labs/course_lab.py agent --request "CALCOLA: (12 + 8) / 5"
python3 labs/course_lab.py pollicino --message ABAAB
python3 labs/course_lab.py ollama --model '<tag-verificato>' --prompt 'Rispondi solo: OK'
python3 labs/course_lab.py benchmark --model '<tag-verificato>'
```

## I dodici laboratori minimi

| Lab | Moduli | Artefatto | Baseline / test negativo |
| --- | --- | --- | --- |
| L00 System manifest | M00 | OS, Python, CPU e memoria | Campi mancanti. |
| L01 Softmax | M02 | Probabilità e surprisal | Logit molto grande, temperatura non valida. |
| L02 Byte report | M03 | Caratteri/code point/UTF-8 | Accenti, emoji e stringa vuota. |
| L03 Gradient | M04 | Curva parametri/loss | Learning rate nullo o eccessivo. |
| L04 Attention | M05 | Score, pesi e output | Token futuro mascherato. |
| L05 Memory planner | M10 | Stima pesi/overhead/fit | Modello senza margine. |
| L06 Sampling | M12 | Frequenze per seed | Greedy e distribuzione troncata. |
| L07 Evaluation | M14 | Accuracy per categoria/errori | Baseline inclusa nelle fixture. |
| L08 Tiny RAG | M15 | Ranking e citazioni | Query senza evidenza. |
| L09 Safe tool | M16 | Decisione, schema e risultato | Codice/nomi/chiamate rifiutati. |
| L10 Pollicino | M02/M19 | Intervallo, bit, round trip e SHA-256 | Stream corrotto/messaggio non A-B. |
| L11 Ollama + benchmark | M11/M13/M18 | Manifest, risposta e timing | Servizio spento/tag errato/timeout. |

## Modalità studente e docente

La consegna studente è nella pagina del modulo e non contiene valori attesi.
La [guida docente](../docs/course/teacher/lab-guide.md) contiene criteri,
failure injection e controlli. Non raccogliere prompt personali: usare fixture
del repository o testi creati per il laboratorio.

## Test

```bash
python3 -m unittest discover -s tests -v
```

Il test di unità non contatta Ollama. Il rehearsal hardware è separato perché
deve registrare il modello e la macchina realmente usati.

