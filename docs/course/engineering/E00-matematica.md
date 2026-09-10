# E00 - La matematica che serve nel laboratorio

## Obiettivi e intuizione Practitioner

Immagina un mixer: ogni cursore descrive una proprietà, ogni collegamento
decide quanto quella proprietà influenza un'altra. Un vettore raccoglie i
cursori, una matrice contiene i pesi dei collegamenti. Non è necessario che
un singolo cursore significhi sempre «animale» o «verbo»: nei modelli reali le
caratteristiche possono essere distribuite fra molte coordinate.

Al termine distingui numero, vettore, matrice, probabilità e derivata; sai
leggere le dimensioni di un'operazione e spiegare perché il training modifica
i pesi. Nel percorso intuitivo bastano i numeri degli esempi; chi studia AI
Engineer ricostruisce i passaggi e li collega a `tiny_lm.py`.

## Vettori, matrici e forme

Con $x=(1,2)$ e $w=(3,-1)$, il prodotto scalare è
$x\cdot w=1\cdot3+2\cdot(-1)=1$. Una matrice $W$ con due righe e tre
colonne trasforma il vettore riga $x$ in tre numeri: $y=xW+b$.
La forma è $(1,2)(2,3)+(1,3)=(1,3)$. La somma del bias si ripete per
ogni esempio del batch: questo è broadcasting, non un nuovo peso per esempio.

Per $B$ sequenze, $T$ posizioni e larghezza $D$, le rappresentazioni hanno
forma $(B,T,D)$. Una proiezione di attenzione produce query, key e value;
con $H$ teste, ciascuna testa usa $d=D/H$ coordinate. Nel modello del corso
$D=48$, $H=4$, quindi $d=12$. Scrivere queste dimensioni prima del codice
evita errori che una formula senza indici nasconde.

## Da punteggi a probabilità

I logits sono punteggi liberi, anche negativi. La softmax li normalizza:

$$p_i=\frac{e^{z_i-m}}{\sum_j e^{z_j-m}},\qquad m=\max_j z_j.$$

Sottrarre lo stesso $m$ non cambia i rapporti e riduce il rischio di overflow.
Con logits $(\ln 2,0)$ otteniamo $(2/3,1/3)$. Una temperatura $\tau>0$
divide i logits prima della softmax: a $\tau=2$ la distribuzione è meno
concentrata. Temperatura zero è una convenzione di selezione greedy nel
decoder; non si deve eseguire letteralmente una divisione per zero.

Se il simbolo osservato è il secondo, la loss è $-\ln(1/3)=\ln3$, circa
1,099 nat. In bit è $-\log_2(1/3)$, circa 1,585. Per $N$ simboli:

$$L=-\frac1N\sum_{t=1}^N\ln p(x_t\mid x_{<t}),
\qquad \mathrm{PPL}=e^L,\qquad \mathrm{bpb}=L/\ln2.$$

La perplexity è una misura del costo probabilistico medio, non una percentuale
di risposte vere. Confrontarla fra tokenizer diversi può essere fuorviante:
un token non contiene sempre lo stesso numero di byte. Nel nostro modello il
vocabolario è esattamente l'insieme dei 256 byte, quindi bpb è ben definito.

## Derivate, catena e aggiornamento AI Engineer

La derivata dice come cambia la loss per un piccolo cambiamento di parametro.
Per una softmax seguita da cross-entropy con target one-hot $y$:

$$\frac{\partial L}{\partial z_i}=p_i-y_i.$$

Nell'esempio precedente, target secondo, il gradiente è $(2/3,-2/3)$.
Un passo di discesa riduce il primo logit e aumenta il secondo. Non servono
due regole indipendenti per «premiare» e «punire»: il gradiente produce entrambe.
La formula segue da $L=-z_k+\log\sum_j e^{z_j}$ derivando i due termini.

Per $Y=XW$, se $G=\partial L/\partial Y$, allora
$\partial L/\partial W=X^TG$ e $\partial L/\partial X=GW^T$.
Le trasposte fanno coincidere le dimensioni. In una rete composta il gradiente
attraversa ogni operazione in ordine inverso: è la regola della catena.
Autograd registra questo grafo; `backward()` calcola derivate, mentre
`optimizer.step()` aggiorna i pesi. Sono due operazioni diverse.

SGD usa $\theta' = \theta-\eta g$. AdamW stima medie mobili di gradiente e
quadrato del gradiente, corregge il bias iniziale e applica un decadimento
separato dei pesi. Il clipping limita la norma del gradiente: non sostituisce
né il learning rate né una buona separazione dei dati.

## Laboratorio e verifica

Esegui `python3 labs/course_lab.py softmax --logits 0 1 2` e
`python3 labs/course_lab.py gradient --steps 12`. Prima prevedi cosa accade
aggiungendo 100 a tutti i logits; poi ripeti la softmax. Calcola a mano loss
e gradiente nell'esempio a due classi. In E04 controlla che il programma usi
target spostati di una posizione e che il test resti escluso dalla selezione.

Consegna una pagina con forme delle matrici, un calcolo completo e un errore
diagnosticato. Per verificare una derivata puoi usare differenze centrali
$(L(\theta+\epsilon)-L(\theta-\epsilon))/(2\epsilon)$ su un modello minuscolo
in float64; un epsilon troppo piccolo amplifica gli errori di arrotondamento.

Fonte primaria: [Transformer](https://arxiv.org/abs/1706.03762).
Il modello didattico usa varianti esplicitate in E04: non replica tutte le
scelte del paper né le architetture dei modelli di frontiera.
