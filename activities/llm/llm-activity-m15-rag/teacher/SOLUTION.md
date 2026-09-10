# Guida docente M15 — Embedding, ricerca e RAG

Riservato al docente.

## M15 - RAG e citazioni

La risposta «LAB-A ha 24 posti» deve citare il chunk della stanza A, con
estratto realmente presente. L'ID inventato viene rifiutato dal validatore.
Un estratto corretto associato a un'affermazione sulla stanza B non supera
la correzione semantica, anche se supera il controllo di sottostringa.
Senza chunk sopra soglia il codice si astiene senza generazione; una soglia
troppo severa può aumentare astensioni improprie. Il documento ostile resta
testo e il generatore non ha tool, quindi non può compiere effetti tramite
la pipeline. Non concludere per questo che il testo generato sia immune da
injection. L'eval live va conservato anche se il modello piccolo fallisce.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
