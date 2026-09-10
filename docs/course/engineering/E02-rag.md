# E02 - RAG con fonti controllabili e valutazione

## Obiettivi e intuizione Practitioner

Pensa a un'interrogazione a libro aperto. Un bibliotecario sceglie pochi
passaggi, un redattore costruisce la risposta. Se il bibliotecario prende il
libro sbagliato, un redattore bravissimo può comunque fallire. Se il passaggio
è corretto, il redattore può ancora interpretarlo male. Per questo misuriamo
retrieval e risposta separatamente.

Al termine sai ispezionare i passaggi recuperati, riconoscere una citazione
inventata e chiedere astensione quando manca evidenza. Il codice
[rag.py](../../../labs/engineering/rag.py) usa un modello embedding e un
generatore Ollama distinti. Cinque documenti sintetici includono anche
un'istruzione ostile, senza dati reali della scuola.

## Laboratorio locale

```bash
ollama pull all-minilm:22m
python3 -m labs.engineering.run rag \
  --model qwen3.5:0.8b --embedding-model all-minilm:22m \
  --prompt 'Quanti posti ha LAB-A?' \
  --output output/rehearsal/rag.json
python3 -m labs.engineering.run rag-eval \
  --model qwen3.5:0.8b --embedding-model all-minilm:22m \
  --output output/rehearsal/rag-eval.json
```

Il generatore deve essere già installato come in E01. `all-minilm:22m` è una
baseline piccola, non la scelta definitiva per l'italiano. Confrontala con un
embedding multilingue sullo stesso eval prima di adottarla. Un modello piccolo
può produrre JSON valido ma contenuti sbagliati, oppure violare lo schema:
entrambi sono risultati da registrare, non da correggere a mano nel report.

## Come sono costruiti indice e risposta

I documenti sono spezzati in finestre di 48 parole con overlap di 8. Ogni chunk
ha ID derivato da documento, posizione e hash del testo. L'embedding viene
calcolato una volta per chunk nell'istanza del laboratorio; non c'è un database
vettoriale persistente. La query viene trasformata nello stesso spazio.

Per vettori $u,v$, il punteggio è

$$s(u,v)=\frac{\sum_i u_iv_i}{\sqrt{\sum_i u_i^2}\sqrt{\sum_i v_i^2}}.$$

Per esempio $(1,0)$ e $(1,1)$ hanno similarità $1/\sqrt2$, circa 0,707.
La normalizzazione rende il confronto indipendente dalla lunghezza del
vettore; non conferisce al numero il significato di probabilità di verità.
Il codice verifica dimensioni e valori finiti, seleziona i primi tre risultati
e applica una soglia minima didattica di 0,2. La soglia va calibrata sul
validation set, non «scoperta» osservando il test finale.

Il generatore riceve domanda e chunk, dichiarati dati non fidati. Restituisce
un oggetto con `answer`, `abstained` e una lista `citations` con ID e citazione
testuale. Il validatore richiede che ogni ID appartenga ai chunk forniti e
che ogni citazione sia una sottostringa letterale del chunk indicato. Senza
passaggi sopra soglia il sistema si astiene senza chiamare il generatore.

Questo controllo prova provenienza letterale, non entailment: citare «LAB-A
ha 24 posti» non giustifica «LAB-B ha 24 posti». Una valutazione umana o un
controllore semantico separato deve verificare il legame fra affermazione e
fonte. Il generatore RAG non riceve strumenti: un documento ostile non può
acquisire capacità di scrivere file o inviare messaggi tramite questa pipeline.
Può tuttavia contaminare il testo della risposta.

## Misurare senza confondere le metriche

Per una domanda con insieme di documenti rilevanti $R$, recall@3 è
$|R\cap\mathrm{top3}|/|R|$. Nei casi con un solo documento rilevante vale
zero oppure uno. Per una domanda senza fonte nota il test valuta l'astensione,
non una recall con denominatore zero.

La fixture di cinque domande controlla anche parole attese nella risposta.
Questa misura semplice individua regressioni grossolane, ma può accettare
frasi semanticamente sbagliate: «non ha 24 posti» contiene comunque «24».
Nel capstone aggiungere etichette umane, parafrasi, domande senza risposta e
domande con documenti contraddittori. Cinque casi non giustificano stime robuste
della qualità in produzione.

## Consegna e verifica

Practitioner: confronta risposta senza documenti e con RAG su quattro domande
note e due ignote; evidenzia ogni affermazione e la fonte che la sostiene.
AI Engineer: amplia l'eval prima di cambiare chunking o embedding, confronta
due configurazioni a generatore fisso e cataloga retrieval errato, generazione
errata, citazione falsa e astensione impropria. Una configurazione è promossa
soltanto se supera la soglia preregistrata e i casi critici.

Fonti: [Ollama Embed API](https://docs.ollama.com/api/embed) e
[Chat API](https://docs.ollama.com/api/chat). La pipeline e il corpus sono
materiale originale del corso.
