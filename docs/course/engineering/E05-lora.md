# E05 - LoRA: pochi parametri, effetti da misurare

## Obiettivi e intuizione Practitioner

Pensa a un filtro aggiunto davanti a una macchina fotografica: non ricostruisci
l'obiettivo, ma l'immagine cambia comunque. LoRA lascia fissi i pesi originali
e aggiunge una correzione appresa. Congelare i pesi base non significa congelare
il comportamento del modello che usa la correzione.

Il laboratorio adatta il modello di E04 da frasi semplici a righe strutturate
su stanze, posti e attività. Mostra sia il miglioramento del nuovo compito sia
il peggioramento di quello iniziale. Non usa un corpus acquistato né risposte
di un modello cloud.

## Matrici e gradienti AI Engineer

Per una proiezione $W\in\mathbb R^{d_{out}\times d_{in}}$, LoRA aggiunge

$$W'=W+sBA,\qquad A\in\mathbb R^{r\times d_{in}},
\quad B\in\mathbb R^{d_{out}\times r},\quad s=\alpha/r.$$

Il rango della correzione non supera $r$. Nella head del nostro modello
$d_{in}=48$, $d_{out}=256$, $r=4$, $\alpha=8$, quindi $s=2$.
Invece di aggiornare 12.288 pesi della proiezione, apprendiamo
$4(48+256)=1.216$ parametri. Questo confronto riguarda la head: l'intero
modello base contiene 84.288 parametri, tutti congelati durante l'adattamento.

Per input colonna $x$ e gradiente in uscita $g$, i contributi sono
$\nabla_B L=s\,g(Ax)^T$ e $\nabla_A L=s\,B^Tg\,x^T$.
La classe `LoRAHead` inizializza A casualmente e B a zero: al primo forward
il modello coincide con il base, il gradiente di B può essere non nullo e
quello di A è inizialmente nullo. Inizializzare entrambe a zero impedirebbe
al prodotto di cominciare ad apprendere.

Per l'inferenza si può calcolare separatamente $Wx+sB(Ax)$ oppure fondere
$W+sBA$. Il test confronta i due risultati entro tolleranza. Questa equivalenza
matematica in precisione piena non garantisce equivalenza bit-per-bit dopo
quantizzazione o su runtime differenti.

## Esecuzione e artefatti

```bash
python3 -m labs.engineering.train \
  --output output/engineering --adapter-steps 120
python3 -m labs.engineering.generate \
  --checkpoint output/engineering/tiny-byte-lm.pt \
  --adapter output/engineering/head-lora.pt \
  --prompt 'stanza=' --count 80 \
  --output output/engineering/adapter-generation.json
```

Il primo comando ripete anche il training base: per una nuova configurazione
scegli una directory distinta. L'adapter contiene solo A, B, rango, scala e
SHA-256 del checkpoint base. Il caricatore rifiuta un adapter associato a un
base diverso. Il report controlla con uguaglianza esatta che tutti i parametri
congelati siano rimasti identici.

Il learning rate dell'adapter è 0,02. Validation e test target sono distinti;
il test non viene usato per scegliere il passo migliore. Non applichiamo LoRA
a Q/V o a tutte le proiezioni: questa è una riproduzione minimale dell'idea
di aggiornamento a basso rango sulla sola head, non una ricetta completa
per adattare un modello di frontiera. Non è QLoRA: il base resta in float32.

## Un risultato utile anche quando è negativo

Nel report CPU la loss sul test target scende da **6,449 a 1,471 nat/byte**.
Sul test del dominio base sale però da **0,295 a 4,759**. I pesi congelati
sono identici, ma la composizione base+adapter ha cambiato comportamento.
Per un'app che deve mantenere entrambe le competenze questo adattamento non
supera un criterio ragionevole di regressione.

Anche la generazione libera salvata in `adapter-generation.json` contiene
sequenze malformate e ripetizioni. La loss valuta predizioni condizionate su
prefissi corretti del dataset; generando liberamente, il modello deve invece
continuare anche i propri errori. Una loss target migliore non prova che il
modello produca record validi in autonomia: serve un'evaluation di generazione.

La soluzione non è eliminare il risultato scomodo dal report. Si possono
valutare dati misti, scala minore, meno passi, altro rango o instradamento
esplicito fra base e adapter. Ogni scelta richiede nuova validation e un test
finale ancora separato. Il fatto che l'adapter occupi poco spazio non prova
che sia innocuo o che migliori qualunque domanda.

## Consegna e verifica

Practitioner: interpreta le due colonne «dominio base» e «dominio target» e
decidi se attiveresti sempre l'adapter. AI Engineer: preregistra un limite di
regressione, confronta due ranghi su validation, verifica parametri allenabili
e pesi congelati e consegna un unico confronto finale sul test. Aggiungi un
test che rifiuti un adapter di un checkpoint diverso.

Fonte primaria: [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685).
Il collegamento pratico con prompting, RAG e distillazione resta M17: i pesi
non sono il posto adatto per aggiornare continuamente informazioni citabili.
