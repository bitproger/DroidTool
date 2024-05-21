from gui import Ui_MainWindow
from PyQt6 import QtWidgets
import sys
import os
import subprocess
import adb

class MainWindow(QtWidgets.QMainWindow):
    def reboot(self):
        adb.reboot(self.ui.SelectorTypeReboot.currentText())
    def install(self):
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        adb.install(path)

    def check(self):
        if len(adb.check()) == 4:
            self.ui.StatusConn.setText("ОТКЛЮЧЕНО")
            self.ui.RebootBtn.setEnabled(False)
            self.ui.SelectorTypeReboot.setEnabled(False)
            self.ui.InstallBtn.setEnabled(False)
        else:
            self.ui.StatusConn.setText(adb.check()[4])
            self.ui.RebootBtn.setEnabled(True)
            self.ui.SelectorTypeReboot.setEnabled(True)
            self.ui.InstallBtn.setEnabled(True)
        adb.check()
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.SearchBtn.clicked.connect(self.check)
        self.ui.InstallBtn.clicked.connect(self.install)
        self.ui.RebootBtn.clicked.connect(self.reboot)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())