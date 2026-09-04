# Criteri di completamento della prima edizione

Questa pagina impedisce di dichiarare “finito” il corso quando esiste soltanto
un indice o quando una demo funziona su una singola macchina.

## Un modulo è completo quando

- dichiara destinatari, prerequisiti, obiettivi osservabili e durata stimata;
- contiene una spiegazione intuitiva autonoma e non matematicamente falsa;
- offre l'approfondimento matematico necessario o rimanda in modo preciso a esso;
- collega almeno una fonte primaria o autorevole e ne conserva la provenienza;
- include un esempio svolto e un laboratorio o una dimostrazione riproducibile;
- distingue concetti stabili da dettagli correnti e datati;
- contiene domande diagnostiche, verifica finale e criteri di correzione;
- registra limiti, rischi e affermazioni che l'evidenza non autorizza;
- è leggibile in italiano mantenendo i termini tecnici inglesi utili;
- supera i controlli automatici applicabili a link, codice e fixture.

## Un laboratorio è completo quando

- parte da un ambiente dichiarato e riproducibile;
- fornisce una modalità docente e una modalità studente senza soluzioni esposte;
- usa dati leciti, piccoli e versionati;
- non richiede credenziali reali per il percorso base;
- produce un artefatto o report verificabile, non solo output a schermo;
- include almeno una baseline semplice e un test negativo;
- annota modello, runtime, versione, quantizzazione, hardware e parametri;
- gestisce errori prevedibili e dispone di istruzioni di ripristino;
- dichiara quali risultati sono locali, sintetici o non generalizzabili;
- è stato eseguito almeno una volta sul profilo hardware supportato.

## Il percorso Practitioner è completo quando

- tutti i moduli M00–M19 hanno una lezione fruibile ai livelli I/P/V;
- esistono almeno dodici laboratori eseguibili, di cui uno con Ollama, uno di
  confronto modelli, uno di valutazione, uno RAG e uno applicativo;
- uno studente può scegliere un modello locale motivando memoria, licenza,
  qualità, lingua, latenza e privacy;
- lo studente sa distinguere modello, tokenizer, runtime, interfaccia e servizio;
- lo studente sa costruire un'applicazione locale e valutarla su un piccolo task;
- è disponibile una prova iniziale, verifiche formative e una rubrica finale;
- il capstone è eseguibile senza accesso obbligatorio a un provider cloud.

## Il percorso AI Engineer è completo quando

- ogni modulo possiede gli strati M/E/R pertinenti;
- algebra lineare, probabilità, calcolo, ottimizzazione e informazione sono
  collegati direttamente agli esperimenti che li richiedono;
- viene implementato e addestrato un piccolo Transformer da zero;
- almeno un percorso di fine-tuning/adapter è riprodotto e confrontato con una baseline;
- evaluation, RAG e agenti includono failure analysis e non solo happy path;
- vengono profilati prefill, decode, memoria e KV cache;
- esiste un kernel d'inferenza minimale confrontato con un riferimento;
- il percorso Pollicino arriva almeno al codec classico/statistico esatto e
  documenta separatamente lo stato del Byte Transformer neurale;
- una selezione di paper viene riprodotta in scala didattica o analizzata con
  esperimenti che rendano visibile l'idea centrale;
- il capstone produce codice, report, metriche, decisioni e limiti verificabili.

## Il corso è pronto per il rilascio quando

- la struttura del repository consente di trovare moduli, laboratori, fonti,
  matematica, paper, catalogo dei modelli, verifiche e guida docente;
- tutti i collegamenti interni e gli script di controllo passano;
- nessun segreto, dato personale, peso non ridistribuibile o testo editoriale
  protetto è incluso impropriamente;
- le fonti acquistate sono citate e trasformate, non ripubblicate;
- catalogo dei modelli e prezzi riportano una data di aggiornamento;
- le affermazioni su modelli recenti sono verificate su fonti ufficiali;
- almeno un percorso end-to-end è stato provato sul profilo locale supportato;
- la documentazione dichiara cosa resta opzionale, sperimentale o bloccato da hardware;
- la draft PR riceve una revisione finale senza finding bloccanti;
- soltanto dopo questi controlli la versione viene etichettata `course-v1`.

## Debito consentito nella prima edizione

La prima edizione può rinviare senza fingere completezza:

- training distribuito su cluster multi-GPU;
- implementazioni CUDA altamente ottimizzate;
- addestramento da zero di modelli competitivi di grandi dimensioni;
- prove fisiche PollicinoNet non ancora autorizzate dai gate hardware;
- copertura enciclopedica di ogni modello o paper pubblicato.

Non può invece rinviare la capacità di scegliere, eseguire, misurare e usare un
modello locale, né la comprensione del ciclo next-token e dell'architettura
Transformer a entrambi i livelli previsti.
