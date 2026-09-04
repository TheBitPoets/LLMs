# M05 — Attention e Transformer

**Domanda guida:** come decide ogni token quali parti del contesto usare?
**Durata:** 5 ore Practitioner; 16 ore AI Engineer.
**Prerequisiti:** M03–M04; matrici e softmax per l'estensione.

## Obiettivi osservabili

Saprai seguire embedding → attention causale → residual/norm → MLP → logits; distinguere Query, Key e Value; spiegare maschera causale e multi-head. Il livello AI Engineer implementa un blocco decoder, controlla shape, stabilità e causalità e ne stima il costo.

## Problema iniziale

Nella frase “Maria mise il libro nello zaino perché **esso** era pesante”, per interpretare “esso” bisogna usare parti precedenti del contesto. Un Transformer non sposta un cursore simbolico: costruisce, per ogni posizione e head, pesi con cui mescolare informazioni provenienti da altre posizioni consentite.

## Teoria Practitioner

Ogni token produce una **Query**, ciò che cerca; una **Key**, ciò con cui può essere confrontato; un **Value**, l'informazione da trasferire. Query e Key generano punteggi; la softmax li normalizza; la somma pesata dei Value produce un nuovo vettore. La maschera causale impedisce di leggere token futuri durante la previsione.

Apri [Attention Q/K/V](../../../visuals/attention-qkv-lab.html). Cambia Query e disattiva temporaneamente la maschera. Un peso alto descrive una relazione interna di quello specifico head e layer, non una spiegazione universale del ragionamento.

![Query e Key producono pesi che combinano i Value](../../../visuals/static/rendered/attention-qkv.png)

La multi-head attention esegue più proiezioni in parallelo. Un residual conserva una strada diretta mentre aggiunge la trasformazione; la normalizzazione controlla la scala; la MLP trasforma separatamente ogni posizione. Ripetere il blocco crea rappresentazioni contestuali profonde.

## Esempio minimo

Tre token hanno Key bidimensionali. La Query del terzo token è più simile alla Key del primo: dopo softmax il primo riceve peso maggiore. L'output non copia necessariamente il primo token; combina i suoi Value. Se il primo Value cambia lasciando uguali le Key, i pesi restano uguali ma cambia l'informazione trasmessa.

## Esempio realistico

Nel completamento di codice, un token può usare definizioni di variabili precedenti. Con un contesto lungo, l'attention piena confronta molte coppie e consuma memoria. Runtime e architetture moderne ottimizzano cache e kernel, ma una context window dichiarata non garantisce uguale qualità a qualunque distanza.

## Livello AI Engineer: equazioni e shape

Per input $X\in\mathbb{R}^{T\times d}$:

$$Q=XW_Q,\quad K=XW_K,\quad V=XW_V$$

$$A=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right),\qquad Y=AV.$$

La maschera $M_{ij}=-\infty$ per $j>i$. Ogni riga di $A$ deve sommare a uno. La divisione per $\sqrt{d_k}$ evita che prodotti scalari grandi saturino la softmax. In implementazione si usa un valore molto negativo compatibile con il dtype e una softmax stabile.

Le proiezioni costano circa $O(Td^2)$; score e combinazione $O(T^2d)$. Durante decoding, la KV cache evita di ricalcolare Key e Value del prefisso, ma cresce approssimativamente in modo lineare con token, layer, head KV e dimensione head.

## Confronto tra implementazioni

Una versione didattica materializza la matrice $T\times T$ ed è leggibile. Kernel come FlashAttention riorganizzano il calcolo in blocchi per ridurre traffico di memoria senza cambiare la funzione matematica nei limiti numerici. Prima si verifica la reference implementation; poi si misura l'ottimizzazione.

## Errori frequenti

- Scambiare Key e Value.
- Dimenticare la maschera o applicarla dopo la softmax.
- Interpretare l'attention come spiegazione causale completa.
- Ignorare batch, head e ordine delle dimensioni.
- Testare solo shape senza verificare che il futuro non influenzi il passato.

## Esercizi A–F

- **A:** calcola a mano pesi su tre token.
- **B:** cambia una Query e prevedi il peso dominante.
- **C:** implementa scaled dot-product attention.
- **D:** trova una maschera applicata sull'asse sbagliato.
- **E:** confronta reference e API framework con test numerici.
- **F:** implementa forward/backward di un piccolo decoder e profila memoria.

## Laboratorio

Usa la visuale, quindi costruisci matrici minuscole in NumPy o nel framework scelto. Test obbligatori: righe softmax pari a 1, nessun NaN, output finite e **causal invariance**: modificare un token futuro non deve alterare output precedenti.

## Verifica rapida

Disegna Q/K/V senza analogie ambigue; calcola una riga di attention; spiega il ruolo di maschera, residual e MLP; indica un limite interpretativo dei pesi.

## Sintesi inclusiva

La Query cerca, la Key permette il confronto, il Value porta informazione. La maschera protegge il futuro. Il Transformer alterna comunicazione fra posizioni e trasformazione locale, mantenendo percorsi residuali. Una figura utile deve sempre mostrare anche shape e direzione temporale.

## Fonti e collegamenti

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [Visuale Q/K/V](../../../visuals/attention-qkv-lab.html)
- Activity: `llm-activity-m05-attention`
