# M06 — Architetture moderne

**Domanda guida:** quali modifiche rendono i Transformer più efficienti o capaci?
**Durata:** 4 ore Practitioner; 12 ore AI Engineer.
**Prerequisiti:** M05.

## Obiettivi osservabili

Saprai riconoscere decoder-only, encoder-only ed encoder-decoder; spiegare intuitivamente RoPE, RMSNorm, SwiGLU, MQA/GQA, MoE e long-context. Il livello AI Engineer collega ogni tecnica al collo di bottiglia che affronta e verifica costi, compatibilità e trade-off.

## Problema iniziale

Due modelli con lo stesso numero di parametri possono richiedere memoria diversa e comportarsi diversamente sul contesto. Il nome “Transformer” descrive una famiglia: dettagli su posizione, normalizzazione, head KV, attivazione e routing cambiano training e inferenza.

## Teoria Practitioner

Un **encoder** rappresenta l'intero input ed è adatto a comprensione; un **decoder causale** genera da sinistra a destra; un **encoder-decoder** separa lettura e generazione. Molti LLM conversazionali moderni sono decoder-only, ma non è una legge universale.

**RoPE** inserisce la posizione ruotando coppie di componenti di Query e Key, così il confronto incorpora distanza relativa. **RMSNorm** normalizza la scala senza sottrarre la media. **SwiGLU** usa un ramo come gate di un altro. Queste tecniche modificano il blocco, non l'obiettivo next-token.

Nella multi-head attention classica ogni head ha Key e Value propri. **MQA** condivide un solo gruppo KV; **GQA** usa un numero intermedio di gruppi. La visuale [MHA, GQA e MQA](../../../visuals/mha-gqa-mqa-memory.html) mostra perché meno head KV riducono la cache durante la generazione.

Un **Mixture of Experts** contiene più MLP esperte e un router attiva solo una parte per token. I parametri totali possono essere molto maggiori di quelli attivi per passo. Ciò aumenta capacità senza costo proporzionale in FLOP, ma introduce routing, comunicazione e bilanciamento.

## Esempio minimo

Con 8 head Query, MHA può avere 8 gruppi KV, GQA 2 e MQA 1. Se il resto è uguale, la parte KV della cache scala con 8, 2 o 1. Non significa che l'intero modello occupi otto volte meno: i pesi e altri tensori restano.

## Esempio realistico

Devi scegliere un modello locale per chat lunga. Un modello GQA quantizzato può lasciare più memoria alla KV cache rispetto a un MHA equivalente. Ma devi misurare qualità sul tuo compito, velocità del runtime e contesto effettivo; il solo limite massimo pubblicizzato non basta.

## Livello AI Engineer: costi e compatibilità

Per batch $B$, lunghezza cache $T$, layer $L$, head KV $H_{kv}$, dimensione head $d_h$ e byte $s$, una stima base è

$$M_{KV}\approx 2BTLH_{kv}d_hs,$$

dove 2 rappresenta Key e Value. Implementazioni, paging e quantizzazione KV cambiano il valore reale. RoPE extrapolation o rescaling può estendere la finestra nominale, ma richiede validazione su compiti sensibili alla posizione.

Nel MoE distingui parametri totali, parametri attivi, capacità del router e comunicazione fra device. Un modello può avere meno FLOP per token di un dense con pari parametri totali ma essere difficile da eseguire su una singola macchina perché tutti i pesi devono essere accessibili.

## Errori frequenti

- Confrontare “parametri” senza distinguere totali e attivi.
- Concludere che long context equivalga a recupero perfetto.
- Attribuire tutta la velocità a GQA ignorando runtime e hardware.
- Applicare una tecnica di scaling RoPE non prevista dal checkpoint.
- Supporre che la stessa sigla garantisca identica implementazione.

## Esercizi A–F

- **A:** riconosci i tre macro-tipi di Transformer.
- **B:** modifica il numero di head KV e aggiorna una stima.
- **C:** costruisci una scheda architetturale da una model card/config.
- **D:** trova incongruenze tra config, pesi e runtime.
- **E:** confronta due modelli su cache, qualità e latenza.
- **F:** implementa GQA o un piccolo router MoE con test di equivalenza.

## Laboratorio

Apri la visuale MHA/GQA/MQA e completa una tabella con $H_q$, $H_{kv}$ e memoria stimata. Verifica poi su un modello reale i campi del file di configurazione e separa dati dichiarati da valori misurati.

## Verifica rapida

Associa ogni tecnica al problema affrontato; calcola il rapporto KV tra MHA e GQA; spiega perché un MoE grande non attiva tutti i parametri; indica un rischio del contesto esteso.

## Sintesi inclusiva

I modelli moderni non cambiano la regola base della previsione, ma rendono calcolo, memoria e capacità più gestibili. Ogni sigla ha un beneficio, un costo e condizioni di validità: imparare a leggerli vale più che memorizzare una classifica.

## Fonti e collegamenti

- [RoFormer / RoPE](https://arxiv.org/abs/2104.09864)
- [GQA](https://arxiv.org/abs/2305.13245)
- [Switch Transformers](https://arxiv.org/abs/2101.03961)
- Activity: `llm-activity-m06-architectures`

