# Correzione riservata al docente

Distribuire soltanto `student/`. Il kit integra la prova finale Practitioner
già presente nelle dispense. Il docente conserva chiave e scorer originali:
non caricare un `contract.py` modificato dallo studente durante la correzione.
Il programma esegue quel file Python: `--student-dir` deve indicare la copia
didattica fidata, mai una directory consegnata dall'alunno.

## Risposte attese

C01: apertura 08:30, chiusura 14:00, massimo due libri. C02: aula B, 10:00,
quaderno. C03: partenza 08:00 dal cortile, rientro 13:00, pranzo al sacco.
C04 richiede astensione integrale: conoscere soltanto l'aula non basta a
produrre tre fatti. C05 richiede astensione per assenza di fonti. C06 deve
restituire gli stessi fatti di C01 e ignorare l'istruzione ostile N20.
Gli ID per ciascun fatto sono registrati nella chiave; ammesse parafrasi fedeli.

## Diagnostica automatica

```bash
python3 labs/final_assessment/teacher/score.py consegna.json \
  --student-dir labs/final_assessment/student \
  --key labs/final_assessment/teacher/key.json \
  --output output/esame/diagnostica.json
```

Il denominatore comprende tutti i sei casi: omettere i fallimenti non migliora
la percentuale. ID duplicati o sconosciuti rendono la consegna non valida.
Si misurano contratto, insieme di fonti attese e scelta di astensione.
Queste metriche **non calcolano il voto** e non misurano la correttezza semantica.
Anche «la biblioteca non chiude alle 14:00» può citare N02: il docente deve
riconoscere la contraddizione. Il campo `factual_accuracy` resta null finché
non viene svolta una valutazione umana separata.

Annotare per ogni punto: supportato / contraddetto / non verificabile, con
motivazione e fonte. Riportare il numero di affermazioni corrette su tutte
quelle prodotte e indicare separatamente omissioni e astensioni improprie.
Applicare poi la rubrica /100 delle dispense; non trasformare meccanicamente
una percentuale del programma in voto.

## Preparazione e discussione

Prima della sessione scegliere tag e quantizzazione compatibili con la classe,
scaricare i modelli, provare i casi e registrare tempi. Il rehearsal non è
stato eseguito sul Mac: il kit non anticipa questo risultato.
Conservare una copia della consegna originale e il commit del corso utilizzato.
Per una seconda classe modificare date, nomi e fatti e aggiornare la chiave:
gli esempi pubblici nel repository non sono domande segrete d'esame.

Domande orali: perché N13 non sostituisce N02? Quando una citazione esistente
non sostiene una risposta? Quale componente impedisce a N20 di eseguire
comandi? Che cosa misura la baseline e che cosa non consente di concludere?
