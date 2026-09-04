# M09 - Pesi, formati e licenze

**Domanda guida:** che cosa scarichiamo davvero?  
**Durata:** 3 ore Practitioner; 8 ore AI Engineer.  
**Prerequisiti:** M01 e M06.

## Obiettivi osservabili

Identificare config, tokenizer, template, shard di pesi, dtype, quantizzazione,
licenza e hash; distinguere open source, open-weight e API. L'AI Engineer
ispeziona safetensors e GGUF senza eseguire codice non fidato.

## Lezione intuitiva

Un “modello” scaricato è un bundle di contratti. La config dice come assemblare
i tensori; il tokenizer mappa testo/ID; il template costruisce i turni; i pesi
contengono numeri; la licenza stabilisce usi e redistribuzione. Un file GGUF può
riunire metadati, tokenizer e tensori quantizzati per runtime locali;
safetensors è progettato per tensori con formato ispezionabile senza pickle.

Open-weight significa accesso ai pesi secondo una licenza, non necessariamente
codice, dati e processo di training completamente aperti. “Gratis da scaricare”
non equivale a “senza condizioni”.

## Laboratorio

Eseguire `ollama show` e ispezionare una model card. Registrare nome/tag/digest,
famiglia, parametri, quantizzazione, context, template e licenza. Baseline:
manifest vuoto che deve fallire il gate. Test negativo: mismatch tokenizer/pesi
o licenza non trovata.

## AI Engineer

Leggere header e tensor directory di un file piccolo; verificare shape attese e
hash; confrontare FP32, BF16, FP16, INT8/4 concettualmente. Vietare il caricamento
di pickle non fidato nel percorso base.

## Verifica

Manifest 5, distinzione apertura/licenza 2, integrità 2, rischio supply-chain 1.
Fonti: specifiche ufficiali [safetensors](https://github.com/huggingface/safetensors)
e [GGUF](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md).

