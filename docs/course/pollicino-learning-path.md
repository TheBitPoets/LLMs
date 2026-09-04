# Percorso Pollicino: dalla previsione alla ricostruzione esatta

Stato: progettazione del corso, allineata alla roadmap corrente di Pollicino al
4 settembre 2026.

Progetto sorgente: [`kinderp/pollicino`](https://github.com/kinderp/pollicino)

## Perché appartiene al corso

Pollicino studia quanti bit sia necessario trasmettere per ricostruire
esattamente un'informazione quando encoder e decoder condividono conoscenza
pregressa utile. Trasforma una proprietà astratta dei modelli linguistici in
qualcosa di misurabile:

> una probabilità maggiore assegnata al simbolo successivo reale può ridurre i
> bit necessari per codificarlo.

Il progetto non sostiene che un hash contenga un file e non usa un chatbot per
indovinare liberamente il testo mancante. Il percorso lossless previsto è:

```text
byte autorevoli
    -> predittore next-byte condiviso
    -> conversione deterministica probabilità/frequenze
    -> arithmetic/range coder
    -> payload .pol
    -> stesso predittore e stesso contratto di codifica
    -> byte bit-perfect
    -> verifica SHA-256
```

Questo crea un ponte controllato tra probabilità, cross-entropy, Transformer,
inferenza, compressione, identità del modello e riproducibilità.

## Confini da mantenere espliciti

- **Learned lossless coding**: il modello prevede probabilità, ma il flusso
  codificato conserva l'informazione necessaria a ricostruire ogni byte.
- **Erasure coding**: ricostruisce un oggetto esatto da un sottoinsieme
  sufficiente di shard ridondanti; non è modellazione generativa.
- **Ricostruzione semantica**: può produrre un risultato utile o percettivamente
  simile; non ricostruisce necessariamente i byte autorevoli.
- **Generative Identification Compression** (`fingerprint breve + ricerca tra
  candidati ordinati dal modello`): è un'ipotesi di ricerca successiva. Deve
  competere con la codifica entropica ordinaria a parità di costo del modello.
- **SHA-256**: verifica un candidato; non contiene abbastanza informazione per
  ricostruire un file arbitrario mancante.

## Progressione dei laboratori

| Lab | Domanda comune | Risultato LLM Practitioner | Estensione AI Engineer | Evidenza |
| --- | --- | --- | --- | --- |
| P0 — Gli hash non sono file | Perché un digest verifica ma non ricostruisce? | Dimostrare l'effetto valanga e spiegare intuitivamente collisioni e pigeonhole principle. | Formalizzare il limite informativo e progettare test negativi. | Byte originali e modificati con entrambi i digest. |
| P1 — Modello uniforme sui byte | Che cosa significa “8 bit per byte”? | Comprendere che inizialmente ciascuno dei 256 byte ha la stessa probabilità. | Derivare `-log2(p)` e collegare surprisal media e cross-entropy. | Dimensione corpus, entropia empirica e baseline uniforme. |
| P2 — La memoria migliora la previsione | I byte precedenti possono ridurre l'incertezza? | Confrontare frequenze e bigrammi su testo, JSON e dati casuali. | Implementare smoothing n-gram/Markov senza leakage tra train e test. | Bit/byte di validazione per dominio e controllo negativo casuale. |
| P3 — Le probabilità diventano bit | Come può una previsione comprimere un file? | Osservare un piccolo round trip con arithmetic/range coding. | Implementare frequenze intere deterministiche e misurare l'overhead finito del coder. | Bit/byte teorici e reali, uguaglianza SHA-256. |
| P4 — Predittore neurale next-byte | Una piccola rete supera le baseline semplici? | Esaminare previsioni ed errori di un MLP fornito. | Addestrare MLP e baseline RNN/GRU, diagnosticando l'overfitting. | Split congelati, seed, checkpoint, curva di loss e delta dalla baseline. |
| P5 — Byte Transformer | È lo stesso meccanismo usato da un LLM? | Seguire i byte attraverso embedding, causal attention e softmax. | Implementare RMSNorm, RoPE, attention, MLP e training AdamW in PyTorch. | Test sulle shape, parametri, bit/byte di validazione e configurazione riproducibile. |
| P6 — Codec neurale `.pol` | Entrambe le parti ricostruiscono esattamente? | Eseguire encode/decode guidato e spiegare perché serve lo stesso modello. | Integrare probabilità e range coder; specificare header, identità del modello e fallback. | Decodifica indipendente, hash esatto, rifiuto di corruzione e modello errato. |
| P7 — Formato e portabilità | Che cosa deve accompagnare i pesi? | Identificare architettura, pesi, precisione, versione e licenza. | Pilotare PyTorch e MLX con una specifica comune e verificarne la parità. | Shape, parametri, tolleranze numeriche e metadati della piattaforma. |
| P8 — Kernel d'inferenza | Dove si consumano tempo e memoria? | Leggere un profilo di latenza per byte/token e memoria. | Costruire e ottimizzare il percorso next-byte minimo; studiare matmul, KV cache, SIMD/GPU e precisione. | Output di riferimento, profiler, throughput, memoria e correttezza. |
| P9 — Rappresentazione ibrida | Quando non conviene usare un modello? | Scegliere tra raw, compressione classica, learned coding e riferimento a chunk noti. | Implementare una policy misurata includendo costo di checkpoint e bootstrap. | Description length completa e regret rispetto alla scelta oracle. |
| P10 — Identificazione generativa | Il calcolo può sostituire bit trasmessi? | Comprendere l'ipotesi senza presentarla come compressione consolidata. | Definire spazi di candidati deterministici, fingerprint progressivi e frontiere compute/bandwidth. | Numero candidati, costo di ricerca, bit di fingerprint/residuo e baseline classica. |
| P11 — Codebook condiviso su PollicinoNet | Quando si ripaga un modello precondiviso? | Simulare la sincronizzazione mattutina e i successivi messaggi su link scarso. | Confrontare codebook statici, stile zstd e appresi contando bootstrap e controllo. | Punto di pareggio, storage, CPU, costo totale sul filo ed etichetta sintetica. |

## Due percorsi completi

### LLM Practitioner

Obbligatori: P0, P1, P2, P3 guidato, P5 guidato, P6 guidato, P7 e P9.

Dimostrazioni facoltative: P4, P8, P10 e P11.

Al termine lo studente deve saper spiegare:

- che un modello predice una distribuzione di probabilità, non la verità;
- perché i dati prevedibili possono essere rappresentati con meno bit;
- perché un codec esatto non può accettare silenziosamente una ricostruzione approssimata;
- perché identità, precisione e runtime del modello contano;
- perché la compressione neurale deve battere baseline classiche semplici includendo modello e bootstrap.

### AI Engineer

Completamento di P0–P11 con implementazioni, ablation ed evidence package. Il
progetto finale è un piccolo codec Byte Transformer riproducibile con:

- policy del corpus e split train/validation/test immutabili;
- baseline statistiche e di compressione classica;
- specifica del modello condivisa tra le implementazioni supportate;
- conversione deterministica da probabilità a frequenze intere;
- decodifica indipendente bit-perfect e verifica SHA-256;
- test negativi per modello errato, stream corrotto e dati casuali;
- report su bit/byte, throughput, memoria e total description length;
- componente d'inferenza ottimizzato ma compatibile con gli output di riferimento;
- decisione scritta sui domini in cui l'approccio vince, perde o resta inconcludente.

## Scala matematica

La matematica viene introdotta quando spiega un risultato osservato:

1. conteggio e pigeonhole principle;
2. probabilità e probabilità condizionata;
3. self-information `I(x) = -log2 p(x)`;
4. entropia e cross-entropy;
5. maximum likelihood come previsione del simbolo successivo;
6. vettori, matrici ed embedding;
7. prodotti scalari, softmax e scaled attention;
8. gradienti, backpropagation e AdamW;
9. rappresentazione numerica e frequenze intere deterministiche;
10. costo ammortizzato del modello e frontiera bandwidth/compute.

Ogni punto deve avere una spiegazione intuitiva, un esempio visuale o
manipolabile e un'estensione rigorosa. Le formule non sostituiscono gli esperimenti.

## Policy per corpus e benchmark

Si parte da fixture piccole, lecite e ridistribuibili che rappresentano:

- testo in linguaggio naturale;
- codice sorgente;
- JSON, XML e CSV;
- dati binari o media raw/non compressi;
- formati già compressi;
- byte crittograficamente casuali come controllo negativo.

Train, validation e test restano separati. I risultati sono riportati per
dominio: un fallimento su dati incomprimibili o fuori dominio non viene nascosto
in una media globale. Dizionario appreso e checkpoint fanno parte del costo
totale, salvo esperimenti che dichiarino e giustifichino la side information
come già condivisa.

## Relazione con Ollama e gli LLM di frontiera

Pollicino è intenzionalmente più piccolo di un LLM conversazionale, ma il suo
Byte Transformer espone lo stesso ciclo centrale: rappresentare il contesto,
applicare blocchi Transformer causali e predire il simbolo successivo. Dopo P5
viene confrontato con un modello selezionato tramite Ollama:

| Dimensione | Byte Transformer Pollicino | LLM servito da Ollama |
| --- | --- | --- |
| Vocabolario | 256 valori byte | Vocabolario del tokenizer specifico del modello |
| Obiettivo | Probabilità next-byte per codifica esatta | Generazione next-token per linguaggio e applicazioni |
| Visibilità del training | Piccolo esperimento interamente ispezionabile | Normalmente pesi preaddestrati consumati come artefatto |
| Requisito runtime | Contratto esatto sulle probabilità per il decode lossless | Sampling e serving utili, spesso tolleranti a variazioni implementative |
| Valutazione | Bit/byte, round trip esatto, description length totale | Qualità sul task, latenza, throughput, memoria, sicurezza e costo |

Il confronto evita due confusioni: eseguire un modello non equivale a capirne
l'implementazione; costruire un piccolo Transformer non equivale ad addestrare
un modello di frontiera competitivo.

## Dipendenze e ordine di implementazione

Il corso segue la roadmap Pollicino senza partire dall'ipotesi più speculativa:

```text
P0–P3 fondamenti classici e statistici
    -> P4 baseline appresa
    -> P5 Byte Transformer
    -> P6 codec neurale esatto
    -> P7 portabilità
    -> P8 lavoro sul kernel
    -> P9 policy ibrida
    -> P10 ricerca sull'identificazione generativa
    -> P11 esperimento di ammortamento PollicinoNet
```

Il corso LLM Practitioner non dipende dal completamento di P6–P11. Fixture
guidate possono insegnarne i concetti mentre il percorso AI Engineer sviluppa e
valida l'implementazione di ricerca reale.

## Dichiarazione sullo stato corrente

Al 4 settembre 2026 la roadmap canonica di Pollicino presenta predittori
classici, Byte Transformer, codec neurale e identificazione generativa come
lavoro pianificato. PollicinoNet dispone di più infrastruttura implementata ed
evidenze di ricerca sintetiche: identità esatta dei contenuti, store,
riconciliazione, trasferimento riprendibile ed esperimenti di routing. I due
stati non vanno fusi nell'affermazione che il modello neurale di ricostruzione
dei file esista già.
