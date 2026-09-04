# M01 — Mappa dell'ecosistema

**Domanda guida:** dove sono modello, dati e calcolo quando usiamo un assistente AI?
**Durata:** 2 ore Practitioner; 4 ore AI Engineer.
**Prerequisiti:** M00.

## Obiettivi osservabili

Saprai distinguere modello di base, modello post-addestrato, tokenizer, runtime, API e applicazione; seguire il percorso dei dati in uno scenario locale o cloud; motivare una scelta con privacy, capacità, costo e manutenzione. Il livello AI Engineer aggiunge deployment ibrido, confini di fiducia e dipendenze operative.

## Problema iniziale

Scrivi una domanda in un'interfaccia e compare una risposta. Dove è stato eseguito il calcolo? Chi conserva il prompt? L'applicazione ha consultato documenti o strumenti? Dal solo schermo non si può sapere. Per ragionare bene serve una mappa a strati.

## Teoria Practitioner

Il **tokenizer** converte testo o byte in identificatori. Il **modello** contiene architettura e parametri appresi. Un **checkpoint** è una revisione concreta dei pesi. Il **runtime** legge il formato dei pesi, alloca memoria ed esegue i kernel. Un **server di inferenza** espone richieste concorrenti tramite API. L'**applicazione** gestisce utenti, prompt, cronologia, retrieval e interfaccia.

“Open weight” significa che i pesi sono ottenibili secondo una licenza; non implica automaticamente codice, dati di training o libertà d'uso illimitata. “Open source” va verificato componente per componente. Un servizio cloud può usare un modello proprietario oppure ospitare un modello open weight: posizione del calcolo e regime dei pesi sono assi diversi.

Apri [Dove viaggia il prompt?](../../../visuals/local-vs-cloud-data-journey.html). Nel percorso locale, prompt e pesi possono restare sulla macchina, ma installazione, download e log vanno comunque controllati. Nel cloud, la macchina invia una richiesta a un servizio soggetto a condizioni, retention e regione. “Locale” non equivale a “automaticamente sicuro”; “cloud” non equivale a “automaticamente insicuro”.

![Percorso dei dati nelle varianti locale e cloud](../../../visuals/static/rendered/local-cloud.png)

## Esempio minimo

In Ollama, un nome come `famiglia:tag` seleziona un artefatto gestito dal runtime. L'interfaccia web può inviare il prompt all'API locale `localhost`. Se la stessa interfaccia usa invece un endpoint esterno, cambia il confine di fiducia anche se l'aspetto resta identico. Documenta separatamente UI, API, runtime, modello, revisione e posizione dei dati.

## Esempio realistico

Un chatbot scolastico deve rispondere su circolari. Architettura A: modello cloud e documenti inviati al provider. B: modello e indice locali. C: retrieval locale, testo anonimizzato e modello cloud. A può offrire capacità superiori; B controllo e offline; C un compromesso. La decisione include qualità, dati, latenza, costi, aggiornamenti e audit.

## Livello AI Engineer: confini e deployment

Disegna data plane e control plane. Il data plane tratta prompt, embedding e output; il control plane gestisce configurazione, modelli, autorizzazioni e osservabilità. Identifica asset, attori, ingressi e trust boundary. Un processo locale con accesso a tutti i file può essere più rischioso di un'API cloud limitata a testo anonimizzato.

Nel deployment ibrido puoi usare routing per sensibilità, capacità o costo: classificazione locale e richiesta remota solo quando consentito; fallback locale senza rete; modelli differenti per task. Il routing deve essere misurato e protetto: se invia per errore dati sensibili al ramo cloud, l'architettura fallisce anche se i singoli modelli funzionano.

## Confronto tra soluzioni

| Criterio | Locale | Cloud | Ibrido |
| --- | --- | --- | --- |
| Avvio | download e configurazione | credenziali/API | entrambi |
| Privacy | controllo locale da verificare | dipende da contratto e flusso | dipende dal routing |
| Capacità | limitata dall'hardware | sistemi grandi disponibili | selettiva |
| Costi | hardware ed energia | consumo e abbonamenti | più complessi |
| Offline | possibile | normalmente no | parziale |
| Manutenzione | a carico dell'utente | in parte del provider | doppia superficie |

## Errori frequenti

- Confondere interfaccia e modello sottostante.
- Credere che un tag mobile identifichi per sempre gli stessi pesi.
- Ignorare log, cache, telemetria e backup nel percorso dei dati.
- Valutare soltanto il costo per token e non quello operativo.
- Dichiarare “open source” senza leggere la licenza.

## Esercizi A–F

- **A:** associa dieci termini allo strato corretto.
- **B:** modifica un diagramma cloud trasformandolo in locale.
- **C:** disegna il data journey di un'app che usi davvero.
- **D:** trova il punto in cui un dato riservato supera un confine non dichiarato.
- **E:** progetta tre varianti locale/cloud/ibrida e scegli con una matrice pesata.
- **F:** realizza un router con policy, audit e fallback dimostrabile.

## Laboratorio

Usa la visuale, poi completa una scheda con componenti, proprietario, posizione e dati trattati. Esegui `python3 labs/course_lab.py local-cloud` e confronta la tua classificazione. La consegna non chiede quale soluzione sia “migliore” in assoluto, ma quale soddisfi i vincoli espliciti.

## Verifica rapida

Spiega in 90 secondi il percorso di un prompt locale; indica due componenti che non sono il modello; descrivi un rischio locale e uno cloud; chiarisci perché open weight e locale non sono sinonimi.

## Sintesi inclusiva

L'esperienza “scrivo e ricevo una risposta” nasconde una catena. Separare tokenizer, pesi, runtime, server e applicazione rende visibili costi, responsabilità e dati. La scelta corretta dipende dal compito e dai vincoli.

## Fonti e collegamenti

- [Visuale locale/cloud](../../../visuals/local-vs-cloud-data-journey.html)
- [Catalogo modelli datato](../catalog/models-2026-09-04.md)
- Activity: `llm-activity-m01-ecosystem-map`
