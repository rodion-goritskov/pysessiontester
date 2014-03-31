from PyQt4.QtGui import QDialog, QFileDialog
from settings_window import Ui_optionsDialog
from config_utils import SessionConfig

EXPORT_PATH = ""


class SettingsWindow(QDialog, Ui_optionsDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.configfile = SessionConfig("export.ini")
        global EXPORT_PATH
        EXPORT_PATH = self.configfile.read_config()
        self.exportPath.setText(EXPORT_PATH)
        self.choosepathButton.clicked.connect(self.choose_directory)
        self.buttonBox.accepted.connect(self.set_directory)

    def choose_directory(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.Directory)
        if (self.file_dialog.exec_()):
            self.result = self.file_dialog.selectedFiles()
        global EXPORT_PATH
        EXPORT_PATH = self.result[0]
        self.exportPath.setText(EXPORT_PATH)

    def set_directory(self):
        self.configfile.write_config(self.exportPath.text())
