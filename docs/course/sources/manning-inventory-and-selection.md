# Inventario e selezione Manning per il corso LLM

Snapshot verificato sulla libreria e sul catalogo Manning il **4 settembre
2026**. Prezzi, completezza MEAP e date sono dati correnti, non contenuto
stabile del corso.

Questo documento non autorizza acquisti automatici. Serve a usare gli undici
crediti annuali rimasti dopo l'acquisizione di *Build Applications with Local
AI Models on a Mac* senza comprare duplicati concettuali.

## Prodotti presenti nella libreria

| Titolo | Pertinenza | Uso previsto |
| --- | --- | --- |
| Build Applications with Local AI Models on a Mac | Diretta | Percorso introduttivo Ollama, Python, Streamlit, voce e applicazione locale. |
| LLMs in Production | Diretta | Deployment, sistemi e pratiche operative. |
| LLM Evaluation and Alignment, The Foundational Ideas | Diretta | M08 e M14: valutazione, allineamento e limiti. |
| LLM Customization and Fine-Tuning | Diretta | M17: adattamento e fine-tuning. |
| Knowledge Graphs and LLMs in Action | Diretta | M15: conoscenza strutturata e applicazioni ibride. |
| Essential GraphRAG | Diretta | M15: retrieval su grafi e valutazione. |
| Domain-Specific Small Language Models | Diretta | M10 e M17: piccoli modelli specializzati. |
| Designing AI Systems | Diretta | M01, M13, M14 e progetto finale. |
| Deep Learning with PyTorch, Second Edition | Fondamentale | M04–M07 e implementazioni AI Engineer. |
| Deep Learning with PyTorch | Superata dalla seconda edizione | Consultazione storica; non fonte primaria del corso. |
| Build an AI Agent (From Scratch) | Diretta | M16: agent loop e implementazione senza dipendenza totale da framework. |
| Test Yourself on Build a Large Language Model (From Scratch) | Complementare | Diagnostica e autovalutazione. |
| Build a Large Language Model (From Scratch) | Fondamentale | M02–M08 e M19: piccolo GPT implementato progressivamente. |
| Build Your Own Robot | Progetto adiacente | Integrazione eventuale con Romeo; non fonte centrale LLM. |
| Publishing Python Packages | Infrastruttura | Packaging dei laboratori e dei componenti riusabili. |
| Kubernetes in Action, Second Edition | Infrastruttura | Serving/distribuzione avanzata, non prerequisito Practitioner. |
| Kubernetes in Action | Superata dalla seconda edizione | Consultazione storica. |
| Event Streams in Action | Infrastruttura | Eventi e osservabilità per applicazioni/agent workflow. |
| Exploring Python Basics | Prerequisito | Recupero Python per studenti. |
| Practical Recommender Systems | Adiacente | Sistemi di raccomandazione; fuori dal tronco LLM v1. |
| Machine Learning with TensorFlow | Adiacente/storica | Fondamenti ML, non fonte tecnica principale della v1. |

## Undici acquisizioni raccomandate

L'ordine bilancia valore, copertura mancante, maturità e rischio di
sovrapposizione. Un titolo MEAP acquistato resta utile perché include gli
aggiornamenti successivi, ma la completezza corrente viene comunque registrata.

