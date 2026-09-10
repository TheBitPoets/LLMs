# Activity M16 — Tool use, agenti e MCP

## Obiettivo

Applica la dispensa M16 e produci un risultato verificabile.

## Consegna specifica

Aggiungi una terza stanza al tool E03 aggiornando schema, policy e test; verifica argomenti extra e budget. Progetta separatamente la conferma richiesta da un futuro tool con effetti.

## Procedura comune

1. Leggi problema iniziale, teoria Practitioner ed esempio della dispensa.
2. Completa il livello A–D assegnato; per E–F realizza il prodotto richiesto.
3. Registra modello/revisione, runtime/versione, parametri, hardware, input e risultato.
4. Distingui ciò che hai misurato da ciò che stai inferendo.
5. Consegna artefatto, relazione breve e un limite osservato.

## Evidenza attesa

Schema, allowlist, least privilege, conferma, idempotenza e audit.

## Autoverifica

- [ ] Un compagno può ripetere il lavoro con le informazioni fornite.
- [ ] Non ho inserito dati personali o segreti nei prompt.
- [ ] Ho confrontato il risultato con una baseline.
- [ ] Ho indicato almeno un caso in cui la soluzione può fallire.

## Esempi eseguibili distribuiti

Gli asset `example` contengono codice originale e test pubblici. Sono esempi svolti da studiare, non la consegna completata. Esegui `python3 -m unittest discover -s tests -v` dalla root dello scaffold.

Prima dei test neurali installa `python3 -m pip install -r labs/engineering/requirements-cpu.txt`. Consulta il capitolo E03-agenti-mcp.md nella Course Board. Le prove Ollama richiedono servizio e modelli installati; quelle CPU usano fixture incluse. I report vanno in una directory nuova e devono distinguere simulazione e misure.
