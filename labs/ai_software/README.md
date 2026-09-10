# PrenotaLab: sviluppare con un coding agent

Python 3.11+, nessuna dipendenza per il percorso base. Le
[sei lezioni](../../docs/course/ai-software/README.md) guidano il lavoro.

## Partenza dello studente

Dalla radice del repository esporta lo starter in una **nuova** cartella:

```bash
python3 labs/ai_software/prepare.py ../prenotalab-studente
cd ../prenotalab-studente
python3 -m unittest discover -s . -p 'test_*.py' -v
git init
git add booking.py test_booking.py SPEC.md AGENTS.example.md
git commit -m 'Baseline didattica PrenotaLab'
git switch -c feature/contratto-prenotazioni
```

Al primo lancio diversi test **devono fallire**: lo starter è incompleto.
Il commit richiede nome/email Git già configurati; in laboratorio senza Git
si può conservare una copia iniziale e un diff, dichiarando il limite.
Apri soltanto la cartella esportata nel coding agent scelto. Non passargli
le soluzioni docente. Leggi e adatta `AGENTS.example.md` secondo lo strumento.
Non è necessario rinominarlo: puoi allegarlo come contesto della richiesta.

Il lavoro dell'agente termina con modifiche locali e test leggibili. La
consegna studente consiste in specifica, codice, casi aggiunti, diff e report.
La pubblicazione del progetto scolastico è una decisione del docente.

## Verifica del materiale per il docente

Dalla radice del repository:

```bash
python3 -m unittest discover -s tests -p 'test_ai_software.py' -v
python3 -m unittest discover -s tests -p 'test_booking_proposal.py' -v
```

Il primo comando esegue lo stesso contratto pubblico su memoria e SQLite,
più verifiche di limiti, rollback, persistenza e conflitto concorrente.
La [soluzione](reference/booking.py) è destinata al docente: contiene anche
l'estensione R07-R08. Lo starter richiede solo R01-R06.

## Estensione AI Engineer: una proposta con Ollama

Prerequisiti: servizio Ollama già avviato, modello locale scelto secondo M09-M11,
supporto all'API chat/output strutturato verificato sul modello scelto.
Sostituire il segnaposto con il tag realmente installato:

```bash
python3 labs/ai_software/proposal.py --model '<tag-locale-verificato>' --text 'LAB-A dalle 9 alle 10'
```

Il risultato è una **bozza da rivedere**, non una prenotazione. Il programma
valida forma e limiti dei campi; la corrispondenza alla richiesta va valutata
a parte. Un JSON valido può indicare l'aula sbagliata. Nessun testo restituito
dal modello viene eseguito come codice e nessuna richiesta crea prenotazioni.

`proposal.py` è una singola chiamata LLM: non è un coding agent. Il coding agent
è lo strumento usato dallo studente per leggere, modificare e verificare il repo.
I test dell'adapter usano una risposta simulata e non misurano un modello reale.
Tempi/token mancanti restano `null`, senza stime spacciate per osservazioni.

## Ambito

Il progetto serve a rendere visibili requisiti, regressioni e responsabilità
dei componenti. La soluzione SQLite usa una transazione per controllo e scrittura;
una connessione per thread. Mancano deliberatamente date, autenticazione,
autorizzazioni applicative, interfaccia web e gestione operativa. Il passaggio a
un servizio reale richiede una nuova specifica e una nuova valutazione.
