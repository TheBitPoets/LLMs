# E01 - Una chat che conserva uno stato coerente

## Obiettivi e intuizione Practitioner

La chat assomiglia a un quaderno che l'applicazione riapre a ogni domanda.
Il modello vede le pagine inviate nella richiesta, non tutte le conversazioni
precedenti. Se una risposta arriva a metà e la connessione cade, copiare quel
frammento nel quaderno come risposta completa crea un ricordo sbagliato.

L'obiettivo è usare una chat locale a più turni, osservare lo streaming e
spiegare cosa succede a cronologia e interfaccia quando una richiesta fallisce.
Il riferimento è [client.py](../../../labs/engineering/client.py), richiamato
dal [runner](../../../labs/engineering/run.py). È un'applicazione da terminale;
una GUI può riusare il medesimo oggetto `ChatSession`.

## Preparazione e prima prova

Avvia Ollama secondo M11. Scegli un tag dalla libreria dopo il controllo di
memoria e licenza, scaricalo e verifica che compaia in `ollama list`. Il tag
piccolo seguente è una baseline per provare il collegamento, non un vincitore
dell'evaluation né una garanzia di tool calling:

```bash
ollama pull qwen3.5:0.8b
python3 -m labs.engineering.run chat \
  --model qwen3.5:0.8b --interactive \
  --prompt 'Ricorda: il progetto si chiama Aurora.' \
  --output output/rehearsal/chat.json
```

Al secondo turno chiedi il nome del progetto; esci con `/quit`. Il runner
stampa i frammenti mentre arrivano e salva risultati e inventario del runtime
alla fine. Per la prova usa dati fittizi: il report contiene testo della
richiesta e risposta. Se il servizio manca, l'errore deve essere visibile e il
programma termina con codice diverso da zero; avvia il servizio e ripeti.

## Il contratto AI Engineer

`Ollama` limita l'origine HTTP al loopback, la dimensione delle risposte e il
tempo delle operazioni. Il payload fissa seed, temperatura e output massimo.
Lo streaming è una sequenza di oggetti JSON delimitati da newline; non si
deve tentare di leggere tutto il corpo come un singolo JSON.

`ChatSession` passa da idle a streaming. Accumula frammenti in una variabile
provvisoria e chiama un callback per l'interfaccia. Solo un messaggio finale
`done=true` permette di aggiungere la coppia utente/assistente alla cronologia.
EOF anticipato, JSON malformato, errore HTTP e cancellazione lasciano intatta
la cronologia precedente. Il test controlla lo stato, non soltanto una stringa
di errore a schermo.

Quando il budget di caratteri è superato vengono eliminati i turni più vecchi
completi, preservando il messaggio di sistema. Il budget è una protezione
applicativa approssimata: non è un conteggio token del tokenizer del modello.
Un messaggio singolo troppo lungo viene rifiutato. Riassumere la storia
sarebbe una policy diversa, con propri errori da valutare.

La cancellazione usa un evento controllato fra le letture. Con HTTP bloccante
non garantisce arresto istantaneo durante una lettura: interviene al prossimo
frammento o al timeout, configurato a 30 secondi. Il contesto chiude la
connessione quando il generatore termina. Non viene eseguito retry automatico:
la richiesta potrebbe essere già stata elaborata dal servizio.

## Tempi, test e limite dell'evidenza

Il tempo al primo testo visibile è
$t_{\text{primo frammento}}-t_{\text{invio}}$; include rete e runtime.
Un modello che emette reasoning separato può avere tempo al primo testo finale
diverso dal tempo al primo token interno. Per il throughput usa i contatori
del provider: `eval_count / (eval_duration / 1e9)` quando il denominatore è
positivo. Contare caratteri al secondo non equivale a contare token.

```bash
python3 -m unittest discover -s tests \
  -p 'test_engineering_apps.py' -v
```

I test aprono un server HTTP locale che simula risposte e interruzioni, quindi
verificano trasporto e stato senza scaricare pesi. Non misurano qualità,
latenza o memoria di Ollama reale. Tale sessione rimane nel rehearsal.

## Consegna e controllo

Practitioner: conduci tre turni, annota quali messaggi servono a rispondere e
spiega perché riavviare la chat cambia il risultato. AI Engineer: aggiungi una
policy che mantenga solo le ultime due coppie complete, crea un test per un
errore dopo il primo frammento e dimostra che la risposta parziale non entra
nella storia. Consegna codice, test e report; non fissare come test unitario
la formulazione linguistica di un modello generativo.

Fonte primaria del protocollo: [Ollama Chat API](https://docs.ollama.com/api/chat).
Riferimento software: separazione adapter/dominio e revisione per specifiche
nel supplemento S00-S05.
