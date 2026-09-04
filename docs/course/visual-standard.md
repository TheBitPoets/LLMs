# Standard visuale del corso LLM

Questo standard specializza il *Raiatea Pedagogical Visual Standard* per il
corso LLM. Una figura editoriale è una fonte da interpretare, non un asset da
copiare automaticamente.

## Principio

> Una buona immagine non decora la spiegazione: rende visibile un cambiamento
> di stato, una relazione o una scelta che il testo da solo costringe a tenere
> nella memoria di lavoro.

Per ogni concetto difficile si preferisce una sequenza controllabile:

1. orientamento: che cosa entra e che cosa vogliamo osservare;
2. un solo cambiamento visuale per passo;
3. spiegazione breve del perché;
4. possibilità di tornare indietro, mettere in pausa e cambiare un valore;
5. consolidamento con domanda diagnostica e limite dell'analogia.

## Uso delle immagini dei libri

- Conservare privatamente la figura sorgente e la sua coordinata bibliografica.
- Annotare quali relazioni o passaggi si vogliono spiegare meglio.
- Creare una ricostruzione originale, con struttura e grafica proprie.
- Citare il libro come fonte del concetto o come confronto, senza incorporare
  materiale editoriale protetto quando non necessario.
- Se una figura deve essere mostrata direttamente, farlo soltanto nel perimetro
  consentito dalla licenza e mai pubblicarla nel repository senza autorizzazione.
- Separare sempre: **fonte**, **interpretazione**, **adattamento didattico** e
  **nuova evidenza prodotta dal laboratorio**.

## Corredo minimo di ogni modulo

Ogni modulo M02–M18 dovrebbe possedere almeno:

- una **mappa iniziale** con input, trasformazione e output;
- una **figura progressiva** per il meccanismo centrale;
- un **esempio numerico** visualizzato;
- una **vista rigorosa** che usa gli stessi colori e oggetti della vista intuitiva;
- una **figura di confronto** quando esistono scelte progettuali;
- una **versione statica stampabile** dell'ultimo stato significativo;
- testo alternativo e didascalia che non dipendano dal colore.

## Visuali prioritarie

| Modulo | Visuale o animazione | Interazione utile |
| --- | --- | --- |
| M02 | Il ciclo next-token | Avanti/indietro tra contesto, logits, probabilità, scelta e nuovo contesto. |
| M03 | Tokenizzazione | Modificare una stringa e confrontare byte e token di tokenizer differenti. |
| M04 | Discesa della loss | Muovere un parametro e vedere previsione, errore e gradiente. |
| M05 | Query, Key, Value | Selezionare un token e osservare score e combinazione dei Value. |
| M06 | MHA, MQA e GQA | Variare il numero di gruppi KV e vedere memoria e condivisione. |
| M07 | Scaling e dati | Variare parametri/token/compute distinguendo trend da garanzia. |
| M08 | Dal base model all'assistente | Attivare SFT e preference optimization osservando cosa cambia. |
| M09 | Anatomia di un modello | Aprire config, tokenizer, shard di pesi e metadati di licenza. |
| M10 | Modello dentro la memoria | Variare parametri, precisione, quantizzazione, KV cache e context length. |
| M12 | Sampling | Controllare temperature, top-k, top-p e seed sulla stessa distribuzione. |
| M14 | Evaluation | Confrontare media, distribuzione degli errori e casi critici. |
| M15 | RAG | Seguire query, embedding, retrieval, reranking, contesto e risposta citata. |
| M16 | Agente | Vedere stato, scelta del tool, approvazione, risultato e stop condition. |
| M18 | Prefill e decode | Osservare KV cache, memoria e costo per token. |
| M19 | Pollicino | Trasformare probabilità next-byte in intervalli e poi in bit esatti. |

## Tre profondità sulla stessa figura

### Vista intuitiva

Etichette brevi, oggetti familiari, massimo una nuova relazione per passo.
L'analogia dichiara dove smette di essere corretta.

### Vista tecnica

Tensor shape, parametri, pseudocodice e costi computazionali vengono sovrapposti
agli stessi oggetti, senza cambiare improvvisamente il modello mentale.

### Vista matematica

Le equazioni compaiono accanto al passaggio che calcolano. Se si seleziona un
termine, la visuale evidenzia le quantità corrispondenti. La formula non è una
slide separata e decontestualizzata.

## Movimento e accessibilità

- Nessun autoplay obbligatorio.
- Controlli precedente, successivo, pausa, ripeti e salto diretto.
- Rispetto di `prefers-reduced-motion` e interruttore interno.
- Nessun lampeggio; durata e direzione non devono essere l'unico veicolo di significato.
- Navigazione da tastiera e focus visibile.
- Contrasto verificabile e palette compatibile con comuni deficit cromatici.
- Testo alternativo che descrive la relazione, non l'aspetto decorativo.
- Layout utilizzabile su proiettore, notebook e schermo stretto.

## Gate di qualità

Una visuale entra nel corso soltanto se:

1. riduce un errore concettuale plausibile;
2. ogni animazione ha uno scopo didattico nominabile;
3. la versione statica conserva il significato essenziale;
4. esempi, formule e codice concordano;
5. il learner controlla il ritmo;
6. fonte e trasformazione sono tracciabili;
7. semplificazioni e limiti sono visibili;
8. una domanda verifica comprensione o trasferimento, non memoria dell'etichetta.
