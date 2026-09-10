# PrenotaLab: contratto v1

Scopo: prenotare LAB-A e LAB-B in una sola giornata scolastica sintetica.
I minuti si contano da mezzanotte: 540 = 09:00, 600 = 10:00.
I dati sono inventati. Utenti, date, fusi orari, login e deployment non fanno
parte di questo esercizio. Non presentare il prototipo come servizio scolastico operativo.

## Requisiti e accettazione

- **R01** `reserve(request_id, room, start, end)` restituisce un `Booking`
  immutabile con questi quattro campi e `cancelled=False`.
- **R02** due prenotazioni attive della stessa aula non si sovrappongono.
  Gli intervalli sono `[start, end)`: 09:00-10:00 e 10:00-11:00 sono compatibili.
  Aule diverse sono indipendenti. Un conflitto solleva `ValueError`.
- **R03** gli ID sono stringhe non vuote dopo `strip()`, lunghe al massimo
  64 caratteri; il valore originale è conservato (nessuna normalizzazione).
  Aula in {LAB-A, LAB-B}. Start/end sono `int` (esclusi bool), tra 480 e 1080,
  con `start < end` e durata massima 180 minuti. Dati invalidi sollevano
  `ValueError`; ogni errore lascia lo stato invariato.
- **R04** stessa chiave e stessi dati restituiscono la prenotazione nello
  stato corrente senza duplicare effetti. Stessa chiave e dati diversi
  sollevano `ValueError`, anche se la precedente prenotazione è cancellata.
- **R05** `cancel(request_id)` marca la prenotazione cancellata e libera
  l'aula. Ripeterla restituisce lo stesso risultato. ID sconosciuto:
  `KeyError`. Ripetere la richiesta originaria dopo la cancellazione
  restituisce il record cancellato: non lo riattiva.
- **R06** `list_active()` restituisce solo record attivi ordinati per
  `(start, room, request_id)`, senza consentire di modificare lo stato interno.

## Esempi che fissano il significato

Given LAB-A occupata da 540 a 600, when prenoto LAB-A da 600 a 660,
then ottengo una seconda prenotazione attiva.

Given la stessa situazione, when prenoto LAB-A da 599 a 660,
then ricevo ValueError e rimane una sola prenotazione.

Given r1 cancellata, when ripeto r1 con gli stessi dati,
then ricevo r1 cancellata e nessuna prenotazione attiva viene creata.

## Estensione software engineer (contratto v2)

- **R07** lo stesso servizio deve accettare un archivio in memoria oppure
  SQLite senza cambiare le regole R01-R06; i dati SQLite sopravvivono alla riapertura.
- **R08** controllo del conflitto e inserimento sono atomici anche tra
  due istanze SQLite sullo stesso file. Due richieste sovrapposte concorrenti
  non possono entrambe riuscire. Non basta un test sequenziale per dimostrarlo.

## Definition of done del laboratorio

Requisiti tracciati ai test; test pubblici invariati; almeno due casi aggiunti
indipendentemente dal generatore; diff spiegato; limiti e comandi nel README;
revisione umana dei cambiamenti. Il nome del modello non costituisce evidenza
di correttezza. I test sono esempi finiti, non una prova di tutti i comportamenti.
