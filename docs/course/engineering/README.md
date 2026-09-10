# Laboratori applicativi e implementazioni AI Engineer

Questa sezione completa le implementazioni dei moduli M04-M19. Non aggiunge
automaticamente ore alle 68 del percorso scolastico: il docente usa gli esempi
Practitioner nei moduli corrispondenti; lo studio integrale AI Engineer è un
percorso personale aggiuntivo di circa 32 ore, da adattare ai prerequisiti.

Il codice di riferimento è originale e si trova in
[labs/engineering](../../../labs/engineering/README.md). Gli esempi svolti sono
materiale di studio; le consegne richiedono nuove prove e modifiche. Le soluzioni
di correzione delle Activity rimangono negli asset riservati al docente.

| Capitolo | Collegamento | Studio avanzato stimato |
| --- | --- | --- |
| [E00 Matematica operativa](E00-matematica.md) | M02-M05 | 4 ore |
| [E01 Chat affidabile](E01-chat.md) | M11/M13 | 3 ore |
| [E02 RAG e valutazione](E02-rag.md) | M03/M14/M15 | 4 ore |
| [E03 Agenti e MCP](E03-agenti-mcp.md) | M16 | 4 ore |
| [E04 Transformer da zero](E04-training.md) | M04/M05/M07/M19 | 5 ore |
| [E05 LoRA e regressioni](E05-lora.md) | M17 | 3 ore |
| [E06 Inferenza e kernel](E06-inferenza.md) | M10/M18 | 5 ore |
| [E07 Codec neurale](E07-codec.md) | M19/Pollicino | 4 ore |

Prerequisiti Practitioner: funzioni, liste, file e JSON in Python. Per AI
Engineer servono anche array, indici, funzioni composte e lettura di grafici;
E00 costruisce il ponte verso le formule. Usare Python 3.12 per ripetere
l'ambiente verificato. Le applicazioni usano la libreria standard; i capitoli
neurali richiedono PyTorch 2.8.0. I grafici pubblicati sono già disponibili.

Tre tipi di evidenza sono distinti: test con provider simulato, protocollo MCP
eseguito fra processi reali, esperimenti neurali misurati su CPU. Il servizio
Ollama reale e il profilo Mac scolastico hanno un proprio rehearsal ancora da
eseguire. Un mock non misura la qualità di un modello scaricato.

Per ogni consegna usare il [report di laboratorio](REPORT-template.md),
conservando anche gli insuccessi. Per passare dal codice di esempio a un
prodotto, proseguire con [S00-S05: sviluppo software con AI](../ai-software/README.md).
