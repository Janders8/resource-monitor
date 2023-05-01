from ram import Ram
from cpu import Cpu
from gpu import Gpu
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
        #cpu
        self.ui.textBrowserCpu.setText(str(Cpu.getFormatedThreadUsage()))
        self.ui.textBrowserRamPercent.setText(str(Ram.getRamPercentage()))
        #ram
        self.ui.textBrowserRamUsed.setText(str(Ram.getRamUsed()))
        self.ui.textBrowserRamTotal.setText(str(Ram.getRamTotal()))
        #gpu
        #if gpu exist
        self.ui.textBrowserGpuName.setText(str(Gpu.getGpuName()))
        self.ui.textBrowserGpuLoad.setText(str(Gpu.getGpuLoad()))
        self.ui.textBrowserGpuMemory.setText(str(Gpu.getGpuMemoryUsed()))
        self.ui.textBrowserGpuTemp.setText(str(Gpu.getGpuTemp()))

        # timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update)

    def update(self):
        #cpu
        self.ui.textBrowserCpu.setText(str(Cpu.getFormatedThreadUsage()))
        self.ui.textBrowserRamPercent.setText(str(Ram.getRamPercentage()))
        #ram
        self.ui.textBrowserRamUsed.setText(str(Ram.getRamUsed()))
        self.ui.textBrowserRamTotal.setText(str(Ram.getRamTotal()))
        #gpu
        self.ui.textBrowserGpuName.setText(str(Gpu.getGpuName()))
        self.ui.textBrowserGpuLoad.setText(str(Gpu.getGpuLoad()))
        self.ui.textBrowserGpuMemory.setText(str(Gpu.getGpuMemoryUsed()))
        self.ui.textBrowserGpuTemp.setText(str(Gpu.getGpuTemp()))

df = Cpu.initiateMonitor()
print(str(df.columns))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window(Cpu.getLogicalCpus())
    win.show()
    sys.exit(app.exec())