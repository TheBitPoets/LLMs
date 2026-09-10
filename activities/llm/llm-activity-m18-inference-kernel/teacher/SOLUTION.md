# Guida docente M18 — Sistemi e kernel d'inferenza

Riservato al docente.

## M18 - Kernel e benchmark

Prima del timing servono equivalenza numerica e causalità. E06 confronta
reference, softmax online tiled e funzione di libreria; il tiled Python
risulta più lento nella shape misurata. È un esito corretto: spiega il costo
dei cicli e delle chiamate rispetto alla fusione hardware. La cache mantiene
K/V e usa posizioni con offset; un test su singolo token senza passato non
basta a controllarla. Il report distingue prefill e decode ripetuto.
La consegna avanzata deve includere dimensioni non multiple del tile e più
ripetizioni. Su GPU richiedere sincronizzazione; su CPU non inventare una
misura GPU. Una tolleranza troppo larga che nasconde errori non è equivalenza.

Rubrica: evidenze 4; spiegazione 3; correttezza 2; limiti 1.
