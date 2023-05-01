from ram import Ram
from cpu import Cpu
from gpu import Gpu
from gui import *
from CsvWriter import *
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




        # timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update)

        #buttons
        self.ui.StartLogging.clicked.connect(self.clickedStartLogging)
        self.ui.EndLogging.clicked.connect(self.clickedEndLogging)

        #logging
        self.isLogging = False

    def update(self):



        # updating display
        #cpu
        cpuThread = Cpu.getThreadUsage()
        cpuThreadFormated = Cpu.getFormatedThreadUsage(cpuThread)
        cpuTemp = Cpu.getCpusTemp()


        self.ui.textBrowserCpu.setText(str(cpuThreadFormated))
        self.ui.textBrowserCpuTemp.setText(str(cpuTemp))


        #ram
        ramPercent = Ram.getRamPercentage()
        ramUsed = Ram.getRamUsed()
        ramTotal = Ram.getRamTotal()

        self.ui.textBrowserRamPercent.setText(str(ramPercent))
        self.ui.textBrowserRamUsed.setText(str(ramUsed))
        self.ui.textBrowserRamTotal.setText(str(ramTotal))
        #gpu

        gpuLoad = Gpu.getGpuLoad()
        gpuMemory = Gpu.getGpuMemoryUsed()
        gpuTemp = Gpu.getGpuTemp()

        self.ui.textBrowserGpuName.setText(str(Gpu.getGpuName()))
        self.ui.textBrowserGpuLoad.setText(str(gpuLoad))
        self.ui.textBrowserGpuMemory.setText(str(gpuMemory))
        self.ui.textBrowserGpuTemp.setText(str(gpuTemp))

        # if logging is enabled
        if self.isLogging:
            df = self.csv.dfHeaders
            #print(df)

            # cpu
            #print(cpuThread)


            newRow = cpuThread + [ramPercent] + [ramUsed] + [ramTotal] + [gpuLoad] + [gpuMemory] + [gpuTemp]

            print(gpuMemory)

            df.loc[len(df)] = newRow

            df.to_csv(self.csv.fileName, mode="a", index=False, header = False)





    def clickedStartLogging(self):
        self.isLogging = True
        self.ui.StartLogging.setEnabled(False)
        self.ui.EndLogging.setEnabled(True)

        self.csv = CsvWriter()


    def clickedEndLogging(self):
        self.isLogging = False
        self.ui.StartLogging.setEnabled(True)
        self.ui.EndLogging.setEnabled(False)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window(Cpu.getLogicalCpus())
    win.show()
    sys.exit(app.exec())