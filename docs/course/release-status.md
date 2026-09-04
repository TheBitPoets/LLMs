# Stato di rilascio della prima edizione

Data audit documentale: 4 settembre 2026.

## Completato e verificato nel repository

- mappa annuale e criteri di completamento;
- 20 moduli Practitioner/AI Engineer;
- snapshot modelli datato e fonti ufficiali;
- timeline ragionata dei paper;
- dieci visuali interattive originali;
- dodici laboratori minimi tramite runner standard-library;
- fixture, baseline e test negativi;
- diagnostica, prova finale, rubriche e guida docente;
- rehearsal hardware documentato;
- CI per struttura, link locali, JavaScript, JSON e unit test;
- test automatici locali: 12/12 passati.

## Gate esterno ancora necessario

Il rehearsal Ollama deve essere eseguito sul Mac M4 Pro 36 GB o su un altro
profilo dichiarato. Questo ambiente non espone quel servizio/hardware, quindi
non vengono inventati TTFT, token/s, memoria, digest o risultati di qualità.

## Stato corretto

**Course content complete / hardware validation pending.**

La prima edizione candidata è stata integrata in `main` con la PR #1 e commit
di merge `af41651b09880981506a83d7d53a4f22bde061bf`. Non creare il tag
`course-v1` e non dichiarare “validato in classe” finché:

1. il rehearsal end-to-end non produce evidence package;
2. il docente non registra tempo reale e problemi del primo pilot;
3. gli eventuali finding del rehearsal non sono chiusi o accettati esplicitamente.

Le implementazioni neurali avanzate di Pollicino restano roadmap del progetto
esterno; il corso include e verifica solo il codec didattico/statistico presente
nel runner e non confonde questo risultato con un Byte Transformer completato.
