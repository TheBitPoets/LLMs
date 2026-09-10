# Soluzioni ragionate dei venti moduli LLM

Apparato docente. Gli esempi E00-E07 sono pubblici e svolti; queste indicazioni
servono a correggere le nuove consegne, distinguendo evidenza e semplice
esecuzione dell'esempio. I risultati numerici citati provengono dai report CPU
versionati. Le risposte dei modelli Ollama restano da raccogliere nel rehearsal.
Per ogni modulo la rubrica assegna 4 punti a evidenze, 3 a spiegazione, 2 a
correttezza tecnica e 1 a limiti. Una risposta copiata senza prova non soddisfa
il criterio di riproducibilità.

## M00 - Baseline e domanda verificabile

Una buona consegna è «estrarre aula e ora da dieci avvisi sintetici, almeno
otto corretti, zero aule inventate». La baseline può essere una ricerca per
espressione regolare; confrontarla con LLM solo sugli stessi dieci avvisi.
Un report corretto separa dati di preparazione e valutazione, registra la
versione e conserva gli errori. «Il modello capisce la scuola» non è una
conclusione misurabile. Chiedere allo studente quale esempio metterebbe in
crisi la baseline: un'aula scritta in lettere è un caso pertinente.
Il comando `python3 labs/course_lab.py system` registra l'ambiente, ma non
dimostra alcuna prestazione del modello. Accettare esplicitamente «non misurato»
nei campi che richiedono Ollama; non accettare valori inventati per completarli.

## M01 - Ecosistema e confini dei dati

La soluzione deve separare almeno pesi/tokenizer, runtime, applicazione e
dati. In locale la domanda attraversa l'app e il servizio sul dispositivo;
in cloud attraversa anche rete e infrastruttura del provider. «Locale» non
garantisce assenza di traffico: un'app può fare telemetria o usare strumenti
remoti. Un modello open-weight può essere eseguito da un servizio cloud e
un'interfaccia open source può chiamare pesi chiusi. Sono assi indipendenti.
Per correggere, seguire una domanda dall'input all'output e chiedere dove vive
la cronologia. Il catalogo datato deve servire a leggere condizioni correnti,
non a memorizzare una classifica. Premiare una scelta motivata da compito,
memoria e licenza anche quando non sceglie il modello più grande.

## M02 - Probabilità e bit

Con logits $(\ln2,0)$ la distribuzione è $(2/3,1/3)$. Se il target è il secondo
simbolo, la loss è $\ln3$ nat e $\log_2 3$ bit. Aggiungere una costante a tutti
i logits non cambia la softmax: numeratore e denominatore sono moltiplicati
per lo stesso fattore. Moltiplicarli invece cambia la concentrazione.
Il comando `python3 labs/course_lab.py softmax --logits 0 1 2` permette di
controllare normalizzazione e sorpresa. La correzione deve distinguere alta
probabilità da verità: il modello può assegnare alta probabilità a un errore
frequente. Nel ramo Pollicino le probabilità controllano il costo di codifica,
mentre il decoder deve ricostruire anche simboli a bassa probabilità.

## M03 - Byte, token e embedding

La lettera «è» occupa due byte in UTF-8, ma un tokenizer può rappresentarla
con uno o più token. Gli ID sono indici discreti; la lookup restituisce righe
della matrice embedding. La distanza fra ID numerici non misura somiglianza
semantica. Per il round trip richiedere uguaglianza dei byte, includendo
accenti, newline e spazi finali. Unicode apparentemente identico può avere
rappresentazioni diverse: normalizzare prima della prova cambia il problema.
E02 usa vettori prodotti da un modello embedding, mentre E04 usa embedding
allenabili dei byte dentro il Transformer: funzioni e addestramenti differenti.
Correggere chi assume che una similarità coseno di 0,8 significhi «80% vero».

## M04 - Training e generalizzazione

