# S04 - Pattern applicativi, adapter e confini

## Problema iniziale

Ora il calendario sa prenotare, ma deve anche cancellare e ordinare gli
incontri attivi. In seguito potrebbe salvare su disco o ricevere richieste
in linguaggio naturale. Se ogni novità viene aggiunta alla stessa funzione,
diventa difficile distinguere le regole del dominio dal modo di leggere e
scrivere i dati.

Un adapter è come una presa che collega dispositivi diversi rispettando una
stessa interfaccia. La somiglianza riguarda il confine: una presa non stabilisce
il programma da eseguire, e un archivio non dovrebbe inventare le regole di
prenotazione. Il nome del pattern è utile solo se chiarisce una responsabilità.

## Risultato Practitioner

Completi R05-R06 e ottieni un piccolo prodotto funzionante in memoria.
Riconosci tre parti: dati della prenotazione, regole del servizio, archivio.
Sai spiegare perché ripetere una cancellazione non deve duplicare effetti
e perché un elenco restituito non deve consentire di modificare lo stato interno.

## Laboratorio E: completa il servizio

Dedica 20 minuti agli esempi di cancellazione, 40 all'implementazione con
l'agente, 35 ai test e 25 alla mappa dei componenti. Parti dal tuo lavoro
di S02-S03, non dalla soluzione docente.

Chiedi due modifiche separate. Prima implementa `cancel`: record attivo →
cancellato; secondo invio → stesso record cancellato; ID sconosciuto → KeyError.
Poi implementa `list_active` e il suo ordinamento. Verifica il caso in cui
un vecchio retry arriva dopo la cancellazione: R04 richiede il record nello
stato corrente, quindi non deve riaprire la prenotazione.

La rubrica premia il comportamento e la spiegazione. Per la classe non è
necessario introdurre Protocol, database o un framework per agenti. Prima
fai funzionare i nove test pubblici, poi aggiungi un caso di ordinamento con
due aule e lo stesso orario e un caso di cancellazione ripetuta.

## Esempio minimo: chi decide?

L'utente dice «LAB-A dalle nove alle dieci». Un LLM può suggerire:

```json
{"room": "LAB-A", "start": 540, "end": 600}
```

Il parser controlla i campi;
la persona verifica che corrispondano alla richiesta; il servizio controlla
se l'aula è libera. Sono tre controlli diversi. Se LAB-A è occupata, il modello
non può rendere valida la prenotazione dichiarandola disponibile.

Una normale app può essere realizzata con l'aiuto di un coding agent senza
contenere alcun LLM. Aggiungere un LLM nel prodotto è una decisione distinta,
con nuovi errori possibili e un costo da valutare rispetto a un semplice modulo.

## Ramo software engineer: ports and adapters, altre 3 ore

Definisci il contratto di un archivio: transazione, elenco dei record e
salvataggio. Il servizio riceve l'archivio dall'esterno: questa è dependency
injection. Implementa un archivio in memoria e uno SQLite; esegui gli stessi
test R01-R06 su entrambi. Aggiungi riapertura del file e verifica R07.

Per R08 disegna la sequenza di due richieste contemporanee. Senza atomicità,
entrambe possono leggere «aula libera» prima che una delle due scriva.
La soluzione di riferimento usa `BEGIN IMMEDIATE` intorno a controllo e
scrittura, con una connessione per thread. Il test concorrente avvia due
istanze sullo stesso file e richiede un successo e un conflitto. Un test
sequenziale non osserva questa interleaving; un singolo test concorrente
riuscito non prova tutte le condizioni operative di un database reale.

Scrivi un'ADR di una pagina: decisione, alternative, motivazione, conseguenze.
Per questo prototipo SQLite è sufficiente; introdurre microservizi avrebbe
un costo da giustificare. Prima di dichiarare produzione restano nuovi requisiti
su utenti, date, accesso, migrazione e gestione operativa.

## Ramo AI Engineer: adapter LLM e valutazione, altre 3 ore

Esegui `proposal.py` dal kit con un modello Ollama installato. Il programma
usa lo schema JSON nella richiesta e valida localmente campi, tipi e intervallo.
Restituisce solo una bozza. Il test con risposta simulata dimostra il contratto
dell'adapter, non la capacità del modello di capire gli orari.

Prepara dodici richieste sintetiche: quattro chiare, quattro parafrasi e quattro
ambigue o incomplete. Fissa i risultati attesi prima di interrogare il modello.
Per le ambigue, una scelta inventata conta come errore anche se il JSON passa
il parser. L'adapter minimo non possiede uno stato «chiedi chiarimento»: misura
questa limitazione e progetta una revisione dello schema con decisione
`proposal` oppure `clarify`. Implementala in un branch e aggiungi test specifici.

Confronta con un modulo manuale a tre campi e con una risposta simulata.
Misura validità strutturale, correttezza semantica, richieste di chiarimento
appropriate, tempo e correzioni umane. Se il LLM non migliora l'esperienza
sul compito, mantenere il modulo è una decisione ingegneristica valida.

## Verifica e consegna

La classe consegna R01-R06 verdi e un diagramma dei componenti. Il software
engineer aggiunge adapter, ADR, persistenza e prova concorrente. L'AI Engineer
aggiunge dataset, risultati reali datati e almeno un output formalmente valido
ma sbagliato. Domanda diagnostica: lo schema JSON può verificare che l'aula
richiesta dall'utente sia quella desiderata? Da solo no: struttura e significato
richiedono valutazioni differenti.
