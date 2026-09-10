# Evidenze CPU del corso - 10 settembre 2026

Questi file provengono da esecuzioni reali su CPU x86_64, Python 3.12.14,
PyTorch 2.8.0+cpu, un thread e seed 7 per gli esperimenti neurali.
I dati sono sintetici e i checkpoint sono originali del corso.

- `training-report.json`: training, validation, test, baseline, LoRA e hash.
- `tiny-byte-lm.pt`: 84.288 parametri, addestrati da inizializzazione casuale.
- `head-lora.pt`: adapter sulla sola head, associato all'hash del base.
- `generation-report.json`, `adapter-generation.json`: byte generati e
  anteprima UTF-8; i risultati imperfetti sono conservati integralmente.
- `inference-report.json`: equivalenza, cache e ripetizioni del benchmark CPU.
- `codec-report.json`: otto round trip, gzip e costo completo del modello.
- `mcp-report.json`: handshake, discovery e tool su subprocess reale, senza LLM.

Riproduzione dalla root: `python3 -m labs.engineering.train`, poi i moduli
`generate`, `inference`, `codec_experiment` e `run mcp-check` come descritto
nei capitoli E01-E07. Scegliere output nuovi per confrontare configurazioni.
I tempi cambiano con il carico della macchina; gli hash legano gli artefatti,
non certificano prestazioni su un altro dispositivo.

Non sono presenti misure live di modelli Ollama, cloud, coding agent o radio.
Il test del modello è interno a una distribuzione di frasi a template;
la generazione adattata può essere incoerente anche se la loss migliora.
Nessuna evidenza di competenza generale o superiorità rispetto a gzip.
