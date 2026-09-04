# Soluzioni delle verifiche rapide

Documento riservato al docente. Le risposte sono criteri minimi, non copioni obbligatori. Accettare formulazioni equivalenti se corrette e motivate.

## M00

1. Il modello produce distribuzioni/output; l'applicazione gestisce interazione, stato, dati e controlli.
2. La baseline rende interpretabile il miglioramento e può mostrare che il modello non serve.
3. È una stima o simulazione; diventa misura solo osservando l'esecuzione reale.
4. Almeno checkpoint sorgente, prompt/template, runtime, hardware, contesto e protocollo.

## M01

Il percorso locale attraversa UI, API locale, runtime, tokenizer/pesi e ritorno; modello e runtime sono componenti diversi. Rischi locali: accesso eccessivo a file/log; cloud: invio/retention. Open weight riguarda disponibilità/licenza dei pesi, “locale” il luogo di esecuzione.

## M02

Il logit è un punteggio; la probabilità è il valore normalizzato. Ogni token scelto entra nel contesto e cambia il passo seguente. Probabilità linguistica non verifica fatti. Il decoding lossless richiede distribuzioni/frequenze identiche fra encoder e decoder.

## M03

Catena: contenuto → byte → tokenizer → ID → lookup embedding → layer. L'ID è un indice, l'embedding un vettore appreso. Spazi, emoji e subword rompono l'equivalenza token-parola. Pollicino usa byte per preservare qualunque file.

## M04

L'optimizer modifica i pesi usando i gradienti. La validation guida scelte, il test stima il risultato finale. Training giù e validation su suggerisce overfitting/shift/leak da indagare. Gradient descent sottrae learning-rate × gradiente.

## M05

Query cerca, Key viene confrontata, Value porta l'informazione. I pesi sono softmax di $QK^T/\sqrt{d_k}$ più maschera. La maschera blocca il futuro; residual conserva una via diretta; MLP trasforma ogni posizione. Attention non è una spiegazione causale completa.

## M06

RoPE: posizione; GQA/MQA: KV cache; MoE: capacità con pochi esperti attivi; RMSNorm/SwiGLU: stabilità/blocco. Il rapporto KV MHA:GQA segue il rapporto fra head KV. Long context nominale non garantisce recupero affidabile.

## M07

Più volume può aggiungere duplicati o dati scadenti. Le scaling law sono relazioni empiriche in un regime, non garanzie universali. Contaminazione: duplicati o derivati del test nel training. Data card: origine, licenza, trasformazioni, split, filtri e limiti.

## M08

SFT imita esempi; preference optimization favorisce risposte; RL ottimizza reward. Il post-training orienta comportamento ma non crea un verificatore di verità. Controllare accuratezza/costo, non lunghezza. Distillazione può trasferire errori e fallire fuori distribuzione.

## M09

L'architettura definisce operazioni; il checkpoint valori concreti. Il formato organizza i tensori; la quantizzazione ne riduce precisione/spazio. Servono repository, revisione/digest, file/hash, tokenizer, template, licenza, runtime e conversione.

## M10

$M_w\approx Nb/8$ è solo peso grezzo; vanno aggiunti scale, cache, buffer e sistema. Bandwidth muove dati, compute esegue operazioni. Una quantizzazione si sceglie con memoria, kernel e qualità misurata sul task.

## M11

La CLI è interazione diretta; l'API è il contratto per applicazioni. Identificare digest/tag e versione runtime. Timeout e modello assente devono produrre errore limitato e diagnosticabile. Ripetibilità richiede anche template, parametri, fixture e hardware.

## M12

Top-p conserva massa cumulativa; temperature rimodella logits, top-k tronca per rango. Input non fidato va delimitato e privato di privilegi. La grammatica garantisce sintassi raggiungibile, non correttezza dei valori.

## M13

La memoria vive nello stato dell'applicazione o servizio; il modello vede solo il contesto inviato. Un adapter consente provider sostituibile. Il timeout produce stato fallito/annullato coerente. Metriche sicure: TTFT, durata, token, codice errore.

## M14

Requisito “JSON sempre leggibile” → schema valido 100% dopo retry limitato. Format-validity non prova correttezza. Un confronto appaiato riduce variabilità fra esempi. Bias judge: ordine, verbosità, stile, self-preference.

## M15

Ingestione, chunk, embedding/indice, retrieval, reranking, prompt, generazione e verifica. Recall misura recupero; correctness la risposta. Una citazione è valida se esiste e supporta il claim. Documenti restano dati senza privilegi.

## M16

Il modello propone; applicazione e policy autorizzano. MCP standardizza esposizione di tool/risorse, non sicurezza. Stati minimi: plan, validate, approve, execute, observe, done/fail. Allowlist e sandbox sono controlli esterni al prompt.

## M17

Fatti aggiornati/citabili → RAG; comportamento stabile → SFT/LoRA. Parametri LoRA per una matrice: $r(d_{in}+d_{out})$. L'adapter richiede il base esatto. Controllare task generale, sicurezza, formato e latenza oltre al target.

## M18

Prefill elabora il prompt; decode produce token sequenziali. KV cache evita ricalcolo del prefisso. Memory-bound significa limitato dai byte mossi rispetto alle operazioni. Benchmark: warm-up, sync, shape/dtype uguali, ripetizioni e statistiche.

## M19

La consegna deve essere riproducibile e confrontata con baseline. Nel ramo Pollicino encoder e decoder condividono modello e frequenze canoniche; il test autoritativo è uguaglianza byte-per-byte. Il toy codec non prova ancora un codec neurale produttivo.
