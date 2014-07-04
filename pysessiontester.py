import sys
from PyQt4.QtGui import QApplication, QMainWindow, QSystemTrayIcon, QIcon
from PyQt4 import QtCore
from main_window import Ui_MainAppWindow
from export_session import *
import datetime
import threading
import time
from settings import SettingsWindow


class SessionTesterWindow(QMainWindow, Ui_MainAppWindow):

    progress_bar_change = QtCore.pyqtSignal()
    session_end = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)

        self.isStarted = False
        self.isPaused = True
        self.isRIP = False
        self.current_time = 0

        self.tray_icon = QSystemTrayIcon(QIcon("trayicon.xpm"))
        self.tray_icon.show()
        self.session_end.connect(self.session_end_message)

        self.setupUi(self)
        self.sessionStartButton.clicked.connect(self.start_session)
        self.newSessionButton.clicked.connect(self.new_session)
        self.exportSessionButton.clicked.connect(self.export_session)
        self.settingsButton.clicked.connect(self.open_settings)
        self.tray_icon.activated.connect(self.maximize_window)

        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat("Session progress")

    def start_session(self):
        self.session_time = self.__count_session_time(
            self.sessionTimeField.time().toString("hh:mm:ss"))
        if (self.isPaused is True) & (self.session_time > 0):
            self.isPaused = False
            self.sessionStartButton.setText("Pause session")
            self.session_time = self.__count_session_time(
                self.sessionTimeField.time().toString("hh:mm:ss"))
            self.progressBar.setMaximum(self.session_time)
            if self.isRIP is True:
                self.progressBar.setValue(0)
                self.current_time = 0
                self.isRIP = False
            self.progress_bar_change.connect(self.set_progress_bar)
            self.t = threading.Thread(target=self.set_progress)
            self.t.daemon = True
            self.t.start()
        else:
            self.sessionStartButton.setText("Start session")
            self.isPaused = True

    def new_session(self):
        self.progressBar.setValue(0)
        self.progressBar.setFormat("Session progress")
        self.sessionStartButton.setText("Start session")
        self.current_time = 0
        self.isPaused = True

    def export_session(self):
        export_session_to_html(self.textEdit.toPlainText())

    def set_progress_bar(self):
        self.progressBar.setValue(self.current_time)
        self.progressBar.setFormat("Time left:" + str(
            datetime.timedelta(seconds=self.time_to_go)))

    def session_end_message(self):
        self.tray_icon.showMessage("Session is over!", "Session time is over")
        self.sessionStartButton.setText("Start session")
        self.progressBar.setFormat("Session is over!")
        self.isPaused = True
        self.isRIP = True

    def set_progress(self):
        while (self.current_time < self.session_time):
            if self.isPaused is False:
                time.sleep(1)
            else:
                break
            if self.isPaused is False:
                self.current_time = self.current_time + 1
                self.progress_bar_change.emit()
                self.time_to_go = self.session_time - self.current_time
        if self.current_time == self.session_time:
            self.session_end.emit()

    def __count_session_time(self, time_string):
        self.result_date = time_string.split(":")
        return (int(self.result_date[0])*3600) + (int(self.result_date[1])*60) + int(self.result_date[2])

    def maximize_window(self, reason):
        if self.isHidden() is False:
            self.hide()
        elif self.isHidden() is True:
            self.show()

    def open_settings(self):
        self.settings = SettingsWindow(self)
        self.settings.show()


app = QApplication(sys.argv)
window = SessionTesterWindow()
window.show()
sys.exit(app.exec_())
