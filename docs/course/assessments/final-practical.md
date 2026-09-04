# Prova pratica finale Practitioner

**Tempo:** 3 ore più presentazione. **Materiali:** repository, documentazione
offline e modello locale già autorizzato.

## Consegna

Ricevi 20 brevi appunti sintetici. Devi costruire una pipeline locale che
produca tre punti JSON, ciascuno con `testo` e `source_id`, oppure si astenga.

1. seleziona un modello/tag motivando licenza, memoria, italiano e latenza;
2. crea una baseline senza LLM;
3. definisci prompt/schema e parametri;
4. esegui dataset normale, limite e ostile;
5. misura valid JSON, source accuracy, factual errors e tempi;
6. analizza tre errori e decidi se il sistema supera il gate;
7. consegna evidence manifest e data-flow.

## Rubrica /100

| Dimensione | Punti |
| --- | ---: |
| Selezione e manifest | 15 |
| Baseline e disegno eval | 15 |
| Applicazione e gestione errori | 20 |
| Metriche e failure analysis | 20 |
| Privacy, licenza e prompt injection | 15 |
| Spiegazione visuale e difesa | 15 |

Soglia 60. Sicurezza/provenienza almeno 8/15 e nessun dato personale. Bonus
entro 5 punti, senza superare 100, per confronto rigoroso con secondo modello.

## Variante AI Engineer

Aggiungere paired bootstrap, retrieval eval, adapter o kernel profilato;
riprodurre almeno un'idea ★ della timeline; documentare ablation, costi e
regressioni. La sola complessità del codice non assegna punti.

