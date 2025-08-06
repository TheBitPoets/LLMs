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

<h2>Tokenizzatori: come i grandi modelli linguistici vedono il mondo</h2>

<table align="center">
  <td>
    <h3>Questo capitolo copre</h3>
    <ul>
      <li>Creazione di token da frasi</li>
      <li>Controllo della dimensione del vocabolario con la normalizzazione</li>
      <li>Evitare i rischi nella tokenizzazione</li>
      <li>Strategie di tokenizzazione per rimuovere l'ambiguità</li>
    </ul>
  </td>
</table>

<p align="justify">
Come discusso nel capitolo 1, nel mondo dell'intelligenza artificiale è spesso utile trovare analogie con l'apprendimento umano per spiegare come le macchine "imparano". Il modo in cui leggiamo e comprendiamo le frasi è un processo complesso che cambia con l'età e coinvolge molteplici processi cognitivi sequenziali e simultanei [1]. I modelli linguistici di grandi dimensioni (LLM), tuttavia, utilizzano processi più semplici rispetto ai processi cognitivi umani. Impiegano algoritmi basati su reti neurali per catturare le relazioni tra le parole in grandi quantità di dati e quindi utilizzare queste informazioni sulle relazioni per interpretare e generare frasi.
</p>

<p align="justify">
La nostra analisi del funzionamento di questi algoritmi inizierà dal loro input: frasi di testo. In questo capitolo, esploreremo come l'LLM elabora queste frasi per trasformarle in input per il modello. Proprio come il linguaggio è fondamentale per il modo in cui si pensa e si elaborano le informazioni, gli input di un LLM sono cruciali nell'influenzare il tipo di concetti e compiti che gli LLM possono svolgere.
</p>

<h3>2.1 I token come rappresentazioni numeriche</h3>

<p align="justify">
Può sembrare ovvio che gli LLM debbano elaborare frasi, ma per comprenderlo appieno dobbiamo essere più specifici. Mentre parliamo del funzionamento degli LLM, vedremo che le frasi testuali sono innaturali per gli algoritmi delle reti neurali che li alimentano, perché le reti neurali utilizzano fondamentalmente numeri per svolgere il loro lavoro. Come mostrato nella figura 2.1 , gli algoritmi impiegati dagli LLM devono convertire il testo umano in una rappresentazione numerica prima di poterci lavorare. I token sono le rappresentazioni che gli LLM utilizzano per scomporre il testo in parti che possono essere codificate come numeri.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 2.1 Per comprendere il testo, gli LLM devono scomporre il testo in token. Ogni token univoco è associato a un identificatore numerico
      </p>
    </figcaption>
    
  ![CH02_F01_Boozallen](https://github.com/user-attachments/assets/027d0f48-fc83-4d18-9aa1-1995f950e04f)
 
  </figure>
</div>
  </td>
</table>

<p align="justify">
Si può pensare ai token come alla più piccola unità di testo elaborata da un LLM: un "atomo", se vogliamo, la parte più piccola da cui sono costruite tutte le altre cose. Quindi, cosa sono gli atomi del testo? Considerate questo: mentre leggete questo libro, quali sono i più piccoli elementi costitutivi che il vostro cervello usa per elaborare il significato? Due risposte naturali sono lettere e parole . È molto allettante definire le lettere come l'atomo, dato che le parole sono fatte di lettere, ma leggete consapevolmente ogni lettera in ogni parola? Per la maggior parte delle persone, la risposta è "no". (Se siete dislessici come uno dei coautori di questo libro, questa è una domanda bizzarra. Ma l'elaborazione cognitiva è complessa e non completamente compresa; abbiate pazienza con le analogie!) Osservate le parole e le parti di parola più importanti. In effetti, probabilmente non capirete questa frase anche se non abbiamo usato la giusta pronuncia o le lettere. Le persone utilizzano inconsciamente parti di parole per elaborare il testo e gli LLM sono costruiti utilizzando lo stesso principio.
</p>

<p align="justify">
In questo capitolo imparerai come funziona il processo di conversione del testo in token. Innanzitutto, analizzeremo i token in modo più dettagliato; poi, analizzeremo le procedure utilizzate per decidere come le frasi vengono convertite in token.
</p>

<h3>2.2 I modelli linguistici vedono solo i token</h3>

<p align="justify">
In età adulta, la maggior parte delle persone di lingua inglese conosce circa 30.000 parole [2]. GPT-3, l'LLM che inizialmente ha alimentato ChatGPT, ha un vocabolario di 50.257 token [3]. Questi token non sono parole, ma parti di parole denominate sotto-parole , una rappresentazione che si trova a metà strada tra parole e lettere. Intuitivamente, un token cattura l'unità semantica minima significativa della lingua . Ad esempio, la parola schoolhouseverrà spesso suddivisa in due token, schoole house, e la parola thoughtfulcome thoughte ful. Questo è utile per riconoscere parole frequenti e avere le sotto-parole per interpretare nuove parole che non abbiamo mai visto prima. Le persone spesso usano una tecnica simile, chiamata decomposizione semantica, per comprendere parole che non hanno mai visto prima. Intuitivamente scomponiamo le nuove parole in parti costituenti per coglierne il significato in base alle parole che già comprendiamo.
</p>

<p align="justify">
L'ingegneria delle feature è il processo di conversione dei dati in un formato più adatto all'algoritmo e al compito da svolgere. Per creare un algoritmo in grado di rilevare la lingua di un dato testo, è possibile scrivere codice che prenda il testo come input e restituisca la percentuale di volte in cui ciascun carattere compare. Ad esempio, se un carattere écompare spesso in un documento, si dispone di una buona funzionalità per indicare che è più probabile che il documento sia in spagnolo o francese piuttosto che in russo o cinese. Un'ingegneria delle feature efficace consiste nel riflettere attentamente sul funzionamento del modello, sugli obiettivi che si vogliono raggiungere e su come preparare i dati per la combinazione di modello e obiettivo.
</p>

<p align="justify">
La tokenizzazione è l'ingegneria delle funzionalità dei LLM; è di fondamentale importanza perché i token sono le uniche informazioni con cui un modello interagisce. I token sono visti come oggetti individuali e astratti, non intrinsecamente connessi. Le relazioni vengono apprese attraverso l'osservazione dei dati.
</p>

<p align="justify">
Tornando alla figura 2.1 , è evidente che i token per Dise dissono correlati, con l'unica differenza che uno inizia con la lettera maiuscola D. Tuttavia, si può vedere che il modello assegna l'identificatore \(4944\) a Dise l'identificatore \(834\) a dis. In altre parole, il modello non vede intrinsecamente alcuna connessione tra i token che rappresentano Dise dis, anche se noi, come esseri umani, vediamo una connessione ovvia. Il modello non vede Dis nemmeno o dis. Affinché un LLM elabori i token, dobbiamo convertirli in numeri in modo che il modello veda i numeri \(4944\) e \(834\) . È importante notare che il modello non ha alcun modo diretto per sapere se questi token sono correlati.
</p>

<p align="justify">
Un token è una mappatura da una sottoparola a una rappresentazione numerica univoca. A sua volta, la tokenizzazione è il processo di conversione di una stringa di testo completo in una sequenza di token. Se avete già utilizzato librerie di apprendimento automatico (in particolare strumenti di elaborazione del linguaggio naturale [NLP]), probabilmente avrete familiarità con alcune delle forme più semplici di tokenizzazione. Ad esempio, un semplice processo di tokenizzazione suddivide un testo in token suddividendolo in base agli spazi. Tuttavia, questo approccio limita la nostra capacità di creare sottoparole o di elaborare lingue che non utilizzano spazi vuoti per delimitare le parole, come il cinese.
</p>

<h3>2.2.1 Il processo di tokenizzazione</h3>

<p align="justify">
Il processo generico seguito dalla tokenizzazione è illustrato nella figura 2.2 con quattro passaggi chiave:
</p>

<ol>
  <li>
    <p align="justify">
    Ricezione del testo da elaborare : ciò significa ottenere un input di testo come stringtipo di dati (una raccolta di lettere, cifre o simboli) da un utente, da Internet o da qualsiasi altra fonte che contenga il testo desiderato.
    </p>
  </li>
  <li>
    <p align="justify">
    Trasformazione della stringa : spesso comporta la modifica della stringa in modo utile, ad esempio convertendo i caratteri maiuscoli in minuscoli. Questo potrebbe essere fatto anche per motivi di sicurezza (ad esempio, il testo proviene da un utente e dobbiamo rimuovere qualsiasi elemento che possa sembrare un input dannoso) o per eliminare variazioni irrilevanti nel testo per aiutare l'algoritmo a imparare meglio. Questo processo è noto come normalizzazione .
    </p>
  </li>
  <li>
    <p align="justify">
    Suddivisione della stringa in token : una volta disponibile, una stringa deve essere suddivisa in una sequenza di sottostringhe discrete; queste sono i token presenti nella stringa più grande. Questa operazione è detta segmentazione .
    </p>
  </li>
  <li>
    <p align="justify">
    Mappatura di ciascun token su un identificatore univoco : l'identificatore univoco è solitamente un numero intero, che produce un output comprensibile per l'LLM.
    </p>
  </li>
</ol>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 2.2 In generale, la tokenizzazione comporta l'elaborazione dell'input per produrre identificatori numerici per i token.
      </p>
    </figcaption>
    
<img width="1100" height="1095" alt="CH02_F02_Boozallen" src="https://github.com/user-attachments/assets/b089d58b-2398-477e-9f03-c27c56ca54e0" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
La prima e l'ultima parte di questo processo lasciano poco spazio a scelte o comportamenti diversi. Innanzitutto, è necessario un input da elaborare; infine, è necessario un identificatore numerico per ogni token per memorizzare e recuperare le informazioni che verranno associate a quel token. I due passaggi intermedi, normalizzazione e segmentazione, sono quelli in cui è possibile scegliere cosa fare.
</p>

<p align="justify">
L'ultimo passaggio del processo di tokenizzazione è la costruzione del vocabolario. Il vocabolario di un modello è il numero totale di token univoci rilevati durante l'addestramento, quando forniamo all'algoritmo i dati da cui apprendere. Per costruire un vocabolario ricco di token univoci, è quasi sempre necessaria una grande quantità di dati.

<p align="justify">
La scelta del vocabolario per un modello comporta una serie di compromessi: più ampio è il vocabolario, più informazioni il modello può elaborare correttamente. Si consideri un bambino di un anno con un vocabolario di poche decine di parole. Questo bambino non sarà un comunicatore molto efficace (ma va bene così: ha molto tempo per imparare). Quindi, un vocabolario più ampio non solo aiuta il modello a comprendere più cose, ma lo rende anche più grande. Se si dispone di un vocabolario troppo ampio, si potrebbe rallentare il modello a causa del numero di calcoli necessari per utilizzarlo, oppure il modello potrebbe consumare una quantità eccessiva di memoria o spazio su disco, il che renderebbe più difficile il trasferimento o la condivisione su altre macchine, ad esempio quando lo si distribuisce come parte di un'applicazione software.
</p>

