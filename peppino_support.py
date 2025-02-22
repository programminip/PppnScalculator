from fractions2 import Fraction as fr
import re
regex_periodico = r"^[-+]?\d+\.\d+_\d+$"
regex_frazione = r"^[-+]?\d+\/\d+$"
regex_conversioni = r"converti\([^,]+,[^)]+\)"

def analizzatore_numeri(stringa,i=False,fl=False,frc=False):
    '''Analizza una stringa ed estrae i numeri in essa presenti.
    I numeri così estratti verranno disposti in 4 liste separate che verranno date come valori di ritorno.
    La prima lista conterrà i numeri interi trovati.
    La seconda e la terza conterranno i numeri in virgola trovati.
    \tLa seconda lista conterrà i numeri in virgola.
    \tLa terza lista conterrà le rispettive frazioni generatrici (Oggetti Fraction2)
    La quarta lista conterrà i numeri immaginari.

    La classe Fraction2 estende Fraction per fare in modo di poter generare un oggetto frazione a partire da una stringa che rappresenta un numero periodico (le cire del suo periodo sono indicate dopo il simbolo underscore. Ad esempio 3.2672_2 indica il numero periodico 3.26727272727272727272)
    i, fl ed fr sono valori booleani che stabiliscono se un numero va aggiunto ad un'altra lista quando possibile'''
    all, interi, floating, frazioni, complessi = [], [], [], [], []
    elementi = stringa.split(' ')
    for elemento in elementi:
        if 'j' in elemento:
            try:
                complessi.append(complex(elemento))
                all.append(complex(elemento))
                continue
            except:
                pass
        if re.match(regex_periodico, elemento) or re.match(regex_frazione, elemento):
            frazione = fr(elemento)
            frazioni.append(frazione)
            all.append(frazione)
            if fl:
                floating.append(frazione.numerator / frazione.denominator)
            if i and frazione.denominator == 1:
                interi.append(frazione.numerator)
        else:
            try:
                numero = float(elemento)
            except:
                continue
            if numero == int(numero):
                interi.append(int(numero))
                all.append(int(numero))
                if frc:
                    frazioni.append(fr(numero))
                if fl and not i:
                    floating.append(numero / 1)
            else:
                floating.append(numero)
                all.append(numero)
                if frc:
                    frazioni.append(fr(numero))

    return all, interi, floating, frazioni, complessi

def analizzatore_comandi(stringa,comandi):
    '''Data una stringa ed una lista di comandi possibili ritorna una lista contenente quelli presenti nella stringa'''
    stringa = stringa.lower()
    elementi = stringa.split(' ')
    comandi_out = []
    for elemento in elementi:
        if elemento in comandi or re.match(regex_conversioni, elemento):
            comandi_out.append(elemento)
    return comandi_out

if __name__=='__main__':
    pass
