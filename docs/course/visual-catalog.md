# Catalogo delle visualizzazioni

Le figure dei testi sono usate come fonti di confronto private. Gli asset
pubblicati qui sono ricostruzioni originali: evidenziano un cambiamento per
passo, dichiarano i limiti dell'analogia e possono essere usati con mouse,
tastiera o stampa.

| Visuale | Moduli | Errore concettuale contrastato | Interazioni | Fonte concettuale |
| --- | --- | --- | --- | --- |
| [Il ciclo next-token](../../visuals/next-token-prediction.html) | M02, M12 | Il modello recupera una frase completa o la temperatura lo rende più competente. | Passi, play/pausa, temperatura, reset. | Softmax e generazione autoregressiva; esempio originale. |
| [Dove viaggia il prompt?](../../visuals/local-vs-cloud-data-journey.html) | M01, M11, M13 | Locale significa automaticamente sicuro; cloud e locale sono categorie di qualità. | Tre scenari, percorso in cinque passi, play/pausa. | Kamigusa, *Build Applications with Local AI Models on a Mac*, MEAP V06, figure 1.1 e 3.2. |
| [Da `ollama run` alla risposta](../../visuals/ollama-request-and-memory.html) | M10, M11, M18 | Il file su disco è già eseguibile; la dimensione dei pesi coincide con tutta la memoria necessaria. | Parametri, bit, contesto, RAM, ciclo richiesta. | Kamigusa, stesso volume, figura 3.1 e sezioni 4.3–4.4. |
| [Dal testo ai numeri](../../visuals/token-byte-embedding-lab.html) | M03 | Il modello vede parole; caratteri, byte, token e ID sono equivalenti. | Testo libero, quattro viste, embedding illustrativo. | Sintesi originale dei meccanismi di tokenizzazione ed embedding. |
| [Attention: Query, Key e Value](../../visuals/attention-qkv-lab.html) | M05 | Attention recupera una parola o costituisce da sola una spiegazione del modello. | Query selezionabile, maschera causale, score, softmax e somma dei Value. | Vaswani et al., *Attention Is All You Need* (2017). |
| [Pollicino: dalle probabilità ai bit](../../visuals/pollicino-probabilities-to-bits.html) | M02, M19 | Una previsione probabilistica non può contribuire a una ricostruzione esatta. | Messaggio A/B modificabile, intervalli progressivi, bit e decodifica. | Codifica aritmetica adattiva e roadmap `kinderp/pollicino`; esempio originale. |
| [MHA, GQA e MQA](../../visuals/mha-gqa-mqa-memory.html) | M06, M10, M18 | Parametri totali, attivi e KV cache sono la stessa quantità. | Query head, gruppi KV, contesto e stima memoria. | GQA e model config moderne; esempio originale. |
| [Sampling controls](../../visuals/sampling-controls-lab.html) | M02, M12 | Sampling e temperature migliorano la conoscenza del modello. | Temperature, top-k, top-p, seed e 12 estrazioni. | Strategie di decoding; esempio originale. |
| [RAG: dalla domanda alla citazione](../../visuals/rag-evidence-journey.html) | M14, M15, M16 | Una fonte recuperata è automaticamente corretta e può impartire istruzioni. | Fonte trovata/assente/ostile e pipeline in cinque gate. | RAG, provenance bundle e prompt-injection defense. |
| [Prefill, decode e KV cache](../../visuals/prefill-decode-kv-cache.html) | M10, M13, M18 | Prompt e output hanno lo stesso profilo di costo; streaming elimina il calcolo. | Lunghezze prompt/output e cambio fase. | Serving autoregressivo e KV cache; esempio originale. |

## Come usarle in classe

1. mostrare il primo stato e chiedere una previsione individuale;
2. avanzare soltanto dopo aver raccolto due spiegazioni differenti;
3. modificare una variabile e far motivare l'effetto prima di osservarlo;
4. aprire la vista tecnica usando gli stessi oggetti della vista intuitiva;
5. chiudere con la domanda diagnostica, non con il semplice replay.

## Figure statiche per le dispense

Le animazioni non sono adatte alla stampa. Il volume usa sette ricostruzioni
SVG originali che conservano le relazioni essenziali e restano nitide in A4:

| Figura | Modulo | Versione interattiva collegata |
| --- | --- | --- |
| `visuals/static/local-cloud.svg` | M01 | percorso locale/cloud |
| `visuals/static/next-token.svg` | M02 | ciclo next-token |
| `visuals/static/token-embedding.svg` | M03 | testo, byte, token, embedding |
| `visuals/static/attention-qkv.svg` | M05 | attention Q/K/V |
| `visuals/static/rag-pipeline.svg` | M15 | RAG ed evidenza |
| `visuals/static/prefill-decode.svg` | M18 | prefill, decode e KV cache |
| `visuals/static/pollicino-codec.svg` | M19 | probabilità, coder e checksum |

Gli SVG non incorporano scansioni, illustrazioni o testi Manning. Sono stati
disegnati per questo corso a partire dalle relazioni tecniche citate nei moduli.

## Provenienza e trasformazione

Le coordinate bibliografiche indicano la relazione o il problema didattico
studiato, non una licenza a riprodurre l'impaginazione. Per ogni nuovo asset si
registrano:

- fonte e coordinata consultata;
- errore concettuale che la nuova figura deve ridurre;
- relazioni conservate e semplificazioni introdotte;
- interazione aggiunta e sua funzione didattica;
- limite dichiarato e verifica diagnostica;
- assenza o autorizzazione di eventuale materiale editoriale incorporato.

## Backlog successivo non bloccante

Le dieci visuali interattive e le sette figure statiche coprono il nucleo
concettuale e i laboratori principali. La
seconda iterazione potrà aggiungere loss landscape, RoPE tridimensionale,
post-training, formati GGUF/safetensors e un profiler con tracce hardware reali.
