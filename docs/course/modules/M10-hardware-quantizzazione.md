# M10 — Hardware e quantizzazione

**Domanda guida:** quale modello entra davvero nella macchina e a quale velocità?
**Durata:** 4 ore Practitioner; 12 ore AI Engineer.
**Prerequisiti:** M06 e M09.

## Obiettivi osservabili

Saprai stimare memoria di pesi e KV cache, distinguere RAM/VRAM, bandwidth e compute, misurare time-to-first-token e token/s e confrontare quantizzazioni. Il livello AI Engineer analizza roofline, batching, offload e metodi weight-only o weight-activation.

## Problema iniziale

Un file da 20 GB entra in una macchina con 36 GB di memoria? Forse. Oltre ai pesi servono runtime, cache, buffer e sistema operativo; il contesto e il parallelismo cambiano il picco. “Si scarica” non significa “si esegue bene”.

## Teoria Practitioner

La capacità di memoria decide se il carico è possibile. La **bandwidth** misura quanto rapidamente i dati arrivano alle unità di calcolo; i **FLOPS/TOPS** stimano operazioni, ma formato e kernel devono usarle. CPU, GPU e acceleratori hanno gerarchie e supporto differenti. Nella memoria unificata, CPU e GPU condividono lo stesso pool, ma restano pressione, bandwidth e limiti del sistema.

La quantizzazione riduce la rappresentazione dei pesi e talvolta di attivazioni o cache. Modelli più compatti possono essere più veloci e lasciare spazio al contesto, ma la perdita di qualità dipende da metodo, layer, task e runtime. Non esiste “la” qualità dei 4 bit.

Apri [Ollama e memoria](../../../visuals/ollama-request-and-memory.html). Separa **TTFT**, il tempo prima del primo token, da **decode throughput**, i token generati al secondo. Prefill e decode hanno colli di bottiglia diversi.

## Esempio minimo

Pesi grezzi: $M_w\approx N b/8$, con $N$ parametri e $b$ bit medi. Un modello 8B a 4 bit richiede circa 4 GB grezzi, non il totale reale. Aggiungi metadati, scale, buffer e KV cache. Applica margine invece di occupare il 100% della memoria.

## Esempio realistico

Sul Mac M4 Pro 36 GB selezioni tre tag Ollama: piccolo, medio e più grande quantizzato. Per ciascuno registri download, memoria idle e picco, TTFT, token/s, qualità su fixture e temperatura del sistema. La scelta per la classe privilegia affidabilità e tempi prevedibili, non il massimo numero di parametri caricabile una volta.

## Livello AI Engineer: stime e roofline

La KV cache base è

$$M_{KV}\approx2BTLH_{kv}d_hs.$$

Il fattore 2 rappresenta Key e Value. Paged attention, cache quantizzata e allocatori aggiungono dettagli. Nel decode a batch piccolo si rileggono molti pesi per produrre pochi token: spesso il limite è la bandwidth. Con batch maggiore si riusa meglio il peso ma crescono latenza e memoria.

Metodi weight-only conservano attivazioni a precisione maggiore; W8A8 quantizza anche attivazioni e richiede kernel compatibili. Group size più piccolo usa più scale e può preservare qualità, ma aumenta overhead. Per confrontare quantizzazioni usa stesso checkpoint sorgente, template, dataset e runtime.

## Protocollo di misura

1. Riavvia o stabilizza lo stato e registra processi concorrenti.
2. Separa cold start da richieste successive.
3. Fissa prompt, output token, context length e seed quando disponibile.
4. Ripeti e riporta mediana e dispersione, non solo il caso migliore.
5. Registra picco di memoria, TTFT, token/s ed energia se misurabile.
6. Valuta qualità sul task reale e annota errori.

## Errori frequenti

- Usare la dimensione del file come RAM esatta.
- Confrontare token/s con output o contesti diversi.
- Scambiare TTFT e velocità di decode.
- Credere che una GPU con più FLOPS sia sempre più veloce.
- Riempire tutta la memoria senza margine operativo.

## Esercizi A–F

- **A:** stima memoria grezza di quattro modelli.
- **B:** cambia contesto e aggiorna la KV cache.
- **C:** costruisci un foglio di budget completo.
- **D:** trova errori in un benchmark non controllato.
- **E:** confronta due quantizzazioni su qualità e prestazioni.
- **F:** profila un serving multiutente e proponi batching/offload.

## Laboratorio

Esegui `python3 labs/course_lab.py memory` e completa prima le stime. Il rehearsal reale usa `docs/course/rehearsal/README.md`: non inventare dati hardware prima dell'esecuzione. Conserva un manifest distinto per ogni artefatto.

## Verifica rapida

Calcola pesi grezzi; spiega perché il totale è maggiore; distingui bandwidth e compute; motiva una quantizzazione senza dire soltanto “occupa meno”.

## Sintesi inclusiva

Prima di scaricare, fai un budget. Memoria abilita il modello; bandwidth, kernel e batch determinano gran parte della velocità. Quantizzare è un compromesso misurabile tra spazio, prestazioni e qualità.

## Fonti e collegamenti

- [Visuale richiesta e memoria](../../../visuals/ollama-request-and-memory.html)
- [Visuale KV cache](../../../visuals/prefill-decode-kv-cache.html)
- [Rehearsal](../rehearsal/README.md)
- Activity: `llm-activity-m10-memory-budget`

