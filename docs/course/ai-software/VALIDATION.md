# Evidenze della verifica tecnica

Data: 10 settembre 2026. Ambiente di sviluppo Python, senza servizio Ollama
o sessione di coding agent usata come benchmark.

- Suite del repository: **40 test superati**. Include 9 esempi di contratto
  eseguiti su memoria e su SQLite, 6 controlli ingegneristici aggiuntivi,
  3 controlli dell'adapter con risposta simulata, i 12 test LLM preesistenti
  e la verifica dei comandi documentati.
- Il test concorrente usa due connessioni SQLite sullo stesso file temporaneo:
  una prenotazione riesce e una viene rifiutata. Il test sugli intervalli
  confronta la funzione con insiemi di minuti su un dominio finito.
- Content Pack e sei Activity validati anche con gli script canonici TheBitLab.
  Course Design trasformato nella mappa didattica dal generatore canonico.
- Metadati e copie degli asset riproducibili tramite
  `python3 scripts/scaffold_ai_software_pack.py --check`.
- Undici visuali con JavaScript sintatticamente valido. Per la nuova visuale
  verificati i sei casi 599/600/601, con e senza confronto stretto.
- PDF rigenerati: 92 pagine studente, 105 docente. Verifica strict, stream di
  ogni pagina, presenza S00-S05 e separazione della guida docente; controllo
  dei margini su tutte le pagine e ispezione delle pagine modificate.

Le prove tecniche non validano qualità di un modello, efficacia didattica,
tempi reali delle lezioni o disponibilità hardware degli studenti. Questi
risultati vanno raccolti nel rehearsal/pilot concordato. Il supplemento resta
editorialmente `draft`; questo report non equivale ad approvazione docente.
