# M14 — Valutazione

**Domanda guida:** come sappiamo se un modello o un'applicazione è adatto al nostro scopo?
**Durata:** 4 ore Practitioner; 14 ore AI Engineer.
**Prerequisiti:** M00, M10–M13.

## Obiettivi osservabili

Saprai trasformare requisiti in dataset, metriche e soglie; confrontare qualità, latenza, memoria, costo e sicurezza; costruire un regression set. Il livello AI Engineer stima incertezza, accordo tra annotatori e limiti di model-as-judge.

## Problema iniziale

Un benchmark pubblico assegna 78 punti al modello A e 75 al B. Per il tuo chatbot scolastico A è davvero migliore? Non sappiamo lingua, task, formato, hardware, contaminazione, costo o errore più grave. La valutazione utile parte dalla decisione che dobbiamo prendere.

## Teoria Practitioner

Definisci prima i casi d'uso e gli errori inaccettabili. Costruisci esempi rappresentativi, casi limite e test avversariali. Una metrica aggregata deve essere accompagnata da esempi di errore. Accuracy va bene solo quando classi e costo degli errori lo permettono; precision, recall e F1 rispondono a domande diverse.

Per generazione puoi misurare validità del formato, presenza di evidenza, correttezza verificabile, completezza e preferenza umana. Latenza include almeno TTFT e totale; costo include token, hardware, energia e operazioni. Sicurezza include leakage, prompt injection e azioni non autorizzate.

## Esempio minimo

Su 20 risposte JSON, 18 sono sintatticamente valide e 15 corrette. La format-validity è 90%, l'accuratezza end-to-end 75%. Riportare soltanto il 90% nasconde il problema reale. Conserva anche i cinque failure case con categoria.

## Esempio realistico

Confronta due modelli locali su 40 richieste divise in italiano, estrazione, spiegazione e rifiuto. Fissa digest, prompt e parametri. Usa validatori deterministici quando possibile; due valutatori umani su una parte; misura memoria e latenza. La matrice finale pesa i criteri secondo il deployment.

## Livello AI Engineer: statistica e giudici

Una media senza dispersione può essere instabile. Usa intervalli bootstrap per metriche complesse o intervalli per proporzioni; confronti appaiati quando gli stessi esempi sono valutati da entrambi i modelli. Correggi l'uso ripetuto del test set creando un regression set versionato e un holdout meno consultato.

L'accordo tra annotatori distingue difficoltà del task da errore del modello. Definisci rubrica, esempi ancora e procedura per disaccordi. Un LLM judge è veloce ma sensibile a posizione, stile, lunghezza, self-preference e contaminazione. Calibralo contro umani, randomizza ordine e mantieni test deterministici come autorità quando disponibili.

## Matrice di decisione

| Dimensione | Esempio di misura | Possibile soglia |
| --- | --- | --- |
| Task | accuratezza appaiata | ≥ baseline + margine |
| Grounding | claim supportati | nessun claim critico senza fonte |
| Formato | schema valido | 100% dopo retry limitato |
| Prestazioni | TTFT e token/s | entro UX richiesta |
| Risorse | picco memoria | sotto budget con margine |
| Sicurezza | attacchi bloccati | zero azioni non autorizzate |

## Errori frequenti

- Scegliere esempi dopo aver visto il modello.
- Ottimizzare sul test fino a consumarlo.
- Riportare solo la media o il caso migliore.
- Usare un judge senza calibrazione.
- Confrontare costi con lunghezze di output diverse.
- Ignorare severità e distribuzione degli errori.

## Esercizi A–F

- **A:** abbina requisiti e metriche.
- **B:** aggiungi casi limite a un dataset troppo facile.
- **C:** costruisci evaluator deterministico e report errori.
- **D:** trova bias in una valutazione model-as-judge.
- **E:** confronta due modelli con protocollo preregistrato.
- **F:** realizza eval harness continuo con gate di regressione.

## Laboratorio

Esegui `python3 labs/course_lab.py evaluate` sulle fixture. Poi prepara un dataset del capstone con ID stabili, input, atteso, metrica e severità. Ogni esecuzione deve produrre manifest e report machine-readable.

## Verifica rapida

Trasforma un requisito in soglia; distingui format-validity e correttezza; spiega perché serve un confronto appaiato; elenca due bias di un LLM judge.

## Sintesi inclusiva

Valutare significa supportare una decisione. Il benchmark generale è un indizio; il test sul proprio compito, con baseline, soglie, failure case e costi, è l'evidenza. I giudici automatici aiutano ma non sostituiscono controlli indipendenti.

## Fonti e collegamenti

- [HELM](https://arxiv.org/abs/2211.09110)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [Prova pratica finale](../assessments/final-practical.md)
- Activity: `llm-activity-m14-evaluation`
