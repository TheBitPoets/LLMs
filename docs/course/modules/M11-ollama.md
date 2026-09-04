# M11 — Ollama e inferenza locale

**Domanda guida:** come scegliamo, eseguiamo e documentiamo un modello locale?
**Durata:** 4 ore Practitioner; 8 ore AI Engineer.
**Prerequisiti:** M09–M10; terminale e HTTP di base.

## Obiettivi osservabili

Saprai installare e verificare Ollama, acquisire un modello compatibile, usare CLI e API, fissare parametri, osservare streaming e gestire errori. Il livello AI Engineer documenta template, opzioni, lifecycle, concorrenza e riproducibilità.

## Problema iniziale

Digitare `ollama run nome` produce una risposta, ma non certifica quale artefatto sia stato usato, quanta memoria richieda o se il test sia ripetibile. Il laboratorio trasforma la demo in un esperimento tracciabile.

## Teoria Practitioner

Ollama gestisce modelli, avvia un server locale ed espone API. Prima verifica la documentazione corrente: comandi, tag e disponibilità cambiano. `ollama list` mostra gli artefatti locali; `ollama show` ne espone informazioni; `ollama run` apre una sessione; l'API consente a un'applicazione di inviare richieste senza simulare la tastiera.

Apri [il ciclo della richiesta](../../../visuals/ollama-request-and-memory.html). Il prompt passa al template chat e al tokenizer; il runtime carica i pesi, esegue prefill e poi decode; la risposta può arrivare in streaming. “localhost” limita il percorso di rete solo se bind, proxy e applicazioni sono configurati correttamente.

## Esempio minimo

```bash
ollama --version
ollama list
ollama show MODELLO
ollama run MODELLO "Rispondi soltanto con OK"
```

Sostituisci `MODELLO` con un tag scelto dal catalogo **verificato il giorno della prova**. Conserva output dei primi tre comandi e il digest quando disponibile. Non inserire il nome di un modello nel corso stabile: il catalogo datato gestisce le parti volatili.

Una richiesta API tipica:

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "MODELLO",
  "messages": [{"role": "user", "content": "Rispondi con OK"}],
  "stream": false,
  "options": {"temperature": 0}
}'
```

## Esempio realistico

Costruisci un piccolo client Python con timeout, controllo dello status HTTP, parsing esplicito e log senza contenuto sensibile. Esegui una fixture di dieci prompt, registra configurazione e tempi e salva output separati. Se il server non risponde, l'app deve mostrare un errore utile; non deve bloccarsi indefinitamente.

## Livello AI Engineer: template e lifecycle

L'API riceve ruoli e opzioni, ma il runtime deve serializzarli nel template previsto dal checkpoint. Un template incompatibile può degradare un ottimo modello. Ispeziona il Modelfile o i metadati e differenzia system prompt, messaggi, stop token e parametri di sampling.

Il lifecycle comprende download, verifica, caricamento, keep-alive, scaricamento e aggiornamento. Un tag mobile può cambiare: per benchmark conserva digest, data e versione Ollama. Con richieste concorrenti misura queueing e memoria; il throughput aggregato può crescere mentre la latenza per utente peggiora.

## Gestione sicura degli errori

- timeout di connessione e risposta;
- modello assente o non caricabile;
- memoria insufficiente;
- risposta troncata o JSON invalido;
- stream interrotto;
- server esposto su interfacce non previste;
- aggiornamento che cambia comportamento.

Ogni errore deve produrre messaggio, codice o evidenza diagnostica senza mostrare segreti.

## Errori frequenti

- Copiare un comando con modello non adatto al proprio hardware.
- Non registrare digest, versione e template.
- Assumere che `temperature: 0` garantisca bitwise determinism.
- Usare retry infiniti.
- Pubblicare il server sulla LAN senza autenticazione o policy.

## Esercizi A–F

- **A:** verifica servizio, elenco e metadati.
- **B:** modifica un parametro e confronta output.
- **C:** scrivi un client con timeout e validazione.
- **D:** diagnostica quattro failure case preparati.
- **E:** costruisci un'app locale con streaming e log riproducibile.
- **F:** realizza serving controllato con benchmark, policy e rollback.

## Laboratorio

Segui `docs/course/rehearsal/README.md` quando sarà disponibile il Mac M4 Pro 36 GB. Prima del rehearsal puoi esercitarti con `python3 labs/course_lab.py ollama-request`, che costruisce e valida una richiesta senza dichiarare esecuzione hardware.

## Verifica rapida

Mostra la differenza tra CLI e API; identifica modello e runtime; dimostra timeout e gestione di un modello assente; spiega quali dati servono per ripetere la prova.

## Sintesi inclusiva

Ollama rende semplice iniziare, non elimina le decisioni. Un'esecuzione seria fissa artefatto, runtime, template, parametri, hardware e fixture. L'applicazione deve gestire errori e proteggere il confine locale.

## Fonti e collegamenti

- [Documentazione Ollama](https://docs.ollama.com/)
- [Catalogo modelli del corso](../catalog/models-2026-09-04.md)
- [Rehearsal Ollama](../rehearsal/README.md)
- Activity: `llm-activity-m11-ollama`
