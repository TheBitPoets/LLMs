# LLMs

<h2>1 Quadro generale: cosa sono gli LLM?</h2>

<table align="center">
  <td>
    <h3>Questo capitolo copre</h3>
    <ul>
       <li>Cosa sono i trasformatori generativi preaddestrati e i grandi modelli linguistici</li>
      <li>Come funzionano gli LLM in parole semplici</li>
      <li>Come gli esseri umani e le macchine rappresentano le lingue in modo diverso</li>
      <li>Perché strumenti come ChatGPT funzionano così bene</li>
      <li>Comprendere i limiti e le preoccupazioni dell'utilizzo degli LLM</li> 
    </ul>
  </td>
</table>

<p align="justify">
L'entusiasmo attorno a termini come machine learning (ML), deep learning (DL) e intelligenza artificiale (IA) ha raggiunto livelli record. Gran parte della prima esposizione pubblica a questi termini è stata guidata da un prodotto chiamato ChatGPT, una forma di IA generativa sviluppata da un'azienda chiamata OpenAI. Ora vediamo offerte di IA generativa come Gemini di Google, Copilot di Microsoft, Llama di Meta, Claude di Anthropic e nuovi arrivati come DeepSeek nelle notizie quotidiane. Apparentemente da un giorno all'altro, la capacità dei computer di parlare, imparare ed eseguire compiti complessi ha compiuto un balzo in avanti radicale. Stanno nascendo nuove aziende di IA generativa e le aziende esistenti stanno investendo pubblicamente miliardi di dollari nel settore. La tecnologia in questo ambito si sta evolvendo a un ritmo esasperante.
</p>

<p align="justify">
Questo libro si propone di aiutarvi a dare un senso a questo nuovo mondo, dissipando il mistero che si cela dietro il funzionamento di ChatGPT e delle tecnologie correlate. ...
</p>

<p align="justify">
Dopo aver letto questo libro, capirai cos'è realmente l'intelligenza artificiale generativa come ChatGPT , cosa può e non può fare e, soprattutto, il "perché" dietro i suoi limiti. Con questa conoscenza, sarai un consumatore più efficace di questa famiglia di tecnologie, sia come utente, sviluppatore software o decisore aziendale in organizzazioni che decidono se e, in caso affermativo, come integrarla nei propri prodotti o nelle proprie attività. Questa base servirà anche da trampolino di lancio per studi più approfonditi nel campo, fornendo conoscenze che ti permetteranno di comprendere ricerche approfondite e altri lavori.
</p>

<h3>1.1 L'intelligenza artificiale generativa nel contesto</h3>

<p align="justify">
Innanzitutto, dobbiamo essere più specifici su ciò di cui parliamo quando parliamo di LLM, GPT e dei vari strumenti che si basano su di essi. GPT in ChatGPT sta per Generative Pretrained Transformer . Ognuna di queste parole ha un significato particolare nel contesto di ChatGPT. Dedicheremo i capitoli successivi a discutere il significato di pretrained e transformer , ma iniziamo qui discutendo il significato di generativo in questo contesto.
</p>

<p align="justify">
I chatbot basati sull'intelligenza artificiale come ChatGPT sono una forma di intelligenza artificiale generativa . In generale, l'intelligenza artificiale generativa è un software in grado di creare o generare vari media (ad esempio, testo, immagini, audio e video) sulla base di dati osservati in passato e influenzati da ciò che le persone considerano un output piacevole e accurato. Ad esempio, se a ChatGPT viene chiesto "Scrivi un haiku sulla neve che cade sui pini", utilizzerà tutti i dati con cui è stato addestrato su haiku, neve, pini e altre forme di poesia per generare un haiku originale, come mostrato nella figura 1.1.
</p>

<table align="center">
  <td>
<div align="center">
  <figure>
    <figcaption>Figura 1.1 Un semplice haiku generato da ChatGPT</figcaption>
<img width="690" height="512" alt="CH01_F01_Boozallen" src="https://github.com/user-attachments/assets/6863ce33-0c84-4832-a28b-d22a0a5929f7" />
  </figure>
</div>
    </td>
</table>

<p align="justify">
Fondamentalmente, questi sistemi sono modelli di apprendimento automatico che generano nuovi output, quindi l'intelligenza artificiale generativa è una descrizione appropriata. Alcuni possibili input e output sono illustrati nella figura 1.2 . Sebbene ChatGPT si occupi principalmente di testo come input e output, offre anche un supporto più sperimentale per diversi tipi di dati, come audio e immagini. Tuttavia, dalla nostra definizione, si può immaginare che molti tipi diversi di algoritmi e attività rientrino nella descrizione dell'intelligenza artificiale generativa.
</p>