Riferimento eseguibile: `python3 -m labs.engineering.train`. Controllare
`training-report.json`, split e hash. Il base ha test loss circa 0,295 nat/byte
contro circa 2,92 dell'unigramma; la conclusione valida riguarda il corpus
sintetico a template. Le righe test sono distinte, ma i template sono comuni:
non è una prova di generalizzazione a documenti scolastici reali.
La selezione avviene sul minimo di validation ai checkpoint osservati; il test
non sceglie il learning rate. Se lo studente introduce uno split per argomento,
aspettarsi risultati diversi e valutarne l'interpretazione. Non richiedere
la medesima durata CPU o un identico ultimo decimale su altre piattaforme.
La regressione scalare del runner base resta utile per spiegare il gradiente.

## M05 - Attention causale

Con una query che assegna punteggi 0 e $\ln2$ a due chiavi ammesse, i pesi
sono 1/3 e 2/3. L'output è la stessa combinazione dei value, non delle key.
In TinyLM una testa ha dimensione 12; la matrice dei punteggi ha dimensioni
tempo×tempo per testa. Il test decisivo modifica i token futuri e confronta
i logits del prefisso: devono restare uguali entro la tolleranza numerica.
Una softmax con righe a somma uno può comunque guardare il futuro se manca
la maschera: la sola normalizzazione non è prova sufficiente.
E04 fornisce il modello e `test_engineering_neural.py` il controllo di
causalità. Chiedere allo studente di spiegare l'offset della maschera con cache.

## M06 - Architetture moderne

Per la KV cache, a parità di livelli, contesto e dimensione testa, passare
da otto teste KV a due riduce quel costo a un quarto; non riduce automaticamente
allo stesso modo pesi totali o FLOP dell'intero modello. Nel MoE distinguere
parametri attivi da parametri da conservare: gli esperti non selezionati
restano parte dell'artefatto. RoPE cambia il modo di incorporare la posizione,
non rende affidabile qualunque lunghezza di contesto. Una risposta corretta
collega ogni tecnica al collo di bottiglia che affronta e a un limite.
Usare il catalogo del 10 settembre per confrontare una card recente con
TinyLM: quest'ultimo usa MHA e posizioni apprese, senza attribuirgli QSA,
Gated DeltaNet o altri componenti assenti dal codice.

## M07 - Dati e contaminazione

Nel corpus E04 il controllo fra insiemi di righe trova duplicati esatti.
Questo non trova parafrasi né template condivisi. Una soluzione migliore per
valutare trasferimento a un dominio nuovo separa per fonte, argomento o tempo
prima del campionamento delle finestre. Suddividere finestre sovrapposte dopo
averle estratte può copiare gran parte dello stesso testo fra train e test.
La data card deve dichiarare origine sintetica, generatore, licenza e limiti,
non soltanto il numero di righe. Non è possibile inferire una scaling law
affidabile da due modelli minuscoli addestrati con budget non confrontabili.
Chiedere quale dato cambierebbe la decisione di raccolta e quale contaminazione
resterebbe invisibile a un hash esatto.

## M08 - Post-training e reasoning

Correggere distinguendo obiettivo e meccanismo: SFT apprende da esempi,
preferenze confrontano risposte, reward/verificatori valutano un esito,
reasoning a inferenza spende un budget durante l'uso. Una risposta più lunga
non prova una migliore soluzione. Per un esercizio aritmetico fissare problemi,
risposte verificabili e budget; confrontare risposta diretta e uso di un tool
con lo stesso criterio di esattezza. Registrare anche fallimenti e costo.
Il testo di reasoning esposto da un modello non va considerato una misura
completa o fedele di tutti i calcoli interni. E03 permette di osservare una
traccia di azioni verificabili; non rappresenta da solo un esperimento RL
né una riproduzione del post-training di un modello commerciale.

## M09 - Artefatto, formato e licenza