<p align="justify">
Il vocabolario del modello si costruisce elaborando i dati di training e identificando i token. Ogni volta che si vede un nuovo token, gli si assegna un identificatore univoco in base al numero di token univoci visti. Questo processo è spesso semplice come memorizzare un contatore impostato su 0e incrementarlo ogni volta che viene trovato un nuovo token. Una volta completato il processo, si ottiene un tokenizzatore che è di fatto un codificatore . Il tokenizzatore può ricevere testo come input e restituire una codifica numerica di quel testo che gli algoritmi LLM possono utilizzare come output.
</p>

<h3>2.2.2 Controllo della dimensione del vocabolario nella tokenizzazione</h3>

<p align="justify">
GPT-NeoX, un LLM disponibile al pubblico, impiega circa 10 GB per memorizzare il suo vocabolario su disco. Si tratta di una grande quantità di dati, già abbastanza grande da rendere molti casi d'uso reali difficili dal punto di vista dell'archiviazione e del calcolo dei dati. È così grande che memorizzarlo su una scheda micro-SD sarebbe proibitivamente lento, rendendo l'utilizzo su un telefono cellulare o su alcune console di gioco una sfida significativa. È così grande da non poter essere trasmesso in streaming in tempo reale e deve essere scaricato e caricato nella RAM del processore per eseguire la tokenizzazione. Tuttavia, un vocabolario deve essere sufficientemente ampio da rappresentare tutte le parole e le sotto-parole che il modello incontrerà durante l'addestramento e l'utilizzo. Supponiamo che un modello incontri una parola che non è presente nel suo vocabolario e non può essere rappresentata combinando le sotto-parole del suo vocabolario. In tal caso, il modello non può acquisire informazioni su quel testo. Di conseguenza, è essenziale valutare le preoccupazioni relative alle dimensioni del vocabolario rispetto alla necessità dei modelli di interpretare un'ampia varietà di contenuti. Nella PNL, questo è spesso chiamato problema fuori dal vocabolario, quando ci imbattiamo in parole che non possiamo rappresentare utilizzando i token disponibili nel modello.
</p>

<p align="justify">
La dimensione del vocabolario è uno dei fattori che contribuiscono alla dimensione di un LLM, quindi è fondamentale discutere metodi e compromessi per controllarla. In questa sezione, descriveremo come la modifica del comportamento del processo di tokenizzazione possa influenzare la dimensione del vocabolario e influire sulle capacità e sull'accuratezza del modello.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 2.3 Il processo di normalizzazione solitamente comporta la modifica del testo per rimuovere i caratteri maiuscoli e la punteggiatura.
      </p>
    </figcaption>
<img width="1074" height="519" alt="CH02_F03_Boozallen" src="https://github.com/user-attachments/assets/4fe888ab-ca3e-49dd-b44d-97111f4375f5" />
  </figure>
</div>
  </td>
</table>

<p align="justify">
Nella figura 2.3 , ci concentriamo sul secondo passaggio di trasformazione, la normalizzazione, che converte i caratteri maiuscoli "H" e "W" in minuscoli e rimuove la punteggiatura. Questi comuni passaggi di normalizzazione hanno origine dalle pipeline NLP classiche e vengono talvolta eseguiti ancora oggi nei moderni approcci di deep learning. Hanno l'effetto immediatamente desiderabile di ridurre le dimensioni del vocabolario. Invece di dover rappresentare "Hello" e "hello" come due token separati, vengono mappati su un unico token univoco. Questa mappatura fa un'enorme differenza perché ogni parola che inizia una frase e viene scritta con la lettera maiuscola potenzialmente duplicherà una parola nel vocabolario con una versione maiuscola. Tale normalizzazione può anche aiutare con vari errori di battitura e di ortografia.
</p>

<p align="justify">
Ad esempio, durante la scrittura di questo libro, abbiamo digitato "LLMs", "LLms" e "llms", e abbiamo commesso vari altri errori di battitura con maiuscole e minuscole. Convertire ogni carattere in minuscolo in ogni variante risolve tutti questi errori di battitura in un'unica forma semplice, riducendo così il vocabolario e l'ambiguità.
</p>

<p align="justify">
Tuttavia, convertire il testo in minuscolo non sempre riduce l'ambiguità. Consideriamo "Bill" e "bill". Nel primo caso, l'uso delle maiuscole è fondamentale per capire che "Bill" è probabilmente il nome di qualcuno, mentre "bill" è più probabilmente un'unità di denaro (o una delle altre definizioni di "bill"). L'uso delle maiuscole è fondamentale non solo per comprendere il significato del testo, ma anche per comprenderne gli errori. Consideriamo ancora una volta tutti i vari modi in cui abbiamo scritto male le parole "LLM" in questo libro. Un algoritmo di intelligenza artificiale di alta qualità sarebbe in grado di riconoscere un errore di battitura e correggerlo! ChatGPT è in grado di farlo e quindi richiede l'uso delle maiuscole nel modello. Quindi c'è un importante compromesso da considerare tra la dimensione del vocabolario e la potenziale accuratezza del modello.
</p>

<p align="justify">
Nell'NLP classico e persino nei modelli di deep learning non così datati come BERT (un predecessore degli LLM che alimentano ChatGPT), la capacità di un algoritmo di riconoscere errori di battitura e correggerli era estremamente limitata al di fuori di soluzioni progettate esplicitamente per tale scopo. Per questo motivo, gran parte del lavoro che un tempo era necessario per progettare una solida fase di normalizzazione è stato scartato per gli LLM odierni. Un vocabolario più ampio è auspicabile per produrre modelli più capaci in grado di imparare a comprendere gli errori.
</p>

<h3>2.2.3 La tokenizzazione in dettaglio</h3>

<p align="justify">
Le fasi di normalizzazione e segmentazione nel processo di tokenizzazione determinano in larga misura la dimensione del vocabolario. Nella figura 2.4 , mostriamo una delle strategie più semplici per la tokenizzazione. Questa strategia segue una regola semplice: ogni volta che viene rilevato uno spazio nel testo, la stringa più grande viene suddivisa in quei token. Nel caso di "hello world", è facile come chiamare hello world.split( )in Python. Questo è un approccio ragionevole da adottare; è il modo in cui noi, come esseri umani, leggiamo le frasi. Ma aggiunge anche una sottile complessità.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 2.4 Il processo di segmentazione scompone il testo normalizzato in parole o token in modo che ciascuno possa essere elaborato in modo indipendente.
      </p>
    </figcaption>
<img width="1091" height="526" alt="CH02_F04_Boozallen" src="https://github.com/user-attachments/assets/0497417c-e6b3-44dd-a167-183c4edf2431" />
  </figure>
</div>
  </td>
</table>

<p align="justify">
Cosa succede quando si usa la punteggiatura nel testo? Se usiamo la nostra regola degli spazi vuoti per convertire la stringa "hello, world" in [hello,, world], ci imbattiamo in un problema simile a quello che si verifica con le maiuscole. Ci ritroviamo con due token distinti per lo stesso concetto: helloe hello,. L'approccio tradizionale spesso risolveva questo problema rimuovendo e sviluppando regole più complesse per suddividere le stringhe in token. Sebbene questo sia un passo nella giusta direzione verso la riduzione delle dimensioni del vocabolario, specificare manualmente le regole di tokenizzazione non risolve altri problemi. Ad esempio, le strategie di tokenizzazione basate su regole rappresentano un problema significativo per lingue come il cinese, che non utilizzano spazi per separare le parole.

<b>Identificazione delle sottoparole con codifica a coppie di byte</b>

<p align="justify">
Il tema generale degli LLM è quello di ridurre l'ingegneria delle funzionalità a mano e lasciare che siano gli algoritmi a svolgere il lavoro più pesante. Per questo motivo, per suddividere le stringhe in token viene in genere utilizzato un algoritmo noto come codifica a coppie di byte (BPE). La codifica a coppie di byte è un algoritmo per suddividere le parole in sequenze di caratteri di sottoparole comuni. Oggi, la BPE viene solitamente eseguita con un segmentatore personalizzato e praticamente senza normalizzazione.
</p>

<p align="justify">
Nota : sperimentalmente, abbiamo notato che molti prodotti simili a ChatGPT rimuovono alcuni caratteri Unicode che non vengono stampati (Unicode è strano), ma per il resto accettano il testo così com'è. La maggior parte dei modelli linguistici precedenti utilizza diverse tipologie di normalizzazione e, a nostro avviso, come normalizzare al meglio il testo per gli LLM è una questione aperta.
</p>

<p align="justify">
Poiché trovare l'insieme più efficiente di sottoparole è un compito computazionalmente costoso, BPE utilizza un'euristica per prendere una scorciatoia. Inizia esaminando le singole lettere come token e poi trova coppie di lettere adiacenti che ricorrono più frequentemente e le combina in token di sottoparole. L'algoritmo ripete questo processo molte volte, continuando con i token di sottoparole, finché non viene raggiunta una certa soglia e il vocabolario non è "sufficientemente piccolo". Ad esempio, nel primo passaggio, l'algoritmo BPE esamina la frequenza delle singole lettere usate in inglese e incontra le lettere "i", "n" e "g" vicine tra loro frequentemente. Nel primo passaggio, BPE potrebbe osservare che "n" e "g" ricorrono insieme più frequentemente di "i" e "n", quindi produrrà i token ie ng. In un passaggio successivo, potrebbe combinare quei token in ingbase alla frequenza di quella combinazione di lettere rispetto alla frequenza con cui "ng" ricorre con altre lettere o sottoparole. Una volta raggiunto il suo punto di arresto, BPE avrà identificato singole parole come "mangiare" e "bere" come combinazioni ricorrenti. Potrebbe anche catturare "ing" come suffisso, in modo che altre parole che terminano con quella sottoparola possano essere rappresentate come token. Una volta completato l'algoritmo, otterremo token che catturano parole complete e altri che catturano sottoparole. Questo processo è mostrato ad alto livello nella figura 2.5 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 2.5 Un algoritmo semplificato di codifica a coppie di byte per la creazione di token: innanzitutto, trovare la coppia di caratteri "ng" più frequente. Quindi, sostituire tutte le istanze di "ng" con un token segnaposto "T" e aggiungere "ng" al vocabolario. Ripetere il processo finché non rimangono più coppie di byte in comune.
      </p>
    </figcaption><img width="1100" height="469" alt="CH02_F05_Boozallen" src="https://github.com/user-attachments/assets/43b68798-ff04-4d79-9f7c-2b686efa2064" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Nota: eseguire l'algoritmo BPE per creare un vocabolario è sorprendentemente costoso perché deve leggere i dati di input molte volte per calcolare le combinazioni di lettere più frequenti. Mentre gli LLM vengono addestrati su oltre 500 milioni o addirittura 1 miliardo di pagine di testo, i loro tokenizzatori vengono solitamente creati utilizzando un piccolo sottoinsieme di quei dati. Spesso, un tokenizzatore viene addestrato utilizzando una raccolta di testo molto più piccola, delle dimensioni di un romanzo.
</p>

