# M01 - Mappa dell'ecosistema

**Domanda guida:** che differenza c'è tra modello, prodotto, runtime e applicazione?  
**Durata:** 2 ore Practitioner; 4 ore AI Engineer.  
**Prerequisiti:** M00.

## Obiettivi osservabili

Classificare correttamente almeno otto componenti; tracciare il viaggio di un
prompt; confrontare locale e cloud su privacy, rete, qualità, costo e controllo.
L'AI Engineer documenta API boundary, trust boundary e lifecycle delle versioni.

## Lezione intuitiva

La metafora musicale è utile se ne dichiariamo il limite: i **pesi** sono lo
spartito appreso; il **runtime** è l'esecutore meccanico; il **tokenizer** decide
come leggere i simboli; il **template** organizza i turni; l'**app** raccoglie
input e mostra output; un **provider** offre calcolo e contratti. Nessun pezzo,
isolato, coincide con il prodotto completo.

Aprire la visuale [Dove viaggia il prompt?](../../../visuals/local-vs-cloud-data-journey.html).
Seguire appunti personali e contenuto pubblico. Locale non significa
automaticamente sicuro: un'app locale può chiamare ricerca web o telemetria.
Cloud non significa automaticamente migliore: qualità e costo dipendono dal
task e dal modello disponibile.

## Laboratorio

Disegnare due data-flow dello stesso caso d'uso, uno con Ollama e uno con API.
Per ogni freccia indicare: dato, protocollo, proprietario, conservazione e
possibile errore. Baseline: risposta manuale senza LLM. Test negativo:
disabilitare la rete nel percorso dichiarato offline e osservare cosa fallisce.

## Estensione AI Engineer

Definire component diagram e sequence diagram; separare control plane e data
plane; indicare alias mobili e ID versionati dei modelli. Produrre un threat
model STRIDE leggero per prompt, documenti recuperati e tool output.

## Verifica

Dato un diagramma con Chat UI, Ollama, GGUF, tokenizer e modello remoto, lo
studente etichetta ogni ruolo e corregge tre confini errati. Rubrica 10 punti:
ruoli 4, viaggio dati 2, trade-off 2, test offline 2. Fonti: documentazione
[Ollama](https://docs.ollama.com/) e cataloghi ufficiali nello snapshot del corso.

