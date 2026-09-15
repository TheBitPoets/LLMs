# Percorso pratico: progettare software con coding agent

Questo percorso insegna a realizzare e mantenere software usando l'AI nel
lavoro quotidiano. Non richiede lo studio della matematica dei Transformer.
Si collega a M11-M16 per scelta del modello, API, contesto e valutazione.
Il prodotto guida è **PrenotaLab**, un gestore di prenotazioni scolastiche.

## Risultati e destinatari

Lo studente trasforma una richiesta in esempi verificabili, prepara il contesto
per un agente, rivede un diff, diagnostica una regressione e consegna codice
che sa spiegare. Servono funzioni, liste, eccezioni Python e test elementari;
per chi parte da zero prevedere un laboratorio Python preliminare.

Il percorso avanzato ha due diramazioni pratiche. L'**AI Engineer** progetta
adapter LLM, valuta output strutturati e confronta modelli sul proprio compito.
Il **software engineer** lavora su codice esistente, confini architetturali,
transazioni, concorrenza, revisioni di specifica e integrazione continua.
Sono approfondimenti dello stesso progetto, non qualifiche professionali
ottenibili con dodici ore di esercizi.

## Sequenza didattica

| Lezione | Attività principale | Consegna |
| --- | --- | --- |
| [S00](S00-contesto.md) | A: leggere ed eseguire | Baseline e mappa del repo |
| [S01](S01-specifiche.md) | B: precisare le regole | Specifica e casi di accettazione |
| [S02](S02-implementazione.md) | C: implementare una porzione | Patch, test e spiegazione |
| [S03](S03-diagnosi.md) | D: diagnosticare | Regressione riprodotta e corretta |
| [S04](S04-pattern.md) | E: costruire un mini-progetto | Cancellazione e adapter |
| [S05](S05-consegna.md) | F: integrare e valutare | Release riproducibile e report |

La pianificazione autonoma è di **6 incontri da 2 ore: 12 ore per la classe**.
Gli approfondimenti richiedono indicativamente altre 6 ore per il ramo AI
Engineer e altre 6 per il ramo software engineer, da validare con un pilot.
Chi svolge entrambi aggiunge 12 ore, oltre le 12 comuni.

Il Course Design annuale LLM resta di **34 settimane × 2 ore = 68 ore**.
Questo supplemento ha un proprio Content Pack/Course Design. Per inserirlo
nell'anno occorre allocare esplicitamente 12 ore aggiuntive (80 totali), oppure
sostituire laboratori per 12 ore e registrare nel piano quali vengono rimandati.
Qui non viene effettuata una sostituzione implicita.

## Materiali e modalità

Il [kit eseguibile](../../../labs/ai_software/README.md) esporta soltanto i file
studente in un nuovo repository di lavoro. La soluzione docente non deve essere
passata al coding agent durante l'esercizio. I metadati separano gli asset
studente/docente; il repository GitHub pubblico non rende segrete le soluzioni.
Per una verifica sommativa il docente deve usare una variante non pubblicata.

Un coding agent può leggere file, proporre modifiche e, secondo lo strumento,
eseguire verifiche. Un modello è solo una parte del sistema: contano anche
strumenti, istruzioni, contesto, permessi e interfaccia. Il percorso è neutrale
rispetto al prodotto; funziona con uno strumento disponibile nel laboratorio,
oppure con un assistente locale e applicazione manuale delle patch. Nel secondo
caso registrare **sviluppo assistito**, senza dichiarare un agente autonomo.

Il progetto base funziona senza account e senza un modello. Per certificare
l'esperienza con un coding agent, però, serve almeno una sessione reale con
prompt, modifiche e verifiche registrati. I test automatici di questo repository
validano gli esempi software, non le prestazioni di un agente o l'efficacia in classe.

Le dispense, i test e le figure sono originali. I
[riferimenti Manning verificati](../sources/manning-coding-agents-2026-09-10.md)
guidano gli approfondimenti del docente. *Vibe Engineering* informa in
particolare il filo pratico S02-S03-S05: lavorare per incrementi piccoli,
validare, rifattorizzare senza cambiare il contratto e consegnare con evidenze.

> **Fonte/ispirazione:** [Vibe Engineering](https://www.manning.com/books/vibe-engineering),
> scheda pubblica, § «about the book» (ispirazione; verificato 2026-09-15).

Il laboratorio non dipende da
capitoli MEAP ancora da pubblicare. Lo stato editoriale del nuovo pack è `draft`
in attesa di revisione didattica. Non è ancora un Course Bundle approvato.
