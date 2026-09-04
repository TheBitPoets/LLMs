# Timeline ragionata delle idee che hanno costruito gli LLM

La timeline usa la catena **problema → idea → evidenza → adozione → limite**.
Non richiede allo studente Practitioner di leggere integralmente ogni paper;
l'AI Engineer riproduce in scala almeno le voci marcate con ★.

## Fondamenti dell'informazione e del linguaggio neurale

| Anno | Lavoro | Problema e idea centrale | Esperimento del corso | Limite da ricordare |
| ---: | --- | --- | --- | --- |
| 1948 | Shannon, *A Mathematical Theory of Communication* | Quantificare informazione e limite della compressione tramite entropia. | ★ Frequenze, surprisal e arithmetic coding nel percorso Pollicino. | Un buon codice richiede una buona distribuzione e un contratto condiviso. |
| 2003 | Bengio et al., *A Neural Probabilistic Language Model* | Combattere la sparsità degli n-gram con rappresentazioni distribuite e rete neurale. | Confronto n-gram/MLP next-symbol. | Contesto corto e costo di calcolo dell'epoca. |
| 2013 | Mikolov et al., word2vec | Imparare vettori utili da compiti predittivi efficienti. | Similarità e analogie con controllo negativo. | Le analogie non rendono l'embedding una mappa semantica perfetta. |
| 2014 | Bahdanau et al., neural machine translation with attention | Evitare un singolo collo di bottiglia usando pesi dinamici sulle rappresentazioni. | Visuale Q/K/V come ponte, chiarendo la differenza dall'attention originale. | I pesi non sono automaticamente spiegazioni causali. |

## Transformer e pre-training

| Anno | Lavoro | Problema e idea centrale | Esperimento del corso | Limite da ricordare |
| ---: | --- | --- | --- | --- |
| 2017 | Vaswani et al., *Attention Is All You Need* | Parallelizzare la sequenza con self-attention, posizione, residual e MLP. | ★ Attention manuale e piccolo blocco causale. | Costo quadratico standard con la lunghezza del contesto. |
| 2018 | Devlin et al., BERT | Pre-training bidirezionale per rappresentazioni e task discriminativi. | Confronto mascherato vs autoregressivo. | Non è lo stesso obiettivo di un decoder generativo. |
| 2018–19 | GPT e GPT-2 technical reports | Pre-training autoregressivo seguito da adattamento/zero-shot. | Training next-token su corpus giocattolo. | Capacità emergenti non eliminano errori e dipendenza dai dati. |
| 2020 | Brown et al., GPT-3 | Scaling e in-context learning con 175B parametri. | Few-shot vs zero-shot con ordine esempi variato. | Benchmark e prompt sensitivity; costi e opacità dei dati. |
| 2020 | Kaplan et al., scaling laws | Descrivere trend regolari tra compute, dati, parametri e loss. | Piccolo scaling sweep. | Una legge empirica nel regime osservato non è una garanzia universale. |
| 2022 | Hoffmann et al., Chinchilla | Correggere modelli troppo grandi e sotto-addestrati bilanciando dati/parametri. | Budget fisso e confronto di configurazioni. | Ricetta dipendente da obiettivo, dati e regime hardware. |

## Architetture efficienti e contesto

| Anno | Lavoro | Idea | Esperimento | Limite |
| ---: | --- | --- | --- | --- |
| 2019 | Zhang & Sennrich, RMSNorm | Normalizzazione più semplice senza ricentramento. | ★ Implementazione confrontata con LayerNorm. | Stabilità dipende dall'intero training setup. |
| 2020 | Shazeer, GLU variants | Gating nelle MLP Transformer, inclusa SwiGLU. | Ablation ReLU/GELU/SwiGLU. | Più parametri/costo se dimensioni non riequilibrate. |
| 2021 | Su et al., RoFormer/RoPE | Codificare posizione ruotando coppie di dimensioni di Q/K. | ★ Rotazione 2D e test di posizione relativa. | Estensione oltre il training richiede attenzione e valutazione. |
| 2022 | Dao et al., FlashAttention | Calcolo exact attention IO-aware senza materializzare l'intera matrice in HBM. | Profilo reference vs kernel ottimizzato disponibile. | “Exact” riguarda il meccanismo, non bit-identical tra ogni precisione/hardware. |
| 2023 | Ainslie et al., GQA | Condividere gruppi KV tra query head, compromesso MHA/MQA. | Visuale e stima KV cache. | La qualità va misurata dopo conversione/training. |
| 2023 | Kwon et al., vLLM/PagedAttention | Ridurre frammentazione della KV cache nel serving. | Simulatore di pagine e batching. | Ottimizza serving, non la qualità del modello. |
| 2023 | Gu & Dao, Mamba | State-space selective per sequenze con costo lineare. | Confronto concettuale stato ricorrente/attention. | Ecosistema, training e task possono favorire ibridi. |
| 2024 | DeepSeek-V2, Multi-head Latent Attention | Comprimere rappresentazioni KV per ridurre costo di inferenza. | Calcolo memoria MLA vs GQA semplificato. | Dipende da architettura e pesi addestrati per il metodo. |

