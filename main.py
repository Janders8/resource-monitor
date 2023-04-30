from ram import Ram
from cpu import Cpu
from gui import *
import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QLabel, QTextBrowser
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
    def __init__(self, cpus, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # create threads fields
        #
        # labelList = []
        # textField = []
        #
        # for i in range(cpus):
        #     labelList.append((QLabel("thread_" + str(i))))
        #     #textField.append(QTextBrowser(self.ui.formLayoutWidget))
        #     #self.ui.formLayout.addRow(labelList[i], textField[i])




        # starting text
        self.ui.textBrowserCpu.setText(str(Cpu.getFormatedThreadUsage()))
        self.ui.textBrowserRamPercent.setText(str(Ram.getRamPercentage()))
        self.ui.textBrowserRamUsed.setText(str(Ram.getRamUsed()))
        self.ui.textBrowserRamTotal.setText(str(Ram.getRamTotal()))

        # timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update)

    def update(self):

        self.ui.textBrowserCpu.setText(str(Cpu.getFormatedThreadUsage()))
        self.ui.textBrowserRamPercent.setText(str(Ram.getRamPercentage()))
        self.ui.textBrowserRamUsed.setText(str(Ram.getRamUsed()))
        self.ui.textBrowserRamTotal.setText(str(Ram.getRamTotal()))

df = Cpu.initiateMonitor()
print(str(df.columns))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window(Cpu.getLogicalCpus())
    win.show()
    sys.exit(app.exec())