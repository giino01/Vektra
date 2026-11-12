<div align="center">

# V E K T R A

**Il quadro strumenti della tua BYD, a modo tuo.**

Cruscotto personalizzato per lo schermo dietro il volante dei veicoli BYD DiLink 3.

**VERSIONE 2.6.0** · pubblicata il 12 novembre 2026 · 75.6 MB

[**Scarica l'applicazione**](https://giino01.github.io/Vektra/Vektra-2.6.0.apk) · [**Pagina del progetto**](https://giino01.github.io/Vektra/)

[Français](README.md) · [English](README.en.md) · **Italiano** · [Deutsch](README.de.md) · [Português](README.pt.md) · [Türkçe](README.tr.md)

</div>

---

## Panoramica

![Il quadro in atmosfera blu](img/combine-normal.png)

Da sinistra a destra: la data, il **tachimetro a lancetta** graduato fino a 220 km/h, il **brano in riproduzione** qualunque sia l'app che lo suona, tre cifre scelte in base alla modalità, la **linea di flusso dell'energia** il cui punto centrale va a destra in rosso quando la batteria si scarica e a sinistra in verde quando si ricarica, poi il **meteo animato** e la **pressione delle quattro gomme** in bar.

![Il quadro in atmosfera rossa, modalità Sport](img/combine-sport.png)

In Sport l'atmosfera diventa rossa, compare un badge `SPORT` e le tre cifre in basso cambiano: potenza, regime motore e posizione dell'acceleratore, al posto dei consumi e della batteria.

> Le immagini di questa pagina sono **disegnate dal codice della versione pubblicata** a ogni pubblicazione, con valori dimostrativi. Non possono quindi mostrare una versione più vecchia di quella proposta qui.

## I temi

Il tasto **Tema** apre il **Theme Store** e scorre i temi installati. **Carbone 3D** è il tema integrato predefinito e **VektraUI** l'altro tema integrato; il tema **Aston** si scarica con un tocco. La scelta viene ricordata e torna all'accensione.

![Lo stesso tema su sfondo chiaro](img/clair-theme-vektraui.png)

Ogni tema esiste in scuro e in chiaro. Lo sfondo chiaro riprende il blu-grigio dell'interfaccia BYD, misurato su fotografia, perché l'app vi si fonda invece di esservi appoggiata. L'impostazione **Aspetto** sceglie l'uno, l'altro, o segue il tablet.

## Cosa serve

- Un veicolo **BYD con DiLink 3.0 (13.1.32 e 13.1.33), DiLink 4.0 o DiLink 5.0 / 5.1**, riconosciuto automaticamente.
- Il tablet deve accettare l'**installazione di applicazioni esterne** (sideload).
- Il **debug ADB in rete** attivo sul tablet, porta 5555. VEKTRA vi si collega in locale, sul tablet stesso — nulla esce dal veicolo.
- Una connessione internet sul tablet per il meteo e gli aggiornamenti. Tutto il resto funziona offline.

**Perché l'ADB.** I comandi che liberano lo schermo del quadro sono consentiti solo all'utente `shell` di Android. Un'applicazione normale non può inviarli. VEKTRA passa quindi dall'ADB del tablet, in locale, per ottenere quel diritto.

## Installazione

1. Scarica il file dell'applicazione da questa pagina, sul tablet.
2. Aprilo e accetta l'installazione. Se Android rifiuta, autorizza le «origini sconosciute» per il gestore file usato.
3. Apri VEKTRA. Al primo avvio, la schermata iniziale chiede la lingua, poi il modello della tua auto.
4. Scegli la lingua e poi il modello, premendo **Continua** a ogni passo. Si apre la schermata principale.
5. Il primo comando inviato farà comparire la richiesta **«Consentire il debug USB?»**. Spunta **Consenti sempre**, poi accetta. Compare una sola volta.

![Schermata iniziale e scelta della lingua](img/accueil-langue.png)

Sono disponibili dieci lingue: francese, inglese, olandese, tedesco, spagnolo, italiano, portoghese brasiliano, arabo, turco e cinese.

## Attivare la visualizzazione

1. Nella sezione **Controllo**, premi **Verifica · ADB e diagnostica**. È ciò che attiva l'autorizzazione al debug e conferma che la connessione funziona.
2. Torna su **Quadro** e premi **Mostra sul quadro**. Prima, spunta una modalità di visualizzazione: **Tema a schermo intero** o **App a schermo intero** (e **Schermo piccolo** sulla Sealion 7). Senza modalità spuntata la proiezione non parte, nemmeno all'avvio dell'auto.
3. Il quadro originale va in standby, viene creato lo schermo virtuale del quadro, poi VEKTRA vi compare. L'operazione richiede una decina di secondi.
4. L'anteprima al centro del tablet mostra in diretta ciò che è disegnato dietro il volante. Il pulsante **Anteprima** la richiude se preferisci un quadro di stato.

**Per tornare indietro**, premi **Ripristina l'originale**: il quadro BYD riprende il comando. Se non torna, spegni e riaccendi il quadro.

## La barra di sinistra

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

## Novità della 2.6.0

- Da sapere: dopo l'aggiornamento nessuna modalità di visualizzazione è selezionata. Vai nella scheda Quadro e seleziona la tua prima di avviare la proiezione.
- Da sapere: la prima volta che chiami «Vektra», l'app scarica una sola volta circa 40 MB per riconoscere la tua lingua.
- Aggiunta: 11 nuovi temi nel Theme Store: Chassis, Orbit, Sport, Mappa, Orizzonte, Aurora, Cronografo, Energia, Cielo, Carbone 3D+ e VektraUI+.
- Aggiunta: Carbone 3D+, quadranti 3D sotto vetro, e VektraUI+, archi al neon.
- Aggiunta: temi animati: la strada di Orizzonte scorre con la tua velocità, Aurora ed Energia si muovono, Cielo mostra il meteo reale.
- Aggiunta: Mappa, Carbone 3D+ e VektraUI+ mostrano la tua app (Waze, Google Maps…) o Navigation Vektra al centro del quadro.
- Aggiunta: Modifica: sposta, ingrandisci o nascondi ogni blocco di un tema, poi salva.
- Aggiunta: lo sfondo dei temi si raccorda al quadro, sia chiaro sia scuro.
- Aggiunta: modalità App a schermo intero: sul quadro viene mostrata solo la tua app, da spostare e ridimensionare in Modifica.
- Aggiunta: Anteprima › Interaction App: regola la dimensione dell'app e del suo testo, e la dimensione della mappa Vektra. Cambia solo il quadro, mai il tablet.
- Aggiunta: nuovi comandi dell'auto, anche a voce: finestrini (anche in %), tetto apribile, tendina, bagagliaio, chiusura, memoria sedile 1/2/3, clima per zona, ventilazione, sedili e volante riscaldati, luci, luci ambiente, caricatore wireless, modalità di guida, rigenerazione, specchietti, luci di emergenza, limite di carica e ricarica programmata.
- Aggiunta: Copilota: avviso quando la batteria 12 V è scarica.
- Aggiunta: temi Classico e Blade: CARBURANTE (ibride DM-i), BATTERIA e ABITACOLO in basso a sinistra.
- Aggiunta: nulla di ciò che dici viene inviato su internet prima della parola «Vektra».
- Aggiunta (SEALION7): due profili di visualizzazione: Schermo intero (VEKTRA sotto la fascia superiore dell'auto) o Schermo piccolo (la tua app nella finestra a destra).
- Aggiunta (SEALION7): una versione Sealion 7 di ogni tema.
- Aggiunta (SEALION7): dati dell'auto: velocità, P/R/N/D, batteria, autonomia, chilometraggio, batteria 12 V, ricarica, pneumatici e potenza.
- Aggiunta (SEALION7): visualizzazione forzata: VEKTRA passa davanti alla navigazione originale del quadro.
- Correzione (SEALION7): velocità e lancetta fluide, senza ritardo.
- Correzione (SEALION7): la marcia P/R/N/D è corretta e l'apertura di porte e bagagliaio in D è di nuovo bloccata.
- Correzione (SEALION7): la temperatura esterna non resta più bloccata a 0 °C.
- Correzione: Vektra risponde subito, anche con la musica in riproduzione.
- Correzione: memoria sedile: il sedile arriva fino alla sua posizione senza fermarsi a metà.
- Correzione: ABITACOLO mostra la vera temperatura dell'abitacolo, non quella impostata sul clima.
- Correzione: app proiettata: tutte le sue finestre vanno sul quadro e Chiudi la arresta completamente.
- Correzione: proiezione delle app più fluida.
- Correzione: niente più voce robotica all'avvio.
- Correzione: il meteo compare subito all'avvio, senza città predefinita.

---

Progetto personale, senza alcun legame con BYD. Installazione e uso a tuo rischio. Le informazioni mostrate provengono dal sistema dell'auto e possono essere inesatte: non affidarti mai a esse per guidare.
