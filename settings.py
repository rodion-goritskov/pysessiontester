from PyQt4.QtGui import QDialog, QFileDialog
from settings_window import Ui_optionsDialog

EXPORT_PATH = ""


class SettingsWindow(QDialog, Ui_optionsDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.exportPath.setText(EXPORT_PATH)
        self.choosepathButton.clicked.connect(self.choose_directory)

    def choose_directory(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.Directory)
        if (self.file_dialog.exec_()):
            self.result = self.file_dialog.selectedFiles()
        global EXPORT_PATH
        EXPORT_PATH = self.result[0]
        self.exportPath.setText(EXPORT_PATH)
