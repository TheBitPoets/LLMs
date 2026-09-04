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

## Come usarle in classe

1. mostrare il primo stato e chiedere una previsione individuale;
2. avanzare soltanto dopo aver raccolto due spiegazioni differenti;
3. modificare una variabile e far motivare l'effetto prima di osservarlo;
4. aprire la vista tecnica usando gli stessi oggetti della vista intuitiva;
5. chiudere con la domanda diagnostica, non con il semplice replay.

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

## Backlog prioritario

| Priorità | Visuale | Modulo | Stato atteso |
| ---: | --- | --- | --- |
| 1 | Token, byte e tokenizer | M03 | Testo modificabile e confronto fra rappresentazioni. |
| 2 | Query, Key e Value | M05 | Attention manuale con pesi e somma dei Value. |
| 3 | MHA, MQA e GQA | M06 | Confronto della condivisione KV e del costo di memoria. |
| 4 | Sampling lab | M12 | Temperature, top-k, top-p e seed sulla stessa distribuzione. |
| 5 | RAG con citazioni | M15 | Query, retrieval, reranking, contesto, risposta e astensione. |
| 6 | Pollicino: probabilità → intervalli → bit | M19 | Codifica e decodifica deterministiche passo per passo. |
