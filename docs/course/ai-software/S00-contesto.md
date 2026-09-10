# S00 - Leggere il progetto prima di delegare

## Problema iniziale

La segreteria chiede: «Ci serve qualcosa per prenotare i laboratori senza
sovrapposizioni». Un agente potrebbe produrre subito un'applicazione elegante.
Non sa però se sono ammessi incontri consecutivi, quali aule esistono e che
cosa deve accadere quando un utente preme due volte lo stesso pulsante.
L'obiettivo iniziale è scoprire queste decisioni e osservare il software esistente.

Pensa al contesto come alla cartella consegnata a un collega che entra oggi
nel progetto: deve contenere la domanda, le regole e i file pertinenti.
Una cartella enorme piena di versioni contraddittorie può confondere più di una
cartella piccola e curata. L'analogia riguarda l'organizzazione del lavoro:
non implica che il modello comprenda o ricordi come una persona.

## Risultato Practitioner

Alla fine sai distinguere requisito, comportamento osservato e ipotesi;
prepari una richiesta limitata; riconosci se il sistema sta solo suggerendo
testo oppure sta modificando un repository. Non devi scegliere il modello
«migliore in assoluto»: devi verificare che lo strumento disponibile sappia
leggere i file del piccolo progetto e proporti un diff comprensibile.

Esporta lo starter seguendo il README del kit. Esegui i nove test pubblici
prima di modificare i file. Alcuni falliscono intenzionalmente: conserva l'output
iniziale. Scrivi quali casi passano, quali falliscono e quali terminano con
un'eccezione. Il numero di test verdi è una fotografia della baseline, non un voto.

## Laboratorio A: osserva, poi formula la domanda

Dedica 20 minuti alla lettura, 25 alla baseline, 25 al confronto con l'agente,
30 alla mappa del progetto e 20 alla discussione. È una traccia di 120 minuti,
da adattare ai tempi reali della classe.

In `booking.py` individua il record `Booking`, il servizio `BookingService`
e la funzione `overlaps`. Nel file di test riconosci preparazione, azione e
asserzione. Collega almeno tre nomi di test agli ID della specifica. Un nome
come `test_R02_adjacent_is_allowed` racconta l'intento, ma devi leggere anche
l'asserzione per sapere che cosa controlla davvero.

Fornisci all'agente solo SPEC.md, booking.py e test_booking.py dello starter.
Usa questa richiesta iniziale e conserva la risposta:

> Leggi questi tre file. Non modificarli ancora. Descrivi il flusso di una
> prenotazione, identifica le regole implementate e quelle mancanti. Per ogni
> osservazione cita funzione o test. Separa ciò che hai eseguito da ciò che
> hai dedotto. Proponi tre domande di chiarimento sul dominio.

Controlla ogni riferimento della risposta. Se l'agente cita una funzione che
non esiste, registra l'errore e ripeti con contesto più preciso. Se afferma
«tutti i test passano», chiedi il comando e confrontalo con il tuo output.
Una spiegazione plausibile non sostituisce una verifica eseguita.

## Esempio minimo

La frase «le due prenotazioni si toccano» è ambigua. La baseline usa `<=`
nella funzione di sovrapposizione; la specifica accetta invece gli intervalli
consecutivi. Osserva una prenotazione 540-600 e una 600-660. Prima predici
il risultato, poi esegui il relativo test. Hai trovato un disaccordo preciso
fra documento e codice, abbastanza piccolo da discutere senza conoscere l'intera app.

## Approfondimento AI Engineer e software engineer

Prepara una mappa del contesto a tre colonne: file, ragione per includerlo,
scadenza dell'informazione. La specifica vale finché non è revisionata; un log
vale per un'esecuzione; una documentazione del provider richiede una versione
o data. Per un repository grande chiedi prima un elenco di file candidati,
poi leggi le dipendenze necessarie: includere tutto indiscriminatamente può
sprecare contesto e introdurre istruzioni incompatibili.

Confronta due sessioni fresche: una con la sola richiesta vaga e una con i tre
file. Misura riferimenti corretti, omissioni e tempo umano per la revisione.
Non dedurre un vantaggio generale da una sola coppia di risposte. Conserva
strumento/versione, modello dichiarato, eventuale revisione locale, prompt e
commit iniziale. Se il servizio non espone il modello esatto, scrivi «non esposto».

## Verifica e consegna

Consegna baseline, mappa di tre file e una pagina di osservazioni corrette
o respinte. Spiega a voce una regola senza consultare la risposta dell'AI.
Domanda diagnostica: se cambi modello ma lasci un documento obsoleto nel
contesto, quale problema rimane? Risposta attesa: le istruzioni sul comportamento
desiderato restano sbagliate o contraddittorie; un modello diverso non le corregge per definizione.

Il pattern praticato è **esplora, pianifica, modifica, verifica**. In questa
lezione completi solo le prime due fasi. Passa a S01 con almeno un'ambiguità
reale da risolvere, non con una lunga lista generica di consigli.
