# Stato di rilascio e verifiche residue

Aggiornamento: **10 settembre 2026, edizione LLM 0.10.0**.

## Materiali e implementazioni

Il percorso dispone ora di 20 moduli LLM, otto capitoli engineering E00-E07
con matematica e implementazioni, e sei lezioni pratiche S00-S05 sullo sviluppo
software con coding agent. Le soluzioni dei venti moduli sono sviluppate per
argomento e separate dagli asset studente.

Il piano annuale resta di 34 settimane per 2 ore. E00-E07 approfondisce i
moduli esistenti; lo studio integrale AI Engineer richiede circa 32 ore
aggiuntive. S00-S05 conserva il proprio Course Design di 12 ore e le due
estensioni personali di 6 ore. Queste stime non sostituiscono i tempi in classe.

## Evidenze disponibili

| Obiettivo | Implementazione e verifica |
| --- | --- |
| Chat | Stato, streaming, cronologia, timeout e cancellazione; test HTTP locale con risposte simulate |
| RAG | Embedding Ollama, ranking, generazione JSON, citazioni letterali e astensione; test di contratto e fixture eval |
| Agenti | Ciclo di tool calling con allowlist, budget e traccia; provider simulato nei test |
| MCP | Sottoinsieme stdio 2025-06-18; handshake, discovery e chiamata fra processi reali |
| Training | Transformer byte da 84.288 parametri, corpus originale, split e checkpoint; training CPU eseguito |
| LoRA | 1.216 parametri sulla head; pesi base invariati, miglioramento target e regressione base misurati |
| Inferenza | Reference, tiled online softmax e funzione di libreria; equivalenza, KV cache e tempi CPU |
| Codec | Tutti i byte e file vuoto, predittore adattivo o neurale; otto round trip e confronto gzip con costo del modello |
| Software con AI | PrenotaLab, specifiche, test, soluzione SQLite e adapter di sola proposta |
| Modelli recenti | Nuovo catalogo datato 10 settembre con fonti ufficiali |

Le misure e i piccoli checkpoint originali sono in
[output/engineering](../../output/engineering). Il modello non è un assistente
generale: i dati condividono template sintetici. LoRA peggiora il dominio
originale; il tiled Python è più lento del riferimento nella prova; il codec
neurale non batte gzip nei casi misurati. Questi risultati fanno parte delle
lezioni e non vengono presentati come successi universali.

## Verifiche che restano realmente aperte

1. **Rehearsal sul Mac M4 Pro 36 GB**, rinviato come concordato dopo tutti i
   corsi dell'anno: eseguire chat, RAG, tool calling e confronto di almeno due
   modelli Ollama reali; registrare digest, memoria, tempi, qualità ed errori.
2. **Revisione docente** di contenuti, soluzioni e tempi effettivi prima
   dell'uso in classe e dell'approvazione didattica del pack.
3. **Freeze del Course Bundle**, successivo ai gate: stato `approved` e tag
   `course-v1` non vengono anticipati.

I laboratori applicativi sono implementati e testati a livello di contratto;
non sono dichiarati collaudati con ogni modello del catalogo. Mancano ancora
le misure live Ollama sul profilo supportato, richieste dalla definition of done.
Quindi il completamento dei materiali non equivale ancora alla chiusura di
tutti i criteri di rilascio.

L'integrazione nel progetto esterno PollicinoNet, la portabilità numerica
bit-per-bit del codec fra hardware diversi e kernel CUDA competitivi restano
estensioni di ricerca, non prerequisiti del capstone locale di questa edizione.

## Content Pack, PDF e pubblicazione

Il [verbale di verifica](engineering/VALIDATION.md) riporta ambiente, comandi,
65 test superati, validazione canonica e controllo delle dispense.

Il pack LLM usa `thebitlab.content-pack.v1`, conserva `reviewed` e indicizza
i capitoli engineering originali senza gli apparati docente. Le Activity
distribuiscono esempi e test attraverso asset dichiarati. Il supplemento
software conserva `draft`. I riferimenti Manning rimangono teacher-reference:
le schede pubbliche sono state consultate, i capitoli liveBook non sono stati
letti in questa sessione per il precedente errore di accesso.

La CI controlla metadati generati, link, test Python, JavaScript e PDF.
I PDF devono superare apertura strict, xref/EOF e lettura di tutte le pagine,
oltre al controllo visivo dopo la build. I blob pubblicati vengono confrontati
con gli SHA locali, includendo PDF e checkpoint, per evitare troncature.
