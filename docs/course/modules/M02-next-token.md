# M02 — Predire il simbolo successivo

**Domanda guida:** come nasce un testo lungo da una sola previsione alla volta?
**Durata:** 3 ore Practitioner; 8 ore AI Engineer.
**Prerequisiti:** M00–M01; percentuali e logaritmi per l'estensione.

## Obiettivi osservabili

Saprai leggere una distribuzione di probabilità, distinguere logits e probabilità, simulare la generazione autoregressiva e spiegare perché plausibilità non significa verità. Il livello AI Engineer calcola softmax, cross-entropy, entropia e perplexity e collega la previsione ai bit di un codificatore aritmetico.

## Problema iniziale

Completa “La capitale d'Italia è …”. Una risposta sembra richiedere conoscenza geografica; per il modello l'operazione immediata è assegnare punteggi ai token possibili. Ripetendo scelta e reinserimento del token nel contesto emerge un paragrafo. Il comportamento complesso nasce da un ciclo semplice, ma i parametri che producono i punteggi hanno appreso strutture molto ricche.

## Teoria Practitioner

I **logits** sono punteggi non normalizzati. La softmax li trasforma in valori positivi che sommano a uno. Il decoder sceglie un token: il massimo produce una scelta greedy; il campionamento tratta la distribuzione come una lotteria controllata. Il token scelto viene aggiunto al contesto e il modello calcola una nuova distribuzione.

Apri [Il ciclo next-token](../../../visuals/next-token-prediction.html). Cambia il contesto e osserva che non stai interrogando un archivio di frasi: stai cambiando la distribuzione condizionata. Una sequenza può essere grammaticalmente probabile e fattualmente falsa; l'obiettivo di training non contiene un verificatore universale della realtà.

![Il token scelto rientra nel contesto e avvia il passo successivo](../../../visuals/static/rendered/next-token.png)

## Esempio minimo

Supponi tre candidati con probabilità `mare=0,50`, `monte=0,30`, `casa=0,20`. Greedy sceglie sempre “mare”. Campionando, “mare” compare circa metà delle volte su molte prove, non necessariamente cinque volte su dieci. Dopo la scelta, le probabilità del passo successivo cambiano. La probabilità dell'intera sequenza è il prodotto delle probabilità condizionate dei singoli passi.

## Esempio realistico

Un modello deve produrre JSON. Anche se ogni token più probabile sembra sensato, basta una parentesi mancante per rendere invalido l'oggetto. Per questo un'applicazione robusta combina prompt, output strutturato o grammatica, validazione e retry controllato. La previsione next-token resta il motore, ma il prodotto richiede controlli esterni.

## Livello AI Engineer: matematica

Per logits $z_i$ e temperatura $T>0$:

$$p_i=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}.$$

Sottrarre $\max_j z_j$ prima dell'esponenziale evita overflow senza cambiare il risultato. Con target corretto $y$, la negative log-likelihood è $-\log p_y$; la cross-entropy media su $N$ token è

$$L=-\frac1N\sum_{t=1}^{N}\log p(x_t\mid x_{<t}).$$

La perplexity è $\exp(L)$ quando si usano logaritmi naturali. È interpretabile come dimensione efficace dell'incertezza, ma confronti validi richiedono stesso dataset, stessa tokenizzazione e stessa convenzione. L'entropia $H(p)=-\sum_i p_i\log_2p_i$ misura l'incertezza in bit.

## Dalle probabilità ai bit

Un buon modello assegna alta probabilità al simbolo osservato. Un codificatore aritmetico può usare quelle probabilità per restringere un intervallo e rappresentare la sequenza con circa $-\log_2 p(x)$ bit. Apri [probabilità → bit](../../../visuals/pollicino-probabilities-to-bits.html). Per una ricostruzione lossless, encoder e decoder devono riprodurre esattamente la stessa distribuzione a ogni passo: una piccola divergenza può corrompere tutto il resto.

## Errori frequenti

- Leggere probabilità come percentuale di verità.
- Sommare probabilità dei passi invece di moltiplicarle.
- Confrontare perplexity con tokenizer differenti.
- Credere che temperatura zero modifichi i pesi.
- Usare un output convincente come prova di una fonte consultata.

## Esercizi A–F

- **A:** scegli il token greedy in cinque distribuzioni.
- **B:** modifica una distribuzione e prevedi come cambia l'entropia.
- **C:** implementa softmax stabile e verifica che la somma sia uno.
- **D:** correggi un calcolo di perplexity con log e base incoerenti.
- **E:** costruisci un generatore bigram e confronta strategie.
- **F:** collega un modello causale a un codec aritmetico con round trip esatto.

## Laboratorio

Usa la visuale e poi esegui `python3 labs/course_lab.py next-token`. Registra distribuzione, scelta, sorpresa $-\log_2p$ e sequenza. Per Pollicino esegui anche `python3 labs/course_lab.py arithmetic-codec` e verifica che input e output coincidano.

## Verifica rapida

1. Che differenza c'è tra logit e probabilità?
2. Perché il contesto cambia a ogni token generato?
3. Perché una frase probabile può essere falsa?
4. Quale condizione rende possibile il decoding lossless?

## Sintesi inclusiva

Il modello sceglie un seguito una volta alla volta. I punteggi diventano probabilità, la strategia decide il token e il ciclo riparte. La probabilità descrive la previsione del modello, non certifica la realtà. La stessa distribuzione può guidare generazione o compressione.

## Fonti e collegamenti

- Claude Shannon, *A Mathematical Theory of Communication* (1948)
- [Visuale next-token](../../../visuals/next-token-prediction.html)
- [Percorso Pollicino](../pollicino-learning-path.md)
- Activity: `llm-activity-m02-next-token`
