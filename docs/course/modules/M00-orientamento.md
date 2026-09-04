# M00 — Orientamento e baseline

**Domanda guida:** come studiamo un sistema che produce risposte convincenti senza confondere fluidità e conoscenza?
**Durata:** 2 ore Practitioner; 4 ore AI Engineer.
**Prerequisiti:** curiosità, uso elementare del computer e disponibilità a verificare le affermazioni.

## Obiettivi osservabili

Al termine saprai distinguere modello, applicazione e servizio; formulare una previsione verificabile; registrare una baseline; classificare un risultato come misurato, simulato o atteso; applicare regole minime su privacy, copyright e sicurezza. Nel livello AI Engineer saprai inoltre descrivere minacce, variabili di confondimento e limiti di validità di un esperimento.

## Problema iniziale

Due chatbot rispondono correttamente alla stessa domanda. Possiamo concludere che sono equivalenti? No: potrebbero usare modelli diversi, retrieval, strumenti esterni o istruzioni nascoste. Anche a parità di risposta potrebbero differire per costo, latenza, privacy, memoria, licenza e affidabilità su casi nuovi. Il corso parte quindi da una regola: **una demo non è ancora un'evidenza generale**.

## Teoria Practitioner

Un modello linguistico è una funzione parametrica che, dato un contesto, assegna probabilità ai possibili token successivi. L'applicazione decide come raccogliere il prompt, conservare la conversazione, recuperare documenti e mostrare l'output. Il runtime carica ed esegue i pesi. Il servizio aggiunge rete, autenticazione, quote e condizioni economiche. Dire “uso l'AI” nasconde questi livelli e rende impossibile capire che cosa è accaduto.

Una baseline è il punto di confronto più semplice e onesto. Per riassumere un testo può essere “prime tre frasi”; per classificare email può essere la classe più frequente; per Pollicino può essere il file non compresso o un compressore tradizionale. Senza baseline, “funziona bene” non ha significato operativo.

Ogni prova usa il ciclo **domanda → ipotesi → procedura → osservazione → conclusione limitata**. Una misura è prodotta dall'esecuzione reale; una simulazione deriva da un modello esplicito; un'aspettativa è ciò che prevediamo prima della prova. Mescolarle è uno degli errori più comuni nei progetti AI.

## Esempio minimo

Domanda: “Abbassare la temperatura rende identica una risposta locale?” Ipotesi: “con temperatura zero l'output sarà sempre identico”. Procedura: stessa revisione del modello, stesso prompt, stesso template, stessi parametri, cinque esecuzioni. Osservazione: si registrano hash e testi. Conclusione corretta: “nel nostro runtime e hardware, con questa configurazione, le cinque uscite coincidono” oppure “non coincidono”. Non possiamo trasformarla in “tutti gli LLM sono deterministici”.

## Esempio realistico

Devi scegliere un assistente locale per documenti scolastici. Prima stabilisci criteri: nessun dato personale verso cloud, risposta entro 10 secondi, citazioni recuperabili, memoria entro il budget. Poi confronti una baseline senza modello, un modello piccolo e uno più grande sullo stesso set di richieste. Conservi versione, parametri, hardware, dataset e risultati. La scelta finale nasce dai vincoli, non dal modello più famoso.

## Livello AI Engineer: validità dell'esperimento

La variabile indipendente è ciò che modifichi, per esempio la quantizzazione; le variabili dipendenti sono misure come latenza e accuratezza. Tutto il resto dovrebbe rimanere controllato. Se cambi insieme modello, prompt e runtime non puoi attribuire il risultato a una causa.

Definisci prima metrica e soglia. Per una proporzione di successi $\hat p=k/n$, un campione piccolo ha grande incertezza: 9 risposte corrette su 10 non dimostrano un'affidabilità del 90% sul mondo reale. Dataset, campionamento e failure case contano quanto il punteggio medio. Registra sempre semi casuali quando disponibili, commit, dipendenze e condizioni hardware.

Una threat model minima considera dati sensibili nel prompt, output falso o dannoso, dipendenze compromesse, licenze incompatibili, prompt injection e accesso eccessivo a strumenti. Il controllo deve essere proporzionato al rischio: una spiegazione didattica e un agente che può modificare file non possono avere la stessa autonomia.

## Errori frequenti

- Chiamare “modello” l'intera applicazione.
- Scegliere la metrica dopo aver visto il risultato.
- Confrontare prove con prompt, contesto o hardware diversi.
- Conservare soltanto lo screenshot migliore.
- Inserire dati personali, password o documenti riservati nei prompt.
- Trattare sicurezza e licenza come dettagli finali.

## Esercizi A–F

- **A — osserva:** etichetta cinque affermazioni come misura, simulazione o aspettativa.
- **B — modifica:** trasforma “il modello X è migliore” in un'ipotesi verificabile.
- **C — crea:** prepara un manifest di evidenza per una prova riproducibile.
- **D — diagnostica:** trova tre variabili di confondimento in un confronto dato.
- **E — mini-progetto:** confronta una baseline deterministica e un chatbot su dieci esempi.
- **F — prodotto:** definisci protocollo, rischi, criteri di arresto e report per il capstone annuale.

## Laboratorio

Compila la diagnostica iniziale e il template `docs/course/templates/evidence-manifest.json`. Esegui `python3 labs/course_lab.py evidence` e completa i campi mancanti. Non serve ancora installare un modello: lo scopo è imparare a registrare una prova prima di essere affascinati dall'output.

## Verifica rapida

1. Qual è la differenza fra modello e applicazione?
2. Perché una baseline deve precedere il confronto?
3. Una stima di memoria calcolata su carta è misura o simulazione?
4. Che cosa devi mantenere costante per confrontare due quantizzazioni?

Superamento: almeno 3 risposte corrette e un manifest senza ambiguità tra osservato e atteso.

## Sintesi inclusiva

Un LLM genera continuazioni probabili; l'applicazione decide come usarlo. Prima di giudicare un risultato fissa domanda, confronto e misura. Proteggi i dati e limita l'autonomia in base al rischio. Se un compagno non può ripetere la prova, manca ancora un pezzo dell'evidenza.

## Fonti e collegamenti

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Mappa curricolare](../curriculum-map.md)
- [Manifest di evidenza](../templates/evidence-manifest.json)
- Activity: `llm-activity-m00-baseline`

