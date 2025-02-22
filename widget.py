# This Python file uses the following encoding: utf-8
import doc
import sys
import peppino_math
import peppino_support
import math
import pickle


from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

# VENV → source /home/peppe/PppnScalculator/.qtcreator/Python_3_13_1venv/bin/activate

convum1, convum2 = '', ''
convJson = {}
costanti = {'Costanti':'','π, Pi Greco':math.pi,'c, Velocità luce (m/s)':299792458}
memoria = []
comandi_possibili = ['modificatori','potenza','potenza_mk2','converti','media']

def salva_json(il_json, nome_file):
    with open(nome_file, "wb") as filescr:
      pickle.dump(convJson, filescr)

def converti(da, a, valore, conversioni):
    """Converte un valore da un'unità all'altra."""
    chiave = (da, a)
    if chiave in conversioni:
        fattore = conversioni[chiave]
        return valore * fattore
    else:
        raise ValueError(f'Non conosco la conversione {chiave}')

def daProporzionare(numeri):
    output=''
    if len(numeri)==3:
        prop=peppino_math.proporzione(*numeri)
        output=f'Proporzioni possibili fra {numeri}:\n'
        for ppz in prop:
            output=f'{output}{ppz}  →  x = {prop[ppz]}\n'
    return output

def daMediare(numeri):
    mediaAritmetica=peppino_math.media_aritmetica(*numeri)
    try:
        mediaPonderata=peppino_math.media_ponderata(*numeri) if len(numeri)%2==0 else 'Non calcolabile'
    except Exception as e:
        mediaPonderata=str(e)
    mediaGeometrica=peppino_math.media_geometrica(*numeri) if not 0 in numeri else 'Non calcolabile.'
    return f'''Media Aritmetica = {mediaAritmetica}
Media Ponderata = {mediaPonderata} (considerando i numeri inseriti in coppia valore/peso)
Media Geometrica = {mediaGeometrica}'''

