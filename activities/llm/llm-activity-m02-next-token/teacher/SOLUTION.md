# Guida docente M02 — Predire il simbolo successivo

Riservato al docente.

## M02 - Probabilità e bit

Con logits $(\ln2,0)$ la distribuzione è $(2/3,1/3)$. Se il target è il secondo
simbolo, la loss è $\ln3$ nat e $\log_2 3$ bit. Aggiungere una costante a tutti
i logits non cambia la softmax: numeratore e denominatore sono moltiplicati
per lo stesso fattore. Moltiplicarli invece cambia la concentrazione.
Il comando `python3 labs/course_lab.py softmax --logits 0 1 2` permette di
controllare normalizzazione e sorpresa. La correzione deve distinguere alta
probabilità da verità: il modello può assegnare alta probabilità a un errore
frequente. Nel ramo Pollicino le probabilità controllano il costo di codifica,
mentre il decoder deve ricostruire anche simboli a bassa probabilità.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
