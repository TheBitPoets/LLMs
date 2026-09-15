# S02 - Implementare una porzione e verificarla

## Problema iniziale

Delegare «completa tutta l'app» produce spesso un diff difficile da leggere.
Se cambiano insieme struttura, nomi, regole e test, non è facile capire perché
una prenotazione prima riuscisse e ora fallisca. Il laboratorio limita il
primo incarico a una porzione completa del comportamento: prenotare, controllare
i dati e rilevare i conflitti.

Immagina una fetta di torta che attraversa tutti gli strati: una piccola
funzione utile deve collegare requisito, codice e verifica. Scrivere soltanto
tutte le classi vuote equivale a preparare uno strato isolato: non dimostra
ancora che l'utente possa completare un'azione.

## Risultato Practitioner

Sai chiedere una patch circoscritta, verificare un test che fallisce prima e
passa dopo, e spiegare il cambiamento. La prima porzione realizza R01-R03;
la seconda aggiunge R04. R05-R06 vengono completati nel mini-progetto S04.
Finché ci sono requisiti mancanti, la suite completa può correttamente restare rossa.

Usa il branch creato nello starter. Prima leggi i test R01-R03 e annota gli
esiti attesi senza l'aiuto dell'agente. Conserva i test pubblici: sono parte
del contratto didattico. Se ritieni un test errato, apri una discussione sulla
regola, invece di modificarlo per ottenere il verde.

## Laboratorio C: un incarico con criteri di uscita

Dedica 20 minuti al piano, 40 alla prima porzione, 30 all'idempotenza e 30
alla revisione. Puoi iniziare con questa richiesta:

> Implementa soltanto R01-R03 in booking.py. Mantieni le firme pubbliche,
> usa solo la libreria standard e non cambiare i test forniti. Prima indica
> quali funzioni toccherai. Dopo mostra il diff e l'esito dei test eseguiti.
> Elenca separatamente i requisiti ancora mancanti.

Dopo la modifica esegui i test e leggi il diff con `git diff`. Verifica che
la soluzione controlli i dati prima di modificare lo stato. Aggiungi tu un
caso non suggerito dall'agente: una prenotazione che finisce esattamente
alle 18:00 oppure un intervallo completamente contenuto in uno già occupato.

Per R04 prepara prima un esempio di retry: la richiesta r1 può arrivare
due volte perché l'interfaccia non ha ricevuto la risposta del primo invio.
Il risultato deve essere lo stesso record, non una seconda prenotazione
e neppure un errore di conflitto. Chiedi una seconda patch solo per questa regola.
Poi riusa r1 cambiando aula: ora il sistema deve rifiutare la richiesta.

Non occorre chiedere pensieri interni al modello. Sono sufficienti un piano
breve, riferimenti al codice, scelte verificabili ed esiti dei comandi.
Una spiegazione molto lunga non aumenta da sola la qualità della patch.

### Il ciclo dell'incremento comprensibile

Per ogni incarico usa sempre la stessa scheda: **intento -> confine -> prova
rossa -> modifica minima -> prova verde -> lettura del diff -> decisione**.
Il confine dichiara file e comportamento ammessi; la decisione dice se tenere,
correggere o scartare la patch. Se non riesci a descrivere il cambiamento in
tre frasi, riduci l'incarico prima di continuare. Questo rende confrontabili
anche sessioni svolte con agenti differenti.

> **Fonte/ispirazione:** [Vibe Engineering](https://www.manning.com/books/vibe-engineering),
> scheda pubblica, § «about the book», piccoli incrementi comprensibili
> (ispirazione; verificato 2026-09-15).

Non accumulare cinque patch non lette. Dopo ogni incremento salva nel report
comando, esito e una riga sul rischio residuo. Un test verde autorizza il passo
successivo solo per il contratto che quel test riesce davvero a osservare.

> **Fonte/ispirazione:** [Vibe Engineering](https://www.manning.com/books/vibe-engineering),
> scheda pubblica, § «Vibe Engineering also shows you...» su test e miglioramento
> (ispirazione; verificato 2026-09-15).

## Esempio minimo: un test che può smentire il codice

Se il codice usa `a_start <= b_end`, il caso 540-600 seguito da 600-660
fallisce. Con la regola semichiusa serve un confronto stretto. Prima del
cambiamento il test segnala il disaccordo; dopo deve passare. Aggiungi anche
599-660, che deve continuare a essere rifiutato: una correzione che accetta
tutto renderebbe verde il primo esempio e violerebbe comunque R02.

Questo è il valore del ciclo **test fallisce, modifica minima, test passa,
riordina preservando il comportamento**. Non tutti i test devono necessariamente
essere scritti prima del codice, ma ogni requisito importante deve avere
un controllo capace di rilevarne una violazione.

## Approfondimento per gli ingegneri

Il pattern **functional core / imperative shell** separa calcoli deterministici
da letture e scritture. `overlaps` restituisce un booleano e non modifica
archivi; il servizio decide quando salvare. Si può così verificare la funzione
con molte combinazioni senza avviare un server o interrogare un LLM.

Il software engineer controlla anche che le modifiche non alterino API o
ordinamento dei risultati senza una nuova specifica. Mantiene commit piccoli
con messaggi che spiegano il cambiamento osservabile. Non misura il progresso
contando righe generate: meno codice può soddisfare meglio lo stesso contratto.

L'AI Engineer ripete un solo incarico su due configurazioni, partendo ogni
volta dallo stesso commit. Conserva prompt, contesto, diff, tempo di revisione
e numero di tentativi. Fissa prima il budget, per esempio 15 minuti e due
cicli di correzione. Il tempo speso a verificare e correggere fa parte del costo,
anche quando la risposta del modello arriva in pochi secondi.

## Verifica e consegna

Consegna due patch leggibili, i test iniziali e finali, un caso aggiunto da te
e l'elenco R05-R06 ancora da implementare. Devi saper indicare il punto in cui
lo stato cambia e spiegare perché un errore non deve lasciare metà operazione.
Domanda diagnostica: perché un test scritto dallo stesso agente che genera
il codice potrebbe essere insufficiente? Può condividere la stessa interpretazione
errata; servono casi ricavati dalla specifica e una revisione indipendente.