<table align="center">
  <td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 1.2 L'intelligenza artificiale generativa prende alcuni input (numeri, testo, immagini) e produce un nuovo output (solitamente testo o immagini). È possibile qualsiasi combinazione di opzioni di input o output e la natura dell'output dipende dal tipo di algoritmo addestrato. Potrebbe essere necessario aggiungere dettagli, riscrivere qualcosa per renderlo più breve, estrapolare parti mancanti e altro ancora.
      </p>
    </figcaption>
<img width="1100" height="581" alt="CH01_F02_Boozallen" src="https://github.com/user-attachments/assets/c804ed7b-cf44-4644-8ca6-64eca75cbd05" />
  </figure>
</div>
    </td>
</table>

<p align="justify">
Approfondendo ulteriormente, ChatGPT si occupa di testo umano, quindi sarebbe anche corretto definirlo un modello del linguaggio umano, o un modello linguistico, se si è una persona competente che lavora nel campo noto come elaborazione del linguaggio naturale (NLP). Il campo dell'NLP interseca sia l'informatica che la linguistica ed esplora la tecnologia che aiuta i computer a comprendere, manipolare e creare il linguaggio umano. Alcuni dei primi tentativi nel campo dell'NLP risalgono agli anni '40, quando i ricercatori speravano di costruire macchine in grado di tradurre automaticamente tra lingue diverse. Di conseguenza, l'NLP e i modelli linguistici esistono da molto tempo. Quindi, cosa rende diversi i nuovi strumenti di intelligenza artificiale generativa? La differenza più evidente è che ChatGPT e algoritmi simili sono molto più complessi di quelli che le persone hanno costruito in passato e vengono addestrati su quantità di dati molto maggiori.
</p>

<p align="justify">
Per questo motivo, il termine " large language models" (LLM) è diventato piuttosto diffuso per descrivere GPT e modelli di apprendimento automatico simili. GPT descrive un tipo specifico di LLM sviluppato da OpenAI, e altre aziende utilizzano tecnologie simili per costruire i propri LLM e chatbot di intelligenza artificiale. Più in generale, gli LLM sono modelli di apprendimento automatico addestrati su grandi quantità di dati linguistici.
</p>

<p align="justify">
Un diagramma di queste relazioni è visibile nella figura 1.3 . ChatGPT, Copilot, Claude e Gemini sono alcuni dei prodotti che operano tramite testo e sono costruiti utilizzando LLM. Gli LLM utilizzano tecniche di intelligenza artificiale e PNL. Il componente principale di un LLM è un trasformatore, che spiegheremo in dettaglio nel capitolo 3.
</p>

<table align="center">
  <td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 1.3 Una mappa di alto livello dei vari termini con cui avrai familiarità e delle loro relazioni. L'intelligenza artificiale generativa è una descrizione della funzionalità: la funzione di generare contenuti e utilizzare tecniche di intelligenza artificiale per raggiungere tale obiettivo.
      </p>
    </figcaption>
<img width="1100" height="374" alt="CH01_F03_Boozallen" src="https://github.com/user-attachments/assets/683f1e58-1dff-45ec-a5a0-e588ec971f8e" />
  </figure>
</div>
    </td>
</table>

<p align="justify">
Nota: la vista e il linguaggio non sono le uniche opzioni per l'IA generativa. La generazione di audio (si pensi alla sintesi vocale, come quando il GPS pronuncia i nomi delle strade), i giochi da tavolo come gli scacchi e persino il ripiegamento delle proteine hanno utilizzato l'IA generativa. Questo libro si concentrerà principalmente su testo e linguaggio, poiché questi sono i principali tipi di dati utilizzati da GPT e LLM.
</p>

<p align="justify">
Come suggerisce il nome , questi modelli non sono piccoli. Si dice specificamente che ChatGPT [1] contenga 1,76 trilioni di parametri che vengono utilizzati per determinarne il comportamento. Ogni parametro è in genere memorizzato come un numero in virgola mobile (un numero con un punto decimale) che utilizza 4 byte per l'archiviazione. Ciò significa che il modello stesso occupa 7 terabyte di memoria. Questa dimensione è maggiore di quanto la maggior parte dei computer potrebbe contenere nella RAM, per non parlare delle unità di elaborazione grafica (GPU) più potenti con 80 gigabyte di memoria. Le GPU sono componenti hardware speciali che eccellono nell'esecuzione delle operazioni matematiche che rendono possibili gli LLM. Attualmente, per la realizzazione di LLM sono necessarie molte GPU, quindi stiamo già discutendo di un'ampia infrastruttura computazionale e di complessità su più macchine per costruire un LLM. Al contrario, i modelli linguistici più comuni sarebbero di 2 GB o meno nella maggior parte dei casi, ovvero oltre 5.000 volte più piccoli, una dimensione molto più ragionevole se si considera la creazione e l'utilizzo di un modello del genere su hardware più standard.
</p>

<table align="center">
  <td>
    <h4>Ottimizzazione degli LLM</h4>
    <p align="justify">
