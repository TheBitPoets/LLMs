# M19 - Costruire e integrare

**Domanda guida:** possiamo unire teoria, modello, applicazione ed evidenze?  
**Durata:** 3 ore di preparazione più progetto; 24+ ore AI Engineer.  
**Prerequisiti:** M00–M18, con estensioni proporzionate al livello.

## Risultato Practitioner

Costruire un'app locale utile, scegliere il modello con una matrice di vincoli,
registrare configurazione e confrontarlo con baseline. Opzioni:

1. assistente locale per appunti con output strutturato;
2. RAG su materiali leciti del corso con citazioni e astensione;
3. agente read-only a un tool con approvazione;
4. laboratorio Pollicino guidato su probabilità e codec esatto.

Consegna: codice, README riproducibile, 20+ fixture, report metriche/errori,
data-flow/privacy, demo registrata e dichiarazione dei limiti. Il progetto deve
funzionare senza provider cloud; l'uso cloud resta confronto facoltativo.

## Capstone AI Engineer: piccolo LLM da zero

Implementare tokenizer byte o BPE, dataloader causale, embedding, RMSNorm,
RoPE, GQA/MHA, SwiGLU, blocchi residual, head e training AdamW. Addestrare una
scala didattica con split congelati; confrontare n-gram e MLP. Aggiungere almeno
una estensione tra LoRA, quantizzazione, RAG o kernel profilato.

L'obiettivo non è competere con modelli di frontiera: è poter spiegare e
verificare ogni passaggio.

## Ramo Pollicino

Seguire [il percorso P0–P11](../pollicino-learning-path.md). Gate minimo della
prima edizione: codec statistico esatto con frequenze deterministiche,
round-trip indipendente e SHA-256. Il Byte Transformer neurale rimane etichettato
roadmap finché il repository `kinderp/pollicino` non fornisce evidenza reale.

Per il capstone avanzato: predictor next-byte, range coder, header `.pol`, model
identity, test modello errato/stream corrotto, bit-per-byte, throughput, memoria
e total description length inclusi modello/bootstrap. PollicinoNet è un
esperimento separato su codebook condivisi e link scarsi, non prova del codec neurale.

## Difesa e rubrica

| Dimensione | Punti |
| --- | ---: |
| Problema, requisiti e baseline | 15 |
| Correttezza e test negativi | 20 |
| Evaluation e failure analysis | 20 |
| Riproducibilità e manifest | 15 |
| Sicurezza, privacy, licenze | 10 |
| Spiegazione intuitiva/visuale | 10 |
| Decisioni e limiti | 10 |

Soglia 60/100; correttezza, sicurezza e provenienza non possono essere zero.
La presentazione deve rispondere a una variazione imprevista di input, non solo
riprodurre una demo preparata.

