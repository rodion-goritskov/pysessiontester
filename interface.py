# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Mar 10 00:23:06 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_MainAppWindow(object):
    def setupUi(self, MainAppWindow):
        MainAppWindow.setObjectName(_fromUtf8("MainAppWindow"))
        MainAppWindow.resize(800, 600)
        MainAppWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainAppWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newSessionButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.newSessionButton.setObjectName(_fromUtf8("newSessionButton"))
        self.horizontalLayout.addWidget(self.newSessionButton)
        self.exportSessionButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.exportSessionButton.setObjectName(_fromUtf8("exportSessionButton"))
        self.horizontalLayout.addWidget(self.exportSessionButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sessionTimeField = QtGui.QTimeEdit(self.horizontalLayoutWidget)
        self.sessionTimeField.setObjectName(_fromUtf8("sessionTimeField"))
        self.horizontalLayout.addWidget(self.sessionTimeField)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 29, 801, 541))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 570, 801, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.progressBar = QtGui.QProgressBar(self.horizontalLayoutWidget_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.sessionStartButton = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.sessionStartButton.setObjectName(_fromUtf8("sessionStartButton"))
        self.horizontalLayout_3.addWidget(self.sessionStartButton)
        MainAppWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainAppWindow)
        QtCore.QMetaObject.connectSlotsByName(MainAppWindow)

    def retranslateUi(self, MainAppWindow):
        MainAppWindow.setWindowTitle(_translate("MainAppWindow", "MainWindow", None))
        self.newSessionButton.setText(_translate("MainAppWindow", "New session", None))
        self.exportSessionButton.setText(_translate("MainAppWindow", "Export session", None))
        self.sessionTimeField.setDisplayFormat(_translate("MainAppWindow", "hh:mm:ss", None))
        self.pushButton_3.setText(_translate("MainAppWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("MainAppWindow", "PushButton", None))
        self.sessionStartButton.setText(_translate("MainAppWindow", "Start session", None))

