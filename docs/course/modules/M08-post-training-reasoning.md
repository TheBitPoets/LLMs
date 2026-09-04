# M08 — Post-training e reasoning

**Domanda guida:** come diventa assistente un modello che ha imparato soprattutto a continuare testi?
**Durata:** 3 ore Practitioner; 12 ore AI Engineer.
**Prerequisiti:** M04–M07.

## Obiettivi osservabili

Saprai distinguere pre-training, supervised fine-tuning, preference optimization, RL e distillazione; riconoscere quando più token di ragionamento aiutano o sprecano risorse. Il livello AI Engineer formula gli obiettivi principali e progetta confronti controllati tra policy.

## Problema iniziale

Un modello base può completare “Domanda: … Risposta: …”, ma non necessariamente seguire bene istruzioni o rifiutare richieste rischiose. Per renderlo un assistente si aggiungono esempi, preferenze e feedback. Questo migliora il comportamento osservabile, senza trasformare il modello in un oracolo.

## Teoria Practitioner

Nel **supervised fine-tuning (SFT)** il modello imita risposte curate. Nei metodi di **preference optimization** impara a favorire una risposta scelta rispetto a una rifiutata. Nell'**RLHF** un segnale derivato da preferenze guida una policy con reinforcement learning. Varianti possono usare feedback umano, AI o verificatori automatici.

“Reasoning model” descrive sistemi addestrati o configurati per spendere calcolo aggiuntivo prima della risposta, usare tracce interne, strumenti o verifiche. Una risposta più lunga non prova un ragionamento migliore. Il test deve misurare risultato, robustezza, costo e capacità di correggersi.

## Esempio minimo

Prompt: “Rispondi con un numero”. Il modello base continua con spiegazioni; dopo SFT rispetta più spesso il formato. Una coppia di preferenza può insegnare a privilegiare la risposta corretta e concisa. Tuttavia, se le preferenze premiano stile sicuro invece di correttezza, il modello può imparare sicurezza apparente.

## Esempio realistico

Per problemi matematici confronta risposta diretta, scomposizione guidata e uso di un calcolatore. Mantieni stesso modello e dataset; registra accuratezza, token, latenza e fallimenti. Se il calcolatore migliora l'esattezza, il merito appartiene al sistema modello+strumento, non ai soli pesi.

## Livello AI Engineer: obiettivi

Nell'SFT si minimizza la negative log-likelihood dei token di risposta, spesso mascherando la parte prompt. Un preference model può stimare $r(x,y)$ da coppie $(y_w,y_l)$. La DPO ottimizza direttamente una probabilità relativa rispetto a una policy di riferimento; il dettaglio della parametrizzazione conta, ma l'intuizione è aumentare il margine per la risposta preferita senza allontanarsi senza controllo.

RL con reward verificabile è particolarmente utile quando il risultato può essere controllato, per esempio test di codice o esito matematico. Anche qui reward hacking e distribuzioni strette sono rischi: una policy può massimizzare il verificatore sfruttandone lacune.

Distillazione trasferisce comportamento da un teacher a uno student mediante output, logits o dati sintetici. Riduce costo di esecuzione ma può trasferire errori e non conferisce automaticamente le stesse capacità fuori distribuzione.

## Errori frequenti

- Confondere instruction tuning con acquisizione di nuovi fatti garantiti.
- Valutare reasoning dalla lunghezza della spiegazione.
- Usare come giudice lo stesso modello senza controlli indipendenti.
- Ignorare il modello di riferimento o la forza della regolarizzazione.
- Premiare una metrica facilmente manipolabile.

## Esercizi A–F

- **A:** classifica esempi come pre-training, SFT o preferenza.
- **B:** riscrivi una coppia di preferenza ambigua.
- **C:** costruisci un piccolo dataset SFT con criteri espliciti.
- **D:** diagnostica reward hacking in un verificatore.
- **E:** confronta tre strategie di reasoning con budget uguale.
- **F:** implementa un esperimento SFT/DPO ridotto e valuta regressioni.

## Laboratorio

Esegui `python3 labs/course_lab.py reasoning` su problemi verificabili. Pre-registra modalità e budget, poi confronta risposta diretta, scomposizione e tool. Non conservare soltanto l'accuratezza media: raccogli categorie di errore.

## Verifica rapida

Distingui SFT, preferenze e RL; spiega perché il post-training non garantisce verità; proponi una metrica contro verbosity; descrivi un rischio della distillazione.

## Sintesi inclusiva

Il pre-training costruisce capacità generali di previsione; il post-training orienta comportamento, formato e preferenze. Reasoning e strumenti possono migliorare compiti difficili, ma consumano risorse e devono essere verificati sul risultato, non sull'apparenza.

## Fonti e collegamenti

- [InstructGPT](https://arxiv.org/abs/2203.02155)
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
- [Timeline dei paper](../research/paper-timeline.md)
- Activity: `llm-activity-m08-post-training`