## Istruzioni, preferenze e reasoning

| Anno | Lavoro | Idea | Esperimento | Limite |
| ---: | --- | --- | --- | --- |
| 2022 | Ouyang et al., InstructGPT | SFT + preference data + RLHF per seguire intenzioni meglio del solo pre-training. | Mappa base→SFT→reward→policy e confronto output. | Preferenze dei labeler e reward hacking. |
| 2022 | Wei et al., Chain-of-Thought | Esempi con passaggi intermedi migliorano alcuni compiti di reasoning. | Prompt ablation con score sull'esito, non sulla retorica. | Testo plausibile non prova che il ragionamento interno sia fedele. |
| 2022 | Wang et al., Self-Consistency | Campionare più catene e aggregare la risposta. | Accuratezza vs costo e diversità. | Moltiplica inferenza; errori correlati possono prevalere. |
| 2023 | Rafailov et al., DPO | Ottimizzare preferenze con obiettivo diretto senza esplicito reward model online. | ★ Loss DPO su coppie sintetiche. | Qualità e copertura delle preferenze restano decisive. |
| 2025 | DeepSeek-R1 | RL con reward verificabile e pipeline di distillazione per reasoning. | Confronto base/reasoning/distillato su problemi verificabili. | Output lunghi, reward specifici e benchmark contamination. |

## Adattamento, retrieval e applicazioni

| Anno | Lavoro | Idea | Esperimento | Limite |
| ---: | --- | --- | --- | --- |
| 2020 | Lewis et al., RAG | Recuperare documenti e condizionare la generazione su fonti esterne. | ★ Retrieval, contesto, citazione e astensione. | Retrieval sbagliato e prompt injection nei documenti. |
| 2021 | Hu et al., LoRA | Aggiornamenti low-rank al posto del fine-tuning di tutti i pesi. | ★ Adapter piccolo vs baseline prompt/RAG. | Non aggiunge affidabilmente conoscenza senza dati adeguati. |
| 2023 | Dettmers et al., QLoRA | Backpropagation attraverso base quantizzata 4-bit con adapter. | Stima memoria e riproduzione su modello didattico. | Training memory-efficient non significa inferenza ottima né assenza di perdita. |
| 2023–24 | Toolformer, ReAct e function calling | Alternare modello, azione e osservazione tramite strumenti. | Agente a un solo tool con schema, log e approvazione. | Prompt injection, permessi e loop impongono confini esterni al modello. |
| 2024–26 | Context engineering e MCP | Trattare istruzioni, stato, retrieval, tool e contratti come sistema. | Server/tool locale minimale e trace valutabile. | Un protocollo collega componenti; non rende corretto l'agente. |

## Percorso di lettura a due livelli

- **Practitioner**: scheda problema/idea/limite, visuale e un esperimento per
  Shannon, Transformer, scaling, instruction tuning, RAG e reasoning.
- **AI Engineer**: lettura guidata di metodi e figure, implementazioni ★,
  riproduzione in piccola scala e relazione che separa risultato osservato da
  affermazione del paper.

## Fonti primarie

- [Shannon 1948](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)
- [Neural Probabilistic Language Model](https://www.jmlr.org/papers/v3/bengio03a.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [BERT](https://arxiv.org/abs/1810.04805)
- [GPT-3](https://arxiv.org/abs/2005.14165)
- [Scaling Laws](https://arxiv.org/abs/2001.08361)
- [Chinchilla](https://arxiv.org/abs/2203.15556)
- [RMSNorm](https://arxiv.org/abs/1910.07467)
- [GLU Variants](https://arxiv.org/abs/2002.05202)
- [RoFormer](https://arxiv.org/abs/2104.09864)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [GQA](https://arxiv.org/abs/2305.13245)
- [vLLM](https://arxiv.org/abs/2309.06180)
- [Mamba](https://arxiv.org/abs/2312.00752)
- [InstructGPT](https://arxiv.org/abs/2203.02155)
- [Chain-of-Thought](https://arxiv.org/abs/2201.11903)
- [Self-Consistency](https://arxiv.org/abs/2203.11171)
- [DPO](https://arxiv.org/abs/2305.18290)
- [DeepSeek-R1](https://arxiv.org/abs/2501.12948)
- [RAG](https://arxiv.org/abs/2005.11401)
- [LoRA](https://arxiv.org/abs/2106.09685)
- [QLoRA](https://arxiv.org/abs/2305.14314)

