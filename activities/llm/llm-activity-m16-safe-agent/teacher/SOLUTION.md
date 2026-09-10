# Guida docente M16 — Tool use, agenti e MCP

Riservato al docente.

## M16 - Agente e protocollo

La soluzione deve mostrare una traccia con `lookup_room`, argomento `LAB-A`
e risultato 24 prima della risposta finale. Il numero 24 da solo potrebbe
essere stato inventato. La policy rifiuta tool sconosciuti e chiavi extra;
il limite passi arresta un agente che continua a chiedere lo stesso strumento.
Il test MCP avvia un processo reale, esegue handshake e discovery e verifica
che una chiamata prima dell'inizializzazione fallisca. Aggiungere una stanza
richiede aggiornare dati e validazione, non soltanto descrivere il nuovo valore
nel prompt. `readOnlyHint` non impone permessi. Per operazioni con effetti
rimandare a S04: approvazione e transazione appartengono all'applicazione.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
