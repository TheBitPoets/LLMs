# E03 - Tool calling e MCP osservabili

## Obiettivi e intuizione Practitioner

Un assistente può compilare una richiesta per la segreteria; la segreteria
decide se eseguirla secondo regole precise. Nel nostro programma il modello
propone una chiamata, mentre il codice controlla nome e argomenti. Una frase
convincente non conferisce permessi.

Il laboratorio cerca informazioni su due laboratori scolastici fittizi.
L'unico tool è `lookup_room`, di sola lettura. Il ciclo
[agent.py](../../../labs/engineering/agent.py) funziona sia con una funzione
Python sia con un processo MCP separato. Imparerai a distinguere il modello,
la policy dell'applicazione e il protocollo che trasporta la richiesta.

## Prima il protocollo, poi il modello

```bash
python3 -m labs.engineering.run mcp-check \
  --output output/rehearsal/mcp.json
python3 -m labs.engineering.run agent \
  --model qwen3.5:0.8b --mcp \
  --prompt 'Usa lookup_room per sapere i posti di LAB-A.' \
  --output output/rehearsal/agent.json
```

Il primo comando non usa un LLM: avvia un vero subprocess, inizializza MCP,
scopre il tool e lo chiama. Il secondo richiede Ollama e un tag capace di
tool calling. Il tag piccolo è una prova di compatibilità: se non effettua
la chiamata, il report deve mostrarlo. Prova poi un modello compatibile più
capace scelto con il budget hardware; non inventare una traccia di tool a mano.

## La macchina a stati AI Engineer

Il ciclo inizia con messaggio di sistema, domanda e schema del tool. Ricevuta
la risposta, controlla tutte le chiamate del batch prima di eseguirne una.
Accetta solo il nome previsto e un oggetto con l'unica chiave `room`, il cui
valore deve essere `LAB-A` o `LAB-B`. Un nome sconosciuto o un argomento extra
provoca un errore esplicito. Lo schema inviato al modello non sostituisce
questi controlli eseguiti dal programma.

Il risultato viene inserito nella storia con ruolo `tool` e nome del tool,
come previsto dal contratto Ollama usato. Il modello può quindi formulare
la risposta o proporre un nuovo passo. Il programma limita il ciclo a quattro
passi e sei chiamate; raggiungere il budget è un errore, non un successo
silenzioso. Le chiamate identiche sono memoizzate nel singolo ciclo. Questa
scelta è valida qui perché i dati sono fissi e il tool è read-only; per dati
mutabili servirebbe una policy di freschezza.

Una risposta finale senza tool call può essere prodotta dal modello, ma non
prova che abbia consultato il laboratorio. Per il criterio «dato ottenuto dal
tool» il docente controlla la traccia, non soltanto il numero 24 nel testo.

## Che cosa implementa MCP

[mcp.py](../../../labs/engineering/mcp.py) implementa un sottoinsieme educativo
della versione **2025-06-18** su stdio. Il client invia `initialize`, controlla
la versione e invia `notifications/initialized`; poi usa `tools/list` e
`tools/call`. Le richieste hanno ID JSON-RPC e le risposte devono riportare
lo stesso ID. Le notifiche non ricevono risposta. Gli errori distinguono JSON
non valido, metodo sconosciuto e parametri non validi.

Il server scrive solo messaggi di protocollo su stdout, uno per riga: inserire
un `print` di debug in quel flusso rompe il trasporto. Esistono limiti di riga
e timeout del client. La chiusura del contesto termina il processo figlio.
La fixture non implementa HTTP, autenticazione, sessioni distribuite o ogni
capacità dello standard. Per un servizio reale usare un SDK mantenuto e
verificarne la versione; il laboratorio serve a rendere visibile il contratto.

L'indicazione `readOnlyHint` descrive il tool ai client. Non è un controllo
di sicurezza: la restrizione effettiva deriva dal codice e dai permessi.

## Consegna e valutazione

Practitioner: disegna il confine fra proposta del modello e decisione del
programma; confronta una risposta ottenuta dal tool con una risposta senza
chiamate. AI Engineer: aggiungi una terza stanza aggiornando schema, policy,
fixture e test; prova argomenti extra, ID errato, chiamata prima dell'handshake
e loop oltre budget. Non aggiungere operazioni con effetti esterni a questo
esercizio. Il percorso PrenotaLab insegna separatamente proposta, conferma
umana e transazione.

I test automatici usano un modello simulato per rendere riproducibili gli
errori e un subprocess MCP reale per verificare il trasporto. La qualità
della selezione tool con un LLM locale resta una misura del rehearsal.

Fonti primarie: [MCP lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle),
[MCP tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
e [Ollama Chat API](https://docs.ollama.com/api/chat).
