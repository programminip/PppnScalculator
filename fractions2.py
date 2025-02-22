from fractions import Fraction

class Fraction(Fraction):
    def __new__(cls, numerator=0, denominator=None):
        if isinstance(numerator,str) and denominator==None:
            if '_' in numerator:
                parti = numerator.split('.')
                parti = [parti[0],parti[1].split('_')]
                cifrePeriodo = int(parti[1][1])
                cifreAntiperiodoEPeriodo = len(parti[1][0])
                cifreAntiperiodo = cifreAntiperiodoEPeriodo-cifrePeriodo
                antiperiodoEPeriodo = int(parti[1][0])
                parteIntera = int(parti[0])
                positivo = 1 if parteIntera >= 0 else -1
                parteIntera = abs(parteIntera)
                antiperiodo = int(antiperiodoEPeriodo/(10**cifrePeriodo))
                numerator = positivo * int((parteIntera*(10**cifreAntiperiodoEPeriodo) + antiperiodoEPeriodo) - (parteIntera * (10**cifreAntiperiodo)+ antiperiodo))                
                denominator = int((10**cifrePeriodo - 1)*(10**cifreAntiperiodo))
        return super().__new__(cls,numerator,denominator)

if __name__=='__main__':
    a=Fraction("22.2345_2")
    print(a)
