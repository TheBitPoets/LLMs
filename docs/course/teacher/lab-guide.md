# Guida docente ai laboratori

## Preparazione comune

1. clonare il commit da provare e registrarlo;
2. eseguire `python3 -m unittest discover -s tests -v`;
3. distribuire una cartella output vuota per gruppo;
4. assegnare driver, navigator e responsabile evidenze a rotazione;
5. mostrare consegna e metrica, non l'output atteso.

## Failure injection e criteri

| Lab | Iniezione docente | Evidenza corretta |
| --- | --- | --- |
| L00 | Rimuovere un campo dal manifest copiato | Lo studente rifiuta il confronto incompleto. |
| L01 | Logits 1000/999/998 | Probabilità finite, somma circa 1. |
| L02 | `è`, emoji e stringa vuota | Caratteri ≠ byte; round trip esplicito. |
| L03 | Learning rate 1 | Loss instabile/divergente riconosciuta, non nascosta. |
| L04 | Modificare il Value futuro | Output precedente invariato con mask causale. |
| L05 | 14B 8-bit, 64k, 16 GB | Configurazione rifiutata senza margine. |
| L06 | Stesso seed due volte | Conteggi identici nel runner, senza generalizzare ad altri runtime. |
| L07 | Numero alterato | Failure case visibile nella categoria corretta. |
| L08 | Query “xylophone zirconium” | Astensione per overlap nullo. |
| L09 | `__import__('os')` | Nessuna esecuzione; AST non permesso. |
| L10 | Bit modificato | Hash/round trip fallisce o output cambia. |
| L11 | Servizio spento/tag inesistente | Errore controllato, nessun report inventato. |

## Evidenze minime

Ogni gruppo consegna comando, stdout JSON, breve interpretazione, baseline,
test negativo, configurazione e limite. Per Ollama aggiungere digest/tag,
runtime, quantizzazione, hardware, prompt, options, token count e tempi.

## Correzione

Usare 0–2 punti per: correttezza, riproducibilità, baseline, test negativo,
interpretazione/limite. Un output numericamente corretto senza comando o
configurazione non supera 6/10.

