# Engineering lab: applicazioni e piccolo modello locale

Esempi originali eseguibili del corso. Dalla root del repository, Python 3.12.
Le applicazioni usano la libreria standard; training, adapter, inferenza e
codec neurale richiedono PyTorch. I documenti sono sintetici e i checkpoint
sono i pesi minuscoli addestrati qui, non modelli Manning o di terzi.

## Percorso senza servizio LLM

```bash
python3 -m pip install -r labs/engineering/requirements-cpu.txt
python3 -m labs.engineering.run mcp-check --output output/engineering/mcp-report.json
python3 -m labs.engineering.train
python3 -m labs.engineering.generate --output output/engineering/generation-report.json
python3 -m labs.engineering.inference
python3 -m labs.engineering.codec_experiment
python3 -m unittest discover -s tests -v
```

Usare `--output` con una directory nuova per conservare un training precedente.
I tempi CPU non sono trasferibili al Mac della classe. Gli esperimenti
versionati in `output/engineering` contengono hash, configurazione e limiti.
Per riprodurre esattamente le fixture: `python3 -m labs.engineering.make_corpus`.

## Applicazioni con Ollama locale

Avviare il servizio e installare un modello compatibile con l'hardware, poi:

```bash
python3 -m labs.engineering.run chat --model qwen3.5:0.8b --interactive
python3 -m labs.engineering.run rag --model qwen3.5:0.8b --embedding-model all-minilm:22m
python3 -m labs.engineering.run rag-eval --model qwen3.5:0.8b --embedding-model all-minilm:22m
python3 -m labs.engineering.run agent --model qwen3.5:0.8b --mcp
```

I tag sono baseline di collegamento, da scaricare prima dell'uso e valutare;
non garantiscono qualità italiana, output JSON o tool calling. Aggiungere
`--output output/rehearsal/nome.json` per conservare una prova non sensibile.
Per RAG installare anche il modello embedding. Se il modello non supporta
il contratto richiesto, conservare il fallimento e confrontare un altro tag.

## Errori e limiti dichiarati

- Chat: risposta parziale non confermata; cancel fra letture, timeout 30 s.
- RAG: citazioni verificate come provenienza letterale; entailment da valutare.
- Agent: un solo tool read-only, allowlist e budget; nessun invio o scrittura.
- MCP: sottoinsieme stdio 2025-06-18, non SDK o server di produzione completo.
- TinyLM: byte, 84.288 parametri, corpus a template, nessuna competenza generale.
- LoRA: sola head, base float32; regressione base misurata e pubblicata.
- Kernel: Python/PyTorch CPU; tiled più lento della reference in questa prova.
- Codec: tutti i byte e vuoto; checksum non autenticazione; numerica neurale
  identica richiesta, nessuna garanzia portabile fra dispositivi.

Le spiegazioni e consegne sono in `docs/course/engineering/E00-E07`.
I test di trasporto usano HTTP simulato; il test MCP avvia processi reali.
La verifica con modelli Ollama e hardware della scuola resta nel rehearsal
rinviato, separata dagli esperimenti CPU già eseguiti.
