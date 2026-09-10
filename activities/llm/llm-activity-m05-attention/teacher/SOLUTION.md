# Guida docente M05 — Attention e Transformer

Riservato al docente.

## M05 - Attention causale

Con una query che assegna punteggi 0 e $\ln2$ a due chiavi ammesse, i pesi
sono 1/3 e 2/3. L'output è la stessa combinazione dei value, non delle key.
In TinyLM una testa ha dimensione 12; la matrice dei punteggi ha dimensioni
tempo×tempo per testa. Il test decisivo modifica i token futuri e confronta
i logits del prefisso: devono restare uguali entro la tolleranza numerica.
Una softmax con righe a somma uno può comunque guardare il futuro se manca
la maschera: la sola normalizzazione non è prova sufficiente.
E04 fornisce il modello e `test_engineering_neural.py` il controllo di
causalità. Chiedere allo studente di spiegare l'offset della maschera con cache.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
