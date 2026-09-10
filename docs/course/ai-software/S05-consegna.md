# S05 - Consegnare, confrontare e mantenere

## Problema iniziale

Sul computer dell'autore tutto funziona, ma un compagno non sa quale comando
eseguire. La specifica parla di tre ore, un test ammette quattro ore e il README
descrive una versione precedente. Il prodotto non è pronto solo perché
l'ultima sessione con l'agente si è conclusa senza errori visibili.

La consegna è un pacchetto di evidenze: un'altra persona deve poter partire
da uno stato noto, ripetere i controlli e capire le decisioni. È anche il
momento in cui l'autore dimostra di saper modificare il programma senza
dipendere interamente dalla conversazione che lo ha generato.

## Risultato Practitioner

Consegni un repository leggibile con specifica, implementazione, test,
istruzioni ed esiti. Sai distinguere una demo da una release riproducibile,
descrivi un limite e fai una modifica piccola davanti al docente. Usi la
rubrica per verificare la tua comprensione, non per contare quanti prompt hai scritto.

## Laboratorio F: prova di consegna a un compagno

Dedica 25 minuti alla pulizia della documentazione, 30 alla prova in una nuova
cartella, 25 alla revisione incrociata, 25 al colloquio e 15 al report finale.
La soluzione del docente resta fuori dal progetto studente.

Completa il template di report del percorso. In una copia pulita esegui:

```bash
python3 -m unittest discover -s . -p 'test_*.py' -v
git diff --check
git status --short
```

Il primo comando verifica il contratto e i casi aggiunti. Il secondo segnala
problemi di whitespace, non la correttezza del programma. Il terzo mostra
modifiche e file non registrati: leggilo per verificare di non aver dimenticato
artefatti importanti. Nessuno di questi comandi pubblica il progetto.

Scambia il lavoro con un compagno. Il revisore deve eseguire le istruzioni
senza attingere alla cronologia della chat e ricostruire due decisioni a partire
da SPEC.md. Se servono informazioni orali indispensabili, aggiungile al README.
Conserva nel report un problema trovato dal revisore e come lo hai risolto.

Per il colloquio il docente chiede una variazione circoscritta, per esempio
cambiare l'orario di apertura o aggiungere una terza aula. Prima elenca
requisiti e test coinvolti, poi modifica il codice e spiega un caso limite.
Non è necessario vietare l'AI durante tutto il progetto: la breve prova
individuale serve a verificare che il risultato sia stato compreso.

## Esempio minimo: una release che si può ricostruire

«Ho usato un agente famoso e tutti i test sono verdi» non identifica un
artefatto. «Commit iniziale X, patch Y, contratto v1, Python 3.12, comando Z,
output allegato, due casi aggiunti e tre requisiti ancora esclusi» consente
a un'altra persona di verificare l'affermazione. I valori X/Y/Z vanno sostituiti
con dati reali della sessione, non copiati da un esempio.

Se una piattaforma cloud non espone versione o modello preciso, registra
nome dello strumento, data, impostazioni disponibili e il limite. Per un
modello locale registra tag e digest effettivi oltre a runtime e hardware.
Non inventare token o tempi mancanti; misura almeno il tempo umano complessivo.

## Ramo software engineer: CI e cambiamenti di specifica, altre 3 ore

Prepara una pipeline che, da checkout pulito e versione Python dichiarata,
esegua i test. Il report deve mostrare che cosa è stato controllato; un check
verde su un commit precedente non valida una patch successiva.
Scrivi una descrizione di pull request con problema, cambiamento osservabile,
test e limiti. Una PR è una proposta di integrazione: non è la revisione stessa.

Applica la variante di S01 in un branch: aggiorna specifica, test dei confini,
codice e README nella stessa modifica. Per un bug su codice esistente distingui
la correzione di un'implementazione sbagliata dalla decisione di cambiare
il contratto. Introduci una checklist breve per il revisore basata su queste
evidenze, evitando un elenco generico di decine di voci mai controllate.

## Ramo AI Engineer: confronto locale e cloud, altre 3 ore

Confronta due configurazioni di sviluppo sullo stesso incarico e sullo stesso
commit iniziale, con contesto e budget dichiarati. Registra task completato,
regressioni, tentativi, tempo di generazione, tempo umano e costo disponibile.
Due interfacce diverse possono avere strumenti diversi: in quel caso confronti
**sistemi di sviluppo**, non isoli l'effetto del solo modello.

Alterna l'ordine delle prove o assegna incarichi equivalenti a coppie diverse,
per ridurre l'effetto dell'apprendimento del compito. Tieni separati i task
usati per perfezionare i prompt e quelli di valutazione finale. Poche prove
non autorizzano classifiche generali; usa i risultati per la scelta locale
del laboratorio e annota quando vanno aggiornati.

## Rubrica e criteri di completamento

La valutazione su 10 punti assegna 3 a requisiti ed esempi, 3 a correttezza e
test indipendenti, 2 a riproducibilità e 2 alla spiegazione individuale.
Per superare il percorso servono almeno 6 punti, tutti R01-R06 soddisfatti
e nessuna evidenza inventata. Le estensioni avanzate hanno evidenze aggiuntive:
non compensano un contratto base rotto.

Consegna codice, specifica, report, diff, output dei test e decisioni accettate
o respinte dall'agente. Domanda diagnostica finale: quale parte del tuo lavoro
rimane valida se domani cambi coding agent? Requisiti, esempi, test, confini
del programma e procedura di verifica sono riutilizzabili; istruzioni e
configurazione dello strumento devono essere adattate e nuovamente provate.
