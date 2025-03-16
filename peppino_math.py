import math
import fractions2

def proporzione(*args):
    '''Calcola una proporzione:\n 
    Metodo 1: passa 4 parametri es. 5, 10, None, 15\t\t- ritorna il risultato numerico
    Metodo 2: passa 4 parametri es. 5, 10, 'x', 15\t\t- ritorna una stringa 'x = 7.5'
    \t\tal posto di x puoi usare un nome diverso, y, litri, patate, 'stocazzo
    Metodo 3: passa 3 parametri es. 5, 10, 15\t\t\t- ritorna un dizionario di 4 risultati
    Metodo 4: passa un solo parametro stringa - '5:10=x:15'
    \t\tritorna una stringa 'x = 7.5', x può avere un nome diverso, invece
    \t\tritorna il risultato numerico se usi None es. '5:10=None:15'''

    if len(args) == 1:
        if type(args[0]).__name__ == 'str':
            supp = args[0].replace("=", ":")
            supp = supp.split(":")
            args = []
            for el in supp:
                args.append(float(el) if el.isnumeric() else el if el != 'None' else None)
        else:
            raise TypeError('Un solo parametro deve essere una stringa con x come incognita. Es. 5:10=x:15')
    if len(args) == 3:
        numeri, incognita, pos = 0, 0, 0
        for i, arg in enumerate(args):
            numeri += 1 if isinstance(arg,(int, float)) else 0
            incognita, pos = (incognita + 1, i) if isinstance(arg,(str, type(None))) else (incognita, pos)
        if numeri != 3:
            raise TypeError('Uno o più parametri sono di tipo errato')
        return {f'x:{args[0]}={args[1]}:{args[2]}':args[0]*args[1]/args[2], f'{args[0]}:x={args[1]}:{args[2]}':args[0]*args[2]/args[1] ,f'{args[0]}:{args[1]}=x:{args[2]}':args[0]*args[2]/args[1] ,f'{args[0]}:{args[1]}={args[2]}:x':args[1]*args[2]/args[0]}
    elif len(args) == 4:
        numeri, incognita, pos = 0, 0, 0
        for i, arg in enumerate(args):
            numeri += 1 if isinstance(arg,(int, float)) else 0
            incognita, pos = (incognita + 1, i) if isinstance(arg,(str, type(None))) else (incognita, pos)
        if numeri != 3 or incognita != 1:
            raise TypeError('Uno o più parametri sono di tipo errato')
        match pos:
            case 0:
                ris = args[1]*args[2]/args[3]
            case 1:
                ris = args[0]*args[3]/args[2]
            case 2:
                ris = args[0]*args[3]/args[1]
            case 3:
                ris = args[1]*args[2]/args[0]
        if isinstance(args[pos],type(None)):
            return ris
        else:
            return f'{args[pos]} = {ris}'
    else:
        raise TypeError('Numero di parametri errato.')

def potenza(*args):
    '''Richiede almeno 2 argomenti. L'ultimo argomento è l'esponente a cui verranno elevati tutti gli altri argomenti. Ritorna una lista'''
    if len(args) < 2:
        raise ValueError("Sono necessari almeno 2 dati per calcolare una potenza.")
    esponente = args[len(args)-1]
    args = list(args)
    args.pop(len(args)-1)
    return [round(a**esponente,5) for a in args]

def media_aritmetica(*args):
    '''Richiede almeno 2 argomenti. Ritorna la media aritmetica degli argomenti passati'''
    if len(args) < 2:
        raise ValueError("Sono necessari almeno 2 dati per calcolare una media.")
    somma=0
    for numero in args:
        somma+=numero
    return somma/len(args)

def media_ponderata(*args):
    '''Ritorna la madia ponderata dei valori passati come coppia valore, peso.

    Si consideri l'esempio in cui vogliamo passare 4 coppie di valori/pesi:
    valoreA: 5, pesoA:10;
    valoreB: 7, pesoB:13;
    valoreC: 2.5, pesoC:4;
    valoreD: 5, pesoD:5;
    Metodi di passaggio dati.

    media_ponderata((5,10), (7,13), (2.5,4), (5,5))
    Metodo 1: Ogni coppia viene passata come iterabile (liste o tuple).

    media_ponderata((5,7,2.5,5), (10,13,4,5))
    Metodo 2: Vengono passati due iterabili, il primo con tutti i valori ed il secondo con tutti i pesi.
              Questo metodo è utilizzabile solo se ci sono PIÙ di due coppie di valori.

    media_ponderata(5,10,7,13,2.5,4,5,5)
    Metodo 3: Vengono passati solo numeri alternandoli come valore, peso, valore, peso, ecc..

    Richiede almeno due coppie.'''
    numeri, iterabili = 0, 0
    for el in args:
        numeri += 1 if isinstance(el, (int, float)) else 0
        iterabili += 1 if isinstance(el, (tuple, list)) else 0
    if numeri!=0 and iterabili!=0:
        raise TypeError("La funzione richiede o solo numeri o solo iterabili")
    if numeri!=0 and len(args)%2!=0:
        raise ValueError("Numero errato di valori inseriti")
    if numeri!=0:
        dati = []
        for i in range(0,len(args),2):
            dati.append((args[i],args[i+1]))
        return media_ponderata(*dati)
    if iterabili == 2:
        if len(args[0])!=len(args[1]):
            raise ValueError("Errore nei dati")
        if len(args[0])>2:
            return media_ponderata(*zip(args[0],args[1]))
    
    numeratore, denominatore = 0, 0
    for coppia in args:
        if len(coppia)>2:
            raise ValueError("Errore nei dati")
        numeratore += coppia[0]*coppia[1]
        denominatore += coppia[1]
    if denominatore == 0:
        raise ValueError("Divisione per 0")
    return numeratore/denominatore

