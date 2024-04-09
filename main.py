import ctypes, sys
import threading


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    pass
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(1)

from gui import *
from CsvWriter import *
from disk import *
from errors import *
import time
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
from testSelect import Tests


class WorkerThread(QThread):
    result_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

    def run(self):

        while True:
            start = time.time()

            # cpu
            cpu_thread = Cpu.get_thread_usage()
            cpu_thread_formated = Cpu.get_formated_thread_usage(cpu_thread)
            cpu_temp = Cpu.get_cpus_temp()
            print("cpu time: ", time.time() - start)

            # ram
            start_ram = time.time()
            ram_percent = Ram.get_ram_percentage()
            ram_used = Ram.get_ram_used()
            ram_total = Ram.get_ram_total()
            print("ram time: ", time.time() - start_ram)

            # gpu
            start_gpu = time.time()
            gpu_load = Gpu.get_gpu_load()
            gpu_memory = Gpu.get_gpu_memory_used()
            gpu_temp = Gpu.get_gpu_temp()
            print("gpu time: ", time.time() - start_gpu)

            # disk speed in MB/s
            start_disk = time.time()
            # diskRead, diskWrite, diskTotal = Disk.diskIOSpeed()
            disk_read, disk_write, disk_total, disk_wait_time, disk_queue, disk_usage = Disk.disk_info()
            print("disk time: ", time.time() - start_disk)

            # errors
            whea_error = errors.get_whea_value()

            parameters_dict = {
                "cpu_thread": cpu_thread,
                "cpu_thread_formated": cpu_thread_formated,
                "cpu_temp": cpu_temp,
                "ram_percent": ram_percent,
                "ram_used": ram_used,
                "ram_total": ram_total,

                "gpu_load": gpu_load,
                "gpu_memory": gpu_memory,
                "gpu_temp": gpu_temp,

                "disk_read": disk_read,
                "disk_write": disk_write,
                "disk_total": disk_total,
                "disk_wait_time": disk_wait_time,
                "disk_queue": disk_queue,
                "disk_usage": disk_usage,

                "whea_error": whea_error

            }
            self.result_signal.emit(parameters_dict)
            end = time.time()

            print("time of geating measurments: ", end - start)
            # update every two seconds
            try:
                time.sleep(2 - (end - start))
            except:
                pass


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.csv = CsvWriter()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # buttons
        self.ui.StartLogging.clicked.connect(self.clicked_start_logging)
        self.ui.EndLogging.clicked.connect(self.clicked_end_logging)
        self.ui.startTest.clicked.connect(self.manage_test)
        # logging
        self.isLogging = False

        # measure threat
        self.my_thread = WorkerThread()
        self.my_thread.result_signal.connect(self.update)
        self.my_thread.start()

        # initial values
        self.tests = Tests()
        self.testTime = ""

        # combbox for tests
        for t in self.tests.tests:
            self.ui.comboBoxTests.addItem(f'{t}')

        self.ui.textBrowserGpuName.setText(str(Gpu.get_gpu_name()))
        self.ui.textBrowserDiskModel.setText(str(Disk.get_hard_drive_model()))

    def update(self, values={}):

        start = time.time()

        cpu_thread_formated = values["cpu_thread_formated"]
        cpu_temp = values["cpu_temp"]

        self.ui.textBrowserCpu.setText(str(cpu_thread_formated))
        self.ui.textBrowserCpuTemp.setText(str(cpu_temp))
        self.ui.textBrowserTestTime.setText(str(self.testTime))

        # ram
        ram_percent = values["ram_percent"]
        ram_used = values["ram_used"]
        ram_total = values["ram_total"]

        self.ui.textBrowserRamPercent.setText(str(ram_percent))
        self.ui.textBrowserRamUsed.setText(str(ram_used))
        self.ui.textBrowserRamTotal.setText(str(ram_total))

        # gpu
        gpu_load = values["gpu_load"]
        gpu_memory = values["gpu_memory"]
        gpu_temp = values["gpu_temp"]

        self.ui.textBrowserGpuLoad.setText(str(gpu_load))
        self.ui.textBrowserGpuMemory.setText(str(gpu_memory))
        self.ui.textBrowserGpuTemp.setText(str(gpu_temp))

        # disk in MB/s
        disk_read = values["disk_read"]
        disk_write = values["disk_write"]
        disk_total = values["disk_total"]
        disk_wait = values["disk_wait_time"]
        disk_queue = values["disk_queue"]
        disk_usage = values["disk_usage"]

        self.ui.textBrowserDiskReadSpeed.setText(str(disk_read))
        self.ui.textBrowserDiskWriteSpeed.setText(str(disk_write))
        self.ui.textBrowserDiskTotalSpeed.setText(str(disk_total))
        self.ui.textBrowserDiskWaitTime.setText(str(disk_wait))
        self.ui.textBrowserDiskQueue.setText(str(disk_queue))
        self.ui.textBrowserDiskUsage.setText(str(disk_usage))

        # errors
        if values["whea_error"]:
            err = "Detected hardware error!"
        else:
            err = "No error detected"

        self.ui.textBrowserWHEA.setText(err)

        # if logging is enabled
        if self.isLogging:
            self.csv.update(values)

        end = time.time()
        print("gui update time: ", end - start)

    # button functions
    def manage_test(self):
        thread = threading.Thread(target=self.start_test, args=(self.ui.comboBoxTests.currentText(),))
        thread.start()

        self.ui.textBrowserTestTime.setText("Execution test...")
        self.testTime = "Execution test..."

    def start_test(self, test_path):
        self.ui.startTest.setEnabled(False)

        time = self.tests.run_using_specyfic_python(test_path)

        self.ui.startTest.setEnabled(True)
        print("czas testu do wyswietlenia", str(time), type(str(time)))

        self.testTime = time


    def clicked_start_logging(self):
        self.isLogging = True
        self.ui.StartLogging.setEnabled(False)
        self.ui.EndLogging.setEnabled(True)

    def clicked_end_logging(self):
        self.isLogging = False
        self.ui.StartLogging.setEnabled(True)
        self.ui.EndLogging.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
