# Guida docente M00 — Orientamento e baseline

Riservato al docente.

## M00 - Baseline e domanda verificabile

Una buona consegna è «estrarre aula e ora da dieci avvisi sintetici, almeno
otto corretti, zero aule inventate». La baseline può essere una ricerca per
espressione regolare; confrontarla con LLM solo sugli stessi dieci avvisi.
Un report corretto separa dati di preparazione e valutazione, registra la
versione e conserva gli errori. «Il modello capisce la scuola» non è una
conclusione misurabile. Chiedere allo studente quale esempio metterebbe in
crisi la baseline: un'aula scritta in lettere è un caso pertinente.
Il comando `python3 labs/course_lab.py system` registra l'ambiente, ma non
dimostra alcuna prestazione del modello. Accettare esplicitamente «non misurato»
nei campi che richiedono Ollama; non accettare valori inventati per completarli.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
