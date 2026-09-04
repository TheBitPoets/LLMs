# M05 - Attention e Transformer

**Domanda guida:** come sceglie quali parti del contesto usare?  
**Durata:** 5 ore Practitioner; 16 ore AI Engineer.  
**Prerequisiti:** M03–M04; matrici e softmax per l'estensione.

## Obiettivi osservabili

Seguire embedding→attention causale→residual/norm→MLP→logits; distinguere
Query, Key e Value; spiegare maschera causale e multi-head. L'AI Engineer
implementa forward/backward di un blocco decoder e ne verifica shape e causalità.

## Lezione intuitiva

Ogni token crea una **Query**, cioè ciò che cerca in quello specifico head. Le
**Key** permettono il confronto; i **Value** contengono l'informazione da
mescolare. La softmax trasforma gli score in pesi. Un token futuro viene
mascherato perché durante la generazione non esiste ancora.

Aprire [Attention Q/K/V](../../../visuals/attention-qkv-lab.html), cambiare
Query e disattivare temporaneamente la maschera. Il peso più alto non è una
spiegazione universale: cambia per head, layer e Query.

Il residual è una strada principale a cui si aggiunge una trasformazione; la
normalizzazione mantiene scale gestibili; la MLP trasforma ogni posizione. Il
blocco ripetuto costruisce rappresentazioni sempre più contestuali.

## Matematica AI Engineer

`Q=XW_Q`, `K=XW_K`, `V=XW_V`; `A=softmax(QKᵀ/√d_k + M)` e `Y=AV`. La maschera
`M_ij=-∞` per `j>i`. Verificare che ogni riga di `A` sommi a 1 e che modificare
un token futuro non alteri gli output precedenti. Derivare costi approssimati:
projection `O(Td²)`, attention score/value `O(T²d)`.

## Laboratorio e verifica

Calcolo manuale su tre token; implementazione NumPy/PyTorch confrontata con un
riferimento; test causale e finite values. Verifica: diagramma 3, calcolo 3,
causalità 2, limite interpretativo 2. Fonte primaria:
[Vaswani et al. 2017](https://arxiv.org/abs/1706.03762).

