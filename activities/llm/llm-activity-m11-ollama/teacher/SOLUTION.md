# Guida docente M11 — Ollama e inferenza locale

Riservato al docente.

## M11 - Runtime locale

La prova completa richiede servizio Ollama attivo, modello presente e una
richiesta valida. E01 salva versione e inventario; lo studente deve controllare
che la voce del modello contenga il digest effettivo. Un tag non trovato o
un servizio spento devono produrre diagnosi e codice d'errore, non una risposta
inventata. I test HTTP simulati verificano il client ma non certificano
compatibilità del modello o velocità del runtime. Per il recupero avviare il
servizio o installare il tag scelto, poi ripetere lo stesso comando.
Una richiesta a loopback non prova che qualunque modello del catalogo sia
locale: verificare origine e artefatto, evitando tag cloud per la prova offline.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