Molti ricercatori stanno studiando modi per ridurre il consumo di memoria dei LLM. A volte, questo include tecniche che richiedono meno di 4 byte per memorizzare un parametro, utilizzando un metodo chiamato "precisione mista" [2]. Questo approccio memorizza alcuni parametri LLM utilizzando 2 byte o meno e presenta un compromesso tra accuratezza ed efficienza della memoria. Alla fine, l'effetto sull'accuratezza è spesso trascurabile. Questa ottimizzazione è una delle tante che i ricercatori adottano per rendere i LLM più efficienti in termini di risorse
    </p>
  </td>
</table>

<table align="center">
  <td>
    <h4>Alternative GPU</h4>
    <p align="justify">
Sebbene le GPU siano attualmente l'hardware più utilizzato per addestrare i modelli di apprendimento automatico (LLM), non sono l'unica opzione disponibile. Sempre più aziende stanno sviluppando hardware specifico che offre vantaggi generali per l'addestramento di modelli di apprendimento automatico. Ad esempio, nel 2018, Google ha reso disponibile al pubblico la sua Tensor Processing Unit (TPU) [3] come parte della Google Cloud Platform (GCP). Sebbene le TPU abbiano generalmente una capacità di calcolo inferiore rispetto alle GPU, la loro architettura specializzata consente loro di ottenere prestazioni migliori rispetto alle GPU per specifiche attività di apprendimento automatico.
    </p>
  </td>
</table>

<h3>1.2 Cosa imparerai</h3>

<p align="justify">
In questo libro, spiegheremo come funzionano gli LLM e vi forniremo il vocabolario necessario per comprenderli. Una volta terminata la lettura, avrete una comprensione colloquiale di cosa sia un LLM e dei passaggi critici coinvolti nel suo funzionamento. Inoltre, avrete una prospettiva su ciò che un LLM può ragionevolmente fare, in particolare le considerazioni relative alla sua implementazione o al suo utilizzo. Discuteremo i punti salienti sui limiti fondamentali degli LLM e forniremo suggerimenti su come progettare tenendo conto di questi o quando gli LLM e, più in generale, l'IA generativa dovrebbero essere completamente evitati.
</p>

<p align="justify">
Tenete presente che i dettagli su come i trasformatori vengono combinati per costruire ChatGPT, Claude o Gemini sono sfumati e questo libro si concentra principalmente su ciò che tutti questi sistemi hanno in comune. In effetti, non possiamo conoscere alcune delle effettive differenze tra questi LLM perché, sebbene i fornitori commerciali di LLM abbiano condiviso molte informazioni sui loro modelli, non ne hanno condivise alcune, probabilmente considerate segreti commerciali.
</p>

<p align="justify">
A causa dell'impatto che gli LLM basati sui trasformatori avranno sul mondo, ci siamo volutamente concentrati su un vasto pubblico per questo libro. Programmatori di ogni estrazione, dirigenti, manager, addetti alle vendite, artisti, scrittori, editori e molti altri dovranno interagire con gli LLM o subire le conseguenze sul loro lavoro nei prossimi anni. Quindi, daremo per scontato che tu, caro lettore, abbia una conoscenza minima di programmazione, ma che abbia familiarità con i costrutti di base della programmazione: logica, funzioni e forse anche alcune strutture dati. Inoltre, non è necessario essere un matematico; ti mostreremo un po' di matematica dove può essere utile, ma sarà facoltativa per comprendere il funzionamento degli LLM.
</p>

<p align="justify">
Questo approccio implica che in questo libro verrà presentato pochissimo codice. Se desiderate approfondire direttamente la creazione e l'utilizzo di un LLM, consultate altri libri del catalogo Manning, come " Build a Large Language Model from Scratch" di Sebastian Raschka (2024) o " Inside Deep Learning" di Edward Raff. (2022), completeranno il materiale presentato qui. Tuttavia, se volete capire perché l'LLM che state utilizzando produce output insoliti, come il vostro team potrebbe essere in grado di utilizzarlo o dove evitarlo, o se avete un collega con poca esperienza in machine learning che ha bisogno di acquisire competenze conversazionali, questo è il libro di cui voi e i vostri colleghi avete bisogno.
</p>

<p align="justify">
In particolare, la prima parte di questo libro si concentra su cosa fanno gli LLM: i loro input e output, la conversione degli input in output e come vincoliamo la natura di tali output. Nella seconda parte, ci concentriamo su cosa fanno gli esseri umani: come interagiscono con la tecnologia e quali rischi ciò comporta per l'utilizzo dell'IA generativa. Analogamente, discuteremo alcune considerazioni etiche che sorgono durante l'utilizzo e la creazione di LLM.
</p>

