# M04 — Apprendere dai dati

**Domanda guida:** come cambiano miliardi di numeri affinché la previsione migliori?
**Durata:** 4 ore Practitioner; 12 ore AI Engineer.
**Prerequisiti:** M02–M03; derivate e algebra lineare per l'estensione.

## Obiettivi osservabili

Saprai descrivere training, validation e inferenza; interpretare una curva di loss; riconoscere overfitting, leakage e distribuzione fuori dominio. Il livello AI Engineer deriva il gradiente di un classificatore semplice, implementa un training loop e spiega optimizer, batch, learning rate e checkpoint.

## Problema iniziale

Un modello memorizza perfettamente gli esempi di allenamento ma fallisce su frasi nuove. Ha ridotto la loss di training, ma non ha dimostrato di generalizzare. L'obiettivo non è ricordare il foglio delle risposte: è estrarre regolarità utili su dati non visti.

## Teoria Practitioner

Nel pre-training mostriamo sequenze e chiediamo di prevedere il token successivo. La loss misura quanto il modello ha penalizzato il token osservato. La retropropagazione attribuisce una parte dell'errore ai parametri; l'optimizer li aggiorna. Un **batch** contiene più esempi prima di un aggiornamento. Un'**epoca** attraversa una volta il dataset, concetto meno netto nei grandi stream.

Separiamo training, validation e test. Il training modifica i pesi; la validation guida decisioni come quando fermarsi; il test dovrebbe essere usato alla fine. Se esempi o duplicati attraversano le separazioni, otteniamo leakage e una stima ottimistica.

## Esempio minimo

Un modello con un solo parametro produce $\hat y=wx$. Per esempi $(1,2)$ e $(2,4)$, $w=1$ sottostima. La loss quadratica segnala l'errore; il gradiente indica la direzione in cui cambiare $w$. Aggiornando più volte, $w$ si avvicina a 2. Il principio è lo stesso nei Transformer, ma con moltissimi parametri, operazioni e dati.

## Esempio realistico

Alleni un classificatore di messaggi scolastici. La loss di training scende sempre; quella di validation scende e poi risale. Il modello si adatta a dettagli non utili sui nuovi esempi. Puoi fermarti al checkpoint migliore, aumentare dati, regolarizzare o ridurre capacità. Prima controlla duplicati e distribuzione: non ogni curva strana è overfitting.

## Livello AI Engineer: gradienti e ottimizzazione

Per logits $z=W x$ e target one-hot $y$, con softmax $p$, la cross-entropy ha gradiente $\partial L/\partial z=p-y$. La chain rule propaga il segnale attraverso layer e operazioni. L'aggiornamento base è

$$\theta_{t+1}=\theta_t-\eta\nabla_\theta L,$$

dove $\eta$ è il learning rate. Adam conserva stime mobili del primo e secondo momento del gradiente; weight decay e clipping affrontano problemi diversi e non sono sinonimi.

Con mixed precision alcune operazioni usano formati ridotti per velocità e memoria, mentre scale o copie selezionate preservano stabilità. Gradient accumulation simula batch effettivi maggiori. Un checkpoint riprendibile include pesi, optimizer, scheduler e stato casuale.

## Come leggere le curve

- training e validation scendono: apprendimento compatibile con i dati;
- training scende, validation sale: possibile overfitting o shift;
- entrambe piatte: controllare learning rate, dati, implementazione e capacità;
- spike o NaN: instabilità numerica, batch anomalo o overflow;
- test sorprendentemente migliore: controllare campione, leakage e difficoltà.

## Errori frequenti

- Usare il test set per scegliere iperparametri.
- Concludere dall'unico numero finale senza guardare le curve.
- Confondere una loss minore con “più verità”.
- Non fissare seed e versioni durante un confronto.
- Riprendere soltanto i pesi perdendo lo stato dell'optimizer.

## Esercizi A–F

- **A:** ordina forward, loss, backward e update.
- **B:** modifica il learning rate in una simulazione e descrivi la curva.
- **C:** implementa regressione o bigram model con un training loop.
- **D:** diagnostica leakage e overfitting in quattro scenari.
- **E:** confronta optimizer o batch size mantenendo costante il budget.
- **F:** addestra un piccolo LM, salva checkpoint riprendibile e redigi model card.

## Laboratorio

Esegui `python3 labs/course_lab.py loss` e calcola cross-entropy e perplexity. Traccia training e validation per un modello giocattolo; salva metriche a ogni epoca e seleziona il checkpoint con una regola definita prima.

## Verifica rapida

Spiega chi modifica i pesi; distingui validation e test; interpreta una curva divergente; scrivi l'aggiornamento del gradient descent e chiarisci il ruolo del learning rate.

## Sintesi inclusiva

Il training confronta previsione e dato, misura l'errore e modifica i parametri. Una loss bassa sul training non basta: serve generalizzazione su dati separati. Curve, split e registrazione completa proteggono da conclusioni ingannevoli.

## Fonti e collegamenti

- [Deep Learning, Goodfellow, Bengio e Courville](https://www.deeplearningbook.org/)
- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- Activity: `llm-activity-m04-learning-curve`
