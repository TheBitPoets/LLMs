# Soluzione docente

## S00 - Baseline e mappa del repository

Nello starter `Booking` rappresenta i dati; `BookingService.reserve` controlla
solo un conflitto e aggiunge una riga; `overlaps` usa erroneamente confronti
inclusivi. `cancel` non è implementato e `list_active` conserva l'ordine di
inserimento. Mancano validazione e idempotenza. I casi happy path, conflitto
effettivo e due aule diverse passano; adiacenza, validazione, retry, riuso ID,
cancellazione e ordinamento espongono le lacune.

La mappa corretta collega R02 a `overlaps` e al test di adiacenza; R04 a
`reserve` e ai due test sul request_id; R05 a `cancel`. Respinge una risposta
dell'agente che dichiari presenti un database o un endpoint HTTP nello starter.
Per chi fatica con il codice, usare tre schede cartacee: stato prima, richiesta,
stato dopo. Questo supporto mantiene osservabile lo stesso risultato didattico.

Evidenza minima: output originale, tre collegamenti corretti e una deduzione
separata da una misura. La domanda sul documento obsoleto verifica che lo
studente attribuisca il difetto al contesto, senza invocare automaticamente
un modello più grande. Non richiedere un account cloud per superare questa fase.
