# Guida docente M13 — Applicazioni conversazionali

Riservato al docente.

## M13 - Stato della chat

Riferimento: `ChatSession` in `client.py`. Dopo un errore a metà streaming
la storia deve essere esattamente quella precedente all'invio; il frammento
può essere stato visualizzato ma non deve essere confermato come turno.
La policy elimina coppie complete, non metà conversazione, e preserva il
sistema. Un limite di caratteri non è un limite token esatto. Il test con
server HTTP locale controlla sia chiusura sia stato di cancellazione.
Per la consegna «ultime due coppie» la soluzione corretta applica il limite
al contesto da inviare e aggiorna la storia solo a completamento. Cancellare
durante una lettura bloccante può attendere il timeout: non promettere arresto
istantaneo senza cambiare il trasporto.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
