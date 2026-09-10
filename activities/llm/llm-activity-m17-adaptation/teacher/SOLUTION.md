# Guida docente M17 — Fine-tuning e adapter

Riservato al docente.

## M17 - Adapter e regressione

Il riferimento E05 apprende 1.216 parametri sulla head. Con B iniziale zero,
l'output iniziale coincide con il base; congelare i parametri si controlla
anche confrontando i tensori prima/dopo. Nel report target loss 6,449→1,471,
base loss 0,295→4,759: l'adattamento fallisce un requisito di mantenimento
delle prestazioni originali. Una soluzione corretta non nasconde questa
regressione e propone un esperimento, non una cura certa.
Per confrontare ranghi, usare validation per scegliere e un test finale
separato; non richiedere che il rango maggiore vinca. Il loader controlla
l'hash del base prima di caricare l'adapter. LoRA sulla sola head non equivale
a QLoRA o a un fine-tuning completo di tutte le proiezioni.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
