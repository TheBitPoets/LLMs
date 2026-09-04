# M13 - Applicazioni conversazionali

**Domanda guida:** che cosa deve aggiungere il software attorno al modello?  
**Durata:** 4 ore Practitioner; 10 ore AI Engineer.  
**Prerequisiti:** M11–M12; Python di base.

## Obiettivi osservabili

Costruire una chat locale con streaming, history limitata, errori visibili e
configurazione registrata; distinguere memoria dell'app e context window.
L'AI Engineer definisce contratti, observability e threat model.

## Lezione intuitiva

Una chat non è solo una casella di testo. L'app decide quali messaggi reinviare,
come applicare template, quanto contesto conservare, cosa loggare, come fermare
la generazione e come gestire un servizio indisponibile. Se un messaggio non
viene reinserito nel contesto o recuperato da storage, il modello non lo ricorda.

Il progetto `TheBitPoets/Llma_Chatbot` viene usato come anatomia, non come prova
automatica di readiness. Prima si crea una versione minima API/CLI; poi UI.

## Laboratorio

Chat Python con adapter Ollama, stream incrementale, limite token/turni,
comando reset, timeout e salvataggio JSONL opzionale esplicito. Artefatti:
transcript redatto, config ed error report. Baseline: singola chiamata senza
history. Test: server spento, disconnect a metà stream, prompt vuoto, contesto
oltre budget e output non valido.

## AI Engineer

Definire interfaccia `ModelClient`, envelope request/response, cancellation e
idempotenza dove applicabile. Tracciare TTFT, durata, token e risultato senza
salvare contenuto sensibile per default. Threat model su XSS/Markdown, prompt
injection, log e file upload.

## Verifica

Funzione 3, stato 2, errori 2, evidenze 2, privacy 1. Nessuna credenziale cloud
è necessaria per il percorso base.

