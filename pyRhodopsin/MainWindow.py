# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow - untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(384, 566)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.comLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.comLineEdit.setObjectName(_fromUtf8("comLineEdit"))
        self.horizontalLayout_6.addWidget(self.comLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.isiSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.isiSpinBox.setMinimum(1)
        self.isiSpinBox.setMaximum(100000)
        self.isiSpinBox.setObjectName(_fromUtf8("isiSpinBox"))
        self.horizontalLayout.addWidget(self.isiSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.durationSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.durationSpinBox.setMinimum(1)
        self.durationSpinBox.setMaximum(100000)
        self.durationSpinBox.setObjectName(_fromUtf8("durationSpinBox"))
        self.horizontalLayout_2.addWidget(self.durationSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.nspikesSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.nspikesSpinBox.setMinimum(1)
        self.nspikesSpinBox.setMaximum(100000)
        self.nspikesSpinBox.setObjectName(_fromUtf8("nspikesSpinBox"))
        self.horizontalLayout_4.addWidget(self.nspikesSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.ibiSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.ibiSpinBox.setMaximum(100000)
        self.ibiSpinBox.setObjectName(_fromUtf8("ibiSpinBox"))
        self.horizontalLayout_5.addWidget(self.ibiSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.potSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.potSpinBox.setEnabled(True)
        self.potSpinBox.setMaximum(63)
        self.potSpinBox.setObjectName(_fromUtf8("potSpinBox"))
        self.horizontalLayout_7.addWidget(self.potSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.rampCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.rampCheckBox.setObjectName(_fromUtf8("rampCheckBox"))
        self.horizontalLayout_8.addWidget(self.rampCheckBox)
        self.pretriggerCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.pretriggerCheckBox.setObjectName(_fromUtf8("pretriggerCheckBox"))
        self.horizontalLayout_8.addWidget(self.pretriggerCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.potPretSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.potPretSpinBox.setEnabled(False)
        self.potPretSpinBox.setMaximum(63)
        self.potPretSpinBox.setObjectName(_fromUtf8("potPretSpinBox"))
        self.horizontalLayout_9.addWidget(self.potPretSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setEnabled(False)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_10.addWidget(self.label_8)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.pretriggerDurationSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.pretriggerDurationSpinBox.setEnabled(False)
        self.pretriggerDurationSpinBox.setMinimum(1)
        self.pretriggerDurationSpinBox.setMaximum(100000)
        self.pretriggerDurationSpinBox.setObjectName(_fromUtf8("pretriggerDurationSpinBox"))
        self.horizontalLayout_10.addWidget(self.pretriggerDurationSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.OnPushButton = QtGui.QPushButton(self.centralwidget)
        self.OnPushButton.setObjectName(_fromUtf8("OnPushButton"))
        self.horizontalLayout_3.addWidget(self.OnPushButton)
        self.offPushButton = QtGui.QPushButton(self.centralwidget)
        self.offPushButton.setObjectName(_fromUtf8("offPushButton"))
        self.horizontalLayout_3.addWidget(self.offPushButton)
        self.blinkPushButton = QtGui.QPushButton(self.centralwidget)
        self.blinkPushButton.setObjectName(_fromUtf8("blinkPushButton"))
        self.horizontalLayout_3.addWidget(self.blinkPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pyRhodopsin", None))
        self.label_5.setText(_translate("MainWindow", "Arduino port", None))
        self.comLineEdit.setText(_translate("MainWindow", "COM5", None))
        self.label.setText(_translate("MainWindow", "Interspike interval (ms)", None))
        self.label_2.setText(_translate("MainWindow", "Duration (ms)", None))
        self.label_3.setText(_translate("MainWindow", "Number of spikes per burst (0: no burst.)", None))
        self.label_4.setText(_translate("MainWindow", "Interburst interval (ms)", None))
        self.label_6.setText(_translate("MainWindow", "Potentiometer value (0-63)", None))
        self.rampCheckBox.setText(_translate("MainWindow", "Ramp mode", None))
        self.pretriggerCheckBox.setText(_translate("MainWindow", "Pretrigger mode", None))
        self.label_7.setText(_translate("MainWindow", "Pretrigger pot. value (0-63)", None))
        self.label_8.setText(_translate("MainWindow", "Pretrigger duration (ms)", None))
        self.OnPushButton.setText(_translate("MainWindow", "On", None))
        self.offPushButton.setText(_translate("MainWindow", "Off", None))
        self.blinkPushButton.setText(_translate("MainWindow", "Blinking", None))

