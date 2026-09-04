# M04 - Apprendere dai dati

**Domanda guida:** come cambia un modello durante il training?  
**Durata:** 4 ore Practitioner; 12 ore AI Engineer.  
**Prerequisiti:** M02–M03; derivate per l'estensione.

## Obiettivi osservabili

Spiegare esempio→previsione→loss→gradiente→aggiornamento; distinguere train,
validation e test; riconoscere underfitting, overfitting e leakage. L'AI
Engineer deriva e implementa gradient descent, backpropagation e AdamW.

## Lezione intuitiva

Immaginiamo una manopola che modifica la previsione. La loss misura quanto la
previsione si discosta dal target; il gradiente indica la direzione locale in
cui la loss cresce. Ci muoviamo in direzione opposta di un passo controllato
dal learning rate. Un singolo passo non “insegna un fatto”: modifica molti
comportamenti collegati.

I dati di validation sono uno specchio durante lo sviluppo; il test è una busta
sigillata aperta alla fine. Se scegliamo il modello guardando ripetutamente il
test, quel test diventa di fatto training decisionale.

## Matematica

Per regressione semplice `ŷ=wx+b`, `L=(ŷ-y)^2`, quindi
`∂L/∂w=2(ŷ-y)x`. L'aggiornamento è `w←w-η∂L/∂w`. Per next-token si usa la
cross-entropy. Backprop applica la chain rule al grafo; AdamW mantiene momenti
dei gradienti e separa weight decay dall'aggiornamento adattivo.

## Laboratorio

Addestrare un neurone su dati sintetici con gradienti calcolati a mano e
confrontati con finite differences. Poi addestrare un MLP next-symbol piccolo,
tracciando train/validation loss. Baseline: frequenza del simbolo. Test
negativi: label casuali e split duplicati per mostrare rispettivamente limite
di apprendimento e leakage.

## Verifica

Interpretare tre curve senza vedere il codice e proporre un intervento
falsificabile. Rubrica: ciclo training 3, split 2, gradiente 2, diagnosi curve
2, limite 1. Fonti: Goodfellow et al., *Deep Learning*, capitoli 6–8; AdamW e
materiali PyTorch vengono citati nella guida AI Engineer.

