# E04 - Costruire e addestrare un Transformer da zero

## Obiettivi e intuizione Practitioner

Un modello inizializzato a caso assomiglia a una tastiera che suggerisce
continuazioni senza aver letto nulla. Il training gli mostra molti prefissi
e il byte che viene dopo, correggendo gradualmente i collegamenti interni.
Il nostro modello ha 84.288 parametri: abbastanza per vedere il meccanismo,
troppo pochi e con dati troppo semplici per confonderlo con un assistente.

Qui «da zero» significa che definiamo architettura e pesi iniziali e facciamo
training senza checkpoint preaddestrati. PyTorch fornisce tensori, autograd e
ottimizzatore; non implementiamo una libreria numerica completa. La classe
[TinyLM](../../../labs/engineering/tiny_lm.py) è leggibile in un unico file.

## Architettura e forme AI Engineer

Il vocabolario contiene 256 byte. Per input $(B,T)$, la lookup dei token e
quella delle posizioni producono $(B,T,48)$; la loro somma entra in due blocchi.
Ogni blocco usa LayerNorm, attenzione causale a quattro teste, residuo,
LayerNorm, feed-forward 48→192→48 con GELU e secondo residuo.
Una normalizzazione finale e una matrice 48→256 producono logits per posizione.

Per un vettore $x$ di 48 coordinate, LayerNorm usa media e varianza di quel
vettore: $\gamma(x-\mu)/\sqrt{\sigma^2+\epsilon}+\beta$.
Non normalizza mescolando esempi del batch. Il residuo somma l'input alla
trasformazione, consentendo al blocco di apprendere una correzione.

Per testa, $Q,K,V$ hanno forma $(B,4,T,12)$ e

$$A=\mathrm{softmax}(QK^T/\sqrt{12}+M),\qquad O=AV.$$

$M_{ij}$ vale zero se $j\le i$ e meno infinito altrimenti. Modificare un byte
futuro non deve modificare i logits precedenti: il test di causalità verifica
questo comportamento. La maschera impedisce al training di copiare direttamente
il target dalla posizione successiva.

Questa architettura usa posizioni assolute apprese e LayerNorm, non RoPE,
RMSNorm, GQA o MoE. M06 spiega quelle varianti. Non si deve attribuirle al
nostro codice solo perché sono comuni nei modelli recenti.

## Dati e training riproducibile

```bash
python3 -m pip install -r labs/engineering/requirements-cpu.txt
python3 -m labs.engineering.train
python3 -m labs.engineering.generate \
  --prompt 'Ada studia' --count 80 \
  --output output/engineering/generation-report.json
```

I sei file in `fixtures/text` sono originali e sintetici. I documenti sono
suddivisi per indice in train/validation/test e controllati per duplicati
esatti. Condividono però nomi e strutture di frase: il test misura nuove
combinazioni della medesima distribuzione semplice, non generalizzazione al
linguaggio naturale. Il generatore del corpus permette di riprodurli.

Ogni batch contiene otto finestre da 64 byte. Gli input sono $x_t$ e i target
sono $x_{t+1}$. Si eseguono 160 passi AdamW, learning rate 0,003, clipping a
norma 1, seed 7 e un thread CPU. Ogni venti passi si misura la validation e
si conserva il checkpoint migliore. Il test non decide quando fermarsi.
La loss di training nel grafico è quella del batch corrente; la validation
copre tutti i target validi con finestre consecutive e contesto azzerato.

![Curve misurate di training e adattamento](../../../visuals/static/rendered/engineering-training.png)

## Risultati osservati e interpretazione

Nel report versionato, Python 3.12.14 e PyTorch 2.8.0 CPU x86_64, la loss test
del modello base è circa **0,295 nat/byte**, contro circa **2,92** della baseline
unigramma add-one. La conversione produce circa 0,425 bit/byte ideali; un
archivio reale deve pagare anche intestazione, arrotondamenti e modello.

Il comando di generazione produce byte e un testo di anteprima. Byte casuali
possono non formare UTF-8 valido: il report conserva l'esadecimale esatto e
segnala le sostituzioni nell'anteprima. Non è una chat istruita né possiede un
token di fine sequenza. Dopo 64 byte usa una finestra mobile con posizioni
azzerate; questa policy va distinta dalla KV cache a contesto fisso di E06.

## Consegna e verifica

Practitioner: confronta una continuazione con le frasi del corpus e indica
due regolarità apprese e un limite. AI Engineer: prima di guardare il test,
definisci un nuovo split per argomento, confronta larghezza 24 e 48 a budget
dichiarato e registra curve, hash, numero di parametri e loss. Se il test
diventa molto più difficile, spiega il cambiamento di distribuzione.

I test controllano causalità, riduzione della loss su una fixture apprendibile
e corrispondenza fra inferenza piena e con cache. La fixture di unit test
dimostra che il training funziona; solo il protocollo separato valuta un task.
Per ripristinare una prova usa una nuova directory `--output`, conservando
quella precedente invece di sovrascrivere il confronto.

Fonte primaria: [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
Le scelte e le differenze rispetto al paper sono dichiarate sopra.
