# M17 — Fine-tuning e adapter

**Domanda guida:** quando conviene cambiare i pesi invece di migliorare dati, prompt o strumenti?
**Durata:** 3 ore Practitioner; 14 ore AI Engineer.
**Prerequisiti:** M04, M08, M14–M15.

## Obiettivi osservabili

Saprai distinguere prompting, RAG, SFT, adapter, distillazione e continued pre-training; scegliere la tecnica in base al problema. Il livello AI Engineer calcola parametri LoRA, prepara dataset e training, fonde adapter e verifica regressioni.

## Problema iniziale

Il chatbot non conosce l'ultima circolare. Fare fine-tuning è una cattiva prima risposta: i fatti cambiano e servono citazioni, quindi RAG è più adatto. Se invece sbaglia sempre formato o stile specialistico, adattare i pesi può avere senso.

## Teoria Practitioner

Il prompting cambia il contesto, non i pesi. RAG porta conoscenza aggiornata al prompt. SFT aggiorna il comportamento mediante esempi input-output. **LoRA** congela i pesi base e apprende piccole matrici a basso rango; QLoRA mantiene il base quantizzato durante training per ridurre memoria. Continued pre-training espone il modello a un dominio con obiettivo linguistico; distillazione insegna a un modello più piccolo usando un teacher.

La scala delle soluzioni segue il costo del problema: prima regole e baseline, poi prompt/schema, retrieval o tool; solo dopo training se l'errore è stabile e ci sono dati e valutazione adeguati.

## Esempio minimo

Un modello produce `Sì, certamente: 42` quando serve `42`. Prompt e constrained output possono risolvere. Un modello deve imitare stabilmente un formato raro su molti task: SFT può essere utile. Un modello deve conoscere prezzi aggiornati: retrieval o API, non memorizzazione nei pesi.

## Esempio realistico

Per classificare richieste scolastiche, prepara train/validation/test separati per tempo e mittente. Confronta baseline, prompt few-shot e LoRA sullo stesso test. Registra licenza dei dati, modello base, commit, seed, learning rate, rank, checkpoint e curve. Verifica che l'adapter non peggiori capacità generali critiche.

## Livello AI Engineer: LoRA e training

Per un peso $W\in\mathbb{R}^{d_{out}\times d_{in}}$, LoRA usa

$$W'=W+\frac{\alpha}{r}BA,$$

con $A\in\mathbb{R}^{r\times d_{in}}$, $B\in\mathbb{R}^{d_{out}\times r}$ e rango $r$ piccolo. I parametri allenabili sono $r(d_{in}+d_{out})$ invece di $d_{in}d_{out}$ per quella matrice. Target modules, rank, dropout e scaling influenzano capacità e costo.

In QLoRA il base quantizzato riduce memoria, mentre adapter e stati optimizer usano precisioni adatte. La fusione dell'adapter crea un nuovo checkpoint e deve conservare provenienza e licenze. Un adapter è compatibile soltanto con l'esatto modello base previsto.

## Albero decisionale

| Problema | Prima scelta |
| --- | --- |
| dato aggiornato e citabile | RAG/tool |
| formato rigido | schema/constrained decoding |
| istruzione ricorrente | prompt, poi SFT |
| stile/comportamento stabile | SFT/LoRA |
| dominio linguistico ampio | continued pre-training + SFT |
| costo troppo alto | modello piccolo, quantizzazione, distillazione |

## Errori frequenti

- Allenare prima di costruire un eval set.
- Usare dati sintetici non controllati come verità.
- Mescolare train e test o duplicati.
- Dimenticare licenza e dati personali.
- Valutare solo il task adattato ignorando regressioni.
- Caricare adapter sul checkpoint base sbagliato.

## Esercizi A–F

- **A:** associa problema e tecnica.
- **B:** migliora una decisione “facciamo fine-tuning”.
- **C:** prepara dataset e data card per SFT.
- **D:** diagnostica leakage o adapter incompatibile.
- **E:** addestra un LoRA su modello piccolo e confronta baseline.
- **F:** pipeline completa dati→training→eval→merge→rollback.

## Laboratorio

Esegui `python3 labs/course_lab.py adaptation` per l'albero decisionale. L'estensione reale usa un modello piccolo e dataset non sensibile. Prima dell'addestramento congela eval set e criteri; dopo misura task target, regressioni, memoria e latenza.

## Verifica rapida

Scegli tra RAG e LoRA in tre scenari; calcola i parametri LoRA; spiega compatibilità col base; elenca due regressioni da controllare.

## Sintesi inclusiva

Modificare i pesi è potente ma costoso e meno aggiornabile. Usa retrieval per fatti, strumenti per azioni, schema per formato e fine-tuning per comportamenti stabili. Ogni adattamento vale solo se supera una baseline su un test separato.

## Fonti e collegamenti

- [LoRA](https://arxiv.org/abs/2106.09685)
- [QLoRA](https://arxiv.org/abs/2305.14314)
- Activity: `llm-activity-m17-adaptation`
