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
Figura 3.11 Dimostriamo la generazione di testo iniziando con la frase "Amo mangiare" e poi mostrando che alcuni possibili completamenti che sono cibi, come barbecue e sushi, hanno alte probabilità, mentre un'auto e il numero 42 hanno basse probabilità. La selezione casuale ponderata sceglie la parola tacos . Il ciclo di generazione si interrompe quando appare il token EoS.    
      </p>
    </figcaption>
    
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

<h2>4 Come imparano gli LLM</h2>

<table align="center">
  <td>
    <h3>Questo capitolo copre</h3>
    <ul>
      <li>
        <p align="justify">
        Algoritmi di addestramento con funzioni di perdita e discesa del gradiente
        </p>
      </li>
      <li>
        <p align="justify">
        Come gli LLM imitano il testo umano
        </p>
      </li>
      <li>
        <p align="justify">
        Come la formazione può portare gli LLM a commettere errori
        </p>
      </li>
      <li>
        <p align="justify">
        Sfide nella scalabilità degli LLM
        </p>
      </li>
    </ul>
  </td>
</table>

<p align="justify">
I termini apprendimento e addestramento sono comunemente usati nella comunità del machine learning per descrivere il comportamento degli algoritmi quando osservano i dati e formulano previsioni basate su tali osservazioni. Usiamo questa terminologia a malincuore perché, sebbene semplifichi la discussione sul funzionamento di questi algoritmi, riteniamo che non sia la soluzione ideale. Fondamentalmente, questa terminologia porta a idee sbagliate sugli LLM e sull'intelligenza artificiale. Queste parole implicano che questi algoritmi abbiano qualità simili a quelle umane; inducono a credere che gli algoritmi mostrino comportamenti emergenti e siano capaci di fare più di quanto siano realmente capaci. Fondamentalmente, questa terminologia è errata. Un computer non impara in alcun modo simile a come apprendono gli esseri umani. I modelli migliorano in base ai dati e al feedback, ma è estremamente importante mantenere questo meccanismo distinto da qualsiasi cosa che assomigli all'apprendimento umano. In effetti, probabilmente non si desidera che un'IA impari come un essere umano: passiamo molti anni della nostra vita concentrati sull'istruzione e prendiamo ancora decisioni stupide.
</p>

<p align="justify">
Gli algoritmi di deep learning si addestrano in un modo molto più stereotipato di quello umano. È stereotipato nel senso letterale di utilizzare molta matematica e nel senso figurato di seguire una semplice procedura ripetitiva miliardi di volte fino al completamento. Vi risparmieremo la matematica, ma in questo capitolo vi aiuteremo a svelare il mistero di come vengono addestrati gli LLM.
</p>

<p align="justify">
Molti algoritmi di apprendimento automatico utilizzano l'algoritmo di addestramento chiamato "discesa del gradiente" . Il nome di questo algoritmo implica alcuni dettagli che esamineremo con una panoramica generale su come la discesa del gradiente viene utilizzata per l'apprendimento automatico. Una volta compreso l'approccio generale utilizzato per addestrare diversi tipi di modelli, esploreremo come la discesa del gradiente viene applicata agli LLM per creare un modello che produca un output testuale convincente.
</p>

<p align="justify">
Comprendere questi dettagli ti aiuterà a evitare le connotazioni imprecise implicite in parole come " imparare" . Ancora più importante, ti preparerà anche a comprendere meglio quando gli LLM hanno successo e falliscono nella loro attuale configurazione e i modi spesso subdoli in cui tali algoritmi possono produrre risultati fuorvianti.
</p>

<h3>4.1 Discesa del gradiente</h3>

<p align="justify">
La discesa del gradiente è la chiave di tutti i moderni algoritmi di deep learning. Quando un professionista del settore menziona la discesa del gradiente, si riferisce implicitamente a due elementi critici del processo di addestramento. Il primo è noto come funzione di perdita , e il secondo è il calcolo dei gradienti , ovvero misurazioni che indicano come regolare i parametri della rete neurale in modo che la funzione di perdita produca risultati specifici. Si possono considerare questi due componenti di alto livello:
</p>

<p align="justify">
Funzione di perdita : è necessario un singolo punteggio numerico che calcoli il livello di malfunzionamento dell'algoritmo.
Discesa del gradiente : è necessario un processo meccanico che modifichi i valori numerici all'interno di un algoritmo per ridurre al minimo il punteggio della funzione di perdita.
La funzione di perdita e la discesa del gradiente sono componenti dell'algoritmo di addestramento utilizzato per produrre un modello di apprendimento automatico. Oggi vengono utilizzati molti algoritmi di addestramento diversi, ma in genere ogni algoritmo invia input a un modello, ne osserva l'output e lo modifica per migliorarne le prestazioni. Un algoritmo di addestramento ripeterà questo processo un numero enorme di volte. Con dati sufficienti, un modello produrrà gli output previsti ripetutamente e in modo affidabile quando confrontato con input non osservati in precedenza.
</p>

<h3>4.1.1 Che cos'è una funzione di perdita?</h3>

<p align="justify">
Useremo l'esempio del desiderio di fare soldi per aiutarci a sviluppare un'immagine mentale di una funzione di perdita adatta. In effetti, una persona intelligente può fare soldi, quindi se hai un computer intelligente, dovrebbe essere in grado di aiutarti a fare soldi. Per scegliere una funzione di perdita adatta a questo o a qualsiasi altro compito (queste lezioni si generalizzano a qualsiasi problema di apprendimento automatico oltre agli LLM), dobbiamo soddisfare tre criteri: specificità , computabilità e fluidità . In altre parole, la funzione di perdita deve essere
</p>

<ul>
  <li>
  <p align="justify">
Specifico e correlato al comportamento desiderato del modello
  </p>
  </li>
  <li>
  <p align="justify">
Calcolabile in un lasso di tempo ragionevole con una quantità ragionevole di risorse
  </p>
  </li>
  <li>
  <p align="justify">
Uniforme, nel senso che l'output della funzione non fluttua in modo eccessivo quando vengono forniti input simili
  </p>
  </li>
</ul>

<p align="justify">
Utilizzeremo i seguenti esempi e controesempi per aiutarti a sviluppare un'intuizione per ciascuna proprietà.
</p>

<b>Specificità della funzione di perdita</b>

<p align="justify">
Innanzitutto, iniziamo con un pessimo esempio di specificità. Se il tuo capo venisse da te e ti dicesse: "Costruisci un computer intelligente", sarebbe un obiettivo magnifico, ma non è un obiettivo specifico. Ricorda, nel capitolo 1, abbiamo discusso di quanto sia difficile definire l'intelligenza. In cosa esattamente il tuo capo vuole che questo computer sia intelligente? Basterebbe un computer intelligente che non sa fare i tuoi compiti di calcolo? Invece, potresti provare a ottimizzare per un punteggio di QI specifico, ma questo è correlato a ciò che vuole il tuo capo? Siamo riusciti a far superare ai computer i test del QI per oltre un decennio [1], anche prima dell'introduzione degli LLM. Tuttavia, non potevano fare altro che superare un test del QI ed eseguire compiti limitati. In definitiva, il test del QI non è correlato a ciò che vogliamo che i computer facciano. Di conseguenza, non vale la pena ottimizzare il QI come metrica per il successo nell'apprendimento automatico o per costruire il computer intelligente che il tuo capo ti ha chiesto di creare.
</p>

<p align="justify">
Un altro esempio riguarda la sfida della gestione del denaro. Consideriamo uno scenario in cui si desidera ridurre al minimo il debito. Potremmo persino volere che il debito diventi negativo, il che significa che altri ci devono dei soldi! Usiamo l'esempio del debito qui perché è intrinsecamente un valore che si desidera ridurre. Questa analogia si allinea perfettamente con la terminologia utilizzata nella pratica: si desidera ridurre al minimo la perdita così come si desidera ridurre il debito. Anche il volume del debito è una misura oggettiva, il che lo rende un buon modo per garantire che la nostra funzione di perdita sia rilevante in condizioni mutevoli. Infine, se il nostro obiettivo generale è mantenere un surplus di denaro, la minimizzazione del debito è ben correlata a tale obiettivo. La minimizzazione del debito ha tutte le caratteristiche di una buona funzione di perdita!
</p>

<table align="center">
  <td>
    <h3>Una nota sulla terminologia</h3>
<p align="justify">
    Potresti anche sentire le funzioni di perdita descritte come funzioni obiettivo . Ti consigliamo di evitare questo termine perché è ambiguo. Ad esempio, non è chiaro se si desidera minimizzare (il debito) o massimizzare il proprio obiettivo (il profitto). Entrambi gli approcci funzionano tecnicamente; moltiplicando un obiettivo di massimizzazione per \(-1\) si ottiene un obiettivo di minimizzazione.
</p>
<p align="justify">
In alcuni contesti, come l'apprendimento per rinforzo (RL) , si potrebbe anche sentire il termine "funzione di ricompensa" . Questo è appropriato perché gli algoritmi RL mirano a massimizzare la ricompensa eseguendo un comportamento desiderabile.
</p>
<p align="justify">
Indipendentemente dalla terminologia, le funzioni obiettivo, le funzioni di ricompensa e le funzioni di perdita rispondono tutte allo stesso requisito fondamentale: forniscono un modo per valutare gli output prodotti da un modello di apprendimento automatico.
</p>
  </td>
</table>

<b>Calcolabilità della funzione di perdita</b>

<p align="justify">
Anche la funzione di perdita deve essere qualcosa che possiamo calcolare rapidamente con un computer. L'esempio del debito non è adatto a questo aspetto perché tutti gli input e gli output necessari non sono prontamente disponibili per un computer. Lavorare di più aumenterà il reddito e quindi ridurrà il debito? Forse, ma come codificheremo il tuo duro lavoro nel computer? Qui, abbiamo il problema che i fattori più critici per ridurre al minimo il debito sono difficili da quantificare, come la disponibilità di un lavoro, l'idoneità a tali lavori, la probabilità di promozione, ecc. Quindi la perdita è specifica, ma gli input che si collegano a tale perdita non sono calcolabili.
</p>

<p align="justify">
Un obiettivo migliore e più calcolabile sarebbe prevedere la perdita di un investimento. Le ragioni per cui questo obiettivo è migliore sono sottili. L'obiettivo è comunque oggettivo perché i nostri algoritmi apprendono dai dati storici. Ad esempio, un investimento storico in obbligazioni X e azioni Y ha prodotto rendimenti specifici. Anche gli input sono ora oggettivi: è possibile quantificare la quantità di denaro investita in ciascun investimento. Si investe o si preleva denaro. Non ci sono problemi difficili da codificare come il "duro lavoro" da affrontare. Con una copia dei dati storici, un computer può calcolare rapidamente la perdita/rendimento di un investimento.
</p>


<b>Levigatezza della funzione di perdita</b>

<p align="justify">
La terza cosa di cui abbiamo bisogno è la fluidità. Molte persone hanno un buon intuito sul significato di fluidità, pensando a una consistenza liscia rispetto a una irregolare. Invece di consistenza, stiamo parlando della fluidità di una funzione, che può essere rappresentata disegnando la funzione stessa come un grafico. Ad esempio, quando si cerca di prevedere una perdita su un investimento, ci si imbatte nel problema che i rendimenti degli investimenti non sono solitamente fluidi. Possono seguire un modello di volatilità in cui i grafici dei prezzi sono frastagliati con variazioni brusche e improvvise. Questo rende difficile l'apprendimento. Un grafico che mostra i valori instabili dei rendimenti degli investimenti nel mondo reale è mostrato nella figura 4.1 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 4.1 I rendimenti degli investimenti non sono facili da prevedere, in parte perché non sono uniformi. (Immagine modificata da [2] sotto licenza Creative Commons
      </p>
    </figcaption>
    
