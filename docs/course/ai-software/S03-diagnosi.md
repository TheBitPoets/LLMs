# S03 - Diagnosticare difetti e lavorare su codice esistente

## Problema iniziale

Un compagno segnala: «Non riesco a prenotare subito dopo un'altra lezione».
L'agente propone di riscrivere il calendario. Prima di accettare una modifica
ampia, devi capire se il difetto dipende da una regola sbagliata, da un confronto
nel codice o da un dato interpretato male. La segnalazione descrive un sintomo;
la diagnosi deve individuare la causa.

Il debugging assomiglia a un esperimento: formula un'ipotesi, scegli una prova
che possa smentirla e osserva il risultato. Aggiungere modifiche casuali finché
la schermata sembra funzionare rende difficile capire che cosa abbia risolto
il problema e che cosa possa essersi rotto altrove.

## Risultato Practitioner

Sai ridurre una segnalazione a un caso ripetibile, identificare una riga
responsabile e mantenere un test di regressione. Sai anche fermare un ciclo
di correzioni quando non produce nuove evidenze. Il codice esistente viene
prima compreso e caratterizzato, poi cambiato.

## Laboratorio D: una regressione intenzionale

Parti dal risultato R01-R04 di S02. Salva il commit funzionante. In una copia
di lavoro dedicata, il docente reintroduce il confronto inclusivo nella
funzione `overlaps`. È una mutazione didattica di una regola di calendario,
non un test di intrusione. I test esistenti devono rilevarla.

Nei primi 20 minuti riproduci il sintomo, nei successivi 30 scrivi e confronta
due ipotesi. Dedica 30 minuti alla patch e 25 alla regressione; usa gli ultimi
15 per il resoconto. Prima di interrogare l'agente, scrivi che cosa ti aspetti
per 599, 600 e 601 come inizio della seconda prenotazione.

Usa questo incarico:

> Il test sugli intervalli adiacenti fallisce. Riproduci il caso con due
> prenotazioni, confronta il risultato con R02 e identifica la causa minima.
> Proponi una patch limitata. Mantieni i casi di sovrapposizione e mostra
> quali test dimostrano che la correzione non li ha indeboliti.

Leggi la risposta prima di applicarla. Una proposta che elimina il controllo
dei conflitti fa riuscire la richiesta segnalata ma viola l'invariante.
Una proposta che cambia il test per rifiutare gli intervalli adiacenti modifica
il requisito senza averne discusso l'intento.

Ripeti con un secondo difetto scelto dal docente: includere i record cancellati
nel controllo dei conflitti, oppure trattare il retry come una nuova richiesta.
In questo secondo caso la correzione riguarda l'ordine delle verifiche:
prima riconosci l'identità della richiesta, poi cerchi conflitti con altre richieste.

## Esempio minimo: osservazione e spiegazione

![R02: intervalli adiacenti ammessi e confronto inclusivo errato](../../../visuals/static/rendered/booking-intervals.png)

Esplora la [simulazione interattiva](../../../visuals/booking-spec-tests.html)
con inizi alle 09:59, 10:00 e 10:01, prima e dopo la correzione.

Osservazione: «prenotazione 600-660 rifiutata dopo 540-600». Ipotesi A:
il sistema include il minuto finale nel primo intervallo. Ipotesi B:
il sistema rifiuta ogni seconda prenotazione. Prova discriminante: prenota
660-720. Se riesce, B non spiega il comportamento. Hai ristretto la diagnosi
prima di generare altro codice.

Registra il test che prima falliva e ora passa insieme al caso negativo che
continua a fallire nel modo previsto. Non bastano screenshot del messaggio
«risolto» dell'agente. Se fai due tentativi senza migliorare la diagnosi,
torna al requisito e riduci il caso: il budget serve anche a interrompere
una spirale di cambiamenti poco comprensibili.

## Approfondimento software engineer: brownfield e refactoring

In un sistema esistente senza specifiche, un test di caratterizzazione registra
il comportamento attuale. Non dimostra che quel comportamento sia desiderabile.
Scrivi separatamente «oggi accade X» e «il dominio richiede Y», poi negozia
il cambiamento. Mescolare correzioni funzionali e riorganizzazione del codice
nello stesso diff aumenta il lavoro della revisione.

Sperimenta il pattern **characterize, change, compare**: conserva test sul
comportamento rilevante, introduci una modifica piccola, confronta gli esiti.
Se estrai un archivio SQLite in S04, il contratto pubblico diventa il controllo
che il refactoring non abbia cambiato le regole del calendario.

Se l'agente propone una riscrittura, separala in due decisioni: prima la
correzione osservabile, poi l'eventuale refactoring a comportamento invariato.
Misura ampiezza del diff, test toccati e tempo di revisione. Una patch più corta
non è automaticamente migliore, ma rende più semplice attribuire l'esito a una
causa e tornare indietro se compare una regressione.

> **Fonte/ispirazione:** [Vibe Engineering](https://www.manning.com/books/vibe-engineering),
> scheda pubblica, § «what's inside», modernizzazione, validazione e refactoring
> (ispirazione; verificato 2026-09-15).

## Approfondimento AI Engineer: generator e reviewer

Una seconda sessione può rivedere la patch con specifica e test, senza ricevere
la spiegazione persuasiva del primo generatore. Questo riduce una fonte di
condizionamento, ma non rende i due modelli statisticamente indipendenti e
non sostituisce la verifica umana. Confronta difetti trovati, falsi allarmi
e tempo totale di revisione.

Usa una tabella con affermazione del revisore, evidenza, decisione. Accettare
tutti i suggerimenti del reviewer non è più rigoroso che accettare tutto
il codice del generatore. La domanda è sempre quale requisito e quale prova
supportino il cambiamento.

## Verifica e consegna

Consegna sintomo, caso minimo, due ipotesi, prova discriminante, patch e test
di regressione. Spiega perché una correzione apparentemente più semplice è
stata respinta. La visuale sugli intervalli del percorso permette di esplorare
i confini; il codice e i test restano l'evidenza del comportamento reale.
Domanda diagnostica: un test di caratterizzazione che passa autorizza a
conservare per sempre quel comportamento? No: documenta la baseline; la decisione
di prodotto richiede ancora confronto con la specifica.
