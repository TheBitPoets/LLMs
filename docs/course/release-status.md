# Stato di rilascio della prima edizione

Data audit documentale: 4 settembre 2026.

## Completato e verificato nel repository

- mappa annuale e criteri di completamento;
- 20 moduli Practitioner/AI Engineer;
- dispense sviluppate: circa 14.000 parole più glossario e apparati;
- volume studente A4 e volume docente A4 con soluzioni, in PDF/HTML/Markdown;
- Content Pack `thebitlab.content-pack.v1` con 20 content item;
- Course Design annuale da 34 settimane e 20 Activity 1.0 A–F;
- snapshot modelli datato e fonti ufficiali;
- timeline ragionata dei paper;
- dieci visuali interattive e sette figure statiche originali;
- dodici laboratori minimi tramite runner standard-library;
- fixture, baseline e test negativi;
- diagnostica, prova finale, rubriche e guida docente;
- rehearsal hardware documentato;
- CI per struttura, link locali, JavaScript, JSON e unit test;
- test automatici locali: 12/12 passati.

## Gate esterni ancora necessari

Il rehearsal Ollama deve essere eseguito sul Mac M4 Pro 36 GB o su un altro
profilo dichiarato. Questo ambiente non espone quel servizio/hardware, quindi
non vengono inventati TTFT, token/s, memoria, digest o risultati di qualità.

Il Content Pack è `reviewed`, non `approved`: serve la revisione esplicita del
docente sulle dispense, sulle soluzioni e sulle Activity. Solo allora tutti gli
elementi possono passare ad `approved` e alimentare un Course Bundle immutabile.

## Stato corretto

**Course materials complete / teacher approval and hardware validation pending.**

La prima edizione candidata è stata integrata in `main` con la PR #1 e commit
di merge `af41651b09880981506a83d7d53a4f22bde061bf`. Non creare il tag
`course-v1` e non dichiarare “validato in classe” finché:

1. il rehearsal end-to-end non produce evidence package;
2. il docente non registra tempo reale e problemi del primo pilot;
3. gli eventuali finding del rehearsal non sono chiusi o accettati esplicitamente.

Le implementazioni neurali avanzate di Pollicino restano roadmap del progetto
esterno; il corso include e verifica solo il codec didattico/statistico presente
nel runner e non confonde questo risultato con un Byte Transformer completato.