![CH04_F01_Boozallen](https://github.com/user-attachments/assets/44cb01a9-a789-48e7-89a6-45e497e4510e)

  </figure>
</div>
  </td>
</table>

<p align="justify">
Il ritorno sull'investimento è un ottimo esempio di perdita negativa (non uniforme), poiché un comportamento irregolare è problematico per qualsiasi approccio predittivo. Sarebbe opportuno essere sempre cauti nei confronti di chiunque o di qualsiasi approccio che affermi di funzionare bene nel prevedere dati non uniformi come questo. Tuttavia, esiste una definizione tecnica precisa di "scorrevole" che, se non soddisfatta da una funzione di perdita, è un duro colpo. Le funzioni che dipendono da discontinuità, o interruzioni nella coerenza dei loro valori, sono le funzioni più comuni che non sono tecnicamente uniformi, ma vorremmo essere in grado di utilizzarle nella pratica. Alcuni esempi di funzioni non uniformi sono mostrati nella figura 4.2 per aiutarvi a comprendere. La scorrevolezza è solitamente inibita da discontinuità, come quella mostrata nel grafico centrale, o da nette variazioni nel valore di una funzione, come mostrato nel grafico a destra.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.2 Esempi di una funzione regolare a sinistra e di due funzioni non regolari a destra. L'esempio al centro è per lo più regolare, ma una regione non è regolare perché la funzione non ha alcun valore. A destra, la funzione non è regolare in nessun punto a causa della brusca variazione di valore.
      </p>
    </figcaption>
    
<img width="1100" height="359" alt="CH04_F02_Boozallen" src="https://github.com/user-attachments/assets/c0d8d142-e592-40b5-8fb3-28d353b2e0fd" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Non approfondiremo le definizioni matematiche formali che descrivono cosa rende qualcosa "scorrevole" e quali variazioni di valore sono accettabili o inaccettabili nelle funzioni "scorrevoli". Tuttavia, vi abbiamo fornito sufficienti informazioni di base per comprendere ciò che dovete sapere. La cosa importante da capire è che la vostra intuizione su cosa significhi "scorrevole", ovvero che il valore cambia continuamente, è un buon barometro della fattibilità di una funzione di perdita. Questo può sembrare arbitrario, ma è un problema onnipresente. Supponiamo di voler costruire un modello per prevedere con precisione il cancro. L'accuratezza non è una funzione "scorrevole" perché si conta il numero di previsioni riuscite sul totale delle previsioni. Ad esempio, se avete 50 pazienti e ne avete previsti correttamente 48, una funzione "scorrevole" avrebbe un'opzione per 48,2 casi, 47,921351 casi o qualsiasi numero vi venga in mente. Tuttavia, il conteggio effettivo dei casi di cancro è limitato ai numeri interi 1, 2, 3, \(\ldots\) , 48, 49, 50 perché non esiste un caso parziale di cancro.
</p>

<table>
  <td>
    <h3>Come si gestiscono le perdite non uniformi?</h3>
    <p align="justify">
    Può sembrare assurdo che l'accuratezza sia uno degli obiettivi predittivi più comuni, ma non possiamo usarla quando addestriamo un algoritmo. Eppure è così! Quindi, come gestiamo questo strano fenomeno? La risposta è creare un problema proxy . Un problema proxy è un modo alternativo di rappresentare un problema che è correlato a ciò che vogliamo risolvere, ma che si comporta meglio. In questo caso, utilizziamo una funzione di perdita di entropia incrociata invece dell'accuratezza. Anche se non entreremo nei dettagli della perdita di entropia incrociata in questa sede, il suo utilizzo dimostra che i problemi proxy sono trucchi fondamentali utilizzati nell'apprendimento automatico e nell'intelligenza artificiale.
    </p>
  </td>
</table>

<p align="justify">
Questa discussione ci porta a un altro aspetto fondamentale da considerare riguardo al modo in cui gli LLM apprendono, come accade per la maggior parte degli algoritmi: la tecnica che utilizziamo per addestrarli non è sempre focalizzata su ciò che vogliamo che facciano, ma su ciò che possiamo fargli imparare. Questa focalizzazione può portare a un disallineamento degli incentivi, con conseguenti risultati inaspettati o prestazioni scadenti. Discuteremo di come la natura della funzione di perdita di un LLM crei questo disallineamento degli incentivi dopo aver esaminato la seconda componente principale dell'addestramento: la discesa del gradiente.
</p>

<h3>4.1.2 Che cosa è la discesa del gradiente?</h3>

<p align="justify">
Disporre di una funzione di perdita è un prerequisito per eseguire una discesa del gradiente. La funzione di perdita indica oggettivamente quanto male si sta eseguendo il compito. La discesa del gradiente è il processo che utilizziamo per capire come modificare i parametri della rete neurale per ridurre la perdita subita. Questo viene fatto confrontando i dati di addestramento in ingresso e gli output effettivi rispetto a quelli attesi della rete neurale utilizzando la funzione di perdita. In questo caso, il gradiente è la direzione e l'entità di cui è necessario modificare i parametri di una rete neurale per ridurre l'entità dell'errore misurato dalla funzione di perdita. La discesa del gradiente ci mostra come modificare "solo un po'" tutti i parametri di una rete neurale per migliorarne le prestazioni e ridurre la differenza tra gli output attesi e quelli effettivi. Un diagramma di questo processo è mostrato nella figura 4.3 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.3 Input ed etichette (le risposte corrette note per ciascun input) vengono utilizzati per modificare la rete neurale durante la discesa del gradiente. Una rete è composta da parametri che vengono modificati di poco ogni volta che viene applicata la discesa del gradiente. Alla fine trasformiamo la rete in qualcosa di utile applicando la discesa del gradiente milioni o miliardi di volte.
      </p>
    </figcaption>
    
<img width="1100" height="728" alt="CH04_F03_Boozallen" src="https://github.com/user-attachments/assets/d72c5bd1-c96f-4a45-9a8d-5c4ef3ae9639" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Come mostra la figura 4.3 , creiamo una nuova rete leggermente diversa ogni volta che applichiamo la discesa del gradiente. Poiché le modifiche sono piccole, questo processo deve essere eseguito miliardi di volte. In questo modo, tutte le piccole modifiche si sommano per creare una modifica più significativa e significativa nella rete complessiva.
</p>

<p align="justify">
Nota: i moderni LLM eseguono miliardi di aggiornamenti dei parametri perché sono addestrati su miliardi di token. Più dati si hanno, più volte si esegue la discesa del gradiente. Meno dati si hanno, meno spesso è necessario eseguirla. I dati utilizzati per addestrare un LLM sono più di quanti se ne possano leggere in una vita.
</p>

<p align="justify">
La discesa del gradiente è un processo matematico che viene applicato ripetutamente senza deviazioni. Non vi è alcuna garanzia che funzioni o che trovi la soluzione migliore o addirittura valida. Ciononostante, molti ricercatori sono rimasti sorpresi dalla praticità di questo approccio relativamente semplice.
</p>

<p align="justify">
Per aiutarvi a comprendere il funzionamento della discesa del gradiente, useremo un semplice esempio: far rotolare una palla lungo una collina. La posizione della palla rappresenta un valore parametrico per un nodo della rete neurale che l'algoritmo di addestramento può modificare. L'altezza della collina rappresenta l'entità della perdita e descrive le scarse prestazioni del modello per l'input di addestramento. Vogliamo far rotolare la palla lungo la collina fino alla valle più profonda perché è l'area con la perdita più bassa, il che indica che il modello sta funzionando al meglio. Un esempio è mostrato nella figura 4.4.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.4 Questa figura mostra il quadro generale della discesa del gradiente applicata a un problema a parametro singolo. La curva illustra il valore della funzione di perdita per un dato valore del parametro. La posizione della pallina mostra la perdita per il valore corrente del parametro. L'obiettivo è trovare i valori dei parametri corrispondenti a un minimo globale che rappresenti la soluzione ideale con la perdita minima.
      </p>
    </figcaption>
    
<img width="1100" height="503" alt="CH04_F04_Boozallen" src="https://github.com/user-attachments/assets/83c41fe1-c075-4cec-8b72-cc12af5a167a" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Come potete vedere, la palla potrebbe cadere in molte valli. Nel gergo del settore, questo problema verrebbe definito "non convesso" , perché più percorsi portano a una perdita ridotta, ma ogni percorso non necessariamente progredisce verso la migliore soluzione possibile. È anche importante notare che questa non è un'analogia. La discesa del gradiente guarda letteralmente il mondo in questo modo. Questi esempi mostrano come funziona la discesa del gradiente per un modello con un solo parametro da ottimizzare. La stessa procedura viene applicata a miliardi di parametri durante l'addestramento di un LLM.
</p>

<p align="justify">
Da questa posizione, cerchiamo avidamente in quale direzione muovere la palla verso il basso. Applichiamo la discesa del gradiente due volte nella figura 4.5 . Questo mostra che l'opzione avida è a sinistra. Quando ci spostiamo a sinistra modificando il nostro parametro, spostiamo leggermente la palla lungo il pendio. Dal grafico, si può vedere che esiste una soluzione migliore cercando verso destra, ma a causa della semplicità dell'algoritmo, è improbabile che la discesa del gradiente la trovi. Trovare il risultato ottimale in questo caso richiederebbe una strategia più intelligente che coinvolga la ricerca e l'esplorazione, il che è troppo costoso per essere applicato bene nella pratica.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.5 L'algoritmo di discesa del gradiente adotta misure per regolare i parametri al fine di trovare il risultato ottimale con la perdita minima. Sfortunatamente, l'algoritmo si blocca in un minimo locale, un'area del grafico che non è ottimale perché altri valori dei parametri corrispondono ad aree con una perdita inferiore.
      </p>
    </figcaption>
    
<img width="1100" height="550" alt="CH04_F05_Boozallen" src="https://github.com/user-attachments/assets/7e55c764-348b-4b60-bdf0-a25d09ef8180" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Si noti inoltre che nel secondo passaggio della figura 4.5 , la pallina si blocca. Sebbene sia evidente che continuando a muoversi verso sinistra si otterrà una perdita ancora inferiore, questo risultato è ovvio solo perché possiamo vedere l'immagine completa. La discesa del gradiente non può vedere l'immagine completa o persino ciò che si trova nelle vicinanze. Conosce solo la posizione esatta grazie ai parametri correnti e alla funzione di perdita. Quindi, è una procedura greedy . Le procedure greedy come la discesa del gradiente sono approcci semplificati con la proprietà desiderata della computabilità, in quanto non sono eccessivamente costose da eseguire più volte per ottenere un risultato. Le procedure greedy sono miopi perché scelgono il passo ottimale successivo basandosi solo sullo stato attuale, sebbene possano esistere soluzioni più ampie e ottimali. Lo fanno perché valutare lo stato attuale e tutti i possibili stati futuri sarebbe impossibile a causa del numero di potenziali risultati da considerare. Sarebbe semplicemente troppo da calcolare. La speranza è che prendere molte semplici decisioni ottimali utilizzando informazioni limitate porti generalmente al risultato più positivo, in questo caso, minimizzando il valore della funzione di perdita.
</p>

<b>Importanti sfumature nella discesa del gradiente</b>

<p align="justify">
In questa discussione sulla discesa del gradiente, abbiamo tralasciato alcune sfumature importanti che devono essere considerate per l'uso nel mondo reale. Innanzitutto, come descritto qui, la discesa del gradiente dovrebbe utilizzare tutti i dati di training simultaneamente, il che è computazionalmente irrealizzabile. Utilizziamo invece una procedura chiamata discesa del gradiente stocastica (SGD). La SGD è esattamente la stessa che abbiamo descritto, tranne per il fatto che utilizza un piccolo sottoinsieme casuale dei dati di training invece dell'intero set di dati. Questo riduce drasticamente la memoria necessaria per addestrare il modello, con conseguenti soluzioni più rapide e migliori. Questo metodo funziona perché la discesa del gradiente apporta solo piccole modifiche alla direzione greedy corrente. Si scopre che una piccola quantità di dati è quasi altrettanto efficace che utilizzarli tutti quando si decide quale passo intraprendere. Se si dispone di un miliardo di token, è possibile eseguire un miliardo di passaggi SGD all'incirca nello stesso tempo necessario per eseguire un passaggio standard di discesa del gradiente utilizzando tutti i dati.
</p>

<p align="justify">
Molti approcci di training utilizzano una particolare forma di SGD chiamata Adaptive MomentEstimation (Adam). Adam include alcuni trucchi aggiuntivi per aiutare a minimizzare più velocemente la funzione di perdita ed evitare di rimanere bloccati. Il trucco principale di Adam è che fornisce alla palla un certo slancio, che aumenta man mano che gli aggiornamenti si muovono continuamente in una direzione. Questo slancio fa sì che la palla rotoli giù per la collina più velocemente e significa che, se viene raggiunto un piccolo minimo locale, potrebbe esserci abbastanza slancio per superare quel punto e continuare ad avanzare, raggiungendo così l'area del grafico della funzione di perdita con la minore quantità di perdita.
</p>

<p align="justify">
Lo svantaggio di Adam è che memorizzare queste informazioni sulla quantità di moto per ciascun parametro aumenta la memoria richiesta per l'addestramento di un fattore tre rispetto al semplice SGD. La memoria è il fattore più critico quando si costruiscono LLM perché spesso determina il numero di GPU necessarie, il che si traduce in denaro speso. Sebbene Adam non renda il modello finale più grande perché si rischia di buttare via i dati relativi ai calcoli aggiuntivi sulla quantità di moto di Adam una volta completato l'addestramento, è comunque necessario un sistema sufficientemente grande per eseguire l'addestramento in primo luogo. La maggiore precisione che deriva dalla capacità di Adam di ridurre al minimo le perdite in modo più efficace ha un prezzo da pagare.
</p>

<h3>4.2 Gli LLM imparano a imitare il testo umano</h3>

<p align="justify">
Ora che abbiamo capito come gli algoritmi di deep learning vengono addestrati specificando una funzione di perdita utilizzata con la discesa del gradiente, possiamo discutere come questa viene applicata agli LLM. Nello specifico, ci concentreremo sui dati e sulle funzioni di perdita o ricompensa utilizzate per addestrare gli LLM.
</p>

<p align="justify">
Gli LLM sono generalmente addestrati su testi scritti da esseri umani. Nello specifico, sono addestrati esplicitamente a imitare testi prodotti da esseri umani. Sebbene questo possa sembrare un po' ovvio (a cosa altro dovrebbero essere addestrati?), questo dettaglio viene spesso trascurato o confuso con altri aspetti, persino dagli esperti del settore. In particolare, i modelli linguistici non sono addestrati per svolgere nessuna delle seguenti attività:
</p>

<ul>
  <li>
    <p align="justify">
    Memorizzare il testo
    </p>
  </li>
  <li>
    <p align="justify">
    Generare nuove idee
    </p>
  </li>
  <li>
    <p align="justify">
    Costruisci rappresentazioni del mondo
    </p>
  </li>
  <li>
    <p align="justify">
    Produrre un testo fattualmente accurato
    </p>
  </li>
</ul>

<p align="justify">
È essenziale spiegare ulteriormente questo concetto prima di approfondire. Quando si addestra un modello a giocare a scacchi, il modello impara a giocare bene perché viene ricompensato per la vittoria. Un modello linguistico, al contrario, viene ricompensato solo per la produzione di testo che assomiglia esattamente ai dati di addestramento. Di conseguenza, tutto il testo generato dall'LLM che assomiglia al testo del corpus di addestramento produce ricompense elevate (o perdite basse), anche quando tali generazioni non sono veritiere o fattuali. Questo è un esempio di disallineamento tra la funzione di perdita e l'obiettivo di livello superiore del progettista, come discusso nella sezione 4.1.
</p>

<p align="justify">
Gli LLM vengono addestrati su dataset di centinaia di gigabyte di testo estratti da Internet. Internet è noto per contenere una grande quantità di informazioni errate (e strane). Gli LLM che sono più bravi nella maggior parte dei compiti spesso finiscono per essere peggiori in compiti che sono comunemente travisati nei loro dati di addestramento (vedi l'Inverse Scaling Prize su https://github.com/inverse-scaling/prize ). Ad esempio, i ricercatori hanno costantemente scoperto che i modelli linguistici migliori sono anche più bravi a riprodurre conoscenze comuni false [3], imitando stereotipi e pregiudizi sociali [4]. Tendono a cadere in una spirale discendente che rafforza gli errori. Ad esempio, dopo aver generato codice contenente bug, è più probabile che generino codice contenente bug aggiuntivi [5]. Questi elementi sono comunemente rappresentati nel testo di addestramento, quindi gli LLM vengono premiati positivamente per averli previsti, anche se errati. Pertanto, migliorare in base alla sua funzione di perdita per un LLM significa anche peggiorare in questi compiti che richiedono verità e correttezza.
</p>

<h3>4.2.1 Funzioni di ricompensa LLM</h3>

<p align="justify">
In precedenza, abbiamo detto che gli LLM vengono premiati per la produzione di dati che "sembrano simili ai propri dati di addestramento". In questa sottosezione, esploreremo più concretamente cosa questo significhi.
</p>

<p align="justify">
Gli LLM vengono addestrati mostrando i primi due token di una frase e chiedendo loro di predire il token successivo. La perdita si basa sull'accuratezza di tale previsione rispetto ai dati di addestramento. Ad esempio, potrebbe essere mostrato "Questo è un" e ci si aspetta che produca "test". Se il modello produce "test", ottiene un punto, altrimenti ne perde uno. Questo processo viene eseguito per tutti i segmenti iniziali del testo, come mostrato nella figura 4.6 . Qui, il modello viene addestrato a predire ciascuna delle parole evidenziate in modo indipendente. Questa configurazione non è esclusiva degli LLM. È stata utilizzata per addestrare reti neurali ricorrenti (RNN) per molti anni. Tuttavia, uno dei motivi essenziali per cui gli LLM sono diventati così popolari è che possono essere addestrati in modo molto più efficiente di una RNN. Una RNN deve essere addestrata su ogni generazione in modo sequenziale, poiché ogni nuova parola generata dipende dalle parole scelte in precedenza. Un LLM può essere addestrato su tutte le generazioni in parallelo grazie all'architettura del trasformatore discussa nel capitolo 3. La possibilità di addestrare un modello su generazioni correlate in parallelo rappresenta un'accelerazione enorme, consentendo l'addestramento su larga scala ed è un prerequisito per la creazione degli LLM all'avanguardia di oggi utilizzando terabyte di dati.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.6 Un LLM vede questa frase nove volte, ogni volta imparando dalla previsione di una singola parola alla fine di ciascuna delle nove sequenze.
      </p>
    </figcaption>
    
![CH04_F06_Boozallen](https://github.com/user-attachments/assets/bfd9adfd-1971-4630-8a08-2990d7be4ca9)

  </figure>
</div>
  </td>
</table>

<p align="justify">
Abbiamo discusso di come la previsione del token successivo possa essere problematica perché l'algoritmo potrebbe essere incentivato a produrre output errati o fattualmente errati. Dobbiamo anche discutere l'intuizione alla base del perché, nonostante ciò, questo approccio possa produrre output così convincenti. È ragionevole chiedersi: come può un algoritmo addestrato per creare il token più probabile successivo eseguire apparentemente qualcosa che potremmo scambiare per ragionamento?
</p>

<p align="justify">
Per sviluppare questa intuizione, immagina come potresti provare a predire il token successivo per una data frase. Un computer non ha alcuna pressione per rispondere rapidamente, quindi prenditi il tuo tempo. Considera la frase "Adoro mangiare <spazio vuoto>" e prova a indovinare quale parola potrebbe essere inserita nello "spazio vuoto". Le parti iniziali della frase ti forniscono un contesto prezioso. Dato che stiamo parlando di mangiare, puoi quasi immediatamente restringere l'ambito a un alimento. Tenere un elenco di tutti i possibili alimenti non è difficile per un computer.
</p>
  
<p align="justify">
Ora, se consideriamo il background degli autori di questo libro, avremo ancora più contesto. Siamo americani e viviamo in un'area geografica comune, il che rende più probabile la presenza di cucine specifiche rispetto ad altre. Un LLM non avrà questo background, ma se la frase fosse più lunga e avesse più contesto, potremmo iniziare a restringere le scelte come mostrato nella figura 4.7 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.7 Il contesto può aiutarti a fare previsioni attendibili sulla parola successiva. Spostandoti da sinistra a destra, viene aggiunto testo aggiuntivo che potrebbe comparire in una frase. Le immagini nel fumetto di ogni frase mostrano come il contesto aggiunto elimini le previsioni.
      </p>
    </figcaption>
    
<img width="1100" height="171" alt="CH04_F07_Boozallen" src="https://github.com/user-attachments/assets/66f3ffb3-ffc4-4b6f-9360-53a9306e4202" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Identificando parole chiave o frasi nel testo precedente, è possibile ottenere informazioni sulla parola migliore da predire in seguito. Un computer che esegue questi calcoli esegue molte più elaborazioni di quanto un essere umano richieda. Questo tipo di associazione basata sulla forza bruta limita sostanzialmente l'ambito a qualcosa di molto ragionevole. Ancora una volta, il modello verrà aggiornato miliardi di volte per perfezionare queste associazioni e acquisire così una capacità utile correlata ai nostri obiettivi di un algoritmo in grado di comprendere e reagire al testo umano.
</p>

<p align="justify">
Tuttavia, correlazione non è causalità e la strategia di predizione della parola successiva può portare a errori umoristici. Gli LLM sono suscettibili all'errore di "petizione di principio", in cui la premessa della domanda implica qualcosa di falso. Poiché l'LLM non è addestrato per l'accuratezza o la contraddizione, tenta di produrre una sequenza di previsioni testuali di tipo umano che potrebbero seguire la tua domanda fuorviante. Un esempio di ChatGPT alle prese con questo tipo di problema è mostrato nella figura 4.8 , dove ci interroghiamo sull'eccezionale resistenza degli spaghetti secchi.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.8 Sebbene la previsione del token successivo sia potente, non fornisce alla rete capacità di ragionamento o logica. Se chiediamo a ChatGPT qualcosa di assurdo e falso, spiega volentieri come accade.
      </p>
    </figcaption>
    
![CH04_F08_Boozallen](https://github.com/user-attachments/assets/a52715af-4e7f-4a4c-b7ad-87d6dd8dff1c)

  </figure>
</div>
  </td>
</table>

<p align="justify">
Il motivo per cui gli spaghetti possono sostenere un peso centinaia di volte superiore al loro è assurdo e falso. Tuttavia, l'algoritmo è stato predisposto per fornire una risposta sulla resistenza alla trazione del materiale formattando la domanda: "Perché X è così resistente?". Il modello può estrarre questo contesto chiave. I dati di training precedenti probabilmente spiegano tali proprietà del materiale sulla base di una domanda fattuale, che informa il modello prevedendo che una risposta simile sia appropriata. Il soggetto della frase (spaghetti) e l'oggetto (peso di 10 libbre) vengono utilizzati per fornire dettagli minori della risposta, che altrimenti è generica.
</p>

<h3>4.3 LLM e nuovi compiti</h3>

<p align="justify">
La natura della strategia autoregressiva di previsione della parola successiva e il suo utilizzo come perdita o ricompensa durante il processo di formazione ci fornisce preziose informazioni sulla natura delle risposte generate da un LLM e su come possano essere potenzialmente inaccurate dal punto di vista fattuale. Tuttavia, ci mostra anche perché gli LLM possono essere efficaci per la ricerca di informazioni, in quanto ricerca per parole chiave molto più potente di un motore di ricerca standard. Esistono modi per aggirare i limiti delle risposte non fattuali. Ad esempio, molti approcci LLM aggiungono citazioni all'output generato in modo che sia possibile verificare rapidamente che il contenuto utilizzato per produrre il testo generato sia stato accurato dal punto di vista fattuale. Un LLM può anche essere una preziosa cassa di risonanza, uno pseudo-partner con cui scambiare idee come fonte di ispirazione e creatività. Fondamentalmente, questo aiuta anche a comprendere un caso chiave in cui è meglio evitare gli LLM perché saranno più propensi a generare errori: problemi e compiti nuovi.
</p>

<p align="justify">
Gli LLM generalmente non sono bravi a svolgere compiti nuovi. Capire se il tuo compito è nuovo può essere piuttosto impegnativo, dato che Internet è strano. Esistono tonnellate di cose casuali su Internet, inclusi concorsi su come disegnare anatre e unicorni in modo programmatico [6]. Se il compito è sufficientemente simile a uno già visto in precedenza o strutturalmente simile ad altri elementi nei dati di addestramento, potresti ottenere qualcosa di apparentemente ragionevole. Questo risultato può essere estremamente utile, ma può peggiorare man mano che il tuo compito diventa più unico rispetto a ciò che esiste nei dati di addestramento.
</p>

<p align="justify">
Ad esempio, abbiamo chiesto a ChatGPT di scrivere codice che calcolasse la costante matematica \(\pi\) (pi greco) in Python. Questo compito non è nuovo; online esistono tonnellate di codice simile e ChatGPT ci restituisce fedelmente il codice corretto.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    
<img width="492" height="183" alt="image" src="https://github.com/user-attachments/assets/705f0021-e930-4b3b-b52f-3c67f67f341a" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Ora forziamo ChatGPT a fare un'estrapolazione non particolarmente impegnativa. Abbiamo chiesto a ChatGPT di tradurre questa funzione nel linguaggio di programmazione Modula-3. Questo compito non è un'estrapolazione troppo impegnativa; Modula-3 è un linguaggio di programmazione con uno stile simile e un linguaggio di programmazione storicamente significativo che ha influenzato la progettazione finale di quasi tutti i linguaggi di programmazione più popolari oggi! Tuttavia, è eccessivamente esoterico. Oggi si possono trovare pochissimi esempi di questo linguaggio di programmazione, principalmente nel contesto delle classi dei compilatori universitari. Il seguente elenco mostra il ragionevole tentativo di ChatGPT. Come avrete potuto prevedere dal contesto di questo capitolo finora, ChatGPT ha commesso alcuni errori, evidenziati nell'elenco.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    
<img width="490" height="292" alt="image" src="https://github.com/user-attachments/assets/147221a8-e316-45f2-839f-0a8464c12ad3" />

  </figure>
</div>
  </td>
</table>


<p align="justify">
Questo breve programma presenta tre errori che ne impedirebbero il funzionamento. È ancora più interessante che ChatGPT li sbagli perché estrapola con sicurezza le pratiche di programmazione standard di altri linguaggi. (In questo caso, con sicurezza significa che ChatGPT non ci avvisa dei suoi potenziali errori. Uno degli autori ama dire che ChatGPT sembra il loro amico più presuntuoso e spesso inesatto.) In questo caso, **è una funzione di elevamento a potenza comunemente usata, quindi ChatGPT decide che Modula-3 supporta questa operazione. Per quanto possiamo dedurre dalle ricerche su Internet, Modula-3 non ha esempi documentati di come elevare a potenza una variabile. Poiché la maggior parte dei linguaggi di programmazione supporta questa azione con un'opzione ^, **, o pow(), ChatGPT ne estrapola semplicemente una. La risposta corretta sarebbe che deve prima implementare una powfunzione e poi usarla per calcolare pi greco.
</p>

<p align="justify">
Un altro mistero sono gli argomenti forniti alla PutRealfunzione. La nostra ipotesi migliore è che 15corrisponda a un'estrapolazione della stampa di 15 cifre di un valore in virgola mobile, un'impostazione predefinita tipica per il calcolo di pi greco. In ogni caso, non è così che funziona quella funzione.
</p>

<p align="justify">
Il punto più significativo è che ChatGPT coglie correttamente alcuni dettagli, ma solo per le parti che si trovano su Internet e sono già spiegate (ad esempio, FLOAT(i)è richiesto, come sta facendo 4.0 * piinvece di 4 * pi). Le attività senza esempi su Internet sono quelle in cui ChatGPT commette errori.
</p>

<p align="justify">
Questo esempio evidenzia anche i limiti del "ragionamento" percepito rispetto a quello effettivo negli attuali LLM. La specifica completa del linguaggio per Modula-3 è disponibile online e ha documentato tutti questi dettagli o la loro assenza. ChatGPT ha quasi sicuramente esaminato molte altre specifiche di linguaggi di programmazione, specifiche di parser e milioni di righe di codice nei linguaggi di programmazione più comuni. Se una persona avesse queste conoscenze di base e risorse, eseguire l'induzione logica necessaria per evitare tutti e tre gli errori non dovrebbe essere troppo impegnativo. Tuttavia, l'LLM non esegue alcun processo di induzione e, quindi, commette errori nonostante l'ampiezza delle informazioni disponibili.
</p>

<p align="justify">
Ciò non significa che il risultato non sia di grande impatto, e che possa rivelarsi uno strumento prezioso per accelerare lo sviluppo del proprio codice o l'utilizzo di API e linguaggi non familiari. Tuttavia, dimostra anche che tali strumenti funzioneranno molto meglio con linguaggi e API ampiamente utilizzati e documentati, soprattutto se conformi agli standard previsti. Ad esempio, la maggior parte dei database utilizza il linguaggio SQL, il che rende più probabile un'estrapolazione accurata di come utilizzare un nuovo database che utilizza anch'esso SQL.
</p>

<h3>4.3.1 Mancata identificazione del compito corretto</h3>

<p align="justify">
Un altro caso degno di nota in cui gli LLM falliscono è quando non riescono a identificare correttamente il compito che dovrebbero svolgere e invece rispondono a una domanda diversa da quella intesa dall'utente. L'incapacità di identificare correttamente il compito rappresentava un problema sostanziale per modelli come il GPT-3 originale, ma il lavoro successivo volto ad aumentare il numero di esempi strutturati per compito nei dati di addestramento ha notevolmente migliorato la capacità dei modelli ChatGPT successivi di seguire le istruzioni. Tuttavia, in alcuni casi, ChatGPT continua a non riuscire a identificare il compito corretto. Ad esempio, questo comportamento può essere ottenuto in modo affidabile chiedendo informazioni su un compito insolito, leggermente diverso da un compito comune, o modificando un problema che ha già incontrato molte volte in modo non familiare.
</p>

<p align="justify">
Un esempio è un famoso enigma logico che riguarda il trasporto di un cavolo, una capra e un lupo attraverso un fiume in barca. L'enigma stabilisce che la capra non può essere lasciata sola con il cavolo (perché la capra lo mangerebbe) o con il lupo (che divorerebbe la capra). ChatGPT può risolvere rapidamente questo enigma, ma se modifichiamo leggermente la struttura logica dell'enigma, il modello continua a utilizzare il vecchio ragionamento, come mostrato nella figura 4.9 .
</p>

<p align="justify">
Sebbene sia spesso difficile ricondurre gli errori commessi dagli LLM a cause specifiche, in questo caso il modello ci dice allegramente di "assicurarci che nessuno degli elementi (cavolo, capra, lupo) venga lasciato insieme senza supervisione". Sebbene questa istruzione sia corretta nella versione originale del problema cavolo/capra/lupo (e probabilmente si basasse sulla specifica dei vincoli nel problema logico), il modello non sa che la versione data non presenta problemi con la capra e il lupo che si trovano insieme da soli. Non solo non è necessario scambiare gli animali come suggerito, ma il consiglio di ChatGPT fallirà perché posiziona il lupo e il cavolo insieme, cosa che abbiamo esplicitamente vietato.
</p>

<p align="justify">
Un altro curioso esempio di questo fenomeno si verifica quando si elimina la necessità di lasciare qualcosa indietro. Qualsiasi comprensione logica del puzzle chiarisce che è sufficiente caricare tutto sulla barca e attraversare. Ancora una volta, il modello è troppo abituato a rispondere alla versione del problema che ha già visto molte volte e lo fa.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.9 ChatGPT non riesce a risolvere due versioni modificate di un classico enigma logico a causa del modo in cui vengono addestrati i LLM. Il contenuto che ricorre frequentemente nella stessa forma generale (ad esempio, un famoso enigma logico) induce il modello a riproporre la risposta frequente. Questo può accadere anche quando il contenuto viene modificato in modi importanti e ovvi per una persona.
      </p>
    </figcaption>
    
<img width="1100" height="644" alt="CH04_F09_Boozallen" src="https://github.com/user-attachments/assets/c3a7ae03-d341-4cdd-ab2f-49069dcc22ab" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Per comprendere perché ciò accada, è importante ricordare la natura autoregressiva della formazione LLM discussa nel capitolo 3. Il modello è esplicitamente incentivato a generare contenuti basati su contenuti precedenti. Il contenuto generato per risolvere il puzzle logico riformulato appare quasi esattamente uguale al contenuto che risolve il puzzle logico originale in termini di parole e ordine. Di conseguenza, è una buona corrispondenza fuzzy nella query e nell'abbinamento delle chiavi del livello di trasformazione a produrre i valori che compongono la soluzione del puzzle originale. La corrispondenza fuzzy viene effettuata e la soluzione precedente viene restituita fedelmente tramite il meccanismo di attenzione utilizzato dai trasformatori. Sebbene questa strategia sia eccellente per il modello per prevedere correttamente i token per il famoso puzzle, non implica il ragionamento attraverso la logica del puzzle.
</p>

<h3>4.3.2 Gli LLM non possono pianificare</h3>

<p align="justify">
Un altro sottile limite della natura autoregressiva degli LLM è che possono lavorare solo con le informazioni che vedono nel contesto. Gli LLM sono addestrati a ricevere un input e produrre una continuazione plausibile. Tuttavia, non possono pianificare, prendere impegni o tracciare stati interni. Un ottimo esempio si verifica quando si tenta di giocare al gioco "20 domande" con ChatGPT. Quando un essere umano gioca a 20 domande, si impegna preventivamente a un'informazione nascosta, l'oggetto che ha scelto di identificare tramite le risposte. Quando ChatGPT gioca a questo gioco, risponde alle domande individualmente e poi, a posteriori, trova un output coerente con le risposte fornite. Questo esempio è illustrato nella figura 4.10 , che mostra possibili alberi di dialogo per giocare a 20 domande. Quando qualcuno gioca a un gioco con un LLM, uno di questi alberi di dialogo viene scelto casualmente invece di trovare un oggetto target che rimanga coerente per tutta la partita.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
      Figura 4.10 L'agente di dialogo non si impegna su un oggetto specifico all'inizio del gioco.
      </p>
    </figcaption>
    
<img width="1100" height="538" alt="CH04_F10_Boozallen" src="https://github.com/user-attachments/assets/74b3a302-debe-407f-af72-7affb9b88363" />

  </figure>
</div>
  </td>
</table>

<h3>4.4 Se gli LLM non riescono a estrapolare bene, posso utilizzarli?</h3>

<p align="justify">
La maggior parte del lavoro da svolgere non è né nuovo né innovativo. Almeno, non è così nuovo o innovativo da far fallire un LLM. Tuttavia, comprendere che le capacità di un LLM peggiorano rapidamente man mano che è richiesta maggiore logica o sottigliezza può aiutare a restringere l'ambito di utilizzo.
</p>

<p align="justify">
Quando progettiamo sistemi informatici di livello produttivo, un fattore essenziale da considerare è l'ambito di utilizzo dello strumento. Quando si rende disponibile un prodotto LLM come ChatGPT a un pubblico generico senza un ambito specifico, le persone gli chiederanno di fare ogni sorta di cose casuali e folli inaspettate. Sebbene questo possa essere ottimo per la ricerca, spesso non è pratico per le applicazioni di produzione. Sebbene i vostri utenti e clienti cercheranno di fare cose imprevedibili con la vostra applicazione LLM, supponete di limitare l'accesso al sistema e di progettare in modo che i vostri utenti abbiano un obiettivo specifico, casi d'uso limitati o persino limitino il modo in cui i loro input arrivano al vostro LLM. In tal caso, potete creare qualcosa con un'esperienza utente molto più affidabile.
</p>

<table align="center">
  <td>
    <h3>Come posso utilizzare un LLM senza l'input dell'utente?</h3>
    <p align="justify">
Gli LLM sono eccellenti nel fornire codifica o elaborazione dati a basso sforzo, soprattutto quando si svolgono attività quotidiane su dati non formattati o curati in modo così pulito. Tuttavia, è possibile ottenere utilità senza troppi rischi offrendo agli utenti un insieme finito di scelte. Avere un insieme limitato di prompt come codice tra cui un utente può scegliere o lasciare che sia l'utente a decidere su quale fonte dati (ad esempio, un database interno) eseguire un prompt consente di evitare che (la maggior parte) delle persone fornisca a un LLM testo arbitrario.
  </p>
  </td>
</table>

<p align="justify">
Potreste invece chiedervi: "Possiamo rilevare nuove richieste e segnalare all'utente un errore?". Ipoteticamente, sì, potreste provare a farlo. Innanzitutto, lo sconsigliamo perché non è ottimale dal punto di vista dell'esperienza utente. In secondo luogo, diventa un'attività nota come rilevamento di novità o rilevamento di valori anomali . Questo problema è impegnativo ed è probabilmente impossibile da risolvere in modo da garantire l'assenza di errori. Di conseguenza, incoraggiamo la prevenzione rispetto al rilevamento, scegliendo casi d'uso che non richiedono una previsione altamente accurata dei guasti attraverso l'analisi di input o output LLM.
</p>

<table align="center">
  <td>
    <h3>Applicazioni per sollecitare</h3>
    <p align="justify">
    Il prompting è l'arte di elaborare un input per un ampio modello linguistico che induca un comportamento desiderabile. I modelli linguistici possono essere molto sensibili all'esatta inquadratura dei loro input, rendendo la capacità di progettare input a cui venga data una risposta appropriata molto preziosa. Un tema ricorrente nell'uso degli LLM è che le persone in genere non pensano a come interagire correttamente con essi. Il modo migliore per sollecitare un LLM è pensare a come apparirebbe il tipo di output a cui si è interessati nei dati di addestramento e poi scriverne il primo quarto. Invece, le persone spesso descrivono il compito che desiderano che un modello linguistico svolga, dando per scontato che questa chiarificazione manterrà l'LLM concentrato sul problema. Sfortunatamente, questo approccio produce risultati incoerenti e ha ispirato la ricerca sull'ottimizzazione degli LLM fornendo loro un gran numero di istruzioni e risposte come dati di addestramento.
  </p>
  </td>
</table>

<h3>4.5 Più grande è meglio?</h3>

<p align="justify">
Nel 2019, Rich Sutton ha coniato il termine “la lezione amara” per descrivere la sua esperienza con l’apprendimento automatico. “La lezione più importante che si può trarre da 70 anni di ricerca sull’intelligenza artificiale è che i metodi generali che sfruttano il calcolo sono in definitiva i più efficaci, e con un ampio margine” [7].
</p>

<p align="justify">
C'è la genuina sensazione che i trasformatori siano l'esempio per eccellenza di questo principio. È possibile continuare a ingrandirli, addestrarli con maggiore parallelismo e aggiungere più GPU. Questo differisce notevolmente dalle reti neurali reticolari (RNN), che non possono essere parallelizzate con la stessa efficienza di un trasformatore. Lo osserviamo anche nel dominio delle immagini con i metodi GAN (Generative Adversarial Network), che faticano a raggiungere la scala del miliardo di parametri. I metodi basati sui trasformatori utilizzati negli LLM scalano facilmente fino a decine di miliardi, consentendo la costruzione di modelli più grandi e migliori.
</p>

<p align="justify">
Dal punto di vista della progettazione di soluzioni, il vostro prototipo attuale potrebbe incontrare vincoli significativi dovuti alle dimensioni del modello. Modelli più grandi richiedono più risorse e impiegano più tempo per effettuare previsioni. Qual è il tempo di risposta massimo che i vostri utenti accetteranno? Quanto è costoso l'hardware necessario per eseguire il vostro modello a questa velocità? Il tasso di crescita delle dimensioni del modello supera il tasso di crescita dell'hardware consumer. Di conseguenza, potreste non essere in grado di distribuire il vostro modello su dispositivi embedded o potreste aver bisogno di una connettività Internet per ridurre i costi. Di conseguenza, dovete considerare l'infrastruttura di rete nella vostra progettazione per gestire la necessità di una connessione continua. Questo requisito aumenta il consumo di batteria, un fattore da considerare quando si utilizza continuamente una radio Wi-Fi anziché un'elaborazione locale. Pertanto, sebbene i modelli più grandi siano più accurati, i vincoli di progettazione potrebbero impedirne l'implementazione pratica. Combinando questi vincoli con le nozioni su come gli LLM effettuano le loro previsioni e i casi d'uso di quando e dove gli LLM falliscono, appresi in questo capitolo, sarete in grado di comprendere come utilizzare gli LLM per risolvere i problemi che vi interessano nel modo più efficace.
</p>

<h3>Riepilogo</h3>
<ul>
  <li>
  <p align="justify">
  L'apprendimento profondo necessita di una funzione perdita/ricompensa che quantifichi specificamente quanto un algoritmo sia incapace di fare previsioni
  </p>
  </li>
  <li>
  <p align="justify">
  Questa funzione perdita/ricompensa dovrebbe essere progettata per essere correlata all'obiettivo generale di ciò che vogliamo che l'algoritmo realizzi nella vita reale.
  </p>
  </li>
    <li>
  <p align="justify">
  La discesa del gradiente comporta l'utilizzo incrementale di una funzione perdita/ricompensa per modificare i parametri della rete.
  </p>
  </li>
    <li>
  <p align="justify">
  Gli LLM sono addestrati a imitare il testo umano prevedendo il token successivo. Questo compito è sufficientemente specifico da consentire l'addestramento di un modello per eseguirlo, ma non è perfettamente correlato a obiettivi di alto livello come il ragionamento.
  </p>
  </li>
    <li>
  <p align="justify">
  Gli LLM daranno il massimo delle loro prestazioni su compiti simili a quelli comuni e ripetitivi osservati nei dati di addestramento, ma falliranno quando il compito è sufficientemente nuovo.
  </p>
  </li>
</ul>

<h2>5 Come possiamo limitare il comportamento degli LLM?</h2>

<table>
  <td>
    <h3>Questo capitolo copre</h3>
    <ul>
      <li>
      <p align="justify">
Limitare il comportamento degli LLM per renderli più utili
      </p>
      </li>
      <li>
      <p align="justify">
Le quattro aree in cui possiamo limitare il comportamento LLM
      </p>
      </li>
      <li>
      <p align="justify">
Come la messa a punto ci consente di aggiornare gli LLM
      </p>
      </li>
      <li>
      <p align="justify">
Come l'apprendimento per rinforzo può cambiare l'output degli LLM
      </p>
      </li>
      <li>
      <p align="justify">
Modifica degli input di un LLM utilizzando la generazione aumentata del recupero
      </p>
      </li>
    </ul>
  </td>
</table>

<p align="justify">
Potrebbe sembrare controintuitivo pensare di poter rendere un modello più utile controllando l'output che il modello è autorizzato a produrre, ma è quasi sempre necessario quando si lavora con gli LLM. Questo controllo è reso necessario dal fatto che, quando gli viene presentato un prompt di testo arbitrario, un LLM tenterà di generare quella che ritiene essere una risposta appropriata, indipendentemente dall'uso previsto. Si consideri un chatbot che aiuta un cliente ad acquistare un'auto: non si vuole che l'LLM esca dal copione e parli di atletica o sport solo perché ha chiesto qualcosa relativo all'uso del veicolo per le partite di calcio dei figli.
</p>

<p align="justify">
In questo capitolo, discuteremo più in dettaglio perché si desidera limitare, o vincolare, l'output prodotto da un LLM e le sfumature associate a tali vincoli. Vincolare accuratamente un LLM è una delle cose più difficili da realizzare a causa della natura del modo in cui gli LLM vengono addestrati a completare l'input in base a ciò che osservano nei dati di addestramento. Attualmente, non esistono soluzioni perfette. Discuteremo i quattro potenziali ambiti in cui il comportamento di un LLM può essere modificato:
</p>

<ul>
  <li>
    <p align="justify">
Prima che avvenga la formazione, curare i dati utilizzati per addestrare l'LLM
    </p>
  </li>
  <li>
    <p align="justify">
Modificando il modo in cui viene impartito l'LLM
    </p>
  </li>
  <li>
    <p align="justify">
Ottimizzando l'LLM su un set di dati
    </p>
  </li>
  <li>
    <p align="justify">
Scrivendo un codice speciale dopo il completamento dell'addestramento per controllare gli output del modello
    </p>
  </li>
</ul>

<p align="justify">
Questi quattro casi sono riassunti nella figura 5.1 . Ogni fase di sviluppo di un LLM alimenta la successiva. La fase di fine-tuning, un secondo ciclo di addestramento eseguito su un set di dati più piccolo, è la più importante per il funzionamento attuale di strumenti come ChatGPT e l'approccio più probabile da utilizzare nella pratica. La prima fase di addestramento, più ampia, di cui abbiamo parlato nei capitoli da 2 a 4, è spesso definita pre-addestramento , perché avviene prima che la messa a punto renda il modello utile. Il modello prodotto dal processo di pre-addestramento è talvolta definito modello di base o modello di fondazione , perché rappresenta il punto di partenza per costruire un modello specifico per un'attività, o perfezionato.
</p>


<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.1 È possibile intervenire per modificare o limitare il comportamento di un LLM in quattro punti. Le due fasi di addestramento del modello sono mostrate al centro del diagramma, dove vengono modificati i parametri del modello. A sinistra, è anche possibile modificare i dati di addestramento prima dell'addestramento del modello. A destra, è possibile intercettare gli output del modello dopo l'addestramento e scrivere codice per gestire situazioni specifiche.        
      </p>
    </figcaption>
    
<img width="1100" height="432" alt="CH05_F01_Boozallen" src="https://github.com/user-attachments/assets/afbbd0f1-300d-4cfb-bef0-43385289c6b1" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Data l'importanza e l'efficacia della messa a punto fine, dedicheremo la maggior parte del capitolo a questo fattore e a come può essere eseguito.
</p>

<h3>5.1 Perché vogliamo limitare il comportamento?</h3>

<p align="justify">
Gli LLM hanno un successo incredibile perché sono la prima tecnologia a realizzare l'idea di "Dire a un computer cosa fare in parole semplici, e lui lo fa". Essendo molto espliciti su ciò che si desidera che accada, stabilendo un livello di dettaglio specifico e specificando un certo tono, è possibile rendere un LLM uno strumento incredibilmente efficace. Questo insieme dettagliato di istruzioni è chiamato prompt , e l'arte di progettare un buon prompt è stata definita " ingegneria dei prompt" . Ad esempio, potremmo sviluppare un prompt per un bot che vende auto, come mostrato nella figura 5.2 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.2 Gli LLM commerciali come ChatGPT sono progettati per seguire le istruzioni (entro certi limiti) e possono svolgere molti compiti a basso livello cognitivo o di pattern matching con un'efficacia molto elevata. Questi compiti includono la scrittura stilizzata, come il pattern matching, e il seguire le istruzioni, come il gioco di ruolo di un venditore di automobili.        
      </p>
    </figcaption>
    
![CH05_F02_Boozallen](https://github.com/user-attachments/assets/59962c53-2bfc-48e9-a593-6b06a8687953)

  </figure>
</div>
  </td>
</table>

<p align="justify">
Si potrebbe fornire a un LLM un prompt su come organizzare i dati in valori separati da virgole, in modo da poterli copiare in Excel. Si potrebbe progettare un prompt su come categorizzare le risposte a un sondaggio in forma libera in temi riassuntivi. In tutti i casi, il prompt è un esercizio per limitare, o vincolare, il comportamento a un compito specifico e a un insieme di obiettivi. Tuttavia, le tecniche di tokenizzazione e di addestramento che abbiamo discusso nei capitoli precedenti non consentono questo tipo di istruzione.
</p>

<p align="justify">
Ricordare che i modelli fanno ciò per cui sono stati addestrati è essenziale. Nel caso di un LLM standard, il compito consiste nel prendere un brano di testo e generare una continuazione di quel documento che assomigli a un tipico brano del corpus di addestramento con l'inizio fornito. Non è addestrato a rispondere a domande, pensare, riassumere il testo, sostenere una conversazione o altro. Per ottenere questo comportamento desiderabile di "istruzioni in sequenza", dobbiamo eseguire un fine-tuning, un secondo ciclo di addestramento con obiettivi diversi che produrranno il comportamento desiderato. Potreste chiedervi: "Perché non addestriamo gli LLM per il compito che vogliamo che svolgano?". Nella maggior parte delle applicazioni di deep learning, consigliamo vivamente di seguire il processo definito nel capitolo 4 per creare una funzione di perdita specifica, calcolabile e fluida. Tuttavia, per i tipi di compiti in cui gli LLM sono bravi, ci sono molte ragioni per cui questo processo di addestramento in due fasi funziona bene.
</p>

<p align="justify">
Il primo motivo riguarda l'ampiezza delle conoscenze necessarie per raggiungere obiettivi specifici. Ripensiamo al compito di un chatbot che vende un'auto. Se vogliamo costruire un modello che venda auto con successo, sarebbe fantastico costruire un set di dati composto solo da dati rilevanti per l'auto. Ma quando il potenziale acquirente vuole sapere se l'auto può contenere tutta l'attrezzatura necessaria per un giocatore di hockey, quanto sarà facile da pulire, se sarà possibile per il nonno artritico salire e scendere dai sedili del passeggero, o qualsiasi altra possibile domanda che qualcuno potrebbe avere su come la sua auto interagisce con la sua vita, ci si trova di fronte al problema di enumerare tutte le possibili domande che si potrebbero ricevere sulle auto. Non è possibile ottenere tutte le informazioni necessarie per generare risposte per ogni possibile situazione. Invece, ci affidiamo ai processi di formazione di cui abbiamo parlato finora, che possono essere considerati pre-formazione, per acquisire informazioni da un'ampia raccolta di contenuti con testi su sport, artrite, ecc. Ci auguriamo che queste informazioni aiutino il modello a essere meglio preparato o genericamente utile per rispondere a domande più ampie.
</p>

<p align="justify">
Questo è il secondo e principale motivo per cui utilizziamo un processo di addestramento in due fasi: ottenere centinaia di milioni di documenti che descrivono un problema specifico da utilizzare come parte della fase di pre-addestramento sarebbe impossibile. Allo stato attuale delle conoscenze, questa scala massiccia è necessaria per creare le straordinarie capacità osservate in GPT. Tuttavia, con uno sforzo relativamente minimo, è possibile pre-addestrare centinaia di milioni di informazioni generali, come pagine web, per impartire ai modelli conoscenze generali. Successivamente, è spesso sufficiente perfezionare il modello con solo centinaia di documenti per vincolarlo a produrre qualcosa di utilmente adattato al compito da svolgere. Ottenere poche centinaia di documenti per un problema specifico può essere impegnativo, ma realizzabile.
</p>

<p align="justify">
Ad alto livello, una seconda fase di addestramento di fine-tuning può aiutare a limitare un LLM a un sottoinsieme di comportamenti utili, poiché il modello originale non è incentivato a fare ciò che desideriamo. Nelle sezioni seguenti, presenteremo esempi concreti dei diversi problemi che emergono con i modelli di base, che renderanno evidenti le ragioni per cui questo funziona.
</p>

<h3>5.1.1 I modelli base non sono molto utilizzabili</h3>

<p align="justify">
L'addestramento di un LLM seguendo il processo descritto nel capitolo 4 produce un modello, solitamente definito modello base , perché può fungere da piattaforma di base per la creazione di applicazioni o modelli perfezionati. Sfortunatamente, i modelli base non sono molto utili alla maggior parte delle persone perché non espongono le conoscenze di base tramite un'interfaccia utente intuitiva, possono essere difficili da mantenere in tema e a volte producono contenuti poco convincenti. I modelli base non sono nemmeno addestrati con il concetto di chatbot come ChatGPT.
</p>

<h3>5.1.2 Non tutti gli output del modello sono desiderabili</h3>

<p align="justify">
A volte, ciò che un modello ritiene probabile che accada in un documento non è auspicabile. Le ragioni sono diverse, tra cui:
</p>

<ul>
  <li>
    <p align="justify">
Memorizzazione — A volte, gli LLM possono generare copie lunghe ed esatte di sequenze presenti nei loro dati di training, un processo spesso definito memorizzazione , che si riferisce all'idea che il testo venga riprodotto a memoria dal set di training. La memorizzazione può essere utile, ad esempio per memorizzare le risposte a specifiche domande fattuali. Ad esempio, se qualcuno chiede: "Quando è nato Abraham Lincoln?", si desidera che il modello ripeta "12 febbraio 1809". Tuttavia, può anche essere sostanzialmente dannoso se porta un modello a violare il copyright. Se qualcuno chiede "Una copia di Inside Deep Learning di Edward Raff" e il modello ne produce una copia letterale, Edward potrebbe arrabbiarsi con voi per violazione del copyright!      
    </p>
  </li>
  <li>
    <p align="justify">
Cose negative sul web — Non tutto ciò che si trova su internet è qualcosa a cui si vorrebbe esporre un utente. Ci sono molti contenuti vili e incitanti all'odio su internet, così come informazioni fattualmente errate che vanno da idee sbagliate comuni a teorie del complotto. Sebbene gli sviluppatori di modelli cerchino spesso di filtrare questi dati prima di addestrare il modello, ciò non è sempre possibile.    
    </p>
  </li>
  <li>
    <p align="justify">
Informazioni mancanti e nuove — Sfortunatamente, il mondo continua a evolversi e a diventare più complesso dopo aver addestrato i nostri modelli. Quindi, un modello addestrato su informazioni fino al 2018 non saprà nulla di ciò che è accaduto dopo, come il COVID-19 o l'invenzione da incubo della necrobotica [1]. Ma potresti voler che il tuo modello sia a conoscenza di questi sviluppi per rimanere utile, senza dover pagare un costo considerevole per riaddestrare il modello di base da zero. 
    </p>
  </li>
</ul>

<table>
  <td>
    <h3>Aspettando che il sistema legale si adegui</h3>
    <p align="justify">
Non siamo i vostri avvocati; questo non è un libro di diritto! I problemi legali relativi agli LLM sono complessi e ci sono molte sfumature riguardo al fair use e alla violazione. I motori di ricerca possono mostrarvi il contenuto delle loro fonti alla lettera, ma perché? Una combinazione di leggi che affrontano esplicitamente queste problematiche, come il Digital Millennium Copyright Act (DMCA), e precedenti stabiliti da sentenze giudiziarie, come Field contro Google, Inc. (412 F.Supp. 2d 1106 [D. Nev. 2006]), stabilisce nel tempo gli usi accettabili e non accettabili. Tuttavia, la legislazione e i casi giudiziari richiedono tempo per essere elaborati e la rivoluzione dell'IA generativa non si adatta perfettamente all'attuale concezione giuridica.
    </p>
    <p align="justify">
Forse vorreste una risposta chiara e precisa su cosa è e cosa non è proibito dalla legge negli Stati Uniti o nel vostro Paese, e la risposta più probabile è che tale certezza non esiste ancora per gli LLM. Inoltre, non saremmo mai stati beccati a dare simili consigli legali sulla carta stampata: non interpretiamo nemmeno gli avvocati in TV!
    </p>
  </td>
</table>

<p align="justify">
GPT-3.5 e 4 sono stati migliorati per evitare di rispondere a domande che non conoscono (non sempre con successo), ma possiamo guardare ad alcuni modelli di base open source come GPT-Neo per vedere cosa succede senza contromisure proattive. Ad esempio, se inventiamo il nuovo farmaco falso, MELTON-24, e chiediamo "Cos'è MELTON-24 e può aiutarmi a dormire meglio?", otteniamo la risposta inutile: "La melatonina causa numerosi problemi del sonno, tra cui insonnia e affaticamento. Questa causa insonnia, ed è per questo che è importante evitare determinati alimenti che possono sopprimere la melatonina".
</p>

<p align="justify">
In questo caso, la somiglianza di MELTON con la melatonina e il richiamo al "sonno" sono stati sufficienti per far sì che il modello cogliesse il tema della melatonina. Tuttavia, la risposta è ovviamente assurda, poiché MELTON-24 non esiste. Idealmente, vorremmo che il modello riconoscesse e rispondesse, riconoscendo la sua mancanza di informazioni piuttosto che produrre altro testo come ha fatto in questo caso.
</p>

<h3>5.1.3 Alcuni casi richiedono una formattazione specifica</h3>

<p align="justify">
Se un utente richiede dati in un formato specifico, come un formato di testo strutturato come JSON (per un esempio di un formato comune per lo scambio di dati tra computer, vedere https://en.wikipedia.org/wiki/JSON ), e non si fa corrispondere ogni parentesi aperta o chiusa o non si codificano correttamente i caratteri speciali, l'output non soddisferà i suoi obiettivi. Non importa quanto sofisticato o quasi corretto possa essere stato l'output; i requisiti di formattazione sono quasi sempre requisiti rigorosi. Abbiamo presentato un esempio di questo tipo di problema nel capitolo 4, quando abbiamo chiesto a ChatGPT di scrivere codice in Modula-3, e ha preso in prestito una sintassi Python non valida per Modula-3. Il codice non verrà compilato se viola le regole di sintassi. L'approccio probabilistico di un LLM alla generazione di testo per output specifici desiderati non garantirà il rispetto di tutte le regole di sintassi desiderate nel 100% dei casi.
</p>

<h3>5.2 Fine-tuning: il metodo principale per cambiare il comportamento</h3>

<p align="justify">
Ora che comprendiamo le diverse ragioni per cui vogliamo limitare e controllare il comportamento di un LLM, siamo più preparati a introdurre nuove informazioni nel modello per affrontare il problema che stiamo cercando di risolvere, evitando al contempo di produrre contenuti dannosi o legalmente discutibili. Ricordiamo che, sebbene esistano quattro diversi ambiti in cui possiamo intervenire per modificare il comportamento, la messa a punto è molto più efficace delle altre. Sia le opzioni closed source come OpenAI [2] che gli strumenti open source come Hugging Face [3], tra molti altri, offrono diverse opzioni per la messa a punto, rendendolo il metodo più accessibile per i professionisti.
</p>

<p align="justify">
Qualsiasi metodo di fine-tuning avrà lo stesso effetto: produrre una nuova variante di un LLM con parametri aggiornati che ne controllano il comportamento. Di conseguenza, è possibile combinare e abbinare diverse strategie di fine-tuning perché l'effetto fondamentale che producono è lo stesso: un nuovo set di parametri che può essere utilizzato così com'è o modificato ulteriormente. Il modello base di una persona potrebbe essere il modello perfezionato di un'altra persona. Questo accade con molti LLM open source in cui un modello iniziale (ad esempio, Llama) viene modificato da un'altra parte (ad esempio, si possono trovare molti modelli "Instruct Llama"), che è possibile poi ulteriormente perfezionare in base ai dati o a un caso d'uso specifico.
</p>

<p align="justify">
Il modo più semplice per personalizzare un LLM è quello di suggerire e perfezionare iterativamente i suggerimenti fino a ottenere il comportamento desiderato. Tuttavia, la messa a punto è il passo logico successivo se questa non funziona. Questa fase comporta un moderato aumento di impegno e costi, come la raccolta dei dati per la messa a punto e l'acquisizione dell'hardware per l'esecuzione di una sessione di messa a punto.
</p>

<p align="justify">
Due metodi di fine-tuning che dovresti conoscere in particolare sono il fine-tuning supervisionato (SFT) e il più intimidatorio apprendimento per rinforzo tramite feedback umano (RLHF). L'SFT è l'approccio più semplice ed è eccellente per incorporare nuove conoscenze in un modello o semplicemente per potenziarlo nel tuo ambito applicativo preferito. L'RLHF è più complesso, ma fornisce una strategia per far sì che un LLM persegua obiettivi più difficili e astratti come "essere un buon chatbot".
</p>

<h3>5.2.1 Fine-tuning supervisionato</h3>

<p align="justify">
Il modo più comune per influenzare l'output di un modello è l'SFT. L'SFT consiste nell'utilizzare contenuti di esempio di alta qualità, in genere scritti da persone, che catturano informazioni essenziali per il compito, ma che non sono necessariamente ben riflesse nel modello di base.
</p>

<p align="justify">
Ciò accade spesso perché gli LLM sono formati su una grande quantità di contenuti generalmente disponibili, che potrebbero avere una sovrapposizione minima con le vostre esigenze specifiche. Se gestite un ospedale, gli LLM hanno visionato pochissime cartelle cliniche. Se gestite uno studio legale, probabilmente non hanno visionato molte trascrizioni di deposizioni. Se gestite un'officina di riparazioni, probabilmente non hanno visionato tutti i manuali a cui potreste avere accesso.
</p>

<p align="justify">
Attenzione : la messa a punto è un modo utile per aggiungere nuove informazioni al modello, ma può anche avere implicazioni per la sicurezza. Se si desidera creare un LLM basato su cartelle cliniche, è opportuno effettuare la messa a punto su cartelle cliniche di esempio. Tuttavia, esiste il rischio che qualcuno possa indurre il modello a riprodurre informazioni sensibili contenute in tali dati di messa a punto, perché fondamentalmente, gli LLM tentano di completare l'input in base ai dati di training che hanno visualizzato. In conclusione: non addestrare o mettere a punto gli LLM su dati che si desidera mantenere privati.
</p>

<p align="justify">
Consideriamo di nuovo il nostro esempio dell'azienda automobilistica e del suo chatbot di vendita. Un modello base proveniente da una fonte terza potrebbe generalmente essere a conoscenza delle automobili, ma probabilmente non conoscerà tutto sui prodotti dell'azienda. Affinando un modello su manuali interni, cronologie delle chat, email, materiali di marketing e altri documenti interni, è possibile garantire che il modello sia preparato con quante più informazioni possibili sulle auto. Si potrebbero anche scrivere documenti di esempio sui pregi dei veicoli rispetto alla concorrenza, sui vantaggi, sugli script e altro ancora per garantire che l'LLM contenga le informazioni desiderate.
</p>

<p align="justify">
Il meccanismo di SFT è facile da spiegare. Come abbiamo accennato, SFT necessita semplicemente di più documenti. Possono essere in qualsiasi formato da cui sia possibile estrarre testo. Questo costituisce tutto il lavoro necessario per applicare SFT, perché SFT non fa altro che ripetere lo stesso processo di addestramento appreso nel capitolo 4. La Figura 5.3 mostra che il processo per SFT è lo stesso visto in precedenza. La differenza è che i parametri iniziali sono casuali e inutili la prima volta che si addestra il modello base. La seconda volta che si esegue la messa a punto, si inizia con i parametri del modello base che codificano ciò che il modello base ha appreso osservando i suoi dati di addestramento.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.3 Il fine-tuning supervisionato (SFT) è un approccio semplice per migliorare i risultati del modello. Si ripete lo stesso processo utilizzato per costruire il modello di base. Una volta che il modello di base è stato addestrato su una grande quantità di dati generali, si continua l'addestramento su una raccolta di dati specializzati più piccola.
      </p>
    </figcaption>
    
<img width="1100" height="576" alt="CH05_F03_Boozallen" src="https://github.com/user-attachments/assets/4ae02193-c728-474a-9fb2-1fac7ad98ffa" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Fortunatamente, ora hai una buona comprensione di SFT. Come il processo di training originale, riutilizza il task "prevedere il token successivo" per garantire che il tuo modello contenga informazioni dai nuovi documenti creati al suo interno. Come diretta conseguenza della previsione del token successivo, SFT non ci consente di modificare gli incentivi dell'LLM. Per questo motivo, obiettivi astratti come "non insultare l'utente" sono difficili da raggiungere con SFT.

<p align="justify">
Ottimizzazione delle insidie
Riutilizzando la strategia di discesa del gradiente del capitolo 4, tutti i metodi di fine-tuning tendono a ereditare due problemi relativi alla capacità di un LLM di restituire il contenuto su cui è stato addestrato. Poiché la SFT è così semplice, questo è il momento giusto per esaminare i problemi più ampi della fine-tuning, che vanno oltre la SFT.

<p align="justify">
Non vi è alcuna garanzia che SFT conservi correttamente le informazioni fornite. Questo problema, noto come dimenticanza catastrofica [4], si verifica quando si addestra il modello su nuovi dati ma non si continua l'addestramento su dati più vecchi, e il modello inizia a "dimenticare" quelle informazioni più vecchie. Non è facile determinare cosa verrà dimenticato e cosa no. La dimenticanza catastrofica è un problema riconosciuto dal 1989 [5]. In altre parole, la messa a punto fine non è puramente additiva; si rinuncia a qualcosa per essa.

<h3>5.2.2 Apprendimento per rinforzo dal feedback umano</h3>

<p align="justify">
Al momento della stesura di questo articolo, RLHF è il paradigma dominante per i modelli vincolanti. Come suggerisce il nome, utilizza un approccio derivato dal campo dell'apprendimento per rinforzo (RL). RL è un'ampia famiglia di tecniche in cui un algoritmo deve prendere decisioni multiple per massimizzare un obiettivo a lungo termine, come mostrato nella figura 5.4 , dove quattro termini sono utilizzati con un significato tecnico:

<ul>
  <li>
    <p align="justify">
Agente : l'entità/IA/robot che desidera raggiungere un obiettivo generale e che potrebbe richiedere più azioni per raggiungerlo.
    </p>
  </li>
  <li>
    <p align="justify">
Azione : lo spazio di tutte le possibili azioni che l'agente può compiere o intraprendere per promuovere i propri obiettivi.
    </p>
  </li>
  <li>
    <p align="justify">
Ambiente — Il luogo/oggetto/spazio interessato da un'azione. L'ambiente può cambiare o meno a seguito dell'azione, delle azioni intraprese da altri agenti o del naturale e continuo cambiamento dell'ambiente.
    </p>
  </li>
  <li>
    <p align="justify">
Ricompensa : la quantificazione numerica del miglioramento (che può essere negativo) che può verificarsi o meno dopo un dato numero di azioni.
    </p>
  </li>
</ul>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
La Figura 5.4 RL riguarda le interazioni iterative, in cui la ricompensa per le azioni potrebbe non materializzarsi per molto tempo e richiedere più passaggi per essere raggiunta. Per un chatbot come ChatGPT, l'ambiente è la conversazione con un utente e le azioni sono gli infiniti possibili testi che ChatGPT può completare. La ricompensa diventa, in un certo senso, la soddisfazione dell'utente nei confronti del chatbot al termine della conversazione.
      </p>
    </figcaption>
    
<img width="1100" height="494" alt="CH05_F04_Boozallen" src="https://github.com/user-attachments/assets/ab73a65a-cdec-49d4-9b25-b0c92564918b" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Nell'esempio di un LLM utilizzato come chatbot per interagire con le persone, gli utenti sono l'ambiente. L'LLM stesso è l'agente e il testo che può produrre è l'azione. Questo lascia un ultimo aspetto da specificare: la ricompensa. Se dovessimo far sì che un utente ottenga un punteggio di +1 per una buona conversazione con un chatbot (ad esempio, niente linguaggio volgare, niente bugie, risposte utili) e un punteggio di -1 per una conversazione scadente (ad esempio, suggerisce di distruggere tutti gli umani), allora aggiungeremmo il feedback umano al nostro apprendimento per rinforzo.
</p>

<p align="justify">
Un lettore attento potrebbe notare che una ricompensa suona sospettosamente simile alla funzione di perdita discussa nel capitolo 4. In effetti, il nostro esempio di una conversazione positiva e negativa rientra in quel regime molto soggettivo e difficile da quantificare che abbiamo definito un cattivo esempio di funzione di perdita. La ricompensa +1/-1 non è uniforme perché il valore punta in una direzione o nell'altra, e non esiste una via di mezzo, un'altra caratteristica negativa per una funzione di perdita.
</p>

<p align="justify">
Uno degli aspetti più interessanti dell'RL è la sua capacità di lavorare con obiettivi non continui e difficili da quantificare. Utilizziamo il termine " ricompensa" invece di "perdita" per indicare la differenza tra queste due situazioni. Generalmente, i tipi di obiettivi che l'RL può apprendere sono definiti " non differenziabili" . Di conseguenza, questi obiettivi non possono essere appresi utilizzando le stesse tecniche matematiche come la discesa del gradiente, che abbiamo trattato descrivendo l'apprendimento delle reti neurali nel capitolo 4. Spiegheremo più avanti come funziona specificamente l'RLHF. L'avvertenza dell'RL è che può essere computazionalmente dispendiosa e richiedere una quantità significativa di dati. L'RL è notoriamente un metodo di apprendimento impegnativo. Spesso funziona peggio di altre tecniche di fine-tuning come la SFT perché l'RL richiede molti più esempi del modo "giusto" e "sbagliato" di fare le cose rispetto ad altri approcci, e poiché utilizziamo il feedback umano per guidare l'RLHF, i risultati non sono sempre perfetti. Ad esempio, nella figura 5.5 , RLHF non può aiutare un LLM a comprendere le istruzioni di base al di fuori di ciò che ha visto esplicitamente durante l'addestramento RLHF perché non aggiunge alcuna capacità di eseguire la logica di base, come la comprensione della richiesta dell'utente di evitare di visualizzare informazioni sui delfini, al modello sottostante.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.5 RLHF è piuttosto efficace nel far sì che gli LLM evitino problemi noti e specifici. Tuttavia, non fornisce al modello nuovi strumenti per gestire problemi nuovi. Il desiderio di parlare dei Miami Dolphins come la cosa logica da dire dopo aver chiesto del football a Miami viola la prima richiesta di evitare di menzionare i delfini.
      </p>
    </figcaption>
    
![CH05_F05_Boozallen](https://github.com/user-attachments/assets/9418690f-167e-48d1-a025-1780c15b7773)

  </figure>
</div>
  </td>
</table>

<p align="justify">
Gli LLM non eseguono il ragionamento nello stesso modo in cui noi umani concepiamo il ragionamento. Si può arrivare molto lontano raccogliendo centinaia di milioni di esempi di "tutto", ma il mondo è strano. Abbiamo poche prove che gli LLM possano produrre in modo affidabile risposte soddisfacenti quando si verifica qualcosa di nuovo. Tuttavia, RLHF è finora il metodo migliore per vincolare il comportamento di un LLM. Nonostante le sue sfide, RL presenta un modo di apprendimento non disponibile con metodi basati su gradienti che richiedono obiettivi differenziabili. Ancora più importante, ChatGPT ha dimostrato che RL può funzionare in molti casi. Quindi, approfondiamo il funzionamento di RLHF.
</p>

<h3>5.2.3 Messa a punto: il quadro generale</h3>

<p align="justify">
SFT e RLHF sono i due metodi principali per perfezionare un LLM. SFT può lavorare con migliaia di documenti o campioni, mentre RLHF spesso richiede decine di migliaia di esempi. Questo non dovrebbe impedirti di approfondire l'argomento se hai meno dati, ma in tal caso, potrebbe essere più proficuo impiegare il tuo tempo sviluppando prompt più efficaci.
</p>

<p align="justify">
Ancora più importante, SFT e RLHF non si escludono a vicenda. Entrambi modificano i parametri sottostanti del modello ed è possibile applicarli uno dopo l'altro per ottenere i vantaggi di ciascun approccio. Inoltre, non sono gli unici metodi di fine-tuning attualmente esistenti. Ad esempio, si stanno sviluppando nuovi metodi di fine-tuning che rimuovono concetti da un LLM per forzare un modello a ignorare i dati da cui ha appreso dopo essere stato addestrato [6]. Ulteriori tecniche per l'alterazione del modello saranno sviluppate nei prossimi anni. Tutte richiederanno probabilmente una raccolta di dati, ma richiederanno meno lavoro complessivo rispetto al tentativo di costruire autonomamente un LLM da zero.
</p>

<h3>5.3 La meccanica della RLHF</h3>

<p align="justify">
Per descrivere il funzionamento di RLHF, introdurremo una versione incompleta di RLHF, spiegheremo perché non funziona e poi spiegheremo come risolverlo. In questa sezione, non discuteremo la matematica dettagliata utilizzata da RLHF, poiché non fornirebbe approfondimenti particolarmente approfonditi su RLHF da un livello elevato. Se desiderate approfondire i dettagli, vi consigliamo di iniziare con "Implementazione di RLHF: imparare a riassumere con trlX" [7] dopo aver completato questo capitolo.
</p>

<h3>5.3.1 Iniziare con una RLHF ingenua</h3>

<p align="justify">
Innanzitutto, diamo un'occhiata alla versione incompleta e ingenua di RLHF. Abbiamo discusso di come RL possa apprendere con obiettivi non differenziabili. Supponiamo quindi di avere un essere umano che valuterà l'output di un LLM con una ricompensa di qualità , dove +1 indica una buona risposta e -1 una risposta inadeguata. Questa ricompensa di qualità è semplicemente un punteggio arbitrario che assegniamo all'output prodotto dall'LLM per indicare che un esempio è in qualche modo migliore degli altri.
</p>

<p align="justify">
Quindi, se un utente richiede a un LLM "Raccontami una barzelletta" e l'LLM produce una risposta del tipo "Quante anatre ci vogliono per avvitare una lampadina?", potremmo assegnare un punteggio di +1 per una barzelletta (ragionevolmente) buona. Se invece l'LLM produce una frase come "I cani sono cattivi", assegneremo un punteggio di -1 perché non sta nemmeno tentando di fare una barzelletta. Poiché la RL è difficile da realizzare utilizzando semplici ricompense di qualità di +1 e -1, aggiungeremo informazioni aggiuntive per l'algoritmo RL, come le probabilità di ciascun token generato. In questo modo, l'algoritmo RL sa quanto può essere probabile ogni token. L'intero processo è riassunto nella figura 5.6 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.6 Una versione ingenua e incompleta di RLHF. Le linee tratteggiate rappresentano il testo inviato da un componente all'altro. Poiché il testo è incompatibile con la discesa del gradiente, è necessario utilizzare un algoritmo RL più complesso. Questo ci consente di modificare i pesi dell'LLM in base a un punteggio di qualità per gli output dell'LLM.
      </p>
    </figcaption>
    
<img width="1100" height="266" alt="CH05_F06_Boozallen" src="https://github.com/user-attachments/assets/f7969a02-576a-46e0-aae4-1ed404650b86" />

  </figure>
</div>
  </td>
</table>

<table>
  <td>
    <h3>Perché fornire probabilità a RL?</h3>
    <p align="justify">
Può sembrare strano che stiamo fornendo all'algoritmo RL le probabilità di ogni token. Ci sono ragioni matematiche più profonde per cui questo è utile, che non approfondiremo in questo capitolo. Ma per una certa intuizione, una buona battuta spesso richiede depistaggio o sorpresa. Se tutte le probabilità di una sequenza sono valori elevati (vicini a 1,0), probabilmente non è una buona battuta perché è troppo prevedibile.
    </p>
    <p align="justify">
In generale, nell'ambito dell'elaborazione del linguaggio naturale, produrre un buon testo generato è un atto di equilibrio tra rendere qualcosa probabile (ovvero, probabile che accada) e non renderlo troppo probabile (ovvero, ripetitivo).
    </p>
  </td>
</table>

<h3>5.3.2 Il modello di ricompensa della qualità</h3>

<p align="justify">
Abbiamo descritto la ricompensa per la qualità come punteggi assegnati da esseri umani per ogni completamento di un prompt. Sebbene valutare manualmente i completamenti in tempo reale funzionerebbe tecnicamente, sarebbe irragionevole a causa del livello di impegno richiesto. Tuttavia, il feedback umano viene comunque incorporato tramite la ricompensa per la qualità. Invece, addestriamo una rete neurale come modello di ricompensa . Questo si ottiene chiedendo agli esseri umani di raccogliere manualmente centinaia di migliaia di coppie di prompt e completamento e di valutarle come buone o cattive. Questi punteggi diventano i dati etichettati utilizzati per addestrare il modello di ricompensa, come mostrato nella figura 5.7 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.7 Il modello di ricompensa viene addestrato come un algoritmo di classificazione supervisionato standard. Una rete neurale, che potrebbe essere un LLM o un'altra rete più semplice come una rete neurale convoluzionale o ricorrente, viene addestrata per prevedere come un essere umano valuterebbe una coppia di completamento rapido. Poiché le reti neurali sono differenziabili, questo addestramento funziona e fornisce uno strumento che rappresenta l'"essere umano" in RLHF.
      </p>
    </figcaption>
    
<img width="1100" height="451" alt="CH05_F07_Boozallen" src="https://github.com/user-attachments/assets/e97337c0-67bc-44c4-bb3f-582ede700df0" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Raccogliere centinaia di migliaia di prompt valutati e coppie di completamento è costoso ma fattibile (ad esempio, https://huggingface.co/datasets/Anthropic/hh-rlhf ), soprattutto quando si utilizzano strumenti di crowd-sourcing come Mechanical Turk ( https://www.mturk.com/ ). Si tratta di una grande quantità di dati da gestire manualmente, ma di ordini di grandezza inferiori ai miliardi di token utilizzati per creare i modelli di base iniziali. Questi set di dati RLHF devono essere di grandi dimensioni perché è necessario coprire molti scenari, domande e richieste che un utente potrebbe fornire. Come abbiamo già visto nella figura 5.5 con l'esempio del delfino, RLHF tende a funzionare per argomenti relativamente semplici e noti. Quindi l'ampiezza nella gestione di diverse situazioni deriva direttamente dall'ampiezza nei dati di fine-tuning.
</p>

<p align="justify">
Nota: abbiamo utilizzato +1/-1 come esempio di ricompensa di qualità perché è il più semplice da descrivere. Poiché la vita reale non necessita di gradienti, è possibile utilizzare qualsiasi punteggio pertinente al problema. Utilizzare un punteggio di classificazione, in cui si confrontano più completamenti per un determinato prompt e li si classifica dal migliore al peggiore, è più popolare ed efficace perché si valutano più completamenti contemporaneamente. In ogni caso, fornire feedback positivi e negativi rimane fondamentalmente lo stesso.
</p>

<h3>5.3.3 L'obiettivo RLHF simile ma diverso</h3>

<p align="justify">
Una volta addestrato un modello di ricompensa, è possibile creare e valutare tutti i prompt desiderati per il processo RLHF. Il feedback umano viene integrato nel modello di ricompensa e può ora essere distribuito, parallelizzato e riutilizzato. L'unico problema rimanente è che l'attuale versione ingenua di RLHF è incentivata esclusivamente a massimizzare la ricompensa di qualità, che non è l'unico obiettivo su cui RL deve concentrarsi.
</p>

<p align="justify">
Di conseguenza, il modello inizierà a degradarsi nel tempo, producendo output incomprensibili e senza senso, di scarsa qualità e privi di valore per qualsiasi lettore. Questo degrado è correlato a un fenomeno chiamato attacchi avversari , in cui è sorprendentemente facile ingannare una rete neurale inducendola a prendere decisioni assurde con modifiche relativamente minori all'input. L'apprendimento automatico avversario (AML) è in rapida evoluzione e ha una sua complessità, quindi lasceremo la discussione ad altri [8]. Ma l'implementazione ingenua di RLHF che descriviamo nella figura 5.6 esegue essenzialmente un attacco avversario contro un LLM perché si concentrerà solo sulla massimizzazione della ricompensa di qualità, non sull'essere utile per l'utente. In sostanza, questa è la legge di Goodhart che si verifica nell'IA/ML: "Quando una misura diventa un obiettivo, cessa di essere una buona misura".
</p>

<p align="justify">
Per affrontare questo problema, dobbiamo aggiungere un secondo obiettivo all'algoritmo RL. Calcoleremo una seconda ricompensa per la similarità tra l'output dell'LLM di base originale e l'output dell'LLM con la messa a punto. Concettualmente, questa ricompensa può essere considerata una ricompensa quando l'LLM con la messa a punto produce un output migliore, simile al comportamento dell'LLM originale. Impedisce al modello di deviare dai binari diventando troppo innovativo. Fondamentalmente, vogliamo che l'output generato dall'LLM con la messa a punto sia basato sui dati di addestramento inizialmente osservati dall'LLM originale. Non vogliamo che il modello con la messa a punto diventi così creativo da generare risultati non-senso. Questa ricompensa viene aggiunta all'algoritmo RL per stabilizzare la messa a punto. La Figura 5.8 fornisce il quadro completo del funzionamento di RLHF.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.8 La versione completa di RLHF. Le linee tratteggiate sono testo e richiedono a RL di aggiornare i parametri. L'LLM originale è il modello base senza alcuna modifica, mentre l'LLM da perfezionare parte come modello base, ma viene modificato per migliorare la qualità dei suoi output. Le componenti di ricompensa per similarità e qualità sono fornite con probabilità di parola per migliorare il calcolo. RL regola i parametri combinando i punteggi di qualità e similarità
      </p>
    </figcaption>
    
<img width="1100" height="501" alt="CH05_F08_Boozallen" src="https://github.com/user-attachments/assets/ef283f21-8256-4b7c-b2f3-5598d4b8536a" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Un modello che impara a produrre output incomprensibili riceverebbe una penalità elevata per mancanza di similarità, scoraggiando il modello dal diventare troppo diverso. Un modello che produce esattamente gli stessi output riceverebbe un punteggio di qualità basso, scoraggiando la mancanza di cambiamento. L'equilibrio di entrambi i fattori contribuisce in modo eccellente a ottenere un effetto Riccioli d'oro che consente al modello una flessibilità sufficiente per cambiare senza perdere il suo output simile a quello umano.
</p>

<h3>5.4 Altri fattori nella personalizzazione del comportamento LLM</h3>

<p align="justify">
Il fine-tuning è il metodo dominante per alterare il comportamento di un LLM, ma non è infallibile e non è l'unico ambito in cui possono verificarsi cambiamenti comportamentali. Il nostro focus sul fine-tuning si basa sul valore dell'RLHF nel produrre comportamenti LLM che vanno oltre la semplice previsione del token successivo.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.9 Oltre alla messa a punto, è possibile modificare il comportamento del modello modificando i dati di addestramento, modificando il processo di addestramento del modello di base o modificando gli output del modello scrivendo codice per gestire situazioni specifiche
      </p>
    </figcaption>
    
<img width="1100" height="432" alt="CH05_F09_Boozallen" src="https://github.com/user-attachments/assets/a6f4d784-e68d-442b-8511-2e688d7cde93" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Le altre tre fasi in cui è possibile modificare il comportamento dell'LLM, descritte nella figura 5.9 , non sono facilmente accessibili all'utente. Tuttavia, ora esamineremo brevemente le altre fasi, insieme ad alcuni dettagli chiave che è necessario conoscere per completezza. Questi fattori possono aiutarvi a comprendere quali siano le difficoltà da raggiungere con la messa a punto e la portata delle domande che potreste voler approfondire presso il vostro fornitore di LLM.
</p>

<h3>5.4.1 Modifica dei dati di allenamento</h3>

<p align="justify">
Il detto "garbage in, garbage out" è un classico in tutti gli ambiti del ML. Si può notare che OpenAI [9] e Google [10] forniscono molti dettagli tecnici di basso livello su come sviluppano i loro LLM, ma molti meno dettagli sui dati utilizzati per la loro costruzione. Questo perché la maggior parte del "trucco segreto" nella costruzione di LLM efficaci riguarda la data curation, ovvero lo sviluppo di una raccolta di dati che rappresenti attività diverse, un uso linguistico di alta qualità e una gamma di situazioni diverse. La dimensione e la qualità dei set di dati utilizzati per addestrare, convalidare e testare gli LLM sono importanti.
</p>

<p align="justify">
La dimensione e la qualità dei dati sono diventate particolarmente rilevanti man mano che i contenuti generati dagli LLM vengono utilizzati regolarmente e tornano online. Ad esempio, si stima che dal 6% al 16% delle revisioni paritarie accademiche utilizzino gli LLM [11], ed è altamente probabile che molti servizi di editing utilizzeranno presto queste nuove tecnologie. Questo aumento dell'uso crea potenzialmente un circolo vizioso negativo. Con l'aumentare della quantità di dati generati dagli LLM, ci saranno proporzionalmente meno contenuti non LLM disponibili per la formazione degli LLM. Ciò si tradurrà in una diminuzione complessiva della diversità linguistica disponibile e, quindi, della novità che gli LLM saranno in grado di acquisire. A sua volta, la qualità di un LLM formato su dati più recenti si riduce [12]. Questo problema sarà probabilmente significativo nel mantenere gli LLM aggiornati, poiché la cura di un set di dati di alta qualità non sarà più semplice come prima.
</p>

<p align="justify">
C'è anche il problema che gli LLM possono riflettere solo le informazioni disponibili durante la formazione e hanno una probabilità sproporzionatamente maggiore di riflettere informazioni più diffuse durante la formazione. Se si desidera un LLM che non contenga parolacce o linguaggio razzista, è necessario impegnarsi a ripulire il proprio dataset da qualsiasi parolaccia o linguaggio razzista.
</p>

<p align="justify">
Tuttavia, questo problema è potenzialmente un'arma a doppio taglio. Se vogliamo che il nostro LLM sappia riconoscere e respingere in modo appropriato il linguaggio razzista o volgare, deve sapere cosa sono il razzismo e il volgare. Si può immaginare di usare il prompting su un LLM che non ha mai visto alcun testo razzista per "insegnargli" a usare parole razziste in un contesto che, senza sapere Xse è razzista, appare innocuo. Ma nella forma finale, noi, come lettori consapevoli del razzismo, riconosceremmo la frase come discutibile. Questo problema, al momento, non ha risposta, ma è qualcosa di cui essere consapevoli.
</p>

<p align="justify">
Anche la modifica dei dati è importante, poiché rappresenta l'unica possibilità di influenzare il modo in cui la tokenizzazione viene eseguita in un LLM. Come discusso nel capitolo 2, diversi approcci alla tokenizzazione presentano dei compromessi, ma le scelte effettuate vengono integrate per sempre nel modello una volta iniziato l'addestramento.
</p>

<h3>5.4.2 Modifica dell'addestramento del modello di base</h3>

<p align="justify">
La privacy dei dati di training deve essere una preoccupazione significativa durante l'addestramento o la messa a punto di LLM. In genere, è possibile ricostruire i dati di training di un modello elaborando gli input in un modo specifico. In alcuni casi, è stato dimostrato che gli LLM generano esattamente i passaggi su cui sono stati addestrati. Ciò è problematico se i dati di training contengono informazioni private, come informazioni di identificazione personale (PII), informazioni sanitarie private (PHI) o altre categorie di dati sensibili. Un utente di un modello potrebbe, forse inconsapevolmente, fornire un prompt che rivela questi dati alla lettera.
</p>

<p align="justify">
L'addestramento iniziale di un algoritmo è il momento ideale per mitigare alcune di queste preoccupazioni sulla privacy utilizzando una tecnica nota come privacy differenziale (DP). La DP è complessa, quindi se desiderate approfondire l'argomento, vi consigliamo il libro Programming Differential Privacy [13]. In breve, la DP aggiunge una quantità accuratamente costruita di rumore casuale per fornire garanzie dimostrabili sulla privacy dei dati nel processo di addestramento del modello. La DP non gestisce tutto, ma fornisce una protezione molto maggiore di quella disponibile con la maggior parte degli algoritmi odierni.
</p>

<p align="justify">
Allora perché non l'hanno fatto tutti? Beh, aggiungere rumore tende naturalmente a ridurre la qualità del risultato. Grandi sessioni di training sono costose, costano da centinaia di migliaia a milioni di dollari ciascuna. Se dovessi fare 10 volte più sessioni di training per impostare correttamente i parametri di privacy, avresti un problema da un milione a decine di milioni di dollari. Ma con il miglioramento della DP ogni anno, sospettiamo che diventerà più diffuso nel tempo.
</p>

<h3>5.4.3 Modifica delle uscite</h3>

<p align="justify">
Infine, possiamo esaminare i token prodotti e scrivere codice per modificarne il comportamento in base alle combinazioni di token generate dal modello. Dopo la messa a punto, questa è la seconda fase più probabile che un consumatore di LLM utilizzerà per modificare il proprio comportamento.
</p>

<p align="justify">
In precedenza in questo capitolo, abbiamo discusso dell'esigenza comune degli LLM di generare output che aderiscano a un formato preciso, come XML o JSON. Implementare requisiti di formattazione come questi è un problema comune con gli LLM. Ogni singola previsione fallita si traduce in un errore nella generazione di output valido. Un esempio di questo tipo di errore è visibile nella figura 5.10 , dove chiediamo all'LLM di completare del codice Python; il token successivo dovrebbe essere un punto e virgola (;), ma tenta erroneamente di inserire un carattere di nuova riga (\n).
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.10 Scrivendo codice che imponga una specifica di formato, è possibile rilevare l'output non valido da un LLM durante la sua generazione. Una volta rilevato, un modo semplice per migliorare la situazione è far sì che l'LLM produca il token successivo più probabile finché non viene trovato un output valido.
      </p>
    </figcaption>
    
<img width="1100" height="443" alt="CH05_F10_Boozallen" src="https://github.com/user-attachments/assets/df10dd87-3813-46f5-a9a9-5491b02098d8" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Esistono vari strumenti (ad esempio, https://github.com/noamgat/lm-format-enforcer ) per specificare formati rigorosi come parte della fase di decodifica dell'LLM. Se questi strumenti rilevano un errore di analisi, rigenerano immediatamente l'ultimo token fino a produrre un output valido.
</p>

<p align="justify">
Sono possibili approcci più sofisticati per la selezione del token successivo. Tuttavia, la lezione importante da trarre è la capacità di utilizzare gli output intermedi per prendere decisioni prima di generare l'output completo. Anche le semplici liste "go/no-go" della vecchia scuola sono strumenti preziosi per individuare comportamenti scorretti. Non è necessario passare un output all'utente in tempo reale; è sempre possibile introdurre un ritardo artificiale in modo da poter visualizzare una parte più ampia della risposta prima di inviarla all'utente. Questo dà il tempo di intervenire sui filtri per linguaggio scorretto o su altri controlli hard-coded. Se si verifica una corrispondenza, proprio come nella figura 5.10 , è possibile rigenerare un output o interrompere la sessione dell'utente.
</p>

<h3>5.5 Integrazione degli LLM in flussi di lavoro più ampi</h3>

<p align="justify">
A questo punto del capitolo, abbiamo trattato alcuni approcci di base per manipolare un LLM al fine di produrre output più desiderabili e coerenti. Finora, ci siamo concentrati su tecniche che coinvolgono l'LLM stesso, sia attraverso prompt, manipolazione dei dati di training o messa a punto di un modello di base. In questa sezione, esploreremo come personalizzare l'output prodotto da un LLM integrando gli input e gli output degli LLM in catene di operazioni multifase per ottenere risultati più personalizzati. Questo ambito è in rapida evoluzione, quindi tratteremo brevemente un esempio concreto di integrazione di un LLM in un flusso di lavoro di recupero delle informazioni più ampio e poi discuteremo di uno strumento generico per mostrarvi come personalizzare gli output dell'LLM utilizzando più interazioni con un LLM.
</p>

<h3>5.5.1 Personalizzazione di LLM con generazione aumentata del recupero</h3>

<p align="justify">
La generazione aumentata del recupero (RAG) è una tecnica che consente di produrre risposte da un LLM riducendo al contempo la probabilità di generare spiegazioni insensate o comunque errate. La componente "recupero" del nome RAG dovrebbe fornire un utile suggerimento sul funzionamento della tecnica. Quando un utente fornisce input a un sistema RAG, questo utilizza un LLM per creare una query che viene eseguita su un motore di ricerca contenente un indice di documenti. A seconda del caso d'uso, potrebbe trattarsi di un indice di informazioni generali, come Google, o di un indice specifico per argomento, come una raccolta di materiali di marketing automobilistico. In risposta alla query, il motore di ricerca genera un elenco di documenti pertinenti. Il sistema RAG utilizza quindi l'LLM per estrarre informazioni da tali documenti e generare risposte migliori. A tal fine, il sistema RAG combina il contenuto dei documenti recuperati con la query originale dell'utente per creare un prompt completo per l'LLM che si tradurrà in una risposta migliore. Questo metodo tende a funzionare bene perché, invece di chiedere a un LLM di generare una risposta basata sui suoi dati di training o di fine-tuning, ora gli chiediamo di generare una risposta all'input riassumendo un insieme di documenti rilevanti per una normale query su un motore di ricerca e fornendo quell'insieme di documenti rilevanti da cui trarre le sue risposte all'LLM. In altre parole, stiamo aiutando l'LLM a concentrarsi sui dati di cui ha bisogno per rispondere correttamente a una determinata domanda. Descriviamo questo processo nella figura 5.11 e lo confrontiamo con i normali casi d'uso dell'LLM descritti finora.
</p>

<p align="justify">
I due vantaggi più significativi dell'approccio RAG finora sono i seguenti:

<ul>
  <li>
    <p align="justify">
L'output di un sistema RAG è più accurato, fattualmente corretto o comunque utile per la domanda originale dell'utente perché si basa su fonti specifiche contenute in un indice di documenti.
    </p>
  </li>
  <li>
    <p align="justify">
L'LLM può generare citazioni o riferimenti ai documenti di origine utilizzati per produrre le sue risposte, consentendo agli utenti di convalidare o correlare il materiale di origine con il materiale di origine originale.
    </p>
  </li>
</ul>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 5.11 A sinistra, mostriamo il normale utilizzo di un LLM da parte di un utente che chiede come scrivere in formato JSON. Gli LLM hanno naturalmente la possibilità di produrre output errati, che vogliamo ridurre al minimo. A destra, mostriamo l'approccio RAG. Utilizzando un motore di ricerca, possiamo trovare documenti pertinenti a una query e combinarli in un nuovo prompt, fornendo all'LLM maggiori informazioni e contesto per produrre una risposta migliore.
      </p>
    </figcaption>
    
<img width="1100" height="771" alt="CH05_F11_Boozallen" src="https://github.com/user-attachments/assets/029659dc-34be-4f71-a47e-a72c9eaf4d3d" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Quest'ultimo punto, relativo alle citazioni, è particolarmente importante. Il RAG non risolverà tutti i problemi degli LLM, poiché l'LLM genera comunque l'output finale in un sistema RAG. L'LLM potrebbe comunque generare errori o allucinazioni dovuti a contenuti che non riesce a trovare o che non esistono. È anche possibile che l'LLM non catturi o rappresenti accuratamente il contenuto di nessuno dei documenti sorgente che utilizza. Di conseguenza, l'utilità dell'approccio RAG è direttamente correlata alla qualità della ricerca che esegue e ai documenti restituiti. In conclusione, se non si riesce a creare un motore di ricerca efficace per il proprio problema, non si può costruire un modello RAG efficace.
</p>

<table>
  <td>
    <h3>Dimensione del contesto</h3>
    <p align="justify">
Quando si pensa agli LLM, è importante considerare un aspetto noto come dimensione del contesto . La dimensione del contesto dell'LLM determina quanti token può gestire computazionalmente in una singola richiesta di completamento. Si può pensare a questa dimensione come alla quantità di dati che un LLM è in grado di esaminare quando riceve input sotto forma di prompt. Ad esempio, GPT-3 ha una dimensione del contesto di 2.048 token. Tuttavia, nei chatbot, ad esempio, il contesto viene spesso utilizzato per contenere una trascrizione continua dell'intera conversazione, inclusi eventuali output dell'LLM. Se si ha una conversazione con GPT-3 che supera i 2.048 token, si scoprirà che GPT-3 spesso perde traccia di alcuni degli argomenti discussi all'inizio della chat.
    </p>
  <p align="justify">
La dimensione del contesto è un fattore abilitante e limitante per l'utilizzo di RAG. Se un sistema RAG recupera un intero libro da elaborare tramite il tuo LLM, quest'ultimo richiederà una dimensione del contesto enorme per poterlo utilizzare. In caso contrario, il LLM può consumare solo la prima parte di un documento recuperato (fino alla dimensione del contesto del LLM) e potrebbe perdere informazioni. Di conseguenza, la dimensione del contesto è un'importante caratteristica operativa da considerare nella scelta di un modello. Alcuni modelli attuali, come Grok di X, possono gestire fino a 128.000 token come dimensione del contesto. Sebbene grandi dimensioni del contesto come quelle di Grok aumentino il limite massimo di ciò che un LLM può consumare, l'efficacia dei LLM nella gestione di grandi quantità di input, rese possibili da dimensioni del contesto più ampie, è ancora un'area di studio attiva.
  </p>  
  </td>
</table>

<p align="justify">
Nella figura 5.11 potreste notare che dobbiamo creare un nuovo prompt. Abbiamo aggiunto il prefisso "Rispondi alla domanda:" seguito dal suffisso "Utilizzando le seguenti informazioni:". Ipoteticamente, potreste ottenere risultati migliori modificando questo prompt. Potreste pensare di aggiungere istruzioni come "Ignora le seguenti informazioni se non sono pertinenti alla domanda originale". Queste idee stanno iniziando a entrare nel campo dell'ingegneria dei prompt, la pratica di modificare e adattare il testo in un LLM per modificarne il comportamento, come abbiamo già detto nel capitolo 4.
</p>

<p align="justify">
Il prompt engineering è davvero utile e rappresenta un buon modo per combinare più chiamate a un LLM per migliorare i risultati. Ad esempio, potresti provare a migliorare i risultati di ricerca chiedendo all'LLM di riscrivere la domanda. (Questa discussione tocca un'area classica del recupero delle informazioni chiamata espansione delle query , se desideri approfondire l'argomento). Tuttavia, il prompt engineering può essere molto fragile: qualsiasi aggiornamento a un LLM potrebbe modificare il funzionamento dei prompt, e sarebbe una seccatura dover riscrivere ogni prompt, soprattutto quando si affronta qualcosa di più complesso, come un modello RAG o qualcosa di ancora più sofisticato.
</p>

<h3>5.5.2 Programmazione LLM di uso generale</h3>

<p align="justify">
Sebbene siano ancora una novità, stiamo già iniziando a vedere librerie di programmazione e altri strumenti software creati utilizzando gli LLM come componenti di applicazioni personalizzate. Uno che apprezziamo particolarmente è DSPy ( https://dspy.ai ), che può semplificare la creazione e la manutenzione di programmi che tentano di modificare gli input e gli output di un LLM. Una buona libreria software nasconderà i dettagli che ostacolano la produttività, e DSPy svolge un buon lavoro nell'astrarre le seguenti attività relative all'utilizzo degli LLM:
</p>

<ul>
  <li>
  <p align="justify">
Integrazione dello specifico LLM utilizzato
  </p>
  </li>
  <li>
  <p align="justify">
Implementazione di modelli comuni di sollecitazione
  </p>
  </li>
  <li>
  <p align="justify">
Adattare i prompt alla combinazione desiderata di dati, attività e LLM.
  </p>
  </li>
</ul>

<p align="justify">
Questo non è un libro di programmazione, quindi un tutorial completo su DSPy esula dallo scopo. Tuttavia, è utile esaminare i modi in cui DSPy può essere utilizzato per implementare il modello RAG descritto nella sezione 5.5.1 . Richiederà di scegliere un LLM da utilizzare (GPT-3.5, in questo caso), nonché un database di informazioni (Wikipedia funzionerà bene) e di definire l'algoritmo RAG. DSPy funziona definendo un LLM e un database predefiniti utilizzati da tutti i componenti (a meno che non si intervenga), semplificando la separazione e la sostituzione delle parti utilizzate. Questo processo è illustrato nel seguente elenco.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    
<img width="497" height="536" alt="image" src="https://github.com/user-attachments/assets/8b061ca9-d03b-4b4f-8fb0-25072106f11e" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Questo codice imposta le scelte sopra menzionate nei LLM e nei database come predefinite, rendendo altrettanto semplice sostituire OpenAI con un altro LLM online o locale come Llama. La class RAG(dspy.Module):classe definisce quindi l'algoritmo RAG. L'inizializzatore è composto solo da due parti.
</p>

<p align="justify">
Innanzitutto, abbiamo bisogno di un modo per cercare in un database di stringhe basato su documenti vettorializzati, definito con ColBERTv2. Utilizza un modello linguistico più vecchio, risalente a soli quattro anni fa (incredibile la velocità con cui si sta evolvendo il settore), ma molto più veloce, in termini di velocità ed efficienza. Ricordate, il modello linguistico più ampio (ovvero, il più costoso da gestire) necessita solo di un numero ragionevole di documenti per essere recuperato. Sebbene ColBERTv2 probabilmente non funzioni bene come GPT-3.5, è più che sufficiente per ottenere i documenti corretti nella maggior parte dei casi. The dspy.Retrievethen utilizza questo database predefinito per la ricerca, quindi non è necessario specificare altro se non il numero di documenti da recuperare.
</p>

<p align="justify">
In secondo luogo, dobbiamo combinare le domande e i documenti in una query per l'LLM. In DSPy, il prompt è astratto. Invece, scriviamo quella che DSPy chiama una firma , che potete immaginare come gli input e gli output di una funzione. A questi dovrebbero essere assegnati nomi inglesi significativi, in modo che DSPy possa generare un prompt efficace per voi. (Di fatto, DSPy utilizza un modello linguistico per ottimizzare i prompt!) In questo caso, abbiamo due input ( questione relevant_documents) separati da una virgola. Il ->viene utilizzato per indicare l'inizio degli output, di cui ne abbiamo solo uno: il answeralla domanda.
</p>

<p align="justify">
Nota: DSPy supporta alcuni tipi di base nelle firme. Ad esempio, è possibile imporre che la risposta debba essere un numero intero indicandolo "question, relevant_documents -> answer:int"nella stringa. Questo comando applicherà la stessa tecnica di rigenerazione in caso di errore appena illustrata nella figura 5.10 .
</p>

<p align="justify">
Questo è tutto ciò che serve per definire il nostro modello RAG! Gli oggetti vengono chiamati e passati nella forwardfunzione, ma è possibile modificare questo codice per aggiungere ulteriori dettagli, se lo si desidera. È possibile convertire tutto in minuscolo, eseguire un correttore ortografico o utilizzare qualsiasi tipo di codice si desideri. Questo approccio consente di combinare e abbinare le regole di programmazione con gli LLM.
</p>

<p align="justify">
È inoltre possibile modificare facilmente la definizione RAG per includere nuovi vincoli e scrivere codice per far sì che un LLM esegua la convalida. Ancora più importante, DSPy supporta l'utilizzo di un set di training/validazione per ottimizzare i prompt, perfezionare gli LLM locali e aiutare a creare un modello testato empiricamente, migliorato e quantificato per raggiungere i propri obiettivi senza dover dedicare molto tempo ai dettagli specifici dell'LLM. Adottare strumenti come questo in tempi brevi fornirà una soluzione molto più robusta che consentirà di aggiornare più facilmente le architetture più recenti.
</p>

<h3>Riepilogo</h3>

<ul>
  <li>
    <p align="justify">
È possibile intervenire per modificare il comportamento di un modello in quattro fasi: la raccolta dati/tokenizzazione, l'addestramento del modello base iniziale, la messa a punto del modello base e l'intercettazione dei token previsti. Tutte e quattro le fasi sono importanti, ma la messa a punto è quella più efficace per la maggior parte degli utenti per apportare modifiche che riducono i costi e forniscono la capacità ottimale di modificare gli obiettivi del modello.
    </p>
  </li>
  <li>
    <p align="justify">
La messa a punto supervisionata (SFT) esegue il normale processo di addestramento su una raccolta di dati personalizzata più piccola ed è utile per perfezionare la conoscenza del modello di un dominio specifico.
    </p>
  </li>
  <li>
    <p align="justify">
L'apprendimento per rinforzo tramite feedback umano (RLHF) richiede più dati, ma ci consente di specificare obiettivi più complessi di "prevedere il token successivo".
    </p>
  </li>
  <li>
    <p align="justify">
È possibile utilizzare strumenti esistenti come i correttori di sintassi per rilevare output LLM errati nei casi in cui il formato di output deve essere rigoroso, come nel caso di JSON o XML. La generazione e il controllo della sintassi possono essere eseguiti in un ciclo finché l'output non soddisfa i vincoli sintattici necessari.
    </p>
  </li>
  <li>
    <p align="justify">
La generazione aumentata del recupero (RAG) è un metodo diffuso per ampliare l'input di un LLM, individuando prima i contenuti pertinenti tramite un motore di ricerca o un database e inserendoli poi nel prompt.
    </p>
  </li>
  <li>
    <p align="justify">
Stanno iniziando a emergere framework di codifica come DSPy che separano l'LLM specifico, la vettorializzazione e la definizione dei prompt dalla logica di come gli input e gli output dell'LLM vengono modificati per un'attività specifica. Questo metodo consente di creare soluzioni LLM più affidabili e ripetibili, in grado di adattarsi rapidamente a nuovi modelli e metodi.
    </p>
  </li>
</ul>

<h2>6 Oltre l'elaborazione del linguaggio naturale</h2>

<table>
  <td>
    <ul>
      <li>
      <p align="justify">
Come funzionano i livelli di trasformazione su dati diversi dal testo
      </p>
      </li>
      <li>
      <p align="justify">
Aiutare gli LLM a scrivere software funzionante
      </p>
      </li>
      <li>
      <p align="justify">
Adattare gli LLM in modo che comprendano la notazione matematica
      </p>
      </li>
      <li>
      <p align="justify">
Come i trasformatori sostituiscono i passaggi di input e output per lavorare con le immagini
      </p>
      </li>
    </ul>
  </td>
</table>

<p align="justify">
Sebbene la modellazione del linguaggio naturale fosse lo scopo principale dei trasformatori, i ricercatori di machine learning hanno rapidamente scoperto che potevano prevedere qualsiasi cosa che coinvolgesse sequenze di dati. I trasformatori visualizzano una frase come una sequenza di token e producono una sequenza correlata di token, come una traduzione da una lingua all'altra, oppure prevedono i token successivi in una sequenza, ad esempio quando rispondono a domande o si comportano come un chatbot. Sebbene la modellazione e la previsione di sequenze siano strumenti potenti per interpretare e generare il linguaggio naturale, il linguaggio naturale è l'unico dominio in cui gli LLM possono essere utili.
</p>

<p align="justify">
Molti tipi di dati, diversi dal linguaggio umano, possono essere rappresentati come una sequenza di token. Il codice sorgente utilizzato per implementare il software ne è un esempio. Invece delle parole e della sintassi che ci si aspetterebbe di vedere in inglese, il codice sorgente è scritto in un linguaggio di programmazione come Python. Il codice sorgente ha una propria struttura che descrive le operazioni che uno sviluppatore di software vuole che un computer esegua. Come nel linguaggio umano, i token nel codice sorgente hanno un significato che varia a seconda del linguaggio utilizzato e del contesto in cui compaiono. Anzi, il codice sorgente è più strutturato e specifico del linguaggio umano. Un linguaggio di programmazione con sfumature di ambiguità e significato sarebbe difficile da interpretare per un computer e più difficile da modificare e mantenere per altri.
</p>

<p align="justify">
Il codice sorgente, o semplicemente "codice" (come lo chiameremo d'ora in poi), è solo un esempio di come LLM e trasformatori funzionano con dati che non sono linguaggio naturale. Quasi tutti i dati che possono essere riformulati come una sequenza di token possono utilizzare i trasformatori e le numerose lezioni che abbiamo imparato sul funzionamento degli LLM. Questo capitolo esaminerà tre esempi che diventano progressivamente meno simili al linguaggio naturale: codice, matematica e visione artificiale.
</p>

<p align="justify">
Ciascuno di questi tre diversi tipi di dati, noti come modalità dati , richiederà un nuovo modo di considerare gli input o gli output di un trasformatore. Tuttavia, in tutti i casi, il trasformatore stesso rimarrà invariato. Continueremo a sovrapporre più livelli di trasformatore per costruire un modello e continueremo ad addestrare i livelli del trasformatore utilizzando la discesa del gradiente. Il codice, essendo il più simile al linguaggio naturale, non richiede troppe modifiche. Per far funzionare bene un LLM in codice, tuttavia, cambieremo il modo in cui gli output dell'LLM generano token successivi. Successivamente, esamineremo la matematica, dove è necessario modificare la tokenizzazione per far sì che un LLM esegua correttamente operazioni di base come l'addizione. Infine, per la visione artificiale, che riguarda l'elaborazione di immagini e l'esecuzione di attività come il rilevamento e l'identificazione di oggetti, modificheremo sia gli input che gli output, mostrando come è possibile convertire un tipo di dati molto diverso in una sequenza sostituendo completamente il concetto di token. Nella figura 6.1 mostriamo le parti degli LLM che è necessario modificare per funzionare con ciascuna modalità dati .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.1 Se scomponiamo un LLM in tre componenti principali: input (tokenizzazione), trasformazione (trasformatori) e generazione di output (unedding), possiamo utilizzare nuove modalità di dati modificando almeno uno dei componenti di input o di output. Nel frattempo, il trasformatore non richiede modifiche nella maggior parte dei casi d'uso perché è di uso generale.
      </p>
    </figcaption>
    
<img width="1062" height="646" alt="CH06_F01_Boozallen" src="https://github.com/user-attachments/assets/3613e797-43a3-4b0d-9156-610871b11474" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Lavorando con tutti e tre i nuovi tipi di dati, dobbiamo risolvere un problema comune. Come possiamo fornire all'LLM o al trasformatore la capacità di utilizzare le conoscenze relative a quella specifica area disciplinare? Solitamente, questo problema viene risolto integrando software esterno nell'LLM. Si può pensare a questi componenti software esterni come a strumenti. Analogamente a come si ha bisogno di un martello per piantare un chiodo in un pezzo di legno, gli LLM possono trarre vantaggio dall'utilizzo di strumenti per raggiungere gli obiettivi finali. Strumenti sviluppati per la programmazione ci aiuteranno a migliorare gli LLM di programmazione. Sapere come gli esseri umani elaborano i calcoli e gli strumenti che utilizziamo per automatizzarli ci aiuterà a creare LLM di matematica migliori. Capire come rappresentiamo le immagini come pixel (che alla fine trasformiamo in sequenze di numeri che rappresentano la quantità di rosso, verde e blu in una parte di un'immagine) ci permetterà di convertirli in sequenze per l'LLM. Riflettendo sulle conoscenze specifiche relative al tuo lavoro in cui gli LLM non sono ancora stati applicati, sarai in grado di identificare le caratteristiche uniche dei dati con cui lavori per modificare un LLM in modo che funzioni meglio con i dati di quel dominio di conoscenza.
</p>

<h3>6.1 LLM per lo sviluppo del software</h3>

<p align="justify">
Abbiamo già brevemente discusso del fatto che gli LLM possono scrivere codice sorgente per il software. Nel capitolo 4 , abbiamo chiesto a ChatGPT di scrivere del codice Python per calcolare la costante matematica \(\pi\) . Successivamente, gli abbiamo chiesto di convertire quel codice in un linguaggio poco noto chiamato Modula-3. Il software è stata una delle prime cose in cui si è scoperto che gli LLM potevano essere d'aiuto, come conseguenza relativamente naturale del funzionamento della programmazione. I linguaggi di programmazione sono progettati per essere letti e scritti dagli esseri umani, proprio come il testo! Di conseguenza, possiamo generare codice senza modificare il processo di tokenizzazione. Tutto ciò che abbiamo discusso sulla costruzione di LLM si applica allo stesso modo al codice e ai linguaggi umani.
</p>

<p align="justify">
Possiamo vederlo osservando la tokenizzazione di ChatGPT di due segmenti di codice simili per Python e Java nella figura 6.2 . Qui, utilizziamo sfumature di grigio per mostrare il tokenizzatore di OpenAI ( https://platform.openai.com/tokenizer ), che suddivide il codice in token diversi. Sebbene lo stesso token possa avere un colore diverso in ogni esempio, possiamo concentrarci su come il tokenizzatore suddivide il codice in token e sulle somiglianze tra i due esempi. Queste includono elementi come
</p>

<ul>
  <li>
    <p align="justify">
L'indentazione per ogni riga di codice
    </p>
  </li>
  <li>
    <p align="justify">
Le variabili x e i(nella maggior parte dei casi)
    </p>
  </li>
  <li>
    <p align="justify">
Il nome della funzione e l'istruzione di ritorno
    </p>
  </li>
  <li>
    <p align="justify">
Gli operatori, come +=
    </p>
  </li>
</ul>

<p align="justify">
Queste somiglianze rendono molto più semplice per un LLM correlare le somiglianze tra ogni porzione di codice. Le somiglianze implicano anche che l'LLM condivida informazioni tra linguaggi di programmazione con pratiche di denominazione, sintassi e codifica comuni durante la formazione.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.2 Due esempi simili di codice scritto nei linguaggi di programmazione Python (a sinistra) e Java (a destra). Questi mostrano come la codifica a coppie di byte possa identificare token simili in linguaggi diversi. I riquadri mostrano i singoli token. I metodi di tokenizzazione standard per i linguaggi umani svolgono un lavoro ragionevole sul codice, poiché presenta molte somiglianze con il linguaggio naturale.
      </p>
    </figcaption>
    
<img width="1100" height="319" alt="CH06_F02_Boozallen" src="https://github.com/user-attachments/assets/df3e1770-ef59-439b-9e0b-fff2bc66e218" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Gli sviluppatori software sono incoraggiati a utilizzare nomi di variabile significativi che riflettano il ruolo o lo scopo di una variabile nei programmi che scrivono. Le variabili con nomi simili initValuevengono suddivise in due token per inite Value, utilizzando gli stessi token per rappresentare il testo in linguaggio naturale in cui compare il prefisso "init" della parola "Value". Quindi non solo condividiamo informazioni tra linguaggi di programmazione con sintassi simile, ma condividiamo anche informazioni sul contesto e l'intenzione del codice tramite i nomi delle variabili. Gli LLM traggono vantaggio anche dai commenti al codice che i programmatori aggiungono per descrivere parti complesse del codice per sé stessi o per altri programmatori. Nella figura 6.3 , abbiamo la versione Java ripetuta con una modifica nel nome della variabile e un commento descrittivo (ma non necessario nella vita reale) all'inizio della funzione.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.3 Codice scritto in Java, incluso un commento che descrive le funzioni del codice. Poiché (si spera) un codice (buono) contiene molti commenti, esiste una naturale combinazione di linguaggio naturale e codice che l'LLM può utilizzare per ottenere informazioni. Quando le variabili hanno nomi descrittivi, diventa più facile per il modello correlare le informazioni tra il codice e l'intento descritto nei commenti e nei nomi delle variabili.        
      </p>
    </figcaption>
    
<img width="1100" height="419" alt="CH06_F03_Boozallen" src="https://github.com/user-attachments/assets/c2656dce-8d26-41af-bbd0-25455215af12" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Nella maggior parte dei casi, otteniamo gli stessi token tra codice e commenti, collegando linguaggi umani e di programmazione poiché utilizzano la stessa rappresentazione. Che lavoriamo con un linguaggio di programmazione o con un linguaggio naturale, otteniamo gli stessi token e incorporamenti. Il bello è che un LLM riutilizzerà le informazioni sui linguaggi naturali per catturare il significato del codice sorgente, proprio come fanno i programmatori umani.
</p>

<p align="justify">
In ogni caso, vediamo che la tokenizzazione non è perfetta per il codice. Ci sono casi limite in cui il tokenizzatore dell'LLM non converte i tipi di dati nel codice nello stesso token. Ad esempio, si può notare che il token for (doublenell'argomento della funzione viene gestito in modo diverso dal token for doublenel corpo della funzione. Tuttavia, queste differenze sono simili ai problemi che già riscontriamo negli LLM per il linguaggio naturale, dove diversi casi di punteggiatura attorno a una parola come "hello", "hello." e "hello!" vengono interpretati come token diversi. Poiché gli LLM possono gestire queste piccole differenze, è logico che possano gestire lo stesso problema anche per il codice. Il problema è, per molti versi, più facile da gestire per un LLM nel codice perché il codice è sensibile alle maiuscole e alle minuscole, quindi non dobbiamo preoccuparci che situazioni testuali come "hello" e "Hello" vengano mappate in modo inappropriato a token diversi. Nel codice, "hello" e "Hello" sarebbero nomi di variabili o funzioni separati e distinti. Trattarli come token separati è corretto perché il linguaggio di programmazione li tratta come elementi diversi.
</p>

<p align="justify">
La generazione di codice è particolarmente interessante dal punto di vista applicativo, grazie alle diverse opportunità di autovalidazione. Possiamo applicare tutte le lezioni sul fine tuning supervisionato (SFT) e sull'apprendimento per rinforzo con feedback umano (RLHF) del capitolo 5 per rendere un LLM un agente di codifica efficace.
</p>

<h3>6.1.1 Migliorare gli LLM per lavorare con il codice</h3>

<p align="justify">
Il primo passo per migliorare un LLM per il codice è garantire che gli esempi di codice siano presenti nei dati di training iniziali. Data la natura di Internet, la maggior parte degli sviluppatori LLM lo ha già fatto: gli esempi di codice sono frequenti online e finiscono naturalmente nei set di dati di training di tutti.
</p>

<p align="justify">
Migliorare i risultati diventa quindi un'opportunità per applicare la SFT, dove raccogliamo esempi di codice aggiuntivi e perfezioniamo il nostro LLM sugli esempi di codice forniti. Repository open source come GitHub, che contengono volumi significativi di codice, rendono particolarmente semplice ottenere grandi quantità di codice. Il codice raccolto da fonti come GitHub costituisce la base di un set di dati di ottimizzazione per gli LLM che interpretano e producono codice.
</p>

<p align="justify">
Il caso più interessante è l'utilizzo di RLHF per migliorare l'utilità di un modello per la scrittura di codice. Anche in questo caso, sono disponibili molti strumenti e set di dati che consentono di creare un set di dati RLHF decente per un assistente di programmazione. Fonti come Stack Overflow consentono agli utenti di inserire domande, offrono la possibilità ad altri di fornire risposte a queste domande e includono un sistema in cui gli altri utenti votano le risposte migliori. Le fonti di dati includono competizioni di programmazione come CodeJam, che forniscono molti esempi di soluzioni a uno specifico problema di programmazione. L'integrazione di informazioni da fonti di dati come queste è mostrata nella figura 6.4 .
</p>

<p align="justify">
Come tutte le buone soluzioni di apprendimento automatico, si ottengono i risultati migliori se si creano ed etichettano i dati specifici per il proprio compito. Si dice che OpenAI abbia fatto questo per generare codice, assumendo appaltatori per completare le attività di codifica come parte della creazione dei dati per il loro sistema [1]. Indipendentemente da come vengono raccolti i dati di addestramento e di fine-tuning, la strategia generale rimane la stessa: utilizzare tokenizzatori standard e SFT con RLHF per creare un LLM su misura per generare codice. Questa ricetta è stata utilizzata con successo per produrre LLM come Code Llama [2] e StarCoder [3].
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.4 Lo sviluppo di un LLM per il codice richiede più fasi di perfezionamento. Le procedure di addestramento standard, come quelle descritte nel capitolo 4 , producono un LLM di base iniziale. Utilizzando una grande quantità di codice, SFT crea un LLM che funziona bene con il codice. L'inclusione di RLHF come seconda fase di perfezionamento migliora la capacità dell'LLM di produrre codice.
      </p>
    </figcaption>
    
<img width="1100" height="401" alt="CH06_F04_Boozallen" src="https://github.com/user-attachments/assets/ea640806-4a84-4b45-bc95-ec6cf9de385f" />

  </figure>
</div>
  </td>
</table>

<h3>6.1.2 Validazione del codice generato dagli LLM</h3>

<p align="justify">
Gli LLM sono particolarmente utili per la generazione di codice perché prevedono una fase di verifica oggettiva e di facile esecuzione: il tentativo di compilare il codice in un programma eseguibile [4]. Quando si genera un linguaggio naturale, è difficile verificare la correttezza dell'output generato da un LLM perché il linguaggio naturale può essere soggettivo. Non esiste un modo automatico per verificare la veridicità o la veridicità dell'output generato da un LLM. Tuttavia, quando si genera codice, il semplice controllo della corretta compilazione del codice in un eseguibile è un buon primo passo e consente di individuare gran parte del codice errato. Alcuni prodotti commerciali vanno oltre e integrano strumenti come compilatori (software che trasformano il codice sorgente in eseguibili) e strumenti di visualizzazione nel loro backend. Ad esempio, ChatGPT può verificare se il codice che scrive viene compilato prima di restituirlo all'utente. Se il codice non supera questa fase di verifica, ChatGPT tenterà di generare codice diverso per il prompt ricevuto. Se il modello non riesce a creare codice valido da compilare, avviserà l'utente di questo fatto.
</p>

<p align="justify">
Oltre a verificare la compilabilità del codice, gli LLM sono sempre più in grado di creare metodi per convalidare la correttezza funzionale. Molti strumenti di generazione di codice utilizzano gli LLM per generare test unitari, ovvero piccoli programmi che forniscono input di esempio al codice generato e ne convalidano la correttezza. In alcuni casi, queste funzionalità richiedono allo sviluppatore di descrivere i casi di test che desidera che l'LLM generi, e l'LLM crea un'implementazione iniziale come punto di partenza per ulteriori test.
</p>

<p align="justify">
Il codice è particolarmente speciale perché esistono diversi modi per convalidarne l'output, oltre alla semplice compilazione. Ad esempio, la compilazione del codice non può avvenire finché l'LLM non ha completato la generazione della risposta.
</p>

<p align="justify">
Considerando che gli LLM sono costosi da gestire e non vogliamo che l'utente attenda troppo a lungo l'output, sarebbe ideale se l'LLM potesse correggere gli errori prima di completare una generazione estesa. Applicando ancora una volta le lezioni del capitolo 5, possiamo utilizzare un parser sintattico per verificare se il codice è errato prima di completare l'intero processo di generazione. Se parti del codice di output non superano un controllo sintattico di base, possiamo istruire l'LLM a rigenerare solo quella porzione di codice difettosa. Mostriamo il processo di base alla base di questo nella figura 6.5 , dove l'LLM esegue un controllo per token invece di attendere il completamento della generazione prima di controllare il codice tramite compilazione. Il controllo sintattico è meno costoso e può essere più rapido della compilazione, ma non convalida che un compilatore possa trasformare il codice in un programma eseguibile funzionante.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.5 Un esempio di codice Python in cui if(A > B)sono stati generati i token correnti. Se il token successivo prodotto dall'LLM è una nuova riga, si verificherà un errore di sintassi perché ifun'istruzione deve terminare con due punti per essere valida. L'esecuzione di un controllo sintattico su ogni nuovo token ci consente di rilevare questo errore e forzare l'LLM a scegliere un token alternativo che non causi un errore di sintassi.
      </p>
    </figcaption>
    
<img width="620" height="578" alt="CH06_F05_Boozallen" src="https://github.com/user-attachments/assets/e18f7124-5f76-4fce-8839-30aec098cf44" />

  </figure>
</div>
  </td>
</table>

<h3>6.1.3 Miglioramento del codice tramite formattazione</h3>

<p align="justify">
L'utilizzo di parser per il controllo della sintassi e di compilatori per produrre eseguibili funzionanti semplifica notevolmente l'adattamento dei LLM al nuovo dominio problematico della generazione di codice. Tuttavia, un ulteriore trucco è utile. Possiamo utilizzare strumenti noti come formattatori di codice (noti anche dai programmatori come linter ) per modificare la tokenizzazione e migliorare le prestazioni.
</p>

<p align="justify">
Il problema è che possono esserci molti modi per scrivere codice che esegue le stesse funzioni ma è tokenizzato in modo diverso. Applicare un linter per regolare la formattazione del codice sorgente aiuta a rimuovere le differenze tra due porzioni di codice funzionalmente equivalenti, ma diverse. Sebbene la riformattazione del codice non sia un requisito per il corretto funzionamento dei LLM, aiuta a evitare inutili ridondanze che possono verificarsi. Ad esempio, si consideri il linguaggio di programmazione Java che utilizza le parentesi per iniziare e terminare un nuovo ambito in un programma. Varie forme di spazio vuoto ora non sono importanti, ma verrebbero tokenizzate in modo diverso, soprattutto perché le parentesi sono facoltative per un ambito che utilizza una sola riga di codice! La Figura 6.6 mostra come questi diversi formati legali esistano per il codice che esegue le stesse funzioni e come potremmo, idealmente, convertire il codice in un'unica rappresentazione canonica.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.6 Un esempio di codice Java che mostra come diversi modi di formattare lo stesso codice portino a diverse tokenizzazioni, sebbene ciascuna sia semanticamente identica. I linter sono uno strumento comune per forzare il codice a seguire una specifica regola di formattazione. Invece, un linter può essere utilizzato per creare una forma "base" identica, evitando così di rappresentare informazioni non necessarie (come spazi anziché tabulazioni).
      </p>
    </figcaption>
    
<img width="1100" height="494" alt="CH06_F06_Boozallen" src="https://github.com/user-attachments/assets/12824a93-bd26-4e52-bf4b-3f260bfb45e6" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
La rimozione degli aspetti non funzionali del codice è chiamata canonicalizzazione , ovvero convertiamo il codice con variazioni di formattazione in una forma standard o "canonica". Qui, abbiamo dimostrato un metodo robusto di canonicalizzazione aggiungendo token speciali come <code>NEW SCOPE</code> quelli che catturano il fatto che esista un nuovo contesto per l' ifistruzione, indipendentemente dal fatto che si tratti di un'istruzione a riga singola o multiriga. Invece di aggiungere token speciali, possiamo utilizzare una formattazione coerente in tutto il codice (ad esempio, usare sempre spazi anziché tabulazioni, una nuova riga prima {o senza). Sia l'analisi sintattica che la formattazione speciali miglioreranno le prestazioni di un LLM del codice. Il metodo robusto, in cui aggiungiamo token speciali, offrirà prestazioni migliori rispetto alla formattazione, ma ha il costo aggiuntivo di scrivere e mantenere un parser personalizzato per il codice che aggiunge tali token speciali. Il problema di modificare il tokenizzatore sarà più critico nella prossima sezione, quando discuteremo dell'utilizzo degli LLM per la matematica.
</p>

<h3>6.2 LLM per matematica formale</h3>

<p align="justify">
Gli LLM possono anche svolgere compiti matematici solitamente piuttosto impegnativi per gli esseri umani. Questi compiti vanno oltre la semplice esecuzione di operazioni come addizione e sottrazione per calcolare numeri; includono matematica formale e simbolica. Forniamo un esempio dei tipi di matematica formale di cui stiamo parlando nella figura 6.7 . Si può chiedere a questi LLM di calcolare derivate, limiti e integrali e di scrivere dimostrazioni. Possono produrre risultati sorprendentemente ragionevoli.
</p>

<p align="justify">
Gli LLM per il codice sono pratici perché possiamo usare parser e compilatori per validare parzialmente i loro output. Una corretta tokenizzazione è fondamentale per creare un LLM utile per la matematica. L'uso degli LLM per la matematica è ancora un'area di ricerca particolarmente attiva [6], quindi i modi migliori per far sì che un LLM esegua calcoli matematici non sono ancora noti. Tuttavia, i ricercatori hanno identificato alcuni problemi che si concentrano nella fase di tokenizzazione della creazione e dell'esecuzione di un LLM.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.7 Un problema di matematica simbolica che il Minerva LLM può risolvere correttamente. Sebbene questo esempio mescoli il linguaggio naturale con contenuti matematici, la tokenizzazione standard utilizzata da molti LLM non consentirebbe questo tipo di output matematico e può causare alcuni problemi sorprendenti. (Immagine concessa in licenza Creative Commons da [5])
      </p>
    </figcaption>
    
<img width="1100" height="405" alt="CH06_F07_Boozallen" src="https://github.com/user-attachments/assets/f755757a-6e02-4646-994b-dbb285b2de6e" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Nota : nel capitolo 5 abbiamo accennato al fatto che il fine-tuning può essere applicato più volte, e gli LLM in matematica ne sono un ottimo esempio. I ricercatori spesso creano LLM in matematica perfezionando gli LLM in codice, che a loro volta vengono creati perfezionando gli LLM in testo generico. Tra SFT e RLHF in ogni fase, vengono applicati da tre a sei cicli di perfezionamento all'LLM originale a valle per gli LLM in matematica.
</p>

<h3>6.2.1 Input sanificato</h3>

<p align="justify">
Gli LLM in matematica spesso soffrono di una preparazione dell'input che può funzionare bene per il testo in linguaggio naturale, ma degrada la rappresentazione dei concetti matematici. Nel testo, le rappresentazioni matematiche formattate spesso includono simboli come {}<>;^. Simboli speciali come questi vengono comunemente rimossi dai dati di training quando si lavora con testo normale. Per preservare queste informazioni è necessario riscrivere i parser di input per la tokenizzazione, in modo da garantire di non rimuovere i dati da cui si sta cercando di far apprendere il modello.
</p>
  
<p align="justify">
Rappresentazioni multiple per equazioni matematiche equivalenti complicano ulteriormente la formazione degli LLM alla comprensione della matematica, proprio come la formattazione multipla può causare problemi durante l'elaborazione dei linguaggi di programmazione. Diversi formati come TeX, asciimath e MathML consentono di esprimere la notazione matematica utilizzando testo normale, ma forniscono istruzioni a un tipografo per la corretta rappresentazione delle equazioni. Questi formati offrono molti modi diversi per rappresentare la stessa equazione. Mostriamo un esempio di questo problema nella figura 6.8 . Ci sono problemi con il metodo di impaginazione della matematica (ovvero, come disegnare l'equazione scegliendo TeX rispetto a MathML) e con la rappresentazione della matematica (ovvero, due modi matematicamente equivalenti di esprimere la stessa cosa).
</p>

<p align="justify">
Si tratta di due forme di un problema che è emerso più volte nella nostra discussione sugli LLM: modi diversi di rappresentare la stessa cosa. Nel caso della matematica, la preferenza attuale è quella di mantenere la matematica formattata usando TeX e alternative molto simili ma meno frequenti come asciimath, e di scartare contenuti prolissi come MathML. Basiamo questa motivazione su tre fattori:
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.8 Un'equazione matematica in alto a sinistra illustra due diversi problemi di rappresentazione che si verificano in matematica. La matematica ben formattata richiede un linguaggio di composizione. TeX e MathML sono due linguaggi di composizione diversi che hanno testo e, quindi, tokenizzazione molto diversi. Separatamente dal linguaggio di composizione, esistono molti modi per rappresentare la stessa affermazione matematica.
      </p>
    </figcaption>
    
<img width="1100" height="507" alt="CH06_F08_Boozallen" src="https://github.com/user-attachments/assets/a9252b0e-98a0-4198-9e1f-db883fffc8db" />

  </figure>
</div>
  </td>
</table>

<ul>
  <li>
  <p align="justify">
La matematica formattata basata su TeX è la forma di matematica più comune e disponibile grazie a fonti accessibili al pubblico come arXiv, che utilizza costantemente la formattazione TeX.
  </p>
  </li>
  <li>
  <p align="justify">
Mantenere tutte le rappresentazioni simili a TeX attenua la sfida di apprendere formati multipli e, di conseguenza, set di token molto diversi.
  </p>
  </li>
  <li>
  <p align="justify">
Il MathML più dettagliato utilizza una varietà più ampia di token; pertanto, sono necessarie più risorse di elaborazione per memorizzare i dati associati a ciascun token univoco.
  </p>
  </li>
</ul>

<p align="justify">
Scegliere TeX come unica rappresentazione preferita per la matematica negli LLM non risolve il problema dell'esistenza di molteplici modi per scrivere equazioni equivalenti. Determinare quali equazioni siano uguali è così difficile che i ricercatori hanno dimostrato che nessun singolo algoritmo può determinare l'equivalenza di due espressioni matematiche. (Siamo un po' vaghi con le parole, dato che questa sezione riguarda la matematica formale , quindi vi indicheremo la fonte [7]). Finora, la risposta migliore per gli LLM sembra essere "lasciare che sia il modello a provare a capirlo", che finora ha avuto un discreto successo. Ma non saremmo sorpresi se gli sviluppatori dei futuri LLM di matematica investissero molto nel miglioramento della pre-elaborazione creando rappresentazioni canoniche più coerenti per le equazioni matematiche che riducano la varietà di possibili espressioni per le espressioni equivalenti.
</p>

<h3>6.2.2 Aiutare gli LLM a comprendere i numeri</h3>

<p align="justify">
Per la maggior parte delle persone, i numeri sono la parte più accessibile della matematica. È possibile inserirli in una calcolatrice e ottenere il risultato. Sebbene possa essere noioso, è possibile eseguire calcoli a mano se non si dispone di una calcolatrice. Si seguono regole fisse per ottenere il risultato. Sorprendentemente, gli LLM hanno molte difficoltà a eseguire questo tipo di calcoli meccanici, ma gli sviluppatori hanno lavorato per migliorare la capacità dei tokenizzatori di lavorare meglio con i numeri.
</p>

<p align="justify">
Il primo problema è che l'algoritmo standard di codifica a coppie di byte (BPE) produce tokenizzatori che creano token incoerenti per i numeri. Ad esempio, "1812" verrà probabilmente tokenizzato come un singolo token perché ci sono riferimenti alla Guerra del 1812 in migliaia di documenti; i tokenizzatori probabilmente scomporranno 1811 e 1813 in numeri più piccoli. Per approfondire il motivo per cui ciò accade, si consideri la stringa iniziale 3252+3253e il modo in cui GPT-3 e GPT-4 tokenizzano questa stringa. GPT-4 farà un lavoro migliore perché sembra tokenizzare i numeri iniziando ogni volta con le prime tre cifre, ottenendo un numero di tre cifre seguito da un numero di una sola cifra. GPT-3 appare incoerente perché cambia l'ordine in cui tokenizza i numeri, come mostrato nella figura 6.9 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.9 Gli studenti di LLM non possono imparare a fare calcoli aritmetici di base se non tokenizzano le cifre in modo coerente. In questa figura, le sottolineature indicano token diversi. Le cifre tokenizzate potrebbero rappresentare le decine, le centinaia o le migliaia di un dato numero. GPT-3 (a sinistra) è incoerente nel modo in cui i numeri vengono tokenizzati, rendendo l'addizione di due numeri inutilmente complessa. GPT-4 è migliore (ma non perfetto) nel tokenizzare i numeri in modo coerente.
      </p>
    </figcaption>
    
<img width="882" height="701" alt="CH06_F09_Boozallen" src="https://github.com/user-attachments/assets/37e77a97-e90d-4a55-88c1-bc25f8173235" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Ora si è verificato un problema significativo. Il token "3" per GPT-3 si verifica due volte in due contesti diversi, una volta nella posizione delle migliaia ( tremiladuecento ...) e una volta nella posizione delle decine (tremiladuecentocinquantatré ). Affinché GPT-3 addizioni correttamente questi numeri, il tokenizzatore deve acquisire correttamente quattro posizioni diverse delle cifre. Al contrario, GPT-4 utilizza l'ordine delle rappresentazioni delle cifre per ciascun numero, rendendo più facile ottenere il risultato corretto.
</p>

<p align="justify">
Si stanno ancora sperimentando diversi modi per modificare il tokenizzatore per migliorare la capacità degli LLM di lavorare con i numeri. Se vogliamo tokenizzare le cifre in sottocomponenti, l'approccio migliore al momento è separare ogni numero, come 3252, in singole cifre, come "3, 2, 5, 2" [8]. Tuttavia, esistono anche altre alternative.
</p>

<p align="justify">
Un altro approccio interessante per rappresentare i numeri è chiamato xVal [9], con l'idea di sostituire ogni numero con lo stesso token che rappresenta "un numero". Potremmo chiamare questo token speciale NUM, che verrà mappato su un vettore di numeri dal livello di incorporamento di cui abbiamo parlato nel capitolo 3 .
</p>

<p align="justify">
Il trucco intelligente è includere un moltiplicatore con ogni token, un secondo numero moltiplicato per il valore del vettore incorporato. Per impostazione predefinita, l'LLM utilizza un moltiplicatore di 1 per ogni token. Moltiplicare qualsiasi cosa per 1 non produce alcun effetto. Ma per qualsiasi NUMtoken che incontriamo, verrà invece moltiplicato per il numero originale del testo! In questo modo, possiamo rappresentare ogni possibile numero che potrebbe apparire, anche valori frazionari, inclusi quelli che non sono apparsi nei dati di addestramento. I numeri acquisiti in questo modo sono correlati in modo semplice e intuitivo. Lo mostriamo più in dettaglio nella figura 6.10 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.10 xVal utilizza un trucco per ridurre il numero di token e renderli meno ambigui. Modificando il modo in cui l'LLM converte i numeri in vettori, un singolo vettore rappresenta ogni numero, come il numero 1. Utilizzando sempre il token 1 e moltiplicandolo per il numero osservato, evitiamo molti casi limite nella rappresentazione dei token numerici, come numeri che non sono mai apparsi nei dati di addestramento. Questo metodo di conversione semplifica anche il supporto di numeri frazionari come 3,14.
      </p>
    </figcaption>
    
<img width="1100" height="408" alt="CH06_F10_Boozallen" src="https://github.com/user-attachments/assets/161ef36b-a030-4239-80d3-5ef6776a9030" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Sia le cifre coerenti che la strategia xVal condividono un'importante consapevolezza. Sappiamo come rappresentare la matematica e algoritmi semplici come l'addizione e la moltiplicazione delle elementari. Se progettiamo l'LLM per tokenizzare la matematica in un modo più coerente con il modo in cui noi, come esseri umani, svolgiamo compiti matematici, i nostri LLM acquisiranno capacità matematiche migliori e più coerenti.
</p>

<h3>6.2.3 Anche gli LLM di matematica utilizzano strumenti</h3>

<p align="justify">
Il lettore attento potrebbe aver notato che la maggior parte dei problemi di tokenizzazione relativi alla matematica riguarda la gestione di cifre e non di matematica simbolica. Gli LLM non possono eseguire addizioni o sottrazioni essenziali senza modificare il tokenizzatore e mantenendo simboli tipicamente "cattivi" come {}<>;^. Abilitare il calcolo modificando il modo in cui il tokenizzatore gestisce i numeri può sembrare un problema di poco conto. Tuttavia, è un fattore significativo per buone prestazioni simboliche e spesso insufficiente per gestire altre forme di matematica simbolica. Ottenere le migliori prestazioni possibili nella matematica simbolica si basa su strumenti esterni e su trucchi intelligenti con l'output degli LLM.
</p>
  
<p align="justify">
Se avete mai avuto la calcolatrice TI-89 che risolveva le derivate, sapete che i computer possono automatizzare i calcoli senza LLM. Funzionalmente, i sistemi di computer algebra (CAS) possono fornire questa funzionalità. Un CAS implementa algoritmi per eseguire alcuni (ma non tutti) i passaggi matematici. Il calcolo delle derivate è uno di questi, quindi avere un LLM che utilizza un CAS, come Sympy, aiuta a garantire che l'LLM esegua sempre correttamente determinati passaggi. Tuttavia, la possibilità di integrare un CAS come Sympy in un LLM non garantisce che l'intera sequenza di passaggi venga eseguita correttamente.
</p>

<p align="justify">
Per convalidare la correttezza, gli LLM in matematica hanno iniziato a utilizzare un linguaggio di programmazione chiamato Lean . In Lean, il programma è una sorta di dimostrazione matematica e non verrà compilato se contiene un errore nella dimostrazione. Di fatto, i passaggi di dimostrazione errati vengono considerati un tipo di errore di sintassi che può essere rilevato. Una volta rilevato, come abbiamo mostrato in altri esempi, l'output può essere rigenerato dall'LLM finché la dimostrazione, generata come programma Lean, non viene compilata correttamente, proprio come mostrato nella sezione 6.1.2 .
</p>

<p align="justify">
L'utilizzo di Lean può garantire che una dimostrazione restituita da un LLM sia corretta al 100%, ma non vi è alcuna garanzia che l'LLM riesca a trovare la dimostrazione. In particolare, potrebbero esserci casi in cui l'LLM potrebbe essere in grado di risolvere correttamente il problema, ma potrebbe non essere in grado di esprimerlo utilizzando Lean. La logica alla base di questo problema è rappresentata nella figura 6.11 , e si riduce al fatto che l'efficacia dell'uso degli strumenti negli LLM dipende dalla varietà di esempi di utilizzo dello strumento nei dati di training. Poiché Lean è relativamente nuovo e di nicchia, ci sono pochi esempi di messa a punto di un LLM per utilizzarlo in modo efficace. Persone come te e me dovranno generare quegli esempi per produrre dati di training adeguati per insegnare a un LLM come utilizzare Lean.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.11 Dato un obiettivo matematico, far sì che un LLM utilizzi il metodo Lean (percorso corretto) potrebbe non portare a una dimostrazione verificabilmente corretta, perché potrebbe non essere efficace nell'utilizzare il metodo Lean come strumento. Far sì che l'LLM produca una dimostrazione normale (percorso sinistro) potrebbe produrre una dimostrazione corretta, ma non un modo per verificare che sia (o non sia) corretta.
      </p>
    </figcaption>
    
<img width="766" height="883" alt="CH06_F11_Boozallen" src="https://github.com/user-attachments/assets/5629677e-f684-46fc-bf48-86c036738d92" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Cosa si può fare se l'LLM non fornisce una prova verificabile della correttezza dei calcoli? Un trucco utilizzato oggi è quello di eseguire l'LLM più volte. Poiché il token successivo viene selezionato in modo casuale, si può potenzialmente ottenere un risultato diverso con una risposta diversa ogni volta che si esegue l'LLM. La risposta che appare più frequentemente è con ogni probabilità corretta. Questo processo non garantisce la correttezza della dimostrazione, ma è utile.
</p>

<h3>6.3 Trasformatori e visione artificiale</h3>

<p align="justify">
Il processo di traduzione di codice e matematica in token è piuttosto intuitivo. Il codice è fondamentalmente testo utilizzato per dire ai computer cosa fare in modo estremamente pedante. La matematica è difficile da convertire in token, ma abbiamo discusso di come sia possibile. La visione artificiale è un'altra storia, in cui i dati coinvolti sono immagini o video rappresentati tramite pixel. L'idea di token per le immagini sembra confusa. Come diavolo potremmo convertire un'immagine in token? Le immagini in genere contengono molti dettagli e non è possibile combinare semplicemente un gruppo di piccole immagini in un'unica immagine coerente come si fa quando si mettono insieme delle parole per formare una frase. Ciononostante, possiamo applicare i trasformatori alle immagini se pensiamo alla tokenizzazione come a un processo per convertire qualsiasi input in una sequenza di numeri.
</p>

<p align="justify">
Nota: esisteva un approccio alla rappresentazione delle immagini come una combinazione di piccole immagini chiamate "codici" . I codici possono essere utili, ma non sono la stessa cosa nello spirito della nostra discussione. Considerate questo come un spunto di riflessione da esplorare se volete conoscere alcune vecchie tecniche di visione artificiale.
</p>

<p align="justify">
Sebbene algoritmi di riconoscimento di immagini e generatori di immagini di alta qualità esistessero già da molti anni prima dei trasformatori, questi ultimi sono rapidamente diventati uno dei metodi principali per lavorare con le immagini nell'apprendimento automatico. Sia le architetture di trasformatori visivi (ViT) che utilizzano esclusivamente trasformatori, sia i modelli di architettura mista come VQGAN e U-Net Transformer che combinano trasformatori con altri tipi di strutture dati, hanno ottenuto un grande successo sia nell'interpretazione di dati basati su immagini sia nella produzione di straordinarie immagini generate al computer a partire da descrizioni testuali. Può sembrare controintuitivo che i trasformatori funzionino così bene nelle immagini, perché queste non hanno l'aspetto di sequenze discrete di simboli come il linguaggio naturale, il codice o le sequenze di amminoacidi. Tuttavia, i trasformatori svolgono un ruolo fondamentale nella visione artificiale, apportando coesione globale ai modelli.
</p>

<h3>6.3.1 Conversione di immagini in patch e viceversa</h3>

<p align="justify">
Concettualmente, sostituiremo il processo di tokenizzazione e di embedding con un nuovo processo che restituisce una sequenza di vettori simile ai livelli di embedding discussi nella sezione 3.1.1 . L'approccio prevalente per creare una sequenza che rappresenta un'immagine consiste nel dividere l'immagine in un insieme di patch . Di conseguenza, sostituiremo il nostro tokenizzatore con un estrattore di patch che restituisce una sequenza di vettori. L'output di un LLM utilizza un livello di unembedding per riconvertire i vettori in token. Poiché non abbiamo token, abbiamo bisogno di un combinatore di patch per prendere gli output di un trasformatore e unirli in un'unica immagine coerente. Mostriamo questo processo nella figura 6.12 . Si prega di prestare particolare attenzione al fatto che la parte centrale del diagramma rimane la stessa di quella dei LLM basati su testo. Riutilizziamo gli stessi livelli di trasformazione e l'algoritmo di apprendimento (discesa del gradiente) tra testo e immagini.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.12 A sinistra, questo diagramma semplificato mostra come l'input di testo viene tokenizzato e incorporato prima di essere inviato al trasformatore. Un livello di unembedding converte quindi l'output del trasformatore nella rappresentazione testuale desiderata. L'input e l'output saranno immagini durante l'esecuzione di un'attività di visione artificiale. Il trasformatore rimane lo stesso, ma poi modifichiamo il metodo per suddividere l'immagine in una sequenza di vettori per eseguire l'estrazione di patch anziché la tokenizzazione. L'LLM produce l'output dell'immagine utilizzando un combinatore di patch, analogo al livello di unembedding per gli LLM di testo
      </p>
    </figcaption>
    
<img width="1100" height="598" alt="CH06_F12_Boozallen" src="https://github.com/user-attachments/assets/fcbec0a7-ad74-48c3-ae36-6554b1362851" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Poiché tutto, tranne la generazione della sequenza vettoriale in input e le fasi di output, rimane invariato, possiamo concentrarci sul funzionamento della conversione delle immagini da e verso vettori. Sarà utile concentrarsi prima sul lato input.
</p>

<p align="justify">
Come suggerisce il nome patch , l'estrattore di patch suddivide ogni immagine in una sequenza di immagini più piccole. È comune scegliere una dimensione fissa per la patch, come un quadrato di \(16 \x 16\) pixel. Vogliamo una dimensione fissa in modo che sia facile da inserire in una rete neurale, che elabora sempre dati di dimensione fissa, e piccoli in modo che rappresentino solo una parte dell'intera immagine. Suddividere un'immagine in patch è simile a suddividere il testo in una raccolta di token. Ogni singolo token non è informativo, ma se combinato con altri token, forma una frase coerente.
</p>

<p align="justify">
Una volta suddivisa un'immagine in patch, ogni pixel di quella patch viene convertito in tre numeri che rappresentano la quantità di rosso, verde e blu (RGB) presente in ciascun pixel. Un vettore iniziale viene creato combinando i valori RGB di ciascun pixel in un unico vettore lungo. Quindi, per il nostro quadrato di \(16 \x 16\) pixel con tre valori di colore per ogni pixel, avremo un vettore con 768 valori di lunghezza (16 di altezza, 16 di larghezza e un valore RGB per ogni pixel). Quindi, una piccola rete neurale che potrebbe avere solo uno o due livelli elabora ogni vettore separatamente per ottenere gli output finali. Questa rete neurale implementa un processo di estrazione delle caratteristiche molto leggero che non richiede significative risorse di memoria o di calcolo. Questo schema è comune nella visione artificiale perché il primo livello di solito apprende schemi semplici come "buio dentro, luce fuori" e non necessita della maggiore spesa o potenza di un livello trasformatore per apprendere le caratteristiche di base di una patch di immagine. L'intero processo è riassunto nella figura  6.13 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.13 L'estrazione di patch è un processo semplice. L'estrattore di patch scompone un'immagine in riquadri quadrati chiamati patch. Le immagini sono costituite da valori di pixel che sono già numeri, quindi convertiamo ogni patch in un vettore di numeri. Quindi, utilizziamo una piccola rete neurale come preprocessore prima di passare i vettori alla rete neurale completa basata sul trasformatore.
      </p>
    </figcaption>
    
<img width="1100" height="471" alt="CH06_F13_Boozallen" src="https://github.com/user-attachments/assets/4f8361ca-5d4f-465d-886b-51d40b413f67" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Esistono molti modi possibili per progettare la piccola rete neurale utilizzata nell'estrattore di patch, ma generalmente tutti funzionano ugualmente bene. Un'opzione è quella di utilizzare quella che viene chiamata rete neurale convoluzionale (CNN), un tipo di rete neurale che comprende che i pixel vicini sono correlati tra loro. Altri hanno utilizzato lo stesso tipo di strato lineare che è un componente di uno strato trasformatore. In questo caso, il modello complessivo che include la piccola rete neurale e una serie di trasformatori è spesso chiamato trasformatore visivo .
</p>

<p align="justify">
La progettazione della piccola rete è un dettaglio minore, ma vale la pena menzionarlo perché la sua esistenza è rilevante per il combinatore di patch che produce l'output finale. Non importa se si sceglie una CNN o un livello lineare per l'architettura della piccola rete neurale, ma è essenziale garantire che la forma dell'output corrisponda alla forma dell'input. Ad esempio, se si hanno \(16 \x 16\) patch, è possibile utilizzare la piccola rete per forzare l'output ad avere \(16 \x 16 \x 3 = 768\) valori, indipendentemente dalle dimensioni del livello del trasformatore stesso. Per produrre l'output dell'immagine, si inverte il processo di estrazione delle patch per convertire i vettori in patch e quindi combinare le patch in un'immagine, come mostrato in figura 6.14 .
</p>

<p align="justify">
Abbiamo quindi sostituito con successo la tokenizzazione dell'input e l'incorporamento dell'output con nuovi livelli incentrati sulle immagini. Per molti versi, questo è molto più funzionale della tokenizzazione. Non c'è bisogno di creare/tenere traccia di un vocabolario, nessun processo di campionamento, ecc. Questa è una visione cruciale dell'applicabilità generale dei trasformatori come nucleo generale di un LLM. Se si riescono a trovare molti dati e un metodo ragionevole per convertirli in una sequenza di vettori, è possibile utilizzare i trasformatori per risolvere determinate classi di problemi di input e output.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.14 Rispetto alla figura 6.13 , le frecce qui vanno nella direzione opposta. Lo scopo è sottolineare che il combinatore e l'estrattore di patch fanno la stessa cosa, ma operano in direzioni diverse. La rete neurale è più importante in questa fase in quanto consente di forzare l'uscita del trasformatore ad avere la stessa forma delle patch originali, perché possiamo controllare la dimensione dell'uscita di qualsiasi rete neurale.
      </p>
    </figcaption>
    
<img width="1100" height="452" alt="CH06_F14_Boozallen" src="https://github.com/user-attachments/assets/ddd8b336-8c5d-4f13-9c52-063c64dc69d8" />

  </figure>
</div>
  </td>
</table>

<h3>6.3.2 Modelli multimodali che utilizzano immagini e testo</h3>

<p align="justify">
La capacità di modificare l'input e l'output di un LLM per arrivare a un trasformatore visivo significa che possiamo prendere un'immagine come input e produrre un'immagine come output. Ciò dimostra come un trasformatore possa produrre input di diverse modalità, ma abbiamo discusso solo casi in cui input e output sono la stessa modalità. Possiamo avere testo come input e testo come output oppure immagini come input e immagini come output. Tuttavia, il deep learning è flessibile! Non c'è nulla che ci obblighi a utilizzare la stessa modalità sia come input che come output o addirittura a limitare input e output a un'unica modalità. È possibile combinare testo come input con immagine come output, immagini come input e testo come output, testo e immagini come input e audio come output, o qualsiasi altra combinazione di modalità dati che si possa immaginare. La Figura 6.15 mostra come immagine e testo ci offrano quattro modi totali in cui potremmo combinarli per gestire diversi tipi di dati.
</p>

<p align="justify">
Creando un modello che utilizza le immagini come input e il testo come output, creiamo un modello di didascalia delle immagini . Possiamo addestrare questo modello a generare un testo che descriva il contenuto dell'immagine di input. Modelli come questi contribuiscono a rendere le immagini più facilmente individuabili e ad aiutare gli utenti ipovedenti.
</p>

<p align="justify">
Creando un modello che utilizza il testo come input e un'immagine come output, creiamo un modello di generazione di immagini . È possibile descrivere l'immagine desiderata utilizzando le parole e il modello può creare un'immagine realistica basata sull'input. Prodotti famosi come MidJourney sono modelli di questo tipo. Sebbene la loro implementazione implichi più di un semplice trasformatore di visione, l'idea di base è la stessa: abbinando un input basato su testo con un output basato su immagini e una grande quantità di dati, possiamo creare nuove funzionalità multimodali che abbracciano diverse tipologie di dati.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.15 Quattro combinazioni che mostrano diversi tipi di input e output del modello. L'esempio più a destra rappresenta un normale LLM basato su testo di cui abbiamo già parlato. A sinistra, mostriamo possibilità come un modello di generazione di immagini che accetta testo come input ("Disegnami un'immagine di un segnale di stop in una zona alluvionale") o un modello di didascalia di immagini che genera testo che descrive un'immagine in input ("Questa immagine mostra un segnale di stop circondato da acqua torbida").
      </p>
    </figcaption>
    
<img width="1100" height="920" alt="CH06_F15_Boozallen" src="https://github.com/user-attachments/assets/57f5e56d-2375-4d97-bf4f-139893c4dbe8" />

  </figure>
</div>
  </td>
</table>

<h3>6.3.3 Applicabilità delle lezioni precedenti</h3>

<p align="justify">
Altre lezioni apprese in questo libro rimangono rilevanti per questi modelli di trasformazione della visione e multimodali. In definitiva, imparano a fare ciò per cui sono stati addestrati e, quando si cerca di modificarli in modi che vanno oltre quanto trovato nei dati di addestramento, si potrebbe ottenere un risultato insolito. Ad esempio, potremmo dire a un modello di generazione di immagini "Disegna qualsiasi cosa tranne un adorabile gatto", e probabilmente otterremo un gatto come mostrato nella figura 6.16.
</p>

<p align="justify">
Questi modelli sono (attualmente) addestrati con coppie di immagini e frammenti di testo che descrivono l'immagine. In questo modo, apprendono una forte correlazione per produrre visualizzazioni di qualsiasi elemento nella frase di input. Ad esempio, il modello vuole produrre un gatto poiché la parola " gatto " è presente nella frase di input. Richieste di disegno astratto più sofisticate come "Disegna qualsiasi cosa tranne..." non compaiono in tali set di dati, quindi il modello non è addestrato a gestire tali richieste.
</p>

<p align="justify">
Allo stesso modo, mentre LLM come ChatGPT hanno sviluppato il prompting come strategia per ideare input che producano gli output desiderati, il prompting è stato sviluppato anche per i modelli di didascalia delle immagini. Non è raro includere informazioni insolite come "Unreal3D", il nome del software utilizzato per generare immagini 3D per videogiochi, al fine di produrre output con uno stile e una qualità particolari. Parole come " alta risoluzione" e persino i nomi di artisti, vivi e morti, vengono utilizzati per cercare di influenzare i modelli affinché producano stili particolari.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 6.16 Generato con una vecchia versione di Stable Diffusion, un popolare modello di generazione di immagini. Nonostante il comando "Non disegnare un gatto", il modello è stato addestrato a generare contenuti. La richiesta è al di fuori di ciò che il modello era incentivato ad apprendere, quindi non può gestirla. Questo è simile ai problemi con gli LLM che ripropongono output simili ma errati perché il modello ha visto dati simili durante l'addestramento.
      </p>
    </figcaption>
    
![CH06_F16_Boozallen](https://github.com/user-attachments/assets/d689cf53-6ee2-47ec-9cfd-a3daddb8021c)

  </figure>
</div>
  </td>
</table>

<h3>Riepilogo</h3>

<ul>
  <li>
  <p align="justify">
Gli LLM traggono vantaggio dalla possibilità di utilizzare strumenti esterni. Ad esempio, un LLM di codice può utilizzare correttori di sintassi e compilatori per rilevare errori nella generazione di codice. Quando l'LLM rileva un errore, l'output viene rigenerato, riducendo al minimo il rischio di fornire all'utente codice inutile o non funzionante.
  </p>
  </li>
  <li>
  <p align="justify">
I tokenizzatori devono essere modificati per supportare la matematica, mantenendo i simboli insoliti utilizzati per esprimere calcoli matematici formattati e modificando la rappresentazione delle cifre. Possiamo migliorare ulteriormente i corsi di laurea magistrale in matematica fornendo loro strumenti come sistemi di algebra computazionale per rilevare ed evitare errori.
  </p>
  </li>
  <li>
  <p align="justify">
I trasformatori possono essere applicati alle immagini suddividendo l'immagine in patch, dove ogni patch diventa un vettore e genera una sequenza di input che il trasformatore deve elaborare. Le patch sono concettualmente simili ai token per i LLM testuali.
  </p>
  </li>
  <li>
  <p align="justify">
I trasformatori possono utilizzare diverse modalità di dati per l'input e l'output, consentendo la creazione di modelli multimodali come quelli utilizzati nella didascalia delle immagini e nella generazione delle immagini.
  </p>
  </li>
</ul>

<h2>7 Idee sbagliate, limiti e capacità eccezionali degli LLM</h2>

<table>
  <td>
    <h3></h3>
    <ul>
    <li>
    <p align="justify">
In che modo gli LLM e gli esseri umani differiscono nell'apprendimento
    </p>
    </li>
        <li>
    <p align="justify">
Migliorare gli LLM nelle applicazioni sensibili alla latenza e alla scala
    </p>
    </li>
        <li>
    <p align="justify">
Produrre output intermedi per risultati finali migliori
    </p>
    </li>
        <li>
    <p align="justify">
Come la complessità computazionale limita ciò che un LLM può fare
    </p>
    </li>
    </ul>
  </td>
</table>

<p align="justify">
Grazie a ChatGPT, il mondo ha acquisito una maggiore consapevolezza degli LLM e delle loro potenzialità. Nonostante questa consapevolezza, persistono ancora molti malintesi e incomprensioni sugli LLM. Molti credono che gli LLM siano in continuo apprendimento e miglioramento, più intelligenti delle persone e che presto saranno in grado di risolvere ogni problema del mondo. Sebbene queste affermazioni siano esagerate, alcuni temono sinceramente che gli LLM possano sconvolgere seriamente il mondo.
</p>

<p align="justify">
Non vogliamo certo affermare che non vi siano preoccupazioni legittime riguardo agli LLM, e ne parleremo più approfonditamente negli ultimi due capitoli del libro. Tuttavia, molti pensieri e preoccupazioni che potreste incontrare sugli LLM sono ingigantiti rispetto all'evoluzione generale degli LLM e della tecnologia.
</p>

<p align="justify">
Questo capitolo discuterà alcuni aspetti critici del funzionamento degli LLM e di come questi aspetti siano correlati a questi preconcetti. In definitiva, questi aspetti operativi degli LLM influenzano il modo in cui si desidera utilizzare o evitare un LLM nella pratica.
</p>

<p align="justify">
In primo luogo, discuteremo le differenze tra il modo in cui apprendono gli esseri umani e gli LLM. Gli esseri umani apprendono velocemente, mentre gli LLM sono statici per impostazione predefinita. Sebbene gli LLM possano essere incredibilmente efficaci nell'elaborazione dei dati, le persone sono meglio attrezzate per essere più produttive quando imparano cose nuove.
</p>

<p align="justify">
Successivamente, affronteremo il motivo per cui il termine "pensare" è fuorviante quando si considera il funzionamento di un LLM. Sottolineeremo che è meglio pensare al funzionamento di un LLM come a un'attività di elaborazione dati , perché gli LLM non distinguono tra formulazione ed emissione di output. Al contrario, spesso le persone "pensano prima di parlare".
</p>

<p align="justify">
Infine, discuteremo la portata delle capacità di calcolo degli LLM e come i concetti di informatica ci aiutino a comprendere alcuni dei limiti intrinseci delle capacità attuali e future di un LLM. Questi tre argomenti sono correlati, quindi ne scopriremo il collegamento man mano che li approfondiremo.
</p>

<h3>7.1 Tasso di apprendimento umano vs. LLM</h3>

<p align="justify">
Sebbene ne abbiamo discusso implicitamente, è utile essere espliciti su come la formazione di un LLM differisca dall'apprendimento di una persona. Il testo fluido e spesso lucido prodotto dall'intelligenza artificiale generativa e le analogie che utilizziamo per mettere in relazione le capacità degli LLM con quelle umane possono far sembrare che ci sia una qualche relazione tra i due. Molte persone online stanno promuovendo l'idea che tale connessione tra ciò che un LLM può fare e ciò che un essere umano può fare sia reale. In realtà, i due sono molto diversi e comportano considerazioni importanti su quando, come e perché si potrebbe preferire una persona a un'intelligenza artificiale e su come esseri umani e intelligenza artificiale possano lavorare insieme.
</p>

<p align="justify">
Dal materiale trattato finora, sappiamo che gli LLM apprendono predicendo la parola successiva, utilizzando centinaia di milioni di documenti come esempi. Nel capitolo 4 , abbiamo presentato il processo algoritmico di "apprendimento" negli LLM: l'algoritmo di discesa del gradiente, che altera i parametri della rete neurale di un LLM tentando di predire il token successivo in un input campione. Successivamente, nel capitolo 5 , abbiamo mostrato come algoritmi di fine-tuning, come RLHF, alterino nuovamente i parametri dell'LLM. Queste due componenti dell'apprendimento in un LLM hanno una somiglianza minima con l'apprendimento umano e impongono alcune limitazioni cruciali a ciò che possiamo aspettarci dall'LLM. Uno degli aspetti più critici è la velocità e l'efficacia di questo approccio di apprendimento in relazione al volume di dati forniti al processo di formazione.
</p>

<p align="justify">
Per approfondire questo aspetto, considerate come un LLM apprenda in relazione a come apprendono le persone. Avete mai incontrato qualcuno che non ha mai parlato con nessuno, che non ha mai avuto un genitore che gli parlasse, eppure in qualche modo capiva la lingua? Probabilmente no. In effetti, la conversazione è una parte fondamentale dell'acquisizione linguistica [1]. Almeno inizialmente, si acquisiscono conoscenza e linguaggio dall'interazione e dalla comunicazione con gli altri e con l'ambiente. Di conseguenza, si può apprendere efficacemente con molte meno informazioni di quelle che un LLM ha nei dati su cui si basa.
</p>

<p align="justify">
Negli scenari migliori di acquisizione del linguaggio infantile, gli studi hanno osservato che i bambini sono esposti a circa 15.000 parole parlate totali al mese [2]. Se dovessimo essere generosi e arrotondare questa cifra a 20.000 parole e considerare questo periodo su 100 anni, una persona incontrerebbe fino a 24 milioni di parole parlate nel corso della sua intera vita. Questa è chiaramente una sovrastima enorme. Aggiungiamo a questo il fatto che la maggior parte delle persone è in grado di parlare fluentemente la propria lingua madre, con una comprensione implicita del vocabolario e della struttura linguistica, almeno all'età di 18 anni. Ora confrontiamo questo con i corsi di laurea triennale (LLM). GPT-3, ad esempio, è stato addestrato su centinaia di miliardi di parole. Basandosi solo sul conteggio delle parole, questo è un modo molto inefficiente per imparare una lingua!
</p>

<p align="justify">
L'acquisizione del linguaggio ci aiuta anche a riconoscere le nette differenze nel modo in cui le parole vengono acquisite. Neonati e bambini piccoli iniziano con parole semplici, come "mamma" e "papà" , e alla fine imparano concetti di base come "colori", "no" , " cibo ", ecc. Parole più complesse vengono aggiunte nel tempo, basandosi sulle parole precedenti. Eppure, un LLM inizia con la visione di tutte le parole simultaneamente in base alla loro frequenza d'uso. In effetti, è corretto immaginare un LLM che simbolizza questo stesso libro come parte del suo primo "apprendimento", acquisendo simultaneamente la conoscenza di tutto il suo vocabolario finale, invece di iniziare con concetti semplici e costruire conoscenze su quelle basi. Sebbene questo processo contribuisca alla velocità di apprendimento di un LLM, può compromettere la capacità dell'LLM di tracciare relazioni di alto livello tra i concetti.
</p>

<p align="justify">
Il principale vantaggio di un LLM rispetto agli esseri umani è la scala su cui opera e la sua capacità di svolgere più attività contemporaneamente. Questo vantaggio è un tema comune nell'apprendimento automatico e nel deep learning. Non è facile assumere un esercito di persone per esaminare libri contabili, note spese, documenti interni o qualsiasi mezzo di informazione per svolgere un lavoro di conoscenza come scrivere una recensione, individuare potenziali frodi o rispondere a una domanda politica oscuro. Tuttavia, è possibile ottenere rapidamente un esercito di computer per tentare di automatizzare queste attività. Mentre un singolo LLM può analizzare più parti di una frase contemporaneamente, è possibile utilizzare più computer che eseguono lo stesso LLM per lavorare in parallelo. La formazione per un LLM offre un'opportunità simile: gli LLM vengono formati su più parole di quante ne leggerete o sentirete mai in tutta la vostra vita, ed è possibile formare un LLM di grandi dimensioni noleggiando o acquistando migliaia di computer per svolgere il lavoro contemporaneamente.
</p>

<p align="justify">
Considerando questi fatti, insieme al materiale trattato nei capitoli precedenti, possiamo elencare diversi pro e contro di alto livello dell'utilizzo degli LLM per svolgere determinate attività rispetto agli esseri umani. Una sintesi di questi fattori è mostrata nella figura 7.1 , che descrive come i vantaggi e gli svantaggi degli LLM porteranno a benefici e svantaggi naturali del loro utilizzo e, quindi, fornirà spunti su dove gli LLM dovrebbero e non dovrebbero essere utilizzati.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 7.1 Una sintesi dei punti di forza e di debolezza degli LLM rispetto agli esseri umani che svolgono lo stesso compito. Questi portano a considerazioni naturali che è necessario valutare quando si utilizza un LLM. Da queste, possiamo trarre raccomandazioni generali per un utilizzo efficace dell'LLM.
      </p>
    </figcaption>
    
<img width="1100" height="329" alt="CH07_F01_Boozallen" src="https://github.com/user-attachments/assets/f9c66cd3-4ca1-48fb-b52a-6c51d5bd7366" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Ecco alcuni dei vantaggi degli LLM:
</p>

Gli LLM ben formati dispongono di un'ampia raccolta di informazioni di base, quindi svolgono bene molti compiti che non sono poi così diversi da quelli già affrontati, e richiedono poco lavoro per rendere il modello efficace. Sebbene queste informazioni non siano necessariamente corrette o dettagliate, l'ampiezza delle aree tematiche su cui un LLM può ricevere e generare risposte ragionevoli va ben oltre gli ambiti che la maggior parte delle persone può coprire.

Per molti compiti, non è necessario ottenere una risposta esattamente corretta. Richieste ampie di informazioni generali in un'area disciplinare consentono intrinsecamente a un LLM di essere flessibile e senza vincoli nella sua risposta. Questo è particolarmente vero se si perfeziona l'output dell'LLM attraverso altri processi. Ad esempio, una persona potrebbe revisionare un testo per migliorarlo, ma utilizzare un LLM per produrre la prima bozza o fornire ispirazione per superare il blocco dello scrittore e accelerare la creazione dell'opera. Allo stesso modo, un LLM può essere utilizzato per perfezionare la scrittura di un autore, rendendola più naturale o coinvolgente attraverso la riformulazione o l'utilizzo di una più ampia varietà di vocaboli.

Gli LLM possono essere formati più rapidamente rispetto alle persone. È possibile produrre un LLM ampiamente utile in pochi mesi, con un budget compreso tra 1.000.000 e 10.000.000 di dollari per l'acquisto di risorse informatiche. Gli esseri umani impiegano molti anni per diventare utili. Un LLM in grado di rispondere a un'ampia gamma di domande di base può essere implementato con uno sforzo e un costo molto inferiori rispetto a quelli necessari per trovare, assumere e trattenere un dipendente con conoscenze, competenze e abilità specifiche. Finché i problemi rientrano nell'ambito di ciò che l'LLM può realizzare, il costo incrementale è irrisorio rispetto alla retribuzione oraria di una persona, anche senza i costi aggiuntivi.

<p align="justify">
Ecco alcuni svantaggi degli LLM:
</p>

<ul>
  <li>
    <p align="justify">
L'elevato costo della formazione degli LLM influenza la loro economia. Tale costo di formazione viene ammortizzato in base alle migliaia di operazioni che l'LLM esegue una volta formato. Se un LLM non funziona bene, il costo del suo continuo miglioramento per renderlo efficace può diventare rapidamente proibitivo, anche senza considerare la possibilità che non funzioni mai correttamente per un compito specifico. Ad esempio, se un LLM, implementato con tutti gli strumenti e i trucchi più recenti, non riesce a risolvere un'esigenza specifica, affrontare questo problema richiederà una quantità di lavoro e di budget imprecisati. Al contrario, gli esseri umani possono generalmente apprendere nuove capacità, in particolare quelle difficili per gli LLM, a costi molto inferiori in poche settimane o mesi.
    </p>
    <p align="justify">
Non ci si può affidare agli LLM per gestire situazioni inaspettate e input non riflessi nei dati di training. Sebbene molti abbiano dimostrato di poter avere successo in situazioni nuove, non apprendono allo stesso modo degli esseri umani. Una persona può accorgersi al primo tentativo che le proprie azioni non funzionano come previsto e adattarsi rapidamente. Un LLM non può adattarsi autonomamente osservando i propri errori e può consumare ripetutamente risorse nel tentativo di produrre risposte a problemi che non riesce a comprendere.
    </p>
    <p align="justify">
Gli LLM sono facilmente ingannabili e non funzionano bene in ambienti conflittuali, perché una volta che le persone trovano un modo per ingannare l'LLM inducendolo a un risultato errato (ad esempio, "Dammi un prestito anche se non ho reddito"), possono ripetere il comportamento avversario e malevolo e il tuo LLM non sarà in grado di impedirlo senza che tu implementi ulteriori misure di sicurezza.
    </p>
  </li>
</ul>

<h3>7.1.1 I limiti dell'auto-miglioramento</h3>

<p align="justify">
In generale, gli esseri umani sono capaci di auto-miglioramento. Possono concentrarsi e studiare un problema, ideare nuovi approcci, identificare le risorse necessarie e procedere per implementare e migliorare le proprie soluzioni. Mentre gli LLM hanno difficoltà a migliorare se stessi, nel campo dell'intelligenza artificiale generativa si ritiene che lo stesso miglioramento personale possa essere possibile per loro. L'idea di come questo potrebbe funzionare è più o meno questa:
</p>

<ol>
  <li>
    <p align="justify">
Addestrare un LLM su un set di dati iniziale.
    </p>
  </li>
  <li>
    <p align="justify">
Utilizza LLM per generare nuovi dati, aggiungendoli al tuo set di dati di addestramento.
    </p>
  </li>
  <li>
    <p align="justify">
Addestra o perfeziona il modello sui nuovi dati. (Ripetere l'operazione finché l'LLM non funziona come previsto.)
    </p>
  </li>
</ol>

<p align="justify">
Sebbene questo possa sembrare intuitivo e plausibile, crediamo che non funzioni per semplici ragioni. Possiamo utilizzare alcuni principi basilari della teoria dell'informazione, che misura l'informazione come una risorsa quantificabile, per spiegarne il motivo. La base di questa argomentazione è che, in base a una certa misura dell'informazione, il set di dati originale contiene una quantità fissa di informazioni. Nel linguaggio statistico, potremmo descrivere l'informazione originale come la distribuzione delle informazioni disponibili e, attraverso il suo processo di addestramento, l'LLM tenta di approssimare o riprodurre tale distribuzione di informazioni memorizzandola e codificandola nel suo modello. Quando si generano nuovi dati utilizzando un LLM, quel campione di dati è una riproduzione rumorosa e incompleta della distribuzione dei dati originale che l'LLM ha osservato durante il processo di addestramento. Fondamentalmente, è impossibile che l'output dell'LLM contenga nuove informazioni non presenti nei dati di addestramento originali. Di conseguenza, la realtà di tali esperimenti è che cicli successivi di generazione di dati e addestramento degradano la qualità e le prestazioni del modello [3]. Per far funzionare qualcosa del genere, è necessario qualcosa che fornisca informazioni esterne o nuove a ogni ciclo.
</p>

<p align="justify">
Questi concetti si collegano anche al timore di alcuni che l'IA possa migliorare se stessa fino a diventare così intelligente da non avere alcuna speranza di comprenderla o controllarla. Alcuni sostengono che l'LLM possa utilizzare altri strumenti, acquisendo in qualche modo informazioni esterne o ulteriori dati di addestramento, per migliorarsi. In definitiva, ciò richiede la convinzione che, sebbene esistano limiti al miglioramento della maggior parte delle tecnologie, gli LLM saranno immuni a questi limiti, come la legge dei rendimenti decrescenti. La Figura 7.2 descrive i limiti intrinseci all'auto-miglioramento degli LLM.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 7.2 Le preoccupazioni che gli LLM si automigliorino presuppongono la convinzione che gli LLM non seguiranno la normale curva sigmoide o a S dei rendimenti decrescenti che descrive lo sviluppo di quasi tutte le altre tecnologie. Affinché si verifichi un automiglioramento infinito, dobbiamo credere che vincoli come potenza, dati o capacità computazionale siano sempre risolvibili e che, in qualche modo, gli esseri umani non li risolverebbero altrimenti per aree al di fuori degli LLM. Vincoli come questi sono il motivo per cui possiamo descrivere la maggior parte dello sviluppo tecnologico utilizzando curve a S, dove il progresso rallenta man mano che entrano in vigore più vincoli. In altre parole, alla fine raggiungeremo uno stato in cui non potremo semplicemente costruire un computer più grande.
      </p>
    </figcaption>
    
<img width="1100" height="846" alt="CH07_F02_Boozallen" src="https://github.com/user-attachments/assets/effb3429-c6dd-4dc1-9978-762f95637ddc" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Un ottimo esempio di limitazioni al miglioramento tecnico è la legge di Moore, che afferma approssimativamente che il numero di transistor su un chip raddoppierebbe ogni 18-24 mesi. La legge di Moore ha previsto in modo per lo più accurato la crescita dei transistor su un chip, ma ci sono segnali della curva a S dei rendimenti decrescenti nei transistor. Il tasso di raddoppio del numero di transistor su un chip sta diminuendo. Ancora più importante, le prestazioni totali del sistema sono già entrate in questa curva a S. Il numero di transistor è correlato alle prestazioni di elaborazione totali, ma non indica direttamente le prestazioni di elaborazione. Osservando il quadro generale nella figura 7.3 , si noterà che altri vincoli impediscono miglioramenti illimitati nell'intero sistema. A parte la legge di Moore, il costo pratico delle GPU ad alte prestazioni e dell'infrastruttura che le ospita rappresenta un altro ostacolo al miglioramento illimitato.
</p>

<table>
  <td>
    <h3>Gli LLM non sono esseri umani: non giudicateli secondo standard umani!</h3>
    <p align="justify">
Molti titoli accattivanti hanno esaltato le prestazioni degli LLM nell'esame MCAT per la facoltà di medicina, nell'esame di abilitazione alla professione forense e nei test del QI per misurare la loro intelligenza. Sebbene questi siano sempre interessanti e pieni di avvertenze come "Quanti esempi dello stesso tipo di domande sono presenti nei dati di training dell'LLM?", non sono buoni modi per estrapolare informazioni sugli LLM e sulle loro capacità rispetto agli esseri umani. In effetti, definire una definizione esatta di intelligenza è complesso ed è uno dei motivi per cui esistono diversi tipi di test del QI [4]. In definitiva, questi test si sono rivelati utili nel prevedere i risultati delle persone in vari compiti. Tuttavia, questi test non sono progettati per valutare algoritmi di intelligenza e non abbiamo motivo di credere che lo facciano in modo accurato o ragionevole! Il problema è la correlazione, non la causalità. I test del QI sono tutti correlati a risultati desiderabili, ma non misurano una proprietà sottostante che controlla o causa i risultati allo stesso modo, ad esempio, di un test della glicemia. In un test della glicemia, se la glicemia è troppo bassa o troppo alta, sappiamo cosa accadrà perché misura un'importante proprietà sottostante che determina l'esito di un processo che comprendiamo abbastanza bene. I test del QI sono utili, ma la loro utilità deriva da anni di iterazioni e miglioramenti. Ora comprendiamo meglio quali risposte a questi test sono correlate alle prestazioni delle persone, ma non misurano le cause sottostanti di tali prestazioni.
    </p>
  </td>
</table>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 7.3 La legge di Moores è un esempio comune di crescita illimitata, ma è fuorviante. I transistor continuano a raddoppiare, ma frequenza, potenza, prestazioni single-thread e capacità di elaborazione totale no. Quindi le prestazioni totali del sistema non hanno continuato a raddoppiare circa ogni due anni. Altri fattori simili limiteranno le prestazioni dell'LLM e ne influenzeranno la capacità nel tempo. Utilizzato con licenza CC4.0 da https://github.com/karlrupp/microprocessor-trend-data .
      </p>
    </figcaption>

<img width="1100" height="642" alt="CH07_F03_Boozallen" src="https://github.com/user-attachments/assets/110313f4-f598-4d91-8de3-139a71f69b3f" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Esistono molti esempi di informazioni esterne utilizzate per migliorare l'intelligenza artificiale generativa. Alcuni algoritmi creati per mani robotiche utilizzano informazioni esterne provenienti da un simulatore fisico. Apple utilizza un software di modellazione 3D per generare dati che migliorano il riconoscimento dell'iride sui propri telefoni [5]. Negli esempi del capitolo 6 , hai visto un potenziale percorso per migliorare un LLM utilizzando un compilatore per il codice o il linguaggio Lean per verificare la matematica. Questi esempi dimostrano processi completamente automatizzabili che generano nuove informazioni che possono portare all'auto-miglioramento.
</p>

<p align="justify">
Tuttavia, non si è mai assistito a un esempio di auto-miglioramento illimitato; i progressi osservati grazie all'utilizzo di questi strumenti esterni alla fine raggiungono un punto morto e, in ultima analisi, si affidano agli esseri umani per sviluppare le informazioni collaterali, scrivendo simulatori fisici migliori per i robot, compilatori migliori per il codice e sistemi di conoscenza di dominio più evoluti come Lean. Il miglioramento di questi strumenti comporta un costo elevato per la formazione degli LLM, imponendo così un secondo limite economico all'auto-miglioramento degli LLM, che va oltre l'aspetto pratico.
</p>

<h3>7.1.2 Apprendimento a pochi colpi</h3>

<p align="justify">
L'apprendimento a pochi scatti è anche chiamato apprendimento contestuale . Questa tecnica prevede la fornitura di esempi del tipo di output che si desidera che un LLM produca come parte del prompt inviato. Supponiamo di voler fornire a un LLM informazioni accurate su una domanda dell'help desk. È possibile fornire all'LLM un prompt con la domanda di un utente all'help desk, seguito da un esempio del tipo di risposta appropriato. Se si fornisce un solo esempio, si parla di apprendimento a uno scatto . Fornire due esempi invece di uno singolo è noto come apprendimento a due scatti , e così via, quindi questo approccio viene descritto come a pochi scatti perché il numero preciso di esempi non è generalmente importante quanto il fatto che ne vengano forniti solo pochi. Questo metodo di incorporazione di esempi in un prompt è un tipo specifico di progettazione dei prompt, come illustrato nella figura 7.4 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 7.4 I prompt con esempi di come si desidera che l'LLM produca l'output sono chiamati prompt "poche-shot" perché l'LLM non ha rilevato alcun esempio di questo comportamento specifico nei suoi dati di training. Nel prompt, è possibile includere esempi di input e output simili a RLHF/fine-tuning supervisionato (SFT). Questo stile di prompt incoraggia il modello a produrre l'output desiderato fornendo esempi di come dovrebbe apparire l'output desiderato. Poiché gli LLM si addestrano su una quantità così grande di dati non etichettati, gli esempi "k-shot" sono un modo efficace per ottenere risultati migliori con il minimo sforzo.
      </p>
    </figcaption>

<img width="1100" height="372" alt="CH07_F04_Boozallen" src="https://github.com/user-attachments/assets/abac5b7f-c1ba-420f-b7b0-159bae46dcdc" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Includere esempi nei prompt è utile per migliorare le prestazioni di un LLM in nuovi compiti. Non è necessario utilizzare RLHF o SFT per modificare il modello, e funziona meglio del prompting zero-shot, in cui chiediamo all'LLM di svolgere il compito senza esempi. Ma si tratta di un apprendimento efficiente?
</p>

<p align="justify">
Il prompting a poche riprese non è un processo di addestramento, perché non alteriamo il modello in alcun modo, come faremmo nel processo di addestramento o di messa a punto. Lo "stato" o i pesi dell'LLM rimangono gli stessi. Per quanto accuratamente l'LLM esegua il compito il lunedì, sarà esattamente la stessa accuratezza il martedì e il mercoledì, indipendentemente dal numero di migliaia o milioni di prompt a poche riprese che gestisce. Non vi è alcun miglioramento nelle capacità del modello a meno che non si intervenga manualmente per includere esempi migliori nel prompt, fornire più esempi o intervenire in qualche modo. In questo senso, non si verifica alcun vero apprendimento e nulla nel modello cambia. Otteniamo semplicemente un output migliore dal modello modificando il nostro prompt.
</p>

<p align="justify">
Tuttavia, in senso astratto, l'LLM apprende perché il prompt modifica il comportamento del modello fornendo un contesto aggiuntivo per descrivere il problema. Il comportamento esibito tramite prompt è correlato al comportamento ottenuto attraverso la messa a punto su esempi simili [6]. Ciò significa, in breve, che l'apprendimento a pochi scatti non riflette fondamentalmente nulla di diverso da ciò che la discesa del gradiente può già fare.
</p>

<p align="justify">
Nota: se non si dispone di molti dati, il prompting a pochi scatti è probabilmente il modo più efficace per un professionista o un utente per far funzionare bene un LLM sui propri dati. Poiché possiamo pensare a questo prompting come a una discesa del gradiente o a un fine-tuning inefficiente, è necessario aspettarsi rendimenti decrescenti aggiungendo esempi in uno stile a pochi scatti. Ad esempio, se si includono molti esempi di come si desidera che un LLM risponda nel prompt e non si ottengono comunque le prestazioni necessarie, si dovrebbe prendere in considerazione SFT, RLHF e gli altri approcci di fine-tuning che abbiamo discusso nel capitolo 5 .
</p>

<h3>7.2 Efficienza del lavoro: un cervello umano da 10 watt contro un computer da 2000 watt</h3>

<p align="justify">
Il cervello umano consuma l'equivalente di 10 watt per mantenere la coscienza, permettendovi di leggere questo libro. Una workstation di fascia alta con una GPU per l'intelligenza artificiale e l'apprendimento automatico potrebbe facilmente consumare 2.000 watt. Un server di fascia alta per l'esecuzione dei più grandi LLM disponibili oggi si aggira tra i 10.000 e i 15.000 watt. A prima vista, sembrerebbe che utilizzare un LLM potrebbe quindi essere 1.500 volte più inefficiente dal punto di vista energetico rispetto a far svolgere un compito a un essere umano. Dovremmo essere molto orgogliosi di questo aspetto del nostro successo evolutivo e della nostra efficienza, ma è anche solo un aspetto di ciò che potremmo intendere per efficienza. Nella figura 7.5 mostriamo che molti diversi tipi di efficienza potrebbero avvantaggiare una persona rispetto alle macchine .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 7.5 L'hardware costoso che fa funzionare gli LLM porta a diversi compromessi. Ad esempio, il costo di avvio dell'utilizzo degli LLM è spesso elevato e questi non si adattano in modo indipendente. Questa mancanza di adattamento indipendente porta a molte debolezze naturali che un essere umano supererebbe in prestazioni rispetto a un LLM. Alcune debolezze, come il fatto che un modello non cambi senza addestramento, possono essere considerate punti di forza. Non si ottengono processi ripetibili e facili da scalare se ogni nuovo LLM in esecuzione si comporta in modo diverso e imprevedibile.
      </p>
    </figcaption>

<img width="1100" height="532" alt="CH07_F05_Boozallen" src="https://github.com/user-attachments/assets/ddb9e528-292f-4140-ad10-bd555a394fb4" />

  </figure>
</div>
  </td>
</table>

<h3>7.2.1 Potenza</h3>

<p align="justify">
L'energia è uno dei fattori determinanti nel determinare il costo finanziario della creazione e gestione di un LLM, ma la reale necessità non è ancora del tutto chiara. Certo, molti fornitori vi forniranno un preventivo per la gestione di un LLM, ma non conosciamo i costi reali sostenuti da ciascun fornitore o i margini che ciascuno di essi ha stabilito. Ad esempio, un fornitore di LLM potrebbe adottare una strategia di margine negativo o di perdita, e il costo a lungo termine dell'utilizzo di un LLM potrebbe essere superiore a quanto appare in base ai prezzi attuali. Sappiamo che gli LLM generano una domanda significativa di energia, a tal punto che le grandi aziende tecnologiche stanno sviluppando piani per costruire centrali nucleari per supportare l'energia necessaria ai futuri data center per far funzionare tutti i modelli che prevedono [7]. Sulla base di ciò, sembra che possiamo aspettarci che i nuovi LLM saranno più grandi e più assetati di energia, ma il loro valore compenserà il costo di costruzione di centrali elettriche dedicate per i loro data center.
</p>

<p align="justify">
In base a questo fattore, è necessario prestare attenzione quando una soluzione LLM di successo crea una domanda eccessiva; si potrebbero verificare problemi di capacità energetica nel soddisfare tale domanda. Potrebbe anche essere necessario prestare attenzione all'elasticità dei costi energetici. Non solo i fornitori di LLM potrebbero modificare le strutture dei costi, ma se si ospita un LLM autonomamente, negli Stati Uniti si verificano fluttuazioni del prezzo dell'energia pari a 6 volte [8]. Questo potrebbe non rappresentare un problema se la base clienti prevista è di soli 20.000 utenti, ma se si prevede di costruire qualcosa che servirà milioni di utenti o più, il costo dell'energia potrebbe rappresentare un grave rischio operativo e ambientale.
</p>

<h3>7.2.2 Latenza, scalabilità e disponibilità</h3>

<p align="justify">
La latenza è il tempo che intercorre tra l'interrogazione di un LLM e l'ottenimento di un output, la scalabilità descrive la rapidità con cui si può passare da uno a mille LLM in funzione e la disponibilità descrive la possibilità di avere un LLM operativo 24 ore su 24, 7 giorni su 7. Questi sono tutti importanti vantaggi dell'LLM – e più in generale dei computer in generale – rispetto alle persone. Gli LLM e l'intelligenza artificiale/apprendimento automatico possono reagire a più situazioni più velocemente, in qualsiasi momento, rispetto agli esseri umani. Questa velocità di reazione può essere sia positiva che negativa. Quando si dispone di un sistema che richiede supervisione e revisione degli output, non si ottiene il pieno vantaggio di disponibilità di un LLM senza sviluppare un piano di personale adeguato.
</p>

<h3>7.2.3 Raffinamento</h3>

<p align="justify">
Come abbiamo discusso nella sezione 7.1.1 , gli LLM non possono auto-migliorarsi facilmente. Tuttavia, le persone possono migliorare e lo fanno, ed è un obiettivo comune migliorare l'efficienza di un processo nel tempo. Sarà necessario mantenere il personale aggiornato per progettare prompt migliori e creare programmi di formazione più efficaci per migliorare l'efficienza degli LLM; senza di loro, le prestazioni degli LLM non miglioreranno.
</p>

<p align="justify">
Migliorare l'efficienza di un LLM non implica solo l'aggiornamento a LLM più recenti o l'affinamento dei modelli esistenti, ma include anche la creazione dell'infrastruttura e la registrazione di input, output e metriche di performance per studiare cosa funziona e cosa no. È possibile utilizzare framework come DSPy, di cui abbiamo parlato nella sezione 5.5.2, per catturare questi elementi e identificare e gestire i casi che non funzionano o che iniziano a fallire nel tempo, man mano che le circostanze cambiano. Ad esempio, si potrebbe sviluppare un LLM iniziale che funziona bene. Ma quei dannati ragazzi continuano ad aggiungere nuove emoji agli iDroid e agli AppleBot [9]. Senza una formazione aggiuntiva, il vostro LLM non capirà queste nuove emoji, ma i vostri clienti inizieranno inevitabilmente a usarle, quindi il sistema inizierà a funzionare male. Non lo scoprirete mai se non registrate gli input e gli output dell'LLM nei log o non sollecitate feedback dai vostri utenti, che possono fornire informazioni sulle aree in cui l'LLM sta fallendo o avendo successo. L'acquisizione di queste informazioni è essenziale per migliorare e perfezionare il processo, cosa che gli LLM non possono fare senza l'intervento umano.
</p>

<p align="justify">
Nota: il problema degli emoji è un ottimo esempio del perché eliminare la codifica e utilizzare solo LLM probabilmente non accadrà mai. Gli emoji saranno nuovi token che LLM non avrà mai visto nei dati di training, quindi intrinsecamente non sarà in grado di gestirli. Come potremmo gestire questa situazione in pratica? Il nostro primo tentativo sarebbe quello di scrivere codice che rilevi gli emoji e li sostituisca con una descrizione dell'aspetto, dell'intento e delle connotazioni dell'emoji. Potrebbe non funzionare in tutti i casi, ma è per questo che si testa e si convalida.
</p>

<p align="justify">
Nel campo dell'apprendimento automatico, viene prestata notevole attenzione al concetto di "data drift", ovvero la deriva dei dati nel mondo reale che si evolve costantemente rispetto a quanto catturato nei dati di training di un modello. Quando si tratta di linguaggio naturale, gli emoji sono solo un esempio concreto di come i dati del mondo reale cambieranno nel tempo con l'evoluzione dell'uso del linguaggio. L'esempio degli emoji può essere esteso per includere i problemi creati da una nuova terminologia o da nuovi modi di utilizzare le parole esistenti in una lingua. Esaminando il lavoro esistente in questo campo, possiamo identificare ulteriori tecniche per misurare e mitigare la deriva dei dati per gli LLM, come la raccolta di dati di training aggiuntivi e la messa a punto dei modelli o la modifica dei prompt per includere definizioni supplementari per una terminologia inedita.
</p>

<h3>7.3 I modelli linguistici non sono modelli del mondo</h3>

<p align="justify">
Da un LLM è spesso possibile ricavare informazioni accurate sul mondo. Di conseguenza, è facile presumere che un modello linguistico conosca informazioni sul mondo. In effetti, come lettore di questo libro, puoi ragionare sul mondo e su ciò che accadrà senza intraprendere alcuna azione particolare. Ora, non stiamo parlando di qualcosa di così sofisticato come la previsione del mercato azionario, ma anche di azioni e pensieri semplici. Ad esempio, cosa succederebbe se dicessi a qualcuno che il suo maglione è brutto?
</p>

<p align="justify">
Non è necessario interagire con l'ambiente o trovare un maglione brutto per rispondere a questa domanda. Non è necessario parlare o interagire con nessuno o nulla per rispondere a questa domanda. È possibile immaginare il "mondo" dei maglioni e le sensazioni che qualcun altro potrebbe provare e dedurne i risultati. Se vi dicessi che qualcuno indossa il maglione a una festa di Natale (un concorso di maglioni brutti, forse?), potreste aggiornare il vostro modello mentale del mondo e dedurre i risultati senza averli vissuti. Un LLM non può pensare prima di parlare. Generare testo è il modo più vicino che un LLM arriva a "pensare" (usando il termine in senso lato in questo contesto). Potete vedere un semplice esempio di ciò nella figura 7.6 , dove il ragionamento eccessivamente prolisso di un LLM lo porta infine a raggiungere un bel commento. Il ragionamento, sia esso svolto implicitamente o esplicitamente da noi umani, è diverso dal parlare della cosa su cui stiamo ragionando. Per un LLM, non c'è separazione dei processi; è necessario produrre più output per "pensare di più" alla risposta. Pertanto, gli LLM non sono in grado di pensare in modo indipendente dalla generazione di output.
</p>

<p align="justify">
Attenzione: usiamo il termine "pensare" in senso lato nel contesto di un LLM. Per essere pignoli, intendiamo dire che i calcoli che un LLM esegue per rispondere a una domanda non sono dinamici. L'output di 10 token richiede la stessa quantità di lavoro indipendentemente dal contenuto di tali token. Rispondere a un problema complesso che richiede agli esseri umani di pensare di più richiederà probabilmente a un LLM di eseguire più calcoli, ma ciò di solito significa che l'LLM deve anche produrre un output più lungo, anche se la risposta non dovrebbe essere più lunga. Ogni volta che qualcuno usa il termine "pensare" in concomitanza con un LLM, è meglio sostituire "pensare" con "calcolare" .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 7.6 Il contesto e il motivo per cui qualcuno indossa o fa qualcosa di insolito potrebbero rientrare nell'ambito di qualcosa che un LLM riconosce correttamente e per il quale produce una risposta appropriata. Tuttavia, potrebbe non essere possibile per un LLM raggiungere tale risposta appropriata senza produrre un testo intermedio. Per un problema di matematica, questo testo intermedio potrebbe essere utile, ma potrebbe non essere sempre appropriato o desiderabile per un utente.
      </p>
    </figcaption>

<img width="1100" height="585" alt="CH07_F06_Boozallen" src="https://github.com/user-attachments/assets/0acb4601-4f17-4c84-9013-1206adc53e16" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Questo esempio dimostra che un LLM non può pianificare senza generare testo sul processo di pianificazione. Se l'LLM non produce testo, è come se non esistesse. Esistono metodi per costruire prompt che incoraggiano gli LLM a scomporre i propri output per simulare la pianificazione. Questo è spesso chiamato prompt a catena di pensiero (CoT), in cui si include nel prompt un'affermazione come "Pensiamo passo dopo passo". Questa istruzione passo dopo passo spesso migliora la capacità del modello di eseguire le attività [10], ma non è chiaro perché ciò migliori le prestazioni. Ancora una volta, l'ambiguità di cosa significhi "pensare" può causare aspettative irragionevoli su ciò che gli LLM possono e non possono fare.
</p>

<p align="justify">
Anche con CoT, gli LLM commetteranno comunque molti errori, come passaggi mancanti, calcoli mancanti ed esecuzione di ragionamenti logicamente non validi [11]. Altri fattori possono contribuire ai guadagni di prestazioni osservati quando un LLM produce output suddivisi in una serie di passaggi. Considera:
</p>

<ul>
  <li>
  <p align="justify">
Nel capitolo 3, abbiamo parlato dei trasformatori e del meccanismo di attenzione utilizzato nelle loro implementazioni. Abbiamo imparato che più a lungo durano l'input ricevuto e gli output prodotti da un LLM, più calcoli vengono eseguiti dal trasformatore. Quindi, pensare passo dopo passo funziona meglio solo perché l'LLM, tramite il trasformatore, riesce a eseguire più calcoli ? Se l'LLM avesse un modello del mondo, potrebbe eseguire questo calcolo sull'output senza generarlo.
  </p>
  </li>
  <li>
  <p align="justify">
Gli LLM riflettono la natura dei loro dati di formazione. Potrebbero esserci contenuti correlati al metodo "pensa passo dopo passo" e ad altri materiali didattici con contenuti più dettagliati e solitamente corretti. In definitiva, potremmo allineare manualmente la memoria vaga degli LLM con documenti di formazione più pertinenti, piuttosto che far svolgere loro una funzione fondamentalmente diversa.
  </p>
  </li>
</ul>

<p align="justify">
Attenzione: la definizione precisa di "modello del mondo" non è ancora ben definita e può avere connotazioni diverse per persone diverse. Quando si discute di modelli del mondo, è una buona idea discutere prima la definizione in modo che tutti siano sulla stessa lunghezza d'onda. Molti discorsi sui LLM si sovrappongono, un aspetto che approfondiremo negli ultimi due capitoli di questo libro.
</p>

<p align="justify">
Questi problemi sono impegnativi e implicano domande di ricerca aperte. La nostra posizione è che i drammatici fallimenti degli LLM evidenziano che queste sono spiegazioni più probabili di qualcosa di più profondo. È importante notare che alcune ricerche di nicchia si concentrano sull'integrazione di modelli del mondo nei metodi di apprendimento automatico. Un esempio tecnico ma abbastanza accessibile di questo tipo, realizzato da David Ha e Jürgen Schmidhuber nel 2018, è disponibile online ( https://worldmodels.github.io/ ) e mostra enormi miglioramenti delle prestazioni rispetto ai metodi esistenti all'epoca. Altri stanno lavorando alla creazione di modelli del mondo per gli LLM e all'utilizzo degli LLM come modelli del mondo [12]. I metodi attuali non hanno lo stesso elevato grado di flessibilità degli esseri umani; questi esempi hanno una portata più limitata e funzionano per una classe generale di problemi.
</p>

<h3>7.4 Limiti computazionali: i problemi difficili sono ancora difficili</h3>

<p align="justify">
Alcune persone sono preoccupate per l'IA "fuori controllo", in cui un algoritmo di IA diventa così avanzato e capace da poter risolvere problemi che noi non potremmo mai risolvere e che tale IA non avrebbe obiettivi in linea con il benessere umano. Se un'IA di questo tipo esistesse, potrebbe migliorarsi in modi in cui noi stessi non potremmo migliorare, dando vita a un'IA ancora più potente. Molti hanno lasciato che questo pensiero dilagasse, immaginando che un LLM diventi quasi divino nella capacità e nell'abilità di superare gli umani. C'è una questione etica qui che discuteremo più approfonditamente nell'ultimo capitolo del libro. Per ora, c'è una semplice ragione tecnica per cui non siamo così preoccupati da questa idea, e ci aiuta anche a comprendere i limiti realistici degli LLM. In sostanza, ci sono molti modi per misurare quella che possiamo chiamare complessità computazionale o complessità algoritmica. Confrontando la complessità degli LLM con altri algoritmi ben studiati, possiamo essere più specifici su ciò che gli LLM possono e non possono raggiungere. Discuteremo anche di come le soluzioni approssimative ai problemi mediante LLM possano, ove opportuno, evitare parte della complessità delle soluzioni precise agli stessi problemi.
</p>

<p align="justify">
In informatica, dedichiamo molto tempo a studiare la complessità algoritmica. Per la maggior parte degli studenti o dei professionisti, questo significa capire come una variazione nella quantità di dati di input modifichi il tempo necessario a un processo per produrre risultati. Uno dei casi più ideali, che raramente si verifica nella realtà, è che raddoppiando gli input, il processo impiegherà il doppio del tempo. In altre parole, un processo che potrebbe richiedere 2 giorni per n elementi (nel caso di un LLM, un elemento potrebbe essere un token) impiega 4 giorni per 2 volte n . Quando si parla di complessità in informatica, si usa spesso la notazione matematica, nota come notazione Big-O, per comunicare diversi livelli di complessità. Quando il tempo di calcolo di un processo cresce alla stessa velocità della dimensione del suo input, si parla di complessità lineare e si indica in notazione Big-O come O(n ). Se si disegna un grafico con la dimensione dei dati sull'asse x e il tempo di calcolo sull'asse y, si otterrà una linea, poiché sia i dati che il tempo di calcolo crescono alla stessa velocità. Altre complessità comuni nel mondo reale includono la log-lineare ( \(\mathcal{O}(n \log n)\) ), dove \(2 \times n\) potrebbe essere più vicino a 4,4 giorni; quadratica ( \(\mathcal{O}(n^2)\) , dove \(2 \times n\) potrebbe essere più vicino a 8 giorni; ed esponenziale ( \(\mathcal{O}(e^n)\) ), dove il tempo di calcolo cresce così rapidamente all'aumentare della dimensione dell'input che è molto probabile che il mondo non esista più prima che l'algoritmo termini. In ognuno di questi casi, il grafico della dimensione dell'input rispetto al tempo di calcolo diventa più ripido man mano che i sistemi diventano più complessi. In altre parole, per algoritmi più complessi, il tempo di elaborazione aumenterà più rapidamente all'aumentare della quantità di dati elaborati.
</p>

<p align="justify">
Abbiamo intrapreso questo breve viaggio nell'informatica per aiutarvi a comprendere la complessità computazionale dell'esecuzione di un LLM. Per un input di n elementi, l'LLM ha una complessità computazionale di O(n^2) o complessità quadratica. Se possiamo dimostrare che un algoritmo/attività richiede più di O(n^2) lavoro, allora abbiamo sostanzialmente dimostrato che un LLM non può risolvere il problema in modo efficiente perché i suoi algoritmi principali non sono in grado di eseguire algoritmi con quel livello di complessità, con precisione.
</p>

<p align="justify">
Attenzione: questo non è un corso di laurea specialistica su metodi formali o algoritmi; stiamo fornendo una rapida panoramica sullo studio della complessità algoritmica. L'obiettivo è fornire al lettore un'intuizione tecnica per il problema, ma non vi abbiamo ancora fornito tutte le conoscenze necessarie per discutere questo argomento in dettaglio. Per saperne di più su algoritmi e complessità, consultate il libro di Aditya Y. Bhargava Grokking Algorithms: An Illustrated Guide for Programmers and Other Curious People [13].
</p>

<p align="justify">
Se fosse possibile far sì che un LLM risolvesse un problema che richiede, ad esempio, una complessità cubica di \(\mathcal{O}(n^3)\) , ma l'LLM stesso avesse una complessità più rapida (minore) di \(\mathcal{O}(n^2)\) , allora avremmo una contraddizione logica. In altre parole, un LLM non può risolvere un problema complesso più velocemente di quanto indicato dall'analisi di complessità. Molti compiti e algoritmi del mondo reale hanno complessità peggiori di \(\mathcal{O}(n)\) . Descriviamo alcuni esempi nella tabella 7.1 e noterete che la manciata che abbiamo elencato riguarda la logistica o l'allocazione delle risorse. Ad esempio, la consegna di pacchi e la riprogrammazione dei voli sono problemi che presentano complessità algoritmiche estremamente complesse.
</p>

<div align="center">
<img width="611" height="418" alt="image" src="https://github.com/user-attachments/assets/a66c443f-9598-48d3-9c1c-01d7a001b5ea" />
</div>

<p align="justify">
Un secondo motivo importante e correlato per cui ci interessiamo agli algoritmi è la classe di complessità di un algoritmo. Una classe di complessità definisce l'ambito dei possibili algoritmi che un algoritmo può risolvere. Le classi di complessità più note sono \(P\) (per polinomio) e \(NP\) , che sono problemi che richiedono almeno \(\mathcal{O}(e^n)\) di tempo per essere completati. Queste classi molto ampie contengono praticamente tutti i problemi che potrebbero interessarvi.
</p>

<p align="justify">
Nota: molti pensano che \(NP\) stia per non-polinomio , ma è falso! In realtà significa polinomio non deterministico .
</p>

<p align="justify">
Ciò che è interessante e informativo è che William Merrill e Ashish Sabharwal [14] hanno dimostrato che la capacità di un LLM di risolvere problemi è correlata al numero di token che genera nei passaggi intermedi. Per un LLM, generare una risposta rientra in una classe di complessità chiamata \(TC^0\) (sappiamo, gli informatici sono i peggiori nel dare nomi alle cose). Questa classe di complessità è molto restrittiva, il che significa che un LLM può a malapena risolvere qualsiasi cosa. Man mano che i passaggi intermedi \(n\) diventano più lunghi, si raggiunge infine la classe di complessità di \(P\) . Ciò significa che un LLM non può mai risolvere problemi del mondo reale che siano NP o più difficili! Colleghiamo tutto questo nella figura 7.7 , che mostra come questi livelli di classi di complessità si relazionano.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 7.7 Un diagramma di Venn delle complessità computazionali (assumendo \(P \neq NP\) , un dettaglio secondario per i nerd) correlate tra loro. Le frecce in alto forniscono esempi del tipo di problema che una nuova classe di complessità consente di risolvere. Le frecce in basso mostrano dove si collocano gli LLM in termini di complessità.
      </p>
    </figcaption>

<img width="1100" height="672" alt="CH07_F07_Boozallen" src="https://github.com/user-attachments/assets/c4b795e5-9220-4f4f-a002-4f7a78bc4e22" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Questa scoperta è ancora più dannosa perché le classi di complessità descrivono i tipi di problemi che è possibile risolvere, non l'efficienza con cui è possibile risolverli. Ad esempio, un LLM deve generare nell'ordine di \(n^c\) token per risolvere un algoritmo che comporta \(n^c\) di complessità. Tuttavia, un LLM necessita anche di \(\mathcal{O}(n^2)\) di tempo per elaborare \(n\) token, quindi si ottiene uno sforzo computazionale \(\mathcal{O}\left((n^c)^2\right) = \mathcal{O}(n^{2 \times c})\) , un enorme aumento della complessità. Inoltre, questa stima della complessità non tiene conto dei dati di training dell'LLM e del tempo necessario per sviluppare i prompt necessari affinché l'LLM esegua l'algoritmo correttamente e senza errori.
</p>

<h3>7.4.1 Utilizzo di algoritmi fuzzy per problemi fuzzy</h3>

<p align="justify">
Questa discussione su algoritmi e complessità può sembrare molto critica per gli LLM. In realtà, lo è solo se si vogliono applicare gli LLM a problemi che richiedono risultati corretti. Se anche il più piccolo errore è inaccettabile nel vostro sistema, non dovreste usare l'apprendimento automatico, figuriamoci un LLM.
</p>

<p align="justify">
Come l'apprendimento automatico in generale, gli LLM funzionano meglio per i problemi fuzzy, in cui è difficile descrivere cosa renda qualcosa corretto o errato. Nei problemi fuzzy, spesso è accettabile che esistano errori; altri processi possono rimediare a tali errori, oppure il costo degli errori è potenzialmente sufficientemente basso da poter essere ignorato. Ecco perché il testo e il linguaggio naturale sono adatti agli LLM. Le risposte a problemi come "Cosa intendeva Suzy in quell'email?" o "John intendeva insinuare questo nel suo testo?" sono intrinsecamente fuzzy. Il linguaggio umano è pieno di imprecisioni, chiarimenti e ripetizioni che ben si sposano con la difficoltà di far sì che gli LLM risolvano problemi che richiedono risposte coerenti e precise.
</p>

<h3>7.4.2 Quando "abbastanza vicino" è abbastanza buono per i problemi difficili</h3>

<p align="justify">
Per controbattere un attimo, dovremmo anche sottolineare che gli esseri umani non possono risolvere problemi NP-difficili quando usiamo il termine "solve" nel senso di "arrivare alla soluzione ottimale per la quale non esiste una soluzione migliore". Utilizziamo approssimazioni per risolvere problemi complessi perché sappiamo che sono troppo difficili da risolvere perfettamente.
</p>

<p align="justify">
Ad esempio, nella tabella 7.1 e nella figura 7.7, abbiamo menzionato il problema del commesso viaggiatore, un problema famoso e importante per la pianificazione del percorso di consegna. Il corriere postale vuole consegnare la posta di tutti nel minor tempo e distanza percorsa, senza ripetere alcun percorso. Dal punto di vista computazionale, trovare il percorso migliore è NP-difficile, quindi è possibile applicarlo solo a poche centinaia o forse migliaia di destinazioni di consegna. Tuttavia, esistono algoritmi quadratici molto più veloci che approssimano il problema e possiamo dimostrare che forniscono un percorso che non è peggiore di 2 volte la distanza di percorrenza del percorso a distanza minima. Quindi, nel mondo reale, utilizziamo queste e altre tecniche per ottenere soluzioni del tipo "abbastanza vicino è abbastanza buono". Anche gli LLM possono potenzialmente ottenere soluzioni del tipo "abbastanza vicino è abbastanza buono", ma sono comunque vincolati dal fatto che sono inefficienti per problemi esatti.
</p>

<p align="justify">
Senza una comprensione dei dati di training di un LLM, abbiamo difficoltà a stimare quanto bene potrebbe risolvere un problema difficile tramite approssimazione. Si consideri che il gioco degli scacchi è tecnicamente più difficile di NP-difficile. GPT-3.5 può giocare una partita di scacchi decente in grado di sconfiggere un vero essere umano [15], sebbene non al livello di "dominazione di tutti gli esseri umani" che i programmi di scacchi dedicati possono raggiungere. Questo dimostra che gli LLM sono bravi a risolvere approssimativamente problemi molto difficili?
</p>

<p align="justify">
Probabilmente no. Innanzitutto, il gioco degli scacchi di ChatGPT è migliorato notevolmente dopo aver aggiunto gli scacchi come parametro di valutazione ( https://github.com/openai/evals/pull/45 ). Non è irragionevole sospettare che i creatori di ChatGPT abbiano apportato delle modifiche che hanno incorporato gli scacchi come obiettivo esplicito. In secondo luogo, Internet è pieno di partite di scacchi da studiare ed esplorare ( https://old.chesstempo.com/game-database.html ), quindi è probabile che ChatGPT sia stato addestrato su partite di scacchi complete registrate nei suoi dati di addestramento.
</p>

<p align="justify">
Tuttavia, è interessante notare che ChatGPT può utilizzare i dati di training per giocare una partita a scacchi ragionevole, confrontando ciò che ha visto in precedenza con situazioni leggermente diverse in futuro. Quando si considera dove una soluzione basata su LLM funzionerà meglio, raccomandiamo questo schema mentale: applicare gli LLM a problemi ripetitivi e leggermente variabili per massimizzarne l'utilità. Applicazioni come la sintesi di testi, la traduzione linguistica, la stesura delle prime bozze di documenti e la verifica di testi esistenti rientrano tutte in questa categoria.
</p>

<p align="justify">
Lezioni simili provengono da altre aree del deep learning, dove è più facile ragionare su ciò che accade all'interno di un modello rispetto ai LLM. Ad esempio, giocare a Go è stata una delle sfide più longeve nella ricerca sull'intelligenza artificiale per decenni. Solo di recente l'intelligenza artificiale è riuscita a battere giocatori di livello campione. Come gli LLM, le IA che giocano a Go si addestrano osservando molti esempi di partite. Tuttavia, se si costruisse un bot che gioca a Go e che esegue mosse insolite e/o senza senso, sconfiggerebbe l'IA "sovrumana" ma perderebbe contro i dilettanti umani [16]. Questo esempio evidenzia anche il rischio dell'utilizzo di LLM in ambienti avversari, dove gli esseri umani sono molto più abili nell'affrontare le novità significative in una situazione rispetto alle attuali IA/LLM.
</p>

<h3>Riepilogo</h3>

<ul>
  <li>
    <p align="justify">
Il vantaggio principale degli LLM rispetto agli umani è la scalabilità che raggiungono. Gli LLM possono operare a basso costo, 24 ore su 24, 7 giorni su 7, e possono essere ridimensionati per soddisfare la domanda con uno sforzo molto inferiore rispetto alla formazione o alla riduzione della forza lavoro umana.
    </p>
  </li>
  <li>
    <p align="justify">
Gli esseri umani sono più abili nel gestire situazioni molto nuove, il che è importante se le persone che interagiscono con l'LLM potrebbero essere avversari (ad esempio, se cercano di commettere una frode).
    </p>
  </li>
  <li>
    <p align="justify">
Sappiamo che gli LLM sono efficaci per problemi simili a quelli riscontrati in precedenza nei loro dati di addestramento, il che li rende utili per lavori ripetitivi.
    </p>
  </li>
  <li>
    <p align="justify">
L'ingegneria rapida è probabilmente il punto di partenza più efficace per "insegnare" qualcosa di nuovo agli LLM, a meno che non si possano dedicare grandi quantità di sforzi e denaro alla raccolta e alla messa a punto dei dati.
    </p>
  </li>
  <li>
    <p align="justify">
Gli LLM non possono auto-migliorarsi e sono inefficienti nel risolvere problemi algoritmici che richiedono una risposta corretta specifica. Funzionano meglio su problemi "fuzzy", dove esiste un certo intervallo di risultati soddisfacenti e un certo margine di errore è accettabile.
    </p>
  </li>
</ul>

<h3>8 Progettazione di soluzioni con modelli linguistici di grandi dimensioni</h3>

<table>
  <td>
    <h3>Questo capitolo copre</h3>
    <ul>
      <li>
      <p align="justify">
Utilizzo della generazione aumentata del recupero per ridurre gli errori
      </p>
      </li>
      <li>
      <p align="justify">
Come gli LLM possono supervisionare gli esseri umani per mitigare il pregiudizio dell'automazione
      </p>
      </li>
      <li>
      <p align="justify">
Abilitazione di strumenti di apprendimento automatico classici con incorporamenti
      </p>
      </li>
      <li>
      <p align="justify">
Modalità di presentazione degli LLM reciprocamente vantaggiose per aziende e utenti
      </p>
      </li>
    </ul>
  </td>
</table>

<p align="justify">
A questo punto dovresti avere una solida conoscenza degli LLM e delle loro capacità. Producono testo molto simile al testo umano perché sono stati formati su centinaia di milioni di documenti di testo umano. Il contenuto che producono è prezioso, ma anche soggetto a errori. E, come sai, puoi mitigare questi errori incorporando conoscenze di settore o strumenti come i parser per il codice sorgente del computer.
</p>

<p align="justify">
Ora siete pronti a progettare una soluzione utilizzando un LLM. Come si fa a considerare tutto ciò di cui abbiamo parlato finora e a trasformarlo in un piano di implementazione efficace? Questo capitolo vi guiderà attraverso il processo, i compromessi e le considerazioni nella progettazione di tale piano. Per farlo, useremo un esempio concreto che tutti possiamo comprendere: contattare il supporto tecnico quando è necessario aiuto.
</p>

<p align="justify">
Innanzitutto, considereremo la strada più ovvia: costruire un chatbot. I chatbot sono il veicolo che ha introdotto molte persone agli LLM perché, in generale, possono svolgere un ottimo lavoro nel generare output in modo interattivo. Valuteremo i rischi dell'implementazione di un chatbot basato su LLM in uno scenario di assistenza clienti. Attraverso questa discussione, scoprirete che l'utilizzo di un LLM può aumentare il rischio rispetto ad altre opzioni. Tuttavia, un semplice chatbot può essere un'opzione valida se i rischi sono sufficientemente minimi.
</p>

<p align="justify">
Successivamente, esploreremo i modi per gestire i rischi utilizzando progetti applicativi che migliorino il modo in cui i clienti interagiscono con l'LLM. Discuteremo di come affidare a una persona il controllo di ogni output prodotto da un LLM sia irto di problemi a causa di un fenomeno noto come bias di automazione. Discuteremo di come il bias di automazione possa essere evitato, in modo un po' controintuitivo, affidando la supervisione dell'LLM alla persona. Esploreremo come gli embedding di un LLM, la rappresentazione semantica del testo codificato come numeri, possano essere combinati con algoritmi di apprendimento automatico classici per affrontare questo rischio e gestire attività che un LLM non può svolgere in modo indipendente.
</p>

<p align="justify">
Infine, analizzeremo il modo in cui la tecnologia viene presentata agli utenti e il suo ruolo fondamentale nel creare fiducia e trasmettere una comprensione del suo funzionamento interno. Discuteremo l'ambito dell'"intelligenza artificiale spiegabile", in cui un algoritmo di apprendimento automatico produce un output che descrive o spiega come è arrivato a un output specifico. L'intelligenza artificiale spiegabile è spesso l'approccio adottato per gestire situazioni in cui le persone hanno bisogno di capire come funziona un LLM, ma gli studi dimostrano che, sebbene la spiegabilità possa far luce sul funzionamento interno degli LLM descrivendo il comportamento di questi modelli in termini umani, non tende a essere di per sé utile. Descriveremo invece i vantaggi di concentrarsi sulla trasparenza, sull'allineamento degli incentivi con i clienti e sulla creazione di cicli di feedback per progettare soluzioni che soddisfino meglio le esigenze sia delle aziende che le utilizzano sia dei clienti che interagiscono con esse, fornendo output accurati e creando efficienze nei processi aziendali.
</p>

<h3>8.1 Creare semplicemente un chatbot?</h3>

<p align="justify">
Non sorprende che molte persone stiano sviluppando chatbot utilizzando LLM basati su architetture di tipo transformer, la stessa tecnologia alla base di ChatGPT. È un primo passo ovvio e apparentemente ragionevole. La straordinaria capacità di ChatGPT di interagire con le persone, adattarsi alle conversazioni e recuperare e presentare informazioni dimostra quanto bene la tecnologia LLM supporti le applicazioni di interazione con i clienti. Con l'avvento e la disponibilità degli LLM, sarebbe probabilmente poco lungimirante tentare di implementare un agente del servizio clienti utilizzando qualsiasi altro approccio, come l'utilizzo di un sistema esperto addestrato a utilizzare un albero decisionale di risposte predefinite. Quando un cliente insoddisfatto ha un problema tecnico, invece di cercare un documento di Domande Frequenti (FAQ) online, inviare un'e-mail nel buco nero di un sistema di ticketing o chiamare un numero di telefono con un sistema di risposta vocale interattiva automatizzato, può iniziare a interagire direttamente con uno strumento basato sull'intelligenza artificiale e fare progressi nella risoluzione dei problemi. Sembra fantastico sulla carta, e se si disegna un piccolo diagramma come quello della figura 8.1 , sembra proprio che stiamo semplificando la vita.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 8.1 Osservando il diagramma di processo, sembrerebbe che la sostituzione di FAQ, ticket via email e numeri di supporto possa essere semplificata e snella con un chatbot basato su LLM. Tuttavia, l'assurdità di questa visione è che il processo è incompleto. I potenziali errori e i processi di correzione necessari per garantire il corretto funzionamento di un LLM sono nascosti e creano ulteriore complessità.

      </p>
    </figcaption>

<img width="1100" height="612" alt="CH08_F01_Boozallen" src="https://github.com/user-attachments/assets/aaf97296-013a-4d53-b0f5-cfa01c2b97f1" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Ci sono certamente casi in cui un chatbot è una buona idea. Ma sorprendentemente, un chatbot online basato su LLM che gestisce il supporto probabilmente non è in cima alla lista degli strumenti di supporto clienti per la maggior parte delle aziende, a causa dello sforzo richiesto per costruire un sistema che sia accurato e affidabile in molti casi e che non crei output inaspettati quando confrontato con input inaspettati. In definitiva, la decisione di utilizzare un LLM per implementare un chatbot di supporto clienti si riduce alla nostra continua discussione sugli errori che un LLM potrebbe commettere nel generare risposte ai clienti. Sappiamo che gli LLM non sono esenti da errori e, sebbene l'apprendimento automatico sia talvolta pratico, il costo di questi potenziali errori è il criterio decisionale principale quando si considera l'implementazione di questa tecnologia. Fondamentalmente, l'utilizzo di un LLM aumenta potenzialmente il costo di questi errori. Il punto è che, nella loro forma attuale, gli LLM possono fornire risposte errate e la responsabilità di queste ricade sulle spalle delle aziende o degli individui che li implementano e li gestiscono.
</p>

<p align="justify">
I dirigenti o i product manager potrebbero considerare il costo degli errori nel contesto di alcuni classici indicatori chiave di performance aziendali. Ad esempio, i tassi di fidelizzazione dei clienti potrebbero diminuire se affidassero il supporto ai chatbot. Forse il tasso di fidelizzazione sarebbe più elevato rispetto a quello che si otterrebbe esternalizzando le funzioni di relazione con i clienti a un call center in un altro paese. In effetti, queste considerazioni sono importanti da valutare e probabilmente si dovrebbe effettuare un'implementazione di prova per vedere cosa ne pensano i clienti prima di sostituire la funzione di assistenza clienti con un LLM all'ingrosso.
</p>

<p align="justify">
Nota: consigliamo quasi sempre di effettuare implementazioni di prova di qualsiasi sistema di apprendimento automatico. Il detto degli investitori "Le performance passate non sono garanzia di rendimenti futuri" è valido per qualsiasi intelligenza artificiale. Un modo per farlo è attraverso implementazioni fantasma , in cui si esegue il nuovo sistema di intelligenza artificiale insieme al processo esistente per alcune settimane o mesi. Si può scegliere di ignorarne i risultati mentre i processi aziendali esistenti sono in atto. Questo dà il tempo di osservare le discrepanze tra i processi attuali e quelli nuovi, identificare e risolvere i problemi e determinare se le prestazioni del sistema di apprendimento automatico peggiorano nel tempo.
</p>

<p align="justify">
Ancora più grave, il tuo LLM può fornire consigli che possono danneggiare i tuoi utenti. Poiché un LLM non è una persona che può essere ritenuta legalmente responsabile delle proprie azioni, tu e la tua azienda sarete ritenuti responsabili. Questo è già accaduto con una compagnia aerea che ha implementato un chatbot che forniva dichiarazioni di policy errate. Un tribunale ha stabilito che l'azienda doveva attenersi alla policy generata e condivisa in modo errato dal suo chatbot [1].
</p>

<p align="justify">
Consigliamo di considerare sempre un atteggiamento conflittuale quando si implementa un LLM. Chiedersi "Cosa potrebbe fare un malintenzionato motivato se sapesse come funziona?" aiuterà a identificare e mitigare i rischi significativi ed è spesso il modo migliore per determinare se l'applicazione LLM che si intende applicare è una buona o una cattiva idea. Ad esempio, un'azienda automobilistica ha integrato un LLM nel proprio sito web per aiutare a vendere auto e rispondere alle domande. Dopo averlo capito, gli utenti hanno impiegato meno di un giorno per convincere il sito web a vendere loro un'auto per solo 1 dollaro [2].
</p>

<p align="justify">
Se il costo potenziale o il rischio di errori è basso, puoi tranquillamente implementare un chatbot LLM, se lo desideri. Ma, ai fini di questo capitolo, supponiamo che questo agente di supporto tecnico che stiamo ipotizzando sia molto importante e che gli errori che commette potrebbero costare molto all'azienda. La domanda ora diventa: come possiamo progettare una soluzione che ci offra vantaggi in termini di produttività ed efficienza, limitando al contempo l'accesso diretto degli utenti a un LLM? Se sei alle prime armi con l'intelligenza artificiale e il machine learning e un chatbot è la tua principale esposizione al settore, questo potrebbe sembrare una contraddizione, ma esistono alcuni modelli di progettazione semplici e ripetibili che puoi applicare a questo scopo.
</p>

<h3>8.2 Bias di automazione</h3>

<p align="justify">
Un approccio comune per affrontare il rischio di utilizzare gli LLM per le interazioni dirette con i clienti è quello di farli interagire con il personale di supporto o con i tecnici. Questo approccio viene spesso definito "human in the loop" perché c'è una persona che esamina il feedback tra l'LLM e il cliente, fornendo una valutazione critica dell'output del sistema automatizzato e intervenendo e modificando l'output quando rileva un errore. Il tecnico continuerà a essere impiegato, ma ne aumenteremo l'efficienza facendo in modo che l'LLM generi una risposta iniziale a ogni domanda dell'utente e che un tecnico si occupi di tali risposte per garantirne l'accuratezza e la pertinenza. Se l'LLM genera una risposta potenzialmente costosa o errata, i nostri fidati tecnici interverranno e risponderanno con qualcosa di più appropriato. In questo contesto, spetta in ultima analisi al tecnico scegliere la risposta autorevole più appropriata.
</p>

<p align="justify">
Il lettore più attento che ricorda la nostra discussione sulla generazione aumentata del recupero (RAG) del capitolo 5 potrebbe persino individuare dei modi per migliorare questa idea. Direte: "Ah, possiamo inserire tutti i nostri manuali di formazione e la documentazione in un database, e poi possiamo usare RAG in modo che l'LLM possa recuperare le informazioni più rilevanti per la domanda di un utente". Questo approccio è delineato nella figura 8.2 , che mostra un processo in cui le domande di un utente vengono prima inviate all'LLM per focalizzare la generazione di output utilizzando una raccolta di risposte note.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 8.2 Un approccio ingenuo all'implementazione di un sistema "human in the loop" che utilizza un LLM abbinato a un database di informazioni rilevanti per produrre un output che viene infine rivisto e possibilmente corretto da un lavoratore umano
      </p>
    </figcaption>

<img width="1100" height="666" alt="CH08_F02_Boozallen" src="https://github.com/user-attachments/assets/7ab9db70-2dc1-47a5-8406-66707df1d1dd" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
L'approccio RAG probabilmente mitigherà molti rischi, ma potrebbe anche incorrere nella trappola del bias di automazione . Il bias di automazione si riferisce al fatto che le persone, in generale, tendono a scegliere scelte automatiche o predefinite presentate da un sistema perché è più facile che applicare il pensiero critico per determinare quale scelta sia più appropriata alla situazione specifica. Se un sistema funziona bene e non richiede interventi frequenti, diventa incredibilmente difficile rimanere ipervigili e rilevare errori occasionali. Il paradosso è che se il sistema è così impreciso nei suoi suggerimenti che è possibile mantenere la vigilanza, è probabile che il sistema rallenti rispetto a rispondere direttamente alle domande senza automazione.
</p>

<p align="justify">
È qui che le implementazioni di prova o fantasma diventano incredibilmente importanti. Se il sistema è così accurato che la vera fonte di rischio è il bias dell'automazione, si hanno due opzioni che non richiedono di discostarsi dalla progettazione "human in the loop":
</p>

<ul>
  <li>
    <p align="justify">
    Aggiungere un percorso di "fuga verso un essere umano" alla pipeline
    </p>
  </li>
  <li>
    <p align="justify">
Mitigare il rischio di errori esterni tramite modifiche ai processi
    </p>
  </li>
</ul>

<p align="justify">
Il primo punto è piuttosto semplice. Prima o poi, si verificherà una situazione nuova a cui l'LLM non sarà in grado di rispondere. In questo caso, sarebbe opportuno fornire al cliente un modo per "uscire" da un ciclo infinito con un computer e accedere a un livello di supporto superiore. Potrebbe trattarsi di una durata massima della conversazione misurata in base al numero di messaggi scambiati o al tempo trascorso in chat, di un'opzione per contattare un operatore umano che compare in base a più tentativi falliti di comunicazione, o di altre possibili soluzioni.
</p>

<p align="justify">
Nota : supponiamo che tu voglia creare un dataset RLHF o SFT per adattare il tuo LLM alla tua situazione, come discusso nel capitolo 5. In tal caso, puoi anche aggiungere esempi di training in cui la risposta prevista dell'LLM è "Mi dispiace, questa situazione sembra più complessa di quanto io possa risolvere; permettimi di chiedere aiuto a un essere umano".
</p>

<h3>8.2.1 Modifica del processo</h3>

<p align="justify">
Il secondo suggerimento, cambiare il processo, non è così difficile come potrebbe sembrare. Se uno dei vostri superiori ha un MBA, è (a quanto pare) addestrato a pensare in questi termini. (Uno degli autori ha un MBA, quindi possiamo dirlo tranquillamente.) Ad esempio, le interazioni con il chatbot potrebbero includere un avvertimento su qualsiasi risultato che richieda "l'approvazione finale di un essere umano". In questo caso, far revisionare l'intera conversazione da una persona è molto meno rischioso per l'automazione rispetto al richiedere a qualcuno di mantenere una vigilanza costante durante una conversazione continua. In definitiva, gli utenti avversari sanno che un essere umano controllerà e quindi sono demotivati dal cercare di aggirare il sistema.
</p>

<p align="justify">
A seconda del contesto, è possibile impedire l'uso conflittuale di un LLM richiedendo all'utente di fornire garanzie per garantire la propria buona fede. Ad esempio, si potrebbero adottare misure equivalenti al blocco della carta di credito dell'utente, come una sorta di assicurazione contro interazioni in malafede. Tale blocco verrebbe annullato al completamento della transazione. Si potrebbe anche limitare la parte di processo automatizzata, richiedere l'autenticazione o randomizzare la frequenza con cui le persone vengono indirizzate a un essere umano anziché a un'intelligenza artificiale, in modo da rendere imprevedibile il verificarsi di una situazione che potrebbe essere sfruttata.
</p>

<p align="justify">
Tutte queste azioni dipenderanno dalla tua applicazione specifica, dai rischi, dalla tolleranza a tali rischi e dalla natura dei tuoi utenti. Alcuni clienti potrebbero essere scoraggiati da un blocco del credito e rimanerne irritati. Oppure potresti presentarlo come un metodo opzionale in cui l'utente ottiene uno sconto di 2 dollari sulla bolletta se un sistema di intelligenza artificiale lo ha aiutato con successo a risolvere il suo problema, presumendo che sia inferiore a quanto sarebbe costato per chiamata il vecchio sistema. In ogni caso, la decisione dipenderà dal caso specifico e dalla tua creatività nel gestire il rischio.
</p>

<h3>8.2.2 Quando le cose sono troppo rischiose per gli LLM autonomi</h3>

<p align="justify">
Quindi, dopo aver effettuato una distribuzione di prova, valutato i rischi e le propensioni avverse dei vostri utenti, avete concluso che è troppo rischioso per gli LLM fornire le risposte iniziali. Come potrebbe un LLM garantire comunque un certo livello di efficienza?
</p>

<p align="justify">
Un approccio poco intuitivo consiste nel far sì che sia l'LLM a controllare la persona, anziché la persona a controllare l'LLM. Questo può sembrare strano. Perché dovremmo lasciare che l'LLM supervisioni se non possiamo fidarci che agisca da solo? Per approfondire questo aspetto, immaginiamo di avere un sistema LLM che svolga questo ruolo di supervisione, controllando ogni risposta, come mostrato nella figura 8.3 .
</p>

<p align="justify">
Se l'LLM e la persona hanno ragione, verrà intrapresa un'azione e il messaggio verrà inoltrato al cliente. Sarà come se l'utente stesse chattando con il tecnico. Tuttavia, se il tecnico e l'LLM non sono d'accordo sulla risposta, possiamo chiedere al tecnico di ricontrollare la propria risposta prima di inviarla all'utente.
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 8.3 Si noti che la direzione delle frecce in questo diagramma è cambiata rispetto alla figura 8.2 . Tutto passa prima all'uomo e utilizziamo gli LLM per individuare gli errori prima che si verifichino.
      </p>
    </figcaption>

<img width="1100" height="1095" alt="CH08_F03_Boozallen" src="https://github.com/user-attachments/assets/fcec303e-d1c1-4c8c-b694-b73bc31241cd" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Questo doppio controllo potrebbe essere semplice come dire al tecnico: "Ehi, sembra che questa soluzione non sia adatta; per favore conferma prima di inviare". Potresti provare a far sì che l'LLM produca la propria alternativa suggerita. Oppure potresti escludere l'LLM dal processo e utilizzarlo per avvisare un tecnico più esperto di unirsi al processo e fornire assistenza. Indipendentemente da come sia strutturato, lo scopo è segnalare il rischio di un'interazione negativa con il cliente, ad esempio una risposta errata. Sebbene questo rischio esistesse in precedenza, ora abbiamo la possibilità di mitigarlo.

<p align="justify">
Inoltre, poiché stiamo prendendo in considerazione errori di supporto clienti causati da un essere umano, in genere non ci assumiamo alcun nuovo rischio, perché un rappresentante del supporto che agisce da solo potrebbe facilmente commettere un errore. Quindi, se l'LLM e l'essere umano sbagliano entrambi contemporaneamente, eri già destinato a commettere quell'errore di processo in ogni caso. Così è la vita. Tecnicamente, potremmo sostenere che i tecnici potrebbero mettere in discussione eccessivamente le proprie risposte in base alla valutazione delle interazioni da parte di un LLM, riducendo così l'efficienza. Inoltre, un LLM eccessivamente sensibile potrebbe chiedere ai tecnici di ricontrollare il proprio lavoro troppo spesso, il che causerebbe un affaticamento da avvisi che potrebbe portare i tecnici a ignorare completamente i suggerimenti dell'LLM. Se il tuo caso d'uso è soggetto a questo tipo di problemi, questo fatto verrà scoperto durante le implementazioni di prova che forniranno feedback specifici sul contesto su come un LLM dovrebbe essere ottimizzato per affrontare questo problema. L'avvertenza generale che si applica a tutto il machine learning è particolarmente importante in questo caso: testare sempre; non dare per scontato.

<p align="justify">
Utilizzare un LLM per verificare le prestazioni umane può ridurre gli errori nel processo nel suo complesso. Potrebbe sembrare che questo approccio non acceleri i tempi, perché la risposta iniziale è ancora generata dagli esseri umani. Tuttavia, questo approccio crea comunque opportunità per una maggiore efficienza:

<ul>
  <li>
    <p align="justify">
Può ridurre la durata della conversazione aiutando a individuare gli errori e a raggiungere una soluzione più rapidamente.
    </p>
  </li>
  <li>
    <p align="justify">
Può identificare il personale che necessita di maggiore formazione o informazioni per rispondere alle domande dei clienti o riconoscere quando si verificano specifiche situazioni di errore.
    </p>
  </li>
  <li>
    <p align="justify">
Può aiutare a evitare l'escalation verso livelli di supporto o di gestione più costosi, riducendo la frequenza e i costi dei clienti problematici.
    </p>
  </li>
</ul>

<h3>8.3 Utilizzare più di un LLM per ridurre il rischio</h3>

<p align="justify">
Tutto ciò che abbiamo discusso ha implicato un approccio "combattere il fuoco con il fuoco" in cui, sebbene vi siano rischi nell'utilizzo degli LLM, abbiamo valutato diversi modi per mitigarli. Sebbene abbiamo modificato il modo in cui utilizziamo gli LLM, questi rimangono la componente principale. In alternativa, possiamo valutare l'utilizzo di strumenti diversi dagli LLM per affrontare le nostre sfide progettuali. Altri approcci nell'ambito dell'IA generativa, come la sintesi vocale e la sintesi vocale, possono essere utilizzati per creare esperienze utente più accessibili o semplicemente più pratiche. Ad esempio, gli utenti con artrite o ipovedenti potrebbero preferire di gran lunga una telefonata piuttosto che digitare le risposte in una finestra di prompt di un chatbot.
</p>

<p align="justify">
Se pensiamo al nostro problema di assistenza clienti e a quando gli LLM funzionano bene, scopriremo che sono disponibili anche gli ingredienti per una classe più ampia di strumenti. Gli LLM funzionano meglio quando ci sono ripetizioni in scenari in cui i problemi si ripresentano e possono essere fornite soluzioni e risposte formulate. Gli LLM sono molto flessibili nel riconoscere schemi generali nella natura confusa del linguaggio. Se l'LLM riesce a interpretare correttamente il problema di un utente e esiste una soluzione nota, può potenzialmente guidare l'utente attraverso tale soluzione. Questo potrebbe sembrare molto simile a un chatbot non supervisionato, ma la differenza fondamentale è che nei casi in cui l'LLM assume un ruolo subordinato nella soluzione, l'output è stato in ultima analisi generato dai tecnici dell'assistenza clienti, come descritto nella figura 8.3 .
</p>

<p align="justify">
Questa sezione discuterà anche di come possiamo utilizzare tecniche classiche di apprendimento automatico, come la classificazione, per affrontare problemi esistenti. Possiamo farlo sfruttando le conoscenze acquisite negli LLM per abilitare le tecniche di apprendimento automatico producendo incorporamenti del testo dell'utente.
</p>

<h3>8.3.1 Combinazione di incorporamenti LLM con altri strumenti</h3>

<p align="justify">
Nel capitolo 3 , abbiamo descritto come un LLM trasforma i token in embedding, ovvero vettori che codificano una rappresentazione semantica del significato di ciascun token come una serie di numeri. Questi embedding vettoriali sono utili anche in altri modi, al di fuori del contesto dell'architettura del trasformatore dell'LLM. Sebbene gli embedding vettoriali siano essenziali per il funzionamento dell'LLM, sono di per sé uno strumento straordinariamente utile.
</p>

<p align="justify">
La natura semantica dei vettori prodotti dagli LLM è importante perché centinaia di altri algoritmi di apprendimento automatico pratici operano su rappresentazioni vettoriali. Gli LLM sono essenzialmente un modo molto potente per convertire testi complessi in linguaggio umano in una forma compatibile con il resto del campo dell'apprendimento automatico. L'utilizzo degli output vettoriali degli LLM con altri algoritmi si è rivelata una strategia così straordinariamente utile che i professionisti la descrivono come "creazione di incorporamenti". La descrizione deriva dall'idea che l'LLM prenda una rappresentazione (testo umano) e la incorpori in un'altra rappresentazione (un vettore matematico). Poiché questi numeri codificano informazioni sul testo originale, è possibile rappresentarli graficamente come numeri e vedere che testi simili finiscono in posizioni simili sul grafico, come mostrato nella figura 8.4 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 8.4 Gli LLM producono vettori numerici noti come embedding come parte intrinseca del loro funzionamento. L'utilità di questi embedding dipende dal fatto che questi numeri cambiano solo di poco quando viene fornito un testo simile. I due test di esempio qui presenti avranno embedding simili e, pertanto, i loro grafici appaiono simili, anche se non condividono nessuna delle stesse parole. Questa è una potente funzionalità presente nelle vecchie tecniche di apprendimento automatico.
      </p>
    </figcaption>

<img width="1100" height="633" alt="CH08_F04_Boozallen" src="https://github.com/user-attachments/assets/54383d6a-2d2b-4463-acf3-6c84cf227cd4" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
Diamo un'occhiata a una rapida descrizione di quattro tipi di algoritmi di apprendimento automatico che puoi utilizzare una volta che hai gli embedding. Consideriamo ogni tipo di apprendimento automatico particolarmente utile per la maggior parte degli utilizzi reali con gli LLM; menzioneremo anche alcuni algoritmi popolari che puoi trovare, relativamente affidabili e facili da usare. La conclusione fondamentale è che se si abbandona la mentalità che solo un LLM può risolvere un problema, si ha a disposizione un set di strumenti più ampio. Questo elenco è la mappa di partenza per alcuni di questi strumenti:
</p>

<ul>
  <li>
    <p align="justify">
Algoritmi di clustering : raggruppano i testi in base alla loro somiglianza, distinguendoli dalla maggior parte del testo disponibile (ad esempio, utilizzati per l'analisi dei segmenti di mercato). Tra gli algoritmi più diffusi figurano k-means e HDBSCAN.
    </p>
  </li>
  <li>
    <p align="justify">
Rilevamento di valori anomali : individuazione di testi diversi da praticamente tutti gli altri testi disponibili (ad esempio, individuazione di clienti contrari o problemi nuovi). Tra gli algoritmi più diffusi figurano le foreste di isolamento e il fattore di valori anomali locali (Local Outlier Factor, LoF).
    </p>
  </li>
  <li>
    <p align="justify">
Visualizzazione delle informazioni : creazione di un grafico 2D dei dati per consentirne l'ispezione/esplorazione visiva, soprattutto se combinato con strumenti interattivi (ad esempio, esplorazione dei dati). Tra gli algoritmi più diffusi figurano UMAP e PCA.
    </p>
  </li>
  <li>
    <p align="justify">
Classificazione e regressione : se si etichettano i vecchi testi con risultati noti (ad esempio, punteggio del promotore netto), è possibile utilizzare la classificazione (ad esempio, scegliere uno tra A, B o C) o la regressione (ad esempio, prevedere un numero continuo come 3,14 o 42) per prevedere quale sarebbe il punteggio di un nuovo testo (ad esempio, categorizzazione dei dati e previsione del valore). L'utilizzo di embedding come input per algoritmi semplici come la regressione logistica e la regressione lineare funziona bene, rispettivamente, per la classificazione o la regressione.
    </p>
  </li>
</ul>

<p align="justify">
Nota : gli embedding non sono una novità, essendo stati inventati come parte degli LLM. Un algoritmo noto come Word2Vec, in grado di incorporare singole parole, ha reso popolari gli embedding come strategia di riferimento per rappresentare il significato di un testo già nel 2013. Ciononostante, gli LLM tendono a produrre embedding con maggiore utilità rispetto ad altri algoritmi più vecchi. Tuttavia, un LLM è molto più impegnativo dal punto di vista computazionale rispetto ad algoritmi più vecchi come Word2Vec. Per questo motivo, potrebbe essere opportuno utilizzare un algoritmo più vecchio o più veloce per questo compito. L'esistenza di metodi di intelligenza artificiale generativa in immagini, video e parlato significa che è possibile utilizzare gli embedding anche per domini come immagini, video e parlato, oltre che per il testo.
</p>

<h3>8.3.2 Progettazione di una soluzione che utilizza gli embedding</h3>

<p align="justify">
Ora che abbiamo descritto il concetto di embedding e come ci offrono più strumenti, creiamo una soluzione avanzata per il call center di supporto tecnico. Continueremo a utilizzare gli LLM per la loro capacità di generare testo e i loro embedding, e integreremo altre tecniche di apprendimento automatico per abilitare l'interazione vocale a cui le persone sono abituate, ridurre i tempi di attesa e aumentare l'efficienza.
</p>

<p align="justify">
Innanzitutto, per supportare l'interazione vocale, utilizzeremo la conversione da voce a testo per convertire le parole pronunciate da un utente in testo che viene utilizzato come input in un LLM. Sarebbe ragionevole pensare: "Ho già usato sistemi a controllo vocale davvero pessimi", e sì, probabilmente è così. Ecco perché è essenziale aggiungere un meccanismo di "salvataggio" per sfuggire al sistema automatizzato (ad esempio, numero massimo di tentativi, tempi o opt-out) nei casi in cui il sistema non riesca a comprendere il parlato di un utente. Oltre alla conversione da voce a testo, utilizzeremo anche la conversione da testo a voce per fornire al LLM un modo per convertire il testo in uscita in qualcosa che un utente dovrebbe essere in grado di sentire e comprendere.
</p>

<p align="justify">
In secondo luogo, per ridurre i tempi di attesa, possiamo implementare un sistema in cui, se si è formata una coda di chiamate a causa del numero di richieste di supporto in arrivo, chiederemo al cliente di descrivere il suo problema in modo che possa essere indirizzato all'analista più appropriato. Partendo dal presupposto che i clienti possano avere nuovi problemi, non tentiamo di utilizzare l'LLM per risolverli direttamente. Invece, utilizzeremo la descrizione del problema del cliente per chiamare l'API di incorporamento dell'LLM e produrre una rappresentazione del problema. Una volta incorporata la descrizione del problema, possiamo utilizzare il clustering per raggruppare gli utenti nella coda. Gli utenti con problemi simili possono essere assegnati allo stesso team di analisti per aiutare gli analisti a risolvere i problemi più velocemente. Questo di per sé è un vantaggio.
</p>

<p align="justify">
Possiamo utilizzare questo raggruppamento dei problemi per aumentare ulteriormente l'efficienza. Supponiamo che un analista abbia identificato un problema comune per il quale esiste una soluzione coerente e predefinita. Invece di affidarsi all'LLM per generare dinamicamente una soluzione ipotetica, l'analista umano può condividere la soluzione predefinita che è già stata verificata da utenti reali. Inoltre, è possibile inviare tale soluzione agli utenti in attesa in coda tramite l'LLM. Sarà possibile informare gli utenti: "È stata sviluppata una soluzione automatizzata che riteniamo possa risolvere il problema. Mentre aspettate, proviamo a risolverlo con la nostra IA automatizzata". Questo approccio è riassunto nella figura 8.5 .
</p>

<table align="center">
<td>
<div align="center">
  <figure>
    <figcaption>
      <p align="justify">
Figura 8.5 Questo diagramma descrive la nostra "soluzione migliore" per le richieste di assistenza clienti, in cui i clienti descrivono il loro problema mentre aspettano di parlare con qualcuno. L'LLM utilizza una rappresentazione incorporata del problema per confrontare problemi simili con soluzioni note. Mentre l'utente attende, un sistema automatizzato può fornire informazioni che potrebbero aiutarlo a risolvere il problema senza l'intervento del personale di supporto. Se questo non funziona, c'è sempre la possibilità di "tirarsi indietro" e parlare con una persona reale. Il modello utilizzato per generare gli incorporamenti non deve necessariamente essere lo stesso dell'LLM che guida l'utente attraverso la soluzione.
      </p>
    </figcaption>

<img width="1100" height="488" alt="CH08_F05_Boozallen" src="https://github.com/user-attachments/assets/df94a3dc-1d8d-4be8-9bd4-8951f4f3d242" />

  </figure>
</div>
  </td>
</table>

<p align="justify">
È possibile combinare le soluzioni descritte finora. Ad esempio, il ciclo di interazione analista-cliente in alto a destra nella figura 8.5 potrebbe prevedere due persone che discutono del problema, oppure potrebbe essere la soluzione di convalida supervisionata da LLM che abbiamo progettato nella figura 8.3 . A seconda dei problemi da risolvere, ci sono molte opportunità per estendere queste soluzioni ora che disponiamo degli embedding. Ad esempio, se gli analisti salvassero informazioni su quanto sia arrabbiato o turbato un cliente, si potrebbe addestrare un modello di regressione per prevedere quanto arrabbiato un cliente potrebbe essere in base al loro embedding. Quindi, si potrebbero distribuire equamente i clienti arrabbiati tra gli analisti per evitare che qualcuno si senta sopraffatto o cercare di indirizzare i clienti arrabbiati lontano dai nuovi analisti che stanno ancora imparando come aiutare i clienti a risolvere i loro problemi.
</p>

<p align="justify">
Per essere chiari, non stiamo dicendo che tutti i sistemi di supporto tecnico al cliente saranno migliori se adottassero questo approccio. L'obiettivo è mostrarvi che esistono modi per costruire soluzioni con gli LLM che ne aggirino i limiti, come la tendenza ad avere allucinazioni e l'incapacità di incorporare nuove conoscenze in modo dinamico. In sintesi, presentiamo due strategie di base:
</p>

<ul>
  <li>
    <p align="justify">
Utilizzate gli LLM come un secondo sguardo su ciò che sta accadendo. Se l'LLM concorda, tutto va bene. In caso contrario, eseguite un doppio controllo che può essere semplice o complesso, a seconda della natura del problema.
    </p>
  </li>
  <li>
    <p align="justify">
Utilizzare gli embedding per applicare il machine learning classico al problema. Il clustering (raggruppamento di elementi simili) e l'individuazione di outlier (individuazione di elementi unici o insoliti) saranno particolarmente utili per molte applicazioni del mondo reale.
    </p>
  </li>
</ul>

<p align="justify">
Non ci affidiamo esclusivamente all'LLM per generare output in qualsiasi fase di queste soluzioni, perché gli LLM possono generare output errati o inappropriati. Tuttavia, possiamo comunque utilizzare gli LLM per ridurre il carico di lavoro, gli errori e i tempi di risoluzione prestando attenzione a come progettiamo il sistema nel suo complesso.
</p>

<h3>8.4 La presentazione della tecnologia è importante</h3>

<p align="justify">
Alcuni di voi potrebbero rimanere increduli dopo aver letto questo esempio di come progetteremmo un sistema di supporto tecnico che utilizza gli LLM. Spesso sentiamo persone che credono fermamente nella tecnologia LLM dire: "Se si fa spiegare il ragionamento all'LLM, l'utente o l'analista possono capire se ha senso e tutti i problemi relativi ad allucinazioni ed errori saranno risolti". Riceviamo spesso richieste simili di creare una "IA spiegabile" da parte di coloro che si trovano all'estremità più scettica dello spettro, preoccupati per gli errori prodotti dagli LLM e che non capiscono cosa stia succedendo. Pertanto, c'è la percezione da entrambe le parti che le spiegazioni forniranno i mezzi per creare fiducia nella tecnologia e credere che l'LLM (o qualsiasi algoritmo di apprendimento automatico) funzioni correttamente ed efficacemente.
</p>

<p align="justify">
In questa sezione, vogliamo discutere alcuni punti che supportano l'idea che la spiegabilità non sia la soluzione a questi problemi. La spiegabilità non è l'unica soluzione che aiuterà a individuare gli errori o a rendere un sistema più trasparente e affidabile. La triste verità è che le nostre ipotesi su come un LLM funzionerà con le persone sono spesso errate e devono essere attentamente valutate. Infatti, recenti ricerche hanno dimostrato che quando un sistema impiega tecniche di intelligenza artificiale spiegabili, le persone si fidano erroneamente della correttezza dell'intelligenza artificiale basandosi esclusivamente sul fatto che sia presente una spiegazione, indipendentemente dalla sua accuratezza. Questo è vero anche quando l'utente potrebbe svolgere il compito in modo indipendente senza il supporto di un'intelligenza artificiale e gli è stato spiegato come funzionano effettivamente i sistemi di intelligenza artificiale [3]. In conclusione, le spiegazioni possono essere dannose per gli stessi obiettivi che cercano di raggiungere.
</p>

<table>
<td>
<h3>Perché utilizzare l'intelligenza artificiale spiegabile?</h3>
<p align="justify">
Nella nostra esperienza professionale, molte richieste di IA spiegabile provengono da paura o ansia. Idealmente, l'IA spiegabile non sarebbe la soluzione per placare tali timori, perché sarebbe controproducente per il raggiungimento degli obiettivi reali. Quindi, perché mai qualcuno dovrebbe sviluppare un'IA spiegabile di qualsiasi tipo?
</p>

<p align="justify">
Due aspetti fondamentali rendono l'intelligenza artificiale spiegabile utile da un punto di vista pratico:
</p>

<ul>
<li>
  <p align="justify">
Rispondendo alla domanda, spiegabile a chi ?

  </p>
</li>
<li>
  <p align="justify">
Raggiungere un'intelligenza artificiale spiegabile partendo dalla definizione del problema

  </p>
</li>
</ul>

<p align="justify">
Ad esempio, un problema reale potrebbe descrivere la necessità di sviluppare una comprensione scientifica di un processo fisico o chimico. Con questo obiettivo, una spiegazione utile dell'algoritmo potrebbe essere quella di generare un'equazione che produca le risposte, anziché produrle direttamente. Con l'equazione, un fisico o un chimico può verificarne la coerenza logica e utilizzarla come punto di partenza per ulteriori esplorazioni scientifiche.
</p>

<p align="justify">
In questo caso, la soluzione è spiegabile solo a qualcuno con una competenza significativa, ma è l'unica persona che ha bisogno della spiegazione. La spiegazione sotto forma di equazione affronta anche direttamente il problema della comprensione scientifica, piuttosto che limitarsi a comprendere il funzionamento interno dell'algoritmo dell'IA. Non abbiamo alcuna spiegazione su come l'IA abbia elaborato l'equazione stessa, e l'equazione è (si spera) una forma logicamente coerente che spiega il processo fisico o chimico.
</p>

<p align="justify">
Questo esempio riflette la situazione generale in cui troviamo l'intelligenza artificiale spiegabile più utile: quando viene utilizzata per aiutare un pubblico ristretto e specifico di utenti potenzialmente esperti a raggiungere un obiettivo molto specifico. Ad esempio, è comune per i data scientist utilizzare l'intelligenza artificiale spiegabile per capire perché un particolare modello commette un particolare insieme di errori, anche se gli strumenti utilizzati non sono comprensibili a un pubblico di non data scientist.
</p>
</td>
</table>

<p align="justify">
Quindi, se l'intelligenza artificiale spiegabile non è una soluzione per costruire la fiducia in un sistema o in una soluzione di intelligenza artificiale, qual è? Sfortunatamente, non esiste un metodo generico e rigorosamente valutato per costruire la fiducia nell'intelligenza artificiale. Il nostro suggerimento, non originale, è di concentrarsi sulla trasparenza, sulla valutazione dell'utente e sulle specificità dei casi d'uso coinvolti.
</p>

<h3>8.4.1 Come puoi essere trasparente?</h3>

<p align="justify">
La trasparenza può essere semplice come informare gli utenti sul sistema di intelligenza artificiale utilizzato: con quale modello è stato progettato e, in generale, come è stato modificato? Se il sistema è concepito per imitare una persona specifica ("Fatti istruire da Albert Einstein, l'intelligenza artificiale") o un tipo di persona qualificata ("Chiedi al Dott. GPT di quel neo sulla tua schiena"), quella persona o una persona con credenziali simili ha acconsentito o ne ha approvato l'efficacia? Come può il consumatore verificare queste informazioni?
</p>

<p align="justify">
In sostanza, elencare questo tipo di domande ragionevoli e le relative risposte che un revisore o un utente scettico potrebbero voler conoscere vi metterà molto più avanti rispetto alla media nel rendere il vostro sistema più trasparente. Non è necessario che queste informazioni siano presentate in dettaglio a ogni utente, ma avere un modo per consentirgli di accedervi è utile. Non solo aiuta gli utenti più esperti a comprendere cosa sta succedendo, ma aiuta anche a definire le aspettative degli utenti in generale su ciò che è e non è possibile con un determinato sistema. Inoltre, è essenziale informare gli utenti quando interagiscono con un sistema che genera risposte automatiche. C'è una grande differenza tra cercare di fingere che un essere umano abbia il controllo e quindi sia in grado di risolvere qualsiasi sfida ragionevole e un'IA automatizzata che si informa il cliente di avere capacità limitate.
</p>

<h3>8.4.2 Allineare gli incentivi agli utenti</h3>

<p align="justify">
Parte della trasparenza e della presentazione del sistema implica l'allineamento degli incentivi coinvolti. Questa non è solo una frase rassicurante sulle pratiche di gestione, ma un consiglio pratico. Ricordate dal capitolo 4 che gli algoritmi di intelligenza artificiale sono macchine avide che ottimizzano per ciò che chiedete, non per ciò che intendete. Se iniziate a costruire un sistema LLM in cui gli incentivi del sistema non sono ben allineati con i vostri obiettivi più ampi, rischiate di sovra-adattarvi a ciò che avete chiesto, non a ciò di cui avete bisogno sia voi che i vostri utenti.
</p>

<p align="justify">
Con incentivi allineati (ad esempio, il nostro esempio "prova l'LLM e ottieni uno sconto di 2 dollari sulla tua fattura se ha funzionato"), hai molte più probabilità di ottenere un risultato positivo. Ti offrono anche più modi per pubblicizzare l'utilizzo di un LLM come meccanismo per offrire valore ai tuoi clienti, invece di apparire come persone malvagie che cercano di esternalizzare tutti i lavori. Presentare e discutere gli incentivi allineati tra un'azienda e i suoi clienti e come stai utilizzando gli LLM per raggiungere tali obiettivi descrive ciò che deve essere detto senza bisogno di nascondere le informazioni.
</p>

<h3>8.4.3 Incorporazione di cicli di feedback</h3>

<p align="justify">
Il mondo non è un luogo statico. Le cose cambiano e ciò che funziona oggi potrebbe non funzionare domani. Questo è uno dei motivi per cui è necessario sottoporre qualsiasi sistema di intelligenza artificiale/apprendimento automatico a un audit regolare e continuo: perché non migliorano né si adattano in modo indipendente con l'esperienza.
</p>

<p align="justify">
Ma ti aiuterà anche a individuare potenziali cicli di feedback negativi, un aspetto a cui dovresti cercare di pensare in anticipo. I cicli di feedback negativi non sono sempre prevedibili. Per aiutarti a individuarli, prova a pensare a quali utenti trarranno o meno i maggiori benefici da un nuovo sistema e cosa succede quando questo si ripete più e più volte.
</p>

<p align="justify">
Ad esempio, abbiamo accennato al fatto che la sintesi vocale e la conversione da testo a voce possono essere utili per i clienti più anziani o con problemi di udito o di movimento. Se non includessimo tale opzione, col tempo rischieremmo di alienare questi clienti, perché ogni volta che hanno un problema, devono utilizzare un sistema fisicamente difficile.
</p>

<p align="justify">
Immagina di essere un'azienda di telefonia mobile che fa affidamento sui piani famiglia per una parte del suo fatturato. I tuoi clienti di mezza età che hanno acquistato i tuoi piani famiglia per primi sono frustrati dal tuo sistema di supporto, quindi trasferiscono l'intero piano famiglia a un nuovo fornitore che si impegna ulteriormente per garantire un processo di assistenza clienti accurato ed efficiente. Ora stai perdendo contemporaneamente sia i tuoi clienti più anziani che quelli più giovani!
</p>

<p align="justify">
Il punto è riflettere attentamente e allenarsi a fare questi esperimenti mentali. Non si riuscirà a individuare ogni caso, ma si migliorerà. Audit e test regolari aiutano quindi a individuare i casi di fallimento, a documentarli e a migliorare il modo di pensare alle situazioni future e ai problemi ricorrenti.
</p>

<h3>Riepilogo</h3>

<ul>
  <li>
    <p align="justify">
Gli LLM possono presentare errori, e per prima cosa è necessario determinarne il rischio e il costo potenziale per progettare una soluzione appropriata. Se il rischio e il costo degli errori sono bassi, è possibile utilizzare un normale LLM in stile chatbot.
    </p>
  </li>
  <li>
    <p align="justify">
È possibile controllare il rischio derivante dall'utilizzo di un LLM modificando il modo in cui gli utenti interagiscono con il sistema o spostando l'automazione su una parte diversa del processo aziendale.
    </p>
  </li>
  <li>
    <p align="justify">
Includere un “essere umano nel ciclo” per supervisionare un LLM crea un rischio di distorsione nell’automazione, anche quando si utilizzano tecniche come RAG per ridurre il rischio di errori.
    </p>
  </li>
  <li>
    <p align="justify">
Gli LLM possono convertire il testo in incorporamenti, rappresentazioni numeriche in cui frasi simili ricevono valori simili. Ciò consente di utilizzare ulteriori approcci di apprendimento automatico, tra cui tecniche classiche come il clustering e il rilevamento di valori anomali.
    </p>
  </li>
  <li>
    <p align="justify">
Sebbene gli LLM possano spiegare le proprie decisioni, le loro spiegazioni sono spesso inefficaci perché le persone ne diventano dipendenti. Concentratevi invece sulla produzione di spiegazioni che soddisfino un bisogno o un caso d'uso specifico, piuttosto che sul generico "bisogno di spiegare".
    </p>
  </li>
    <li>
    <p align="justify">
Progetta gli incentivi del tuo sistema in modo che siano in linea con quelli dei tuoi utenti. Questo è un buon modo per evitare errori, come ad esempio ottimizzare un LLM in base a ciò che hai richiesto anziché a ciò che intendevi, e un buon modo per comunicare e presentare il tuo LLM agli utenti.
    </p>
  </li>
</ul>
