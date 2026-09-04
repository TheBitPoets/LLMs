# Mappa curricolare del corso LLM 2026/27

Stato: specifica della prima edizione completa.

## Durata e modalità

Il percorso **LLM Practitioner** è progettato per un anno scolastico di circa
30 settimane e 60 ore guidate, più un progetto finale. Il percorso **AI
Engineer** riusa lo stesso ordine concettuale e aggiunge studio, matematica,
implementazioni e paper per circa 180–240 ore complessive, adattabili al tempo
disponibile del maintainer.

Le ore sono budget di progettazione, non attestazioni automatiche. La reale
durata verrà aggiornata usando evidenze d'aula e tempi registrati.

## Legenda

- **I**: spiegazione intuitiva obbligatoria per entrambi i livelli;
- **P**: laboratorio Practitioner;
- **M**: matematica rigorosa AI Engineer;
- **E**: implementazione AI Engineer;
- **R**: lettura o riproduzione guidata di ricerca;
- **V**: verifica osservabile.

## I venti moduli

| Modulo | Domanda guida | Practitioner | AI Engineer | Artefatto/verifica |
| --- | --- | --- | --- | --- |
| M00 — Orientamento e baseline | Che cosa vogliamo davvero saper fare? | I, P, V | E, V | Diario iniziale, prova diagnostica e scheda hardware. |
| M01 — Mappa dell'ecosistema | Che differenza c'è tra modello, prodotto, runtime e applicazione? | I, P, V | R, V | Mappa locale/cloud e scheda comparativa di due sistemi. |
| M02 — Predire il simbolo successivo | Che cosa fa il modello a ogni passo? | I, P, V | M, E | Visualizzazione delle probabilità next-token/next-byte. |
| M03 — Token, byte ed embedding | Come diventa numero un testo? | I, P, V | M, E | Confronto tra tokenizer e piccola embedding table. |
| M04 — Apprendere dai dati | Come cambia un modello durante il training? | I, P, V | M, E | Neurone/MLP, loss curve e controllo dell'overfitting. |
| M05 — Attention e Transformer | Come sceglie quali parti del contesto usare? | I, P, V | M, E, R | Visuale Q/K/V, attention manuale e blocco causale. |
| M06 — Architetture moderne | Perché i modelli non sono tutti uguali? | I, P, V | M, E, R | Schede su RoPE, RMSNorm, GQA/MQA, MoE e varianti. |
| M07 — Pre-training, dati e scaling | Da dove arrivano capacità e limiti? | I, P, V | M, E, R | Data card sintetica e piccolo scaling experiment. |
| M08 — Post-training e reasoning | Come diventa utile e controllabile un base model? | I, P, V | M, E, R | Confronto base/instruct/reasoning e mappa SFT–preference–RL. |
| M09 — Pesi, formati e licenze | Che cosa scarichiamo davvero? | I, P, V | E, R | Ispezione config, tokenizer, safetensors/GGUF e licenza. |
| M10 — Hardware e quantizzazione | Quale modello può girare sulla macchina disponibile? | I, P, V | M, E | Stima memoria, benchmark e scelta motivata del modello. |
| M11 — Ollama e inferenza locale | Come avviamo e controlliamo un modello locale? | I, P, V | E | Installazione, pull verificato, chat, API e Modelfile. |
| M12 — Sampling e prompting | Perché lo stesso modello può rispondere diversamente? | I, P, V | M, E | Esperimento su temperature, top-p, seed e structured output. |
| M13 — Applicazioni conversazionali | Che cosa deve aggiungere il software attorno al modello? | I, P, V | E | Chat locale con streaming, stato e contratti d'errore. |
| M14 — Valutazione | Come sappiamo se un modello è adatto allo scopo? | I, P, V | M, E, R | Dataset di eval, baseline, report e decisione motivata. |
| M15 — Embedding, ricerca e RAG | Quando il modello deve consultare fonti esterne? | I, P, V | M, E, R | RAG locale con citazioni, retrieval eval e test di astensione. |
| M16 — Tool use, agenti e MCP | Quando un modello può agire e come lo limitiamo? | I, P, V | E, R | Agente con un solo tool sicuro, log e approvazione umana. |
| M17 — Fine-tuning e adapter | Quando il prompt o il RAG non bastano? | I, P, V | M, E, R | Decisione prompt/RAG/tuning e piccolo LoRA controllato. |
| M18 — Sistemi e kernel d'inferenza | Che cosa succede sotto Ollama? | I, P, V | M, E, R | Profilo prefill/decode, KV cache e kernel minimale verificato. |
| M19 — Costruire e integrare | Possiamo unire teoria, modello e applicazione? | I, P, V | M, E, R, V | Capstone; ramo Pollicino per previsione e ricostruzione esatta. |

## Sequenza nell'anno scolastico

| Periodo | Moduli | Ore Practitioner | Traguardo |
| --- | --- | ---: | --- |
| Settembre–ottobre | M00–M03 | 10 | Distinguere modello, runtime e prodotto; vedere token e probabilità. |
| Novembre–dicembre | M04–M06 | 12 | Capire apprendimento, attention e differenze architetturali. |
| Gennaio | M07–M09 | 8 | Comprendere dati, post-training, pesi, formati e licenze. |
| Febbraio | M10–M12 | 10 | Scegliere, eseguire e controllare un modello locale. |
| Marzo | M13–M15 | 10 | Costruire e valutare chatbot e RAG con fonti. |
| Aprile | M16–M18 | 6 | Comprendere agenti, tuning e inferenza sotto il runtime. |
| Maggio–giugno | M19 | 4 + progetto | Presentare un'applicazione e difendere le scelte tecniche. |

## Fili longitudinali

### Timeline dei paper

Ogni innovazione viene collocata in una catena problema → idea → evidenza →
adozione → limite. Il corso non riduce la storia a una lista di titoli.

### Catalogo dei modelli

Ogni confronto usa una data di osservazione. Provider, nomi, licenze, prezzi,
context limit e benchmark cambiano; le lezioni stabili non dipendono da una
classifica permanente.

### Matematica a doppia esposizione

Il Practitioner incontra quantità e relazioni attraverso oggetti manipolabili,
grafici ed esempi numerici. L'AI Engineer formalizza le stesse relazioni e le
implementa. I simboli compaiono dopo il problema che risolvono.

### Evidenza e sicurezza

Ogni laboratorio distingue output osservato, interpretazione e conclusione.
Applicazioni con strumenti, dati personali o contenuti non fidati adottano
permessi minimi, validazione, sandbox quando necessaria e approvazione umana.

## Dipendenze principali

```text
M00 -> M01 -> M02 -> M03 -> M04 -> M05
                              |       |
                              v       v
                             M07 <-  M06 -> M08 -> M09 -> M10 -> M11
                                                     |       |
                                                     v       v
                                                    M17     M12 -> M13 -> M14
                                                                      |       |
                                                                      v       v
                                                                     M15 -> M16
M05 -> M06 -> M10 -> M18 ----------------------------------------------|
M02 -> M03 -> M04 -> M05 -> percorso Pollicino -----------------------> M19
```

Il diagramma rappresenta prerequisiti concettuali, non impone che ogni
approfondimento AI Engineer sia completato prima dei laboratori Practitioner.
