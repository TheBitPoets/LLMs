# Corso LLM 2026/27

Questo repository è la fonte del percorso teorico-pratico sugli LLM articolato
su due livelli. Il corso è indipendente da una singola piattaforma didattica:
Raiatea potrà in seguito rappresentarlo e adattarlo, mentre TheBitLab potrà
eseguirne i laboratori.

## I due livelli

| Livello | Destinatari | Risultato atteso |
| --- | --- | --- |
| **LLM Practitioner** | Studenti della scuola secondaria, docenti e utenti tecnicamente curiosi | Spiegare intuitivamente i meccanismi importanti, scegliere ed eseguire un modello locale o cloud adeguato, misurarlo e costruire un'applicazione utile. |
| **AI Engineer** | Il maintainer e sviluppatori avanzati | Derivare e implementare i meccanismi, addestrare piccoli modelli, riprodurre risultati di ricerca selezionati e comprendere l'inferenza fino ai kernel e ai costi hardware. |

Non sono due corsi indipendenti. Ogni argomento deve offrire, quando utili, gli
stessi quattro strati:

1. **intuizione** — spiegazione visuale, analogia ed esempio concreto;
2. **esperimento** — comportamento osservabile in un laboratorio piccolo e riproducibile;
3. **matematica e implementazione** — derivazione, codice e modi di fallire;
4. **paper e sistemi di frontiera** — origine dell'idea e impiego nei modelli attuali.

È possibile completare gli strati 1–2 senza essere obbligati ad attraversare
gli strati 3–4. Il percorso AI Engineer li completa tutti e registra evidenze.

## Tronco comune

1. Che cosa predice un modello linguistico e che cosa non conosce.
2. Token, rappresentazioni byte, embedding e contesto.
3. Probabilità, entropia e previsione del token successivo.
4. Attention, blocchi Transformer, posizione e normalizzazione.
5. Pre-training, dati, ottimizzazione e scaling.
6. Post-training, instruction following, preference optimization e alignment.
7. Famiglie di modelli, licenze, open weight e servizi cloud.
8. File dei modelli, formati numerici, quantizzazione e budget di memoria.
9. Inferenza locale con Ollama e runtime di livello inferiore.
10. Sampling, structured output, strumenti e API applicative.
11. Retrieval, context engineering, memoria e agenti.
12. Valutazione, benchmark, osservabilità, sicurezza e riproducibilità.
13. Fine-tuning, adapter, distillazione e deployment.
14. Sistemi d'inferenza: batching, KV cache, kernel di attention e serving.
15. Costruzione da zero di un piccolo modello linguistico.

Famiglie di modelli e tecniche di frontiera formano un catalogo vivo e datato.
I concetti stabili appartengono alle lezioni; classifiche, context limit,
prezzi e disponibilità appartengono a snapshot versionati.

## Scala dei progetti pratici

Il corso usa progetti complementari invece di un unico esempio sovraccarico:

| Progetto | Ruolo nel corso |
| --- | --- |
| `TheBitPoets/LLMs` | Fondamento concettuale collegato alle fonti e indice del corso. |
| `TheBitPoets/Llma_Chatbot` | Anatomia applicativa: prompt, API, stato della conversazione, retrieval e valutazione. |
| Laboratori Ollama | Scoperta dei modelli, esecuzione locale, compatibilità hardware, quantizzazione e confronto. |
| `kinderp/pollicino` | Dalla previsione ai bit: Byte Transformer, compressione neurale lossless, inferenza deterministica e ricostruzione esatta. |
| PollicinoNet | Distribuzione di modelli/codebook condivisi, manifest, trasferimento intermittente e conteggio completo dei costi. |
| Raiatea | Futura superficie per apprendimento, spiegazione, recupero ed evidenze governati dalle fonti. |
| TheBitLab | Futuro ambiente di esecuzione e valutazione riproducibile. |

## Regola comune sulle evidenze

Ogni affermazione pratica deve indicare:

- modello e revisione esatta;
- runtime e versione;
- rappresentazione del modello e quantizzazione;
- prompt/template e parametri di generazione;
- hardware e limite di memoria rilevante;
- dataset o fixture di test;
- metrica e baseline;
- se il risultato è misurato, simulato o soltanto atteso.

Una demo riuscita non diventa una capacità generale. Un modello locale che
risponde a un prompt non è automaticamente adeguato a un dominio; un
esperimento di rete sintetico non costituisce evidenza fisica LoRa.

## Documenti correnti del corso

- [Percorso didattico Pollicino](docs/course/pollicino-learning-path.md)
- [Mappa curricolare](docs/course/curriculum-map.md)
- [Criteri di completamento](docs/course/definition-of-done.md)
- [Standard visuale e animazioni](docs/course/visual-standard.md)
- [Catalogo delle visualizzazioni e provenienza](docs/course/visual-catalog.md)
- [Visuale interattiva: previsione next-token](visuals/next-token-prediction.html)
- [Visuale interattiva: percorso dei dati locale e cloud](visuals/local-vs-cloud-data-journey.html)
- [Visuale interattiva: richiesta Ollama e memoria](visuals/ollama-request-and-memory.html)
- [Visuale interattiva: testo, byte, token ed embedding](visuals/token-byte-embedding-lab.html)
- [Visuale interattiva: attention Query, Key e Value](visuals/attention-qkv-lab.html)
- [Visuale interattiva: Pollicino, dalle probabilità ai bit](visuals/pollicino-probabilities-to-bits.html)
- [Inventario e selezione Manning](docs/course/sources/manning-inventory-and-selection.md)
- [Valutazione di Build Applications with Local AI Models](docs/course/sources/local-ai-models-review.md)

## Prossimi passi di progettazione

1. Inventariare le fonti possedute e mapparle sul tronco comune.
2. Scrivere i venti moduli seguendo la mappa curricolare.
3. Implementare i laboratori Ollama, valutazione e Pollicino prioritari.
4. Preparare verifiche, rubriche e progetti finali per i due livelli.
5. Mantenere separati una timeline dei paper e un catalogo datato dei modelli di frontiera.
