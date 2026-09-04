# M12 - Sampling e prompting

**Domanda guida:** perché lo stesso modello può rispondere diversamente?  
**Durata:** 3 ore Practitioner; 8 ore AI Engineer.  
**Prerequisiti:** M02 e M11.

## Obiettivi osservabili

Distinguere greedy, temperature, top-k, top-p, seed e stop; costruire prompt
con input delimitato e output strutturato; misurare stabilità. L'AI Engineer
implementa sampler e parser con vincoli.

## Lezione intuitiva

Il prompt modifica il contesto; il sampler decide come scegliere dalla
distribuzione. Temperature riscalda/raffredda le differenze; top-k conserva i
k candidati maggiori; top-p conserva il più piccolo insieme con massa almeno p.
L'ordine delle operazioni e l'implementazione del runtime contano.

Un prompt robusto dichiara ruolo operativo, task, dati delimitati, vincoli e
schema. Non deve chiedere al modello di “essere accurato” al posto di una
verifica. Structured output riduce errori sintattici quando runtime/modello lo
supportano; non rende veri i campi.

## Laboratorio

Sulla stessa distribuzione eseguire 100 campioni per configurazione e
confrontare frequenze/diversità. Poi chiedere estrazione JSON da cinque testi,
validare schema e distinguere parse rate da field accuracy. Baseline regex o
parser manuale. Test negativi: campo assente, testo ostile e risposta troncata.

## AI Engineer

Implementare softmax stabile, top-k/top-p, RNG con seed e test statistici
semplici. Per output vincolato studiare decoding grammar-aware e validazione
post-hoc; misurare retry e latenza.

## Verifica

Parametri 3, esperimento 2, schema/validazione 2, distinzione sintassi/verità 2,
riproducibilità 1.

