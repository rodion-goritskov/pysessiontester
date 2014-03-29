# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_window.ui'
#
# Created: Sun Mar 30 00:40:10 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_optionsDialog(object):
    def setupUi(self, optionsDialog):
        optionsDialog.setObjectName(_fromUtf8("optionsDialog"))
        optionsDialog.resize(395, 289)
        optionsDialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        optionsDialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(optionsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(optionsDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.exportPath = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.exportPath.setObjectName(_fromUtf8("exportPath"))
        self.horizontalLayout.addWidget(self.exportPath)
        self.choosepathButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.choosepathButton.setObjectName(_fromUtf8("choosepathButton"))
        self.horizontalLayout.addWidget(self.choosepathButton)

        self.retranslateUi(optionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), optionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), optionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(optionsDialog)

    def retranslateUi(self, optionsDialog):
        optionsDialog.setWindowTitle(_translate("optionsDialog", "Settings", None))
        self.label.setText(_translate("optionsDialog", "Export path:", None))
        self.choosepathButton.setText(_translate("optionsDialog", "...", None))

