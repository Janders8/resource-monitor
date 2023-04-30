from ram import Ram
from cpu import Cpu
from test import *
import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.textBrowser.setText("test")


df = Cpu.initiateMonitor()

# while True:
#
#
#     df.loc[len(df)] = Cpu.getThreadUsage()
#
#     print(df)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())