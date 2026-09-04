# M08 - Post-training e reasoning

**Domanda guida:** come diventa utile e controllabile un base model?  
**Durata:** 3 ore Practitioner; 12 ore AI Engineer.  
**Prerequisiti:** M04 e M07.

## Obiettivi osservabili

Distinguere base, instruct e reasoning model; descrivere SFT, preference
optimization, RLHF/RLVR e distillazione; valutare esito e costo del reasoning.
L'AI Engineer implementa loss SFT e DPO su dati piccoli.

## Lezione intuitiva

Il pre-training insegna a continuare testi; SFT mostra esempi di istruzioni e
risposte; le preferenze confrontano risposte; RL ottimizza un reward. Un modello
di reasoning può spendere più token e calcolo prima della risposta. Un testo
lungo e convincente non prova che la catena narrata sia fedele al calcolo interno.

Confrontare lo stesso task su base/instruct/reasoning controllando template e
budget. Separare accuratezza finale, token prodotti, latenza e casi irrisolti.

## Matematica AI Engineer

SFT minimizza NLL sui token target, mascherando quelli che non vanno appresi.
DPO aumenta la preferenza relativa di `y_w` su `y_l` rispetto a un reference
model mediante una logistic loss. RLVR usa reward verificabili, ma ciò che non
entra nel reward può essere trascurato o sfruttato.

## Laboratorio

Dataset sintetico di coppie preferite/non preferite con policy di annotazione.
Baseline zero-shot. Confrontare self-consistency con singolo campione a parità
di budget registrando accuracy/costo. Test negativo: problema con premessa falsa
e risposta non verificabile.

## Verifica

Pipeline 3, distinzione obiettivi 2, esperimento 2, reward hacking/limiti 2,
provenienza 1. Fonti: InstructGPT, DPO, CoT, Self-Consistency e DeepSeek-R1.