def media_geometrica(*args):
    '''Richiede almeno 2 argomenti. Ritorna la media geometrica degli argomenti passati.
    Gli argomenti devono essere maggiori di 0'''
    prodotto = 1
    for numero in args:
        if numero <= 0:
            raise ValueError("Non calcolabile con numeri <= 0")
        prodotto*=numero
    return prodotto**(1/len(args))
def scomposizione_fattori_primi(n): # ideata da Gemini 2.0 e migliorata da me
  """
  Scompone un numero intero in fattori primi.
  Ritorna un dizionario che ha come chiavi i fattori e come valore l'esponente.
  """
  fattori = {}
  if n < 0:
    fattori[-1]=1
    n=-n
  d = 2
  while d * d <= n:
    while n % d == 0:
      fattori[d]=fattori[d]+1 if d in fattori else 1
      n //= d
    d += 1
  if n > 1:
    fattori[n]=1
  return fattori

def potenza_mk2(frazione1, frazione2):
    if not (isinstance(frazione1,fractions2.Fraction) and isinstance(frazione1,fractions2.Fraction)):
        raise ValueError('La funzione non ha ricevuto frazioni')
    numeratore1, denominatore1, numeratore2, denominatore2 = frazione1.numerator, frazione1.denominator, frazione2.numerator, frazione2.denominator
    output = ''
    if (numeratore1 < 0 and denominatore1 < 0) or (numeratore1 >=0 and denominatore1 < 0):
        numeratore1 *= -1
        denominatore1 *= -1
    if (numeratore2 < 0 and denominatore2 < 0) or (numeratore2 >=0 and denominatore2 < 0):
        numeratore2 *= -1
        denominatore2 *= -1
    if denominatore2 > 5000:
        raise ValueError("Errore. Il denominatore dell'esponente deve essere al massimo pari a 1000")
    if denominatore1 == 0 or denominatore2 == 0:
        raise ZeroDivisionError
    if numeratore2 < 0 and denominatore2 == 1:
        output = f'({numeratore1}/{denominatore1})**{numeratore2} = ({denominatore1}/{numeratore1})**{-numeratore2}=({denominatore1**(-numeratore2)}/{numeratore1**(-numeratore2)}) = {(denominatore1**(-numeratore2))/(numeratore1**(-numeratore2))}'
    elif denominatore2 == 1:
        output = f'{(numeratore1/denominatore1 ** numeratore2)}'
    else:
        output = f'({numeratore1}/{denominatore1})**({numeratore2}/{denominatore2}) = {denominatore2}√({numeratore1}/{denominatore1})**{numeratore2} =\n'
        if numeratore2 < 0:
            provvisorio = denominatore1
            denominatore1 = numeratore1
            numeratore1 = provvisorio
            numeratore2 = -numeratore2
            output = f'{output}\n{denominatore2}√({numeratore1}/{denominatore1})**{numeratore2} = \n'
        numeratore1 = numeratore1 ** numeratore2
        denominatore1 = denominatore1 ** numeratore2
        output = f'{output}{denominatore2}√({numeratore1}/{denominatore1})= \n'
        if denominatore1 < 0:
            numeratore1 *= -1
            denominatore1 *= -1
            if denominatore2 == 2:
                output = f'{output}{numeratore**(1/2)}/{denominatore**(1/2)} = \n'
        if denominatore2 == 2:
            output = f'{output}±{(numeratore1 / denominatore1) ** (1 / denominatore2)}'
        else:
            modulo = abs(numeratore1/denominatore1) ** (1/denominatore2)
            for k in range(0,denominatore2):
                if numeratore1 < 0:
                    ot = (math.pi*(1+2*k))/denominatore2
                else:
                    ot =(math.pi*(2*k))/denominatore2
                otc = math.cos(ot)
                ots = math.sin(ot)
                tolleranza = 1e-15
                if abs(otc) < tolleranza:
                    otc = 0.0
                if abs(ots) < tolleranza:
                    ots = 0.0
                parte_reale = modulo * otc
                parte_immaginaria = modulo * ots
                comp = complex(parte_reale,parte_immaginaria)
                output=f'{output}\nRisultato {k + 1} ≈ {comp}'
                if comp.imag==0:
                    output=f'{output} ∈ R'
    return output


if __name__=='__main__':
    print(potenza_mk2(fractions2.Fraction('16'),fractions2.Fraction('1/5001')))
