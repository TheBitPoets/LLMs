# M18 - Sistemi e kernel d'inferenza

**Domanda guida:** che cosa succede sotto Ollama?  
**Durata:** 3 ore Practitioner; 18 ore AI Engineer.  
**Prerequisiti:** M05–M06, M10–M11; programmazione numerica per l'estensione.

## Obiettivi osservabili

Distinguere load, prefill e decode; leggere TTFT, token/s, memoria e KV cache;
spiegare batching e bandwidth. L'AI Engineer implementa un kernel minimale e lo
confronta con un riferimento.

## Lezione intuitiva

Nel **prefill** molti token del prompt vengono processati insieme e costruiscono
la KV cache; nel **decode** arriva un token alla volta e si riusano Key/Value
precedenti. Prompt lungo aumenta TTFT e cache; output lungo ripete molti passi
di decode. Continuous batching inserisce richieste senza aspettare che l'intero
lotto finisca; paged KV riduce sprechi e frammentazione.

## Laboratorio Practitioner

Con Ollama eseguire matrice 3×3 di prompt/output corti, medi e lunghi. Registrare
load duration, prompt eval duration, eval duration e token count se esposti.
Separare cold/warm. Variare context finché memoria/latency non sono accettabili.

## AI Engineer

1. scrivere matmul e causal attention di riferimento;
2. aggiungere tiling/vectorization con NumPy, PyTorch o Triton quando disponibile;
3. confrontare output con tolleranze per dtype;
4. profilare tempo, bandwidth stimata e allocazioni;
5. studiare online softmax/FlashAttention senza dichiarare equivalente un kernel incompleto.

Kernel corretto prima che veloce: shape casuali, dimensioni non multiple del
tile, mask, NaN/Inf e seed. Per Pollicino, la determinismo richiesto dal codec
può imporre un percorso diverso dal serving generativo tollerante.

## Verifica

Profilo 2, distinzione prefill/decode 2, correttezza reference 3, speedup onesto
1, limiti hardware/precisione 2. Fonti: FlashAttention, vLLM e testi CUDA/Triton.

