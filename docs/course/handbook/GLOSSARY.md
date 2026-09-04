# Glossario essenziale LLM

Le definizioni sono operative: indicano come usare il termine nel corso. Le grandezze dipendenti da una release appartengono al catalogo datato, non al glossario.

| Termine | Definizione operativa |
| --- | --- |
| Agente | Sistema che sceglie iterativamente passi o tool in base allo stato e alle osservazioni. |
| Alignment | Insieme di tecniche e valutazioni che orientano il comportamento verso obiettivi e vincoli umani. |
| Attention | Operazione che combina Value usando pesi derivati dal confronto fra Query e Key. |
| Baseline | Soluzione di confronto semplice, fissata prima di valutare una proposta. |
| Batch | Gruppo di sequenze elaborato insieme in training o inferenza. |
| Benchmark | Protocollo, dataset e metriche usati per confrontare sistemi; non è una proprietà assoluta del modello. |
| BPE | Tokenizzazione subword che apprende fusioni frequenti di unità più piccole. |
| Checkpoint | Stato concreto dei pesi, identificato da revisione o hash. |
| Chunk | Unità documentale indicizzata e recuperata in una pipeline RAG. |
| Cloud model | Modello eseguito dietro un servizio remoto; non specifica se i pesi siano aperti. |
| Constrained decoding | Selezione dei token limitata da una grammatica o da vincoli formali. |
| Context window | Numero massimo di token che una configurazione può trattare; non garantisce qualità uniforme a ogni distanza. |
| Cross-entropy | Loss che penalizza la bassa probabilità assegnata al token osservato. |
| Data leakage | Informazione del test o del futuro che entra impropriamente nel training o nella scelta del sistema. |
| Decode | Fase autoregressiva che produce nuovi token, normalmente uno per sequenza e passo. |
| Digest | Identificatore derivato dal contenuto, utile per fissare un artefatto. |
| Distillazione | Trasferimento di comportamento o distribuzioni da un teacher a uno student. |
| Embedding | Vettore appreso che rappresenta un token o un oggetto per il calcolo. |
| Entropia | Incertezza media di una distribuzione; in base 2 si misura in bit. |
| Eval set | Insieme versionato di casi con criteri attesi usato per valutare. |
| Fine-tuning | Aggiornamento di tutti o parte dei parametri su dati e obiettivi successivi al pre-training. |
| GQA | Grouped-Query Attention: più head Query condividono un numero minore di head Key/Value. |
| Grounding | Legame verificabile tra risposta e informazioni fornite o recuperate. |
| Hallucination | Contenuto non supportato presentato in modo plausibile; va scomposto in categorie misurabili. |
| Inference | Uso di pesi addestrati per calcolare output senza normale aggiornamento dei parametri. |
| KV cache | Key e Value dei token precedenti conservati per evitare ricalcolo durante decode. |
| Latency | Tempo per una richiesta; specificare TTFT, tempo totale e condizioni. |
| Logit | Punteggio non normalizzato prodotto prima della softmax. |
| LoRA | Adattamento a basso rango che apprende matrici aggiuntive mantenendo congelato il peso base. |
| Loss | Funzione scalare ottimizzata durante training; non coincide direttamente con verità o utilità. |
| MCP | Protocollo per esporre strumenti e risorse a client AI; non sostituisce autorizzazione e sandbox. |
| MHA | Multi-Head Attention con proiezioni multiple; nella forma standard ogni head ha propri K/V. |
| Model card | Documento su capacità, dati, uso previsto, valutazioni, rischi e limiti di un modello. |
| MoE | Mixture of Experts: router che attiva un sottoinsieme di moduli esperti per token. |
| MQA | Multi-Query Attention: le head Query condividono un solo gruppo Key/Value. |
| Open weight | Pesi ottenibili secondo una licenza; non implica apertura di dati, training o uso illimitato. |
| Parameter | Valore appreso del modello; il conteggio non misura da solo capacità o costo effettivo. |
| Perplexity | Esponenziale della cross-entropy media; confrontabile solo con protocollo e tokenizzazione coerenti. |
| Post-training | Fasi successive al pre-training, come SFT, preferenze, RL o distillazione. |
| Precisione numerica | Formato usato per rappresentare valori, per esempio FP32, BF16 o FP16. |
| Prefill | Elaborazione del prompt che costruisce rappresentazioni e KV cache. |
| Prompt injection | Istruzione non fidata che tenta di deviare il sistema o ottenere privilegi. |
| Quantizzazione | Rappresentazione approssimata e più compatta di pesi, attivazioni o cache. |
| RAG | Retrieval-Augmented Generation: recupero di contenuti seguito da generazione condizionata. |
| Reasoning model | Modello o sistema ottimizzato per spendere calcolo aggiuntivo su compiti multi-passo; va valutato sul risultato. |
| Retrieval | Selezione e ranking di documenti o chunk rispetto a una query. |
| RoPE | Positional encoding che applica rotazioni a Query e Key per incorporare la posizione. |
| Runtime | Software che carica i pesi ed esegue operatori e kernel sul dispositivo. |
| Sampling | Scelta stocastica di un token dalla distribuzione filtrata. |
| Seed | Stato iniziale di un generatore pseudo-casuale; da solo non garantisce ripetibilità cross-runtime. |
| SFT | Supervised Fine-Tuning su coppie istruzione-risposta o sequenze curate. |
| Softmax | Trasformazione che converte logits in valori positivi normalizzati. |
| Structured output | Output vincolato o validato rispetto a uno schema; garantisce struttura, non verità. |
| Temperature | Scala applicata ai logits prima del campionamento per modificare la concentrazione. |
| Token | Unità discreta prodotta dal tokenizer; non coincide necessariamente con una parola. |
| Tokenizer | Procedura e vocabolario che convertono testo/byte in ID e viceversa. |
| Tool call | Proposta strutturata di chiamata a una funzione; l'applicazione deve validare e autorizzare. |
| Top-k | Filtro che conserva i k token con probabilità più alta. |
| Top-p | Filtro che conserva il più piccolo insieme con massa cumulativa almeno p. |
| Training | Processo che usa dati e gradienti per aggiornare i parametri. |
| Transformer | Architettura basata su attention, trasformazioni per posizione, residual e normalizzazione. |
| TTFT | Time To First Token: tempo dalla richiesta al primo token disponibile. |
| Validation set | Dati separati usati per scegliere configurazioni senza consumare il test finale. |

