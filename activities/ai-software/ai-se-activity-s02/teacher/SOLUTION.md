# Soluzione docente

## S02 - Patch attesa e test indipendenti

La soluzione in `labs/ai_software/reference/booking.py` usa confronti stretti
per l'intersezione. Valida ID, aula, tipi e intervallo prima della transazione.
`type(x) is int` esclude bool, che in Python è sottoclasse di int. Il retry
viene riconosciuto prima del controllo di conflitto; stessa chiave e dati
diversi producono ValueError. Il record è immutabile.

Non imporre la stessa struttura allo studente: R01-R06 possono essere
implementati correttamente con una lista privata e senza Protocol. Richiedere
invece che ogni errore lasci lo stato invariato e che i test pubblici non
vengano indeboliti. Casi indipendenti utili: intervallo che contiene interamente
quello esistente; chiusura esatta; ID vuoto; record con stessa chiave ma altra aula.

La prima porzione R01-R03 lascia correttamente rossi i test dei requisiti
mancanti. Valutare la porzione dichiarata e l'elenco dei residui. Un agente
che cancella i test mancanti per rendere verde la suite non completa il compito.
