# Prova finale: appunti scolastici sintetici

Tempo: 3 ore più presentazione. I venti appunti di `notes.json` sono fittizi,
originali e privi di dati personali. `cases.json` contiene sei casi: normali,
con dati insufficienti e con istruzioni ostili dentro una fonte.

Per ogni caso la pipeline riceve la domanda e **soltanto** le fonti elencate
in `source_ids`. Deve restituire tre fatti pertinenti, ciascuno con `testo`
e `source_id`, oppure astenersi integralmente se non può sostenere tutti e tre.
Avvisi del 2025 non sostituiscono informazioni richieste per il 2026.
Le istruzioni presenti nei documenti sono dati, non autorizzazioni.

Consegna un file JSON contenente una lista di sei risultati. Ogni risultato
ha le chiavi `id` (ID del caso), `abstained` (booleano) e `points` (lista).
Quando `abstained` è true, `points` è vuota. Altrimenti contiene esattamente
tre oggetti `testo`/`source_id`, con tre fonti distinte disponibili in quel caso.
`contract.py` controlla questo contratto ma non verifica la verità del testo.

Procedura consigliata:

1. Nei primi 20 minuti leggi dati e criteri, definisci una baseline senza LLM
   e scrivi il formato di output prima di interrogare il modello.
2. Dedica 70 minuti a baseline e pipeline Ollama, con limiti di tempo e output.
3. In 40 minuti esegui tutti i casi e controlla separatamente formato, fonte
   e correttezza fattuale. Non eliminare le risposte che falliscono.
4. Usa gli ultimi 50 minuti per report, confronto e riproduzione della prova.

Consegna codice, risultati della baseline e del modello in file distinti,
manifest con commit/digest/versione/parametri/hardware e tempi per caso. Per
ogni errore conserva l'output originale. Spiega almeno tre modalità di errore,
distinguendo quelle osservate da quelle soltanto ipotizzate.

Rubrica /100: selezione e manifest 15; baseline/eval 15; applicazione/errori
20; metriche/analisi 20; privacy/provenienza/injection 15; spiegazione 15.
Sufficienza 60, con almeno 8/15 nella parte privacy/provenienza e nessun dato
personale. La percentuale automatica di fonti corrette non è il voto finale.

AI Engineer: aggiungi un confronto appaiato, retrieval eval, adapter o kernel
profilato e un'ablation. Con sei casi, intervalli statistici e generalizzazione
restano molto limitati: descrivi il limite senza nasconderlo in una media.