<p align="justify">
Il processo BPE può sembrare strano a prima vista, ma è possibile considerarlo un modo per identificare stringhe comuni in un corpus. Ad esempio, BPE imparerà quasi sempre a rappresentare New Yorkun singolo token, il che è utile poiché lo stato e la città di New York sono ricorrenti nel testo. Rappresentare l'intero concetto come un singolo token semplifica l'utilizzo di questo tipo di informazioni. Infatti, la maggior parte delle parole comuni diventeranno token univoci, mentre le parole rare saranno, si spera, catturate come una combinazione di sotto-parole. Ad esempio, loquacioussaranno tokenizzate da GPT-4 come lo, qu, e acious. Questo metodo è un successo perché "acious" è un suffisso latino per inclinazione/propensione, rendendo più facile per il modello gestire correttamente una parola insolita. È anche un caso di fallimento perché il prefisso latino " loqu" è stato suddiviso in due token invece di uno, rendendo più difficile l'apprendimento.
</p>

<p align="justify">
Dopo aver utilizzato BPE per creare un vocabolario, gli autori del modello aggiungono manualmente token aggiuntivi per vari motivi, ad esempio parole importanti per uno specifico dominio di conoscenza. Come discuteremo nella prossima sezione, in alcuni domini, avere i token corretti ha un effetto significativo, catturando sfumature di significato. Spesso, gli autori si assicurano che i token necessari siano inclusi. Gli autori del modello aggiungono anche token speciali che non rappresentano direttamente parti di parole, ma forniscono informazioni ausiliarie al modello. Alcuni esempi comuni sono il token "sconosciuto" (tipicamente rappresentato come [UNK]), che viene utilizzato se il tokenizzatore non riesce a elaborare correttamente un simbolo, e il token di sistema [SYSTM], che viene utilizzato per distinguere tra il prompt integrato di un modello e i dati inseriti dall'utente, nonché altri tipi di marcatori stilistici. I modelli multimodali che accettano input di testo e immagini utilizzano token univoci per indicare al modello quando il flusso di input passa da byte che rappresentano dati di testo a byte che rappresentano dati di immagine.
</p>