<table align="center">
  <td>
    <h4>La formazione LLM è costosa</h4>
    <p align="justify">
      Per la maggior parte delle persone, conseguire un LLM non è realisticamente possibile; richiede un investimento minimo di 100.000 dollari e comporterebbe uno sforzo di 100 milioni di dollari per cercare di competere con OpenAI. Allo stesso tempo, le risorse disponibili per la formazione degli LLM sono in continua evoluzione. Di conseguenza, invece di illustrare come si presenta oggi un LLM, ci concentriamo su contenuti con una durata più lunga: conoscenze utili che riteniamo saranno valide tra anni, anziché su esempi di codice che potrebbero essere obsoleti in pochi mesi.
    </p>
  </td>
</table>

<h3>1.3 Introduzione al funzionamento degli LLM</h3>

<p align="justify">
L'intelligenza artificiale generativa (GAI o GenAI) è destinata a cambiare il modo in cui produciamo e interagiamo con le informazioni. L'introduzione di ChatGPT nel novembre 2022 ha evidenziato le capacità dell'intelligenza artificiale moderna e ha affascinato una parte significativa del mondo. Attualmente, è possibile registrarsi gratuitamente su https://chat.openai.com/ per provarlo.
</p>

<p align="justify">
Se inserisci il prompt di testo "Riassumi il testo seguente in due frasi", seguito da tutto il testo introduttivo di questo capitolo, otterrai qualcosa di simile a quanto segue.
</p>

<p align="justify">
"Il recente aumento di attenzione verso l'intelligenza artificiale, in particolare i modelli linguistici di grandi dimensioni (LLM) come ChatGPT di OpenAI, ha evidenziato le loro vaste capacità nell'elaborazione del linguaggio naturale. Questo libro si propone di fornire ai lettori una comprensione colloquiale degli LLM, delle loro complessità operative, delle potenziali applicazioni, dei limiti e delle considerazioni etiche che circondano il loro utilizzo, presupponendo solo una familiarità di base con i concetti di programmazione e un background matematico minimo. È davvero impressionante e, a un pubblico occasionale, potrebbe sembrare che questa capacità sia nata dal nulla."
</p>

<p align="justify">
Quando visiti il sito web di OpenAI e ti registri a ChatGPT, potresti notare un'opzione simile a quella mostrata nella figura 1.4 . Come suggerisce il nome GPT-4, OpenAI sta, al momento della stesura di questo articolo, lavorando alla sua quarta generazione di modelli GPT. I LLM come GPT-4 rappresentano un'area consolidata della ricerca in ML per la creazione di algoritmi in grado di sintetizzare e reagire alle informazioni, producendo output che sembrano generati dall'uomo. Questa capacità sblocca diverse aree di interazione tra persone e macchine che in precedenza esistevano solo nella fantascienza. La potenza della rappresentazione linguistica codificata in ChatGPT consente dialoghi convincenti, la comprensione delle istruzioni, la generazione di riassunti, la risposta alle domande, la creazione di contenuti e molte altre applicazioni. In effetti, è probabile che molte possibili applicazioni di questa tecnologia non esistano ancora perché la nostra reazione istintiva è quella di pensare ai nostri problemi attuali piuttosto che a nuove capacità o prodotti che potrebbero esistere.
</p>

<table align="center">
  <td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 1.4 Quando ti registri a ChatGPT di OpenAI, hai due opzioni: il modello GPT-3.5, che puoi utilizzare gratuitamente, o il modello GPT-4, che è a pagamento.
      </p>
    </figcaption>
<img width="720" height="546" alt="CH01_F04_Boozallen" src="https://github.com/user-attachments/assets/4a7e0c8a-83e7-48d1-8dbd-1840b0018aa8" />
  </figure>
</div>
    </td>
</table>

<p align="justify">
Il fattore critico per te, lettore, è che questa tecnologia non è nata dal nulla, ma è il risultato di progressi costanti nell'ultimo decennio, caratterizzati da notevoli miglioramenti anno dopo anno nell'apprendimento automatico. Di conseguenza, sappiamo già molto sul funzionamento degli LLM e sui modi in cui possono fallire.
</p>

<p align="justify">
Presumiamo un background minimo in modo che possiate regalare questo libro ad amici e familiari. (Uno degli autori spera di poter regalare questo libro alla propria madre, che è molto orgogliosa di loro anche se non sa esattamente quale sia il loro lavoro.) Di conseguenza, dobbiamo colmare una lacuna potenzialmente ampia nel background prima di immergerci nell'argomento. Questo primo capitolo mira a fornirvi questo background in modo che il capitolo successivo possa iniziare il processo di risposta a questa domanda: come diavolo ha fatto un computer a riassumere l'introduzione di questo libro?
</p>

<h3>1.4 Cos'è l'intelligenza?</h3>

<p align="justify">
Intelligenza artificiale è un nome eccellente dal punto di vista del marketing, sebbene in origine fosse utilizzato per indicare un intero campo di ricerca accademica. Questa pratica ha portato a un sottile problema che fornisce alle persone un falso modello mentale del funzionamento dell'IA. Cercheremo di evitare di rafforzare questo modello. Per spiegarlo, discuteremo perché "intelligenza artificiale" non è un nome così attraente. Possiamo dimostrarlo facilmente considerando una semplice domanda: cos'è l'intelligenza?
</p>

