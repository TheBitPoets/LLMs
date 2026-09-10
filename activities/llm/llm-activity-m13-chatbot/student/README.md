# Activity M13 — Applicazioni conversazionali

## Obiettivo

Applica la dispensa M13 e produci un risultato verificabile.

## Consegna specifica

Estendi il client E01 con una policy che mantenga soltanto le ultime due coppie complete e aggiungi un test di errore dopo il primo frammento, senza alterare la storia confermata.

## Procedura comune

1. Leggi problema iniziale, teoria Practitioner ed esempio della dispensa.
2. Completa il livello A–D assegnato; per E–F realizza il prodotto richiesto.
3. Registra modello/revisione, runtime/versione, parametri, hardware, input e risultato.
4. Distingui ciò che hai misurato da ciò che stai inferendo.
5. Consegna artefatto, relazione breve e un limite osservato.

## Evidenza attesa

Provider sostituibile, mock deterministico e stati di errore/cancel verificati.

## Autoverifica

- [ ] Un compagno può ripetere il lavoro con le informazioni fornite.
- [ ] Non ho inserito dati personali o segreti nei prompt.
- [ ] Ho confrontato il risultato con una baseline.
- [ ] Ho indicato almeno un caso in cui la soluzione può fallire.

## Esempi eseguibili distribuiti

Gli asset `example` contengono codice originale e test pubblici. Sono esempi svolti da studiare, non la consegna completata. Esegui `python3 -m unittest discover -s tests -v` dalla root dello scaffold.

Prima dei test neurali installa `python3 -m pip install -r labs/engineering/requirements-cpu.txt`. Consulta il capitolo E01-chat.md nella Course Board. Le prove Ollama richiedono servizio e modelli installati; quelle CPU usano fixture incluse. I report vanno in una directory nuova e devono distinguere simulazione e misure.