<p align="justify">
Open AI ha deciso di utilizzare BPE per codificare il testo in token quando ha sviluppato ChatGPT e ha rilasciato il suo tokenizzatore come pacchetto open source tiktoken( https://github.com/openai/tiktoken ). Tuttavia, sono disponibili diversi altri algoritmi e implementazioni per la generazione automatica di token, inclusi gli algoritmi WordPiece e SentencePiece sviluppati da Google [4]. Ognuno di questi presenta diversi compromessi. Ad esempio, WordPiece utilizza una tecnica diversa per contare la frequenza delle sotto-parole candidate durante la creazione del vocabolario del tokenizzatore. Uno degli algoritmi implementati in SentencePiece elabora intere frasi, preservando gli spazi vuoti durante il calcolo dei token, il che può migliorare l'output durante la creazione di modelli che gestiscono più lingue. Tuttavia, BPE è l'algoritmo più ampiamente utilizzato. Ad esempio, ora è utilizzato esclusivamente nei recenti LLM di Google.
</p>

<p align="justify">
Indipendentemente dall'algoritmo scelto, la dimensione del vocabolario di un tokenizzatore è un parametro critico del modello, determinato dal data scientist o dall'ingegnere incaricato dell'addestramento e dell'ampliamento del tokenizzatore. Le sezioni seguenti approfondiscono alcune considerazioni sulla dimensione del vocabolario e altre decisioni prese durante il processo di sviluppo del tokenizzatore.
</p>

<h3>2.2.4 I rischi della tokenizzazione</h3>

<p align="justify">
Come accennato nel capitolo 1, in questo libro non approfondiremo molto la codifica. L'obiettivo è fornirvi una comprensione ragionevole del funzionamento degli LLM e rimuovere parte della magia e del mistero, in modo che possiate concentrarvi su come gli LLM possono essere utilizzati per il vostro lavoro. La tokenizzazione è il primo tassello del puzzle. È una strategia semplice ma efficace per produrre gli input per gli LLM. Avete imparato come la dimensione del vocabolario giochi un ruolo significativo nella distribuibilità di un modello, il compromesso tra il riconoscimento delle sfumature e l'inutile ridondanza associata alla creazione di un vocabolario, come il processo di tokenizzazione influenzi la dimensione del vocabolario e come il processo di selezione dei token possa essere automatizzato con BPE.
</p>

<p align="justify">
Le scelte effettuate al momento della tokenizzazione influenzano ciò che gli LLM possono fare oggi e ciò che li influenzerà in futuro. Queste scelte comportano alcune sfide di ampio respiro di cui essere consapevoli. Per approfondire questo argomento, vale la pena condividere due dettagli salienti ma sfumati del BPE: la relazione tra lunghezza delle frasi e numero di token e il rischio che gli LLM vengano confusi da caratteri, noti come omoglifi, che appaiono identici ma hanno codifiche binarie diverse.
</p>

<p align="justify">
Le frasi più lunghe non significano più gettoni
Un aspetto poco intuitivo del BPE è che frasi più lunghe non implicano più token. Per capirne il motivo, guarda la figura 2.6 , dove mostriamo una tokenizzazione reale di due stringhe diverse tramite GPT-3. La stringa "I'm running" è più lunga di un carattere rispetto alla stringa "I'm runnin", ma è più corta di un token! Se non ci credi, puoi provare a tokenizzare stringhe diverse su  https://platform.openai.com/tokenizer .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
     Figura 2.6 Tokenizzazione di due frasi diverse
      </p>
    </figcaption>
    <img width="1100" height="409" alt="CH02_F06_Boozallen" src="https://github.com/user-attachments/assets/b833c1c2-2268-4814-ae75-b3b8e9fa7599" />
  </figure>
</div>
  </td>
</table>

<p align="justify">
Questa discrepanza si verifica perché BPE è alla ricerca avida del set più piccolo di token per qualsiasi input. In questo caso specifico, la stringa "running" ricorre abbastanza frequentemente nei nostri dati di addestramento da ottenere un token a sé stante. Nel caso in cui manchi la "g", non esiste alcun token per "runnin" nel nostro vocabolario, perché tale variante potrebbe essere apparsa raramente nei nostri dati di addestramento. Pertanto, "runnin" deve essere suddiviso in almeno due token, ottenendo rune nin.
</p>

<p align="justify">
Questa sfumatura dell'implementazione del tokenizzatore è terreno fertile per bug software. Diversi tokenizzatori possono fornire risposte diverse su come tokenizzare la stessa stringa. Quando si progettano test unitari e infrastrutture, questo fattore è importante da tenere a mente per evitare di perdersi o confondersi durante l'aggiornamento o la conversione tra implementazioni di tokenizzatori, che potrebbero causare nuove differenze nella generazione di token. Può anche influire sulle valutazioni degli LLM, poiché molti modelli sono altamente sensibili agli spazi vuoti aggiunti e una tokenizzazione incoerente può inavvertitamente portare a confronti non coerenti.
</p>

<b>Gli omoglifi creano confusione</b>

<p align="justify">
Gli omoglifi sono un problema che gli sviluppatori possono incontrare quando lavorano con più lingue umane o quando considerano le implicazioni per la sicurezza dell'elaborazione di dati forniti esternamente. Quando l'input proviene da utenti arbitrari, a volte può essere dannoso e voler ingannare il modello inducendolo a comportarsi in modo scorretto. Un modo per contrastare un LLM è un attacco omoglifico .
</p>

<p align="justify">
Un omoglifo si verifica quando due o più caratteri hanno codifiche di byte diverse ma appaiono identici quando vengono visualizzati sullo schermo. Un esempio è la lettera latina "H", utilizzata nella maggior parte delle lingue dell'Europa occidentale, e la "H" cirillica, utilizzata in tutta l'Europa orientale e l'Asia centrale.
</p>

<p align="justify">
BPE codificherà gli omoglifi che utilizzano codifiche di byte diverse in token diversi. Di conseguenza, gli omoglifi possono aumentare il numero di token in un testo, modificare il modo in cui un LLM analizza le informazioni e aumentare i costi di elaborazione. Un esempio divertente di omoglifo è il carattere Unicode U+200B, noto anche come "spazio a larghezza zero". Questo carattere viene utilizzato nella composizione tipografica e occupa spazio, ma non stampa nulla, non mostra nulla e non modifica in alcun modo la resa di un documento.
</p>

<p align="justify">
Lo spazio di larghezza zero è una delle tante cose strane e interessanti presenti nelle specifiche Unicode e potrebbe essere usato per creare problemi. Molti servizi impiegano quindi passaggi di normalizzazione che rimuovono questi caratteri strani e sostituiscono gli omoglifi con una rappresentazione canonica (ovvero, qualsiasi cosa che assomigli a una "a" deve essere codificata come a). Ad esempio, l'attuale interfaccia del tokenizzatore di OpenAI rimuoverà gli omoglifi. È necessario considerare gli omoglifi se si desidera implementare un LLM sul proprio hardware o sul dispositivo di un utente.
</p>

<h3>2.3 Capacità di tokenizzazione e LLM</h3>

<p align="justify">
Se ci interessa solo la capacità di un LLM di produrre testo di alta qualità, simile a quello umano, i dettagli specifici di come tokenizzare il testo non sono importanti quanto i dati e il calcolo utilizzati per costruire questi modelli. Se si investe in potenza di calcolo e scalabilità sufficienti nei modelli, questi alla fine troveranno rappresentazioni utili indipendentemente dai componenti costitutivi. A volte, però, la tokenizzazione influisce notevolmente sulle capacità di un LLM. In questa sezione, ne esamineremo alcuni esempi.
</p>

<p align="justify">
Potrebbe darsi che gli esempi che seguono non siano direttamente pertinenti al tuo lavoro o a ciò che vorresti fare con un LLM. Va benissimo; lo scopo di questi esempi non è dissuaderti dall'utilizzare un LLM. Piuttosto, l'obiettivo è aiutarti a comprendere che la portata di ciò che gli LLM apprendono è limitata dalla rappresentazione scelta e che potrebbe non esserci un modo per aggirare queste preoccupazioni senza un importante lavoro di ingegneria. Se inizi a sviluppare un'applicazione con LLM e riscontri difficoltà significative, pensa a come la tokenizzazione potrebbe essere un fattore determinante per il tuo obiettivo. Se la tokenizzazione è effettivamente il problema, c'è poco che tu possa fare per risolverlo, quindi potrebbe essere meglio considerare altri approcci, come l'ampliamento manuale del vocabolario con token importanti per la tua applicazione.
</p>

<h3>2.3.1 Gli LLM sono scarsi nei giochi di parole</h3>

<p align="justify">
Gli utenti amano spesso chiedere agli LLM di risolvere enigmi o di svolgere compiti che coinvolgono giochi di parole. Ad esempio, la figura 2.7 mostra un gioco di parole in cui la risposta corretta dipende dall'esatta sequenza di lettere e dal numero di lettere in una parola.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 2.7 L'approccio basato sulla tokenizzazione implica che ChatGPT non possa realmente "vedere" singoli caratteri o lunghezze di parola. Se si pongono domande che richiedono l'identificazione di sottocaratteri e li si modifica in modo univoco e insolito, ChatGPT inizia a non funzionare. Il carattere centrale corretto è "a", ma ChatGPT insiste che la lettera sia "e". Ciò che ChatGPT vede sono tre token, che rappresentano rispettivamente P, ine, e apple.
      </p>
    </figcaption>
    
![CH02_F07_Boozallen](https://github.com/user-attachments/assets/70c53a2b-2904-4b3d-b5d6-e64588f46be8)
  
  </figure>
</div>
  </td>
</table>

<p align="justify">
Giocare a giochi di parole potrebbe non essere un aspetto che ti interessa per la tua candidatura, ma il motivo per cui falliscono potrebbe essere molto rilevante per il tuo problema. Sebbene molti esempi come questo siano problemi di tipo "giocattolo", in quanto non particolarmente importanti dal punto di vista scientifico o commerciale, rivelano notevoli falle nel funzionamento di questi modelli. Possono entrare in gioco in usi più pratici, come quando i modelli hanno difficoltà a scrivere poesie contenenti rime o assonanze.
</p>

<p align="justify">
Si supponga, ad esempio, di voler creare un'applicazione che risponda a domande sui farmaci prescritti a un utente. I farmaci hanno spesso nomi lunghi e confusi che le persone non riescono a ricordare o scrivono in modo errato e, poiché un LLM non riconosce le lettere, potrebbe confondere il nome di un farmaco con il nome lungo e strano di un altro farmaco.
</p>

<p align="justify">
Poiché i nomi dei farmaci sono poco comuni, la tokenizzazione sarà diversa, anche in caso di piccoli errori di ortografia. Ad esempio, in GPT-3, "Amoxicillina" e il semplice errore di ortografia "Amoxicillan" non hanno token in comune! Questo crea un rischio molto maggiore che l'LLM risponda in modo errato, dove il rischio è intrinsecamente più elevato, rendendo ancora più importante testare a fondo una domanda LLM, elaborarla con estrema cura o potenzialmente evitarla del tutto.
</p>

<h3>2.3.2 Gli LLM sono sfidati dalla matematica</h3>

<p align="justify">
La tokenizzazione influisce in modo significativo sui compiti che implicano il ragionamento simbolico formale, tra cui la matematica e i giochi da tavolo. Sia la matematica che i giochi da tavolo vengono implementati dagli LLM come problemi di ragionamento simbolico in cui i singoli token hanno regole specifiche che governano le loro interazioni e il loro significato quando osservati insieme ad altri token. Ad esempio, i modelli che contengono singoli token per ogni cifra tendono ad avere prestazioni aritmetiche migliori rispetto ai modelli che non li contengono. Questo perché il numero 123456 diventerà due token in GPT-3, [, ]in base alla frequenza di tali token nei dati di addestramento originali del tokenizzatore. Ciò rende più difficile per il modello gestire le singole cifre di quel numero. Alcuni sviluppatori di sistemi hanno risolto questo problema normalizzando i numeri inserendo spazi tra tutte le cifre, come 1 2 3 4 5 6, che crea un nuovo output con sei token, uno per ogni cifra.
</p>

<p align="justify">
Questa differenza nelle capacità matematiche è ben illustrata nella figura 2.8 , che mostra le prestazioni nei calcoli aritmetici durante l'addestramento. La curva superiore è un tipico tokenizzatore BPE, mentre la curva inferiore, che mostra prestazioni migliori, è lo stesso tokenizzatore modificato per avere la tokenizzazione a livello di cifra dei numeri.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 2.8 Confronto tra il modo in cui due LLM imparano a eseguire calcoli aritmetici nel tempo. Il tempo è mostrato sull'asse x. La curva superiore è un tipico tokenizzatore BPE, mentre la curva inferiore è lo stesso tokenizzatore modificato per utilizzare token che rappresentano singole cifre. L'asse y descrive la capacità dell'LLM di eseguire calcoli matematici con accuratezza, dove un numero inferiore significa meno errori. In conclusione, gli LLM che utilizzano la tokenizzazione a livello di cifra possono imparare a fare calcoli matematici meglio e più velocemente.
      </p>
    </figcaption>
    
  <img width="1100" height="387" alt="CH02_F08_Boozallen" src="https://github.com/user-attachments/assets/35c22179-e36c-438f-ad25-644d650f3503" />

  </figure>
</div>
  </td>
</table>

<h3>2.3.3 LLM ed equità linguistica</h3>

<p align="justify">
La maggior parte dei tokenizzatori LLM può rappresentare qualsiasi simbolo coperto da Unicode, che include i caratteri della maggior parte degli alfabeti del mondo. Tuttavia, l'efficienza con cui questi tokenizzatori rappresentano il testo in una determinata lingua varia notevolmente, soprattutto perché i tokenizzatori vengono in genere addestrati su raccolte più piccole di risorse testuali per lingue diverse. Ciò può causare una sostanziale iniquità nei servizi commerciali basati su LLM [5], poiché la tokenizzazione di parole in lingue rare nel set di addestramento si basa di default su un insieme più granulare di sottoparole, con conseguente aumento dell'utilizzo dei token. I fornitori commerciali di LLM come OpenAI e Anthropic in genere addebitano ai clienti un costo per token, solitamente una frazione di centesimo per ogni token immesso nell'LLM e prodotto come output dall'LLM. Questi costi si sommano se si considera che un'applicazione commerciale ad alto utilizzo può elaborare decine di milioni di token al giorno.
</p>

<p align="justify">
Il tempo impiegato da un LLM per completare una richiesta e l'importo addebitato a un utente per token dipendono direttamente dal tokenizzatore. Pertanto, le lingue rappresentate in modo più efficiente tramite un tokenizzatore sono economicamente incentivate rispetto a quelle che non lo sono. Utilizzando l'inglese come base di partenza, i ricercatori hanno scoperto che il costo per rispondere a una query di un utente in tedesco o italiano è di circa il 50% superiore quando si utilizzano ChatGPT e GPT-4. Lingue che differiscono in modo ancora più sostanziale dall'inglese possono comportare costi molto più elevati: il tumbuka e il bulgaro costano più del doppio, mentre dzongkha, oriya, santali e shan costano oltre 12 volte di più dell'inglese.
</p>

<h3>2.4 Verifica la tua comprensione</h3>

<ol>
  <li>
    <p align="justify">
  Come ti aspetti che le seguenti parole o frasi vengano tokenizzate? Prova a estrarle tu stesso e poi a eseguirle tramite un vero tokenizzatore LLM, come quello disponibile su https://platform.openai.com/tokenizer :
  </p>
  <ul>
   <li>
     sostenuto
   </li> 
    <li>
      grandi modelli linguistici
    </li>
    <li>
      Scuola
    </li>
    <li>
      Il modo in cui elaboriamo le frasi per comprenderle è un processo complesso che cambia con l'età e coinvolge molteplici processi cognitivi sequenziali e simultanei.
    </li>
  </ul>
    <li>
    Quanto pensi che sia importante la differenza tra maiuscole e minuscole in ciascuno degli esempi precedenti? Prova a riproporli con diverse maiuscole e minuscole.
    </li>
    <li>
    Simuliamo il modo in cui gli studenti LLM pensano alla matematica usando un cifrario in cui ogni lettera inglese corrisponde a un numero. Ad esempio, \(W=8\) , \(A=4\) , \(I=7\) e \(T=2\) , quindi scriveremmo WAIT per indicare \(8472\) . Sapendo questo fatto e che \(GO+SLOW=STOP\) , riesci a capire cosa rappresenta \(STOP\) ?
    </li>
    <li>
      Dal momento che un token è l'unità di base su cui opera un LLM, perché ha senso (dal punto di vista tecnologico) che i linguaggi rappresentati in modo meno efficiente da un tokenizzatore costino di più?
    </li>
    <li>
È un problema etico che gli LLM applichino prezzi diversi per lo stesso servizio a seconda della lingua parlata? Lo considereresti una discriminazione?
    </li>
</ul>
</li>  
</ol>

<h3>2.5 Tokenizzazione nel contesto</h3>

<p align="justify">
I dettagli della tokenizzazione che analizzeremo in questo capitolo costituiscono gli elementi fondamentali degli LLM, che regolano l'input che possono rappresentare efficacemente e l'output che producono. La tokenizzazione è una componente fondamentale di LLM come ChatGPT nello sviluppo di rappresentazioni efficaci del testo, in modo che possano essere utilizzate per apprendere le relazioni tra token quando vengono presentate grandi quantità di informazioni nel processo di formazione, interpretando l'input dell'utente e producendo le risposte di alta qualità a cui siamo abituati. Il potenziale di un LLM è limitato o favorito dalla strategia di tokenizzazione e dal vocabolario che impiega, insieme a tutte le altre caratteristiche che esploreremo nei capitoli seguenti.

<h3>Riepilogo</h3>

<ul>
  <li>
    <p align="justify">
    La tokenizzazione è il processo fondamentale che gli LLM utilizzano per comprendere il testo convertendo le frasi in token.
    </p>
  </li>
  <li>
    <p align="justify">
    I token sono le più piccole unità di informazione in un testo che ne rappresentano il contenuto. A volte corrispondono a parole complete, ma spesso rappresentano frammenti di parole o sotto-parole.
    </p>
  </li>
  <li>
    <p align="justify">
    La tokenizzazione implica la normalizzazione del testo in una rappresentazione standard, che può comportare la conversione dei caratteri in minuscolo o la traduzione della codifica in byte dei caratteri Unicode in modo che caratteri visibilmente identici utilizzino la stessa codifica.
    </p>
  </li>
  <li>
    <p align="justify">
    La tokenizzazione implica anche la segmentazione , ovvero la scomposizione del testo in parole o sotto-parole. Algoritmi come la codifica a coppie di byte (BPE) forniscono un meccanismo per apprendere automaticamente come segmentare in modo efficiente il testo in base alla ricorrenza statistica di combinazioni di lettere in un set di dati di addestramento.
    </p>
  </li>
  <li>
    <p align="justify">
    Il risultato della creazione di un tokenizzatore è noto come vocabolario , ovvero la raccolta unica di token di parole e sottoparole che un tokenizzatore può utilizzare per rappresentare il testo che ha elaborato.
    </p>
  </li>
  <li>
    <p align="justify">
    La dimensione del vocabolario di un tokenizzatore influisce sulla capacità dell'LLM di rappresentare accuratamente i dati e sulle risorse di archiviazione e di calcolo necessarie per comprendere e prevedere il testo.
    </p>
  </li>
  <li>
    <p align="justify">
    Internamente all'LLM, i token sono rappresentati tramite numeri. Di conseguenza, non si comprende la relazione tra i token, come prefissi e suffissi, o il fatto che due token condividano un insieme simile di lettere.
    </p>
  </li>
  <li>
    <p align="justify">
    Per supportare specifici domini di conoscenza, i tokenizzatori addestrati automaticamente possono essere potenziati per fornire token importanti per la loro applicazione.
    </p>
  </li>
  <li>
    <p align="justify">
   I tokenizzatori che non comprendono singole lettere o cifre avranno problemi con le operazioni aritmetiche o con semplici giochi di parole.
    </p>
  </li>
</ul>

<h2>3 Trasformatori: come gli ingressi diventano uscite</h2>

<table align="center">
  <td>
    <h3>Questo capitolo copre</h3>
    <ul>
      <li>
          Conversione di token in vettori
      </li>
      <li>
     Transformers, i loro tipi e i loro ruoli   
      </li>
      <li>
       Conversione dei vettori in token 
      </li>
      <li>
        Creazione del ciclo di generazione del testo
      </li>
</ul>
  </td>
</table>

<p align="justify">
Nel capitolo 2, abbiamo visto come i modelli linguistici di grandi dimensioni (LLM) considerino il testo come unità fondamentali note come token. Ora è il momento di parlare di cosa fanno gli LLM con i token che vedono. Il processo che gli LLM utilizzano per generare il loro testo è notevolmente diverso da quello con cui gli esseri umani formano frasi coerenti. Quando un LLM opera, lavora sui token, ma allo stesso tempo non può manipolarli come fanno gli esseri umani perché l'LLM non comprende la struttura e la relazione tra le lettere che ogni token rappresenta.
</p>

<p align="justify">
Ad esempio, chi parla inglese sa che le parole "magia", "magico" e "mago" sono tutte correlate. Possiamo capire che le frasi che contengono queste parole siano tutte collegate allo stesso argomento perché condividono una radice comune. Tuttavia, gli LLM che operano su numeri interi che rappresentano i token che compongono queste parole non possono comprendere le relazioni tra i token senza un lavoro aggiuntivo per stabilire tali connessioni.
</p>

<p align="justify">
Per questo motivo, gli LLM vantano una lunga tradizione nell'ambito dell'apprendimento automatico e del deep learning, eseguendo una sorta di conversione ciclica. Innanzitutto, i token vengono convertiti in una forma numerica su cui gli algoritmi di deep learning possono lavorare. Successivamente, l'LLM riconverte questa rappresentazione numerica in un nuovo token. Questo ciclo si ripete iterativamente, il che non è paragonabile al funzionamento umano. Sareste incredibilmente preoccupati se i vostri colleghi dovessero tirare fuori una calcolatrice per risolvere diversi problemi matematici tra una parola e l'altra.
</p>

<p align="justify">
Eppure, questo processo è, in effetti, il modo in cui gli LLM producono output. In questo capitolo, lo analizzeremo in due fasi. In primo luogo, esamineremo l'intero processo a un livello più alto per introdurre concetti fondamentali e costruire un modello mentale di come gli LLM generano testo. In secondo luogo, questo modello servirà da impalcatura per una discussione più approfondita dei dettagli e delle scelte progettuali associate ai componenti che gli LLM utilizzano per catturare le relazioni tra parole e linguaggio e, in definitiva, generare l'output con cui abbiamo familiarità.
</p>

<h3>3.1 Il modello del trasformatore</h3>

<p align="justify">
Molti LLM che si incontrano oggi interpretano i token e producono output utilizzando un'architettura software nota come trasformatore. Questa architettura consiste in un insieme di algoritmi e strutture dati che memorizzano le informazioni rappresentandole come numeri in una rete neurale. In sostanza, i trasformatori sono algoritmi di predizione di sequenze. Sebbene sia comune descriverli come linguaggio di "ragionamento" o di "comprensione", ciò che in realtà fanno è predire i token. I trasformatori offrono tre diversi approcci alla predizione dei token. Mentre ci concentriamo sulla famosa architettura GPT (più formalmente nota come modelli solo decodificatore), vale la pena introdurre anche i modelli solo codificatore e codificatore-decodificatore:
</p>

<ul>
  <li>
    <p align="justify">
Modelli basati solo su codificatore : questi modelli sono progettati per creare rappresentazioni della conoscenza che possono essere utilizzate per eseguire attività, ovvero per codificare l'input in una rappresentazione numerica più utile per un algoritmo. Il modo migliore per considerarli è che prendono il testo e lo elaborano in una forma più facile da utilizzare per un algoritmo di apprendimento automatico. Sono ampiamente utilizzati nella ricerca scientifica. Esempi famosi includono BERT e RoBERTa.
    </p>
  </li>
  <li>
    <p align="justify">
Modelli "decoder-only" — Questi modelli sono progettati per generare testo. Il modo migliore per immaginarli è che prendano un documento parzialmente scritto e ne producano una probabile continuazione prevedendo il token successivo. Esempi famosi includono GPT di OpenAI e Gemini di Google.
    </p>
  </li>
  <li>
    <p align="justify">
Modelli di codifica-decodifica — Questi modelli sono progettati anche per generare testo. A differenza dei modelli di sola decodifica, prendono un intero passaggio di testo e creano un passaggio corrispondente anziché continuare quello esistente. Sono meno popolari dei modelli di sola decodifica perché sono più costosi da addestrare e il loro utilizzo è talvolta più impegnativo. Per attività con una sequenza di input e output chiaramente definita, i modelli di codifica-decodifica tendono a superare i modelli di sola decodifica. Ad esempio, sono molto più efficaci nelle attività di traduzione e riassunto rispetto ai modelli di sola decodifica. Esempi famosi includono T5 e l'algoritmo alla base di Google Translate.
    </p>
  </li>
</ul>

<p align="justify">
Indipendentemente dal tipo di trasformatore utilizzato, i componenti essenziali del modello sono costituiti da tre strati base, disposti internamente in modo diverso. Un'analogia ragionevole alla loro intercambiabilità è quella dei motori delle auto a benzina: funzionano tutti in modo simile e hanno gli stessi componenti generali. Il modo in cui questi componenti (leggi: strati) sono assemblati all'interno del motore (leggi: trasformatore) determina diversi compromessi in termini di prestazioni.
</p>

<table align="center">
  <td>
    <h4>Cos'è esattamente uno strato di rete neurale?</h4>
    <p align="justify">
Gli LLM sono uno delle centinaia di algoritmi che oggi chiamiamo reti neurali . Tuttavia, questa denominazione è impropria sotto diversi aspetti. In primo luogo, ciò che oggi costituisce un approccio basato sulle reti neurali è molto ampio, al punto che fare riferimento a un "approccio basato sulle reti neurali" non fornisce al lettore troppe informazioni sull'approccio esatto descritto. In secondo luogo, la parte neurale del nome ha poco o nulla a che fare con le neuroscienze o con il funzionamento del cervello. A volte, c'è un'ispirazione intuitiva del tipo "Ehi, il cervello fa più o meno questo; possiamo imitare quel comportamento e trarne qualcosa di utile?", ma non per la maggior parte dei metodi attuali. In terzo luogo, una rete neurale descrive più un accordo standard sull'assemblaggio di strutture dati che un algoritmo specifico. Pensate alla costruzione di una casa: usate assi di legno, cartongesso e molte opzioni per mobili, vernici e scelte di design per assemblare tutto in una casa. Ogni casa ha un aspetto unico ma anche familiare: sono tutte assemblate in modo prevedibile. Il "livello" di una rete neurale è il componente più piccolo, ma è possibile utilizzare molti tipi di livelli in modi diversi. I trasformatori sono solo uno dei tanti elementi che vengono assemblati in una rete più ampia
    </p>
  </td>
</table>

<h3>3.1.1 Strati del modello del trasformatore</h3>

<p align="justify">
La figura 3.1 descrive i componenti essenziali del modello del trasformatore: lo strato di incorporamento , che genera rappresentazioni di token che possono contenere più significato; lo strato del trasformatore , che effettua previsioni basate sulle relazioni tra le parole; e lo strato di output , che trasforma le rappresentazioni numeriche utilizzate all'interno del trasformatore in parole che gli esseri umani possono leggere.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.1 I componenti di base del modello del trasformatore, costituiti dallo strato di incorporamento, da più strati del trasformatore e dallo strato di uscita
      </p>
    </figcaption>
    
<img width="1100" height="288" alt="CH03_F01_Boozallen" src="https://github.com/user-attachments/assets/0377d1bd-b430-4561-b392-89f3eebeffc9" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Diamo un'occhiata più in dettaglio a questi strati:
</p>

<ul>
  <li>
  <p align="justify">
Livello di incorporamento — Il livello di incorporamento accetta i token grezzi come input e li mappa in rappresentazioni che catturano il significato di ciascun token. Ad esempio, nel capitolo 2, abbiamo discusso di come i token rappresentino concetti, ma i singoli token non hanno alcuna relazione tra loro. Consideriamo le parole "cane" e "lupo". Grazie alla nostra comprensione del linguaggio, sappiamo che questi termini sono correlati, ma abbiamo bisogno di un modo per catturare questa relazione all'interno di una rete neurale. Questo è esattamente ciò che fa il livello di incorporamento. Cattura informazioni su ciascun token che ne codificano il significato e ci permettono di esprimere la sua relazione concettuale con gli altri token. Di conseguenza, possiamo catturare l'idea che le rappresentazioni dei token doge wolfsiano più simili tra loro rispetto alle rappresentazioni dei token rede France. Possiamo pensare al livello di incorporamento come alla parte del modello che elabora le parole su una pagina e le mappa in rappresentazioni concettuali astratte nella nostra mente.
  </p>    
  </li>
  <li>
  <p align="justify">
Livello di trasformazione — I livelli di trasformazione sono il luogo in cui avviene la maggior parte del calcolo in un modello linguistico: catturano le relazioni tra le parole create dal livello di incorporamento e svolgono la maggior parte del lavoro effettivo per ottenere l'output. Sebbene i LLM abbiano generalmente un solo livello di incorporamento e un livello di output, hanno molti livelli di trasformazione. I modelli più potenti hanno più livelli di trasformazione.
È allettante descrivere il livello di trasformazione come la parte "pensante" del modello. Questa definizione implica erroneamente che i livelli di trasformazione (o il modello più ampio costruito da essi) possano pensare, ma il pensiero umano è autoriflessivo e variabile in durata e impegno. Si può pensare a qualcosa per mezzo secondo o mesi, a seconda dell'impegno richiesto per l'attività. Un trasformatore ripete sempre lo stesso processo con lo stesso impegno per ogni attività. Non c'è introspezione né alterazione dello stato mentale di un livello di trasformazione. Pertanto, un modo migliore per immaginare un livello di trasformazione è un insieme di regole fuzzy : fuzzy perché non richiedono corrispondenze esatte (perché gli embedding potrebbero restituire qualcosa di simile a "cane" per "lupo") e regole perché i trasformatori non hanno flessibilità. Una volta completato l'apprendimento, un livello di trasformazione farà la stessa cosa ogni volta.
  </p>    
  </li>
  <li>
  <p align="justify">
Livello di output : dopo che il modello ha eseguito il calcolo, vengono eseguite ulteriori trasformazioni nel livello di output per ottenere un risultato utile. Più comunemente, il livello di output funziona come l'inverso del livello di incorporamento, trasformando il risultato del calcolo dallo spazio degli incorporamenti, che cattura i concetti, nello spazio dei token, che cattura le sottoparole effettive per creare l'output testuale. Si può pensare a questo come alla parte del modello che prende la risposta che si è scelta e poi sceglie le parole effettive per esprimere quella risposta su una pagina, selezionando le parole che più probabilmente rappresentano i concetti che compongono la risposta. Infine, si conclude con un processo di unembedding, che converte gli incorporamenti in token. Poiché ogni token ha una mappatura biunivoca a una sottoparola, possiamo utilizzare un semplice dizionario o una mappa per convertire nuovamente i token in testo leggibile. Questo processo è descritto in dettaglio nella figura 3.2 .
  </p>    
  </li>
</ul>

<h3>3.2 Esplorazione dettagliata dell'architettura del trasformatore</h3>

<p align="justify">
Per comprendere meglio cosa accade all'interno di un LLM, può essere utile riformulare quella che abbiamo descritto come una sequenza di passaggi. Facciamolo nella figura 3.2 , che descrive sette passaggi. Contrassegneremo ciascuno di essi con riferimento alla sezione in cui lo abbiamo trattato in precedenza o vi informeremo quando stiamo per spiegare un nuovo dettaglio. Questo capitolo fornisce molte informazioni contemporaneamente, quindi le analizzeremo pezzo per pezzo man mano che procederemo.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.2 Il processo di conversione dell'input in output utilizzando un modello linguistico di grandi dimensioni
      </p>
    </figcaption>
    
<img width="1100" height="736" alt="CH03_F02_Boozallen" src="https://github.com/user-attachments/assets/08bd38cc-b43f-4052-bcbd-a8e25fb810ff" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
I sette passaggi per conseguire un LLM sono i seguenti:
</p>

<ol>
  <li>
    <p align="justify">
Mappare il testo sui token (capitolo 2).
    </p>
  </li>
  <li>
    <p align="justify">
Mappare i token nello spazio di incorporamento ( nuovo , sottosezione Rappresentazione dei token con vettori ).
    </p>
  </li>
  <li>
    <p align="justify">
Aggiungere informazioni a ciascun incorporamento che catturino la posizione di ciascun token nel testo di input ( nuovo , sottosezione Aggiunta di informazioni sulla posizione ).
    </p>
  </li>
  <li>
    <p align="justify">
Passare i dati attraverso uno strato trasformatore (ripetere \(L\) volte) ( nuovo , sottosezione 3.2.2 ).
    </p>
  </li>
  <li>
    <p align="justify">
Applicare il livello di unembedding per ottenere token che potrebbero generare buone risposte ( nuovo , sottosezione 3.2.3 ).
    </p>
  </li>
  <li>
    <p align="justify">
Prendi un campione dall'elenco dei possibili token per generare una singola risposta ( nuovo , sottosezione Campionamento dei token per produrre output ).
    </p>
  </li>
  <li>
    <p align="justify">
Decodificare i token della risposta in testo effettivo (capitolo 2).
    </p>
  </li>
</ol>

<h3>3.2.1 Incorporamento dei livelli</h3>

<p align="justify">
Ci sono molte sfumature nella tokenizzazione, negli embedding e nella precisione con cui il linguaggio viene tradotto in cose che i modelli possono comprendere. La sfumatura più importante è che le reti neurali non funzionano ancora direttamente con i token. Nel complesso, le reti neurali hanno bisogno di numeri che possano essere manipolati e un token ha un'identità numerica fissa. Non possiamo cambiare l'identità di un token perché l'identità ci permette di riconvertire i token in testo leggibile. Abbiamo bisogno di un livello che trasformi i token in forma numerica nelle parole o sotto-parole che rappresentano.
</p>

<b>Rappresentazione dei token con vettori</b>

<p align="justify">
Il nostro trasformatore ha bisogno di numeri su cui lavorare. Con questo intendiamo numeri continui , quindi qualsiasi valore frazionario è disponibile: 0,3, -5, 3,14, ecc. Abbiamo anche bisogno di più di un numero per rappresentare ogni token, in modo da catturare le sfumature di significato e le relazioni tra i token. Se provassimo a usare un solo numero per rappresentare ogni parola, incontreremmo difficoltà a catturare i molteplici significati, sinonimi, contrari e le relazioni che questi creano. Ad esempio, potremmo dire che l'antonimo (opposto) di una parola dovrebbe essere ottenibile moltiplicando una parola per \(-1\) . Come mostra la figura 3.3 , questo porta rapidamente a conclusioni assurde sulle relazioni tra le parole.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.3 Se si utilizza un solo numero per rappresentare un token, si incontrano rapidamente problemi in cui parole simili/dissimili non possono essere adattate tra loro. Qui vediamo come cercare di rappresentare semplici relazioni sinonimo/contrario diventa rapidamente insensato anche con solo una manciata di parole.
      </p>
    </figcaption>
    
<img width="1100" height="487" alt="CH03_F03_Boozallen" src="https://github.com/user-attachments/assets/a82bc4d2-ac3a-4b6c-8bc5-cfacaff1157a" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Ad esempio, supponiamo di avere un token stockche abbiamo arbitrariamente deciso verrà convertito in un numero (ad esempio, 5.2). Voglio assegnare a parole finanziarie correlate, come capital, un numero simile (ad esempio, 5.3) perché hanno significati simili. Esistono anche antonimi di stockaltri significati di , come rare. Supponiamo di usare un valore negativo per catturare l'idea di un antonimo e di assegnargli il valore di -5.2. Ma ora le cose si complicano perché un altro antonimo di capitalè debt. Ma se gli antonimi sono negazioni debte rarehanno un significato simile, il che è assurdo. La Figura 3.3 illustra il problema: quando usiamo un singolo numero per rappresentare una parola, non possiamo codificare le loro relazioni senza implicare strane relazioni con altre parole, e non siamo ancora andati oltre le quattro parole!
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.4 L'aggiunta di un'ulteriore dimensione alla nostra rappresentazione simbolica ci consente di rappresentare una disposizione più diversificata delle relazioni semantiche. Qui vediamo come due dimensioni possano catturare le relazioni per molteplici significati della stessa parola.
      </p>
    </figcaption>
    
![CH03_F04_Boozallen](https://github.com/user-attachments/assets/91fed6bf-0a78-41f5-9e18-c5cd690337bc)

  </figure>
</div>
  </td>
</table>

<p align="justify">
Il trucco sta nell'utilizzare più numeri per rappresentare ogni token, consentendo di trovare rappresentazioni migliori che tengano conto delle diverse relazioni tra le parole. Un esempio che utilizza due numeri è mostrato nella figura 3.4 . Possiamo vedere cose come blandessere quasi equidistanti da raree well-done, pur avendo anche spazio per bankessere lontani da tutte e tre le parole appena menzionate e invece essere vicini a stock. Siamo persino riusciti a inserire qualche parola in più. Più numeri si utilizzano, chiamati dimensioni nel gergo del settore, più complesse saranno le relazioni che si potranno rappresentare.
</p>

<table align="center">
<td>
  <h3>La maledizione della dimensionalità</h3>
  <p align="justify">
Se più dimensioni sono più efficaci nel catturare significati sottili, perché non usarne quante più dimensioni possibili per rappresentare i nostri dati? Quando si ha a che fare con un gran numero di dimensioni, sorgono diversi problemi. Una preoccupazione principale è che i LLM gestiscono molti embedding e l'aggiunta di più dimensioni aumenta la memoria e il calcolo necessari per memorizzare ed elaborare gli embedding. Inoltre, aggiungendo più dimensioni, la dimensione dello spazio semantico esplode e la quantità di dati e il tempo necessari per addestrare un modello di apprendimento automatico a conoscere tutte le posizioni nello spazio semantico crescono in modo esponenziale. Il matematico Richard E. Bellman ha coniato il termine "maledizione della dimensionalità" per descrivere questo fenomeno perché, sebbene desideriamo creare uno spazio in grado di catturare significati sfumati, siamo limitati dalle proprietà fondamentali dello spazio che creiamo.
  </p>
</td>
</table>

<p align="justify">
Nel gergo LLM, gli elenchi di numeri utilizzati per rappresentare i token sono chiamati embedding . Si può pensare a un embedding come a un array o a un elenco di valori in virgola mobile. In breve, chiamiamo tali array vettori . Ogni posizione nel vettore è chiamata dimensione. Come mostrato nella figura 3.4 , l'utilizzo di più dimensioni ci consente di catturare le sottigliezze nelle relazioni tra le parole nel linguaggio umano.
</p>

<p align="justify">
Poiché gli embedding esistono in più dimensioni, spesso affermiamo che risiedono in uno spazio semantico . In alcune applicazioni di apprendimento automatico, questo è chiamato spazio latente , soprattutto quando non si ha a che fare con il testo. Lo spazio semantico è un termine vago e poco definito nel settore, ma è comunemente usato come abbreviazione per dire che gli embedding vettoriali che rappresentano ciascun token si comportano bene, in quanto sinonimi/contrari hanno distanze più vicine/più lontane e che possiamo usare queste relazioni in modo produttivo. Ad esempio, nella figura 3.5 , mostriamo un caso famoso in cui una trasformazione "make female" può essere costruita sottraendo l'embedding for malee aggiungendo l'embedding for female. Questa trasformazione può essere applicata a molte parole di genere maschile diverse per trovare parole di genere femminile dello stesso concetto. Anche la collocazione di tutte le parole "reali" in basso a destra nella figura 3.5 è intenzionale, poiché molti tipi diversi di relazioni possono essere mantenuti simultaneamente in uno spazio ad alta dimensione.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.5 Una dimostrazione di come le relazioni tra gli embedding creino uno spazio semantico. Le parole con significati simili sono vicine tra loro e la stessa trasformazione può essere applicata a più parole per ottenere un risultato simile: in questo caso, una trasformazione per trovare la versione femminile di una parola maschile.
      </p>
    </figcaption>
    
<img width="1100" height="553" alt="CH03_F05_Boozallen" src="https://github.com/user-attachments/assets/d87d8820-8661-4496-a0cb-45b19785d66c" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Sorprendentemente, non possiamo garantire che queste relazioni semantiche si formino durante il processo di addestramento. Capita spesso che si formino, e si è scoperto che sono molto utili. Per estensione, le relazioni in uno spazio semantico non sono infallibili e possono insinuarsi distorsioni nei dati. Ad esempio, i modelli spesso determinano che " doctorè più simile a" malee " nurseè più simile a" femaleperché, nel testo generalmente disponibile utilizzato per costruire la maggior parte dei modelli, è più comune che i medici siano descritti come uomini e le infermiere come donne. Le relazioni non sono quindi una verità scoperta del mondo, ma un riflesso dei dati che sono entrati nel processo.
</p>

<b>Aggiunta di informazioni posizionali</b>

<p align="justify">
Un problema critico è che un trasformatore standard non comprende le informazioni sequenziali. Se si fornisse al trasformatore una frase e si riorganizzassero tutti i token, considererebbe tutte le possibili permutazioni dei token come identiche! Questo problema è illustrato nella figura 3.6 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.6 Senza informazioni posizionali, i trasformatori non capiscono che i loro input hanno un ordine specifico e tutte le possibili riorganizzazioni dei token appaiono identiche all'algoritmo. Questo è problematico perché l'ordine delle parole può modificare il contesto della parola o, se eseguito in modo casuale, diventare incomprensibile.
      </p>
    </figcaption>
    
<img width="1043" height="511" alt="CH03_F06_Boozallen" src="https://github.com/user-attachments/assets/cca43e08-c390-4e83-9a5f-6ca8ed8b9a03" />


  </figure>
</div>
  </td>
</table>

<p align="justify">
Per questo motivo, il livello di embedding genera due diversi tipi di embedding. In primo luogo, crea un embedding di parola che cattura il significato del token e, in secondo luogo, crea un embedding posizionale che cattura la posizione del token in una sequenza.
</p>

<p align="justify">
L'idea è sorprendentemente semplice. Proprio come abbiamo mappato ogni token univoco a un vettore di significato univoco, mapperemo anche ogni posizione univoca del token (prima, seconda, terza e così via) a un vettore di posizione. Quindi ogni token verrà incorporato due volte: una volta per la sua identità e una seconda per la sua posizione. Questi due vettori vengono poi sommati per creare un unico vettore che rappresenta la parola e la sua posizione nella frase. Questo processo è descritto nella figura 3.7 .
</p>

<p align="justify">
Nota: l'utilizzo di più dimensioni anziché posizioni assolute semplifica l'apprendimento del posizionamento relativo da parte del trasformatore, anche se per noi umani è eccessivamente ridondante [1].
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.7 Gli embedding di parole non catturano il fatto che i token di input appaiano in un ordine specifico. Questa informazione viene catturata da un embedding posizionale. Gli embedding di posizione funzionano allo stesso modo degli embedding di parole e vengono sommati. Gli embedding combinati risultanti contengono le informazioni necessarie al modello per comprendere l'ordine dei token.
      </p>
    </figcaption>
    
<img width="1100" height="438" alt="CH03_F07_Boozallen" src="https://github.com/user-attachments/assets/3ab8fb46-12cb-4f7a-b767-125a25c3d792" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Questi sono tutti i dettagli mancanti necessari per comprendere come i token vengono convertiti in vettori per i livelli del trasformatore. Questa strategia può sembrare un po' ingenua, ed è proprio così. Si sono provati metodi più sofisticati per gestire queste informazioni, ma questo semplice approccio "Trasformiamo tutto in un vettore e sommiamolo" funziona sorprendentemente bene. È importante sottolineare che ha avuto successo anche con video e immagini. Avere una strategia semplice che funzioni abbastanza bene per molti problemi diversi è prezioso, ed è per questo che questo approccio ingenuo ha preso piede.
</p>

<h3>3.2.2 Strati del trasformatore</h3>

<p align="justify">
Lo strato del trasformatore mira a trasformare l'input in un output più utile. La maggior parte degli strati precedenti delle reti neurali, come lo strato di incorporamento, sono progettati per incorporare convinzioni molto specifiche su come funziona il mondo nel loro funzionamento. L'idea è che se la convinzione codificata è accurata rispetto a come funziona effettivamente il mondo, il modello raggiungerà una soluzione migliore utilizzando meno dati. I trasformatori adottano la strategia opposta. Codificano un meccanismo generico che può apprendere molte attività se si ottengono dati sufficienti.
</p>

<p align="justify">
Per fare ciò, i trasformatori funzionano con tre componenti principali:
</p>

<ul>
  <li>
    <p align="justify">
Query : le query sono vettori (da un livello di incorporamento) che rappresentano ciò che stai cercando.
    </p
    <li>
    <p align="justify">
Chiave : i vettori chiave rappresentano le possibili risposte a cui associare una query.
    </p>
  </li>
  <li>
    <p align="justify">
Valore : ogni chiave ha un vettore di valori corrispondente, ovvero il valore effettivo da restituire quando una query e una chiave corrispondono.
    </p>
  </li>
  </li>
</ul>

<p align="justify">
Questa terminologia corrisponde al comportamento di un dictoggetto dizionario o in Python. Si cerca un elemento nel dizionario tramite la sua chiave, in modo da poter poi creare un output utile. La differenza è che un trasformatore è fuzzy. Non stiamo cercando una singola chiave, ma stiamo valutando tutte le chiavi , ponderate in base al loro grado di similarità con la query. La Figura 3.8 mostra come funziona con un semplice esempio. Mentre le query e le chiavi sono mostrate come stringhe, queste stringhe sono sostitutive dei vettori a cui ciascuna stringa verrà mappata tramite il livello di incorporamento.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.8 Un esempio di come funzionano query, chiavi e valori all'interno di un trasformatore rispetto a un dizionario Python. Quando un dizionario Python abbina query a chiavi, necessita di una corrispondenza esatta per trovare il valore, altrimenti non restituirà nulla. Un trasformatore restituisce sempre qualcosa in base alle corrispondenze più simili tra query e chiavi.
      </p>
    </figcaption>
    
<img width="1100" height="561" alt="CH03_F08_Boozallen" src="https://github.com/user-attachments/assets/33f8fe72-c17b-4993-aee1-f8c54a48a1dc" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Far sì che ogni chiave contribuisca a una query potrebbe creare confusione, soprattutto se esiste una sola corrispondenza esatta tra una query e una chiave specifica. Questo problema è gestito da un dettaglio chiamato attenzione o meccanismo di attenzione .
</p>

<p align="justify">
L'attenzione all'interno di un trasformatore può essere considerata simile alla capacità di prestare attenzione a ciò che è importante. È possibile ignorare le informazioni irrilevanti e distraenti (ad esempio, tasti sbagliati) e concentrarsi principalmente su ciò che è importante (i tasti più adatti). L'analogia si estende ulteriormente, in quanto l'attenzione è adattiva; ciò che è importante è funzione delle altre opzioni disponibili. Il tuo capo che ti dà le istruzioni per la settimana cattura la tua attenzione, ma l'allarme antincendio che scatta sposta la tua attenzione dal capo all'allarme (e a un potenziale incendio).
</p>

<p align="justify">
Durante la generazione del token successivo, un trasformatore prende la query per il token corrente e la confronta con la chiave di tutti i token precedenti. Il confronto tra query e chiave genera una serie di valori che il meccanismo di attenzione utilizza per calcolare il peso da assegnare a ciascun potenziale token successivo quando decide quale token generare successivamente. Il valore di ciascun token indica al modello quale dovrebbe essere il contributo di ogni token precedente alla probabilità. La funzione di attenzione calcola quindi il token successivo, come mostrato nella figura 3.9 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.9 Il token successivo in una frase viene previsto utilizzando il token corrente come query e calcolando corrispondenze con le parole precedenti come chiavi. I singoli valori non devono necessariamente esistere nello spazio semantico; l'output del meccanismo di attenzione produce qualcosa di simile a uno dei token nel vocabolario.
      </p>
    </figcaption>
    
<img width="1100" height="772" alt="CH03_F09_Boozallen" src="https://github.com/user-attachments/assets/47c76287-6523-4ecf-802d-cdd5a14cc5a9" />

  </figure>
</div>
  </td>
</table>

<table align="center">
  <td>
    <h4>Qual è la matematica dell'attenzione?</h4>
    <p align="justify">
    Non entreremo nei dettagli della matematica alla base dell'attenzione perché richiederebbe molto spazio per essere descritta, e l'argomento è già stato trattato altrove. Lo abbiamo fatto in un libro precedente: il capitolo 11 di Inside Deep Learning [2] spiega i trasformatori e l'attenzione in modo molto più tecnico.
    </p>
    
<p align="justify">
Per i curiosi, l'equazione primaria è
</p>


<div align="center">
<img width="511" height="126" alt="image" src="https://github.com/user-attachments/assets/4caa3a80-60f2-45cc-9559-5a6d9eec455d" />
</div>

<div align="center">
<img width="511" height="126" alt="image" src="https://github.com/user-attachments/assets/962922c7-e96a-433f-8228-740464a88914" />
</div>

<p align="justify">
Le query, le chiavi e i valori sono rappresentati rispettivamente dalle singole matrici (Q) , (K) e (V) . La moltiplicazione di matrici rende l'attenzione efficiente quando implementata su GPU, poiché queste possono eseguire numerose operazioni di moltiplicazione in parallelo. La funzione softmax implementa il componente principale dell'analogia dell'attenzione assegnando molti valori prossimi a zero, il che fa sì che il trasformatore ignori gli elementi non importanti.
</p>

<p align="justify">
Il passaggio finale di norma e feedforward è l'applicazione della normalizzazione di livello e di un livello lineare tramite una connessione di salto . Se questi termini non ti sono familiari, non preoccuparti: non è necessario conoscere questa matematica per comprendere il resto del libro. Se desideri apprendere il significato di questi termini, ti rimandiamo a Inside Deep Learning [2] per una comprensione tecnicamente dettagliata.
</p>

</td>
</table>

<p align="justify">
Un modello di trasformatore è composto da decine di strati di trasformatore. Gli strati intermedi del trasformatore svolgono lo stesso compito meccanico descritto nella figura 3.9 , pur non dovendo prevedere un token, poiché l'ultimo strato del trasformatore è l'unico che deve predire un token effettivo. Lo strato del trasformatore è sufficientemente generale da consentire al modello di apprendere compiti complessi come l'ordinamento, l'impilamento e altre sofisticate trasformazioni di input.
</p>

<h3>3.2.3 Separazione degli strati</h3>

<p align="justify">
L'ultima fase di un LLM è lo strato di unembedding, che trasforma la rappresentazione vettoriale numerica utilizzata dai trasformatori in uno specifico token di output, in modo da poter restituire il testo corrispondente a tale token. Questo processo di generazione dell'output è anche chiamato decodifica , perché decodifica la rappresentazione vettoriale del trasformatore in un testo di output. È un componente cruciale per l'utilizzo di un LLM per generare testo. Non solo la decodifica del token corrente è essenziale per la produzione dell'output, ma il token successivo dipenderà da ogni token precedente selezionato per l'output. Questo processo è mostrato nella figura 3.10 , dove generiamo ricorsivamente i token uno alla volta. In termini statistici, questo è noto come processo autoregressivo , il che significa che ogni elemento dell'output si basa sull'output precedente.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.10 La produzione di output da LLM prevede la conversione dei documenti in token e il successivo utilizzo del modello per produrre output. Eseguiamo questo processo in modo ciclico sia per elaborare il testo sia per generare output leggibile.      </p>
    </figcaption>
    
<img width="834" height="840" alt="CH03_F10_Boozallen" src="https://github.com/user-attachments/assets/cd7dd87f-b216-42ad-bd7b-76fc1af4d762" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Forse ti starai chiedendo come si interrompe questo processo. Quando costruiamo il vocabolario dei token, includiamo alcuni token speciali che non compaiono nel testo. Uno di questi token speciali è un token di fine sequenza (EoS). Il modello si addestra su testi con endpoint naturali che terminano con il marcatore EoS e, quando il modello genera un nuovo token, il token EoS è una delle opzioni che può generare. Se l'EoS viene generato, sappiamo che è il momento di interrompere il ciclo e restituire il testo completo all'utente. È inoltre consigliabile mantenere un limite massimo di generazione se il modello entra in uno stato non valido e non riesce a generare il token EoS.
</p>

<b>Campionamento di token per produrre output</b>

<p align="justify">
Ciò che manca in questo processo è il modo in cui convertiamo un vettore, un array di numeri in virgola mobile prodotto dagli strati del trasformatore, in un singolo token. Questo processo è chiamato campionamento perché utilizza un metodo statistico per selezionare i token campione dal vocabolario in base all'input e all'output dell'LLM fino a quel momento. L'algoritmo di campionamento dell'LLM valuta tali campioni per selezionare il token da produrre. Esistono diverse tecniche per eseguire questo campionamento, ma tutte seguono la stessa strategia di base in due fasi:
</p>

<ol>
  <li>
    <p align="justify">
Per ogni token nel vocabolario, calcola la probabilità che ciascun token sia il token selezionato successivo.
    </p>
  </li>
  <li>
    <p align="justify">
Scegli casualmente un gettone in base alle probabilità calcolate.
    </p>
  </li>
</ol>

<p align="justify">
Se hai utilizzato ChatGPT o altri LLM, potresti aver notato che non sempre forniscono lo stesso output per lo stesso input. La fase di decodifica è il motivo per cui potresti ottenere risposte diverse ogni volta che poni la stessa domanda.
</p>

<p align="justify">
Può sembrare controintuitivo che i token vengano selezionati casualmente. Tuttavia, è una componente fondamentale per generare testo di buona qualità. Si consideri l'esempio di generazione di testo nella figura 3.11 , in cui stiamo cercando di completare la frase "Amo mangiare". Sarebbe irrealistico se il modello scegliesse sempre "sushi" come token successivo perché ha la probabilità più alta. Se qualcuno ti dicesse sempre "sushi" in questo contesto, penseresti che qualcosa non va. Abbiamo bisogno della casualità per gestire il fatto che ci sono più scelte valide e che non è probabile che tutte le opzioni si verifichino.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 3.11 Dimostriamo la generazione di testo iniziando con la frase "Amo mangiare" e poi mostrando che alcuni possibili completamenti che sono cibi, come barbecue e sushi, hanno alte probabilità, mentre un'auto e il numero 42 hanno basse probabilità. La selezione casuale ponderata sceglie la parola tacos . Il ciclo di generazione si interrompe quando appare il token EoS.    </figcaption>
    
<img width="1100" height="793" alt="CH03_F11_Boozallen" src="https://github.com/user-attachments/assets/324a0efe-3507-45f9-816a-41df8fdee666" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Si noti inoltre che nell'esempio della figura 3.11 altri token, come 42, sarebbero privi di senso, se le probabilità fossero minime. Ancora una volta, dobbiamo assegnare a ogni token una probabilità per sapere quali token sono probabili o improbabili.
</p>

<table>
  <td>
    <h4>Come si ottengono le probabilità per i token?</h4>
    <p align="justify">
    Ogni possibile token successivo ha una probabilità diversa di essere selezionato. La maggior parte dei token ha una probabilità quasi nulla di essere selezionata. Un lettore attento potrebbe chiedersi: come possiamo assegnare una probabilità a un token prima di conoscere gli altri token? Lo facciamo assegnando a ogni token un punteggio, che indica quanto è buona la corrispondenza tra l'embedding di quel token e il vettore corrente (ovvero, l'uscita del trasformatore). Il punteggio è arbitrario da -infty a infty e calcolato indipendentemente per ciascun token. La differenza relativa nei punteggi viene quindi utilizzata per creare le probabilità. Ad esempio, se un token avesse un punteggio di 65,2 e un secondo token avesse un punteggio di -5,0, le probabilità sarebbero rispettivamente vicine al 100% e allo 0% per il singolo token. Se i punteggi fossero 65,2 e 65,1, le probabilità sarebbero rispettivamente vicine al 50,5% e al 49,5%. Allo stesso modo, punteggi pari a 0,2 e 0,1 darebbero le stesse probabilità dei punteggi 65,2 e 65,1 perché stiamo considerando le differenze relative nei punteggi per assegnare le probabilità, non i singoli punteggi stessi.
    </p>
  </td>
</table>

<p align="justify">
A volte un trasformatore genera generazioni insolite o senza senso. Non è comune, ma gli altri token hanno una probabilità prossima allo zero e, alla fine, verrà estratto un token strano che non ti aspetteresti. Una volta estratto un token inaspettato, tutti i token generati in futuro verranno prodotti in un modo che tenterà di dare un senso alla generazione insolita.
</p>

<p align="justify">
Ad esempio, se l'LLM producesse "Adoro mangiare il gesso ", rimarreste piuttosto sorpresi. Ma non è eccessivamente irragionevole, perché mangiare gesso è un sintomo di una condizione medica chiamata pica. Una volta selezionata la parola gesso , l'LLM potrebbe divagare sulla pica o su qualche altra diatriba medica, ovviamente se siete così fortunati che la vostra insolita generazione rientri nella sfera del "raro ma ragionevole" e non in una previsione del tutto errata.
</p>

<p align="justify">
Nota: molti algoritmi possono calcolare le probabilità finali utilizzate per selezionare le parole da generare. Uno di questi è il campionamento a nucleo, noto anche come campionamento Top-p, che prevede la determinazione dei token con la più alta probabilità di output potenziali e la scelta dei token da generare da tale elenco. Questo metodo può aiutarci a evitare previsioni irragionevoli. Se possibile, è opportuno verificare quale algoritmo di campionamento utilizza il tuo LLM in modo da comprenderne i rischi di produrre output più rari o irragionevoli.
</p>

<h3>3.3 Il compromesso tra creatività e risposte di attualità</h3>

<p align="justify">
A seconda di come i tuoi utenti intendono interagire con un LLM, potresti desiderare di generare output sorprendenti o creativi. Supponiamo che tu stia utilizzando un LLM per favorire il brainstorming di idee per nuovi prodotti e che tu stia utilizzando un chatbot come cassa di risonanza digitale per stimolare le idee. In questo caso, probabilmente vorrai generare output insoliti perché l'obiettivo è essere creativi e pensare a qualcosa di nuovo.
</p>

<p align="justify">
Al contrario, a volte la creatività è del tutto indesiderata. Un potenziale utilizzo degli LLM è la ricerca offline, che consente di installare un LLM su un telefono cellulare (relativamente potente) e di chiedere/cercare informazioni anche in assenza di connessione a Internet. In questo caso, è necessario che i risultati dell'LLM siano affidabili, pertinenti e fattuali. Non è necessaria una reinterpretazione creativa.
</p>

<p align="justify">
Una caratteristica dei LLM chiamata temperatura bilancia questo compromesso. La variabile temperatura (che è un numero compreso tra 0 e 1 e spesso ha un valore predefinito di 0,7 o 0,8) viene utilizzata per esagerare la probabilità di token a bassa verosimiglianza (alta temperatura) o per ridurla a quella di token a bassa verosimiglianza (bassa temperatura).
</p>

<p align="justify">
Consideriamo le molecole in un bicchiere d'acqua come analogia. Supponiamo di voler sapere quale molecola si troverà in cima al bicchiere (non chiedeteci perché; lasciate perdere). Se il bicchiere venisse abbassato a una temperatura pari allo zero assoluto, tutte le molecole rimarrebbero immobili e la molecola in cima al bicchiere sarebbe sempre la stessa (ovvero, genereremmo sempre lo stesso token). Se aumentassimo la temperatura del bicchiere a tal punto da farla bollire, le molecole rimbalzerebbero, rendendo la molecola in cima al bicchiere essenzialmente casuale (ovvero, otterremmo un token completamente casuale). Aumentando o diminuendo la temperatura, si modifica l'equilibrio tra una scelta più casuale (e, quindi, spesso creativa) e una più mirata al token successivo più probabile (mantenendo così la generazione più attuale).
</p>

<p align="justify">
In senso pratico, considerando il nostro esempio di "Mi piace mangiare", una temperatura più alta porterebbe alla generazione di diversi tipi di cibo, non solo pizza o sushi, ma anche cibi meno tipici o più specifici come il manzo Wellington o il chili vegetariano.
</p>

<h3>3.4 Trasformatori nel contesto</h3>

<p align="justify">
Abbiamo trattato molti argomenti in questo capitolo. I livelli di incorporamento, i livelli di trasformazione e i livelli di disincorporamento sono gli elementi fondamentali che fanno funzionare gli LLM. I concetti su come gli LLM codificano il significato e la posizione e poi utilizzano pile di livelli di trasformazione per scoprire la struttura del testo sono tutti fondamentali per comprendere come gli LLM catturano le informazioni e producono la qualità di output di cui sono capaci. Ma abbiamo ancora molto da approfondire! Come creiamo questi livelli per generare incorporamenti e probabilità analizzando innanzitutto pile e pile di dati? Nel capitolo 4, continueremo a esplorare come immettere i dati in questa architettura e incentivare l'LLM ad "apprendere" relazioni significative nel testo attraverso il processo di addestramento.
</p>

<h3>Riepilogo</h3>

<ul>
  <li>
    <p align="justify">
Sebbene gli LLM utilizzino i token come unità di base del significato semantico, questi sono rappresentati matematicamente all'interno del modello come vettori di inclusione anziché come stringhe. Questi vettori di inclusione possono catturare relazioni di prossimità, dissimilarità, antonimi e altre proprietà linguistico-descrittive.
    </p>
  </li>
  <li>
    <p align="justify">
Posizione e ordine delle parole non sono naturali per i trasformatori e vengono ottenuti tramite un altro vettore che rappresenta la posizione relativa. Il modello può rappresentare l'ordine delle parole aggiungendo i vettori di posizione e di word embedding.
    </p>
  </li>
  <li>
    <p align="justify">
I livelli di trasformazione agiscono come una sorta di dizionario fuzzy, restituendo risposte approssimative a corrispondenze approssimative. Questo processo fuzzy è chiamato attenzione e utilizza i termini query , key e value come analoghi a key e value in un dizionario Python.
    </p>
  </li>
  <li>
    <p align="justify">
ChatGPT è un esempio di trasformatore solo decodificatore, ma esistono anche trasformatori solo codificatore e trasformatori codificatore-decodificatore. I trasformatori solo decodificatore sono più adatti alla generazione di testo, ma altri tipi di trasformatori possono essere più adatti ad altri compiti.
    </p>
  </li>
  <li>
    <p align="justify">
I modelli LLM sono autoregressivi, ovvero funzionano in modo ricorsivo. Tutti i token generati in precedenza vengono immessi nel modello a ogni passaggio per ottenere il token successivo. In parole povere, i modelli autoregressivi prevedono l'evento successivo utilizzando gli eventi precedenti.
    </p>
  </li>
  <li>
    <p align="justify">
L'output di qualsiasi trasformatore non è un numero di token; piuttosto, l'output è una probabilità di quanto è probabile ogni token. La selezione di un token specifico è chiamata unembedding o campionamento e include una certa casualità.
    </p>
  </li>
  <li>
    <p align="justify">
L'intensità della casualità può essere controllata, ottenendo risultati più o meno realistici, più creativi o unici, o più coerenti. La maggior parte degli LLM ha una soglia predefinita per la casualità che sembra ragionevole, ma potrebbe essere necessario modificarla per usi diversi.
    </p>
  </li>
</ul>





