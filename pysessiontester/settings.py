from PyQt4.QtGui import QDialog, QFileDialog
from pysessiontester.ui.settings_window import Ui_optionsDialog


class SettingsWindow(QDialog, Ui_optionsDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.config_file = parent.session_config
        self.export_directory = self.config_file.read_config()
        self.exportPath.setText(self.export_directory)
        
        self.choosepathButton.clicked.connect(self.choose_directory)
        self.buttonBox.accepted.connect(self.set_directory)

    def choose_directory(self):
        self.file_dialog = QFileDialog(self)
        self.file_dialog.setFileMode(QFileDialog.Directory)
        if (self.file_dialog.exec_()):
            result = self.file_dialog.selectedFiles()
        self.export_directory = result[0]
        self.exportPath.setText(self.export_directory)

    def set_directory(self):
        self.config_file.write_config(self.export_directory)
