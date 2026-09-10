# Guida docente M10 — Hardware e quantizzazione

Riservato al docente.

## M10 - Budget di memoria

Per 8 miliardi di parametri a 4 bit il solo limite ideale dei pesi è 4 GB
decimali. Scale, metadati, cache, attivazioni e runtime aumentano il totale;
GB e GiB non sono uguali. In E06 la cache float32 del modello minuscolo con
48 posizioni occupa esattamente 36.864 byte, ottenuti dalla formula e dai
tensori. Questo valore non è il picco RSS del processo. Premiare tabelle che
separano stima, misura e unità. Il throughput va misurato a contesto e output
comparabili; includere o escludere il caricamento deve essere dichiarato.
Non trasportare le latenze della CPU del workspace al Mac M4 Pro né assumere
che memoria unificata significhi tutta la RAM disponibile al modello.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
