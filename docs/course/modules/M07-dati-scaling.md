# M07 — Pre-training, dati e scaling

**Domanda guida:** che cosa otteniamo aumentando dati, parametri e calcolo?
**Durata:** 3 ore Practitioner; 10 ore AI Engineer.
**Prerequisiti:** M04–M06.

## Obiettivi osservabili

Saprai descrivere acquisizione, filtraggio, deduplicazione, mixture e data governance; interpretare le scaling law senza trasformarle in garanzie. Il livello AI Engineer ragiona su token budget, compute-optimal training, contaminazione e documentazione del dataset.

## Problema iniziale

“Più dati” sembra sempre meglio. Ma duplicati, dati personali, codice con licenza incompatibile, testi tossici o test set presenti nel training possono migliorare alcune metriche e peggiorare affidabilità e legalità. Il dataset è parte del comportamento del modello.

## Teoria Practitioner

Una pipeline di pre-training raccoglie fonti, estrae contenuti, filtra qualità, lingua e sicurezza, rimuove duplicati, applica pesi alle sorgenti e tokenizza. Ogni filtro produce falsi positivi e falsi negativi. La mixture decide quanto spesso il modello vede ciascun dominio; una piccola fonte può essere sovracampionata.

Le **scaling law** descrivono regolarità empiriche: entro un intervallo, la loss tende a migliorare in modo prevedibile aumentando parametri, dati e compute. Non dicono che ogni capacità cresca uniformemente né risolvono qualità, allineamento o contaminazione.

## Esempio minimo

Un corpus contiene cento copie della stessa pagina e cento pagine diverse. Contare i documenti suggerisce 200 esempi; deduplicare rivela solo 101 contenuti. Se il test contiene la pagina duplicata, il punteggio può misurare memoria invece di generalizzazione.

## Esempio realistico

Per un modello didattico italiano costruisci una data card: origine, autorizzazione, periodo, lingue, rimozione PII, deduplicazione, split e limiti. Prima del training calcola hash dei documenti e cerca sovrapposizioni tra train e test. Conserva lo script di trasformazione, non soltanto il dataset finale.

## Livello AI Engineer: budget e contaminazione

Il compute di training di un decoder dense è spesso stimato come ordine di grandezza $C\approx6ND$, con $N$ parametri e $D$ token, ma architettura e implementazione cambiano la costante. Risultati compute-optimal mostrano che, dato un budget, un modello troppo grande e poco addestrato può essere peggiore di uno più piccolo con più token.

La contaminazione non è soltanto corrispondenza esatta. Parafrasi, soluzioni, traduzioni e dati derivati possono attraversare gli split. Si usano hashing, MinHash o similarità embedding, ma nessun filtro prova assenza completa. I benchmark devono dichiarare cutoff temporale e procedure di decontaminazione.

Data governance comprende base giuridica, consenso o licenza, diritto di rimozione, provenienza, sicurezza e impatto sui gruppi. “Disponibile sul web” non significa automaticamente riutilizzabile per training o redistribuzione.

## Errori frequenti

- Contare volume grezzo ignorando duplicati.
- Usare benchmark pubblici durante molte iterazioni e chiamarli ancora test.
- Concludere che una legge empirica valga fuori dal regime osservato.
- Documentare le fonti ma non le trasformazioni.
- Confondere accessibilità con licenza.

## Esercizi A–F

- **A:** ordina gli stadi di una pipeline dati.
- **B:** applica deduplicazione a un piccolo corpus.
- **C:** redigi una data card con provenienza e limiti.
- **D:** individua leakage tra train, validation e test.
- **E:** progetta una mixture multilingue e giustifica i pesi.
- **F:** costruisci pipeline versionata con audit, decontaminazione e report.

## Laboratorio

Esegui `python3 labs/course_lab.py scaling` per esplorare una relazione semplificata. Poi crea un corpus giocattolo, calcola hash, elimina duplicati e mostra come cambia una metrica. L'obiettivo è vedere quanto il dataset possa alterare una conclusione.

## Verifica rapida

Spiega perché più dati non equivale a dati migliori; distingui scaling law e garanzia; descrivi due forme di contaminazione; elenca i campi minimi di una data card.

## Sintesi inclusiva

Il modello apprende ciò che la pipeline rende frequente e osservabile. Dimensione, qualità, mixture, licenze e contaminazione devono essere trattate insieme. Le scaling law aiutano a pianificare, non sostituiscono la misura.

## Fonti e collegamenti

- [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)
- [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)
- [Data Statements for NLP](https://aclanthology.org/Q18-1041/)
- Activity: `llm-activity-m07-data-card`
