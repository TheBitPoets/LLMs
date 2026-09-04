# M11 - Ollama e inferenza locale

**Domanda guida:** come avviamo e controlliamo un modello locale?  
**Durata:** 4 ore Practitioner; 8 ore AI Engineer.  
**Prerequisiti:** M09–M10; terminale di base.

## Obiettivi osservabili

Installare/verificare Ollama, eseguire pull/run/show/list/ps, chiamare l'API,
creare un Modelfile e produrre un evidence report. L'AI Engineer analizza log,
streaming, timeout, keep-alive e riproducibilità.

## Lezione intuitiva

Ollama è il runtime/server, non il modello. Riceve una richiesta, carica pesi e
metadati, esegue prefill/decode e invia token al client. Aprire
[il ciclo della richiesta](../../../visuals/ollama-request-and-memory.html).

Il primo modello non va fissato per sempre nel testo. Al momento del laboratorio
si consulta lo snapshot corrente e si sceglie una taglia compatibile. Sul Mac
M4 Pro 36 GB si parte didatticamente da 4B–9B quantizzati; su macchine 8–16 GB
da 0.8B–4B, poi si misura.

## Laboratorio Practitioner

1. registrare OS/hardware e versione `ollama --version`;
2. verificare il servizio e la porta locale;
3. `ollama pull <tag>` e registrare digest/dimensione;
4. `ollama show <tag>` prima di `ollama run <tag>`;
5. chiamare `/api/generate` con streaming disabilitato, poi abilitato;
6. salvare prompt, options, tempi e risposta in JSONL;
7. ripetere offline dopo il download.

Non inserire dati personali. Un Modelfile controlla base, template/system e
parametri, non modifica magicamente la conoscenza dei pesi.

## Test e ripristino

Test negativi: servizio spento, tag errato, timeout, JSON non valido e memoria
insufficiente. Il client deve mostrare un errore utile e non perdere il report.
Ripristino: verificare servizio, `ollama list`, spazio disco e ridurre tag/context.

## Verifica

Esecuzione 3, manifest 2, API/stream 2, error handling 2, privacy 1. Fonte:
[Ollama documentation](https://docs.ollama.com/) e libro Kamigusa posseduto.
