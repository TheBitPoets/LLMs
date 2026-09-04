# M09 — Pesi, formati e licenze

**Domanda guida:** che cosa stiamo realmente scaricando quando scegliamo un modello locale?
**Durata:** 3 ore Practitioner; 8 ore AI Engineer.
**Prerequisiti:** M01 e M06.

## Obiettivi osservabili

Saprai leggere una model card, distinguere architettura, checkpoint, precisione, quantizzazione, formato e licenza; scegliere un artefatto compatibile con runtime e uso. Il livello AI Engineer ispeziona metadati, shard, tensori e conversioni e costruisce una supply chain riproducibile.

## Problema iniziale

Lo stesso nome di modello compare in file da dimensioni diverse: originale BF16, quantizzazioni a 8 o 4 bit, conversioni GGUF e varianti fine-tuned. Non sono intercambiabili. Una scelta sbagliata può non caricarsi, produrre output degradato o violare la licenza.

## Teoria Practitioner

L'**architettura** definisce le operazioni e la forma dei tensori. Il **checkpoint** contiene valori appresi in una revisione. Un **formato contenitore** organizza tensori e metadati; `safetensors` evita deserializzazione di codice arbitrario tipica di formati più generici, mentre `GGUF` è progettato per ecosistemi di inferenza come llama.cpp e può includere tokenizer e metadati.

La **precisione** descrive la rappresentazione numerica, per esempio FP32, BF16 o FP16. La **quantizzazione** mappa valori in formati più compatti con scale e gruppi. Sigle come Q4 non specificano da sole algoritmo, group size o qualità.

Una licenza può consentire i pesi ma imporre condizioni su uso commerciale, ridistribuzione, utenti o derivati. Controlla testo della licenza, model card e provenienza dell'artefatto; una conversione comunitaria non eredita magicamente affidabilità.

## Esempio minimo

Un modello da 7 miliardi di parametri richiede circa 14 GB solo per pesi a 2 byte, prima di cache e overhead. Una quantizzazione nominale a 4 bit suggerisce circa 3,5 GB grezzi, ma scale, metadati e allineamenti aumentano il file. La dimensione su disco non coincide esattamente con memoria residente.

## Esempio realistico

Per scegliere un artefatto annota: repository, commit o digest, file, hash, architettura, tokenizer, chat template, quantizzazione, licenza, runtime minimo e fonte. Prova il caricamento offline dopo il download. Se il tag può cambiare, non è sufficiente per un esperimento riproducibile.

## Livello AI Engineer: ispezione e conversione

I grandi checkpoint possono essere suddivisi in shard con un indice che mappa tensori e file. Una conversione deve preservare nomi, shape, tokenizer, token speciali, configurazione RoPE e tying dei pesi. Dopo conversione esegui test su logits o output con tolleranza dichiarata, non solo “il file si apre”.

Il formato non determina da solo il kernel: runtime diversi possono leggere lo stesso contenitore con implementazioni differenti. Distingui peso quantizzato staticamente, quantizzazione dinamica delle attivazioni e quantizzazione della KV cache. Registra tool e versione della conversione per evitare artefatti non ricostruibili.

Per la supply chain verifica hash, firma quando disponibile, identità dell'autore, dipendenze e codice remoto. Evita `trust_remote_code` senza review e sandbox. Conserva SBOM o almeno inventario di modelli e licenze.

## Scheda di decisione

| Campo | Domanda |
| --- | --- |
| Capacità | il checkpoint è adatto al task e alla lingua? |
| Memoria | pesi, KV cache e overhead entrano? |
| Runtime | architettura e quantizzazione sono supportate? |
| Licenza | uso e ridistribuzione sono consentiti? |
| Provenienza | repository, revisione e hash sono affidabili? |
| Template | prompt e token speciali sono quelli previsti? |

## Errori frequenti

- Usare soltanto il numero di parametri per scegliere.
- Confondere formato file e precisione numerica.
- Trattare tutti i “4 bit” come equivalenti.
- Scaricare una conversione senza provenienza o hash.
- Ignorare chat template e tokenizer.
- Copiare nel repository libri o asset licensed usati solo come riferimento.

## Esercizi A–F

- **A:** associa formato, dtype e quantizzazione alle definizioni.
- **B:** completa una model card incompleta.
- **C:** confronta tre artefatti con la scheda di decisione.
- **D:** trova incompatibilità tra config e pesi.
- **E:** converti un modello piccolo e verifica equivalenza entro tolleranza.
- **F:** costruisci pipeline firmata di acquisizione, scan, conversione e rollback.

## Laboratorio

Compila `docs/course/templates/model-decision.md` per due candidati. Esegui `python3 labs/course_lab.py memory` come prima stima, quindi confronta dimensione file e memoria misurata quando il runtime sarà disponibile.

## Verifica rapida

Spiega checkpoint contro architettura; formato contro quantizzazione; elenca i dati necessari a fissare un artefatto; interpreta una condizione di licenza senza sostituirti a una consulenza legale.

## Sintesi inclusiva

Il nome del modello non basta. Per usare pesi locali servono artefatto preciso, tokenizer, template, formato, quantizzazione, runtime e licenza compatibili. Una scelta riproducibile è identificata da revisioni e hash, non da un'etichetta mobile.

## Fonti e collegamenti

- [safetensors](https://github.com/huggingface/safetensors)
- [GGUF](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md)
- [Inventario Manning](../sources/manning-inventory-and-selection.md)
- Activity: `llm-activity-m09-model-selection`
