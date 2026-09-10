# Soluzione docente

## S01 - Soluzione degli esempi e variante

Esempi v1: LAB-A 540-600 poi 600-660 è ammesso; 599-660 è rifiutato;
LAB-B 540-600 è indipendente. 480-660 dura 180 ed è ammesso; 480-661
è rifiutato. 900-1080 è ammesso; 900-1081 è fuori orario.
Durata zero è rifiutata senza cambiare l'archivio.

Per la variante 120 minuti, R03 passa a durata massima 120; i test nuovi
devono ammettere 480-600 e rifiutare 480-601. La proposta deve identificare
specifica, validazione del servizio, test dei confini e documentazione; nel
ramo LLM anche il parser usa lo stesso limite e va aggiornato. La variante
rimane separata dal contratto v1 condiviso finché il docente non l'adotta.

Matrice minima: R01→happy path→reserve; R02→adiacenza/conflitto/aule→overlaps
e reserve; R03→validazione senza effetti→reserve; R04→retry/ID in conflitto→reserve;
R05→cancel e retry successivo→cancel/reserve; R06→ordinamento→list_active.
Assegnare credito alle decisioni motivate, non alla lunghezza della specifica.
