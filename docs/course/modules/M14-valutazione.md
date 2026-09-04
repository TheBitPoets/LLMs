# M14 - Valutazione

**Domanda guida:** come sappiamo se un modello è adatto allo scopo?  
**Durata:** 4 ore Practitioner; 14 ore AI Engineer.  
**Prerequisiti:** M00, M11–M13.

## Obiettivi osservabili

Trasformare requisiti in dataset e grader; usare baseline, split, failure
taxonomy e intervalli; decidere con più metriche. L'AI Engineer misura accordo
tra annotatori, incertezza e regressioni.

## Lezione intuitiva

Un benchmark è un termometro costruito per una domanda. Un numero alto può non
misurare il nostro caso d'uso; una media può nascondere errori rari ma gravi.
Prima di eseguire il modello si congelano esempi, criteri e soglia. Si conserva
ogni errore con categoria, non solo lo score.

Esempio riassunto appunti: coverage dei cinque punti, factual consistency su
nomi/numeri, rispetto lunghezza, astensione quando il testo è insufficiente.
Baseline: estrazione delle prime frasi. Un LLM-as-judge può assistere, ma va
calibrato contro giudizi umani e può essere sensibile a ordine e stile.

## Laboratorio

Creare almeno 20 fixture lecite: normali, limite e avversarie. Eseguire due
modelli/configurazioni più baseline. Reportare metriche per categoria, costo,
TTFT/token-s, memoria e tre failure case commentati. Test negativo: perturbare
un numero nel documento e verificare che il grader lo rilevi.

## AI Engineer

Bootstrap confidence interval; precision/recall/F1 per estrazione; Cohen kappa
o accordo percentuale con limiti; paired comparison e regression gate.
Contamination check e separazione dev/test. Nessun test set viene usato per
riscrivere il prompt prima del report finale.

## Verifica

Dataset 2, grader 2, baseline 1, report distribuzioni 2, failure analysis 2,
decisione/limiti 1. Fonte: documentazione e testi Manning su LLM evaluation.

