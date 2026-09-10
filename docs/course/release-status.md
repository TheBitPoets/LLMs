# Stato di rilascio e lavoro residuo

Audit aggiornato: **10 settembre 2026**.

## Valutazione corretta

**Il corso è in ampliamento: non resta soltanto il test hardware.** La precedente
frase «Course materials complete» era troppo forte rispetto alle implementazioni
disponibili. Avere capitoli per tutti gli argomenti non significa avere già
laboratori completi e soluzioni sviluppate per tutti gli obiettivi AI Engineer.

## Materiali disponibili

- 20 moduli LLM con spiegazioni Practitioner/AI Engineer, glossario e apparati.
- Content Pack LLM v1, Course Design annuale 34 settimane × 2 ore e 20 Activity.
- Sei lezioni aggiuntive S00-S05 sullo sviluppo software con coding agent,
  Content Pack autonomo, Course Design di 12 ore e sei Activity A-F.
- Progetto PrenotaLab: starter deliberatamente incompleto, specifica R01-R08,
  test pubblici e soluzione docente con memoria, SQLite e transazioni.
- Adapter Ollama per proposte JSON e relativi test con risposta simulata;
  nessuna prenotazione viene creata da una risposta LLM.
- Riferimenti Manning verificati su schede pubbliche il 10 settembre;
  capitoli liveBook non letti in questa sessione per errore di accesso 403.
- Dispense PDF studente/docente, visuali interattive e figure originali.
- Runner minimo con esperimenti di probabilità, byte, gradienti, attention,
  memoria euristica, sampling, valutazione di fixture e codec A/B.
- Correzione dei comandi inesistenti o privi di argomenti nelle dispense;
  controllo automatico che gli esempi CLI siano accettati dal parser reale.

## Limiti concreti da completare nel percorso LLM

| Obiettivo | Disponibilità corrente | Lavoro ancora necessario |
| --- | --- | --- |
| Chat applicativa | Richiesta Ollama non streaming | Client con stato, streaming, cancel e test end-to-end |
| RAG completo | Retrieval lessicale sulle fixture | Embedding, generazione con fonti ed eval end-to-end |
| Agenti e MCP | Parser/calcolatore deterministico | Applicazione con tool calling reale e integrazione MCP verificata |
| Training e LoRA | Teoria, regressione scalare e tracce | Piccolo modello neurale, training riproducibile, adapter ed eval |
| Kernel d'inferenza | Calcolo Python e visuali | Reference numerica, kernel ottimizzato e misure hardware |
| Pollicino neurale | Codec A/B didattico esatto | Codifica byte generale, modello neurale e integrazione nel progetto esterno |
| Soluzioni dei 20 moduli | Criteri e quick-check | Ulteriori soluzioni eseguibili per gli obiettivi avanzati |
| Modelli recentissimi | Snapshot 4 settembre | Nuova verifica datata delle release e prove sul compito |

Il supplemento software dispone di un proprio progetto eseguibile e verificato
con test automatici. Gli esercizi avanzati di confronto modelli e revisione
dello schema con chiarimenti sono consegne da svolgere, non misure già raccolte.

## Verifiche e gate distinti

La CI controlla struttura, link, metadati generati, JavaScript, test Python e
integrità dei PDF. I PDF devono superare lettura strict, controllo xref/EOF,
lettura degli stream di ogni pagina e ispezione visiva dopo la rigenerazione.
La verifica dei blob GitHub deve confrontarne lo SHA con il file locale,
per evitare la troncatura binaria che aveva reso invalidi i PDF precedenti.

Il rehearsal sul Mac M4 Pro 36 GB resta rinviato come concordato. Non sono
stati misurati in questo ambiente digest, memoria, TTFT, token/s o qualità di
modelli locali reali. Le risposte simulate degli unit test non sostituiscono
una sessione con coding agent né il confronto locale/cloud.

Il pack LLM conserva `reviewed`, il supplemento software è `draft`. Il docente
deve rivedere contenuti, soluzioni e tempi prima di portarli ad `approved` e
generare un Course Bundle immutabile. Non creare `course-v1` né dichiarare
«validato in classe» prima di chiudere i residui e raccogliere le evidenze.
