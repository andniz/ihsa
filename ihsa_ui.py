# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ihsamain.ui'
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

class Ui_IHS(object):
    def setupUi(self, IHS):
        IHS.setObjectName(_fromUtf8("IHS"))
        IHS.resize(804, 619)
        self.centralwidget = QtGui.QWidget(IHS)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 520, 88, 29))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 221, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(140, 20, 501, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(578, 518, 184, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(450, 140, 258, 217))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_10 = QtGui.QLabel(self.widget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_4.addWidget(self.label_10)
        self.listView = QtGui.QListView(self.widget1)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_4.addWidget(self.listView)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(40, 320, 307, 105))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_8 = QtGui.QLabel(self.widget2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_5.addWidget(self.label_8)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.radioButton = QtGui.QRadioButton(self.widget2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.widget2)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.widget2)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout_3.addWidget(self.radioButton_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.widget3 = QtGui.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(90, 100, 100, 201))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.widget3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.widget3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.widget3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.widget4 = QtGui.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(40, 100, 41, 201))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.widget4)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.widget4)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.widget4)
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.verticalLayout.addWidget(self.plainTextEdit_3)
        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.widget4)
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))
        self.verticalLayout.addWidget(self.plainTextEdit_4)
        self.plainTextEdit_5 = QtGui.QPlainTextEdit(self.widget4)
        self.plainTextEdit_5.setObjectName(_fromUtf8("plainTextEdit_5"))
        self.verticalLayout.addWidget(self.plainTextEdit_5)
        self.plainTextEdit_6 = QtGui.QPlainTextEdit(self.widget4)
        self.plainTextEdit_6.setObjectName(_fromUtf8("plainTextEdit_6"))
        self.verticalLayout.addWidget(self.plainTextEdit_6)
        IHS.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(IHS)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        IHS.setStatusBar(self.statusbar)

        self.retranslateUi(IHS)
        QtCore.QMetaObject.connectSlotsByName(IHS)

    def retranslateUi(self, IHS):
        IHS.setWindowTitle(_translate("IHS", "IHS", None))
        self.pushButton_3.setText(_translate("IHS", "Wykres", None))
        self.label_7.setText(_translate("IHS", "Podaj dolne i górne granice zmiennych", None))
        self.label_9.setText(_translate("IHS", "Program wylicza minima funkcji z wykorzystaniem algorytmu Improved Harmony Search", None))
        self.pushButton.setText(_translate("IHS", "Oblicz", None))
        self.pushButton_2.setText(_translate("IHS", "Zamknij", None))
        self.label_10.setText(_translate("IHS", "Obliczone wartości", None))
        self.label_8.setText(_translate("IHS", "Wybierz funkcję, której minima mają zostać obliczone:", None))
        self.radioButton.setText(_translate("IHS", "Three-Hump camel", None))
        self.radioButton_2.setText(_translate("IHS", "RadioButton", None))
        self.radioButton_3.setText(_translate("IHS", "RadioButton", None))
        self.label.setText(_translate("IHS", "Dolna granica x1", None))
        self.label_2.setText(_translate("IHS", "Górna granica x1", None))
        self.label_3.setText(_translate("IHS", "Dolna granica x2", None))
        self.label_4.setText(_translate("IHS", "Górna granica x2", None))
        self.label_5.setText(_translate("IHS", "Dolna granica x3", None))
        self.label_6.setText(_translate("IHS", "Górna granica x3", None))