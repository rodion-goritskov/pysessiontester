import sys
from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4 import QtCore
from interface import Ui_MainAppWindow
from export_session import *
import datetime
import threading
import time


class SessionTesterWindow(QMainWindow, Ui_MainAppWindow):

    progress_bar_change = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)

        self.isStarted = False
        self.isPaused = True
        self.isRIP = False
        self.current_time = 0

        self.setupUi(self)
        self.sessionStartButton.clicked.connect(self.start_session)
        self.newSessionButton.clicked.connect(self.new_session)
        self.exportSessionButton.clicked.connect(self.export_session)
        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat("Session progress")

    def start_session(self):
        if self.isPaused is True:
            self.isPaused = False
            self.sessionStartButton.setText("Pause session")
            self.session_time = self.__count_session_time(self.sessionTimeField.time().toString("hh:mm:ss"))
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
        self.sessionStartButton.setText("Start session")
        self.current_time = 0
        self.isPaused = True

    def export_session(self):
        export_session_to_html(self.textEdit.toPlainText())

    def set_progress_bar(self):
        self.progressBar.setValue(self.current_time)
        self.progressBar.setFormat("Time left:" + str(datetime.timedelta(seconds=self.time_to_go)))

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
            self.sessionStartButton.setText("Start session")
            self.isPaused = True
            self.isRIP = True

    def __count_session_time(self, time_string):
        self.result_date = time_string.split(":")
        return (int(self.result_date[0])*3600) + (int(self.result_date[1])*60) + int(self.result_date[2])


app = QApplication(sys.argv)
window = SessionTesterWindow()
window.show()
sys.exit(app.exec_())
