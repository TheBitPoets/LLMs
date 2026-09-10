# Guida docente M09 — Pesi, formati e licenze

Riservato al docente.

## M09 - Artefatto, formato e licenza

Una scheda completa nomina repository e revisione, tokenizer/template,
quantizzazione, runtime, licenza e digest scaricato. «GGUF» indica un formato,
non un unico livello di precisione o una licenza. Safetensors contiene tensori
con metadati; una quantizzazione specifica richiede supporto del runtime.
Un file FP8 e uno Q4 non sono intercambiabili solo perché hanno lo stesso nome
di famiglia. Correggere con un caso negativo: modello disponibile come pesi,
ma runtime della classe privo dell'architettura necessaria. La scelta deve
essere rifiutata o accompagnata da un piano verificato di conversione.
Il catalogo collega fonti ufficiali; non sostituisce la verifica della licenza
del singolo artefatto al momento del download.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
