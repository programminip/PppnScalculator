# This Python file uses the following encoding: utf-8
messaggio_predefinito ='''Grazie per aver scaricato la Calcolatrice Peppinica.
Cosa c'è di più in Calcolatrice Peppinica rispetto alle migliaia di calcolatrici nel mondo?
Calcolatrice Peppinica offre due modalità di utilizzo:

1) Inserisci numeri separati da uno spazio nella barra in alto poi premi "Go".
Calcolatrice Peppinica eseguirà i calcoli più comuni con i numeri che le hai fornito.
I calcoli eseguiti cambieranno a seconda della quantità di numeri o dei modificatori.
Per esempio per calcolare una proporzione hai bisogno di tre dati quindi queste verranno calcolate solo quando inserirai 3 valori.
Oltre numeri interi e con la virgola puoi inserire frazioni e numeri complessi (per questi usa la j e non la i, per esempio 15-23j) inoltre puoi inserire numeri periodici indicando dopo un carattere di underscore quante sono le cifre del periodo (ad esempio puoi scrivere il numero 11,345656565656 come 11.3456_2).
I numeri periodici verranno trasformati in frazioni mentre per gli altri numeri potrai scegliere se vuoi che si trasformino da un tipo all'altro mediante le spunte sulle opzioni interi/float/frazioni.
Oltre ai numeri puoi inserire degli appositi comandi che modificheranno il comportamento della calcolatrice.
Inserisci "modificatori" e premi "?" per avere la loro lista. Inserisci un modificatore e premi "?" per sapere più dettagliatamente che cosa fa.

2) Usa Calcolatrice Peppinica come una comune calcolatrice con il tastierino numerico.
Questa modalità non implementa una logica per svolgere i calcoli richiesti ma, in modo molto paraculo sfrutta la funzione eval() di Python per eseguire il calcolo.
Questo comporta che potrai eseguire qualsiasi operazione come se fossi in un terminale di Python, Calcolatrice Peppinica importa varie librerie, per esempio math dunque se le conosci potrai richiamare le loro funzioni. Ad esempio per calcolare il seno di un angolo di 90° potrai scrivere math.sin(math.pi/2) e poi premere il tasto "=".
A proposito di pi greco, c'è una barra che contiene varie costanti, cliccandole puoi riportarle nella barra in alto.
Calcolatrice Peppinica riporta tutti i calcoli che hai fatto ed i loro risultati nel riquadro centrale. Inoltre ogni risultato viene memorizzato nel caso tu lo voglia riutilizzare.
Ci sono 4 tasti per cancellare:
    La "C" in alto cancella TUTTO, compresa la memoria;
    Il tastino "Svuota memoria" cancella solo la memoria;
    "CE" cancella l'ultimo carattere inserito;
    "C" cancella il contenuto della barra di inserimento. Se questa è già vuota cancella il riquadro dei risultati.


Calcolatrice Peppinica può essere utilizzato come convertitore personalizzato. Inserisci un fattore di conversione e questo verrà memorizzato in un file per usi futuri.
Se adesempio nella barra sottostante inserirai che 1 metro = 0.001 chilometro da quel momento potrai convertire da metri in chilometri e viceversa.
Per il fattore di conversione puoi anche usare valori calcolandoli, considerando l'esempio precedente puoi scrivere 1/1000 al posto di 0.001 .
Per effettuare le conversioni utilizza poi il modificatore "converti".'''

modificatori ='''potenza\t(per potenze e radici)
potenza_mk2\t(calcola radici mostrando tutti i risultati complessi)
media\t(per medie dei numeri inseriti (int e float)
converti\t(per conversioni - converti(um1,um2) )'''
potenza ='''Questo modificatore usa l'ultimo numero inserito come esponente e lo usa per calcolare le potenze con tutti gli altri numeri.\nRicorda che puoi usarlo per calcolare le radici usando come esponente l'inverso.\nPer esempio la radice cubica di 9 puoi calcolarla elevando 9 ad 1/3'''
potenza_mk2='''Il modificatore in questione calcola i risultati complessi (tutti) di una singola radice.\nPer funzionare usalo con due frazioni, la prima è il radicando e la seconda l'inverso dell'indice.\nPurtroppo al momento Calcolatrice Peppinica non è in grado di calcolare tutti i risultati di una radice con radicando complesso (perché sinceramente non ci capisco un cazzo, e comunque accontentati, non lo fanno nemmeno le calcolatrici di Google e di Microsoft).\n\nAttenzione, Calcolatrice Peppinica indicherà fra i risultati ottenuti quelli che appartengono ai numeri reali, per farlo viene fatta un'approssimazione di 10 alla -15 quindi potrebbe potenzialmente essere sbagliato. Anche se sarà davvero difficile.\n\nL'indice della radice (ossia il denominatore della seconda frazione) non può essere maggiore di 5000 (e non rompete il cazzo tanto 5000 risultati non li legge nessuno)'''
converti ='''Permette di convertire i valori inseriti (prende in considerazione solo interi e float) da un'unità di misura ad un'altra.\n\nPer funzionare devi prima aver aggiunto il fattore di conversione. Puoi farlo nella parte in basso della calcolatrice.\n\nLa sintassi completa del comando è converti(unità_di_misura_A,unità_di_misura_B)\nAd esempio se hai impostato il fattore di conversione per passare da metri a chilometri potrai usare:\nconverti(metri,chilometri)\nQuesto convertirà tutti i numeri inseriti da metri a chilometri.'''
media='''Calcola le medie dei numeri inseriti.\n Calcola la media aritmetica, la media ponderata e la media geometrica.\n (La media geometrica viene calcolata solo se tutti i numeri sono diversi da 0)'''