from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.comboBox.insertItems(0,[n for n in costanti])
        self.ui.comboBox.textActivated.connect(lambda: self.pressed(costanti[self.ui.comboBox.currentText()]))

        self.ui.comboBoxMemoria.textActivated.connect(lambda: self.pressed(self.ui.comboBoxMemoria.currentText()))
        self.ui.bottoneSvuotaMemoria.clicked.connect(self.svuotaMemoria)

        self.listaconversioni()
        self.ui.comboBoxConversioni.textActivated.connect(lambda: self.conversioni_select(self.ui.comboBoxConversioni.currentText()))

        self.ui.bottone0.clicked.connect(lambda: self.pressed(0))
        self.ui.bottone1.clicked.connect(lambda: self.pressed(1))
        self.ui.bottone2.clicked.connect(lambda: self.pressed(2))
        self.ui.bottone3.clicked.connect(lambda: self.pressed(3))
        self.ui.bottone4.clicked.connect(lambda: self.pressed(4))
        self.ui.bottone5.clicked.connect(lambda: self.pressed(5))
        self.ui.bottone6.clicked.connect(lambda: self.pressed(6))
        self.ui.bottone7.clicked.connect(lambda: self.pressed(7))
        self.ui.bottone8.clicked.connect(lambda: self.pressed(8))
        self.ui.bottone9.clicked.connect(lambda: self.pressed(9))
        self.ui.bottonePunto.clicked.connect(lambda: self.pressed('.'))
        self.ui.bottonepiu.clicked.connect(lambda: self.pressed('+'))
        self.ui.bottonemeno.clicked.connect(lambda: self.pressed('-'))
        self.ui.bottoneper.clicked.connect(lambda: self.pressed('*'))
        self.ui.bottonediviso.clicked.connect(lambda: self.pressed('/'))
        self.ui.bottoneTondaAperta.clicked.connect(lambda: self.pressed('('))
        self.ui.bottoneTondaChiusa.clicked.connect(lambda: self.pressed(')'))
        self.ui.bottoneUguale.clicked.connect(self.calcola_classic)

        self.ui.bottoneCanc.clicked.connect(self.canc)
        self.ui.bottoneC.clicked.connect(self.CCC)
        self.ui.bottoneCE.clicked.connect(self.CCCE)

        self.ui.bottoneBoh.clicked.connect(self.mostra_documentazione)

        self.ui.bottoneOk.clicked.connect(self.gooo)

        self.ui.pushButtonConversioni.clicked.connect(self.salva_conversione_check)

        self.ui.pushButtonConversioniRimuovi.clicked.connect(self.cancella_conversione)


    def gooo(self):
        try:
            if self.ui.textInput.toPlainText() == '':
                return
            i = self.ui.checkBoxInteri.isChecked()
            fl = self.ui.checkBoxFloat.isChecked()
            frc = self.ui.checkBoxFrazioni.isChecked()
            comandi = peppino_support.analizzatore_comandi(self.ui.textInput.toPlainText(),comandi_possibili)
            all,interi,floating,frazioni,complessi = peppino_support.analizzatore_numeri(self.ui.textInput.toPlainText(),i,fl,frc)
            output=''
            intEFloat = interi + floating
            if len(interi) > 0:
                output=f'{output}Operazioni sui numeri interi:\nNumeri interi inseriti: {interi}\nSommatoria: {sum(interi)}\n'
                output=f'{output}Il minimo comune multiplo è uguale a {math.lcm(*interi)}\nIl massimo comune divisore è uguale a {math.gcd(*interi)}\n'
                output=f'{output}Scomposizione in fattori primi:\n'
                for intero in interi:
                    output=f'{output}{intero} → {peppino_math.scomposizione_fattori_primi(intero)}\n'
                output=f'{output}{daProporzionare(interi)}'
                if 'media' in comandi and len(interi) >=2:
                    output=f'{output}{daMediare(interi)}\n'
                output=f'{output}\n'
            if len(floating) > 0:
                output=f'{output}Operazioni sui numeri float:\nNumeri float inseriti: {floating}\nSommatoria: {sum(floating)}\n'
                output=f'{output}{daProporzionare(floating)}'
                if 'media' in comandi and len(floating) >=2:
                    output=f'{output}{daMediare(floating)}\n'
                output=f'{output}\n'
            if len(frazioni) > 0:
                output=f'{output}Operazioni sulle frazioni:\nFrazioni inserite: {frazioni}\nSommatoria: {sum(frazioni)}\n'
                output=f'{output}\n'
            if len(complessi)> 0:
                output=f'{output}Operazioni sui numeri complessi:\nNumeri complessi inseriti: {complessi}\nSommatoria: {sum(complessi)}\n'
                output=f'{output}\n'
            if len(interi) > 0 and len(floating)>0:
                output=f'{output}Operazioni su interi e float:\nInteri e float inseriti: {intEFloat}\nSommatoria: {sum(intEFloat)}\n'
                output=f'{output}{daProporzionare(intEFloat)}'
                if 'media' in comandi:
                    output=f'{output}{daMediare(intEFloat)}\n'
                output=f'{output}\n'
            if len(frazioni)==2 and 'potenza_mk2' in comandi:
                output=f'{output}{peppino_math.potenza_mk2(*frazioni)}\n'
            if 'potenza' in comandi:
                output=f'{output}Potenze:\n'
                potenze=peppino_math.potenza(*all)
                espo = all[len(all)-1]
                for i in range(0, len(all)-1):
                    output=f'{output}{all[i]} ** {espo} = {potenze[i]}\n'
                output=f'{output}\n'

            output=f'{output}\nConversioni:\n'
            set_com = set(comandi)
            for comando in set_com:
                try:
                    if 'converti' in comando and ',' in comando:
                        u = comando.split(',')
                        u1=u[0][9:]
                        u2=u[1][:len(u[1])-1]
                        for numero in intEFloat:
                            output=f'{output}{numero} {u1} = {converti(u1,u2,numero,convJson)} {u2}\n'
                        output=f'{output}\n'
                except Exception:
                    raise ValueError('Richiesta di conversione malformulata')

            self.ui.textOutput.setPlainText(output)
        except Exception as e:
            self.ui.textOutput.setPlainText(str(e))

    def mostra_documentazione(self):
        comandi = peppino_support.analizzatore_comandi(self.ui.textInput.toPlainText(),comandi_possibili)
        if len(comandi)==0:
            self.ui.textOutput.setPlainText(doc.messaggio_predefinito)
        else:
            self.ui.textOutput.setPlainText('')
            mex_out = ''
            mex_out = f'{mex_out}{doc.modificatori}\n' if 'modificatori' in comandi else f'{mex_out}'
            mex_out = f'{mex_out}{doc.potenza}\n' if 'potenza' in comandi else f'{mex_out}'
            mex_out = f'{mex_out}{doc.potenza_mk2}\n' if 'potenza_mk2' in comandi else f'{mex_out}'
            mex_out = f'{mex_out}{doc.converti}\n' if 'converti' in comandi else f'{mex_out}'
            mex_out = f'{mex_out}{doc.media}\n' if 'media' in comandi else f'{mex_out}'
            #...
            self.ui.textOutput.setPlainText(mex_out)

    def salva_conversione_check(self):
        unitaMis1 = self.ui.textUM1.toPlainText()
        unitaMis2 = self.ui.textUM2.toPlainText()
        fattoreConv = self.ui.textFC.toPlainText()
        if unitaMis1 == '' or unitaMis2 == '':
            self.ui.textOutput.setPlainText('Il testo per le unità di misura è obbligatorio')
            return
        if ',' in unitaMis1 or ',' in unitaMis2:
            self.ui.textOutput.setPlainText("Non è consentito l'uso della virgola all'interno del nome di una unità di misura")
            return
        try:
            fattoreConv=float(fattoreConv)
        except:
            try:
                fattoreConv=eval(fattoreConv)
                fattoreConv=float(fattoreConv)
            except:
                self.ui.textOutput.setPlainText('Fattore di conversione invalido')
            else:
                self.salva_conversione(unitaMis1, unitaMis2, fattoreConv)
        else:
            self.salva_conversione(unitaMis1, unitaMis2, fattoreConv)

    def salva_conversione(self, um1, um2, fc):
        #print(type(um1).__name__)
        convJson[(um1,um2)]=fc
        convJson[(um2,um1)]=1/fc
        self.listaconversioni()

    def cancella_conversione(self):
        global convum1
        global convum2
        if (convum1, convum2) in convJson:
            del(convJson[(convum1, convum2)])
            del(convJson[(convum2, convum1)])
            convum1, convum2 = '', ''
            self.listaconversioni()
        else:
            self.ui.textOutput.setPlainText('Elemento non presente')

    def CCC(self):
        if (self.ui.textInput.toPlainText()==""):
            self.ui.textOutput.setPlainText("")
        else:
            self.ui.textInput.setPlainText("")

    def CCCE(self):
        testo=self.ui.textInput.toPlainText()
        testo=testo[0:len(testo)-1]
        self.ui.textInput.setPlainText(testo)

    def canc(self):
        self.ui.textInput.setPlainText("")
        self.ui.textOutput.setPlainText("")
        self.svuotaMemoria()

    def svuotaMemoria(self):
        memoria = []
        self.ui.comboBoxMemoria.clear()

    def pressed(self,x):
        testo = self.ui.textInput.toPlainText()
        self.ui.textInput.setPlainText(f'{testo}{x}')

    def calcola_classic(self):
        try:
            formula = self.ui.textInput.toPlainText()
            risultato = eval(formula)
            self.ui.comboBoxMemoria.clear()
            memoria.insert(0,str(risultato))
            self.ui.comboBoxMemoria.insertItems(0,memoria)
            self.ui.textInput.setPlainText(str(risultato))
            self.ui.textOutput.setPlainText(f'{formula} = {risultato}\n\n{self.ui.textOutput.toPlainText()}')
        except Exception:
            self.ui.textOutput.setPlainText("Calcolo mal formulato. Verificare.")

    def listaconversioni(self):
        r=[]
        for el in convJson:
            r.append(f'{el[0]} - {el[1]}')
        self.ui.comboBoxConversioni.clear()
        self.ui.comboBoxConversioni.insertItems(0,r)
        salva_json(convJson,'conversioni.pkl')

    def conversioni_select(self,chiavi):
        global convum1
        global convum2
        chia=chiavi.split(' - ')
        self.pressed(f' converti({chia[0]},{chia[1]}) ')
        self.ui.textUM1.setPlainText(chia[0])
        convum1=chia[0]
        self.ui.textUM2.setPlainText(chia[1])
        convum2=chia[1]
        self.ui.textFC.setPlainText('')

if __name__ == "__main__":
    try:
        with open('conversioni.pkl', "rb") as fileConversioni:
            convJson = pickle.load(fileConversioni)
    except FileNotFoundError:
        pass

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
