# M16 — Tool use, agenti e MCP

**Domanda guida:** quando un modello passa dal proporre testo al poter agire?
**Durata:** 3 ore Practitioner; 12 ore AI Engineer.
**Prerequisiti:** M13–M15.

## Obiettivi osservabili

Saprai distinguere workflow, tool call e agente; progettare schema, permessi, conferme e audit; spiegare il ruolo di MCP senza scambiarlo per autonomia. Il livello AI Engineer costruisce un orchestratore con state machine, idempotenza, policy e test avversariali.

## Problema iniziale

Un chatbot suggerisce “cancella il file”; un agente con uno strumento può cancellarlo davvero. La qualità linguistica non è un controllo di autorizzazione. Ogni capacità esterna amplia gli effetti e richiede confini tecnici.

## Teoria Practitioner

Un **workflow** ha passi stabiliti dal programma. Nel **tool use**, il modello propone nome e argomenti di una funzione; l'applicazione valida e decide se eseguirla. Un **agente** sceglie iterativamente passi in base allo stato e ai risultati. Più libertà aumenta flessibilità e superficie di errore.

MCP è un protocollo per esporre strumenti e risorse con descrizioni standard a client compatibili. Non sostituisce autenticazione, autorizzazione, sandbox, consenso o validazione. La descrizione del tool aiuta il modello a proporre una chiamata; il codice deve comunque applicare policy.

## Esempio minimo

Tool `meteo(città)` accetta solo una stringa e non ha effetti. Tool `invia_email(destinatario,testo)` ha effetto esterno e dati personali: richiede destinatario risolto, anteprima, conferma e idempotency key. Non basta chiedere al modello “sei sicuro?”.

## Esempio realistico

Un agente scolastico può cercare circolari e preparare una bozza, ma non inviarla senza approvazione. La policy consente lettura solo in una directory, blocca segreti, limita chiamate e tempo, registra tool e argomenti redatti. Se una pagina recuperata ordina di inviare documenti, l'istruzione resta dato non fidato.

## Livello AI Engineer: macchina a stati

Modella stati come `PLAN`, `VALIDATE`, `AWAIT_APPROVAL`, `EXECUTE`, `OBSERVE`, `DONE`, `FAILED`. Ogni transizione ha precondizioni e budget. Gli argomenti vengono validati con schema e poi con policy semantica. L'esecuzione usa least privilege e sandbox; gli output hanno dimensione e tipo limitati.

Le operazioni con effetti usano idempotency key per evitare duplicati dopo timeout. Compensating action non equivale sempre a rollback: un'email inviata non può essere “disinviata”. Circuit breaker e massimo numero di passi fermano loop. L'audit conserva chi ha autorizzato cosa, senza copiare segreti.

## Threat model essenziale

- prompt injection diretta o dai documenti;
- tool confused deputy che usa privilegi dell'app per l'utente sbagliato;
- argomenti con path traversal o comandi;
- esfiltrazione tramite output o URL;
- loop e consumo incontrollato;
- race, retry e doppio effetto;
- descrizione del tool ingannevole o server compromesso.

## Errori frequenti

- Eseguire direttamente il JSON prodotto dal modello.
- Dare accesso all'intero filesystem per comodità.
- Chiedere conferma dopo l'effetto.
- Affidare al modello la decisione finale sui propri permessi.
- Non distinguere fallimento del tool da fallimento del reasoning.

## Esercizi A–F

- **A:** classifica chat, workflow, tool use e agente.
- **B:** aggiungi schema e allowlist a un tool.
- **C:** implementa tool read-only con validazione.
- **D:** blocca injection e path traversal in casi forniti.
- **E:** costruisci agente con conferma prima degli effetti.
- **F:** realizza orchestratore auditabile con sandbox e test avversariali.

## Laboratorio

Esegui `python3 labs/course_lab.py tool-policy`. Costruisci prima un tool finto che registra la proposta senza agire. Aggiungi validazione, autorizzazione e conferma. Testa argomenti invalidi, chiamata duplicata, timeout e contenuto malevolo recuperato.

## Verifica rapida

Spiega chi decide l'esecuzione; indica che cosa MCP standardizza e che cosa no; disegna una state machine; mostra un controllo non basato sul prompt.

## Sintesi inclusiva

Il modello propone; il sistema autorizza ed esegue. Tool e agenti sono potenti perché collegano testo ed effetti. Schema, least privilege, conferma, idempotenza, budget e audit devono restare fuori dal controllo del modello.

## Fonti e collegamenti

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- Activity: `llm-activity-m16-safe-agent`

