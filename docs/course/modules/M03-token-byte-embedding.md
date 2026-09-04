# M03 - Token, byte ed embedding

**Domanda guida:** come diventa numero un testo?  
**Durata:** 3 ore Practitioner; 10 ore AI Engineer.  
**Prerequisiti:** M02; vettori solo per l'estensione.

## Obiettivi osservabili

Distinguere carattere Unicode, byte UTF-8, token, token ID ed embedding;
misurare la tokenizzazione invece di stimarla “a parole”; spiegare perché
tokenizer e pesi formano un contratto. L'AI Engineer implementa un tokenizer
didattico e un embedding lookup.

## Lezione intuitiva

Una frase attraversa più alfabeti. Unicode nomina i caratteri; UTF-8 li
serializza in byte; il tokenizer raggruppa sequenze nel proprio vocabolario;
gli ID indicizzano righe di una matrice appresa. L'ID 42 non è “più grande” nel
significato dell'ID 10. È un indirizzo.

Usare [Dal testo ai numeri](../../../visuals/token-byte-embedding-lab.html).
Confrontare “caffe”, “caffè”, spazi, emoji e una parola italiana lunga. Il
tokenizer didattico della visuale non finge di essere BPE: serve a vedere quali
livelli non vanno confusi.

## Matematica e implementazione

Con matrice `E∈R^(V×d)`, l'ID `t` seleziona `e_t=E[t]`. Per un batch di shape
`[B,T]`, il risultato ha shape `[B,T,d]`. L'operazione equivale a moltiplicare
un one-hot per `E`, ma il lookup evita di materializzare il one-hot.

L'AI Engineer implementa byte tokenizer (vocabolario 256), BPE minimale con
merge appresi solo sul train e round trip `decode(encode(x))==x`. Confronta
fertility token/carattere tra italiano, inglese, codice ed emoji.

## Laboratorio e verifica

Artefatto CSV: testo, caratteri, byte, token, ratio e anomalie per due
tokenizer reali autorizzati. Test negativo: testo con caratteri combinanti e
byte non validi gestiti esplicitamente. Verifica 10 punti: livelli 4, misura 2,
round trip 2, limite/errore 2. Fonte: model card dei tokenizer scelti e
[Neural Probabilistic Language Model](https://www.jmlr.org/papers/v3/bengio03a.html).