<p align="justify">
Si potrebbe pensare che qualcosa come un test del quoziente intellettivo (QI) possa aiutarci a rispondere a questa domanda. I test del QI hanno una forte correlazione con numerosi risultati, come il rendimento scolastico, ma non ci forniscono una definizione oggettiva di intelligenza. Gli studi dimostrano che una certa dose di fattori naturali (ereditarietà) e culturali (ambiente) influenzano il QI di una persona. Dovrebbe anche sembrare sospetto il fatto che possiamo ridurre l'intelligenza a qualcosa di così semplice come un numero: dopotutto, spesso rimproveriamo le persone per essere "intelligenti solo sui libri" e non "intelligenti per la strada". Anche se sapessimo cos'è l'intelligenza, cosa la renderebbe artificiale? L'intelligenza ha forse aromi e coloranti artificiali?
</p>

<p align="justify">
In conclusione, i test del QI misurano la capacità di eseguire un insieme finito di capacità, per lo più alcuni specifici tipi di enigmi logici in un intervallo di tempo limitato, ma non ci aiutano a comprendere la natura fondamentale dell'intelligenza. La verità è che non esiste una comprensione perfetta di cosa sia l'intelligenza.
</p>

<p align="justify">
Il campo dell'intelligenza artificiale cerca da tempo di far sì che i computer, che sono macchine rigide, deterministiche e che seguono regole, svolgano compiti specifici che gli esseri umani possono svolgere ma di cui non possono fornire definizioni o istruzioni precise. Ad esempio, se vogliamo che un computer conti fino a 1.000 e stampi ogni numero divisibile per 5, possiamo scrivere istruzioni dettagliate che quasi tutti i programmatori possono convertire in codice. Ma se vi chiedo di scrivere un programma che tenti di rilevare se un'immagine arbitraria contiene un gatto, la sfida è ben diversa. Bisogna in qualche modo definire con precisione cos'è un gatto e poi tutti i dettagli su come riconoscerlo. Come si scrive esattamente il codice per trovare e distinguere i baffi di un gatto da quelli di un cane? Come si riconosce un gatto quando non ha i baffi? In fin dei conti, non è facile.
</p>

<p align="justify">
Tuttavia, poiché l'intelligenza artificiale e l'apprendimento automatico si sono concentrate su questi compiti difficili da specificare che gli esseri umani possono svolgere, descrivere gli algoritmi di intelligenza artificiale e apprendimento automatico usando analogie è diventato particolarmente comune. Per far sì che un computer rilevi i gatti, forniamo migliaia e migliaia di esempi di immagini che rappresentano gatti e immagini che non rappresentano gatti. Quindi eseguiamo uno dei tanti algoritmi diversi con un processo matematico specifico e dettagliato per distinguere i gatti dal resto del mondo. Ma nel vocabolario tecnico, chiamiamo questo processo apprendimento . Quando il modello non riesce a rilevare un gatto in una nuova immagine perché si tratta di un leone e i leoni non erano nell'elenco originale dei gatti, spesso diciamo che il modello non ha capito i leoni.
</p>

<p align="justify">
In effetti, ogni volta che cerchiamo di spiegare qualcosa agli amici, spesso usiamo analogie con concetti condivisi che entrambi conosciamo. Poiché l'intelligenza artificiale e l'apprendimento automatico si concentrano ampiamente sulla replica delle capacità umane di svolgere compiti, le analogie spesso utilizzano un linguaggio che implica le funzioni cognitive letterali di un essere umano. Man mano che gli LLM dimostrano capacità a un livello prossimo a quello umano, queste analogie diventano più problematiche che utili, perché le persone le interpretano troppo a fondo e iniziano a credere che significhino più di quanto in realtà significhino.
</p>

<p align="justify">
Per questo motivo, faremo attenzione alle nostre analogie e metteremo in guardia il lettore dal seguirle troppo a lungo. Alcuni termini, come "apprendimento" , sono gergo tecnico che vale la pena comprendere, ma vogliamo che siate prudenti riguardo a ciò che potrebbero implicare. In alcuni casi, le analogie sono ancora utili in questo libro, ma cercheremo di essere espliciti sui limiti di come interpretarle.
</p>

<h3>1.5 Come gli esseri umani e le macchine rappresentano il linguaggio in modo diverso</h3>

