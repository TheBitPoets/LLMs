# Guida docente M04 — Apprendere dai dati

Riservato al docente.

## M04 - Training e generalizzazione

Riferimento eseguibile: `python3 -m labs.engineering.train`. Controllare
`training-report.json`, split e hash. Il base ha test loss circa 0,295 nat/byte
contro circa 2,92 dell'unigramma; la conclusione valida riguarda il corpus
sintetico a template. Le righe test sono distinte, ma i template sono comuni:
non è una prova di generalizzazione a documenti scolastici reali.
La selezione avviene sul minimo di validation ai checkpoint osservati; il test
non sceglie il learning rate. Se lo studente introduce uno split per argomento,
aspettarsi risultati diversi e valutarne l'interpretazione. Non richiedere
la medesima durata CPU o un identico ultimo decimale su altre piattaforme.
La regressione scalare del runner base resta utile per spiegare il gradiente.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