Una scheda completa nomina repository e revisione, tokenizer/template,
quantizzazione, runtime, licenza e digest scaricato. «GGUF» indica un formato,
non un unico livello di precisione o una licenza. Safetensors contiene tensori
con metadati; una quantizzazione specifica richiede supporto del runtime.
Un file FP8 e uno Q4 non sono intercambiabili solo perché hanno lo stesso nome
di famiglia. Correggere con un caso negativo: modello disponibile come pesi,
ma runtime della classe privo dell'architettura necessaria. La scelta deve
essere rifiutata o accompagnata da un piano verificato di conversione.
Il catalogo collega fonti ufficiali; non sostituisce la verifica della licenza
del singolo artefatto al momento del download.

## M10 - Budget di memoria

Per 8 miliardi di parametri a 4 bit il solo limite ideale dei pesi è 4 GB
decimali. Scale, metadati, cache, attivazioni e runtime aumentano il totale;
GB e GiB non sono uguali. In E06 la cache float32 del modello minuscolo con
48 posizioni occupa esattamente 36.864 byte, ottenuti dalla formula e dai
tensori. Questo valore non è il picco RSS del processo. Premiare tabelle che
separano stima, misura e unità. Il throughput va misurato a contesto e output
comparabili; includere o escludere il caricamento deve essere dichiarato.
Non trasportare le latenze della CPU del workspace al Mac M4 Pro né assumere
che memoria unificata significhi tutta la RAM disponibile al modello.

## M11 - Runtime locale

La prova completa richiede servizio Ollama attivo, modello presente e una
richiesta valida. E01 salva versione e inventario; lo studente deve controllare
che la voce del modello contenga il digest effettivo. Un tag non trovato o
un servizio spento devono produrre diagnosi e codice d'errore, non una risposta
inventata. I test HTTP simulati verificano il client ma non certificano
compatibilità del modello o velocità del runtime. Per il recupero avviare il
servizio o installare il tag scelto, poi ripetere lo stesso comando.
Una richiesta a loopback non prova che qualunque modello del catalogo sia
locale: verificare origine e artefatto, evitando tag cloud per la prova offline.

## M12 - Sampling e output strutturato

Nel confronto cambiare una variabile alla volta. Temperatura influenza la
concentrazione, top-k limita il numero di candidati, top-p limita la massa
cumulata; l'ordine delle operazioni conta. Un decoder greedy può essere
ripetibile nel medesimo ambiente ma non rende vero il contenuto. Per JSON
distinguere sintassi, schema e correttezza semantica: `{ "posti": 99 }` può
essere JSON perfetto e dato sbagliato. E02 valida citazioni e schema, E03
valida tool e argomenti prima dell'esecuzione. Il criterio minimo include
un output malformato e uno formalmente valido ma non supportato dai dati.
Non assegnare pieno punteggio a una singola risposta riuscita senza confronto.

## M13 - Stato della chat

Riferimento: `ChatSession` in `client.py`. Dopo un errore a metà streaming
la storia deve essere esattamente quella precedente all'invio; il frammento
può essere stato visualizzato ma non deve essere confermato come turno.
La policy elimina coppie complete, non metà conversazione, e preserva il
sistema. Un limite di caratteri non è un limite token esatto. Il test con
server HTTP locale controlla sia chiusura sia stato di cancellazione.
Per la consegna «ultime due coppie» la soluzione corretta applica il limite
al contesto da inviare e aggiorna la storia solo a completamento. Cancellare
durante una lettura bloccante può attendere il timeout: non promettere arresto
istantaneo senza cambiare il trasporto.

## M14 - Evaluation e soglie

Congelare domande, etichette e criteri prima del confronto finale. In E02
recall@3 con un solo documento rilevante vale zero o uno; per casi senza fonte
si valuta l'astensione. Una metrica a sottostringa può accettare una negazione
errata: aggiungere un caso «non ha 24 posti» mostra il limite. La soluzione
docente deve classificare retrieval, generazione, citazione e astensione,
evitando un unico numero che nasconde errori gravi. Cinque casi sono una
smoke evaluation, non una stima affidabile della popolazione.
Un judge LLM richiede calibrazione su etichette umane e controllo dell'ordine
dei candidati; non è una fonte primaria indipendente dei fatti valutati.

