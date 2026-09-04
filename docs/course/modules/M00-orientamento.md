# M00 - Orientamento e baseline

**Domanda guida:** che cosa vogliamo davvero saper fare?  
**Durata:** 2 ore Practitioner; 4 ore AI Engineer.  
**Prerequisiti:** uso elementare di file, browser e terminale solo per l'estensione.

## Obiettivi osservabili

Il Practitioner distingue capacità dimostrata, aspettativa e slogan; descrive
un proprio caso d'uso con input, output, rischio e metrica; registra il profilo
hardware senza pubblicare dati personali. L'AI Engineer aggiunge versioni,
seed, dipendenze e criteri di riproducibilità.

## Lezione intuitiva

Un LLM non è “un'intelligenza in una scatola”. È un componente che riceve un
contesto e calcola una distribuzione sul prossimo token. Prodotto, modello,
runtime, prompt, strumenti e dati esterni determinano insieme ciò che vediamo.
Per questo il corso parte da una domanda concreta: *quale decisione prenderemo
con l'output e quale errore sarebbe più costoso?*

Esempio: “riassumere gli appunti” è troppo vago. Una specifica verificabile è:
“da appunti italiani di 500–1.500 parole, produrre cinque punti che non
aggiungano nomi, date o numeri; ogni punto deve essere rintracciabile nel testo”.

## Attività e laboratorio

1. Compilare la scheda `caso-uso.md`: utente, dati, risultato, vincoli, errori.
2. Eseguire la diagnostica iniziale senza voto.
3. Registrare CPU, memoria e sistema operativo; GPU solo se nota.
4. Scrivere una previsione: quale modello/taglia potrebbe funzionare e perché.

Artefatti: scheda caso d'uso, baseline concettuale e hardware profile. Test
negativo: una descrizione che usa solo “potente”, “intelligente” o “migliore”
senza metrica non supera il gate.

## Estensione AI Engineer

Creare un evidence manifest con commit, versione Python, runtime, timestamp,
hardware e hash delle fixture. Definire una metrica primaria e due guardrail.
Separare variabili controllate, indipendenti e osservate.

## Verifica e criteri

- 2 punti: caso d'uso e destinatario specifici;
- 2: rischio principale e test negativo;
- 2: metrica calcolabile;
- 2: profilo hardware sufficiente a ripetere la prova;
- 2: distinzione corretta tra osservato e atteso.

Soglia: 6/10, ma i punti su rischio e distinzione delle evidenze sono
obbligatori. Fonte: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