| Priorità | Titolo | Stato osservato | Lacuna coperta | Perché entra |
| ---: | --- | --- | --- | --- |
| 1 | [Build a Reasoning Model (From Scratch)](https://www.manning.com/books/build-a-reasoning-model-from-scratch) | Pubblicato giugno 2026, 440 pp. | Reasoning, inference-time scaling, verifier, GRPO, distillazione | È la continuazione naturale del libro LLM da zero già posseduto e collega metodi, costi e failure mode. |
| 2 | [Quantization and Fast Inference](https://www.manning.com/books/quantization-and-fast-inference) | MEAP 100%, aggiornato agosto 2026 | PTQ, QAT, NF4/FP4, activation outlier, KV cache | Copre direttamente scelta del modello locale, memoria e ottimizzazione, centrali per entrambi i livelli. |
| 3 | [Reinforcement Learning from Human Feedback](https://www.manning.com/books/reinforcement-learning-from-human-feedback) | Pubblicato luglio 2026, 312 pp. | SFT, reward model, PPO, DPO, KL, preference e synthetic data | È la fonte più mirata per capire il post-training moderno senza confonderlo con RL generico. |
| 4 | [Deep Learning with Python, Third Edition](https://www.manning.com/books/deep-learning-with-python-third-edition) | Pubblicato settembre 2025, 648 pp., colore | Fondamenti intuitivi, Keras/PyTorch/JAX, Transformer e GPT | Fornisce un ponte visuale e pratico da zero al generative AI, utile anche per progettare le spiegazioni Practitioner. |
| 5 | [Math and Architectures of Deep Learning](https://www.manning.com/books/math-and-architectures-of-deep-learning) | Pubblicato aprile 2024, 552 pp. | Algebra lineare, calcolo vettoriale, statistica e architetture | È la dorsale rigorosa della matematica AI Engineer, da trasformare in spiegazioni intuitive parallele. |
| 6 | [Context Engineering](https://www.manning.com/books/context-engineering) | MEAP 100%, aggiornato agosto 2026 | Prompt, RAG, memoria, skill, MCP, harness e osservabilità | Unifica ciò che entra nella context window e impedisce un corso fermo al solo prompt engineering. |
| 7 | [Building Reliable AI Systems](https://www.manning.com/books/building-reliable-ai-systems) | Pubblicato agosto 2026, 368 pp. | Grounding, safe agency, graceful failure, eval e operation | Porta il corso dall'applicazione dimostrativa al sistema misurabile, sicuro e mantenibile. |
| 8 | [Rearchitecting LLMs](https://www.manning.com/books/rearchitecting-llms) | MEAP 75%, aggiornato agosto 2026 | Pruning, distillazione e modifica strutturale di Llama/Gemma/Qwen | Mostra come ottenere SLM locali più efficienti e collega paper recenti a esperimenti reali. |
| 9 | [CUDA for LLMs](https://www.manning.com/books/cuda-for-llms) | MEAP 100%, aggiornato agosto 2026 | CUDA, profiling, estensioni PyTorch, FlashAttention | È la fonte principale per il requisito di costruire e capire kernel d'inferenza su NVIDIA. |
| 10 | [GPU Programming with Triton](https://www.manning.com/books/gpu-programming-with-triton) | MEAP 36%, iniziato agosto 2026 | Kernel Python/Triton, fusion, tiling, sparse attention | Offre il percorso più accessibile da PyTorch al kernel; complementare a CUDA, ma ancora giovane. |
| 11 | [AI Agents in Action, Second Edition](https://www.manning.com/books/ai-agents-in-action-second-edition) | Pubblicato giugno 2026, 392 pp. | MCP, A2A, tool use, memoria, reasoning, eval e deployment | Aggiunge una vista production-oriented e aggiornata senza sostituire l'implementazione from scratch già posseduta. |

## Titoli osservati ma non inclusi nei primi undici

| Titolo | Decisione corrente |
| --- | --- |
| Agent Design Patterns | Molto promettente e visuale, ma al 23% e sovrapposto al libro agentico già posseduto; tenere sotto osservazione. |
| Build a Multi-Agent System (From Scratch) | Buono per infrastruttura, MCP e A2A; secondo candidato se si rinvia Triton o se il corso multi-agent diventa prioritario. |
| Grokking AI Applications | Utile per il livello intuitivo, ma il corpus posseduto e Deep Learning with Python 3e coprono meglio la progressione tecnica. |
| Understanding AI | Ampia introduzione; valore marginale inferiore rispetto alle lacune tecniche individuate. |
| Grokking Bayes | Ottima fonte visuale per probabilità; da valutare per un futuro percorso matematico generale, non indispensabile alla v1 LLM. |

## Regola prima di spendere i crediti

Prima dell'acquisizione definitiva:

1. verificare che il titolo non sia già presente con nome o edizione diversa;
2. controllare l'indice completo e almeno un capitolo campione;
3. assegnare capitoli precisi ai moduli del corso;
4. preferire una lacuna reale a un titolo nuovo ma sovrapposto;
5. registrare data, versione MEAP e motivo della scelta;
6. non considerare l'accesso in abbonamento equivalente al possesso permanente del PDF.

## Possibile sostituzione prudenziale

Poiché *GPU Programming with Triton* è soltanto al 36%, la scelta prudente è
tenere l'undicesimo credito non impegnato finché non sono disponibili più
capitoli. Se il credito deve essere usato subito, il libro resta una scelta
coerente con il requisito kernel. Se invece serve materiale completo adesso,
lo sostituisce *Build a Multi-Agent System (From Scratch)*, osservato al 77%.
