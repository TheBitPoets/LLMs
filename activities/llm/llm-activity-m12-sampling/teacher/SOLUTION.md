# Guida docente M12 — Sampling e prompting

Riservato al docente.

## M12 - Sampling e output strutturato

Nel confronto cambiare una variabile alla volta. Temperatura influenza la
concentrazione, top-k limita il numero di candidati, top-p limita la massa
cumulata; l'ordine delle operazioni conta. Un decoder greedy può essere
ripetibile nel medesimo ambiente ma non rende vero il contenuto. Per JSON
distinguere sintassi, schema e correttezza semantica: `{ "posti": 99 }` può
essere JSON perfetto e dato sbagliato. E02 valida citazioni e schema, E03
valida tool e argomenti prima dell'esecuzione. Il criterio minimo include
un output malformato e uno formalmente valido ma non supportato dai dati.
Non assegnare pieno punteggio a una singola risposta riuscita senza confronto.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
