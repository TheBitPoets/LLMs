# Guida docente

## Obiettivo e tono

Il corso forma utilizzatori critici e costruttori, non spettatori di demo. Ogni
incontro parte da una previsione dello studente, rende visibile un meccanismo,
produce un artefatto e chiude con una domanda diagnostica. I termini inglesi
utili restano accanto all'italiano.

## Struttura di una lezione da due ore

| Minuti | Attività | Evidenza |
| ---: | --- | --- |
| 0–10 | Problema concreto e previsione individuale | Ticket iniziale. |
| 10–30 | Visuale progressiva controllata dagli studenti | Due spiegazioni alternative. |
| 30–50 | Esempio numerico o dimostrazione | Calcolo annotato. |
| 50–90 | Laboratorio a coppie: driver/navigator | JSON/report o scheda. |
| 90–105 | Failure injection del docente | Errore osservato e recupero. |
| 105–115 | Confronto con baseline e limiti | Decisione motivata. |
| 115–120 | Exit ticket | Una risposta e una domanda aperta. |

## Sequenza dell'anno

Usare la scansione M00–M19 della mappa curricolare. Le 60 ore guidate includono
recupero e verifiche formative; il capstone usa lavoro aggiuntivo. Se il tempo
si riduce, non eliminare M02, M05, M09–M15 e M19: ridurre invece ablation e
cataloghi specialistici.

## Differenziazione a due livelli

- **Percorso base:** visuale, manipolazione, linguaggio concreto, coppia di
  esempi e un controesempio; formule solo dopo la relazione osservata.
- **Percorso avanzato:** stessa figura e stessi colori, con shape, equazioni,
  complessità, pseudocodice e paper.
- **Recupero:** cambiare rappresentazione, non ripetere la stessa spiegazione;
  usare una sequenza più corta e far verbalizzare input/trasformazione/output.
- **Potenziamento:** chiedere un test che potrebbe smentire la conclusione o
  una baseline più semplice.

## Minori, privacy e uso responsabile

Non inserire dati personali, sanitari, disciplinari o elaborati identificabili
in servizi esterni. Il percorso base è locale e usa fixture sintetiche. Tool e
agenti sono read-only, con allowlist, budget e approvazione. Il docente verifica
policy d'istituto, licenze e informativa prima di introdurre account/provider.

Il modello non assegna autonomamente voti e non prende decisioni educative ad
alto impatto. Un output offensivo o errato diventa failure case redatto, non
materiale da redistribuire senza contesto.

## Profili hardware

- Profilo A: browser + Python 3.11, nessun modello; copre visuali e L00–L10.
- Profilo B: 8–16 GB, Ollama e modello 0.8B–4B quantizzato; output corto.
- Profilo C: Mac M4 Pro 36 GB; confronto 4B–9B, eventuale 27B solo dopo stima.
- Profilo D: GPU dedicata; estensione kernel/tuning, mai prerequisito per la classe.

Se Ollama non è disponibile, usare report registrati e completare il rehearsal
successivamente. Non simulare una misura hardware come se fosse reale.

## Valutazione

La diagnostica iniziale non fa media. Ogni modulo usa 10 punti con soglia 6;
gli aspetti safety/provenienza indicati come gate non possono essere compensati.
Il capstone usa la rubrica M19. Conservare esempi di errori e revisioni, non solo
il prodotto finale.

## Provenienza delle immagini

Le figure Manning restano fonti private. In classe e nel repository si usano le
ricostruzioni originali del catalogo, con citazione del concetto e dichiarazione
dei limiti. Nessuna scansione del libro viene incorporata nelle slide pubbliche.

