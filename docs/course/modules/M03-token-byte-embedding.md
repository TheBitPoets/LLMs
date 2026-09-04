# M03 — Token, byte ed embedding

**Domanda guida:** che cosa vede davvero un modello quando scriviamo una frase o gli diamo un file?
**Durata:** 3 ore Practitioner; 10 ore AI Engineer.
**Prerequisiti:** M02; vettori per l'estensione.

## Obiettivi osservabili

Saprai descrivere la catena testo → byte → token → ID → embedding, verificare un round trip e spiegare perché costo e context window dipendono dai token. Il livello AI Engineer implementa una tokenizzazione elementare, una lookup table di embedding e analizza vantaggi e limiti di modelli token-, byte- e character-level.

## Problema iniziale

Le parole “casa”, “cassa”, un'emoji e un frammento binario non hanno la stessa rappresentazione. Un modello non riceve direttamente significati: riceve numeri costruiti da una convenzione. Cambiare tokenizer può cambiare lunghezza, costo, segmentazione delle lingue e compatibilità con i pesi.

## Teoria Practitioner

Il testo Unicode viene serializzato in byte, spesso UTF-8. Un tokenizer raggruppa byte o caratteri in unità ricorrenti; ogni token ha un ID nel vocabolario. L'ID non esprime una distanza semantica: è un indice. La matrice di embedding associa l'ID a un vettore appreso. Dopo i layer, il modello produce logits sul vocabolario e il decoder riconverte gli ID in byte e testo.

Apri [Dal testo ai numeri](../../../visuals/token-byte-embedding-lab.html). Prova parole italiane, codice, spazi e emoji. Un token non coincide necessariamente con una parola: può essere un prefisso, uno spazio più parola, un byte o un simbolo speciale. Per questo non esiste una conversione universale da parole a token.

![Catena dal contenuto ai vettori elaborati dal modello](../../../visuals/static/rendered/token-embedding.png)

## Esempio minimo

Con un vocabolario didattico `{"ca": 4, "sa": 7, "ssa": 9}`, “casa” può diventare `[4,7]` e “cassa” `[4,9]`. Gli ID 7 e 9 non codificano una vicinanza semantica. È la matrice $E\in\mathbb{R}^{V\times d}$ a fornire i vettori: per l'ID $i$, l'embedding iniziale è la riga $E_i$.

## Esempio realistico

Devi stimare se un corpus entra nel contesto. Contare caratteri non basta. Esegui il tokenizer esatto del checkpoint, conta istruzioni, documenti, cronologia e spazio riservato all'output. Un template chat aggiunge token speciali invisibili. Se cambi famiglia di modello devi ripetere il conteggio.

## Livello AI Engineer: tokenizzazione ed embedding

Metodi subword come BPE partono da unità piccole e fondono coppie frequenti; Unigram seleziona segmentazioni probabili da un vocabolario candidato. I tokenizer byte-level coprono qualunque sequenza di byte, ma una singola entità visiva può occupare più unità. I modelli byte-level eliminano un vocabolario linguistico fisso e sono interessanti per file arbitrari, ma devono elaborare sequenze più lunghe.

Una lookup di embedding equivale a moltiplicare un vettore one-hot per $E$, ma l'indicizzazione evita il grande vettore sparso. Gli embedding contestuali prodotti dai layer non coincidono con le righe iniziali: lo stesso token assume rappresentazioni diverse in contesti diversi.

Per un file, round trip significa `decode(encode(x)) == x`. Normalizzazioni Unicode o sostituzioni di caratteri invalidi possono rompere l'uguaglianza. Per Pollicino la sequenza di byte originale è l'autorità: il percorso non deve trasformarla silenziosamente in testo.

## Confronto tra rappresentazioni

| Unità | Vantaggio | Costo o limite |
| --- | --- | --- |
| Parola | sequenza breve | vocabolario enorme, parole ignote |
| Subword | buon compromesso | segmentazione dipendente dal corpus |
| Carattere | semplice da spiegare | Unicode e sequenze più lunghe |
| Byte | copertura universale e round trip | più passi da elaborare |

## Errori frequenti

- Chiamare token ogni parola separata da spazi.
- Interpretare l'ID come valore semantico.
- Usare il tokenizer di un modello con i pesi di un altro.
- Dimenticare token speciali e chat template nel budget.
- Normalizzare un file quando serve ricostruzione esatta.

## Esercizi A–F

- **A:** segmenta manualmente una frase con un vocabolario dato.
- **B:** cambia una fusione BPE e osserva la lunghezza.
- **C:** implementa encode/decode per un tokenizer didattico.
- **D:** trova perché un round trip Unicode non coincide.
- **E:** misura token per italiano, inglese e codice su due tokenizer.
- **F:** progetta una rappresentazione byte-level con test esaustivi.

## Laboratorio

Esegui `python3 labs/course_lab.py bytes` e prova file con zero byte, UTF-8 multibyte e dati non testuali. Se disponi di un tokenizer reale, registra nome e revisione e confronta rapporto byte/token su tre domini.

## Verifica rapida

Disegna la catena completa; spiega ID contro embedding; mostra un caso in cui token e parola non coincidono; indica perché Pollicino preferisce preservare i byte.

## Sintesi inclusiva

Il modello riceve indici, non parole. Il tokenizer stabilisce come il contenuto diventa una sequenza; l'embedding trasforma gli indici in vettori appresi. Formato, costi e limiti dipendono da questa scelta. Nei file lossless, nessun passaggio può perdere informazione.

## Fonti e collegamenti

- [SentencePiece](https://arxiv.org/abs/1808.06226)
- [ByT5](https://arxiv.org/abs/2105.13626)
- [Visuale token/byte/embedding](../../../visuals/token-byte-embedding-lab.html)
- Activity: `llm-activity-m03-token-inspector`
