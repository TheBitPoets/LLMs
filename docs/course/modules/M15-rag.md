# M15 - Embedding, ricerca e RAG

**Domanda guida:** quando il modello deve consultare fonti esterne?  
**Durata:** 4 ore Practitioner; 14 ore AI Engineer.  
**Prerequisiti:** M03, M13–M14.

## Obiettivi osservabili

Seguire ingest→chunk→embedding/index→query→retrieval→rerank→context→answer;
separare retrieval quality e generation quality; citare e astenersi. L'AI
Engineer implementa retrieval e valuta recall/MRR.

## Lezione intuitiva

RAG non “insegna” permanentemente documenti ai pesi: recupera frammenti al
momento della domanda e li inserisce nel contesto. Se il frammento giusto non
viene recuperato, il generatore non può citarlo; se viene recuperato, può
comunque ignorarlo o interpretarlo male.

Chunking è una scelta: pezzi troppo piccoli perdono contesto, troppo grandi
diluiscono segnali e consumano token. Una citazione è valida solo se punta al
frammento che sostiene davvero l'affermazione.

## Laboratorio

Corpus locale di documenti del corso con ID, versione e licenza. Baseline
keyword/BM25 semplificata; seconda pipeline embedding. Costruire 15 query con
evidence gold, inclusi casi senza risposta. Misurare recall@k e accuracy delle
citazioni prima della qualità stilistica. Test negativi: documento con prompt
injection, fonte contraddittoria e risposta assente.

## AI Engineer

Normalizzazione e coseno, dense/sparse/hybrid retrieval, reranker, MRR/nDCG,
context packing e deduplica. Tracciare `Claim→Evidence→Source→Fragment`, validità
temporale e conflitti, coerentemente con Raiatea. I documenti sono dati non
fidati: non possono cambiare policy o autorizzazioni.

## Verifica

Retrieval 3, citazioni 2, astensione 2, injection defense 2, provenienza 1.
Fonte primaria: [Lewis et al. RAG](https://arxiv.org/abs/2005.11401).

