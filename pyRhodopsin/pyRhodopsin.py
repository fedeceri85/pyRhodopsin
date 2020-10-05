import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import serial
import time

from MainWindow import Ui_MainWindow


class pyRhodopsin(Ui_MainWindow, PyQt4.QtGui.QMainWindow):
    def __init__(self, parent=None):
        PyQt4.QtGui.QMainWindow.__init__(self, parent=parent)
        self.com = 'COM6'
        self.isi = 1000
        self.duration = 2
        self.N = 0
        self.ibi = 5000
        self.mode = 0
        self.potValue = 63
        self.rampMode = False
        self.pretrigger = False
        self.pretriggerValue = 30
        self.pretriggerDuration = 20
        try:
            self.ser = serial.Serial(self.com,9600, timeout=5, parity=serial.PARITY_EVEN, rtscts=1)
            time.sleep(2)
            self.ser.isOpen()
            self.ser.flushInput()
            self.ser.flushOutput()
        except:
            self.ser = None
            self.com = 'None'
        self.setupUi(self)
        self.nspikesSpinBox.setMinimum(0)
        self.updateValues()

        #CONNECTIONS
        self.connect(self.comLineEdit, SIGNAL("editingFinished()"), self.connectToSerial)
        self.connect(self.OnPushButton,SIGNAL("clicked()"),self.turnon)
        self.connect(self.offPushButton,SIGNAL("clicked()"),self.turnoff)
        self.connect(self.blinkPushButton,SIGNAL("clicked()"),self.blink)
        self.connect(self.rampCheckBox,SIGNAL("stateChanged(int)"),self.toggleRamp)
        self.connect(self.pretriggerCheckBox,SIGNAL("stateChanged(int)"),self.togglePretrigger)



    def updateValues(self):
        self.comLineEdit.setText(self.com)
        self.isiSpinBox.setValue(self.isi)
        self.durationSpinBox.setValue(self.duration)
        self.nspikesSpinBox.setValue(self.N)
        self.ibiSpinBox.setValue(self.ibi)
        self.potSpinBox.setValue(self.potValue)
        self.rampCheckBox.setChecked(self.rampMode)
        self.pretriggerCheckBox.setChecked(self.pretrigger)
        self.potPretSpinBox.setValue(self.pretriggerValue)
        self.pretriggerDurationSpinBox.setValue(self.pretriggerDuration)

    def connectToSerial(self):
        self.com = str(self.comLineEdit.text())
        try:
            self.ser.close()
        except AttributeError:
            pass
        try:
            self.ser = serial.Serial(self.com,9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
            time.sleep(2)
            self.ser.isOpen()
            self.ser.flushInput()
            self.ser.flushOutput()
        except:
            self.ser = None
            self.com = 'None'

        self.updateValues()

    def turnon(self):
        self.potValue = self.potSpinBox.value()
        str5 = str(63-self.potValue)
        message = "0 0 1 0 0 "+str5+" 0 0 0\n"
	message = bytearray(message)
	print(message)
	#message = b"0 0 1 0 0 30\n"
        self.ser.write(message)
        self.mode = 1


    def turnoff(self):
        self.potValue = self.potSpinBox.value()
        str5 = str(63-self.potValue)	
	message = "0 0 0 0 0 "+str5+" 0 0 0\n"
	message = bytearray(message)
        self.ser.write(message)
	print(message)
        self.mode=0

    def blink(self):
        self.isi = self.isiSpinBox.value()
        self.duration = self.durationSpinBox.value()
        self.N = self.nspikesSpinBox.value()
        self.ibi = self.ibiSpinBox.value()
        self.potValue = self.potSpinBox.value()
        self.pretriggerValue = self.potPretSpinBox.value()
        self.pretriggerDuration = self.pretriggerDurationSpinBox.value()
        str1 = str(self.isi)
        str2 = str(self.duration)
        str3 = str(self.N)
        str4 = str(self.ibi)
        str5 = str(63-self.potValue)
        if self.rampCheckBox.isChecked():
            str6 = '1'
        elif self.pretriggerCheckBox.isChecked():
            str6 = '2'
        else:
            str6 = '0'

        str7 = str(63-  self.pretriggerValue )
        str8 = str(self.pretriggerDuration)
        message =  bytearray(str1 + ' '  + str2 + ' ' + '2 '+ str4 + ' '+ str3+' '+str5+' '+str6+' '+str7+' '+str8+'\n')
	print(message)
        self.ser.write(message)
        self.mode=2

    def changePower(self):
        if self.mode==0:
            self.turnoff()
        elif self.mode==1:
            self.turnon()
        elif self.mode==2:
            self.blink()
	time.sleep(0.1)

    def toggleRamp(self):
        if self.rampCheckBox.isChecked():
            self.rampMode = True
            self.pretrigger = False
            self.pretriggerCheckBox.setChecked(False)
            self.pretriggerDurationSpinBox.setEnabled(False)
            self.potPretSpinBox.setEnabled(False)
            self.label_7.setEnabled(False)
            self.label_8.setEnabled(False)
        else: 
            self.rampMode = False


    def togglePretrigger(self):

        if self.pretriggerCheckBox.isChecked():
            self.rampMode = False
            self.pretrigger = True
            self.rampCheckBox.setChecked(False)
            self.pretriggerDurationSpinBox.setEnabled(True)
            self.potPretSpinBox.setEnabled(True)
            self.label_7.setEnabled(True)
            self.label_8.setEnabled(True)
        else: 
            self.pretrigger = False
            self.pretriggerDurationSpinBox.setEnabled(False)
            self.potPretSpinBox.setEnabled(False)
            self.label_7.setEnabled(False)
            self.label_8.setEnabled(False)

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    Rhodopsin = pyRhodopsin()
    Rhodopsin.show()

    # ipshell = InteractiveShellEmbed()
    # ipshell()
    ans = app.exec_()
    sys.exit(ans)