## M15 - RAG e citazioni

La risposta «LAB-A ha 24 posti» deve citare il chunk della stanza A, con
estratto realmente presente. L'ID inventato viene rifiutato dal validatore.
Un estratto corretto associato a un'affermazione sulla stanza B non supera
la correzione semantica, anche se supera il controllo di sottostringa.
Senza chunk sopra soglia il codice si astiene senza generazione; una soglia
troppo severa può aumentare astensioni improprie. Il documento ostile resta
testo e il generatore non ha tool, quindi non può compiere effetti tramite
la pipeline. Non concludere per questo che il testo generato sia immune da
injection. L'eval live va conservato anche se il modello piccolo fallisce.

## M16 - Agente e protocollo

La soluzione deve mostrare una traccia con `lookup_room`, argomento `LAB-A`
e risultato 24 prima della risposta finale. Il numero 24 da solo potrebbe
essere stato inventato. La policy rifiuta tool sconosciuti e chiavi extra;
il limite passi arresta un agente che continua a chiedere lo stesso strumento.
Il test MCP avvia un processo reale, esegue handshake e discovery e verifica
che una chiamata prima dell'inizializzazione fallisca. Aggiungere una stanza
richiede aggiornare dati e validazione, non soltanto descrivere il nuovo valore
nel prompt. `readOnlyHint` non impone permessi. Per operazioni con effetti
rimandare a S04: approvazione e transazione appartengono all'applicazione.

## M17 - Adapter e regressione

Il riferimento E05 apprende 1.216 parametri sulla head. Con B iniziale zero,
l'output iniziale coincide con il base; congelare i parametri si controlla
anche confrontando i tensori prima/dopo. Nel report target loss 6,449→1,471,
base loss 0,295→4,759: l'adattamento fallisce un requisito di mantenimento
delle prestazioni originali. Una soluzione corretta non nasconde questa
regressione e propone un esperimento, non una cura certa.
Per confrontare ranghi, usare validation per scegliere e un test finale
separato; non richiedere che il rango maggiore vinca. Il loader controlla
l'hash del base prima di caricare l'adapter. LoRA sulla sola head non equivale
a QLoRA o a un fine-tuning completo di tutte le proiezioni.

## M18 - Kernel e benchmark

Prima del timing servono equivalenza numerica e causalità. E06 confronta
reference, softmax online tiled e funzione di libreria; il tiled Python
risulta più lento nella shape misurata. È un esito corretto: spiega il costo
dei cicli e delle chiamate rispetto alla fusione hardware. La cache mantiene
K/V e usa posizioni con offset; un test su singolo token senza passato non
basta a controllarla. Il report distingue prefill e decode ripetuto.
La consegna avanzata deve includere dimensioni non multiple del tile e più
ripetizioni. Su GPU richiedere sincronizzazione; su CPU non inventare una
misura GPU. Una tolleranza troppo larga che nasconde errori non è equivalenza.

## M19 - Capstone e codec esatto

Nel ramo applicativo richiedere un bisogno definito, baseline, eval e casi
di errore; E01-E03 forniscono componenti da integrare, S00-S05 il metodo di
sviluppo. Nel ramo codec, tutti gli otto casi del report ricostruiscono i byte.
Per il testo sintetico di 148 byte: adattivo 359, neurale 317, gzip 60; il
neurale aggiunge 347.451 byte di modello al primo trasferimento. Quindi non
vince quel confronto. L'hash del checkpoint lega la versione, ma non prova
CDF identiche su CPU diverse. Richiedere un test di corruzione e un mismatch
di modello; qualunque differenza di byte boccia il criterio lossless.
L'integrazione fisica PollicinoNet resta separata e non viene simulata come
prova radio. Il capstone del corso può essere completato senza quel gate.
