# Guida docente: PrenotaLab e coding agent

Materiale di riferimento per correzione e discussione. Nel Content Pack
questo testo e la soluzione Python sono asset docente; non vengono inclusi
nello starter esportato. Il repository pubblico rimane accessibile: per una
prova sommativa predisporre una variante non pubblicata.

## S00 - Baseline e mappa del repository

Nello starter `Booking` rappresenta i dati; `BookingService.reserve` controlla
solo un conflitto e aggiunge una riga; `overlaps` usa erroneamente confronti
inclusivi. `cancel` non è implementato e `list_active` conserva l'ordine di
inserimento. Mancano validazione e idempotenza. I casi happy path, conflitto
effettivo e due aule diverse passano; adiacenza, validazione, retry, riuso ID,
cancellazione e ordinamento espongono le lacune.

La mappa corretta collega R02 a `overlaps` e al test di adiacenza; R04 a
`reserve` e ai due test sul request_id; R05 a `cancel`. Respinge una risposta
dell'agente che dichiari presenti un database o un endpoint HTTP nello starter.
Per chi fatica con il codice, usare tre schede cartacee: stato prima, richiesta,
stato dopo. Questo supporto mantiene osservabile lo stesso risultato didattico.

Evidenza minima: output originale, tre collegamenti corretti e una deduzione
separata da una misura. La domanda sul documento obsoleto verifica che lo
studente attribuisca il difetto al contesto, senza invocare automaticamente
un modello più grande. Non richiedere un account cloud per superare questa fase.

## S01 - Soluzione degli esempi e variante

Esempi v1: LAB-A 540-600 poi 600-660 è ammesso; 599-660 è rifiutato;
LAB-B 540-600 è indipendente. 480-660 dura 180 ed è ammesso; 480-661
è rifiutato. 900-1080 è ammesso; 900-1081 è fuori orario.
Durata zero è rifiutata senza cambiare l'archivio.

Per la variante 120 minuti, R03 passa a durata massima 120; i test nuovi
devono ammettere 480-600 e rifiutare 480-601. La proposta deve identificare
specifica, validazione del servizio, test dei confini e documentazione; nel
ramo LLM anche il parser usa lo stesso limite e va aggiornato. La variante
rimane separata dal contratto v1 condiviso finché il docente non l'adotta.

Matrice minima: R01→happy path→reserve; R02→adiacenza/conflitto/aule→overlaps
e reserve; R03→validazione senza effetti→reserve; R04→retry/ID in conflitto→reserve;
R05→cancel e retry successivo→cancel/reserve; R06→ordinamento→list_active.
Assegnare credito alle decisioni motivate, non alla lunghezza della specifica.

## S02 - Patch attesa e test indipendenti

La soluzione in `labs/ai_software/reference/booking.py` usa confronti stretti
per l'intersezione. Valida ID, aula, tipi e intervallo prima della transazione.
`type(x) is int` esclude bool, che in Python è sottoclasse di int. Il retry
viene riconosciuto prima del controllo di conflitto; stessa chiave e dati
diversi producono ValueError. Il record è immutabile.

Non imporre la stessa struttura allo studente: R01-R06 possono essere
implementati correttamente con una lista privata e senza Protocol. Richiedere
invece che ogni errore lasci lo stato invariato e che i test pubblici non
vengano indeboliti. Casi indipendenti utili: intervallo che contiene interamente
quello esistente; chiusura esatta; ID vuoto; record con stessa chiave ma altra aula.

La prima porzione R01-R03 lascia correttamente rossi i test dei requisiti
mancanti. Valutare la porzione dichiarata e l'elenco dei residui. Un agente
che cancella i test mancanti per rendere verde la suite non completa il compito.

## S03 - Diagnosi di riferimento

Per il difetto inclusivo, 600-660 fallisce dopo 540-600 mentre 660-720
riesce: questo smentisce l'ipotesi «tutte le seconde richieste falliscono».
Il confronto `<=` include il confine; la correzione usa `<` in entrambe
le direzioni. Il caso 599-660 deve continuare a produrre conflitto.

Per il retry, controllare il conflitto prima dell'identità provoca un falso
errore sulla stessa richiesta. Per la cancellazione, cercare la condizione
`not row.cancelled` nel filtro dei conflitti. Il test deve anche verificare
il vecchio retry dopo cancel: deve restituire il record cancellato.

Se lo studente chiede una riscrittura generale, invitarlo a indicare quale
ipotesi la giustifichi. Una patch piccola non è sempre migliore, ma qui la
causa è circoscritta. Distinguere diagnosi, correzione e refactoring nel report.
La revisione tramite un secondo agente può suggerire casi; la correttezza
resta verificata contro il contratto e i comandi eseguiti.

## S04 - Soluzione base e diramazioni avanzate

`cancel` conserva la riga con `cancelled=True`; cancellare fisicamente il
record perderebbe l'informazione necessaria a R04 dopo un retry. `list_active`
filtra e ordina, restituendo una nuova lista di record immutabili.
Un caso nuovo con uguale start e aule diverse controlla il secondo criterio
di ordinamento; aggiungere ID diversi per verificare il terzo dove applicabile.

Il ramo software engineer usa un contratto Store con `transaction`, `all`
e `put`. La reference esegue R01-R06 sia in memoria sia su SQLite, verifica
rollback e riapertura, e usa due thread con connessioni separate per un conflitto.
Il lock in memoria protegge la transazione; SQLite usa BEGIN IMMEDIATE.
Gli archivi sono componenti interni: chiamare `put` fuori dal servizio può
aggirare le regole di dominio, perciò non costituisce l'API del prodotto.

Il ramo AI Engineer dispone di un adapter locale e test con risposta simulata.
Una bozza LAB-B per richiesta LAB-A è formalmente valida ma semanticamente
errata. Il parser non può scoprirlo senza confrontare con l'intento.
Per «prenota domani mattina» mancano dati e il prototipo a giornata singola
non è appropriato: l'eval deve contare una scelta arbitraria come errore.

La revisione con stato `clarify` è un'estensione assegnata: non è già
implementata in proposal.py. Accettare uno schema con due varianti disgiunte
e test per campi obbligatori, stato sconosciuto, domanda vuota e proposta
completa. Non attribuire qualità reale ai test mock o inventare risultati Ollama.

## S05 - Correzione della consegna

Una consegna sufficiente realizza R01-R06, mantiene i test pubblici e aggiunge
due casi indipendenti. Include istruzioni eseguibili da cartella pulita e
un report con almeno una decisione motivata. I 10 punti sono: requisiti 3,
correttezza/test 3, riproducibilità 2, spiegazione individuale 2; soglia 6
con contratto base integro ed evidenze autentiche.

Per il colloquio chiedere di anticipare l'esito di un caso prima di eseguirlo.
Una terza aula coinvolge validazione, esempi e test; nel ramo LLM anche enum
dello schema e parser. Un cambio di apertura coinvolge i limiti del dominio
e i test ai confini. La spiegazione deve individuare questi punti prima della patch.

Le sei ore aggiuntive di ciascun ramo sono stime: tre ore in S04 e tre in
S05. Registrare tempi del pilot. Il corso annuale resta di 68 ore; il nuovo
percorso autonomo ne richiede altre 12. L'eventuale scelta di sostituire parti
del piano annuale va registrata con coperture perse e recuperi previsti.

La CI verifica il software di riferimento e la struttura dei materiali.
Restano distinti il rehearsal con modelli reali, il giudizio didattico del
docente e la prova in classe. Nessuno di questi viene sostituito da un PDF
ben formato o da una suite verde.
