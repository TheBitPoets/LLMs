# M16 - Tool use, agenti e MCP

**Domanda guida:** quando un modello può agire e come lo limitiamo?  
**Durata:** 3 ore Practitioner; 12 ore AI Engineer.  
**Prerequisiti:** M12–M15.

## Obiettivi osservabili

Distinguere modello, tool, agent loop e orchestratore; applicare schema,
allowlist, permessi minimi, budget, stop e approvazione. L'AI Engineer costruisce
un tool/MCP server minimale con trace ed eval.

## Lezione intuitiva

Un modello propone testo strutturato; il software valida e decide se chiamare
uno strumento. L'osservazione ritorna nel contesto e il ciclo continua. Il
modello non riceve autorità implicita: ogni tool espone una capacità precisa.
MCP standardizza come descrivere e invocare risorse/strumenti; non garantisce
che input, tool o modello siano sicuri.

## Laboratorio

Agente locale con un solo tool read-only: calcolatrice o ricerca in un corpus
del corso. Schema chiuso, massimo tre chiamate, timeout e log. Il docente abilita
una falsa istruzione dentro un documento: l'agente deve trattarla come dato.
Baseline: chiamata diretta del tool senza LLM. Nessun invio, acquisto o modifica
esterna nel percorso scolastico.

## AI Engineer

State machine esplicita: `PLAN→VALIDATE→APPROVE?→EXECUTE→OBSERVE→STOP`.
Capability tokens o policy per-tool, idempotency key, output sanitization e
separazione dei log. Eval su task success, chiamate superflue, violazioni,
loop, latenza e costo.

## Verifica

Architettura 2, schema 2, least privilege 2, injection test 2, stop/evidenze 2.
Fonti: specifica [Model Context Protocol](https://modelcontextprotocol.io/) e
paper ReAct/Toolformer indicati nella timeline.

