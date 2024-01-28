# admin acces windows
import ctypes, sys
import threading

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# if is_admin():
#     pass
# else:
#     # Re-run the program with admin rights
#     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#     sys.exit(1)


import pandas as pd
from ram import Ram
from cpu import Cpu
from gpu import Gpu
from gui import *
from CsvWriter import *
from disk import *
from errors import *
import time
import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QLabel, QTextBrowser
)
from PyQt5.QtCore import pyqtSignal


from PyQt5.QtCore import QThread

from testSelect import Tests

class MyThread(QThread):
    my_signal = pyqtSignal(dict)
    def __init__(self):
        super().__init__()

    def run(self):

        while True:
            start = time.time()
            # cpu cores
            # cpuCore = Cpu.getCoreUsage()
            # cpuCoreFormated = Cpu.getFormatedCoreUsage(cpuCore)
            # cpuTemp = Cpu.getCpusTemp()
            # print("cpu time: ", time.time() - start)

            cpuThread = Cpu.getThreadUsage()
            cpuThreadFormated = Cpu.getFormatedThreadUsage(cpuThread)
            cpuTemp = Cpu.getCpusTemp()
            #cpuErrors = Cpu.getCpuErrors()

            print("cpu time: ", time.time() - start)


            # ram
            startRam = time.time()
            ramPercent = Ram.getRamPercentage()
            ramUsed = Ram.getRamUsed()
            ramTotal = Ram.getRamTotal()
            print("ram time: ", time.time() - startRam)

            # gpu
            startGpu = time.time()
            gpuLoad = Gpu.getGpuLoad()
            gpuMemory = Gpu.getGpuMemoryUsed()
            gpuTemp = Gpu.getGpuTemp()
            print("gpu time: ", time.time() - startGpu)



            # disk speed in MB/s
            startDisk = time.time()
            #diskRead, diskWrite, diskTotal = Disk.diskIOSpeed()
            diskRead, diskWrite, diskTotal, diskWaitTime, diskQueue, diskUsage = Disk.diskInfo()
            print("disk time: ", time.time() - startDisk)

            #errors
            wheaError = errors.getWheaValue()

            dict = {
                # "cpuCore" : cpuCore,
                # "cpuCoreFormated" : cpuCoreFormated,
                "cpuThread" : cpuThread,
                "cpuThreadFormated" : cpuThreadFormated,
                "cpuTemp" : cpuTemp,
                #"cpuErrors" : cpuErrors,

                "ramPercent" : ramPercent,
                "ramUsed" : ramUsed,
                "ramTotal" : ramTotal,

                "gpuLoad" : gpuLoad,
                "gpuMemory" : gpuMemory,
                "gpuTemp" : gpuTemp,

                "diskRead" : diskRead,
                "diskWrite" : diskWrite,
                "diskTotal" : diskTotal,
                "diskWaitTime" : diskWaitTime,
                "diskQueue" : diskQueue,
                "diskUsage" : diskUsage,

                "wheaError" : wheaError


            }
            self.my_signal.emit(dict)
            end = time.time()

            print("time of geating measurments: ", end-start)
            #update every two seconds
            try:
                time.sleep(2 - (end-start))
            except:
                pass


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
        # self.timer = QTimer()
        # self.timer.setInterval(1000)
        # self.timer.start()
        # self.timer.timeout.connect(self.update)

        #buttons
        self.ui.StartLogging.clicked.connect(self.clickedStartLogging)
        self.ui.EndLogging.clicked.connect(self.clickedEndLogging)
        self.ui.startTest.clicked.connect(self.manageTest)
        #logging
        self.isLogging = False

        #measure threat
        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.update)
        self.my_thread.start()

        #initial values
        self.tests = Tests()
        self.testTime = ""

        # combbox for tests
        for t in self.tests.tests:
            self.ui.comboBoxTests.addItem(f'{t}')

        self.ui.textBrowserGpuName.setText(str(Gpu.getGpuName()))
        self.ui.textBrowserDiskModel.setText(str(Disk.get_hard_drive_model()))



    def update(self, values = {}):

        start = time.time()

        # updating display
        #cpu
        # cpuThread = Cpu.getThreadUsage()
        # cpuThreadFormated = Cpu.getFormatedThreadUsage(cpuThread)


        # cpuCore = values["cpuCore"]
        # cpuCoreFormated = values["cpuCoreFormated"]

        cpuThread = values["cpuThread"]
        cpuThreadFormated = values["cpuThreadFormated"]
        cpuTemp = values["cpuTemp"]
        #cpuErrors = values["cpuErrors"]


        self.ui.textBrowserCpu.setText(str(cpuThreadFormated))
        self.ui.textBrowserCpuTemp.setText(str(cpuTemp))
        #self.ui.textBrowserCpuErrors.setText(str(cpuErrors))

        self.ui.textBrowserTestTime.setText(str(self.testTime))


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


        self.ui.textBrowserGpuLoad.setText(str(gpuLoad))
        self.ui.textBrowserGpuMemory.setText(str(gpuMemory))
        self.ui.textBrowserGpuTemp.setText(str(gpuTemp))

        #disk in MB/s
        # read, write, total = self.diskMonitor.diskIOSpeed()
        #

        diskRead = values["diskRead"]
        diskWrite = values["diskWrite"]
        diskTotal = values["diskTotal"]
        diskWait = values["diskWaitTime"]
        diskQueue = values["diskQueue"]
        diskUsage = values["diskUsage"]

        self.ui.textBrowserDiskReadSpeed.setText(str(diskRead))
        self.ui.textBrowserDiskWriteSpeed.setText(str(diskWrite))
        self.ui.textBrowserDiskTotalSpeed.setText(str(diskTotal))
        self.ui.textBrowserDiskWaitTime.setText(str(diskWait))
        self.ui.textBrowserDiskQueue.setText(str(diskQueue))
        self.ui.textBrowserDiskUsage.setText(str(diskUsage))

        #errors
        if values["wheaError"]:
            err = "wykryto błąd!"
        else:
            err = "nie wykryto błędu"

        self.ui.textBrowserWHEA.setText(err)




        # if logging is enabled
        if self.isLogging:
            self.csv.update(values)

        end = time.time()
        print("gui update time: " , end-start)

    # button functions

    def manageTest(self):
        thread = threading.Thread(target=self.__startTest, args= (self.ui.comboBoxTests.currentText(),))
        thread.start()

        self.ui.textBrowserTestTime.setText("Execution test...")
        self.testTime = "Execution test..."

    def __startTest(self, testPath):
        self.ui.startTest.setEnabled(False)

        time = self.tests.runUsingSpecyficPython(testPath)

        self.ui.startTest.setEnabled(True)
        print("czas testu do wyswietlenia", str(time), type(str(time)))

        # simple time update doesnt work, i think ith should by in main thread
        self.testTime = time
        #self.ui.textBrowserTestTime.setText(str(time))




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