<p align="justify">
Cosa significa rappresentare il linguaggio? Noi esseri umani iniziamo implicitamente a imparare a rappresentare il linguaggio poco dopo la nascita, attraverso l'interazione con gli altri e il mondo che ci circonda. Procediamo attraverso l'istruzione formale per sviluppare una comprensione delle componenti, delle strutture sottostanti e delle regole che governano il linguaggio e il suo uso. La nostra rappresentazione interna del linguaggio è stata ampiamente studiata. Mentre alcune leggi del linguaggio sono state scoperte, molte sono ancora oggetto di dibattito. La rappresentazione interna del linguaggio di ChatGPT si basa su parti di questa conoscenza. È abilitata utilizzando i concetti di reti neurali artificiali , note anche come deep learning (un'altra analogia pericolosa), che sono combinazioni di strutture dati e algoritmi che si basano vagamente sulle strutture del cervello umano. Tuttavia, la nostra comprensione del funzionamento della mente è incompleta. Mentre le reti neurali che alimentano gli LLM sono una mera semplificazione della struttura del cervello umano, la loro potenza risiede nella capacità di catturare e codificare il linguaggio in modo utile per generarlo e interagire con le persone.
</p>

<p align="justify">
Nota le astrazioni della struttura del cervello si sono dimostrate utili in molti ambiti. Le reti neurali hanno dimostrato incredibili progressi nel linguaggio, nella visione, nell'apprendimento e nel riconoscimento di pattern. La convergenza dei progressi negli algoritmi di apprendimento automatico neurale, l'estrema proliferazione di dati digitali e l'esplosione dell'hardware informatico, come le GPU, hanno portato ai progressi che rendono ChatGPT possibile oggi.
</p>

<p align="justify">
Il dettaglio cruciale da trarre da questa discussione è che tu, come essere umano, hai una comprensione innata del linguaggio che hai appreso nel tempo. Il tuo apprendimento e il tuo uso del linguaggio sono interattivi. Attraverso l'evoluzione, sembriamo tutti avere modi relativamente coerenti di apprendere e comunicare tra noi. Per saperne di più su questo concetto, esamina la teoria della grammatica universale introdotta dal linguista Noam Chomsky. A differenza delle persone, gli LLM hanno una rappresentazione del linguaggio che viene appresa attraverso un processo statico. Quando hai una conversazione con Claude o ChatGPT, quest'ultimo partecipa meccanicamente a un dialogo con te, nonostante non abbia mai partecipato a una conversazione prima.
</p>

<p align="justify">
La rappresentazione del linguaggio che un LLM apprende può essere di alta qualità, ma non è esente da errori. È manipolabile nel senso che possiamo alterare il comportamento degli LLM in modi specifici per limitare ciò di cui sono consapevoli o ciò che producono. Comprendere che gli LLM rappresentano il linguaggio utilizzando relazioni dedotte da esempi ci aiuta a mantenere aspettative realistiche. Se si intende utilizzare un LLM, quanto è pericoloso se è sbagliato? Come si può lavorare con la rappresentazione del linguaggio per costruire un prodotto o evitare un esito negativo? Queste sono alcune delle preoccupazioni di alto livello che discuteremo in questo libro.
</p>

<h3>1.6 Trasformatori preaddestrati generativi </h3>

<p align="justify">
Il termine "Generative Pretrained Transformer" è stato coniato da OpenAI per indicare un nuovo tipo di modello introdotto nel 2018 che incorpora un componente di rete neurale noto come trasformatore. Sebbene il modello GPT originale (GPT-1) non sia più utilizzato, i concetti fondamentali alla base del pre-addestramento e dei trasformatori sono diventati pilastri fondamentali della recente rivoluzione nell'intelligenza artificiale generativa e di strumenti come Claude, Gemini, Llama e Copilot.
</p>

<p align="justify">
È inoltre essenziale riconoscere che questi strumenti di intelligenza artificiale basati su GPT sono solo un esempio di un vasto dominio di ricerca algoritmica e applicazione degli LLM. Al di fuori del rilascio di ChatGPT, abbiamo osservato un'incredibile proliferazione di LLM. Alcuni LLM, come quelli rilasciati da EleutherAI e dal BigScience Research Workshop, sono liberamente disponibili al pubblico per promuovere la ricerca ed esplorare le applicazioni. Aziende come Meta, Microsoft e Google, come abbiamo accennato, hanno rilasciato altri LLM con termini di licenza più restrittivi. Gli LLM disponibili al pubblico che chiunque può utilizzare per creare un'applicazione o un sistema, a volte chiamati modelli di base , hanno creato una vivace comunità di ricercatori, appassionati e aziende che esplorano le applicazioni, i limiti e le opportunità creati dagli LLM e dall'intelligenza artificiale generativa. I concetti che insegniamo in questo libro si applicano quasi uniformemente a tutti gli LLM. Ognuno di questi produce output utilizzando strutture simili, se non identiche, a quelle presenti in ChatGPT.
</p>

<p align="justify">
Potrebbe sembrare impossibile che un solo libro contenga una sintesi generale applicabile a molti modelli. Tuttavia, è possibile per diverse ragioni, una delle più importanti è che non arriveremo al livello di dettaglio necessario per programmare un LLM da zero. Naturalmente, alcune parti di ChatGPT e di altri LLM commerciali rimangono segreti commerciali. Di conseguenza, il nostro ambito e le nostre descrizioni sono intenzionalmente generalizzati agli aspetti più comuni di tutti gli LLM generativi odierni.
</p>

<p align="justify">
Il secondo motivo per cui possiamo fornire una sintesi così ampiamente applicabile è la natura degli LLM. Sebbene sia vero che si possano apportare numerose modifiche al loro funzionamento e alla loro struttura, i ricercatori del settore riscontrano costantemente che i dettagli più importanti sono i seguenti:
</p>

<ul>
  <li>Quanto è grande il modello? È possibile ingrandirlo?</li>
  <li>Quanti dati sono stati utilizzati per costruire il modello? È possibile ottenerne di più?</li>
</ul>

<p align="justify">
Questi punti possono essere frustranti per i ricercatori che amano pensare di avere intuizioni o progetti vitali che migliorano significativamente il funzionamento e l'operatività di questi LLM perché, in molti casi, lo stesso miglioramento potrebbe essere ottenuto altrettanto facilmente "ingrandendolo" o costruendo un modello con più dati o più parametri. Aumentare le dimensioni sia dei modelli che dei pool di dati è una componente cruciale di molte preoccupazioni etiche relative all'utilizzo e alla costruzione di LLM, di cui parleremo nel capitolo 9 .
</p>

<h3>1.7 Perché gli LLM hanno così tanto successo</h3>

<p align="justify">
Nei prossimi capitoli discuteremo i dettagli del funzionamento degli LLM, ma vale anche la pena condividere qui una lezione chiave appresa studiando gli algoritmi di ML. Per molti anni, ottenere prestazioni migliori dal proprio algoritmo per qualsiasi compito si stesse cercando di svolgere significava spesso progettare in modo intelligente l'algoritmo stesso. Si studiava il problema, i dati e la matematica e si cercava di ricavare verità preziose sul mondo che si potevano poi codificare nell'algoritmo. Se si faceva un buon lavoro, le prestazioni miglioravano, si richiedevano meno dati e tutto andava bene. Molti algoritmi classici di deep learning di cui potreste aver sentito parlare, come le reti neurali convoluzionali (CNN) e le reti a memoria a lungo e breve termine (LSTM), sono, in generale, il risultato di un'attenta riflessione e di un'intelligenza artificiale. Anche gli algoritmi di ML più semplici e "superficiali", come XGBoost, che non si basano su reti neurali o deep learning, sono stati creati utilizzando una progettazione di algoritmi intelligente.
</p>

<p align="justify">
Gli LLM dimostrano una tendenza più recente. Invece di sviluppare algoritmi più complessi, li semplificano e implementano un algoritmo ingenuo che cattura semplicemente le relazioni tra le informazioni. Per molti versi, gli LLM hanno meno convinzioni sul mondo, forzatamente integrate nell'algoritmo. Fondamentalmente, questo offre maggiore flessibilità. Come potrebbe essere una buona idea se vi dicessi che l'approccio opposto è il modo in cui le persone hanno migliorato gli algoritmi? La differenza è che gli LLM e tecniche simili sono semplicemente più grandi, enormemente più grandi. Sono addestrati su molti più dati e con una capacità molto maggiore di catturare più relazioni tra più parole in più frasi; questo approccio basato sulla forza bruta sembra aver superato i metodi di apprendimento automatico classici in termini di prestazioni. Questa idea è illustrata nella figura 1.5 .
</p>

<table align="center">
  <td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 1.5 Se l'intelligenza di un algoritmo si basa sulla quantità di informazioni codificate nel progetto, le tecniche più datate spesso migliorano le prestazioni perché sono più intelligenti delle precedenti. Come si evince dalla dimensione dei cerchi, gli LLM hanno per lo più scelto un approccio "più stupido", utilizzando più dati e parametri e imponendo vincoli minimi su ciò che l'algoritmo può apprendere
      </p>
    </figcaption>
<img width="1100" height="531" alt="CH01_F05_Boozallen" src="https://github.com/user-attachments/assets/97cd6822-5b07-42ae-bf72-93f85d0850bc" />
  </figure>
</div>
    </td>
</table>

<p align="justify">
Come abbiamo già affermato, "più grande" non significa "migliore" in ogni parametro. L'implementazione di questi modelli rappresenta attualmente una sfida logistica e computazionale. Molti vincoli reali, tra cui tempo di risposta, consumo energetico, consumo della batteria e manutenibilità, ne risentono negativamente. Quindi, i LLM hanno migliorato solo una definizione ristretta di "prestazioni".
</p>

<p align="justify">
Tuttavia, vale la pena di riflettere sulla lezione sull'importanza di "ingrandirsi" piuttosto che "diventare intelligenti". A volte, nella progettazione di una soluzione di apprendimento automatico, anche se si utilizza un LLM, la risposta migliore potrebbe essere "Andiamo a raccogliere molti più dati".
</p>

<h3>1.8 LLM in azione: il bello, il brutto e lo spaventoso</h3>

<p align="justify">
In questo libro, forniremo esempi di come gli LLM possano fallire, spesso in modi esilaranti o ridicoli. Lo scopo di queste illustrazioni non è dire che gli LLM non siano in grado di svolgere un compito. Con modifiche all'input, alla configurazione o un colpo di fortuna, spesso è possibile far funzionare meglio gli LLM.
</p>

<p align="justify">
Lo scopo di queste illustrazioni è mostrarvi come gli LLM possano fallire, spesso su argomenti così semplici che un bambino potrebbe farli meglio. Mentre leggete questo libro e interagite con gli LLM, queste illustrazioni dovrebbero farvi riflettere e portarvi a pensare: "Se uso ChatGPT per un compito difficile, ma fallisce su quelli facili, mi sto preparando al fallimento?". La risposta può spesso essere un enfatico sì. ! Usare gli LLM in modo sicuro richiede un certo scetticismo o dubbio sui risultati, impegno per verificarne e convalidarne la correttezza e la capacità di adattarsi di conseguenza. Se usate un LLM per un compito che non potete svolgere da soli, rischiate di esporvi a risultati errati che non potete verificare personalmente. Continueremo ad approfondire questo punto e come affrontarlo nel corso del libro, mentre approfondiremo l'uso degli LLM.
</p>

<p align="justify">
È facile immaginare i molti modi in cui gli LLM possono potenzialmente semplificarci la vita quando funzionano: rispondere a tutte le email, riassumere documenti lunghi e spiegare nuovi concetti. Ciò che non viene naturale a molti è come le cose possano andare male e diventare rapidamente pericolose.
</p>

<p align="justify">
Questo tipo di pensiero antagonistico può spesso essere innescato da un esempio iniziale: diciamo che vuoi imparare a costruire una bomba. Se poni questa domanda a ChatGPT, ottieni la risposta edulcorata: "Mi dispiace, non posso aiutarti con questa richiesta. Se sei in crisi o hai bisogno di aiuto, contatta le autorità locali o i professionisti che possono aiutarti". Tuttavia, i ricercatori hanno recentemente dimostrato come far sì che ChatGPT e molti altri LLM commerciali rispondano alla domanda senza esitazione, tra le tante richieste di informazioni pericolose [4].
</p>

<p align="justify">
Si potrebbe sostenere che se qualcuno fosse così intelligente da capire come ingannare l'LLM, potrebbe probabilmente ottenere qualsiasi informazione pericolosa desideri da un'altra fonte. Questo è probabilmente vero, ma allo stesso tempo non tiene conto della portata dell'automazione negli LLM e negli strumenti di intelligenza artificiale generativa. Nessun algoritmo di intelligenza artificiale o apprendimento automatico è perfetto e, se milioni di persone pongono domande, gli LLM potrebbero produrre una risposta pericolosa nello 0,01% dei casi. ChatGPT ha oltre 100 milioni di utenti [5], quindi si tratta di 10.000 risposte pericolose. Il problema peggiora se si considera cosa un malintenzionato potrebbe iniziare ad automatizzare. Discuteremo questo problema più approfonditamente nella seconda parte del libro.
</p>

<p align="justify">
Non vediamo l'ora di unirti a noi per esplorare il funzionamento degli LLM. Alla fine, avrai una comprensione dettagliata di molti aspetti da considerare quando impieghi le rivoluzionarie potenzialità degli LLM nella tua attività o nella tua vita quotidiana.
</p>

<table align="center">
  <td>
    <h4>Riepilogo</h4>
    <ul>
      <li>
      ChatGPT è un tipo di modello linguistico di grandi dimensioni, che a sua volta rientra nella più ampia famiglia dell'intelligenza artificiale/apprendimento automatico generativo. I modelli generativi producono nuovi output e i LLM sono unici per la qualità del loro output, ma sono estremamente costosi da realizzare e utilizzare.
      </li>
      <li>
      Gli LLM si basano su una comprensione incompleta del funzionamento del cervello umano e dell'apprendimento linguistico. Questo viene utilizzato come ispirazione nella progettazione, ma non significa che i modelli abbiano le stesse capacità o debolezze degli esseri umani.
      </li>
      <li>
      L'intelligenza è un concetto sfaccettato e difficile da quantificare, il che rende difficile stabilire se gli LLM siano intelligenti. È più facile pensare agli LLM e al loro potenziale utilizzo in termini di capacità e affidabilità.
      </li>
      <li>
      Il linguaggio umano deve essere convertito da e verso la rappresentazione interna di un LLM. Il modo in cui questa rappresentazione viene formata cambierà ciò che un LLM apprende e influenzerà il modo in cui è possibile costruire soluzioni utilizzando gli LLM.
      </li>
    </ul>
  </td>
</table>







