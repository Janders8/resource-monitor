import pandas as pd

from ram import Ram
from cpu import Cpu
from gpu import Gpu
from gui import *
from CsvWriter import *
from disk import *
import time
import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QLabel, QTextBrowser
)
from PyQt5.QtCore import QTimer, QThread, pyqtSignal





# while True:
#
#
#     df.loc[len(df)] = Cpu.getThreadUsage()
#
#     print(df)

from PyQt5.QtCore import QThread

class MyThread(QThread):
    my_signal = pyqtSignal(dict)
    def __init__(self):
        super().__init__()

    def run(self):

        while True:
            start = time.time()
            # cpu
            cpuCore = Cpu.getCoreUsage()
            cpuCoreFormated = Cpu.getFormatedCoreUsage(cpuCore)
            cpuTemp = Cpu.getCpusTemp()



            # ram
            ramPercent = Ram.getRamPercentage()
            ramUsed = Ram.getRamUsed()
            ramTotal = Ram.getRamTotal()

            # gpu
            gpuLoad = Gpu.getGpuLoad()
            gpuMemory = Gpu.getGpuMemoryUsed()
            gpuTemp = Gpu.getGpuTemp()



            # disk speed in MB/s
            diskRead, diskWrite, diskTotal = Disk.diskIOSpeed()

            dict = {
                "cpuCore" : cpuCore,
                "cpuCoreFormated" : cpuCoreFormated,
                "cpuTemp" : cpuTemp,

                "ramPercent" : ramPercent,
                "ramUsed" : ramUsed,
                "ramTotal" : ramTotal,

                "gpuLoad" : gpuLoad,
                "gpuMemory" : gpuMemory,
                "gpuTemp" : gpuTemp,

                "diskRead" : diskRead,
                "diskWrite" : diskWrite,
                "diskTotal" : diskTotal


            }
            end = time.time()
            print(2 - (end-start))
            time.sleep(2 - (end-start))


            print("worker time: ", end - start)
            self.my_signal.emit(dict)



            #time.sleep(1)





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

        # disk monitor
        self.diskMonitor = Disk()


        # timer
        # self.timer = QTimer()
        # self.timer.setInterval(1000)
        # self.timer.start()
        # self.timer.timeout.connect(self.update)

        #buttons
        self.ui.StartLogging.clicked.connect(self.clickedStartLogging)
        self.ui.EndLogging.clicked.connect(self.clickedEndLogging)

        #logging
        self.isLogging = False

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.update)
        self.my_thread.start()


    def update(self, values = {}):

        start = time.time()




        # updating display
        #cpu
        # cpuThread = Cpu.getThreadUsage()
        # cpuThreadFormated = Cpu.getFormatedThreadUsage(cpuThread)


        cpuCore = values["cpuCore"]
        cpuCoreFormated = values["cpuCoreFormated"]
        cpuTemp = values["cpuTemp"]


        self.ui.textBrowserCpu.setText(str(cpuCoreFormated))
        self.ui.textBrowserCpuTemp.setText(str(cpuTemp))


        #ram
        ramPercent = values["ramPercent"]
        ramUsed = values["ramUsed"]
        ramTotal = values["ramTotal"]

        self.ui.textBrowserRamPercent.setText(str(ramPercent))
        self.ui.textBrowserRamUsed.setText(str(ramUsed))
        self.ui.textBrowserRamTotal.setText(str(ramTotal))
        #gpu

        gpuLoad = values["gpuLoad"]
        gpuMemory = values["gpuMemory"]
        gpuTemp = values["gpuTemp"]

        self.ui.textBrowserGpuName.setText(str(Gpu.getGpuName()))
        self.ui.textBrowserGpuLoad.setText(str(gpuLoad))
        self.ui.textBrowserGpuMemory.setText(str(gpuMemory))
        self.ui.textBrowserGpuTemp.setText(str(gpuTemp))

        #disk in MB/s
        # read, write, total = self.diskMonitor.diskIOSpeed()
        #

        diskRead = values["diskRead"]
        diskWrite = values["diskWrite"]
        diskTotal = values["diskTotal"]

        self.ui.textBrowserDiskReadSpeed.setText(str(diskRead))
        self.ui.textBrowserDiskWriteSpeed.setText(str(diskWrite))
        self.ui.textBrowserDiskTotalSpeed.setText(str(diskTotal))



        # if logging is enabled
        if self.isLogging:
            #empty dataframe with headers
            self.csv.dfHeaders.drop(self.csv.dfHeaders.index,inplace=True)

            # create new row
            newRow = cpuCore + [cpuTemp] + [ramPercent] + [ramUsed] + [ramTotal] + [gpuLoad] + [gpuMemory] + [gpuTemp]
            #add new row
            self.csv.dfHeaders.loc[len(self.csv.dfHeaders)] = newRow

            print(self.csv.dfHeaders)

            # save new row
            self.csv.dfHeaders.to_csv(self.csv.fileName, mode="a", index=False, header = False)

        end = time.time()
        print("update: " , end-start)



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