# Guida docente M06 — Architetture moderne

Riservato al docente.

## M06 - Architetture moderne

Per la KV cache, a parità di livelli, contesto e dimensione testa, passare
da otto teste KV a due riduce quel costo a un quarto; non riduce automaticamente
allo stesso modo pesi totali o FLOP dell'intero modello. Nel MoE distinguere
parametri attivi da parametri da conservare: gli esperti non selezionati
restano parte dell'artefatto. RoPE cambia il modo di incorporare la posizione,
non rende affidabile qualunque lunghezza di contesto. Una risposta corretta
collega ogni tecnica al collo di bottiglia che affronta e a un limite.
Usare il catalogo del 10 settembre per confrontare una card recente con
TinyLM: quest'ultimo usa MHA e posizioni apprese, senza attribuirgli QSA,
Gated DeltaNet o altri componenti assenti dal codice.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
