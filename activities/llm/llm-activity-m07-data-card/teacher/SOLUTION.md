# Guida docente M07 — Pre-training, dati e scaling

Riservato al docente.

## M07 - Dati e contaminazione

Nel corpus E04 il controllo fra insiemi di righe trova duplicati esatti.
Questo non trova parafrasi né template condivisi. Una soluzione migliore per
valutare trasferimento a un dominio nuovo separa per fonte, argomento o tempo
prima del campionamento delle finestre. Suddividere finestre sovrapposte dopo
averle estratte può copiare gran parte dello stesso testo fra train e test.
La data card deve dichiarare origine sintetica, generatore, licenza e limiti,
non soltanto il numero di righe. Non è possibile inferire una scaling law
affidabile da due modelli minuscoli addestrati con budget non confrontabili.
Chiedere quale dato cambierebbe la decisione di raccolta e quale contaminazione
resterebbe invisibile a un hash esatto.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
