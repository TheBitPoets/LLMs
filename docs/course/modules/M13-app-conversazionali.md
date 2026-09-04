# M13 — Applicazioni conversazionali

**Domanda guida:** che cosa serve attorno al modello per ottenere una chat affidabile?
**Durata:** 4 ore Practitioner; 10 ore AI Engineer.
**Prerequisiti:** M11–M12; Python e HTTP di base.

## Obiettivi osservabili

Saprai progettare messaggi, stato, streaming, limiti e gestione degli errori; costruire un client locale minimo; distinguere memoria dell'applicazione e contesto del modello. Il livello AI Engineer tratta concorrenza, idempotenza, backpressure, osservabilità e test.

## Problema iniziale

Un ciclo input/output che chiama il modello sembra una chat. Dopo alcuni turni però il contesto cresce, le istruzioni si contraddicono, la rete cade o un utente invia dati sensibili. Il prodotto deve governare tutto ciò che il modello non governa.

## Teoria Practitioner

Una conversazione è una sequenza di messaggi con ruolo e contenuto. L'app decide quali messaggi reinviare, quali riassume e quali elimina. Il modello non “ricorda” una sessione precedente se l'app o il servizio non gli forniscono stato. Context window e memoria persistente sono concetti distinti.

Lo streaming migliora il tempo percepito, ma richiede stati espliciti: in attesa, in ricezione, completato, annullato, errore. L'interfaccia non deve mostrare una risposta parziale come definitivamente valida. Timeout, cancel e retry devono evitare duplicazioni o richieste infinite.

## Esempio minimo

```python
import json
from urllib.request import Request, urlopen

payload = {"model": "MODELLO", "messages": [{"role": "user", "content": "Ciao"}], "stream": False}
request = Request("http://localhost:11434/api/chat", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
with urlopen(request, timeout=30) as response:
    data = json.load(response)
print(data["message"]["content"])
```

Questo frammento è un punto di partenza, non un'app completa: mancano validazione, errori, configurazione, log sicuri e test.

## Esempio realistico

`Llma_Chatbot` può separare adapter del provider, dominio della conversazione e UI. Lo stesso test di contratto deve funzionare con Ollama e con un mock deterministico. Un limite token arresta output eccessivi; la cronologia è ridotta con una policy esplicita; i log conservano ID e tempi, non prompt sensibili.

## Livello AI Engineer: architettura

Definisci un'interfaccia del provider con request, eventi stream, usage ed errori normalizzati. Mantieni il dominio indipendente dall'SDK. Usa un correlation ID per collegare richiesta, tentativi e metriche. I retry sono sicuri soltanto quando l'operazione è idempotente o protetta da chiavi; per tool con effetti esterni serve conferma e deduplicazione.

La backpressure impedisce che produttore e consumatore saturino memoria. Con molti utenti, queueing e rate limit proteggono il runtime. L'osservabilità include TTFT, latenza totale, token, error category, cancel e modello/digest, con redazione dei contenuti.

## Struttura consigliata

| Componente | Responsabilità |
| --- | --- |
| UI | input, rendering, accessibilità, cancel |
| Conversation service | stato, policy del contesto, orchestrazione |
| Provider adapter | protocollo Ollama/cloud, streaming, errori |
| Validator | schema, limiti, sanitizzazione |
| Storage | sessioni autorizzate, retention, cifratura |
| Telemetry | metriche tecniche prive di segreti |

## Errori frequenti

- Inserire l'intera cronologia senza budget.
- Accoppiare UI direttamente a un SDK.
- Registrare prompt e chiavi nei log.
- Riprovarе automaticamente un'azione con effetti.
- Confondere stop dello stream e annullamento lato server.
- Testare soltanto con il modello reale e output variabili.

## Esercizi A–F

- **A:** completa una sequenza di messaggi con ruoli.
- **B:** aggiungi timeout e messaggio d'errore al client.
- **C:** implementa adapter Ollama dietro un'interfaccia.
- **D:** correggi un bug di doppio invio durante retry.
- **E:** costruisci chat locale con streaming, cancel e test mock.
- **F:** realizza servizio multiutente con rate limit, audit e benchmark.

## Laboratorio

Parti dal client minimo e usa un server mock prima del modello reale. Testa risposta valida, timeout, JSON invalido, stream interrotto e cancel. Solo dopo collega Ollama e registra manifest e metriche.

## Verifica rapida

Spiega dove vive la memoria; mostra come sostituire il provider; gestisci un timeout senza perdere lo stato; elenca tre metriche che non richiedono salvare il prompt.

## Sintesi inclusiva

La chat è un sistema, non una casella di testo. L'applicazione possiede stato, privacy, errori, limiti e interfaccia; il modello produce continuazioni. Separare i componenti permette test, sostituzione e controllo.

## Fonti e collegamenti

- [Documentazione API Ollama](https://docs.ollama.com/api/introduction)
- [Valutazione del libro Local AI Models](../sources/local-ai-models-review.md)
- Activity: `llm-activity-m13-chatbot`

