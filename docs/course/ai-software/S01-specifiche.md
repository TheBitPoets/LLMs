# S01 - Dalla richiesta alla specifica verificabile

## Problema iniziale

«Gestisci correttamente le prenotazioni» non dice che cosa fare con una
durata zero o con una richiesta ripetuta. Anche «nessuna sovrapposizione»
lascia aperto il caso degli intervalli consecutivi. La specifica serve a
rendere queste scelte esplicite prima che diventino decisioni accidentali del codice.

Per la classe la specifica è un accordo scritto con esempi: come le regole
di un gioco che permettono di risolvere una discussione durante una partita.
L'analogia smette di essere sufficiente quando il dominio cresce: in un
sistema reale ci sono requisiti incompatibili, eccezioni e costi da negoziare.

## Risultato Practitioner

Sai scrivere una regola osservabile, scegliere esempi ai confini e collegare
un test alla regola. Parti dal contratto v1 fornito: il primo esercizio non
chiede di inventare ogni decisione, ma di capire perché quelle decisioni
servono. La variante successiva verrà invece progettata da te.

Una specifica utile contiene scopo, esclusioni, termini, invarianti, esempi,
errori e criteri di completamento. L'invariante qui è: nessuna coppia di
prenotazioni attive della stessa aula occupa minuti in comune. Gli ID R01-R06
permettono di discutere e tracciare le regole senza dipendere dal numero di riga.

## Laboratorio B: modifica una regola senza perdere il controllo

Nei primi 25 minuti leggi R01-R06 e traduci 540 e 600 in orari. Nei successivi
25 scrivi esempi con input e risultato atteso. Dedica 30 minuti alla revisione
con un compagno o un agente, 25 alla variante e 15 alla restituzione.

Per R02 prepara tre casi: intervalli sovrapposti, adiacenti e stessa fascia
in due aule diverse. Per R03 considera l'apertura alle 08:00, la chiusura
alle 18:00 e la durata massima di tre ore. «Input sbagliato» va precisato:
deve essere rifiutato e lo stato deve rimanere invariato.

Chiedi all'agente di agire come revisore della specifica:

> Controlla R01-R06. Per ogni regola cerca un caso limite e un possibile
> conflitto con un'altra regola. Non cambiare i requisiti e non scrivere codice.
> Restituisci una tabella requisito, caso, risultato previsto, dubbio residuo.

Decidi quali osservazioni accettare e perché. Un agente può suggerire di
aggiungere login, email o un calendario completo: sono nuove funzionalità,
da valutare rispetto allo scopo. La richiesta non autorizza ad ampliare il
prodotto ogni volta che viene in mente una possibilità.

La variante B porta la durata massima da 180 a 120 minuti. Scrivi una breve
richiesta di modifica con motivazione e nuovi casi: 120 minuti ammessi,
121 rifiutati. Elenca i test e i documenti coinvolti. **Non applicare la variante
al contratto condiviso della classe**: consegnala come proposta separata,
così S02 può usare la baseline comune v1. Il docente può adottarla in un branch
dedicato per un'esercitazione successiva.

## Esempio minimo: Given, When, Then

Given LAB-A prenotata dalle 09:00 alle 10:00; When chiedo LAB-A dalle 10:00
alle 11:00; Then la richiesta riesce e ci sono due prenotazioni attive.
Spostare l'inizio alle 09:59 cambia l'esito: la richiesta fallisce e lo stato
contiene ancora una sola prenotazione. Un minuto basta a distinguere due
interpretazioni che una descrizione generica confonde.

Gli esempi non coprono automaticamente tutte le combinazioni. Sono un ponte
fra accordo umano e test eseguibili. Chi implementa deve anche riconoscere
la regola generale, altrimenti potrebbe codificare solamente i casi mostrati.

## Approfondimento: sviluppo guidato dalle specifiche

Nel lavoro guidato dalle specifiche si versionano insieme intento, piano,
test e implementazione. Una modifica al comportamento inizia aggiornando
l'accordo; la revisione verifica che il diff realizzi proprio quel cambiamento.
Non basta chiamare un file `spec.md` per ottenere questo risultato.

L'ingegnere del software aggiunge una matrice R01-R08 → test → componente,
una decisione architetturale breve e una procedura per modificare le regole.
L'AI Engineer aggiunge esempi di output formalmente valido ma semanticamente
errato: «LAB-B» al posto di «LAB-A» passa lo schema JSON, ma non soddisfa la richiesta.

Strumenti come GitHub Spec Kit e OpenSpec possono organizzare gli artefatti
di questo processo. Il laboratorio parte da file semplici per rendere visibili
le decisioni. Come estensione, importa la stessa piccola funzionalità nello
strumento scelto e confronta documenti prodotti, manutenzione e tracciabilità;
consulta il suo README corrente per installazione e comandi. Non presumere
che template differenti abbiano lo stesso significato.

## Verifica e consegna

Consegna sei esempi nuovi, la proposta della variante B e la matrice di
tracciabilità iniziale. Un compagno deve poter decidere l'esito di ogni esempio
senza chiederti spiegazioni. Domanda diagnostica: se codice e test concordano
ma contraddicono una regola approvata, che cosa è sbagliato? L'implementazione
e i test possono condividere lo stesso errore; occorre tornare all'intento e
chiarirlo, non approvare il cambiamento solo perché la suite è verde.
