# M18 — Sistemi e kernel d'inferenza

**Domanda guida:** che cosa accade fra i tensori del modello e l'hardware?
**Durata:** 3 ore Practitioner; 18 ore AI Engineer.
**Prerequisiti:** M05–M06 e M10–M11; programmazione parallela per l'estensione.

## Obiettivi osservabili

Saprai distinguere prefill, decode, KV cache, batching e serving; leggere un profilo di latenza. Il livello AI Engineer implementa una reference kernel, ragiona su layout, tiling, fusion e precisione e confronta correttezza e prestazioni.

## Problema iniziale

Due runtime eseguono gli stessi pesi sullo stesso hardware, ma uno produce il primo token prima e l'altro più token al secondo. Il modello matematico è simile; scheduler, cache, kernel, layout e batching cambiano l'esecuzione.

## Teoria Practitioner

Nel **prefill** il runtime elabora in parallelo i token del prompt e costruisce la KV cache. Nel **decode** genera un token per sequenza alla volta riusando la cache. Un prompt lungo aumenta il prefill; un output lungo moltiplica i passi di decode.

Apri [Prefill, decode e KV cache](../../../visuals/prefill-decode-kv-cache.html). La cache scambia memoria per calcolo evitato. Il batching statico raggruppa richieste intere; il continuous batching inserisce e rimuove sequenze durante il servizio. Paged KV cache riduce frammentazione e permette gestione più flessibile.

![Prefill e decode hanno profili di lavoro differenti](../../../visuals/static/rendered/prefill-decode.png)

## Esempio minimo

Per una moltiplicazione di matrici, una versione con tre loop è facile da verificare. Una versione tiled carica blocchi in memoria più vicina e riusa i dati. Se il tile o gli indici sono sbagliati, può essere veloce ma scorretto: il reference output è il primo gate.

## Esempio realistico

Profila una richiesta Ollama o llama.cpp e separa model load, tokenization, prefill, decode e rendering. Ripeti con prompt e output di lunghezze controllate. Se token/s resta simile ma TTFT cresce col prompt, il collo di bottiglia è coerente con il prefill; serve comunque un profiler per attribuzione più precisa.

## Livello AI Engineer: arithmetic intensity

Il roofline confronta picco di compute e bandwidth. L'arithmetic intensity è operazioni per byte trasferito. Un kernel è memory-bound quando il limite $\text{bandwidth}\times\text{intensity}$ è sotto il picco di compute. Il decode batch-1 spesso riusa poco i pesi; il prefill con matrici più grandi può utilizzare meglio il compute.

FlashAttention calcola softmax attention a blocchi, mantenendo statistiche online e riducendo letture/scritture della matrice completa. La funzione resta attention esatta entro differenze floating-point. Kernel fusion evita round trip in memoria fra operazioni come bias, activation e scaling.

Un kernel deve specificare shape, stride, dtype, allineamento, dispositivi e tolleranza. I test includono casi piccoli, dimensioni non multiple del tile, valori estremi, NaN policy e confronto con reference. Il benchmark richiede warm-up, sincronizzazione e statistiche robuste.

## Dal reference al kernel

1. Scrivi equazione e implementazione lenta leggibile.
2. Genera fixture e test numerici.
3. Profila e identifica il collo di bottiglia.
4. Cambia layout, tiling o fusion una cosa alla volta.
5. Verifica di nuovo correttezza e stabilità.
6. Misura su shape rappresentative, non solo favorevoli.

## Errori frequenti

- Cronometrare operazioni asincrone senza sincronizzare.
- Confrontare kernel su dtype o shape diversi.
- Ottimizzare prima di avere una reference.
- Ignorare copie host-device e conversioni.
- Misurare solo throughput e non latenza o memoria.
- Dichiarare velocità da un singolo run caldo.

## Esercizi A–F

- **A:** classifica fasi prefill e decode.
- **B:** modifica lunghezza prompt/output e predici il costo.
- **C:** implementa e misura una matmul reference.
- **D:** trova un benchmark asincrono errato.
- **E:** ottimizza un kernel con test di tolleranza.
- **F:** integra un kernel nel runtime con dispatch, fallback e benchmark CI.

## Laboratorio

Esegui `python3 labs/course_lab.py serving`. Costruisci prima una simulazione di scheduling. Nel livello avanzato implementa softmax o matmul in NumPy/framework e una versione ottimizzata; riporta accelerazione solo dopo equivalenza entro tolleranza.

## Verifica rapida

Spiega prefill contro decode; indica perché serve KV cache; descrivi memory-bound; mostra protocollo corretto di benchmark e almeno un caso limite.

## Sintesi inclusiva

Il runtime traduce il grafo in lavoro sull'hardware. Prefill e decode hanno profili diversi; cache e batching cambiano memoria e latenza. Un kernel è valido prima perché corretto, poi perché veloce su workload rappresentativi.

## Fonti e collegamenti

- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180)
- [Visuale prefill/decode](../../../visuals/prefill-decode-kv-cache.html)
- Activity: `llm-activity-m18-inference-kernel`
