# Diagnostica iniziale e finale

Somministrare le stesse domande prima di M00 e dopo M19. La prima prova non fa
media; il confronto misura cambiamento concettuale. Richiedere una frase di
motivazione, non solo la lettera.

1. Ollama è: A un modello; B un runtime/server; C un tokenizer; D un dataset.
2. Abbassare temperature: A aggiunge conoscenza; B rende i pesi più precisi;
   C concentra la scelta sulla distribuzione; D aumenta la RAM.
3. Un file modello da 8 GB entra sicuramente in 8 GB di RAM? Spiega.
4. Token e parola sono sempre equivalenti? Fornisci un controesempio.
5. Perché la maschera causale nasconde i token futuri?
6. Open-weight significa che dati, codice e licenza sono sempre open source?
7. RAG modifica permanentemente i pesi? Descrivi dove entra la fonte.
8. Una citazione generata prova che la fonte sostiene l'affermazione?
9. Un benchmark alto basta a scegliere un modello per appunti italiani?
10. Un tool descritto al modello viene eseguito direttamente dal modello?
11. SHA-256 permette di ricostruire un file mancante? Qual è il suo ruolo?
12. Quali informazioni devi salvare per ripetere un test Ollama?

## Chiave e punteggio

1 B; 2 C. Per 3: no, servono runtime/KV/sistema e margine. Per 4: no,
tokenizer-specifico, spazi/parti/byte/emoji. Per 5: impedisce leakage dal
futuro nell'obiettivo autoregressivo. Per 6: no, leggere ogni licenza e
disponibilità di training data/code. Per 7: no, inserisce frammenti nel
contesto. Per 8: no, verificare entailment e coordinate. Per 9: no, serve eval
locale con rischi/costi. Per 10: il software valida/autorizza/esegue. Per 11:
verifica, non ricostruzione. Per 12: tag/digest, runtime, quantizzazione,
hardware, prompt/template/options, fixture, seed e metriche.

Due punti per domanda: 1 correttezza, 1 motivazione. Totale 24. Registrare per
concetto, non usare il totale per etichettare lo studente.

