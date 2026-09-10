# Guida docente M19 — Costruire e integrare

Riservato al docente.

## M19 - Capstone e codec esatto

Nel ramo applicativo richiedere un bisogno definito, baseline, eval e casi
di errore; E01-E03 forniscono componenti da integrare, S00-S05 il metodo di
sviluppo. Nel ramo codec, tutti gli otto casi del report ricostruiscono i byte.
Per il testo sintetico di 148 byte: adattivo 359, neurale 317, gzip 60; il
neurale aggiunge 347.451 byte di modello al primo trasferimento. Quindi non
vince quel confronto. L'hash del checkpoint lega la versione, ma non prova
CDF identiche su CPU diverse. Richiedere un test di corruzione e un mismatch
di modello; qualunque differenza di byte boccia il criterio lossless.
L'integrazione fisica PollicinoNet resta separata e non viene simulata come
prova radio. Il capstone del corso può essere completato senza quel gate.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
