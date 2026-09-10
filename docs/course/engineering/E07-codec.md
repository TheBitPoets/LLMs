# E07 - Dal predittore alla ricostruzione esatta di un file

## Obiettivi e intuizione Practitioner

Un modello che «ricorda più o meno» un testo non è un compressore lossless.
Encoder e decoder devono ricostruire gli stessi byte, anche se rappresentano
un'immagine, zeri o dati senza struttura. Il modello suggerisce quanto sono
probabili i byte; il codificatore trasforma quelle probabilità in bit.

Il nuovo [byte_codec.py](../../../labs/engineering/byte_codec.py) estende
il precedente esempio A/B a tutti i 256 byte, incluso il file vuoto. Usa un
predittore statistico adattivo oppure il Transformer di E04. È un laboratorio
utile a Pollicino, ma non è un'integrazione nel repository PollicinoNet né una
prova di trasmissione radio.

## Intervalli e frequenze AI Engineer

Per un intervallo intero inclusivo $[l,h]$, ampiezza $R=h-l+1$, cumulata
$C$ e totale $F$, il byte $b$ seleziona

$$h'=l+\lfloor RC_{b+1}/F\rfloor-1,
\qquad l'=l+\lfloor RC_b/F\rfloor.$$

Entrambe le formule usano il vecchio $l$. Per due simboli A/B con frequenze
3 e 1 e intervallo 0..15, A sceglie 0..11, B sceglie 12..15. Il programma
usa 32 bit e rinormalizzazione E1/E2/E3: emette bit comuni o rinvia quelli
ambigui finché l'intervallo non consente una decisione. Il decoder esegue le
stesse divisioni intere, non campiona dalla distribuzione.

Il predittore adattivo parte con frequenza uno per ogni byte, incrementa il
byte osservato e dimezza i conteggi con arrotondamento quando il totale
raggiunge 16.384. Il predittore neurale trasforma la softmax in frequenze
intere positive con totale 4.096: assegna prima uno a ogni byte, distribuisce
la parte intera delle quote residue e assegna il resto per frazione decrescente,
risolvendo le parità per indice del byte. Nessun simbolo ha probabilità zero.

Il byte iniziale convenzionale è zero; poi entrambi i lati usano gli ultimi
64 byte e azzerano le posizioni a ogni finestra. Questa convenzione è fissata
dal formato del predittore, pur non essendo un token BOS addestrato separatamente.
La procedura non usa temperatura né decoding generativo.

## Archivio e integrità

L'archivio TBC1 conserva versione, identità del predittore, lunghezza originale,
numero di bit, hash del payload e hash del file originale. Nel caso neurale
l'identità include lo SHA-256 del checkpoint. Input troncati, checksum errati,
modello differente o limite di output superato producono errore. Il decoder
limita l'output a un milione di byte per questa implementazione educativa.

I checksum rilevano corruzione accidentale, non autenticano un mittente ostile.
Inoltre checkpoint identico non implica CDF identica su hardware differenti:
piccole differenze floating-point possono cambiare un arrotondamento. La
prova neurale è ripetibile nell'ambiente numerico CPU dichiarato; la portabilità
bit-per-bit richiede un percorso di inferenza canonico o una verifica specifica
su ogni piattaforma. Il checksum finale rileva una divergenza, non la ripara.

## Esecuzione e confronto onesto

```bash
python3 -m labs.engineering.codec_experiment
python3 -m labs.engineering.byte_codec encode \
  labs/engineering/fixtures/text/base-test.txt /tmp/prova.tbc
python3 -m labs.engineering.byte_codec decode \
  /tmp/prova.tbc /tmp/prova-decoded.txt
```

Le destinazioni devono essere nuove; per ripetere scegli altri nomi. Aggiungi
`--checkpoint output/engineering/tiny-byte-lm.pt` a entrambi i comandi per la
variante neurale. Confronta gli hash e, quando entrambi i file sono disponibili,
anche l'uguaglianza diretta dei byte.

L'esperimento versionato verifica otto round trip: vuoto, tutti i byte, 256
byte pseudocasuali e testo sintetico, ciascuno con due predittori. Sul testo
di 148 byte l'archivio adattivo occupa 359 byte, quello neurale 317 e gzip 60.
Alla prima distribuzione il neurale deve aggiungere 347.451 byte di checkpoint:
totale 347.768. Nei casi esaminati non batte gzip. Un costo ideale basso della
loss non elimina metadati e costo del modello condiviso.

## Consegna e criterio assoluto

Practitioner: spiega perché un archivio di 317 byte può essere meno conveniente
di un file di 148. AI Engineer: aggiungi casi con ripetizioni, UTF-8 e rumore,
mantieni encoder e decoder separati e verifica un checkpoint errato. Produci
una tabella con input, payload, archivio, costo condiviso, tempo ed esito.
Qualunque byte diverso rende fallita la prova lossless, anche se il testo
«sembra uguale». Le prove di rete e radio rimangono un gate separato.

Fonti e contesto: [percorso Pollicino](../pollicino-learning-path.md) e
[timeline dei paper](../research/paper-timeline.md). Il codec e le fixture
qui pubblicati sono originali e non derivati da immagini o pagine Manning.
