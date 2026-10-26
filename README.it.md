<div align="center">

# V E K T R A

**Il quadro strumenti della tua BYD, a modo tuo.**

Cruscotto personalizzato per lo schermo dietro il volante dei veicoli BYD DiLink 3.

**VERSIONE 1.8.1** · pubblicata il 26 ottobre 2026 · 43.0 MB

[**Scarica l'applicazione**](https://giino01.github.io/Vektra/Vektra-1.8.1.apk) · [**Pagina del progetto**](https://giino01.github.io/Vektra/)

[Français](README.md) · [English](README.en.md) · **Italiano** · [Deutsch](README.de.md) · [Português](README.pt.md) · [Türkçe](README.tr.md)

</div>

---

## Panoramica

![Il quadro in atmosfera blu](img/combine-normal.png)

Da sinistra a destra: la data, il **tachimetro a lancetta** graduato fino a 220 km/h, il **brano in riproduzione** qualunque sia l'app che lo suona, tre cifre scelte in base alla modalità, la **linea di flusso dell'energia** il cui punto centrale va a destra in rosso quando la batteria si scarica e a sinistra in verde quando si ricarica, poi il **meteo animato** e la **pressione delle quattro gomme** in bar.

![Il quadro in atmosfera rossa, modalità Sport](img/combine-sport.png)

In Sport l'atmosfera diventa rossa, compare un badge `SPORT` e le tre cifre in basso cambiano: potenza, regime motore e posizione dell'acceleratore, al posto dei consumi e della batteria.

> Le immagini di questa pagina sono **disegnate dal codice della versione pubblicata** a ogni pubblicazione, con valori dimostrativi. Non possono quindi mostrare una versione più vecchia di quella proposta qui.

## Otto temi

Il tasto **Tema** scorre otto disposizioni del quadro: Carbonio, Carbonio 3D, Gran Turismo, Flusso di energia, Ossidiana, Rosso Sport, Lumen e Nebulosa. Una pressione passa alla successiva. La scelta viene ricordata e torna all'accensione.

![Lo stesso tema su sfondo chiaro](img/clair-theme-hyperos3d.png)

Ogni tema esiste in scuro e in chiaro. Lo sfondo chiaro riprende il blu-grigio dell'interfaccia BYD, misurato su fotografia, perché l'app vi si fonda invece di esservi appoggiata. L'impostazione **Aspetto** sceglie l'uno, l'altro, o segue il tablet.

## Cosa serve

- Un veicolo **BYD con DiLink 3** (Android 10). Messo a punto su una Seal U DM-i; gli altri modelli DiLink 3 non sono stati verificati.
- Il tablet deve accettare l'**installazione di applicazioni esterne** (sideload).
- Il **debug ADB in rete** attivo sul tablet, porta 5555. VEKTRA vi si collega in locale, sul tablet stesso — nulla esce dal veicolo.
- Una connessione internet sul tablet per il meteo e gli aggiornamenti. Tutto il resto funziona offline.

**Perché l'ADB.** I comandi che liberano lo schermo del quadro sono consentiti solo all'utente `shell` di Android. Un'applicazione normale non può inviarli. VEKTRA passa quindi dall'ADB del tablet, in locale, per ottenere quel diritto.

## Installazione

1. Scarica il file dell'applicazione da questa pagina, sul tablet.
2. Aprilo e accetta l'installazione. Se Android rifiuta, autorizza le «origini sconosciute» per il gestore file usato.
3. Apri VEKTRA. Al primo avvio, la schermata iniziale chiede la lingua.
4. Premi **Continua**. Si apre la schermata principale.
5. Il primo comando inviato farà comparire la richiesta **«Consentire il debug USB?»**. Spunta **Consenti sempre**, poi accetta. Compare una sola volta.

![Schermata iniziale e scelta della lingua](img/accueil-langue.png)

Sono disponibili sei lingue: francese, inglese, italiano, tedesco, portoghese brasiliano e turco.

## Attivare la visualizzazione

1. Nella sezione **Controllo**, premi **Verifica · ADB e diagnostica**. È ciò che attiva l'autorizzazione al debug e conferma che la connessione funziona.
2. Torna su **Quadro** e premi **Mostra sul quadro**.
3. Il quadro originale va in standby, viene creato lo schermo virtuale del quadro, poi VEKTRA vi compare. L'operazione richiede una decina di secondi.
4. L'anteprima al centro del tablet mostra in diretta ciò che è disegnato dietro il volante. Il pulsante **Anteprima** la richiude se preferisci un quadro di stato.

**Per tornare indietro**, premi **Ripristina l'originale**: il quadro BYD riprende il comando. Se non torna, spegni e riaccendi il quadro.

## Le quattro sezioni

| Sezione | A cosa serve |
| --- | --- |
| **Quadro** | L'anteprima in diretta, il pulsante di visualizzazione, la scelta di schermo, modalità e tema. |
| **Controllo** | Il rilevamento completo dei dispositivi individuati, con un pulsante per copiare tutto. |
| **Registro** | Ogni comando inviato e ogni risposta ricevuta. |
| **Impostazioni** | Lingua, aspetto, avvio automatico, accesso musica, aggiornamenti, meteo. |

![Quadro](img/tablette-combine.png)

![Impostazioni](img/tablette-reglages.png)

## Musica

Per mostrare il brano in riproduzione, VEKTRA ha bisogno dell'**accesso alle notifiche**: è la regola di Android per leggere le sessioni audio. Premi la riga **Accesso alle notifiche** e l'app se lo concede da sola tramite ADB, senza cancellare nulla dall'elenco esistente. Una volta concesso, titolo, artista, copertina e avanzamento compaiono, **qualunque app stia suonando** — radio, Bluetooth o un'app installata.

## Avvio e arresto automatici

Quando questa impostazione è attiva, VEKTRA prende il quadro appena l'auto è accesa e lo restituisce appena è spenta. Lo stato del veicolo è letto **direttamente dall'auto**, una volta al secondo: 0 spento, 1 accessori, 2 quadro acceso. Uno spegnimento va confermato due volte di fila prima che lo schermo sia restituito — un singolo singhiozzo non deve far sparire la visualizzazione in marcia.

## Aspetto

Scuro, chiaro o automatico — l'aspetto segue allora quello del tablet. L'impostazione riguarda solo il quadro: lo schermo del tablet resta sempre scuro, è una postazione di guida.

## Aggiornamento

VEKTRA controlla da sola a ogni apertura. Quando una versione è disponibile, una finestra mostra le novità e propone **Più tardi** o **Scarica e installa**. Se accetti, l'app si scarica, si installa sopra e si riapre da sola. Tutte le versioni portano la **stessa firma**: un aggiornamento sostituisce sempre il precedente senza che Android lo rifiuti e senza perdere le impostazioni.

## In caso di problemi

- **Il quadro resta bloccato.** Premi *Ripristina l'originale*, poi riprova. Se non cambia nulla, spegni e riaccendi il quadro.
- **Nessun dato, solo trattini.** L'SDK dell'auto non ha risposto. La sezione Controllo dice quali dispositivi sono raggiungibili.
- **La musica non compare.** L'accesso alle notifiche non è stato concesso: vedi sopra. Verifica anche che qualcosa stia davvero suonando.
- **L'aggiornamento dice «Non disponibile».** Il tablet non ha raggiunto la fonte. Verifica la connessione internet, poi riprova: compare il motivo esatto.
- **Altro.** Apri *Controllo*, premi *Copia tutta la scansione*, poi invia il testo. Contiene tutto il necessario per capire.

## Novità della 1.8.1

- Theme Store: nuova sezione nel menu a sinistra, aperta anche dal tasto «Tema». Carbonio 3D resta il tema integrato predefinito; il tema Aston si scarica con un tocco, con anteprima, dimensione, avanzamento, Applica, Aggiorna e Rimuovi. Ogni tema viene verificato (firma Vektra) prima dell'installazione; un file .vektra ricevuto in altro modo si installa anche con «Importa tema». I prossimi temi arriveranno nello stesso modo.
- Mappa Vektra 3D: una mappa fluida disegnata direttamente dal tablet, con edifici 3D, che segue l'auto in continuo. Ora è la mappa di tutti gli schermi: scheda «Navigazione», widget Navigazione di Carbonio 3D, tema Aston e mappa a tutto quadro; la freccia resta sulla strada percorsa e la linea blu parte dalla freccia (il tratto già percorso scompare). Nuova sezione «Mappa» nelle Impostazioni: stile, edifici 3D e zoom.
- Tema Aston (nel Theme Store): due quadranti, marcia P R N D, spie e al centro musica, meteo o mappa; una navigazione avviata dal tablet appare sul quadro (prossima svolta, distanza, tempo rimanente, ora di arrivo, autovelox reali).
- Navigazione: la guida ora segue l'auto lungo il percorso. La prossima indicazione avanza durante il viaggio, distanza e tempo rimanenti sono misurati sul percorso, ogni manovra viene annunciata e l'arrivo segnalato. Il percorso viene ricalcolato automaticamente quando si esce dal tragitto o lo si percorre contromano, nel senso di marcia dell'auto. La mappa non rallenta più a ogni posizione GPS.
- Nessun valore inventato: senza dati dell'auto gli schermi mostrano «--» invece di velocità, batteria, pressione pneumatici, limite o brano di prova; niente più falsi autovelox aggiunti al percorso o annunciati; la marcia M o S non appare più come «D».
- Importazione di widget e temi: lettura in background (un file grande non blocca più lo schermo), dimensione limitata, immagini ridotte alla dimensione del quadro; formati realmente supportati indicati (immagini, widget Vektra .json, disposizione .json, .zip, .vektra); un widget KWGT, SVG, HTML o XML viene rifiutato con una spiegazione.
- Modifica: un widget nascosto o non importato non intercetta più i tocchi, il grande widget Navigazione non trattiene più la selezione, lo zoom generale non viene più applicato due volte ai bordi della mappa e l'anteprima del tablet non ha più un buco al posto della mappa.
- Interfaccia: tutte le finestre (voce, lingua della voce, importazione, variabili, fonte degli aggiornamenti, donazione) e tutti i messaggi hanno lo stile dell'app; la tastiera si apre sul campo indirizzo.
- Visualizzazione sul quadro: la visualizzazione completa di VEKTRA torna da sola sul quadro quando l'avvio automatico riavvia l'app (poteva restare spenta) e la mappa non scompare più dopo un riavvio; VektraUI ora appare in modo pulito, senza elementi di Carbonio 3D sopra.

---

Progetto personale, senza alcun legame con BYD. Installazione e uso a tuo rischio. Le informazioni mostrate provengono dal sistema dell'auto e possono essere inesatte: non affidarti mai a esse per guidare.
