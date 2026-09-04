# M07 - Pre-training, dati e scaling

**Domanda guida:** da dove arrivano capacità e limiti?  
**Durata:** 3 ore Practitioner; 10 ore AI Engineer.  
**Prerequisiti:** M04–M06.

## Obiettivi osservabili

Descrivere corpus→dedup/filter→token→batch→loss→checkpoint; leggere una data
card; distinguere trend di scaling da garanzia. L'AI Engineer progetta uno
scaling experiment controllato.

## Lezione intuitiva

Il modello comprime regolarità statistiche dei dati nei parametri. Più dati non
significa automaticamente dati migliori: duplicati possono amplificare
memorizzazione, filtri possono cancellare lingue o gruppi, licenze e privacy
limitano l'uso. Anche il “numero di token” dipende dal tokenizer.

Le scaling law descrivono curve empiriche della loss al variare di compute,
parametri e dati. Sono simili a una carta topografica del regime osservato, non
una legge che promette capacità specifiche. Chinchilla mostra che, a compute
fisso, un modello più piccolo addestrato su più token può batterne uno più
grande sotto-addestrato.

## Laboratorio

Creare una data card per un corpus piccolo e lecito: origine, licenza, lingua,
PII, deduplica, split, hash e rimozioni. Addestrare tre bigrammi/MLP su 25%, 50%
e 100% dei dati con seed multipli. Riportare curve e intervallo, non una sola
run. Controllo: dati casuali e duplicazione artificiale.

## AI Engineer

Fissare un budget di operazioni, variare dimensione modello/token e adattare
learning rate. Fit log-log soltanto come descrizione dei punti. Calcolare
compute e total description length includendo checkpoint.

## Verifica

Data card 4, disegno esperimento 3, lettura critica scaling 2, limite 1. Fonti:
Kaplan et al. e Hoffmann et al. nella timeline.

