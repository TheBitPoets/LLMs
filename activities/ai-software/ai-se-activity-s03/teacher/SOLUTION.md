# Soluzione docente

## S03 - Diagnosi di riferimento

Per il difetto inclusivo, 600-660 fallisce dopo 540-600 mentre 660-720
riesce: questo smentisce l'ipotesi «tutte le seconde richieste falliscono».
Il confronto `<=` include il confine; la correzione usa `<` in entrambe
le direzioni. Il caso 599-660 deve continuare a produrre conflitto.

Per il retry, controllare il conflitto prima dell'identità provoca un falso
errore sulla stessa richiesta. Per la cancellazione, cercare la condizione
`not row.cancelled` nel filtro dei conflitti. Il test deve anche verificare
il vecchio retry dopo cancel: deve restituire il record cancellato.

Se lo studente chiede una riscrittura generale, invitarlo a indicare quale
ipotesi la giustifichi. Una patch piccola non è sempre migliore, ma qui la
causa è circoscritta. Distinguere diagnosi, correzione e refactoring nel report.
La revisione tramite un secondo agente può suggerire casi; la correttezza
resta verificata contro il contratto e i comandi eseguiti.
