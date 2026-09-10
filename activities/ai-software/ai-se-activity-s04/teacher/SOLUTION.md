# Soluzione docente

## S04 - Soluzione base e diramazioni avanzate

`cancel` conserva la riga con `cancelled=True`; cancellare fisicamente il
record perderebbe l'informazione necessaria a R04 dopo un retry. `list_active`
filtra e ordina, restituendo una nuova lista di record immutabili.
Un caso nuovo con uguale start e aule diverse controlla il secondo criterio
di ordinamento; aggiungere ID diversi per verificare il terzo dove applicabile.

Il ramo software engineer usa un contratto Store con `transaction`, `all`
e `put`. La reference esegue R01-R06 sia in memoria sia su SQLite, verifica
rollback e riapertura, e usa due thread con connessioni separate per un conflitto.
Il lock in memoria protegge la transazione; SQLite usa BEGIN IMMEDIATE.
Gli archivi sono componenti interni: chiamare `put` fuori dal servizio può
aggirare le regole di dominio, perciò non costituisce l'API del prodotto.

Il ramo AI Engineer dispone di un adapter locale e test con risposta simulata.
Una bozza LAB-B per richiesta LAB-A è formalmente valida ma semanticamente
errata. Il parser non può scoprirlo senza confrontare con l'intento.
Per «prenota domani mattina» mancano dati e il prototipo a giornata singola
non è appropriato: l'eval deve contare una scelta arbitraria come errore.

La revisione con stato `clarify` è un'estensione assegnata: non è già
implementata in proposal.py. Accettare uno schema con due varianti disgiunte
e test per campi obbligatori, stato sconosciuto, domanda vuota e proposta
completa. Non attribuire qualità reale ai test mock o inventare risultati Ollama.
