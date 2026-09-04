# M12 — Sampling e prompting

**Domanda guida:** come controlliamo una distribuzione senza fingere di cambiare il modello?
**Durata:** 3 ore Practitioner; 8 ore AI Engineer.
**Prerequisiti:** M02 e M11.

## Obiettivi osservabili

Saprai spiegare temperature, top-k, top-p, seed, stop e lunghezza; progettare prompt con istruzioni, dati e formato separati; validare output strutturati. Il livello AI Engineer misura entropia, calibrazione e interazioni tra decoder e grammar constraints.

## Problema iniziale

Lo stesso modello produce una poesia creativa e un JSON rigoroso. Non servono necessariamente pesi diversi: prompt, template e decoder cambiano il comportamento. Ma nessun parametro garantisce da solo correttezza.

## Teoria Practitioner

La **temperature** riscalda o concentra la distribuzione. **Top-k** conserva i k candidati più probabili. **Top-p** conserva il più piccolo insieme con massa cumulativa almeno p. Dopo il filtro si rinormalizza e si campiona. Seed e implementazione influenzano la ripetibilità; stop e limite token controllano la terminazione.

Apri [Sampling controls](../../../visuals/sampling-controls-lab.html). Osserva che temperature, top-k e top-p interagiscono: non sono tre manopole indipendenti. Per compiti fattuali o strutturati si parte da bassa variabilità; per esplorazione creativa si può aumentarla e generare più candidati.

Un prompt robusto separa ruolo/obiettivo, input non fidato, vincoli, formato e criteri. Delimitare un documento non lo rende sicuro: il modello può seguire istruzioni contenute nei dati. L'applicazione deve validare e limitare le conseguenze.

## Esempio minimo

Con probabilità `[0,50, 0,25, 0,15, 0,10]`, top-k 2 conserva i primi due; top-p 0,70 conserva anch'esso due elementi perché raggiungono 0,75. Con distribuzioni diverse i due filtri selezionano insiemi differenti.

## Esempio realistico

Vuoi estrarre `nome`, `data` e `importo`. Definisci schema, chiedi JSON senza testo extra, usa structured output se disponibile, valida tipi e campi, rifiuta o riprova con limite. Non inserire direttamente l'output in SQL o in un comando. La validazione è parte della funzione applicativa.

## Livello AI Engineer: decoder e vincoli

Applicare temperature ai logits precede normalmente top-k/top-p, ma dettagli del runtime possono cambiare. Repetition penalty e frequency/presence penalty non sono equivalenti e possono danneggiare codice o dati. Constrained decoding maschera token che renderebbero impossibile completare una grammatica: garantisce sintassi entro il vincolo, non verità dei valori.

Misura diversità con tasso di duplicazione o entropia e qualità con test specifici. La calibrazione confronta probabilità dichiarata e frequenza osservata; i logits degli LLM non sono automaticamente probabilità affidabili di correttezza semantica.

## Errori frequenti

- Usare temperature come “livello di intelligenza”.
- Cambiare più parametri contemporaneamente.
- Credere che JSON valido sia contenuto corretto.
- Inserire dati non fidati dentro istruzioni privilegiate.
- Usare prompt segreti come unico controllo di sicurezza.

## Esercizi A–F

- **A:** applica top-k e top-p a distribuzioni date.
- **B:** modifica un prompt ambiguo separando dati e istruzioni.
- **C:** crea schema e validatore per un output.
- **D:** diagnostica una combinazione che tronca sempre la risposta.
- **E:** costruisci un confronto controllato tra decoder.
- **F:** implementa constrained decoding o un gateway con policy e test avversariali.

## Laboratorio

Usa la visuale e `python3 labs/course_lab.py sampling`. Con modello locale disponibile, esegui una griglia piccola cambiando una sola variabile, conserva output e valuta formato, diversità, correttezza e costo.

## Verifica rapida

Calcola un insieme top-p; spiega temperature contro top-k; progetta un prompt con input non fidato; indica che cosa garantisce e non garantisce una grammatica.

## Sintesi inclusiva

Il decoder sceglie dalla distribuzione prodotta dal modello. Le manopole controllano varietà e terminazione, non aggiungono conoscenza. Prompt chiari aiutano; schema, validazione e limiti rendono l'applicazione affidabile.

## Fonti e collegamenti

- [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751)
- [Visuale sampling](../../../visuals/sampling-controls-lab.html)
- Activity: `llm-activity-m12-sampling`
