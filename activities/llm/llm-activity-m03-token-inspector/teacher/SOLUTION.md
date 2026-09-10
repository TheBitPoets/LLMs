# Guida docente M03 — Token, byte ed embedding

Riservato al docente.

## M03 - Byte, token e embedding

La lettera «è» occupa due byte in UTF-8, ma un tokenizer può rappresentarla
con uno o più token. Gli ID sono indici discreti; la lookup restituisce righe
della matrice embedding. La distanza fra ID numerici non misura somiglianza
semantica. Per il round trip richiedere uguaglianza dei byte, includendo
accenti, newline e spazi finali. Unicode apparentemente identico può avere
rappresentazioni diverse: normalizzare prima della prova cambia il problema.
E02 usa vettori prodotti da un modello embedding, mentre E04 usa embedding
allenabili dei byte dentro il Transformer: funzioni e addestramenti differenti.
Correggere chi assume che una similarità coseno di 0,8 significhi «80% vero».

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
