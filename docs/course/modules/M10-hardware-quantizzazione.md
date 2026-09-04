# M10 - Hardware e quantizzazione

**Domanda guida:** quale modello può girare sulla macchina disponibile?  
**Durata:** 4 ore Practitioner; 12 ore AI Engineer.  
**Prerequisiti:** M06 e M09.

## Obiettivi osservabili

Stimare memoria dei pesi e margine; distinguere disco, RAM/VRAM, bandwidth e
compute; confrontare quantizzazioni con qualità e velocità misurate. L'AI
Engineer comprende PTQ, calibration, weight-only, activation e KV quantization.

## Lezione intuitiva

Un modello sul disco è come un libro nello zaino; per lavorarci occorre aprirlo
sul tavolo della memoria. `parametri × bit / 8` stima solo i pesi. Runtime,
buffer, sistema, contesto e KV cache occupano altro spazio. Durante il decode si
legge moltissimo peso per produrre pochi token: la bandwidth può contare più
dei soli FLOPS.

Usare [Ollama e memoria](../../../visuals/ollama-request-and-memory.html) sul
profilo M4 Pro 36 GB e su un PC da 8/16 GB. La quantizzazione rappresenta i
pesi con meno bit e scale; riduce memoria, ma errore e kernel supportati
determinano qualità e velocità reali.

## Laboratorio

Scegliere tre tag dello stesso modello/quantizzazione quando disponibili.
Misurare resident memory, time-to-first-token, token/s e score del dataset M14.
Warm-up separato dalle run; almeno cinque ripetizioni. Test negativo: contesto
lungo o modello sovradimensionato fino al rifiuto controllato.

## AI Engineer

Implementare quantizzazione simmetrica per-channel di una matrice e calcolare
errore MSE/coseno sull'output. Studiare outlier, group size, dequantizzazione
fusa e differenza tra peso compresso su disco e percorso di calcolo.

## Verifica

Stima 2, misura 3, confronto qualità 2, scelta motivata 2, limite 1. Fonte:
documentazione runtime e testo *Quantization and Fast Inference* selezionato.

