# M17 - Fine-tuning e adapter

**Domanda guida:** quando prompt o RAG non bastano?  
**Durata:** 3 ore Practitioner; 14 ore AI Engineer.  
**Prerequisiti:** M04, M08, M14–M15.

## Obiettivi osservabili

Scegliere tra prompt, RAG e tuning; spiegare SFT, LoRA/QLoRA, dataset e
catastrophic forgetting; confrontare sempre con baseline. L'AI Engineer esegue
un adapter piccolo riproducibile.

## Lezione intuitiva

Prompt modifica istruzioni correnti; RAG fornisce conoscenza recuperabile;
fine-tuning modifica comportamento nei pesi. Se il problema è una fonte che
cambia ogni settimana, RAG è spesso più adatto. Se serve uno stile/schema
ricorrente con molti esempi puliti, SFT/adapter può aiutare.

LoRA non riscrive ogni matrice: aggiunge un aggiornamento low-rank `ΔW=BA` e
addestra `A,B`. QLoRA mantiene la base quantizzata durante il training degli
adapter. Piccola memoria non compensa dati poveri o eval assente.

## Laboratorio

Decision memo prima del codice. Dataset train/dev/test con provenienza e
deduplica. Addestrare adapter su un modello didattico o piccolo solo se hardware
consente; in alternativa riprodurre la matematica su MLP. Baseline zero-shot,
few-shot e RAG. Test negativi: esempio canary, fuori dominio e regressione su
capacità generale.

## AI Engineer

Implementare layer LoRA lineare, merge/unmerge e conteggio parametri. Tracciare
learning rate, rank, alpha, dropout, seed, checkpoint e licenza. Misurare delta
paired, memoria, tempo e forgetting. Non distribuire pesi/base senza diritto.

## Verifica

Decisione 2, dataset 2, implementazione 2, baseline/eval 2, licenza/limiti 2.
Fonti: [LoRA](https://arxiv.org/abs/2106.09685) e
[QLoRA](https://arxiv.org/abs/2305.14314).

