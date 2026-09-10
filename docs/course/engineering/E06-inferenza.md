# E06 - Prefill, KV cache e un kernel di attenzione

## Obiettivi e intuizione Practitioner

Quando leggi una frase lunga per rispondere, elabori prima il testo ricevuto.
Poi aggiungi parole una alla volta. Ricalcolare ogni volta tutti gli appunti
sarebbe uno spreco: la KV cache conserva key e value delle posizioni già viste.
Richiede memoria e non elimina il costo di consultare il passato.

Il laboratorio distingue prefill e decode, confronta un calcolo esplicito,
un microkernel a blocchi e una funzione ottimizzata della libreria. Non parte
dall'assunto che il codice più complicato sia più veloce.

## Memoria e causalità AI Engineer

Con $L$ livelli, batch $B$, contesto $T$, $H_{kv}$ teste key/value, dimensione
$d$ e $s$ byte per elemento, la cache occupa idealmente

$$M_{KV}=2LBTH_{kv}ds.$$

Il fattore due rappresenta K e V. Nel modello del corso, per 48 posizioni,
$L=2$, $B=1$, $H_{kv}=4$, $d=12$, $s=4$: otteniamo 36.864 byte, valore
controllato contando lo storage dei tensori. Non comprende pesi, attivazioni,
allocator o memoria del processo. In GQA $H_{kv}$ può essere minore delle
teste query; il nostro riferimento implementa MHA con numeri uguali.

Con cache lunga $P$ e nuove query indicizzate da $i$, la maschera ammette
chiavi $j\le P+i$. Usare $j\le i$ senza offset durante il decode nasconderebbe
quasi tutto il passato. Anche le posizioni apprese devono cominciare da $P$.
Il test confronta logits ottenuti su tutto il prefisso e con token incrementali.

## Softmax online: elaborare blocchi senza salvare tutti i punteggi

Per una riga di query manteniamo massimo corrente $m$, denominatore $\ell$
e accumulatore vettoriale $a$. Per un nuovo blocco di punteggi $s_j$ e value
$v_j$ aggiorniamo:

$$m'=\max(m,\max_j s_j),$$
$$\ell'=e^{m-m'}\ell+\sum_j e^{s_j-m'},$$
$$a'=e^{m-m'}a+\sum_j e^{s_j-m'}v_j,\qquad o=a/\ell.$$

Il riscalamento mette i blocchi nello stesso sistema di riferimento numerico.
Con due punteggi 0 e $\ln2$, i pesi finali sono 1/3 e 2/3 anche se vengono
letti in blocchi separati. La maschera causale si applica prima degli
esponenziali; un blocco totalmente mascherato non deve introdurre NaN.

[inference.py](../../../labs/engineering/inference.py) implementa questa
ricorrenza con tensori PyTorch e cicli Python. Riduce la matrice temporanea
dei punteggi a blocchi, ma non realizza la fusione CUDA né l'ottimizzazione
dell'accesso alla memoria di FlashAttention. La terza variante usa
`scaled_dot_product_attention` della libreria; il backend effettivo dipende
dal dispositivo e non va chiamato automaticamente «FlashAttention» su CPU.

## Esperimento riproducibile

```bash
python3 -m labs.engineering.inference
python3 -m unittest discover -s tests \
  -p 'test_engineering_neural.py' -v
```

Le prove numeriche precedono il benchmark. In float32 CPU l'errore massimo
del tiled rispetto al riferimento è circa $4,8\cdot10^{-7}$; per i logits
con cache circa $4,1\cdot10^{-6}$. I test includono lunghezza 19 e tile 7,
quindi bordi non multipli della dimensione del blocco.

Nel report versionato, su shape $(1,4,64,12)$, la mediana di sette misure
dopo due warm-up è circa 0,071 ms per il riferimento, 0,650 ms per il tiled
Python e 0,036 ms per la libreria. **Il tiled didattico è più lento.**
Il decode ripetendo il prefisso impiega circa 20,6 ms, quello con cache circa
16,1 ms nella prova registrata. Sono misure CPU piccole e sensibili al carico;
non predicono token/s di un modello Ollama sul Mac.

## Consegna e controllo

Practitioner: spiega perché un contesto lungo può consumare memoria anche con
pochi parametri attivi. AI Engineer: varia lunghezza e tile, controlla prima
errore e finitezza, poi salva tutte le ripetizioni e la mediana. Distingui
memoria stimata dei tensori, picco del processo e memoria allocata dal device.
Su un acceleratore servono sincronizzazione o eventi appropriati: il solo
tempo della chiamata Python può misurare soltanto l'accodamento.

Fonte primaria dell'idea di attenzione esatta con attenzione agli accessi in
memoria: [FlashAttention](https://arxiv.org/abs/2205.14135).
La nostra implementazione riproduce la ricorrenza online a scala didattica;
un kernel CUDA/Triton competitivo resta un progetto avanzato facoltativo.
