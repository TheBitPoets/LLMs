# M06 - Architetture moderne

**Domanda guida:** perché i modelli non sono tutti uguali?  
**Durata:** 4 ore Practitioner; 12 ore AI Engineer.  
**Prerequisiti:** M05.

## Obiettivi osservabili

Leggere una config e riconoscere decoder-only, RoPE, RMSNorm, SwiGLU, MHA/GQA/MQA
e MoE; spiegare parametri totali vs attivi. L'AI Engineer implementa ablation
piccole e calcola memoria KV.

## Lezione intuitiva

RoPE ruota coppie di coordinate per rendere confrontabili distanze relative;
RMSNorm regola la scala senza sottrarre la media; SwiGLU usa un cancello nella
MLP. MHA mantiene Key/Value distinti per ogni head; MQA li condivide; GQA crea
gruppi intermedi. MoE instrada ogni token verso pochi esperti: riduce calcolo
attivo rispetto ai parametri totali, ma tutti i pesi devono comunque essere
disponibili e il routing introduce nuovi costi.

## Laboratorio

Confrontare config di due modelli realmente scaricabili. Produrre una scheda
con `hidden_size`, layer, attention heads, KV heads, vocab, context e
quantizzazione. Baseline: Transformer didattico M05. Test negativo: una config
incompleta non autorizza a indovinare l'architettura.

## AI Engineer

Implementare RMSNorm e RoPE con test numerici; stimare la KV cache come funzione
di layer, KV heads, head dimension, token, batch e byte per elemento. Eseguire
ablation MHA/GQA simulata mantenendo esplicito che una conversione non addestrata
non misura la qualità di un vero modello GQA.

## Verifica

Scheda architetturale 4 punti; spiegazione parametri attivi/totali 2; memoria KV
2; limite 2. Fonti: RMSNorm, RoFormer e GQA nella timeline; model card dei pesi.

