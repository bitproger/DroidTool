import fastboot
from gui import Ui_MainWindow
from PyQt6 import QtWidgets
import sys
import os
import subprocess
import adb

class MainWindow(QtWidgets.QMainWindow):
    def check_FB(self):
        if len(fastboot.check()):
            self.ui.StatusConn_FB.setText(fastboot.check()[0])
            self.ui.RebootBtn_FB.setEnabled(True)
            self.ui.SelectorTypeReboot_FB.setEnabled(True)
        else:
            self.ui.StatusConn_FB.setText("ОТКЛЮЧЕНО")
            self.ui.RebootBtn_FB.setEnabled(False)
            self.ui.SelectorTypeReboot_FB.setEnabled(False)

    def reboot_FB(self):
        fastboot.reboot(self.ui.SelectorTypeReboot_FB.currentText())

    def reboot(self):
        adb.reboot(self.ui.SelectorTypeReboot.currentText())
    def install(self):
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        adb.install(path)
    def remove(self):
        appr = self.ui.RemoveSelector.currentText()
        adb.remove(appr)

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
            self.ui.RemoveSelector.setEnabled(True)
            self.ui.DelButton.setEnabled(True)
            for i in adb.list_apps():
                self.ui.RemoveSelector.addItem(i.split(":")[1])
        adb.check()
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.SearchBtn.clicked.connect(self.check)
        self.ui.InstallBtn.clicked.connect(self.install)
        self.ui.RebootBtn.clicked.connect(self.reboot)
        self.ui.SearchBtn_FB.clicked.connect(self.check_FB)
        self.ui.RebootBtn_FB.clicked.connect(self.reboot_FB)
        self.ui.DelButton.clicked.connect(self.remove)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())