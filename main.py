from ram import Ram
from cpu import Cpu
from gui import *
import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.QtCore import QTimer



df = Cpu.initiateMonitor()
# while True:
#
#
#     df.loc[len(df)] = Cpu.getThreadUsage()
#
#     print(df)



class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # starting text
        self.ui.textBrowser.setText(str(Cpu.getThreadUsage()))

        # timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()

        self.timer.timeout.connect(self.update)
    def update(self):

        self.ui.textBrowser.setText(str(Cpu.getThreadUsage()))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())