# M02 - Predire il simbolo successivo

**Domanda guida:** che cosa fa il modello a ogni passo?  
**Durata:** 3 ore Practitioner; 8 ore AI Engineer.  
**Prerequisiti:** M01; percentuali.

## Obiettivi osservabili

Il Practitioner segue contesto→logits→probabilità→scelta→nuovo contesto e
spiega perché temperatura non aggiunge conoscenza. L'AI Engineer calcola
softmax stabile, negative log-likelihood, cross-entropy e perplexity.

## Lezione intuitiva

Il modello non scrive prima tutta la risposta: assegna punteggi ai possibili
token successivi, li trasforma in probabilità, sceglie secondo la strategia di
decoding e ripete. La probabilità è una preferenza condizionata dal contesto,
non una certificazione di verità.

Usare [Il ciclo next-token](../../../visuals/next-token-prediction.html). Con
“Il cielo è” confrontare scelta greedy e campionamento. Abbassare la temperatura
concentra una distribuzione esistente; non corregge pesi, dati o ragionamento.

## Esempio matematico

Con logits `[2, 1, 0]`, sottraiamo il massimo per stabilità e calcoliamo
`softmax(z_i)=exp(z_i-max(z))/Σ exp(z_j-max(z))`. Se il token vero riceve
probabilità `0,7`, la surprisal è `-log2(0,7)≈0,515 bit`; se riceve `0,01`, è
circa `6,64 bit`. La loss media in log naturale è la cross-entropy; la
perplexity è `exp(loss)`.

## Laboratorio

Calcolare a mano una distribuzione di quattro candidati, poi usare lo script
del corso variando temperatura e seed. Registrare 20 estrazioni e confrontare
frequenze osservate/attese. Test negativo: un logit `1000` non deve produrre
overflow nella softmax stabile.

Collegamento Pollicino: aprire [probabilità→bit](../../../visuals/pollicino-probabilities-to-bits.html)
e osservare che una migliore probabilità sul simbolo vero restringe più
efficientemente l'intervallo, senza rinunciare alla ricostruzione esatta.

## Verifica

Spiegazione orale del ciclo (4 punti), calcolo corretto (3), distinzione
competenza/sampling (2), limite dichiarato (1). Fonte primaria: Shannon (1948)
e la definizione autoregressiva richiamata nella timeline.

